"""Faithfulness, bounds and safe progressive enhancement of pathway SVGs."""

import copy
import re
import xml.etree.ElementTree as ET
from types import SimpleNamespace

import pytest

from pathwaymech.graph_view import graph_html

NS = {"s": "http://www.w3.org/2000/svg"}


def record(**changes):
    values = dict(id="test:pathway", label="Test pathway", taxa=[], reactions=[],
                  participants=[], mechanistic_edges=[], gene_clusters=[])
    return SimpleNamespace(**(values | changes))


def edge(subject, obj, predicate="produces"):
    return {"subject": subject, "object": obj, "predicate": predicate,
            "description": "Exact assertion", "evidence": [{"reference_id": "PMID:123"}]}


def diagram(item, labels=None, anchors=None):
    rendered = graph_html(item, labels or {}, anchors or {})
    start = rendered.index('<svg xmlns=')
    return ET.fromstring(rendered[start:rendered.index("</svg>", start) + 6])


def elements(root, name):
    return [item for item in root.findall(".//s:a", NS)
            if name in item.attrib.get("class", "").split()]


def test_declared_types_directions_edges_ids_and_evidence_are_preserved():
    item = record(
        participants=[{"id": "a", "label": "Same", "category": "small_molecule"},
                      {"id": "b", "label": "Same", "category": "protein"},
                      {"id": "alone", "label": "Isolated"}],
        reactions=[{"id": "r", "label": "Reaction", "direction": "REVERSIBLE"}],
        mechanistic_edges=[edge("a", "r", "consumes"), edge("b", "r", "catalyzes"),
                           edge("r", "a"), edge("r", "a", "has_output"),
                           edge("r", "r", "regulates")],
    )
    before = copy.deepcopy(item)
    root = diagram(item, anchors={"a": "component-1"})
    nodes = {node.attrib["data-node-id"]: node for node in elements(root, "graph-node")}
    assert set(nodes) == {"a", "b", "alone", "r"}
    assert nodes["a"].attrib["data-node-label"] == nodes["b"].attrib["data-node-label"]
    assert nodes["a"].attrib["data-kind"] == "chemical"
    assert nodes["b"].attrib["data-kind"] == "protein"
    assert nodes["alone"].attrib["data-kind"] == "participant"
    assert nodes["a"].attrib["href"] == "#component-1"
    assert "Source reaction direction: REVERSIBLE" in "".join(nodes["r"].itertext())
    actual = elements(root, "graph-edge")
    assert [(e.attrib["data-subject"], e.attrib["data-predicate"], e.attrib["data-object"])
            for e in actual] == [(e["subject"], e["predicate"], e["object"])
                                 for e in item.mechanistic_edges]
    assert [e.attrib["href"] for e in actual] == [f"#mechanism-edge-{i}" for i in range(1, 6)]
    assert len({e.find("s:path", NS).attrib["d"] for e in actual}) == 5
    assert all("PMID:123" in "".join(e.itertext()) for e in actual)
    assert all(e.find("s:path", NS).attrib.get("marker-end") for e in actual)
    assert item == before


def test_empty_cluster_has_no_invented_network_and_taxa_only_appear_when_asserted():
    empty = graph_html(record(gene_clusters=[{"id": "cluster:1"}]), {}, {})
    assert "No supported network is recorded" in empty
    assert "<svg" not in empty
    item = record(participants=[{"id": "a", "label": "A"}],
                  taxa=[{"id": "taxon:1", "label": "Used"},
                        {"id": "taxon:2", "label": "Scope only"}],
                  mechanistic_edges=[edge("a", "test:pathway", "part_of"),
                                     edge("test:pathway", "taxon:1", "occurs_in")])
    root = diagram(item)
    assert {n.attrib["data-node-id"] for n in elements(root, "graph-node")} == {
        "a", "test:pathway", "taxon:1"}
    assert all("graph-edge-context" in e.attrib["class"] for e in elements(root, "graph-edge"))
    item.mechanistic_edges.append(edge("outside", "a"))
    with pytest.raises(ValueError, match="not declared"):
        diagram(item)


