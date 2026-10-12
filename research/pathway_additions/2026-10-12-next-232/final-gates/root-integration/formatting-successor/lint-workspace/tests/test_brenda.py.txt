"""Synthetic projections test provenance and prevent unsupported BRENDA joins."""

from __future__ import annotations

import copy
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import urlencode

import pytest

from pathwaymech.brenda import (
    BRENDA_ROLE_VARIABLES,
    brenda_role_query,
    brenda_seed_rows,
    load_brenda_role_bundle,
)

NATIVE = "https://purl.dsmz.de/brenda/"
SCHEMA = "https://purl.dsmz.de/schema/"
PATHWAY = NATIVE + "pathway/9876"
ENDPOINT = "https://sparql.dsmz.de/api/brenda"


def _uri(value):
    return {"type": "uri", "value": value}


def _row(reaction="S/123", role="substrate/42", compound="42", **optional):
    return {
        "reaction": _uri(NATIVE + "reaction/" + reaction),
        "role": _uri(NATIVE + role),
        "roleType": _uri(SCHEMA + ("Product" if role.startswith("product") else "Substrate")),
        "compound": _uri(NATIVE + "compound/" + compound),
        **optional,
    }


def _write(tmp_path, rows=None, limit=100, **overrides):
    result = {
        "head": {"vars": list(BRENDA_ROLE_VARIABLES)},
        "results": {"bindings": [_row()] if rows is None else rows},
    }
    result_bytes = json.dumps(result).encode()
    query = brenda_role_query(PATHWAY, limit)
    (tmp_path / "roles.json").write_bytes(result_bytes)
    (tmp_path / "roles.rq").write_text(query)
    manifest = {
        "format_version": 1,
        "pathway_uri": PATHWAY,
        "results_file": "roles.json",
        "query_file": "roles.rq",
        "results_sha256": hashlib.sha256(result_bytes).hexdigest(),
        "query_sha256": hashlib.sha256(query.encode()).hexdigest(),
        "source_url": ENDPOINT + "?" + urlencode({"query": query, "format": "json"}),
        "retrieved_at": "2026-10-08T03:00:00+00:00",
        "row_limit": limit,
        **overrides,
    }
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest))
    return path


def _mutate_manifest(path, **changes):
    manifest = json.loads(path.read_text())
    manifest.update(changes)
    path.write_text(json.dumps(manifest))


def _replace_results(path, payload):
    (path.parent / "roles.json").write_bytes(payload)
    _mutate_manifest(path, results_sha256=hashlib.sha256(payload).hexdigest())


def test_query_matches_existing_reviewed_canary():
    original = Path("research/source_discovery/2026-10-07-brenda-canary/roles.rq").read_bytes()
    assert brenda_role_query(NATIVE + "pathway/76", 1000).encode() == original


def test_preserves_bindings_reused_roles_and_literal_metadata(tmp_path):
    rows = [
        _row(name={"type": "literal", "value": 'A\tquoted\n"name"', "xml:lang": "en-GB"}),
        _row(reaction="I/456", name={"type": "literal", "value": ""}),
        _row(reaction="I/456", compound="43"),
        _row(
            reaction="I/456",
            compound="43",
            inchi={
                "type": "literal",
                "value": "example structure",
                "datatype": "urn:example:datatype",
            },
        ),
    ]
    path = _write(tmp_path, rows)
    bundle = load_brenda_role_bundle(path)
    assert bundle.bindings == tuple(rows)
    rendered = list(
        csv.DictReader(io.StringIO("\n".join(brenda_seed_rows(bundle))), delimiter="\t")
    )
    assert len(rendered) == 4
    assert [json.loads(row["raw_binding_json"]) for row in rendered] == rows
    assert {row["role_uri"] for row in rendered} == {NATIVE + "substrate/42"}
    assert [row["source_locator"] for row in rendered] == [
        f"results.bindings[{i}]" for i in range(4)
    ]
    assert {row["claim_type"] for row in rendered} == {"source_reported_reaction_role"}
    assert not {"taxon", "catalyst", "stoichiometry", "evidence", "direction"} & rendered[0].keys()
    assert (
        rendered[0]["results_sha256"]
        == hashlib.sha256((tmp_path / "roles.json").read_bytes()).hexdigest()
    )


