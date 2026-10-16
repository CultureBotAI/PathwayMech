"""Full native originals and closed identity roles for METH-ACETATE-PWY."""

from __future__ import annotations

import base64
import copy
import gzip
import hashlib
import json
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.biocyc_acetate_methanogenesis import (
    FIELD,
    MATERIAL_ROLES,
    NODE_ROLES,
    PROFILES,
    acetate_methanogenesis_metadata,
    acetate_methanogenesis_term,
)
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, corpus_ids

FIXTURES = Path(__file__).parent / "fixtures/acetate_methanogenesis_authority"
ENTRIES = json.loads((FIXTURES / "manifest.json").read_text())
STORAGE = json.loads((FIXTURES / "storage.json").read_text())
BY_FRAME = {e["url"].split("META:", 1)[1]: e for e in ENTRIES}
REPRESENTATIVES = [
    "ACET",
    "CPD-8",
    "Corrinoids",
    "CoI-Corrinoid-Fe-S-proteins",
    "Methylated-corrinoid-Fe-S-Proteins",
    "CPLX-322",
    "CPLX-441",
    "CPLX-461",
    "PTAMSARC-MONOMER",
    "ENZRXN-481",
    "ACETATEKIN-RXN",
    "METH-ACETATE-PWY",
    "K+",
]


def stage(tmp_path, frame):
    entry = copy.deepcopy(BY_FRAME[frame])
    storage = STORAGE[entry["path"]]
    packed = (FIXTURES / storage["path"]).read_bytes()
    assert len(packed) == storage["compressed_bytes"]
    assert hashlib.sha256(packed).hexdigest() == storage["compressed_sha256"]
    raw = gzip.decompress(packed)
    assert len(raw) == storage["bytes"] and hashlib.sha256(raw).hexdigest() == storage["sha256"]
    p = tmp_path / entry["path"]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(raw)
    return entry


def metadata(tmp_path, frame):
    return acetate_methanogenesis_metadata(stage(tmp_path, frame), tmp_path)


def snapshot(meta):
    ident, term = acetate_methanogenesis_term(meta, "original")
    return {"version": 1, "sources": {"original": meta}, "terms": {ident: term}}


def consume(tmp_path, value):
    p = tmp_path / "authority.json"
    p.write_text(json.dumps(value))
    return _load_authority(p)


def rewrite(tmp_path, entry, root):
    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    (tmp_path / entry["path"]).write_bytes(raw)
    entry["sha256"] = hashlib.sha256(raw).hexdigest()


def restage(meta, root):
    """Update every opaque byte/hash slot; semantic guards must still reject."""
    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    meta["sha256"] = hashlib.sha256(raw).hexdigest()
    native = meta[FIELD]
    native["original_base64"] = base64.b64encode(raw).decode("ascii")
    native["root_attributes"] = dict(root.attrib)
    native["metadata_xml"] = ET.tostring(root.find("metadata"), encoding="unicode")
    native["projection"]["slots"] = [
        {"ordinal": i, "name": n.tag, "xml": ET.tostring(n, encoding="unicode")}
        for i, n in enumerate(root[1], 1)
    ]


@pytest.mark.parametrize("frame", list(BY_FRAME))
def test_complete_original_roundtrip(tmp_path, frame):
    entry = stage(tmp_path, frame)
    meta = acetate_methanogenesis_metadata(entry, tmp_path)
    native = meta[FIELD]
    assert (
        base64.b64decode(native["original_base64"], validate=True)
        == (tmp_path / entry["path"]).read_bytes()
    )
    assert len(native["projection"]["slots"]) == sum(PROFILES[native["id"]]["slots"].values())
    assert consume(tmp_path, snapshot(meta)) == snapshot(meta)["terms"]


