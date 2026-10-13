"""Whole aceto originals, bounded producer and offline-consumer adversaries."""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.biocyc_aceto import ACETO_KINDS, FIELD, aceto_metadata
from pathwaymech.biocyc_native_context import retained
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot

FIXTURES = Path(__file__).parent / "fixtures/aceto_authority"
ROWS = json.loads((FIXTURES / "manifest.json").read_text())
BY_ID = {r["id"]: r for r in ROWS}
PWY = "MetaCyc:ACETOACETATE-DEG-PWY"
PARENT = "EcoCyc:ACETOACETYL-COA-TRANSFER-CPLX"
COMPOSITE = "MetaCyc:ACETYL-COA-ACETYLTRANSFER-RXN"
RESIDUE = "MetaCyc:PROT-CYS"


def stage(tmp_path):
    for p in FIXTURES.glob("*.xml"):
        shutil.copyfile(p, tmp_path / p.name)
    return copy.deepcopy(ROWS)


def build(tmp_path, entries, ids):
    corpus = tmp_path / "records"
    corpus.mkdir(exist_ok=True)
    ids = list(ids)
    (corpus / "selected.yaml").write_text(
        yaml.safe_dump({"id": ids[0], "participants": [{"id": n} for n in ids[1:]]})
    )
    p = tmp_path / "manifest.json"
    p.write_text(json.dumps(entries))
    return build_snapshot(p, corpus, tmp_path)


def consume(tmp_path, data):
    p = tmp_path / "snapshot.json"
    p.write_text(json.dumps(data))
    return _load_authority(p)


def original(entry, tmp_path):
    return ET.fromstring((tmp_path / entry["path"]).read_bytes())


def save(entry, root, tmp_path):
    body = ET.tostring(root, encoding="utf-8")
    (tmp_path / entry["path"]).write_bytes(body)
    entry["sha256"] = hashlib.sha256(body).hexdigest()


@pytest.mark.parametrize("row", ROWS, ids=lambda r: r["id"])
def test_whole_original_roundtrip(tmp_path, row):
    stage(tmp_path)
    entry = copy.deepcopy(row["entry"])
    body = (tmp_path / entry["path"]).read_bytes()
    assert len(body) == row["original"]["bytes"]
    assert hashlib.sha256(body).hexdigest() == row["original"]["sha256"]
    built = build(tmp_path, [entry], [row["id"]])
    assert consume(tmp_path, built) == built["terms"]
    if entry["kind"] in ACETO_KINDS:
        native = built["sources"][entry["key"]][FIELD]["document"]["native"]
        assert (
            native["source_slots"] == retained(original(entry, tmp_path)[1], set())["source_slots"]
        )


def test_full_companion_scope(tmp_path):
    rows = stage(tmp_path)
    built = build(tmp_path, [r["entry"] for r in rows], BY_ID)
    consume(tmp_path, built)
    by = {r["id"]: built["sources"][r["entry"]["key"]] for r in rows}
    assert len(by[PWY][FIELD]["document"]["native"]["pathway_links"]) == 2
    n = by[PARENT][FIELD]
    assert [c["document"]["native"]["components"][0]["coefficient"] for c in n["companions"]] == [
        2,
        2,
    ]
    n = by[COMPOSITE][FIELD]
    assert len(n["document"]["native"]["sides"]) == 3
    assert sum(len(c["document"]["native"]["sides"]) for c in n["companions"]) == 8
    assert "reaction-ordering" not in n["document"]["native"]["direct_slot_order"]
    n = by[RESIDUE][FIELD]
    assert len(n["document"]["native"]["subclasses"]) == 47
    assert len(n["companions"][0]["document"]["native"]["subclasses"]) == 30
    assert (
        sum(
            c["native_type"] == "Protein"
            for c in n["companions"][0]["document"]["native"]["subclasses"]
        )
        == 1
    )


def drop(e, path):
    parent, _, tag = path.rpartition("/")
    n = e.find(parent) if parent else e
    n.remove(n.find(tag))


