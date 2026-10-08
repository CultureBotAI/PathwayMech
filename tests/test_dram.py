from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path

import pytest

from pathwaymech.dram import DRAM_NATIVE_HEADER, dram_seed_rows, load_dram_module_steps

COMMIT = "abcde" * 8
# Deliberately synthetic support rows; no upstream dataset is vendored.
FIRST = ["test enzyme", "K99991", "M99991", "test module", "0,0", "", "", "", ""]


def _table(path: Path, rows: list[list[str]], header: list[str] | None = None) -> str:
    with path.open("w", encoding="utf-8", newline="") as stream:
        csv.writer(stream, delimiter="\t").writerows(
            [list(DRAM_NATIVE_HEADER) if header is None else header, *rows]
        )
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load(path: Path, digest: str):
    return load_dram_module_steps(path, source_commit=COMMIT, expected_sha256=digest)


def test_duplicate_rows_survive_with_distinct_pinned_artifact_locators(tmp_path: Path) -> None:
    path = tmp_path / "renamed table.tsv"
    digest = _table(path, [FIRST, FIRST])

    first, second = _load(path, digest.upper())

    assert first.native_fields == second.native_fields == tuple(
        zip(DRAM_NATIVE_HEADER, FIRST, strict=True)
    )
    assert first.source_line_start == first.source_line_end == 2
    assert second.source_line_start == second.source_line_end == 3
    assert first.source_row_id != second.source_row_id
    assert first.source_row_id == f"DRAM1:{digest}:L2-L2"
    assert first.source_file == path.name
    assert first.source_commit == COMMIT
    assert first.source_sha256 == digest
    assert first.source_path == "data/module_step_form.tsv"
    assert first.source_url.endswith(f"/{COMMIT}/data/module_step_form.tsv")


def test_native_cells_roundtrip_controls_names_and_conflicting_description_ids(
    tmp_path: Path,
) -> None:
    path = tmp_path / "native.tsv"
    row = [
        ' K99999 descriptive text\t"quoted"\rsecond\nthird ',
        "K99991",
        "M99991",
        " module \u00a0",
        "5,0,1,0",
        "C99991,G99992",
        "first, name,second",
        "G99993",
        "",
    ]
    digest = _table(path, [row, FIRST])

    records = _load(path, digest)
    exported = list(
        csv.DictReader(io.StringIO("\n".join(dram_seed_rows(records)), newline=""), delimiter="\t")
    )

    assert len(exported) == 2
    assert [exported[0][name] for name in DRAM_NATIVE_HEADER] == row
    assert json.loads(exported[0]["native_fields_json"]) == [
        [name, value] for name, value in zip(DRAM_NATIVE_HEADER, row, strict=True)
    ]
    assert records[0].source_line_start == 2
    assert records[0].source_line_end == 4
    assert records[1].source_line_start == records[1].source_line_end == 5


@pytest.mark.parametrize("tail", [FIRST[:-1], [*FIRST, "extra"], [], [*FIRST[:1], "", *FIRST[2:]]])
def test_late_malformed_row_is_refused_without_partial_result(
    tmp_path: Path, tail: list[str]
) -> None:
    path = tmp_path / "malformed.tsv"
    digest = _table(path, [FIRST, tail])

    with pytest.raises(ValueError, match="DRAM lines 3-3"):
        _load(path, digest)


@pytest.mark.parametrize(
    "header",
    [list(reversed(DRAM_NATIVE_HEADER)), list(DRAM_NATIVE_HEADER[:-1]), ["ko"] * 9],
)
def test_schema_drift_is_refused(tmp_path: Path, header: list[str]) -> None:
    path = tmp_path / "changed.tsv"
    digest = _table(path, [FIRST], header)

    with pytest.raises(ValueError, match="exact nine-column"):
        _load(path, digest)


@pytest.mark.parametrize("payload", [b"", b"\xff", b'gene\t"unterminated'])
def test_empty_encoding_or_csv_errors_are_value_errors(tmp_path: Path, payload: bytes) -> None:
    path = tmp_path / "bad.tsv"
    path.write_bytes(payload)

    with pytest.raises(ValueError):
        _load(path, hashlib.sha256(payload).hexdigest())


def test_header_only_is_not_successful_ingestion(tmp_path: Path) -> None:
    path = tmp_path / "header.tsv"
    digest = _table(path, [])

    with pytest.raises(ValueError, match="no data rows"):
        _load(path, digest)


def test_hash_mismatch_precedes_table_parsing(tmp_path: Path) -> None:
    path = tmp_path / "changed.tsv"
    path.write_bytes(b"not the pinned table")

    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        _load(path, "0" * 64)


@pytest.mark.parametrize("commit", ["master", "a" * 39, "g" * 40, "", None])
def test_commit_must_be_full_hexadecimal_sha(tmp_path: Path, commit: str) -> None:
    path = tmp_path / "native.tsv"
    digest = _table(path, [FIRST])

    with pytest.raises(ValueError, match="source_commit"):
        load_dram_module_steps(path, source_commit=commit, expected_sha256=digest)


@pytest.mark.parametrize("digest", ["", "a" * 63, "g" * 64, None])
def test_artifact_digest_is_mandatory_and_well_formed(tmp_path: Path, digest: str) -> None:
    path = tmp_path / "native.tsv"
    _table(path, [FIRST])

    with pytest.raises(ValueError, match="expected_sha256"):
        _load(path, digest)
