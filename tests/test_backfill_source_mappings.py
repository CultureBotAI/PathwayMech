from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from pathwaymech.chebi import load_chebi_xrefs
from pathwaymech.schema import validate_record
from pathwaymech.wikipathways import gpml_to_pathway_record, load_gpml_pathway
from scripts.backfill_source_mappings import (
    BackfillError,
    backfill_source_mappings,
    raw_source_records,
)

CHEBI_FIXTURE = Path("tests/fixtures/chebi/kegg_compounds.obo")
WIKIPATHWAYS_FIXTURE = Path("tests/fixtures/wikipathways/WPTEST.gpml")
BIOPAX_FIXTURE = Path("tests/fixtures/biopax/R-TEST.owl")


def test_backfill_adds_source_mappings_without_rewriting_curated_fields(
    tmp_path: Path,
) -> None:
    data_dir = tmp_path / "data" / "pathways"
    data_dir.mkdir(parents=True)
    record = gpml_to_pathway_record(
        load_gpml_pathway(WIKIPATHWAYS_FIXTURE),
        "WikiPathways:WPTEST",
        load_chebi_xrefs(CHEBI_FIXTURE),
    )
    record["description"] = "Curated description."
    record["source_mappings"] = []
    record_path = data_dir / "mini.yaml"
    record_path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    biopax_record = raw_source_records(
        wikipathways_gpml=[],
        reactome_biopax=[BIOPAX_FIXTURE],
    )[0]
    biopax_record["source_mappings"] = []
    (data_dir / "biopax.yaml").write_text(
        yaml.safe_dump(biopax_record, sort_keys=False),
        encoding="utf-8",
    )

    source_records = raw_source_records(
        wikipathways_gpml=[WIKIPATHWAYS_FIXTURE],
        reactome_biopax=[BIOPAX_FIXTURE],
        chebi_obo=CHEBI_FIXTURE,
    )

    results = backfill_source_mappings(data_dir, source_records)
    data = yaml.safe_load(record_path.read_text(encoding="utf-8"))

    assert sorted((result.record_id, result.added) for result in results) == [
        ("Reactome:R-TEST-12345", 1),
        ("WikiPathways:WP9999", 1),
    ]
    assert data["description"] == "Curated description."
    assert data["source_mappings"] == [
        {
            "subject_id": "CAS:98-92-0",
            "subject_label": "Nicotinamide",
            "predicate_id": "skos:exactMatch",
            "object_id": "CHEBI:17154",
            "object_label": "nicotinamide",
            "mapping_justification": "semapv:UnspecifiedMatching",
            "source_pathway_id": "WikiPathways:WP9999",
            "source_element_id": "cas-substrate",
        }
    ]
    validate_record(data)


def test_backfill_check_does_not_write(tmp_path: Path) -> None:
    data_dir = tmp_path / "data" / "pathways"
    data_dir.mkdir(parents=True)
    record = gpml_to_pathway_record(
        load_gpml_pathway(WIKIPATHWAYS_FIXTURE),
        "WikiPathways:WPTEST",
        load_chebi_xrefs(CHEBI_FIXTURE),
    )
    record["source_mappings"] = []
    record_path = data_dir / "mini.yaml"
    text = yaml.safe_dump(record, sort_keys=False)
    record_path.write_text(text, encoding="utf-8")

    source_records = raw_source_records(
        wikipathways_gpml=[WIKIPATHWAYS_FIXTURE],
        reactome_biopax=[],
        chebi_obo=CHEBI_FIXTURE,
    )

    assert backfill_source_mappings(data_dir, source_records, check=True)
    assert record_path.read_text(encoding="utf-8") == text


def test_backfill_rejects_raw_files_that_no_longer_contain_curated_reactions(
    tmp_path: Path,
) -> None:
    data_dir = tmp_path / "data" / "pathways"
    data_dir.mkdir(parents=True)
    record = gpml_to_pathway_record(
        load_gpml_pathway(WIKIPATHWAYS_FIXTURE),
        "WikiPathways:WPTEST",
    )
    record["reactions"].append(
        {"id": "WikiPathways:WP9999/missing", "label": "missing reaction"}
    )
    (data_dir / "mini.yaml").write_text(
        yaml.safe_dump(record, sort_keys=False),
        encoding="utf-8",
    )
    source_records = raw_source_records(
        wikipathways_gpml=[WIKIPATHWAYS_FIXTURE],
        reactome_biopax=[],
        chebi_obo=CHEBI_FIXTURE,
    )

    with pytest.raises(BackfillError, match="raw source is missing"):
        backfill_source_mappings(data_dir, source_records)


def test_backfill_rejects_batch_without_partial_writes(tmp_path: Path) -> None:
    data_dir = tmp_path / "data" / "pathways"
    data_dir.mkdir(parents=True)
    record = gpml_to_pathway_record(
        load_gpml_pathway(WIKIPATHWAYS_FIXTURE),
        "WikiPathways:WPTEST",
        load_chebi_xrefs(CHEBI_FIXTURE),
    )
    source_record = dict(record)
    record["source_mappings"] = []
    record_path = data_dir / "mini.yaml"
    text = yaml.safe_dump(record, sort_keys=False)
    record_path.write_text(text, encoding="utf-8")
    missing_record = dict(source_record, id="WikiPathways:WP404")

    with pytest.raises(BackfillError, match="WikiPathways:WP404"):
        backfill_source_mappings(data_dir, [source_record, missing_record])

    assert record_path.read_text(encoding="utf-8") == text
