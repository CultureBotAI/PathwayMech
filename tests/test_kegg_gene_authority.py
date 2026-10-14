"""Adversarial synthetic CDS fixtures; real issuing-source replay stays external."""

from __future__ import annotations

import hashlib
import json
import sys

import pytest
import yaml

from pathwaymech.identifiers import _load_authority, identifier_errors
from pathwaymech.kegg_gene import (
    GENE_KIND,
    gene_metadata,
    gene_term,
    project,
    validate_gene_assertions,
    validate_gene_metadata,
)
from scripts import build_source_identifier_snapshot as builder

URL = "https://rest.kegg.jp/get/cgt:test_locus"
IDENTIFIER = "KEGG:cgt:test_locus"
BODY = (
    "ENTRY       test_locus       CDS       T00501\n"
    "NAME        (GenBank) hypothetical protein\n"
    "ORGANISM    cgt  Corynebacterium glutamicum R\n"
    "POSITION    100..108\n"
    "DBLINKS     NCBI-ProteinID: TEST00001\n"
    "            UniProt: TEST01\n"
    "REFERENCE   PMID:1\n"
    "  AUTHORS   Example A\n"
    "  TITLE     Source context, not a gene name\n"
    "            continued title\n"
    "AASEQ       2\n"
    "            MK\n"
    "NTSEQ       9\n"
    "            atgaaataa\n"
    "///\n"
)


def entry(tmp_path, body=BODY, *, key="gene", url=URL, version="synthetic observation"):
    path = tmp_path / (key + ".txt")
    path.write_bytes(body.encode() if isinstance(body, str) else body)
    return {
        "key": key,
        "kind": GENE_KIND,
        "path": path.name,
        "url": url,
        "version": version,
        "license": "Synthetic test fixture",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def metadata(tmp_path, body=BODY):
    return gene_metadata(entry(tmp_path, body), tmp_path)


def fixture(tmp_path):
    entries = [entry(tmp_path)]
    module = tmp_path / "module.txt"
    module.write_text("ENTRY       M99999  Pathway Module\nNAME        Test module\n///\n")
    entries.append(
        {
            "key": "module",
            "kind": "kegg-module-flatfile",
            "path": module.name,
            "url": "https://rest.kegg.jp/get/M99999",
            "version": "synthetic observation",
            "license": "Synthetic fixture",
            "sha256": hashlib.sha256(module.read_bytes()).hexdigest(),
        }
    )
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    record = {
        "id": "KEGG:M99999",
        "label": "Test module",
        "taxa": [],
        "reactions": [],
        "participants": [{"id": IDENTIFIER, "label": "test_locus", "category": "gene"}],
    }
    path = records / "record.yaml"
    path.write_text(yaml.safe_dump(record))
    return manifest, records, entries, record, path


def write_snapshot(tmp_path, snapshot):
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(snapshot))
    return path


def test_whole_native_record_preserved_without_manufactured_gene_alias(tmp_path):
    meta = metadata(tmp_path)
    native = meta["native_gene"]
    assert native["original_text"].encode() == BODY.encode()
    assert native["genome_id"] == "T00501"
    assert native["organism_code"] == "cgt"
    assert native["aaseq"] == {"length": 2, "sequence": "MK"}
    assert native["ntseq"] == {"length": 9, "sequence": "atgaaataa"}
    assert native["name_annotation"] == ["(GenBank) hypothetical protein"]
    assert (
        "".join(line + "\n" for field in native["fields"] for line in field["lines"]) + "///\n"
        == BODY
    )
    assert gene_term(meta, "gene") == (
        IDENTIFIER,
        {
            "label": "test_locus",
            "synonyms": [],
            "source": "gene",
            "entity_type": "native_gene",
            "label_kind": "canonical",
        },
    )
    assert list(builder.source_terms(GENE_KIND, tmp_path / "gene.txt", url=URL)) == [
        (IDENTIFIER, "test_locus", []),
    ]


def test_complement_position_and_annotation_continuation_are_preserved():
    body = BODY.replace("100..108", "complement(100..108)").replace(
        "NAME        (GenBank) hypothetical protein",
        "NAME        (GenBank) hypothetical\n            protein",
    )
    native = project(body.encode(), URL)
    assert native["position"] == {
        "native": "complement(100..108)",
        "start": 100,
        "end": 108,
        "strand": "-",
    }
    assert native["name_annotation"] == ["(GenBank) hypothetical", "protein"]


