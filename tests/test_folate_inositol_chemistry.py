"""Biochemical regression checks independent of the bounded migration code."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(slug):
    return yaml.safe_load((ROOT / "data/pathways" / (slug + ".yaml")).read_text())


def sides(record, activity):
    return {
        role: {
            e["object"]
            for e in record["mechanistic_edges"]
            if e["subject"] == activity and e["predicate"] == role
        }
        for role in ("has_input", "has_output")
    }


def test_folate_dehydrogenases_do_not_consume_and_produce_the_same_folate():
    record = load("folate-interconversions")
    for activity in (
        "gomodel:1.5.1.15-RXN",
        "gomodel:METHYLENETHFDEHYDROG-NADP-RXN",
        "gomodel:YeastPathways_PWY3O-697/6a4c244800005484",
    ):
        role = sides(record, activity)
        assert "CHEBI:20502" in role["has_input"]
        assert "CHEBI:57455" in role["has_output"]
        assert "CHEBI:20502" not in role["has_output"]
    for activity in (
        "gomodel:METHENYLTHFCYCLOHYDRO-RXN",
        "gomodel:YeastPathways_PWY3O-697/6a4c244800005468",
    ):
        assert "CHEBI:57455" in sides(record, activity)["has_input"]


def test_met13_and_met12_keep_their_distinct_cofactor_specificity():
    record = load("folate-interconversions")
    met13 = sides(record, "gomodel:YeastPathways_PWY3O-697/6a4c244800005519")
    met12 = sides(record, "gomodel:1.5.1.20-RXN")
    assert "CHEBI:57783" in met13["has_input"] and "CHEBI:58349" in met13["has_output"]
    assert "CHEBI:57945" not in met13["has_input"]
    assert "CHEBI:57945" in met12["has_input"] and "CHEBI:57540" in met12["has_output"]


def test_retained_folate_material_flow_has_actual_shared_intermediate():
    record = load("folate-interconversions")
    folates = {"CHEBI:20502", "CHEBI:57455", "CHEBI:57451", "CHEBI:67016", "CHEBI:134413"}
    edges = [e for e in record["mechanistic_edges"] if e["predicate"] == "provides_input_for"]
    assert len(edges) == 3
    for edge in edges:
        assert (
            sides(record, edge["subject"])["has_output"]
            & sides(record, edge["object"])["has_input"]
            & folates
        )


def test_vip1_and_kcs1_regioisomers_and_catalysts():
    record = load("inositol-phosphate-biosynthesis")
    assert "CHEBI:74946" in sides(record, "gomodel:RXN3O-258")["has_output"]
    for aid in ("gomodel:RXN3O-143", "gomodel:RXN3O-9819"):
        assert "CHEBI:77983" in sides(record, aid)["has_output"]
        assert "CHEBI:15378" in sides(record, aid)["has_input"]
    assert "CHEBI:74946" in sides(record, "gomodel:RXN3O-9819")["has_input"]
    assert any(
        e["subject"] == "SGD:S000002424"
        and e["predicate"] == "enables"
        and e["object"] == "gomodel:RXN3O-9819"
        for e in record["mechanistic_edges"]
    )
    ids = {n["id"] for n in record["participants"]}
    assert not ids & {"CHEBI:53064", "CHEBI:52965", "CHEBI:187038"}


def test_ip5_kinases_do_not_make_bispyrophosphate_and_ddp1_is_not_over_specific():
    record = load("inositol-phosphate-biosynthesis")
    for aid in ("gomodel:RXN-4941", "gomodel:YeastPathways_PWY3O-402/6a4c244800000690"):
        products = sides(record, aid)["has_output"]
        assert "gomodel:CHEBI_14178_RXN-4941" in products
        assert "CHEBI:14178" not in products
    assert "CHEBI:14178" in sides(record, "gomodel:RXN3O-786")["has_input"]
    assert "gomodel:CHEBI_62919_RXN3O-786" in sides(record, "gomodel:RXN3O-785")["has_input"]


def test_vip1_domain_phosphatase_is_qualified_and_has_exact_hydrolysis_chemistry():
    record = load("inositol-phosphate-biosynthesis")
    role = sides(record, "RHEA:79724")
    assert role["has_input"] == {"CHEBI:74946", "CHEBI:15377"}
    assert role["has_output"] == {"CHEBI:58130", "CHEBI:43474", "CHEBI:15378"}
    edge = next(
        e
        for e in record["mechanistic_edges"]
        if e["object"] == "RHEA:79724" and e["predicate"] == "enables"
    )
    assert edge["subject"] == "SGD:S000004402"
    assert "domain" in edge["description"] and "In-vitro" in edge["description"]
    assert edge["evidence"][0]["reference_id"] == "PMID:32303658"
    assert "//sec[@id='s5']" in edge["evidence"][0]["source_locator"]
    assert "not an assertion of physiological flux" in edge["evidence"][0]["source_assertion"]
