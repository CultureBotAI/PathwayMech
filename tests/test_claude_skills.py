from __future__ import annotations

import yaml

from scripts.validate_claude_skills import SKILLS_DIR, validate_skills


def test_claude_skills_validate() -> None:
    assert validate_skills() == []


def test_expected_claude_skills_exist() -> None:
    names = {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}

    assert {
        "add-pathway",
        "cross-mech-protein-links",
        "pathwaymech-discover-sources",
        "review-open-issues",
        "review-yaml-category",
        "review-yaml-record",
        "source-triage",
    } <= names


def test_cross_mech_assessment_is_a_registered_review_route() -> None:
    root = SKILLS_DIR.parent.parent
    profile = yaml.safe_load((root / "conf/record_review.yaml").read_text())
    assert ".claude/skills/cross-mech-protein-links/SKILL.md" in profile["skills"]


def test_agents_skills_symlink_exposes_claude_skills_including_review_open_issues() -> None:
    root = SKILLS_DIR.parent.parent
    agents_md = root / "AGENTS.md"
    assert agents_md.is_file()
    assert "CLAUDE.md" in agents_md.read_text(encoding="utf-8")
    assert ".agents/skills" in agents_md.read_text(encoding="utf-8")

    agents_skills = root / ".agents" / "skills"
    assert agents_skills.is_symlink()
    assert str(agents_skills.readlink()) == "../.claude/skills"
    assert agents_skills.resolve() == SKILLS_DIR.resolve()
    review_skill = agents_skills / "review-open-issues" / "SKILL.md"
    assert review_skill.resolve() == (SKILLS_DIR / "review-open-issues" / "SKILL.md").resolve()
    review_text = review_skill.read_text(encoding="utf-8")
    assert "PathwayMech" in review_text
    assert "read-only" in review_text.lower()
