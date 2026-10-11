"""Source-bound author replay of the full pyochelin draft; not independent approval."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import re
import sqlite3
import subprocess
from collections import Counter
from datetime import UTC, datetime
from functools import cache
from itertools import product
from pathlib import Path

if not __debug__:
    raise RuntimeError("optimized Python disables required source guards")
p = argparse.ArgumentParser(description=__doc__)
for n in [
    "repo-root",
    "record",
    "source-manifest",
    "source-projection",
    "authority-root",
    "reactive-helper",
    "rdkit-python",
    "output",
]:
    p.add_argument("--" + n, required=True, type=Path)
a = p.parse_args()
R = a.repo_root.resolve()
T = a.record.resolve()
M = a.source_manifest.resolve()
P = a.source_projection.resolve()
A = a.authority_root.resolve()
OUT = a.output.absolute()

started_at = datetime.now(UTC).isoformat()
work = OUT.with_suffix(".artifacts")
if OUT.exists() or work.exists():
    raise FileExistsError(OUT if OUT.exists() else work)

# Capture formal inputs before importing repository validators or invoking probes.
# A receipt must attest the bytes actually parsed, never replacement file bytes.
input_bindings = {}
captured_bytes = {}


def absolute(path):
    return Path(path).absolute()


def uncached_sha(path):
    with Path(path).open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def capture(path, scope, *, keep_bytes=False, expected=None):
    path = absolute(path)
    key = str(path)
    if key in input_bindings:
        binding = input_bindings[key]
        if expected is not None and binding["sha256"] != expected:
            raise ValueError("conflicting expected input digest: " + key)
        return binding
    if not path.is_file():
        raise ValueError("required input is not a file: " + key)
    resolved = str(path.resolve(strict=True))
    if keep_bytes:
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        captured_bytes[key] = data
    else:
        digest = uncached_sha(path)
    if str(path.resolve(strict=True)) != resolved:
        raise ValueError("input symlink changed during capture: " + key)
    if expected is not None and digest != expected:
        raise ValueError("source digest mismatch: " + key)
    binding = dict(path=key, resolved_path=resolved, sha256=digest, scope=scope)
    input_bindings[key] = binding
    return binding


def captured(path):
    return captured_bytes[str(absolute(path))]


def sha(path):
    key = str(absolute(path))
    if key in input_bindings:
        return input_bindings[key]["sha256"]
    return uncached_sha(path)


def read(path):
    key = str(absolute(path))
    if key in captured_bytes:
        return json.loads(captured_bytes[key])
    return json.loads(Path(path).read_text())


formal = [
    T,
    M,
    P,
    absolute(__file__),
    a.reactive_helper.absolute(),
    R / "conf/identifier_policy.yaml",
    A / "conf/identifier_policy.yaml",
    A / "data/pathways" / T.name,
]
authority_files = sorted((A / "data/identifier_authorities").rglob("*.json"))
if not authority_files:
    raise ValueError("authority snapshot directory has no JSON inputs")
runtime_files = sorted((R / "src/pathwaymech").rglob("*.py"))
runtime_files += sorted((R / "src/pathwaymech/schema").rglob("*.yaml"))
formal += authority_files + runtime_files
for path in formal:
    capture(path, "formal_or_runtime", keep_bytes=True)
if OUT.resolve() in {Path(b["resolved_path"]) for b in input_bindings.values()}:
    raise ValueError("output collides with an input")
manifest = json.loads(captured(M))
proj = json.loads(captured(P))
assert sha(T) == manifest["target_sha256"] == proj["target_sha256"]

# Original bodies are bound to the captured manifest's pre-existing digests.
# They are streamed rather than held in memory; every body is rehashed at completion.
for row in manifest["sources"]:
    capture(row["path"], "original_source", expected=row["sha256"])
for path in manifest["reference_paths"].values():
    if str(absolute(path)) not in input_bindings:
        raise ValueError("reference body is absent from source manifest: " + str(path))


def verify_bindings(stage, *, formal_only=False):
    for binding in input_bindings.values():
        if formal_only and binding["scope"] == "original_source":
            continue
        path = Path(binding["path"])
        if (
            str(path.resolve(strict=True)) != binding["resolved_path"]
            or uncached_sha(path) != binding["sha256"]
        ):
            raise ValueError("input changed after capture (" + stage + "): " + str(path))
    current_authorities = sorted((A / "data/identifier_authorities").rglob("*.json"))
    current_runtime = sorted((R / "src/pathwaymech").rglob("*.py"))
    current_runtime += sorted((R / "src/pathwaymech/schema").rglob("*.yaml"))
    if current_authorities != authority_files or current_runtime != runtime_files:
        raise ValueError("input file inventory changed after capture: " + stage)


work.mkdir(parents=True, exist_ok=False)

import yaml  # noqa: E402
from lxml import etree as E  # noqa: E402

from pathwaymech.identifiers import identifier_errors  # noqa: E402
from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx  # noqa: E402
from pathwaymech.schema import validate_record  # noqa: E402
from pathwaymech.strict import strict_errors  # noqa: E402

verify_bindings("after_repository_import", formal_only=True)
raw = yaml.safe_load(captured(T))
for policy in [R / "conf/identifier_policy.yaml", A / "conf/identifier_policy.yaml"]:
    policy_data = yaml.safe_load(captured(policy))
    for row in policy_data["namespaces"].values():
        path = A / row["snapshot"]
        if str(absolute(path)) not in input_bindings:
            raise ValueError("policy names an uncaptured authority snapshot: " + str(path))
refs = {r["id"]: r for r in raw["references"]}
for ident, path in manifest["reference_paths"].items():
    assert sha(path) == refs[ident]["source_sha256"], ident
assert sha(R / "conf/identifier_policy.yaml") == sha(A / "conf/identifier_policy.yaml")
assert yaml.safe_load((A / "data/pathways" / T.name).read_text()) == raw
rec = validate_record(raw)
assert not strict_errors([T], R)
errs = identifier_errors(A)
assert not errs, errs
originals = Path(manifest["roles"]["native_originals"])
pw = next(
    n
    for n in E.parse(manifest["roles"]["native_pathway"]).getroot()
    if n.get("frameid") == "PWY-6408"
)


@cache
def native(f):
    return next(
        n for n in E.parse(str(originals / (f + ".xml"))).getroot() if n.get("frameid") == f
    )


members = {n.get("frameid") for n in pw.findall(".//reaction-list/Reaction")}
assert len(members) == 11, members
small = {
    "AMP": "CHEBI:456215",
    "ATP": "CHEBI:30616",
    "CPD-110": "CHEBI:30762",
    "CPD-12084": "CHEBI:86458",
    "CPD-12085": "CHEBI:144924",
    "CYS": "CHEBI:35235",
    "NADP": "CHEBI:58349",
    "NADPH": "CHEBI:57783",
    "PPI": "CHEBI:33019",
    "PROTON": "CHEBI:15378",
    "WATER": "CHEBI:15377",
    "S-ADENOSYLMETHIONINE": "CHEBI:59789",
    "ADENOSYL-HOMO-CYS": "CHEBI:57856",
}
roles = {
    "RXN-11113": ["Q9HWG3"],
    "RXN-11115": ["G3XCV2", "Q9HWG4"],
    "RXN-11125": ["G3XCV2"],
    "RXN-19466": ["Q9HWG3"],
    "RXN-19469": ["G3XCV2"],
    "RXN-11118": ["G3XCV2"],
    "RXN-11117": ["Q9HWG4"],
    "RXN-11120": ["Q9HWG4"],
    "RXN-11121": ["Q9HWG5"],
    "RXN-11122": ["Q9HWG4"],
    "RXN-11123": ["Q9HWG4"],
}
up = read(manifest["roles"]["pao1_uniprot"])
ups = {x["primaryAccession"]: x for x in up["results"]}
source_sides = {}
for f in sorted(members):
    n = native(f)
    assert n.findtext("reaction-direction") in [
        "LEFT-TO-RIGHT",
        "PHYSIOL-LEFT-TO-RIGHT",
    ]
    source_sides[f] = {
        side: Counter(
            {
                next(c for c in x if c.get("frameid")).get("frameid"): int(
                    x.findtext("coefficient") or 1
                )
                for x in n.findall(side)
            }
        )
        for side in ["left", "right"]
    }


def science(d):
    assert {n["id"] for n in d["reactions"]} == {"MetaCyc:" + f for f in members}
    assert all(n["direction"] == "left_to_right" for n in d["reactions"])
    ed = d["mechanistic_edges"]
    nodes = {n["id"]: n for n in d["participants"]}
    assert all(n.get("category") != "complex" for n in d["participants"])
    assert {n["id"] for n in d["taxa"]} == {"NCBITaxon:208964"}
    assert (
        "interconverting I/II" in d["description"]
        and "does not assert exclusive I production" in d["description"]
    )
    assert (
        "MetaCyc:CPD-9992" in nodes
        and not {"CHEBI:67183", "CHEBI:67185", "CHEBI:29669"} & nodes.keys()
    )
    endpoint = next(e for e in ed if e["id"] == "pch-edge-037")
    endpoint_sources = {v["reference_id"]: v for v in endpoint["evidence"]}
    native_endpoint = endpoint_sources["MetaCyc:CPD-9992"]
    assert "/p-1" in native_endpoint["source_assertion"]
    assert "physiological I/II mixture" not in native_endpoint["source_assertion"]
    assert "projects one member" not in native_endpoint["source_assertion"]
    structural_endpoint = endpoint_sources["CHEBI:67183"]
    assert "protonation-normalized" in structural_endpoint["source_assertion"]
    assert "not exact charge equivalence" in structural_endpoint["source_assertion"]
    assert "/default_structure/standard_inchi" in structural_endpoint["source_locator"]
    assert "I and II" in endpoint_sources["PMID:17938167"]["source_assertion"]
    for edge_id in ["pch-edge-062", "pch-edge-063"]:
        role = next(e for e in ed if e["id"] == edge_id)
        identity = role["evidence"][0]
        assert identity["reference_id"] == "UniProtKB:Q9HWG4"
        assert "identity evidence does not independently assign" in identity["source_assertion"]
        assert "/results/2/comments/0" not in identity["source_locator"]
        assert "/results/2/genes/0/geneName/value" in identity["source_locator"]
        if edge_id == "pch-edge-063":
            primary = role["evidence"][1]
            assert primary["reference_id"] == "PMID:30525512"
            assert "native I structure" not in primary["source_assertion"]
            assert "formal projection" not in primary["source_assertion"]
    for f, ss in source_sides.items():
        rid = "MetaCyc:" + f
        for side, pred in [("left", "consumes"), ("right", "produces")]:
            selected = Counter(
                small.get(i, "MetaCyc:" + i) for i, c in ss[side].items() for _ in range(c)
            )
            actual = Counter(
                e["subject"] if side == "left" else e["object"]
                for e in ed
                if e["predicate"] == pred
                and (e["object"] if side == "left" else e["subject"]) == rid
            )
            assert actual == selected, (f, side, actual, selected)
        actualroles = {
            e["subject"] for e in ed if e["object"] == rid and e["predicate"] == "enables"
        }
        assert actualroles == {"UniProtKB:" + x for x in roles[f]}, (f, actualroles)
        assert (
            sum(
                e["subject"] == rid and e["predicate"] == "part_of" and e["object"] == d["id"]
                for e in ed
            )
            == 1
        )
    for e in ed:
        for v in e["evidence"]:
            assert len(v["source_assertion"]) <= 400 and v["source_locator"]
            if v["reference_id"].startswith("UniProtKB:"):
                assert not re.search(
                    r"(?:^|;\s*)/(?:sequence|comments|organism|proteinDescription)",
                    v["source_locator"],
                ), v
                ix = int(re.search(r"/results/(\d+)/", v["source_locator"])[1])
                assert up["results"][ix]["primaryAccession"] == v["reference_id"].split(":")[1]
                # Every full JSON pointer selected in the locator must actually resolve.
                for pointer in re.findall(
                    r"/results/\d+(?:/[A-Za-z_]+|/\d+)+", v["source_locator"]
                ):
                    obj = up
                    for key in pointer[1:].split("/"):
                        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
            if v["reference_id"] == "PMID:35105906":
                for loc in re.findall(
                    r'article/body//sec\[@id="[^"]+"\](?:/p\[1\])?', v["source_locator"]
                ):
                    assert E.parse(str(originals / "PMC8807600.xml")).xpath("/" + loc), loc
            if v["reference_id"] in ["PMID:30525512", "PMID:27601130"]:
                fn = {
                    "PMID:30525512": "PMC6372355-bioc.xml",
                    "PMID:27601130": "PMC5046821-bioc.xml",
                }[v["reference_id"]]
                tree = E.parse(str(originals / fn))
                for offset in re.findall(r'offset="(\d+)"', v["source_locator"]):
                    assert tree.xpath('//passage[offset="' + offset + '"]'), offset
            if (
                v["reference_id"].startswith("MetaCyc:")
                and v["reference_id"].split(":", 1)[1] in source_sides
            ):
                # All scoped native side/membership claims retain their actual source frame.
                assert v["reference_id"].split(":", 1)[1] in v["source_locator"]
    assert not any(e["predicate"] == "catalyzes" for e in ed)
    assert not any(e["subject"] == "UniProtKB:Q56950" for e in ed)
    return True


science(raw)
endpoint_json = read(manifest["reference_paths"]["CHEBI:67183"])
assert endpoint_json["chebi_accession"] == "CHEBI:67183"
assert endpoint_json["name"] == "pyochelin I"
assert endpoint_json["chemical_data"]["charge"] == 0
native_endpoint_inchi = native("CPD-9992").findtext("inchi")
assert "/p-1" in native_endpoint_inchi
assert (
    native_endpoint_inchi.replace("/p-1", "")
    == endpoint_json["default_structure"]["standard_inchi"]
)
assert proj["graph_to_source"] == raw["mechanistic_edges"]
assert {r["id"] for r in proj["source_to_graph"]} == members
assert len(proj["chemical_sides"]) == sum(
    len(s) for ss in source_sides.values() for s in ss.values()
)
# Structure/protomer crosswalk requires both native InChI and explicit charged atoms.
con = sqlite3.connect("file:" + manifest["roles"]["chebi"] + "?mode=ro", uri=True)
for f, cid in small.items():
    facts = dict(
        con.execute(
            "select predicate,value from statements where subject=? and value is not null",
            (cid,),
        )
    )
    assert native(f).findtext("inchi") == facts["chemrof:inchi_string"]
    if f in ["CYS", "S-ADENOSYLMETHIONINE", "ADENOSYL-HOMO-CYS"]:
        charges = {
            (x.get("elementType"), x.get("formalCharge")) for x in native(f).findall(".//atom")
        }
        assert ("N", "1") in charges and ("O", "-1") in charges
        assert "zwitterion" in facts["rdfs:label"]
# Original article titles, not bibliography or abbreviations headings.
for pm, fn in [
    ("30525512", "PMC6372355-bioc.xml"),
    ("27601130", "PMC5046821-bioc.xml"),
]:
    t = E.parse(str(originals / fn))
    n = t.xpath('//passage[infon[@key="section_type"]="TITLE"]/text')
    assert len(n) == 1
    assert refs["PMID:" + pm]["title"] == " ".join(n[0].text.split())
# Translate exact PA14 source submissions and quantify, rather than erase, strain differences.
code = {
    "".join(c): aa
    for c, aa in zip(
        product("TCAG", repeat=3),
        "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
        strict=True,
    )
}
seqchecks = []
for af, old, new, nchanges in [
    ("AF184620", "Q9RFM9", "Q9HWG3", 3),
    ("AF184621", "Q9RFM8", "G3XCV2", 14),
    ("AF184622", "Q9RFM7", "Q9HWG4", 19),
]:
    text = (originals / (af + ".embl")).read_text()
    assert '/strain="PA14"' in text
    dna = "".join(re.findall("[acgt]+", text.split("\nSQ   ")[1].split("\n", 1)[1])).upper()
    tr = "".join(code[dna[i : i + 3]] for i in range(0, len(dna), 3))
    assert tr[-1] == "*"
    tr = tr[:-1]
    ft = "\n".join(line[5:] for line in text.splitlines() if line.startswith("FT   "))
    given = "".join(re.search('/translation="(.*?)"', ft, re.S)[1].split())
    assert tr == given == read(originals / ("uniprot-" + old + ".json"))["sequence"]["value"]
    dif = sum(a != b for a, b in zip(tr, ups[new]["sequence"]["value"], strict=True))
    assert dif == nchanges
    seqchecks.append(dict(source=af, old_accession=old, current=new, substitutions=dif))
text = (originals / "AF074705.embl").read_text()
assert '/strain="PAO1"' in text
seq = "".join(re.findall("[acgt]+", text.split("\nSQ   ")[1].split("\n", 1)[1])).upper()
for block in text.split("FT   CDS             ")[1:]:
    g = re.search('/gene="(.*?)"', block)[1]
    if g not in ["pchE", "pchF", "pchG"]:
        continue
    start, end = map(int, re.match(r"(\d+)\.\.(\d+)", block).groups())
    dna = seq[start - 1 : end]
    tr = "".join(code[dna[i : i + 3]] for i in range(0, len(dna), 3))
    assert tr[-1] == "*"
    tr = tr[:-1]
    if dna[:3] in ["GTG", "TTG"]:
        tr = "M" + tr[1:]
    given = "".join(re.search('/translation="(.*?)"', block, re.S)[1].replace("\nFT", "\n").split())
    assert tr == given
    acc = {"pchE": "G3XCV2", "pchF": "Q9HWG4", "pchG": "Q9HWG5"}[g]
    dif = sum(a != b for a, b in zip(tr, ups[acc]["sequence"]["value"], strict=True))
    assert dif == (6 if g == "pchF" else 0)
    seqchecks.append(dict(source="AF074705.2", gene=g, current=acc, substitutions=dif))
pdb = read(originals / "RCSB-7EMY.json")["entity_poly"]["pdbx_seq_one_letter_code_can"]
assert (
    ups["G3XCV2"]["sequence"]["value"] in pdb
    and len(pdb) - len(ups["G3XCV2"]["sequence"]["value"]) == 17
)
redirect = read(originals / "uniprot-O85740.json")
assert redirect["primaryAccession"] == "Q9HWG4" and "O85740" in redirect["secondaryAccessions"]
# Meaningful altered-record controls are checked against the original sources.
negative = []
for key, mut in [
    ("missing_reaction", lambda d: d["reactions"].pop()),
    ("wrong_side", lambda d: d["mechanistic_edges"][0].update(subject="CHEBI:15377")),
    (
        "false_exact_I_only",
        lambda d: d.update(
            description=d["description"].replace(
                "does not assert exclusive I production",
                "asserts exclusive I production",
            )
        ),
    ),
    (
        "batch_pointer",
        lambda d: next(
            v
            for e in d["mechanistic_edges"]
            for v in e["evidence"]
            if v["reference_id"] == "UniProtKB:G3XCV2"
        ).update(source_locator="/sequence/value"),
    ),
    (
        "pchf_role_annotation_transfer",
        lambda d: next(e for e in d["mechanistic_edges"] if e["id"] == "pch-edge-062")["evidence"][
            0
        ].update(source_assertion="Current PAO1 functional annotation supports methylation."),
    ),
    (
        "pchf_primary_projection_transfer",
        lambda d: next(e for e in d["mechanistic_edges"] if e["id"] == "pch-edge-063")["evidence"][
            1
        ].update(source_assertion="The native I structure is a formal projection."),
    ),
    (
        "endpoint_source_transfer",
        lambda d: next(
            v
            for e in d["mechanistic_edges"]
            if e["id"] == "pch-edge-037"
            for v in e["evidence"]
            if v["reference_id"] == "MetaCyc:CPD-9992"
        ).update(
            source_assertion=(
                "The /p-1 source-defined product projects one member of the "
                "physiological I/II mixture."
            )
        ),
    ),
]:
    d = copy.deepcopy(raw)
    mut(d)
    try:
        science(d)
    except (AssertionError, KeyError, TypeError, AttributeError, IndexError):
        negative.append(dict(name=key, rejected=True))
    else:
        raise AssertionError("invalid-record control passed: " + key)
cmd = [
    str(a.rdkit_python),
    str(a.reactive_helper),
    "--manifest",
    str(M),
    "--projection",
    str(P),
    "--output",
    str(work / "reactive-chemistry.json"),
]
proc = subprocess.run(cmd, cwd=R, text=True, capture_output=True)
(work / "reactive-chemistry.log").write_text(proc.stdout + proc.stderr)
assert proc.returncode == 0, proc.stderr
np, ep = write_kgx([rec], work / "kgx")
en = list(csv.DictReader(ep.open(), delimiter="\t"))
nn = list(csv.DictReader(np.open(), delimiter="\t"))
assert len(en) == len(raw["mechanistic_edges"])
for e, k in zip(raw["mechanistic_edges"], en, strict=True):
    assert (e["subject"], LOCAL_PREDICATE_CURIES[e["predicate"]], e["object"]) == (
        k["subject"],
        k["predicate"],
        k["object"],
    )
    assert json.loads(k["evidence"]) == e["evidence"]
    for r in json.loads(k["reference_metadata"]):
        assert r == refs[r["id"]]
for n in raw["participants"]:
    if n["category"] == "chemical_entity":
        assert next(x for x in nn if x["id"] == n["id"])["category"] == "biolink:ChemicalEntity"
result = dict(
    started_at=started_at,
    finished_at=datetime.now(UTC).isoformat(),
    status="passed",
    scope=(
        "External prepared-authority author replay; "
        "no maintained corpus gate or scientific self-approval"
    ),
    record_sha256=sha(T),
    source_manifest_sha256=sha(M),
    source_projection_sha256=sha(P),
    original_sources=len(manifest["sources"]),
    native_objects=len(members),
    native_sides=len(proj["chemical_sides"]),
    balances=11,
    sequence_checks=seqchecks,
    negative_controls=negative,
    checks=[
        "native+closed schema",
        "unchanged canonical identifier policy",
        "all original reference body hashes",
        "11 full native membership objects and native sides",
        "exact small-molecule InChI and zwitterion charges",
        "actual batch pointers and original article-title locations",
        "separate native endpoint, protonation-normalized I structure and primary I/II evidence",
        "original PA14/PAO1 CDS translations and differences",
        "PchE deposited core plus tag",
        "original reactive-group chemistry including domain anchors",
        "actual KGX evidence/reference preservation",
    ],
    kgx=dict(
        nodes=len(nn),
        edges=len(en),
        evidence=sum(len(e["evidence"]) for e in raw["mechanistic_edges"]),
        nodes_sha256=sha(np),
        edges_sha256=sha(ep),
    ),
    reactive_command=cmd,
    reactive_exit_code=proc.returncode,
    helper_sha256=sha(Path(__file__)),
    reactive_helper_sha256=sha(a.reactive_helper),
    limits=[
        "No full-protein or stable DEFG assembly stoichiometry",
        (
            "Native I monoanion is one observed-product projection, "
            "not exclusive physiological release"
        ),
        "Historical constructs and inferred current annotations remain qualified",
        "Three ATP is derived, not measured",
    ],
)
# Uncached checks include original sources, parsed metadata, policies, snapshots,
# scientific record, helper code and repository validation/runtime inputs.
verify_bindings("before_receipt")
result["input_bindings"] = list(input_bindings.values())
result["input_binding_recheck"] = dict(
    at=datetime.now(UTC).isoformat(),
    status="passed",
    uncached=True,
    files=len(input_bindings),
    stage="immediately_before_exclusive_receipt",
)
with OUT.open("x") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
print(
    "PASS",
    len(members),
    "native objects;",
    len(en),
    "edges;",
    result["kgx"]["evidence"],
    "evidence; external author replay",
)
