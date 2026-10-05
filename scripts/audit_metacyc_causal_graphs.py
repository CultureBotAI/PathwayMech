#!/usr/bin/env python3
"""Audit every MetaCyc graph against independent Rhea RDF and native pathway XML.

This review helper reads full source artifacts and writes an edge-level ledger.
It never treats a corpus label or a green schema check as source verification.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

import yaml

RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RHEA = "http://rdf.rhea-db.org/"


def read_rhea(path: Path, directions: Path, selected: set[str]) -> dict:
    families = {}
    with directions.open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            family = tuple(row.values())
            if any(identifier in selected for identifier in family):
                for identifier in family:
                    families[identifier] = row["RHEA_ID_MASTER"]
    wanted = set(families)
    masters = set(families.values())
    predicates = {
        "accession",
        "label",
        "name",
        "substrates",
        "products",
        "side",
        "contains",
        "compound",
        "chebi",
        "ec",
        "seeAlso",
        "directionalReaction",
        "bidirectionalReaction",
        "status",
        "subClassOf",
        "comment",
        "citation",
    }
    facts = defaultdict(lambda: defaultdict(set))
    for _, element in ET.iterparse(path, events=("end",)):
        if element.tag != RDF + "Description":
            continue
        uri = element.get(RDF + "about", "")
        local = uri.removeprefix(RHEA)
        keep = (
            local.split("_")[0] in wanted
            or local.startswith("Compound_")
            or (local.startswith("Participant_") and local.split("_")[1] in masters)
        )
        if keep:
            for child in element:
                predicate = child.tag.split("}")[-1]
                if predicate in predicates:
                    value = child.get(RDF + "resource") or child.text
                    if value:
                        facts[uri][predicate].add(value)
        element.clear()
    results = {}
    for identifier in sorted(selected):
        uri = RHEA + identifier
        node = facts[uri]
        master = families.get(identifier)
        parent = facts[RHEA + master] if master else {}
        result = {
            "master": f"RHEA:{master}" if master else None,
            "label": sorted(node.get("label", [])),
            "types": sorted(node.get("subClassOf", [])),
            "ec": sorted("EC:" + value.rsplit("/", 1)[-1] for value in parent.get("ec", [])),
            "metacyc": sorted(
                {
                    value.split("METACYC:", 1)[1]
                    for member, family in families.items()
                    if family == master
                    for value in facts[RHEA + member].get("seeAlso", [])
                    if "METACYC:" in value
                }
            ),
            "sides": {},
        }
        for kind in ("substrates", "products", "side"):
            sides = node.get(kind, [])
            for side in sides:
                chemicals = set()
                for participant in facts[side].get("contains", []):
                    for compound in facts[participant].get("compound", []):
                        chemicals.update(facts[compound].get("accession", []))
                result["sides"][kind if kind != "side" else side] = sorted(chemicals)
        results[f"RHEA:{identifier}"] = result
    return results


def read_pathway(path: Path) -> dict:
    root = ET.parse(path).getroot()
    pathway = root.find("Pathway")
    if pathway is None:
        raise ValueError(f"{path}: no native pathway record")
    layouts = {}
    for layout in pathway.findall("reaction-layout"):
        entity = next(child for child in layout if child.tag in {"Reaction", "Pathway"})
        reaction = entity.get("frameid")
        layouts[reaction] = {
            "kind": entity.tag,
            "direction": layout.findtext("direction"),
            "left": [item.get("frameid") for item in layout.findall("left-primaries/*")],
            "right": [item.get("frameid") for item in layout.findall("right-primaries/*")],
        }
    return {
        "pathway": pathway.get("frameid"),
        "label": pathway.findtext("common-name"),
        "layouts": layouts,
        "ordering": [
            [
                before.get("frameid"),
                next(child for child in entry if child.tag in {"Reaction", "Pathway"}).get(
                    "frameid"
                ),
            ]
            for entry in pathway.findall("reaction-ordering")
            for before in entry.findall("predecessor-reactions/*")
        ],
        "species": [
            item.get("frameid").removeprefix("TAX-") for item in pathway.findall("species/Organism")
        ],
        "taxonomic_range": [
            item.get("frameid").removeprefix("TAX-")
            for item in pathway.findall("taxonomic-range/Organism")
        ],
        "comment": pathway.findtext("comment"),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def audit(root: Path, rhea_path: Path, directions: Path, metacyc: Path, output: Path) -> None:
    records = []
    for path in sorted((root / "data/pathways").rglob("*.yaml")):
        record = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        if record["id"].startswith("MetaCyc:"):
            records.append((path, record))
    selected = {
        node["id"].split(":")[1]
        for _, record in records
        for node in record["reactions"]
        if node["id"].startswith("RHEA:")
    }
    reactions = read_rhea(rhea_path, directions, selected)
    ledger = []
    for path, record in records:
        primary = read_pathway(metacyc / (record["id"].split(":")[1] + ".xml"))
        row = {
            "path": str(path.relative_to(root)),
            "id": record["id"],
            "source": primary,
            "reaction_reviews": [],
            "edges": [],
        }
        for node in record["reactions"]:
            identifier = node["id"]
            chemistry = reactions.get(identifier)
            observed = {
                "substrates": sorted(
                    edge["subject"]
                    for edge in record["mechanistic_edges"]
                    if edge["predicate"] == "consumes" and edge["object"] == identifier
                ),
                "products": sorted(
                    edge["object"]
                    for edge in record["mechanistic_edges"]
                    if edge["predicate"] == "produces" and edge["subject"] == identifier
                ),
                "enzymes": sorted(
                    edge["subject"]
                    for edge in record["mechanistic_edges"]
                    if edge["predicate"] == "catalyzes" and edge["object"] == identifier
                ),
            }
            review = {"id": identifier, "observed": observed, "authority": chemistry}
            if chemistry:
                review["differences"] = {}
                for side in ("substrates", "products"):
                    expected = chemistry["sides"].get(side)
                    if expected is None:
                        review["differences"][side] = "direction_requires_pathway_evidence"
                    else:
                        review["differences"][side] = {
                            "missing": sorted(set(expected) - set(observed[side])),
                            "extra": sorted(set(observed[side]) - set(expected)),
                        }
                review["enzyme_not_in_rhea"] = sorted(
                    set(observed["enzymes"]) - set(chemistry["ec"])
                )
            row["reaction_reviews"].append(review)
        for edge in record["mechanistic_edges"]:
            row["edges"].append(
                {
                    "id": edge["id"],
                    "subject": edge["subject"],
                    "predicate": edge["predicate"],
                    "object": edge["object"],
                    "evidence": edge["evidence"],
                }
            )
        ledger.append(row)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"records": ledger, "rhea": reactions}, indent=2) + "\n")
    print(
        f"Audited {len(records)} MetaCyc records and {len(reactions)} Rhea reaction IDs: {output}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--rhea-rdf", type=Path, required=True)
    parser.add_argument("--directions", type=Path, required=True)
    parser.add_argument("--metacyc-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    audit(args.root, args.rhea_rdf, args.directions, args.metacyc_dir, args.output)


if __name__ == "__main__":
    main()
