"""Offline sulfoquinovose author source replay; not an independent scientific review."""

from __future__ import annotations

import collections
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

from pathwaymech.kgx import EXPLICIT_CATEGORIES, LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-201"
RAW = Path("/private/tmp/pathwaymech-next-201-evidence/sulfoquinovose")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/sulfoquinovose-degradation-i.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
SELECTED = ["40440", "40444", "40516", "40513"]
MASTERS = {"40439", "40443", "40515", "40511"}
NATIVE = ["RXN-15296", "RXN-15297", "RXN-15298", "RXN-15299"]


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def native(frame):
    return ET.parse(str(RAW / f"{frame}.xml")).getroot()[1]


def rhea_extract():
    directions = {}
    for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
        cells = line.split("\t")
        if cells[0] in MASTERS:
            directions[cells[0]] = dict(
                zip(
                    ["master", "left_to_right", "right_to_left", "bidirectional"],
                    cells,
                    strict=True,
                )
            )
    numbers = {v for d in directions.values() for v in d.values()}
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
    needed = {v for d in nodes.values() for vs in d.values() for v in vs if v in compounds}
    nodes.update({uri: compounds[uri] for uri in needed})
    sides, balances, terms = [], [], {}
    with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as db:
        for rid in SELECTED:
            balance = collections.Counter()
            for role in ["substrates", "products"]:
                side = nodes[RH + rid][role][0]
                for predicate, participants in nodes[side].items():
                    if not re.fullmatch(r"contains\d+", predicate):
                        continue
                    coefficient = int(predicate[8:])
                    sign = -1 if role == "substrates" else 1
                    for participant in participants:
                        compound = nodes[participant]["compound"][0]
                        cp = nodes[compound]
                        cid = cp["accession"][0]
                        values = {
                            a: b if b is not None else c
                            for a, b, c in db.execute(
                                "select predicate,value,object from statements where subject=?",
                                (cid,),
                            )
                        }
                        terms[cid] = values
                        assert values.get("owl:deprecated") not in ["true", True]
                        assert values["chemrof:generalized_empirical_formula"] == cp["formula"][0]
                        assert values["chemrof:charge"] == cp["charge"][0]
                        formula = cp["formula"][0]
                        parts = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
                        assert "".join(a + b for a, b in parts) == formula
                        for atom, count in parts:
                            balance[atom] += sign * coefficient * int(count or 1)
                        balance["charge"] += sign * coefficient * int(cp["charge"][0])
                        sides.append(
                            dict(
                                reaction=rid,
                                role=role,
                                side=side,
                                predicate=predicate,
                                participant=participant,
                                compound=compound,
                                id=cid,
                                coefficient=coefficient,
                                label=values["rdfs:label"],
                                formula=formula,
                                charge=cp["charge"][0],
                            )
                        )
            assert all(v == 0 for v in balance.values()), (rid, balance)
            balances.append(dict(reaction=rid, residual=dict(balance), status="passed"))
    return dict(
        directions=directions,
        nodes=nodes,
        selected=SELECTED,
        sides=sides,
        balances=balances,
        terms=terms,
    )


def pointer(data, path):
    for key in path.strip("/").split("/"):
        data = data[int(key)] if isinstance(data, list) else data[key]
    return data


def source_checks(record, manifest, projection):
    refs = {r["id"]: r for r in record["references"]}
    sources = {s["reference_id"]: s for s in manifest["reference_sources"]}
    checks = []
    for edge in record["mechanistic_edges"]:
        for evidence in edge["evidence"]:
            rid = evidence["reference_id"]
            source = sources[rid]
            assert refs[rid]["source_sha256"] == source["sha256"] == digest(source["path"])
            loc = evidence["source_locator"]
            assert len(evidence["source_assertion"]) <= 400
            if rid.startswith("MetaCyc:"):
                tree = ET.parse(source["path"])
                first = loc.split(";")[0]
                assert tree.xpath(first), (edge["id"], first)
            elif rid.startswith("UniProtKB:"):
                data = read_json(source["path"])
                paths = re.findall(r"/comments/\d+(?:/[A-Za-z]+|/\d+)*", loc)
                assert paths
                for path in paths:
                    assert pointer(data, path) is not None, (edge["id"], path)
            elif rid == "PMID:33791429":
                tree = ET.parse(source["path"])
                first = loc.split(";")[0]
                assert tree.xpath(first), (edge["id"], first)
            elif source["path"].endswith(".json"):
                result = read_json(source["path"])["resultList"]["result"][0]
                assert result["id"] == rid[5:] and result["abstractText"]
            elif rid.startswith("RHEA:"):
                assert rid[5:] in projection["rhea"]["selected"]
            else:
                assert Path(source["path"]).read_bytes().startswith(b"%PDF")
            checks.append(dict(edge=edge["id"], reference_id=rid, source_locator=loc))
    return checks


