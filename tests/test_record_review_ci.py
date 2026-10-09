"""The review gate must not fall back to the modified HEAD on missing event data."""
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_review_workflow_requires_a_trusted_event_base():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    job = workflow["jobs"]["qc"]
    assert job["env"]["RECORD_REVIEW_BASE"] == (
        "${{ github.event.pull_request.base.sha || "
        "github.event.merge_group.base_sha || github.event.before }}"
    )
    checkout = next(
        step for step in job["steps"] if step.get("uses", "").startswith("actions/checkout@")
    )
    assert checkout["with"]["fetch-depth"] == 0


def test_missing_review_base_fails_even_with_no_reports():
    spec = importlib.util.spec_from_file_location(
        "record_review_ci", ROOT / "scripts/record_review.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.main(["--repo-root", str(ROOT), "check", "--base", ""]) == 1
