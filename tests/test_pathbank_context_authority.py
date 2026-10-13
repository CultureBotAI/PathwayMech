from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest

from pathwaymech.identifiers import _load_authority
from pathwaymech.pathbank_context import (
    PATHBANK_CONTEXT_KIND,
    context_term,
    context_terms,
    pathbank_terms,
    validate_context_assertions,
    validate_context_metadata,
)
from scripts.build_source_identifier_snapshot import build_snapshot

FIXTURE = Path(__file__).parent / "fixtures/pathbank_context/SMP0002097.owl"
RAW = FIXTURE.read_bytes()
URL = "https://pathbank.org/view/SMP0002097/download?type=owl_markup"
BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
STRING = {RDF + "datatype": "http://www.w3.org/2001/XMLSchema#string"}
ROOT = "PathBank:SMP0002097"
LOC = ROOT + "/CellularLocation/Cytosol"
INTERFACE = ROOT + "/SubPathwayInteractions/553236"


def owner(raw=RAW, url=URL):
    return {
        "kind": PATHBANK_CONTEXT_KIND,
        "url": url,
        "version": "complete current source acquired 2026-10-12",
        "license": "PathBank terms; public-release review deferred",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "native_pathbank_context": {"xml": raw.decode(), "bytes": len(raw)},
    }


def snapshot(raw=RAW, selected=LOC):
    metadata = owner(raw)
    parsed = {r[0]: r for r in context_terms(raw, URL)}
    return {
        "version": 1,
        "sources": {"typed": metadata},
        "terms": {selected: context_term(selected, parsed, "typed")},
    }


def consume(tmp_path, data):
    path = tmp_path / "authority.json"
    path.write_text(json.dumps(data))
    return _load_authority(path)


def produce(tmp_path, entries, wanted=LOC):
    manifest = []
    for i, (kind, raw, url) in enumerate(entries):
        name = f"original-{i}.owl"
        (tmp_path / name).write_bytes(raw)
        manifest.append(
            {
                "key": str(i),
                "kind": kind,
                "path": name,
                "url": url,
                "version": "2026-10-12",
                "license": "source terms",
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest))
    records = tmp_path / "records"
    records.mkdir()
    (records / "selected.yaml").write_text(f"id: {wanted}\n")
    return build_snapshot(path, records, tmp_path)


