"""Reproduce bounded PathBank candidate screening; this does not approve records."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

import yaml

BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
MICROBIAL_NAMES = {"Escherichia coli", "Pseudomonas aeruginosa", "Saccharomyces cerevisiae"}


def screen(archive_path: Path, records: Path, output: Path) -> None:
    """Screen explicit named microbial BioSources, preserving all other labels."""
    maintained = [yaml.safe_load(p.read_text()) for p in sorted(records.rglob("*.yaml"))]
    rows = []
    biosource_counts = Counter()
    classes = Counter()
    parsed = 0
    with ZipFile(archive_path) as archive:
        for member in sorted(archive.namelist()):
            if not member.endswith(".owl"):
                continue
            raw = archive.read(member)
            root = ET.fromstring(raw)
            parsed += 1
            names = {
                node.findtext(BP + "displayName") or node.findtext(BP + "name") or "(unnamed)"
                for node in root.findall(BP + "BioSource")
            }
            biosource_counts.update(names)
            microbes = names & MICROBIAL_NAMES
            if not microbes:
                continue
            index = {
                (n.get(RDF + "ID") or n.get(RDF + "about", "")).removeprefix("#"): n
                for n in root
            }
            pathways = root.findall(BP + "Pathway")
            reactions = root.findall(BP + "BiochemicalReaction")
            ids, titles = set(), set()
            for pathway in pathways:
                titles.update(
                    n.text for n in pathway.findall(BP + "displayName") if n.text
                )
                for ref in pathway.findall(BP + "xref"):
                    xref = index.get(ref.get(RDF + "resource", "").removeprefix("#"))
                    if xref is not None and (xref.findtext(BP + "db") or "").casefold() == "smpdb":
                        accession = xref.findtext(BP + "id")
                        if accession:
                            ids.add("PathBank:" + accession)
            if len(pathways) > 1:
                state = "multiple_pathways_need_membership_selection"
            elif len(pathways) == 1:
                state = (
                    "single_pathway_ge2_document_reactions" if len(reactions) >= 2
                    else "single_pathway_lt2_document_reactions"
                )
            else:
                state = "no_pathway_object"
            classes[state] += 1
            exact_matches = sorted(r["id"] for r in maintained if r["id"] in ids)
            title_matches = sorted(
                r["id"] for r in maintained
                if r["label"].casefold() in {t.casefold() for t in titles}
            )
            rows.append({
                "member": member,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "explicit_microbial_biosources": " | ".join(sorted(microbes)),
                "pathway_object_count": len(pathways),
                "document_reaction_count": len(reactions),
                "native_pathway_ids": " | ".join(sorted(ids)),
                "native_titles": " | ".join(sorted(titles)),
                "screening_class": state,
                "exact_record_id_matches": " | ".join(exact_matches),
                "exact_record_title_matches": " | ".join(title_matches),
                "disposition": "needs_scientific_review_and_semantic_deduplication",
            })
    if not rows:
        raise ValueError("No explicitly named microbial BioSources found")
    output.mkdir(parents=True, exist_ok=True)
    with (output / "pathbank-screening.tsv").open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)
    receipt = {
        "archive_url": "https://pathbank.org/downloads/pathbank_primary_biopax.zip",
        "archive_sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(),
        "archive_bytes": archive_path.stat().st_size,
        "archive_version": "preserved archive; original Last-Modified 2019-08-16",
        "parsed_owl_members": parsed,
        "explicit_microbe_files": len(rows),
        "screening_classes": dict(sorted(classes.items())),
        "all_document_biosource_label_counts": dict(sorted(biosource_counts.items())),
        "maintained_record_count_at_screening": len(maintained),
        "limitations": [
            "Named-microbe screen only: BiologicalState and unnamed sources remain unclassified.",
            "Document reaction counts do not establish native pathway membership "
            "or biochemical completeness.",
            "Exact ID/title matches are hints; absent matches do not establish a novel route.",
            "The selected count is neither unique pathways nor approved additions.",
            "This inventory does not establish exhaustion of PathBank or other sources.",
        ],
    }
    (output / "pathbank-screening.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in (
        "parsed_owl_members", "explicit_microbe_files", "screening_classes",
        "maintained_record_count_at_screening",
    )}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--records", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    screen(args.archive, args.records, args.output)
