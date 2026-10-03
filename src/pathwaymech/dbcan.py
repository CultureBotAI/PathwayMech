from __future__ import annotations

import csv
import posixpath
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree

DBCAN_PUL_SEED_HEADER = (
    "dbcan_pul_id\tpmids\torganism\tncbi_taxon_id\tgenomic_accession\t"
    "nucleotide_range\tsubstrate\tmode\tverification_methods\tgene_loci\t"
    "cazyme_families\tnum_cazymes\tnum_genes"
)

_NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_NS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
_NS_PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
_SPACE = re.compile(r"[\t\r\n]+")
_WORD = re.compile(r"[^a-z0-9]+")


@dataclass(frozen=True)
class DbcanPulRecord:
    id: str
    pmids: tuple[str, ...]
    organism: str
    ncbi_taxon_id: str
    genomic_accession: str
    nucleotide_range: str
    substrate: str
    mode: str
    verification_methods: tuple[str, ...]
    gene_loci: str
    cazyme_families: tuple[str, ...]
    num_cazymes: str
    num_genes: str


def load_dbcan_pul(path: Path) -> list[DbcanPulRecord]:
    rows = _xlsx_rows(path) if path.suffix.lower() == ".xlsx" else _delimited_rows(path)
    return [record for row in rows if (record := _dbcan_pul_record(row))]


def dbcan_pul_seed_rows(records: list[DbcanPulRecord]) -> list[str]:
    return [
        DBCAN_PUL_SEED_HEADER,
        *[
            "\t".join(
                [
                    record.id,
                    "|".join(record.pmids),
                    _cell(record.organism),
                    record.ncbi_taxon_id,
                    _cell(record.genomic_accession),
                    _cell(record.nucleotide_range),
                    _cell(record.substrate),
                    _cell(record.mode),
                    "|".join(_cell(method) for method in record.verification_methods),
                    _cell(record.gene_loci),
                    "|".join(_cell(family) for family in record.cazyme_families),
                    record.num_cazymes,
                    record.num_genes,
                ]
            )
            for record in records
        ],
    ]


def _dbcan_pul_record(row: dict[str, str]) -> DbcanPulRecord | None:
    record_id = _first(row, "ID", "PUL ID", "PUL_ID")
    if not record_id:
        return None

    return DbcanPulRecord(
        id=record_id.removeprefix("dbCAN-PUL:"),
        pmids=_pmids(_first(row, "PMID", "pmid")),
        organism=_first(row, "organism_name", "Organism", "organism"),
        ncbi_taxon_id=_ncbi_taxon(
            _first(row, "ncbi_species_tax_id", "ncbi_taxon_id", "tax_id")
        ),
        genomic_accession=_first(
            row,
            "genomic_accession_number",
            "genomic_accession",
            "accession",
        ),
        nucleotide_range=_first(
            row,
            "nucleotide_position_range",
            "nucleotide_range",
            "position_range",
        ),
        substrate=_first(row, "substrate_final", "substrate"),
        mode=_first(row, "degradation_biosynthesis", "mode"),
        verification_methods=_split(
            _first(
                row,
                "verification_final",
                "verification",
                "methods",
                "experimental_methods",
            ),
            separators=",;|",
        ),
        gene_loci=_first(
            row,
            "gene_locus_tags_or_modular",
            "gene_locus_tags",
            "locus_tags",
        ),
        cazyme_families=_split(
            _first(
                row,
                "cazymes_predicted_dbcan",
                "cazymes_predicted_dbCAN2",
                "cazyme_families",
            ),
            separators=",;|",
        ),
        num_cazymes=_first(row, "num_cazymes"),
        num_genes=_first(row, "num_genes"),
    )


def _delimited_rows(path: Path) -> list[dict[str, str]]:
    delimiter = "," if path.suffix.lower() == ".csv" else "\t"
    with path.open(encoding="utf-8", newline="") as stream:
        return [dict(row) for row in csv.DictReader(stream, delimiter=delimiter)]


