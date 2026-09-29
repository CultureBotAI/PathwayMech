from __future__ import annotations

from pathlib import Path

import yaml

from pathwaymech.mibig import load_mibig_json, mibig_cluster, mibig_pathway_record, mibig_seed_rows
from pathwaymech.schema import validate_record

FIXTURE = Path("tests/fixtures/mibig/BGC0000001.json")


def test_mibig_json_builds_cluster_lookup_rows() -> None:
    cluster = mibig_cluster(load_mibig_json(FIXTURE))

    assert cluster.id == "MIBiG:BGC0000001"
    assert cluster.products == ("mini metabolite",)
    assert cluster.genes == ("gene-a", "gene-b")
    assert [locus.accession for locus in cluster.loci] == ["ABCD01000001.1"]
    assert [(locus.start, locus.end) for locus in cluster.loci] == [(10, 80)]
    assert cluster.references == ("PMID:12345678",)
    assert cluster.biosynthetic_classes == ("RiPP",)
    assert cluster.organism == "Mini test microbe"
    assert cluster.taxon_id == "12345"


def test_mibig_seed_rows_emit_tsv() -> None:
    assert mibig_seed_rows([mibig_cluster(load_mibig_json(FIXTURE))]) == [
        "mibig_id\tproducts\tgenes\tloci\treferences",
        "MIBiG:BGC0000001\tmini metabolite\tgene-a;gene-b\tABCD01000001.1\tPMID:12345678",
    ]


def test_mibig_cluster_builds_bgc_shaped_pathway_record() -> None:
    record = mibig_pathway_record(mibig_cluster(load_mibig_json(FIXTURE)))

    validate_record(record)
    assert yaml.safe_load(yaml.safe_dump(record)) == {
        "id": "MIBiG:BGC0000001",
        "label": "mini metabolite biosynthetic gene cluster",
        "description": "Experimentally characterized MIBiG MIBiG:BGC0000001 gene cluster.",
        "pathway_type": "biosynthetic-gene-cluster",
        "taxa": [{"id": "NCBITaxon:12345", "label": "Mini test microbe"}],
        "participants": [],
        "reactions": [],
        "mechanistic_edges": [],
        "gene_clusters": [
            {
                "id": "MIBiG:BGC0000001",
                "label": "mini metabolite biosynthetic gene cluster",
                "products": ["mini metabolite"],
                "biosynthetic_classes": ["RiPP"],
                "genes": [{"id": "gene-a"}, {"id": "gene-b"}],
                "loci": [{"accession": "ABCD01000001.1", "start": 10, "end": 80}],
            }
        ],
        "references": [
            {"id": "MIBiG:BGC0000001", "title": "MIBiG record BGC0000001"},
            {"id": "PMID:12345678", "title": "MIBiG literature reference PMID:12345678"},
        ],
    }
