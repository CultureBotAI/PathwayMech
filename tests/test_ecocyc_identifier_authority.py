"""Native EcoCyc identity boundaries; fixtures do not establish pathway biology."""
from __future__ import annotations

import copy
import hashlib
import io
import json
import os
import subprocess
import sys
import tarfile
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.cli import _record_page, _reference_url
from pathwaymech.graph_view import _declared_nodes
from pathwaymech.identifiers import identifier_errors
from pathwaymech.kgx import kgx_nodes
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.strict import TARGET_CLASS, validator
from scripts.build_source_identifier_snapshot import build_snapshot, source_terms

HOST = "bf2i-artsymbiocyc.insa-lyon.fr"
FRAME = "CPLX0-226"
URL = f"https://{HOST}/getxml?id=ECOLI:{FRAME}"
LABEL = "CRP-cyclic-AMP DNA-binding transcriptional dual regulator"
VERSION = "27.0"
KIND = "ecocyc-protein-xml"
NATIVE = f'''<?xml version="1.0" encoding="iso-8859-1"?>
<ptools-xml ptools-version="27.0" xml:base="http://{HOST}:443/getxml?ECOLI:{FRAME}">
<metadata><url>http://{HOST}:443/</url><service_name>getxml</service_name>
<query>ECOLI:{FRAME}</query><num_results>1</num_results>
<PGDB orgid="ECOLI" version="27.0"><species datatype="string">Escherichia coli</species>
<strain datatype="string">K-12 substr. MG1655</strain><dblink>
<dblink-db>NCBI-TAXONOMY-DB</dblink-db><dblink-oid>511145</dblink-oid>
<dblink-relationship>unification</dblink-relationship>
<dblink-URL>http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=511145</dblink-URL>
</dblink></PGDB></metadata>
<Protein ID="ECOLI:{FRAME}" orgid="ECOLI" frameid="{FRAME}" detail="full">
<parent><Protein resource="getxml?ECOLI:Protein-Small-Molecule-Complexes" orgid="ECOLI"
frameid="Protein-Small-Molecule-Complexes" class="true"/></parent>
<common-name datatype="string">{LABEL}</common-name><synonym datatype="string">CRP-cAMP</synonym>
<component><Protein resource="getxml?ECOLI:PC00004" orgid="ECOLI" frameid="PC00004"/></component>
<component><Compound resource="getxml?ECOLI:CAMP" orgid="ECOLI" frameid="CAMP"/></component>
</Protein></ptools-xml>'''


def native():
    return ET.fromstring(NATIVE)


def parse(tmp_path, document=None, *, url=URL, version=VERSION, kind=KIND):
    path = tmp_path / "source.xml"
    if document is None:
        document = native()
    if isinstance(document, ET.Element):
        document = ET.tostring(document, encoding="utf-8", xml_declaration=True)
    elif isinstance(document, str):
        document = document.encode("iso-8859-1")
    path.write_bytes(document)
    return list(source_terms(kind, path, url=url, version=version))


def test_direct_native_name_and_only_direct_synonym(tmp_path):
    tree = native()
    nested = ET.SubElement(tree.find("Protein"), "nested")
    ET.SubElement(nested, "common-name", datatype="string").text = "Nested object, not an alias"
    ET.SubElement(nested, "synonym", datatype="string").text = "Nested alias"
    assert parse(tmp_path, tree) == [("EcoCyc:" + FRAME, LABEL, ["CRP-cAMP"])]


@pytest.mark.parametrize("frame,tag,parent,label,synonyms,kind", [
    ("CPLX0-226", "Protein", "Protein-Small-Molecule-Complexes", LABEL, ["CRP-cAMP"], KIND),
    ("PC00004", "Protein", "Protein-Complexes", "DNA-binding transcriptional dual regulator CRP",
     ["CRP"], KIND),
    ("RNA0-241", "RNA", "Regulatory-RNAs", "small regulatory RNA SgrS", ["SgrS", "RyaA"],
     "ecocyc-rna-xml"),
])
def test_three_native_shapes(tmp_path, frame, tag, parent, label, synonyms, kind):
    text = NATIVE.replace(FRAME, frame).replace("Protein-Small-Molecule-Complexes", parent)
    tree = ET.fromstring(text)
    entity = tree.find("Protein")
    entity.tag = tag
    entity.find("parent/Protein").tag = tag
    entity.find("common-name").text = label
    for node in entity.findall("synonym"):
        entity.remove(node)
    for alias in synonyms:
        ET.SubElement(entity, "synonym", datatype="string").text = alias
    assert parse(tmp_path, tree, url=URL.replace(FRAME, frame), kind=kind) == [
        ("EcoCyc:" + frame, label, sorted(synonyms))]


