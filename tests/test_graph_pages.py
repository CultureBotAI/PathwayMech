"""Integration checks for faithful, navigable record-page networks."""
from __future__ import annotations

import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

import pytest
import yaml

from pathwaymech.cli import _record_page, render_pages_main, render_site
from pathwaymech.schema import validate_record

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ("assets/pathway-network.js", "assets/pathway-network.css")


class Page(HTMLParser):
    def __init__(self, source: str):
        super().__init__()
        self.elements: list[tuple[str, dict[str, str | None]]] = []
        self.rows: dict[str, list[str]] = {}
        self.current_row: str | None = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag == "tr":
            self.current_row = attrs.get("id")
            if self.current_row:
                self.rows[self.current_row] = []

    def handle_endtag(self, tag):
        if tag == "tr":
            self.current_row = None

    def handle_data(self, data):
        if self.current_row:
            self.rows[self.current_row].append(data)


def svg_elements(page: str, class_name: str) -> list[ElementTree.Element]:
    matches = re.findall(r"<svg\b.*?</svg>", page, flags=re.DOTALL)
    assert matches, "A record with mechanistic edges must render an SVG network"
    svgs = [ElementTree.fromstring(source) for source in matches]
    svgs = [svg for svg in svgs if "pathway-network-svg" in svg.get("class", "").split()]
    assert len(svgs) == 1, "The page must contain one complete pathway network"
    return [element for svg in svgs for element in svg.iter()
            if class_name in element.get("class", "").split()]


@pytest.fixture(scope="module")
def records():
    return {
        path.stem: validate_record(yaml.load(path.read_text(), Loader=yaml.CSafeLoader))
        for path in sorted((ROOT / "data" / "pathways").glob("*.yaml"))
    }


@pytest.fixture
def raw_record():
    return {
        "id": "gomodel:network-test", "label": "Network test", "description": "Test record",
        "pathway_type": "test", "taxa": [{"id": "NCBITaxon:1", "label": "root"}],
        "participants": [
            {"id": "CHEBI:15377", "label": "water", "category": "small_molecule"},
            {"id": "CHEBI:15378", "label": "proton", "category": "small_molecule"},
        ],
        "reactions": [{"id": "gomodel:network-test/r1", "label": "reaction"}],
        "mechanistic_edges": [{
            "id": "source-edge", "subject": "gomodel:network-test/r1",
            "predicate": "has_input", "object": "CHEBI:15377", "evidence": [{
                "reference_id": "gomodel:network-test", "source_assertion": "Recorded input.",
                "source_locator": "model.json#/facts/0",
            }],
        }],
        "references": [{"id": "gomodel:network-test", "title": "Source model"}],
    }


def test_every_published_graph_preserves_directed_edges_and_evidence_targets(records):
    """No loss, reversal, or deduplication in the page-to-graph integration."""
    for name, record in records.items():
        page = _record_page(record)
        parsed = Page(page)
        rendered = svg_elements(page, "graph-edge")
        expected = Counter((edge["subject"], edge["predicate"], edge["object"])
                           for edge in record.mechanistic_edges)
        actual = Counter((edge.get("data-subject"), edge.get("data-predicate"),
                          edge.get("data-object")) for edge in rendered)
        assert actual == expected, name
        assert len(rendered) == len(record.mechanistic_edges), name
        by_target = {edge.get("href"): edge for edge in rendered}
        assert len(by_target) == len(rendered), name
        for index, edge in enumerate(record.mechanistic_edges, 1):
            row_id = f"mechanism-edge-{index}"
            assert f"#{row_id}" in by_target, (name, row_id)
            diagram_edge = by_target[f"#{row_id}"]
            assert (diagram_edge.get("data-subject"), diagram_edge.get("data-predicate"),
                    diagram_edge.get("data-object")) == (
                        edge["subject"], edge["predicate"], edge["object"]
                    ), (name, row_id)
            row = " ".join(parsed.rows[row_id])
            for evidence in edge["evidence"]:
                assert evidence["reference_id"] in row, (name, row_id)
                if "source_assertion" in evidence:
                    assert evidence["source_assertion"] in row, (name, row_id)
                if "source_locator" in evidence:
                    assert evidence["source_locator"] in row, (name, row_id)
        ids = [attrs["id"] for _, attrs in parsed.elements if attrs.get("id")]
        assert len(ids) == len(set(ids)), name


