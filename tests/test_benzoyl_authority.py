"""Actual complete native originals and adversarial producer/consumer parity."""

from __future__ import annotations

import copy
import gzip
import hashlib
import json
import shutil
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.biocyc_benzoyl import (
    BENZOYL_KINDS,
    FIELD,
    benzoyl_metadata,
    benzoyl_term,
)
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot

FIXTURE = Path(__file__).parent / "fixtures/benzoyl_authority"
ROWS = json.loads((FIXTURE / "manifest.json").read_text())
STORAGE = json.loads((FIXTURE / "storage.json").read_text())
BY_ID = {row["id"]: row for row in ROWS}
BY_PATH = {row["entry"]["path"]: row for row in ROWS}
TYPED = [row["id"] for row in ROWS if row["entry"]["kind"] in BENZOYL_KINDS]
ANCHOR = "MetaCyc:RXN-15012"


def fixture_bytes(path):
    stored = STORAGE["files"][path]
    compressed = (FIXTURE / stored["path"]).read_bytes()
    assert len(compressed) == stored["bytes"]
    assert hashlib.sha256(compressed).hexdigest() == stored["sha256"]
    body = gzip.decompress(compressed)
    assert stored["original"] == BY_PATH[path]["original"]
    assert len(body) == stored["original"]["bytes"]
    assert hashlib.sha256(body).hexdigest() == stored["original"]["sha256"]
    return body


def stage(tmp_path):
    assert set(STORAGE["files"]) == set(BY_PATH)
    for path in BY_PATH:
        (tmp_path / path).write_bytes(fixture_bytes(path))
    return {row["id"]: copy.deepcopy(row["entry"]) for row in ROWS}


def build(tmp_path, entries, ids):
    corpus = tmp_path / "selected"
    corpus.mkdir(exist_ok=True)
    ids = list(ids)
    (corpus / "one.yaml").write_text(
        yaml.safe_dump(
            {
                "id": ids[0],
                "participants": [{"id": ident} for ident in ids[1:]],
            }
        )
    )
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return build_snapshot(manifest, corpus, tmp_path)


def consume(tmp_path, data):
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(data))
    return _load_authority(path)


def original(tmp_path, entry):
    return ET.fromstring((tmp_path / entry["path"]).read_bytes())


def save(tmp_path, entry, root):
    body = ET.tostring(root, encoding="utf-8")
    (tmp_path / entry["path"]).write_bytes(body)
    entry["sha256"] = hashlib.sha256(body).hexdigest()


def snapshot(metadata, key):
    ident, term = benzoyl_term(metadata, key)
    return {"version": 1, "sources": {key: metadata}, "terms": {ident: term}}


