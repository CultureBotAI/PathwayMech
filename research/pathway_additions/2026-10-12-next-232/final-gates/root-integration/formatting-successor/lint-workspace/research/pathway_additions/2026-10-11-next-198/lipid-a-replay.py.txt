"""Offline author checks against original lipid-A sources, not an independent review."""

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
from lxml import html

from pathwaymech.kgx import EXPLICIT_CATEGORIES, LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-198"
RAW = Path("/private/tmp/pathwaymech-next-198-evidence/lipid-a")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
SELECTED = ["24703", "24712", "24707", "27723", "27735", "35372"]
MASTERS = {"24702", "24706", "24710", "27722", "27734", "35371"}
NATIVE = ["RXN0-1861", "RXN0-1863", "RXN0-1862", "RXN0-3521", "RXN0-5409", "RXN0-2001"]


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def native(frame):
    return ET.parse(str(RAW / f"metacyc-{frame}.xml")).getroot()[1]


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


def check_native(projection):
    pathway = native("PWY0-1338")
    members = pathway.xpath("reaction-list/Reaction/@frameid")
    assert set(members) == set(NATIVE) and len(members) == 6
    for upstream, downstream in zip(NATIVE, NATIVE[1:], strict=False):
        assert pathway.xpath(
            "reaction-ordering[Reaction/@frameid=$down]/predecessor-reactions/"
            "Reaction[@frameid=$up]",
            down=downstream,
            up=upstream,
        ), (upstream, downstream)
    assert pathway.xpath('hypothetical-reactions/Reaction[@frameid="RXN0-5409"]')
    assembly = native("CPLX0-7718")
    assert assembly.xpath('component[Protein/@frameid="G7168-MONOMER"]/coefficient/text()') == ["6"]
    for mid in ["RXN0-1861", "RXN0-1862"]:
        assert assembly.xpath(
            "catalyzes/Enzymatic-Reaction/reaction/Reaction[@frameid=$id]", id=mid
        )
    xrefs = {}
    for mid in NATIVE:
        xrefs[mid] = native(mid).xpath('dblink[dblink-db="RHEA"]/dblink-oid/text()')
    assert xrefs == dict(
        zip(NATIVE, [["24703"], ["24713"], ["24707"], ["27723"], ["27735"], ["35372"]], strict=True)
    )
    biopax_counts = []
    for expected in projection["pathbank"]:
        tree = ET.parse(str(RAW / expected["member"]))
        objects = {
            e.get(RDF + "ID") or e.get(RDF + "about"): e
            for e in tree.getroot()
            if isinstance(e.tag, str) and (e.get(RDF + "ID") or e.get(RDF + "about"))
        }
        counts = dict(collections.Counter(ET.QName(e).localname for e in objects.values()))
        assert counts == expected["classes"]
        assert counts["BiochemicalReaction"] == 6 and counts["Catalysis"] == 5
        for reaction in expected["reactions"]:
            obj = objects[reaction["id"]]
            for side in ["left", "right"]:
                assert [e.get(RDF + "resource").lstrip("#") for e in obj.findall(BP + side)] == [
                    e["id"] for e in reaction[side]
                ]
            coefficients = []
            for e in obj.findall(BP + "participantStoichiometry"):
                s = objects[e.get(RDF + "resource").lstrip("#")]
                coefficients.append(
                    dict(
                        entity=[
                            q.get(RDF + "resource").lstrip("#")
                            for q in s.findall(BP + "physicalEntity")
                        ],
                        coefficient=s.findtext(BP + "stoichiometricCoefficient"),
                    )
                )
            assert coefficients == reaction["stoichiometry"]
        biopax_counts.append(dict(member=expected["member"], classes=counts))
    return dict(native_members=members, xrefs=xrefs, biopax=biopax_counts)


def pointer(data, path):
    for key in path.strip("/").split("/"):
        data = data[int(key)] if isinstance(data, list) else data[key]
    return data


