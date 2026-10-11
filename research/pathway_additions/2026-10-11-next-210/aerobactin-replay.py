"""Offline author checks of authentic sources; this is not an independent review."""

from __future__ import annotations

import collections
import copy
import csv
import gzip
import hashlib
import json
import re
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import etree as ET
from lxml import html

from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
REPO = Path("/private/tmp/pathwaymech-next-209-20261011")
SCOUT = Path("/private/tmp/pathwaymech-aerobactin-scout-20261011")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = OUT / "aerobactin-biosynthesis.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
STEPS = [
    ("1.14.13.59-RXN", "23229", "23228", "EMB09147.1", "IucD"),
    ("N6-HYDROXYLYSINE-O-ACETYLTRANSFERASE-RXN", "22389", "22388", "EMB09145.1", "IucB"),
    ("RXN-13054", "32164", "32163", "EMB09144.1", "IucA"),
    ("RXN-13056", "32168", "32167", "EMB09146.1", "IucC"),
]


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def sql_values(db, curie):
    with sqlite3.connect(f"file:{CACHE}/{db}.db?mode=ro", uri=True) as connection:
        return {
            p: v
            for p, v in connection.execute(
                "select predicate,value from statements where subject=?", (curie,)
            )
            if v is not None
        }


def rhea():
    masters = {r[2] for r in STEPS}
    directions = {}
    for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
        cells = line.split("\t")
        if cells[0] in masters:
            directions[cells[0]] = dict(zip(["master", "lr", "rl", "bi"], cells, strict=True))
    numbers = {v for row in directions.values() for v in row.values()}
    nodes, compounds = {}, {}
    with gzip.open(CACHE / "rhea.rdf.gz", "rb") as source:
        for _, e in ET.iterparse(source, events=("end",), tag=RDF + "Description"):
            uri = e.get(RDF + "about", "")
            name = uri.rsplit("/", 1)[-1]
            selected = name.split("_", 1)[0] in numbers or (
                name.startswith("Participant_") and name.split("_")[1] in numbers
            )
            dest = nodes if selected else compounds if name.startswith("Compound_") else None
            if dest is not None:
                for child in e:
                    key = ET.QName(child).localname
                    value = child.get(RDF + "resource") or (child.text or "").strip()
                    values = dest.setdefault(uri, {}).setdefault(key, [])
                    if value not in values:
                        values.append(value)
            e.clear()
            while e.getprevious() is not None:
                del e.getparent()[0]
    nodes.update(
        {
            u: row
            for u, row in compounds.items()
            if any(u in vs for row2 in nodes.values() for vs in row2.values())
        }
    )
    sides, balances = [], []
    net = collections.Counter()
    for _, rid, master, _, _ in STEPS:
        assert directions[master]["lr"] == rid
        assert RH + rid in nodes[RH + master]["directionalReaction"]
        bal = collections.Counter()
        for role in ["substrates", "products"]:
            side = nodes[RH + rid][role][0]
            sign = -1 if role == "substrates" else 1
            for pred, parts in nodes[side].items():
                if not re.fullmatch(r"contains\d+", pred):
                    continue
                coeff = int(pred[8:])
                for part in parts:
                    compound = nodes[part]["compound"][0]
                    cp = nodes[compound]
                    cid = cp["accession"][0]
                    assert cid.startswith("CHEBI:")
                    vals = sql_values("chebi", cid)
                    formula = cp["formula"][0]
                    charge = int(cp["charge"][0])
                    assert vals["chemrof:generalized_empirical_formula"] == formula
                    assert int(vals["chemrof:charge"]) == charge
                    tokens = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
                    assert "".join(a + b for a, b in tokens) == formula
                    for atom, count in tokens:
                        bal[atom] += sign * coeff * int(count or 1)
                    bal["charge"] += sign * coeff * charge
                    multiplier = 2 if rid in ["23229", "22389"] else 1
                    net[cid] += multiplier * sign * coeff
                    sides.append(
                        {
                            "reaction": "RHEA:" + rid,
                            "role": role,
                            "id": cid,
                            "coefficient": coeff,
                            "side": side,
                            "predicate": "rh:" + pred,
                            "participant": part,
                            "compound": compound,
                            "formula": formula,
                            "charge": charge,
                        }
                    )
        assert not {k: v for k, v in bal.items() if v}, (rid, bal)
        balances.append({"reaction": "RHEA:" + rid, "residual": {}})
    return nodes, sides, balances, {k: v for k, v in net.items() if v}


