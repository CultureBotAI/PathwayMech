from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree

import yaml

from pathwaymech.biopax import biopax_to_pathway_record, load_biopax
from pathwaymech.schema import validate_record

FIXTURE = Path("tests/fixtures/biopax/R-TEST.owl")


def test_biopax_converts_to_valid_reactome_record() -> None:
    root = load_biopax(FIXTURE)

    record = validate_record(biopax_to_pathway_record(root, "Reactome:R-TEST"))

    assert record.id == "Reactome:R-TEST-12345"
    assert record.label == "Mini BioPAX glycolysis"
    assert record.taxa == [{"id": "NCBITaxon:12345", "label": "Mini test microbe"}]
    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "CHEBI:58289", "label": "2-phosphonato-D-glycerate(3-)"},
        {"id": "UniProtKB:P12345", "label": "Mini enzyme"},
    ]
    assert {"id": "UniProtKB:P99999", "label": "Mini carrier"} not in record.participants
    assert record.reactions == [
        {
            "id": "Reactome:R-TEST-67890",
            "label": "phosphoglycerate mutase reaction",
        }
    ]
    assert [edge["predicate"] for edge in record.mechanistic_edges] == [
        "consumes",
        "produces",
        "catalyzes",
    ]
    assert record.mechanistic_edges[0]["evidence"] == [
        {
            "reference_id": "PMID:12345678",
            "quote": "Mini BioPAX reaction evidence.",
        }
    ]
    assert record.mechanistic_edges[2] == {
        "id": "biopax-edge-3",
        "subject": "UniProtKB:P12345",
        "predicate": "catalyzes",
        "object": "Reactome:R-TEST-67890",
        "evidence": [
            {
                "reference_id": "PMID:12345678",
                "quote": "Mini BioPAX reaction evidence.",
            }
        ],
    }
    assert record.references == [
        {"id": "PMID:87654321", "title": "Pathway-only BioPAX publication"},
        {"id": "PMID:12345678", "title": "Mini BioPAX publication"}
    ]
    assert record.source_mappings == [
        {
            "subject_id": "UniProt:P12345",
            "subject_label": "Mini enzyme",
            "predicate_id": "skos:exactMatch",
            "object_id": "UniProtKB:P12345",
            "object_label": "Mini enzyme",
            "mapping_justification": "semapv:UnspecifiedMatching",
            "confidence": "1.0",
            "source_pathway_id": "Reactome:R-TEST-12345",
            "source_element_id": "mini_enzyme",
        }
    ]


def test_biopax_seed_yaml_round_trips_as_pathbank_record() -> None:
    root = load_biopax(FIXTURE)
    text = yaml.safe_dump(
        biopax_to_pathway_record(root, "PathBank:SMP0000001"),
        sort_keys=False,
    )

    assert validate_record(yaml.safe_load(text)).id == "PathBank:SMP0000001"
    assert "id: PathBank:SMP0000001/reaction" in text


def test_biopax_truncates_long_reaction_comments() -> None:
    long_quote = "a" * 401
    text = FIXTURE.read_text(encoding="utf-8").replace(
        "Mini BioPAX reaction evidence.",
        long_quote,
    )

    record = validate_record(
        biopax_to_pathway_record(ElementTree.fromstring(text), "Reactome:R-TEST")
    )

    quote = record.mechanistic_edges[0]["evidence"][0]["quote"]
    assert quote == "a" * 400


def test_biopax_deduplicates_participants_by_stable_curie() -> None:
    text = FIXTURE.read_text(encoding="utf-8").replace(
        'rdf:resource="#two_pga_xref"',
        'rdf:resource="#three_pga_xref"',
    )

    record = validate_record(
        biopax_to_pathway_record(ElementTree.fromstring(text), "Reactome:R-TEST")
    )

    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "UniProtKB:P12345", "label": "Mini enzyme"},
    ]
    assert record.mechanistic_edges[1]["object"] == "CHEBI:58272"
