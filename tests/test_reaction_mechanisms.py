"""A detail graph must retain chemistry, scope and evidence without minted IDs."""

from __future__ import annotations

import copy
import json
from dataclasses import asdict
from pathlib import Path

import pytest

from pathwaymech.kgx import kgx_edges, kgx_nodes
from pathwaymech.reaction_mechanisms import mechanism_equation
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.strict import TARGET_CLASS, validator


def _evidence(reference="DOI:fixture"):
    return [{"reference_id": reference, "quote": "Synthetic test evidence."}]


def _edge(key, subject, predicate, obj, **extra):
    return {
        "key": key,
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "assertion_status": "supported",
        "evidence": _evidence(),
        **extra,
    }


def _record():
    """Synthetic authority-looking IDs test contracts, not scientific identity."""
    path = Path(__file__).parent / "fixtures" / "reaction_mechanism.json"
    return json.loads(path.read_text())


def _mechanism(record):
    return record["reaction_mechanisms"][0]


def _alternative():
    record = _record()
    m = _mechanism(record)
    m["relation_to_source"] = "alternative_interpretation"
    m["edges"][0]["subject"] = {"node_id": "CHEBI:4"}
    m["source_conflicts"] = [
        {
            "source_participant_id": "CHEBI:1",
            "interpreted_participant_id": "CHEBI:4",
            "side": "inputs",
            "coefficient": 1,
            "kind": "stereo",
            "status": "unresolved",
            "rationale": "These synthetic isomers are distinct, not exact aliases.",
            "evidence": _evidence(),
        }
    ]
    return record


@pytest.fixture(scope="module")
def closed_checker():
    return validator()


def test_two_step_sum_and_lossless_validation(closed_checker):
    raw = _record()
    parsed = validate_record(raw)
    assert asdict(parsed)["reaction_mechanisms"] == raw["reaction_mechanisms"]
    assert parsed.detail_only_participant_ids == ["CHEBI:3"]
    assert mechanism_equation(_mechanism(raw)) == {
        "inputs": [{"participant_id": "CHEBI:1", "coefficient": 1}],
        "outputs": [{"participant_id": "CHEBI:2", "coefficient": 1}],
    }
    assert not closed_checker.validate(raw, TARGET_CLASS).results


def test_source_orientation_is_selected_without_rewriting_native_reaction():
    raw = _record()
    equation = _mechanism(raw)["source_equation"]
    equation["inputs"], equation["outputs"] = equation["outputs"], equation["inputs"]
    equation["orientation"] = "reversed"
    assert validate_record(raw).reactions == raw["reactions"]
    equation["orientation"] = "as_reported"
    with pytest.raises(ValidationError, match="exact source equation"):
        validate_record(raw)


@pytest.mark.parametrize(
    "locations,allowed",
    [
        ([], True),
        (["GO:1", "GO:1"], True),
        (["GO:1"], False),
        (["GO:1", "GO:2"], False),
        (["GO:1", "GO:1", "GO:1"], False),
    ],
)
def test_no_implicit_transport_or_ambiguous_locations(locations, allowed):
    raw = _record()
    for i, location in enumerate(locations):
        _mechanism(raw)["edges"].append(
            _edge(
                f"location_{i}",
                {"step_key": "first" if i % 2 == 0 else "second"},
                "occurs_in",
                {"node_id": location},
            )
        )
    if allowed:
        validate_record(raw)
    else:
        with pytest.raises(ValidationError, match="identical explicit location"):
            validate_record(raw)


def test_alternative_retains_exact_disagreement(closed_checker):
    raw = _alternative()
    assert validate_record(raw).reaction_mechanisms == raw["reaction_mechanisms"]
    assert not closed_checker.validate(raw, TARGET_CLASS).results
    # Quantities larger than one are supported when both complete terms agree.
    m = _mechanism(raw)
    m["source_equation"]["inputs"][0]["coefficient"] = 2
    m["edges"][0]["coefficient"] = 2
    m["source_conflicts"][0]["coefficient"] = 2
    validate_record(raw)


