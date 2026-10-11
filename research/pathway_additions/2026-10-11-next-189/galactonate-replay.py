"""Replay this record's exact native/Rhea/protein claims against retained bodies.

Run from the cohort repository with its locked environment. Raw sources remain
external; this author check is not a substitute for independent scientific review.
"""

import collections
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

import yaml

from pathwaymech.kgx import kgx_edges, kgx_nodes, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path(__file__).resolve().parents[3]
RAW = Path("/private/tmp/pathwaymech-next-189-evidence/galactonate")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = Path(__file__).resolve().parent
TARGET = ROOT / "data/pathways/d-galactonate-degradation.yaml"
START = datetime.datetime.now(datetime.UTC).isoformat()
R = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
SPECS = [
    ("18649", "18650", "GALACTONDEHYDRAT-RXN", "GALACTONATE-DEHYDRATASE-MONOMER", "Q6BF17"),
    ("16525", "16526", "DEHYDDEOXGALACTKIN-RXN", "DEHYDDEOXGALACTKIN-MONOMER", "P31459"),
    (
        "24464",
        "24465",
        "DEHYDDEOXPHOSGALACT-ALDOL-RXN",
        "DEHYDDEOXPHOSGALACT-ALDOL-MONOMER",
        "Q6BF16",
    ),
]


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


before = sha(TARGET)
record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
errors = strict_errors([TARGET], ROOT)
assert not errors, errors
assert record["id"] == "MetaCyc:GALACTCAT-PWY"
assert len(record["participants"]) == 14 and len(record["reactions"]) == 3
assert len(record["mechanistic_edges"]) == 27
triplets = [(e["subject"], e["predicate"], e["object"]) for e in record["mechanistic_edges"]]
assert len(set(triplets)) == len(triplets), "No duplicate general contains/containsN edges"
manifest = json.loads((DOSSIER / "galactonate-source-manifest.json").read_text())
hashes = {}
for source in manifest["sources"]:
    digest = sha(source["file"])
    assert digest == source["sha256"], source["file"]
    hashes[source["file"]] = digest
for reference in record["references"]:
    assert hashes[manifest["reference_artifacts"][reference["id"]]] == reference["source_sha256"]

families = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    fields = line.split("\t")
    if fields[0] in {spec[0] for spec in SPECS}:
        families[fields[0]] = dict(
            zip(
                ["master", "left_to_right", "right_to_left", "bidirectional"],
                fields,
                strict=True,
            )
        )
numbers = {v for family in families.values() for v in family.values()}
triples = collections.defaultdict(lambda: collections.defaultdict(list))
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
    parser = ET.iterparse(stream, events=("start", "end"))
    _, top = next(parser)
    for event, node in parser:
        if event != "end" or node.tag != RDF + "Description":
            continue
        uri = node.get(RDF + "about", "")
        key = uri.removeprefix(R)
        if (
            key.split("_")[0] in numbers
            or (key.startswith("Participant_") and key.split("_")[1] in numbers)
            or key.startswith("Compound_")
        ):
            for child in node:
                value = child.get(RDF + "resource") or (child.text or "").strip()
                prop = child.tag.split("}")[-1]
                if value not in triples[uri][prop]:
                    triples[uri][prop].append(value)
        node.clear()
        top.clear()

balances, sides, net = [], [], collections.Counter()
with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as db:

    def props(cid):
        return {
            p: v if v is not None else o
            for p, v, o in db.execute(
                "select predicate,value,object from statements where subject=?",
                (cid,),
            )
        }

    for reaction in record["reactions"]:
        rid = reaction["id"].split(":")[1]
        master = next(m for m, f in families.items() if f[reaction["direction"]] == rid)
        assert R + rid in triples[R + master]["directionalReaction"]
        assert reaction["label"] == triples[R + rid]["equation"][0]
        total = collections.Counter()
        for side, predicate, sign in [("substrates", "consumes", -1), ("products", "produces", 1)]:
            side_uri = triples[R + rid][side][0]
            expected = {}
            for prop, participants in triples[side_uri].items():
                if not re.fullmatch(r"contains\d+", prop):
                    continue
                for participant in participants:
                    compound = triples[participant]["compound"][0]
                    cid = "CHEBI:" + triples[compound]["chebi"][0].split("_")[-1]
                    coefficient = int(prop[8:])
                    expected[cid] = coefficient
                    authoritative = props(cid)
                    formula = triples[compound]["formula"][0]
                    charge = triples[compound]["charge"][0]
                    assert formula == authoritative["chemrof:generalized_empirical_formula"]
                    assert charge == str(authoritative["chemrof:charge"])
                    for atom, amount in re.findall(r"([A-Z][a-z]?)(\d*)", formula):
                        total[atom] += sign * coefficient * int(amount or 1)
                    total["charge"] += sign * coefficient * int(charge)
                    net[cid] += sign * coefficient
            actual = {
                e["subject"] if sign == -1 else e["object"]: e.get("stoichiometry", 1)
                for e in record["mechanistic_edges"]
                if e["predicate"] == predicate
                and (e["object"] if sign == -1 else e["subject"]) == reaction["id"]
            }
            assert actual == expected, (reaction["id"], side, actual, expected)
            sides.extend(
                {"reaction": reaction["id"], "side": side, "chemical": c, "coefficient": n}
                for c, n in expected.items()
            )
        assert not any(total.values()), (reaction["id"], total)
        balances.append({"reaction": reaction["id"], "residuals": dict(total)})
    for participant in record["participants"]:
        if participant["id"].startswith("CHEBI:"):
            assert props(participant["id"])["rdfs:label"] == participant["label"]
