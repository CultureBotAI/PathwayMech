"""Bounded complete-original identities for PWY0-321 and reviewed Paa contexts.

All names come from the issuing XML. The frame/type/slot profiles constrain the
reviewed source scope; they are not curated-label authority. Original bytes,
request, PGDB, release, every source slot and derived term are replayed by both
producer and consumer. Native net equations do not identify isolated catalysts.
Existing authority owners and the separate P321 profile are not reinterpreted.
"""

from __future__ import annotations

import base64
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import (
    HOST,
    PROVENANCE,
    PROVENANCE_ORDER,
    _TreeBuilder,
    keys,
    name,
    one,
    original_path,
    provenance,
    require,
    scalar,
)
from pathwaymech.biocyc_native_context import attributes, blank, integer, ref_node
from pathwaymech.biocyc_p321 import original_bytes

META_KIND = "metacyc-phenylacetate-xml"
ECO_KIND = "ecocyc-phenylacetate-xml"
PHENYLACETATE_KINDS = {META_KIND, ECO_KIND}
FIELD = "native_phenylacetate"
# Native object tags observed in the 65 complete originals. Recognize the tag
# even when an altered object has lost every identity attribute. CML elements
# and scalar slots are not native objects; unfamiliar context carrying native
# identity attributes must still pass the same complete-identity checks.
_NATIVE_OBJECT_TAGS = {
    "Compound", "Evidence-Code", "Publication", "Reaction", "Regulation",
    "Enzymatic-Reaction", "Protein", "Person", "Organization", "Gene",
    "Organism", "Feature", "GO-Term", "cco", "Pathway", "Genetic-Element",
    "Promoter", "Transcription-Unit", "DNA-Binding-Site",
}
_NATIVE_IDENTITY_ATTRIBUTES = {"frameid", "orgid", "ID", "resource"}
# Complete direct-slot multiplicities of the independently reviewed originals.
# Slot XML and derived names are read from the bytes, never supplied here.
PROFILES = {'EcoCyc:ENZRXN0-7862': {'slots': {'common-name': 1,
                                   'enzyme': 1,
                                   'evidence': 2,
                                   'kcat': 1,
                                   'km': 1,
                                   'physiologically-relevant': 1,
                                   'reaction': 1},
                         'tag': 'Enzymatic-Reaction'},
 'EcoCyc:G6717-MONOMER': {'slots': {'comment': 1,
                                    'common-name': 1,
                                    'component-of': 1,
                                    'credits': 1,
                                    'dblink': 16,
                                    'gene': 1,
                                    'has-feature': 6,
                                    'has-go-term': 5,
                                    'location': 1,
                                    'molecular-weight-exp': 1,
                                    'molecular-weight-seq': 1,
                                    'parent': 1,
                                    'species': 1,
                                    'synonym': 2},
                          'tag': 'Protein'},
 'EcoCyc:G6720-MONOMER': {'slots': {'abbrev-name': 1,
                                    'appears-in-left-side-of': 1,
                                    'citation': 2,
                                    'common-name': 1,
                                    'component-of': 1,
                                    'dblink': 13,
                                    'dna-footprint-size': 1,
                                    'gene': 1,
                                    'has-feature': 5,
                                    'has-go-term': 7,
                                    'location': 1,
                                    'molecular-weight-seq': 1,
                                    'parent': 1,
                                    'species': 1,
                                    'symmetry': 1,
                                    'synonym': 2},
                          'tag': 'Protein'},
 'EcoCyc:G6721-MONOMER': {'slots': {'common-name': 1,
                                    'component-of': 1,
                                    'credits': 1,
                                    'dblink': 12,
                                    'gene': 1,
                                    'has-feature': 4,
                                    'has-go-term': 4,
                                    'location': 1,
                                    'molecular-weight-seq': 1,
                                    'parent': 1,
                                    'species': 1,
                                    'synonym': 2},
                          'tag': 'Protein'},
 'EcoCyc:PM4': {'slots': {'absolute-plus-1-pos': 1,
                          'citation': 1,
                          'common-name': 1,
                          'component-of': 1,
                          'evidence': 2,
                          'minus-10-left': 1,
                          'minus-10-right': 1,
                          'regulated-by': 1,
                          'replicon': 1,
                          'synonym': 2,
                          'transcription-direction': 1},
                'tag': 'Promoter'},
 'EcoCyc:PM5': {'slots': {'absolute-plus-1-pos': 1,
                          'binds-sigma-factor': 1,
                          'citation': 1,
                          'common-name': 1,
                          'component-of': 1,
                          'evidence': 3,
                          'minus-10-left': 1,
                          'minus-10-right': 1,
                          'minus-35-left': 1,
                          'minus-35-right': 1,
                          'regulated-by': 1,
                          'replicon': 1,
                          'synonym': 1,
                          'transcription-direction': 1},
                'tag': 'Promoter'},
 'EcoCyc:TU5': {'slots': {'citation': 1,
                          'comment': 1,
                          'common-name': 1,
                          'component': 15,
                          'evidence': 4,
                          'regulated-by': 1,
                          'replicon': 1},
                'tag': 'Transcription-Unit'},
 'MetaCyc:3-HYDROXYADIPYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                           'citation': 1,
                                           'cml': 1,
                                           'common-name': 1,
                                           'dblink': 6,
                                           'gibbs-0': 1,
                                           'inchi': 1,
                                           'inchi-key': 1,
                                           'molecular-weight': 1,
                                           'monoisotopic-mw': 1,
                                           'parent': 1},
                                 'tag': 'Compound'},
 'MetaCyc:3-KETO-ADIPYL-COA': {'slots': {'appears-in-right-side-of': 1,
                                         'cml': 1,
                                         'common-name': 1,
                                         'dblink': 7,
                                         'gibbs-0': 1,
                                         'inchi': 1,
                                         'inchi-key': 1,
                                         'molecular-weight': 1,
                                         'monoisotopic-mw': 1,
                                         'parent': 2,
                                         'synonym': 4},
                               'tag': 'Compound'},
 'MetaCyc:ACETYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                  'appears-in-right-side-of': 1,
                                  'cml': 1,
                                  'common-name': 1,
                                  'dblink': 12,
                                  'gibbs-0': 1,
                                  'inchi': 1,
                                  'inchi-key': 1,
                                  'molecular-weight': 1,
                                  'monoisotopic-mw': 1,
                                  'parent': 2,
                                  'regulates': 1,
                                  'synonym': 5},
                        'tag': 'Compound'},
 'MetaCyc:AMP': {'slots': {'appears-in-left-side-of': 1,
                           'appears-in-right-side-of': 1,
                           'cml': 1,
                           'cofactors-of': 1,
                           'common-name': 1,
                           'dblink': 11,
                           'gibbs-0': 1,
                           'inchi': 1,
                           'inchi-key': 1,
                           'molecular-weight': 1,
                           'monoisotopic-mw': 1,
                           'parent': 1,
                           'regulates': 1,
                           'synonym': 9},
                 'tag': 'Compound'},
 'MetaCyc:ATP': {'slots': {'appears-in-left-side-of': 1,
                           'appears-in-right-side-of': 1,
                           'cml': 1,
                           'cofactors-of': 1,
                           'common-name': 1,
                           'component-of': 1,
                           'dblink': 13,
                           'gibbs-0': 1,
                           'inchi': 1,
                           'inchi-key': 1,
                           'molecular-weight': 1,
                           'monoisotopic-mw': 1,
                           'parent': 1,
                           'regulates': 1,
                           'synonym': 3},
                 'tag': 'Compound'},
 'MetaCyc:CIS-34-DEHYDROADIPYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                                'appears-in-right-side-of': 1,
                                                'cml': 1,
                                                'common-name': 1,
                                                'dblink': 5,
                                                'gibbs-0': 1,
                                                'inchi': 1,
                                                'inchi-key': 1,
                                                'molecular-weight': 1,
                                                'monoisotopic-mw': 1},
                                      'tag': 'Compound'},
 'MetaCyc:CO-A': {'slots': {'appears-in-left-side-of': 1,
                            'appears-in-right-side-of': 1,
                            'cml': 1,
                            'comment': 1,
                            'common-name': 1,
                            'dblink': 11,
                            'gibbs-0': 1,
                            'inchi': 1,
                            'inchi-key': 1,
                            'molecular-weight': 1,
                            'monoisotopic-mw': 1,
                            'parent': 1,
                            'regulates': 1,
                            'synonym': 3},
                  'tag': 'Compound'},
 'MetaCyc:CPD-207': {'slots': {'appears-in-left-side-of': 1,
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
                               'synonym': 1},
                     'tag': 'Compound'},
 'MetaCyc:CPD0-2362': {'slots': {'appears-in-left-side-of': 1,
                                 'appears-in-right-side-of': 1,
                                 'cml': 1,
                                 'common-name': 1,
                                 'credits': 1,
                                 'dblink': 5,
                                 'gibbs-0': 1,
                                 'inchi': 1,
                                 'inchi-key': 1,
                                 'molecular-weight': 1,
                                 'monoisotopic-mw': 1,
                                 'synonym': 1},
                       'tag': 'Compound'},
 'MetaCyc:CPD0-2363': {'slots': {'appears-in-left-side-of': 1,
                                 'appears-in-right-side-of': 1,
                                 'cml': 1,
                                 'common-name': 1,
                                 'credits': 1,
                                 'dblink': 5,
                                 'gibbs-0': 1,
                                 'inchi': 1,
                                 'inchi-key': 1,
                                 'molecular-weight': 1,
                                 'monoisotopic-mw': 1,
                                 'synonym': 1},
                       'tag': 'Compound'},
 'MetaCyc:CPD0-2364': {'slots': {'appears-in-right-side-of': 1,
                                 'cml': 1,
                                 'common-name': 1,
                                 'credits': 1,
                                 'dblink': 5,
                                 'gibbs-0': 1,
                                 'inchi': 1,
                                 'inchi-key': 1,
                                 'molecular-weight': 1,
                                 'monoisotopic-mw': 1,
                                 'synonym': 1},
                       'tag': 'Compound'},
 'MetaCyc:CPD0-2558': {'slots': {'appears-in-left-side-of': 1,
                                 'appears-in-right-side-of': 1,
                                 'citation': 1,
                                 'cml': 1,
                                 'common-name': 1,
                                 'credits': 1,
                                 'dblink': 2,
                                 'gibbs-0': 1,
                                 'inchi': 1,
                                 'inchi-key': 1,
                                 'molecular-weight': 1,
                                 'monoisotopic-mw': 1,
                                 'regulates': 1},
                       'tag': 'Compound'},
 'MetaCyc:CPD0-2559': {'slots': {'appears-in-right-side-of': 1,
                                 'cml': 1,
                                 'common-name': 1,
                                 'credits': 1,
                                 'dblink': 2,
                                 'gibbs-0': 1,
                                 'inchi': 1,
                                 'inchi-key': 1,
                                 'molecular-weight': 1,
                                 'monoisotopic-mw': 1},
                       'tag': 'Compound'},
 'MetaCyc:CPDMETA-13650': {'slots': {'appears-in-left-side-of': 1,
                                     'appears-in-right-side-of': 1,
                                     'citation': 1,
                                     'cml': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 4,
                                     'gibbs-0': 1,
                                     'inchi': 1,
                                     'inchi-key': 1,
                                     'molecular-weight': 1,
                                     'monoisotopic-mw': 1,
                                     'synonym': 1},
                           'tag': 'Compound'},
 'MetaCyc:CPLX-8168': {'slots': {'catalyzes': 1,
                                 'comment': 1,
                                 'common-name': 1,
                                 'component': 4,
                                 'credits': 1,
                                 'parent': 1,
                                 'species': 1},
                       'tag': 'Protein'},
 'MetaCyc:CPLX0-1762': {'slots': {'catalyzes': 1,
                                  'comment': 1,
                                  'common-name': 1,
                                  'component': 4,
                                  'credits': 1,
                                  'has-go-term': 2,
                                  'parent': 1,
                                  'species': 1},
                        'tag': 'Protein'},
 'MetaCyc:CPLX0-8538': {'slots': {'catalyzes': 1,
                                  'citation': 1,
                                  'comment': 1,
                                  'component': 1,
                                  'credits': 1,
                                  'parent': 1,
                                  'species': 1},
                        'tag': 'Protein'},
 'MetaCyc:ENZRXN-12716': {'slots': {'comment': 1,
                                    'common-name': 1,
                                    'enzyme': 1,
                                    'evidence': 1,
                                    'km': 3,
                                    'ph-opt': 1,
                                    'physiologically-relevant': 1,
                                    'reaction': 1,
                                    'regulated-by': 1,
                                    'synonym': 1,
                                    'temperature-opt': 1},
                          'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXN-18271': {'slots': {'common-name': 1,
                                    'enzyme': 1,
                                    'evidence': 1,
                                    'physiologically-relevant': 1,
                                    'reaction': 1,
                                    'synonym': 1},
                          'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXN-18272': {'slots': {'common-name': 1,
                                    'enzyme': 1,
                                    'evidence': 1,
                                    'physiologically-relevant': 1,
                                    'reaction': 1,
                                    'reaction-direction': 1,
                                    'synonym': 1},
                          'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXN-18273': {'slots': {'common-name': 1,
                                    'enzyme': 1,
                                    'evidence': 1,
                                    'physiologically-relevant': 1,
                                    'reaction': 1},
                          'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXN-18275': {'slots': {'common-name': 1,
                                    'enzyme': 1,
                                    'evidence': 1,
                                    'physiologically-relevant': 1,
                                    'reaction': 1,
                                    'reaction-direction': 1},
                          'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXN0-2601': {'slots': {'cofactor': 2,
                                    'common-name': 1,
                                    'credits': 1,
                                    'enzyme': 1,
                                    'evidence': 2,
                                    'physiologically-relevant': 1,
                                    'reaction': 1,
                                    'reaction-direction': 1,
                                    'synonym': 2},
                          'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXN0-2606': {'slots': {'common-name': 1,
                                    'credits': 1,
                                    'enzyme': 1,
                                    'evidence': 1,
                                    'physiologically-relevant': 1,
                                    'reaction': 1,
                                    'reaction-direction': 1},
                          'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXNMETA-19626': {'slots': {'common-name': 1,
                                        'credits': 1,
                                        'enzyme': 1,
                                        'evidence': 2,
                                        'km': 1,
                                        'ph-opt': 1,
                                        'physiologically-relevant': 1,
                                        'reaction': 1,
                                        'reaction-direction': 1,
                                        'regulated-by': 1},
                              'tag': 'Enzymatic-Reaction'},
 'MetaCyc:ENZRXNMETA-19627': {'slots': {'alternative-substrate': 1,
                                        'comment': 1,
                                        'common-name': 1,
                                        'credits': 1,
                                        'enzyme': 1,
                                        'evidence': 2,
                                        'km': 1,
                                        'ph-opt': 1,
                                        'physiologically-relevant': 1,
                                        'reaction': 1},
                              'tag': 'Enzymatic-Reaction'},
 'MetaCyc:G6708-MONOMER': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 23,
                                     'gene': 1,
                                     'has-feature': 11,
                                     'has-go-term': 13,
                                     'location': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 4},
                           'tag': 'Protein'},
 'MetaCyc:G6709-MONOMER': {'slots': {'comment': 1,
                                     'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 20,
                                     'gene': 1,
                                     'has-feature': 10,
                                     'has-go-term': 6,
                                     'location': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 2},
                           'tag': 'Protein'},
 'MetaCyc:G6710-MONOMER': {'slots': {'comment': 1,
                                     'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 10,
                                     'gene': 1,
                                     'has-feature': 1,
                                     'has-go-term': 4,
                                     'location': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 2},
                           'tag': 'Protein'},
 'MetaCyc:G6711-MONOMER': {'slots': {'comment': 1,
                                     'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 21,
                                     'gene': 1,
                                     'has-feature': 4,
                                     'has-go-term': 4,
                                     'location': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 2},
                           'tag': 'Protein'},
 'MetaCyc:G6713-MONOMER': {'slots': {'comment': 1,
                                     'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 25,
                                     'gene': 1,
                                     'has-feature': 13,
                                     'has-go-term': 8,
                                     'location': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 2},
                           'tag': 'Protein'},
 'MetaCyc:G6716-MONOMER': {'slots': {'catalyzes': 1,
                                     'citation': 1,
                                     'comment': 1,
                                     'credits': 1,
                                     'dblink': 19,
                                     'gene': 1,
                                     'has-feature': 6,
                                     'has-go-term': 11,
                                     'location': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 4},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-12132': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 9,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'pi': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-15947': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 6,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-15948': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 4,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-15949': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 6,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-15950': {'slots': {'common-name': 1,
                                     'component-of': 1,
                                     'credits': 1,
                                     'dblink': 20,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-15951': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 6,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:MONOMER-15953': {'slots': {'catalyzes': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 7,
                                     'gene': 1,
                                     'molecular-weight-exp': 1,
                                     'molecular-weight-seq': 1,
                                     'parent': 1,
                                     'species': 1,
                                     'synonym': 1},
                           'tag': 'Protein'},
 'MetaCyc:NADH': {'slots': {'appears-in-left-side-of': 1,
                            'appears-in-right-side-of': 1,
                            'cml': 1,
                            'cofactors-of': 1,
                            'comment': 1,
                            'common-name': 1,
                            'dblink': 11,
                            'gibbs-0': 1,
                            'inchi': 1,
                            'inchi-key': 1,
                            'molecular-weight': 1,
                            'monoisotopic-mw': 1,
                            'parent': 1,
                            'regulates': 1,
                            'synonym': 11},
                  'tag': 'Compound'},
 'MetaCyc:NADP': {'slots': {'appears-in-left-side-of': 1,
                            'appears-in-right-side-of': 1,
                            'cml': 1,
                            'cofactors-of': 1,
                            'comment': 1,
                            'common-name': 1,
                            'dblink': 11,
                            'gibbs-0': 1,
                            'inchi': 1,
                            'inchi-key': 1,
                            'molecular-weight': 1,
                            'monoisotopic-mw': 1,
                            'parent': 1,
                            'regulates': 1,
                            'synonym': 12},
                  'tag': 'Compound'},
 'MetaCyc:NADPH': {'slots': {'appears-in-left-side-of': 1,
                             'appears-in-right-side-of': 1,
                             'cml': 1,
                             'cofactors-of': 1,
                             'comment': 1,
                             'common-name': 1,
                             'dblink': 11,
                             'gibbs-0': 1,
                             'inchi': 1,
                             'inchi-key': 1,
                             'molecular-weight': 1,
                             'monoisotopic-mw': 1,
                             'parent': 1,
                             'regulates': 1,
                             'synonym': 13},
                   'tag': 'Compound'},
 'MetaCyc:OXYGEN-MOLECULE': {'slots': {'abbrev-name': 1,
                                       'appears-in-left-side-of': 1,
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
                                       'synonym': 3,
                                       'systematic-name': 1},
                             'tag': 'Compound'},
 'MetaCyc:PHENYLACETATE': {'slots': {'appears-in-left-side-of': 1,
                                     'appears-in-right-side-of': 1,
                                     'cml': 1,
                                     'comment': 1,
                                     'common-name': 1,
                                     'credits': 1,
                                     'dblink': 10,
                                     'gibbs-0': 1,
                                     'inchi': 1,
                                     'inchi-key': 1,
                                     'molecular-weight': 1,
                                     'monoisotopic-mw': 1,
                                     'parent': 4,
                                     'synonym': 3},
                           'tag': 'Compound'},
 'MetaCyc:PWY0-321': {'slots': {'comment': 1,
                                'common-name': 1,
                                'credits': 1,
                                'dblink': 1,
                                'evidence': 1,
                                'in-pathway': 1,
                                'parent': 1,
                                'pathway-link': 2,
                                'reaction-layout': 9,
                                'reaction-list': 1,
                                'reaction-ordering': 8,
                                'species': 6,
                                'super-pathways': 1,
                                'taxonomic-range': 1},
                      'tag': 'Pathway'},
 'MetaCyc:RXN-10819': {'slots': {'credits': 1,
                                 'dblink': 3,
                                 'ec-number': 1,
                                 'enzymatic-reaction': 1,
                                 'gibbs-0': 1,
                                 'in-pathway': 1,
                                 'left': 3,
                                 'orphan': 1,
                                 'parent': 2,
                                 'physiologically-relevant': 1,
                                 'reaction-direction': 1,
                                 'right': 3},
                       'tag': 'Reaction'},
 'MetaCyc:RXN-17752': {'slots': {'citation': 1,
                                 'credits': 1,
                                 'dblink': 1,
                                 'gibbs-0': 1,
                                 'left': 1,
                                 'orphan': 1,
                                 'parent': 2,
                                 'physiologically-relevant': 1,
                                 'reaction-direction': 1,
                                 'right': 2,
                                 'spontaneous': 1},
                       'tag': 'Reaction'},
 'MetaCyc:RXN-2425': {'slots': {'credits': 1,
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
 'MetaCyc:RXN-3641': {'slots': {'dblink': 3,
                                'ec-number': 1,
                                'enzymatic-reaction': 1,
                                'gibbs-0': 1,
                                'in-pathway': 1,
                                'left': 2,
                                'orphan': 1,
                                'parent': 2,
                                'physiologically-relevant': 1,
                                'reaction-direction': 1,
                                'right': 2},
                      'tag': 'Reaction'},
 'MetaCyc:RXN0-2042': {'slots': {'credits': 1,
                                 'dblink': 3,
                                 'ec-number': 1,
                                 'enzymatic-reaction': 1,
                                 'gibbs-0': 1,
                                 'in-pathway': 1,
                                 'left': 4,
                                 'orphan': 1,
                                 'parent': 2,
                                 'physiologically-relevant': 1,
                                 'reaction-direction': 1,
                                 'right': 3},
                       'tag': 'Reaction'},
 'MetaCyc:RXN0-2044': {'slots': {'citation': 1,
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
 'MetaCyc:RXN0-6510': {'slots': {'credits': 1,
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
                                 'right': 1},
                       'tag': 'Reaction'},
 'MetaCyc:RXN0-6512': {'slots': {'citation': 1,
                                 'credits': 1,
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
                                 'right': 2},
                       'tag': 'Reaction'},
 'MetaCyc:RXN0-7103': {'slots': {'credits': 1,
                                 'dblink': 1,
                                 'ec-number': 1,
                                 'enzymatic-reaction': 1,
                                 'gibbs-0': 1,
                                 'left': 2,
                                 'orphan': 1,
                                 'parent': 2,
                                 'physiologically-relevant': 1,
                                 'reaction-direction': 1,
                                 'right': 3},
                       'tag': 'Reaction'},
 'MetaCyc:RXNMETA-12671': {'slots': {'credits': 1,
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
                                     'right': 1},
                           'tag': 'Reaction'},
 'MetaCyc:RXNMETA-12672': {'slots': {'credits': 1,
                                     'dblink': 3,
                                     'ec-number': 1,
                                     'enzymatic-reaction': 1,
                                     'gibbs-0': 1,
                                     'in-pathway': 1,
                                     'left': 3,
                                     'orphan': 1,
                                     'parent': 2,
                                     'physiologically-relevant': 1,
                                     'reaction-direction': 1,
                                     'right': 3},
                           'tag': 'Reaction'},
 'MetaCyc:SUC-COA': {'slots': {'abbrev-name': 1,
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
                               'synonym': 9,
                               'systematic-name': 1},
                     'tag': 'Compound'},
 'MetaCyc:TRANS-23-DEHYDROADIPYL-COA': {'slots': {'appears-in-left-side-of': 1,
                                                  'appears-in-right-side-of': 1,
                                                  'cml': 1,
                                                  'common-name': 1,
                                                  'dblink': 5,
                                                  'gibbs-0': 1,
                                                  'inchi': 1,
                                                  'inchi-key': 1,
                                                  'molecular-weight': 1,
                                                  'monoisotopic-mw': 1,
                                                  'synonym': 3},
                                        'tag': 'Compound'}}

COMPLEXES = {"MetaCyc:CPLX-8168", "MetaCyc:CPLX0-1762", "MetaCyc:CPLX0-8538"}
NATIVE_MEMBERS = {
    "RXN-10819", "RXN0-2042", "RXN0-6510", "RXNMETA-12671", "RXNMETA-12672",
    "RXN0-6512", "RXN-2425", "RXN0-2044", "RXN-3641",
}
NODE_ROLES = {
    "native_phenylacetate_compound": ("participants", {"small_molecule", "cofactor"}),
    "native_phenylacetate_protein": ("participants", {"protein"}),
    "native_phenylacetate_complex": ("participants", {"complex"}),
    "native_phenylacetate_activity": ("participants", {"molecular_activity"}),
    "native_phenylacetate_dna": ("participants", {"dna"}),
    "native_phenylacetate_reaction": ("reactions", {"molecular_activity"}),
}


def _identity(kind: str) -> tuple[str, str]:
    require(kind in PHENYLACETATE_KINDS, "unsupported phenylacetate kind")
    return ("META", "MetaCyc") if kind == META_KIND else ("ECOLI", "EcoCyc")


def _envelope(body: bytes, source: dict, kind: str):
    pgdb, prefix = _identity(kind)
    frame = provenance(source, pgdb)
    ident = prefix + ":" + frame
    require(ident in PROFILES, "outside the reviewed phenylacetate frame scope")
    require(source["version"] == "27.0", "unsupported phenylacetate source release")
    require(hashlib.sha256(body).hexdigest() == source["sha256"], "original hash mismatch")
    root = ET.fromstring(body, parser=ET.XMLParser(target=_TreeBuilder()))
    legacy = f"http://{HOST}:443/"
    require(
        root.tag == "ptools-xml" and len(root) == 2
        and set(root.attrib) == {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        and root.get("ptools-version") == "27.0"
        and root.get("{http://www.w3.org/XML/1998/namespace}base")
        in {source["url"], legacy + "getxml?" + pgdb + ":" + frame},
        "phenylacetate envelope mismatch",
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
        == Counter(["species"] if pgdb == "META" else ["species", "strain", "dblink"]),
        "incomplete native PGDB context",
    )
    require(
        scalar(db, "species", True) == ("MetaCyc" if pgdb == "META" else "Escherichia coli"),
        "wrong native database species",
    )
    if pgdb == "ECOLI":
        require(scalar(db, "strain", True) == "K-12 substr. MG1655", "wrong ECOLI database strain")
        link = one(db, "dblink")
        blank(link)
        wanted = {
            "dblink-db": "NCBI-TAXONOMY-DB", "dblink-oid": "511145",
            "dblink-relationship": "unification",
            "dblink-URL": "http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=511145",
        }
        require(not link.attrib and Counter(n.tag for n in link) == Counter(wanted.keys()),
                "invalid ECOLI database taxon link")
        require(all(scalar(link, k) == v for k, v in wanted.items()), "wrong ECOLI taxon identity")
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
        require(not wrapper.attrib and Counter(n.tag for n in wrapper)
                in (Counter({"Compound": 1}), Counter({"Compound": 1, "coefficient": 1})),
                "invalid reaction material occurrence")
        material = ref_node(one(wrapper, "Compound"), pgdb, "Compound")
        coeff = wrapper.find("coefficient")
        result.append({"material": material["id"],
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
        require(len(members) == 9 and set(members) == {prefix + ":" + f for f in NATIVE_MEMBERS},
                "wrong complete PWY0-321 native membership")
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


def phenylacetate_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(entry, PROVENANCE | {"key", "kind", "path"}, "invalid phenylacetate manifest")
    require(isinstance(entry["key"], str) and bool(entry["key"].strip()), "empty source key")
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    result = {**source, "kind": entry["kind"],
              FIELD: document(original_path(entry, cache_dir).read_bytes(), source, entry["kind"])}
    validate_phenylacetate_metadata(result)
    return result


def validate_phenylacetate_metadata(metadata: dict) -> None:
    keys(metadata, PROVENANCE | {"kind", FIELD}, "invalid phenylacetate metadata")
    source = {k: metadata[k] for k in PROVENANCE_ORDER}
    native = metadata[FIELD]
    keys(native, {"id", "original_base64", "root_attributes", "metadata_xml", "projection"},
         "incomplete original phenylacetate document")
    expected = document(original_bytes(native["original_base64"]), source, metadata["kind"])
    require(json.dumps(native, sort_keys=True) == json.dumps(expected, sort_keys=True),
            "phenylacetate projection does not match original bytes")


def phenylacetate_term(metadata: dict, source_key: str) -> tuple[str, dict]:
    validate_phenylacetate_metadata(metadata)
    native = metadata[FIELD]["projection"]
    tag, ident = native["native_type"], native["id"]
    role = {
        "Compound": "compound", "Protein": "complex" if ident in COMPLEXES else "protein",
        "Enzymatic-Reaction": "activity", "Reaction": "reaction",
        "Promoter": "dna", "Transcription-Unit": "dna", "Pathway": "pathway",
    }[tag]
    return ident, {
        "label": native["label"], "synonyms": native["synonyms"], "source": source_key,
        "entity_type": "native_pathway" if role == "pathway" else "native_phenylacetate_" + role,
        "label_kind": "canonical" if native["label_origin"] == "direct_common_name"
                      else "source_context",
    }


def validate_phenylacetate_assertions(sources: dict, claims: list[tuple[str, str]]) -> None:
    """Reject downgrades/conflicting original owners before selection and on load."""
    assertions = {}
    for metadata in sources.values():
        kind = metadata.get("kind")
        if kind in PHENYLACETATE_KINDS:
            validate_phenylacetate_metadata(metadata)
            native = metadata[FIELD]
            ident = native["id"]
            assertion = json.dumps(native, sort_keys=True), metadata["version"], kind
            if ident in assertions:
                require(assertions[ident] == assertion, "conflicting complete native identity")
            assertions[ident] = assertion
        elif FIELD in metadata:
            raise ValueError("phenylacetate metadata requires its exact typed kind")
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
                    expected = META_KIND if ident.startswith("MetaCyc:") else ECO_KIND
                    require(kind == expected, "complete native identity requires its typed source")
    for ident, source in claims:
        if ident in PROFILES:
            metadata = sources[source]
            expected = META_KIND if ident.startswith("MetaCyc:") else ECO_KIND
            require(metadata.get("kind") == expected and metadata[FIELD]["id"] == ident,
                    "claimed native identity requires its complete typed owner")
