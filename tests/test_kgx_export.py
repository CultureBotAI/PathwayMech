from __future__ import annotations

import csv
from dataclasses import replace
from pathlib import Path

from pathwaymech.kgx import (
    EDGE_COLUMNS,
    LOCAL_PREDICATE_CURIES,
    NODE_COLUMNS,
    kgx_edges,
    kgx_nodes,
    write_kgx,
)
from pathwaymech.schema import ALLOWED_EDGE_PREDICATES, PathwayRecord
from pathwaymech.yaml_io import load_pathway_records


def record() -> PathwayRecord:
    return PathwayRecord(
        id="WikiPathways:WP9999",
        label="test pathway",
        description="A compact test pathway.",
        pathway_type="test",
        taxa=[{"id": "NCBITaxon:562", "label": "Escherichia coli"}],
        participants=[
            {"id": "CHEBI:17234", "label": "D-glucose"},
            {"id": "UniProtKB:P0A6F5", "label": "dummy enzyme"},
        ],
        reactions=[{"id": "WikiPathways:WP9999/r1", "label": "dummy reaction"}],
        gene_clusters=[{"id": "MIBiG:BGC0000001", "label": "dummy cluster"}],
        mechanistic_edges=[
            {
                "id": "edge-001",
                "subject": "CHEBI:17234",
                "predicate": "consumes",
                "object": "WikiPathways:WP9999/r1",
                "evidence": [
                    {
                        "reference_id": "PMID:1",
                        "quote": "D-glucose is consumed by the dummy reaction.",
                    }
                ],
            },
            {
                "id": "edge-002",
                "subject": "WikiPathways:WP9999/r1",
                "predicate": "produces",
                "object": "UniProtKB:P0A6F5",
                "evidence": [
                    {
                        "reference_id": "PMID:1",
                        "quote": "The dummy reaction produces the dummy enzyme.",
                    }
                ],
            },
        ],
        references=[{"id": "PMID:1", "title": "test reference"}],
    )


def test_every_local_predicate_has_a_kgx_curie() -> None:
    assert set(LOCAL_PREDICATE_CURIES) == ALLOWED_EDGE_PREDICATES


def test_kgx_nodes_cover_every_pathway_local_node_type() -> None:
    rows = {node.id: node for node in kgx_nodes([record()])}

    assert rows["WikiPathways:WP9999"].category == "biolink:Pathway"
    assert rows["NCBITaxon:562"].category == "biolink:OrganismTaxon"
    assert rows["CHEBI:17234"].category == "biolink:SmallMolecule"
    assert rows["UniProtKB:P0A6F5"].category == "biolink:GeneOrGeneProduct"
    assert rows["WikiPathways:WP9999/r1"].category == "biolink:BiochemicalReaction"
    assert rows["MIBiG:BGC0000001"].category == "biolink:GenomicEntity"


def test_kgx_nodes_category_panther_reactions() -> None:
    rows = {
        node.id: node
        for node in kgx_nodes(
            [
                replace(
                    record(),
                    id="PANTHER:P00001",
                    reactions=[
                        {
                            "id": "PANTHER:R-TEST-67890",
                            "label": "test PANTHER reaction",
                        }
                    ],
                )
            ]
        )
    }

    assert rows["PANTHER:R-TEST-67890"].category == "biolink:BiochemicalReaction"


def test_kgx_edges_are_curied_and_unique_outside_record_scope() -> None:
    rows = kgx_edges([record()])

    assert rows[0].id == "pathwaymech:WikiPathways_WP9999_edge-001_a5cf9bf257e6"
    assert rows[0].predicate == "pathwaymech:consumes"
    assert rows[0].subject == "CHEBI:17234"
    assert rows[0].object == "WikiPathways:WP9999/r1"
    assert rows[0].source_records == "PMID:1"


def test_kgx_edge_ids_do_not_collide_after_punctuation_sanitizing() -> None:
    edge_ids = {
        kgx_edges([replace(record(), id=record_id)])[0].id
        for record_id in ("WikiPathways:WP/1", "WikiPathways:WP_1")
    }

    assert len(edge_ids) == 2


def test_write_kgx_uses_lf_tsv_with_stable_headers(tmp_path: Path) -> None:
    nodes_path, edges_path = write_kgx([record()], tmp_path)

    assert nodes_path.read_bytes().count(b"\r") == 0
    assert edges_path.read_bytes().count(b"\r") == 0
    assert nodes_path.read_text(encoding="utf-8").splitlines()[0] == "\t".join(
        NODE_COLUMNS
    )
    assert edges_path.read_text(encoding="utf-8").splitlines()[0] == "\t".join(
        EDGE_COLUMNS
    )


def test_corpus_export_has_no_duplicate_or_dangling_nodes(tmp_path: Path) -> None:
    records = load_pathway_records(Path("data/pathways"))
    nodes_path, edges_path = write_kgx(records, tmp_path)

    with nodes_path.open(encoding="utf-8", newline="") as stream:
        nodes = list(csv.DictReader(stream, delimiter="\t"))
    with edges_path.open(encoding="utf-8", newline="") as stream:
        edges = list(csv.DictReader(stream, delimiter="\t"))

    node_ids = {node["id"] for node in nodes}
    endpoints = {edge["subject"] for edge in edges} | {edge["object"] for edge in edges}

    assert len(node_ids) == len(nodes)
    assert endpoints <= node_ids
    assert {edge["predicate"] for edge in edges} <= set(LOCAL_PREDICATE_CURIES.values())
    assert all(node["category"].startswith("biolink:") for node in nodes)