def tree_mutation(case):
    root = ET.fromstring(RAW)
    index = {n.get(RDF + "ID") or n.get(RDF + "about"): n for n in root}
    loc = index["CellularLocation/Cytosol"]
    interaction = index["SubPathwayInteractions/553236"]
    child = index["http://identifiers.org/smpdb/SMP0000857"]
    primary = index["http://identifiers.org/smpdb/SMP0002097"]
    sam = index["Compound/PW_C000921_Cytosol"]
    step = index["SubPathwayInteractionSteps/SubPathway553236"]
    xref = index["Reference/GENE_ONTOLOGY_GO_0005829"]
    if case == "location_no_term":
        loc.remove(loc.find(BP + "term"))
    elif case == "location_duplicate_term":
        loc.append(copy.deepcopy(loc.find(BP + "term")))
    elif case == "location_empty_term":
        loc.find(BP + "term").text = " "
    elif case == "location_resource_term":
        loc.find(BP + "term").attrib = {RDF + "resource": "#x"}
    elif case == "location_wrong_datatype":
        loc.find(BP + "term").set(RDF + "datatype", "wrong")
    elif case == "location_no_xref":
        loc.remove(loc.find(BP + "xref"))
    elif case == "location_duplicate_xref":
        loc.append(copy.deepcopy(loc.find(BP + "xref")))
    elif case == "location_dangling_xref":
        loc.find(BP + "xref").set(RDF + "resource", "#absent")
    elif case == "location_wrong_type":
        loc.tag = BP + "SmallMolecule"
    elif case == "location_wrong_xref_type":
        xref.tag = BP + "RelationshipXref"
    elif case == "location_wrong_db":
        xref.find(BP + "db").text = "OTHER"
    elif case == "location_wrong_go":
        xref.find(BP + "id").text = "GO:not-a-number"
    elif case == "location_extra_field":
        ET.SubElement(loc, BP + "left", {RDF + "resource": "#Compound/PW_C000921"})
    elif case == "location_orphan":
        for n in root:
            for link in list(n.findall(BP + "cellularLocation")):
                if link.get(RDF + "resource") == "#CellularLocation/Cytosol":
                    n.remove(link)
    elif case == "physical_duplicate_location":
        sam.append(copy.deepcopy(sam.find(BP + "cellularLocation")))
    elif case == "physical_foreign_location":
        sam.find(BP + "cellularLocation").set(
            RDF + "resource", "https://wrong.example/#CellularLocation/Cytosol"
        )
    elif case == "physical_nonvocabulary":
        sam.find(BP + "cellularLocation").set(RDF + "resource", "#Compound/PW_C000921")
    elif case == "interface_orphan":
        child.remove(child.find(BP + "pathwayComponent"))
    elif case == "interface_wrong_order":
        step.find(BP + "stepProcess").set(RDF + "resource", "#Reactions/5165")
    elif case == "interface_extra_owner":
        ET.SubElement(
            primary, BP + "pathwayComponent", {RDF + "resource": "#SubPathwayInteractions/553236"}
        )
    elif case == "interface_duplicate_member":
        child.append(copy.deepcopy(child.find(BP + "pathwayComponent")))
    elif case == "interface_duplicate_order":
        child.append(copy.deepcopy(child.find(BP + "pathwayOrder")))
    elif case == "interface_no_participant":
        interaction.remove(interaction.find(BP + "participant"))
    elif case == "interface_duplicate_participant":
        interaction.append(copy.deepcopy(interaction.find(BP + "participant")))
    elif case == "interface_noncompound":
        interaction.find(BP + "participant").set(RDF + "resource", "#Protein/5967")
    elif case == "interface_foreign_participant":
        interaction.find(BP + "participant").set(
            RDF + "resource", "https://wrong.example/#Compound/PW_C000921_Cytosol"
        )
    elif case == "interface_inhibitory":
        interaction.find(BP + "name").text = "InhibitorySubPathwayControl"
    elif case.startswith("interface_add_"):
        ET.SubElement(
            interaction, BP + case.removeprefix("interface_add_"), STRING
        ).text = "unsupported"
    elif case == "participant_no_reference":
        sam.remove(sam.find(BP + "entityReference"))
    elif case == "participant_wrong_reference":
        sam.find(BP + "entityReference").set(RDF + "resource", "#Protein/5967")
    elif case == "participant_no_location":
        sam.remove(sam.find(BP + "cellularLocation"))
    elif case == "participant_no_output":
        sam.remove(sam.find(BP + "name"))
    elif case == "child_wrong_marker":
        child.find(BP + "name").text = "SomethingElse"
    elif case == "child_extra_field":
        ET.SubElement(child, BP + "left", STRING).text = "extra"
    elif case == "primary_no_child":
        primary.remove(
            next(
                n
                for n in primary.findall(BP + "pathwayComponent")
                if n.get(RDF + "resource", "").endswith("SMP0000857")
            )
        )
    elif case == "primary_duplicate_child":
        primary.append(
            copy.deepcopy(
                next(
                    n
                    for n in primary.findall(BP + "pathwayComponent")
                    if n.get(RDF + "resource", "").endswith("SMP0000857")
                )
            )
        )
    elif case == "primary_missing_step":
        root.remove(index["PathwaySubPathway/553236"])
    elif case == "duplicate_subject":
        root.append(copy.deepcopy(loc))
    elif case == "ambiguous_subject":
        loc.set(RDF + "about", "#CellularLocation/Cytosol")
    elif case == "traversal_subject":
        loc.set(RDF + "ID", "../CellularLocation/Cytosol")
    elif case == "foreign_subject":
        loc.attrib = {RDF + "about": "https://wrong.example/#CellularLocation/Cytosol"}
    elif case == "nested_base":
        loc.set("{http://www.w3.org/XML/1998/namespace}base", "https://wrong.example/")
    else:
        raise AssertionError(case)
    return ET.tostring(root, encoding="utf-8")


