import argparse
import csv
import gzip
import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as E
from pathlib import Path

parser = argparse.ArgumentParser(
    description=(
        "Replay deferred heme source facts; "
        "not a pathway validation or biological acceptance check."
    )
)
parser.add_argument(
    "--raw-root", type=Path, default=Path("/private/tmp/pathwaymech-next-186-evidence/heme")
)
parser.add_argument(
    "--authority-cache", type=Path, default=Path("/private/tmp/pathwaymech-curation-authorities")
)
parser.add_argument("--check-authority-hashes", action="store_true")
args = parser.parse_args()
rawdir = args.raw_root
cache = args.authority_cache
outdir = Path(__file__).resolve().parent


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1048576):
            h.update(block)
    return h.hexdigest()


manifest = json.loads((outdir / "heme-source-manifest.json").read_text())
checked = []
for entry in manifest["entries"]:
    source = (
        cache
        if entry["file"] in {"go.db", "chebi.db", "rhea.rdf.gz", "rhea-directions.tsv"}
        else rawdir
    ) / entry["file"]
    if source.name.endswith(".db") and not args.check_authority_hashes:
        continue
    assert digest(source) == entry["sha256"], source
    checked.append(str(source))


def save(n, x):
    expected = json.loads((outdir / n).read_text())
    assert x == expected, "Source projection mismatch: " + n


def original(n):
    return next(x for x in E.parse(rawdir / n).getroot() if x.tag != "metadata")


root = original("metacyc-PWY-7766.xml")


def attrs(x):
    return {
        "tag": x.tag,
        "attributes": dict(x.attrib),
        "text": x.text,
        "children": [attrs(c) for c in x],
    }


pathway = {
    "id": root.get("frameid"),
    "label": root.findtext("common-name"),
    "membership": [x.get("frameid") for x in root.findall("./reaction-list/Reaction")],
    "native_order": [attrs(x) for x in root.findall("reaction-ordering")],
    "pathway_links": [attrs(x) for x in root.findall("pathway-links")],
}
reactions = []
for i in pathway["membership"]:
    r = original("metacyc-" + i + ".xml")
    reactions.append(
        {
            "id": i,
            "directions": [x.text for x in r.findall("reaction-direction")],
            "sides": {side: [attrs(x) for x in r.findall(side)] for side in ["left", "right"]},
            "dblink": [attrs(x) for x in r.findall("dblink")],
            "enzymatic_reactions": [attrs(x) for x in r.findall("enzymatic-reaction")],
        }
    )
compounds = []
for i in ["CPD-17070", "CPD-21388", "PROTOHEME"]:
    r = original("metacyc-" + i + ".xml")
    compounds.append(
        {
            "id": i,
            "label": r.findtext("common-name"),
            "inchi": r.findtext("inchi"),
            "synonyms": [x.text for x in r.findall("synonym")],
            "dblink": [attrs(x) for x in r.findall("dblink")],
        }
    )
