#!/usr/bin/env python3
"""Inventory every yeast GO-CAM chemical side against independently matched proteins.

Exact identity, conjugate acid/base and broader/narrower classes remain distinct
in the output. A compatible comparison is not an assertion of mass balance,
complete enzyme coverage or physiological irreversibility. Unmatched terms need
curator disposition; this script never modifies pathway records.
"""

import argparse
import collections
import functools
import hashlib
import json
import sqlite3
from pathlib import Path

import yaml

from scripts.audit_metacyc_causal_graphs import read_rhea

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--root", type=Path, default=Path.cwd())
parser.add_argument("--uniprot-json", type=Path, required=True)
parser.add_argument("--uniprot-provenance", type=Path, required=True)
parser.add_argument("--rhea-rdf", type=Path, required=True)
parser.add_argument("--directions", type=Path, required=True)
parser.add_argument("--chebi-db", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
ROOT = args.root
raw = args.uniprot_json.read_bytes()
metadata = json.loads(args.uniprot_provenance.read_text())
if hashlib.sha256(raw).hexdigest() != metadata["sha256"]:
    raise ValueError("UniProt source checksum mismatch")
source = json.loads(raw)
proteins = {}
uniprot = {}
ambiguous = set()
for i, p in enumerate(source["results"]):
    uniprot["UniProtKB:" + p["primaryAccession"]] = (p, i)
    for x in p.get("uniProtKBCrossReferences", []):
        if x["database"] == "SGD":
            key = "SGD:" + x["id"]
            if key in proteins:
                ambiguous.add(key)
            proteins[key] = (p, i)
proteins.update(uniprot)
records = []
selected = set()
for f in sorted((ROOT / "data/pathways").rglob("*.yaml")):
    r = yaml.load(f.read_text(), Loader=yaml.CSafeLoader)
    if r["id"].startswith("gomodel:") and any(n["id"] == "NCBITaxon:559292" for n in r["taxa"]):
        records.append((f, r))
        for n in r["participants"]:
            if n["id"] in ambiguous:
                raise ValueError("ambiguous selected protein " + n["id"])
            if n["id"] in proteins:
                for c in proteins[n["id"]][0].get("comments", []):
                    if c["commentType"] == "CATALYTIC ACTIVITY":
                        selected.update(
                            x["id"].split(":")[1]
                            for x in c["reaction"].get("reactionCrossReferences", [])
                            if x["id"].startswith("RHEA:")
                        )
if not records or not selected:
    raise ValueError("No yeast records or independent catalytic annotations")
rhea = read_rhea(args.rhea_rdf, args.directions, selected)
con = sqlite3.connect(f"file:{args.chebi_db}?mode=ro", uri=True)


@functools.lru_cache(None)
def term(id):
    rows = con.execute(
        "SELECT predicate,object,value FROM statements WHERE subject=?", (id,)
    ).fetchall()
    props = collections.defaultdict(list)
    for pred, obj, val in rows:
        props[pred].append(obj or val)
    return props


@functools.lru_cache(None)
def ancestors(id):
    found = {id}
    todo = [id]
    while todo:
        current = todo.pop()
        for parent in term(current)["rdfs:subClassOf"]:
            if parent.startswith("CHEBI:") and parent not in found:
                found.add(parent)
                todo.append(parent)
    return found


@functools.lru_cache(None)
def charge_family(id):
    found = {id}
    todo = [id]
    while todo:
        current = todo.pop()
        for axiom in term(current)["rdfs:subClassOf"]:
            if not axiom.startswith("_:"):
                continue
            data = term(axiom)
            prop = data["owl:onProperty"]
            if any(p in {"RO:0018033", "RO:0018034"} for p in prop):
                for other in data["owl:someValuesFrom"]:
                    if other.startswith("CHEBI:") and other not in found:
                        found.add(other)
                        todo.append(other)
    return found


@functools.lru_cache(None)
def relationship(a, b):
    if a == b:
        return "exact"
    if not a.startswith("CHEBI:") or not b.startswith("CHEBI:"):
        return None
    if b in charge_family(a) or a in charge_family(b):
        return "source_conjugate"
    ka = term(a)["chemrof:inchi_key_string"]
    kb = term(b)["chemrof:inchi_key_string"]
    if ka and kb and ka[0].rsplit("-", 1)[0] == kb[0].rsplit("-", 1)[0]:
        return "same_inchi_except_protonation"
    if a in ancestors(b):
        return "observed_broader_class"
    if b in ancestors(a):
        return "observed_narrower_class"
    for x in charge_family(a):
        for y in charge_family(b):
            if x in ancestors(y) or y in ancestors(x):
                return "class_plus_conjugate"
    return None


def compare(obs, exp):
    pairs = []
    remaining = []
    for a in obs:
        matches = [(b, relationship(a, b)) for b in exp if relationship(a, b)]
        if matches:
            pairs.append({"observed": a, "candidates": matches})
        else:
            remaining.append(a)
    return {
        "pairs": pairs,
        "unmatched_observed": remaining,
        "unrepresented_source": [b for b in exp if not any(relationship(a, b) for a in obs)],
    }


ledger = []
for file, r in records:
    nodes = {n["id"]: n for n in r["participants"] + r["reactions"]}
    parts = collections.defaultdict(list)
    for e in r["mechanistic_edges"]:
        if e["predicate"] == "has_part":
            parts[e["subject"]].append(e["object"])
    for activity in r["reactions"]:
        aid = activity["id"]
        edges = [
            e
            for e in r["mechanistic_edges"]
            if e["subject"] == aid and e["predicate"] in {"has_input", "has_output"}
        ]
        obs = {
            k: sorted({e["object"] for e in edges if e["predicate"] == k})
            for k in ["has_input", "has_output"]
        }
        enabled = sorted(
            {
                e["subject"]
                for e in r["mechanistic_edges"]
                if e["predicate"] == "enables" and e["object"] == aid
            }
        )
        expanded = set(enabled)
        todo = list(enabled)
        while todo:
            en = todo.pop()
            for part in parts[en]:
                if part not in expanded:
                    expanded.add(part)
                    todo.append(part)
        candidates = []
        protein_info = []
        for en in sorted(expanded):
            if en not in proteins:
                continue
            p, index = proteins[en]
            pis = []
            for ci, c in enumerate(p.get("comments", [])):
                if c["commentType"] != "CATALYTIC ACTIVITY":
                    continue
                for x in c["reaction"].get("reactionCrossReferences", []):
                    if not x["id"].startswith("RHEA:"):
                        continue
                    rid = x["id"]
                    pis.append(rid)
                    rr = rhea[rid]
                    sides = list(rr["sides"].values())
                    if len(sides) != 2:
                        continue
                    for rev in [False, True]:
                        a, b = sides[::-1] if rev else sides
                        left = compare(obs["has_input"], a)
                        right = compare(obs["has_output"], b)
                        score = sum(
                            len(set(v["unmatched_observed"]) - {"CHEBI:15378", "CHEBI:15377"})
                            for v in [left, right]
                        )
                        score2 = sum(len(v["unrepresented_source"]) for v in [left, right])
                        candidates.append(
                            {
                                "protein": en,
                                "accession": p["primaryAccession"],
                                "index": index,
                                "comment_index": ci,
                                "rhea": rid,
                                "reaction": c["reaction"]["name"],
                                "source_inputs": a,
                                "source_outputs": b,
                                "reverse_side_order": rev,
                                "comparisons": {"has_input": left, "has_output": right},
                                "unmatched_count": score,
                                "unrepresented_source_count": score2,
                            }
                        )
            protein_info.append(
                {
                    "id": en,
                    "accession": p["primaryAccession"],
                    "source_index": index,
                    "rhea": pis,
                    "function": [
                        c for c in p.get("comments", []) if c["commentType"] == "FUNCTION"
                    ],
                }
            )
        candidates.sort(key=lambda c: (c["unmatched_count"], c["unrepresented_source_count"]))
        best = candidates[0] if candidates else None
        row = {
            "record": r["id"],
            "path": str(file.relative_to(ROOT)),
            "activity": activity,
            "observed": obs,
            "enablers": enabled,
            "mapped_proteins": protein_info,
            "candidates": candidates,
            "best": best,
            "status": "no_catalytic_authority"
            if best is None
            else (
                "compatible_at_stated_specificity"
                if best["unmatched_count"] == 0
                else "requires_review"
            ),
        }
        ledger.append(row)
labels = {
    id: term(id)["rdfs:label"]
    for row in ledger
    for id in row["observed"]["has_input"] + row["observed"]["has_output"]
}
for row in ledger:
    for c in row["candidates"]:
        for id in c["source_inputs"] + c["source_outputs"]:
            labels[id] = term(id)["rdfs:label"]
out = {
    "records": len(records),
    "activities": len(ledger),
    "source": metadata,
    "rhea_sha256": hashlib.file_digest(args.rhea_rdf.open("rb"), "sha256").hexdigest(),
    "rhea_directions_sha256": hashlib.file_digest(args.directions.open("rb"), "sha256").hexdigest(),
    "chebi_sha256": hashlib.file_digest(args.chebi_db.open("rb"), "sha256").hexdigest(),
    "chebi_sha256_scope": "uncompressed_semantic_sql_database",
    "ledger": ledger,
    "labels": labels,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(out, indent=2) + "\n")
print(
    "records",
    len(records),
    "activities",
    len(ledger),
    collections.Counter(r["status"] for r in ledger),
)
