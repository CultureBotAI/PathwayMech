from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree

import pytest
import yaml

from pathwaymech.biopax import biopax_to_pathway_record, load_biopax
from pathwaymech.schema import validate_record

FIXTURE = Path("tests/fixtures/biopax/R-TEST.owl")


def test_biopax_converts_to_valid_reactome_record() -> None:
    root = load_biopax(FIXTURE)

    record = validate_record(biopax_to_pathway_record(root, "Reactome:R-TEST"))

    assert record.id == "Reactome:R-TEST-12345"
    assert record.label == "Mini BioPAX glycolysis"
    assert record.taxa == [{"id": "NCBITaxon:12345", "label": "Mini test microbe"}]
    named = {node["id"]: node for node in record.participants}
    assert named["CHEBI:58272"]["label"] == "3-phosphonato-D-glycerate(3-)"
    assert named["UniProtKB:P12345"]["label"] == "Mini enzyme"
    assert named["Reactome:R-TEST-12345/enzyme_complex"]["category"] == "complex"
    before = "Reactome:R-TEST-12345/protein_state_before"
    after = "Reactome:R-TEST-12345/protein_state_after"
    assert before in named and after in named
    assert "UniProtKB:P99999" not in named
    assert record.reactions == [
        {
            "id": "Reactome:R-TEST-67890",
            "label": "phosphoglycerate mutase reaction",
            "direction": "left_to_right",
        }
    ]
    triples = {(e["subject"], e["predicate"], e["object"]) for e in record.mechanistic_edges}
    assert (before, "consumes", "Reactome:R-TEST-67890") in triples
    assert ("Reactome:R-TEST-67890", "produces", after) in triples
    assert ("Reactome:R-TEST-12345/enzyme_complex", "catalyzes", "Reactome:R-TEST-67890") in triples
    assert ("Reactome:R-TEST-12345/enzyme_complex", "has_part", "UniProtKB:P12345") in triples
    assert ("UniProtKB:P12345", "catalyzes", "Reactome:R-TEST-67890") not in triples
    for e in record.mechanistic_edges:
        for evidence in e["evidence"]:
            assert evidence["reference_id"] == record.id
            assert "quote" not in evidence
            assert evidence["source_assertion"]
            assert evidence["source_locator"]
    assert {r["id"] for r in record.references} == {
        "PMID:87654321",
        "PMID:12345678",
        record.id,
    }
    assert record.source_mappings == [
        {
            "subject_id": "UniProt:P12345",
            "subject_label": "Mini enzyme",
            "predicate_id": "skos:exactMatch",
            "object_id": "UniProtKB:P12345",
            "object_label": "Mini enzyme",
            "mapping_justification": "semapv:UnspecifiedMatching",
            "confidence": "1.0",
            "source_pathway_id": "Reactome:R-TEST-12345",
            "source_element_id": "mini_enzyme",
        }
    ]


def test_biopax_seed_yaml_round_trips_as_pathbank_record() -> None:
    root = load_biopax(FIXTURE)
    text = yaml.safe_dump(
        biopax_to_pathway_record(root, "PathBank:SMP0000001"),
        sort_keys=False,
    )

    assert validate_record(yaml.safe_load(text)).id == "PathBank:SMP0000001"
    assert "id: PathBank:SMP0000001/reaction" in text


def test_biopax_accepts_panther_pathway_xrefs() -> None:
    text = FIXTURE.read_text(encoding="utf-8").replace("Reactome", "PANTHER Pathway")

    record = validate_record(
        biopax_to_pathway_record(ElementTree.fromstring(text), "PANTHER:P00001")
    )

    assert record.id == "PANTHER:R-TEST-12345"
    assert record.reactions[0]["id"] == "PANTHER:R-TEST-67890"


def test_biopax_does_not_misattribute_or_truncate_source_comments() -> None:
    long_quote = "a" * 401
    text = FIXTURE.read_text(encoding="utf-8").replace(
        "Mini BioPAX reaction evidence.",
        long_quote,
    )

    record = validate_record(
        biopax_to_pathway_record(ElementTree.fromstring(text), "Reactome:R-TEST")
    )

    evidence = record.mechanistic_edges[0]["evidence"][0]
    assert "quote" not in evidence
    assert evidence["reference_id"] == record.id
    assert long_quote[:50] not in evidence["source_assertion"]


