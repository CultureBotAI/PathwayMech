"""Replay retained PWY-5875 draft; structural parity is not scientific approval."""

import argparse
import collections
import csv
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
from pathlib import Path

import yaml
from lxml import etree as ET

from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, kgx_edges, kgx_nodes, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-201-evidence/staphyloxanthin")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-201"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--target",
    type=Path,
    default=DOSSIER / "withheld/staphyloxanthin-biosynthesis.yaml",
    help="Explicit retained research draft; no maintained pathway is presumed.",
)
parser.add_argument(
    "--output",
    type=Path,
    default=RAW / "withheld-author-replay.json",
    help="New replay receipt; the historical author validation is preserved.",
)
args = parser.parse_args()
TARGET = args.target.resolve()
if args.output.resolve() == (DOSSIER / "staphyloxanthin-validation.json").resolve():
    parser.error("Historical validation receipt must remain unchanged")
START = datetime.datetime.now(datetime.UTC).isoformat()
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def native(identifier):
    x = ET.parse(str(RAW / (identifier + ".xml"))).getroot()[1]
    assert x.get("frameid") == identifier
    return x


def ontology(db, identifier):
    with sqlite3.connect(f"file:{CACHE}/{db}.db?mode=ro", uri=True) as connection:
        rows = connection.execute(
            "select predicate,value,object from statements where subject=?", (identifier,)
        ).fetchall()
    return {p: v if v is not None else o for p, v, o in rows}


def atoms(formula):
    parts = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
    assert "".join(a + n for a, n in parts) == formula
    return {a: int(n or 1) for a, n in parts}


record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert strict_errors([TARGET], ROOT) == []
manifest = json.loads((DOSSIER / "staphyloxanthin-source-manifest.json").read_text())
projection = json.loads((DOSSIER / "staphyloxanthin-source-projection.json").read_text())
proteins = json.loads((DOSSIER / "staphyloxanthin-protein-projection.json").read_text())
assert digest(TARGET) == manifest["target_sha256"] == projection["target_sha256"]
assert proteins["target_sha256"] == digest(TARGET)
source_checks = {}
for source in manifest["sources"] + manifest["unavailable_or_rejected_attempts"]:
    if "raw_path" in source:
        assert digest(source["raw_path"]) == source["sha256"]
        source_checks[source["raw_path"]] = source["sha256"]
for source in manifest["shared_full_authorities"]:
    assert digest(source["file"]) == source["sha256"]
reference_checks = {}
web_only = []
for reference in record["references"]:
    if "source_sha256" in reference:
        path = manifest["reference_artifacts"][reference["id"]]
        assert digest(path) == reference["source_sha256"]
        reference_checks[reference["id"]] = reference["source_sha256"]
    else:
        assert reference["id"] == "DOI:10.31635/ccschem.020.202000219"
        assert "web retrieval" in reference["source_version"]
        web_only.append(reference["id"])
# Independently parse selected family triples from the full upstream RDF again.
masters = set(projection["directions"])
directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    values = line.split("\t")
    if values[0] in masters:
        directions[values[0]] = dict(
            zip(["master", "left_to_right", "right_to_left", "bidirectional"], values, strict=True)
        )
assert directions == projection["directions"]
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
                value = child.get(RDF + "resource") or (child.text or "").strip()
                if value not in dest.setdefault(uri, {}).setdefault(key, []):
                    dest[uri][key].append(value)
        x.clear()
        while x.getprevious() is not None:
            del x.getparent()[0]
