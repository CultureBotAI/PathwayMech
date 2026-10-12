from __future__ import annotations

import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree

import pytest

from pathwaymech.dbcan import dbcan_pul_seed_rows, load_dbcan_pul

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG = "http://schemas.openxmlformats.org/package/2006/relationships"


def _workbook(
    path: Path, rows: list[tuple[int, list[str]]], names: tuple[str, ...] = ("Add_to_DB",)
) -> None:
    """Small synthetic worksheet with explicit row numbers and styled blank cells."""
    workbook = ElementTree.Element(f"{{{NS}}}workbook")
    sheets = ElementTree.SubElement(workbook, f"{{{NS}}}sheets")
    relationships = ElementTree.Element(f"{{{PKG}}}Relationships")
    with zipfile.ZipFile(path, "w") as archive:
        for index, name in enumerate(names, 1):
            relation = f"rId{index}"
            target = f"worksheets/sheet{index}.xml"
            ElementTree.SubElement(
                sheets, f"{{{NS}}}sheet", {"name": name, f"{{{REL}}}id": relation}
            )
            ElementTree.SubElement(
                relationships, f"{{{PKG}}}Relationship", {"Id": relation, "Target": target}
            )
            worksheet = ElementTree.Element(f"{{{NS}}}worksheet")
            data = ElementTree.SubElement(worksheet, f"{{{NS}}}sheetData")
            for number, values in rows:
                row = ElementTree.SubElement(data, f"{{{NS}}}row", {"r": str(number)})
                for column, value in enumerate(values):
                    cell = ElementTree.SubElement(
                        row, f"{{{NS}}}c", {"r": f"{chr(65 + column)}{number}"}
                    )
                    if value:
                        cell.set("t", "inlineStr")
                        inline = ElementTree.SubElement(cell, f"{{{NS}}}is")
                        ElementTree.SubElement(inline, f"{{{NS}}}t").text = value
                    else:
                        cell.set("s", "3")
            archive.writestr(f"xl/{target}", ElementTree.tostring(worksheet))
        archive.writestr("xl/workbook.xml", ElementTree.tostring(workbook))
        archive.writestr("xl/_rels/workbook.xml.rels", ElementTree.tostring(relationships))


def _export(records: list) -> list[dict[str, str]]:
    return list(
        csv.DictReader(
            io.StringIO(
                "\n".join(dbcan_pul_seed_rows(records, include_provenance=True)), newline=""
            ),
            delimiter="\t",
        )
    )


def test_native_xlsx_preserves_aliases_domain_groups_and_physical_locator(tmp_path: Path) -> None:
    path = tmp_path / "native.xlsx"
    header = [
        "ID",
        "gene_locus_tags_or_modular",
        "old_other_gene_locus_tags_or_modules",
        "cazymes_predicted_dbCAN2",
        "cazymes_predicted_dbcan",
        "ncbi_species_tax_id",
        "verification_final",
        "extra",
        "extra",
        "",
    ]
    native = [
        "PULTEST",
        "newA-newC",
        "oldA-oldC",
        "yes",
        "CBM27|GH26|CBM23,GH3",
        "166486\u00a0",
        "",
        "first",
        "second",
        "",
    ]
    _workbook(path, [(1, header), (2, []), (76, native)])
    digest = hashlib.sha256(path.read_bytes()).hexdigest()

    (record,) = load_dbcan_pul(path, expected_sha256=digest.upper())

    assert record.source_file == "native.xlsx"
    assert record.source_sheet == "Add_to_DB"
    assert record.source_row == 76
    assert record.source_sha256 == digest
    assert record.ncbi_taxon_id == "NCBITaxon:166486"
    assert record.verification_methods == ()
    assert record.native_fields == tuple(zip(header, native, strict=True))
    (exported,) = _export([record])
    assert json.loads(exported["native_fields_json"]) == [
        list(pair) for pair in record.native_fields
    ]
    assert exported["source_row"] == "76"
    assert exported["source_sha256"] == digest


