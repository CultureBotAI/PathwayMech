"""Complete PWY0-1477 native sources, request scope and typed graph roles."""

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

from pathwaymech.biocyc_ethanolamine import (
    FIELD,
    NODE_ROLES,
    PROFILES,
    ethanolamine_metadata,
    ethanolamine_term,
    validate_ethanolamine_assertions,
)
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, corpus_ids

FIXTURES = Path(__file__).parent / "fixtures/ethanolamine_authority"
ENTRIES = json.loads((FIXTURES / "manifest.json").read_text())
STORAGE = json.loads((FIXTURES / "storage.json").read_text())
BY_ID = {
    entry["url"].split("?", 1)[1].replace("META:", "MetaCyc:").replace("ECOLI:", "EcoCyc:"): entry
    for entry in ENTRIES
}
REPRESENTATIVES = [
    "MetaCyc:GDP",
    "MetaCyc:FE+2",
    "MetaCyc:Reduced-Flavoproteins",
    "MetaCyc:ETHAMLY-CPLX",
    "MetaCyc:STM2468-MONOMER",
    "MetaCyc:CPLX-9275",
    "MetaCyc:ETHAMLY-ENZRXN",
    "MetaCyc:ETHAMLY-RXN",
    "MetaCyc:RXN-19336",
    "MetaCyc:PWY0-1477",
    "EcoCyc:ETHAMLY-CPLX",
    "EcoCyc:G7281-MONOMER",
    "EcoCyc:CCI-CYTOSOL-GN",
]


def stage(tmp_path, ident):
    entry = copy.deepcopy(BY_ID[ident])
    storage = STORAGE[entry["path"]]
    packed = (FIXTURES / storage["path"]).read_bytes()
    assert len(packed) == storage["compressed_bytes"]
    assert hashlib.sha256(packed).hexdigest() == storage["compressed_sha256"]
    raw = gzip.decompress(packed)
    assert len(raw) == storage["bytes"]
    assert hashlib.sha256(raw).hexdigest() == storage["sha256"] == entry["sha256"]
    (tmp_path / entry["path"]).write_bytes(raw)
    return entry


def metadata(tmp_path, ident):
    return ethanolamine_metadata(stage(tmp_path, ident), tmp_path)


def snapshot(meta):
    ident, term = ethanolamine_term(meta, "original")
    return {"version": 1, "sources": {"original": meta}, "terms": {ident: term}}


def consume(tmp_path, value):
    path = tmp_path / "authority.json"
    path.write_text(json.dumps(value))
    return _load_authority(path)


def mutate_original(tmp_path, entry, meta, root):
    """Re-pin bytes and opaque projections; original semantic checks must reject."""
    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    (tmp_path / entry["path"]).write_bytes(raw)
    entry["sha256"] = hashlib.sha256(raw).hexdigest()
    meta["sha256"] = entry["sha256"]
    native = meta[FIELD]
    native["original_base64"] = base64.b64encode(raw).decode()
    native["root_attributes"] = dict(root.attrib)
    native["metadata_xml"] = ET.tostring(root.find("metadata"), encoding="unicode")
    native["projection"]["slots"] = [
        {"ordinal": i, "name": node.tag, "xml": ET.tostring(node, encoding="unicode")}
        for i, node in enumerate(root[1], 1)
    ]


def rejected_both(tmp_path, entry, value):
    with pytest.raises(ValueError):
        ethanolamine_metadata(entry, tmp_path)
    with pytest.raises(ValueError):
        consume(tmp_path, value)


@pytest.mark.parametrize("ident", list(BY_ID))
def test_complete_original_roundtrip(tmp_path, ident):
    entry = stage(tmp_path, ident)
    meta = ethanolamine_metadata(entry, tmp_path)
    native = meta[FIELD]
    assert (
        base64.b64decode(native["original_base64"], validate=True)
        == (tmp_path / entry["path"]).read_bytes()
    )
    assert len(native["projection"]["slots"]) == sum(PROFILES[ident]["slots"].values())
    assert consume(tmp_path, snapshot(meta)) == snapshot(meta)["terms"]


