from __future__ import annotations

import json
from pathlib import Path

import pytest

from pathwaymech.cross_mech import SiblingProtein, build_pathway_index, build_report
from pathwaymech.rhea_directions import load_rhea_directions, master_ids


def test_directional_record_matches_master_and_other_direction_annotations():
    # Independent upstream quartet for the MurA reaction, not numeric rounding.
    directions = {value: "18681" for value in ("18681", "18682", "18683", "18684")}
    records = [{"id": "MetaCyc:A", "label": "route A",
                "participants": [{"id": "UniProtKB:P0A749", "label": "MurA"}],
                "reactions": [{"id": "RHEA:18682", "label": "MurA reaction"}]},
               {"id": "MetaCyc:B", "label": "route B", "participants": [],
                "reactions": [{"id": "RHEA:18683", "label": "opposite direction"}]}]
    protein = SiblingProtein("Mech", "a.yaml", "a", "a", "protein", "enzyme", "P0A749")
    annotations = {"P0A749": {"rhea": ["RHEA:18681"]}}
    index = build_pathway_index(records, annotations=annotations, rhea_directions=directions)
    report = build_report(index, {"Mech": ([protein], [], [])}, annotations)
    assert len(report.overlaps) == 1
    # A direct match to one record must not hide a chemistry lead for another.
    assert [(row["pathway_record"], row["basis"], row["shared_rhea"])
            for row in report.reaction_matches] == [("MetaCyc:B", "record_rhea", "RHEA:18681")]
    assert master_ids(["RHEA:99999", "18683"], directions) == {"99999", "18681"}


def test_pinned_map_is_provenanced_and_covers_real_directional_ids():
    path = Path(__file__).resolve().parents[1] / "conf" / "rhea_directions.json"
    mapping = load_rhea_directions(path)
    assert mapping["18682"] == mapping["18683"] == "18681"


@pytest.mark.parametrize("change", [
    {"format": "unknown"}, {"source": {}}, {"directions": {}},
    {"directions": {"18681": "18680"}},
])
def test_map_rejects_unverifiable_or_inconsistent_inputs(tmp_path, change):
    path = tmp_path / "rhea.json"
    data = {"format": "rhea-directions/1",
            "source": {"url": "https://example.test/rhea.tsv", "retrieved_at": "2026-10-05",
                       "license": "CC-BY-4.0", "sha256": "a" * 64},
            "directions": {"18680": "18680", "18681": "18680"}}
    path.write_text(json.dumps(data | change))
    with pytest.raises(ValueError):
        load_rhea_directions(path)
