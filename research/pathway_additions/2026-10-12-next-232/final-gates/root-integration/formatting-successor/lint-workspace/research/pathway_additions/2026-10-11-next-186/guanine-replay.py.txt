"""Replay complete guanine salvage scope and chemistry from original authority inputs."""

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
RAW = Path("/private/tmp/pathwaymech-next-186-evidence/guanine")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-186"
TARGET = ROOT / "data/pathways/guanine-and-guanosine-salvage.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
SELECTED = {
    "27710": ("27711", "left_to_right", "GUANOSINEKIN-RXN", "PWY-6618"),
    "13233": ("13234", "left_to_right", "RXN0-5199", "PWY-6620"),
    "25424": ("25426", "right_to_left", "GUANPRIBOSYLTRAN-RXN", "PWY-6620"),
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
assert record["id"] == "MetaCyc:PWY-6579"
assert len(record["reactions"]) == 3 and len(record["participants"]) == 19
assert len(record["mechanistic_edges"]) == 27
assert sum(len(e["evidence"]) for e in record["mechanistic_edges"]) == 51
manifest = json.loads((DOSSIER / "guanine-source-manifest.json").read_text())
raw_hashes = {}
for source in manifest["sources"]:
    actual = digest(source["file"])
    assert actual == source["sha256"], source["file"]
    raw_hashes[source["file"]] = actual
    if "archive_file" in source:
        assert digest(source["archive_file"]) == source["archive_sha256"]
for reference in record["references"]:
    assert digest(manifest["reference_artifacts"][reference["id"]]) == reference["source_sha256"]
projection = json.loads((DOSSIER / "guanine-source-projection.json").read_text())
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
assert actual_chemical_edges == expected_chemical_edges and len(sides) == 13
indirect_net = collections.Counter()
for rid in ["13234", "25426"]:
    indirect_net.update(reaction_nets[rid])
assert indirect_net["CHEBI:16235"] == 0
assert {k: v for k, v in indirect_net.items() if v} == {
    "CHEBI:16750": -1,
    "CHEBI:43474": -1,
    "CHEBI:58017": -1,
    "CHEBI:57720": 1,
    "CHEBI:58115": 1,
    "CHEBI:33019": 1,
}
# Exact native hierarchy and correct separation of the two alternatives.
superpathway = native("PWY-6579")
assert [x.get("frameid") for x in superpathway.findall("reaction-list/Pathway")] == [
    "PWY-6618",
    "PWY-6620",
]
assert superpathway.findtext("common-name") == record["label"]
assert "adenosine" in superpathway.findtext("comment")
assert not any(
    x["reference_id"] == "MetaCyc:PWY-6579" and "/comment" in x["source_locator"]
    for e in edges
    for x in e["evidence"]
)
order = native("PWY-6620").find("reaction-ordering")
assert order.find("Reaction").get("frameid") == "GUANPRIBOSYLTRAN-RXN"
assert order.find("predecessor-reactions/Reaction").get("frameid") == "RXN0-5199"
transfers = [e for e in edges if e["predicate"] == "provides_input_for"]
assert (
    len(transfers) == 1
    and transfers[0]["subject"] == "RHEA:13234"
    and transfers[0]["object"] == "RHEA:25426"
)
# Native PathBank document retains exactly the same three reactions and coherent sides.
biopax_root = ET.parse(RAW / "PW002074.owl").getroot()
bp = {x.get(RDF + "ID") or x.get(RDF + "about"): x for x in biopax_root}
pathway = bp["http://identifiers.org/smpdb/SMP0002086"]
actual_members = {
    x.get(RDF + "resource").lstrip("#") for x in pathway.findall(BP + "pathwayComponent")
}
assert {k for k, x in bp.items() if x.tag == BP + "BiochemicalReaction"} == {
    "Reactions/6057",
    "Reactions/6058",
    "Reactions/6059",
}
assert {"Reactions/6057", "Reactions/6058", "Reactions/6059"} <= actual_members
normalization = {
    "PW_C000087": "CHEBI:16750",
    "PW_C000414": "CHEBI:30616",
    "PW_C001034": "CHEBI:456216",
    "PW_C040034": "CHEBI:15378",
    "PW_C001080": "CHEBI:58115",
    "PW_C001104": "CHEBI:43474",
    "PW_C001146": "CHEBI:57720",
    "PW_C000086": "CHEBI:16235",
    "PW_C000190": "CHEBI:58017",
    "PW_C000170": "CHEBI:33019",
}
for native_id, rid in [("6057", "27711"), ("6058", "13234"), ("6059", "25426")]:
    x = bp["Reactions/" + native_id]
    for native_side, role in [("left", "substrates"), ("right", "products")]:
        source_ids = {
            normalization[y.get(RDF + "resource").rsplit("/", 1)[-1]]
            for y in x.findall(BP + native_side)
        }
        assert source_ids == {
            s["chemical"] for s in sides if s["reaction"] == rid and s["role"] == role
        }
# Each complex, current protein, exact activity and magnesium assignment.
assemblies = [
    (
        "P0AEW6",
        "CPLX0-322",
        "GSK-MONOMER",
        2,
        "GUANOSINEKIN-ENZRXN",
        "GUANOSINEKIN-RXN",
        "27710",
        "27711",
    ),
    (
        "P0ABP8",
        "DEOD-CPLX",
        "DEOD-MONOMER",
        6,
        "GUANPHOSPHOR-ENZRXN",
        "RXN0-5199",
        "13233",
        "13234",
    ),
    (
        "P0A9M5",
        "GPT-CPLX",
        "GPT-MONOMER",
        4,
        "GUANPRIBOSYLTRAN-ENZRXN",
        "GUANPRIBOSYLTRAN-RXN",
        "25424",
        "25426",
    ),
]
for up, cplx, mono, count, enz, rxn, master, rid in assemblies:
    protein = json.loads((RAW / f"uniprot-{up}.json").read_text())
    assert (
        protein["primaryAccession"] == up
        and protein["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    )
    assert protein["organism"]["taxonId"] == 83333
    assert any(
        x["database"] == "BioCyc" and x["id"] == "MetaCyc:" + mono
        for x in protein["uniProtKBCrossReferences"]
    )
    complex_node = native(cplx)
    assert complex_node.find("component/Protein").get("frameid") == mono
    assert int(complex_node.findtext("component/coefficient")) == count
    assert complex_node.find("species/Organism").get("frameid") == "TAX-511145"
    assert native(enz).find("enzyme/Protein").get("frameid") == cplx
    assert native(enz).find("reaction/Reaction").get("frameid") == rxn
    activity = next(
        c
        for c in protein["comments"]
        if c["commentType"] == "CATALYTIC ACTIVITY"
        and any(y["id"] == "RHEA:" + master for y in c["reaction"]["reactionCrossReferences"])
    )
    assert any(x["evidenceCode"] == "ECO:0000269" for x in activity["reaction"]["evidences"])
    assert any(
        e["subject"] == "MetaCyc:" + cplx
        and e["predicate"] == "catalyzes"
        and e["object"] == "RHEA:" + rid
        for e in edges
    )
    if up != "P0ABP8":
        assert any(
            c["commentType"] == "COFACTOR"
            and any(x["cofactorCrossReference"]["id"] == "CHEBI:18420" for x in c["cofactors"])
            for c in protein["comments"]
        )
    assert (
        next(p["label"] for p in record["participants"] if p["id"] == "UniProtKB:" + up)
        == protein["proteinDescription"]["recommendedName"]["fullName"]["value"]
    )
# Independently retained primary bodies prove the cited source scopes and conflicts.
abstracts = {
    x["id"]: x
    for x in json.loads((RAW / "primary-abstracts.json").read_text())["resultList"]["result"]
}
assert "tetrameric" in abstracts["9100006"]["abstractText"]
assert "trimer" in abstracts["6305942"]["abstractText"]
assert "six subunits" in abstracts["235429"]["abstractText"]
assert "inhibited by GDP and GTP" in abstracts["10879466"]["abstractText"]
passages = [
    x.findtext("text", "")
    for x in ET.parse(RAW / "PMC8362273-ncbi.xml").getroot().findall(".//passage")
]
assert "GDP, but not GTP or GMP" in passages[11]
assert (
    "dimers in the absence of ppGpp" in passages[13] and "tetramers in the presence" in passages[13]
)
assert "dimerization is required for Gsk activity" in passages[18]
assert "tetramers are less active than dimers" in passages[26]
assert "MG1655" in passages[69]
assert "both the inosine- and guanosine-kinase activities" in passages[12]
assert not any(e["subject"] == "CHEBI:37565" and e["predicate"] == "inhibits" for e in edges)
assert {e["subject"] for e in edges if e["predicate"] == "inhibits"} == {
    "CHEBI:77828",
    "CHEBI:58189",
}
for node in record["participants"] + record["taxa"]:
    if node["id"].startswith(("CHEBI:", "NCBITaxon:")):
        facts = ontology("chebi" if node["id"].startswith("CHEBI:") else "ncbitaxon", node["id"])
        assert facts["rdfs:label"] == node["label"]
        assert facts.get("owl:deprecated") not in ["true", "1"]
# Real KGX serialization keeps every edge, evidence item and reference metadata.
exported = kgx_edges([validated])
assert len(exported) == len(edges)
references = {r["id"]: r for r in record["references"]}
for actual, expected in zip(exported, edges, strict=True):
    assert (actual.subject, actual.predicate, actual.object) == (
        expected["subject"],
        LOCAL_PREDICATE_CURIES[expected["predicate"]],
        expected["object"],
    )
    assert json.loads(actual.evidence) == expected["evidence"]
    assert json.loads(actual.reference_metadata) == [
        references[i] for i in sorted({e["reference_id"] for e in expected["evidence"]})
    ]
    assert actual.description == expected.get("description", "")
exported_nodes = {x.id: x for x in kgx_nodes([validated])}
assert len(exported_nodes) == 24
for rid, direction, _, _ in SELECTED.values():
    assert exported_nodes["RHEA:" + rid].direction == direction
    assert exported_nodes["RHEA:" + rid].category == "biolink:BiochemicalReaction"
paths = write_kgx([validated], RAW / "kgx")
result = {
    "status": "passed",
    "started_at": STARTED,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "replay_script_sha256": digest(Path(__file__)),
    "checks": [
        "native and closed schemas",
        "all retained source and reference digests",
        "independent full Rhea RDF replay, three explicit master/directional families",
        "all 13 chemical sides and three formula/charge balances",
        "native complete two-route boundary and one material dependency",
        "PathBank complete three-reaction corroboration, no exact-match charge claim",
        "three native assemblies/current protein/activity bridges",
        "magnesium and primary Gsk assembly/regulation scopes",
        "historical Gpt and unresolved GTP conflicts preserved",
        "all canonical chemical/taxon/protein labels",
        "actual 24-node/27-edge/51-evidence KGX parity",
    ],
    "balances": balances,
    "indirect_branch_net": dict(indirect_net),
    "direct_branch_net": dict(reaction_nets["27711"]),
    "raw_hashes": raw_hashes,
    "kgx": [{"path": str(p), "sha256": digest(p)} for p in paths],
    "excluded_checks": (
        "Shared whole-corpus gates, renderer, independent scientific review and publication "
        "are handled by root/reviewer and are not claimed by this author replay."
    ),
}
(RAW / "replay-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps({k: v for k, v in result.items() if k not in ["raw_hashes", "balances"]}, indent=2)
)