@pytest.mark.parametrize("name", [
    "zymosterol-biosynthesis",  # self-loop
    "sphingolipid-biosynthesis-yeast",  # parallel and opposing edges
    "palmitoleate-biosynthesis",  # isolated declared component
    "linearmycin-biosynthetic-gene-cluster",  # pathway endpoint
    "pyruvate-fermentation-to-acetoin-iii",  # identical labels, distinct identities
    "peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways",  # largest node count
])
def test_real_graph_nodes_retain_declared_identities_and_component_navigation(records, name):
    record = records[name]
    page = _record_page(record)
    parsed = Page(page)
    nodes = svg_elements(page, "graph-node")
    actual = [node.get("data-node-id") for node in nodes]
    assert len(actual) == len(set(actual))
    declared = {node["id"] for node in record.participants + record.reactions}
    endpoints = {edge[key] for edge in record.mechanistic_edges for key in ("subject", "object")}
    assert set(actual) == declared | endpoints
    for node in nodes:
        identifier = node.get("data-node-id")
        if identifier not in declared:
            continue
        target = node.get("href", "")
        assert target.startswith("#")
        assert identifier in " ".join(parsed.rows[target[1:]])


@pytest.mark.parametrize("direction", ["left_to_right", "right_to_left", "reversible"])
def test_source_direction_is_node_metadata_without_rewriting_edges(raw_record, direction):
    raw_record["reactions"][0]["direction"] = direction
    page = _record_page(validate_record(raw_record))
    nodes = svg_elements(page, "graph-node")
    activity = next(node for node in nodes
                    if node.get("data-node-id") == "gomodel:network-test/r1")
    title = " ".join("".join(child.itertext()) for child in activity.iter()
                     if child.tag.rsplit("}", 1)[-1] == "title")
    assert direction.replace("_", " ") in title.replace("_", " ")
    edge, = svg_elements(page, "graph-edge")
    assert edge.get("data-subject") == "gomodel:network-test/r1"
    assert edge.get("data-object") == "CHEBI:15377"
    assert edge.get("data-predicate") == "has_input"


def test_repeated_source_edge_ids_still_link_to_separate_evidence_rows(raw_record):
    raw_record["mechanistic_edges"].append({
        **raw_record["mechanistic_edges"][0], "predicate": "has_output", "evidence": [{
            "reference_id": "gomodel:network-test", "quote": "A separate supporting excerpt.",
        }],
    })
    page = _record_page(validate_record(raw_record))
    rendered = svg_elements(page, "graph-edge")
    assert {edge.get("href") for edge in rendered} == {
        "#mechanism-edge-1", "#mechanism-edge-2",
    }
    parsed = Page(page)
    assert "Recorded input." in " ".join(parsed.rows["mechanism-edge-1"])
    assert "A separate supporting excerpt." in " ".join(parsed.rows["mechanism-edge-2"])


def test_empty_record_does_not_fabricate_graph_edges(raw_record):
    raw_record["mechanistic_edges"] = []
    page = _record_page(validate_record(raw_record))
    parsed = Page(page)
    assert not any("graph-edge" in attrs.get("class", "").split()
                   for _, attrs in parsed.elements)
    assert not any(attrs.get("href", "").startswith("#mechanism-edge-")
                   for _, attrs in parsed.elements)
    assert "No mechanistic edges" in page


def test_graph_assets_are_local_and_owned_by_site_rendering(raw_record):
    files = render_site([validate_record(raw_record)])
    for asset in ASSETS:
        assert files[asset].strip()
    page = next(text for path, text in files.items() if path.startswith("records/"))
    parsed = Page(page)
    scripts = [attrs["src"] for tag, attrs in parsed.elements if tag == "script" and "src" in attrs]
    styles = [attrs["href"] for tag, attrs in parsed.elements
              if tag == "link" and attrs.get("rel") == "stylesheet"]
    assert "../assets/pathway-network.js" in scripts
    assert "../assets/pathway-network.css" in styles
    assert all(not url.startswith(("http:", "https:", "//")) for url in scripts + styles)


@pytest.mark.parametrize("asset", ASSETS)
def test_stale_graph_asset_fails_site_gate_and_render_restores_it(tmp_path, raw_record, asset):
    source_dir = tmp_path / "data" / "pathways"
    source_dir.mkdir(parents=True)
    (source_dir / "test.yaml").write_text(yaml.safe_dump(raw_record))
    (tmp_path / "pages").mkdir()
    (tmp_path / "pages" / "style.css").write_text("body {}\n")
    (tmp_path / "pages" / ".nojekyll").write_text("\n")
    assert render_pages_main([], root=tmp_path) == 0
    target = tmp_path / "pages" / asset
    original = target.read_bytes()
    target.write_text("stale asset\n")
    assert render_pages_main(["--check"], root=tmp_path) == 1
    assert target.read_text() == "stale asset\n"
    assert render_pages_main([], root=tmp_path) == 0
    assert target.read_bytes() == original
    assert render_pages_main(["--check"], root=tmp_path) == 0
