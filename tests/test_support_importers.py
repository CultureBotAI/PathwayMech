from __future__ import annotations

import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

from pathwaymech.bigg import bigg_reactions, bigg_seed_rows, load_bigg_model
from pathwaymech.bvbrc import bvbrc_seed_rows, load_bvbrc_pathways
from pathwaymech.dbcan import dbcan_pul_seed_rows, load_dbcan_pul
from pathwaymech.gapmind import gapmind_seed_rows, load_gapmind_steps
from pathwaymech.go import go_seed_rows, load_go_obo
from pathwaymech.modelseed import load_modelseed_tsv, modelseed_seed_rows
from pathwaymech.unipathway import load_unipathway_obo, unipathway_seed_rows
from pathwaymech.veupathdb import load_veupathdb_pathways, veupathdb_seed_rows


def test_go_obo_seed_rows_skip_obsolete_terms() -> None:
    terms = load_go_obo(Path("tests/fixtures/go/go.obo"))

    assert go_seed_rows(terms) == [
        "go_id\tname\tnamespace",
        "GO:0061620\tglycolytic process through glucose-6-phosphate\tbiological_process",
    ]


def test_modelseed_reaction_seed_rows() -> None:
    reactions = load_modelseed_tsv(Path("tests/fixtures/modelseed/reactions.tsv"))

    assert modelseed_seed_rows(reactions) == [
        "modelseed_id\tequation\tec_numbers\taliases",
        "ModelSEED:rxn00001\t(1) cpd00001 = (1) cpd00067\t1.1.1.1\tKEGG:R00001",
    ]


def test_bigg_reaction_seed_rows() -> None:
    reactions = bigg_reactions(load_bigg_model(Path("tests/fixtures/bigg/model.json")))

    assert bigg_seed_rows(reactions) == [
        "model_id\treaction_id\tname\tgene_reaction_rule",
        "BiGG:iJO1366\tBiGG:PGK\tphosphoglycerate kinase\tb2926",
    ]


def test_bvbrc_pathway_seed_rows() -> None:
    calls = load_bvbrc_pathways(Path("tests/fixtures/bvbrc/pathways.tsv"))

    assert bvbrc_seed_rows(calls) == [
        "genome_id\tgene_id\tec_number\tpathway_id\tpathway_name",
        "562.1\tfig|562.1.peg.1\tEC:2.7.2.3\tKEGG:map00010\t"
        "Glycolysis / Gluconeogenesis",
    ]


def test_veupathdb_pathway_seed_rows() -> None:
    calls = load_veupathdb_pathways(Path("tests/fixtures/veupathdb/pathways.tsv"))

    assert veupathdb_seed_rows(calls) == [
        (
            "component_site\torganism\tgene_id\tgene_product\tpathway_source\t"
            "pathway_id\tpathway_name\tec_number\texact_match\treaction_count"
        ),
        (
            "PlasmoDB\tPlasmodium falciparum 3D7\tPF3D7_1133400\t"
            "phosphoglycerate kinase\tKEGG\tKEGG:ec00010\t"
            "Glycolysis / Gluconeogenesis\tEC:2.7.2.3\tYes\t1"
        ),
    ]


def test_gapmind_step_seed_rows() -> None:
    elements = load_gapmind_steps(Path("tests/fixtures/gapmind/aa/thr.steps"))

    assert gapmind_seed_rows(elements) == [
        (
            "family\tpathway_slug\telement_id\telement_type\tdescription\tec_numbers\t"
            "uniprot_ids\tmetacyc_ids\thmm_ids\tother_identifiers\t"
            "ignored_identifiers\timports\tcomponents"
        ),
        "aa\tthr\tphosphohomoserine\timport\t\t\t\t\t\t\t\tmet.steps:phosphohomoserine\t",
        (
            "aa\tthr\tthrC\tstep\tthreonine synthase\tEC:4.2.3.1\t"
            "UniProtKB:A0A000|UniProtKB:Q935V6\tMetaCyc:RXN-1\tTIGR00001\t"
            "reanno:sample:locus\tUniProtKB:P11111|EC:1.2.3.4\t\t"
        ),
        "aa\tthr\tall\tvariant\t\t\t\t\t\t\t\t\tphosphohomoserine|thrC",
    ]