@pytest.mark.parametrize("frame", REPRESENTATIVES)
@pytest.mark.parametrize(
    "mutation",
    [
        "query",
        "version",
        "frame",
        "type",
        "class",
        "slot",
        "detail",
        "base",
        "result_count",
        "database_species",
        "duplicate_name",
        "parent",
        "doctype",
    ],
)
def test_wrong_full_original_rejected_at_both_boundaries(tmp_path, frame, mutation):
    entry = stage(tmp_path, frame)
    meta = acetate_methanogenesis_metadata(entry, tmp_path)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    entity = root[1]
    if mutation == "query":
        root.find("metadata/query").text = "META:WRONG"
    elif mutation == "version":
        root.find("metadata/PGDB").set("version", "26.5")
    elif mutation == "frame":
        entity.set("frameid", "WRONG")
    elif mutation == "type":
        entity.tag = "Gene"
    elif mutation == "class":
        if entity.get("class") == "true":
            del entity.attrib["class"]
        else:
            entity.set("class", "true")
    elif mutation == "slot":
        entity.remove(entity[0])
    elif mutation == "detail":
        entity.set("detail", "low")
    elif mutation == "base":
        root.set("{http://www.w3.org/XML/1998/namespace}base", "https://example.org/wrong")
    elif mutation == "result_count":
        root.find("metadata/num_results").text = "2"
    elif mutation == "database_species":
        root.find("metadata/PGDB/species").text = "EcoCyc"
    elif mutation == "duplicate_name":
        ET.SubElement(entity, "common-name", {"datatype": "string"}).text = "invented"
    elif mutation == "parent":
        wrapper = entity.find("parent")
        if wrapper is None:
            wrapper = ET.SubElement(entity, "parent")
            ET.SubElement(wrapper, entity.tag, {"orgid": "META", "class": "true"})
        parent = wrapper[0]
        parent.set("frameid", "Wrong-Parent")
        parent.set("resource", "getxml?META:Wrong-Parent")
    if mutation == "doctype":
        raw = b'<!DOCTYPE ptools-xml [<!ENTITY fake "invented">]>' + ET.tostring(root)
        (tmp_path / entry["path"]).write_bytes(raw)
        entry["sha256"] = hashlib.sha256(raw).hexdigest()
        meta["sha256"] = entry["sha256"]
        meta[FIELD]["original_base64"] = base64.b64encode(raw).decode()
    else:
        rewrite(tmp_path, entry, root)
        restage(meta, root)
    with pytest.raises(ValueError):
        acetate_methanogenesis_metadata(entry, tmp_path)
    with pytest.raises(ValueError):
        consume(tmp_path, snapshot_unchecked(meta))


def snapshot_unchecked(meta):
    """Retain a valid previous term while testing original/metadata guards."""
    native = meta[FIELD]["projection"]
    return {
        "version": 1,
        "sources": {"original": meta},
        "terms": {
            native["id"]: {
                "label": native["label"],
                "synonyms": native["synonyms"],
                "source": "original",
            }
        },
    }


def embedded_representatives():
    found = {}
    for entry in ENTRIES:
        raw = gzip.decompress((FIXTURES / STORAGE[entry["path"]]["path"]).read_bytes())
        root = ET.fromstring(raw)
        for index, node in enumerate(root[1].iter()):
            if index and node.get("frameid"):
                found.setdefault(node.tag, (root[1].get("frameid"), index))
    return sorted((tag, frame, index) for tag, (frame, index) in found.items())


@pytest.mark.parametrize("tag,frame,index", embedded_representatives())
@pytest.mark.parametrize("mutation", ["no_frame", "no_identity", "foreign", "class", "detail"])
def test_each_embedded_object_type_is_checked(tmp_path, tag, frame, index, mutation):
    entry = stage(tmp_path, frame)
    meta = acetate_methanogenesis_metadata(entry, tmp_path)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    node = list(root[1].iter())[index]
    assert node.tag == tag
    if mutation == "no_frame":
        del node.attrib["frameid"]
    elif mutation == "no_identity":
        node.attrib.clear()
    elif mutation == "foreign":
        node.set("ID" if "ID" in node.attrib else "resource", "META:FOREIGN")
    elif mutation == "class":
        node.set("class", "false")
    else:
        node.set("detail", "wrong")
    rewrite(tmp_path, entry, root)
    restage(meta, root)
    with pytest.raises(ValueError):
        acetate_methanogenesis_metadata(entry, tmp_path)
    with pytest.raises(ValueError):
        consume(tmp_path, snapshot_unchecked(meta))