@pytest.mark.parametrize("path,key,value", [
    (".", "ptools-version", "28.0"),
    ("metadata/PGDB", "orgid", "META"),
    ("metadata/PGDB", "version", "28.0"),
    ("metadata/PGDB/species", "datatype", "integer"),
    ("metadata/PGDB/strain", "datatype", "symbol"),
    ("Protein", "ID", "ECOLI:PC00004"),
    ("Protein", "orgid", "META"),
    ("Protein", "frameid", "PC00004"),
    ("Protein", "detail", "low"),
    ("Protein", "class", "true"),
    ("Protein", "resource", "getxml?ECOLI:CPLX0-226"),
    ("Protein/parent/Protein", "orgid", "META"),
    ("Protein/parent/Protein", "frameid", "Polypeptides"),
    ("Protein/parent/Protein", "resource", "getxml?META:Protein-Small-Molecule-Complexes"),
    ("Protein/parent/Protein", "class", "false"),
    ("Protein/common-name", "datatype", "symbol"),
    ("Protein/common-name", "extra", "untrusted"),
    ("Protein/synonym", "datatype", "symbol"),
])
def test_attribute_identity_and_type_failures(tmp_path, path, key, value):
    tree = native()
    tree.find(path).set(key, value)
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, tree)


@pytest.mark.parametrize("path,value", [
    ("metadata/service_name", "other"), ("metadata/query", "META:CPLX0-226"),
    ("metadata/query", "ECOLI:PC00004"), ("metadata/num_results", "2"),
    ("metadata/PGDB/species", "Salmonella enterica"),
    ("metadata/PGDB/strain", "K-12"), ("metadata/PGDB/dblink/dblink-db", "OTHER"),
    ("metadata/PGDB/dblink/dblink-oid", "562"),
    ("metadata/PGDB/dblink/dblink-relationship", "related"),
    ("metadata/PGDB/dblink/dblink-URL", "https://example.org/511145"),
    ("metadata/url", f"http://{HOST}/"),
    ("metadata/url", f"https://{HOST}:443/"),
    ("metadata/url", "https://example.org/"),
    ("metadata/url", f"http://{HOST}:80/"),
])
def test_metadata_identity_failures(tmp_path, path, value):
    tree = native()
    tree.find(path).text = value
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, tree)


@pytest.mark.parametrize("path", ["metadata", "metadata/PGDB", "metadata/query",
    "metadata/PGDB/species", "metadata/PGDB/strain", "metadata/PGDB/dblink",
    "metadata/PGDB/dblink/dblink-oid", "Protein", "Protein/parent", "Protein/common-name",
    "Protein/synonym"])
@pytest.mark.parametrize("mode", ["duplicate", "remove"])
def test_missing_and_duplicate_identity_slots(tmp_path, path, mode):
    if path == "Protein/synonym" and mode == "remove":
        # Aliases are optional; malformed aliases are never silently discarded.
        tree = native()
        tree.find("Protein").remove(tree.find(path))
        assert parse(tmp_path, tree)[0][2] == []
        return
    tree = native()
    owner = tree.find(path.rsplit("/", 1)[0]) if "/" in path else tree
    node = tree.find(path)
    owner.append(copy.deepcopy(node)) if mode == "duplicate" else owner.remove(node)
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, tree)


@pytest.mark.parametrize("url", [URL.replace("https:", "http:"), URL + "#fragment", URL + "&x=1",
    URL + "&id=ECOLI:CPLX0-226", URL.replace(HOST, "example.org"),
    URL.replace(HOST, "user@" + HOST), URL.replace(HOST, HOST + ":443"),
    URL.replace("ECOLI:", "META:"), URL.replace("ECOLI:", "ECOLI%3A"),
    URL.replace("getxml", "gene"), URL + "\n", URL + "&detail=full", None])
