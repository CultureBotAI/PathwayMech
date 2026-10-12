"""Replay the complete two-reaction P121-PWY record against retained originals."""

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

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-192-evidence/adenine-salvage-i")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-192"
TARGET = ROOT / "data/pathways/adenine-and-adenosine-salvage-i.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
SELECTED = {
    "27642": ("27643", "left_to_right", "ADENPHOSPHOR-RXN", "L2R"),
    "16609": ("16611", "right_to_left", "ADENPRIBOSYLTRAN-RXN", "R2L"),
}
START = datetime.datetime.now(datetime.UTC).isoformat()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def native(identifier):
    return next(
        x for x in ET.parse(RAW / (identifier + ".xml")).getroot() if x.get("frameid") == identifier
    )


def ont(db, identifier):
    with sqlite3.connect(f"file:{CACHE}/{db}.db?mode=ro", uri=True) as c:
        rows = c.execute(
            "select predicate,value,object from statements where subject=?", (identifier,)
        ).fetchall()
    return {
        p: v if v is not None else o
        for p, v, o in rows
        if p
        in {
            "rdfs:label",
            "chemrof:charge",
            "chemrof:generalized_empirical_formula",
            "owl:deprecated",
            "IAO:0000115",
        }
    }


def atoms(formula):
    fields = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
    assert "".join(a + n for a, n in fields) == formula
    return {a: int(n or 1) for a, n in fields}


record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert strict_errors([TARGET], ROOT) == []
assert record["id"] == "MetaCyc:P121-PWY"
assert (
    len(record["participants"]),
    len(record["reactions"]),
    len(record["mechanistic_edges"]),
) == (14, 2, 20)
assert sum(len(x["evidence"]) for x in record["mechanistic_edges"]) == 39
manifest = json.loads((DOSSIER / "adenine-salvage-i-source-manifest.json").read_text())
projection = json.loads((DOSSIER / "adenine-salvage-i-source-projection.json").read_text())
assert manifest["target_sha256"] == projection["target_sha256"] == digest(TARGET)
source_hashes = {}
for s in manifest["sources"] + manifest["shared_full_authorities"]:
    assert digest(s["file"]) == s["sha256"], s["file"]
    source_hashes[s["file"]] = s["sha256"]
for ref in record["references"]:
    assert digest(manifest["reference_artifacts"][ref["id"]]) == ref["source_sha256"]
for id, saved in projection["native_metacyc"].items():
    x = native(id)
    assert saved["frameid"] == x.get("frameid")
    assert saved["common_name"] == x.findtext("common-name")
    assert saved["reaction_list"] == [r.get("frameid") for r in x.findall("reaction-list/Reaction")]
    for key, fields in saved["retained_native_fields"].items():
        assert fields == [ET.tostring(y, encoding="unicode") for y in x.findall(key)]
for id, saved in projection["proteins"].items():
    d = json.loads((RAW / ("uniprot-" + id + ".json")).read_text())
    assert saved == {k: d.get(k) for k in saved}
    assert d["organism"]["taxonId"] == 83333
    assert (
        next(n for n in record["participants"] if n["id"] == "UniProtKB:" + id)["label"]
        == d["proteinDescription"]["recommendedName"]["fullName"]["value"]
    )
# Rebuild relevant RDF triples from the full upstream release, not the saved projection.
directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    fields = line.split("\t")
    if fields[0] in SELECTED:
        directions[fields[0]] = dict(
            zip(["master", "left_to_right", "right_to_left", "bidirectional"], fields, strict=True)
        )
