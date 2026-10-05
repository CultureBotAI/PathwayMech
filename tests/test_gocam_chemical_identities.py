"""Independent biochemical regression checks for repaired GO-CAM imports."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(slug):
    return yaml.load((ROOT / "data/pathways" / f"{slug}.yaml").read_text(), Loader=yaml.CSafeLoader)


def edges(data):
    return {(e["subject"], e["predicate"], e["object"]) for e in data["mechanistic_edges"]}


def test_fox2_stereochemistry_and_distinct_dci1_eci1_chemistry():
    data = record("fatty-acid-oxidation-pathway")
    graph = edges(data)
    assert ("RHEA:26528", "has_output", "CHEBI:57319") in graph
    assert ("RHEA:32712", "has_input", "CHEBI:57319") in graph
    assert "CHEBI:15455" not in {n["id"] for n in data["participants"]}
    assert ("SGD:S000005706", "enables", "RHEA:45241") in graph
    assert ("RHEA:45241", "has_input", "CHEBI:85110") in graph
    assert ("RHEA:45241", "has_output", "CHEBI:85111") in graph
    eci = "gomodel:YeastPathways_YEAST-FAO-PWY/6a4c244800006775"
    assert ("SGD:S000004274", "enables", eci) in graph
    assert (eci, "has_input", "CHEBI:27773") in graph
    assert not any(s == "RHEA:45241" and p == "provides_input_for" for s, p, _ in graph)


def test_mae1_retains_decarboxylation_and_does_not_become_malate_dehydrogenase():
    data = record("gluconeogenesis-i")
    graph = edges(data)
    mae = "SGD:S000001512"
    activities = {o for s, p, o in graph if s == mae and p == "enables"}
    assert activities == {"gomodel:1.1.1.39-RXN"}
    assert ("gomodel:1.1.1.39-RXN", "has_output", "CHEBI:15361") in graph
    assert ("gomodel:1.1.1.39-RXN", "has_output", "CHEBI:16526") in graph
    assert ("gomodel:MALATE-DEH-RXN", "has_output", "CHEBI:16452") in graph


def test_aro8_transamination_has_one_amino_donor_on_each_side():
    graph = edges(record("tryptophan-degradation"))
    aid = "gomodel:TRYPTOPHAN-AMINOTRANSFERASE-RXN"
    assert (aid, "has_input", "CHEBI:57912") in graph
    assert (aid, "has_input", "CHEBI:16810") in graph
    assert (aid, "has_output", "CHEBI:29985") in graph
    assert (aid, "has_output", "CHEBI:17640") in graph
    assert (aid, "has_input", "CHEBI:29985") not in graph


def test_psa1_uses_triphosphate_donor_and_diphosphate_leaving_group():
    graph = edges(record("dolichyl-phosphate-d-mannose-biosynthesis"))
    assert ("RHEA:15230", "has_input", "CHEBI:37565") in graph
    assert ("RHEA:15230", "has_output", "CHEBI:33019") in graph
    assert ("RHEA:15230", "has_output", "CHEBI:57527") in graph
    assert ("RHEA:15230", "has_input", "CHEBI:58189") not in graph


def test_arg2_and_arg7_acetyl_glutamate_labels_have_located_independent_evidence():
    data = record("l-arginine-biosynthesis-ii-acetyl-cycle")
    for aid in [
        "gomodel:N-ACETYLTRANSFER-RXN",
        "gomodel:YeastPathways_ARGSYNBSUB-PWY/6a4c244800000704",
    ]:
        node = next(n for n in data["reactions"] if n["id"] == aid)
        assert "glutamate" in node["label"] and "methionine" not in node["label"]
        edge = next(
            e
            for e in data["mechanistic_edges"]
            if e["predicate"] == "enables" and e["object"] == aid
        )
        assert any(
            "RHEA:24292" in ev.get("source_assertion", "") and "/reaction" in ev["source_locator"]
            for ev in edge["evidence"]
        )


def test_yeast_datp_retains_diphosphate_route_without_unenabled_class_iii_branch():
    data = record("adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii")
    graph = edges(data)
    assert not any("gomodel:RXN0-745" in (s, o) for s, _, o in graph)
    assert ("gomodel:ADPREDUCT-RXN", "has_output", "CHEBI:57667") in graph
    assert ("gomodel:DADPKIN-RXN", "has_output", "CHEBI:61404") in graph
    assert any(r["id"] == "PMID:6370695" for r in data["references"])


def test_coq1_hexaprenyl_label_agrees_with_preserved_six_unit_product():
    data = record("hexaprenyl-diphosphate-biosynthesis")
    activity = next(r for r in data["reactions"] if r["id"] == "gomodel:RXN3O-9805")
    assert activity["label"] == "hexaprenyl diphosphate synthase activity"
    assert (activity["id"], "has_output", "CHEBI:58179") in edges(data)
    assert ("SGD:S000000207", "enables", activity["id"]) in edges(data)
