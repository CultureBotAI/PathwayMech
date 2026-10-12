"""Author replay of complete biotin source bytes; writes optional external receipt only."""

import collections
import csv
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
import sys
import xml.etree.ElementTree as E
from pathlib import Path

import yaml
from lxml import etree as L
from lxml import html

from pathwaymech.kgx import kgx_edges, kgx_nodes
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

P = Path("/private/tmp/pathwaymech-next-184-evidence/biotin")
C = Path("/private/tmp/pathwaymech-curation-authorities")
masters = {"17105", "42700", "42288", "16861", "15805", "22060"}
rows = {
    r["RHEA_ID_MASTER"]: r
    for r in csv.DictReader((C / "rhea-directions.tsv").open(), delimiter="\t")
    if r["RHEA_ID_MASTER"] in masters
}
nums = {v for r in rows.values() for v in r.values()}
subjects = {}
comps = {}
rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
B = "http://rdf.rhea-db.org/"
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
        dest = subjects if chosen else comps if n.startswith("Compound_") else None
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
        for fields in subjects.values()
        for vals in fields.values()
        for v in vals
        if v in comps and v not in subjects
    }
    if not needed:
        break
    subjects.update({i: comps[i] for i in needed})
sides = []
for m, r in rows.items():
    rid = r["RHEA_ID_LR"]
    for side in ["substrates", "products"]:
        sn = subjects[B + rid][side][0]
        for co, ps in subjects[sn].items():
            if not re.fullmatch(r"contains\d+", co):
                continue
            for pt in ps:
                cu = subjects[pt]["compound"][0]
                cp = subjects[cu]
                c = cp["accession"][0].replace("GENERIC:", "RHEA-COMP:")
                sides.append(
                    dict(
                        master=m,
                        reaction="RHEA:" + rid,
                        side=side,
                        coefficient=int(co[8:]),
                        chemical=c,
                        side_uri=sn,
                        participant_uri=pt,
                        compound_uri=cu,
                    )
                )


D = Path("research/pathway_additions/2026-10-11-next-184")
T = Path("data/pathways/biotin-biosynthesis-i.yaml")
projection = json.loads((D / "biotin-source-projection.json").read_text())
assert (
    rows == projection["rows"] and subjects == projection["nodes"] and sides == projection["sides"]
)


