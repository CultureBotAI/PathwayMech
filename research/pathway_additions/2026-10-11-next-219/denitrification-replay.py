"""Offline source replay of complete native denitrification; author check, not approval."""

import argparse
import csv
import gzip
import hashlib
import importlib.util
import json
import os
import re
import sqlite3
import sys
import tempfile
from collections import Counter
from copy import deepcopy
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("--record", required=True, type=Path)
p.add_argument("--repo", required=True, type=Path)
p.add_argument("--output", required=True, type=Path)
a = p.parse_args()
assert a.record.is_file() and a.repo.is_dir()
assert a.output.parent.is_dir() and not os.path.lexists(a.output)
R = Path(__file__).resolve().parent
ORIGINAL_AUTHOR = Path("/private/tmp/pathwaymech-denitrification-author-20261011")
D = R / "draft"
started = datetime.now(UTC).isoformat()
bindings = {}
captured = {}


def digest(b):
    return hashlib.sha256(b).hexdigest()


def filehash(path):
    with Path(path).open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def bind(path, expected=None, retain=True):
    path = Path(path).absolute()
    resolved = path.resolve(strict=True)
    if str(path) in bindings:
        row = bindings[str(path)]
        assert resolved == Path(row["resolved_path"])
        if expected:
            assert expected == row["sha256"]
        return
    b = resolved.read_bytes() if retain else None
    h = digest(b) if retain else filehash(resolved)
    assert path.resolve(strict=True) == resolved, ("retargeted while capturing", path)
    if expected:
        assert h == expected, ("input digest", path)
    bindings[str(path)] = {
        "path": str(path),
        "resolved_path": str(resolved),
        "sha256": h,
    }
    if retain:
        captured[str(path)] = b


def original(path):
    return captured[str(Path(path).absolute())]


def readj(path):
    return json.loads(original(path))


def fresh():
    for row in bindings.values():
        path = Path(row["path"])
        assert path.resolve(strict=True) == Path(row["resolved_path"]), (
            "input path changed",
            path,
        )
        assert filehash(path) == row["sha256"], ("input bytes changed", path)


# Bind formal inputs before imports, first reads, parser use, or arbitrary source execution.
formal = [
    a.record,
    Path(__file__),
    *sorted(D.glob("*.json")),
    D / "denitrification-curation.md",
    R / "predecessor-preservation.json",
    R / "correction.json",
]
runtime = [
    *sorted((a.repo / "src/pathwaymech").rglob("*.py")),
    a.repo / "src/pathwaymech/schema/pathwaymech.yaml",
    a.repo / "scripts/build_source_identifier_snapshot.py",
]
for path in formal + runtime:
    bind(path)
manifest = readj(D / "denitrification-source-manifest.json")
for row in readj(R / "predecessor-preservation.json")["files"]:
    bind(row["path"], row["sha256"])
for row in manifest["prior_proof_inputs"]:
    bind(row["path"], row["sha256"])
for row in manifest["bodies"]:
    bind(row["path"], row["sha256"])
for row in manifest["issuing_databases"]:
    bind(row["path"], row["sha256"], retain=False)
adapter = Path(
    "/private/tmp/claw-published-duf-offline-20261007/src/kg_microbe_sources/imodulondb.py"
)
bind(adapter, "1901c6ab519795051d0b70b57412c4ad463949b3dd02a49d05936464e6fd4aa2")
for fn in [
    "context.json",
    "context-manifest.json",
    "inventory.json",
    "inventory-manifest.json",
    "adapter.json",
]:
    bind(ORIGINAL_AUTHOR / "imod" / fn)
for row in readj(ORIGINAL_AUTHOR / "imod/context-manifest.json") + readj(
    ORIGINAL_AUTHOR / "imod/inventory-manifest.json"
):
    bind(row["path"], row["sha256"])
assert str(a.output.absolute()) not in bindings
assert str(a.output.resolve()) not in {x["resolved_path"] for x in bindings.values()}
# Imports deliberately follow complete input capture and path selection.
sys.path.insert(0, str(a.repo / "src"))
import yaml  # noqa: E402
from lxml import etree, html  # noqa: E402

