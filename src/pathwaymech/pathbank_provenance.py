"""Closed provenance contract for independently acquired PathBank ZIP members."""

from __future__ import annotations

import re
from typing import Any

PATHBANK_ARCHIVE_KIND = "pathbank-biopax-zip"
PATHBANK_ARCHIVE_URL = "https://pathbank.org/downloads/pathbank_primary_biopax.zip"


def validate_pathbank_archive(url: str, sha256: str, archive: Any) -> None:
    """Check typed bindings; the builder additionally verifies the original bytes."""
    if url != PATHBANK_ARCHIVE_URL:
        raise ValueError("PathBank ZIP requires the exact official archive URL")
    if not isinstance(sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", sha256):
        raise ValueError("PathBank ZIP requires an exact archive SHA-256")
    if not isinstance(archive, dict) or archive.keys() != {
        "bytes", "member", "member_bytes", "member_sha256", "root",
    }:
        raise ValueError("PathBank ZIP requires a closed archive provenance object")
    if any(type(archive[key]) is not int or archive[key] <= 0
           for key in ("bytes", "member_bytes")):
        raise ValueError("PathBank ZIP archive/member byte counts must be positive integers")
    patterns = {
        "member": r"PW[0-9]+\.owl",
        "member_sha256": r"[0-9a-f]{64}",
        "root": r"SMP[0-9]+",
    }
    if any(not isinstance(archive[key], str) or not re.fullmatch(pattern, archive[key])
           for key, pattern in patterns.items()):
        raise ValueError("PathBank ZIP requires exact native member, hash and root identities")
