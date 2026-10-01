from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree

import yaml

from pathwaymech.chebi import load_chebi_xrefs
from pathwaymech.kegg import kgml_to_pathway_record, load_kgml
from pathwaymech.schema import validate_record

FIXTURE = Path("tests/fixtures/kegg/map00010.kgml")
CHEBI_FIXTURE = Path("tests/fixtures/chebi/kegg_compounds.obo")


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


def test_kgml_can_map_kegg_compounds_to_chebi() -> None:
    record = validate_record(
        kgml_to_pathway_record(
            load_kgml(FIXTURE),
            load_chebi_xrefs(CHEBI_FIXTURE),
        )
    )

    assert record.participants == [
        {"id": "CHEBI:58272", "label": "CHEBI:58272"},
        {"id": "CHEBI:58289", "label": "CHEBI:58289"},
    ]
    assert record.source_mappings == [
        {
            "subject_id": "KEGG:C00236",
            "subject_label": "3-phospho-D-glycerate",
            "predicate_id": "skos:exactMatch",
            "object_id": "CHEBI:58272",
            "object_label": "3-phosphonato-D-glycerate(3-)",
            "mapping_justification": "semapv:UnspecifiedMatching",
            "confidence": "1.0",
            "source_pathway_id": "KEGG:map00010",
            "source_element_id": "KEGG:R01512/substrate/11",
        },
        {
            "subject_id": "KEGG:C00197",
            "subject_label": "2-phospho-D-glycerate",
            "predicate_id": "skos:exactMatch",
            "object_id": "CHEBI:58289",
            "object_label": "2-phosphonato-D-glycerate(3-)",
            "mapping_justification": "semapv:UnspecifiedMatching",
            "confidence": "1.0",
            "source_pathway_id": "KEGG:map00010",
            "source_element_id": "KEGG:R01512/product/12",
        },
    ]


def test_kgml_skips_unnamed_reaction_participants() -> None:
    root = ElementTree.fromstring(
        """
        <pathway name="path:map00010" title="Glycolysis / Gluconeogenesis">
          <reaction id="1" name="rn:R01512">
            <substrate id="11" />
            <product id="12" name="cpd:C00197" />
          </reaction>
        </pathway>
        """
    )

    record = validate_record(kgml_to_pathway_record(root))

    assert record.participants == [{"id": "KEGG:C00197", "label": "KEGG:C00197"}]
    assert [edge["predicate"] for edge in record.mechanistic_edges] == ["produces"]
