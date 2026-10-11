"""Replay the complete ADP-heptose source projection; write external scratch only."""

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
import zipfile
from pathlib import Path

import yaml
from lxml import etree as L
from lxml import html

from pathwaymech.kgx import kgx_edges, kgx_nodes
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

P = Path("/private/tmp/pathwaymech-nicotine-next-evidence/adhp")
C = Path("/private/tmp/pathwaymech-curation-authorities")
masters = {"27489", "27473", "28518", "27465", "17577"}
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
chem = {}
conn = sqlite3.connect("file:" + str(C / "chebi.db") + "?mode=ro", uri=True)
for curie in sorted(
    {s["chemical"] for s in sides}
    | {"CHEBI:29105", "CHEBI:18420", "CHEBI:29035", "CHEBI:48828", "CHEBI:58349", "CHEBI:57540"}
):
    if curie.startswith("CHEBI:"):
        fields = {}
        for pred, val, obj in conn.execute(
            "select predicate,value,object from statements where subject=?", (curie,)
        ):
            if pred in [
                "rdfs:label",
                "chemrof:charge",
                "chemrof:generalized_empirical_formula",
                "owl:deprecated",
            ]:
                fields.setdefault(pred, []).append(val if val is not None else obj)
        chem[curie] = fields
    else:
        chem[curie] = subjects[B + "Compound_" + curie.split(":")[1]]
balances = []
for m, r in rows.items():
    atoms = collections.Counter()
    charge = 0
    for s in [s for s in sides if s["master"] == m]:
        node = subjects[s["compound_uri"]]
        if "reactivePart" in node:
            node = subjects[node["reactivePart"][0]]
        form = node["formula"][0]
        sgn = -1 if s["side"] == "substrates" else 1
        coeff = sgn * s["coefficient"]
        parts = re.findall(r"([A-Z][a-z]?)(\d*)", form)
        assert "".join(a + b for a, b in parts) == form, form
        for a, b in parts:
            atoms[a] += coeff * int(b or 1)
        charge += coeff * int(node["charge"][0])
    assert all(v == 0 for v in atoms.values()) and charge == 0, (m, atoms, charge)
    balances.append(
        dict(
            reaction="RHEA:" + r["RHEA_ID_LR"],
            atom_or_R_group_delta=dict(atoms),
            charge_delta=charge,
            scope=(
                "All selected Rhea participants are fully defined small molecules. "
                "Element and formal-charge totals are computed from the exact source "
                "formulas and coefficients."
            ),
        )
    )
replayed = dict(directions=rows, nodes=subjects, sides=sides, identities=chem, balances=balances)

D = Path("research/pathway_additions/2026-10-11-nicotine-next")
T = Path("data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml")


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


maintained = json.loads((D / "adhp-chemistry-projection.json").read_text())
assert replayed == maintained, "Fresh full-RDF replay differs from maintained projection"
document = yaml.safe_load(T.read_text())
record = validate_record(document)
errors = strict_errors([T], Path.cwd())
assert not errors, errors
assert len(sides) == 19 and len(rows) == 5
actual_side_edges = [
    e for e in document["mechanistic_edges"] if e["predicate"] in {"consumes", "produces"}
]
expected = {
    (s["chemical"], "consumes", s["reaction"])
    if s["side"] == "substrates"
    else (s["reaction"], "produces", s["chemical"])
    for s in sides
}
assert {(e["subject"], e["predicate"], e["object"]) for e in actual_side_edges} == expected
for side in sides:
    e = next(
        e
        for e in actual_side_edges
        if (e["subject"] == side["chemical"] and e["object"] == side["reaction"])
        or (e["object"] == side["chemical"] and e["subject"] == side["reaction"])
    )
    assert f"coefficient {side['coefficient']}" in e["evidence"][0]["source_assertion"]
    assert side["participant_uri"] in e["evidence"][0]["source_locator"]
    assert side["compound_uri"] in e["evidence"][0]["source_locator"]
    assert e["evidence"][0]["reference_id"] == side["reaction"]
for n in document["participants"]:
    if n["id"].startswith("CHEBI:"):
        assert n["label"] == chem[n["id"]]["rdfs:label"][0]
        assert "owl:deprecated" not in chem[n["id"]]
for n in document["reactions"]:
    assert n["direction"] == "left_to_right"
    assert n["label"] == subjects[B + n["id"].split(":")[1]]["label"][0]
