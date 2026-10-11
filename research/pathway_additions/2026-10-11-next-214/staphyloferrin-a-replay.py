"""External source replay and artifact checks; not an independent scientific review."""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import subprocess
import sys
from datetime import UTC, datetime
from functools import cache
from pathlib import Path

import yaml
from lxml import etree as ET
from lxml import html

from pathwaymech.identifiers import identifier_errors
from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

D = Path(__file__).resolve().parent
B = D.parent
R = Path("/private/tmp/pathwaymech-next-211-20261011")
F = Path("/private/tmp/pathwaymech-staphyloferrin-a-followup-20261011")
ORIGINALS = Path("/private/tmp/pathwaymech-siderophore-next-scout-20261011/originals")
T = D / "staphyloferrin-a-biosynthesis.yaml"


@cache
def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def norm(text):
    return " ".join(text.split())


started = datetime.now(UTC).isoformat()
raw = yaml.safe_load(T.read_text())
record = validate_record(raw)
assert not strict_errors([T], R)
p = read(D / "staphyloferrin-a-source-projection.json")
assert p["target_sha256"] == sha(T)
assert p["graph_to_source"] == raw["mechanistic_edges"]
# Replay complete original RDF and native structures, not just the saved projection.
run = subprocess.run(
    [sys.executable, str(B / "scratch/original_chemistry_replay.py")],
    cwd=B,
    capture_output=True,
    text=True,
    check=False,
)
(B / "source-replay.log").write_text(run.stdout + run.stderr)
assert run.returncode == 0, run.stderr
chem = read(B / "scratch/chemistry.json")
assert len(chem["reactions"]) == 3
assert all(not r["balance_residual"] for r in chem["reactions"])
assert [b["exact_equal"] for b in chem["native_current_bridges"]] == [True, True, False, False]
assert chem["route_net"] == p["net"]
assert chem["route_net"] == {
    "CHEBI:46911": -1,
    "CHEBI:16947": -2,
    "CHEBI:30616": -2,
    "CHEBI:456215": 2,
    "CHEBI:33019": 2,
    "CHEBI:15378": 2,
    "CHEBI:142973": 1,
}
native = ET.parse(str(ORIGINALS / "PWY-7990.xml")).find("Pathway")
members = native.xpath("reaction-list/Reaction/@frameid")
assert set(members) == {"ORNITHINE-RACEMASE-RXN", "RXN-19522", "RXN-19521"}
assert {r["native"] for r in p["source_to_graph"]} == set(members)
assert {r["reaction"] for r in p["source_to_graph"]} == {r["id"] for r in raw["reactions"]}
assert "R00672" in (ORIGINALS / "M00876.txt").read_text()
assert all(x in (ORIGINALS / "M00876.txt").read_text() for x in ["R12353", "R12354"])
for row in p["source_to_graph"]:
    x = ET.parse(str(ORIGINALS / (row["native"] + ".xml"))).find("Reaction")
    assert x.findtext("reaction-direction") == row["native_direction"]
    sides = {
        s: [
            {"id": t[0].get("frameid"), "coefficient": int(t.findtext("coefficient") or 1)}
            for t in x.findall(s)
        ]
        for s in ["left", "right"]
    }
    assert sides == row["native_sides"]
    layout = native.xpath("reaction-layout[Reaction/@frameid=$n]/direction/text()", n=row["native"])
    assert layout == ["L2R"]
reactions = {f"RHEA:{r['directional']}": r for r in chem["reactions"]}
assert len(p["chemical_sides"]) == 16
for side in p["chemical_sides"]:
    expected = next(
        x
        for x in reactions[side["reaction"]]["sides"][side["role"]]
        if x["participant_uri"] == side["participant_uri"]
    )
    assert {k: side[k] for k in expected} == expected
    e = next(e for e in raw["mechanistic_edges"] if e["id"] == side["edge_id"])
    sub, obj = (
        (side["id"], side["reaction"])
        if side["role"] == "substrates"
        else (side["reaction"], side["id"])
    )
    assert (e["subject"], e["object"]) == (sub, obj)
    assert f"rh:contains{side['coefficient']}" in e["evidence"][0]["source_locator"]
