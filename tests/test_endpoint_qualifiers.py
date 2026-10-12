"""Qualifications are part of an edge claim across validation, viewing and export."""

from __future__ import annotations

import copy
import csv
import io
import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml

import pathwaymech.cli as cli
from pathwaymech.cli import _record_page
from pathwaymech.graph_view import graph_html
from pathwaymech.kgx import kgx_edges, kgx_nodes, render_kgx, write_kgx
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.strict import TARGET_CLASS, validator
from pathwaymech.wikipathways import _unique_edges

NS = {"s": "http://www.w3.org/2000/svg"}


@pytest.fixture
def raw():
    evidence = [{"reference_id": "PMID:1", "source_assertion": "Synthetic assay edge.",
                 "source_locator": "Fixture assay results"}]
    construct = {"endpoint": "object", "kind": "experimental_construct",
                 "description": "Ser1-NagB assay construct; no sequence equivalence elsewhere.",
                 "evidence": [{"reference_id": "PMID:2", "source_assertion":
                               "Synthetic fixture: cleavage yields an N-terminal serine.",
                               "source_locator": "Fixture construct methods"}]}
    tagged = {"endpoint": "subject", "kind": "experimental_construct",
              "description": "His-tagged U-PII preparation; occupancy is assay-dependent.",
              "evidence": [{"reference_id": "PMID:3", "quote": "Synthetic tagged PII fixture."}]}
    state = {"endpoint": "subject", "kind": "molecular_state",
             "description": "cAMP-bound CRP in the specified promoter context.",
             "evidence": [{"reference_id": "PMID:2", "source_assertion":
                           "Synthetic fixture: CRP binds cAMP.",
                           "source_locator": "Fixture state"}]}
    return {
        "id": "MetaCyc:GLCMANNANAUT-PWY", "label": "Endpoint qualification fixture",
        "description": "Software fixture, not an independently curated pathway.",
        "pathway_type": "test", "taxa": [{"id": "NCBITaxon:562", "label": "E. coli"}],
        "participants": [
            {"id": "MetaCyc:URIDYLYL-PII", "label": "U-PII", "category": "protein"},
            {"id": "UniProtKB:P0A759", "label": "NagB", "category": "protein"},
            {"id": "UniProtKB:P0ACJ8", "label": "CRP", "category": "complex"},
            {"id": "CHEBI:15377", "label": "water", "category": "small_molecule"},
        ],
        "reactions": [{"id": "MetaCyc:RXN-1", "label": "Fixture reaction"}],
        "mechanistic_edges": [
            {"id": "assay", "subject": "MetaCyc:URIDYLYL-PII", "predicate": "activates",
             "object": "UniProtKB:P0A759", "evidence": evidence,
             "endpoint_qualifiers": [tagged, construct]},
            {"id": "state", "subject": "UniProtKB:P0ACJ8", "predicate": "regulates",
             "object": "MetaCyc:GLCMANNANAUT-PWY", "evidence": evidence,
             "endpoint_qualifiers": [state]},
            {"id": "native", "subject": "MetaCyc:URIDYLYL-PII", "predicate": "regulates",
             "object": "UniProtKB:P0A759", "evidence": evidence},
        ],
        "references": [{"id": f"PMID:{n}", "title": f"Synthetic fixture {n}"} for n in (1, 2, 3)],
    }


@pytest.fixture(scope="module")
def checker():
    return validator()


def test_complete_claim_and_native_state_id_survive_both_validators(raw, checker):
    before = copy.deepcopy(raw)
    record = validate_record(raw)
    assert not checker.validate(raw, TARGET_CLASS).results
    assert record.mechanistic_edges == before["mechanistic_edges"]
    assert record.mechanistic_edges[0]["subject"] == "MetaCyc:URIDYLYL-PII"
    assert raw == before


@pytest.mark.parametrize(("field", "value"), [
    ("endpoint", "target"), ("endpoint", []), ("kind", "variant"), ("kind", None),
    ("description", " "), ("description", "x" * 401),
    ("description", "x" * 400 + "\n"), ("description", None),
    ("evidence", []), ("evidence", None), ("id", "UniProtKB:invented-construct"),
])
def test_invalid_qualifier_fields_fail_both(raw, checker, field, value):
    raw["mechanistic_edges"][0]["endpoint_qualifiers"][0][field] = value
    assert checker.validate(raw, TARGET_CLASS).results
    with pytest.raises(ValidationError, match="endpoint_qualifiers"):
        validate_record(raw)


