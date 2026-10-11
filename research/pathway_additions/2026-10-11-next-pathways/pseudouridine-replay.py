"""Replay exact retained source bodies and the target without network/shared writes.

Run from the repository root with .venv/bin/python. The external raw cache is
required; no curated projection is used as a substitute for primary input.
"""

import csv
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import UTC, datetime
from functools import cache
from pathlib import Path

import yaml

from pathwaymech.kgx import write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
RAW = Path("/private/tmp/pathwaymech-next-pathways-evidence/pseudouridine")
AUTH = Path("/private/tmp/pathwaymech-curation-authorities")
RESEARCH = ROOT / "research/pathway_additions/2026-10-11-next-pathways"
TARGET = ROOT / "data/pathways/pseudouridine-degradation.yaml"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
URI = "http://rdf.rhea-db.org/"


@cache
def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def native_frame(name, tag):
    root = ET.parse(RAW / f"metacyc-{name}.xml").getroot()
    assert root.find("metadata/PGDB").get("orgid") == "META"
    frame = root.find(tag)
    assert frame.get("frameid") == name and frame.get("detail") == "full"
    return frame


def has_xref(frame, database, identifier):
    return any(
        x.findtext("dblink-db") == database
        and x.findtext("dblink-oid") == identifier
        and x.findtext("dblink-relationship") == "unification"
        for x in frame.findall("dblink")
    )


record = yaml.safe_load(TARGET.read_text())
validated = validate_record(record)
assert not strict_errors([TARGET], ROOT)
manifest = json.loads((RESEARCH / "pseudouridine-source-manifest.json").read_text())
assert manifest["target_sha256"] == sha(TARGET)
bodies = {x["id"]: Path(x["path"]) for x in manifest["record_reference_bodies"]}
for reference in record["references"]:
    assert sha(bodies[reference["id"]]) == reference["source_sha256"]
artifact_count = 0
for artifact in manifest["artifacts"]:
    if artifact.get("sha256"):
        assert sha(artifact["path"]) == artifact["sha256"], artifact["file"]
        artifact_count += 1
    assert all(
        key.lower()
        in {"content-type", "last-modified", "etag", "x-uniprot-release", "x-uniprot-release-date"}
        for key in artifact.get("headers", {})
    )

# Replay the complete native discovery graph, including its misleading title.
native = {}
for element in ET.parse(RAW / "PW001887.owl").getroot():
    key = element.get(RDF + "about") or "#" + element.get(RDF + "ID", "")
    values = defaultdict(list)
    for child in element:
        values[child.tag.split("}")[-1]].append(child.get(RDF + "resource") or child.text)
    native[key] = dict(values)
discovery = native["http://identifiers.org/smpdb/SMP0001901"]
assert {x for x in discovery["pathwayComponent"] if x.startswith("#Reactions/")} == {
    "#Reactions/5150",
    "#Reactions/5151",
}
projection = json.loads((RESEARCH / "pseudouridine-source-projection.json").read_text())
assert {
    key: value["properties"] for key, value in projection["native_pathbank"]["objects"].items()
} == native
assert projection["native_pathbank"]["sha256"] == sha(RAW / "PW001887.owl")

pathway = native_frame("PWY-6019", "Pathway")
assert pathway.findtext("common-name") == record["label"]
assert {x.get("frameid") for x in pathway.findall("reaction-list/Reaction")} == {
    "PSEUDOURIDINE-KINASE-RXN",
    "RXN0-5398",
}
layouts = {
    x.find("Reaction").get("frameid"): x.findtext("direction")
    for x in pathway.findall("reaction-layout")
}
assert layouts == {"PSEUDOURIDINE-KINASE-RXN": "L2R", "RXN0-5398": "R2L"}
ordering = pathway.find("reaction-ordering")
assert ordering.find("Reaction").get("frameid") == "RXN0-5398"
assert ordering.find("predecessor-reactions/Reaction").get("frameid") == "PSEUDOURIDINE-KINASE-RXN"
assert has_xref(native_frame("PSEUDOURIDINE-KINASE-RXN", "Reaction"), "RHEA", "22449")
assert has_xref(native_frame("RXN0-5398", "Reaction"), "RHEA", "18340")

# Two full-RDF streaming passes retain original family/side/coefficient predicates.
masters = {"22448", "18337"}
directions = [
    row
    for row in csv.DictReader((AUTH / "rhea-directions.tsv").open(), delimiter="\t")
    if row["RHEA_ID_MASTER"] in masters
]
assert len(directions) == 2
needed = {URI + value for row in directions for value in row.values()}
needed |= {URI + master + "_" + side for master in masters for side in ["L", "R"]}
nodes = defaultdict(lambda: defaultdict(list))


