from __future__ import annotations

from pathlib import Path

import pytest

from pathwaymech.pathway_tools import (
    load_pathway_tools_dat,
    metacyc_pathway_records,
    pmn_pathway_records,
)
from pathwaymech.schema import validate_record

METACYC_FIXTURE = Path("tests/fixtures/metacyc/pathways.dat")
PMN_FIXTURE = Path("tests/fixtures/pmn/pathways.dat")


def test_metacyc_flat_file_converts_to_valid_pathway_record() -> None:
    records = metacyc_pathway_records(load_pathway_tools_dat(METACYC_FIXTURE))

    record = validate_record(records[0])

    assert record.id == "MetaCyc:GLYCOLYSIS"
    assert record.reactions == [
        {"id": "MetaCyc:PHOSGLYPHOS-RXN", "label": "PHOSGLYPHOS-RXN"},
        {"id": "MetaCyc:2PGADEHYDRAT-RXN", "label": "2PGADEHYDRAT-RXN"},
    ]
    assert record.mechanistic_edges == [
        {
            "id": "metacyc-edge-1",
            "subject": "MetaCyc:PHOSGLYPHOS-RXN",
            "predicate": "precedes",
            "object": "MetaCyc:2PGADEHYDRAT-RXN",
            "evidence": [
                {
                    "reference_id": "MetaCyc:GLYCOLYSIS",
                    "source_assertion": (
                        "The PREDECESSORS slot lists PHOSGLYPHOS-RXN as a direct "
                        "predecessor of 2PGADEHYDRAT-RXN in this pathway."
                    ),
                    "source_locator": "pathways.dat[UNIQUE-ID=GLYCOLYSIS]/PREDECESSORS[1]",
                }
            ],
        }
    ]


def test_pmn_flat_file_converts_to_valid_pathway_record() -> None:
    records = pmn_pathway_records(
        load_pathway_tools_dat(PMN_FIXTURE), pgdb="chlamy", source_version="fixture-1"
    )

    record = validate_record(records[0])

    assert record.id == "PMN:chlamy:CHLAMY-GLYOX"
    assert record.reactions == [
        {"id": "PMN:chlamy:RXN-GLYOX-1", "label": "RXN-GLYOX-1"},
        {"id": "PMN:chlamy:RXN-GLYOX-2", "label": "RXN-GLYOX-2"},
    ]
    assert record.mechanistic_edges == [
        {
            "id": "pmn-edge-1",
            "subject": "PMN:chlamy:RXN-GLYOX-1",
            "predicate": "precedes",
            "object": "PMN:chlamy:RXN-GLYOX-2",
            "evidence": [
                {
                    "reference_id": "PMN:chlamy:CHLAMY-GLYOX",
                    "source_assertion": (
                        "The PREDECESSORS slot lists RXN-GLYOX-1 as a direct "
                        "predecessor of RXN-GLYOX-2 in this pathway."
                    ),
                    "source_locator": (
                        "pathways.dat[UNIQUE-ID=CHLAMY-GLYOX]/PREDECESSORS[1]"
                    ),
                }
            ],
        }
    ]
    assert record.references[0]["source_version"] == "fixture-1"


def _branched_pathway(*predecessors: str) -> dict[str, list[str]]:
    return {
        "UNIQUE-ID": ["PWY-1"],
        "REACTION-LIST": ["R1", "R2", "R3"],
        "PREDECESSORS": list(predecessors),
    }


def test_pmn_frame_identity_includes_the_pgdb() -> None:
    native = [_branched_pathway("(R3 R1 R2)")]
    chlamy = pmn_pathway_records(native, pgdb="chlamy")[0]
    ara = pmn_pathway_records(native, pgdb="ara")[0]
    assert chlamy["id"] != ara["id"]
    assert {node["id"] for node in chlamy["reactions"]}.isdisjoint(
        {node["id"] for node in ara["reactions"]}
    )


