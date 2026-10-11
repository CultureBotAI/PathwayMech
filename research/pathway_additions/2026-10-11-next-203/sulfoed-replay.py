"""Offline SQ1 sulfo-ED author replay, not an independent scientific review."""

from __future__ import annotations

import collections
import csv
import gzip
import hashlib
import json
import re
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import etree as ET
from lxml import html

from pathwaymech.kgx import EXPLICIT_CATEGORIES, LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-203"
RAW = Path("/private/tmp/pathwaymech-next-203-evidence/sulfoed")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")
TARGET = ROOT / "data/pathways/sulfoquinovose-degradation-ii.yaml"
RH = "http://rdf.rhea-db.org/"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
SELECTED = ["47897", "47909", "47913", "47925", "47929", "47933"]
MASTERS = {"47896", "47908", "47912", "47924", "47928", "47932"}
NATIVE = ["RXN-17096", "RXN-17095", "RXN-17097", "RXN-17098", "RXN-17101"]


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def native(frame):
    return ET.parse(str(RAW / f"{frame}.xml")).getroot()[1]


def rhea_extract():
    directions = {}
    for line in (CACHE / "rhea-directions.tsv").read_text().splitlines()[1:]:
        cells = line.split("\t")
        if cells[0] in MASTERS:
            directions[cells[0]] = dict(
                zip(
                    ["master", "left_to_right", "right_to_left", "bidirectional"],
                    cells,
                    strict=True,
                )
            )
    numbers = {v for d in directions.values() for v in d.values()}
    nodes, compounds = {}, {}
    with gzip.open(CACHE / "rhea.rdf.gz", "rb") as stream:
        for _, element in ET.iterparse(stream, events=("end",), tag=RDF + "Description"):
            uri = element.get(RDF + "about", "")
            name = uri.rsplit("/", 1)[-1]
            chosen = name.split("_", 1)[0] in numbers or (
                name.startswith("Participant_") and name.split("_")[1] in numbers
            )
            dest = nodes if chosen else compounds if name.startswith("Compound_") else None
            if dest is not None:
                for child in element:
                    key = ET.QName(child).localname
                    value = child.get(RDF + "resource") or (child.text or "").strip()
                    values = dest.setdefault(uri, {}).setdefault(key, [])
                    if value not in values:
                        values.append(value)
            element.clear()
            while element.getprevious() is not None:
                del element.getparent()[0]
    needed = {v for d in nodes.values() for vs in d.values() for v in vs if v in compounds}
    nodes.update({uri: compounds[uri] for uri in needed})
    sides, balances, terms = [], [], {}
    with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as db:
        for rid in SELECTED:
            balance = collections.Counter()
            for role in ["substrates", "products"]:
                side = nodes[RH + rid][role][0]
                for predicate, participants in nodes[side].items():
                    if not re.fullmatch(r"contains\d+", predicate):
                        continue
                    coefficient = int(predicate[8:])
                    sign = -1 if role == "substrates" else 1
                    for participant in participants:
                        compound = nodes[participant]["compound"][0]
                        cp = nodes[compound]
                        cid = cp["accession"][0]
                        values = {
                            a: b if b is not None else c
                            for a, b, c in db.execute(
                                "select predicate,value,object from statements where subject=?",
                                (cid,),
                            )
                        }
                        terms[cid] = values
                        assert values.get("owl:deprecated") not in ["true", True]
                        assert values["chemrof:generalized_empirical_formula"] == cp["formula"][0]
                        assert values["chemrof:charge"] == cp["charge"][0]
                        formula = cp["formula"][0]
                        parts = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
                        assert "".join(a + b for a, b in parts) == formula
                        for atom, count in parts:
                            balance[atom] += sign * coefficient * int(count or 1)
                        balance["charge"] += sign * coefficient * int(cp["charge"][0])
                        sides.append(
                            dict(
                                reaction=rid,
                                role=role,
                                side=side,
                                predicate=predicate,
                                participant=participant,
                                compound=compound,
                                id=cid,
                                coefficient=coefficient,
                                label=values["rdfs:label"],
                                formula=formula,
                                charge=cp["charge"][0],
                            )
                        )
            assert all(v == 0 for v in balance.values()), (rid, balance)
            balances.append(dict(reaction=rid, residual=dict(balance), status="passed"))
    return dict(
        directions=directions,
        nodes=nodes,
        selected=SELECTED,
        sides=sides,
        balances=balances,
        terms=terms,
    )


