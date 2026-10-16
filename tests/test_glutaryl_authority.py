"""Whole issuing originals and adversarial boundaries for native PWY-5177."""
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

from pathwaymech.biocyc_glutaryl import (
    FIELD,
    KIND,
    NODE_ROLES,
    glutaryl_metadata,
    glutaryl_term,
    validate_glutaryl_metadata,
)
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, corpus_ids

FIXTURES = Path(__file__).parent / "fixtures/glutaryl_authority"
ENTRIES = json.loads((FIXTURES / "manifest.json").read_text())
STORAGE = json.loads((FIXTURES / "storage.json").read_text())
BY_FRAME = {e["url"].split(":")[-1]: e for e in ENTRIES}
REPRESENTATIVES = ["FAD", "MONOMER-5381", "CPLX-4041", "GLUTARYL-COA-DEHYDROG-RXN",
                   "ENZRXN-41", "PWY-5177"]
EMBEDDED_TAGS = ["Compound", "Enzymatic-Reaction", "Evidence-Code", "Feature", "GO-Term",
                 "Gene", "Organism", "Organization", "Pathway", "Person", "Protein",
                 "Publication", "Reaction", "Regulation", "cco"]


def stage(tmp_path, frame):
    entry = copy.deepcopy(BY_FRAME[frame])
    stored = STORAGE[entry["path"]]
    packed = (FIXTURES / stored["path"]).read_bytes()
    assert len(packed) == stored["compressed_bytes"]
    assert hashlib.sha256(packed).hexdigest() == stored["compressed_sha256"]
    raw = gzip.decompress(packed)
    assert len(raw) == stored["bytes"] and hashlib.sha256(raw).hexdigest() == stored["sha256"]
    path = tmp_path / entry["path"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return entry


def metadata(tmp_path, frame):
    return glutaryl_metadata(stage(tmp_path, frame), tmp_path)


def snapshot(meta, key="original"):
    ident, term = glutaryl_term(meta, key)
    return {"version": 1, "sources": {key: meta}, "terms": {ident: term}}


def consume(tmp_path, value):
    path = tmp_path / "authority.json"
    path.write_text(json.dumps(value))
    return _load_authority(path)


def rewrite(tmp_path, entry, root):
    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    (tmp_path / entry["path"]).write_bytes(raw)
    entry["sha256"] = hashlib.sha256(raw).hexdigest()


def restage_consumer_original(meta, root):
    """Update all body/digest/opaque slots so rejection tests semantic guards."""
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
    meta = glutaryl_metadata(entry, tmp_path)
    raw = (tmp_path / entry["path"]).read_bytes()
    assert base64.b64decode(meta[FIELD]["original_base64"], validate=True) == raw
    assert len(meta[FIELD]["projection"]["slots"]) == len(ET.fromstring(raw)[1])
    assert consume(tmp_path, snapshot(meta)) == snapshot(meta)["terms"]


@pytest.mark.parametrize("frame", REPRESENTATIVES)
@pytest.mark.parametrize("mutation", ["query", "version", "frame", "type", "class", "slot", "extra",
                                      "detail", "base", "result_count", "metadata_species"])
def test_wrong_native_envelope_or_profile_rejected(tmp_path, frame, mutation):
    entry = stage(tmp_path, frame)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    if mutation == "query":
        root.find("metadata/query").text = "META:WRONG"
    elif mutation == "version":
        root.find("metadata/PGDB").set("version", "26.5")
    elif mutation == "frame":
        root[1].set("frameid", "WRONG")
    elif mutation == "type":
        root[1].tag = "Gene"
    elif mutation == "class":
        root[1].set("class", "true")
    elif mutation == "slot":
        root[1].remove(root[1][0])
    elif mutation == "detail":
        root[1].set("detail", "low")
    elif mutation == "base":
        root.set("{http://www.w3.org/XML/1998/namespace}base", "https://example.org/WRONG")
    elif mutation == "result_count":
        root.find("metadata/num_results").text = "2"
    elif mutation == "metadata_species":
        root.find("metadata/PGDB/species").text = "EcoCyc"
    else:
        ET.SubElement(root[1], "unexpected-slot").text = "unsupported"
    rewrite(tmp_path, entry, root)
    with pytest.raises(ValueError):
        glutaryl_metadata(entry, tmp_path)


@pytest.fixture(scope="module")
def embedded_sources():
    examples = {}
    for entry in ENTRIES:
        entity = ET.fromstring(gzip.decompress(
            (FIXTURES / STORAGE[entry["path"]]["path"]).read_bytes()))[1]
        for node in entity.iter():
            if node is not entity and node.tag in EMBEDDED_TAGS:
                examples.setdefault(node.tag, entry["url"].split(":")[-1])
    assert set(examples) == set(EMBEDDED_TAGS)
    return examples


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize("tag", EMBEDDED_TAGS)
@pytest.mark.parametrize("mutation", ["no_frame", "no_identity", "foreign_resource"])
def test_embedded_native_identity_cannot_disappear(
    tmp_path, embedded_sources, boundary, tag, mutation
):
    entry = stage(tmp_path, embedded_sources[tag])
    meta = glutaryl_metadata(entry, tmp_path)
    value = snapshot(meta)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    node = next(n for n in root[1].iter(tag) if n is not root[1])
    if mutation == "no_frame":
        del node.attrib["frameid"]
    elif mutation == "no_identity":
        for attr in ("frameid", "orgid", "ID", "resource"):
            node.attrib.pop(attr, None)
    else:
        node.attrib.pop("ID", None)
        node.set("resource", "getxml?ECOLI:WRONG")
    if boundary == "producer":
        rewrite(tmp_path, entry, root)
        with pytest.raises(ValueError):
            glutaryl_metadata(entry, tmp_path)
    else:
        restage_consumer_original(meta, root)
        with pytest.raises(ValueError):
            consume(tmp_path, value)


@pytest.mark.parametrize("mutation", ["hash", "url", "version", "projection", "base64", "kind"])
def test_consumer_replays_source_original(tmp_path, mutation):
    meta = metadata(tmp_path, "PWY-5177")
    if mutation == "hash":
        meta["sha256"] = "0" * 64
    elif mutation == "url":
        meta["url"] = meta["url"].replace("PWY-5177", "P321-PWY")
    elif mutation == "version":
        meta["version"] = "28.0"
    elif mutation == "projection":
        meta[FIELD]["projection"]["label"] = "invented label"
    elif mutation == "base64":
        meta[FIELD]["original_base64"] += "\n"
    else:
        meta["kind"] = "metacyc-html"
    with pytest.raises(ValueError):
        validate_glutaryl_metadata(meta)


@pytest.mark.parametrize("frame", REPRESENTATIVES)
@pytest.mark.parametrize("field", ["label", "synonyms", "entity_type", "label_kind"])
def test_consumer_rejects_label_or_type_override(tmp_path, frame, field):
    value = snapshot(metadata(tmp_path, frame))
    term = next(iter(value["terms"].values()))
    term[field] = ["invented alias"] if field == "synonyms" else "invented value"
    with pytest.raises(ValueError):
        consume(tmp_path, value)


def test_native_scope_and_named_anomalies_preserved(tmp_path):
    pathway = metadata(tmp_path, "PWY-5177")[FIELD]["projection"]
    assert len(pathway["reaction_list"]) == 5
    assert "MetaCyc:GLUTARYL-COA-DEHYDROGENASE-RXN" not in pathway["reaction_list"]
    composite = metadata(tmp_path, "GLUTARYL-COA-DEHYDROGENASE-RXN")[FIELD]["projection"]
    assert composite["reaction_list"] == ["MetaCyc:GLUTARYL-COA-DEHYDROG-RXN",
                                         "MetaCyc:GLUTACONYL-COA-DECARBOXYLASE-RXN"]
    assert composite["reaction_direction"] == "PHYSIOL-LEFT-TO-RIGHT"
    assert len(composite["sides"]["left"]) == len(composite["sides"]["right"]) == 3
    proton = next(x for x in composite["sides"]["left"] if x["material"] == "MetaCyc:PROTON")
    assert proton["coefficient"] == 2
    for side, frame in [("left", "ETF-Oxidized"), ("right", "ETF-Reduced")]:
        etf = next(x for x in composite["sides"][side] if x["material"] == "MetaCyc:" + frame)
        assert etf["native_type"] == "Protein" and etf["is_class"] is True
    for frame in ["ENZRXN-41", "ENZRXN-22164", "ACETYL-COA-ACETYLTRANSFER-ENZRXN",
                  "THLCLOS-ENZRXN"]:
        meta = metadata(tmp_path, frame)
        ident, term = glutaryl_term(meta, "s")
        assert term["entity_type"] == "native_glutaryl_activity"
        assert NODE_ROLES[term["entity_type"]] == ("participants", {"molecular_activity"})
        assert meta[FIELD]["projection"]["reaction"] != ident
    assert metadata(tmp_path, "CPLX-4041")[FIELD]["projection"]["components"] == [
        {"id": "MetaCyc:MONOMER-5381", "coefficient": 4}]
    assert glutaryl_term(metadata(tmp_path, "RXN-11667"), "s")[1]["label"] == (
        "(S)-3-hydroxybutanoyl-CoA dehydrogenase")
    assert glutaryl_term(metadata(tmp_path, "MONOMER-19851"), "s")[1]["label"] == (
        "(S)-3-hydroxybutanoyl-CoA dehydrogeanse")
    for frame in ["CPLX-7355", "ACETYL-COA-ACETYLTRANSFER-CPLX"]:
        term = glutaryl_term(metadata(tmp_path, frame), "s")[1]
        assert term["label"] == frame and term["label_kind"] == "source_context"


@pytest.mark.parametrize("frame", ["GLUTARYL-COA-DEHYDROG-RXN", "GLUTARYL-COA-DEHYDROGENASE-RXN"])
@pytest.mark.parametrize("mutation", ["instance", "compound", "free_FAD"])
def test_generic_etf_cannot_become_exact_protein_or_fad(tmp_path, frame, mutation):
    entry = stage(tmp_path, frame)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    node = root.find("Reaction/left/Protein")
    if mutation == "instance":
        del node.attrib["class"]
    elif mutation == "compound":
        node.tag = "Compound"
    else:
        node.set("frameid", "FAD")
        node.set("resource", "getxml?META:FAD")
    rewrite(tmp_path, entry, root)
    with pytest.raises(ValueError):
        glutaryl_metadata(entry, tmp_path)


def test_unselected_wrong_frame_is_rejected_before_selection(tmp_path):
    good = stage(tmp_path, "FAD")
    bad = stage(tmp_path, "PWY-5177")
    root = ET.fromstring((tmp_path / bad["path"]).read_bytes())
    root[1].set("frameid", "P321-PWY")
    rewrite(tmp_path, bad, root)
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([good, bad]))
    corpus = tmp_path / "records"
    corpus.mkdir()
    (corpus / "record.yaml").write_text("id: MetaCyc:FAD\n")
    with pytest.raises(ValueError):
        build_snapshot(manifest, corpus, tmp_path)


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize("query", ["META:PWY-5177", "id=META:PWY-5177", "object=META:PWY-5177"])
@pytest.mark.parametrize("host", ["bf2i-artsymbiocyc.insa-lyon.fr", "biocyc.org", "www.biocyc.org",
                                  "metacyc.org", "www.metacyc.org"])