def test_pmn_requires_explicit_pgdb() -> None:
    with pytest.raises(TypeError, match="pgdb"):
        pmn_pathway_records([])  # type: ignore[call-arg]


@pytest.mark.parametrize("pgdb", ["", " ", "chlamy:PWY", "../chlamy", "chlamy cyc"])
def test_pmn_rejects_invalid_pgdb(pgdb: str) -> None:
    with pytest.raises(ValueError, match="PGDB"):
        pmn_pathway_records([], pgdb=pgdb)


def test_predecessors_preserve_every_incoming_branch() -> None:
    record = validate_record(metacyc_pathway_records([
        _branched_pathway("(R1)", "(R2)", "(R3 R1 R2)")
    ])[0])
    assert [(edge["subject"], edge["object"]) for edge in record.mechanistic_edges] == [
        ("MetaCyc:R1", "MetaCyc:R3"), ("MetaCyc:R2", "MetaCyc:R3")
    ]
    assert all(edge["predicate"] == "precedes" for edge in record.mechanistic_edges)
    assert all(
        edge["evidence"][0]["source_locator"].endswith("PREDECESSORS[3]")
        for edge in record.mechanistic_edges
    )


@pytest.mark.parametrize("value", [
    "R3 R1", "(R3 R1", "R3 R1)", "()", "(R3 (R1 R2))", "(R3 R1) extra",
    "INHERITED-PWY", "(MISSING)", "(R3 MISSING)", "(R3 R3)", '(R"3" R1)',
])
def test_predecessors_reject_incomplete_or_unsupported_links(value: str) -> None:
    with pytest.raises(ValueError, match="PREDECESSORS"):
        metacyc_pathway_records([_branched_pathway(value)])


def test_flat_file_continuations_do_not_truncate_predecessors(tmp_path: Path) -> None:
    path = tmp_path / "pathways.dat"
    path.write_text(
        "UNIQUE-ID - PWY-1\nREACTION-LIST - R1\nREACTION-LIST - R2\n"
        "REACTION-LIST - R3\nPREDECESSORS - (R3 R1\n/R2)\n//\n",
        encoding="utf-8",
    )
    record = metacyc_pathway_records(load_pathway_tools_dat(path))[0]
    assert len(record["mechanistic_edges"]) == 2


@pytest.mark.parametrize("text", ["/orphan\n", "UNIQUE-ID - PWY\nbroken line\n//\n"])
def test_flat_file_rejects_silently_dropped_lines(tmp_path: Path, text: str) -> None:
    path = tmp_path / "pathways.dat"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError, match="line"):
        load_pathway_tools_dat(path)


def test_duplicate_native_pathway_ids_are_rejected() -> None:
    with pytest.raises(ValueError, match="duplicate pathway"):
        metacyc_pathway_records([_branched_pathway(), _branched_pathway()])


def test_duplicate_links_keep_all_source_locators_without_duplicate_edges() -> None:
    record = metacyc_pathway_records([
        _branched_pathway('(R3 "R1")', "(R3 R1)")
    ])[0]
    assert len(record["mechanistic_edges"]) == 1
    evidence = record["mechanistic_edges"][0]["evidence"]
    assert [item["source_locator"].split("/")[-1] for item in evidence] == [
        "PREDECESSORS[1]", "PREDECESSORS[2]"
    ]


def test_subpathways_need_explicit_expansion_before_conversion() -> None:
    native = _branched_pathway("(R3 R1)")
    native["SUB-PATHWAYS"] = ["PWY-2"]
    with pytest.raises(ValueError, match="sub-pathway expansion"):
        metacyc_pathway_records([native])


def test_pmn_does_not_requalify_another_database_frame() -> None:
    native = _branched_pathway()
    native["UNIQUE-ID"] = ["PMN:ara:PWY-1"]
    with pytest.raises(ValueError, match="mismatched frame"):
        pmn_pathway_records([native], pgdb="chlamy")
