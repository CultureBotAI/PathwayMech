"""Offline original-source author replay. Pending adapters are reported, never waived."""

from __future__ import annotations

import collections
import copy
import csv
import hashlib
import json
import re
import sqlite3
import tarfile
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import etree as E

from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import PathwayRecord, ValidationError, validate_record
from pathwaymech.strict import strict_errors

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
SCOUT = Path("/private/tmp/pathwaymech-bacillibactin-scout-20261011")
REPO = Path("/private/tmp/pathwaymech-next-210-20261011")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = OUT / "bacillibactin-biosynthesis.yaml"
STEPS = [
    "ISOCHORSYN-RXN",
    "ISOCHORMAT-RXN",
    "DHBDEHYD-RXN",
    "DHBAMPLIG-RXN",
    "RXN-19449",
    "RXN-9376",
    "RXN-19458",
    "RXN-19460",
    "RXN-9377",
    "RXN-19452",
    "RXN-19461",
    "RXN-19462",
]
OLD_CARRIER = "DHB-glycyl-arginyl-DhbF"
MNX = "metanetx.chemical:MNXM743865"


def digest(p):
    with Path(p).open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def load(p):
    return json.loads(Path(p).read_text())


def native(n):
    path = ROOT / "originals" / (n + ".xml")
    if not path.exists():
        path = SCOUT / (n + ".xml")
    root = E.parse(str(path)).getroot()
    assert root.get("ptools-version") == "22.5"
    x = next(x for x in root if x.tag != "metadata")
    assert x.get("frameid") == n and x.get("orgid") == "META"
    return x


def sides(n):
    return {
        s: {
            next(x for x in slot if x.get("frameid")).get("frameid"): int(
                slot.findtext("coefficient") or "1"
            )
            for slot in native(n).findall(s)
        }
        for s in ["left", "right"]
    }


def formula(n):
    m = native(n).find("cml/molecule")
    assert m is not None, "No whole native formula for " + n
    f = m.find("formula").get("concise").split()
    out = dict(zip(f[::2], map(int, f[1::2]), strict=True))
    out["charge"] = int(m.get("formalCharge"))
    return out


def combine(*terms):
    out = collections.Counter()
    for coeff, f in terms:
        for k, v in f.items():
            out[k] += coeff * v
    return dict(out)


def balance(s, classes=None):
    terms = []
    for side, entries in s.items():
        for n, coeff in entries.items():
            f = classes[n] if classes and n in classes else formula(n)
            terms.append(((-1 if side == "left" else 1) * coeff, f))
    return {k: v for k, v in combine(*terms).items() if v}


def guard(doc, projection):
    assert {r["id"] for r in doc["reactions"]} == {"MetaCyc:" + n for n in STEPS}
    assert not any(x["id"] == "MetaCyc:" + OLD_CARRIER for x in doc["participants"])
    terminal = next(x for x in doc["participants"] if x["id"] == MNX)
    assert "L-threonyl" in terminal["label"] and "arginyl" not in terminal["label"]
    assert terminal["category"] == "chemical_entity"
    assert projection["whole_polypeptide_balance_claimed"] is False
    assert projection["selected_native_to_graph"][OLD_CARRIER] == MNX
    selected = [e for e in doc["mechanistic_edges"] if e["object"] == MNX]
    assert len(selected) == 2
    for e in selected:
        assert {"PMID:39870587", MNX} <= {x["reference_id"] for x in e["evidence"]}
        assert "not native-equation equivalence" in e["evidence"][0]["source_assertion"]
        assert "not whole DhbF polypeptides" in e["description"]
    assert "nine ATP per trimer" in doc["description"]
    assert "not a measured ATP/product ratio" in doc["description"]
    assert "upstream DhbA/C/B activities are genome and cluster annotations" in doc["description"]


def reject(fn):
    try:
        fn()
    except AssertionError:
        return True
    raise AssertionError("Malformed biological claim unexpectedly accepted")