BAD_TREES = [
    "location_no_term",
    "location_duplicate_term",
    "location_empty_term",
    "location_resource_term",
    "location_wrong_datatype",
    "location_no_xref",
    "location_duplicate_xref",
    "location_dangling_xref",
    "location_wrong_type",
    "location_wrong_xref_type",
    "location_wrong_db",
    "location_wrong_go",
    "location_extra_field",
    "location_orphan",
    "physical_duplicate_location",
    "physical_foreign_location",
    "physical_nonvocabulary",
    "interface_orphan",
    "interface_wrong_order",
    "interface_extra_owner",
    "interface_duplicate_member",
    "interface_duplicate_order",
    "interface_no_participant",
    "interface_duplicate_participant",
    "interface_noncompound",
    "interface_foreign_participant",
    "interface_inhibitory",
    "interface_add_left",
    "interface_add_right",
    "interface_add_conversionDirection",
    "interface_add_controller",
    "interface_add_participantStoichiometry",
    "interface_add_catalysis",
    "participant_no_reference",
    "participant_wrong_reference",
    "participant_no_location",
    "participant_no_output",
    "child_wrong_marker",
    "child_extra_field",
    "primary_no_child",
    "primary_duplicate_child",
    "primary_missing_step",
    "duplicate_subject",
    "ambiguous_subject",
    "traversal_subject",
    "foreign_subject",
    "nested_base",
]


def test_whole_real_document_and_legacy_projection(tmp_path):
    receipt = json.loads(FIXTURE.with_suffix(".receipt.json").read_text())
    assert receipt["body"]["sha256"] == hashlib.sha256(RAW).hexdigest()
    assert len(RAW) == 70189 and len(ET.fromstring(RAW)) == 208
    terms = context_terms(RAW, URL)
    assert len(terms) == 38
    assert terms[:35] == list(pathbank_terms(ET.fromstring(RAW), url=URL))
    assert [row[0] for row in terms[-3:]] == [
        LOC,
        ROOT + "/CellularLocation/Periplasmic_Space",
        INTERFACE,
    ]
    actual = produce(tmp_path, [(PATHBANK_CONTEXT_KIND, RAW, URL)])
    assert actual["sources"]["0"]["native_pathbank_context"]["xml"].encode() == RAW
    assert consume(tmp_path, actual) == actual["terms"]


@pytest.mark.parametrize("case", BAD_TREES)
@pytest.mark.parametrize("boundary", ["producer", "consumer"])
def test_incomplete_native_context_rejected(tmp_path, case, boundary):
    raw = tree_mutation(case)
    with pytest.raises(ValueError):
        if boundary == "producer":
            produce(tmp_path, [(PATHBANK_CONTEXT_KIND, raw, URL)])
        else:
            data = snapshot()
            data["sources"]["typed"] = owner(raw)
            consume(tmp_path, data)


@pytest.mark.parametrize(
    "url",
    [
        URL.replace("https:", "http:"),
        URL.replace("pathbank.org", "wrong.example"),
        URL.replace("pathbank.org", "www.pathbank.org"),
        URL + "#x",
        URL + "&extra=x",
        URL.replace("SMP0002097", "SMP0000857"),
        URL.replace("/download", "/../download"),
        URL.replace("pathbank.org", "pathbank.org.evil.example"),
        URL.replace("/view/", "/view/%2e%2e/"),
    ],
)
def test_invalid_typed_request(url):
    with pytest.raises(ValueError):
        context_terms(RAW, url)


@pytest.mark.parametrize(
    "raw",
    [
        b'<!DOCTYPE rdf:RDF [<!ENTITY x "evil">]>' + RAW,
        RAW.replace(
            b'<?xml version="1.0" encoding="UTF-8"?>', b'<?xml version="1.0" encoding="latin1"?>'
        ),
        RAW.replace(b"Cytosol", b"Cytosol\xff", 1),
        b"<broken>",
    ],
)
def test_unsafe_or_incomplete_document(raw):
    with pytest.raises(ValueError):
        context_terms(raw, URL)


