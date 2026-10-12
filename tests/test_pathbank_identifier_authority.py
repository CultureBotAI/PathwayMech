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


DOWNLOAD = "https://pathbank.org/view/SMP9999999/download?type=owl_markup"


def add_stub(root, accession="SMP9999998"):
    primary = root.find(BP + "Pathway")
    uri = "http://identifiers.org/smpdb/" + accession
    stub = ET.SubElement(root, BP + "Pathway", {RDF + "about": uri})
    ET.SubElement(stub, BP + "displayName").text = "Adjacent native pathway"
    ET.SubElement(stub, BP + "name").text = "SubPathway"
    ET.SubElement(stub, BP + "xref", {RDF + "resource": "#xref-" + accession})
    xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "xref-" + accession})
    ET.SubElement(xref, BP + "db").text = "SMPDB"
    ET.SubElement(xref, BP + "id").text = accession
    interaction_id = "SubPathwayInteractions/" + accession
    ET.SubElement(stub, BP + "pathwayComponent", {RDF + "resource": "#" + interaction_id})
    interaction = ET.SubElement(root, BP + "Interaction", {RDF + "ID": interaction_id})
    ET.SubElement(interaction, BP + "participant", {RDF + "resource": "#Compound/native"})
    ET.SubElement(primary, BP + "pathwayComponent", {RDF + "resource": uri})
    return stub


@pytest.mark.parametrize("position", [0, 1, 2, 3])
def test_exact_requested_root_selected_independently_of_pathway_order(position):
    root = native_source()
    primary = root.find(BP + "Pathway")
    for accession in ["SMP9999998", "SMP9999997", "SMP9999996"]:
        add_stub(root, accession)
    root.remove(primary)
    root.insert(position, primary)
    terms = list(pathbank_terms(root, url=DOWNLOAD))
    assert terms[0] == (PATHWAY, "Native pathway title", [])
    children = {"PathBank:" + accession for accession in ["SMP9999998", "SMP9999997", "SMP9999996"]}
    assert all(
        identifier == PATHWAY or identifier in children or identifier.startswith(PATHWAY + "/")
        for identifier, _, _ in terms
    )
    assert {identifier for identifier, _, _ in terms if identifier in children} == children
    assert all(names == [] for identifier, _, names in terms if identifier in children)
    assert not any("SubPathwayInteractions" in identifier for identifier, _, _ in terms)


def test_transport_and_compartment_scopes_are_native_contexts(tmp_path):
    manifest, records, record, record_path = authority_fixture(tmp_path)
    root = native_source()
    add_stub(root)
    transport = ET.SubElement(root, BP + "Transport", {RDF + "ID": "Transports/505"})
    ET.SubElement(transport, BP + "displayName").text = "Transport505"
    ET.SubElement(root.find(BP + "Pathway"), BP + "pathwayComponent", {
        RDF + "resource": "#Transports/505",
    })
    native_ids = [
        f"Compound/{compound}_{compartment}"
        for compound, compartments in [
            ("adenine", ["Periplasmic_Space", "Cytosol"]),
            ("hydrogen", ["Periplasmic_Space", "Cytosol"]),
            ("IMP", ["Cytosol", "Cytoplasm"]),
        ] for compartment in compartments
    ]
    for native in native_ids:
        node = ET.SubElement(root, BP + "SmallMolecule", {RDF + "ID": native})
        ET.SubElement(node, BP + "displayName").text = "Same chemical name"
        record["participants"].append({"id": PATHWAY + "/" + native, "label": "Scoped instance"})
    record["reactions"].append({"id": PATHWAY + "/Transports/505", "label": "Native transport"})
    record_path.write_text(yaml.safe_dump(record))
    entries = json.loads(manifest.read_text())
    source = tmp_path / entries[0]["path"]
    source.write_bytes(ET.tostring(root))
    entries[0].update(url=DOWNLOAD, sha256=hashlib.sha256(source.read_bytes()).hexdigest())
    manifest.write_text(json.dumps(entries))
    result = build_snapshot(manifest, records, tmp_path)
    for native in [*native_ids, "Transports/505"]:
        assert result["terms"][PATHWAY + "/" + native]["label_kind"] == "source_context"
    assert result["terms"][PATHWAY + "/Transports/505"]["label"] == "Transport505"


@pytest.mark.parametrize("url", [
    DOWNLOAD.replace("https:", "http:"), DOWNLOAD.replace("pathbank.org", "elsewhere.org"),
    DOWNLOAD.replace("pathbank.org", "pathbank.org.example.com"),
    DOWNLOAD.replace("pathbank.org", "user@pathbank.org"),
    DOWNLOAD.replace("pathbank.org", "pathbank.org:443"), DOWNLOAD + "#fragment",
    DOWNLOAD + "&type=owl_markup", DOWNLOAD + "&extra=1", DOWNLOAD.replace("SMP9999999", "PW1"),
    DOWNLOAD.replace("SMP9999999", "SMP9999998"), DOWNLOAD.replace("owl_markup", "pwml_markup"),
    DOWNLOAD.replace("?type=owl_markup", ""), DOWNLOAD + " ",
])
def test_invalid_or_mismatched_native_download_request_fails(url):
    with pytest.raises(ValueError):
        list(pathbank_terms(native_source(), url=url))