ns = {
    "rh": "http://rdf.rhea-db.org/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}
raw = gzip.decompress((cache / "rhea.rdf.gz").read_bytes()).decode()
starts = {}
for m in re.finditer(r'<rdf:Description rdf:about="([^"]+)">', raw):
    starts.setdefault(m[1], []).append(m.start())
wrapper = "<root " + " ".join(f'xmlns:{k}="{v}"' for k, v in ns.items()) + ">"
master_directed = {
    "19865": "19866",
    "43436": "43437",
    "49572": "49574",
    "57940": "57941",
    "57944": "57945",
    "56516": "56517",
}
directions = {
    r["RHEA_ID_MASTER"]: r
    for r in csv.DictReader((cache / "rhea-directions.tsv").open(), delimiter="\t")
    if r["RHEA_ID_MASTER"] in master_directed
}
wanted = {ns["rh"] + x for d in directions.values() for x in d.values()}
nodes = {}
while wanted:
    uri = wanted.pop()
    if uri in nodes or uri not in starts:
        continue
    props = {}
    for start in starts[uri]:
        end = raw.index("</rdf:Description>", start) + len("</rdf:Description>")
        node = E.fromstring(wrapper + raw[start:end] + "</root>")[0]
        for child in node:
            key = child.tag.split("}", 1)[1]
            val = child.get("{" + ns["rdf"] + "}resource") or child.text
            if val not in props.setdefault(key, []):
                props[key].append(val)
            if (
                key
                in {
                    "side",
                    "substrates",
                    "products",
                    "contains",
                    "compound",
                    "reactivePart",
                    "chebi",
                    "underlyingChebi",
                }
                and val
                and val.startswith(ns["rh"])
            ):
                wanted.add(val)
    nodes[uri] = props
projection = []
for master, directed in master_directed.items():
    row = {
        "master": "RHEA:" + master,
        "directed": "RHEA:" + directed,
        "direction": "right_to_left"
        if directions[master]["RHEA_ID_RL"] == directed
        else "left_to_right",
        "equation": nodes[ns["rh"] + directed]["equation"],
        "sides": {},
    }
    for side in ["substrates", "products"]:
        su = nodes[ns["rh"] + directed][side][0]
        entries = []
        for part in nodes[su]["contains"]:
            pn = nodes[part]
            co = pn["compound"][0]
            cn = nodes[co]
            terms = [
                k for k, v in nodes[su].items() if re.fullmatch(r"contains\d+", k) and part in v
            ]
            assert len(terms) == 1, (su, part, terms)
            coefficient = int(terms[0][8:])
            entries.append(
                {
                    "participant_uri": part,
                    "compound_uri": co,
                    "coefficient": coefficient,
                    "coefficient_predicate": terms[0],
                    "curie": cn["accession"][0],
                    "name": cn["name"][0],
                    "formula": cn["formula"][0],
                    "charge": int(cn["charge"][0]),
                }
            )
        row["sides"][side] = {"uri": su, "entries": entries}
    sums = {}
    for side in ["substrates", "products"]:
        counts = {"charge": 0}
        for en in row["sides"][side]["entries"]:
            for atom, num in re.findall(r"([A-Z][a-z]?)(\d*)", en["formula"]):
                counts[atom] = counts.get(atom, 0) + en["coefficient"] * int(num or 1)
            counts["charge"] += en["coefficient"] * en["charge"]
        sums[side] = counts
    row["balance"] = {
        "sums": sums,
        "passed": sums["substrates"] == sums["products"],
        "scope": "Source equation atom/charge consistency only; not physiological redox validity.",
    }
    projection.append(row)
# Scan all Rhea142 text properties, not only selected reaction IDs.
all_matches = []
for match in re.finditer(
    r'<rdf:Description rdf:about="([^"]+)">(.*?)</rdf:Description>', raw, re.S
):
    if re.search(r"coproheme|harderoheme|Fe-coproporphyrin|ferriheme", match[2], re.I):
        node = E.fromstring(wrapper + match[0] + "</root>")[0]
        selected = [
            {"predicate": x.tag.split("}", 1)[1], "value": x.text}
            for x in node
            if x.text
            and re.search(r"coproheme|harderoheme|Fe-coproporphyrin|ferriheme", x.text, re.I)
        ]
        if selected:
            all_matches.append({"uri": match[1], "matched_text_properties": selected})
chebi = sqlite3.connect("file:" + str(cache / "chebi.db") + "?mode=ro", uri=True)
chemids = sorted(
    {e["curie"] for r in projection for side in r["sides"].values() for e in side["entries"]}
    | {"CHEBI:60454", "CHEBI:55376", "CHEBI:36144", "CHEBI:17627"}
)
chemistry = {
    i: [
        {"predicate": p, "value": v, "object": o}
        for p, v, o in chebi.execute(
            "select predicate,value,object from statements where subject=? "
            "order by predicate,value,object",
            [i],
        )
    ]
    for i in chemids
}
go = sqlite3.connect("file:" + str(cache / "go.db") + "?mode=ro", uri=True)
gofacts = [
    {"predicate": p, "value": v, "object": o}
    for p, v, o in go.execute(
        "select predicate,value,object from statements where subject=? "
        "order by predicate,value,object",
        ["GO:0006785"],
    )
]
proteins = {}
for i in ["P32395", "P32396", "P32397", "P39645"]:
    d = json.load(open(rawdir / f"uniprot-{i}.json"))
    proteins[i] = {
        "organism": d["organism"],
        "genes": d["genes"],
        "proteinDescription": d["proteinDescription"],
        "comments": [
            {"source_locator": f"/comments/{j}", **x}
            for j, x in enumerate(d["comments"])
            if x["commentType"]
            in ["FUNCTION", "CATALYTIC ACTIVITY", "SUBUNIT", "COFACTOR", "SUBCELLULAR LOCATION"]
        ],
    }
save(
    "heme-source-projection.json",
    {
        "status": "deferred_research_not_maintained_graph",
        "pathway": pathway,
        "native_reactions": reactions,
        "native_iron_compounds": compounds,
        "rhea_directions": directions,
        "rhea_source_equations": projection,
        "chemical_authority": chemistry,
        "broad_GO_facts": gofacts,
        "proteins": proteins,
        "rhea142_all_text_redox_search": all_matches,
        "search_limits": (
            "Full Rhea142 RDF text properties and complete ChEBI255 statements "
            "value column searched; native MetaCyc object inspection limited "
            "to the exact pathway, five member reactions, net lead, three iron "
            "compounds and named enzyme frames. No universal absence assertion."
        ),
    },
)
assert all(row["balance"]["passed"] for row in projection)
assert len(pathway["membership"]) == 5
assert all("/q;+2/" in item["inchi"] for item in compounds)
# Replay the exact primary statement, not the author's paraphrase.
primary = E.parse(rawdir / "primary-2016-bioc.xml")
passage = next(x for x in primary.findall(".//passage") if x.findtext("offset") == "4273")
assert "the coproheme decarboxylase yields ferric heme b." in passage.findtext("text")
assert "Staphylococcus aureus" in passage.findtext("text")
# Native source labels do not create a ferric-state identity.
for curie in ["CHEBI:68438", "CHEBI:142463", "CHEBI:60344"]:
    assert any(
        x["predicate"] == "chemrof:inchi_string" and "/q;+2/" in (x["value"] or "")
        for x in chemistry[curie]
    )
# Repeat complete pinned ChEBI statement-value search, including synonym/annotation rows.
searched = chebi.execute(
    "select distinct subject,predicate,value from statements "
    "where value like '%coproporphyrin%' or value like '%harderopor%' "
    "or value like '%harderoheme%'"
).fetchall()
assert sorted([list(x) for x in searched]) == sorted(
    json.loads((rawdir / "chebi-expanded-redox-search.json").read_text())
)
assert not (outdir.parents[2] / "data/pathways/heme-b-biosynthesis-iv.yaml").exists()
print(
    json.dumps(
        {
            "status": "passed",
            "source_hashes_checked": len(checked),
            "authority_hashes_rechecked": args.check_authority_hashes,
            "biological_disposition": (
                "deferred; balanced source chemistry does not resolve iron-state conflict"
            ),
        },
        indent=2,
    )
)
print(
    json.dumps(
        {
            "native_membership": pathway["membership"],
            "rhea_projection_count": len(projection),
            "source_balances_pass": [r["directed"] for r in projection if r["balance"]["passed"]],
            "rhea142_text_matches": len(all_matches),
            "chebi_ids": len(chemids),
        },
        indent=2,
    )
)