def duplicate(e, path):
    parent, _, tag = path.rpartition("/")
    n = e.find(parent) if parent else e
    n.append(copy.deepcopy(n.find(tag)))


def change_ref(n, frame):
    old = n.get("frameid")
    n.set("frameid", frame)
    for key in ["resource", "ID"]:
        if key in n.attrib:
            n.set(key, n.get(key).replace(old, frame))


def mutate(case, root):
    e = root[1]
    group, number = case.rsplit("-", 1)
    n = int(number)
    if group == "envelope":
        if n == 1:
            root.find("metadata/query").text = "META:WRONG"
        elif n == 2:
            root.find("metadata/PGDB").set("orgid", "ECOLI")
        elif n == 3:
            e.tag = "Protein"
        elif n == 4:
            e.set("class", "true")
        elif n == 5:
            e.attrib.pop("class")
        elif n in {6, 7}:
            root.set("ptools-version", "28.0")
        elif n == 8:
            root.find("metadata/url").text = "https://wrong.example/"
        elif n == 14:
            root.tag = "html"
        elif n == 16:
            root.append(copy.deepcopy(e))
        elif n == 17:
            duplicate(root[0], "query")
        elif n == 18:
            e.set("ID", "META:WRONG")
    elif group == "pathway":
        if n in {1, 2}:
            drop(e, "common-name")
        elif n == 3:
            e.find("reaction-list").remove(e.find("reaction-list")[0])
        elif n == 4:
            duplicate(e, "reaction-list/Reaction")
        elif n == 5:
            change_ref(e.find("reaction-ordering/Reaction"), "WRONG")
        elif n == 6:
            change_ref(
                e.find("reaction-ordering/predecessor-reactions/Reaction"),
                e.find("reaction-ordering/Reaction").get("frameid"),
            )
        elif n == 7:
            drop(e, "reaction-layout")
        elif n == 8:
            e.find("reaction-layout/direction").text = "FORWARD"
        elif n == 9:
            e.find("reaction-layout/left-primaries")[0].tag = "Protein"
        elif n == 10:
            drop(e, "pathway-link/link-target/Pathway")
        elif n == 11:
            duplicate(e, "pathway-link/link-target")
        elif n == 12:
            e.find("evidence/Evidence-Code").attrib.pop("class")
        elif n == 13:
            ET.SubElement(e.find("evidence/Evidence-Code"), "unsupported")
    elif group == "nested-assembly":
        if n in {1, 2}:
            ET.SubElement(
                e, "common-name" if n == 1 else "synonym", datatype="string"
            ).text = "invented"
        elif n == 3:
            change_ref(e.find("parent/Protein"), "Proteins")
        elif n == 4:
            drop(e, "component")
        elif n == 5:
            e.findall("component")[1][0].attrib.update(e.find("component/Protein").attrib)
        elif n == 6:
            drop(e, "component/coefficient")
        elif n == 7:
            e.find("component/coefficient").text = "2"
        elif n == 8:
            change_ref(e.find("component/Protein"), e.get("frameid"))
        elif n == 14:
            drop(e, "common-name")
        elif n == 15:
            e.find("component/coefficient").text = "1"
        elif n == 16:
            change_ref(e.find("component/Protein"), "ATOD-MONOMER")
        elif n == 17:
            drop(e, "component-of")
        elif n == 18:
            change_ref(e.find("component/Protein"), "ACETOACETYL-COA-TRANSFER-CPLX")
        elif n == 19:
            change_ref(e.find("catalyzes/Enzymatic-Reaction/enzyme/Protein"), "WRONG")
        elif n == 20:
            e.find("molecular-weight-exp/citation/Publication").tag = "Protein"
    elif group == "composite":
        if n in {1, 2}:
            change_ref(
                e.find("parent/Reaction"),
                "Electron-Transfer-Reactions" if n == 1 else "Chemical-Reactions",
            )
        elif n == 3:
            duplicate(e, "parent")
        elif n == 4:
            ET.SubElement(e, "common-name", datatype="string").text = "invented"
        elif n == 5:
            e.find("reaction-direction").text = "LEFT-TO-RIGHT"
        elif n == 6:
            drop(e, "left/coefficient")
        elif n == 7:
            duplicate(e, "left")
        elif n == 8:
            ET.SubElement(e.find("left"), "compartment")
        elif n == 9:
            drop(e, "reaction-list/Reaction")
        elif n == 10:
            duplicate(e, "reaction-list/Reaction")
        elif n == 11:
            ET.SubElement(e, "reaction-ordering")
        elif n == 14:
            change_ref(e.find("parent/Reaction"), "Composite-Reactions")
        elif n == 15:
            e.find("in-pathway/Reaction").tag = "Pathway"
        elif n == 16:
            change_ref(e.find("in-pathway/Reaction"), "WRONG")
        elif n == 17:
            next(x for x in e.findall("left/Compound") if x.get("class") == "true").attrib.pop(
                "class"
            )
        elif n == 18:
            change_ref(e.find("left/Compound"), "WRONG")
        elif n == 19:
            e.find("gibbs-0/evidence/Evidence-Code").attrib.pop("class")
        elif n == 20:
            e.find("gibbs-0/evidence/Publication").tag = "Protein"
    elif group == "residue-class":
        if n == 1:
            drop(e, "common-name")
        elif n in {3, 19}:
            change_ref(e.find("parent/Compound"), "Amino-Acids")
        elif n == 6:
            for x in e.findall("subclass"):
                if x[0].get("frameid") == "PROT-CYS":
                    e.remove(x)
        elif n == 7:
            duplicate(e, "subclass")
        elif n == 8:
            next(x for x in e.findall("subclass/Protein")).tag = "Compound"
        elif n == 9:
            e.find("subclass")[0].attrib.pop("class")
        elif n == 10:
            e.find("subclass")[0].tag = "Pathway"
        elif n == 11:
            e.find("cml/molecule").set("id", "WRONG")
        elif n == 12:
            duplicate(e, "cml/molecule/atomArray/atom")
        elif n == 13:
            e.find("cml/molecule/bondArray/bond").set("atomRefs", "missing absent")
        elif n == 14:
            e.find("cml/molecule/atomArray/atom").set("x2", "nan")
        elif n == 15:
            ET.SubElement(e.find("cml/molecule"), "injected")
        elif n == 16:
            next(
                x
                for x in e.findall("cml/molecule/atomArray/atom")
                if x.get("elementType") == "Proteins"
            ).set("elementType", "C")
        elif n == 17:
            e.find("cml/molecule/formula").set("concise", "C 3 H 7 N 1 O 2 S 1")
    return root


