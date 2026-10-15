"""Complete issuing originals and adversarial P321 producer/consumer controls."""

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

from pathwaymech.biocyc_p321 import (
    FIELDS,
    GENE_KIND,
    P321_KINDS,
    p321_metadata,
    p321_term,
)
from pathwaymech.biocyc_pathway import PATHWAY_KIND, pathway_metadata, pathway_term
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot

FIXTURE = Path(__file__).parent / "fixtures/p321_authority"
ENTRIES = json.loads((FIXTURE / "manifest.json").read_text())
STORAGE = json.loads((FIXTURE / "storage.json").read_text())
EXPECTED = json.loads((FIXTURE / "expected-terms.json").read_text())
BY_ID = {
    ident: next(e for e in ENTRIES if e["key"] == term["source"])
    for ident, term in EXPECTED.items()
}
TYPED = [ident for ident, e in BY_ID.items() if e["kind"] in P321_KINDS | {PATHWAY_KIND}]
ANCHOR = "MetaCyc:R266-RXN"


def fixture_bytes(path):
    row = STORAGE[path]
    compressed = (FIXTURE / row["path"]).read_bytes()
    assert len(compressed) == row["compressed_bytes"]
    assert hashlib.sha256(compressed).hexdigest() == row["compressed_sha256"]
    body = gzip.decompress(compressed)
    assert len(body) == row["bytes"] and hashlib.sha256(body).hexdigest() == row["sha256"]
    return body


def stage(tmp_path):
    for path in STORAGE:
        target = tmp_path / path
        target.parent.mkdir(exist_ok=True, parents=True)
        target.write_bytes(fixture_bytes(path))
    return copy.deepcopy(BY_ID)


def build(tmp_path, entries, ids):
    corpus = tmp_path / "selected"
    corpus.mkdir(exist_ok=True)
    ids = list(ids)
    (corpus / "record.yaml").write_text(
        yaml.safe_dump({"id": ids[0], "participants": [{"id": ident} for ident in ids[1:]]})
    )
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return build_snapshot(manifest, corpus, tmp_path)


def consume(tmp_path, data):
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(data))
    return _load_authority(path)


def metadata(entry, tmp_path):
    return (pathway_metadata if entry["kind"] == PATHWAY_KIND else p321_metadata)(entry, tmp_path)


def native(meta):
    return meta["native_pathway" if meta["kind"] == PATHWAY_KIND else FIELDS[meta["kind"]]]


def projection(meta):
    value = native(meta)
    return value if meta["kind"] == PATHWAY_KIND else value["document"]["projection"]


def original(tmp_path, entry):
    return ET.fromstring((tmp_path / entry["path"]).read_bytes())


def save(tmp_path, entry, root):
    body = ET.tostring(root, encoding="iso-8859-1", xml_declaration=True)
    (tmp_path / entry["path"]).write_bytes(body)
    entry["sha256"] = hashlib.sha256(body).hexdigest()


def snapshot(meta, key):
    ident, term = (pathway_term if meta["kind"] == PATHWAY_KIND else p321_term)(meta, key)
    return {"version": 1, "sources": {key: meta}, "terms": {ident: term}}


def test_all_31_additions_roundtrip_and_additive_order(tmp_path):
    entries = stage(tmp_path)
    data = build(tmp_path, list(entries.values()), EXPECTED)
    assert data["terms"] == EXPECTED
    assert consume(tmp_path, data) == EXPECTED
    # These are only the new additions. Existing first-owner order is not reversed.
    assert build(tmp_path, list(entries.values())[::-1], EXPECTED) == data
    assert build(tmp_path, list(entries.values()), EXPECTED) == data
    for ident in TYPED:
        entry = entries[ident]
        meta = data["sources"][entry["key"]]
        value = native(meta)
        encoded = (
            value["original_base64"]
            if meta["kind"] == PATHWAY_KIND
            else value["document"]["original_base64"]
        )
        assert base64.b64decode(encoded) == fixture_bytes(entry["path"])
        source = original(tmp_path, entry)[1]
        projected = projection(meta)
        assert projected["direct_slot_order"] == [n.tag for n in source]
        assert projected["source_slots"] == [
            {"tag": n.tag, "xml": ET.tostring(n, encoding="unicode")} for n in source
        ]
        if entry["kind"] == GENE_KIND:
            child = value["product_source"]
            assert base64.b64decode(child["document"]["original_base64"]) == fixture_bytes(
                entry["product_source"]["path"]
            )


