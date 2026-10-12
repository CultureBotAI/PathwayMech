import csv
import hashlib
import io
from pathlib import Path

import pytest

from pathwaymech.cli import import_hadeg_main

FIXTURE = Path("tests/fixtures/hadeg/memberships.csv")


def test_hadeg_cli_emits_support_rows(capsys: pytest.CaptureFixture[str]) -> None:
    assert import_hadeg_main([
        str(FIXTURE), "--source-commit", "a" * 40,
        "--sha256", hashlib.sha256(FIXTURE.read_bytes()).hexdigest(),
    ]) == 0
    rows = list(csv.DictReader(io.StringIO(capsys.readouterr().out), delimiter="\t"))
    assert rows
    assert all(row["claim_type"] == "source_reported_group_membership" for row in rows)
    assert all(row["identifier_verification"] == "not_verified" for row in rows)


@pytest.mark.parametrize("failure", ["checksum", "late_row", "missing_file"])
def test_hadeg_cli_errors_emit_no_partial_tsv(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], failure: str,
) -> None:
    path = tmp_path / "memberships.csv"
    payload = FIXTURE.read_bytes()
    if failure == "late_row":
        payload += b"bad,row\n"
    if failure != "missing_file":
        path.write_bytes(payload)
    digest = "0" * 64 if failure == "checksum" else hashlib.sha256(payload).hexdigest()
    assert import_hadeg_main([
        str(path), "--source-commit", "a" * 40, "--sha256", digest,
    ]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert str(path) in captured.err