# Read exact protein identity and comparison anew from original bodies.
proteins = {
    x.findtext("GBSeq_accession-version"): x
    for x in ET.parse(str(F / "originals/Newman-proteins.xml")).getroot()
}
comp = []
for ac, up, locus in [
    ("BAF68351.1", "Q2FW73", "NWMN_2079"),
    ("BAF68352.1", "Q2FW72", "NWMN_2080"),
    ("BAF68354.1", "Q2FW70", "NWMN_2082"),
]:
    x = proteins[ac]
    quals = [
        (q.findtext("GBQualifier_name"), q.findtext("GBQualifier_value"))
        for q in x.findall(".//GBQualifier")
    ]
    assert ("locus_tag", locus) in quals
    assert ("strain", "Newman") in quals
    assert ("db_xref", "taxon:426430") in quals
    path = (
        (ORIGINALS / (up + ".json"))
        if (ORIGINALS / (up + ".json")).exists()
        else F / "originals" / (up + (".json"))
    )
    u = read(path)
    assert u["organism"]["taxonId"] == 93061
    ns = x.findtext("GBSeq_sequence").upper()
    us = u["sequence"]["value"]
    assert len(ns) == len(us)
    differences = [i + 1 for i, (a, b) in enumerate(zip(ns, us, strict=True)) if a != b]
    assert differences == ([532] if up == "Q2FW70" else [])
    comp.append(
        {
            "accession": ac,
            "locus": locus,
            "up": up,
            "length": len(ns),
            "newman_sequence_sha256": hashlib.sha256(ns.encode()).hexdigest(),
            "up_sequence_sha256": hashlib.sha256(us.encode()).hexdigest(),
            "different_positions": differences,
            "exact_sequence_equal": not differences,
        }
    )
u = read(ORIGINALS / "Q2FW73.json")
assert u["entryType"] == "UniProtKB unreviewed (TrEMBL)"
assert u["comments"][0]["cofactors"][0]["evidences"][0]["evidenceCode"] == "ECO:0000256"
assert u["comments"][0]["cofactors"][0]["cofactorCrossReference"]["id"] == "CHEBI:597326"
for obj, rxn in [("ENZRXN-26283", "RXN-19521"), ("ENZRXN-26284", "RXN-19522")]:
    x = ET.parse(str(ORIGINALS / (obj + ".xml"))).find("Enzymatic-Reaction")
    assert x.find("reaction/Reaction").get("frameid") == rxn
    assert x.find("cofactor/Compound").get("frameid") == "MG+2"
sfac = ET.parse(str(ORIGINALS / "MONOMER-20490.xml")).find("Protein")
assert "assumed" in sfac.findtext("comment") and "not been purified" in sfac.findtext("comment")
# Literal selected source paragraphs establish identity and limits, without copying methods.
h = html.parse(str(F / "originals/PMC2856993.html"))
checks = []
for sel, fragments in [
    ('//*[@id="sec5"]/p[2]', ["S. aureus Newman genomic DNA", "Recombinant SfaB and SfaD"]),
    ('//*[@id="sec7"]/p', ["Using recombinant SfaB and SfaD"]),
    (
        '//*[@id="sec18"]/p[2]',
        ["R-configuration", "S configuration", "R configuration", "does not fit"],
    ),
]:
    text = norm(" ".join(" ".join(x.itertext()) for x in h.xpath(sel)))
    assert all(fragment in text for fragment in fragments), (sel, text)
    checks.append(
        {
            "selector": sel,
            "selected_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "selected_characters": len(text),
        }
    )
assert (
    next(r for r in raw["references"] if r["id"] == "PMID:20147287")["title"]
    == h.xpath('//meta[@name="citation_title"]/@content')[0]
)
assert all(len(r["title"]) < 400 for r in raw["references"])
ct = read(ORIGINALS / "PMID19138128.json")["resultList"]["result"][0]
assert (
    "SfnaD using the delta-amine" in ct["abstractText"]
    and "SfnaB utilizing the alpha-amine" in ct["abstractText"]
)
# Original-body integrity and honest web-only provenance.
ref_checks = []
for ref in raw["references"]:
    if ref["id"] == "PMID:19400778":
        assert "source_sha256" not in ref and "no local full-body hash" in ref["source_version"]
        continue
    path = p["reference_original_paths"][ref["id"]]
    assert sha(path) == ref["source_sha256"], ref["id"]
    ref_checks.append({"id": ref["id"], "path": path, "sha256": ref["source_sha256"]})
manifest = read(D / "staphyloferrin-a-source-manifest.json")
for item in manifest["sources"]:
    assert sha(item["path"]) == item["sha256"], item["path"]


# Negative guards target actual scientific/provenance failure modes.
def guard(doc):
    assert {r["id"] for r in doc["reactions"]} == {"RHEA:11585", "RHEA:59137", "RHEA:59141"}
    assert not doc.get("source_mappings"), "No exact native/current stereochemical equivalence"
    assert not any(n.get("category") == "complex" for n in doc["participants"])
    for e in doc["mechanistic_edges"]:
        if e["subject"] == "NCBIProtein:BAF68351.1" and e["object"] == "RHEA:11585":
            assert e["predicate"] == "enables"
            assert "inferred" in e["description"].lower()
        if e["predicate"] == "has_cofactor":
            assert (
                "inference" in e["description"].lower()
                or "qualified native" in e["description"].lower()
            )
    assert "stereospecific" in doc["description"] or "specifies" in doc["description"]
    assert "residue 532" in doc["description"]


