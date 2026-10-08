import csv
import hashlib
import io
import json
import shutil
from pathlib import Path

import pytest

from pathwaymech.cli import import_brenda_main

CANARY = Path("research/source_discovery/2026-10-07-brenda-canary")
MANIFEST = "role-import-manifest.json"


def test_brenda_cli_preserves_real_canary_bindings(capsys: pytest.CaptureFixture[str]) -> None:
    assert import_brenda_main([str(CANARY / MANIFEST)]) == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    rows = list(csv.DictReader(io.StringIO(captured.out), delimiter="\t"))
    original = json.loads((CANARY / "roles.json").read_text())["results"]["bindings"]
    assert [json.loads(row["raw_binding_json"]) for row in rows] == original
    assert len(rows) == 62
    assert len({row["reaction_uri"] for row in rows}) == 15


@pytest.mark.parametrize("failure", ["checksum", "late_binding", "missing_artifact"])
def test_brenda_cli_fails_without_partial_output(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], failure: str,
) -> None:
    for name in (MANIFEST, "roles.rq", "roles.json"):
        shutil.copyfile(CANARY / name, tmp_path / name)
    results = tmp_path / "roles.json"
    if failure == "checksum":
        results.write_bytes(results.read_bytes() + b" ")
    elif failure == "late_binding":
        payload = json.loads(results.read_text())
        payload["results"]["bindings"][-1]["reaction"]["type"] = "literal"
        results.write_text(json.dumps(payload))
        manifest = json.loads((tmp_path / MANIFEST).read_text())
        manifest["results_sha256"] = hashlib.sha256(results.read_bytes()).hexdigest()
        (tmp_path / MANIFEST).write_text(json.dumps(manifest))
    else:
        results.unlink()
    assert import_brenda_main([str(tmp_path / MANIFEST)]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert str(tmp_path / MANIFEST) in captured.err
