"""Full native originals and closed identity roles for METHANOGENESIS-PWY."""

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

from pathwaymech.biocyc_methanogenesis import (
    FIELD,
    KIND,
    MATERIAL_ROLES,
    NODE_ROLES,
    PROFILES,
    methanogenesis_metadata,
    methanogenesis_term,
    validate_methanogenesis_metadata,
)
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, corpus_ids

FIXTURES = Path(__file__).parent / "fixtures/methanogenesis_authority"
ENTRIES = json.loads((FIXTURES / "manifest.json").read_text())
STORAGE = json.loads((FIXTURES / "storage.json").read_text())
BY_FRAME = {e["url"].split("META:", 1)[1]: e for e in ENTRIES}
REPRESENTATIVES = [
    "HYDROGEN-MOLECULE",
    "CPLX-381",
    "CPLX-3321",
    "ENZRXN-702",
    "2.1.1.86-RXN",
    "METHANOGENESIS-PWY",
    "CCO-MEMBRANE",
    "MG+2",
    "Formyl-methanofurans",
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
    return methanogenesis_metadata(stage(tmp_path, frame), tmp_path)


def snapshot(meta):
    ident, term = methanogenesis_term(meta, "original")
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
    e = stage(tmp_path, frame)
    m = methanogenesis_metadata(e, tmp_path)
    assert (
        base64.b64decode(m[FIELD]["original_base64"], validate=True)
        == (tmp_path / e["path"]).read_bytes()
    )
    assert len(m[FIELD]["projection"]["slots"]) == len(
        ET.fromstring((tmp_path / e["path"]).read_bytes())[1]
    )
    assert consume(tmp_path, snapshot(m)) == snapshot(m)["terms"]


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
        "metadata_species",
    ],
)
def test_wrong_native_envelope_or_profile_rejected(tmp_path, frame, mutation):
    e = stage(tmp_path, frame)
    root = ET.fromstring((tmp_path / e["path"]).read_bytes())
    if mutation == "query":
        root.find("metadata/query").text = "META:WRONG"
    elif mutation == "version":
        root.find("metadata/PGDB").set("version", "26.5")
    elif mutation == "frame":
        root[1].set("frameid", "WRONG")
    elif mutation == "type":
        root[1].tag = "Gene"
    elif mutation == "class":
        if root[1].get("class") == "true":
            del root[1].attrib["class"]
        else:
            root[1].set("class", "true")
    elif mutation == "slot":
        root[1].remove(root[1][0])
    elif mutation == "detail":
        root[1].set("detail", "low")
    elif mutation == "base":
        root.set("{http://www.w3.org/XML/1998/namespace}base", "https://example.org/WRONG")
    elif mutation == "result_count":
        root.find("metadata/num_results").text = "2"
    else:
        root.find("metadata/PGDB/species").text = "EcoCyc"
    rewrite(tmp_path, e, root)
    with pytest.raises(ValueError):
        methanogenesis_metadata(e, tmp_path)


@pytest.fixture(scope="module")
def embedded_sources():
    examples = {}
    for entry in ENTRIES:
        entity = ET.fromstring(
            gzip.decompress((FIXTURES / STORAGE[entry["path"]]["path"]).read_bytes())
        )[1]
        for n in entity.iter():
            if n is not entity and {"ID", "resource", "frameid", "orgid"} & n.attrib.keys():
                examples.setdefault(n.tag, entry["url"].split("META:", 1)[1])
    return examples


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize("mutation", ["no_frame", "no_identity", "foreign_resource"])
def test_embedded_identity_cannot_disappear(tmp_path, embedded_sources, boundary, mutation):
    for tag, frame in embedded_sources.items():
        e = stage(tmp_path, frame)
        m = methanogenesis_metadata(e, tmp_path)
        root = ET.fromstring((tmp_path / e["path"]).read_bytes())
        n = next(n for n in root[1].iter(tag) if n is not root[1])
        if mutation == "no_frame":
            del n.attrib["frameid"]
        elif mutation == "no_identity":
            for key in ["frameid", "orgid", "ID", "resource"]:
                n.attrib.pop(key, None)
        else:
            n.attrib.pop("ID", None)
            n.set("resource", "getxml?ECOLI:WRONG")
        if boundary == "producer":
            rewrite(tmp_path, e, root)
            with pytest.raises(ValueError):
                methanogenesis_metadata(e, tmp_path)
        else:
            restage(m, root)
            with pytest.raises(ValueError):
                validate_methanogenesis_metadata(m)


@pytest.mark.parametrize("frame", REPRESENTATIVES)
@pytest.mark.parametrize("field", ["label", "entity_type", "source", "label_kind"])
def test_term_tampering_rejected(tmp_path, frame, field):
    s = snapshot(metadata(tmp_path, frame))
    next(iter(s["terms"].values()))[field] = "wrong"
    with pytest.raises(ValueError):
        consume(tmp_path, s)


