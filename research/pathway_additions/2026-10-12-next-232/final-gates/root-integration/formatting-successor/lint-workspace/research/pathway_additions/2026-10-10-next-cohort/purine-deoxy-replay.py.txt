"""Replay the curated record against externally retained native source bodies.

Run from the repository root with .venv/bin/python. No network or shared-file writes.
"""

import csv
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from pathwaymech.kgx import write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-cohort-evidence/purine-deoxy")
AUTH = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/purine-deoxyribonucleosides-degradation.yaml"
OUT = RAW / "author-replay.json"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert not strict_errors([TARGET], ROOT)
research = ROOT / "research/pathway_additions/2026-10-10-next-cohort"
projection = json.loads((research / "purine-deoxy-source-projection.json").read_text())
manifest = json.loads((research / "purine-deoxy-source-manifest.json").read_text())
config = {
    "native_reaction_map": projection["native_reaction_map"],
    "reference_bodies": {x["id"]: x["path"] for x in manifest["record_reference_bodies"]},
}
for ref in record["references"]:
    assert sha(config["reference_bodies"][ref["id"]]) == ref["source_sha256"], ref["id"]
# Replay native BioPAX directly; do not trust a curator's projection as authority.
rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
bp = "{http://www.biopax.org/release/biopax-level3.owl#}"
native = {}
for elem in ET.parse(RAW / "PW002077.owl").getroot():
    key = elem.get(rdf + "about") or "#" + elem.get(rdf + "ID", "")
    vals = defaultdict(list)
    for child in elem:
        vals[child.tag.split("}")[-1]].append(child.get(rdf + "resource") or child.text)
    native[key] = dict(vals)
pathway = native["http://identifiers.org/smpdb/SMP0002089"]
assert len([x for x in pathway["pathwayComponent"] if x.startswith("#Reactions/")]) == 6
assert set(config["native_reaction_map"]) == {r["id"].split(":")[1] for r in record["reactions"]}
# Structures in PathBank include broader stereochemical/protonation forms. These
# are role projections, explicitly NOT exact-match mappings between different species.
chemical_map = {
    "PW_C000058": "CHEBI:17172",
    "PW_C001420": "CHEBI:15377",
    "PW_C000050": "CHEBI:28997",
    "PW_C000784": "CHEBI:15343",
    "PW_C000024": "CHEBI:16708",
    "PW_C022608": "CHEBI:28938",
    "PW_C040034": "CHEBI:15378",
    "PW_C000813": "CHEBI:62877",
    "PW_C001104": "CHEBI:43474",
    "PW_C000086": "CHEBI:16235",
    "PW_C001042": "CHEBI:57259",
    "PW_C000869": "CHEBI:59776",
    "PW_C000102": "CHEBI:17368",
    "PW_C000068": "CHEBI:17256",
}
# Stream the independent complete Rhea RDF; merge repeated subject descriptions.
uri = "http://rdf.rhea-db.org/"
masters = {str(int(x)) for x in ["28190", "27742", "27750", "27738", "27658", "12821"]}
rows = [
    r
    for r in csv.DictReader((AUTH / "rhea-directions.tsv").open(), delimiter="\t")
    if r["RHEA_ID_MASTER"] in masters
]
nodes = defaultdict(lambda: defaultdict(list))
needed = {uri + r[k] for r in rows for k in r}
needed |= {uri + m + "_" + s for m in masters for s in ["L", "R"]}


def collect(wanted, participants=False):
    depth = 0
    with gzip.open(AUTH / "rhea.rdf.gz", "rb") as stream:
        for event, elem in ET.iterparse(stream, events=["start", "end"]):
            if event == "start":
                depth += 1
                continue
            if depth == 2:
                key = elem.get(rdf + "about")
                if key in wanted or (
                    participants
                    and any((key or "").startswith(uri + "Participant_" + m + "_") for m in masters)
                ):
                    for child in elem:
                        value = child.get(rdf + "resource") or child.text
                        if value is not None and value not in nodes[key][child.tag.split("}")[-1]]:
                            nodes[key][child.tag.split("}")[-1]].append(value)
                elem.clear()
            depth -= 1


