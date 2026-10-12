"""Offline first-cycle author evidence replay; not an independent scientific review."""

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
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-206"
RAW = Path("/private/tmp/pathwaymech-next-206-evidence/three-hydroxypropionate")
SHARED = RAW.parent / "glyoxylate"
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml"
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
    "23721",
    "20555",
    "22889",
    "38256",
    "40524",
    "12462",
    "16630",
]
NATIVE = [
    "RXN0-5224",
    "BIOTIN-CARBOXYL-RXN",
    "RXN0-5055",
    "RXN-8963",
    "RXN-8974",
    "RXN-9086",
    "RXN-6383",
    "RXN-9087",
    "PROPIONYL-COA-CARBOXY-RXN",
    "METHYLMALONYL-COA-EPIM-RXN",
    "METHYLMALONYL-COA-MUT-RXN",
    "RXN-8964",
    "MALYL-COA-LYASE-RXN",
]


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


def html_text(pmc, anchor):
    tree = ET.parse(str(RAW / f"{pmc}.html"), ET.HTMLParser())
    nodes = tree.xpath("//*[@id=$anchor]", anchor=anchor)
    assert len(nodes) == 1, (pmc, anchor)
    return " ".join(" ".join(nodes[0].itertext()).split())


def rhea_extract():
    directions = {}
    for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
        cells = line.split("\t")
        if set(cells) & set(SELECTED):
            directions[cells[0]] = dict(zip(["master", "lr", "rl", "bi"], cells, strict=True))
    assert len(directions) == 15
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
    while True:
        needed = {
            v
            for n in nodes.values()
            for vs in n.values()
            for v in vs
            if v in compounds and v not in nodes
        }
        if not needed:
            break
        nodes.update({uri: compounds[uri] for uri in needed})
    sides, balances, terms = [], [], {}
    net = collections.Counter()
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
                        cid = cp["accession"][0].replace("GENERIC:", "RHEA-COMP:")
                        chemistry = nodes[cp["reactivePart"][0]] if "reactivePart" in cp else cp
                        chebi = chemistry["chebi"][0].rsplit("/", 1)[-1].replace("_", ":")
                        values = {
                            a: b if b is not None else c
                            for a, b, c in db.execute(
                                "select predicate,value,object from statements where subject=?",
                                (chebi,),
                            )
                        }
                        terms[chebi] = values
                        assert values.get("owl:deprecated") not in ["true", True]
                        assert (
                            values["chemrof:generalized_empirical_formula"]
                            == chemistry["formula"][0]
                        )
                        assert values["chemrof:charge"] == chemistry["charge"][0]
                        formula = chemistry["formula"][0]
                        atoms = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
                        assert "".join(a + b for a, b in atoms) == formula
                        for atom, count in atoms:
                            balance[atom] += sign * coefficient * int(count or 1)
                        balance["charge"] += sign * coefficient * int(chemistry["charge"][0])
                        net[cid] += sign * coefficient
                        sides.append(
                            {
                                "reaction": rid,
                                "role": role,
                                "side": side,
                                "predicate": predicate,
                                "participant": participant,
                                "compound": compound,
                                "id": cid,
                                "coefficient": coefficient,
                                "formula": formula,
                                "charge": chemistry["charge"][0],
                                "chemistry_scope": "reactive residue; unchanged protein scaffold"
                                if "reactivePart" in cp
                                else "source chemical/formula class",
                            }
                        )
            assert all(v == 0 for v in balance.values()), (rid, balance)
            balances.append({"reaction": rid, "residual": dict(balance), "status": "passed"})
    assert net["CHEBI:36655"] == 1 and net["CHEBI:57288"] == 0
    assert net["RHEA-COMP:10505"] == net["RHEA-COMP:10506"] == 0
    assert net["CHEBI:132124"] == -1 and net["CHEBI:24646"] == 1
    return {
        "directions": directions,
        "nodes": nodes,
        "sides": sides,
        "balances": balances,
        "terms": terms,
        "net_once_hydration": {k: v for k, v in net.items() if v},
        "net_limit": "One hydration is the listed reaction count; two turnovers express both"
        " inorganic-carbon inputs as CO2. Generic quinone redox and carrier cancellation are"
        " class/scaffold accounting, not a measured physiological carrier identification.",
    }


def pointer(data, path):
    for key in path.strip("/").split("/"):
        data = data[int(key)] if isinstance(data, list) else data[key]
    return data


