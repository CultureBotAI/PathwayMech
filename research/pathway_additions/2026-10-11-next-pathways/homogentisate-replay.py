"""Replay the three-step strain U pathway against independently retained sources.

Run with the worktree Python from the repository root. Writes one result under
/private/tmp, without modifying maintained data, projections or reviews.
"""

import collections
import csv
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
RAW = Path("/private/tmp/pathwaymech-next-pathways-evidence/homogentisate")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-pathways"
TARGET = ROOT / "data/pathways/homogentisate-degradation.yaml"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RH = "http://rdf.rhea-db.org/"
START = datetime.datetime.now(datetime.UTC).isoformat()


def digest(path):
    hasher = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            hasher.update(block)
    return hasher.hexdigest()


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
assert record["id"] == "GO:1902000"
assert record["taxa"] == [{"id": "NCBITaxon:303", "label": "Pseudomonas putida"}]
assert len(record["reactions"]) == 3
assert len(record["participants"]) == 15
assert len(record["mechanistic_edges"]) == 24
assert sum(len(e["evidence"]) for e in record["mechanistic_edges"]) == 38
manifest = json.loads((DOSSIER / "homogentisate-source-manifest.json").read_text())
raw_hashes = {}
for row in manifest["sources"]:
    if "sha256" in row:
        actual = digest(row["file"])
        assert actual == row["sha256"], row["file"]
        raw_hashes[row["file"]] = actual
projection = json.loads((DOSSIER / "homogentisate-source-projection.json").read_text())
masters = {"15449", "14817", "10244"}
with (CACHE / "rhea-directions.tsv").open() as stream:
    directions = {
        row["RHEA_ID_MASTER"]: row
        for row in csv.DictReader(stream, delimiter="\t")
        if row["RHEA_ID_MASTER"] in masters
    }