needed = {v for d in nodes.values() for vs in d.values() for v in vs if v in compounds}
nodes.update({u: compounds[u] for u in needed})
assert nodes == projection["nodes"]
assert record["id"] == "MetaCyc:PWY-5875"
assert record["label"] == native("PWY-5875").findtext("common-name")
assert set(native("PWY-5875").xpath("reaction-list/Reaction/@frameid")) == {
    s["native"] for s in projection["steps"]
}
assert len(record["reactions"]) == len(projection["steps"]) == 9
edges = record["mechanistic_edges"]
chemical_edges = set()
balances, source_sides, generic_formula_notation = {}, [], []
for step in projection["steps"]:
    rid, mid = step["reaction"], step["native"]
    reaction = next(r for r in record["reactions"] if r["id"] == rid)
    assert reaction["direction"] == "left_to_right"
    assert native("PWY-5875").xpath(
        f'reaction-layout[Reaction/@frameid="{mid}"]/direction/text()'
    ) == ["L2R"]
    membership = next(e for e in edges if e["subject"] == rid and e["predicate"] == "part_of")
    assert membership["object"] == record["id"]
    if not rid.startswith("RHEA:"):
        continue
    number = rid.split(":")[1]
    master = next(m for m, d in directions.items() if d["left_to_right"] == number)
    assert RH + number in nodes[RH + master]["directionalReaction"]
    assert reaction["label"] == nodes[RH + number]["equation"][0]
    assert any(
        v["reference_id"] == rid
        and "rh:directionalReaction" in v["source_locator"]
        and RH + master in v["source_locator"]
        for v in membership["evidence"]
    )
    native_xrefs = native(mid).xpath('dblink[dblink-db="RHEA"]/dblink-oid/text()')
    if native_xrefs:
        assert all(x in directions[master].values() for x in native_xrefs)
    balance = collections.Counter()
    for side in [s for s in projection["sides"] if s["reaction"] == number]:
        compound = nodes[side["compound"]]
        cid, coefficient = compound["accession"][0], side["coefficient"]
        assert cid == side["chemical"]
        chebi = ontology("chebi", cid)
        current_formula = chebi["chemrof:generalized_empirical_formula"]
        source_formula = compound["formula"][0]
        if cid in ["CHEBI:17499", "CHEBI:13193"]:
            assert (source_formula, current_formula) == {
                "CHEBI:17499": ("H2R", "H2A"),
                "CHEBI:13193": ("R", "A"),
            }[cid]
            generic_formula_notation.append(
                {
                    "id": cid,
                    "rhea_formula": source_formula,
                    "chebi_formula": current_formula,
                    "scope": (
                        "Different placeholder symbols for the same source-issued generic class; "
                        "not empirical atoms."
                    ),
                }
            )
        else:
            assert current_formula == source_formula
        assert chebi["chemrof:charge"] == compound["charge"][0]
        assert chebi.get("owl:deprecated") not in ["true", True]
        sign = -1 if side["role"] == "substrates" else 1
        triple = (cid, "consumes", rid) if sign == -1 else (rid, "produces", cid)
        chemical_edges.add(triple)
        edge = next(e for e in edges if (e["subject"], e["predicate"], e["object"]) == triple)
        assert any(
            v["reference_id"] == rid
            and side["side"] in v["source_locator"]
            and side["participant"] in v["source_locator"]
            and side["compound"] in v["source_locator"]
            and f"coefficient {coefficient}" in v["source_assertion"]
            for v in edge["evidence"]
        )
        for atom, amount in atoms(compound["formula"][0]).items():
            balance[atom] += sign * coefficient * amount
        balance["charge"] += sign * coefficient * int(compound["charge"][0])
        source_sides.append(side)
    assert all(n == 0 for n in balance.values()), (rid, balance)
    balances[rid] = {
        "residuals": dict(balance),
        "scope": "formal generic R-symbol balance; ChEBI uses A; physiological donor unidentified"
        if number == "56105"
        else "exact formula and charge balance",
    }
# Exact native terminal source sides and chemical identity bridges.
mapping = {
    "CPD-9913": "CHEBI:79064",
    "NDP-glucoses": "MetaCyc:NDP-glucoses",
    "CPD-9915": "CHEBI:80353",
    "Nucleoside-Diphosphates": "MetaCyc:Nucleoside-Diphosphates",
    "CPD-20650": "MetaCyc:CPD-20650",
    "CPD-9916": "CHEBI:71690",
    "CO-A": "CHEBI:57287",
}
bridges = []
for mid in ["RXN-9308", "RXN-9309"]:
    rid = "MetaCyc:" + mid
    assert native(mid).findtext("reaction-direction") == "PHYSIOL-LEFT-TO-RIGHT"
    for role in ["left", "right"]:
        for x in native(mid).findall(role):
            nid = x.find("Compound").get("frameid")
            cid = mapping[nid]
            assert x.findtext("coefficient", "1") == "1"
            triple = (cid, "consumes", rid) if role == "left" else (rid, "produces", cid)
            chemical_edges.add(triple)
            assert any((e["subject"], e["predicate"], e["object"]) == triple for e in edges)
            if cid.startswith("CHEBI:"):
                assert cid.split(":")[1] in native(nid).xpath(
                    'dblink[dblink-db="CHEBI"]/dblink-oid/text()'
                )
                chebi = ontology("chebi", cid)
                assert native(nid).findtext("inchi") == chebi["chemrof:inchi_string"]
                bridges.append({"native": nid, "chebi": cid, "exact_inchi_match": True})