def test_complete_originals_roundtrip_all_slots_companions_and_first_owners(tmp_path):
    entries = stage(tmp_path)
    data = build(tmp_path, list(entries.values()), BY_ID)
    assert consume(tmp_path, data) == data["terms"]
    for ident in TYPED:
        source = data["sources"][entries[ident]["key"]]
        body = source[FIELD]["document"]["original_xml"].encode("utf-8")
        assert body == fixture_bytes(entries[ident]["path"])
        assert len(body) == BY_ID[ident]["original"]["bytes"]
        assert hashlib.sha256(body).hexdigest() == source["sha256"]
        for companion in source[FIELD]["companions"]:
            native = companion["document"]
            assert (
                native["original_xml"].encode("utf-8")
                == fixture_bytes(BY_ID[native["id"]]["entry"]["path"])
            )
            # A separately selected constituent keeps its ordinary first owner.
            assert data["terms"][native["id"]]["source"] == entries[native["id"]]["key"]
    bcr = data["sources"][entries["MetaCyc:1.3.99.15-RXN"]["key"]][FIELD]
    assert len(bcr["document"]["projection"]["activities"]) == 2
    assert bcr["document"]["projection"]["direction"] == "PHYSIOL-RIGHT-TO-LEFT"
    assert [
        s["coefficient"]
        for s in bcr["document"]["projection"]["sides"]
        if s["entity"]["native_type"] == "Protein"
    ] == [2, 2]
    oah = data["sources"][entries["MetaCyc:OAHTHAUERA-RXN"]["key"]][FIELD]
    assert oah["document"]["projection"]["memberships"] == []
    assert [c["document"]["id"] for c in oah["companions"]] == [
        "MetaCyc:RXN-15012",
        "MetaCyc:RXN-15013",
    ]


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
@pytest.mark.parametrize("changed", [False, True])
def test_complete_preselection_conflicts_and_first_owner(
    tmp_path, ident, reverse, selected, changed
):
    entries = stage(tmp_path)
    first = entries[ident]
    second = {**copy.deepcopy(first), "key": "second", "path": "second.xml"}
    if changed:
        root = original(tmp_path, first)
        node = root[1].find("comment")
        if node is not None:
            node.text += " Retained contextual clarification."
        else:
            root[1].find("gibbs-0").text = "-99.1"
        save(tmp_path, second, root)
    else:
        shutil.copyfile(tmp_path / first["path"], tmp_path / second["path"])
    pairs = [first, second][:: (-1 if reverse else 1)]
    wanted = ident if selected else ANCHOR
    manifest = pairs + ([] if selected else [entries[ANCHOR]])
    metadata = {e["key"]: benzoyl_metadata(e, tmp_path) for e in pairs}
    single = build(tmp_path, [pairs[0]], [ident])
    consumer = {**single, "sources": metadata}
    if not selected:
        unrelated = build(tmp_path, [entries[ANCHOR]], [ANCHOR])
        consumer["sources"].update(unrelated["sources"])
        consumer["terms"] = unrelated["terms"]
    if changed:
        with pytest.raises(ValueError, match="conflicting complete bounded"):
            build(tmp_path, manifest, [wanted])
        with pytest.raises(ValueError, match="conflicting complete bounded"):
            consume(tmp_path, consumer)
    else:
        data = build(tmp_path, manifest, [wanted])
        assert consume(tmp_path, data) == data["terms"]
        assert consume(tmp_path, consumer) == consumer["terms"]
        if selected:
            assert data["terms"][ident]["source"] == pairs[0]["key"]


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize("field", ["id", "projection", "original_xml", "source_hash", "kind"])
def test_consumer_cannot_edit_or_strip_complete_original_scope(tmp_path, ident, field):
    entries = stage(tmp_path)
    entry = entries[ident]
    metadata = benzoyl_metadata(entry, tmp_path)
    data = snapshot(metadata, entry["key"])
    if field == "source_hash":
        metadata["sha256"] = "0" * 64
    elif field == "kind":
        metadata.pop("kind")
    elif field == "projection":
        metadata[FIELD]["document"][field]["label"] = "forged authority label"
    elif field == "original_xml":
        metadata[FIELD]["document"][field] += "\n"
    else:
        metadata[FIELD]["document"][field] = "MetaCyc:OTHER"
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("typed_present", [False, True])
def test_request_only_downgrade_rejected_even_when_unselected(
    tmp_path, ident, reverse, typed_present
):
    entries = stage(tmp_path)
    entry = entries[ident]
    downgraded = {k: v for k, v in entry.items() if k != "constituent_sources"}
    downgraded.update(key="downgraded", kind="metacyc-html")
    owners = ([entry] if typed_present else []) + [downgraded, entries[ANCHOR]]
    if reverse:
        owners.reverse()
    with pytest.raises(ValueError, match="requires its complete typed scope"):
        build(tmp_path, owners, [ANCHOR])
    unrelated = build(tmp_path, [entries[ANCHOR]], [ANCHOR])
    old = {k: v for k, v in downgraded.items() if k in {"url", "version", "sha256", "license"}}
    unrelated["sources"]["downgraded"] = old
    if typed_present:
        unrelated["sources"][entry["key"]] = benzoyl_metadata(entry, tmp_path)
    if reverse:
        unrelated["sources"] = dict(reversed(list(unrelated["sources"].items())))
    with pytest.raises(ValueError, match="requires its complete typed scope"):
        consume(tmp_path, unrelated)


@pytest.mark.parametrize("ident", TYPED)
def test_parsed_term_cannot_move_to_untyped_owner_with_uninformative_url(tmp_path, ident):
    entries = stage(tmp_path)
    data = snapshot(benzoyl_metadata(entries[ident], tmp_path), entries[ident]["key"])
    data["sources"]["other"] = {
        "url": "https://example.org/other",
        "version": "1",
        "license": "fixture",
        "sha256": "0" * 64,
    }
    data["terms"][ident] = {"source": "other", "label": "invented", "synonyms": []}
    with pytest.raises(ValueError, match="conflicting typed native identity scope"):
        consume(tmp_path, data)


