"""Replay exact methylglyoxal I sources; writes only external audit scratch.

Run from the worktree root with its Python. Raw source bodies listed in the
manifest and the pinned authority cache must be present. Full corpus checks
and shared authority snapshot regeneration belong to the integration workflow.
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
RAW = Path("/private/tmp/pathwaymech-next-cohort-evidence/methylglyoxal-i")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-10-next-cohort"
TARGET = ROOT / "data/pathways/methylglyoxal-degradation-i.yaml"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RH = "http://rdf.rhea-db.org/"


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def source_fields(element):
    result = {}
    for child in element:
        result.setdefault(child.tag.rsplit("}", 1)[-1], []).append(
            child.get(RDF + "resource") or (child.text or "").strip()
        )
    return result


def ontology(db, identifier):
    with sqlite3.connect(f"file:{CACHE / (db + '.db')}?mode=ro", uri=True) as conn:
        rows = conn.execute(
            "select predicate,value,object from statements where subject=?", (identifier,)
        ).fetchall()
    result = {}
    for predicate, value, obj in rows:
        if predicate in {
            "rdfs:label",
            "IAO:0000115",
            "chemrof:charge",
            "owl:deprecated",
            "chemrof:generalized_empirical_formula",
            "IAO:0100001",
        }:
            result.setdefault(predicate, []).append(value if value is not None else obj)
    return result


record = yaml.safe_load(TARGET.read_text())
validate_record(record)
assert strict_errors([TARGET], ROOT) == []
manifest = json.loads((DOSSIER / "methylglyoxal-i-source-manifest.json").read_text())
source_checks = []
for source in manifest["artifacts"]:
    if "sha256" not in source:
        continue
    path = Path(source["file"])
    if not path.is_absolute():
        path = RAW / path
    assert digest(path) == source["sha256"], path
    source_checks.append({"path": str(path), "sha256": digest(path)})

projection = json.loads((DOSSIER / "methylglyoxal-i-source-projection.json").read_text())
masters = {"19069", "25245", "51468"}
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
        selected = name.split("_", 1)[0] in nums or (
            name.startswith("Participant_") and name.split("_")[1] in nums
        )
        destination = subjects if selected else compounds if name.startswith("Compound_") else None
        if destination is not None:
            for key, values in source_fields(element).items():
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
assert subjects == projection["chemistry"]["nodes"]
assert directions == projection["chemistry"]["directions"]
sides = []
for master, direction in directions.items():
    reverse = master == "19069"
    rid = direction["RHEA_ID_RL" if reverse else "RHEA_ID_LR"]
    assert RH + rid in subjects[RH + master]["directionalReaction"]
    rnode = next(x for x in record["reactions"] if x["id"] == "RHEA:" + rid)
    assert rnode["label"] == subjects[RH + rid]["equation"][0]
    assert rnode["direction"] == ("right_to_left" if reverse else "left_to_right")
    for side in ["substrates", "products"]:
        uri = subjects[RH + rid][side][0]
        for key, values in subjects[uri].items():
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
                    }
                )
expected_edges = collections.Counter()
for side in sides:
    if side["side"] == "substrates":
        expected_edges[(side["chemical"], "consumes", side["reaction"])] += 1
    else:
        expected_edges[(side["reaction"], "produces", side["chemical"])] += 1
actual_edges = collections.Counter(
    (edge["subject"], edge["predicate"], edge["object"])
    for edge in record["mechanistic_edges"]
    if edge["predicate"] in {"consumes", "produces"}
)
assert expected_edges == actual_edges and len(sides) == 12
chemicals = {}
for node in record["participants"]:
    identifier = node["id"]
    if identifier.startswith("CHEBI:"):
        fields = ontology("chebi", identifier)
        assert fields["rdfs:label"] == [node["label"]]
        assert fields.get("owl:deprecated") != ["true"]
        chemicals[identifier] = fields
    elif identifier.startswith("GO:"):
        assert ontology("go", identifier)["rdfs:label"] == [node["label"]]
    elif identifier.startswith("UniProtKB:"):
        source = json.loads((RAW / f"uniprot-{identifier.split(':')[1]}.json").read_text())
        assert source["proteinDescription"]["recommendedName"]["fullName"]["value"] == node["label"]
        assert source["organism"]["taxonId"] == 83333
assert ontology("ncbitaxon", "NCBITaxon:83333")["rdfs:label"] == [record["taxa"][0]["label"]]
assert ontology("go", "GO:0019243")["owl:deprecated"] == ["true"]
balances = []
net = collections.Counter()
for rid in ["RHEA:19071", "RHEA:25246", "RHEA:51469"]:
    atoms = collections.Counter()
    charge = 0
    for side in [x for x in sides if x["reaction"] == rid]:
        sign = -1 if side["side"] == "substrates" else 1
        coefficient = sign * side["coefficient"]
        fields = chemicals[side["chemical"]]
        formula = fields["chemrof:generalized_empirical_formula"][0]
        parts = re.findall(r"([A-Z][a-z]?)([0-9]*)", formula)
        assert "".join(element + count for element, count in parts) == formula
        for element, count in parts:
            atoms[element] += coefficient * int(count or 1)
        charge += coefficient * int(fields["chemrof:charge"][0])
        net[side["chemical"]] += coefficient
    assert all(v == 0 for v in atoms.values()) and charge == 0
    balances.append(
        {"reaction": rid, "element_or_R_group_delta": dict(atoms), "charge_delta": charge}
    )
assert net["CHEBI:57925"] == net["CHEBI:57474"] == net["CHEBI:16004"] == 0

native = ET.parse(RAW / "PW002113.owl").getroot()
objects = {x.get(RDF + "ID", x.get(RDF + "about")): x for x in native}
pathway = source_fields(objects["http://identifiers.org/smpdb/SMP0002125"])
assert {x for x in pathway["pathwayComponent"] if x.startswith("#Reactions/")} == {
    "#Reactions/6149",
    "#Reactions/6150",
    "#Reactions/6151",
}
assert source_fields(objects["ProteinComplex/4108"])["component"] == ["#Protein/6205"]
assert source_fields(objects["Protein/6205/Stoichiometry/2.0"])["stoichiometricCoefficient"] == [
    "2.0"
]
for reaction, catalysis, controller in [
    ("6149", "6107", "ProteinComplex/4108"),
    ("6150", "6108", "Protein/6206"),
    ("6151", "6109", "Protein/5893"),
]:
    obj = source_fields(objects["ReactionCatalysis/" + catalysis])
    assert obj["controller"] == ["#" + controller]
    assert obj["controlled"] == ["#Reactions/" + reaction]
metacyc = {}
for identifier in [
    "PWY-5386",
    "GLYOXI-CPLX",
    "GLYOXI-MONOMER",
    "GLYOXI-RXN",
    "GLYOXII-RXN",
    "DLACTDEHYDROGFAD-RXN",
]:
    root = ET.parse(RAW / f"metacyc-{identifier}.xml").getroot()
    assert root.get("ptools-version") == "22.5"
    metacyc[identifier] = next(x for x in root if x.get("frameid") == identifier)
assert {x.get("frameid") for x in metacyc["PWY-5386"].findall("reaction-list/Reaction")} == {
    "GLYOXI-RXN",
    "GLYOXII-RXN",
    "DLACTDEHYDROGFAD-RXN",
}
assert metacyc["GLYOXI-CPLX"].findtext("component/coefficient") == "2"
assert metacyc["GLYOXI-MONOMER"].findtext("dblink[dblink-db='UNIPROT']/dblink-oid") == "P0AC81"
for identifier, master in [("GLYOXI-RXN", "19072"), ("GLYOXII-RXN", "25245")]:
    assert metacyc[identifier].findtext("dblink[dblink-db='RHEA']/dblink-oid") == master
assert metacyc["DLACTDEHYDROGFAD-RXN"].find("dblink[dblink-db='RHEA']") is None

quotes = []
for edge in record["mechanistic_edges"]:
    for evidence in edge["evidence"]:
        if "quote" not in evidence:
            continue
        pmid = evidence["reference_id"].split(":")[1]
        if pmid == "37850128":
            article = ET.parse(RAW / "primary-PMC10521649.xml").getroot()
            text = " ".join(article.itertext())
        else:
            text = json.loads((RAW / f"primary-{pmid}.json").read_text())["resultList"]["result"][
                0
            ]["abstractText"]
        assert evidence["quote"] in text, (edge["id"], evidence["quote"])
        quotes.append({"edge": edge["id"], "reference": evidence["reference_id"], "verbatim": True})
receipt = {
    "completed_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "status": "pass",
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "command": (
        ".venv/bin/python research/pathway_additions/"
        "2026-10-10-next-cohort/methylglyoxal-i-replay.py"
    ),
    "script_sha256": digest(Path(__file__)),
    "source_checks": source_checks,
    "counts": {
        "participants": len(record["participants"]),
        "reactions": len(record["reactions"]),
        "edges": len(record["mechanistic_edges"]),
        "evidence": sum(len(x["evidence"]) for x in record["mechanistic_edges"]),
        "rhea_sides": len(sides),
    },
    "native_membership_and_controllers": (
        "all three native steps checked; exact homodimer coefficient checked"
    ),
    "checks": [
        "native schema",
        "closed schema",
        "all reference-body source digests",
        "full Rhea RDF re-extraction",
        "directions and twelve exact sides",
        "chemical/protein/GO/taxon labels",
        "native membership/catalysts",
        "explicit native Rhea bridges versus absent Dld bridge",
        "all quoted excerpts verbatim",
    ],
    "balances": balances,
    "net": {k: v for k, v in net.items() if v},
    "quotes": quotes,
    "limits": [
        "R groups cancel symbolically for corresponding quinone/quinol classes; "
        "no UQ6-specific claim",
        "large GO/ChEBI/taxon cache digests use root's independently verified source provenance; "
        "no whole-file memory reads",
        "this is the author replay, not independent scientific review or full integration gates",
    ],
}
(RAW / "replay-result.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(
    json.dumps(
        {
            "status": receipt["status"],
            "sha256": receipt["target_sha256"],
            "counts": receipt["counts"],
        }
    )
)