def test_empty_projection_is_explicitly_preserved_as_no_rows(tmp_path):
    bundle = load_brenda_role_bundle(_write(tmp_path, []))
    assert bundle.bindings == ()
    assert len(list(brenda_seed_rows(bundle))) == 1


@pytest.mark.parametrize("count", [2, 3])
def test_rejects_possible_truncation_at_or_above_limit(tmp_path, count):
    path = _write(tmp_path, [_row(reaction=f"S/{i}") for i in range(count)], limit=2)
    with pytest.raises(ValueError, match="may be truncated"):
        load_brenda_role_bundle(path)


@pytest.mark.parametrize("kind", ["results", "query"])
def test_hashes_exact_bytes_before_parsing(tmp_path, kind):
    path = _write(tmp_path)
    artifact = tmp_path / ("roles.json" if kind == "results" else "roles.rq")
    with artifact.open("ab") as handle:
        handle.write(b" ")
    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        load_brenda_role_bundle(path)


def test_rejects_query_scope_mismatch_even_when_artifact_hashes_match(tmp_path):
    path = _write(tmp_path, pathway_uri=NATIVE + "pathway/999")
    with pytest.raises(ValueError, match="supported pathway scope"):
        load_brenda_role_bundle(path)


def test_rejects_other_query_with_correct_hash_and_matching_url(tmp_path):
    path = _write(tmp_path)
    query = brenda_role_query(PATHWAY, 100).replace("hasReaction", "hasEnzyme")
    (tmp_path / "roles.rq").write_text(query)
    _mutate_manifest(
        path,
        query_sha256=hashlib.sha256(query.encode()).hexdigest(),
        source_url=ENDPOINT + "?" + urlencode({"query": query, "format": "json"}),
    )
    with pytest.raises(ValueError, match="supported pathway scope"):
        load_brenda_role_bundle(path)


@pytest.mark.parametrize("url_query_newline", [True, False])
def test_url_may_omit_single_final_query_newline(tmp_path, url_query_newline):
    path = _write(tmp_path)
    query = brenda_role_query(PATHWAY, 100)
    if not url_query_newline:
        query = query.removesuffix("\n")
    _mutate_manifest(
        path, source_url=ENDPOINT + "?" + urlencode({"query": query, "format": "json"})
    )
    assert len(load_brenda_role_bundle(path).bindings) == 1


def test_query_file_may_omit_single_final_newline(tmp_path):
    path = _write(tmp_path)
    query = brenda_role_query(PATHWAY, 100).removesuffix("\n")
    (tmp_path / "roles.rq").write_text(query)
    _mutate_manifest(
        path,
        query_sha256=hashlib.sha256(query.encode()).hexdigest(),
        source_url=ENDPOINT + "?" + urlencode({"query": query, "format": "json"}),
    )
    assert load_brenda_role_bundle(path).query_sha256 == hashlib.sha256(query.encode()).hexdigest()


@pytest.mark.parametrize(
    "change",
    [
        lambda url: url.replace("sparql.dsmz.de", "example.org"),
        lambda url: url + "&query=other",
        lambda url: url + "&timeout=5",
        lambda url: url + "#fragment",
        lambda url: url.replace("format=json", "format=xml"),
        lambda url: url.replace("pathway%2F9876", "pathway%2F9999"),
        lambda url: url + "\n",
    ],
)
def test_source_url_must_describe_exact_official_query(tmp_path, change):
    path = _write(tmp_path)
    _mutate_manifest(path, source_url=change(json.loads(path.read_text())["source_url"]))
    with pytest.raises(ValueError, match="source_url"):
        load_brenda_role_bundle(path)


@pytest.mark.parametrize(
    "filename",
    ["../roles.json", "/tmp/roles.json", "a/roles.json", "..", "a\\roles.json", "", "x\x00"],
)
def test_rejects_nonlocal_artifact_paths(tmp_path, filename):
    path = _write(tmp_path, results_file=filename)
    with pytest.raises(ValueError, match="local basename"):
        load_brenda_role_bundle(path)


def test_rejects_symlink_escape(tmp_path):
    path = _write(tmp_path)
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "results.json").write_bytes((tmp_path / "roles.json").read_bytes())
    (tmp_path / "linked.json").symlink_to(outside / "results.json")
    _mutate_manifest(path, results_file="linked.json")
    with pytest.raises(ValueError, match="escapes"):
        load_brenda_role_bundle(path)


