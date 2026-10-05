#!/usr/bin/env python3
"""Bounded, independently reviewed folate and inositol chemistry corrections.

This is a one-time guarded migration. It deliberately does not infer enzyme
specificity from equation similarity or specialize generic source compounds.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sqlite3
from pathlib import Path

import yaml
from review_gocam_graphs import IndentedDumper

from pathwaymech.curation import publish_curation
from pathwaymech.schema import validate_record

BATCH_SHA = "9600fe7f1e55a4f51554b244607a706b1604904dc71de8960b2f399bf75b0c7c"
PAPER_SHA = "3e4daf11de27f7571fd524187c26585c63365169c80143be547437354180a0c9"
PAPER_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7196807/fullTextXML"
PP4 = "gomodel:CHEBI_14178_RXN-4941"
PP5 = "gomodel:CHEBI_62919_RXN3O-786"


def activity_audit(record, proteins):
    """Inventory every reviewed activity, including retained native chemistry."""
    by_sgd = {
        "SGD:" + x["id"]: (p, i)
        for p, i in proteins.values()
        for x in p.get("uniProtKBCrossReferences", [])
        if x["database"] == "SGD"
    }
    reviewed = []
    for node in record["reactions"]:
        aid = node["id"]
        enablers = [
            e["subject"]
            for e in record["mechanistic_edges"]
            if e["predicate"] == "enables" and e["object"] == aid
        ]
        sources = []
        for enabler in enablers:
            if enabler in by_sgd:
                protein, index = by_sgd[enabler]
                sources.append(
                    {
                        "accession": protein["primaryAccession"],
                        "batch_index": index,
                        "comments": [
                            {"index": i, "annotation": c}
                            for i, c in enumerate(protein.get("comments", []))
                            if c["commentType"] in ("FUNCTION", "CATALYTIC ACTIVITY")
                        ],
                    }
                )
            elif enabler == "SGD:S000218158":
                sources.append(
                    {
                        "complex": "ComplexPortal:CPX-1268",
                        "disposition": "Native mitochondrial glycine cleavage "
                        "chemical sides and complex components retained.",
                    }
                )
            else:
                raise ValueError(f"Unexpected unaudited enabler {enabler}")
        reviewed.append(
            {
                "activity": aid,
                "label": node["label"],
                "enablers": enablers,
                "reviewed_protein_annotations": sources,
                "chemical_sides": {
                    role: [
                        e["object"]
                        for e in record["mechanistic_edges"]
                        if e["subject"] == aid and e["predicate"] == role
                    ]
                    for role in ("has_input", "has_output")
                },
                "disposition": "Compared all chemical sides; bounded corrections "
                "and qualified new activity are detailed in this record's change ledger. "
                "Other native intermediate chemistry retained at its source specificity.",
            }
        )
    return reviewed


def curate(root: Path, source_dir: Path, chebi_db: Path, rhea_db: Path, apply=False, report=None):
    raw = (source_dir / "uniprot-yeast-reviewed-catalysis.json").read_bytes()
    meta = json.loads((source_dir / "uniprot-yeast-reviewed-catalysis.provenance.json").read_text())
    if hashlib.sha256(raw).hexdigest() != BATCH_SHA or meta["sha256"] != BATCH_SHA:
        raise ValueError("Unreviewed UniProt catalytic source bytes")
    if hashlib.sha256((source_dir / "PMC7196807.xml").read_bytes()).hexdigest() != PAPER_SHA:
        raise ValueError("Unreviewed Vip1 primary experimental source bytes")
    proteins = {p["primaryAccession"]: (p, i) for i, p in enumerate(json.loads(raw)["results"])}
    chebi = sqlite3.connect(f"file:{chebi_db}?mode=ro", uri=True)
    rhea = sqlite3.connect(f"file:{rhea_db}?mode=ro", uri=True)
    ledger, pending = [], []

    def node(record, identifier, label=None, reaction=False):
        section = "reactions" if reaction else "participants"
        if any(n["id"] == identifier for n in record[section]):
            return
        if label is None:
            db = rhea if identifier.startswith("RHEA:") else chebi
            row = db.execute(
                "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'",
                (identifier,),
            ).fetchone()
            if row is None:
                raise ValueError(f"Missing independently grounded identifier {identifier}")
            label = row[0]
        n = {
            "id": identifier,
            "label": label,
            "category": "molecular_activity" if reaction else "small_molecule",
        }
        if reaction:
            n["direction"] = "left_to_right"
        record[section].append(n)

    def uniprot(record, accession, family, text):
        p, index = proteins[accession]
        matches = [
            (i, c)
            for i, c in enumerate(p["comments"])
            if c["commentType"] == "CATALYTIC ACTIVITY"
            and any(x["id"] == family for x in c["reaction"].get("reactionCrossReferences", []))
        ]
        if family == "FUNCTION":
            matches = [(i, c) for i, c in enumerate(p["comments"]) if c["commentType"] == family]
        if len(matches) != 1:
            raise ValueError(f"Expected exact independent annotation {accession} {family}")
        ci, _ = matches[0]
        rid = "UniProtKB:" + accession
        if not any(r["id"] == rid for r in record["references"]):
            record["references"].append(
                {
                    "id": rid,
                    "title": f"UniProtKB {accession} catalytic annotations",
                    "url": meta["url"],
                    "source_version": "2026_03",
                    "source_sha256": BATCH_SHA,
                }
            )
        return {
            "reference_id": rid,
            "source_assertion": text,
            "source_locator": f"{meta['url']} [sha256:{BATCH_SHA}] #/results/{index}/comments/{ci}",
        }

    def paper(record, pmid, title, text, locator, full=False):
        rid = "PMID:" + pmid
        if not any(r["id"] == rid for r in record["references"]):
            ref = {"id": rid, "title": title, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"}
            if full:
                ref.update(url=PAPER_URL, source_sha256=PAPER_SHA)
            record["references"].append(ref)
        return {
            "reference_id": rid,
            "source_assertion": text,
            "source_locator": (f"{PAPER_URL} [sha256:{PAPER_SHA}] " if full else "") + locator,
        }

    def replace(record, edge_id, old, new, evidence, reason):
        edge = next(e for e in record["mechanistic_edges"] if e["id"] == edge_id)
        if edge["object"] != old:
            raise ValueError(f"Changed migration baseline {edge_id}: {edge['object']} != {old}")
        edge["object"] = new
        edge["evidence"] = evidence
        edge["description"] = reason

    def add(record, identifier, subject, predicate, obj, evidence, description=None):
        if any(e["id"] == identifier for e in record["mechanistic_edges"]):
            raise ValueError(f"Already migrated: {identifier}")
        edge = {
            "id": identifier,
            "subject": subject,
            "predicate": predicate,
            "object": obj,
            "evidence": evidence,
        }
        if description:
            edge["description"] = description
        record["mechanistic_edges"].append(edge)

    for slug in ("folate-interconversions", "inositol-phosphate-biosynthesis"):
        path = root / "data/pathways" / f"{slug}.yaml"
        record = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        before = copy.deepcopy(record)
        exclusions, notes = [], []
        if slug == "folate-interconversions":
            node(record, "CHEBI:57455")
            for eid, accession, family in [
                ("edge-001", "Q02046", "RHEA:22892"),
                ("edge-052", "P07245", "RHEA:22812"),
                ("edge-051", "P07245", "RHEA:23700"),
                ("edge-080", "P09440", "RHEA:22812"),
                ("edge-090", "P09440", "RHEA:23700"),
            ]:
                ev = uniprot(
                    record,
                    accession,
                    family,
                    f"{accession} {family} distinguishes the methenyl folate CHEBI:57455 "
                    "from the methylene folate; the native GO-CAM CHEBI:20502 endpoint "
                    "incorrectly merged these oxidation states.",
                )
                replace(
                    record,
                    eid,
                    "CHEBI:20502",
                    "CHEBI:57455",
                    [ev],
                    "Corrected the methenyl endpoint; the distinct methylene input is retained.",
                )
            ev = uniprot(
                record,
                "P53128",
                "RHEA:19817",
                "MET13 methylenetetrahydrofolate reductase uses NADPH/NADP, as "
                "annotated by RHEA:19817; its reduction direction consumes NADPH.",
            )
            primary = paper(
                record,
                "11729203",
                "Metabolic engineering in yeast demonstrates that "
                "S-adenosylmethionine controls flux through the "
                "methylenetetrahydrofolate reductase reaction in vivo",
                "The experimental "
                "study identifies the yeast MET13-encoded reductase as NADPH-dependent.",
                "PubMed abstract, MET13 cofactor-specificity statement",
            )
            for eid, old, new in [
                ("edge-079", "CHEBI:57540", "CHEBI:58349"),
                ("edge-105", "CHEBI:57945", "CHEBI:57783"),
            ]:
                replace(
                    record,
                    eid,
                    old,
                    new,
                    [ev, primary],
                    "MET13 uses NADPH/NADP; the independently supported MET12 NADH branch remains.",
                )
            # These were individually inspected against the corrected chemical sides.
            # Reverse catalysis does not establish the displayed directed material flow.
            keep_flow = {"edge-007", "edge-041", "edge-058"}
            for edge in record["mechanistic_edges"]:
                if edge["predicate"] == "provides_input_for" and edge["id"] not in keep_flow:
                    exclusions.append(
                        {
                            "edge": copy.deepcopy(edge),
                            "reason": "Displayed donor outputs and acceptor inputs do not share "
                            "the required "
                            "folate intermediate after resolving methenyl/methylene states "
                            "and native "
                            "ligase direction. Reversible enzyme capacity or a shared nucleotide "
                            "cofactor does not establish this directed material-flow assertion; "
                            "no unobserved reaction reversal or compartment transport is inferred.",
                        }
                    )
            removed = {x["edge"]["id"] for x in exclusions}
            record["mechanistic_edges"] = [
                e for e in record["mechanistic_edges"] if e["id"] not in removed
            ]
            notes = [
                "All 14 activities reviewed. MET12 NADH branch retained: P46151 annotates both "
                "RHEA:19817 and RHEA:19821. Formate ligases retain native reverse chemical sides, "
                "which reversible RHEA:20221 supports. Broad folate/polyglutamate classes "
                "are not silently narrowed to monoglutamate species.",
                "Three supported native material-flow edges retained; 18 unsupported directed "
                "links quarantined with their complete original evidence.",
            ]
        else:
            for identifier in ("CHEBI:74946", "CHEBI:77983"):
                node(record, identifier)
            node(record, PP4, "a diphospho-1D-myo-inositol tetrakisphosphate")
            node(record, PP5, "diphosphoinositol pentakisphosphate")
            vip1 = uniprot(
                record,
                "Q06685",
                "RHEA:37459",
                "Vip1 adds a diphosphate at inositol "
                "position 1: RHEA:37459 produces CHEBI:74946 from inositol hexakisphosphate.",
            )
            modern = paper(
                record,
                "32303658",
                "Vip1 is a kinase and pyrophosphatase switch that "
                "regulates inositol diphosphate signaling",
                "Crystallography of the "
                "Saccharomyces cerevisiae Vip1 kinase product establishes 1-IP7; "
                "the old 4/6-IP7 assignment is incorrect.",
                "//sec[@id='s3']/p",
                full=True,
            )
            replace(
                record,
                "edge-032",
                "CHEBI:53064",
                "CHEBI:74946",
                [vip1, modern],
                "Corrected experimentally established Vip1 1-position specificity.",
            )
            vip8 = uniprot(
                record,
                "Q06685",
                "RHEA:10276",
                "Vip1 RHEA:10276 phosphorylates "
                "5-IP7 to 1,5-IP8 (CHEBI:77983), consuming ATP and a proton.",
            )
            replace(
                record,
                "edge-089",
                "CHEBI:52965",
                "CHEBI:77983",
                [vip8],
                "Corrected 1,5-bis(diphosphate) positions; the former 5,6 isomer is unsupported.",
            )
            kcs8 = uniprot(
                record,
                "Q12494",
                "RHEA:37467",
                "Kcs1 RHEA:37467 adds the 5-position "
                "diphosphate to 1-IP7 (CHEBI:74946), producing 1,5-IP8 (CHEBI:77983).",
            )
            for eid, old, new in [
                ("edge-010", "CHEBI:53064", "CHEBI:74946"),
                ("edge-025", "CHEBI:52965", "CHEBI:77983"),
            ]:
                replace(
                    record, eid, old, new, [kcs8], "Corrected the Kcs1-specific IP7/IP8 isomers."
                )
            for rid, ev in [("gomodel:RXN3O-143", vip8), ("gomodel:RXN3O-9819", kcs8)]:
                add(record, rid.split(":")[1] + "-proton", rid, "has_input", "CHEBI:15378", [ev])
            add(
                record,
                "Kcs1-1IP7-kinase",
                "SGD:S000002424",
                "enables",
                "gomodel:RXN3O-9819",
                [kcs8],
            )
            for eid, pmid, title, assertion in [
                (
                    "edge-047",
                    "11311242",
                    "The transcriptional regulator, Arg82, is a hybrid kinase "
                    "with both monophosphoinositol and diphosphoinositol "
                    "polyphosphate synthase activity",
                    "Purified Arg82 phosphorylates IP5 to two PP-InsP4 isomers: "
                    "one diphosphate plus "
                    "four monophosphates, not bis(diphosphate) InsP4.",
                ),
                (
                    "edge-023",
                    "10827188",
                    "The inositol hexakisphosphate kinase family. Catalytic "
                    "flexibility and function in yeast vacuole biogenesis",
                    "Purified yeast inositol "
                    "hexakisphosphate kinase phosphorylates IP5 to PP-InsP4; this experiment does "
                    "not establish a unique positional isomer here.",
                ),
            ]:
                ev = paper(
                    record,
                    pmid,
                    title,
                    assertion,
                    "PubMed abstract, purified kinase substrate/product results",
                )
                replace(
                    record,
                    eid,
                    "CHEBI:14178",
                    PP4,
                    [ev],
                    "Preserved the independently existing native generic PP-InsP4 entity; "
                    "its former CHEBI:14178 type has two diphosphates and is incorrect.",
                )
            ddp = uniprot(
                record,
                "Q99321",
                "FUNCTION",
                "DDP1 hydrolyzes beta-phosphates from "
                "diphosphoinositol pentakisphosphate and bis(diphosphoinositol) "
                "tetrakisphosphate. This assertion does not identify a positional isomer.",
            )
            for eid, old, new in [
                ("edge-040", "CHEBI:52965", "CHEBI:14178"),
                ("edge-062", "CHEBI:62919", PP5),
                ("edge-050", "CHEBI:62919", PP5),
            ]:
                replace(
                    record,
                    eid,
                    old,
                    new,
                    [ddp],
                    "Retained supported generic DDP1 substrates "
                    "and products without imposing unsupported pyrophosphate positions.",
                )
            for edge in record["mechanistic_edges"]:
                if edge["id"] in {"edge-020", "edge-053"}:
                    exclusions.append(
                        {
                            "edge": copy.deepcopy(edge),
                            "reason": "The same proton occurs on both native sides and cancels "
                            "in the net "
                            "Kcs1 IP6-kinase equation RHEA:12793; no proton turnover is asserted.",
                        }
                    )
            record["mechanistic_edges"] = [
                e for e in record["mechanistic_edges"] if e["id"] not in {"edge-020", "edge-053"}
            ]
            labels = {
                "gomodel:RXN3O-258": "ATP + inositol hexakisphosphate -> ADP + 1-IP7",
                "gomodel:RXN3O-143": "ATP + 5-IP7 + H(+) -> ADP + 1,5-IP8",
                "gomodel:RXN3O-9819": "ATP + 1-IP7 + H(+) -> ADP + 1,5-IP8",
                "gomodel:2.7.1.152-RXN": "ATP + inositol hexakisphosphate -> ADP + 5-IP7",
            }
            for reaction in record["reactions"]:
                if reaction["id"] in labels:
                    reaction["label"] = labels[reaction["id"]]
            node(record, "RHEA:79724", reaction=True)
            phys = paper(
                record,
                "32303658",
                "Vip1 is a kinase and pyrophosphatase switch that "
                "regulates inositol diphosphate signaling",
                "The recombinant S. cerevisiae "
                "Vip1 pyrophosphatase domain hydrolyzes 1-IP7 but not 3-IP7 in vitro. "
                "This is domain-assay evidence, not an assertion of physiological flux.",
                "//sec[@id='s5']/p[2]; //sec[@id='s5']/p[3]; //fig[@id='fig03']; Table 2",
                full=True,
            )
            add(
                record,
                "Vip1-1IP7-phosphatase",
                "SGD:S000004402",
                "enables",
                "RHEA:79724",
                [phys],
                "In-vitro recombinant pyrophosphatase-domain activity; no cellular flux or "
                "S. pombe phenotype is projected onto S. cerevisiae.",
            )
            record["references"].append(
                {
                    "id": "RHEA:79724",
                    "title": "Rhea 1-IP7 hydrolysis reaction",
                    "url": "https://www.rhea-db.org/rhea/79724",
                    "source_version": "139",
                }
            )
            for predicate, ids in [
                ("has_input", ["CHEBI:74946", "CHEBI:15377"]),
                ("has_output", ["CHEBI:58130", "CHEBI:43474", "CHEBI:15378"]),
            ]:
                for identifier in ids:
                    ev = {
                        "reference_id": "RHEA:79724",
                        "source_assertion": "RHEA:79724 hydrolyzes 1-IP7 and water to "
                        "inositol hexakisphosphate, "
                        "phosphate and a proton.",
                        "source_locator": "Rhea release 139 RDF: 79724 side "
                        f"79723_{'L' if predicate == 'has_input' else 'R'}; "
                        f"contains/compound/accession {identifier}",
                    }
                    add(
                        record,
                        f"Vip1-hydrolysis-{predicate}-{identifier.split(':')[1]}",
                        "RHEA:79724",
                        predicate,
                        identifier,
                        [ev],
                    )
            notes = [
                "All 14 original activities reviewed; one experimentally supported recombinant "
                "Vip1 pyrophosphatase-domain activity added. Native IPMK intermediate steps "
                "are retained rather than replaced by an aggregate Rhea equation.",
                "PP4 native ID authenticates ./YeastPathways_PWY3O-402.json#/individuals/0 "
                "and /facts/46; PP5 authenticates /individuals/46 and /facts/49,/facts/61. "
                "These source-local generic entities do not claim unique chemical structures.",
                "CHEBI:187038 was rejected despite its promising PP-InsP4 label: its ChEBI255 "
                "SMILES/InChI encode six monophosphates. No structure identity was guessed.",
                "UniProt Q06685 CAUTION denying phosphatase activity is superseded for the "
                "tested recombinant domain by PMID:32303658; no S. pombe in-vivo phenotype "
                "or untested yeast IP8 hydrolysis was imported.",
            ]
        used = {e[k] for e in record["mechanistic_edges"] for k in ("subject", "object")}
        record["participants"] = [n for n in record["participants"] if n["id"] in used]
        validate_record(record)
        ledger.append(
            {
                "path": str(path.relative_to(root)),
                "activities_before": len(before["reactions"]),
                "activities_after": len(record["reactions"]),
                "activities_reviewed": activity_audit(record, proteins),
                "notes": notes,
                "source_exclusions": exclusions,
                "changed_original_edges": [
                    e for e in before["mechanistic_edges"] if e not in record["mechanistic_edges"]
                ],
                "corrected_or_added_edges": [
                    e for e in record["mechanistic_edges"] if e not in before["mechanistic_edges"]
                ],
            }
        )
        pending.append((path, record))
    report = report or root / "reports/causal_graph_review/folate-inositol-chemistry-review.json"
    publish_curation(
        pending,
        report,
        {"uniprot_sha256": BATCH_SHA, "primary_xml_sha256": PAPER_SHA, "records": ledger},
        apply=apply,
        serialize=lambda record: yaml.dump(
            record,
            Dumper=IndentedDumper,
            sort_keys=False,
            allow_unicode=True,
            width=100,
        ),
    )
    return ledger


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--chebi-db", type=Path, required=True)
    parser.add_argument("--rhea-db", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    print(
        json.dumps(
            curate(
                args.root, args.source_dir, args.chebi_db, args.rhea_db, args.apply, args.report
            ),
            indent=2,
        )
    )
