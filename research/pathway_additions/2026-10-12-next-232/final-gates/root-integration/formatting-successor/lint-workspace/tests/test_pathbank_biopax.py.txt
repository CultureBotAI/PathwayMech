"""Synthetic PathBank-shaped exports; raw third-party data remains external."""

from __future__ import annotations

import copy
from xml.etree import ElementTree as ET

import pytest

from pathwaymech.biopax import biopax_to_pathway_record
from pathwaymech.schema import validate_record

BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


def _fixture():
    root = ET.Element(RDF + "RDF")

    def node(kind, native, **values):
        element = ET.SubElement(root, BP + kind, {RDF + "ID": native})
        for key, value in values.items():
            ET.SubElement(element, BP + key).text = value
        return element

    def link(element, key, target):
        ET.SubElement(element, BP + key, {RDF + "resource": "#" + target})

    def xref(native, db, accession):
        return node("UnificationXref", native, db=db, id=accession)

    pathway = node("Pathway", "pathway", displayName="Synthetic microbial cycle")
    pathway.attrib = {RDF + "about": "http://identifiers.org/smpdb/SMP9999999"}
    link(pathway, "xref", "pathwhiz")
    link(pathway, "xref", "smpdb")
    link(pathway, "organism", "taxon")
    link(pathway, "pathwayComponent", "reaction")
    xref("pathwhiz", "PathWhiz", "PW123456")
    xref("smpdb", "SMPDB", "SMP9999999")
    reaction = node("BiochemicalReaction", "reaction", conversionDirection="LEFT_TO_RIGHT")
    link(reaction, "left", "substrate")
    link(reaction, "right", "product")
    for name, identifier in (("substrate", "CHEBI:15377"), ("product", "CHEBI:15378")):
        physical = node("SmallMolecule", name, displayName="Source " + name)
        link(physical, "entityReference", name + "_ref")
        reference = node("SmallMoleculeReference", name + "_ref")
        link(reference, "xref", "ignored")
        link(reference, "xref", name + "_chebi")
        xref(name + "_chebi", "ChEBI", identifier)
    xref("ignored", "Unrecognized database", "native-value")
    protein = node("Protein", "protein", displayName="Source enzyme subunit")
    link(protein, "entityReference", "protein_ref")
    reference = node("ProteinReference", "protein_ref")
    link(reference, "xref", "ignored")
    link(reference, "xref", "uniprot")
    xref("uniprot", "UniProt", "P12345")
    complex_node = node("Complex", "complex", displayName="Source enzyme assembly")
    link(complex_node, "component", "protein")
    catalyst = node("Catalysis", "catalysis")
    link(catalyst, "controller", "complex")
    link(catalyst, "controlled", "reaction")
    taxon = node("BioSource", "taxon", displayName="Source microbe")
    link(taxon, "xref", "taxonomy")
    xref("taxonomy", "TAXONOMY", "12345")
    return root


def _native(root, native):
    return next(e for e in root if e.get(RDF + "ID") == native)


def test_pathbank_keeps_native_accession_taxon_and_all_direct_reference_xrefs():
    record = biopax_to_pathway_record(_fixture(), "PathBank:PW123456")
    validate_record(record)
    assert record["id"] == "PathBank:SMP9999999"
    assert record["label"] == "Synthetic microbial cycle"
    assert record["taxa"] == [{"id": "NCBITaxon:12345", "label": "Source microbe"}]
    nodes = {p["id"]: p for p in record["participants"]}
    assert set(nodes) == {
        "CHEBI:15377",
        "CHEBI:15378",
        "UniProtKB:P12345",
        "PathBank:SMP9999999/complex",
    }
    assert nodes["CHEBI:15377"]["label"] == "Source substrate"
    assert nodes["UniProtKB:P12345"]["label"] == "Source enzyme subunit"
    edges = {(e["subject"], e["predicate"], e["object"]) for e in record["mechanistic_edges"]}
    assert ("PathBank:SMP9999999/complex", "catalyzes", "PathBank:SMP9999999/reaction") in edges
    assert ("UniProtKB:P12345", "catalyzes", "PathBank:SMP9999999/reaction") not in edges
    assert len(record["reactions"]) == 1
    assert len(record["mechanistic_edges"]) == 4
    assert all("PW123456" not in p["id"] for p in record["participants"])


