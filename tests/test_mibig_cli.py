from __future__ import annotations

import csv
import io
import json
from pathlib import Path

import pytest

from pathwaymech.cli import import_mibig_main


def test_mibig_yaml_refuses_late_retired_entry_without_partial_output(
    tmp_path: Path, capsys: pytest.CaptureFixture[str],
) -> None:
    active = tmp_path / "active.json"
    retired = tmp_path / "retired.json"
    active.write_text(json.dumps({"accession": "BGC0000829", "status": "active"}))
    retired.write_text(json.dumps({
        "accession": "BGC0000828", "status": "retired",
        "retirement_reasons": ["Duplicate of BGC0000829"],
        "see_also": ["BGC0000829"],
    }))

    assert import_mibig_main(["--yaml", str(active), str(retired)]) == 1
    output = capsys.readouterr()
    assert output.out == ""
    assert "BGC0000828" in output.err
    assert "retired" in output.err.lower()


def test_mibig_support_output_keeps_retired_entry_for_audit(
    tmp_path: Path, capsys: pytest.CaptureFixture[str],
) -> None:
    path = tmp_path / "retired.json"
    path.write_text(json.dumps({
        "accession": "BGC0000828", "status": "retired",
        "quality": "questionable", "completeness": "unknown",
        "retirement_reasons": ["Duplicate\tentry\nwith notes"],
        "see_also": ["BGC0000829"],
    }))

    assert import_mibig_main([str(path)]) == 0
    output = capsys.readouterr()
    rows = list(csv.DictReader(io.StringIO(output.out), delimiter="\t"))
    assert len(rows) == 1
    assert rows[0]["mibig_id"] == "MIBiG:BGC0000828"
    assert rows[0]["status"] == "retired"
    assert rows[0]["quality"] == "questionable"
    assert json.loads(rows[0]["retirement_reasons"]) == ["Duplicate\tentry\nwith notes"]
    assert json.loads(rows[0]["see_also"]) == ["BGC0000829"]
    assert output.err == ""