from pathwaymech.kgx import kgx_edges, kgx_nodes, write_kgx  # noqa: E402
from pathwaymech.schema import validate_record  # noqa: E402
from pathwaymech.strict import strict_errors  # noqa: E402

record = yaml.safe_load(original(a.record))
projection = readj(D / "denitrification-source-projection.json")
facts = readj(D / "denitrification-chemical-identities.json")
proteins = readj(D / "denitrification-protein-projection.json")
scope = readj(D / "denitrification-chemistry-and-scope.json")
authority = readj(D / "denitrification-authority-proposal.json")
refs = {x["id"]: x for x in record["references"]}
assert (
    digest(original(a.record))
    == manifest["record_sha256"]
    == projection["record_sha256"]
)
assert record["references"] == manifest["references"]
paths = projection["references_to_original_paths"]
# No double attribution: each located assertion is replayed at its original exact pointer/XPath.
replayed = []
for span in projection["evidence_spans"] + projection.get("scope_only_spans", []):
    assert span["sha256"] == bindings[span["path"]]["sha256"]
    assert refs[span["reference_id"]]["source_sha256"] == span["sha256"]
    payload = []
    for sel in span["selectors"]:
        if span["kind"] == "json":
            q = readj(span["path"])
            for key in sel.strip("/").split("/") if sel != "/" else []:
                q = q[int(key)] if isinstance(q, list) else q[key]
            payload.append(q)
        elif span["kind"] in ["xml", "html"]:
            t = etree.ElementTree(
                html.fromstring(original(span["path"]))
                if span["kind"] == "html"
                else etree.fromstring(original(span["path"]))
            )
            xs = t.xpath(sel)
            assert xs, (span["reference_id"], sel)
            payload.append(
                [
                    etree.tostring(x, encoding="unicode")
                    if isinstance(x, etree._Element)
                    else str(x)
                    for x in xs
                ]
            )
        elif span["kind"] == "sql":
            with sqlite3.connect(f"file:{span['path']}?mode=ro", uri=True) as db:
                rows = [
                    {"predicate": p, "value": v, "object": o}
                    for p, v, o in db.execute(
                        "select predicate,value,object from statements where subject=?",
                        (span["reference_id"],),
                    )
                ]
            payload.append(rows)
        elif span["kind"] == "cif":
            chunks = original(span["path"]).decode().split("\n#")
            xs = [x for x in chunks if "\n" + sel in x]
            assert len(xs) == 1
            payload.append(xs[0])
        else:
            raise ValueError(span["kind"])
    assert (
        digest(json.dumps(payload, sort_keys=True).encode()) == span["payload_sha256"]
    ), span
    replayed.append(
        (span["reference_id"], span["source_locator"], span["source_assertion"])
    )
actual = [
    (v["reference_id"], v["source_locator"], v["source_assertion"])
    for e in record["mechanistic_edges"]
    for v in e["evidence"]
]
scope_blocks = projection["taxon_scope_evidence"]["evidence"]
web_blocks = projection["web_inspected_evidence"]
assert Counter(actual) + Counter(
    (x["reference_id"], x["source_locator"], x["source_assertion"])
    for x in scope_blocks
) == Counter(replayed) + Counter(
    (x["reference_id"], x["source_locator"], x["source_assertion"]) for x in web_blocks
)
assert (
    len(web_blocks) == 1
    and "no local full-text" in refs[web_blocks[0]["reference_id"]]["source_version"]
)
# Full native objects and direction fields independently rebuilt from original XML.
route = etree.fromstring(original(paths[record["id"]]))
members = route.xpath("/ptools-xml/Pathway/reaction-list/Reaction/@frameid")
assert len(members) == 5 and {"MetaCyc:" + x for x in members} == set(
    projection["full_members"]
)
assert {x["id"] for x in record["reactions"]} == set(projection["full_members"])
assert all(x["direction"] == "left_to_right" for x in record["reactions"])
for frame in members:
    assert route.xpath(
        f'/ptools-xml/Pathway/reaction-layout[Reaction/@frameid="{frame}"]/direction/text()'
    ) == ["L2R"]