def test_issuing_request_is_exact(tmp_path, url):
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, url=url)


@pytest.mark.parametrize("base", [f"http://{HOST}/getxml?ECOLI:{FRAME}",
    f"http://{HOST}:80/getxml?ECOLI:{FRAME}", f"http://{HOST}:443/getxml?ECOLI:OTHER",
    f"http://{HOST}:443/getxml?id=ECOLI:{FRAME}", URL + "#fragment",
    URL.replace(HOST, "example.org"), URL.replace(FRAME, "OTHER")])
def test_serialized_base_does_not_relax_transport(tmp_path, base):
    tree = native()
    tree.set("{http://www.w3.org/XML/1998/namespace}base", base)
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, tree)


def test_exact_https_metadata_also_matches(tmp_path):
    tree = native()
    tree.set("{http://www.w3.org/XML/1998/namespace}base", URL)
    tree.find("metadata/url").text = f"https://{HOST}/"
    assert parse(tmp_path, tree)[0][0] == "EcoCyc:" + FRAME


@pytest.mark.parametrize("value", ["", " ", FRAME, "ECOLI:" + FRAME, "EcoCyc:" + FRAME,
    "Unknown", "Not found", "Error page", "<script>bad</script>", "<i>unfinished",
    "<i title='bad'>x</i>", "x&not-an-entity;", "x<!--comment-->", "x<?pi?>",
    "&#0;", "&#10;", "&#xD800;", "&#1114112;", "&amp;lt;bad&amp;gt;", "x\tbad"])
@pytest.mark.parametrize("slot", ["common-name", "synonym"])
def test_unresolved_or_unsafe_names_and_aliases_fail(tmp_path, value, slot):
    tree = native()
    tree.find("Protein/" + slot).text = value
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, tree)


@pytest.mark.parametrize("slot", ["common-name", "synonym"])
def test_nested_name_is_not_a_native_string(tmp_path, slot):
    tree = native()
    ET.SubElement(tree.find("Protein/" + slot), "b").text = "Not native string"
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, tree)


@pytest.mark.parametrize("tag", ["Gene", "RNA", "Compound"])
def test_wrong_top_level_type_fails(tmp_path, tag):
    tree = native()
    tree.find("Protein").tag = tag
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, tree)


@pytest.mark.parametrize("version", [None, "", "27.0 ", "27", "28.0", "release 27.0"])
def test_version_must_match_native_metadata(tmp_path, version):
    with pytest.raises(ValueError, match="EcoCyc"):
        parse(tmp_path, version=version)


@pytest.mark.parametrize("encoding", ["utf-8", "utf-16"])
def test_dtd_entity_rejected_during_parsing(tmp_path, encoding):
    body = NATIVE[NATIVE.index("<ptools-xml"):]
    body = ('<?xml version="1.0" encoding="' + encoding + '"?>'
            '<!DOCTYPE ptools-xml [<!ENTITY poison "substitute">]>' + body)
    with pytest.raises(ValueError, match="DOCTYPE"):
        parse(tmp_path, body.encode(encoding))


def entry(tmp_path, filename="source.xml", tree=None, **overrides):
    source = tmp_path / filename
    source.write_bytes(ET.tostring(tree if tree is not None else native()))
    return {"key": filename, "kind": KIND, "path": filename, "url": URL,
            "version": VERSION, "license": "Fixture only",
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(), **overrides}


def fixture(tmp_path, entries=None, *, selected=True):
    records = tmp_path / "records"
    records.mkdir()
    (records / "ids.yaml").write_text(yaml.safe_dump({"id": "EcoCyc:" +
        (FRAME if selected else "UNSELECTED")}))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries or [entry(tmp_path)]))
    return manifest, records


