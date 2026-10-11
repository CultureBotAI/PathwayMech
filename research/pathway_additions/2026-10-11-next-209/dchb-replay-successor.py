"""Author replay against retained original sources; not independent review.

The full 14-step cycle is checked. Thirteen Rhea equations have exact or formal
symbolic-group balances; generic KEGG ferredoxin has no whole-carrier formula.
Only its explicitly derived acid-base normalization is verified numerically.
"""

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

ROOT = Path.cwd()
D = ROOT / "research/pathway_additions/2026-10-11-next-209"
TARGET = ROOT / "data/pathways/dicarboxylate-hydroxybutyrate-cycle.yaml"
RAW = Path("/private/tmp/pathwaymech-next-209-evidence/dchb")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def pointer(obj, path):
    for key in path.strip("/").split("/"):
        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
    return obj


def formula(text):
    parts = re.findall(r"([A-Z][a-z]?)(\d*)", text)
    assert "".join(a + b for a, b in parts) == text, text
    return collections.Counter({a: int(b or 1) for a, b in parts})


def parse_flatfile(path):
    result = {}
    for block in Path(path).read_text().split("///"):
        if not block.strip():
            continue
        fields = {}
        key = None
        for line in block.strip("\n").splitlines():
            if line[:12].strip():
                key = line[:12].strip()
            assert key is not None
            fields.setdefault(key, []).append(line[12:].strip())
        eid = fields["ENTRY"][0].split()[0]
        assert eid not in result
        result[eid] = fields
    return result


def original_rhea(steps):
    masters = {s["candidate_chemical_reaction"].split(":")[1] for s in steps[1:]}
    directions = {}
    for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
        cells = line.split("\t")
        if cells[0] in masters:
            directions[cells[0]] = dict(zip(["master", "lr", "rl", "bi"], cells, strict=True))
    assert len(directions) == 13
    nums = {n for row in directions.values() for n in row.values()}
    nodes, compounds = {}, {}
    with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
        for _, element in ET.iterparse(stream, events=("end",), tag=RDF + "Description"):
            uri = element.get(RDF + "about", "")
            short = uri.rsplit("/", 1)[-1]
            chosen = short.split("_", 1)[0] in nums or (
                short.startswith("Participant_") and short.split("_")[1] in nums
            )
            dest = nodes if chosen else compounds if short.startswith("Compound_") else None
            if dest is not None:
                # Multiple descriptions of the same RDF subject must be merged.
                for child in element:
                    pred = ET.QName(child).localname
                    value = child.get(RDF + "resource") or (child.text or "").strip()
                    vals = dest.setdefault(uri, {}).setdefault(pred, [])
                    if value not in vals:
                        vals.append(value)
            element.clear()
            while element.getprevious() is not None:
                del element.getparent()[0]
    needed = {v for n in nodes.values() for vs in n.values() for v in vs if v in compounds}
    nodes.update({k: compounds[k] for k in needed})
    sides = []
    balances = []
    db = sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True)
    for step in steps[1:]:
        rid = step["selected_id"].split(":")[1]
        master = step["candidate_chemical_reaction"].split(":")[1]
        assert RH + rid in nodes[RH + master]["directionalReaction"]
        assert step["canonical_name"] == nodes[RH + rid]["label"][0]
        assert step["direction"] == (
            "left_to_right" if rid == directions[master]["lr"] else "right_to_left"
        )
        delta = collections.Counter()
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
                    vals = {
                        p: v
                        for p, v in db.execute(
                            "select predicate,value from statements where subject=?", (cid,)
                        )
                        if v is not None
                    }
                    current_formula = vals["chemrof:generalized_empirical_formula"]
                    if cid in ["CHEBI:17499", "CHEBI:13193"]:
                        # Both databases explicitly use a symbolic unspecified group.
                        # ChEBI uses A/H2A; Rhea uses R/H2R, not an elemental formula.
                        assert (cid, current_formula, cp["formula"][0]) in [
                            ("CHEBI:17499", "H2A", "H2R"),
                            ("CHEBI:13193", "A", "R"),
                        ]
                    else:
                        assert current_formula == cp["formula"][0]
                    assert vals["chemrof:charge"] == cp["charge"][0]
                    assert vals.get("owl:deprecated") not in ["true", True]
                    for atom, count in formula(cp["formula"][0]).items():
                        delta[atom] += sign * coeff * count
                    delta["charge"] += sign * coeff * int(cp["charge"][0])
                    sides.append(
                        {
                            "reaction": step["selected_id"],
                            "id": cid,
                            "role": role,
                            "coefficient": coeff,
                            "participant": part,
                            "compound": compound,
                            "side": side,
                        }
                    )
        assert not {k: v for k, v in delta.items() if v}, (rid, delta)
        balances.append(
            {
                "reaction": step["selected_id"],
                "residual": dict(delta),
                "scope": "formal symbolic R-group balance; unknown donor retained"
                if rid == "16359"
                else "exact source atom/charge balance",
            }
        )
    return sides, balances