@pytest.mark.parametrize(
    "spelling,direction,reactant",
    [
        ("LEFT_TO_RIGHT", "left_to_right", "CHEBI:15377"),
        ("RIGHT_TO_LEFT", "right_to_left", "CHEBI:15378"),
        ("REVERSIBLE", "reversible", "CHEBI:15377"),
    ],
)
def test_pathbank_direction_variants_preserve_orientation_and_original_spelling(
    spelling, direction, reactant
):
    root = _fixture()
    _native(root, "reaction").find(BP + "conversionDirection").text = spelling
    record = biopax_to_pathway_record(root, "PathBank:PW123456")
    assert record["reactions"][0]["direction"] == direction
    role_edges = [
        e for e in record["mechanistic_edges"] if e["predicate"] in {"consumes", "produces"}
    ]
    assert next(e for e in role_edges if e["predicate"] == "consumes")["subject"] == reactant
    for edge in role_edges:
        evidence = edge["evidence"][0]
        assert spelling in evidence["source_assertion"]
        assert "#reaction/bp:conversionDirection" in evidence["source_locator"]
        assert "quote" not in evidence


@pytest.mark.parametrize("source", ["Reactome", "PANTHER"])
def test_underscore_spelling_is_not_relaxed_for_other_sources(source):
    with pytest.raises(ValueError, match="invalid conversion direction"):
        biopax_to_pathway_record(_fixture(), source + ":example")


def test_unknown_pathbank_direction_still_rejected():
    root = _fixture()
    _native(root, "reaction").find(BP + "conversionDirection").text = "FORWARD"
    with pytest.raises(ValueError, match="invalid conversion direction"):
        biopax_to_pathway_record(root, "PathBank:PW123456")


def test_native_smpdb_id_never_comes_from_pathwhiz_or_filename():
    root = _fixture()
    # In a generic fixture lacking a source URI or SMPDB assertion, retain its
    # explicit fallback verbatim; never derive an SMP accession from a PW ID.
    root.find(BP + "Pathway").attrib = {RDF + "ID": "pathway"}
    _native(root, "smpdb").find(BP + "db").text = "Unknown"
    record = biopax_to_pathway_record(root, "PathBank:PW123456")
    assert record["id"] == "PathBank:PW123456"
    assert "SMP123456" not in str(record)


def test_smpdb_uri_disagreement_is_explicit():
    root = _fixture()
    _native(root, "smpdb").find(BP + "id").text = "SMP9999998"
    with pytest.raises(ValueError, match="URI and SMPDB xref must agree"):
        biopax_to_pathway_record(root, "PathBank:PW123456")


def test_multiple_native_pathways_are_not_silently_collapsed():
    root = _fixture()
    other = copy.deepcopy(root.find(BP + "Pathway"))
    other.set(RDF + "about", "http://identifiers.org/smpdb/SMP9999998")
    root.append(other)
    with pytest.raises(ValueError, match="exactly one native Pathway"):
        biopax_to_pathway_record(root, "PathBank:PW123456")


@pytest.mark.parametrize(
    "reference,xref,message",
    [
        ("substrate_ref", "product_chebi", "conflicting CHEBI"),
        ("protein_ref", "other_uniprot", "conflicting UniProtKB"),
    ],
)
def test_conflicting_expected_entity_xrefs_are_not_selected_by_order(reference, xref, message):
    root = _fixture()
    extra = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "other_uniprot"})
    ET.SubElement(extra, BP + "db").text = "UniProt"
    ET.SubElement(extra, BP + "id").text = "P99999"
    ET.SubElement(_native(root, reference), BP + "xref", {RDF + "resource": "#" + xref})
    with pytest.raises(ValueError, match=message):
        biopax_to_pathway_record(root, "PathBank:PW123456")


def test_reference_xref_selection_does_not_use_wrong_entity_namespace():
    root = _fixture()
    reference = _native(root, "substrate_ref")
    reference.clear()
    reference.set(RDF + "ID", "substrate_ref")
    ET.SubElement(reference, BP + "xref", {RDF + "resource": "#uniprot"})
    record = biopax_to_pathway_record(root, "PathBank:PW123456")
    assert "PathBank:SMP9999999/substrate" in {p["id"] for p in record["participants"]}
    assert (
        next(e for e in record["mechanistic_edges"] if e["predicate"] == "consumes")["subject"]
        == "PathBank:SMP9999999/substrate"
    )


@pytest.mark.parametrize("accession", ["12345", "99999"])
def test_pathbank_taxon_xrefs_require_one_distinct_supported_id(accession):
    root = _fixture()
    extra = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "other_taxonomy"})
    ET.SubElement(extra, BP + "db").text = "NCBI Taxonomy"
    ET.SubElement(extra, BP + "id").text = accession
    ET.SubElement(_native(root, "taxon"), BP + "xref", {RDF + "resource": "#other_taxonomy"})
    if accession == "99999":
        with pytest.raises(ValueError, match="taxon has conflicting NCBITaxon"):
            biopax_to_pathway_record(root, "PathBank:PW123456")
    else:
        record = biopax_to_pathway_record(root, "PathBank:PW123456")
        assert record["taxa"] == [{"id": "NCBITaxon:12345", "label": "Source microbe"}]


