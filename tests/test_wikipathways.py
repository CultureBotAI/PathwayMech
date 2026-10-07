from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree

import yaml

from pathwaymech.chebi import load_chebi_xrefs
from pathwaymech.schema import validate_record
from pathwaymech.wikipathways import (
    gpml_to_pathway_record,
    load_gpml_pathway,
    wikipathways_fallback_id,
)

FIXTURE = Path("tests/fixtures/wikipathways/WPTEST.gpml")
CHEBI_FIXTURE = Path("tests/fixtures/chebi/kegg_compounds.obo")


def test_gpml_converts_to_valid_pathway_record() -> None:
    root = load_gpml_pathway(FIXTURE)

    record = validate_record(gpml_to_pathway_record(root, "WikiPathways:WPTEST"))

    assert record.id == "WikiPathways:WP9999"
    assert record.label == "Mini glycolysis"
    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "CHEBI:58289", "label": "2-phosphonato-D-glycerate(3-)"},
        {"id": "UniProtKB:P12345", "label": "Mini enzyme"},
        {"id": "SGD:S000000001", "label": "Mini SGD enzyme"},
        {"id": "CAS:98-92-0", "label": "Nicotinamide"},
        {"id": "CHEBI:15377", "label": "H2O"},
        {"id": "LIPIDMAPS:LMFA01010001", "label": "ATP"},
        {"id": "CHEBI:456215", "label": "AMP"},
    ]
    assert record.reactions == [
        {
            "id": "WikiPathways:WP9999/interaction",
            "label": "WikiPathways:WP9999 interaction interaction",
            "direction": "left_to_right",
        },
        {
            "id": "WikiPathways:WP9999/anchored",
            "label": "WikiPathways:WP9999 interaction anchored",
            "direction": "left_to_right",
        },
    ]
    assert [
        (edge["subject"], edge["predicate"], edge["object"]) for edge in record.mechanistic_edges
    ] == [
        ("CHEBI:58272", "consumes", "WikiPathways:WP9999/interaction"),
        ("WikiPathways:WP9999/interaction", "produces", "CHEBI:58289"),
        ("CAS:98-92-0", "consumes", "WikiPathways:WP9999/anchored"),
        ("WikiPathways:WP9999/anchored", "produces", "CHEBI:456215"),
        ("CHEBI:15377", "consumes", "WikiPathways:WP9999/anchored"),
        ("LIPIDMAPS:LMFA01010001", "consumes", "WikiPathways:WP9999/anchored"),
        ("SGD:S000000001", "catalyzes", "WikiPathways:WP9999/anchored"),
    ]
    assert record.references == [
        {"id": "PMID:12345678", "title": "WikiPathways publication PMID:12345678"},
        {"id": "WikiPathways:WP9999", "title": "WikiPathways source pathway WikiPathways:WP9999"},
    ]


def test_gpml_seed_yaml_round_trips_as_pathway_record() -> None:
    root = load_gpml_pathway(FIXTURE)
    text = yaml.safe_dump(
        gpml_to_pathway_record(root, "WikiPathways:WPTEST"),
        sort_keys=False,
    )

    assert validate_record(yaml.safe_load(text)).id == "WikiPathways:WP9999"


def test_gpml_deduplicates_participants_by_stable_curie() -> None:
    text = FIXTURE.read_text(encoding="utf-8").replace(
        'ID="58289"',
        'ID="CHEBI:58272"',
    )

    record = validate_record(
        gpml_to_pathway_record(ElementTree.fromstring(text), "WikiPathways:WPTEST")
    )

    assert record.participants == [
        {"id": "CHEBI:58272", "label": "3-phosphonato-D-glycerate(3-)"},
        {"id": "UniProtKB:P12345", "label": "Mini enzyme"},
        {"id": "SGD:S000000001", "label": "Mini SGD enzyme"},
        {"id": "CAS:98-92-0", "label": "Nicotinamide"},
        {"id": "CHEBI:15377", "label": "H2O"},
        {"id": "LIPIDMAPS:LMFA01010001", "label": "ATP"},
        {"id": "CHEBI:456215", "label": "AMP"},
    ]
    assert record.mechanistic_edges[1]["object"] == "CHEBI:58272"


def test_wikipathways_fallback_id_uses_filename_accession() -> None:
    assert (
        wikipathways_fallback_id(Path("Sc_NAD_salvage_pathway_V_WP171_20260901.gpml"))
        == "WikiPathways:WP171"
    )


