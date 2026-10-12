"""Historical replay must not silently absorb a later pathway cohort."""

import runpy
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "research/cross_mech/2026-10-05/reproduce.py"


def test_dated_audit_reads_pinned_pathways_after_checkout_changes(tmp_path):
    def git(*args):
        return subprocess.check_output(["git", "-C", str(tmp_path), *args], text=True).strip()

    git("init", "-q")
    git("config", "user.name", "Test")
    git("config", "user.email", "test@example.invalid")
    record = tmp_path / "data/pathways/example.yaml"
    record.parent.mkdir(parents=True)
    record.write_text("id: old\nlabel: Historical pathway\n")
    git("add", ".")
    git("commit", "-qm", "historical cohort")
    pin = git("rev-parse", "HEAD")
    record.write_text("id: replacement\nlabel: Later pathway\n")
    git("add", ".")
    git("commit", "-qm", "later cohort")
    record.write_text("invalid: [dirty working tree")
    (record.parent / "untracked.yaml").write_text("id: untracked\n")

    replay = runpy.run_path(str(SCRIPT))
    load = replay["pathway_records"]
    load.__globals__["PATHWAY_PIN"] = pin
    assert load(tmp_path) == [{"id": "old", "label": "Historical pathway"}]


def test_dated_audit_refuses_missing_pathway_pin(tmp_path):
    replay = runpy.run_path(str(SCRIPT))
    with pytest.raises(OSError, match="not a commit"):
        replay["pathway_records"](tmp_path)
