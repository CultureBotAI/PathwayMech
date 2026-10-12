from __future__ import annotations

import csv
import io
import json
from dataclasses import replace
from pathlib import Path

import pytest
import yaml

from pathwaymech.kgx import (
    EDGE_COLUMNS,
    LOCAL_PREDICATE_CURIES,
    NODE_COLUMNS,
    _tsv,
    kgx_edges,
    kgx_nodes,
    write_kgx,
)
from pathwaymech.schema import ALLOWED_EDGE_PREDICATES, PathwayRecord, validate_record
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


def test_kegg_reaction_class_and_explicit_generic_carriers_survive_export(tmp_path):
    checked = replace(
        record(), id="KEGG:M00374", label="Dicarboxylate-hydroxybutyrate cycle",
        participants=[
            {"id": "KEGG:C00138", "label": "Reduced ferredoxin", "category": "chemical_entity"},
            {"id": "KEGG:C00139", "label": "Oxidized ferredoxin", "category": "chemical_entity"},
            {"id": "KEGG:C00022", "label": "Pyruvate"},
        ],
        reactions=[{"id": "KEGG:R01196", "label": "Native reaction", "direction": "left_to_right"}],
        gene_clusters=[], mechanistic_edges=[{
            "id": "carrier", "subject": "KEGG:C00138", "predicate": "consumes",
            "object": "KEGG:R01196", "description": "The native coefficient is 2.",
            "evidence": [{"reference_id": "PMID:1", "quote": "Synthetic export test evidence."}],
        }],
    )
    node_path, edge_path = write_kgx([checked], tmp_path)
    with node_path.open() as stream:
        nodes = {row["id"]: row for row in csv.DictReader(stream, delimiter="\t")}
    assert nodes["KEGG:M00374"]["category"] == "biolink:Pathway"
    assert nodes["KEGG:R01196"]["category"] == "biolink:BiochemicalReaction"
    assert nodes["KEGG:R01196"]["direction"] == "left_to_right"
    assert nodes["KEGG:C00022"]["category"] == "biolink:SmallMolecule"
    for identifier in ("KEGG:C00138", "KEGG:C00139"):
        assert nodes[identifier]["category"] == "biolink:ChemicalEntity"
        assert nodes[identifier]["source_category"] == "chemical_entity"
    with edge_path.open() as stream:
        edge = next(csv.DictReader(stream, delimiter="\t"))
    assert edge["description"] == checked.mechanistic_edges[0]["description"]
    assert json.loads(edge["evidence"]) == checked.mechanistic_edges[0]["evidence"]
    explicit = replace(checked, reactions=[{
        **checked.reactions[0], "category": "molecular_activity",
    }])
    assert next(n for n in kgx_nodes([explicit]) if n.id == "KEGG:R01196").category == (
        "biolink:MolecularActivity"
    )


@pytest.mark.parametrize("path, identifier", [
    ("epoxysqualene-biosynthesis", "gomodel:YeastPathways_PWY-5670-1/654d809000002591"),
    ("epoxysqualene-biosynthesis", "gomodel:YeastPathways_PWY-5670-1/654d809000002611"),
    ("formaldehyde-oxidation-ii-glutathione-dependent",
     "gomodel:YeastPathways_PWY-1801-1/65692e7e00001183"),
    ("s-adenosyl-l-methionine-cycle-ii",
     "gomodel:ba4cc2f6-35b0-45f1-a3b5-7bf7a1e71bf8_RXN-7605"),
    ("very-long-chain-fatty-acid-biosynthesis",
     "gomodel:46fed9f2-cf0b-4568-b40e-557bd0cfffe5_RXN3O-9813"),
])
def test_unresolved_corpus_participants_are_not_exported_as_reactions(path, identifier):
    source = yaml.safe_load(Path(f"data/pathways/{path}.yaml").read_text(encoding="utf-8"))
    checked = validate_record(source)
    node = next(node for node in kgx_nodes([checked]) if node.id == identifier)

    assert node.category == "biolink:NamedThing"
    assert any(n["id"] == identifier for n in checked.participants)


@pytest.mark.parametrize("prefix", ["gomodel", "WikiPathways", "Reactome"])
def test_native_participant_fallback_retains_reaction_defaults(prefix):
    participant = f"{prefix}:test/entity"
    reaction = f"{prefix}:test/reaction"
    checked = replace(
        record(),
        participants=[{"id": participant, "label": "Unresolved physical entity"}],
        reactions=[{"id": reaction, "label": "Conversion"}],
    )
    rows = {node.id: node for node in kgx_nodes([checked])}

    assert rows[participant].category == "biolink:NamedThing"
    assert rows[reaction].category == "biolink:BiochemicalReaction"


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
    for path in (nodes_path, edges_path):
        assert all(not line.endswith(("\t", " ")) for line in path.read_text().splitlines())
    assert all(line.endswith('\t""') for line in edges_path.read_text().splitlines()[1:])
    with edges_path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    assert len(rows) == 2
    assert all(tuple(row) == EDGE_COLUMNS and row["endpoint_qualifiers"] == "" for row in rows)


def test_tsv_empty_terminal_fields_round_trip_without_changing_populated_cells() -> None:
    values = ["", None, '""', '"', 'a "quoted" value', "β-D-glucose",
              json.dumps({"label": 'a "quote"', "control": "\t\n"}), " \t\n "]
    rendered = _tsv(("first", "middle", "last"), [
        {"first": str(index), "middle": "", "last": value}
        for index, value in enumerate(values)
    ])
    rows = list(csv.DictReader(io.StringIO(rendered), delimiter="\t"))
    expected = ["", "", *values[2:-1], ""]
    assert rows == [{"first": str(index), "middle": "", "last": value}
                    for index, value in enumerate(expected)]
    assert all(not line.endswith(("\t", " ")) for line in rendered.splitlines())


def test_phb_polymer_is_exported_as_a_chemical_entity(tmp_path: Path) -> None:
    source = yaml.safe_load(
        Path("data/pathways/polyhydroxybutanoate-biosynthesis.yaml").read_text(encoding="utf-8")
    )
    checked = validate_record(source)
    nodes_path, _ = write_kgx([checked], tmp_path)
    with nodes_path.open(encoding="utf-8", newline="") as stream:
        nodes = {row["id"]: row for row in csv.DictReader(stream, delimiter="\t")}

    polymer = nodes["CHEBI:8298"]
    assert polymer["category"] == "biolink:ChemicalEntity"
    assert polymer["source_category"] == "polymer"
    assert json.loads(polymer["source_contexts"])[0]["category"] == "polymer"
    assert nodes["CHEBI:57288"]["category"] == "biolink:SmallMolecule"


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
