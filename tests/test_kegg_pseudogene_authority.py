"""Explicit pseudogene identity, never a fallback from the complete-CDS profile."""

from __future__ import annotations

import copy
import hashlib
import json
import sys

import pytest
import yaml

from pathwaymech.identifiers import _load_authority, identifier_errors
from pathwaymech.kegg_gene import (
    GENE_KIND,
    PSEUDOGENE_KIND,
    gene_metadata,
    gene_term,
    project,
    project_pseudogene,
    validate_gene_assertions,
    validate_gene_metadata,
)
from scripts import build_source_identifier_snapshot as builder

URL = "https://rest.kegg.jp/get/cgt:test_locus"
IDENTIFIER = "KEGG:cgt:test_locus"
BODY = (
    "ENTRY       test_locus       gene      T00501\n"
    "SYMBOL      source_alias\n"
    "NAME        (GenBank) pseudogene\n"
    "ORGANISM    cgt  Corynebacterium glutamicum R\n"
    "POSITION    100..102\n"
    "NTSEQ       3\n"
    "            ccg\n"
    "///\n"
)
CDS = (
    BODY.replace("gene      T00501", "CDS       T00501")
    .replace("(GenBank) pseudogene", "(GenBank) hypothetical protein")
    .replace("100..102", "100..108")
    .replace(
        "NTSEQ       3\n            ccg",
        "AASEQ       2\n            MK\nNTSEQ       9\n            atgaaataa",
    )
)


def entry(tmp_path, body=BODY, *, kind=PSEUDOGENE_KIND, key="gene", version="synthetic"):
    path = tmp_path / (key + ".txt")
    path.write_bytes(body.encode() if isinstance(body, str) else body)
    return dict(
        key=key,
        kind=kind,
        path=path.name,
        url=URL,
        version=version,
        license="Synthetic fixture",
        sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
    )


def metadata(tmp_path):
    return gene_metadata(entry(tmp_path), tmp_path)


def fixture(tmp_path):
    module = tmp_path / "module.txt"
    module.write_text("ENTRY       M99999  Pathway Module\nNAME        Test module\n///\n")
    entries = [
        entry(tmp_path),
        dict(
            key="module",
            kind="kegg-module-flatfile",
            path=module.name,
            url="https://rest.kegg.jp/get/M99999",
            version="synthetic",
            license="Synthetic",
            sha256=hashlib.sha256(module.read_bytes()).hexdigest(),
        ),
    ]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    record = dict(
        id="KEGG:M99999",
        label="Test module",
        taxa=[],
        reactions=[],
        participants=[dict(id=IDENTIFIER, label="test_locus", category="gene")],
    )
    path = records / "record.yaml"
    path.write_text(yaml.safe_dump(record))
    return manifest, records, entries, record, path


def write_snapshot(tmp_path, snapshot):
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(snapshot))
    return path


def test_explicit_gene_annotation_preserves_original_without_protein_or_alias(tmp_path):
    meta = metadata(tmp_path)
    native = meta["native_gene"]
    assert native["original_text"].encode() == BODY.encode()
    assert native["native_type"] == "gene"
    assert native["annotation_class"] == "pseudogene"
    assert native["sequence_scope"] == "native_annotation_only"
    assert native["genome_id"] == "T00501"
    assert native["ntseq"] == {"length": 3, "sequence": "ccg"}
    assert "aaseq" not in native
    assert gene_term(meta, "gene")[1] == dict(
        label="test_locus",
        synonyms=[],
        source="gene",
        entity_type="native_gene",
        label_kind="canonical",
    )
    assert list(builder.source_terms(PSEUDOGENE_KIND, tmp_path / "gene.txt", url=URL)) == [
        (IDENTIFIER, "test_locus", [])
    ]
    with pytest.raises(ValueError):
        project(BODY.encode(), URL)
    with pytest.raises(ValueError):
        project_pseudogene(CDS.encode(), URL)
    assert project(CDS.encode(), URL)["native_type"] == "CDS"


def test_annotation_length_is_not_interpreted_as_complete_cds():
    body = (
        BODY.replace("100..102", "complement(100..104)")
        .replace("NTSEQ       3", "NTSEQ       5")
        .replace("ccg", "ccgaa")
    )
    native = project_pseudogene(body.encode(), URL)
    assert native["ntseq"] == {"length": 5, "sequence": "ccgaa"}
    assert native["position"]["strand"] == "-"
    assert "aaseq" not in native


@pytest.mark.parametrize(
    "url",
    [
        "",
        URL.replace("https:", "http:"),
        URL.replace("rest.kegg.jp", "example.org"),
        URL.replace("rest.kegg.jp", "rest.kegg.jp.example.org"),
        URL.replace("rest.kegg.jp", "u@rest.kegg.jp"),
        URL.replace("rest.kegg.jp", "rest.kegg.jp:443"),
        URL + "/",
        URL + "?x=1",
        URL + "#x",
        URL + "\n",
        URL + " ",
        URL + "+cgt:other",
        URL + "/ntseq",
        URL.replace("cgt:", "eco:"),
        URL.replace("test_locus", "other"),
    ],
)
def test_request_scope_is_exact(url):
    with pytest.raises(ValueError):
        project_pseudogene(BODY.encode(), url)


