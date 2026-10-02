from __future__ import annotations

from pathlib import Path
from typing import Any


def load_pathway_tools_dat(path: Path) -> list[dict[str, list[str]]]:
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
    return pathway_tools_pathway_records(records, source_prefix="MetaCyc")


def pmn_pathway_records(records: list[dict[str, list[str]]]) -> list[dict[str, Any]]:
    return pathway_tools_pathway_records(records, source_prefix="PMN")


def pathway_tools_pathway_records(
    records: list[dict[str, list[str]]],
    *,
    source_prefix: str,
) -> list[dict[str, Any]]:
    return [
        pathway_tools_pathway_record(record, source_prefix=source_prefix)
        for record in records
    ]


def pathway_tools_pathway_record(
    record: dict[str, list[str]],
    *,
    source_prefix: str,
) -> dict[str, Any]:
    pathway_id = _curie(_first(record, "UNIQUE-ID"), source_prefix)
    reactions = [
        _curie(identifier, source_prefix)
        for identifier in record.get("REACTION-LIST", [])
    ]
    reaction_set = set(reactions)
    edges = []

    for predecessor in record.get("PREDECESSORS", []):
        downstream, upstream = _predecessor_pair(predecessor)
        if not downstream or not upstream:
            continue
        downstream_id = _curie(downstream, source_prefix)
        upstream_id = _curie(upstream, source_prefix)
        if downstream_id in reaction_set and upstream_id in reaction_set:
            edges.append(
                {
                    "id": f"{source_prefix.lower()}-edge-{len(edges) + 1}",
                    "subject": upstream_id,
                    "predicate": "precedes",
                    "object": downstream_id,
                    "evidence": [
                        {
                            "reference_id": pathway_id,
                            "quote": (
                                f"{source_prefix} predecessor link {upstream} "
                                f"before {downstream}."
                            ),
                        }
                    ],
                }
            )

    return {
        "id": pathway_id,
        "label": _first(record, "COMMON-NAME") or pathway_id,
        "description": f"{source_prefix} pathway {pathway_id}.",
        "pathway_type": "metabolic",
        "taxa": [],
        "participants": [],
        "reactions": [
            {"id": reaction_id, "label": reaction_id.removeprefix(f"{source_prefix}:")}
            for reaction_id in reactions
        ],
        "mechanistic_edges": edges,
        "references": [
            {
                "id": pathway_id,
                "title": f"{source_prefix} source pathway {pathway_id}",
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


def _curie(identifier: str, source_prefix: str) -> str:
    return f"{source_prefix}:{identifier.removeprefix(f'{source_prefix}:')}"
