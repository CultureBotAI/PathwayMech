"""Replay the entire ten-step PWY-5838 record against original native sources."""

import collections
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
import zipfile
from pathlib import Path

import yaml
from lxml import etree as ET

from pathwaymech.kgx import kgx_edges, kgx_nodes, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-195-evidence/menaquinol")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-195"
TARGET = ROOT / "data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
START = datetime.datetime.now(datetime.UTC).isoformat()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def native(identifier):
    x = ET.parse(str(RAW / f"metacyc-{identifier}.xml")).getroot()[1]
    assert x.get("frameid") == identifier
    return x


def atoms(formula):
    parts = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
    assert "".join(a + n for a, n in parts) == formula
    return {a: int(n or 1) for a, n in parts}


def ontology(db, identifier):
    with sqlite3.connect(f"file:{CACHE}/{db}.db?mode=ro", uri=True) as c:
        rows = c.execute(
            "select predicate,value,object from statements where subject=?", (identifier,)
        ).fetchall()
    return {p: v if v is not None else o for p, v, o in rows}


record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert strict_errors([TARGET], ROOT) == []
manifest = json.loads((DOSSIER / "menaquinol-source-manifest.json").read_text())
projection = json.loads((DOSSIER / "menaquinol-source-projection.json").read_text())
protein_projection = json.loads((DOSSIER / "menaquinol-protein-projection.json").read_text())
assert digest(TARGET) == manifest["target_sha256"] == projection["target_sha256"]
assert protein_projection["target_sha256"] == digest(TARGET)
source_hashes = {}
for s in manifest["sources"]:
    assert digest(s["raw_path"]) == s["sha256"], s["raw_path"]
    source_hashes[s["raw_path"]] = s["sha256"]
for s in manifest["shared_full_authorities"]:
    assert digest(s["file"]) == s["sha256"], s["file"]
    source_hashes[s["file"]] = s["sha256"]
for r in record["references"]:
    assert digest(manifest["reference_artifacts"][r["id"]]) == r["source_sha256"]
archive = manifest["archive"]
assert digest(archive["file"]) == archive["sha256"]
with zipfile.ZipFile(archive["file"]) as z:
    names = [
        n for n in z.namelist() if n.endswith("/" + archive["member"]) or n == archive["member"]
    ]
    assert len(names) == 1
    member = z.read(names[0])
assert hashlib.sha256(member).hexdigest() == archive["member_sha256"]
assert member == (RAW / "PW001897.owl").read_bytes()
# Re-read every selected Rhea family and participant from the complete upstream RDF.
masters = set(projection["rhea"]["directions"])
directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    values = line.split("\t")
    if values[0] in masters:
        directions[values[0]] = dict(
            zip(["master", "left_to_right", "right_to_left", "bidirectional"], values, strict=True)
        )
