"""Replay authored PreQ0 assertions against original inputs; not scientific review."""

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
from pathlib import Path

import yaml
from lxml import etree

from pathwaymech.kgx import render_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path(__file__).resolve().parents[3]
DOSSIER = Path(__file__).parent
RAW = Path('/private/tmp/pathwaymech-next-198-evidence/preq0')
CACHE = Path('/private/tmp/pathwaymech-curation-authorities')
TARGET = ROOT / 'data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml'
RH = 'http://rdf.rhea-db.org/'
NS = {'rh': RH, 'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
      'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
RDF_RESOURCE = '{' + NS['rdf'] + '}resource'


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(name):
    return json.loads((DOSSIER / ('preq0-' + name + '.json')).read_text())


def main():
    doc = yaml.safe_load(TARGET.read_text())
    record = validate_record(doc)
    assert strict_errors([TARGET], ROOT) == []
    target_hash = digest(TARGET)
    projection = read('source-projection')
    manifest = read('source-manifest')
    identifiers = read('identifiers')
    authorities = read('authority-inputs')
    for receipt in [projection, manifest, identifiers, authorities, read('dedup')]:
        assert receipt['target_sha256'] == target_hash
    original_hashes = {}
    for item in manifest['source_bodies']:
        path = item['raw_path']
        observed = original_hashes.setdefault(path, digest(path))
        assert observed == item['sha256'], path
    for ref in doc['references']:
        assert digest(manifest['reference_body_map'][ref['id']]) == ref['source_sha256']
    edges = {e['id']: e for e in doc['mechanistic_edges']}
    assert projection['graph_to_source'] == [
        {key: edge[key] for key in ['edge_id', 'subject', 'predicate', 'object', 'evidence']}
        for edge in [dict(edge_id=e['id'], **e) for e in doc['mechanistic_edges']]
    ]
    chemical_edges = {
        e['id'] for e in doc['mechanistic_edges'] if e['predicate'] in {'consumes', 'produces'}
    }
    assert chemical_edges == {s['edge_id'] for s in projection['rhea_side_projection']}
    # Read original RDF, never use the derived projection as authority.
    wanted = {RH + i for i in ['17473', '17474', '27966', '27967', '27974',
                              '27975', '27982', '27983']}
    for side in projection['rhea_side_projection']:
        wanted.update(side[k] for k in ['side_uri', 'participant_uri', 'compound_uri'])
    original = gzip.open(CACHE / 'rhea.rdf.gz', 'rt').read()
    nodes = {}
    wrapper = '<root ' + ' '.join(f'xmlns:{k}="{v}"' for k, v in NS.items()) + '>'
    for match in re.finditer(r'<rdf:Description rdf:about="([^"]+)">', original):
        uri = match[1]
        if uri not in wanted:
            continue
        end = original.index('</rdf:Description>', match.start()) + len('</rdf:Description>')
        element = etree.fromstring((wrapper + original[match.start():end] + '</root>').encode())[0]
        props = nodes.setdefault(uri, {})
        for child in element:
            key = child.tag.split('}', 1)[1]
            value = child.get(RDF_RESOURCE) or child.text
            if value not in props.setdefault(key, []):
                props[key].append(value)
    assert wanted == set(nodes)
    del original
    connection = sqlite3.connect(f'file:{CACHE / "chebi.db"}?mode=ro', uri=True)
    chemistry = {}
    for curie in {s['curie'][0] for s in projection['rhea_side_projection']}:
        chemistry[curie] = dict(connection.execute(
            'SELECT predicate,value FROM statements WHERE subject=? AND value IS NOT NULL',
            (curie,),
        ).fetchall())
    totals = {}
    for side in projection['rhea_side_projection']:
        master, directed = RH + side['master'], RH + side['directed']
        assert directed in nodes[master]['directionalReaction']
        assert side['side_uri'] in nodes[directed][side['side']]
        assert side['participant_uri'] in nodes[side['side_uri']][side['coefficient_predicate']]
        assert side['compound_uri'] in nodes[side['participant_uri']]['compound']
        compound = nodes[side['compound_uri']]
        for key in ['formula', 'charge']:
            assert compound[key] == side[key]
        assert compound['accession'] == side['curie']
        curie = side['curie'][0]
        formula, charge = side['formula'][0], int(side['charge'][0])
        assert chemistry[curie]['chemrof:generalized_empirical_formula'] == formula
        assert chemistry[curie]['chemrof:charge'] == str(charge)
        edge = edges[side['edge_id']]
        endpoint = 'subject' if side['side'] == 'substrates' else 'object'
        assert edge[endpoint] == curie
        assert f"coefficient {side['coefficient']}" in edge['evidence'][0]['source_assertion']
        assert side['coefficient_predicate'] in edge['evidence'][0]['source_locator']
        total = totals.setdefault(side['directed'], {}).setdefault(side['side'], Counter())
        for atom, count in re.findall(r'([A-Z][a-z]?)(\d*)', formula):
            total[atom] += int(count or '1') * side['coefficient']
        total['charge'] += charge * side['coefficient']
    for sides in totals.values():
        assert sides['substrates'] == sides['products']
    # Meaningful regression: the old one-ATP/ADP source remains disclosed, never exported.
    quec = [s for s in projection['rhea_side_projection'] if s['directed'] == '27983']
    assert {(s['side'], s['curie'][0], s['coefficient']) for s in quec} == {
        ('substrates', 'CHEBI:61036', 1), ('substrates', 'CHEBI:28938', 1),
        ('substrates', 'CHEBI:30616', 2), ('products', 'CHEBI:45075', 1),
        ('products', 'CHEBI:456215', 2), ('products', 'CHEBI:33019', 2),
        ('products', 'CHEBI:15378', 2),
    }
    for reaction in doc['reactions']:
        assert reaction['label'] == nodes[RH + reaction['id'].split(':')[1]]['label'][0]
    pw = etree.parse(str(RAW / 'PWY-6703.xml')).find('Pathway')
    assert pw.get('frameid') == 'PWY-6703'
    native_members = {r.get('frameid') for r in pw.findall('./reaction-list/Reaction')}
    assert native_members == {r['native_id'].split(':')[1] for r in projection['reactions']}
    assert len(native_members) == 4
    for reaction in projection['reactions']:
        frame = reaction['native_id'].split(':')[1]
        element = etree.parse(reaction['raw_path']).find('Reaction')
        assert element.get('frameid') == frame
        assert element.findtext('reaction-direction') == reaction['native_direction']
        assert element.xpath('./dblink[dblink-db="RHEA"]/dblink-oid/text()') == (
            reaction['native_rhea_xrefs']
        )
    assert etree.parse(str(RAW / 'RXN-12093.xml')).xpath(
        '/ptools-xml/Reaction/right/Compound[@frameid="ADP"]'
    )
    # Assembly identity and source-specific inference tiers, not an experiment-count shortcut.
    for frame, monomer, count in [('FOLE-CPLX', 'GTP-CYCLOHYDRO-I-MONOMER', 10),
                                  ('CPLX0-8123', 'G7431-MONOMER', 6)]:
        protein = etree.parse(str(RAW / (frame + '.xml'))).find('Protein')
        assert protein.find('./component/Protein').get('frameid') == monomer
        assert int(protein.findtext('./component/coefficient')) == count
    monomer = etree.parse(str(RAW / 'G7431-MONOMER.xml')).find('Protein')
    assert monomer.xpath('./dblink[dblink-db="UNIPROT"]/dblink-oid/text()') == ['P65870']
    for accession in ['P0A6T5', 'P65870', 'P64554', 'P77756']:
        entry = json.loads((RAW / f'uniprot-{accession}.json').read_text())
        assert entry['primaryAccession'] == accession
        assert entry['organism']['taxonId'] == 83333
        node = next(n for n in doc['participants'] if n['id'] == 'UniProtKB:' + accession)
        assert node['label'] == entry['proteinDescription']['recommendedName']['fullName']['value']
    for accession, rule in [('P64554', 'MF_00917'), ('P77756', 'MF_01633')]:
        entry = json.loads((RAW / f'uniprot-{accession}.json').read_text())
        proof = entry['comments'][1]['reaction']['evidences']
        assert proof == [{'evidenceCode': 'ECO:0000255', 'source': 'HAMAP-Rule', 'id': rule}]
        role = next(e for e in doc['mechanistic_edges']
                    if e['subject'] == 'UniProtKB:' + accession and e['predicate'] == 'enables')
        assert 'inference' in role['description']
        assert not any(e['subject'] == 'UniProtKB:' + accession and e['predicate'] == 'catalyzes'
                       for e in doc['mechanistic_edges'])
    quee = json.loads((RAW / 'uniprot-P64554.json').read_text())
    for index, curie in [(2, 'CHEBI:49883'), (3, 'CHEBI:59789'), (4, 'CHEBI:18420')]:
        assert quee['comments'][index]['cofactors'][0]['cofactorCrossReference']['id'] == curie
    queued = json.loads((RAW / 'uniprot-P65870.json').read_text())
    assert 'homotrimers and homododecamers' in queued['comments'][7]['texts'][0]['value']
    assert 'homohexamer' in queued['comments'][8]['texts'][0]['value']
    # Original BioC manuscript passages support the selected limitations literally.
    primary = etree.parse(str(RAW / 'PMC4022186-bioc.xml')).findall('.//passage')
    assert 'Bacillus subtilis' in primary[1].findtext('text')
    assert 'SAM is regenerated' in primary[58].findtext('text')
    toym = etree.parse(str(RAW / 'PMC4767005-bioc.xml')).findall('.//passage')
    assert 'Streptomyces rimosus' in toym[3].findtext('text')
    assert 'two ATP-dependent half reactions' in toym[6].findtext('text')
    for edge in doc['mechanistic_edges']:
        for evidence in edge['evidence']:
            if 'quote' in evidence:
                path = manifest['reference_body_map'][evidence['reference_id']]
                text = ' '.join(etree.parse(path).getroot().itertext())
                assert evidence['quote'] in text
    # Complete original PathBank subject inventory and all nine reaction objects on each map.
    archive = (
        '/private/tmp/pathwaymech-pathbank-dbcan-evidence/pathbank/'
        'pathbank_primary_biopax.zip'
    )
    with zipfile.ZipFile(archive) as source:
        for member in projection['native_pathbank']:
            payload = source.read(member['member'])
            assert hashlib.sha256(payload).hexdigest() == member['sha256']
            tree = etree.fromstring(payload)
            ids = []
            for node in tree:
                about = node.get('{' + NS['rdf'] + '}about')
                rdf_id = node.get('{' + NS['rdf'] + '}ID')
                if about is not None:
                    ids.append(about)
                elif rdf_id is not None:
                    ids.append('#' + rdf_id)
            assert sorted(ids) == member['all_native_subjects']
            assert len(member['reactions']) == 9
            assert all(r['disposition'] for r in member['reactions'])
    spec = importlib.util.spec_from_file_location(
        'source_builder', ROOT / 'scripts/build_source_identifier_snapshot.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for item in authorities['proposed_source_inputs']:
        assert digest(item['raw_path']) == item['sha256']
        if item['kind'] == 'metacyc-html':
            assert list(module.metacyc_terms(Path(item['raw_path']).read_text())) == [
                (item['id'], item['canonical_label'], [])]
    # All named identifiers are independently checked, including still-pending root snapshots.
    by_id = {n['id']: n for n in identifiers['named_identifiers']}
    for curie, node in by_id.items():
        if curie.startswith('CHEBI:'):
            label = connection.execute(
                "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'",
                (curie,),
            ).fetchone()[0]
            assert label == node['label']
    connection.close()
    for database, curie in [('go.db', 'GO:0097288'), ('ncbitaxon.db', 'NCBITaxon:83333')]:
        connection = sqlite3.connect(f'file:{CACHE / database}?mode=ro', uri=True)
        label = connection.execute(
            "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'",
            (curie,),
        ).fetchone()[0]
        assert label == by_id[curie]['label']
        connection.close()
    kgx = render_kgx([record])
    exported = list(csv.DictReader(io.StringIO(kgx['edges.tsv']), delimiter='\t'))
    nodes_out = list(csv.DictReader(io.StringIO(kgx['nodes.tsv']), delimiter='\t'))
    assert len(exported) == len(doc['mechanistic_edges'])
    for edge, output in zip(doc['mechanistic_edges'], exported, strict=True):
        assert json.loads(output['evidence']) == edge['evidence']
        assert output['description'] == edge['description']
        assert output['subject'] == edge['subject'] and output['object'] == edge['object']
    assert len(nodes_out) == 30
    for name, text in kgx.items():
        (RAW / ('actual-kgx-' + name)).write_text(text)
    result = dict(
        target_sha256=target_hash, result='pass', scope='author replay, not independent review',
        native_and_closed_schema=True, original_source_bodies=len(manifest['source_bodies']),
        complete_native_members=len(native_members), rhea_sides=len(chemical_edges),
        balanced_reactions=len(totals), named_identifiers=len(by_id),
        pathbank_complete_map_dispositions=2, pathbank_reactions_dispositioned=18,
        kgx_nodes=len(nodes_out), kgx_edges=len(exported),
        kgx_evidence=sum(len(e['evidence']) for e in doc['mechanistic_edges']),
        verified_reference_bodies=len(doc['references']),
        regressions=[
            'current two-ATP QueC equation and obsolete native equation retained separately',
                     'Bacillus QueE and Streptomyces ToyM scope not transferred to E. coli',
                     'E. coli QueE/QueC automatic inference preserved in functional roles',
                     'SAM regeneration and QueD alternate assemblies explicitly retained'],
        full_shared_gates='delegated to root after all cohort inputs freeze',
    )
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
