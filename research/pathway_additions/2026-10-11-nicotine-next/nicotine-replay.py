"""Replay retained nicotine native sources, chemistry and exact sequence bridges.

Run from the repository root with the environment's Python. All raw inputs are
external retained original bodies; no network or shared-file writes are made.
The only output is an external replay-result.json. Large files are streamed.
"""

import collections
import csv
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as E
from functools import cache
from pathlib import Path

import yaml

from pathwaymech.kgx import write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

P = Path("/private/tmp/pathwaymech-nicotine-next-evidence/nicotine")
C = Path("/private/tmp/pathwaymech-curation-authorities")
PRIOR = Path("/private/tmp/pathwaymech-next-pathways-evidence/nicotine")
ROOT = Path.cwd()
D = ROOT / "research/pathway_additions/2026-10-11-nicotine-next"
TARGET = ROOT / "data/pathways/nicotine-degradation-ii.yaml"
STARTED = datetime.datetime.now(datetime.UTC).isoformat()


@cache
def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def native(i, tag):
    path = P / ("metacyc-" + i + ".xml")
    if not path.exists():
        path = PRIOR / ("metacyc-" + i + ".xml")
    if i == "PWY-6993":
        path = PRIOR / "PWY-6993.xml"
    root = E.parse(path).getroot()
    assert root.get("ptools-version") == "22.5"
    assert root.find("metadata/PGDB").get("orgid") == "META"
    frame = root.find(tag)
    assert frame.get("frameid") == i
    return frame


record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert not strict_errors([TARGET], ROOT)
projection = json.loads((D / "nicotine-source-projection.json").read_text())
manifest = json.loads((D / "nicotine-source-manifest.json").read_text())
for item in manifest["sources"]:
    assert sha(item["path"]) == item["sha256"], item["path"]
    assert all(
        k.lower()
        in {"content-type", "x-uniprot-release", "x-uniprot-release-date", "last-modified", "etag"}
        for k in item.get("headers", {})
    )
source_hashes = {x["sha256"] for x in manifest["sources"]}
for ref in record["references"]:
    assert ref["source_sha256"] in source_hashes, ref["id"]

masters = {"73655", "75415", "75351", "34215", "33927", "13213", "27522", "30843", "27385", "13169"}
rows = {
    r["RHEA_ID_MASTER"]: r
    for r in csv.DictReader((C / "rhea-directions.tsv").open(), delimiter="\t")
    if r["RHEA_ID_MASTER"] in masters
}
nums = {v for r in rows.values() for v in r.values()}
subjects = {}
comps = {}
rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
B = "http://rdf.rhea-db.org/"
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
        dest = subjects if chosen else comps if n.startswith("Compound_") else None
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
        for fields in subjects.values()
        for vals in fields.values()
        for v in vals
        if v in comps and v not in subjects
    }
    if not needed:
        break
    subjects.update({i: comps[i] for i in needed})
sides = []
for m, r in rows.items():
    rid = r["RHEA_ID_LR"]
    for side in ["substrates", "products"]:
        sn = subjects[B + rid][side][0]
        for co, ps in subjects[sn].items():
            if not re.fullmatch(r"contains\d+", co):
                continue
            for pt in ps:
                cu = subjects[pt]["compound"][0]
                cp = subjects[cu]
                c = cp["accession"][0].replace("GENERIC:", "RHEA-COMP:")
                sides.append(
                    dict(
                        master=m,
                        reaction="RHEA:" + rid,
                        side=side,
                        coefficient=int(co[8:]),
                        chemical=c,
                        side_uri=sn,
                        participant_uri=pt,
                        compound_uri=cu,
                    )
                )
chem = {}
conn = sqlite3.connect("file:" + str(C / "chebi.db") + "?mode=ro", uri=True)
for curie in sorted(
    {s["chemical"] for s in sides}
    | {"CHEBI:57692", "CHEBI:29033", "CHEBI:15339", "CHEBI:17499", "CHEBI:71308", "CHEBI:30413"}
):
    if curie.startswith("CHEBI:"):
        fields = {}
        for pred, val, obj in conn.execute(
            "select predicate,value,object from statements where subject=?", (curie,)
        ):
            if pred in [
                "rdfs:label",
                "chemrof:charge",
                "chemrof:generalized_empirical_formula",
                "owl:deprecated",
            ]:
                fields.setdefault(pred, []).append(val if val is not None else obj)
        chem[curie] = fields
    else:
        chem[curie] = subjects[B + "Compound_" + curie.split(":")[1]]
