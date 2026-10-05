#!/usr/bin/env python3
"""Audit all yeast GO-CAM activity locations against pinned native protein evidence.

Location annotations describe physical entities. They do not automatically place
every activity of a protein in each compartment. Only the explicitly inspected
functional assertions below generate new activity locations. Conflicting generic
cytosol assertions are quarantined in the complete source-exclusion ledger.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sqlite3
from collections import Counter
from pathlib import Path

import yaml
from review_gocam_graphs import IndentedDumper

from pathwaymech.schema import validate_record

SOURCE_SHA = "95f72dcc644358c480e0e59f996cf88533558b5fa4256460a030e0a1eaf9678d"
# Inspected native UniProt location vocabulary -> GO cellular components.
# Microsomes are an experimental fraction, not an in-vivo organelle; the GO
# microsome class is obsolete. Retain these source facts in the audit only.
LOCATION_MAP = {
    "SL-0086": "GO:0005737",
    "SL-0091": "GO:0005829",
    "SL-0171": "GO:0031966",
    "SL-0169": "GO:0005758",
    "SL-0170": "GO:0005759",
    "SL-0168": "GO:0005743",
    "SL-0204": "GO:0005777",
    "SL-0039": "GO:0005886",
    "SL-0029": "GO:0005935",
    "SL-0089": "GO:0030659",
    "SL-0162": "GO:0016020",
    "SL-0097": "GO:0005789",
    "SL-0166": None,
    "SL-0165": None,
    "SL-0154": "GO:0005811",
    "SL-0173": "GO:0005739",
    "SL-0191": "GO:0005634",
    "SL-0203": "GO:0005778",
    "SL-0172": "GO:0005741",
    "SL-0271": "GO:0005774",
    "SL-0090": "GO:0005856",
    "SL-0243": "GO:0005576",
    "SL-0200": "GO:0042597",
    "SL-0178": "GO:0005635",
    "SL-0272": "GO:0005773",
    "SL-0095": "GO:0005783",
    "SL-0134": "GO:0000139",
    "SL-0100": "GO:0010008",
    "SL-0267": "GO:0032588",
    "SL-0266": "GO:0005802",
    "SL-0008": "GO:0030479",
    "SL-0151": "GO:0031902",
    "SL-0136": "GO:0032580",
    "SL-0202": "GO:0005782",
}

# These are bounded, manually inspected FUNCTION assertions, not keyword rules.
# The snippet is also a guard against changed upstream semantics on replay.
# General sterol-module boilerplate is deliberately not projected to each enzyme.
ACTIVITY_LOCATIONS = {
    "P40350": [("GO:0005789", "Endoplasmic reticulum membrane-bound UDP-glucose")],
    "Q08558": [("GO:0005777", "Peroxisomal di-isomerase")],
    "Q05902": [("GO:0005773", "turnover of the vacuolar GSH")],
    "P36013": [("GO:0005739", "NAD-dependent mitochondrial malic enzyme")],
    "P09440": [("GO:0005739", "Mitochondrial isozyme of C-1-tetrahydrofolate synthase")],
    "P35731": [("GO:0005739", "biosynthesis of fatty acids in mitochondria")],
    "P40857": [("GO:0005789", "endoplasmic reticulum-bound enzymatic process")],
    "Q99190": [("GO:0005789", "endoplasmic reticulum-bound enzymatic process")],
    "P42837": [("GO:0005774", "turnover of PtdIns(3,5)P2 at the vacuole membrane")],
    "P33333": [("GO:0005811", "to phosphatidic acid (PA) in lipid particles")],
    "P39006": [("GO:0005739", "Phosphatidylethanolamine formed in the mitochondria")],
    "P53037": [
        ("GO:0000139", "site of PtdEtn synthesis on the Golgi/endosome membranes"),
        ("GO:0010008", "site of PtdEtn synthesis on the Golgi/endosome membranes"),
    ],
}
COMPLEX_LOCATIONS = {
    "SGD:S000218158": (
        "CPX-1268",
        "GO:0005739",
        "Located in the mitochondrion.",
        "e4fe5081d0a6516ee143b07c7e6cba8f584140019c9d5eaefefaaf770559764b",
    ),
    "SGD:S000218211": (
        "CPX-1739",
        "GO:0005794",
        "Function in the Golgi.",
        "5d1054a984220288b54c85c6c3f690a2bd9bc675ebb80943208912e96a5e3794",
    ),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_locator(provenance, index, suffix):
    return f"{provenance['url']}#/results/{index}{suffix}; sha256={provenance['sha256']}"


def evidence_codes(value):
    return (
        "; ".join(
            item["evidenceCode"]
            + (f" ({item['source']}:{item['id']})" if item.get("source") else "")
            for item in value.get("evidences", [])
        )
        or "evidence code not specified by source"
    )


def protein_index(source):
    result = {}
    ambiguous = set()
    for index, protein in enumerate(source["results"]):
        if (
            protein["organism"]["taxonId"] != 559292
            or protein["entryType"] != "UniProtKB reviewed (Swiss-Prot)"
        ):
            raise ValueError("Expected reviewed S288C protein source")
        keys = ["UniProtKB:" + protein["primaryAccession"]]
        keys += [
            "SGD:" + x["id"]
            for x in protein.get("uniProtKBCrossReferences", [])
            if x["database"] == "SGD"
        ]
        for key in keys:
            if key in result:
                del result[key]
                ambiguous.add(key)
            elif key not in ambiguous:
                result[key] = index, protein
    return result, ambiguous


def locations(protein):
    result = []
    for ci, comment in enumerate(protein.get("comments", [])):
        if comment["commentType"] != "SUBCELLULAR LOCATION":
            continue
        for li, location in enumerate(comment.get("subcellularLocations", [])):
            native = location["location"]
            if native["id"] not in LOCATION_MAP:
                raise ValueError(f"Unreviewed native location: {native}")
            result.append(
                {
                    "comment_index": ci,
                    "location_index": li,
                    "annotation": location,
                    "comment": comment,
                    "go_id": LOCATION_MAP[native["id"]],
                }
            )
    return result


def curate(record, proteins, provenance, labels, complexes):
    report = {
        "record_id": record["id"],
        "proteins": [],
        "activity_locations": [],
        "excluded_source_edges": [],
        "new_edges": [],
    }
    participants = {node["id"]: node for node in record["participants"]}
    references = {ref["id"]: ref for ref in record["references"]}
    edges = {(e["subject"], e["predicate"], e["object"]): e for e in record["mechanistic_edges"]}

    def node(identifier):
        participants.setdefault(
            identifier,
            {"id": identifier, "label": labels[identifier], "category": "cellular_component"},
        )

    def add(subject, predicate, obj, evidence, description):
        key = subject, predicate, obj
        if key in edges:
            for item in evidence:
                if item not in edges[key]["evidence"]:
                    edges[key]["evidence"].append(item)
            return
        edge = {
            "id": "location-" + hashlib.sha256("|".join(key).encode()).hexdigest()[:12],
            "subject": subject,
            "predicate": predicate,
            "object": obj,
            "description": description,
            "evidence": evidence,
        }
        edges[key] = edge
        report["new_edges"].append(edge["id"])

    def ref(protein):
        accession = protein["primaryAccession"]
        identifier = "UniProtKB:" + accession
        references.setdefault(
            identifier,
            {
                "id": identifier,
                "title": f"Reviewed UniProtKB {accession} location annotations",
                "url": provenance["url"],
                "source_version": "UniProt release 2026_03",
                "source_sha256": provenance["sha256"],
            },
        )
        return identifier

    known = {}
    for identifier in list(participants):
        if identifier not in proteins:
            continue
        index, protein = proteins[identifier]
        annotations = locations(protein)
        known[identifier] = annotations
        report["proteins"].append(
            {
                "id": identifier,
                "accession": protein["primaryAccession"],
                "source_index": index,
                "locations": annotations,
            }
        )
        for annotation in annotations:
            go_id = annotation["go_id"]
            if not go_id:
                continue
            ci, li = annotation["comment_index"], annotation["location_index"]
            location, comment = annotation["annotation"], annotation["comment"]
            native = location["location"]
            node(go_id)
            participants[identifier]["category"] = "protein"
            context = f"; molecular form: {comment['molecule']}" if comment.get("molecule") else ""
            evidence = [
                {
                    "reference_id": ref(protein),
                    "source_assertion": (
                        f"UniProtKB:{protein['primaryAccession']} annotates location "
                        f"{native['value']} ({native['id']}){context}."
                    ),
                    "source_locator": source_locator(
                        provenance, index, f"/comments/{ci}/subcellularLocations/{li}"
                    ),
                }
            ]
            if identifier.startswith("SGD:"):
                xi = next(
                    i
                    for i, x in enumerate(protein["uniProtKBCrossReferences"])
                    if x["database"] == "SGD" and "SGD:" + x["id"] == identifier
                )
                evidence.append(
                    {
                        "reference_id": ref(protein),
                        "source_assertion": (
                            f"UniProtKB:{protein['primaryAccession']} has the exact "
                            f"SGD cross-reference {identifier}."
                        ),
                        "source_locator": source_locator(
                            provenance, index, f"/uniProtKBCrossReferences/{xi}"
                        ),
                    }
                )
            description = "Physical protein location from reviewed UniProt. " + evidence_codes(
                native
            )
            if context:
                description += context + "."
            for detail in ("topology", "orientation"):
                if detail in location:
                    description += f" {detail.capitalize()}: {location[detail]['value']}."
            for text in comment.get("note", {}).get("texts", []):
                description += " Source qualification: " + text["value"]
            add(identifier, "located_in", go_id, evidence, description)

    activity_ids = {n["id"] for n in record["reactions"]}
    for activity in sorted(activity_ids):
        enablers = [
            e["subject"]
            for e in record["mechanistic_edges"]
            if e["object"] == activity and e["predicate"] in ("enables", "catalyzes")
        ]
        # Chemical cofactors can enable an activity too; only physical catalyst
        # identities are relevant to the compartment comparison.
        enablers = [
            i
            for i in enablers
            if i in proteins
            or i.startswith(("SGD:", "UniProtKB:"))
            or participants.get(i, {}).get("category") in ("protein", "complex")
        ]
        original = [
            copy.deepcopy(e)
            for e in record["mechanistic_edges"]
            if e["subject"] == activity and e["predicate"] == "occurs_in"
        ]
        states = {}
        for identifier in enablers:
            locs = known.get(identifier, [])
            names = [a["annotation"]["location"]["value"] for a in locs]
            if identifier in COMPLEX_LOCATIONS:
                states[identifier] = "explicit_noncytosolic_function"
            elif any(n == "Cytoplasm" or n.startswith("Cytoplasm,") for n in names):
                states[identifier] = "compatible_cytoplasmic_location"
            elif any(a["go_id"] for a in locs):
                states[identifier] = "noncytoplasmic_location_only"
            else:
                states[identifier] = "no_independent_location"
        quarantined = bool(states) and all(
            s in ("explicit_noncytosolic_function", "noncytoplasmic_location_only")
            for s in states.values()
        )
        action = "retained_native_location"
        if quarantined:
            key = activity, "occurs_in", "GO:0005829"
            if key in edges:
                excluded = edges.pop(key)
                report["excluded_source_edges"].append(
                    {
                        "edge": excluded,
                        "reason": (
                            "Generic native cytosol assertion is not accepted as a definite "
                            "activity location: every resolved catalyst has only organellar, "
                            "membrane, nuclear or extracellular annotations. Physical locations "
                            "are retained separately; a replacement activity location requires "
                            "an explicit functional assertion. Membrane attachment does not itself "
                            "rule out a cytosolic catalytic face."
                        ),
                        "catalyst_audit": states,
                    }
                )
                action = "quarantined_conflicting_cytosol"
        elif any(s == "noncytoplasmic_location_only" for s in states.values()):
            action = "retained_mixed_or_unresolved_isoenzyme_location"
            key = activity, "occurs_in", "GO:0005829"
            if key in edges:
                edges[key]["description"] = (
                    "Native activity-level cytosol assertion retained for a reaction with "
                    "alternative enablers. It does not place every isoenzyme in the cytosol; "
                    "separate located_in edges describe the individual protein annotations."
                )
        elif not states or any(s == "no_independent_location" for s in states.values()):
            action = "retained_native_location_independent_gap"
        report["activity_locations"].append(
            {
                "activity": activity,
                "enablers": states,
                "source_locations": original,
                "action": action,
            }
        )

        for identifier in enablers:
            if identifier in COMPLEX_LOCATIONS:
                cpx, go_id, snippet, _ = COMPLEX_LOCATIONS[identifier]
                if snippet not in complexes[cpx]["functions"][0]:
                    raise ValueError(f"Changed complex functional source: {cpx}")
                node(go_id)
                add(
                    activity,
                    "occurs_in",
                    go_id,
                    [
                        {
                            "reference_id": identifier,
                            "source_assertion": (
                                f"Complex Portal {cpx} places this complex's catalytic function "
                                f"in the {labels[go_id]}."
                            ),
                            "source_locator": f"{cpx}.json#/functions/0",
                        }
                    ],
                    "Functional compartment explicitly described by Complex Portal. "
                    + complexes[cpx]["evidenceType"]["identifier"]
                    + ": "
                    + complexes[cpx]["evidenceType"]["description"]
                    + ".",
                )
                continue
            if identifier not in proteins:
                continue
            index, protein = proteins[identifier]
            for go_id, snippet in ACTIVITY_LOCATIONS.get(protein["primaryAccession"], []):
                matches = [
                    (ci, ti, text)
                    for ci, comment in enumerate(protein.get("comments", []))
                    if comment["commentType"] == "FUNCTION"
                    for ti, text in enumerate(comment["texts"])
                    if snippet in text["value"]
                ]
                if len(matches) != 1:
                    raise ValueError(f"Changed inspected functional source: {identifier} {snippet}")
                ci, ti, text = matches[0]
                node(go_id)
                add(
                    activity,
                    "occurs_in",
                    go_id,
                    [
                        {
                            "reference_id": ref(protein),
                            "source_assertion": (
                                f"UniProtKB:{protein['primaryAccession']} describes the "
                                f"corresponding catalytic function in the {labels[go_id]}; "
                                "this projection applies "
                                f"to the activity enabled by {identifier}."
                            ),
                            "source_locator": source_locator(
                                provenance, index, f"/comments/{ci}/texts/{ti}"
                            ),
                        }
                    ],
                    "Activity compartment supported by an inspected functional annotation. "
                    + evidence_codes(text)
                    + ". Alternative isoenzymes may function elsewhere.",
                )
    record["participants"] = list(participants.values())
    record["references"] = list(references.values())
    record["mechanistic_edges"] = list(edges.values())
    validate_record(record)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--uniprot-json", type=Path, required=True)
    parser.add_argument("--provenance", type=Path, required=True)
    parser.add_argument("--complex-dir", type=Path, required=True)
    parser.add_argument("--go-db", type=Path, required=True)
    parser.add_argument("--records", type=Path, default=Path("data/pathways"))
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    provenance = json.loads(args.provenance.read_text())
    if digest(args.uniprot_json) != SOURCE_SHA or provenance["sha256"] != SOURCE_SHA:
        raise ValueError("Location batch differs from inspected source")
    proteins, ambiguous = protein_index(json.loads(args.uniprot_json.read_text()))
    complexes = {}
    for cpx, _, _, sha in COMPLEX_LOCATIONS.values():
        path = args.complex_dir / (cpx + ".json")
        if digest(path) != sha:
            raise ValueError(f"Complex source mismatch: {cpx}")
        complexes[cpx] = json.loads(path.read_text())
    db = sqlite3.connect(f"file:{args.go_db}?mode=ro", uri=True)
    identifiers = set(LOCATION_MAP.values()) - {None}
    identifiers.update(v[1] for v in COMPLEX_LOCATIONS.values())
    labels = {}
    for identifier in identifiers:
        rows = db.execute(
            "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'", (identifier,)
        ).fetchall()
        if len(rows) != 1 or rows[0][0].startswith("obsolete"):
            raise ValueError(f"Invalid current GO location: {identifier}")
        labels[identifier] = rows[0][0]
    reports, pending = [], []
    for path in sorted(args.records.rglob("*.yaml")):
        record = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        if not record["id"].startswith("gomodel:") or not any(
            taxon["id"] == "NCBITaxon:559292" for taxon in record["taxa"]
        ):
            continue
        report = curate(record, proteins, provenance, labels, complexes)
        report["file"] = str(path)
        report["input_sha256"] = digest(path)
        reports.append(report)
        pending.append((path, record))
    if len(reports) != 85:
        raise ValueError(f"Expected complete 85-record yeast cohort, got {len(reports)}")
    result = {
        "source": provenance,
        "mapping": LOCATION_MAP,
        "excluded_ambiguous_protein_mappings": sorted(ambiguous),
        "records": reports,
        "summary": {
            "records": len(reports),
            "quarantined_cytosol": sum(len(r["excluded_source_edges"]) for r in reports),
            "added_edges": sum(len(r["new_edges"]) for r in reports),
            "activity_decisions": dict(
                Counter(a["action"] for r in reports for a in r["activity_locations"])
            ),
        },
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, indent=2) + "\n")
    if args.write:
        for path, record in pending:
            path.write_text(
                yaml.dump(
                    record, Dumper=IndentedDumper, sort_keys=False, allow_unicode=True, width=100
                )
            )
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