@pytest.mark.parametrize("value", [None, {}, "construct", ["construct"]])
def test_qualifiers_have_a_closed_list_of_objects_shape(raw, checker, value):
    raw["mechanistic_edges"][0]["endpoint_qualifiers"] = value
    assert checker.validate(raw, TARGET_CLASS).results
    with pytest.raises(ValidationError, match="endpoint_qualifiers"):
        validate_record(raw)


def test_cardinality_and_unique_roles_are_checked(raw, checker):
    qualifiers = raw["mechanistic_edges"][0]["endpoint_qualifiers"]
    qualifiers.append(copy.deepcopy(qualifiers[0]))
    assert checker.validate(raw, TARGET_CLASS).results
    with pytest.raises(ValidationError, match="at most two"):
        validate_record(raw)
    qualifiers.pop()
    qualifiers[1]["endpoint"] = "subject"
    with pytest.raises(ValidationError, match="only once"):
        validate_record(raw)


@pytest.mark.parametrize("target", ["MetaCyc:RXN-1", "MetaCyc:GLCMANNANAUT-PWY",
                                    "NCBITaxon:562", "CHEBI:15377", "MetaCyc:UNKNOWN"])
def test_only_protein_complex_participant_endpoints_can_be_qualified(raw, target):
    raw["mechanistic_edges"][0]["subject"] = target
    with pytest.raises(ValidationError, match="declared protein or complex participant"):
        validate_record(raw)


@pytest.mark.parametrize("category", [None, "gene", "molecular_activity"])
def test_prefix_does_not_supply_the_required_declared_participant_type(raw, category):
    node = raw["participants"][0]
    if category is None:
        node.pop("category")
    else:
        node["category"] = category
    with pytest.raises(ValidationError, match="declared protein or complex participant"):
        validate_record(raw)


def test_ambiguous_duplicate_declarations_do_not_supply_a_protein_type(raw):
    raw["participants"].append({"id": "MetaCyc:URIDYLYL-PII", "label": "untyped duplicate"})
    with pytest.raises(ValidationError, match="declared protein or complex participant"):
        validate_record(raw)


@pytest.mark.parametrize("problem", ["missing-ref", "bad-ref-type", "both", "neither",
                                     "blank", "long", "no-locator", "xml"])
def test_qualifier_evidence_uses_the_existing_native_rules(raw, problem):
    item = raw["mechanistic_edges"][0]["endpoint_qualifiers"][1]["evidence"][0]
    if problem == "missing-ref":
        item["reference_id"] = "PMID:999"
    elif problem == "bad-ref-type":
        item["reference_id"] = []
    elif problem == "both":
        item["quote"] = "A second evidence field."
    elif problem == "neither":
        item.pop("source_assertion")
    elif problem == "blank":
        item["source_assertion"] = " "
    elif problem == "long":
        item["source_assertion"] = "x" * 401
    elif problem == "no-locator":
        item.pop("source_locator")
    else:
        item["source_assertion"] = '<Interaction GraphId="not-human-readable"/>'
    with pytest.raises(ValidationError, match="endpoint_qualifiers.*evidence"):
        validate_record(raw)


def test_full_400_character_description_and_empty_optional_list(raw, checker):
    raw["mechanistic_edges"][0]["endpoint_qualifiers"][0]["description"] = "a\n" + "b" * 398
    assert not checker.validate(raw, TARGET_CLASS).results
    validate_record(raw)
    for edge in raw["mechanistic_edges"]:
        edge["endpoint_qualifiers"] = []
    assert not checker.validate(raw, TARGET_CLASS).results
    with_empty = kgx_edges([validate_record(raw)])
    for edge in raw["mechanistic_edges"]:
        edge.pop("endpoint_qualifiers")
    assert with_empty == kgx_edges([validate_record(raw)])