@pytest.mark.parametrize("frame", ["MG+2", "MN+2", "NA+"])
@pytest.mark.parametrize("replacement", ["%2B", "%2b", " ", "%20"])
def test_actual_charged_request_is_not_normalized(tmp_path, frame, replacement):
    e = stage(tmp_path, frame)
    e["url"] = e["url"].replace("+", replacement)
    with pytest.raises(ValueError):
        methanogenesis_metadata(e, tmp_path)


@pytest.mark.parametrize("frame", ["CPLX-3321", "CPLX-581", "CPLX-601", "CPLX-622", "CPLX-641"])
def test_unnamed_homomer_name_is_exact_sole_activity(tmp_path, frame):
    e = stage(tmp_path, frame)
    m = methanogenesis_metadata(e, tmp_path)
    root = ET.fromstring((tmp_path / e["path"]).read_bytes())
    assert m[FIELD]["projection"]["label_origin"] == "sole_native_homomer_activity_name"
    node = root[1].find("catalyzes/Enzymatic-Reaction/enzyme/Protein")
    node.set("frameid", "WRONG")
    node.set("resource", "#META:WRONG")
    restage(m, root)
    with pytest.raises(ValueError):
        validate_methanogenesis_metadata(m)


def test_unnamed_heteromer_is_only_frame_label(tmp_path):
    m = metadata(tmp_path, "CPLX-381")
    assert methanogenesis_term(m, "x")[1]["label"] == "CPLX-381"
    assert m[FIELD]["projection"]["label_origin"] == "native_frame_id"


def test_material_classes_and_transport_remain_exact(tmp_path):
    for frame in ["FORMYLMETHANOFURAN-DEHYDROGENASE-RXN", "METHELENE-THMPT-OXI-RXN"]:
        e = stage(tmp_path, frame)
        m = methanogenesis_metadata(e, tmp_path)
        root = ET.fromstring((tmp_path / e["path"]).read_bytes())
        node = next(
            n
            for side in ["left", "right"]
            for wrapper in root[1].findall(side)
            for n in wrapper
            if n.get("frameid") in MATERIAL_ROLES and MATERIAL_ROLES[n.get("frameid")]["is_class"]
        )
        del node.attrib["class"]
        restage(m, root)
        with pytest.raises(ValueError):
            validate_methanogenesis_metadata(m)
    m = metadata(tmp_path, "2.1.1.86-RXN")
    sides = m[FIELD]["projection"]["sides"]
    assert len(sides["left"]) == len(sides["right"]) == 3
    assert all(x["compartment"] == "MetaCyc:CCO-IN" for x in sides["left"])
    assert next(x for x in sides["left"] if x["material"] == "MetaCyc:NA+")["coefficient"] == 2
    sodium = next(x for x in sides["right"] if x["material"] == "MetaCyc:NA+")
    assert sodium["coefficient"] == 2 and sodium["compartment"] == "MetaCyc:CCO-OUT"
    assert all(x["compartment"] == "MetaCyc:CCO-IN" for x in sides["right"] if x is not sodium)


@pytest.mark.parametrize("frame", REPRESENTATIVES)
@pytest.mark.parametrize("request_form", ["bare", "id", "object"])
def test_legacy_owner_downgrade_rejected_before_selection(tmp_path, frame, request_form):
    e = stage(tmp_path, frame)
    e["kind"] = "metacyc-html"
    if request_form != "bare":
        e["url"] = e["url"].replace("getxml?META:", "getxml?" + request_form + "=META:")
    p = tmp_path / "manifest.json"
    p.write_text(json.dumps([e]))
    records = tmp_path / "records"
    records.mkdir()
    (records / "a.yaml").write_text("id: MetaCyc:UNRELATED\n")
    with pytest.raises(ValueError):
        build_snapshot(p, records, tmp_path)


def test_reference_only_ids_are_not_builder_selection(tmp_path):
    (tmp_path / "a.yaml").write_text(
        yaml.safe_dump(
            {"id": "MetaCyc:METHANOGENESIS-PWY", "references": [{"id": "MetaCyc:ENZRXN-701"}]}
        )
    )
    assert corpus_ids(tmp_path) == {"MetaCyc:METHANOGENESIS-PWY"}


def test_new_profile_and_roles_are_finite():
    assert len(PROFILES) == 92
    assert not {"MetaCyc:Oxidized-ferredoxins", "MetaCyc:Reduced-ferredoxins"} & PROFILES.keys()
    assert NODE_ROLES["native_methanogenesis_activity"] == ("participants", {"molecular_activity"})
    assert KIND == "metacyc-methanogenesis-xml"


