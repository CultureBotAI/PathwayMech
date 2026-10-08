"""Rebuild metadata counts from the externally retained dbCAN-PUL workbook.

This independent standard-library audit emits no source rows or pathway graphs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import posixpath
import re
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
FILE = "dbCAN-PUL_Feb-2025.xlsx"
MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
HEADERS = (
    "ID",
    "PMID",
    "verification_final",
    "genomic_accession_number",
    "nucleotide_position_range",
    "substrate_final",
    "gene_locus_tags_or_modular",
    "old_other_gene_locus_tags_or_modules",
    "organism_name",
    "ncbi_species_tax_id",
    "degradation_biosynthesis",
    "cazy_diamond_eval",
    "dbcan_hmmer_eval",
    "hotpep_hits",
    "tp_eval",
    "num_cgcs",
    "cazymes_predicted_dbCAN2",
    "num_cazymes",
    "num_genes",
    "cazymes_predicted_dbcan",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def inventory(cache: Path, exported: Path | None = None) -> dict:
    manifest = json.loads((HERE / "acquisition-manifest.json").read_text())
    for artifact in manifest:
        original = (cache / artifact["file"]).read_bytes()
        require(len(original) == artifact["bytes"], f"size mismatch: {artifact['file']}")
        require(
            hashlib.sha256(original).hexdigest() == artifact["sha256"],
            f"checksum mismatch: {artifact['file']}",
        )
    artifact = next(item for item in manifest if item["file"] == FILE)
    with ZipFile(cache / FILE) as archive:
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        sheets = workbook.findall(f"{{{MAIN}}}sheets/{{{MAIN}}}sheet")
        require(len(sheets) == 1 and sheets[0].get("name") == "Add_to_DB", "sheet mismatch")
        relationships = {
            item.get("Id"): item.get("Target")
            for item in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        }
        target = relationships[sheets[0].attrib[f"{{{REL}}}id"]]
        part = (
            target.lstrip("/")
            if target.startswith("/")
            else posixpath.normpath(posixpath.join("xl", target))
        )
        strings = [
            "".join(node.text or "" for node in element.iter(f"{{{MAIN}}}t"))
            for element in ET.fromstring(archive.read("xl/sharedStrings.xml"))
        ]
        native = ET.fromstring(archive.read(part))
        require(not native.findall(f".//{{{MAIN}}}f"), "unexpected formula cell")
        rows = []
        for row in native.findall(f"{{{MAIN}}}sheetData/{{{MAIN}}}row"):
            number = int(row.attrib["r"])
            values = {}
            for cell in row.findall(f"{{{MAIN}}}c"):
                coordinate = cell.attrib["r"]
                raw = cell.findtext(f"{{{MAIN}}}v", "")
                if cell.get("t") == "s":
                    raw = strings[int(raw)]
                elif cell.get("t") == "inlineStr":
                    raw = "".join(node.text or "" for node in cell.iter(f"{{{MAIN}}}t"))
                values[coordinate] = raw
            if any(values.values()):
                rows.append((number, values))
    require(rows[0][0] == 1, "header row mismatch")
    require(
        tuple(rows[0][1].get(f"{chr(65 + i)}1", "") for i in range(20)) == HEADERS,
        "header mismatch",
    )
    require("U1" in rows[0][1] and rows[0][1]["U1"] == "", "blank U header differs")
    require(
        all(
            re.fullmatch(r"[A-U][1-9][0-9]*", coordinate)
            and (not coordinate.startswith("U") or value == "")
            for _, cells in rows
            for coordinate, value in cells.items()
        ),
        "unexpected data beyond the 20 named columns",
    )
    data = [
        (
            number,
            {header: cells.get(f"{chr(65 + i)}{number}", "") for i, header in enumerate(HEADERS)},
        )
        for number, cells in rows[1:]
    ]
    ids = [row["ID"] for _, row in data]
    require(len(ids) == len(set(ids)), "duplicate source ID")
    require(all(re.fullmatch(r"PUL\d{4}", item) for item in ids), "unexpected source ID")
    if exported is not None:
        with exported.open(newline="") as handle:
            imported = list(csv.DictReader(handle, delimiter="\t"))
        require(len(imported) == len(data), "export row count differs")
        for (number, native_row), imported_row in zip(data, imported, strict=True):
            require(imported_row["dbcan_pul_id"] == native_row["ID"], "export ID differs")
            require(imported_row["source_file"] == FILE, "export source file differs")
            require(imported_row["source_sha256"] == artifact["sha256"], "export hash differs")
            require(imported_row["source_sheet"] == "Add_to_DB", "export sheet differs")
            require(imported_row["source_row"] == str(number), "export row locator differs")
            require(
                json.loads(imported_row["native_fields_json"])
                == [[key, value] for key, value in native_row.items()] + [["", ""]],
                f"export native cells differ at row {number}",
            )
    mode = Counter(row["degradation_biosynthesis"].strip() for _, row in data)
    empty_counts = {header: sum(not row[header] for _, row in data) for header in HEADERS}
    return {
        "kind": "source inventory metadata; no redistributed source rows",
        "source_file": FILE,
        "source_sha256": artifact["sha256"],
        "worksheet": "Add_to_DB",
        "worksheet_part": part,
        "header_row": 1,
        "headers": list(HEADERS),
        "physical_header_width": 21,
        "blank_physical_header_columns": ["U"],
        "nonempty_data_rows": len(data),
        "distinct_native_ids": len(set(ids)),
        "first_data_row": min(number for number, _ in data),
        "last_data_row": max(number for number, _ in data),
        "distinct_raw_taxonomy_strings": len({row["ncbi_species_tax_id"] for _, row in data}),
        "distinct_trimmed_taxonomy_strings": len(
            {row["ncbi_species_tax_id"].strip() for _, row in data}
        ),
        "distinct_pubmed_number_tokens": len(
            {token for _, row in data for token in re.findall(r"\d+", row["PMID"])}
        ),
        "mode_counts_after_whitespace_trim": dict(sorted(mode.items())),
        "blank_cell_counts": empty_counts,
        "rows_with_old_locus_identifiers": sum(
            bool(row["old_other_gene_locus_tags_or_modules"]) for _, row in data
        ),
        "rows_with_pipe_in_family_field": sum(
            "|" in row["cazymes_predicted_dbcan"] for _, row in data
        ),
        "rows_with_only_sequence_homology_method": sum(
            row["verification_final"].strip() == "sequence homology analysis" for _, row in data
        ),
        "scope_limits": [
            "Taxonomy and PubMed counts are source tokens, not independently verified authorities.",
            "A source locus row is not automatically a complete pathway or experimental mechanism.",
            "Current source methods include homology-only and blank annotations.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--export", type=Path, help="also compare a provenance TSV to all native cells"
    )
    args = parser.parse_args()
    result = inventory(args.cache, args.export)
    if args.check:
        expected = json.loads((HERE / "workbook-inventory.json").read_text())
        require(result == expected, "inventory differs")
        print("dbCAN-PUL original hashes and metadata inventory verified.")
        if args.export is not None:
            print("All 633 exported rows match the native cells and artifact locators.")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