def normalization(projection, paths, doc):
    native = parse_flatfile(paths["KEGG:R01196"])["R01196"]
    assert native["EQUATION"] == [
        "2 C00138 + C00024 + C00011 + 2 C00080 <=> 2 C00139 + C00022 + C00010"
    ]
    small = parse_flatfile(paths["KEGG:C00024"])
    db = sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True)
    shifts = []
    for row in projection["first_reaction_normalization"]["native_form_bridges"]:
        facts = []
        for cid in [row["native_chebi"], row["selected_chebi"]]:
            vals = {
                p: v
                for p, v in db.execute(
                    "select predicate,value from statements where subject=?", (cid,)
                )
                if v is not None
            }
            facts.append(vals)
        assert small[row["kegg"]]["FORMULA"] == [facts[0]["chemrof:generalized_empirical_formula"]]
        before, after = [formula(v["chemrof:generalized_empirical_formula"]) for v in facts]
        delta = {a: before[a] - after[a] for a in set(before) | set(after) if before[a] != after[a]}
        assert delta == {"H": row["lost_H"]}
        assert int(facts[0]["chemrof:charge"]) - int(facts[1]["chemrof:charge"]) == row["lost_H"]

        # Exact stereochemistry/connectivity are preserved; only protonation layer changes.
        def normalize(s):
            return re.sub(r"/p[+-]?\d+", "", s)

        assert normalize(facts[0]["chemrof:inchi_string"]) == normalize(
            facts[1]["chemrof:inchi_string"]
        )
        shifts.append(dict(row, formula_shift=delta))
    assert shifts[0]["lost_H"] == shifts[1]["lost_H"] == 4
    assert 2 - shifts[2]["lost_H"] == 1
    for cid in ["C00138", "C00139"]:
        carrier = parse_flatfile(paths["KEGG:" + cid])[cid]
        assert "FORMULA" not in carrier
        node = next(p for p in doc["participants"] if p["id"] == "KEGG:" + cid)
        assert node["category"] == "chemical_entity"
        assert node["label"] == carrier["NAME"][0].rstrip(";")
    first = [s for s in projection["selected_sides"] if s["step"] == 1]
    assert len(first) == 7
    proton = next(s for s in first if s["id"] == "CHEBI:15378")
    assert proton["coefficient"] == 1 and proton["role"] == "substrates"
    assert not projection["first_reaction_normalization"]["full_formula_charge_claim"]
    return {
        "status": "passed_acid_base_derivation_only",
        "shifts": shifts,
        "native_proton_input": 2,
        "selected_proton_input": 1,
        "whole_carrier_balance": "not asserted; generic KEGG carriers lack formula and charge",
        "exact_carrier_cluster_or_sequence": "not asserted",
    }