def coherent_raw(case):
    if case == "term":
        return RAW.replace(b">Cytosol</bp:term>", b">Other compartment</bp:term>")
    if case == "xref":
        return RAW.replace(b">GO:0005829</bp:id>", b">GO:0005737</bp:id>")
    if case == "participant":
        # Still a complete valid generic interface but a different native state.
        return RAW.replace(b"Compound/PW_C000921_Cytosol", b"Compound/PW_C000921_OtherState")
    if case == "unselected_object":
        return (
            RAW.replace(b">Cadaverine</bp:displayName>", b">Changed</bp:displayName>")
            if b">Cadaverine</bp:displayName>" in RAW
            else RAW.replace(b"CC[C", b"CCC[C", 1)
        )
    raise AssertionError(case)


@pytest.mark.parametrize("case", ["term", "xref", "participant"])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [ROOT, LOC, INTERFACE])
def test_coherent_whole_owner_conflicts_before_selection(tmp_path, case, reverse, selected):
    other = coherent_raw(case)
    assert other != RAW and len(context_terms(other, URL)) == 38
    entries = [(PATHBANK_CONTEXT_KIND, RAW, URL), (PATHBANK_CONTEXT_KIND, other, URL)]
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="conflicting complete issuer"):
        produce(tmp_path, entries, selected)
    data = snapshot(selected=selected)
    data["sources"]["unselected"] = owner(other)
    if reverse:
        data["sources"] = dict(reversed(list(data["sources"].items())))
    with pytest.raises(ValueError, match="conflicting complete issuer"):
        consume(tmp_path, data)


@pytest.mark.parametrize("kind", ["pathbank-biopax", "biopax"])
@pytest.mark.parametrize(
    "url", [URL, "https://example.org/no-frame-id", URL.replace("SMP0002097", "SMP9999999")]
)
@pytest.mark.parametrize("reverse", [False, True])
def test_producer_body_identity_cannot_hide_behind_request_or_selection(
    tmp_path, kind, url, reverse
):
    entries = [(PATHBANK_CONTEXT_KIND, RAW, URL), (kind, RAW, url)]
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="PathBank context"):
        produce(tmp_path, entries, INTERFACE)


@pytest.mark.parametrize(
    "url",
    [
        URL,
        URL.replace("pathbank.org", "www.pathbank.org"),
        URL.replace("pathbank.org", "PATHBANK.ORG"),
        URL.replace("https:", "http:"),
        URL.replace("/view/", "/%76iew/"),
        URL.replace("pathbank.org", "%70athbank.org"),
        URL.replace("SMP", "smp"),
        URL.replace("pathbank.org", "pathbank.org."),
    ],
)
@pytest.mark.parametrize("reverse", [False, True])
def test_consumer_unselected_request_only_downgrade_claim(tmp_path, url, reverse):
    data = snapshot()
    stripped = {k: v for k, v in owner().items() if k not in {"kind", "native_pathbank_context"}}
    stripped["url"] = url
    data["sources"]["unselected"] = stripped
    if reverse:
        data["sources"] = dict(reversed(list(data["sources"].items())))
    with pytest.raises(ValueError, match="untyped competing issuer"):
        consume(tmp_path, data)


@pytest.mark.parametrize(
    "field", ["kind", "native_pathbank_context", "sha256", "url", "version", "license"]
)
def test_missing_typed_owner_field(tmp_path, field):
    data = snapshot()
    del data["sources"]["typed"][field]
    with pytest.raises(ValueError):
        consume(tmp_path, data)


