"""Offline author replay of original sources for the complete PWY-5744 record.

This is an author check, not an independent scientific review. PCS primary text
was inspected through a web renderer; its unavailable original body is excluded
from byte-content claims. Generic protein states have only scaffold balances.
"""

from __future__ import annotations

import collections
import csv
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as XML
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import etree as ET
from lxml import html

from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-206"
RAW = Path("/private/tmp/pathwaymech-next-206-evidence/glyoxylate")
SHARED = RAW.parent / "three-hydroxypropionate"
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/glyoxylate-assimilation.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
SELECTED = [
    "10750",
    "13502",
    "54729",
    "26448",
    "26440",
    "26535",
    "26519",
    "26456",
    "38261",
    "38264",
    "38268",
    "38273",
    "22613",
]
MASTERS = {
    "10748",
    "13501",
    "54728",
    "26446",
    "26438",
    "26534",
    "26518",
    "26454",
    "22612",
    "38259",
    "38263",
    "38267",
    "38271",
}


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for b in iter(lambda: stream.read(1048576), b""):
            h.update(b)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def check_native_hydration_assertion(doc, projection):
    """Keep the no-Rhea-xref hydration and carrier-transfer objects distinct."""
    source = ET.parse(projection["reference_original_paths"]["MetaCyc:RXN-8965"]).getroot()[1]
    assert source.xpath("left/Compound/@frameid") == ["CPD-627"]
    assert source.xpath("right/Compound/@frameid") == ["CPD-14205", "WATER"]
    assert source.findtext("reaction-direction") == "RIGHT-TO-LEFT"
    edge = next(e for e in doc["mechanistic_edges"] if e["id"] == "glyox-edge-066")
    assert edge["object"] == "RHEA:38273"
    evidence = edge["evidence"][1]
    assert evidence["reference_id"] == "MetaCyc:RXN-8965"
    for fact in ["CPD-627", "CPD-14205", "WATER", "RIGHT-TO-LEFT", "hydration"]:
        assert fact in evidence["source_assertion"], fact
    assert "carboxybiotin" not in evidence["source_assertion"]
    assert "reaction-direction" in evidence["source_locator"]
    transfer = [
        ev
        for e in doc["mechanistic_edges"]
        for ev in e["evidence"]
        if ev["reference_id"] == "MetaCyc:RXN0-5055"
    ]
    assert len(transfer) == 1
    assert "carboxybiotin" in transfer[0]["source_assertion"]
    assert "acetyl-CoA" in transfer[0]["source_assertion"]
    return {
        "native_hydration": "RXN-8965 right-to-left CPD-14205 + WATER -> CPD-627",
        "distinct_transfer": "RXN0-5055 retains its separately sourced carrier-transfer assertion",
    }


def rhea():
    directions = {}
    for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
        cells = line.split("\t")
        if cells[0] in MASTERS:
            directions[cells[0]] = dict(zip(["master", "lr", "rl", "bi"], cells, strict=True))
    assert len(directions) == 13
    numbers = {n for row in directions.values() for n in row.values()}
    nodes, compounds = {}, {}
    with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
        for _, element in ET.iterparse(stream, events=("end",), tag=RDF + "Description"):
            uri = element.get(RDF + "about", "")
            name = uri.rsplit("/", 1)[-1]
            chosen = name.split("_", 1)[0] in numbers or (
                name.startswith("Participant_") and name.split("_")[1] in numbers
            )
            dest = nodes if chosen else compounds if name.startswith("Compound_") else None
            if dest is not None:
                for child in element:
                    key = ET.QName(child).localname
                    value = child.get(RDF + "resource") or (child.text or "").strip()
                    values = dest.setdefault(uri, {}).setdefault(key, [])
                    if value not in values:
                        values.append(value)
            element.clear()
            while element.getprevious() is not None:
                del element.getparent()[0]
    needed = {v for row in nodes.values() for vs in row.values() for v in vs if v in compounds}
    while True:
        extra = {v for u in needed for vs in compounds[u].values() for v in vs if v in compounds}
        if extra <= needed:
            break
        needed |= extra
    nodes.update({u: compounds[u] for u in needed})
    sides, balances = [], []
    net = collections.Counter()
    db = sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True)
    for rid in SELECTED:
        balance = collections.Counter()
        scope = "exact_small_molecule_equation"
        for role in ["substrates", "products"]:
            side = nodes[RH + rid][role][0]
            for pred, participants in nodes[side].items():
                if not re.fullmatch(r"contains\d+", pred):
                    continue
                coeff = int(pred[8:])
                sign = -1 if role == "substrates" else 1
                for part in participants:
                    cp = nodes[nodes[part]["compound"][0]]
                    cid = cp["accession"][0].replace("GENERIC:", "RHEA-COMP:")
                    formula_cp = cp
                    if cid.startswith("RHEA-COMP:"):
                        formula_cp = nodes[cp["reactivePart"][0]]
                        scope = (
                            "formal_reactive_part_balance_with_unchanged_protein_scaffold_"
                            "not_whole_protein_formula"
                        )
                    vals = {
                        p: v
                        for p, v in db.execute(
                            "select predicate,value from statements where subject=?",
                            (
                                formula_cp.get(
                                    "accession",
                                    [formula_cp["chebi"][0].rsplit("/", 1)[-1].replace("_", ":")],
                                )[0],
                            ),
                        )
                        if v is not None
                    }
                    assert vals["chemrof:generalized_empirical_formula"] == formula_cp["formula"][0]
                    assert vals["chemrof:charge"] == formula_cp["charge"][0]
                    assert vals.get("owl:deprecated") not in ["true", True]
                    formula = formula_cp["formula"][0]
                    tokens = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
                    assert "".join(a + b for a, b in tokens) == formula
                    for a, b in tokens:
                        balance[a] += sign * coeff * int(b or 1)
                    balance["charge"] += sign * coeff * int(formula_cp["charge"][0])
                    net[cid] += sign * coeff
                    sides.append(
                        {
                            "reaction": rid,
                            "role": role,
                            "id": cid,
                            "coefficient": coeff,
                            "side": side,
                            "participant": part,
                            "compound": nodes[part]["compound"][0],
                        }
                    )
        assert not {k: v for k, v in balance.items() if v}, (rid, balance)
        balances.append({"reaction": rid, "scope": scope, "residual": dict(balance)})
    return directions, nodes, sides, balances, {k: v for k, v in net.items() if v}


