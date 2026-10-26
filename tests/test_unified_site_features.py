"""The X-Mech website features the site provides, checked on rendered pages.

Each assertion is scoped to the part of the page the feature lives in: a link
that also appears in the navigation or another table would otherwise satisfy
an assertion about the section under test.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from dataclasses import replace
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import yaml

import pathwaymech.cli as cli
from pathwaymech.cli import (
    SITE_URL,
    SiteError,
    _record_page,
    _reference_url,
    _term_url,
    render_site,
)
from pathwaymech.schema import PathwayRecord
from pathwaymech.site_display import autolink_html, corpus_as_of, rich_text_html

ROOT = Path(__file__).resolve().parents[1]
HARNESS = Path(__file__).with_name("site_features_harness.cjs")
needs_node = pytest.mark.skipif(shutil.which("node") is None,
                                reason="Node is needed to execute browser logic")


def record(**changes) -> PathwayRecord:
    base = PathwayRecord(
        id="MetaCyc:PWY-TEST", label="Test pathway", description="Recorded description",
        pathway_type="cofactor-biosynthesis", taxa=[{"id": "NCBITaxon:562", "label": "E. coli"}],
        participants=[], reactions=[], mechanistic_edges=[], references=[],
    )
    return replace(base, **changes)


def between(text: str, start: str, end: str) -> str:
    """The first stretch of `text` from `start` up to the next `end`."""
    head = text.index(start)
    return text[head:text.index(end, head)]


def hrefs(fragment: str) -> list[str]:
    return [value.replace("&amp;", "&") for value in re.findall(r'href="([^"]*)"', fragment)]


def map_payload(page: str, script_id: str) -> dict:
    blob = re.search(rf'<script id="{script_id}" type="application/json">(.*?)</script>',
                     page, re.S)
    return json.loads(blob.group(1).replace("<\\/", "</"))


# --------------------------------------------------------------------------
# Embedding maps open the record a point stands for
# --------------------------------------------------------------------------

def _site_with_maps(tmp_path: Path, records: list[PathwayRecord]) -> Path:
    """Embedding files shaped like the committed ones, hrefs from YAML stems."""
    embeddings = tmp_path / "data" / "embeddings"
    embeddings.mkdir(parents=True)
    ids = [item.id for item in records]
    (embeddings / "corpus_map.json").write_text(json.dumps({
        "classes": ["cofactor-biosynthesis"],
        "hrefs": {identifier: f"records/yaml-stem-{n}.html" for n, identifier in enumerate(ids)},
        "points": [[0.1, 0.2, 0, identifier, "label", "cofactor-biosynthesis", "E. coli"]
                   for identifier in ids[:-1]],
    }))
    (embeddings / "sequence_map.json").write_text(json.dumps({"points": [{
        "x": 0.5, "y": 0.5, "protein_id": "UniProtKB:P00001", "label": "Protein",
        "organism": "E. coli", "class": "cofactor-biosynthesis",
        "primary_href": "records/yaml-stem-0.html",
        "records": [{"id": identifier, "label": "label", "href": f"records/yaml-stem-{n}.html"}
                    for n, identifier in enumerate(ids)],
    }]}))
    return tmp_path


def test_map_points_open_the_record_page_not_the_stored_yaml_stem_href(tmp_path):
    records = [record(id="MetaCyc:PWY-A", label="A"), record(id="MetaCyc:PWY-B", label="B"),
               record(id="GO:0000001", label="C")]
    files = render_site(records, root=_site_with_maps(tmp_path, records))
    text_map = map_payload(files["map.html"], "corpus-map-data")
    assert [point["url"] for point in text_map["points"]] == [
        "records/MetaCyc_PWY-A.html", "records/MetaCyc_PWY-B.html"]
    sequence = map_payload(files["sequence-map.html"], "seq-map-data")
    protein = sequence["proteins"][0]
    assert protein["url"] == "records/MetaCyc_PWY-A.html"
    assert protein["pathway_urls"] == ["records/MetaCyc_PWY-A.html",
                                       "records/MetaCyc_PWY-B.html", "records/GO_0000001.html"]
    assert {item["url"] for item in sequence["pathways"]} == {
        "records/MetaCyc_PWY-A.html", "records/MetaCyc_PWY-B.html", "records/GO_0000001.html"}
    for url in [*protein["pathway_urls"], *(p["url"] for p in text_map["points"])]:
        assert url in files


def test_a_point_for_an_unpublished_record_opens_nothing(tmp_path):
    published = [record(id="MetaCyc:PWY-A", label="A"), record(id="MetaCyc:PWY-B", label="B")]
    root = _site_with_maps(tmp_path, [*published, record(id="MetaCyc:GONE", label="Gone")])
    files = render_site(published, root=root)
    sequence = map_payload(files["sequence-map.html"], "seq-map-data")
    protein = sequence["proteins"][0]
    # Labels and links stay aligned, so the data table pairs each pathway with its page.
    assert protein["pathway_urls"] == ["records/MetaCyc_PWY-A.html",
                                       "records/MetaCyc_PWY-B.html", ""]
    assert len(protein["pathway_labels"]) == len(protein["pathway_urls"])
    assert {item["id"]: item["url"] for item in sequence["pathways"]}["MetaCyc:GONE"] == ""


def test_a_map_link_to_a_page_no_record_renders_fails_the_render(monkeypatch):
    real = cli._load_or_fallback_corpus_map

    def stale(records, root):
        payload = real(records, root)
        payload["points"][0]["url"] = "records/not-a-record.html"
        return payload

    monkeypatch.setattr(cli, "_load_or_fallback_corpus_map", stale)
    with pytest.raises(SiteError, match="records/not-a-record.html"):
        render_site([record()])


def test_the_text_map_names_the_published_records_it_does_not_plot(tmp_path):
    records = [record(id="MetaCyc:PWY-A", label="A"), record(id="MetaCyc:PWY-B", label="B"),
               record(id="GO:0000001", label="Not embedded")]
    page = render_site(records, root=_site_with_maps(tmp_path, records))["map.html"]
    coverage = between(page, '<p class="map-coverage">', "</p>")
    assert "2 of 3 published pathway records are plotted" in coverage
    assert "computed separately" in coverage and "corpus_map.json" in coverage
    assert hrefs(coverage) == ["records/GO_0000001.html"]
    assert "Not embedded" in coverage


def test_each_map_offers_its_data_as_a_keyboard_reachable_table():
    files = render_site([record()])
    for name, prefix in (("map.html", "map"), ("sequence-map.html", "seq")):
        page = files[name]
        table = between(page, f'<details class="map-table" id="{prefix}-table">', "</details>")
        assert "<summary>View data as table</summary>" in table, name
        assert re.search(r'<div class="table-scroll" role="region" tabindex="0" '
                         r'aria-label="[^"]+">', table), name
        assert hrefs(between(page, "<noscript>", "</noscript>")) == ["browse.html"], name


@needs_node
@pytest.mark.parametrize("name, scenario", [
    ("map.html", "map_table_lists_the_plotted_records_and_follows_the_search"),
    ("sequence-map.html", "sequence_table_links_each_proteins_pathways"),
])
def test_shipped_map_table(tmp_path, name, scenario):
    scripts = re.findall(r"<script>(.*?)</script>", render_site([record()])[name], re.S)
    assert len(scripts) == 1
    script = tmp_path / "map.js"
    script.write_text(scripts[0])
    result = subprocess.run(["node", str(HARNESS), str(script), scenario],
                            capture_output=True, text=True, timeout=15)
    assert result.returncode == 0, result.stdout + result.stderr
    assert f"Site feature passed: {scenario}" in result.stdout


def test_the_narrow_layout_keeps_a_wide_table_inside_its_scrolling_region():
    """At 390 px a bare `1fr` column grew to fit the open protein table, so the
    page scrolled sideways and the table's own region never did."""
    css = (ROOT / "pages/style.css").read_text()
    narrow = between(css, "@media (max-width: 860px) {", "\n}\n")
    rule = between(narrow, ".browse-layout {", "}")
    assert "grid-template-columns: minmax(0, 1fr);" in rule