def test_biopax_deduplicates_participants_by_stable_curie() -> None:
    text = FIXTURE.read_text(encoding="utf-8").replace(
        'rdf:resource="#two_pga_xref"',
        'rdf:resource="#three_pga_xref"',
    )

    record = validate_record(
        biopax_to_pathway_record(ElementTree.fromstring(text), "Reactome:R-TEST")
    )

    assert [n["id"] for n in record.participants].count("CHEBI:58272") == 1
    assert any(
        e["object"] == "CHEBI:58272" and e["predicate"] == "produces"
        for e in record.mechanistic_edges
    )


def _native_biopax(direction: str | None = "RIGHT-TO-LEFT") -> ElementTree.Element:
    direction_xml = (
        f"<bp:conversionDirection>{direction}</bp:conversionDirection>"
        if direction is not None
        else ""
    )
    return ElementTree.fromstring(f"""<rdf:RDF
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:bp="http://www.biopax.org/release/biopax-level3.owl#">
      <bp:Pathway rdf:ID="pathway"><bp:displayName>Test</bp:displayName></bp:Pathway>
      <bp:BiochemicalReaction rdf:ID="r">{direction_xml}
        <bp:left rdf:resource="#a"/><bp:right rdf:resource="#b"/>
        <bp:comment>A source annotation is not a paper quotation.</bp:comment>
      </bp:BiochemicalReaction>
      <bp:SmallMolecule rdf:ID="a"><bp:displayName>A</bp:displayName>
        <bp:cellularLocation rdf:resource="#cyto"/></bp:SmallMolecule>
      <bp:SmallMolecule rdf:ID="b"><bp:displayName>B</bp:displayName>
        <bp:cellularLocation rdf:resource="#cyto"/></bp:SmallMolecule>
      <bp:Protein rdf:ID="p"><bp:displayName>Protein subunit</bp:displayName>
        <bp:cellularLocation rdf:resource="#cyto"/></bp:Protein>
      <bp:SmallMolecule rdf:ID="zinc"><bp:displayName>Bound zinc</bp:displayName>
        <bp:cellularLocation rdf:resource="#cyto"/></bp:SmallMolecule>
      <bp:Complex rdf:ID="assembly"><bp:displayName>Metal-dependent enzyme assembly</bp:displayName>
        <bp:component rdf:resource="#p"/><bp:component rdf:resource="#zinc"/>
        <bp:cellularLocation rdf:resource="#cyto"/></bp:Complex>
      <bp:Catalysis rdf:ID="cat"><bp:controller rdf:resource="#assembly"/>
        <bp:controlled rdf:resource="#r"/></bp:Catalysis>
      <bp:CellularLocationVocabulary rdf:ID="cyto"><bp:term>cytosol</bp:term>
        <bp:xref rdf:resource="#go"/></bp:CellularLocationVocabulary>
      <bp:UnificationXref rdf:ID="go"><bp:db>GO</bp:db><bp:id>0005829</bp:id>
      </bp:UnificationXref>
    </rdf:RDF>""")


def test_biopax_reverses_sides_and_preserves_metal_bound_catalyst() -> None:
    record = validate_record(biopax_to_pathway_record(_native_biopax(), "Reactome:R-TEST"))
    triples = {(e["subject"], e["predicate"], e["object"]) for e in record.mechanistic_edges}
    assert ("Reactome:R-TEST/b", "consumes", "Reactome:R-TEST/r") in triples
    assert ("Reactome:R-TEST/r", "produces", "Reactome:R-TEST/a") in triples
    assert ("Reactome:R-TEST/assembly", "catalyzes", "Reactome:R-TEST/r") in triples
    assert ("Reactome:R-TEST/assembly", "has_part", "Reactome:R-TEST/zinc") in triples
    assert ("Reactome:R-TEST/assembly", "has_part", "Reactome:R-TEST/p") in triples
    assert ("Reactome:R-TEST/r", "occurs_in", "GO:0005829") in triples
    assert ("Reactome:R-TEST/p", "catalyzes", "Reactome:R-TEST/r") not in triples
    assert not any(s == "Reactome:R-TEST/zinc" and p == "consumes" for s, p, _ in triples)
    assert record.reactions[0]["direction"] == "right_to_left"


