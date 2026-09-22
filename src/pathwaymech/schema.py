from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any

ALLOWED_CURIE_PREFIXES = {
    "CHEBI",
    "DOI",
    "EC",
    "GO",
    "GTDB",
    "KEGG",
    "MetaCyc",
    "NCBITaxon",
    "PMID",
    "RHEA",
    "UniProtKB",
}

ALLOWED_EDGE_PREDICATES = {
    "activates",
    "catalyzes",
    "consumes",
    "enables",
    "inhibits",
    "precedes",
    "produces",
    "regulates",
}


class ValidationError(ValueError):
    """Raised when a pathway YAML document violates the local schema."""

    def __init__(self, errors: list[str]) -> None:
        super().__init__("\n".join(errors))
        self.errors = errors


@dataclass(frozen=True)
class PathwayRecord:
    id: str
    label: str
    description: str
    pathway_type: str
    taxa: list[dict[str, Any]]
    participants: list[dict[str, Any]]
    reactions: list[dict[str, Any]]
    mechanistic_edges: list[dict[str, Any]]
    references: list[dict[str, Any]]


def validate_records(records: list[dict[str, Any]]) -> list[PathwayRecord]:
    """Validate multiple records and reject duplicate pathway ids."""

    validated = [validate_record(record) for record in records]
    id_counts = Counter(record.id for record in validated)
    duplicate_ids = sorted(record_id for record_id, count in id_counts.items() if count > 1)
    if duplicate_ids:
        raise ValidationError([f"duplicate pathway id: {record_id}" for record_id in duplicate_ids])
    return validated


def validate_record(record: dict[str, Any]) -> PathwayRecord:
    """Validate one raw YAML record."""

    errors: list[str] = []
    if not isinstance(record, dict):
        raise ValidationError(["record must be a mapping"])

    required = [
        "id",
        "label",
        "description",
        "pathway_type",
        "taxa",
        "participants",
        "reactions",
        "mechanistic_edges",
        "references",
    ]
    for field in required:
        if field not in record:
            errors.append(f"missing required field: {field}")

    for field in ["id", "label", "description", "pathway_type"]:
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")

    _validate_curie(record.get("id"), "id", errors)
    taxa = _validate_named_nodes(record.get("taxa"), "taxa", errors)
    participants = _validate_named_nodes(record.get("participants"), "participants", errors)
    reactions = _validate_named_nodes(record.get("reactions"), "reactions", errors)
    references = _validate_references(record.get("references"), errors)
    edges = _validate_edges(
        record.get("mechanistic_edges"),
        {record.get("id"), *taxa, *participants, *reactions},
        references,
        errors,
    )

    if errors:
        raise ValidationError(errors)

    return PathwayRecord(
        id=record["id"],
        label=record["label"],
        description=record["description"],
        pathway_type=record["pathway_type"],
        taxa=record["taxa"],
        participants=record["participants"],
        reactions=record["reactions"],
        mechanistic_edges=edges,
        references=record["references"],
    )


def _validate_named_nodes(value: Any, field: str, errors: list[str]) -> set[str]:
    if not isinstance(value, list):
        errors.append(f"{field} must be a list")
        return set()

    ids: set[str] = set()
    for index, item in enumerate(value):
        path = f"{field}[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{path} must be a mapping")
            continue
        node_id = item.get("id")
        label = item.get("label")
        if not isinstance(node_id, str) or not node_id.strip():
            errors.append(f"{path}.id must be a non-empty string")
        else:
            _validate_curie(node_id, f"{path}.id", errors)
            ids.add(node_id)
        if not isinstance(label, str) or not label.strip():
            errors.append(f"{path}.label must be a non-empty string")
    return ids


def _validate_references(value: Any, errors: list[str]) -> set[str]:
    if not isinstance(value, list):
        errors.append("references must be a list")
        return set()

    ids: set[str] = set()
    for index, item in enumerate(value):
        path = f"references[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{path} must be a mapping")
            continue
        reference_id = item.get("id")
        if not isinstance(reference_id, str) or not reference_id.strip():
            errors.append(f"{path}.id must be a non-empty string")
        else:
            _validate_curie(reference_id, f"{path}.id", errors)
            ids.add(reference_id)
        if not item.get("title") and not item.get("citation"):
            errors.append(f"{path} must include title or citation")
    return ids


def _validate_edges(
    value: Any,
    node_ids: set[Any],
    reference_ids: set[str],
    errors: list[str],
) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        errors.append("mechanistic_edges must be a list")
        return []

    for index, item in enumerate(value):
        path = f"mechanistic_edges[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{path} must be a mapping")
            continue
        edge_id = item.get("id")
        if not isinstance(edge_id, str) or not edge_id.strip():
            errors.append(f"{path}.id must be a non-empty string")
        subject = item.get("subject")
        predicate = item.get("predicate")
        obj = item.get("object")
        if subject not in node_ids:
            errors.append(f"{path}.subject does not resolve locally: {subject!r}")
        if obj not in node_ids:
            errors.append(f"{path}.object does not resolve locally: {obj!r}")
        if predicate not in ALLOWED_EDGE_PREDICATES:
            errors.append(f"{path}.predicate is not supported: {predicate!r}")
        _validate_evidence(item.get("evidence"), reference_ids, f"{path}.evidence", errors)
    return value


def _validate_evidence(
    value: Any,
    reference_ids: set[str],
    path: str,
    errors: list[str],
) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{path} must be a non-empty list")
        return

    for index, item in enumerate(value):
        item_path = f"{path}[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{item_path} must be a mapping")
            continue
        reference_id = item.get("reference_id")
        if reference_id not in reference_ids:
            errors.append(f"{item_path}.reference_id is not declared: {reference_id!r}")
        quote = item.get("quote")
        if not isinstance(quote, str) or not quote.strip():
            errors.append(f"{item_path}.quote must be a non-empty string")
        elif len(quote) > 400:
            errors.append(f"{item_path}.quote must be 400 characters or fewer")


def _validate_curie(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, str) or ":" not in value:
        errors.append(f"{path} must be a CURIE")
        return
    prefix = value.split(":", 1)[0]
    if prefix not in ALLOWED_CURIE_PREFIXES:
        errors.append(f"{path} has unsupported prefix: {prefix}")
