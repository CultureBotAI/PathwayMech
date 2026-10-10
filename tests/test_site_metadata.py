from __future__ import annotations

import csv
import io
import json
from dataclasses import replace

from pathwaymech.cli import _record_page, _reference_url, render_site
from pathwaymech.kgx import write_kgx
from pathwaymech.schema import PathwayRecord
from pathwaymech.site_display import label_html, load_site_history, plain_label


def record(**changes):
    base = PathwayRecord(
        id="MetaCyc:TEST", label="Z pathway", description="Recorded description",
        pathway_type="cofactor-biosynthesis", taxa=[{"id": "NCBITaxon:562", "label": "E. coli"}],
        participants=[], reactions=[], mechanistic_edges=[], references=[],
    )
    return replace(base, **changes)


def test_browse_sorts_visible_labels_then_ids_and_searches_only_names_and_ids():
    files = render_site([record(), record(id="MetaCyc:A", label="<i>A</i> pathway"),
                         record(id="MetaCyc:B", label="A pathway")])
    browse = files["browse.html"]
    assert browse.index('records/MetaCyc_A.html') < browse.index('records/MetaCyc_B.html')
    assert browse.index('records/MetaCyc_B.html') < browse.index('records/MetaCyc_TEST.html')
    assert 'data-search="A pathway MetaCyc:A"' in browse
    assert 'data-search="A pathway MetaCyc:A 0 mechanistic edges"' not in browse


def test_scientific_label_formatting_has_no_attributes_or_executable_html():
    raw = 'H<SUP>+</SUP> <i>de novo</i> <img src=x onerror=alert(1)>'
    assert label_html(raw) == ('H<sup>+</sup> <i>de novo</i> '
                               '&lt;img src=x onerror=alert(1)&gt;')
    assert plain_label('H<SUP>+</SUP>') == 'H+'
    assert label_html('<sup onclick="x">bad</sup>').startswith('&lt;sup onclick=')
    assert '<script>' not in label_html('&lt;script&gt;alert(1)&lt;/script&gt;')


def test_metadata_and_real_curation_history_are_shown_without_inventing_events():
    page = _record_page(record(curation_history=[{
        "timestamp": "2026-10-01T12:00:00Z", "action": "Review", "changes": "Checked sources",
    }]), sessions=[{
        "source_path": "history/records/test/session.yaml",
        "session": {"timestamp": "2026-10-02T12:00:00Z",
                    "actors": [{"type": "human", "name": "A"}]},
        "events": [{"type": "EDIT", "summary": "Correct label", "details": "Source <text>"}],
    }])
    for expected in ('cofactor biosynthesis', 'E. coli', 'wwwtax.cgi?id=562',
                     '2026-10-01T12:00:00Z', 'Checked sources', 'Correct label',
                     'Source &lt;text&gt;', 'history/records/test/session.yaml'):
        assert expected in page
    empty = _record_page(record(taxa=[], pathway_type=""))
    assert empty.count('Not recorded') == 2
    assert 'No curation history recorded for this pathway' in empty


def test_source_cluster_and_go_cam_source_fragment_have_honest_status():
    cluster = record(gene_clusters=[{"id": "MIBiG:BGC0002072", "label": "Cluster"}])
    assert 'Source cluster summary' in render_site([cluster])["browse.html"]
    assert 'but no curated mechanistic edges' in _record_page(cluster)
    fragment = '"subject":"gomodel:a","property":"RO:0002413","object":"gomodel:b"'
    model = record(reactions=[{"id": "gomodel:a", "label": "Activity A"},
                              {"id": "gomodel:b", "label": "Activity B"}],
        mechanistic_edges=[{
        "id": "edge-1", "subject": "gomodel:a", "predicate": "provides_input_for",
        "object": "gomodel:b",
        "evidence": [{"reference_id": "gomodel:one", "quote": fragment}],
    }], references=[{"id": "gomodel:one", "title": "Source model"}])
    page = _record_page(model)
    assert 'GO-CAM source assertion' in page
    assert 'not a quotation from an experimental publication' in page
    assert 'subject: <code>gomodel:a</code>' in page
    assert '&quot;subject&quot;:&quot;gomodel:a&quot;' in page
    assert '<summary>Exact source fragment</summary>' in page


def test_reference_routes_validate_identifier_shapes_and_escape_parameters():
    routes = {
        "WikiPathways:WP296": "https://www.wikipathways.org/instance/WP296",
        "gomodel:YeastPathways_GLYCOLYSIS":
            "https://model.geneontology.org/YeastPathways_GLYCOLYSIS",
        "MIBiG:BGC0002072": "https://mibig.secondarymetabolites.org/go/BGC0002072",
        "Reactome:R-HSA-70263": "https://reactome.org/content/detail/R-HSA-70263",
        "MetaCyc:PWY-6543": "https://metacyc.org/META/NEW-IMAGE?type=PATHWAY&object=PWY-6543",
    }
    for identifier, expected in routes.items():
        assert _reference_url(identifier) == expected
    for identifier in ('Other:1', 'WikiPathways:WP1/evil', 'MetaCyc:X&other=true'):
        assert _reference_url(identifier) is None


def test_published_downloads_equal_complete_export_and_include_isolated_records(tmp_path):
    records = [record(), record(id="MetaCyc:OTHER", label="Second")]
    files = render_site(records)
    paths = write_kgx(records, tmp_path)
    for path in paths:
        assert files[f'downloads/{path.name}'] == path.read_text()
    nodes = list(csv.DictReader(io.StringIO(files['downloads/nodes.tsv']), delimiter='\t'))
    assert {row['id'] for row in nodes} == {'MetaCyc:TEST', 'MetaCyc:OTHER', 'NCBITaxon:562'}
    manifest = json.loads(files['downloads/manifest.json'])
    assert manifest['pathway_records'] == 2
    assert manifest['files']['nodes.tsv']['rows'] == 3
    assert manifest['files']['edges.tsv']['rows'] == 0
    assert manifest['data_license'] == 'CC-BY-4.0'


def test_session_history_matches_exact_record_path(tmp_path):
    folder = tmp_path / 'history/records/example'
    folder.mkdir(parents=True)
    (folder / 'session.yaml').write_text('target: {path: data/pathways/example.yaml}\n')
    history = load_site_history(tmp_path)
    assert list(history) == ['data/pathways/example.yaml']
    assert history['data/pathways/example.yaml'][0]['source_path'].endswith('/session.yaml')
