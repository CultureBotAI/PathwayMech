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

    assert [source.id for source in sources[:3]] == ["go-cam", "wikipathways", "rhea"]
    assert [source.id for source in sources[-3:]] == ["modelseed", "bigg", "bv-brc"]
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
