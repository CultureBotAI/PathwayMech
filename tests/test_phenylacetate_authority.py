"""Whole issuing originals and adversarial checks for bounded Paa identities."""
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

from pathwaymech.biocyc_phenylacetate import (
    FIELD,
    META_KIND,
    NODE_ROLES,
    phenylacetate_metadata,
    phenylacetate_term,
    validate_phenylacetate_assertions,
    validate_phenylacetate_metadata,
)
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot

FIXTURES = Path(__file__).parent / "fixtures/phenylacetate_authority"
ENTRIES = json.loads((FIXTURES / "manifest.json").read_text())
STORAGE = json.loads((FIXTURES / "storage.json").read_text())
BY_FRAME = {e["url"].split(":")[-1]: e for e in ENTRIES}
REPRESENTATIVES = ["AMP", "G6716-MONOMER", "CPLX0-8538", "RXN0-6512",
                   "ENZRXN-18273", "PWY0-321", "PM5", "TU5", "ENZRXN0-7862"]
EMBEDDED_OBJECT_TAGS = [
    "Compound", "Evidence-Code", "Publication", "Reaction", "Regulation",
    "Enzymatic-Reaction", "Protein", "Person", "Organization", "Gene",
    "Organism", "Feature", "GO-Term", "cco", "Pathway", "Genetic-Element",
    "Promoter", "Transcription-Unit", "DNA-Binding-Site",
]


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
    return phenylacetate_metadata(stage(tmp_path, frame), tmp_path)


def snapshot(meta, key="original"):
    ident, term = phenylacetate_term(meta, key)
    return {"version": 1, "sources": {key: meta}, "terms": {ident: term}}


def consume(tmp_path, value):
    file = tmp_path / "authority.json"
    file.write_text(json.dumps(value))
    return _load_authority(file)


def rewrite(tmp_path, entry, root):
    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    (tmp_path / entry["path"]).write_bytes(raw)
    entry["sha256"] = hashlib.sha256(raw).hexdigest()


@pytest.fixture(scope="module")
def embedded_object_sources():
    """Find genuine nested examples independently of the adapter's tag guard."""
    examples = {}
    for entry in ENTRIES:
        packed = (FIXTURES / STORAGE[entry["path"]]["path"]).read_bytes()
        entity = ET.fromstring(gzip.decompress(packed))[1]
        for node in entity.iter():
            if node is not entity and node.tag in EMBEDDED_OBJECT_TAGS:
                examples.setdefault(node.tag, entry["url"].split(":")[-1])
    assert set(examples) == set(EMBEDDED_OBJECT_TAGS)
    return examples


