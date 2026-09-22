from __future__ import annotations

from pathlib import Path

import yaml

from pathwaymech.gocam import gocam_to_pathway_record, load_gocam_model
from pathwaymech.schema import validate_record

FIXTURE = Path("tests/fixtures/gocam/mini_model.json")


def test_gocam_model_converts_to_valid_pathway_record() -> None:
    model = load_gocam_model(FIXTURE)

    record = validate_record(gocam_to_pathway_record(model))

    assert record.id == "gomodel:YeastPathways_GLYCOLYSIS"
    assert record.taxa == [{"id": "NCBITaxon:559292", "label": "NCBITaxon:559292"}]
    assert {participant["id"] for participant in record.participants} == {
        "CHEBI:57604",
        "CHEBI:58272",
        "CHEBI:58289",
        "SGD:S000000605",
        "SGD:S000001635",
    }
    assert [reaction["id"] for reaction in record.reactions] == [
        "gomodel:PHOSGLYPHOS-RXN",
        "gomodel:RXN-15513",
    ]
    assert [edge["predicate"] for edge in record.mechanistic_edges] == [
        "enables",
        "consumes",
        "produces",
        "precedes",
        "enables",
        "consumes",
        "produces",
    ]
    assert record.references == [
        {
            "id": "GO_REF:0000123",
            "title": "GO-CAM evidence reference GO_REF:0000123",
        }
    ]


def test_gocam_seed_yaml_round_trips_as_pathway_record() -> None:
    model = load_gocam_model(FIXTURE)
    text = yaml.safe_dump(gocam_to_pathway_record(model), sort_keys=False)

    assert validate_record(yaml.safe_load(text)).id == "gomodel:YeastPathways_GLYCOLYSIS"
