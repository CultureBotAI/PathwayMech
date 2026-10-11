"""Replay PWY-7181 source identities, exact reaction sides and balance.

Run with the worktree Python from its root. Writes only external evidence scratch.
The native and primary bodies listed in pyrimidine-source-manifest.json are required.
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
RAW = Path("/private/tmp/pathwaymech-next-routes-evidence/pyrimidine")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/pyrimidine-deoxyribonucleosides-degradation.yaml"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RH = "http://rdf.rhea-db.org/"


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def project(element):
    result = {}
    for child in element:
        result.setdefault(child.tag.rsplit("}", 1)[-1], []).append(
            child.get(RDF + "resource") or (child.text or "").strip()
        )
    return result


def authority_fields(db, identifier):
    with sqlite3.connect(f"file:{CACHE / (db + '.db')}?mode=ro", uri=True) as conn:
        rows = conn.execute(
            "select predicate,value,object from statements where subject=?", (identifier,)
        ).fetchall()
    fields = {}
    for predicate, value, obj in rows:
        if predicate in {
            "rdfs:label",
            "IAO:0000115",
            "chemrof:charge",
            "chemrof:generalized_empirical_formula",
            "owl:deprecated",
            "rdfs:subClassOf",
        }:
            fields.setdefault(predicate, []).append(value if value is not None else obj)
    assert fields.get("owl:deprecated") != ["true"]
    return fields


def counts(formula):
    parts = re.findall(r"([A-Z][a-z]?)([0-9]*)", formula)
    assert "".join(element + count for element, count in parts) == formula
    return {element: int(count or 1) for element, count in parts}


record = yaml.safe_load(TARGET.read_text())
validate_record(record)
assert strict_errors([TARGET], ROOT) == []
masters = {"13433", "22824", "16037"}
with (CACHE / "rhea-directions.tsv").open() as handle:
    directions = {
        row["RHEA_ID_MASTER"]: row
        for row in csv.DictReader(handle, delimiter="\t")
        if row["RHEA_ID_MASTER"] in masters
    }
nums = {number for row in directions.values() for number in row.values()}
subjects = {}
compounds = {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as handle:
    context = ET.iterparse(handle, events=("start", "end"))
    _, rdf_root = next(context)
    for event, element in context:
        if event != "end" or element.tag != RDF + "Description":
            continue
        uri = element.get(RDF + "about", "")
        name = uri.rsplit("/", 1)[-1]
        selected = (
            name.split("_", 1)[0] in nums
            or name.startswith("Participant_")
            and name.split("_")[1] in nums
        )
        destination = subjects if selected else compounds if name.startswith("Compound_") else None
        if destination is not None:
            for key, values in project(element).items():
                for value in values:
                    if value not in destination.setdefault(uri, {}).setdefault(key, []):
                        destination[uri][key].append(value)
        element.clear()
        rdf_root.clear()
needed = {
    value
    for fields in subjects.values()
    for values in fields.values()
    for value in values
    if value in compounds
}
subjects.update({uri: compounds[uri] for uri in needed})
assert (
    digest(CACHE / "rhea.rdf.gz")
    == "8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf"
)
prior = json.loads((RAW / "rhea-projection.json").read_text())["nodes"]
assert subjects == prior
sides = []
for master, row in directions.items():
    rid = row["RHEA_ID_LR"]
    node = subjects[RH + rid]
    assert subjects[RH + master]["directionalReaction"] == [RH + rid, RH + row["RHEA_ID_RL"]]
    assert subjects[RH + master]["bidirectionalReaction"] == [RH + row["RHEA_ID_BI"]]
    assert node["substrates"] == [RH + master + "_L"]
    assert node["products"] == [RH + master + "_R"]
    target_reaction = next(item for item in record["reactions"] if item["id"] == "RHEA:" + rid)
    assert target_reaction["direction"] == "left_to_right"
    assert target_reaction["label"] == node["equation"][0]
    for side in ["substrates", "products"]:
        side_uri = node[side][0]
        for key, values in subjects[side_uri].items():
            if not re.fullmatch(r"contains\d+", key):
                continue
            for participant in values:
                compound = subjects[participant]["compound"][0]
                chemical = "CHEBI:" + subjects[compound]["chebi"][0].rsplit("_", 1)[-1]
                sides.append(
                    {
                        "reaction": "RHEA:" + rid,
                        "side": side,
                        "coefficient": int(key[8:]),
                        "chemical": chemical,
                        "side_uri": side_uri,
                        "participant_uri": participant,
                        "compound_uri": compound,
                    }
                )
chemicals = {
    item["id"]: authority_fields("chebi", item["id"])
    for item in record["participants"]
    if item["id"].startswith("CHEBI:")
}
for item in record["participants"]:
    if item["id"] in chemicals:
        assert chemicals[item["id"]]["rdfs:label"] == [item["label"]]
balances = []
for rid in ["RHEA:13434", "RHEA:22825", "RHEA:16038"]:
    delta = collections.Counter()
    charge = 0
    for side in [row for row in sides if row["reaction"] == rid]:
        chemical = chemicals[side["chemical"]]
        coefficient = side["coefficient"] * (-1 if side["side"] == "substrates" else 1)
        for element, count in counts(chemical["chemrof:generalized_empirical_formula"][0]).items():
            delta[element] += coefficient * count
        charge += coefficient * int(chemical["chemrof:charge"][0])
    assert all(value == 0 for value in delta.values()) and charge == 0
    balances.append({"reaction": rid, "element_delta": dict(delta), "charge_delta": charge})
branch_nets = {}
for branch, reactions in {
    "deoxycytidine": {"RHEA:13434", "RHEA:22825"},
    "thymidine": {"RHEA:16038"},
}.items():
    net = collections.Counter()
    for row in sides:
        if row["reaction"] in reactions:
            sign = -1 if row["side"] == "substrates" else 1
            net[row["chemical"]] += sign * row["coefficient"]
    branch_nets[branch] = {chemical: value for chemical, value in net.items() if value}
assert "CHEBI:16450" not in branch_nets["deoxycytidine"]
assert branch_nets["deoxycytidine"] == {
    "CHEBI:15698": -1,
    "CHEBI:15377": -1,
    "CHEBI:15378": -1,
    "CHEBI:43474": -1,
    "CHEBI:28938": 1,
    "CHEBI:57259": 1,
    "CHEBI:17568": 1,
}
expected_edges = set()
for row in sides:
    if row["side"] == "substrates":
        expected_edges.add((row["chemical"], "consumes", row["reaction"]))
    else:
        expected_edges.add((row["reaction"], "produces", row["chemical"]))
actual_edges = {
    (edge["subject"], edge["predicate"], edge["object"])
    for edge in record["mechanistic_edges"]
    if edge["predicate"] in {"consumes", "produces"}
}
assert actual_edges == expected_edges and len(actual_edges) == 13
native = {}
for path in sorted(RAW.glob("metacyc-*.xml")):
    tree = ET.parse(path).getroot()
    node = list(tree)[1]
    fields = {
        key: [ET.tostring(child, encoding="unicode") for child in node.findall(key)]
        for key in [
            "common-name",
            "reaction-list",
            "reaction-ordering",
            "reaction-layout",
            "reaction-direction",
            "left",
            "right",
            "dblink",
            "catalyzes",
            "component",
            "location",
            "component-of",
            "pathway-link",
        ]
    }
    native[node.get("frameid")] = {
        "path": str(path),
        "sha256": digest(path),
        "version": tree.find("metadata/PGDB").get("version"),
        "fields": fields,
    }
pathway = ET.parse(RAW / "metacyc-PWY-7181.xml").getroot().find("Pathway")
assert {node.get("frameid") for node in pathway.findall("reaction-list/Reaction")} == {
    "CYTIDEAM-RXN",
    "URA-PHOSPH-RXN",
    "THYM-PHOSPH-RXN",
}
assert pathway.find("species/Organism").get("frameid") == "TAX-511145"
for complex_id, monomer, accession in [
    ("CYTIDEAM-CPLX", "CYTIDEAM-MONOMER", "P0ABF6"),
    ("DEOA-CPLX", "DEOA-MONOMER", "P07650"),
]:
    complex_node = ET.parse(RAW / f"metacyc-{complex_id}.xml").getroot().find("Protein")
    monomer_node = ET.parse(RAW / f"metacyc-{monomer}.xml").getroot().find("Protein")
    assert complex_node.find("component/Protein").get("frameid") == monomer
    assert complex_node.findtext("component/coefficient") == "2"
    assert monomer_node.find("location/cco").get("frameid") == "CCO-CYTOSOL"
    assert any(
        node.findtext("dblink-db") == "UNIPROT"
        and node.findtext("dblink-oid") == accession
        and node.findtext("dblink-relationship") == "unification"
        for node in monomer_node.findall("dblink")
    )
protein = {}
for accession in ["P0ABF6", "P07650"]:
    source = json.loads((RAW / f"{accession}.json").read_text())
    protein[accession] = {
        key: source[key]
        for key in [
            "primaryAccession",
            "organism",
            "genes",
            "entryAudit",
            "proteinDescription",
            "comments",
        ]
    }
    assert source["organism"]["taxonId"] == 83333
    assert any(
        item["id"] == "UniProtKB:" + accession
        and item["label"] == source["proteinDescription"]["recommendedName"]["fullName"]["value"]
        for item in record["participants"]
    )
result = {
    "checked_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "native_schema": "pass",
    "closed_schema": "pass",
    "rhea": {"directions": directions, "subjects": subjects, "sides": sides, "balances": balances},
    "branch_nets": branch_nets,
    "chemical_authority_fields": chemicals,
    "native": native,
    "protein": protein,
    "ontology": {
        "GO:0005829": authority_fields("go", "GO:0005829"),
        "GO:0046127": authority_fields("go", "GO:0046127"),
        "NCBITaxon:511145": authority_fields("ncbitaxon", "NCBITaxon:511145"),
    },
    "counts": {
        "nodes": 21,
        "edges": len(record["mechanistic_edges"]),
        "evidence": sum(len(edge["evidence"]) for edge in record["mechanistic_edges"]),
        "chemical_sides": len(sides),
    },
    "passed": True,
}
(RAW / "pyrimidine-replay-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({key: result[key] for key in ["target_sha256", "counts", "passed"]}))
