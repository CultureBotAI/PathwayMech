"""Offline Rhea quartet mappings for cross-corpus chemistry leads.

The undirected master groups the same chemical transformation; this does not
assert that an enzyme catalyses a particular physiological direction.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


def load_rhea_directions(path: Path) -> dict[str, str]:
    """Read an independently sourced, provenance-bearing direction map."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("format") != "rhea-directions/1":
        raise ValueError(f"{path}: unsupported Rhea directions format")
    source = data.get("source", {})
    if (not isinstance(source, dict)
            or not all(isinstance(source.get(key), str) and source[key]
                       for key in ("url", "retrieved_at", "license", "sha256"))
            or not re.fullmatch(r"[a-f0-9]{64}", source["sha256"])):
        raise ValueError(f"{path}: incomplete Rhea direction provenance")
    mapping = data.get("directions")
    if not isinstance(mapping, dict) or not mapping:
        raise ValueError(f"{path}: empty Rhea direction mapping")
    for direction, master in mapping.items():
        if (not isinstance(direction, str) or not direction.isdigit()
                or not isinstance(master, str) or not master.isdigit()
                or mapping.get(master) != master):
            raise ValueError(f"{path}: invalid Rhea quartet entry {direction!r}")
    return mapping


def master_ids(values, directions: dict[str, str]) -> set[str]:
    """Normalize known quartet members, preserving unknown IDs for exact joins."""
    ids = {str(value).rsplit(":", 1)[-1] for value in values}
    return {directions.get(value, value) for value in ids}
