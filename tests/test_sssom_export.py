from __future__ import annotations

import csv
from pathlib import Path

import pytest

from pathwaymech.schema import PathwayRecord
from pathwaymech.sssom import SSSOM_COLUMNS, SssomRow, sssom_rows, write_sssom


def record(source_mappings: list[dict[str, str]] | None = None) -> PathwayRecord:
    return PathwayRecord(
        id="Reactome:R-TEST-12345",
        label="test pathway",
        description="A compact test pathway.",
        pathway_type="test",
        taxa=[],
        participants=[{"id": "UniProtKB:P12345", "label": "Mini enzyme"}],
        reactions=[],
        mechanistic_edges=[],
        references=[],
        source_mappings=source_mappings
        if source_mappings is not None
        else [
            {
                "subject_id": "UniProt:P12345",
                "subject_label": "Mini enzyme",
                "predicate_id": "skos:exactMatch",
                "object_id": "UniProtKB:P12345",
                "object_label": "Mini enzyme",
                "mapping_justification": "semapv:UnspecifiedMatching",
                "source_pathway_id": "Reactome:R-TEST-12345",
                "source_element_id": "mini_enzyme",
            }
        ],
    )


def test_sssom_rows_keep_source_context_in_deterministic_rows() -> None:
    assert sssom_rows([record()]) == [
        SssomRow(
            subject_id="UniProt:P12345",
            subject_label="Mini enzyme",
            predicate_id="skos:exactMatch",
            object_id="UniProtKB:P12345",
            object_label="Mini enzyme",
            mapping_justification="semapv:UnspecifiedMatching",
            comment=(
                "source_pathway_id=Reactome:R-TEST-12345; "
                "source_element_id=mini_enzyme"
            ),
        )
    ]


def test_write_sssom_uses_lf_tsv_with_stable_headers(tmp_path: Path) -> None:
    path = write_sssom([record()], tmp_path / "source_mappings.sssom.tsv")

    assert path.read_bytes().count(b"\r") == 0
    assert path.read_text(encoding="utf-8").splitlines()[3] == "\t".join(SSSOM_COLUMNS)
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t", fieldnames=SSSOM_COLUMNS))

    assert rows[-1]["subject_id"] == "UniProt:P12345"
    assert rows[-1]["object_id"] == "UniProtKB:P12345"


def test_sssom_rejects_label_only_subjects() -> None:
    bad_mapping = dict(record().source_mappings[0], subject_id="Mini enzyme")

    with pytest.raises(ValueError, match="subject_id must be a CURIE"):
        sssom_rows([record([bad_mapping])])


def test_sssom_rejects_empty_curie_prefixes() -> None:
    bad_mapping = dict(record().source_mappings[0], subject_id=":P12345")

    with pytest.raises(ValueError, match="subject_id must be a CURIE"):
        sssom_rows([record([bad_mapping])])


def test_sssom_rejects_final_curie_only_pseudo_mappings() -> None:
    bad_mapping = dict(record().source_mappings[0], subject_id="UniProtKB:P12345")

    with pytest.raises(ValueError, match="source mapping subject_id must differ"):
        sssom_rows([record([bad_mapping])])