def test_unselected_request_downgrade_rejected(tmp_path, boundary, query, host):
    good = stage(tmp_path, "FAD")
    body = b"<html><title>unrelated</title></html>"
    (tmp_path / "unselected.html").write_bytes(body)
    bad = {"key": "bad", "kind": "metacyc-html", "path": "unselected.html",
           "url": f"https://{host}/getxml?{query}", "version": "27.0", "license": "test",
           "sha256": hashlib.sha256(body).hexdigest()}
    if boundary == "producer":
        manifest = tmp_path / "manifest.json"
        manifest.write_text(json.dumps([good, bad]))
        corpus = tmp_path / "records"
        corpus.mkdir()
        (corpus / "record.yaml").write_text("id: MetaCyc:FAD\n")
        with pytest.raises(ValueError, match="typed source"):
            build_snapshot(manifest, corpus, tmp_path)
    else:
        value = snapshot(glutaryl_metadata(good, tmp_path))
        value["sources"]["bad"] = {k: bad[k] for k in ("url", "version", "license", "sha256")}
        with pytest.raises(ValueError, match="typed source"):
            consume(tmp_path, value)


def record_consumer(tmp_path, frame):
    meta = metadata(tmp_path, frame)
    value = snapshot(meta)
    ident, term = next(iter(value["terms"].items()))
    section, categories = NODE_ROLES[term["entity_type"]]
    node = {"id": ident, "label": term["label"], "category": sorted(categories)[0]}
    anchor = metadata(tmp_path, "PWY-5177")
    anchor_id, anchor_term = glutaryl_term(anchor, "pathway")
    value["sources"]["pathway"] = anchor
    value["terms"][anchor_id] = anchor_term
    record = {"id": anchor_id, "label": anchor_term["label"], "taxa": [],
              "participants": [], "reactions": []}
    record[section] = [node]
    (tmp_path / "data/pathways").mkdir(parents=True)
    (tmp_path / "authority.json").write_text(json.dumps(value))
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump({
        "version": 1, "namespaces": {"MetaCyc": {"snapshot": "authority.json",
                                                   "policy": "canonical_or_synonym"}},
        "contextual_labels": [{"namespace": "MetaCyc", "sections": [section],
                               "record_prefixes": ["MetaCyc"], "reason": "broad rule test"}],
    }))
    return record, node, section