@pytest.mark.parametrize(
    "url",
    [
        "",
        URL.replace("https:", "http:"),
        URL.replace("rest.kegg.jp", "example.org"),
        URL.replace("rest.kegg.jp", "rest.kegg.jp.example.org"),
        URL.replace("rest.kegg.jp", "user@rest.kegg.jp"),
        URL.replace("rest.kegg.jp", "rest.kegg.jp:443"),
        URL + "/",
        URL + "?x=1",
        URL + "#x",
        URL + "\n",
        URL + " ",
        URL + "+cgt:other",
        URL + "/aaseq",
        URL.replace("cgt:", "Cgt:"),
        URL.replace("cgt:", "eco:"),
        URL.replace("test_locus", "other"),
        URL.replace(":", "%3A", 2),
        "https://rest.kegg.jp/get/M99999",
        "https://rest.kegg.jp/get/genes:cgt:test_locus",
    ],
)
def test_request_identity_and_options_fail_closed(url):
    with pytest.raises(ValueError, match="KEGG gene"):
        project(BODY.encode(), url)


@pytest.mark.parametrize(
    "body",
    [
        "",
        "<html>not found</html>",
        BODY.replace("///\n", ""),
        BODY + "\n",
        BODY + "trailing error\n",
        BODY + BODY,
        BODY + "///\n",
        "\n" + BODY,
        BODY.replace("ENTRY       ", "ENTRY\t"),
        BODY.replace("NAME        ", " NAME       "),
        BODY.replace("NAME        ", "name        "),
        BODY.replace("NAME        ", "NAME       "),
        BODY.replace("AASEQ       2", "AASEQ       2\nNAME        duplicate"),
        BODY.replace("test_locus       CDS", "wrong_locus      CDS"),
        BODY.replace("CDS", "RNA"),
        BODY.replace("T00501", "T00501 other"),
        BODY.replace("T00501", "t00501"),
        BODY.replace("T00501", "T501"),
        BODY.replace("cgt  Coryne", "eco  Coryne"),
        BODY.replace("T00501\n", "T00501\n            orphan ENTRY continuation\n"),
        BODY.replace("  TITLE", "  ENTRY"),
        BODY.replace("  TITLE", "  NAME "),
        BODY.replace("            MK", "            M*"),
        BODY.replace("            MK", "            M X"),
        BODY.replace("            MK", "            mk"),
        BODY.replace("AASEQ       2", "AASEQ       3"),
        BODY.replace("AASEQ       2", "AASEQ       02"),
        BODY.replace("AASEQ       2", "AASEQ       0"),
        BODY.replace("            MK", "            "),
        BODY.replace("NTSEQ       9", "NTSEQ       8"),
        BODY.replace("atgaaataa", "atgnaataa"),
        BODY.replace("atgaaataa", "atgaaatac"),
        BODY.replace("100..108", "100..109"),
        BODY.replace("100..108", "108..100"),
        BODY.replace("100..108", "0..8"),
        BODY.replace("100..108", "0100..108"),
        BODY.replace("100..108", "join(100..105,200..202)"),
        BODY.replace("100..108", "<100..108"),
        BODY.replace("100..108", "complement(100..108"),
        BODY.replace("100..108", "100..108)"),
        BODY.replace("100..108", "100"),
        BODY.replace("100..108", "chromosome:100..108"),
        BODY.replace("AASEQ       2\n            MK", "AASEQ       1\n            M"),
        BODY.replace("\n", "\r\n"),
        BODY.replace("hypothetical", "bad\x00annotation"),
        BODY.replace("hypothetical", "bad\x7fannotation"),
    ],
)
def test_malformed_mixed_duplicate_or_incomplete_native_cds_rejected(body):
    with pytest.raises(ValueError, match="KEGG gene"):
        project(body.encode(), URL)


@pytest.mark.parametrize("tag", ["ENTRY", "NAME", "ORGANISM", "POSITION", "AASEQ", "NTSEQ"])
def test_required_fields_cannot_be_missing_or_duplicated(tag):
    lines = BODY.splitlines(keepends=True)
    index = next(i for i, line in enumerate(lines) if line.startswith(tag + " "))
    for body in [
        "".join(lines[:index] + lines[index + 1 :]),
        "".join(lines[:index] + [lines[index]] + lines[index:]),
    ]:
        with pytest.raises(ValueError, match="KEGG gene"):
            project(body.encode(), URL)


@pytest.mark.parametrize(
    "raw", [BODY.encode("utf-16"), BODY.encode("utf-8-sig"), BODY.encode() + b"\xff"]
)
def test_original_encoding_is_not_reinterpreted(raw):
    with pytest.raises(ValueError, match="KEGG gene"):
        project(raw, URL)


def test_translation_is_explicitly_not_inferred_from_matching_length():
    # Validly shaped source with a disagreeing second codon stays inspectable;
    # whole protein/CDS equivalence is a separate issuing-source scientific audit.
    native = project(BODY.replace("atgaaataa", "atgcgataa").encode(), URL)
    assert native["aaseq"]["sequence"] == "MK"
    assert native["ntseq"]["sequence"] == "atgcgataa"


