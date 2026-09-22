from __future__ import annotations

from pathlib import Path

from pathwaymech.mibig import load_mibig_json, mibig_cluster, mibig_seed_rows

FIXTURE = Path("tests/fixtures/mibig/BGC0000001.json")


def test_mibig_json_builds_cluster_lookup_rows() -> None:
    cluster = mibig_cluster(load_mibig_json(FIXTURE))

    assert cluster.id == "MIBiG:BGC0000001"
    assert cluster.products == ("mini metabolite",)
    assert cluster.genes == ("gene-a", "gene-b")
    assert cluster.loci == ("ABCD01000001.1",)
    assert cluster.references == ("PMID:12345678",)


def test_mibig_seed_rows_emit_tsv() -> None:
    assert mibig_seed_rows([mibig_cluster(load_mibig_json(FIXTURE))]) == [
        "mibig_id\tproducts\tgenes\tloci\treferences",
        "MIBiG:BGC0000001\tmini metabolite\tgene-a;gene-b\tABCD01000001.1\tPMID:12345678",
    ]