assert len(sides) == 11
assert {c: n for c, n in net.items() if n} == {
    "CHEBI:12931": -1,
    "CHEBI:30616": -1,
    "CHEBI:15377": 1,
    "CHEBI:456216": 1,
    "CHEBI:15378": 1,
    "CHEBI:59776": 1,
    "CHEBI:15361": 1,
}

native = ET.parse(RAW / "GALACTCAT-PWY.xml").find("Pathway")
assert native.findtext("common-name") == record["label"]
native_ids = [s[2] for s in SPECS]
assert {n.get("frameid") for n in native.findall("reaction-list/Reaction")} == set(native_ids)
assert {
    (n.find("Reaction").get("frameid"), n.find("predecessor-reactions/Reaction").get("frameid"))
    for n in native.findall("reaction-ordering")
} == set(zip(native_ids[1:], native_ids[:-1], strict=True))
assert {
    n.find("Reaction").get("frameid"): n.findtext("direction")
    for n in native.findall("reaction-layout")
} == {n: "L2R" for n in native_ids}
for master, direct, nrxn, protein, accession in SPECS:
    reaction = ET.parse(RAW / f"metacyc-{nrxn}.xml").find("Reaction")
    refs = [
        n.findtext("dblink-oid")
        for n in reaction.findall("dblink")
        if n.findtext("dblink-db") == "RHEA"
    ]
    assert refs == [families[master]["bidirectional"] if master == "24464" else direct]
    assert reaction.findtext("reaction-direction") == (
        "REVERSIBLE" if master == "24464" else "LEFT-TO-RIGHT"
    )
    protein_node = ET.parse(RAW / f"metacyc-{protein}.xml").find("Protein")
    assert (accession, "unification") in [
        (n.findtext("dblink-oid"), n.findtext("dblink-relationship"))
        for n in protein_node.findall("dblink")
        if n.findtext("dblink-db") == "UNIPROT"
    ]
    assert protein_node.find("species/Organism").get("frameid") == "TAX-511145"
    assert nrxn in [
        n.get("frameid")
        for n in protein_node.findall("catalyzes/Enzymatic-Reaction/reaction/Reaction")
    ]
    assert not protein_node.findall("component-of"), "Reassess assembly source if native changes"
    up = json.loads((RAW / f"uniprot-{accession}.json").read_text())
    assert up["organism"]["taxonId"] == 83333
    assert (
        next(p["label"] for p in record["participants"] if p["id"] == "UniProtKB:" + accession)
        == up["proteinDescription"]["recommendedName"]["fullName"]["value"]
    )
    reaction_comment = next(
        c["reaction"] for c in up["comments"] if c["commentType"] == "CATALYTIC ACTIVITY"
    )
    assert {"database": "Rhea", "id": "RHEA:" + master} in reaction_comment[
        "reactionCrossReferences"
    ]
    assert ("UniProtKB:" + accession, "enables", "RHEA:" + direct) in triplets

up_d = json.loads((RAW / "uniprot-Q6BF17.json").read_text())
assert up_d["comments"][2]["cofactors"][0]["evidences"] == [{"evidenceCode": "ECO:0000250"}]
up_a = json.loads((RAW / "uniprot-Q6BF16.json").read_text())
assert up_a["comments"][4]["texts"][0]["value"] == "Homotrimer"
for up in [up_d, up_a]:
    assert "fused dgoA and dgoD" in next(
        c["note"] for c in up["comments"] if c["commentType"] == "SEQUENCE CAUTION"
    )