@pytest.mark.parametrize("about", ["#local-pathway", "https://other.example/SMP9999999", ""])
def test_requested_definition_requires_its_issuing_native_uri(about):
    root = native_source()
    root.find(BP + "Pathway").set(RDF + "about", about)
    with pytest.raises(ValueError, match="PathBank"):
        list(pathbank_terms(root, url=DOWNLOAD))


@pytest.mark.parametrize("problem", [
    "unattached", "expanded", "wrong-xref", "missing-xref", "requested-stub",
    "dangling-step", "wrong-step-class", "duplicate-accession", "no-primary-definition",
])
def test_only_attached_verified_interface_stubs_are_supported(problem):
    root = native_source()
    primary = root.find(BP + "Pathway")
    stub = add_stub(root)
    if problem == "unattached":
        primary.remove(primary.findall(BP + "pathwayComponent")[-1])
    elif problem == "expanded":
        root.find(BP + "Interaction").tag = BP + "BiochemicalReaction"
    elif problem == "wrong-xref":
        root.findall(BP + "UnificationXref")[-1].find(BP + "id").text = "SMP9999997"
    elif problem == "missing-xref":
        stub.remove(stub.find(BP + "xref"))
    elif problem == "requested-stub":
        with pytest.raises(ValueError, match="primary"):
            list(pathbank_terms(root, url=DOWNLOAD.replace("SMP9999999", "SMP9999998")))
        return
    elif problem == "dangling-step":
        ET.SubElement(primary, BP + "pathwayOrder", {RDF + "resource": "#missing-step"})
    elif problem == "wrong-step-class":
        ET.SubElement(primary, BP + "pathwayOrder", {RDF + "resource": "#Reactions/7"})
    elif problem == "duplicate-accession":
        duplicate = copy.deepcopy(primary)
        duplicate.set(RDF + "about", "#different-subject")
        root.append(duplicate)
    elif problem == "no-primary-definition":
        primary.remove(primary.findall(BP + "pathwayComponent")[0])
    with pytest.raises(ValueError, match="PathBank"):
        list(pathbank_terms(root, url=DOWNLOAD))


def test_pathway_step_attachment_does_not_invent_an_interaction_authority():
    root = native_source()
    primary = root.find(BP + "Pathway")
    stub = add_stub(root)
    primary.remove(primary.findall(BP + "pathwayComponent")[-1])
    ET.SubElement(primary, BP + "pathwayOrder", {RDF + "resource": "#interface-step"})
    step = ET.SubElement(root, BP + "PathwayStep", {RDF + "ID": "interface-step"})
    ET.SubElement(step, BP + "stepProcess", {RDF + "resource": stub.get(RDF + "about")})
    terms = list(pathbank_terms(root, url=DOWNLOAD))
    assert ("PathBank:SMP9999998", "Adjacent native pathway", []) in terms
    assert [term for term in terms if term[0] != "PathBank:SMP9999998"] == list(
        pathbank_terms(native_source())
    )


@pytest.mark.parametrize("existing", [True, False])
def test_wrong_native_root_cannot_write_or_replace_output(tmp_path, monkeypatch, existing):
    manifest, records, _, _ = authority_fixture(tmp_path)
    entries = json.loads(manifest.read_text())
    entries[0]["url"] = DOWNLOAD.replace("SMP9999999", "SMP9999998")
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "output.json"
    if existing:
        output.write_bytes(b"prior authority\n")
    monkeypatch.setattr(sys, "argv", [
        "builder", "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(tmp_path), "--output", str(output),
    ])
    with pytest.raises(ValueError, match="PathBank"):
        main()
    assert output.read_bytes() == b"prior authority\n" if existing else not output.exists()


@pytest.mark.parametrize("problem", [
    "missing", "empty", "blank", "duplicate", "conflicting", "nested", "generic", "lower-generic",
])
def test_attached_child_requires_one_direct_biological_title(problem):
    root = native_source()
    stub = add_stub(root)
    name = stub.find(BP + "displayName")
    if problem == "missing":
        stub.remove(name)
    elif problem in {"empty", "blank", "generic", "lower-generic"}:
        name.text = {"empty": None, "blank": " \t", "generic": "SubPathway",
                     "lower-generic": "subpathway"}[problem]
    elif problem in {"duplicate", "conflicting"}:
        ET.SubElement(stub, BP + "displayName").text = (
            name.text if problem == "duplicate" else "Conflicting child"
        )
    else:
        ET.SubElement(name, "nested").text = "additional name"
    with pytest.raises(ValueError, match="PathBank attached pathway"):
        list(pathbank_terms(root, url=DOWNLOAD))


