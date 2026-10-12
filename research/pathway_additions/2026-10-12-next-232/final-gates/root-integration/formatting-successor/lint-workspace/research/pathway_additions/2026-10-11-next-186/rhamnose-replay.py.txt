"""Replay the complete dTDP-rhamnose record against retained primary authorities.

Run from the repository root. External raw source paths are recorded in the
manifest; no record or authority snapshot is constructed from fixture data.
"""

import collections
import csv
import datetime
import gzip
import hashlib
import importlib.util
import io
import json
import re
import sqlite3
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

from pathwaymech.kgx import render_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-186-evidence/rhamnose")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-186"
TARGET = ROOT / "data/pathways/dtdp-l-rhamnose-biosynthesis.yaml"
START = datetime.datetime.now(datetime.UTC).isoformat()
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
ORDER = [
    ("DTDPGLUCOSEPP-RXN", "15225", "15226", "left_to_right", "P37744"),
    ("DTDPGLUCDEHYDRAT-RXN", "17221", "17222", "left_to_right", "P37759"),
    ("DTDPDEHYDRHAMEPIM-RXN", "16969", "16970", "left_to_right", "P37745"),
    ("DTDPDEHYRHAMREDUCT-RXN", "21796", "21798", "right_to_left", "P37760"),
]


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            result.update(block)
    return result.hexdigest()


def ontology(database, identifier):
    with sqlite3.connect(f"file:{CACHE}/{database}.db?mode=ro", uri=True) as connection:
        rows = connection.execute(
            "select predicate,value,object from statements where subject=?", (identifier,)
        ).fetchall()
    return rows


def properties(database, identifier):
    return {
        p: v if v is not None else o
        for p, v, o in ontology(database, identifier)
        if p
        in {
            "rdfs:label",
            "owl:deprecated",
            "chemrof:charge",
            "chemrof:generalized_empirical_formula",
        }
    }


def native(frame, kind):
    path = RAW / f"{frame}.xml"
    if not path.exists():
        path = RAW / f"metacyc-{frame}.xml"
    return next(
        x
        for x in ET.parse(path).iter(kind)
        if x.get("frameid") == frame and x.get("detail") == "full"
    )


record = yaml.safe_load(TARGET.read_text())
typed = validate_record(record)
assert strict_errors([TARGET], ROOT) == []
assert record["id"] == "GO:0019305"
assert len(record["participants"]) == 19 and len(record["reactions"]) == 4
assert len(record["mechanistic_edges"]) == 31
assert sum(len(e["evidence"]) for e in record["mechanistic_edges"]) == 67
manifest = json.loads((DOSSIER / "rhamnose-source-manifest.json").read_text())
raw_hashes = {}
for row in manifest["sources"]:
    actual = digest(row["file"])
    assert actual == row["sha256"], row["file"]
    raw_hashes[row["file"]] = actual
    assert not set(row.get("metadata", {})) - {
        "Content-Type",
        "Last-Modified",
        "X-UniProt-Release",
        "X-UniProt-Release-Date",
    }
    for name in ["url", "final_url"]:
        if name in row:
            query = urllib.parse.parse_qs(urllib.parse.urlsplit(row[name]).query)
            assert not {k.lower() for k in query} & {
                "expires",
                "checksum",
                "accname",
                "token",
                "key",
                "session",
                "access_token",
            }, (name, row["file"])
for reference in record["references"]:
    assert digest(manifest["reference_artifacts"][reference["id"]]) == reference["source_sha256"]
projection = json.loads((DOSSIER / "rhamnose-source-projection.json").read_text())
assert projection["target_sha256"] == digest(TARGET)
directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    cells = line.split("\t")
    if cells[0] in {x[1] for x in ORDER}:
        directions[cells[0]] = dict(
            zip(["master", "left_to_right", "right_to_left", "bidirectional"], cells, strict=True)
        )
