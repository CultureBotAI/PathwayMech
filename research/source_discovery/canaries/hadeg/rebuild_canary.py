"""Rebuild the four-row HADEG research projection from a supplied frozen cache.

No downloads, PathwayRecord writes, or automatic biological inference occur.
Only Python's standard library is required.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
WORKBOOK = "Tables/1_Aerobic_alkane_degradation_pathways_and_genes.xlsx"
CSV = "Tables/7_All_pathways.csv"
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def workbook_rows(path: Path) -> list[dict[str, str]]:
    """Read the pinned workbook's shared-string cells; reject schema drift."""
    with ZipFile(path) as archive:
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        sheets = workbook.findall("s:sheets/s:sheet", NS)
        require(len(sheets) == 1 and sheets[0].get("name") == "1", "unexpected worksheet")
        shared = [
            "".join(node.itertext())
            for node in ET.fromstring(archive.read("xl/sharedStrings.xml")).findall("s:si", NS)
        ]
        sheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
        rows = []
        for row in sheet.findall("s:sheetData/s:row", NS):
            cells = {}
            for cell in row.findall("s:c", NS):
                value = cell.findtext("s:v", namespaces=NS)
                if value is not None:
                    cells[cell.attrib["r"]] = shared[int(value)] if cell.get("t") == "s" else value
            rows.append(cells)
    require(
        rows[1]
        == dict(
            zip(
                (f"{col}2" for col in "ABCDEF"),
                ("Group", "Pathway", "Subpathway", "Gene", "Protein acc. No.", "Source"),
                strict=True,
            )
        ),
        "unexpected workbook header",
    )
    return rows[2:]


def ncbi_identity(root: ET.Element, accession: str, gene: str) -> dict[str, Any]:
    matches = [
        node
        for node in root.findall("GBSeq")
        if node.findtext("GBSeq_accession-version") == accession
    ]
    require(len(matches) == 1, f"NCBI accession/version mismatch: {accession}")
    record = matches[0]
    fields: dict[str, list[str]] = {}
    taxa = []
    for feature in record.findall("GBSeq_feature-table/GBFeature"):
        kind = feature.findtext("GBFeature_key")
        if kind not in {"source", "CDS", "Protein"}:
            continue
        for qualifier in feature.findall("GBFeature_quals/GBQualifier"):
            name = qualifier.findtext("GBQualifier_name", "")
            value = qualifier.findtext("GBQualifier_value", "")
            fields.setdefault(name, []).append(value)
            if kind == "source" and name == "db_xref" and value.startswith("taxon:"):
                taxa.append(value.split(":", 1)[1])
    require(gene in fields.get("gene", []), f"NCBI gene mismatch: {accession}")
    require(len(set(taxa)) == 1, f"NCBI source taxon missing or conflicting: {accession}")
    require(len(set(fields.get("coded_by", []))) == 1, f"NCBI locus ambiguous: {accession}")
    return {
        "raw": accession,
        "syntax_class": "versioned_ncbi_protein_accession_candidate",
        "verification_status": "verified_exact_accession_version",
        "curie": f"NCBIProtein:{accession}",
        "authority_artifact": "finnerty-ncbi-proteins.xml",
        "authority_locator": f'/GBSet/GBSeq[GBSeq_accession-version="{accession}"]',
        "label": fields["product"][0],
        "taxon_id": f"NCBITaxon:{taxa[0]}",
        "taxon_label": record.findtext("GBSeq_organism"),
        "taxon_locator": (
            'GBSeq_feature-table/GBFeature[GBFeature_key="source"]/GBFeature_quals/'
            'GBQualifier[GBQualifier_name="db_xref"]'
        ),
        "coded_by": fields["coded_by"][0],
    }