class QualifierText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current = None
        self.text = {}
        self.cells = {}
        self.role = None
        self.column = -1

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "tr":
            self.column = -1
        elif tag == "td":
            self.column += 1
        elif tag == "div" and attrs.get("class") == "endpoint-qualifier":
            self.current = attrs["id"]
            self.text[self.current] = ""
            self.cells[self.current] = self.column

    def handle_data(self, value):
        if self.current:
            self.text[self.current] += value

    def handle_endtag(self, tag):
        if tag == "div":
            self.current = None


def test_no_javascript_page_keeps_qualifications_beside_correct_endpoints(raw):
    page = _record_page(validate_record(raw))
    parser = QualifierText()
    parser.feed(page)
    for index, edge in enumerate(raw["mechanistic_edges"], 1):
        for qualifier in edge.get("endpoint_qualifiers", []):
            key = f"mechanism-edge-{index}-qualifier-{qualifier['endpoint']}"
            assert parser.cells[key] == {"subject": 0, "object": 2}[qualifier["endpoint"]]
            assert qualifier["description"] in parser.text[key]
            for evidence in qualifier["evidence"]:
                assert evidence["reference_id"] in parser.text[key]
                assert evidence.get("quote", evidence.get("source_assertion")) in parser.text[key]
                if evidence.get("source_locator"):
                    assert evidence["source_locator"] in parser.text[key]


def test_graph_never_attaches_a_qualified_claim_to_the_shared_bare_node(raw):
    record = validate_record(raw)
    before = copy.deepcopy(raw)
    markup = graph_html(record, {}, {})
    start = markup.index('<svg xmlns=')
    svg = ET.fromstring(markup[start:markup.index("</svg>", start) + 6])
    links = svg.findall(".//s:a", NS)
    nodes = {node.attrib["data-node-id"]: node for node in links
             if "data-node-id" in node.attrib}
    edges = [node for node in links if "data-predicate" in node.attrib]
    for index, (edge, view) in enumerate(zip(record.mechanistic_edges, edges, strict=True), 1):
        for role in ("subject", "object"):
            qualifier = next((q for q in edge.get("endpoint_qualifiers", [])
                              if q["endpoint"] == role), None)
            key = view.attrib["data-" + role]
            if qualifier:
                assert key != edge[role] and ":" not in key
                assert view.attrib["data-" + role + "-id"] == edge[role]
                node = nodes[key]
                assert node.attrib["data-base-node-id"] == edge[role]
                assert qualifier["kind"].replace("_", " ") in node.attrib["data-node-label"]
                assert qualifier["description"] in node.attrib["aria-label"]
                assert node.attrib["href"] == f"#mechanism-edge-{index}-qualifier-{role}"
                for evidence in qualifier["evidence"]:
                    assert evidence["reference_id"] in node.attrib["aria-label"]
                    assert evidence.get("quote", evidence.get("source_assertion")) in (
                        node.attrib["aria-label"]
                    )
            else:
                assert key == edge[role]
    assert raw == before
    assert "cAMP-bound CRP" in markup and "Ser1-NagB" in markup


def test_qualification_text_is_escaped_in_both_views(raw):
    attack = '<script>alert("&")</script>'
    raw["mechanistic_edges"][0]["endpoint_qualifiers"][0]["description"] = attack
    page = _record_page(validate_record(raw))
    assert attack not in page
    parser = QualifierText()
    parser.feed(page)
    assert attack in parser.text["mechanism-edge-1-qualifier-subject"]


def test_kgx_roundtrip_retains_qualifier_payload_and_qualifier_only_citations(raw, tmp_path):
    checked = validate_record(raw)
    nodes, edges = write_kgx([checked], tmp_path)
    exported = render_kgx([checked])
    assert nodes.read_text() == exported["nodes.tsv"]
    assert edges.read_text() == exported["edges.tsv"]
    rows = list(csv.DictReader(io.StringIO(exported["edges.tsv"]), delimiter="\t"))
    for edge, row in zip(raw["mechanistic_edges"], rows, strict=True):
        assert row["subject"] == edge["subject"] and row["object"] == edge["object"]
        assert json.loads(row["endpoint_qualifiers"] or "[]") == edge.get("endpoint_qualifiers", [])
    assert rows[0]["source_records"] == "PMID:1|PMID:2|PMID:3"
    assert {ref["id"] for ref in json.loads(rows[0]["reference_metadata"])} == {
        "PMID:1", "PMID:2", "PMID:3",
    }
    assert {node.id for node in kgx_nodes([checked])} == {
        raw["id"],
        *(node["id"] for key in ("taxa", "participants", "reactions") for node in raw[key]),
    }


