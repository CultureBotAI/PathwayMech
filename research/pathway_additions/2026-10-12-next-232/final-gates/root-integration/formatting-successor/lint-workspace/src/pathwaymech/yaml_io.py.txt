from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from pathwaymech.schema import PathwayRecord, validate_records


def pathway_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.yaml") if path.is_file())


def load_yaml_file(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        data = yaml.safe_load(stream)
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def load_pathway_records(root: Path) -> list[PathwayRecord]:
    return validate_records([load_yaml_file(path) for path in pathway_files(root)])