collect(needed, True)
collect({c for obj in nodes.values() for c in obj.get("compound", [])})
chebi = sqlite3.connect(f"file:{AUTH / 'chebi.db'}?mode=ro", uri=True)
checks = []
side_count = 0
for row in rows:
    rid = "RHEA:" + row["RHEA_ID_LR"]
    master = row["RHEA_ID_MASTER"]
    assert uri + row["RHEA_ID_LR"] in nodes[uri + master]["directionalReaction"]
    assert uri + row["RHEA_ID_BI"] in nodes[uri + master]["bidirectionalReaction"]
    balance = Counter()
    charge = 0
    selected_sides = {}
    for role in ["substrates", "products"]:
        selected_sides[role] = []
        for side in nodes[uri + row["RHEA_ID_LR"]][role]:
            for pred, participants in nodes[side].items():
                if not re.fullmatch(r"contains\d+", pred):
                    continue
                coefficient = int(pred[8:])
                for participant in participants:
                    compound = nodes[nodes[participant]["compound"][0]]
                    cid = compound["accession"][0]
                    values = dict(
                        chebi.execute(
                            "select predicate,value from statements where subject=? "
                            "and predicate in "
                            "('chemrof:generalized_empirical_formula','chemrof:charge')",
                            (cid,),
                        )
                    )
                    assert values["chemrof:generalized_empirical_formula"] == compound["formula"][0]
                    assert int(values["chemrof:charge"]) == int(compound["charge"][0])
                    sign = -1 if role == "substrates" else 1
                    for atom, count in re.findall(r"([A-Z][a-z]?)(\d*)", compound["formula"][0]):
                        balance[atom] += sign * coefficient * int(count or 1)
                    charge += sign * coefficient * int(compound["charge"][0])
                    pred_local = "consumes" if role == "substrates" else "produces"
                    matches = [
                        e
                        for e in record["mechanistic_edges"]
                        if e["predicate"] == pred_local
                        and (e["subject"], e["object"])
                        == ((cid, rid) if role == "substrates" else (rid, cid))
                    ]
                    assert len(matches) == 1
                    evidence = matches[0]["evidence"][0]
                    assert (
                        side in evidence["source_locator"]
                        and participant in evidence["source_locator"]
                    )
                    assert f"rh:contains{coefficient}" in evidence["source_locator"]
                    assert f"coefficient {coefficient}" in evidence["source_assertion"]
                    selected_sides[role].append((cid, coefficient))
                    side_count += 1
    assert not any(balance.values()) and charge == 0, rid
    nid, meta, native_rhea = config["native_reaction_map"][row["RHEA_ID_LR"]]
    obj = native["#Reactions/" + nid]
    assert "#Reactions/" + nid in pathway["pathwayComponent"]
    left, right = (
        ("right", "left") if obj["conversionDirection"] == ["RIGHT_TO_LEFT"] else ("left", "right")
    )
    for role, native_role in [("substrates", left), ("products", right)]:
        expected = []
        for chemical in obj[native_role]:
            stoich = [
                native[s]
                for s in obj["participantStoichiometry"]
                if native[s]["physicalEntity"] == [chemical]
            ]
            assert len(stoich) == 1
            expected.append(
                (
                    chemical_map[chemical.split("/")[-1]],
                    int(float(stoich[0]["stoichiometricCoefficient"][0])),
                )
            )
        assert sorted(expected) == sorted(selected_sides[role]), (rid, role)
    xml = ET.parse(RAW / f"metacyc-{meta}.xml").getroot()
    frame = next(e for e in xml.iter() if e.get("frameid") == meta and e.get("detail") == "full")
    assert any(
        e.findtext("dblink-db") == "RHEA" and e.findtext("dblink-oid") == native_rhea
        for e in frame.findall("dblink")
    )
    checks.append(
        {
            "reaction": rid,
            "native_reaction": nid,
            "native_direction": obj["conversionDirection"][0],
            "native_Rhea_xref": native_rhea,
            "sides": selected_sides,
            "balance": "pass",
        }
    )
