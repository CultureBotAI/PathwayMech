"""Publication safeguards for bounded curation migrations.

Compute and validate the complete cohort before publishing. Historical applied
ledgers, including legacy ledgers without an ``applied`` flag, are immutable.
"""

from __future__ import annotations

import json
import subprocess
import tempfile
from collections.abc import Callable, Mapping, Sequence
from copy import deepcopy
from functools import cache
from pathlib import Path
from typing import Any

import yaml

from pathwaymech.schema import validate_record

CAUSAL_REVIEW_BASELINE = "88744403c934a84828d373cfccb8cdaa7507ad77"
_CANDIDATE_YAML_WIDTHS = (100, 88, 80, 120, 4096)


def _collect_anchored_subtrees(value: Any) -> list[Any]:
    """Return list/dict subtrees referenced multiple times (YAML anchors/aliases)."""
    seen: dict[int, Any] = {}
    repeated_ids: set[int] = set()
    ordered_ids: list[int] = []

    def _walk(node: Any) -> None:
        if not isinstance(node, (dict, list)):
            return
        obj_id = id(node)
        if obj_id in seen:
            if obj_id not in repeated_ids:
                repeated_ids.add(obj_id)
                ordered_ids.append(obj_id)
            return
        seen[obj_id] = node
        if isinstance(node, dict):
            for child in node.values():
                _walk(child)
        else:
            for child in node:
                _walk(child)

    _walk(value)
    return [deepcopy(seen[obj_id]) for obj_id in ordered_ids]


def _restore_yaml_anchors(value: Any, anchored_subtrees: Sequence[Any]) -> Any:
    """Re-link equal list/dict subtrees to shared instances so safe_dump emits aliases."""
    if not anchored_subtrees:
        return value
    shared_targets = [deepcopy(item) for item in anchored_subtrees]

    def _relink(node: Any) -> Any:
        if not isinstance(node, (dict, list)):
            return node
        for target in shared_targets:
            if type(node) is type(target) and node == target:
                return target
        if isinstance(node, dict):
            return {key: _relink(child) for key, child in node.items()}
        return [_relink(child) for child in node]

    return _relink(deepcopy(value))


def _detect_yaml_width(existing_text: str, existing_value: Any) -> int:
    """Detect the wrap width of an existing YAML file, defaulting to 100."""
    if not isinstance(existing_value, dict):
        return 100
    existing_lines = existing_text.splitlines()
    best_width = 100
    best_score = -1
    for width in _CANDIDATE_YAML_WIDTHS:
        dumped = yaml.safe_dump(
            existing_value,
            sort_keys=False,
            allow_unicode=True,
            width=width,
        )
        if dumped == existing_text:
            return width
        dumped_lines = dumped.splitlines()
        overlap = sum(
            1
            for left, right in zip(existing_lines, dumped_lines, strict=False)
            if left == right
        )
        score = overlap * 2 - abs(len(existing_lines) - len(dumped_lines))
        if score > best_score:
            best_score = score
            best_width = width
    return best_width


def _serialize_record(path: Path, record: dict) -> str:
    """Serialize a record while preserving existing wrap width and YAML anchor aliases."""
    width = 100
    value: Any = record
    if path.exists() and path.is_file():
        try:
            existing_text = path.read_text(encoding="utf-8")
            existing_value = yaml.safe_load(existing_text)
        except (OSError, yaml.YAMLError):
            existing_text = ""
            existing_value = None
        if isinstance(existing_value, dict):
            width = _detect_yaml_width(existing_text, existing_value)
            anchored = _collect_anchored_subtrees(existing_value)
            if anchored:
                value = _restore_yaml_anchors(record, anchored)
    return yaml.safe_dump(
        value,
        sort_keys=False,
        allow_unicode=True,
        width=width,
    )


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
    outputs = (
        [
            (path, serialize(record) if serialize is not None else _serialize_record(path, record))
            for path, record in pending
        ]
        if apply
        else []
    )
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
