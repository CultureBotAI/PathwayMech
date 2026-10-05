from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from dataclasses import field as dataclass_field
from typing import Any

from jsonschema import FormatChecker

# The fleet's deterministic curation-timestamp year guard (CurationEvent.timestamp
# in the schema): rejects the 2206-for-2026 class of typo without a wall clock.
CURATION_TIMESTAMP = re.compile(r"^20[0-9]{2}-")
# `range: datetime` in the schema becomes JSON Schema `format: date-time`, which the
# closed gate checks with jsonschema's FormatChecker. Using the same checker here
# keeps the two validators agreeing on what a timestamp is by construction.
_DATE_TIME = FormatChecker(formats=["date-time"])
_SOURCE_XML_QUOTE = re.compile(r"^\s*<\s*/?\s*([A-Za-z_:][\w:.-]*)")
_CONFIDENCE = re.compile(r"^(0(\.[0-9]+)?|1(\.0+)?)(?![\s\S])")
_SOURCE_XML_EVIDENCE_TAGS = {
    "Anchor",
    "DataNode",
    "Graphics",
    "Group",
    "Interaction",
    "Point",
    "Xref",
    "left-primaries",
    "reaction-layout",
    "reaction-ordering",
    "rh:ec",
    "right-primaries",
}

ALLOWED_CURIE_PREFIXES = {
    "BV-BRC",
    "BiGG",
    "CAS",
    "CHEBI",
    "ChemSpider",
    "DOI",
    "EC",
    "ECO",
    "Ensembl",
    "Entrez",
    "GO",
    "GO_REF",
    "GTDB",
    "HMDB",
    "KEGG",
    "LIPIDMAPS",
    "MIBiG",
    "MetaCyc",
    "ModelSEED",
    "NCBIProtein",
    "NCBITaxon",
    "PANTHER",
    "PathBank",
    "PMN",
    "PMID",
    "PubChem",
    "RHEA",
    "Reactome",
    "SGD",
    "TubercuList",
    "UniProtKB",
    "WikiPathways",
    "gomodel",
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
    gene_clusters: list[dict[str, Any]] = dataclass_field(default_factory=list)
    source_mappings: list[dict[str, Any]] = dataclass_field(default_factory=list)
    curation_history: list[dict[str, Any]] = dataclass_field(default_factory=list)


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
    gene_clusters = _validate_gene_clusters(record.get("gene_clusters", []), errors)
    source_mappings = _validate_source_mappings(record.get("source_mappings", []), errors)
    references = _validate_references(record.get("references"), errors)
    edges = _validate_edges(
        record.get("mechanistic_edges"),
        {record.get("id"), *taxa, *participants, *reactions},
        participants,
        reactions,
        references,
        errors,
    )
    if "curation_history" in record:
        _validate_curation_history(record["curation_history"], errors)

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
        gene_clusters=gene_clusters,
        source_mappings=source_mappings,
        mechanistic_edges=edges,
        references=record["references"],
        curation_history=record.get("curation_history", []),
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


def _validate_gene_clusters(value: Any, errors: list[str]) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        errors.append("gene_clusters must be a list")
        return []

    for index, item in enumerate(value):
        path = f"gene_clusters[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{path} must be a mapping")
            continue

        cluster_id = item.get("id")
        if not isinstance(cluster_id, str) or not cluster_id.strip():
            errors.append(f"{path}.id must be a non-empty string")
        else:
            _validate_curie(cluster_id, f"{path}.id", errors)
            if not cluster_id.startswith("MIBiG:"):
                errors.append(f"{path}.id must use the MIBiG prefix")

        label = item.get("label")
        if not isinstance(label, str) or not label.strip():
            errors.append(f"{path}.label must be a non-empty string")

        _validate_optional_strings(
            item.get("products"),
            f"{path}.products",
            errors,
        )
        _validate_optional_strings(
            item.get("biosynthetic_classes"),
            f"{path}.biosynthetic_classes",
            errors,
        )
        _validate_cluster_genes(item.get("genes"), f"{path}.genes", errors)
        _validate_genomic_loci(item.get("loci"), f"{path}.loci", errors)
    return value


def _validate_optional_strings(value: Any, path: str, errors: list[str]) -> None:
    if value is None:
        return
    if not isinstance(value, list):
        errors.append(f"{path} must be a list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{path}[{index}] must be a non-empty string")


def _validate_cluster_genes(value: Any, path: str, errors: list[str]) -> None:
    if value is None:
        return
    if not isinstance(value, list):
        errors.append(f"{path} must be a list")
        return
    for index, item in enumerate(value):
        item_path = f"{path}[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{item_path} must be a mapping")
            continue
        gene_id = item.get("id")
        if not isinstance(gene_id, str) or not gene_id.strip():
            errors.append(f"{item_path}.id must be a non-empty string")
        label = item.get("label")
        if "label" in item and (not isinstance(label, str) or not label.strip()):
            errors.append(f"{item_path}.label must be a non-empty string")


