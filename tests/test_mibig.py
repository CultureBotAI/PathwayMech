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
    assert [locus.accession for locus in cluster.loci] == [
        "ABCD01000001.1",
        "ABCD01000001.1",
    ]
    assert [(locus.start, locus.end) for locus in cluster.loci] == [(10, 80), (120, 160)]
    assert cluster.references == ("PMID:12345678", "PMID:87654321")
    assert cluster.biosynthetic_classes == ("RiPP",)
    assert cluster.organism == "Mini test microbe"
    assert cluster.taxon_id == "12345"


def test_mibig_seed_rows_emit_tsv() -> None:
    assert mibig_seed_rows([mibig_cluster(load_mibig_json(FIXTURE))]) == [
        "mibig_id\tproducts\tgenes\tloci\treferences",
        "MIBiG:BGC0000001\tmini metabolite\tgene-a;gene-b\t"
        "ABCD01000001.1;ABCD01000001.1\tPMID:12345678;PMID:87654321",
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
                "loci": [
                    {"accession": "ABCD01000001.1", "start": 10, "end": 80},
                    {"accession": "ABCD01000001.1", "start": 120, "end": 160},
                ],
            }
        ],
        "references": [
            {"id": "MIBiG:BGC0000001", "title": "MIBiG record BGC0000001"},
            {"id": "PMID:12345678", "title": "MIBiG literature reference PMID:12345678"},
            {"id": "PMID:87654321", "title": "MIBiG literature reference PMID:87654321"},
        ],
    }


def test_mibig_cluster_accepts_v4_top_level_json() -> None:
    cluster = mibig_cluster(
        {
            "accession": "BGC0002072",
            "compounds": [
                {"name": "linearmycin A"},
                {"name": "linearmycin C"},
                {"name": "linearmycin C"},
            ],
            "biosynthesis": {
                "classes": [{"class": "PKS", "subclass": "Type I"}],
                "modules": [
                    {"genes": ["AKL64834.1"]},
                    {"at_domain": {"gene": "AKL69764.1"}},
                ],
            },
            "loci": [
                {
                    "accession": "CP011664.1",
                    "location": {"from": 1061319, "to": 1236790},
                }
            ],
            "legacy_references": [
                "pubmed:28919037",
                "doi:10.1016/0040-4039(95)00392-P",
            ],
            "taxonomy": {"name": "Streptomyces sp. Mg1", "ncbiTaxId": 465541},
        }
    )

    assert cluster.id == "MIBiG:BGC0002072"
    assert cluster.products == ("linearmycin A", "linearmycin C")
    assert cluster.genes == ("AKL64834.1", "AKL69764.1")
    assert cluster.biosynthetic_classes == ("PKS:Type I",)
    assert cluster.references == ("PMID:28919037",)
    assert cluster.taxon_id == "465541"


def test_mibig_cluster_rejects_records_without_a_cluster_accession() -> None:
    try:
        mibig_cluster({"loci": [{"accession": "ABCD01000001.1"}]})
    except ValueError as error:
        assert str(error) == "MIBiG JSON missing mibig_accession"
    else:
        raise AssertionError("expected a missing accession error")