def graph_chemistry(doc, sides):
    chemical = [e for e in doc["mechanistic_edges"] if e["predicate"] in ["consumes", "produces"]]
    assert len(chemical) == len(sides) == 24
    for side in sides:
        pred = "consumes" if side["role"] == "substrates" else "produces"
        subj = side["id"] if pred == "consumes" else side["reaction"]
        obj = side["reaction"] if pred == "consumes" else side["id"]
        es = [
            e for e in chemical if (e["subject"], e["predicate"], e["object"]) == (subj, pred, obj)
        ]
        assert len(es) == 1, (subj, pred, obj)
        ev = es[0]["evidence"][0]
        assert ev["reference_id"] == side["reaction"]
        assert f"coefficient {side['coefficient']}" in ev["source_assertion"]
        assert all(
            side[k] in ev["source_locator"]
            for k in ["side", "predicate", "participant", "compound"]
        )
        if side["id"] == "CHEBI:63796":
            assert "unspecified" in es[0]["description"]
            assert "does not assert acceptance of the 3R" in es[0]["description"]
            assert {x["reference_id"] for x in es[0]["evidence"]} == {
                side["reaction"],
                "CHEBI:63796",
                "PMID:29618511",
            }


def native_checks(doc, paths):
    pathway = ET.parse(paths["MetaCyc:AEROBACTINSYN-PWY"]).getroot()[1]
    members = pathway.xpath("reaction-list/Reaction/@frameid")
    assert set(members) == {s[0] for s in STEPS} and len(members) == 4
    orderings = {
        (x.find("predecessor-reactions/Reaction").get("frameid"), x.find("Reaction").get("frameid"))
        for x in pathway.findall("reaction-ordering")
    }
    assert orderings == {(STEPS[i][0], STEPS[i + 1][0]) for i in range(3)}
    reactions = []
    for native, rid, _, _, _ in STEPS:
        rx = ET.parse(paths["MetaCyc:" + native]).getroot()[1]
        assert rx.get("frameid") == native
        assert rx.xpath('dblink[dblink-db="RHEA"]/dblink-oid/text()') == [rid]
        assert rx.xpath('dblink[dblink-db="RHEA"]/dblink-relationship/text()') == ["unification"]
        layout = pathway.xpath("reaction-layout[Reaction/@frameid=$n]", n=native)
        assert len(layout) == 1 and layout[0].findtext("direction") == "L2R"
        reactions.append(
            {
                "native": native,
                "rhea": "RHEA:" + rid,
                "left": rx.xpath("left/Compound/@frameid"),
                "right": rx.xpath("right/Compound/@frameid"),
                "source_direction": rx.findtext("reaction-direction"),
                "layout_direction": "L2R",
            }
        )
    compounds = []
    for frame, cid, root in [
        ("CPD-265", "CHEBI:57820", BASE / "originals"),
        ("CPD-961", "CHEBI:58122", BASE / "originals"),
        ("CPD-14069", "CHEBI:63796", SCOUT / "authority-agent-originals"),
        ("AEROBACTIN", "CHEBI:58396", SCOUT / "authority-agent-originals"),
    ]:
        n = ET.parse(str(root / (frame + ".xml"))).getroot()[1]
        assert cid.split(":")[1] in n.xpath('dblink[dblink-db="CHEBI"]/dblink-oid/text()')
        assert n.findtext("inchi") == sql_values("chebi", cid)["chemrof:inchi_string"]
        compounds.append(
            {
                "native": frame,
                "chebi": cid,
                "exact_original_inchi_equal": True,
                "stereo_scope": "lysine S fixed; citrate center unspecified"
                if frame == "CPD-14069"
                else "source InChI stereochemistry preserved",
            }
        )
    assert "/t9-,14?/m0/s1" in sql_values("chebi", "CHEBI:63796")["chemrof:inchi_string"]
    return {"members": members, "reaction_projections": reactions, "compound_bridges": compounds}


