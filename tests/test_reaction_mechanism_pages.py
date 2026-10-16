"""Visible, navigable mechanistic detail without rewriting a source representation."""
from __future__ import annotations

import copy
import re
from collections import Counter
from dataclasses import asdict, replace
from html.parser import HTMLParser
from xml.etree import ElementTree

import pytest

from pathwaymech.cli import _record_page
from pathwaymech.mechanism_view import mechanism_anchor
from pathwaymech.schema import validate_record


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.elements = []
        self.text = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def handle_data(self, text):
        self.text.append(text)


def _evidence(role):
    return [{"reference_id": f"DOI:{role}", "source_assertion": f"Evidence only for {role}.",
             "source_locator": f"Synthetic source, {role} section"}]


@pytest.fixture
def detail_record():
    """Synthetic IDs exercise representation; they are not biochemical curation."""
    def edge(key, subject, predicate, obj, **extra):
        return dict(key=key, subject=subject, predicate=predicate, object=obj,
                    assertion_status="supported", evidence=_evidence("edge"), **extra)

    raw = {
        "id": "MetaCyc:PAGE-FIXTURE", "label": "Page fixture", "description": "Synthetic",
        "pathway_type": "test", "taxa": [],
        "participants": [
            {"id": f"CHEBI:{n}", "label": label, "category": "small_molecule"}
            for n, label in [(1, "Source input"), (2, "Product"), (3, "Transient detail"),
                             (4, "Interpreted input"), (5, "Isolated source component")]
        ] + [{"id": "UniProtKB:FIXTURE", "label": "Catalyst", "category": "protein"}],
        "reactions": [{"id": "RHEA:1", "label": "Source net", "direction": "left_to_right",
                       "category": "molecular_activity"}],
        "mechanistic_edges": [
            {"id": predicate, "subject": "RHEA:1", "predicate": predicate, "object": identifier,
             "evidence": _evidence("source")}
            for predicate, identifier in [("has_input", "CHEBI:1"), ("has_output", "CHEBI:2")]
        ],
        "detail_only_participant_ids": ["CHEBI:3", "CHEBI:4"],
        "references": [{"id": f"DOI:{role}", "title": f"Reference only for {role}"}
                       for role in ["source", "association", "step", "edge", "hypothesis",
                                    "qualifier", "conflict"]],
    }
    mechanism = {
        "version": 1, "key": "decomposition", "source_reaction_id": "RHEA:1",
        "relation_to_source": "decomposition", "description": "Two detailed changes",
        "evidence": _evidence("association"),
        "source_equation": {"orientation": "reversed",
                            "inputs": [{"participant_id": "CHEBI:2", "coefficient": 1}],
                            "outputs": [{"participant_id": "CHEBI:1", "coefficient": 2}]},
        "steps": [
            {"key": key, "label": "Repeated step label", "description": f"Description {key}",
             "assertion_status": status, "evidence": _evidence("step")}
            for key, status in [("first", "supported"), ("second", "inferred")]
        ],
        "edges": [
            edge("a_in", {"node_id": "CHEBI:1"}, "consumes", {"step_key": "first"}, coefficient=2),
            edge("x_out", {"step_key": "first"}, "produces", {"node_id": "CHEBI:3"}, coefficient=2),
            edge("x_in", {"node_id": "CHEBI:3"}, "consumes", {"step_key": "second"}, coefficient=2),
            edge("b_out", {"step_key": "second"}, "produces", {"node_id": "CHEBI:2"},
                 coefficient=1),
            edge("cat", {"node_id": "UniProtKB:FIXTURE"}, "catalyzes", {"step_key": "first"},
                 endpoint_qualifiers=[{"endpoint": "subject", "kind": "experimental_construct",
                                       "description": "Tagged catalyst only",
                                       "evidence": _evidence("qualifier")}]),
        ],
    }
    mechanism["steps"][0]["hypotheses"] = [
        {"description": "Unobserved intermediate <script>unsafe()</script>",
         "status": "proposed", "evidence": _evidence("hypothesis")}
    ]
    alternate = copy.deepcopy(mechanism)
    alternate.update(key="alternative", relation_to_source="alternative_interpretation")
    alternate["edges"][0]["subject"] = {"node_id": "CHEBI:4"}
    alternate["edges"][0]["assertion_status"] = "proposed"
    alternate["source_conflicts"] = [
        {"source_participant_id": "CHEBI:1", "interpreted_participant_id": "CHEBI:4",
         "side": "inputs", "coefficient": 2, "kind": "constitution", "status": "unresolved",
         "rationale": "Distinct identities & unresolved evidence",
         "evidence": _evidence("conflict")}
    ]
    raw["reaction_mechanisms"] = [mechanism, alternate]
    return validate_record(raw)


def _graphs(page):
    svgs = [ElementTree.fromstring(source)
            for source in re.findall(r"<svg\b.*?</svg>", page, flags=re.DOTALL)]
    return [svg for svg in svgs if svg.get("class") == "pathway-network-svg"]


def _elements(svg, kind):
    return [node for node in svg.iter() if kind in node.get("class", "").split()]


