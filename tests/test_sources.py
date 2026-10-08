from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from pathwaymech.sources import (
    SourceInventoryError,
    source_seed_rows,
    validate_source_inventory,
)


def test_configured_sources_have_ingest_priorities() -> None:
    config = yaml.safe_load(Path("conf/sources.yaml").read_text(encoding="utf-8"))

    sources = validate_source_inventory(config)

    assert [source.id for source in sources] == [
        "go-cam",
        "wikipathways",
        "rhea",
        "mibig",
        "reactome",
        "pathbank",
        "metacyc",
        "kegg",
        "go",
        "modelseed",
        "bigg",
        "bv-brc",
        "pmn",
        "veupathdb",
        "gapmind",
        "unipathway",
        "dbcan-pul",
        "panther",
        "puldb",
        "seed-pubseed",
        "microscope-microcyc",
        "jgi-img-abc",
        "ecmdb",
        "algaepath",
        "brenda",
        "hadeg",
        "envipath",
        "dram",
        "diting",
        "metabolic",
    ]
    assert [source.priority for source in sources] == sorted(
        source.priority for source in sources
    )


def test_source_seed_rows_include_disabled_candidates() -> None:
    config = yaml.safe_load(Path("conf/sources.yaml").read_text(encoding="utf-8"))
    sources = validate_source_inventory(config)

    rows = source_seed_rows(sources)

    assert rows[0] == "priority\tid\tingest_status\tenabled\trole\tlabel"
    assert rows[1] == (
        "10\tgo-cam\tactive\ttrue\tcausal-activity-model\t"
        "Gene Ontology Causal Activity Models"
    )
    assert any(row.startswith("60\tpathbank\tfixture\ttrue\t") for row in rows)
    assert (
        "130\tpmn\tlicense-gated\ttrue\talgal-pathway-reference\t"
        "Plant Metabolic Network / ChlamyCyc"
    ) in rows
    assert (
        "140\tveupathdb\tsupport\ttrue\tprotist-fungal-pathway-membership\t"
        "VEuPathDB"
    ) in rows
    assert "150\tgapmind\tsupport\ttrue\tenzyme-step-rulebase\tGapMind" in rows
    assert "160\tunipathway\tsupport\ttrue\tpathway-crosswalk\tUniPathway" in rows
    assert "260\thadeg\tsupport\ttrue\tdegradation-pathway-membership\tHADEG" in rows
    assert "250\tbrenda\tsupport\ttrue\tpathway-reaction-component-reference\tBRENDA" in rows
    assert "170\tdbcan-pul\tlicense-gated\ttrue\tglycan-locus-reference\tdbCAN-PUL" in rows
    assert (
        "180\tpanther\tfixture\ttrue\tbiopax-pathway-reference\tPANTHER Pathway"
    ) in rows
    assert (
        "190\tpuldb\tdeferred\tfalse\tglycan-locus-reference\tPULDB"
    ) in rows


@pytest.mark.parametrize(
    ("source_id", "status"),
    [
        ("envipath", "license-gated"),
        ("dram", "license-gated"),
        ("diting", "deferred"),
        ("metabolic", "license-gated"),
    ],
)
def test_discovery_candidates_are_not_enabled(source_id: str, status: str) -> None:
    config = yaml.safe_load(Path("conf/sources.yaml").read_text(encoding="utf-8"))
    sources = {source.id: source for source in validate_source_inventory(config)}

    assert sources[source_id].enabled is False
    assert sources[source_id].ingest_status == status


def test_duplicate_source_priority_fails() -> None:
    duplicate_priority = {
        "sources": [
            {
                "id": "a",
                "priority": 10,
                "label": "A",
                "enabled": False,
                "ingest_status": "next",
                "role": "pathway-reference",
                "homepage": "https://example.org/a",
                "notes": "Candidate A.",
            },
            {
                "id": "b",
                "priority": 10,
                "label": "B",
                "enabled": False,
                "ingest_status": "next",
                "role": "pathway-reference",
                "homepage": "https://example.org/b",
                "notes": "Candidate B.",
            },
        ]
    }

    with pytest.raises(SourceInventoryError, match="duplicate source priority: 10"):
        validate_source_inventory(duplicate_priority)


def test_invalid_source_id_fails() -> None:
    bad_id = {
        "sources": [
            {
                "id": "GO CAM",
                "priority": 10,
                "label": "GO-CAM",
                "enabled": False,
                "ingest_status": "next",
                "role": "causal-activity-model",
                "homepage": "https://example.org/go-cam",
                "notes": "Invalid source identifier.",
            },
        ]
    }

    with pytest.raises(SourceInventoryError, match="lowercase letters"):
        validate_source_inventory(bad_id)
