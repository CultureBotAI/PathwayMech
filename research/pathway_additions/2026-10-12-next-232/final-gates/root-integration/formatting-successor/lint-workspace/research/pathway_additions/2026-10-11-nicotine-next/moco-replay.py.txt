"""Replay Moco native identity, complete chemistry and target KGX from preserved public sources."""

import collections
import csv
import datetime
import gzip
import hashlib
import io
import json
import re
import sqlite3
import xml.etree.ElementTree as E
from pathlib import Path

import yaml
from lxml import etree, html

from pathwaymech.kgx import render_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

P = Path("/private/tmp/pathwaymech-nicotine-next-evidence/moco")
C = Path("/private/tmp/pathwaymech-curation-authorities")
B = "http://rdf.rhea-db.org/"
rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
masters = {"49576", "49580", "17457", "48612", "43616", "26333", "31331", "35047", "26377"}
rows = {
    r["RHEA_ID_MASTER"]: r
    for r in csv.DictReader((C / "rhea-directions.tsv").open(), delimiter="\t")
    if r["RHEA_ID_MASTER"] in masters
}
nums = {v for r in rows.values() for v in r.values()}
nodes = {}
comp = {}
with gzip.open(C / "rhea.rdf.gz", "rb") as f:
    context = E.iterparse(f, events=["start", "end"])
    _, root = next(context)
    for event, e in context:
        if event != "end" or e.tag != rdf + "Description":
            continue
        uri = e.get(rdf + "about", "")
        n = uri.rsplit("/", 1)[-1]
        chosen = n.split("_")[0] in nums or (
            n.startswith("Participant_") and n.split("_")[1] in nums
        )
        dest = nodes if chosen else comp if n.startswith("Compound_") else None
        if dest is not None:
            for ch in e:
                k = ch.tag.rsplit("}", 1)[-1]
                v = ch.get(rdf + "resource") or (ch.text or "").strip()
                if v not in dest.setdefault(uri, {}).setdefault(k, []):
                    dest[uri][k].append(v)
        e.clear()
        root.clear()
while True:
    needed = {
        v
        for fields in nodes.values()
        for vals in fields.values()
        for v in vals
        if v in comp and v not in nodes
    }
    if not needed:
        break
    nodes.update({i: comp[i] for i in needed})
sides = []
balances = []
for m, row in rows.items():
    d = row["RHEA_ID_LR"]
    atoms = collections.Counter()
    charge = 0
    for role in ["substrates", "products"]:
        side = nodes[B + d][role][0]
        for co, pts in nodes[side].items():
            if not re.fullmatch(r"contains\d+", co):
                continue
            for pt in pts:
                cu = nodes[pt]["compound"][0]
                cp = nodes[cu]
                cid = cp["accession"][0].replace("GENERIC:", "RHEA-COMP:")
                n = int(co[8:])
                bn = nodes[cp["reactivePart"][0]] if cp.get("reactivePart") else cp
                parts = re.findall(r"([A-Z][a-z]?)(\d*)", bn["formula"][0])
                assert "".join(a + b for a, b in parts) == bn["formula"][0]
                sgn = -1 if role == "substrates" else 1
                for a, b in parts:
                    atoms[a] += sgn * n * int(b or 1)
                charge += sgn * n * int(bn["charge"][0])
                sides.append(
                    {
                        "master": m,
                        "reaction": "RHEA:" + d,
                        "side": role,
                        "coefficient": n,
                        "chemical": cid,
                        "side_uri": side,
                        "participant_uri": pt,
                        "compound_uri": cu,
                    }
                )
    assert all(v == 0 for v in atoms.values()) and charge == 0, (m, atoms, charge)
    balances.append(
        {"reaction": "RHEA:" + d, "atom_or_R_delta": dict(atoms), "charge_delta": charge}
    )
con = sqlite3.connect("file:" + str(C / "chebi.db") + "?mode=ro", uri=True)
identities = {}
for cid in sorted(
    {s["chemical"] for s in sides} | {"CHEBI:49883", "CHEBI:18420", "CHEBI:29105", "CHEBI:597326"}
):
    if cid.startswith("CHEBI:"):
        identities[cid] = {
            p: v if v is not None else o
            for p, v, o in con.execute(
                "select predicate,value,object from statements where subject=? "
                "and predicate in ('rdfs:label','chemrof:generalized_empirical_formula',"
                "'chemrof:charge','owl:deprecated')",
                (cid,),
            )
        }
    else:
        identities[cid] = nodes[B + "Compound_" + cid.split(":")[1]]