@pytest.mark.parametrize("ident", REPRESENTATIVES)
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
        "count",
        "species",
        "parent",
        "duplicate_name",
        "doctype",
    ],
)
def test_full_identity_mutations_fail_at_both_boundaries(tmp_path, ident, mutation):
    entry = stage(tmp_path, ident)
    meta = ethanolamine_metadata(entry, tmp_path)
    value = snapshot(meta)
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
        entity.set("class", "false")
    elif mutation == "slot":
        entity.remove(entity[0])
    elif mutation == "detail":
        entity.set("detail", "low")
    elif mutation == "base":
        root.set("{http://www.w3.org/XML/1998/namespace}base", "https://example.org/wrong")
    elif mutation == "count":
        root.find("metadata/num_results").text = "2"
    elif mutation == "species":
        root.find("metadata/PGDB/species").text = "wrong database species"
    elif mutation == "parent":
        wrapper = entity.find("parent")
        if wrapper is None:
            wrapper = ET.SubElement(entity, "parent")
            ET.SubElement(wrapper, entity.tag, {"orgid": entity.get("orgid"), "class": "true"})
        parent = wrapper[0]
        parent.set("frameid", "Wrong-Parent")
        parent.set("resource", "getxml?" + entity.get("orgid") + ":Wrong-Parent")
    elif mutation == "duplicate_name":
        ET.SubElement(entity, "common-name", {"datatype": "string"}).text = "invented"
    mutate_original(tmp_path, entry, meta, root)
    if mutation == "doctype":
        raw = (
            b'<!DOCTYPE ptools-xml [<!ENTITY fake "invented">]>'
            + (tmp_path / entry["path"]).read_bytes()
        )
        (tmp_path / entry["path"]).write_bytes(raw)
        entry["sha256"] = meta["sha256"] = hashlib.sha256(raw).hexdigest()
        meta[FIELD]["original_base64"] = base64.b64encode(raw).decode()
    rejected_both(tmp_path, entry, value)


def embedded_representatives():
    found = {}
    for ident, entry in BY_ID.items():
        root = ET.fromstring(
            gzip.decompress((FIXTURES / STORAGE[entry["path"]]["path"]).read_bytes())
        )
        for index, node in enumerate(root[1].iter()):
            if index and node.get("frameid"):
                found.setdefault(node.tag, (ident, index))
    return sorted((tag, ident, index) for tag, (ident, index) in found.items())


@pytest.mark.parametrize("tag,ident,index", embedded_representatives())
@pytest.mark.parametrize("mutation", ["no_frame", "no_identity", "foreign", "class", "detail"])
def test_every_embedded_native_type_is_checked(tmp_path, tag, ident, index, mutation):
    entry = stage(tmp_path, ident)
    meta = ethanolamine_metadata(entry, tmp_path)
    value = snapshot(meta)
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
    mutate_original(tmp_path, entry, meta, root)
    rejected_both(tmp_path, entry, value)


@pytest.mark.parametrize(
    "ident",
    [
        "MetaCyc:ETHAMLY-CPLX",
        "EcoCyc:ETHAMLY-CPLX",
        "MetaCyc:STM2468-MONOMER",
        "MetaCyc:ETHAMLY-RXN",
    ],
)
def test_unnamed_objects_keep_frame_and_distinct_roles(tmp_path, ident):
    meta = metadata(tmp_path, ident)
    term = ethanolamine_term(meta, "original")[1]
    assert term["label"] == ident.split(":", 1)[1]
    assert term["label_kind"] == "source_context"
    assert meta[FIELD]["projection"]["label_origin"] == "native_frame_id"
    assert term["entity_type"].endswith(
        "_complex" if "CPLX" in ident else "_protein" if "MONOMER" in ident else "_reaction"
    )


def test_real_gdp_acronym_is_direct_source_name(tmp_path):
    meta = metadata(tmp_path, "MetaCyc:GDP")
    assert meta[FIELD]["projection"]["label_origin"] == "direct_common_name"
    assert ethanolamine_term(meta, "original")[1]["label"] == "GDP"
    assert ethanolamine_term(meta, "original")[1]["label_kind"] == "canonical"


def test_source_equations_components_and_ordering_are_not_inferred(tmp_path):
    eal = metadata(tmp_path, "MetaCyc:ETHAMLY-CPLX")[FIELD]["projection"]
    assert eal["components"] == [
        {"id": "MetaCyc:EUTB-MONOMER", "coefficient": 6},
        {"id": "MetaCyc:EUTC-MONOMER", "coefficient": 6},
    ]
    eut_t = metadata(tmp_path, "MetaCyc:CPLX-9275")[FIELD]["projection"]
    assert eut_t["components"] == [{"id": "MetaCyc:STM2467-MONOMER", "coefficient": None}]
    reaction = metadata(tmp_path, "MetaCyc:RXN-19336")[FIELD]["projection"]
    proteins = [
        r for side in reaction["sides"].values() for r in side if r["native_type"] == "Protein"
    ]
    assert len(proteins) == 2 and all(r["is_class"] for r in proteins)
    assert all(r["compartment"] is None for side in reaction["sides"].values() for r in side)
    root = metadata(tmp_path, "MetaCyc:PWY0-1477")[FIELD]["projection"]
    assert len(root["reaction_list"]) == 5 and len(root["reaction_ordering"]) == 4
    assert "MetaCyc:RXN-19336" not in root["reaction_list"]
    assert (
        metadata(tmp_path, "MetaCyc:ETHAMLY-RXN")[FIELD]["projection"]["reaction_direction"]
        == "LEFT-TO-RIGHT"
    )


