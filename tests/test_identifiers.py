"""Offline acceptance tests for the pathway corpus identifier gate."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml

from pathwaymech import cli
from pathwaymech.identifiers import identifier_errors


@pytest.fixture
def corpus(tmp_path):
    """A recursive corpus and independently authored authority data."""
    root = tmp_path / "repo"
    record_path = root / "data/pathways/nested/example.yaml"
    record = {
        "id": "GO:0000001",
        "label": "example biological process",
        "taxa": [{"id": "NCBITaxon:562", "label": "Escherichia coli"}],
        "participants": [{"id": "CHEBI:15377", "label": "water"}],
        "reactions": [{"id": "RHEA:12345", "label": "example reaction"}],
    }
    terms = {
        "GO:0000001": {
            "label": "example biological process",
            "synonyms": ["accepted process synonym"],
            "source": "fixture",
        },
        "NCBITaxon:562": {
            "label": "Escherichia coli", "synonyms": [], "source": "fixture",
        },
        "CHEBI:15377": {"label": "water", "synonyms": [], "source": "fixture"},
        "RHEA:12345": {
            "label": "example reaction", "synonyms": [], "source": "fixture",
        },
        "gomodel:example": {
            "label": "source pathway", "synonyms": [], "source": "fixture",
        },
    }
    snapshot = {
        "version": 1,
        "sources": {
            "fixture": {
                "url": "https://example.org/source",
                "version": "fixture-v1",
                "sha256": "a" * 64,
                "license": "CC0",
            },
        },
        "terms": terms,
    }
    snapshot_path = root / "data/identifier_authorities/test.json"
    config = {
        "version": 1,
        "namespaces": {
            prefix: {
                "snapshot": "data/identifier_authorities/test.json",
                "policy": "canonical",
            }
            for prefix in ("GO", "NCBITaxon", "CHEBI", "RHEA", "gomodel")
        },
        "contextual_labels": [],
    }
    config_path = root / "conf/identifier_policy.yaml"
    for path in (record_path, snapshot_path, config_path):
        path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text(yaml.safe_dump(record), encoding="utf-8")
    snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
    config_path.write_text(yaml.safe_dump(config), encoding="utf-8")
    return {
        "root": root,
        "record": record,
        "record_path": record_path,
        "config": config,
        "config_path": config_path,
        "snapshot": snapshot,
        "snapshot_path": snapshot_path,
    }


def _write_record(corpus):
    corpus["record_path"].write_text(yaml.safe_dump(corpus["record"]), encoding="utf-8")


def _write_config(corpus):
    corpus["config_path"].write_text(yaml.safe_dump(corpus["config"]), encoding="utf-8")


def _write_snapshot(corpus):
    corpus["snapshot_path"].write_text(json.dumps(corpus["snapshot"]), encoding="utf-8")


def _named_node(record, section):
    return record if section == "identity" else record[section][0]


def test_resolves_all_named_surfaces_in_a_nested_record(corpus):
    assert identifier_errors(corpus["root"]) == []
    assert cli.check_identifiers_main([], root=corpus["root"]) == 0


@pytest.mark.parametrize("section", ["identity", "taxa", "participants", "reactions"])
def test_nonexistent_supported_identifier_fails_each_surface(corpus, section):
    node = _named_node(corpus["record"], section)
    prefix = node["id"].split(":", 1)[0]
    node["id"] = f"{prefix}:999999999999999999999"
    _write_record(corpus)

    errors = identifier_errors(corpus["root"])

    assert errors
    assert any(node["id"] in error for error in errors)
    assert cli.check_identifiers_main([], root=corpus["root"]) != 0


@pytest.mark.parametrize("section", ["identity", "taxa", "participants", "reactions"])
def test_wrong_canonical_label_fails_each_surface(corpus, section):
    _named_node(corpus["record"], section)["label"] = "obviously wrong canonical label"
    _write_record(corpus)

    assert identifier_errors(corpus["root"])
    assert cli.check_identifiers_main([], root=corpus["root"]) != 0


def test_a_bad_nested_record_is_checked_alongside_a_good_root_record(corpus):
    top_level = corpus["root"] / "data/pathways/good.yaml"
    top_level.write_text(yaml.safe_dump(corpus["record"]), encoding="utf-8")
    corpus["record"]["id"] = "GO:999999999999999999999"
    _write_record(corpus)

    assert identifier_errors(corpus["root"])


def test_synonyms_require_the_explicit_synonym_policy(corpus):
    corpus["record"]["label"] = "accepted process synonym"
    _write_record(corpus)
    assert identifier_errors(corpus["root"])

    corpus["config"]["namespaces"]["GO"]["policy"] = "canonical_or_synonym"
    _write_config(corpus)
    assert identifier_errors(corpus["root"]) == []


def _contextual_reaction(corpus):
    corpus["record"]["id"] = "gomodel:example"
    corpus["record"]["label"] = "source pathway"
    corpus["record"]["reactions"] = [{"id": "GO:0000001", "label": "source display text"}]
    corpus["config"]["contextual_labels"] = [{
        "namespace": "GO",
        "sections": ["reactions"],
        "record_prefixes": ["gomodel"],
        "reason": "Reaction display text retained from the source pathway.",
    }]
    _write_record(corpus)
    _write_config(corpus)


def test_scoped_contextual_label_is_preserved_but_id_must_resolve(corpus):
    _contextual_reaction(corpus)
    original = corpus["record_path"].read_bytes()

    assert identifier_errors(corpus["root"]) == []
    assert corpus["record_path"].read_bytes() == original

    corpus["record"]["reactions"][0]["id"] = "GO:999999999999999999999"
    _write_record(corpus)
    assert identifier_errors(corpus["root"])


def test_cross_reference_label_cannot_be_used_as_a_canonical_authority(corpus):
    term = corpus["snapshot"]["terms"]["GO:0000001"]
    term["label_kind"] = "source_context"
    _write_snapshot(corpus)
    # Even an exact text match cannot establish a canonical label from a cross-reference.
    assert identifier_errors(corpus["root"])
    _contextual_reaction(corpus)
    assert identifier_errors(corpus["root"]) == []
    corpus["record"]["reactions"][0]["id"] = "GO:999999999999999999999"
    _write_record(corpus)
    assert identifier_errors(corpus["root"])


@pytest.mark.parametrize("outside_scope", ["record_prefix", "section", "namespace"])
def test_contextual_waiver_cannot_escape_its_declared_scope(corpus, outside_scope):
    _contextual_reaction(corpus)
    if outside_scope == "record_prefix":
        corpus["record"]["id"] = "GO:0000001"
        corpus["record"]["label"] = "example biological process"
    elif outside_scope == "section":
        corpus["record"]["participants"] = copy.deepcopy(corpus["record"]["reactions"])
    else:
        corpus["record"]["reactions"][0]["id"] = "RHEA:12345"
    _write_record(corpus)

    assert identifier_errors(corpus["root"])


def test_unknown_namespace_fails_instead_of_being_skipped(corpus):
    corpus["record"]["participants"][0]["id"] = "CHBEI:15377"
    _write_record(corpus)

    assert identifier_errors(corpus["root"])
    assert cli.check_identifiers_main([], root=corpus["root"]) != 0


def test_empty_corpus_fails(corpus):
    corpus["record_path"].unlink()

    assert identifier_errors(corpus["root"])
    assert cli.check_identifiers_main([], root=corpus["root"]) != 0


@pytest.mark.parametrize("body", ["{}", "null", "[]", "label: no identifiers\n"])
def test_records_with_no_selected_pairs_fail(corpus, body):
    corpus["record_path"].write_text(body, encoding="utf-8")

    assert identifier_errors(corpus["root"])


@pytest.mark.parametrize("section", ["id", "label", "taxa", "participants", "reactions"])
def test_missing_required_named_surface_fails(corpus, section):
    del corpus["record"][section]
    _write_record(corpus)

    assert identifier_errors(corpus["root"])


@pytest.mark.parametrize("section", ["taxa", "participants", "reactions"])
def test_empty_optional_node_collection_keeps_record_identity_check(corpus, section):
    corpus["record"][section] = []
    _write_record(corpus)

    assert identifier_errors(corpus["root"]) == []
    corpus["record"]["id"] = "GO:999999999999999999999"
    _write_record(corpus)
    assert identifier_errors(corpus["root"])


@pytest.mark.parametrize("problem", ["missing", "malformed_json", "empty_terms", "not_mapping"])
def test_unavailable_or_empty_authority_snapshot_fails(corpus, problem):
    if problem == "missing":
        corpus["snapshot_path"].unlink()
    elif problem == "malformed_json":
        corpus["snapshot_path"].write_text("{broken", encoding="utf-8")
    elif problem == "not_mapping":
        corpus["snapshot_path"].write_text("[]", encoding="utf-8")
    else:
        corpus["snapshot"]["terms"] = {}
        _write_snapshot(corpus)

    assert identifier_errors(corpus["root"])
    assert cli.check_identifiers_main([], root=corpus["root"]) != 0


@pytest.mark.parametrize("field", ["url", "version", "sha256", "license"])
def test_authority_provenance_cannot_be_omitted(corpus, field):
    del corpus["snapshot"]["sources"]["fixture"][field]
    _write_snapshot(corpus)

    assert identifier_errors(corpus["root"])


@pytest.mark.parametrize("problem", ["unattributed_term", "blank_label", "bad_synonyms"])
def test_malformed_authority_terms_fail(corpus, problem):
    term = corpus["snapshot"]["terms"]["GO:0000001"]
    if problem == "unattributed_term":
        term["source"] = "missing-source"
    elif problem == "blank_label":
        term["label"] = ""
    else:
        term["synonyms"] = "a string is not a synonym list"
    _write_snapshot(corpus)

    assert identifier_errors(corpus["root"])


@pytest.mark.parametrize("problem", ["missing", "malformed_yaml", "empty", "empty_namespaces"])
def test_missing_or_unusable_policy_fails(corpus, problem):
    if problem == "missing":
        corpus["config_path"].unlink()
    elif problem == "malformed_yaml":
        corpus["config_path"].write_text("[broken", encoding="utf-8")
    elif problem == "empty":
        corpus["config_path"].write_text("{}", encoding="utf-8")
    else:
        corpus["config"]["namespaces"] = {}
        _write_config(corpus)

    assert identifier_errors(corpus["root"])
    assert cli.check_identifiers_main([], root=corpus["root"]) != 0


@pytest.mark.parametrize("policy", ["canoncal", "id_only", "", None])
def test_unknown_label_policy_is_rejected(corpus, policy):
    corpus["config"]["namespaces"]["GO"]["policy"] = policy
    _write_config(corpus)

    assert identifier_errors(corpus["root"])


@pytest.mark.parametrize(
    "problem",
    ["blank_reason", "empty_sections", "empty_prefixes", "unknown_section", "unknown_namespace"],
)
def test_malformed_contextual_rules_fail(corpus, problem):
    _contextual_reaction(corpus)
    rule = corpus["config"]["contextual_labels"][0]
    if problem == "blank_reason":
        rule["reason"] = ""
    elif problem == "empty_sections":
        rule["sections"] = []
    elif problem == "empty_prefixes":
        rule["record_prefixes"] = []
    elif problem == "unknown_section":
        rule["sections"] = ["reaction_typo"]
    else:
        rule["namespace"] = "CHBEI"
    _write_config(corpus)

    assert identifier_errors(corpus["root"])


def test_explicit_policy_path_is_used(corpus):
    alternate = corpus["root"] / "alternate-policy.yaml"
    corpus["config_path"].rename(alternate)

    assert identifier_errors(corpus["root"], config_path=alternate) == []
    assert cli.check_identifiers_main(["--config", str(alternate)], root=corpus["root"]) == 0
    assert cli.check_identifiers_main([], root=corpus["root"]) != 0


def test_ci_quality_gate_executes_identifier_validation(corpus, monkeypatch):
    """Exercise the real checker through QC; bypass only unrelated gates."""
    for stage in (
        "validate_main", "_validate_strict_gate", "_validate_history_gate",
        "check_provenance_main", "validate_sources_main", "check_docs_main",
        "deep_research_contract_main", "check_pages_main",
    ):
        monkeypatch.setattr(cli, stage, lambda: 0)
    actual_check = cli.check_identifiers_main
    checked_roots: list[Path] = []

    def fixture_check(*args, **kwargs):
        checked_roots.append(corpus["root"])
        return actual_check([], root=corpus["root"])

    monkeypatch.setattr(cli, "check_identifiers_main", fixture_check)

    assert cli.run_qc_main() == 0
    assert checked_roots == [corpus["root"]]
    corpus["record"]["label"] = "wrong canonical label from an incoming PR"
    _write_record(corpus)
    assert cli.run_qc_main() != 0
    assert checked_roots == [corpus["root"], corpus["root"]]
