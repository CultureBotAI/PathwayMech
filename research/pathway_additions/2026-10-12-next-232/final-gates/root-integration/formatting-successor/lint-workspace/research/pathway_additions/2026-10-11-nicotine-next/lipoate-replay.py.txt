import collections
import csv
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as E
from pathlib import Path

import yaml
from lxml import etree as L

from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

P = Path("/private/tmp/pathwaymech-nicotine-next-evidence/lipoate")
C = Path("/private/tmp/pathwaymech-curation-authorities")
B = "http://rdf.rhea-db.org/"
rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
masters = {"17665", "16585"}
rows = {
    r["RHEA_ID_MASTER"]: r
    for r in csv.DictReader((C / "rhea-directions.tsv").open(), delimiter="\t")
    if r["RHEA_ID_MASTER"] in masters
}
nums = {v for r in rows.values() for v in r.values()}
nodes = {}
comp = {}
with gzip.open(C / "rhea.rdf.gz", "rb") as f:
    context = E.iterparse(f, events=["start", "end"])
    _, root = next(context)
    for event, e in context:
        if event != "end" or e.tag != rdf + "Description":
            continue
        uri = e.get(rdf + "about", "")
        n = uri.rsplit("/", 1)[-1]
        chosen = n.split("_")[0] in nums or (
            n.startswith("Participant_") and n.split("_")[1] in nums
        )
        dest = nodes if chosen else comp if n.startswith("Compound_") else None
        if dest is not None:
            for ch in e:
                k = ch.tag.rsplit("}", 1)[-1]
                v = ch.get(rdf + "resource") or (ch.text or "").strip()
                if v not in dest.setdefault(uri, {}).setdefault(k, []):
                    dest[uri][k].append(v)
        e.clear()
        root.clear()
while True:
    needed = {
        v
        for fields in nodes.values()
        for vals in fields.values()
        for v in vals
        if v in comp and v not in nodes
    }
    if not needed:
        break
    nodes.update({i: comp[i] for i in needed})
sides = []
balances = []
for m, row in rows.items():
    d = row["RHEA_ID_LR"]
    atoms = collections.Counter()
    charge = 0
    for role in ["substrates", "products"]:
        side = nodes[B + d][role][0]
        for co, pts in nodes[side].items():
            if not re.fullmatch(r"contains\d+", co):
                continue
            for pt in pts:
                cu = nodes[pt]["compound"][0]
                cp = nodes[cu]
                cid = cp["accession"][0].replace("GENERIC:", "RHEA-COMP:")
                n = int(co[8:])
                sgn = -1 if role == "substrates" else 1
                components = (
                    [nodes[u] for u in cp["reactivePart"]] if cp.get("reactivePart") else [cp]
                )
                for bn in components:
                    parts = re.findall(r"([A-Z][a-z]?)(\d*)", bn["formula"][0])
                    assert "".join(a + b for a, b in parts) == bn["formula"][0]
                    for a, b in parts:
                        atoms[a] += sgn * n * int(b or 1)
                    charge += sgn * n * int(bn["charge"][0])
                sides.append(
                    {
                        "master": m,
                        "reaction": "RHEA:" + d,
                        "side": role,
                        "coefficient": n,
                        "chemical": cid,
                        "side_uri": side,
                        "participant_uri": pt,
                        "compound_uri": cu,
                    }
                )
    assert all(v == 0 for v in atoms.values()) and charge == 0, (m, atoms, charge)

    balances.append(
        {"reaction": "RHEA:" + d, "atom_or_R_delta": dict(atoms), "charge_delta": charge}
    )
con = sqlite3.connect("file:" + str(C / "chebi.db") + "?mode=ro", uri=True)
identities = {}
for cid in sorted({s["chemical"] for s in sides} | {"CHEBI:49883"}):
    if cid.startswith("CHEBI:"):
        identities[cid] = {
            p: v if v is not None else o
            for p, v, o in con.execute(
                "select predicate,value,object from statements where subject=? "
                "and predicate in ('rdfs:label','chemrof:generalized_empirical_formula',"
                "'chemrof:charge','owl:deprecated')",
                (cid,),
            )
        }
    else:
        identities[cid] = nodes[B + "Compound_" + cid.split(":")[1]]