assert side_count == 22
# Native complex/component and protein crosswalks.
assembly = native["#ProteinComplex/4056"]
assert assembly["component"] == ["#Protein/6182"]
assert native[assembly["componentStoichiometry"][0]]["stoichiometricCoefficient"] == ["6.0"]
for frame_id, accession in [
    ("DEOD-MONOMER", "P0ABP8"),
    ("ADENODEAMIN-MONOMER", "P22333"),
    ("PPENTOMUT-MONOMER", "P0A6K6"),
    ("DEOXYRIBOSE-P-ALD-MONOMER", "P0A6L0"),
]:
    xml = ET.parse(RAW / f"metacyc-{frame_id}.xml").getroot()
    frame = next(
        e for e in xml.iter() if e.get("frameid") == frame_id and e.get("detail") == "full"
    )
    assert any(
        e.findtext("dblink-db") == "UNIPROT" and e.findtext("dblink-oid") == accession
        for e in frame.findall("dblink")
    )
    assert frame.find("species/Organism").get("frameid") == "TAX-511145"
    protein = json.loads((RAW / f"{accession}.json").read_text())
    assert protein["organism"]["taxonId"] == 83333
    assert (
        next(x for x in record["participants"] if x["id"] == "UniProtKB:" + accession)["label"]
        == protein["proteinDescription"]["recommendedName"]["fullName"]["value"]
    )
    assert any(
        x["database"] == "GO" and x["id"] == "GO:0005829"
        for x in protein["uniProtKBCrossReferences"]
    )
# Every ChEBI node is independently checked against the complete ontology DB.
for node in record["participants"]:
    if node["id"].startswith("CHEBI:"):
        assert (
            chebi.execute(
                "select value from statements where subject=? and predicate='rdfs:label'",
                (node["id"],),
            ).fetchone()[0]
            == node["label"]
        )
# Actual exporter, then TSV readback verifies all evidence and descriptions.
kgx_dir = RAW / "kgx"
write_kgx([validated], kgx_dir)
edges = list(csv.DictReader((kgx_dir / "edges.tsv").open(), delimiter="\t"))
nodes_out = list(csv.DictReader((kgx_dir / "nodes.tsv").open(), delimiter="\t"))
assert len(edges) == len(record["mechanistic_edges"])
for out, original in zip(edges, record["mechanistic_edges"], strict=True):
    assert json.loads(out["evidence"]) == original["evidence"]
    assert out["description"] == original.get("description", "")
    assert json.loads(out["reference_metadata"])
assert (
    next(n for n in nodes_out if n["id"] == "MetaCyc:DEOD-CPLX")["category"]
    == "biolink:MacromolecularComplex"
)
receipt = {
    "status": "pass",
    "target_sha256": sha(TARGET),
    "native_sha256": sha(RAW / "PW002077.owl"),
    "rhea_gzip_sha256": sha(AUTH / "rhea.rdf.gz"),
    "checks": [
        "native schema",
        "closed LinkML schema",
        "all reference body hashes",
        "22 native and full-RDF reaction sides and coefficients",
        "six atom/charge balances against complete ChEBI DB",
        "six MetaCyc/Rhea directional bridges",
        "native assembly and four UniProt/MG1655 crosswalks",
        "all ChEBI canonical labels",
        "actual KGX evidence, descriptions and complex category",
    ],
    "reaction_replay": checks,
    "counts": {
        "participants": len(record["participants"]),
        "reactions": len(record["reactions"]),
        "edges": len(edges),
        "evidence": sum(len(e["evidence"]) for e in record["mechanistic_edges"]),
        "kgx_nodes": len(nodes_out),
        "references": len(record["references"]),
    },
}
OUT.write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({"status": "pass", "receipt": str(OUT), "counts": receipt["counts"]}))
