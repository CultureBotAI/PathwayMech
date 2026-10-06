import csv
import json
from copy import deepcopy

import pytest

from pathwaymech.cli import _record_page
from pathwaymech.kgx import kgx_edges, kgx_nodes, write_kgx
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.strict import TARGET_CLASS, validator


@pytest.fixture
def record():
    return {
        "id": "gomodel:test", "label": "Test", "description": "A source assertion fixture.",
        "pathway_type": "test", "taxa": [],
        "participants": [
            {"id": "GO:0005737", "label": "cytoplasm", "category": "cellular_component"},
            {"id": "CHEBI:15377", "label": "water", "category": "small_molecule"},
        ],
        "reactions": [{"id": "gomodel:test/r1", "label": "activity"}],
        "mechanistic_edges": [{
            "id": "e1", "subject": "gomodel:test/r1", "predicate": "occurs_in",
            "object": "GO:0005737", "evidence": [{
                "reference_id": "gomodel:test", "source_assertion": "Activity occurs in cytoplasm.",
                "source_locator": "model.json /facts/0 (BFO:0000066)",
            }],
        }],
        "references": [{"id": "gomodel:test", "title": "Source model"}],
    }


@pytest.fixture(scope="module")
def checker():
    return validator()


def test_structured_source_and_compartment_survive_validation_rendering_and_export(record, checker):
    assert not checker.validate(record, TARGET_CLASS).results
    checked = validate_record(record)
    page = _record_page(checked)
    assert "Source assertion:" in page and "model.json /facts/0" in page
    assert "<blockquote>" not in page
    nodes = {node.id: node.category for node in kgx_nodes([checked])}
    assert nodes["GO:0005737"] == "biolink:CellularComponent"
    assert kgx_edges([checked])[0].predicate == "BFO:0000066"


@pytest.mark.parametrize("change", [
    lambda e: e.pop("source_locator"),
    lambda e: e.__setitem__("source_locator", " "),
    lambda e: e.pop("source_assertion"),
    lambda e: e.__setitem__("source_assertion", " "),
    lambda e: e.__setitem__("source_assertion", "x" * 401),
    lambda e: e.__setitem__("quote", "This is not also a quotation."),
    lambda e: (e.__setitem__("quote", "A quotation"), e.pop("source_locator")),
])
def test_untraceable_or_ambiguous_structured_evidence_fails_both_validators(
    record, checker, change,
):
    change(record["mechanistic_edges"][0]["evidence"][0])
    assert checker.validate(record, TARGET_CLASS).results
    with pytest.raises(ValidationError):
        validate_record(record)


def test_verbatim_quotes_remain_distinct(record, checker):
    record["mechanistic_edges"][0]["evidence"] = [{
        "reference_id": "gomodel:test", "quote": "A verbatim source excerpt.",
    }]
    assert not checker.validate(record, TARGET_CLASS).results
    page = _record_page(validate_record(record))
    assert "<blockquote>A verbatim source excerpt.</blockquote>" in page


def test_occurs_in_cannot_target_a_small_molecule(record):
    record["mechanistic_edges"][0]["object"] = "CHEBI:15377"
    with pytest.raises(ValidationError, match="cellular_component"):
        validate_record(record)


def test_has_input_direction_and_aggregate_pathway_products(record):
    edge = record["mechanistic_edges"][0]
    edge.update(predicate="has_input", object="CHEBI:15377")
    validate_record(record)
    broken = deepcopy(record)
    broken["mechanistic_edges"][0].update(subject="CHEBI:15377", object="gomodel:test/r1")
    with pytest.raises(ValidationError, match="activity or pathway"):
        validate_record(broken)
    edge.update(subject=record["id"], predicate="produces")
    validate_record(record)


@pytest.mark.parametrize("kind", ["cellular_component", "biological_process", "molecular_activity"])
@pytest.mark.parametrize("predicate", ["consumes", "produces"])
def test_context_nodes_cannot_be_consumed_as_metabolites(record, kind, predicate):
    record["participants"][0]["category"] = kind
    subject, obj = "GO:0005737", "gomodel:test/r1"
    if predicate == "produces":
        subject, obj = obj, subject
    record["mechanistic_edges"][0].update(subject=subject, predicate=predicate, object=obj)
    with pytest.raises(ValidationError, match="context node as a metabolite"):
        validate_record(record)