for edge in record["mechanistic_edges"]:
    for evidence in edge["evidence"]:
        if evidence["reference_id"].startswith("RHEA:"):
            for subject, predicate, obj in re.findall(
                r"(http://rdf\.rhea-db\.org/\S+) rh:(\w+) (https?://[A-Za-z0-9_./:-]+)",
                evidence["source_locator"],
            ):
                assert obj.rstrip(";") in triples[subject][predicate], (
                    edge["id"],
                    subject,
                    predicate,
                    obj,
                )
        if evidence["reference_id"] == "PMID:17981470":
            assert (edge["subject"], edge["predicate"], edge["object"]) == (
                "UniProtKB:Q6BF16",
                "enables",
                "RHEA:24465",
            )
        if evidence["reference_id"] == "PMID:33224125":
            assert (edge["subject"], edge["predicate"], edge["object"]) == (
                "CHEBI:12931",
                "inhibits",
                "UniProtKB:P31460",
            )
        if evidence["reference_id"] == "PMID:30455279":
            assert edge["predicate"] in {"part_of", "regulates", "inhibits"}
    if edge["predicate"] == "has_cofactor":
        assert edge["subject"] == "UniProtKB:Q6BF17", "Do not assign an exclusive DgoR metal"


# Replay exact source figure panel attachment after independent issue352.
class FigureText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.current = None
        self.parts = []
        self.figures = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.current is None and attrs.get("id") in {"F1", "F8"}:
            self.current = attrs["id"]
            self.depth = 1
            self.parts = []
        elif self.current and tag not in {
            "img",
            "br",
            "hr",
            "meta",
            "link",
            "input",
            "source",
            "wbr",
        }:
            self.depth += 1

    def handle_endtag(self, tag):
        if self.current:
            self.depth -= 1
            if not self.depth:
                self.figures[self.current] = " ".join(self.parts)
                self.current = None

    def handle_data(self, data):
        if self.current:
            self.parts.append(data.strip())


figure_parser = FigureText()
figure_parser.feed((RAW / "PMC6351737.html").read_text())
growth_panel = figure_parser.figures["F1"].split("(C)", 1)[1].split("(D)", 1)[0]
assert "cultures were spotted" in growth_panel and "M9 minimal medium" in growth_panel
effector_ab = figure_parser.figures["F8"].split("(A and B)", 1)[1].split("(C)", 1)[0]
effector_c = figure_parser.figures["F8"].split("(C)", 1)[1]
assert "releases DgoR from its target DNA" in effector_ab
assert "trypsin-mediated digestion" in effector_c
for edge_number, expected_locator in [("025", "Fig. 1C"), ("027", "Fig. 8A-C")]:
    edge = next(
        e for e in record["mechanistic_edges"] if e["id"] == "galactonate-edge-" + edge_number
    )
    evidence = next(e for e in edge["evidence"] if e["reference_id"] == "PMID:30455279")
    assert expected_locator in evidence["source_locator"]

nodes, edges = kgx_nodes([validated]), kgx_edges([validated])
assert len(nodes) == 19 and len(edges) == 27
for original, exported in zip(record["mechanistic_edges"], edges, strict=True):
    assert json.loads(exported.evidence) == original["evidence"]
    assert exported.description == original.get("description", "")
    assert exported.subject == original["subject"] and exported.object == original["object"]
kgx_paths = write_kgx([validated], RAW / "author-kgx")
assert sha(TARGET) == before
result = {
    "status": "passed",
    "started_at": START,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": before,
    "native_and_closed_schema": "passed",
    "raw_source_hashes": hashes,
    "direction_families": families,
    "native_complete_reactions": native_ids,
    "chemical_sides": sides,
    "atom_charge_balances": balances,
    "net_stoichiometry": {c: n for c, n in net.items() if n},
    "gene_product_native_identity_and_taxon": "passed",
    "assembly_and_inference_limits": "passed",
    "rhea_exact_locator_triples": "passed",
    "primary_attachment_regressions": "passed",
    "primary_figure_panel_attachment_regression": "passed: F1(C) growth and F8(A-C) effector",
    "issue352": json.loads((DOSSIER / "galactonate-source-projection.json").read_text())[
        "review_issue352"
    ],
    "actual_kgx": {
        "nodes": len(nodes),
        "edges": len(edges),
        "evidence": sum(len(e["evidence"]) for e in record["mechanistic_edges"]),
        "files": [{"path": str(p), "sha256": sha(p)} for p in kgx_paths],
    },
    "script_sha256": sha(__file__),
    "scope": (
        "Author narrow raw replay; full corpus/render/test/lint and independent "
        "scientific review are delegated to root and another reviewer, not claimed here."
    ),
}
(DOSSIER / "galactonate-validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {k: v for k, v in result.items() if k not in {"raw_source_hashes", "chemical_sides"}},
        indent=2,
    )
)
