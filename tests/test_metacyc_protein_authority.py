"""Native Protein XML is issuing evidence, never a source of nested aliases."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree

import pytest

from scripts.build_source_identifier_snapshot import build_snapshot, main, source_terms

URL = "https://example.org/getxml?id=META:CPLX-1"
NAME = "crotonyl-CoA carboxylase/reductase"
INVALID_NUMERIC_NAMES = [
    "protein &amp;#-1;",
    "protein &amp;amp;#946;",
    "protein &amp;#xFFFE;",
    "protein &amp;#xFFFF;",
]
NATIVE = f"""<?xml version="1.0" encoding="iso-8859-1"?>
<ptools-xml ptools-version="27.0" xml:base="http://example.org:443/getxml?META:CPLX-1">
<metadata><url>http://example.org:443/</url><service_name>getxml</service_name>
<query>META:CPLX-1</query><num_results>1</num_results>
<PGDB orgid="META" version="27.0"><species datatype="string">MetaCyc</species></PGDB>
</metadata><Protein ID="META:CPLX-1" orgid="META" frameid="CPLX-1" detail="full">
<parent><Protein resource="getxml?META:Protein-Complexes" orgid="META"
frameid="Protein-Complexes" class="true"/></parent>
<component><Protein resource="getxml?META:MONOMER-2" orgid="META" frameid="MONOMER-2"/>
<coefficient datatype="integer">2</coefficient></component>
<catalyzes><Enzymatic-Reaction><common-name>Not the protein name</common-name>
</Enzymatic-Reaction></catalyzes>
<credits><Person><common-name>Not a protein</common-name></Person></credits>
<species><Organism orgid="META" frameid="TAX-1063">
<common-name>Cereibacter sphaeroides</common-name></Organism></species>
<synonym datatype="string">Not an imported alias</synonym>
<common-name datatype="string">{NAME}</common-name></Protein></ptools-xml>
"""


def parse(tmp_path, body=NATIVE, *, url=URL, version="27.0"):
    path = tmp_path / "original.xml"
    raw = body.encode("iso-8859-1") if isinstance(body, str) else body
    path.write_bytes(raw)
    result = list(source_terms("metacyc-protein-xml", path, url=url, version=version))
    assert path.read_bytes() == raw
    return result


def test_only_direct_full_protein_has_native_canonical_authority(tmp_path):
    assert parse(tmp_path) == [("MetaCyc:CPLX-1", NAME, [])]


@pytest.mark.parametrize(
    ("native", "expected"),
    [
        ("L-malyl-CoA/&amp;beta;-methylmalyl-CoA lyase", "L-malyl-CoA/β-methylmalyl-CoA lyase"),
        (
            "(2&lt;i&gt;S&lt;/i&gt;)-methylsuccinyl-CoA dehydrogenase",
            "(2S)-methylsuccinyl-CoA dehydrogenase",
        ),
        (" café  protein ", "café protein"),
        ("protein &amp;#946;", "protein β"),
        ("protein &amp;#x3B2;", "protein β"),
    ],
)
def test_original_encoding_and_native_presentation_are_preserved(tmp_path, native, expected):
    assert parse(tmp_path, NATIVE.replace(NAME, native)) == [("MetaCyc:CPLX-1", expected, [])]


def test_native_database_version_is_not_software_version(tmp_path):
    body = NATIVE.replace('ptools-version="27.0"', 'ptools-version="28.1"')
    assert parse(tmp_path, body) == [("MetaCyc:CPLX-1", NAME, [])]
    with pytest.raises(ValueError, match="version mismatch"):
        parse(tmp_path, body, version="28.1")


@pytest.mark.parametrize(
    "mutation",
    [
        ("ptools-xml", "not-native"),
        ('ID="META:CPLX-1"', 'ID="ECOLI:CPLX-1"'),
        ('frameid="CPLX-1" detail', 'frameid="CPLX-9" detail'),
        ('ID="META:CPLX-1" orgid="META"', 'ID="META:CPLX-1" orgid="ECOLI"'),
        ('detail="full"', 'detail="low"'),
        ('detail="full"', 'detail="full" class="true"'),
        ('ID="META:CPLX-1"', 'resource="getxml?META:CPLX-1"'),
        ("<query>META:CPLX-1</query>", "<query>META:CPLX-9</query>"),
        ("<num_results>1</num_results>", "<num_results>2</num_results>"),
        ("<service_name>getxml</service_name>", "<service_name>login</service_name>"),
        ('<PGDB orgid="META"', '<PGDB orgid="ECOLI"'),
        ('version="27.0"><species', 'version="22.5"><species'),
        ('version="27.0"><species', "><species"),
        (">MetaCyc</species>", ">EcoCyc</species>"),
        ("<query>META:CPLX-1</query>", ""),
        ("<query>META:CPLX-1</query>", "<query>META:CPLX-1<x/></query>"),
        ("<url>http://example.org:443/</url>", "<url>http://other.org/</url>"),
        ("<url>http://example.org:443/</url>", "<url>http://example.org:invalid/</url>"),
        ("<url>http://example.org:443/</url>", "<url>http://example.org:99999/</url>"),
        ("getxml?META:CPLX-1", "getxml?META:CPLX-9"),
        ('xml:base="http://example.org:443/', 'xml:base="http://example.org:invalid/'),
        ('<common-name datatype="string">' + NAME + "</common-name>", ""),
        ('<common-name datatype="string">' + NAME, '<common-name datatype="list">' + NAME),
    ],
)
def test_wrong_or_incomplete_native_identity_fails(tmp_path, mutation):
    with pytest.raises(ValueError):
        parse(tmp_path, NATIVE.replace(*mutation))


@pytest.mark.parametrize("path", ["Protein", "metadata", "metadata/PGDB", "Protein/common-name"])
def test_duplicate_direct_identity_fields_fail_even_when_identical(tmp_path, path):
    root = ElementTree.fromstring(NATIVE.encode())
    parent_path, _, tag = path.rpartition("/")
    parent = root.find(parent_path) if parent_path else root
    node = parent.find(tag)
    parent.append(ElementTree.fromstring(ElementTree.tostring(node)))
    with pytest.raises(ValueError):
        parse(tmp_path, ElementTree.tostring(root))


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "CPLX-1",
        "META:CPLX-1",
        "MetaCyc:CPLX-1",
        "Error: object not found",
        "&lt;script&gt;forged&lt;/script&gt;",
        "&lt;i&gt;unfinished",
        "&lt;/i&gt;bad",
        "protein &amp;notknown;",
        "protein &amp;#0;",
        "protein &amp;#xD800;",
        "&lt;!-- hidden --&gt;protein",
        "&lt;!DOCTYPE fake&gt;protein",
        "&lt;?fake processing?&gt;protein",
        "&lt;i title='hidden'&gt;name&lt;/i&gt;",
        "&lt;![CDATA[hidden]]&gt;protein",
    ],
)
def test_unresolved_or_ambiguous_name_cannot_use_nested_fallback(tmp_path, name):
    with pytest.raises(ValueError):
        parse(tmp_path, NATIVE.replace(NAME, name))


@pytest.mark.parametrize(
    "name", [*INVALID_NUMERIC_NAMES, "protein &amp;#;", "protein &amp;#xZZ;", "protein &amp;#"]
)
def test_numeric_name_markup_and_invalid_decoded_xml_characters_fail(tmp_path, name):
    with pytest.raises(ValueError, match="resolved native common-name|invalid character reference"):
        parse(tmp_path, NATIVE.replace(NAME, name))


@pytest.mark.parametrize(
    "url",
    [
        None,
        "",
        "https://example.org/getxml?id=ECOLI:CPLX-1",
        "https://example.org/getxml?id=META:CPLX-9",
        URL + "&id=META:CPLX-1",
        URL + "&id=META:CPLX-9",
        URL + "&detail=low",
        URL + "&detail=full&detail=full",
        URL + "&other=1",
        URL + "#fragment",
        "https://other.org/getxml?id=META:CPLX-1",
        "https://user@example.org/getxml?id=META:CPLX-1",
        "file:///getxml?id=META:CPLX-1",
        "https://example.org/other?id=META:CPLX-1",
        "https://example.org/getxml?id=META:CPLX-1\n",
        "https://example.org:invalid/getxml?id=META:CPLX-1",
        "https://example.org:99999/getxml?id=META:CPLX-1",
        "https://example.org:0/getxml?id=META:CPLX-1",
    ],
)
def test_manifest_request_is_required_and_must_match_body(tmp_path, url):
    with pytest.raises(ValueError):
        parse(tmp_path, url=url)


def test_explicit_full_detail_and_percent_encoded_query_are_supported(tmp_path):
    assert parse(tmp_path, url=URL.replace("META:", "META%3A") + "&detail=full") == [
        ("MetaCyc:CPLX-1", NAME, []),
    ]


@pytest.mark.parametrize("version", [None, "", "22.5", "27.0 ", "MetaCyc27.0"])
def test_manifest_version_must_be_exact_native_pgdb_version(tmp_path, version):
    with pytest.raises(ValueError, match="version mismatch"):
        parse(tmp_path, version=version)


@pytest.mark.parametrize(
    "declaration",
    [
        '<!DOCTYPE ptools-xml [<!ENTITY fake "forged">]>',
        '<!DOCTYPE ptools-xml SYSTEM "file:///definitely-not-an-authority">',
        '<!DOCTYPE ptools-xml SYSTEM "https://example.invalid/not-an-authority">',
    ],
)
@pytest.mark.parametrize("encoding", ["utf-8", "utf-16"])
def test_dtd_is_rejected_before_entity_text_for_any_xml_encoding(tmp_path, declaration, encoding):
    body = NATIVE.replace('encoding="iso-8859-1"', f'encoding="{encoding}"')
    body = body.replace("<ptools-xml ", declaration + "<ptools-xml ", 1)
    with pytest.raises(ValueError, match="DOCTYPE"):
        parse(tmp_path, body.encode(encoding))


@pytest.mark.parametrize(
    "body",
    [
        "<html><title>Login</title><body>Not native</body></html>",
        '<script>window.location.replace("/gene?id=CPLX-1");</script>',
        '<!ENTITY fake "name"><ptools-xml/>',
        "<ptools-xml><Protein",
    ],
)
def test_error_redirect_and_malformed_bodies_fail(tmp_path, body):
    with pytest.raises((ValueError, ElementTree.ParseError)):
        parse(tmp_path, body)


def fixture(tmp_path: Path, *, selected=True):
    records = tmp_path / "records"
    records.mkdir()
    identifier = "MetaCyc:CPLX-1" if selected else "MetaCyc:CPLX-9"
    (records / "record.yaml").write_text(f"id: {identifier}\nlabel: curated invention\n")
    source = tmp_path / "original.xml"
    source.write_bytes(NATIVE.encode("iso-8859-1"))
    entries = [
        {
            "key": "native",
            "kind": "metacyc-protein-xml",
            "path": source.name,
            "url": URL,
            "version": "27.0",
            "license": "synthetic fixture",
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        }
    ]
    return records, entries, source


def build(tmp_path, records, entries):
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return build_snapshot(manifest, records, tmp_path)


def test_builder_uses_native_label_and_exact_source_bytes_version(tmp_path):
    records, entries, source = fixture(tmp_path)
    snapshot = build(tmp_path, records, entries)
    assert snapshot["terms"] == {
        "MetaCyc:CPLX-1": {"label": NAME, "synonyms": [], "source": "native"},
    }
    assert snapshot["sources"]["native"]["version"] == "27.0"
    assert (
        snapshot["sources"]["native"]["sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    )
    assert "curated invention" not in json.dumps(snapshot)


@pytest.mark.parametrize("other_kind", ["metacyc-protein-xml", "metacyc-html"])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_xml_involved_conflicting_labels_fail_in_both_orders_before_selection(
    tmp_path,
    other_kind,
    reverse,
    selected,
):
    records, entries, source = fixture(tmp_path, selected=selected)
    other = tmp_path / "other-source"
    if other_kind == "metacyc-protein-xml":
        other.write_text(NATIVE.replace(NAME, "conflicting native name"))
    else:
        other.write_text(
            "<TITLE>MetaCyc conflicting native name</TITLE>"
            "<script>typeObjectPage={object:'CPLX-1',orgid:'META'}</script>"
        )
    entries.append(
        {
            **entries[0],
            "key": "other",
            "kind": other_kind,
            "path": other.name,
            "sha256": hashlib.sha256(other.read_bytes()).hexdigest(),
        }
    )
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="conflicting MetaCyc protein native names"):
        build(tmp_path, records, entries)


def test_exact_xml_duplicate_does_not_import_new_aliases(tmp_path):
    records, entries, source = fixture(tmp_path)
    entries.append({**entries[0], "key": "second"})
    result = build(tmp_path, records, entries)
    assert result["terms"]["MetaCyc:CPLX-1"] == {
        "label": NAME,
        "synonyms": [],
        "source": "native",
    }


def test_adding_xml_preserves_existing_terms_and_provenance(tmp_path):
    records, entries, source = fixture(tmp_path)
    existing = tmp_path / "old.html"
    existing.write_text(
        "<TITLE>MetaCyc existing pathway</TITLE>"
        "<script>typeObjectPage={object:'PWY-1',orgid:'META'}</script>"
    )
    old = {
        **entries[0],
        "key": "prior",
        "kind": "metacyc-html",
        "path": existing.name,
        "version": "old native version",
        "url": "https://example.org/META/NEW-IMAGE?object=PWY-1",
        "sha256": hashlib.sha256(existing.read_bytes()).hexdigest(),
    }
    record = records / "record.yaml"
    record.write_text("id: MetaCyc:PWY-1\nlabel: existing pathway\n")
    baseline = build(tmp_path, records, [old])
    record.write_text(record.read_text() + "participants:\n- id: MetaCyc:CPLX-1\n")
    expanded = build(tmp_path, records, [old, *entries])
    assert expanded["terms"]["MetaCyc:PWY-1"] == baseline["terms"]["MetaCyc:PWY-1"]
    assert expanded["sources"]["prior"] == baseline["sources"]["prior"]
    assert set(expanded["terms"]) == {"MetaCyc:PWY-1", "MetaCyc:CPLX-1"}
    assert hashlib.sha256(source.read_bytes()).hexdigest() == entries[0]["sha256"]


def test_existing_html_only_precedence_is_unchanged(tmp_path):
    records, entries, source = fixture(tmp_path)
    for key, name in [("first", "name one"), ("second", "name two")]:
        html = tmp_path / (key + ".html")
        html.write_text(
            f"<TITLE>MetaCyc {name}</TITLE>"
            "<script>typeObjectPage={object:'CPLX-1',orgid:'META'}</script>"
        )
        entries.append(
            {
                **entries[0],
                "key": key,
                "kind": "metacyc-html",
                "path": html.name,
                "sha256": hashlib.sha256(html.read_bytes()).hexdigest(),
            }
        )
    result = build(tmp_path, records, entries[1:])
    assert result["terms"]["MetaCyc:CPLX-1"]["label"] == "name one"
    assert result["terms"]["MetaCyc:CPLX-1"]["synonyms"] == []


@pytest.mark.parametrize("problem", ["hash", "version", "request", "later-invalid", "missing-id"])
@pytest.mark.parametrize("existing_output", [False, True])
def test_failed_build_preserves_output(tmp_path, monkeypatch, problem, existing_output):
    records, entries, source = fixture(tmp_path, selected=problem != "missing-id")
    if problem == "hash":
        source.write_text(NATIVE.replace(NAME, "modified body"))
    elif problem == "version":
        entries[0]["version"] = "22.5"
    elif problem == "request":
        entries[0]["url"] = URL.replace("CPLX-1", "CPLX-9")
    elif problem == "later-invalid":
        bad = tmp_path / "bad.xml"
        bad.write_text(NATIVE.replace(NAME, ""))
        entries.append(
            {
                **entries[0],
                "key": "bad",
                "path": bad.name,
                "sha256": hashlib.sha256(bad.read_bytes()).hexdigest(),
            }
        )
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "authority.json"
    sentinel = b"previous authority\n"
    if existing_output:
        output.write_bytes(sentinel)
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
        main()
    if existing_output:
        assert output.read_bytes() == sentinel
    else:
        assert not output.exists()


@pytest.mark.parametrize("name", INVALID_NUMERIC_NAMES)
@pytest.mark.parametrize("existing_output", [False, True])
def test_invalid_numeric_name_cli_preserves_or_does_not_create_output(
    tmp_path, name, existing_output
):
    records, entries, source = fixture(tmp_path)
    source.write_bytes(NATIVE.replace(NAME, name).encode("iso-8859-1"))
    entries[0]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "authority.json"
    sentinel = b"reviewed prior authority\n"
    if existing_output:
        output.write_bytes(sentinel)
    builder = Path(__file__).resolve().parents[1] / "scripts/build_source_identifier_snapshot.py"
    result = subprocess.run(
        [
            sys.executable,
            "-B",
            str(builder),
            "--manifest",
            str(manifest),
            "--cache-dir",
            str(tmp_path),
            "--records",
            str(records),
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert "resolved native common-name" in result.stderr or "invalid character reference" in (
        result.stderr
    )
    assert "Retained" not in result.stdout
    if existing_output:
        assert output.read_bytes() == sentinel
    else:
        assert not output.exists()
