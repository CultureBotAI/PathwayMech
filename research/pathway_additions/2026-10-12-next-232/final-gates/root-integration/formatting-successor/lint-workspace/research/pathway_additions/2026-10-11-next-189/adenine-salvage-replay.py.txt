"""Replay complete adenine and adenosine salvage III from original sources."""

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

from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, kgx_edges, kgx_nodes, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-189-evidence/adenine-salvage")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-189"
TARGET = ROOT / "data/pathways/adenine-and-adenosine-salvage-iii.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
SELECTED = {
    "27642": ("27644", "right_to_left", "ADENPHOSPHOR-RXN", "PWY-6609"),
    "24408": ("24409", "left_to_right", "ADENODEAMIN-RXN", "PWY-6609"),
    "27646": ("27647", "left_to_right", "INOPHOSPHOR-RXN", "PWY-6609"),
    "17973": ("17975", "right_to_left", "HYPOXANPRIBOSYLTRAN-RXN", "PWY-6609"),
}
STARTED = datetime.datetime.now(datetime.UTC).isoformat()


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            result.update(block)
    return result.hexdigest()


def native(identifier):
    return next(x for x in ET.parse(RAW / f"{identifier}.xml").getroot() if x.tag != "metadata")


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
            "chemrof:charge",
            "chemrof:generalized_empirical_formula",
            "owl:deprecated",
        }
    }


def atoms(formula):
    fields = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
    assert "".join(a + n for a, n in fields) == formula
    return {a: int(n or 1) for a, n in fields}


record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert strict_errors([TARGET], ROOT) == []
assert record["id"] == "MetaCyc:PWY-6609"
assert len(record["reactions"]) == 4 and len(record["participants"]) == 24
assert len(record["mechanistic_edges"]) == 42
assert sum(len(e["evidence"]) for e in record["mechanistic_edges"]) == 79
manifest = json.loads((DOSSIER / "adenine-salvage-source-manifest.json").read_text())
raw_hashes = {}
for source in manifest["sources"]:
    actual = digest(source["file"])
    assert actual == source["sha256"], source["file"]
    raw_hashes[source["file"]] = actual
    if "archive_file" in source:
        assert digest(source["archive_file"]) == source["archive_sha256"]
for reference in record["references"]:
    assert digest(manifest["reference_artifacts"][reference["id"]]) == reference["source_sha256"]
projection = json.loads((DOSSIER / "adenine-salvage-source-projection.json").read_text())
# Reconstruct all retained native XML fields; the projection is not its own authority.
for identifier, saved in projection["native_metacyc"].items():
    item = native(identifier)
    assert saved["frameid"] == item.get("frameid")
    assert saved["label"] == item.findtext("common-name")
    assert saved["reactions"] == [x.get("frameid") for x in item.findall("reaction-list/Reaction")]
    for field, slot in [
        ("reaction_layout", "reaction-layout"),
        ("reaction_ordering", "reaction-ordering"),
        ("left", "left"),
        ("right", "right"),
        ("components", "component"),
    ]:
        assert saved[field] == [ET.tostring(x, encoding="unicode") for x in item.findall(slot)]
    assert saved["xrefs"] == [{c.tag: c.text for c in x} for x in item.findall("dblink")]
    assert saved["species"] == [x.get("frameid") for x in item.findall("species/Organism")]
