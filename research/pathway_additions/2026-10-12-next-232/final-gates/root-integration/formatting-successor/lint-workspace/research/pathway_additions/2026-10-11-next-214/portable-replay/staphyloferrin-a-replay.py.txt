"""Portable one-record source replay; implementation work, not independent approval.

All inputs are explicit. Original metadata and bytes are preserved; only a new
external receipt and its exclusively created companion directory may be written.
No network access, maintained output, or whole-corpus gate is performed.
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
from datetime import UTC, datetime
from functools import cache
from pathlib import Path

import yaml
from lxml import etree as ET
from lxml import html


def fresh_sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


@cache
def sha(path):
    return fresh_sha(path)


def read(path):
    return json.loads(Path(path).read_text())


def norm(text):
    return " ".join(text.split())


def metadata(path):
    stat = Path(path).stat()
    return {"bytes": stat.st_size, "mode": stat.st_mode, "mtime_ns": stat.st_mtime_ns}


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ["repo-root", "record", "source-manifest", "source-projection", "output"]:
        parser.add_argument("--" + name, required=True, type=Path)
    parser.add_argument(
        "--authority-root",
        type=Path,
        help="Optional prepared authority root; policy must match repo-root exactly",
    )
    parser.add_argument(
        "--stereo-python",
        type=Path,
        help="Explicit Python interpreter with RDKit; defaults to current interpreter",
    )
    return parser.parse_args()


def main(args):
    started = datetime.now(UTC).isoformat()
    sys.dont_write_bytecode = True
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled; python -O is unsupported")
    R = args.repo_root.resolve(strict=True)
    T = args.record.resolve(strict=True)
    manifest_path = args.source_manifest.resolve(strict=True)
    projection_path = args.source_projection.resolve(strict=True)
    output = args.output.absolute()
    assert not output.is_symlink() and not output.exists(), "Output receipt must be new"
    output = output.resolve()
    B = output.with_suffix(".artifacts")
    assert not B.exists() and not B.is_symlink(), "Companion directory must be new"
    assert not output.is_relative_to(R) and not B.is_relative_to(R), "External outputs only"
    authority_root = (args.authority_root or R).resolve(strict=True)
    # Preserve a virtualenv interpreter symlink: resolving it changes its import environment.
    stereo_python = (args.stereo_python or Path(sys.executable)).absolute()
    assert stereo_python.is_file(), stereo_python
    stereo_probe = subprocess.run(
        [
            str(stereo_python),
            "-B",
            "-c",
            "from rdkit import Chem, rdBase; print(rdBase.rdkitVersion)",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert stereo_probe.returncode == 0, stereo_probe.stderr
    assert (R / "src/pathwaymech").is_dir()
    sys.path.insert(0, str(R / "src"))
    from pathwaymech.identifiers import identifier_errors
    from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
    from pathwaymech.schema import validate_record
    from pathwaymech.strict import strict_errors

    for name in ["identifiers", "kgx", "schema", "strict"]:
        assert Path(sys.modules["pathwaymech." + name].__file__).resolve().is_relative_to(R / "src")
    policy = R / "conf/identifier_policy.yaml"
    authority_policy = authority_root / "conf/identifier_policy.yaml"
    assert sha(policy) == sha(authority_policy), "Authority policy must be byte-identical"
    inputs = [
        T,
        manifest_path,
        projection_path,
        policy,
        authority_policy,
        R / "src/pathwaymech/schema/pathwaymech.yaml",
        Path(__file__).resolve(),
    ]
    for module in ["identifiers", "kgx", "schema", "strict"]:
        inputs.append(Path(sys.modules["pathwaymech." + module].__file__).resolve())
    authority_inputs = {}
    for entry in yaml.safe_load(policy.read_text())["namespaces"].values():
        rel = Path(entry["snapshot"])
        assert not rel.is_absolute() and ".." not in rel.parts
        path = (authority_root / rel).resolve(strict=True)
        authority_inputs[str(rel)] = path
        inputs.append(path)
    captured = {str(p): {"sha256": fresh_sha(p), **metadata(p)} for p in inputs}
    manifest = read(manifest_path)
    p = read(projection_path)
    if "target_sha256" in manifest:
        assert manifest["target_sha256"] == sha(T), "Stale manifest target"
    assert p["target_sha256"] == sha(T), "Stale source projection target"
    assert p["graph_to_source"] == yaml.safe_load(T.read_text())["mechanistic_edges"]
    by_name, path_hashes = {}, {}
    for row in manifest["sources"]:
        path = Path(row["path"])
        path = (path if path.is_absolute() else manifest_path.parent / path).resolve(strict=True)
        assert row.get("accepted") is not False
        assert re.fullmatch("[a-f0-9]{64}", row["sha256"])
        assert path_hashes.setdefault(path, row["sha256"]) == row["sha256"]
        by_name.setdefault(path.name, set()).add(path)
    assert len(path_hashes) == len(manifest["sources"]) == 53
    for path, expected in path_hashes.items():
        assert sha(path) == expected, f"Original-body digest mismatch: {path}"
    original_metadata = {str(path): metadata(path) for path in path_hashes}
    for path in [*inputs, *path_hashes]:
        assert path != output and not path.is_relative_to(B), "Output overlaps an input"

    def source_name(name):
        matches = by_name[name]
        assert len(matches) == 1, f"Ambiguous original basename: {name}"
        return next(iter(matches))

    def save(name, value):
        target = B / name
        assert target.parent == B and not target.is_symlink()
        with target.open("x") as stream:
            stream.write(json.dumps(value, indent=2) + "\n")

    B.mkdir(parents=True, exist_ok=False)

    def replay_originals():
        RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        RH = "http://rdf.rhea-db.org/"
        raw = gzip.decompress(source_name("rhea.rdf.gz").read_bytes()).decode()
        blocks = {}
        for m in re.finditer(
            r'<rdf:Description rdf:about="([^"]+)"[^>]*>(.*?)</rdf:Description>', raw, re.S
        ):
            blocks.setdefault(m[1], []).append(m[0])

        def prop(uri):
            out = collections.defaultdict(list)
            for b in blocks[uri]:
                x = ET.fromstring(
                    (
                        '<x xmlns:rdf="'
                        + RDF
                        + '" xmlns:rh="'
                        + RH
                        + '" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">'
                        + b
                        + "</x>"
                    ).encode()
                )[0]
                for c in x:
                    k = ET.QName(c).localname
                    v = c.get("{" + RDF + "}resource") or c.text
                    if v not in out[k]:
                        out[k].append(v)
            return dict(out)

        con = sqlite3.connect("file:" + str(source_name("chebi.db")) + "?mode=ro", uri=True)

        def chem(cid):
            return dict(
                con.execute(
                    "select predicate,value from statements where subject=? and value is not null",
                    (cid,),
                )
            )

        def side(uri):
            p = prop(uri)
            out = []
            for k, vs in p.items():
                if re.fullmatch("contains[0-9]+", k):
                    for v in vs:
                        cu = prop(v)["compound"][0]
                        cp = prop(cu)
                        cid = "CHEBI:" + re.search(r"CHEBI[_:](\d+)", cp["chebi"][0])[1]
                        c = chem(cid)
                        out.append(
                            dict(
                                id=cid,
                                coefficient=int(k[8:]),
                                label=c["rdfs:label"],
                                formula=c["chemrof:generalized_empirical_formula"],
                                charge=int(c["chemrof:charge"]),
                                inchi=c["chemrof:inchi_string"],
                                side_uri=uri,
                                participant_uri=v,
                                compound_uri=cu,
                            )
                        )
            return out

        rows = []
        net = collections.Counter()
        for master in [11584, 59136, 59140]:
            r = prop(RH + str(master + 1))
            s = {role: side(r[role][0]) for role in ["substrates", "products"]}
            res = collections.Counter()
            for role, sign in [("substrates", -1), ("products", 1)]:
                for t in s[role]:
                    n = sign * t["coefficient"]
                    net[t["id"]] += n
                    toks = re.findall(r"([A-Z][a-z]?)(\d*)", t["formula"])
                    assert "".join(a + b for a, b in toks) == t["formula"]
                    for a, b in toks:
                        res[a] += n * int(b or 1)
                    res["charge"] += n * t["charge"]
            assert not {k: v for k, v in res.items() if v}
            rows.append(
                dict(
                    master=master,
                    directional=master + 1,
                    direction="left_to_right",
                    sides=s,
                    balance_residual={},
                    master_metadata=prop(RH + str(master)),
                )
            )
        bridges = []
        for native, cid in [
            ("L-ORNITHINE", "CHEBI:46911"),
            ("CPD-217", "CHEBI:57668"),
            ("CPD-21047", "CHEBI:142972"),
            ("CPD-12589", "CHEBI:142973"),
        ]:
            p = source_name(native + ".xml")
            x = ET.parse(str(p)).find("./Compound")
            c = chem(cid)
            bridges.append(
                dict(
                    native_id=native,
                    chebi_id=cid,
                    native_inchi=x.findtext("inchi"),
                    current_inchi=c.get("chemrof:inchi_string"),
                    exact_equal=x.findtext("inchi") == c.get("chemrof:inchi_string"),
                    native_path=str(p),
                    native_sha256=sha(p),
                )
            )
        # Preserve the exact structure-search result; no whole-ontology absence claim.
        terms = {cid: chem(cid) for cid in ["CHEBI:142972", "CHEBI:142973", "CHEBI:84711"]}
        go = sqlite3.connect("file:" + str(source_name("go.db")) + "?mode=ro", uri=True)
        gohits = list(
            go.execute(
                "select subject,predicate,value from statements "
                "where lower(value) like '%staphyloferrin%'"
            )
        )
        o = dict(
            started_at=started,
            finished_at=datetime.now(UTC).isoformat(),
            status="passed",
            scope=(
                "Three complete native transformations and current reaction-class atom/charge "
                "accounting; not a curated record or exact protein catalytic proof"
            ),
            originals=[
                dict(path=str(p), sha256=sha(p))
                for p in [
                    source_name(n)
                    for n in ["rhea.rdf.gz", "rhea-directions.tsv", "chebi.db", "go.db"]
                ]
            ],
            reactions=rows,
            route_net={k: v for k, v in net.items() if v},
            native_current_bridges=bridges,
            selected_chemical_authority=terms,
            go_label_synonym_definition_search=gohits,
        )
        con.close()
        go.close()
        return o

    raw = yaml.safe_load(T.read_text())
    record = validate_record(raw)
    assert not strict_errors([T], R)
    chem = replay_originals()
    save("chemistry.json", chem)
    assert len(chem["reactions"]) == 3
    assert all(not r["balance_residual"] for r in chem["reactions"])
    assert [b["exact_equal"] for b in chem["native_current_bridges"]] == [True, True, False, False]
    assert chem["route_net"] == p["net"]
    assert chem["route_net"] == {
        "CHEBI:46911": -1,
        "CHEBI:16947": -2,
        "CHEBI:30616": -2,
        "CHEBI:456215": 2,
        "CHEBI:33019": 2,
        "CHEBI:15378": 2,
        "CHEBI:142973": 1,
    }
    native = ET.parse(str(source_name("PWY-7990.xml"))).find("Pathway")
    members = native.xpath("reaction-list/Reaction/@frameid")
    assert set(members) == {"ORNITHINE-RACEMASE-RXN", "RXN-19522", "RXN-19521"}
    assert {r["native"] for r in p["source_to_graph"]} == set(members)
    assert {r["reaction"] for r in p["source_to_graph"]} == {r["id"] for r in raw["reactions"]}
    assert "R00672" in (source_name("M00876.txt")).read_text()
    assert all(x in (source_name("M00876.txt")).read_text() for x in ["R12353", "R12354"])
    for row in p["source_to_graph"]:
        x = ET.parse(str(source_name(row["native"] + ".xml"))).find("Reaction")
        assert x.findtext("reaction-direction") == row["native_direction"]
        sides = {
            s: [
                {"id": t[0].get("frameid"), "coefficient": int(t.findtext("coefficient") or 1)}
                for t in x.findall(s)
            ]
            for s in ["left", "right"]
        }
        assert sides == row["native_sides"]
        layout = native.xpath(
            "reaction-layout[Reaction/@frameid=$n]/direction/text()", n=row["native"]
        )
        assert layout == ["L2R"]
    reactions = {f"RHEA:{r['directional']}": r for r in chem["reactions"]}
    assert len(p["chemical_sides"]) == 16
    for side in p["chemical_sides"]:
        expected = next(
            x
            for x in reactions[side["reaction"]]["sides"][side["role"]]
            if x["participant_uri"] == side["participant_uri"]
        )
        assert {k: side[k] for k in expected} == expected
        e = next(e for e in raw["mechanistic_edges"] if e["id"] == side["edge_id"])
        sub, obj = (
            (side["id"], side["reaction"])
            if side["role"] == "substrates"
            else (side["reaction"], side["id"])
        )
        assert (e["subject"], e["object"]) == (sub, obj)
        assert f"rh:contains{side['coefficient']}" in e["evidence"][0]["source_locator"]
    # Read exact protein identity and comparison anew from original bodies.
    proteins = {
        x.findtext("GBSeq_accession-version"): x
        for x in ET.parse(str(source_name("Newman-proteins.xml"))).getroot()
    }
    comp = []
    for ac, up, locus in [
        ("BAF68351.1", "Q2FW73", "NWMN_2079"),
        ("BAF68352.1", "Q2FW72", "NWMN_2080"),
        ("BAF68354.1", "Q2FW70", "NWMN_2082"),
    ]:
        x = proteins[ac]
        quals = [
            (q.findtext("GBQualifier_name"), q.findtext("GBQualifier_value"))
            for q in x.findall(".//GBQualifier")
        ]
        assert ("locus_tag", locus) in quals
        assert ("strain", "Newman") in quals
        assert ("db_xref", "taxon:426430") in quals
        path = source_name(up + ".json")
        u = read(path)
        assert u["organism"]["taxonId"] == 93061
        ns = x.findtext("GBSeq_sequence").upper()
        us = u["sequence"]["value"]
        assert len(ns) == len(us)
        differences = [i + 1 for i, (a, b) in enumerate(zip(ns, us, strict=True)) if a != b]
        assert differences == ([532] if up == "Q2FW70" else [])
        comp.append(
            {
                "accession": ac,
                "locus": locus,
                "up": up,
                "length": len(ns),
                "newman_sequence_sha256": hashlib.sha256(ns.encode()).hexdigest(),
                "up_sequence_sha256": hashlib.sha256(us.encode()).hexdigest(),
                "different_positions": differences,
                "exact_sequence_equal": not differences,
            }
        )
    u = read(source_name("Q2FW73.json"))
    assert u["entryType"] == "UniProtKB unreviewed (TrEMBL)"
    assert u["comments"][0]["cofactors"][0]["evidences"][0]["evidenceCode"] == "ECO:0000256"
    assert u["comments"][0]["cofactors"][0]["cofactorCrossReference"]["id"] == "CHEBI:597326"
    for obj, rxn in [("ENZRXN-26283", "RXN-19521"), ("ENZRXN-26284", "RXN-19522")]:
        x = ET.parse(str(source_name(obj + ".xml"))).find("Enzymatic-Reaction")
        assert x.find("reaction/Reaction").get("frameid") == rxn
        assert x.find("cofactor/Compound").get("frameid") == "MG+2"
    sfac = ET.parse(str(source_name("MONOMER-20490.xml"))).find("Protein")
    assert "assumed" in sfac.findtext("comment") and "not been purified" in sfac.findtext("comment")
    # Literal selected source paragraphs establish identity and limits, without copying methods.
    h = html.parse(str(source_name("PMC2856993.html")))
    checks = []
    for sel, fragments in [
        ('//*[@id="sec5"]/p[2]', ["S. aureus Newman genomic DNA", "Recombinant SfaB and SfaD"]),
        ('//*[@id="sec7"]/p', ["Using recombinant SfaB and SfaD"]),
        (
            '//*[@id="sec18"]/p[2]',
            ["R-configuration", "S configuration", "R configuration", "does not fit"],
        ),
    ]:
        text = norm(" ".join(" ".join(x.itertext()) for x in h.xpath(sel)))
        assert all(fragment in text for fragment in fragments), (sel, text)
        checks.append(
            {
                "selector": sel,
                "selected_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
                "selected_characters": len(text),
            }
        )
    assert (
        next(r for r in raw["references"] if r["id"] == "PMID:20147287")["title"]
        == h.xpath('//meta[@name="citation_title"]/@content')[0]
    )
    assert all(len(r["title"]) < 400 for r in raw["references"])
    ct = read(source_name("PMID19138128.json"))["resultList"]["result"][0]
    assert (
        "SfnaD using the delta-amine" in ct["abstractText"]
        and "SfnaB utilizing the alpha-amine" in ct["abstractText"]
    )
    # Original-body integrity and honest web-only provenance.
    ref_checks = []
    for ref in raw["references"]:
        if ref["id"] == "PMID:19400778":
            assert "source_sha256" not in ref and "no local full-body hash" in ref["source_version"]
            continue
        path = p["reference_original_paths"][ref["id"]]
        assert Path(path).resolve() in path_hashes, "Reference body outside explicit manifest"
        assert path_hashes[Path(path).resolve()] == ref["source_sha256"]
        assert sha(path) == ref["source_sha256"], ref["id"]
        ref_checks.append({"id": ref["id"], "path": path, "sha256": ref["source_sha256"]})

    # Negative guards target actual scientific/provenance failure modes.
    def guard(doc):
        assert {r["id"] for r in doc["reactions"]} == {"RHEA:11585", "RHEA:59137", "RHEA:59141"}
        assert not doc.get("source_mappings"), "No exact native/current stereochemical equivalence"
        assert not any(n.get("category") == "complex" for n in doc["participants"])
        for e in doc["mechanistic_edges"]:
            if e["subject"] == "NCBIProtein:BAF68351.1" and e["object"] == "RHEA:11585":
                assert e["predicate"] == "enables"
                assert "inferred" in e["description"].lower()
            if e["predicate"] == "has_cofactor":
                assert (
                    "inference" in e["description"].lower()
                    or "qualified native" in e["description"].lower()
                )
        assert "stereospecific" in doc["description"] or "specifies" in doc["description"]
        assert "residue 532" in doc["description"]

    guard(raw)
    negative = []
    for kind in [
        "truncate_racemization",
        "sfac_direct_catalysis",
        "false_stereo_exact_match",
        "invent_assembly",
    ]:
        bad = copy.deepcopy(raw)
        if kind == "truncate_racemization":
            bad["reactions"] = bad["reactions"][1:]
        elif kind == "sfac_direct_catalysis":
            next(
                e
                for e in bad["mechanistic_edges"]
                if e["subject"] == "NCBIProtein:BAF68351.1" and e["object"] == "RHEA:11585"
            )["predicate"] = "catalyzes"
        elif kind == "false_stereo_exact_match":
            bad["source_mappings"] = [
                {
                    "subject": "MetaCyc:CPD-12589",
                    "object": "CHEBI:142973",
                    "predicate": "skos:exactMatch",
                }
            ]
        else:
            bad["participants"].append(
                {"id": "MetaCyc:invented", "label": "invented", "category": "complex"}
            )
        try:
            guard(bad)
        except AssertionError:
            negative.append(kind)
        else:
            raise AssertionError("Invalid mutation accepted: " + kind)
    # The fresh identifier gate binds the final exact draft.
    # Canonical authority source bodies stay unchanged.
    sandbox = B / "authority-sandbox"
    (sandbox / "data/pathways").mkdir(parents=True)
    (sandbox / "conf").mkdir()
    shutil.copyfile(T, sandbox / "data/pathways" / T.name)
    shutil.copyfile(policy, sandbox / "conf/identifier_policy.yaml")
    for rel, original in authority_inputs.items():
        destination = sandbox / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, destination)
    identifier_findings = identifier_errors(sandbox)
    assert not identifier_findings, identifier_findings
    assert fresh_sha(sandbox / "data/pathways" / T.name) == sha(T)
    nodes_file, edges_file = write_kgx([record], B / "kgx")
    nodes = list(csv.DictReader(nodes_file.open(), delimiter="\t"))
    exported = list(csv.DictReader(edges_file.open(), delimiter="\t"))
    assert len(nodes) == 19 and len(exported) == 31
    refs = {r["id"]: r for r in raw["references"]}
    for edge, out in zip(raw["mechanistic_edges"], exported, strict=True):
        assert (out["subject"], out["predicate"], out["object"]) == (
            edge["subject"],
            LOCAL_PREDICATE_CURIES[edge["predicate"]],
            edge["object"],
        )
        assert json.loads(out["evidence"]) == edge["evidence"]
        assert out["description"] == edge.get("description", "")
        assert json.loads(out["reference_metadata"]) == [
            refs[i] for i in sorted({e["reference_id"] for e in edge["evidence"]})
        ]
    assert sum(len(e["evidence"]) for e in raw["mechanistic_edges"]) == 59
    # Recompute source-native stereochemistry from issued InChIs using RDKit.
    stereo_script = (
        "from rdkit import Chem, rdBase\nimport json, sys\nfrom pathlib"
        " import Path\nd = json.loads(Path(sys.argv[1]).read_text())\nr"
        "ows = []\nfor row in d['native_current_bridges']:\n    if row["
        "'native_id'] not in ['CPD-21047', 'CPD-12589']:\n        cont"
        "inue\n    for source, key in [('native', 'native_inchi'), ('c"
        "urrent', 'current_inchi')]:\n        m = Chem.MolFromInchi(ro"
        "w[key])\n        assert m\n        Chem.AssignStereochemistry("
        "m, cleanIt=True, force=True)\n        centers = Chem.FindMolC"
        "hiralCenters(m, includeUnassigned=True)\n        orn = [idx f"
        "or idx, cip in centers if any((n.GetSymbol() == 'N' for n in"
        " m.GetAtomWithIdx(idx).GetNeighbors()))]\n        assert len("
        "orn) == 1\n        ci = []\n        for idx, cip in centers:\n "
        "           if idx != orn[0]:\n                ci.append(dict("
        "cip=cip, distance_to_ornithine_alpha=len(Chem.GetShortestPat"
        "h(m, idx, orn[0])) - 1))\n        ci.sort(key=lambda x: x['di"
        "stance_to_ornithine_alpha'])\n        if len(ci) == 2:\n      "
        "      ci[0]['role'] = 'N2-citryl'\n            ci[1]['role'] "
        "= 'N5-citryl'\n            assert ci[0]['distance_to_ornithin"
        "e_alpha'] < ci[1]['distance_to_ornithine_alpha']\n        els"
        "e:\n            ci[0]['role'] = 'N5-citryl'\n        rows.appe"
        "nd(dict(native_id=row['native_id'], source=source, id=row['c"
        "hebi_id'] if source == 'current' else row['native_id'], orni"
        "thine_alpha=dict(centers)[orn[0]], citryl_centers=ci))\nasser"
        "t [x['cip'] for x in rows[-1]['citryl_centers']] == ['R', 'S"
        "']\nassert rows[1]['citryl_centers'][0]['cip'] == 'S'\nassert "
        "rows[0]['citryl_centers'][0]['cip'] == '?'\no = dict(status='"
        "passed', rdkit_version=rdBase.rdkitVersion, rows=rows, prima"
        "ry_figure='PMC2856993 Figure 2A, independently viewed: N2 ci"
        "trate R; ornithine alpha R; N5 citrate S.', scope='Role-awar"
        "e structure interpretation of retained issued InChIs, not fr"
        "esh experimental stereochemistry. The primary ligand was fer"
        "ric receptor-bound material; free product ionization is from"
        " the chemical authority.')\nwith Path(sys.argv[2]).open('x') "
        "as stream:\n    stream.write(json.dumps(o, indent=2) + '\\n')\n"
    )
    run = subprocess.run(
        [
            str(stereo_python),
            "-B",
            "-c",
            stereo_script,
            str(B / "chemistry.json"),
            str(B / "stereochemistry.json"),
        ],
        cwd=B,
        capture_output=True,
        text=True,
        check=False,
    )
    save(
        "stereochemistry-console.json",
        {
            "command_interpreter": str(stereo_python),
            "exit_code": run.returncode,
            "stdout": run.stdout,
            "stderr": run.stderr,
            "script_sha256": hashlib.sha256(stereo_script.encode()).hexdigest(),
        },
    )
    assert run.returncode == 0, run.stderr
    stereo = read(B / "stereochemistry.json")

    assert [x["cip"] for x in stereo["rows"][-1]["citryl_centers"]] == ["R", "S"]
    assert stereo["rows"][1]["citryl_centers"][0]["cip"] == "S"
    assert stereo["rows"][0]["citryl_centers"][0]["cip"] == "?"
    result = {
        "started_at": started,
        "finished_at": datetime.now(UTC).isoformat(),
        "status": "passed_portable_replay_not_independent_approval",
        "target_sha256": sha(T),
        "counts": {
            "native_members": 3,
            "reactions": 3,
            "chemical_sides": 16,
            "balanced_reactions": 3,
            "participants": 14,
            "taxa": 1,
            "nodes": len(nodes),
            "edges": 31,
            "evidence": 59,
            "references": 28,
            "hashed_references": len(ref_checks),
            "web_only_references": 1,
        },
        "reference_hash_checks": ref_checks,
        "source_body_count": len(manifest["sources"]),
        "protein_comparisons": comp,
        "primary_locator_checks": checks,
        "native_stereo_bridges": [b["exact_equal"] for b in chem["native_current_bridges"]],
        "net": chem["route_net"],
        "negative_guards_rejected": negative,
        "actual_kgx": {
            "nodes_path": str(nodes_file),
            "nodes_sha256": sha(nodes_file),
            "edges_path": str(edges_file),
            "edges_sha256": sha(edges_file),
            "full_evidence_and_reference_metadata_preserved": True,
        },
        "checks": [
            "native and closed schema",
            "actual original RDF and ChEBI side/direction/balance replay",
            "three full native object boundaries and ordering",
            "exact Newman issuing protein identities and NCTC 8325 sequence differences",
            "selected original primary paragraph and title guards",
            "source-body hashes",
            "canonical unchanged identifier gate in external sandbox",
            "actual target KGX edge/evidence/reference equality",
        ],
        "limits": [
            "No shared authority integration or full corpus gates",
            "No independent scientific approval",
            "Cotton full text unavailable; individual SfaC activity remains inferred",
            "Beasley original text inspected through web only, no local body hash",
            "Bound product stereochemistry does not directly assay free intermediate or ionization",
            "Cofactor transfer remains explicitly qualified inference",
        ],
    }
    result["input_checks"] = captured
    result["original_body_checks"] = [
        {"path": str(path), "sha256": sha256} for path, sha256 in path_hashes.items()
    ]
    result["authority_input_scope"] = {
        "root": str(authority_root),
        "snapshots": {rel: str(path) for rel, path in authority_inputs.items()},
        "scope": "One-record check only; no integrated corpus approval",
    }
    result["repository"] = {
        "path": str(R),
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=R, text=True).strip(),
    }
    result["helper_sha256"] = fresh_sha(__file__)
    result["stereochemistry"] = {
        "fresh_original_inchi_computation": True,
        "rdkit_version": stereo["rdkit_version"],
        "receipt_sha256": fresh_sha(B / "stereochemistry.json"),
    }
    for path, captured_row in captured.items():
        assert metadata(path) == {k: captured_row[k] for k in ["bytes", "mode", "mtime_ns"]}
        assert fresh_sha(path) == captured_row["sha256"], f"Input changed during replay: {path}"
    for path, expected in original_metadata.items():
        assert metadata(path) == expected, f"Original metadata changed during replay: {path}"
    result["input_bytes_and_metadata_preserved"] = True
    with output.open("x") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "status": result["status"],
                "counts": result["counts"],
                "target_sha256": result["target_sha256"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main(parse_args())