def test_route_carriers_unknown_coefficient_and_gene_product_scope(tmp_path):
    entries = stage(tmp_path)
    data = build(tmp_path, list(entries.values()), EXPECTED)
    values = {ident: projection(data["sources"][entries[ident]["key"]]) for ident in TYPED}
    pathway = values["MetaCyc:P321-PWY"]
    assert len(pathway["reaction_list"]) == len(pathway["reaction_layout"]) == 9
    assert len(pathway["reaction_ordering"]) == 8
    assert len(pathway["citations"]) == 8 and len(pathway["pathway_links"]) == 3
    assert [n["reaction"]["id"] for n in pathway["reaction_layout"] if n["direction"] == "R2L"] == [
        "MetaCyc:1.3.99.15-RXN",
        "MetaCyc:R265-RXN",
    ]
    reaction = values["MetaCyc:R265-RXN"]
    assert [
        v["entity"]["id"] for v in reaction["sides"] if v["entity"]["native_type"] == "Protein"
    ] == ["MetaCyc:ETF-Oxidized", "MetaCyc:ETF-Reduced"]
    assert all(v["coefficient"] == 1 and not v["coefficient_explicit"] for v in reaction["sides"])
    assert [v["id"] for v in values["MetaCyc:ETF-Reduced"]["state_links"]["modified-form"]] == [
        "MetaCyc:ETF-Semiquinone",
        "MetaCyc:ETF-Oxidized",
    ]
    singleton = values["MetaCyc:CPLX-926"]
    assert singleton["coefficient"] is None and singleton["coefficient_explicit"] is False
    assert singleton["activity"]["id"] == "MetaCyc:ENZRXN-1144"
    assert values["MetaCyc:G-545"]["product"]["id"] == "MetaCyc:MONOMER-888"
    assert values["MetaCyc:G-550"]["product"]["id"] == "MetaCyc:MONOMER-893"