balances = []
for m, r in rows.items():
    atoms = collections.Counter()
    charge = 0
    for s in [s for s in sides if s["master"] == m]:
        node = subjects[s["compound_uri"]]
        if "reactivePart" in node:
            node = subjects[node["reactivePart"][0]]
        form = node["formula"][0]
        sgn = -1 if s["side"] == "substrates" else 1
        coeff = sgn * s["coefficient"]
        parts = re.findall(r"([A-Z][a-z]?)(\d*)", form)
        assert "".join(a + b for a, b in parts) == form, form
        for a, b in parts:
            atoms[a] += coeff * int(b or 1)
        charge += coeff * int(node["charge"][0])
    assert all(v == 0 for v in atoms.values()) and charge == 0, (m, atoms, charge)
    balances.append(
        dict(
            reaction="RHEA:" + r["RHEA_ID_LR"],
            atom_or_R_group_delta=dict(atoms),
            charge_delta=charge,
            scope=(
                "Rhea exact small molecules plus reactive-part formulas "
                "for whole protein carriers; "
                "fixed carrier backbones cancel, not isolated-fragment graph nodes."
            ),
        )
    )
replayed = dict(directions=rows, nodes=subjects, sides=sides, identities=chem, balances=balances)

assert replayed == projection["rhea"], "Raw Rhea or ChEBI projection differs"
assert len(sides) == 50 and len(balances) == 10
edges = record["mechanistic_edges"]
participants = {x["id"]: x for x in record["participants"]}
reactions = {x["id"]: x for x in record["reactions"]}
triples = {(e["subject"], e["predicate"], e["object"]): e for e in edges}
assert len(triples) == len(edges)
# Family claims are checked on their actual master subject, not inferred from
# a directed equation alone. Every chemical edge preserves the native locator.
expected_chemical = set()
for master, row in rows.items():
    rid = "RHEA:" + row["RHEA_ID_LR"]
    assert B + row["RHEA_ID_LR"] in subjects[B + master]["directionalReaction"]
    assert B + row["RHEA_ID_BI"] in subjects[B + master]["bidirectionalReaction"]
    assert reactions[rid]["direction"] == "left_to_right"
    assert reactions[rid]["label"] == subjects[B + row["RHEA_ID_LR"]]["equation"][0]
    for edge in edges:
        for evidence in edge["evidence"]:
            if evidence["reference_id"] == rid and "master" in evidence.get("source_assertion", ""):
                assert master in evidence["source_locator"]
                assert "directionalReaction" in evidence["source_locator"]
for s in sides:
    cid = "CHEBI:190393" if s["chemical"] == "CHEBI:193521" else s["chemical"]
    triple = (
        (cid, "consumes", s["reaction"])
        if s["side"] == "substrates"
        else (s["reaction"], "produces", cid)
    )
    expected_chemical.add(triple)
    edge = triples[triple]
    ev = next(e for e in edge["evidence"] if e["reference_id"] == s["reaction"])
    for literal in [
        s["side_uri"],
        s["participant_uri"],
        s["compound_uri"],
        "contains" + str(s["coefficient"]),
    ]:
        assert literal in ev["source_locator"], (edge["id"], literal)