@pytest.mark.parametrize("add_orphan_step", [False, True])
def test_pathbank_rejects_orphan_reaction_even_when_an_unattached_step_references_it(
    add_orphan_step,
):
    root = _fixture()
    other = copy.deepcopy(_native(root, "reaction"))
    other.set(RDF + "ID", "orphan_reaction")
    root.append(other)
    if add_orphan_step:
        step = ET.SubElement(root, BP + "BiochemicalPathwayStep", {RDF + "ID": "orphan_step"})
        ET.SubElement(step, BP + "stepConversion", {RDF + "resource": "#orphan_reaction"})
    with pytest.raises(ValueError, match="lack explicit pathway membership: orphan_reaction"):
        biopax_to_pathway_record(root, "PathBank:PW123456")


@pytest.mark.parametrize(
    "step_kind,relation,target",
    [
        (None, "pathwayComponent", "catalysis"),
        ("BiochemicalPathwayStep", "stepConversion", "reaction"),
        ("BiochemicalPathwayStep", "stepProcess", "catalysis"),
        ("PathwayStep", "stepProcess", "reaction"),
        ("PathwayStep", "stepProcess", "catalysis"),
    ],
)
def test_pathbank_accepts_explicit_attached_membership_without_inventing_order(
    step_kind, relation, target
):
    root = _fixture()
    expected = biopax_to_pathway_record(root, "PathBank:PW123456")
    pathway = root.find(BP + "Pathway")
    pathway.remove(pathway.find(BP + "pathwayComponent"))
    parent = pathway
    if step_kind:
        parent = ET.SubElement(root, BP + step_kind, {RDF + "ID": "attached_step"})
        ET.SubElement(pathway, BP + "pathwayOrder", {RDF + "resource": "#attached_step"})
    ET.SubElement(parent, BP + relation, {RDF + "resource": "#" + target})
    assert biopax_to_pathway_record(root, "PathBank:PW123456") == expected


def test_pathbank_rejects_dangling_membership_reference():
    root = _fixture()
    pathway = root.find(BP + "Pathway")
    ET.SubElement(pathway, BP + "pathwayOrder", {RDF + "resource": "#missing_step"})
    with pytest.raises(ValueError, match="unresolved membership reference missing_step"):
        biopax_to_pathway_record(root, "PathBank:PW123456")


@pytest.mark.parametrize("source", ["Reactome", "PANTHER"])
def test_other_sources_keep_existing_membership_and_taxon_behavior(source):
    root = _fixture()
    _native(root, "reaction").find(BP + "conversionDirection").text = "LEFT-TO-RIGHT"
    pathway = root.find(BP + "Pathway")
    pathway.remove(pathway.find(BP + "pathwayComponent"))
    _native(root, "taxonomy").find(BP + "db").text = "NCBI Taxonomy"
    extra = ET.SubElement(root, BP + "UnificationXref", {RDF + "ID": "other_taxonomy"})
    ET.SubElement(extra, BP + "db").text = "NCBI Taxonomy"
    ET.SubElement(extra, BP + "id").text = "99999"
    ET.SubElement(_native(root, "taxon"), BP + "xref", {RDF + "resource": "#other_taxonomy"})
    record = biopax_to_pathway_record(root, source + ":example")
    assert len(record["reactions"]) == 1
    assert record["taxa"] == [{"id": "NCBITaxon:12345", "label": "Source microbe"}]


@pytest.mark.parametrize(
    "source,attached,reactant",
    [
        ("PathBank", False, "CHEBI:15377"),
        ("PathBank", True, "CHEBI:15378"),
        ("Reactome", False, "CHEBI:15378"),
        ("PANTHER", False, "CHEBI:15378"),
    ],
)
def test_pathbank_contextual_step_direction_requires_pathway_attachment(source, attached, reactant):
    root = _fixture()
    _native(root, "reaction").find(BP + "conversionDirection").text = "REVERSIBLE"
    step = ET.SubElement(root, BP + "BiochemicalPathwayStep", {RDF + "ID": "context_step"})
    ET.SubElement(step, BP + "stepConversion", {RDF + "resource": "#reaction"})
    ET.SubElement(step, BP + "stepDirection").text = "RIGHT-TO-LEFT"
    if attached:
        ET.SubElement(
            root.find(BP + "Pathway"), BP + "pathwayOrder", {RDF + "resource": "#context_step"}
        )
    record = biopax_to_pathway_record(root, source + ":PW123456")
    assert record["reactions"][0]["direction"] == "reversible"
    consumes = next(edge for edge in record["mechanistic_edges"] if edge["predicate"] == "consumes")
    assert consumes["subject"] == reactant
    includes_step = "#context_step/bp:stepDirection" in consumes["evidence"][0]["source_locator"]
    assert includes_step == (attached or source != "PathBank")