@pytest.mark.parametrize(
    "frame",
    [
        "1.2.7.4-RXN",
        "ACETATEKIN-RXN",
        "ACETYLSYNCLTH-RXN",
        "MTRMBARK-RXN",
        "PHOSACETYLTRANS-RXN",
        "RXN-12908",
        "CPLX-322",
        "CPLX-481",
        "PTAMSARC-MONOMER",
    ],
)
def test_unnamed_objects_keep_frame_without_nested_name_promotion(tmp_path, frame):
    meta = metadata(tmp_path, frame)
    term = acetate_methanogenesis_term(meta, "original")[1]
    assert term["label"] == frame and term["label_kind"] == "source_context"
    assert meta[FIELD]["projection"]["label_origin"] == "native_frame_id"
    assert "common-name" not in PROFILES["MetaCyc:" + frame]["slots"]


@pytest.mark.parametrize(
    "frame", ["CoI-Corrinoid-Fe-S-proteins", "Methylated-corrinoid-Fe-S-Proteins"]
)
def test_corrinoid_protein_classes_cannot_become_physical_complexes(tmp_path, frame):
    meta = metadata(tmp_path, frame)
    term = acetate_methanogenesis_term(meta, "original")[1]
    assert meta[FIELD]["projection"]["is_class"] is True
    assert term["entity_type"] == "native_acetate_methanogenesis_protein_class"
    assert "components" not in meta[FIELD]["projection"]
    bad = snapshot(meta)
    bad["terms"]["MetaCyc:" + frame]["entity_type"] = "native_acetate_methanogenesis_complex"
    with pytest.raises(ValueError):
        consume(tmp_path, bad)


@pytest.mark.parametrize("frame", ["CPLX-322", "CPLX-481"])
def test_incomplete_source_composition_is_explicit_not_invented(tmp_path, frame):
    meta = metadata(tmp_path, frame)
    assert meta[FIELD]["projection"]["components"] == []
    assert acetate_methanogenesis_term(meta, "original")[1]["entity_type"].endswith("_complex")


@pytest.mark.parametrize(
    "frame,mutation",
    [
        ("ACETATEKIN-RXN", "material"),
        ("ACETATEKIN-RXN", "direction"),
        ("ACETATEKIN-RXN", "coefficient"),
        ("MTRMBARK-RXN", "compartment"),
        ("CPLX-441", "component"),
        ("CPLX-461", "component_coefficient"),
        ("ENZRXN-481", "enzyme"),
        ("ENZRXN-19881", "reaction"),
        ("METH-ACETATE-PWY", "member"),
    ],
)
def test_same_slot_count_cannot_change_native_biochemical_scope(tmp_path, frame, mutation):
    entry = stage(tmp_path, frame)
    meta = acetate_methanogenesis_metadata(entry, tmp_path)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    entity = root[1]
    if mutation == "direction":
        entity.find("reaction-direction").text = "PHYSIOL-LEFT-TO-RIGHT"
    elif mutation == "coefficient":
        ET.SubElement(entity.find("left"), "coefficient", {"datatype": "integer"}).text = "2"
    elif mutation == "compartment":
        wrapper = ET.SubElement(entity.find("left"), "compartment")
        ET.SubElement(
            wrapper, "cco", {"orgid": "META", "frameid": "CCO-IN", "resource": "getxml?META:CCO-IN"}
        )
    elif mutation == "component_coefficient":
        coeff = entity.find("component/coefficient")
        assert coeff is not None
        coeff.text = str(int(coeff.text) + 1)
    else:
        path, replacement = {
            "material": ("left/Compound", "ADP"),
            "component": ("component/Protein", "PTAMSARC-MONOMER"),
            "enzyme": ("enzyme/Protein", "CPLX-461"),
            "reaction": ("reaction/Reaction", "ACETATEKIN-RXN"),
            "member": ("reaction-list/Reaction", "ACETATEKIN-RXN"),
        }[mutation]
        node = entity.find(path)
        assert node.get("frameid") != replacement
        node.set("frameid", replacement)
        node.set("resource", "getxml?META:" + replacement)
    rewrite(tmp_path, entry, root)
    restage(meta, root)
    with pytest.raises(ValueError):
        acetate_methanogenesis_metadata(entry, tmp_path)
    with pytest.raises(ValueError):
        consume(tmp_path, snapshot_unchecked(meta))