@pytest.mark.parametrize("change", ["name", "alias", "parent", "kind", "version"])
@pytest.mark.parametrize("selected", [True, False])
def test_conflicting_source_identity_fails_before_filter(tmp_path, change, selected):
    tree = native()
    overrides = {}
    if change == "name":
        tree.find("Protein/common-name").text = "Different native name"
    elif change == "alias":
        tree.find("Protein/synonym").text = "Different native alias"
    elif change == "parent":
        parent = tree.find("Protein/parent/Protein")
        parent.set("frameid", "Protein-Complexes")
        parent.set("resource", "getxml?ECOLI:Protein-Complexes")
    elif change == "kind":
        tree.find("Protein").tag = "RNA"
        parent = tree.find("RNA/parent/Protein")
        parent.tag = "RNA"
        parent.set("frameid", "Regulatory-RNAs")
        parent.set("resource", "getxml?ECOLI:Regulatory-RNAs")
        overrides["kind"] = "ecocyc-rna-xml"
    else:
        tree.set("ptools-version", "28.0")
        tree.find("metadata/PGDB").set("version", "28.0")
        overrides["version"] = "28.0"
    entries = [entry(tmp_path), entry(tmp_path, "other.xml", tree, **overrides)]
    manifest, records = fixture(tmp_path, entries, selected=selected)
    with pytest.raises(ValueError, match="conflicting EcoCyc native identity"):
        build_snapshot(manifest, records, tmp_path)


def test_conflicting_releases_of_distinct_ids_fail_before_filter(tmp_path):
    tree = ET.fromstring(NATIVE.replace(FRAME, "OTHER").replace("27.0", "28.0"))
    entries = [entry(tmp_path), entry(tmp_path, "other.xml", tree,
        url=URL.replace(FRAME, "OTHER"), version="28.0")]
    manifest, records = fixture(tmp_path, entries, selected=False)
    with pytest.raises(ValueError, match="conflicting EcoCyc native PGDB versions"):
        build_snapshot(manifest, records, tmp_path)


def test_duplicate_agreement_preserves_whole_first_source_assertion(tmp_path):
    entries = [entry(tmp_path), entry(tmp_path, "other.xml")]
    manifest, records = fixture(tmp_path, entries)
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"] == {"EcoCyc:" + FRAME: {
        "label": LABEL, "synonyms": ["CRP-cAMP"], "source": "source.xml"}}
    assert set(result["sources"]) == {"source.xml"}