def original_source_checks(record, projection, chemistry):
    members = native("PWY-5743").xpath("reaction-list/Reaction/@frameid")
    assert len(members) == 13 and set(members) == set(NATIVE)
    mapping = projection["physiological_reaction_mapping"]
    for row in mapping:
        if not row["native_id"]:
            continue
        obj = native(row["native_id"].split(":")[1])
        crossrefs = obj.xpath("dblink[dblink-db='RHEA']/dblink-oid/text()")
        if crossrefs:
            rid = row["id"].split(":")[1]
            family = next(d for d in chemistry["directions"].values() if rid in d.values())
            assert crossrefs[0] in family.values(), (row, crossrefs)
    assert native("CPLX-7550").xpath("component/coefficient/text()") == ["2"]
    assert native("CPLX-7549").xpath("component/coefficient/text()") == ["6"]
    assert native("CPLX-7546").xpath("component/coefficient/text()") == ["6"]
    assert native("CPLX-7548").xpath("component/coefficient/text()") == ["1", "1"]
    assert "three or four" in native("CPLX-7552").findtext("comment")
    assert "CPLX-7552" not in [n["id"] for n in record["participants"]]
    proteins = {
        n["id"]: read_json(projection["reference_original_paths"][n["id"]])
        for n in record["references"]
        if n["id"].startswith("UniProtKB:")
    }
    for curie, original in proteins.items():
        assert original["primaryAccession"] == curie.split(":")[1]
    assert (
        proteins["UniProtKB:S5N020"]["sequence"]["value"]
        == read_json(RAW / "uniprot-A9WC35.json")["sequence"]["value"]
    )
    assert (
        proteins["UniProtKB:Q6QQP7"]["sequence"]["value"]
        != read_json(RAW / "uniprot-A9WIU3.json")["sequence"]["value"]
    )
    gb = ET.parse(str(SHARED / "AAL47820.2.xml"))
    assert (
        gb.xpath("//GBSeq_sequence/text()")[0].upper()
        == proteins["UniProtKB:Q8VRG6"]["sequence"]["value"]
    )
    assert "OK-70" in (SHARED / "AF445079.2.embl").read_text()
    # Check every literal JSON pointer used in the graph, including optional note fields.
    pointers = []
    for edge in record["mechanistic_edges"]:
        for evidence in edge["evidence"]:
            curie = evidence["reference_id"]
            if curie not in proteins:
                continue
            for loc in evidence["source_locator"].split("; "):
                if "[" in loc:
                    assert proteins[curie]["uniProtKBCrossReferences"]
                elif "–" in loc:
                    first, last = loc.rsplit("/", 1)[1].split("–")
                    for i in range(int(first), int(last) + 1):
                        pointer(proteins[curie], "/references/" + str(i))
                else:
                    pointer(proteins[curie], loc)
                pointers.append({"edge": edge["id"], "source": curie, "locator": loc})
    anchors = {
        "PMC134993": {
            "sec21": ["145", "300"],
            "sec23": ["semialdehyde"],
            "sec27": ["partial"],
            "sec29": ["sequence"],
        },
        "PMC135395": {"sec2": ["OK-70"], "sec12": ["Cloning"], "sec28": ["EDTA", "31%"]},
        "PMC1428406": {
            "sec2": ["OK-70"],
            "sec14": ["smtA"],
            "sec15": ["smtB"],
            "sec16": ["coexpression"],
            "sec38": ["sequence"],
            "sec39": ["expressing both", "reconstituted"],
            "sec40": ["550", "50"],
        },
        "PMC3832036": {"sec6": ["228", "15"], "sec9": ["trimers"], "sec18": ["OK-70"]},
        "PMC11077971": {
            "s2-1": ["596", "BCCP"],
            "s2-2": ["tetramer"],
            "s2-3": ["complex"],
            "s2-4": ["active"],
            "s4-1": ["1647", "1648"],
            "s4-3": ["ATP"],
            "s4-4": ["biotinylation"],
            "s4-5": ["HPLC"],
            "s4-8": ["AUC"],
        },
    }
    for pmc, checks in anchors.items():
        for anchor, words in checks.items():
            text = html_text(pmc, anchor)
            assert all(w.lower() in text.lower() for w in words), (pmc, anchor, words)
    text = (RAW / "PMC95321.html").read_text()
    assert "Succinate dehydrogenase" in text and "Fumarate hydratase" in text
    text = " ".join(ET.parse(str(RAW / "PMC1428406.html"), ET.HTMLParser()).getroot().itertext())
    assert "reduced quinone" in text
    return {"native_members": members, "valid_json_locators": pointers, "primary_anchors": anchors}