# Issue 368: generic class locators must resolve to fields present in the original XML.
class_locator_checks = []
for edge_id, native_id in [
    ("stx-edge-050", "NDP-glucoses"),
    ("stx-edge-052", "Nucleoside-Diphosphates"),
]:
    obj = native(native_id)
    evidence = next(e for e in edges if e["id"] == edge_id)["evidence"][1]
    assert evidence["reference_id"] == "MetaCyc:" + native_id
    assert evidence["source_locator"] == "Compound/common-name; dblink; cml/molecule"
    assert obj.find("inchi") is None
    for field in ["common-name", "dblink", "cml/molecule"]:
        assert obj.find(field) is not None
    class_locator_checks.append({"edge": edge_id, "native": native_id, "status": "passed"})

# Native final acyl-CoA formula matches exact ChEBI-form product/CoA accounting.
acyl = native("CPD-20650").find("cml/molecule")
parts = acyl.find("formula").get("concise").split()
acyl_atoms = {parts[i]: int(parts[i + 1]) for i in range(0, len(parts), 2)}
balance = collections.Counter()
for cid, sign in [("CHEBI:80353", -1), ("CHEBI:71690", 1), ("CHEBI:57287", 1)]:
    c = ontology("chebi", cid)
    for a, n in atoms(c["chemrof:generalized_empirical_formula"]).items():
        balance[a] += sign * n
    balance["charge"] += sign * int(c["chemrof:charge"])
for a, n in acyl_atoms.items():
    balance[a] -= n
balance["charge"] -= int(acyl.get("formalCharge"))
assert all(v == 0 for v in balance.values()), balance
native_acyl_projection = {
    "residuals": dict(balance),
    "scope": (
        "Formal native proposed-donor formula projection only; no experimental acyl-CoA "
        "identity, physiological microstate or donor-specific assay validation."
    ),
}
# Class formulas are absent, so do not assert an empirical atom balance for CrtQ.
for cid in ["NDP-glucoses", "Nucleoside-Diphosphates"]:
    assert native(cid).find("cml/molecule/formula").get("concise") == ""
assert int(native("NDP-glucoses").find("cml/molecule").get("formalCharge")) == -2
assert int(native("Nucleoside-Diphosphates").find("cml/molecule").get("formalCharge")) == -3
assert int(ontology("chebi", "CHEBI:79064")["chemrof:charge"]) == -1
assert int(ontology("chebi", "CHEBI:80353")["chemrof:charge"]) == 0
assert -1 + -2 == 0 + -3
observed_chemical = {
    (e["subject"], e["predicate"], e["object"])
    for e in edges
    if e["predicate"] in ["consumes", "produces"]
}
assert observed_chemical == chemical_edges
for u, projected in proteins["proteins"].items():
    original = json.loads((RAW / f"uniprot-{u}.json").read_text())
    assert projected == {k: original.get(k) for k in projected}
    assert original["primaryAccession"] == u and "reviewed" in original["entryType"]
    assert original["organism"]["taxonId"] == 426430
    assert (
        next(n for n in record["participants"] if n["id"] == "UniProtKB:" + u)["label"]
        == (original["proteinDescription"]["recommendedName"]["fullName"]["value"])
    )
assert native("MONOMER-17444").findtext("species/Organism/strain-name") == "KCTC 1928"
assert native("MONOMER-17444").xpath('dblink[dblink-db="UNIPROT"]/dblink-relationship/text()') == [
    "Ortholog"
]
assert json.loads((RAW / "uniprot-A0A0H3KDU5.json").read_text())["entryType"] == "Inactive"
assert "UniProtKB:A0A0H3KDU5" not in {n["id"] for n in record["participants"]}
ald = next(
    e for e in edges if e["subject"] == "MetaCyc:MONOMER-17444" and e["predicate"] == "enables"
)
assert any(
    v["reference_id"] in web_only and "C244S" in v["source_assertion"] for v in ald["evidence"]
)
# Guard against attribution regression: native predecessor and Rhea chemistry are separate sources.
links = [e for e in edges if e["predicate"] == "provides_input_for"]
assert len(links) == 8
for link in links:
    assert link["evidence"][0]["reference_id"] == record["id"]
    assert len(link["evidence"]) == 3
    assert "CHEBI:" not in link["evidence"][0]["source_assertion"]