# Explicit ChEBI issuing-authority replacement with identical charged formula.
replacement = list(
    conn.execute("select predicate,value,object from statements where subject=?", ("CHEBI:193521",))
)
assert ("IAO:0100001", None, "CHEBI:190393") in replacement
active = dict(
    (p, v if v is not None else o)
    for p, v, o in conn.execute(
        "select predicate,value,object from statements where subject=?", ("CHEBI:190393",)
    )
)
assert active["chemrof:generalized_empirical_formula"] == "C10H13N2"
assert active["chemrof:charge"] == "1"
assert active["oio:hasAlternativeId"] == "CHEBI:193521"
assert "CHEBI:193521" not in participants and "CHEBI:190393" in participants
assert not record.get("source_mappings")
assert projection["chemical_replacement"]["source_id"] == "CHEBI:193521"
assert projection["chemical_replacement"]["target_id"] == "CHEBI:190393"
# All selected ChEBI labels and small-molecule formulas must be authoritative.
for cid, p in participants.items():
    if not cid.startswith("CHEBI:"):
        continue
    q = dict(
        (k, v if v is not None else o)
        for k, v, o in conn.execute(
            "select predicate,value,object from statements where subject=?", (cid,)
        )
    )
    assert p["label"] == q["rdfs:label"]
    for s in sides:
        if s["chemical"] != cid:
            continue
        raw = subjects[s["compound_uri"]]
        assert raw["formula"][0] == q["chemrof:generalized_empirical_formula"]
        assert int(raw["charge"][0]) == int(q["chemrof:charge"])
# Full native boundary, including both unresolved-catalyst terminal steps.
pathway = native("PWY-6993", "Pathway")
boundary = dict(projection["complete_native_boundary"])
assert set(boundary) == {x.get("frameid") for x in pathway.findall("reaction-list/Reaction")}
assert len(boundary) == len(reactions) == 11
assert set(boundary.values()) == set(reactions)
assert {(r, "part_of", record["id"]) for r in reactions} <= set(triples)
assert {
    e["subject"] for e in edges if e["predicate"] == "part_of" and e["object"] == record["id"]
} == set(reactions)
spm = native("RXN-13082", "Reaction")
spm_ids = {
    "CPD-14094": "CHEBI:66942",
    "WATER": "CHEBI:15377",
    "Acceptor": "CHEBI:15339",
    "CPD-14096": "CHEBI:66893",
    "Donor-H2": "CHEBI:17499",
}
spm_sides = []
for side, tag in [("substrates", "left"), ("products", "right")]:
    for term in spm.findall(tag):
        raw = term.find("Compound").get("frameid")
        cid = spm_ids[raw]
        coefficient = int(term.findtext("coefficient", "1"))
        assert coefficient == 1
        spm_sides.append(
            dict(
                reaction="MetaCyc:RXN-13082",
                side=side,
                chemical=cid,
                coefficient=coefficient,
                native=raw,
            )
        )
        triple = (
            (cid, "consumes", "MetaCyc:RXN-13082")
            if side == "substrates"
            else ("MetaCyc:RXN-13082", "produces", cid)
        )
        expected_chemical.add(triple)
        assert triple in triples
        if raw != "WATER":
            frame = native(raw, "Compound")
            assert any(
                x.findtext("dblink-db") == "CHEBI" and "CHEBI:" + x.findtext("dblink-oid") == cid
                for x in frame.findall("dblink")
            )
assert spm_sides == projection["spm_native_sides"]
assert expected_chemical == {t for t in triples if t[1] in {"consumes", "produces"}}
# Generic A/AH2 formal balance: not a resolved physiological carrier identity.
symbolic = collections.Counter()
for form, co in [("C9H8NO3", -1), ("H2O", -1), ("A", -1), ("C9H8NO4", 1), ("AH2", 1)]:
    for element, n in re.findall(r"([A-Z][a-z]?)([0-9]*)", form):
        symbolic[element] += co * int(n or 1)