COMMON = [
    "root",
    "extra-root",
    "version",
    "base",
    "query",
    "pgdb",
    "num-results",
    "frame",
    "type",
    "class",
    "unknown-attribute",
    "unknown-slot",
    "mixed-text",
]


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize("mutation", COMMON)
def test_closed_complete_envelopes_and_shapes(tmp_path, ident, mutation):
    entry = stage(tmp_path)[ident]
    root = original(tmp_path, entry)
    entity = root[1]
    if mutation == "root":
        root.tag = "surrogate"
    elif mutation == "extra-root":
        root.append(copy.deepcopy(entity))
    elif mutation == "version":
        root.set("ptools-version", "26.0")
    elif mutation == "base":
        root.set("{http://www.w3.org/XML/1998/namespace}base", "https://example.org/")
    elif mutation == "query":
        root.find("metadata/query").text = "META:OTHER"
    elif mutation == "pgdb":
        root.find("metadata/PGDB").set("orgid", "ECOLI")
    elif mutation == "num-results":
        root.find("metadata/num_results").text = "2"
    elif mutation == "frame":
        entity.set("frameid", "OTHER")
    elif mutation == "type":
        entity.tag = "Compound"
    elif mutation == "class":
        entity.set("class", "false")
    elif mutation == "unknown-attribute":
        entity.set("inferred", "true")
    elif mutation == "unknown-slot":
        ET.SubElement(entity, "unsupported")
    elif mutation == "mixed-text":
        entity.text = "unexpected"
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        metadata(entry, tmp_path)


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize(
    "mutation",
    [
        "name",
        "slot-count",
        "type",
        "original-hash",
        "unknown",
        "missing",
        "wrong-json-type",
        "term",
    ],
)
def test_consumer_reconstructs_whole_projection_and_term(tmp_path, ident, mutation):
    entry = stage(tmp_path)[ident]
    meta = metadata(entry, tmp_path)
    data = snapshot(meta, entry["key"])
    projected = projection(meta)
    if mutation == "name":
        projected["direct_common_name" if entry["kind"] == PATHWAY_KIND else "label"] = "forged"
    elif mutation == "slot-count":
        projected["source_slots"].pop()
    elif mutation == "type":
        projected["native_attributes"]["class"] = "false"
    elif mutation == "original-hash":
        meta["sha256"] = "0" * 64
    elif mutation == "unknown":
        meta["extra"] = "forged"
    elif mutation == "missing":
        del native(meta)["original_base64" if entry["kind"] == PATHWAY_KIND else "document"]
    elif mutation == "wrong-json-type":
        meta["version"] = 27
    elif mutation == "term":
        data["terms"][ident]["entity_type"] = "chemical_class"
    with pytest.raises((ValueError, TypeError, KeyError)):
        consume(tmp_path, data)


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_changed_complete_owners_rejected_before_selection(tmp_path, ident, reverse, selected):
    entries = stage(tmp_path)
    first = entries[ident]
    second = copy.deepcopy(first)
    second.update(key="conflict", path="conflict.xml")
    root = original(tmp_path, first)
    change = root[1].find("comment")
    if change is None:
        change = root[1].find("gibbs-0")
    if change is None:
        # Genes have no opaque comment: mutate product comment, preserving identity.
        second["product_source"]["path"] = "conflict-product.xml"
        child_root = original(tmp_path, first["product_source"])
        child_root[1].find("comment").text += " Additional retained context."
        save(tmp_path, second["product_source"], child_root)
    else:
        change.text = (
            "-99.5" if change.tag == "gibbs-0" else change.text + " Additional retained context."
        )
    save(tmp_path, second, root)
    pair = [first, second][::-1] if reverse else [first, second]
    ids = [ident] if selected else [ANCHOR]
    with pytest.raises(ValueError):
        build(tmp_path, pair + ([] if selected else [entries[ANCHOR]]), ids)
    data = snapshot(metadata(first, tmp_path), first["key"])
    data["sources"] = {e["key"]: metadata(e, tmp_path) for e in pair}
    if not selected:
        anchor = build(tmp_path, [entries[ANCHOR]], [ANCHOR])
        data["sources"].update(anchor["sources"])
        data["terms"] = anchor["terms"]
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_legacy_and_request_only_downgrades_rejected(tmp_path, ident, reverse, selected):
    entries = stage(tmp_path)
    entry = entries[ident]
    legacy = {k: v for k, v in entry.items() if k != "product_source"}
    legacy.update(key="downgrade", kind="metacyc-html")
    pair = [entry, legacy][::-1] if reverse else [entry, legacy]
    ids = [ident] if selected else [ANCHOR]
    with pytest.raises(ValueError):
        build(tmp_path, pair + ([] if selected else [entries[ANCHOR]]), ids)
    # Consumer request-only owner has no term and no typed metadata.
    data = snapshot(metadata(entry, tmp_path), entry["key"])
    downgrade = {k: legacy[k] for k in ("url", "version", "license", "sha256")}
    items = [(entry["key"], data["sources"][entry["key"]]), ("downgrade", downgrade)]
    data["sources"] = dict(items[::-1] if reverse else items)
    if not selected:
        anchor = build(tmp_path, [entries[ANCHOR]], [ANCHOR])
        data["sources"].update(anchor["sources"])
        data["terms"] = anchor["terms"]
    with pytest.raises(ValueError):
        consume(tmp_path, data)
    with pytest.raises(ValueError):
        build(tmp_path, [legacy, entries[ANCHOR]], [ANCHOR])


