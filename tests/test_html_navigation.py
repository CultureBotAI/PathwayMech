from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace

from pathwaymech.cli import _record_page, _reference_url, render_pages_main, render_site


class Elements(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


def record():
    return SimpleNamespace(id="GO:42", label="Example", description="A pathway",
        participants=[{"id": "CHEBI:1", "label": '<script>Substrate</script>'}],
        taxa=[], reactions=[], gene_clusters=[],
        references=[{"id": "PMID:123", "title": "Source paper"},
                    {"id": "DOI:10.1/paper", "citation": "Second source"}],
        mechanistic_edges=[{"id": "edge-1", "subject": "CHEBI:1", "predicate": "produces",
            "object": "UNKNOWN:2", "description": "Only the source claim", "evidence": [
                {"reference_id": "PMID:123", "quote": "A < B & C"},
                {"reference_id": "DOI:10.1/paper", "quote": "Second quote"}]}])


def test_record_displays_declared_labels_each_evidence_quote_and_real_source_path():
    page = _record_page(record(), "data/pathways/a source.yaml")
    parsed = Elements()
    parsed.feed(page)
    text = " ".join(parsed.text)
    for expected in ["<script>Substrate</script>", "CHEBI:1", "UNKNOWN:2", "produces",
                     "Only the source claim", "A < B & C", "Second quote",
                     "Source paper", "Second source"]:
        assert expected in text
    assert not any(tag == "script" for tag, _ in parsed.elements)
    links = [attrs.get("href") for tag, attrs in parsed.elements if tag == "a"]
    for link in ["../browse.html", "../index.html", "#reference-1", "#reference-2",
                 "https://culturebotai.github.io/mechs/",
                 "https://github.com/CultureBotAI/PathwayMech/blob/main/data/pathways/a%20source.yaml"]:
        assert link in links
    assert sum(tag == "main" for tag, _ in parsed.elements) == 1
    assert any(attrs.get("role") == "region" and attrs.get("tabindex") == "0"
               for _, attrs in parsed.elements)


def test_browse_keeps_all_records_and_source_path_association():
    pages = render_site([record()], {"GO:42": "data/pathways/unrelated-filename.yaml"})
    assert 'href="records/GO_42.html"' in pages["browse.html"]
    assert 'id="pathway-query"' in pages["browse.html"]
    assert 'type="reset"' in pages["browse.html"]
    assert 'unrelated-filename.yaml' in pages["records/GO_42.html"]


def test_published_record_has_navigation_and_source_link():
    root = Path(__file__).resolve().parents[1]
    page = (root / "pages/records/WikiPathways_WP5587.html").read_text()
    assert 'href="../browse.html"' in page
    assert 'data/pathways/2-phenylethanol-biosynthesis.yaml' in page


def test_reference_routes_and_ambiguous_labels_remain_truthful():
    assert _reference_url("PMID:123") == "https://pubmed.ncbi.nlm.nih.gov/123/"
    assert _reference_url("DOI:10.1/a b") == "https://doi.org/10.1/a%20b"
    assert _reference_url("RHEA:12345") == "https://www.rhea-db.org/rhea/12345"
    assert _reference_url("CUSTOM:123") is None
    assert _reference_url("PMID:not-a-number") is None
    sample = record()
    sample.reactions = [{"id": "CHEBI:1", "label": "Conflicting name"}]
    page = _record_page(sample)
    assert "Conflicting name" not in page and "&lt;script&gt;Substrate" not in page
    assert "CHEBI:1" in page
    sample.participants = [{"id": "CHEBI:1", "label": ""}]
    sample.reactions = []
    assert "<code>CHEBI:1</code>" in _record_page(sample)


def test_renderer_links_nested_actual_source_filename(tmp_path):
    import shutil

    root = Path(__file__).resolve().parents[1]
    nested = tmp_path / "data/pathways/subfolder/actual-source-name.yaml"
    nested.parent.mkdir(parents=True)
    shutil.copy(root / "data/pathways/2-phenylethanol-biosynthesis.yaml", nested)
    assert render_pages_main([], root=tmp_path) == 0
    page = (tmp_path / "pages/records/WikiPathways_WP5587.html").read_text()
    assert 'data/pathways/subfolder/actual-source-name.yaml' in page