def test_every_committed_map_point_opens_a_published_record():
    """The bug the review found: all 270 + 216 + 1,229 map URLs were 404s."""
    pages = {path.relative_to(ROOT / "pages").as_posix()
             for path in (ROOT / "pages").rglob("*.html")}
    urls = []
    for name, script_id in (("map.html", "corpus-map-data"), ("sequence-map.html", "seq-map-data")):
        payload = map_payload((ROOT / "pages" / name).read_text(), script_id)
        for item in (*payload.get("points", []), *payload.get("pathways", []),
                     *payload.get("proteins", [])):
            urls += [url for url in (item.get("url"), *item.get("pathway_urls", [])) if url]
    assert len(urls) > 1000
    assert [url for url in urls if url not in pages] == []


# --------------------------------------------------------------------------
# The theme toggle changes what is painted, on every page
# --------------------------------------------------------------------------

def _rules(css: str, selector: str) -> dict[str, str]:
    """The custom properties of every rule with exactly this selector, merged."""
    tokens: dict[str, str] = {}
    pattern = rf"(?m)^\s*{re.escape(selector)}\s*\{{([^}}]*)\}}"
    for body in re.findall(pattern, css):
        tokens.update((name, value.strip()) for name, value in
                      re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body))
    return tokens


@pytest.mark.parametrize("stylesheet, scope", [
    ("pages/style.css", ""),
    ("pages/style.css", " .home-page"),
    ("src/pathwaymech/assets/pathway-network.css", " .pathway-network"),
])
def test_both_dark_blocks_declare_the_same_tokens(stylesheet, scope):
    """The OS preference and a chosen dark theme must paint the same palette."""
    css = (ROOT / stylesheet).read_text()
    by_os = _rules(css, ':root:not([data-theme="light"])' + scope)
    chosen = _rules(css, ':root[data-theme="dark"]' + scope)
    assert by_os, "the OS dark theme must apply only when the reader did not choose light"
    assert chosen == by_os
    light = _rules(css, (scope.strip() or ":root"))
    assert set(by_os) <= set(light), "a dark-only token has no light value"
    assert any(by_os[name] != light[name] for name in by_os)


