"""Replay native seven-step scope, directional sides, state identities and balance.

Run from the worktree with its Python. Reads raw bodies in the recorded external
cache and writes only an external replay result; no maintained record edits.
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
RAW = Path("/private/tmp/pathwaymech-next-cohort-evidence/pyrimidine-ribo")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/pyrimidine-ribonucleosides-degradation.yaml"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RH = "http://rdf.rhea-db.org/"
PB = "PathBank:SMP0002038"


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def projection(element):
    fields = {}
    for child in element:
        fields.setdefault(child.tag.rsplit("}", 1)[-1], []).append(
            child.get(RDF + "resource") or (child.text or "").strip()
        )
    return fields


def ontology(db, identifier):
    with sqlite3.connect(f"file:{CACHE}/{db}.db?mode=ro", uri=True) as c:
        rows = c.execute(
            "select predicate,value,object from statements where subject=?", (identifier,)
        ).fetchall()
    return {
        p: v if v is not None else o
        for p, v, o in rows
        if p
        in {
            "rdfs:label",
            "owl:deprecated",
            "IAO:0100001",
            "chemrof:charge",
            "chemrof:generalized_empirical_formula",
        }
    }


record = yaml.safe_load(TARGET.read_text())
validate_record(record)
assert strict_errors([TARGET], ROOT) == []
assert record["id"] == PB and len(record["reactions"]) == 7
native = {}
for element in ET.parse(RAW / "PW002024.owl").getroot():
    key = element.get(RDF + "ID") or element.get(RDF + "about", "")
    native[key] = {"type": element.tag.rsplit("}", 1)[-1], **projection(element)}
pathway = native["http://identifiers.org/smpdb/SMP0002038"]
assert pathway["displayName"] == [record["label"]]
assert {k for k, v in native.items() if v["type"] == "BiochemicalReaction"} == {
    "Reactions/" + str(n) for n in range(5895, 5900)
}
assert {k for k, v in native.items() if v["type"] == "Transport"} == {
    "Transports/488",
    "Transports/489",
}
masters = {"27878", "27890", "16069", "24388", "18793", "29951", "29983"}
with (CACHE / "rhea-directions.tsv").open() as f:
    directions = {
        row["RHEA_ID_MASTER"]: row
        for row in csv.DictReader(f, delimiter="\t")
        if row["RHEA_ID_MASTER"] in masters
    }
assert len(directions) == 7
numbers = {v for row in directions.values() for v in row.values()}
subjects, compounds = {}, {}
with gzip.open(CACHE / "rhea.rdf.gz", "rb") as f:
    context = ET.iterparse(f, events=("start", "end"))
    _, root = next(context)
    for event, element in context:
        if event != "end" or element.tag != RDF + "Description":
            continue
        uri = element.get(RDF + "about", "")
        name = uri.rsplit("/", 1)[-1]
        chosen = name.split("_", 1)[0] in numbers or (
            name.startswith("Participant_") and name.split("_")[1] in numbers
        )
        destination = subjects if chosen else compounds if name.startswith("Compound_") else None
        if destination is not None:
            for key, values in projection(element).items():
                for value in values:
                    if value not in destination.setdefault(uri, {}).setdefault(key, []):
                        destination[uri][key].append(value)
        element.clear()
        root.clear()
needed = {v for fields in subjects.values() for vs in fields.values() for v in vs if v in compounds}
subjects.update({uri: compounds[uri] for uri in needed})
assert (
    digest(CACHE / "rhea.rdf.gz")
    == "8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf"
)
assert subjects == json.loads((RAW / "rhea-projection.json").read_text())["nodes"]
sides, chemicals = [], {}
state_map = {}
for reaction in record["reactions"]:
    rid = reaction["id"].split(":")[1]
    master = next(m for m, row in directions.items() if rid in row.values())
    fields = subjects[RH + rid]
    assert RH + rid in subjects[RH + master]["directionalReaction"]
    expected_direction = "right_to_left" if rid in {"29953", "29985"} else "left_to_right"
    assert reaction["direction"] == expected_direction
    assert reaction["label"] == fields["equation"][0]
    for side in ("substrates", "products"):
        su = fields[side][0]
        for prop, participants in subjects[su].items():
            if not re.fullmatch(r"contains\d+", prop):
                continue
            for participant in participants:
                compound = subjects[participant]["compound"][0]
                chemical = "CHEBI:" + subjects[compound]["chebi"][0].rsplit("_", 1)[-1]
                chemicals[chemical] = ontology("chebi", chemical)
                target = chemical
                if rid in {"29953", "29985"}:
                    suffix = "Periplasmic_Space" if side == "substrates" else "Cytosol"
                    location = "Out" if side == "substrates" else "In"
                    assert subjects[participant]["location"] == [RH + location]
                    key = {
                        "CHEBI:16704": "PW_C000202",
                        "CHEBI:17562": "PW_C000061",
                        "CHEBI:15378": "PW_C040034",
                    }[chemical]
                    obj = "Compound/" + key + "_" + suffix
                    target = PB + "/" + obj
                    state_map[target] = chemical
                    transport = "Transports/488" if rid == "29953" else "Transports/489"
                    assert (
                        "#" + obj in native[transport]["left" if side == "substrates" else "right"]
                    )
                    assert native[obj]["entityReference"] == ["#CompoundReference/" + key]
                    assert native[obj]["cellularLocation"] == ["#CellularLocation/" + suffix]
                sides.append(
                    dict(
                        reaction=reaction["id"],
                        side=side,
                        chemical=chemical,
                        node=target,
                        coefficient=int(prop[8:]),
                        side_uri=su,
                        participant_uri=participant,
                        compound_uri=compound,
                    )
                )
expected = {
    (x["node"], "consumes", x["reaction"])
    if x["side"] == "substrates"
    else (x["reaction"], "produces", x["node"])
    for x in sides
}
actual = {
    (e["subject"], e["predicate"], e["object"])
    for e in record["mechanistic_edges"]
    if e["predicate"] in {"consumes", "produces"}
}
assert actual == expected and len(sides) == 27
balances = []
for reaction in record["reactions"]:
    delta = collections.Counter()
    charge = 0
    for side in [s for s in sides if s["reaction"] == reaction["id"]]:
        chemical = chemicals[side["chemical"]]
        formula = chemical["chemrof:generalized_empirical_formula"]
        atoms = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
        assert "".join(a + n for a, n in atoms) == formula
        coefficient = side["coefficient"] * (-1 if side["side"] == "substrates" else 1)
        for atom, count in atoms:
            delta[atom] += coefficient * int(count or 1)
        charge += coefficient * int(chemical["chemrof:charge"])
    assert all(n == 0 for n in delta.values()) and charge == 0
    balances.append(dict(reaction=reaction["id"], atom_delta=dict(delta), charge_delta=charge))
# Direct native controller/protein identity checks, including the two physical complexes.
for nr, cat, protein, uid, complex_id in [
    ("5895", "5858", "5948", "P08331", None),
    ("5896", "5859", "5948", "P08331", None),
    ("5897", "5860", "6175", "P0ABF6", "3973"),
    ("5898", "5861", "10357", "P12758", "3974"),
    ("5899", "5862", "6000", "P0A6K6", None),
    ("488", "420", "7058", "P0AFF4", None),
    ("489", "421", "7058", "P0AFF4", None),
]:
    transport = nr in {"488", "489"}
    control = native[("TransportCatalysis/" if transport else "ReactionCatalysis/") + cat]
    assert control["controlled"] == [("#Transports/" if transport else "#Reactions/") + nr]
    controller = ("#ProteinComplex/" + complex_id) if complex_id else "#Protein/" + protein
    assert control["controller"] == [controller]
    assert "#Reference/UniProt_" + uid in native["ProteinReference/" + protein]["xref"]
for obj, protein, count in [("3973", "6175", 2), ("3974", "10357", 6)]:
    assert native["ProteinComplex/" + obj]["component"] == ["#Protein/" + protein]
    st = native["Protein/" + protein + "/Stoichiometry/" + str(count) + ".0"]
    assert float(st["stoichiometricCoefficient"][0]) == count
identifiers = {}
for node in record["participants"] + record["taxa"]:
    identifier = node["id"]
    prefix = identifier.split(":")[0]
    if prefix in {"CHEBI", "GO", "NCBITaxon"}:
        fields = ontology(
            {"CHEBI": "chebi", "GO": "go", "NCBITaxon": "ncbitaxon"}[prefix], identifier
        )
        assert fields.get("owl:deprecated") != "true"
        assert fields["rdfs:label"] == node["label"]
        identifiers[identifier] = fields
    elif prefix == "UniProtKB":
        uid = identifier.split(":")[1]
        up = json.loads((RAW / f"uniprot-{uid}.json").read_text())
        assert up["primaryAccession"] == uid and up["organism"]["taxonId"] == 83333
        assert node["label"] == up["proteinDescription"]["recommendedName"]["fullName"]["value"]
        identifiers[identifier] = {
            "taxon": 83333,
            "label": node["label"],
            "entryAudit": up["entryAudit"],
        }
    elif prefix == "PathBank":
        assert identifier.removeprefix(PB + "/") in native
        identifiers[identifier] = native[identifier.removeprefix(PB + "/")]
    else:
        identifiers[identifier] = {
            "label": node["label"],
            "grounding": ("Native complex XML and root HTML authority; membership replay above"),
        }
assert ontology("go", "GO:0005620")["IAO:0100001"] == "GO:0042597"
assert ontology("go", "GO:0005620")["owl:deprecated"] == "true"
for edge in record["mechanistic_edges"]:
    if edge["predicate"] in {"enables", "catalyzes"}:
        assert any("rh:directionalReaction" in ev["source_locator"] for ev in edge["evidence"])
# Source-specific regression: transport papers must remain on NupG transport edges.
for paper in {"PMID:15513740", "PMID:33640454"}:
    attachments = {
        (edge["subject"], edge["predicate"], edge["object"])
        for edge in record["mechanistic_edges"]
        if any(ev["reference_id"] == paper for ev in edge["evidence"])
    }
    assert attachments == {
        ("UniProtKB:P0AFF4", "enables", "RHEA:29953"),
        ("UniProtKB:P0AFF4", "enables", "RHEA:29985"),
    }, (paper, attachments)
result = dict(
    status="pass",
    finished_at=datetime.datetime.now(datetime.UTC).isoformat(),
    target=str(TARGET.relative_to(ROOT)),
    target_sha256=digest(TARGET),
    record_id=record["id"],
    participants=len(record["participants"]),
    reactions=7,
    edges=len(record["mechanistic_edges"]),
    evidence=sum(len(e["evidence"]) for e in record["mechanistic_edges"]),
    chemical_sides=sides,
    balances=balances,
    identifiers=identifiers,
    native_scope={"biochemical_reactions": 5, "transports": 2, "complete": True},
    checks=[
        "native schema",
        "closed schema",
        "full native boundary",
        "Rhea RDF family and all sides",
        "27 chemical-side and transport-state assertions",
        "7 atom/charge balances",
        "native enzyme and complex membership",
        "all named-node identity projection",
        "exact Rhea family bridge locators",
        "NupG primary-paper attachment regression for issue335",
        "GO obsolete-term replacement",
    ],
    not_run=["full corpus gates, rendering and saved scientific review are root/delegated work"],
)
(RAW / "replay-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {k: result[k] for k in ["status", "target_sha256", "reactions", "edges", "evidence"]}
    )
)
