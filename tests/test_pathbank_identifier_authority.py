"""Synthetic native BioPAX authorities; production inputs remain external."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.identifiers import _load_authority, identifier_errors
from pathwaymech.pathbank_provenance import (
    PATHBANK_ARCHIVE_DEFAULT_PATH,
    PATHBANK_ARCHIVE_KIND,
    PATHBANK_ARCHIVE_LICENSE,
    PATHBANK_ARCHIVE_URL,
    PATHBANK_ARCHIVE_VERSION,
    audit_pathbank_archive_member_authority,
    build_pathbank_archive_manifest_entry,
    inspect_pathbank_archive_member,
    rank_pathbank_archive_member_candidates,
    select_next_pathbank_archive_candidate,
    summarize_pathbank_archive_candidate_frontier,
)
from scripts.build_source_identifier_snapshot import (
    build_snapshot,
    main,
    pathbank_terms,
    source_terms,
)

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



def archive_fixture(tmp_path, root=None):
    if root is None:
        root = native_source()
        add_stub(root)
    body = ET.tostring(root)
    path = tmp_path / "primary.zip"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("PW9999999.owl", body)
    return path, {
        "key": "archive", "kind": PATHBANK_ARCHIVE_KIND, "path": path.name,
        "url": PATHBANK_ARCHIVE_URL, "version": "fixture", "license": "fixture",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "archive": {"bytes": path.stat().st_size, "member": "PW9999999.owl",
                    "member_bytes": len(body), "member_sha256": hashlib.sha256(body).hexdigest(),
                    "root": "SMP9999999"},
    }


def parse_archive(path, entry):
    return list(source_terms(entry["kind"], path, url=entry["url"], version=entry["version"],
                             archive=entry.get("archive"), sha256=entry["sha256"]))


def archive_snapshot(tmp_path):
    path, entry = archive_fixture(tmp_path)
    records = tmp_path / "records"
    records.mkdir()
    (records / "record.yaml").write_text(yaml.safe_dump({
        "id": PATHWAY, "label": "Curated title never used as authority", "participants": [
            {"id": PATHWAY + "/ProteinComplex/8", "label": "Curated complex"}],
        "reactions": [{"id": "PathBank:SMP9999998", "label": "Curated child"}],
    }))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([entry]))
    return build_snapshot(manifest, records, tmp_path), entry, path, manifest, records


def test_archive_bytes_root_and_attached_names_remain_independent_authority(tmp_path):
    snapshot, entry, path, _, _ = archive_snapshot(tmp_path)
    terms = parse_archive(path, entry)
    assert terms == list(pathbank_terms(ET.fromstring(zipfile.ZipFile(path).read(
        entry["archive"]["member"])), url=DOWNLOAD))
    metadata = snapshot["sources"]["archive"]
    assert metadata["sha256"] == entry["sha256"]
    assert metadata["archive"] == entry["archive"]
    assert metadata["url"] == PATHBANK_ARCHIVE_URL
    assert metadata["pathway_accessions"] == ["SMP9999999", "SMP9999998"]
    assert snapshot["terms"]["PathBank:SMP9999998"]["label"] == "Adjacent native pathway"
    assert snapshot["terms"][PATHWAY + "/ProteinComplex/8"]["label_kind"] == "source_context"
    assert "Curated" not in json.dumps(snapshot)
    authority = tmp_path / "snapshot.json"
    authority.write_text(json.dumps(snapshot))
    assert _load_authority(authority) == snapshot["terms"]


@pytest.mark.parametrize("problem", [
    "archive-hash", "archive-bytes", "member-hash", "member-bytes", "member-missing",
    "root-missing", "root-stub", "live-url", "foreign-url", "url-query", "url-fragment",
    "url-whitespace", "member-path", "bool-bytes", "string-bytes", "missing-field",
    "extra-field", "unknown-kind", "missing-object", "invalid-member-hash",
])
def test_archive_binding_cannot_be_spoofed_before_parsing(tmp_path, problem):
    path, entry = archive_fixture(tmp_path)
    archive = entry["archive"]
    if problem == "archive-hash":
        entry["sha256"] = "0" * 64
    elif problem in {"archive-bytes", "member-bytes"}:
        archive["bytes" if problem == "archive-bytes" else "member_bytes"] += 1
    elif problem == "member-hash":
        archive["member_sha256"] = "0" * 64
    elif problem == "member-missing":
        archive["member"] = "PW0000000.owl"
    elif problem in {"root-missing", "root-stub"}:
        archive["root"] = "SMP0000000" if problem == "root-missing" else "SMP9999998"
    elif problem.endswith("url") or problem.startswith("url-"):
        entry["url"] = {"live-url": DOWNLOAD, "foreign-url": "https://example.org/source.zip",
                        "url-query": PATHBANK_ARCHIVE_URL + "?root=SMP9999999",
                        "url-fragment": PATHBANK_ARCHIVE_URL + "#PW9999999.owl",
                        "url-whitespace": PATHBANK_ARCHIVE_URL + " "}[problem]
    elif problem == "member-path":
        archive["member"] = "../PW9999999.owl"
    elif problem in {"bool-bytes", "string-bytes"}:
        archive["bytes"] = True if problem == "bool-bytes" else str(archive["bytes"])
    elif problem == "missing-field":
        archive.pop("member_sha256")
    elif problem == "extra-field":
        archive["claimed_title"] = "Plausible name"
    elif problem == "unknown-kind":
        entry["kind"] = "pathbank-biopax"
    elif problem == "missing-object":
        entry.pop("archive")
    elif problem == "invalid-member-hash":
        archive["member_sha256"] = "not-a-hash"
    with pytest.raises(ValueError, match="PathBank"):
        parse_archive(path, entry)


@pytest.mark.parametrize("problem", [
    "unattached-child", "expanded-child", "duplicate-accession", "wrong-namespace", "wrong-root",
])
def test_archive_native_membership_remains_closed(tmp_path, problem):
    root = native_source()
    stub = add_stub(root)
    if problem == "unattached-child":
        primary = root.find(BP + "Pathway")
        primary.remove(primary.findall(BP + "pathwayComponent")[-1])
    elif problem == "expanded-child":
        root.find(BP + "Interaction").tag = BP + "BiochemicalReaction"
    elif problem == "duplicate-accession":
        root.append(copy.deepcopy(stub))
    elif problem == "wrong-namespace":
        stub.tag = "{https://other.example/}Pathway"
    else:
        root.tag = "NotRDF"
    path, entry = archive_fixture(tmp_path, root)
    with pytest.raises(ValueError, match="PathBank"):
        parse_archive(path, entry)


def test_duplicate_selected_zip_member_is_rejected_even_when_bytes_match(tmp_path):
    path, entry = archive_fixture(tmp_path)
    with zipfile.ZipFile(path) as archive:
        body = archive.read(entry["archive"]["member"])
    with zipfile.ZipFile(path, "a") as archive, pytest.warns(UserWarning, match="Duplicate name"):
        archive.writestr(entry["archive"]["member"], body)
    entry["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    entry["archive"]["bytes"] = path.stat().st_size
    with pytest.raises(ValueError, match="one exact member"):
        parse_archive(path, entry)


@pytest.mark.parametrize("problem", [
    "missing-archive", "extra-archive-field", "bool-count", "wrong-url", "wrong-kind",
    "missing-kind", "missing-pathways", "duplicate-pathways", "wrong-first-pathway",
    "non-pathbank-term", "unlisted-pathway", "wrong-local-root", "contextual-pathway",
    "canonical-local", "unsafe-local", "invented-entity-type", "hash-scope",
])
def test_snapshot_consumer_rejects_malformed_typed_archive_provenance(tmp_path, problem):
    snapshot, _, _, _, _ = archive_snapshot(tmp_path)
    meta = snapshot["sources"]["archive"]
    term = snapshot["terms"][PATHWAY]
    if problem == "missing-archive":
        meta.pop("archive")
    elif problem == "extra-archive-field":
        meta["archive"]["other"] = "unsupported"
    elif problem == "bool-count":
        meta["archive"]["member_bytes"] = True
    elif problem == "wrong-url":
        meta["url"] = DOWNLOAD
    elif problem == "wrong-kind":
        meta["kind"] = "metacyc-reaction-xml"
    elif problem == "missing-kind":
        meta.pop("kind")
    elif problem == "missing-pathways":
        meta.pop("pathway_accessions")
    elif problem == "duplicate-pathways":
        meta["pathway_accessions"].append(meta["pathway_accessions"][0])
    elif problem == "wrong-first-pathway":
        meta["pathway_accessions"].reverse()
    elif problem in {"non-pathbank-term", "unlisted-pathway", "wrong-local-root", "unsafe-local"}:
        identifier = {"non-pathbank-term": "MetaCyc:PWY-FIXTURE",
                      "unlisted-pathway": "PathBank:SMP0000000",
                      "wrong-local-root": "PathBank:SMP9999998/ProteinComplex/8",
                      "unsafe-local": PATHWAY + "/ProteinComplex/../8"}[problem]
        snapshot["terms"][identifier] = snapshot["terms"].pop(
            PATHWAY if problem in {"non-pathbank-term", "unlisted-pathway"}
            else PATHWAY + "/ProteinComplex/8")
    elif problem == "contextual-pathway":
        term["label_kind"] = "source_context"
    elif problem == "canonical-local":
        snapshot["terms"][PATHWAY + "/ProteinComplex/8"].pop("label_kind")
    elif problem == "invented-entity-type":
        term["entity_type"] = "reaction"
    elif problem == "hash-scope":
        meta["sha256_scope"] = "Actually only the member hash"
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(snapshot))
    with pytest.raises(ValueError):
        _load_authority(path)


def test_archive_builder_failure_preserves_previous_output(tmp_path, monkeypatch):
    _, entry, _, manifest, records = archive_snapshot(tmp_path)
    entry["archive"]["member_sha256"] = "0" * 64
    manifest.write_text(json.dumps([entry]))
    output = tmp_path / "output.json"
    output.write_text("previous reviewed authority")
    monkeypatch.setattr(sys, "argv", ["builder", "--manifest", str(manifest),
                        "--records", str(records), "--cache-dir", str(tmp_path),
                        "--output", str(output)])
    with pytest.raises(ValueError, match="member bytes"):
        main()
    assert output.read_text() == "previous reviewed authority"


@pytest.mark.parametrize("problem", ["extra-field", "missing-archive", "legacy-scope"])
def test_archive_manifest_fields_are_closed(tmp_path, problem):
    _, entry, _, manifest, records = archive_snapshot(tmp_path)
    if problem == "extra-field":
        entry["root"] = "SMP9999999"
    elif problem == "missing-archive":
        entry.pop("archive")
    else:
        entry["sha256_scope"] = "Only a member, despite claiming the ZIP kind"
    manifest.write_text(json.dumps([entry]))
    with pytest.raises(ValueError, match="closed source manifest"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("selected", [True, False])
def test_archive_and_live_child_name_conflict_fails_before_selection(tmp_path, selected):
    _, entry, _, manifest, records = archive_snapshot(tmp_path)
    root = native_source()
    child = add_stub(root)
    child.find(BP + "displayName").text = "Conflicting native child name"
    path = tmp_path / "live.owl"
    path.write_bytes(ET.tostring(root))
    other = {"key": "live", "kind": "pathbank-biopax", "path": path.name,
             "url": DOWNLOAD, "version": "fixture", "license": "fixture",
             "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    manifest.write_text(json.dumps([entry, other]))
    if not selected:
        (records / "record.yaml").write_text(yaml.safe_dump({
            "id": PATHWAY, "label": "Native pathway title"}))
    with pytest.raises(ValueError, match="conflicting PathBank native pathway names"):
        build_snapshot(manifest, records, tmp_path)


def add_interaction_stub(root, *, route="both"):
    """A second issuing format: primary Interaction points to an empty child."""
    primary = root.find(BP + "Pathway")
    uri = "http://identifiers.org/smpdb/SMP9999998"
    child = ET.SubElement(root, BP + "Pathway", {RDF + "about": uri})
    ET.SubElement(child, BP + "displayName").text = "An independently named adjacent pathway"
    ET.SubElement(child, BP + "name").text = "InhibitorySubPathway"
    ET.SubElement(child, BP + "xref", {RDF + "resource": "#child-smp"})
    xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "child-smp"})
    ET.SubElement(xref, BP + "db").text = "SMPDB"
    ET.SubElement(xref, BP + "id").text = "SMP9999998"
    bridge = ET.SubElement(root, BP + "Interaction", {RDF + "ID": "SubPathwayControls/812"})
    ET.SubElement(bridge, BP + "displayName").text = "Native drawing connector"
    ET.SubElement(bridge, BP + "name").text = "SubPathway812Control"
    ET.SubElement(bridge, BP + "name").text = "InhibitorySubPathwayControl"
    ET.SubElement(bridge, BP + "participant", {RDF + "resource": "#Compound/interface"})
    ET.SubElement(bridge, BP + "participant", {RDF + "resource": uri})
    compound = ET.SubElement(root, BP + "SmallMolecule", {RDF + "ID": "Compound/interface"})
    ET.SubElement(compound, BP + "displayName").text = "Native interface compound name"
    ET.SubElement(compound, BP + "name").text = "SubPathwayInhibitor"
    ET.SubElement(compound, BP + "entityReference", {RDF + "resource": "#reference/interface"})
    ET.SubElement(root, BP + "SmallMoleculeReference", {RDF + "ID": "reference/interface"})
    step = ET.SubElement(root, BP + "PathwayStep", {RDF + "ID": "PathwaySubPathway/812"})
    ET.SubElement(step, BP + "stepProcess", {RDF + "resource": "#SubPathwayControls/812"})
    if route in {"direct", "both"}:
        ET.SubElement(primary, BP + "pathwayComponent", {
            RDF + "resource": "#SubPathwayControls/812",
        })
    if route in {"ordered", "both"}:
        ET.SubElement(primary, BP + "pathwayOrder", {
            RDF + "resource": "#PathwaySubPathway/812",
        })
    return primary, child, bridge, compound, step, xref


@pytest.mark.parametrize("route", ["direct", "ordered", "both"])
@pytest.mark.parametrize("child_first", [True, False])
def test_primary_owned_interaction_only_adds_an_opaque_native_identity(route, child_first):
    root = native_source()
    _, child, _, _, _, _ = add_interaction_stub(root, route=route)
    if child_first:
        root.remove(child)
        root.insert(0, child)
    terms = list(pathbank_terms(root, url=DOWNLOAD))
    assert terms[:2] == [
        (PATHWAY, "Native pathway title", []),
        ("PathBank:SMP9999998", "An independently named adjacent pathway", []),
    ]
    assert all("SubPathwayControls" not in term[0] for term in terms)
    assert not any(term[0].startswith("PathBank:SMP9999998/") for term in terms)
    assert len([term for term in terms if term[0] == "PathBank:SMP9999998"]) == 1


INTERACTION_PROBLEMS = [
    "unowned", "only-catalysis-owned", "dangling-owner", "wrong-step-type", "step-conversion",
    "extra-step-process", "duplicate-direct-owner", "duplicate-ordered-owner", "wrong-owner",
    "wrong-process-type", "process-marker-missing", "process-marker-wrong",
    "process-marker-duplicated", "extra-process-field", "foreign-process", "process-extra-attr",
    "missing-participant", "extra-participant", "duplicate-participant", "dangling-participant",
    "participant-text", "participant-extra-attr", "participant-nested", "two-pathway-participants",
    "root-as-child", "wrong-compound-type", "compound-marker-wrong", "compound-reference-missing",
    "compound-reference-dangling", "compound-reference-wrong-type", "compound-extra-field",
    "foreign-compound-reference", "child-marker-missing", "child-marker-wrong",
    "child-marker-duplicated", "child-expanded", "child-extra-field", "child-duplicate-title",
    "child-empty-title", "child-nested-title", "child-generic-title", "child-duplicate-xref",
    "child-dangling-xref", "child-wrong-xref-type", "child-conflicting-accession",
    "child-conflicting-uri", "child-xref-duplicate-id", "child-xref-duplicate-db",
    "duplicate-child", "duplicate-bridge-subject", "duplicate-bridge-to-child", "foreign-child",
    "nested-base", "unrelated-child", "extra-literal-attribute", "nested-process-name",
]


def break_interaction_source(root, problem):
    primary, child, bridge, compound, step, xref = add_interaction_stub(root)
    names = bridge.findall(BP + "name")
    participants = bridge.findall(BP + "participant")
    reference = root.find(BP + "SmallMoleculeReference")
    if problem in {"unowned", "only-catalysis-owned", "wrong-owner"}:
        primary.remove(primary.findall(BP + "pathwayComponent")[-1])
        primary.remove(primary.find(BP + "pathwayOrder"))
        if problem == "only-catalysis-owned":
            control = ET.SubElement(root, BP + "Catalysis", {RDF + "ID": "indirect-owner"})
            ET.SubElement(control, BP + "controlled", {RDF + "resource": "#SubPathwayControls/812"})
            ET.SubElement(primary, BP + "pathwayComponent", {RDF + "resource": "#indirect-owner"})
        elif problem == "wrong-owner":
            ET.SubElement(child, BP + "pathwayComponent", {
                RDF + "resource": "#SubPathwayControls/812",
            })
    elif problem == "dangling-owner":
        primary.find(BP + "pathwayOrder").set(RDF + "resource", "#missing-owner")
    elif problem == "wrong-step-type":
        step.tag = BP + "BiochemicalPathwayStep"
    elif problem == "step-conversion":
        step[0].tag = BP + "stepConversion"
    elif problem == "extra-step-process":
        ET.SubElement(step, BP + "stepProcess", {RDF + "resource": "#Reactions/7"})
    elif problem == "duplicate-direct-owner":
        primary.append(copy.deepcopy(primary.findall(BP + "pathwayComponent")[-1]))
    elif problem == "duplicate-ordered-owner":
        primary.append(copy.deepcopy(primary.find(BP + "pathwayOrder")))
    elif problem == "wrong-process-type":
        bridge.tag = BP + "Control"
    elif problem == "process-marker-missing":
        bridge.remove(names[1])
    elif problem == "process-marker-wrong":
        names[1].text = "ArbitraryControl"
    elif problem == "process-marker-duplicated":
        names[0].text = names[1].text
    elif problem == "extra-process-field":
        ET.SubElement(bridge, BP + "controlled", {RDF + "resource": child.get(RDF + "about")})
    elif problem == "foreign-process":
        bridge.attrib = {RDF + "about": "https://elsewhere.example/#SubPathwayControls/812"}
    elif problem == "process-extra-attr":
        bridge.set("scope", "trusted")
    elif problem == "missing-participant":
        bridge.remove(participants[1])
    elif problem == "extra-participant":
        ET.SubElement(bridge, BP + "participant", {RDF + "resource": "#Reactions/7"})
    elif problem == "duplicate-participant":
        participants[1].set(RDF + "resource", participants[0].get(RDF + "resource"))
    elif problem == "dangling-participant":
        participants[0].set(RDF + "resource", "#missing-compound")
    elif problem == "participant-text":
        participants[0].text = "ambiguous inline identity"
    elif problem == "participant-extra-attr":
        participants[0].set("scope", "trusted")
    elif problem == "participant-nested":
        ET.SubElement(participants[0], BP + "SmallMolecule")
    elif problem == "two-pathway-participants":
        participants[0].set(RDF + "resource", primary.get(RDF + "about"))
    elif problem == "root-as-child":
        participants[1].set(RDF + "resource", primary.get(RDF + "about"))
    elif problem == "wrong-compound-type":
        compound.tag = BP + "Protein"
    elif problem == "compound-marker-wrong":
        compound.find(BP + "name").text = "UnrelatedDrawingNode"
    elif problem == "compound-reference-missing":
        compound.remove(compound.find(BP + "entityReference"))
    elif problem == "compound-reference-dangling":
        root.remove(reference)
    elif problem == "compound-reference-wrong-type":
        reference.tag = BP + "ProteinReference"
    elif problem == "compound-extra-field":
        ET.SubElement(compound, BP + "controller", {RDF + "resource": "#Reactions/7"})
    elif problem == "foreign-compound-reference":
        reference.attrib = {RDF + "about": "https://elsewhere.example/#reference/interface"}
    elif problem == "child-marker-missing":
        child.remove(child.find(BP + "name"))
    elif problem == "child-marker-wrong":
        child.find(BP + "name").text = "UnrelatedPathway"
    elif problem == "child-marker-duplicated":
        child.append(copy.deepcopy(child.find(BP + "name")))
    elif problem == "child-expanded":
        ET.SubElement(child, BP + "pathwayComponent", {RDF + "resource": "#Reactions/7"})
    elif problem == "child-extra-field":
        ET.SubElement(child, BP + "organism", {RDF + "resource": "#species"})
    elif problem == "child-duplicate-title":
        child.append(copy.deepcopy(child.find(BP + "displayName")))
    elif problem == "child-empty-title":
        child.find(BP + "displayName").text = " "
    elif problem == "child-nested-title":
        ET.SubElement(child.find(BP + "displayName"), "em").text = "nested"
    elif problem == "child-generic-title":
        child.find(BP + "displayName").text = "inhibitorysubpathway"
    elif problem == "child-duplicate-xref":
        child.append(copy.deepcopy(child.find(BP + "xref")))
    elif problem == "child-dangling-xref":
        child.find(BP + "xref").set(RDF + "resource", "#absent")
    elif problem == "child-wrong-xref-type":
        xref.tag = BP + "RelationshipXref"
    elif problem == "child-conflicting-accession":
        xref.find(BP + "id").text = "SMP1234567"
    elif problem == "child-conflicting-uri":
        child.set(RDF + "about", "http://identifiers.org/smpdb/SMP1234567")
    elif problem == "child-xref-duplicate-id":
        xref.append(copy.deepcopy(xref.find(BP + "id")))
    elif problem == "child-xref-duplicate-db":
        xref.append(copy.deepcopy(xref.find(BP + "db")))
    elif problem == "duplicate-child":
        root.append(copy.deepcopy(child))
    elif problem == "duplicate-bridge-subject":
        root.append(copy.deepcopy(bridge))
    elif problem == "duplicate-bridge-to-child":
        other = copy.deepcopy(bridge)
        other.set(RDF + "ID", "SubPathwayControls/813")
        root.append(other)
        ET.SubElement(primary, BP + "pathwayComponent", {
            RDF + "resource": "#SubPathwayControls/813",
        })
    elif problem == "foreign-child":
        child.tag = "{https://elsewhere.example/}Pathway"
    elif problem == "nested-base":
        bridge.set(XML + "base", "https://elsewhere.example/")
    elif problem == "unrelated-child":
        other = add_stub(root, "SMP9999997")
        primary.remove(primary.findall(BP + "pathwayComponent")[-1])
        assert other.get(RDF + "about").endswith("SMP9999997")
    elif problem == "extra-literal-attribute":
        names[1].set("verified", "yes")
    elif problem == "nested-process-name":
        ET.SubElement(names[1], "em").text = "nested"
    else:
        raise AssertionError(problem)


@pytest.mark.parametrize("problem", INTERACTION_PROBLEMS)
def test_interaction_shape_cannot_authorize_unproven_child_identity(tmp_path, problem):
    root = native_source()
    break_interaction_source(root, problem)
    path, entry = archive_fixture(tmp_path, root)
    with pytest.raises(ValueError, match="PathBank"):
        parse_archive(path, entry)


@pytest.mark.parametrize("route", ["direct", "ordered", "both"])
def test_interaction_archive_has_separate_original_provenance_and_no_causal_terms(tmp_path, route):
    root = native_source()
    add_interaction_stub(root, route=route)
    path, entry = archive_fixture(tmp_path, root)
    records = tmp_path / "selection"
    records.mkdir()
    (records / "selection.yaml").write_text(yaml.safe_dump({
        "id": PATHWAY, "label": "DO NOT USE THIS CURATED TITLE",
        "participants": [{"id": "PathBank:SMP9999998", "label": "ALSO NOT AN AUTHORITY"}],
    }))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([entry]))
    result = build_snapshot(manifest, records, tmp_path)
    assert set(result["terms"]) == {PATHWAY, "PathBank:SMP9999998"}
    assert result["terms"]["PathBank:SMP9999998"] == {
        "label": "An independently named adjacent pathway", "synonyms": [], "source": "archive",
    }
    assert result["sources"]["archive"]["pathway_accessions"] == ["SMP9999999", "SMP9999998"]
    assert result["sources"]["archive"]["archive"] == entry["archive"]
    assert not any(marker in json.dumps(result) for marker in [
        "InhibitorySubPathway", "SubPathwayInhibitor", "DO NOT USE", "ALSO NOT",
    ])
    snapshot = tmp_path / "authority.json"
    snapshot.write_text(json.dumps(result))
    assert _load_authority(snapshot) == result["terms"]
    assert path.read_bytes()


@pytest.mark.parametrize("selected", [True, False])
def test_invalid_interaction_child_preserves_previous_authority_before_selection(
    tmp_path, monkeypatch, selected,
):
    root = native_source()
    break_interaction_source(root, "unowned")
    source, entry = archive_fixture(tmp_path, root)
    records = tmp_path / "records"
    records.mkdir()
    (records / "record.yaml").write_text(yaml.safe_dump({
        "id": "PathBank:SMP9999998" if selected else PATHWAY,
        "label": "irrelevant selection label",
    }))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps([entry]))
    output = tmp_path / "authority.json"
    output.write_bytes(b"previous authority\n")
    monkeypatch.setattr(sys, "argv", [
        "builder", "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(source.parent), "--output", str(output),
    ])
    with pytest.raises(ValueError, match="PathBank"):
        main()
    assert output.read_bytes() == b"previous authority\n"


def test_build_pathbank_archive_manifest_entry_computes_exact_closed_provenance(tmp_path):
    path, expected = archive_fixture(tmp_path)
    built = build_pathbank_archive_manifest_entry(
        path,
        "PW9999999.owl",
        "SMP9999999",
    )
    assert built == {
        "key": "pathbank-primary-2019-PW9999999-SMP9999999",
        "kind": PATHBANK_ARCHIVE_KIND,
        "path": PATHBANK_ARCHIVE_DEFAULT_PATH,
        "url": PATHBANK_ARCHIVE_URL,
        "version": PATHBANK_ARCHIVE_VERSION,
        "license": PATHBANK_ARCHIVE_LICENSE,
        "sha256": expected["sha256"],
        "archive": expected["archive"],
    }


@pytest.mark.parametrize(
    "member,root,kwargs,match",
    [
        ("PW0001.xml", "SMP9999999", {}, "exact PW"),
        ("PW9999999.owl", "PW9999999", {}, "exact SMP"),
        ("PW0000001.owl", "SMP9999999", {}, "missing member"),
        (
            "PW9999999.owl",
            "SMP0000001",
            {},
            "PathBank request and native pathway accessions disagree",
        ),
        (
            "PW9999999.owl",
            "SMP9999998",
            {},
            "PathBank requested source must contain the primary pathway definition",
        ),
        ("PW9999999.owl", "SMP9999999", {"key": " "}, "key must be a non-empty string"),
        ("PW9999999.owl", "SMP9999999", {"path": ""}, "path must be a non-empty string"),
        (
            "PW9999999.owl",
            "SMP9999999",
            {"path": "/etc/primary.zip"},
            "relative path without parent traversal",
        ),
        (
            "PW9999999.owl",
            "SMP9999999",
            {"path": "../primary.zip"},
            "relative path without parent traversal",
        ),
    ],
)
def test_build_pathbank_archive_manifest_entry_rejects_invalid_inputs(
    tmp_path, member, root, kwargs, match
):
    path, _ = archive_fixture(tmp_path)
    with pytest.raises(ValueError, match=match):
        build_pathbank_archive_manifest_entry(path, member, root, **kwargs)


def test_build_pathbank_archive_manifest_entry_rejects_duplicate_or_non_rdf_member(tmp_path):
    path, entry = archive_fixture(tmp_path)
    with zipfile.ZipFile(path) as archive:
        body = archive.read(entry["archive"]["member"])
    with zipfile.ZipFile(path, "a") as archive, pytest.warns(UserWarning, match="Duplicate name"):
        archive.writestr(entry["archive"]["member"], body)
    with pytest.raises(ValueError, match="one exact member"):
        build_pathbank_archive_manifest_entry(path, "PW9999999.owl", "SMP9999999")

    non_rdf_zip = tmp_path / "non_rdf.zip"
    with zipfile.ZipFile(non_rdf_zip, "w") as archive:
        archive.writestr("PW9999999.owl", b"<NotRDF/>")
    with pytest.raises(ValueError, match="native RDF/BioPAX"):
        build_pathbank_archive_manifest_entry(non_rdf_zip, "PW9999999.owl", "SMP9999999")

    bad_zip = tmp_path / "bad.zip"
    bad_zip.write_bytes(b"not a zip archive")
    with pytest.raises(ValueError, match="valid ZIP archive"):
        build_pathbank_archive_manifest_entry(bad_zip, "PW9999999.owl", "SMP9999999")


def test_inspect_pathbank_archive_member_enumerates_native_terms_and_external_xrefs(tmp_path):
    root = native_source()
    add_stub(root)
    uniprot_xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "uniprot-xref"})
    ET.SubElement(uniprot_xref, BP + "db").text = "UniProt"
    ET.SubElement(uniprot_xref, BP + "id").text = "P0A9T0"
    taxon_xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "taxon-xref"})
    ET.SubElement(taxon_xref, BP + "db").text = "TAXONOMY"
    ET.SubElement(taxon_xref, BP + "id").text = "562"
    path, expected = archive_fixture(tmp_path, root)
    summary = inspect_pathbank_archive_member(path, "PW9999999.owl", "SMP9999999")
    assert summary == {
        "manifest_entry": {
            "key": "pathbank-primary-2019-PW9999999-SMP9999999",
            "kind": PATHBANK_ARCHIVE_KIND,
            "path": PATHBANK_ARCHIVE_DEFAULT_PATH,
            "url": PATHBANK_ARCHIVE_URL,
            "version": PATHBANK_ARCHIVE_VERSION,
            "license": PATHBANK_ARCHIVE_LICENSE,
            "sha256": expected["sha256"],
            "archive": expected["archive"],
        },
        "pathway_id": PATHWAY,
        "pathway_label": "Native pathway title",
        "native_term_ids": [
            PATHWAY,
            "PathBank:SMP9999998",
            PATHWAY + "/Reactions/7",
            PATHWAY + "/ProteinComplex/8",
        ],
        "external_xrefs": {
            "CHEBI": ["CHEBI:15377"],
            "NCBITaxon": ["NCBITaxon:562"],
            "UniProtKB": ["UniProtKB:P0A9T0"],
        },
    }


def test_audit_pathbank_archive_member_authority_partitions_indexed_and_missing_curies(tmp_path):
    root = native_source()
    add_stub(root)
    uniprot_xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "uniprot-xref"})
    ET.SubElement(uniprot_xref, BP + "db").text = "UniProt"
    ET.SubElement(uniprot_xref, BP + "id").text = "P0A9T0"
    taxon_xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "taxon-xref"})
    ET.SubElement(taxon_xref, BP + "db").text = "TAXONOMY"
    ET.SubElement(taxon_xref, BP + "id").text = "562"
    path, _ = archive_fixture(tmp_path, root)

    partial_snapshot = tmp_path / "partial_sources.json"
    partial_snapshot.write_text(
        json.dumps(
            {
                "sources": {},
                "terms": {
                    "CHEBI:15377": {"label": "water", "synonyms": [], "source": "chebi-obo"},
                    "NCBITaxon:562": {
                        "label": "Escherichia coli",
                        "synonyms": [],
                        "source": "ncbitaxon-obo",
                    },
                },
            }
        ),
        encoding="utf-8",
    )
    partial_audit = audit_pathbank_archive_member_authority(
        path, "PW9999999.owl", "SMP9999999", partial_snapshot
    )
    assert partial_audit["manifest_key_registered"] is False
    assert partial_audit["indexed_native_term_ids"] == []
    assert partial_audit["missing_native_term_ids"] == [
        PATHWAY,
        "PathBank:SMP9999998",
        PATHWAY + "/Reactions/7",
        PATHWAY + "/ProteinComplex/8",
    ]
    assert partial_audit["indexed_external_xrefs"] == {
        "CHEBI": ["CHEBI:15377"],
        "NCBITaxon": ["NCBITaxon:562"],
        "UniProtKB": [],
    }
    assert partial_audit["missing_external_xrefs"] == {
        "CHEBI": [],
        "NCBITaxon": [],
        "UniProtKB": ["UniProtKB:P0A9T0"],
    }
    assert partial_audit["ready_for_check_identifiers"] is False

    complete_snapshot = tmp_path / "complete_sources.json"
    complete_snapshot.write_text(
        json.dumps(
            {
                "sources": {
                    "pathbank-primary-2019-PW9999999-SMP9999999": partial_audit["manifest_entry"]
                },
                "terms": {
                    PATHWAY: {
                        "label": "Native pathway title",
                        "synonyms": [],
                        "source": "pathbank-primary-2019-PW9999999-SMP9999999",
                    },
                    "PathBank:SMP9999998": {
                        "label": "An independently named adjacent pathway",
                        "synonyms": [],
                        "source": "pathbank-primary-2019-PW9999999-SMP9999999",
                    },
                    PATHWAY + "/Reactions/7": {
                        "label": "Reaction 7",
                        "synonyms": [],
                        "source": "pathbank-primary-2019-PW9999999-SMP9999999",
                    },
                    PATHWAY + "/ProteinComplex/8": {
                        "label": "Complex 8",
                        "synonyms": [],
                        "source": "pathbank-primary-2019-PW9999999-SMP9999999",
                    },
                    "CHEBI:15377": {"label": "water", "synonyms": [], "source": "chebi-obo"},
                    "NCBITaxon:562": {
                        "label": "Escherichia coli",
                        "synonyms": [],
                        "source": "ncbitaxon-obo",
                    },
                    "UniProtKB:P0A9T0": {
                        "label": "D-3-phosphoglycerate dehydrogenase",
                        "synonyms": [],
                        "source": "uniprot-entries",
                    },
                },
            }
        ),
        encoding="utf-8",
    )
    complete_audit = audit_pathbank_archive_member_authority(
        path, "PW9999999.owl", "SMP9999999", complete_snapshot
    )
    assert complete_audit["manifest_key_registered"] is True
    assert complete_audit["indexed_native_term_ids"] == [
        PATHWAY,
        "PathBank:SMP9999998",
        PATHWAY + "/Reactions/7",
        PATHWAY + "/ProteinComplex/8",
    ]
    assert complete_audit["missing_native_term_ids"] == []
    assert complete_audit["indexed_external_xrefs"] == {
        "CHEBI": ["CHEBI:15377"],
        "NCBITaxon": ["NCBITaxon:562"],
        "UniProtKB": ["UniProtKB:P0A9T0"],
    }
    assert complete_audit["missing_external_xrefs"] == {
        "CHEBI": [],
        "NCBITaxon": [],
        "UniProtKB": [],
    }
    assert complete_audit["ready_for_check_identifiers"] is True


@pytest.mark.parametrize(
    "payload,match",
    [
        (None, "valid JSON authority snapshot"),
        ("not json", "valid JSON authority snapshot"),
        ("[]", "'sources' and 'terms' mappings"),
        ('{"sources": []}', "'sources' and 'terms' mappings"),
        ('{"sources": {}, "terms": []}', "'sources' and 'terms' mappings"),
    ],
)
def test_audit_pathbank_archive_member_authority_rejects_invalid_snapshot(tmp_path, payload, match):
    path, _ = archive_fixture(tmp_path)
    snapshot_path = tmp_path / "invalid_sources.json"
    if payload is not None:
        snapshot_path.write_text(payload, encoding="utf-8")
    with pytest.raises(ValueError, match=match):
        audit_pathbank_archive_member_authority(
            path, "PW9999999.owl", "SMP9999999", snapshot_path
        )


def _member_root_for_accession(
    smp_accession: str, *, uniprot_ids: tuple[str, ...] = ()
) -> ET.Element:
    root = native_source()
    pathway = root.find(BP + "Pathway")
    pathway.set(RDF + "about", f"http://identifiers.org/smpdb/{smp_accession}")
    root.find(BP + "UnificationXref").find(BP + "id").text = smp_accession
    for idx, uniprot_id in enumerate(uniprot_ids):
        xref = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": f"uniprot-{idx}"})
        ET.SubElement(xref, BP + "db").text = "UniProt"
        ET.SubElement(xref, BP + "id").text = uniprot_id
    return root


def test_rank_pathbank_archive_member_candidates_orders_by_readiness_and_missing_counts(tmp_path):
    archive_path = tmp_path / "candidates.zip"
    root_ready = _member_root_for_accession("SMP9999991", uniprot_ids=("P0A9T0",))
    root_one_missing = _member_root_for_accession("SMP9999992", uniprot_ids=("P0A9T0", "P00877"))
    root_two_missing = _member_root_for_accession(
        "SMP9999993", uniprot_ids=("P00877", "P0A6D7")
    )
    with zipfile.ZipFile(archive_path, "w") as archive:
        archive.writestr(
            "PW9999993.owl", ET.tostring(root_two_missing, encoding="utf-8", xml_declaration=True)
        )
        archive.writestr(
            "PW9999991.owl", ET.tostring(root_ready, encoding="utf-8", xml_declaration=True)
        )
        archive.writestr(
            "PW9999992.owl", ET.tostring(root_one_missing, encoding="utf-8", xml_declaration=True)
        )

    ready_manifest = build_pathbank_archive_manifest_entry(
        archive_path, "PW9999991.owl", "SMP9999991"
    )
    snapshot_path = tmp_path / "sources.json"
    snapshot_path.write_text(
        json.dumps(
            {
                "sources": {ready_manifest["key"]: ready_manifest},
                "terms": {
                    "PathBank:SMP9999991": {
                        "label": "Native pathway title",
                        "synonyms": [],
                        "source": ready_manifest["key"],
                    },
                    "PathBank:SMP9999991/Reactions/7": {
                        "label": "1.2.3.4",
                        "synonyms": ["Native substrate → native product"],
                        "source": ready_manifest["key"],
                    },
                    "PathBank:SMP9999991/ProteinComplex/8": {
                        "label": "ProteinComplex/8",
                        "synonyms": [],
                        "source": ready_manifest["key"],
                    },
                    "CHEBI:15377": {"label": "water", "synonyms": [], "source": "chebi-obo"},
                    "UniProtKB:P0A9T0": {
                        "label": "D-3-phosphoglycerate dehydrogenase",
                        "synonyms": [],
                        "source": "uniprot-entries",
                    },
                },
            }
        ),
        encoding="utf-8",
    )

    ranked = rank_pathbank_archive_member_candidates(
        archive_path,
        [
            ("PW9999993.owl", "SMP9999993"),
            ("PW9999991.owl", "SMP9999991"),
            ("PW9999992.owl", "SMP9999992"),
        ],
        snapshot_path,
    )
    assert [entry["pathway_id"] for entry in ranked] == [
        "PathBank:SMP9999991",
        "PathBank:SMP9999992",
        "PathBank:SMP9999993",
    ]
    assert [entry["ready_for_check_identifiers"] for entry in ranked] == [True, False, False]
    assert [entry["missing_external_xref_count"] for entry in ranked] == [0, 1, 2]
    assert [entry["missing_native_term_count"] for entry in ranked] == [0, 3, 3]


@pytest.mark.parametrize(
    "candidates,match",
    [
        ([], "non-empty sequence"),
        ("PW9999999.owl", "non-empty sequence"),
        ([("PW9999999.owl",)], "2-element \\(member, root\\) string pairs"),
        ([("PW9999999.owl", 123)], "2-element \\(member, root\\) string pairs"),
        (
            [("PW9999999.owl", "SMP9999999"), ("PW9999999.owl", "SMP9999998")],
            "duplicate member: PW9999999.owl",
        ),
        (
            [("PW9999999.owl", "SMP9999999"), ("PW9999998.owl", "SMP9999999")],
            "duplicate root: SMP9999999",
        ),
    ],
)
def test_rank_pathbank_archive_member_candidates_rejects_invalid_candidates(
    tmp_path, candidates, match
):
    path, _ = archive_fixture(tmp_path)
    snapshot_path = tmp_path / "sources.json"
    snapshot_path.write_text(json.dumps({"sources": {}, "terms": {}}), encoding="utf-8")
    with pytest.raises(ValueError, match=match):
        rank_pathbank_archive_member_candidates(path, candidates, snapshot_path)


def test_select_next_pathbank_archive_candidate_skips_registered_and_excluded_pathways(tmp_path):
    archive_path = tmp_path / "candidates.zip"
    root_registered = _member_root_for_accession("SMP9999991", uniprot_ids=("P0A9T0",))
    root_one_missing = _member_root_for_accession("SMP9999992", uniprot_ids=("P0A9T0", "P00877"))
    root_two_missing = _member_root_for_accession(
        "SMP9999993", uniprot_ids=("P00877", "P0A6D7")
    )
    with zipfile.ZipFile(archive_path, "w") as archive:
        archive.writestr(
            "PW9999993.owl", ET.tostring(root_two_missing, encoding="utf-8", xml_declaration=True)
        )
        archive.writestr(
            "PW9999991.owl", ET.tostring(root_registered, encoding="utf-8", xml_declaration=True)
        )
        archive.writestr(
            "PW9999992.owl", ET.tostring(root_one_missing, encoding="utf-8", xml_declaration=True)
        )

    registered_manifest = build_pathbank_archive_manifest_entry(
        archive_path, "PW9999991.owl", "SMP9999991"
    )
    snapshot_path = tmp_path / "sources.json"
    snapshot_path.write_text(
        json.dumps(
            {
                "sources": {registered_manifest["key"]: registered_manifest},
                "terms": {
                    "PathBank:SMP9999991": {
                        "label": "Native pathway title",
                        "synonyms": [],
                        "source": registered_manifest["key"],
                    },
                    "PathBank:SMP9999991/Reactions/7": {
                        "label": "1.2.3.4",
                        "synonyms": ["Native substrate → native product"],
                        "source": registered_manifest["key"],
                    },
                    "PathBank:SMP9999991/ProteinComplex/8": {
                        "label": "ProteinComplex/8",
                        "synonyms": [],
                        "source": registered_manifest["key"],
                    },
                    "CHEBI:15377": {"label": "water", "synonyms": [], "source": "chebi-obo"},
                    "UniProtKB:P0A9T0": {
                        "label": "D-3-phosphoglycerate dehydrogenase",
                        "synonyms": [],
                        "source": "uniprot-entries",
                    },
                },
            }
        ),
        encoding="utf-8",
    )

    candidates = [
        ("PW9999993.owl", "SMP9999993"),
        ("PW9999991.owl", "SMP9999991"),
        ("PW9999992.owl", "SMP9999992"),
    ]
    selected_unregistered = select_next_pathbank_archive_candidate(
        archive_path, candidates, snapshot_path
    )
    assert selected_unregistered is not None
    assert selected_unregistered["pathway_id"] == "PathBank:SMP9999992"
    assert selected_unregistered["missing_external_xref_count"] == 1

    selected_including_registered = select_next_pathbank_archive_candidate(
        archive_path,
        candidates,
        snapshot_path,
        require_unregistered_manifest=False,
    )
    assert selected_including_registered is not None
    assert selected_including_registered["pathway_id"] == "PathBank:SMP9999991"

    selected_after_exclusion = select_next_pathbank_archive_candidate(
        archive_path,
        candidates,
        snapshot_path,
        excluded_pathway_ids={"PathBank:SMP9999992"},
    )
    assert selected_after_exclusion is not None
    assert selected_after_exclusion["pathway_id"] == "PathBank:SMP9999993"

    assert (
        select_next_pathbank_archive_candidate(
            archive_path,
            candidates,
            snapshot_path,
            excluded_pathway_ids=["PathBank:SMP9999992", "PathBank:SMP9999993"],
        )
        is None
    )


@pytest.mark.parametrize(
    "kwargs,match",
    [
        (
            {"require_unregistered_manifest": "yes"},
            "boolean require_unregistered_manifest flag",
        ),
        (
            {"excluded_pathway_ids": "PathBank:SMP9999991"},
            "collection of PathBank:SMP\\[0-9\\]\\+ CURIEs",
        ),
        (
            {"excluded_pathway_ids": ["SMP9999991"]},
            "entries to match PathBank:SMP\\[0-9\\]\\+",
        ),
        (
            {"excluded_pathway_ids": [123]},
            "entries to match PathBank:SMP\\[0-9\\]\\+",
        ),
    ],
)
def test_select_next_pathbank_archive_candidate_rejects_invalid_filters(
    tmp_path, kwargs, match
):
    path, _ = archive_fixture(tmp_path)
    snapshot_path = tmp_path / "sources.json"
    snapshot_path.write_text(json.dumps({"sources": {}, "terms": {}}), encoding="utf-8")
    with pytest.raises(ValueError, match=match):
        select_next_pathbank_archive_candidate(
            path,
            [("PW9999999.owl", "SMP9999999")],
            snapshot_path,
            **kwargs,
        )


def test_summarize_pathbank_archive_candidate_frontier_aggregates_remaining_and_missing_xrefs(
    tmp_path,
):
    archive_path = tmp_path / "candidates.zip"
    root_registered = _member_root_for_accession("SMP9999991", uniprot_ids=("P0A9T0",))
    root_one_missing = _member_root_for_accession("SMP9999992", uniprot_ids=("P0A9T0", "P00877"))
    root_two_missing = _member_root_for_accession(
        "SMP9999993", uniprot_ids=("P00877", "P0A6D7")
    )
    with zipfile.ZipFile(archive_path, "w") as archive:
        archive.writestr(
            "PW9999993.owl", ET.tostring(root_two_missing, encoding="utf-8", xml_declaration=True)
        )
        archive.writestr(
            "PW9999991.owl", ET.tostring(root_registered, encoding="utf-8", xml_declaration=True)
        )
        archive.writestr(
            "PW9999992.owl", ET.tostring(root_one_missing, encoding="utf-8", xml_declaration=True)
        )

    registered_manifest = build_pathbank_archive_manifest_entry(
        archive_path, "PW9999991.owl", "SMP9999991"
    )
    snapshot_path = tmp_path / "sources.json"
    snapshot_path.write_text(
        json.dumps(
            {
                "sources": {registered_manifest["key"]: registered_manifest},
                "terms": {
                    "PathBank:SMP9999991": {
                        "label": "Native pathway title",
                        "synonyms": [],
                        "source": registered_manifest["key"],
                    },
                    "PathBank:SMP9999991/Reactions/7": {
                        "label": "1.2.3.4",
                        "synonyms": ["Native substrate → native product"],
                        "source": registered_manifest["key"],
                    },
                    "PathBank:SMP9999991/ProteinComplex/8": {
                        "label": "ProteinComplex/8",
                        "synonyms": [],
                        "source": registered_manifest["key"],
                    },
                    "CHEBI:15377": {"label": "water", "synonyms": [], "source": "chebi-obo"},
                    "UniProtKB:P0A9T0": {
                        "label": "D-3-phosphoglycerate dehydrogenase",
                        "synonyms": [],
                        "source": "uniprot-entries",
                    },
                },
            }
        ),
        encoding="utf-8",
    )

    candidates = [
        ("PW9999993.owl", "SMP9999993"),
        ("PW9999991.owl", "SMP9999991"),
        ("PW9999992.owl", "SMP9999992"),
    ]
    frontier = summarize_pathbank_archive_candidate_frontier(
        archive_path, candidates, snapshot_path
    )
    assert frontier["total_candidates"] == 3
    assert frontier["registered_count"] == 1
    assert frontier["registered_pathway_ids"] == ["PathBank:SMP9999991"]
    assert frontier["excluded_pathway_ids"] == []
    assert frontier["remaining_count"] == 2
    assert frontier["next_candidate"] is not None
    assert frontier["next_candidate"]["pathway_id"] == "PathBank:SMP9999992"
    assert [entry["pathway_id"] for entry in frontier["remaining_candidates"]] == [
        "PathBank:SMP9999992",
        "PathBank:SMP9999993",
    ]
    assert frontier["missing_external_xrefs_union"] == {
        "CHEBI": [],
        "NCBITaxon": [],
        "UniProtKB": ["UniProtKB:P00877", "UniProtKB:P0A6D7"],
    }

    frontier_after_exclusion = summarize_pathbank_archive_candidate_frontier(
        archive_path,
        candidates,
        snapshot_path,
        excluded_pathway_ids={"PathBank:SMP9999992"},
    )
    assert frontier_after_exclusion["excluded_pathway_ids"] == ["PathBank:SMP9999992"]
    assert frontier_after_exclusion["remaining_count"] == 1
    assert frontier_after_exclusion["next_candidate"] is not None
    assert frontier_after_exclusion["next_candidate"]["pathway_id"] == "PathBank:SMP9999993"
    assert frontier_after_exclusion["missing_external_xrefs_union"] == {
        "CHEBI": [],
        "NCBITaxon": [],
        "UniProtKB": ["UniProtKB:P00877", "UniProtKB:P0A6D7"],
    }

    empty_frontier = summarize_pathbank_archive_candidate_frontier(
        archive_path,
        candidates,
        snapshot_path,
        excluded_pathway_ids=["PathBank:SMP9999992", "PathBank:SMP9999993"],
    )
    assert empty_frontier["remaining_count"] == 0
    assert empty_frontier["next_candidate"] is None
    assert empty_frontier["remaining_candidates"] == []
    assert empty_frontier["missing_external_xrefs_union"] == {
        "CHEBI": [],
        "NCBITaxon": [],
        "UniProtKB": [],
    }


@pytest.mark.parametrize(
    "kwargs,match",
    [
        (
            {"require_unregistered_manifest": "yes"},
            "boolean require_unregistered_manifest flag",
        ),
        (
            {"excluded_pathway_ids": "PathBank:SMP9999991"},
            "collection of PathBank:SMP\\[0-9\\]\\+ CURIEs",
        ),
        (
            {"excluded_pathway_ids": ["SMP9999991"]},
            "entries to match PathBank:SMP\\[0-9\\]\\+",
        ),
        (
            {"excluded_pathway_ids": [123]},
            "entries to match PathBank:SMP\\[0-9\\]\\+",
        ),
    ],
)
def test_summarize_pathbank_archive_candidate_frontier_rejects_invalid_filters(
    tmp_path, kwargs, match
):
    path, _ = archive_fixture(tmp_path)
    snapshot_path = tmp_path / "sources.json"
    snapshot_path.write_text(json.dumps({"sources": {}, "terms": {}}), encoding="utf-8")
    with pytest.raises(ValueError, match=match):
        summarize_pathbank_archive_candidate_frontier(
            path,
            [("PW9999999.owl", "SMP9999999")],
            snapshot_path,
            **kwargs,
        )
