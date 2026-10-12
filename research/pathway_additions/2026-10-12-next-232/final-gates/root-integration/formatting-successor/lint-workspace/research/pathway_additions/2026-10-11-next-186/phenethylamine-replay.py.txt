"""Replay retained phenylethylamine source identities, chemistry and graph sides.

Run from the repository root. Original source bodies remain in the external
paths recorded by the source manifest; this does not fetch or infer missing data.
Scientific interpretation is assessed separately in the saved record review.
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

from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-186"
RAW = Path("/private/tmp/pathwaymech-next-186-evidence/phenethylamine")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/phenylethylamine-degradation-i.yaml"
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
        node
        for node in ET.parse(RAW / f"native-{frame}.xml").iter(kind)
        if node.get("frameid") == frame and node.get("detail") == "full"
    )


record = yaml.safe_load(TARGET.read_text())
validate_record(record)
assert strict_errors([TARGET], ROOT) == []
manifest = json.loads((DOSSIER / "phenethylamine-source-manifest.json").read_text())
projection = json.loads((DOSSIER / "phenethylamine-source-projection.json").read_text())
assert manifest["record_sha256"] == digest(TARGET)
hashes = {row["path"]: digest(row["path"]) for row in manifest["sources"]}
for row in manifest["sources"]:
    assert hashes[row["path"]] == row["sha256"], row["path"]
for reference in record["references"]:
    assert digest(manifest["reference_artifacts"][reference["id"]]) == reference["source_sha256"]

pathway = native("2PHENDEG-PWY", "Pathway")
members = {node.get("frameid") for node in pathway.findall("reaction-list/Reaction")}
assert members == {"AMINEPHEN-RXN", "PHENDEHYD-RXN"}
assert pathway.find("reaction-ordering/Reaction").get("frameid") == "PHENDEHYD-RXN"
assert (
    pathway.find("reaction-ordering/predecessor-reactions/Reaction").get("frameid")
    == "AMINEPHEN-RXN"
)
complex_node = native("AMINEOXID-CPLX", "Protein")
component = next(
    x
    for x in complex_node.findall("component")
    if x.find("Protein").get("frameid") == "AMINEOXID-MONOMER"
)
assert component.findtext("coefficient") == "2"
for accession in ("P46883", "P80668", "Q47129"):
    entry = json.loads((RAW / f"uniprot-{accession}.json").read_text())
    assert entry["primaryAccession"] == accession and entry["organism"]["taxonId"] == 83333

expected = projection["rhea"]["nodes"]
actual = {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
    context = ET.iterparse(stream, events=("start", "end"))
    _, root = next(context)
    for event, element in context:
        if event != "end" or element.tag != RDF + "Description":
            continue
        uri = element.get(RDF + "about", "")
        if uri in expected:
            for child in element:
                key = child.tag.rsplit("}", 1)[-1]
                value = child.get(RDF + "resource") or (child.text or "").strip()
                values = actual.setdefault(uri, {}).setdefault(key, [])
                if value not in values:
                    values.append(value)
        element.clear()
        root.clear()
assert actual == expected
directions = {}
for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
    cells = line.split("\t")
    if cells[0] in {"25265", "21392"}:
        directions[cells[0]] = dict(
            zip(("master", "left_to_right", "right_to_left", "bidirectional"), cells, strict=True)
        )
assert directions == projection["rhea"]["directions"]

balances = {}
sides = []
with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as connection:
    for reaction in record["reactions"]:
        reaction_id = reaction["id"]
        native_reaction = actual[RH + reaction_id.split(":")[1]]
        assert reaction["label"] == native_reaction["equation"][0]
        assert reaction["direction"] == "left_to_right"
        balance = collections.Counter()
        charge = 0
        for side, sign, predicate in (("substrates", -1, "consumes"), ("products", 1, "produces")):
            side_uri = native_reaction[side][0]
            for property_name, participants in actual[side_uri].items():
                if not re.fullmatch(r"contains\d+", property_name):
                    continue
                coefficient = int(property_name[8:])
                for participant in participants:
                    compound = actual[actual[participant]["compound"][0]]
                    chemical = "CHEBI:" + compound["chebi"][0].rsplit("_", 1)[-1]
                    values = dict(
                        connection.execute(
                            "select predicate,value from statements where subject=? "
                            "and predicate in ('chemrof:charge',"
                            "'chemrof:generalized_empirical_formula')",
                            (chemical,),
                        )
                    )
                    assert values["chemrof:generalized_empirical_formula"] == compound["formula"][0]
                    assert str(values["chemrof:charge"]) == compound["charge"][0]
                    formula = compound["formula"][0]
                    terms = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
                    assert "".join(element + count for element, count in terms) == formula
                    for element, count in terms:
                        balance[element] += sign * coefficient * int(count or "1")
                    charge += sign * coefficient * int(compound["charge"][0])
                    triple = (
                        (chemical, predicate, reaction_id)
                        if sign == -1
                        else (reaction_id, predicate, chemical)
                    )
                    assert (
                        sum(
                            (edge["subject"], edge["predicate"], edge["object"]) == triple
                            for edge in record["mechanistic_edges"]
                        )
                        == 1
                    )
                    sides.append(
                        {
                            "reaction": reaction_id,
                            "side": side,
                            "chemical": chemical,
                            "coefficient": coefficient,
                        }
                    )
        assert all(value == 0 for value in balance.values()) and charge == 0
        balances[reaction_id] = {"atom_residuals": dict(balance), "charge_residual": charge}
assert len(sides) == len(projection["chemical_sides"])
assert sum(
    edge["predicate"] in {"consumes", "produces"} for edge in record["mechanistic_edges"]
) == len(sides)
report = {
    "status": "passed",
    "completed_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target_sha256": digest(TARGET),
    "script_sha256": digest(Path(__file__)),
    "retained_source_hashes": hashes,
    "native_members": sorted(members),
    "directed_rhea": directions,
    "chemical_sides": sides,
    "balances": balances,
    "limits": [
        "This deterministic source replay does not replace independent scientific assessment.",
        "Raw sources are external retained inputs, not redistributed in the repository.",
    ],
}
(DOSSIER / "phenethylamine-validation.json").write_text(json.dumps(report, indent=2) + "\n")
print(
    json.dumps(
        {
            "status": "passed",
            "chemical_sides": len(sides),
            "reactions": len(balances),
            "sources_rehashed": len(hashes),
        }
    )
)