@pytest.mark.parametrize("ident", TYPED)
def test_identical_owners_preserve_first_owner(tmp_path, ident):
    first = stage(tmp_path)[ident]
    second = {**copy.deepcopy(first), "key": "same-original"}
    for pair in ([first, second], [second, first]):
        data = build(tmp_path, pair, [ident])
        assert data["terms"][ident]["source"] == pair[0]["key"]
        assert consume(tmp_path, data) == data["terms"]


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize("attack", ["dtd", "hash", "encoding"])
def test_original_bytes_declared_encoding_and_hostile_xml(tmp_path, ident, attack):
    entry = stage(tmp_path)[ident]
    path = tmp_path / entry["path"]
    body = path.read_bytes()
    if attack == "dtd":
        body = body.replace(
            b"<ptools-xml", b'<!DOCTYPE ptools-xml [<!ENTITY attack "forged">]><ptools-xml', 1
        )
    elif attack == "encoding":
        body = body.replace(b"iso-8859-1", b"not-a-real-encoding", 1)
    else:
        body += b"\n"
    path.write_bytes(body)
    if attack != "hash":
        entry["sha256"] = hashlib.sha256(body).hexdigest()
    with pytest.raises((ValueError, LookupError)):
        metadata(entry, tmp_path)


def test_non_ascii_latin1_original_roundtrip(tmp_path):
    entry = stage(tmp_path)["MetaCyc:CPLX-926"]
    path = tmp_path / entry["path"]
    body = path.read_bytes().replace(b"The predicted", b"\xc9vidence. The predicted", 1)
    path.write_bytes(body)
    entry["sha256"] = hashlib.sha256(body).hexdigest()
    meta = metadata(entry, tmp_path)
    assert base64.b64decode(native(meta)["document"]["original_base64"]) == body
    assert "Évidence" in next(
        s["xml"] for s in projection(meta)["source_slots"] if s["tag"] == "comment"
    )
    assert consume(tmp_path, snapshot(meta, entry["key"]))


PATHWAY_BAD = [
    "missing-citation",
    "duplicate-citation",
    "missing-evidence",
    "wrong-evidence",
    "missing-link",
    "wrong-link-type",
    "wrong-link-target",
    "extra-link",
    "missing-member",
    "missing-layout",
    "cycle",
    "invalid-direction",
]


@pytest.mark.parametrize("attack", PATHWAY_BAD)
def test_pathway_evidence_links_and_route_grammar(tmp_path, attack):
    entry = stage(tmp_path)["MetaCyc:P321-PWY"]
    root = original(tmp_path, entry)
    e = root[1]
    if attack == "missing-citation":
        e.remove(e.find("citation"))
    elif attack == "duplicate-citation":
        citations = e.findall("citation")
        e.remove(citations[-1])
        e.append(copy.deepcopy(citations[0]))
    elif attack == "missing-evidence":
        e.remove(e.find("evidence"))
    elif attack == "wrong-evidence":
        e.find("evidence/Evidence-Code").set("orgid", "ECOLI")
    elif attack == "missing-link":
        e.remove(e.find("pathway-link"))
    elif attack == "wrong-link-type":
        e.find("pathway-link/Compound").tag = "Protein"
    elif attack == "wrong-link-target":
        e.find("pathway-link/link-target/Pathway").tag = "Reaction"
    elif attack == "extra-link":
        e.append(copy.deepcopy(e.find("pathway-link")))
    elif attack == "missing-member":
        listing = e.find("reaction-list")
        listing.remove(listing[0])
    elif attack == "missing-layout":
        e.remove(e.find("reaction-layout"))
    elif attack == "cycle":
        order = e.find("reaction-ordering")
        order.find("predecessor-reactions")[0].attrib = dict(order[0].attrib)
    elif attack == "invalid-direction":
        e.find("reaction-layout/direction").text = "SIDEWAYS"
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        metadata(entry, tmp_path)


REACTION_BAD = [
    "fad",
    "swap-states",
    "class",
    "compound",
    "parent",
    "direction",
    "coefficient-zero",
    "coefficient-negative",
    "activity",
    "enzyme",
    "reaction",
    "unknown-gibbs",
    "duplicate-gibbs",
    "unknown-publication",
    "missing-url",
    "ec",
]


