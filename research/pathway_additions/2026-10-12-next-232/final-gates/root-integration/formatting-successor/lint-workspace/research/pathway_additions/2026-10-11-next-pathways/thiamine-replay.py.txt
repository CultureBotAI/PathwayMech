"""Replay the complete thiamine source projection; writes external scratch only.
Run with the worktree Python from its root. Full gates belong to integration.
"""

import collections
import csv
import datetime
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as E
from pathlib import Path

import yaml
from lxml import html

from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

P = Path("/private/tmp/pathwaymech-next-pathways-evidence/thiamine")
C = Path("/private/tmp/pathwaymech-curation-authorities")
masters = {"17457", "43344", "43340", "26297", "26361", "12605", "24840", "19893", "47844", "15913"}
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
    {s["chemical"] for s in sides} | {"CHEBI:49883", "CHEBI:29105", "CHEBI:18420", "CHEBI:597326"}
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
                "Rhea exact small molecules plus reactive-part formulas "
                "for whole protein carriers; "
                "fixed carrier backbones cancel, not isolated-fragment graph nodes."
            ),
        )
    )
replayed = dict(directions=rows, nodes=subjects, sides=sides, identities=chem, balances=balances)
print(
    "directions",
    len(rows),
    "side occurrences",
    len(sides),
    "chemical and carrier nodes",
    len(chem),
    "balances",
    len(balances),
)


ROOT = Path.cwd()
D = ROOT / "research/pathway_additions/2026-10-11-next-pathways"
Y = ROOT / "data/pathways/thiamine-diphosphate-biosynthesis-i.yaml"


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


y = yaml.safe_load(Y.read_text())
validate_record(y)
assert strict_errors([Y], ROOT) == []
projection = json.loads((D / "thiamine-source-projection.json").read_text())
for key, value in replayed.items():
    assert projection[key] == value, key
checks = []
manifest = json.loads((D / "thiamine-source-manifest.json").read_text())
for entry in manifest["artifacts"]:
    if "sha256" not in entry:
        continue
    path = P / entry["file"]
    assert digest(path) == entry["sha256"], path
    checks.append(dict(file=str(path), sha256=entry["sha256"]))
for entry in manifest["pinned_authorities"]:
    assert digest(entry["path"]) == entry["sha256"], entry["path"]
    checks.append(dict(file=entry["path"], sha256=entry["sha256"]))
# Exact chosen native boundary; PathBank predecessor has a different boundary.
for identifier, expected in {
    "THISYN-PWY": {"PWY-6890", "PWY-6892", "PWY-6894"},
    "PWY-6890": {"PYRIMSYN1-RXN", "PYRIMSYN3-RXN"},
    "PWY-6892": {
        "RXN0-308",
        "RXN-14382",
        "RXN-11319",
        "RXN-9789",
        "RXN-9788",
        "DXS-RXN",
        "THIAZOLSYN2-RXN",
    },
    "PWY-6894": {"RXN-12611", "THI-P-KIN-RXN"},
}.items():
    root = E.parse(P / ("metacyc-" + identifier + ".xml")).getroot()
    assert root.get("ptools-version") == "22.5"
    node = next(x for x in root if x.get("frameid") == identifier)
    assert {x.get("frameid") for x in node.findall("reaction-list/*")} == expected
    assert set(projection["native_pathway"][identifier]) == expected
native = {x.get(rdf + "ID", x.get(rdf + "about")): x for x in E.parse(P / "PW002028.owl").getroot()}
bp = "{http://www.biopax.org/release/biopax-level3.owl#}"
pathway = native["http://identifiers.org/smpdb/SMP0002042"]
assert {
    x.get(rdf + "resource")
    for x in pathway.findall(bp + "pathwayComponent")
    if x.get(rdf + "resource", "").startswith("#Reactions/")
} == {
    "#Reactions/" + i
    for i in ["3410", "3411", "5930", "3412", "3413", "3414", "5931", "5932", "5933", "5934"]
}
expected = collections.Counter(
    (s["chemical"], "consumes", s["reaction"])
    if s["side"] == "substrates"
    else (s["reaction"], "produces", s["chemical"])
    for s in sides
)
actual = collections.Counter(
    (e["subject"], e["predicate"], e["object"])
    for e in y["mechanistic_edges"]
    if e["predicate"] in ["consumes", "produces"]
)
assert actual == expected and len(sides) == 59
for s in sides:
    edge = next(
        e
        for e in y["mechanistic_edges"]
        if (e["subject"], e["predicate"], e["object"])
        == (
            (s["chemical"], "consumes", s["reaction"])
            if s["side"] == "substrates"
            else (s["reaction"], "produces", s["chemical"])
        )
    )
    assert "Coefficient " + str(s["coefficient"]) + " " in edge["description"]
    assert edge["evidence"][0]["reference_id"] == "RHEA:" + s["master"]
