"""Replay the full methylcitrate route and its uncertainty-preserving source mapping."""

import collections
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

from pathwaymech.kgx import kgx_edges, kgx_nodes, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path(__file__).resolve().parents[3]
DOSSIER = Path(__file__).resolve().parent
RAW = Path("/private/tmp/pathwaymech-next-195-evidence/propanoyl")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/2-methylcitrate-cycle-i.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
START = datetime.datetime.now(datetime.UTC).isoformat()


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def native(frame):
    return next(
        x
        for x in ET.parse(RAW / f"metacyc-{frame}.xml").iter()
        if x.get("frameid") == frame and x.get("detail") == "full"
    )


record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert not strict_errors([TARGET], ROOT)
manifest = json.loads((DOSSIER / "propanoyl-source-manifest.json").read_text())
projection = json.loads((DOSSIER / "propanoyl-source-projection.json").read_text())
assert projection["record_sha256"] == digest(TARGET)
hashes = {}
for source in (
    manifest["fresh_original_bodies"]
    + manifest["reused_bodies"]
    + manifest["authority_inputs"]
    + manifest["additional_inputs"]
):
    if source.get("path"):
        assert digest(source["path"]) == source["sha256"], source["path"]
        hashes[source["path"]] = source["sha256"]
for reference in record["references"]:
    assert reference["source_sha256"] in hashes.values(), reference["id"]

# Rebuild exact RDF objects from the compressed official release, merging repeated subjects.
text = gzip.open(CACHE / "rhea.rdf.gz", "rt").read()
starts = collections.defaultdict(list)
for match in re.finditer(r'<rdf:Description rdf:about="([^"]+)">', text):
    starts[match[1]].append(match.start())
wrapper = (
    '<root xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" '
    'xmlns:rh="http://rdf.rhea-db.org/" '
    'xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">'
)
nodes = {}
for uri in projection["rhea_original_nodes"]:
    values = {}
    for start in starts[uri]:
        end = text.index("</rdf:Description>", start) + len("</rdf:Description>")
        element = ET.fromstring(wrapper + text[start:end] + "</root>")[0]
        for child in element:
            key = child.tag.split("}", 1)[1]
            value = child.get(RDF + "resource") or child.text
            if value not in values.setdefault(key, []):
                values[key].append(value)
    nodes[uri] = values
assert nodes == projection["rhea_original_nodes"]
del text

selected = ["20374", "57493", "57497", "17943", "16810"]
masters = ["20373", "57492", "57496", "17941", "16809"]
directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    master, lr, rl, bi = line.split("\t")
    directions[master] = {"left_to_right": lr, "right_to_left": rl, "reversible": bi}
for master, rid in zip(masters, selected, strict=True):
    reaction = next(x for x in record["reactions"] if x["id"] == "RHEA:" + rid)
    assert directions[master][reaction["direction"]] == rid
    assert reaction["label"] == nodes[RH + rid]["label"][0]
for child, parent, directed in [("23780", "57492", "57493"), ("17725", "57496", "57497")]:
    assert RH + parent in nodes[RH + child]["subClassOf"]
    assert RH + directed in nodes[RH + parent]["directionalReaction"]
    assert RH + "Approved" in nodes[RH + parent]["status"]
    assert "http://rdf.ncbi.nlm.nih.gov/pubmed/28956599" in nodes[RH + parent]["citation"]

rows = []
for rid in selected:
    for side_name in ["substrates", "products"]:
        for side in nodes[RH + rid][side_name]:
            for part in nodes[side]["contains"]:
                compound = nodes[part]["compound"][0]
                cid = nodes[compound]["chebi"][0].rsplit("/", 1)[-1].replace("_", ":")
                coefficients = [
                    int(key[8:])
                    for key, values in nodes[side].items()
                    if key.startswith("contains") and key != "contains" and part in values
                ]
                assert len(coefficients) == 1
                rows.append(("RHEA:" + rid, side_name, cid, coefficients[0]))
expected_sides = collections.Counter(rows)
assert len(rows) == 21
actual = collections.Counter()
for edge in record["mechanistic_edges"]:
    if edge["predicate"] in {"consumes", "produces"}:
        consuming = edge["predicate"] == "consumes"
        rid = edge["object"] if consuming else edge["subject"]
        cid = edge["subject"] if consuming else edge["object"]
        coefficient = int(
            re.search(r"coefficient (\d+)", edge["evidence"][0]["source_assertion"])[1]
        )
        actual[(rid, "substrates" if consuming else "products", cid, coefficient)] += 1
assert actual == expected_sides
assert ("RHEA:57493", "products", "CHEBI:15598", 1) in rows
assert ("RHEA:57497", "substrates", "CHEBI:15598", 1) in rows

connection = sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True)
chem = {}
for cid in projection["chemistry"]:
    chem[cid] = {
        p: v
        for p, v in connection.execute(
            "select predicate,value from statements where subject=? "
            "and (predicate like ? or predicate=?)",
            (cid, "chemrof:%", "rdfs:label"),
        )
        if v is not None
    }
