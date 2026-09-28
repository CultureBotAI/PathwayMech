from __future__ import annotations

import shutil
from pathlib import Path
from types import SimpleNamespace

import pytest

from pathwaymech.cli import _page, _record_page, _slug, render_pages_main


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


# --------------------------------------------------------------------------
# Rendering and checking the committed site
# --------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def site(tmp_path: Path) -> Path:
    """A repository with two real records and a hand-kept stylesheet."""
    records = sorted((ROOT / "data" / "pathways").glob("*.yaml"))[:2]
    (tmp_path / "data" / "pathways").mkdir(parents=True)
    for record in records:
        shutil.copy(record, tmp_path / "data" / "pathways" / record.name)
    (tmp_path / "pages").mkdir()
    (tmp_path / "pages" / "style.css").write_text("body {}\n")
    (tmp_path / "pages" / ".nojekyll").write_text("\n")
    assert render_pages_main([], root=tmp_path) == 0
    return tmp_path


def test_a_fresh_render_checks_clean(site: Path) -> None:
    assert render_pages_main(["--check"], root=site) == 0


def test_a_page_that_differs_from_its_record_fails_the_check(site: Path, capsys) -> None:
    page = next((site / "pages" / "records").glob("*.html"))
    page.write_text(page.read_text() + "<!-- edited by hand -->")

    assert render_pages_main(["--check"], root=site) == 1
    assert f"pages/records/{page.name}: not what its record renders to" in capsys.readouterr().err


def test_a_missing_page_fails_the_check(site: Path) -> None:
    (site / "pages" / "browse.html").unlink()
    assert render_pages_main(["--check"], root=site) == 1


def test_a_page_whose_record_is_gone_fails_the_check_and_a_render_removes_it(
    site: Path, capsys
) -> None:
    """The renderer used to leave such pages published forever."""
    orphan = site / "pages" / "records" / "Removed_record.html"
    orphan.write_text("<html></html>")

    assert render_pages_main(["--check"], root=site) == 1
    assert "pages/records/Removed_record.html: no record renders it" in capsys.readouterr().err
    assert render_pages_main([], root=site) == 0
    assert not orphan.exists()
    assert render_pages_main(["--check"], root=site) == 0


def test_a_render_leaves_the_hand_kept_files_alone(site: Path) -> None:
    (site / "pages" / "style.css").write_text("body { color: red; }\n")
    assert render_pages_main([], root=site) == 0
    assert (site / "pages" / "style.css").read_text() == "body { color: red; }\n"
    assert (site / "pages" / ".nojekyll").is_file()


def test_the_check_writes_nothing(site: Path) -> None:
    page = next((site / "pages" / "records").glob("*.html"))
    page.write_text("stale")
    render_pages_main(["--check"], root=site)
    assert page.read_text() == "stale"


def test_the_committed_site_is_current() -> None:
    """The gate CI and `just validate` run, applied to the real repository."""
    assert render_pages_main(["--check"]) == 0


def test_the_quality_gate_runs_the_site_check(monkeypatch) -> None:
    """`just validate` and CI run the gate; a stale site must fail it."""
    import pathwaymech.cli as cli

    monkeypatch.setattr(cli, "check_pages_main", lambda: 1)
    assert cli.run_qc_main() == 1