small = facts["native_small_molecule_bridges"]
native_sides = {}
for rid in projection["full_members"]:
    t = etree.fromstring(original(paths[rid]))
    rows = []
    for side in ["left", "right"]:
        for i, x in enumerate(t.findall("Reaction/" + side), 1):
            native = x[0].get("frameid")
            c = x.find("compartment/cco")
            rows.append(
                {
                    "side": side,
                    "native": native,
                    "node": small.get(native, {}).get(
                        "selected_id", "MetaCyc:" + native
                    ),
                    "coefficient": int(x.findtext("coefficient") or 1),
                    "compartment": c.get("frameid") if c is not None else None,
                    "selector": f"/ptools-xml/Reaction/{side}[{i}]",
                }
            )
    native_sides[rid] = rows
assert native_sides == projection["native_sides"]
# Issuing chemical identities; all seven small molecules are exact structures, not name matches.
for cid, t in facts["terms"].items():
    dbpath = facts["databases"][t["source"]]["path"]
    with sqlite3.connect(f"file:{dbpath}?mode=ro", uri=True) as db:
        rows = [
            {"predicate": p, "value": v, "object": o}
            for p, v, o in db.execute(
                "select predicate,value,object from statements where subject=?", (cid,)
            )
        ]
    assert rows == t["statements"]
    assert not any(
        x["predicate"] == "owl:deprecated" and x["value"] == "true" for x in rows
    )
for frame, v in small.items():
    tree = etree.fromstring(original(paths["MetaCyc:" + frame]))
    e = tree.find("Compound")
    assert e.findtext("inchi") == v["native_inchi"]
    assert int(e.find("cml/molecule").get("formalCharge")) == v["charge"]
    terms = facts["terms"][v["selected_id"]]["statements"]
    assert (
        next(x["value"] for x in terms if x["predicate"] == "chemrof:inchi_string")
        == v["native_inchi"]
    )
# Read current native Rhea 142 graph, retaining nested Compound objects and containsN coefficients.
rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
rh = "http://rdf.rhea-db.org/"
g = {}
with gzip.open(facts["databases"]["rhea.rdf.gz"]["path"], "rb") as stream:
    for _, el in etree.iterparse(stream, events=("end",), tag=rdf + "Description"):
        uri = el.get(rdf + "about")
        if uri:
            node = g.setdefault(uri, {})
            for c in el:
                pred = etree.QName(c).localname
                v = c.get(rdf + "resource") or (c.text or "").strip()
                if v not in node.setdefault(pred, []):
                    node[pred].append(v)
        el.clear()
        while el.getprevious() is not None:
            del el.getparent()[0]
for fam, selection in facts["rhea_native_projection"].items():
    for uri, expected in selection.items():
        assert g[uri] == expected, (fam, uri)
# Deliberately broad class comparison only: preserve source-native carrier subclasses
# and vectorial protons in the maintained graph, rather than asserting exact identities.
class_ids = {k: v["selected_id"] for k, v in small.items()}
class_ids.update(
    {
        "ETR-Quinols": "CHEBI:24646",
        "ETR-Quinones": "CHEBI:132124",
        "Reduced-cytochromes-c551": "GENERIC:10350",
        "Cytochromes-C-Reduced": "GENERIC:10350",
        "Oxidized-cytochromes-c551": "GENERIC:14399",
        "Cytochromes-C-Oxidized": "GENERIC:14399",
    }
)
class_comparisons = []
rhea_count = 0
for case in scope["rhea_class_comparisons"]:
    rid = case["rhea"].split(":")[1]
    r = g[rh + rid]
    assert rh + rid in g[rh + case["master"]]["directionalReaction"]
    assert r["status"] == [rh + "Approved"]
    sides = []
    for side in ["substrates", "products"]:
        for pred, parts in g[r[side][0]].items():
            if re.fullmatch(r"contains\d+", pred):
                for part in parts:
                    cu = g[part]["compound"][0]
                    sides.append(
                        {
                            "side": side,
                            "coefficient": int(pred[8:]),
                            "compound_uri": cu,
                            "compound": g[cu],
                        }
                    )
    assert sides == case["sides"]
    native_class = Counter()
    rhea_class = Counter()
    for x in native_sides[case["native"]]:
        native_class[class_ids[x["native"]]] += x["coefficient"] * (
            -1 if x["side"] == "left" else 1
        )
    for x in sides:
        rhea_class[x["compound"]["accession"][0]] += x["coefficient"] * (
            -1 if x["side"] == "substrates" else 1
        )
    native_class = {k: v for k, v in native_class.items() if v}
    rhea_class = {k: v for k, v in rhea_class.items() if v}
    assert native_class == rhea_class, (case["native"], native_class, rhea_class)
    class_comparisons.append(
        {
            "native": case["native"],
            "rhea": case["rhea"],
            "scoped_class_counter": native_class,
            "scope": case["disposition"],
        }
    )
    rhea_count += len(sides)
