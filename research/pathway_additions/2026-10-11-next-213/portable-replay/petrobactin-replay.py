"""Portable original-source replay for the complete petrobactin pathway.

Explicit inputs; raw originals are selected only from a SHA-bound manifest.
The output receipt and companion artifacts are written only to new output paths.
This is one-record quality control, not a whole-corpus gate or scientific approval.
"""

from __future__ import annotations

import argparse
import collections
import copy
import csv
import gzip
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import html


def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--source-manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--source-projection", type=Path)
    parser.add_argument("--identity-assessment", type=Path)
    parser.add_argument(
        "--authority-root",
        type=Path,
        help="Prepared external authority root; default is repo-root. "
        "Its policy must be byte-identical to the selected repository.",
    )
    return parser.parse_args()


def main(args):
    if sys.flags.optimize:
        raise RuntimeError("Assertions are required: do not use python -O")
    R = args.repo_root.resolve()
    TARGET = args.record.resolve()
    manifest_path = args.source_manifest.resolve()
    D = manifest_path.parent
    projection_path = (args.source_projection or D / "petrobactin-source-projection.json").resolve()
    identity_path = (
        args.identity_assessment or D / "petrobactin-identity-assessment.json"
    ).resolve()
    output = args.output.resolve()
    B = output.with_suffix(".artifacts")
    authority_root = (args.authority_root or R).resolve()
    assert (R / "src/pathwaymech").is_dir(), R
    sys.path.insert(0, str(R / "src"))
    from pathwaymech.identifiers import identifier_errors
    from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
    from pathwaymech.schema import validate_record
    from pathwaymech.strict import strict_errors

    for module_name in ["identifiers", "kgx", "schema", "strict"]:
        loaded = Path(sys.modules["pathwaymech." + module_name].__file__).resolve()
        assert loaded.is_relative_to(R / "src"), loaded
    assert not output.exists() and not B.exists(), "Output paths must be new"
    inputs = [
        TARGET,
        manifest_path,
        projection_path,
        identity_path,
        R / "conf/identifier_policy.yaml",
        R / "src/pathwaymech/schema/pathwaymech.yaml",
    ]
    captured = {str(path): sha(path) for path in inputs}
    manifest = read(manifest_path)
    assert manifest["target_sha256"] == sha(TARGET), "Stale source manifest target"
    assert read(identity_path)["target_sha256"] == sha(TARGET), "Stale identity assessment target"
    assert read(projection_path)["target_sha256"] == sha(TARGET), "Stale source projection target"
    assert (
        read(projection_path)["graph_to_source"]
        == yaml.safe_load(TARGET.read_text())["mechanistic_edges"]
    )
    # Pin the accepted correction before any expensive source work.
    asbd = next(
        e
        for e in yaml.safe_load(TARGET.read_text())["mechanistic_edges"]
        if e["id"] == "petrobactin-edge-082"
    )
    expected_description = (
        "The selected versioned Sterne AsbD protein participates in petrobactin biosynthesis. "
        "This contextual participation does not assert an exact identity between AsbD and "
        "every member of the generic carrier classes."
    )
    assert asbd["subject"] == "NCBIProtein:AAT54156.1"
    assert asbd["predicate"] == "part_of" and asbd["object"] == "MetaCyc:PWY-6289"
    assert asbd["description"] == expected_description, "Issue 388 AsbD scope regression"
    accepted = manifest["sources"]
    assert accepted and all(s.get("accepted") is True for s in accepted)
    by_ref, by_name, path_hashes = {}, {}, {}
    for entry in accepted:
        path = Path(entry["path"])
        if not path.is_absolute():
            path = D / path
        path = path.resolve()
        assert re.fullmatch(r"[a-f0-9]{64}", entry["sha256"])
        assert entry.get("url", "").startswith(("https://", "http://"))
        previous = path_hashes.setdefault(path, entry["sha256"])
        assert previous == entry["sha256"], "Conflicting digests for one original"
        if "reference_id" in entry:
            value = (path, entry["sha256"])
            assert by_ref.setdefault(entry["reference_id"], value) == value
        by_name.setdefault(path.name, set()).add(path)
    for path, expected in path_hashes.items():
        assert sha(path) == expected, f"Original-body digest mismatch: {path}"
    assert not any(path == output or path.is_relative_to(B) for path in path_hashes)
    assert not any(path == output or path.is_relative_to(B) for path in inputs)
    B.mkdir(parents=True)

    def source_path(reference_id):
        return by_ref[reference_id][0]

    def source_name(name):
        matches = by_name[name]
        assert len(matches) == 1, f"Ambiguous source basename: {name}"
        return next(iter(matches))

    def save(name, value):
        (B / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

    def replay_originals():
        RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        RH = "http://rdf.rhea-db.org/"
        NOW = datetime.now(UTC).isoformat()
        source = manifest["sources"]
        raw = gzip.decompress(source_path("RHEA:48405").read_bytes()).decode()
        starts = {}
        for m in re.finditer(r'<rdf:Description rdf:about="([^"]+)">', raw):
            starts.setdefault(m[1], []).append(m.start())
        wrapper = (
            '<root xmlns:rh="'
            + RH
            + '" xmlns:rdf="'
            + RDF
            + '" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">'
        )
        nodes = {}

        def node(uri):
            if uri in nodes:
                return nodes[uri]
            props = {}
            assert uri in starts, uri
            for start in starts[uri]:
                end = raw.index("</rdf:Description>", start) + len("</rdf:Description>")
                item = ET.fromstring(wrapper + raw[start:end] + "</root>")[0]
                for child in item:
                    key = child.tag.split("}", 1)[1]
                    val = child.get("{" + RDF + "}resource") or child.text
                    if val not in props.setdefault(key, []):
                        props[key].append(val)
            nodes[uri] = props
            return props

        directions = {}
        masters = [
            "48404",
            "24848",
            "62468",
            "62476",
            "63808",
            "63812",
            "63816",
            "64028",
            "64024",
            "63820",
        ]
        for master in masters:
            props = node(RH + master)
            directions[master] = {"master": master}
            for directed in props["directionalReaction"]:
                dp = node(directed)
                if dp["substrates"] == [RH + master + "_L"] and dp["products"] == [
                    RH + master + "_R"
                ]:
                    key = "left_to_right"
                else:
                    assert dp["substrates"] == [RH + master + "_R"]
                    assert dp["products"] == [RH + master + "_L"]
                    key = "right_to_left"
                assert key not in directions[master]
                directions[master][key] = directed.removeprefix(RH)
            assert len(props["bidirectionalReaction"]) == 1
            directions[master]["bidirectional"] = props["bidirectionalReaction"][0].removeprefix(RH)
            assert set(directions[master]) == {
                "master",
                "left_to_right",
                "right_to_left",
                "bidirectional",
            }
        assert len(directions) == 10
        queue = {RH + x for d in directions.values() for x in d.values()}
        while queue:
            uri = queue.pop()
            props = node(uri)
            for k, values in props.items():
                if k in {
                    "side",
                    "substrates",
                    "products",
                    "contains",
                    "compound",
                    "reactivePart",
                    "underlyingChebi",
                    "chebi",
                } or re.fullmatch(r"contains\d+", k):
                    queue.update(v for v in values if v and v.startswith(RH) and v not in nodes)

        con = sqlite3.connect("file:" + str(source_path("CHEBI:149594")) + "?mode=ro", uri=True)
        chemical_facts = {}

        def chebi_id(uri):
            m = re.search(r"CHEBI[_:](\d+)", uri)
            assert m, uri
            return "CHEBI:" + m[1]

        def chemical(cid):
            if cid not in chemical_facts:
                facts = dict(
                    con.execute(
                        (
                            "select predicate,value from statements where subject=? and v"
                            "alue is not null"
                        ),
                        [cid],
                    ).fetchall()
                )
                chemical_facts[cid] = {
                    k: facts.get(k)
                    for k in [
                        "rdfs:label",
                        "chemrof:generalized_empirical_formula",
                        "chemrof:charge",
                        "chemrof:inchi_string",
                    ]
                }
            return chemical_facts[cid]

        def compound(uri):
            p = node(uri)
            if "reactivePart" in p:
                parts = [
                    {"uri": rp, "chebi": chebi_id(node(rp)["chebi"][0])} for rp in p["reactivePart"]
                ]
                for part in parts:
                    part["facts"] = chemical(part["chebi"])
                return {
                    "uri": uri,
                    "id": "RHEA-COMP:" + p["id"][0],
                    "label": p["name"][0],
                    "reactive_parts": parts,
                    "scope": (
                        "whole generic polypeptide class; reactive part is not the whole carrier"
                    ),
                }
            cid = chebi_id(p["chebi"][0])
            return {"uri": uri, "id": cid, "facts": chemical(cid)}

        def side(uri):
            p = node(uri)
            members = p.get("contains", [])
            out = []
            for member in members:
                keys = [k for k, v in p.items() if re.fullmatch(r"contains\d+", k) and member in v]
                assert len(keys) == 1, (uri, member, keys)
                coefficient = int(keys[0].removeprefix("contains"))
                c = compound(node(member)["compound"][0])
                out.append(
                    {
                        "side_uri": uri,
                        "coefficient_predicate": RH + keys[0],
                        "participant_uri": member,
                        "coefficient": coefficient,
                        **c,
                    }
                )
            assert len(out) == len(members) and out
            return out

        def atom_vector(formula):
            tokens = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
            assert "".join(a + b for a, b in tokens) == formula, formula
            out = {}
            for atom, amount in tokens:
                out[atom] = out.get(atom, 0) + int(amount or 1)
            return out

        reactions = []
        for master in masters:
            d = directions[master]
            m = node(RH + master)
            rid = d["left_to_right"]
            p = node(RH + rid)
            assert RH + rid in m.get("directionalReaction", [])
            left = side(p["substrates"][0])
            right = side(p["products"][0])
            total = {}
            carrier_total = 0
            for sign, terms in [(-1, left), (1, right)]:
                for term in terms:
                    n = sign * term["coefficient"]
                    if "reactive_parts" in term:
                        facts = [q["facts"] for q in term["reactive_parts"]]
                        carrier_total += n
                    else:
                        facts = [term["facts"]]
                    for f in facts:
                        for atom, count in atom_vector(
                            f["chemrof:generalized_empirical_formula"]
                        ).items():
                            total[atom] = total.get(atom, 0) + count * n
                        total["charge"] = total.get("charge", 0) + int(f["chemrof:charge"]) * n
            residual = {k: v for k, v in total.items() if v}
            assert not residual and carrier_total == 0
            reactions.append(
                {
                    "master": "RHEA:" + master,
                    "selected": "RHEA:" + rid,
                    "family": d,
                    "status": p.get("status"),
                    "equation": p["equation"][0],
                    "substrates": left,
                    "products": right,
                    "reactive_part_atom_and_charge_residual": residual,
                    "carrier_class_count_residual": carrier_total,
                    "balance_scope": (
                        "Generic-carrier reactions conditionally balance matched unsp"
                        "ecified protein scaffolds; this is not a full AsbD sequence "
                        "or an enzyme-assembly count."
                    ),
                }
            )
        con.close()
        save(
            "rhea-source-projection.json",
            {
                "created_at": NOW,
                "originals": source,
                "selected_reactions": reactions,
                "nodes": nodes,
                "chemical_facts_source": str(source_path("CHEBI:149594")),
            },
        )
        print("Rhea reactions", len(reactions), "nodes", len(nodes))
        for r in reactions:
            print(
                r["selected"],
                r["reactive_part_atom_and_charge_residual"],
                r["carrier_class_count_residual"],
            )

        # Compare issuing genome translations to reviewed entries without exporting sequences.
        text = source_path("NCBITaxon:260799").read_text()
        assert (
            text.startswith("ID   AE017225; SV 1;")
            and "DE   Bacillus anthracis str. Sterne" in text
        )
        blocks = re.split(r"(?m)(?=^FT   \S)", text)
        cds = []
        for block in blocks:
            if not block.startswith("FT   CDS"):
                continue
            cleaned = "\n".join(line[21:] for line in block.splitlines() if line.startswith("FT"))
            qualifiers = {m[1]: m[2] for m in re.finditer(r'/(\w+)="([^"]*)"', cleaned, re.S)}
            if qualifiers.get("protein_id") in {f"AAT5415{i}.1" for i in range(3, 9)}:
                cds.append(qualifiers)
        assert len(cds) == 6
        comparisons = []
        for q, accession in zip(
            sorted(cds, key=lambda x: x["protein_id"]),
            ["Q81RQ9", "Q81RQ8", "Q81RQ7", "Q81RQ6", "Q81RQ5", "Q81RQ4"],
            strict=True,
        ):
            data = json.loads(source_path("UniProtKB:" + accession).read_text())
            seq = "".join(q["translation"].split())
            current = data["sequence"]["value"]
            comparisons.append(
                {
                    "genome_protein_id": q["protein_id"],
                    "gene": q.get("gene"),
                    "locus_tag": q.get("locus_tag"),
                    "genome_product": q.get("product"),
                    "reviewed_uniprot": accession,
                    "genome_translation_sha256": hashlib.sha256(seq.encode()).hexdigest(),
                    "reviewed_sequence_sha256": hashlib.sha256(current.encode()).hexdigest(),
                    "genome_length": len(seq),
                    "reviewed_length": len(current),
                    "exact_sequence_equal": seq == current,
                    (
                        "source_is_exact_contiguous_subsequence_of_reviewed_at_zero_based"
                    ): current.find(seq),
                    "reviewed_is_exact_contiguous_subsequence_of_source_at_zero_based": seq.find(
                        current
                    ),
                    "same_length_mismatch_count": sum(
                        a != b for a, b in zip(seq, current, strict=True)
                    )
                    if len(seq) == len(current)
                    else None,
                }
            )
        save(
            "genome-identity-comparison.json",
            {
                "created_at": NOW,
                "source": {
                    "path": str(source_path("NCBITaxon:260799")),
                    "sha256": sha(source_path("NCBITaxon:260799")),
                },
                "source_scope": (
                    "Original issued genomic CDS translation annotations, not ind"
                    "ependently retranslated nucleotide sequence; sequence equali"
                    "ty is not identity of tagged experimental constructs."
                ),
                "comparisons": comparisons,
            },
        )
        print(
            "Source protein identity comparisons",
            [
                (
                    x["genome_protein_id"],
                    x["reviewed_uniprot"],
                    x["exact_sequence_equal"],
                    x["same_length_mismatch_count"],
                )
                for x in comparisons
            ],
        )

        # The exact compound bridge is deliberately independent of formula balance.
        mapping = {
            "3-DEHYDRO-SHIKIMATE": "CHEBI:16630",
            "3-4-DIHYDROXYBENZOATE": "CHEBI:36241",
            "CIT": "CHEBI:16947",
            "SPERMIDINE": "CHEBI:57834",
            "CPD-11474": "CHEBI:144942",
            "CPD-11479": "CHEBI:149586",
            "CPD-11480": "CHEBI:149592",
            "CPD-11477": "CHEBI:149593",
            "CPD-11481": "CHEBI:149594",
            "CPD-9985": "CHEBI:142778",
        }
        con = sqlite3.connect("file:" + str(source_path("CHEBI:149594")) + "?mode=ro", uri=True)
        bridges = []
        for native_id, cid in mapping.items():
            path = source_path("MetaCyc:" + native_id)
            compound_node = ET.parse(path).getroot().find("Compound")
            assert compound_node.get("frameid") == native_id
            mol = compound_node.find("cml/molecule")
            facts = dict(
                con.execute(
                    "select predicate,value from statements where subject=? and value is not null",
                    [cid],
                ).fetchall()
            )
            native_inchi = compound_node.findtext("inchi")
            current_inchi = facts["chemrof:inchi_string"]
            bridges.append(
                {
                    "native": "MetaCyc:" + native_id,
                    "chebi": cid,
                    "source": {"path": str(path), "sha256": sha(path)},
                    "native_inchi": native_inchi,
                    "chebi_inchi": current_inchi,
                    "exact_inchi_equal": native_inchi == current_inchi,
                    "native_formula": mol.find("formula").get("concise"),
                    "chebi_formula": facts["chemrof:generalized_empirical_formula"],
                    "native_charge": mol.get("formalCharge"),
                    "chebi_charge": facts["chemrof:charge"],
                }
            )
        con.close()
        assert sum(x["exact_inchi_equal"] for x in bridges) == 9
        terminal = next(x for x in bridges if x["native"] == "MetaCyc:CPD-9985")
        assert terminal["chebi_inchi"] in source_path("CHEBI:142778").read_text()

        def arm_lengths(inchi):
            """Measure N-to-N carbon paths from the original single-component InChI connectivity."""
            formula, connectivity = inchi.split("/")[1:3]
            assert formula == "C34H50N6O11" and connectivity.startswith("c")
            graph = {i: set() for i in range(1, 52)}
            stack = []
            current = None
            for token in re.findall(r"\d+|[(),-]", connectivity[1:]):
                if token.isdigit():
                    n = int(token)
                    if current is not None:
                        graph[current].add(n)
                        graph[n].add(current)
                    current = n
                elif token == "(":
                    stack.append(current)
                elif token == ")":
                    current = stack.pop()
                elif token == ",":
                    current = stack[-1]
            assert not stack and all(graph.values())

            def in_cycle(n):
                neighbors = list(graph[n])
                for start in neighbors:
                    wanted = set(neighbors) - {start}
                    todo, visited = [start], {n}
                    while todo:
                        v = todo.pop()
                        if v in visited:
                            continue
                        if v in wanted:
                            return True
                        visited.add(v)
                        todo.extend(graph[v] - visited)
                return False

            result = {"aromatic_amide_to_inner_nitrogen": [], "citrate_amide_to_inner_nitrogen": []}
            for n in range(35, 41):
                carbonyl = [
                    c
                    for c in graph[n]
                    if c <= 34 and any(o >= 41 and len(graph[o]) == 1 for o in graph[c])
                ]
                if not carbonyl:
                    continue
                assert len(carbonyl) == 1
                c = carbonyl[0]
                other_c = [x for x in graph[c] if x <= 34]
                assert len(other_c) == 1
                key = (
                    "aromatic_amide_to_inner_nitrogen"
                    if in_cycle(other_c[0])
                    else "citrate_amide_to_inner_nitrogen"
                )
                path = [x for x in graph[n] if x != c]
                assert len(path) == 1
                previous, current, count = n, path[0], 0
                while current <= 34:
                    count += 1
                    onward = graph[current] - {previous}
                    assert len(onward) == 1
                    previous, current = current, next(iter(onward))
                assert 35 <= current <= 40
                result[key].append(count)
            for value in result.values():
                value.sort()
            return result

        native_arms, chebi_arms = (
            arm_lengths(terminal["native_inchi"]),
            arm_lengths(terminal["chebi_inchi"]),
        )
        assert native_arms == {
            "aromatic_amide_to_inner_nitrogen": [3, 3],
            "citrate_amide_to_inner_nitrogen": [4, 4],
        }
        assert chebi_arms == {
            "aromatic_amide_to_inner_nitrogen": [4, 4],
            "citrate_amide_to_inner_nitrogen": [3, 3],
        }
        save(
            "chemical-identity-adjudication.json",
            {
                "created_at": NOW,
                "bridges": bridges,
                "terminal_connectivity": {
                    "native": native_arms,
                    "chebi": chebi_arms,
                    "live_chebi_original": {
                        "path": str(source_path("CHEBI:142778")),
                        "sha256": sha(source_path("CHEBI:142778")),
                    },
                    "primary_figure": {
                        "path": str(source_name("PMC3346087-F1.jpg")),
                        "sha256": sha(source_name("PMC3346087-F1.jpg")),
                        "locator": "PMID:22408253 Figure 1A and terminal product in Figure 1C",
                        "inspection": (
                            "Prior recorded visual inspection; this replay checks origina"
                            "l image bytes and independently recomputes InChI connectivit"
                            "y, not a new automated interpretation of the figure."
                        ),
                    },
                    "decision": (
                        "Do not assert exact identity between MetaCyc:CPD-9985 and CH"
                        "EBI:142778. Equal formula, charge and a database cross-refer"
                        "ence do not establish connectivity equivalence. Terminal Rhe"
                        "a atom balance is not validation of its product structure."
                    ),
                },
                "scope": (
                    "Original-source technical replay, not independent scientific"
                    " approval or a new experimental finding."
                ),
            },
        )
        print(
            "Chemical bridges",
            len(bridges),
            "exact",
            sum(x["exact_inchi_equal"] for x in bridges),
            "terminal constitutional conflict verified",
        )

    started = datetime.now(UTC).isoformat()
    raw = yaml.safe_load(TARGET.read_text())
    record = validate_record(raw)
    assert not strict_errors([TARGET], R)
    p = read(projection_path)
    assert p["target_sha256"] == sha(TARGET)
    assert p["graph_to_source"] == raw["mechanistic_edges"]
    # Reparse original full RDF, native structures and genome translations in this process.
    replay_originals()
    fresh = read(B / "rhea-source-projection.json")
    byrid = {r["selected"]: r for r in fresh["selected_reactions"]}
    assert len(byrid) == 10
    native = ET.parse(source_path("MetaCyc:PWY-6289")).getroot().find("Pathway")
    members = [x.get("frameid") for x in native.findall("reaction-list/Reaction")]
    assert len(members) == len(set(members)) == 10
    mapping = {x["native"]: x["reaction"] for x in p["source_to_graph"]}
    assert set(members) == set(mapping)
    assert set(mapping.values()) == {r["id"] for r in raw["reactions"]}
    assert all(r["direction"] == "left_to_right" for r in raw["reactions"])
    for n in members:
        e = ET.parse(source_path("MetaCyc:" + n)).getroot().find("Reaction")
        assert e.get("frameid") == n
        assert e.findtext("reaction-direction") in {"LEFT-TO-RIGHT", "PHYSIOL-LEFT-TO-RIGHT"}
        layouts = [
            x for x in native.findall("reaction-layout") if x.find("Reaction").get("frameid") == n
        ]
        assert len(layouts) == 1 and layouts[0].findtext("direction") == "L2R"
    # Exact native side identity and coefficients are independent of current equation labels.
    native_sides = []
    for n in members:
        e = ET.parse(source_path("MetaCyc:" + n)).getroot().find("Reaction")
        sides = {}
        for name in ["left", "right"]:
            sides[name] = [
                {"id": x[0].get("frameid"), "coefficient": int(x.findtext("coefficient") or 1)}
                for x in e.findall(name)
            ]
        native_sides.append(
            {"native": n, "direction": e.findtext("reaction-direction"), "sides": sides}
        )
    assert len(p["chemical_sides"]) == 54
    for s in p["chemical_sides"]:
        source = byrid[s["source_rhea"]]
        exact = next(
            t
            for t in source[s["role"]]
            if t["participant_uri"] == s["source_side"]["participant_uri"]
        )
        assert exact == s["source_side"]
        expected_id = exact["id"]
        if s["reaction"] == "MetaCyc:RXN-10679" and expected_id == "CHEBI:142778":
            expected_id = "MetaCyc:CPD-9985"
        assert s["identifier"] == expected_id and s["coefficient"] == exact["coefficient"]
        sub, obj = (
            (expected_id, s["reaction"])
            if s["role"] == "substrates"
            else (s["reaction"], expected_id)
        )
        matches = [
            e
            for e in raw["mechanistic_edges"]
            if e["subject"] == sub
            and e["object"] == obj
            and e["predicate"] == ("consumes" if s["role"] == "substrates" else "produces")
        ]
        assert len(matches) == 1
    # Atom/charge balance is separate from identity. The terminal native structure is checked first.
    chem = read(B / "chemical-identity-adjudication.json")
    assert sum(x["exact_inchi_equal"] for x in chem["bridges"]) == 9
    assert len(chem["bridges"]) == 10
    for key in ["native", "chebi"]:
        assert (
            chem["terminal_connectivity"][key]
            == read(identity_path)["chemical_comparisons"]["terminal_connectivity"][key]
        )
    # Source replay itself asserts nine matching InChIs and unequal terminal carbon-arm
    # connectivity.
    terminal = ET.parse(source_path("MetaCyc:CPD-9985")).getroot().find("Compound")
    assert terminal.get("frameid") == "CPD-9985"
    assert terminal.find("cml/molecule").get("formalCharge") == "1"
    formula = terminal.find("cml/molecule/formula").get("concise")
    assert formula == "C 34 H 51 N 6 O 11", formula
    assert all(not r["reactive_part_atom_and_charge_residual"] for r in fresh["selected_reactions"])
    assert all(r["carrier_class_count_residual"] == 0 for r in fresh["selected_reactions"])
    # Maturation is a separate priming transformation, not a per-product cost.
    base = {
        "RHEA:24849": 2,
        "RHEA:62469": 2,
        "RHEA:62477": 2,
        "RHEA:63809": 1,
        "MetaCyc:RXN-10679": 1,
    }
    branch_a = base | {"RHEA:63813": 1, "RHEA:64025": 1}
    branch_b = base | {"RHEA:64029": 1, "RHEA:63817": 1}

    def net(flux):
        total = collections.Counter()
        for side in p["chemical_sides"]:
            factor = flux.get(side["reaction"], 0)
            sign = -1 if side["role"] == "substrates" else 1
            total[side["identifier"]] += sign * factor * side["coefficient"]
        return {key: value for key, value in sorted(total.items()) if value}

    net_a, net_b = net(branch_a), net(branch_b)
    assert net_a == net_b
    assert net_a["MetaCyc:CPD-9985"] == 1
    assert net_a["CHEBI:30616"] == -4 and net_a["CHEBI:456215"] == 4
    assert not any(x.startswith("RHEA-COMP:") for x in net_a)
    # Meaningful negative guards address known source conflicts rather than mirror arbitrary
    # formatting.

    def guard(doc):
        all_ids = {x["id"] for s in ["participants", "reactions"] for x in doc[s]}
        assert "CHEBI:142778" not in all_ids, (
            "Rejected constitutional isomer must not become terminal product"
        )
        assert "RHEA:63821" not in {x["id"] for x in doc["reactions"]}, (
            "No exact terminal equation equivalence"
        )
        assert "RHEA:62461" not in all_ids, (
            "Net AsbC would double-count its retained component reactions"
        )
        assert len(doc["reactions"]) == 10
        assert not doc.get("source_mappings"), "No false cross-source exactMatch"
        assert not any(
            e["object"] == "RHEA:48405" and e["predicate"] in {"enables", "catalyzes"}
            for e in doc["mechanistic_edges"]
        ), "Physiological maturation catalyst remains unassigned"
        for edge in doc["mechanistic_edges"]:
            for evidence in edge["evidence"]:
                if evidence["reference_id"].startswith("MetaCyc:"):
                    assert "unification cross-reference" not in evidence.get("source_assertion", "")

    guard(raw)
    negative = []
    for kind in ["wrong_terminal_product", "invented_maturation_catalyst", "truncated_boundary"]:
        bad = copy.deepcopy(raw)
        if kind == "wrong_terminal_product":
            next(x for x in bad["participants"] if x["id"] == "MetaCyc:CPD-9985")["id"] = (
                "CHEBI:142778"
            )
        elif kind == "invented_maturation_catalyst":
            bad["mechanistic_edges"].append(
                {
                    "subject": "NCBIProtein:AAT54156.1",
                    "predicate": "catalyzes",
                    "object": "RHEA:48405",
                }
            )
        else:
            bad["reactions"] = [x for x in bad["reactions"] if x["id"] != "RHEA:48405"]
        try:
            guard(bad)
        except AssertionError:
            negative.append(kind)
        else:
            raise AssertionError("Known invalid mutation was accepted: " + kind)
    # Rehash every actual reference original, keeping original full-body versus projection scope
    # clear.
    ref_reports = []
    for ref in raw["references"]:
        path = source_path(ref["id"])
        assert path_hashes[path] == ref["source_sha256"], ref["id"]
        source_entry = next(s for s in accepted if s.get("reference_id") == ref["id"])
        assert source_entry["url"] == ref["url"], ref["id"]
        ref_reports.append(
            {"reference_id": ref["id"], "path": str(path), "sha256": ref["source_sha256"]}
        )
    # Recheck source-native protein identities against issuing genome annotations.
    comparisons = read(B / "genome-identity-comparison.json")["comparisons"]
    assert sum(x["exact_sequence_equal"] for x in comparisons) == 4
    ncbi = {
        x.findtext("GBSeq_accession-version"): x
        for x in ET.parse(source_path("NCBIProtein:AAT54153.1")).getroot()
    }
    assert len(ncbi) == 6
    for c in comparisons:
        n = ncbi[c["genome_protein_id"]]
        assert (
            hashlib.sha256(n.findtext("GBSeq_sequence").upper().encode()).hexdigest()
            == c["genome_translation_sha256"]
        )
        qs = {
            x.findtext("GBQualifier_name"): x.findtext("GBQualifier_value")
            for f in n.findall("GBSeq_feature-table/GBFeature")
            if f.findtext("GBFeature_key") == "source"
            for x in f.findall("GBFeature_quals/GBQualifier")
        }
        assert qs["strain"] == "Sterne" and qs["db_xref"] == "taxon:260799"
    # Literal excerpt and metadata titles must occur at the actual inspected source selectors.
    quotes = 0
    for e in raw["mechanistic_edges"]:
        for v in e["evidence"]:
            if "quote" in v:
                tree = html.fromstring(source_path(v["reference_id"]).read_bytes())
                text = " ".join(" ".join(tree.xpath('//*[@id="sec5"]/p[2]')[0].itertext()).split())
                assert v["quote"] in text
                quotes += 1
    for pmid in ["PMID:22408253", "PMID:18955706"]:
        ref = next(x for x in raw["references"] if x["id"] == pmid)
        tree = html.fromstring(source_path(pmid).read_bytes())
        assert ref["title"] == tree.xpath('//meta[@name="citation_title"]/@content')[0]
    # Isolate the selected record while preserving the repository policy exactly.
    sandbox = B / "identifier-sandbox"
    (sandbox / "data/pathways").mkdir(parents=True)
    (sandbox / "conf").mkdir()
    shutil.copyfile(TARGET, sandbox / "data/pathways" / TARGET.name)
    policy = R / "conf/identifier_policy.yaml"
    assert sha(authority_root / "conf/identifier_policy.yaml") == sha(policy)
    shutil.copyfile(policy, sandbox / "conf/identifier_policy.yaml")
    authority_inputs = {}
    for entry in yaml.safe_load(policy.read_text())["namespaces"].values():
        rel = Path(entry["snapshot"])
        assert not rel.is_absolute() and ".." not in rel.parts
        original = authority_root / rel
        authority_inputs[str(original)] = sha(original)
        destination = sandbox / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, destination)
    assert not identifier_errors(sandbox)
    assert sha(sandbox / "data/pathways" / TARGET.name) == sha(TARGET)
    # Actual exported bytes preserve every evidence item and original reference metadata.
    nodes_file, edges_file = write_kgx([record], B / "kgx")
    nodes = list(csv.DictReader(nodes_file.open(), delimiter="\t"))
    exported = list(csv.DictReader(edges_file.open(), delimiter="\t"))
    assert len(exported) == len(raw["mechanistic_edges"]) == 94
    refmap = {x["id"]: x for x in raw["references"]}
    for e, out in zip(raw["mechanistic_edges"], exported, strict=True):
        assert (out["subject"], out["predicate"], out["object"]) == (
            e["subject"],
            LOCAL_PREDICATE_CURIES[e["predicate"]],
            e["object"],
        )
        assert json.loads(out["evidence"]) == e["evidence"]
        assert out["description"] == e.get("description", "")
        assert json.loads(out["reference_metadata"]) == [
            refmap[k] for k in sorted({v["reference_id"] for v in e["evidence"]})
        ]
    for n in nodes:
        if n["id"].startswith("RHEA-COMP:"):
            assert n["category"] == "biolink:ChemicalEntity"
    assert (
        next(x for x in nodes if x["id"] == "MetaCyc:CPD-9985")["category"]
        == "biolink:SmallMolecule"
    )
    result = {
        "started_at": started,
        "finished_at": datetime.now(UTC).isoformat(),
        "status": "passed_author_checks_not_independent_approval",
        "target_sha256": sha(TARGET),
        "native_and_closed_schema": "passed",
        "canonical_identifier_check": "passed_external_sandbox",
        "complete_native_members": 10,
        "both_branches_retained": True,
        "original_rhea_reactions_reparsed": 10,
        "selected_chemical_sides": 54,
        "formal_balances": 10,
        "balance_scope": (
            "Matched generic protein scaffolds plus reactive parts; "
            "does not validate identity or specify assembly stoichiometry"
        ),
        "terminal_identity": (
            "Native CPD-9985, independently checked connectivity; "
            "Rhea terminal small-product mapping rejected"
        ),
        "branch_a_flux": branch_a,
        "branch_b_flux": branch_b,
        "same_derived_net": net_a,
        "net_limit": (
            "Derived four ATP-to-AMP events per product, not direct ATP/product measurement; "
            "maturation is separate priming and not added per product"
        ),
        "negative_guards_rejected": negative,
        "native_source_sides": native_sides,
        "source_reference_checks": ref_reports,
        "source_protein_comparisons": comparisons,
        "literal_quotes_checked": quotes,
        "kgx": {
            "nodes": len(nodes),
            "edges": len(exported),
            "evidence": sum(len(x["evidence"]) for x in raw["mechanistic_edges"]),
            "nodes_sha256": sha(nodes_file),
            "edges_sha256": sha(edges_file),
        },
        "deferred_integration_gates": [
            "shared corpus render-pages",
            "full just validate",
            "full just test",
            "base-aware history and independent review",
        ],
        "reference_repository": {
            "path": str(R),
            "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=R, text=True).strip(),
        },
        "helper_sha256": sha(__file__),
        "source_manifest": {"path": str(manifest_path), "sha256": sha(manifest_path)},
        "original_body_checks": [{"path": str(k), "sha256": v} for k, v in path_hashes.items()],
        "authority_input_scope": {
            "root": str(authority_root),
            "snapshots": authority_inputs,
            "limitation": "One-record check; no corpus or baseline-integration claim",
        },
        "input_checks": captured,
        "issue388_scope_guard": "passed; exact corrected protein description retained",
        "rhea_direction_source": (
            "Full original RDF family/left-right sides; no external TSV dependency"
        ),
    }
    for path, expected in captured.items():
        assert sha(path) == expected, f"Input changed during replay: {path}"
    for path, expected in authority_inputs.items():
        assert sha(path) == expected, f"Authority changed during replay: {path}"
    with output.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                k: result[k]
                for k in [
                    "status",
                    "target_sha256",
                    "complete_native_members",
                    "selected_chemical_sides",
                    "formal_balances",
                    "kgx",
                ]
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main(parse_args())
