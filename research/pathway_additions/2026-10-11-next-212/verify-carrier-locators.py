"""Check corrected carrier locators against original XML and the immutable draft."""
import argparse
import copy
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument('--record', required=True, type=Path)
parser.add_argument('--initial-record', required=True, type=Path)
parser.add_argument('--holo-dhbb-source', required=True, type=Path)
parser.add_argument('--dhbf-source', required=True, type=Path)
parser.add_argument('--output', required=True, type=Path)
args = parser.parse_args()
assert digest(args.initial_record) == (
    '2b2387392ceaedd93bcd2e28977b104eff01f6749a0012aca699b0b2ac8e3d9e'
)
original = yaml.safe_load(args.initial_record.read_text())
record = yaml.safe_load(args.record.read_text())
expected = copy.deepcopy(original)
source_specs = [
    ('Holo-DhbB', args.holo_dhbb_source,
     '10b44a70171a20f03c78f040587ef4466eb8efcc4fe10e0b1131646ba934e6e7',
     ['018', '033']),
    ('DhbF', args.dhbf_source,
     'e6d402775acc49fc63f147f6a4619631cdc85e1aeb2657cf93305961f30e6c0d',
     ['027', '041', '048', '052']),
]
checks = []
for frame, source, expected_hash, edge_numbers in source_specs:
    assert digest(source) == expected_hash
    matches = [item for item in ET.fromstring(source.read_bytes()).iter()
               if item.tag.split('}')[-1] == 'Protein' and item.get('frameid') == frame]
    native = max(matches, key=len)
    children = {item.tag.split('}')[-1] for item in native}
    assert {'common-name', 'parent'} <= children
    assert 'unmodified-form' not in children
    for number in edge_numbers:
        edge_id = 'bacillibactin-edge-' + number
        current = next(edge for edge in record['mechanistic_edges'] if edge['id'] == edge_id)
        before = next(edge for edge in expected['mechanistic_edges'] if edge['id'] == edge_id)
        reference = 'MetaCyc:' + frame
        locator = f'Protein[@frameid="{frame}"]/common-name; parent'
        assert current['evidence'][1]['reference_id'] == reference
        assert current['evidence'][1]['source_locator'] == locator, (
            edge_id + ': locator must name only fields present in the original source'
        )
        assert before['evidence'][1]['source_locator'] == locator + '; unmodified-form'
        before['evidence'][1]['source_locator'] = locator
        checks.append({'edge_id': edge_id, 'reference_id': reference,
                       'source_sha256': expected_hash, 'present_fields': sorted(children)})
assert record == expected, 'Other scientific fields or valid carrier selectors changed'
report = {'status': 'passed', 'record_sha256': digest(args.record),
          'initial_record_sha256': digest(args.initial_record), 'checked_locators': checks,
          'complete_record_equals_initial_plus_only_six_corrected_fields': True,
          'limits': ('Source-selector and exact-delta check; '
                     'global gates and scientific review are separate.')}
assert not args.output.exists(), 'Preserve an existing observation'
args.output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report))