def test_biopax_reversible_conversion_is_explicit() -> None:
    record = biopax_to_pathway_record(_native_biopax("REVERSIBLE"), "Reactome:R-TEST")
    assert record["reactions"][0]["direction"] == "reversible"
    assert any(
        e["subject"] == "Reactome:R-TEST/a" and e["predicate"] == "consumes"
        for e in record["mechanistic_edges"]
    )


def test_biopax_unspecified_direction_is_not_assumed_left_to_right() -> None:
    with pytest.raises(ValueError, match="explicit conversion direction"):
        biopax_to_pathway_record(_native_biopax(None), "Reactome:R-TEST")


def test_biopax_catalysis_direction_is_used_with_its_actual_locator() -> None:
    root = _native_biopax(None)
    catalysis = next(e for e in root if e.tag.endswith("}Catalysis"))
    direction = ElementTree.SubElement(
        catalysis, "{http://www.biopax.org/release/biopax-level3.owl#}catalysisDirection"
    )
    direction.text = "RIGHT-TO-LEFT"
    record = biopax_to_pathway_record(root, "Reactome:R-TEST")
    assert record["reactions"][0]["direction"] == "right_to_left"
    assert (
        "#cat/bp:catalysisDirection"
        in record["mechanistic_edges"][0]["evidence"][0]["source_locator"]
    )


def test_biopax_contextual_direction_controls_orientation_of_reversible_reaction() -> None:
    root = _native_biopax("REVERSIBLE")
    ns = "{http://www.biopax.org/release/biopax-level3.owl#}"
    rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
    step = ElementTree.SubElement(root, ns + "BiochemicalPathwayStep", {rdf + "ID": "step"})
    ElementTree.SubElement(step, ns + "stepConversion", {rdf + "resource": "#r"})
    ElementTree.SubElement(step, ns + "stepDirection").text = "RIGHT-TO-LEFT"
    record = biopax_to_pathway_record(root, "Reactome:R-TEST")
    assert record["reactions"][0]["direction"] == "reversible"
    assert any(
        e["subject"] == "Reactome:R-TEST/b" and e["predicate"] == "consumes"
        for e in record["mechanistic_edges"]
    )
    assert (
        "#step/bp:stepDirection" in record["mechanistic_edges"][0]["evidence"][0]["source_locator"]
    )


def test_biopax_conflicting_explicit_directions_are_not_silently_overridden() -> None:
    root = _native_biopax("RIGHT-TO-LEFT")
    catalysis = next(e for e in root if e.tag.endswith("}Catalysis"))
    ns = "{http://www.biopax.org/release/biopax-level3.owl#}"
    ElementTree.SubElement(catalysis, ns + "catalysisDirection").text = "LEFT-TO-RIGHT"
    with pytest.raises(ValueError, match="contradictory direction"):
        biopax_to_pathway_record(root, "Reactome:R-TEST")


def _add_direction(root, element_name, property_name, direction):
    ns = "{http://www.biopax.org/release/biopax-level3.owl#}"
    element = next(e for e in root if e.tag == ns + element_name)
    ElementTree.SubElement(element, ns + property_name).text = direction


def _add_pathway_step(root, direction):
    ns = "{http://www.biopax.org/release/biopax-level3.owl#}"
    rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
    step = ElementTree.SubElement(root, ns + "BiochemicalPathwayStep", {rdf + "ID": "step"})
    ElementTree.SubElement(step, ns + "stepConversion", {rdf + "resource": "#r"})
    ElementTree.SubElement(step, ns + "stepDirection").text = direction


def test_biopax_catalysis_orients_reversible_conversion_and_preserves_both_sources():
    root = _native_biopax("REVERSIBLE")
    _add_direction(root, "Catalysis", "catalysisDirection", "RIGHT-TO-LEFT")

    record = validate_record(biopax_to_pathway_record(root, "Reactome:R-TEST"))
    assert record.reactions[0]["direction"] == "reversible"
    edge = next(e for e in record.mechanistic_edges if e["predicate"] == "consumes")
    assert edge["subject"] == "Reactome:R-TEST/b"
    evidence = edge["evidence"][0]
    assert "displayed orientation is RIGHT-TO-LEFT" in evidence["source_assertion"]
    assert "#r/bp:conversionDirection" in evidence["source_locator"]
    assert "#cat/bp:catalysisDirection" in evidence["source_locator"]


