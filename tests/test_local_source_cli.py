from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path

import pytest
import yaml

from pathwaymech.cli import import_biopax_main, import_dbcan_pul_main

BIOPAX = Path("tests/fixtures/biopax/R-TEST.owl")
DBCAN = Path("tests/fixtures/dbcan/dbcan-pul.tsv")


def test_biopax_cli_binds_draft_to_input_bytes_and_source(
    capsys: pytest.CaptureFixture[str],
) -> None:
    digest = hashlib.sha256(BIOPAX.read_bytes()).hexdigest()
    assert import_biopax_main([
        "Reactome", str(BIOPAX), "--sha256", digest,
        "--source-url", "https://example.org/source.zip", "--source-version", "release/member.owl",
    ]) == 0
    result = yaml.safe_load(capsys.readouterr().out)
    reference = next(ref for ref in result["references"] if ref["id"] == result["id"])
    assert reference["source_sha256"] == digest
    assert reference["source_version"] == "release/member.owl"
    assert reference["url"] == "https://example.org/source.zip"


def test_dbcan_cli_exports_complete_native_cells_with_digest(
    capsys: pytest.CaptureFixture[str],
) -> None:
    digest = hashlib.sha256(DBCAN.read_bytes()).hexdigest()
    assert import_dbcan_pul_main([
        str(DBCAN), "--sha256", digest, "--include-provenance",
    ]) == 0
    result = list(csv.DictReader(io.StringIO(capsys.readouterr().out), delimiter="\t"))
    with DBCAN.open(newline="") as stream:
        source = list(csv.reader(stream, delimiter="\t"))
    assert len(result) == len(source) - 1
    for row, native in zip(result, source[1:], strict=True):
        assert row["source_sha256"] == digest
        assert json.loads(row["native_fields_json"]) == [
            list(pair) for pair in zip(source[0], native, strict=True)
        ]


@pytest.mark.parametrize("kind", ["biopax", "dbcan"])
@pytest.mark.parametrize("failure", ["checksum", "empty_checksum", "malformed", "missing"])
def test_local_source_cli_failure_is_atomic(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], kind: str, failure: str,
) -> None:
    source = BIOPAX if kind == "biopax" else DBCAN
    main = import_biopax_main if kind == "biopax" else import_dbcan_pul_main
    args = ["Reactome"] if kind == "biopax" else []
    args.append(str(source))
    if failure in {"checksum", "empty_checksum"}:
        args += ["--sha256", "0" * 64 if failure == "checksum" else ""]
    else:
        second = tmp_path / ("second.owl" if kind == "biopax" else "second.xlsx")
        if failure == "malformed":
            second.write_text("not XML or an XLSX workbook")
        args.append(str(second))
    assert main(args) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err


@pytest.mark.parametrize("kind", ["biopax", "dbcan"])
def test_local_source_digest_cannot_ambiguously_bind_multiple_files(
    capsys: pytest.CaptureFixture[str], kind: str,
) -> None:
    source = BIOPAX if kind == "biopax" else DBCAN
    main = import_biopax_main if kind == "biopax" else import_dbcan_pul_main
    args = ["Reactome"] if kind == "biopax" else []
    with pytest.raises(SystemExit) as error:
        main([*args, str(source), str(source), "--sha256", "0" * 64])
    assert error.value.code == 2
    assert capsys.readouterr().out == ""


def test_biopax_source_url_parse_error_has_no_traceback(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as error:
        import_biopax_main([
            "Reactome", str(BIOPAX), "--sha256", "0" * 64,
            "--source-url", "https://[",
        ])
    assert error.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "valid absolute HTTP(S)" in captured.err
