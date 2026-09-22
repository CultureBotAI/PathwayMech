from __future__ import annotations

from pathlib import Path

import yaml

from pathwaymech.kegg import kgml_to_pathway_record, load_kgml
from pathwaymech.schema import validate_record

FIXTURE = Path("tests/fixtures/kegg/map00010.kgml")


def test_kgml_converts_to_valid_pathway_record() -> None:
    record = validate_record(kgml_to_pathway_record(load_kgml(FIXTURE)))

    assert record.id == "KEGG:map00010"
    assert record.participants == [
        {"id": "KEGG:C00236", "label": "KEGG:C00236"},
        {"id": "KEGG:C00197", "label": "KEGG:C00197"},
    ]
    assert record.reactions == [{"id": "KEGG:R01512", "label": "KEGG:R01512"}]
    assert [edge["predicate"] for edge in record.mechanistic_edges] == [
        "consumes",
        "produces",
    ]


def test_kgml_seed_yaml_round_trips_as_pathway_record() -> None:
    text = yaml.safe_dump(kgml_to_pathway_record(load_kgml(FIXTURE)), sort_keys=False)

    assert validate_record(yaml.safe_load(text)).id == "KEGG:map00010"
