#!/usr/bin/env python3
"""Reproduce the exhaustive GO-CAM native graph review from pinned raw sources.

Dry-run by default. --write updates only gomodel records after every candidate
validates. Raw source files are external inputs, never inferred from the corpus.
Additional independently cited edges survive a subsequent native-source refresh.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import tarfile
from collections import Counter
from datetime import UTC, datetime
from functools import cache
from pathlib import Path

import yaml

from pathwaymech.gocam_native import activity_ids, annotation_values, project_native_model
from pathwaymech.schema import validate_record

ARCHIVE_URL = "https://current.geneontology.org/products/json/noctua-models-json.tgz"
ARCHIVE_SHA256 = "7a6999245e9265f2167d6e47c7565adb17433ad26611f1a877dc79564279523b"
CHEBI_SHA256 = "6cd3c7f18d8b22c577e110e00008fb288d8f5b34424bbe5011858747062f9dd9"
GLY1_SHA256 = "f66256c250243efb72e5b6108db6b8aef1acf264f0e212166aeb12dd6374e748"
GLY1_URL = (
    "https://rest.uniprot.org/uniprotkb/search?query="
    "%28gene_exact%3AGLY1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json"
)
SCOPE_SOURCES = {
    "THREOCAT2-PWY": "fc90084c6cd2dd9fca125d571aff66563dbe8b77072d0731fee02e533a3cec41",
    "PWY3O-402": "3a5a693132e02b45cb64e0c2563accabac5f123a5ec38366cbef87cc36b60cb0",
    "PWY-5041": "3c85f94b2435ff4d3a8cfe9627b3ef2f6ced6ea9dc44ded62ec8a022ae9a2772",
}
# These decisions were checked against the species-specific SGD text, not just
# reaction membership in the imported BioPAX outline. In particular, SGD says
# KBL is absent and TDH is uncertain in yeast. Do not inflate taxon claims.
THREONINE_CONTEXT = {
    "gomodel:AKBLIG-RXN": (
        "SGD summary explicitly reports that S. cerevisiae lacks KBL; "
        "imported outline is not species evidence."
    ),
    "gomodel:THREODEHYD-RXN": (
        "SGD calls yeast TDH existence uncertain; no enabling protein in the source model."
    ),
    "gomodel:THREOSPON-RXN": (
        "SGD describes this fate as presumed, downstream of the uncertain "
        "TDH route; retain as contextual uncertainty."
    ),
    "gomodel:HOMOSERDEAM-RXN": (
        "Homoserine side branch outside the retained enzyme-supported "
        "threonine route; no source enabler."
    ),
    "gomodel:METBALT-RXN": (
        "O-succinylhomoserine side branch outside the retained threonine route; no source enabler."
    ),
    "gomodel:AMACETOXID-RXN": (
        "Downstream aminoacetone outline lacks a yeast enabler; SGD text "
        "does not independently establish this activity."
    ),
    "gomodel:AMINOPROPDEHYDROG-RXN": (
        "Aminopropanol branch lacks a yeast enabler and independent "
        "species-specific support in the inspected SGD summary."
    ),
    "gomodel:KETOBUTFORMLY-RXN": (
        "Propionate fermentation outline lacks a yeast enabler and "
        "species-specific support in the inspected SGD summary."
    ),
    "gomodel:PROPKIN-RXN": (
        "Propionate kinase outline lacks a yeast enabler and "
        "species-specific support in the inspected SGD summary."
    ),
    "gomodel:PTAALT-RXN": (
        "Phosphate propanoyltransferase outline lacks a yeast enabler and "
        "species-specific support in the inspected SGD summary."
    ),
}


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def chebi_terms(path: Path) -> dict:
    if digest(path) != CHEBI_SHA256:
        raise ValueError("ChEBI artifact differs from the inspected release 255")
    terms, current = {}, None
    for line in path.open(encoding="utf-8"):
        line = line.rstrip("\n")
        if line == "[Term]":
            current = {}
        elif line.startswith("["):
            current = None
        elif current is not None and ": " in line:
            key, value = line.split(": ", 1)
            if key == "id":
                terms[value] = current
            elif key == "name":
                current["name"] = value
            elif key == "is_a":
                current.setdefault("parents", []).append(value.split(" ! ")[0])
    return terms


class IndentedDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def enrich_gly1(record: dict, source: Path, terms: dict) -> None:
    """Add the independently reviewed yeast aldolase route missing from GO-CAM."""
    if digest(source) != GLY1_SHA256:
        raise ValueError("GLY1 source differs from the inspected UniProt entry 198")
    entry = json.loads(source.read_text())["results"][0]
    if entry["primaryAccession"] != "P37303" or entry["organism"]["taxonId"] != 559292:
        raise ValueError("GLY1 protein/taxon mismatch")
    protein, activity = "UniProtKB:P37303", "GO:0004793"
    additions = [
        {
            "id": protein,
            "label": entry["proteinDescription"]["recommendedName"]["fullName"]["value"],
            "category": "protein",
        },
        {"id": "CHEBI:15343", "label": terms["CHEBI:15343"]["name"], "category": "small_molecule"},
        {"id": "CHEBI:57305", "label": terms["CHEBI:57305"]["name"], "category": "small_molecule"},
    ]
    existing = {node["id"] for node in record["participants"]}
    record["participants"].extend(node for node in additions if node["id"] not in existing)
    if activity not in {node["id"] for node in record["reactions"]}:
        record["reactions"].append(
            {
                "id": activity,
                "label": "threonine aldolase activity",
                "category": "molecular_activity",
            }
        )
    reference = {
        "id": protein,
        "title": "UniProt reviewed GLY1 (P37303), Saccharomyces cerevisiae S288C",
        "url": GLY1_URL,
        "source_version": "Entry 198; annotation update 2026-06-10",
        "source_sha256": GLY1_SHA256,
    }
    if protein not in {ref["id"] for ref in record["references"]}:
        record["references"].append(reference)
    specifications = [
        (
            protein,
            "enables",
            activity,
            "/comments/1/reaction; /uniProtKBCrossReferences/38",
            "Reviewed GLY1 is annotated to threonine aldolase activity and "
            "catalyzes L-threonine cleavage to acetaldehyde and glycine; the "
            "catalytic annotation cites experimental evidence from PMID:9151955.",
        ),
        (
            activity,
            "has_input",
            "CHEBI:57926",
            "/comments/1/reaction",
            "The reviewed GLY1 catalytic reaction is L-threonine = acetaldehyde "
            "+ glycine; its ChEBI cross-references identify L-threonine as "
            "CHEBI:57926.",
        ),
        (
            activity,
            "has_output",
            "CHEBI:15343",
            "/comments/1/reaction",
            "The reviewed GLY1 catalytic reaction produces acetaldehyde, "
            "cross-referenced as CHEBI:15343, from L-threonine.",
        ),
        (
            activity,
            "has_output",
            "CHEBI:57305",
            "/comments/1/reaction",
            "The reviewed GLY1 catalytic reaction produces glycine, "
            "cross-referenced as CHEBI:57305, from L-threonine.",
        ),
        (
            protein,
            "located_in",
            "GO:0005829",
            "/uniProtKBCrossReferences/36",
            "The reviewed GLY1 entry records a cytosol annotation (GO:0005829) "
            "with IDA:SGD evidence.",
        ),
        (
            activity,
            "part_of",
            "GO:0006567",
            "/comments/5; /uniProtKBCrossReferences/40",
            "UniProt assigns GLY1 to the single-step L-threonine degradation via "
            "the aldolase pathway and records L-threonine catabolic process "
            "(GO:0006567).",
        ),
    ]
    triples = {(e["subject"], e["predicate"], e["object"]) for e in record["mechanistic_edges"]}
    for subject, predicate, obj, locator, assertion in specifications:
        if (subject, predicate, obj) in triples:
            continue
        record["mechanistic_edges"].append(
            {
                "id": f"edge-{len(record['mechanistic_edges']) + 1:03d}",
                "subject": subject,
                "predicate": predicate,
                "object": obj,
                "evidence": [
                    {
                        "reference_id": protein,
                        "source_assertion": assertion,
                        "source_locator": "UniProt JSON #/results/0"
                        + locator.replace("; /", "; /results/0/"),
                    }
                ],
            }
        )
    suffix = (
        " Independently reviewed UniProt evidence adds the GLY1 threonine "
        "aldolase route producing glycine and acetaldehyde."
    )
    if suffix.strip() not in record["description"]:
        record["description"] += suffix


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--chebi", type=Path, required=True)
    parser.add_argument("--records", type=Path, default=Path("data/pathways"))
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument(
        "--gly1-uniprot",
        type=Path,
        help="Pinned reviewed GLY1 query response for the independent threonine aldolase route",
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if digest(args.archive) != ARCHIVE_SHA256:
        raise ValueError("GO-CAM archive differs from the independently inspected snapshot")
    terms = chebi_terms(args.chebi)

    @cache
    def ancestors(identifier: str) -> frozenset[str]:
        return frozenset({identifier}).union(
            *(ancestors(p) for p in terms.get(identifier, {}).get("parents", []))
        )

    def chemical_category(identifier: str) -> str | None:
        lineage = ancestors(identifier)
        for root, category in [
            ("CHEBI:16991", "dna"),
            ("CHEBI:33697", "rna"),
            ("CHEBI:36080", "protein"),
            ("CHEBI:18059", "lipid"),
        ]:
            if root in lineage:
                return category
        if identifier in {"CHEBI:24431", "CHEBI:33695"} or "CHEBI:33839" in lineage:
            return None
        return "small_molecule"

    records = []
    for path in sorted(args.records.rglob("*.yaml")):
        record = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        if record["id"].startswith("gomodel:"):
            records.append((path, record))
    wanted = {record["id"] for _, record in records}
    models = {}
    with tarfile.open(args.archive) as archive:
        for member in archive:
            if not member.isfile() or not member.name.endswith(".json"):
                continue
            identifier = "gomodel:" + Path(member.name).stem
            if identifier in wanted:
                raw = archive.extractfile(member).read()
                model = json.loads(raw)
                if model["id"] != identifier:
                    raise ValueError(f"archive filename/model mismatch: {member.name}")
                models[identifier] = (member.name, model, hashlib.sha256(raw).hexdigest())
    if set(models) != wanted:
        raise ValueError(f"missing primary models: {wanted - set(models)}")
    timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    ledger = []
    pending = []
    for path, record in records:
        member, model, model_sha = models[record["id"]]
        model_activities = activity_ids(model)
        included = model_activities.copy()
        exclusions = (
            THREONINE_CONTEXT if record["id"] == "gomodel:YeastPathways_THREOCAT2-PWY" else {}
        )
        included.difference_update(exclusions)
        labels = {identifier: term["name"] for identifier, term in terms.items() if "name" in term}
        labels.update(
            {n["id"]: n["label"] for field in ("participants", "reactions") for n in record[field]}
        )
        projection = project_native_model(
            model,
            source_member=member,
            included_activities=included,
            known_labels=labels,
            chemical_category=chemical_category,
        )
        before = {
            "participants": len(record["participants"]),
            "reactions": len(record["reactions"]),
            "edges": len(record["mechanistic_edges"]),
        }
        before_reactions = {n["id"] for n in record["reactions"]}
        # Curator additions supported by separate primary references are kept.
        external_edges = [
            e
            for e in record["mechanistic_edges"]
            if any(ev["reference_id"] != record["id"] for ev in e["evidence"])
        ]
        external_nodes = {n for edge in external_edges for n in (edge["subject"], edge["object"])}
        established_cofactors = {
            edge["object"] for edge in external_edges if edge["predicate"] == "has_cofactor"
        }
        for field in ("participants", "reactions"):
            projected_ids = {n["id"] for n in projection[field]}
            record[field] = projection[field] + [
                n
                for n in record[field]
                if n["id"] in external_nodes and n["id"] not in projected_ids
            ]
            for node in record[field]:
                if node["id"] in established_cofactors:
                    node["category"] = "cofactor"
        record["mechanistic_edges"] = projection["mechanistic_edges"] + external_edges
        for index, edge in enumerate(record["mechanistic_edges"], 1):
            edge["id"] = f"edge-{index:03d}"
        reference = next(r for r in record["references"] if r["id"] == record["id"])
        reference.update(
            url=ARCHIVE_URL,
            source_sha256=ARCHIVE_SHA256,
            source_version="Pinned Noctua JSON archive; model date "
            + ", ".join(annotation_values(model, "date"))
            + "; member "
            + member,
        )
        if (
            record["id"] == "gomodel:YeastPathways_THREOCAT2-PWY"
            and "KBL" not in record["description"]
        ):
            record["description"] += (
                " The broader imported outline contains unassigned "
                "reactions; SGD reports KBL absent and threonine dehydrogenase uncertain in yeast, "
                "so those outline branches are not asserted as established yeast mechanisms."
            )
        added = sorted(included - before_reactions)
        if record["id"] == "gomodel:YeastPathways_PWY-5041" and "gomodel:RXN-7605" in added:
            record["description"] += (
                " The source also models the generic SAM-dependent methyl transfer "
                "step without assigning an enabling protein."
            )
        if record["id"] == "gomodel:YeastPathways_PWY3O-402" and "gomodel:RXN3O-9819" in added:
            record["description"] += (
                " The source includes the additional diphosphoinositol "
                "pentakisphosphate phosphorylation step without assigning its "
                "enabling protein."
            )
        if record["id"] == "gomodel:YeastPathways_THREOCAT2-PWY" and args.gly1_uniprot:
            enrich_gly1(record, args.gly1_uniprot, terms)
        event = {
            "timestamp": timestamp,
            "curator": "Codex",
            "action": "review-causal-graph",
            "changes": (
                "Reviewed every native GO-CAM fact; preserved precise input/output, "
                "causal, location, "
                "membership and complex-part relations with traceable structured "
                "source evidence. Kept distinct "
                "generic physical instances and recorded source-scope exclusions in "
                "the cohort review ledger."
            ),
            "llm_assisted": True,
        }
        record.setdefault("curation_history", []).append(event)
        validate_record(record)
        represented = sum(f["status"] == "represented" for f in projection["facts"])
        lineage_categories = Counter(
            n.get("category", "unspecified") for n in record["participants"]
        )
        row = {
            "file": str(path),
            "id": record["id"],
            "status": "reviewed-updated",
            "model_member": member,
            "model_sha256": model_sha,
            "before": before,
            "after": {
                "participants": len(record["participants"]),
                "reactions": len(record["reactions"]),
                "edges": len(record["mechanistic_edges"]),
            },
            "source_facts": len(model["facts"]),
            "represented_facts": represented,
            "excluded_facts": len(model["facts"]) - represented,
            "scope_exclusions": exclusions,
            "added_native_activities": added,
            "participant_categories": dict(lineage_categories),
            "activity_enablers_unassigned": sorted(
                included - {f["subject"] for f in model["facts"] if f["property"] == "RO:0002333"}
            ),
            "individual_projections": projection["individual_projections"],
            "facts": projection["facts"],
        }
        ledger.append(row)
        pending.append((path, record))
    args.report_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "timestamp": timestamp,
        "source": {"url": ARCHIVE_URL, "sha256": ARCHIVE_SHA256},
        "chebi": {
            "version": "255",
            "sha256": CHEBI_SHA256,
            "url": "https://ftp.ebi.ac.uk/pub/databases/chebi/ontology/chebi.obo",
        },
        "scope_source_pages": [
            {
                "url": "https://pathway.yeastgenome.org/YEAST/NEW-IMAGE?object=" + identifier,
                "sha256": sha,
            }
            for identifier, sha in SCOPE_SOURCES.items()
        ],
        "records": ledger,
    }
    if args.gly1_uniprot:
        report["independent_enrichment"] = {
            "url": GLY1_URL,
            "sha256": GLY1_SHA256,
            "record": "gomodel:YeastPathways_THREOCAT2-PWY",
            "entry": "UniProtKB:P37303",
        }
    (args.report_dir / "gocam-causal-review.json").write_text(json.dumps(report, indent=2) + "\n")
    if args.write:
        for path, record in pending:
            path.write_text(
                yaml.dump(
                    record, Dumper=IndentedDumper, sort_keys=False, allow_unicode=True, width=100
                )
            )
    print(
        json.dumps(
            {
                "records": len(ledger),
                "source_facts": sum(r["source_facts"] for r in ledger),
                "represented_facts": sum(r["represented_facts"] for r in ledger),
                "excluded_facts": sum(r["excluded_facts"] for r in ledger),
                "edges": sum(r["after"]["edges"] for r in ledger),
                "written": args.write,
            }
        )
    )


if __name__ == "__main__":
    main()