order = [
    ("RXN0-4301", "27490", "P63224", "CPLX0-7660", "G6106-MONOMER", 4),
    ("RXN0-4341", "27474", "P76658", "CPLX0-3661", "G7590-MONOMER", 2),
    ("RXN0-4361", "28519", "P63228", None, "EG11736-MONOMER", 1),
    ("RXN0-4342", "27466", "P76658", "CPLX0-3661", "G7590-MONOMER", 2),
    ("5.1.3.20-RXN", "17578", "P67910", "CPLX0-3681", "EG10838-MONOMER", 5),
]
path = L.parse(str(P / "metacyc-PWY0-1241.xml")).xpath('//*[@frameid="PWY0-1241"]')[0]
assert set(path.xpath("./reaction-list/Reaction/@frameid")) == {o[0] for o in order}
assert len(path.findall("reaction-ordering")) == 4
for index, (native, rx, protein, complex_id, monomer, coefficient) in enumerate(order):
    nr = L.parse(str(P / f"metacyc-{native}.xml")).xpath(f'//*[@frameid="{native}"]')[0]
    assert nr.xpath('./dblink[dblink-db="RHEA"]/dblink-oid/text()') == [rx]
    assert path.xpath(f'./reaction-layout[Reaction/@frameid="{native}"]/direction/text()') == [
        "L2R"
    ]
    if index:
        assert path.xpath(
            f'./reaction-ordering[Reaction/@frameid="{native}"]/predecessor-reactions/Reaction/@frameid'
        ) == [order[index - 1][0]]
    mon = L.parse(str(P / f"metacyc-{monomer}.xml")).xpath(f'//*[@frameid="{monomer}"]')[0]
    assert mon.xpath('./dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [protein]
    up = json.loads((P / f"uniprot-{protein}.json").read_text())
    assert up["primaryAccession"] == protein and up["organism"]["taxonId"] == 83333
    master = next(m for m, row in rows.items() if row["RHEA_ID_LR"] == rx)
    assert any(
        c["commentType"] == "CATALYTIC ACTIVITY"
        and any(x["id"] == "RHEA:" + master for x in c["reaction"]["reactionCrossReferences"])
        for c in up["comments"]
    )
    if complex_id:
        cp = L.parse(str(P / f"metacyc-{complex_id}.xml")).xpath(f'//*[@frameid="{complex_id}"]')[0]
        assert cp.xpath("./component/Protein/@frameid") == [monomer]
        assert cp.xpath("./component/coefficient/text()") == [str(coefficient)]
        assert native in cp.xpath("./catalyzes/Enzymatic-Reaction/reaction/Reaction/@frameid")
        assert cp.xpath("./species/Organism/@frameid") == ["TAX-511145"]
with zipfile.ZipFile(
    "/private/tmp/pathwaymech-pathbank-dbcan-evidence/pathbank/pathbank_primary_biopax.zip"
) as archive:
    assert archive.read("PW002095.owl") == (P / "PW002095.owl").read_bytes()
projection = json.loads((D / "adhp-native-projection.json").read_text())
assert len(projection["pathbank_objects"]) == 147
member = projection["pathbank_objects"]["http://identifiers.org/smpdb/SMP0002107"]["properties"][
    "pathwayComponent"
]
assert {m for m in member if m.startswith("#Reactions/")} == {
    f"#Reactions/{i}" for i in range(6111, 6116)
}
source_manifest = json.loads((D / "adhp-source-manifest.json").read_text())
source_results = []
for artifact in source_manifest["artifacts"]:
    path_ = Path(artifact["external_path"])
    if "sha256" in artifact and path_.exists():
        got = digest(path_)
        assert got == artifact["sha256"], (path_, got, artifact["sha256"])
        source_results.append({"path": str(path_), "sha256": got})
for reference in document["references"]:
    assert any(reference["source_sha256"] == item["sha256"] for item in source_results), reference[
        "id"
    ]
q = json.loads((P / "uniprot-Q643R3.json").read_text())
assert q["organism"]["taxonId"] == 9606
assert "LPCAT4" in str(q["proteinDescription"])
quotes = [
    ("16030223", "the HldE functional unit is a dimer"),
    ("10896473", "AGME is a homopentameric enzyme"),
]
for pmid, quote in quotes:
    abstract = L.parse(str(P / f"PMID{pmid}-core.xml")).findtext(".//abstractText")
    assert quote in abstract
    assert quote in (D / "adhp-curation.md").read_text()
# Exact primary evidence locators and diagnostic phrases used by curated assertions.
bio = L.parse(str(P / "PMC2844806-bioc.xml"))
passages = {int(x.findtext("offset")): x.findtext("text", "") for x in bio.findall(".//passage")}
assert "does not interact with the substrate" in passages[20251]
assert "remains undefined" in passages[23631]
assert "Mg2+" in passages[15508]
for fn, paragraph, needle in [
    ("PMC139585.html", 19, "A. thermoaerophilus GmhA"),
    ("PMC139585.html", 23, "Synthetic"),
    ("PMC2844805.html", 43, "C(7)phosphate"),
]:
    paras = html.parse(str(P / fn)).xpath("//article//p")
    assert needle in paras[paragraph - 1].text_content()
kn, ke = kgx_nodes([record]), kgx_edges([record])
assert len(kn) == 33 and len(ke) == 43
assert all(
    len(json.loads(k.evidence)) == len(document["mechanistic_edges"][i]["evidence"])
    for i, k in enumerate(ke)
)
report = {
    "checked_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(T),
    "target_sha256": digest(T),
    "replay_script_sha256": digest(Path(__file__)),
    "native_schema": "pass",
    "closed_schema": "pass",
    "full_rdf_fresh_projection": "pass",
    "native_pathway_reactions": 5,
    "native_predecessor_links": 4,
    "reaction_side_occurrences": 19,
    "balance_checks": balances,
    "native_uniprot_bridges": 4,
    "native_assemblies": 3,
    "kgx_local_nodes": len(kn),
    "kgx_local_edges": len(ke),
    "evidence_count": sum(len(e["evidence"]) for e in document["mechanistic_edges"]),
    "literal_primary_excerpt_checks": len(quotes),
    "source_hash_checks": source_results,
    "owned_inputs": [
        {"path": str(f), "sha256": digest(f)}
        for f in sorted(D.glob("adhp-*"))
        if f.name != "adhp-validation.json"
    ],
    "limits": (
        "Author source and narrow schema replay only. No independent scientific review, "
        "corpus tests or generated-page claim. Source paths are external, and failed "
        "full-text attempts do not become evidence."
    ),
}
out = Path(sys.argv[1]) if len(sys.argv) > 1 else P / "author-replay.json"
out.write_text(json.dumps(report, indent=2) + "\n")
print(
    json.dumps(
        {
            k: report[k]
            for k in [
                "target_sha256",
                "native_schema",
                "closed_schema",
                "reaction_side_occurrences",
                "kgx_local_nodes",
                "kgx_local_edges",
                "evidence_count",
            ]
        }
    )
)
