"""Synthetic native BioPAX authorities; production inputs remain external."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.identifiers import identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, main, pathbank_terms

BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
XML = "{http://www.w3.org/XML/1998/namespace}"
BASE = "https://example.org/native.owl"
PATHWAY = "PathBank:SMP9999999"


def native_source():
    root = ET.Element(RDF + "RDF", {XML + "base": BASE})
    pathway = ET.SubElement(root, BP + "Pathway", {
        RDF + "about": "http://identifiers.org/smpdb/SMP9999999",
    })
    ET.SubElement(pathway, BP + "displayName").text = "Native pathway title"
    ET.SubElement(pathway, BP + "xref", {RDF + "resource": "#xref"})
    ET.SubElement(pathway, BP + "pathwayComponent", {RDF + "resource": "#Reactions/7"})
    xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "xref"})
    ET.SubElement(xref, BP + "db").text = "SMPDB"
    ET.SubElement(xref, BP + "id").text = "SMP9999999"
    reaction = ET.SubElement(root, BP + "BiochemicalReaction", {RDF + "ID": "Reactions/7"})
    ET.SubElement(reaction, BP + "displayName").text = "1.2.3.4"
    ET.SubElement(reaction, BP + "name").text = "Native substrate → native product"
    ET.SubElement(root, BP + "Complex", {RDF + "ID": "ProteinComplex/8"})
    # Neither an external xref nor a referenced-but-undeclared local object is
    # an authority for a new native or target-namespace identifier.
    ET.SubElement(reaction, BP + "left", {RDF + "resource": "#Compound/missing"})
    chemical_xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "chebi"})
    ET.SubElement(chemical_xref, BP + "db").text = "ChEBI"
    ET.SubElement(chemical_xref, BP + "id").text = "CHEBI:15377"
    ET.SubElement(chemical_xref, BP + "displayName").text = "Not a ChEBI authority label"
    return root


def test_native_smp_accession_and_declared_graph_only():
    terms = list(pathbank_terms(native_source()))
    assert terms == [
        (PATHWAY, "Native pathway title", []),
        (PATHWAY + "/Reactions/7", "1.2.3.4", ["Native substrate → native product"]),
        (PATHWAY + "/ProteinComplex/8", "ProteinComplex/8", []),
    ]


@pytest.mark.parametrize("about", ["#Reactions/7", BASE + "#Reactions/7"])
def test_local_rdf_about_and_rdf_id_have_the_same_identity(about):
    root = native_source()
    root.find(BP + "BiochemicalReaction").attrib = {RDF + "about": about}
    assert list(pathbank_terms(root))[1][0] == PATHWAY + "/Reactions/7"


@pytest.mark.parametrize("problem", [
    "missing-xref", "pathwhiz-only", "wrong-uri", "malformed-accession",
    "conflicting-xrefs", "multiple-pathways", "unlabelled-pathway", "duplicate-subject",
    "foreign-graph-uri", "nested-base", "missing-local-id", "unsafe-local-id",
    "dual-subject-attributes", "conflicting-xref-values", "conflicting-xref-databases",
])
def test_ambiguous_or_unsupported_identity_fails_closed(problem):
    root = native_source()
    pathway = root.find(BP + "Pathway")
    xref = root.find(BP + "UnificationXref")
    if problem == "missing-xref":
        root.remove(xref)
    elif problem == "pathwhiz-only":
        xref.find(BP + "db").text = "PathWhiz"
        xref.find(BP + "id").text = "PW9999999"
    elif problem == "wrong-uri":
        pathway.set(RDF + "about", "http://identifiers.org/smpdb/SMP9999998")
    elif problem == "malformed-accession":
        xref.find(BP + "id").text = "PW9999999"
    elif problem == "conflicting-xrefs":
        extra = copy.deepcopy(xref)
        extra.set(RDF + "ID", "other-xref")
        extra.find(BP + "id").text = "SMP9999998"
        root.append(extra)
        ET.SubElement(pathway, BP + "xref", {RDF + "resource": "#other-xref"})
    elif problem == "multiple-pathways":
        extra = copy.deepcopy(pathway)
        extra.set(RDF + "about", "http://identifiers.org/smpdb/SMP9999998")
        root.append(extra)
    elif problem == "unlabelled-pathway":
        pathway.remove(pathway.find(BP + "displayName"))
    elif problem == "duplicate-subject":
        root.append(copy.deepcopy(root.find(BP + "Complex")))
    elif problem == "foreign-graph-uri":
        root.find(BP + "Complex").attrib = {RDF + "about": "https://other.org/#ProteinComplex/8"}
    elif problem == "nested-base":
        root.find(BP + "Complex").set(XML + "base", "https://other.org/")
    elif problem == "missing-local-id":
        root.find(BP + "Complex").attrib.clear()
    elif problem == "unsafe-local-id":
        root.find(BP + "Complex").set(RDF + "ID", "ProteinComplex/../8")
    elif problem == "dual-subject-attributes":
        root.find(BP + "Complex").set(RDF + "about", "#ProteinComplex/9")
    elif problem == "conflicting-xref-values":
        ET.SubElement(xref, BP + "id").text = "SMP9999998"
    elif problem == "conflicting-xref-databases":
        ET.SubElement(xref, BP + "db").text = "PathWhiz"
    with pytest.raises(ValueError, match="PathBank"):
        list(pathbank_terms(root))


def authority_fixture(tmp_path):
    records = tmp_path / "data" / "pathways"
    records.mkdir(parents=True)
    record = {
        "id": PATHWAY, "label": "Native pathway title", "taxa": [],
        "participants": [{"id": PATHWAY + "/ProteinComplex/8", "label": "Curated assembly"}],
        "reactions": [{"id": PATHWAY + "/Reactions/7", "label": "Curated reaction step"}],
    }
    record_path = records / "pathway.yaml"
    record_path.write_text(yaml.safe_dump(record))
    source = tmp_path / "PW_DIFFERENT.owl"
    raw = ET.tostring(native_source())
    source.write_bytes(raw)
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([{
        "key": "native", "kind": "pathbank-biopax", "path": source.name,
        "url": "https://example.org/public.zip", "version": "fixture", "license": "fixture",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "sha256_scope": "Unmodified synthetic archive member PW_DIFFERENT.owl",
    }]))
    return manifest, records, record, record_path


def test_builder_selects_independent_labels_and_marks_local_context(tmp_path):
    manifest, records, _, _ = authority_fixture(tmp_path)
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"][PATHWAY]["label"] == "Native pathway title"
    assert "label_kind" not in result["terms"][PATHWAY]
    assert result["terms"][PATHWAY + "/Reactions/7"]["label_kind"] == "source_context"
    assert result["terms"][PATHWAY + "/ProteinComplex/8"]["label_kind"] == "source_context"
    assert "Curated" not in json.dumps(result)
    assert result["sources"]["native"]["sha256_scope"].endswith("PW_DIFFERENT.owl")


@pytest.mark.parametrize("missing", [PATHWAY + "/Compound/missing", "PathBank:PW9999999"])
def test_unresolved_pathbank_id_cannot_replace_existing_snapshot(tmp_path, monkeypatch, missing):
    manifest, records, record, path = authority_fixture(tmp_path)
    record["participants"].append({"id": missing, "label": "Plausible name"})
    path.write_text(yaml.safe_dump(record))
    output = tmp_path / "authority.json"
    output.write_text("previous authority\n")
    monkeypatch.setattr(sys, "argv", [
        "build_source_identifier_snapshot.py", "--manifest", str(manifest),
        "--records", str(records), "--cache-dir", str(tmp_path), "--output", str(output),
    ])
    with pytest.raises(ValueError, match="unresolved source identifiers: PathBank"):
        main()
    assert output.read_text() == "previous authority\n"


@pytest.mark.parametrize("problem,code", [
    (None, None), ("missing", "ID_NOT_FOUND"), ("wrong-title", "LABEL_MISMATCH"),
    ("local-id-as-pathway", "LABEL_AUTHORITY_UNAVAILABLE"),
    ("other-record-prefix", "LABEL_AUTHORITY_UNAVAILABLE"),
])
def test_production_pathbank_policy_is_contextual_only_in_declared_slots(tmp_path, problem, code):
    manifest, records, record, path = authority_fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    snapshot["terms"]["MetaCyc:TEST"] = {
        "label": "Other native pathway", "synonyms": [], "source": "native",
    }
    policy = yaml.safe_load(Path("conf/identifier_policy.yaml").read_text())
    policy["namespaces"] = {
        key: value for key, value in policy["namespaces"].items() if key in {"PathBank", "MetaCyc"}
    }
    policy["contextual_labels"] = [
        rule for rule in policy["contextual_labels"] if rule["namespace"] == "PathBank"
    ]
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf" / "identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data" / "identifier_authorities" / "sources.json"
    authority.parent.mkdir()
    authority.write_text(json.dumps(snapshot))
    if problem == "missing":
        record["participants"][0]["id"] = PATHWAY + "/ProteinComplex/absent"
    elif problem == "wrong-title":
        record["label"] = "Different pathway"
    elif problem == "local-id-as-pathway":
        record["id"] = PATHWAY + "/ProteinComplex/8"
        record["label"] = "ProteinComplex/8"
    elif problem == "other-record-prefix":
        record["id"] = "MetaCyc:TEST"
        record["label"] = "Other native pathway"
    path.write_text(yaml.safe_dump(record))
    errors = identifier_errors(tmp_path)
    if code:
        assert any(code in error for error in errors), errors
    else:
        assert errors == []