def _xlsx_rows(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        strings = _shared_strings(archive)
        workbook = ElementTree.fromstring(archive.read("xl/workbook.xml"))
        rels = _workbook_relationships(archive)
        sheet = workbook.find(f".//{{{_NS_MAIN}}}sheet")
        if sheet is None:
            return []
        sheet_path = _sheet_path(rels[sheet.attrib[f"{{{_NS_REL}}}id"]])
        rows = _sheet_rows(
            ElementTree.fromstring(archive.read(sheet_path)),
            strings,
        )

    header_index, header = next(
        (
            (index, [_cell(value) for value in row])
            for index, row in enumerate(rows)
            if any(row)
        ),
        (-1, []),
    )
    return [
        {
            header[index]: row[index] if index < len(row) else ""
            for index in range(len(header))
            if header[index]
        }
        for row in rows[header_index + 1 :]
        if any(_cell(value) for value in row)
    ]


def _shared_strings(archive: zipfile.ZipFile) -> list[str]:
    try:
        root = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    return [
        "".join(node.text or "" for node in element.iter(f"{{{_NS_MAIN}}}t"))
        for element in root
    ]


def _workbook_relationships(archive: zipfile.ZipFile) -> dict[str, str]:
    root = ElementTree.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    return {
        relationship.attrib["Id"]: relationship.attrib["Target"]
        for relationship in root.findall(f"{{{_NS_PKG_REL}}}Relationship")
    }


def _sheet_path(target: str) -> str:
    if target.startswith("/"):
        return target.removeprefix("/")
    return posixpath.normpath(posixpath.join("xl", target))


def _sheet_rows(root: ElementTree.Element, strings: list[str]) -> list[list[str]]:
    rows = []
    for row in root.findall(f".//{{{_NS_MAIN}}}sheetData/{{{_NS_MAIN}}}row"):
        values: list[str] = []
        for cell in row.findall(f"{{{_NS_MAIN}}}c"):
            index = _column_index(cell.attrib.get("r", "A1"))
            while len(values) <= index:
                values.append("")
            values[index] = _cell_value(cell, strings)
        rows.append(values)
    return rows


def _cell_value(cell: ElementTree.Element, strings: list[str]) -> str:
    value = cell.find(f"{{{_NS_MAIN}}}v")
    raw = "" if value is None or value.text is None else value.text
    if cell.attrib.get("t") == "s":
        return strings[int(raw)] if raw else ""
    if cell.attrib.get("t") == "inlineStr":
        return "".join(node.text or "" for node in cell.iter(f"{{{_NS_MAIN}}}t"))
    return raw


def _column_index(reference: str) -> int:
    index = 0
    for char in reference:
        if not char.isalpha():
            break
        index = index * 26 + ord(char.upper()) - ord("A") + 1
    return index - 1


def _first(row: dict[str, str], *names: str) -> str:
    normalized = {_normalize(key): value for key, value in row.items()}
    for name in names:
        value = normalized.get(_normalize(name), "")
        if value and value.strip():
            return value.strip()
    return ""


def _pmids(value: str) -> tuple[str, ...]:
    return tuple(f"PMID:{pmid}" for pmid in re.findall(r"\d+", value))


def _ncbi_taxon(value: str) -> str:
    if not value:
        return ""
    return value if value.startswith("NCBITaxon:") else f"NCBITaxon:{value}"


def _split(value: str, *, separators: str) -> tuple[str, ...]:
    pieces = re.split(f"[{re.escape(separators)}]", value)
    return tuple(dict.fromkeys(_cell(piece) for piece in pieces if _cell(piece)))


def _cell(value: str) -> str:
    return _SPACE.sub(" ", value).strip()


def _normalize(value: str) -> str:
    return _WORD.sub("_", value.casefold()).strip("_")