def pointer(data, path):
    for key in path.strip("/").split("/"):
        data = data[int(key)] if isinstance(data, list) else data[key]
    return data


def native_projection():
    pathway = native("PWY-7722")
    members = pathway.xpath("reaction-list/Reaction/@frameid")
    assert set(members) == set(NATIVE) and len(members) == 5
    assert pathway.findtext("common-name") == "sulfoquinovose degradation II"
    assert pathway.xpath("species/Organism/strain-name/text()") == ["SQ1"]
    rows = []
    for i, frame in enumerate(NATIVE):
        reaction = native(frame)
        assert reaction.findtext("reaction-direction") == "LEFT-TO-RIGHT"
        assert reaction.xpath('dblink[dblink-db="RHEA"]/dblink-oid/text()') == [SELECTED[i]]
        if i:
            assert pathway.xpath(
                "reaction-ordering[Reaction/@frameid=$d]/predecessor-reactions/Reaction[@frameid=$u]",
                d=frame,
                u=NATIVE[i - 1],
            )
        rows.append(
            dict(
                native=frame,
                selected=[SELECTED[i]] if i < 4 else ["47929", "47933"],
                direction=reaction.findtext("reaction-direction"),
                left=[
                    dict(id=c.get("frameid"), coefficient=s.findtext("coefficient") or "1")
                    for s in reaction.findall("left")
                    for c in s
                    if c.tag == "Compound"
                ],
                right=[
                    dict(id=c.get("frameid"), coefficient=s.findtext("coefficient") or "1")
                    for s in reaction.findall("right")
                    for c in s
                    if c.tag == "Compound"
                ],
                enzyme_frames=reaction.xpath(
                    "enzymatic-reaction/Enzymatic-Reaction/enzyme/Protein/@frameid"
                ),
            )
        )
    bridges = []
    with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as db:
        for frame, cid in [
            ("CPD-10247", "77132"),
            ("CPD-18481", "88091"),
            ("CPD-18482", "88093"),
            ("CPD-18483", "88094"),
            ("CPD-18718", "90109"),
            ("CPD-11799", "61289"),
        ]:
            source = native(frame)
            current = db.execute(
                "select value from statements where subject=? and predicate='chemrof:inchi_string'",
                ("CHEBI:" + cid,),
            ).fetchone()[0]
            assert source.findtext("inchi") == current, frame
            assert cid in source.xpath('dblink[dblink-db="CHEBI"]/dblink-oid/text()')
            bridges.append(
                dict(
                    native=frame,
                    chebi="CHEBI:" + cid,
                    native_inchi=source.findtext("inchi"),
                    current_inchi=current,
                    relation="exact identity of the selected charged structural forms",
                )
            )
    assert "CPD-16503" in native("MONOMER-19523").findtext("comment")
    assert "CPD-16503" in native("MONOMER-19525").findtext("comment")
    assert native("RXN-17098").xpath('right/Compound[@frameid="CPD-18718"]')
    assert native("RXN-17101").xpath('left/Compound[@frameid="CPD-18718"]')
    assert native("RXN-17101").xpath('right/Compound[@frameid="CPD-11799"]')
    return dict(
        native_members=rows,
        chemical_bridges=bridges,
        dispositions=[
            dict(
                source="PWY-7722",
                status="complete",
                details=(
                    "All five native transformations represented; native generic final"
                    " NAD(P) reaction expands to exactly two experimentally supported "
                    "cofactor alternatives, not consecutive chemistry."
                ),
            ),
            dict(
                source="MONOMER-19521/comment",
                status="superseded wording",
                details=(
                    "Old 2-dehydrogenase prose is inconsistent with native C1 reaction"
                    " and primary/current reviewed 1-dehydrogenase identity."
                ),
            ),
            dict(
                source="MONOMER-19523/comment; MONOMER-19525/comment",
                status="superseded stereoisomer links",
                details=(
                    "Old CPD-16503 R-SLA comment links conflict with the native "
                    "reaction substrates/products and current Rhea/UniProt S-SLA/S-SL."
                    " Exact native selected compound InChIs match ChEBI. HPLC-MS is "
                    "not relabeled as a direct enantiomeric assay."
                ),
            ),
            dict(
                source="MONOMER-19525/comment",
                status="superseded family analogy",
                details=(
                    "The native KDPG-family analogy is rejected: full 2015 Discussion "
                    "identifies COG3836 distinct from KDPG COG0800. No KDPG absolute "
                    "inactivity is asserted after the 2026 abstract."
                ),
            ),
            dict(
                source="RXN-17101",
                status="complete cofactor expansion",
                details=(
                    "Native generic NAD-P-OR-NOP and NADH-P-OR-NOP classes cover NAD "
                    "and NADP alternatives. Current Rhea47928 and47932 master "
                    "equations and primary2015 support both."
                ),
            ),
            dict(
                source="PWY-7722 pathway links / CPD-367",
                status="context-only",
                details=(
                    "The broad native pathway link is not an extra reaction or current"
                    " endpoint; selected terminal native reaction uses CPD-11799."
                ),
            ),
            dict(
                source="PMID26195800 Discussion",
                status="excluded from native boundary",
                details=(
                    "Predicted SQ-glycoside hydrolysis, mutarotation, transport and "
                    "regulator assignments are outside the exact five-member pathway; "
                    "no unsupported gene-product IDs/causal edges added."
                ),
            ),
        ],
    )