@pytest.mark.parametrize(
    "body",
    [
        "",
        "<html>error</html>",
        BODY + BODY,
        BODY + "\n",
        BODY + "error\n",
        BODY.replace("///\n", ""),
        BODY.replace("gene      T00501", "CDS       T00501"),
        BODY.replace("gene      T00501", "RNA       T00501"),
        BODY.replace("test_locus", "other"),
        BODY.replace("T00501", "T501"),
        BODY.replace("T00501", "T00501 other"),
        BODY.replace("cgt  Coryne", "eco  Coryne"),
        BODY.replace("pseudogene", "protein"),
        BODY.replace("pseudogene", "pseudogene-like"),
        BODY.replace("pseudogene", "pseudogene protein"),
        BODY.replace("pseudogene\n", "pseudogene\n            continued"),
        BODY.replace("NTSEQ", "AASEQ       1\n            M\nNTSEQ"),
        BODY.replace("NTSEQ       3", "NTSEQ       4"),
        BODY.replace("NTSEQ       3", "NTSEQ       03"),
        BODY.replace("NTSEQ       3", "NTSEQ       0"),
        BODY.replace("ccg", "cng"),
        BODY.replace("ccg", "c c"),
        BODY.replace("100..102", "100..103"),
        BODY.replace("100..102", "102..100"),
        BODY.replace("100..102", "<100..102"),
        BODY.replace("100..102", "join(100..101,103)"),
        BODY.replace("ENTRY       ", "ENTRY\t"),
        BODY.replace("NAME        ", " NAME       "),
        BODY.replace("\n", "\r\n"),
        BODY.replace("pseudogene", "pseudo\x00gene"),
        BODY.replace("T00501\n", "T00501\n            continuation\n"),
    ],
)
def test_malformed_wrong_class_or_partial_original_rejected(body):
    with pytest.raises(ValueError):
        project_pseudogene(body.encode(), URL)


@pytest.mark.parametrize("tag", ["ENTRY", "NAME", "ORGANISM", "POSITION", "NTSEQ"])
@pytest.mark.parametrize("action", ["missing", "duplicate"])
def test_required_native_fields_cannot_be_removed_or_duplicated(tag, action):
    lines = BODY.splitlines(keepends=True)
    index = next(i for i, row in enumerate(lines) if row.startswith(tag + " "))
    lines[index : index + 1] = [] if action == "missing" else [lines[index], lines[index]]
    with pytest.raises(ValueError):
        project_pseudogene("".join(lines).encode(), URL)


@pytest.mark.parametrize(
    "field",
    [
        "id",
        "native_type",
        "annotation_class",
        "sequence_scope",
        "locus",
        "genome_id",
        "organism_code",
        "organism_name",
        "name_annotation",
        "position",
        "ntseq",
        "fields",
        "original_text",
    ],
)
@pytest.mark.parametrize("action", ["missing", "forged"])
def test_every_derived_projection_field_is_reconstructed(tmp_path, field, action):
    meta = metadata(tmp_path)
    if action == "missing":
        del meta["native_gene"][field]
    else:
        meta["native_gene"][field] = "forged"
    with pytest.raises(ValueError):
        validate_gene_metadata(meta)


@pytest.mark.parametrize(
    "problem",
    ["cds-kind", "untyped-kind", "hash", "url", "version", "aaseq", "bool-position", "raw-edit"],
)
def test_provenance_and_projection_laundering_rejected(tmp_path, problem):
    meta = metadata(tmp_path)
    if problem in {"cds-kind", "untyped-kind"}:
        meta["kind"] = GENE_KIND if problem == "cds-kind" else "kegg-module-flatfile"
    elif problem == "hash":
        meta["sha256"] = "0" * 64
    elif problem == "url":
        meta["url"] = URL.replace("test_locus", "other")
    elif problem == "version":
        meta["version"] = ""
    elif problem == "aaseq":
        meta["native_gene"]["aaseq"] = {"length": 1, "sequence": "P"}
    elif problem == "bool-position":
        meta["native_gene"]["position"]["start"] = True
    else:
        meta["native_gene"]["original_text"] = BODY.replace("ccg", "cct")
    with pytest.raises(ValueError):
        validate_gene_metadata(meta)


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize(
    "difference", ["cds", "genome", "position", "sequence", "field", "version"]
)
def test_whole_owner_conflicts_fail_before_selection_in_both_orders(
    tmp_path, selected, reverse, difference
):
    manifest, records, entries, record, path = fixture(tmp_path)
    changed = {
        "cds": CDS,
        "genome": BODY.replace("T00501", "T00502"),
        "position": BODY.replace("100..102", "101..103"),
        "sequence": BODY.replace("ccg", "cct"),
        "field": BODY.replace("NTSEQ", "DBLINKS     test: value\nNTSEQ"),
    }.get(difference, BODY)
    second = entry(
        tmp_path,
        changed,
        kind=GENE_KIND if difference == "cds" else PSEUDOGENE_KIND,
        key="second",
        version="different" if difference == "version" else "synthetic",
    )
    sources = {
        "first": gene_metadata(entries[0], tmp_path),
        "second": gene_metadata(second, tmp_path),
    }
    if reverse:
        sources = dict(reversed(list(sources.items())))
    with pytest.raises(ValueError, match="conflicting whole gene"):
        validate_gene_assertions(sources)
    entries.append(second)
    manifest.write_text(json.dumps(entries[::-1] if reverse else entries))
    if not selected:
        record["participants"] = []
        path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="conflicting whole gene"):
        builder.build_snapshot(manifest, records, tmp_path)
    with pytest.raises(ValueError, match="conflicting whole gene"):
        _load_authority(write_snapshot(tmp_path, dict(version=1, sources=sources, terms={})))


