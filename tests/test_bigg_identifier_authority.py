"""Synthetic universal API fixtures; authentic originals are verified externally."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from pathwaymech.identifiers import identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, source_terms

MET_KIND = "bigg-universal-metabolite-json"
RXN_KIND = "bigg-universal-reaction-json"
URL = "https://bigg.ucsd.edu/api/v2/universal/metabolites/acmana"
VERSION_URL = "https://bigg.ucsd.edu/api/v2/database_version"
METABOLITE = {
    "bigg_id": "acmana", "name": "Native  metabolite name",
    "old_identifiers": ["acmana", "legacy_id"],
    "database_links": {"CHEBI": [{"id": "CHEBI:17122"}]},
    "compartments_in_models": [{"bigg_id": "c", "model_bigg_id": "model"}],
    "charges": [0], "formulae": ["C8H15NO6"],
}
REACTION = {
    "bigg_id": "ACMANAptspp", "name": "Native reaction name",
    "old_identifiers": ["ACMANAptspp"], "database_links": {},
    "models_containing_reaction": [{"bigg_id": "model"}],
    "metabolites": [{"bigg_id": "acmana", "stoichiometry": -1}],
    "reaction_string": "a &#8652; b", "pseudoreaction": False,
}
VERSION = {"api_version": "v2", "bigg_models_version": "1.6.0",
           "last_updated": "2019-10-31 10:05:54.157598"}


def write_json(path, value):
    path.write_text(json.dumps(value))
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse(tmp_path, body=METABOLITE, *, kind=MET_KIND, url=URL):
    path = tmp_path / "native.json"
    raw = body if isinstance(body, bytes) else json.dumps(body).encode()
    path.write_bytes(raw)
    result = list(source_terms(kind, path, url=url))
    assert path.read_bytes() == raw
    return result


@pytest.mark.parametrize("kind,body,url", [
    (MET_KIND, METABOLITE, URL),
    (RXN_KIND, REACTION, URL.replace("metabolites/acmana", "reactions/ACMANAptspp")),
])
def test_universal_native_name_only_without_cross_database_terms(tmp_path, kind, body, url):
    assert parse(tmp_path, body, kind=kind, url=url) == [
        ("BiGG:" + body["bigg_id"], body["name"], []),
    ]


@pytest.mark.parametrize("url", [
    URL.replace("https:", "http:"), URL.replace("bigg.ucsd.edu", "other.example"),
    URL.replace("bigg.ucsd.edu", "bigg.ucsd.edu.example.com"),
    URL.replace("bigg.ucsd.edu", "user@bigg.ucsd.edu"),
    URL.replace("bigg.ucsd.edu", "bigg.ucsd.edu:443"), URL + "?id=acmana",
    URL + "#fragment", URL + "/", URL + " ", URL.replace("api/v2", "api/v1"),
    URL.replace("universal", "models/iML1515"), URL.replace("metabolites", "reactions"),
    URL.replace("acmana", "acmanap"), URL.replace("acmana", "%61cmana"),
    URL.replace("acmana", "../acmana"), URL.replace("acmana", ""),
])
def test_exact_universal_request_required(tmp_path, url):
    with pytest.raises(ValueError, match="BiGG"):
        parse(tmp_path, url=url)


@pytest.mark.parametrize("body", [
    b"<html>not found</html>", b"{}", b"null", b"[]", b"[{},{}]",
    b'{"error":"missing"}', b'{"bigg_id":"acmana","bigg_id":"acmana"}',
    b'{"name":"one","name":"two"}', b'{"database_links":{"x":1,"x":2}}',
    b'{"value":NaN}', b'{"value":Infinity}', b'{"name":"\xff"}',
    json.dumps(METABOLITE).encode("utf-16"),
])
def test_nonunique_or_error_json_fails(tmp_path, body):
    with pytest.raises(ValueError, match="BiGG"):
        parse(tmp_path, body)


@pytest.mark.parametrize("field,value", [
    ("bigg_id", None), ("bigg_id", ""), ("bigg_id", ["acmana"]),
    ("bigg_id", "acmana_c"), ("name", None), ("name", []), ("name", ""),
    ("name", "  "), ("name", "unknown"), ("name", "acmana"),
    ("name", "<b>name</b>"), ("name", "bad\x00name"), ("name", "bad\nname"),
    ("old_identifiers", "acmana"), ("old_identifiers", [""]),
    ("database_links", []), ("charges", 0), ("formulae", "C8H15NO6"),
    ("compartments_in_models", {}),
])
def test_invalid_native_identity_name_or_shape_fails(tmp_path, field, value):
    body = {**METABOLITE, field: value}
    with pytest.raises(ValueError, match="BiGG"):
        parse(tmp_path, body)


@pytest.mark.parametrize("field", [
    "name", "bigg_id", "charges", "formulae", "compartments_in_models",
])
def test_missing_native_fields_fail(tmp_path, field):
    body = {k: v for k, v in METABOLITE.items() if k != field}
    with pytest.raises(ValueError, match="BiGG"):
        parse(tmp_path, body)


@pytest.mark.parametrize("kind,body", [(MET_KIND, REACTION), (RXN_KIND, METABOLITE)])
def test_endpoint_kind_cannot_relabel_other_native_object(tmp_path, kind, body):
    category = "metabolites" if kind == MET_KIND else "reactions"
    url = "https://bigg.ucsd.edu/api/v2/universal/" + category + "/" + body["bigg_id"]
    with pytest.raises(ValueError, match="BiGG"):
        parse(tmp_path, body, kind=kind, url=url)


@pytest.mark.parametrize("extra", ["error", "results", "lower_bound", "model_bigg_id"])
def test_error_and_model_fields_do_not_become_universal_authority(tmp_path, extra):
    with pytest.raises(ValueError, match="BiGG"):
        parse(tmp_path, {**METABOLITE, extra: "wrong object"})


@pytest.mark.parametrize("field,value", [
    ("pseudoreaction", 0), ("pseudoreaction", "false"), ("reaction_string", ""),
    ("reaction_string", []), ("metabolites", {}), ("models_containing_reaction", {}),
])
def test_reaction_shape_is_not_inferred_from_its_name(tmp_path, field, value):
    with pytest.raises(ValueError, match="BiGG"):
        parse(tmp_path, {**REACTION, field: value}, kind=RXN_KIND,
              url=URL.replace("metabolites/acmana", "reactions/ACMANAptspp"))


def fixture(tmp_path):
    version = tmp_path / "version.json"
    version_sha = write_json(version, VERSION)
    native = tmp_path / "native.json"
    body_sha = write_json(native, METABOLITE)
    entries = [{
        "key": "native", "kind": MET_KIND, "path": native.name, "url": URL,
        "sha256": body_sha, "version": "BiGG Models 1.6.0; retrieved 2026-10-11",
        "license": "Synthetic fixture", "version_source": {
            "path": version.name, "url": VERSION_URL, "sha256": version_sha,
        },
    }]
    manifest = tmp_path / "manifest.json"
    write_json(manifest, entries)
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    (records / "fixture.yaml").write_text(yaml.safe_dump({
        "id": "BiGG:acmana", "label": METABOLITE["name"],
        "taxa": [], "participants": [], "reactions": [],
    }))
    return manifest, records, entries


@pytest.mark.parametrize("problem", [
    "missing", "wrong-url", "query", "wrong-hash", "absolute", "traversal", "empty-path",
    "release", "date", "version-api", "version-release", "version-date", "version-error",
    "version-list", "version-duplicate", "version-date-only", "body-hash",
])
def test_manifest_requires_bound_native_version_before_selection(tmp_path, problem):
    manifest, records, entries = fixture(tmp_path)
    entry = entries[0]
    companion = entry["version_source"]
    if problem == "missing":
        del entry["version_source"]
    elif problem == "wrong-url":
        companion["url"] = VERSION_URL.replace("bigg.ucsd.edu", "example.org")
    elif problem == "query":
        companion["url"] += "?version=1.6.0"
    elif problem == "wrong-hash":
        companion["sha256"] = "0" * 64
    elif problem in {"absolute", "traversal", "empty-path"}:
        companion["path"] = {"absolute": "/tmp/version.json", "traversal": "../version.json",
                             "empty-path": ""}[problem]
    elif problem in {"release", "date"}:
        entry["version"] = entry["version"].replace(
            "1.6.0" if problem == "release" else "2026-10-11",
            "1.7.0" if problem == "release" else "2026-99-99",
        )
    elif problem == "body-hash":
        entry["sha256"] = "0" * 64
    else:
        body = copy.deepcopy(VERSION)
        if problem == "version-api":
            body["api_version"] = "v3"
        elif problem == "version-release":
            body["bigg_models_version"] = ["1.6.0"]
        elif problem == "version-date":
            body["last_updated"] = "not known"
        elif problem == "version-date-only":
            body["last_updated"] = "2019-10-31"
        elif problem == "version-error":
            body = {"error": "down"}
        elif problem == "version-list":
            body = [VERSION]
        path = tmp_path / companion["path"]
        if problem == "version-duplicate":
            path.write_bytes(b'{"api_version":"v2","api_version":"v2"}')
            companion["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        else:
            companion["sha256"] = write_json(path, body)
    write_json(manifest, entries)
    # Even an unused malformed source fails before the wanted-ID filter.
    (records / "fixture.yaml").write_text("id: GO:0000001\nlabel: Other selection\n")
    with pytest.raises(ValueError):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("mutation", ["label", "kind", "version", "update-observation"])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_native_conflicts_fail_in_both_orders_before_selection(
    tmp_path, mutation, reverse, selected,
):
    manifest, records, entries = fixture(tmp_path)
    other = copy.deepcopy(entries[0])
    other.update(key="other", path="other.json")
    body = copy.deepcopy(METABOLITE)
    if mutation == "label":
        body["name"] = "Another native name"
    elif mutation == "kind":
        body = {**REACTION, "bigg_id": "acmana", "name": METABOLITE["name"]}
        other.update(kind=RXN_KIND, url=URL.replace("metabolites", "reactions"))
    else:
        version = ({**VERSION, "bigg_models_version": "1.7.0"} if mutation == "version"
                   else {**VERSION, "last_updated": "2019-11-01 10:05:54.157598"})
        other["version_source"].update(path="new-version.json",
                                        sha256=write_json(tmp_path / "new-version.json", version))
        if mutation == "version":
            other["version"] = "BiGG Models 1.7.0; retrieved 2026-10-11"
    other["sha256"] = write_json(tmp_path / other["path"], body)
    entries.append(other)
    write_json(manifest, entries[::-1] if reverse else entries)
    if not selected:
        (records / "fixture.yaml").write_text("id: GO:0000001\nlabel: Other selection\n")
    with pytest.raises(ValueError, match="conflicting BiGG"):
        build_snapshot(manifest, records, tmp_path)


def test_native_label_policy_and_missing_id_gate(tmp_path):
    manifest, records, _ = fixture(tmp_path)
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"] == {"BiGG:acmana": {
        "label": METABOLITE["name"], "synonyms": [], "source": "native",
    }}
    policy = yaml.safe_load(Path("conf/identifier_policy.yaml").read_text())
    assert policy["namespaces"]["BiGG"]["policy"] == "canonical"
    assert not any(rule["namespace"] == "BiGG" for rule in policy["contextual_labels"])
    policy["namespaces"] = {"BiGG": policy["namespaces"]["BiGG"]}
    policy["contextual_labels"] = []
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    snapshot = tmp_path / "data/identifier_authorities/sources.json"
    snapshot.parent.mkdir()
    write_json(snapshot, result)
    assert identifier_errors(tmp_path) == []
    record = yaml.safe_load((records / "fixture.yaml").read_text())
    record["label"] = "Native metabolite name"
    (records / "fixture.yaml").write_text(yaml.safe_dump(record))
    assert identifier_errors(tmp_path) == []
    for label in ["Curator name", "legacy_id", "CHEBI:17122"]:
        record["label"] = label
        (records / "fixture.yaml").write_text(yaml.safe_dump(record))
        assert any("LABEL_MISMATCH" in e for e in identifier_errors(tmp_path))
    record.update(id="BiGG:missing", label="Unknown")
    (records / "fixture.yaml").write_text(yaml.safe_dump(record))
    assert any("ID_NOT_FOUND" in e for e in identifier_errors(tmp_path))
    record["participants"] = [{"id": "BiGG:acmana", "label": METABOLITE["name"]}]
    (records / "fixture.yaml").write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="unresolved source identifiers: BiGG:missing"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize("problem", ["wrong-id", "html", "version-hash"])
def test_real_cli_rejection_preserves_output(tmp_path, existing, problem):
    manifest, records, entries = fixture(tmp_path)
    if problem == "version-hash":
        entries[0]["version_source"]["sha256"] = "0" * 64
    else:
        body = (b"<html>service unavailable</html>" if problem == "html"
                else json.dumps({**METABOLITE, "bigg_id": "other"}).encode())
        (tmp_path / "native.json").write_bytes(body)
        entries[0]["sha256"] = hashlib.sha256(body).hexdigest()
    write_json(manifest, entries)
    output = tmp_path / "output.json"
    if existing:
        output.write_bytes(b"previous independent snapshot\n")
    result = subprocess.run([
        sys.executable, "-B", "scripts/build_source_identifier_snapshot.py",
        "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(tmp_path), "--output", str(output),
    ], capture_output=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    assert result.returncode != 0 and b"BiGG" in result.stderr
    assert (
        output.read_bytes() == b"previous independent snapshot\n"
        if existing else not output.exists()
    )
