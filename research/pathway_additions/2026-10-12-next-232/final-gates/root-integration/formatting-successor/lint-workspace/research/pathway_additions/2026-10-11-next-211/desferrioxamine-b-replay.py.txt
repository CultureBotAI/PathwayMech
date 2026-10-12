"Offline original-source checks for an external author draft, not an independent review."

from __future__ import annotations

import collections
import copy
import csv
import hashlib
import importlib.util
import json
import re
import sqlite3
import zipfile
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import etree as ET

from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
SCOUT = Path("/private/tmp/pathwaymech-desferrioxamine-b-scout-20261011")
REPO = Path("/private/tmp/pathwaymech-next-209-20261011")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = OUT / "desferrioxamine-b-biosynthesis.yaml"
STEPS = ["LYSDECARBOX-RXN", "RXN-10995", "RXN-10996", "RXN-10999", "RXN-11001"]
CORRECTED = {
    "left": {"CPD-11955": 2, "CPD-11959": 1, "ATP": 2},
    "right": {"CPD-3764": 1, "AMP": 2, "PPI": 2, "PROTON": 2},
}


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def native(frame):
    candidates = [BASE / "originals" / f"{frame}.xml", SCOUT / "originals" / f"{frame}.xml"]
    path = next(p for p in candidates if p.exists())
    root = ET.parse(str(path)).getroot()
    node = next(x for x in root if x.tag != "metadata")
    assert node.get("frameid") == frame and node.get("orgid") == "META"
    return node


def values(curie):
    database = "ncbitaxon" if curie.startswith("NCBITaxon:") else "chebi"
    with sqlite3.connect(f"file:{CACHE}/{database}.db?mode=ro", uri=True) as connection:
        return {
            p: v
            for p, v in connection.execute(
                "select predicate,value from statements where subject=?", [curie]
            )
            if v is not None
        }


def native_sides(frame):
    node = native(frame)
    return {
        side: {
            slot.find("Compound").get("frameid"): int(slot.findtext("coefficient", "1"))
            for slot in node.findall(side)
        }
        for side in ["left", "right"]
    }


def formula(frame):
    molecule = native(frame).find("cml/molecule")
    assert molecule is not None
    f = molecule.find("formula").get("concise").split()
    assert len(f) % 2 == 0
    atoms = dict(zip(f[::2], map(int, f[1::2]), strict=True))
    atoms["charge"] = int(molecule.get("formalCharge"))
    return atoms


def balance(sides, symbolic=False):
    residual = collections.Counter()
    for side, items in sides.items():
        sign = -1 if side == "left" else 1
        for frame, count in items.items():
            if frame in ["Donor-H2", "Acceptor"]:
                assert symbolic, "Native generic acceptor has no exact formula"
                # Conditional redox bookkeeping only: the same unspecified skeleton cancels.
                f = (
                    {"H": 2, "charge": 0, "A_skeleton": 1}
                    if frame == "Donor-H2"
                    else {"charge": 0, "A_skeleton": 1}
                )
            else:
                f = formula(frame)
            for atom, n in f.items():
                residual[atom] += sign * count * n
    return {a: n for a, n in residual.items() if n}


def final_net_guard(doc, projection):
    rows = [r for r in projection["selected_sides"] if r["reaction"] == "MetaCyc:RXN-11001"]
    sides = {
        s: {r["native"]: r["coefficient"] for r in rows if r["side"] == s}
        for s in ["left", "right"]
    }
    assert sides == CORRECTED, "Reject old one-ATP equation as the current selected net"
    graph = {e["id"]: e for e in doc["mechanistic_edges"]}
    for row in rows:
        edge = graph[row["edge_id"]]
        description = edge["description"]
        assert "not exact native-equation equivalence" in description
        assert "not exact native-equation equivalence or a measured ATP/product" in description
        prim = [e for e in edge["evidence"] if e["reference_id"] == "PMID:37207292"]
        assert len(prim) == 1
        assert (
            f"curated net {row['side']} coefficient for {row['native']} is {row['coefficient']}"
            in prim[0]["source_assertion"]
        )
    assert not any(
        e["subject"] == "MetaCyc:RXN-11001"
        and e["predicate"] == "produces"
        and e["object"] == "CHEBI:15377"
        for e in doc["mechanistic_edges"]
    ), "No native source water product in corrected two-ATP net"


