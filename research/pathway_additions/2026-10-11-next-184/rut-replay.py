"""Replay the complete corrected Rut route against retained native source bytes."""

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

from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-184-evidence/rut-scout")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-184"
TARGET = ROOT / "data/pathways/uracil-degradation-iii.yaml"
START = datetime.datetime.now(datetime.UTC).isoformat()
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
SELECTED = {
    "21620": ("21622", "right_to_left"),
    "31587": ("31588", "left_to_right"),
    "31603": ("31604", "left_to_right"),
    "15649": ("15650", "left_to_right"),
    "34947": ("34948", "left_to_right"),
    "26438": ("26440", "right_to_left"),
}


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
    return {
        p: v if v is not None else o
        for p, v, o in rows
        if p
        in {
            "rdfs:label",
            "owl:deprecated",
            "chemrof:charge",
            "chemrof:generalized_empirical_formula",
        }
    }


record = yaml.safe_load(TARGET.read_text())
validate_record(record)
assert strict_errors([TARGET], ROOT) == []
assert record["id"] == "MetaCyc:PWY0-1471"
assert len(record["participants"]) == 24 and len(record["reactions"]) == 6
assert len(record["mechanistic_edges"]) == 53
assert sum(len(e["evidence"]) for e in record["mechanistic_edges"]) == 92
manifest = json.loads((DOSSIER / "rut-source-manifest.json").read_text())
raw_hashes = {}
for row in manifest["sources"]:
    actual = digest(row["file"])
    assert actual == row["sha256"], row["file"]
    raw_hashes[row["file"]] = actual
for reference in record["references"]:
    assert digest(manifest["reference_artifacts"][reference["id"]]) == reference["source_sha256"]
projection = json.loads((DOSSIER / "rut-source-projection.json").read_text())
directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    cells = line.split("\t")
    if cells[0] in SELECTED:
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
for master, (rid, direction) in SELECTED.items():
    reaction = next(r for r in record["reactions"] if r["id"] == "RHEA:" + rid)
    assert RH + rid in nodes[RH + master]["directionalReaction"]
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
                native = ontology("chebi", chemical)
                assert (
                    native["chemrof:generalized_empirical_formula"] == nodes[compound]["formula"][0]
                )
                assert str(native["chemrof:charge"]) == nodes[compound]["charge"][0]
                chemicals[chemical] = native
                sides.append(
                    dict(
                        reaction=reaction["id"],
                        master=master,
                        side=side,
                        chemical=chemical,
                        coefficient=int(prop[8:]),
                        side_uri=su,
                        participant_uri=participant,
                        compound_uri=compound,
                    )
                )
                net[chemical] += (1 if side == "products" else -1) * int(prop[8:])
assert sides == projection["chemical_sides"]
assert len(sides) == 33
expected = {
    (s["chemical"], "consumes", s["reaction"])
    if s["side"] == "substrates"
    else (s["reaction"], "produces", s["chemical"])
    for s in sides
}
actual = {
    (e["subject"], e["predicate"], e["object"])
    for e in record["mechanistic_edges"]
    if e["predicate"] in ["consumes", "produces"]
}
assert actual == expected
balances = {}
for reaction in record["reactions"]:
    atoms, charge = collections.Counter(), 0
    for side in (s for s in sides if s["reaction"] == reaction["id"]):
        multiplier = (1 if side["side"] == "products" else -1) * side["coefficient"]
        native = chemicals[side["chemical"]]
        for element, count in re.findall(
            r"([A-Z][a-z]?)(\d*)", native["chemrof:generalized_empirical_formula"]
        ):
            atoms[element] += multiplier * int(count or 1)
        charge += multiplier * int(native["chemrof:charge"])
    assert all(v == 0 for v in atoms.values()) and charge == 0, reaction
    balances[reaction["id"]] = dict(atom_residuals=dict(atoms), charge_residual=charge)
