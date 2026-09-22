from __future__ import annotations

from pathlib import Path


def test_core_docs_exist() -> None:
    for path in [
        Path("README.md"),
        Path("CLAUDE.md"),
        Path("docs/CURATION.md"),
        Path("docs/DEEP_RESEARCH_PROVIDERS.md"),
        Path("docs/HARMONIZATION.md"),
        Path("docs/MERGE_QUEUE.md"),
    ]:
        assert path.exists()