@pytest.mark.parametrize(
    "ident,mutation",
    [
        ("MetaCyc:ETHAMLY-RXN", "direction"),
        ("MetaCyc:ETHAMLY-RXN", "material"),
        ("MetaCyc:RXN-19336", "coefficient"),
        ("MetaCyc:RXN-19336", "material_class"),
        ("MetaCyc:ETHAMLY-RXN", "compartment"),
        ("MetaCyc:ETHAMLY-CPLX", "component_coefficient"),
        ("EcoCyc:ETHAMLY-CPLX", "component"),
        ("MetaCyc:CPLX-9275", "omitted_coefficient"),
        ("MetaCyc:ETHAMLY-ENZRXN", "enzyme"),
        ("MetaCyc:ETHAMLY-ENZRXN", "reaction"),
        ("MetaCyc:PWY0-1477", "member"),
        ("MetaCyc:PWY0-1477", "ordering"),
    ],
)
def test_equal_slot_count_cannot_change_biochemical_scope(tmp_path, ident, mutation):
    entry = stage(tmp_path, ident)
    meta = ethanolamine_metadata(entry, tmp_path)
    value = snapshot(meta)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    entity = root[1]
    if mutation == "direction":
        entity.find("reaction-direction").text = "REVERSIBLE"
    elif mutation in {"coefficient", "component_coefficient"}:
        coefficient = next(n for n in entity.iter("coefficient"))
        coefficient.text = str(int(coefficient.text) + 1)
    elif mutation == "omitted_coefficient":
        ET.SubElement(entity.find("component"), "coefficient", {"datatype": "integer"}).text = "2"
    elif mutation == "compartment":
        ET.SubElement(entity.find("left"), "compartment")
    elif mutation == "material_class":
        del entity.find("left/Protein").attrib["class"]
    else:
        path, replacement = {
            "material": ("left/Compound", "ACETALD"),
            "component": ("component/Protein", "G7281-MONOMER"),
            "enzyme": ("enzyme/Protein", "STM2467-MONOMER"),
            "reaction": ("reaction/Reaction", "ALCOHOL-DEHYDROG-RXN"),
            "member": ("reaction-list/Reaction", "RXN-19336"),
            "ordering": ("reaction-ordering/predecessor-reactions/Reaction", "RXN-19336"),
        }[mutation]
        node = entity.find(path)
        assert node.get("frameid") != replacement
        node.set("frameid", replacement)
        node.set("resource", "getxml?" + entity.get("orgid") + ":" + replacement)
    mutate_original(tmp_path, entry, meta, root)
    rejected_both(tmp_path, entry, value)


@pytest.mark.parametrize("replacement", ["%2B", "%2b", " ", "%20"])
def test_charged_acquisition_is_exact_literal_request(tmp_path, replacement):
    entry = stage(tmp_path, "MetaCyc:FE+2")
    entry["url"] = entry["url"].replace("+", replacement)
    with pytest.raises(ValueError):
        ethanolamine_metadata(entry, tmp_path)


@pytest.mark.parametrize(
    "query",
    [
        "META:FE+2",
        "META:FE%2B2",
        "META%3AFE%2B2",
        "id=META:FE+2",
        "object=META:FE%2b2",
        "id=FE%2B2",
        "ECOLI:ETHAMLY-CPLX",
        "id=ECOLI:ETHAMLY-CPLX",
    ],
)
@pytest.mark.parametrize(
    "host", ["bf2i-artsymbiocyc.insa-lyon.fr", "biocyc.org", "ecocyc.org", "www.ecocyc.org"]
)
def test_unselected_wrong_kind_fails_before_source_selection(tmp_path, query, host):
    good = stage(tmp_path, "MetaCyc:GDP")
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
    (records / "one.yaml").write_text("id: MetaCyc:GDP\n")
    with pytest.raises(ValueError, match="typed source"):
        build_snapshot(manifest, records, tmp_path)
    value = snapshot(ethanolamine_metadata(good, tmp_path))
    value["sources"]["legacy"] = {k: old[k] for k in ("url", "version", "sha256", "license")}
    with pytest.raises(ValueError, match="typed source"):
        consume(tmp_path, value)