@pytest.mark.parametrize(
    "change",
    [
        "extra",
        "hash",
        "length",
        "bytes_bool",
        "xml_type",
        "kind",
        "native_extra",
        "term_label",
        "term_synonyms",
        "term_kind",
        "term_entity",
    ],
)
def test_owner_and_term_tampering(tmp_path, change):
    data = snapshot()
    m = data["sources"]["typed"]
    t = data["terms"][LOC]
    if change == "extra":
        m["unexpected"] = "x"
    elif change == "hash":
        m["sha256"] = "0" * 64
    elif change == "length":
        m["native_pathbank_context"]["bytes"] += 1
    elif change == "bytes_bool":
        m["native_pathbank_context"]["bytes"] = True
    elif change == "xml_type":
        m["native_pathbank_context"]["xml"] = []
    elif change == "kind":
        m["kind"] = "pathbank-biopax"
    elif change == "native_extra":
        m["native_pathbank_context"]["extra"] = "x"
    elif change == "term_label":
        t["label"] = "altered"
    elif change == "term_synonyms":
        t["synonyms"] = ["invented"]
    elif change == "term_kind":
        t["label_kind"] = "canonical"
    elif change == "term_entity":
        t["entity_type"] = "reaction"
    with pytest.raises(ValueError):
        consume(tmp_path, data)


def test_valid_other_document_and_identical_later_evidence(tmp_path):
    other = RAW.replace(b"SMP0002097", b"SMP9999999")
    entries = [
        (PATHBANK_CONTEXT_KIND, RAW, URL),
        (PATHBANK_CONTEXT_KIND, RAW, URL),
        (PATHBANK_CONTEXT_KIND, other, URL.replace("SMP0002097", "SMP9999999")),
    ]
    actual = produce(tmp_path, entries)
    assert actual["terms"][LOC]["source"] == "0"
    data = snapshot()
    data["sources"]["identical"] = owner()
    data["sources"]["unrelated"] = owner(other, URL.replace("SMP0002097", "SMP9999999"))
    assert consume(tmp_path, data) == data["terms"]


def test_different_local_identity_and_native_label_are_not_hardcoded():
    other = RAW.replace(b"CellularLocation/Cytosol", b"CellularLocation/NativeAlternative")
    other = other.replace(b">Cytosol</bp:term>", b">Native alternative</bp:term>")
    parsed = dict((row[0], row) for row in context_terms(other, URL))
    assert parsed[ROOT + "/CellularLocation/NativeAlternative"][1] == "Native alternative"


def test_unrelated_untyped_request_remains_valid(tmp_path):
    data = snapshot()
    stripped = {k: v for k, v in owner().items() if k not in {"kind", "native_pathbank_context"}}
    stripped["url"] = "https://example.org/view/SMP0002097/download"
    data["sources"]["unrelated"] = stripped
    assert consume(tmp_path, data) == data["terms"]


def test_complete_owner_registry_with_no_selected_terms():
    assert len(validate_context_assertions({"unused": owner()})["unused"]) == 38
    assert len(validate_context_metadata(owner())) == 38


@pytest.mark.parametrize("reverse", [False, True])
def test_shared_attached_pathway_native_name_conflict(tmp_path, reverse):
    other = RAW.replace(b"SMP0002097", b"SMP9999999")
    other = other.replace(b"S-Adenosyl-L-Methionine Biosynthesis", b"Conflicting native pathway")
    other_url = URL.replace("SMP0002097", "SMP9999999")
    assert len(context_terms(other, other_url)) == 38
    entries = [(PATHBANK_CONTEXT_KIND, RAW, URL), (PATHBANK_CONTEXT_KIND, other, other_url)]
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="conflicting PathBank native pathway names"):
        produce(tmp_path, entries)
    data = snapshot()
    data["sources"]["unselected"] = owner(other, other_url)
    if reverse:
        data["sources"] = dict(reversed(list(data["sources"].items())))
    with pytest.raises(ValueError, match="conflicting PathBank native pathway names"):
        consume(tmp_path, data)


