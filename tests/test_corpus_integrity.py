from __future__ import annotations

import pytest

from pathwaymech.schema import ValidationError, validate_record, validate_records


def valid_record() -> dict:
    return {
        "id": "GO:0006096",
        "label": "glycolytic process",
        "description": "A starter curation fixture for glycolysis.",
        "pathway_type": "metabolic",
        "taxa": [{"id": "NCBITaxon:562", "label": "Escherichia coli"}],
        "participants": [
            {"id": "CHEBI:17234", "label": "D-glucose"},
            {"id": "CHEBI:17544", "label": "pyruvate"},
        ],
        "reactions": [{"id": "RHEA:16109", "label": "glucose phosphorylation"}],
        "mechanistic_edges": [
            {
                "id": "edge-1",
                "subject": "CHEBI:17234",
                "predicate": "consumes",
                "object": "RHEA:16109",
                "evidence": [
                    {
                        "reference_id": "PMID:1",
                        "quote": "Short evidence quote.",
                    }
                ],
            }
        ],
        "references": [{"id": "PMID:1", "title": "Fixture reference"}],
    }


def test_valid_record_passes() -> None:
    record = validate_record(valid_record())

    assert record.id == "GO:0006096"


def test_missing_reference_fails() -> None:
    record = valid_record()
    record["mechanistic_edges"][0]["evidence"][0]["reference_id"] = "PMID:404"

    with pytest.raises(ValidationError, match="PMID:404"):
        validate_record(record)


def test_duplicate_record_ids_fail() -> None:
    with pytest.raises(ValidationError, match="duplicate pathway id"):
        validate_records([valid_record(), valid_record()])


def test_consumes_edges_point_from_participants_to_reactions() -> None:
    record = valid_record()
    record["mechanistic_edges"][0]["subject"] = "RHEA:16109"
    record["mechanistic_edges"][0]["object"] = "CHEBI:17234"

    with pytest.raises(ValidationError) as raised:
        validate_record(record)

    assert raised.value.errors == [
        "mechanistic_edges[0] consumes edges must point from a participant subject "
        "to a reaction object"
    ]


def test_produces_edges_point_from_reactions_to_participants() -> None:
    record = valid_record()
    record["mechanistic_edges"][0]["predicate"] = "produces"

    with pytest.raises(ValidationError) as raised:
        validate_record(record)

    assert raised.value.errors == [
        "mechanistic_edges[0] produces edges must point from a reaction subject "
        "to a participant object"
    ]
