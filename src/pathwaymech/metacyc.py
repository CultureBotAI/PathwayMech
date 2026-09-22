from __future__ import annotations

from pathlib import Path
from typing import Any


def load_metacyc_dat(path: Path) -> list[dict[str, list[str]]]:
    records: list[dict[str, list[str]]] = []
    current: dict[str, list[str]] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line == "//":
            if current:
                records.append(current)
                current = {}
            continue
        if " - " not in line:
            continue
        key, value = line.split(" - ", 1)
        current.setdefault(key, []).append(value)
    if current:
        records.append(current)
    return records


def metacyc_pathway_records(records: list[dict[str, list[str]]]) -> list[dict[str, Any]]:
    return [metacyc_pathway_record(record) for record in records]


def metacyc_pathway_record(record: dict[str, list[str]]) -> dict[str, Any]:
    pathway_id = _curie(_first(record, "UNIQUE-ID"))
    reactions = [_curie(identifier) for identifier in record.get("REACTION-LIST", [])]
    reaction_set = set(reactions)
    edges = []

    for predecessor in record.get("PREDECESSORS", []):
        downstream, upstream = _predecessor_pair(predecessor)
        if not downstream or not upstream:
            continue
        downstream_id = _curie(downstream)
        upstream_id = _curie(upstream)
        if downstream_id in reaction_set and upstream_id in reaction_set:
            edges.append(
                {
                    "id": f"metacyc-edge-{len(edges) + 1}",
                    "subject": upstream_id,
                    "predicate": "precedes",
                    "object": downstream_id,
                    "evidence": [
                        {
                            "reference_id": pathway_id,
                            "quote": f"MetaCyc predecessor link {upstream} before {downstream}.",
                        }
                    ],
                }
            )

    return {
        "id": pathway_id,
        "label": _first(record, "COMMON-NAME") or pathway_id,
        "description": f"MetaCyc pathway {pathway_id}.",
        "pathway_type": "metabolic",
        "taxa": [],
        "participants": [],
        "reactions": [
            {"id": reaction_id, "label": reaction_id.removeprefix("MetaCyc:")}
            for reaction_id in reactions
        ],
        "mechanistic_edges": edges,
        "references": [
            {
                "id": pathway_id,
                "title": f"MetaCyc source pathway {pathway_id}",
            }
        ],
    }


def _first(record: dict[str, list[str]], field: str) -> str:
    values = record.get(field, [])
    return values[0] if values else ""


def _predecessor_pair(value: str) -> tuple[str, str]:
    tokens = value.strip("()").split()
    if len(tokens) < 2:
        return "", ""
    return tokens[0], tokens[1]


def _curie(identifier: str) -> str:
    return f"MetaCyc:{identifier.removeprefix('MetaCyc:')}"
