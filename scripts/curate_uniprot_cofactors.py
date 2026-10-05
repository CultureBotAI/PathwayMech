#!/usr/bin/env python3
"""Add traceable protein/cofactor annotations from inspected UniProt JSON.

Dry-run by default. The manifest names independent source JSON and provenance
files. Only exact accession or SGD cross-reference matches are used; a missing
cofactor comment is not evidence that a protein has no cofactor. Source notes
and evidence codes preserve alternatives, conditions, and inference limits.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import tarfile
from pathlib import Path

import yaml

from pathwaymech.curation import publish_curation
from pathwaymech.schema import validate_record

DEFAULT_DECISIONS = (
    Path(__file__).resolve().parents[1]
    / "reports/causal_graph_review/uniprot-cofactor-decisions.json"
)
GOCAM_ARCHIVE_URL = "https://current.geneontology.org/products/json/noctua-models-json.tgz"
GOCAM_ARCHIVE_SHA256 = "7a6999245e9265f2167d6e47c7565adb17433ad26611f1a877dc79564279523b"


def caution_digest(cautions: list) -> str:
    return hashlib.sha256(
        json.dumps(cautions, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def cofactor_digest(protein: dict) -> str:
    """Pin a reviewed cofactor decision even when UniProt has no CAUTION."""
    comments = [c for c in protein.get("comments", []) if c["commentType"] == "COFACTOR"]
    return hashlib.sha256(
        json.dumps(comments, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def source_locator(source: dict, provenance: dict, pointer: str) -> str:
    """Pin the actual representation, even when a protein reference preexists."""
    return (
        f"{provenance['url']} [sha256:{provenance['sha256']}] #/results/{source['index']}{pointer}"
    )


def native_identifier_mappings(
    proteins: dict,
    archive_path: Path,
    wanted: set[str],
    model_ids: set[str],
    expected_sha256: str,
) -> dict:
    """Join native individual types to exact independently asserted BioCyc IDs."""
    with archive_path.open("rb") as stream:
        actual_sha = hashlib.file_digest(stream, "sha256").hexdigest()
    if actual_sha != expected_sha256:
        raise ValueError("native GO-CAM source digest mismatch")
    external = {}
    for accession, item in proteins.items():
        for index, xref in enumerate(item["protein"].get("uniProtKBCrossReferences", [])):
            if xref["database"] == "BioCyc" and xref["id"].startswith("EcoCyc:"):
                external.setdefault(xref["id"], []).append((accession, index))
    mappings = {}
    with tarfile.open(archive_path) as archive:
        for member in archive:
            model_id = "gomodel:" + Path(member.name).stem
            if not member.isfile() or model_id not in model_ids:
                continue
            model = json.load(archive.extractfile(member))
            if model["id"] != model_id:
                raise ValueError("native model filename/identity mismatch")
            taxa = {
                a["value"]
                for a in model.get("annotations", [])
                if a["key"] == "https://w3id.org/biolink/vocab/in_taxon"
            }
            for index, node in enumerate(model["individuals"]):
                if node["id"] not in wanted:
                    continue
                types = node.get("type", [])
                if len(types) != 1 or types[0]["id"] not in external:
                    continue
                matches = [
                    pair
                    for pair in external[types[0]["id"]]
                    if "NCBITaxon:" + str(proteins[pair[0]]["protein"]["organism"]["taxonId"])
                    in taxa
                ]
                if len(matches) != 1:
                    raise ValueError(f"ambiguous native BioCyc mapping: {node['id']}")
                accession, crossref_index = matches[0]
                if proteins[accession]["protein"]["entryType"] != "UniProtKB reviewed (Swiss-Prot)":
                    raise ValueError(
                        f"native BioCyc mapping requires reviewed Swiss-Prot: {accession}"
                    )
                mapped = {
                    "accession": accession,
                    "native_type": types[0]["id"],
                    "model": model_id,
                    "member": member.name,
                    "individual_index": index,
                    "crossref_index": crossref_index,
                    "archive_sha256": actual_sha,
                }
                if node["id"] in mappings and mappings[node["id"]] != mapped:
                    raise ValueError(f"conflicting native mapping for {node['id']}")
                mappings[node["id"]] = mapped
    return mappings


def load_sources(manifest: Path) -> tuple[dict, dict]:
    entries = json.loads(manifest.read_text())
    proteins, sources = {}, {}
    for entry in entries:
        raw = Path(entry["path"]).read_bytes()
        provenance = json.loads(Path(entry["provenance"]).read_text())
        if hashlib.sha256(raw).hexdigest() != provenance["sha256"]:
            raise ValueError(f"source digest mismatch: {entry['path']}")
        sources[entry["key"]] = provenance
        for index, protein in enumerate(json.loads(raw)["results"]):
            accession = protein["primaryAccession"]
            if accession not in proteins:
                proteins[accession] = {
                    "protein": protein,
                    "source": entry["key"],
                    "index": index,
                }
    return proteins, sources


def identifier_index(proteins: dict, wanted: set[str] | None = None) -> dict:
    index = {}
    for accession, item in proteins.items():
        ids = {"UniProtKB:" + accession}
        ids.update(
            "SGD:" + crossref["id"]
            for crossref in item["protein"].get("uniProtKBCrossReferences", [])
            if crossref["database"] == "SGD"
        )
        for identifier in ids:
            if wanted is not None and identifier not in wanted:
                continue
            if identifier in index and index[identifier] != accession:
                raise ValueError(f"ambiguous protein mapping: {identifier}")
            index[identifier] = accession
    return index


def cofactor_annotations(protein: dict):
    for comment_index, comment in enumerate(protein.get("comments", [])):
        if comment["commentType"] != "COFACTOR":
            continue
        notes = " ".join(text["value"] for text in comment.get("note", {}).get("texts", []))
        for cofactor_index, cofactor in enumerate(comment.get("cofactors", [])):
            crossref = cofactor.get("cofactorCrossReference", {})
            if crossref.get("database") != "ChEBI" or not crossref.get("id"):
                raise ValueError(f"ungrounded cofactor in {protein['primaryAccession']}")
            yield comment_index, cofactor_index, cofactor, notes


def curate(
    record: dict,
    proteins: dict,
    index: dict,
    labels: dict,
    sources: dict,
    decisions: dict | None = None,
    native_mappings: dict | None = None,
) -> dict:
    """Mutate a caller-owned record, returning an auditable per-record result."""
    participants = {node["id"]: node for node in record["participants"]}
    references = {reference["id"]: reference for reference in record["references"]}
    existing = {
        (edge["subject"], edge["object"])
        for edge in record["mechanistic_edges"]
        if edge["predicate"] == "has_cofactor"
    }
    decisions = decisions or {"decisions": {}}
    native_mappings = native_mappings or {}
    report = {
        "record": record["id"],
        "checked": [],
        "unmapped": [],
        "added": [],
        "semantic_decisions": [],
        "preserved_existing": [],
    }
    report["needs_caution_review"] = []
    for identifier in list(participants):
        namespace = identifier.split(":", 1)[0]
        if namespace not in {"SGD", "UniProtKB", "gomodel"}:
            continue
        if namespace == "gomodel" and participants[identifier].get("category") != "protein":
            continue
        native_mapping = native_mappings.get(identifier)
        accession = native_mapping["accession"] if native_mapping else index.get(identifier)
        if not accession:
            report["unmapped"].append(identifier)
            continue
        source = proteins[accession]
        protein = source["protein"]
        annotations = list(cofactor_annotations(protein))
        report["checked"].append(
            {
                "participant": identifier,
                "protein": accession,
                "entry_type": protein["entryType"],
                "cofactor_annotations": len(annotations),
                "source": source["source"],
                "source_index": source["index"],
            }
        )
        if any(subject == identifier for subject, _ in existing):
            # A reviewed contextual assertion can deliberately avoid a more
            # specific ion claim in the generic database (e.g. disputed Fe-S
            # nuclearity). Preserve the curator's whole cofactor decision.
            report["preserved_existing"].append(identifier)
            continue
        cautions = [
            comment
            for comment in protein.get("comments", [])
            if comment["commentType"] == "CAUTION"
        ]
        decision = decisions.get("decisions", {}).get(accession, {})
        expected_cofactors = decision.get("cofactor_sha256")
        if expected_cofactors and expected_cofactors != cofactor_digest(protein):
            raise ValueError(f"Unreviewed cofactor annotation for semantic decision: {accession}")
        if annotations and cautions and decision.get("caution_sha256") != caution_digest(cautions):
            report["needs_caution_review"].append(
                {
                    "participant": identifier,
                    "protein": accession,
                    "cautions": cautions,
                }
            )
            continue
        grouped: dict[str, list] = {}
        for annotation in annotations:
            cofactor = annotation[2]["cofactorCrossReference"]["id"]
            if cofactor in decision.get("excluded_cofactors", []):
                report["semantic_decisions"].append(
                    {
                        "protein": accession,
                        "cofactor": cofactor,
                        "action": decision.get("exclusion_action", "excluded_tentative"),
                        "reason": decision["rationale"],
                    }
                )
                continue
            projected = decision.get("cofactor_projection", {}).get(cofactor, cofactor)
            if projected != cofactor:
                if not all(term in annotation[3] for term in decision["required_note_terms"]):
                    raise ValueError(f"prosthetic group source note changed for {accession}")
                if labels.get(projected) != decision["projection_label"]:
                    raise ValueError(f"missing independent ChEBI label for projection: {projected}")
                report["semantic_decisions"].append(
                    {
                        "protein": accession,
                        "source_cofactor": cofactor,
                        "cofactor": projected,
                        "action": "project_covalent_group",
                        "reason": decision["rationale"],
                    }
                )
            grouped.setdefault(projected, []).append(annotation)
        for cofactor_id, assertions in grouped.items():
            if (identifier, cofactor_id) in existing:
                continue  # Preserve already curated, potentially narrower source conditions.
            if cofactor_id not in labels:
                raise ValueError(f"missing independent ChEBI label: {cofactor_id}")
            node = participants.setdefault(
                cofactor_id, {"id": cofactor_id, "label": labels[cofactor_id]}
            )
            node["category"] = "cofactor"
            reference_id = "UniProtKB:" + accession
            provenance = sources[source["source"]]
            version = next(
                (
                    value
                    for key, value in provenance["headers"].items()
                    if key.lower() == "x-uniprot-release"
                ),
                "retrieved source snapshot",
            )
            references.setdefault(
                reference_id,
                {
                    "id": reference_id,
                    "title": f"UniProtKB {accession} cofactor annotations",
                    "url": provenance["url"],
                    "source_version": version,
                    "source_sha256": provenance["sha256"],
                },
            )
            evidence, descriptions = [], [protein["entryType"] + " annotation."]
            if decision:
                descriptions.append("Reviewed source qualification: " + decision["rationale"])
            if cofactor_id in decision.get("qualifications", {}):
                descriptions.append(decision["qualifications"][cofactor_id])
            for ci, ai, cofactor, note in assertions:
                attribution = sorted(
                    {
                        item["evidenceCode"]
                        + (
                            f" ({item['source']}:{item['id']})"
                            if item.get("source") and item.get("id")
                            else ""
                        )
                        for item in cofactor.get("evidences", [])
                    }
                )
                descriptions.append(
                    "UniProt evidence: " + ("; ".join(attribution) or "not specified")
                )
                if note:
                    descriptions.append(note)
                    note_attribution = sorted(
                        {
                            item["evidenceCode"]
                            + (
                                f" ({item['source']}:{item['id']})"
                                if item.get("source") and item.get("id")
                                else ""
                            )
                            for text in protein["comments"][ci].get("note", {}).get("texts", [])
                            for item in text.get("evidences", [])
                        }
                    )
                    if note_attribution:
                        descriptions.append("UniProt note evidence: " + "; ".join(note_attribution))
                native_cofactor = cofactor["cofactorCrossReference"]["id"]
                assertion = (
                    f"UniProtKB:{accession} annotates {cofactor_id} as a cofactor of this protein."
                )
                if native_cofactor != cofactor_id:
                    assertion = (
                        f"UniProtKB:{accession} cross-references {native_cofactor}, "
                        "but its note specifies a covalently bound pyruvoyl group; "
                        f"that group is projected to {cofactor_id}."
                    )
                    authority = decisions["projection_authority"]
                    references.setdefault(
                        cofactor_id,
                        {
                            "id": cofactor_id,
                            "title": f"ChEBI {cofactor_id}: {labels[cofactor_id]}",
                            **authority,
                        },
                    )
                    evidence.append(
                        {
                            "reference_id": cofactor_id,
                            "source_assertion": f"ChEBI labels {cofactor_id} as pyruvoyl group.",
                            "source_locator": (
                                f"chebi.obo [Term] id: {cofactor_id}; name: pyruvoyl group"
                            ),
                        }
                    )
                evidence.append(
                    {
                        "reference_id": reference_id,
                        "source_assertion": assertion,
                        "source_locator": source_locator(
                            source, provenance, f"/comments/{ci}/cofactors/{ai}"
                        )
                        + (f"; /results/{source['index']}/comments/{ci}/note" if note else ""),
                    }
                )
            if native_mapping:
                model_id = native_mapping["model"]
                references.setdefault(
                    model_id,
                    {
                        "id": model_id,
                        "title": "Native GO-CAM protein identity mapping",
                        "url": GOCAM_ARCHIVE_URL,
                        "source_version": "Pinned Noctua JSON archive",
                        "source_sha256": native_mapping["archive_sha256"],
                    },
                )
                evidence.extend(
                    [
                        {
                            "reference_id": model_id,
                            "source_assertion": (
                                f"The native individual {identifier} "
                                f"has type {native_mapping['native_type']}."
                            ),
                            "source_locator": (
                                f"{native_mapping['member']}#/individuals/"
                                f"{native_mapping['individual_index']}/type/0"
                            ),
                        },
                        {
                            "reference_id": reference_id,
                            "source_assertion": (
                                f"Reviewed UniProtKB:{accession} has the exact "
                                "BioCyc cross-reference "
                                f"{native_mapping['native_type']}; this joins the native model "
                                "protein to its cofactor annotation."
                            ),
                            "source_locator": source_locator(
                                source,
                                provenance,
                                f"/uniProtKBCrossReferences/{native_mapping['crossref_index']}",
                            ),
                        },
                    ]
                )
            elif namespace == "SGD":
                matches = [
                    ci
                    for ci, crossref in enumerate(protein.get("uniProtKBCrossReferences", []))
                    if crossref["database"] == "SGD" and "SGD:" + crossref["id"] == identifier
                ]
                if len(matches) != 1:
                    raise ValueError(f"missing exact source cross-reference for {identifier}")
                evidence.append(
                    {
                        "reference_id": reference_id,
                        "source_assertion": (
                            f"UniProtKB:{accession} has the exact SGD cross-reference {identifier}."
                        ),
                        "source_locator": source_locator(
                            source, provenance, f"/uniProtKBCrossReferences/{matches[0]}"
                        ),
                    }
                )
            edge_id = (
                "cofactor-"
                + hashlib.sha256(f"{identifier}|{cofactor_id}".encode()).hexdigest()[:12]
            )
            if any(edge["id"] == edge_id for edge in record["mechanistic_edges"]):
                raise ValueError(f"edge ID collision: {edge_id}")
            record["mechanistic_edges"].append(
                {
                    "id": edge_id,
                    "subject": identifier,
                    "predicate": "has_cofactor",
                    "object": cofactor_id,
                    "description": " ".join(dict.fromkeys(descriptions)),
                    "evidence": evidence,
                }
            )
            report["added"].append(
                {"protein": identifier, "cofactor": cofactor_id, "edge": edge_id}
            )
    record["participants"] = list(participants.values())
    record["references"] = list(references.values())
    validate_record(record)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--chebi-db", type=Path, required=True)
    parser.add_argument("--records", type=Path, default=Path("data/pathways"))
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--decisions", type=Path, default=DEFAULT_DECISIONS)
    parser.add_argument("--gocam-archive", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    paths = sorted(args.records.rglob("*.yaml"))
    if not paths:
        raise ValueError("empty pathway corpus")
    records = [(path, yaml.load(path.read_text(), Loader=yaml.CSafeLoader)) for path in paths]
    proteins, sources = load_sources(args.manifest)
    wanted = {node["id"] for _, record in records for node in record["participants"]}
    index = identifier_index(proteins, wanted)
    decisions = json.loads(args.decisions.read_text())
    native_mappings = {}
    if args.gocam_archive:
        native_mappings = native_identifier_mappings(
            proteins,
            args.gocam_archive,
            wanted,
            {record["id"] for _, record in records if record["id"].startswith("gomodel:")},
            GOCAM_ARCHIVE_SHA256,
        )
    accessions = set(index.values()) | {
        mapping["accession"] for mapping in native_mappings.values()
    }
    required = {
        annotation[2]["cofactorCrossReference"]["id"]
        for value in (proteins[accession] for accession in accessions)
        for annotation in cofactor_annotations(value["protein"])
    }
    required.update(
        target
        for accession in accessions
        for target in decisions["decisions"]
        .get(accession, {})
        .get("cofactor_projection", {})
        .values()
    )
    with sqlite3.connect(f"file:{args.chebi_db}?mode=ro", uri=True) as db:
        labels = {
            identifier: db.execute(
                "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'",
                (identifier,),
            ).fetchone()
            for identifier in required
        }
    labels = {identifier: row[0] for identifier, row in labels.items() if row}
    pending, reports = [], []
    for path, record in records:
        report = curate(record, proteins, index, labels, sources, decisions, native_mappings)
        report["path"] = str(path)
        reports.append(report)
        if report["added"]:
            pending.append((path, record))
    if args.apply and any(report["needs_caution_review"] for report in reports):
        raise ValueError("unreviewed source cautions remain; no corpus enrichment was written")
    publish_curation(
        pending,
        args.report,
        {
            "sources": sources,
            "records": reports,
            "native_mappings": native_mappings,
            "decisions_sha256": hashlib.sha256(args.decisions.read_bytes()).hexdigest(),
        },
        apply=args.apply,
        serialize=lambda record: yaml.safe_dump(
            record,
            sort_keys=False,
            allow_unicode=True,
            width=88,
        ),
    )
    print(f"{len(reports)} records checked; {len(pending)} records gain cofactor annotations")


if __name__ == "__main__":
    main()