chemids = set(identities)
# Compare a fresh source replay with the maintained graph and its dossier.
ROOT = Path.cwd()
D = ROOT / "research/pathway_additions/2026-10-11-nicotine-next"
T = ROOT / "data/pathways/molybdenum-cofactor-biosynthesis.yaml"


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


y = yaml.safe_load(T.read_text())
rec = validate_record(y)
assert strict_errors([T], ROOT) == []
projection = json.loads((D / "moco-source-projection.json").read_text())
manifest = json.loads((D / "moco-source-manifest.json").read_text())
ids = json.loads((D / "moco-identifiers.json").read_text())
assert all(z["target_sha256"] == digest(T) for z in [projection, manifest, ids])
selected = {r["selected_master"].split(":")[1] for r in projection["native_reactions"]}
ss = [s for s in sides if s["master"] in selected]
bb = [b for b in balances if b["reaction"] != "RHEA:26378"]
assert ss == projection["rhea"]["sides"] and bb == projection["rhea"]["balances"]
assert len(ss) == 44 and len(bb) == 8
assert nodes == projection["rhea"]["nodes"] and identities == projection["rhea"]["identities"]
expected = collections.Counter(
    (s["chemical"], "consumes", s["reaction"])
    if s["side"] == "substrates"
    else (s["reaction"], "produces", s["chemical"])
    for s in ss
)
actual = collections.Counter(
    (e["subject"], e["predicate"], e["object"])
    for e in y["mechanistic_edges"]
    if e["predicate"] in ["consumes", "produces"]
)
assert expected == actual
for s in ss:
    key = (
        (s["chemical"], "consumes", s["reaction"])
        if s["side"] == "substrates"
        else (s["reaction"], "produces", s["chemical"])
    )
    ed = next(
        e for e in y["mechanistic_edges"] if (e["subject"], e["predicate"], e["object"]) == key
    )
    e = ed["evidence"][0]
    assert f"coefficient {s['coefficient']}." in e["source_assertion"]
    assert all(
        v in e["source_locator"]
        for v in [
            s["side_uri"],
            s["participant_uri"],
            s["compound_uri"],
            "rh:contains" + str(s["coefficient"]),
        ]
    )
    assert e["reference_id"] == "RHEA:" + s["master"]
for m in selected:
    rid = rows[m]["RHEA_ID_LR"]
    assert B + rid in nodes[B + m]["directionalReaction"]
    assert (
        y["reactions"][next(i for i, r in enumerate(y["reactions"]) if r["id"] == "RHEA:" + rid)][
            "label"
        ]
        == nodes[B + rid]["equation"][0]
    )
# Exact canonical chemistry, including explicit generic redox symbols and complete carrier states.
for s in ss:
    cp = nodes[s["compound_uri"]]
    if s["chemical"].startswith("RHEA-COMP:"):
        assert len(cp["reactivePart"]) == 1 and cp["subClassOf"] == [B + "GenericPolypeptide"]
    else:
        cid = s["chemical"]
        form = identities[cid]["chemrof:generalized_empirical_formula"]
        form = re.sub(r"([A-Z][a-z]?)1(?!\d)", r"\1", form)
        if cid in ["CHEBI:13193", "CHEBI:17499"]:
            form = form.replace("A", "R")

        def atom(f):
            return collections.Counter(
                {a: int(b or 1) for a, b in re.findall(r"([A-Z][a-z]?)(\d*)", f)}
            )

        assert atom(form) == atom(cp["formula"][0]), (cid, form, cp["formula"])
        assert int(identities[cid]["chemrof:charge"]) == int(cp["charge"][0])