def restage_consumer_original(meta, root):
    """Keep the changed body, digest and retained projection coherent.

    Updating all serialized slots prevents the consumer regression from passing
    merely because the old projection or hash disagrees with the altered bytes.
    These mutations leave the direct selected label and other derived fields
    untouched; only a nested object's identity is changed.
    """
    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    meta["sha256"] = hashlib.sha256(raw).hexdigest()
    native = meta[FIELD]
    native["original_base64"] = base64.b64encode(raw).decode("ascii")
    native["root_attributes"] = dict(root.attrib)
    native["metadata_xml"] = ET.tostring(root.find("metadata"), encoding="unicode")
    native["projection"]["slots"] = [
        {"ordinal": i, "name": node.tag, "xml": ET.tostring(node, encoding="unicode")}
        for i, node in enumerate(root[1], 1)
    ]


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize("tag", EMBEDDED_OBJECT_TAGS)
@pytest.mark.parametrize("missing", ["frameid", "orgid", "locator", "all_identity"])
def test_incomplete_embedded_identity_is_rejected(
    tmp_path, embedded_object_sources, boundary, tag, missing
):
    entry = stage(tmp_path, embedded_object_sources[tag])
    meta = phenylacetate_metadata(entry, tmp_path)
    # Form the valid term before tampering; label and role are not the defect.
    value = snapshot(meta)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    target = next(node for node in root[1].iter(tag) if node is not root[1])
    if missing == "all_identity":
        for attr in ("frameid", "orgid", "ID", "resource"):
            target.attrib.pop(attr, None)
    elif missing == "locator":
        target.attrib.pop("ID", None)
        target.attrib.pop("resource", None)
    else:
        del target.attrib[missing]
    if boundary == "producer":
        rewrite(tmp_path, entry, root)
        with pytest.raises(ValueError, match="incomplete or ambiguous embedded native identity"):
            phenylacetate_metadata(entry, tmp_path)
    else:
        restage_consumer_original(meta, root)
        with pytest.raises(ValueError, match="incomplete or ambiguous embedded native identity"):
            consume(tmp_path, value)


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize(
    "mutation", ["foreign_resource_without_frame", "no_attributes", "both_locators"]
)
def test_embedded_parent_identity_bypass_is_rejected(tmp_path, boundary, mutation):
    entry = stage(tmp_path, "AMP")
    meta = phenylacetate_metadata(entry, tmp_path)
    value = snapshot(meta)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    target = root.find("Compound/parent/Compound")
    assert target is not None
    if mutation == "foreign_resource_without_frame":
        del target.attrib["frameid"]
        target.set("resource", "getxml?ECOLI:WRONG")
        assert target.get("orgid") == "META"
    elif mutation == "no_attributes":
        target.attrib.clear()
    else:
        target.set("ID", target.get("orgid") + ":" + target.get("frameid"))
    if boundary == "producer":
        rewrite(tmp_path, entry, root)
        with pytest.raises(ValueError, match="incomplete or ambiguous embedded native identity"):
            phenylacetate_metadata(entry, tmp_path)
    else:
        restage_consumer_original(meta, root)
        with pytest.raises(ValueError, match="incomplete or ambiguous embedded native identity"):
            consume(tmp_path, value)


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize("identity_attribute", ["frameid", "orgid", "ID", "resource"])
def test_native_identity_attributes_on_other_tags_are_checked(
    tmp_path, boundary, identity_attribute
):
    entry = stage(tmp_path, "AMP")
    meta = phenylacetate_metadata(entry, tmp_path)
    value = snapshot(meta)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    target = root.find("Compound/parent/Compound")
    assert target is not None
    original_value = target.get(identity_attribute, "META:Purine-ribonucleosides-5-P")
    target.tag = "uninterpreted-context"
    target.attrib.clear()
    target.set(identity_attribute, original_value)
    if boundary == "producer":
        rewrite(tmp_path, entry, root)
        with pytest.raises(ValueError, match="incomplete or ambiguous embedded native identity"):
            phenylacetate_metadata(entry, tmp_path)
    else:
        restage_consumer_original(meta, root)
        with pytest.raises(ValueError, match="incomplete or ambiguous embedded native identity"):
            consume(tmp_path, value)


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
def test_metadata_pgdb_identity_is_still_validated(tmp_path, boundary):
    entry = stage(tmp_path, "AMP")
    meta = phenylacetate_metadata(entry, tmp_path)
    value = snapshot(meta)
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    del root.find("metadata/PGDB").attrib["orgid"]
    if boundary == "producer":
        rewrite(tmp_path, entry, root)
        with pytest.raises(ValueError, match="PGDB identity mismatch"):
            phenylacetate_metadata(entry, tmp_path)
    else:
        restage_consumer_original(meta, root)
        with pytest.raises(ValueError, match="PGDB identity mismatch"):
            consume(tmp_path, value)


@pytest.mark.parametrize("frame", list(BY_FRAME))
def test_complete_original_roundtrip(tmp_path, frame):
    entry = stage(tmp_path, frame)
    meta = phenylacetate_metadata(entry, tmp_path)
    raw = base64.b64decode(meta[FIELD]["original_base64"], validate=True)
    assert raw == (tmp_path / entry["path"]).read_bytes()
    assert len(meta[FIELD]["projection"]["slots"]) == len(ET.fromstring(raw)[1])
    assert consume(tmp_path, snapshot(meta)) == snapshot(meta)["terms"]


