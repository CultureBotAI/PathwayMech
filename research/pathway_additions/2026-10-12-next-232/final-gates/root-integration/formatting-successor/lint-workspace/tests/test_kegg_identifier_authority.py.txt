"""Synthetic parser fixtures are not production KEGG authority sources."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

from pathwaymech.identifiers import identifier_errors
from scripts.build_source_identifier_snapshot import (
    KEGG_SOURCE_TYPES,
    build_snapshot,
    kegg_terms,
    main,
    source_terms,
)


def native(identifier="M99999", name="Native cycle", entry_type="Pathway   Module"):
    return f"ENTRY       {identifier}            {entry_type}\nNAME        {name}\n///\n"


def parse(text, kind="kegg-module-flatfile", ids="M99999"):
    return kegg_terms(text, kind, "https://rest.kegg.jp/get/" + ids)


@pytest.mark.parametrize("kind,identifier,entry_type", [
    ("kegg-module-flatfile", "M99999", "Pathway   Module"),
    ("kegg-reaction-flatfile", "R99999", "Reaction"),
    ("kegg-compound-flatfile", "C99999", "Compound"),
])
def test_native_identity_name_and_class(kind, identifier, entry_type):
    assert parse(native(identifier, "Native name", entry_type), kind, identifier) == [
        ("KEGG:" + identifier, "Native name", []),
    ]


def test_continuations_native_synonyms_and_reference_subfields():
    text = (
        "ENTRY       C99999                      Compound\n"
        "NAME        Reduced test carrier;\n"
        "            Reduced test carrier [iron-sulfur] cluster\n"
        "REFERENCE   PMID:1\n"
        "  AUTHORS   Someone A\n"
        "  TITLE     This is not a compound name\n"
        "            Nor is this continuation\n"
        "///\n"
    )
    assert parse(text, "kegg-compound-flatfile", "C99999") == [
        ("KEGG:C99999", "Reduced test carrier", ["Reduced test carrier [iron-sulfur] cluster"]),
    ]


def test_wrapped_name_preserves_stereo_charge_and_punctuation():
    text = native(name="(S)-test:NADP+ oxidoreductase\n            (CoA-acylating);")
    assert parse(text)[0][1] == "(S)-test:NADP+ oxidoreductase (CoA-acylating)"


def test_batch_retains_original_entry_order_not_request_order():
    text = native() + "\n" + native("M99998", "Other cycle")
    assert [term[0] for term in parse(text, ids="M99998+M99999")] == [
        "KEGG:M99999", "KEGG:M99998",
    ]


@pytest.mark.parametrize("text", [
    "", "<html>temporary failure</html>", "ENTRY       M99999 Pathway Module\n///\n",
    native().replace("Native cycle", ""), native().replace("Native cycle", "M99999"),
    native().replace("Native cycle", "KEGG:M99999"),
    native().replace("Native cycle", "First;;Second"),
    native().replace("Native cycle", ";First"),
    native().replace("Native cycle", "First;;"),
    native().replace("M99999", "M9999"), native().replace("M99999", "m99999"),
    native().replace("M99999", "R99999"),
    native().replace("Pathway   Module", "Reaction"),
    native().replace("Pathway   Module", "Module"),
    native().replace("///\n", ""), native() + "trailing error\n",
    native() + "///\n", "            orphan\n" + native(),
    "NAME        orphan\n" + native(), native().replace("ENTRY       ", "ENTRY\t"),
    native().replace("NAME        ", "  NAME      "),
    native().replace("NAME        ", "name        "),
    native().replace("NAME        Native cycle", "NAME        First\nNAME        Second"),
    native().replace("///", "ENTRY       M99998 Pathway Module\n///"),
    native().replace("///", "REFERENCE   PMID:1\n  ENTRY     M99998 Pathway Module\n///"),
    native().replace("///", "REFERENCE   PMID:1\n  NAME      Concealed duplicate\n///"),
    native() + native(), native() + native("M99998").replace("///\n", ""),
])
def test_malformed_native_bodies_fail_closed(text):
    with pytest.raises(ValueError, match="KEGG"):
        parse(text)


@pytest.mark.parametrize("url", [
    "https://example.org/get/M99999", "http://rest.kegg.jp/get/M99999",
    "https://rest.kegg.jp.evil.example/get/M99999",
    "https://rest.kegg.jp/get/M99999?x=1", "https://rest.kegg.jp/get/M99999#fragment",
    "https://rest.kegg.jp/get/M99999/kgml", "https://rest.kegg.jp/get/md:M99999",
    "https://rest.kegg.jp/get/M99999+R99999", "https://rest.kegg.jp/get/M99999+M99999",
    "https://rest.kegg.jp/get/M99998", "https://rest.kegg.jp/get/M99999+M99998",
    "https://rest.kegg.jp/get/" + "+".join(f"M{i:05}" for i in range(11)),
])
def test_request_identity_class_and_options_are_checked(url):
    with pytest.raises(ValueError, match="KEGG"):
        kegg_terms(native(), "kegg-module-flatfile", url)


def test_unrequested_extra_and_mixed_class_entries_fail():
    for extra in [native("M99998"), native("R99998", "Reaction name", "Reaction")]:
        with pytest.raises(ValueError, match="KEGG"):
            parse(native() + extra)


def test_wrong_kind_or_missing_manifest_url_cannot_bypass_identity(tmp_path):
    path = tmp_path / "M99999.txt"
    path.write_text(native())
    with pytest.raises(ValueError, match="KEGG"):
        kegg_terms(native(), "kegg-gene-flatfile", "https://rest.kegg.jp/get/M99999")
    with pytest.raises(ValueError, match="KEGG"):
        list(source_terms("kegg-module-flatfile", path))


def fixture(tmp_path, body=None):
    records = tmp_path / "data" / "pathways"
    records.mkdir(parents=True)
    record = {"id": "KEGG:M99999", "label": "Curator-only description"}
    record_path = records / "record.yaml"
    record_path.write_text(yaml.safe_dump(record))
    source = tmp_path / "unrelated-filename.txt"
    source.write_text(body or native())
    entries = [{
        "key": "native", "kind": "kegg-module-flatfile", "path": source.name,
        "url": "https://rest.kegg.jp/get/M99999", "version": "synthetic fixture",
        "license": "synthetic fixture", "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    }]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return manifest, records, record_path, source, entries


def test_builder_uses_only_native_name_not_curated_or_cross_reference_labels(tmp_path):
    body = native().replace("///", "COMPOUND    C99999  Not a Compound authority\n///")
    manifest, records, _, _, _ = fixture(tmp_path, body)
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"] == {
        "KEGG:M99999": {"label": "Native cycle", "synonyms": [], "source": "native"},
    }
    assert "Curator-only" not in json.dumps(result)


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize("second_name", ["Different cycle", "Native cycle; New alias"])
def test_conflicting_labels_fail_before_selection_in_both_orders(
    tmp_path, selected, reverse, second_name,
):
    manifest, records, record_path, _, entries = fixture(tmp_path)
    if not selected:
        record_path.write_text("id: KEGG:M99998\nlabel: Unselected conflict\n")
    second = tmp_path / "second.txt"
    second.write_text(native(name=second_name))
    entries.append({
        **entries[0], "key": "second", "path": second.name,
        "sha256": hashlib.sha256(second.read_bytes()).hexdigest(),
    })
    manifest.write_text(json.dumps(entries[::-1] if reverse else entries))
    with pytest.raises(ValueError, match="conflicting KEGG native names"):
        build_snapshot(manifest, records, tmp_path)


def test_identical_assertions_keep_one_source_provenance(tmp_path):
    manifest, records, _, _, entries = fixture(tmp_path)
    entries.append({**entries[0], "key": "identical"})
    manifest.write_text(json.dumps(entries))
    snapshot = build_snapshot(manifest, records, tmp_path)
    assert snapshot["terms"]["KEGG:M99999"]["source"] == "native"
    assert set(snapshot["sources"]) == {"native"}


def test_duplicate_source_keys_rejected_even_if_first_source_is_unselected(tmp_path):
    manifest, records, _, source, entries = fixture(tmp_path)
    source.write_text(native("M99998"))
    first = {**entries[0], "url": "https://rest.kegg.jp/get/M99998",
             "sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
    second = tmp_path / "second.txt"
    second.write_text(native())
    manifest.write_text(json.dumps([first, {**entries[0], "path": second.name}]))
    with pytest.raises(ValueError, match="duplicate source key"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("problem", [
    "missing-id", "hash-mismatch", "malformed-batch", "wrong-url", "absolute-path", "parent-path",
])
def test_failed_build_never_replaces_existing_output(tmp_path, monkeypatch, problem):
    manifest, records, record_path, source, entries = fixture(tmp_path)
    if problem == "missing-id":
        record_path.write_text("id: KEGG:M99999\nlabel: Native cycle\nparticipants:\n"
                               "- id: KEGG:R99999\n  label: Plausible reaction\n")
    elif problem == "hash-mismatch":
        source.write_text(native(name="Changed body"))
    elif problem == "malformed-batch":
        source.write_text(native() + native("M99998").removesuffix("///\n"))
        entries[0]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    elif problem == "wrong-url":
        entries[0]["url"] = "https://rest.kegg.jp/get/M99998"
    elif problem == "absolute-path":
        entries[0]["path"] = str(source)
    elif problem == "parent-path":
        entries[0]["path"] = "../" + source.name
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "authority.json"
    output.write_bytes(b"previous snapshot\n")
    monkeypatch.setattr(sys, "argv", [
        "builder", "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(tmp_path), "--output", str(output),
    ])
    with pytest.raises(ValueError):
        main()
    assert output.read_bytes() == b"previous snapshot\n"


@pytest.mark.parametrize("problem,code", [
    (None, None), ("missing", "ID_NOT_FOUND"), ("wrong-name", "LABEL_MISMATCH"),
    ("synonym", "LABEL_MISMATCH"), ("source-context", "LABEL_AUTHORITY_UNAVAILABLE"),
])
def test_production_kegg_policy_remains_canonical_and_blocks_missing_ids(tmp_path, problem, code):
    manifest, records, record_path, _, _ = fixture(tmp_path, native(name="Native cycle; Alias"))
    snapshot = build_snapshot(manifest, records, tmp_path)
    record = {
        "id": "KEGG:M99999", "label": "Native cycle", "taxa": [],
        "participants": [], "reactions": [],
    }
    if problem == "missing":
        record["id"] = "KEGG:M99998"
    elif problem == "wrong-name":
        record["label"] = "Curated variant"
    elif problem == "synonym":
        record["label"] = "Alias"
    elif problem == "source-context":
        snapshot["terms"][record["id"]]["label_kind"] = "source_context"
    record_path.write_text(yaml.safe_dump(record))
    policy = yaml.safe_load(Path("conf/identifier_policy.yaml").read_text())
    assert policy["namespaces"]["KEGG"]["policy"] == "canonical"
    assert not any(rule["namespace"] == "KEGG" for rule in policy["contextual_labels"])
    policy["namespaces"] = {"KEGG": policy["namespaces"]["KEGG"]}
    policy["contextual_labels"] = []
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data/identifier_authorities/sources.json"
    authority.parent.mkdir()
    authority.write_text(json.dumps(snapshot))
    errors = identifier_errors(tmp_path)
    if code:
        assert any(code in error for error in errors), errors
    else:
        assert errors == []


def test_supported_kinds_do_not_implicitly_enable_other_kegg_classes():
    assert set(KEGG_SOURCE_TYPES) == {
        "kegg-module-flatfile", "kegg-reaction-flatfile", "kegg-compound-flatfile",
    }