def test_every_token_a_stylesheet_reads_is_declared():
    """The defect: the toggle set --bg/--fg while body read --background/--text."""
    css = "".join((ROOT / path).read_text() for path in
                  ("pages/style.css", "src/pathwaymech/assets/pathway-network.css"))
    used = set(re.findall(r"var\((--[\w-]+)", css))
    declared = set(re.findall(r"(--[\w-]+)\s*:", css))
    assert used - declared == set()
    style = (ROOT / "pages/style.css").read_text()
    body = between(style, "body {", "}")
    for token in re.findall(r"var\((--[\w-]+)", body):
        assert token in _rules(style, ':root[data-theme="dark"]'), token


def test_no_dark_rule_ignores_a_chosen_light_theme():
    for path in ("pages/style.css", "src/pathwaymech/assets/pathway-network.css"):
        css = (ROOT / path).read_text()
        for block in re.findall(r"@media \(prefers-color-scheme: dark\) \{(.*?)\n\}", css, re.S):
            selectors = re.findall(r"(?m)^\s*([^{}\n]+?)\s*\{", block)
            assert selectors, path
            assert all(s.startswith(':root:not([data-theme="light"])') for s in selectors), path


def test_every_page_loads_the_one_theme_script_and_carries_no_other_toggle():
    files = render_site([record()])
    pages = {name: text for name, text in files.items() if name.endswith(".html")}
    pages["../404.html"] = cli._not_found_page()
    assert {"index.html", "browse.html", "map.html", "sequence-map.html", "schema.html",
            "records/MetaCyc_PWY-TEST.html", "../404.html"} <= set(pages)
    for name, page in pages.items():
        head = between(page, "<head>", "</head>")
        root = {"records/": "../", "../": cli.SITE_PATH}.get(name[:name.find("/") + 1], "")
        assert f'<script src="{root}assets/theme.js"></script>' in head, name
        assert "mech-theme" not in page, f"{name} has its own theme handler"
    assert "mech-theme" not in files["assets/pathway-network.js"]
    assert files["assets/theme.js"] == (ROOT / "src/pathwaymech/assets/theme.js").read_text()


@needs_node
@pytest.mark.parametrize("scenario", ["saved_choice_applies_before_the_page_parses",
                                      "first_click_flips_the_os_theme"])
def test_shipped_theme_script(scenario):
    script = ROOT / "src/pathwaymech/assets/theme.js"
    result = subprocess.run(["node", str(HARNESS), str(script), scenario],
                            capture_output=True, text=True, timeout=15)
    assert result.returncode == 0, result.stdout + result.stderr
    assert f"Site feature passed: {scenario}" in result.stdout


# --------------------------------------------------------------------------
# Browse filters by what the records are
# --------------------------------------------------------------------------

def test_the_pathway_type_filter_lists_each_records_type_with_counts():
    records = [record(id=f"MetaCyc:T{n}", label=f"T{n}", pathway_type=kind)
               for n, kind in enumerate(["amino-acid-biosynthesis"] * 2 + ["methanogenesis"])]
    browse = render_site(records)["browse.html"]
    control = between(browse, '<select id="pathway-type">', "</select>")
    options = re.findall(r'<option value="([^"]*)">([^<]*)</option>', control)
    assert options == [("", "All pathway types"),
                       ("amino-acid-biosynthesis", "amino acid biosynthesis (2)"),
                       ("methanogenesis", "methanogenesis (1)")]
    assert "mechanistic edges" not in control
    assert browse.count('data-type="amino-acid-biosynthesis"') == 2
    assert '<label for="pathway-type">Pathway type</label>' in browse


def test_committed_type_counts_cover_every_record():
    browse = (ROOT / "pages/browse.html").read_text()
    control = between(browse, '<select id="pathway-type">', "</select>")
    counts = [int(n.replace(",", "")) for n in re.findall(r"\(([\d,]+)\)</option>", control)]
    assert sum(counts) == browse.count('<li data-search=')


