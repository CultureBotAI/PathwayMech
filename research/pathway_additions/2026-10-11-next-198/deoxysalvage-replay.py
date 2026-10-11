"""Author replay of complete E. coli deoxyribonucleotide salvage original sources."""

from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.util
import io
import json
import re
import sqlite3
import zipfile
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import etree

from pathwaymech.kgx import render_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path(__file__).resolve().parents[3]
DOSSIER = Path(__file__).parent
RAW = Path("/private/tmp/pathwaymech-next-198-evidence/deoxysalvage")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/pyrimidine-deoxyribonucleotide-salvage.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
BP = "http://www.biopax.org/release/biopax-level3.owl#"
NS = {"rdf": RDF, "rh": RH, "rdfs": "http://www.w3.org/2000/01/rdf-schema#"}


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(name):
    return json.loads((DOSSIER / f"deoxysalvage-{name}.json").read_text())


def main():
    started = datetime.now(UTC).isoformat()
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert strict_errors([TARGET], ROOT) == []
    target_hash = digest(TARGET)
    manifest, projection, proteins, identifiers = [
        read(x)
        for x in ["source-manifest", "source-projection", "protein-projection", "identifiers"]
    ]
    for name in [
        "source-manifest",
        "source-projection",
        "protein-projection",
        "identifiers",
        "dedup",
        "authority-inputs",
    ]:
        assert read(name)["target_sha256"] == target_hash
    for source in manifest["source_bodies"] + manifest["unavailable_or_rejected_attempts"]:
        assert digest(source["raw_path"]) == source["sha256"], source["raw_path"]
    for ref in doc["references"]:
        assert digest(manifest["reference_body_map"][ref["id"]]) == ref["source_sha256"]
    pb_source = next(x for x in manifest["source_bodies"] if x.get("archive"))
    archive = pb_source["archive"]
    assert digest(archive["archive_path"]) == archive["archive_sha256"]
    with zipfile.ZipFile(archive["archive_path"]) as z:
        assert z.read(archive["member"]) == (RAW / archive["member"]).read_bytes()

    # Reparse the original full RDF, including repeated descriptions of the same URI.
    wanted = {RH + r[k] for r in projection["reactions"] for k in ["master"]}
    wanted.update(RH + r["selected_reaction"].split(":")[1] for r in projection["reactions"])
    for side in projection["rhea_side_projection"]:
        wanted.update(side[k] for k in ["side_uri", "participant", "compound"])
    nodes = {}
    wrapper = "<root " + " ".join(f'xmlns:{k}="{v}"' for k, v in NS.items()) + ">"
    with gzip.open(CACHE / "rhea.rdf.gz", "rt") as stream:
        original = stream.read()
    for match in re.finditer(r'<rdf:Description rdf:about="([^"]+)">', original):
        if match[1] not in wanted:
            continue
        end = original.index("</rdf:Description>", match.start()) + len("</rdf:Description>")
        element = etree.fromstring((wrapper + original[match.start() : end] + "</root>").encode())[
            0
        ]
        props = nodes.setdefault(match[1], {})
        for child in element:
            key = etree.QName(child).localname
            value = child.get("{" + RDF + "}resource") or child.text
            if value not in props.setdefault(key, []):
                props[key].append(value)
    del original
    assert wanted == set(nodes)
    chemistry = {}
    conn = sqlite3.connect(f"file:{CACHE / 'chebi.db'}?mode=ro", uri=True)
    for curie in {x["chebi"] for x in projection["rhea_side_projection"]}:
        chemistry[curie] = dict(
            conn.execute(
                "select predicate,value from statements where subject=? and value is not null",
                (curie,),
            )
        )
    conn.close()
    edges = {e["id"]: e for e in doc["mechanistic_edges"]}
    chemical_edges = {
        e["id"] for e in doc["mechanistic_edges"] if e["predicate"] in ["consumes", "produces"]
    }
    assert chemical_edges == {x["edge_id"] for x in projection["rhea_side_projection"]}
    balances = {}
    for x in projection["rhea_side_projection"]:
        assert RH + x["directed"] in nodes[RH + x["master"]]["directionalReaction"]
        assert x["side_uri"] in nodes[RH + x["directed"]][x["side"]]
        assert x["participant"] in nodes[x["side_uri"]]["contains" + str(x["coefficient"])]
        assert nodes[x["participant"]]["compound"] == [x["compound"]]
        assert nodes[x["compound"]]["accession"] == [x["chebi"]]
        assert nodes[x["compound"]]["formula"] == [x["formula"]]
        assert nodes[x["compound"]]["charge"] == [str(x["charge"])]
        assert chemistry[x["chebi"]]["chemrof:generalized_empirical_formula"] == x["formula"]
        assert chemistry[x["chebi"]]["chemrof:charge"] == str(x["charge"])
        e = edges[x["edge_id"]]
        endpoint = "subject" if x["side"] == "substrates" else "object"
        assert e[endpoint] == x["chebi"]
        assert e["evidence"][0]["reference_id"] == "RHEA:" + x["directed"]
        assert f"coefficient {x['coefficient']}" in e["evidence"][0]["source_assertion"]
        for token in [x["side_uri"], x["participant"], x["compound"]]:
            assert token in e["evidence"][0]["source_locator"]
        total = balances.setdefault(x["directed"], {}).setdefault(x["side"], Counter())
        for atom, count in re.findall(r"([A-Z][a-z]?)(\d*)", x["formula"]):
            total[atom] += int(count or "1") * x["coefficient"]
        total["charge"] += x["charge"] * x["coefficient"]
    assert len(balances) == 5
    assert all(b["substrates"] == b["products"] for b in balances.values())
    for frame, x in projection["compound_crosswalks"].items():
        native = etree.parse(x["raw_path"]).find("Compound")
        assert native.get("frameid") == frame
        assert native.xpath('./dblink[dblink-db="CHEBI"]/dblink-oid/text()') == [
            x["curie"].split(":")[1]
        ]
        assert (
            native.findtext("inchi") == chemistry[x["curie"]]["chemrof:inchi_string"] == x["inchi"]
        )
    directions = list(csv.DictReader((CACHE / "rhea-directions.tsv").open(), delimiter="\t"))
    frame_map = {f: x["curie"] for f, x in projection["compound_crosswalks"].items()}
    for r in projection["reactions"]:
        frame, rid = r["native_id"].split(":")[1], r["selected_reaction"].split(":")[1]
        native = etree.parse(r["raw_path"]).find("Reaction")
        assert native.get("frameid") == frame
        assert (
            native.xpath('./dblink[dblink-db="RHEA"]/dblink-oid/text()') == r["native_rhea_xrefs"]
        )
        row = next(x for x in directions if x["RHEA_ID_MASTER"] == r["master"])
        assert row["RHEA_ID_RL" if rid == "16039" else "RHEA_ID_LR"] == rid
        assert set(r["native_rhea_xrefs"]).issubset(set(row.values()))
        declared = next(x for x in doc["reactions"] if x["id"] == r["selected_reaction"])
        assert declared["direction"] == ("right_to_left" if rid == "16039" else "left_to_right")
        assert declared["label"] == nodes[RH + rid]["equation"][0]
        pairs = (
            [("left", "products"), ("right", "substrates")]
            if rid == "16039"
            else [("left", "substrates"), ("right", "products")]
        )
        for native_side, selected_side in pairs:
            before = Counter()
            for part in native.findall(native_side):
                before[frame_map[part[0].get("frameid")]] += int(part.findtext("coefficient", "1"))
            after = Counter(
                {
                    x["chebi"]: x["coefficient"]
                    for x in projection["rhea_side_projection"]
                    if x["directed"] == rid and x["side"] == selected_side
                }
            )
            assert before == after, (rid, before, after)
        # Every reaction membership and catalyst retains explicit master-family provenance.
        for edge in [
            e
            for e in doc["mechanistic_edges"]
            if (e["object"] == "RHEA:" + rid and e["predicate"] == "catalyzes")
            or (e["subject"] == "RHEA:" + rid and e["predicate"] == "part_of")
        ]:
            family = next(e for e in edge["evidence"] if e["reference_id"] == "RHEA:" + rid)
            assert "rh:directionalReaction" in family["source_locator"]
            assert RH + r["master"] in family["source_locator"]

    # All original source-map transformations and controller objects receive dispositions.
    tree = etree.parse(str(RAW / "PW002061.owl"))
    objects = {
        (
            "#" + x.get("{" + RDF + "}ID")
            if x.get("{" + RDF + "}ID")
            else x.get("{" + RDF + "}about")
        ): x
        for x in tree.getroot()
        if x.get("{" + RDF + "}ID") or x.get("{" + RDF + "}about")
    }
    pathway = objects["http://identifiers.org/smpdb/SMP0002073"]
    members = pathway.xpath("./b:pathwayComponent/@rdf:resource", namespaces={"b": BP, "rdf": RDF})
    preserved = projection["original_pathbank_member"]
    assert set(members) == set(preserved["pathway_members"]) and len(members) == 18
    assert {u for u in members if u.startswith("#Transports/")} == set(
        preserved["transport_dispositions"]
    )
    for r in projection["reactions"]:
        source = objects[r["pathbank_object"]]
        assert source.findtext("{" + BP + "}conversionDirection") == "LEFT_TO_RIGHT"
        rid = r["selected_reaction"].split(":")[1]
        for native_side, selected_side in [("left", "substrates"), ("right", "products")]:
            mapped = Counter()
            for link in source.findall("{" + BP + "}" + native_side):
                molecule = objects[link.get("{" + RDF + "}resource")]
                ref = objects[
                    molecule.find("{" + BP + "}entityReference").get("{" + RDF + "}resource")
                ]
                xrefs = [
                    objects[x.get("{" + RDF + "}resource")] for x in ref.findall("{" + BP + "}xref")
                ]
                source_chebi = [
                    x.findtext("{" + BP + "}id")
                    for x in xrefs
                    if x.findtext("{" + BP + "}db") == "ChEBI"
                ]
                assert len(source_chebi) == 1, source_chebi
                crosswalk = projection["pathbank_chemical_crosswalks"][source_chebi[0]]
                assert crosswalk["source_chebi"] == source_chebi[0]
                mapped[crosswalk["selected_chebi"]] += 1
            expected = Counter(
                {
                    x["chebi"]: x["coefficient"]
                    for x in projection["rhea_side_projection"]
                    if x["directed"] == rid and x["side"] == selected_side
                }
            )
            assert mapped == expected, (rid, mapped, expected)
        for link in source.findall("{" + BP + "}participantStoichiometry"):
            stoich = objects[link.get("{" + RDF + "}resource")]
            assert float(stoich.findtext("{" + BP + "}stoichiometricCoefficient")) == 1.0
    eco = etree.parse(str(RAW / "ecocyc-PWY0-181.xml")).find("Pathway")
    assert eco.get("orgid") == "ECOLI" and eco.get("frameid") == "PWY0-181"
    assert set(eco.xpath("./reaction-list/Reaction/@frameid")) == {
        r["native_id"].split(":")[1] for r in projection["reactions"]
    }
    other = etree.parse(str(RAW / "metacyc-PWY-7199.xml")).find("Pathway")
    assert set(other.xpath("./reaction-list/Reaction/@frameid")) != set(
        eco.xpath("./reaction-list/Reaction/@frameid")
    )
    go = json.loads((RAW / "go-GO0010139.json").read_text())["results"][0]
    assert go["id"] == doc["id"] and go["name"] == doc["label"] and not go["isObsolete"]
    conn = sqlite3.connect(f"file:{CACHE / 'go.db'}?mode=ro", uri=True)
    assert (
        conn.execute(
            "select value from statements where subject=? and predicate='rdfs:label'", (doc["id"],)
        ).fetchone()[0]
        == doc["label"]
    )
    conn.close()
    assert not doc.get("source_mappings")
    assert all(x["id"] not in ["MetaCyc:PWY0-181", "MetaCyc:PWY-7199"] for x in doc["references"])

    for acc, x in proteins["proteins"].items():
        up = json.loads(Path(x["raw_path"]).read_text())
        assert up["primaryAccession"] == acc and up["organism"]["taxonId"] == 83333
        assert up["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
        complex_node = etree.parse(str(RAW / f"metacyc-{x['native_complex']}.xml")).find("Protein")
        assert complex_node.find("component/Protein").get("frameid") == x["native_component"]
        assert complex_node.findtext("component/coefficient") == ("2" if acc != "P23331" else None)
        assert complex_node.xpath("./species/Organism/@frameid") == ["TAX-511145"]
        monomer = etree.parse(str(RAW / f"metacyc-{x['native_component']}.xml")).find("Protein")
        assert monomer.xpath('./dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [acc]
        for edge in doc["mechanistic_edges"]:
            if (
                edge["subject"] != "MetaCyc:" + x["native_complex"]
                or edge["predicate"] != "catalyzes"
            ):
                continue
            r = next(r for r in projection["reactions"] if r["selected_reaction"] == edge["object"])
            assert r["native_id"].split(":")[1] in complex_node.xpath(
                "./catalyzes/Enzymatic-Reaction/reaction/Reaction/@frameid"
            )
    tdk = json.loads((RAW / "uniprot-P23331.json").read_text())
    assert tdk["comments"][3]["texts"][0]["evidences"][0]["evidenceCode"] == "ECO:0000255"
    cdd = json.loads((RAW / "uniprot-P0ABF6.json").read_text())
    assert cdd["comments"][3]["cofactors"][0]["cofactorCrossReference"]["id"] == "CHEBI:29105"
    assert "zinc" in cdd["comments"][3]["note"]["texts"][0]["value"]
    # Exact primary access and locator anchors, not a substitute for the scientific reading.
    abstract = json.loads((RAW / "pmid-2041474.json").read_text())["resultList"]["result"][0][
        "abstractText"
    ]
    assert all(s in abstract for s in ["W3110", "KY895", "multimeric complex"])
    full = etree.HTML((RAW / "PMC2168750.html").read_bytes())
    fulltext = " ".join(full.xpath("//article//text()"))
    assert (
        "Escherichia coli" in fulltext and "three known routes" in fulltext and "K-12" in fulltext
    )
    assert "thymidine kinase" in fulltext.lower() or "thd kinase" in fulltext.lower()
    assert (RAW / "PMID4202859.pdf").read_bytes().startswith(b"%PDF")
    assert all(x in (RAW / "PMID4202859.txt").read_text() for x in ["Y-70-272", "802", "Substrate"])

    spec = importlib.util.spec_from_file_location(
        "source_builder", ROOT / "scripts/build_source_identifier_snapshot.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for item in read("authority-inputs")["proposed_source_inputs"]:
        assert digest(item["raw_path"]) == item["sha256"]
        if item["kind"] == "metacyc-html":
            assert list(mod.metacyc_terms(Path(item["raw_path"]).read_text())) == [
                (item["id"], item["canonical_label"], [])
            ]
    kgx = render_kgx([record])
    exported = list(csv.DictReader(io.StringIO(kgx["edges.tsv"]), delimiter="\t"))
    nodes_out = list(csv.DictReader(io.StringIO(kgx["nodes.tsv"]), delimiter="\t"))
    assert len(exported) == len(edges) == 41
    assert len(nodes_out) == 28
    for before, after in zip(doc["mechanistic_edges"], exported, strict=True):
        assert (before["subject"], before["object"]) == (after["subject"], after["object"])
        assert before.get("description", "") == after["description"]
        assert before["evidence"] == json.loads(after["evidence"])
        assert {x["id"] for x in json.loads(after["reference_metadata"])} == {
            x["reference_id"] for x in before["evidence"]
        }
    categories = {x["id"]: x for x in nodes_out}
    for part in doc["participants"]:
        assert {"record_id": doc["id"], "collection": "participants", **part} in json.loads(
            categories[part["id"]]["source_contexts"]
        )
        if part["category"] == "complex":
            assert categories[part["id"]]["category"] == "biolink:MacromolecularComplex"
    export_dir = RAW / "actual-kgx"
    export_dir.mkdir(exist_ok=True)
    for name, body in kgx.items():
        (export_dir / name).write_text(body)
    print(
        json.dumps(
            dict(
                status="passed",
                started_at=started,
                completed_at=datetime.now(UTC).isoformat(),
                target=str(TARGET.relative_to(ROOT)),
                target_sha256=target_hash,
                helper_sha256=digest(__file__),
                source_bodies=len(manifest["source_bodies"]),
                unavailable_attempts_hashed=len(manifest["unavailable_or_rejected_attempts"]),
                reference_bodies=len(doc["references"]),
                pathbank_members=18,
                pathbank_biochemical_reactions=5,
                transport_objects_dispositioned=4,
                chemical_sides=len(chemical_edges),
                atom_charge_balances=balances,
                exact_native_chebi_inchi_bridges=14,
                counts=dict(
                    participants=21,
                    reactions=5,
                    nodes=28,
                    edges=41,
                    evidence=sum(len(e["evidence"]) for e in doc["mechanistic_edges"]),
                ),
                checks=[
                    "native schema",
                    "closed schema",
                    "all original source/reference/archive hashes",
                    "fresh complete RDF side/coefficient/family replay",
                    "native reaction sides and selected reversal",
                    "GO native process identity and distinct EcoCyc versus MetaCyc scope",
                    "all PathBank membership and biochemical side replay",
                    "native complexes and reviewed protein identities with explicit Tdk inference",
                    "actual KGX all endpoints/description/evidence/reference metadata/categories",
                ],
                actual_kgx={
                    name: dict(path=str(export_dir / name), sha256=digest(export_dir / name))
                    for name in kgx
                },
                limits=[
                    "Author verification, not independent scientific review.",
                    "Root owns full corpus render/test/identifier gates; not attested here.",
                    "Primary1991/1994/1990 structures abstract only;1973/2007 full text inspected.",
                    "Native K12 annotation, E.coli B studies and mutant flux evidence "
                    "have distinct scope.",
                ],
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