@pytest.mark.parametrize("frame", ["FAD", "CPLX-4041", "MONOMER-5381", "RXN-11667", "ENZRXN-41"])
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
    assert any(("LABEL_MISMATCH" if bad == "label" else "ENTITY_TYPE_MISMATCH") in e
               for e in errors)


def test_hydration_root_and_edge_prose_preserves_canonical_label_without_waiver(tmp_path):
    record, node, _ = record_consumer(tmp_path, "RXN-11667")
    assert node["label"] == "(S)-3-hydroxybutanoyl-CoA dehydrogenase"
    disclosure = (
        "Crotonyl-CoA hydration to (S)-3-hydroxybutanoyl-CoA. Native RXN-11667 is reversible, "
        "with (S)-3-hydroxybutanoyl-CoA on the left and water plus crotonyl-CoA on the right; "
        "the pathway uses right-to-left. Its canonical dehydrogenase name is a source anomaly."
    )
    record["description"] = disclosure
    record["mechanistic_edges"] = [{
        "subject_id": "MetaCyc:PWY-5177", "predicate": "has_part",
        "object_id": "MetaCyc:RXN-11667", "description": disclosure,
    }]
    # Reference-only identities are provenance objects, not named authority nodes.
    record["references"] = [{"id": "MetaCyc:REG-7497", "title": "source regulation"}]
    path = tmp_path / "data/pathways/draft.yaml"
    path.write_text(yaml.safe_dump(record))
    assert identifier_errors(tmp_path) == []
    assert "MetaCyc:REG-7497" not in corpus_ids(tmp_path / "data/pathways")
    saved = yaml.safe_load(path.read_text())
    assert "description" not in saved["reactions"][0]
    assert saved["description"] == saved["mechanistic_edges"][0]["description"] == disclosure