def pointer(obj, path):
    for key in path.strip("/").split("/"):
        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
    return obj


def main():
    start = datetime.now(UTC).isoformat()
    original_hash = digest(TARGET)
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert not strict_errors([TARGET], ROOT)
    projection = read(DOSSIER / "glyoxylate-source-projection.json")
    manifest = read(DOSSIER / "glyoxylate-source-manifest.json")
    coverage = read(DOSSIER / "glyoxylate-native-coverage.json")
    for src in manifest["original_bodies"]:
        assert digest(src["path"]) == src["sha256"], src["path"]
    refs = {r["id"]: r for r in doc["references"]}
    for rid, p in projection["reference_original_paths"].items():
        assert digest(p) == refs[rid]["source_sha256"], rid
    assert [r["id"] for r in doc["references"] if "source_sha256" not in r] == ["PMID:11821399"]
    assert all(projection["source_to_graph_coverage"].keys())
    directions, nodes, sides, balances, net = rhea()
    assert net == {
        "CHEBI:16526": -1,
        "CHEBI:30616": -2,
        "CHEBI:456216": 1,
        "CHEBI:43474": 1,
        "CHEBI:15378": -1,
        "CHEBI:57783": -3,
        "CHEBI:58349": 3,
        "CHEBI:456215": 1,
        "CHEBI:33019": 1,
        "CHEBI:36655": -1,
        "CHEBI:15361": 1,
    }, net
    assert {r["id"] for r in doc["reactions"]} == {"RHEA:" + r for r in SELECTED}
    for rx in doc["reactions"]:
        rid = rx["id"].split(":")[1]
        family = next(v for v in directions.values() if rid in v.values())
        assert rx["direction"] == ("left_to_right" if rid == family["lr"] else "right_to_left")
        assert RH + rid in nodes[RH + family["master"]]["directionalReaction"]
        assert rx["label"] == nodes[RH + rid]["label"][0]
        assert rx.get("category") == (None if rid == "10750" else "molecular_activity")
    chemical_edges = [
        e for e in doc["mechanistic_edges"] if e["predicate"] in ["consumes", "produces"]
    ]
    assert len(chemical_edges) == len(sides)
    for s in sides:
        rid = "RHEA:" + s["reaction"]
        pred = "consumes" if s["role"] == "substrates" else "produces"
        subj = s["id"] if pred == "consumes" else rid
        obj = rid if pred == "consumes" else s["id"]
        es = [
            e
            for e in chemical_edges
            if (e["subject"], e["predicate"], e["object"]) == (subj, pred, obj)
        ]
        assert len(es) == 1
        evidence = es[0]["evidence"][0]
        assert evidence["reference_id"] == rid
        assert f"coefficient {s['coefficient']}" in evidence["source_assertion"]
        assert (
            s["participant"] in evidence["source_locator"]
            and s["compound"] in evidence["source_locator"]
        )
    pw = ET.parse(projection["reference_original_paths"][doc["id"]]).getroot()[1]
    members = pw.xpath("reaction-list/Reaction/@frameid")
    assert len(members) == 13 and set(members) == set(projection["native_members"])
    for row in coverage["selected"]:
        source = ET.parse(projection["reference_original_paths"][row["native_id"]]).getroot()[1]
        assert source.get("frameid") == row["native_id"].split(":")[1]
        assert source.findtext("reaction-direction") == row["native_direction"]
        assert (
            source.xpath('dblink[dblink-db="RHEA"]/dblink-oid/text()') == row["native_rhea_xrefs"]
        )
        if row["native_rhea_xrefs"]:
            assert set(row["native_rhea_xrefs"]) <= set(row["master"].values())
        for role in ["left", "right"]:
            actual = [
                {"id": c.get("frameid"), "coefficient": side.findtext("coefficient") or "1"}
                for side in source.findall(role)
                for c in side
                if c.tag in ["Compound", "Protein"]
            ]
            assert actual == row[role]
    native_assertion_guard = check_native_hydration_assertion(doc, projection)
    # The actual archived review target reproduces the defect and must fail this guard.
    previous = yaml.safe_load(
        (
            DOSSIER / "initial-review-inputs/blobs/"
            "b28136c61fae7fcf2b9673d176e74d0c001b6cfedeab652ba75ab4ac01aa01e5-"
            "glyoxylate-assimilation.yaml.txt"
        ).read_text()
    )
    try:
        check_native_hydration_assertion(previous, projection)
    except AssertionError:
        native_assertion_guard["archived_wrong_assertion_rejected"] = True
    else:
        raise AssertionError("Archived RXN-8965 copy error was not rejected")
    db = sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True)
    for b in coverage["chemical_bridges"]:
        frame = b["native_id"].split(":")[1]
        source = ET.parse(str(RAW / (frame + ".xml"))).getroot()[1]
        if b["selected_id"].startswith("RHEA-COMP:"):
            assert "dimers" in frame and source.get("class") == "true"
            continue
        actual = source.findtext("inchi")
        current = db.execute(
            "select value from statements where subject=? and predicate='chemrof:inchi_string'",
            [b["selected_id"]],
        ).fetchone()[0]
        assert actual == b["native_inchi"] and current == b["current_inchi"]
        if b["disposition"] == "exact_original_InChI_match":
            assert actual == current
        else:
            assert actual != current and frame in ["CPD-9409", "CPD-627"]
    assert (
        sum(b["disposition"] == "exact_original_InChI_match" for b in coverage["chemical_bridges"])
        == 23
    )
    # All structured UniProt path prefixes resolve in their own actual original body.
    pointers = 0
    for e in doc["mechanistic_edges"]:
        for v in e["evidence"]:
            if v["reference_id"].startswith("UniProtKB:"):
                body = read(projection["reference_original_paths"][v["reference_id"]])
                for p in re.findall(
                    r"/[A-Za-z_][A-Za-z_0-9]*(?:/[A-Za-z_0-9]+)*", v["source_locator"]
                ):
                    pointer(body, p)
                    pointers += 1
    ncbi = XML.parse(RAW / "AAL47820.2.xml")
    seq = ncbi.findtext(".//GBSeq_sequence").upper()
    assert seq == read(RAW / "uniprot-Q8VRG6.json")["sequence"]["value"] and len(seq) == 1822
    assert ncbi.findtext(".//GBSeq_accession-version") == "AAL47820.2"
    assert (
        read(SHARED / "uniprot-S5N020.json")["sequence"]["value"]
        == read(SHARED / "uniprot-A9WC35.json")["sequence"]["value"]
    )
    assert (
        read(SHARED / "uniprot-Q6QQP7.json")["sequence"]["value"]
        != read(SHARED / "uniprot-A9WIU3.json")["sequence"]["value"]
    )
    assemblies = []
    for complex_id, mon, up, n in [
        ("CPLX-7549", "MONOMER-13604", "S5N020", 6),
        ("CPLX-7550", "MONOMER-13606", "Q6QQP7", 2),
        ("CPLX-8468", "MONOMER-17292", "A9WC34", 2),
        ("CPLX-8466", "MONOMER-17293", "A9WC36", 2),
        ("CPLX-8467", "MONOMER-17294", "A9WC41", 2),
    ]:
        native = ET.parse(
            projection["reference_original_paths"]["MetaCyc:" + complex_id]
        ).getroot()[1]
        component = native.xpath("component[Protein/@frameid=$m]", m=mon)
        assert len(component) == 1
        coeff = component[0].findtext("coefficient") or "1"
        assert int(coeff) == n
        assert any(
            e["subject"] == "MetaCyc:" + complex_id
            and e["predicate"] == "has_part"
            and e["object"] == "UniProtKB:" + up
            for e in doc["mechanistic_edges"]
        )
        assemblies.append(
            {
                "complex": complex_id,
                "component": mon,
                "selected_protein": up,
                "native_copies": n,
                "scope": (
                    "Exact sequence bridges or explicit primary-linked "
                    "species-level strain limits retained in record"
                ),
            }
        )
    # Important exact primary locations inspected during authorship must actually exist.
    primary_checks = {
        "PMID:19955419": ["sec3", "sec4", "sec5", "sec6", "sec15", "F1", "F4"],
        "PMID:18065535": ["sec28", "sec38"],
        "PMID:11948153": ["sec2", "sec21", "sec23", "sec27", "sec28", "sec29"],
        "PMID:38572988": ["s2-1", "s2-2", "s2-3", "s2-4", "s4-1", "s4-8"],
        "PMID:24206647": ["T1", "sec6", "sec9", "sec18"],
    }
    for rid, ids in primary_checks.items():
        body = html.fromstring(Path(projection["reference_original_paths"][rid]).read_bytes())
        for sid in ids:
            assert body.get_element_by_id(sid) is not None
    xml = ET.parse(projection["reference_original_paths"]["PMID:36535006"])
    for sid in ["notes-3", "sec2.2", "sec3.1", "sec3.2", "sec3.3"]:
        assert xml.xpath("//*[@id=$i]", i=sid)
    export = Path("/private/tmp/pathwaymech-next-206-glyoxylate-kgx")
    export.mkdir(exist_ok=True)
    paths = write_kgx([record], export)
    rows = list(csv.DictReader((export / "edges.tsv").open(), delimiter="\t"))
    node_rows = list(csv.DictReader((export / "nodes.tsv").open(), delimiter="\t"))
    assert len(rows) == len(doc["mechanistic_edges"]) == 107
    for original, out in zip(doc["mechanistic_edges"], rows, strict=True):
        assert (out["subject"], out["predicate"], out["object"]) == (
            original["subject"],
            LOCAL_PREDICATE_CURIES[original["predicate"]],
            original["object"],
        )
        assert json.loads(out["evidence"]) == original["evidence"]
        assert {r["id"] for r in json.loads(out["reference_metadata"])} == {
            v["reference_id"] for v in original["evidence"]
        }
    assert len(node_rows) == 62
    assert (
        next(n for n in node_rows if n["id"] == "RHEA:10750")["category"]
        == "biolink:BiochemicalReaction"
    )
    assert not any(
        e["object"] == "RHEA:10750" and e["predicate"] in ["catalyzes", "enables"]
        for e in doc["mechanistic_edges"]
    )
    assert digest(TARGET) == original_hash
    result = {
        "status": "passed",
        "scope": "Author original-source and schema/export replay; not independent review",
        "started_at": start,
        "finished_at": datetime.now(UTC).isoformat(),
        "target": str(TARGET.relative_to(ROOT)),
        "target_sha256": original_hash,
        "original_bodies_rehashed": len(manifest["original_bodies"]),
        "reference_digests_rehashed": len(projection["reference_original_paths"]),
        "primary_web_only_exclusion": ["PMID:11821399"],
        "native_member_count": len(members),
        "native_assertion_guard": native_assertion_guard,
        "rhea_sides_verified": len(sides),
        "balances": balances,
        "net": net,
        "native_chemical_dispositions": coverage["chemical_bridges"],
        "uniprot_pointers_resolved": pointers,
        "assemblies": assemblies,
        "native_schema": "passed",
        "closed_schema": "passed",
        "actual_kgx": {
            "nodes": len(node_rows),
            "edges": len(rows),
            "evidence": sum(len(e["evidence"]) for e in doc["mechanistic_edges"]),
            "files": [{"path": str(p), "sha256": digest(p)} for p in paths],
        },
        "limits": [
            (
                "11 exact small-molecule balances and 2 formal carrier-reactive-part balances; "
                "no whole protein empirical formula claim."
            ),
            (
                "PCS web-only primary body not byte-replayed; "
                "native and accession-version originals rehashed."
            ),
            (
                "CIP stereo adjudication separately executed through RDKit, original outputs "
                "and primary figure retained; this helper rechecks the exact compared InChI bytes."
            ),
            "No whole-corpus gate claim: parent performs rendering/full validation/tests.",
        ],
        "helper_sha256": digest(__file__),
    }
    (DOSSIER / "glyoxylate-validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "status": result["status"],
                "target_sha256": original_hash,
                "sides": len(sides),
                "balances": len(balances),
                "kgx": result["actual_kgx"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