# Each mutant starts from a complete original; consumers reconstruct the same
# changed source subtree. No mutated fixture is an issuing source.
XML_CASES = []
for group, ids, ident in [
    ("envelope", [1, 2, 3, 4, 6, 7, 8, 14, 16, 17, 18], PWY),
    ("pathway", list(range(1, 14)), PWY),
    ("nested-assembly", [1, 2, 3, 4, 5, 6, 7, 8, 19, 20], PARENT),
    ("composite", list(range(1, 12)), COMPOSITE),
    ("residue-class", [1, 3, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19], RESIDUE),
]:
    XML_CASES += [(f"{group}-{n:02}", ident, None) for n in ids]
XML_CASES += [("envelope-05", RESIDUE, None)]
XML_CASES += [(f"nested-assembly-{n:02}", PARENT, 0) for n in [14, 15, 16, 17, 18]]
XML_CASES += [(f"composite-{n:02}", COMPOSITE, 0) for n in [14, 15, 16, 17, 18, 19, 20]]
XML_CASES += [(f"residue-class-{n:02}", RESIDUE, 0) for n in [6, 7, 8]]


@pytest.mark.parametrize("case,ident,companion", XML_CASES, ids=[c[0] for c in XML_CASES])
@pytest.mark.parametrize("surface", ["producer", "consumer"])
def test_whole_xml_negative(tmp_path, case, ident, companion, surface):
    rows = stage(tmp_path)
    entry = next(r["entry"] for r in rows if r["id"] == ident)
    data = build(tmp_path, [entry], [ident])
    descriptor = entry
    doc = data["sources"][entry["key"]][FIELD]["document"]
    if companion is not None:
        field = {
            "EcoCyc:ACETOACETYL-COA-TRANSFER-CPLX": "component_sources",
            COMPOSITE: "constituent_sources",
            RESIDUE: "parent_source",
        }[ident]
        descriptor = entry[field] if field == "parent_source" else entry[field][companion]
        doc = data["sources"][entry["key"]][FIELD]["companions"][companion]["document"]
    root = mutate(case, original(descriptor, tmp_path))
    if surface == "producer":
        save(descriptor, root, tmp_path)
        with pytest.raises((ValueError, ET.ParseError)):
            build(tmp_path, [entry], [ident])
    else:
        doc["envelope"] = {
            "attributes": dict(root.attrib),
            "metadata_xml": ET.tostring(root[0], encoding="unicode"),
        }
        if case == "envelope-16":
            doc["envelope"]["metadata_xml"] += ET.tostring(root[2], encoding="unicode")
        core = set(doc["native"]["direct_slot_order"]) - {
            s["tag"] for s in doc["native"]["context_slots"]
        }
        doc["native"].update(retained(root[1], core))
        if case == "envelope-14":
            doc["envelope"]["metadata_xml"] = "<html><body>login</body></html>"
        # Entity tag is explicit in the typed projection; a forged native type
        # must be rejected even though the rebuilding tag comes from the kind.
        doc["native"]["native_type"] = root[1].tag
        with pytest.raises((ValueError, ET.ParseError)):
            consume(tmp_path, data)


