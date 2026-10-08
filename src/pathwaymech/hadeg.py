"""Read pinned HADEG source memberships without inferring pathway mechanisms.

Identifier patterns identify namespace candidates only. This module does not
resolve accessions with their issuers or establish biological pathway membership.
"""

from __future__ import annotations

import csv
import hashlib
import io
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path

HADEG_COLUMNS = (
    "Mechanism",
    "Compound",
    "Pathway",
    "Subpathway",
    "Protein_ID",
    "Gene",
    "code_mechanism",
    "code_compound",
    "code_subpathway",
)
HADEG_SOURCE_PATH = "Tables/7_All_pathways.csv"
_UNIPROT_CANDIDATE = re.compile(
    r"(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|"
    r"[A-NR-Z][0-9][A-Z][A-Z0-9]{2}[0-9](?:[A-Z][A-Z0-9]{2}[0-9])?)"
)
_NCBI_PROTEIN_CANDIDATE = re.compile(
    r"(?:[A-Z]{3}(?:[0-9]{5}|[0-9]{7})|"
    r"(?:AP|NP|XP|YP|WP|ZP)_[0-9]{6,9})\.[1-9][0-9]*"
)
_CONTROL_CHARACTERS = re.compile(r"[\x00-\x1f\x7f-\x9f\u2028\u2029]")


@dataclass(frozen=True)
class HadegMembership:
    """One observed CSV row; neither a resolved identifier nor a pathway record."""

    raw_values: tuple[str, ...]
    source_commit: str
    source_sha256: str
    source_line: int

    @property
    def source_url(self) -> str:
        return (
            f"https://raw.githubusercontent.com/jarojasva/HADEG/{self.source_commit}/"
            f"{HADEG_SOURCE_PATH}"
        )

    @property
    def source_locator(self) -> str:
        return f"{HADEG_SOURCE_PATH}:line={self.source_line}"

    @property
    def protein_id(self) -> str:
        return self.raw_values[4]

    @property
    def identifier_candidate(self) -> str:
        return self.protein_id.strip()

    @property
    def candidate_namespace(self) -> str:
        if _UNIPROT_CANDIDATE.fullmatch(self.identifier_candidate):
            return "UniProtKB"
        if _NCBI_PROTEIN_CANDIDATE.fullmatch(self.identifier_candidate):
            return "NCBIProtein"
        return "unresolved"

    @property
    def identifier_verification(self) -> str:
        return "not_verified"


def load_hadeg_memberships(
    path: Path, *, source_commit: str, expected_sha256: str
) -> list[HadegMembership]:
    """Validate the complete local artifact before returning any observations.

    The caller provides the expected upstream commit and artifact hash. Matching
    those inputs validates local integrity, not the source's scientific claims.
    """
    if not re.fullmatch(r"[0-9a-fA-F]{40}", source_commit):
        raise ValueError("HADEG source_commit must be a full 40-character hexadecimal commit")
    if not re.fullmatch(r"[0-9a-fA-F]{64}", expected_sha256):
        raise ValueError("HADEG expected_sha256 must be 64 hexadecimal characters")
    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if digest != expected_sha256.lower():
        raise ValueError(
            f"HADEG SHA-256 mismatch: expected {expected_sha256.lower()}, got {digest}"
        )
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("HADEG CSV must be UTF-8") from error
    reader = csv.reader(io.StringIO(text, newline=""), strict=True)
    rows: list[HadegMembership] = []
    seen: set[tuple[str, ...]] = set()
    try:
        header = next(reader, None)
        if header != list(HADEG_COLUMNS):
            raise ValueError("HADEG CSV must have exactly the nine expected columns in order")
        for values in reader:
            line = reader.line_num
            if len(values) != len(HADEG_COLUMNS):
                raise ValueError(f"HADEG CSV line {line}: expected nine fields, got {len(values)}")
            for column, value in zip(HADEG_COLUMNS, values, strict=True):
                if not value.strip():
                    raise ValueError(f"HADEG CSV line {line}: blank {column}")
                if _CONTROL_CHARACTERS.search(value):
                    raise ValueError(f"HADEG CSV line {line}: control character in {column}")
            raw_values = tuple(values)
            if raw_values in seen:
                raise ValueError(f"HADEG CSV line {line}: duplicate source row")
            seen.add(raw_values)
            rows.append(HadegMembership(raw_values, source_commit.lower(), digest, line))
    except csv.Error as error:
        raise ValueError(f"HADEG CSV line {reader.line_num}: malformed CSV: {error}") from error
    if not rows:
        raise ValueError("HADEG CSV contains no membership rows")
    return rows


def hadeg_seed_rows(records: Iterable[HadegMembership]) -> Iterator[str]:
    """Render validated memberships as TSV lines, without trailing newlines."""
    yield _tsv_line(
        (
            "source",
            "source_version",
            "source_url",
            "source_sha256",
            "source_locator",
            "claim_type",
            *HADEG_COLUMNS,
            "identifier_candidate",
            "candidate_namespace",
            "identifier_verification",
        )
    )
    for record in records:
        yield _tsv_line(
            (
                "hadeg",
                record.source_commit,
                record.source_url,
                record.source_sha256,
                record.source_locator,
                "source_reported_group_membership",
                *record.raw_values,
                record.identifier_candidate,
                record.candidate_namespace,
                record.identifier_verification,
            )
        )


def _tsv_line(values: tuple[str, ...]) -> str:
    output = io.StringIO(newline="")
    csv.writer(output, delimiter="\t", lineterminator="").writerow(values)
    return output.getvalue()