def source_attribution_guard(doc, projection):
    """Reject source fields attributed to a different body and missing locus spans."""
    edges = {e["id"]: e for e in doc["mechanistic_edges"]}
    paths = projection["reference_original_paths"]
    primary = html.fromstring(Path(paths["PMID:19411323"]).read_bytes())
    for n, locus, paragraph in [
        (82, "1204", 3),
        (83, "0418", 6),
        (84, "1509", 8),
        (85, "1334", 9),
        (86, "1335", 9),
    ]:
        ev = edges[f"dchb-edge-{n:03}"]["evidence"][0]
        assert ev["reference_id"] == "PMID:19411323"
        assert "(//table)[1]" in ev["source_locator"]
        assert f'//*[@id="sec5"]/p[{paragraph}]' in ev["source_locator"]
        table = primary.xpath("(//table)[1]")
        assert len(table) == 1
        text = " ".join(table[0].itertext())
        loci = {
            part
            for group in re.findall(r"Tneu_(\d{4}(?:/\d{4})*)", text)
            for part in group.split("/")
        }
        assert locus in loci
        assay = primary.xpath(f'//*[@id="sec5"]/p[{paragraph}]')
        assert len(assay) == 1 and "extract" in " ".join(assay[0].itertext())
    ev = edges["dchb-edge-095"]["evidence"][0]
    assert ev["reference_id"] == "PMID:21169482"
    assert '//*[@id="sec24"]/p[1]' in ev["source_locator"]
    assert '//*[@id="sec24"]/p[2]' in ev["source_locator"]
    primary11 = html.fromstring(Path(paths["PMID:21169482"]).read_bytes())
    context = " ".join(primary11.xpath('//*[@id="sec24"]/p[2]')[0].itertext())
    assert all(word in context for word in ["Msed_0399", "native", "recombinant"])
    native = parse_flatfile(paths["KEGG:R01196"])["R01196"]
    assert "FORMULA" not in native
    small = parse_flatfile(paths["KEGG:C00024"])
    for key in ["C00024", "C00010", "C00022"]:
        assert "FORMULA" in small[key] and "DBLINKS" in small[key]
    refs = {r["id"]: r for r in doc["references"]}
    for n, idx, cid in [(103, 1, "CHEBI:15361"), (116, 2, "CHEBI:57288")]:
        evidence = edges[f"dchb-edge-{n:03}"]["evidence"]
        ev = evidence[idx]
        assert ev["reference_id"] == "KEGG:R01196"
        assert not any(
            s in ev["source_locator"] for s in ["FORMULA", "compound batch", "C00024/C00022"]
        )
        assert "EQUATION" in ev["source_locator"]
        batch = [e for e in evidence if e["reference_id"] == "KEGG:C00024"]
        chebi = [e for e in evidence if e["reference_id"] == cid]
        assert len(batch) == len(chebi) == 1
        assert "FORMULA" in batch[0]["source_locator"]
        assert "chemrof:inchi_string" in chebi[0]["source_locator"]
        assert (
            refs[cid]["source_sha256"]
            == "26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f"
        )
        assert refs["KEGG:R01196"]["source_sha256"] != refs["KEGG:C00024"]["source_sha256"]
    return {"source_blocks_corrected": 8, "separate_body_evidence_added": 4}


def issue377_checks(doc, projection):
    fix = read(D / "dchb-provenance-fix.json")
    assert fix["after_sha256"] == digest(TARGET)
    for name, expected in fix["original_nine_dossier_hashes"].items():
        assert digest(D / name) == expected
    result = source_attribution_guard(doc, projection)
    rejected = []
    for item in fix["changes"]:
        trial = copy.deepcopy(doc)
        edge = next(e for e in trial["mechanistic_edges"] if e["id"] == item["edge"])
        edge["evidence"][item["evidence_index"]] = item["before"]
        try:
            source_attribution_guard(trial, projection)
        except AssertionError:
            rejected.append(item["edge"])
        else:
            raise AssertionError("Historical source-local defect not rejected: " + item["edge"])
    assert len(rejected) == 8
    result.update(historical_defects_individually_rejected=rejected, original_dossiers_preserved=9)
    return result


