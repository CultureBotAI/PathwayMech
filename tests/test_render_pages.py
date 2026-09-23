from __future__ import annotations

from types import SimpleNamespace

from pathwaymech.cli import _page, _record_page, _slug


def test_slug_uses_safe_path_characters() -> None:
    assert _slug("GO:0006096") == "GO_0006096"


def test_page_escapes_title() -> None:
    page = _page("<Pathway>", "<p>ok</p>")

    assert "<title>&lt;Pathway&gt;</title>" in page


def test_record_page_uses_parent_stylesheet() -> None:
    record = SimpleNamespace(
        label="<Pathway>",
        description="ok",
        mechanistic_edges=[],
    )

    page = _record_page(record)

    assert 'href="../style.css"' in page
    assert "<title>&lt;Pathway&gt;</title>" in page