@needs_node
def test_a_shared_link_with_a_retired_value_falls_back_to_the_default(tmp_path):
    page = render_site([record()])["browse.html"]
    scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
    assert len(scripts) == 1
    script = tmp_path / "browse.js"
    script.write_text(scripts[0])
    scenario = "unknown_url_values_select_the_defaults"
    result = subprocess.run(["node", str(HARNESS), str(script), scenario],
                            capture_output=True, text=True, timeout=15)
    assert result.returncode == 0, result.stdout + result.stderr


# --------------------------------------------------------------------------
# Displayed identifiers link where a reader can look them up
# --------------------------------------------------------------------------

def linked_record() -> PathwayRecord:
    return record(
        participants=[
            {"id": "CHEBI:15377", "label": "water", "category": "small_molecule"},
            {"id": "MetaCyc:CPD-1", "label": "compound one", "category": "small_molecule"},
            {"id": "MetaCyc:ENZ-CPLX", "label": "enzyme", "category": "complex"},
            {"id": "BiGG:acmana", "label": "metabolite", "category": "small_molecule"},
            {"id": "MetaCyc:CCO-IN", "label": "cytosol", "category": "cellular_component"},
            {"id": "WikiPathways:WP1/id4b00dac6", "label": "diagram node"},
            {"id": "FOO:123", "label": "unregistered"},
        ],
        reactions=[{"id": "MetaCyc:RXN-1", "label": "reaction one"},
                   {"id": "MetaCyc:PWY-OTHER", "label": "another record", "category": "pathway"}],
        mechanistic_edges=[{
            "id": "edge-1", "subject": "MetaCyc:RXN-1", "predicate": "has_input",
            "object": "CHEBI:15377", "evidence": [{"reference_id": "PMID:1", "quote": "q"}]}],
        references=[{"id": "PMID:1", "title": "Paper"}],
    )


def test_component_identifiers_link_to_resolvers_and_own_records_open_their_page():
    page = _record_page(linked_record(), own_pages={"MetaCyc:PWY-OTHER": "MetaCyc_PWY-OTHER.html",
                                                    "MetaCyc:PWY-TEST": "MetaCyc_PWY-TEST.html"})
    table = between(page, "<caption>Declared biological components", "</table>")
    links = dict(re.findall(r'<a href="([^"]+)"><code>([^<]+)</code></a>', table))
    by_id = {code: href.replace("&amp;", "&") for href, code in links.items()}
    assert by_id == {
        "NCBITaxon:562": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=562",
        "CHEBI:15377": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:15377",
        "MetaCyc:CPD-1": "https://metacyc.org/compound?orgid=META&id=CPD-1",
        "MetaCyc:ENZ-CPLX": "https://metacyc.org/gene?orgid=META&id=ENZ-CPLX",
        "BiGG:acmana": "https://bigg.ucsd.edu/universal/metabolites/acmana",
        "FOO:123": "https://bioregistry.io/FOO:123",
        "MetaCyc:RXN-1": "https://metacyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-1",
        "MetaCyc:PWY-OTHER": "MetaCyc_PWY-OTHER.html",
    }
    # No public page exists for a compartment frame or a GPML GraphId: shown, not linked.
    for unlinked in ("MetaCyc:CCO-IN", "WikiPathways:WP1/id4b00dac6"):
        assert f"<code>{unlinked}</code>" in table and f"><code>{unlinked}</code></a>" not in table
    assert 'href="#"' not in page


def test_edge_endpoints_and_the_record_identity_link_without_linking_to_itself():
    page = _record_page(linked_record(), own_pages={"MetaCyc:PWY-TEST": "MetaCyc_PWY-TEST.html"})
    edges = between(page, "<caption>Mechanistic edges and their cited evidence", "</table>")
    assert hrefs(between(edges, "<td>", "</td>")) == [
        "https://metacyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-1"]
    assert "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:15377" in hrefs(edges)
    identity = between(page, '<p id="pathway-identity">', "</p>")
    assert hrefs(identity) == ["https://metacyc.org/META/NEW-IMAGE?type=PATHWAY&object=PWY-TEST"]


