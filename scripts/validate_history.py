#!/usr/bin/env python3
"""Validate repository history records against the vendored claw schema.

One implementation, called by both `just validate-history` and `scripts/run_qc.py`,
so the gate does not depend on the task runner being installed — CI runs qc with
uv alone, and a `just` shell-out failed there with exit 127 (#54).

    python scripts/validate_history.py                 # everything under history/
    python scripts/validate_history.py history/records/x/y.yaml
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA = REPO_ROOT / "src" / "pathwaymech" / "schema" / "history.yaml"
TARGET_CLASS = "HistoryRecord"


def linkml_validate() -> str:
    """The linkml-validate installed beside this interpreter.

    A bare name resolves only when the virtualenv is on PATH, as under `uv run`;
    run any other way it raised FileNotFoundError instead of validating (#211).
    """
    beside = Path(sys.executable).with_name("linkml-validate")
    return str(beside) if beside.exists() else "linkml-validate"


def records(target: Path) -> list[Path]:
    if target.is_dir():
        return sorted(target.rglob("*.yaml"))
    return [target]


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "history"
    if not target.exists():
        print(f"validate-history: {target} does not exist", file=sys.stderr)
        return 2
    paths = records(target)
    if not paths:
        print(f"No history records under {target}.")
        return 0

    # Link check first: it explains a bad URL better than the schema's uri error.
    links = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "validate_history_links.py"), str(target)],
        cwd=REPO_ROOT, check=False,
    )
    if links.returncode:
        return links.returncode

    result = subprocess.run(
        [linkml_validate(), "--schema", str(SCHEMA), "--target-class", TARGET_CLASS,
         *[str(p) for p in paths]],
        cwd=REPO_ROOT, check=False,
    )
    if result.returncode:
        return result.returncode
    print(f"{len(paths)} history record(s) valid against {SCHEMA.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