def incomplete_context(case):
    root = ET.fromstring(RAW)
    index = {n.get(RDF + "ID") or n.get(RDF + "about"): n for n in root}
    child = index["http://identifiers.org/smpdb/SMP0000857"]
    reference = index["CompoundReference/PW_C000921"]
    if case == "remove_child_pathwhiz_xref":
        child.remove(
            next(n for n in child.findall(BP + "xref") if "PathWhiz" in n.get(RDF + "resource"))
        )
    elif case == "empty_interface_compound_reference":
        for n in list(reference):
            reference.remove(n)
    elif case == "missing_formula":
        reference.remove(reference.find(BP + "chemicalFormula"))
    elif case == "invalid_mass":
        reference.find(BP + "molecularWeight").text = "NaN"
    elif case == "missing_structure_data":
        structure = index["ChemicalStructure/PW_C000921"]
        structure.remove(structure.find(BP + "structureData"))
    elif case == "missing_reference_xref":
        reference.remove(reference.find(BP + "xref"))
    elif case == "empty_reference_xref_object":
        xref = index["Reference/PubChem-compound_24762165"]
        for n in list(xref):
            xref.remove(n)
    else:
        raise AssertionError(case)
    return ET.tostring(root, encoding="utf-8")


@pytest.mark.parametrize(
    "case", ["remove_child_pathwhiz_xref", "empty_interface_compound_reference"]
)
@pytest.mark.parametrize("boundary", ["producer", "consumer"])
def test_required_child_and_reference_contents(tmp_path, case, boundary):
    raw = incomplete_context(case)
    with pytest.raises(ValueError, match="PathBank context"):
        if boundary == "producer":
            produce(tmp_path, [(PATHBANK_CONTEXT_KIND, raw, URL)])
        else:
            data = snapshot()
            data["sources"]["typed"] = owner(raw)
            consume(tmp_path, data)


@pytest.mark.parametrize(
    "case",
    [
        "missing_formula",
        "invalid_mass",
        "missing_structure_data",
        "missing_reference_xref",
        "empty_reference_xref_object",
    ],
)
@pytest.mark.parametrize("boundary", ["producer", "consumer"])
def test_interface_reference_requires_complete_native_fields(tmp_path, case, boundary):
    raw = incomplete_context(case)
    with pytest.raises(ValueError, match="PathBank context"):
        if boundary == "producer":
            produce(tmp_path, [(PATHBANK_CONTEXT_KIND, raw, URL)])
        else:
            data = snapshot()
            data["sources"]["typed"] = owner(raw)
            consume(tmp_path, data)


def test_context_owner_serialization_stable_across_hash_seeds(tmp_path):
    """The same complete issuer body must serialize byte identically across processes."""
    (tmp_path / "original.owl").write_bytes(RAW)
    entry = {
        "key": "typed",
        "kind": PATHBANK_CONTEXT_KIND,
        "path": "original.owl",
        "url": URL,
        "version": "2026-10-12",
        "license": "source terms",
        "sha256": hashlib.sha256(RAW).hexdigest(),
    }
    (tmp_path / "manifest.json").write_text(json.dumps([entry]))
    records = tmp_path / "records"
    records.mkdir()
    ids = [row[0] for row in context_terms(RAW, URL)]
    (records / "selected.yaml").write_text(
        "id: "
        + ids[0]
        + "\nparticipants:\n"
        + "".join("  - id: " + identifier + "\n" for identifier in ids[1:])
    )
    program = """
import json, sys
from pathlib import Path
from scripts.build_source_identifier_snapshot import build_snapshot
from pathwaymech.identifiers import _load_authority
root=Path(sys.argv[1])
snapshot=build_snapshot(root/'manifest.json',root/'records',root)
body=json.dumps(snapshot,indent=2,ensure_ascii=False)+'\\n'
path=root/('result-'+sys.argv[2]+'.json')
path.write_text(body)
assert _load_authority(path)==snapshot['terms']
assert len(snapshot['terms'])==38
print(body,end='')
"""
    results = []
    for seed in ("1", "2", "3"):
        result = subprocess.run(
            [sys.executable, "-B", "-c", program, str(tmp_path), seed],
            env={**os.environ, "PYTHONHASHSEED": seed, "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True,
            text=True,
            check=True,
        )
        results.append(result.stdout)
    assert results[0] == results[1] == results[2]
    assert list(json.loads(results[0])["sources"]["typed"]) == [
        "kind",
        "url",
        "version",
        "license",
        "sha256",
        "native_pathbank_context",
    ]
