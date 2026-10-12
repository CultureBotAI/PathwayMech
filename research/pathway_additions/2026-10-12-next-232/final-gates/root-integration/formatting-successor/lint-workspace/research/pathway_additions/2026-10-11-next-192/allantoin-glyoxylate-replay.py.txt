"""Replay the complete PWY-5705 source projection against preserved originals.

External raw bodies are deliberately not repository fixtures. This checks exact
source/graph identity and balanced chemistry; it is not an independent scientific
review, an experimental validation, or a replacement for the corpus gates.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.util
import io
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path

import yaml
from lxml import etree

from pathwaymech.kgx import render_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path(__file__).resolve().parents[3]
DOSSIER = Path(__file__).parent
RAW = Path("/private/tmp/pathwaymech-next-192-evidence/allantoin")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml"
RH = "http://rdf.rhea-db.org/"
NS = {
    "rh": RH,
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}
RDF_RESOURCE = "{" + NS["rdf"] + "}resource"


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_json(name: str) -> dict:
    return json.loads((DOSSIER / name).read_text())


def main() -> None:
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert strict_errors([TARGET], ROOT) == []
    projection = read_json("allantoin-glyoxylate-source-projection.json")
    manifest = read_json("allantoin-glyoxylate-source-manifest.json")
    ids = read_json("allantoin-glyoxylate-identifiers.json")
    target_hash = digest(TARGET)
    for item in [projection, manifest, ids]:
        assert item["target_sha256"] == target_hash
    for item in manifest["source_bodies"]:
        assert digest(Path(item["raw_path"])) == item["sha256"], item["raw_path"]
    for ref in doc["references"]:
        assert digest(Path(manifest["reference_body_map"][ref["id"]])) == ref["source_sha256"]
    # Exact native page, using the production parser rather than a fabricated term.
    spec = importlib.util.spec_from_file_location(
        "source_builder", ROOT / "scripts/build_source_identifier_snapshot.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert list(module.metacyc_terms((RAW / "metacyc-PWY-5705.html").read_text())) == [
        ("MetaCyc:PWY-5705", "allantoin degradation to glyoxylate III", [])
    ]
    # Independently parse original RDF descriptions referenced by the source projection.
    original = gzip.open(CACHE / "rhea.rdf.gz", "rt").read()
    wanted = {
        RH + x for x in ["17029", "17030", "27485", "27486", "25241", "25242", "11304", "11305"]
    }
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
    native_to_chebi = {}
    for frame, item in projection["compound_crosswalks"].items():
        compound = etree.parse(item["raw_path"]).find("Compound")
        assert compound.get("frameid") == frame
        assert compound.xpath('./dblink[dblink-db="CHEBI"]/dblink-oid/text()') == [
            item["curie"].split(":")[1]
        ]
        assert compound.findtext("inchi") == chemistry[item["curie"]]["chemrof:inchi_string"]
        native_to_chebi[frame] = item["curie"]
    for reaction in projection["reactions"]:
        element = etree.parse(reaction["raw_path"]).find("Reaction")
        assert element.get("frameid") == reaction["native_id"].split(":", 1)[1]
        assert element.findtext("reaction-direction") == "LEFT-TO-RIGHT"
        assert (
            element.xpath('./dblink[dblink-db="RHEA"]/dblink-oid/text()')
            == reaction["native_rhea_xrefs"]
        )
        for side, rhea_side in [("left", "substrates"), ("right", "products")]:
            native = Counter()
            for part in element.findall(side):
                native[native_to_chebi[part[0].get("frameid")]] += int(
                    part.findtext("coefficient", "1")
                )
            selected = Counter(
                {
                    s["curie"]: s["coefficient"]
                    for s in projection["rhea_side_projection"]
                    if "RHEA:" + s["directed"] == reaction["selected_reaction"]
                    and s["side"] == rhea_side
                }
            )
            assert native == selected
    p = etree.parse(str(RAW / "metacyc-PWY-5705.xml")).find("Pathway")
    assert set(p.xpath("./reaction-list/*/@frameid")) == {"PWY-5698", "UREIDOGLYCOLATE-LYASE-RXN"}
    p = etree.parse(str(RAW / "metacyc-PWY-5698.xml")).find("Pathway")
    assert set(p.xpath("./reaction-list/*/@frameid")) == {
        "ALLANTOINASE-RXN",
        "ALLANTOATE-DEIMINASE-RXN",
        "URUR-RXN",
    }
    for assembly in projection["assemblies"]:
        frame = assembly["complex_id"].split(":")[1]
        p = etree.parse(str(RAW / f"metacyc-{frame}.xml")).find("Protein")
        assert p.find("component/Protein").get("frameid") == assembly["component_frame"]
        assert int(p.findtext("component/coefficient")) == assembly["coefficient"]
        acc = assembly["uniprot"].split(":")[1]
        up = json.loads((RAW / f"uniprot-{acc}.json").read_text())
        assert any(
            x["id"].endswith(":" + assembly["component_frame"])
            for x in up["uniProtKBCrossReferences"]
            if x["database"] == "BioCyc"
        )
    for acc, master in [
        ("P77671", "17029"),
        ("P77425", "27485"),
        ("P75713", "25241"),
        ("P77731", "11304"),
    ]:
        up = json.loads((RAW / f"uniprot-{acc}.json").read_text())
        assert up["primaryAccession"] == acc and up["organism"]["taxonId"] == 83333
        assert {"database": "Rhea", "id": "RHEA:" + master} in up["comments"][1]["reaction"][
            "reactionCrossReferences"
        ]
    alla = json.loads((RAW / "uniprot-P77731.json").read_text())
    assert alla["comments"][4]["texts"][0]["value"] == "Homodimer"
    assert alla["comments"][2]["cofactors"][0]["cofactorCrossReference"]["id"] == "CHEBI:49786"
    # Native AllA is a gene product; qualified enables preserves role without a fake complex.
    assert (
        len(
            [
                e
                for e in doc["mechanistic_edges"]
                if e["subject"] == "UniProtKB:P77731"
                and e["predicate"] == "enables"
                and e["object"] == "RHEA:11305"
            ]
        )
        == 1
    )
    assert not any(
        e["subject"] == "UniProtKB:P77731" and e["predicate"] == "catalyzes"
        for e in doc["mechanistic_edges"]
    )
    kgx = render_kgx([record])
    exported = list(csv.DictReader(io.StringIO(kgx["edges.tsv"]), delimiter="\t"))
    nodes_out = list(csv.DictReader(io.StringIO(kgx["nodes.tsv"]), delimiter="\t"))
    assert len(exported) == len(edges) == 41
    assert len(nodes_out) == 27
    exported_nodes = {n["id"]: n for n in nodes_out}
    for participant in doc["participants"]:
        node = exported_nodes[participant["id"]]
        assert node["source_category"] == participant["category"]
        contexts = json.loads(node["source_contexts"])
        assert {"record_id": doc["id"], "collection": "participants", **participant} in contexts
    for curie in ["MetaCyc:CPLX-64", "MetaCyc:CPLX-7524"]:
        assert exported_nodes[curie]["category"] == "biolink:MacromolecularComplex"
    assert exported_nodes["UniProtKB:P77731"]["category"] == "biolink:Protein"
    for reaction in doc["reactions"]:
        assert exported_nodes[reaction["id"]]["direction"] == "left_to_right"
    for before, after in zip(doc["mechanistic_edges"], exported, strict=True):
        assert before["subject"] == after["subject"] and before["object"] == after["object"]
        assert before["description"] == after["description"]
        assert before["evidence"] == json.loads(after["evidence"])
        metadata = json.loads(after["reference_metadata"])
        assert {x["id"] for x in metadata} == {x["reference_id"] for x in before["evidence"]}
    print(
        json.dumps(
            {
                "status": "passed",
                "target": str(TARGET.relative_to(ROOT)),
                "target_sha256": target_hash,
                "counts": {
                    "native_reactions": 4,
                    "rhea_sides": 17,
                    "balanced_reactions": len(totals),
                    "native_compound_crosswalks": 10,
                    "named_nodes": 27,
                    "edges": len(edges),
                    "evidence": sum(len(e["evidence"]) for e in edges.values()),
                    "reference_bodies": len(doc["references"]),
                    "manifest_originals_rehashed": len(manifest["source_bodies"]),
                },
                "balance_vectors": totals,
                "limits": [
                    "Author replay against original sources; "
                    "independent scientific review remains separate.",
                    "Full corpus gates are delegated to root; no claim they ran in this command.",
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