@pytest.mark.parametrize("identifier, category, expected", [
    ("GO:0019305", "", "https://www.ebi.ac.uk/QuickGO/term/GO:0019305"),
    ("EC:1.1.1.169", "", "https://enzyme.expasy.org/EC/1.1.1.169"),
    ("UniProtKB:A0R5M7", "", "https://www.uniprot.org/uniprotkb/A0R5M7/entry"),
    ("SGD:S000000010", "", "https://www.yeastgenome.org/locus/S000000010"),
    ("PathBank:SMP0000807", "", "https://pathbank.org/view/SMP0000807"),
    ("KEGG:ppu:PP_2515", "", "https://www.kegg.jp/entry/ppu:PP_2515"),
    ("EcoCyc:FE+2", "small_molecule", "https://ecocyc.org/compound?orgid=ECOLI&id=FE%2B2"),
    ("gomodel:YeastPathways_GLYCOLYSIS", "", "https://model.geneontology.org/YeastPathways_GLYCOLYSIS"),
    # Ids with no page of their own stay unlinked rather than becoming 404s.
    ("gomodel:1.1.1.190-RXN", "", None),
    ("gomodel:6882d2b800000609/6882d2b800000610", "", None),
    ("PathBank:PW002085", "", None),
    ("RHEA-COMP:10000", "", None),
    ("BiGG:acmana", "", None),
    ("MetaCyc:CPD-1", "", None),
    ("MetaCyc:X&other=true", "small_molecule", None),
    ("not a curie", "", None),
])
def test_term_routes(identifier, category, expected):
    assert _term_url(identifier, category) == expected


def test_citation_routes_keep_their_contract():
    assert _reference_url("MetaCyc:PWY-6543") == (
        "https://metacyc.org/META/NEW-IMAGE?type=PATHWAY&object=PWY-6543")
    assert _reference_url("EcoCyc:CPLX0-226") == "https://ecocyc.org/gene?id=CPLX0-226"
    assert _reference_url("FOO:1") is None


def test_references_open_the_sources_page_and_keep_the_retrieved_file():
    page = _record_page(record(references=[
        {"id": "UniProtKB:P00001", "title": "Protein",
         "url": "https://rest.uniprot.org/uniprotkb/P00001.json"},
        {"id": "PMID:42", "title": "Paper", "url": "https://pubmed.ncbi.nlm.nih.gov/42/"},
        {"id": "MetaCyc:ENZRXN-1", "title": "Undeclared frame",
         "url": "https://websvc.biocyc.org/getxml?META:ENZRXN-1"},
    ]))
    references = between(page, "<h2>References</h2>", "</ul>")
    first = between(references, '<li id="reference-1">', "</li>")
    assert hrefs(first) == ["https://www.uniprot.org/uniprotkb/P00001/entry",
                            "https://rest.uniprot.org/uniprotkb/P00001.json"]
    assert "retrieved source" in first
    second = between(references, '<li id="reference-2">', "</li>")
    assert hrefs(second) == ["https://pubmed.ncbi.nlm.nih.gov/42/"]
    third = between(references, '<li id="reference-3">', "</li>")
    assert hrefs(third) == ["https://websvc.biocyc.org/getxml?META:ENZRXN-1"]


# --------------------------------------------------------------------------
# Citations in record prose can be followed
# --------------------------------------------------------------------------

@pytest.mark.parametrize("text, links", [
    ("with ECO:0000269 PMID:11697907.", [("https://pubmed.ncbi.nlm.nih.gov/11697907/",
                                          "PMID:11697907")]),
    ("see doi:10.1038/nrmicro.2016.94).", [("https://doi.org/10.1038/nrmicro.2016.94",
                                            "doi:10.1038/nrmicro.2016.94")]),
    ("(10.1016/0005-2744(70)90044-4)", [("https://doi.org/10.1016/0005-2744%2870%2990044-4",
                                         "10.1016/0005-2744(70)90044-4")]),
    ("full text PMC94635.html", [("https://pmc.ncbi.nlm.nih.gov/articles/PMC94635/",
                                  "PMC94635")]),
    ("at https://example.org/a?b=1&c=2, then", [("https://example.org/a?b=1&amp;c=2",
                                                 "https://example.org/a?b=1&amp;c=2")]),
    ("javascript:alert(1) and PMID:x", []),
    ("https://user:secret@example.org/x", []),
    # Markup around a citation ends the token instead of joining it (TraitMech #2022).
    ("[10.1038/x](https://doi.org/10.1038/x)", [
        ("https://doi.org/10.1038/x", "10.1038/x"),
        ("https://doi.org/10.1038/x", "https://doi.org/10.1038/x")]),
    ("**10.1099/y**", [("https://doi.org/10.1099/y", "10.1099/y")]),
    ("`10.1146/z`", [("https://doi.org/10.1146/z", "10.1146/z")]),
    ("see **https://example.org/b**; and https://example.org/c:", [
        ("https://example.org/b", "https://example.org/b"),
        ("https://example.org/c", "https://example.org/c")]),
    ("(https://example.org/a)-(https://example.org/b)", [
        ("https://example.org/a", "https://example.org/a"),
        ("https://example.org/b", "https://example.org/b")]),
    ("rdf:about='http://rdf.rhea-db.org/20374'", [
        ("http://rdf.rhea-db.org/20374", "http://rdf.rhea-db.org/20374")]),
    ('https://example.org/"><script>x</script>', [("https://example.org/", "https://example.org/")]),
])
def test_autolink_links_only_citation_tokens_and_keeps_the_text(text, links):
    rendered = autolink_html(text)
    assert re.findall(r'<a href="([^"]*)">([^<]*)</a>', rendered) == links
    assert "<script>" not in rendered
    assert re.sub(r"<[^>]+>", "", rendered).replace("&amp;", "&").replace(
        "&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#x27;", "'") == text


