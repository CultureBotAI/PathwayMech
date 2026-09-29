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
from pathwaymech.schema import (
    ALLOWED_CURIE_PREFIXES,
    ALLOWED_EDGE_PREDICATES,
    ValidationError,
    validate_record,
)
from pathwaymech.strict import SCHEMA_PATH, TARGET_CLASS, strict_errors, validator

ROOT = Path(__file__).resolve().parents[1]
RECORDS = sorted((ROOT / "data" / "pathways").rglob("*.yaml"))


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
    "an undeclared gene cluster key": lambda r: _gene_cluster(r).__setitem__("role", "x"),
    "an undeclared cluster gene key": lambda r: _cluster_gene(r).__setitem__("role", "x"),
    "an undeclared genomic locus key": lambda r: _genomic_locus(r).__setitem__("role", "x"),
    "an undeclared edge key": lambda r: _edge(r).__setitem__("weight", 1),
    "an undeclared evidence key": lambda r: _evidence(r).__setitem__("page", 3),
    "a predicate outside the enum": lambda r: _edge(r).__setitem__("predicate", "causes"),
    "a node CURIE with an unknown prefix": lambda r: r["participants"][0].__setitem__(
        "id", "FOO:1"
    ),
    "a record id that is not a CURIE": lambda r: r.__setitem__("id", "nocolon"),
    "a gene cluster outside MIBiG": lambda r: _gene_cluster(r).__setitem__("id", "RHEA:1"),
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
    allowed = re.match(r"\^\(([^)]*)\):", patterns.pop()).group(1).split("|")
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


# --------------------------------------------------------------------------
# Every rule the schema declares, driven from the schema itself (#195)
# --------------------------------------------------------------------------

# Where one instance of each class sits in a record, to break it there.
_GENE_CLUSTER = {
    "id": "MIBiG:BGC0000001",
    "label": "mini metabolite biosynthetic gene cluster",
    "products": ["mini metabolite"],
    "biosynthetic_classes": ["RiPP"],
    "genes": [{"id": "gene-a", "label": "gene A"}],
    "loci": [{"accession": "ABCD01000001.1", "start": 10, "end": 80}],
}


def _gene_cluster(r: dict) -> dict:
    r["gene_clusters"] = [copy.deepcopy(_GENE_CLUSTER)]
    return r["gene_clusters"][0]


def _cluster_gene(r: dict) -> dict:
    return _gene_cluster(r)["genes"][0]


def _genomic_locus(r: dict) -> dict:
    return _gene_cluster(r)["loci"][0]


_WHERE = {
    "PathwayRecord": lambda r: r,
    "NamedNode": lambda r: r["participants"][0],
    "GeneCluster": _gene_cluster,
    "ClusterGene": _cluster_gene,
    "GenomicLocus": _genomic_locus,
    "MechanisticEdge": lambda r: r["mechanistic_edges"][0],
    "EvidenceItem": lambda r: r["mechanistic_edges"][0]["evidence"][0],
    "Reference": lambda r: r["references"][0],
}
_VIEW = SchemaView(str(SCHEMA_PATH))
_REQUIRED = [
    (name, slot)
    for name in _WHERE
    for slot in _VIEW.class_slots(name)
    if _VIEW.induced_slot(slot, name).required
]
# Every slot whose pattern refuses a blank string.
_NON_BLANK = [
    (name, slot)
    for name in _WHERE
    for slot in _VIEW.class_slots(name)
    if (pattern := _VIEW.induced_slot(slot, name).pattern) and not re.search(pattern, "  ")
]


def test_the_schema_driven_cases_cover_the_schema() -> None:
    assert set(_WHERE) == set(_VIEW.all_classes())


# The rules pinned here are the Python validator's (src/pathwaymech/schema.py).
# The cases above are generated from the schema, so on their own they would
# follow a schema that lost a rule; these sets are what keep it from losing one.
EXPECTED_REQUIRED = (
    {
        ("PathwayRecord", slot)
        for slot in ("id", "label", "description", "pathway_type", "taxa", "participants",
                     "reactions", "mechanistic_edges", "references")
    }
    | {("GeneCluster", slot) for slot in ("id", "label")}
    | {("ClusterGene", "id"), ("GenomicLocus", "accession")}
    | {("MechanisticEdge", slot) for slot in ("id", "subject", "predicate", "object", "evidence")}
    | {("NamedNode", "id"), ("NamedNode", "label"), ("Reference", "id"),
       ("EvidenceItem", "reference_id"), ("EvidenceItem", "quote")}
)
EXPECTED_NON_BLANK = (
    {("PathwayRecord", slot) for slot in ("id", "label", "description", "pathway_type")}
    | {("NamedNode", "id"), ("NamedNode", "label"), ("MechanisticEdge", "id"),
       ("EvidenceItem", "quote"), ("Reference", "id"), ("Reference", "title"),
       ("Reference", "citation")}
    | {("GeneCluster", slot) for slot in ("id", "label", "products",
                                          "biosynthetic_classes")}
    | {("ClusterGene", "id"), ("ClusterGene", "label"), ("GenomicLocus", "accession")}
)


def test_the_schema_requires_exactly_what_the_python_validator_requires() -> None:
    assert set(_REQUIRED) == EXPECTED_REQUIRED


def test_the_schema_refuses_blanks_exactly_where_the_python_validator_does() -> None:
    assert set(_NON_BLANK) == EXPECTED_NON_BLANK


