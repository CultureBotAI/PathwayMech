"""Whole protein redox states must remain distinct from reactive-part ChEBI IDs."""

import gzip
import hashlib
import json
from xml.etree import ElementTree as ET

import pytest
import yaml

from scripts.build_source_identifier_snapshot import build_snapshot, rhea_component_terms

RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RH = "{http://rdf.rhea-db.org/}"
RDFS = "{http://www.w3.org/2000/01/rdf-schema#}"


def source():
    root = ET.Element(RDF + "RDF")
    for number, name in [(41, "oxidized carrier"), (42, "reduced carrier")]:
        node = ET.SubElement(root, RDF + "Description", {
            RDF + "about": f"http://rdf.rhea-db.org/Compound_{number}",
        })
        ET.SubElement(node, RH + "id").text = str(number)
        ET.SubElement(node, RH + "accession").text = f"GENERIC:{number}"
        ET.SubElement(node, RH + "name").text = name
        ET.SubElement(node, RDFS + "subClassOf", {
            RDF + "resource": "http://rdf.rhea-db.org/GenericPolypeptide",
        })
    # A free chemical and a bound reactive part are neither whole carrier.
    for uri, kind in [("Compound_15377", "SmallMolecule"),
                      ("Compound_41_rp1", "ReactivePart")]:
        node = ET.SubElement(root, RDF + "Description", {
            RDF + "about": f"http://rdf.rhea-db.org/{uri}",
        })
        ET.SubElement(node, RH + "name").text = "reactive chemical"
        ET.SubElement(node, RDFS + "subClassOf", {
            RDF + "resource": "http://rdf.rhea-db.org/" + kind,
        })
    return root


def write_source(tmp_path, root):
    path = tmp_path / "rhea.rdf.gz"
    with gzip.open(path, "wb") as handle:
        handle.write(ET.tostring(root))
    return path


def test_whole_carriers_only_and_source_names(tmp_path):
    assert list(rhea_component_terms(write_source(tmp_path, source()))) == [
        ("RHEA-COMP:41", "oxidized carrier", []),
        ("RHEA-COMP:42", "reduced carrier", []),
    ]


@pytest.mark.parametrize("problem", [
    "foreign-uri", "reactive-part-uri", "wrong-id", "wrong-accession",
    "missing-name", "conflicting-names", "duplicate-subject",
])
def test_ambiguous_carriers_fail_closed(tmp_path, problem):
    root = source()
    node = root[0]
    if problem == "foreign-uri":
        node.set(RDF + "about", "https://other.org/Compound_41")
    elif problem == "reactive-part-uri":
        node.set(RDF + "about", "http://rdf.rhea-db.org/Compound_41_rp1")
    elif problem == "wrong-id":
        node.find(RH + "id").text = "42"
    elif problem == "wrong-accession":
        node.find(RH + "accession").text = "CHEBI:41"
    elif problem == "missing-name":
        node.remove(node.find(RH + "name"))
    elif problem == "conflicting-names":
        ET.SubElement(node, RH + "name").text = "other carrier"
    elif problem == "duplicate-subject":
        root.append(ET.fromstring(ET.tostring(node)))
    with pytest.raises(ValueError):
        list(rhea_component_terms(write_source(tmp_path, root)))


def test_snapshot_preserves_authority_and_requires_every_carrier(tmp_path):
    artifact = write_source(tmp_path, source())
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([{
        "key": "rhea-test", "kind": "rhea-components-rdf-gz", "path": artifact.name,
        "url": "https://example.org/rhea.rdf.gz", "version": "test", "license": "CC-BY",
        "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
    }]))
    records = tmp_path / "records"
    records.mkdir()
    record_path = records / "test.yaml"
    record = {"id": "GO:1", "participants": [{"id": "RHEA-COMP:41", "label": "invented"}]}
    record_path.write_text(yaml.safe_dump(record))
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"] == {"RHEA-COMP:41": {
        "label": "oxidized carrier", "synonyms": [], "source": "rhea-test",
    }}
    record["participants"].append({"id": "RHEA-COMP:43", "label": "unverified"})
    record_path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="unresolved source identifiers: RHEA-COMP:43"):
        build_snapshot(manifest, records, tmp_path)
