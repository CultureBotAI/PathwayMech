"""Synthetic membership inputs; no source table or authority claims are copied."""

from __future__ import annotations

import csv
import hashlib
import io
from pathlib import Path

import pytest

from pathwaymech.hadeg import HADEG_COLUMNS, hadeg_seed_rows, load_hadeg_memberships

FIXTURE = Path(__file__).parent / "fixtures" / "hadeg" / "memberships.csv"
COMMIT = "abcdef01" * 5


def _load(path: Path, **kwargs):
    return load_hadeg_memberships(
        path,
        source_commit=kwargs.get("source_commit", COMMIT),
        expected_sha256=kwargs.get(
            "expected_sha256", hashlib.sha256(path.read_bytes()).hexdigest()
        ),
    )


def _write(tmp_path: Path, rows: list[list[str]], *, header=HADEG_COLUMNS) -> Path:
    path = tmp_path / "memberships.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)
    return path


def _row(protein_id="P12345") -> list[str]:
    return ["Aerobic", "Compound", "Group", "Subgroup", protein_id, "gene", "Ae", "A", "B_"]


def test_preserves_membership_scope_raw_values_and_pinned_provenance():
    records = _load(FIXTURE)
    assert len(records) == 4
    assert records[0].protein_id == "P12345 "
    assert records[0].identifier_candidate == "P12345"
    assert [r.candidate_namespace for r in records] == [
        "UniProtKB",
        "NCBIProtein",
        "unresolved",
        "UniProtKB",
    ]
    assert records[0].source_line == 2
    assert records[-1].source_line == 5
    assert records[0].source_url == (
        f"https://raw.githubusercontent.com/jarojasva/HADEG/{COMMIT}/Tables/7_All_pathways.csv"
    )
    assert records[0].source_sha256 == hashlib.sha256(FIXTURE.read_bytes()).hexdigest()
    assert all(r.identifier_verification == "not_verified" for r in records)

    output = list(csv.DictReader(io.StringIO("\n".join(hadeg_seed_rows(records))), delimiter="\t"))
    assert len(output) == 4
    assert output[0]["Protein_ID"] == "P12345 "
    assert output[0]["source_locator"] == "Tables/7_All_pathways.csv:line=2"
    assert output[3]["Pathway"] == "Example_other_group"
    assert {r["claim_type"] for r in output} == {"source_reported_group_membership"}
    assert (
        not {"taxon", "taxa", "predicate", "reactions", "mechanistic_edges", "curie"}
        & output[0].keys()
    )


@pytest.mark.parametrize(
    ("identifier", "namespace"),
    [
        ("A0A0B4J2F0", "UniProtKB"),
        ("NP_123456.2", "NCBIProtein"),
        ("BAB1234567.1", "NCBIProtein"),
        ("BAB123456.1", "unresolved"),
        ("NM_123456.1", "unresolved"),
        ("AB123456", "unresolved"),
        ("AAA12345", "unresolved"),
        ("UPI0000000001", "unresolved"),
        ("1ABC_A", "unresolved"),
        ("local_gene", "unresolved"),
        ("P12345-2", "unresolved"),
        ("p12345", "unresolved"),
        ("P12345 extra", "unresolved"),
    ],
)
def test_namespace_patterns_are_conservative_unverified_candidates(tmp_path, identifier, namespace):
    record = _load(_write(tmp_path, [_row(identifier)]))[0]
    assert record.candidate_namespace == namespace
    assert record.identifier_verification == "not_verified"
    assert record.protein_id == identifier


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"source_commit": "main"}, "40-character"),
        ({"source_commit": "a" * 39}, "40-character"),
        ({"source_commit": "g" * 40}, "40-character"),
        ({"expected_sha256": "a" * 63}, "64 hexadecimal"),
        ({"expected_sha256": "g" * 64}, "64 hexadecimal"),
        ({"expected_sha256": "0" * 64}, "SHA-256 mismatch"),
    ],
)
def test_requires_full_commit_and_matching_digest(kwargs, message):
    with pytest.raises(ValueError, match=message):
        _load(FIXTURE, **kwargs)


def test_canonicalizes_hex_case_without_changing_raw_values():
    digest = hashlib.sha256(FIXTURE.read_bytes()).hexdigest()
    record = _load(FIXTURE, source_commit=COMMIT.upper(), expected_sha256=digest.upper())[0]
    assert record.source_commit == COMMIT
    assert record.source_sha256 == digest
    assert record.protein_id == "P12345 "


@pytest.mark.parametrize(
    "header",
    [
        HADEG_COLUMNS[:-1],
        (*HADEG_COLUMNS, "extra"),
        (*HADEG_COLUMNS[:-1], "Protein_ID"),
        tuple(reversed(HADEG_COLUMNS)),
    ],
)
def test_rejects_wrong_duplicate_or_reordered_headers(tmp_path, header):
    with pytest.raises(ValueError, match="exactly the nine expected columns"):
        _load(_write(tmp_path, [_row()], header=header))


@pytest.mark.parametrize("row", [_row()[:-1], [*_row(), "extra"], []])
def test_rejects_ragged_or_blank_rows_after_valid_input(tmp_path, row):
    with pytest.raises(ValueError, match="line 3: expected nine fields"):
        _load(_write(tmp_path, [_row(), row]))


@pytest.mark.parametrize("value", ["", "   ", "\t"])
def test_rejects_blank_fields(tmp_path, value):
    with pytest.raises(ValueError, match="blank Protein_ID"):
        _load(_write(tmp_path, [_row(value)]))


@pytest.mark.parametrize("value", ["a\tb", "a\nb", "a\rb", "a\x00b", "a\x7fb", "a\u2028b"])
def test_rejects_control_characters_instead_of_silently_changing_tsv_cells(tmp_path, value):
    with pytest.raises(ValueError, match="control character in Protein_ID"):
        _load(_write(tmp_path, [_row(value)]))


def test_rejects_duplicate_complete_source_rows(tmp_path):
    with pytest.raises(ValueError, match="line 3: duplicate source row"):
        _load(_write(tmp_path, [_row(), _row()]))


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        (b"", "exactly the nine expected columns"),
        ((",".join(HADEG_COLUMNS) + "\n").encode(), "no membership rows"),
        ((",".join(HADEG_COLUMNS) + '\n"unterminated').encode(), "malformed CSV"),
        (b"\xff", "must be UTF-8"),
    ],
)
def test_rejects_empty_malformed_and_non_utf8_files(tmp_path, payload, message):
    path = tmp_path / "invalid.csv"
    path.write_bytes(payload)
    with pytest.raises(ValueError, match=message):
        _load(path)


def test_quoted_comma_and_crlf_preserve_values_and_physical_lines(tmp_path):
    row = _row()
    row[1] = '"Example compound", with qualifier'
    records = _load(_write(tmp_path, [row, _row("AAA12345.1")]))
    assert records[0].raw_values[1] == '"Example compound", with qualifier'
    assert [r.source_line for r in records] == [2, 3]
    output = list(csv.DictReader(io.StringIO("\n".join(hadeg_seed_rows(records))), delimiter="\t"))
    assert output[0]["Compound"] == row[1]
