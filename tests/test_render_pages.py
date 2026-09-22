from __future__ import annotations

from pathwaymech.cli import _page, _slug


def test_slug_uses_safe_path_characters() -> None:
    assert _slug("GO:0006096") == "GO_0006096"


def test_page_escapes_title() -> None:
    page = _page("<Pathway>", "<p>ok</p>")

    assert "<title>&lt;Pathway&gt;</title>" in page