for node in y["participants"]:
    i = node["id"]
    if i in chem:
        assert node["label"] == (
            chem[i]["rdfs:label"][0] if i.startswith("CHEBI:") else chem[i]["name"][0]
        )
    if i.startswith("UniProtKB:"):
        u = json.loads((P / ("uniprot-" + i.split(":")[1] + ".json")).read_text())
        assert u["organism"]["taxonId"] == 83333
        assert node["label"] == u["proteinDescription"]["recommendedName"]["fullName"]["value"]
for node in y["reactions"]:
    num = node["id"].split(":")[1]
    assert node["label"] == subjects[B + num]["equation"][0]
    assert node["direction"] == "left_to_right"
    assert node["category"] == "molecular_activity"
# Every reference digest maps to the actual inspected body; quote text is literal.
byhash = {a["sha256"]: P / a["file"] for a in manifest["artifacts"] if "sha256" in a}
byhash.update({a["sha256"]: Path(a["path"]) for a in manifest["pinned_authorities"]})
references = {r["id"]: r for r in y["references"]}
quote_checks = []
for ref in references.values():
    assert ref["source_sha256"] in byhash, ref
for edge in y["mechanistic_edges"]:
    for evidence in edge["evidence"]:
        ref = references[evidence["reference_id"]]
        path = byhash[ref["source_sha256"]]
        if "quote" in evidence:
            if path.suffix == ".html":
                body = " ".join(html.parse(str(path)).xpath("//article")[0].text_content().split())
            else:
                body = E.parse(path).findtext(".//abstractText") or ""
            assert evidence["quote"] in body, (edge["id"], path)
            quote_checks.append(
                dict(
                    edge=edge["id"], reference_id=ref["id"], quote=evidence["quote"], file=str(path)
                )
            )
        if "source_assertion" in evidence:
            assert evidence["source_locator"]
# Issue 338: keep structured cofactor annotation and primary interpretation separate.
zinc = next(e for e in y["mechanistic_edges"] if e["id"] == "thiamine-edge-087")
assert [e["reference_id"] for e in zinc["evidence"]] == ["UniProtKB:P30138", "PMID:16388576"]
assert "structural" not in zinc["evidence"][0]["source_assertion"]
assert zinc["evidence"][0]["source_locator"] == "comments[commentType='COFACTOR']"
assert zinc["evidence"][1]["source_locator"] == (
    "Results, ThiF active site, paragraph P21 (PMC2566941 section S11)."
)
zinc_primary = html.parse(str(P / "PMC2566941.html")).getroot().get_element_by_id("P21")
assert zinc_primary.getparent().get("id") == "S11"
assert "more then 20 Å from the active site" in zinc_primary.text_content()
assert "most likely has a structural rather than a catalytic role" in zinc_primary.text_content()
zinc_uniprot = json.loads((P / "uniprot-P30138.json").read_text())
zinc_comment = next(c for c in zinc_uniprot["comments"] if c["commentType"] == "COFACTOR")
assert zinc_comment["note"]["texts"][0]["value"] == "Binds 1 zinc ion per subunit."
assert zinc_comment["cofactors"][0]["cofactorCrossReference"]["id"] == "CHEBI:29105"
# These source-specific safeguards prevent a convenient partial route or double count.
assert len(y["reactions"]) == 10 and len(y["mechanistic_edges"]) == 92
assert {x["id"] for x in y["participants"] if x["id"].startswith("RHEA-COMP:")} == {
    "RHEA-COMP:" + i for i in ["12157", "12158", "12909", "12910", "19908"]
}
assert not {"MetaCyc:RXN-14382", "MetaCyc:RXN-9788"} & {x["id"] for x in y["reactions"]}
assert not {"UniProtKB:P0A6B9", "UniProtKB:P0AMX5"} & {x["id"] for x in y["participants"]}
assert len(projection["native_projection"]) == 11
out = dict(
    checked_at=datetime.datetime.now(datetime.UTC).isoformat(),
    target=str(Y),
    target_sha256=digest(Y),
    native_schema="pass",
    closed_schema="pass",
    full_native_reaction_count=11,
    maintained_reaction_count=10,
    side_occurrences=len(sides),
    balance_checks=balances,
    source_body_checks=checks,
    literal_quote_checks=quote_checks,
    participants=len(y["participants"]),
    edges=len(y["mechanistic_edges"]),
    evidence=sum(len(e["evidence"]) for e in y["mechanistic_edges"]),
    references=len(y["references"]),
    limits=[
        "Mechanistic prose and source inference grades require independent scientific review.",
        (
            "Full corpus, canonical shared identity snapshots, pages and KGX "
            "are integration gates and were not run here."
        ),
        (
            "Carrier formula balance uses exact reactive parts "
            "while the graph retains whole protein states."
        ),
    ],
)
(P / "author-replay-result.json").write_text(json.dumps(out, indent=2) + "\n")
print(
    json.dumps(
        {
            k: v
            for k, v in out.items()
            if k not in ["balance_checks", "source_body_checks", "literal_quote_checks"]
        },
        indent=2,
    )
)