# Actual exported bytes retain all local edges and their full source metadata.
output_dir = RAW / "author-kgx"
node_path, edge_path = write_kgx([validated], output_dir)
knodes = kgx_nodes([validated])
kedges = kgx_edges([validated])
with edge_path.open() as stream:
    rows = list(csv.DictReader(stream, delimiter="\t"))
assert len(rows) == len(kedges) == len(edges) == 70
for edge, row, obj in zip(edges, rows, kedges, strict=True):
    assert row["subject"] == edge["subject"] == obj.subject
    assert row["object"] == edge["object"] == obj.object
    assert row["predicate"] == LOCAL_PREDICATE_CURIES[edge["predicate"]]
    assert json.loads(row["evidence"]) == edge["evidence"]
assert sum(len(json.loads(row["evidence"])) for row in rows) == 123
categories = {n.id: n.category for n in knodes}
for cid in [
    "CHEBI:13193",
    "CHEBI:17499",
    "MetaCyc:NDP-glucoses",
    "MetaCyc:Nucleoside-Diphosphates",
]:
    assert categories[cid] == "biolink:ChemicalEntity"
assert categories["MetaCyc:MONOMER-17444"] == "biolink:Protein"
assert all(categories[r["id"]] == "biolink:MolecularActivity" for r in record["reactions"])
# Exact structures conflict despite formula balance: expose this known blocker.
pspp_native = native("CPD-465").findtext("inchi")
pspp_current = ontology("chebi", "CHEBI:57310")["chemrof:inchi_string"]
ps7 = json.loads((RAW / "pspp/rcsb-PS7.json").read_text())
pspp_ligand = ps7["rcsb_chem_comp_descriptor"]["InChI"]
assert pspp_native != pspp_current
assert pspp_current.replace("/p-3", "") != pspp_ligand
result = {
    "status": "structural_replay_passed_scientific_grounding_blocked",
    "publication_eligible": False,
    "open_scientific_issue": "https://github.com/CultureBotAI/PathwayMech/issues/369",
    "pspp_identity_conflict": {
        "native_inchi": pspp_native,
        "current_chebi_inchi": pspp_current,
        "rcsb_ps7_inchi": pspp_ligand,
        "scope": "Formula and graph parity do not resolve the distinct stereochemical structures. "
        "PS7 was prepared using human squalene synthase and soaked into CrtM; "
        "this is not a direct absolute-stereochemistry assay of Newman-produced PSPP.",
    },
    "started_at": START,
    "completed_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "helper_sha256": digest(__file__),
    "source_bodies_rehashed": len(source_checks),
    "reference_bodies_rehashed": len(reference_checks),
    "web_only_primary_not_replayed": web_only,
    "source_hashes": source_checks,
    "native_reactions": 9,
    "rhea_source_side_checks": len(source_sides),
    "native_chemical_side_checks": 8,
    "atom_charge_balances": balances,
    "generic_formula_notation": generic_formula_notation,
    "native_acyl_formula_projection": native_acyl_projection,
    "crtQ_class_limit": (
        "Native blank formulas; exact class charge and source side parity only, "
        "no empirical atom balance claimed."
    ),
    "native_chemical_inchi_bridges": bridges,
    "generic_class_locator_checks": class_locator_checks,
    "protein_entries_checked": 5,
    "aldH_scope": "Native KCTC1928; deleted ortholog excluded; 2020 C244S assembly qualified.",
    "kgx": {
        "nodes": len(knodes),
        "edges": len(rows),
        "evidence": 123,
        "nodes_sha256": digest(node_path),
        "edges_sha256": digest(edge_path),
    },
    "checks": [
        "native schema",
        "closed LinkML schema",
        "original source hashes",
        "Rhea family/side replay",
        "selected authority side/formula parity; PSPP exact identity remains blocked",
        "native full9-step coverage",
        "protein scope",
        "actual KGX bytes",
    ],
    "shared_full_corpus_gates": (
        "Not a maintained record; root checks final corpus exclusion separately."
    ),
}
args.output.write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {k: v for k, v in result.items() if k not in ["source_hashes", "atom_charge_balances"]},
        indent=2,
    )
)