net = {k: v for k, v in net.items() if v}
assert net == {
    "CHEBI:57945": -2,
    "CHEBI:15378": -4,
    "CHEBI:57540": 2,
    "CHEBI:17568": -1,
    "CHEBI:15379": -1,
    "CHEBI:15377": -1,
    "CHEBI:28938": 2,
    "CHEBI:16526": 1,
    "CHEBI:57783": -1,
    "CHEBI:16510": 1,
    "CHEBI:58349": 1,
}, net
for accession, master, rid in [
    ("P75893", "21620", "21622"),
    ("P75898", "31587", "31588"),
    ("P75897", "31603", "31604"),
    ("P0AFQ5", "34947", "34948"),
    ("P39831", "26438", "26440"),
    ("P75894", "26438", "26440"),
]:
    protein = json.loads((RAW / f"uniprot-{accession}.json").read_text())
    assert protein["primaryAccession"] == accession and protein["organism"]["taxonId"] == 83333
    assert protein["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    assert any(
        c.get("reaction")
        and any(x["id"] == "RHEA:" + master for x in c["reaction"]["reactionCrossReferences"])
        for c in protein["comments"]
    )
    label = next(p["label"] for p in record["participants"] if p["id"] == "UniProtKB:" + accession)
    assert label == protein["proteinDescription"]["recommendedName"]["fullName"]["value"]
    subject = "MetaCyc:CPLX0-1962" if accession == "P39831" else "UniProtKB:" + accession
    edge = next(
        e
        for e in record["mechanistic_edges"]
        if e["subject"] == subject and e["object"] == "RHEA:" + rid
    )
    assert any(e["reference_id"] == "UniProtKB:" + accession for e in edge["evidence"])
    assert any(
        e["reference_id"] == "RHEA:" + rid and "directionalReaction" in e["source_locator"]
        for e in edge["evidence"]
    )
    if accession == "P75894":
        assert "not a purified RutE assay" in edge["description"]
        assert edge["predicate"] == "enables"
    if accession == "P0AFQ5":
        assert any(e["reference_id"] == "PMID:33839153" for e in edge["evidence"])
        assert any(e["reference_id"] == "PMID:23143235" for e in edge["evidence"])
        assert "not essential" in edge["description"] and edge["predicate"] == "enables"
    if accession == "P75898":
        assert "spontaneous NADH" in edge["description"]
        assert any(e["reference_id"] == "PMID:28661684" for e in edge["evidence"])
root = ET.parse(RAW / "metacyc-CPLX0-1962.xml").getroot()
complex_node = next(
    x
    for x in root.iter("Protein")
    if x.get("frameid") == "CPLX0-1962" and x.get("detail") == "full"
)
assert complex_node.findtext("component/coefficient") == "4"
assert complex_node.find("component/Protein").get("frameid") == "EG12345-MONOMER"
assert complex_node.findtext("common-name") == "3-hydroxy acid dehydrogenase"
subunit = ET.parse(RAW / "metacyc-EG12345-MONOMER.xml").getroot()
assert any(x.findtext("dblink-oid") == "P39831" for x in subunit.iter("dblink"))
spontaneous = next(
    x
    for x in ET.parse(RAW / "metacyc-RXN0-5222.xml").iter("Reaction")
    if x.get("frameid") == "RXN0-5222" and x.get("detail") == "full"
)
assert spontaneous.findtext("spontaneous") == "true"
assert "category" not in next(r for r in record["reactions"] if r["id"] == "RHEA:15650")
assert not any(
    e["object"] == "RHEA:15650" and e["predicate"] in ["enables", "catalyzes"]
    for e in record["mechanistic_edges"]
)
assert not any(p["id"] == "UniProtKB:P75895" for p in record["participants"])
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
for node in record["participants"] + record["taxa"]:
    if node["id"].startswith(("CHEBI:", "NCBITaxon:")):
        native = ontology("chebi" if node["id"].startswith("CHEBI:") else "ncbitaxon", node["id"])
        assert native["rdfs:label"] == node["label"] and native.get("owl:deprecated") not in [
            "true",
            "1",
        ]
for projected, edge in zip(projection["edge_evidence"], record["mechanistic_edges"], strict=True):
    assert projected == {
        "edge": edge["id"],
        **{k: edge[k] for k in ["subject", "predicate", "object", "evidence"]},
    }
result = {
    "started_at": START,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "status": "passed",
    "target": str(TARGET),
    "target_sha256": digest(TARGET),
    "replay_script_sha256": digest(Path(__file__)),
    "checks": [
        "native and closed schemas",
        "all raw source and reference hashes",
        "complete Rhea RDF family/sides replay",
        "33 chemical sides",
        "six formula/charge balances",
        "complete net including regenerated FMN",
        "six exact reviewed protein identities and reaction bridges",
        "native YdfG4mer identity",
        "RutC direct deaminase and trimer evidence attachment",
        "RutE inference tier preserved",
        "spontaneous carbamate category and absence of unsupported RutD catalyst",
        "six material dependencies",
        "all53 edge evidence projections",
        "canonical native chemical and taxon labels",
    ],
    "balances": balances,
    "net_stoichiometry": net,
    "raw_hashes": raw_hashes,
    "excluded_checks": (
        "Shared corpus gates, pages and independent scientific review "
        "belong to root/reviewer; not claimed here."
    ),
}
(RAW / "replay-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps({k: v for k, v in result.items() if k not in ["raw_hashes", "balances"]}, indent=2)
)