def test_non_native_source_cannot_issue_ecocyc_terms(tmp_path):
    archive = tmp_path / "gocam.tar.gz"
    body = json.dumps({"id": "EcoCyc:" + FRAME, "annotations": [
        {"key": "title", "value": LABEL}]}).encode()
    with tarfile.open(archive, "w:gz") as stream:
        member = tarfile.TarInfo("model.json")
        member.size = len(body)
        stream.addfile(member, io.BytesIO(body))
    entries = [{"key": "gocam", "kind": "gocam-tar", "path": archive.name,
        "url": "https://model.geneontology.org/fixture", "version": "fixture",
        "license": "Fixture", "sha256": hashlib.sha256(archive.read_bytes()).hexdigest()}]
    manifest, records = fixture(tmp_path, entries, selected=False)
    with pytest.raises(ValueError, match="EcoCyc identifiers require native ECOLI XML"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("exists", [True, False])
def test_real_cli_failure_leaves_output_unchanged(tmp_path, exists):
    tree = native()
    tree.find("metadata/PGDB/dblink/dblink-oid").text = "562"
    manifest, records = fixture(tmp_path, [entry(tmp_path, tree=tree)])
    output = tmp_path / "output.json"
    if exists:
        output.write_bytes(b"previous verified snapshot\n")
    result = subprocess.run([sys.executable, "-B", "scripts/build_source_identifier_snapshot.py",
        "--manifest", str(manifest), "--cache-dir", str(tmp_path), "--records", str(records),
        "--output", str(output)], capture_output=True, text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    assert result.returncode != 0 and "EcoCyc native taxon mismatch" in result.stderr
    assert output.read_bytes() == b"previous verified snapshot\n" if exists else not output.exists()


@pytest.mark.parametrize("problem,code", [(None, None), ("alias", None),
    ("invented", "LABEL_MISMATCH"), ("missing", "ID_NOT_FOUND"),
    ("context", "LABEL_AUTHORITY_UNAVAILABLE")])
def test_policy_accepts_only_verified_native_names_and_aliases(tmp_path, problem, code):
    manifest, records = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    record = {"id": "EcoCyc:" + FRAME, "label": LABEL,
              "taxa": [], "participants": [], "reactions": []}
    if problem == "alias":
        record["label"] = "CRP-cAMP"
    elif problem == "invented":
        record["label"] = "Curator state invention"
    elif problem == "missing":
        record["id"] = "EcoCyc:MISSING"
    elif problem == "context":
        snapshot["terms"][record["id"]]["label_kind"] = "source_context"
    record_dir = tmp_path / "data/pathways"
    record_dir.mkdir(parents=True)
    (record_dir / "record.yaml").write_text(yaml.safe_dump(record))
    policy = yaml.safe_load(Path("conf/identifier_policy.yaml").read_text())
    assert policy["namespaces"]["EcoCyc"]["policy"] == "canonical_or_synonym"
    assert not any(row["namespace"] == "EcoCyc" for row in policy["contextual_labels"])
    policy["namespaces"] = {"EcoCyc": policy["namespaces"]["EcoCyc"]}
    policy["contextual_labels"] = []
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data/identifier_authorities/sources.json"
    authority.parent.mkdir()
    authority.write_text(json.dumps(snapshot))
    errors = identifier_errors(tmp_path)
    assert any(code in error for error in errors) if code else errors == []


@pytest.fixture(scope="module")
def checker():
    return validator()


def software_record():
    return {"id": "MetaCyc:TEST", "label": "Software test fixture", "taxa": [],
        "description": "Synthetic software fixture, not a biological claim.",
        "pathway_type": "test", "reactions": [],
        "participants": [
            {"id": "EcoCyc:RNA0-241", "label": "SgrS", "category": "rna"},
            {"id": "EcoCyc:CPLX0-226", "label": "CRP-cAMP", "category": "complex"},
            {"id": "EcoCyc:PC00004", "label": "CRP", "category": "complex"}],
        "references": [{"id": "EcoCyc:RNA0-241", "title": "Native source"}],
        "mechanistic_edges": [{"id": "test-edge", "subject": "EcoCyc:RNA0-241",
            "predicate": "regulates",
            "object": "EcoCyc:PC00004", "evidence": [{"reference_id": "EcoCyc:RNA0-241",
                "source_assertion": "Synthetic software fixture; no biological assertion.",
                "source_locator": "Software fixture"}]}]}


@pytest.mark.parametrize("prefix", ["EcoCyc", "ECOLI", "ECocyc", "ecocyc"])
def test_exact_namespace_schema_parity(checker, prefix):
    raw = software_record()
    raw["participants"][0]["id"] = prefix + ":RNA0-241"
    raw["mechanistic_edges"][0]["subject"] = prefix + ":RNA0-241"
    if prefix == "EcoCyc":
        validate_record(raw)
        assert not checker.validate(raw, TARGET_CLASS).results
    else:
        with pytest.raises(ValidationError, match="unsupported prefix"):
            validate_record(raw)
        assert checker.validate(raw, TARGET_CLASS).results


def test_explicit_rna_complex_categories_and_public_citations():
    raw = software_record()
    model = validate_record(raw)
    nodes = {n.id: n for n in kgx_nodes([model])}
    assert nodes["EcoCyc:RNA0-241"].category == "biolink:RNAProduct"
    for frame in ("CPLX0-226", "PC00004"):
        assert nodes["EcoCyc:" + frame].category == "biolink:MacromolecularComplex"
    graph = _declared_nodes(model, {})
    assert graph["EcoCyc:RNA0-241"]["type_label"] == "rna"
    assert graph["EcoCyc:CPLX0-226"]["type_label"] == "complex"
    assert 'https://ecocyc.org/gene?id=RNA0-241' in _record_page(model)
    for node in raw["participants"]:
        del node["category"]
    assert all(n.category == "biolink:NamedThing" for n in kgx_nodes([validate_record(raw)])
               if n.id.startswith("EcoCyc:"))


@pytest.mark.parametrize("frame", ["CPLX0-226", "PC00004", "RNA0-241"])
def test_public_citation_route(frame):
    assert _reference_url("EcoCyc:" + frame) == "https://ecocyc.org/gene?id=" + frame


@pytest.mark.parametrize("identifier", ["EcoCyc:X&other=true", "EcoCyc:X#fragment",
    "EcoCyc:X/path", "EcoCyc:", "ECOLI:RNA0-241", "ecocyc:RNA0-241"])
def test_citation_route_does_not_accept_untrusted_local_values(identifier):
    assert _reference_url(identifier) is None