@pytest.mark.parametrize("attack", REACTION_BAD)
def test_etf_reaction_typed_sides_complete_ancillary_and_backlinks(tmp_path, attack):
    entry = stage(tmp_path)["MetaCyc:R265-RXN"]
    root = original(tmp_path, entry)
    e = root[1]
    protein = e.find("left/Protein")
    if attack == "fad":
        protein.set("frameid", "FAD")
    elif attack == "swap-states":
        protein.attrib = dict(e.find("right/Protein").attrib)
    elif attack == "class":
        protein.set("class", "false")
    elif attack == "compound":
        protein.tag = "Compound"
    elif attack == "parent":
        e.find("parent/Reaction").set("frameid", "Electron-Transfer-Reactions")
    elif attack == "direction":
        e.find("reaction-direction").text = "PHYSIOL-LEFT-TO-RIGHT"
    elif attack.startswith("coefficient"):
        ET.SubElement(e.find("left"), "coefficient", {"datatype": "integer"}).text = (
            "0" if attack.endswith("zero") else "-1"
        )
    elif attack == "activity":
        e.find("enzymatic-reaction/Enzymatic-Reaction").set("frameid", "OTHER")
    elif attack in {"enzyme", "reaction"}:
        e.find("enzymatic-reaction/Enzymatic-Reaction/" + attack)[0].set("frameid", "OTHER")
    elif attack == "unknown-gibbs":
        ET.SubElement(e.find("gibbs-0"), "extra")
    elif attack == "duplicate-gibbs":
        e.find("gibbs-0").append(copy.deepcopy(e.find("gibbs-0/evidence")))
    elif attack == "unknown-publication":
        ET.SubElement(e.find("gibbs-0/evidence/Publication"), "extra")
    elif attack == "missing-url":
        p = e.find("gibbs-0/evidence/Publication")
        p.remove(p.find("url"))
    elif attack == "ec":
        e.find("ec-number").text = "EC-1.2.3.4"
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        metadata(entry, tmp_path)


def test_explicit_reaction_one_retains_presence_without_assembly_coercion(tmp_path):
    entry = stage(tmp_path)["MetaCyc:R265-RXN"]
    root = original(tmp_path, entry)
    ET.SubElement(root[1].find("left"), "coefficient", {"datatype": "integer"}).text = "1"
    save(tmp_path, entry, root)
    meta = metadata(entry, tmp_path)
    assert projection(meta)["sides"][0]["coefficient_explicit"] is True
    assert consume(tmp_path, snapshot(meta, entry["key"]))


@pytest.mark.parametrize("ident", ["MetaCyc:ETF-Reduced", "MetaCyc:ETF-Oxidized"])
@pytest.mark.parametrize(
    "attack", ["state", "parent", "duplicate-context", "class", "name", "credit"]
)
def test_etf_class_scope_and_full_context(tmp_path, ident, attack):
    entry = stage(tmp_path)[ident]
    root = original(tmp_path, entry)
    e = root[1]
    if attack == "state":
        slot = e.find("modified-form") if ident.endswith("Reduced") else e.find("unmodified-form")
        slot.remove(slot[0])
    elif attack == "parent":
        e.find("parent/Protein").set("frameid", "Ferredoxins")
    elif attack == "duplicate-context":
        listing = e.find("appears-in-left-side-of")
        listing.append(copy.deepcopy(listing[0]))
    elif attack == "class":
        e.set("class", "false")
    elif attack == "name":
        e.find("common-name").text = "FAD"
    elif attack == "credit":
        e.find("credits/revised/Person").set("orgid", "ECOLI")
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        metadata(entry, tmp_path)


