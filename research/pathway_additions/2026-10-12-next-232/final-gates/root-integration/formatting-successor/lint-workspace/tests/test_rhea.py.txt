from __future__ import annotations

from pathlib import Path

from pathwaymech.rhea import load_rhea_tsv, rhea_seed_rows

FIXTURE = Path("tests/fixtures/rhea/reactions.tsv")


def test_rhea_tsv_builds_reaction_lookup_rows() -> None:
    reactions = load_rhea_tsv(FIXTURE)

    assert reactions[0].id == "RHEA:10588"
    assert reactions[0].chebi_ids == (
        "CHEBI:57604",
        "CHEBI:456216",
        "CHEBI:58272",
        "CHEBI:30616",
    )
    assert reactions[0].ec_numbers == ("EC:2.7.2.3",)
    assert reactions[0].go_terms == ("GO:0004618",)
    assert reactions[0].xrefs == ("KEGG:R01512", "MetaCyc:PHOSGLYPHOS-RXN")


def test_rhea_seed_rows_emit_tsv() -> None:
    assert rhea_seed_rows(load_rhea_tsv(FIXTURE)) == [
        "rhea_id\tequation\tchebi_ids\tec_numbers\tgo_terms\txrefs",
        (
            "RHEA:10588\t"
            "3-phospho-D-glyceroyl phosphate + ADP = 3-phospho-D-glycerate + ATP\t"
            "CHEBI:57604;CHEBI:456216;CHEBI:58272;CHEBI:30616\t"
            "EC:2.7.2.3\tGO:0004618\tKEGG:R01512;MetaCyc:PHOSGLYPHOS-RXN"
        ),
    ]
