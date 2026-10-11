"""Replay original source chemistry/identities and the bounded authored record.

Run from the repository root. This is an author verification, not an independent
scientific review. No network calls or repository-wide generated writes occur.
"""

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

from pathwaymech.kgx import kgx_edges, kgx_nodes
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-189-evidence/phenethylamine-ii")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-189"
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/phenylethylamine-degradation-ii.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            result.update(block)
    return result.hexdigest()


def native(frame, kind):
    return next(
        x
        for x in ET.parse(RAW / f"native-{frame}.xml").iter(kind)
        if x.get("frameid") == frame and x.get("detail") == "full"
    )


initial_hash = digest(TARGET)
record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert not strict_errors([TARGET], ROOT)
manifest = json.loads((DOSSIER / "phenethylamine-ii-source-manifest.json").read_text())
projection = json.loads((DOSSIER / "phenethylamine-ii-source-projection.json").read_text())
assert initial_hash == manifest["record_sha256"]
source_hashes = {}
for source in manifest["sources"]:
    actual_hash = digest(source["path"])
    assert actual_hash == source["sha256"], source["path"]
    source_hashes[source["path"]] = actual_hash
for reference in record["references"]:
    assert (
        source_hashes[manifest["reference_artifacts"][reference["id"]]]
        == reference["source_sha256"]
    )

pathway = native("PWY-6534", "Pathway")
assert {x.get("frameid") for x in pathway.findall("reaction-list/Reaction")} == {
    "RXN-11510",
    "PHENDEHYD-RXN",
}
assert pathway.find("reaction-ordering/Reaction").get("frameid") == "PHENDEHYD-RXN"
assert (
    pathway.find("reaction-ordering/predecessor-reactions/Reaction").get("frameid") == "RXN-11510"
)
for frame, cross in [("RXN-11510", "36724"), ("PHENDEHYD-RXN", "21395")]:
    rxn = native(frame, "Reaction")
    assert any(
        x.findtext("dblink-db") == "RHEA" and x.findtext("dblink-oid") == cross
        for x in rxn.findall("dblink")
    )

# Reconstruct needed nodes independently from the complete official RDF, merging
# duplicate Description subjects and retaining their actual predicates.
needed = {RH + x for x in ["36723", "36724", "36726", "21392", "21393", "21395"]}
for reaction in projection["rhea"]:
    for side in reaction["sides"]:
        needed.update(side[k] for k in ["side_uri", "participant_uri", "compound_uri"])
