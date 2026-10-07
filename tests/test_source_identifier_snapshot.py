"""Primary source extraction must not turn curated labels into an authority."""

from __future__ import annotations

import hashlib
import io
import json
import sys
import tarfile
from pathlib import Path

import pytest

from scripts.build_source_identifier_snapshot import (
    build_snapshot,
    gocam_terms,
    main,
    metacyc_terms,
    source_terms,
)


def test_untyped_native_gocam_instance_has_existence_without_invented_chemical_identity():
    terms = list(gocam_terms({"id": "gomodel:test", "individuals": [{"id": "gomodel:untyped"}]}))
    assert terms == [("gomodel:untyped", "gomodel:untyped", [])]


def test_ncbi_protein_native_accession_and_gene_synonym(tmp_path):
    source = tmp_path / "protein.xml"
    source.write_text("""<GBSet><GBSeq>
      <GBSeq_accession-version>AKL64828.1</GBSeq_accession-version>
      <GBSeq_definition>ACP S-malonyltransferase [Streptomyces sp. Mg1]</GBSeq_definition>
      <GBSeq_feature-table><GBFeature><GBFeature_quals><GBQualifier>
      <GBQualifier_name>gene</GBQualifier_name><GBQualifier_value>lnyI</GBQualifier_value>
      </GBQualifier></GBFeature_quals></GBFeature></GBSeq_feature-table>
      </GBSeq></GBSet>""")
    assert list(source_terms("ncbi-protein-xml", source)) == [(
        "NCBIProtein:AKL64828.1", "ACP S-malonyltransferase [Streptomyces sp. Mg1]", ["lnyI"],
    )]


def source_fixture(tmp_path: Path) -> tuple[Path, Path, Path]:
    records = tmp_path / "records"
    (records / "nested").mkdir(parents=True)
    (records / "nested" / "record.yaml").write_text(
        "id: MetaCyc:TEST-PWY\nlabel: curator description, not authority\n"
    )
    cache = tmp_path / "cache"
    cache.mkdir()
    raw = (
        b"<TITLE>MetaCyc Native source name</TITLE>"
        b"<script>var typeObjectPage = {object:'TEST-PWY',orgid:'META',"
        b"type:'Compounds'}</script>"
    )
    (cache / "source.html").write_bytes(raw)
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        json.dumps(
            [
                {
                    "key": "primary-source",
                    "kind": "metacyc-html",
                    "path": "source.html",
                    "url": "https://example.org/native/TEST-PWY",
                    "version": "fixture",
                    "license": "fixture",
                    "sha256": hashlib.sha256(raw).hexdigest(),
                }
            ]
        )
    )
    return manifest, records, cache


def test_nested_selection_reads_label_only_from_primary_source(tmp_path: Path) -> None:
    manifest, records, cache = source_fixture(tmp_path)
    result = build_snapshot(manifest, records, cache)
    assert result["terms"]["MetaCyc:TEST-PWY"]["label"] == "Native source name"
    assert "curator description" not in json.dumps(result)


def test_modified_source_bytes_cannot_reuse_frozen_provenance(tmp_path: Path) -> None:
    manifest, records, cache = source_fixture(tmp_path)
    (cache / "source.html").write_text("replacement source")
    with pytest.raises(ValueError, match="sha256"):
        build_snapshot(manifest, records, cache)


@pytest.mark.parametrize(
    "text",
    [
        "<TITLE>MetaCyc Source name</TITLE>",
        "<TITLE>Create Account</TITLE>",
        "<TITLE>MetaCyc Error</TITLE>"
        "<script>var typeObjectPage = {object:'TEST-PWY',orgid:'META'}</script>",
        "<TITLE>MetaCyc Source name</TITLE>"
        "<script>var typeObjectPage = {object:'TEST-PWY',orgid:'YEAST'}</script>",
        "<TITLE>MetaCyc TEST-PWY</TITLE>"
        "<script>var typeObjectPage = {object:'TEST-PWY',orgid:'META'}</script>",
    ],
)
def test_unresolved_or_wrong_database_page_is_not_authority(text: str) -> None:
    with pytest.raises(ValueError):
        list(metacyc_terms(text))


def test_no_source_matches_is_an_error(tmp_path: Path) -> None:
    manifest, records, cache = source_fixture(tmp_path)
    (records / "nested" / "record.yaml").write_text("id: MetaCyc:UNKNOWN\nlabel: unknown\n")
    with pytest.raises(ValueError, match="no corpus identifiers"):
        build_snapshot(manifest, records, cache)


def test_partial_refresh_preserves_existing_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    manifest, records, cache = source_fixture(tmp_path)
    (records / "nested" / "record.yaml").write_text(
        "id: MetaCyc:TEST-PWY\nlabel: test\nparticipants:\n"
        "  - id: MetaCyc:MISSING\n    label: unknown\n"
        "  - id: CHEBI:15377\n    label: water\n"
    )
    output = tmp_path / "authority.json"
    output.write_text("previous authority\n")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "build_source_identifier_snapshot.py",
            "--manifest",
            str(manifest),
            "--records",
            str(records),
            "--cache-dir",
            str(cache),
            "--output",
            str(output),
        ],
    )
    with pytest.raises(ValueError, match="unresolved source identifiers: MetaCyc:MISSING"):
        main()
    assert output.read_text() == "previous authority\n"


def test_gocam_display_names_cannot_masquerade_as_canonical_names(tmp_path: Path) -> None:
    records = tmp_path / "records"
    records.mkdir()
    (records / "record.yaml").write_text(
        "id: gomodel:TEST\nlabel: model\nparticipants:\n"
        "- id: SGD:S000000001\n  label: gene\n"
        "reactions:\n- id: gomodel:activity\n  label: activity\n"
    )
    model = {
        "id": "gomodel:TEST",
        "annotations": [{"key": "title", "value": "model display"}],
        "individuals": [
            {
                "id": "gomodel:activity",
                "type": [{"id": "SGD:S000000001", "label": "gene Scer"}],
                "annotations": [{"key": "rdfs:label", "value": "activity display"}],
            }
        ],
    }
    raw = json.dumps(model).encode()
    source = tmp_path / "models.tgz"
    with tarfile.open(source, "w:gz") as archive:
        member = tarfile.TarInfo("model.json")
        member.size = len(raw)
        archive.addfile(member, io.BytesIO(raw))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        json.dumps(
            [
                {
                    "key": "gocam",
                    "kind": "gocam-tar",
                    "path": "models.tgz",
                    "url": "https://example.org/models.tgz",
                    "version": "fixture",
                    "license": "fixture",
                    "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                }
            ]
        )
    )
    result = build_snapshot(manifest, records, tmp_path)
    assert set(result["terms"]) == {"gomodel:TEST", "gomodel:activity", "SGD:S000000001"}
    assert {term["label_kind"] for term in result["terms"].values()} == {"source_context"}