def test_etf_pair_reaction_reciprocity(tmp_path):
    entries = stage(tmp_path)
    entry = entries["MetaCyc:ETF-Reduced"]
    root = original(tmp_path, entry)
    ref = root[1].find("appears-in-left-side-of/Reaction")
    ref.set("frameid", "OTHER-RXN")
    ref.set("resource", "getxml?META:OTHER-RXN")
    save(tmp_path, entry, root)
    metadata(entry, tmp_path)  # valid individual reference; incompatible paired context
    pair = [entries["MetaCyc:ETF-Reduced"], entries["MetaCyc:ETF-Oxidized"]]
    with pytest.raises(ValueError):
        build(tmp_path, pair, ["MetaCyc:ETF-Reduced"])
    data = snapshot(metadata(entry, tmp_path), entry["key"])
    other = pair[1]
    data["sources"][other["key"]] = metadata(other, tmp_path)
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize(
    "attack",
    [
        "coefficient",
        "component",
        "second-component",
        "parent",
        "activity",
        "enzyme",
        "reaction",
        "direct-name",
        "nested-name",
        "species",
    ],
)
def test_singleton_no_coefficient_inference_or_naming_chain_substitution(tmp_path, attack):
    entry = stage(tmp_path)["MetaCyc:CPLX-926"]
    root = original(tmp_path, entry)
    e = root[1]
    if attack == "coefficient":
        ET.SubElement(e.find("component"), "coefficient", {"datatype": "integer"}).text = "1"
    elif attack == "component":
        e.find("component/Protein").tag = "Compound"
    elif attack == "second-component":
        e.append(copy.deepcopy(e.find("component")))
    elif attack == "parent":
        e.find("parent/Protein").set("frameid", "Polypeptides")
    elif attack == "activity":
        e.find("catalyzes/Enzymatic-Reaction").set("frameid", "OTHER")
    elif attack in {"enzyme", "reaction"}:
        e.find("catalyzes/Enzymatic-Reaction/" + attack)[0].set("frameid", "OTHER")
    elif attack == "direct-name":
        ET.SubElement(e, "common-name", {"datatype": "string"}).text = "BadK"
    elif attack == "nested-name":
        act = e.find("catalyzes/Enzymatic-Reaction")
        label = act.find("common-name")
        act.remove(label)
        act.find("enzyme").append(label)
    elif attack == "species":
        e.find("species/Organism").set("frameid", "TAX-562")
    save(tmp_path, entry, root)
    with pytest.raises(ValueError):
        metadata(entry, tmp_path)


@pytest.mark.parametrize("ident", ["MetaCyc:G-545", "MetaCyc:G-550"])
@pytest.mark.parametrize(
    "attack",
    [
        "missing",
        "extra",
        "absolute",
        "traversal",
        "url",
        "version",
        "hash",
        "swap",
        "reciprocal",
        "species",
        "xref",
        "name",
        "parent",
        "product-type",
        "multiple-products",
        "kegg-field",
    ],
)
def test_gene_product_provenance_and_separate_native_shape(tmp_path, ident, attack):
    entries = stage(tmp_path)
    entry = entries[ident]
    if attack == "kegg-field":
        meta = metadata(entry, tmp_path)
        data = snapshot(meta, entry["key"])
        meta["native_gene"] = meta.pop("native_metacyc_gene")
        with pytest.raises(ValueError):
            consume(tmp_path, data)
        return
    child = entry["product_source"]
    if attack == "missing":
        del entry["product_source"]
    elif attack == "extra":
        child["extra"] = "forged"
    elif attack == "absolute":
        child["path"] = str(tmp_path / child["path"])
    elif attack == "traversal":
        child["path"] = "../outside.xml"
    elif attack == "url":
        child["url"] = child["url"].replace("META:", "ECOLI:")
    elif attack == "version":
        child["version"] = "26.0"
    elif attack == "hash":
        child["sha256"] = "0" * 64
    elif attack == "swap":
        entry["product_source"] = entries[
            "MetaCyc:G-550" if ident.endswith("545") else "MetaCyc:G-545"
        ]["product_source"]
    elif attack in {"reciprocal", "species", "xref"}:
        root = original(tmp_path, child)
        if attack == "reciprocal":
            root[1].find("gene/Gene").set("frameid", "OTHER")
        elif attack == "species":
            root[1].find("species/Organism").set("frameid", "TAX-562")
        else:
            next(n for n in root[1].findall("dblink") if n.findtext("dblink-db") == "UNIPROT").find(
                "dblink-oid"
            ).text = "P00000"
        save(tmp_path, child, root)
    else:
        root = original(tmp_path, entry)
        if attack == "name":
            root[1].find("common-name").text = "badR"
        elif attack == "parent":
            root[1].find("parent/Gene").set("frameid", "Pseudogenes")
        elif attack == "product-type":
            root[1].find("product/Protein").tag = "Gene"
        elif attack == "multiple-products":
            root[1].find("product").append(copy.deepcopy(root[1].find("product/Protein")))
        save(tmp_path, entry, root)
    with pytest.raises((ValueError, KeyError)):
        metadata(entry, tmp_path)


