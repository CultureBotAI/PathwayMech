#!/usr/bin/env python3
"""Apply the source-reviewed October 2026 MetaCyc graph corrections.

This is a reproducible, bounded curation migration, not an importer. All source
arguments are required; labels come from independent authorities. The companion
audit and report describe selection limits and the manually reviewed expansions.
Run against an unchanged checkout to reproduce the original before/after ledger.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET

import yaml
from audit_metacyc_causal_graphs import read_pathway, read_rhea

EXPANSIONS = {
    "RHEA:22109": ["RHEA:40676", "RHEA:39968", "RHEA:39976"],
    "RHEA:32289": ["RHEA:16295", "RHEA:10678"],
    "RHEA:32272": ["RHEA:10893", "RHEA:25079"],
    "RHEA:13966": ["RHEA:43021", "RHEA:40668", "RHEA:40672"],
    "RHEA:10533": ["RHEA:14082", "RHEA:26435"],
    "RHEA:10154": ["RHEA:30757", "RHEA:15650"],
}
# Catalysis applies to the enzyme-mediated substeps, not spontaneous subsequent
# tautomerization/hydrolysis. RidA is added separately only if UniProt matches.
CATALYTIC_STEPS = {
    "RHEA:22109": ["RHEA:40676"],
    "RHEA:32289": ["RHEA:16295", "RHEA:10678"],
    "RHEA:32272": ["RHEA:10893"],
    "RHEA:13966": ["RHEA:43021"],
    "RHEA:10533": ["RHEA:14082", "RHEA:26435"],
    "RHEA:10154": ["RHEA:30757"],
}
ADDITIONS = {
    "MetaCyc:GLYOXYLATE-BYPASS": {
        "RHEA:16846": "EC:2.3.3.1",
        "RHEA:10229": "EC:4.2.1.3",
        "RHEA:22145": "EC:4.2.1.3",
        "RHEA:21433": "EC:1.1.1.37",
    },
    "MetaCyc:ARGSYN-PWY": {"RHEA:18634": "EC:6.3.5.5"},
}
PREFERRED_TAXA = {
    "562": 83333,
    "1773": 83332,
    "287": 208964,
    "2242": 64091,
    "2336": 243274,
    "2746": 768066,
    "158": 243275,
}
COMPONENT_PARENTS = {"RHEA:33800": "RHEA:20641", "RHEA:33804": "RHEA:20641"}
CURRENCY = {
    "CHEBI:15377",
    "CHEBI:15378",
    "CHEBI:30616",
    "CHEBI:456216",
    "CHEBI:57540",
    "CHEBI:57945",
    "CHEBI:58349",
    "CHEBI:57783",
    "CHEBI:43474",
    "CHEBI:57287",
    "CHEBI:456215",
    "CHEBI:28938",
}
# Explicitly reviewed physiological metabolite feedback, grounded to the
# protein's ACTIVITY REGULATION annotation; no sign is guessed from a name.
REGULATION = {
    "P00561": [("CHEBI:57926", "regulates")],
    "P00893": [("CHEBI:57762", "inhibits")],
    "P00894": [("CHEBI:57762", "inhibits")],
    "P00904": [("CHEBI:57912", "inhibits")],
    "P00895": [("CHEBI:57912", "inhibits")],
    "P00888": [("CHEBI:58315", "inhibits")],
    "P0AF18": [("CHEBI:58725", "inhibits"), ("CHEBI:30089", "inhibits")],
    "P04968": [("CHEBI:58045", "inhibits"), ("CHEBI:57762", "activates")],
    "P08660": [("CHEBI:32551", "inhibits")],
    "P0A6I6": [("CHEBI:57287", "inhibits")],
    "P0A6I3": [("CHEBI:57287", "inhibits")],
    "P0A6L2": [("CHEBI:32551", "inhibits")],
    "P0A759": [("CHEBI:57513", "activates")],
    "P0A6C5": [("CHEBI:32682", "inhibits")],
    "P0A7B5": [("CHEBI:60039", "inhibits"), ("CHEBI:456216", "inhibits")],
    "P0A9J8": [("CHEBI:58095", "inhibits")],
    "P0A9T0": [("CHEBI:33384", "inhibits")],
    "P0A9D4": [("CHEBI:35235", "inhibits")],
    "P60757": [("CHEBI:57595", "inhibits"), ("CHEBI:456215", "inhibits")],
    "P9WK17": [("CHEBI:15589", "inhibits")],
    "Q48296": [("CHEBI:32682", "activates")],
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assertion(reference, text, locator):
    if len(text) > 400:
        raise ValueError(f"Overlong evidence assertion ({len(text)}): {text}")
    return {"reference_id": reference, "source_assertion": text, "source_locator": locator}


def norm(text):
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(".")


def labels_from_db(path):
    connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)

    def label(identifier):
        row = connection.execute(
            "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'",
            (identifier,),
        ).fetchone()
        if not row or not row[0]:
            raise ValueError(f"Independent authority has no label for {identifier}")
        return row[0]

    return label


def enzyme_records(path):
    result = {}
    for entry in path.read_text().split("//\n"):
        match = re.search(r"^ID   (.+)$", entry, re.M)
        if match:
            result["EC:" + match[1]] = {
                "label": " ".join(
                    line[5:] for line in entry.splitlines() if line.startswith("DE   ")
                ).rstrip("."),
                "comment": " ".join(
                    line[5:].strip() for line in entry.splitlines() if line.startswith("CC   ")
                ),
            }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    for name in [
        "rhea-rdf",
        "directions",
        "metacyc-dir",
        "chebi-db",
        "go-db",
        "enzyme-dat",
        "pubmed-xml",
        "additional-pubmed-xml",
        "uniprot-dir",
        "report-dir",
    ]:
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--baseline-ref", help="Read records at an explicit Git revision for repeatable migration"
    )
    args = parser.parse_args()
    records = []
    for path in sorted((args.root / "data/pathways").rglob("*.yaml")):
        content = (
            subprocess.check_output(
                ["git", "show", args.baseline_ref + ":" + str(path.relative_to(args.root))],
                cwd=args.root,
                text=True,
            )
            if args.baseline_ref
            else path.read_text()
        )
        record = yaml.load(content, Loader=yaml.CSafeLoader)
        if record["id"].startswith("MetaCyc:"):
            records.append((path, record))
    if len(records) != 50:
        raise ValueError(f"This reviewed migration expects 50 MetaCyc records, got {len(records)}")
    selected = {
        node["id"].split(":")[1]
        for _, r in records
        for node in r["reactions"]
        if node["id"].startswith("RHEA:")
    }
    selected.update(r.split(":")[1] for values in EXPANSIONS.values() for r in values)
    selected.update(r.split(":")[1] for values in ADDITIONS.values() for r in values)
    families, directions = {}, {}
    with args.directions.open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            for key, value in row.items():
                families["RHEA:" + value] = "RHEA:" + row["RHEA_ID_MASTER"]
                directions["RHEA:" + value] = {
                    "RHEA_ID_MASTER": None,
                    "RHEA_ID_LR": "left_to_right",
                    "RHEA_ID_RL": "right_to_left",
                    "RHEA_ID_BI": "reversible",
                }[key]
            if selected.intersection(row.values()):
                selected.update(row.values())
    rhea = read_rhea(args.rhea_rdf, args.directions, selected)
    chebi_label = labels_from_db(args.chebi_db)
    go_label = labels_from_db(args.go_db)
    enzymes = enzyme_records(args.enzyme_dat)
    articles = {}
    for path in (args.pubmed_xml, args.additional_pubmed_xml):
        for article in ET.parse(path).getroot():
            pmid = "PMID:" + article.findtext(".//PMID")
            articles[pmid] = {
                "title": "".join(article.find(".//ArticleTitle").itertext()),
                "abstract": " ".join(
                    "".join(x.itertext()) for x in article.findall(".//AbstractText")
                ),
            }
    proteins = {}
    protein_sources = {}
    location_sources, location_mappings = {}, {}
    for sl in ("SL-0086", "SL-0039"):
        artifact = args.uniprot_dir.parent / (sl + ".json")
        location_record = json.loads(artifact.read_text())
        if location_record["id"] != sl or len(location_record["geneOntologies"]) != 1:
            raise ValueError(f"Ambiguous UniProt location mapping: {artifact}")
        location_mappings[sl] = location_record["geneOntologies"][0]["goId"]
        location_sources[sl] = {
            "url": "https://rest.uniprot.org/locations/" + sl + ".json",
            "sha256": digest(artifact),
        }
    protein_manifest = json.loads((args.uniprot_dir / "manifest.json").read_text())
    for key, source in protein_manifest.items():
        artifact = args.uniprot_dir / (key + ".json")
        if digest(artifact) != source["sha256"]:
            raise ValueError(f"UniProt artifact checksum mismatch: {artifact}")
        for protein in json.loads(artifact.read_text())["results"]:
            proteins["UniProtKB:" + protein["primaryAccession"]] = protein
            protein_sources["UniProtKB:" + protein["primaryAccession"]] = source
    ledger = []
    identifiers = set()
    for path, record in records:
        before = json.loads(json.dumps(record))
        native_id = record["id"].split(":")[1]
        primary_path = args.metacyc_dir / (native_id + ".xml")
        primary = read_pathway(primary_path)
        references = {r["id"]: r for r in record["references"]}
        nodes = {n["id"]: n for n in record["participants"]}
        reactions = {n["id"]: n for n in record["reactions"]}
        review = {
            "id": record["id"],
            "path": str(path.relative_to(args.root)),
            "native_species": primary["species"],
            "native_taxonomic_range": primary["taxonomic_range"],
            "native_layouts": primary["layouts"],
            "record_taxa": record["taxa"],
            "direction_changes": {},
            "expanded_reactions": {},
            "added_reactions": [],
            "protein_annotations": [],
            "cofactor_annotations": [],
            "regulatory_annotations": [],
            "location_annotations": [],
            "annotation_cautions": [],
            "literature_evidence": [],
            "ordering_specificity_bridges": [],
        }

        def reference(identifier, references=references):
            if identifier not in references:
                references[identifier] = {
                    "id": identifier,
                    "title": identifier + " authority record",
                }
            item = references[identifier]
            if identifier.startswith("RHEA:"):
                item.update(
                    url="https://www.rhea-db.org/rhea/" + identifier.split(":")[1],
                    source_version="139",
                )
            elif identifier.startswith("MetaCyc:"):
                file = args.metacyc_dir / (identifier.split(":")[1] + ".xml")
                if file.exists():
                    item.update(
                        url="https://pathway.yeastgenome.org/getxml?id=META:"
                        + identifier.split(":")[1]
                        + "&detail=full",
                        source_version="22.5",
                        source_sha256=digest(file),
                    )
            elif identifier.startswith("EC:"):
                item.update(
                    url="https://enzyme.expasy.org/EC/" + identifier.split(":")[1],
                    source_version="02-Sep-2026",
                )
            elif identifier.startswith("PMID:"):
                item["url"] = "https://pubmed.ncbi.nlm.nih.gov/" + identifier.split(":")[1] + "/"
            elif identifier.startswith("UniProtKB:"):
                item.update(
                    url="https://rest.uniprot.org/uniprotkb/" + identifier.split(":")[1] + ".json",
                    source_version="2026_03",
                )
            return identifier

        def node(identifier, category=None, nodes=nodes):
            if identifier not in nodes:
                if identifier.startswith("CHEBI:"):
                    label = chebi_label(identifier)
                elif identifier.startswith("EC:"):
                    label = enzymes[identifier]["label"]
                elif identifier.startswith("GO:"):
                    label = go_label(identifier)
                else:
                    label = proteins[identifier]["proteinDescription"]["recommendedName"][
                        "fullName"
                    ]["value"]
                nodes[identifier] = {"id": identifier, "label": label}
            if category:
                nodes[identifier]["category"] = category

        for n in nodes.values():
            n["category"] = (
                "molecular_activity"
                if n["id"].startswith("EC:")
                else ("protein" if n["id"].startswith("UniProtKB:") else "small_molecule")
            )
        edge_list = []

        def add(subject, predicate, obj, evidence, edge_list=edge_list):
            edge_list.append(
                {"subject": subject, "predicate": predicate, "object": obj, "evidence": evidence}
            )

        # Resolve reversible identifiers to the source-supported pathway flow.
        replacements = {}
        for rid in list(reactions):
            if rid in rhea and directions[rid] == "reversible":
                inputs = sorted(
                    e["subject"]
                    for e in record["mechanistic_edges"]
                    if e["predicate"] == "consumes" and e["object"] == rid
                )
                outputs = sorted(
                    e["object"]
                    for e in record["mechanistic_edges"]
                    if e["predicate"] == "produces" and e["subject"] == rid
                )
                matches = [
                    key
                    for key, value in rhea.items()
                    if value["master"] == families[rid]
                    and value["sides"].get("substrates") == inputs
                    and value["sides"].get("products") == outputs
                    and directions[key] in {"left_to_right", "right_to_left"}
                    and "http://rdf.rhea-db.org/DirectionalReaction" in value["types"]
                ]
                if len(matches) != 1:
                    raise ValueError(f"Cannot uniquely orient {record['id']} {rid}: {matches}")
                replacements[rid] = matches[0]
                review["direction_changes"][rid] = matches[0]
        for edge in record["mechanistic_edges"]:
            edge["subject"] = replacements.get(edge["subject"], edge["subject"])
            edge["object"] = replacements.get(edge["object"], edge["object"])
        for old, new in replacements.items():
            reactions[new] = {**reactions.pop(old), "id": new}

        original_catalysts = {}
        for edge in record["mechanistic_edges"]:
            if edge["predicate"] == "catalyzes":
                original_catalysts.setdefault(edge["object"], []).append(edge)
        expansion = {old: new for old, new in EXPANSIONS.items() if old in reactions}
        review["expanded_reactions"] = expansion
        for old, new_ids in expansion.items():
            del reactions[old]
            for rid in new_ids:
                reactions[rid] = {"id": rid, "label": rhea[rid]["label"][0]}
        for rid, ec in ADDITIONS.get(record["id"], {}).items():
            reactions[rid] = {"id": rid, "label": rhea[rid]["label"][0]}
            node(ec, "molecular_activity")
            original_catalysts[rid] = [{"subject": ec, "object": rid, "evidence": []}]
            review["added_reactions"].append(rid)

        # Reaction sides are reconstructed from Rhea, not from old display labels.
        for rid, reaction in reactions.items():
            if rid not in rhea:
                # The only native reaction is the explicitly sourced spontaneous
                # rhamnulose cyclization; preserve its broader product class.
                if rid != "MetaCyc:RXN-15356":
                    raise ValueError(f"Unexpected non-Rhea reaction {rid}")
                reaction["direction"] = "left_to_right"
                for edge in record["mechanistic_edges"]:
                    if edge["predicate"] in {"consumes", "produces"} and rid in (
                        edge["subject"],
                        edge["object"],
                    ):
                        evidence = assertion(
                            reference(rid),
                            (
                                f"MetaCyc assigns {edge['subject']} {edge['predicate']} "
                                f"{edge['object']} in the spontaneous rhamnulose cyclization."
                            ),
                            (
                                "Reaction[@frameid='RXN-15356']/left|right; native compound "
                                "cross-references"
                            ),
                        )
                        add(edge["subject"], edge["predicate"], edge["object"], [evidence])
                continue
            reaction["direction"] = directions[rid]
            if directions[rid] not in {"left_to_right", "right_to_left"}:
                raise ValueError(f"Reaction flow still ambiguous: {rid}")
            for kind, predicate in [("substrates", "consumes"), ("products", "produces")]:
                for chemical in rhea[rid]["sides"][kind]:
                    node(chemical, nodes.get(chemical, {}).get("category", "small_molecule"))
                    subject, obj = (chemical, rid) if kind == "substrates" else (rid, chemical)
                    add(
                        subject,
                        predicate,
                        obj,
                        [
                            assertion(
                                reference(rid),
                                (
                                    f"Rhea lists {chemical} on the {kind} side of {rid} in this "
                                    f"directed reaction."
                                ),
                                (
                                    f"rdf:Description[@rdf:about='http://rdf.rhea-db.org/"
                                    f"{rid.split(':')[1]}']/rh:{kind}; "
                                    f"rh:contains/rh:compound/rh:accession"
                                ),
                            )
                        ],
                    )

        # Existing catalysis evidence is preserved when its exact title/abstract
        # text can be verified. Structured evidence is explicitly an assertion.
        for old, catalysts in original_catalysts.items():
            targets = CATALYTIC_STEPS.get(old, [old])
            for rid in targets:
                for catalyst in catalysts:
                    ec = catalyst["subject"]
                    if ec.startswith("EC:") and ec in rhea[rid]["ec"]:
                        ev = [
                            assertion(
                                reference(rhea[rid]["master"]),
                                f"Rhea associates {ec} with the reaction family containing {rid}.",
                                "rh:ec",
                            )
                        ]
                    else:
                        ev = [
                            assertion(
                                reference(record["id"]),
                                (
                                    f"The native pathway assigns {ec} activity to the "
                                    f"enzymatic step "
                                    f"represented by {rid}; this is a component step when the EC "
                                    f"definition is an overall reaction."
                                ),
                                (
                                    "Pathway/reaction-layout; Reaction/enzymatic-reaction and "
                                    "component-reaction relationships"
                                ),
                            )
                        ]
                    for item in catalyst.get("evidence", []):
                        ref, quote = item["reference_id"], item.get("quote", "")
                        if not ref.startswith("PMID:") or not quote:
                            continue
                        article = articles.get(ref, {})
                        location = next(
                            (
                                field
                                for field in ["title", "abstract"]
                                if norm(quote) in norm(article.get(field, ""))
                            ),
                            None,
                        )
                        if ref == "PMID:4976555":
                            location = None
                            review["annotation_cautions"].append(
                                {
                                    "reference": ref,
                                    "decision": (
                                        "Removed Salmonella typhimurium article-title evidence "
                                        "from the E. coli enzyme edge; E. coli catalysis is "
                                        "supported separately "
                                        "by MetaCyc and UniProt."
                                    ),
                                }
                            )
                        if location:
                            ev.append(
                                {
                                    "reference_id": reference(ref),
                                    "quote": quote,
                                    "source_locator": "PubMed ArticleTitle"
                                    if location == "title"
                                    else "PubMed Abstract",
                                }
                            )
                        review["literature_evidence"].append(
                            {
                                "reference": ref,
                                "quote": quote,
                                "verified_location": location,
                                "retained": bool(location),
                            }
                        )
                    add(ec, "catalyzes", rid, ev)

        # Explicit ordering is supported by the pathway layout. Expansions add
        # intermediate flow without retaining a duplicate overall reaction.
        links = set()

        def sides(rid, side):
            return set(rhea.get(rid, {}).get("sides", {}).get(side, []))

        for edge in record["mechanistic_edges"]:
            if edge["predicate"] != "precedes":
                continue
            lefts, rights = (
                expansion.get(edge["subject"], [edge["subject"]]),
                expansion.get(edge["object"], [edge["object"]]),
            )
            matches = [
                (a, b)
                for a in lefts
                for b in rights
                if (sides(a, "products") & sides(b, "substrates")) - CURRENCY
            ]
            links.update(matches or [(lefts[-1], rights[0])])
        for series in expansion.values():
            links.update(zip(series, series[1:], strict=False))
        if record["id"] == "MetaCyc:GLYOXYLATE-BYPASS":
            series = [
                "RHEA:16846",
                "RHEA:10229",
                "RHEA:22145",
                "RHEA:13246",
                "RHEA:18182",
                "RHEA:21433",
                "RHEA:16846",
            ]
            links.update(zip(series, series[1:], strict=False))
            record["description"] = (
                "The glyoxylate cycle assimilates acetyl-CoA through citrate "
                "synthase, aconitase, isocitrate lyase and malate synthase. "
                "Malate dehydrogenase regenerates oxaloacetate, closing the "
                "cycle while succinate is released. Enzyme activities have been "
                "demonstrated in Mycobacterium tuberculosis."
            )
            reference("PMID:16027371")
        if record["id"] == "MetaCyc:ARGSYN-PWY":
            consumers = [rid for rid in reactions if "CHEBI:58228" in sides(rid, "substrates")]
            links.update(("RHEA:18634", rid) for rid in consumers)
        for subject, obj in sorted(links):
            shared = sorted((sides(subject, "products") & sides(obj, "substrates")) - CURRENCY)
            note = (
                (" Shared intermediate: " + ", ".join(shared) + ".")
                if shared
                else (
                    " The source ordering may bridge anomer-specific and broader substrate classes."
                )
            )
            if not shared:
                review["ordering_specificity_bridges"].append([subject, obj])
            add(
                subject,
                "precedes",
                obj,
                [
                    assertion(
                        reference(record["id"]),
                        f"MetaCyc pathway ordering places {subject} before {obj} in this pathway."
                        + note,
                        (
                            "Pathway/reaction-ordering and reaction-layout; Rhea-to-MetaCyc "
                            "cross-references"
                        ),
                    )
                ],
            )

        # Named proteins are restricted to a reviewed reference strain within
        # the existing species scope and to an exact catalytic Rhea family.
        allowed_taxa = {
            PREFERRED_TAXA[t["id"].split(":")[1]]
            for t in record["taxa"]
            if t["id"].split(":")[1] in PREFERRED_TAXA
        }
        for pid, protein in sorted(proteins.items()):
            if protein["organism"]["taxonId"] not in allowed_taxa:
                continue
            matched = []
            for comment in protein.get("comments", []):
                if comment["commentType"] != "CATALYTIC ACTIVITY":
                    continue
                masters = {
                    families.get(x["id"], x["id"])
                    for x in comment["reaction"].get("reactionCrossReferences", [])
                    if x["database"] == "Rhea"
                }
                for rid in reactions:
                    direct_match = rid in rhea and rhea[rid]["master"] in masters
                    component_match = any(
                        families[old] in masters and rid in CATALYTIC_STEPS[old]
                        for old in expansion
                    )
                    component_match = component_match or COMPONENT_PARENTS.get(rid) in masters
                    if direct_match or component_match:
                        matched.append((rid, comment, component_match and not direct_match))
            if pid == "UniProtKB:P00893" and record["id"] == "MetaCyc:ILEUSYN-PWY":
                matched.append(
                    (
                        "RHEA:27655",
                        {
                            "reaction": {"evidences": [{"evidenceCode": "ECO:0000269"}]},
                            "literature": "PMID:2675968",
                        },
                        False,
                    )
                )
            if not matched:
                continue
            if pid == "UniProtKB:P0DP90":
                review["annotation_cautions"].append(
                    {
                        "protein": pid,
                        "decision": (
                            "Excluded repaired ilvG frameshift mutant; the ordinary K12 "
                            "gene is disrupted."
                        ),
                        "source_locator": "comments[commentType='MISCELLANEOUS']",
                    }
                )
                continue
            if pid == "UniProtKB:P0A7B5":
                review["annotation_cautions"].append(
                    {
                        "protein": pid,
                        "decision": (
                            "Did not add the suggested ProB-ProA interaction/channeling "
                            "requirement: primary PMID:39514317 demonstrates that "
                            "channeling is unnecessary in E. coli."
                        ),
                        "source_locator": (
                            "UniProt ACTIVITY REGULATION versus PMID:39514317 Abstract"
                        ),
                    }
                )
            node(pid, "protein")
            for rid, comment, component in matched:
                codes = sorted(
                    {e["evidenceCode"] for e in comment["reaction"].get("evidences", [])}
                )
                relationship = (
                    "the overall reaction containing the native MetaCyc enzymatic component "
                    if component
                    else "the reaction family of "
                )
                if comment.get("literature"):
                    evidence = [
                        assertion(
                            reference(comment["literature"]),
                            (
                                "The study directly measures E. coli acetohydroxy acid synthase "
                                "III producing acetohydroxybutyrate from pyruvate and "
                                "2-ketobutyrate; UniProt identifies its catalytic subunit as "
                                "P00893."
                            ),
                            (
                                "PubMed Abstract; AHAS isozyme III kinetics; UniProt "
                                "proteinDescription and genes"
                            ),
                        )
                    ]
                    reference(pid)
                else:
                    evidence = [
                        assertion(
                            reference(pid),
                            (
                                f"UniProt annotates {pid} with catalytic activity for "
                                f"{relationship}{rid}. Annotation evidence: "
                                f"{', '.join(codes) or 'curated source annotation'}; organism "
                                f"taxon: NCBITaxon:{protein['organism']['taxonId']}."
                            ),
                            (
                                "comments[commentType='CATALYTIC "
                                "ACTIVITY'].reaction.reactionCrossReferences"
                            ),
                        )
                    ]
                add(pid, "enables", rid, evidence)
            review["protein_annotations"].append(
                {
                    "id": pid,
                    "taxon": protein["organism"],
                    "reactions": sorted({r for r, _, _ in matched}),
                }
            )
            for comment in protein.get("comments", []):
                if comment["commentType"] == "SUBCELLULAR LOCATION":
                    for location in comment.get("subcellularLocations", []):
                        loc = location.get("location", {})
                        go = location_mappings.get(loc.get("id"))
                        if go:
                            node(go, "cellular_component")
                            codes = sorted({e["evidenceCode"] for e in loc.get("evidences", [])})
                            add(
                                pid,
                                "located_in",
                                go,
                                [
                                    assertion(
                                        reference(pid),
                                        (
                                            f"UniProt locates {pid} in {loc['value']} "
                                            f"({loc['id']}, mapped "
                                            f"by UniProt to {go}). Annotation evidence: "
                                            f"{', '.join(codes) or 'curated source annotation'}."
                                        ),
                                        (
                                            "comments[commentType='SUBCELLULAR "
                                            "LOCATION'].subcellularLocations; UniProt location "
                                            "vocabulary "
                                            "GO mapping"
                                        ),
                                    )
                                ],
                            )
                            review["location_annotations"].append(
                                {"protein": pid, "go": go, "annotation": location}
                            )
                if comment["commentType"] != "ACTIVITY REGULATION":
                    continue
                text = " ".join(t["value"] for t in comment.get("texts", []))
                review["regulatory_annotations"].append(
                    {
                        "protein": pid,
                        "source_text": text,
                        "added": REGULATION.get(protein["primaryAccession"], []),
                    }
                )
                for cid, predicate in REGULATION.get(protein["primaryAccession"], []):
                    node(cid, nodes.get(cid, {}).get("category", "small_molecule"))
                    # The ProB interaction claim in this annotation is outdated
                    # (PMID:39514317); retain only its independent inhibitor statement.
                    excerpt = (
                        "Inhibited by proline and ADP"
                        if protein["primaryAccession"] == "P0A7B5"
                        else text
                    )
                    if len(excerpt) > 300:
                        excerpts = {
                            "P0AF18": (
                                "Inhibited by high substrate concentration and by products "
                                "glucosamine 6-phosphate and acetate."
                            ),
                            "P0A6I6": (
                                "Feedback inhibited by CoA, which is competitive with ATP, "
                                "4'-phosphopantetheine and 3'-dephospho-CoA."
                            ),
                        }
                        excerpt = excerpts[protein["primaryAccession"]]
                    add(
                        cid,
                        predicate,
                        pid,
                        [
                            assertion(
                                reference(pid),
                                f"UniProt activity-regulation annotation: {excerpt}",
                                "comments[commentType='ACTIVITY REGULATION'].texts",
                            )
                        ],
                    )
            for comment in protein.get("comments", []):
                if comment["commentType"] != "COFACTOR":
                    continue
                full_note = " ".join(t["value"] for t in comment.get("note", {}).get("texts", []))
                for cofactor in comment.get("cofactors", []):
                    xref = cofactor.get("cofactorCrossReference", {})
                    if xref.get("database") != "ChEBI":
                        continue
                    cid = xref["id"]
                    if pid in {"UniProtKB:P00561", "UniProtKB:P00562"} and cid == "CHEBI:25213":
                        review["annotation_cautions"].append(
                            {
                                "protein": pid,
                                "decision": (
                                    "No has_cofactor edge for the tentative metal-cation "
                                    "annotation: the source only observes sodium in a structure "
                                    "and proposes a possible effect on stability or activity."
                                ),
                                "source_locator": "comments[commentType='COFACTOR'].note",
                            }
                        )
                        continue
                    if pid == "UniProtKB:P05791" and cid == "CHEBI:190135":
                        cid = "CHEBI:30408"
                        full_note = (
                            "Cluster nuclearity is left unspecified: the current UniProt "
                            "annotation infers [2Fe-2S], while its caution cites older E. "
                            "coli [4Fe-4S] evidence and a later M. tuberculosis result."
                        )
                        review["annotation_cautions"].append(
                            {
                                "protein": pid,
                                "decision": full_note,
                                "source_locator": (
                                    "comments[commentType='CAUTION']; PMID:7771772; PMID:8325851"
                                ),
                            }
                        )
                    codes = sorted({e["evidenceCode"] for e in cofactor.get("evidences", [])})
                    base = (
                        f"UniProt lists {cid} as a cofactor of {pid} (evidence: "
                        f"{', '.join(codes) or 'curated annotation'})."
                    )
                    # Long notes remain fully preserved in the ledger. The edge
                    # describes a source annotation, not universal necessity.
                    text = base + (
                        " " + full_note
                        if len(base + " " + full_note) <= 400
                        else (
                            " The source note qualifies cofactor use; see the complete "
                            "annotation in the review ledger."
                        )
                    )
                    node(cid, "cofactor")
                    add(
                        pid,
                        "has_cofactor",
                        cid,
                        [
                            assertion(
                                reference(pid),
                                text,
                                "comments[commentType='COFACTOR'].cofactors and note",
                            )
                        ],
                    )
                    review["cofactor_annotations"].append(
                        {"protein": pid, "cofactor": cid, "annotation": cofactor, "note": full_note}
                    )
        if record["id"] == "MetaCyc:PWY-6124":
            ev = assertion(
                reference("PMID:21548610"),
                (
                    "The study demonstrates AIR carboxylase activity of class II "
                    "PurE in Treponema denticola, supporting the direct AIR-to-CAIR "
                    "route in this bacterial taxon."
                ),
                "PubMed Abstract; purified TdPurE catalytic activity",
            )
            for edge in edge_list:
                if edge["predicate"] == "catalyzes" and edge["subject"] == "EC:4.1.1.21":
                    edge["evidence"].append(ev)
        if record["id"] == "MetaCyc:HISTSYN-PWY":
            for edge in edge_list:
                if edge["predicate"] == "catalyzes" and edge["object"] in COMPONENT_PARENTS:
                    edge["evidence"].append(
                        assertion(
                            reference("PMID:11842181"),
                            (
                                "The study describes E. coli HisD catalyzing sequential "
                                "NAD-dependent oxidations of histidinol to histidinaldehyde and "
                                "then histidine."
                            ),
                            "PubMed Abstract; sequential HisD reactions",
                        )
                    )
        if record["id"] == "MetaCyc:GLYOXYLATE-BYPASS":
            for edge in edge_list:
                if edge["predicate"] == "catalyzes" and edge["subject"] in {
                    "EC:2.3.3.1",
                    "EC:4.2.1.3",
                    "EC:1.1.1.37",
                }:
                    edge["evidence"].append(
                        assertion(
                            reference("PMID:16027371"),
                            (
                                "The study measured citrate synthase, aconitase and malate "
                                "dehydrogenase activities in Mycobacterium tuberculosis "
                                "lysates."
                            ),
                            "PubMed Abstract; enzyme activity measurements",
                        )
                    )
        # Keep pre-existing node IDs, including class nodes, and the source
        # bibliography. Deduplicate exactly identical graph triples.
        merged = {}
        for edge in edge_list:
            key = (edge["subject"], edge["predicate"], edge["object"])
            if key not in merged:
                merged[key] = edge
            else:
                for item in edge["evidence"]:
                    if item not in merged[key]["evidence"]:
                        merged[key]["evidence"].append(item)
        record["mechanistic_edges"] = [
            {"id": f"edge-{i:03d}", **edge} for i, edge in enumerate(merged.values(), 1)
        ]
        record["participants"] = list(nodes.values())
        record["reactions"] = list(reactions.values())
        for ref in list(references):
            reference(ref)
        record["references"] = list(references.values())
        review["before_counts"] = {
            k: len(before[k]) for k in ("participants", "reactions", "mechanistic_edges")
        }
        review["after_counts"] = {
            k: len(record[k]) for k in ("participants", "reactions", "mechanistic_edges")
        }
        review["reaction_checks"] = [
            {
                "id": rid,
                "direction": n["direction"],
                "source": rhea.get(rid, {"native": "MetaCyc:RXN-15356"}),
            }
            for rid, n in reactions.items()
        ]

        def leaf_layouts(native):
            source = read_pathway(args.metacyc_dir / (native + ".xml"))
            leaves = {}
            for key, layout in source["layouts"].items():
                if layout["kind"] == "Pathway":
                    leaves.update(leaf_layouts(key))
                else:
                    leaves[key] = layout
            return leaves

        leaves = leaf_layouts(native_id)
        review["native_reaction_coverage"] = {
            native: [
                rid
                for rid in reactions
                if native in rhea.get(rid, {}).get("metacyc", []) or rid == "MetaCyc:" + native
            ]
            for native in leaves
        }
        review["native_reaction_exclusions"] = {}
        if native_id == "ARO-PWY":
            review["native_reaction_exclusions"]["RXN-7968"] = (
                "Optional generic NAD(P)-dependent quinate/shikimate "
                "dehydrogenase alternative in the nested multi-organism source. "
                "The E. coli record represents the specifically grounded "
                "NADPH-dependent AroE biosynthetic route; the source "
                "alternative introduces no missing core metabolite."
            )
        unexplained = set(
            native for native, matches in review["native_reaction_coverage"].items() if not matches
        ) - set(review["native_reaction_exclusions"])
        if unexplained:
            raise ValueError(
                f"Unreviewed native pathway reactions in {record['id']}: {sorted(unexplained)}"
            )
        review["reactions_without_named_protein"] = sorted(
            set(reactions)
            - {rid for item in review["protein_annotations"] for rid in item["reactions"]}
        )
        review["activity_class_cofactor_comments"] = {
            pid: enzymes[pid]["comment"]
            for pid in nodes
            if pid.startswith("EC:")
            and re.search(
                "cofactor|requires|metal|magnesium|pyridox|zinc|iron|cobalamin|thiamine",
                enzymes[pid]["comment"],
                re.I,
            )
        }
        review["bound_cofactor_review"] = (
            "Reviewed exact-taxonomic-scope UniProt catalytic matches and "
            "ENZYME comments. Absence of an annotation is not evidence that "
            "a cofactor is unnecessary. Broad Bacteria records and narrow "
            "scopes without reviewed protein matches retain unresolved "
            "protein/cofactor coverage."
        )
        review["regulation_and_compartments"] = (
            "Native pathway comments and available protein annotations "
            "reviewed; additions require exact grounded molecular entities "
            "and taxon-matched evidence. No organelle or DNA/RNA entity is "
            "inferred merely from a pathway name."
        )
        identifiers.update(n["id"] for k in ("participants", "reactions") for n in record[k])
        if args.apply:
            path.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=100))
        ledger.append(review)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    (args.report_dir / "metacyc-review.json").write_text(
        json.dumps({"records": ledger}, indent=2) + "\n"
    )
    (args.report_dir / "metacyc-identifiers.txt").write_text("\n".join(sorted(identifiers)) + "\n")
    manifest = {
        "rhea_rdf": {
            "url": "https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz",
            "sha256": digest(args.rhea_rdf),
            "version": "139",
            "sha256_scope": "uncompressed_rdf",
        },
        "rhea_directions": {
            "url": "https://ftp.expasy.org/databases/rhea/tsv/rhea-directions.tsv",
            "sha256": digest(args.directions),
            "version": "139",
        },
        "enzyme_dat": {
            "url": "https://ftp.expasy.org/databases/enzyme/enzyme.dat",
            "sha256": digest(args.enzyme_dat),
            "version": "02-Sep-2026",
        },
        "pubmed": {
            "url": json.loads(args.pubmed_xml.with_suffix(".manifest.json").read_text())["url"],
            "sha256": digest(args.pubmed_xml),
        },
        "additional_pubmed": {
            "url": (
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=p"
                "ubmed&id=21548610,16027371&retmode=xml"
            ),
            "sha256": digest(args.additional_pubmed_xml),
        },
        "uniprot": protein_manifest,
        "uniprot_locations": location_sources,
        "metacyc": {
            p.stem: {
                "url": "https://pathway.yeastgenome.org/getxml?id=META:" + p.stem + "&detail=full",
                "sha256": digest(p),
                "version": "22.5",
            }
            for p in sorted(args.metacyc_dir.glob("*.xml"))
        },
    }
    (args.report_dir / "metacyc-sources.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(
        f"{'Updated' if args.apply else 'Reviewed'} {len(ledger)} "
        f"MetaCyc records; ledger: {args.report_dir}"
    )


if __name__ == "__main__":
    main()