for node in record["participants"]:
    if node["id"].startswith("MetaCyc:"):
        assert native(node["id"].split(":", 1)[1]).findtext("common-name") == node["label"]
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
edges = record["mechanistic_edges"]
expected_chemical_edges = set()
sides, balances, reaction_nets = [], [], {}
for master, (rid, direction, meta, pwy) in SELECTED.items():
    reaction = next(x for x in record["reactions"] if x["id"] == "RHEA:" + rid)
    assert reaction["label"] == nodes[RH + rid]["equation"][0]
    assert reaction["direction"] == direction
    assert RH + rid in nodes[RH + master]["directionalReaction"]
    assert directions[master][direction] == rid
    native_xrefs = [
        x.findtext("dblink-oid")
        for x in native(meta).findall("dblink")
        if x.findtext("dblink-db") == "RHEA"
    ]
    assert len(native_xrefs) == 1 and native_xrefs[0] in directions[master].values()
    assert meta in [x.get("frameid") for x in native(pwy).findall("reaction-list/Reaction")]
    membership = next(
        e for e in edges if e["subject"] == "RHEA:" + rid and e["predicate"] == "part_of"
    )
    assert membership["object"] == record["id"]
    assert any(
        x["reference_id"] == "RHEA:" + rid
        and f"rh:{master} rh:directionalReaction rh:{rid}" in x["source_locator"]
        for x in membership["evidence"]
    )
    balance = collections.Counter()
    net = collections.Counter()
    for side in ("substrates", "products"):
        side_uri = nodes[RH + rid][side][0]
        for key, values in nodes[side_uri].items():
            if not re.fullmatch(r"contains\d+", key):
                continue
            coefficient = int(key[8:])
            for part in values:
                compound = nodes[nodes[part]["compound"][0]]
                cid = compound["accession"][0]
                chemical = ontology("chebi", cid)
                assert chemical["chemrof:generalized_empirical_formula"] == compound["formula"][0]
                assert int(chemical["chemrof:charge"]) == int(compound["charge"][0])
                sign = -1 if side == "substrates" else 1
                net[cid] += sign * coefficient
                for atom, count in atoms(compound["formula"][0]).items():
                    balance[atom] += sign * coefficient * count
                balance["charge"] += sign * coefficient * int(compound["charge"][0])
                triple = (
                    (cid, "consumes", "RHEA:" + rid)
                    if sign == -1
                    else ("RHEA:" + rid, "produces", cid)
                )
                expected_chemical_edges.add(triple)
                chemical_edge = next(
                    e for e in edges if (e["subject"], e["predicate"], e["object"]) == triple
                )
                assert any(
                    x["reference_id"] == "RHEA:" + rid
                    and side_uri in x["source_locator"]
                    and part in x["source_locator"]
                    for x in chemical_edge["evidence"]
                )
                sides.append(
                    {"reaction": rid, "role": side, "chemical": cid, "coefficient": coefficient}
                )
    assert all(v == 0 for v in balance.values()), (rid, balance)
    reaction_nets[rid] = net
    balances.append(
        {"reaction": rid, "element_charge_residuals": dict(balance), "status": "passed"}
    )
actual_chemical_edges = {
    (e["subject"], e["predicate"], e["object"])
    for e in edges
    if e["predicate"] in {"consumes", "produces"}
}
assert actual_chemical_edges == expected_chemical_edges and len(sides) == 17

# Exact native boundary, source orientations and three material transfers.
pwy = native("PWY-6609")
assert pwy.findtext("common-name") == record["label"]
assert pwy.find("species/Organism").get("frameid") == "TAX-511145"
assert set(x.get("frameid") for x in pwy.findall("reaction-list/Reaction")) == {
    v[2] for v in SELECTED.values()
}
expected_orders = {
    ("ADENPHOSPHOR-RXN", "ADENODEAMIN-RXN"),
    ("ADENODEAMIN-RXN", "INOPHOSPHOR-RXN"),
    ("INOPHOSPHOR-RXN", "HYPOXANPRIBOSYLTRAN-RXN"),
}
assert {
    (x.find("predecessor-reactions/Reaction").get("frameid"), x.find("Reaction").get("frameid"))
    for x in pwy.findall("reaction-ordering")
} == expected_orders
assert {(e["subject"], e["object"]) for e in edges if e["predicate"] == "provides_input_for"} == {
    ("RHEA:27644", "RHEA:24409"),
    ("RHEA:24409", "RHEA:27647"),
    ("RHEA:27647", "RHEA:17975"),
}
full_net = collections.Counter()
for net in reaction_nets.values():
    full_net.update(net)
assert {k: v for k, v in full_net.items() if v} == {
    "CHEBI:16708": -1,
    "CHEBI:15377": -1,
    "CHEBI:15378": -1,
    "CHEBI:28938": 1,
    "CHEBI:58017": -1,
    "CHEBI:58053": 1,
    "CHEBI:33019": 1,
}
# PathBank legacy label I independently contains all four biochemical transformations.
bp = {
    x.get(RDF + "ID") or x.get(RDF + "about"): x for x in ET.parse(RAW / "PW002069.owl").getroot()
}
assert {k for k, x in bp.items() if x.tag == BP + "BiochemicalReaction"} == {
    "Reactions/6047",
    "Reactions/6049",
    "Reactions/6050",
    "Reactions/6052",
}
assert (
    bp["http://identifiers.org/smpdb/SMP0002081"].findtext(BP + "displayName")
    == "Adenine and Adenosine Salvage I"
)
normalization = {
    "PW_C001146": "CHEBI:57720",
    "PW_C000024": "CHEBI:16708",
    "PW_C000034": "CHEBI:16335",
    "PW_C001104": "CHEBI:43474",
    "PW_C001420": "CHEBI:15377",
    "PW_C040034": "CHEBI:15378",
    "PW_C000127": "CHEBI:17596",
    "PW_C022608": "CHEBI:28938",
    "PW_C000102": "CHEBI:17368",
    "PW_C000190": "CHEBI:58017",
    "PW_C000114": "CHEBI:58053",
    "PW_C000170": "CHEBI:33019",
}
for bid, rid in [("6047", "27644"), ("6049", "24409"), ("6050", "27647"), ("6052", "17975")]:
    reaction = bp["Reactions/" + bid]
    for source_side, role in [("left", "substrates"), ("right", "products")]:
        assert {
            normalization[x.get(RDF + "resource").rsplit("/", 1)[-1]]
            for x in reaction.findall(BP + source_side)
        } == {s["chemical"] for s in sides if s["reaction"] == rid and s["role"] == role}
    for x in reaction.findall(BP + "participantStoichiometry"):
        st = bp[x.get(RDF + "resource").lstrip("#")]
        assert float(st.findtext(BP + "stoichiometricCoefficient")) == 1