@pytest.mark.parametrize("ident", TYPED)
@pytest.mark.parametrize("attack", ["category", "label"])
def test_native_placement_and_canonical_labels_before_exemptions(tmp_path, ident, attack):
    entries = stage(tmp_path)
    data = build(tmp_path, list(entries.values()), EXPECTED)
    repo = tmp_path / "repo"
    (repo / "conf").mkdir(parents=True)
    (repo / "data/pathways").mkdir(parents=True)
    cfg = {
        "version": 1,
        "namespaces": {
            "MetaCyc": {"snapshot": "data/authority.json", "policy": "canonical_or_synonym"}
        },
        "contextual_labels": [
            {
                "namespace": "MetaCyc",
                "sections": ["participants", "reactions", "taxa"],
                "record_prefixes": ["MetaCyc"],
                "reason": "adversarial broad exemption",
            }
        ],
    }
    (repo / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(cfg))
    (repo / "data/authority.json").write_text(json.dumps(data))
    node = {"id": ident, "label": data["terms"][ident]["label"]}
    entity = data["terms"][ident].get("entity_type")
    category = {
        "native_gene": "gene",
        "protein_class": "protein",
        "protein_complex": "complex",
        "reaction": "molecular_activity",
    }.get(entity)
    record = {
        "id": "MetaCyc:P321-PWY",
        "label": data["terms"]["MetaCyc:P321-PWY"]["label"],
        "participants": [],
        "reactions": [],
        "taxa": [],
    }
    if entity == "native_pathway":
        if attack == "category":
            record["participants"].append({**node, "category": "chemical_entity"})
        else:
            record["label"] = "forged"
    else:
        section = "reactions" if entity == "reaction" else "participants"
        record[section].append({**node, "category": category})
        if attack == "category":
            record[section][0]["category"] = "chemical_entity"
        else:
            record[section][0]["label"] = "forged"
    path = repo / "data/pathways/record.yaml"
    path.write_text(yaml.safe_dump(record))
    errors = identifier_errors(repo)
    if entity == "reaction" and attack == "label":
        assert not errors, errors  # unnamed reaction still permits contextual display
    else:
        assert any(
            ("ENTITY_TYPE_MISMATCH" if attack == "category" else "LABEL_MISMATCH") in e
            for e in errors
        ), errors


GENE_PRODUCTS = [("MetaCyc:G-545", "MetaCyc:MONOMER-888"), ("MetaCyc:G-550", "MetaCyc:MONOMER-893")]


def gene_product_pair(entries, gene_id, product_id):
    gene = entries[gene_id]
    product = {
        **copy.deepcopy(gene["product_source"]),
        "key": "standalone-" + product_id.split(":", 1)[1],
        "kind": "metacyc-protein-xml",
    }
    return gene, product


def merged_ordinary_product_snapshots(
    tmp_path, gene, product, gene_id, product_id, reverse, selected
):
    # Use actual native-builder outputs: ordinary output deliberately has no kind.
    gene_data = build(tmp_path, [gene], [gene_id])
    product_data = build(tmp_path, [product], [product_id])
    assert set(product_data["sources"][product["key"]]) == {"url", "version", "sha256", "license"}
    parts = [gene_data, product_data][::-1] if reverse else [gene_data, product_data]
    wanted = {"gene": {gene_id}, "product": {product_id}, "both": {gene_id, product_id}}[selected]
    combined = {
        "version": 1,
        "sources": {k: v for part in parts for k, v in part["sources"].items()},
        "terms": {k: v for part in parts for k, v in part["terms"].items() if k in wanted},
    }
    return combined