def main():
    started = datetime.now(UTC).isoformat()
    starting_target_sha256 = digest(TARGET)
    record = yaml.safe_load(TARGET.read_text())
    validated = validate_record(record)
    assert not strict_errors([TARGET], ROOT)
    manifest = read_json(DOSSIER / "three-hydroxypropionate-source-manifest.json")
    original_hashes = []
    for entry in manifest["sources"] + manifest["transformed_inspection_outputs"]:
        actual = digest(entry["path"])
        assert actual == entry["sha256"], entry["path"]
        original_hashes.append({"path": entry["path"], "sha256": actual})
    chebi_source = next(v for v in manifest["pinned_authorities"] if v["version"] == "255")
    assert digest(chebi_source["path"]) == chebi_source["sha256"]
    projection = read_json(DOSSIER / "three-hydroxypropionate-source-projection.json")
    assert projection["target_sha256"] == digest(TARGET)
    chemistry = rhea_extract()
    originals = original_source_checks(record, projection, chemistry)
    rnodes = {n["id"].split(":")[1]: n for n in record["reactions"]}
    assert set(rnodes) == set(SELECTED)
    for rid, node in rnodes.items():
        family = next(d for d in chemistry["directions"].values() if rid in d.values())
        assert node["label"] == chemistry["nodes"][RH + rid]["label"][0]
        assert node["direction"] == ("left_to_right" if rid == family["lr"] else "right_to_left")
    side_edges = [
        e for e in record["mechanistic_edges"] if e["predicate"] in ["consumes", "produces"]
    ]
    assert len(side_edges) == len(chemistry["sides"])
    for side in chemistry["sides"]:
        rid = "RHEA:" + side["reaction"]
        pred = "consumes" if side["role"] == "substrates" else "produces"
        sub, obj = (side["id"], rid) if pred == "consumes" else (rid, side["id"])
        matches = [
            e for e in side_edges if (e["subject"], e["predicate"], e["object"]) == (sub, pred, obj)
        ]
        assert len(matches) == 1
        assert matches[0]["description"] == f"Stoichiometric coefficient {side['coefficient']}."
        assert side["participant"] in matches[0]["evidence"][0]["source_locator"]
    for edge in record["mechanistic_edges"]:
        if edge["predicate"] == "provides_input_for":
            a, b = edge["subject"].split(":")[1], edge["object"].split(":")[1]
            outputs = {
                s["id"]
                for s in chemistry["sides"]
                if s["reaction"] == a and s["role"] == "products"
            }
            inputs = {
                s["id"]
                for s in chemistry["sides"]
                if s["reaction"] == b and s["role"] == "substrates"
            }
            assert any(cid in edge["description"] for cid in outputs & inputs)
    out = RAW / "actual-kgx"
    nodepath, edgepath = write_kgx([validated], out)
    with edgepath.open() as stream:
        exported = list(csv.DictReader(stream, delimiter="\t"))
    with nodepath.open() as stream:
        node_export = {n["id"]: n for n in csv.DictReader(stream, delimiter="\t")}
    by_id = {e["id"]: e for e in record["mechanistic_edges"]}
    assert len(exported) == len(by_id)
    refs = {r["id"]: r for r in record["references"]}
    export_map = {}
    for edge_id, edge in by_id.items():
        suffix = hashlib.sha256(f"{record['id']}\0{edge_id}".encode()).hexdigest()[:12]
        safe = re.sub(r"[^A-Za-z0-9._-]+", "_", f"{record['id']}_{edge_id}").strip("_")
        export_map[f"pathwaymech:{safe}_{suffix}"] = edge
    for item in exported:
        edge = export_map[item["id"]]
        assert item["subject"] == edge["subject"] and item["object"] == edge["object"]
        assert item["predicate"] == LOCAL_PREDICATE_CURIES[edge["predicate"]]
        assert json.loads(item["evidence"]) == edge["evidence"]
        assert item["description"] == edge.get("description", "")
        assert json.loads(item["reference_metadata"]) == [
            refs[i] for i in sorted({v["reference_id"] for v in edge["evidence"]})
        ]
    for node in record["participants"]:
        assert node_export[node["id"]]["category"] == EXPLICIT_CATEGORIES[node["category"]]
    assert node_export["RHEA:10750"]["category"] == "biolink:BiochemicalReaction"
    assert digest(TARGET) == starting_target_sha256, "Target changed during author replay"
    result = {
        "status": "passed",
        "author_check_not_independent_review": True,
        "started_at": started,
        "finished_at": datetime.now(UTC).isoformat(),
        "target_sha256": digest(TARGET),
        "helper_sha256": digest(Path(__file__)),
        "original_source_checks": original_hashes,
        "chemistry": chemistry,
        "native_and_primary_checks": originals,
        "counts": {
            "participants": len(record["participants"]),
            "reactions": len(rnodes),
            "edges": len(by_id),
            "evidence": sum(len(e["evidence"]) for e in by_id.values()),
            "chemical_sides": len(side_edges),
            "references": len(refs),
        },
        "kgx": {
            "nodes": len(node_export),
            "edges": len(exported),
            "nodes_sha256": digest(nodepath),
            "edges_sha256": digest(edgepath),
        },
        "limits": manifest["limits"],
        "checks": [
            "native schema",
            "closed LinkML",
            "source hashes",
            "original Rhea RDF",
            "ChEBI formulas and charges",
            "15 balances and cycle net",
            "native boundary",
            "literal primary anchors",
            "protein sequences and JSON pointers",
            "actual KGX",
        ],
        "shared_gates": "Root runs whole-corpus gates separately.",
    }
    (DOSSIER / "three-hydroxypropionate-validation.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps({k: result[k] for k in ["status", "target_sha256", "counts", "kgx"]}))


if __name__ == "__main__":
    main()
