"""Bounded complete source originals for the native METHANOGENESIS-PWY graph.

Prospective scope: exact types, class roles and complete slots; no curated label
allowlist, public alias promotion or biochemical reconciliation. Existing owners
are unchanged. Source-only activities remain separate from generic reactions.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit
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
    require,
    scalar,
)
from pathwaymech.biocyc_native_context import attributes, blank, integer, ref_node
from pathwaymech.biocyc_p321 import original_bytes

KIND = "metacyc-methanogenesis-xml"
METHANOGENESIS_KINDS = {KIND}
FIELD = "native_methanogenesis"
_NATIVE_IDENTITY_ATTRIBUTES = {"frameid", "orgid", "ID", "resource"}
_NATIVE_OBJECT_TAGS = {
    "Compound",
    "Enzymatic-Reaction",
    "Evidence-Code",
    "Feature",
    "GO-Term",
    "Gene",
    "Organism",
    "Organization",
    "Pathway",
    "Person",
    "Protein",
    "Publication",
    "Reaction",
    "Regulation",
    "cco",
}
PROFILES = {
    "MetaCyc:2.1.1.86-RXN": {
        "is_class": False,
        "slots": {
            "dblink": 16,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 3,
            "orphan": 1,
            "parent": 3,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 3,
        },
        "tag": "Reaction",
    },
    "MetaCyc:2.3.1.101-RXN": {
        "is_class": False,
        "slots": {
            "dblink": 10,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 3,
            "orphan": 1,
            "parent": 2,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 2,
        },
        "tag": "Reaction",
    },
    "MetaCyc:3.5.4.27-RXN": {
        "is_class": False,
        "slots": {
            "dblink": 7,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 2,
            "orphan": 1,
            "parent": 2,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 2,
        },
        "tag": "Reaction",
    },
    "MetaCyc:AF_RS00880-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 5,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS05405-MONOMER": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 8,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS08270-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 11,
            "gene": 1,
            "has-feature": 4,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS08295-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 11,
            "gene": 1,
            "has-feature": 2,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS08305-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS09685-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 9,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS09690-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 6,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS09695-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS09700-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS09720-MONOMER": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 9,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS10430-MONOMER": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 10,
            "gene": 1,
            "has-feature": 2,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:AF_RS11105-MONOMER": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 11,
            "gene": 1,
            "has-feature": 5,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:BP07_RS06315-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:BP07_RS06320-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:BP07_RS06325-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:BP07_RS06330-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:BP07_RS06335-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:BP07_RS06340-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:BP07_RS06345-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:BP07_RS06350-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 3,
            "gene": 1,
            "has-feature": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CCO-IN": {
        "is_class": False,
        "slots": {"comment": 1, "common-name": 1, "parent": 1, "sensu": 1, "surrounded-by": 1},
        "tag": "cco",
    },
    "MetaCyc:CCO-MEMBRANE": {
        "is_class": True,
        "slots": {
            "common-name": 1,
            "definition": 1,
            "goid": 1,
            "instance": 1,
            "parent": 1,
            "sensu": 1,
            "subclass": 14,
        },
        "tag": "cco",
    },
    "MetaCyc:CCO-OUT": {
        "is_class": False,
        "slots": {"comment": 1, "common-name": 1, "parent": 1, "sensu": 1, "surrounds": 1},
        "tag": "cco",
    },
    "MetaCyc:CPD-15873": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "citation": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 3,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "synonym": 8,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD-19570": {
        "is_class": False,
        "slots": {
            "appears-in-right-side-of": 1,
            "citation": 1,
            "cml": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 2,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 4,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD-21374": {
        "is_class": False,
        "slots": {
            "appears-in-right-side-of": 1,
            "citation": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 1,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "synonym": 2,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD-7162": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "citation": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "dblink": 6,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "synonym": 4,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPLX-3321": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "component": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-381": {
        "is_class": False,
        "slots": {"catalyzes": 1, "comment": 1, "component": 6, "parent": 1, "species": 1},
        "tag": "Protein",
    },
    "MetaCyc:CPLX-561": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 3,
            "credits": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-562": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 4,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-581": {
        "is_class": False,
        "slots": {"catalyzes": 1, "component": 1, "parent": 1, "species": 1},
        "tag": "Protein",
    },
    "MetaCyc:CPLX-601": {
        "is_class": False,
        "slots": {"catalyzes": 1, "comment": 1, "component": 1, "parent": 1, "species": 1},
        "tag": "Protein",
    },
    "MetaCyc:CPLX-622": {
        "is_class": False,
        "slots": {"catalyzes": 1, "comment": 1, "component": 1, "parent": 1, "species": 1},
        "tag": "Protein",
    },
    "MetaCyc:CPLX-641": {
        "is_class": False,
        "slots": {"catalyzes": 1, "comment": 1, "component": 1, "parent": 1, "species": 1},
        "tag": "Protein",
    },
    "MetaCyc:CPLX-642": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component": 8,
            "component-of": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-643": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 1,
            "credits": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX2065-6": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 8,
            "credits": 1,
            "evidence": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX26TB-9": {
        "is_class": False,
        "slots": {
            "catalyzes": 1,
            "common-name": 1,
            "component": 8,
            "evidence": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CoM": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 8,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "synonym": 7,
            "systematic-name": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:ENZRXN-4121": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "km": 1,
            "ph-opt": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "regulated-by": 1,
            "specific-activity": 1,
            "temperature-opt": 1,
            "vmax": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-422": {
        "is_class": False,
        "slots": {
            "cofactor": 2,
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "regulated-by": 1,
            "synonym": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-641": {
        "is_class": False,
        "slots": {
            "cofactor": 1,
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "regulated-by": 1,
            "synonym": 2,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-662": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "regulated-by": 1,
            "synonym": 3,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-702": {
        "is_class": False,
        "slots": {
            "cofactor": 2,
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "km": 2,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "regulated-by": 1,
            "specific-activity": 1,
            "synonym": 3,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:FMDAMBARK-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FMDBMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "isozyme-sequence-similarity": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FMDBMBARK-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FMDCMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 9,
            "gene": 1,
            "isozyme-sequence-similarity": 2,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FMDCMBARK-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FMDDMBARK-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FMDEMBARK-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FMDFMBARK-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FORMYL-THMPT": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 4,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "synonym": 5,
        },
        "tag": "Compound",
    },
    "MetaCyc:FORMYLMETHANOFURAN-DEHYDROGENASE-RXN": {
        "is_class": False,
        "slots": {
            "credits": 1,
            "dblink": 19,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 3,
            "orphan": 1,
            "parent": 2,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 4,
        },
        "tag": "Reaction",
    },
    "MetaCyc:FTRMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FWDAMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FWDBMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "isozyme-sequence-similarity": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FWDCMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "isozyme-sequence-similarity": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FWDDMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "isozyme-sequence-similarity": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:Formyl-methanofurans": {
        "is_class": True,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 3,
            "instance": 5,
            "parent": 1,
            "synonym": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:H2-METHYLENE-THMPT-DEHYDRO-RXN": {
        "is_class": False,
        "slots": {
            "dblink": 3,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 2,
            "orphan": 1,
            "parent": 2,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 2,
        },
        "tag": "Reaction",
    },
    "MetaCyc:HCN": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 8,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:HMDMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 9,
            "gene": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:HYDROGEN-MOLECULE": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 11,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:MCHMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:MERMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "dblink": 6,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:METHANOGENESIS-PWY": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 1,
            "evidence": 1,
            "in-pathway": 1,
            "parent": 1,
            "pathway-link": 9,
            "reaction-layout": 6,
            "reaction-list": 1,
            "reaction-ordering": 5,
            "species": 3,
            "super-pathways": 1,
            "taxonomic-range": 1,
        },
        "tag": "Pathway",
    },
    "MetaCyc:METHELENE-THMPT-OXI-RXN": {
        "is_class": False,
        "slots": {
            "dblink": 3,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 2,
            "orphan": 1,
            "parent": 2,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 2,
        },
        "tag": "Reaction",
    },
    "MetaCyc:METHENYLTETRAHYDROMETHANOPTERIN": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 5,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "synonym": 6,
        },
        "tag": "Compound",
    },
    "MetaCyc:METHYL-THMPT": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 4,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "synonym": 6,
        },
        "tag": "Compound",
    },
    "MetaCyc:METHYLENETETRAHYDROMETHANOPTERIN": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 6,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "synonym": 5,
        },
        "tag": "Compound",
    },
    "MetaCyc:MG+2": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 10,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 5,
        },
        "tag": "Compound",
    },
    "MetaCyc:MN+2": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 10,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 4,
        },
        "tag": "Compound",
    },
    "MetaCyc:MONOMER-4021": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "dblink": 4,
            "gene": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:MTRAMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 6,
            "gene": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:MTRBMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:MTRCMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:MTRDMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:MTREMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:MTRFMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:MTRGMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:MTRHMAUTO-MONOMER": {
        "is_class": False,
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "MetaCyc:Me-CoM": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 6,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "synonym": 8,
        },
        "tag": "Compound",
    },
    "MetaCyc:Methanofurans": {
        "is_class": True,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "dblink": 4,
            "instance": 5,
            "parent": 1,
            "subclass": 2,
        },
        "tag": "Compound",
    },
    "MetaCyc:NA+": {
        "is_class": False,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 11,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 2,
        },
        "tag": "Compound",
    },
    "MetaCyc:Oxidized-Factor-F420": {
        "is_class": True,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "dblink": 2,
            "instance": 11,
            "parent": 1,
            "synonym": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:Reduced-Factor-F420": {
        "is_class": True,
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "dblink": 4,
            "instance": 9,
            "parent": 1,
            "synonym": 2,
        },
        "tag": "Compound",
    },
    "MetaCyc:THMPT": {
        "is_class": False,
        "slots": {
            "abbrev-name": 1,
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 6,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "synonym": 2,
        },
        "tag": "Compound",
    },
}
COMPLEXES = {
    "MetaCyc:CPLX-3321",
    "MetaCyc:CPLX-381",
    "MetaCyc:CPLX-561",
    "MetaCyc:CPLX-562",
    "MetaCyc:CPLX-581",
    "MetaCyc:CPLX-601",
    "MetaCyc:CPLX-622",
    "MetaCyc:CPLX-641",
    "MetaCyc:CPLX-642",
    "MetaCyc:CPLX-643",
    "MetaCyc:CPLX2065-6",
    "MetaCyc:CPLX26TB-9",
}
UNNAMED_HOMOMERS = {
    "MetaCyc:CPLX-3321",
    "MetaCyc:CPLX-581",
    "MetaCyc:CPLX-601",
    "MetaCyc:CPLX-622",
    "MetaCyc:CPLX-641",
}
MATERIAL_ROLES = {
    "CARBON-DIOXIDE": {"is_class": False, "tag": "Compound"},
    "CoM": {"is_class": False, "tag": "Compound"},
    "FORMYL-THMPT": {"is_class": False, "tag": "Compound"},
    "Formyl-methanofurans": {"is_class": True, "tag": "Compound"},
    "HYDROGEN-MOLECULE": {"is_class": False, "tag": "Compound"},
    "METHENYLTETRAHYDROMETHANOPTERIN": {"is_class": False, "tag": "Compound"},
    "METHYL-THMPT": {"is_class": False, "tag": "Compound"},
    "METHYLENETETRAHYDROMETHANOPTERIN": {"is_class": False, "tag": "Compound"},
    "Me-CoM": {"is_class": False, "tag": "Compound"},
    "Methanofurans": {"is_class": True, "tag": "Compound"},
    "NA+": {"is_class": False, "tag": "Compound"},
    "Oxidized-Factor-F420": {"is_class": True, "tag": "Compound"},
    "Oxidized-ferredoxins": {"is_class": True, "tag": "Protein"},
    "PROTON": {"is_class": False, "tag": "Compound"},
    "Reduced-Factor-F420": {"is_class": True, "tag": "Compound"},
    "Reduced-ferredoxins": {"is_class": True, "tag": "Protein"},
    "THMPT": {"is_class": False, "tag": "Compound"},
    "WATER": {"is_class": False, "tag": "Compound"},
}
NATIVE_MEMBERS = {
    "FORMYLMETHANOFURAN-DEHYDROGENASE-RXN",
    "2.3.1.101-RXN",
    "3.5.4.27-RXN",
    "H2-METHYLENE-THMPT-DEHYDRO-RXN",
    "METHELENE-THMPT-OXI-RXN",
    "2.1.1.86-RXN",
}
NODE_ROLES = {
    "native_methanogenesis_compound": ("participants", {"small_molecule", "cofactor"}),
    "native_methanogenesis_compound_class": ("participants", {"chemical_entity", "cofactor"}),
    "native_methanogenesis_protein": ("participants", {"protein"}),
    "native_methanogenesis_complex": ("participants", {"complex"}),
    "native_methanogenesis_activity": ("participants", {"molecular_activity"}),
    "native_methanogenesis_reaction": ("reactions", {"molecular_activity"}),
    "native_methanogenesis_location": ("participants", {"cellular_component"}),
}


def _identity(kind: str) -> tuple[str, str]:
    require(kind in METHANOGENESIS_KINDS, "unsupported methanogenesis kind")
    return "META", "MetaCyc"


def _source_frame(source: dict) -> str:
    """Retain the exact bare request syntax of all 92 selected acquisition receipts.

    This source kind does not normalize an unacquired id= URL into provenance.
    Earlier typed source request contracts are unchanged.
    """
    keys(source, PROVENANCE, "invalid source provenance fields")
    require(
        all(isinstance(v, str) and bool(v.strip()) for v in source.values()),
        "empty source provenance",
    )
    match = re.fullmatch(
        rf"https://{re.escape(HOST)}/getxml\?META:([A-Za-z0-9][A-Za-z0-9_.+\-]*)", source["url"]
    )
    require(match is not None, "requires exact acquired native HTTPS META request")
    require(re.fullmatch(r"[0-9a-f]{64}", source["sha256"]) is not None, "invalid provenance hash")
    return match[1]


def _envelope(body: bytes, source: dict, kind: str):
    pgdb, prefix = _identity(kind)
    frame = _source_frame(source)
    ident = prefix + ":" + frame
    require(ident in PROFILES, "outside the reviewed methanogenesis frame scope")
    require(source["version"] == "27.0", "unsupported methanogenesis source release")
    require(hashlib.sha256(body).hexdigest() == source["sha256"], "original hash mismatch")
    root = ET.fromstring(body, parser=ET.XMLParser(target=_TreeBuilder()))
    legacy = f"http://{HOST}:443/"
    require(
        root.tag == "ptools-xml"
        and len(root) == 2
        and set(root.attrib) == {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        and root.get("ptools-version") == "27.0"
        and root.get("{http://www.w3.org/XML/1998/namespace}base")
        in {source["url"], legacy + "getxml?" + pgdb + ":" + frame.replace("+", "%2b")},
        "methanogenesis envelope mismatch",
    )
    meta = one(root, "metadata")
    entity = next(n for n in root if n.tag != "metadata")
    blank(root)
    blank(meta)
    require(
        not meta.attrib
        and Counter(n.tag for n in meta)
        == Counter(["url", "service_name", "query", "num_results", "PGDB"]),
        "invalid complete native metadata",
    )
    require(
        scalar(meta, "url") in {legacy, f"https://{HOST}/"}
        and scalar(meta, "service_name") == "getxml"
        and scalar(meta, "query") == pgdb + ":" + frame
        and scalar(meta, "num_results") == "1",
        "native request identity mismatch",
    )
    db = one(meta, "PGDB")
    blank(db)
    require(db.attrib == {"orgid": pgdb, "version": "27.0"}, "PGDB identity mismatch")
    require(
        Counter(n.tag for n in db) == Counter(["species"]),
        "incomplete native PGDB context",
    )
    require(
        scalar(db, "species", True) == "MetaCyc",
        "wrong native database species",
    )
    attributes(entity, frame, pgdb, PROFILES[ident]["tag"], PROFILES[ident]["is_class"])
    require(
        Counter(n.tag for n in entity) == PROFILES[ident]["slots"],
        "incomplete or unsupported complete native slots",
    )
    # Check every embedded native identity while retaining uninterpreted context.
    # Embedded annotations do not become selected taxa, enzymes or chemical aliases.
    for node in entity.iter():
        if node.tag not in _NATIVE_OBJECT_TAGS and not _NATIVE_IDENTITY_ATTRIBUTES.intersection(
            node.attrib
        ):
            continue
        require(
            bool(node.get("frameid"))
            and bool(node.get("orgid"))
            and (("ID" in node.attrib) != ("resource" in node.attrib)),
            "incomplete or ambiguous embedded native identity",
        )
        native = node.get("orgid", "") + ":" + node.get("frameid", "")
        require(
            node.get("orgid") == pgdb and bool(node.get("frameid")),
            "embedded native database identity mismatch",
        )
        if "ID" in node.attrib:
            require(node.get("ID") == native, "embedded native ID/frame mismatch")
        if "resource" in node.attrib:
            require(
                node.get("resource") in {"getxml?" + native, "#" + native},
                "embedded native resource/frame mismatch",
            )
    return root, entity, ident


def _literal_ref(
    node: ET.Element, pgdb: str, tag: str, *, is_class: bool = False, local: bool = False
) -> dict:
    """Exact native references, retaining literal charged frame tokens locally."""
    frame = node.get("frameid", "")
    attrs = {"resource": "getxml?" + pgdb + ":" + frame, "orgid": pgdb, "frameid": frame}
    if is_class:
        attrs["class"] = "true"
    accepted = [attrs]
    if local:
        accepted.append({**attrs, "resource": "#" + pgdb + ":" + frame})
    require(
        re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+\-]*", frame) is not None
        and node.tag == tag
        and node.attrib in accepted
        and not len(node)
        and not (node.text or "").strip()
        and not (node.tail or "").strip(),
        "invalid literal native reference",
    )
    return {"id": "MetaCyc:" + frame, "native_type": tag, "is_class": is_class}


def _side(entity: ET.Element, side: str, pgdb: str) -> list[dict]:
    result = []
    for wrapper in entity.findall(side):
        blank(wrapper)
        materials = [n for n in wrapper if n.tag not in {"coefficient", "compartment"}]
        require(not wrapper.attrib and len(materials) == 1, "invalid native material occurrence")
        node = materials[0]
        require(node.get("frameid") in MATERIAL_ROLES, "outside exact native material scope")
        role = MATERIAL_ROLES[node.get("frameid")]
        allowed = {node.tag: 1}
        coeff = wrapper.find("coefficient")
        compartment = wrapper.find("compartment")
        if coeff is not None:
            allowed["coefficient"] = 1
        if compartment is not None:
            allowed["compartment"] = 1
        require(Counter(n.tag for n in wrapper) == allowed, "invalid material slot multiplicity")
        material = _literal_ref(node, pgdb, role["tag"], is_class=role["is_class"])
        location = None
        if compartment is not None:
            blank(compartment)
            require(
                not compartment.attrib and len(compartment) == 1, "invalid occurrence compartment"
            )
            location = _literal_ref(compartment[0], pgdb, "cco")["id"]
            require(
                location in {"MetaCyc:CCO-IN", "MetaCyc:CCO-OUT"},
                "outside native occurrence locations",
            )
        result.append(
            {
                "material": material["id"],
                "native_type": role["tag"],
                "is_class": role["is_class"],
                "coefficient": integer(coeff) if coeff is not None else None,
                "compartment": location,
            }
        )
    require(
        bool(result) and len({(r["material"], r["compartment"]) for r in result}) == len(result),
        "empty or duplicate native material occurrences",
    )
    return result


def _projection(entity: ET.Element, ident: str) -> dict:
    frame = entity.get("frameid")
    pgdb, prefix = ("META", "MetaCyc") if ident.startswith("MetaCyc:") else ("ECOLI", "EcoCyc")
    common = entity.findall("common-name")
    require(len(common) <= 1, "duplicate common name")
    label = name(common[0], "") if common else frame
    label_origin = "direct_common_name" if common else "native_frame_id"
    if ident in UNNAMED_HOMOMERS:
        require(not common, "unnamed homomer gained direct name outside retained source profile")
        component = one(entity, "component")
        require(
            integer(one(component, "coefficient")) >= 2,
            "unnamed homomer requires multiple identical subunits",
        )
        activity_wrapper = one(entity, "catalyzes")
        blank(activity_wrapper)
        require(
            not activity_wrapper.attrib and len(activity_wrapper) == 1, "ambiguous homomer activity"
        )
        activity = activity_wrapper[0]
        require(
            activity.tag == "Enzymatic-Reaction" and activity.get("detail") == "low",
            "invalid naming activity",
        )
        enzyme = one(activity, "enzyme")
        blank(enzyme)
        require(not enzyme.attrib and len(enzyme) == 1, "invalid naming enzyme link")
        require(
            _literal_ref(enzyme[0], pgdb, "Protein", local=True)["id"] == ident,
            "naming activity belongs to another enzyme",
        )
        label = name(one(activity, "common-name"), "")
        label_origin = "sole_native_homomer_activity_name"
    aliases = sorted({name(n, "") for n in entity.findall("synonym")} - {label})
    result = {
        "id": ident,
        "native_type": entity.tag,
        "is_class": PROFILES[ident]["is_class"],
        "label": label,
        "synonyms": aliases,
        "label_origin": label_origin,
        "slots": [
            {"ordinal": i, "name": n.tag, "xml": ET.tostring(n, encoding="unicode")}
            for i, n in enumerate(entity, 1)
        ],
    }
    if entity.tag == "Reaction":
        result["sides"] = {side: _side(entity, side, pgdb) for side in ("left", "right")}
        direction = scalar(entity, "reaction-direction")
        require(
            direction in {"REVERSIBLE", "PHYSIOL-LEFT-TO-RIGHT", "PHYSIOL-RIGHT-TO-LEFT"},
            "invalid native reaction direction",
        )
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
            require(
                not wrapper.attrib
                and Counter(n.tag for n in wrapper)
                in (Counter({"Protein": 1}), Counter({"Protein": 1, "coefficient": 1})),
                "invalid native complex component",
            )
            component = ref_node(one(wrapper, "Protein"), pgdb, "Protein")["id"]
            coeff = wrapper.find("coefficient")
            components.append(
                {"id": component, "coefficient": integer(coeff) if coeff is not None else None}
            )
        require(
            bool(components) and len({r["id"] for r in components}) == len(components),
            "empty or duplicate native complex components",
        )
        result["components"] = components
    if entity.tag == "Pathway":
        listing = one(entity, "reaction-list")
        blank(listing)
        require(not listing.attrib, "attributed native reaction list")
        members = [ref_node(n, pgdb, "Reaction")["id"] for n in listing]
        require(
            len(members) == 6 and set(members) == {prefix + ":" + f for f in NATIVE_MEMBERS},
            "wrong complete METHANOGENESIS-PWY native membership",
        )
        result["reaction_list"] = members
    return result


def document(body: bytes, source: dict, kind: str) -> dict:
    root, entity, ident = _envelope(body, source, kind)
    return {
        "id": ident,
        "original_base64": base64.b64encode(body).decode("ascii"),
        "root_attributes": dict(root.attrib),
        "metadata_xml": ET.tostring(one(root, "metadata"), encoding="unicode"),
        "projection": _projection(entity, ident),
    }


def methanogenesis_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(entry, PROVENANCE | {"key", "kind", "path"}, "invalid methanogenesis manifest")
    require(isinstance(entry["key"], str) and bool(entry["key"].strip()), "empty source key")
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    result = {
        **source,
        "kind": entry["kind"],
        FIELD: document(original_path(entry, cache_dir).read_bytes(), source, entry["kind"]),
    }
    validate_methanogenesis_metadata(result)
    return result


def validate_methanogenesis_metadata(metadata: dict) -> None:
    keys(metadata, PROVENANCE | {"kind", FIELD}, "invalid methanogenesis metadata")
    source = {k: metadata[k] for k in PROVENANCE_ORDER}
    native = metadata[FIELD]
    keys(
        native,
        {"id", "original_base64", "root_attributes", "metadata_xml", "projection"},
        "incomplete original methanogenesis document",
    )
    expected = document(original_bytes(native["original_base64"]), source, metadata["kind"])
    require(
        json.dumps(native, sort_keys=True) == json.dumps(expected, sort_keys=True),
        "methanogenesis projection does not match original bytes",
    )


def methanogenesis_term(metadata: dict, source_key: str) -> tuple[str, dict]:
    validate_methanogenesis_metadata(metadata)
    native = metadata[FIELD]["projection"]
    tag, ident = native["native_type"], native["id"]
    role = {
        "Compound": "compound_class" if native["is_class"] else "compound",
        "Protein": "complex" if ident in COMPLEXES else "protein",
        "Enzymatic-Reaction": "activity",
        "Reaction": "reaction",
        "Pathway": "pathway",
        "cco": "location",
    }[tag]
    return ident, {
        "label": native["label"],
        "synonyms": native["synonyms"],
        "source": source_key,
        "entity_type": "native_pathway" if role == "pathway" else "native_methanogenesis_" + role,
        "label_kind": "canonical"
        if native["label_origin"] == "direct_common_name"
        else "source_context",
    }


def validate_methanogenesis_assertions(sources: dict, claims: list[tuple[str, str]]) -> None:
    """Reject downgrades/conflicting original owners before selection and on load."""
    assertions = {}
    for metadata in sources.values():
        kind = metadata.get("kind")
        if kind in METHANOGENESIS_KINDS:
            validate_methanogenesis_metadata(metadata)
            native = metadata[FIELD]
            ident = native["id"]
            assertion = json.dumps(native, sort_keys=True), metadata["version"], kind
            if ident in assertions:
                require(assertions[ident] == assertion, "conflicting complete native identity")
            assertions[ident] = assertion
        elif FIELD in metadata:
            raise ValueError("methanogenesis metadata requires its exact typed kind")
        url = urlsplit(metadata.get("url", ""))
        if url.hostname in {HOST, "biocyc.org", "www.biocyc.org", "metacyc.org", "www.metacyc.org"}:
            params = parse_qs(url.query)
            tokens = [v for name in ("id", "object") for v in params.get(name, [])]
            # Native receipts also use /getxml?META:FRAME (or ECOLI:FRAME).
            # Treat only the complete literal query on that HTTP(S) endpoint as
            # a bare request token. The exact profile lookup below must not turn
            # arbitrary query values, suffixes or unrelated paths into identities.
            if (
                url.scheme in {"http", "https"}
                and url.path == "/getxml"
                and url.query.startswith(("META:", "ECOLI:"))
            ):
                tokens.append(unquote(url.query))
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
            require(
                metadata.get("kind") == expected and metadata[FIELD]["id"] == ident,
                "claimed native identity requires its complete typed owner",
            )
