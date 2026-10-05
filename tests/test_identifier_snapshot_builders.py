"""Snapshot generation must obtain assertions from the independent authority."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

import pytest
import yaml

from scripts.build_ontology_identifier_snapshot import main


@pytest.fixture
def authority(tmp_path: Path) -> Path:
    database = tmp_path / "authority.db"
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE prefix (prefix TEXT, base TEXT)")
        connection.executemany("INSERT INTO prefix VALUES (?, ?)", [
            ("obo", "http://purl.obolibrary.org/obo/"),
            ("cc", "https://creativecommons.org/licenses/"),
        ])
        connection.execute(
            "CREATE TABLE statements (subject TEXT, predicate TEXT, object TEXT, value TEXT)"
        )
        connection.executemany("INSERT INTO statements VALUES (?, ?, ?, ?)", [
            ("obo:go.owl", "owl:versionIRI", "obo:go/releases/2026-07-26/go.owl", None),
            ("obo:go.owl", "owl:versionInfo", None, "2026-07-26"),
            ("obo:go.owl", "dcterms:license", "cc:by/4.0/", None),
            ("GO:0008150", "rdfs:label", None, "biological_process"),
            ("GO:0008150", "oio:hasExactSynonym", None, "biological process"),
            ("GO:0008150", "oio:hasRelatedSynonym", None, "physiological phenomenon"),
            ("GO:0006096", "rdfs:label", None, "glycolytic process"),
        ])
    return database


def write_record(corpus: Path, relative_path: str, identifier: str, label: str) -> None:
    path = corpus / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({"id": identifier, "label": label}), encoding="utf-8")


def build(authority: Path, corpus: Path, output: Path) -> int:
    return main([
        "--source", f"GO={authority}", "--corpus", str(corpus), "--output", str(output),
    ])


def test_nested_snapshot_uses_authority_not_corpus_labels(
    tmp_path: Path, authority: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    corpus = tmp_path / "corpus"
    write_record(corpus, "record.yaml", "GO:0008150", "invented nonsense")
    # A label beginning with a CURIE is still prose, never an identifier slot.
    write_record(corpus, "nested/record.yaml", "GO:0006096", "GO:9999999 curator description")
    output = tmp_path / "snapshot.json"

    assert build(authority, corpus, output) == 0

    snapshot = json.loads(output.read_text())
    assert set(snapshot["terms"]) == {"GO:0008150", "GO:0006096"}
    assert snapshot["terms"]["GO:0008150"] == {
        "label": "biological_process",
        "synonyms": ["biological process"],
        "source": "go-2026-07-26",
    }
    assert snapshot["terms"]["GO:0006096"]["label"] == "glycolytic process"
    assert "LABEL_DIFFERENCE" in capsys.readouterr().out
    assert snapshot["sources"]["go-2026-07-26"] == {
        "url": "http://purl.obolibrary.org/obo/go/releases/2026-07-26/go.owl",
        "version": "2026-07-26",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "sha256": hashlib.sha256(authority.read_bytes()).hexdigest(),
        "sha256_scope": "uncompressed_semantic_sql_database",
    }


def test_unresolved_identifier_does_not_publish_or_replace_snapshot(
    tmp_path: Path, authority: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    corpus = tmp_path / "corpus"
    write_record(corpus, "record.yaml", "GO:9999999", "invented but plausible process")
    output = tmp_path / "snapshot.json"

    assert build(authority, corpus, output) == 1
    assert not output.exists()
    assert "UNRESOLVED\tGO:9999999" in capsys.readouterr().err

    output.write_text("previous reviewed snapshot\n")
    assert build(authority, corpus, output) == 1
    assert output.read_text() == "previous reviewed snapshot\n"


@pytest.mark.parametrize("source_state", ["missing", "empty", "no_terms", "no_license"])
def test_unavailable_or_empty_authority_never_publishes(
    tmp_path: Path, authority: Path, source_state: str
) -> None:
    corpus = tmp_path / "corpus"
    write_record(corpus, "record.yaml", "GO:0008150", "biological_process")
    if source_state == "missing":
        authority.unlink()
    elif source_state == "empty":
        authority.write_bytes(b"")
    else:
        with sqlite3.connect(authority) as connection:
            if source_state == "no_terms":
                connection.execute("DELETE FROM statements WHERE subject LIKE 'GO:%'")
            else:
                connection.execute("DELETE FROM statements WHERE predicate='dcterms:license'")
    output = tmp_path / "snapshot.json"

    assert build(authority, corpus, output) == 1
    assert not output.exists()


@pytest.mark.parametrize("empty_selection", [False, True])
def test_missing_corpus_or_zero_identifier_selection_cannot_publish(
    tmp_path: Path, authority: Path, empty_selection: bool
) -> None:
    corpus = tmp_path / "corpus"
    if empty_selection:
        write_record(corpus, "record.yaml", "MetaCyc:TRPSYN-PWY", "tryptophan biosynthesis")
    output = tmp_path / "snapshot.json"

    assert build(authority, corpus, output) == 1
    assert not output.exists()