@pytest.mark.parametrize(
    "field,value,message",
    [
        ("row_limit", True, "row_limit"),
        ("row_limit", 0, "row_limit"),
        ("row_limit", 10001, "row_limit"),
        ("format_version", True, "format_version"),
        ("format_version", 2, "format_version"),
        ("retrieved_at", "2026-10-08", "timestamp"),
        ("retrieved_at", "2026-02-30T12:00:00Z", "timestamp"),
        ("pathway_uri", NATIVE + "pathway/1#other", "pathway_uri"),
        ("query_sha256", "z" * 64, "hexadecimal"),
    ],
)
def test_manifest_contract(tmp_path, field, value, message):
    path = _write(tmp_path, **{field: value})
    with pytest.raises(ValueError, match=message):
        load_brenda_role_bundle(path)


@pytest.mark.parametrize(
    "term",
    [
        None,
        {"type": "uri", "value": "x"},
        {"type": "literal", "value": None},
        {"type": "literal", "value": "x", "extra": "x"},
        {"type": "literal", "value": "x", "xml:lang": ""},
        {"type": "literal", "value": "x", "datatype": "relative"},
        {"type": "literal", "value": "x", "xml:lang": "en", "datatype": "urn:x"},
    ],
)
def test_optional_term_null_or_malformed_is_not_unbound(tmp_path, term):
    path = _write(tmp_path, [_row(name=term)])
    with pytest.raises(ValueError, match="binding 0"):
        load_brenda_role_bundle(path)


@pytest.mark.parametrize(
    "field,term",
    [
        ("reaction", {"type": "literal", "value": NATIVE + "reaction/S/123"}),
        ("reaction", _uri("https://example.org/reaction/S/123")),
        ("role", _uri(NATIVE + "product/42")),
        ("roleType", _uri(SCHEMA + "Catalyst")),
        ("compound", _uri(NATIVE + "compound/42?query=1")),
    ],
)
def test_native_uri_roles_and_types_are_checked(tmp_path, field, term):
    row = _row()
    row[field] = term
    with pytest.raises(ValueError, match="binding 0"):
        load_brenda_role_bundle(_write(tmp_path, [row]))


def test_late_bad_row_prevents_any_bundle_return(tmp_path):
    row = _row(reaction="I/124")
    row["organism"] = _uri(NATIVE + "organism/42")
    with pytest.raises(ValueError, match="binding 1"):
        load_brenda_role_bundle(_write(tmp_path, [_row(), row]))


def test_exact_duplicate_rows_are_rejected_but_distinct_metadata_is_preserved(tmp_path):
    row = _row()
    reordered = dict(reversed(list(copy.deepcopy(row).items())))
    with pytest.raises(ValueError, match="duplicate row"):
        load_brenda_role_bundle(_write(tmp_path, [row, reordered]))


@pytest.mark.parametrize(
    "payload,message",
    [
        (b'{"head": {}, "head": {}}', "duplicate JSON key"),
        (b'{"head": {"vars": NaN}}', "invalid JSON constant"),
        (b"[]", "JSON object"),
        (b"{}", "exactly head and results"),
        (b'{"error": "timeout"}', "exactly head and results"),
        (b'{"head": ', "malformed UTF-8 JSON"),
        (b"\xff", "malformed UTF-8 JSON"),
    ],
)
def test_rejects_invalid_results_even_when_hash_matches(tmp_path, payload, message):
    path = _write(tmp_path)
    _replace_results(path, payload)
    with pytest.raises(ValueError, match=message):
        load_brenda_role_bundle(path)


def test_rejects_duplicate_nested_term_keys(tmp_path):
    path = _write(tmp_path)
    payload = (
        (tmp_path / "roles.json")
        .read_bytes()
        .replace(b'"type": "uri"', b'"type": "uri", "type": "literal"', 1)
    )
    _replace_results(path, payload)
    with pytest.raises(ValueError, match="duplicate JSON key"):
        load_brenda_role_bundle(path)


def test_inchikey_requires_the_querys_inchi_binding(tmp_path):
    path = _write(tmp_path, [_row(inchikey={"type": "literal", "value": "opaque-key"})])
    with pytest.raises(ValueError, match="without inchi"):
        load_brenda_role_bundle(path)