def source_locations(record, manifest):
    refs = {r["id"]: r for r in record["references"]}
    sources = {r["reference_id"]: r for r in manifest["reference_sources"]}
    checks = []
    for edge in record["mechanistic_edges"]:
        for ev in edge["evidence"]:
            rid = ev["reference_id"]
            source = sources[rid]
            assert source["sha256"] == refs[rid]["source_sha256"] == digest(source["raw_path"])
            loc = ev.get("source_locator", "")
            if rid.startswith("UniProtKB:"):
                data = read_json(source["raw_path"])
                paths = re.findall(r"/comments/\d+(?:/[A-Za-z]+|/\d+)*", loc)
                assert paths, (edge["id"], loc)
                for path in paths:
                    assert pointer(data, path) is not None, (edge["id"], path)
            elif "abstracts" in source["raw_path"]:
                data = read_json(source["raw_path"])
                result = next(q for q in data["resultList"]["result"] if q["id"] == rid[5:])
                assert result["abstractText"] and f'id="{rid[5:]}"' in loc
            elif source["raw_path"].endswith(".html"):
                tree = html.parse(source["raw_path"])
                for anchor in re.findall(r"\bP\d+\b|pro70037-sec-\d+", loc):
                    assert tree.xpath("//*[@id=$anchor]", anchor=anchor), (edge["id"], anchor)
            elif source["raw_path"].endswith(".xml"):
                tree = ET.parse(source["raw_path"])
                first = loc.split(";")[0]
                if first.startswith("/ptools-xml"):
                    assert tree.xpath(first), (edge["id"], first)
            checks.append(dict(edge=edge["id"], reference_id=rid, source_locator=loc))
    # Additional original-body regressions guard against organism/assembly inference shortcuts.
    a = html.parse(str(RAW / "primary-PMC10914315.html"))

    def text(pid):
        return " ".join(a.xpath("//*[@id=$id]//text()", id=pid))

    assert "MST100" in text("P10") and "Salmonella" in text("P13")
    assert "Salmonella" in text("P19") and "MnCl" in text("P19")
    assert "EDTA" in text("P29") and "Co" in text("P29")
    b = html.parse(str(RAW / "primary-PMC2613183.html"))
    p40 = " ".join(b.xpath('//*[@id="P40"]//text()'))
    assert "heterodimer" in p40 and "energy" in p40
    c = html.parse(str(RAW / "primary-PMC11761694.html"))
    assert "typhimurium" in " ".join(c.xpath('//*[@id="pro70037-sec-0003"]//text()')).lower()
    return checks