def test_new_kind_does_not_admit_existing_or_unreviewed_scope(tmp_path):
    for frame in ["P321-PWY", "PWY0-321", "ETF-Oxidized", "ACETYL-COA", "REG-7497", "UNKNOWN"]:
        entry = stage(tmp_path, "FAD")
        entry["url"] = entry["url"].replace("FAD", frame)
        entry["kind"] = KIND
        with pytest.raises(ValueError, match="outside"):
            glutaryl_metadata(entry, tmp_path)


@pytest.mark.parametrize("request_url", [
    "https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:FAD",
    "http://bf2i-artsymbiocyc.insa-lyon.fr/getxml?META:FAD",
    "https://biocyc.org/getxml?META:FAD",
    "https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?META%3AFAD",
    "https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?META:FAD&detail=full",
    "https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?ECOLI:FAD",
])
def test_new_kind_retains_exact_acquired_request_syntax(tmp_path, request_url):
    entry = stage(tmp_path, "FAD")
    entry["url"] = request_url
    with pytest.raises(ValueError, match="exact acquired"):
        glutaryl_metadata(entry, tmp_path)


def test_normal_producer_builds_all49_from_originals(tmp_path):
    entries = [stage(tmp_path, frame) for frame in BY_FRAME]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "records"
    records.mkdir()
    (records / "selection.yaml").write_text(yaml.safe_dump({
        "id": "MetaCyc:PWY-5177",
        "participants": [{"id": "MetaCyc:" + frame} for frame in BY_FRAME if frame != "PWY-5177"],
    }))
    value = build_snapshot(manifest, records, tmp_path)
    assert len(value["sources"]) == len(value["terms"]) == 49
    assert consume(tmp_path, value) == value["terms"]


@pytest.mark.parametrize("frame", ["PWY-5177", "GLUTARYL-COA-DEHYDROGENASE-RXN"])
def test_same_size_wrong_native_membership_is_rejected(tmp_path, frame):
    entry = stage(tmp_path, frame)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    node = root[1].find("reaction-list/Reaction")
    node.set("frameid", "RXN-8031")
    node.set("resource", "getxml?META:RXN-8031")
    rewrite(tmp_path, entry, root)
    with pytest.raises(ValueError, match="membership"):
        glutaryl_metadata(entry, tmp_path)
