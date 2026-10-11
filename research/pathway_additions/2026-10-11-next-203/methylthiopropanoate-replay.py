"""Replay original MMPA pathway sources; this is author validation, not review."""

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
RAW = Path('/private/tmp/pathwaymech-next-203-evidence/methylthiopropanoate')
CACHE = Path('/private/tmp/pathwaymech-curation-authorities')
TARGET = ROOT / 'data/pathways/methylthiopropanoate-degradation-i.yaml'
RH = 'http://rdf.rhea-db.org/'
RDF = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'


@cache
def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(name):
    return json.loads((DOSSIER / ('methylthiopropanoate-' + name + '.json')).read_text())


def xml(frame, tag):
    return etree.parse(str(RAW / (frame + '.xml'))).find(tag)


def normalized(text):
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
    edges = {e['id']: e for e in doc['mechanistic_edges']}
    assert projection['graph_to_source'] == [
        dict(edge_id=e['id'], subject=e['subject'], predicate=e['predicate'],
             object=e['object'], evidence=e['evidence']) for e in doc['mechanistic_edges']
    ]
    # Read original RDF, merging repeated descriptions of each selected subject.
    wanted = set(projection['original_rhea_nodes'])
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
    assert nodes == projection['original_rhea_nodes']
    chemical_edges = {e['id'] for e in edges.values()
                      if e['predicate'] in {'consumes', 'produces'}}
    assert chemical_edges == {s['edge_id'] for s in projection['rhea_side_projection']}
    assert len(chemical_edges) == 17
    con = sqlite3.connect(f'file:{CACHE / "chebi.db"}?mode=ro', uri=True)

    def chemistry(curie):
        return dict(con.execute(
            'select predicate,value from statements where subject=? and value is not null',
            (curie,),
        ))

    balances = {}
    net_counts = {}
    all_sides = projection['rhea_side_projection'] + projection['rhea_component_projection']
    for row in all_sides:
        master, directed = RH + row['master'], RH + row['directed']
        assert directed in nodes[master]['directionalReaction']
        assert row['side_uri'] in nodes[directed][row['side']]
        assert row['participant_uri'] in nodes[row['side_uri']][row['coefficient_predicate']]
        assert row['compound_uri'] in nodes[row['participant_uri']]['compound']
        assert row['coefficient'] == int(row['coefficient_predicate'].removeprefix('contains'))
        compound = nodes[row['compound_uri']]
        assert compound == row['compound']
        curie = row['curie'][0]
        assert [s.replace('GENERIC:', 'RHEA-COMP:') for s in compound['accession']] == [curie]
        total = balances.setdefault(row['directed'], {}).setdefault(row['side'], Counter())
        # Whole carrier stays a polypeptide class. Only its original declared reactive
        # part is used for formal balance; identical protein scaffold cancels.
        parts = [nodes[u] for u in compound.get('reactivePart', [])] or [compound]
        for part in parts:
            formula, charge = part['formula'][0], part['charge'][0]
            chebi = curie if curie.startswith('CHEBI:') else (
                part['chebi'][0].split('/')[-1].replace('_', ':'))
            auth = chemistry(chebi)
            assert auth['chemrof:generalized_empirical_formula'] == formula
            assert auth['chemrof:charge'] == charge
            for atom, count in re.findall(r'([A-Z][a-z]?)(\d*)', formula):
                total[atom] += int(count or '1') * row['coefficient']
            total['charge'] += int(charge) * row['coefficient']
        signed = row['coefficient'] * (1 if row['side'] == 'products' else -1)
        counts = net_counts.setdefault(row['directed'], Counter())
        counts[curie] += signed
        if 'edge_id' in row:
            edge = edges[row['edge_id']]
            endpoint = 'subject' if row['side'] == 'substrates' else 'object'
            assert edge[endpoint] == curie
            ev = edge['evidence'][0]
            assert f"coefficient {row['coefficient']}" in ev['source_assertion']
            for fragment in [row['side_uri'], row['coefficient_predicate'],
                             row['participant_uri'], row['compound_uri']]:
                assert fragment in ev['source_locator']
    for sides in balances.values():
        assert sides['substrates'] == sides['products']
    assert len(balances) == 7
    summed = Counter()
    for rx in ['45149', '45153', '45157', '45161']:
        summed.update(net_counts[rx])
    assert {k: v for k, v in summed.items() if v} == dict(net_counts['45145'])
    assert {x['id'] for x in doc['reactions']} == {'RHEA:43053', 'RHEA:52613', 'RHEA:45145'}
    for reaction in doc['reactions']:
        assert reaction['label'] == nodes[RH + reaction['id'].split(':')[1]]['label'][0]
        assert reaction['direction'] == 'left_to_right'
    native = xml('PWY-6048', 'Pathway')
    assert set(native.xpath('./reaction-list/Reaction/@frameid')) == {
        'RXN-12571', 'RXN-12572', 'RXN-12573'}
    for row in projection['native_member_coverage']:
        source = xml(row['native'], 'Reaction')
        expected = 'LEFT-TO-RIGHT' if row['native'] == 'RXN-12572' else 'PHYSIOL-LEFT-TO-RIGHT'
        assert source.findtext('reaction-direction') == expected
        assert row['enzymatic_reaction'] in source.xpath(
            './enzymatic-reaction/Enzymatic-Reaction/@frameid')
        annotation = xml(row['enzymatic_reaction'], 'Enzymatic-Reaction')
        assert annotation.xpath('./enzyme/Protein/@frameid') == [row['enzyme_frame']]
        assert annotation.xpath('./reaction/Reaction/@frameid') == [row['native']]
        protein = xml(row['enzyme_frame'], 'Protein')
        assert protein.xpath('./dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == [
            row['uniprot']]
        assert protein.xpath('./species/Organism/@frameid') == ['TAX-246200']
        current = json.loads((RAW / ('uniprot-' + row['uniprot'] + '.json')).read_text())
        assert current['primaryAccession'] == row['uniprot']
        assert current['organism']['taxonId'] == 246200
        xrefs = current['comments'][1]['reaction']['reactionCrossReferences']
        assert {'database': 'Rhea', 'id': 'RHEA:' + row['master']} in xrefs
        assert edges[row['membership_edge']]['subject'] == 'RHEA:' + row['directed']
        native_xref = source.xpath('./dblink[dblink-db="RHEA"]/dblink-oid/text()')
        assert native_xref == ([] if row['native'] == 'RXN-12572' else [row['directed']])
    for frame, facts in projection['native_objects'].items():
        assert digest(facts['raw_path']) == facts['sha256']
        original = xml(frame, facts['tag'])
        assert original.get('frameid') == facts['frameid']
        for key in ['common-name', 'reaction-direction', 'physiologically-relevant',
                    'ec-number', 'inchi', 'inchi-key']:
            if key in facts:
                assert [e.text for e in original.findall(key)] == facts[key]
        if frame == 'PWY-6048':
            comment = html.fromstring('<div>' + original.findtext('comment') + '</div>')
            assert facts['comment_disposition']['excerpt'] in comment.text_content()
    # The four component reactions remain in research, with their original xrefs;
    # none is separately claimed as a DmdD-catalyzed graph reaction.
    composite = xml('RXN-12573', 'Reaction')
    components = composite.xpath('./reaction-list/Reaction/@frameid')
    assert set(components) == {'RXN-16010', 'RXN-16011', 'RXN-16012', 'RXN-16013'}
    for native_rx, rx in zip(sorted(components), ['45149', '45153', '45157', '45161'], strict=True):
        assert xml(native_rx, 'Reaction').xpath(
            './dblink[dblink-db="RHEA"]/dblink-oid/text()') == [rx]
    for bridge in projection['native_chemical_bridges']:
        assert xml(bridge['native'], 'Compound').findtext('inchi') == bridge['native_inchi']
        assert bridge['native_inchi'] == chemistry(bridge['chebi'])['chemrof:inchi_string']
    assert '/b8-5+' in chemistry('CHEBI:84994')['chemrof:inchi_string']
    for edge in edges.values():
        if edge['predicate'] == 'provides_input_for':
            side_sources = [e for e in edge['evidence'] if e['reference_id'].startswith('RHEA:')]
            assert len(side_sources) == 2
            assert {e['reference_id'] for e in side_sources} == {edge['subject'], edge['object']}
        if edge['subject'].startswith('RHEA-COMP:') or edge['object'].startswith('RHEA-COMP:'):
            assert {e['reference_id'] for e in edge['evidence']} == {
                'RHEA:52613', 'MetaCyc:RXN-12572', 'UniProtKB:Q5LLW7'}
            assert 'remains unresolved' in edge['description']
    # Primary source/locator guards constrain important interpretations.
    dmdc = html.fromstring((RAW / 'PMC8824276.html').read_bytes())
    section = normalized(' '.join(dmdc.xpath('//*[@id="s2-3"]//text()')))
    for phrase in ['130.5 kDa', 'homodimer', 'uncharacterized flavoprotein in vivo',
                   'No activity was detected with DCPIP, FAD, FMN, or NADP']:
        assert phrase in section
    cloning = normalized(' '.join(dmdc.xpath('//*[@id="s3-1"]//text()')))
    assert 'SPO3804' in cloning and 'Ruegeria pomeroyi DSS-3' in cloning
    dmdb = html.fromstring((RAW / 'PMC3957724.html').read_bytes())
    assert 'Mg2+ was required for activity' in normalized(
        dmdb.xpath('//*[@id="sec3-2"]')[0].text_content())
    relief = normalized(' '.join(dmdb.xpath('//*[@id="sec3-6"]//text()')))
    assert 'ADP had no effect on the DMSP inhibition of RPO_DmdB2' in relief
    assert '80% of activity was regained' in relief and '8 mM' in relief
    dmdd = etree.parse(str(RAW / 'PMC3660561.xml'))
    mechanism = normalized(' '.join(dmdd.xpath('//sec[@id="s2g"]//text()')))
    assert 'spontaneous outcome' in mechanism
    assert 'spontaneously decompose, producing' in mechanism
    assert 'It is expected that this compound' in mechanism
    assert 'hexamer' in normalized(' '.join(dmdd.xpath('//sec[@id="s2b"]//text()')))
    # Canonical labels and source-body authority are checked independently of YAML labels.
    spec = importlib.util.spec_from_file_location(
        'sourcebuilder', ROOT / 'scripts/build_source_identifier_snapshot.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for source in authorities['proposed_source_inputs']:
        assert digest(source['raw_path']) == source['sha256']
        if source['kind'] == 'metacyc-html':
            assert list(module.metacyc_terms(Path(source['raw_path']).read_text())) == [
                (source['id'], source['canonical_label'], [])]
    for node in ids['named_nodes']:
        if node['id'].startswith('CHEBI:'):
            assert node['label'] == chemistry(node['id'])['rdfs:label']
        elif node['id'].startswith('UniProtKB:'):
            source_path = RAW / ('uniprot-' + node['id'].split(':')[1] + '.json')
            entry = json.loads(source_path.read_text())
            name = entry['proteinDescription']['recommendedName']['fullName']['value']
            assert node['label'] == name
    kgx = render_kgx([record])
    exported = list(csv.DictReader(io.StringIO(kgx['edges.tsv']), delimiter='\t'))
    nodes_out = list(csv.DictReader(io.StringIO(kgx['nodes.tsv']), delimiter='\t'))
    assert len(exported) == len(edges) == 29
    assert len(nodes_out) == 25
    for edge, out in zip(doc['mechanistic_edges'], exported, strict=True):
        assert json.loads(out['evidence']) == edge['evidence']
        assert out['description'] == edge.get('description', '')
        assert out['subject'] == edge['subject'] and out['object'] == edge['object']
    for name, value in kgx.items():
        (RAW / ('actual-kgx-' + name)).write_text(value)
    print(json.dumps(dict(
        result='pass', target_sha256=target_hash, scope='author replay, not independent review',
        native_and_closed_schema=True, source_body_count=len(manifest['source_bodies']),
        reference_body_count=len(doc['references']), complete_native_members=3,
        rhea_graph_sides=17, additional_component_sides=15, formula_charge_balances=7,
        composite_components_sum_exactly_to_net=True, exact_native_inchi_bridges=3,
        reviewed_protein_crosswalks=3, named_nodes=len(ids['named_nodes']),
        kgx_nodes=len(nodes_out), kgx_edges=len(exported),
        kgx_evidence=sum(len(e['evidence']) for e in edges.values()),
        safeguards=['Generic ETF class is not direct primary physiological specificity',
                    'DmdD net and component chemistry are not double counted',
                    'DSS-3 dimer/dimer/hexamer roles do not assert monomer sufficiency',
                    'DmdB2 conditional MMPA relief is distinct from DmdB1 ADP relief',
                    'DmdC FAD inference is distinct from a free-FAD electron acceptor'],
        full_corpus_gates='delegated to root after cohort freeze',
    ), indent=2))


if __name__ == '__main__':
    main()