def test_gpml_can_map_kegg_compound_xrefs_to_chebi() -> None:
    root = ElementTree.fromstring(
        """
        <Pathway xmlns="http://pathvisio.org/GPML/2013a" Name="KEGG compound">
          <DataNode TextLabel="2PG" GraphId="source" Type="Metabolite">
            <Xref Database="KEGG Compound" ID="C00197" />
          </DataNode>
          <DataNode TextLabel="ATP" GraphId="target" Type="Metabolite">
            <Xref Database="LIPID MAPS" ID="LMFA01010001" />
          </DataNode>
          <Interaction GraphId="interaction">
            <Graphics ConnectorType="Straight">
              <Point GraphRef="source" />
              <Point GraphRef="target" ArrowHead="Arrow" />
            </Graphics>
          </Interaction>
        </Pathway>
        """
    )

    record = validate_record(
        gpml_to_pathway_record(
            root,
            "WikiPathways:WPTEST",
            load_chebi_xrefs(CHEBI_FIXTURE),
        )
    )

    assert record.participants == [
        {"id": "CHEBI:58289", "label": "2PG"},
        {"id": "LIPIDMAPS:LMFA01010001", "label": "ATP"},
    ]
    assert record.source_mappings == [
        {
            "subject_id": "KEGG:C00197",
            "subject_label": "2PG",
            "predicate_id": "skos:exactMatch",
            "object_id": "CHEBI:58289",
            "object_label": "2-phosphonato-D-glycerate(3-)",
            "mapping_justification": "semapv:UnspecifiedMatching",
            "confidence": "1.0",
            "source_pathway_id": "WikiPathways:WPTEST",
            "source_element_id": "source",
        }
    ]


def test_gpml_can_keep_xrefs_from_leftover_microbial_maps() -> None:
    root = ElementTree.fromstring(
        """
        <Pathway xmlns="http://pathvisio.org/GPML/2013a" Name="leftover xrefs">
          <DataNode TextLabel="hmdb" GraphId="hmdb" Type="Metabolite">
            <Xref Database="HMDB" ID="HMDB0000902" />
          </DataNode>
          <DataNode TextLabel="cas" GraphId="cas" Type="Metabolite">
            <Xref Database="CAS" ID="98-92-0" />
          </DataNode>
          <DataNode TextLabel="chemspider" GraphId="chemspider" Type="Metabolite">
            <Xref Database="Chemspider" ID="555" />
          </DataNode>
          <DataNode TextLabel="pubchem" GraphId="pubchem" Type="Metabolite">
            <Xref Database="PubChem-compound" ID="647" />
          </DataNode>
          <DataNode TextLabel="ensembl" GraphId="ensembl" Type="GeneProduct">
            <Xref Database="Ensembl" ID="b0639" />
          </DataNode>
          <DataNode TextLabel="entrez" GraphId="entrez" Type="GeneProduct">
            <Xref Database="Entrez Gene" ID="812223" />
          </DataNode>
          <DataNode TextLabel="tuberculist" GraphId="tuberculist" Type="GeneProduct">
            <Xref Database="TubercuList" ID="Rv1905c" />
          </DataNode>
          <DataNode TextLabel="ncbi protein" GraphId="ncbi-protein" Type="Protein">
            <Xref Database="NCBI Protein" ID="NP_215282" />
          </DataNode>
        </Pathway>
        """
    )

    record = validate_record(gpml_to_pathway_record(root, "WikiPathways:WPTEST"))

    assert record.participants == [
        {"id": "HMDB:HMDB0000902", "label": "hmdb"},
        {"id": "CAS:98-92-0", "label": "cas"},
        {"id": "ChemSpider:555", "label": "chemspider"},
        {"id": "PubChem:647", "label": "pubchem"},
        {"id": "Ensembl:b0639", "label": "ensembl"},
        {"id": "Entrez:812223", "label": "entrez"},
        {"id": "TubercuList:Rv1905c", "label": "tuberculist"},
        {"id": "NCBIProtein:NP_215282", "label": "ncbi protein"},
    ]


def test_gpml_can_map_native_chemical_xrefs_to_chebi() -> None:
    root = ElementTree.fromstring(
        """
        <Pathway xmlns="http://pathvisio.org/GPML/2013a" Name="chemical xrefs">
          <DataNode TextLabel="hmdb" GraphId="hmdb" Type="Metabolite">
            <Xref Database="HMDB" ID="HMDB0000902" />
          </DataNode>
          <DataNode TextLabel="cas" GraphId="cas" Type="Metabolite">
            <Xref Database="CAS" ID="98-92-0" />
          </DataNode>
          <DataNode TextLabel="chemspider" GraphId="chemspider" Type="Metabolite">
            <Xref Database="Chemspider" ID="555" />
          </DataNode>
          <DataNode TextLabel="pubchem" GraphId="pubchem" Type="Metabolite">
            <Xref Database="PubChem-compound" ID="647" />
          </DataNode>
        </Pathway>
        """
    )

    record = validate_record(
        gpml_to_pathway_record(root, "WikiPathways:WPTEST", load_chebi_xrefs(CHEBI_FIXTURE))
    )

    assert record.participants == [{"id": "CHEBI:17154", "label": "hmdb"}]