def test_builder_and_consumer_preserve_exact_typed_owner(tmp_path):
    manifest, records, _, _, _ = fixture(tmp_path)
    snapshot = builder.build_snapshot(manifest, records, tmp_path)
    assert snapshot["sources"]["gene"] == metadata(tmp_path)
    assert snapshot["terms"][IDENTIFIER] == gene_term(metadata(tmp_path), "gene")[1]
    assert _load_authority(write_snapshot(tmp_path, snapshot)) == snapshot["terms"]
    for source in ["module", "missing"]:
        bad = copy.deepcopy(snapshot)
        bad["terms"][IDENTIFIER]["source"] = source
        with pytest.raises(ValueError):
            _load_authority(write_snapshot(tmp_path, bad))


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("kind", [GENE_KIND, "kegg-module-flatfile", "uniprot"])
def test_manifest_cannot_downgrade_pseudogene_kind(tmp_path, selected, kind):
    manifest, records, entries, record, path = fixture(tmp_path)
    entries[0]["kind"] = kind
    manifest.write_text(json.dumps(entries))
    if not selected:
        record["participants"] = []
        path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError):
        builder.build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize(
    "section,category",
    [
        ("participants", "gene"),
        ("participants", "protein"),
        ("participants", "complex"),
        ("participants", None),
        ("participants", "molecular_activity"),
        ("reactions", "gene"),
        ("taxa", "gene"),
        ("record", None),
    ],
)
def test_gene_only_placement_and_canonical_locus_cannot_be_waived(tmp_path, section, category):
    manifest, records, _, record, path = fixture(tmp_path)
    snapshot = builder.build_snapshot(manifest, records, tmp_path)
    node = record["participants"].pop()
    node.pop("category")
    if category is not None:
        node["category"] = category
    if section == "record":
        record.update(id=node["id"], label=node["label"])
    else:
        record[section].append(node)
    policy = dict(
        version=1,
        namespaces={"KEGG": dict(snapshot="snapshot.json", policy="canonical")},
        contextual_labels=[
            dict(
                namespace="KEGG",
                sections=["record", "taxa", "participants", "reactions"],
                record_prefixes=["KEGG"],
                reason="Attempted type and label waiver",
            )
        ],
    )
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    path.write_text(yaml.safe_dump(record))
    write_snapshot(tmp_path, snapshot)
    errors = identifier_errors(tmp_path)
    if (section, category) == ("participants", "gene"):
        assert errors == []
        record["participants"][0]["label"] = "source_alias"
        path.write_text(yaml.safe_dump(record))
        assert any("LABEL_MISMATCH" in x for x in identifier_errors(tmp_path))
    else:
        assert any("ENTITY_TYPE_MISMATCH" in x for x in errors)


@pytest.mark.parametrize(
    "problem", ["hash", "wrong-kind", "projection", "missing-sequence", "path"]
)
def test_failed_pseudogene_build_never_replaces_output(tmp_path, monkeypatch, problem):
    manifest, records, entries, _, _ = fixture(tmp_path)
    if problem == "hash":
        entries[0]["sha256"] = "0" * 64
    elif problem == "wrong-kind":
        entries[0]["kind"] = GENE_KIND
    elif problem == "projection":
        entries[0]["native_gene"] = {"id": IDENTIFIER}
    elif problem == "path":
        entries[0]["path"] = "../gene.txt"
    else:
        entries[0] = entry(tmp_path, BODY.replace("NTSEQ       3\n            ccg\n", ""))
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "output.json"
    output.write_bytes(b"previous reviewed snapshot\n")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "builder",
            "--manifest",
            str(manifest),
            "--records",
            str(records),
            "--cache-dir",
            str(tmp_path),
            "--output",
            str(output),
        ],
    )
    with pytest.raises(ValueError):
        builder.main()
    assert output.read_bytes() == b"previous reviewed snapshot\n"


def test_default_cds_name_remains_annotation_not_an_implicit_profile_selector():
    body = CDS.replace("hypothetical protein", "pseudogene")
    assert project(body.encode(), URL)["native_type"] == "CDS"
    with pytest.raises(ValueError):
        project_pseudogene(body.encode(), URL)