assert directions == projection["rhea"]["directions"]
numbers = {v for d in directions.values() for v in d.values()}
nodes, compounds = {}, {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
    for _, x in ET.iterparse(stream, events=("end",), tag=RDF + "Description"):
        uri = x.get(RDF + "about", "")
        name = uri.rsplit("/", 1)[-1]
        selected = name.split("_", 1)[0] in numbers or (
            name.startswith("Participant_") and name.split("_")[1] in numbers
        )
        dest = nodes if selected else compounds if name.startswith("Compound_") else None
        if dest is not None:
            for child in x:
                key = ET.QName(child).localname
                val = child.get(RDF + "resource") or (child.text or "").strip()
                if val not in dest.setdefault(uri, {}).setdefault(key, []):
                    dest[uri][key].append(val)
        x.clear()
        while x.getprevious() is not None:
            del x.getparent()[0]
needed = {v for d in nodes.values() for vs in d.values() for v in vs if v in compounds}
nodes.update({u: compounds[u] for u in needed})
assert nodes == projection["rhea"]["nodes"]
steps = projection["selected_steps"]
assert len(steps) == 10
assert record["id"] == "MetaCyc:PWY-5838"
assert record["label"] == native("PWY-5838").findtext("common-name")
assert set(native("PWY-5838").xpath("reaction-list/Pathway/@frameid")) == {
    "PWY-5837",
    "PWY-5783",
    "PWY-5852",
    "MENAQUINONESYN-PWY",
}
assert len(native("MENAQUINONESYN-PWY").findall("reaction-list/Reaction")) == 1
for sub in projection["full_native_hierarchy"]["PWY-5838"]:
    assert set(native(sub).xpath("reaction-list/Reaction/@frameid")) == {
        s[1] for s in steps if s[2] == sub
    }
# Exact source sides, coefficients, directions, formulas and atom/charge balances.
edges = record["mechanistic_edges"]
expected, side_checks, balances = set(), [], []
net = collections.Counter()
for rid, metacyc, sub, up, cplx, monomer in steps:
    master = next(m for m, d in directions.items() if d["left_to_right"] == rid)
    r = next(x for x in record["reactions"] if x["id"] == "RHEA:" + rid)
    assert r["direction"] == "left_to_right"
    assert r["label"] == nodes[RH + rid]["equation"][0]
    assert RH + rid in nodes[RH + master]["directionalReaction"]
    assert native(sub).xpath(
        f'reaction-layout[Reaction/@frameid="{metacyc}"]/direction/text()'
    ) == ["L2R"]
    xrefs = native(metacyc).xpath('dblink[dblink-db="RHEA"]/dblink-oid/text()')
    assert len(xrefs) == 1 and xrefs[0] in directions[master].values()
    membership = next(e for e in edges if e["subject"] == r["id"] and e["predicate"] == "part_of")
    assert membership["object"] == record["id"]
    assert any(
        v["reference_id"] == r["id"]
        and RH + master in v["source_locator"]
        and "rh:directionalReaction" in v["source_locator"]
        for v in membership["evidence"]
    )
    balance = collections.Counter()
    for role in ["substrates", "products"]:
        side = nodes[RH + rid][role][0]
        for pred, participants in nodes[side].items():
            if not re.fullmatch(r"contains\d+", pred):
                continue
            coefficient = int(pred[8:])
            for participant in participants:
                compound_uri = nodes[participant]["compound"][0]
                compound = nodes[compound_uri]
                cid = compound["accession"][0]
                assert cid.startswith("CHEBI:")
                chebi = ontology("chebi", cid)
                assert chebi["chemrof:generalized_empirical_formula"] == compound["formula"][0]
                assert chebi["chemrof:charge"] == compound["charge"][0]
                assert chebi.get("owl:deprecated") not in ["true", True]
                sign = -1 if role == "substrates" else 1
                triple = (cid, "consumes", r["id"]) if sign == -1 else (r["id"], "produces", cid)
                expected.add(triple)
                edge = next(
                    e for e in edges if (e["subject"], e["predicate"], e["object"]) == triple
                )
                assert any(
                    v["reference_id"] == r["id"]
                    and side in v["source_locator"]
                    and participant in v["source_locator"]
                    and compound_uri in v["source_locator"]
                    and f"coefficient {coefficient}" in v["source_assertion"]
                    for v in edge["evidence"]
                )
                for atom, count in atoms(compound["formula"][0]).items():
                    balance[atom] += sign * coefficient * count
                balance["charge"] += sign * coefficient * int(compound["charge"][0])
                net[cid] += sign * coefficient
                side_checks.append(
                    {"reaction": rid, "role": role, "chemical": cid, "coefficient": coefficient}
                )
    assert all(v == 0 for v in balance.values()), (rid, balance)
    balances.append({"reaction": rid, "atom_charge_residuals": dict(balance), "status": "passed"})
    u = json.loads((RAW / f"uniprot-{up}.json").read_text())
    assert u["organism"]["taxonId"] == 83333 and "reviewed" in u["entryType"]
    assert protein_projection["proteins"][up] == {
        k: u.get(k) for k in protein_projection["proteins"][up]
    }
    assert native(monomer).xpath('dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [up]
    catalyst = cplx or ("MENE-CPLX" if up == "P37353" else monomer)
    assert metacyc in native(catalyst).xpath(
        "catalyzes/Enzymatic-Reaction/reaction/Reaction/@frameid"
    )
    if cplx:
        assert native(cplx).xpath("component/Protein/@frameid") == [monomer]
        count = int(native(cplx).findtext("component/coefficient"))
        assert count == {"P38051": 2, "P17109": 2, "P0ABU0": 6, "P77781": 4, "P0AD57": 2}[up]
        assert any(
            e["subject"] == "UniProtKB:" + up
            and e["predicate"] == "part_of"
            and e["object"] == "MetaCyc:" + cplx
            for e in edges
        )
assert expected == {
    (e["subject"], e["predicate"], e["object"])
    for e in edges
    if e["predicate"] in ["consumes", "produces"]
}
assert net["CHEBI:128769"] == -5 and net["CHEBI:175763"] == -1
assert net["CHEBI:61684"] == 1 and net["CHEBI:29748"] == -1
assert net["CHEBI:33019"] == 7
for cid in [
    "CHEBI:29780",
    "CHEBI:58818",
    "CHEBI:58689",
    "CHEBI:18325",
    "CHEBI:57364",
    "CHEBI:58897",
    "CHEBI:11173",
    "CHEBI:57711",
    "CHEBI:61873",
    "CHEBI:57287",
]:
    assert net[cid] == 0, cid
assert RH + "26478" in nodes[RH + "30099"]["subClassOf"]
assert RH + "42640" in nodes[RH + "30063"]["subClassOf"]
# No unqualified MenE oligomer or old EntC/hydrogenase catalyst enters this record.
ids = {n["id"] for n in record["participants"]}
assert not ids & {"MetaCyc:MENE-CPLX", "UniProtKB:P0AEJ2", "UniProtKB:P69739", "UniProtKB:P0ACD8"}
assert any(e["subject"] == "UniProtKB:P37353" and e["predicate"] == "enables" for e in edges)
for pdb in ["6NJ0", "5C5H"]:
    d = json.loads((RAW / f"rcsb-{pdb}-assembly-1.json").read_text())
    assert d["pdbx_struct_assembly"]["oligomeric_count"] == 1
    assert any(r["id"] == "DOI:10.2210/pdb" + pdb + "/pdb" for r in record["references"])
assert len(projection["pathbank_reaction_dispositions"]) == 11
objects = {o["id"]: o for o in projection["pathbank_original"]["objects"]}
assert {o["id"] for o in objects.values() if o["kind"] == "BiochemicalReaction"} == {
    x["native_object"] for x in projection["pathbank_reaction_dispositions"]
}
assert not any(x["tag"] == "conversionDirection" for x in objects["Reactions/179427"]["fields"])
assert (
    next(
        x
        for x in projection["pathbank_reaction_dispositions"]
        if x["native_object"] == "Reactions/179427"
    )["selected_reaction"]
    is None
)
# Connectivity evidence must cite both actual reaction sides, not just native ordering.
for e in edges:
    if e["predicate"] != "provides_input_for":
        continue
    assert {e["subject"], e["object"]} <= {v["reference_id"] for v in e["evidence"]}
    assert any("rh:products" in v["source_locator"] for v in e["evidence"])
    assert any("rh:substrates" in v["source_locator"] for v in e["evidence"])
# Review #357: all eight corrected locators must address existing native source anchors.
fix = json.loads((DOSSIER / "menaquinol-provenance-fix.json").read_text())
assert fix["final_target_sha256"] == digest(TARGET)
for change in fix["changes"]:
    assert digest(change["raw_path"]) == change["raw_sha256"]
    path = Path(change["raw_path"])
    tree = ET.parse(str(path)) if path.suffix == ".xml" else ET.HTML(path.read_bytes())
    edge = next(e for e in edges if e["id"] == change["edge_id"])
    evidence = next(v for v in edge["evidence"] if v["reference_id"] == change["reference_id"])
    assert evidence["source_assertion"] == change["source_assertion"]
    assert evidence["source_locator"] == change["verified_replacement_locator"]
    for anchor_check in change["native_anchor_checks"]:
        attribute, value = anchor_check["attribute"], anchor_check["value"]
        elements = tree.xpath(f'//*[@{attribute}="{value}"]')
        assert elements
        if anchor_check["expected_text"]:
            text = " ".join(" ".join(elements[0].itertext()).split())
            assert anchor_check["expected_text"].casefold() in text.casefold()
# Actual exporter writes files; verify all evidence and contexts survive.
out = RAW / "kgx"
write_kgx([validated], out)
exported = kgx_edges([validated])
assert len(exported) == len(edges) == 85
for e, k in zip(edges, exported, strict=True):
    assert json.loads(k.evidence) == e["evidence"]
assert len(kgx_nodes([validated])) == 56
report = {
    "status": "passed",
    "started_at": START,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "command": (
        "UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 "
        ".venv/bin/python research/pathway_additions/2026-10-11-next-195/menaquinol-replay.py"
    ),
    "scope": "Author replay, not independent scientific review; full corpus gates belong to root.",
    "source_hashes": source_hashes,
    "native_boundary_complete": True,
    "chemical_sides": side_checks,
    "balances": balances,
    "net": {k: v for k, v in net.items() if v},
    "counts": {"participants": 44, "reactions": 10, "edges": 85, "evidence": 179, "nodes": 56},
    "kgx": {p.name: digest(p) for p in out.glob("*.tsv")},
    "helper_sha256": digest(__file__),
}
(DOSSIER / "menaquinol-validation.json").write_text(json.dumps(report, indent=2) + "\n")
print(
    json.dumps({"status": "passed", "counts": report["counts"], "chemical_sides": len(side_checks)})
)
