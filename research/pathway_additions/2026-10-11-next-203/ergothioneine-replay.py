"""Author replay of original sources; not an independent scientific review."""

from __future__ import annotations

import collections
import gzip
import hashlib
import json
import re
import sqlite3
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import etree as ET
from lxml import html

from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, kgx_edges, kgx_nodes, render_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
D = ROOT / "research/pathway_additions/2026-10-11-next-203"
RAW = Path("/private/tmp/pathwaymech-next-203-evidence/ergothioneine")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/ergothioneine-biosynthesis-i.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
SELECTED = ["13286", "38472", "42673", "42685", "52781"]
MASTERS = {"13285", "38471", "42672", "42684", "52780", "52784"}


def digest(path):
    checksum = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            checksum.update(block)
    return checksum.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def native(frame):
    return ET.parse(str(RAW / (frame + ".xml"))).getroot()[1]


def formula(value):
    pieces = re.findall(r"([A-Z][a-z]?)(\d*)", value)
    assert "".join(a + b for a, b in pieces) == value, value
    return {atom: int(number or 1) for atom, number in pieces}


def extract_rhea():
    dirs = {}
    for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
        values = line.split("\t")
        if values[0] in MASTERS:
            dirs[values[0]] = dict(zip(["master", "lr", "rl", "bi"], values, strict=True))
    numbers = {value for item in dirs.values() for value in item.values()}
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
    needed = {
        v for item in nodes.values() for values in item.values() for v in values if v in compounds
    }
    nodes.update({uri: compounds[uri] for uri in needed})
    sides = []
    for rid in SELECTED + ["52785"]:
        assert any(item["lr"] == rid for item in dirs.values()), rid
        for role in ["substrates", "products"]:
            side = nodes[RH + rid][role][0]
            for predicate, participants in nodes[side].items():
                if not re.fullmatch(r"contains\d+", predicate):
                    continue
                for participant in participants:
                    compound = nodes[participant]["compound"][0]
                    cid = nodes[compound]["accession"][0]
                    sides.append(
                        dict(
                            reaction="RHEA:" + rid,
                            role=role,
                            chemical=cid,
                            coefficient=int(predicate[8:]),
                            side=side,
                            participant=participant,
                            compound=compound,
                            predicate=predicate,
                        )
                    )
    return nodes, sides


