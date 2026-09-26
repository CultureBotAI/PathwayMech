from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree

import yaml

from pathwaymech.schema import validate_record
from pathwaymech.wikipathways import (
    gpml_to_pathway_record,
    load_gpml_pathway,
    wikipathways_fallback_id,
)

FIXTURE = Path("tests/fixtures/wikipathways/WPTEST.gpml")


def test_gpml_converts_to_valid_pathway_record() -> None:
    root = load_gpml_pathway(FIXTURE)

    record = validate_record(gpml_to_pathway_record(root, "WikiPathways:WPTEST"))

    assert record.id == "WikiPathways:WP9999"
    assert record.label == "Mini glycolysis"
    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "CHEBI:58289", "label": "2-phosphonato-D-glycerate(3-)"},
        {"id": "UniProtKB:P12345", "label": "Mini enzyme"},
        {"id": "SGD:S000000001", "label": "Mini SGD enzyme"},
        {"id": "CHEBI:15377", "label": "H2O"},
        {"id": "CHEBI:456215", "label": "AMP"},
    ]
    assert record.reactions == [
        {
            "id": "WikiPathways:WP9999/interaction",
            "label": "WikiPathways:WP9999 interaction interaction",
        },
        {
            "id": "WikiPathways:WP9999/anchored",
            "label": "WikiPathways:WP9999 interaction anchored",
        },
    ]
    assert [
        (edge["subject"], edge["predicate"], edge["object"])
        for edge in record.mechanistic_edges
    ] == [
        ("CHEBI:58272", "consumes", "WikiPathways:WP9999/interaction"),
        ("WikiPathways:WP9999/interaction", "produces", "CHEBI:58289"),
        ("WikiPathways:WP9999/anchored", "produces", "CHEBI:456215"),
        ("CHEBI:15377", "consumes", "WikiPathways:WP9999/anchored"),
        ("SGD:S000000001", "catalyzes", "WikiPathways:WP9999/anchored"),
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

    assert validate_record(yaml.safe_load(text)).id == "WikiPathways:WP9999"


def test_gpml_deduplicates_participants_by_stable_curie() -> None:
    text = FIXTURE.read_text(encoding="utf-8").replace(
        'ID="58289"',
        'ID="CHEBI:58272"',
    )

    record = validate_record(
        gpml_to_pathway_record(ElementTree.fromstring(text), "WikiPathways:WPTEST")
    )

    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "UniProtKB:P12345", "label": "Mini enzyme"},
        {"id": "SGD:S000000001", "label": "Mini SGD enzyme"},
        {"id": "CHEBI:15377", "label": "H2O"},
        {"id": "CHEBI:456215", "label": "AMP"},
    ]
    assert record.mechanistic_edges[1]["object"] == "CHEBI:58272"


def test_wikipathways_fallback_id_uses_filename_accession() -> None:
    assert (
        wikipathways_fallback_id(Path("Sc_NAD_salvage_pathway_V_WP171_20260901.gpml"))
        == "WikiPathways:WP171"
    )