x = {
    "directions": rows,
    "nodes": nodes,
    "sides": sides,
    "balances": balances,
    "identities": identities,
}
repo = Path.cwd()
folder = repo / "research/pathway_additions/2026-10-11-nicotine-next"
target = repo / "data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml"
assert x == json.loads((folder / "lipoate-rhea-projection.json").read_text())
r = yaml.safe_load(target.read_text())
validate_record(r)
assert not strict_errors([target], repo)
assert (
    hashlib.sha256((C / "rhea.rdf.gz").read_bytes()).hexdigest()
    == "8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf"
)
man = json.loads((folder / "lipoate-source-manifest.json").read_text())
digests = set()
for row in man:
    body = Path(row["file"]).read_bytes()
    assert len(body) == row["bytes"]
    assert hashlib.sha256(body).hexdigest() == row["sha256"]
    digests.add(row["sha256"])
for ref in r["references"]:
    assert ref["source_sha256"] in digests or ref["id"].startswith("RHEA:")
expected = {
    (s["chemical"], "consumes", s["reaction"])
    if s["side"] == "substrates"
    else (s["reaction"], "produces", s["chemical"])
    for s in sides
}
actual = {
    (e["subject"], e["predicate"], e["object"])
    for e in r["mechanistic_edges"]
    if e["predicate"] in ["consumes", "produces"]
}
assert expected == actual and len(expected) == 17
for s in sides:
    a, b = (
        (s["chemical"], s["reaction"])
        if s["side"] == "substrates"
        else (s["reaction"], s["chemical"])
    )
    edge = next(
        e
        for e in r["mechanistic_edges"]
        if e["subject"] == a and e["object"] == b and e["predicate"] in ["consumes", "produces"]
    )
    item = edge["evidence"][0]
    assert (
        item["reference_id"] == s["reaction"]
        and "coefficient " + str(s["coefficient"]) in item["source_assertion"]
        and s["participant_uri"] in item["source_locator"]
    )
p = L.parse(str(P / "metacyc-PWY0-501.xml"))
assert p.xpath("/ptools-xml/Pathway/reaction-list/Reaction/@frameid") == ["RXN0-947", "RXN0-949"]
assert p.xpath("/ptools-xml/Pathway/reaction-layout/direction/text()") == ["L2R", "L2R"]
assert p.xpath("/ptools-xml/Pathway/reaction-ordering/Reaction/@frameid") == ["RXN0-949"]
assert p.xpath("/ptools-xml/Pathway/reaction-ordering/predecessor-reactions/Reaction/@frameid") == [
    "RXN0-947"
]
for frame, rid in [("RXN0-947", "17666"), ("RXN0-949", "16586")]:
    assert L.parse(str(P / f"metacyc-{frame}.xml")).xpath(
        '/ptools-xml/Reaction/dblink[dblink-db="RHEA"]/dblink-oid/text()'
    ) == [rid]
c = L.parse(str(P / "metacyc-CPLX0-782.xml"))
assert c.xpath("/ptools-xml/Protein/component/Protein/@frameid") == ["EG11306-MONOMER"]
assert c.xpath("/ptools-xml/Protein/component/coefficient/text()") == ["2"]
assert L.parse(str(P / "metacyc-EG11306-MONOMER.xml")).xpath(
    '/ptools-xml/Protein/dblink[dblink-db="UNIPROT"]/dblink-oid/text()'
) == ["P60716"]
for acc in ["P60720", "P60716"]:
    up = json.loads((P / f"uniprot-{acc}.json").read_text())
    assert (
        up["primaryAccession"] == acc
        and up["organism"]["taxonId"] == 83333
        and up["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    )
assert len(nodes[B + "Compound_14568"]["reactivePart"]) == 2
report = {
    "verified_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "status": "pass",
    "record_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    "checks": [
        "native and closed record schemas",
        "all retained source-body digests and record-reference digests",
        "full Rhea RDF re-projection equals retained projection",
        "all 17 chemical-side edges and coefficients",
        "both atom/charge balances, summing all reactivePart nodes",
        "exact two-step native membership, direction and predecessor",
        "directed Rhea cross-references",
        "native LipA dimer composition and UniProt bridge",
        "current reviewed K-12 protein identities",
    ],
    "balances": balances,
    "limits": ("Deterministic author replay, not independent scientific review "
               "or experimental verification of formal redox conventions."),
}
(P / "replay-receipt.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