@pytest.mark.parametrize("frame", ["CA+2", "CO+2", "K+", "NI+2", "ZN+2"])
@pytest.mark.parametrize("replacement", ["%2B", "%2b", " ", "%20"])
def test_typed_acquisition_preserves_literal_charged_request(tmp_path, frame, replacement):
    entry = stage(tmp_path, frame)
    entry["url"] = entry["url"].replace("+", replacement)
    with pytest.raises(ValueError):
        acetate_methanogenesis_metadata(entry, tmp_path)


@pytest.mark.parametrize(
    "query",
    [
        "META:K+",
        "META:K%2B",
        "META:K%2b",
        "META%3AK%2B",
        "id=META:K+",
        "id=META:K%2B",
        "object=META:K%2B",
        "id=K%2B",
        "META:PTAMSARC-MONOMER",
        "id=META:PTAMSARC-MONOMER",
    ],
)
@pytest.mark.parametrize("host", ["bf2i-artsymbiocyc.insa-lyon.fr", "biocyc.org"])
def test_unselected_downgraded_owner_rejected_by_producer_and_consumer(tmp_path, query, host):
    good = stage(tmp_path, "ACET")
    old = {
        **good,
        "key": "legacy",
        "kind": "metacyc-compounds",
        "url": f"https://{host}/getxml?{query}",
    }
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([good, old]))
    records = tmp_path / "records"
    records.mkdir()
    (records / "one.yaml").write_text("id: MetaCyc:ACET\n")
    with pytest.raises(ValueError, match="typed source"):
        build_snapshot(manifest, records, tmp_path)
    meta = acetate_methanogenesis_metadata(good, tmp_path)
    value = snapshot(meta)
    value["sources"]["legacy"] = {k: old[k] for k in ("url", "version", "sha256", "license")}
    with pytest.raises(ValueError, match="typed source"):
        consume(tmp_path, value)


@pytest.mark.parametrize("query", ["note=META:K%2B", "META:K%2B-suffix", "id=META:unrelated"])
def test_unrelated_request_values_are_not_profile_claims(tmp_path, query):
    from pathwaymech.biocyc_acetate_methanogenesis import validate_acetate_methanogenesis_assertions

    validate_acetate_methanogenesis_assertions(
        {"unrelated": {"url": "https://biocyc.org/getxml?" + query}}, []
    )


@pytest.mark.parametrize("field", ["label", "entity_type", "label_kind", "source"])
def test_term_projection_cannot_be_forged(tmp_path, field):
    value = snapshot(metadata(tmp_path, "PTAMSARC-MONOMER"))
    value["terms"]["MetaCyc:PTAMSARC-MONOMER"][field] = "invented"
    with pytest.raises(ValueError):
        consume(tmp_path, value)


