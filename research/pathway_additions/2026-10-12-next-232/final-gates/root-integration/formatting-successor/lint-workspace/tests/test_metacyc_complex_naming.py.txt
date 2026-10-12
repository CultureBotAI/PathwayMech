"""Native complex enzyme names require a single, identity-checked relation."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest

from scripts.build_source_identifier_snapshot import build_snapshot, source_terms

URL = "https://example.org/getxml?id=META:CPLX-1"
NAME = "N-acetylneuraminate lyase"
NATIVE = """<?xml version="1.0" encoding="iso-8859-1"?>
<ptools-xml xml:base="http://example.org:443/getxml?META:CPLX-1">
<metadata><url>http://example.org:443/</url><service_name>getxml</service_name>
<query>META:CPLX-1</query><num_results>1</num_results>
<PGDB orgid="META" version="27.0"><species datatype="string">MetaCyc</species></PGDB>
</metadata><Protein ID="META:CPLX-1" orgid="META" frameid="CPLX-1" detail="full">
<parent><Protein resource="getxml?META:Protein-Complexes" orgid="META"
frameid="Protein-Complexes" class="true"/></parent>
<component><Protein resource="getxml?META:MONOMER-1" orgid="META" frameid="MONOMER-1"/>
<coefficient datatype="integer">4</coefficient>
<citation>native component evidence</citation></component>
<catalyzes><Enzymatic-Reaction ID="META:ENZRXN-1" orgid="META" frameid="ENZRXN-1" detail="low">
<common-name datatype="string">&lt;i&gt;N&lt;/i&gt;-acetylneuraminate lyase</common-name>
<enzyme><Protein resource="#META:CPLX-1" orgid="META" frameid="CPLX-1"/></enzyme>
<reaction><Reaction resource="getxml?META:RXN-1" orgid="META" frameid="RXN-1"/></reaction>
<synonym datatype="string">Do not import activity aliases</synonym>
</Enzymatic-Reaction></catalyzes>
<credits><Person><common-name>Not a protein</common-name></Person></credits>
<species><Organism><common-name>Not the enzyme name</common-name></Organism></species>
<synonym datatype="string">Do not import protein aliases</synonym>
</Protein></ptools-xml>"""
ACTIVITY = "Protein/catalyzes/Enzymatic-Reaction"


def root():
    return ET.fromstring(NATIVE.encode("iso-8859-1"))


def parse(tmp_path, document=None, *, url=URL, version="27.0"):
    path = tmp_path / "source.xml"
    raw = NATIVE.encode("iso-8859-1") if document is None else ET.tostring(document)
    path.write_bytes(raw)
    result = list(source_terms("metacyc-protein-xml", path, url=url, version=version))
    assert path.read_bytes() == raw
    return result


def test_single_exact_linked_activity_names_complex_without_borrowed_aliases(tmp_path):
    assert parse(tmp_path) == [("MetaCyc:CPLX-1", NAME, [])]


@pytest.mark.parametrize("detail", ["low", "full"])
@pytest.mark.parametrize("coefficient", ["2", "4", "6"])
def test_native_homomer_coefficients_and_resolved_activity_details(tmp_path, detail, coefficient):
    document = root()
    document.find(ACTIVITY).set("detail", detail)
    document.find("Protein/component/coefficient").text = coefficient
    assert parse(tmp_path, document) == [("MetaCyc:CPLX-1", NAME, [])]


@pytest.mark.parametrize("path", [
    "Protein/parent", "Protein/parent/Protein", "Protein/component",
    "Protein/component/Protein", "Protein/component/coefficient", "Protein/catalyzes",
    ACTIVITY, ACTIVITY + "/enzyme", ACTIVITY + "/enzyme/Protein",
    ACTIVITY + "/reaction", ACTIVITY + "/reaction/Reaction", ACTIVITY + "/common-name",
])
@pytest.mark.parametrize("operation", ["missing", "duplicate"])
def test_every_required_relation_is_single_and_present(tmp_path, path, operation):
    document = root()
    parent_path, _, tag = path.rpartition("/")
    parent = document.find(parent_path)
    node = parent.find(tag)
    if operation == "missing":
        parent.remove(node)
    else:
        parent.append(copy.deepcopy(node))
    with pytest.raises(ValueError):
        parse(tmp_path, document)


@pytest.mark.parametrize(("path", "attribute", "value"), [
    ("Protein/parent/Protein", "class", "false"),
    ("Protein/parent/Protein", "frameid", "Polypeptides"),
    ("Protein/component/Protein", "orgid", "ECOLI"),
    ("Protein/component/Protein", "resource", "getxml?META:OTHER-MONOMER"),
    ("Protein/component/Protein", "ID", "META:MONOMER-1"),
    ("Protein/component/coefficient", "datatype", "float"),
    (ACTIVITY, "orgid", "ECOLI"),
    (ACTIVITY, "ID", "META:ENZRXN-2"),
    (ACTIVITY, "frameid", ""),
    (ACTIVITY, "detail", "minimal"),
    (ACTIVITY, "resource", "getxml?META:ENZRXN-1"),
    (ACTIVITY, "class", "true"),
    (ACTIVITY + "/enzyme/Protein", "orgid", "ECOLI"),
    (ACTIVITY + "/enzyme/Protein", "frameid", "MONOMER-1"),
    (ACTIVITY + "/enzyme/Protein", "resource", "#META:OTHER-CPLX"),
    (ACTIVITY + "/enzyme/Protein", "ID", "META:CPLX-1"),
    (ACTIVITY + "/reaction/Reaction", "orgid", "ECOLI"),
    (ACTIVITY + "/reaction/Reaction", "frameid", ""),
    (ACTIVITY + "/reaction/Reaction", "resource", "getxml?META:RXN-2"),
    (ACTIVITY + "/common-name", "datatype", "symbol"),
    (ACTIVITY + "/common-name", "resource", "getxml?META:NAME-1"),
])
def test_native_identity_cannot_be_inferred_from_labels(tmp_path, path, attribute, value):
    document = root()
    document.find(path).set(attribute, value)
    with pytest.raises(ValueError):
        parse(tmp_path, document)


@pytest.mark.parametrize("coefficient", ["", "0", "1", "-2", "+2", "2.0", "two"])
def test_fallback_requires_explicit_integer_assembly_coefficient(tmp_path, coefficient):
    document = root()
    document.find("Protein/component/coefficient").text = coefficient
    with pytest.raises(ValueError):
        parse(tmp_path, document)


def test_complex_cannot_be_its_own_component(tmp_path):
    document = root()
    subunit = document.find("Protein/component/Protein")
    subunit.set("frameid", "CPLX-1")
    subunit.set("resource", "getxml?META:CPLX-1")
    with pytest.raises(ValueError, match="invalid component frame"):
        parse(tmp_path, document)


@pytest.mark.parametrize("path", [
    "Protein/parent/Protein", "Protein/component/Protein",
    ACTIVITY + "/enzyme/Protein", ACTIVITY + "/reaction/Reaction",
])
@pytest.mark.parametrize("nested", [False, True])
def test_native_references_must_be_empty(tmp_path, path, nested):
    document = root()
    node = document.find(path)
    if nested:
        ET.SubElement(node, "common-name").text = NAME
    else:
        node.text = NAME
    with pytest.raises(ValueError):
        parse(tmp_path, document)


@pytest.mark.parametrize("name", [
    "", " ", "CPLX-1", "META:CPLX-1", "MetaCyc:CPLX-1", "ENZRXN-1",
    "META:ENZRXN-1", "MetaCyc:ENZRXN-1", "Unknown enzyme", "Not found",
    "<script>enzyme</script>", "<i>unfinished", "<i title='x'>enzyme</i>",
    "enzyme &notknown;", "enzyme &#-1;", "enzyme &#xFFFF;", "enzyme &amp;#946;",
])
def test_activity_name_uses_same_safe_decoder_and_rejects_identity_placeholders(tmp_path, name):
    document = root()
    document.find(ACTIVITY + "/common-name").text = name
    with pytest.raises(ValueError):
        parse(tmp_path, document)


@pytest.mark.parametrize(("name", "label"), [
    ("<i>N</i>-acetylneuraminate lyase", NAME),
    (" café  &beta;-enzyme ", "café β-enzyme"),
    ("enzyme &#x3B2;", "enzyme β"),
])
def test_native_activity_presentation_decodes_without_changing_identity(tmp_path, name, label):
    document = root()
    document.find(ACTIVITY + "/common-name").text = name
    assert parse(tmp_path, document) == [("MetaCyc:CPLX-1", label, [])]


def test_direct_name_precedes_even_invalid_activity_relation(tmp_path):
    document = root()
    ET.SubElement(document.find("Protein"), "common-name", datatype="string").text = "Direct name"
    document.find(ACTIVITY + "/enzyme/Protein").set("orgid", "ECOLI")
    assert parse(tmp_path, document) == [("MetaCyc:CPLX-1", "Direct name", [])]


@pytest.mark.parametrize("problem", ["blank", "duplicate", "datatype", "nested", "markup"])
def test_bad_direct_name_never_uses_otherwise_valid_activity(tmp_path, problem):
    document = root()
    protein = document.find("Protein")
    node = ET.SubElement(protein, "common-name", datatype="string")
    node.text = "Direct name"
    if problem == "blank":
        node.text = " "
    elif problem == "duplicate":
        protein.append(copy.deepcopy(node))
    elif problem == "datatype":
        node.set("datatype", "symbol")
    elif problem == "nested":
        ET.SubElement(node, "name").text = "Direct name"
    else:
        node.text = "<script>Direct name</script>"
    with pytest.raises(ValueError):
        parse(tmp_path, document)


def source_entry(tmp_path, filename, document):
    path = tmp_path / filename
    path.write_bytes(ET.tostring(document))
    return {"key": filename, "kind": "metacyc-protein-xml", "path": filename,
            "url": URL, "version": "27.0", "license": "synthetic fixture",
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


@pytest.mark.parametrize("reverse", [False, True])
def test_fallback_and_direct_name_conflict_still_fails_before_selection(tmp_path, reverse):
    entries = [source_entry(tmp_path, "derived.xml", root())]
    direct = root()
    node = ET.SubElement(direct.find("Protein"), "common-name", datatype="string")
    node.text = "Conflicting name"
    entries.append(source_entry(tmp_path, "direct.xml", direct))
    if reverse:
        entries.reverse()
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "records"
    records.mkdir()
    (records / "record.yaml").write_text("id: MetaCyc:OTHER-PWY\n")
    with pytest.raises(ValueError, match="conflicting MetaCyc protein native names"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("existing_output", [False, True])
@pytest.mark.parametrize("problem", ["none", "wrong-backref", "later-bad-source", "bad-direct"])
def test_real_cli_success_and_failure_preserve_the_output_contract(
    tmp_path, existing_output, problem,
):
    document = root()
    if problem == "wrong-backref":
        document.find(ACTIVITY + "/enzyme/Protein").set("resource", "#META:OTHER-CPLX")
    if problem == "bad-direct":
        ET.SubElement(document.find("Protein"), "common-name", datatype="string").text = " "
    entries = [source_entry(tmp_path, "source.xml", document)]
    if problem == "later-bad-source":
        bad = root()
        bad.find("Protein/component/coefficient").text = "1"
        entries.append(source_entry(tmp_path, "bad.xml", bad))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "records"
    records.mkdir()
    (records / "record.yaml").write_text("id: MetaCyc:CPLX-1\nlabel: Curated invention\n")
    output = tmp_path / "authority.json"
    sentinel = b"previous reviewed authority\n"
    if existing_output:
        output.write_bytes(sentinel)
    builder = Path(__file__).resolve().parents[1] / "scripts/build_source_identifier_snapshot.py"
    result = subprocess.run([
        sys.executable, "-B", str(builder), "--manifest", str(manifest),
        "--records", str(records), "--cache-dir", str(tmp_path), "--output", str(output),
    ], capture_output=True, text=True, check=False)
    if problem == "none":
        assert result.returncode == 0, result.stderr
        snapshot = json.loads(output.read_bytes())
        assert snapshot["terms"] == {
            "MetaCyc:CPLX-1": {"label": NAME, "synonyms": [], "source": "source.xml"},
        }
        assert snapshot["sources"]["source.xml"]["sha256"] == entries[0]["sha256"]
        assert "Curated invention" not in output.read_text()
    else:
        assert result.returncode != 0
        assert "ValueError: MetaCyc" in result.stderr
        assert "Retained" not in result.stdout
        if existing_output:
            assert output.read_bytes() == sentinel
        else:
            assert not output.exists()