@pytest.mark.parametrize(
    "mutation",
    [
        lambda m: m.pop("source_conflicts"),
        lambda m: m["source_conflicts"][0].update(side="outputs"),
        lambda m: m["source_conflicts"][0].update(coefficient=2),
        lambda m: m["source_conflicts"].append(copy.deepcopy(m["source_conflicts"][0])),
        lambda m: m["source_conflicts"][0].update(source_participant_id="CHEBI:2"),
        lambda m: m["source_equation"]["inputs"].append(
            {"participant_id": "CHEBI:2", "coefficient": 1}
        ),
        lambda m: m["edges"].append(
            _edge("extra", {"node_id": "CHEBI:2"}, "consumes", {"step_key": "first"}, coefficient=1)
        ),
    ],
)
def test_incomplete_or_wrong_side_conflicts_are_rejected(mutation):
    raw = _alternative()
    mutation(_mechanism(raw))
    with pytest.raises(ValidationError):
        validate_record(raw)


def test_shared_id_quantity_change_cannot_be_hidden_as_substitution():
    raw = _alternative()
    m = _mechanism(raw)
    m["source_equation"]["inputs"][0]["coefficient"] = 2
    m["edges"].append(
        _edge(
            "remaining_a", {"node_id": "CHEBI:1"}, "consumes", {"step_key": "first"}, coefficient=1
        )
    )
    with pytest.raises(ValidationError, match="shared term's coefficient"):
        validate_record(raw)


@pytest.mark.parametrize(
    "mutation",
    [
        lambda r: _mechanism(r)["edges"][0].update(coefficient=True),
        lambda r: _mechanism(r)["edges"][0].update(coefficient=0),
        lambda r: _mechanism(r)["edges"][0].update(coefficient=0.5),
        lambda r: _mechanism(r)["edges"][4].update(coefficient=1),
        lambda r: _mechanism(r)["edges"][0].update(subject={"step_key": "other_mechanism"}),
        lambda r: _mechanism(r)["edges"][0].update(
            subject={"node_id": "CHEBI:1", "step_key": "first"}
        ),
        lambda r: _mechanism(r)["edges"][0].update(predicate={}),
        lambda r: _mechanism(r)["edges"][0].update(evidence=[]),
        lambda r: _mechanism(r)["edges"][0]["evidence"][0].update(reference_id="DOI:missing"),
        lambda r: _mechanism(r)["edges"][0]["evidence"][0].update(unrecognized="x"),
        lambda r: _mechanism(r)["steps"][0].update(key="RHEA:invented"),
        lambda r: _mechanism(r)["steps"].append(copy.deepcopy(_mechanism(r)["steps"][0])),
        lambda r: _mechanism(r)["edges"].append(copy.deepcopy(_mechanism(r)["edges"][0])),
        lambda r: _mechanism(r).update(source_reaction_id=r["id"]),
        lambda r: r["participants"].append(copy.deepcopy(r["participants"][0])),
        lambda r: r["participants"][0].update(category="protein"),
        lambda r: _mechanism(r)["edges"][4].update(subject={"node_id": "CHEBI:1"}),
        lambda r: _mechanism(r)["edges"][0].update(object={"node_id": "CHEBI:2"}),
        lambda r: _mechanism(r)["edges"][0].update(coefficient=2),
        lambda r: r.update(detail_only_participant_ids=["CHEBI:1"]),
        lambda r: r.update(detail_only_participant_ids=["CHEBI:4"]),
        lambda r: r.update(detail_only_participant_ids=["CHEBI:3", "CHEBI:3"]),
    ],
)
def test_bad_identity_scope_evidence_or_equations_fail(mutation):
    raw = _record()
    mutation(raw)
    with pytest.raises(ValidationError):
        validate_record(raw)


