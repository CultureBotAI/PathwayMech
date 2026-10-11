"""Synthetic byte fixtures exercise encoding; original bodies remain external."""

from __future__ import annotations

import hashlib
import json
import sys

import pytest

from scripts.build_source_identifier_snapshot import build_snapshot, main, source_terms

NATIVE = (
    b"<TITLE>MetaCyc a native carrier</TITLE>"
    b"<script>var typeObjectPage = {object:'TEST-CARRIER',orgid:'META',"
    b"type:'Compounds'}</script>"
)


def parse(tmp_path, body):
    path = tmp_path / "native.html"
    path.write_bytes(body)
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    terms = list(source_terms("metacyc-html", path))
    assert hashlib.sha256(path.read_bytes()).hexdigest() == before
    return terms


def test_invalid_bytes_outside_identity_are_losslessly_preserved(tmp_path):
    body = NATIVE + b"<p>3\x963.5 kbp of unrelated sequence</p>\r\n"
    assert body.decode("utf-8", errors="surrogateescape").encode("utf-8", "surrogateescape") == body
    assert parse(tmp_path, body) == [("MetaCyc:TEST-CARRIER", "a native carrier", [])]
    assert (tmp_path / "native.html").read_bytes() == body


def test_valid_utf8_and_native_markup_are_preserved(tmp_path):
    body = NATIVE.replace(b"a native carrier", "a β-<i>D</i>-carrier &amp; cofactor".encode())
    assert parse(tmp_path, body) == [("MetaCyc:TEST-CARRIER", "a β-D-carrier & cofactor", [])]


@pytest.mark.parametrize(
    "metadata",
    [
        b"type:'Com}pounds'",
        b'type:"Com}pounds"',
        br"type:'Com\'}pounds'",
        br'type:"Com\"}pounds"',
        br"type:'tail\\',extra:'}'",
        b"type:'Compounds',extra:{hint:'}'}",
    ],
)
def test_quoted_braces_and_escapes_do_not_end_metadata(tmp_path, metadata):
    body = NATIVE.replace(b"type:'Compounds'", metadata)
    assert parse(tmp_path, body + b"<p>unrelated\xffprose</p>") == [
        ("MetaCyc:TEST-CARRIER", "a native carrier", [])
    ]
    # An invalid byte after a quoted brace remains inside the guarded object.
    bad = body.replace(b"}</script>", b",note:'bad\xff'}</script>")
    with pytest.raises(ValueError, match="undecodable bytes"):
        parse(tmp_path, bad)


@pytest.mark.parametrize(
    "metadata",
    [
        b"type:'Com}pound\xffs'",
        b'type:"Com}pound\xffs"',
        b"type:'Compounds'/* } */ ,note:'bad\xff'",
        b"type:`Com}pounds`,note:'bad\xff'",
        b"type:/}/,note:'bad\xff'",
    ],
)
def test_metadata_extent_cannot_hide_invalid_fields(tmp_path, metadata):
    with pytest.raises(ValueError, match="MetaCyc"):
        parse(tmp_path, NATIVE.replace(b"type:'Compounds'", metadata))


@pytest.mark.parametrize(
    "ending",
    [b"</script>", b",note:'unterminated}</script>", b",extra:{x:1}</script>"],
)
def test_unfinished_metadata_is_rejected(tmp_path, ending):
    with pytest.raises(ValueError, match="MetaCyc"):
        parse(tmp_path, NATIVE.replace(b"}</script>", ending))


@pytest.mark.parametrize(
    "body",
    [
        NATIVE.replace(b"native carrier", b"native\x96carrier"),
        NATIVE.replace(b"native carrier", b"native\xc3\x28carrier"),
        NATIVE.replace(b"native carrier", b"native\xffcarrier"),
        NATIVE.replace(b"a native carrier", b"a <i title='bad\x96'>native</i> carrier"),
        NATIVE.replace(b"TEST-CARRIER", b"TEST\x96CARRIER"),
        NATIVE.replace(b"META", b"ME\x96TA"),
        NATIVE.replace(b"Compounds", b"Compound\x96s"),
        NATIVE + b"<TITLE>MetaCyc bad\x96name</TITLE>",
        NATIVE + b"<script>typeObjectPage={object:'OTHER\x96ID',orgid:'META'}</script>",
        NATIVE.replace(b"TEST-CARRIER", b"TEST\x96CARRIER").replace(b"}</script>", b"</script>"),
        NATIVE.replace(b"Compounds", b"Compound\x96s").replace(b"}</script>", b"</script>"),
        NATIVE + b"<TITLE>MetaCyc bad\x96name",
        NATIVE + b"<TITLE title='bad\x96'>MetaCyc another native name</TITLE>",
    ],
)
def test_invalid_bytes_in_all_native_identity_or_title_surfaces_fail(tmp_path, body):
    with pytest.raises(ValueError, match="MetaCyc"):
        parse(tmp_path, body)


def test_other_source_decoders_are_not_relaxed(tmp_path):
    path = tmp_path / "uniprot.json"
    path.write_bytes(b'{"unrelated": "invalid\x96byte"}')
    with pytest.raises(UnicodeDecodeError):
        list(source_terms("uniprot", path))


def fixture(tmp_path):
    records = tmp_path / "records"
    records.mkdir()
    (records / "record.yaml").write_text("id: MetaCyc:TEST-CARRIER\nlabel: Selection only\n")
    source = tmp_path / "original.html"
    source.write_bytes(NATIVE + b"<p>3\x963.5 kbp</p>")
    entries = [
        {
            "key": "native",
            "kind": "metacyc-html",
            "path": source.name,
            "url": "https://example.org/native/TEST-CARRIER",
            "version": "synthetic fixture",
            "license": "synthetic fixture",
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        }
    ]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return source, entries, manifest, records


def test_authority_metadata_hashes_the_unchanged_original_bytes(tmp_path):
    source, entries, manifest, records = fixture(tmp_path)
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"] == {
        "MetaCyc:TEST-CARRIER": {"label": "a native carrier", "synonyms": [], "source": "native"}
    }
    assert result["sources"]["native"]["sha256"] == entries[0]["sha256"]
    assert source.read_bytes() == NATIVE + b"<p>3\x963.5 kbp</p>"
    source.write_bytes(source.read_bytes().replace(b"\x96", b"-"))
    with pytest.raises(ValueError, match="sha256"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("quoted_brace", [False, True])
def test_bad_identity_bytes_cannot_replace_prior_snapshot(tmp_path, monkeypatch, quoted_brace):
    source, entries, manifest, records = fixture(tmp_path)
    before, after = (
        (b"Compounds", b"Com}pound\xffs") if quoted_brace
        else (b"TEST-CARRIER", b"TEST\x96CARRIER")
    )
    source.write_bytes(source.read_bytes().replace(before, after))
    entries[0]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "authority.json"
    output.write_bytes(b"previous independent authority\n")
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
    with pytest.raises(ValueError, match="undecodable bytes"):
        main()
    assert output.read_bytes() == b"previous independent authority\n"