def collect(wanted, participants=False):
    depth = 0
    with gzip.open(AUTH / "rhea.rdf.gz", "rb") as stream:
        for event, element in ET.iterparse(stream, events=["start", "end"]):
            if event == "start":
                depth += 1
                continue
            if depth == 2:
                key = element.get(RDF + "about")
                if key in wanted or (
                    participants
                    and any(
                        (key or "").startswith(URI + "Participant_" + master + "_")
                        for master in masters
                    )
                ):
                    for child in element:
                        value = child.get(RDF + "resource") or child.text
                        predicate = child.tag.split("}")[-1]
                        if value is not None and value not in nodes[key][predicate]:
                            nodes[key][predicate].append(value)
                element.clear()
            depth -= 1


collect(needed, True)
collect({c for node in nodes.values() for c in node.get("compound", [])})
chebi = sqlite3.connect(f"file:{AUTH / 'chebi.db'}?mode=ro", uri=True)
reaction_checks = []
side_count = 0
for master, directed, direction in [
    ("22448", "22449", "left_to_right"),
    ("18337", "18339", "right_to_left"),
]:
    rid = "RHEA:" + directed
    row = next(r for r in directions if r["RHEA_ID_MASTER"] == master)
    assert URI + directed in nodes[URI + master]["directionalReaction"]
    assert URI + row["RHEA_ID_BI"] in nodes[URI + master]["bidirectionalReaction"]
    assert next(r for r in record["reactions"] if r["id"] == rid)["direction"] == direction
    balance = Counter()
    charge = 0
    sides = {}
    for role in ["substrates", "products"]:
        sides[role] = []
        for side in nodes[URI + directed][role]:
            for predicate, participants in nodes[side].items():
                if not re.fullmatch(r"contains\d+", predicate):
                    continue
                coefficient = int(predicate[8:])
                for participant in participants:
                    compound = nodes[nodes[participant]["compound"][0]]
                    cid = compound["accession"][0]
                    values = dict(
                        chebi.execute(
                            "select predicate,value from statements "
                            "where subject=? and predicate in "
                            "('chemrof:generalized_empirical_formula','chemrof:charge')",
                            (cid,),
                        )
                    )
                    assert values["chemrof:generalized_empirical_formula"] == compound["formula"][0]
                    assert int(values["chemrof:charge"]) == int(compound["charge"][0])
                    sign = -1 if role == "substrates" else 1
                    for atom, count in re.findall(r"([A-Z][a-z]?)(\d*)", compound["formula"][0]):
                        balance[atom] += sign * coefficient * int(count or 1)
                    charge += sign * coefficient * int(compound["charge"][0])
                    endpoint = (cid, rid) if role == "substrates" else (rid, cid)
                    edge_predicate = "consumes" if role == "substrates" else "produces"
                    matches = [
                        e
                        for e in record["mechanistic_edges"]
                        if (e["subject"], e["object"]) == endpoint
                        and e["predicate"] == edge_predicate
                    ]
                    assert len(matches) == 1
                    evidence = matches[0]["evidence"][0]
                    assert (
                        side in evidence["source_locator"]
                        and participant in evidence["source_locator"]
                    )
                    assert f"rh:contains{coefficient}" in evidence["source_locator"]
                    assert f"coefficient {coefficient}" in evidence["source_assertion"]
                    sides[role].append([cid, coefficient])
                    side_count += 1
    assert not any(balance.values()) and charge == 0, rid
    reaction_checks.append({"reaction": rid, "master": master, "sides": sides, "balance": "pass"})
assert side_count == 9
assert (
    len([e for e in record["mechanistic_edges"] if e["predicate"] in {"consumes", "produces"}]) == 9
)

# Native physical trimer and taxon/protein crosswalk, distinct from kinase function.
assembly = native_frame("CPLX0-8233", "Protein")
assert assembly.find("component/Protein").get("frameid") == "EG12033-MONOMER"
assert assembly.findtext("component/coefficient") == "3"
assert assembly.find("catalyzes/Enzymatic-Reaction/reaction/Reaction").get("frameid") == "RXN0-5398"
subunit = native_frame("EG12033-MONOMER", "Protein")
assert has_xref(subunit, "UNIPROT", "P33025")
assert subunit.find("species/Organism").get("frameid") == "TAX-511145"
for accession, master in [("P30235", "22448"), ("P33025", "18337")]:
    protein = json.loads((RAW / f"uniprot-{accession}.json").read_text())
    assert protein["organism"]["taxonId"] == 83333
    node = next(n for n in record["participants"] if n["id"] == "UniProtKB:" + accession)
    assert node["label"] == protein["proteinDescription"]["recommendedName"]["fullName"]["value"]
    assert {"database": "Rhea", "id": "RHEA:" + master} in protein["comments"][1]["reaction"][
        "reactionCrossReferences"
    ]
    if accession == "P30235":
        assert not any(c["commentType"] == "SUBUNIT" for c in protein["comments"])
        assert (
            next(e for e in record["mechanistic_edges"] if e["subject"] == node["id"])["predicate"]
            == "enables"
        )
    else:
        assert protein["comments"][5]["texts"][0]["value"] == "Homotrimer"
        metals = {x["cofactorCrossReference"]["id"] for x in protein["comments"][2]["cofactors"]}
        assert metals == {
            e["object"] for e in record["mechanistic_edges"] if e["predicate"] == "has_cofactor"
        }