def test_native_scope_is_preserved(tmp_path):
    pathway = metadata(tmp_path, "PWY0-321")[FIELD]["projection"]
    assert len(pathway["reaction_list"]) == 9
    assert "MetaCyc:RXN0-6512" in pathway["reaction_list"]
    net = metadata(tmp_path, "RXN0-6512")[FIELD]["projection"]
    assert net["reaction_direction"] == "PHYSIOL-RIGHT-TO-LEFT"
    assert net["sides"]["left"][0]["material"] == "MetaCyc:TRANS-23-DEHYDROADIPYL-COA"
    abce = metadata(tmp_path, "CPLX-8168")[FIELD]["projection"]
    assert len(abce["components"]) == 4
    assert all(c["coefficient"] is None for c in abce["components"])
    paaz = metadata(tmp_path, "CPLX0-8538")[FIELD]["projection"]
    assert paaz["components"] == [{"id": "MetaCyc:G6708-MONOMER", "coefficient": 6}]
    assert phenylacetate_term(metadata(tmp_path, "AMP"), "s")[1]["label"] == "AMP"
    unnamed = phenylacetate_term(metadata(tmp_path, "G6716-MONOMER"), "s")[1]
    assert unnamed["label"] == "G6716-MONOMER" and unnamed["label_kind"] == "source_context"
    assert metadata(tmp_path, "ENZRXN0-7862")[FIELD]["projection"]["reaction"] == "EcoCyc:RXN0-7104"


@pytest.mark.parametrize("frame", REPRESENTATIVES)
@pytest.mark.parametrize(
    "mutation", ["query", "version", "frame", "type", "class", "slot", "extra"]
)
def test_producer_rejects_wrong_complete_original(tmp_path, frame, mutation):
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
    else:
        ET.SubElement(root[1], "unexpected-native-slot").text = "not supported"
    rewrite(tmp_path, entry, root)
    with pytest.raises(ValueError):
        phenylacetate_metadata(entry, tmp_path)


@pytest.mark.parametrize("mutation", ["hash", "url", "release", "projection", "base64", "kind"])
def test_consumer_reparses_original_and_source(tmp_path, mutation):
    meta = metadata(tmp_path, "PWY0-321")
    if mutation == "hash":
        meta["sha256"] = "0" * 64
    elif mutation == "url":
        meta["url"] = meta["url"].replace("PWY0-321", "P321-PWY")
    elif mutation == "release":
        meta["version"] = "28.0"
    elif mutation == "projection":
        meta[FIELD]["projection"]["label"] = "invented name"
    elif mutation == "base64":
        meta[FIELD]["original_base64"] += "\n"
    else:
        meta["kind"] = "metacyc-html"
    with pytest.raises(ValueError):
        validate_phenylacetate_metadata(meta)


@pytest.mark.parametrize("frame", REPRESENTATIVES)
@pytest.mark.parametrize("field", ["label", "synonyms", "entity_type", "label_kind"])
def test_consumer_rejects_curated_term_overrides(tmp_path, frame, field):
    value = snapshot(metadata(tmp_path, frame))
    term = next(iter(value["terms"].values()))
    term[field] = ["invented alias"] if field == "synonyms" else "invented value"
    with pytest.raises(ValueError):
        consume(tmp_path, value)


def test_unselected_wrong_frame_is_rejected_before_selection(tmp_path):
    good = stage(tmp_path, "AMP")
    bad = stage(tmp_path, "RXN0-6512")
    root = ET.fromstring((tmp_path / bad["path"]).read_bytes())
    root[1].set("frameid", "RXN-2425")
    rewrite(tmp_path, bad, root)
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([good, bad]))
    corpus = tmp_path / "records"
    corpus.mkdir()
    (corpus / "record.yaml").write_text("id: MetaCyc:AMP\n")
    with pytest.raises(ValueError):
        build_snapshot(manifest, corpus, tmp_path)