def main():
    started = datetime.now(UTC).isoformat()
    target_hash = digest(TARGET)
    record = yaml.safe_load(TARGET.read_text())
    manifest = read(D / "ergothioneine-source-manifest.json")
    assert manifest["target_sha256"] == digest(TARGET)
    for source in manifest["sources"]:
        assert digest(source["path"]) == source["sha256"], source["path"]
    # Fresh stream hashes, no whole-file allocation for source databases.
    for source in manifest["authority_inputs"]:
        assert digest(source["path"]) == source["sha256"], source["path"]
    projection = read(D / "ergothioneine-source-projection.json")
    nodes, sides = extract_rhea()
    first = [s for s in sides if s["reaction"] != "RHEA:52785"]
    assert first == projection["chemical_sides"]
    pwy = native("PWY-7255")
    members = pwy.xpath("reaction-list/Reaction/@frameid")
    assert set(members) == set(projection["native_members"]) and len(members) == 7
    for frame, rid in zip(
        projection["native_members"], projection["selected_reactions"], strict=True
    ):
        rr = next(r for r in record["reactions"] if r["id"] == rid)
        if rid.startswith("RHEA:"):
            assert rr["label"] == nodes[RH + rid.split(":")[1]]["label"][0]
            assert rr["direction"] == "left_to_right"
            native_xref = native(frame).xpath("dblink[dblink-db='RHEA']/dblink-oid/text()")[0]
            assert native_xref in {rid.split(":")[1], str(int(rid.split(":")[1]) - 1)}
        else:
            assert native(frame).findtext("spontaneous") == "true"
    assert native("RXN-15804").findtext("reaction-direction") == "REVERSIBLE"
    assert pwy.xpath("reaction-layout[Reaction/@frameid='RXN-15804']/direction/text()") == ["R2L"]
    assert native("RXN-18089").findtext("reaction-direction") == "PHYSIOL-LEFT-TO-RIGHT"
    terminal = projection["terminal_sides"]
    for frame, side, compound, cid in terminal:
        assert native(frame).xpath(f"{side}/Compound[@frameid='{compound}']")
        role = "substrates" if (side == "left") == (frame == "RXN-18089") else "products"
        first.append(dict(reaction="MetaCyc:" + frame, role=role, chemical=cid, coefficient=1))
    balances = {}
    with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as db:
        chemicals = {}
        for cid in {s["chemical"] for s in first}:
            fields = dict(
                db.execute(
                    "select predicate,value from statements where subject=? and predicate in "
                    "('rdfs:label','chemrof:charge','chemrof:generalized_empirical_formula',"
                    "'chemrof:smiles_string','chemrof:inchi_string')",
                    (cid,),
                )
            )
            chemicals[cid] = fields
        for rxn in record["reactions"]:
            balance = collections.Counter()
            for side in [s for s in first if s["reaction"] == rxn["id"]]:
                sign = -1 if side["role"] == "substrates" else 1
                chem = chemicals[side["chemical"]]
                atoms = formula(chem["chemrof:generalized_empirical_formula"])
                atoms["charge"] = int(chem["chemrof:charge"])
                for atom, count in atoms.items():
                    balance[atom] += sign * side["coefficient"] * count
            assert all(value == 0 for value in balance.values()), (rxn["id"], balance)
            balances[rxn["id"]] = dict(balance)
        # Native and selected tautomer distinction, rather than an InChI-only merge.
        assert (
            chemicals["CHEBI:4828"]["chemrof:inchi_string"]
            == chemicals["CHEBI:82707"]["chemrof:inchi_string"]
        )
        assert "c(S)" in chemicals["CHEBI:4828"]["chemrof:smiles_string"]
        assert "c(=S)" in chemicals["CHEBI:82707"]["chemrof:smiles_string"]
    for frame, order in [("Ergothioneine", "1"), ("Ergothioneine-Thione", "2")]:
        molecule = native(frame).find("cml/molecule")
        assert molecule.get("formalCharge") == "0"
        sulfur = molecule.xpath("atomArray/atom[@elementType='S']/@id")[0]
        bonds = [
            b for b in molecule.findall("bondArray/bond") if sulfur in b.get("atomRefs").split()
        ]
        assert len(bonds) == 1 and bonds[0].get("order") == order
    assert native("Donor-H2").xpath("dblink[dblink-db='CHEBI']/dblink-oid/text()") == ["17499"]
    assert native("Acceptor").xpath("dblink[dblink-db='CHEBI']/dblink-oid/text()") == ["15339"]
    assert "unknown acceptors that transfer two electrons and two protons" in native(
        "Acceptor"
    ).findtext("comment")
    alternative = [s for s in sides if s["reaction"] == "RHEA:52785"]
    assert {s["chemical"] for s in alternative if s["role"] == "products"} == {
        "CHEBI:134344",
        "CHEBI:13193",
        "CHEBI:15377",
    }
    assert "CHEBI:134344" not in {x["id"] for x in record["participants"]}
    assert "RHEA:42689" not in {x["id"] for x in record["reactions"]}
    expected = collections.Counter((s["reaction"], s["role"], s["chemical"]) for s in first)
    actual = collections.Counter(
        (e["object"], "substrates", e["subject"])
        if e["predicate"] == "consumes"
        else (e["subject"], "products", e["object"])
        for e in record["mechanistic_edges"]
        if e["predicate"] in {"consumes", "produces"}
    )
    assert expected == actual
    # Test exact nearest structured locators and actual original-primary anchors.
    for edge in record["mechanistic_edges"]:
        for evidence in edge["evidence"]:
            ref = evidence["reference_id"]
            locator = evidence["source_locator"]
            if ref.startswith("UniProtKB:"):
                obj = read(RAW / ("uniprot-" + ref.split(":")[1] + ".json"))
                for pointer in re.findall(r"/comments/\d+(?:/[A-Za-z0-9]+)*", locator):
                    value = obj
                    for key in pointer[1:].split("/"):
                        value = value[int(key)] if isinstance(value, list) else value[key]
            if ref in {"PMID:26149121", "PMID:38072054"}:
                tree = ET.parse(
                    str(RAW / ("PMC4493562.xml" if ref.endswith("26149121") else "PMC10805701.xml"))
                )
                for section in re.findall(r"sec\[@id='([^']+)'\]", locator):
                    assert tree.xpath(f"//sec[@id='{section}']"), section
    c = ET.parse(str(RAW / "PMC10805701.xml"))
    assert "A0R5M7" in " ".join(c.xpath("//sec[@id='sec3.2']/p[1]")[0].itertext())
    assert "76" in " ".join(c.xpath("//sec[@id='sec1.1']/p[2]")[0].itertext())
    phys = html.parse(str(RAW / "PMC3697313.html"))
    assert "restoration" in " ".join(phys.xpath("//section[@id='sec12']/p[1]")[0].itertext())
    assert "mc" in " ".join(phys.xpath("//section[@id='sec5']/p[1]")[0].itertext())
    # Exact protein authority names/taxon and raw evidence tiers.
    for protein in [p for p in record["participants"] if p["id"].startswith("UniProtKB:")]:
        obj = read(RAW / ("uniprot-" + protein["id"].split(":")[1] + ".json"))
        assert obj["organism"]["taxonId"] == 246196
        assert obj["proteinDescription"]["recommendedName"]["fullName"]["value"] == protein["label"]
    egta = read(RAW / "uniprot-A0R5N1.json")
    assert egta["comments"][1]["reaction"]["evidences"][0]["evidenceCode"] == "ECO:0000250"
    # Issue371: a different engineered preparation is contextual, not an exact inhibitory edge.
    egt_d = read(RAW / "uniprot-A0R5M8.json")["sequence"]["value"]
    early = html.parse(str(RAW / "PMC4014345.html"))
    paragraph = "".join(early.xpath("//*[@id='sec2.1']/p[1]")[0].itertext())
    assayed = re.search(r"MALSLANY[A-Z]+", paragraph).group()
    assert [
        (i + 1, a, b) for i, (a, b) in enumerate(zip(assayed, egt_d, strict=True)) if a != b
    ] == [(2, "A", "T")]
    assert not any(e["id"] == "ergothioneine-edge-048" for e in record["mechanistic_edges"])
    assert "not transferred" in record["description"]
    assert any(r["id"] == "DOI:10.1021/acschembio.8b00127.s001" for r in record["references"])
    valid = validate_record(record)
    assert strict_errors([TARGET], ROOT) == []
    output = RAW / "kgx"
    output.mkdir(exist_ok=True)
    for name, content in render_kgx([valid]).items():
        (output / name).write_text(content)
    exported = [asdict(e) for e in kgx_edges([valid])]
    for edge, kgx in zip(record["mechanistic_edges"], exported, strict=True):
        assert kgx["subject"] == edge["subject"] and kgx["object"] == edge["object"]
        assert kgx["predicate"] == LOCAL_PREDICATE_CURIES[edge["predicate"]]
        assert json.loads(kgx["evidence"]) == edge["evidence"]
        metadata = json.loads(kgx["reference_metadata"])
        assert metadata == [
            next(r for r in record["references"] if r["id"] == identifier)
            for identifier in sorted({ev["reference_id"] for ev in edge["evidence"]})
        ]
    nn = {n.id: asdict(n) for n in kgx_nodes([valid])}
    for cid in ["CHEBI:17499", "CHEBI:13193"]:
        assert nn[cid]["category"] == "biolink:ChemicalEntity"
    for rid in ["MetaCyc:RXN-18089", "MetaCyc:RXN-15804"]:
        assert nn[rid]["category"] == "biolink:BiochemicalReaction"
        assert not any(
            e["object"] == rid and e["predicate"] in {"enables", "catalyzes"}
            for e in record["mechanistic_edges"]
        )
    assert digest(TARGET) == target_hash
    receipt = dict(
        status="passed",
        started_at=started,
        finished_at=datetime.now(UTC).isoformat(),
        role="author source replay, not independent scientific review",
        target_sha256=digest(TARGET),
        source_count=len(manifest["sources"]),
        script_sha256=digest(__file__),
        native_members=members,
        chemical_side_count=len(first),
        balances=balances,
        counts=dict(
            participants=len(record["participants"]),
            reactions=len(record["reactions"]),
            edges=len(record["mechanistic_edges"]),
            evidence=sum(len(e["evidence"]) for e in record["mechanistic_edges"]),
        ),
        checks=[
            "54 original bodies and two pinned authority bodies rehashed",
            "fresh original Rhea RDF projection and exact seven-native-member coverage",
            "all chemical sides, coefficients, seven atom/charge balances",
            "neutral thiol versus thione retained, current cationic alternative excluded",
            "exact generic AH2/A scope and no assigned terminal enzyme",
            "original protein JSON pointers and selected primary anchors",
            "native and closed schemas",
            "actual KGX endpoints, predicates and all evidence metadata",
        ],
        limits=[
            "Manual original-source scientific interpretation is documented separately.",
            "Generic A is symbolic; the physiological donor is unidentified.",
            "Full corpus gates and independent scientific review remain root-coordinated.",
        ],
    )
    (D / "ergothioneine-validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
