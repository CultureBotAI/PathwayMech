from __future__ import annotations

from pathlib import Path

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
                    "quote": (
                        "MetaCyc predecessor link PHOSGLYPHOS-RXN "
                        "before 2PGADEHYDRAT-RXN."
                    ),
                }
            ],
        }
    ]


def test_pmn_flat_file_converts_to_valid_pathway_record() -> None:
    records = pmn_pathway_records(load_pathway_tools_dat(PMN_FIXTURE))

    record = validate_record(records[0])

    assert record.id == "PMN:CHLAMY-GLYOX"
    assert record.reactions == [
        {"id": "PMN:RXN-GLYOX-1", "label": "RXN-GLYOX-1"},
        {"id": "PMN:RXN-GLYOX-2", "label": "RXN-GLYOX-2"},
    ]
    assert record.mechanistic_edges == [
        {
            "id": "pmn-edge-1",
            "subject": "PMN:RXN-GLYOX-1",
            "predicate": "precedes",
            "object": "PMN:RXN-GLYOX-2",
            "evidence": [
                {
                    "reference_id": "PMN:CHLAMY-GLYOX",
                    "quote": (
                        "PMN predecessor link RXN-GLYOX-1 "
                        "before RXN-GLYOX-2."
                    ),
                }
            ],
        }
    ]
