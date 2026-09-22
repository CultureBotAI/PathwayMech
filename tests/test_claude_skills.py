from __future__ import annotations

from scripts.validate_claude_skills import SKILLS_DIR, validate_skills


def test_claude_skills_validate() -> None:
    assert validate_skills() == []


def test_expected_claude_skills_exist() -> None:
    names = {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}

    assert {
        "add-pathway",
        "review-open-issues",
        "review-yaml-category",
        "review-yaml-record",
        "source-triage",
    } <= names
