"""Reproduce this bounded Reactome curation from the reviewed source projection.

No network calls. All records are validated before any destination is written.
Existing, different records or historical ledgers are never overwritten.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from pathwaymech.schema import validate_record
from pathwaymech.strict import validator

HERE = Path(__file__).resolve().parent


def triple(edge):
    return [edge["subject"], edge["predicate"], edge["object"]]


def build(source, plan):
    record = copy.deepcopy(source["record"])
    removed = plan.get("exclude_reactions", {})
    reaction_ids = {r["id"] for r in record["reactions"]} - removed.keys()
    original = record["mechanistic_edges"]
    excluded = {tuple(item["triple"]): item["reason"] for item in plan.get("exclude_edges", [])}
    changed = {tuple(item["triple"]): item for item in plan.get("change_edges", [])}
    original_triples = [tuple(triple(edge)) for edge in original]
    for reviewed in excluded.keys() | changed.keys():
        if original_triples.count(reviewed) != 1:
            raise ValueError("A reviewed decision must match exactly one source edge")
    if removed.keys() - {reaction["id"] for reaction in record["reactions"]}:
        raise ValueError("A rejected reaction is absent from the source projection")
    edges, decisions = [], []
    for before in original:
        edge = copy.deepcopy(before)
        decision = {"source_edge": before}
        rejected = removed.get(edge["subject"]) or removed.get(edge["object"])
        if rejected or tuple(triple(edge)) in excluded:
            decision.update(status="excluded", reason=rejected or excluded[tuple(triple(edge))])
        else:
            change = changed.get(tuple(triple(edge)))
            if change:
                edge.update(copy.deepcopy(change["set"]))
                decision.update(status="corrected", reason=change["reason"])
            else:
                decision.update(status="retained", reason="Inspected source assertion retained.")
            edges.append(edge)
            decision["curated_edge"] = edge
        decisions.append(decision)

    # Reach physical entities from accepted reactions, then follow composition
    # and location outwards. Shared compartment nodes must not pull excluded
    # enzymes back into the graph.
    reached = set(reaction_ids)
    for edge in edges:
        if edge["subject"] in reaction_ids or edge["object"] in reaction_ids:
            reached.update((edge["subject"], edge["object"]))
    while True:
        previous = reached.copy()
        for edge in edges:
            if edge["predicate"] in {"has_part", "located_in"} and edge["subject"] in reached:
                reached.add(edge["object"])
        if previous == reached:
            break
    for decision in decisions:
        edge = decision.get("curated_edge")
        if edge and not {edge["subject"], edge["object"]}.issubset(reached):
            decision.update(status="excluded", reason="Context belongs only to excluded reactions.")
            decision.pop("curated_edge")
    edges = [d["curated_edge"] for d in decisions if "curated_edge" in d]
    for edge in plan.get("add_edges", []):
        edges.append(copy.deepcopy(edge))
    record["description"] = plan["description"]
    record["mechanistic_edges"] = edges
    record["reactions"] = [r for r in record["reactions"] if r["id"] in reaction_ids]
    record["participants"] = [p for p in record["participants"] if p["id"] in reached]
    for node in record["participants"]:
        node["category"] = plan["categories"][node["id"]]
        if node["id"] in plan["labels"]:
            node["label"] = plan["labels"][node["id"]]
    for node in record["reactions"]:
        node["category"] = "molecular_activity"
    for ref in record["references"]:
        if ref["id"] == record["id"]:
            ref.update(plan["source_reference"])
    existing_refs = {r["id"] for r in record["references"]}
    for ref in plan.get("references", []):
        if ref["id"] in existing_refs:
            next(r for r in record["references"] if r["id"] == ref["id"]).update(ref)
        else:
            record["references"].append(copy.deepcopy(ref))
            existing_refs.add(ref["id"])
    mappings = [m for m in record.get("source_mappings", []) if m["object_id"] in reached]
    for mapping in mappings:
        if mapping["object_id"] in plan["labels"]:
            mapping["object_label"] = plan["labels"][mapping["object_id"]]
    if mappings:
        record["source_mappings"] = mappings
    else:
        record.pop("source_mappings", None)
    used_changes = {
        tuple(triple(d["source_edge"])) for d in decisions if d["status"] == "corrected"
    }
    if used_changes != changed.keys():
        raise ValueError("A reviewed correction no longer matches exactly one source edge")
    if len({e["id"] for e in edges}) != len(edges):
        raise ValueError("Duplicate final edge IDs")
    return record, {
        "pathway_id": record["id"],
        "source_sha256": source["manifest"]["sha256"],
        "source_reaction_count": len(source["record"]["reactions"]),
        "curated_reaction_count": len(record["reactions"]),
        "source_edge_count": len(original),
        "curated_edge_count": len(edges),
        "source_edge_dispositions": decisions,
        "added_edges": plan.get("add_edges", []),
        "removed_participants": [
            p for p in source["record"]["participants"] if p["id"] not in reached
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir", type=Path, help="Write new records here; otherwise validate only."
    )
    parser.add_argument("--ledger", type=Path, help="Write a new complete edge-disposition ledger.")
    args = parser.parse_args()
    source_bytes = (HERE / "source-projection.json").read_bytes()
    source = json.loads(source_bytes)
    plan = json.loads((HERE / "curation-plan.json").read_text())
    if hashlib.sha256(source_bytes).hexdigest() != plan["source_projection_sha256"]:
        raise ValueError("Source projection has changed since review")
    checker = validator()
    outputs, ledgers = [], []
    for item in source["pathways"]:
        spec = plan["pathways"][item["record"]["id"]]
        record, ledger = build(item, spec)
        validate_record(record)
        errors = list(checker.validate(record, "PathwayRecord").results)
        if errors:
            raise ValueError([error.message for error in errors])
        payload = yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=100)
        ledger["record_filename"] = spec["filename"]
        ledger["record_sha256"] = hashlib.sha256(payload.encode()).hexdigest()
        ledgers.append(ledger)
        if args.output_dir:
            outputs.append((args.output_dir / spec["filename"], payload))
    if args.ledger:
        payload = {
            "date": "2026-10-07",
            "source_projection_sha256": plan["source_projection_sha256"],
            "pathways": ledgers,
        }
        outputs.append((args.ledger, json.dumps(payload, indent=2) + "\n"))
    for path, content in outputs:
        if path.exists() and path.read_text() != content:
            raise ValueError(f"Refusing to overwrite existing different artifact: {path}")
    for path, content in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(content)
    counts = [
        {k: v for k, v in ledger.items() if k.endswith("count") or k == "pathway_id"}
        for ledger in ledgers
    ]
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
