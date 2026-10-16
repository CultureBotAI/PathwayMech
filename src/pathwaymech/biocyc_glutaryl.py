"""Complete issuing originals for the bounded PWY-5177 native graph additions.

Names come only from direct issuing XML slots; the profile contains no curated
labels. Both boundaries replay complete source bytes, envelope and every slot.
Native activity identities remain distinct from generic reactions. Protein-class
ETF references in equations remain classes, never exact proteins or free FAD.
Existing P321, phenylacetate and other authority owners are unchanged.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import (
    FRAME,
    HOST,
    PROVENANCE,
    PROVENANCE_ORDER,
    _TreeBuilder,
    keys,
    name,
    one,
    original_path,
    require,
    scalar,
)
from pathwaymech.biocyc_native_context import attributes, blank, integer, ref_node
from pathwaymech.biocyc_p321 import original_bytes

KIND = "metacyc-glutaryl-xml"
GLUTARYL_KINDS = {KIND}
FIELD = "native_glutaryl"
_NATIVE_IDENTITY_ATTRIBUTES = {"frameid", "orgid", "ID", "resource"}
# Closed observed object types, including tags whose identity attributes were removed.
_NATIVE_OBJECT_TAGS = {'Compound',
 'Enzymatic-Reaction',
 'Evidence-Code',
 'Feature',
 'GO-Term',
 'Gene',
 'Organism',
 'Organization',
 'Pathway',
 'Person',
 'Protein',
 'Publication',
 'Reaction',
 'Regulation',
 'cco'}
# Complete direct-slot multiplicities of the 49 reviewed full originals.
# Label text, aliases and opaque scientific annotations are never supplied here.
PROFILES = {'MetaCyc:ACETOACETYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                       'appears-in-right-side-of': 1,
                                       'cml': 1,
                                       'common-name': 1,
                                       'dblink': 13,
                                       'gibbs-0': 1,
                                       'inchi': 1,
                                       'inchi-key': 1,
                                       'molecular-weight': 1,
                                       'monoisotopic-mw': 1,
                                       'parent': 2,
                                       'regulates': 1,
                                       'synonym': 2},
                             'tag': 'Compound'},
 'MetaCyc:ACETYL-COA-ACETYLTRANSFER-CPLX': {'slots': {'catalyzes': 1,
                                                      'component': 1,
                                                      'credits': 1,
                                                      'molecular-weight-exp': 1,
                                                      'parent': 1,
                                                      'species': 1},
                                            'tag': 'Protein'},
 'MetaCyc:ACETYL-COA-ACETYLTRANSFER-ENZRXN': {'slots': {'comment': 1,
                                                        'common-name': 1,
                                                        'credits': 1,
                                                        'enzyme': 1,
                                                        'evidence': 2,
                                                        'kcat': 2,
                                                        'km': 4,
                                                        'physiologically-relevant': 1,
                                                        'reaction': 1,
                                                        'reaction-direction': 1,
                                                        'regulated-by': 1,
                                                        'synonym': 4},
                                              'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ACETYL-COA-ACETYLTRANSFER-MONOMER': {'slots': {'comment': 1,
                                                         'common-name': 1,
                                                         'component-of': 1,
                                                         'credits': 1,
                                                         'dblink': 24,
                                                         'gene': 1,
                                                         'has-feature': 5,
                                                         'has-go-term': 12,
                                                         'location': 1,
                                                         'molecular-weight-exp': 1,
                                                         'molecular-weight-seq': 1,
                                                         'parent': 1,
                                                         'species': 1,
                                                         'synonym': 1},
                                               'tag': 'Protein'},
 'MetaCyc:BUTYRYL-COA': {'slots': {'abbrev-name': 1,
                                   'appears-in-left-side-of': 1,
                                   'appears-in-right-side-of': 1,
                                   'cml': 1,
                                   'common-name': 1,
                                   'dblink': 11,
                                   'gibbs-0': 1,
                                   'inchi': 1,
                                   'inchi-key': 1,
                                   'molecular-weight': 1,
                                   'monoisotopic-mw': 1,
                                   'parent': 1,
                                   'regulates': 1,
                                   'synonym': 2,
                                   'systematic-name': 1},
                         'tag': 'Compound'},
 'MetaCyc:CARBON-DIOXIDE': {'slots': {'appears-in-left-side-of': 1,
                                      'appears-in-right-side-of': 1,
                                      'cml': 1,
                                      'common-name': 1,
                                      'dblink': 11,
                                      'gibbs-0': 1,
                                      'inchi': 1,
                                      'inchi-key': 1,
                                      'molecular-weight': 1,
                                      'monoisotopic-mw': 1,
                                      'synonym': 3},
                            'tag': 'Compound'},
 'MetaCyc:CPLX-4041': {'slots': {'catalyzes': 1,
                                 'comment': 1,
                                 'common-name': 1,
                                 'component': 1,
                                 'credits': 1,
                                 'molecular-weight-exp': 1,
                                 'parent': 1,
                                 'species': 1,
                                 'synonym': 1},
                       'tag': 'Protein'},
 'MetaCyc:CPLX-41': {'slots': {'catalyzes': 1,
                               'comment': 1,
                               'common-name': 1,
                               'component': 1,
                               'molecular-weight-exp': 1,
                               'parent': 1,
                               'species': 1,
                               'synonym': 1},
                     'tag': 'Protein'},
 'MetaCyc:CPLX-6989': {'slots': {'catalyzes': 1,
                                 'comment': 1,
                                 'common-name': 1,
                                 'component': 1,
                                 'molecular-weight-exp': 1,
                                 'parent': 1,
                                 'pi': 1,
                                 'species': 1},
                       'tag': 'Protein'},
 'MetaCyc:CPLX-7035': {'slots': {'catalyzes': 1,
                                 'citation': 1,
                                 'comment': 1,
                                 'common-name': 1,
                                 'component': 1,
                                 'credits': 1,
                                 'molecular-weight-exp': 1,
                                 'parent': 1,
                                 'species': 1},
                       'tag': 'Protein'},
 'MetaCyc:CPLX-706': {'slots': {'catalyzes': 1,
                                'comment': 1,
                                'common-name': 1,
                                'component': 1,
                                'parent': 1,
                                'species': 1},
                      'tag': 'Protein'},
 'MetaCyc:CPLX-7355': {'slots': {'catalyzes': 1,
                                 'comment': 1,
                                 'component': 1,
                                 'credits': 1,
                                 'molecular-weight-exp': 1,
                                 'parent': 1,
                                 'species': 1},
                       'tag': 'Protein'},
 'MetaCyc:CPLX-7788': {'slots': {'catalyzes': 1,
                                 'comment': 1,
                                 'common-name': 1,
                                 'component': 1,
                                 'credits': 1,
                                 'molecular-weight-exp': 1,
                                 'parent': 1,
                                 'species': 1},
                       'tag': 'Protein'},
 'MetaCyc:CROTONYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                    'appears-in-right-side-of': 1,
                                    'cml': 1,
                                    'common-name': 1,
                                    'dblink': 10,
                                    'gibbs-0': 1,
                                    'inchi': 1,
                                    'inchi-key': 1,
                                    'molecular-weight': 1,
                                    'monoisotopic-mw': 1,
                                    'parent': 1,
                                    'regulates': 1,
                                    'synonym': 8},
                          'tag': 'Compound'},
 'MetaCyc:CRTCLOS-MONOMER': {'slots': {'common-name': 1,
                                       'component-of': 1,
                                       'dblink': 10,
                                       'gene': 1,
                                       'molecular-weight-exp': 1,
                                       'molecular-weight-seq': 1,
                                       'parent': 1,
                                       'species': 1,
                                       'synonym': 1},
                             'tag': 'Protein'},
 'MetaCyc:ENZRXN-22164': {'slots': {'common-name': 1,
                                    'enzyme': 1,
                                    'evidence': 1,
                                    'km': 3,
                                    'ph-opt': 2,
                                    'physiologically-relevant': 1,
                                    'reaction': 1,
                                    'reaction-direction': 1,
                                    'regulated-by': 1,
                                    'temperature-opt': 1,
                                    'vmax': 2},
                          'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXN-41': {'slots': {'alternative-substrate': 1,
                                 'common-name': 1,
                                 'enzyme': 1,
                                 'evidence': 1,
                                 'km': 1,
                                 'physiologically-relevant': 1,
                                 'reaction': 1,
                                 'reaction-direction': 1,
                                 'regulated-by': 1,
                                 'synonym': 2},
                       'tag': 'Enzymatic-Reaction'},
 'MetaCyc:FAD': {'slots': {'appears-in-left-side-of': 1,
                           'appears-in-right-side-of': 1,
                           'cml': 1,
                           'cofactors-of': 1,
                           'comment': 1,
                           'common-name': 1,
                           'credits': 1,
                           'dblink': 10,
                           'gibbs-0': 1,
                           'inchi': 1,
                           'inchi-key': 1,
                           'molecular-weight': 1,
                           'monoisotopic-mw': 1,
                           'parent': 3,
                           'regulates': 1,
                           'synonym': 3},
                 'tag': 'Compound'},
 'MetaCyc:G1G01-166-MONOMER': {'slots': {'catalyzes': 1,
                                         'citation': 2,
                                         'comment': 1,
                                         'common-name': 1,
                                         'credits': 1,
                                         'dblink': 14,
                                         'gene': 1,
                                         'has-feature': 3,
                                         'has-go-term': 7,
                                         'location': 1,
                                         'molecular-weight-seq': 1,
                                         'parent': 1,
                                         'species': 1,
                                         'synonym': 1},
                               'tag': 'Protein'},
 'MetaCyc:GLUTACONYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                      'appears-in-right-side-of': 1,
                                      'cml': 1,
                                      'common-name': 1,
                                      'dblink': 8,
                                      'gibbs-0': 1,
                                      'inchi': 1,
                                      'inchi-key': 1,
                                      'molecular-weight': 1,
                                      'monoisotopic-mw': 1,
                                      'parent': 1,
                                      'synonym': 4},
                            'tag': 'Compound'},
 'MetaCyc:GLUTACONYL-COA-DECARBOXYLASE-RXN': {'slots': {'dblink': 3,
                                                        'gibbs-0': 1,
                                                        'in-pathway': 1,
                                                        'left': 2,
                                                        'orphan': 1,
                                                        'parent': 2,
                                                        'physiologically-relevant': 1,
                                                        'reaction-direction': 1,
                                                        'right': 2},
                                              'tag': 'Reaction'},
 'MetaCyc:GLUTARYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                    'appears-in-right-side-of': 1,
                                    'cml': 1,
                                    'common-name': 1,
                                    'dblink': 9,
                                    'gibbs-0': 1,
                                    'inchi': 1,
                                    'inchi-key': 1,
                                    'molecular-weight': 1,
                                    'monoisotopic-mw': 1,
                                    'parent': 1,
                                    'regulates': 1,
                                    'synonym': 2},
                          'tag': 'Compound'},
 'MetaCyc:GLUTARYL-COA-DEHYDROG-RXN': {'slots': {'dblink': 3,
                                                 'gibbs-0': 1,
                                                 'in-pathway': 1,
                                                 'left': 3,
                                                 'orphan': 1,
                                                 'parent': 2,
                                                 'physiologically-relevant': 1,
                                                 'reaction-direction': 1,
                                                 'right': 2},
                                       'tag': 'Reaction'},
 'MetaCyc:GLUTARYL-COA-DEHYDROGENASE-RXN': {'slots': {'credits': 1,
                                                      'dblink': 4,
                                                      'ec-number': 1,
                                                      'enzymatic-reaction': 1,
                                                      'gibbs-0': 1,
                                                      'left': 3,
                                                      'orphan': 1,
                                                      'parent': 2,
                                                      'physiologically-relevant': 1,
                                                      'reaction-direction': 1,
                                                      'reaction-list': 1,
                                                      'right': 3},
                                            'tag': 'Reaction'},
 'MetaCyc:IODOACETAMIDE': {'slots': {'cml': 1,
                                     'common-name': 1,
                                     'dblink': 6,
                                     'gibbs-0': 1,
                                     'inchi': 1,
                                     'inchi-key': 1,
                                     'molecular-weight': 1,
                                     'monoisotopic-mw': 1,
                                     'parent': 1,
                                     'regulates': 1,
                                     'synonym': 6},
                           'tag': 'Compound'},
 'MetaCyc:MONOMER-10': {'slots': {'catalyzes': 1,
                                  'comment': 1,
                                  'common-name': 1,
                                  'parent': 1,
                                  'species': 1},
                        'tag': 'Protein'},
 'MetaCyc:MONOMER-11806': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'gene': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-11936': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'dblink': 10,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-12290': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'parent': 1,
                                     'species': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-13086': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'dblink': 17,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-13469': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'credits': 1,
                                     'dblink': 7,
                                     'gene': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-13585': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'credits': 1,
                                     'dblink': 13,
                                     'gene': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-13738': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 14,
                                     'gene': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-13740': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 9,
                                     'gene': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-14626': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'molecular-weight-exp': 1,
                                     'parent': 1,
                                     'species': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-16803': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 15,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 3},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-18244': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 24,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-19851': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 13,
                                     'gene': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-19852': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 12,
                                     'gene': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-20831': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 13,
                                     'gene': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-5381': {'slots': {'common-name': 1,
                                    'component-of': 1,
                                    'gene': 1,
                                    'molecular-weight-exp': 1,
                                    'parent': 1,
                                    'species': 1,
                                    'synonym': 1},
                          'tag': 'Protein'},
 'MetaCyc:PWY-5177': {'slots': {'comment': 1,
                                'common-name': 1,
                                'credits': 1,
                                'evidence': 1,
                                'in-pathway': 1,
                                'parent': 1,
                                'pathway-link': 2,
                                'reaction-layout': 5,
                                'reaction-list': 1,
                                'reaction-ordering': 4,
                                'species': 9,
                                'super-pathways': 1,
                                'taxonomic-range': 1},
                      'tag': 'Pathway'},
 'MetaCyc:RXN-11662': {'slots': {'credits': 1,
                                 'dblink': 3,
                                 'ec-number': 1,
                                 'enzymatic-reaction': 1,
                                 'gibbs-0': 1,
                                 'in-pathway': 1,
                                 'left': 2,
                                 'orphan': 1,
                                 'parent': 2,
                                 'physiologically-relevant': 1,
                                 'reaction-direction': 1,
                                 'right': 3},
                       'tag': 'Reaction'},
 'MetaCyc:RXN-11667': {'slots': {'common-name': 1,
                                 'credits': 1,
                                 'dblink': 3,
                                 'ec-number': 1,
                                 'enzymatic-reaction': 1,
                                 'gibbs-0': 1,
                                 'in-pathway': 1,
                                 'left': 1,
                                 'orphan': 1,
                                 'parent': 2,
                                 'physiologically-relevant': 1,
                                 'reaction-direction': 1,
                                 'right': 2},
                       'tag': 'Reaction'},
 'MetaCyc:S-3-HYDROXYBUTANOYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                               'appears-in-right-side-of': 1,
                                               'cml': 1,
                                               'common-name': 1,
                                               'credits': 1,
                                               'dblink': 8,
                                               'gibbs-0': 1,
                                               'inchi': 1,
                                               'inchi-key': 1,
                                               'molecular-weight': 1,
                                               'monoisotopic-mw': 1,
                                               'parent': 2,
                                               'synonym': 1},
                                     'tag': 'Compound'},
 'MetaCyc:THLCLOS-CPLX': {'slots': {'catalyzes': 1,
                                    'comment': 1,
                                    'common-name': 1,
                                    'component': 1,
                                    'credits': 1,
                                    'parent': 1,
                                    'species': 1,
                                    'synonym': 1},
                          'tag': 'Protein'},
 'MetaCyc:THLCLOS-ENZRXN': {'slots': {'common-name': 1,
                                      'enzyme': 1,
                                      'evidence': 1,
                                      'km': 3,
                                      'physiologically-relevant': 1,
                                      'reaction': 1,
                                      'reaction-direction': 1,
                                      'regulated-by': 1,
                                      'synonym': 2},
                            'tag': 'Enzymatic-Reaction'},
 'MetaCyc:THLCLOS-MONOMER': {'slots': {'common-name': 1,
                                       'component-of': 1,
                                       'credits': 1,
                                       'dblink': 17,
                                       'gene': 1,
                                       'has-go-term': 1,
                                       'location': 1,
                                       'molecular-weight-exp': 1,
                                       'molecular-weight-seq': 1,
                                       'parent': 1,
                                       'species': 1,
                                       'synonym': 1},
                             'tag': 'Protein'},
 'MetaCyc:YPL028W-MONOMER': {'slots': {'common-name': 1,
                                       'component-of': 1,
                                       'dblink': 20,
                                       'gene': 1,
                                       'has-go-term': 1,
                                       'location': 1,
                                       'molecular-weight-seq': 1,
                                       'parent': 1,
                                       'species': 1},
                             'tag': 'Protein'}}
COMPLEXES = {'MetaCyc:ACETYL-COA-ACETYLTRANSFER-CPLX',
 'MetaCyc:CPLX-4041',
 'MetaCyc:CPLX-41',
 'MetaCyc:CPLX-6989',
 'MetaCyc:CPLX-7035',
 'MetaCyc:CPLX-706',
 'MetaCyc:CPLX-7355',
 'MetaCyc:CPLX-7788',
 'MetaCyc:THLCLOS-CPLX'}
NATIVE_MEMBERS = {
    "RXN-11667", "RXN-11662", "ACETYL-COA-ACETYLTRANSFER-RXN",
    "GLUTACONYL-COA-DECARBOXYLASE-RXN", "GLUTARYL-COA-DEHYDROG-RXN",
}
COMPOSITE_MEMBERS = {"GLUTARYL-COA-DEHYDROG-RXN", "GLUTACONYL-COA-DECARBOXYLASE-RXN"}
ETF_CLASSES = {"ETF-Oxidized", "ETF-Reduced"}
NODE_ROLES = {
    "native_glutaryl_compound": ("participants", {"small_molecule", "cofactor"}),
    "native_glutaryl_protein": ("participants", {"protein"}),
    "native_glutaryl_complex": ("participants", {"complex"}),
    "native_glutaryl_activity": ("participants", {"molecular_activity"}),
    "native_glutaryl_reaction": ("reactions", {"molecular_activity"}),
}

def _identity(kind: str) -> tuple[str, str]:
    require(kind in GLUTARYL_KINDS, "unsupported glutaryl kind")
    return "META", "MetaCyc"


def _source_frame(source: dict) -> str:
    """Retain the exact bare request syntax of all 49 acquisition receipts.

    This source kind does not normalize an unacquired id= URL into provenance.
    Earlier typed source request contracts are unchanged.
    """
    keys(source, PROVENANCE, "invalid source provenance fields")
    require(all(isinstance(v, str) and bool(v.strip()) for v in source.values()),
            "empty source provenance")
    match = re.fullmatch(rf"https://{re.escape(HOST)}/getxml\?META:({FRAME})", source["url"])
    require(match is not None, "requires exact acquired native HTTPS META request")
    require(re.fullmatch(r"[0-9a-f]{64}", source["sha256"]) is not None,
            "invalid provenance hash")
    return match[1]


def _envelope(body: bytes, source: dict, kind: str):
    pgdb, prefix = _identity(kind)
    frame = _source_frame(source)
    ident = prefix + ":" + frame
    require(ident in PROFILES, "outside the reviewed glutaryl frame scope")
    require(source["version"] == "27.0", "unsupported glutaryl source release")
    require(hashlib.sha256(body).hexdigest() == source["sha256"], "original hash mismatch")
    root = ET.fromstring(body, parser=ET.XMLParser(target=_TreeBuilder()))
    legacy = f"http://{HOST}:443/"
    require(
        root.tag == "ptools-xml" and len(root) == 2
        and set(root.attrib) == {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        and root.get("ptools-version") == "27.0"
        and root.get("{http://www.w3.org/XML/1998/namespace}base")
        in {source["url"], legacy + "getxml?" + pgdb + ":" + frame},
        "glutaryl envelope mismatch",
    )
    meta = one(root, "metadata")
    entity = next(n for n in root if n.tag != "metadata")
    blank(root)
    blank(meta)
    require(
        not meta.attrib and Counter(n.tag for n in meta)
        == Counter(["url", "service_name", "query", "num_results", "PGDB"]),
        "invalid complete native metadata",
    )
    require(
        scalar(meta, "url") in {legacy, f"https://{HOST}/"}
        and scalar(meta, "service_name") == "getxml"
        and scalar(meta, "query") == pgdb + ":" + frame
        and scalar(meta, "num_results") == "1", "native request identity mismatch",
    )
    db = one(meta, "PGDB")
    blank(db)
    require(db.attrib == {"orgid": pgdb, "version": "27.0"}, "PGDB identity mismatch")
    require(
        Counter(n.tag for n in db)
        == Counter(["species"]),
        "incomplete native PGDB context",
    )
    require(
        scalar(db, "species", True) == "MetaCyc",
        "wrong native database species",
    )
    attributes(entity, frame, pgdb, PROFILES[ident]["tag"], False)
    require(Counter(n.tag for n in entity) == PROFILES[ident]["slots"],
            "incomplete or unsupported complete native slots")
    # Check every embedded native identity while retaining uninterpreted context.
    # Embedded annotations do not become selected taxa, enzymes or chemical aliases.
    for node in entity.iter():
        if (node.tag not in _NATIVE_OBJECT_TAGS
                and not _NATIVE_IDENTITY_ATTRIBUTES.intersection(node.attrib)):
            continue
        require(
            bool(node.get("frameid")) and bool(node.get("orgid"))
            and (("ID" in node.attrib) != ("resource" in node.attrib)),
            "incomplete or ambiguous embedded native identity",
        )
        native = node.get("orgid", "") + ":" + node.get("frameid", "")
        require(node.get("orgid") == pgdb and bool(node.get("frameid")),
                "embedded native database identity mismatch")
        if "ID" in node.attrib:
            require(node.get("ID") == native, "embedded native ID/frame mismatch")
        if "resource" in node.attrib:
            require(node.get("resource") in {"getxml?" + native, "#" + native},
                    "embedded native resource/frame mismatch")
    return root, entity, ident


def _side(entity: ET.Element, side: str, pgdb: str) -> list[dict]:
    result = []
    for wrapper in entity.findall(side):
        blank(wrapper)
        materials = [n for n in wrapper if n.tag != "coefficient"]
        require(not wrapper.attrib and len(materials) == 1
                and Counter(n.tag for n in wrapper) in (
                    Counter({materials[0].tag: 1}),
                    Counter({materials[0].tag: 1, "coefficient": 1}),
                ), "invalid reaction material occurrence")
        node = materials[0]
        is_etf = node.get("frameid") in ETF_CLASSES
        require(node.tag == ("Protein" if is_etf else "Compound"),
                "reaction material must preserve native chemical or ETF class identity")
        material = ref_node(node, pgdb, node.tag, is_class=is_etf)
        coeff = wrapper.find("coefficient")
        result.append({"material": material["id"], "native_type": node.tag,
                       "is_class": is_etf,
                       "coefficient": integer(coeff) if coeff is not None else None})
    require(bool(result) and len({r["material"] for r in result}) == len(result),
            "empty or duplicate reaction side")
    return result


def _projection(entity: ET.Element, ident: str) -> dict:
    frame = entity.get("frameid")
    pgdb, prefix = ("META", "MetaCyc") if ident.startswith("MetaCyc:") else ("ECOLI", "EcoCyc")
    common = entity.findall("common-name")
    require(len(common) <= 1, "duplicate common name")
    label = name(common[0], "") if common else frame
    aliases = sorted({name(n, "") for n in entity.findall("synonym")} - {label})
    result = {
        "id": ident, "native_type": entity.tag, "is_class": False,
        "label": label, "synonyms": aliases,
        "label_origin": "direct_common_name" if common else "native_frame_id",
        "slots": [{"ordinal": i, "name": n.tag, "xml": ET.tostring(n, encoding="unicode")}
                  for i, n in enumerate(entity, 1)],
    }
    if entity.tag == "Reaction":
        result["sides"] = {side: _side(entity, side, pgdb) for side in ("left", "right")}
        direction = scalar(entity, "reaction-direction")
        require(direction in {"REVERSIBLE", "PHYSIOL-LEFT-TO-RIGHT", "PHYSIOL-RIGHT-TO-LEFT"},
                "invalid native reaction direction")
        result["reaction_direction"] = direction
        if ident == "MetaCyc:GLUTARYL-COA-DEHYDROGENASE-RXN":
            listing = one(entity, "reaction-list")
            blank(listing)
            require(not listing.attrib, "attributed native composite list")
            members = [ref_node(n, pgdb, "Reaction")["id"] for n in listing]
            require(len(members) == 2
                    and set(members) == {"MetaCyc:" + f for f in COMPOSITE_MEMBERS},
                    "wrong complete native composite membership")
            result["reaction_list"] = members
    if entity.tag == "Enzymatic-Reaction":
        for slot, tag in (("enzyme", "Protein"), ("reaction", "Reaction")):
            wrapper = one(entity, slot)
            blank(wrapper)
            require(not wrapper.attrib and len(wrapper) == 1, "invalid native activity link")
            result[slot] = ref_node(wrapper[0], pgdb, tag)["id"]
    if ident in COMPLEXES:
        components = []
        for wrapper in entity.findall("component"):
            blank(wrapper)
            require(not wrapper.attrib and Counter(n.tag for n in wrapper)
                    in (Counter({"Protein": 1}), Counter({"Protein": 1, "coefficient": 1})),
                    "invalid native complex component")
            component = ref_node(one(wrapper, "Protein"), pgdb, "Protein")["id"]
            coeff = wrapper.find("coefficient")
            components.append({"id": component,
                               "coefficient": integer(coeff) if coeff is not None else None})
        require(bool(components) and len({r["id"] for r in components}) == len(components),
                "empty or duplicate native complex components")
        result["components"] = components
    if entity.tag == "Pathway":
        listing = one(entity, "reaction-list")
        blank(listing)
        require(not listing.attrib, "attributed native reaction list")
        members = [ref_node(n, pgdb, "Reaction")["id"] for n in listing]
        require(len(members) == 5 and set(members) == {prefix + ":" + f for f in NATIVE_MEMBERS},
                "wrong complete PWY-5177 native membership")
        result["reaction_list"] = members
    return result


def document(body: bytes, source: dict, kind: str) -> dict:
    root, entity, ident = _envelope(body, source, kind)
    return {
        "id": ident, "original_base64": base64.b64encode(body).decode("ascii"),
        "root_attributes": dict(root.attrib),
        "metadata_xml": ET.tostring(one(root, "metadata"), encoding="unicode"),
        "projection": _projection(entity, ident),
    }


def glutaryl_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(entry, PROVENANCE | {"key", "kind", "path"}, "invalid glutaryl manifest")
    require(isinstance(entry["key"], str) and bool(entry["key"].strip()), "empty source key")
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    result = {**source, "kind": entry["kind"],
              FIELD: document(original_path(entry, cache_dir).read_bytes(), source, entry["kind"])}
    validate_glutaryl_metadata(result)
    return result


def validate_glutaryl_metadata(metadata: dict) -> None:
    keys(metadata, PROVENANCE | {"kind", FIELD}, "invalid glutaryl metadata")
    source = {k: metadata[k] for k in PROVENANCE_ORDER}
    native = metadata[FIELD]
    keys(native, {"id", "original_base64", "root_attributes", "metadata_xml", "projection"},
         "incomplete original glutaryl document")
    expected = document(original_bytes(native["original_base64"]), source, metadata["kind"])
    require(json.dumps(native, sort_keys=True) == json.dumps(expected, sort_keys=True),
            "glutaryl projection does not match original bytes")


def glutaryl_term(metadata: dict, source_key: str) -> tuple[str, dict]:
    validate_glutaryl_metadata(metadata)
    native = metadata[FIELD]["projection"]
    tag, ident = native["native_type"], native["id"]
    role = {
        "Compound": "compound", "Protein": "complex" if ident in COMPLEXES else "protein",
        "Enzymatic-Reaction": "activity", "Reaction": "reaction",
        "Pathway": "pathway",
    }[tag]
    return ident, {
        "label": native["label"], "synonyms": native["synonyms"], "source": source_key,
        "entity_type": "native_pathway" if role == "pathway" else "native_glutaryl_" + role,
        "label_kind": "canonical" if native["label_origin"] == "direct_common_name"
                      else "source_context",
    }


def validate_glutaryl_assertions(sources: dict, claims: list[tuple[str, str]]) -> None:
    """Reject downgrades/conflicting original owners before selection and on load."""
    assertions = {}
    for metadata in sources.values():
        kind = metadata.get("kind")
        if kind in GLUTARYL_KINDS:
            validate_glutaryl_metadata(metadata)
            native = metadata[FIELD]
            ident = native["id"]
            assertion = json.dumps(native, sort_keys=True), metadata["version"], kind
            if ident in assertions:
                require(assertions[ident] == assertion, "conflicting complete native identity")
            assertions[ident] = assertion
        elif FIELD in metadata:
            raise ValueError("glutaryl metadata requires its exact typed kind")
        url = urlsplit(metadata.get("url", ""))
        if url.hostname in {HOST, "biocyc.org", "www.biocyc.org", "metacyc.org", "www.metacyc.org"}:
            params = parse_qs(url.query)
            tokens = [v for name in ("id", "object") for v in params.get(name, [])]
            # Native receipts also use /getxml?META:FRAME (or ECOLI:FRAME).
            # Treat only the complete literal query on that HTTP(S) endpoint as
            # a bare request token. The exact profile lookup below must not turn
            # arbitrary query values, suffixes or unrelated paths into identities.
            if (url.scheme in {"http", "https"} and url.path == "/getxml"
                    and url.query.startswith(("META:", "ECOLI:"))):
                tokens.append(url.query)
            for token in tokens:
                if token.startswith("META:"):
                    ident = "MetaCyc:" + token[5:]
                elif token.startswith("ECOLI:"):
                    ident = "EcoCyc:" + token[6:]
                else:
                    prefix = "EcoCyc" if "/ECOLI/" in url.path.upper() else "MetaCyc"
                    ident = prefix + ":" + token
                if ident in PROFILES:
                    expected = KIND
                    require(kind == expected, "complete native identity requires its typed source")
    for ident, source in claims:
        if ident in PROFILES:
            metadata = sources[source]
            expected = KIND
            require(metadata.get("kind") == expected and metadata[FIELD]["id"] == ident,
                    "claimed native identity requires its complete typed owner")
