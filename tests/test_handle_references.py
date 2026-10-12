"""Handle references are citations, never biological node identifiers."""

import csv
import importlib
import io
import json
from pathlib import Path

import pytest
import yaml
from lxml import html

from pathwaymech.cli import _record_page
from pathwaymech.identifiers import _load_authority, _load_policy
from pathwaymech.kgx import render_kgx
from pathwaymech.schema import ALLOWED_CURIE_PREFIXES, ValidationError, validate_record
from pathwaymech.strict import TARGET_CLASS, validator

HANDLE = "hdl:1993/32279"
ISSUING_URL = "https://mspace.lib.umanitoba.ca/handle/1993/32279"
ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def checker():
    return validator()


@pytest.fixture
def record():
    return {
        "id": "MetaCyc:TEST-HANDLE", "label": "Handle reference fixture",
        "description": "Synthetic validation fixture, not a scientific claim.",
        "pathway_type": "test",
        "taxa": [{"id": "NCBITaxon:562", "label": "Escherichia coli"}],
        "participants": [{
            "id": "CHEBI:15377", "label": "water", "category": "small_molecule",
        }],
        "reactions": [{
            "id": "RHEA:16109", "label": "fixture activity", "category": "molecular_activity",
        }],
        "mechanistic_edges": [{
            "id": "e1", "subject": "CHEBI:15377", "predicate": "consumes",
            "object": "RHEA:16109", "evidence": [{
                "reference_id": HANDLE, "source_assertion": "Synthetic validation assertion.",
                "source_locator": "fixture",
            }],
        }],
        "references": [{
            "id": HANDLE, "title": "Handle reference test fixture", "url": ISSUING_URL,
            "source_version": "fixture",
            "source_sha256": "e0276c90358e3f177441ec3f71e99454727a31099a50920a325c7cc31cff8fc8",
        }],
    }


def set_reference(record, identifier):
    record["references"][0]["id"] = identifier
    record["mechanistic_edges"][0]["evidence"][0]["reference_id"] = identifier


@pytest.mark.parametrize("identifier", [HANDLE, "hdl:20.500.12345/Ab_1-2.3"])
def test_supported_handles_are_valid_declared_references(record, checker, identifier):
    set_reference(record, identifier)
    validate_record(record)
    assert not checker.validate(record, TARGET_CLASS).results


@pytest.mark.parametrize("prefix", sorted(ALLOWED_CURIE_PREFIXES))
def test_existing_reference_prefixes_remain_valid(record, checker, prefix):
    set_reference(record, prefix + ":fixture")
    validate_record(record)
    assert not checker.validate(record, TARGET_CLASS).results


@pytest.mark.parametrize("identifier", [
    "hdl:", "hdl:/32279", "hdl:1993/", "hdl:1993", "hdl:1993/32 279",
    "hdl:1993/32279\n", "hdl:1993/32\t279", "hdl:1993/32279/extra",
    "hdl:1993//32279", "hdl:1993/.32279", "hdl:1993/é", "hdl:1993/32279?x",
    "hdl:1993/32279#x", "hdl:1993../32279", "hdl:abc/32279", "HDL:1993/32279",
    "https://hdl.handle.net/1993/32279", "OTHER:1993/32279",
])
def test_malformed_or_unsupported_reference_ids_fail_both(record, checker, identifier):
    set_reference(record, identifier)
    with pytest.raises(ValidationError):
        validate_record(record)
    assert checker.validate(record, TARGET_CLASS).results


def test_undeclared_handle_evidence_is_rejected_by_native_local_check(record):
    record["mechanistic_edges"][0]["evidence"][0]["reference_id"] = "hdl:1993/99999"
    with pytest.raises(ValidationError, match="reference"):
        validate_record(record)


@pytest.mark.parametrize("collection", [None, "taxa", "participants", "reactions"])
def test_handle_cannot_be_a_biological_identifier(record, checker, collection):
    assert "hdl" not in ALLOWED_CURIE_PREFIXES
    if collection is None:
        record["id"] = HANDLE
    else:
        record[collection].append({"id": HANDLE, "label": "Invalid biological node"})
    with pytest.raises(ValidationError, match="prefix"):
        validate_record(record)
    assert checker.validate(record, TARGET_CLASS).results


@pytest.mark.parametrize("endpoint", ["subject", "object"])
def test_declared_reference_is_not_a_declared_edge_endpoint(record, endpoint):
    record["mechanistic_edges"][0][endpoint] = HANDLE
    with pytest.raises(ValidationError, match="does not resolve locally"):
        validate_record(record)


@pytest.mark.parametrize("name", ["sources.json", "ontology.json"])
def test_authority_snapshots_cannot_issue_handle_terms(tmp_path, name):
    path = tmp_path / name
    path.write_text(json.dumps({
        "version": 1,
        "sources": {"fixture": {
            "url": ISSUING_URL, "version": "fixture", "license": "fixture", "sha256": "a" * 64,
        }},
        "terms": {HANDLE: {"label": "fixture", "synonyms": [], "source": "fixture"}},
    }), encoding="utf-8")
    with pytest.raises(ValueError, match="invalid authority identifier"):
        _load_authority(path)


def test_authority_policy_cannot_configure_handle_namespace(tmp_path):
    path = tmp_path / "policy.yaml"
    path.write_text(yaml.safe_dump({
        "version": 1, "namespaces": {"hdl": {"snapshot": "sources.json", "policy": "exact"}},
        "contextual_labels": [],
    }), encoding="utf-8")
    with pytest.raises(ValueError, match="unknown configured namespace: hdl"):
        _load_policy(path, tmp_path)


@pytest.mark.parametrize("reference", [
    HANDLE, "RHEA:29170", "RHEA:30251", "CHEBI:9999999", "GO:9999999", "NCBITaxon:9999999",
])
def test_native_snapshot_collectors_do_not_select_citations(
    record, tmp_path, monkeypatch, reference,
):
    set_reference(record, reference)
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    source = importlib.import_module("build_source_identifier_snapshot")
    ontology = importlib.import_module("build_ontology_identifier_snapshot")
    (tmp_path / "record.yaml").write_text(yaml.safe_dump(record), encoding="utf-8")
    assert source.corpus_ids(tmp_path) == {
        "MetaCyc:TEST-HANDLE", "NCBITaxon:562", "CHEBI:15377", "RHEA:16109",
    }
    assert ontology.walk_identifiers(record, {"CHEBI", "GO", "NCBITaxon", "RHEA"}) == {
        "NCBITaxon:562", "CHEBI:15377", "RHEA:16109",
    }


@pytest.mark.parametrize("reference", [HANDLE, "RHEA:29170", "RHEA:30251"])
def test_reference_url_and_metadata_survive_page_and_kgx_without_citation_node(record, reference):
    set_reference(record, reference)
    checked = validate_record(record)
    page = html.fromstring(_record_page(checked))
    assert page.xpath("//a[@href=$url]", url=ISSUING_URL)
    assert reference in page.text_content()
    assert not page.xpath("//*[@data-node-id=$identifier]", identifier=reference)
    exported = render_kgx([checked])
    nodes = list(csv.DictReader(io.StringIO(exported["nodes.tsv"]), delimiter="\t"))
    edges = list(csv.DictReader(io.StringIO(exported["edges.tsv"]), delimiter="\t"))
    assert reference not in {node["id"] for node in nodes}
    assert len(edges) == 1
    assert json.loads(edges[0]["reference_metadata"]) == record["references"]
    assert json.loads(edges[0]["evidence"]) == record["mechanistic_edges"][0]["evidence"]
    assert edges[0]["source_records"] == reference