def main():
    started = datetime.now(UTC).isoformat()
    initial = digest(TARGET)
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert not strict_errors([TARGET], ROOT)
    projection = read(D / "dchb-source-projection-successor.json")
    assert projection["target_sha256"] == initial
    manifest = read(D / "dchb-source-manifest-successor.json")
    for item in manifest["original_bodies"]:
        assert digest(item["path"]) == item["sha256"], item["path"]
    paths = projection["reference_original_paths"]
    refs = {r["id"]: r for r in doc["references"]}
    source_hashes = {}
    for rid, p in paths.items():
        if p not in source_hashes:
            source_hashes[p] = digest(p)
        assert source_hashes[p] == refs[rid]["source_sha256"], rid
    module = parse_flatfile(paths["KEGG:M00374"])["M00374"]
    native_members = set(re.findall(r"\bR\d{5}\b", " ".join(module["REACTION"])))
    assert len(native_members) == 14
    assert native_members == {s["native_module_reaction"][5:] for s in projection["steps"]}
    assert doc["label"] == module["NAME"][0]
    assert len(doc["reactions"]) == 14
    assert {r["id"] for r in doc["reactions"]} == {s["selected_id"] for s in projection["steps"]}
    original_sides, balances = original_rhea(projection["steps"])
    for side in original_sides:
        old = next(
            s
            for s in projection["selected_sides"]
            if (s["reaction"], s["role"], s["id"]) == (side["reaction"], side["role"], side["id"])
        )
        for key in ["participant", "compound", "coefficient"]:
            assert old[key] == side[key], (key, old, side)
    normalization_check = normalization(projection, paths, doc)
    correction_check = issue377_checks(doc, projection)
    edges = doc["mechanistic_edges"]
    chemical = [e for e in edges if e["predicate"] in ["consumes", "produces"]]
    assert len(chemical) == len(projection["selected_sides"])
    net = collections.Counter()
    for side in projection["selected_sides"]:
        rid, cid = side["reaction"], side["id"]
        sign = -1 if side["role"] == "substrates" else 1
        key = (cid, "consumes", rid) if sign < 0 else (rid, "produces", cid)
        matched = [e for e in chemical if (e["subject"], e["predicate"], e["object"]) == key]
        assert len(matched) == 1
        edge = matched[0]
        assert f"coefficient {side['coefficient']}" in edge["description"]
        if side["step"] == 1:
            assert "derived acid-base normalization" in edge["description"]
            assert "normalization" in edge["evidence"][0]["source_assertion"]
        else:
            evidence = edge["evidence"][0]
            assert evidence["reference_id"] == rid
            assert side["participant"] in evidence["source_locator"]
            assert side["compound"] in evidence["source_locator"]
        net[cid] += sign * side["coefficient"]
    net = {k: v for k, v in net.items() if v}
    assert net == {
        "KEGG:C00138": -2,
        "KEGG:C00139": 2,
        "CHEBI:57288": 1,
        "CHEBI:16526": -1,
        "CHEBI:15378": -1,
        "CHEBI:57287": -1,
        "CHEBI:30616": -3,
        "CHEBI:456215": 2,
        "CHEBI:43474": 3,
        "CHEBI:17544": -1,
        "CHEBI:17499": -1,
        "CHEBI:13193": 1,
        "CHEBI:456216": 1,
        "CHEBI:57783": -2,
        "CHEBI:58349": 2,
        "CHEBI:33019": 1,
    }, net
    # Check material continuity independently from exact source-derived sides.
    for row in projection["continuity"]:
        for rx, role in [(row["upstream"], "products"), (row["downstream"], "substrates")]:
            assert any(
                s["reaction"] == rx and s["role"] == role and s["id"] == row["intermediate"]
                for s in projection["selected_sides"]
            )
        assert any(
            e["subject"] == row["upstream"]
            and e["object"] == row["downstream"]
            and e["predicate"] == "provides_input_for"
            for e in edges
        )
    # All primary locators must resolve in original bodies to captured content hashes.
    primary_count = 0
    for source in projection["primary_assertions"]:
        root = html.fromstring(Path(paths[source["reference"]]).read_bytes())
        for row in source["rows"]:
            found = root.xpath(row["xpath"])
            assert len(found) == 1
            text = " ".join(" ".join(found[0].itertext()).split())
            assert hashlib.sha256(text.encode()).hexdigest() == row["text_sha256"]
            primary_count += 1
    primary = html.fromstring(Path(paths["PMID:19411323"]).read_bytes())
    assert primary.xpath('//*[@id="f1"]') and primary.xpath("//table[1]")
    t = " ".join(primary.xpath("//table[1]")[0].itertext())
    table_loci = {
        "Tneu_" + number
        for group in re.findall(r"Tneu_(\d{4}(?:/\d{4})*)", t)
        for number in group.split("/")
    }
    proteins = read(D / "dchb-protein-projection.json")
    body = read(proteins["original_path"])
    pointer_count = 0
    for loc, pr in proteins["selected"].items():
        entry = pointer(body, pr["source_locator"])
        assert entry["primaryAccession"] == pr["accession"]
        assert entry["organism"]["taxonId"] == 444157
        assert loc in table_loci, loc
        assert (
            hashlib.sha256(entry["sequence"]["value"].encode()).hexdigest() == pr["sequence_sha256"]
        )
    for e in edges:
        for evidence in e["evidence"]:
            if evidence["reference_id"].startswith("UniProtKB:"):
                for path in re.findall(
                    r"/results/\d+(?:/[A-Za-z_0-9]+)*", evidence["source_locator"]
                ):
                    pointer(body, path)
                    pointer_count += 1
    # No arbitrary member of four alternative PFOR locus groups is promoted to catalyst.
    excluded = {
        "UniProtKB:" + p["accession"] for p in proteins["PFOR_alternatives_not_nodes"].values()
    }
    assert not excluded & {p["id"] for p in doc["participants"]}
    assert not any(
        e["object"] == "KEGG:R01196" and e["predicate"] in ["enables", "catalyzes"] for e in edges
    )
    assert len(proteins["selected"]) == 15
    # Every retained cofactor has a matching current ECO:0000256 source assertion.
    for e in edges:
        if e["predicate"] == "has_cofactor":
            evidence = e["evidence"][0]
            c = pointer(body, evidence["source_locator"])
            assert any(v["cofactorCrossReference"]["id"] == e["object"] for v in c)
            assert all(ev["evidenceCode"] == "ECO:0000256" for v in c for ev in v["evidences"])
    export = RAW / "kgx-replay-successor"
    export.mkdir(exist_ok=True)
    write_kgx([record], export)
    rows = list(csv.DictReader((export / "edges.tsv").open(), delimiter="\t"))
    nodes = list(csv.DictReader((export / "nodes.tsv").open(), delimiter="\t"))
    assert len(rows) == len(edges) == 116
    for src, out in zip(edges, rows, strict=True):
        assert (out["subject"], out["predicate"], out["object"]) == (
            src["subject"],
            LOCAL_PREDICATE_CURIES[src["predicate"]],
            src["object"],
        )
        assert json.loads(out["evidence"]) == src["evidence"]
        assert {x["id"] for x in json.loads(out["reference_metadata"])} == {
            x["reference_id"] for x in src["evidence"]
        }
    categories = {r["id"]: r["category"] for r in nodes}
    assert categories["KEGG:M00374"] == "biolink:Pathway"
    assert categories["KEGG:R01196"] == "biolink:MolecularActivity"
    assert categories["KEGG:C00138"] == categories["KEGG:C00139"] == "biolink:ChemicalEntity"
    assert len(nodes) == 66
    assert digest(TARGET) == initial
    result = {
        "status": "passed",
        "scope": "Author source/schema/export replay, not independent review",
        "started_at": started,
        "finished_at": datetime.now(UTC).isoformat(),
        "target": str(TARGET.relative_to(ROOT)),
        "target_sha256": initial,
        "original_bodies_rehashed": len(manifest["original_bodies"]),
        "reference_original_digests_checked": len(paths),
        "full_module_reaction_objects": 14,
        "rhea_sides_reparsed": len(original_sides),
        "chemical_edges": len(chemical),
        "balances": balances,
        "kegg_first_reaction": normalization_check,
        "issue377_source_attribution_checks": correction_check,
        "net_stoichiometry": net,
        "net_scope": (
            "Selected formal bookkeeping, not whole-carrier atom/charge validation "
            "or measured physiological proton flux"
        ),
        "exact_primary_anchor_checks": primary_count,
        "uniprot_pointer_checks": pointer_count,
        "selected_proteins": 15,
        "unresolved_PFOR_alternatives_not_promoted": len(excluded),
        "native_schema": "passed",
        "closed_schema": "passed",
        "kgx": {
            "nodes": len(nodes),
            "edges": len(rows),
            "evidence": sum(len(e["evidence"]) for e in edges),
            "node_sha256": digest(export / "nodes.tsv"),
            "edge_sha256": digest(export / "edges.tsv"),
        },
        "helper_sha256": digest(Path(__file__)),
        "inputs": [
            {"path": str(p.relative_to(ROOT)), "sha256": digest(p)}
            for p in [
                TARGET,
                D / "dchb-source-projection-successor.json",
                D / "dchb-protein-projection.json",
                D / "dchb-source-manifest-successor.json",
            ]
        ],
    }
    (RAW / "replay-result-successor.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