guard(raw)
negative = []
for kind in [
    "truncate_racemization",
    "sfac_direct_catalysis",
    "false_stereo_exact_match",
    "invent_assembly",
]:
    bad = copy.deepcopy(raw)
    if kind == "truncate_racemization":
        bad["reactions"] = bad["reactions"][1:]
    elif kind == "sfac_direct_catalysis":
        next(
            e
            for e in bad["mechanistic_edges"]
            if e["subject"] == "NCBIProtein:BAF68351.1" and e["object"] == "RHEA:11585"
        )["predicate"] = "catalyzes"
    elif kind == "false_stereo_exact_match":
        bad["source_mappings"] = [
            {
                "subject": "MetaCyc:CPD-12589",
                "object": "CHEBI:142973",
                "predicate": "skos:exactMatch",
            }
        ]
    else:
        bad["participants"].append(
            {"id": "MetaCyc:invented", "label": "invented", "category": "complex"}
        )
    try:
        guard(bad)
    except AssertionError:
        negative.append(kind)
    else:
        raise AssertionError("Invalid mutation accepted: " + kind)
# The fresh identifier gate binds the final exact draft.
# Canonical authority source bodies stay unchanged.
sandbox = B / "authority-sandbox"
(sandbox / "data/pathways/staphyloferrin-a-biosynthesis.yaml").write_bytes(T.read_bytes())
assert not identifier_errors(sandbox)
nodes_file, edges_file = write_kgx([record], B / "kgx")
nodes = list(csv.DictReader(nodes_file.open(), delimiter="\t"))
exported = list(csv.DictReader(edges_file.open(), delimiter="\t"))
assert len(nodes) == 19 and len(exported) == 31
refs = {r["id"]: r for r in raw["references"]}
for edge, out in zip(raw["mechanistic_edges"], exported, strict=True):
    assert (out["subject"], out["predicate"], out["object"]) == (
        edge["subject"],
        LOCAL_PREDICATE_CURIES[edge["predicate"]],
        edge["object"],
    )
    assert json.loads(out["evidence"]) == edge["evidence"]
    assert out["description"] == edge.get("description", "")
    assert json.loads(out["reference_metadata"]) == [
        refs[i] for i in sorted({e["reference_id"] for e in edge["evidence"]})
    ]
assert sum(len(e["evidence"]) for e in raw["mechanistic_edges"]) == 59
# Source-native state/charge/stereochemistry replay is independently rerunnable with cached RDKit.
stereo = read(B / "scratch/stereochemistry.json")
assert [x["cip"] for x in stereo["rows"][-1]["citryl_centers"]] == ["R", "S"]
assert stereo["rows"][1]["citryl_centers"][0]["cip"] == "S"
assert stereo["rows"][0]["citryl_centers"][0]["cip"] == "?"
result = {
    "started_at": started,
    "finished_at": datetime.now(UTC).isoformat(),
    "status": "passed_external_author_replay",
    "target_sha256": sha(T),
    "counts": {
        "native_members": 3,
        "reactions": 3,
        "chemical_sides": 16,
        "balanced_reactions": 3,
        "participants": 14,
        "taxa": 1,
        "nodes": len(nodes),
        "edges": 31,
        "evidence": 59,
        "references": 28,
        "hashed_references": len(ref_checks),
        "web_only_references": 1,
    },
    "reference_hash_checks": ref_checks,
    "source_body_count": len(manifest["sources"]),
    "protein_comparisons": comp,
    "primary_locator_checks": checks,
    "native_stereo_bridges": [b["exact_equal"] for b in chem["native_current_bridges"]],
    "net": chem["route_net"],
    "negative_guards_rejected": negative,
    "actual_kgx": {
        "nodes_path": str(nodes_file),
        "nodes_sha256": sha(nodes_file),
        "edges_path": str(edges_file),
        "edges_sha256": sha(edges_file),
        "full_evidence_and_reference_metadata_preserved": True,
    },
    "checks": [
        "native and closed schema",
        "actual original RDF and ChEBI side/direction/balance replay",
        "three full native object boundaries and ordering",
        "exact Newman issuing protein identities and NCTC 8325 sequence differences",
        "selected original primary paragraph and title guards",
        "source-body hashes",
        "canonical unchanged identifier gate in external sandbox",
        "actual target KGX edge/evidence/reference equality",
    ],
    "limits": [
        "No shared authority integration or full corpus gates",
        "No independent scientific approval",
        "Cotton full text unavailable; individual SfaC activity remains inferred",
        "Beasley original text inspected through web only, no local body hash",
        "Bound product stereochemistry does not directly assay free intermediate or ionization",
        "Cofactor transfer remains explicitly qualified inference",
    ],
}
(D / "staphyloferrin-a-validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {
            "status": result["status"],
            "counts": result["counts"],
            "target_sha256": result["target_sha256"],
        },
        indent=2,
    )
)
