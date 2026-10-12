from __future__ import annotations

import shutil
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from pathwaymech.cli import (
    _home_page,
    _page,
    _record_page,
    _slug,
    check_pages_main,
    render_pages_main,
)


def test_home_statistics_count_records_and_deduplicate_taxa_and_references() -> None:
    records = [
        SimpleNamespace(taxa=[{"id": "NCBITaxon:1"}], mechanistic_edges=[{}, {}],
                        references=[{"id": "PMID:1"}, {"id": "PMID:2"}]),
        SimpleNamespace(taxa=[{"id": "NCBITaxon:1"}], mechanistic_edges=[{}],
                        references=[{"id": "PMID:2"}]),
    ]
    page = _home_page(records)

    assert '<dt>Pathway records</dt><dd>2</dd>' in page
    assert '<dt>Taxa represented</dt><dd>1</dd>' in page
    assert '<dt>Mechanistic edges</dt><dd>3</dd>' in page
    assert '<dt>Distinct references</dt><dd>2</dd>' in page


def test_empty_home_collection_has_zero_statistics_and_working_navigation() -> None:
    page = _home_page([])

    assert page.count('<dd>0</dd>') == 4
    assert page.count('<h1') == 1
    assert 'href="browse.html"' in page
    assert 'href="https://culturebotai.github.io/mechs/"' in page


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
    assert (
        "pages/records/Removed_record.html: neither rendered from a record nor hand-kept"
        in capsys.readouterr().err
    )
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


def _record_with_id(site: Path, new_id: str, name: str, **changes: str) -> None:
    """A copy of a site record under a new id (every mention of the old id
    replaced, so its edges still resolve)."""
    source = sorted((site / "data" / "pathways").glob("*.yaml"))[0]
    old_id = yaml.safe_load(source.read_text())["id"]
    record = yaml.safe_load(source.read_text().replace(old_id, new_id))
    record.update(changes)
    (site / "data" / "pathways" / name).write_text(yaml.safe_dump(record, sort_keys=False))


@pytest.mark.parametrize(
    "stray", ["pathways.html", "records/old/WikiPathways_WP1.html", "records/WikiPathways_WP3.htm"]
)
def test_a_file_that_is_neither_rendered_nor_hand_kept_fails_the_check(
    site: Path, stray: str, capsys
) -> None:
    """The workflow publishes everything under pages/, so the check reads all of it."""
    (site / "pages" / stray).parent.mkdir(parents=True, exist_ok=True)
    (site / "pages" / stray).write_text("<html></html>")
    assert render_pages_main(["--check"], root=site) == 1
    assert f"pages/{stray}: neither rendered from a record nor hand-kept" in capsys.readouterr().err


def test_a_missing_hand_kept_file_fails_the_check(site: Path, capsys) -> None:
    (site / "pages" / "style.css").unlink()
    assert render_pages_main(["--check"], root=site) == 1
    assert "pages/style.css: hand-kept file is missing" in capsys.readouterr().err


def test_two_records_rendering_to_one_page_are_refused(site: Path, capsys) -> None:
    """Differing only in case is still one file on macOS, so still a collision."""
    _record_with_id(site, "WikiPathways:WPX1", "a.yaml")
    _record_with_id(site, "WikiPathways:wpx1", "b.yaml")
    assert render_pages_main([], root=site) == 1
    assert render_pages_main(["--check"], root=site) == 1
    assert "both render to pages/records/" in capsys.readouterr().err


def test_an_id_whose_case_changed_is_published_under_its_new_name(site: Path) -> None:
    _record_with_id(site, "WikiPathways:WPCASE", "case.yaml")
    assert render_pages_main([], root=site) == 0
    (site / "data" / "pathways" / "case.yaml").unlink()
    _record_with_id(site, "WikiPathways:wpcase", "case.yaml")

    assert render_pages_main([], root=site) == 0
    names = {p.name for p in (site / "pages" / "records").iterdir()}
    assert "WikiPathways_wpcase.html" in names and "WikiPathways_WPCASE.html" not in names
    assert render_pages_main(["--check"], root=site) == 0


def test_a_carriage_return_does_not_make_a_fresh_render_look_stale(site: Path) -> None:
    _record_with_id(site, "WikiPathways:WPCR", "cr.yaml", description="first line\r\nsecond")
    assert render_pages_main([], root=site) == 0
    assert render_pages_main(["--check"], root=site) == 0


def test_the_check_entry_point_fails_a_stale_site_and_writes_nothing(site: Path) -> None:
    """What CI's gate and the Pages refusal step run."""
    page = next((site / "pages" / "records").glob("*.html"))
    page.write_text("stale")
    assert check_pages_main(root=site) == 1
    assert page.read_text() == "stale"
    assert render_pages_main([], root=site) == 0
    assert check_pages_main(root=site) == 0
