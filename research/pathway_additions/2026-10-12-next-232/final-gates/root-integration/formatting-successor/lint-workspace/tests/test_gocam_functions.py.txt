"""Regressions for independently established catalytic counterexamples."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

SPEC = spec_from_file_location(
    "review_gocam_functions", Path(__file__).parents[1] / "scripts/review_gocam_functions.py"
)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_idempotent_replay_preserves_original_applied_ledger(tmp_path):
    path = tmp_path / "review.json"
    original = '{"applied":true,"records":[{"superseded_edges":["native-fact"]}]}'
    path.write_text(original)
    assert not MODULE.may_publish_report(path, 0)
    assert path.read_text() == original
    with pytest.raises(ValueError, match="choose a new report path"):
        MODULE.may_publish_report(path, 1)
    assert path.read_text() == original


def source(acc):
    return {
        acc: {
            "provenance": {
                "url": f"https://rest.uniprot.org/uniprotkb/{acc}.json",
                "sha256": "a" * 64,
                "release": "test",
            },
            "entry": {
                "comments": [
                    {"commentType": "FUNCTION", "texts": [{"value": "Reviewed function."}]},
                    {"commentType": "CATALYTIC ACTIVITY", "reaction": {"name": "A + B = C"}},
                ]
            },
        }
    }


def record(rid, activities, chemicals):
    return {
        "id": rid,
        "label": "Test pathway",
        "description": "Test catalytic correction.",
        "pathway_type": "test",
        "taxa": [{"id": "NCBITaxon:559292", "label": "Saccharomyces cerevisiae S288C"}],
        "participants": [{"id": c, "label": c} for c in chemicals],
        "reactions": [{"id": a, "label": "Source activity"} for a in activities],
        "mechanistic_edges": [],
        "references": [{"id": rid, "title": "Source model"}],
    }


def edge(rec, subject, predicate, obj):
    rec["mechanistic_edges"].append(
        {
            "id": f"native-{len(rec['mechanistic_edges'])}",
            "subject": subject,
            "predicate": predicate,
            "object": obj,
            "evidence": [{"reference_id": rec["id"], "quote": "Inspected native assertion."}],
        }
    )


def endpoints(rec, activity, predicate):
    return {
        e["object"]
        for e in rec["mechanistic_edges"]
        if e["subject"] == activity and e["predicate"] == predicate
    }


def test_adk2_corrects_donor_without_modifying_adk1_and_is_idempotent():
    activity = "gomodel:YeastPathways_PWY-7219/6a4c244800000590"
    rec = record(
        "gomodel:YeastPathways_PWY-7219",
        [activity, "gomodel:ADENYL-KIN-RXN"],
        ["CHEBI:30616", "CHEBI:456215", "CHEBI:456216"],
    )
    edge(rec, activity, "has_input", "CHEBI:30616")
    edge(rec, "gomodel:ADENYL-KIN-RXN", "has_input", "CHEBI:30616")
    labels = {x: x for x in ("CHEBI:37565", "CHEBI:58189")}
    original = deepcopy(rec)
    result, ledger = MODULE.curate(rec, source("P26364"), labels)
    assert rec == original
    assert endpoints(result, activity, "has_input") == {"CHEBI:37565", "CHEBI:456215"}
    assert endpoints(result, activity, "has_output") == {"CHEBI:58189", "CHEBI:456216"}
    assert endpoints(result, "gomodel:ADENYL-KIN-RXN", "has_input") == {"CHEBI:30616"}
    assert len(ledger["superseded_edges"]) == 1
    assert MODULE.curate(result, source("P26364"), labels)[0] == result


def test_crd1_uses_cdp_dag_and_cmp_not_glycerol():
    activity = "gomodel:CARDIOLIPSYN-RXN"
    rec = record("gomodel:YeastPathways_PHOSLIPSYN2-PWY-1", [activity], ["CHEBI:17754"])
    edge(rec, activity, "has_output", "CHEBI:17754")
    labels = {
        x: x for x in ("CHEBI:58332", "CHEBI:64716", "CHEBI:62237", "CHEBI:60377", "CHEBI:15378")
    }
    result, ledger = MODULE.curate(rec, source("Q07560"), labels)
    assert endpoints(result, activity, "has_input") == {"CHEBI:58332", "CHEBI:64716"}
    assert endpoints(result, activity, "has_output") == {
        "CHEBI:62237",
        "CHEBI:60377",
        "CHEBI:15378",
    }
    assert ledger["superseded_edges"][0]["edge"]["object"] == "CHEBI:17754"


def test_thiamine_preserves_protein_bound_suicide_substrates_and_phosphate_routing():
    thi13 = "gomodel:RXN3O-9804"
    thi4 = "gomodel:RXN3O-401"
    kinase = "gomodel:PYRIMSYN3-RXN"
    kinase2 = "gomodel:YeastPathways_PWY3O-17/6a4c244800007677"
    rec = record(
        "gomodel:YeastPathways_PWY3O-17",
        [thi13, thi4, kinase, kinase2, "gomodel:RXNQT-4301"],
        ["CHEBI:58354", "SGD:S000003376"],
    )
    edge(rec, kinase, "has_input", "CHEBI:58354")
    edge(rec, kinase2, "has_input", "CHEBI:58354")
    edge(rec, "SGD:S000003376", "enables", "gomodel:RXNQT-4301")
    for predicate, chemical in (
        ("has_input", "CHEBI:29034"),
        ("has_output", "CHEBI:29033"),
        ("has_output", "CHEBI:33190"),
        ("has_input", "CHEBI:15377"),
        ("has_output", "CHEBI:15378"),
        ("has_output", "CHEBI:157692"),
        ("has_output", "CHEBI:29969"),
    ):
        rec["participants"].append({"id": chemical, "label": chemical})
        edge(rec, thi13, predicate, chemical)
    labels = {
        f"CHEBI:{x}": f"chemical {x}"
        for x in [
            143915,
            29979,
            29034,
            15377,
            29969,
            157692,
            58354,
            33190,
            29033,
            15378,
            29950,
            57305,
            57540,
            90873,
            139151,
            17154,
        ]
    }
    sources = {**source("Q07748"), **source("P32318")}
    result, ledger = MODULE.curate(rec, sources, labels)
    assert endpoints(result, thi13, "has_input") == {"CHEBI:143915", "CHEBI:29979"}
    assert endpoints(result, thi13, "has_output") == {"CHEBI:58354"}
    assert endpoints(result, thi13, "provides_input_for") == {kinase, kinase2}
    assert "CHEBI:29950" in endpoints(result, thi4, "has_input")
    assert "CHEBI:90873" in endpoints(result, thi4, "has_output")
    assert any(x["edge"]["predicate"] == "enables" for x in ledger["superseded_edges"])
    assert not endpoints(result, "SGD:S000003376", "enables")
    assert not (
        {"CHEBI:29034", "CHEBI:29033", "CHEBI:33190", "CHEBI:15379"}
        & (endpoints(result, thi13, "has_input") | endpoints(result, thi13, "has_output"))
    )
    quarantined = {
        item["edge"]["object"]
        for item in ledger["superseded_edges"]
        if item["edge"]["subject"] == thi13
    }
    assert {
        "CHEBI:29034", "CHEBI:29033", "CHEBI:33190", "CHEBI:15377",
        "CHEBI:15378", "CHEBI:157692", "CHEBI:29969",
    } <= quarantined
    chemistry = [
        e
        for e in result["mechanistic_edges"]
        if e["subject"] == thi13 and e["predicate"] in {"has_input", "has_output"}
    ]
    assert all("Candida albicans" in e["description"] for e in chemistry)
    assert all("not direct evidence" in e["description"] for e in chemistry)
    assert all("remain unresolved" in e["description"] for e in chemistry)
    assert any(ref["id"] == "PMID:35675507" for ref in result["references"])
    assert not any("Equation coefficients" in e["description"] for e in chemistry)
    assert MODULE.curate(result, sources, labels)[0] == result


def test_removing_unsupported_ethanol_isozymes_preserves_other_activity():
    rec = record(
        "gomodel:YeastPathways_PWY3O-4300",
        ["gomodel:YeastPathways_PWY3O-4300/6a4c244800003351", "gomodel:ADH2-RXN"],
        ["SGD:S000003225", "CHEBI:16236"],
    )
    edge(rec, "SGD:S000003225", "enables", "gomodel:YeastPathways_PWY3O-4300/6a4c244800003351")
    edge(rec, "gomodel:ADH2-RXN", "has_input", "CHEBI:16236")
    result, ledger = MODULE.curate(rec, {**source("P10127"), **source("P38113")}, {})
    assert [n["id"] for n in result["reactions"]] == ["gomodel:ADH2-RXN"]
    assert not any(n["id"] == "SGD:S000003225" for n in result["participants"])
    assert len(ledger["superseded_edges"]) == 1