def identity_checks(doc):
    proteins = ET.parse(str(BASE / "originals/hvKP1-iuc-proteins.xml")).getroot()
    proteinmap = {p.findtext("GBSeq_accession-version"): p for p in proteins}
    contig = ET.parse(str(BASE / "originals/AOIZ01000119.1.xml")).getroot()[0]
    nt = contig.findtext("GBSeq_sequence").upper()
    # NCBI bacterial genetic code 11: ordinary residue assignments and initiator methionine.
    bases = "TCAG"
    amino = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = [a + b + c for a in bases for b in bases for c in bases]
    code = dict(zip(codons, amino, strict=True))
    bridges = []
    for feature in contig.findall("GBSeq_feature-table/GBFeature"):
        q = {
            x.findtext("GBQualifier_name"): x.findtext("GBQualifier_value")
            for x in feature.findall("GBFeature_quals/GBQualifier")
        }
        acc = q.get("protein_id")
        if acc not in proteinmap:
            continue
        assert q["transl_table"] == "11" and q["codon_start"] == "1"
        location = feature.findtext("GBFeature_location")
        match = re.fullmatch(r"(\d+)\.\.(\d+)", location)
        assert match
        a, b = map(int, match.groups())
        coding = nt[a - 1 : b]
        assert len(coding) % 3 == 0 and coding[:3] in ["ATG", "GTG", "TTG"]
        translated = "".join(code[coding[i : i + 3]] for i in range(0, len(coding), 3))
        assert translated.endswith("*") and "*" not in translated[:-1]
        translated = "M" + translated[1:-1]
        protein = proteinmap[acc]
        sequence = protein.findtext("GBSeq_sequence").upper()
        assert translated == q["translation"] == sequence
        source = protein.xpath('GBSeq_feature-table/GBFeature[GBFeature_key="source"]')[0]
        quals = {
            x.findtext("GBQualifier_name"): x.findtext("GBQualifier_value")
            for x in source.findall("GBFeature_quals/GBQualifier")
        }
        assert quals["strain"] == "hvKP1" and quals["db_xref"] == "taxon:1267897"
        node = next(p for p in doc["participants"] if p["id"] == "NCBIProtein:" + acc)
        assert node["label"] == protein.findtext("GBSeq_definition")
        bridges.append(
            {
                "accession": acc,
                "native_contig": "AOIZ01000119.1",
                "locus_tag": q["locus_tag"],
                "coding_location": location,
                "translation_table": 11,
                "residues": len(sequence),
                "protein_sha256": hashlib.sha256(sequence.encode()).hexdigest(),
                "native_DNA_translation_and_GenPept_agree": True,
                "taxon": "NCBITaxon:1267897",
                "scope": (
                    "native source gene; not a claim that every engineered assay construct "
                    "has this exact sequence"
                ),
            }
        )
    assert len(bridges) == 4
    return bridges


def section(pmc, identity):
    doc = html.parse(str(BASE / "originals" / (pmc + "-HTML.html")))
    return " ".join(doc.xpath("//*[@id=$i]", i=identity)[0].text_content().split())