URL_CASES = {
    "envelope-09": lambda s: s.replace("pathway.yeastgenome.org", "pathway.yeastgenome.org:443"),
    "envelope-10": lambda s: s + "&extra=1",
    "envelope-11": lambda s: s + "#fragment",
    "envelope-12": lambda s: s.replace("?META:", "?id=META:"),
    "envelope-13": lambda s: s.replace("https:", "http:"),
}


@pytest.mark.parametrize("case", URL_CASES)
@pytest.mark.parametrize("surface", ["producer", "consumer"])
def test_request_negative(tmp_path, case, surface):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[PWY]["entry"])
    data = build(tmp_path, [entry], [PWY])
    if surface == "producer":
        entry["url"] = URL_CASES[case](entry["url"])
        with pytest.raises(ValueError):
            build(tmp_path, [entry], [PWY])
    else:
        data["sources"][entry["key"]]["url"] = URL_CASES[case](entry["url"])
        with pytest.raises(ValueError):
            consume(tmp_path, data)


@pytest.mark.parametrize("encoding", ["utf-8", "utf-16"])
@pytest.mark.parametrize("surface", ["producer", "consumer"])
def test_envelope_15_dtd(tmp_path, encoding, surface):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[PWY]["entry"])
    data = build(tmp_path, [entry], [PWY])
    if surface == "producer":
        root = original(entry, tmp_path)
        body = (
            '<?xml version="1.0" encoding="'
            + encoding
            + '"?><!DOCTYPE ptools-xml [<!ENTITY own "x">]>'
            + ET.tostring(root, encoding="unicode")
        ).encode(encoding)
        (tmp_path / entry["path"]).write_bytes(body)
        entry["sha256"] = hashlib.sha256(body).hexdigest()
        with pytest.raises((ValueError, ET.ParseError)):
            build(tmp_path, [entry], [PWY])
    else:
        doc = data["sources"][entry["key"]][FIELD]["document"]
        doc["envelope"]["metadata_xml"] = (
            '<!DOCTYPE metadata [<!ENTITY own "x">]>' + doc["envelope"]["metadata_xml"]
        )
        with pytest.raises((ValueError, ET.ParseError)):
            consume(tmp_path, data)