def test_unipathway_obo_seed_rows() -> None:
    terms = load_unipathway_obo(Path("tests/fixtures/unipathway/upa.obo"))

    assert unipathway_seed_rows(terms) == [
        (
            "unipathway_id\tterm_type\tname\txrefs\tparents\tpart_ofs\t"
            "input_compounds\toutput_compounds"
        ),
        (
            "UPa:UCR99999\treaction\tsubstrate = product\t"
            "KEGG:R99999|MetaCyc:RXN-99999|RHEA:99999\t\tUPa:UER99999\t"
            "UPa:UPC99998\tUPa:UPC99999"
        ),
        (
            "UPa:UER99999\tenzymatic_reaction\tproduct from substrate: step 1/1\t"
            "EC:1.1.1.1|GO:0004022\t\tUPa:ULS99999\t"
            "UPa:UPC99998\tUPa:UPC99999"
        ),
        (
            "UPa:ULS99999\tlinear_sub_pathway\tproduct from substrate\t\t\t"
            "UPa:UPA99999\tUPa:UPC99998\tUPa:UPC99999"
        ),
        (
            "UPa:UPA99999\tpathway\tsynthetic product biosynthesis\t\t"
            "UPa:UPA00001\t\t\t"
        ),
        "UPa:UPC99999\tcompound\tproduct\tCHEBI:99999\t\t\t\t",
    ]


def test_dbcan_pul_seed_rows() -> None:
    records = load_dbcan_pul(Path("tests/fixtures/dbcan/dbcan-pul.tsv"))

    assert dbcan_pul_seed_rows(records) == [
        (
            "dbcan_pul_id\tpmids\torganism\tncbi_taxon_id\tgenomic_accession\t"
            "nucleotide_range\tsubstrate\tmode\tverification_methods\tgene_loci\t"
            "cazyme_families\tnum_cazymes\tnum_genes"
        ),
        (
            "PUL0001\tPMID:30796211\tRoseburia intestinalis\tNCBITaxon:166486\t"
            "NZ_GG692714.1\t156723-175880\tbeta-mannan\tdegradation\t"
            "RNA-Seq|substrate binding assay|enzyme activity assay|mass spectrometry\t"
            "ROSINTL182_05469-ROSINTL182_05483\t"
            "GH1|CE2|GH130|GH36|GH113\t7\t15"
        ),
        (
            "PUL0003\tPMID:26559526|PMID:26827771\tBacillus subtilis\t"
            "NCBITaxon:1423\tNC_000964\t1942714-1945654\txylan\tdegradation\t"
            "RT-PCR\txynCD\tGH30|GH30_8|GH43_16|CBM6\t2\t2"
        ),
    ]


def test_dbcan_pul_xlsx_reader_preserves_blank_cells(tmp_path: Path) -> None:
    path = tmp_path / "dbcan-pul.xlsx"
    _write_xlsx(
        path,
        [
            [
                "ID",
                "PMID",
                "notes",
                "verification_final",
                "genomic_accession_number",
                "organism_name",
                "ncbi_species_tax_id",
                "substrate_final",
                "cazymes_predicted_dbcan",
            ],
            [
                "PUL0004",
                "26827771",
                "",
                "enzyme activity assay,substrate binding assay",
                "KM624528.1",
                "uncultured bacterium",
                "77133",
                "beta-glucan",
                "GH1",
            ],
        ],
    )

    record = load_dbcan_pul(path)[0]

    assert record.id == "PUL0004"
    assert record.verification_methods == (
        "enzyme activity assay",
        "substrate binding assay",
    )
    assert record.genomic_accession == "KM624528.1"


def _write_xlsx(path: Path, rows: list[list[str]]) -> None:
    string_indexes: dict[str, int] = {}
    sheet_rows = []
    for row_index, row in enumerate(rows, start=1):
        cells = []
        for column_index, value in enumerate(row):
            if value == "":
                continue
            string_index = string_indexes.setdefault(value, len(string_indexes))
            cells.append(
                f'<c r="{_column_ref(column_index)}{row_index}" t="s">'
                f"<v>{string_index}</v>"
                "</c>"
            )
        sheet_rows.append(f'<row r="{row_index}">{"".join(cells)}</row>')

    strings = "".join(
        f"<si><t>{escape(value)}</t></si>"
        for value in string_indexes
    )
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "xl/workbook.xml",
            (
                '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                "<sheets>"
                '<sheet name="Add_to_DB" sheetId="1" r:id="rId1"/>'
                "</sheets>"
                "</workbook>"
            ),
        )
        archive.writestr(
            "xl/_rels/workbook.xml.rels",
            (
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '<Relationship Id="rId1" '
                'Target="worksheets/sheet1.xml"/>'
                "</Relationships>"
            ),
        )
        archive.writestr(
            "xl/sharedStrings.xml",
            (
                '<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                f"{strings}"
                "</sst>"
            ),
        )
        archive.writestr(
            "xl/worksheets/sheet1.xml",
            (
                '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                "<sheetData>"
                f"{''.join(sheet_rows)}"
                "</sheetData>"
                "</worksheet>"
            ),
        )


def _column_ref(index: int) -> str:
    value = ""
    index += 1
    while index:
        index, remainder = divmod(index - 1, 26)
        value = chr(ord("A") + remainder) + value
    return value
