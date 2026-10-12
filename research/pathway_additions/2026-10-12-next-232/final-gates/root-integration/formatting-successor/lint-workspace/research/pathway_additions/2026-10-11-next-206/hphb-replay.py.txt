"""Replay complete original HP/HB sources and actual target exports (author checks)."""

from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.util
import io
import json
import re
import sqlite3
from collections import Counter
from functools import cache
from pathlib import Path

import yaml
from lxml import etree, html

from pathwaymech.kgx import render_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path(__file__).resolve().parents[3]
DOSSIER = Path(__file__).parent
RAW = Path('/private/tmp/pathwaymech-next-206-evidence/hphb')
CACHE = Path('/private/tmp/pathwaymech-curation-authorities')
TARGET = ROOT / 'data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml'
RH = 'http://rdf.rhea-db.org/'
RDF = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'


@cache
def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def read(name):
    return load(DOSSIER / ('hphb-' + name + '.json'))


def xml(frame, tag):
    return etree.parse(str(RAW / (frame + '.xml'))).find(tag)


def norm(text):
    return ' '.join(text.split())


def main():
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert strict_errors([TARGET], ROOT) == []
    target_hash = digest(TARGET)
    projection, manifest = read('source-projection'), read('source-manifest')
    ids, authorities = read('identifiers'), read('authority-inputs')
    for receipt in [projection, manifest, ids, authorities, read('dedup')]:
        assert receipt['target_sha256'] == target_hash
    for body in manifest['source_bodies']:
        assert digest(body['raw_path']) == body['sha256'], body['raw_path']
    for ref in doc['references']:
        assert digest(manifest['reference_body_map'][ref['id']]) == ref['source_sha256']
    # Review issues 373/374: validate article metadata and claim-specific passages,
    # not merely a selector that exists or a generic enzyme word in a paragraph.
    primary_titles_checked = 0
    for ref in doc['references']:
        if not ref['id'].startswith('PMID:') or ref['id'] == 'PMID:12581213':
            continue
        path = Path(manifest['reference_body_map'][ref['id']])
        tree = etree.parse(str(path)) if path.suffix == '.xml' else html.parse(str(path))
        selector = '/article/front/article-meta/title-group/article-title'
        title_nodes = tree.xpath(selector if path.suffix == '.xml' else '//h1')
        assert len(title_nodes) == 1, ref['id']
        # Preserve the existing HTML inline-node spacing convention; JATS title
        # extraction joins its inline content without inserted spaces.
        joiner = '' if path.suffix == '.xml' else ' '
        assert ref['title'] == norm(joiner.join(title_nodes[0].itertext())), ref['id']
        primary_titles_checked += 1
    assert primary_titles_checked == 12
    edges = {e['id']: e for e in doc['mechanistic_edges']}
    module = html.parse(manifest['reference_body_map']['PMID:24532060'])
    source_paragraphs = module.xpath('//*[@id="sec3-1"]/p')
    expected_locators = [module.getpath(source_paragraphs[i]) for i in (1, 3)]
    for edge_id, locus in [('hphb-edge-122', 'Msed_0656'),
                           ('hphb-edge-124', 'Msed_0399'),
                           ('hphb-edge-125', 'Msed_0399')]:
        assertion = edges[edge_id]['evidence'][2]
        assert assertion['reference_id'] == 'PMID:24532060'
        assert assertion['source_locator'].split('; ') == expected_locators
        selected = [module.xpath(locator) for locator in expected_locators]
        assert all(len(nodes_at_locator) == 1 for nodes_at_locator in selected)
        activity_text, module_text = [norm(''.join(nodes[0].itertext())) for nodes in selected]
        assert locus in activity_text
        assert 'hydration' in activity_text and 'dehydrogenation' in activity_text
        assert 'reconstitution' in module_text and 'confirm the in vitro conversion' in module_text
    assert projection['graph_to_source'] == [
        dict(edge_id=e['id'], subject=e['subject'], predicate=e['predicate'],
             object=e['object'], evidence=e['evidence']) for e in edges.values()
    ]
    # Full original RDF is parsed independently, including repeated descriptions.
    wanted, nodes = set(projection['original_rhea_nodes']), {}
    with gzip.open(CACHE / 'rhea.rdf.gz', 'rb') as stream:
        for _, element in etree.iterparse(
                stream, events=('end',), tag='{' + RDF + '}Description'):
            uri = element.get('{' + RDF + '}about')
            if uri in wanted:
                props = nodes.setdefault(uri, {})
                for child in element:
                    key = child.tag.split('}')[-1]
                    value = child.get('{' + RDF + '}resource') or child.text
                    if value not in props.setdefault(key, []):
                        props[key].append(value)
            element.clear()
            while element.getprevious() is not None:
                del element.getparent()[0]
    assert nodes == projection['original_rhea_nodes']
    con = sqlite3.connect(f'file:{CACHE / "chebi.db"}?mode=ro', uri=True)

    def chemical(curie):
        return dict(con.execute(
            'select predicate,value from statements where subject=? and value is not null',
            (curie,),
        ))

    sides = projection['rhea_sides']
    chemical_edges = [e for e in edges.values() if e['predicate'] in {'consumes', 'produces'}]
    assert len(chemical_edges) == len(sides) == 78
    balances, reaction_counts = {}, {}
    for row, edge in zip(sides, chemical_edges, strict=True):
        directed = RH + row['directed']
        assert row['side_uri'] in nodes[directed][row['side']]
        assert row['participant_uri'] in nodes[row['side_uri']][row['coefficient_predicate']]
        assert row['compound_uri'] in nodes[row['participant_uri']]['compound']
        assert row['coefficient'] == int(row['coefficient_predicate'].removeprefix('contains'))
        compound = nodes[row['compound_uri']]
        assert compound == row['compound']
        curie = row['curie'][0]
        assert compound['accession'] == [curie]
        authority = chemical(curie)
        formula, charge = compound['formula'][0], compound['charge'][0]
        assert formula == authority['chemrof:generalized_empirical_formula']
        assert charge == authority['chemrof:charge']
        assert re.sub(r'([A-Z][a-z]?)(\d*)', '', formula) == ''
        total = balances.setdefault(row['directed'], {}).setdefault(row['side'], Counter())
        for atom, count in re.findall(r'([A-Z][a-z]?)(\d*)', formula):
            total[atom] += int(count or '1') * row['coefficient']
        total['charge'] += int(charge) * row['coefficient']
        signed = row['coefficient'] * (1 if row['side'] == 'products' else -1)
        reaction_counts.setdefault(row['directed'], Counter())[curie] += signed
        endpoint = 'subject' if row['side'] == 'substrates' else 'object'
        assert edge[endpoint] == curie
        assert edge['object' if endpoint == 'subject' else 'subject'] == 'RHEA:' + row['directed']
        ev = edge['evidence'][0]
        assert f"coefficient {row['coefficient']}" in ev['source_assertion']
        for fragment in [row['side_uri'], row['coefficient_predicate'],
                         row['participant_uri'], row['compound_uri']]:
            assert fragment in ev['source_locator']
    for two_sides in balances.values():
        assert two_sides['substrates'] == two_sides['products']
    assert len(balances) == 17
    cycle_sum = Counter()
    for counts in reaction_counts.values():
        cycle_sum.update(counts)
    cycle_sum = {k: v for k, v in cycle_sum.items() if v}
    # Original native half-reactions sum exactly to the independently issued net.
    native_sum = Counter()
    for frame in ['BIOTIN-CARBOXYL-RXN', 'RXN0-5055']:
        original = xml(frame, 'Reaction')
        for side, sign in [('left', -1), ('right', 1)]:
            for participant in original.findall(side):
                entity = next(iter(participant))
                native_sum[entity.get('frameid')] += sign * int(
                    participant.findtext('coefficient') or '1')
    native_sum = {k: v for k, v in native_sum.items() if v}
    assert native_sum == projection['chemistry']['native_sum']
    mapping = {b['native']: b['chebi'] for b in projection['chemistry']['chemical_bridges']}
    assert {mapping[k]: v for k, v in native_sum.items()} == dict(reaction_counts['11309'])
    assert not any('BCCP' in p['id'] for p in doc['participants'])
    # All native members are represented; no net plus half-reaction double counting.
    native_path = etree.parse(projection['native_pathway']['path']).find('Pathway')
    members = native_path.xpath('./reaction-list/Reaction/@frameid')
    assert len(members) == 18
    coverage = projection['coverage']
    assert set(members) == {x['native_reaction'] for x in coverage}
    assert len({x['represented_reaction'] for x in coverage}) == 17
    assert {r['id'] for r in doc['reactions']} == {x['represented_reaction'] for x in coverage}
    for row in projection['native_reaction_projection']:
        original = xml(row['id'], 'Reaction')
        assert original.findtext('reaction-direction') == row['direction']
        assert original.xpath('./dblink[dblink-db="RHEA"]/dblink-oid/text()') == row['rhea']
        for side in ['left', 'right']:
            parsed = []
            for part in original.findall(side):
                parsed.append([
                    next(iter(part)).get('frameid'), part.findtext('coefficient') or '1'])
            assert parsed == row[side], (row['id'], side)
    layouts = {x['reaction']: x['direction'] for x in projection['native_pathway']['layout']}
    for row in projection['native_reaction_projection']:
        if row['id'] in {'BIOTIN-CARBOXYL-RXN', 'RXN0-5055'}:
            continue
        original_counts = Counter()
        for side, sign in [('left', -1), ('right', 1)]:
            for chemical_frame, coefficient in row[side]:
                original_counts[mapping[chemical_frame]] += (
                    int(coefficient) * sign * (1 if layouts[row['id']] == 'L2R' else -1))
        represented = next(x['represented_reaction'].split(':')[1] for x in coverage
                           if x['native_reaction'] == row['id'])
        assert dict(original_counts) == dict(reaction_counts[represented])
    for rx in doc['reactions']:
        number = rx['id'].split(':')[1]
        assert rx['label'] == nodes[RH + number]['label'][0]
        family = next(v for v in projection['rhea_directions'].values() if number in v.values())
        assert family[rx['direction']] == number
        assert RH + number in nodes[RH + family['master']]['directionalReaction']
    hydration = next(r for r in doc['reactions'] if r['id'] == 'RHEA:10750')
    assert 'category' not in hydration
    assert not any(e['object'] == hydration['id'] and e['predicate'] in {'enables', 'catalyzes'}
                   for e in edges.values())
    # Chemical identity checks distinguish one broader native scaffold and a stale xref.
    for b in projection['chemistry']['chemical_bridges']:
        original = xml(b['native'], 'Compound')
        assert original.findtext('inchi') == b['native_inchi']
        assert chemical(b['chebi'])['chemrof:inchi_string'] == b['authority_inchi']
        if b['native'] == 'CROTONYL-COA':
            assert b['native_inchi'].replace('20?', '20+') == b['authority_inchi']
            assert 'Not skos:exactMatch' in b['relationship']
        else:
            assert b['native_inchi'] == b['authority_inchi']
    assert mapping['PPI'] == 'CHEBI:33019'
    assert xml('PPI', 'Compound').xpath(
        './dblink[dblink-db="CHEBI"]/dblink-oid/text()') == ['29888']
    # Original CDS translations resolve the two reversed native cross-references.
    entries = load(RAW / 'uniprot-gene-batch.json')['results']
    entries += load(RAW / 'uniprot-Msed_0394.json')['results']
    proteins = {x['primaryAccession']: x for x in entries}
    for row in projection['carboxylase_sequence_crosscheck']:
        original = (RAW / (row['source'] + '.embl')).read_text()
        chunks = re.split(r'^FT   CDS\s+', original, flags=re.M)[1:]
        chunk = next(c for c in chunks if '/protein_id="' + row['protein_id'] + '"' in c)
        sequence_text = re.search(r'/translation="([^"]+)"', chunk, re.S).group(1)
        sequence = re.sub(r'^FT\s+', '', sequence_text, flags=re.M)
        sequence = re.sub(r'\s+', '', sequence)
        assert sequence == row['sequence']
        assert [a for a, p in proteins.items() if p['sequence']['value'] == sequence] == (
            row['exact_uniprot_matches'])
    for monomer, wrong in [('MONOMER-13716', 'A4YD22'), ('MONOMER-13717', 'A4YD23')]:
        assert xml(monomer, 'Protein').xpath(
            './dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [wrong]
    correct = {e['object'] for e in edges.values() if e['subject'] == 'MetaCyc:CPLX-7575'
               and e['predicate'] == 'has_part'}
    assert correct == {'UniProtKB:A4YD22', 'UniProtKB:A4YD23', 'UniProtKB:A4YGI1'}
    # Every selected sequence is strain 399549; foreign and outdated roles are scoped.
    selected = [p['id'].split(':')[1] for p in doc['participants']
                if p['id'].startswith('UniProtKB:')]
    assert len(selected) == 21
    assert all(proteins[a]['organism']['taxonId'] == 399549 for a in selected)
    assert xml('MONOMER-13730', 'Protein').xpath(
        './dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == ['Q975C8']
    assert not any(p['id'] == 'UniProtKB:Q975C8' for p in doc['participants'])
    # All literal source locators resolve on original bodies; primary guard anchors
    # verify source paragraph selection rather than inferring truth from a citation.
    for guard in projection['primary_locator_guards']:
        path = Path(guard['path'])
        if guard['representation'] == 'publisher web-reader JSON':
            text = ''.join(load(path)['parts'])
        else:
            tree = etree.parse(str(path)) if path.suffix == '.xml' else html.parse(str(path))
            hits = tree.xpath(guard['locator'])
            assert len(hits) == 1
            text = norm(''.join(hits[0].itertext()))
        assert guard['literal_anchor'] in text
    for edge in edges.values():
        for assertion in edge['evidence']:
            reference = assertion['reference_id']
            if reference.startswith('MetaCyc:'):
                tree = etree.parse(manifest['reference_body_map'][reference])
                for xpath in assertion['source_locator'].split('; '):
                    if xpath.startswith('/'):
                        assert tree.xpath(xpath), (reference, xpath)
            if reference.startswith('UniProtKB:'):
                body = load(manifest['reference_body_map'][reference])
                locator = assertion['source_locator'].split(';')[0]
                value = body
                for fragment in locator.lstrip('/').split('/'):
                    value = value[int(fragment)] if isinstance(value, list) else value[fragment]
                assert value is not None
        if edge['predicate'] == 'provides_input_for':
            assert {e['reference_id'] for e in edge['evidence']} == {
                edge['subject'], edge['object']}
    # Meaningful exact primary guards for the principal-enzyme update and assemblies.
    later = html.parse(str(RAW / 'PMC7845616.html'))
    discussion = norm(' '.join(later.xpath('//*[@id="s3"]//text()')))
    assert '99%' in discussion and '86%' in discussion and 'Msed_2001' in discussion
    assert '8.2%' in discussion and '5.5%' in discussion
    mutant = html.parse(str(RAW / 'PMC3416614.html'))
    assembly = norm(''.join(mutant.xpath('//*[@id="sec16"]//text()')))
    assert '173.7 kDa' in assembly and 'α2β2' in assembly
    assert not any(n['id'] in {'MetaCyc:CPLX-8531', 'MetaCyc:CPLX-8532'}
                   for n in doc['participants'])
    recent = html.parse(str(RAW / 'PMC5433351.html'))
    assert 'homo-octamer' in norm(''.join(recent.xpath('//*[@id="S13"]//text()')))
    assert 'homopentamer' in norm(''.join(recent.xpath('//*[@id="S15"]//text()')))
    assert 'Msed_1426' in norm(''.join(recent.xpath('//*[@id="S16"]//text()')))
    assert any(e['predicate'] == 'enables' and e['subject'] == 'UniProtKB:A4YGN2'
               and any(a['reference_id'] == 'PMID:27771364' for a in e['evidence'])
               for e in edges.values())
    protein_projection = read('protein-projection')
    assert protein_projection['target_sha256'] == target_hash
    assert len(protein_projection['complete_selected_proteins']) == 21
    for row in protein_projection['complete_selected_proteins']:
        acc = row['id'].split(':')[1]
        assert hashlib.sha256(proteins[acc]['sequence']['value'].encode()).hexdigest() == (
            row['sequence_sha256'])
    for row in protein_projection['native_assemblies']:
        original = xml(row['native'], 'Protein')
        assert row['components'] == [
            {'id': c.find('Protein').get('frameid'), 'coefficient': c.findtext('coefficient')}
            for c in original.findall('component')]
    for guard in protein_projection['late_primary_locator_guards']:
        tree = html.parse(guard['raw_path'])
        nodes_at_locator = tree.xpath(guard['source_locator'])
        assert len(nodes_at_locator) == 1
        assert guard['literal_anchor'] in ''.join(nodes_at_locator[0].itertext())
    # Independently parse original native HTML authority names using canonical code.
    spec = importlib.util.spec_from_file_location(
        'sourcebuilder', ROOT / 'scripts/build_source_identifier_snapshot.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for source in authorities['native_html']:
        assert list(module.metacyc_terms(Path(source['path']).read_text())) == [
            (source['id'], source['canonical_label'], source['synonyms'])]
    for n in ids['identifiers']:
        if n['id'].startswith('CHEBI:'):
            assert n['label'] == chemical(n['id'])['rdfs:label']
    # Export the actual record, preserving all evidence arrays and descriptions.
    kgx = render_kgx([record])
    out_edges = list(csv.DictReader(io.StringIO(kgx['edges.tsv']), delimiter='\t'))
    out_nodes = list(csv.DictReader(io.StringIO(kgx['nodes.tsv']), delimiter='\t'))
    assert len(out_edges) == len(edges) == 164
    assert len(out_nodes) == len(ids['identifiers']) == 87
    for edge, out in zip(doc['mechanistic_edges'], out_edges, strict=True):
        assert json.loads(out['evidence']) == edge['evidence']
        assert out['description'] == edge.get('description', '')
        assert out['subject'] == edge['subject'] and out['object'] == edge['object']
    hydration_out = next(n for n in out_nodes if n['id'] == 'RHEA:10750')
    assert hydration_out['category'] == 'biolink:BiochemicalReaction'
    for name, text in kgx.items():
        (RAW / ('actual-kgx-' + name)).write_text(text)
    print(json.dumps(dict(
        status='passed', scope='author source replay, not independent scientific review',
        target_sha256=target_hash, original_source_bodies=len(manifest['source_bodies']),
        references=len(doc['references']), original_rhea_nodes=len(nodes),
        native_objects=18, represented_reactions=17, enzymatic_transformations=16,
        chemical_side_assertions=78, formula_charge_balances=17,
        exact_native_chemical_bridges=29, explicitly_broader_native_chemical_bridge=1,
        exact_original_carboxylase_cds_translations=3, selected_strain_proteins=21,
        primary_locator_guards=len(projection['primary_locator_guards']),
        exact_primary_titles_checked=primary_titles_checked,
        terminal_module_claim_specific_locators_checked=3,
        native_and_closed_schema=True, kgx_nodes=len(out_nodes), kgx_edges=len(out_edges),
        kgx_evidence=sum(len(e['evidence']) for e in edges.values()), cycle_net=cycle_sum,
        chebi_database_sha256=digest(CACHE / 'chebi.db'),
        rhea_original_sha256=digest(CACHE / 'rhea.rdf.gz'),
        full_corpus_gates='delegated to root after final cohort freeze',
    ), indent=2))


if __name__ == '__main__':
    main()
