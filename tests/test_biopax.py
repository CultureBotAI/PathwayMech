from __future__ import annotations

from pathlib import Path

import yaml

from pathwaymech.biopax import biopax_to_pathway_record, load_biopax
from pathwaymech.schema import validate_record

FIXTURE = Path("tests/fixtures/biopax/R-TEST.owl")


def test_biopax_converts_to_valid_reactome_record() -> None:
    root = load_biopax(FIXTURE)

    record = validate_record(biopax_to_pathway_record(root, "Reactome:R-TEST"))

    assert record.id == "Reactome:R-TEST"
    assert record.label == "Mini BioPAX glycolysis"
    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "CHEBI:58289", "label": "2-phosphonato-D-glycerate(3-)"},
    ]
    assert record.reactions == [
        {
            "id": "Reactome:R-TEST/reaction",
            "label": "phosphoglycerate mutase reaction",
        }
    ]
    assert [edge["predicate"] for edge in record.mechanistic_edges] == [
        "consumes",
        "produces",
    ]
    assert record.references == [
        {"id": "PMID:12345678", "title": "BioPAX publication PMID:12345678"}
    ]


def test_biopax_seed_yaml_round_trips_as_pathbank_record() -> None:
    root = load_biopax(FIXTURE)
    text = yaml.safe_dump(
        biopax_to_pathway_record(root, "PathBank:SMP0000001"),
        sort_keys=False,
    )

    assert validate_record(yaml.safe_load(text)).id == "PathBank:SMP0000001"