def rebuild(cache_dir: Path) -> dict[str, Any]:
    manifest = json.loads((HERE / "acquisition-manifest.json").read_text())
    for artifact in manifest:
        data = (cache_dir / artifact["path"]).read_bytes()
        require(
            hashlib.sha256(data).hexdigest() == artifact["sha256"],
            f"SHA-256 mismatch: {artifact['path']}",
        )
        require(len(data) == artifact["bytes"], f"size mismatch: {artifact['path']}")
    projection = json.loads((HERE / "review-assessments.json").read_text())
    assessments = projection.pop("membership_assessments")
    projection["artifacts"] = manifest
    members = []
    workbook = workbook_rows(cache_dir / WORKBOOK)
    ncbi = ET.parse(cache_dir / "finnerty-ncbi-proteins.xml").getroot()
    with (cache_dir / CSV).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            if row["Pathway"] != "A_Finnerty_pathway":
                continue
            accession = row["Protein_ID"]
            require(accession in assessments, f"unexpected canary accession: {accession}")
            hits = [
                r
                for r in workbook
                if any(key.startswith("E") and value == accession for key, value in r.items())
            ]
            require(len(hits) == 1, f"workbook join missing or ambiguous: {accession}")
            wrow = hits[0]
            number = next(key[1:] for key in wrow if key.startswith("E"))
            for col, field in zip("ABC", ("Compound", "Pathway", "Subpathway"), strict=True):
                require(wrow[f"{col}{number}"] == row[field], f"workbook {field} mismatch")
            gene = wrow[f"D{number}"]
            prefix = (
                row["code_mechanism"] + row["code_compound"] + row["code_subpathway"].rstrip("_")
            )
            require(row["Gene"] == f"{prefix}_{gene}", f"workbook gene mismatch: {accession}")
            member = {
                "source_id": "hadeg",
                "source_commit": projection["source_commit"],
                "source_row": row,
                "csv_locator": f"{CSV}:line={reader.line_num};column=Protein_ID",
                "workbook_locator": f"{WORKBOOK}#sheet=1;cells=A{number}:F{number}",
                "workbook_gene": gene,
                "workbook_source": wrow[f"F{number}"],
                "claim_type": "source_reported_group_membership",
                "claim_verification": (
                    "observed_in_source; biological pathway membership "
                    "not independently established"
                ),
                "reaction_topology": None,
            }
            if accession in {"Q02UU0", "Q9I6Z2"}:
                authority = json.loads((cache_dir / f"{accession}.json").read_text())
                require(
                    authority["primaryAccession"] == accession,
                    f"UniProt accession mismatch: {accession}",
                )
                require(
                    authority["genes"][0]["geneName"]["value"] == gene,
                    f"UniProt gene mismatch: {accession}",
                )
                function = next(c for c in authority["comments"] if c["commentType"] == "FUNCTION")
                codes = sorted(
                    {
                        e["evidenceCode"]
                        for text in function["texts"]
                        for e in text.get("evidences", [])
                    }
                )
                require(
                    codes == assessments[accession]["evidence_codes"], "function evidence changed"
                )
                member["identifier"] = {
                    "raw": accession,
                    "syntax_class": "uniprot_accession_candidate",
                    "verification_status": "verified_exact_primary_accession",
                    "curie": f"UniProtKB:{accession}",
                    "authority_artifact": f"{accession}.json",
                    "authority_locator": "/primaryAccession",
                    "label": authority["proteinDescription"]["recommendedName"]["fullName"][
                        "value"
                    ],
                    "taxon_id": f"NCBITaxon:{authority['organism']['taxonId']}",
                    "taxon_label": authority["organism"]["scientificName"],
                    "taxon_locator": "/organism",
                    "authority_entry_version": authority["entryAudit"]["entryVersion"],
                }
            else:
                member["identifier"] = ncbi_identity(ncbi, accession, gene)
            member["functional_evidence"] = assessments[accession]
            members.append(member)
    require(
        len(members) == 4 and {m["identifier"]["raw"] for m in members} == set(assessments),
        "canary membership is missing or duplicated",
    )
    projection["members"] = members
    return projection


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = rebuild(args.cache_dir)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Rebuilt {len(result['members'])} source-membership observations")
