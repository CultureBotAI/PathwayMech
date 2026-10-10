"""Replay Sbm chemistry/assembly/reference checks against preserved issuing-authority bodies."""

import argparse
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import yaml

from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--raw", type=Path, required=True)
parser.add_argument("--authorities", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
repo = Path(__file__).resolve().parents[3]
target = repo / "data/pathways/succinate-to-propanoate.yaml"
record = yaml.safe_load(target.read_text())
validate_record(record)
assert not strict_errors([target], repo)
rh = "http://rdf.rhea-db.org/"
rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
masters = ["22888", "27666", "28010"]
selected = {str(int(m) + i) for m in masters for i in range(4)}
nodes = {}
with gzip.open(args.authorities / "rhea.rdf.gz", "rb") as stream:
    for _, element in ET.iterparse(stream, events=("end",)):
        if element.tag != "{" + rdf + "}Description":
            continue
        uri = element.get("{" + rdf + "}about", "")
        name = uri.removeprefix(rh)
        if (
            name in selected
            or name.startswith("Compound_")
            or any(
                name.startswith(m + "_") or name.startswith("Participant_" + m + "_")
                for m in masters
            )
        ):
            properties = nodes.setdefault(uri, {})
            for child in element:
                key = child.tag.rsplit("}", 1)[-1]
                value = child.get("{" + rdf + "}resource", child.text)
                if value not in properties.setdefault(key, []):
                    properties[key].append(value)
        element.clear()


def side(rid, field):
    """Follow actual directed reaction -> side -> participant -> compound -> ChEBI."""
    result = {}
    for pred, participants in nodes[nodes[rh + rid][field][0]].items():
        if not re.fullmatch(r"contains[0-9]+", pred):
            continue
        for participant in participants:
            compound = nodes[participant]["compound"][0]
            ident = "CHEBI:" + nodes[compound]["chebi"][0].rsplit("_", 1)[-1]
            result[ident] = int(pred[8:])
    return result


rxns = {
    rid: {f: side(rid, f) for f in ["substrates", "products"]}
    for rid in ["22890", "27667", "28011"]
}
expected = set()
for rid, rxn in rxns.items():
    expected.update((c, "consumes", "RHEA:" + rid) for c in rxn["substrates"])
    expected.update(("RHEA:" + rid, "produces", c) for c in rxn["products"])
actual = {
    (e["subject"], e["predicate"], e["object"])
    for e in record["mechanistic_edges"]
    if e["predicate"] in {"consumes", "produces"}
}
assert actual == expected
assert len(actual) == 10
assert nodes[rh + "22890"]["substrates"] == [rh + "22888_R"]
con = sqlite3.connect("file:" + str(args.authorities / "chebi.db") + "?mode=ro", uri=True)
chem = {}
for ident in {c for rx in rxns.values() for s in rx.values() for c in s} | {"CHEBI:18408"}:
    chem[ident] = dict(
        con.execute(
            "SELECT predicate,value FROM statements WHERE subject=? AND predicate IN (?,?,?)",
            (ident, "rdfs:label", "chemrof:generalized_empirical_formula", "chemrof:charge"),
        )
    )
    participant = next(n for n in record["participants"] if n["id"] == ident)
    assert participant["label"] == chem[ident]["rdfs:label"]


def balance(items):
    counts = Counter()
    for ident, coefficient in items.items():
        formula = chem[ident]["chemrof:generalized_empirical_formula"]
        for atom, number in re.findall(r"([A-Z][a-z]*)([0-9]*)", formula):
            counts[atom] += coefficient * int(number or 1)
        counts["charge"] += coefficient * int(chem[ident]["chemrof:charge"])
    return dict(counts)


net = Counter()
for rxn in rxns.values():
    assert balance(rxn["substrates"]) == balance(rxn["products"])
    net.update(rxn["products"])
    net.subtract(rxn["substrates"])
assert {k: v for k, v in net.items() if v} == {
    "CHEBI:30031": -1,
    "CHEBI:15378": -1,
    "CHEBI:17272": 1,
    "CHEBI:16526": 1,
}
for complex_id, monomer_id, accession, copies in [
    ("CPLX0-7741", "METHYLMALONYL-COA-MUT-MONOMER", "P27253", "2"),
    ("CPLX0-254", "G7516-MONOMER", "P52045", "6"),
]:
    root = ET.parse(args.raw / f"metacyc-{complex_id}.xml").getroot().find("Protein")
    assert root.find("component/Protein").get("frameid") == monomer_id
    assert root.findtext("component/coefficient") == copies
    root = ET.parse(args.raw / f"metacyc-{monomer_id}.xml").getroot().find("Protein")
    assert accession in [
        d.findtext("dblink-oid")
        for d in root.findall("dblink")
        if d.findtext("dblink-db") == "UNIPROT"
    ]
source_files = [p for p in args.raw.iterdir() if p.suffix in {".xml", ".json", ".pdf", ".html"}]
source_files.append(args.authorities / "rhea.rdf.gz")
by_hash = {hashlib.sha256(p.read_bytes()).hexdigest(): p for p in source_files}
for ref in record["references"]:
    assert ref["source_sha256"] in by_hash, ref["id"]
assert all("context" not in e for e in record["mechanistic_edges"])
assert all("quote" not in ev for e in record["mechanistic_edges"] for ev in e["evidence"])
result = {
    "checked_at": datetime.now(UTC).isoformat(),
    "target_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    "status": "passed",
    "reaction_sides": rxns,
    "chemical_edges_replayed": 10,
    "references_rehashed": len(record["references"]),
    "edges": len(record["mechanistic_edges"]),
    "evidence": sum(len(e["evidence"]) for e in record["mechanistic_edges"]),
    "checks": [
        "local contract",
        "closed schema",
        "full Rhea RDF directed sides",
        "independent ChEBI labels/formulas/charges",
        "all reaction and net balance",
        "two exact native assembly and UniProt mappings",
        "exact reference body hashes",
    ],
    "limits": "This author replay does not independently settle ScpB specificity or native flux.",
}
args.output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
