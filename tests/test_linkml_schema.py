"""The closed LinkML schema describes every record, and each rule in it bites.

A schema that accepts the corpus proves nothing until a record breaking each
rule is shown to be rejected; the cases below each change exactly one thing.
"""

from __future__ import annotations

import copy
import importlib.util
import re
from pathlib import Path

import pytest
import yaml
from linkml_runtime.utils.schemaview import SchemaView

import pathwaymech.cli as cli
from pathwaymech.schema import ALLOWED_CURIE_PREFIXES, ALLOWED_EDGE_PREDICATES
from pathwaymech.strict import SCHEMA_PATH, TARGET_CLASS, strict_errors, validator

ROOT = Path(__file__).resolve().parents[1]
RECORDS = sorted((ROOT / "data" / "pathways").glob("*.yaml"))


@pytest.fixture(scope="module")
def checker():
    return validator()


@pytest.fixture(scope="module")
def record() -> dict:
    return yaml.safe_load(RECORDS[0].read_text(encoding="utf-8"))


def test_every_record_validates_in_closed_mode() -> None:
    assert strict_errors(RECORDS, ROOT) == []


def _edge(r: dict) -> dict:
    return r["mechanistic_edges"][0]


def _evidence(r: dict) -> dict:
    return _edge(r)["evidence"][0]


CASES = {
    "an undeclared record key": lambda r: r.__setitem__("notes", "x"),
    "an undeclared node key": lambda r: r["participants"][0].__setitem__("role", "x"),
    "an undeclared edge key": lambda r: _edge(r).__setitem__("weight", 1),
    "an undeclared evidence key": lambda r: _evidence(r).__setitem__("page", 3),
    "a predicate outside the enum": lambda r: _edge(r).__setitem__("predicate", "causes"),
    "a node CURIE with an unknown prefix": lambda r: r["participants"][0].__setitem__(
        "id", "FOO:1"
    ),
    "a record id that is not a CURIE": lambda r: r.__setitem__("id", "nocolon"),
    "a reference with neither title nor citation": lambda r: r["references"].__setitem__(
        0, {"id": r["references"][0]["id"]}
    ),
    "a quote longer than 400 characters": lambda r: _evidence(r).__setitem__("quote", "x" * 401),
    "a blank quote": lambda r: _evidence(r).__setitem__("quote", "   "),
    "an edge with no evidence": lambda r: _edge(r).__setitem__("evidence", []),
    "a missing required field": lambda r: r.pop("pathway_type"),
    "a blank label": lambda r: r.__setitem__("label", "  "),
}


@pytest.mark.parametrize("case", CASES, ids=list(CASES))
def test_a_record_breaking_one_rule_is_rejected(checker, record, case) -> None:
    broken = copy.deepcopy(record)
    CASES[case](broken)
    assert checker.validate(broken, TARGET_CLASS).results, f"{case} was accepted"


def test_the_quote_limit_is_400_characters_not_fewer(checker, record) -> None:
    edited = copy.deepcopy(record)
    _evidence(edited)["quote"] = "a\n" + "b" * 398
    assert not checker.validate(edited, TARGET_CLASS).results


def test_the_schema_and_the_python_validator_name_the_same_predicates() -> None:
    enum = SchemaView(str(SCHEMA_PATH)).get_enum("EdgePredicateEnum")
    assert set(enum.permissible_values) == ALLOWED_EDGE_PREDICATES


def test_the_schema_and_the_python_validator_allow_the_same_prefixes() -> None:
    view = SchemaView(str(SCHEMA_PATH))
    patterns = {
        view.induced_slot("id", name).pattern
        for name in ("PathwayRecord", "NamedNode", "Reference")
    }
    assert len(patterns) == 1
    allowed = re.fullmatch(r"\^\((.*)\):", patterns.pop()).group(1).split("|")
    assert set(allowed) == ALLOWED_CURIE_PREFIXES


def test_the_schema_directory_does_not_shadow_the_schema_module() -> None:
    """src/pathwaymech/schema/ holds YAML beside the module schema.py. Adding an
    __init__.py there would make the directory win the import and silently
    hide the Python validator."""
    assert not (SCHEMA_PATH.parent / "__init__.py").exists()
    spec = importlib.util.find_spec("pathwaymech.schema")
    assert spec is not None and spec.origin and spec.origin.endswith("schema.py")


def test_the_quality_gate_runs_strict_validation(monkeypatch) -> None:
    """`just validate` and CI run the gate; a strict failure must fail it."""
    monkeypatch.setattr(cli, "_validate_strict_gate", lambda: 1)
    assert cli.run_qc_main() == 1


def test_the_command_names_the_failing_record(tmp_path, capsys, record) -> None:
    (tmp_path / "data" / "pathways").mkdir(parents=True)
    broken = copy.deepcopy(record)
    broken["notes"] = "x"
    path = tmp_path / "data" / "pathways" / "broken.yaml"
    path.write_text(yaml.safe_dump(broken), encoding="utf-8")
    assert cli.validate_strict_main([], root=tmp_path) == 1
    assert "data/pathways/broken.yaml: Additional properties" in capsys.readouterr().err