def _native_gpml(interactions: str) -> ElementTree.Element:
    return ElementTree.fromstring(f"""<Pathway xmlns="http://pathvisio.org/GPML/2013a">
      <DataNode GraphId="a" TextLabel="substrate" Type="Metabolite">
        <Xref Database="ChEBI" ID="15377"/></DataNode>
      <DataNode GraphId="b" TextLabel="product" Type="Metabolite">
        <Xref Database="ChEBI" ID="15378"/></DataNode>
      <DataNode GraphId="enzyme" TextLabel="enzyme" Type="Protein">
        <Xref Database="UniProt" ID="P12345"/></DataNode>
      <DataNode GraphId="metal" TextLabel="zinc" Type="Metabolite">
        <Xref Database="ChEBI" ID="29105"/></DataNode>
      {interactions}</Pathway>""")


def test_gpml_reversible_and_right_to_left_are_not_two_products() -> None:
    for first_arrow, second_arrow, direction, substrate, product in [
        ("Arrow", "Arrow", "reversible", "CHEBI:15377", "CHEBI:15378"),
        ("Arrow", "Line", "right_to_left", "CHEBI:15378", "CHEBI:15377"),
    ]:
        root = _native_gpml(f'''<Interaction GraphId="r"><Graphics>
          <Point GraphRef="a" ArrowHead="{first_arrow}"/>
          <Point GraphRef="b" ArrowHead="{second_arrow}"/>
        </Graphics></Interaction>''')
        record = gpml_to_pathway_record(root, "WikiPathways:WP9999")
        assert record["reactions"][0]["direction"] == direction
        assert {
            (e["subject"], e["predicate"], e["object"]) for e in record["mechanistic_edges"]
        } == {
            (substrate, "consumes", "WikiPathways:WP9999/r"),
            ("WikiPathways:WP9999/r", "produces", product),
        }


def test_gpml_inhibition_is_not_a_product_and_orphan_anchor_is_not_a_reaction() -> None:
    root = _native_gpml("""<Interaction GraphId="inhibition"><Graphics>
      <Point GraphRef="a"/><Point GraphRef="b" ArrowHead="mim-inhibition"/>
      <Anchor GraphId="anchor"/></Graphics></Interaction>
      <Interaction GraphId="controller"><Graphics><Point GraphRef="enzyme"/>
      <Point GraphRef="anchor" ArrowHead="mim-catalysis"/></Graphics></Interaction>""")
    record = gpml_to_pathway_record(root, "WikiPathways:WP9999")
    assert record["reactions"] == []
    assert record["mechanistic_edges"] == []


def test_gpml_native_unknown_metabolite_and_anchored_cofactor_survive() -> None:
    root = _native_gpml("""
      <DataNode GraphId="unmapped" TextLabel="source-local muropeptide" Type="Metabolite"/>
      <Interaction GraphId="r"><Graphics><Point GraphRef="unmapped"/>
      <Point GraphRef="b" ArrowHead="Arrow"/><Anchor GraphId="anchor"/>
      </Graphics></Interaction>
      <Interaction GraphId="water"><Graphics><Point GraphRef="a"/>
      <Point GraphRef="anchor" ArrowHead="Arrow"/></Graphics></Interaction>
      <Interaction GraphId="metal-support"><Graphics><Point GraphRef="metal"/>
      <Point GraphRef="anchor" ArrowHead="mim-catalysis"/></Graphics></Interaction>""")
    record = validate_record(gpml_to_pathway_record(root, "WikiPathways:WP9999"))
    triples = {(e["subject"], e["predicate"], e["object"]) for e in record.mechanistic_edges}
    assert ("WikiPathways:WP9999/unmapped", "consumes", "WikiPathways:WP9999/r") in triples
    assert ("CHEBI:15377", "consumes", "WikiPathways:WP9999/r") in triples
    assert ("CHEBI:29105", "enables", "WikiPathways:WP9999/r") in triples
    assert not any(s == "CHEBI:29105" and p == "catalyzes" for s, p, _ in triples)
    for edge in record.mechanistic_edges:
        assert edge["evidence"][0]["reference_id"] == record.id
        assert "source_locator" in edge["evidence"][0]
        assert "quote" not in edge["evidence"][0]