@pytest.mark.parametrize(
    "frame",
    [
        "ACET",
        "Corrinoids",
        "CoI-Corrinoid-Fe-S-proteins",
        "CPLX-322",
        "PTAMSARC-MONOMER",
        "ENZRXN-481",
        "MTRMBARK-RXN",
    ],
)
@pytest.mark.parametrize("bad", [None, "label", "category", "section"])
def test_record_consumer_enforces_native_role_before_contextual_labels(tmp_path, frame, bad):
    meta = metadata(tmp_path, frame)
    value = snapshot(meta)
    ident, term = next(iter(value["terms"].items()))
    section, categories = NODE_ROLES[term["entity_type"]]
    node = {"id": ident, "label": term["label"], "category": sorted(categories)[0]}
    anchor = metadata(tmp_path, "METH-ACETATE-PWY")
    anchor_id, anchor_term = acetate_methanogenesis_term(anchor, "pathway")
    value["sources"]["pathway"] = anchor
    value["terms"][anchor_id] = anchor_term
    record = {
        "id": anchor_id,
        "label": anchor_term["label"],
        "taxa": [],
        "participants": [],
        "reactions": [],
    }
    record[section].append(node)
    if bad == "label":
        node["label"] = "invented contextual name"
    elif bad == "category":
        node["category"] = "gene"
    elif bad == "section":
        record[section] = []
        record["participants" if section == "reactions" else "reactions"].append(node)
    (tmp_path / "data/pathways").mkdir(parents=True)
    (tmp_path / "data/pathways/one.yaml").write_text(yaml.safe_dump(record))
    (tmp_path / "authority.json").write_text(json.dumps(value))
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "namespaces": {
                    "MetaCyc": {"snapshot": "authority.json", "policy": "canonical_or_synonym"}
                },
                "contextual_labels": [
                    {
                        "namespace": "MetaCyc",
                        "sections": ["participants", "reactions"],
                        "record_prefixes": ["MetaCyc"],
                        "reason": "adversarial broad rule",
                    }
                ],
            }
        )
    )
    errors = identifier_errors(tmp_path)
    if bad:
        assert errors and any("MISMATCH" in error for error in errors)
    else:
        assert errors == []


def test_reference_only_and_old_owners_do_not_expand_finite_profiles(tmp_path):
    assert len(PROFILES) == 52
    assert len(MATERIAL_ROLES) == 19
    for ident in ["MetaCyc:ORG-5913", "MetaCyc:ACKMSARC", "MetaCyc:ATP", "MetaCyc:CCO-MEMBRANE"]:
        assert ident not in PROFILES
    (tmp_path / "one.yaml").write_text(
        yaml.safe_dump(
            {
                "id": "MetaCyc:METH-ACETATE-PWY",
                "references": [{"id": "MetaCyc:ORG-5913"}, {"id": "NCBITaxon:28890"}],
            }
        )
    )
    assert corpus_ids(tmp_path) == {"MetaCyc:METH-ACETATE-PWY"}


def test_duplicate_source_key_is_rejected(tmp_path):
    entry = stage(tmp_path, "ACET")
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([entry, entry]))
    records = tmp_path / "records"
    records.mkdir()
    (records / "one.yaml").write_text("id: MetaCyc:ACET\n")
    with pytest.raises(ValueError, match="duplicate source key"):
        build_snapshot(manifest, records, tmp_path)


def test_conflicting_complete_originals_fail_before_selection(tmp_path):
    first = stage(tmp_path, "ACET")
    second = {**first, "key": "second", "path": "second.xml"}
    root = ET.fromstring((tmp_path / first["path"]).read_bytes())
    root[1].find("common-name").text = "a different source common name"
    rewrite(tmp_path, second, root)
    # A name read from original bytes is not rejected by a curated-name allowlist.
    a = acetate_methanogenesis_metadata(first, tmp_path)
    b = acetate_methanogenesis_metadata(second, tmp_path)
    assert a[FIELD]["projection"]["label"] != b[FIELD]["projection"]["label"]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([first, second]))
    records = tmp_path / "records"
    records.mkdir()
    (records / "one.yaml").write_text("id: MetaCyc:unselected\n")
    with pytest.raises(ValueError, match="conflicting complete native identity"):
        build_snapshot(manifest, records, tmp_path)
    value = snapshot(a)
    value["sources"]["second"] = b
    with pytest.raises(ValueError, match="conflicting complete native identity"):
        consume(tmp_path, value)


@pytest.mark.parametrize("mutation", ["kind", "hash", "path", "version", "frame"])
def test_source_manifest_provenance_is_checked_before_projection(tmp_path, mutation):
    entry = stage(tmp_path, "ACET")
    if mutation == "kind":
        entry["kind"] = "metacyc-methanogenesis-xml"
    elif mutation == "hash":
        entry["sha256"] = "0" * 64
    elif mutation == "path":
        entry["path"] = "../escape.xml"
    elif mutation == "version":
        entry["version"] = "26.5"
    else:
        entry["url"] = entry["url"].replace("META:ACET", "META:ATP")
    with pytest.raises(ValueError):
        acetate_methanogenesis_metadata(entry, tmp_path)
