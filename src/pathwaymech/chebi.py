from __future__ import annotations

import re
from pathlib import Path

from pathwaymech.source_mapping import CurieMapping

XREF_PATTERNS = (
    ("CAS", re.compile(r"\bCAS(?::| Registry Number:)\s*(\d{2,7}-\d{2}-\d)\b", re.I)),
    ("ChemSpider", re.compile(r"\bChemSpider:\s*(\d+)\b", re.I)),
    ("HMDB", re.compile(r"\bHMDB:\s*(HMDB\d+)\b", re.I)),
    ("KEGG", re.compile(r"\bKEGG(?:\s+COMPOUND)?:\s*(C\d{5})\b", re.I)),
    ("PubChem", re.compile(r"\bPubChem(?:[-\s]Compound)?:\s*(\d+)\b", re.I)),
)
XREF_LABEL = re.compile(r'"([^"]+)"')


def load_chebi_xrefs(path: Path) -> dict[str, CurieMapping]:
    """Return chemical database to ChEBI CURIE mappings from a ChEBI OBO file."""
    mappings: dict[str, CurieMapping] = {}
    current_id: str | None = None
    current_name: str | None = None
    current_xrefs: dict[str, str] = {}
    in_term = False
    is_obsolete = False

    def flush() -> None:
        if not current_id or is_obsolete:
            return
        for source_curie, source_label in current_xrefs.items():
            mappings.setdefault(
                source_curie,
                CurieMapping(
                    subject_id=source_curie,
                    subject_label=source_label,
                    object_id=current_id,
                    object_label=current_name or current_id,
                ),
            )

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("[") and line.endswith("]"):
            flush()
            current_id = None
            current_name = None
            current_xrefs = {}
            in_term = line == "[Term]"
            is_obsolete = False
            continue
        if not in_term:
            continue
        if line.startswith("id: CHEBI:"):
            current_id = line.removeprefix("id: ")
        elif line.startswith("name:"):
            current_name = line.removeprefix("name:").strip()
        elif line == "is_obsolete: true":
            is_obsolete = True
        elif line.startswith("xref:"):
            current_xrefs.update(_xref_curies(line))

    flush()
    return mappings


def _xref_curies(line: str) -> dict[str, str]:
    curies = {}
    label = _xref_label(line)
    for prefix, pattern in XREF_PATTERNS:
        for local_id in pattern.findall(line):
            curie = f"{prefix}:{local_id}"
            curies[curie] = label or curie
    return curies


def _xref_label(line: str) -> str | None:
    match = XREF_LABEL.search(line)
    return match.group(1) if match else None
