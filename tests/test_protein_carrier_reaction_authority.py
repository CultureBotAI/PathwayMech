"""Complete Mar original, whole reconstruction and preselection conflict controls."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.biocyc_native_context import ancillary, rebuild, retained
from pathwaymech.biocyc_pathway import pathway_metadata
from pathwaymech.biocyc_protein_carrier_reaction import (
    CORE,
    FIELD,
    carrier_reaction_metadata,
    carrier_reaction_term,
)
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, source_terms

FIXTURE = Path(__file__).parent / "fixtures/protein_carrier_reaction"
ROW = json.loads((FIXTURE / "manifest.json").read_text())
IDENT = "MetaCyc:RXN-21320"


def original():
    return ET.fromstring((FIXTURE / "RXN-21320.xml").read_bytes())


def item(tmp_path, root=None, key="mar", **changes):
    entry = {**ROW["entry"], "key": key, "path": key + ".xml", **changes}
    body = (FIXTURE / "RXN-21320.xml").read_bytes() if root is None else ET.tostring(root)
    (tmp_path / entry["path"]).write_bytes(body)
    entry["sha256"] = hashlib.sha256(body).hexdigest()
    return entry


def build(tmp_path, entries, ids=(IDENT,)):
    selected = tmp_path / "selected"
    selected.mkdir(exist_ok=True)
    (selected / "one.yaml").write_text(
        yaml.safe_dump({"id": ids[0], "participants": [{"id": i} for i in ids[1:]]})
    )
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return build_snapshot(manifest, selected, tmp_path)


def consume(tmp_path, data):
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(data))
    return _load_authority(path)


def snapshot(metadata, source="mar"):
    ident, term = carrier_reaction_term(metadata, source)
    return {"version": 1, "sources": {source: metadata}, "terms": {ident: term}}


def unrelated(tmp_path):
    fixtures = FIXTURE.parent / "nitrate_authority"
    row = next(
        r
        for r in json.loads((fixtures / "manifest.json").read_text())
        if r["id"] == "MetaCyc:PWY0-1352"
    )
    entry = {**row["entry"], "key": "other", "path": "other.xml"}
    (tmp_path / entry["path"]).write_bytes((fixtures / row["entry"]["path"]).read_bytes())
    return entry, row["id"]


def test_complete_original_roundtrip_and_every_slot(tmp_path):
    raw = (FIXTURE / "RXN-21320.xml").read_bytes()
    assert len(raw) == 4104 and hashlib.sha256(raw).hexdigest() == ROW["original"]["sha256"]
    metadata = carrier_reaction_metadata(item(tmp_path), tmp_path)
    native = metadata[FIELD]
    assert native["direct_slot_order"] == [n.tag for n in original()[1]]
    for slot, child in zip(native["source_slots"], original()[1], strict=True):
        assert slot == {"tag": child.tag, "xml": ET.tostring(child, encoding="unicode")}
    assert [
        (s["side"], s["entity"]["id"], s["coefficient"], s["coefficient_explicit"])
        for s in native["sides"]
    ] == [
        ("left", "MetaCyc:CPD-7677", 1, False),
        ("left", "MetaCyc:Reduced-ferredoxins", 2, True),
        ("left", "MetaCyc:PROTON", 2, True),
        ("right", "MetaCyc:ETHYLENE-CMPD", 1, False),
        ("right", "MetaCyc:CPD-7671", 1, False),
        ("right", "MetaCyc:WATER", 1, False),
        ("right", "MetaCyc:Oxidized-ferredoxins", 2, True),
    ]
    assert [s["source_position"] for s in native["sides"]] == [12, 13, 14, 5, 6, 7, 8]
    assert [s["entity"]["native_type"] for s in native["sides"]].count("Protein") == 2
    data = build(tmp_path, [item(tmp_path)])
    assert consume(tmp_path, data) == data["terms"]
    assert data["terms"][IDENT] == {
        "label": "RXN-21320",
        "synonyms": [],
        "source": "mar",
        "entity_type": "reaction",
        "label_kind": "source_context",
    }
    assert rebuild(native, "Reaction").findtext("ec-number") == "EC-1.18.98.M1"


BAD = [
    "parent-missing",
    "parent-duplicate",
    "parent-other",
    "parent-class",
    "parent-type",
    "left-empty",
    "right-empty",
    "carrier-instance",
    "compound-class",
    "carrier-as-compound",
    "reference-resource",
    "reference-org",
    "reference-nested",
    "multiple-targets",
    "side-text",
    "side-tail",
    "duplicate-side",
    "coefficient-zero",
    "coefficient-negative",
    "coefficient-fraction",
    "coefficient-symbol",
    "coefficient-type",
    "coefficient-duplicate",
    "coefficient-nested",
    "coefficient-before-target",
    "compartment",
    "direction-missing",
    "direction-duplicate",
    "direction-other",
    "name",
    "empty-name",
    "borrowed-name",
    "unknown-slot",
    "orphan",
    "orphan-duplicate",
    "boolean",
    "boolean-duplicate",
    "comment-duplicate",
    "activity-duplicate",
    "activity-backlink",
    "activity-extra",
    "activity-enzyme-class",
    "credit-extra",
    "credit-date",
    "credit-person-extra",
    "credit-affiliation",
    "ec-token",
    "ec-official",
    "ec-duplicate",
]


def mutate(root, case):
    e = root[1]
    left = e.findall("left")[1]
    if case == "parent-missing":
        e.remove(e.find("parent"))
    elif case == "parent-duplicate":
        e.append(copy.deepcopy(e.find("parent")))
    elif case == "parent-other":
        p = e.find("parent/Reaction")
        p.set("frameid", "Protein-Modification-Reactions")
        p.set("resource", "getxml?META:Protein-Modification-Reactions")
    elif case == "parent-class":
        e.find("parent/Reaction").attrib.pop("class")
    elif case == "parent-type":
        e.find("parent/Reaction").tag = "Compound"
    elif case in {"left-empty", "right-empty"}:
        for n in e.findall(case.split("-")[0]):
            e.remove(n)
    elif case == "carrier-instance":
        left[0].attrib.pop("class")
    elif case == "compound-class":
        e.find("left/Compound").set("class", "true")
    elif case == "carrier-as-compound":
        left[0].tag = "Compound"
        left[0].attrib.pop("class")
    elif case == "reference-resource":
        left[0].set("resource", "getxml?META:OTHER")
    elif case == "reference-org":
        left[0].set("orgid", "ECOLI")
    elif case == "reference-nested":
        ET.SubElement(left[0], "comment").text = "bad"
    elif case == "multiple-targets":
        left.append(copy.deepcopy(left[0]))
    elif case == "side-text":
        left.text = "bad"
    elif case == "side-tail":
        left[0].tail = "bad"
    elif case == "duplicate-side":
        e.append(copy.deepcopy(left))
    elif case.startswith("coefficient-"):
        n = left[1]
        suffix = case.removeprefix("coefficient-")
        if suffix in {"zero", "negative", "fraction", "symbol"}:
            n.text = {"zero": "0", "negative": "-1", "fraction": "0.5", "symbol": "n"}[suffix]
        elif suffix == "type":
            n.set("datatype", "float")
        elif suffix == "duplicate":
            left.append(copy.deepcopy(n))
        elif suffix == "nested":
            ET.SubElement(n, "value").text = "2"
        else:
            left.remove(n)
            left.insert(0, n)
    elif case == "compartment":
        ET.SubElement(left, "compartment")
    elif case == "direction-missing":
        e.remove(e.find("reaction-direction"))
    elif case == "direction-duplicate":
        e.append(copy.deepcopy(e.find("reaction-direction")))
    elif case == "direction-other":
        e.find("reaction-direction").text = "RIGHT-TO-LEFT"
    elif case in {"name", "empty-name", "borrowed-name"}:
        n = ET.SubElement(e, "common-name", {"datatype": "string"})
        n.text = "" if case == "empty-name" else "(2-methylsulfanyl)ethanol reductase"
    elif case == "unknown-slot":
        ET.SubElement(e, "catalyzes")
    elif case == "orphan":
        e.find("orphan").text = "YES"
    elif case == "boolean":
        e.find("physiologically-relevant").text = "T"
    elif case in {
        "orphan-duplicate",
        "boolean-duplicate",
        "comment-duplicate",
        "activity-duplicate",
        "ec-duplicate",
    }:
        tag = {
            "boolean": "physiologically-relevant",
            "activity": "enzymatic-reaction",
            "ec": "ec-number",
        }.get(case.split("-")[0], case.split("-")[0])
        e.append(copy.deepcopy(e.find(tag)))
    elif case == "activity-backlink":
        n = e.find("enzymatic-reaction/Enzymatic-Reaction/reaction/Reaction")
        n.set("frameid", "OTHER")
        n.set("resource", "#META:OTHER")
    elif case == "activity-extra":
        ET.SubElement(e.find("enzymatic-reaction/Enzymatic-Reaction"), "other")
    elif case == "activity-enzyme-class":
        e.find("enzymatic-reaction/Enzymatic-Reaction/enzyme/Protein").set("class", "true")
    elif case == "credit-extra":
        ET.SubElement(e.find("credits"), "revised")
    elif case == "credit-date":
        e.find("credits/created/date").text = "2020-13-40"
    elif case == "credit-person-extra":
        ET.SubElement(e.find("credits/created/Person"), "extra")
    elif case == "credit-affiliation":
        e.find("credits/created/Organization").set("frameid", "OTHER")
    elif case == "ec-token":
        e.find("ec-number").text = "EC-1.18.98.M2"
    elif case == "ec-official":
        e.find("ec-number/official").text = "true"
    else:
        raise AssertionError(case)
    return root


@pytest.mark.parametrize("case", BAD)
@pytest.mark.parametrize("endpoint", ["producer", "consumer"])
def test_bad_whole_assertion_rejected(tmp_path, case, endpoint):
    bad = mutate(original(), case)
    if endpoint == "producer":
        with pytest.raises(ValueError):
            build(tmp_path, [item(tmp_path, bad)])
    else:
        metadata = carrier_reaction_metadata(item(tmp_path), tmp_path)
        data = snapshot(metadata)
        metadata[FIELD].update(retained(bad[1], CORE))
        with pytest.raises(ValueError):
            consume(tmp_path, data)


@pytest.mark.parametrize(
    "case",
    ["host", "query", "pgdb", "version", "frame", "class", "type", "extra-root", "text", "doctype"],
)
def test_producer_envelope_rejected(tmp_path, case):
    root = original()
    changes = {}
    if case == "host":
        changes["url"] = ROW["entry"]["url"].replace(
            "bf2i-artsymbiocyc.insa-lyon.fr", "example.org"
        )
    elif case == "query":
        root.find("metadata/query").text = "META:OTHER"
    elif case == "pgdb":
        root.find("metadata/PGDB").set("orgid", "ECOLI")
    elif case == "version":
        root.set("ptools-version", "28.0")
    elif case == "frame":
        root[1].set("frameid", "OTHER")
    elif case == "class":
        root[1].set("class", "true")
    elif case == "type":
        root[1].tag = "Protein"
    elif case == "extra-root":
        root.append(copy.deepcopy(root[1]))
    elif case == "text":
        root.text = "bad"
    entry = item(tmp_path, root, **changes)
    if case == "doctype":
        p = tmp_path / entry["path"]
        p.write_bytes(b"<!DOCTYPE ptools-xml []>" + p.read_bytes())
        entry["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
    with pytest.raises(ValueError):
        build(tmp_path, [entry])


def coherent(root, case):
    e = root[1]
    if case == "coefficient":
        e.findall("left")[1][1].text = "3"
    elif case == "carrier-identity":
        p = e.findall("left")[1][0]
        p.set("frameid", "Other-ferredoxins")
        p.set("resource", "getxml?META:Other-ferredoxins")
    elif case == "side-order":
        n = e.findall("right")[0]
        e.remove(n)
        e.insert(8, n)
    elif case == "comment":
        e.find("comment").text += " Additional retained scientific context."
    elif case == "physiological":
        e.find("physiologically-relevant").text = "false"
    elif case == "credit":
        e.find("credits/created/date").text = "2020-03-12"
    elif case == "enzyme":
        n = e.find("enzymatic-reaction/Enzymatic-Reaction/enzyme/Protein")
        n.set("frameid", "CPLX-OTHER")
        n.set("resource", "getxml?META:CPLX-OTHER")
    elif case == "version":
        root.set("ptools-version", "27.1")
        root.find("metadata/PGDB").set("version", "27.1")
    else:
        raise AssertionError(case)
    return root


@pytest.mark.parametrize(
    "case",
    [
        "coefficient",
        "carrier-identity",
        "side-order",
        "comment",
        "physiological",
        "credit",
        "enzyme",
        "version",
    ],
)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
@pytest.mark.parametrize("endpoint", ["producer", "consumer"])
def test_coherent_conflicts_before_selection(tmp_path, case, reverse, selected, endpoint):
    a = item(tmp_path, key="a")
    b = item(
        tmp_path,
        coherent(original(), case),
        key="b",
        version="27.1" if case == "version" else "27.0",
    )
    ma = carrier_reaction_metadata(a, tmp_path)
    mb = carrier_reaction_metadata(b, tmp_path)
    # Each assertion is individually valid, including full derived projections.
    assert consume(tmp_path, snapshot(ma, "a"))[IDENT]["source"] == "a"
    assert consume(tmp_path, snapshot(mb, "b"))[IDENT]["source"] == "b"
    entries = [b, a] if reverse else [a, b]
    control, other = unrelated(tmp_path)
    if endpoint == "producer":
        with pytest.raises(ValueError, match="conflicting whole protein-carrier"):
            build(tmp_path, entries + [control], (IDENT, other) if selected else (other,))
    else:
        data = build(tmp_path, [control], (other,))
        data["sources"].update({x["key"]: ma if x["key"] == "a" else mb for x in entries})
        if selected:
            data["terms"][IDENT] = carrier_reaction_term(ma, "a")[1]
        with pytest.raises(ValueError, match="conflicting whole protein-carrier"):
            consume(tmp_path, data)


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_identical_duplicate_owners_preserve_first_owner(tmp_path, reverse, selected):
    a = item(tmp_path, key="a")
    b = item(tmp_path, key="b")
    control, other = unrelated(tmp_path)
    entries = [b, a] if reverse else [a, b]
    data = build(tmp_path, entries + [control], (IDENT, other) if selected else (other,))
    assert consume(tmp_path, data) == data["terms"]
    if selected:
        assert data["terms"][IDENT]["source"] == entries[0]["key"]
    for e in entries:
        data["sources"][e["key"]] = carrier_reaction_metadata(e, tmp_path)
    assert consume(tmp_path, data) == data["terms"]


@pytest.mark.parametrize(
    "field",
    [
        "label",
        "synonyms",
        "source",
        "kind",
        "wrong-field",
        "missing-slots",
        "slot-order",
        "projection",
        "url",
        "version",
        "attributes",
    ],
)
def test_consumer_projection_or_provenance_tampering(tmp_path, field):
    data = build(tmp_path, [item(tmp_path)])
    m = data["sources"]["mar"]
    n = m[FIELD]
    t = data["terms"][IDENT]
    if field == "label":
        t["label"] = "invented"
    elif field == "synonyms":
        t["synonyms"] = ["invented"]
    elif field == "source":
        t["source"] = "absent"
    elif field == "kind":
        m["kind"] = "metacyc-reaction-xml"
    elif field == "wrong-field":
        m["native_electron_transfer"] = m.pop(FIELD)
    elif field == "missing-slots":
        n.pop("source_slots")
    elif field == "slot-order":
        n["source_slots"] = n["source_slots"][::-1]
    elif field == "projection":
        n["sides"][0]["coefficient"] = 2
    elif field == "url":
        m["url"] = m["url"].replace("META:", "ECOLI:")
    elif field == "version":
        m["version"] = "bad"
    elif field == "attributes":
        n["native_attributes"]["class"] = "true"
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
@pytest.mark.parametrize("typed_present", [False, True])
@pytest.mark.parametrize("ordinary_kind", [False, True])
def test_scope_stripping_cannot_hide_in_unselected_owner(
    tmp_path, reverse, selected, typed_present, ordinary_kind
):
    entry = item(tmp_path)
    control, other = unrelated(tmp_path)
    metadata = carrier_reaction_metadata(entry, tmp_path)
    stripped = {k: v for k, v in metadata.items() if k != FIELD}
    if ordinary_kind:
        stripped["kind"] = "metacyc-reaction-xml"
    else:
        stripped.pop("kind")
    pairs = [("bad", stripped)] + ([("mar", metadata)] if typed_present else [])
    if reverse:
        pairs.reverse()
    data = build(tmp_path, [control], (other,))
    data["sources"].update(pairs)
    if selected:
        data["terms"][IDENT] = carrier_reaction_term(metadata, "mar" if typed_present else "bad")[1]
    with pytest.raises(ValueError, match="complete typed scope"):
        consume(tmp_path, data)
    entries = [{**entry, "key": "bad", "kind": "metacyc-reaction-xml"}] + (
        [entry] if typed_present else []
    )
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="complete typed scope"):
        build(tmp_path, entries + [control], (IDENT, other) if selected else (other,))


def test_local_ec_exception_does_not_change_shared_validator(tmp_path):
    entry = item(tmp_path)
    carrier_reaction_metadata(entry, tmp_path)
    with pytest.raises(ValueError, match="EC context"):
        ancillary(
            original()[1], {"ec-number"}, {n.tag for n in original()[1]} - {"ec-number"}, "META"
        )
    with pytest.raises(ValueError):
        list(
            source_terms(
                "metacyc-reaction-xml",
                tmp_path / entry["path"],
                url=entry["url"],
                version=entry["version"],
            )
        )


def test_structurally_valid_ordinary_reclassification_still_rejected(tmp_path):
    root = original()
    e = root[1]
    for side in [*e.findall("left"), *e.findall("right")]:
        side[0].tag = "Compound"
        side[0].attrib.pop("class", None)
        for coefficient in side.findall("coefficient"):
            side.remove(coefficient)
    e.remove(e.find("ec-number"))
    entry = item(tmp_path, root, kind="metacyc-reaction-xml")
    # The unchanged ordinary reader can parse this synthetic scope reduction.
    # The producer must reject the protected identity before corpus selection.
    assert list(
        source_terms(
            entry["kind"], tmp_path / entry["path"], url=entry["url"], version=entry["version"]
        )
    ) == [(IDENT, "RXN-21320", [])]
    control, other = unrelated(tmp_path)
    with pytest.raises(ValueError, match="complete typed scope"):
        build(tmp_path, [entry, control], (other,))


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_other_valid_typed_owner_conflicts_before_selection(tmp_path, reverse, selected):
    control, other = unrelated(tmp_path)
    root = ET.fromstring((tmp_path / control["path"]).read_bytes())
    for node in root.iter():
        for k, v in list(node.attrib.items()):
            node.set(k, v.replace("PWY0-1352", "RXN-21320"))
        if node.text:
            node.text = node.text.replace("META:PWY0-1352", "META:RXN-21320")
    bad = {
        **control,
        "key": "wrong-type",
        "path": "wrong-type.xml",
        "url": control["url"].replace("PWY0-1352", "RXN-21320"),
    }
    body = ET.tostring(root)
    (tmp_path / bad["path"]).write_bytes(body)
    bad["sha256"] = hashlib.sha256(body).hexdigest()
    bad_metadata = pathway_metadata(bad, tmp_path)
    assert bad_metadata["native_pathway"]["id"] == IDENT
    mar = item(tmp_path)
    entries = [bad, mar] if reverse else [mar, bad]
    with pytest.raises(ValueError, match="complete typed scope"):
        build(tmp_path, entries + [control], (IDENT, other) if selected else (other,))
    data = build(tmp_path, [control], (other,))
    metadata = carrier_reaction_metadata(mar, tmp_path)
    data["sources"].update(
        {e["key"]: bad_metadata if e["key"] == "wrong-type" else metadata for e in entries}
    )
    if selected:
        data["terms"][IDENT] = carrier_reaction_term(metadata, "mar")[1]
    with pytest.raises(ValueError, match="complete typed scope"):
        consume(tmp_path, data)


def test_positive_explicit_one_and_positive_integer_preserved(tmp_path):
    root = original()
    ET.SubElement(root[1].find("left"), "coefficient", {"datatype": "integer"}).text = "1"
    root[1].findall("left")[1][1].text = "7"
    data = build(tmp_path, [item(tmp_path, root)])
    assert consume(tmp_path, data) == data["terms"]
    sides = data["sources"]["mar"][FIELD]["sides"]
    assert (sides[0]["coefficient"], sides[0]["coefficient_explicit"], sides[1]["coefficient"]) == (
        1,
        True,
        7,
    )


@pytest.mark.parametrize("category", ["molecular_activity", "protein", "small_molecule"])
def test_identifier_category_gate(tmp_path, category):
    entry = item(tmp_path)
    control, other = unrelated(tmp_path)
    data = build(tmp_path, [control, entry], (other, IDENT))
    (tmp_path / "authority.json").write_text(json.dumps(data))
    conf = tmp_path / "conf"
    conf.mkdir()
    (conf / "identifier_policy.yaml").write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "namespaces": {"MetaCyc": {"snapshot": "authority.json", "policy": "canonical"}},
                "contextual_labels": [
                    {
                        "namespace": "MetaCyc",
                        "sections": ["reactions"],
                        "record_prefixes": ["MetaCyc"],
                        "reason": "Native reaction label context",
                    }
                ],
            }
        )
    )
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    (records / "one.yaml").write_text(
        yaml.safe_dump(
            {
                "id": other,
                "label": data["terms"][other]["label"],
                "taxa": [],
                "participants": [],
                "reactions": [
                    {"id": IDENT, "label": "source contextual chemistry", "category": category}
                ],
            }
        )
    )
    errors = identifier_errors(tmp_path)
    assert (
        not errors
        if category == "molecular_activity"
        else any("ENTITY_TYPE_MISMATCH" in e for e in errors)
    )