def check_original_science(record):
    pathway = native("PWY-7446")
    members = pathway.xpath("reaction-list/Reaction/@frameid")
    assert set(members) == set(NATIVE) and len(members) == 4
    for i, frame in enumerate(NATIVE):
        reaction = native(frame)
        assert reaction.xpath('dblink[dblink-db="RHEA"]/dblink-oid/text()') == [SELECTED[i]]
        expected_direction = "RIGHT-TO-LEFT" if i == 3 else "LEFT-TO-RIGHT"
        assert reaction.findtext("reaction-direction") == expected_direction
        if i:
            assert pathway.xpath(
                "reaction-ordering[Reaction/@frameid=$down]/predecessor-reactions/"
                "Reaction[@frameid=$up]",
                down=frame,
                up=NATIVE[i - 1],
            )
    for complex_id, monomer, accession, coefficient, enzrxn, rxn in [
        ("CPLX0-7683", "EG11845-MONOMER", "P32140", "6", "ENZRXN0-7820", "RXN-15296"),
        ("CPLX0-7794", "EG11847-MONOMER", "P0A9V8", "4", "ENZRXN0-7824", "RXN-15299"),
    ]:
        assembly = native(complex_id)
        assert assembly.xpath(
            "component[Protein/@frameid=$monomer]/coefficient/text()", monomer=monomer
        ) == [coefficient]
        assert assembly.xpath(
            "catalyzes/Enzymatic-Reaction[@frameid=$e]/reaction/Reaction/@frameid", e=enzrxn
        ) == [rxn]
        assert native(monomer).xpath('dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [accession]
    # Current source-specific activities are separate from old native prose and generic classes.
    for accession, rid in zip(["P32140", "P32143", "P32141", "P0A9V8"], SELECTED, strict=True):
        protein = read_json(RAW / f"uniprot-{accession}.json")
        assert protein["organism"]["taxonId"] == 83333
        assert (
            protein["comments"][1]["physiologicalReactions"][0]["reactionCrossReference"]["id"]
            == "RHEA:" + rid
        )
    assert native("RXN-15298").xpath('right/Compound[@frameid="CPD-18717"]')
    assert "(2R)" in native("EG11846-MONOMER").findtext("comment")
    assert "/m1/" in native("CPD-16503").findtext("inchi")
    assert "/m0/" in native("CPD-18718").findtext("inchi")
    # Primary 2021 preparation/species distinctions; paragraph numbers are counted in original JATS.
    tree = ET.parse(str(RAW / "PMC8006165.xml"))

    def text(section, paragraph):
        return " ".join(
            "".join(tree.xpath("//sec[@id=$s]/p", s=section)[paragraph - 1].itertext()).split()
        )

    assay = text("sec2.4", 1)
    assert "could not detect" in assay and "E. coli" in assay and "Salmonella enterica" in assay
    assert "coupled system" in assay
    regulator = text("sec2.3", 1)
    for term in ["ADP", "SQ", "SLA", "DHAP", "F6P", "FBP", "PEP", "citrate"]:
        assert term in regulator
    assert "0.3 mM" in regulator and "substrate inhibition" in regulator
    assert "penta-hydrated Mg" in text("sec2.3", 6)
    supplement = (RAW / "Sharma2021-SI.txt").read_text()
    pages = supplement.split("\f")
    assert "Figure S19. Purification and properties of SeYihT" in pages[18]
    assert "127 kDa" in pages[18] and "99%" in pages[18]
    assert "Crystallographic tetramer of E. coli YihT and S. enterica YihT" in pages[19]
    assert "Figure S9. Purification and properties of EcYihV" in pages[9]
    sequences = []
    for title, accession, next_title, tail in [
        ("EcYihS wild-type", "P32140", "EcYihV wild-type", "LEHHHHHH"),
        ("EcYihV wild-type", "P32143", "EcYihT wild-type", "LEHHHHHH"),
        ("EcYihT wild-type", "P32141", "SeYihT wild-type", "LE"),
    ]:
        segment = supplement.split(title)[1].split(next_title)[0]
        sequence = "".join(re.findall(r"^([A-Z]{6,})[ \t]*$", segment, re.M))
        authoritative = read_json(RAW / f"uniprot-{accession}.json")["sequence"]["value"]
        assert sequence == authoritative + tail
        sequences.append(
            dict(accession=accession, matched_native_length=len(authoritative), construct_tail=tail)
        )
    yihu = (RAW / "Sharma2020.txt").read_text()
    assert "modelling of the natural isomer S-DHPS" in " ".join(yihu.split())
    assert "assuming that L-SLA was not a substrate" in " ".join(yihu.split())
    # Figure 1A S-SLA label was visually inspected, not recovered by PDF text extraction.
    assert "tetramer in solution" in " ".join(yihu.split())
    # Issue366: the claimed gel-shift result is p1, while AFM is p3.
    sr_edge = next(e for e in record["mechanistic_edges"] if e["id"] == "sulfoquinovose-edge-032")
    sr_locator = sr_edge["evidence"][0]["source_locator"]
    sr_tree = ET.parse(str(RAW / "PMC8006165.xml"))
    selected = sr_tree.xpath(sr_locator)
    original = sr_tree.xpath('//sec[@id="sec2.2"]/p')
    assert selected == original[:3]
    assert "gel-shift assay" in " ".join("".join(selected[0].itertext()).split())
    assert "temperature unfolding assay" in " ".join("".join(selected[1].itertext()).split())
    assert "atomic force microscopy" in " ".join("".join(selected[2].itertext()).split())
    assert "lower potency than SQ" in " ".join("".join(selected[2].itertext()).split())
    return dict(
        native_members=members,
        primary_construct_sequences=sequences,
        stereochemistry=(
            "Current (2S) structures retained; old native (2R) comment excluded. "
            "Original 2020 Figure 1A visually inspected separately."
        ),
    )


def run():
    started = datetime.now(UTC).isoformat()
    record = yaml.safe_load(TARGET.read_text())
    manifest = read_json(DOSSIER / "sulfoquinovose-source-manifest.json")
    projection = read_json(DOSSIER / "sulfoquinovose-source-projection.json")
    target_hash = digest(TARGET)
    assert manifest["target_sha256"] == projection["target_sha256"] == target_hash
    validated = validate_record(record)
    errors = strict_errors([TARGET], ROOT)
    assert not errors, errors
    for source in manifest["body_sources"]:
        assert digest(source["raw_path"]) == source["sha256"], source["raw_path"]
    # Hash selected chemistry here; shared integration verifies the large taxon database.
    authority = next(a for a in manifest["authority_inputs"] if a["raw_path"].endswith("chebi.db"))
    assert digest(authority["raw_path"]) == authority["sha256"]
    assert digest(manifest["rhea_directions"]["raw_path"]) == manifest["rhea_directions"]["sha256"]
    extracted = rhea_extract()
    assert extracted == projection["rhea"]
    expected = []
    net = collections.Counter()
    for side in extracted["sides"]:
        if side["role"] == "substrates":
            expected.append((side["id"], "consumes", "RHEA:" + side["reaction"]))
            net[side["id"]] -= side["coefficient"]
        else:
            expected.append(("RHEA:" + side["reaction"], "produces", side["id"]))
            net[side["id"]] += side["coefficient"]
    chemical = [
        e for e in record["mechanistic_edges"] if e["predicate"] in ["consumes", "produces"]
    ]
    assert collections.Counter(expected) == collections.Counter(
        (e["subject"], e["predicate"], e["object"]) for e in chemical
    )
    assert len(chemical) == 15
    assert {k: v for k, v in net.items() if v} == {
        "CHEBI:142957": -1,
        "CHEBI:30616": -1,
        "CHEBI:57945": -1,
        "CHEBI:456216": 1,
        "CHEBI:57642": 1,
        "CHEBI:176527": 1,
        "CHEBI:57540": 1,
    }
    for rid in SELECTED:
        r = next(r for r in record["reactions"] if r["id"] == "RHEA:" + rid)
        assert r["direction"] == ("right_to_left" if rid == "40513" else "left_to_right")
    with sqlite3.connect(f"file:{CACHE}/ncbitaxon.db?mode=ro", uri=True) as db:
        assert (
            db.execute(
                "select value from statements where subject='NCBITaxon:83333' "
                "and predicate='rdfs:label'"
            ).fetchone()[0]
            == record["taxa"][0]["label"]
        )
    with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as db:
        for n in record["participants"]:
            if n["id"].startswith("CHEBI:"):
                assert (
                    db.execute(
                        "select value from statements where subject=? and predicate='rdfs:label'",
                        (n["id"],),
                    ).fetchone()[0]
                    == n["label"]
                )
    science = check_original_science(record)
    locations = source_checks(record, manifest, projection)
    assert len(locations) == 84
    output = RAW / "replay-kgx"
    nodes_path, edges_path = write_kgx([validated], output)
    with nodes_path.open() as f:
        nodes = {n["id"]: n for n in csv.DictReader(f, delimiter="\t")}
    with edges_path.open() as f:
        edges = list(csv.DictReader(f, delimiter="\t"))
    assert len(nodes) == 32 and len(edges) == 41
    refs = {r["id"]: r for r in record["references"]}
    for original, actual in zip(record["mechanistic_edges"], edges, strict=True):
        assert (
            original["subject"],
            LOCAL_PREDICATE_CURIES[original["predicate"]],
            original["object"],
        ) == (actual["subject"], actual["predicate"], actual["object"])
        assert json.loads(actual["evidence"]) == original["evidence"]
        assert actual["description"] == original.get("description", "")
        expected_refs = [refs[r] for r in sorted({e["reference_id"] for e in original["evidence"]})]
        assert json.loads(actual["reference_metadata"]) == expected_refs
    for group in ["participants", "reactions"]:
        for n in record[group]:
            actual = nodes[n["id"]]
            assert actual["category"] == EXPLICIT_CATEGORIES[n["category"]]
            assert actual["source_category"] == n["category"]
            assert actual["direction"] == n.get("direction", "")
            assert json.loads(actual["source_contexts"])[0] == dict(
                record_id=record["id"], collection=group, **n
            )
    result = dict(
        status="passed",
        started_at=started,
        finished_at=datetime.now(UTC).isoformat(),
        target=str(TARGET.relative_to(ROOT)),
        target_sha256=target_hash,
        command=(
            "PYTHONPATH=src UV_NO_SYNC=1 "
            "UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache .venv/bin/python"
            " research/pathway_additions/2026-10-11-next-201/sulfoquinovose-replay.py"
        ),
        workdir=str(ROOT),
        helper_sha256=digest(Path(__file__)),
        checked_bodies=len(manifest["body_sources"]),
        chemical_side_occurrences=len(chemical),
        balances=extracted["balances"],
        net_stoichiometry={k: v for k, v in net.items() if v},
        source_checks=locations,
        original_science=science,
        authority_hash_scope=(
            "Author streamed full ChEBI255 and original Rhea142; taxon selected label"
            " queried, full taxon hash delegated to shared integration."
        ),
        kgx=dict(
            nodes=len(nodes),
            edges=len(edges),
            evidence=len(locations),
            nodes_sha256=digest(nodes_path),
            edges_sha256=digest(edges_path),
            output_dir=str(output),
        ),
        limits=[
            "Author replay, not independent scientific review.",
            (
                "Full shared gates and independent identifier snapshot integration are "
                "coordinated by root."
            ),
            (
                "PDF figure labels were visually inspected; text assertions and exact "
                "source-body hashes are replayed."
            ),
        ],
    )
    (DOSSIER / "sulfoquinovose-validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: result[k]
                for k in [
                    "status",
                    "target_sha256",
                    "checked_bodies",
                    "chemical_side_occurrences",
                    "kgx",
                ]
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    run()