def test_scientific_formatting_survives_beside_a_linked_citation():
    assert rich_text_html("H<sup>+</sup> efflux (PMID:7)") == (
        'H<sup>+</sup> efflux (<a href="https://pubmed.ncbi.nlm.nih.gov/7/">PMID:7</a>)')


def test_citations_link_in_every_part_of_a_record_page():
    page = _record_page(record(
        description="Described in PMID:101.",
        participants=[{"id": "UniProtKB:P00001", "label": "protein", "category": "protein"}],
        reactions=[{"id": "RHEA:1", "label": "reaction"}],
        mechanistic_edges=[{
            "id": "edge-1", "subject": "RHEA:1", "predicate": "has_participant",
            "object": "UniProtKB:P00001", "description": "Edge note PMID:102.",
            "endpoint_qualifiers": [{"endpoint": "object", "kind": "construct",
                                     "description": "Construct from PMID:103.",
                                     "evidence": [{"reference_id": "PMID:1", "quote": "q"}]}],
            "evidence": [{"reference_id": "PMID:1",
                          "source_assertion": "Asserted with ECO:0000269 PMID:104.",
                          "source_locator": "PMID:999 locator stays code"}]}],
        references=[{"id": "PMID:1", "title": "Title citing doi:10.1000/xyz",
                     "source_version": "DOI 10.1000/abc; retrieved"}],
        curation_history=[{"timestamp": "2026-10-01T00:00:00Z", "changes": "Fixed per PMID:105"}],
    ))
    expected = {
        between(page, "<main", "<dl>"): "https://pubmed.ncbi.nlm.nih.gov/101/",
        between(page, "<p>Edge note", "</p>"): "https://pubmed.ncbi.nlm.nih.gov/102/",
        between(page, '<div class="endpoint-qualifier"', "</p>"):
            "https://pubmed.ncbi.nlm.nih.gov/103/",
        between(page, "<strong>Source assertion:</strong>", "</p>"):
            "https://pubmed.ncbi.nlm.nih.gov/104/",
        between(page, '<li id="reference-1">', "</li>"): "https://doi.org/10.1000/xyz",
        between(page, 'id="history-title"', "</section>"): "https://pubmed.ncbi.nlm.nih.gov/105/",
    }
    for section, url in expected.items():
        assert url in hrefs(section), section[:60]
    assert "https://doi.org/10.1000/abc" in hrefs(between(page, '<li id="reference-1">', "</li>"))
    locator = between(page, "<summary>Source location</summary>", "</details>")
    assert hrefs(locator) == []


# --------------------------------------------------------------------------
# Every page states its licences and a dated corpus version
# --------------------------------------------------------------------------

def test_every_page_type_footer_states_the_licences_and_the_corpus_date():
    files = render_site([record(curation_history=[{"timestamp": "2026-10-01T09:30:00Z"}])])
    for name, page in files.items():
        if not name.endswith(".html"):
            continue
        footer = between(page, '<footer class="site-footer">', "</footer>")
        licences = [f"{cli.GITHUB_BLOB}/{licence}"
                    for licence in ("LICENSE-DATA", "LICENSE-CODE", "LICENSE")]
        assert hrefs(footer)[:3] == licences, name
        assert "Project data:" in footer and "CC BY 4.0" in footer and "BSD-3-Clause" in footer
        assert "Third-party source material keeps its own terms" in footer
        assert "Corpus as of 2026-10-01 09:30 UTC · 1 pathway record" in footer, name


def test_footer_licences_are_what_the_licence_files_say():
    scope = (ROOT / "LICENSE").read_text()
    assert "Creative Commons Attribution 4.0" in scope and "CC-BY-4.0" in scope
    assert "BSD-3-Clause" in scope and "retain their own licenses" in scope
    assert (ROOT / "LICENSE-DATA").read_text().startswith("Attribution 4.0 International")
    assert (ROOT / "LICENSE-CODE").read_text().startswith("BSD 3-Clause License")


def test_the_landing_states_the_code_licence_beside_the_data_licence():
    page = render_site([record()])["index.html"]
    downloads = between(page, 'id="downloads-title"', "</section>")
    assert f"{cli.GITHUB_BLOB}/LICENSE-CODE" in hrefs(downloads)
    assert f"{cli.GITHUB_BLOB}/LICENSE-DATA" in hrefs(downloads)