numbers = {v for d in directions.values() for v in d.values()}
nodes, compounds = {}, {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
    context = ET.iterparse(stream, events=("start", "end"))
    _, root = next(context)
    for event, x in context:
        if event != "end" or x.tag != RDF + "Description":
            continue
        uri = x.get(RDF + "about", "")
        name = uri.rsplit("/", 1)[-1]
        chosen = name.split("_", 1)[0] in numbers or (
            name.startswith("Participant_") and name.split("_")[1] in numbers
        )
        dest = nodes if chosen else compounds if name.startswith("Compound_") else None
        if dest is not None:
            for child in x:
                k = child.tag.rsplit("}", 1)[-1]
                v = child.get(RDF + "resource") or (child.text or "").strip()
                if v not in dest.setdefault(uri, {}).setdefault(k, []):
                    dest[uri][k].append(v)
        x.clear()
        root.clear()
needed = {v for x in nodes.values() for vs in x.values() for v in vs if v in compounds}
nodes.update({u: compounds[u] for u in needed})
assert nodes == projection["rhea"]["nodes"]
assert directions == projection["rhea"]["directions"]
edges = record["mechanistic_edges"]
expected = set()
sides, balances, net = [], [], collections.Counter()
for master, (rid, direction, meta, _layout) in SELECTED.items():
    reaction = next(r for r in record["reactions"] if r["id"] == "RHEA:" + rid)
    assert reaction["direction"] == direction
    assert reaction["label"] == nodes[RH + rid]["equation"][0]
    assert directions[master][direction] == rid
    assert RH + rid in nodes[RH + master]["directionalReaction"]
    native_xref = [
        x.findtext("dblink-oid")
        for x in native(meta).findall("dblink")
        if x.findtext("dblink-db") == "RHEA"
    ]
    assert len(native_xref) == 1 and native_xref[0] in directions[master].values()
    member = next(e for e in edges if e["subject"] == "RHEA:" + rid and e["predicate"] == "part_of")
    assert member["object"] == record["id"]
    assert any(
        ev["reference_id"] == "RHEA:" + rid
        and f"rh:{master} rh:directionalReaction rh:{rid}" in ev["source_locator"]
        for ev in member["evidence"]
    )
    balance = collections.Counter()
    for role in ["substrates", "products"]:
        side = nodes[RH + rid][role][0]
        for key, participants in nodes[side].items():
            if not re.fullmatch(r"contains\d+", key):
                continue
            coefficient = int(key[8:])
            for participant in participants:
                compound = nodes[nodes[participant]["compound"][0]]
                cid = compound["accession"][0]
                current = ont("chebi", cid)
                assert {k: current[k] for k in projection["rhea"]["chebi"][cid]} == projection[
                    "rhea"
                ]["chebi"][cid]
                assert current["chemrof:generalized_empirical_formula"] == compound["formula"][0]
                assert current["chemrof:charge"] == compound["charge"][0]
                sign = -1 if role == "substrates" else 1
                triple = (
                    (cid, "consumes", "RHEA:" + rid)
                    if sign == -1
                    else ("RHEA:" + rid, "produces", cid)
                )
                expected.add(triple)
                edge = next(
                    e for e in edges if (e["subject"], e["predicate"], e["object"]) == triple
                )
                assert any(
                    ev["reference_id"] == "RHEA:" + rid
                    and side in ev["source_locator"]
                    and participant in ev["source_locator"]
                    and f"coefficient {coefficient}" in ev["source_assertion"]
                    for ev in edge["evidence"]
                )
                for atom, count in atoms(compound["formula"][0]).items():
                    balance[atom] += sign * coefficient * count
                balance["charge"] += sign * coefficient * int(compound["charge"][0])
                net[cid] += sign * coefficient
                sides.append(
                    {"reaction": rid, "role": role, "chemical": cid, "coefficient": coefficient}
                )
    assert all(v == 0 for v in balance.values()), balance
    balances.append({"reaction": rid, "atom_charge_residuals": dict(balance), "status": "passed"})
assert {
    (e["subject"], e["predicate"], e["object"])
    for e in edges
    if e["predicate"] in {"consumes", "produces"}
} == expected
assert len(sides) == 8
assert {k: v for k, v in net.items() if v} == {
    "CHEBI:16335": -1,
    "CHEBI:43474": -1,
    "CHEBI:57720": 1,
    "CHEBI:58017": -1,
    "CHEBI:456215": 1,
    "CHEBI:33019": 1,
}
pwy = native("P121-PWY")
assert pwy.findtext("common-name") == record["label"]
assert set(x.get("frameid") for x in pwy.findall("reaction-list/Reaction")) == {
    v[2] for v in SELECTED.values()
}
assert {
    x.find("Reaction").get("frameid"): x.findtext("direction")
    for x in pwy.findall("reaction-layout")
} == {v[2]: v[3] for v in SELECTED.values()}
assert [
    (x.find("predecessor-reactions/Reaction").get("frameid"), x.find("Reaction").get("frameid"))
    for x in pwy.findall("reaction-ordering")
] == [("ADENPHOSPHOR-RXN", "ADENPRIBOSYLTRAN-RXN")]
assert "TAX-511145" not in [x.get("frameid") for x in pwy.findall("species/Organism")]
connect = next(e for e in edges if e["predicate"] == "provides_input_for")
assert (connect["subject"], connect["object"]) == ("RHEA:27643", "RHEA:16611")
assert {"RHEA:27643", "RHEA:16611"} <= {e["reference_id"] for e in connect["evidence"]}
# Verify native complex membership and exact accession bridge; no monomer catalysts.
for complex_id, monomer, accession, count, rxn in [
    ("DEOD-CPLX", "DEOD-MONOMER", "P0ABP8", 6, "ADENPHOSPHOR-RXN"),
    ("ADENPRIBOSYLTRAN-CPLX", "ADENPRIBOSYLTRAN-MONOMER", "P69503", 2, "ADENPRIBOSYLTRAN-RXN"),
]:
    x = native(complex_id)
    assert int(x.find("component").findtext("coefficient")) == count
    assert x.find("component/Protein").get("frameid") == monomer
    assert any(
        d.findtext("dblink-db") == "UNIPROT" and d.findtext("dblink-oid") == accession
        for d in native(monomer).findall("dblink")
    )
    assert rxn in [
        x.get("frameid") for x in x.findall("catalyzes/Enzymatic-Reaction/reaction/Reaction")
    ]
assert all(e["subject"].startswith("MetaCyc:") for e in edges if e["predicate"] == "catalyzes")
apt = native("ADENPRIBOSYLTRAN-ENZRXN")
assert apt.find("cofactor/Compound").get("frameid") == "MG+2"
assert apt.find("alternative-cofactor/alternate/Compound").get("frameid") == "MN+2"
# Independently inspect exact paper passages used, including the assay's construct limit.
primary = ET.parse(RAW / "PMC4125576.xml").getroot()
texts = [x.findtext("text") or "" for x in primary.findall(".//passage")]
assert (
    "1.5 mM PRPP" in texts[45]
    and "10 mM MgCl2" in texts[45]
    and "adenine hydrochloride" in texts[45]
)
assert "BL21(AI)" in texts[29] and "recombinant" in texts[65]
assert "APRT" in texts[148] and "21.2 ± 1.7" in texts[148]
pnp = ET.parse(RAW / "PMC6193948.xml").getroot()
texts = [x.findtext("text") or "" for x in pnp.findall(".//passage")]
assert "adenosine" in texts[22] and "wild-type" in texts[22]
assert "homohexamer" in texts[40]
assert any(
    x["id"] == "365172" and "intracellularly" in x["abstractText"]
    for x in json.loads((RAW / "primary-abstracts.json").read_text())["resultList"]["result"]
)
# Narrow actual exporter: preserve every evidence array and record-local node context.
kgx = RAW / "kgx"
write_kgx([validated], kgx)
exported = kgx_edges([validated])
assert len(exported) == len(edges)
for e, k in zip(edges, exported, strict=True):
    assert json.loads(k.evidence) == e["evidence"]
assert len(kgx_nodes([validated])) == 18
report = {
    "status": "passed",
    "started_at": START,
    "completed_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "helper_sha256": digest(Path(__file__)),
    "source_hashes": source_hashes,
    "native_reactions": 2,
    "participants": 14,
    "edges": 20,
    "evidence": 39,
    "chemical_sides": sides,
    "balances": balances,
    "full_route_net": {k: v for k, v in net.items() if v},
    "checks": [
        "native and closed schema",
        "retained original source hashes",
        "full Rhea RDF replay and direction-family bridges",
        "all 8 stoichiometric chemical sides and 2 atom/charge balances",
        "exact full native boundary and physiological layout",
        "separately cited material-transfer bridge",
        "native complex stoichiometry and exact protein xrefs",
        "native metal alternatives and primary assay limits",
        "actual KGX 20 edges and full evidence parity",
    ],
    "shared_corpus_gates": "Delegated to root; not claimed by this author replay.",
}
(DOSSIER / "adenine-salvage-i-validation.json").write_text(json.dumps(report, indent=2) + "\n")
print(
    json.dumps(
        {
            "status": "passed",
            "target_sha256": report["target_sha256"],
            "edges": 20,
            "evidence": 39,
            "balances": len(balances),
        }
    )
)