def child_fixture(tmp_path, *, second_name=None, separate_primary=False):
    manifest, records, record, path = authority_fixture(tmp_path)
    record["id"] = "PathBank:SMP9999998"
    record["label"] = "Adjacent native pathway"
    record["participants"] = []
    record["reactions"] = []
    path.write_text(yaml.safe_dump(record))
    entries = json.loads(manifest.read_text())
    root = native_source()
    add_stub(root)
    first = tmp_path / entries[0]["path"]
    first.write_bytes(ET.tostring(root))
    entries[0].update(url=DOWNLOAD, sha256=hashlib.sha256(first.read_bytes()).hexdigest())
    if second_name is not None:
        if separate_primary:
            root = native_source()
            root.find(BP + "Pathway").set(
                RDF + "about", "http://identifiers.org/smpdb/SMP9999998",
            )
            root.find(BP + "UnificationXref").find(BP + "id").text = "SMP9999998"
            root.find(BP + "Pathway").find(BP + "displayName").text = second_name
        else:
            root.findall(BP + "Pathway")[-1].find(BP + "displayName").text = second_name
        second = tmp_path / "second.owl"
        second.write_bytes(ET.tostring(root))
        entries.append({**entries[0], "key": "second", "path": second.name,
                        "url": DOWNLOAD.replace("SMP9999999", "SMP9999998")
                        if separate_primary else DOWNLOAD,
                        "sha256": hashlib.sha256(second.read_bytes()).hexdigest()})
    manifest.write_text(json.dumps(entries))
    return manifest, records, record, path, entries


def test_child_canonical_term_has_no_generic_alias_or_inferred_local_graph(tmp_path):
    manifest, records, _, _, _ = child_fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    assert snapshot["terms"] == {
        "PathBank:SMP9999998": {
            "label": "Adjacent native pathway", "synonyms": [], "source": "native",
        },
    }
    policy = yaml.safe_load(Path("conf/identifier_policy.yaml").read_text())
    policy["namespaces"] = {"PathBank": policy["namespaces"]["PathBank"]}
    policy["contextual_labels"] = [
        rule for rule in policy["contextual_labels"]
        if rule["namespace"] == "PathBank" and rule["record_prefixes"] == ["PathBank"]
    ]
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data/identifier_authorities/sources.json"
    authority.parent.mkdir()
    authority.write_text(json.dumps(snapshot))
    assert identifier_errors(tmp_path) == []
    path = records / "pathway.yaml"
    record = yaml.safe_load(path.read_text())
    record["label"] = "SubPathway"
    path.write_text(yaml.safe_dump(record))
    assert any("LABEL_MISMATCH" in error for error in identifier_errors(tmp_path))


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize("separate_primary", [True, False])
def test_child_name_conflicts_fail_before_selection_and_preserve_output(
    tmp_path, monkeypatch, selected, reverse, separate_primary,
):
    manifest, records, record, path, entries = child_fixture(
        tmp_path, second_name="Different title", separate_primary=separate_primary,
    )
    if not selected:
        record.update(id=PATHWAY, label="Native pathway title")
        path.write_text(yaml.safe_dump(record))
    if reverse:
        manifest.write_text(json.dumps(entries[::-1]))
    output = tmp_path / "output.json"
    previous = b"previous reviewed authority\n"
    output.write_bytes(previous)
    monkeypatch.setattr(sys, "argv", [
        "builder", "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(tmp_path), "--output", str(output),
    ])
    with pytest.raises(ValueError, match="conflicting PathBank native pathway names"):
        main()
    assert output.read_bytes() == previous


def test_agreeing_child_and_primary_names_keep_first_provenance(tmp_path):
    manifest, records, _, _, _ = child_fixture(
        tmp_path, second_name="Adjacent native pathway", separate_primary=True,
    )
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"]["PathBank:SMP9999998"] == {
        "label": "Adjacent native pathway", "synonyms": [], "source": "native",
    }
    assert set(result["sources"]) == {"native"}


@pytest.mark.parametrize("existing", [True, False])
def test_invalid_unselected_child_cannot_publish_selected_parent(tmp_path, monkeypatch, existing):
    manifest, records, record, path, entries = child_fixture(tmp_path)
    record.update(id=PATHWAY, label="Native pathway title")
    path.write_text(yaml.safe_dump(record))
    original = tmp_path / entries[0]["path"]
    root = ET.parse(original).getroot()
    root.findall(BP + "Pathway")[-1].find(BP + "displayName").text = " "
    original.write_bytes(ET.tostring(root))
    entries[0]["sha256"] = hashlib.sha256(original.read_bytes()).hexdigest()
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "output.json"
    if existing:
        output.write_bytes(b"prior authority\n")
    monkeypatch.setattr(sys, "argv", [
        "builder", "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(tmp_path), "--output", str(output),
    ])
    with pytest.raises(ValueError, match="PathBank attached pathway"):
        main()
    assert output.read_bytes() == b"prior authority\n" if existing else not output.exists()