META_CASES = [
    ("envelope-19", PARENT),
    ("envelope-20", PARENT),
    ("pathway-15", PWY),
    ("pathway-16", PWY),
    *[(f"nested-assembly-{n:02}", PARENT) for n in [9, 10, 11, 12, 13]],
    *[(f"composite-{n:02}", COMPOSITE) for n in [12, 13]],
    *[(f"residue-class-{n:02}", RESIDUE) for n in [4, 5]],
]


@pytest.mark.parametrize("case,ident", META_CASES, ids=[n[0] for n in META_CASES])
@pytest.mark.parametrize("surface", ["producer", "consumer"])
def test_companion_metadata_negative(tmp_path, case, ident, surface):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[ident]["entry"])
    data = build(tmp_path, [entry], [ident])
    field = {
        PARENT: "component_sources",
        COMPOSITE: "constituent_sources",
        RESIDUE: "parent_source",
        PWY: None,
    }[ident]
    metadata = data["sources"][entry["key"]]
    if surface == "producer":
        if case == "pathway-15":
            entry["version"] = "27.0"
        elif case == "pathway-16":
            entry["kind"] = "metacyc-pathway-xml"
        elif case in {"nested-assembly-09", "composite-12"}:
            entry[field].pop()
        elif case == "nested-assembly-10":
            entry[field].append(copy.deepcopy(entry[field][0]))
        elif case == "residue-class-04":
            entry[field] = copy.deepcopy(
                BY_ID["MetaCyc:Protein-S-Acetyl-Cysteines"]["entry"]["parent_source"]
            )
        else:
            desc = entry[field] if ident == RESIDUE else entry[field][0]
            if case == "envelope-19":
                desc["path"] = "../" + desc["path"]
            elif case in {"envelope-20", "nested-assembly-13", "composite-13", "residue-class-05"}:
                desc["sha256"] = "0" * 64
            elif case == "nested-assembly-11":
                desc["url"] = desc["url"].replace("ATOA-CPLX", "WRONG")
            elif case == "nested-assembly-12":
                desc["version"] = "26.0"
        with pytest.raises((ValueError, ET.ParseError)):
            build(tmp_path, [entry], [ident])
    else:
        companions = metadata[FIELD]["companions"]
        if case == "pathway-15":
            metadata["version"] = "27.0"
        elif case == "pathway-16":
            metadata["kind"] = "metacyc-pathway-xml"
        elif case in {"nested-assembly-09", "composite-12", "residue-class-04"}:
            companions.pop()
        elif case == "nested-assembly-10":
            companions.append(copy.deepcopy(companions[0]))
        elif case == "envelope-19":
            companions[0]["path"] = "../original.xml"
        elif case in {"envelope-20", "nested-assembly-13", "composite-13", "residue-class-05"}:
            companions[0]["sha256"] = "not-a-digest"
        elif case == "nested-assembly-11":
            companions[0]["url"] = companions[0]["url"].replace("ATOA-CPLX", "WRONG")
        elif case == "nested-assembly-12":
            companions[0]["version"] = "26.0"
        with pytest.raises((ValueError, ET.ParseError)):
            consume(tmp_path, data)


@pytest.mark.parametrize(
    "ident,field",
    [
        (i, f)
        for i in [PWY, PARENT, COMPOSITE, RESIDUE]
        for f in ["component_sources", "constituent_sources", "parent_source"]
        if f not in BY_ID[i]["entry"]
    ],
)
def test_manifest_companions_closed_on_all_kinds(tmp_path, ident, field):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[ident]["entry"])
    entry[field] = []
    with pytest.raises(ValueError):
        build(tmp_path, [entry], [ident])


@pytest.mark.parametrize(
    "case,ident",
    [("nested-assembly-21", PARENT), ("residue-class-02", RESIDUE), ("residue-class-18", RESIDUE)],
)
def test_no_promoted_nested_or_xref_names(tmp_path, case, ident):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[ident]["entry"])
    data = build(tmp_path, [entry], [ident])
    if case == "nested-assembly-21":
        data["terms"][ident]["label"] = "acetoacetyl-CoA transferase"
    elif case == "residue-class-02":
        data["terms"][ident]["synonyms"].append("n-name is not a synonym")
    else:
        data["terms"]["CHEBI:25917"] = data["terms"].pop(ident)
    with pytest.raises(ValueError):
        consume(tmp_path, data)


