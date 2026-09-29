from __future__ import annotations

import re
from pathlib import Path

XREF_PATTERNS = (
    ("CAS", re.compile(r"\bCAS(?::| Registry Number:)(\d{2,7}-\d{2}-\d)\b", re.I)),
    ("ChemSpider", re.compile(r"\bChemSpider:(\d+)\b", re.I)),
    ("HMDB", re.compile(r"\bHMDB:(HMDB\d+)\b", re.I)),
    ("KEGG", re.compile(r"\bKEGG(?:\s+COMPOUND)?:(C\d{5})\b", re.I)),
    ("PubChem", re.compile(r"\bPubChem(?:[-\s]Compound)?:(\d+)\b", re.I)),
)


def load_chebi_xrefs(path: Path) -> dict[str, str]:
    """Return chemical database to ChEBI CURIE mappings from a ChEBI OBO file."""
    mappings: dict[str, str] = {}
    current_id: str | None = None
    current_xrefs: set[str] = set()
    is_obsolete = False

    def flush() -> None:
        if not current_id or is_obsolete:
            return
        for source_curie in current_xrefs:
            mappings.setdefault(source_curie, current_id)

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line == "[Term]":
            flush()
            current_id = None
            current_xrefs = set()
            is_obsolete = False
            continue
        if line.startswith("id: CHEBI:"):
            current_id = line.removeprefix("id: ")
        elif line == "is_obsolete: true":
            is_obsolete = True
        elif line.startswith("xref:"):
            current_xrefs.update(_xref_curies(line))

    flush()
    return mappings


def _xref_curies(line: str) -> list[str]:
    curies = []
    for prefix, pattern in XREF_PATTERNS:
        for local_id in pattern.findall(line):
            curies.append(f"{prefix}:{local_id}")
    return curies