assert all(n == 0 for n in symbolic.values())
assert "CHEBI:71308" not in participants
cofactor = native("CPD0-1882", "Compound")
assert cofactor.findtext("inchi").split("/")[1] == "C19H26N8O13P2S2.Mo.2O"
assert "/p-4/" in cofactor.findtext("inchi")
assert cofactor.find("cml/molecule").get("formalCharge") == "-2"
# Source order is independently replayed on the exact native ordering frames.
native_order = {
    (x.find("predecessor-reactions/Reaction").get("frameid"), x.find("Reaction").get("frameid"))
    for x in pathway.findall("reaction-ordering")
    if x.find("predecessor-reactions/Reaction") is not None
}
orders = {(boundary[a], "provides_input_for", boundary[b]) for a, b in native_order}
assert orders == {t for t in triples if t[1] == "provides_input_for"}, native_order
assert len(orders) == 10
# Issue343 regression: native order alone is not a ChEBI identity bridge.
for key in orders:
    edge = triples[key]
    first = edge["evidence"][0]
    assert first["reference_id"] == "MetaCyc:PWY-6993"
    assert "CHEBI:" not in first["source_assertion"]
    common = {t[2] for t in triples if t[0] == key[0] and t[1] == "produces"} & {
        t[0] for t in triples if t[2] == key[2] and t[1] == "consumes"
    }
    common -= {"CHEBI:15377", "CHEBI:15378", "CHEBI:57945", "CHEBI:57783"}
    assert len(common) == 1
    cid = common.pop()
    assert cid in edge["description"]
    for evidence in (
        triples[(key[0], "produces", cid)]["evidence"]
        + triples[(cid, "consumes", key[2])]["evidence"]
    ):
        assert evidence in edge["evidence"]
    if cid == "CHEBI:190393":
        assert any(v["reference_id"] == cid for v in edge["evidence"])
assert (
    native("CPLX-8439", "Protein")
    .find("catalyzes/Enzymatic-Reaction/reaction/Reaction")
    .get("frameid")
    == "RXN-13081"
)
assert (
    "catalyzes/Enzymatic-Reaction"
    in triples[("MetaCyc:CPLX-8439", "catalyzes", "RHEA:33928")]["evidence"][0]["source_locator"]
)
# Exact primary-deposit/protein identities, active statuses and canonical names.
proteins = {}
for accession, declared in projection["proteins"].items():
    protein = json.loads((P / ("uniprot-" + accession + ".json")).read_text())
    assert protein["primaryAccession"] == accession
    assert "Inactive" not in protein["entryType"]
    assert {k: v for k, v in protein.items() if k in declared} == declared
    desc = protein["proteinDescription"]
    name = desc.get("recommendedName", desc.get("submissionNames", [{}])[0])["fullName"]["value"]
    assert participants["UniProtKB:" + accession]["label"] == name
    proteins[accession] = protein
for accession in ["F8G0N8", "F8G0N9", "F8G0P0"]:
    assert (
        "Inactive" in json.loads((P / ("uniprot-" + accession + ".json")).read_text())["entryType"]
    )
    assert "UniProtKB:" + accession not in participants
cyc = json.loads((P / "rcsb-7TLX-entity1.json").read_text())
sequence = proteins["A0A0E3ELC2"]["sequence"]["value"]
assert sequence == "".join((P / "WP_080563818.1.fasta").read_text().splitlines()[1:])
assert len(sequence) == 132 and sequence[27:] == cyc["entity_poly"]["pdbx_seq_one_letter_code_can"]
assert cyc["entity_src_gen"][0]["pdbx_gene_src_ncbi_taxonomy_id"] == "1042876"
assert proteins["A0A0E3ELC2"]["organism"]["taxonId"] == 303
assert any(
    x["reference_database_accession"] == "A0A0E3ELC2"
    and x["aligned_regions"] == [{"entity_beg_seq_id": 1, "ref_beg_seq_id": 28, "length": 105}]
    for x in cyc["rcsb_polymer_entity_align"]
)
features = re.split(r"\nFT   (?=[A-Za-z])", (P / "GQ857548.embl").read_text())
for bridge in projection["nic2_sequence_bridges"]:
    section = next(
        s
        for s in features
        if s.startswith("CDS") and '/protein_id="' + bridge["protein"] + '"' in s
    )
    translation = re.search(r'/translation="([^"]+)"', section)[1]
    translation = re.sub(r"\s", "", re.sub(r"\nFT\s+", "", translation))
    assert translation == proteins[bridge["uniprot"]]["sequence"]["value"]
# Assembly identities come from exact S16 native components, not same-name
# proteins from HZN6/N-9; functional edges do not assert isolated monomers.
for complex_id, components in {
    "CPLX-8439": {"MONOMER-17159": 2},
    "CPLX-8990": {"MONOMER-19246": 2},
    "CPLX-8991": {"MONOMER-19251": 1, "MONOMER-19252": 1, "MONOMER-19253": 1},
}.items():
    frame = native(complex_id, "Protein")
    assert {
        x.find("Protein").get("frameid"): int(x.findtext("coefficient", "1"))
        for x in frame.findall("component")
    } == components
    assert any(x.findtext("strain-name") == "S16" for x in frame.findall("species/Organism"))