assert g[rh + "10991"]["subClassOf"][0].endswith("BidirectionalReaction")
# Full compartment-preserving balance with symbolic unchanged carrier frameworks.
models = scope["native_whole_carrier_accounting"]["models"]
net = Counter()
balances = []
for rid, rows in native_sides.items():
    expected = next(
        x
        for x in scope["native_whole_carrier_accounting"]["balances"]
        if x["reaction"] == rid
    )
    atoms = Counter()
    charge = 0
    for x in rows:
        c = x["coefficient"] * (-1 if x["side"] == "left" else 1)
        m = models[x["native"]]
        for k, v in m["atoms"].items():
            atoms[k] += c * v
        charge += c * m["charge"]
        net[(x["native"], x["compartment"])] += c * expected["coefficient_to_one_N2"]
    assert not any(atoms.values()) and charge == 0
    balances.append(
        {"reaction": rid, "atom_residual": dict(atoms), "charge_residual": charge}
    )
assert [
    {"native": n, "compartment": c, "coefficient": v} for (n, c), v in net.items() if v
] == scope["native_whole_carrier_accounting"]["net_per_N2"]
assert net[("NITROGEN-MOLECULE", "CCO-OUT")] == 1
# Current protein evidence and exact structural sequence discrepancies.
for acc, pj in proteins.items():
    u = readj(pj["path"])
    assert u["primaryAccession"] == acc and u["organism"]["taxonId"] == 208964
    for key in [
        "sequence",
        "genes",
        "entryType",
        "organism",
        "entryAudit",
        "comments",
        "features",
    ]:
        assert u.get(key, []) == pj[key], (acc, key)
for x in scope["rcsb_sequence_dispositions"]:
    u = readj(x["path"])
    seq = u["entity_poly"]["pdbx_seq_one_letter_code_can"]
    assert digest(seq.encode()) == x["structure_sequence_sha256"]
    assert u["entity_src_nat"][0]["strain"] == "PAO1"
    assert (
        u["rcsb_polymer_entity_container_identifiers"]["reference_sequence_identifiers"]
        == x["issuing_mapping"]
    )
    assert seq != proteins[x["current_accession"]]["sequence"]["value"]
# Complete original CIF directly agrees with original entity sequences and source strain rows.
cif = original(paths["DOI:10.2210/pdb3o0r/pdb"]).decode()
for entity, _unused_accession in [(3, "Q59647"), (4, "Q59646")]:
    hits = re.findall(
        r"\n" + str(entity) + r" 'polypeptide\(L\)' no no \n;(.*?)\n;", cif, re.DOTALL
    )
    assert len(hits) == 1
    sequence = "".join(hits[0].split())
    native = readj(ORIGINAL_AUTHOR / "raw" / f"rcsb-3O0R-polymer-{entity}.json")
    assert sequence == native["entity_poly"]["pdbx_seq_one_letter_code_can"]
    assert re.search(
        r"\n"
        + str(entity)
        + r" 1 sample .*?'Pseudomonas aeruginosa' 208964 \? \? PAO1",
        cif,
    )