def alter_ref(node, frame):
    old = node.get("frameid")
    for key, value in list(node.attrib.items()):
        node.set(key, value.replace(old, frame))


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize(
    "problem",
    [
        "release",
        "class",
        "nested-name",
        "missing-context",
        "parent",
        "duplicate-parent",
        "unknown-slot",
        "mixed-text",
    ],
)
def test_whole_envelope_context_and_identity_fail_closed(tmp_path, ident, problem):
    entry = stage(tmp_path)[ident]
    root = original(tmp_path, entry)
    entity = root[1]
    if problem == "release":
        root.find("metadata/PGDB").set("version", "28.0")
    elif problem == "class":
        entity.set("class", "false")
    elif problem == "nested-name":
        node = entity.find("common-name")
        if node is None:
            node = ET.SubElement(entity, "common-name", {"datatype": "string"})
        ET.SubElement(node, "common-name").text = "nested name"
    elif problem == "missing-context":
        target = entity.find("credits")
        entity.remove(target if target is not None else entity.find("gibbs-0"))
    elif problem == "parent":
        alter_ref(entity.find("parent")[0], "Wrong-Parents")
    elif problem == "duplicate-parent":
        entity.append(copy.deepcopy(entity.find("parent")))
    elif problem == "unknown-slot":
        ET.SubElement(entity, "unreviewed-slot")
    else:
        entity.text = "non-whitespace"
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        benzoyl_metadata(entry, tmp_path)


@pytest.mark.parametrize(
    "problem",
    ["missing", "duplicate", "self", "coefficient", "zero", "backlink", "nested-name", "species"],
)
def test_heteromer_component_and_activity_scope(tmp_path, problem):
    entry = stage(tmp_path)["MetaCyc:CPLX-1341"]
    root = original(tmp_path, entry)
    entity = root[1]
    component = entity.find("component")
    if problem == "missing":
        entity.remove(component)
    elif problem == "duplicate":
        other = entity.findall("component")[1]
        other[0].attrib = dict(component[0].attrib)
    elif problem == "self":
        alter_ref(component[0], "CPLX-1341")
    elif problem in {"coefficient", "zero"}:
        component[1].text = "2" if problem == "coefficient" else "0"
    elif problem == "backlink":
        alter_ref(entity.find("catalyzes/Enzymatic-Reaction/enzyme/Protein"), "CPLX-WRONG")
    elif problem == "species":
        entity.find("species/Organism").set("class", "false")
    else:
        node = entity.find("catalyzes/Enzymatic-Reaction/common-name")
        ET.SubElement(node, "span").text = "invented name"
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        benzoyl_metadata(entry, tmp_path)


@pytest.mark.parametrize(
    "problem",
    [
        "coefficient",
        "type",
        "class",
        "direction",
        "activity",
        "backlink",
        "ec",
        "official",
        "credit",
        "citation",
    ],
)
def test_bcr_does_not_erase_carrier_or_two_activity_scope(tmp_path, problem):
    entry = stage(tmp_path)["MetaCyc:1.3.99.15-RXN"]
    root = original(tmp_path, entry)
    entity = root[1]
    carrier = entity.find("left/Protein")
    if problem == "coefficient":
        entity.find("left/coefficient").text = "1"
    elif problem == "type":
        carrier.tag = "Compound"
        carrier.attrib.pop("class")
    elif problem == "class":
        carrier.attrib.pop("class")
    elif problem == "direction":
        entity.find("reaction-direction").text = "PHYSIOL-LEFT-TO-RIGHT"
    elif problem == "activity":
        wrapper = entity.find("enzymatic-reaction")
        wrapper.remove(wrapper[0])
    elif problem == "backlink":
        alter_ref(
            entity.find("enzymatic-reaction/Enzymatic-Reaction/reaction/Reaction"), "RXN-WRONG"
        )
    elif problem == "ec":
        entity.find("ec-number").text = "EC-1.18.98.M1"
    elif problem == "official":
        entity.find("ec-number/official").text = "NIL"
    elif problem == "credit":
        entity.find("credits/revised/date").text = "not-a-date"
    else:
        entity.find("citation/Publication/pubmed-id").text = "not-a-PMID"
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        benzoyl_metadata(entry, tmp_path)