@pytest.mark.parametrize("conversion", [None, "REVERSIBLE"])
@pytest.mark.parametrize("catalysis", [None, "RIGHT-TO-LEFT"])
def test_biopax_accepts_reversible_pathway_step(conversion, catalysis):
    root = _native_biopax(conversion)
    _add_pathway_step(root, "REVERSIBLE")
    if catalysis:
        _add_direction(root, "Catalysis", "catalysisDirection", catalysis)

    record = validate_record(biopax_to_pathway_record(root, "Reactome:R-TEST"))
    assert record.reactions[0]["direction"] == "reversible"
    edge = next(e for e in record.mechanistic_edges if e["predicate"] == "consumes")
    assert edge["subject"] == f"Reactome:R-TEST/{'b' if catalysis else 'a'}"
    locator = edge["evidence"][0]["source_locator"]
    assert "#step/bp:stepDirection" in locator
    if conversion:
        assert "#r/bp:conversionDirection" in locator
    if catalysis:
        assert "#cat/bp:catalysisDirection" in locator


def test_biopax_rejects_opposing_catalysis_and_pathway_step_orientations():
    root = _native_biopax("REVERSIBLE")
    _add_pathway_step(root, "LEFT-TO-RIGHT")
    _add_direction(root, "Catalysis", "catalysisDirection", "RIGHT-TO-LEFT")
    with pytest.raises(ValueError, match="contradictory direction"):
        biopax_to_pathway_record(root, "Reactome:R-TEST")


def test_biopax_unknown_controller_retains_conversion_and_catalysis_direction():
    root = _native_biopax("REVERSIBLE")
    catalysis = next(e for e in root if e.tag.endswith("}Catalysis"))
    catalysis.remove(next(e for e in catalysis if e.tag.endswith("}controller")))
    _add_direction(root, "Catalysis", "catalysisDirection", "RIGHT-TO-LEFT")

    record = validate_record(biopax_to_pathway_record(root, "Reactome:R-TEST"))
    assert not any(e["predicate"] == "catalyzes" for e in record.mechanistic_edges)
    edge = next(e for e in record.mechanistic_edges if e["predicate"] == "consumes")
    assert edge["subject"] == "Reactome:R-TEST/b"
    assert "#cat/bp:catalysisDirection" in edge["evidence"][0]["source_locator"]


@pytest.mark.parametrize("resource", [None, "#missing", "#r"])
def test_biopax_explicit_unresolved_controller_still_fails(resource):
    root = _native_biopax()
    controller = next(e for e in root.iter() if e.tag.endswith("}controller"))
    controller.attrib.clear()
    if resource is not None:
        controller.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", resource)
    with pytest.raises(ValueError, match="unresolved controller"):
        biopax_to_pathway_record(root, "Reactome:R-TEST")


@pytest.mark.parametrize("kind, category", [
    ("Rna", "rna"), ("RnaRegion", "rna"), ("Dna", "dna"), ("DnaRegion", "dna"),
    ("SmallMolecule", "small_molecule"), ("PhysicalEntity", None),
])
def test_biopax_physical_catalyst_is_not_restricted_to_protein(kind, category):
    root = _native_biopax()
    ns = "{http://www.biopax.org/release/biopax-level3.owl#}"
    rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
    catalyst = ElementTree.SubElement(root, ns + kind, {rdf + "ID": "catalyst"})
    ElementTree.SubElement(catalyst, ns + "displayName").text = "Source-supported catalyst"
    controller = next(e for e in root.iter() if e.tag.endswith("}controller"))
    controller.set(rdf + "resource", "#catalyst")

    record = validate_record(biopax_to_pathway_record(root, "Reactome:R-TEST"))
    node = next(n for n in record.participants if n["id"] == "Reactome:R-TEST/catalyst")
    assert node.get("category") == category
    edge = next(e for e in record.mechanistic_edges if e["predicate"] == "catalyzes")
    assert edge["subject"] == node["id"]
    assert edge["object"] == "Reactome:R-TEST/r"
    assert "#cat/bp:controller/#catalyst" in edge["evidence"][0]["source_locator"]