# Canonical issuing labels are parsed from authentic original bodies, not draft labels.
spec = importlib.util.spec_from_file_location(
    "builder", a.repo / "scripts/build_source_identifier_snapshot.py"
)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
labels = {}
for row in authority["sources"]:
    assert filehash(row["path"]) == row["sha256"]
    actual = list(b.source_terms(row["kind"], Path(row["path"]), url=row["url"]))
    assert json.loads(json.dumps(actual)) == row["extracted_terms"]
    for cid, label, syn in actual:
        labels[cid] = (label, syn)
for cid, term in facts["terms"].items():
    labels[cid] = (
        next(x["value"] for x in term["statements"] if x["predicate"] == "rdfs:label"),
        [],
    )
for node in [record, *record["taxa"], *record["participants"], *record["reactions"]]:
    assert node["label"] in [labels[node["id"]][0], *labels[node["id"]][1]], node


# Every chemical side appears once, with correct direction/class/transport semantics.
def check_graph(r):
    es = r["mechanistic_edges"]
    rs = {x["id"] for x in r["reactions"]}
    assert rs == set(native_sides)
    assert {
        x["object"]
        for x in es
        if x["subject"] == r["id"] and x["predicate"] == "has_part"
    } == rs
    chemistry = [
        e
        for e in es
        if e["predicate"] in ["consumes", "produces", "has_input", "has_output"]
    ]
    expected = []
    for rid, rows in native_sides.items():
        for x in rows:
            left = x["side"] == "left"
            transport = rid == "MetaCyc:TRANS-RXN0-239"
            triple = (
                (rid, "has_input" if left else "has_output", x["node"])
                if transport
                else (x["node"], "consumes", rid)
                if left
                else (rid, "produces", x["node"])
            )
            expected.append(triple)
            matches = [
                e
                for e in chemistry
                if (e["subject"], e["predicate"], e["object"]) == triple
            ]
            assert len(matches) == 1, triple
            assert f"Coefficient {x['coefficient']};" in matches[0]["description"]
            assert any(
                z["reference_id"] == rid
                and z["source_locator"] == "XPath " + x["selector"]
                for z in matches[0]["evidence"]
            )
    assert Counter(
        (e["subject"], e["predicate"], e["object"]) for e in chemistry
    ) == Counter(expected)
    assert not any(
        e["predicate"] in ["enables", "catalyzes"]
        and e["object"] == "MetaCyc:TRANS-RXN0-239"
        for e in es
    )
    assert not any(e["predicate"] == "inhibits" for e in es)
    assert "antiport versus uniport remains unresolved" in r["description"]
    assert "proton-pump annotation conflicts" in r["description"]
    assert all(not x["id"].startswith("MetaCyc:CPLX") for x in r["participants"])
    assert "ECO:0000255 HAMAP" in next(
        e["description"]
        for e in es
        if e["subject"] == "UniProtKB:Q9HYL2" and e["predicate"] == "has_cofactor"
    )
    assert all(
        e["source_assertion"] == s["source_assertion"]
        for edge in es
        for e in edge["evidence"]
        for s in projection["evidence_spans"]
        if (e["reference_id"], e["source_locator"])
        == (s["reference_id"], s["source_locator"])
        and len(
            {
                s["source_assertion"]
                for s in projection["evidence_spans"]
                if (e["reference_id"], e["source_locator"])
                == (s["reference_id"], s["source_locator"])
            }
        )
        == 1
    )