@pytest.mark.parametrize(
    "mutation",
    [
        lambda m: m.update(unknown=True),
        lambda m: m["steps"][0].update(unknown=True),
        lambda m: m["edges"][0].update(unknown=True),
        lambda m: m["source_equation"]["inputs"][0].update(unknown=True),
        lambda m: m["edges"][0]["subject"].update(unknown=True),
        lambda m: m["edges"][0]["evidence"][0].update(unknown=True),
        lambda m: m["steps"][0].update(
            hypotheses=[{"description": "Proposed", "status": "supported", "evidence": _evidence()}]
        ),
        lambda m: m["source_equation"].update(orientation=None),
        lambda m: m.update(version=2),
    ],
)
def test_closed_schema_rejects_unknown_null_and_proposal_misrepresentation(
    closed_checker, mutation
):
    raw = _record()
    mutation(_mechanism(raw))
    assert closed_checker.validate(raw, TARGET_CLASS).results
    with pytest.raises(ValidationError):
        validate_record(raw)


def test_construct_role_and_qualifier_evidence_cannot_drift():
    raw = _record()
    qualifier = {
        "endpoint": "subject",
        "kind": "experimental_construct",
        "description": "Tagged test construct",
        "evidence": _evidence(),
    }
    _mechanism(raw)["edges"][4]["endpoint_qualifiers"] = [qualifier]
    validate_record(raw)
    qualifier["endpoint"] = "object"
    with pytest.raises(ValidationError, match="protein or complex"):
        validate_record(raw)


def test_local_keys_cannot_escape_to_public_top_level_edges():
    raw = _record()
    raw["mechanistic_edges"] = [
        {
            "id": "escape",
            "subject": "first",
            "predicate": "produces",
            "object": "CHEBI:2",
            "evidence": _evidence(),
        }
    ]
    with pytest.raises(ValidationError, match="does not resolve locally"):
        validate_record(raw)


def test_kgx_keeps_all_nested_evidence_and_two_record_contexts_without_fake_nodes():
    raw = _alternative()
    m = _mechanism(raw)
    for tag in ("hypothesis", "qualifier", "conflict"):
        raw["references"].append(
            {"id": f"DOI:{tag}", "title": tag, "url": f"https://example.org/{tag}"}
        )
    m["steps"][0]["hypotheses"] = [
        {
            "description": "Unobserved state",
            "status": "proposed",
            "evidence": _evidence("DOI:hypothesis"),
        }
    ]
    m["edges"][4]["endpoint_qualifiers"] = [
        {
            "endpoint": "subject",
            "kind": "experimental_construct",
            "description": "Tagged",
            "evidence": _evidence("DOI:qualifier"),
        }
    ]
    m["source_conflicts"][0]["evidence"] = _evidence("DOI:conflict")
    first = validate_record(raw)
    second_raw = copy.deepcopy(raw)
    second_raw["id"] = "MetaCyc:SECOND"
    _mechanism(second_raw)["description"] = "Separately scoped claim"
    second = validate_record(second_raw)
    nodes = kgx_nodes([first, second])
    assert not kgx_edges([first, second])
    assert {n.id for n in nodes} == {
        first.id,
        second.id,
        "RHEA:1",
        *(n["id"] for n in raw["participants"]),
    }
    parent = next(n for n in nodes if n.id == "RHEA:1")
    contexts = json.loads(parent.source_contexts)
    assert len(contexts) == 2
    for context in contexts:
        expected = m if context["record_id"] == first.id else _mechanism(second_raw)
        detail = context["reaction_mechanisms"][0]
        assert detail["mechanism"] == expected
        assert {r["id"] for r in detail["references"]} == {r["id"] for r in raw["references"]}
    detail_node = next(n for n in nodes if n.id == "CHEBI:3")
    assert all(
        c["graph_scope"] == "mechanism_detail_only" for c in json.loads(detail_node.source_contexts)
    )


def test_empty_extension_preserves_existing_kgx_rows():
    raw = _record()
    raw.pop("reaction_mechanisms")
    raw.pop("detail_only_participant_ids")
    old = validate_record(raw)
    raw.update(reaction_mechanisms=[], detail_only_participant_ids=[])
    new = validate_record(raw)
    assert kgx_nodes([old]) == kgx_nodes([new])
    assert kgx_edges([old]) == kgx_edges([new])