@pytest.mark.parametrize(("name", "slot"), _REQUIRED, ids=[f"{n}.{s}" for n, s in _REQUIRED])
def test_removing_any_required_slot_is_rejected(checker, record, name, slot) -> None:
    broken = copy.deepcopy(record)
    _WHERE[name](broken).pop(slot)
    assert checker.validate(broken, TARGET_CLASS).results, f"{name}.{slot} is not enforced"


@pytest.mark.parametrize(("name", "slot"), _NON_BLANK, ids=[f"{n}.{s}" for n, s in _NON_BLANK])
def test_blanking_any_non_blank_slot_is_rejected(checker, record, name, slot) -> None:
    broken = copy.deepcopy(record)
    target = _WHERE[name](broken)
    target[slot] = "  "
    assert checker.validate(broken, TARGET_CLASS).results, f"{name}.{slot} accepts blanks"


def test_bgc_shaped_fields_are_validated_by_both_schemas(checker, record) -> None:
    edited = copy.deepcopy(record)
    edited["gene_clusters"] = [copy.deepcopy(_GENE_CLUSTER)]
    assert not checker.validate(edited, TARGET_CLASS).results
    assert validate_record(edited).gene_clusters == [_GENE_CLUSTER]


@pytest.mark.parametrize(("field", "value"), [("start", 0), ("end", -1)])
def test_bgc_locus_coordinates_must_be_positive(checker, record, field, value) -> None:
    broken = copy.deepcopy(record)
    _genomic_locus(broken)[field] = value
    assert checker.validate(broken, TARGET_CLASS).results
    with pytest.raises(ValidationError) as raised:
        validate_record(broken)
    assert raised.value.errors == [f"gene_clusters[0].loci[0].{field} must be a positive integer"]


# --------------------------------------------------------------------------
# Where the schema was looser than the Python validator (#193)
# --------------------------------------------------------------------------


def test_a_401_character_quote_ending_in_a_newline_is_rejected(checker, record) -> None:
    """`$` matches before a final newline in Python's re, so it admitted 401."""
    broken = copy.deepcopy(record)
    _evidence(broken)["quote"] = "x" * 400 + "\n"
    assert checker.validate(broken, TARGET_CLASS).results


@pytest.mark.parametrize("value", [None, "c"], ids=["citation-null", "citation-set"])
def test_an_explicit_null_is_an_error_not_an_omission(checker, record, value) -> None:
    broken = copy.deepcopy(record)
    reference = {"id": broken["references"][0]["id"], "title": None}
    if value is not None:
        reference["citation"] = value
    broken["references"][0] = reference
    assert checker.validate(broken, TARGET_CLASS).results


@pytest.mark.parametrize("curie", ["CHEBI:", "CHEBI: 123", "CHEBI:12 3", "CHEBI:123\n"])
def test_a_curie_needs_a_local_part_without_whitespace(checker, record, curie) -> None:
    """A new, unreferenced node, so no other rule (edge resolution) can be
    what rejects it."""
    broken = copy.deepcopy(record)
    broken["participants"].append({"id": curie, "label": "added"})
    assert checker.validate(broken, TARGET_CLASS).results
    with pytest.raises(ValidationError) as raised:
        validate_record(broken)
    assert raised.value.errors == [
        f"participants[{len(broken['participants']) - 1}].id "
        "must have a local part with no whitespace"
    ]


# --------------------------------------------------------------------------
# What the gate reads (#191, #192, #194)
# --------------------------------------------------------------------------


def _repo_with(tmp_path: Path, files: dict[str, object]) -> Path:
    for name, content in files.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            content if isinstance(content, str) else yaml.safe_dump(content), encoding="utf-8"
        )
    return tmp_path


def test_a_record_in_a_subdirectory_is_validated_too(tmp_path, record, capsys) -> None:
    """Every other gate recurses; the closed one must read the same records."""
    broken = copy.deepcopy(record)
    broken["notes"] = "x"
    root = _repo_with(tmp_path, {"data/pathways/good.yaml": record,
                                 "data/pathways/group/nested.yaml": broken})
    assert cli.validate_strict_main([], root=root) == 1
    assert "data/pathways/group/nested.yaml: Additional properties" in capsys.readouterr().err


def test_a_draft_outside_the_repository_is_checked_not_crashed(tmp_path, record, capsys) -> None:
    root = _repo_with(tmp_path / "repo", {"data/pathways/good.yaml": record})
    draft = tmp_path / "draft.yaml"
    broken = copy.deepcopy(record)
    broken["notes"] = "x"
    draft.write_text(yaml.safe_dump(broken), encoding="utf-8")
    assert cli.validate_strict_main([str(draft)], root=root) == 1
    assert f"{draft.resolve()}: Additional properties" in capsys.readouterr().err


def test_an_unreadable_record_is_named(tmp_path) -> None:
    root = _repo_with(tmp_path, {"data/pathways/broken.yaml": "id: [unclosed\n"})
    errors = strict_errors([root / "data/pathways/broken.yaml"], root)
    assert errors and errors[0].startswith("data/pathways/broken.yaml: unreadable")


def test_the_conventional_script_runs_the_closed_gate() -> None:
    """scripts/validate_strict.py is the closed LinkML gate in every sibling Mech."""
    text = (ROOT / "scripts" / "validate_strict.py").read_text(encoding="utf-8")
    assert "validate_strict_main" in text and "validate_main()" not in text