def must_reject(call):
    try:
        call()
    except AssertionError:
        return True
    raise AssertionError("Malformed claim was unexpectedly accepted")


def main():
    started = datetime.now(UTC).isoformat()
    doc = yaml.safe_load(TARGET.read_text())
    projection = load(OUT / "desferrioxamine-b-source-projection.json")
    assert projection["record_sha256"] == digest(TARGET)
    record = validate_record(doc)
    errors = strict_errors([TARGET], REPO)
    assert not errors, errors
    manifest = load(OUT / "desferrioxamine-b-source-manifest.json")
    for row in manifest["original_sources"]:
        assert digest(row["original_path"]) == row["sha256"], row["original_path"]
    for ref in doc["references"]:
        path = projection["reference_original_paths"][ref["id"]]
        assert digest(path) == ref["source_sha256"]
        assert len(ref["title"]) < 300, ref["id"]
    membership = native("PWY-6376").xpath("reaction-list/Reaction/@frameid")
    assert len(membership) == 5 and set(membership) == set(STEPS)
    native_rows, balances = [], []
    for frame in STEPS:
        path_layout = native("PWY-6376").xpath("reaction-layout[Reaction/@frameid=$f]", f=frame)
        assert len(path_layout) == 1 and path_layout[0].findtext("direction") == "L2R"
        original = native_sides(frame)
        selected = CORRECTED if frame == "RXN-11001" else original
        for side, entries in original.items():
            for compound, n in entries.items():
                native_rows.append(
                    {
                        "reaction": "MetaCyc:" + frame,
                        "side": side,
                        "native": compound,
                        "coefficient": n,
                    }
                )
        selected_rows = [
            x for x in projection["selected_sides"] if x["reaction"] == "MetaCyc:" + frame
        ]
        assert {
            s: {x["native"]: x["coefficient"] for x in selected_rows if x["side"] == s}
            for s in ["left", "right"]
        } == selected
        residual = balance(selected, symbolic=(frame == "RXN-10995"))
        assert not residual, (frame, residual)
        balances.append(
            {
                "native_reaction": frame,
                "residual": residual,
                "scope": (
                    "conditional generic AH2/A skeleton abstraction; not an exact"
                    " native formula or donor identity"
                )
                if frame == "RXN-10995"
                else "exact original CML atoms and charge",
            }
        )
    assert native_rows == projection["source_sides"]
    weighted_net = collections.Counter()
    multipliers = dict(zip(STEPS, [3, 3, 2, 1, 1], strict=True))
    for frame in STEPS:
        sides = CORRECTED if frame == "RXN-11001" else native_sides(frame)
        for side, entries in sides.items():
            for compound, count in entries.items():
                weighted_net[compound] += (-1 if side == "left" else 1) * multipliers[frame] * count
    weighted_net = {k: v for k, v in weighted_net.items() if v}
    assert not set(weighted_net) & {"CADAVERINE", "CPD-11953", "CPD-11955", "CPD-11959"}
    assert weighted_net["LYS"] == -3 and weighted_net["CPD-3764"] == 1
    assert weighted_net["ATP"] == -2
    ordering = {
        (x.find("predecessor-reactions/Reaction").get("frameid"), x.find("Reaction").get("frameid"))
        for x in native("PWY-6376").findall("reaction-ordering")
    }
    assert ordering == {
        (e["subject"].split(":", 1)[1], e["object"].split(":", 1)[1])
        for e in doc["mechanistic_edges"]
        if e["predicate"] == "provides_input_for"
    }
    original_net = native_sides("RXN-11001")
    assert original_net["left"]["ATP"] == 1 and original_net["right"]["WATER"] == 1
    assert not balance(original_net)
    final_net_guard(doc, projection)
    bad = copy.deepcopy(projection)
    next(
        x
        for x in bad["selected_sides"]
        if x["reaction"] == "MetaCyc:RXN-11001" and x["native"] == "ATP"
    )["coefficient"] = 1
    assert must_reject(lambda: final_net_guard(doc, bad))
    bad_doc = copy.deepcopy(doc)
    next(
        e
        for e in bad_doc["mechanistic_edges"]
        if e["id"]
        == next(
            x["edge_id"]
            for x in projection["selected_sides"]
            if x["reaction"] == "MetaCyc:RXN-11001"
        )
    )["description"] = "This is the exact native equation."
    assert must_reject(lambda: final_net_guard(bad_doc, projection))
    # Every selected chemical side has an exact graph edge and source coefficient attachment.
    edge_by_id = {e["id"]: e for e in doc["mechanistic_edges"]}
    chemical_edges = [
        e for e in doc["mechanistic_edges"] if e["predicate"] in ["consumes", "produces"]
    ]
    assert len(chemical_edges) == len(projection["selected_sides"])
    for row in projection["selected_sides"]:
        e = edge_by_id[row["edge_id"]]
        triple = (
            (row["id"], "consumes", row["reaction"])
            if row["side"] == "left"
            else (row["reaction"], "produces", row["id"])
        )
        assert (e["subject"], e["predicate"], e["object"]) == triple
        original = native_sides(row["reaction"].split(":", 1)[1])
        expected = (
            f"native {row['side']} side assigns {row['native']} "
            f"with coefficient {original[row['side']][row['native']]}"
        )
        assert expected in e["evidence"][0]["source_assertion"]
    for row in projection["chemical_identities"]:
        node = native(row["native"])
        assert node.findtext("inchi") == row["inchi"]
        if row["id"].startswith("CHEBI:"):
            v = values(row["id"])
            assert v["chemrof:inchi_string"] == row["inchi"]
            parsed = {
                a: int(n or 1)
                for a, n in re.findall(
                    r"([A-Z][a-z]?)(\d*)", v["chemrof:generalized_empirical_formula"]
                )
            }
            parsed["charge"] = int(v["chemrof:charge"])
            assert parsed == formula(row["native"])
    # Native charged states remain source-issued; neutral stale cross-references are not exact
    # mappings.
    assert [formula(f)["charge"] for f in ["CPD-11953", "CPD-11955", "CPD-11959", "CPD-3764"]] == [
        1,
        0,
        1,
        1,
    ]
    assert not doc.get("source_mappings")
    auth = load(OUT / "desferrioxamine-b-authority-inputs.json")
    spec = importlib.util.spec_from_file_location(
        "authority", REPO / "scripts/build_source_identifier_snapshot.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    canonical = {}
    for row in auth["canonical_native_terms"]:
        terms = list(module.metacyc_terms(Path(row["original_path"]).read_text()))
        matches = [t for t in terms if t[0] == row["id"]]
        assert len(matches) == 1 and matches[0][1] == row["canonical_label"]
        canonical[row["id"]] = row["canonical_label"]
    assert doc["label"] == canonical[doc["id"]]
    for node in doc["participants"] + doc["taxa"]:
        expected = (
            canonical[node["id"]]
            if node["id"].startswith("MetaCyc:")
            else values(node["id"])["rdfs:label"]
        )
        assert node["label"] == expected
    ups = load(SCOUT / "originals/uniprot-coelicolor-des.json")["results"]
    proteins = {u["primaryAccession"]: u for u in ups}
    for frame, accession in [
        ("SCO2782-MONOMER", "Q9L072"),
        ("SCO2783-MONOMER", "Q9L071"),
        ("SCO2784-MONOMER", "Q9L070"),
        ("SCO2785-MONOMER", "Q9L069"),
    ]:
        node = native(frame)
        assert node.xpath('dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [accession]
        assert node.xpath(
            'species/Organism/dblink[dblink-db="NCBI-TAXONOMY-DB"]/dblink-oid/text()'
        ) == ["100226"]
        assert proteins[accession]["organism"]["taxonId"] == 100226
        assert "unreviewed" in proteins[accession]["entryType"]
    assembly = native("CPLX-7949")
    assert assembly.xpath("component/Protein/@frameid") == ["SCO2785-MONOMER"]
    assert assembly.xpath("component/coefficient/text()") == ["2"]
    assert assembly.xpath(
        'species/Organism/dblink[dblink-db="NCBI-TAXONOMY-DB"]/dblink-oid/text()'
    ) == ["100226"]
    # Exact retained native/engineered ScDesD sequence, from original published SI tables.
    bridge = load(BASE / "desD-construct-crosscheck.json")
    extraction = load(BASE / "2022-supplement-extraction.json")
    with zipfile.ZipFile(BASE / "originals/2022-supplementary.zip") as archive:
        assert hashlib.sha256(archive.read("mmc1.pdf")).hexdigest() == extraction["sha256"]
    text = (BASE / "primary2022-si-text.txt").read_text()
    compact = re.sub(r"\s+", "", text)
    for row in bridge["results"]:
        assert row["sequence"] in compact
        assert row["core_sequence"] == proteins["Q9L069"]["sequence"]["value"]
        assert row["sequence"] == row["tag"] + row["core_sequence"]
    mismatches = load(SCOUT / "primary2023-construct-crosscheck.json")
    for row in mismatches:
        assert (
            row["native_sequence_after_tag_removal"]
            != proteins[row["accession"]]["sequence"]["value"]
        )
    assert "sequence-unmatched 2023" in doc["description"]
    for accession, cofactor in [("Q9L072", "CHEBI:597326"), ("Q9L071", "CHEBI:57692")]:
        cs = [
            cf
            for c in proteins[accession]["comments"]
            if c["commentType"] == "COFACTOR"
            for cf in c["cofactors"]
            if cf["cofactorCrossReference"]["id"] == cofactor
        ]
        assert len(cs) == 1
        assert all(e["evidenceCode"] == "ECO:0000256" for e in cs[0]["evidences"])
    # Validate exact front-article titles, not all bibliography titles.
    for pmid, pmc in [
        ("35750210", "PMC9356276"),
        ("42630954", "PMC13495013"),
        ("33784308", "PMC8009421"),
    ]:
        article = ET.parse(str(SCOUT / "originals" / (pmc + ".xml")))
        title = " ".join(
            "".join(article.find("front/article-meta/title-group/article-title").itertext()).split()
        )
        assert next(r["title"] for r in doc["references"] if r["id"] == "PMID:" + pmid) == title
    nodes_path, edges_path = write_kgx([record], BASE / "actual-kgx")
    with edges_path.open() as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    assert len(rows) == len(doc["mechanistic_edges"])
    for original, exported in zip(doc["mechanistic_edges"], rows, strict=True):
        assert exported["subject"] == original["subject"]
        assert exported["object"] == original["object"]
        assert exported["predicate"] == LOCAL_PREDICATE_CURIES[original["predicate"]]
        assert json.loads(exported["evidence"]) == original["evidence"]
        assert exported["description"] == original.get("description", "")
        refs = {r["id"]: r for r in doc["references"]}
        selected_refs = {e["reference_id"] for e in original["evidence"]}
        assert json.loads(exported["reference_metadata"]) == [
            refs[r] for r in sorted(selected_refs)
        ]
    with nodes_path.open() as f:
        nodes = {n["id"]: n for n in csv.DictReader(f, delimiter="\t")}
    for cid in ["MetaCyc:Donor-H2", "MetaCyc:Acceptor"]:
        assert nodes[cid]["category"] == "biolink:ChemicalEntity"
    report = {
        "started_at": started,
        "finished_at": datetime.now(UTC).isoformat(),
        "record_sha256": digest(TARGET),
        "status": "passed_author_replay_not_independent_review",
        "counts": {
            "participants": len(doc["participants"]),
            "reactions": 5,
            "edges": len(doc["mechanistic_edges"]),
            "evidence": sum(len(e["evidence"]) for e in doc["mechanistic_edges"]),
            "references": len(doc["references"]),
            "original_source_bodies": len(manifest["original_sources"]),
            "native_chemical_sides": len(native_rows),
            "selected_chemical_sides": len(projection["selected_sides"]),
            "kgx_nodes": len(nodes),
        },
        "native_boundary": membership,
        "weighted_full_pathway_net": weighted_net,
        "balance_checks": balances,
        "source_old_one_ATP_balanced": True,
        "primary_two_ATP_derived_not_measured": True,
        "mutation_guards": [
            "one-ATP selected claim rejected",
            "unsupported exact-native-equation claim rejected",
        ],
        "construct_scope": {
            "ScDesD_native_and_tagged_core_exact_matches": 2,
            "2023_DesABC_not_coelicolor_exact_matches": 3,
        },
        "schema_native_and_closed": "passed",
        "canonical_native_authority_count": len(canonical),
        "actual_kgx": {
            "nodes": str(nodes_path),
            "nodes_sha256": digest(nodes_path),
            "edges": str(edges_path),
            "edges_sha256": digest(edges_path),
        },
        "limitations": [
            (
                "RXN10995 atom bookkeeping uses a conditional generic redox s"
                "keleton, not complete original native chemical formulas or a"
                " specific physiological donor."
            ),
            (
                "No corpus render, global authority rebuild, full repository "
                "suite or independent scientific approval performed; external"
                " draft only."
            ),
        ],
    }
    (OUT / "desferrioxamine-b-validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