@pytest.mark.parametrize(("gene_id", "product_id"), GENE_PRODUCTS)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", ["gene", "product", "both"])
@pytest.mark.parametrize("surface", ["producer", "consumer"])
def test_exact_ordinary_gene_product_coexistence(
    tmp_path, gene_id, product_id, reverse, selected, surface
):
    entries = stage(tmp_path)
    gene, product = gene_product_pair(entries, gene_id, product_id)
    combined = merged_ordinary_product_snapshots(
        tmp_path, gene, product, gene_id, product_id, reverse, selected
    )
    before = copy.deepcopy(combined)
    if surface == "producer":
        pair = [gene, product][::-1] if reverse else [gene, product]
        actual = build(tmp_path, pair, combined["terms"])
        assert actual["terms"] == combined["terms"]
        assert all(value == combined["sources"][key] for key, value in actual["sources"].items())
        assert consume(tmp_path, actual) == actual["terms"]
    else:
        # Preserve both sources even when one has no selected term.
        assert consume(tmp_path, combined) == combined["terms"]
    assert combined == before


@pytest.mark.parametrize(("gene_id", "product_id"), GENE_PRODUCTS)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", ["gene", "product", "both"])
@pytest.mark.parametrize("attack", ["original", "version", "wrong-kind", "request-only-kind"])
def test_ordinary_gene_product_producer_conflicts_stay_closed(
    tmp_path, gene_id, product_id, reverse, selected, attack
):
    entries = stage(tmp_path)
    gene, product = gene_product_pair(entries, gene_id, product_id)
    if attack == "original":
        body = (tmp_path / product["path"]).read_bytes() + b"\n"
        product["path"] = "different-product.xml"
        (tmp_path / product["path"]).write_bytes(body)
        product["sha256"] = hashlib.sha256(body).hexdigest()
    elif attack == "version":
        product["version"] = "27.1"
    elif attack == "wrong-kind":
        product["kind"] = "metacyc-reaction-xml"
    else:
        product["kind"] = "metacyc-html"
    pair = [gene, product][::-1] if reverse else [gene, product]
    wanted = {"gene": [gene_id], "product": [product_id], "both": [gene_id, product_id]}[selected]
    with pytest.raises(ValueError, match="gene product owner differs"):
        build(tmp_path, pair, wanted)


@pytest.mark.parametrize(("gene_id", "product_id"), GENE_PRODUCTS)
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", ["gene", "product", "both"])
@pytest.mark.parametrize(
    "attack",
    [
        "hash",
        "version",
        "request-only-url",
        "wrong-kind",
        "invented-ordinary-kind",
        "extra-provenance",
    ],
)
def test_ordinary_gene_product_consumer_conflicts_stay_closed(
    tmp_path, gene_id, product_id, reverse, selected, attack
):
    entries = stage(tmp_path)
    gene, product = gene_product_pair(entries, gene_id, product_id)
    combined = merged_ordinary_product_snapshots(
        tmp_path, gene, product, gene_id, product_id, reverse, selected
    )
    owner = combined["sources"][product["key"]]
    if attack == "hash":
        owner["sha256"] = "0" * 64
    elif attack == "version":
        owner["version"] = "27.1"
    elif attack == "request-only-url":
        owner["url"] = "https://biocyc.org/getxml?id=META%3A" + product_id.split(":", 1)[1]
    elif attack == "wrong-kind":
        owner["kind"] = "metacyc-reaction-xml"
    elif attack == "invented-ordinary-kind":
        owner["kind"] = "metacyc-protein-xml"
    else:
        owner["sha256_scope"] = "unsupported-extra"
    with pytest.raises(ValueError):
        consume(tmp_path, combined)