def test_unselected_request_downgrade_is_rejected(tmp_path):
    good = stage(tmp_path, "AMP")
    bad = stage(tmp_path, "PWY0-321")
    bad["kind"] = "metacyc-html"
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([good, bad]))
    corpus = tmp_path / "records"
    corpus.mkdir()
    (corpus / "record.yaml").write_text("id: MetaCyc:AMP\n")
    with pytest.raises(ValueError, match="typed source"):
        build_snapshot(manifest, corpus, tmp_path)


def unselected_generic_request(tmp_path, boundary, url):
    """A valid selected AMP owner plus an unrelated, unselected HTML owner."""
    good = stage(tmp_path, "AMP")
    body = (
        b"<html><TITLE>MetaCyc Unrelated context title</TITLE>"
        b"<script>typeObjectPage={object:'UNREVIEWED-FRAME',orgid:'META'}</script></html>"
    )
    (tmp_path / "unselected.html").write_bytes(body)
    unselected = {
        "key": "unselected", "kind": "metacyc-html", "path": "unselected.html",
        "url": url, "version": "27.0", "license": "test fixture",
        "sha256": hashlib.sha256(body).hexdigest(),
    }
    if boundary == "producer":
        manifest = tmp_path / "manifest.json"
        manifest.write_text(json.dumps([good, unselected]))
        corpus = tmp_path / "records"
        corpus.mkdir()
        (corpus / "record.yaml").write_text("id: MetaCyc:AMP\n")
        return build_snapshot(manifest, corpus, tmp_path)["terms"]
    value = snapshot(phenylacetate_metadata(good, tmp_path))
    value["sources"]["unselected"] = {
        key: unselected[key] for key in ("url", "version", "license", "sha256")
    }
    return consume(tmp_path, value)


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize("token", ["META:PWY0-321", "ECOLI:PM5"])
@pytest.mark.parametrize("host", [
    "bf2i-artsymbiocyc.insa-lyon.fr", "biocyc.org", "www.biocyc.org",
    "metacyc.org", "www.metacyc.org",
])
@pytest.mark.parametrize("query_prefix", ["", "id=", "object="])
def test_unselected_known_native_request_forms_require_typed_owner(
    tmp_path, boundary, token, host, query_prefix
):
    url = f"https://{host}/getxml?{query_prefix}{token}"
    with pytest.raises(ValueError, match="complete native identity requires its typed source"):
        unselected_generic_request(tmp_path, boundary, url)


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize("token", ["META:PWY0-321", "ECOLI:PM5"])
def test_unselected_legacy_native_request_requires_typed_owner(tmp_path, boundary, token):
    url = f"http://bf2i-artsymbiocyc.insa-lyon.fr:443/getxml?{token}"
    with pytest.raises(ValueError, match="complete native identity requires its typed source"):
        unselected_generic_request(tmp_path, boundary, url)


@pytest.mark.parametrize("boundary", ["producer", "consumer"])
@pytest.mark.parametrize("url", [
    "https://example.org/getxml?META:PWY0-321",
    "https://biocyc.org.example/getxml?ECOLI:PM5",
    "https://biocyc.org/search?META:PWY0-321",
    "https://biocyc.org/getxmlish?ECOLI:PM5",
    "https://biocyc.org/META/NEW-IMAGE?META:PWY0-321",
    "https://biocyc.org/getxml?note=META:PWY0-321",
    "https://biocyc.org/getxml?next=https%3A%2F%2Fbiocyc.org%2Fgetxml%3FMETA:PWY0-321",
    "https://biocyc.org/getxml?META:PWY0-321&view=full",
    "https://biocyc.org/getxml?META:PWY0-321=",
    "https://biocyc.org/getxml?prefixMETA:PWY0-321",
    "https://biocyc.org/getxml?PWY0-321",
    "https://biocyc.org/getxml?META:UNREVIEWED-FRAME",
    "https://biocyc.org/getxml?ECOLI:UNREVIEWED-FRAME",
    "https://biocyc.org/getxml?meta:PWY0-321",
    "https://biocyc.org/getxml?description=see-id=META:PWY0-321",
])
def test_unrelated_queries_do_not_assert_native_identity(tmp_path, boundary, url):
    assert set(unselected_generic_request(tmp_path, boundary, url)) == {"MetaCyc:AMP"}


