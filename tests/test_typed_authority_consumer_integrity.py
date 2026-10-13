"""Retained native owners cannot be contradicted or erased by term selection."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import test_aceto_authority as aceto
import test_biocyc_carrier_authority as carrier
import test_electron_transfer_authority as native
import yaml

from pathwaymech.identifiers import _load_authority, identifier_errors

MODES = ["class-red", "state-red", "reaction", "quinone", "complex", "polymer"]
LEGACY = {
    "url": "https://example.org/legacy",
    "version": "1",
    "license": "fixture",
    "sha256": "0" * 64,
}


def entry(tmp_path, mode, key, changed=False):
    if mode in {"class-red", "state-red"}:
        root = carrier.document(mode)
        if changed:
            root[1].find("common-name").text = "different native canonical name"
        return carrier.entry(tmp_path, mode, key=key, root=root)
    if mode == "polymer":
        root = native.rdf_document()
        if changed:
            root[0].find(native.RH + "formula").text = "C3H6(C2H4)<i><sub>n</sub></i>"
        return native.rdf_entry(tmp_path, root, key=key)
    root = native.document(mode)
    if changed:
        if mode == "reaction":
            root[1].find("left/coefficient").text = "9"
        else:
            root[1].find("common-name").text = "different native canonical name"
    return native.entry(tmp_path, mode, root, key=key)


def metadata(item, tmp_path):
    if item["kind"] in {carrier.CARRIER_CLASS_KIND, carrier.ECOCYC_STATE_KIND}:
        return carrier.metadata(item, tmp_path)
    return native.metadata(item, tmp_path)


def selected_id(mode):
    if mode == "class-red":
        return "MetaCyc:RED"
    if mode == "state-red":
        return "EcoCyc:RED"
    if mode == "polymer":
        return "RHEA-COMP:99991"
    return ("EcoCyc" if mode == "complex" else "MetaCyc") + ":SYNTHETIC.17"


def consume(tmp_path, data, reverse=False):
    body = copy.deepcopy(data)
    if reverse:
        body["sources"] = dict(reversed(list(body["sources"].items())))
    path = tmp_path / "authority.json"
    path.write_text(json.dumps(body))
    return _load_authority(path)


@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("reverse", [False, True])
def test_typed_identity_cannot_move_to_legacy_term_owner(tmp_path, mode, reverse):
    item = entry(tmp_path, mode, "typed")
    ident = selected_id(mode)
    data = native.snap(tmp_path, [item], ident)
    data["sources"]["legacy"] = LEGACY
    data["terms"][ident] = {"label": "fabricated name", "synonyms": [], "source": "legacy"}
    with pytest.raises(ValueError, match="conflicting typed native identity scope"):
        consume(tmp_path, data, reverse)


@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
@pytest.mark.parametrize("changed", [False, True])
def test_complete_owner_conflict_parity_and_identical_duplicate_acceptance(
    tmp_path, mode, reverse, selected, changed
):
    entries = [entry(tmp_path, mode, "first"), entry(tmp_path, mode, "second", changed)]
    if reverse:
        entries.reverse()
    ident = selected_id(mode)
    chosen = entries[0]
    wanted = ident
    if not selected:
        chosen = carrier.entry(tmp_path, "class-compound", key="anchor")
        wanted = "MetaCyc:CLIENT"
    data = native.snap(tmp_path, [chosen], wanted)
    data["sources"].update({e["key"]: metadata(e, tmp_path) for e in entries})
    producer_entries = entries if selected else [*entries, chosen]
    before = json.dumps(data)
    if changed:
        with pytest.raises(ValueError, match="conflicting"):
            native.snap(tmp_path, producer_entries, wanted)
        with pytest.raises(ValueError, match="conflicting"):
            consume(tmp_path, data)
    else:
        built = native.snap(tmp_path, producer_entries, wanted)
        assert consume(tmp_path, data) == data["terms"]
        assert consume(tmp_path, built) == built["terms"]
        if selected:
            assert built["terms"][ident]["source"] == entries[0]["key"]
    assert json.dumps(data) == before


@pytest.mark.parametrize("reverse", [False, True])
def test_counterpart_facts_checked_without_selecting_the_counterpart(tmp_path, reverse):
    first = carrier.entry(tmp_path, "state-red", key="first")
    changed = carrier.document("state-red")
    changed[1].find("common-name").text = "different counterpart name"
    second = carrier.entry(tmp_path, "state-ox", key="second", partner=changed)
    entries = [second, first] if reverse else [first, second]
    data = native.snap(tmp_path, [first], "EcoCyc:RED")
    data["sources"] = {e["key"]: metadata(e, tmp_path) for e in entries}
    with pytest.raises(ValueError, match="conflicting"):
        native.snap(tmp_path, entries, "EcoCyc:OX")
    with pytest.raises(ValueError, match="conflicting"):
        consume(tmp_path, data)


@pytest.mark.parametrize("reverse", [False, True])
def test_counterpart_identity_cannot_be_selected_from_a_legacy_owner(tmp_path, reverse):
    first = carrier.entry(tmp_path, "state-red", key="first")
    data = native.snap(tmp_path, [first], "EcoCyc:RED")
    data["sources"]["legacy"] = LEGACY
    data["terms"]["EcoCyc:OX"] = {"label": "fabricated", "synonyms": [], "source": "legacy"}
    with pytest.raises(ValueError, match="conflicting typed native identity scope"):
        consume(tmp_path, data, reverse)


@pytest.mark.parametrize("reverse", [False, True])
def test_unselected_polymer_members_are_registered(tmp_path, reverse):
    root = native.rdf_document()
    root.append(native.rdf_document("99992")[0])
    first = native.rdf_entry(tmp_path, root, key="first")
    changed = native.rdf_document("99992")
    changed[0].find(native.RH + "formula").text = "C3H6(C2H4)<i><sub>n</sub></i>"
    second = native.rdf_entry(tmp_path, changed, key="second")
    entries = [second, first] if reverse else [first, second]
    data = native.snap(tmp_path, [first], "RHEA-COMP:99991")
    data["sources"] = {e["key"]: metadata(e, tmp_path) for e in entries}
    with pytest.raises(ValueError, match="conflicting"):
        native.snap(tmp_path, entries, "RHEA-COMP:99991")
    with pytest.raises(ValueError, match="conflicting"):
        consume(tmp_path, data)


@pytest.mark.parametrize("mode", MODES[:-1])
@pytest.mark.parametrize("reverse", [False, True])
def test_same_native_facts_from_conflicting_releases_are_rejected(tmp_path, mode, reverse):
    first = entry(tmp_path, mode, "first")
    second = entry(tmp_path, mode, "second")
    originals = [second]
    if mode == "state-red":
        originals.append(second["counterpart_source"])
    for original in originals:
        path = tmp_path / original["path"]
        root = ET.fromstring(path.read_bytes())
        root.set("ptools-version", "26.0")
        root.find("metadata/PGDB").set("version", "26.0")
        path.write_bytes(ET.tostring(root))
        original["version"] = "26.0"
        original["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    entries = [second, first] if reverse else [first, second]
    data = native.snap(tmp_path, [first], selected_id(mode))
    data["sources"] = {e["key"]: metadata(e, tmp_path) for e in entries}
    with pytest.raises(ValueError, match="conflicting"):
        native.snap(tmp_path, entries, selected_id(mode))
    with pytest.raises(ValueError, match="conflicting"):
        consume(tmp_path, data)


def test_identical_polymer_facts_keep_producer_release_compatibility(tmp_path):
    first = entry(tmp_path, "polymer", "first")
    second = {**first, "key": "second", "version": "another-compatible-release"}
    data = native.snap(tmp_path, [first, second], "RHEA-COMP:99991")
    data["sources"]["second"] = metadata(second, tmp_path)
    assert consume(tmp_path, data) == data["terms"]


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("other", ["reaction", "ordinary-reaction", "state"])
def test_unselected_cross_kind_identity_claims_are_rejected(tmp_path, reverse, other):
    mode = "state-red" if other == "state" else "class-red"
    first = entry(tmp_path, mode, "first")
    data = native.snap(tmp_path, [first], selected_id(mode))
    if other == "ordinary-reaction":
        data["sources"]["second"] = {
            **{k: first[k] for k in LEGACY},
            "kind": "metacyc-reaction-xml",
        }
    else:
        # Each source has a valid whole shape; their native identity types disagree.
        mode = "complex" if other == "state" else "reaction"
        second = native.entry(tmp_path, mode, native.document(mode, "RED"), key="second")
        data["sources"]["second"] = metadata(second, tmp_path)
    with pytest.raises(ValueError, match="conflicting"):
        consume(tmp_path, data, reverse)


@pytest.mark.parametrize("reverse", [False, True])
def test_existing_aceto_companion_owners_remain_compatible(tmp_path, reverse):
    rows = aceto.stage(tmp_path)
    entries = [row["entry"] for row in rows]
    if reverse:
        entries.reverse()
    data = aceto.build(tmp_path, entries, aceto.BY_ID)
    before = json.dumps(data)
    assert consume(tmp_path, data, reverse) == data["terms"]
    assert json.dumps(data) == before


def test_identifier_gate_rejects_erased_type_and_fabricated_name(tmp_path):
    first = entry(tmp_path, "class-red", "first")
    data = native.snap(tmp_path, [first], "MetaCyc:RED")
    data["sources"]["legacy"] = LEGACY
    data["terms"]["MetaCyc:ROOT"] = {"label": "root", "synonyms": [], "source": "legacy"}
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    record = {
        "id": "MetaCyc:ROOT",
        "label": "root",
        "taxa": [],
        "reactions": [],
        "participants": [
            {"id": "MetaCyc:RED", "label": "a native class-red", "category": "small_molecule"}
        ],
    }
    policy = tmp_path / "policy.yaml"
    policy.write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "namespaces": {"MetaCyc": {"snapshot": "authority.json", "policy": "canonical"}},
                "contextual_labels": [],
            }
        )
    )
    (records / "record.yaml").write_text(yaml.safe_dump(record))
    consume(tmp_path, data)
    assert any("ENTITY_TYPE_MISMATCH" in e for e in identifier_errors(tmp_path, policy))
    data["terms"]["MetaCyc:RED"] = {"label": "fabricated", "synonyms": [], "source": "legacy"}
    record["participants"][0]["label"] = "fabricated"
    (records / "record.yaml").write_text(yaml.safe_dump(record))
    (tmp_path / "authority.json").write_text(json.dumps(data))
    assert any(
        "conflicting typed native identity scope" in e for e in identifier_errors(tmp_path, policy)
    )


def test_checked_in_source_authority_terms_are_unchanged():
    path = Path(__file__).parents[1] / "data/identifier_authorities/sources.json"
    before = path.read_bytes()
    assert _load_authority(path) == json.loads(before)["terms"]
    assert path.read_bytes() == before