def test_the_corpus_date_comes_from_recorded_curation_never_the_clock():
    records = [record(curation_history=[{"timestamp": "2026-10-12T19:55:52.877350+00:00"},
                                        {"timestamp": "2026-10-05T06:05:08Z"}])]
    sessions = [[{"session": {"timestamp": "2026-10-25T16:45:00Z"}},
                 {"session": {"timestamp": "not a time"}}]]
    assert corpus_as_of(records, sessions) == "2026-10-25 16:45 UTC"
    assert corpus_as_of(records, []) == "2026-10-12 19:55 UTC"
    assert corpus_as_of([record()], []) == ""
    assert corpus_as_of([record(curation_history=[{"timestamp": "2026-10-12T21:00:00-05:00"}])],
                        []) == "2026-10-13 02:00 UTC"


# --------------------------------------------------------------------------
# A readable schema reference, generated from the schema
# --------------------------------------------------------------------------

def test_schema_page_documents_every_class_slot_and_enum():
    schema = yaml.safe_load((ROOT / "src/pathwaymech/schema/pathwaymech.yaml").read_text())
    page = render_site([record()])["schema.html"]
    for name, element in schema["classes"].items():
        section = between(page, f'<section class="schema-class" id="class-{name}"', "</section>")
        for slot in (element.get("attributes") or {}):
            assert f'<tr id="class-{name}-{slot}">' in section, (name, slot)
    for name, enum in schema["enums"].items():
        section = between(page, f'<section class="schema-enum" id="enum-{name}"', "</section>")
        for value in enum["permissible_values"]:
            assert f"<dt><code>{value}</code>" in section, (name, value)
    targets = set(re.findall(r'id="([^"]+)"', page))
    assert {link[1:] for link in hrefs(page) if link.startswith("#")} <= targets
    taxa = between(page, '<tr id="class-PathwayRecord-taxa">', "</tr>")
    assert hrefs(taxa) == ["#class-NamedNode"]
    assert "<td>Required, multivalued</td>" in taxa
    history = between(page, '<tr id="class-PathwayRecord-curation_history">', "</tr>")
    assert hrefs(history) == ["#class-CurationEvent"]
    assert "<td>Optional, multivalued</td>" in history


def test_schema_prose_keeps_format_examples_as_text(tmp_path):
    """Schema descriptions give identifier formats, not citations to follow."""
    schema = tmp_path / "fixture.yaml"
    schema.write_text("""\
id: https://example.org/fixture
name: fixture
prefixes:
  linkml: https://w3id.org/linkml/
default_range: string
imports:
  - linkml:types
classes:
  Thing:
    description: A thing, cited as DOI:10.1000/xyz.
    attributes:
      reference:
        description: A citation such as PMID:12345678 or https://example.org/x.
enums:
  Kind:
    description: As in PMC1234567.
    permissible_values:
      one:
        description: From doi:10.1000/abc.
""")
    page = cli._schema_page(schema_path=schema)
    main = between(page, "<main", "</main>")
    for example in ("DOI:10.1000/xyz", "PMID:12345678", "https://example.org/x",
                    "PMC1234567", "doi:10.1000/abc"):
        assert example in main
    citations = ("https://pubmed.ncbi.nlm.nih.gov/", "https://doi.org/",
                 "https://pmc.ncbi.nlm.nih.gov/", "https://example.org/")
    assert [link for link in hrefs(main) if link.startswith(citations)] == []


def test_the_schema_page_renders_the_same_bytes_twice():
    cli._schema_reference.cache_clear()
    first = cli._schema_page()
    cli._schema_reference.cache_clear()
    assert cli._schema_page() == first


def test_every_page_type_links_the_schema_from_its_navigation():
    files = render_site([record()])
    for name in ("index.html", "browse.html", "map.html", "sequence-map.html",
                 "records/MetaCyc_PWY-TEST.html", "schema.html"):
        nav = between(files[name], '<nav aria-label="Main navigation">', "</nav>")
        root = "../" if name.startswith("records/") else ""
        assert f"{root}schema.html" in hrefs(nav), name


# --------------------------------------------------------------------------
# A themed not-found page, and a way to report a record
# --------------------------------------------------------------------------

