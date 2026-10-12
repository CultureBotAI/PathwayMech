from __future__ import annotations

import csv
import io
import json
from pathlib import Path

import pytest
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
        "mibig_id\tproducts\tgenes\tloci\treferences\tstatus\tquality\tcompleteness"
        "\tretirement_reasons\tsee_also",
        "MIBiG:BGC0000001\tmini metabolite\tgene-a;gene-b\t"
        "ABCD01000001.1;ABCD01000001.1\tPMID:12345678;PMID:87654321\t\t\t\t\t",
    ]


def test_mibig_cluster_builds_bgc_shaped_pathway_record() -> None:
    record = mibig_pathway_record(mibig_cluster(load_mibig_json(FIXTURE)))

    validate_record(record)
    assert yaml.safe_load(yaml.safe_dump(record)) == {
        "id": "MIBiG:BGC0000001",
        "label": "mini metabolite biosynthetic gene cluster",
        "description": (
            "MIBiG source record MIBiG:BGC0000001 describes a biosynthetic gene cluster."
        ),
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


def test_mibig_cluster_preserves_source_product_order_for_label() -> None:
    cluster = mibig_cluster(
        {
            "cluster": {
                "mibig_accession": "BGC0000070",
                "compounds": [
                    {"compound": "griseofulvin"},
                    {"compound": "4-desmethylgriseofulvin"},
                    {"compound": "griseofulvin"},
                ],
            }
        }
    )

    assert cluster.products == ("griseofulvin", "4-desmethylgriseofulvin")
    assert (
        mibig_pathway_record(cluster)["label"]
        == "griseofulvin and related metabolites biosynthetic gene cluster"
    )


def test_mibig_cluster_rejects_records_without_a_cluster_accession() -> None:
    try:
        mibig_cluster({"loci": [{"accession": "ABCD01000001.1"}]})
    except ValueError as error:
        assert str(error) == "MIBiG JSON missing mibig_accession"
    else:
        raise AssertionError("expected a missing accession error")


def _seed_dict(cluster):
    return list(csv.DictReader(io.StringIO("\n".join(mibig_seed_rows([cluster]))), delimiter="\t"))[
        0
    ]


@pytest.mark.parametrize("legacy", [True, False])
def test_retired_source_is_auditable_but_cannot_become_a_draft(legacy):
    source = {
        "accession": "BGC9999001",
        "status": "retired",
        "quality": "questionable",
        "completeness": "unknown",
        "retirement_reasons": ["Duplicate of BGC9999002"],
        "see_also": ["BGC9999002"],
    }
    if legacy:
        source["mibig_accession"] = source.pop("accession")
        source = {"cluster": source}
    cluster = mibig_cluster(source)
    assert cluster.id == "MIBiG:BGC9999001"
    assert (cluster.status, cluster.quality, cluster.completeness) == (
        "retired",
        "questionable",
        "unknown",
    )
    assert cluster.retirement_reasons == ("Duplicate of BGC9999002",)
    assert cluster.see_also == ("BGC9999002",)
    row = _seed_dict(cluster)
    assert row["mibig_id"] == "MIBiG:BGC9999001"
    assert row["status"] == "retired"
    assert json.loads(row["retirement_reasons"]) == ["Duplicate of BGC9999002"]
    assert json.loads(row["see_also"]) == ["BGC9999002"]
    with pytest.raises(ValueError, match="Retired MIBiG record MIBiG:BGC9999001"):
        mibig_pathway_record(cluster)


def test_questionable_active_record_keeps_assessments_without_experimental_upgrade():
    cluster = mibig_cluster(
        {
            "accession": "BGC9999002",
            "status": "active",
            "quality": "questionable",
            "completeness": "complete",
        }
    )
    draft = mibig_pathway_record(cluster)
    validate_record(draft)
    assert draft["id"] == "MIBiG:BGC9999002"
    assert draft["description"] == (
        "MIBiG source record MIBiG:BGC9999002 describes a biosynthetic gene cluster. "
        'Source assessments: status="active"; quality="questionable"; completeness="complete".'
    )
    assert "experimentally" not in draft["description"].lower()
    row = _seed_dict(cluster)
    assert (row["status"], row["quality"], row["completeness"]) == (
        "active",
        "questionable",
        "complete",
    )


def test_missing_flags_remain_absent_and_nested_noncluster_flags_do_not_leak():
    cluster = mibig_cluster(
        {
            "accession": "BGC9999003",
            "genes": [{"quality": "high", "status": "active"}],
            "compounds": [{"completeness": "complete"}],
        }
    )
    for field in ("status", "quality", "completeness", "retirement_reasons", "see_also"):
        assert getattr(cluster, field) is None
        assert _seed_dict(cluster)[field] == ""
    assert mibig_pathway_record(cluster)["description"] == (
        "MIBiG source record MIBiG:BGC9999003 describes a biosynthetic gene cluster."
    )


def test_explicit_empty_lists_remain_distinct_from_absent_flags():
    cluster = mibig_cluster(
        {
            "accession": "BGC9999004",
            "retirement_reasons": [],
            "see_also": [],
        }
    )
    assert cluster.retirement_reasons == ()
    assert cluster.see_also == ()
    assert _seed_dict(cluster)["retirement_reasons"] == "[]"
    assert _seed_dict(cluster)["see_also"] == "[]"


def test_seed_tsv_roundtrips_tabs_newlines_and_literal_source_order():
    cluster = mibig_cluster(
        {
            "accession": "BGC9999005",
            "status": "active",
            "quality": "questionable",
            "compounds": [{"name": 'name\twith\n"quotes"'}],
            "retirement_reasons": ["second\nline", "first\ttab", "second\nline"],
            "see_also": ["BGC9999007", "BGC9999006"],
        }
    )
    row = _seed_dict(cluster)
    assert row["products"] == 'name\twith\n"quotes"'
    assert json.loads(row["retirement_reasons"]) == ["second\nline", "first\ttab", "second\nline"]
    assert json.loads(row["see_also"]) == ["BGC9999007", "BGC9999006"]


def test_conflicting_legacy_and_modern_status_is_not_silently_ignored():
    with pytest.raises(ValueError, match="Conflicting MIBiG status"):
        mibig_cluster(
            {
                "accession": "BGC9999008",
                "status": "active",
                "cluster": {"mibig_accession": "BGC9999008", "status": "retired"},
            }
        )


@pytest.mark.parametrize(
    "field,value",
    [
        ("status", None),
        ("status", False),
        ("quality", ""),
        ("completeness", {}),
        ("retirement_reasons", "duplicate"),
        ("see_also", [None]),
    ],
)
def test_malformed_assessment_fields_fail_explicitly(field, value):
    with pytest.raises(ValueError, match=f"MIBiG {field}"):
        mibig_cluster({"accession": "BGC9999009", field: value})


def test_source_status_spelling_preserved_but_retirement_guard_cannot_be_bypassed():
    cluster = mibig_cluster({"accession": "BGC9999010", "status": " Retired "})
    assert cluster.status == " Retired "
    assert _seed_dict(cluster)["status"] == " Retired "
    with pytest.raises(ValueError, match="Retired MIBiG"):
        mibig_pathway_record(cluster)