def run():
    started = datetime.now(UTC).isoformat()
    record = yaml.safe_load(TARGET.read_text())
    target_hash = digest(TARGET)
    manifest = read_json(DOSSIER / "lipid-a-source-manifest.json")
    projection = read_json(DOSSIER / "lipid-a-source-projection.json")
    assert manifest["target_sha256"] == projection["target_sha256"] == target_hash
    validated = validate_record(record)
    errors = strict_errors([TARGET], ROOT)
    assert not errors, errors
    for body in manifest["body_sources"]:
        assert digest(body["raw_path"]) == body["sha256"], body["raw_path"]
    for name in ["chebi.db", "go.db"]:
        authority = next(a for a in manifest["authority_inputs"] if a["raw_path"].endswith(name))
        assert digest(authority["raw_path"]) == authority["sha256"]
    # Shared integration checked the taxon database digest; query the selected taxon here.
    with sqlite3.connect(f"file:{CACHE}/ncbitaxon.db?mode=ro", uri=True) as db:
        label = db.execute(
            "select value from statements where subject=? and predicate='rdfs:label'",
            ("NCBITaxon:83333",),
        ).fetchone()[0]
        assert label == record["taxa"][0]["label"]
    extracted = rhea_extract()
    assert extracted == projection["rhea"], "fresh original RDF/ChEBI projection changed"
    edges = record["mechanistic_edges"]
    chemical = [e for e in edges if e["predicate"] in ["consumes", "produces"]]
    expected = []
    for s in extracted["sides"]:
        if s["role"] == "substrates":
            triple = (s["id"], "consumes", "RHEA:" + s["reaction"])
        else:
            triple = ("RHEA:" + s["reaction"], "produces", s["id"])
        expected.append(triple)
        edge = next(e for e in chemical if (e["subject"], e["predicate"], e["object"]) == triple)
        assert f"coefficient {s['coefficient']}" in edge["evidence"][0]["source_assertion"]
    assert collections.Counter(expected) == collections.Counter(
        (e["subject"], e["predicate"], e["object"]) for e in chemical
    )
    net = collections.Counter()
    for s in extracted["sides"]:
        sign = -1 if s["role"] == "substrates" else 1
        net[s["id"]] += sign * s["coefficient"] * (1 if s["reaction"] == "35372" else 2)
    for intermediate in ["58710", "58708", "58709", "58909", "60463", "60392"]:
        assert net["CHEBI:" + intermediate] == 0, intermediate
    native_checks = check_native(projection)
    locations = source_locations(record, manifest)
    assert len(locations) == 98
    assert not any(
        e["subject"] == "UniProtKB:P76472" and e["predicate"] == "has_cofactor" for e in edges
    )
    assert not any(n["id"] == "MetaCyc:CPLX0-7720" for n in record["participants"])
    assert (
        len([e for e in edges if e["predicate"] == "enables" and e["object"] == record["id"]]) == 2
    )
    output = RAW / "replay-kgx"
    nodes_path, edges_path = write_kgx([validated], output)
    with nodes_path.open() as f:
        nodes = {n["id"]: n for n in csv.DictReader(f, delimiter="\t")}
    with edges_path.open() as f:
        exported = list(csv.DictReader(f, delimiter="\t"))
    assert len(nodes) == 39 and len(exported) == 50
    refs = {r["id"]: r for r in record["references"]}
    for original, actual in zip(edges, exported, strict=True):
        assert (
            original["subject"],
            LOCAL_PREDICATE_CURIES[original["predicate"]],
            original["object"],
        ) == (actual["subject"], actual["predicate"], actual["object"])
        assert json.loads(actual["evidence"]) == original["evidence"]
        expected_refs = [refs[r] for r in sorted({e["reference_id"] for e in original["evidence"]})]
        assert json.loads(actual["reference_metadata"]) == expected_refs
        assert actual["description"] == original.get("description", "")
    for group in ["participants", "reactions"]:
        for node in record[group]:
            actual = nodes[node["id"]]
            assert actual["category"] == EXPLICIT_CATEGORIES[node["category"]]
            assert actual["source_category"] == node["category"]
            assert actual["direction"] == node.get("direction", "")
            assert json.loads(actual["source_contexts"])[0] == dict(
                record_id=record["id"], collection=group, **node
            )
    result = dict(
        status="passed",
        started_at=started,
        finished_at=datetime.now(UTC).isoformat(),
        target=str(TARGET.relative_to(ROOT)),
        target_sha256=target_hash,
        command=(
            "PYTHONPATH=src UV_NO_SYNC=1 "
            "UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache "
            ".venv/bin/python research/pathway_additions/2026-10-11-next-198/lipid-a-replay.py"
        ),
        workdir=str(ROOT),
        helper_sha256=digest(Path(__file__)),
        checked_bodies=len(manifest["body_sources"]),
        independently_rehashed_large_authorities=["ChEBI 255", "GO 2026-07-26"],
        taxon_digest_scope="shared canonical integration digest; exact selected taxon queried here",
        native=native_checks,
        chemical_side_occurrences=len(chemical),
        balances=extracted["balances"],
        net_stoichiometry={k: v for k, v in sorted(net.items()) if v},
        evidence_locator_checks=locations,
        kgx=dict(
            nodes=len(nodes),
            edges=len(exported),
            evidence_blocks=len(locations),
            nodes_sha256=digest(nodes_path),
            edges_sha256=digest(edges_path),
            output_dir=str(output),
        ),
        schemas="native and closed LinkML passed",
        limitations=[
            "Author replay checks sources/export; it is not independent scientific review.",
            "Source limits, disputed assemblies and species-specific metals remain as recorded.",
            "Archive/taxonomy digests were not rehashed here; exact members/taxon were checked.",
        ],
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