check_graph(record)
negative = []
for name, mutator in [
    ("missing native transport", lambda r: r["reactions"].pop(1)),
    (
        "wrong redox direction",
        lambda r: next(
            e for e in r["mechanistic_edges"] if e["predicate"] == "consumes"
        ).update(predicate="produces"),
    ),
    (
        "c551 collapsed to generic carrier",
        lambda r: next(
            e
            for e in r["mechanistic_edges"]
            if e["subject"] == "MetaCyc:Reduced-cytochromes-c551"
        ).update(subject="MetaCyc:Cytochromes-C-Reduced"),
    ),
    (
        "coefficient loss",
        lambda r: next(
            e for e in r["mechanistic_edges"] if e["predicate"] == "consumes"
        ).update(description="Coefficient 7; invented"),
    ),
    (
        "unsupported exact antiport catalyst",
        lambda r: r["mechanistic_edges"].append(
            {
                "subject": "UniProtKB:Q9HXD4",
                "predicate": "enables",
                "object": "MetaCyc:TRANS-RXN0-239",
                "evidence": [],
            }
        ),
    ),
    (
        "transport certainty replacement",
        lambda r: r.update(
            description=r["description"].replace(
                "antiport versus uniport remains unresolved",
                "antiport is experimentally established",
            )
        ),
    ),
    (
        "silent pump conflict deletion",
        lambda r: r.update(
            description=r["description"].replace(
                "proton-pump annotation conflicts", "annotation agrees"
            )
        ),
    ),
]:
    mutant = deepcopy(record)
    mutator(mutant)
    try:
        check_graph(mutant)
    except (AssertionError, KeyError, ValueError):
        negative.append(name)
    else:
        raise AssertionError(("negative accepted", name))
# Offline identical iMod parsing retains actual source/parser failures.
# Nonhits imply no biological absence; import follows bound adapter selection.
sys.path.insert(0, str(adapter.parent.parent))
from kg_microbe_sources.imodulondb import ImodulonDBClient, ImodulonDBError  # noqa: E402

imodrows = readj(ORIGINAL_AUTHOR / "imod/context-manifest.json") + readj(
    ORIGINAL_AUTHOR / "imod/inventory-manifest.json"
)
raw = {x["url"]: json.loads(original(x["path"])) for x in imodrows}
client = ImodulonDBClient(transport=lambda u: raw[u])
context = readj(ORIGINAL_AUTHOR / "imod/context.json")
for dataset, queries in context["queries"].items():
    for query, expected in queries.items():
        try:
            got = asdict(client.search("p_aeruginosa", dataset, query))
        except ImodulonDBError as ex:
            got = {"error": repr(ex)}
        assert json.loads(json.dumps(got)) == expected
for key, fn in [("components", client.imodulon_genes), ("genes", client.gene)]:
    for dataset, rows in context[key].items():
        for term, expected in rows.items():
            try:
                got = asdict(
                    fn(
                        "p_aeruginosa",
                        dataset,
                        int(term) if key == "components" else term,
                    )
                )
            except ImodulonDBError as ex:
                got = {"error": repr(ex)}
            assert json.loads(json.dumps(got)) == expected

# Issue407 semantic source guards. Synchronized mutant projections ensure these
# reject the original provenance defects rather than merely stale target hashes.
old_record = yaml.safe_load(
    original(ORIGINAL_AUTHOR / "draft/nitrate-reduction-i-denitrification.yaml")
)
old_edges = {e["id"]: e for e in old_record["mechanistic_edges"]}
primary_tree = html.fromstring(original(paths["PMID:17400734"]))
primary_selector = "//article/section[2]/section/section[4]/p"
primary_p = primary_tree.xpath(primary_selector)
assert len(primary_p) >= 2
assert "nucleotide exchanges" in " ".join(primary_p[1].itertext())
assert "Anr box consensus motif" in " ".join(primary_p[1].itertext())
assert "No obvious promoter activity" in " ".join(primary_p[1].itertext())