# Reverse native-to-ChEBI identity belongs to ChEBI, not a nonexistent native dblink.
assert (
    con.execute(
        "select value from statements where subject=? and predicate=?",
        ("CHEBI:131766", "oio:hasDbXref"),
    )
    .fetchall()
    .count(("metacyc.compound:CPD-19179",))
    == 1
)
# Native exact boundary and the known stale MoaA reference are both preserved.
native = etree.parse(str(P / "metacyc-PWY-6823.xml"))
assert set(native.xpath("/ptools-xml/Pathway/reaction-list/Reaction/@frameid")) == {
    r["native"] for r in projection["native_reactions"]
}
for r in projection["native_reactions"]:
    t = etree.parse(str(P / f"metacyc-{r['native']}.xml"))
    rx = t.getroot().find("Reaction")
    assert rx.findtext("reaction-direction") == r["native_direction"]
    cross = rx.xpath('dblink[dblink-db="RHEA"]/dblink-oid/text()')
    assert cross == (
        ["26378"] if r["native"] == "RXN-8340" else [r["selected_directional"].split(":")[1]]
    )
for r in projection["assemblies"]:
    f = r["id"].split(":")[1]
    t = etree.parse(str(P / f"metacyc-{f}.xml"))
    assert t.xpath("/ptools-xml/Protein/species/Organism/@frameid") == ["TAX-511145"]
    for c in r["components"]:
        assert (
            int(
                t.xpath(
                    "/ptools-xml/Protein/component[Protein/@frameid=$m]/coefficient/text()",
                    m=c["native"],
                )[0]
            )
            == c["coefficient"]
        )
        q = etree.parse(str(P / f"metacyc-{c['native']}.xml"))
        assert q.xpath('/ptools-xml/Protein/dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [
            c["uniprot"]
        ]
        assert any(
            e["subject"] == "UniProtKB:" + c["uniprot"]
            and e["object"] == r["id"]
            and e["predicate"] == "part_of"
            for e in y["mechanistic_edges"]
        )