def test_source_membership_and_nested_evidence_are_preserved(detail_record):
    before = asdict(detail_record)
    page = _record_page(detail_record)
    assert asdict(detail_record) == before
    parsed = Page(page)
    text = " ".join(parsed.text)
    source, first, second = _graphs(page)
    source_nodes = {node.get("data-node-id") for node in _elements(source, "graph-node")}
    assert source_nodes == {"CHEBI:1", "CHEBI:2", "CHEBI:5", "UniProtKB:FIXTURE", "RHEA:1"}
    assert "Source pathway representation" in text
    assert "Isolated source component" in text
    assert "Detail only" in text
    for graph in (first, second):
        assert "CHEBI:3" in {node.get("data-node-id") for node in _elements(graph, "graph-node")}
        assert len(_elements(graph, "graph-edge")) == 5
        assert len([node for node in _elements(graph, "graph-node")
                    if node.get("data-node-label") == "Repeated step label"]) == 2
    # Original direction and IDs remain source assertions despite a competing claim.
    actual = Counter((e.get("data-subject"), e.get("data-predicate"), e.get("data-object"))
                     for e in _elements(source, "graph-edge"))
    expected = Counter((e["subject"], e["predicate"], e["object"])
                       for e in detail_record.mechanistic_edges)
    assert actual == expected
    assert all("source-reported" in e.get("aria-label") for e in _elements(source, "graph-edge"))
    assert "Source-reported assertion." in text
    for role in ("association", "step", "edge", "hypothesis", "qualifier", "conflict"):
        assert f"Evidence only for {role}." in text
        assert f"Synthetic source, {role} section" in text
        assert f"Reference only for {role}" in text
    for expected_text in ("constitution difference", "unresolved", "coefficient: 2",
                          "Tagged catalyst only", "The inverse of this source equation",
                          "does not by itself establish physiological", "Location:",
                          "No transport or co-location is inferred."):
        assert expected_text in text
    assert "Unobserved intermediate <script>unsafe()</script>" in text
    assert "<script>unsafe()</script>" not in page
    assert "record-local mechanistic claim" in text
    assert "Repeated step label — record-local mechanistic claim 1" in text
    assert "Repeated step label — record-local mechanistic claim 2" in text


def test_source_isolates_remain_visible_with_details_and_no_source_edges(detail_record):
    record = replace(detail_record, mechanistic_edges=[])
    source, first, second = _graphs(_record_page(record))
    assert not _elements(source, "graph-edge")
    source_nodes = {node.get("data-node-id") for node in _elements(source, "graph-node")}
    assert source_nodes == {"CHEBI:1", "CHEBI:2", "CHEBI:5", "UniProtKB:FIXTURE", "RHEA:1"}
    assert len(_elements(first, "graph-edge")) == len(_elements(second, "graph-edge")) == 5


def test_all_local_navigation_and_control_ids_are_unique_and_resolve(detail_record):
    page = _record_page(detail_record)
    parsed = Page(page)
    ids = [attrs["id"] for _, attrs in parsed.elements if "id" in attrs]
    assert len(ids) == len(set(ids))
    for _, attrs in parsed.elements:
        target = attrs.get("href", "")
        if target.startswith("#"):
            assert target[1:] in ids, target
        for attribute in ("aria-labelledby", "aria-describedby", "for"):
            for target in attrs.get(attribute, "").split():
                assert target in ids, (attribute, target)
    for class_name in ("graph-node-picker", "graph-native-size", "graph-viewport"):
        controls = [attrs for _, attrs in parsed.elements
                    if class_name in attrs.get("class", "").split()]
        assert len(controls) == 3
        assert len({control["id"] for control in controls}) == 3
    for mechanism in detail_record.reaction_mechanisms:
        for edge in mechanism["edges"]:
            target = mechanism_anchor(detail_record.id, mechanism["key"], "edge", edge["key"])
            assert target in ids
        for step in mechanism["steps"]:
            target = mechanism_anchor(detail_record.id, mechanism["key"], "step", step["key"])
            assert target in ids
    # Scoped graph markers must also be globally unambiguous.
    markers = [node.get("id") for svg in _graphs(page) for node in svg.iter()
               if node.tag.endswith("marker")]
    assert len(markers) == len(set(markers)) == 3


def test_multiline_claim_labels_reserve_separate_evidence_link_boxes(detail_record):
    for graph in _graphs(_record_page(detail_record)):
        boxes = []
        for edge in _elements(graph, "graph-edge"):
            labels = _elements(edge, "graph-edge-label")
            x = float(labels[0].get("x"))
            top = min(float(label.get("y")) for label in labels) - 14
            bottom = max(float(label.get("y")) for label in labels) + 6
            for old_x, old_top, old_bottom in boxes:
                if x == old_x:
                    assert bottom + 4 <= old_top or old_bottom + 4 <= top
            boxes.append((x, top, bottom))
            assert bottom < float(graph.get("height"))


def test_explicit_step_location_is_readable(detail_record):
    raw = asdict(detail_record)
    raw["participants"].append({"id": "GO:1", "label": "Test compartment",
                                "category": "cellular_component"})
    for mechanism in raw["reaction_mechanisms"]:
        for step in mechanism["steps"]:
            mechanism["edges"].append({
                "key": "where_" + step["key"], "subject": {"step_key": step["key"]},
                "predicate": "occurs_in", "object": {"node_id": "GO:1"},
                "assertion_status": "supported", "evidence": _evidence("edge"),
            })
    page = _record_page(validate_record(raw))
    assert "Recorded step location:" in page
    assert "Test compartment" in page


def test_source_declarations_remain_when_only_nested_edges_exist(detail_record):
    raw = asdict(detail_record)
    raw["mechanistic_edges"] = []
    source, first, second = _graphs(_record_page(validate_record(raw)))
    assert not _elements(source, "graph-edge")
    assert {node.get("data-node-id") for node in _elements(source, "graph-node")} == {
        "CHEBI:1", "CHEBI:2", "CHEBI:5", "UniProtKB:FIXTURE", "RHEA:1",
    }
    assert len(_elements(first, "graph-edge")) == len(_elements(second, "graph-edge")) == 5
