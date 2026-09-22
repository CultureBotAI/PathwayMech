from __future__ import annotations

from pathlib import Path

from pathwaymech.metacyc import load_metacyc_dat, metacyc_pathway_records
from pathwaymech.schema import validate_record

FIXTURE = Path("tests/fixtures/metacyc/pathways.dat")


def test_metacyc_flat_file_converts_to_valid_pathway_record() -> None:
    records = metacyc_pathway_records(load_metacyc_dat(FIXTURE))

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