@pytest.mark.parametrize(
    "key",
    [
        "id",
        "native_type",
        "locus",
        "organism_code",
        "organism_name",
        "genome_id",
        "position",
        "aaseq",
        "ntseq",
        "fields",
        "original_text",
        "name_annotation",
    ],
)
def test_consumer_reconstructs_every_derived_field(tmp_path, key):
    for action in ["missing", "forged"]:
        meta = metadata(tmp_path)
        if action == "missing":
            del meta["native_gene"][key]
        else:
            meta["native_gene"][key] = "forged"
        with pytest.raises(ValueError, match="KEGG gene"):
            validate_gene_metadata(meta)


@pytest.mark.parametrize(
    "problem",
    [
        "extra-metadata",
        "extra-native",
        "empty-native",
        "wrong-kind",
        "missing-kind",
        "wrong-url",
        "wrong-hash",
        "missing-hash",
        "empty-version",
        "raw-edit",
        "raw-surrogate",
        "bool-position",
    ],
)
def test_consumer_refuses_partial_or_forged_typed_metadata(tmp_path, problem):
    meta = metadata(tmp_path)
    if problem == "extra-metadata":
        meta["allowed"] = True
    elif problem == "extra-native":
        meta["native_gene"]["allowed"] = True
    elif problem == "empty-native":
        meta["native_gene"] = {}
    elif problem == "wrong-kind":
        meta["kind"] = "kegg-module-flatfile"
    elif problem == "missing-kind":
        del meta["kind"]
    elif problem == "wrong-url":
        meta["url"] = URL.replace("test_locus", "other")
    elif problem == "wrong-hash":
        meta["sha256"] = "0" * 64
    elif problem == "missing-hash":
        del meta["sha256"]
    elif problem == "empty-version":
        meta["version"] = ""
    elif problem == "raw-edit":
        meta["native_gene"]["original_text"] = BODY.replace("hypothetical", "different")
    elif problem == "raw-surrogate":
        meta["native_gene"]["original_text"] = "\ud800"
    else:
        meta["native_gene"]["position"]["start"] = True
    with pytest.raises(ValueError, match="KEGG gene"):
        validate_gene_metadata(meta)


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize("change", ["name", "genome", "sequence", "position", "field", "version"])
def test_conflicts_checked_before_selection_for_every_whole_source(
    tmp_path, selected, reverse, change
):
    manifest, records, entries, record, path = fixture(tmp_path)
    body = {
        "name": BODY.replace("hypothetical", "different"),
        "genome": BODY.replace("T00501", "T00502"),
        "sequence": BODY.replace("atgaaataa", "atgcgataa"),
        "position": BODY.replace("100..108", "101..109"),
        "field": BODY.replace("TEST00001", "TEST00002"),
    }.get(change, BODY)
    entries.append(
        entry(
            tmp_path,
            body,
            key="second",
            version="different" if change == "version" else entries[0]["version"],
        )
    )
    manifest.write_text(json.dumps(entries[::-1] if reverse else entries))
    if not selected:
        record["participants"] = []
        path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="conflicting whole gene"):
        builder.build_snapshot(manifest, records, tmp_path)
    first = gene_metadata(entries[0], tmp_path)
    second = gene_metadata(entries[-1], tmp_path)
    sources = {"first": first, "second": second}
    with pytest.raises(ValueError, match="conflicting whole gene"):
        validate_gene_assertions(dict(reversed(list(sources.items()))) if reverse else sources)