def protein_projection():
    out = []
    for up, protein, gene, old, accession in [
        ("P0DOV5", "MONOMER-19521", "G-44226", "PpSQ1_00090", "KHL76346.1"),
        ("P0DOV6", "MONOMER-19522", "G-44227", "PpSQ1_00091", "KHL76347.1"),
        ("P0DOV7", "MONOMER-19524", "G-44229", "PpSQ1_00089", "KHL76345.1"),
        ("P0DOV8", "MONOMER-19525", "G-44230", "PpSQ1_00100", "KHL76360.1"),
        ("P0DOV9", "MONOMER-19523", "G-44228", "PpSQ1_00088", "KHL76344.1"),
    ]:
        u = read_json(RAW / f"UniProt-{up}.json")
        assert u["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
        assert u["organism"]["taxonId"] == 303
        assert all(r["referenceComments"][0]["value"] == "SQ1" for r in u["references"])
        assert native(protein).xpath("species/Organism/strain-name/text()") == ["SQ1"]
        assert native(gene).findtext("common-name") == old
        assert native(protein).xpath("gene/Gene/@frameid") == [gene]
        file = RAW / f"NCBI-{accession}{'-retry' if up == 'P0DOV8' else ''}.xml"
        ncbi = ET.parse(str(file))
        assert ncbi.findtext(".//GBSeq_accession-version") == accession
        assert ncbi.xpath('//GBQualifier[GBQualifier_name="strain"]/GBQualifier_value/text()') == [
            "SQ1"
        ]
        seq = ncbi.findtext(".//GBSeq_sequence").upper()
        assert seq == u["sequence"]["value"]
        locus = u["genes"][0]["orfNames"][0]["value"]
        assert ncbi.xpath(
            '//GBQualifier[GBQualifier_name="locus_tag"]/GBQualifier_value/text()'
        ) == [locus]
        out.append(
            dict(
                accession=up,
                label=u["proteinDescription"]["recommendedName"]["fullName"]["value"],
                entry_audit=u["entryAudit"],
                taxon=303,
                strain="SQ1",
                native_frame=protein,
                native_gene=gene,
                original_IMG_locus=old,
                current_GenBank_locus=locus,
                EMBL_protein=accession,
                sequence_sha256=hashlib.sha256(seq.encode()).hexdigest(),
                sequence=seq,
                comments=u["comments"],
                source_scope=(
                    "reviewed functions with exact source evidence codes; original "
                    "GenBank sequence/strain only"
                ),
            )
        )
    # Full primary sequence is directly bridged to current SQDH after removal of tag.
    article = html.parse(str(RAW / "PMC12133307-original.html"))
    sequence_text = "".join(article.xpath('//*[@id="s5-2"]')[0].itertext())
    sqdh = out[0]["sequence"]
    assert "MGSSHHHHHHSSG" + sqdh in re.sub(r"\s+", "", sequence_text)
    # Original 2015 aldolase forward primer maps exactly 36 nt upstream of the
    # current call on the original SQ1 contig; reverse primer covers its endpoint.
    seq = "".join((RAW / "NCBI-JTCJ01000004.1.fasta").read_text().splitlines()[1:]).upper()
    rev = seq.translate(str.maketrans("ACGT", "TGCA"))[::-1]
    start = len(seq) - rev.index("ATGTCCACTGCTGTCACG")
    assert start == 19596 and start - 19560 == 36
    assert seq.index("GTAGGCTGTCGCTAC") + 1 == 18796
    assert seq[19557:19560] == "CAG"  # annotated reverse-strand start is CTG
    # Universal codon table, with start translation handled explicitly.
    bases = "TCAG"
    aas = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = {
        a + b + c: aa
        for (a, b, c), aa in zip(
            ((a, b, c) for a in bases for b in bases for c in bases), aas, strict=True
        )
    }
    coding = seq[18792:19596].translate(str.maketrans("ACGT", "TGCA"))[::-1]
    translated = "".join(codons[coding[i : i + 3]] for i in range(0, len(coding), 3))
    assert translated[:12] == "MSTAVTPPTFTP"
    assert translated[12] == "L" and "M" + translated[13:-1] == out[3]["sequence"]
    return dict(
        proteins=out,
        sequence_bridges=dict(
            SQDH_2025="exact P0DOV5 sequence after N-terminal His-tag removal",
            aldolase_2015=dict(
                original_forward_primer="CACCATGTCCACTGCTGTCACG",
                original_reverse_primer="TCAGTAGGCTGTCGCTAC",
                contig="JTCJ01000004.1",
                original_construct_interval="complement(18793..19596)",
                current_CDS_interval="complement(18793..19560)",
                extension=translated[:12],
                remaining_difference=(
                    "Current CDS starts at CTG, translated as initiator Met in the "
                    "annotation; same codon is Leu internally in the longer "
                    "experimental construct."
                ),
                decision=(
                    "Same original genomic locus with an explicit "
                    "start-annotation/construct difference; no whole-sequence "
                    "exactMatch assertion."
                ),
            ),
        ),
    )


def source_checks(record, manifest, projection):
    sources = {x["reference_id"]: x for x in manifest["reference_sources"]}
    refs = {x["id"]: x for x in record["references"]}
    hashes = {}
    for s in sources.values():
        if s["path"] not in hashes:
            hashes[s["path"]] = digest(s["path"])
        assert hashes[s["path"]] == s["sha256"] == refs[s["reference_id"]]["source_sha256"]
    checked = []
    for edge in record["mechanistic_edges"]:
        for e in edge["evidence"]:
            rid = e["reference_id"]
            loc = e["source_locator"]
            path = sources[rid]["path"]
            if rid.startswith("MetaCyc:") or rid.startswith("NCBIProtein:"):
                tree = ET.parse(path)
                for xp in loc.split("; "):
                    assert tree.xpath(xp), (edge["id"], xp)
            elif rid.startswith("UniProtKB:"):
                d = read_json(path)
                for xp in loc.split("; "):
                    assert pointer(d, xp) is not None, (edge["id"], xp)
            elif rid.startswith("RHEA:"):
                # Replay each referred subject and the exact master→member triple.
                uris = re.findall(r'rdf:about="([^"]+)"', loc)
                assert uris and all(u in projection["rhea"]["nodes"] for u in uris)
                if "directionalReaction" in loc:
                    assert (
                        RH + rid[5:] in projection["rhea"]["nodes"][uris[0]]["directionalReaction"]
                    )
            elif rid == "PMID:41830472":
                d = read_json(path)["resultList"]["result"][0]
                assert d["id"] == "41830472" and "homohexamer" in d["abstractText"]
            else:
                tree = html.parse(path)
                xps = re.findall(r'//\*\[@id="[^"]+"\](?:/p\[\d+\])?', loc)
                assert xps, (edge["id"], loc)
                for xp in xps:
                    assert tree.xpath(xp), (edge["id"], xp)
            checked.append(dict(edge=edge["id"], reference_id=rid, source_locator=loc))
    return checked


def check_primary():
    trees = {
        p: html.parse(str(RAW / f"{p}-original.html"))
        for p in ["PMC4534283", "PMC12133307", "PMC10599462"]
    }

    def text(p, xp):
        return " ".join("".join(z.itertext()) for z in trees[p].xpath(xp))

    tests = [
        (
            "PMC4534283",
            '//*[@id="s5"]/p[2]',
            ["lactonase", "dehydratase", "aldolase", "pyruvate", "cochromatography", "SL"],
        ),
        (
            "PMC4534283",
            '//*[@id="s4"]/p[2]',
            ["NAD+", "NADP+", "succinate semialdehyde", "could not determine"],
        ),
        ("PMC4534283", '//*[@id="s3"]/p[4]', ["insertion mutant", "glucose", "SQ"]),
        ("PMC4534283", '//*[@id="si8"]/p[1]', ["chromosomal DNA", "SQ1", "DNA sequencing"]),
        ("PMC4534283", '//*[@id="si3"]/p[1]', ["DSM 100120", "30 °C"]),
        ("PMC12133307", '//*[@id="s2-2"]/p[1]', ["SEC-MALLS", "119", "tetramer"]),
        ("PMC12133307", '//*[@id="s2-1"]/p[2]', ["high enzyme concentration", "low rate"]),
        ("PMC12133307", '//*[@id="s2-1"]/p[4]', ["competitive inhibitor", "NADH"]),
        ("PMC10599462", '//*[@id="sec3"]/p[1]', ["racemic", "47", "Rhizobium"]),
        ("PMC10599462", '//*[@id="sec6"]/p[1]', ["tetramer", "210"]),
    ]
    for p, xp, terms in tests:
        actual = text(p, xp)
        for term in terms:
            assert term in actual, (p, xp, term)
    return [dict(source=p, locator=xp, checked_terms=terms) for p, xp, terms in tests]


def main():
    started = datetime.now(UTC).isoformat()
    target_hash = digest(TARGET)
    record = yaml.safe_load(TARGET.read_text())
    validated = validate_record(record)
    assert not strict_errors([TARGET], ROOT)
    manifest = read_json(DOSSIER / "sulfoed-source-manifest.json")
    for x in manifest["original_acquisitions"]:
        if "sha256" in x:
            assert digest(x["path"]) == x["sha256"], x["path"]
    assert (
        digest(CACHE / "rhea-directions.tsv")
        == "deae1911da372c70ee8fc97992809c7923e63b288a8702fc4396edcb2633fb04"
    )
    assert (
        digest(CACHE / "chebi.db")
        == "26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f"
    )
    rhea = rhea_extract()
    native_data = native_projection()
    proteins = protein_projection()
    primary = check_primary()
    projection = read_json(DOSSIER / "sulfoed-source-projection.json")
    assert projection["rhea"] == rhea
    assert projection["native"] == native_data
    assert read_json(DOSSIER / "sulfoed-protein-projection.json") == proteins
    chemical = [
        e for e in record["mechanistic_edges"] if e["predicate"] in ["consumes", "produces"]
    ]
    expected = [
        (x["id"], "consumes", "RHEA:" + x["reaction"])
        if x["role"] == "substrates"
        else ("RHEA:" + x["reaction"], "produces", x["id"])
        for x in rhea["sides"]
    ]
    assert collections.Counter(expected) == collections.Counter(
        (e["subject"], e["predicate"], e["object"]) for e in chemical
    )
    assert len(chemical) == 27
    nets = {}
    for final in ["47929", "47933"]:
        net = collections.Counter()
        for x in rhea["sides"]:
            if x["reaction"] in SELECTED[:4] + [final]:
                net[x["id"]] += x["coefficient"] * (-1 if x["role"] == "substrates" else 1)
        net = {k: v for k, v in net.items() if v}
        nets[final] = net
        assert net["CHEBI:77132"] == -1 and net["CHEBI:15361"] == 1 and net["CHEBI:61289"] == 1
        assert net["CHEBI:15377"] == -1 and net["CHEBI:15378"] == 4
        assert net["CHEBI:57540"] == (-2 if final == "47933" else -1)
        assert net["CHEBI:57945"] == (2 if final == "47933" else 1)
    assert all(x["direction"] == "left_to_right" for x in record["reactions"])
    assert all(e["predicate"] != "catalyzes" for e in record["mechanistic_edges"])
    with sqlite3.connect(f"file:{CACHE}/ncbitaxon.db?mode=ro", uri=True) as db:
        assert (
            db.execute(
                
                    "select value from statements where subject='NCBITaxon:303' and "
                    "predicate='rdfs:label'"
                
            ).fetchone()[0]
            == record["taxa"][0]["label"]
        )
    with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as db:
        for p in record["participants"]:
            if p["id"].startswith("CHEBI:"):
                assert (
                    db.execute(
                        "select value from statements where subject=? and predicate='rdfs:label'",
                        (p["id"],),
                    ).fetchone()[0]
                    == p["label"]
                )
            else:
                assert (
                    read_json(RAW / f"UniProt-{p['id'][10:]}.json")["proteinDescription"][
                        "recommendedName"
                    ]["fullName"]["value"]
                    == p["label"]
                )
    checked = source_checks(record, manifest, projection)
    nodes_path, edges_path = write_kgx([validated], RAW / "replay-kgx")
    with nodes_path.open() as f:
        nodes = {x["id"]: x for x in csv.DictReader(f, delimiter="\t")}
    with edges_path.open() as f:
        edges = list(csv.DictReader(f, delimiter="\t"))
    refs = {x["id"]: x for x in record["references"]}
    assert len(edges) == 48 and len(nodes) == 28 and len(checked) == 86
    for actual, original in zip(edges, record["mechanistic_edges"], strict=True):
        assert (actual["subject"], actual["predicate"], actual["object"]) == (
            original["subject"],
            LOCAL_PREDICATE_CURIES[original["predicate"]],
            original["object"],
        )
        assert json.loads(actual["evidence"]) == original["evidence"]
        assert actual["description"] == original.get("description", "")
        assert json.loads(actual["reference_metadata"]) == [
            refs[r] for r in sorted({e["reference_id"] for e in original["evidence"]})
        ]
    for group in ["participants", "reactions"]:
        for n in record[group]:
            actual = nodes[n["id"]]
            assert actual["category"] == EXPLICIT_CATEGORIES[n["category"]]
            assert actual["direction"] == n.get("direction", "")
            assert json.loads(actual["source_contexts"])[0] == dict(
                record_id=record["id"], collection=group, **n
            )
    assert digest(TARGET) == target_hash
    result = dict(
        status="passed",
        started_at=started,
        finished_at=datetime.now(UTC).isoformat(),
        target=str(TARGET.relative_to(ROOT)),
        target_sha256=target_hash,
        helper_sha256=digest(Path(__file__)),
        command=(
            "PYTHONPATH=src UV_NO_SYNC=1 "
            "UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache "
            ".venv/bin/python "
            "research/pathway_additions/2026-10-11-next-203/sulfoed-replay.py"
        ),
        workdir=str(ROOT),
        source_body_count=sum("sha256" in x for x in manifest["original_acquisitions"]),
        reference_count=len(refs),
        chemical_sides=len(chemical),
        balances=rhea["balances"],
        native_reaction_members=5,
        selected_activities=6,
        alternative_net_equations=nets,
        exact_native_chemical_bridges=6,
        proteins=5,
        original_primary_checks=primary,
        evidence_locator_checks=checked,
        kgx=dict(
            nodes=len(nodes),
            edges=len(edges),
            evidence=len(checked),
            nodes_sha256=digest(nodes_path),
            edges_sha256=digest(edges_path),
        ),
        limits=[
            "Author source replay, not independent scientific review.",
            (
                "Full ChEBI255, Rhea142 and direction input digests checked; "
                "selected taxon label queried, full 14GB taxon digest delegated to"
                " shared integration."
            ),
            "2026 abstract-only aldolase context is not verified construct-specific evidence.",
            (
                "Canonical shared identifier snapshots, history, pages and full "
                "gates are coordinated separately by root."
            ),
        ],
    )
    (DOSSIER / "sulfoed-validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: result[k]
                for k in [
                    "status",
                    "target_sha256",
                    "source_body_count",
                    "reference_count",
                    "chemical_sides",
                    "kgx",
                ]
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