def test_the_not_found_page_works_at_any_address():
    """GitHub serves it at the missing address, at any depth: nothing may be relative."""
    page = cli._not_found_page()
    assert '<meta name="robots" content="noindex">' in page
    head = between(page, "<head>", "</head>")
    assert '<link rel="stylesheet" href="/PathwayMech/pages/style.css">' in head
    assert '<script src="/PathwayMech/pages/assets/theme.js"></script>' in head
    references = hrefs(page) + re.findall(r'(?:src|action)="([^"]+)"', page)
    assert [ref for ref in references
            if not ref.startswith(("/PathwayMech/", "https://", "#"))] == []
    assert re.search(r'action="([^"]+)"', page).group(1) == "/PathwayMech/pages/browse.html"
    main = between(page, "<main", "</main>")
    assert {"/PathwayMech/pages/browse.html", "/PathwayMech/pages/index.html"} <= set(hrefs(main))
    assert page.index('<a class="skip-link" href="#main-content">') < page.index("<main")
    footer = between(page, '<footer class="site-footer">', "</footer>")
    assert f"{cli.GITHUB_BLOB}/LICENSE-CODE" in hrefs(footer)
    # No corpus date or record count, so a curation change never rewrites it.
    assert "Corpus as of" not in page
    assert not re.search(r"[0-9] pathway record", page)


def _two_record_site(tmp_path: Path) -> Path:
    for path in sorted((ROOT / "data" / "pathways").glob("*.yaml"))[:2]:
        target = tmp_path / "data" / "pathways" / path.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(path, target)
    (tmp_path / "pages").mkdir()
    (tmp_path / "pages" / "style.css").write_text("body {}\n")
    (tmp_path / "pages" / ".nojekyll").write_text("\n")
    return tmp_path


def test_the_render_writes_the_root_not_found_page_and_the_check_guards_it(tmp_path, capsys):
    site = _two_record_site(tmp_path)
    assert cli.render_pages_main([], root=site) == 0
    assert (site / "404.html").read_text() == cli._not_found_page()
    assert not (site / "pages" / "404.html").exists()
    assert cli.render_pages_main(["--check"], root=site) == 0
    (site / "404.html").write_text("stale")
    assert cli.render_pages_main(["--check"], root=site) == 1
    assert "404.html: not what the renderer writes" in capsys.readouterr().err
    (site / "404.html").unlink()
    assert cli.render_pages_main(["--check"], root=site) == 1


def test_the_committed_not_found_page_is_current():
    assert (ROOT / "404.html").read_text() == cli._not_found_page()


def test_the_pages_workflow_publishes_the_not_found_page_at_the_artifact_root():
    workflow = yaml.safe_load((ROOT / ".github/workflows/pages.yaml").read_text())
    steps = workflow["jobs"]["publish"]["steps"]
    stage = next(step["run"] for step in steps if step.get("name") == "Stage the site")
    assert 'cp index.html 404.html "$site/"' in [line.strip() for line in stage.splitlines()]
    # The stale-site refusal, which now also covers 404.html, runs before staging.
    runs = [step.get("run", "") for step in steps]
    assert any("pathwaymech-check-pages" in run for run in runs[:runs.index(stage)])


def test_every_record_page_links_a_prefilled_issue_for_that_record():
    page = _record_page(record(), "data/pathways/test.yaml")
    actions = between(page, '<p class="record-actions">', "</p>")
    issue = next(link for link in hrefs(actions) if "/issues/new?" in link)
    query = parse_qs(urlsplit(issue).query)
    assert urlsplit(issue)._replace(query="").geturl() == f"{cli.GITHUB_REPO}/issues/new"
    assert query["title"] == ["Problem with MetaCyc:PWY-TEST"]
    assert query["body"] == [f"{SITE_URL}records/MetaCyc_PWY-TEST.html"]
    assert f"{cli.GITHUB_BLOB}/data/pathways/test.yaml" in hrefs(actions)
    assert f"{cli.GITHUB_REPO}/edit/main/data/pathways/test.yaml" in hrefs(actions)


# --------------------------------------------------------------------------
# Sibling links
# --------------------------------------------------------------------------

VERIFIED_SIBLING_ROUTES = (
    "https://culturebotai.github.io/mechs/",
    "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=",
    "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
    "https://culturebotai.github.io/proteintraitsmech/browse.html?q=",
    "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CellStructureMech/pages/browse.html?q=",
    "https://culturebotai.github.io/HabitatMech/pages/browse.html?q=",
    "https://culturebotai.github.io/NaturalProductMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:",
    "https://culturebotai.github.io/DUFMech/index.html?q=",
    "https://culturebotai.github.io/CMMMech/pages/browse.html?q=",
    "https://culturebotai.github.io/AIMech/pages/browse.html?q=",
)


def test_every_link_into_the_suite_uses_a_verified_route():
    links = []
    for path in sorted((ROOT / "pages").rglob("*.html")):
        links += [link for link in hrefs(path.read_text())
                  if link.startswith("https://culturebotai.github.io/")
                  and not link.startswith(SITE_URL)]
    assert links, "every page links the Mech directory"
    assert [link for link in links if not link.startswith(VERIFIED_SIBLING_ROUTES)] == []
