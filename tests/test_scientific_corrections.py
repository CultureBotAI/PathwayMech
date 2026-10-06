"""Corpus regressions for primary-source conflicts found in adversarial review."""

import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parents[1]


def record(slug):
    return yaml.safe_load((ROOT / f"data/pathways/{slug}.yaml").read_text())


@pytest.mark.parametrize(
    ("slug", "chemical"),
    [
        ("phospholipids-degradation", "CHEBI:15354"),
        ("triglyceride-biosynthesis", "CHEBI:57597"),
    ],
)
def test_lipid_pathway_membership_does_not_make_free_precursors_lipids(slug, chemical):
    participant = next(n for n in record(slug)["participants"] if n["id"] == chemical)
    assert participant["category"] == "small_molecule"


def test_arg82_crystal_contact_exclusion_preserves_plc1_calcium():
    rec = record("inositol-phosphate-biosynthesis")
    calcium = [
        e for e in rec["mechanistic_edges"]
        if e["predicate"] == "has_cofactor" and e["object"] == "CHEBI:29108"
    ]
    assert not any(e["subject"] == "SGD:S000002580" for e in calcium)
    assert any(e["id"] == "cofactor-8c1e5281d7cf" for e in calcium)
    assert any(n["id"] == "CHEBI:29108" for n in rec["participants"])


def test_thi13_retains_only_inferred_core_with_original_endpoints_auditable():
    rec = record("thiamine-biosynthesis")
    edges = [e for e in rec["mechanistic_edges"] if e["subject"] == "gomodel:RXN3O-9804"]
    assert {e["object"] for e in edges if e["predicate"] == "has_input"} == {
        "CHEBI:143915", "CHEBI:29979",
    }
    assert {e["object"] for e in edges if e["predicate"] == "has_output"} == {
        "CHEBI:58354",
    }
    assert len([e for e in edges if e["predicate"] == "provides_input_for"]) == 2
    for edge in edges:
        if edge["predicate"] in {"has_input", "has_output", "provides_input_for"}:
            assert "inferred by similarity" in edge["description"]
            assert "not direct evidence for S. cerevisiae THI13" in edge["description"]
            assert "remain unresolved" in edge["description"]
    ledger = json.loads(
        (ROOT / "reports/causal_graph_review/adversarial-scientific-corrections.json").read_text()
    )
    correction = next(r for r in ledger["records"] if r["record"] == rec["id"])
    quarantined = [
        item["original"] for item in correction["superseded_mechanistic_edges"]
        if item["replacement"] is None
    ]
    assert {e["object"] for e in quarantined} == {
        "CHEBI:29034", "CHEBI:29033", "CHEBI:33190", "CHEBI:15377",
        "CHEBI:15378", "CHEBI:157692", "CHEBI:29969",
    }
    assert all(e["evidence"] for e in quarantined)
    assert correction["inherited_thi13_reaction"]["name"]
