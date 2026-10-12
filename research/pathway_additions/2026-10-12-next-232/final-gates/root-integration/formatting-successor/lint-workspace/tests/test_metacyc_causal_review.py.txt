"""Regressions for source-verified chemistry and qualified protein context."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(slug):
    return yaml.safe_load((ROOT / "data/pathways" / f"{slug}.yaml").read_text())


def triples(data):
    return {(e["subject"], e["predicate"], e["object"]) for e in data["mechanistic_edges"]}


def test_glyoxylate_cycle_regenerates_oxaloacetate():
    edges = triples(record("glyoxylate-cycle"))
    assert ("RHEA:21433", "produces", "CHEBI:16452") in edges
    assert ("CHEBI:16452", "consumes", "RHEA:16846") in edges
    assert ("RHEA:21433", "precedes", "RHEA:16846") in edges
    assert ("RHEA:10229", "produces", "CHEBI:16383") in edges
    assert ("CHEBI:16383", "consumes", "RHEA:22145") in edges


def test_tryptophan_synthase_exposes_indole_without_duplicate_net_flux():
    data = record("l-tryptophan-biosynthesis")
    edges = triples(data)
    assert "RHEA:10533" not in {n["id"] for n in data["reactions"]}
    assert ("RHEA:14082", "produces", "CHEBI:16881") in edges
    assert ("CHEBI:16881", "consumes", "RHEA:26435") in edges
    assert ("RHEA:14082", "precedes", "RHEA:26435") in edges


def test_spontaneous_decomposition_is_not_assigned_to_upstream_enzyme():
    edges = triples(record("l-isoleucine-biosynthesis-i-from-threonine"))
    assert ("EC:4.3.1.19", "catalyzes", "RHEA:40676") in edges
    assert ("EC:4.3.1.19", "catalyzes", "RHEA:39968") not in edges
    assert ("EC:4.3.1.19", "catalyzes", "RHEA:39976") not in edges
    assert ("RHEA:40676", "produces", "CHEBI:48306") in edges
    assert ("RHEA:39968", "produces", "CHEBI:76545") in edges


def test_reference_strain_mutant_and_cluster_disagreement_are_not_overstated():
    for slug in ("l-valine-biosynthesis", "l-isoleucine-biosynthesis-i-from-threonine"):
        data = record(slug)
        assert "UniProtKB:P0DP90" not in {n["id"] for n in data["participants"]}
        edges = triples(data)
        assert ("UniProtKB:P05791", "has_cofactor", "CHEBI:30408") in edges
        assert ("UniProtKB:P05791", "has_cofactor", "CHEBI:190135") not in edges


def test_feedback_targets_specific_protein_and_preserves_opposite_valine_effects():
    edges = triples(record("l-isoleucine-biosynthesis-i-from-threonine"))
    assert ("CHEBI:57762", "activates", "UniProtKB:P04968") in edges
    assert ("CHEBI:57762", "inhibits", "UniProtKB:P00893") in edges
    assert ("CHEBI:58045", "inhibits", "UniProtKB:P04968") in edges


def test_air_carboxylation_has_bacterial_primary_evidence():
    data = record("inosine-5-phosphate-biosynthesis-ii")
    assert data["taxa"][0]["id"] == "NCBITaxon:158"
    edge = next(
        e
        for e in data["mechanistic_edges"]
        if e["subject"] == "EC:4.1.1.21" and e["predicate"] == "catalyzes"
    )
    assert edge["object"] == "RHEA:10794"
    assert any(e["reference_id"] == "PMID:21548610" for e in edge["evidence"])
