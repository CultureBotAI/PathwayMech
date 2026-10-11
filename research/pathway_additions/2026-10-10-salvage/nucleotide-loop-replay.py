import collections
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as E
from pathlib import Path

OUT = Path("/private/tmp/pathwaymech-salvage-evidence/nucleotide-loop")
OLD = Path("/private/tmp/pathwaymech-next-evidence/cobalamin")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
R = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RH = "http://rdf.rhea-db.org/"


def digest(p):
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def project(e):
    d = {}
    for c in e:
        d.setdefault(c.tag.rsplit("}", 1)[-1], []).append(
            c.attrib.get(R + "resource") or (c.text or "").strip()
        )
    return d


directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    vals = line.split("\t")
    if vals[0] in ["11196", "23560", "30367"]:
        directions[vals[0]] = dict(
            zip(["master", "left_to_right", "right_to_left", "bidirectional"], vals, strict=True)
        )
nums = {v for d in directions.values() for v in d.values()}
subjects = {}
compounds = {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as f:
    ctx = E.iterparse(f, events=("start", "end"))
    _, root = next(ctx)
    for ev, e in ctx:
        if ev == "end" and e.tag == R + "Description":
            uri = e.attrib.get(R + "about", "")
            name = uri.rsplit("/", 1)[-1]
            target = (
                subjects
                if (
                    name.split("_", 1)[0] in nums
                    or name.startswith("Participant_")
                    and name.split("_")[1] in nums
                )
                else compounds
                if name.startswith("Compound_")
                else None
            )
            if target is not None:
                for k, vs in project(e).items():
                    for v in vs:
                        if v not in target.setdefault(uri, {}).setdefault(k, []):
                            target[uri][k].append(v)
            e.clear()
            root.clear()
needed = {v for s in subjects.values() for vs in s.values() for v in vs if v in compounds}
for u in needed:
    subjects[u] = compounds[u]
assert (
    digest(CACHE / "rhea.rdf.gz")
    == "8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf"
)
prior = json.loads((OLD / "rhea-projection.json").read_text())["subjects"]
assert all(prior[u]["fields"] == n for u, n in subjects.items())
chemids = {"CHEBI:18420"}
sides = []
for master, d in directions.items():
    rid = d["left_to_right"]
    n = subjects[RH + rid]
    assert n["substrates"] == [RH + master + "_L"] and n["products"] == [RH + master + "_R"]
    for field in ["substrates", "products"]:
        side = n[field][0]
        for k, ps in subjects[side].items():
            if not re.fullmatch("contains[0-9]+", k):
                continue
            for p in ps:
                compound = subjects[p]["compound"][0]
                cid = "CHEBI:" + subjects[compound]["chebi"][0].rsplit("_", 1)[1]
                chemids.add(cid)
                sides.append(
                    {
                        "reaction": "RHEA:" + rid,
                        "master": "RHEA:" + master,
                        "side": field,
                        "side_uri": side,
                        "coefficient": int(k[8:]),
                        "participant_uri": p,
                        "compound_uri": compound,
                        "chemical": cid,
                    }
                )
chem = {}
db = sqlite3.connect("file:" + str(CACHE / "chebi.db") + "?mode=ro", uri=True)
for cid in sorted(chemids):
    rows = db.execute(
        "select predicate,value,object from statements where subject=?", (cid,)
    ).fetchall()
    fields = {}
    for k, v, _o in rows:
        if v is not None:
            fields.setdefault(k, []).append(v)
    chem[cid] = {
        k: fields[k]
        for k in ["rdfs:label", "chemrof:generalized_empirical_formula", "chemrof:charge"]
    }
    if "IAO:0000115" in fields:
        chem[cid]["IAO:0000115"] = fields["IAO:0000115"]
    assert fields.get("owl:deprecated") != ["true"]
balances = []
for d in directions.values():
    rid = "RHEA:" + d["left_to_right"]
    counts = collections.Counter()
    charge = 0
    for row in sides:
        if row["reaction"] != rid:
            continue
        sign = -1 if row["side"] == "substrates" else 1
        coeff = row["coefficient"] * sign
        formula = chem[row["chemical"]]["chemrof:generalized_empirical_formula"][0]
        assert "".join(a + b for a, b in re.findall(r"([A-Z][a-z]?)([0-9]*)", formula)) == formula
        for a, b in re.findall(r"([A-Z][a-z]?)([0-9]*)", formula):
            counts[a] += coeff * int(b or 1)
        charge += coeff * int(chem[row["chemical"]]["chemrof:charge"][0])
    assert all(v == 0 for v in counts.values()) and charge == 0, (rid, counts, charge)
    balances.append(
        {"reaction": rid, "element_delta": dict(counts), "charge_delta": charge, "passed": True}
    )
ontology = {}
for dbname, cids in [("go", ["GO:0005886"]), ("ncbitaxon", ["NCBITaxon:83333"])]:
    conn = sqlite3.connect("file:" + str(CACHE / (dbname + ".db")) + "?mode=ro", uri=True)
    for cid in cids:
        ontology[cid] = conn.execute(
            "select value from statements where subject=? and predicate='rdfs:label'", (cid,)
        ).fetchall()[0][0]
native = {}
for f in [
    "metacyc-PWY-5509.xml",
    "metacyc-DMBPPRIBOSYLTRANS-RXN.xml",
    "metacyc-COBALAMIN5PSYN-RXN.xml",
    "metacyc-RXN-8770.xml",
    "metacyc-RIBAZOLEPHOSPHAT-MONOMER.xml",
    "metacyc-COBS-MONOMER.xml",
]:
    root = E.parse(OLD / f).getroot()
    node = list(root)[1]
    fields = {}
    for key in [
        "common-name",
        "reaction-list",
        "reaction-ordering",
        "reaction-layout",
        "reaction-direction",
        "left",
        "right",
        "dblink",
        "comment",
        "catalyzes",
        "species",
        "component",
        "location",
    ]:
        fields[key] = [E.tostring(e, encoding="unicode") for e in node.findall(key)]
    native[f] = {
        "sha256": digest(OLD / f),
        "ptools_version": root.attrib.get("ptools-version"),
        "object": node.attrib,
        "fields": fields,
    }
bp = E.parse(OLD / "PW001884.owl").getroot()
bnodes = {
    e.attrib.get(R + "about", e.attrib.get(R + "ID")): {
        "type": e.tag.rsplit("}", 1)[-1],
        "fields": project(e),
    }
    for e in bp
}
selected = {}
pending = ["ProteinComplex/3870", "ReactionCatalysis/5115", "Reactions/5142"]
while pending:
    k = pending.pop()
    if k in selected:
        continue
    selected[k] = bnodes[k]
    pending.extend(
        v[1:]
        for vs in bnodes[k]["fields"].values()
        for v in vs
        if v.startswith("#") and v[1:] in bnodes
    )
assert selected["ProteinReference/6552"]["fields"]["xref"] == ["#Reference/UniProt_P36562"]
assert selected["Reference/UniProt_P36562"]["fields"]["id"] == ["P36562"]
assert selected["Protein/6552/Stoichiometry/2.0"]["fields"]["stoichiometricCoefficient"] == ["2.0"]
result = {
    "checked_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "rhea": {
        "source_path": str(CACHE / "rhea.rdf.gz"),
        "sha256": digest(CACHE / "rhea.rdf.gz"),
        "release": "142",
        "directions_sha256": digest(CACHE / "rhea-directions.tsv"),
        "directions": directions,
        "nodes": subjects,
        "prior_projection_exact_match": True,
        "sides": sides,
        "balances": balances,
    },
    "chebi": chem,
    "ontology": ontology,
    "metacyc": native,
    "pathbank": {
        "path": str(OLD / "PW001884.owl"),
        "sha256": digest(OLD / "PW001884.owl"),
        "selected_nodes": selected,
    },
}
(OUT / "source-replay.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {
            "directions": directions,
            "sides": sides,
            "balances": balances,
            "chemicals": chem,
            "ontology": ontology,
        },
        indent=2,
    )
)
