"""Original-shaped adversarial fixtures for the four explicitly separate modes."""

from __future__ import annotations

import copy
import gzip
import hashlib
import json
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.biocyc_carrier import CARRIER_CLASS_KIND
from pathwaymech.biocyc_chemical_class import (
    CHEMICAL_CLASS_KIND,
    chemical_class_metadata,
    chemical_class_term,
)
from pathwaymech.biocyc_electron_transfer import (
    ELECTRON_TRANSFER_KIND,
    reaction_metadata,
    reaction_term,
)
from pathwaymech.ecocyc_complex import ECOCYC_COMPLEX_KIND
from pathwaymech.ecocyc_named_complex import (
    NAMED_COMPLEX_KIND,
    named_complex_metadata,
    named_complex_term,
)
from pathwaymech.identifiers import _load_authority, identifier_errors
from pathwaymech.rhea_polymer import (
    RDF,
    RDFS,
    RH,
    RHEA_POLYMER_KIND,
    RHEA_URL,
    URI,
    comparison_projection,
    polymer_metadata,
)
from scripts.build_source_identifier_snapshot import build_snapshot

HOST = "bf2i-artsymbiocyc.insa-lyon.fr"
MODES = ["reaction", "complex", "quinone", "quinol", "heme", "organometallic", "lipid"]
BUILDERS = {
    ELECTRON_TRANSFER_KIND: reaction_metadata,
    NAMED_COMPLEX_KIND: named_complex_metadata,
    CHEMICAL_CLASS_KIND: chemical_class_metadata,
    RHEA_POLYMER_KIND: polymer_metadata,
}
PROJECTORS = {
    ELECTRON_TRANSFER_KIND: reaction_term,
    NAMED_COMPLEX_KIND: named_complex_term,
    CHEMICAL_CLASS_KIND: chemical_class_term,
}


def envelope(frame, pgdb, tag, is_class):
    root = ET.Element(
        "ptools-xml",
        {
            "ptools-version": "27.0",
            "{http://www.w3.org/XML/1998/namespace}base": f"https://{HOST}/getxml?id={pgdb}:{frame}",
        },
    )
    meta = ET.SubElement(root, "metadata")
    for name, text in [
        ("url", f"https://{HOST}/"),
        ("service_name", "getxml"),
        ("query", pgdb + ":" + frame),
        ("num_results", "1"),
    ]:
        ET.SubElement(meta, name).text = text
    db = ET.SubElement(meta, "PGDB", {"orgid": pgdb, "version": "27.0"})
    ET.SubElement(db, "species", datatype="string").text = (
        "MetaCyc" if pgdb == "META" else "Escherichia coli"
    )
    if pgdb == "ECOLI":
        ET.SubElement(db, "strain", datatype="string").text = "K-12 substr. MG1655"
        x = ET.SubElement(db, "dblink")
        for name, text in [
            ("dblink-db", "NCBI-TAXONOMY-DB"),
            ("dblink-oid", "511145"),
            ("dblink-relationship", "unification"),
            (
                "dblink-URL",
                "http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=511145",
            ),
        ]:
            ET.SubElement(x, name).text = text
    attrs = {"ID": pgdb + ":" + frame, "orgid": pgdb, "frameid": frame, "detail": "full"}
    if is_class:
        attrs["class"] = "true"
    ET.SubElement(root, tag, attrs)
    return root


def native_ref(wrapper, pgdb, tag, frame, is_class=False):
    attrs = {"resource": f"getxml?{pgdb}:{frame}", "orgid": pgdb, "frameid": frame}
    if is_class:
        attrs["class"] = "true"
    return ET.SubElement(wrapper, tag, attrs)


def ref(entity, slot, pgdb, tag, frame, is_class=False):
    w = ET.SubElement(entity, slot)
    native_ref(w, pgdb, tag, frame, is_class)
    return w


def document(mode, frame="SYNTHETIC.17"):
    pgdb = "ECOLI" if mode == "complex" else "META"
    tag = "Reaction" if mode == "reaction" else "Protein" if mode == "complex" else "Compound"
    root = envelope(frame, pgdb, tag, tag == "Compound")
    e = root[-1]
    parents = {
        "reaction": ["Small-Molecule-Reactions", "Electron-Transfer-Reactions"],
        "complex": ["Protein-Complexes"],
        "quinone": ["ETR-Quinones"],
        "quinol": ["Methoxybenzenes", "ETR-Quinols"],
        "heme": ["Organometallics", "Hemes", "Cofactors"],
        "organometallic": ["Organometallics"],
        "lipid": ["Glycerolipids"],
    }[mode]
    for p in parents:
        ref(e, "parent", pgdb, tag, p, True)
    if mode == "reaction":
        ET.SubElement(e, "reaction-direction").text = "LEFT-TO-RIGHT"
        for side, compartment in [("left", "CCO-IN"), ("right", "CCO-OUT")]:
            w = ref(e, side, pgdb, "Compound", "PROTON")
            ET.SubElement(w, "coefficient", datatype="integer").text = "4"
            ref(w, "compartment", pgdb, "cco", compartment)
        w = ET.SubElement(e, "reaction-list")
        for frame in ["HALF-A", "HALF-B"]:
            native_ref(w, pgdb, "Reaction", frame)
        w = ET.SubElement(e, "reaction-ordering")
        native_ref(w, pgdb, "Reaction", "HALF-B")
        ref(w, "predecessor-reactions", pgdb, "Reaction", "HALF-A")
    else:
        ET.SubElement(e, "common-name", datatype="string").text = "a native <i>reference</i>"
        ET.SubElement(e, "synonym", datatype="string").text = "Source alias"
        if mode == "complex":
            w = ref(e, "component", pgdb, "Protein", "MONOMER-X")
            ET.SubElement(w, "coefficient", datatype="integer").text = "4"
        else:
            ref(e, "instance", pgdb, "Compound", "MEMBER")
            if mode in ["heme", "organometallic"]:
                a = ET.SubElement(
                    ET.SubElement(e, "cofactors-of"),
                    "Enzymatic-Reaction",
                    {
                        "ID": "META:ACTIVITY",
                        "orgid": "META",
                        "frameid": "ACTIVITY",
                        "detail": "low",
                    },
                )
                ref(a, "enzyme", pgdb, "Protein", "ENZYME")
                ref(a, "reaction", pgdb, "Reaction", "ACTIVITY-RXN")
    return root