assert len(directions) == 3
numbers = {value for row in directions.values() for value in row.values()}
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
nodes.update({uri: compounds[uri] for uri in needed})
assert {"directions": directions, "nodes": nodes} == projection["rhea"]
sides, chemicals, net = [], {}, collections.Counter()
for reaction in record["reactions"]:
    rid = reaction["id"].split(":")[1]
    master = next(m for m, row in directions.items() if row["RHEA_ID_LR"] == rid)
    assert RH + rid in nodes[RH + master]["directionalReaction"]
    assert reaction["direction"] == "left_to_right"
    assert reaction["label"] == nodes[RH + rid]["equation"][0]
    for side in ("substrates", "products"):
        su = nodes[RH + rid][side][0]
        for prop, values in nodes[su].items():
            if not re.fullmatch(r"contains\d+", prop):
                continue
            for participant in values:
                compound = nodes[participant]["compound"][0]
                chemical = "CHEBI:" + nodes[compound]["chebi"][0].rsplit("_", 1)[-1]
                chemicals[chemical] = ontology("chebi", chemical)
                assert (
                    chemicals[chemical]["chemrof:generalized_empirical_formula"]
                    == nodes[compound]["formula"][0]
                )
                assert str(chemicals[chemical]["chemrof:charge"]) == nodes[compound]["charge"][0]
                sides.append(
                    dict(
                        reaction=reaction["id"],
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
assert len(sides) == 11
expected = {
    (s["chemical"], "consumes", s["reaction"])
    if s["side"] == "substrates"
    else (s["reaction"], "produces", s["chemical"])
    for s in sides
}
actual = {
    (e["subject"], e["predicate"], e["object"])
    for e in record["mechanistic_edges"]
    if e["predicate"] in {"consumes", "produces"}
}
assert actual == expected
balances = {}
for reaction in record["reactions"]:
    atoms, charge = collections.Counter(), 0
    for row in (s for s in sides if s["reaction"] == reaction["id"]):
        multiplier = (1 if row["side"] == "products" else -1) * row["coefficient"]
        native = chemicals[row["chemical"]]
        for element, count in re.findall(
            r"([A-Z][a-z]?)(\d*)", native["chemrof:generalized_empirical_formula"]
        ):
            atoms[element] += multiplier * int(count or 1)
        charge += multiplier * int(native["chemrof:charge"])
    assert all(n == 0 for n in atoms.values()) and charge == 0
    balances[reaction["id"]] = {"atom_residuals": dict(atoms), "charge_residual": charge}
net = {key: value for key, value in net.items() if value}
assert net == {
    "CHEBI:16169": -1,
    "CHEBI:15379": -1,
    "CHEBI:15378": 2,
    "CHEBI:15377": -1,
    "CHEBI:13705": 1,
    "CHEBI:29806": 1,
}
proteins = json.loads((RAW / "uniprot-AY168855.json").read_text())["results"]
lookup = {x["primaryAccession"]: (i, x) for i, x in enumerate(proteins)}
source = (RAW / "AY168855.embl").read_text()
assert '/strain="U"' in source and '/db_xref="taxon:303"' in source
cds_sections = [s.split("\nFT   gene", 1)[0] for s in source.split("\nFT   CDS")[1:]]
for accession, gene, protein, rid in [
    ("Q6EMI9", "hmgA", "AAO12527.1", "15450"),
    ("Q6EMI7", "hmgC", "AAO12529.1", "14818"),
    ("Q6EMI8", "hmgB", "AAO12528.1", "10245"),
]:
    index, native = lookup[accession]
    assert native["organism"]["taxonId"] == 303
    section = next(s for s in cds_sections if f'/protein_id="{protein}"' in s)
    assert f'/gene="{gene}"' in section and accession in section
    translation = re.search(r'/translation="([^"]+)"', section)[1]
    assert re.sub(r"\s", "", re.sub(r"\nFT\s+", "", translation)) == native["sequence"]["value"]
    assert any(
        r["database"] == "EMBL" and r["id"] == "AY168855"
        for r in native["uniProtKBCrossReferences"]
    )
    assert {"type": "STRAIN", "value": "U"}.items() <= native["references"][0]["referenceComments"][
        0
    ].items()
    edge = next(
        e
        for e in record["mechanistic_edges"]
        if e["predicate"] == "enables" and e["subject"] == "UniProtKB:" + accession
    )
    assert edge["object"] == "RHEA:" + rid
    assert any(e["reference_id"] == "PMID:15262943" for e in edge["evidence"])
    assert any(
        e["reference_id"] == "RHEA:" + rid and "directionalReaction" in e["source_locator"]
        for e in edge["evidence"]
    )
    if accession != "Q6EMI9":
        assert native["entryType"] == "UniProtKB unreviewed (TrEMBL)"
        assert (
            "unreviewed" in edge["description"]
            and "not a purified-enzyme assay" in edge["description"]
        )
for edge in record["mechanistic_edges"]:
    if edge["predicate"] == "has_cofactor":
        _, native = lookup[edge["subject"].split(":")[1]]
        cofactors = [co for c in native["comments"] for co in c.get("cofactors", [])]
        assert any(co["cofactorCrossReference"]["id"] == edge["object"] for co in cofactors)
    if edge["predicate"] == "located_in":
        _, native = lookup[edge["subject"].split(":")[1]]
        assert any(
            c["database"] == "GO" and c["id"] == edge["object"]
            for c in native["uniProtKBCrossReferences"]
        )
        assert "Electronic" in edge["description"]
    assert edge["predicate"] != "catalyzes"
assert all(n["category"] != "complex" for n in record["participants"])
for projected, edge in zip(projection["edge_evidence"], record["mechanistic_edges"], strict=True):
    assert projected == {
        "edge": edge["id"],
        **{k: edge[k] for k in ("subject", "predicate", "object", "evidence")},
    }
for node in (
    [dict(id=record["id"], label=record["label"])] + record["taxa"] + record["participants"]
):
    prefix = node["id"].split(":")[0]
    if prefix in {"GO", "CHEBI", "NCBITaxon"}:
        native = ontology(
            {"GO": "go", "CHEBI": "chebi", "NCBITaxon": "ncbitaxon"}[prefix], node["id"]
        )
        assert native["rdfs:label"] == node["label"] and native.get("owl:deprecated") not in {
            "true",
            "1",
        }
assert (RAW / "PMC451635-europe-render.html").read_bytes().startswith(b"%PDF-")
result = dict(
    started_at=START,
    finished_at=datetime.datetime.now(datetime.UTC).isoformat(),
    status="passed",
    target=str(TARGET),
    target_sha256=digest(TARGET),
    replay_script_sha256=digest(Path(__file__)),
    checks=[
        "native schema",
        "closed LinkML schema",
        "all retained source body hashes",
        "fresh streaming full Rhea RDF and directional family replay",
        "all 11 chemical sides",
        "three atom and charge balances",
        "net reaction with 2 hydrons",
        "exact 3 strain U protein sequence translations and identity bridges",
        "functional enzyme edge and evidence attachment",
        "native cofactors and electronic locations",
        "canonical ontology node labels and obsoletion",
        "all 24 edge evidence projections",
    ],
    balances=balances,
    net_stoichiometry=net,
    raw_hashes=raw_hashes,
    excluded_checks=(
        "Whole-repository gates, pages, KGX and independent scientific review "
        "delegated to parent; not claimed here."
    ),
)
(RAW / "replay-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps({k: v for k, v in result.items() if k not in {"raw_hashes", "balances"}}, indent=2)
)