def check_corrections(candidate, projected):
    by_id = {e["id"]: e for e in candidate["mechanistic_edges"]}
    anr = by_id["denitrification-edge-063"]["evidence"][1]
    assert (
        anr["source_assertion"]
        == old_edges["denitrification-edge-063"]["evidence"][1]["source_assertion"]
    )
    selected = primary_tree.xpath(anr["source_locator"].removeprefix("XPath "))
    assert [etree.tostring(p) for p in selected] == [
        etree.tostring(p) for p in primary_p[:2]
    ], "Anr experimental motif paragraph must be included with expression paragraph"
    nark = by_id["denitrification-edge-074"]
    loc = nark["evidence"][0]
    selected_json = []
    for pointer in loc["source_locator"].removeprefix("JSON pointer ").split("; "):
        value = readj(paths[loc["reference_id"]])
        for bit in pointer.strip("/").split("/"):
            value = value[int(bit)] if isinstance(value, list) else value[bit]
        selected_json.append(value)
    assert len(selected_json) == 2
    annotation, xref = selected_json
    assert annotation["commentType"] == "SUBCELLULAR LOCATION"
    subcellular = annotation["subcellularLocations"][0]
    assert subcellular["location"]["value"] == "Membrane"
    assert subcellular["topology"]["value"] == "Multi-pass membrane protein"
    code = subcellular["location"]["evidences"][0]
    assert code == {
        "evidenceCode": "ECO:0000256",
        "source": "ARBA",
        "id": "ARBA00004141",
    }
    assert xref["database"] == "GO" and xref["id"] == nark["object"] == "GO:0016020"
    assert {"key": "GoTerm", "value": "C:membrane"} in xref["properties"]
    assert {"key": "GoEvidenceType", "value": "IEA:UniProtKB-SubCell"} in xref[
        "properties"
    ]
    for text in [
        subcellular["location"]["value"],
        subcellular["topology"]["value"],
        code["evidenceCode"],
        code["id"],
        xref["id"],
    ]:
        assert text in loc["source_assertion"], ("Missing original source scope", text)
    assert "does not specify the inner/plasma membrane" in loc["source_assertion"]
    assert "no direct localization assay" in nark["description"]
    assert next(p for p in candidate["participants"] if p["id"] == xref["id"]) == {
        "id": "GO:0016020",
        "label": "membrane",
        "category": "cellular_component",
    }
    for e in (anr, loc):
        matches = [
            s
            for s in projected["evidence_spans"]
            if all(
                s[k] == e[k]
                for k in ("reference_id", "source_locator", "source_assertion")
            )
        ]
        assert len(matches) == 1, (
            "Corrected graph evidence must match its source projection"
        )
    assert candidate["reactions"] == old_record["reactions"]
    for edge in candidate["mechanistic_edges"]:
        if edge["id"] not in {"denitrification-edge-063", "denitrification-edge-074"}:
            assert edge == old_edges[edge["id"]], "Unrelated edge changed"


check_corrections(record, projection)
correction_negative = []


def synchronized_mutant(edge_id, field, value):
    candidate = deepcopy(record)
    projected = deepcopy(projection)
    edge = next(e for e in candidate["mechanistic_edges"] if e["id"] == edge_id)
    index = 1 if edge_id == "denitrification-edge-063" else 0
    before = deepcopy(edge["evidence"][index])
    if field.startswith("evidence."):
        edge["evidence"][index][field.split(".", 1)[1]] = value
    else:
        edge[field] = value
    after = edge["evidence"][index]
    row = next(
        s
        for s in projected["evidence_spans"]
        if all(
            s[k] == before[k]
            for k in ("reference_id", "source_locator", "source_assertion")
        )
    )
    row.update(after)
    if row["kind"] == "html":
        row["selectors"] = [after["source_locator"].removeprefix("XPath ")]
        payload = [
            [etree.tostring(p, encoding="unicode") for p in primary_tree.xpath(sel)]
            for sel in row["selectors"]
        ]
    else:
        row["selectors"] = (
            after["source_locator"].removeprefix("JSON pointer ").split("; ")
        )
        payload = []
        for sel in row["selectors"]:
            v = readj(row["path"])
            for bit in sel.strip("/").split("/"):
                v = v[int(bit)] if isinstance(v, list) else v[bit]
            payload.append(v)
    row["payload_sha256"] = digest(json.dumps(payload, sort_keys=True).encode())
    return candidate, projected


