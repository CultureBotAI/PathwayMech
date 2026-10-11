"""Replay retained primary/native bodies for the complete CMP-Kdo record.

Run from the repository root. Requires external raw and pinned authority caches;
never fetches network data or modifies shared snapshots/generated publication.
"""

import csv
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import UTC, datetime
from functools import cache
from pathlib import Path

import yaml

from pathwaymech.kgx import write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-184-evidence/kdo")
AUTH = Path("/private/tmp/pathwaymech-curation-authorities")
OUT = ROOT / "research/pathway_additions/2026-10-11-next-184"
TARGET = ROOT / "data/pathways/cmp-kdo-biosynthesis.yaml"
URI = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


@cache
def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def frame(name, tag):
    root = ET.parse(RAW / (name + ".xml")).getroot()
    assert root.find("metadata/PGDB").get("orgid") == "META"
    assert root.find("metadata/PGDB").get("version") == "22.5"
    node = root.find(tag)
    assert node.get("frameid") == name and node.get("detail") == "full"
    return node


def xref(node, database, identifier):
    return any(
        x.findtext("dblink-db") == database
        and x.findtext("dblink-oid") == identifier
        and x.findtext("dblink-relationship") == "unification"
        for x in node.findall("dblink")
    )


r = yaml.safe_load(TARGET.read_text())
validated = validate_record(r)
assert not strict_errors([TARGET], ROOT)
manifest = json.loads((OUT / "kdo-source-manifest.json").read_text())
assert manifest["target_sha256"] == sha(TARGET)
bodies = {x["id"]: Path(x["path"]) for x in manifest["record_reference_bodies"]}
for reference in r["references"]:
    assert sha(bodies[reference["id"]]) == reference["source_sha256"]
for artifact in manifest["artifacts"]:
    if artifact.get("path"):
        assert sha(artifact["path"]) == artifact["sha256"]
    assert not artifact.get("headers"), "No response headers retained in this author manifest"
assert sha(AUTH / "rhea.rdf.gz") == manifest["mechanism_rhea"]["sha256"]

chebi = sqlite3.connect(f"file:{AUTH / 'chebi.db'}?mode=ro", uri=True)
go = sqlite3.connect(f"file:{AUTH / 'go.db'}?mode=ro", uri=True)
assert (
    go.execute(
        "select value from statements where subject=? and predicate='rdfs:label'", (r["id"],)
    ).fetchone()[0]
    == r["label"]
)
assert go.execute(
    "select value from statements where subject=? and predicate='oio:hasDbXref' "
    "and value='MetaCyc:PWY-1269'",
    (r["id"],),
).fetchone()
for node in r["participants"]:
    if node["id"].startswith("CHEBI:"):
        assert (
            chebi.execute(
                "select value from statements where subject=? and predicate='rdfs:label'",
                (node["id"],),
            ).fetchone()[0]
            == node["label"]
        )

pathway = frame("PWY-1269", "Pathway")
expected = {
    "DARAB5PISOM-RXN": "R2L",
    "RXN-16804": "L2R",
    "KDO-8PSYNTH-RXN": "L2R",
    "KDO-8PPHOSPHAT-RXN": "L2R",
    "CPM-KDOSYNTH-RXN": "L2R",
}
assert {n.get("frameid") for n in pathway.findall("reaction-list/Reaction")} == set(expected)
assert {
    n.find("Reaction").get("frameid"): n.findtext("direction")
    for n in pathway.findall("reaction-layout")
} == expected
projection = json.loads((OUT / "kdo-source-projection.json").read_text())
assert projection["target_sha256"] == sha(TARGET)
assert {x["id"].split(":", 1)[1] for x in projection["native_pathway"]["members"]} == set(expected)
for member in projection["native_pathway"]["members"]:
    name = member["id"].split(":", 1)[1]
    node = frame(name, "Reaction")
    assert member["sha256"] == sha(RAW / (name + ".xml"))
    for side in ["left", "right"]:
        actual = [
            {
                "id": x.find("Compound").get("frameid"),
                "coefficient": int(x.findtext("coefficient") or 1),
            }
            for x in node.findall(side)
        ]
        assert actual == member[side]
spont = frame("RXN-16804", "Reaction")
assert (
    spont.findtext("spontaneous") == "true" and spont.findtext("reaction-direction") == "REVERSIBLE"
)
spont_node = next(n for n in r["reactions"] if n["id"] == "MetaCyc:RXN-16804")
assert spont_node["direction"] == "reversible" and "category" not in spont_node
assert not any(
    e["object"] == spont_node["id"] and e["predicate"] in {"enables", "catalyzes"}
    for e in r["mechanistic_edges"]
)
assert xref(frame("ARABINOSE-5P", "Compound"), "CHEBI", "57693")
assert xref(frame("CPD-18118", "Compound"), "CHEBI", "85971")