@pytest.mark.parametrize("query", ["note=META:FE%2B2", "META:FE%2B2-suffix", "id=META:unrelated"])
def test_unrelated_query_does_not_claim_native_identity(query):
    validate_ethanolamine_assertions(
        {"unrelated": {"url": "https://biocyc.org/getxml?" + query}}, []
    )


@pytest.mark.parametrize("mutation", ["kind", "hash", "path", "version", "pgdb", "id_query"])
def test_source_manifest_scope_is_closed(tmp_path, mutation):
    entry = stage(tmp_path, "EcoCyc:ETHAMLY-CPLX")
    if mutation == "kind":
        entry["kind"] = "metacyc-ethanolamine-xml"
    elif mutation == "hash":
        entry["sha256"] = "0" * 64
    elif mutation == "path":
        entry["path"] = "../escape.xml"
    elif mutation == "version":
        entry["version"] = "26.5"
    elif mutation == "pgdb":
        entry["url"] = entry["url"].replace("ECOLI:", "META:")
    else:
        entry["url"] = entry["url"].replace("?ECOLI:", "?id=ECOLI:")
    with pytest.raises(ValueError):
        ethanolamine_metadata(entry, tmp_path)


@pytest.mark.parametrize("mutation", ["strain", "taxon", "missing_db_slot"])
def test_ecoli_complete_database_envelope(tmp_path, mutation):
    entry = stage(tmp_path, "EcoCyc:G7281-MONOMER")
    meta = ethanolamine_metadata(entry, tmp_path)
    value = snapshot(meta)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    db = root.find("metadata/PGDB")
    if mutation == "strain":
        db.find("strain").text = "K-12"
    elif mutation == "taxon":
        db.find("dblink/dblink-oid").text = "83333"
    else:
        db.remove(db.find("dblink"))
    mutate_original(tmp_path, entry, meta, root)
    rejected_both(tmp_path, entry, value)


@pytest.mark.parametrize("field", ["label", "entity_type", "label_kind", "source"])
def test_forged_term_projection_fails(tmp_path, field):
    value = snapshot(metadata(tmp_path, "MetaCyc:STM2468-MONOMER"))
    value["terms"]["MetaCyc:STM2468-MONOMER"][field] = "invented"
    with pytest.raises(ValueError):
        consume(tmp_path, value)


@pytest.mark.parametrize(
    "ident",
    [
        "MetaCyc:GDP",
        "MetaCyc:Reduced-Flavoproteins",
        "MetaCyc:ETHAMLY-CPLX",
        "MetaCyc:STM2468-MONOMER",
        "MetaCyc:ETHAMLY-ENZRXN",
        "MetaCyc:ETHAMLY-RXN",
        "EcoCyc:CCI-CYTOSOL-GN",
    ],
)
@pytest.mark.parametrize("bad", [None, "label", "category", "section"])
def test_typed_roles_precede_contextual_label_exceptions(tmp_path, ident, bad):
    value = snapshot(metadata(tmp_path, ident))
    term = value["terms"][ident]
    section, categories = NODE_ROLES[term["entity_type"]]
    node = {"id": ident, "label": term["label"], "category": sorted(categories)[0]}
    anchor = metadata(tmp_path, "MetaCyc:PWY0-1477")
    anchor_id, anchor_term = ethanolamine_term(anchor, "pathway")
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
        node["label"] = "invented contextual label"
    elif bad == "category":
        node["category"] = "gene"
    elif bad == "section":
        record[section] = []
        record["participants" if section == "reactions" else "reactions"].append(node)
    (tmp_path / "data/pathways").mkdir(parents=True)
    (tmp_path / "data/pathways/one.yaml").write_text(yaml.safe_dump(record))
    (tmp_path / "authority.json").write_text(json.dumps(value))
    (tmp_path / "conf").mkdir()
    namespaces = {
        prefix: {"snapshot": "authority.json", "policy": "canonical_or_synonym"}
        for prefix in {"MetaCyc", ident.split(":", 1)[0]}
    }
    (tmp_path / "conf/identifier_policy.yaml").write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "namespaces": namespaces,
                "contextual_labels": [
                    {
                        "namespace": prefix,
                        "sections": ["participants", "reactions"],
                        "record_prefixes": ["MetaCyc"],
                        "reason": "adversarial broad rule",
                    }
                    for prefix in namespaces
                ],
            }
        )
    )
    errors = identifier_errors(tmp_path)
    if bad:
        assert errors and any("MISMATCH" in error for error in errors)
    else:
        assert errors == []