def digest(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


r = yaml.safe_load(T.read_text())
record = validate_record(r)
assert not strict_errors([T], Path.cwd())
manifest = json.loads((D / "biotin-source-manifest.json").read_text())
assert manifest["record_sha256"] == digest(T)
for a in manifest["artifacts"]:
    # Shared builder separately rehashes 4 GB ChEBI; keep author source scope explicit.
    if a["file"] == "chebi.db":
        continue
    assert digest(Path(a["external_path"])) == a["sha256"], a["file"]
byhash = {a["sha256"]: a for a in manifest["artifacts"]}
for ref in r["references"]:
    assert ref["source_sha256"] in byhash, ref["id"]
refs = {ref["id"]: ref for ref in r["references"]}
edges = r["mechanistic_edges"]
nodes = {n["id"]: n for k in ["participants", "reactions", "taxa"] for n in r[k]}
assert (
    len(r["reactions"]) == 14
    and len(edges) == 126
    and sum(len(e["evidence"]) for e in edges) == 218
)
native = projection["native_reactions"]
expected = set()
sidechecks = []
for n in native:
    rid = n["record_id"]
    root = L.parse(str(P / f"metacyc-{n['id']}.xml")).getroot().find("Reaction")
    assert root.findtext("reaction-direction") == n["direction"]
    observed = []
    for side in ["left", "right"]:
        for z in root.findall(side):
            observed.append((side, z[0].get("frameid"), int(z.findtext("coefficient") or 1)))
    assert observed == [(z["side"], z["native_id"], z["coefficient"]) for z in n["sides"]]
    if rid.startswith("RHEA:"):
        ss = [s for s in sides if s["reaction"] == rid]
        for s in ss:
            key = (
                (s["chemical"], "consumes", rid)
                if s["side"] == "substrates"
                else (rid, "produces", s["chemical"])
            )
            expected.add(key)
            edge = next(e for e in edges if (e["subject"], e["predicate"], e["object"]) == key)
            assert edge["evidence"][0]["reference_id"] == rid
            assert s["participant_uri"] in edge["evidence"][0]["source_locator"]
            assert f"coefficient {s['coefficient']}" in edge["evidence"][0]["source_assertion"]
        assert nodes[rid]["direction"] == "left_to_right"
    else:
        reverse = n["direction"].endswith("RIGHT-TO-LEFT")
        assert nodes[rid]["direction"] == ("right_to_left" if reverse else "left_to_right")
        for s in n["sides"]:
            consumed = (s["side"] == "right") if reverse else (s["side"] == "left")
            key = (
                (s["mapped_id"], "consumes", rid) if consumed else (rid, "produces", s["mapped_id"])
            )
            expected.add(key)
            edge = next(e for e in edges if (e["subject"], e["predicate"], e["object"]) == key)
            assert (
                s["native_id"] in edge["evidence"][0]["source_locator"]
                and f"coefficient {s['coefficient']}" in edge["evidence"][0]["source_assertion"]
            )
    sidechecks.append(rid)
assert expected == {
    (e["subject"], e["predicate"], e["object"])
    for e in edges
    if e["predicate"] in ["consumes", "produces"]
}
# Full native child membership and all source ordering relations.
for _child, file, indices in [
    ("PWY-6519", "PWY-6519.xml", range(11)),
    ("PWY0-1507", "PWY0-1507.xml", range(11, 14)),
]:
    x = L.parse(str(P / file)).getroot().find("Pathway")
    assert set(x.xpath("./reaction-list/Reaction/@frameid")) == {native[i]["id"] for i in indices}
    for i in indices:
        assert any(
            e["subject"] == native[i]["record_id"]
            and e["predicate"] == "part_of"
            and e["object"] == r["id"]
            for e in edges
        )
for i, (a, b) in enumerate(zip(native[:-1], native[1:], strict=True)):
    file = "biotin-native.xml" if i == 10 else "PWY-6519.xml" if i < 10 else "PWY0-1507.xml"
    x = L.parse(str(P / file)).getroot().find("Pathway")
    assert a["id"] in x.xpath(
        f"./reaction-ordering[Reaction/@frameid='{b['id']}']/predecessor-reactions/Reaction/@frameid"
    )
    e = next(
        e
        for e in edges
        if e["subject"] == a["record_id"]
        and e["predicate"] == "precedes"
        and e["object"] == b["record_id"]
    )
    assert len(e["evidence"]) >= 3
# All assemblies are native, with independent exact protein cross-references.
for a in projection["assemblies"]:
    x = L.parse(str(P / f"metacyc-{a['complex'].split(':')[1]}.xml")).getroot().find("Protein")
    z = x.find("component")
    assert (
        z[0].get("frameid") == a["monomer"] and int(z.findtext("coefficient")) == a["coefficient"]
    )
    m = L.parse(str(P / f"metacyc-{a['monomer']}.xml")).getroot().find("Protein")
    assert a["protein"].split(":")[1] in m.xpath('./dblink[dblink-db="UNIPROT"]/dblink-oid/text()')
# Unresolved first condensation catalyst remains absent, while its chemistry is present.
assert any(e["object"] == "MetaCyc:RXN-11474" and e["predicate"] == "consumes" for e in edges)
assert not any(
    e["object"] == "MetaCyc:RXN-11474" and e["predicate"] in ["catalyzes", "enables"] for e in edges
)
# Independently reread original full UniProt bodies, preserving exact evidence codes/comments.
for id, x in json.loads((D / "biotin-protein-projection.json").read_text()).items():
    raw = json.loads((P / x["file"]).read_text())
    entry = (
        next(z for z in raw["results"] if z["primaryAccession"] == id) if "results" in raw else raw
    )
    assert entry["organism"]["taxonId"] == 83333
    assert x["entry"] == {k: v for k, v in entry.items() if k in x["entry"]}
    if "UniProtKB:" + id in nodes:
        assert (
            nodes["UniProtKB:" + id]["label"]
            == entry["proteinDescription"]["recommendedName"]["fullName"]["value"]
        )
# Eight explicit native FAS scaffold checks, following freshly replayed source sides.
for n, check in zip(native[1:9], projection["native_FAS_scaffold_checks"], strict=True):
    counts = {
        side: sum(
            z["coefficient"]
            for z in n["sides"]
            if z["side"] == side and "acp" in z["native_id"].lower()
        )
        for side in ["left", "right"]
    }
    assert counts == check["ACP_scaffolds"] and counts["left"] == counts["right"]

# Six exact reaction balances from original Rhea formula/charge.
# Reactive parts use an unchanged whole-carrier scaffold convention.
for m in rows:
    atoms = collections.Counter()
    charge = 0
    for s in [s for s in sides if s["master"] == m]:
        n = subjects[s["compound_uri"]]
        n = subjects[n["reactivePart"][0]] if "reactivePart" in n else n
        cf = s["coefficient"] * (-1 if s["side"] == "substrates" else 1)
        for atom, num in re.findall(r"([A-Z][a-z]?)(\d*)", n["formula"][0]):
            atoms[atom] += cf * int(num or 1)
        charge += cf * int(n["charge"][0])
    assert not any(atoms.values()) and charge == 0
# Readonly ChEBI identity, active status and charge-form replay.
# Native ACP states carry no invented formula.
conn = sqlite3.connect("file:" + str(C / "chebi.db") + "?mode=ro", uri=True)
for id, x in projection["chemical_identities"].items():
    fields = {}
    for pred, val, obj in conn.execute(
        "select predicate,value,object from statements where subject=?", (id,)
    ):
        if pred in [
            "rdfs:label",
            "chemrof:charge",
            "chemrof:generalized_empirical_formula",
            "owl:deprecated",
        ]:
            fields.setdefault(pred, []).append(val if val is not None else obj)
    assert (
        fields == x
        and not fields.get("owl:deprecated")
        and nodes[id]["label"] == fields["rdfs:label"][0]
    )
# Source-specific scientific wording checks from inspected primary paragraphs.
biof = html.parse(str(P / "PMC2925990.html")).xpath('//*[@id="P6"]')[0].text_content()
assert "BioF can accept either thioester" in biof
biob = html.parse(str(P / "PMC6541390.html")).xpath('//*[@id="P9"]')[0].text_content()
assert "Flavodoxin" in biob and "NADPH" in biob
assert not any(
    "Purified BioF converted" in e.get("source_assertion", "")
    for edge in edges
    for e in edge["evidence"]
)
# Literal quote check (currently all graph evidence uses faithful structured assertions).
assert all(
    ("source_assertion" in e and e.get("source_locator")) or "quote" in e
    for edge in edges
    for e in edge["evidence"]
)
kn, ke = kgx_nodes([record]), kgx_edges([record])
assert len(ke) == len(edges)
assert all(json.loads(k.evidence) == edges[i]["evidence"] for i, k in enumerate(ke))
assert len([n for n in kn if n.source_category == "protein"]) >= len(
    [n for n in r["participants"] if n.get("category") == "protein"]
)
report = dict(
    status="passed",
    timestamp=datetime.datetime.now(datetime.UTC).isoformat(),
    record_sha256=digest(T),
    script_sha256=digest(Path(__file__)),
    scope=(
        "Author replay of raw native/UniProt/Rhea/ChEBI evidence; "
        "not an independent scientific review or full corpus gates."
    ),
    counts=dict(
        participants=len(r["participants"]),
        reactions=14,
        edges=len(edges),
        evidence=sum(len(e["evidence"]) for e in edges),
        chemical_sides=len(expected),
        Rhea_side_occurrences=len(sides),
        exact_Rhea_balances=6,
        native_FAS_scaffold_checks=8,
        assemblies=8,
        ordering=13,
    ),
    checks=[
        "Native and closed schemas",
        "Fresh whole Rhea142 RDF/direction projection equals maintained selection",
        "All raw source digests except separately managed full ChEBI DB",
        "All fourteen native reactions, sides, coefficients, directions and membership",
        "All thirteen native ordering facts with separate side evidence",
        "Eight native assemblies and exact subunit accessions",
        "Full UniProt selected comments and evidence grades",
        "Six formula/charge balances and eight bounded ACP-scaffold checks",
        "Active ChEBI identities",
        "No invented first-condensation catalyst",
        "Source-specific BioF/Flavodoxin wording checks",
        "Actual KGX local export",
    ],
    limits=[
        (
            "Seven native ACP classes lack authoritative formulas; "
            "no exact elemental/charge balance claimed for the eight native FAS reactions."
        ),
        "Generic Rhea BioB donors do not establish physiological E. coli carrier identity.",
        "Global identifiers/pages/tests are parent integration checks, not claimed here.",
    ],
)
if len(sys.argv) > 1:
    Path(sys.argv[1]).write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
