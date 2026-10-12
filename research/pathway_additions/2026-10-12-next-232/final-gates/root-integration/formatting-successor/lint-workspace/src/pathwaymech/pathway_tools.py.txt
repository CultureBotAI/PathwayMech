from __future__ import annotations

import re
from pathlib import Path
from typing import Any


def load_pathway_tools_dat(
    path: Path, *, encoding: str = "utf-8",
) -> list[dict[str, list[str]]]:
    records: list[dict[str, list[str]]] = []
    current: dict[str, list[str]] = {}
    last_key: str | None = None
    for line_number, raw_line in enumerate(path.read_text(encoding=encoding).splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line == "//":
            if current:
                records.append(current)
                current = {}
            last_key = None
            continue
        if line.startswith("/"):
            if last_key is None:
                raise ValueError(f"orphan continuation at line {line_number}")
            current[last_key][-1] += "\n" + line[1:]
            continue
        if " - " not in line:
            raise ValueError(f"malformed attribute-value pair at line {line_number}")
        key, value = line.split(" - ", 1)
        if not re.fullmatch(r"\^?[A-Z][A-Z0-9?_-]*", key):
            raise ValueError(f"invalid attribute name at line {line_number}: {key!r}")
        current.setdefault(key, []).append(value)
        last_key = key
    if current:
        records.append(current)
    return records


def metacyc_pathway_records(records: list[dict[str, list[str]]]) -> list[dict[str, Any]]:
    return pathway_tools_pathway_records(records, source_prefix="MetaCyc")


def pmn_pathway_records(
    records: list[dict[str, list[str]]],
    *,
    pgdb: str,
    source_version: str | None = None,
) -> list[dict[str, Any]]:
    """Build drafts whose frame identities remain local to an explicit PMN PGDB."""
    return pathway_tools_pathway_records(
        records, source_prefix="PMN", pgdb=pgdb, source_version=source_version
    )


def pathway_tools_pathway_records(
    records: list[dict[str, list[str]]],
    *,
    source_prefix: str,
    pgdb: str | None = None,
    source_version: str | None = None,
) -> list[dict[str, Any]]:
    _validate_scope(source_prefix, pgdb, source_version)
    converted = [
        pathway_tools_pathway_record(
            record, source_prefix=source_prefix, pgdb=pgdb, source_version=source_version
        )
        for record in records
    ]
    ids = [record["id"] for record in converted]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate pathway UNIQUE-ID in Pathway Tools input")
    return converted


def pathway_tools_pathway_record(
    record: dict[str, list[str]],
    *,
    source_prefix: str,
    pgdb: str | None = None,
    source_version: str | None = None,
) -> dict[str, Any]:
    _validate_scope(source_prefix, pgdb, source_version)
    namespace = f"{source_prefix}:{pgdb}" if pgdb is not None else source_prefix
    if len(record.get("UNIQUE-ID", [])) != 1:
        raise ValueError("each pathway must have exactly one UNIQUE-ID")
    native_id = _frame_id(_first(record, "UNIQUE-ID"), namespace)
    pathway_id = _curie(native_id, namespace)
    if record.get("SUB-PATHWAYS") or "Super-Pathways" in record.get("TYPES", []):
        raise ValueError(f"{pathway_id}: sub-pathway expansion is not supported")
    native_reactions = [
        _frame_id(identifier, namespace) for identifier in record.get("REACTION-LIST", [])
    ]
    reactions = [_curie(identifier, namespace) for identifier in native_reactions]
    reaction_set = set(reactions)
    if len(reactions) != len(reaction_set):
        raise ValueError(f"{pathway_id}: duplicate REACTION-LIST frame")
    edges = []
    edge_by_pair: dict[tuple[str, str], dict[str, Any]] = {}

    for slot_index, predecessor in enumerate(record.get("PREDECESSORS", []), 1):
        try:
            downstream, *upstreams = _predecessor_frames(predecessor)
            downstream_id = _curie(downstream, namespace)
            upstream_ids = [_curie(upstream, namespace) for upstream in upstreams]
        except ValueError as exc:
            raise ValueError(f"{pathway_id}: PREDECESSORS[{slot_index}]: {exc}") from exc
        missing = {downstream_id, *upstream_ids} - reaction_set
        if missing:
            raise ValueError(
                f"{pathway_id}: PREDECESSORS[{slot_index}] references frames absent "
                f"from REACTION-LIST: {', '.join(sorted(missing))}"
            )
        if downstream_id in upstream_ids:
            raise ValueError(f"{pathway_id}: PREDECESSORS[{slot_index}] has a self-link")
        for upstream, upstream_id in zip(upstreams, upstream_ids, strict=True):
            evidence = {
                "reference_id": pathway_id,
                "source_assertion": (
                    f"The PREDECESSORS slot lists {upstream} as a direct "
                    f"predecessor of {downstream} in this pathway."
                ),
                "source_locator": (
                    f"pathways.dat[UNIQUE-ID={native_id}]/PREDECESSORS[{slot_index}]"
                ),
            }
            pair = (upstream_id, downstream_id)
            if pair not in edge_by_pair:
                edge = {
                    "id": f"{source_prefix.lower()}-edge-{len(edges) + 1}",
                    "subject": upstream_id,
                    "predicate": "precedes",
                    "object": downstream_id,
                    "evidence": [],
                }
                edge_by_pair[pair] = edge
                edges.append(edge)
            if evidence not in edge_by_pair[pair]["evidence"]:
                edge_by_pair[pair]["evidence"].append(evidence)

    reference = {"id": pathway_id, "title": f"{source_prefix} source pathway {pathway_id}"}
    if source_version is not None:
        reference["source_version"] = source_version

    return {
        "id": pathway_id,
        "label": _first(record, "COMMON-NAME") or pathway_id,
        "description": f"{source_prefix} pathway {pathway_id}.",
        "pathway_type": "metabolic",
        "taxa": [],
        "participants": [],
        "reactions": [
            {"id": reaction_id, "label": native_reaction}
            for reaction_id, native_reaction in zip(reactions, native_reactions, strict=True)
        ],
        "mechanistic_edges": edges,
        "references": [reference],
    }


def _first(record: dict[str, list[str]], field: str) -> str:
    values = record.get(field, [])
    return values[0] if values else ""


def _predecessor_frames(value: str) -> list[str]:
    # SRI's PREDECESSORS slot is (reaction-id pred-id*). A bare pathway
    # frame can mean inherited ordering and needs a separate graph resolver.
    value = value.strip()
    if not (value.startswith("(") and value.endswith(")")):
        raise ValueError("expected a flat (reaction-id pred-id*) tuple")
    body = value[1:-1].strip()
    # Simple frame IDs may be exported as double-quoted strings. Reject
    # concatenated tokens, nested forms and Lisp reader syntax rather than
    # reinterpret them as a different native frame.
    token = r'(?:"[A-Za-z0-9][A-Za-z0-9_: .+-]*"|[A-Za-z0-9][A-Za-z0-9_:.+-]*)'
    if not re.fullmatch(rf"{token}(?:\s+{token})*", body):
        raise ValueError("unsupported or empty predecessor tuple")
    return [item.strip('"') for item in re.findall(token, body)]


def _validate_scope(source_prefix: str, pgdb: str | None, source_version: str | None) -> None:
    if source_prefix not in {"MetaCyc", "PMN"}:
        raise ValueError(f"unsupported Pathway Tools source: {source_prefix}")
    if source_prefix == "PMN":
        if not isinstance(pgdb, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", pgdb):
            raise ValueError("PMN requires an explicit PGDB identifier without separators")
    elif pgdb is not None:
        raise ValueError("PGDB qualification is only supported for PMN")
    if source_version is not None and (
        not isinstance(source_version, str) or not source_version.strip()
    ):
        raise ValueError("source_version must be a non-empty string when supplied")


def _frame_id(identifier: str, namespace: str) -> str:
    native_id = identifier.removeprefix(f"{namespace}:")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+-]*", native_id):
        raise ValueError(f"unsupported or mismatched frame identifier: {identifier!r}")
    return native_id


def _curie(identifier: str, namespace: str) -> str:
    return f"{namespace}:{_frame_id(identifier, namespace)}"