masters = {"23104", "14053", "11500", "23448"}
rows = [
    row
    for row in csv.DictReader((AUTH / "rhea-directions.tsv").open(), delimiter="\t")
    if row["RHEA_ID_MASTER"] in masters
]
assert len(rows) == 4
wanted = {URI + v for row in rows for v in row.values()}
wanted |= {URI + m + "_" + side for m in masters for side in ["L", "R"]}
nodes = defaultdict(lambda: defaultdict(list))


def collect(want, participants=False):
    depth = 0
    with gzip.open(AUTH / "rhea.rdf.gz", "rb") as stream:
        for event, element in ET.iterparse(stream, events=["start", "end"]):
            if event == "start":
                depth += 1
                continue
            if depth == 2:
                key = element.get(RDF + "about")
                if key in want or (
                    participants
                    and any((key or "").startswith(URI + "Participant_" + m + "_") for m in masters)
                ):
                    for child in element:
                        p = child.tag.split("}")[-1]
                        v = child.get(RDF + "resource") or child.text
                        if v is not None and v not in nodes[key][p]:
                            nodes[key][p].append(v)
                element.clear()
            depth -= 1


collect(wanted, True)
collect({c for n in nodes.values() for c in n.get("compound", [])})
replay = []
side_count = 0
for native, master, selected, direction in [
    ("DARAB5PISOM-RXN", "23104", "23106", "right_to_left"),
    ("KDO-8PSYNTH-RXN", "14053", "14054", "left_to_right"),
    ("KDO-8PPHOSPHAT-RXN", "11500", "11501", "left_to_right"),
    ("CPM-KDOSYNTH-RXN", "23448", "23449", "left_to_right"),
]:
    rid = "RHEA:" + selected
    assert URI + selected in nodes[URI + master]["directionalReaction"]
    assert xref(frame(native, "Reaction"), "RHEA", "23107" if master == "23104" else selected)
    if master == "23104":
        assert URI + "23107" in nodes[URI + master]["bidirectionalReaction"]
    rn = next(n for n in r["reactions"] if n["id"] == rid)
    assert rn["direction"] == direction and rn["label"] == nodes[URI + selected]["label"][0]
    balance = Counter()
    charge = 0
    sides = {}
    for role in ["substrates", "products"]:
        sides[role] = []
        for side in nodes[URI + selected][role]:
            for pred, parts in nodes[side].items():
                if not re.fullmatch(r"contains\d+", pred):
                    continue
                coefficient = int(pred[8:])
                for part in parts:
                    c = nodes[nodes[part]["compound"][0]]
                    cid = c["accession"][0]
                    vals = dict(
                        chebi.execute(
                            "select predicate,value from statements where subject=? "
                            "and predicate in ('chemrof:generalized_empirical_formula',"
                            "'chemrof:charge')",
                            (cid,),
                        )
                    )
                    assert vals["chemrof:generalized_empirical_formula"] == c["formula"][0]
                    assert int(vals["chemrof:charge"]) == int(c["charge"][0])
                    sign = -1 if role == "substrates" else 1
                    for atom, number in re.findall(r"([A-Z][a-z]?)(\d*)", c["formula"][0]):
                        balance[atom] += sign * coefficient * int(number or 1)
                    charge += sign * coefficient * int(c["charge"][0])
                    s, o, p = (
                        (cid, rid, "consumes") if role == "substrates" else (rid, cid, "produces")
                    )
                    matches = [
                        e
                        for e in r["mechanistic_edges"]
                        if (e["subject"], e["predicate"], e["object"]) == (s, p, o)
                    ]
                    assert len(matches) == 1
                    ev = matches[0]["evidence"][0]
                    assert side in ev["source_locator"] and part in ev["source_locator"]
                    assert f"rh:{pred}" in ev["source_locator"]
                    assert f"coefficient {coefficient}" in ev["source_assertion"]
                    sides[role].append([cid, coefficient])
                    side_count += 1
    assert not any(balance.values()) and charge == 0, rid
    replay.append(
        {"reaction": rid, "master": master, "sides": sides, "atom_charge_balance": "pass"}
    )
assert side_count == 15
# The additional spontaneous isomerization conserves exact formula and charge.
vals = []
for cid in ["CHEBI:57693", "CHEBI:85971"]:
    vals.append(
        dict(
            chebi.execute(
                "select predicate,value from statements where subject=? "
                "and predicate in ('chemrof:generalized_empirical_formula',"
                "'chemrof:charge')",
                (cid,),
            )
        )
    )
assert vals[0] == vals[1]
assert len([e for e in r["mechanistic_edges"] if e["predicate"] in {"consumes", "produces"}]) == 17
assert not any(
    e["subject"] == "CHEBI:85971" and e["object"] == "RHEA:14054" for e in r["mechanistic_edges"]
)

for c, m, u in [
    ("CPLX0-1262", "G7662-MONOMER", "P45395"),
    ("CPLX0-3929", "EG10973-MONOMER", "P17115"),
    ("KDO-8PSYNTH-CPLX", "KDO-8PSYNTH-MONOMER", "P0A715"),
]:
    f = frame(c, "Protein")
    assert f.find("component/Protein").get("frameid") == m
    assert f.findtext("component/coefficient") == "4"
    assert f.find("species/Organism").get("frameid") == "TAX-511145"
    assert xref(frame(m, "Protein"), "UNIPROT", u)