def record_consumer(tmp_path, frame):
    meta = metadata(tmp_path, frame)
    value = snapshot(meta)
    ident, term = next(iter(value["terms"].items()))
    section, categories = NODE_ROLES[term["entity_type"]]
    node = {"id": ident, "label": term["label"], "category": sorted(categories)[0]}
    anchor = metadata(tmp_path, "METHANOGENESIS-PWY")
    anchor_id, anchor_term = methanogenesis_term(anchor, "pathway")
    value["sources"]["pathway"] = anchor
    value["terms"][anchor_id] = anchor_term
    record = {
        "id": anchor_id,
        "label": anchor_term["label"],
        "taxa": [],
        "participants": [],
        "reactions": [],
    }
    record[section] = [node]
    (tmp_path / "data/pathways").mkdir(parents=True)
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
                        "sections": [section],
                        "record_prefixes": ["MetaCyc"],
                        "reason": "broad rule test",
                    }
                ],
            }
        )
    )
    return record, node, section


@pytest.mark.parametrize(
    "frame",
    [
        "HYDROGEN-MOLECULE",
        "CPLX-381",
        "CPLX-3321",
        "ENZRXN-702",
        "2.1.1.86-RXN",
        "CCO-MEMBRANE",
        "Formyl-methanofurans",
    ],
)
@pytest.mark.parametrize("bad", ["label", "category", "section"])
def test_broad_namespace_rule_cannot_override_native_role_or_label(tmp_path, frame, bad):
    record, node, section = record_consumer(tmp_path, frame)
    if bad == "label":
        node["label"] = "invented source name"
    elif bad == "category":
        node["category"] = "gene"
    else:
        record[section] = []
        record["reactions" if section == "participants" else "participants"] = [node]
    (tmp_path / "data/pathways/draft.yaml").write_text(yaml.safe_dump(record))
    errors = identifier_errors(tmp_path)
    assert any(
        ("LABEL_MISMATCH" if bad == "label" else "ENTITY_TYPE_MISMATCH") in e for e in errors
    )


@pytest.mark.parametrize(
    "frame",
    [
        "Oxidized-ferredoxins",
        "Reduced-ferredoxins",
        "CCO-CYTOSOL",
        "PWY0-321",
        "ENZRXN-701",
        "METHFORM-PWY",
        "UNKNOWN",
    ],
)
def test_new_kind_cannot_claim_existing_or_contextual_owners(tmp_path, frame):
    e = stage(tmp_path, "HYDROGEN-MOLECULE")
    e["url"] = e["url"].replace("HYDROGEN-MOLECULE", frame)
    with pytest.raises(ValueError, match="outside"):
        methanogenesis_metadata(e, tmp_path)


@pytest.mark.parametrize(
    "query",
    ["META:METHANOGENESIS-PWY", "id=META:METHANOGENESIS-PWY", "object=META:METHANOGENESIS-PWY"],
)
@pytest.mark.parametrize(
    "host",
    [
        "bf2i-artsymbiocyc.insa-lyon.fr",
        "biocyc.org",
        "www.biocyc.org",
        "metacyc.org",
        "www.metacyc.org",
    ],
)
def test_unselected_consumer_request_downgrade_rejected(tmp_path, query, host):
    value = snapshot(metadata(tmp_path, "HYDROGEN-MOLECULE"))
    value["sources"]["bad"] = {
        "url": f"https://{host}/getxml?{query}",
        "version": "27.0",
        "license": "test",
        "sha256": "0" * 64,
    }
    with pytest.raises(ValueError, match="typed source"):
        consume(tmp_path, value)


def test_same_size_wrong_root_membership_rejected(tmp_path):
    e = stage(tmp_path, "METHANOGENESIS-PWY")
    root = ET.fromstring((tmp_path / e["path"]).read_bytes())
    n = root[1].find("reaction-list/Reaction")
    n.set("frameid", "UNRELATED")
    n.set("resource", "getxml?META:UNRELATED")
    rewrite(tmp_path, e, root)
    with pytest.raises(ValueError, match="membership"):
        methanogenesis_metadata(e, tmp_path)


@pytest.mark.parametrize("frame", ["MG+2", "MN+2", "NA+"])
@pytest.mark.parametrize("encoded", ["%2B", "%2b"])
def test_percent_encoded_charged_legacy_request_cannot_hide_owner(tmp_path, frame, encoded):
    value = snapshot(metadata(tmp_path, "HYDROGEN-MOLECULE"))
    value["sources"]["bad"] = {
        "url": "https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?META:" + frame.replace("+", encoded),
        "version": "27.0",
        "license": "test",
        "sha256": "0" * 64,
    }
    with pytest.raises(ValueError, match="typed source"):
        consume(tmp_path, value)