def test_identical_whole_sources_keep_first_owner_and_old_module_behavior(tmp_path):
    manifest, records, entries, _, _ = fixture(tmp_path)
    entries.append({**entries[0], "key": "identical"})
    manifest.write_text(json.dumps(entries))
    result = builder.build_snapshot(manifest, records, tmp_path)
    assert result["terms"][IDENTIFIER] == gene_term(metadata(tmp_path), "gene")[1]
    assert result["terms"]["KEGG:M99999"] == {
        "label": "Test module",
        "synonyms": [],
        "source": "module",
    }
    assert set(result["sources"]) == {"gene", "module"}
    assert _load_authority(write_snapshot(tmp_path, result)) == result["terms"]


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("problem", ["wrong-kind", "wrong-type", "untyped-url", "untyped-id"])
def test_source_kind_and_identity_laundering_rejected(tmp_path, monkeypatch, selected, problem):
    manifest, records, entries, record, path = fixture(tmp_path)
    if not selected:
        record["participants"] = []
        path.write_text(yaml.safe_dump(record))
    if problem == "wrong-kind":
        entries[0]["kind"] = "kegg-module-flatfile"
    elif problem == "wrong-type":
        source = tmp_path / entries[0]["path"]
        source.write_text(BODY.replace("CDS", "RNA"))
        entries[0]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    elif problem == "untyped-url":
        entries[0]["kind"] = "uniprot"
    else:
        entries[0]["kind"] = "gocam-tar"
        entries[0]["url"] = "https://example.org/source"
        monkeypatch.setattr(builder, "source_terms", lambda *a, **kw: [(IDENTIFIER, "Fake", [])])
    manifest.write_text(json.dumps(entries))
    with pytest.raises(ValueError, match="KEGG gene"):
        builder.build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize(
    "problem",
    [
        "missing-kind",
        "missing-native",
        "wrong-type",
        "wrong-id",
        "extra-term",
        "wrong-label",
        "alias",
        "wrong-label-kind",
        "erased-owner",
        "untyped-owner",
    ],
)
def test_consumer_source_and_term_laundering_fails(tmp_path, problem):
    manifest, records, _, _, _ = fixture(tmp_path)
    snapshot = builder.build_snapshot(manifest, records, tmp_path)
    term = snapshot["terms"][IDENTIFIER]
    if problem == "missing-kind":
        del snapshot["sources"]["gene"]["kind"]
    elif problem == "missing-native":
        del snapshot["sources"]["gene"]["native_gene"]
    elif problem == "wrong-type":
        term["entity_type"] = "protein_complex"
    elif problem == "wrong-id":
        snapshot["terms"]["KEGG:cgt:other"] = snapshot["terms"].pop(IDENTIFIER)
    elif problem == "extra-term":
        term["allowed_categories"] = ["gene"]
    elif problem == "wrong-label":
        term["label"] = "ShiA"
    elif problem == "alias":
        term["synonyms"] = ["ShiA"]
    elif problem == "wrong-label-kind":
        term["label_kind"] = "source_context"
    elif problem == "erased-owner":
        snapshot["sources"]["gene"] = {
            k: v for k, v in snapshot["sources"]["gene"].items() if k not in {"kind", "native_gene"}
        }
        term.pop("entity_type")
    else:
        term["source"] = "module"
        term.pop("entity_type")
    with pytest.raises(ValueError):
        _load_authority(write_snapshot(tmp_path, snapshot))


def test_consumer_compares_unselected_source_owners(tmp_path):
    manifest, records, _, _, _ = fixture(tmp_path)
    snapshot = builder.build_snapshot(manifest, records, tmp_path)
    second = entry(tmp_path, BODY.replace("T00501", "T00502"), key="second")
    snapshot["sources"]["second"] = gene_metadata(second, tmp_path)
    with pytest.raises(ValueError, match="conflicting whole gene"):
        _load_authority(write_snapshot(tmp_path, snapshot))


@pytest.mark.parametrize(
    "section,category",
    [
        ("participants", None),
        ("participants", "protein"),
        ("participants", "complex"),
        ("participants", "molecular_activity"),
        ("reactions", "gene"),
        ("taxa", "gene"),
        ("record", None),
        ("participants", "gene"),
    ],
)
def test_gene_identity_requires_gene_participant_even_with_contextual_policy(
    tmp_path, section, category
):
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
    policy = {
        "version": 1,
        "namespaces": {"KEGG": {"snapshot": "snapshot.json", "policy": "canonical"}},
        "contextual_labels": [
            {
                "namespace": "KEGG",
                "sections": ["record", "taxa", "participants", "reactions"],
                "record_prefixes": ["KEGG"],
                "reason": "Synthetic attempted type waiver",
            }
        ],
    }
    conf = tmp_path / "conf"
    conf.mkdir()
    (conf / "identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    path.write_text(yaml.safe_dump(record))
    write_snapshot(tmp_path, snapshot)
    errors = identifier_errors(tmp_path)
    if (section, category) == ("participants", "gene"):
        assert errors == []
        record["participants"][0]["label"] = "ShiA"
        path.write_text(yaml.safe_dump(record))
        assert any("LABEL_MISMATCH" in x for x in identifier_errors(tmp_path))
    else:
        assert any("ENTITY_TYPE_MISMATCH" in x for x in errors), errors


@pytest.mark.parametrize("problem", ["hash", "path", "malformed", "missing-id", "projection"])
def test_failed_gene_build_cannot_replace_an_existing_snapshot(tmp_path, monkeypatch, problem):
    manifest, records, entries, record, path = fixture(tmp_path)
    if problem == "hash":
        entries[0]["sha256"] = "0" * 64
    elif problem == "path":
        entries[0]["path"] = "../gene.txt"
    elif problem == "malformed":
        entries[0] = entry(tmp_path, BODY + BODY)
    elif problem == "missing-id":
        record["participants"][0]["id"] = "KEGG:cgt:missing"
        path.write_text(yaml.safe_dump(record))
    else:
        entries[0]["native_gene"] = {"id": IDENTIFIER}
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "output.json"
    output.write_bytes(b"prior reviewed snapshot\n")
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
    assert output.read_bytes() == b"prior reviewed snapshot\n"