def primary_checks(doc):
    assert "EMB09144.1" in section("PMC4928626", "sec2.1")
    assert "574" in section("PMC4928626", "sec2.1")
    active = section("PMC4928626", "sec3.2")
    assert "Mg2+" in active and "Gln427, Asn428, and Asp445" in active
    assert "tetramer" in section("PMC4928626", "sec3.3")
    assert "hvKP1 clinical isolate" in section("PMC5961048", "sec12")
    assert "E. coli BL21" in section("PMC5961048", "sec12")
    assert "all four purified IucA" in section("PMC5961048", "sec4")
    stereo = section("PMC5961048", "sec6")
    assert "3S,2′S" in stereo and "3R,2′S" in stereo
    assert "hLys was not detected" in section("PMC5961048", "sec10")
    assert "tetramer and dimer" in section("PMC5961048", "sec9")
    assert "artifactual consequence" in section("PMC5961048", "sec9")
    amp = section("PMC7325057", "P16")
    assert "AMP" in amp and "PPi" in amp
    assert "ATP, citrate, and ahLys binding sequentially" in section("PMC7325057", "P31")
    page = html.parse(str(SCOUT / "authority-agent-originals/iubmb-6.3.2.38.html"))
    txt = " ".join(page.getroot().text_content().split())
    assert "2 ATP" in txt and "2 ADP" in txt and "AMP-forming" in txt
    assert (
        "full sequences of all engineered constructs were not independently recovered"
        in doc["description"]
    )
    assert not any(
        e["predicate"] == "has_cofactor" and e["subject"] == "NCBIProtein:EMB09146.1"
        for e in doc["mechanistic_edges"]
    )
    mg = next(
        e
        for e in doc["mechanistic_edges"]
        if e["predicate"] == "has_cofactor" and e["subject"] == "NCBIProtein:EMB09144.1"
    )
    assert "sec3.2/p[1]" in mg["evidence"][0]["source_locator"]
    return {
        "2016": "Exact IucA native accession; measured tetramer; observed ATP-bound Mg site",
        "2018": (
            "Full hvKP1 gene-source route; measured citryl stereo; "
            "IucC preparation-dependent oligomers"
        ),
        "2020": "AMP/PPi assay and ordered IucA mechanism",
        "IUBMB_conflict": (
            "2 ATP/2 ADP reaction field retained as a disagreement, not selected chemistry"
        ),
        "engineered_construct_limit": (
            "Full exact construct sequences remain unrecovered; "
            "native accessions are not substituted for those sequences"
        ),
    }


