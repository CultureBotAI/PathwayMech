from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from scripts.stage_imodulondb_pathway_contexts import (
    load_imodulon_rows,
    pathway_participants,
    stage_candidates,
    write_reports,
)


def test_exact_uniprot_matches_stage_and_nonmatches_block(tmp_path: Path) -> None:
    records = tmp_path / "data" / "pathways"
    write_record(records / "cell-wall.yaml", "UniProtKB:P0A6B4")
    rows_path = tmp_path / "imodulondb.jsonl"
    rows_path.write_text(
        "\n".join(
            json.dumps(row)
            for row in (
                imodulon_row(uniprot_id="P0A6B4", in_imodulon=True),
                imodulon_row(uniprot_id="P0A6B4", in_imodulon=False),
                imodulon_row(uniprot_id=None, in_imodulon=True),
                imodulon_row(uniprot_id="not-a-uniprot", in_imodulon=True),
                imodulon_row(uniprot_id="P0A6B5", in_imodulon=True),
            )
        ),
        encoding="utf-8",
    )

    candidates, blocked = stage_candidates(
        load_imodulon_rows(rows_path),
        pathway_participants(records),
    )

    assert [candidate.participant_id for candidate in candidates] == [
        "UniProtKB:P0A6B4"
    ]
    assert candidates[0].pathway_id == "WikiPathways:WP5060"
    assert candidates[0].edge_ids == ("edge-001",)
    assert candidates[0].imodulon_id == "511145/GSE123/7"
    assert [row.reason for row in blocked] == [
        "OUTSIDE_IMODULON",
        "NO_UNIPROT",
        "INVALID_UNIPROT",
        "NO_PATHWAY_PARTICIPANT",
    ]


def test_apply_writes_review_artifacts(tmp_path: Path) -> None:
    records = tmp_path / "data" / "pathways"
    write_record(records / "cell-wall.yaml", "UniProtKB:P0A6B4")
    candidates, blocked = stage_candidates(
        [load_imodulon_rows(write_jsonl(tmp_path, [imodulon_row()]))[0]],
        pathway_participants(records),
    )

    report_dir = tmp_path / "reports" / "imodulondb"
    write_reports(report_dir, candidates, blocked)

    assert {path.name for path in report_dir.iterdir()} == {
        "blocked.tsv",
        "candidates.jsonl",
        "candidates.tsv",
        "summary.md",
    }
    assert "imodulondb-" in (report_dir / "candidates.jsonl").read_text(
        encoding="utf-8"
    )
    assert "Candidates: 1" in (report_dir / "summary.md").read_text(encoding="utf-8")


def test_malformed_rows_fail_with_context(tmp_path: Path) -> None:
    rows_path = write_jsonl(tmp_path, [imodulon_row(k="7")])

    with pytest.raises(ValueError, match=r"imodulondb\.jsonl:1: k must be an integer"):
        load_imodulon_rows(rows_path)


def test_duplicate_candidate_keys_fail(tmp_path: Path) -> None:
    records = tmp_path / "data" / "pathways"
    write_record(records / "cell-wall.yaml", "UniProtKB:P0A6B4")

    with pytest.raises(ValueError, match="duplicate iModulonDB pathway candidate"):
        stage_candidates(
            load_imodulon_rows(write_jsonl(tmp_path, [imodulon_row(), imodulon_row()])),
            pathway_participants(records),
        )


def write_record(path: Path, participant_id: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(
            {
                "id": "WikiPathways:WP5060",
                "label": "Peptidoglycan cytoplasmic synthesis",
                "description": "A fixture pathway.",
                "pathway_type": "cell-wall-biosynthesis",
                "taxa": [{"id": "NCBITaxon:562", "label": "Escherichia coli"}],
                "participants": [
                    {"id": participant_id, "label": "alanine racemase"},
                ],
                "reactions": [
                    {"id": "RHEA:12345", "label": "fixture reaction"},
                ],
                "mechanistic_edges": [
                    {
                        "id": "edge-001",
                        "subject": participant_id,
                        "predicate": "catalyzes",
                        "object": "RHEA:12345",
                        "evidence": [
                            {
                                "reference_id": "PMID:1",
                                "quote": "fixture quote",
                            }
                        ],
                    }
                ],
                "references": [{"id": "PMID:1", "title": "Fixture reference"}],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )


def write_jsonl(tmp_path: Path, rows: list[dict]) -> Path:
    path = tmp_path / "imodulondb.jsonl"
    path.write_text(
        "\n".join(json.dumps(row) for row in rows) + "\n",
        encoding="utf-8",
    )
    return path


def imodulon_row(**overrides: object) -> dict:
    row = {
        "organism": "511145",
        "dataset": "GSE123",
        "k": 7,
        "gene_id": "b4053",
        "gene_locus": "b4053",
        "gene_name": "alr",
        "gene_product": "alanine racemase",
        "weight": 0.42,
        "in_imodulon": True,
        "uniprot_id": "P0A6B4",
        "uniprot_protein_name": "Alanine racemase",
        "all_regulators": "MurR",
        "imodulon_name": "cell wall",
    }
    row.update(overrides)
    return row