@pytest.mark.parametrize("kind", [None, "small_molecule", "gene", "molecular_activity"])
def test_cofactor_subject_must_be_a_supported_enzyme(record, kind):
    record["participants"][0] = {
        "id": "CHEBI:18420", "label": "magnesium(2+)", "category": "cofactor",
    }
    if kind is None:
        record["participants"][1].pop("category")
    else:
        record["participants"][1]["category"] = kind
    record["mechanistic_edges"][0].update(
        subject="CHEBI:15377", predicate="has_cofactor", object="CHEBI:18420",
    )
    with pytest.raises(ValidationError, match="enzyme protein or complex"):
        validate_record(record)


def test_kgx_preserves_qualified_evidence_provenance_and_direction(record, tmp_path):
    record["reactions"][0].update(category="molecular_activity", direction="right_to_left")
    record["mechanistic_edges"][0]["description"] = "Location is inferred from similarity."
    record["references"][0].update(
        url="https://example.org/model.json", source_version="v2", source_sha256="a" * 64,
    )
    checked = validate_record(record)
    nodes_path, edges_path = write_kgx([checked], tmp_path)
    with nodes_path.open() as stream:
        nodes = {n["id"]: n for n in csv.DictReader(stream, delimiter="\t")}
    with edges_path.open() as stream:
        edge = next(csv.DictReader(stream, delimiter="\t"))
    assert nodes["gomodel:test/r1"]["direction"] == "right_to_left"
    assert nodes["gomodel:test/r1"]["source_category"] == "molecular_activity"
    assert edge["description"] == record["mechanistic_edges"][0]["description"]
    assert json.loads(edge["evidence"]) == record["mechanistic_edges"][0]["evidence"]
    assert json.loads(edge["reference_metadata"]) == record["references"]


def test_explicit_node_kinds_override_prefix_guesses_in_either_record_order(record):
    inferred = deepcopy(record)
    inferred["id"] = "gomodel:other"
    inferred["participants"][0].pop("category")
    inferred["mechanistic_edges"] = []
    first, second = validate_record(record), validate_record(inferred)
    for ordered in ([first, second], [second, first]):
        node = next(n for n in kgx_nodes(ordered) if n.id == "GO:0005737")
        assert node.category == "biolink:CellularComponent"
        assert node.source_category == "cellular_component"


def test_shared_identifier_keeps_each_records_direction_and_label(record):
    record["reactions"][0]["direction"] = "left_to_right"
    other = deepcopy(record)
    other["id"] = "gomodel:other"
    other["reactions"][0].update(direction="right_to_left", label="reverse pathway flow")
    first, second = validate_record(record), validate_record(other)
    for ordered in ([first, second], [second, first]):
        node = next(n for n in kgx_nodes(ordered) if n.id == "gomodel:test/r1")
        assert node.direction == ""
        contexts = {x["record_id"]: x for x in json.loads(node.source_contexts)}
        assert contexts["gomodel:test"]["direction"] == "left_to_right"
        assert contexts["gomodel:other"]["direction"] == "right_to_left"
        assert contexts["gomodel:other"]["label"] == "reverse pathway flow"


def test_typed_and_legacy_proteins_can_have_cofactors(record):
    record["participants"][0] = {
        "id": "CHEBI:18420", "label": "magnesium(2+)", "category": "cofactor",
    }
    record["participants"][1] = {"id": "UniProtKB:P00001", "label": "enzyme"}
    record["mechanistic_edges"][0].update(
        subject="UniProtKB:P00001", predicate="has_cofactor", object="CHEBI:18420",
    )
    validate_record(record)
    for category in ("protein", "complex"):
        record["participants"][1]["category"] = category
        validate_record(record)


def test_kgx_preserves_alternative_cofactor_qualification(record):
    record["participants"] = [
        {"id": "UniProtKB:P9WK17", "label": "malate synthase G", "category": "protein"},
        {"id": "CHEBI:29035", "label": "manganese(2+)", "category": "cofactor"},
    ]
    evidence = {
        "reference_id": "gomodel:test",
        "source_assertion": (
            "Mn(2+) can replace Mg(2+); these are alternatives, not joint requirements."
        ),
        "source_locator": "comments[commentType='COFACTOR'].note",
    }
    record["mechanistic_edges"][0].update(
        subject="UniProtKB:P9WK17", predicate="has_cofactor", object="CHEBI:29035",
        evidence=[evidence], description="Alternative catalytic metal.",
    )
    edge = kgx_edges([validate_record(record)])[0]
    assert json.loads(edge.evidence) == [evidence]
    assert edge.description == "Alternative catalytic metal."