def test_complete_builder_replay_selects_exact_scope(tmp_path):
    entries = [stage(tmp_path, ident) for ident in BY_ID]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "records"
    records.mkdir()
    (records / "one.yaml").write_text(
        yaml.safe_dump(
            {
                "id": "MetaCyc:PWY0-1477",
                "participants": [{"id": ident} for ident in BY_ID if ident != "MetaCyc:PWY0-1477"],
            }
        )
    )
    result = build_snapshot(manifest, records, tmp_path)
    assert set(result["terms"]) == set(PROFILES) == set(BY_ID)
    assert len(result["sources"]) == 63
    assert consume(tmp_path, result) == result["terms"]


def test_duplicate_and_conflicting_originals_fail_before_selection(tmp_path):
    first = stage(tmp_path, "MetaCyc:GDP")
    manifest = tmp_path / "manifest.json"
    records = tmp_path / "records"
    records.mkdir()
    (records / "one.yaml").write_text("id: MetaCyc:unselected\n")
    manifest.write_text(json.dumps([first, first]))
    with pytest.raises(ValueError, match="duplicate source key"):
        build_snapshot(manifest, records, tmp_path)
    second = {**first, "key": "second", "path": "second.xml"}
    root = ET.fromstring((tmp_path / first["path"]).read_bytes())
    root[1].find("common-name").text = "different issuing source name"
    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    (tmp_path / second["path"]).write_bytes(raw)
    second["sha256"] = hashlib.sha256(raw).hexdigest()
    a = ethanolamine_metadata(first, tmp_path)
    b = ethanolamine_metadata(second, tmp_path)
    assert a[FIELD]["projection"]["label"] != b[FIELD]["projection"]["label"]
    manifest.write_text(json.dumps([first, second]))
    with pytest.raises(ValueError, match="conflicting complete native identity"):
        build_snapshot(manifest, records, tmp_path)
    value = snapshot(a)
    value["sources"]["second"] = b
    with pytest.raises(ValueError, match="conflicting complete native identity"):
        consume(tmp_path, value)


def test_prior_owners_and_reference_only_ids_do_not_expand_scope(tmp_path):
    assert len(PROFILES) == 63
    for ident in [
        "MetaCyc:ATP",
        "MetaCyc:ACETATEKIN-RXN",
        "MetaCyc:PHOSACETYLTRANS-RXN",
        "MetaCyc:G7285-MONOMER",
        "MetaCyc:ENZRXN-26159",
    ]:
        assert ident not in PROFILES
    (tmp_path / "one.yaml").write_text(
        yaml.safe_dump({"id": "MetaCyc:PWY0-1477", "references": [{"id": "MetaCyc:ENZRXN-26159"}]})
    )
    assert corpus_ids(tmp_path) == {"MetaCyc:PWY0-1477"}


@pytest.mark.parametrize("host", ["ecocyc.org", "www.ecocyc.org"])
@pytest.mark.parametrize("scheme", ["http", "https"])
@pytest.mark.parametrize("query", ["object=ETHAMLY-CPLX", "id=ETHAMLY-CPLX"])
def test_unselected_ecocyc_image_request_cannot_downgrade_owner(tmp_path, host, scheme, query):
    good = stage(tmp_path, "MetaCyc:GDP")
    legacy = {
        **good,
        "key": "legacy",
        "kind": "metacyc-compounds",
        "url": f"{scheme}://{host}/ECOLI/NEW-IMAGE?{query}",
    }
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([good, legacy]))
    records = tmp_path / "records"
    records.mkdir()
    (records / "one.yaml").write_text("id: MetaCyc:GDP\n")
    with pytest.raises(ValueError, match="typed source"):
        build_snapshot(manifest, records, tmp_path)
    value = snapshot(ethanolamine_metadata(good, tmp_path))
    value["sources"]["legacy"] = {
        key: legacy[key] for key in ("url", "version", "sha256", "license")
    }
    with pytest.raises(ValueError, match="typed source"):
        consume(tmp_path, value)


@pytest.mark.parametrize("host", ["ecocyc.org", "www.ecocyc.org"])
def test_guard_host_recognition_does_not_broaden_acquisition(tmp_path, host):
    entry = stage(tmp_path, "EcoCyc:ETHAMLY-CPLX")
    entry["url"] = entry["url"].replace("bf2i-artsymbiocyc.insa-lyon.fr", host)
    with pytest.raises(ValueError, match="exact acquired"):
        ethanolamine_metadata(entry, tmp_path)
