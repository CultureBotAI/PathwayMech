"""Bounded native class/state/reaction fixtures; whole originals replay separately."""

from __future__ import annotations

import copy
import hashlib
import json
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.biocyc_carrier import CARRIER_CLASS_KIND, class_metadata, class_term
from pathwaymech.ecocyc_state import ECOCYC_STATE_KIND, state_metadata, state_term
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import _metacyc_reaction_record, build_snapshot

HOST = "bf2i-artsymbiocyc.insa-lyon.fr"
SHAPES = ["class-red", "class-ox", "class-compound", "state-red", "state-ox"]


def envelope(frame, pgdb="META", tag="Protein", is_class=True):
    taxon = """<strain datatype="string">K-12 substr. MG1655</strain><dblink>
      <dblink-db>NCBI-TAXONOMY-DB</dblink-db><dblink-oid>511145</dblink-oid>
      <dblink-relationship>unification</dblink-relationship><dblink-URL>http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=511145</dblink-URL></dblink>"""
    return ET.fromstring(f'''<ptools-xml ptools-version="27.0" xml:base="http://{HOST}:443/getxml?{pgdb}:{frame}">
      <metadata><url>http://{HOST}:443/</url><service_name>getxml</service_name><query>{pgdb}:{frame}</query><num_results>1</num_results>
      <PGDB orgid="{pgdb}" version="27.0"><species datatype="string">'''
        f'''{"MetaCyc" if pgdb == "META" else "Escherichia coli"}</species>'''
        f'''{taxon if pgdb == "ECOLI" else ""}</PGDB></metadata>
      <{tag} ID="{pgdb}:{frame}" orgid="{pgdb}" frameid="{frame}" detail="full"'''
        f'''{' class="true"' if is_class else ""}/></ptools-xml>''')


def ref(entity, slot, frame, *, pgdb="META", tag="Protein", is_class=True):
    wrapper = ET.SubElement(entity, slot)
    attrs = {"resource": f"getxml?{pgdb}:{frame}", "orgid": pgdb, "frameid": frame}
    if is_class:
        attrs["class"] = "true"
    ET.SubElement(wrapper, tag, attrs)
    return wrapper


def document(shape, *, suffix=""):
    state = shape.startswith("state")
    pgdb = "ECOLI" if state else "META"
    oxidized = shape.endswith("ox")
    compound = shape.endswith("compound")
    frame = ("CLIENT" if compound else "OX" if oxidized else "RED") + suffix
    tag = "Compound" if compound else "Protein"
    root = envelope(frame, pgdb, tag, not state)
    entity = root.find(tag)
    parents = (
        ["Hydride-Acceptors"]
        if compound
        else ["Modified-Proteins", "Ox-Thioredoxin" if state else "Thioredoxin"]
        if oxidized
        else ["Red-Thioredoxin" if state else "Thioredoxin"]
    )
    for parent in parents:
        ref(entity, "parent", parent, pgdb=pgdb, tag=tag)
    ET.SubElement(entity, "common-name", datatype="string").text = "a native " + shape
    ET.SubElement(entity, "synonym", datatype="string").text = "NativeAlias"
    if not compound:
        ref(
            entity,
            "unmodified-form" if oxidized else "modified-form",
            ("RED" if oxidized else "OX") + suffix,
            pgdb=pgdb,
            is_class=not state,
        )
    if state:
        ref(entity, "gene", "GENE" + suffix, pgdb=pgdb, tag="Gene", is_class=False)
    return root


