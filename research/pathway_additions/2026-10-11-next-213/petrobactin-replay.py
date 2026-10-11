"""Original-source author replay of the complete external petrobactin draft.

This is reproducibility/quality control, not independent scientific approval.
No maintained record, shared authority or cache is written.
"""

from __future__ import annotations

import collections
import copy
import csv
import hashlib
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import html

from pathwaymech.identifiers import identifier_errors
from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

D = Path(__file__).resolve().parent
B = D.parent
R = Path("/private/tmp/pathwaymech-next-211-20261011")
F = Path("/private/tmp/pathwaymech-petrobactin-followup-20261011")
ORIGINALS = Path("/private/tmp/pathwaymech-siderophore-next-scout-20261011/originals")
TARGET = D / "petrobactin-biosynthesis.yaml"


def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def save(name, value):
    (D / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


started = datetime.now(UTC).isoformat()
raw = yaml.safe_load(TARGET.read_text())
record = validate_record(raw)
assert not strict_errors([TARGET], R)
p = read(D / "petrobactin-source-projection.json")
assert p["target_sha256"] == sha(TARGET)
assert p["graph_to_source"] == raw["mechanistic_edges"]
# Actual original RDF/chemical/translation extraction, not a projection-only pass.
run = subprocess.run(
    [sys.executable, str(B / "scratch/source_replay.py")],
    cwd=B,
    capture_output=True,
    text=True,
    check=False,
)
(B / "source-replay.log").write_text(run.stdout + run.stderr)
assert run.returncode == 0, run.stderr
fresh = read(B / "scratch/rhea-source-projection.json")
byrid = {r["selected"]: r for r in fresh["selected_reactions"]}
assert len(byrid) == 10
native = ET.parse(ORIGINALS / "PWY-6289.xml").getroot().find("Pathway")
members = [x.get("frameid") for x in native.findall("reaction-list/Reaction")]
assert len(members) == len(set(members)) == 10
mapping = {x["native"]: x["reaction"] for x in p["source_to_graph"]}
assert set(members) == set(mapping)
assert set(mapping.values()) == {r["id"] for r in raw["reactions"]}
assert all(r["direction"] == "left_to_right" for r in raw["reactions"])
for n in members:
    e = ET.parse(ORIGINALS / (n + ".xml")).getroot().find("Reaction")
    assert e.get("frameid") == n
    assert e.findtext("reaction-direction") in {"LEFT-TO-RIGHT", "PHYSIOL-LEFT-TO-RIGHT"}
    layouts = [
        x for x in native.findall("reaction-layout") if x.find("Reaction").get("frameid") == n
    ]
    assert len(layouts) == 1 and layouts[0].findtext("direction") == "L2R"
# Exact native side identity and coefficients are independent of current equation labels.
native_sides = []
for n in members:
    e = ET.parse(ORIGINALS / (n + ".xml")).getroot().find("Reaction")
    sides = {}
    for name in ["left", "right"]:
        sides[name] = [
            {"id": x[0].get("frameid"), "coefficient": int(x.findtext("coefficient") or 1)}
            for x in e.findall(name)
        ]
    native_sides.append(
        {"native": n, "direction": e.findtext("reaction-direction"), "sides": sides}
    )
assert len(p["chemical_sides"]) == 54
for s in p["chemical_sides"]:
    source = byrid[s["source_rhea"]]
    exact = next(
        t for t in source[s["role"]] if t["participant_uri"] == s["source_side"]["participant_uri"]
    )
    assert exact == s["source_side"]
    expected_id = exact["id"]
    if s["reaction"] == "MetaCyc:RXN-10679" and expected_id == "CHEBI:142778":
        expected_id = "MetaCyc:CPD-9985"
    assert s["identifier"] == expected_id and s["coefficient"] == exact["coefficient"]
    sub, obj = (
        (expected_id, s["reaction"]) if s["role"] == "substrates" else (s["reaction"], expected_id)
    )
    matches = [
        e
        for e in raw["mechanistic_edges"]
        if e["subject"] == sub
        and e["object"] == obj
        and e["predicate"] == ("consumes" if s["role"] == "substrates" else "produces")
    ]
    assert len(matches) == 1
# Atom/charge balance is separate from identity. The terminal native structure is checked first.
chem = read(B / "scratch/chemical-identity-adjudication.json")
assert sum(x["exact_inchi_equal"] for x in chem["bridges"]) == 9
assert len(chem["bridges"]) == 10
for key in ["native", "chebi"]:
    assert (
        chem["terminal_connectivity"][key]
        == read(F / "chemical-identity-adjudication.json")["terminal_connectivity"][key]
    )
# Source replay itself asserts nine matching InChIs and unequal terminal carbon-arm connectivity.
terminal = ET.parse(F / "originals/CPD-9985.xml").getroot().find("Compound")
assert terminal.get("frameid") == "CPD-9985"
assert terminal.find("cml/molecule").get("formalCharge") == "1"
formula = terminal.find("cml/molecule/formula").get("concise")
assert formula == "C 34 H 51 N 6 O 11", formula
assert all(not r["reactive_part_atom_and_charge_residual"] for r in fresh["selected_reactions"])
assert all(r["carrier_class_count_residual"] == 0 for r in fresh["selected_reactions"])
# Maturation is a separate priming transformation, not a per-product cost.
base = {"RHEA:24849": 2, "RHEA:62469": 2, "RHEA:62477": 2, "RHEA:63809": 1, "MetaCyc:RXN-10679": 1}
branch_a = base | {"RHEA:63813": 1, "RHEA:64025": 1}
branch_b = base | {"RHEA:64029": 1, "RHEA:63817": 1}


def net(flux):
    total = collections.Counter()
    for side in p["chemical_sides"]:
        factor = flux.get(side["reaction"], 0)
        sign = -1 if side["role"] == "substrates" else 1
        total[side["identifier"]] += sign * factor * side["coefficient"]
    return {key: value for key, value in sorted(total.items()) if value}


net_a, net_b = net(branch_a), net(branch_b)
assert net_a == net_b
assert net_a["MetaCyc:CPD-9985"] == 1
assert net_a["CHEBI:30616"] == -4 and net_a["CHEBI:456215"] == 4
assert not any(x.startswith("RHEA-COMP:") for x in net_a)
# Meaningful negative guards address known source conflicts rather than mirror arbitrary formatting.


def guard(doc):
    all_ids = {x["id"] for s in ["participants", "reactions"] for x in doc[s]}
    assert "CHEBI:142778" not in all_ids, (
        "Rejected constitutional isomer must not become terminal product"
    )
    assert "RHEA:63821" not in {x["id"] for x in doc["reactions"]}, (
        "No exact terminal equation equivalence"
    )
    assert "RHEA:62461" not in all_ids, (
        "Net AsbC would double-count its retained component reactions"
    )
    assert len(doc["reactions"]) == 10
    assert not doc.get("source_mappings"), "No false cross-source exactMatch"
    assert not any(
        e["object"] == "RHEA:48405" and e["predicate"] in {"enables", "catalyzes"}
        for e in doc["mechanistic_edges"]
    ), "Physiological maturation catalyst remains unassigned"
    for edge in doc["mechanistic_edges"]:
        for evidence in edge["evidence"]:
            if evidence["reference_id"].startswith("MetaCyc:"):
                assert "unification cross-reference" not in evidence.get("source_assertion", "")


guard(raw)
negative = []
for kind in ["wrong_terminal_product", "invented_maturation_catalyst", "truncated_boundary"]:
    bad = copy.deepcopy(raw)
    if kind == "wrong_terminal_product":
        next(x for x in bad["participants"] if x["id"] == "MetaCyc:CPD-9985")["id"] = "CHEBI:142778"
    elif kind == "invented_maturation_catalyst":
        bad["mechanistic_edges"].append(
            {"subject": "NCBIProtein:AAT54156.1", "predicate": "catalyzes", "object": "RHEA:48405"}
        )
    else:
        bad["reactions"] = [x for x in bad["reactions"] if x["id"] != "RHEA:48405"]
    try:
        guard(bad)
    except AssertionError:
        negative.append(kind)
    else:
        raise AssertionError("Known invalid mutation was accepted: " + kind)
# Rehash every actual reference original, keeping original full-body versus projection scope clear.
ref_reports = []
for ref in raw["references"]:
    path = Path(p["reference_original_paths"][ref["id"]])
    assert sha(path) == ref["source_sha256"], ref["id"]
    ref_reports.append(
        {"reference_id": ref["id"], "path": str(path), "sha256": ref["source_sha256"]}
    )
# Recheck source-native protein identities against issuing genome annotations.
comparisons = read(B / "scratch/genome-identity-comparison.json")["comparisons"]
assert sum(x["exact_sequence_equal"] for x in comparisons) == 4
ncbi = {
    x.findtext("GBSeq_accession-version"): x
    for x in ET.parse(B / "originals/Sterne-six-proteins.xml").getroot()
}
assert len(ncbi) == 6
for c in comparisons:
    n = ncbi[c["genome_protein_id"]]
    assert (
        hashlib.sha256(n.findtext("GBSeq_sequence").upper().encode()).hexdigest()
        == c["genome_translation_sha256"]
    )
    qs = {
        x.findtext("GBQualifier_name"): x.findtext("GBQualifier_value")
        for f in n.findall("GBSeq_feature-table/GBFeature")
        if f.findtext("GBFeature_key") == "source"
        for x in f.findall("GBFeature_quals/GBQualifier")
    }
    assert qs["strain"] == "Sterne" and qs["db_xref"] == "taxon:260799"
# Literal excerpt and metadata titles must occur at the actual inspected source selectors.
quotes = 0
for e in raw["mechanistic_edges"]:
    for v in e["evidence"]:
        if "quote" in v:
            tree = html.fromstring(
                Path(p["reference_original_paths"][v["reference_id"]]).read_bytes()
            )
            text = " ".join(" ".join(tree.xpath('//*[@id="sec5"]/p[2]')[0].itertext()).split())
            assert v["quote"] in text
            quotes += 1
for pmid in ["PMID:22408253", "PMID:18955706"]:
    ref = next(x for x in raw["references"] if x["id"] == pmid)
    tree = html.fromstring(Path(p["reference_original_paths"][pmid]).read_bytes())
    assert ref["title"] == tree.xpath('//meta[@name="citation_title"]/@content')[0]
assert not identifier_errors(B / "authority-sandbox")
assert sha(B / "authority-sandbox/data/pathways/petrobactin-biosynthesis.yaml") == sha(TARGET)
# Actual exported bytes preserve every evidence item and original reference metadata.
nodes_file, edges_file = write_kgx([record], B / "kgx")
nodes = list(csv.DictReader(nodes_file.open(), delimiter="\t"))
exported = list(csv.DictReader(edges_file.open(), delimiter="\t"))
assert len(exported) == len(raw["mechanistic_edges"]) == 94
refmap = {x["id"]: x for x in raw["references"]}
for e, out in zip(raw["mechanistic_edges"], exported, strict=True):
    assert (out["subject"], out["predicate"], out["object"]) == (
        e["subject"],
        LOCAL_PREDICATE_CURIES[e["predicate"]],
        e["object"],
    )
    assert json.loads(out["evidence"]) == e["evidence"]
    assert out["description"] == e.get("description", "")
    assert json.loads(out["reference_metadata"]) == [
        refmap[k] for k in sorted({v["reference_id"] for v in e["evidence"]})
    ]
for n in nodes:
    if n["id"].startswith("RHEA-COMP:"):
        assert n["category"] == "biolink:ChemicalEntity"
assert (
    next(x for x in nodes if x["id"] == "MetaCyc:CPD-9985")["category"] == "biolink:SmallMolecule"
)
result = {
    "started_at": started,
    "finished_at": datetime.now(UTC).isoformat(),
    "status": "passed_author_checks_not_independent_approval",
    "target_sha256": sha(TARGET),
    "native_and_closed_schema": "passed",
    "canonical_identifier_check": "passed_external_sandbox",
    "complete_native_members": 10,
    "both_branches_retained": True,
    "original_rhea_reactions_reparsed": 10,
    "selected_chemical_sides": 54,
    "formal_balances": 10,
    "balance_scope": (
        "Matched generic protein scaffolds plus reactive parts; "
        "does not validate identity or specify assembly stoichiometry"
    ),
    "terminal_identity": (
        "Native CPD-9985, independently checked connectivity; "
        "Rhea terminal small-product mapping rejected"
    ),
    "branch_a_flux": branch_a,
    "branch_b_flux": branch_b,
    "same_derived_net": net_a,
    "net_limit": (
        "Derived four ATP-to-AMP events per product, not direct ATP/product measurement; "
        "maturation is separate priming and not added per product"
    ),
    "negative_guards_rejected": negative,
    "native_source_sides": native_sides,
    "source_reference_checks": ref_reports,
    "source_protein_comparisons": comparisons,
    "literal_quotes_checked": quotes,
    "kgx": {
        "nodes": len(nodes),
        "edges": len(exported),
        "evidence": sum(len(x["evidence"]) for x in raw["mechanistic_edges"]),
        "nodes_sha256": sha(nodes_file),
        "edges_sha256": sha(edges_file),
    },
    "deferred_integration_gates": [
        "shared corpus render-pages",
        "full just validate",
        "full just test",
        "base-aware history and independent review",
    ],
    "reference_repository": {
        "path": str(R),
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=R, text=True).strip(),
    },
    "helper_sha256": sha(__file__),
    "source_replay_helper_sha256": sha(B / "scratch/source_replay.py"),
}
save("petrobactin-validation.json", result)
print(
    json.dumps(
        {
            k: result[k]
            for k in [
                "status",
                "target_sha256",
                "complete_native_members",
                "selected_chemical_sides",
                "formal_balances",
                "kgx",
            ]
        },
        indent=2,
    )
)
