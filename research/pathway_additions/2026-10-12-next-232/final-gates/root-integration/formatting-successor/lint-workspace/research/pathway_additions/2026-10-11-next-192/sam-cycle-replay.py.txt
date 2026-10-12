"""Author replay of complete SAM cycle I against retained original source bytes.

Run from the repository root. This is author validation, not independent review.
No network calls, source refreshes, page writes or corpus-wide gates are run.
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
RAW = Path("/private/tmp/pathwaymech-next-192-evidence/sam-cycle")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-192"
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/s-adenosyl-l-methionine-cycle-i.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            value.update(block)
    return value.hexdigest()


def native(frame):
    return next(
        e
        for e in ET.parse(RAW / f"metacyc-{frame}.xml").getroot()
        if e.get("frameid") == frame and e.get("detail") == "full"
    )


started = datetime.datetime.now(datetime.UTC).isoformat()
record = yaml.safe_load(TARGET.read_text())
initial_hash = digest(TARGET)
validated = validate_record(record)
assert not strict_errors([TARGET], ROOT)
manifest = json.loads((DOSSIER / "sam-cycle-source-manifest.json").read_text())
projection = json.loads((DOSSIER / "sam-cycle-source-projection.json").read_text())
assert manifest["record_sha256"] == projection["record_sha256"] == initial_hash
hashes = {}
for source in manifest["sources"]:
    path = source["path"]
    hashes[path] = digest(path)
    assert hashes[path] == source["sha256"], path
for reference in record["references"]:
    path = manifest["reference_artifacts"][reference["id"]]
    assert hashes[path] == reference["source_sha256"], reference["id"]

parent = native("PWY-6151")
assert {x.get("frameid") for x in parent.findall("reaction-list/*")} == {
    "SAM-PWY",
    "RXN-7605",
    "ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN",
    "RIBOSYLHOMOCYSTEINASE-RXN",
    "HOMOCYSMET-RXN",
}
assert [x.get("frameid") for x in native("SAM-PWY").findall("reaction-list/*")] == [
    "S-ADENMETSYN-RXN"
]
orders = {
    (p.get("frameid"), x.find("Reaction").get("frameid"))
    for x in parent.findall("reaction-ordering")
    for p in x.findall("predecessor-reactions/Reaction")
}
assert len(orders) == 5
assert "Escherichia coli" in parent.findtext("comment")
assert "EC 2.1.1.13" in parent.findtext("comment")
assert "EC 2.1.1.14" in parent.findtext("comment")

# Read actual complete release RDF once, not the authored projection alone.
needed = set()
for r in projection["rhea"]:
    master = int(r["master"].split(":")[1])
    needed.update(RH + str(master + i) for i in range(4))
    for side in r["sides"]:
        needed.update(side[k] for k in ["side_uri", "participant_uri", "compound_uri"])
nodes = {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
    parser = ET.iterparse(stream, events=("start", "end"))
    _, root = next(parser)
    for event, element in parser:
        if event != "end" or element.tag != RDF + "Description":
            continue
        uri = element.get(RDF + "about", "")
        if uri in needed:
            for child in element:
                k = child.tag.rsplit("}", 1)[-1]
                v = child.get(RDF + "resource") or (child.text or "").strip()
                values = nodes.setdefault(uri, {}).setdefault(k, [])
                if v not in values:
                    values.append(v)
        element.clear()
        root.clear()
assert set(nodes) == needed
edges = record["mechanistic_edges"]
parts = {p["id"]: p for p in record["participants"]}
reactions = {p["id"]: p for p in record["reactions"]}
actual_sides = []
balances = {}
directions = {
    cells[0]: cells[1:]
    for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]
    if (cells := line.split("\t"))
}


def formulas(formula):
    return collections.Counter(
        {e: int(n or "1") for e, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula)}
    )


def edge_match(s, p, o):
    found = [e for e in edges if (e["subject"], e["predicate"], e["object"]) == (s, p, o)]
    assert len(found) == 1, (s, p, o)
    return found[0]


with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as connection:
    for r in projection["rhea"]:
        rid, master = r["id"].split(":")[1], r["master"].split(":")[1]
        assert directions[master][0] == rid
        assert RH + rid in nodes[RH + master]["directionalReaction"]
        assert reactions[r["id"]]["direction"] == "left_to_right"
        assert reactions[r["id"]]["label"] == nodes[RH + rid]["equation"][0]
        balance = collections.Counter()
        charge = 0
        for side, sign, predicate in [("substrates", -1, "consumes"), ("products", 1, "produces")]:
            su = nodes[RH + rid][side][0]
            for key, participants in nodes[su].items():
                if not re.fullmatch(r"contains\d+", key):
                    continue
                coefficient = int(key[8:])
                for participant in participants:
                    cu = nodes[participant]["compound"][0]
                    comp = nodes[cu]
                    chem = comp["accession"][0]
                    authoritative = dict(
                        connection.execute(
                            "select predicate,value from statements "
                            "where subject=? and predicate in "
                            "('rdfs:label','chemrof:charge','chemrof:generalized_empirical_formula')",
                            (chem,),
                        )
                    )
                    assert authoritative["rdfs:label"] == parts[chem]["label"]
                    assert authoritative["chemrof:charge"] == comp["charge"][0]
                    assert (
                        authoritative["chemrof:generalized_empirical_formula"] == comp["formula"][0]
                    )
                    for atom, amount in formulas(comp["formula"][0]).items():
                        balance[atom] += sign * coefficient * amount
                    charge += sign * coefficient * int(comp["charge"][0])
                    s, o = (chem, r["id"]) if sign < 0 else (r["id"], chem)
                    e = edge_match(s, predicate, o)
                    assert e["evidence"][0]["reference_id"] == r["master"]
                    assert f"coefficient {coefficient}." in e["evidence"][0]["source_assertion"]
                    assert f"{su}/rh:{key}" in e["evidence"][0]["source_locator"]
                    actual_sides.append((r["id"], side, chem, coefficient))
        assert not any(balance.values()) and charge == 0
        balances[r["id"]] = {"atom_residual": dict(balance), "charge_residual": charge}
expected = [
    (r["id"], s["side"], s["compound"]["accession"][0], s["coefficient"])
    for r in projection["rhea"]
    for s in r["sides"]
]
assert sorted(actual_sides) == sorted(expected)
assert len(actual_sides) == 21
assert RH + "21199" in nodes[RH + "21196"]["bidirectionalReaction"]

# Check all generic reaction sides directly and the exact compound crosswalks.
generic = native("RXN-7605")
mapping = {
    "S-ADENOSYLMETHIONINE": "CHEBI:59789",
    "ADENOSYL-HOMO-CYS": "CHEBI:57856",
    "PROTON": "CHEBI:15378",
    "Demethylated-methyl-acceptors": "MetaCyc:Demethylated-methyl-acceptors",
    "Methylated-methyl-acceptors": "MetaCyc:Methylated-methyl-acceptors",
}
generic_sides = []
for side in ["left", "right"]:
    for element in generic.findall(side):
        frame = element[0].get("frameid")
        chemical = mapping[frame]
        assert element.findtext("coefficient") in [None, "1"]
        s, o = (chemical, "MetaCyc:RXN-7605") if side == "left" else ("MetaCyc:RXN-7605", chemical)
        e = edge_match(s, "consumes" if side == "left" else "produces", o)
        assert frame in e["evidence"][0]["source_locator"]
        if chemical.startswith("CHEBI:"):
            assert any(
                x.findtext("dblink-db") == "CHEBI"
                and x.findtext("dblink-oid") == chemical.split(":")[1]
                for x in native(frame).findall("dblink")
            )
        else:
            assert parts[chemical]["category"] == "chemical_entity"
            assert native(frame).find("cml/molecule").get("formalCharge") == "0"
            assert "not known or cannot be defined" in native(frame).findtext("comment")
        generic_sides.append((side, chemical, 1))
assert len(generic_sides) == 5
assert generic.findtext("reaction-direction") == "LEFT-TO-RIGHT"
# Formal R-H -> R-CH3 bookkeeping, preserving an unspecified R rather than inventing formula.
assert (
    native("Demethylated-methyl-acceptors").find("cml/molecule/string[@title='smiles']").text
    == "[RH]"
)
assert (
    native("Methylated-methyl-acceptors").find("cml/molecule/string[@title='smiles']").text
    == "C[R]"
)
chemical_formulas = {
    k: v["chemrof:generalized_empirical_formula"] for k, v in projection["chebi"].items()
}
chemical_formulas.update(
    {"MetaCyc:Demethylated-methyl-acceptors": "RH", "MetaCyc:Methylated-methyl-acceptors": "RCH3"}
)
chemical_charge = {k: int(v.get("chemrof:charge", 0)) for k, v in projection["chebi"].items()}
chemical_charge.update(
    {"MetaCyc:Demethylated-methyl-acceptors": 0, "MetaCyc:Methylated-methyl-acceptors": 0}
)
balance = collections.Counter()
charge = 0
for side, chemical, coefficient in generic_sides:
    sign = -1 if side == "left" else 1
    for atom, amount in formulas(chemical_formulas[chemical]).items():
        balance[atom] += sign * coefficient * amount
    charge += sign * coefficient * chemical_charge[chemical]
assert not any(balance.values()) and charge == 0
balances["MetaCyc:RXN-7605"] = {
    "atom_residual": dict(balance),
    "charge_residual": charge,
    "limit": "Formal native R-group balance, not a specific chemical identity.",
}
# Check complete source-defined cycle plus its two documented alternative material links.
frame_to_record = {
    "S-ADENMETSYN-RXN": "RHEA:21081",
    "RXN-7605": "MetaCyc:RXN-7605",
    "ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN": "RHEA:17806",
    "RIBOSYLHOMOCYSTEINASE-RXN": "RHEA:17754",
    "HOMOCYSMET-RXN": "RHEA:21197",
}
assert {(e["subject"], e["object"]) for e in edges if e["predicate"] == "precedes"} == {
    (frame_to_record[a], frame_to_record[b]) for a, b in orders
}
assert {e["subject"] for e in edges if e["predicate"] == "part_of"} == set(reactions)
assert len([e for e in edges if e["predicate"] == "provides_input_for"]) == 2
for frame, monomer, accession, coefficient in [
    ("S-ADENMETSYN-CPLX", "S-ADENMETSYN-MONOMER", "P0A817", 4),
    ("CPLX0-1541", "EG11090-MONOMER", "P0AF12", 2),
]:
    component = native(frame).find("component")
    assert component.find("Protein").get("frameid") == monomer
    assert int(component.findtext("coefficient")) == coefficient
    assert any(
        x.findtext("dblink-db") == "UNIPROT" and x.findtext("dblink-oid") == accession
        for x in native(monomer).findall("dblink")
    )
    edge_match("MetaCyc:" + frame, "has_part", "UniProtKB:" + accession)
for accession, master, _target in [
    ("P0A817", "21080", "RHEA:21081"),
    ("P0AF12", "17805", "RHEA:17806"),
    ("P45578", "17753", "RHEA:17754"),
    ("P25665", "21196", "RHEA:21197"),
    ("P13009", "11172", "RHEA:11173"),
]:
    up = json.loads((RAW / f"uniprot-{accession}.json").read_text())
    assert up["organism"]["taxonId"] == 83333
    assert any(
        x["id"] == "RHEA:" + master
        for c in up["comments"]
        if c["commentType"] == "CATALYTIC ACTIVITY"
        for x in c["reaction"]["reactionCrossReferences"]
    )
    expected_cofactors = {
        c["cofactorCrossReference"]["id"]
        for comment in up["comments"]
        if comment["commentType"] == "COFACTOR"
        for c in comment.get("cofactors", [])
    }
    actual_cofactors = {
        e["object"]
        for e in edges
        if e["subject"] == "UniProtKB:" + accession and e["predicate"] == "has_cofactor"
    }
    assert expected_cofactors == actual_cofactors
# Primary-body inspection is bounded; assert actual full-PDF text locations, not search snippets.
text = (RAW / "primary-11489131.txt").read_text()
for literal in [
    "Pfs must act on SAH before the enzymatic action of LuxS.",
    "E. coli MG1655 genes.",
    "Overexpression and purification of LuxS and Pfs",
    "have prevented the absolute determination of the structure of",
]:
    assert literal in " ".join(text.split())
assert (RAW / "primary-11489131.pdf").read_bytes().startswith(b"%PDF-")
for e in edges:
    for evidence in e["evidence"]:
        assert evidence["source_locator"]
        assert len(evidence["source_assertion"]) <= 400
        if (
            evidence["reference_id"].startswith("PMID:")
            and evidence["reference_id"] != "PMID:11489131"
        ):
            assert "abstractText" in evidence["source_locator"]
# Actual local KGX must preserve every edge/evidence/reference and unrestricted chemical kind.
export_nodes = {n.id: n for n in kgx_nodes([validated])}
export_edges = list(kgx_edges([validated]))
assert len(export_nodes) == 40
assert len(export_edges) == len(edges) == 54
for chemical in ["MetaCyc:Demethylated-methyl-acceptors", "MetaCyc:Methylated-methyl-acceptors"]:
    assert export_nodes[chemical].category == "biolink:ChemicalEntity"
    assert export_nodes[chemical].source_category == "chemical_entity"
for e in edges:
    found = [
        x
        for x in export_edges
        if x.subject == e["subject"]
        and x.object == e["object"]
        and json.loads(x.evidence) == e["evidence"]
    ]
    assert len(found) == 1
assert digest(TARGET) == initial_hash
result = {
    "status": "passed",
    "role": "author verification, not independent review",
    "prior_attempts": [
        {
            "session_id": 66785,
            "exit_code": 1,
            "finding": "All source hashes, Rhea sides and balances passed before a PDF "
            "extraction line break broke a literal substring check. Whitespace "
            "normalization corrected; scientific source wording remains unchanged.",
        },
        {
            "session_id": 72513,
            "exit_code": 1,
            "finding": "Native XML wrapper traversal selected only the first reaction-list child; "
            "full child traversal corrected in author projection/replay. "
            "Target already retained all five native transformations.",
        },
        {
            "session_id": 93017,
            "exit_code": 1,
            "finding": "Author manifest helper omitted successful early fetch receipts using "
            "http_status rather than status. No scientific record changed; "
            "status normalization corrected before this replay.",
        },
    ],
    "started_at": started,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target_sha256": initial_hash,
    "helper_sha256": digest(Path(__file__)),
    "source_hashes_verified": hashes,
    "counts": {
        "participants": 32,
        "reactions": 6,
        "edges": 54,
        "evidence": 109,
        "rhea_sides": 21,
        "generic_sides": 5,
    },
    "checks": [
        "native and closed schemas",
        "full original source hashes/reference digests",
        "five native transformations and MetH alternative",
        "five native cycle orders",
        "Rhea142 full RDF/directions and ChEBI255 sides",
        "six atom/charge balances",
        "two native assemblies and all annotated cofactor IDs",
        "bounded primary-body locators",
        "actual KGX nodes/every edge/evidence",
    ],
    "balances": balances,
    "limits": [
        "No whole-corpus gate or browser claim; parent owns integration.",
        "Generic R-group formula bookkeeping is formal; LuxS iron and homodimer "
        "are similarity annotations.",
        "Full article inspection limited to PMID11489131; other cited primary claims "
        "are abstract-scoped.",
    ],
}
(DOSSIER / "sam-cycle-validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": "passed", "target_sha256": initial_hash, "counts": result["counts"]}))
