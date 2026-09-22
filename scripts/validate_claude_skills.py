#!/usr/bin/env python3
"""Validate local Claude skill layout and frontmatter."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".claude" / "skills"
REQUIRED_FRONTMATTER = {"name", "description"}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    try:
        _, header, _ = text.split("---", 2)
    except ValueError as error:
        raise ValueError("unterminated YAML frontmatter") from error
    value = yaml.safe_load(header)
    if not isinstance(value, dict):
        raise ValueError("frontmatter must be a mapping")
    return value


def validate_skills() -> list[str]:
    errors: list[str] = []
    if not SKILLS_DIR.is_dir():
        return [".claude/skills: missing skill directory"]

    for loose_markdown in sorted(SKILLS_DIR.glob("*.md")):
        errors.append(f"{loose_markdown.relative_to(ROOT)}: use <skill>/SKILL.md layout")

    seen_names: dict[str, Path] = {}
    for directory in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{directory.relative_to(ROOT)}: missing SKILL.md")
            continue
        try:
            metadata = frontmatter(skill_file)
        except ValueError as error:
            errors.append(f"{skill_file.relative_to(ROOT)}: {error}")
            continue

        missing = sorted(REQUIRED_FRONTMATTER - metadata.keys())
        if missing:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing {', '.join(missing)}")

        name = metadata.get("name")
        if name != directory.name:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: name must match directory "
                f"{directory.name!r}"
            )
        elif name in seen_names:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: duplicates name from "
                f"{seen_names[name].relative_to(ROOT)}"
            )
        elif isinstance(name, str):
            seen_names[name] = skill_file

        nested_metadata = metadata.get("metadata")
        nested_version = (
            nested_metadata.get("version") if isinstance(nested_metadata, dict) else None
        )
        if not metadata.get("version") and not nested_version:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing version")

    return errors


def main() -> int:
    errors = validate_skills()
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1

    count = len(list(SKILLS_DIR.glob("*/SKILL.md")))
    print(f"validated {count} Claude skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