PLACEMENTS = [
    (PWY, "pathway-14"),
    (PARENT, "nested-assembly-22"),
    (COMPOSITE, "composite-21"),
    (RESIDUE, "residue-class-20"),
]


@pytest.mark.parametrize("ident,case", PLACEMENTS, ids=[n[1] for n in PLACEMENTS])
@pytest.mark.parametrize(
    "section,category",
    [
        ("record", "pathway"),
        ("participants", "protein"),
        ("participants", "complex"),
        ("participants", "chemical_entity"),
        ("participants", "small_molecule"),
        ("reactions", "molecular_activity"),
    ],
)
def test_typed_placement_before_contextual_bypass(tmp_path, ident, case, section, category):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[ident]["entry"])
    data = build(tmp_path, [entry], [ident])
    (tmp_path / "conf").mkdir()
    (tmp_path / "data/pathways").mkdir(parents=True)
    ns = ident.split(":")[0]
    anchor = ns + ":OTHER"
    data["sources"]["anchor"] = {
        "url": "https://example.org",
        "version": "1",
        "license": "test",
        "sha256": "0" * 64,
    }
    data["terms"][anchor] = {"label": "anchor", "synonyms": [], "source": "anchor"}
    (tmp_path / "snapshot.json").write_text(json.dumps(data))
    (tmp_path / "conf/identifier_policy.yaml").write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "namespaces": {ns: {"snapshot": "snapshot.json", "policy": "canonical"}},
                "contextual_labels": [
                    {
                        "namespace": ns,
                        "sections": ["record", "participants", "reactions"],
                        "record_prefixes": [ns],
                        "reason": "test broad contextual policy",
                    }
                ],
            }
        )
    )
    record = {
        "id": ident if section == "record" else anchor,
        "label": data["terms"][ident]["label"] if section == "record" else "anchor",
        "taxa": [],
        "participants": [],
        "reactions": [],
    }
    if section != "record":
        record[section] = [
            {"id": ident, "label": data["terms"][ident]["label"], "category": category}
        ]
    (tmp_path / "data/pathways/record.yaml").write_text(yaml.safe_dump(record))
    errors = identifier_errors(tmp_path)
    legal = (
        (ident == PWY and section == "record")
        or (ident == PARENT and section == "participants" and category == "complex")
        or (ident == COMPOSITE and section == "reactions" and category == "molecular_activity")
        or (ident == RESIDUE and section == "participants" and category == "chemical_entity")
    )
    if not legal:
        assert any("ENTITY_TYPE_MISMATCH" in e for e in errors)
    else:
        assert not errors


@pytest.mark.parametrize("ident", [PWY, PARENT, COMPOSITE, RESIDUE])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_complete_context_conflicts_before_selection(tmp_path, ident, reverse, selected):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[ident]["entry"])
    other = copy.deepcopy(entry)
    other["key"] = "second-owner"
    other["path"] = "second.xml"
    root = original(entry, tmp_path)
    # A coherent, individually accepted change to retained evidence/context.
    if ident == PWY:
        root[1].find("evidence/Evidence-Code/comment").text += " altered evidence"
    elif ident == PARENT:
        root[1].find("comment").text += " altered context"
    elif ident == COMPOSITE:
        root[1].find("gibbs-0").text = "1.0"
    else:
        root[1].find("cml/molecule/atomArray/atom").set("x2", "1.0")
    save(other, root, tmp_path)
    second = aceto_metadata(other, tmp_path)
    entries = [entry, other]
    if reverse:
        entries.reverse()
    anchor = copy.deepcopy(BY_ID[PWY if ident != PWY else RESIDUE]["entry"])
    wanted = [ident] if selected else [PWY if ident != PWY else RESIDUE]
    base = entries[0] if selected else anchor
    data = build(tmp_path, [base], wanted)
    data["sources"].update({e["key"]: aceto_metadata(e, tmp_path) for e in entries})
    assert second
    if not selected:
        entries.append(anchor)
    with pytest.raises(ValueError, match="conflicting"):
        build(tmp_path, entries, wanted)
    with pytest.raises(ValueError, match="conflicting"):
        consume(tmp_path, data)


