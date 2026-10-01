from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, TypeAlias

EXACT_MATCH = "skos:exactMatch"
UNSPECIFIED_MATCHING = "semapv:UnspecifiedMatching"


@dataclass(frozen=True)
class CurieMapping:
    """A source database accession normalized to a final PathwayMech CURIE."""

    subject_id: str
    subject_label: str
    object_id: str
    object_label: str
    predicate_id: str = EXACT_MATCH
    mapping_justification: str = UNSPECIFIED_MATCHING


CurieMappings: TypeAlias = Mapping[str, str | CurieMapping]


def normalized_curie(source_id: str, mappings: CurieMappings) -> str:
    mapping = mappings.get(source_id)
    if isinstance(mapping, CurieMapping):
        return mapping.object_id
    return mapping or source_id


def source_mapping_row(
    source_id: str,
    source_label: str,
    mapping: str | CurieMapping,
    *,
    source_pathway_id: str,
    source_element_id: str,
) -> dict[str, str]:
    if isinstance(mapping, CurieMapping):
        return {
            "subject_id": mapping.subject_id,
            "subject_label": source_label or mapping.subject_label,
            "predicate_id": mapping.predicate_id,
            "object_id": mapping.object_id,
            "object_label": mapping.object_label,
            "mapping_justification": mapping.mapping_justification,
            "source_pathway_id": source_pathway_id,
            "source_element_id": source_element_id,
        }

    return {
        "subject_id": source_id,
        "subject_label": source_label or source_id,
        "predicate_id": EXACT_MATCH,
        "object_id": mapping,
        "object_label": mapping,
        "mapping_justification": UNSPECIFIED_MATCHING,
        "source_pathway_id": source_pathway_id,
        "source_element_id": source_element_id,
    }


def unique_source_mappings(mappings: list[dict[str, str]]) -> list[dict[str, str]]:
    unique: dict[tuple[tuple[str, Any], ...], dict[str, str]] = {}
    for mapping in mappings:
        unique.setdefault(tuple(sorted(mapping.items())), mapping)
    return list(unique.values())