def test_hostile_labels_and_anchor_values_are_text_not_markup():
    attack = '<script>alert("&")</script>'
    item = record(label=attack, participants=[{"id": attack, "label": "A<sup>2</sup> " + attack}],
                  mechanistic_edges=[edge(attack, attack)])
    root = diagram(item, anchors={attack: 'x" onload="bad'})
    assert root.find(".//s:script", NS) is None
    node = elements(root, "graph-node")[0]
    assert node.attrib["data-node-label"] == "A2 " + attack
    assert node.attrib["href"] == '#x" onload="bad'
    assert "onload" not in node.attrib
    assert all(n.attrib["tabindex"] == "0" for n in elements(root, "graph-node"))
    assert all(n.attrib["tabindex"] == "0" for n in elements(root, "graph-edge"))
    assert root.attrib["aria-labelledby"]


def test_individual_node_heights_and_dense_routing_coordinates_stay_in_bounds():
    item = record(participants=[{"id": "a", "label": "Short"},
                                {"id": "b", "label": "A very long scientific label " * 9}],
                  mechanistic_edges=[edge("a", "b")] + [edge("b", "a") for _ in range(30)]
                  + [edge("b", "b") for _ in range(30)])
    root = diagram(item)
    width, height = float(root.attrib["width"]), float(root.attrib["height"])
    nodes = elements(root, "graph-node")
    assert float(nodes[0].find("s:rect", NS).attrib["y"]) <= 250
    assert float(nodes[0].find("s:rect", NS).attrib["height"]) < float(
        nodes[1].find("s:rect", NS).attrib["height"])
    for line in elements(root, "graph-edge"):
        path = line.find("s:path", NS).attrib["d"]
        for command, raw in re.findall(r"([MHVC])([^MHVC]+)", path):
            numbers = [float(value) for value in raw.replace(",", " ").split()]
            if command == "H":
                assert all(0 <= value <= width for value in numbers)
            elif command == "V":
                assert all(0 <= value <= height for value in numbers)
            else:
                assert all(0 <= value <= width for value in numbers[::2])
                assert all(0 <= value <= height for value in numbers[1::2])
        label = line.find("s:text", NS)
        assert 0 < float(label.attrib["x"]) < width
        assert 0 < float(label.attrib["y"]) < height
    paths = [e.find("s:path", NS).attrib["d"] for e in elements(root, "graph-edge")]
    assert len(set(paths)) == len(paths)


def test_deterministic_markup_progressive_controls_and_plain_text_picker():
    item = record(participants=[{"id": "a", "label": "A<sub>2</sub>"}],
                  mechanistic_edges=[edge("a", "a")])
    first = graph_html(item, {}, {})
    assert first == graph_html(item, {}, {})
    assert 'class="graph-tools" hidden' in first
    assert 'id="graph-node-picker"' in first
    assert '<option value="a">A2 — a</option>' in first
    assert 'id="graph-native-size"' in first
    assert 'id="graph-viewport" tabindex="0"' in first
    assert "1 node · 1 asserted directed edge" in first
    assert "<script" not in first
    other = record(id="other:pathway", participants=item.participants,
                   mechanistic_edges=item.mechanistic_edges)
    def marker(r):
        return diagram(r).find(".//s:marker", NS).attrib["id"]

    assert marker(item) != marker(other)


def test_identifier_prefix_does_not_infer_a_category_or_silently_override_roles():
    item = record(participants=[{"id": "CHEBI:1", "label": "Unclassified"},
                                {"id": "same", "label": "Shared", "category": "protein"}],
                  reactions=[{"id": "same", "label": "Shared"}],
                  mechanistic_edges=[edge("same", "CHEBI:1")])
    nodes = {n.attrib["data-node-id"]: n for n in elements(diagram(item), "graph-node")}
    assert nodes["CHEBI:1"].attrib["data-kind"] == "participant"
    assert nodes["same"].attrib["data-kind"] == "participant"
    assert "Declared type: protein" in "".join(nodes["same"].itertext())
    assert "Declared type: reaction/activity" in "".join(nodes["same"].itertext())
