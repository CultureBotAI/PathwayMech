"""Read dbCAN-PUL support tables while retaining native cells and provenance."""

from __future__ import annotations

import csv
import hashlib
import io
import json
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
DBCAN_PUL_PROVENANCE_HEADER = (
    "source_file\tsource_sha256\tsource_sheet\tsource_row\tnative_fields_json"
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
    source_file: str = ""
    source_sha256: str = ""
    source_sheet: str = ""
    source_row: int = 0
    native_fields: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class _NativeRow:
    fields: tuple[tuple[str, str], ...]
    sheet: str
    number: int


def load_dbcan_pul(
    path: Path,
    *,
    expected_sha256: str | None = None,
) -> list[DbcanPulRecord]:
    """Load all rows before returning; optionally bind the exact artifact digest.

    Existing normalized fields are search summaries. In particular, family
    summaries do not preserve domain grouping. ``native_fields`` retains every
    original header/value pair in order, including blank and duplicate headers,
    so native grouping, old locus tags and prediction settings remain available.
    """
    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if expected_sha256 is not None:
        if not isinstance(expected_sha256, str) or not re.fullmatch(
            r"[a-fA-F0-9]{64}", expected_sha256
        ):
            raise ValueError("dbCAN-PUL expected_sha256 must be 64 hexadecimal characters")
        if digest != expected_sha256.lower():
            raise ValueError("dbCAN-PUL SHA-256 mismatch")
    try:
        rows = (
            _xlsx_rows(payload)
            if path.suffix.lower() == ".xlsx"
            else _delimited_rows(payload, path.suffix.lower())
        )
    except (zipfile.BadZipFile, ElementTree.ParseError, KeyError, IndexError) as error:
        raise ValueError(f"Malformed dbCAN-PUL workbook: {error}") from error
    return [_dbcan_pul_record(row, path.name, digest) for row in rows]


def dbcan_pul_seed_rows(
    records: list[DbcanPulRecord],
    *,
    include_provenance: bool = False,
) -> list[str]:
    """Render TSV safely; opt in to lossless native fields and artifact locators.

    The default thirteen-column summary remains compatible with earlier callers.
    Neither representation infers ordered reactions or gene-specific activities.
    """
    header = DBCAN_PUL_SEED_HEADER
    if include_provenance:
        header += "\t" + DBCAN_PUL_PROVENANCE_HEADER
    result = [header]
    for record in records:
        values = [
            record.id,
            "|".join(record.pmids),
            record.organism,
            record.ncbi_taxon_id,
            record.genomic_accession,
            record.nucleotide_range,
            record.substrate,
            record.mode,
            "|".join(record.verification_methods),
            record.gene_loci,
            "|".join(record.cazyme_families),
            record.num_cazymes,
            record.num_genes,
        ]
        if include_provenance:
            values.extend(
                [
                    record.source_file,
                    record.source_sha256,
                    record.source_sheet,
                    str(record.source_row),
                    json.dumps(record.native_fields, ensure_ascii=True, separators=(",", ":")),
                ]
            )
        buffer = io.StringIO(newline="")
        csv.writer(buffer, delimiter="\t", lineterminator="\r\n").writerow(values)
        result.append(buffer.getvalue().removesuffix("\r\n"))
    return result


def _dbcan_pul_record(row: _NativeRow, filename: str, digest: str) -> DbcanPulRecord:
    fields = row.fields
    record_id = _first(fields, "ID", "PUL ID", "PUL_ID")
    if not record_id:
        raise ValueError(f"dbCAN-PUL {row.sheet or filename} row {row.number}: missing PUL ID")
    return DbcanPulRecord(
        id=record_id.removeprefix("dbCAN-PUL:"),
        pmids=_pmids(_first(fields, "PMID", "pmid")),
        organism=_first(fields, "organism_name", "Organism", "organism"),
        ncbi_taxon_id=_ncbi_taxon(_first(fields, "ncbi_species_tax_id", "ncbi_taxon_id", "tax_id")),
        genomic_accession=_first(
            fields,
            "genomic_accession_number",
            "genomic_accession",
            "accession",
        ),
        nucleotide_range=_first(
            fields,
            "nucleotide_position_range",
            "nucleotide_range",
            "position_range",
        ),
        substrate=_first(fields, "substrate_final", "substrate"),
        mode=_first(fields, "degradation_biosynthesis", "mode"),
        verification_methods=_split(
            _first(fields, "verification_final", "verification", "methods", "experimental_methods"),
            separators=",;|",
        ),
        gene_loci=_first(fields, "gene_locus_tags_or_modular", "gene_locus_tags", "locus_tags"),
        # cazymes_predicted_dbCAN2 is the source's yes/no flag, not a family column.
        cazyme_families=_split(
            _first(fields, "cazymes_predicted_dbcan", "cazyme_families"),
            separators=",;|",
        ),
        num_cazymes=_first(fields, "num_cazymes"),
        num_genes=_first(fields, "num_genes"),
        source_file=filename,
        source_sha256=digest,
        source_sheet=row.sheet,
        source_row=row.number,
        native_fields=fields,
    )


def _table_rows(
    rows: list[tuple[int, list[str]]],
    sheet: str,
) -> list[_NativeRow]:
    header_index = next((i for i, (_, values) in enumerate(rows) if any(values)), None)
    if header_index is None:
        raise ValueError("dbCAN-PUL table is empty")
    header = rows[header_index][1]
    if not any(_normalize(name) in {"id", "pul_id"} for name in header):
        raise ValueError("dbCAN-PUL table has no recognized PUL ID header")
    result = []
    for number, values in rows[header_index + 1 :]:
        if not any(value.strip() for value in values):
            continue
        width = max(len(header), len(values))
        fields = tuple(
            (header[i] if i < len(header) else "", values[i] if i < len(values) else "")
            for i in range(width)
        )
        result.append(_NativeRow(fields, sheet, number))
    return result


def _delimited_rows(payload: bytes, suffix: str) -> list[_NativeRow]:
    delimiter = "," if suffix == ".csv" else "\t"
    try:
        reader = csv.reader(
            io.StringIO(payload.decode("utf-8-sig"), newline=""), delimiter=delimiter, strict=True
        )
        rows = []
        first_line = 1
        for values in reader:
            rows.append((first_line, values))
            first_line = reader.line_num + 1
    except (UnicodeDecodeError, csv.Error) as error:
        raise ValueError(f"Malformed dbCAN-PUL delimited table: {error}") from error
    return _table_rows(rows, "")


def _xlsx_rows(payload: bytes) -> list[_NativeRow]:
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        strings = _shared_strings(archive)
        workbook = ElementTree.fromstring(archive.read("xl/workbook.xml"))
        rels = _workbook_relationships(archive)
        sheet = _dbcan_pul_sheet(workbook.findall(f".//{{{_NS_MAIN}}}sheet"))
        sheet_path = _sheet_path(rels[sheet.attrib[f"{{{_NS_REL}}}id"]])
        root = ElementTree.fromstring(archive.read(sheet_path))
        rows = []
        for index, row in enumerate(
            root.findall(f".//{{{_NS_MAIN}}}sheetData/{{{_NS_MAIN}}}row"), 1
        ):
            values: list[str] = []
            for cell in row.findall(f"{{{_NS_MAIN}}}c"):
                column = _column_index(cell.attrib.get("r", ""))
                while len(values) <= column:
                    values.append("")
                values[column] = _cell_value(cell, strings)
            rows.append((int(row.attrib.get("r", str(index))), values))
    return _table_rows(rows, sheet.attrib.get("name", ""))


def _dbcan_pul_sheet(sheets: list[ElementTree.Element]) -> ElementTree.Element:
    selected = [sheet for sheet in sheets if sheet.attrib.get("name") == "Add_to_DB"]
    if len(selected) == 1:
        return selected[0]
    if not selected and len(sheets) == 1:
        return sheets[0]
    raise ValueError("dbCAN-PUL workbook needs one Add_to_DB sheet or a single unambiguous sheet")


def _shared_strings(archive: zipfile.ZipFile) -> list[str]:
    try:
        root = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    return [
        "".join(node.text or "" for node in element.iter(f"{{{_NS_MAIN}}}t")) for element in root
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


def _cell_value(cell: ElementTree.Element, strings: list[str]) -> str:
    value = cell.find(f"{{{_NS_MAIN}}}v")
    raw = "" if value is None or value.text is None else value.text
    if cell.attrib.get("t") == "s":
        if not raw.isdigit():
            raise ValueError("dbCAN-PUL shared-string cell has no valid string index")
        return strings[int(raw)]
    if cell.attrib.get("t") == "inlineStr":
        return "".join(node.text or "" for node in cell.iter(f"{{{_NS_MAIN}}}t"))
    return raw


def _column_index(reference: str) -> int:
    match = re.fullmatch(r"([A-Za-z]+)[1-9][0-9]*", reference)
    if match is None:
        raise ValueError(f"dbCAN-PUL cell has invalid reference {reference!r}")
    index = 0
    for char in match[1].upper():
        index = index * 26 + ord(char) - ord("A") + 1
    return index - 1


def _first(row: tuple[tuple[str, str], ...], *names: str) -> str:
    for name in names:
        values = [
            value.strip()
            for key, value in row
            if _normalize(key) == _normalize(name) and value.strip()
        ]
        if len(set(values)) > 1:
            raise ValueError(f"dbCAN-PUL ambiguous values for duplicate header {name!r}")
        if values:
            return values[0]
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
