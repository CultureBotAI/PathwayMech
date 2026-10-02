from __future__ import annotations

from pathlib import Path

from pathwaymech.bigg import bigg_reactions, bigg_seed_rows, load_bigg_model
from pathwaymech.bvbrc import bvbrc_seed_rows, load_bvbrc_pathways
from pathwaymech.gapmind import gapmind_seed_rows, load_gapmind_steps
from pathwaymech.go import go_seed_rows, load_go_obo
from pathwaymech.modelseed import load_modelseed_tsv, modelseed_seed_rows
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