def test_non_http_query_does_not_bypass_the_public_url_guard(tmp_path):
    url = "ftp://biocyc.org/getxml?META:PWY0-321"
    # This is not an HTTP native request; the general consumer still rejects
    # unsupported source protocols, independently of the native identity guard.
    validate_phenylacetate_assertions({"unselected": {"url": url}}, [])
    with pytest.raises(ValueError, match="expected a public source URL"):
        unselected_generic_request(tmp_path, "consumer", url)


def test_body_identity_and_source_cannot_choose_different_owner(tmp_path):
    a = metadata(tmp_path, "AMP")
    b = metadata(tmp_path, "ATP")
    value = snapshot(a)
    value["sources"]["other"] = b
    value["terms"]["MetaCyc:AMP"]["source"] = "other"
    with pytest.raises(ValueError):
        consume(tmp_path, value)


@pytest.mark.parametrize("frame", ["AMP", "CPLX0-8538", "G6716-MONOMER", "RXN0-6512", "PM5"])
@pytest.mark.parametrize("bad", ["label", "category"])
def test_namespace_context_rule_cannot_override_exact_profile(tmp_path, frame, bad):
    meta = metadata(tmp_path, frame)
    value = snapshot(meta)
    ident, term = next(iter(value["terms"].items()))
    section, categories = NODE_ROLES[term["entity_type"]]
    node = {"id": ident, "label": term["label"], "category": sorted(categories)[0]}
    if bad == "label":
        node["label"] = "invented source context"
    else:
        node["category"] = "gene"
    (tmp_path / "data/pathways").mkdir(parents=True)
    record = {"id": ident, "label": term["label"], "taxa": [], "participants": [], "reactions": []}
    # Use a known pathway identity; test the target in its actual section.
    anchor = metadata(tmp_path, "PWY0-321")
    anchor_id, anchor_term = phenylacetate_term(anchor, "pathway")
    value["sources"]["pathway"] = anchor
    value["terms"][anchor_id] = anchor_term
    record.update(id=anchor_id, label=anchor_term["label"])
    record[section] = [node]
    (tmp_path / "data/pathways/draft.yaml").write_text(yaml.safe_dump(record))
    (tmp_path / "authority.json").write_text(json.dumps(value))
    namespaces = {i.split(":")[0]: {"snapshot": "authority.json", "policy": "canonical_or_synonym"}
                  for i in value["terms"]}
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump({
        "version": 1, "namespaces": namespaces,
        "contextual_labels": [{"namespace": ident.split(":")[0],
                               "sections": [section], "record_prefixes": ["MetaCyc"],
                               "reason": "adversarial broad namespace rule"}],
    }))
    errors = identifier_errors(tmp_path)
    assert any(("LABEL_MISMATCH" if bad == "label" else "ENTITY_TYPE_MISMATCH") in e
               for e in errors)


def test_unreviewed_frame_and_entity_links_fail(tmp_path):
    entry = stage(tmp_path, "AMP")
    entry["url"] = entry["url"].replace("AMP", "UNREVIEWED")
    with pytest.raises(ValueError, match="outside"):
        phenylacetate_metadata(entry, tmp_path)
    entry = stage(tmp_path, "ENZRXN-18273")
    root = ET.fromstring((tmp_path / entry["path"]).read_bytes())
    root.find("Enzymatic-Reaction/enzyme/Protein").set("frameid", "WRONG")
    rewrite(tmp_path, entry, root)
    with pytest.raises(ValueError, match="resource/frame"):
        phenylacetate_metadata(entry, tmp_path)


def test_profile_does_not_accept_other_p321_scope(tmp_path):
    entry = stage(tmp_path, "PWY0-321")
    entry["url"] = entry["url"].replace("PWY0-321", "P321-PWY")
    entry["kind"] = META_KIND
    with pytest.raises(ValueError, match="outside"):
        phenylacetate_metadata(entry, tmp_path)
