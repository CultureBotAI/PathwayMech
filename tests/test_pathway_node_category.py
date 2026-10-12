"""Nested pathway definitions retain their type across validation and exports."""

from dataclasses import replace
from xml.etree import ElementTree

import pytest

from pathwaymech.graph_view import graph_html
from pathwaymech.kgx import kgx_nodes
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.strict import TARGET_CLASS, validator


@pytest.fixture
def raw():
    return {
        "id": "MetaCyc:TEST-PARENT", "label": "Synthetic parent pathway",
        "description": "Software fixture, not a curated biological assertion.",
        "pathway_type": "test", "taxa": [{"id": "NCBITaxon:562", "label": "E. coli"}],
        "participants": [
            {"id": "CHEBI:15377", "label": "water", "category": "small_molecule"},
            {"id": "GO:0005737", "label": "cytoplasm", "category": "cellular_component"},
        ],
        "reactions": [{"id": "MetaCyc:TEST-CHILD", "label": "Synthetic child pathway",
                       "category": "pathway"}],
        "mechanistic_edges": [{
            "id": "part", "subject": "MetaCyc:TEST-PARENT", "predicate": "has_part",
            "object": "MetaCyc:TEST-CHILD",
            "evidence": [{"reference_id": "PMID:1", "quote": "Synthetic membership fixture."}],
        }],
        "references": [{"id": "PMID:1", "title": "Synthetic fixture"}],
    }


def test_nested_pathway_passes_both_schemas_and_exports_as_only_pathway(raw):
    record = validate_record(raw)
    assert not validator().validate(raw, TARGET_CLASS).results
    child = replace(record, id="MetaCyc:TEST-CHILD", label="Synthetic child pathway",
                    reactions=[], mechanistic_edges=[])
    for records in ([record], [child, record], [record, child]):
        nodes = {node.id: node for node in kgx_nodes(records)}
        assert nodes["MetaCyc:TEST-CHILD"].category == "biolink:Pathway"
    rendered = graph_html(record, {}, {})
    start = rendered.index('<svg xmlns=')
    diagram = ElementTree.fromstring(rendered[start:rendered.index('</svg>', start)+6])
    node = diagram.find(".//*[@data-node-id='MetaCyc:TEST-CHILD']")
    assert node.attrib['data-kind'] == 'pathway'
    assert 'Declared type: pathway' in ''.join(node.itertext())


@pytest.mark.parametrize("predicate", ["consumes", "produces", "located_in"])
def test_pathway_is_not_a_physical_participant(raw, predicate):
    raw["participants"].append(raw["reactions"].pop())
    edge = raw["mechanistic_edges"][0]
    edge["predicate"] = predicate
    edge["subject"] = "MetaCyc:TEST-CHILD"
    edge["object"] = "MetaCyc:TEST-PARENT"
    if predicate == "produces":
        edge["subject"], edge["object"] = edge["object"], edge["subject"]
    if predicate == "located_in":
        edge["object"] = "GO:0005737"
    with pytest.raises(ValidationError, match="metabolite|physical participant"):
        validate_record(raw)


def test_pathway_may_occur_in_a_compartment(raw):
    edge = raw["mechanistic_edges"][0]
    edge.update(subject="MetaCyc:TEST-CHILD", predicate="occurs_in", object="GO:0005737")
    validate_record(raw)


def test_omitted_category_does_not_infer_pathway_from_id_or_label(raw):
    raw["reactions"][0].pop("category")
    nodes = {node.id: node for node in kgx_nodes([validate_record(raw)])}
    assert nodes["MetaCyc:TEST-CHILD"].category == "biolink:BiochemicalReaction"
