from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ALLOWED_INGEST_STATUSES = {
    "active",
    "deferred",
    "fixture",
    "license-gated",
    "next",
    "support",
}

SOURCE_ID_PATTERN = re.compile(r"^[a-z][a-z0-9-]*$")
SOURCE_SEED_HEADER = "priority\tid\tingest_status\tenabled\trole\tlabel"


class SourceInventoryError(ValueError):
    """Raised when the source inventory cannot seed an ingest queue."""

    def __init__(self, errors: list[str]) -> None:
        super().__init__("\n".join(errors))
        self.errors = errors


@dataclass(frozen=True)
class SourceConfig:
    priority: int
    id: str
    label: str
    enabled: bool
    ingest_status: str
    role: str
    homepage: str
    notes: str


def load_source_inventory(path: Path) -> list[SourceConfig]:
    with path.open(encoding="utf-8") as stream:
        config = yaml.safe_load(stream) or {}
    return validate_source_inventory(config)


def validate_source_inventory(config: Any) -> list[SourceConfig]:
    errors: list[str] = []
    if not isinstance(config, dict):
        raise SourceInventoryError(["source inventory must be a mapping"])

    raw_sources = config.get("sources")
    if not isinstance(raw_sources, list):
        raise SourceInventoryError(["sources must be a list"])

    sources = [
        source
        for index, raw_source in enumerate(raw_sources)
        if (source := _validate_source(raw_source, index, errors)) is not None
    ]

    _reject_duplicates(sources, "id", errors)
    _reject_duplicates(sources, "priority", errors)

    if errors:
        raise SourceInventoryError(errors)

    return sorted(sources, key=lambda source: (source.priority, source.id))


def source_seed_rows(sources: list[SourceConfig]) -> list[str]:
    rows = [SOURCE_SEED_HEADER]
    for source in sources:
        enabled = str(source.enabled).lower()
        rows.append(
            "\t".join(
                [
                    str(source.priority),
                    source.id,
                    source.ingest_status,
                    enabled,
                    source.role,
                    source.label,
                ]
            )
        )
    return rows


def _validate_source(
    value: Any,
    index: int,
    errors: list[str],
) -> SourceConfig | None:
    path = f"sources[{index}]"
    if not isinstance(value, dict):
        errors.append(f"{path} must be a mapping")
        return None

    original_error_count = len(errors)
    priority = _required_int(value, "priority", path, errors)
    source_id = _required_string(value, "id", path, errors)
    label = _required_string(value, "label", path, errors)
    enabled = _required_bool(value, "enabled", path, errors)
    ingest_status = _required_string(value, "ingest_status", path, errors)
    role = _required_string(value, "role", path, errors)
    homepage = _required_string(value, "homepage", path, errors)
    notes = _required_string(value, "notes", path, errors)

    if source_id and not SOURCE_ID_PATTERN.fullmatch(source_id):
        errors.append(f"{path}.id must use lowercase letters, digits, or hyphens")
    if ingest_status and ingest_status not in ALLOWED_INGEST_STATUSES:
        errors.append(f"{path}.ingest_status is not supported: {ingest_status!r}")
    if homepage and not homepage.startswith("https://"):
        errors.append(f"{path}.homepage must start with https://")

    if len(errors) > original_error_count:
        return None

    return SourceConfig(
        priority=priority,
        id=source_id,
        label=label,
        enabled=enabled,
        ingest_status=ingest_status,
        role=role,
        homepage=homepage,
        notes=notes,
    )


def _required_int(
    value: dict[str, Any],
    field: str,
    path: str,
    errors: list[str],
) -> int:
    raw = value.get(field)
    if type(raw) is not int or raw < 1:
        errors.append(f"{path}.{field} must be a positive integer")
        return 0
    return raw


def _required_bool(
    value: dict[str, Any],
    field: str,
    path: str,
    errors: list[str],
) -> bool:
    raw = value.get(field)
    if not isinstance(raw, bool):
        errors.append(f"{path}.{field} must be a boolean")
        return False
    return raw


def _required_string(
    value: dict[str, Any],
    field: str,
    path: str,
    errors: list[str],
) -> str:
    raw = value.get(field)
    if not isinstance(raw, str) or not raw.strip():
        errors.append(f"{path}.{field} must be a non-empty string")
        return ""
    return raw


def _reject_duplicates(
    sources: list[SourceConfig],
    field: str,
    errors: list[str],
) -> None:
    counts = Counter(getattr(source, field) for source in sources)
    for value, count in sorted(counts.items()):
        if count > 1:
            errors.append(f"duplicate source {field}: {value}")
