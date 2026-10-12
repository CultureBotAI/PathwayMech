"""Whole nitrate issuing originals and adversarial producer/consumer controls.

The fixture bytes are unedited issuing responses. Mutations below are negative
controls, never replacement sources. No full corpus/source build runs here.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.biocyc_carrier import request
from pathwaymech.biocyc_chemical_class import chemical_class_metadata
from pathwaymech.biocyc_electron_transfer import reaction_metadata
from pathwaymech.biocyc_pathway import pathway_metadata
from pathwaymech.ecocyc_named_complex import named_complex_metadata
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, metacyc_terms

FIXTURES = Path(__file__).parent / "fixtures/nitrate_authority"
ROWS = json.loads((FIXTURES / "manifest.json").read_text())
BY_ID = {row["id"]: row for row in ROWS}
PATHWAY = "MetaCyc:PWY0-1352"
NDH = "EcoCyc:NADH-DHI-CPLX"
ARM = "EcoCyc:CPLX0-3361"
CPD7 = "MetaCyc:CPD-7"
BUILDERS = {
    "metacyc-pathway-xml": pathway_metadata,
    "metacyc-electron-transfer-reaction-xml": reaction_metadata,
    "ecocyc-named-protein-complex-xml": named_complex_metadata,
    "metacyc-chemical-class-xml": chemical_class_metadata,
}


def original(identifier):
    return ET.fromstring((FIXTURES / BY_ID[identifier]["entry"]["path"]).read_bytes())


def item(tmp_path, identifier, root=None, key=None):
    entry = copy.deepcopy(BY_ID[identifier]["entry"])
    if key:
        entry["key"] = key
    entry["path"] = entry["key"] + ".xml"
    body = (
        (FIXTURES / BY_ID[identifier]["entry"]["path"]).read_bytes()
        if root is None
        else ET.tostring(root, encoding="utf-8")
    )
    (tmp_path / entry["path"]).write_bytes(body)
    entry["sha256"] = hashlib.sha256(body).hexdigest()
    return entry


def build(tmp_path, entries, ids):
    records = tmp_path / "selected"
    records.mkdir(exist_ok=True)
    identifiers = list(ids)
    (records / "record.yaml").write_text(
        yaml.safe_dump({"id": identifiers[0], "participants": [{"id": n} for n in identifiers[1:]]})
    )
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return build_snapshot(manifest, records, tmp_path)


def consume(tmp_path, data):
    p = tmp_path / "authority.json"
    p.write_text(json.dumps(data))
    return _load_authority(p)


def native(metadata):
    return next(v for k, v in metadata.items() if k.startswith("native_"))


@pytest.mark.parametrize("row", ROWS, ids=lambda row: row["id"])
def test_complete_original_roundtrip(tmp_path, row):
    body = (FIXTURES / row["entry"]["path"]).read_bytes()
    assert len(body) == row["original"]["bytes"]
    assert hashlib.sha256(body).hexdigest() == row["original"]["sha256"]
    entry = item(tmp_path, row["id"])
    metadata = BUILDERS[entry["kind"]](entry, tmp_path)
    projected = native(metadata)
    assert projected["direct_slot_order"] == [n.tag for n in original(row["id"])[1]]
    for saved, source in zip(projected["source_slots"], original(row["id"])[1], strict=True):
        assert saved["xml"] == ET.tostring(source, encoding="unicode")
    data = build(tmp_path, [entry], [row["id"]])
    assert consume(tmp_path, data) == data["terms"]
    assert list(data["terms"]) == [row["id"]]


def test_whole_native_scope_and_nested_assembly_are_preserved(tmp_path):
    entries = [item(tmp_path, row["id"]) for row in ROWS]
    data = build(tmp_path, entries, BY_ID)
    consume(tmp_path, data)
    by_id = {native(m)["id"]: native(m) for m in data["sources"].values()}
    assert len(by_id[PATHWAY]["source_slots"]) == 14
    assert len(by_id[PATHWAY]["reaction_list"]) == 2
    assert sum(len(by_id[n]["sides"]) for n in ("MetaCyc:RXN0-5388", "MetaCyc:RXN0-3501")) == 13
    assert len(by_id[NDH]["components"]) == 8
    assert len(by_id[ARM]["components"]) == 6
    arm_ids = [v["entity"]["id"] for v in by_id[ARM]["components"]]
    leaves = [v["entity"]["id"] for v in by_id[NDH]["components"] if v["entity"]["id"] != ARM]
    assert len(set(leaves + arm_ids)) == 13
    assert "EcoCyc:NUOC-MONOMER" in arm_ids
    assert [v["coefficient"] for v in by_id["EcoCyc:NITRATREDUCTA-CPLX"]["components"]] == [2, 2, 2]
    assert [v["coefficient"] for v in by_id["EcoCyc:NITRATREDUCTZ-CPLX"]["components"]] == [1, 1, 1]
    assert "EC-7.1.1" in next(
        v["xml"] for v in by_id["MetaCyc:RXN0-5388"]["source_slots"] if v["tag"] == "ec-number"
    )
    assert [v["attributes"]["frameid"] for v in by_id[CPD7]["subclasses"]] == [
        "4Fe-4S+1",
        "4Fe-4S+2",
        "4Fe-4S+3",
    ]


PATHWAY_BAD = [
    "type",
    "class",
    "frame",
    "query",
    "version",
    "pgdb",
    "base",
    "metadata-duplicate",
    "mixed",
    "unknown-slot",
    "duplicate-name",
    "missing-name",
    "duplicate-parent",
    "duplicate-member",
    "empty-list",
    "missing-list",
    "unknown-order-member",
    "self-order",
    "cycle",
    "duplicate-order",
    "missing-layout",
    "duplicate-layout",
    "layout-member",
    "layout-direction",
    "layout-compound-type",
    "taxon-type",
    "taxon-class",
    "taxon-pgdb",
    "taxon-rank",
    "taxon-unknown-slot",
    "taxon-duplicate",
    "nested-title",
    "dtd",
    "pi",
    "hash",
]


def mutate_pathway(root, problem):
    e = root[1]
    if problem in {"type", "class", "frame"}:
        if problem == "type":
            e.tag = "Compound"
        elif problem == "class":
            e.set("class", "true")
        else:
            e.set("frameid", "WRONG")
    elif problem == "query":
        root.find("metadata/query").text = "META:WRONG"
    elif problem == "version":
        root.set("ptools-version", "26.0")
    elif problem == "pgdb":
        root.find("metadata/PGDB").set("orgid", "ECOLI")
    elif problem == "base":
        root.set("{http://www.w3.org/XML/1998/namespace}base", "https://example.org")
    elif problem == "metadata-duplicate":
        root.append(copy.deepcopy(root[0]))
    elif problem == "mixed":
        e.text = "unexpected"
    elif problem == "unknown-slot":
        ET.SubElement(e, "unsupported")
    elif problem == "duplicate-name":
        e.append(copy.deepcopy(e.find("common-name")))
    elif problem in {"missing-name", "nested-title"}:
        e.remove(e.find("common-name"))
    elif problem == "duplicate-parent":
        e.append(copy.deepcopy(e.find("parent")))
    elif problem == "duplicate-member":
        e.find("reaction-list").append(copy.deepcopy(e.find("reaction-list")[0]))
    elif problem == "empty-list":
        e.find("reaction-list").clear()
    elif problem == "missing-list":
        e.remove(e.find("reaction-list"))
    elif problem in {"unknown-order-member", "self-order"}:
        n = e.find("reaction-ordering/Reaction")
        if problem == "self-order":
            n.attrib = dict(e.find("reaction-ordering/predecessor-reactions/Reaction").attrib)
        else:
            n.attrib.update(frameid="WRONG", resource="getxml?META:WRONG")
    elif problem in {"cycle", "duplicate-order"}:
        more = copy.deepcopy(e.find("reaction-ordering"))
        if problem == "cycle":
            a, b = more.find("Reaction"), more.find("predecessor-reactions/Reaction")
            a.attrib, b.attrib = b.attrib, a.attrib
        e.append(more)
    elif problem == "missing-layout":
        e.remove(e.find("reaction-layout"))
    elif problem == "duplicate-layout":
        e.append(copy.deepcopy(e.find("reaction-layout")))
    elif problem == "layout-member":
        e.find("reaction-layout/Reaction").attrib.update(
            frameid="WRONG", resource="getxml?META:WRONG"
        )
    elif problem == "layout-direction":
        e.find("reaction-layout/direction").text = "FORWARD"
    elif problem == "layout-compound-type":
        e.find("reaction-layout/left-primaries/Compound").tag = "Protein"
    elif problem.startswith("taxon"):
        n = e.find("taxonomic-range/Organism")
        if problem == "taxon-type":
            n.tag = "Protein"
        elif problem == "taxon-class":
            n.attrib.pop("class")
        elif problem == "taxon-pgdb":
            n.set("orgid", "ECOLI")
        elif problem == "taxon-rank":
            n.find("rank").text = "made-up"
        elif problem == "taxon-unknown-slot":
            ET.SubElement(n, "unsupported")
        else:
            e.find("taxonomic-range").append(copy.deepcopy(n))


@pytest.mark.parametrize("problem", PATHWAY_BAD)
def test_whole_pathway_rejects_identity_graph_and_taxon_corruption(tmp_path, problem):
    root = original(PATHWAY)
    mutate_pathway(root, problem)
    entry = item(tmp_path, PATHWAY, root)
    if problem in {"dtd", "pi"}:
        p = tmp_path / entry["path"]
        p.write_bytes(
            (b"<!DOCTYPE ptools-xml>" if problem == "dtd" else b"<?unsafe processing?>")
            + p.read_bytes()
        )
        entry["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
    elif problem == "hash":
        entry["sha256"] = "0" * 64
    with pytest.raises(ValueError):
        pathway_metadata(entry, tmp_path)


@pytest.mark.parametrize(
    "problem",
    [
        "native-type",
        "native-id",
        "projected-label",
        "projected-layout",
        "retained-unknown",
        "retained-cycle",
        "missing-kind",
        "wrong-term",
        "generic-owner",
        "conflicting-context",
    ],
)
def test_pathway_consumer_reconstructs_complete_projection(tmp_path, problem):
    data = build(tmp_path, [item(tmp_path, PATHWAY)], [PATHWAY])
    metadata = next(iter(data["sources"].values()))
    n = native(metadata)
    if problem == "native-type":
        n["native_type"] = "Compound"
    elif problem == "native-id":
        n["id"] = "MetaCyc:OTHER"
    elif problem == "projected-label":
        n["direct_common_name"] = "invented"
    elif problem == "projected-layout":
        n["reaction_layout"][0]["direction"] = "R2L"
    elif problem == "retained-unknown":
        n["source_slots"].append({"tag": "unknown", "xml": "<unknown />"})
    elif problem == "retained-cycle":
        root = original(PATHWAY)
        mutate_pathway(root, "cycle")
        n["source_slots"] = [
            {"tag": v.tag, "xml": ET.tostring(v, encoding="unicode")} for v in root[1]
        ]
    elif problem == "missing-kind":
        metadata.pop("kind")
    elif problem == "wrong-term":
        data["terms"][PATHWAY]["entity_type"] = "reaction"
    elif problem == "generic-owner":
        data["sources"]["generic"] = {
            k: metadata[k] for k in ("url", "version", "license", "sha256")
        }
        data["terms"][PATHWAY] = {
            "label": n["direct_common_name"],
            "synonyms": [],
            "source": "generic",
        }
    else:
        more = original(PATHWAY)
        more[1].find("comment").text = "Different source context"
        data["sources"]["conflict"] = pathway_metadata(
            item(tmp_path, PATHWAY, more, "conflict"), tmp_path
        )
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize(
    "section", ["record", "participants", "reactions", "taxa", "invented-label"]
)
def test_pathway_is_only_a_canonical_record_node(tmp_path, section):
    data = build(tmp_path, [item(tmp_path, PATHWAY)], [PATHWAY])
    consume(tmp_path, data)
    data["sources"]["anchor"] = {
        "url": "https://example.org",
        "version": "1",
        "license": "test",
        "sha256": "0" * 64,
    }
    data["terms"]["MetaCyc:OTHER"] = {"label": "other", "synonyms": [], "source": "anchor"}
    (tmp_path / "authority.json").write_text(json.dumps(data))
    r = {"id": PATHWAY, "label": data["terms"][PATHWAY]["label"], "pathway_type": "metabolic"}
    if section in {"participants", "reactions", "taxa"}:
        r = {"id": "MetaCyc:OTHER", "label": "other", section: [dict(r, category="protein")]}
    elif section == "invented-label":
        r["label"] = "invented"
    for field in ("taxa", "participants", "reactions"):
        r.setdefault(field, [])
    folder = tmp_path / "data/pathways"
    folder.mkdir(parents=True)
    (folder / "record.yaml").write_text(yaml.safe_dump(r))
    conf = tmp_path / "conf"
    conf.mkdir()
    (conf / "identifier_policy.yaml").write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "namespaces": {
                    "MetaCyc": {"snapshot": "authority.json", "policy": "canonical_or_synonym"}
                },
                "contextual_labels": [
                    {
                        "namespace": "MetaCyc",
                        "sections": ["record", "participants", "reactions", "taxa"],
                        "record_prefixes": ["MetaCyc"],
                        "reason": "Broad negative control",
                    }
                ],
            }
        )
    )
    errors = identifier_errors(tmp_path)
    if section == "record":
        assert errors == []
    else:
        assert len(errors) == 1
        assert (
            "LABEL_MISMATCH" if section == "invented-label" else "ENTITY_TYPE_MISMATCH"
        ) in errors[0]


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_compound_template_html_cannot_preempt_typed_pathway(tmp_path, reverse, selected):
    typed = item(tmp_path, PATHWAY)
    html = FIXTURES / "MetaCyc-PWY0-1352-issuing-retry.html"
    # Reproduce issue 499 honestly: legacy accepts the matching title despite
    # the source's Compound template. The new typed authority cannot mix with it.
    assert list(metacyc_terms(html.read_text()))[0][0] == PATHWAY
    (tmp_path / "wrong.html").write_bytes(html.read_bytes())
    legacy = dict(
        typed,
        key="legacy",
        kind="metacyc-html",
        path="wrong.html",
        sha256=hashlib.sha256(html.read_bytes()).hexdigest(),
        version="22.5",
        url="https://pathway.yeastgenome.org/compound?orgid=META&id=PWY0-1352",
    )
    entries = [typed, legacy]
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="identity scope"):
        build(tmp_path, entries, [PATHWAY] if selected else ["MetaCyc:UNSELECTED"])


@pytest.mark.parametrize(
    "ec,accepted",
    [
        ("EC-7.1.1", True),
        ("EC-7.1.1.1", True),
        ("EC-7.1.1.-", True),
        ("EC-7.1", False),
        ("EC-7.1.-", False),
        ("EC-7..1", False),
        ("EC-7.1.1.1.1", False),
        ("EC-7.1.x", False),
        ("EC-7.1.1.", False),
        (" EC-7.1.1", False),
        ("EC-7.1.1a", False),
        ("7.1.1", False),
    ],
)
def test_partial_ec_preserves_existing_four_level_contract(tmp_path, ec, accepted):
    root = original("MetaCyc:RXN0-5388")
    root[1].find("ec-number").text = ec
    entry = item(tmp_path, "MetaCyc:RXN0-5388", root)
    if accepted:
        metadata = reaction_metadata(entry, tmp_path)
        assert ec in next(
            v["xml"] for v in native(metadata)["source_slots"] if v["tag"] == "ec-number"
        )
    else:
        with pytest.raises(ValueError, match="EC context"):
            reaction_metadata(entry, tmp_path)


@pytest.mark.parametrize(
    "problem",
    ["attribute", "official-value", "official-attribute", "duplicate-official", "unknown-child"],
)
def test_partial_ec_children_are_closed(tmp_path, problem):
    root = original("MetaCyc:RXN0-5388")
    ec = root[1].find("ec-number")
    child = ET.SubElement(ec, "official")
    child.text = "true"
    if problem == "attribute":
        ec.set("extra", "true")
    elif problem == "official-value":
        child.text = "maybe"
    elif problem == "official-attribute":
        child.set("extra", "true")
    elif problem == "duplicate-official":
        ec.append(copy.deepcopy(child))
    else:
        child.tag = "unknown"
    with pytest.raises(ValueError, match="EC context"):
        reaction_metadata(item(tmp_path, "MetaCyc:RXN0-5388", root), tmp_path)


PLUS_FRAMES = ["4Fe-4S+1", "4Fe-4S+2", "4Fe-4S+3", "PYRUVATE-DEHYDROGENASE-NADP+-RXN"]
PLUS_BAD = [
    "resource-encoded",
    "resource-double",
    "frame-encoded",
    "decoded-space",
    "pgdb",
    "type",
    "class",
    "suffix",
    "extra-query",
    "extra-attribute",
]


@pytest.mark.parametrize("frame", PLUS_FRAMES)
@pytest.mark.parametrize("problem", PLUS_BAD)
@pytest.mark.parametrize("consumer", [False, True])
def test_literal_plus_context_identity_has_no_decoding_or_type_fallback(
    tmp_path, frame, problem, consumer
):
    root = original(CPD7)
    tag = "Reaction" if "RXN" in frame else "Compound"
    node = next(n for n in root[1].iter(tag) if n.get("frameid") == frame)
    if problem == "resource-encoded":
        node.set("resource", node.get("resource").replace("+", "%2B"))
    elif problem == "resource-double":
        node.set("resource", node.get("resource").replace("+", "%252B"))
    elif problem == "frame-encoded":
        node.set("frameid", frame.replace("+", "%2B"))
    elif problem == "decoded-space":
        node.set("frameid", frame.replace("+", " "))
        node.set("resource", node.get("resource").replace("+", " "))
    elif problem == "pgdb":
        node.set("orgid", "ECOLI")
    elif problem == "type":
        node.tag = "Protein"
    elif problem == "class":
        if tag == "Compound":
            node.attrib.pop("class")
        else:
            node.set("class", "true")
    elif problem == "suffix":
        node.set("frameid", frame[:-1])
        node.set("resource", "getxml?META:" + frame[:-1])
    elif problem == "extra-query":
        node.set("resource", node.get("resource") + "&x=1")
    else:
        node.set("extra", "yes")
    if consumer:
        data = build(tmp_path, [item(tmp_path, CPD7)], [CPD7])
        n = native(next(iter(data["sources"].values())))
        n["source_slots"] = [
            {"tag": v.tag, "xml": ET.tostring(v, encoding="unicode")} for v in root[1]
        ]
        with pytest.raises(ValueError):
            consume(tmp_path, data)
    else:
        with pytest.raises(ValueError):
            chemical_class_metadata(item(tmp_path, CPD7, root), tmp_path)


@pytest.mark.parametrize("frame", PLUS_FRAMES)
def test_literal_plus_does_not_relax_selected_request_contract(frame):
    with pytest.raises(ValueError):
        request("https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:" + frame, "META")


@pytest.mark.parametrize(
    "identifier", [NDH, "EcoCyc:NITRATREDUCTA-CPLX", "EcoCyc:NITRATREDUCTZ-CPLX"]
)
@pytest.mark.parametrize(
    "problem",
    [
        "go-frame",
        "go-resource",
        "go-class",
        "go-type",
        "code-class",
        "code-identity",
        "evidence-extra",
        "publication-type",
        "publication-identity",
        "with-duplicate",
    ],
)
def test_named_assembly_go_evidence_is_closed(tmp_path, identifier, problem):
    root = original(identifier)
    go = root[1].find("has-go-term")
    term = go.find("GO-Term")
    evidence = go.find("evidence")
    code = evidence.find("Evidence-Code")
    if problem == "go-frame":
        term.set("frameid", "GO:123")
    elif problem == "go-resource":
        term.set("resource", "getxml?META:" + term.get("frameid"))
    elif problem == "go-class":
        term.attrib.pop("class")
    elif problem == "go-type":
        term.tag = "Protein"
    elif problem == "code-class":
        code.attrib.pop("class")
    elif problem == "code-identity":
        code.set("orgid", "META")
    elif problem == "evidence-extra":
        ET.SubElement(evidence, "unknown")
    elif problem.startswith("publication"):
        pub = next(n for n in evidence if n.tag == "Publication")
        if problem == "publication-type":
            pub.tag = "Protein"
        else:
            pub.set("orgid", "META")
    else:
        evidence.append(copy.deepcopy(evidence.find("with")))
    with pytest.raises(ValueError):
        named_complex_metadata(item(tmp_path, identifier, root), tmp_path)


@pytest.mark.parametrize(
    "problem",
    [
        "mass-unit",
        "mass-citation",
        "mass-publication",
        "location-type",
        "location-pgdb",
        "component-self",
        "component-duplicate",
        "coefficient-zero",
        "reverse-self",
        "reverse-type",
    ],
)
def test_complex_composition_mass_and_location_guards(tmp_path, problem):
    identifier = (
        NDH
        if problem.startswith("mass")
        else ARM
        if problem.startswith("reverse")
        else "EcoCyc:NITRATREDUCTA-CPLX"
    )
    root = original(identifier)
    e = root[1]
    if problem == "mass-unit":
        e.find("molecular-weight-exp").set("units", "grams")
    elif problem == "mass-citation":
        e.find("molecular-weight-exp/citation").set("extra", "yes")
    elif problem == "mass-publication":
        e.find("molecular-weight-exp/citation/Publication").set("class", "true")
    elif problem == "location-type":
        e.find("location/cco").tag = "Protein"
    elif problem == "location-pgdb":
        e.find("location/cco").set("orgid", "META")
    elif problem == "component-self":
        e.find("component/Protein").attrib.update(
            frameid=e.get("frameid"), resource="getxml?ECOLI:" + e.get("frameid")
        )
    elif problem == "component-duplicate":
        e.append(copy.deepcopy(e.find("component")))
    elif problem == "coefficient-zero":
        e.find("component/coefficient").text = "0"
    elif problem == "reverse-self":
        e.find("component-of/Protein").attrib.update(
            frameid=e.get("frameid"), resource="getxml?ECOLI:" + e.get("frameid")
        )
    else:
        e.find("component-of/Protein").tag = "Compound"
    with pytest.raises(ValueError):
        named_complex_metadata(item(tmp_path, identifier, root), tmp_path)


@pytest.mark.parametrize("consumer", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_forward_complex_cycles_fail_without_following_reverse_context(
    tmp_path, consumer, selected
):
    # Valid originals contain an arm -> parent component-of reference and still pass.
    entries = [item(tmp_path, n) for n in [NDH, ARM]]
    data = build(tmp_path, entries, [NDH, ARM])
    consume(tmp_path, data)
    root = original(ARM)
    root[1].find("component/Protein").attrib.update(
        frameid="NADH-DHI-CPLX", resource="getxml?ECOLI:NADH-DHI-CPLX"
    )
    changed = item(tmp_path, ARM, root)
    if consumer:
        data["sources"][changed["key"]] = named_complex_metadata(changed, tmp_path)
        with pytest.raises(ValueError, match="cyclic forward"):
            consume(tmp_path, data)
    else:
        with pytest.raises(ValueError, match="cyclic forward"):
            build(
                tmp_path, [entries[0], changed], [NDH, ARM] if selected else ["MetaCyc:UNSELECTED"]
            )


@pytest.mark.parametrize(
    "identifier",
    ["MetaCyc:Menaquinones", "MetaCyc:Menaquinols", "MetaCyc:3FE-4S", CPD7, "MetaCyc:FeS-Centers"],
)
@pytest.mark.parametrize(
    "problem",
    [
        "unknown-parent",
        "parent-instance",
        "top-instance",
        "duplicate-subclass",
        "projected-profile",
        "projected-category",
    ],
)
def test_new_chemical_profiles_fail_closed_and_reconstruct(tmp_path, identifier, problem):
    root = original(identifier)
    if problem.startswith("projected"):
        data = build(tmp_path, [item(tmp_path, identifier)], [identifier])
        n = native(next(iter(data["sources"].values())))
        n["profile" if problem == "projected-profile" else "allowed_categories"] = (
            "invented" if problem == "projected-profile" else ["protein"]
        )
        with pytest.raises(ValueError):
            consume(tmp_path, data)
        return
    e = root[1]
    if problem == "unknown-parent":
        e.find("parent/Compound").attrib.update(frameid="Unknown", resource="getxml?META:Unknown")
    elif problem == "parent-instance":
        e.find("parent/Compound").attrib.pop("class")
    elif problem == "top-instance":
        e.attrib.pop("class")
    else:
        n = e.find("subclass")
        if n is None:
            n = copy.deepcopy(e.find("parent"))
            n.tag = "subclass"
            e.append(n)
        e.append(copy.deepcopy(n))
    with pytest.raises(ValueError):
        chemical_class_metadata(item(tmp_path, identifier, root), tmp_path)


@pytest.mark.parametrize("identifier", ["MetaCyc:3FE-4S", CPD7, "MetaCyc:FeS-Centers"])
def test_cofactor_profiles_still_require_whole_activity_evidence(tmp_path, identifier):
    root = original(identifier)
    root[1].remove(root[1].find("cofactors-of"))
    with pytest.raises(ValueError, match="activity proof"):
        chemical_class_metadata(item(tmp_path, identifier, root), tmp_path)


@pytest.mark.parametrize(
    "identifier", [NDH, "EcoCyc:NITRATREDUCTA-CPLX", "EcoCyc:NITRATREDUCTZ-CPLX"]
)
def test_consumer_cannot_flatten_assembly_or_change_nar_coefficients(tmp_path, identifier):
    data = build(tmp_path, [item(tmp_path, identifier)], [identifier])
    n = native(next(iter(data["sources"].values())))
    if identifier == NDH:
        n["components"] = [v for v in n["components"] if v["entity"]["id"] != ARM]
    else:
        n["components"][0]["coefficient"] = 1 if identifier.endswith("A-CPLX") else 2
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize(
    "problem",
    [
        None,
        "cid",
        "missing-property",
        "extra-property",
        "property-request",
        "empty-title",
        "invalid-key",
    ],
)
def test_existing_pubchem_contract_preserves_exact_anionic_response(tmp_path, problem):
    from scripts.build_source_identifier_snapshot import _pubchem_record

    original_body = (FIXTURES / "PubChem-21226146-label-authority-retry.json").read_bytes()
    assert (
        hashlib.sha256(original_body).hexdigest()
        == "3b77a855182ca329f7c1c23186630aebb915269ee55a00b9f7fc2a9fb958bb3d"
    )
    body = json.loads(original_body)
    compound = body["PropertyTable"]["Properties"][0]
    assert compound["MolecularFormula"] == "C7H4ClHgO2-"
    url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/21226146/property/Title,IUPACName,MolecularFormula,InChIKey/JSON"
    if problem == "cid":
        compound["CID"] = 1
    elif problem == "missing-property":
        compound.pop("IUPACName")
    elif problem == "extra-property":
        compound["Charge"] = -1
    elif problem == "property-request":
        url = url.replace("IUPACName,", "Charge,")
    elif problem == "empty-title":
        compound["Title"] = ""
    elif problem == "invalid-key":
        compound["InChIKey"] = "made-up"
    path = tmp_path / "pubchem.json"
    path.write_bytes(original_body if problem is None else json.dumps(body).encode())
    if problem is None:
        assert _pubchem_record(path, url) == (
            "PubChem:21226146",
            "(4-Carboxyphenyl)-chloro-mercury",
            [],
        )
    else:
        with pytest.raises(ValueError):
            _pubchem_record(path, url)
