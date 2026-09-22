from __future__ import annotations

from pathlib import Path

from pathwaymech.bigg import bigg_reactions, bigg_seed_rows, load_bigg_model
from pathwaymech.bvbrc import bvbrc_seed_rows, load_bvbrc_pathways
from pathwaymech.go import go_seed_rows, load_go_obo
from pathwaymech.modelseed import load_modelseed_tsv, modelseed_seed_rows


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