@pytest.mark.parametrize("ident", [PWY, PARENT, COMPOSITE, RESIDUE])
@pytest.mark.parametrize("reverse", [False, True])
def test_identical_assertions_and_first_owner(tmp_path, ident, reverse):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[ident]["entry"])
    other = copy.deepcopy(entry)
    other["key"] = "other"
    entries = [entry, other]
    if reverse:
        entries.reverse()
    data = build(tmp_path, entries, [ident])
    consume(tmp_path, data)
    assert data["terms"][ident]["source"] == entries[0]["key"]
    assert data["terms"][ident]["synonyms"] == sorted(data["terms"][ident]["synonyms"])


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("change", ["coefficient", "context", "digest", "version"])
def test_companion_separate_named_owner_conflicts(tmp_path, reverse, change):
    from pathwaymech.ecocyc_named_complex import named_complex_metadata

    stage(tmp_path)
    parent = copy.deepcopy(BY_ID[PARENT]["entry"])
    child = copy.deepcopy(BY_ID["EcoCyc:ATOA-CPLX"]["entry"])
    child["path"] = "changed-child.xml"
    child["key"] = "other-child"
    root = original(BY_ID["EcoCyc:ATOA-CPLX"]["entry"], tmp_path)
    if change == "coefficient":
        root[1].find("component/coefficient").text = "3"
    elif change == "context":
        ET.SubElement(root[1], "comment", datatype="string").text = "extra whole context"
    elif change == "version":
        root.set("ptools-version", "26.0")
        root.find("metadata/PGDB").set("version", "26.0")
        child["version"] = "26.0"
    elif change == "digest":
        root[1].tail = "\n\n"
    save(child, root, tmp_path)
    changed = named_complex_metadata(child, tmp_path)
    entries = [parent, child]
    if reverse:
        entries.reverse()
    data = build(tmp_path, [parent], [PARENT])
    data["sources"][child["key"]] = changed
    with pytest.raises(ValueError):
        build(tmp_path, entries, [PARENT])
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize("reverse", [False, True])
def test_constituent_original_provenance_conflict_unselected(tmp_path, reverse):
    stage(tmp_path)
    parent = copy.deepcopy(BY_ID[COMPOSITE]["entry"])
    child = copy.deepcopy(BY_ID["MetaCyc:RXN-20154"]["entry"])
    root = original(child, tmp_path)
    root[1].tail = "\n\n"
    child["path"] = "changed-rxn.xml"
    save(child, root, tmp_path)
    entries = [parent, child]
    if reverse:
        entries.reverse()
    data = build(tmp_path, [parent], [COMPOSITE])
    data["sources"][child["key"]] = {
        k: child[k] for k in ["url", "version", "license", "sha256", "kind"]
    }
    with pytest.raises(ValueError):
        build(tmp_path, entries, [COMPOSITE])
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize("ident", [PWY, PARENT, COMPOSITE, RESIDUE])
def test_untyped_owner_cannot_override_typed_identity(tmp_path, ident):
    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[ident]["entry"])
    data = build(tmp_path, [entry], [ident])
    data["sources"]["untyped"] = {
        k: data["sources"][entry["key"]][k] for k in ["url", "version", "license", "sha256"]
    }
    data["terms"][ident] = {
        "label": data["terms"][ident]["label"],
        "synonyms": [],
        "source": "untyped",
    }
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_mutated_whole_legacy_html_cannot_preempt_sgd_pathway(tmp_path, reverse, selected):
    from scripts.build_source_identifier_snapshot import metacyc_terms

    stage(tmp_path)
    typed = copy.deepcopy(BY_ID[PWY]["entry"])
    original_html = (
        Path(__file__).parent / "fixtures/nitrate_authority/MetaCyc-PWY0-1352-issuing-retry.html"
    )
    body = original_html.read_text().replace("PWY0-1352", "ACETOACETATE-DEG-PWY")
    assert list(metacyc_terms(body))[0][0] == PWY
    (tmp_path / "mutation.html").write_text(body)
    legacy = {
        k: v
        for k, v in typed.items()
        if k not in {"component_sources", "parent_source", "constituent_sources"}
    }
    legacy.update(
        key="legacy",
        kind="metacyc-html",
        path="mutation.html",
        sha256=hashlib.sha256(body.encode()).hexdigest(),
    )
    entries = [typed, legacy]
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="typed aceto identity"):
        build(tmp_path, entries, [PWY] if selected else [RESIDUE])


