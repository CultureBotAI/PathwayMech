from pathlib import Path

import pytest
import yaml

from pathwaymech.cli import import_metacyc_main, import_pmn_main


def test_pmn_cli_requires_scope(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as error:
        import_pmn_main(["tests/fixtures/pmn/pathways.dat"])
    assert error.value.code == 2
    assert "--pgdb" in capsys.readouterr().err


def test_pmn_cli_preserves_native_scope_and_export_version(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert import_pmn_main([
        "--pgdb", "Chlamy", "--source-version", "fixture-1",
        "tests/fixtures/pmn/pathways.dat",
    ]) == 0
    result = yaml.safe_load(capsys.readouterr().out)
    assert result["id"] == "PMN:Chlamy:CHLAMY-GLYOX"
    assert result["references"][0]["source_version"] == "fixture-1"


@pytest.mark.parametrize("failure", ["missing", "malformed", "duplicate"])
def test_pathway_tools_cli_late_failure_is_atomic(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], failure: str,
) -> None:
    first = "tests/fixtures/metacyc/pathways.dat"
    second = tmp_path / "second.dat"
    if failure == "malformed":
        second.write_text("broken line\n", encoding="utf-8")
    elif failure == "duplicate":
        second.write_bytes(Path(first).read_bytes())
    assert import_metacyc_main([first, str(second)]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert str(second) in captured.err


def test_pathway_tools_cli_selects_canary_from_full_export(
    tmp_path: Path, capsys: pytest.CaptureFixture[str],
) -> None:
    export = tmp_path / "pathways.dat"
    export.write_text(
        "UNIQUE-ID - ELEMENTARY\nREACTION-LIST - R1\nREACTION-LIST - R2\n"
        "PREDECESSORS - (R2 R1)\n//\n"
        "UNIQUE-ID - SUPER\nTYPES - Super-Pathways\nSUB-PATHWAYS - ELEMENTARY\n//\n",
        encoding="utf-8",
    )
    assert import_metacyc_main([str(export), "--pathway-id", "ELEMENTARY"]) == 0
    assert yaml.safe_load(capsys.readouterr().out)["id"] == "MetaCyc:ELEMENTARY"
    assert import_metacyc_main([str(export), "--pathway-id", "SUPER"]) == 1
    assert capsys.readouterr().out == ""
    assert import_metacyc_main([str(export), "--pathway-id", "MISSING"]) == 1
    assert "not found" in capsys.readouterr().err


def test_pathway_tools_cli_uses_explicit_strict_encoding(
    tmp_path: Path, capsys: pytest.CaptureFixture[str],
) -> None:
    export = tmp_path / "pathways.dat"
    export.write_bytes(b"# Copyright \xa9\nUNIQUE-ID - PWY\nCOMMON-NAME - caf\xe9\n//\n")
    assert import_metacyc_main([str(export)]) == 1
    assert capsys.readouterr().out == ""
    assert import_metacyc_main([str(export), "--encoding", "latin-1"]) == 0
    assert yaml.safe_load(capsys.readouterr().out)["label"] == "caf\u00e9"