@pytest.mark.parametrize("change", ["remove", "role-swap", "description", "evidence", "kind"])
def test_identity_and_dedup_do_not_collapse_changed_claims(raw, change):
    original = raw["mechanistic_edges"][0]
    other = copy.deepcopy(original)
    if change == "remove":
        other.pop("endpoint_qualifiers")
    elif change == "role-swap":
        for item in other["endpoint_qualifiers"]:
            item["endpoint"] = {"subject": "object", "object": "subject"}[item["endpoint"]]
    elif change == "description":
        other["endpoint_qualifiers"][1]["description"] = "A different N-terminal construct."
    elif change == "evidence":
        other["endpoint_qualifiers"][1]["evidence"][0]["source_locator"] = "Different location"
    else:
        other["endpoint_qualifiers"][1]["kind"] = "molecular_state"
    raw["mechanistic_edges"] = [original, other]
    rows = kgx_edges([validate_record(raw)])
    assert rows[0].id != rows[1].id
    assert _unique_edges(raw["mechanistic_edges"]) == [original, other]


def test_role_order_and_empty_list_do_not_invent_claim_differences(raw):
    original = raw["mechanistic_edges"][0]
    other = copy.deepcopy(original)
    other["endpoint_qualifiers"].reverse()
    raw["mechanistic_edges"] = [original, other]
    rows = kgx_edges([validate_record(raw)])
    assert rows[0].id == rows[1].id
    assert json.loads(rows[1].endpoint_qualifiers) == other["endpoint_qualifiers"]
    assert _unique_edges(raw["mechanistic_edges"]) == [original]
    original.pop("endpoint_qualifiers")
    other["endpoint_qualifiers"] = []
    assert _unique_edges([original, other]) == [original]


@pytest.mark.parametrize("command", ["export_kgx_main", "render_pages_main"])
@pytest.mark.parametrize("existing", [False, True])
def test_invalid_qualification_cli_fails_before_touching_existing_output(
    raw, tmp_path, command, existing,
):
    data = tmp_path / "data/pathways"
    data.mkdir(parents=True)
    evidence = raw["mechanistic_edges"][0]["endpoint_qualifiers"][0]["evidence"][0]
    evidence["reference_id"] = "PMID:999"
    (data / "record.yaml").write_text(yaml.safe_dump(raw))
    output = tmp_path / ("output/kgx" if command == "export_kgx_main" else "pages")
    if existing:
        output.mkdir(parents=True)
        (output / "sentinel.txt").write_bytes(b"existing output must survive\n")
    before = {str(path.relative_to(tmp_path)): path.read_bytes()
              for path in output.rglob("*") if path.is_file()}
    source = Path(__file__).resolve().parents[1] / "src"
    result = subprocess.run([
        sys.executable, "-B", "-c",
        "from pathlib import Path; import sys; from pathwaymech.cli import " + command
        + "; raise SystemExit(" + command + "([], root=Path(sys.argv[1])))", str(tmp_path),
    ], capture_output=True, text=True, check=False,
        env={**os.environ, "PYTHONPATH": str(source), "PYTHONDONTWRITEBYTECODE": "1"})
    assert result.returncode != 0
    assert "endpoint_qualifiers[0].evidence[0].reference_id is not declared" in result.stderr
    after = {str(path.relative_to(tmp_path)): path.read_bytes()
             for path in output.rglob("*") if path.is_file()}
    assert after == before
    assert output.exists() is existing


def test_provenance_count_includes_qualification_only_evidence(raw, monkeypatch, capsys):
    monkeypatch.setattr(cli, "load_pathway_records", lambda _: [validate_record(raw)])
    assert cli.check_provenance_main() == 0
    assert "checked 6 evidence blocks" in capsys.readouterr().out