@pytest.mark.parametrize("ident", ["MetaCyc:Reduced-ferredoxins", "MetaCyc:Oxidized-ferredoxins"])
@pytest.mark.parametrize("problem", ["name", "parent", "state", "member", "unit-type", "context"])
def test_ferredoxin_generic_unit_and_state_links(tmp_path, ident, problem):
    entry = stage(tmp_path)[ident]
    root = original(tmp_path, entry)
    entity = root[1]
    if problem == "name":
        entity.find("common-name").text = "a whole two-cluster ferredoxin protein"
    elif problem == "parent":
        alter_ref(entity.find("parent")[0], "Thioredoxin")
    elif problem == "state":
        alter_ref(entity.find("unmodified-form")[0], "Other-ferredoxins")
    elif problem == "member":
        entity.remove(entity.find("subclass"))
    elif problem == "unit-type":
        entity.tag = "Compound"
    else:
        entity.find("appears-in-left-side-of")[0].set("orgid", "ECOLI")
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        benzoyl_metadata(entry, tmp_path)


@pytest.mark.parametrize(
    "problem",
    [
        "order",
        "duplicate",
        "backlink",
        "intermediate",
        "water",
        "proton",
        "release",
        "pgdb",
        "activity",
        "selected-member",
    ],
)
def test_oah_complete_constituents_cancellation_and_auxiliary_scope(tmp_path, problem):
    entry = stage(tmp_path)["MetaCyc:OAHTHAUERA-RXN"]
    if problem in {"order", "duplicate"}:
        entry["constituent_sources"] = (
            entry["constituent_sources"][::-1]
            if problem == "order"
            else [entry["constituent_sources"][0]] * 2
        )
    else:
        target = (
            entry
            if problem in {"water", "activity", "selected-member"}
            else entry["constituent_sources"][0 if problem != "proton" else 1]
        )
        root = original(tmp_path, target)
        entity = root[1]
        if problem == "backlink":
            alter_ref(entity.find("in-pathway/Reaction"), "OTHER-COMPOSITE")
        elif problem == "intermediate":
            alter_ref(entity.find("right/Compound"), "CPD-WRONG")
        elif problem == "water":
            entity.find("left/coefficient").text = "1"
        elif problem == "proton":
            alter_ref(entity.findall("right")[1][0], "CPD-WRONG")
        elif problem == "release":
            target["version"] = "28.0"
        elif problem == "pgdb":
            root.find("metadata/PGDB").set("orgid", "ECOLI")
        elif problem == "activity":
            alter_ref(entity.find("enzymatic-reaction/Enzymatic-Reaction/enzyme/Protein"), "OTHER")
        else:
            wrapper = ET.SubElement(entity, "in-pathway")
            ET.SubElement(
                wrapper,
                "Pathway",
                {
                    "resource": "getxml?META:CENTBENZCOA-PWY",
                    "orgid": "META",
                    "frameid": "CENTBENZCOA-PWY",
                },
            )
        save(tmp_path, target, root)
    with pytest.raises(ValueError):
        benzoyl_metadata(entry, tmp_path)


@pytest.mark.parametrize(
    "problem", ["empty", "duplicate", "nested", "absent", "equation", "activity"]
)
def test_named_reaction_requires_its_direct_name_and_complete_context(tmp_path, problem):
    entry = stage(tmp_path)["MetaCyc:RXN-8032"]
    root = original(tmp_path, entry)
    entity = root[1]
    node = entity.find("common-name")
    if problem == "empty":
        node.text = " "
    elif problem == "duplicate":
        entity.append(copy.deepcopy(node))
    elif problem == "nested":
        ET.SubElement(node, "common-name").text = "nested label"
    elif problem == "absent":
        entity.remove(node)
    elif problem == "equation":
        alter_ref(entity.find("left/Compound"), "WRONG-SUBSTRATE")
    else:
        alter_ref(entity.find("enzymatic-reaction/Enzymatic-Reaction/enzyme/Protein"), "OTHER")
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        benzoyl_metadata(entry, tmp_path)