def original(tmp_path, root, name, pgdb, frame):
    path = tmp_path / name
    path.write_bytes(ET.tostring(root, encoding="utf-8", xml_declaration=True))
    return {
        "path": name,
        "url": f"https://{HOST}/getxml?id={pgdb}:{frame}",
        "version": "27.0",
        "license": "Synthetic native-shaped fixture",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def entry(tmp_path, shape="class-red", *, root=None, partner=None, key="native", suffix=""):
    default = document(shape, suffix=suffix)
    entity = list(default)[1]
    pgdb, frame = entity.get("orgid"), entity.get("frameid")
    result = {
        "key": key,
        "kind": ECOCYC_STATE_KIND if shape.startswith("state") else CARRIER_CLASS_KIND,
        **original(tmp_path, default if root is None else root, key + ".xml", pgdb, frame),
    }
    if shape.startswith("state"):
        other = document("state-red" if shape.endswith("ox") else "state-ox", suffix=suffix)
        other_frame = other.find("Protein").get("frameid")
        result["counterpart_source"] = original(
            tmp_path, other if partner is None else partner, key + ".partner.xml", pgdb, other_frame
        )
    return result


def metadata(item, tmp_path):
    return (state_metadata if item["kind"] == ECOCYC_STATE_KIND else class_metadata)(item, tmp_path)


def term(item, tmp_path):
    return (state_term if item["kind"] == ECOCYC_STATE_KIND else class_term)(
        metadata(item, tmp_path), item["key"]
    )


def snapshot(tmp_path, entries, selected=None):
    records = tmp_path / "records"
    records.mkdir(exist_ok=True)
    if selected is None:
        selected = term(entries[0], tmp_path)[0]
    (records / "fixture.yaml").write_text(yaml.safe_dump({"id": selected}))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize("suffix", ["", "-SECOND.17"])
def test_typed_native_shapes_roundtrip_without_accession_allowlists(tmp_path, shape, suffix):
    item = entry(tmp_path, shape, suffix=suffix)
    identifier, expected = term(item, tmp_path)
    data = snapshot(tmp_path, [item])
    assert data["terms"] == {identifier: expected}
    assert expected["entity_type"] == (
        "protein_state"
        if shape.startswith("state")
        else "chemical_class"
        if shape.endswith("compound")
        else "protein_class"
    )
    assert expected["label"] == "a native " + shape and expected["synonyms"] == ["NativeAlias"]
    path = tmp_path / "authority.json"
    path.write_text(json.dumps(data))
    assert _load_authority(path) == data["terms"]
    if shape.startswith("state"):
        native = data["sources"]["native"]["native_protein_state"]
        other = data["sources"]["native"]["counterpart"]["native_protein_state"]
        assert (
            native["gene"] == other["gene"]
            and native["state_link"]["id"] == other["id"]
            and other["state_link"]["id"] == native["id"]
        )


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize(
    "problem",
    [
        "top-class",
        "top-id",
        "top-resource",
        "top-detail",
        "top-extra",
        "native-version",
        "pgdb",
        "species",
        "query",
        "base",
        "results",
        "metadata-extra",
        "two-entities",
        "no-parent",
        "duplicate-parent",
        "wrong-parent",
        "parent-type",
        "parent-class",
        "parent-org",
        "parent-resource",
        "parent-text",
        "parent-tail",
        "parent-extra",
        "parent-child",
        "common-missing",
        "common-empty",
        "common-duplicate",
        "common-type",
        "common-nested",
        "common-frame",
        "unsafe-name",
        "unknown-entity",
        "unsafe-synonym",
        "empty-synonym",
        "duplicate-synonym",
        "hidden-parent",
        "component",
        "unexpected",
    ],
)
def test_malformed_native_shape_rejected_before_filtering(tmp_path, shape, problem):
    root = document(shape)
    entity = list(root)[1]
    parent = entity.find("parent")
    node = parent[0]
    # Some whole issuing originals have no synonyms. These cases add the
    # malformed/duplicate slot explicitly rather than assuming one existed.
    if (
        problem in {"unsafe-synonym", "empty-synonym", "duplicate-synonym"}
        and entity.find("synonym") is None
    ):
        ET.SubElement(entity, "synonym", datatype="string").text = "Mutation-only alias"
    if problem == "top-class":
        entity.set("class", "false" if not shape.startswith("state") else "true")
    elif problem == "top-id":
        entity.set("ID", "META:OTHER")
    elif problem == "top-resource":
        entity.set("resource", "#META:RED")
    elif problem == "top-detail":
        entity.set("detail", "low")
    elif problem == "top-extra":
        entity.set("surprise", "true")
    elif problem == "native-version":
        root.set("ptools-version", "28.0")
    elif problem == "pgdb":
        root.find("metadata/PGDB").set("orgid", "OTHER")
    elif problem == "species":
        root.find("metadata/PGDB/species").text = "Unknown organism"
    elif problem == "query":
        root.find("metadata/query").text = "META:OTHER"
    elif problem == "base":
        root.set(
            "{http://www.w3.org/XML/1998/namespace}base", "https://example.org/getxml?id=META:RED"
        )
    elif problem == "results":
        root.find("metadata/num_results").text = "2"
    elif problem == "metadata-extra":
        ET.SubElement(root.find("metadata"), "unexpected")
    elif problem == "two-entities":
        root.append(copy.deepcopy(entity))
    elif problem == "no-parent":
        entity.remove(parent)
    elif problem == "duplicate-parent":
        entity.append(copy.deepcopy(parent))
    elif problem == "wrong-parent":
        node.set("frameid", "Protein-Complexes")
        node.set("resource", "getxml?" + node.get("orgid") + ":Protein-Complexes")
    elif problem == "parent-type":
        node.tag = "Gene"
    elif problem == "parent-class":
        node.set("class", "TRUE")
    elif problem == "parent-org":
        node.set("orgid", "OTHER")
    elif problem == "parent-resource":
        node.set("resource", "#META:Thioredoxin")
    elif problem == "parent-text":
        parent.text = "hidden"
    elif problem == "parent-tail":
        node.tail = "hidden"
    elif problem == "parent-extra":
        parent.set("class", "true")
    elif problem == "parent-child":
        ET.SubElement(node, "surprise")
    elif problem == "common-missing":
        entity.remove(entity.find("common-name"))
    elif problem == "common-empty":
        entity.find("common-name").text = ""
    elif problem == "common-duplicate":
        entity.append(copy.deepcopy(entity.find("common-name")))
    elif problem == "common-type":
        entity.find("common-name").set("datatype", "symbol")
    elif problem == "common-nested":
        ET.SubElement(entity.find("common-name"), "b").text = "nested"
    elif problem == "common-frame":
        entity.find("common-name").text = entity.get("frameid")
    elif problem == "unsafe-name":
        entity.find("common-name").text = "<script>bad</script>"
    elif problem == "unknown-entity":
        entity.find("common-name").text = "unresolved &foo;"
    elif problem == "unsafe-synonym":
        entity.find("synonym").text = '<i onclick="bad">unsafe</i>'
    elif problem == "empty-synonym":
        entity.find("synonym").text = ""
    elif problem == "duplicate-synonym":
        entity.append(copy.deepcopy(entity.find("synonym")))
    elif problem == "hidden-parent":
        entity.remove(parent)
        ET.SubElement(entity, "wrapper").append(parent)
    else:
        ET.SubElement(entity, problem)
    item = entry(tmp_path, shape, root=root)
    with pytest.raises(ValueError):
        snapshot(tmp_path, [item], selected="MetaCyc:UNSELECTED")


@pytest.mark.parametrize("shape", ["class-red", "class-ox", "state-red", "state-ox"])
@pytest.mark.parametrize(
    "problem",
    [
        "self",
        "missing",
        "both",
        "duplicate",
        "class",
        "org",
        "type",
        "embedded",
        "extra-wrapper",
        "wrong-relation",
    ],
)
def test_state_link_identity_grammar_is_closed(tmp_path, shape, problem):
    root = document(shape)
    entity = root.find("Protein")
    relation = "unmodified-form" if shape.endswith("ox") else "modified-form"
    link = entity.find(relation)
    node = link[0]
    if problem == "self":
        node.set("frameid", entity.get("frameid"))
        node.set("resource", "getxml?" + entity.get("ID"))
    elif problem == "missing":
        entity.remove(link)
    elif problem == "both":
        extra = copy.deepcopy(link)
        extra.tag = "modified-form" if relation == "unmodified-form" else "unmodified-form"
        entity.append(extra)
    elif problem == "duplicate":
        entity.append(copy.deepcopy(link))
    elif problem == "class":
        node.set("class", "true" if shape.startswith("state") else "false")
    elif problem == "org":
        node.set("orgid", "OTHER")
    elif problem == "type":
        node.tag = "Compound"
    elif problem == "embedded":
        ET.SubElement(node, "common-name").text = "nested"
    elif problem == "extra-wrapper":
        link.set("class", "true")
    else:
        link.tag = "modified-form" if relation == "unmodified-form" else "unmodified-form"
    with pytest.raises(ValueError):
        metadata(entry(tmp_path, shape, root=root), tmp_path)


@pytest.mark.parametrize(
    "problem",
    [
        "missing",
        "hash",
        "url",
        "version",
        "absolute",
        "traversal",
        "extra",
        "self-path",
        "gene",
        "reciprocal",
        "same-relation",
        "strain",
        "taxon",
        "gene-duplicate",
        "gene-class",
    ],
)
def test_counterpart_is_separate_hash_bound_reciprocal_same_gene(tmp_path, problem):
    root = document("state-red")
    partner = document("state-ox")
    if problem == "gene":
        partner.find("Protein/gene/Gene").set("frameid", "OTHER")
        partner.find("Protein/gene/Gene").set("resource", "getxml?ECOLI:OTHER")
    elif problem == "reciprocal":
        partner.find("Protein/unmodified-form/Protein").set("frameid", "OTHER")
        partner.find("Protein/unmodified-form/Protein").set("resource", "getxml?ECOLI:OTHER")
    elif problem == "same-relation":
        partner.find("Protein/unmodified-form").tag = "modified-form"
    elif problem == "strain":
        partner.find("metadata/PGDB/strain").text = "another strain"
    elif problem == "taxon":
        partner.find("metadata/PGDB/dblink/dblink-oid").text = "562"
    elif problem == "gene-duplicate":
        partner.find("Protein").append(copy.deepcopy(partner.find("Protein/gene")))
    elif problem == "gene-class":
        partner.find("Protein/gene/Gene").set("class", "true")
    item = entry(tmp_path, "state-red", root=root, partner=partner)
    if problem == "missing":
        del item["counterpart_source"]
    elif problem in {"hash", "url", "version", "absolute", "traversal", "extra", "self-path"}:
        key, value = {
            "hash": ("sha256", "0" * 64),
            "url": ("url", "https://example.org/RED"),
            "version": ("version", "28.0"),
            "absolute": ("path", "/tmp/partner.xml"),
            "traversal": ("path", "../partner.xml"),
            "extra": ("unexpected", True),
            "self-path": ("path", item["path"]),
        }[problem]
        item["counterpart_source"][key] = value
        if problem == "self-path":
            item["counterpart_source"]["sha256"] = item["sha256"]
    with pytest.raises(ValueError):
        metadata(item, tmp_path)


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize(
    "problem",
    [
        "url",
        "hash",
        "absolute",
        "traversal",
        "kind",
        "extra",
        "unrelated-class-proof",
        "unrelated-counterpart",
    ],
)
def test_manifest_guard_scope(tmp_path, shape, problem):
    item = entry(tmp_path, shape)
    key, value = {
        "url": ("url", "http://" + HOST + "/getxml?id=META:RED"),
        "hash": ("sha256", "0" * 64),
        "absolute": ("path", "/tmp/source.xml"),
        "traversal": ("path", "../source.xml"),
        "kind": ("kind", "untyped"),
        "extra": ("extra", True),
        "unrelated-class-proof": ("class_source", {}),
        "unrelated-counterpart": ("counterpart_source", {}),
    }[problem]
    item[key] = value
    with pytest.raises((ValueError, KeyError)):
        metadata(item, tmp_path)


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize("encoding", ["utf-8", "utf-16"])
def test_doctype_entities_do_not_expand(tmp_path, shape, encoding):
    item = entry(tmp_path, shape)
    path = tmp_path / item["path"]
    body = (
        f'<?xml version="1.0" encoding="{encoding}"?><!DOCTYPE ptools-xml [<!ENTITY x SYSTEM "file:///invalid">]>'
        + ET.tostring(document(shape), encoding="unicode")
    )
    path.write_bytes(body.encode(encoding))
    item["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    with pytest.raises(ValueError, match="DOCTYPE"):
        metadata(item, tmp_path)


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize(
    "problem",
    [
        "entity-type",
        "label",
        "synonyms",
        "identifier",
        "source-kind",
        "label-kind",
        "native-type",
        "class-bool",
        "unknown-key",
        "parents",
        "link",
        "counterpart",
    ],
)
def test_consumer_rejects_forged_typed_metadata_and_terms(tmp_path, shape, problem):
    item = entry(tmp_path, shape)
    data = snapshot(tmp_path, [item])
    identifier = next(iter(data["terms"]))
    typed = data["terms"][identifier]
    meta = data["sources"]["native"]
    key = "native_protein_state" if shape.startswith("state") else "native_carrier_class"
    native = meta[key]
    if problem == "entity-type":
        typed["entity_type"] = "reaction"
    elif problem == "label":
        typed["label"] = "fabricated"
    elif problem == "synonyms":
        typed["synonyms"].append("fabricated")
    elif problem == "identifier":
        data["terms"][identifier + "X"] = data["terms"].pop(identifier)
    elif problem == "source-kind":
        meta["kind"] = "metacyc-protein-xml"
    elif problem == "label-kind":
        typed["label_kind"] = "source_context"
    elif problem == "native-type":
        native["native_type"] = "RNA"
    elif problem == "class-bool":
        native["is_class"] = 0 if shape.startswith("state") else 1
    elif problem == "unknown-key":
        native["surprise"] = True
    elif problem == "parents":
        native["parent_classes"] = ["Protein-Complexes"]
    elif problem == "link":
        native["state_link"] = {"kind": "modified-form", "id": identifier}
    else:
        meta["counterpart"] = {"bad": True}
    path = tmp_path / "forged.json"
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError):
        _load_authority(path)


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize(
    "section,category",
    [
        ("record", None),
        ("taxa", "taxon"),
        ("reactions", "molecular_activity"),
        ("participants", "complex"),
        ("participants", "small_molecule"),
        ("participants", "cofactor"),
        ("participants", "gene"),
    ],
)
def test_placement_precedes_contextual_bypass(tmp_path, shape, section, category):
    item = entry(tmp_path, shape)
    data = snapshot(tmp_path, [item])
    identifier, typed = next(iter(data["terms"].items()))
    data["sources"]["legacy"] = {
        "url": "https://example.org/native",
        "version": "1",
        "sha256": "0" * 64,
        "license": "fixture",
    }
    data["terms"]["MetaCyc:TEST"] = {"label": "test pathway", "synonyms": [], "source": "legacy"}
    (tmp_path / "authority.json").write_text(json.dumps(data))
    node = {"id": identifier, "label": typed["label"], "category": category}
    record = {
        "id": "MetaCyc:TEST",
        "label": "test pathway",
        "taxa": [],
        "participants": [],
        "reactions": [],
    }
    if section == "record":
        record.update(node)
    else:
        record[section] = [node]
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    (records / "test.yaml").write_text(yaml.safe_dump(record))
    namespaces = {
        prefix: {"snapshot": "authority.json", "policy": "canonical_or_synonym"}
        for prefix in {"MetaCyc", identifier.split(":")[0]}
    }
    policy = {
        "version": 1,
        "namespaces": namespaces,
        "contextual_labels": [
            {
                "namespace": prefix,
                "sections": ["record", "taxa", "participants", "reactions"],
                "record_prefixes": list(namespaces),
                "reason": "Broad fixture context",
            }
            for prefix in namespaces
        ],
    }
    path = tmp_path / "policy.yaml"
    path.write_text(yaml.safe_dump(policy))
    assert any("ENTITY_TYPE_MISMATCH" in error for error in identifier_errors(tmp_path, path))


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize(
    "policy,label,passes",
    [
        ("canonical", "a native SHAPE", True),
        ("canonical", "NativeAlias", False),
        ("canonical_or_synonym", "NativeAlias", True),
        ("canonical_or_synonym", "fabricated state", False),
    ],
)
def test_names_enforced_even_under_broad_context(tmp_path, shape, policy, label, passes):
    item = entry(tmp_path, shape)
    data = snapshot(tmp_path, [item])
    identifier, typed = next(iter(data["terms"].items()))
    data["sources"]["legacy"] = {
        "url": "https://example.org/native",
        "version": "1",
        "sha256": "0" * 64,
        "license": "fixture",
    }
    data["terms"]["MetaCyc:TEST"] = {"label": "test pathway", "synonyms": [], "source": "legacy"}
    (tmp_path / "authority.json").write_text(json.dumps(data))
    node = {
        "id": identifier,
        "label": label.replace("SHAPE", shape),
        "category": "chemical_entity" if shape.endswith("compound") else "protein",
    }
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    (records / "test.yaml").write_text(
        yaml.safe_dump(
            {
                "id": "MetaCyc:TEST",
                "label": "test pathway",
                "taxa": [],
                "participants": [node],
                "reactions": [],
            }
        )
    )
    namespaces = {
        prefix: {"snapshot": "authority.json", "policy": policy}
        for prefix in {"MetaCyc", identifier.split(":")[0]}
    }
    cfg = {
        "version": 1,
        "namespaces": namespaces,
        "contextual_labels": [
            {
                "namespace": prefix,
                "sections": ["record", "participants"],
                "record_prefixes": ["MetaCyc"],
                "reason": "Broad fixture context",
            }
            for prefix in namespaces
        ],
    }
    path = tmp_path / "policy.yaml"
    path.write_text(yaml.safe_dump(cfg))
    errors = identifier_errors(tmp_path, path)
    assert (not errors) == passes
    if not passes:
        assert any("LABEL_MISMATCH" in error for error in errors)


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("reverse", [True, False])
def test_conflicts_precede_corpus_filter_in_both_orders(tmp_path, shape, selected, reverse):
    first = entry(tmp_path, shape, key="first")
    root = document(shape)
    list(root)[1].find("common-name").text = "a different native name"
    second = entry(tmp_path, shape, root=root, key="second")
    entries = [first, second]
    identifier = term(first, tmp_path)[0]
    with pytest.raises(ValueError, match="conflicting"):
        snapshot(
            tmp_path,
            entries[::-1] if reverse else entries,
            identifier if selected else "MetaCyc:UNSELECTED",
        )


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_typed_class_cannot_be_overwritten_by_legacy_html(tmp_path, reverse, selected):
    first = entry(tmp_path)
    path = tmp_path / "legacy.html"
    path.write_text(
        "<TITLE>MetaCyc a native class-red</TITLE>"
        "<script>typeObjectPage = {object:'RED',orgid:'META'}</script>"
    )
    second = {
        **first,
        "kind": "metacyc-html",
        "key": "legacy",
        "path": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    with pytest.raises(ValueError, match="carrier-class identity scope"):
        snapshot(
            tmp_path,
            [second, first] if reverse else [first, second],
            "MetaCyc:RED" if selected else "MetaCyc:UNSELECTED",
        )


def test_counterpart_assertions_conflict_even_when_only_the_other_node_selected(tmp_path):
    first = entry(tmp_path, "state-red", key="first")
    primary = document("state-ox")
    partner = document("state-red")
    for root in (primary, partner):
        node = root.find("Protein/gene/Gene")
        node.set("frameid", "OTHER")
        node.set("resource", "getxml?ECOLI:OTHER")
    second = entry(tmp_path, "state-ox", root=primary, partner=partner, key="second")
    with pytest.raises(ValueError, match="conflicting EcoCyc"):
        snapshot(tmp_path, [first, second], "EcoCyc:OX")


def reaction():
    root = envelope("RXN", tag="Reaction", is_class=False)
    entity = root.find("Reaction")
    ref(entity, "parent", "Protein-Modification-Reactions", tag="Reaction")
    ET.SubElement(entity, "reaction-direction").text = "RIGHT-TO-LEFT"
    ref(entity, "left", "OX")
    ref(entity, "right", "RED")
    ref(entity, "left", "DONOR", tag="Compound")
    ref(entity, "right", "ACCEPTOR", tag="Compound")
    ET.SubElement(entity, "orphan").text = "YES-PUTATIVE"
    ET.SubElement(entity, "physiologically-relevant", datatype="boolean").text = "true"
    return root


def parse_reaction(tmp_path, root):
    item = original(tmp_path, root, "reaction.xml", "META", "RXN")
    return _metacyc_reaction_record(
        tmp_path / item["path"], url=item["url"], version=item["version"]
    )


def test_protein_reaction_preserves_typed_class_sides_and_flags(tmp_path):
    typed, assertion = parse_reaction(tmp_path, reaction())
    assert typed == ("MetaCyc:RXN", "RXN", [])
    assert assertion == (
        "27.0",
        ("Protein-Modification-Reactions",),
        "RIGHT-TO-LEFT",
        (("Compound", "DONOR", "true"), ("Protein", "OX", "true")),
        (("Compound", "ACCEPTOR", "true"), ("Protein", "RED", "true")),
        (("physiologically-relevant", "true"), ("orphan", "YES-PUTATIVE")),
    )


@pytest.mark.parametrize(
    "problem",
    [
        "parent-union",
        "parent-duplicate",
        "parent-missing",
        "parent-wrong",
        "parent-tag",
        "protein-instance",
        "protein-false",
        "protein-upper",
        "protein-empty",
        "compound-false",
        "compound-upper",
        "compound-empty",
        "wrapper-class",
        "extra-child",
        "missing-child",
        "gene",
        "rna",
        "child-text",
        "child-child",
        "wrapper-text",
        "coefficient",
        "compartment",
        "wrong-org",
        "wrong-resource",
        "wrong-frame",
        "extra-id",
        "embedded",
        "duplicate-side",
        "cross-type-duplicate",
        "no-left-protein",
        "no-right-protein",
        "empty-left",
        "direct-name",
        "empty-name",
    ],
)
def test_reaction_mode_does_not_relax_other_grammar(tmp_path, problem):
    root = reaction()
    entity = root.find("Reaction")
    slot = entity.find("left")
    node = slot[0]
    parent = entity.find("parent")
    if problem == "parent-union":
        ref(entity, "parent", "Chemical-Reactions", tag="Reaction")
    elif problem == "parent-duplicate":
        entity.append(copy.deepcopy(parent))
    elif problem == "parent-missing":
        entity.remove(parent)
    elif problem == "parent-wrong":
        parent[0].set("frameid", "Chemical-Reactions")
        parent[0].set("resource", "getxml?META:Chemical-Reactions")
    elif problem == "parent-tag":
        parent[0].tag = "Protein"
    elif problem == "protein-instance":
        node.attrib.pop("class")
    elif problem in {"protein-false", "protein-upper", "protein-empty"}:
        node.set(
            "class",
            {"protein-false": "false", "protein-upper": "TRUE", "protein-empty": ""}[problem],
        )
    elif problem in {"compound-false", "compound-upper", "compound-empty"}:
        entity.find("right/Compound").set(
            "class",
            {"compound-false": "false", "compound-upper": "TRUE", "compound-empty": ""}[problem],
        )
    elif problem == "wrapper-class":
        slot.set("class", "true")
    elif problem == "extra-child":
        slot.append(copy.deepcopy(node))
    elif problem == "missing-child":
        slot.remove(node)
    elif problem == "gene":
        node.tag = "Gene"
    elif problem == "rna":
        node.tag = "RNA"
    elif problem == "child-text":
        node.text = "hidden"
    elif problem == "child-child":
        ET.SubElement(node, "other")
    elif problem == "wrapper-text":
        slot.text = "hidden"
    elif problem in {"coefficient", "compartment"}:
        ET.SubElement(slot, problem).text = "1"
    elif problem == "wrong-org":
        node.set("orgid", "ECOLI")
    elif problem == "wrong-resource":
        node.set("resource", "getxml?META:OTHER")
    elif problem == "wrong-frame":
        node.set("frameid", "bad frame")
    elif problem == "extra-id":
        node.set("ID", "META:OX")
    elif problem == "embedded":
        node.set("detail", "full")
    elif problem == "duplicate-side":
        entity.append(copy.deepcopy(slot))
    elif problem == "cross-type-duplicate":
        extra = copy.deepcopy(slot)
        extra[0].tag = "Compound"
        entity.append(extra)
    elif problem == "no-left-protein":
        entity.remove(slot)
    elif problem == "no-right-protein":
        entity.remove(entity.find("right"))
    elif problem == "empty-left":
        for row in entity.findall("left"):
            entity.remove(row)
    else:
        ET.SubElement(entity, "common-name", datatype="string").text = (
            "name" if problem == "direct-name" else ""
        )
    with pytest.raises(ValueError):
        parse_reaction(tmp_path, root)


def test_new_reaction_assertion_conflict_retains_xml_type(tmp_path):
    first = reaction()
    ref(first.find("Reaction"), "left", "OTHER-PROTEIN")
    second = copy.deepcopy(first)
    second.find("Reaction/left/Protein").tag = "Compound"
    items = []
    for key, root in [("first", first), ("second", second)]:
        items.append(
            {
                "key": key,
                "kind": "metacyc-reaction-xml",
                **original(tmp_path, root, key + ".xml", "META", "RXN"),
            }
        )
    with pytest.raises(ValueError, match="conflicting MetaCyc reaction"):
        snapshot(tmp_path, items, "MetaCyc:UNSELECTED")


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize(
    "text",
    [
        "carrier &#0;",
        "carrier &#31;",
        "carrier &#x7f;",
        "carrier &#xD800;",
        "carrier &#xFFFF;",
        "carrier &#x110000;",
        "carrier <![CDATA[bad]]>",
        "carrier <br/>",
        "carrier <!--hidden-->",
        "carrier <?hidden?>",
        "carrier <i>unbalanced",
        "carrier </b>",
    ],
)
def test_native_name_markup_never_normalizes_invalid_characters(tmp_path, shape, text):
    root = document(shape)
    list(root)[1].find("common-name").text = text
    with pytest.raises(ValueError):
        metadata(entry(tmp_path, shape, root=root), tmp_path)


@pytest.mark.parametrize("shape", SHAPES)
def test_safe_native_name_markup_is_decoded_without_state_renaming(tmp_path, shape):
    root = document(shape)
    list(root)[1].find(
        "common-name"
    ).text = "native <i>protein</i> &alpha; &amp; carrier(SH)<sub>2</SUB>"
    item = entry(tmp_path, shape, root=root)
    assert term(item, tmp_path)[1]["label"] == "native protein α & carrier(SH)2"


@pytest.mark.parametrize("shape", SHAPES)
def test_identical_duplicates_keep_first_complete_typed_assertion(tmp_path, shape):
    first = entry(tmp_path, shape, key="first")
    second = entry(tmp_path, shape, key="second")
    data = snapshot(tmp_path, [first, second])
    identifier, expected = term(first, tmp_path)
    assert data["terms"] == {identifier: expected} and set(data["sources"]) == {"first"}


@pytest.mark.parametrize("problem", ["taxon-tail", "gene-tail", "gene-wrapper-attribute"])
def test_additional_state_reference_and_taxon_text_is_not_ignored(tmp_path, problem):
    root = document("state-red")
    if problem == "taxon-tail":
        root.find("metadata/PGDB/dblink").tail = "hidden assertion"
    elif problem == "gene-tail":
        root.find("Protein/gene/Gene").tail = "hidden assertion"
    else:
        root.find("Protein/gene").set("class", "true")
    with pytest.raises(ValueError):
        metadata(entry(tmp_path, "state-red", root=root), tmp_path)


@pytest.mark.parametrize("shape", SHAPES)
def test_linked_whole_originals_are_hash_checked_without_requiring_inline_copies(tmp_path, shape):
    item = entry(tmp_path, shape)
    link = tmp_path / "bound-original.xml"
    link.symlink_to(item["path"])
    item["path"] = link.name
    result = snapshot(tmp_path, [item])
    assert next(iter(result["terms"].values()))["entity_type"] in {
        "protein_class",
        "chemical_class",
        "protein_state",
    }
    item["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="hash"):
        snapshot(tmp_path, [item])


@pytest.mark.parametrize("shape", SHAPES)
@pytest.mark.parametrize("filetype", ["directory", "fifo"])
def test_nonregular_sources_rejected_before_common_hash_read(tmp_path, shape, filetype):
    import os

    item = entry(tmp_path, shape)
    path = tmp_path / "nonregular"
    if filetype == "directory":
        path.mkdir()
    else:
        os.mkfifo(path)
    item["path"] = path.name
    with pytest.raises(ValueError, match="regular file"):
        snapshot(tmp_path, [item], selected="MetaCyc:UNSELECTED")


def test_counterpart_source_on_an_unrelated_kind_is_rejected(tmp_path):
    item = entry(tmp_path, "state-red")
    item["kind"] = "metacyc-protein-xml"
    with pytest.raises(ValueError, match="counterpart_source"):
        snapshot(tmp_path, [item], selected="MetaCyc:UNSELECTED")


@pytest.mark.parametrize("shape", SHAPES)
def test_native_provenance_order_is_stable_across_processes(tmp_path, shape):
    """A fresh hash seed must preserve outer and whole counterpart provenance."""
    import os
    import subprocess
    import sys

    item = entry(tmp_path, shape)
    manifest = tmp_path / "entry.json"
    manifest.write_text(json.dumps(item))
    code = """import json, sys
from pathlib import Path
from pathwaymech.biocyc_carrier import CARRIER_CLASS_KIND, class_metadata, class_term
from pathwaymech.ecocyc_state import state_metadata, state_term
p = Path(sys.argv[1]); entry = json.loads(p.read_text())
reader, projector = ((class_metadata, class_term) if entry['kind'] == CARRIER_CLASS_KIND
                     else (state_metadata, state_term))
metadata = reader(entry, p.parent)
print(json.dumps({'metadata': metadata, 'term': projector(metadata, entry['key'])}, indent=2))
"""
    outputs = []
    for seed in (0, 1, 2, 3, 42):
        result = subprocess.run(
            [sys.executable, "-B", "-c", code, str(manifest)],
            capture_output=True,
            text=True,
            check=False,
            env={**os.environ, "PYTHONHASHSEED": str(seed), "PYTHONDONTWRITEBYTECODE": "1"},
        )
        assert result.returncode == 0, result.stderr
        outputs.append(result.stdout)
    decoded = [json.loads(value) for value in outputs]
    assert all(value == decoded[0] for value in decoded)
    # No sort_keys: sorting would conceal changes to emitted dictionary order.
    assert len(set(outputs)) == 1, "Native provenance serialization differs across hash seeds"
    expected_order = ["license", "url", "version", "sha256"]
    metadata = decoded[0]["metadata"]
    assert list(metadata)[:4] == expected_order
    if shape.startswith("state"):
        assert list(metadata["counterpart"])[:4] == expected_order
