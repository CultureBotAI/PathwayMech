from __future__ import annotations

from pathlib import Path


def test_pathway_research_template_has_required_sections() -> None:
    template = Path("templates/pathway_mechanism_research.md").read_text(encoding="utf-8")

    for heading in [
        "## Pathway scope",
        "## Mechanistic summary",
        "## Evidence table",
        "## Gaps",
        "## Candidate YAML",
    ]:
        assert heading in template