@pytest.mark.parametrize("reverse", [False, True])
def test_oah_rejects_conflicting_ordinary_companion_owner_before_selection(tmp_path, reverse):
    entries = stage(tmp_path)
    other = entries[ANCHOR]
    root = original(tmp_path, other)
    root[1].find("gibbs-0").text = "-99.1"
    other["path"] = "changed-constituent.xml"
    save(tmp_path, other, root)
    chosen = entries["MetaCyc:CPLX-1341"]
    owners = [entries["MetaCyc:OAHTHAUERA-RXN"], other, chosen]
    if reverse:
        owners.reverse()
    with pytest.raises(ValueError, match="companion owner differs"):
        build(tmp_path, owners, ["MetaCyc:CPLX-1341"])


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("changed", ["provenance", "body", "projection", "order", "missing"])
def test_consumer_preserves_full_companion_and_ordinary_owner_scope(tmp_path, reverse, changed):
    entries = stage(tmp_path)
    data = build(tmp_path, list(entries.values()), BY_ID)
    oah = data["sources"][entries["MetaCyc:OAHTHAUERA-RXN"]["key"]][FIELD]
    if changed == "provenance":
        data["sources"][entries[ANCHOR]["key"]]["sha256"] = "0" * 64
    elif changed == "body":
        oah["companions"][0]["document"]["original_xml"] += "\n"
    elif changed == "projection":
        oah["companions"][0]["document"]["projection"]["sides"][0]["coefficient"] = 2
    elif changed == "order":
        oah["companions"].reverse()
    else:
        oah["companions"].pop()
    # Test the same invalid scope when neither the composite nor constituents
    # contribute a selected term: validation must precede term selection.
    data["terms"] = {"MetaCyc:CPLX-1341": data["terms"]["MetaCyc:CPLX-1341"]}
    if reverse:
        data["sources"] = dict(reversed(list(data["sources"].items())))
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize("replacement", [True, 1.0, "1"])
def test_projection_numbers_cannot_change_json_type(tmp_path, replacement):
    entry = stage(tmp_path)["MetaCyc:CPLX-1341"]
    data = snapshot(benzoyl_metadata(entry, tmp_path), entry["key"])
    native = data["sources"][entry["key"]][FIELD]
    native["document"]["projection"]["components"][0]["coefficient"] = replacement
    with pytest.raises(ValueError, match="projection mismatch"):
        consume(tmp_path, data)


@pytest.mark.parametrize(
    "ident,category",
    [
        ("MetaCyc:CPLX-1341", "complex"),
        ("MetaCyc:Reduced-ferredoxins", "protein"),
        ("MetaCyc:RXN-8032", "molecular_activity"),
        ("MetaCyc:1.3.99.15-RXN", "molecular_activity"),
    ],
)
@pytest.mark.parametrize("problem", ["none", "placement", "category", "label"])
def test_typed_placement_and_canonical_labels_under_broad_context(
    tmp_path, ident, category, problem
):
    entries = stage(tmp_path)
    data = snapshot(benzoyl_metadata(entries[ident], tmp_path), entries[ident]["key"])
    data["sources"]["anchor"] = {
        "url": "https://example.org/anchor",
        "version": "1",
        "license": "fixture",
        "sha256": "0" * 64,
    }
    data["terms"]["MetaCyc:TEST"] = {"label": "test", "synonyms": [], "source": "anchor"}
    (tmp_path / "authority.json").write_text(json.dumps(data))
    term = data["terms"][ident]
    node = {"id": ident, "label": term["label"], "category": category}
    section = "reactions" if category == "molecular_activity" else "participants"
    if problem == "placement":
        section = "taxa"
    elif problem == "category":
        node["category"] = "chemical_entity"
    elif problem == "label":
        node["label"] = "invented canonical label"
    directory = tmp_path / "data/pathways"
    directory.mkdir(parents=True)
    (directory / "one.yaml").write_text(
        yaml.safe_dump(
            {
                "id": "MetaCyc:TEST",
                "label": "test",
                "taxa": [],
                "participants": [],
                "reactions": [],
                section: [node],
            }
        )
    )
    policy = tmp_path / "policy.yaml"
    policy.write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "namespaces": {"MetaCyc": {"snapshot": "authority.json", "policy": "canonical"}},
                "contextual_labels": [
                    {
                        "namespace": "MetaCyc",
                        "sections": ["participants", "reactions", "taxa"],
                        "record_prefixes": ["MetaCyc"],
                        "reason": "adversarial broad context",
                    }
                ],
            }
        )
    )
    errors = identifier_errors(tmp_path, policy)
    # Unnamed BCR deliberately permits a contextual reaction display.
    expected = problem != "none" and not (
        problem == "label" and term["label_kind"] == "source_context"
    )
    assert bool(errors) == expected, errors