nodes = {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
    context = ET.iterparse(stream, events=("start", "end"))
    _, root = next(context)
    for event, element in context:
        if event != "end" or element.tag != RDF + "Description":
            continue
        uri = element.get(RDF + "about", "")
        if uri in needed:
            for child in element:
                key = child.tag.rsplit("}", 1)[-1]
                value = child.get(RDF + "resource") or (child.text or "").strip()
                values = nodes.setdefault(uri, {}).setdefault(key, [])
                if value not in values:
                    values.append(value)
        element.clear()
        root.clear()
assert set(nodes) == needed
assert RH + "36724" in nodes[RH + "36723"]["directionalReaction"]
assert RH + "21393" in nodes[RH + "21392"]["directionalReaction"]
assert RH + "21395" in nodes[RH + "21392"]["bidirectionalReaction"]
directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    cells = line.split("\t")
    if cells[0] in {"36723", "21392"}:
        directions[cells[0]] = cells[1:]
assert directions == {"36723": ["36724", "36725", "36726"], "21392": ["21393", "21394", "21395"]}

actual_sides = []
balances = {}
with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as connection:
    for reaction in record["reactions"]:
        node = nodes[RH + reaction["id"].split(":")[1]]
        assert reaction["label"] == node["equation"][0]
        assert reaction["direction"] == "left_to_right"
        balance = collections.Counter()
        charge = 0
        for side, sign, predicate in [("substrates", -1, "consumes"), ("products", 1, "produces")]:
            side_uri = node[side][0]
            for property_name, participants in nodes[side_uri].items():
                if not re.fullmatch(r"contains\d+", property_name):
                    continue
                coefficient = int(property_name[8:])
                for participant in participants:
                    compound_uri = nodes[participant]["compound"][0]
                    compound = nodes[compound_uri]
                    chemical = "CHEBI:" + compound["chebi"][0].rsplit("_", 1)[-1]
                    chem = dict(
                        connection.execute(
                            "select predicate,value from statements where subject=? "
                            "and predicate in "
                            "('rdfs:label','chemrof:charge','chemrof:generalized_empirical_formula')",
                            (chemical,),
                        )
                    )
                    # ChEBI uses dummy A; Rhea uses dummy R for the same generic
                    # donor/acceptor class. This is formal balance, not a named protein.
                    chebi_formula = chem["chemrof:generalized_empirical_formula"]
                    if chemical in {"CHEBI:13193", "CHEBI:17499"}:
                        chebi_formula = chebi_formula.replace("A", "R")
                    assert chebi_formula == compound["formula"][0]
                    assert str(chem["chemrof:charge"]) == compound["charge"][0]
                    terms = re.findall(r"([A-Z][a-z]?)(\d*)", compound["formula"][0])
                    for element, count in terms:
                        balance[element] += sign * coefficient * int(count or "1")
                    charge += sign * coefficient * int(compound["charge"][0])
                    s, o = (
                        (chemical, reaction["id"])
                        if side == "substrates"
                        else (reaction["id"], chemical)
                    )
                    matches = [
                        e
                        for e in record["mechanistic_edges"]
                        if (e["subject"], e["predicate"], e["object"]) == (s, predicate, o)
                    ]
                    assert len(matches) == 1
                    evidence = matches[0]["evidence"][0]
                    assert f"coefficient {coefficient}." in evidence["source_assertion"]
                    assert f"{side_uri}/rh:{property_name}" in evidence["source_locator"]
                    actual_sides.append((reaction["id"], side, chemical, coefficient))
                    participant_node = next(
                        p for p in record["participants"] if p["id"] == chemical
                    )
                    assert participant_node["label"] == chem["rdfs:label"]
        assert not any(balance.values()) and charge == 0, (reaction["id"], balance, charge)
        balances[reaction["id"]] = {
            "atom_residual": dict(balance),
            "charge_residual": charge,
            "generic_redox_class": reaction["id"] == "RHEA:36724",
        }
expected_sides = [
    (r["id"], s["side"], s["id"], s["coefficient"]) for r in projection["rhea"] for s in r["sides"]
]
assert sorted(actual_sides) == sorted(expected_sides) and len(actual_sides) == 12
assert sum(e["predicate"] in {"consumes", "produces"} for e in record["mechanistic_edges"]) == 12

# Original source submission verifies strain U and exact protein sequences,
# including the merged UniProt PeaC entry; no nearby strain is substituted.
ena = (RAW / "ena-EF406120.txt").read_text()
assert '/strain="U"' in ena and '/db_xref="taxon:303"' in ena
protein_map = {
    "B1N7H2": ("peaA", "ABR57204.1"),
    "B1N7G9": ("peaD", "ABR57201.1"),
    "B1N7H0": ("peaC", "ABR57202.1"),
    "B1N7H1": ("peaB", "ABR57203.1"),
    "B1N7H3": ("peaE", "ABR57205.1"),
}
for accession, (gene, protein) in protein_map.items():
    entry = json.loads((RAW / f"uniprot-{accession}.json").read_text())
    assert entry["primaryAccession"] == accession and entry["organism"]["taxonId"] == 303
    assert entry["entryType"] == "UniProtKB unreviewed (TrEMBL)"
    assert entry["genes"][0]["geneName"]["value"] == gene
    block = next(x for x in ena.split("FT   CDS") if f'/protein_id="{protein}"' in x)
    translation = re.search(r'/translation="([^\"]+)"', block).group(1)
    # Remove EMBL continuation prefixes before whitespace, preserving actual
    # phenylalanine-threonine (FT) pairs inside the amino-acid sequence.
    translation = re.sub(r"(?m)^FT\s+", "", translation)
    translation = re.sub(r"\s", "", translation)
    assert translation == entry["sequence"]["value"]
complex_node = native("CPLX-8088", "Protein")
components = {
    x.find("Protein").get("frameid"): x.findtext("coefficient")
    for x in complex_node.findall("component")
}
assert components == {"MONOMER-15729": "1", "MONOMER-15730": "1", "MONOMER-15731": "1"}
for monomer, accession in [
    ("MONOMER-15729", "B1N7H2"),
    ("MONOMER-15730", "B1N7G9"),
    ("MONOMER-15731", "B1N7H0"),
    ("MONOMER-15732", "B1N7H3"),
]:
    assert any(
        x.findtext("dblink-db") == "UNIPROT" and x.findtext("dblink-oid") == accession
        for x in native(monomer, "Protein").findall("dblink")
    )
assert "CPLX-8089" not in {x["id"].split(":")[-1] for x in record["participants"]}
assert "in silico" in record["description"]
assert "PeaF/G" in record["description"] and "A/AH2" in record["description"]
assert all(
    "in silico" in e["description"]
    for e in record["mechanistic_edges"]
    if e["predicate"] == "has_part"
)
assert not any(
    e["predicate"] == "has_part" and e["object"] == "UniProtKB:B1N7H1"
    for e in record["mechanistic_edges"]
)
brenda = (RAW / "brenda-686425.html").read_text()
for text in [
    "determinated by in silico-experiments",
    "two hemes acting as redox active groups",
    "before its translocation to the periplasmic space",
]:
    assert text in brenda
abstract = json.loads((RAW / "primary-18177365-europe.json").read_text())["resultList"]["result"][0]
assert (
    abstract["id"] == "18177365"
    and "quinohaemoprotein amine dehydrogenase" in abstract["abstractText"]
)
assert abstract["inPMC"] == "N" and abstract["isOpenAccess"] == "N"

# Actual in-memory exporter checks preserve every edge/evidence/metadata block.
exported_edges = kgx_edges([validated])
exported_nodes = kgx_nodes([validated])
assert len(exported_edges) == 24 and len(exported_nodes) == 22
assert sum(len(json.loads(e.evidence)) for e in exported_edges) == 45
assert all(json.loads(e.reference_metadata) for e in exported_edges)
assert not any(n.id == "MetaCyc:CPLX-8089" for n in exported_nodes)
assert digest(TARGET) == initial_hash
receipt = {
    "status": "passed",
    "checked_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "record_sha256": initial_hash,
    "record": record["id"],
    "replay_script_sha256": digest(Path(__file__)),
    "previous_attempt": {
        "session": 64281,
        "exit_code": 1,
        "log": "/private/tmp/pathwaymech-next-189-phenethylamine-ii-replay.log",
        "log_sha256": digest("/private/tmp/pathwaymech-next-189-phenethylamine-ii-replay.log"),
        "cause": (
            "The original helper stripped genuine FT amino-acid pairs while removing EMBL "
            "continuation prefixes. Anchored prefix removal corrected the helper; no source "
            "or record bytes changed. The corrected exact-sequence checks passed."
        ),
    },
    "source_hashes": source_hashes,
    "checks": {
        "native_and_closed_schema": "passed",
        "original_body_hashes": len(source_hashes),
        "native_members": 2,
        "chemical_sides": 12,
        "reaction_balances": balances,
        "strain_U_sequence_bridges": 5,
        "native_component_bridges": 4,
        "bounded_assembly_and_redox_regressions": "passed",
        "actual_KGX": {"nodes": 22, "edges": 24, "evidence": 45},
    },
    "limitations": [
        "Author replay, not independent scientific review.",
        "Generic Rhea A/AH2 formula balance does not identify a physiological carrier.",
        "Primary18177365 full body unavailable; source-curated statements retain their tier.",
        "Full corpus/render/authority integration gates are owned by root and pending.",
    ],
}
(DOSSIER / "phenethylamine-ii-validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(
    json.dumps(
        {"status": "passed", "record_sha256": initial_hash, "checks": receipt["checks"]}, indent=2
    )
)
