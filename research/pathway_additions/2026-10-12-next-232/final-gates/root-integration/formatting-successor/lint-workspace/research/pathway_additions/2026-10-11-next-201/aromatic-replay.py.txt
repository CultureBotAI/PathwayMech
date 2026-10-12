"""Replay the aromatic author's source claims, not an independent scientific review."""

from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.util
import io
import json
import re
import sqlite3
import zipfile
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
RAW = Path('/private/tmp/pathwaymech-next-201-evidence/aromatic')
CACHE = Path('/private/tmp/pathwaymech-curation-authorities')
TARGET = ROOT / 'data/pathways/phenylpropanoate-and-hydroxyphenylpropanoate-degradation.yaml'
RH = 'http://rdf.rhea-db.org/'
RDF = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'


@cache
def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(name):
    return json.loads((DOSSIER / ('aromatic-' + name + '.json')).read_text())


def xml(frame, tag):
    return etree.parse(str(RAW / (frame + '.xml'))).find(tag)


def main():
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert strict_errors([TARGET], ROOT) == []
    target_hash = digest(TARGET)
    projection = read('source-projection')
    manifest = read('source-manifest')
    ids = read('identifiers')
    authorities = read('authority-inputs')
    for receipt in [projection, manifest, ids, authorities, read('dedup')]:
        assert receipt['target_sha256'] == target_hash
    for body in manifest['source_bodies']:
        assert digest(body['raw_path']) == body['sha256'], body['raw_path']
    for ref in doc['references']:
        assert digest(manifest['reference_body_map'][ref['id']]) == ref['source_sha256']
    edges = {e['id']: e for e in doc['mechanistic_edges']}
    assert projection['graph_to_source'] == [
        dict(edge_id=e['id'], subject=e['subject'], predicate=e['predicate'],
             object=e['object'], evidence=e['evidence']) for e in doc['mechanistic_edges']
    ]
    wanted = {RH + r[k] for r in projection['native_member_coverage']
              for k in ['master', 'directed']}
    for side in projection['rhea_side_projection']:
        wanted.update(side[k] for k in ['side_uri', 'participant_uri', 'compound_uri'])
    nodes = {}
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
    assert set(nodes) == wanted
    chemical_edges = {e['id'] for e in doc['mechanistic_edges']
                      if e['predicate'] in {'consumes', 'produces'}}
    assert chemical_edges == {s['edge_id'] for s in projection['rhea_side_projection']}
    assert len(chemical_edges) == 39
    connection = sqlite3.connect(f'file:{CACHE / "chebi.db"}?mode=ro', uri=True)
    chemistry = {}
    for curie in {s['curie'][0] for s in projection['rhea_side_projection']}:
        chemistry[curie] = dict(connection.execute(
            'select predicate,value from statements where subject=? and value is not null',
            (curie,),
        ))
    balance = {}
    for side in projection['rhea_side_projection']:
        master, directed = RH + side['master'], RH + side['directed']
        assert directed in nodes[master]['directionalReaction']
        assert side['side_uri'] in nodes[directed][side['side']]
        assert side['participant_uri'] in nodes[side['side_uri']][side['coefficient_predicate']]
        assert side['compound_uri'] in nodes[side['participant_uri']]['compound']
        compound = nodes[side['compound_uri']]
        assert compound['accession'] == side['curie']
        curie = side['curie'][0]
        assert compound['formula'] == side['formula']
        assert compound['charge'] == side['charge']
        assert chemistry[curie]['chemrof:generalized_empirical_formula'] == side['formula'][0]
        assert chemistry[curie]['chemrof:charge'] == side['charge'][0]
        assert side['coefficient'] == int(side['coefficient_predicate'].removeprefix('contains'))
        edge = edges[side['edge_id']]
        endpoint = 'subject' if side['side'] == 'substrates' else 'object'
        assert edge[endpoint] == curie
        assert f"coefficient {side['coefficient']}" in edge['evidence'][0]['source_assertion']
        assert side['coefficient_predicate'] in edge['evidence'][0]['source_locator']
        total = balance.setdefault(side['directed'], {}).setdefault(side['side'], Counter())
        for atom, count in re.findall(r'([A-Z][a-z]?)(\d*)', side['formula'][0]):
            total[atom] += int(count or '1') * side['coefficient']
        total['charge'] += int(side['charge'][0]) * side['coefficient']
    for sides in balance.values():
        assert sides['substrates'] == sides['products']
    assert len(balance) == 8
    for reaction in doc['reactions']:
        uri = RH + reaction['id'].split(':')[1]
        assert reaction['label'] == nodes[uri]['label'][0]
        assert reaction['direction'] == (
            'right_to_left' if reaction['id'] == 'RHEA:22582' else 'left_to_right')
    # Full native members and exact source-issued family relationships, not name matching.
    parent = xml('PWY0-1277', 'Pathway')
    assert set(parent.xpath('./reaction-list/Pathway/@frameid')) == {
        'HCAMHPDEG-PWY', 'PWY-5162'}
    native_members = set()
    for child in ['HCAMHPDEG-PWY', 'PWY-5162']:
        native_members.update(xml(child, 'Pathway').xpath('./reaction-list/Reaction/@frameid'))
    assert native_members == {r['native'] for r in projection['native_member_coverage']}
    assert len(native_members) == 8
    for row in projection['native_member_coverage']:
        source = xml(row['native'], 'Reaction')
        xrefs = source.xpath('./dblink[dblink-db="RHEA"]/dblink-oid/text()')
        family = nodes[RH + row['master']]
        if xrefs:
            assert xrefs[0] == row['master'] or RH + xrefs[0] in (
                family.get('directionalReaction', []) + family.get('bidirectionalReaction', []))
        else:
            assert row['native'] == 'MHPCHYDROL-RXN'
        edge = edges[row['membership_edge']]
        assert edge['subject'] == 'RHEA:' + row['directed']
        assert edge['object'] == doc['id']
    # Every material edge has an exact native ordering plus two original chemical-side sources.
    for edge in doc['mechanistic_edges']:
        if edge['predicate'] != 'provides_input_for':
            continue
        native_evidence = edge['evidence'][0]
        frame = native_evidence['reference_id'].split(':')[1]
        mapping = {r['directed']: r['native'] for r in projection['native_member_coverage']}
        upstream = mapping[edge['subject'].split(':')[1]]
        downstream = mapping[edge['object'].split(':')[1]]
        assert xml(frame, 'Pathway').xpath(
            f'./reaction-ordering[Reaction/@frameid="{downstream}"]'
            f'/predecessor-reactions/Reaction[@frameid="{upstream}"]')
        assert len(edge['evidence']) == 3
        assert all(e['reference_id'].startswith('RHEA:') for e in edge['evidence'][1:])
        assert 'CHEBI:' not in native_evidence['source_assertion']
    # Chemical source conflicts are tested against structures and explicit hierarchy.
    for crosswalk in projection['native_chemical_crosswalks']:
        frame = crosswalk['native_id'].split(':')[1]
        source = xml('compound-' + frame, 'Compound')
        assert source.findtext('inchi') == crosswalk['native_inchi']
        assert source.findtext('inchi') == (
            chemistry[crosswalk['selected_curie']]['chemrof:inchi_string'])
        assert source.xpath('./dblink[dblink-db="CHEBI"]/dblink-oid/text()') == (
            crosswalk['native_chebi_xrefs'])
    native_cpd = xml('compound-CPD-157', 'Compound')
    stale = connection.execute(
        'select value from statements where subject=? and predicate=?',
        ('CHEBI:61449', 'chemrof:inchi_string'),
    ).fetchone()[0]
    assert stale != native_cpd.findtext('inchi')
    assert native_cpd.xpath('./dblink[dblink-db="CHEBI"]/dblink-oid/text()') == ['61449']
    assert connection.execute(
        'select 1 from statements where subject=? and predicate=? and object=?',
        ('CHEBI:60088', 'rdfs:subClassOf', 'CHEBI:60087'),
    ).fetchone()
    assert all(n['id'] not in {'CHEBI:61449', 'CHEBI:60088'} for n in doc['participants'])
    # Exact monomer crosswalks and actual native coefficients, with no invented Hca ratio.
    for assembly in projection['assemblies']:
        complex_node = xml(assembly['complex'], 'Protein')
        part = complex_node.xpath(
            f'./component[Protein/@frameid="{assembly["monomer"]}"]')[0]
        coefficient = part.findtext('coefficient')
        assert (int(coefficient) if coefficient is not None else None) == assembly['coefficient']
        monomer = xml(assembly['monomer'], 'Protein')
        assert monomer.xpath('./dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [
            assembly['accession']]
    protein_count = 0
    for node in doc['participants']:
        if not node['id'].startswith('UniProtKB:'):
            continue
        accession = node['id'].split(':')[1]
        entry = json.loads((RAW / f'uniprot-{accession}.json').read_text())
        assert entry['primaryAccession'] == accession and entry['organism']['taxonId'] == 83333
        assert node['label'] == entry['proteinDescription']['recommendedName']['fullName']['value']
        protein_count += 1
    assert protein_count == 11
    # Guard the experimentally important source-specific limitations.
    hca = html.fromstring((RAW / 'PMC107259-original.html').read_bytes()).text_content()
    assert 'the HcaB activity per se has not been demonstrated.' in ' '.join(hca.split())
    for subject in ['UniProtKB:P0CI31', 'UniProtKB:P77397', 'MetaCyc:HCAMULTI-CPLX']:
        assert any(e['subject'] == subject and e['predicate'] == 'enables'
                   for e in doc['mechanistic_edges'])
        assert not any(e['subject'] == subject and e['predicate'] == 'catalyzes'
                       for e in doc['mechanistic_edges'])
    mhpe = ' '.join(html.fromstring(
        (RAW / 'PMC106610-original.html').read_bytes()).text_content().split())
    assert 'showed no observable dependence on divalent metal ions' in mhpe
    assert 'presumably the 4S enantiomer' in mhpe
    assert not any(e['subject'] == 'UniProtKB:P51020' and e['predicate'] == 'has_cofactor'
                   for e in doc['mechanistic_edges'])
    cage = json.loads((RAW / 'pubmed-20053352.json').read_text())[
        'resultList']['result'][0]['abstractText']
    assert 'pentameric' in cage and '60 protein subunits' in cage and 'low pH' in cage
    for edge in doc['mechanistic_edges']:
        for evidence in edge['evidence']:
            ref_path = Path(manifest['reference_body_map'][evidence['reference_id']])
            if 'quote' in evidence:
                text = ' '.join(html.fromstring(ref_path.read_bytes()).text_content().split())
                assert evidence['quote'] in text
            if evidence['reference_id'].startswith('UniProtKB:'):
                entry = json.loads(ref_path.read_text())
                for index in re.findall(r'comments\[(\d+)\]', evidence['source_locator']):
                    assert entry['comments'][int(index)]
                for index in re.findall(r'uniProtKBCrossReferences\[(\d+)\]',
                                        evidence['source_locator']):
                    cross = entry['uniProtKBCrossReferences'][int(index)]
                    if evidence['reference_id'] == 'UniProtKB:P77397':
                        assert cross['database'] == 'EMBL' and cross['id'] == 'D86239'
                        assert any(p['value'] == 'BAA13052.1' for p in cross['properties'])
                    else:
                        assert cross['id'] == 'GO:0005737'
                        assert any(p['value'] == 'IDA:EcoliWiki' for p in cross['properties'])
    # Regress the actual independent-review findings against original source paragraphs.
    assert 'second paragraph' in edges['aromatic-edge-041']['evidence'][1]['source_locator']
    assert 'Table 2 p. 2577' in edges['aromatic-edge-079']['evidence'][3]['source_locator']
    assert 'mhpR, p. 2578' in edges['aromatic-edge-079']['evidence'][3]['source_locator']
    mhpa = html.fromstring((RAW / 'PMC6997738-original.html').read_bytes())
    def section(identifier):
        return ' '.join(mhpa.xpath(f'//*[@id="{identifier}"]')[0].text_content().split())
    assert mhpa.xpath('//meta[@name="citation_pmid"]/@content') == ['31811039']
    assert 'W3110' in section('s2.1') and 'completely lost' in section('s2.1')
    assert 'liquid chromatography-mass spectrometry' in section('s2.3')
    assert '669 kDa' in section('s2.2') and 'C terminus His-tagged' in section('s2.2')
    assert '0.81 mol of FAD' in section('s2.4')
    assert 'NADH' in section('s2.4') and 'NADPH' in section('s2.4')
    assert '9.61 min' in section('s4.7') and '445 nm' in section('s4.7')
    assert 'BAA13052' in mhpa.text_content()
    assert sum(e['reference_id'] == 'PMID:31811039'
               for e in edges['aromatic-edge-042']['evidence']) == 3
    assert any(e['reference_id'] == 'PMID:31811039'
               for e in edges['aromatic-edge-058']['evidence'])
    assert 'stoichiometry remains unresolved' in edges['aromatic-edge-042']['description']
    assert 'directly supported' in edges['aromatic-edge-058']['description']
    assert 'historical comment' in edges['aromatic-edge-042']['evidence'][2]['source_assertion']
    # Original map integrity and complete document-reaction dispositions.
    with zipfile.ZipFile(projection['pathbank_archive']['raw_path']) as archive:
        for item in projection['native_pathbank']:
            body = archive.read(item['member'])
            assert hashlib.sha256(body).hexdigest() == item['sha256']
            tree = etree.fromstring(body)
            subjects = [e.get('{' + RDF + '}about') if e.get('{' + RDF + '}about') is not None
                        else '#' + e.get('{' + RDF + '}ID') for e in tree
                        if e.get('{' + RDF + '}about') is not None or e.get('{' + RDF + '}ID')]
            assert sorted(subjects) == item['all_native_subjects']
            reactions = [e for e in tree if e.tag.endswith('}BiochemicalReaction')]
            projected = [o for o in item['objects'] if o['type'] == 'BiochemicalReaction']
            assert len(reactions) == len(projected) == 14
            assert all(r['disposition'] and r['reason'] for r in projected)
    spec = importlib.util.spec_from_file_location(
        'source_builder', ROOT / 'scripts/build_source_identifier_snapshot.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for source in authorities['proposed_source_inputs']:
        assert digest(source['raw_path']) == source['sha256']
        if source['kind'] == 'metacyc-html':
            assert list(module.metacyc_terms(Path(source['raw_path']).read_text())) == [
                (source['id'], source['canonical_label'], [])]
    for node in ids['named_nodes']:
        if node['id'].startswith('CHEBI:'):
            assert node['label'] == connection.execute(
                'select value from statements where subject=? and predicate=?',
                (node['id'], 'rdfs:label'),
            ).fetchone()[0]
    connection.close()
    for db, curie in [('go.db', 'GO:0005737'), ('ncbitaxon.db', 'NCBITaxon:83333')]:
        connection = sqlite3.connect(f'file:{CACHE / db}?mode=ro', uri=True)
        label = connection.execute(
            'select value from statements where subject=? and predicate=?',
            (curie, 'rdfs:label'),
        ).fetchone()[0]
        assert next(n['label'] for n in ids['named_nodes'] if n['id'] == curie) == label
        connection.close()
    kgx = render_kgx([record])
    exported = list(csv.DictReader(io.StringIO(kgx['edges.tsv']), delimiter='\t'))
    nodes_out = list(csv.DictReader(io.StringIO(kgx['nodes.tsv']), delimiter='\t'))
    assert len(exported) == len(doc['mechanistic_edges'])
    for edge, output in zip(doc['mechanistic_edges'], exported, strict=True):
        assert json.loads(output['evidence']) == edge['evidence']
        assert output['description'] == edge['description']
        assert output['subject'] == edge['subject'] and output['object'] == edge['object']
    assert len(nodes_out) == 48
    for name, value in kgx.items():
        (RAW / ('actual-kgx-' + name)).write_text(value)
    print(json.dumps(dict(
        result='pass', target_sha256=target_hash, scope='author replay, not independent review',
        native_and_closed_schema=True, original_body_count=len(manifest['source_bodies']),
        reference_body_count=len(doc['references']), complete_native_members=8,
        rhea_sides=39, formula_charge_balances=8, native_compound_crosswalks=17,
        exact_current_proteins=11, assembly_components=7, named_nodes=len(ids['named_nodes']),
        pathbank_maps=2, all_document_reactions_dispositioned=28,
        kgx_nodes=len(nodes_out), kgx_edges=len(exported),
        kgx_evidence=sum(len(e['evidence']) for e in doc['mechanistic_edges']),
        material_regressions=[
            'Full native eight-step union, no extra order-only or old keto-tautomer reaction',
            'Stale CPD-157 stereoisomer cross-reference rejected using exact original structure',
            'Absolute dihydrodiol versus relative-cis parent relationship preserved',
            'Native ordering does not impersonate the source of shared ChEBI identities',
            'HcaB isolated-activity limitation and functional enables retained',
            'Issues 365/367 exact locators and direct MhpA source/accession/donor/FAD scope',
            'MhpE metal independence and presumptive absolute assignment retained',
            'MhpD pentamer separated from conditional 60-subunit cage',
        ],
        full_corpus_gates='delegated to root after all cohort sources freeze',
    ), indent=2))


if __name__ == '__main__':
    main()
