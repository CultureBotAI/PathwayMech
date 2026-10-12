#!/usr/bin/env python3
"""Add inspected native Complex Portal composition to existing GO-CAM complexes.

All eight complex identities are anchored by the primary GO-CAM SGD class and
its CPX label. Existing protein nodes are reused only through exact reviewed
UniProt SGD cross-references. This avoids duplicate SGD/UniProt protein nodes.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

import yaml
from review_gocam_graphs import IndentedDumper, chebi_terms, digest

from pathwaymech.curation import changed_records, publish_curation
from pathwaymech.schema import validate_record

COMPLEXES = {
    "SGD:S000217821": (
        "CPX-3163",
        "0fcb89604504093cdb01bb1dbd77394bf0bd9c3488dfeedbabeb1434c49ed4e8",
    ),
    "SGD:S000217863": (
        "CPX-579",
        "ccbb1369177abe4083a66a31055b2e69ff26d38506e4c8a7e063ed786a2194cc",
    ),
    "SGD:S000217933": (
        "CPX-1102",
        "3b80bfeea3253ea8096bc19dba2bdb6a7279f9b740df221e90b4d11fc74d27b3",
    ),
    "SGD:S000217934": (
        "CPX-1103",
        "9bb6e64da63637d23ca711307b6346300830216e362d243513a00add60d6680b",
    ),
    "SGD:S000218025": (
        "CPX-554",
        "4130cfeb17d1011efc4f6a93eb099ea12450c28494be15b9e80890d705e382fb",
    ),
    "SGD:S000218096": (
        "CPX-1706",
        "ffd4950d106647c53033872f3b03bfa760a193a0d85f1573afb37d675d8652c3",
    ),
    "SGD:S000218158": (
        "CPX-1268",
        "e4fe5081d0a6516ee143b07c7e6cba8f584140019c9d5eaefefaaf770559764b",
    ),
    "SGD:S000218211": (
        "CPX-1739",
        "5d1054a984220288b54c85c6c3f690a2bd9bc675ebb80943208912e96a5e3794",
    ),
}
# Other cellular-component xrefs describe the complex class itself. These
# inspected organelle/cytoplasm annotations are the only location projections.
LOCATIONS = {
    "GO:0005737": "cytoplasm",
    "GO:0005739": "mitochondrion",
    "GO:0005794": "Golgi apparatus",
}


def curate_complexes(
    record, sources, proteins, protein_provenance, chemical_labels, sgd_labels=None
):
    nodes = {n["id"]: n for n in record["participants"]}
    refs = {r["id"]: r for r in record["references"]}
    edges = {(e["subject"], e["predicate"], e["object"]): e for e in record["mechanistic_edges"]}
    report = {"file_record": record["id"], "complexes": [], "added_edges": []}
    sgd_labels = sgd_labels or {}

    def add_edge(subject, predicate, obj, evidence, description):
        key = subject, predicate, obj
        if key in edges:
            return
        edge_id = "complex-" + hashlib.sha256("|".join(key).encode()).hexdigest()[:12]
        edge = {
            "id": edge_id,
            "subject": subject,
            "predicate": predicate,
            "object": obj,
            "description": description,
            "evidence": evidence,
        }
        edges[key] = edge
        record["mechanistic_edges"].append(edge)
        report["added_edges"].append(edge_id)

    for complex_id in sorted(set(nodes).intersection(COMPLEXES)):
        cpx, sha = COMPLEXES[complex_id]
        source = sources[cpx]
        nodes[complex_id]["category"] = "complex"
        evidence_type = source["evidenceType"]
        status = f"{evidence_type['identifier']}: {evidence_type['description'].strip()}"
        reference = {
            "id": complex_id,
            "title": f"Complex Portal {cpx}: {source['name']}",
            "url": "https://www.ebi.ac.uk/intact/complex-ws/complex/" + cpx,
            "source_version": "Inspected API snapshot 2026-10-05; release dates "
            + ", ".join(source["releaseDates"]),
            "source_sha256": sha,
        }
        refs.setdefault(complex_id, reference)
        components = []
        for part_index, part in enumerate(source["participants"]):
            identifier = part["identifier"]
            mapping_evidence = []
            if part["interactorType"] == "protein":
                protein_index, protein = proteins[identifier]
                protein_id = "UniProtKB:" + identifier
                matching_sgd = [
                    (i, "SGD:" + xref["id"])
                    for i, xref in enumerate(protein.get("uniProtKBCrossReferences", []))
                    if xref["database"] == "SGD"
                    and ("SGD:" + xref["id"] in nodes or "SGD:" + xref["id"] in sgd_labels)
                ]
                if len(matching_sgd) > 1:
                    raise ValueError(f"ambiguous existing SGD projection for {identifier}")
                projected_id = matching_sgd[0][1] if matching_sgd else protein_id
                label = protein["proteinDescription"]["recommendedName"]["fullName"]["value"]
                if projected_id in sgd_labels:
                    label = sgd_labels[projected_id]
                nodes.setdefault(
                    projected_id, {"id": projected_id, "label": label, "category": "protein"}
                )
                if matching_sgd:
                    if protein_id in nodes and protein_id != projected_id:
                        # Merge only after the primary protein record establishes
                        # exact identity. References keep their source accession.
                        del nodes[protein_id]
                        for edge in record["mechanistic_edges"]:
                            for endpoint in ("subject", "object"):
                                if edge[endpoint] == protein_id:
                                    edge[endpoint] = projected_id
                        edges = {
                            (e["subject"], e["predicate"], e["object"]): e
                            for e in record["mechanistic_edges"]
                        }
                    refs.setdefault(
                        protein_id,
                        {
                            "id": protein_id,
                            "title": f"Reviewed UniProtKB {identifier} SGD cross-reference",
                            "url": protein_provenance["url"],
                            "source_version": "UniProt release 2026_03",
                            "source_sha256": protein_provenance["sha256"],
                        },
                    )
                    mapping_evidence.append(
                        {
                            "reference_id": protein_id,
                            "source_assertion": (
                                f"Reviewed UniProtKB:{identifier} is cross-referenced to "
                                f"{projected_id}; the existing protein node is reused."
                            ),
                            "source_locator": (
                                f"UniProt JSON "
                                f"#/results/{protein_index}/uniProtKBCrossReferences/{matching_sgd[0][0]}"
                            ),
                        }
                    )
            elif part["interactorType"] == "small molecule" and identifier.startswith("CHEBI:"):
                projected_id = identifier
                nodes.setdefault(
                    identifier, {"id": identifier, "label": chemical_labels[identifier]}
                )
                nodes[identifier]["category"] = "cofactor"
            else:
                raise ValueError(f"unhandled complex component: {part}")
            components.append(
                {
                    "source_id": identifier,
                    "projected_id": projected_id,
                    "stoichiometry": part["stochiometry"],
                }
            )
            statement = (
                f"Complex Portal {cpx} lists {identifier} as a {part['interactorType']} component; "
                f"complex evidence is {status}."
            )
            description = status + (
                "; source stoichiometry " + part["stochiometry"]
                if part["stochiometry"]
                else "; stoichiometry unspecified"
            )
            add_edge(
                complex_id,
                "has_part",
                projected_id,
                [
                    {
                        "reference_id": complex_id,
                        "source_assertion": statement,
                        "source_locator": (
                            f"Complex Portal JSON #/participants/{part_index}; /evidenceType"
                        ),
                    }
                ]
                + mapping_evidence,
                description,
            )
        for index, xref in enumerate(source["crossReferences"]):
            if (
                xref["database"] != "gene ontology"
                or xref["qualifier"] != "cellular component"
                or xref["identifier"] not in LOCATIONS
            ):
                continue
            identifier = xref["identifier"]
            nodes.setdefault(
                identifier,
                {
                    "id": identifier,
                    "label": LOCATIONS[identifier],
                    "category": "cellular_component",
                },
            )
            add_edge(
                complex_id,
                "located_in",
                identifier,
                [
                    {
                        "reference_id": complex_id,
                        "source_assertion": (
                            f"Complex Portal {cpx} records cellular location {identifier} "
                            f"({LOCATIONS[identifier]}); its evidence classification is {status}."
                        ),
                        "source_locator": (
                            f"Complex Portal JSON #/crossReferences/{index}; /evidenceType"
                        ),
                    }
                ],
                "Complex location from the independent composition source; original "
                "GO-CAM activity locations are retained with their own provenance.",
            )
        report["complexes"].append(
            {
                "id": complex_id,
                "source": cpx,
                "evidence": status,
                "components": components,
                "source_sha256": sha,
            }
        )
    record["participants"] = list(nodes.values())
    record["references"] = list(refs.values())
    merged = {}
    for edge in record["mechanistic_edges"]:
        key = edge["subject"], edge["predicate"], edge["object"]
        if key not in merged:
            merged[key] = edge
        else:
            for evidence in edge["evidence"]:
                if evidence not in merged[key]["evidence"]:
                    merged[key]["evidence"].append(evidence)
    record["mechanistic_edges"] = list(merged.values())
    validate_record(record)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--complex-dir", required=True, type=Path)
    parser.add_argument("--uniprot-json", required=True, type=Path)
    parser.add_argument("--uniprot-provenance", required=True, type=Path)
    parser.add_argument("--chebi", required=True, type=Path)
    parser.add_argument("--records", default=Path("data/pathways"), type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    provenance = json.loads(args.uniprot_provenance.read_text())
    if digest(args.uniprot_json) != provenance["sha256"]:
        raise ValueError("UniProt source digest mismatch")
    proteins = {
        n["primaryAccession"]: (i, n)
        for i, n in enumerate(json.loads(args.uniprot_json.read_text())["results"])
    }
    sources = {}
    for cpx, sha in COMPLEXES.values():
        path = args.complex_dir / (cpx + ".json")
        if digest(path) != sha:
            raise ValueError(f"Complex Portal artifact differs from inspected source: {cpx}")
        source = json.loads(path.read_text())
        if source["complexAc"] != cpx or source["species"] != "Saccharomyces cerevisiae; 559292":
            raise ValueError(f"complex identity/taxon mismatch: {cpx}")
        sources[cpx] = source
    labels = {
        identifier: term["name"]
        for identifier, term in chebi_terms(args.chebi).items()
        if "name" in term
    }
    reports, pending, records = [], [], []
    for path in sorted(args.records.rglob("*.yaml")):
        record = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        if not record["id"].startswith("gomodel:"):
            continue
        records.append((path, record))
    sgd_labels = {
        n["id"]: n["label"]
        for _, record in records
        for n in record["participants"]
        if n["id"].startswith("SGD:")
    }
    native_parts = {}
    for _, record in records:
        nodes = {node["id"]: node for node in record["participants"]}
        refs = {ref["id"]: ref for ref in record["references"]}
        for edge in record["mechanistic_edges"]:
            if edge["predicate"] == "has_part" and edge["subject"] in COMPLEXES:
                evidence = [e for e in edge["evidence"] if e["reference_id"].startswith("gomodel:")]
                if evidence:
                    native_parts[edge["subject"], edge["object"]] = (
                        nodes[edge["object"]],
                        evidence,
                        refs,
                    )
    for path, record in records:
        nodes = {node["id"]: node for node in record["participants"]}
        refs = {ref["id"]: ref for ref in record["references"]}
        for (complex_id, component), (node, evidence, source_refs) in native_parts.items():
            if complex_id not in nodes:
                continue
            existing = next(
                (
                    edge
                    for edge in record["mechanistic_edges"]
                    if (edge["subject"], edge["predicate"], edge["object"])
                    == (complex_id, "has_part", component)
                ),
                None,
            )
            if existing is None:
                nodes.setdefault(component, copy.deepcopy(node))
                existing = {
                    "id": "complex-native-"
                    + hashlib.sha256(f"{complex_id}|{component}".encode()).hexdigest()[:12],
                    "subject": complex_id,
                    "predicate": "has_part",
                    "object": component,
                    "evidence": [],
                }
                record["mechanistic_edges"].append(existing)
            for item in evidence:
                if item not in existing["evidence"]:
                    existing["evidence"].append(copy.deepcopy(item))
                refs.setdefault(
                    item["reference_id"], copy.deepcopy(source_refs[item["reference_id"]])
                )
        record["participants"], record["references"] = list(nodes.values()), list(refs.values())
        result = curate_complexes(record, sources, proteins, provenance, labels, sgd_labels)
        if result["complexes"]:
            result["file"] = str(path)
            reports.append(result)
            pending.append((path, record))
    pending = changed_records(pending)
    if args.write:
        for _path, record in pending:
            record.setdefault("curation_history", []).append(
                {
                    "timestamp": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "curator": "Codex",
                    "action": "review-complex-composition",
                    "changes": (
                        "Reviewed exact Complex Portal composition, source evidence grades, "
                        "and independent physical complex locations; reused existing "
                        "proteins through reviewed UniProt SGD cross-references."
                    ),
                    "llm_assisted": True,
                }
            )
    publish_curation(
        pending,
        args.report,
        {"uniprot_source": provenance, "records": reports},
        apply=args.write,
        serialize=lambda record: yaml.dump(
            record,
            Dumper=IndentedDumper,
            sort_keys=False,
            allow_unicode=True,
            width=100,
        ),
    )
    print(
        json.dumps(
            {
                "records": len(reports),
                "added_edges": sum(len(r["added_edges"]) for r in reports),
                "written": args.write,
            }
        )
    )


if __name__ == "__main__":
    main()