for name, edge_id, field, value in [
    (
        "original Anr p1-only selector with synchronized projection",
        "denitrification-edge-063",
        "evidence.source_locator",
        old_edges["denitrification-edge-063"]["evidence"][1]["source_locator"],
    ),
    (
        "unsupported inner-membrane object with synchronized evidence",
        "denitrification-edge-074",
        "object",
        "GO:0005886",
    ),
    (
        "original over-specific annotation assertion with synchronized projection",
        "denitrification-edge-074",
        "evidence.source_assertion",
        old_edges["denitrification-edge-074"]["evidence"][0]["source_assertion"],
    ),
    (
        "wrong GO functional cross-reference with synchronized projection",
        "denitrification-edge-074",
        "evidence.source_locator",
        "JSON pointer /comments/0; /uniProtKBCrossReferences/19",
    ),
    (
        "inference promoted to experiment with synchronized projection",
        "denitrification-edge-074",
        "evidence.source_assertion",
        next(
            e
            for e in record["mechanistic_edges"]
            if e["id"] == "denitrification-edge-074"
        )["evidence"][0]["source_assertion"].replace("ECO:0000256", "ECO:0000269"),
    ),
]:
    candidate, projected = synchronized_mutant(edge_id, field, value)
    try:
        check_corrections(candidate, projected)
    except (AssertionError, KeyError, ValueError):
        correction_negative.append(name)
    else:
        raise AssertionError(("Issue407 negative accepted", name))

# Actual closed-schema validation and complete KGX export, with byte-level edge evidence parity.
vr = validate_record(record)
assert not strict_errors([a.record], a.repo)
with tempfile.TemporaryDirectory(prefix="denitrification-kgx-") as temp:
    np, ep = write_kgx([vr], Path(temp))
    with ep.open() as f:
        actualrows = list(csv.DictReader(f, delimiter="\t"))
    assert len(actualrows) == len(record["mechanistic_edges"])
    assert Counter(
        (e["subject"], e["object"], e["description"], e["evidence"]) for e in actualrows
    ) == Counter(
        (e.subject, e.object, re.sub(r"\s+", " ", e.description).strip(), e.evidence)
        for e in kgx_edges([vr])
    )
    kgx = {
        "nodes": len(kgx_nodes([vr])),
        "edges": len(actualrows),
        "evidence": sum(len(json.loads(x["evidence"])) for x in actualrows),
        "nodes_sha256": filehash(np),
        "edges_sha256": filehash(ep),
    }
# Fresh uncached path and byte checks for EVERY formal, runtime, source and prior-proof input.
fresh()
result = {
    "status": "passed_author_source_replay_not_independent_approval",
    "started_at": started,
    "finished_at": datetime.now(UTC).isoformat(),
    "record_sha256": manifest["record_sha256"],
    "native_members": len(members),
    "native_sides": sum(map(len, native_sides.values())),
    "native_balances": balances,
    "rhea_class_sides": rhea_count,
    "qualified_rhea_class_comparisons": class_comparisons,
    "replayed_source_spans_including_scope": len(replayed),
    "graph_local_source_assertions": len(projection["evidence_spans"]),
    "scope_only_source_assertions": len(projection["scope_only_spans"]),
    "web_inspected_assertions": len(web_blocks),
    "negative_controls": negative,
    "issue407_source_semantic_negative_controls": correction_negative,
    "predecessor_files_preserved": len(
        readj(R / "predecessor-preservation.json")["files"]
    ),
    "kgx": kgx,
    "all_bound_inputs": list(bindings.values()),
    "limitations": [
        "Native strict antiport is a convention with PAO1 mechanism/catalyst unresolved.",
        "Rhea comparisons do not collapse compartments or c551 specificity.",
        (
            "Primary 2010 full article web inspection cannot be byte-replayed; "
            "original indexed abstract and RCSB bodies are retained."
        ),
        (
            "External author replay, no whole-corpus authority integration "
            "or formal independent review."
        ),
    ],
}
# Exclusive final creation prevents overwrite even if a competing output appears during replay.
with a.output.open("x") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
print(
    json.dumps(
        {
            k: v
            for k, v in result.items()
            if k not in ["all_bound_inputs", "native_balances"]
        }
    )
)
