"""Replay PWY-5901 against original source bytes; not independent scientific review."""

from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.util
import io
import json
import re
import sqlite3
import zipfile
from collections import Counter
from pathlib import Path

import yaml
from lxml import etree

from pathwaymech.kgx import render_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path(__file__).resolve().parents[3]
DOSSIER = Path(__file__).parent
RAW = Path("/private/tmp/pathwaymech-next-195-evidence/dhb")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml"
RH = "http://rdf.rhea-db.org/"
NS = {
    "rh": RH,
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}
RDF_RESOURCE = "{" + NS["rdf"] + "}resource"


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_json(name):
    return json.loads((DOSSIER / name).read_text())


def main():
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert strict_errors([TARGET], ROOT) == []
    projection = read_json("dhb-source-projection.json")
    manifest = read_json("dhb-source-manifest.json")
    identifiers = read_json("dhb-identifiers.json")
    target_hash = digest(TARGET)
    for item in [projection, manifest, identifiers]:
        assert item["target_sha256"] == target_hash
    for item in manifest["source_bodies"]:
        assert digest(item["raw_path"]) == item["sha256"]
    authority_sources = json.loads(
        (ROOT / "data/identifier_authorities/ontology.json").read_text()
    )["sources"]
    for name, key in [("chebi.db", "chebi-255"), ("go.db", "go-2026-07-26")]:
        source = next(x for x in manifest["source_bodies"] if x["raw_path"].endswith(name))
        for field in ["url", "sha256", "sha256_scope"]:
            assert source[field] == authority_sources[key][field]
    for ref in doc["references"]:
        assert digest(manifest["reference_body_map"][ref["id"]]) == ref["source_sha256"]
    spec = importlib.util.spec_from_file_location(
        "source_builder", ROOT / "scripts/build_source_identifier_snapshot.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    inputs = read_json("dhb-authority-inputs.json")
    for item in inputs["proposed_source_inputs"]:
        if item["kind"] == "metacyc-html":
            assert list(module.metacyc_terms(Path(item["raw_path"]).read_text())) == [
                (item["id"], item["canonical_label"], [])
            ]
    # Independently parse original RDF descriptions referenced by the source projection.
    original = gzip.open(CACHE / "rhea.rdf.gz", "rt").read()
    wanted = {RH + x for x in ["18985", "18986", "11112", "11113", "23824", "23825"]}
    for side in projection["rhea_side_projection"]:
        wanted.update(side[k] for k in ["side_uri", "participant_uri", "compound_uri"])
    nodes: dict = {}
    wrapper = "<root " + " ".join(f'xmlns:{k}="{v}"' for k, v in NS.items()) + ">"
    for match in re.finditer(r'<rdf:Description rdf:about="([^"]+)">', original):
        uri = match[1]
        if uri not in wanted:
            continue
        end = original.index("</rdf:Description>", match.start()) + len("</rdf:Description>")
        element = etree.fromstring((wrapper + original[match.start() : end] + "</root>").encode())[
            0
        ]
        props = nodes.setdefault(uri, {})
        for child in element:
            key = child.tag.split("}", 1)[1]
            val = child.get(RDF_RESOURCE) or child.text
            if val not in props.setdefault(key, []):
                props[key].append(val)
    assert wanted == set(nodes)
    del original
    edges = {e["id"]: e for e in doc["mechanistic_edges"]}
    chemical_edges = {
        e["id"] for e in doc["mechanistic_edges"] if e["predicate"] in {"consumes", "produces"}
    }
    assert chemical_edges == {s["edge_id"] for s in projection["rhea_side_projection"]}
    connection = sqlite3.connect(f"file:{CACHE / 'chebi.db'}?mode=ro", uri=True)
    chemistry = {}
    for curie in {s["curie"] for s in projection["rhea_side_projection"]}:
        props = dict(
            connection.execute(
                "SELECT predicate,value FROM statements WHERE subject=? AND value IS NOT NULL",
                (curie,),
            ).fetchall()
        )
        chemistry[curie] = props
    connection.close()
    totals: dict = {}
    for side in projection["rhea_side_projection"]:
        master, directed = RH + side["master"], RH + side["directed"]
        assert directed in nodes[master]["directionalReaction"]
        assert side["side_uri"] in nodes[directed][side["side"]]
        assert side["participant_uri"] in nodes[side["side_uri"]][side["coefficient_predicate"]]
        assert side["compound_uri"] in nodes[side["participant_uri"]]["compound"]
        compound = nodes[side["compound_uri"]]
        assert compound["accession"] == [side["curie"]]
        assert compound["formula"] == [side["formula"]]
        assert compound["charge"] == [str(side["charge"])]
        assert chemistry[side["curie"]]["chemrof:generalized_empirical_formula"] == side["formula"]
        assert chemistry[side["curie"]]["chemrof:charge"] == str(side["charge"])
        edge = edges[side["edge_id"]]
        endpoint = "subject" if side["side"] == "substrates" else "object"
        assert edge[endpoint] == side["curie"]
        assert f"coefficient {side['coefficient']}" in edge["evidence"][0]["source_assertion"]
        assert side["coefficient_predicate"] in edge["evidence"][0]["source_locator"]
        total = totals.setdefault(side["directed"], {}).setdefault(side["side"], Counter())
        for atom, count in re.findall(r"([A-Z][a-z]?)(\d*)", side["formula"]):
            total[atom] += int(count or "1") * side["coefficient"]
        total["charge"] += side["charge"] * side["coefficient"]
    for sides in totals.values():
        assert sides["substrates"] == sides["products"]

    # Every native chemical uses an explicit external identity AND identical isomer/charge InChI.
    native_to_chebi = {}
    for frame, item in projection["compound_crosswalks"].items():
        compound = etree.parse(item["raw_path"]).find("Compound")
        assert compound.get("frameid") == frame
        assert compound.xpath('./dblink[dblink-db="CHEBI"]/dblink-oid/text()') == [
            item["curie"].split(":")[1]
        ]
        assert compound.findtext("inchi") == chemistry[item["curie"]]["chemrof:inchi_string"]
        native_to_chebi[frame] = item["curie"]
    directions = list(csv.DictReader((CACHE / "rhea-directions.tsv").open(), delimiter="\t"))
    for reaction in projection["reactions"]:
        frame = reaction["native_id"].split(":")[1]
        element = etree.parse(reaction["raw_path"]).find("Reaction")
        assert element.findtext("reaction-direction") == reaction["native_direction"]
        assert (
            element.xpath('./dblink[dblink-db="RHEA"]/dblink-oid/text()')
            == reaction["native_rhea_xrefs"]
        )
        directed = reaction["selected_reaction"].split(":")[1]
        row = next(x for x in directions if x["RHEA_ID_LR"] == directed)
        assert row["RHEA_ID_MASTER"] in {"18985", "11112", "23824"}
        for side, selected_side in [("left", "substrates"), ("right", "products")]:
            original = Counter()
            for part in element.findall(side):
                original[native_to_chebi[part[0].get("frameid")]] += int(
                    part.findtext("coefficient", "1")
                )
            selected = Counter(
                {
                    s["curie"]: s["coefficient"]
                    for s in projection["rhea_side_projection"]
                    if s["directed"] == directed and s["side"] == selected_side
                }
            )
            assert original == selected
        if frame == "ISOCHORSYN-RXN":
            assert row["RHEA_ID_BI"] == "18988" and reaction["native_direction"] == "REVERSIBLE"
            assert RH + "18988" in nodes[RH + "18985"]["bidirectionalReaction"]
    pathway = etree.parse(str(RAW / "metacyc-PWY-5901.xml")).find("Pathway")
    assert set(pathway.xpath("./reaction-list/*/@frameid")) == {
        "ISOCHORSYN-RXN",
        "ISOCHORMAT-RXN",
        "DHBDEHYD-RXN",
    }
    assert set(doc["reactions"][i]["id"] for i in range(3)) == {
        "RHEA:18986",
        "RHEA:11113",
        "RHEA:23825",
    }
    assert all(x["direction"] == "left_to_right" for x in doc["reactions"])
    for frame, acc, index, master in [
        ("ENTC-MONOMER", "P0AEJ2", 1, "18985"),
        ("ENTB-MONOMER", "P0ADI4", 2, "11112"),
        ("ENTA-MONOMER", "P15047", 1, "23824"),
    ]:
        native = etree.parse(str(RAW / f"metacyc-{frame}.xml")).find("Protein")
        assert native.xpath('./dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [acc]
        up = json.loads((RAW / f"uniprot-{acc}.json").read_text())
        assert up["primaryAccession"] == acc and up["organism"]["taxonId"] == 83333
        assert {"database": "Rhea", "id": "RHEA:" + master} in up["comments"][index]["reaction"][
            "reactionCrossReferences"
        ]
    for frame, component, coefficient in [
        ("ENTA-CPLX", "ENTA-MONOMER", 4),
        ("ENTB-CPLX", "HOLO-ENTB", 2),
    ]:
        p = etree.parse(str(RAW / f"metacyc-{frame}.xml")).find("Protein")
        assert p.find("component/Protein").get("frameid") == component
        assert int(p.findtext("component/coefficient")) == coefficient
    holo = etree.parse(str(RAW / "metacyc-HOLO-ENTB.xml")).find("Protein")
    assert holo.find("unmodified-form/Protein").get("frameid") == "ENTB-MONOMER"
    assert holo.find("component-of/Protein").get("frameid") == "ENTB-CPLX"
    for frame, enzyme, native in [
        ("ENTC-MONOMER", "ENTC-ENZRXN", "ISOCHORSYN-RXN"),
        ("ENTB-CPLX", "ISOCHORMAT-ENZRXN", "ISOCHORMAT-RXN"),
        ("ENTA-CPLX", "DHBDEHYD-ENZRXN", "DHBDEHYD-RXN"),
    ]:
        p = etree.parse(str(RAW / f"metacyc-{frame}.xml")).find("Protein")
        assert p.xpath(
            f'./catalyzes/Enzymatic-Reaction[@frameid="{enzyme}"]/reaction/Reaction/@frameid'
        ) == [native]
    for acc, index in [("P0AEJ2", 2), ("P0ADI4", 3)]:
        up = json.loads((RAW / f"uniprot-{acc}.json").read_text())
        assert (
            up["comments"][index]["cofactors"][0]["cofactorCrossReference"]["id"] == "CHEBI:18420"
        )
        assert (
            up["comments"][index]["cofactors"][0]["evidences"][0]["evidenceCode"] == "ECO:0000269"
        )
    assert all(
        not (e["subject"] == "UniProtKB:P15047" and e["predicate"] == "catalyzes")
        for e in doc["mechanistic_edges"]
    )
    assert "MetaCyc:HOLO-ENTB" in {p["id"] for p in doc["participants"]}
    assert "UniProtKB:P0ADI4" not in {p["id"] for p in doc["participants"]}
    archive = next(x for x in manifest["source_bodies"] if x.get("archive_path"))
    assert digest(archive["archive_path"]) == archive["archive_sha256"]
    with zipfile.ZipFile(archive["archive_path"]) as z:
        member = next(n for n in z.namelist() if n.endswith("PW000751.owl"))
        assert z.read(member) == (RAW / "PW000751.owl").read_bytes()
    kgx = render_kgx([record])
    exported = list(csv.DictReader(io.StringIO(kgx["edges.tsv"]), delimiter="\t"))
    nodes_out = list(csv.DictReader(io.StringIO(kgx["nodes.tsv"]), delimiter="\t"))
    assert len(exported) == len(edges) == 23
    assert len(nodes_out) == 20
    for before, after in zip(doc["mechanistic_edges"], exported, strict=True):
        assert before["subject"] == after["subject"] and before["object"] == after["object"]
        assert before.get("description", "") == after["description"]
        assert before["evidence"] == json.loads(after["evidence"])
        assert {x["id"] for x in json.loads(after["reference_metadata"])} == {
            x["reference_id"] for x in before["evidence"]
        }
    exported_nodes = {n["id"]: n for n in nodes_out}
    assert exported_nodes["MetaCyc:HOLO-ENTB"]["category"] == "biolink:Protein"
    for i in ["MetaCyc:ENTA-CPLX", "MetaCyc:ENTB-CPLX"]:
        assert exported_nodes[i]["category"] == "biolink:MacromolecularComplex"
    for participant in doc["participants"]:
        assert {"record_id": doc["id"], "collection": "participants", **participant} in json.loads(
            exported_nodes[participant["id"]]["source_contexts"]
        )
    print(
        json.dumps(
            {
                "status": "passed",
                "target": str(TARGET.relative_to(ROOT)),
                "target_sha256": target_hash,
                "checks": [
                    "native and closed schemas",
                    "all original hashes",
                    "all reference-body hashes",
                    "four canonical native HTML identities",
                    "original full RDF reaction/side/coefficient/compound replay",
                    "native directions and Rhea direction table",
                    "nine native compound ChEBI identity/InChI crosswalks",
                    "all three whole reactions atom/charge balanced",
                    "native complete boundary and all catalysts",
                    "three protein identity/activity crosswalks",
                    "exact holo component and tetramer assembly",
                    "reviewed Mg annotations",
                    "actual target KGX complete evidence/metadata/categories",
                ],
                "counts": {
                    "original_bodies": len(manifest["source_bodies"]),
                    "references": len(doc["references"]),
                    "rhea_sides": 11,
                    "balanced_reactions": len(totals),
                    "named_nodes": 20,
                    "edges": 23,
                    "evidence": sum(len(e["evidence"]) for e in doc["mechanistic_edges"]),
                },
                "balance_vectors": totals,
                "limits": [
                    "Author replay is not independent scientific review "
                    "or an experimental validation.",
                    "Full corpus gates are delegated to root.",
                    "Primary abstract and source-state limitations remain "
                    "in the curation dossier and edge evidence.",
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