assert chem == projection["chemistry"]
assert "/t" not in chem["CHEBI:15598"]["chemrof:inchi_string"]
assert "/t3-,7+/m1/s1" in chem["CHEBI:58853"]["chemrof:inchi_string"]
assert "/t3-,7-/m1/s1" in chem["CHEBI:10860"]["chemrof:inchi_string"]
assert chem["CHEBI:15598"]["chemrof:generalized_empirical_formula"] == "C7H7O7"
assert chem["CHEBI:15598"]["chemrof:charge"] == "-3"
balances = {}
net = collections.Counter()
for rid in selected:
    atoms = collections.Counter()
    charge = 0
    for reaction, side, cid, coeff in rows:
        if reaction != "RHEA:" + rid:
            continue
        signed = coeff * (-1 if side == "substrates" else 1)
        formula = chem[cid]["chemrof:generalized_empirical_formula"]
        tokens = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
        assert "".join(a + n for a, n in tokens) == formula
        for atom, count in tokens:
            atoms[atom] += signed * int(count or 1)
        charge += signed * int(chem[cid]["chemrof:charge"])
        net[cid] += signed
    assert not any(atoms.values()) and charge == 0
    balances[rid] = {"atoms": dict(atoms), "charge": charge}

pathway = native("PWY0-42")
native_ids = {x.get("frameid") for x in pathway.findall("reaction-list/Reaction")}
assert native_ids == set(projection["metacyc_native_members"])
membership = {
    x["subject"]
    for x in record["mechanistic_edges"]
    if x["predicate"] == "part_of" and x["object"] == record["id"]
}
assert membership == {"RHEA:" + x for x in selected}
assert {x["id"] for x in record["reactions"]} == membership
for comp, mono, count, protein in [
    ("CPLX0-251", "G6198-MONOMER", 2, "P31660"),
    ("CPLX0-1021", "G6196-MONOMER", 4, "P77541"),
]:
    component = native(comp).find("component")
    assert component.find("Protein").get("frameid") == mono
    assert int(component.findtext("coefficient")) == count
    assert ("UNIPROT", protein) in [
        (x.findtext("dblink-db"), x.findtext("dblink-oid")) for x in native(mono).findall("dblink")
    ]
for accession in projection["proteins"]:
    protein = json.loads((RAW / f"uniprot-{accession}.json").read_text())
    for key, value in projection["proteins"][accession].items():
        assert protein[key] == value
for accession in ["P31660", "P77243"]:
    cautions = [
        x for x in projection["proteins"][accession]["comments"] if x["commentType"] == "CAUTION"
    ]
    assert len(cautions) == 1
    assert "uncertainty" in cautions[0]["texts"][0]["value"]
abstract = json.loads((RAW / "pmid-28956599.json").read_text())["resultList"]["result"][0][
    "abstractText"
]
assert "PrpC (from Escherichia coli)" in abstract
assert "physiological pathways proceed via (Z)-2-methylaconitate" in abstract
assert "PrpD exhibited the same lack of stereospecificity" in abstract
assert (
    digest(RAW / "primary-2017-si.pdf")
    == "2380572de62615d206018042902b221f945f421d72961bb54f6c7cddba3361a2"
)
source_2025 = ET.parse(RAW / "primary-PMC11982470.xml").findall(".//passage")
assert source_2025[55].findtext("offset") == "36579"
assert "Commercial standards" in source_2025[55].findtext("text")

active_nodes = {record["id"]} | {
    x["id"] for kind in ["taxa", "participants", "reactions"] for x in record[kind]
}
assert not active_nodes.intersection({"CHEBI:58853", "CHEBI:10860", "RHEA:23781", "RHEA:17726"})
assert set(x["id"] for x in record["participants"] if x["category"] == "complex") == {
    "MetaCyc:CPLX0-251",
    "MetaCyc:CPLX0-1021",
}
assert all(x["source_sha256"] in hashes.values() for x in record["references"])
write_kgx([validated], RAW / "kgx")
exported = kgx_edges([validated])
assert len(exported) == len(record["mechanistic_edges"])
for original, exported_edge in zip(record["mechanistic_edges"], exported, strict=True):
    assert json.loads(exported_edge.evidence) == original["evidence"]
assert {x.id for x in kgx_nodes([validated])} == active_nodes
export_triples = {(x.subject, x.object) for x in exported}
assert ("CHEBI:15598", "RHEA:57497") in export_triples
assert ("RHEA:57493", "CHEBI:15598") in export_triples
assert all(
    x.subject not in {"CHEBI:58853", "CHEBI:10860"}
    and x.object not in {"CHEBI:58853", "CHEBI:10860"}
    for x in exported
)
evidence_count = sum(len(x["evidence"]) for x in record["mechanistic_edges"])
report = {
    "started_at": START,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "status": "passed",
    "target_sha256": digest(TARGET),
    "script_sha256": digest(__file__),
    "checks": [
        "native and closed schemas",
        "all retained source body hashes",
        "fresh complete RDF object replay, including generic parents and primary citation",
        "all 21 chemical sides and exact source directions",
        "five atom and charge balances",
        "five-member native boundary",
        "two native assemblies and exact UniProt bridges",
        "all six current protein projections",
        "2017 abstract and full SI identity",
        "2025 primary source locator",
        "actual KGX preserves all local nodes and edges",
        "no disputed stereospecific node or reaction exported",
    ],
    "source_hashes": hashes,
    "balances": balances,
    "net_coefficient_products_positive": {k: v for k, v in net.items() if v},
    "counts": {
        "participants": len(record["participants"]),
        "reactions": len(record["reactions"]),
        "edges": len(record["mechanistic_edges"]),
        "evidence": evidence_count,
        "kgx_nodes": len(kgx_nodes([validated])),
    },
    "limitations": [
        "Author source replay, not independent scientific review.",
        "Exact methylcitrate stereochemistry remains unresolved.",
        "Full-corpus render, validation, tests and identifier snapshots are coordinated by root.",
    ],
}
(DOSSIER / "propanoyl-validation.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