for n in y["participants"]:
    if n["id"].startswith("UniProtKB:"):
        a = n["id"].split(":")[1]
        u = json.loads((P / f"uniprot-{a}.json").read_text())
        assert (
            u["primaryAccession"] == a
            and u["organism"]["taxonId"] == 83333
            and u["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
        )
        assert n["label"] == u["proteinDescription"]["recommendedName"]["fullName"]["value"]
    elif n["id"].startswith("CHEBI:"):
        assert n["label"] == identities[n["id"]]["rdfs:label"]
    elif n["id"].startswith("RHEA-COMP:"):
        assert n["label"] == identities[n["id"]]["name"][0]
    elif n["id"].startswith("MetaCyc:"):
        f = n["id"].split(":")[1]
        p = P.parent / "root-authorities" / f"metacyc-{f}-2026-10-11.html"
        if p.exists():
            assert n["label"] == html.fromstring(p.read_bytes()).xpath("//title/text()")[
                0
            ].removeprefix("MetaCyc ")
        else:
            assert n["label"] == etree.parse(str(P / f"metacyc-{f}.xml")).findtext(
                "Protein/common-name"
            )
# Rehash source bodies once each; never load large authorities into memory.
hashes = {}
sourcechecks = []
for r in manifest["sources"]:
    if "sha256" in r and "path" in r:
        f = r["path"]
        if f not in hashes:
            hashes[f] = digest(f)
        assert hashes[f] == r["sha256"]
        sourcechecks.append({"path": f, "sha256": r["sha256"]})
for r in [manifest["rhea_source"], manifest["chebi_source"]]:
    f = r["path"]
    if f not in hashes:
        hashes[f] = digest(f)
    assert hashes[f] == r["sha256"]
    sourcechecks.append({"path": f, "sha256": r["sha256"]})
for r in y["references"]:
    f = manifest["reference_paths"][r["id"]]
    if f not in hashes:
        hashes[f] = digest(f)
    assert hashes[f] == r["source_sha256"]
# Every native structured locator resolves; subfields and side coefficients checked above.
locators = 0
quotes = []
for ed in y["mechanistic_edges"]:
    for ev in ed["evidence"]:
        rid = ev["reference_id"]
        f = Path(manifest["reference_paths"][rid])
        if "quote" in ev:
            root = (
                etree.parse(str(f)).getroot()
                if f.suffix == ".xml"
                else html.fromstring(f.read_bytes())
            )
            text = " ".join(" ".join(root.itertext()).split())
            q = " ".join(ev["quote"].split())
            assert q in text, (ed["id"], q)
            quotes.append({"edge": ed["id"], "reference": rid, "quote": ev["quote"]})
        elif rid.startswith("MetaCyc:"):
            doc = etree.parse(str(f))
            loc = ev["source_locator"]
            prefix, fields = (
                loc.rsplit("/", 1)
                if False
                else (loc[: loc.index("']/") + 3], loc[loc.index("']/") + 3 :])
            )
            for field in fields.split("; "):
                assert doc.xpath(prefix + field), (ed["id"], prefix + field)
            locators += 1
        elif rid.startswith("UniProtKB:"):
            u = json.loads(f.read_text())
            m = re.search(r"comments\[(\d+)\]", ev["source_locator"])
            assert m and int(m.group(1)) < len(u["comments"])
            locators += 1
# Assertions must retain source-specific limits rather than inherit direct experimental grades.
e = next(
    e
    for e in y["mechanistic_edges"]
    if e["subject"] == "UniProtKB:P30745" and e["predicate"] == "enables"
)
assert "HAMAP" in e["description"] and "Staphylococcus aureus" in e["description"]
e = next(e for e in y["mechanistic_edges"] if e["subject"] == "UniProtKB:P78067")
assert (
    e["predicate"] == "enables"
    and "enhanc" in e["description"]
    and "universally required" in e["description"]
)
assert not any(
    e["predicate"] == "has_cofactor"
    and e["subject"] in ["UniProtKB:P12282", "UniProtKB:P0AF03"]
    and e["object"] == "CHEBI:18420"
    for e in y["mechanistic_edges"]
)
# Actual KGX bytes retain evidence, descriptions and carrier categories.
kgx = render_kgx([rec])
out = P / "kgx"
out.mkdir(exist_ok=True)
for name, body in kgx.items():
    (out / name).write_text(body)
kn = list(csv.DictReader(io.StringIO(kgx["nodes.tsv"]), delimiter="\t"))
ke = list(csv.DictReader(io.StringIO(kgx["edges.tsv"]), delimiter="\t"))
assert len(ke) == 73
for row, ed in zip(ke, y["mechanistic_edges"], strict=True):
    assert json.loads(row["evidence"]) == ed["evidence"] and row["description"] == ed["description"]
for c in [i for i in chemids if i.startswith("RHEA-COMP:")]:
    assert next(n for n in kn if n["id"] == c)["category"] == "biolink:Protein"
assert sum(len(json.loads(r["evidence"])) for r in ke) == sum(
    len(e["evidence"]) for e in y["mechanistic_edges"]
)
receipt = {
    "command": (
        "UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache "
        ".venv/bin/python research/pathway_additions/"
        "2026-10-11-nicotine-next/moco-replay.py"
    ),
    "completed_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target_sha256": digest(T),
    "status": "pass",
    "counts": {
        "participants": len(y["participants"]),
        "reactions": len(y["reactions"]),
        "chemical_sides": len(ss),
        "balances": len(bb),
        "edges": len(ke),
        "evidence": sum(len(e["evidence"]) for e in y["mechanistic_edges"]),
        "named_ids": len(ids["identifiers"]),
        "references": len(y["references"]),
        "kgx_nodes": len(kn),
        "native_or_uniprot_locators": locators,
    },
    "checks": [
        "Native schema and closed LinkML schema",
        "Fresh full Rhea RDF and directions replay; all selected sides/coefficient locators",
        "Eight exact atom/formal charge balances, reactive protein backbones cancel",
        "ChEBI formulas/charges and Rhea whole carrier classes",
        "Eight native pathway members and stale cross-reference disposition",
        "Six assemblies and seven exact UniProt component bridges",
        "Nine reviewed K-12 UniProt identities and labels",
        "Fetched body digests and all record reference hashes",
        "Literal primary quotes",
        "Actual KGX evidence, descriptions and carrier categories",
    ],
    "literal_quotes": quotes,
    "source_hash_checks": sourcechecks,
    "limitations": [
        "Author narrow checks only; full gates and independent review are delegated.",
        "YnjE primary abstract available; PMC HTML is challenge and EuropePMC XML failed.",
        "K-12 MoaA cyclase/clusters are inferred; Staphylococcus experiments remain separate.",
        "Current metal form is not equated to the old drawing or a uniform in vivo redox state.",
    ],
}
(P / "replay-result.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(
    json.dumps(
        {"status": "pass", "target_sha256": receipt["target_sha256"], "counts": receipt["counts"]}
    )
)