for monomer, accession in [("MONOMER-17159", "F8G0M4"), ("MONOMER-19246", "F8G0M3")]:
    frame = native(monomer, "Protein")
    assert any(
        x.findtext("dblink-db") == "UNIPROT" and x.findtext("dblink-oid") == accession
        for x in frame.findall("dblink")
    )
assert any(
    x.findtext("common-name") == "Pseudomonas sp. HZN6"
    for x in native("CPLX-8441", "Protein").findall("species/Organism")
)
for rid in ["RHEA:34216", "RHEA:13214", "RHEA:75416"]:
    assert not any(e["object"] == rid and e["predicate"] in {"catalyzes", "enables"} for e in edges)
assert "category" not in reactions["RHEA:75416"]
for rid in ["RHEA:73656", "RHEA:75352"]:
    for role, carrier in [("substrates", "RHEA-COMP:14399"), ("products", "RHEA-COMP:10350")]:
        assert (
            next(
                s["coefficient"]
                for s in sides
                if s["reaction"] == rid and s["side"] == role and s["chemical"] == carrier
            )
            == 2
        )
    assert not any(
        s["chemical"] in {"CHEBI:15379", "CHEBI:16240"} for s in sides if s["reaction"] == rid
    )
    assert (rid, "has_input", "UniProtKB:A0A0E3ELC2") in triples
assert {t[0] for t in triples if t[1] == "located_in"} == {
    "UniProtKB:F8G0P2",
    "UniProtKB:F8G0P1",
    "UniProtKB:A0A0E3ELC2",
}
assert all(
    "p0015" in e["evidence"][0]["source_locator"] for e in edges if e["predicate"] == "located_in"
)
# Actual exporter preserves every edge and each structured evidence item.
output = P / "kgx"
write_kgx([validated], output)
exported = list(csv.DictReader((output / "edges.tsv").open(), delimiter="\t"))
assert len(exported) == len(edges)
export_predicates = {
    "BFO:0000050": "part_of",
    "RO:0002413": "provides_input_for",
    "RO:0002233": "has_input",
    "RO:0001025": "located_in",
}
for row in exported:
    predicate = export_predicates.get(
        row["predicate"], row["predicate"].removeprefix("pathwaymech:")
    )
    key = (row["subject"], predicate, row["object"])
    assert json.loads(row["evidence"]) == triples[key]["evidence"]
    assert row["description"] == triples[key].get("description", "")
exported_nodes = {n["id"]: n for n in csv.DictReader((output / "nodes.tsv").open(), delimiter="\t")}
assert exported_nodes["RHEA:75416"]["category"] == "biolink:BiochemicalReaction"
assert "MolecularActivity" not in exported_nodes["RHEA:75416"]["category"]
result = {
    "started_at": STARTED,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "status": "passed",
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": sha(TARGET),
    "source_count": len(manifest["sources"]),
    "all_source_hashes_match": True,
    "participants": len(participants),
    "reactions": len(reactions),
    "edges": len(edges),
    "evidence": sum(len(e["evidence"]) for e in edges),
    "rhea_families": len(rows),
    "raw_rhea_sides": len(sides),
    "native_spm_sides": len(spm_sides),
    "chemical_edges": len(expected_chemical),
    "exact_balance_count": len(balances),
    "generic_spm_balance": "formal paired A/AH2 only; carrier identity unresolved",
    "native_order_edges": len(orders),
    "cycN_sequence_bridge": "RefSeq full132aa identical; S16 PDB7TLX mature105aa = UniProt28-132",
    "nic2_deposit_sequence_matches": len(projection["nic2_sequence_bridges"]),
    "schema": "native and closed LinkML passed",
    "kgx_edges": len(exported),
    "kgx_hashes": {f.name: sha(f) for f in output.glob("*.tsv")},
    "source_projection_sha256": sha(D / "nicotine-source-projection.json"),
    "source_manifest_sha256": sha(D / "nicotine-source-manifest.json"),
}
(P / "replay-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