@pytest.mark.parametrize("reverse", [False, True])
def test_coherent_unselected_cross_kind_pathway_rejected(tmp_path, reverse):
    from pathwaymech.biocyc_pathway import pathway_metadata

    stage(tmp_path)
    entry = copy.deepcopy(BY_ID[PWY]["entry"])
    data = build(tmp_path, [entry], [PWY])
    # Use the complete old whole-pathway fixture, mutating only its requested
    # identity to collide with the SGD source. This is an adversarial source.
    fixture = Path(__file__).parent / "fixtures/nitrate_authority"
    row = next(
        r
        for r in json.loads((fixture / "manifest.json").read_text())
        if r["id"] == "MetaCyc:PWY0-1352"
    )
    raw = (
        (fixture / row["entry"]["path"]).read_bytes().replace(b"PWY0-1352", b"ACETOACETATE-DEG-PWY")
    )
    other = copy.deepcopy(row["entry"])
    other.update(
        key="mirror",
        path="mirror.xml",
        url=other["url"].replace("PWY0-1352", "ACETOACETATE-DEG-PWY"),
        sha256=hashlib.sha256(raw).hexdigest(),
    )
    (tmp_path / "mirror.xml").write_bytes(raw)
    metadata = pathway_metadata(other, tmp_path)
    data["sources"]["mirror"] = metadata
    if reverse:
        data["sources"] = dict(reversed(list(data["sources"].items())))
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize("reverse", [False, True])
def test_forward_cycle_through_separate_named_owner(tmp_path, reverse):
    from pathwaymech.ecocyc_named_complex import named_complex_metadata

    stage(tmp_path)
    parent = copy.deepcopy(BY_ID[PARENT]["entry"])
    row = copy.deepcopy(BY_ID["EcoCyc:ATOA-CPLX"]["entry"])
    root = original(row, tmp_path)
    # A complete child original, transformed into the leaf assembly for this
    # adversary. The reciprocal annotation remains reverse-only context.
    leaf = root[1].find("component/Protein").get("frameid")
    root[1].set("ID", "ECOLI:" + leaf)
    root[1].set("frameid", leaf)
    root.find("metadata/query").text = "ECOLI:" + leaf
    root.set(
        "{http://www.w3.org/XML/1998/namespace}base",
        root.get("{http://www.w3.org/XML/1998/namespace}base").replace("ATOA-CPLX", leaf),
    )
    change_ref(root[1].find("component/Protein"), "ACETOACETYL-COA-TRANSFER-CPLX")
    row.update(key="cycle-leaf", path="cycle-leaf.xml", url=row["url"].replace("ATOA-CPLX", leaf))
    save(row, root, tmp_path)
    metadata = named_complex_metadata(row, tmp_path)
    entries = [parent, row]
    if reverse:
        entries.reverse()
    data = build(tmp_path, [parent], [PARENT])
    data["sources"][row["key"]] = metadata
    with pytest.raises(ValueError, match="cyclic"):
        build(tmp_path, entries, [PARENT])
    with pytest.raises(ValueError, match="cyclic"):
        consume(tmp_path, data)