# Distinct native III identity: current I is the separate adenosine-to-AMP route.
assert set(x.get("frameid") for x in native("P121-PWY").findall("reaction-list/Reaction")) != {
    v[2] for v in SELECTED.values()
}
assert record["taxa"] == [{"id": "NCBITaxon:83333", "label": "Escherichia coli K-12"}]
activities = [
    ("P0ABP8", "DEOD-CPLX", 4, "ADENPHOSPHOR-ENZRXN", "27642", "27644"),
    ("P0ABP8", "DEOD-CPLX", 3, "INOPHOSPHOR-ENZRXN", "27646", "27647"),
    ("P22333", "ADENODEAMIN-MONOMER", 1, "ADENODEAMIN-ENZRXN", "24408", "24409"),
    ("P0A9M2", "CPLX0-7685", 1, "HYPOXANPRIBOSYLTRAN-ENZRXN", "17973", "17975"),
    ("P0A9M5", "GPT-CPLX", 3, "HYPXPRIBOSYLTRAN-ENZRXN", "17973", "17975"),
]
proteins = {
    up: json.loads((RAW / f"uniprot-{up}.json").read_text()) for up in {x[0] for x in activities}
}
for up, catalyst, idx, enz, master, rid in activities:
    p = proteins[up]
    assert (
        p["primaryAccession"] == up
        and p["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
        and p["organism"]["taxonId"] == 83333
    )
    saved = projection["uniprot"][up]
    assert saved["comments"] == p["comments"]
    assert saved["organism"] == p["organism"]
    assert saved["go_crossreferences"] == [
        x for x in p["uniProtKBCrossReferences"] if x["database"] == "GO"
    ]
    act = p["comments"][idx]
    assert any(x["id"] == "RHEA:" + master for x in act["reaction"]["reactionCrossReferences"])
    assert any(x["evidenceCode"] == "ECO:0000269" for x in act["reaction"]["evidences"])
    assert native(enz).find("enzyme/Protein").get("frameid") == catalyst
    expected_subject = "UniProtKB:" + up if up == "P22333" else "MetaCyc:" + catalyst
    assert any(
        e["subject"] == expected_subject
        and e["predicate"] == "catalyzes"
        and e["object"] == "RHEA:" + rid
        for e in edges
    )
    assert (
        next(x["label"] for x in record["participants"] if x["id"] == "UniProtKB:" + up)
        == p["proteinDescription"]["recommendedName"]["fullName"]["value"]
    )
for up, cplx, mono, count, idx in [
    ("P0ABP8", "DEOD-CPLX", "DEOD-MONOMER", 6, 10),
    ("P0A9M2", "CPLX0-7685", "HYPOXANPRIBOSYLTRAN-MONOMER", 4, 7),
    ("P0A9M5", "GPT-CPLX", "GPT-MONOMER", 4, 9),
]:
    n = native(cplx)
    assert (
        n.find("component/Protein").get("frameid") == mono
        and int(n.findtext("component/coefficient")) == count
    )
    assert any(
        x.findtext("dblink-db") == "UNIPROT" and x.findtext("dblink-oid") == up
        for x in native(mono).findall("dblink")
    )
    assert proteins[up]["comments"][idx]["commentType"] == "SUBUNIT"
    assert any(
        x["evidenceCode"] == "ECO:0000269"
        for x in proteins[up]["comments"][idx]["texts"][0]["evidences"]
    )
for up, idx, cid, eco in [
    ("P22333", 3, "CHEBI:29105", "ECO:0000255"),
    ("P0A9M2", 3, "CHEBI:18420", "ECO:0000305"),
    ("P0A9M5", 4, "CHEBI:18420", "ECO:0000269"),
]:
    c = proteins[up]["comments"][idx]
    assert c["commentType"] == "COFACTOR"
    assert any(
        x["cofactorCrossReference"]["id"] == cid
        and any(v["evidenceCode"] == eco for v in x["evidences"])
        for x in c["cofactors"]
    )
for e in [e for e in edges if e["predicate"] == "located_in"]:
    p = proteins[e["subject"].split(":", 1)[1]]
    x = next(
        x for x in p["uniProtKBCrossReferences"] if x["database"] == "GO" and x["id"] == e["object"]
    )
    code = next(x["value"] for x in x["properties"] if x["key"] == "GoEvidenceType")
    assert code in e["evidence"][0]["source_assertion"]
assert {e["subject"] for e in edges if e["predicate"] == "inhibits"} == {"CHEBI:58053"}
assert "IMP" in proteins["P0A9M2"]["comments"][4]["texts"][0]["value"]
# Exact primary source locations and explicit access limits.
abstracts = {
    x["id"]: x
    for x in json.loads((RAW / "primary-abstracts.json").read_text())["resultList"]["result"]
}
assert (
    "tetrameric" in abstracts["9100006"]["abstractText"]
    and "trimer" in abstracts["6305942"]["abstractText"]
)
assert (
    "Asp-89" in abstracts["9100006"]["abstractText"]
    or "Asp89" in abstracts["9100006"]["abstractText"]
)
assert (
    "Glu 103" in abstracts["12070315"]["abstractText"]
    or "Glu103" in abstracts["12070315"]["abstractText"]
)
passages = [
    x.findtext("text", "") for x in ET.parse(RAW / "PMC6193948.xml").getroot().findall(".//passage")
]
assert "homohexamer" in passages[40] and "238 amino acids" in passages[40]
assert passages[62] == "Preparation of ternary complexes for crystallisation"
assert "Recombinant wild-type" in passages[63]
assert (RAW / "PMID765747.pdf").read_bytes().startswith(b"%PDF")
assert all(
    token in (RAW / "PMID765747-text.txt").read_text()
    for token in ["Adenosine Deaminase", "Hypoxanthine", "K-12", "Table 2"]
)
for node in record["participants"] + record["taxa"]:
    db = next(
        (
            db
            for prefix, db in [("CHEBI:", "chebi"), ("NCBITaxon:", "ncbitaxon"), ("GO:", "go")]
            if node["id"].startswith(prefix)
        ),
        None,
    )
    if db:
        facts = ontology(db, node["id"])
        assert facts["rdfs:label"] == node["label"] and facts.get("owl:deprecated") not in [
            "true",
            "1",
        ]
# Actual KGX output, including every evidence block and source assertion locator.
exported = kgx_edges([validated])
references = {r["id"]: r for r in record["references"]}
assert len(exported) == len(edges)
for actual, expected in zip(exported, edges, strict=True):
    assert (actual.subject, actual.predicate, actual.object) == (
        expected["subject"],
        LOCAL_PREDICATE_CURIES[expected["predicate"]],
        expected["object"],
    )
    assert json.loads(actual.evidence) == expected["evidence"]
    assert json.loads(actual.reference_metadata) == [
        references[i] for i in sorted({x["reference_id"] for x in expected["evidence"]})
    ]
    assert actual.description == expected.get("description", "")
exported_nodes = {x.id: x for x in kgx_nodes([validated])}
assert len(exported_nodes) == 30
for rid, direction, _, _ in SELECTED.values():
    assert (
        exported_nodes["RHEA:" + rid].direction == direction
        and exported_nodes["RHEA:" + rid].category == "biolink:BiochemicalReaction"
    )
paths = write_kgx([validated], RAW / "kgx")
forbidden = {
    "cookie",
    "set-cookie",
    "authorization",
    "proxy-authorization",
    "x-api-key",
    "access_token",
    "refresh_token",
}


def metadata_safe(value):
    if isinstance(value, dict):
        assert not any(k.lower() in forbidden for k in value)
        for v in value.values():
            metadata_safe(v)
    elif isinstance(value, list):
        for v in value:
            metadata_safe(v)


metadata_safe(manifest)
result = {
    "status": "passed",
    "started_at": STARTED,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "replay_script_sha256": digest(Path(__file__)),
    "checks": [
        "native and closed schemas",
        "all source/reference raw body hashes",
        "full original Rhea RDF and four directional-family bridges",
        "17 exact chemical sides, four formula/charge balances and complete route net",
        "four native MetaCyc reactions and three predecessor links",
        "independent full PathBank four-reaction chemistry, legacy label disposition",
        "three assemblies, four reviewed K-12 proteins and five catalytic links",
        "cofactor inference tiers, localization annotations and product inhibition",
        "primary exact locators and historical assembly discrepancy",
        "canonical ontology/protein labels and actual 30-node/42-edge/79-evidence KGX parity",
        "source metadata safety",
    ],
    "balances": balances,
    "route_net": {k: v for k, v in full_net.items() if v},
    "raw_hashes": raw_hashes,
    "kgx": [{"path": str(p), "sha256": digest(p)} for p in paths],
    "excluded_checks": (
        "Author replay does not replace independent scientific review or root whole-corpus gates."
    ),
}
(RAW / "replay-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps({k: v for k, v in result.items() if k not in ["raw_hashes", "balances"]}, indent=2)
)