def main():
    start = datetime.now(UTC).isoformat()
    doc = yaml.safe_load(TARGET.read_text())
    projection = load(OUT / "bacillibactin-source-projection.json")
    manifest = load(OUT / "bacillibactin-source-manifest.json")
    assert projection["record_sha256"] == manifest["record_sha256"] == digest(TARGET)
    checked = {}
    for x in manifest["original_sources"]:
        checked[x["original_path"]] = digest(x["original_path"])
        assert checked[x["original_path"]] == x["sha256"], x["original_path"]
        if "original_container" in x:
            archive = x["original_container"]
            assert digest(archive["container_path"]) == archive["container_sha256"]
            with tarfile.open(archive["container_path"]) as bundle:
                assert (
                    bundle.extractfile(archive["member"]).read()
                    == Path(x["original_path"]).read_bytes()
                )
    for ref in doc["references"]:
        assert len(ref["title"]) < 350
        assert ref["source_sha256"] == checked[manifest["reference_original_paths"][ref["id"]]]
    authorities = load(OUT / "bacillibactin-authority-inputs.json")
    native_labels = {x["id"]: x["label"] for x in authorities["native_identity_inspection"]}
    assert native_labels[doc["id"]] == doc["label"]
    for participant in doc["participants"]:
        if participant["id"].startswith("MetaCyc:"):
            assert native_labels[participant["id"]] == participant["label"]
    assert projection["graph_to_source"] == [
        {
            "edge_id": e["id"],
            "subject": e["subject"],
            "predicate": e["predicate"],
            "object": e["object"],
            "evidence": e["evidence"],
        }
        for e in doc["mechanistic_edges"]
    ]
    guard(doc, projection)
    bad = copy.deepcopy(doc)
    next(x for x in bad["participants"] if x["id"] == MNX)["label"] = "an L-arginyl carrier"
    assert reject(lambda: guard(bad, projection))
    bad = copy.deepcopy(doc)
    bad["reactions"].append({"id": "MetaCyc:RXN-9374", "label": "six-ATP composite"})
    assert reject(lambda: guard(bad, projection))
    badp = copy.deepcopy(projection)
    badp["whole_polypeptide_balance_claimed"] = True
    assert reject(lambda: guard(doc, badp))
    # Original boundary is twelve native transformations, not twelve selected rows in a dossier.
    assert set(native("PWY-5903").xpath("reaction-list/Reaction/@frameid")) == set(STEPS[3:])
    assert native("PWY-5903").xpath("reaction-list/Pathway/@frameid") == ["PWY-5901"]
    assert set(native("PWY-5901").xpath("reaction-list/Reaction/@frameid")) == set(STEPS[:3])
    chemmap = projection["selected_native_to_graph"]
    graph_sides = [
        e for e in doc["mechanistic_edges"] if e["predicate"] in {"has_input", "has_output"}
    ]
    source_count = 0
    exact_balances = []
    for n in STEPS:
        s = sides(n)
        for side, entries in s.items():
            pred = "has_input" if side == "left" else "has_output"
            for native_id, coeff in entries.items():
                source_count += 1
                edges = [
                    e
                    for e in graph_sides
                    if e["subject"] == "MetaCyc:" + n
                    and e["predicate"] == pred
                    and e["object"] == chemmap[native_id]
                ]
                assert len(edges) == 1, (n, side, native_id)
                e = edges[0]
                assert e["description"].startswith(f"Coefficient {coeff}.")
                assert e["evidence"][0]["reference_id"] == "MetaCyc:" + n
                assert native_id in e["evidence"][0]["source_assertion"]
                assert f"coefficient {coeff}" in e["evidence"][0]["source_assertion"]
                assert side in e["evidence"][0]["source_locator"]
        if n in STEPS[:4] + ["RXN-9376", "RXN-9377"]:
            residual = balance(s)
            assert not residual, (n, residual)
            exact_balances.append(
                {
                    "reaction": n,
                    "residual": residual,
                    "scope": "exact original native CML atoms and charge",
                }
            )
        assert projection["native_reactions"][n]["direction"] == native(n).findtext(
            "reaction-direction"
        )
    assert source_count == len(graph_sides)
    # Conditional reactive-part bookkeeping; source classes do not supply full protein formulas.
    # Common holo carrier scaffold comes from independent thioester-cleavage replay of original MNX.
    carrier = load(OUT / "bacillibactin-carrier-replay.json")
    assert carrier["original_sha256"] == checked[carrier["original_path"]]
    assert carrier["script_sha256"] == digest(OUT / "bacillibactin-carrier-replay.py")
    assert carrier["native_charge"] == -1
    assert (carrier["threonine_alpha_CIP"], carrier["threonine_beta_CIP"]) == ("S", "R")
    assert carrier["derived_holo_fragment_formula"] == "C14H25*2N3O8PS-"
    holo = {"C": 14, "H": 25, "N": 3, "O": 8, "P": 1, "S": 1, "*": 2, "charge": -1}
    cls = {"Holo-DhbB": holo, "DhbF": holo}
    cls["23-dihydroxybenzoyl-DhbB"] = combine(
        (1, holo), (1, formula("CPD-62")), (-1, formula("AMP")), (-1, formula("PROTON"))
    )
    cls["Glycyl-DhbF"] = combine((1, holo), (1, formula("CPD-9993")), (-1, formula("AMP")))
    cls["DHB-glycyl-DhbF"] = combine(
        (1, cls["23-dihydroxybenzoyl-DhbB"]),
        (1, cls["Glycyl-DhbF"]),
        (-1, holo),
        (-1, formula("PROTON")),
    )
    cls["Threonyl-DhbF"] = combine(
        (1, holo), (1, formula("CPD-9994")), (-1, formula("AMP")), (-1, formula("PROTON"))
    )
    # The terminal class has an independently issued structural formula, not a formula inferred
    # solely by forcing the old reaction to balance. The old name remains rejected.
    cls[OLD_CARRIER] = {"C": 27, "H": 39, "N": 5, "O": 14, "P": 1, "S": 1, "*": 2, "charge": -1}
    conditional = []
    for n in STEPS:
        if n not in [x["reaction"] for x in exact_balances]:
            residual = balance(sides(n), cls)
            assert not residual, (n, residual)
            conditional.append(
                {
                    "reaction": n,
                    "residual": residual,
                    "scope": "conditional common Ppant-carrier reactive scaffold; "
                    "not independently observed class formula or whole protein balance",
                }
            )
    weighted = collections.Counter()
    for n in STEPS[3:]:
        mult = 1 if n == "RXN-19462" else 3
        for side, entries in sides(n).items():
            for name, count in entries.items():
                weighted[name] += (-1 if side == "left" else 1) * mult * count
    weighted = {k: v for k, v in weighted.items() if v}
    expected = {
        "2-3-DIHYDROXYBENZOATE": -3,
        "GLY": -3,
        "THR": -3,
        "ATP": -9,
        "CPD-9984": 1,
        "AMP": 9,
        "PPI": 9,
        "PROTON": 6,
    }
    assert weighted == expected, weighted
    assert not balance(
        {
            "left": {k: -v for k, v in weighted.items() if v < 0},
            "right": {k: v for k, v in weighted.items() if v > 0},
        }
    )
    full_net = collections.Counter(weighted)
    for n in STEPS[:3]:
        for side, entries in sides(n).items():
            for name, count in entries.items():
                full_net[name] += (-1 if side == "left" else 1) * 3 * count
    full_net = {k: v for k, v in full_net.items() if v}
    assert not balance(
        {
            "left": {k: -v for k, v in full_net.items() if v < 0},
            "right": {k: v for k, v in full_net.items() if v > 0},
        }
    )
    assert sides("RXN-9374")["left"]["ATP"] == 6
    # Ionic bridge is an exact original InChI comparison, not a database xref alone.
    bridges = []
    with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as c:
        for n in ["ATP", "AMP", "NADH"]:
            cid = chemmap[n]
            term = dict(
                c.execute(
                    "select predicate,value from statements where subject=? and value is not null",
                    [cid],
                )
            )
            assert native(n).findtext("inchi") == term["chemrof:inchi_string"], n
            f = formula(n)
            assert f["charge"] == int(term["chemrof:charge"])
            assert (
                next(x["label"] for x in doc["participants"] if x["id"] == cid)
                == term["rdfs:label"]
            )
            bridges.append(
                {"native": n, "selected": cid, "exact_inchi": True, "charge": f["charge"]}
            )
    # Original NCBI taxonomy, source proteins, and independent ENA chromosome translation.
    tax = E.parse(str(ROOT / "originals/taxon2916802.xml"))
    assert tax.findtext("Taxon/TaxId") == "2916802"
    assert tax.findtext("Taxon/ScientificName") == doc["taxa"][0]["label"]
    proteins = E.parse(str(SCOUT / "followup/ncbi-kh34-proteins.xml")).findall("GBSeq")
    chromosome = (SCOUT / "followup/ena-AP025627.embl").read_text()
    sequence = "".join(
        re.findall("[a-z]+", chromosome.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//", 1)[0])
    ).upper()
    bases = "TCAG"
    amino = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    table = dict(zip([a + b + c for a in bases for b in bases for c in bases], amino, strict=True))
    seqs = {}
    translations = []
    for p in proteins:
        acc = p.findtext("GBSeq_accession-version")
        selected = [x for x in doc["participants"] if x["id"] == "NCBIProtein:" + acc]
        if selected:
            assert selected[0]["label"] == p.findtext("GBSeq_definition")
            assert selected[0]["category"] == "protein"
        quals = [
            (q.findtext("GBQualifier_name"), q.findtext("GBQualifier_value"))
            for q in p.findall(".//GBQualifier")
        ]
        assert ("db_xref", "taxon:2916802") in quals
        coded = next(v for k, v in quals if k == "coded_by")
        m = re.fullmatch(r"AP025627\.1:(\d+)\.\.(\d+)", coded)
        assert m, coded
        lo, hi = map(int, m.groups())
        dna = sequence[lo - 1 : hi]
        aa = "".join(table[dna[i : i + 3]] for i in range(0, len(dna), 3))
        aa = "M" + aa[1:]
        assert aa.endswith("*") and aa[:-1].lower() == p.findtext("GBSeq_sequence")
        seqs[acc] = dna
        translations.append(
            {
                "accession": acc,
                "coded_by": coded,
                "amino_acids": len(aa) - 1,
                "native_sequence_sha256": hashlib.sha256(aa[:-1].encode()).hexdigest(),
                "translation_exact": True,
            }
        )
    primer = "TTATTCTGTTGTTTTTCC"

    def rev(s):
        return s.translate(str.maketrans("ACGT", "TGCA"))[::-1]

    assert primer not in seqs["BDG45614.1"] and primer not in rev(seqs["BDG45614.1"])
    assert primer in rev(seqs["BDG45613.1"])
    extraction = load(ROOT / "primary-extraction.json")
    assert extraction["sha256"] == checked[extraction["original"]]
    for row in extraction["derived_pages"]:
        assert digest(row["text_path"]) == row["sha256"]
    text19 = " ".join((ROOT / "primary-extract/page-19.txt").read_text().split())
    assert "Duet-MCS2-dhbB-F" in text19 and "GACGGAGCTCGAATTTTATTCTGTTGTTTTTCC" in text19
    text12 = " ".join((ROOT / "primary-extract/page-12.txt").read_text().split())
    assert all(a in text12 for a in ["BDG45613", "BDG45614", "BDG45615", "BDG45616", "BDG45617"])
    assert load(ROOT / "originals/quickgo-bacillibactin.json")["numberOfHits"] == 0
    # Honest native/closed schema preflight: MNX adapter integration is a real prerequisite.
    schema_status = {}
    try:
        record = validate_record(doc)
        schema_status["native"] = "passed"
    except ValidationError as e:
        assert e.errors and all("unsupported prefix: metanetx.chemical" in x for x in e.errors), (
            e.errors
        )
        schema_status["native"] = "pending namespace integration"
        schema_status["native_errors"] = e.errors
        record = PathwayRecord(**doc)  # Export preflight only, explicitly not validated schema.
    strict = strict_errors([TARGET], REPO)
    if strict:
        assert all("metanetx.chemical" in x for x in strict), strict
        schema_status["closed"] = "pending namespace integration"
        schema_status["closed_errors"] = strict
    else:
        schema_status["closed"] = "passed"
    nodes_path, edges_path = write_kgx([record], ROOT / "actual-kgx")
    with edges_path.open() as f:
        exported = list(csv.DictReader(f, delimiter="\t"))
    assert len(exported) == len(doc["mechanistic_edges"])
    refs = {x["id"]: x for x in doc["references"]}
    for a, b in zip(doc["mechanistic_edges"], exported, strict=True):
        assert b["subject"] == a["subject"] and b["object"] == a["object"]
        assert b["predicate"] == LOCAL_PREDICATE_CURIES[a["predicate"]]
        assert json.loads(b["evidence"]) == a["evidence"]
        assert b["description"] == a.get("description", "")
        assert json.loads(b["reference_metadata"]) == [
            refs[k] for k in sorted({x["reference_id"] for x in a["evidence"]})
        ]
    with nodes_path.open() as f:
        nodes = {x["id"]: x for x in csv.DictReader(f, delimiter="\t")}
    for x in doc["participants"]:
        if x["category"] == "chemical_entity":
            assert nodes[x["id"]]["category"] == "biolink:ChemicalEntity"
    result = {
        "started_at": start,
        "finished_at": datetime.now(UTC).isoformat(),
        "status": "passed_scientific_author_replay_with_explicit_integration_prerequisites",
        "record_sha256": digest(TARGET),
        "script_sha256": digest(__file__),
        "counts": {
            "native_transformations": 12,
            "chemical_side_edges": source_count,
            "participants": len(doc["participants"]),
            "edges": len(doc["mechanistic_edges"]),
            "evidence": sum(len(x["evidence"]) for x in doc["mechanistic_edges"]),
            "references": len(doc["references"]),
            "original_bodies": len(checked),
            "exported_nodes": len(nodes),
        },
        "exact_small_molecule_balances": exact_balances,
        "conditional_carrier_reactive_part_balances": conditional,
        "NRPS_net": weighted,
        "full_chorismate_net": full_net,
        "nine_ATP_scope": "derived formal stoichiometry, not direct ATP/product measurement",
        "whole_polypeptide_balance": False,
        "native_chebi_bridges": bridges,
        "genome_translation_replay": translations,
        "primer_discrepancy": {
            "label": "Duet-MCS2-dhbB-F",
            "suffix": primer,
            "matches_DhbB_either_strand": False,
            "matches_DhbE_reverse_complement": True,
            "scope": "printed primer does not establish exact coexpression construct; "
            "does not show actual experimental plasmid was incorrect",
        },
        "mutation_guards": [
            "arginyl selected label rejected",
            "six-ATP composite addition rejected",
            "whole-polypeptide balance claim rejected",
        ],
        "schema": schema_status,
        "actual_KGX_preflight": {
            "validated_model": schema_status["native"] == "passed",
            "nodes": str(nodes_path),
            "nodes_sha256": digest(nodes_path),
            "edges": str(edges_path),
            "edges_sha256": digest(edges_path),
            "complete_evidence_and_metadata_preserved": True,
        },
        "canonical_authority_gate": "Pending separately reviewed MetaNetX integration "
        "and original-byte "
        "decoder for four malformed UTF-8 MetaCyc carrier pages; no gate bypass claimed.",
        "independent_scientific_review": "not performed by author; required before promotion",
    }
    (OUT / "bacillibactin-validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
