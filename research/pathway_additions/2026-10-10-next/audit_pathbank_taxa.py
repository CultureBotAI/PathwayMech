"""Audit native BioSource taxonomy links; co-occurrence does not approve pathways."""

import argparse
import csv
import hashlib
import json
import sqlite3
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin
from xml.etree import ElementTree as ET
from zipfile import ZipFile

BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
XML_BASE = "{http://www.w3.org/XML/1998/namespace}base"
# These are the microbial taxa among this archive's complete enumerated taxon set.
# Other IDs remain visible for reassessment; this is not a universal microbe classifier.
MICROBIAL_TAXA = {"2", "287", "4932", "562"}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def audit(archive_path, baseline_path, taxonomy_path, output):
    with baseline_path.open() as stream:
        baseline = {row["member"] for row in csv.DictReader(stream, delimiter="\t")}
    counts = Counter()
    rows = []
    missing = []
    parsed = 0
    with ZipFile(archive_path) as archive:
        for member in sorted(archive.namelist()):
            if not member.endswith(".owl"):
                continue
            raw = archive.read(member)
            root = ET.fromstring(raw)
            parsed += 1
            base = root.get(XML_BASE, "")
            if any(XML_BASE in node.attrib for node in root.iter() if node is not root):
                raise ValueError(f"Nested XML base in {member}")

            def subject(node, base=base):
                identity = node.get(RDF + "ID")
                return urljoin(base, "#" + identity if identity else node.get(RDF + "about", ""))

            index = {subject(node): node for node in root}
            if len(index) != len(root):
                raise ValueError(f"Duplicate or unindexed RDF subjects in {member}")
            biosources = {}
            for node in root.findall(BP + "BioSource"):
                identifiers = set()
                for link in node.findall(BP + "xref"):
                    uri = urljoin(base, link.get(RDF + "resource", ""))
                    xref = index.get(uri)
                    if xref is None:
                        raise ValueError(f"Unresolved BioSource xref {member}: {uri}")
                    if (xref.findtext(BP + "db") or "").casefold() == "taxonomy":
                        accession = xref.findtext(BP + "id")
                        if not accession or not accession.isdigit():
                            raise ValueError(f"Invalid taxonomy ID in {member}")
                        identifiers.add(accession)
                if not identifiers:
                    missing.append({"member": member, "biosource": subject(node)})
                counts.update(identifiers)
                biosources[subject(node)] = {
                    "taxonomy_ids": sorted(identifiers),
                    "display_name": node.findtext(BP + "displayName"),
                    "name": node.findtext(BP + "name"),
                }
            microbial = {key: value for key, value in biosources.items()
                         if MICROBIAL_TAXA.intersection(value["taxonomy_ids"])}
            if not microbial:
                continue
            pathways = []
            for node in root.findall(BP + "Pathway"):
                organisms = [urljoin(base, link.get(RDF + "resource", ""))
                             for link in node.findall(BP + "organism")]
                pathways.append({
                    "native_id": subject(node),
                    "title": node.findtext(BP + "displayName"),
                    "organism_links": organisms,
                    "organism_taxonomy_ids": {
                        uri: biosources.get(uri, {}).get("taxonomy_ids", []) for uri in organisms
                    },
                    "direct_microbial_organism_links": [
                        uri for uri in organisms if uri in microbial
                    ],
                })
            rows.append({
                "member": member,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "included_in_name_screen": member in baseline,
                "microbial_biosources": microbial,
                "native_object_class_counts": dict(sorted(Counter(
                    node.tag.rsplit("}", 1)[-1] for node in root
                ).items())),
                "document_reaction_count": len(root.findall(BP + "BiochemicalReaction")),
                "pathways": pathways,
            })
    with sqlite3.connect(taxonomy_path.resolve().as_uri() + "?mode=ro", uri=True) as db:
        taxa = []
        for identifier, count in sorted(counts.items(), key=lambda item: int(item[0])):
            labels = db.execute(
                "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'",
                ("NCBITaxon:" + identifier,),
            ).fetchall()
            if len(labels) != 1:
                raise ValueError(f"Unresolved taxonomy label {identifier}")
            taxa.append({"id": "NCBITaxon:" + identifier, "label": labels[0][0],
                         "biosource_occurrences": count,
                         "selected_as_microbial": identifier in MICROBIAL_TAXA})
    report = {
        "archive_sha256": sha256(archive_path),
        "archive_bytes": archive_path.stat().st_size,
        "archive_url": "https://pathbank.org/downloads/pathbank_primary_biopax.zip",
        "name_screen_sha256": sha256(baseline_path),
        "taxonomy_database_sha256": sha256(taxonomy_path),
        "parsed_owl_members": parsed,
        "all_native_taxa": taxa,
        "biosources_without_taxonomy_xref": missing,
        "microbial_taxonomy_member_count": len(rows),
        "new_members_beyond_name_screen": [
            row for row in rows if not row["included_in_name_screen"]
        ],
        "members": rows,
        "limitations": [
            "A BioSource anywhere in a document does not establish the organism of its pathway.",
            "Explicit Pathway organism links are reported separately; "
            "absence is not negative evidence.",
            "Document reaction counts do not prove native pathway membership "
            "or mechanistic completeness.",
            "Bacteria and three microbial species are selected "
            "after enumerating all archive taxonomy IDs.",
            "This is an archive inventory, not scientific approval, "
            "semantic deduplication or source exhaustion.",
        ],
    }
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in (
        "parsed_owl_members", "microbial_taxonomy_member_count", "new_members_beyond_name_screen"
    )}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--name-screen", type=Path, required=True)
    parser.add_argument("--taxonomy-db", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    audit(args.archive, args.name_screen, args.taxonomy_db, args.output)