def _validate_genomic_loci(value: Any, path: str, errors: list[str]) -> None:
    if value is None:
        return
    if not isinstance(value, list):
        errors.append(f"{path} must be a list")
        return
    for index, item in enumerate(value):
        item_path = f"{path}[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{item_path} must be a mapping")
            continue
        accession = item.get("accession")
        if not isinstance(accession, str) or not accession.strip():
            errors.append(f"{item_path}.accession must be a non-empty string")
        _validate_optional_positive_int(item.get("start"), f"{item_path}.start", errors)
        _validate_optional_positive_int(item.get("end"), f"{item_path}.end", errors)
        if ("start" in item) != ("end" in item):
            errors.append(f"{item_path} must include both start and end when either is set")


def _validate_optional_positive_int(value: Any, path: str, errors: list[str]) -> None:
    if value is None:
        return
    if type(value) is not int or value < 1:
        errors.append(f"{path} must be a positive integer")


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


def _validate_curation_history(value: Any, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append("curation_history must be a list")
        return

    for index, item in enumerate(value):
        path = f"curation_history[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{path} must be a mapping")
            continue
        timestamp = item.get("timestamp")
        if (
            not isinstance(timestamp, str)
            or not CURATION_TIMESTAMP.match(timestamp)
            or not _DATE_TIME.conforms(timestamp, "date-time")
        ):
            errors.append(
                f"{path}.timestamp must be a quoted RFC 3339 date-time with a timezone, "
                f"starting 20YY-, such as '2026-09-28T12:00:00Z': {timestamp!r}"
            )


def _validate_source_mappings(value: Any, errors: list[str]) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        errors.append("source_mappings must be a list")
        return []

    required = (
        "subject_id",
        "subject_label",
        "predicate_id",
        "object_id",
        "object_label",
        "mapping_justification",
        "confidence",
        "source_pathway_id",
        "source_element_id",
    )
    for index, item in enumerate(value):
        path = f"source_mappings[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{path} must be a mapping")
            continue
        values = {}
        for field in required:
            field_path = f"{path}.{field}"
            field_value = item.get(field)
            if not isinstance(field_value, str) or not field_value.strip():
                errors.append(f"{field_path} must be a non-empty string")
            else:
                values[field] = field_value
        for field in (
            "subject_id",
            "predicate_id",
            "object_id",
            "mapping_justification",
            "source_pathway_id",
        ):
            if field in values:
                _validate_external_curie(item[field], f"{path}.{field}", errors)
        if "predicate_id" in values and item["predicate_id"] != "skos:exactMatch":
            errors.append(f"{path}.predicate_id must be skos:exactMatch")
        if "confidence" in values and not _CONFIDENCE.match(item["confidence"]):
            errors.append(f"{path}.confidence must be a number from 0 through 1")
        if (
            "subject_id" in values
            and "object_id" in values
            and item["subject_id"] == item["object_id"]
        ):
            errors.append(f"{path} must map a source CURIE to a different object CURIE")
    return value


def _validate_edges(
    value: Any,
    node_ids: set[Any],
    participant_ids: set[str],
    reaction_ids: set[str],
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
        subject_resolves = subject in node_ids
        object_resolves = obj in node_ids
        if not subject_resolves:
            errors.append(f"{path}.subject does not resolve locally: {subject!r}")
        if not object_resolves:
            errors.append(f"{path}.object does not resolve locally: {obj!r}")
        if predicate not in ALLOWED_EDGE_PREDICATES:
            errors.append(f"{path}.predicate is not supported: {predicate!r}")
        if subject_resolves and object_resolves:
            _validate_edge_endpoint_types(
                path,
                predicate,
                subject,
                obj,
                participant_ids,
                reaction_ids,
                errors,
            )
        _validate_evidence(item.get("evidence"), reference_ids, f"{path}.evidence", errors)
    return value


def _validate_edge_endpoint_types(
    path: str,
    predicate: Any,
    subject: Any,
    obj: Any,
    participant_ids: set[str],
    reaction_ids: set[str],
    errors: list[str],
) -> None:
    if predicate == "consumes" and (subject not in participant_ids or obj not in reaction_ids):
        errors.append(
            f"{path} consumes edges must point from a participant subject to a reaction object"
        )
    if predicate == "produces" and (subject not in reaction_ids or obj not in participant_ids):
        errors.append(
            f"{path} produces edges must point from a reaction subject to a participant object"
        )


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
        elif _is_source_xml_quote(quote):
            errors.append(f"{item_path}.quote must be human-readable, not raw source XML")


def _validate_curie(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, str) or ":" not in value:
        errors.append(f"{path} must be a CURIE")
        return
    prefix, local = value.split(":", 1)
    if prefix not in ALLOWED_CURIE_PREFIXES:
        errors.append(f"{path} has unsupported prefix: {prefix}")
    if not local or any(character.isspace() for character in local):
        errors.append(f"{path} must have a local part with no whitespace")


def _validate_external_curie(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, str) or ":" not in value:
        errors.append(f"{path} must be a CURIE")
        return
    prefix, local = value.split(":", 1)
    if not prefix or any(character.isspace() for character in prefix):
        errors.append(f"{path} must have a prefix with no whitespace")
    if not local or any(character.isspace() for character in local):
        errors.append(f"{path} must have a local part with no whitespace")


def _is_source_xml_quote(quote: str) -> bool:
    match = _SOURCE_XML_QUOTE.match(quote)
    return bool(match and match.group(1) in _SOURCE_XML_EVIDENCE_TAGS)