def main():
    started = datetime.now(UTC).isoformat()
    targetsha = digest(TARGET)
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert not strict_errors([TARGET], REPO)
    projection = read(OUT / "aerobactin-source-projection.json")
    manifest = read(OUT / "aerobactin-source-manifest.json")
    hashes = {}
    for row in manifest["original_bodies"]:
        hashes[row["path"]] = digest(row["path"])
        assert hashes[row["path"]] == row["sha256"], row["path"]
    refs = {r["id"]: r for r in doc["references"]}
    for rid, path in projection["reference_original_paths"].items():
        assert hashes[path] == refs[rid]["source_sha256"], rid
    nodes, sides, balances, net = rhea()
    graph_chemistry(doc, sides)
    assert len(doc["reactions"]) == 4
    for rx in doc["reactions"]:
        assert rx["label"] == nodes[RH + rx["id"][5:]]["label"][0]
        assert rx["direction"] == "left_to_right"
    for participant in doc["participants"]:
        if participant["id"].startswith("CHEBI:"):
            assert participant["label"] == sql_values("chebi", participant["id"])["rdfs:label"]
    assert doc["label"] == sql_values("go", doc["id"])["rdfs:label"]
    assert doc["taxa"][0]["label"] == sql_values("ncbitaxon", "NCBITaxon:1267897")["rdfs:label"]
    assert set(net) == {
        "CHEBI:32551",
        "CHEBI:57783",
        "CHEBI:15379",
        "CHEBI:58349",
        "CHEBI:15377",
        "CHEBI:57288",
        "CHEBI:57287",
        "CHEBI:16947",
        "CHEBI:30616",
        "CHEBI:456215",
        "CHEBI:33019",
        "CHEBI:15378",
        "CHEBI:58396",
    }
    native = native_checks(doc, projection["reference_original_paths"])
    proteins = identity_checks(doc)
    primaries = primary_checks(doc)
    # A wrong ATP coproduct and an unqualified stereo class must be caught.
    mutations = []
    for kind in ["wrong_coproduct", "missing_stereo_limit"]:
        bad = copy.deepcopy(doc)
        if kind == "wrong_coproduct":
            e = next(
                e
                for e in bad["mechanistic_edges"]
                if e["subject"] == "RHEA:32164"
                and e["predicate"] == "produces"
                and e["object"] == "CHEBI:456215"
            )
            e["object"] = "CHEBI:456216"
        else:
            e = next(e for e in bad["mechanistic_edges"] if e["object"] == "CHEBI:63796")
            e["description"] = "This node is the exact experimentally proven stereoisomer."
        try:
            graph_chemistry(bad, sides)
        except AssertionError:
            mutations.append(kind)
        else:
            raise AssertionError("Source guard accepted " + kind)
    exported = BASE / "kgx"
    paths = write_kgx([record], exported)
    rows = list(csv.DictReader((exported / "edges.tsv").open(), delimiter="\t"))
    node_rows = list(csv.DictReader((exported / "nodes.tsv").open(), delimiter="\t"))
    assert len(rows) == len(doc["mechanistic_edges"]) == 43
    for edge, row in zip(doc["mechanistic_edges"], rows, strict=True):
        assert (row["subject"], row["predicate"], row["object"]) == (
            edge["subject"],
            LOCAL_PREDICATE_CURIES[edge["predicate"]],
            edge["object"],
        )
        assert json.loads(row["evidence"]) == edge["evidence"]
        assert row["description"] == edge.get("description", "")
        assert json.loads(row["reference_metadata"]) == [
            refs[k] for k in sorted({e["reference_id"] for e in edge["evidence"]})
        ]
    assert len(node_rows) == 28
    assert sum(len(e["evidence"]) for e in doc["mechanistic_edges"]) == 75
    assert projection["graph_to_source"] == [
        {
            "edge_id": e["id"],
            "subject": e["subject"],
            "predicate": e["predicate"],
            "object": e["object"],
            "evidence": e["evidence"],
        }
        for e in doc["mechanistic_edges"]
    ]
    assert digest(TARGET) == targetsha == projection["record_sha256"]
    save(
        "aerobactin-original-source-audit.json",
        {
            "native": native,
            "proteins": proteins,
            "rhea_sides": sides,
            "balances": balances,
            "weighted_net_2_2_1_1": net,
            "primary_source_checks": primaries,
            "negative_source_guards_reject": mutations,
        },
    )
    save(
        "aerobactin-validation.json",
        {
            "status": "passed",
            "started_at": started,
            "finished_at": datetime.now(UTC).isoformat(),
            "target_sha256": targetsha,
            "scope": (
                "Author offline original-source/schema/export replay. "
                "No independent review or global corpus approval."
            ),
            "source_bodies_rehashed": len(hashes),
            "references_rehashed": len(refs),
            "native_reactions": 4,
            "rhea_sides": len(sides),
            "balanced_reactions": len(balances),
            "native_CDS_translations_verified": len(proteins),
            "compound_InChI_bridges": 4,
            "node_count": len(node_rows),
            "edge_count": len(rows),
            "evidence_count": 75,
            "native_and_closed_schemas": "passed",
            "canonical_labels_from_original_authorities": "passed",
            "kgx_files": [{"path": str(p), "sha256": digest(p)} for p in paths],
            "global_gates": "not run; external draft is not integrated in the corpus",
            "issuing_authority_snapshot_integration": "pending root in next owned worktree",
        },
    )
    print(json.dumps(read(OUT / "aerobactin-validation.json"), indent=2))


if __name__ == "__main__":
    main()
