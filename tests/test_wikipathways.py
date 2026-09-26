from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree

import yaml

from pathwaymech.schema import validate_record
from pathwaymech.wikipathways import gpml_to_pathway_record, load_gpml_pathway

FIXTURE = Path("tests/fixtures/wikipathways/WPTEST.gpml")


def test_gpml_converts_to_valid_pathway_record() -> None:
    root = load_gpml_pathway(FIXTURE)

    record = validate_record(gpml_to_pathway_record(root, "WikiPathways:WPTEST"))

    assert record.id == "WikiPathways:WPTEST"
    assert record.label == "Mini glycolysis"
    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "CHEBI:58289", "label": "2-phosphonato-D-glycerate(3-)"},
        {"id": "UniProtKB:P12345", "label": "Mini enzyme"},
    ]
    assert record.reactions == [
        {
            "id": "WikiPathways:WPTEST/interaction",
            "label": "WikiPathways:WPTEST interaction interaction",
        }
    ]
    assert [edge["predicate"] for edge in record.mechanistic_edges] == [
        "consumes",
        "produces",
    ]
    assert record.references == [
        {"id": "PMID:12345678", "title": "WikiPathways publication PMID:12345678"}
    ]


def test_gpml_seed_yaml_round_trips_as_pathway_record() -> None:
    root = load_gpml_pathway(FIXTURE)
    text = yaml.safe_dump(
        gpml_to_pathway_record(root, "WikiPathways:WPTEST"),
        sort_keys=False,
    )

    assert validate_record(yaml.safe_load(text)).id == "WikiPathways:WPTEST"


def test_gpml_deduplicates_participants_by_stable_curie() -> None:
    text = FIXTURE.read_text(encoding="utf-8").replace(
        'ID="CHEBI:58289"',
        'ID="CHEBI:58272"',
    )

    record = validate_record(
        gpml_to_pathway_record(ElementTree.fromstring(text), "WikiPathways:WPTEST")
    )

    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "UniProtKB:P12345", "label": "Mini enzyme"},
    ]
    assert record.mechanistic_edges[1]["object"] == "CHEBI:58272"