def test_prediction_no_is_not_a_cazyme_family_and_trailing_blank_is_retained(
    tmp_path: Path,
) -> None:
    path = tmp_path / "native.tsv"
    path.write_text("ID\tcazymes_predicted_dbCAN2\tcazymes_predicted_dbcan\nPULTEST\tno\n")

    (record,) = load_dbcan_pul(path)

    assert record.cazyme_families == ()
    assert record.native_fields == (
        ("ID", "PULTEST"),
        ("cazymes_predicted_dbCAN2", "no"),
        ("cazymes_predicted_dbcan", ""),
    )


def test_tsv_export_roundtrips_controls_quotes_and_original_headers(tmp_path: Path) -> None:
    path = tmp_path / "quoted.csv"
    header = ["ID", "organism_name", "substrate_final", 'native\t"header"', "notes"]
    first = [
        "PULFIRST",
        'microbe\t"strain"',
        "first\rsecond\nthird",
        "native\tvalue",
        " exact \u00a0",
    ]
    second = ["PULSECOND", "microbe", "substrate", "", ""]
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerows([header, first, second])

    records = load_dbcan_pul(path)
    exported = _export(records)

    assert len(exported) == 2
    assert exported[0]["organism"] == first[1]
    assert exported[0]["substrate"] == first[2]
    assert json.loads(exported[0]["native_fields_json"]) == [
        list(pair) for pair in zip(header, first, strict=True)
    ]
    assert records[0].source_row == 2
    assert records[1].source_row == 5


def test_unheaded_extra_values_are_not_discarded(tmp_path: Path) -> None:
    path = tmp_path / "extra.tsv"
    path.write_text("ID\nPULTEST\textra\tlast\n")

    (record,) = load_dbcan_pul(path)

    assert record.native_fields == (("ID", "PULTEST"), ("", "extra"), ("", "last"))


def test_late_missing_id_is_reported_instead_of_dropping_row(tmp_path: Path) -> None:
    path = tmp_path / "missing.tsv"
    path.write_text("ID\tsubstrate\nPULFIRST\tfirst\n\tsecond\n")

    with pytest.raises(ValueError, match="row 3: missing PUL ID"):
        load_dbcan_pul(path)


def test_conflicting_duplicate_known_headers_are_not_silently_overwritten(tmp_path: Path) -> None:
    path = tmp_path / "duplicates.tsv"
    path.write_text("ID\tID\nPULFIRST\tPULSECOND\n")

    with pytest.raises(ValueError, match="duplicate header"):
        load_dbcan_pul(path)


@pytest.mark.parametrize("payload", [b"not a zip", b"PK\x03\x04truncated"])
def test_malformed_xlsx_is_a_value_error(tmp_path: Path, payload: bytes) -> None:
    path = tmp_path / "broken.xlsx"
    path.write_bytes(payload)

    with pytest.raises(ValueError, match="Malformed dbCAN-PUL workbook"):
        load_dbcan_pul(path)


def test_digest_mismatch_is_detected_before_malformed_workbook(tmp_path: Path) -> None:
    path = tmp_path / "broken.xlsx"
    path.write_bytes(b"not a zip")

    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        load_dbcan_pul(path, expected_sha256="0" * 64)


def test_multi_sheet_workbook_without_native_sheet_is_ambiguous(tmp_path: Path) -> None:
    path = tmp_path / "ambiguous.xlsx"
    _workbook(path, [(1, ["ID"]), (2, ["PULTEST"])], ("summary", "data"))

    with pytest.raises(ValueError, match="unambiguous sheet"):
        load_dbcan_pul(path)


def test_unrecognized_table_fails_instead_of_returning_no_records(tmp_path: Path) -> None:
    path = tmp_path / "wrong.tsv"
    path.write_text("title\nnot a support table\n")

    with pytest.raises(ValueError, match="PUL ID header"):
        load_dbcan_pul(path)
