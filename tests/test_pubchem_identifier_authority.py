"""Native single-CID identity fixtures; production originals are verified externally."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

from pathwaymech.identifiers import identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, main, source_terms

KIND = "pubchem-compound-property-json"
URL = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/78645/"
       "property/Title,IUPACName,MolecularFormula,InChIKey/JSON")
COMPOUND = {"CID": 78645, "Title": "2-Hydrazinopyridine", "IUPACName": "pyridin-2-ylhydrazine",
            "MolecularFormula": "C5H7N3", "InChIKey": "NWELCUKYUCBVKK-UHFFFAOYSA-N"}
BODY = {"PropertyTable": {"Properties": [COMPOUND]}}


def parse(tmp_path, body=BODY, *, url=URL):
    raw = body if isinstance(body, bytes) else json.dumps(body).encode()
    path = tmp_path / "native.json"
    path.write_bytes(raw)
    terms = list(source_terms(KIND, path, url=url))
    assert path.read_bytes() == raw
    return terms


def test_native_title_only_no_iupac_or_synonym_promotion(tmp_path):
    assert parse(tmp_path) == [("PubChem:78645", "2-Hydrazinopyridine", [])]


@pytest.mark.parametrize("url", [
    URL.replace("https:", "http:"), URL.replace("pubchem.ncbi.nlm.nih.gov", "example.org"),
    URL.replace("pubchem.ncbi.nlm.nih.gov", "pubchem.ncbi.nlm.nih.gov.example.org"),
    URL.replace("pubchem.ncbi.nlm.nih.gov", "user@pubchem.ncbi.nlm.nih.gov"),
    URL.replace("pubchem.ncbi.nlm.nih.gov", "pubchem.ncbi.nlm.nih.gov:443"),
    URL + "?cid=78645", URL + "#fragment", URL + "/", URL + " ", URL + "\n",
    URL.replace("78645", "78646"), URL.replace("78645", "078645"),
    URL.replace("78645", "78645,78646"), URL.replace("78645", "0"),
    URL.replace("78645", "-1"), URL.replace("78645", "%3778645"),
    URL.replace("cid/78645", "name/2-Hydrazinopyridine"),
    URL.replace("compound", "substance"), URL.replace("/JSON", "/XML"),
    URL.replace("Title,IUPACName,MolecularFormula,InChIKey", "Title"),
    URL.replace("Title,IUPACName", "IUPACName,Title"), "",
])
def test_official_single_cid_request_and_native_identity_must_agree(tmp_path, url):
    with pytest.raises(ValueError, match="PubChem"):
        parse(tmp_path, url=url)


@pytest.mark.parametrize("body", [
    b"<html>error</html>", b"{}", b"null", b"[]", b'{"Fault":{"Code":"PUGREST.NotFound"}}',
    b'{"PropertyTable":{"Properties":[],"Properties":[]}}',
    b'{"PropertyTable":{"Properties":[{"CID":78645,"CID":78646}]}}',
    b'{"PropertyTable":{"Properties":[{"Title":"a","Title":"b"}]}}',
    b'{"extra":{"nested":1,"nested":1}}', b'{"value":NaN}',
    b'{"value":Infinity}', b'{"value":-Infinity}', b'{"value":1e999}',
    b'{"Title":"\xff"}', json.dumps(BODY).encode("utf-16"),
    json.dumps(BODY).encode("utf-8-sig"),
])
def test_malformed_ambiguous_nonfinite_or_non_utf8_source_fails(tmp_path, body):
    with pytest.raises(ValueError, match="PubChem"):
        parse(tmp_path, body)


@pytest.mark.parametrize("body", [
    {"PropertyTable": []}, {"PropertyTable": {}},
    {"PropertyTable": {"Properties": {}}}, {"PropertyTable": {"Properties": []}},
    {"PropertyTable": {"Properties": [COMPOUND, COMPOUND]}},
    {"PropertyTable": {"Properties": [None]}}, {"PropertyTable": {"Properties": ["78645"]}},
    {"PropertyTable": {"Properties": [COMPOUND], "extra": 1}},
    {"PropertyTable": {"Properties": [COMPOUND]}, "Fault": "mixed source"},
])
def test_exact_native_single_property_object_required(tmp_path, body):
    with pytest.raises(ValueError, match="PubChem"):
        parse(tmp_path, body)


@pytest.mark.parametrize("field,value", [
    ("CID", None), ("CID", True), ("CID", 78645.0), ("CID", "78645"),
    ("CID", 0), ("CID", -1), ("CID", 78646), ("CID", [78645]),
    ("Title", ""), ("Title", " \t"), ("Title", None), ("Title", []),
    ("Title", "bad\x00title"), ("Title", "bad\ntitle"), ("Title", "bad\ud800title"),
    ("Title", "bad\x7ftitle"), ("Title", "bad\x85title"),
    ("IUPACName", ""), ("MolecularFormula", None), ("InChIKey", ""),
    ("InChIKey", "NWELCUKYUCBVKK-UHFFFAOYSA"), ("InChIKey", "not-an-inchikey"),
])
def test_invalid_cid_and_native_properties_fail(tmp_path, field, value):
    body = copy.deepcopy(BODY)
    body["PropertyTable"]["Properties"][0][field] = value
    with pytest.raises(ValueError, match="PubChem"):
        parse(tmp_path, body)


@pytest.mark.parametrize("field", COMPOUND)
def test_missing_requested_property_fails(tmp_path, field):
    body = copy.deepcopy(BODY)
    del body["PropertyTable"]["Properties"][0][field]
    with pytest.raises(ValueError, match="PubChem"):
        parse(tmp_path, body)


def test_separately_returned_synonyms_do_not_supply_property_title(tmp_path):
    synonyms = {"InformationList": {"Information": [
        {"CID": 78645, "Synonym": ["2-Hydrazinopyridine", "Vendor material, 97%"]},
    ]}}
    with pytest.raises(ValueError, match="PubChem"):
        parse(tmp_path, synonyms)


def fixture(tmp_path):
    source = tmp_path / "compound.json"
    source.write_text(json.dumps(BODY))
    entries = [{"key": "native", "kind": KIND, "path": source.name, "url": URL,
                "version": "PubChem PUG REST CID 78645 property snapshot retrieved 2026-10-12",
                "license": "Synthetic fixture", "sha256": hashlib.sha256(
                    source.read_bytes()).hexdigest()}]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    record = {"id": "PubChem:78645", "label": "2-Hydrazinopyridine", "taxa": [],
              "participants": [], "reactions": []}
    path = records / "fixture.yaml"
    path.write_text(yaml.safe_dump(record))
    return manifest, records, entries, record, path


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("reverse", [True, False])
def test_conflicting_native_titles_fail_before_selection(tmp_path, selected, reverse):
    manifest, records, entries, record, path = fixture(tmp_path)
    second = tmp_path / "second.json"
    second.write_text(json.dumps({"PropertyTable": {"Properties": [
        {**COMPOUND, "Title": "Conflicting native title"},
    ]}}))
    entries.append({**entries[0], "key": "second", "path": second.name,
                    "sha256": hashlib.sha256(second.read_bytes()).hexdigest()})
    manifest.write_text(json.dumps(entries[::-1] if reverse else entries))
    if not selected:
        record["id"] = "PubChem:999"
        path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="conflicting PubChem native names"):
        build_snapshot(manifest, records, tmp_path)


def test_agreeing_duplicate_sources_keep_first_native_provenance(tmp_path):
    manifest, records, entries, _, _ = fixture(tmp_path)
    entries.append({**entries[0], "key": "second"})
    manifest.write_text(json.dumps(entries))
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"] == {"PubChem:78645": {
        "label": "2-Hydrazinopyridine", "synonyms": [], "source": "native",
    }}
    assert set(result["sources"]) == {"native"}


@pytest.mark.parametrize("existing", [True, False])
@pytest.mark.parametrize("problem", ["hash", "missing-id", "wrong-cid", "wrong-url", "conflict"])
def test_source_failure_cannot_create_or_replace_authority(
    tmp_path, monkeypatch, existing, problem,
):
    manifest, records, entries, record, path = fixture(tmp_path)
    if problem == "hash":
        entries[0]["sha256"] = "0" * 64
    elif problem == "missing-id":
        record["participants"] = [{"id": "PubChem:999", "label": "Plausible missing label"}]
        path.write_text(yaml.safe_dump(record))
    elif problem == "wrong-cid":
        entries[0]["url"] = URL.replace("78645", "78646")
    elif problem == "wrong-url":
        entries[0]["url"] = URL.replace("https:", "http:")
    else:
        second = tmp_path / "second.json"
        second.write_text(json.dumps({"PropertyTable": {"Properties": [
            {**COMPOUND, "Title": "Conflicting native title"},
        ]}}))
        entries.append({**entries[0], "key": "second", "path": second.name,
                        "sha256": hashlib.sha256(second.read_bytes()).hexdigest()})
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "authority.json"
    if existing:
        output.write_bytes(b"previous reviewed snapshot\n")
    monkeypatch.setattr(sys, "argv", [
        "builder", "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(tmp_path), "--output", str(output),
    ])
    with pytest.raises(ValueError):
        main()
    assert (output.read_bytes() == b"previous reviewed snapshot\n"
            if existing else not output.exists())


@pytest.mark.parametrize("problem,code", [
    (None, None), ("wrong-label", "LABEL_MISMATCH"), ("iupac", "LABEL_MISMATCH"),
    ("missing", "ID_NOT_FOUND"), ("empty-authority", "contains no identifiers"),
])
def test_pubchem_canonical_policy_has_no_contextual_or_empty_authority_waiver(
    tmp_path, problem, code,
):
    manifest, records, _, record, path = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    full_policy = yaml.safe_load(Path("conf/identifier_policy.yaml").read_text())
    assert full_policy["namespaces"]["PubChem"]["policy"] == "canonical"
    assert not any(rule["namespace"] == "PubChem" for rule in full_policy["contextual_labels"])
    policy = {"version": 1, "namespaces": {"PubChem": full_policy["namespaces"]["PubChem"]},
              "contextual_labels": []}
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data/identifier_authorities/sources.json"
    authority.parent.mkdir()
    if problem == "wrong-label":
        record["label"] = "Plausible compound name"
    elif problem == "iupac":
        record["label"] = COMPOUND["IUPACName"]
    elif problem == "missing":
        record["id"] = "PubChem:999"
    elif problem == "empty-authority":
        snapshot["terms"] = {"CHEBI:1": {"label": "Other", "synonyms": [], "source": "native"}}
    path.write_text(yaml.safe_dump(record))
    authority.write_text(json.dumps(snapshot))
    errors = identifier_errors(tmp_path)
    assert any(code in error for error in errors) if code else errors == []
