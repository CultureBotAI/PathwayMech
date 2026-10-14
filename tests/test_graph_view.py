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


def assert_separate_label_boxes(root):
    """Check conservative 11 px text extents, including the page's white halo."""
    width, height = float(root.attrib["width"]), float(root.attrib["height"])
    boxes = []
    for label in root.findall('.//s:text[@class="graph-edge-label"]', NS):
        x, y = float(label.attrib["x"]), float(label.attrib["y"])
        text_width = 8 + sum(4 if char == " " else 10 for char in label.text)
        box = (x - text_width / 2, y - 14, x + text_width / 2, y + 6)
        assert 0 < box[0] < box[2] < width
        assert 0 < box[1] < box[3] < height
        boxes.append(box)
    node_boxes = []
    for node in elements(root, "graph-node"):
        shape = node.find('s:rect', NS)
        if shape is not None:
            x, y = float(shape.attrib["x"]), float(shape.attrib["y"])
            node_boxes.append((x, y, x + float(shape.attrib["width"]),
                               y + float(shape.attrib["height"])))
        else:
            coordinates = [tuple(map(float, pair.split(","))) for pair in
                           node.find('s:polygon', NS).attrib["points"].split()]
            xs, ys = zip(*coordinates, strict=True)
            node_boxes.append((min(xs), min(ys), max(xs), max(ys)))

    def separated(a, b):
        return a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1]

    for index, box in enumerate(boxes):
        assert all(separated(box, other) for other in boxes[index + 1:])
        assert all(separated(box, node_box) for node_box in node_boxes)


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
    assert_separate_label_boxes(root)
    assert root.findall('.//s:path[@class="graph-label-leader"]', NS)
    # A dense gutter expands the bottom, while leaving the nodes and header put.
    assert height > max(float(n.find("s:rect", NS).attrib["y"])
                        + float(n.find("s:rect", NS).attrib["height"]) for n in nodes)
    for leader in root.findall('.//s:path[@class="graph-label-leader"]', NS):
        assert "marker-end" not in leader.attrib
        for command, raw in re.findall(r"([MHV])([^MHV]+)", leader.attrib["d"]):
            numbers = [float(value) for value in raw.replace(",", " ").split()]
            if command == "M":
                assert 0 < numbers[0] < width and 0 < numbers[1] < height
            else:
                assert all(0 < value < (height if command == "V" else width)
                           for value in numbers)


def test_crossing_edges_with_distinct_predicates_keep_separate_linked_labels():
    item = record(
        participants=[{"id": "a", "label": "A"}, {"id": "b", "label": "B"}],
        reactions=[{"id": "r", "label": "R"}, {"id": "s", "label": "S"}],
        mechanistic_edges=[edge("a", "r", "consumes"), edge("a", "s", "consumes"),
                           edge("b", "r", "regulates"), edge("b", "s", "regulates")],
    )
    root = diagram(item)
    actual = elements(root, "graph-edge")
    # The two crossing cubics have the same midpoint. Their paths remain intact,
    # while the predicates now have separate boxes and their original evidence.
    assert actual[1].find("s:path", NS).attrib["d"] == (
        "M310,118.0 C416.0,118.0 416.0,262.0 522,262.0")
    assert actual[2].find("s:path", NS).attrib["d"] == (
        "M310,262.0 C416.0,262.0 416.0,118.0 522,118.0")
    assert actual[1].find("s:text", NS).text == "consumes"
    assert actual[2].find("s:text", NS).text == "regulates"
    assert actual[1].attrib["href"] == "#mechanism-edge-2"
    assert actual[2].attrib["href"] == "#mechanism-edge-3"
    assert_separate_label_boxes(root)
    leader = actual[2].find('s:path[@class="graph-label-leader"]', NS)
    assert leader is not None and "marker-end" not in leader.attrib
    # The leader ends at t=.01 on its own cubic, not the other crossing edge.
    match = re.fullmatch(r"M[^H]+ H[^V]+ V([^H]+) H(.+)", leader.attrib["d"])
    ay, ax = map(float, match.groups())
    assert ax == pytest.approx(313.148412)
    assert ay == pytest.approx(261.957088)
    assert float(root.attrib["height"]) == 372
    assert graph_html(item, {}, {}) == graph_html(item, {}, {})


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