assert directions == projection["rhea"]["directions"]
numbers = {v for row in directions.values() for v in row.values()}
nodes, compounds = {}, {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
    context = ET.iterparse(stream, events=("start", "end"))
    _, root = next(context)
    for event, element in context:
        if event != "end" or element.tag != RDF + "Description":
            continue
        uri = element.get(RDF + "about", "")
        name = uri.rsplit("/", 1)[-1]
        chosen = name.split("_", 1)[0] in numbers or (
            name.startswith("Participant_") and name.split("_")[1] in numbers
        )
        destination = nodes if chosen else compounds if name.startswith("Compound_") else None
        if destination is not None:
            for child in element:
                key = child.tag.rsplit("}", 1)[-1]
                value = child.get(RDF + "resource") or (child.text or "").strip()
                if value not in destination.setdefault(uri, {}).setdefault(key, []):
                    destination[uri][key].append(value)
        element.clear()
        root.clear()
needed = {v for x in nodes.values() for vs in x.values() for v in vs if v in compounds}
nodes.update({u: compounds[u] for u in needed})
assert nodes == projection["rhea"]["nodes"]
sides, chemicals, net = [], {}, collections.Counter()
for _frame, master, rid, direction, _accession in ORDER:
    reaction = next(r for r in record["reactions"] if r["id"] == "RHEA:" + rid)
    assert RH + rid in nodes[RH + master]["directionalReaction"]
    assert directions[master][direction] == rid
    assert reaction["direction"] == direction
    assert reaction["label"] == nodes[RH + rid]["equation"][0]
    for side in ["substrates", "products"]:
        su = nodes[RH + rid][side][0]
        for prop, values in nodes[su].items():
            if not re.fullmatch(r"contains\d+", prop):
                continue
            for participant in values:
                compound = nodes[participant]["compound"][0]
                chemical = "CHEBI:" + nodes[compound]["chebi"][0].rsplit("_", 1)[-1]
                authoritative = properties("chebi", chemical)
                assert (
                    authoritative["chemrof:generalized_empirical_formula"]
                    == nodes[compound]["formula"][0]
                )
                assert str(authoritative["chemrof:charge"]) == nodes[compound]["charge"][0]
                chemicals[chemical] = authoritative
                item = dict(
                    reaction="RHEA:" + rid,
                    master=master,
                    direction=direction,
                    side=side,
                    chemical=chemical,
                    coefficient=int(prop[8:]),
                    side_uri=su,
                    participant_uri=participant,
                    compound_uri=compound,
                )
                sides.append(item)
                net[chemical] += (1 if side == "products" else -1) * item["coefficient"]
                edge = next(
                    e
                    for e in record["mechanistic_edges"]
                    if (e["subject"], e["predicate"], e["object"])
                    == (
                        (chemical, "consumes", "RHEA:" + rid)
                        if side == "substrates"
                        else ("RHEA:" + rid, "produces", chemical)
                    )
                )
                evidence = edge["evidence"][0]
                assert f"coefficient {item['coefficient']}" in evidence["source_assertion"]
                assert f"{su} rh:{prop} {participant}" in evidence["source_locator"]
assert sorted(sides, key=str) == sorted(projection["chemical_sides"], key=str)
assert len(sides) == 15
assert (
    len([e for e in record["mechanistic_edges"] if e["predicate"] in ["consumes", "produces"]])
    == 15
)
balances = {}
for reaction in record["reactions"]:
    atoms, charge = collections.Counter(), 0
    for side in (s for s in sides if s["reaction"] == reaction["id"]):
        multiplier = (1 if side["side"] == "products" else -1) * side["coefficient"]
        authoritative = chemicals[side["chemical"]]
        for element, count in re.findall(
            r"([A-Z][a-z]?)(\d*)", authoritative["chemrof:generalized_empirical_formula"]
        ):
            atoms[element] += multiplier * int(count or 1)
        charge += multiplier * int(authoritative["chemrof:charge"])
    assert all(v == 0 for v in atoms.values()) and charge == 0, reaction
    balances[reaction["id"]] = dict(atom_residuals=dict(atoms), charge_residual=charge)
net = {k: v for k, v in net.items() if v}
assert net == {
    "CHEBI:37568": -1,
    "CHEBI:58601": -1,
    "CHEBI:15378": -2,
    "CHEBI:33019": 1,
    "CHEBI:15377": 1,
    "CHEBI:57783": -1,
    "CHEBI:57510": 1,
    "CHEBI:58349": 1,
}, net
pathway = native("DTDPRHAMSYN-PWY", "Pathway")
assert {x.get("frameid") for x in pathway.findall("reaction-list/Reaction")} == {
    x[0] for x in ORDER
}
for index, (frame, master, _rid, direction, accession) in enumerate(ORDER):
    layouts = [
        x for x in pathway.findall("reaction-layout") if x.find("Reaction").get("frameid") == frame
    ]
    assert len(layouts) == 1
    assert layouts[0].findtext("direction") == ("R2L" if direction == "right_to_left" else "L2R")
    xrefs = [
        (x.findtext("dblink-db"), x.findtext("dblink-oid"))
        for x in native(frame, "Reaction").findall("dblink")
    ]
    assert ("RHEA", "15228" if master == "15225" else master) in xrefs
    if index:
        assert any(
            [x.get("frameid") for x in item.iter("Reaction")] == [frame, ORDER[index - 1][0]]
            for item in pathway.findall("reaction-ordering")
        )
    protein = json.loads((RAW / f"uniprot-{accession}.json").read_text())
    assert protein["primaryAccession"] == accession and protein["organism"]["taxonId"] == 83333
    assert protein["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    assert any(
        x["id"] == "RHEA:" + master
        for x in protein["comments"][1]["reaction"]["reactionCrossReferences"]
    )
    assert protein["comments"][1]["reaction"]["evidences"][0]["evidenceCode"] == (
        "ECO:0000269" if accession == "P37744" else "ECO:0000250"
    )
    assert (
        next(p["label"] for p in record["participants"] if p["id"] == "UniProtKB:" + accession)
        == protein["proteinDescription"]["recommendedName"]["fullName"]["value"]
    )
for acc, complex_id, monomer, count in [
    ("P37744", "CPLX0-8034", "DTDPGLUCOSEPP-MONOMER", "4"),
    ("P37759", "DTDPGLUCDEHYDRAT-CPLX", "DTDPGLUCDEHYDRAT-MONOMER", "2"),
]:
    obj = native(complex_id, "Protein")
    assert obj.findtext("component/coefficient") == count
    assert obj.find("component/Protein").get("frameid") == monomer
    obj = native(monomer, "Protein")
    assert any(
        x.findtext("dblink-db") == "UNIPROT"
        and x.findtext("dblink-oid") == acc
        and x.findtext("dblink-relationship") == "unification"
        for x in obj.findall("dblink")
    )
assert len([e for e in record["mechanistic_edges"] if e["predicate"] == "has_cofactor"]) == 3
assert all(
    e["predicate"] == "enables"
    for e in record["mechanistic_edges"]
    if e["subject"] in ["UniProtKB:P37745", "UniProtKB:P37760"] and e["object"].startswith("RHEA:")
)
assert not any(
    p["id"] in ["UniProtKB:P27830", "UniProtKB:P26392", "UniProtKB:P26394"]
    for p in record["participants"]
)
for e in record["mechanistic_edges"]:
    if e["predicate"] == "provides_input_for":
        products = {
            s["chemical"]
            for s in sides
            if s["reaction"] == e["subject"] and s["side"] == "products"
        }
        substrates = {
            s["chemical"]
            for s in sides
            if s["reaction"] == e["object"] and s["side"] == "substrates"
        }
        assert products & substrates
go = json.loads((RAW / "quickgo-0019305.json").read_text())["results"][0]
assert go["id"] == record["id"] and go["name"] == record["label"] and not go["isObsolete"]
assert ("oio:hasDbXref", "MetaCyc:DTDPRHAMSYN-PWY", None) in ontology("go", record["id"])
for node in record["participants"] + record["taxa"]:
    if node["id"].startswith(("CHEBI:", "NCBITaxon:")):
        authoritative = properties(
            "chebi" if node["id"].startswith("CHEBI:") else "ncbitaxon", node["id"]
        )
        assert node["label"] == authoritative["rdfs:label"]
        assert authoritative.get("owl:deprecated") not in ["true", "1"]
spec = importlib.util.spec_from_file_location(
    "source_builder", ROOT / "scripts/build_source_identifier_snapshot.py"
)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
authority_receipt = json.loads(
    (RAW.parent / "root-authorities/first-fetch-manifest.json").read_text()
)
for identifier in ["MetaCyc:CPLX0-8034", "MetaCyc:DTDPGLUCDEHYDRAT-CPLX"]:
    source = next(x for x in authority_receipt if x["id"] == identifier)
    assert digest(source["path"]) == source["sha256"]
    terms = list(builder.metacyc_terms(Path(source["path"]).read_text()))
    assert len(terms) == 1 and terms[0][0] == identifier
    assert terms[0][1] == next(p["label"] for p in record["participants"] if p["id"] == identifier)
for projected, edge in zip(projection["edge_evidence"], record["mechanistic_edges"], strict=True):
    assert projected == {
        "edge": edge["id"],
        **{k: edge[k] for k in ["subject", "predicate", "object", "evidence"]},
    }
export = render_kgx([typed])
output_dir = RAW / "kgx-author-replay"
output_dir.mkdir(exist_ok=True)
for name, content in export.items():
    (output_dir / name).write_text(content)
edge_rows = list(csv.DictReader(io.StringIO(export["edges.tsv"]), delimiter="\t"))
node_rows = list(csv.DictReader(io.StringIO(export["nodes.tsv"]), delimiter="\t"))
assert len(edge_rows) == 31 and len(node_rows) == 25
for original in record["mechanistic_edges"]:
    row = next(
        e
        for e in edge_rows
        if e["subject"] == original["subject"]
        and e["object"] == original["object"]
        and e["predicate"].rsplit(":", 1)[-1]
        == (
            {"part_of": "0000050", "provides_input_for": "0002413"}.get(
                original["predicate"], original["predicate"]
            )
        )
    )
    assert json.loads(row["evidence"]) == original["evidence"]
    assert row["description"] == original.get("description", "")
assert sum(len(json.loads(e["evidence"])) for e in edge_rows) == 67
result = dict(
    started_at=START,
    finished_at=datetime.datetime.now(datetime.UTC).isoformat(),
    status="passed",
    target=str(TARGET.relative_to(ROOT)),
    target_sha256=digest(TARGET),
    replay_script_sha256=digest(Path(__file__)),
    checks=[
        "native and closed schema",
        "all retained HTTP source and reference digests",
        "safe metadata and no signed redirect queries",
        "complete full-RDF source replay",
        "15 chemical sides and coefficients",
        "four atom/charge balances and complete net",
        "four native members, ordered topology, cross-reference relation and direction",
        "four reviewed K-12 proteins with exact evidence tiers",
        "native tetramer/dimer component crosswalks",
        "25 canonical named identities including independent native HTML",
        "three shared-intermediate connections",
        "all31 edge evidence projections",
        "actual KGX25 nodes/31 edges/67 evidence and descriptions preserved",
    ],
    balances=balances,
    net_stoichiometry=net,
    raw_hashes=raw_hashes,
    excluded_checks=(
        "Shared corpus gates, history, pages and independent scientific review "
        "belong to root/reviewer."
    ),
)
(RAW / "replay-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps({k: v for k, v in result.items() if k not in ["raw_hashes", "balances"]}, indent=2)
)