for node in record["participants"]:
    if node["id"].startswith("CHEBI:"):
        assert (
            chebi.execute(
                "select value from statements where subject=? and predicate='rdfs:label'",
                (node["id"],),
            ).fetchone()[0]
            == node["label"]
        )

# Literal quotations plus source-specific strain, kinetics and structural limits.
abstract = json.loads(bodies["PMID:18591240"].read_text())["resultList"]["result"][0][
    "abstractText"
]
bioc = ET.parse(bodies["PMID:23066817"])
passages = {p.findtext("offset"): p.findtext("text", "") for p in bioc.findall(".//passage")}
full_2022 = " ".join(ET.parse(bodies["PMID:35783380"]).getroot().itertext())
source_text = {"PMID:18591240": abstract, "PMID:23066817": " ".join(passages.values())}
quotes = [e for edge in record["mechanistic_edges"] for e in edge["evidence"] if "quote" in e]
for evidence in quotes:
    assert " ".join(evidence["quote"].split()) in " ".join(
        source_text[evidence["reference_id"]].split()
    )
assert "UTI89" in abstract
assert "K12 genomic DNA" in passages["6100"] and "BL21(DE3)" in passages["6949"]
assert "homotrimer" in passages["17266"] and "reverse reaction" in passages["24413"]
assert all(x in passages["31636"] for x in ["Fe(II)", "Co(II)", "Mn(II)", "inhibitory"])
assert "A0A140N873" in full_2022 and "BL21" in full_2022 and "homodimer" in full_2022

output = RAW / "kgx"
write_kgx([validated], output)
edges = list(csv.DictReader((output / "edges.tsv").open(), delimiter="\t"))
export_nodes = list(csv.DictReader((output / "nodes.tsv").open(), delimiter="\t"))
assert len(edges) == len(record["mechanistic_edges"])
for exported, original in zip(edges, record["mechanistic_edges"], strict=True):
    assert json.loads(exported["evidence"]) == original["evidence"]
    assert exported["description"] == original.get("description", "")
    assert json.loads(exported["reference_metadata"])
assert (
    next(n for n in export_nodes if n["id"] == "MetaCyc:CPLX0-8233")["category"]
    == "biolink:MacromolecularComplex"
)

receipt = {
    "status": "pass",
    "completed_at": datetime.now(UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": sha(TARGET),
    "command": ".venv/bin/python "
    "research/pathway_additions/2026-10-11-next-pathways/pseudouridine-replay.py",
    "raw_cache": str(RAW),
    "rhea_gzip_sha256": sha(AUTH / "rhea.rdf.gz"),
    "native_member_sha256": sha(RAW / "PW001887.owl"),
    "checks": [
        "native and closed schemas",
        "all 12 reference digests",
        f"{artifact_count} retained artifact digests and safe header keys",
        "complete original PathBank graph",
        "exact two-step MetaCyc boundary and order",
        "nine full-RDF sides/coefficient locators",
        "two atom/charge balances against full ChEBI",
        "directional versus bidirectional Rhea bridges",
        "native trimer/protein/taxon crosswalk",
        "current UniProt names, catalytic references and alternative metals",
        "all ChEBI labels",
        "two literal quotes and primary strain/reverse-assay limits",
        "actual KGX evidence, descriptions and complex category",
    ],
    "reaction_replay": reaction_checks,
    "counts": {
        "participants": len(record["participants"]),
        "reactions": len(record["reactions"]),
        "edges": len(edges),
        "evidence": sum(len(e["evidence"]) for e in record["mechanistic_edges"]),
        "kgx_nodes": len(export_nodes),
        "references": len(record["references"]),
        "quotes": len(quotes),
    },
    "scope": "Author source replay; not an independent scientific review "
    "or replacement for delegated integration gates.",
}
(RAW / "author-replay.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(
    json.dumps(
        {"status": "pass", "receipt": str(RAW / "author-replay.json"), "counts": receipt["counts"]}
    )
)