def entry(tmp_path, mode="reaction", root=None, key="new"):
    root = document(mode) if root is None else root
    e = root[-1]
    path = tmp_path / (key + ".xml")
    path.write_bytes(ET.tostring(root))
    kind = (
        ELECTRON_TRANSFER_KIND
        if mode == "reaction"
        else NAMED_COMPLEX_KIND
        if mode == "complex"
        else CHEMICAL_CLASS_KIND
    )
    return {
        "key": key,
        "kind": kind,
        "path": path.name,
        "url": f"https://{HOST}/getxml?id={e.get('orgid')}:{e.get('frameid')}",
        "version": "27.0",
        "license": "Synthetic fixture",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def metadata(item, tmp_path):
    return BUILDERS[item["kind"]](item, tmp_path)


def snap(tmp_path, entries, selected):
    folder = tmp_path / "records"
    folder.mkdir(exist_ok=True)
    (folder / "record.yaml").write_text(yaml.safe_dump({"id": selected}))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return build_snapshot(manifest, folder, tmp_path)


def term(item, tmp_path):
    m = metadata(item, tmp_path)
    return PROJECTORS[item["kind"]](m, item["key"])


@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("frame", ["SYNTHETIC.17", "OTHER-UNSELECTED-29"])
def test_roundtrip_has_no_selected_id_allowlist(tmp_path, mode, frame):
    item = entry(tmp_path, mode, document(mode, frame))
    identifier, expected = term(item, tmp_path)
    data = snap(tmp_path, [item], identifier)
    assert data["terms"][identifier] == expected
    path = tmp_path / "authority.json"
    path.write_text(json.dumps(data))
    assert _load_authority(path) == data["terms"]
    native = next(v for k, v in data["sources"]["new"].items() if k.startswith("native_"))
    assert native["direct_slot_order"] == [r["tag"] for r in native["source_slots"]]


@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize(
    "problem",
    [
        "query",
        "version",
        "database",
        "count",
        "species",
        "base",
        "top-id",
        "top-class",
        "top-detail",
        "top-type",
        "mixed",
        "unknown-slot",
        "duplicate-parent",
        "extra-parent",
        "nested-name",
        "name-script",
        "name-control",
        "duplicate-alias",
    ],
)
def test_native_envelope_and_names_fail_closed(tmp_path, mode, problem):
    root = document(mode)
    e = root[-1]
    if problem == "query":
        root.find("metadata/query").text = "META:FORGED"
    elif problem == "version":
        root.set("ptools-version", "28.0")
    elif problem == "database":
        root.find("metadata/PGDB").set("orgid", "OTHER")
    elif problem == "count":
        root.find("metadata/num_results").text = "2"
    elif problem == "species":
        root.find("metadata/PGDB/species").text = "Other organism"
    elif problem == "base":
        root.set("{http://www.w3.org/XML/1998/namespace}base", "https://evil.example/")
    elif problem == "top-id":
        e.set("ID", "META:OTHER")
    elif problem == "top-class":
        e.set("class", "false" if "class" in e.attrib else "true")
    elif problem == "top-detail":
        e.set("detail", "low")
    elif problem == "top-type":
        e.tag = "RNA"
    elif problem == "mixed":
        e.text = "forged"
    elif problem == "unknown-slot":
        ET.SubElement(e, "gene")
    elif problem == "duplicate-parent":
        e.append(copy.deepcopy(e.find("parent")))
    elif problem == "extra-parent":
        ref(e, "parent", e.get("orgid"), e.tag, "Wrong-Parent", True)
    elif problem == "nested-name":
        n = e.find("common-name")
        if n is not None:
            e.remove(n)
        ET.SubElement(ET.SubElement(e, "comment"), "common-name", datatype="string").text = "forged"
    elif problem == "name-script":
        n = e.find("common-name")
        if n is None:
            n = ET.SubElement(e, "common-name", datatype="string")
        n.text = "<script>forged</script>"
    elif problem == "name-control":
        n = e.find("common-name")
        if n is None:
            n = ET.SubElement(e, "common-name", datatype="string")
        n.text = "name&#0;"
    elif problem == "duplicate-alias":
        ET.SubElement(e, "synonym", datatype="string").text = "A NATIVE reference"
    item = entry(tmp_path, mode, root)
    with pytest.raises((ValueError, ET.ParseError)):
        metadata(item, tmp_path)


@pytest.mark.parametrize("mode", ["reaction", "complex", "heme"])
@pytest.mark.parametrize(
    "problem",
    [
        "url-http",
        "url-suffix",
        "request-other",
        "version",
        "hash",
        "path-absolute",
        "path-traversal",
        "path-directory",
        "extra-field",
        "blank-key",
        "doctype",
        "pi",
    ],
)
def test_source_provenance_and_regular_original_guards(tmp_path, mode, problem):
    item = entry(tmp_path, mode)
    if problem == "url-http":
        item["url"] = item["url"].replace("https:", "http:")
    elif problem == "url-suffix":
        item["url"] += "&extra=1"
    elif problem == "request-other":
        item["url"] = item["url"].replace("SYNTHETIC.17", "OTHER")
    elif problem == "version":
        item["version"] = "28.0"
    elif problem == "hash":
        item["sha256"] = "0" * 64
    elif problem == "path-absolute":
        item["path"] = str(tmp_path / item["path"])
    elif problem == "path-traversal":
        item["path"] = "../" + item["path"]
    elif problem == "path-directory":
        item["path"] = "."
    elif problem == "extra-field":
        item["category"] = "cofactor"
    elif problem == "blank-key":
        item["key"] = " "
    else:
        path = tmp_path / item["path"]
        prefix = "<!DOCTYPE ptools-xml>" if problem == "doctype" else "<?forged data?>"
        path.write_text(prefix + path.read_text())
        item["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    with pytest.raises((ValueError, OSError, ET.ParseError)):
        metadata(item, tmp_path)


@pytest.mark.parametrize(
    "problem",
    [
        "zero",
        "negative",
        "fraction",
        "boolean",
        "duplicate-coefficient",
        "duplicate-compartment",
        "protein",
        "literal-electron",
        "duplicate-side",
        "bad-compartment",
        "class-false",
        "bad-reference",
        "empty-left",
        "ordering-unknown",
        "ordering-self",
        "ordering-cycle",
        "ordering-duplicate",
        "missing-list",
        "single-list",
    ],
)
def test_composite_side_and_decomposition_mutations(tmp_path, problem):
    root = document("reaction")
    e = root[-1]
    side = e.find("left")
    if problem in ["zero", "negative", "fraction", "boolean"]:
        side.find("coefficient").text = {
            "zero": "0",
            "negative": "-1",
            "fraction": "0.5",
            "boolean": "true",
        }[problem]
    elif problem == "duplicate-coefficient":
        side.append(copy.deepcopy(side.find("coefficient")))
    elif problem == "duplicate-compartment":
        side.append(copy.deepcopy(side.find("compartment")))
    elif problem == "protein":
        side[0].tag = "Protein"
    elif problem == "literal-electron":
        side.remove(side[0])
        side.text = "e<SUP>-</SUP>"
    elif problem == "duplicate-side":
        e.append(copy.deepcopy(side))
    elif problem == "bad-compartment":
        side.find("compartment/cco").set("orgid", "ECOLI")
    elif problem == "class-false":
        side.find("Compound").set("class", "false")
    elif problem == "bad-reference":
        side.find("Compound").set("resource", "getxml?META:OTHER")
    elif problem == "empty-left":
        e.remove(side)
    elif problem == "ordering-unknown":
        e.find("reaction-ordering/Reaction").set("frameid", "OTHER")
    elif problem == "ordering-self":
        e.find("reaction-ordering/predecessor-reactions")[0].attrib = dict(
            e.find("reaction-ordering/Reaction").attrib
        )
    elif problem == "ordering-cycle":
        w = ET.SubElement(e, "reaction-ordering")
        native_ref(w, "META", "Reaction", "HALF-A")
        ref(w, "predecessor-reactions", "META", "Reaction", "HALF-B")
    elif problem == "ordering-duplicate":
        e.append(copy.deepcopy(e.find("reaction-ordering")))
    elif problem == "missing-list":
        e.remove(e.find("reaction-list"))
    elif problem == "single-list":
        e.find("reaction-list").remove(e.find("reaction-list")[0])
    with pytest.raises(ValueError):
        metadata(entry(tmp_path, "reaction", root), tmp_path)


def test_composite_explicitness_and_opposite_hydrons_are_retained(tmp_path):
    root = document("reaction")
    e = root[-1]
    e.find("left").remove(e.find("left/coefficient"))
    m = metadata(entry(tmp_path, "reaction", root), tmp_path)["native_electron_transfer"]
    assert [
        (s["side"], s["coefficient"], s["coefficient_explicit"], s["compartment"]["id"])
        for s in m["sides"]
    ] == [("left", 1, False, "MetaCyc:CCO-IN"), ("right", 4, True, "MetaCyc:CCO-OUT")]


@pytest.mark.parametrize(
    "mode,problem",
    [
        ("complex", "monomer"),
        ("complex", "duplicate"),
        ("complex", "state"),
        ("complex", "gene"),
        ("heme", "missing-proof"),
        ("heme", "wrong-enzyme"),
        ("quinone", "member-class"),
        ("quinone", "self-member"),
        ("quinone", "duplicate"),
        ("lipid", "cml-identity"),
        ("lipid", "wrong-parent"),
    ],
)
def test_class_and_complex_scientific_type_boundaries(tmp_path, mode, problem):
    root = document(mode)
    e = root[-1]
    if problem == "monomer":
        e.find("component/coefficient").text = "1"
    elif problem == "duplicate":
        e.append(copy.deepcopy(e.find("component" if mode == "complex" else "instance")))
    elif problem in ["state", "gene"]:
        ref(
            e, "modified-form" if problem == "state" else "gene", e.get("orgid"), "Protein", "OTHER"
        )
    elif problem == "missing-proof":
        e.remove(e.find("cofactors-of"))
    elif problem == "wrong-enzyme":
        e.find("cofactors-of/Enzymatic-Reaction/enzyme")[0].tag = "Compound"
    elif problem == "member-class":
        e.find("instance/Compound").set("class", "true")
    elif problem == "self-member":
        e.find("instance/Compound").set("frameid", e.get("frameid"))
    elif problem == "cml-identity":
        ET.SubElement(ET.SubElement(e, "cml"), "molecule", id="OTHER")
    elif problem == "wrong-parent":
        e.find("parent/Compound").set("frameid", "Hydride-Acceptors")
    with pytest.raises(ValueError):
        metadata(entry(tmp_path, mode, root), tmp_path)


def rdf_document(identifier="99991"):
    root = ET.Element(RDF + "RDF")
    n = ET.SubElement(root, RDF + "Description", {RDF + "about": URI + "Compound_" + identifier})
    for k, v in [
        ("id", identifier),
        ("accession", "POLYMER:" + identifier),
        ("name", "a polymer"),
        ("htmlName", "a <i>polymer</i>"),
        ("formula", "C2H4(C2H4)<i><sub>n</sub></i>"),
        ("charge", "(0)(0)<i><sub>n</sub></i>"),
        ("polymerizationIndex", "n"),
    ]:
        ET.SubElement(
            n,
            RH + k,
            {RDF + "datatype": "http://www.w3.org/2001/XMLSchema#long"} if k == "id" else {},
        ).text = v
    for k, v in [
        (RDFS + "subClassOf", URI + "Polymer"),
        (RDF + "type", "http://www.w3.org/2000/01/rdf-schema#Class"),
        (RH + "underlyingChebi", "http://purl.obolibrary.org/obo/CHEBI_123"),
    ]:
        ET.SubElement(n, k, {RDF + "resource": v})
    return root


def rdf_entry(tmp_path, root=None, key="polymer"):
    p = tmp_path / (key + ".rdf.gz")
    p.write_bytes(gzip.compress(ET.tostring(rdf_document() if root is None else root)))
    return {
        "key": key,
        "kind": RHEA_POLYMER_KIND,
        "path": p.name,
        "url": RHEA_URL,
        "version": "test-whole-rdf",
        "license": "Synthetic fixture",
        "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
    }


@pytest.mark.parametrize(
    "problem",
    [
        "id",
        "accession",
        "uri",
        "type",
        "subclass",
        "index",
        "underlying",
        "html",
        "plain",
        "missing",
        "unknown",
        "mixed-type",
        "late-name",
        "late-id",
        "late-accession",
        "drop-type-bad-accession",
    ],
)
@pytest.mark.parametrize("wanted", [True, False])
def test_polymers_validate_whole_assertions_before_filtering(tmp_path, problem, wanted):
    root = rdf_document()
    n = root[0]
    if problem in ["id", "accession", "index", "html", "plain"]:
        tag = {"index": "polymerizationIndex", "html": "htmlName", "plain": "name"}.get(
            problem, problem
        )
        n.find(RH + tag).text = {
            "id": "123",
            "accession": "POLYMER:123",
            "index": "n/2",
            "html": "other",
            "plain": "<script>bad</script>",
        }[problem]
    elif problem == "uri":
        n.set(RDF + "about", URI + "Compound_bad")
    elif problem == "type":
        n.find(RDF + "type").set(RDF + "resource", "wrong")
    elif problem == "subclass":
        n.find(RDFS + "subClassOf").set(RDF + "resource", URI + "GenericPolypeptide")
    elif problem == "underlying":
        n.find(RH + "underlyingChebi").set(RDF + "resource", "http://evil.example/CHEBI_123")
    elif problem == "missing":
        n.remove(n.find(RH + "formula"))
    elif problem == "unknown":
        ET.SubElement(n, RH + "invented").text = "x"
    elif problem == "mixed-type":
        ET.SubElement(n, RDFS + "subClassOf", {RDF + "resource": URI + "GenericPolypeptide"})
    elif problem.startswith("late-"):
        z = ET.SubElement(root, RDF + "Description", n.attrib)
        k = problem.removeprefix("late-")
        ET.SubElement(z, RH + k).text = "conflict"
    else:
        n.remove(n.find(RDFS + "subClassOf"))
        n.find(RH + "accession").text = "POLYMER:broken"
    item = rdf_entry(tmp_path, root)
    if wanted:
        with pytest.raises(ValueError):
            snap(tmp_path, [item], "RHEA-COMP:99991")
    else:
        other = entry(tmp_path, "reaction")
        with pytest.raises(ValueError):
            snap(tmp_path, [item, other], "MetaCyc:SYNTHETIC.17")


def test_nonconflicting_split_and_duplicate_triples_retain_all_fragments(tmp_path):
    root = rdf_document()
    n = root[0]
    z = ET.SubElement(root, RDF + "Description", dict(n.attrib))
    moved = n.find(RH + "formula")
    n.remove(moved)
    z.append(moved)
    z.append(copy.deepcopy(n.find(RDF + "type")))
    m = metadata(rdf_entry(tmp_path, root), tmp_path)
    native = m["native_polymers"]["RHEA-COMP:99991"]
    assert len(native["fragments"]) == 2 and native["formula"].startswith("C2H4")


@pytest.mark.parametrize(
    "html,plain",
    [
        ("N<sup>5</sup>", "N(5)"),
        ("COO<sup>&#8722;</sup>", "COO(-)"),
        ("&#946;-<small>D</small>-(1&#8594;4)", "beta-D-(1->4)"),
        ("a&#x2194;b", "a<->b"),
        ("CH<sub>3</sub>", "CH3"),
    ],
)
def test_exact_comparison_preserves_typography_semantics(html, plain):
    assert comparison_projection(html) == plain


@pytest.mark.parametrize(
    "value",
    [
        "<script>x</script>",
        '<i x="a">a</i>',
        "<i>a</sub>",
        "<i>a",
        "a<!--x-->",
        "a<?x?>",
        "a&bogus;",
        "a&#0;",
        "a&#xD800;",
        "a&#x110000;",
        "a<sup>word</sup>",
        "a<sup><i>2</i></sup>",
        "<i/>",
        "<i></i>",
        "<I>x</I>",
    ],
)
def test_polymer_markup_rejects_unsafe_or_ambiguous_forms(value):
    with pytest.raises(ValueError):
        comparison_projection(value)


@pytest.mark.parametrize("mode", ["reaction", "complex", "quinone"])
@pytest.mark.parametrize(
    "problem",
    [
        "drop-kind",
        "drop-native",
        "native-id",
        "name",
        "entity-type",
        "label-kind",
        "new-category",
        "core-direction-or-name",
        "context-forgery",
    ],
)
def test_consumer_rejects_forged_typed_snapshots(tmp_path, mode, problem):
    item = entry(tmp_path, mode)
    identifier, _ = term(item, tmp_path)
    data = snap(tmp_path, [item], identifier)
    m = data["sources"]["new"]
    t = data["terms"][identifier]
    field = next(k for k in m if k.startswith("native_"))
    if problem == "drop-kind":
        del m["kind"]
    elif problem == "drop-native":
        del m[field]
    elif problem == "native-id":
        m[field]["id"] = "MetaCyc:OTHER"
    elif problem == "name":
        t["label"] = "invented"
    elif problem == "entity-type":
        t["entity_type"] = "protein"
    elif problem == "label-kind":
        t["label_kind"] = "source_context" if mode != "reaction" else "canonical"
    elif problem == "new-category":
        t["allowed_categories"] = ["protein"]
    elif problem == "core-direction-or-name":
        m[field]["direction" if mode == "reaction" else "direct_common_name"] = "forged"
    else:
        m[field]["context_slots"] = [
            {"tag": "comment", "xml": '<comment datatype="string">forged</comment>'}
        ]
    path = tmp_path / "forged.json"
    path.write_text(json.dumps(data))
    with pytest.raises((ValueError, TypeError)):
        _load_authority(path)


@pytest.mark.parametrize("mode", ["reaction", "complex", "quinone", "heme", "lipid", "polymer"])
@pytest.mark.parametrize(
    "placement", ["valid", "wrong-category", "record", "reaction", "invented-label", "alias"]
)
def test_placement_and_label_checks_precede_contextual_policy(tmp_path, mode, placement):
    item = rdf_entry(tmp_path) if mode == "polymer" else entry(tmp_path, mode)
    identifier = "RHEA-COMP:99991" if mode == "polymer" else term(item, tmp_path)[0]
    data = snap(tmp_path, [item], identifier)
    t = data["terms"][identifier]
    prefix = identifier.split(":")[0]
    data["sources"]["anchor"] = {
        "url": "https://example.org/source",
        "version": "1",
        "license": "test",
        "sha256": "0" * 64,
    }
    data["terms"]["MetaCyc:ROUTE"] = {"label": "route", "synonyms": [], "source": "anchor"}
    folder = tmp_path / "data/pathways"
    folder.mkdir(parents=True)
    conf = tmp_path / "conf"
    conf.mkdir()
    (tmp_path / "authority.json").write_text(json.dumps(data))
    category = {
        "reaction": "molecular_activity",
        "complex": "complex",
        "quinone": "chemical_entity",
        "heme": "cofactor",
        "lipid": "lipid",
        "polymer": "polymer",
    }[mode]
    node = {"id": identifier, "label": t["label"], "category": category}
    r = {"id": "MetaCyc:ROUTE", "label": "route", "taxa": [], "participants": [], "reactions": []}
    target = "reactions" if mode == "reaction" else "participants"
    if placement == "wrong-category":
        node["category"] = "protein"
    elif placement == "record":
        r.update(id=identifier, label=node["label"])
    elif placement == "reaction":
        target = "participants" if mode == "reaction" else "reactions"
    elif placement == "invented-label":
        node["label"] = "invented contextual name"
    elif placement == "alias":
        node["label"] = "Source alias"
    if placement != "record":
        r[target].append(node)
    (folder / "record.yaml").write_text(yaml.safe_dump(r))
    namespaces = {
        p: {"snapshot": "authority.json", "policy": "canonical_or_synonym"}
        for p in {"MetaCyc", prefix}
    }
    rules = [
        {
            "namespace": p,
            "sections": ["record", "participants", "reactions"],
            "record_prefixes": ["MetaCyc", prefix] if prefix != "MetaCyc" else ["MetaCyc"],
            "reason": "Deliberately broad test rule",
        }
        for p in namespaces
    ]
    (conf / "identifier_policy.yaml").write_text(
        yaml.safe_dump({"version": 1, "namespaces": namespaces, "contextual_labels": rules})
    )
    errors = identifier_errors(tmp_path)
    allowed = (
        placement == "valid"
        or placement == "alias"
        and mode != "polymer"
        or placement == "invented-label"
        and mode == "reaction"
    )
    assert bool(errors) != allowed, errors


@pytest.mark.parametrize("mode", ["reaction", "complex", "quinone", "polymer"])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("wanted", [False, True])
@pytest.mark.parametrize("changed", ["identity", "context"])
def test_native_conflicts_fail_in_both_orders_before_selection(
    tmp_path, mode, reverse, wanted, changed
):
    if mode == "polymer":
        first = rdf_entry(tmp_path, key="first")
        r = rdf_document()
        r[0].find(RH + ("name" if changed == "identity" else "formula")).text = (
            "another name" if changed == "identity" else "C3H6(C2H4)<i><sub>n</sub></i>"
        )
        if changed == "identity":
            r[0].find(RH + "htmlName").text = "another name"
        second = rdf_entry(tmp_path, r, key="second")
        identifier = "RHEA-COMP:99991"
    else:
        first = entry(tmp_path, mode, key="first")
        r = document(mode)
        if changed == "context":
            ET.SubElement(
                r[-1],
                "comment" if mode != "reaction" else "orphan",
                **({"datatype": "string"} if mode != "reaction" else {}),
            ).text = "source context" if mode != "reaction" else "NO"
        elif mode == "reaction":
            r[-1].find("left/coefficient").text = "2"
        else:
            r[-1].find("common-name").text = "another name"
        second = entry(tmp_path, mode, r, key="second")
        identifier = term(first, tmp_path)[0]
    entries = [first, second]
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="conflicting"):
        snap(tmp_path, entries, identifier if wanted else "MetaCyc:UNSELECTED")


@pytest.mark.parametrize("mode", ["reaction", "complex", "quinone", "polymer"])
@pytest.mark.parametrize("reverse", [False, True])
def test_identical_native_duplicates_preserve_first_source_without_alias_merge(
    tmp_path, mode, reverse
):
    first = (
        rdf_entry(tmp_path, key="first")
        if mode == "polymer"
        else entry(tmp_path, mode, key="first")
    )
    second = {**first, "key": "second"}
    items = [second, first] if reverse else [first, second]
    identifier = "RHEA-COMP:99991" if mode == "polymer" else term(first, tmp_path)[0]
    data = snap(tmp_path, items, identifier)
    assert data["terms"][identifier]["source"] == items[0]["key"]
    assert set(data["sources"]) == {items[0]["key"]}


@pytest.mark.parametrize("mode", ["reaction", "quinone"])
@pytest.mark.parametrize("legacy", ["html", "carrier", "reaction"])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("wanted", [False, True])
def test_new_metacyc_modes_conflict_with_legacy_kinds(tmp_path, mode, legacy, reverse, wanted):
    first = entry(tmp_path, mode, key="new")
    if legacy == "html":
        path = tmp_path / "old.html"
        path.write_text(
            "<TITLE>MetaCyc native label</TITLE>"
            "<script>typeObjectPage = {object:'SYNTHETIC.17',orgid:'META'}</script>"
        )
        old = {
            **first,
            "kind": "metacyc-html",
            "key": "old",
            "path": path.name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    elif legacy == "carrier":
        r = document("quinone")
        r[-1].find("parent/Compound").set("frameid", "Hydride-Acceptors")
        r[-1].find("parent/Compound").set("resource", "getxml?META:Hydride-Acceptors")
        # Legacy hydride acceptor does not retain chemical-class member grammar.
        r[-1].remove(r[-1].find("instance"))
        old = entry(tmp_path, "quinone", r, key="old")
        old["kind"] = CARRIER_CLASS_KIND
    else:
        r = envelope("SYNTHETIC.17", "META", "Reaction", False)
        e = r[-1]
        for parent in ["Chemical-Reactions", "Small-Molecule-Reactions"]:
            ref(e, "parent", "META", "Reaction", parent, True)
        ET.SubElement(e, "reaction-direction").text = "LEFT-TO-RIGHT"
        ref(e, "left", "META", "Compound", "WATER")
        ref(e, "right", "META", "Compound", "PROTON")
        old = entry(tmp_path, "reaction", r, key="old")
        old["kind"] = "metacyc-reaction-xml"
    items = [old, first] if reverse else [first, old]
    with pytest.raises(ValueError, match="conflicting"):
        snap(tmp_path, items, "MetaCyc:SYNTHETIC.17" if wanted else "MetaCyc:UNSELECTED")


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("wanted", [False, True])
@pytest.mark.parametrize("legacy", ["unnamed", "protein", "generic-polymer"])
def test_new_modes_conflict_with_old_complex_and_generic_component_kinds(
    tmp_path, reverse, wanted, legacy
):
    if legacy == "generic-polymer":
        first = rdf_entry(tmp_path, key="new")
        r = rdf_document()
        n = r[0]
        n.find(RH + "accession").text = "GENERIC:99991"
        n.find(RDFS + "subClassOf").set(RDF + "resource", URI + "GenericPolypeptide")
        old = rdf_entry(tmp_path, r, key="old")
        old["kind"] = "rhea-components-rdf-gz"
        identifier = "RHEA-COMP:99991"
    else:
        first = entry(tmp_path, "complex", key="new")
        r = document("complex")
        if legacy == "unnamed":
            r[-1].remove(r[-1].find("common-name"))
            r[-1].remove(r[-1].find("synonym"))
        old = entry(tmp_path, "complex", r, key="old")
        old["kind"] = ECOCYC_COMPLEX_KIND if legacy == "unnamed" else "ecocyc-protein-xml"
        identifier = "EcoCyc:SYNTHETIC.17"
    items = [old, first] if reverse else [first, old]
    with pytest.raises(ValueError, match="conflicting"):
        snap(tmp_path, items, identifier if wanted else "MetaCyc:UNSELECTED")


@pytest.mark.parametrize(
    "problem",
    [
        "kind",
        "native",
        "uri",
        "accession",
        "index",
        "formula",
        "name",
        "term-type",
        "term-label",
        "term-id",
        "term-extra",
    ],
)
def test_polymer_consumer_metadata_mutations(tmp_path, problem):
    item = rdf_entry(tmp_path)
    data = snap(tmp_path, [item], "RHEA-COMP:99991")
    m = data["sources"]["polymer"]
    n = m["native_polymers"]["RHEA-COMP:99991"]
    t = data["terms"]["RHEA-COMP:99991"]
    if problem == "kind":
        del m["kind"]
    elif problem == "native":
        del m["native_polymers"]
    elif problem == "uri":
        n["uri"] = URI + "Compound_1"
    elif problem == "accession":
        n["native_accession"] = "GENERIC:99991"
    elif problem == "index":
        n["polymerization_index"] = "8"
    elif problem == "formula":
        n["formula"] = "C1"
    elif problem == "name":
        n["name"] = "other"
    elif problem == "term-type":
        t["entity_type"] = "chemical_entity"
    elif problem == "term-label":
        t["label"] = "other"
    elif problem == "term-id":
        data["terms"]["RHEA-COMP:1"] = data["terms"].pop("RHEA-COMP:99991")
    else:
        t["allowed_categories"] = ["chemical_entity"]
    path = tmp_path / "mutated.json"
    path.write_text(json.dumps(data))
    with pytest.raises((ValueError, TypeError)):
        _load_authority(path)


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("wanted", [False, True])
def test_named_complex_conflicts_with_complete_state_pair(tmp_path, reverse, wanted):
    # Both companions are independently valid; conflict is at the claimed entity.
    from tests.test_biocyc_carrier_authority import entry as state_entry

    old = state_entry(tmp_path, "state-red", key="state")
    new = entry(tmp_path, "complex", document("complex", "RED"), key="complex")
    items = [old, new] if reverse else [new, old]
    with pytest.raises(ValueError, match="conflicting"):
        snap(tmp_path, items, "EcoCyc:RED" if wanted else "MetaCyc:UNSELECTED")


@pytest.mark.parametrize("reverse", [False, True])
def test_named_complex_retains_shared_ecocyc_version_guard(tmp_path, reverse):
    first = entry(tmp_path, "complex", key="first")
    r = document("complex", "SECOND")
    r.set("ptools-version", "28.0")
    r.find("metadata/PGDB").set("version", "28.0")
    second = entry(tmp_path, "complex", r, key="second")
    second["version"] = "28.0"
    with pytest.raises(ValueError, match="version"):
        snap(tmp_path, [second, first] if reverse else [first, second], "EcoCyc:SYNTHETIC.17")


def cml(entity):
    n = ET.SubElement(
        ET.SubElement(entity, "cml"),
        "molecule",
        id=entity.get("frameid"),
        title="source drawing",
        formalCharge="-2",
    )
    for tag in ["atomArray", "bondArray", "string"]:
        ET.SubElement(n, tag)
    ET.SubElement(n, "formula", concise="C 2 H 4")
    return n


@pytest.mark.parametrize(
    "problem", ["valid", "charge", "duplicate", "formula", "unknown", "identity", "xref-conflict"]
)
def test_class_structure_and_xref_context_is_bounded_and_retained(tmp_path, problem):
    r = document("lipid")
    e = r[-1]
    m = cml(e)
    ET.SubElement(
        e, "comment", datatype="string"
    ).text = "Native <SUP>opaque</SUP> scientific context"
    d = ET.SubElement(e, "dblink")
    for k, v in [
        ("dblink-db", "CHEBI"),
        ("dblink-oid", "123"),
        ("dblink-relationship", "unification"),
    ]:
        ET.SubElement(d, k).text = v
    if problem == "charge":
        m.set("formalCharge", "-2.5")
    elif problem == "duplicate":
        m.append(copy.deepcopy(m.find("formula")))
    elif problem == "formula":
        m.find("formula").set("invented", "x")
    elif problem == "unknown":
        ET.SubElement(m, "unknown")
    elif problem == "identity":
        m.set("id", "OTHER")
    elif problem == "xref-conflict":
        d2 = copy.deepcopy(d)
        d2.find("dblink-relationship").text = "other"
        e.append(d2)
    item = entry(tmp_path, "lipid", r)
    if problem != "valid":
        with pytest.raises(ValueError):
            metadata(item, tmp_path)
    else:
        n = metadata(item, tmp_path)["native_chemical_class"]
        assert [s["xml"] for s in n["context_slots"]] == [
            ET.tostring(x, encoding="unicode") for x in e if x.tag in {"cml", "comment", "dblink"}
        ]


@pytest.mark.parametrize("mode", ["reaction", "complex", "lipid"])
@pytest.mark.parametrize(
    "problem", ["extra-key", "extra-slot-key", "wrong-slot-tag", "pi", "mixed", "bool-coefficient"]
)
def test_consumer_retained_slot_grammar_cannot_be_bypassed(tmp_path, mode, problem):
    item = entry(tmp_path, mode)
    identifier = term(item, tmp_path)[0]
    data = snap(tmp_path, [item], identifier)
    n = next(v for k, v in data["sources"]["new"].items() if k.startswith("native_"))
    if problem == "extra-key":
        n["invented"] = True
    elif problem == "extra-slot-key":
        n["source_slots"][0]["invented"] = True
    elif problem == "wrong-slot-tag":
        n["source_slots"][0]["tag"] = "common-name"
    elif problem == "pi":
        n["source_slots"][0]["xml"] += "<?forged data?>"
    elif problem == "mixed":
        n["source_slots"][0]["xml"] += "forged"
    elif mode == "reaction":
        n["sides"][0]["coefficient"] = True
    elif mode == "complex":
        n["components"][0]["coefficient"] = True
    else:
        n["allowed_categories"].append("protein")
    p = tmp_path / "forged.json"
    p.write_text(json.dumps(data))
    with pytest.raises((ValueError, TypeError, ET.ParseError)):
        _load_authority(p)


@pytest.mark.parametrize(
    "problem",
    ["hash", "url", "version", "extra", "directory", "absolute", "traversal", "doctype", "pi"],
)
def test_polymer_provenance_and_xml_container_guards(tmp_path, problem):
    item = rdf_entry(tmp_path)
    if problem == "hash":
        item["sha256"] = "0" * 64
    elif problem == "url":
        item["url"] = "https://example.org/rhea.rdf.gz"
    elif problem == "version":
        item["version"] = ""
    elif problem == "extra":
        item["selected"] = "99991"
    elif problem == "directory":
        item["path"] = "."
    elif problem == "absolute":
        item["path"] = str(tmp_path / item["path"])
    elif problem == "traversal":
        item["path"] = "../" + item["path"]
    else:
        p = tmp_path / item["path"]
        raw = gzip.decompress(p.read_bytes())
        p.write_bytes(
            gzip.compress((b"<!DOCTYPE RDF>" if problem == "doctype" else b"<?forged data?>") + raw)
        )
        item["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
    with pytest.raises((ValueError, OSError, ET.ParseError)):
        metadata(item, tmp_path)


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("slot", ["id", "accession", "name", "type", "underlyingChebi"])
def test_polymer_late_fragment_conflicts_in_either_order(tmp_path, reverse, slot):
    root = rdf_document()
    z = ET.SubElement(root, RDF + "Description", dict(root[0].attrib))
    if slot == "type":
        ET.SubElement(z, RDF + "type", {RDF + "resource": "http://example.org/other"})
    elif slot == "underlyingChebi":
        ET.SubElement(z, RH + slot, {RDF + "resource": "http://purl.obolibrary.org/obo/CHEBI_999"})
    else:
        ET.SubElement(
            z,
            RH + slot,
            {RDF + "datatype": "http://www.w3.org/2001/XMLSchema#long"} if slot == "id" else {},
        ).text = "999" if slot == "id" else "conflict"
    if reverse:
        root[:] = list(reversed(root))
    with pytest.raises(ValueError):
        metadata(rdf_entry(tmp_path, root), tmp_path)


@pytest.mark.parametrize("mode", ["reaction", "complex", "quinone", "polymer"])
def test_new_metadata_serialization_is_stable_across_hash_seeds(tmp_path, mode):
    import os
    import subprocess
    import sys

    item = rdf_entry(tmp_path) if mode == "polymer" else entry(tmp_path, mode)
    path = tmp_path / "entry.json"
    path.write_text(json.dumps(item))
    script = """import json,sys
from pathlib import Path
from tests.test_electron_transfer_authority import metadata
p=Path(sys.argv[1]);print(json.dumps(metadata(json.loads(p.read_text()),p.parent),ensure_ascii=False))
"""
    outputs = []
    for seed in ["0", "1", "17", "43"]:
        result = subprocess.run(
            [sys.executable, "-B", "-c", script, str(path)],
            capture_output=True,
            text=True,
            check=False,
            env={**os.environ, "PYTHONHASHSEED": seed, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        assert result.returncode == 0, result.stderr
        outputs.append(result.stdout)
    assert len(set(outputs)) == 1
    assert list(json.loads(outputs[0]))[:4] == ["license", "url", "version", "sha256"]


@pytest.mark.parametrize("mode", ["reaction", "complex", "quinone", "polymer"])
def test_nonregular_fifo_is_rejected_without_reading_it(tmp_path, mode, monkeypatch):
    import os

    item = rdf_entry(tmp_path) if mode == "polymer" else entry(tmp_path, mode)
    target = tmp_path / item["path"]
    target.unlink()
    os.mkfifo(target)
    original = type(target).read_bytes
    reads = []

    def guarded(path):
        if path == target:
            reads.append(str(path))
            raise AssertionError("must not read FIFO")
        return original(path)

    monkeypatch.setattr(type(target), "read_bytes", guarded)
    with pytest.raises(ValueError, match="regular"):
        metadata(item, tmp_path)
    assert not reads


@pytest.mark.parametrize("mode", ["reaction", "complex", "quinone", "polymer"])
def test_resolved_regular_original_can_be_a_symlink(tmp_path, mode):
    item = rdf_entry(tmp_path) if mode == "polymer" else entry(tmp_path, mode)
    original = tmp_path / item["path"]
    link = tmp_path / "link"
    link.symlink_to(original)
    expected = metadata(item, tmp_path)
    assert metadata({**item, "path": "link"}, tmp_path) == expected


@pytest.mark.parametrize("encoding", ["utf-8", "utf-16", "utf-32"])
def test_polymer_doctype_is_rejected_in_supported_xml_encodings(tmp_path, encoding):
    item = rdf_entry(tmp_path)
    p = tmp_path / item["path"]
    original = ET.tostring(rdf_document(), encoding="unicode")
    p.write_bytes(
        gzip.compress(
            ('<?xml version="1.0" encoding="' + encoding + '"?><!DOCTYPE RDF>' + original).encode(
                encoding
            )
        )
    )
    item["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
    with pytest.raises((ValueError, ET.ParseError)):
        metadata(item, tmp_path)


def test_polymer_rdf_container_rejects_mixed_text(tmp_path):
    root = rdf_document()
    root.text = "unowned text"
    with pytest.raises(ValueError):
        metadata(rdf_entry(tmp_path, root), tmp_path)
