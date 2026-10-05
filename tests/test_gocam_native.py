from __future__ import annotations

import pytest

from pathwaymech.gocam_native import project_native_model


def individual(identifier, term=None, roots=(), label=None):
    node = {
        "id": identifier,
        "type": [{"id": term, "label": label or term}] if term else [],
        "root-type": [{"id": root} for root in roots],
    }
    if label:
        node["annotations"] = [{"key": "rdfs:label", "value": label}]
    return node


def fact(subject, predicate, obj):
    return {"subject": subject, "property": predicate, "object": obj}


def test_native_context_and_causality_preserve_exact_source_meaning():
    model = {
        "id": "gomodel:test",
        "individuals": [
            individual("gomodel:a", "GO:0000001", ["GO:0003674"], "first activity"),
            individual("gomodel:b", "GO:0000002", ["GO:0003674"], "second activity"),
            individual("gomodel:protein", "SGD:S000000001", ["CHEBI:33695"], "protein"),
            individual("gomodel:chemical", "CHEBI:15377", ["CHEBI:24431"], "water"),
            individual("gomodel:location", "GO:0005829", ["GO:0005575"], "cytosol"),
            individual("gomodel:process", "GO:0008152", ["GO:0008150"], "metabolic process"),
        ],
        "facts": [
            fact("gomodel:a", "RO:0002333", "gomodel:protein"),
            fact("gomodel:a", "RO:0002233", "gomodel:chemical"),
            fact("gomodel:a", "RO:0002234", "gomodel:chemical"),
            fact("gomodel:a", "BFO:0000066", "gomodel:location"),
            fact("gomodel:a", "BFO:0000050", "gomodel:process"),
            fact("gomodel:a", "RO:0002411", "gomodel:b"),
            fact("gomodel:a", "RO:0002413", "gomodel:b"),
        ],
    }
    projected = project_native_model(model, source_member="./test.json")
    edges = {(e["subject"], e["predicate"], e["object"]) for e in projected["mechanistic_edges"]}
    assert edges == {
        ("SGD:S000000001", "enables", "gomodel:a"),
        ("gomodel:a", "has_input", "CHEBI:15377"),
        ("gomodel:a", "has_output", "CHEBI:15377"),
        ("gomodel:a", "occurs_in", "GO:0005829"),
        ("gomodel:a", "part_of", "GO:0008152"),
        ("gomodel:a", "causally_upstream_of", "gomodel:b"),
        ("gomodel:a", "provides_input_for", "gomodel:b"),
    }
    assert len(projected["facts"]) == 7
    evidence = projected["mechanistic_edges"][0]["evidence"][0]
    assert evidence["reference_id"] == "gomodel:test"
    assert "quote" not in evidence
    assert "RO:0002333" in evidence["source_assertion"]
    assert (
        evidence["source_locator"]
        == "./test.json#/facts/0; endpoint types: /individuals/0/type; /individuals/2/type"
    )


def test_generic_redox_states_and_untyped_source_input_remain_distinct():
    model = {
        "id": "gomodel:test",
        "individuals": [
            individual("gomodel:a", "GO:0000001", ["GO:0003674"]),
            individual("gomodel:oxidized", "CHEBI:33695", ["CHEBI:24431"], "ferricytochrome b5"),
            individual("gomodel:reduced", "CHEBI:33695", ["CHEBI:24431"], "ferrocytochrome b5"),
            individual("gomodel:unknown"),
        ],
        "facts": [
            fact("gomodel:a", "RO:0002233", "gomodel:oxidized"),
            fact("gomodel:a", "RO:0002234", "gomodel:reduced"),
            fact("gomodel:a", "RO:0002233", "gomodel:unknown"),
        ],
    }
    projected = project_native_model(model, source_member="test.json")
    assert {n["id"] for n in projected["participants"]} == {
        "gomodel:oxidized",
        "gomodel:reduced",
        "gomodel:unknown",
    }
    assert all(f["status"] == "represented" for f in projected["facts"])
    unknown = next(n for n in projected["participants"] if n["id"] == "gomodel:unknown")
    assert unknown == {"id": "gomodel:unknown", "label": "gomodel:unknown"}


def test_scope_exclusion_is_explicit_and_complete():
    model = {
        "id": "gomodel:test",
        "individuals": [
            individual("gomodel:a", "GO:0000001", ["GO:0003674"]),
            individual("gomodel:b", "GO:0000002", ["GO:0003674"]),
        ],
        "facts": [fact("gomodel:a", "RO:0002413", "gomodel:b")],
    }
    projected = project_native_model(
        model, source_member="test.json", included_activities={"gomodel:a"}
    )
    assert projected["mechanistic_edges"] == []
    assert projected["facts"] == [
        {
            "fact_index": 0,
            "subject": "gomodel:a",
            "predicate": "RO:0002413",
            "object": "gomodel:b",
            "status": "excluded_activity_scope",
            "activities": ["gomodel:b"],
        }
    ]


@pytest.mark.parametrize(
    "relation,endpoint,error",
    [
        ("RO:9999999", "gomodel:b", "unsupported source predicate"),
        ("RO:0002413", "gomodel:missing", "dangling native fact"),
    ],
)
def test_unknown_source_facts_fail_instead_of_silently_disappearing(relation, endpoint, error):
    model = {
        "id": "gomodel:test",
        "individuals": [
            individual("gomodel:a", "GO:0000001", ["GO:0003674"]),
            individual("gomodel:b", "GO:0000002", ["GO:0003674"]),
        ],
        "facts": [fact("gomodel:a", relation, endpoint)],
    }
    with pytest.raises(ValueError, match=error):
        project_native_model(model, source_member="test.json")