for acc, master in [
    ("P45395", "23104"),
    ("P17115", "23104"),
    ("P0A715", "14053"),
    ("P0ABZ4", "11500"),
    ("P04951", "23448"),
]:
    u = json.loads((RAW / f"uniprot-{acc}.json").read_text())
    assert u["organism"]["taxonId"] == 83333 and u["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    assert (
        next(n for n in r["participants"] if n["id"] == "UniProtKB:" + acc)["label"]
        == u["proteinDescription"]["recommendedName"]["fullName"]["value"]
    )
    assert {"database": "Rhea", "id": "RHEA:" + master} in u["comments"][1]["reaction"][
        "reactionCrossReferences"
    ]
assert "Homotrimer" in json.dumps(
    json.loads((RAW / "uniprot-P0A715.json").read_text())["comments"][4]
)
kdsC = json.loads((RAW / "uniprot-P0ABZ4.json").read_text())
assert all("ECO:0000250" in json.dumps(kdsC["comments"][i]) for i in [1, 2, 5])
assert frame("CPLXCQ7-1", "Protein").find("species/Organism").get("frameid") == "TAX-469008"
assert not any(n["id"] == "MetaCyc:CPLXCQ7-1" for n in r["participants"])
assert xref(frame("CPM-KDOSYNTH-MONOMER", "Protein"), "UNIPROT", "P04951")

# Safeguards for the independently read scientific limits.
# Abstract-only sources are not claimed to be full-text sources.
p2009 = (RAW / "PMC2790981.html").read_text()
assert "β-pyranose" in p2009 and "two dimers" in p2009 and "could not be reliably detected" in p2009
p1985 = json.loads((RAW / "pmid-2997221.json").read_text())["resultList"]["result"][0][
    "abstractText"
]
assert "beta" in p1985.lower() and "preferred" in p1985.lower()
p1992 = json.loads((RAW / "pmid-1521535.json").read_text())["resultList"]["result"][0][
    "abstractText"
]
assert "acyclic" in p1992.lower()
assert "beta-pyranose" in r["description"] and "unresolved" in r["description"].lower()
for e in r["mechanistic_edges"]:
    if "RHEA:23449" in [e["subject"], e["object"]]:
        assert (
            "database convention" in e.get("description", "")
            and "experimental alpha" in e["description"]
        )
    for evidence in e["evidence"]:
        assert evidence["source_locator"] and len(evidence["source_assertion"]) <= 400

kgx_dir = RAW / "kgx-author-replay"
npath, epath = write_kgx([validated], kgx_dir)
edges = list(csv.DictReader(epath.open(), delimiter="\t"))
assert len(edges) == len(r["mechanistic_edges"])
for edge in r["mechanistic_edges"]:
    out = next(e for e in edges if "_" + edge["id"] + "_" in e["id"])
    assert json.loads(out["evidence"]) == edge["evidence"]
    assert out["description"] == edge.get("description", "")
nrows = list(csv.DictReader(npath.open(), delimiter="\t"))
assert (
    next(n for n in nrows if n["id"] == "MetaCyc:RXN-16804")["category"]
    == "biolink:BiochemicalReaction"
)
result = {
    "status": "pass",
    "exit_code": 0,
    "completed_at": datetime.now(UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": sha(TARGET),
    "command": ".venv/bin/python research/pathway_additions/2026-10-11-next-184/kdo-replay.py",
    "scope": "Author raw-source replay; independent review and full gates delegated to root.",
    "rhea_sha256": sha(AUTH / "rhea.rdf.gz"),
    "native_sha256": sha(RAW / "PWY-1269.xml"),
    "counts": {
        "participants": len(r["participants"]),
        "reactions": len(r["reactions"]),
        "edges": len(edges),
        "evidence": sum(len(e["evidence"]) for e in r["mechanistic_edges"]),
        "references": len(r["references"]),
        "kgx_nodes": len(nrows),
        "chemical_sides": 17,
    },
    "checks": [
        "native and closed schema",
        "all reference and artifact body hashes",
        "GO exact native identity and ChEBI labels",
        "all five native reaction members and layouts",
        "15 full-RDF coefficient sides and four atom/charge balances",
        "native spontaneous equilibrium and fifth atom/charge balance",
        "native tetramer/component/UniProt crosswalks",
        "current reviewed protein names and taxa",
        "KdsC by-similarity evidence and BL21 exclusion",
        "KdsA assembly conflict retained",
        "KdsB primary beta versus formal alpha conflict on every affected edge",
        "actual KGX evidence/description preservation and spontaneous reaction category",
    ],
    "reaction_replay": replay,
    "replay_script_sha256": sha(Path(__file__)),
}
(OUT / "kdo-validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
