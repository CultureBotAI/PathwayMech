"""Publication safeguards for bounded curation migrations.

Compute and validate the complete cohort before publishing. Historical applied
ledgers, including legacy ledgers without an ``applied`` flag, are immutable.
"""

from __future__ import annotations

import json
import subprocess
import tempfile
from collections.abc import Callable, Mapping, Sequence
from functools import cache
from pathlib import Path
from typing import Any

import yaml

from pathwaymech.schema import validate_record

CAUSAL_REVIEW_BASELINE = "88744403c934a84828d373cfccb8cdaa7507ad77"


@cache
def _closed_validator():
    from pathwaymech.strict import validator

    return validator()


def require(condition: bool, message: str) -> None:
    """Check a migration precondition even when Python runs with ``-O``."""
    if not condition:
        raise ValueError(message)


def guard_baseline(paths: Sequence[Path], revision: str, root: Path | None = None) -> None:
    """Refuse to reconstruct over records changed since the reviewed baseline."""
    if not paths:
        raise ValueError("No migration targets were selected")
    if root is None:
        root = Path(
            subprocess.check_output(
                ["git", "-C", str(paths[0].resolve().parent), "rev-parse", "--show-toplevel"],
                text=True,
            ).strip()
        )
    root = root.resolve()
    changed = []
    for path in paths:
        relative = path.resolve().relative_to(root)
        expected = subprocess.check_output(["git", "show", f"{revision}:{relative}"], cwd=root)
        if path.read_bytes() != expected:
            changed.append(str(relative))
    if changed:
        raise ValueError(
            "Migration baseline differs for "
            + ", ".join(changed)
            + ". Reproduce in an isolated checkout of "
            + revision
            + "."
        )


def changed_records(records: Sequence[tuple[Path, dict]]) -> list[tuple[Path, dict]]:
    """Ignore serializer-only changes and genuinely idempotent replays."""
    return [
        (path, record) for path, record in records if yaml.safe_load(path.read_text()) != record
    ]


def may_publish_report(path: Path, changed: int) -> bool:
    """Protect both marked applied reports and unmarked historical ledgers."""
    if not path.exists():
        return True
    try:
        existing = json.loads(path.read_text())
    except (json.JSONDecodeError, UnicodeDecodeError):
        existing = {}
    if not isinstance(existing, dict) or existing.get("applied") is not False:
        if changed:
            raise ValueError("An applied or legacy review ledger exists; choose a new report path")
        return False
    return True


def publish_curation(
    records: Sequence[tuple[Path, dict]],
    report_path: Path,
    report: dict[str, Any],
    *,
    apply: bool,
    serialize: Callable[[dict], str] | None = None,
    extra_reports: Mapping[Path, str] | None = None,
    baseline: tuple[Sequence[Path], str, Path | None] | None = None,
) -> int:
    """Preflight all records and report destinations before the first write.

    A dry run may create a new, explicitly designated preview report. It never
    changes records or overwrites an applied/legacy ledger. Applied no-op replay
    preserves that ledger byte for byte.
    """
    if baseline is not None:
        guard_baseline(*baseline)
    for path, record in records:
        validate_record(record)
        errors = list(_closed_validator().validate(record, "PathwayRecord").results)
        if errors:
            raise ValueError(f"{path}: " + "; ".join(error.message for error in errors))
    pending = changed_records(records)
    publish = may_publish_report(report_path, len(pending))
    if not publish:
        return 0
    extras = extra_reports or {}
    for path, content in extras.items():
        if path.exists() and (not path.is_file() or path.read_text() != content):
            raise ValueError(
                f"Existing supplemental ledger requires a new report directory: {path}"
            )
    record_paths = {path.resolve() for path, _ in records}
    require(len(record_paths) == len(records), "Duplicate migration target paths")
    report_paths = {report_path.resolve(), *(path.resolve() for path in extras)}
    require(not record_paths.intersection(report_paths), "A report cannot overwrite a record")
    require(len(report_paths) == len(extras) + 1, "Duplicate report destinations")
    serializer = serialize or (
        lambda value: yaml.safe_dump(
            value,
            sort_keys=False,
            allow_unicode=True,
            width=100,
        )
    )
    outputs = [(path, serializer(record)) for path, record in pending] if apply else []
    payload = json.dumps({**report, "applied": apply}, indent=2) + "\n"
    outputs.extend([(report_path, payload), *extras.items()])
    # Stage every output before replacing any destination: an unwritable report
    # directory must not leave already-published records without their ledger.
    staged = []
    try:
        for path, content in outputs:
            require(not path.exists() or path.is_file(), f"Not a file destination: {path}")
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=path.parent,
                prefix=f".{path.name}.",
                suffix=".tmp",
                delete=False,
            ) as stream:
                temporary = Path(stream.name)
                staged.append((temporary, path))
                stream.write(content)
            temporary.chmod(path.stat().st_mode & 0o777 if path.exists() else 0o644)
        for temporary, path in staged:
            temporary.replace(path)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)
    return len(pending)
