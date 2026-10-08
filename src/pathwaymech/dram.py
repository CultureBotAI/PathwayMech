"""Retain DRAM1's native module-step table as provenance-bearing support rows.

These rows are not reactions or experimental organism assertions. In particular,
``path`` is retained verbatim; this adapter does not interpret its coordinates,
split chemical names, or infer completeness logic from repeated coordinates.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from dataclasses import dataclass
from pathlib import Path

DRAM_SOURCE_PATH = "data/module_step_form.tsv"
DRAM_NATIVE_HEADER = (
    "gene",
    "ko",
    "module",
    "module_name",
    "path",
    "product_ids",
    "product_names",
    "substrate_ids",
    "substrate_names",
)
DRAM_PROVENANCE_HEADER = (
    "source_row_id",
    "source_file",
    "source_commit",
    "source_path",
    "source_url",
    "source_sha256",
    "source_line_start",
    "source_line_end",
    "native_fields_json",
)
DRAM_SEED_HEADER = "\t".join(DRAM_NATIVE_HEADER + DRAM_PROVENANCE_HEADER)


@dataclass(frozen=True)
class DramModuleStep:
    native_fields: tuple[tuple[str, str], ...]
    source_file: str
    source_commit: str
    source_sha256: str
    source_line_start: int
    source_line_end: int

    @property
    def source_path(self) -> str:
        return DRAM_SOURCE_PATH

    @property
    def source_url(self) -> str:
        return (
            "https://raw.githubusercontent.com/BortonWrightonLabs/DRAM/"
            f"{self.source_commit}/{self.source_path}"
        )

    @property
    def source_row_id(self) -> str:
        """A local artifact locator, not a native biological identifier."""
        return f"DRAM1:{self.source_sha256}:L{self.source_line_start}-L{self.source_line_end}"


def load_dram_module_steps(
    path: Path,
    *,
    source_commit: str,
    expected_sha256: str,
) -> list[DramModuleStep]:
    """Validate a complete pinned table before returning any support rows.

    The SHA-256 binds the bytes actually parsed. The full source commit is
    caller-supplied provenance; this offline loader does not query GitHub to
    establish that the bytes belong to that commit. The fixed native schema is
    checked exactly so changed, missing, or extra fields cannot disappear.
    """
    if not isinstance(source_commit, str) or not re.fullmatch(r"[a-fA-F0-9]{40}", source_commit):
        raise ValueError("DRAM source_commit must be 40 hexadecimal characters")
    if not isinstance(expected_sha256, str) or not re.fullmatch(
        r"[a-fA-F0-9]{64}", expected_sha256
    ):
        raise ValueError("DRAM expected_sha256 must be 64 hexadecimal characters")
    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if digest != expected_sha256.lower():
        raise ValueError("DRAM SHA-256 mismatch")
    try:
        reader = csv.reader(
            io.StringIO(payload.decode("utf-8-sig"), newline=""),
            delimiter="\t",
            strict=True,
        )
        header = next(reader, None)
        if header is None:
            raise ValueError("DRAM module-step table is empty")
        if tuple(header) != DRAM_NATIVE_HEADER:
            raise ValueError("DRAM module-step table must have the exact nine-column native header")
        records = []
        start = reader.line_num + 1
        for values in reader:
            end = reader.line_num
            if len(values) != len(DRAM_NATIVE_HEADER):
                raise ValueError(f"DRAM lines {start}-{end}: expected nine fields")
            # Blank chemical fields are common. Only the row's native identity
            # and description fields are mandatory; their spelling is unaltered.
            for name, value in zip(DRAM_NATIVE_HEADER[:5], values[:5], strict=True):
                if not value.strip():
                    raise ValueError(f"DRAM lines {start}-{end}: missing {name}")
            records.append(
                DramModuleStep(
                    native_fields=tuple(zip(DRAM_NATIVE_HEADER, values, strict=True)),
                    source_file=path.name,
                    source_commit=source_commit.lower(),
                    source_sha256=digest,
                    source_line_start=start,
                    source_line_end=end,
                )
            )
            start = end + 1
    except (UnicodeDecodeError, csv.Error) as error:
        raise ValueError(f"Malformed DRAM module-step table: {error}") from error
    if not records:
        raise ValueError("DRAM module-step table contains no data rows")
    return records


def dram_seed_rows(records: list[DramModuleStep]) -> list[str]:
    """Render every row in order, preserving duplicates, blanks and controls."""
    result = [DRAM_SEED_HEADER]
    for record in records:
        values = [value for _, value in record.native_fields]
        values.extend(
            [
                record.source_row_id,
                record.source_file,
                record.source_commit,
                record.source_path,
                record.source_url,
                record.source_sha256,
                str(record.source_line_start),
                str(record.source_line_end),
                json.dumps(record.native_fields, ensure_ascii=True, separators=(",", ":")),
            ]
        )
        buffer = io.StringIO(newline="")
        csv.writer(buffer, delimiter="\t", lineterminator="\r\n").writerow(values)
        result.append(buffer.getvalue().removesuffix("\r\n"))
    return result
