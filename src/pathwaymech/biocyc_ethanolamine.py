"""Bounded complete source originals for the native PWY0-1477 graph.

Finite scope: exact types, class roles and complete slots; no curated label
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

META_KIND = "metacyc-ethanolamine-xml"
ECO_KIND = "ecocyc-ethanolamine-xml"
ETHANOLAMINE_KINDS = {META_KIND, ECO_KIND}
FIELD = "native_ethanolamine"
_NATIVE_IDENTITY_ATTRIBUTES = {"frameid", "orgid", "ID", "resource"}
_NATIVE_OBJECT_TAGS = {
    "Compound",
    "Enzymatic-Reaction",
    "Evidence-Code",
    "Feature",
    "GO-Term",
    "Gene",
    "Genetic-Element",
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
    "EcoCyc:CCI-CYTOSOL-GN": {
        "embedded_shapes": {("cco", "", ""): 4, ("cco", "true", ""): 2},
        "is_class": False,
        "parents": [("cco", "CCO-CYTOSOL")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "parent": 1,
            "sensu": 1,
            "surrounded-by": 1,
            "surrounds": 1,
        },
        "tag": "cco",
    },
    "EcoCyc:CCI-PM-BAC-NEG-GN": {
        "embedded_shapes": {("cco", "", ""): 3, ("cco", "true", ""): 2},
        "is_class": False,
        "parents": [("cco", "CCO-PM-BAC-NEG")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "parent": 1,
            "sensu": 1,
            "surrounded-by": 1,
            "surrounds": 1,
        },
        "tag": "cco",
    },
    "EcoCyc:CPLX0-7613": {
        "embedded_shapes": {
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 13,
            ("Organization", "", "full"): 3,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 14,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {"common-name": 1, "component": 1, "credits": 1, "parent": 1, "species": 1},
        "tag": "Protein",
    },
    "EcoCyc:CPLX0-7801": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 15,
            ("Organization", "", "full"): 3,
            ("Person", "", ""): 3,
            ("Person", "", "full"): 14,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 2,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component": 1,
            "credits": 1,
            "evidence": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "EcoCyc:CPLX0-7835": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 15,
            ("Organization", "", "full"): 3,
            ("Person", "", ""): 3,
            ("Person", "", "full"): 14,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 2,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component": 1,
            "credits": 1,
            "evidence": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "EcoCyc:CPLX0-7836": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 14,
            ("Organization", "", "full"): 3,
            ("Person", "", ""): 2,
            ("Person", "", "full"): 14,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 2,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component": 1,
            "credits": 1,
            "evidence": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "EcoCyc:CPLX0-7912": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 15,
            ("Organization", "", "full"): 3,
            ("Person", "", ""): 3,
            ("Person", "", "full"): 14,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 2,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "citation": 1,
            "comment": 1,
            "common-name": 1,
            "component": 1,
            "credits": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "EcoCyc:EG12190-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 16,
            ("Evidence-Code", "true", "full"): 4,
            ("Feature", "", "full"): 6,
            ("Feature", "true", ""): 6,
            ("GO-Term", "true", ""): 7,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 6,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 8,
            ("Publication", "", "full"): 9,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 15,
            "evidence": 2,
            "gene": 1,
            "has-feature": 6,
            "has-go-term": 7,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "EcoCyc:ETHAMLY-CPLX": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", ""): 4,
            ("Evidence-Code", "true", "full"): 2,
            ("GO-Term", "true", ""): 2,
            ("Organization", "", ""): 2,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 3,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 2,
            ("Publication", "", "full"): 4,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "component": 2,
            "credits": 1,
            "dblink": 6,
            "has-go-term": 2,
            "molecular-weight-exp": 1,
            "parent": 1,
            "pi": 1,
        },
        "tag": "Protein",
    },
    "EcoCyc:EUTB-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 39,
            ("Evidence-Code", "true", "full"): 10,
            ("Feature", "", "full"): 9,
            ("Feature", "true", ""): 9,
            ("GO-Term", "true", ""): 9,
            ("Gene", "", ""): 1,
            ("Protein", "", ""): 10,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 24,
            ("Publication", "", "full"): 18,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "dblink": 21,
            "gene": 1,
            "has-feature": 9,
            "has-go-term": 9,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "EcoCyc:EUTC-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 28,
            ("Evidence-Code", "true", "full"): 7,
            ("Feature", "", "full"): 4,
            ("Feature", "true", ""): 4,
            ("GO-Term", "true", ""): 9,
            ("Gene", "", ""): 1,
            ("Protein", "", ""): 5,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 14,
            ("Publication", "", "full"): 16,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "dblink": 19,
            "gene": 1,
            "has-feature": 4,
            "has-go-term": 9,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7270-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 14,
            ("Evidence-Code", "true", "full"): 4,
            ("Feature", "", "full"): 4,
            ("Feature", "true", ""): 4,
            ("GO-Term", "true", ""): 7,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 4,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 6,
            ("Publication", "", "full"): 10,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "citation": 2,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 18,
            "evidence": 1,
            "gene": 1,
            "has-feature": 4,
            "has-go-term": 7,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7271-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 25,
            ("Evidence-Code", "true", "full"): 7,
            ("Feature", "", "full"): 15,
            ("Feature", "true", ""): 15,
            ("GO-Term", "true", ""): 7,
            ("Gene", "", ""): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 13,
            ("Organization", "", "full"): 3,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 14,
            ("Protein", "", ""): 16,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 17,
            ("Publication", "", "full"): 10,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 19,
            "gene": 1,
            "has-feature": 15,
            "has-go-term": 7,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7281-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 7,
            ("Evidence-Code", "true", "full"): 2,
            ("Feature", "", "full"): 1,
            ("Feature", "true", ""): 1,
            ("GO-Term", "true", ""): 4,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 2,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 1,
            ("Publication", "", "full"): 6,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 10,
            "evidence": 1,
            "gene": 1,
            "has-feature": 1,
            "has-go-term": 4,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7282-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 24,
            ("Evidence-Code", "true", "full"): 5,
            ("Feature", "", "full"): 12,
            ("Feature", "true", ""): 12,
            ("GO-Term", "true", ""): 5,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 12,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 14,
            ("Publication", "", "full"): 10,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 10,
            "evidence": 1,
            "gene": 1,
            "has-feature": 12,
            "has-go-term": 5,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7283-MONOMER": {
        "embedded_shapes": {
            ("Compound", "", ""): 3,
            ("Evidence-Code", "true", ""): 26,
            ("Evidence-Code", "true", "full"): 5,
            ("Feature", "", "full"): 12,
            ("Feature", "true", ""): 12,
            ("GO-Term", "true", ""): 8,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 2,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 12,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 13,
            ("Publication", "", "full"): 13,
            ("cco", "", ""): 2,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 15,
            "gene": 1,
            "has-feature": 12,
            "has-go-term": 8,
            "location": 2,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7284-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 3,
            ("Evidence-Code", "true", "full"): 1,
            ("Feature", "", "full"): 1,
            ("Feature", "true", ""): 1,
            ("GO-Term", "true", ""): 2,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 3,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 11,
            "gene": 1,
            "has-feature": 1,
            "has-go-term": 2,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7285-MONOMER": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", ""): 13,
            ("Evidence-Code", "true", "full"): 3,
            ("Feature", "", "full"): 1,
            ("Feature", "true", ""): 1,
            ("GO-Term", "true", ""): 7,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 3,
            ("Publication", "", "full"): 13,
            ("Reaction", "", ""): 1,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "catalyzes": 1,
            "citation": 3,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 14,
            "gene": 1,
            "has-feature": 1,
            "has-go-term": 7,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7286-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 11,
            ("Evidence-Code", "true", "full"): 5,
            ("Feature", "", "full"): 2,
            ("Feature", "true", ""): 2,
            ("GO-Term", "true", ""): 7,
            ("Gene", "", ""): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 13,
            ("Organization", "", "full"): 3,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 14,
            ("Protein", "", ""): 3,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 1,
            ("Publication", "", "full"): 11,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 13,
            "gene": 1,
            "has-feature": 2,
            "has-go-term": 7,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 4,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7287-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 11,
            ("Evidence-Code", "true", "full"): 4,
            ("Feature", "", "full"): 2,
            ("Feature", "true", ""): 2,
            ("GO-Term", "true", ""): 7,
            ("Gene", "", ""): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 10,
            ("Organization", "", "full"): 3,
            ("Person", "", "full"): 13,
            ("Protein", "", ""): 3,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 3,
            ("Publication", "", "full"): 9,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "dblink": 19,
            "gene": 1,
            "has-feature": 2,
            "has-go-term": 7,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 4,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7288-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 13,
            ("Evidence-Code", "true", "full"): 4,
            ("Feature", "", "full"): 1,
            ("Feature", "true", ""): 1,
            ("GO-Term", "true", ""): 9,
            ("Gene", "", ""): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 10,
            ("Organization", "", "full"): 3,
            ("Person", "", "full"): 13,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 4,
            ("Publication", "", "full"): 10,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "dblink": 15,
            "gene": 1,
            "has-feature": 1,
            "has-go-term": 9,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7289-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 15,
            ("Evidence-Code", "true", "full"): 2,
            ("Feature", "", "full"): 3,
            ("Feature", "true", ""): 3,
            ("GO-Term", "true", ""): 10,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 2,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 3,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 8,
            ("Publication", "", "full"): 7,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 12,
            "gene": 1,
            "has-feature": 3,
            "has-go-term": 10,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7290-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 10,
            ("Evidence-Code", "true", "full"): 2,
            ("Feature", "", "full"): 1,
            ("Feature", "true", ""): 1,
            ("GO-Term", "true", ""): 8,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 2,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 3,
            ("Publication", "", "full"): 7,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 14,
            "gene": 1,
            "has-feature": 1,
            "has-go-term": 8,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 2,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7291-MONOMER": {
        "embedded_shapes": {
            ("Compound", "", ""): 1,
            ("Evidence-Code", "true", ""): 14,
            ("Evidence-Code", "true", "full"): 2,
            ("Feature", "", "full"): 2,
            ("Feature", "true", ""): 2,
            ("GO-Term", "true", ""): 10,
            ("Gene", "", ""): 1,
            ("Organization", "", ""): 2,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 6,
            ("Publication", "", "full"): 8,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 12,
            "gene": 1,
            "has-feature": 2,
            "has-go-term": 10,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "EcoCyc:G7292-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 12,
            ("Evidence-Code", "true", "full"): 6,
            ("Feature", "", "full"): 3,
            ("Feature", "true", ""): 3,
            ("GO-Term", "true", ""): 7,
            ("Gene", "", ""): 1,
            ("Genetic-Element", "", ""): 1,
            ("Organism", "", "full"): 1,
            ("Organism", "true", ""): 1,
            ("Organization", "", ""): 12,
            ("Organization", "", "full"): 3,
            ("Person", "", "full"): 14,
            ("Protein", "", ""): 4,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 5,
            ("Publication", "", "full"): 9,
            ("cco", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 16,
            "gene": 1,
            "has-feature": 3,
            "has-go-term": 7,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "MetaCyc:1-AMINO-PROPAN-2-OL": {
        "embedded_shapes": {
            ("Compound", "", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 6,
            ("Regulation", "", "low"): 1,
            ("Regulation", "true", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 8,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "regulates": 1,
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:ACETALD": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 4,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 4,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 63,
            ("Regulation", "", "low"): 4,
            ("Regulation", "true", ""): 4,
        },
        "is_class": False,
        "parents": [("Compound", "Toxins"), ("Compound", "n-Alkanals")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 12,
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
    "MetaCyc:ACETALD-DEHYDROG-RXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 6,
            ("Enzymatic-Reaction", "", "low"): 12,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Pathway", "", ""): 15,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 12,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 12,
            ("Reaction", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Reaction", "Chemical-Reactions"), ("Reaction", "Small-Molecule-Reactions")],
        "slots": {
            "credits": 1,
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
            "right": 3,
        },
        "tag": "Reaction",
    },
    "MetaCyc:ADENOSYLCOBALAMIN": {
        "embedded_shapes": {
            ("Compound", "true", ""): 4,
            ("Enzymatic-Reaction", "", "low"): 23,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 23,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 30,
        },
        "is_class": False,
        "parents": [
            ("Compound", "Adenosylcobamide"),
            ("Compound", "B-vitamins"),
            ("Compound", "Cobalamins"),
            ("Compound", "Cofactors"),
        ],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "cofactors-of": 1,
            "comment": 1,
            "common-name": 1,
            "dblink": 10,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 4,
            "synonym": 19,
            "systematic-name": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:ALCOHOL-DEHYDROG-RXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 5,
            ("Enzymatic-Reaction", "", "low"): 21,
            ("Evidence-Code", "true", "full"): 1,
            ("Pathway", "", ""): 11,
            ("Protein", "", ""): 21,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 21,
            ("Reaction", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Reaction", "Chemical-Reactions"), ("Reaction", "Small-Molecule-Reactions")],
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
            "right": 3,
        },
        "tag": "Reaction",
    },
    "MetaCyc:CPD-1829": {
        "embedded_shapes": {
            ("Compound", "true", ""): 2,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 4,
        },
        "is_class": False,
        "parents": [("Compound", "Cobalamins"), ("Compound", "Organometallics")],
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
            "synonym": 2,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD-315": {
        "embedded_shapes": {
            ("Compound", "", ""): 1,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 2,
            ("Regulation", "", "low"): 1,
            ("Regulation", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Compound", "Cobalamins"), ("Compound", "Cyanocobamides")],
        "slots": {
            "appears-in-right-side-of": 1,
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "dblink": 8,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 10,
            "systematic-name": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD-9037": {
        "embedded_shapes": {
            ("Compound", "", ""): 1,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 5,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 5,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 15,
            ("Regulation", "", "low"): 1,
            ("Regulation", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Compound", "CPD-20938"), ("Compound", "Methylcobamides")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "cofactors-of": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 7,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 7,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD0-1256": {
        "embedded_shapes": {
            ("Compound", "", ""): 1,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
            ("Regulation", "", "low"): 1,
            ("Regulation", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Compound", "Cobalamins")],
        "slots": {
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 3,
            "gibbs-0": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 2,
            "systematic-name": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD0-1258": {
        "embedded_shapes": {
            ("Compound", "", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
            ("Regulation", "", "low"): 1,
            ("Regulation", "true", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cml": 1,
            "common-name": 1,
            "dblink": 5,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "regulates": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD0-1260": {
        "embedded_shapes": {
            ("Compound", "", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
            ("Regulation", "", "low"): 1,
            ("Regulation", "true", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cml": 1,
            "common-name": 1,
            "dblink": 4,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "regulates": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD0-2347": {
        "embedded_shapes": {
            ("Compound", "", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
            ("Regulation", "", "low"): 1,
            ("Regulation", "true", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cml": 1,
            "common-name": 1,
            "dblink": 3,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "regulates": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPLX-9275": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 2,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [
            ("Protein", "Corrinoid-Adenosyltransferases"),
            ("Protein", "Protein-Complexes"),
        ],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 1,
            "credits": 1,
            "molecular-weight-exp": 1,
            "parent": 2,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX0-7912": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 3,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 2,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 2,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "citation": 1,
            "comment": 1,
            "common-name": 1,
            "component": 1,
            "credits": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:ENZRXN-26156": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", ""): 4,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "kcat": 2,
            "km": 2,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-26157": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", ""): 4,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "kcat": 2,
            "km": 2,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-26158": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-26161": {
        "embedded_shapes": {
            ("Compound", "", ""): 6,
            ("Evidence-Code", "true", ""): 3,
            ("Evidence-Code", "true", "full"): 2,
            ("Protein", "", ""): 1,
            ("Publication", "", ""): 6,
            ("Publication", "", "full"): 3,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cofactor": 1,
            "common-name": 1,
            "enzyme": 1,
            "evidence": 3,
            "kcat": 2,
            "km": 2,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "vmax": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN0-7425": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Enzymatic-Reaction", "", ""): 1,
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", ""): 5,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
            ("Regulation", "", "low"): 1,
            ("Regulation", "true", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "enzyme": 1,
            "evidence": 1,
            "km": 3,
            "ph-opt": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "regulated-by": 1,
            "synonym": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ETHAMLY-CPLX": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", ""): 4,
            ("Evidence-Code", "true", "full"): 2,
            ("GO-Term", "true", ""): 2,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 3,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 2,
            ("Publication", "", "full"): 5,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "component": 2,
            "credits": 1,
            "dblink": 6,
            "has-go-term": 2,
            "molecular-weight-exp": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:ETHAMLY-ENZRXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 11,
            ("Enzymatic-Reaction", "", ""): 8,
            ("Evidence-Code", "true", ""): 6,
            ("Evidence-Code", "true", "full"): 4,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", ""): 6,
            ("Publication", "", "full"): 7,
            ("Reaction", "", ""): 1,
            ("Regulation", "", "low"): 8,
            ("Regulation", "true", ""): 8,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cofactor": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "enzyme": 1,
            "evidence": 6,
            "km": 2,
            "ph-opt": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "regulated-by": 1,
            "synonym": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ETHAMLY-RXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 3,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Pathway", "", ""): 1,
            ("Protein", "", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
            ("Reaction", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Reaction", "Chemical-Reactions"), ("Reaction", "Small-Molecule-Reactions")],
        "slots": {
            "dblink": 6,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 1,
            "orphan": 1,
            "parent": 2,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 2,
        },
        "tag": "Reaction",
    },
    "MetaCyc:ETHANOL-AMINE": {
        "embedded_shapes": {
            ("Compound", "", ""): 3,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 3,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 3,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 25,
            ("Regulation", "", "low"): 3,
            ("Regulation", "true", ""): 3,
        },
        "is_class": False,
        "parents": [("Compound", "Primary-Alcohols"), ("Compound", "Primary-Amines")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 12,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "pka1": 1,
            "regulates": 1,
            "synonym": 4,
        },
        "tag": "Compound",
    },
    "MetaCyc:ETOH": {
        "embedded_shapes": {
            ("Compound", "", ""): 3,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 3,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 3,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 33,
            ("Regulation", "", "low"): 3,
            ("Regulation", "true", ""): 3,
        },
        "is_class": False,
        "parents": [
            ("Compound", "Short-Chain-Alcohols"),
            ("Compound", "Short-Chain-Primary-Alcohols"),
        ],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 13,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 6,
        },
        "tag": "Compound",
    },
    "MetaCyc:EUTB-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 39,
            ("Evidence-Code", "true", "full"): 10,
            ("Feature", "", "full"): 9,
            ("Feature", "true", ""): 9,
            ("GO-Term", "true", ""): 9,
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 10,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 9,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 10,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 24,
            ("Publication", "", "full"): 19,
            ("cco", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 21,
            "gene": 1,
            "has-feature": 9,
            "has-go-term": 9,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:EUTC-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 28,
            ("Evidence-Code", "true", "full"): 7,
            ("Feature", "", "full"): 4,
            ("Feature", "true", ""): 4,
            ("GO-Term", "true", ""): 9,
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 5,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 4,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 5,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 14,
            ("Publication", "", "full"): 17,
            ("cco", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 19,
            "gene": 1,
            "has-feature": 4,
            "has-go-term": 9,
            "location": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:FE+2": {
        "embedded_shapes": {
            ("Compound", "", ""): 164,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 438,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 438,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 485,
            ("Regulation", "", "low"): 160,
            ("Regulation", "true", ""): 160,
        },
        "is_class": False,
        "parents": [
            ("Compound", "Divalent-Inorganic-Cations"),
            ("Compound", "Transition-Metal-Cations"),
        ],
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
    "MetaCyc:G7288-MONOMER": {
        "embedded_shapes": {
            ("Evidence-Code", "true", ""): 13,
            ("Evidence-Code", "true", "full"): 4,
            ("Feature", "", "full"): 1,
            ("Feature", "true", ""): 1,
            ("GO-Term", "true", ""): 9,
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 2,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 1,
            ("Publication", "", ""): 4,
            ("Publication", "", "full"): 10,
            ("cco", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 15,
            "gene": 1,
            "has-feature": 1,
            "has-go-term": 9,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "MetaCyc:GDP": {
        "embedded_shapes": {
            ("Compound", "", ""): 26,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 26,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 26,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 240,
            ("Regulation", "", "low"): 26,
            ("Regulation", "true", ""): 26,
        },
        "is_class": False,
        "parents": [("Compound", "All-Nucleosides")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 13,
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
    "MetaCyc:Oxidized-Flavoproteins": {
        "embedded_shapes": {("Protein", "true", ""): 6, ("Reaction", "", ""): 13},
        "is_class": True,
        "parents": [("Protein", "Flavoproteins"), ("Protein", "Modified-Proteins")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "common-name": 1,
            "dblink": 2,
            "parent": 2,
            "subclass": 4,
        },
        "tag": "Protein",
    },
    "MetaCyc:PHMB": {
        "embedded_shapes": {
            ("Compound", "", ""): 97,
            ("Enzymatic-Reaction", "", "low"): 97,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 97,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 97,
            ("Regulation", "", "low"): 97,
            ("Regulation", "true", ""): 97,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cml": 1,
            "common-name": 1,
            "dblink": 3,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "regulates": 1,
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:PWY0-1477": {
        "embedded_shapes": {
            ("Compound", "", ""): 11,
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 2,
            ("Organism", "true", ""): 3,
            ("Organism", "true", "full"): 3,
            ("Organization", "", ""): 3,
            ("Organization", "", "full"): 1,
            ("Pathway", "true", ""): 1,
            ("Person", "", "full"): 2,
            ("Publication", "", "full"): 3,
            ("Reaction", "", ""): 18,
        },
        "is_class": False,
        "parents": [("Pathway", "AMINE-DEG")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 1,
            "evidence": 2,
            "parent": 1,
            "pathway-link": 1,
            "reaction-layout": 5,
            "reaction-list": 1,
            "reaction-ordering": 4,
            "species": 2,
            "taxonomic-range": 1,
        },
        "tag": "Pathway",
    },
    "MetaCyc:RXN-19336": {
        "embedded_shapes": {
            ("Compound", "", ""): 7,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 2,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 4,
            ("Reaction", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Reaction", "Composite-Reactions"), ("Reaction", "Small-Molecule-Reactions")],
        "slots": {
            "credits": 1,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "left": 4,
            "orphan": 1,
            "parent": 2,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "reaction-list": 1,
            "right": 5,
        },
        "tag": "Reaction",
    },
    "MetaCyc:Reduced-Flavoproteins": {
        "embedded_shapes": {
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 5,
            ("Reaction", "", ""): 13,
        },
        "is_class": True,
        "parents": [("Protein", "Flavoproteins")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "common-name": 1,
            "dblink": 2,
            "instance": 1,
            "parent": 1,
            "subclass": 4,
        },
        "tag": "Protein",
    },
    "MetaCyc:STM2461-MONOMER": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:STM2467-MONOMER": {
        "embedded_shapes": {
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 6,
            "gene": 1,
            "molecular-weight-exp": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:STM2468-MONOMER": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "credits": 1,
            "dblink": 9,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:STM2469-MONOMER": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 6,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
}
COMPLEXES = {
    "EcoCyc:CPLX0-7613",
    "EcoCyc:CPLX0-7801",
    "EcoCyc:CPLX0-7835",
    "EcoCyc:CPLX0-7836",
    "EcoCyc:CPLX0-7912",
    "EcoCyc:ETHAMLY-CPLX",
    "MetaCyc:CPLX-9275",
    "MetaCyc:CPLX0-7912",
    "MetaCyc:ETHAMLY-CPLX",
}
MATERIAL_ROLES = {
    "ACETALD": {"is_class": False, "tag": "Compound"},
    "ACETYL-COA": {"is_class": False, "tag": "Compound"},
    "ADENOSYLCOBALAMIN": {"is_class": False, "tag": "Compound"},
    "AMMONIUM": {"is_class": False, "tag": "Compound"},
    "ATP": {"is_class": False, "tag": "Compound"},
    "CO-A": {"is_class": False, "tag": "Compound"},
    "CPD-1829": {"is_class": False, "tag": "Compound"},
    "ETHANOL-AMINE": {"is_class": False, "tag": "Compound"},
    "ETOH": {"is_class": False, "tag": "Compound"},
    "NAD": {"is_class": False, "tag": "Compound"},
    "NADH": {"is_class": False, "tag": "Compound"},
    "Oxidized-Flavoproteins": {"is_class": True, "tag": "Protein"},
    "PPI": {"is_class": False, "tag": "Compound"},
    "PROTON": {"is_class": False, "tag": "Compound"},
    "Pi": {"is_class": False, "tag": "Compound"},
    "Reduced-Flavoproteins": {"is_class": True, "tag": "Protein"},
    "WATER": {"is_class": False, "tag": "Compound"},
}
NATIVE_MEMBERS = [
    "MetaCyc:ALCOHOL-DEHYDROG-RXN",
    "MetaCyc:ACETATEKIN-RXN",
    "MetaCyc:PHOSACETYLTRANS-RXN",
    "MetaCyc:ACETALD-DEHYDROG-RXN",
    "MetaCyc:ETHAMLY-RXN",
]
EXACT_ORDERING = [
    {"predecessors": ["MetaCyc:ETHAMLY-RXN"], "reaction": "MetaCyc:ALCOHOL-DEHYDROG-RXN"},
    {"predecessors": ["MetaCyc:PHOSACETYLTRANS-RXN"], "reaction": "MetaCyc:ACETATEKIN-RXN"},
    {"predecessors": ["MetaCyc:ACETALD-DEHYDROG-RXN"], "reaction": "MetaCyc:PHOSACETYLTRANS-RXN"},
    {"predecessors": ["MetaCyc:ETHAMLY-RXN"], "reaction": "MetaCyc:ACETALD-DEHYDROG-RXN"},
]
EXACT_EQUATIONS = {
    "MetaCyc:ACETALD-DEHYDROG-RXN": {
        "direction": "REVERSIBLE",
        "left": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ACETALD",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CO-A",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:NAD",
                "native_type": "Compound",
            },
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ACETYL-COA",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:NADH",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:PROTON",
                "native_type": "Compound",
            },
        ],
    },
    "MetaCyc:ALCOHOL-DEHYDROG-RXN": {
        "direction": "REVERSIBLE",
        "left": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ETOH",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:NAD",
                "native_type": "Compound",
            },
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ACETALD",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:NADH",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:PROTON",
                "native_type": "Compound",
            },
        ],
    },
    "MetaCyc:ETHAMLY-RXN": {
        "direction": "LEFT-TO-RIGHT",
        "left": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ETHANOL-AMINE",
                "native_type": "Compound",
            }
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:AMMONIUM",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ACETALD",
                "native_type": "Compound",
            },
        ],
    },
    "MetaCyc:RXN-19336": {
        "direction": "PHYSIOL-LEFT-TO-RIGHT",
        "left": [
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ATP",
                "native_type": "Compound",
            },
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CPD-1829",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": True,
                "material": "MetaCyc:Reduced-Flavoproteins",
                "native_type": "Protein",
            },
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:WATER",
                "native_type": "Compound",
            },
        ],
        "right": [
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ADENOSYLCOBALAMIN",
                "native_type": "Compound",
            },
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:PPI",
                "native_type": "Compound",
            },
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:Pi",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": True,
                "material": "MetaCyc:Oxidized-Flavoproteins",
                "native_type": "Protein",
            },
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:PROTON",
                "native_type": "Compound",
            },
        ],
    },
}
EXACT_ACTIVITIES = {
    "MetaCyc:ENZRXN-26156": {
        "enzyme": "MetaCyc:STM2468-MONOMER",
        "reaction": "MetaCyc:ACETATEKIN-RXN",
    },
    "MetaCyc:ENZRXN-26157": {
        "enzyme": "MetaCyc:STM2469-MONOMER",
        "reaction": "MetaCyc:ACETATEKIN-RXN",
    },
    "MetaCyc:ENZRXN-26158": {
        "enzyme": "MetaCyc:STM2461-MONOMER",
        "reaction": "MetaCyc:ALCOHOL-DEHYDROG-RXN",
    },
    "MetaCyc:ENZRXN-26161": {"enzyme": "MetaCyc:CPLX-9275", "reaction": "MetaCyc:RXN-19336"},
    "MetaCyc:ENZRXN0-7425": {
        "enzyme": "MetaCyc:CPLX0-7912",
        "reaction": "MetaCyc:PHOSACETYLTRANS-RXN",
    },
    "MetaCyc:ETHAMLY-ENZRXN": {"enzyme": "MetaCyc:ETHAMLY-CPLX", "reaction": "MetaCyc:ETHAMLY-RXN"},
}
EXACT_COMPONENTS = {
    "EcoCyc:CPLX0-7613": [{"coefficient": 6, "id": "EcoCyc:G7286-MONOMER"}],
    "EcoCyc:CPLX0-7801": [{"coefficient": 3, "id": "EcoCyc:G7271-MONOMER"}],
    "EcoCyc:CPLX0-7835": [{"coefficient": 6, "id": "EcoCyc:G7287-MONOMER"}],
    "EcoCyc:CPLX0-7836": [{"coefficient": 6, "id": "EcoCyc:G7292-MONOMER"}],
    "EcoCyc:CPLX0-7912": [{"coefficient": 2, "id": "EcoCyc:G7288-MONOMER"}],
    "EcoCyc:ETHAMLY-CPLX": [
        {"coefficient": 6, "id": "EcoCyc:EUTB-MONOMER"},
        {"coefficient": 6, "id": "EcoCyc:EUTC-MONOMER"},
    ],
    "MetaCyc:CPLX-9275": [{"coefficient": None, "id": "MetaCyc:STM2467-MONOMER"}],
    "MetaCyc:CPLX0-7912": [{"coefficient": 2, "id": "MetaCyc:G7288-MONOMER"}],
    "MetaCyc:ETHAMLY-CPLX": [
        {"coefficient": 6, "id": "MetaCyc:EUTB-MONOMER"},
        {"coefficient": 6, "id": "MetaCyc:EUTC-MONOMER"},
    ],
}

NODE_ROLES = {
    "native_ethanolamine_compound": ("participants", {"small_molecule", "cofactor"}),
    "native_ethanolamine_compound_class": (
        "participants",
        {"chemical_entity", "cofactor"},
    ),
    "native_ethanolamine_protein_class": ("participants", {"protein"}),
    "native_ethanolamine_protein": ("participants", {"protein"}),
    "native_ethanolamine_complex": ("participants", {"complex"}),
    "native_ethanolamine_activity": ("participants", {"molecular_activity"}),
    "native_ethanolamine_reaction": ("reactions", {"molecular_activity"}),
    "native_ethanolamine_location": ("participants", {"cellular_component"}),
}


def _identity(kind: str) -> tuple[str, str]:
    require(kind in ETHANOLAMINE_KINDS, "unsupported ethanolamine kind")
    return ("META", "MetaCyc") if kind == META_KIND else ("ECOLI", "EcoCyc")


def _source_frame(source: dict, pgdb: str) -> str:
    """Retain the exact bare request syntax of the 63 selected native originals.

    This source kind does not normalize an unacquired id= URL into provenance.
    Earlier typed source request contracts are unchanged.
    """
    keys(source, PROVENANCE, "invalid source provenance fields")
    require(
        all(isinstance(v, str) and bool(v.strip()) for v in source.values()),
        "empty source provenance",
    )
    match = re.fullmatch(
        rf"https://{re.escape(HOST)}/getxml\?{pgdb}:([A-Za-z0-9][A-Za-z0-9_.+\-]*)", source["url"]
    )
    require(match is not None, "requires exact acquired native HTTPS request")
    require(re.fullmatch(r"[0-9a-f]{64}", source["sha256"]) is not None, "invalid provenance hash")
    return match[1]


def _envelope(body: bytes, source: dict, kind: str):
    pgdb, prefix = _identity(kind)
    frame = _source_frame(source, pgdb)
    ident = prefix + ":" + frame
    require(ident in PROFILES, "outside the reviewed ethanolamine frame scope")
    require(source["version"] == "27.0", "unsupported ethanolamine source release")
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
        "ethanolamine envelope mismatch",
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
            "dblink-db": "NCBI-TAXONOMY-DB",
            "dblink-oid": "511145",
            "dblink-relationship": "unification",
            "dblink-URL": "http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=511145",
        }
        require(
            not link.attrib and Counter(n.tag for n in link) == Counter(wanted.keys()),
            "invalid ECOLI database taxon link",
        )
        require(all(scalar(link, k) == v for k, v in wanted.items()), "wrong ECOLI taxon identity")
    attributes(entity, frame, pgdb, PROFILES[ident]["tag"], PROFILES[ident]["is_class"])
    require(
        Counter(n.tag for n in entity) == PROFILES[ident]["slots"],
        "incomplete or unsupported complete native slots",
    )
    parents = []
    for wrapper in entity.findall("parent"):
        blank(wrapper)
        require(not wrapper.attrib and len(wrapper) == 1, "invalid direct parent")
        node = wrapper[0]
        parent = _literal_ref(node, pgdb, entity.tag, is_class=True)
        parents.append((node.tag, parent["id"].split(":", 1)[1]))
    require(parents == PROFILES[ident]["parents"], "native parent/type scope mismatch")
    shapes = Counter()
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
        require(node.tag in _NATIVE_OBJECT_TAGS, "unknown embedded native object type")
        expected_attrs = {"frameid", "orgid"}
        if "ID" in node.attrib:
            expected_attrs |= {"ID", "detail"}
            require(node.get("detail") in {"low", "full"}, "invalid embedded detail")
        else:
            expected_attrs.add("resource")
        if "class" in node.attrib:
            require(node.get("class") == "true", "invalid embedded class flag")
            expected_attrs.add("class")
        require(set(node.attrib) == expected_attrs, "invalid embedded identity attributes")
        if node is not entity:
            shapes[(node.tag, node.get("class", ""), node.get("detail", ""))] += 1
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
    require(shapes == PROFILES[ident]["embedded_shapes"], "incomplete embedded object shapes")
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
    return {
        "id": ("MetaCyc:" if pgdb == "META" else "EcoCyc:") + frame,
        "native_type": tag,
        "is_class": is_class,
    }


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
        require(compartment is None, "ethanolamine equation materials are unlocated")
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
    pgdb = "META" if ident.startswith("MetaCyc:") else "ECOLI"
    common = entity.findall("common-name")
    require(len(common) <= 1, "duplicate common name")
    label = name(common[0], "") if common else frame
    label_origin = "direct_common_name" if common else "native_frame_id"
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
            direction in {"REVERSIBLE", "LEFT-TO-RIGHT", "PHYSIOL-LEFT-TO-RIGHT"},
            "invalid native reaction direction",
        )
        require(
            {**result["sides"], "direction": direction} == EXACT_EQUATIONS[ident],
            "native equation differs from the bounded original scope",
        )
        result["reaction_direction"] = direction
    if entity.tag == "Enzymatic-Reaction":
        for slot, tag in (("enzyme", "Protein"), ("reaction", "Reaction")):
            wrapper = one(entity, slot)
            blank(wrapper)
            require(not wrapper.attrib and len(wrapper) == 1, "invalid native activity link")
            result[slot] = ref_node(wrapper[0], pgdb, tag)["id"]
            require(result[slot] == EXACT_ACTIVITIES[ident][slot], "wrong exact activity link")
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
            len({r["id"] for r in components}) == len(components)
            and components == EXACT_COMPONENTS[ident],
            "unsupported or duplicate native complex components",
        )
        result["components"] = components
    if entity.tag == "Pathway":
        listing = one(entity, "reaction-list")
        blank(listing)
        require(not listing.attrib, "attributed native reaction list")
        members = [ref_node(n, pgdb, "Reaction")["id"] for n in listing]
        require(
            members == NATIVE_MEMBERS,
            "wrong complete PWY0-1477 native membership",
        )
        result["reaction_list"] = members
        ordering = []
        for wrapper in entity.findall("reaction-ordering"):
            blank(wrapper)
            require(
                not wrapper.attrib
                and Counter(n.tag for n in wrapper)
                == Counter({"Reaction": 1, "predecessor-reactions": 1}),
                "invalid pathway ordering wrapper",
            )
            reaction = ref_node(one(wrapper, "Reaction"), pgdb, "Reaction")["id"]
            predecessors = one(wrapper, "predecessor-reactions")
            blank(predecessors)
            require(
                not predecessors.attrib and len(predecessors) == 1,
                "invalid pathway predecessor list",
            )
            ordering.append(
                {
                    "reaction": reaction,
                    "predecessors": [ref_node(n, pgdb, "Reaction")["id"] for n in predecessors],
                }
            )
        require(ordering == EXACT_ORDERING, "wrong exact pathway reaction ordering")
        result["reaction_ordering"] = ordering
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


def ethanolamine_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(entry, PROVENANCE | {"key", "kind", "path"}, "invalid ethanolamine manifest")
    require(isinstance(entry["key"], str) and bool(entry["key"].strip()), "empty source key")
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    result = {
        **source,
        "kind": entry["kind"],
        FIELD: document(original_path(entry, cache_dir).read_bytes(), source, entry["kind"]),
    }
    validate_ethanolamine_metadata(result)
    return result


def validate_ethanolamine_metadata(metadata: dict) -> None:
    keys(metadata, PROVENANCE | {"kind", FIELD}, "invalid ethanolamine metadata")
    source = {k: metadata[k] for k in PROVENANCE_ORDER}
    native = metadata[FIELD]
    keys(
        native,
        {"id", "original_base64", "root_attributes", "metadata_xml", "projection"},
        "incomplete original ethanolamine document",
    )
    expected = document(original_bytes(native["original_base64"]), source, metadata["kind"])
    require(
        json.dumps(native, sort_keys=True) == json.dumps(expected, sort_keys=True),
        "ethanolamine projection does not match original bytes",
    )


def ethanolamine_term(metadata: dict, source_key: str) -> tuple[str, dict]:
    validate_ethanolamine_metadata(metadata)
    native = metadata[FIELD]["projection"]
    tag, ident = native["native_type"], native["id"]
    role = {
        "Compound": "compound_class" if native["is_class"] else "compound",
        "Protein": "protein_class"
        if native["is_class"]
        else ("complex" if ident in COMPLEXES else "protein"),
        "Enzymatic-Reaction": "activity",
        "Reaction": "reaction",
        "Pathway": "pathway",
        "cco": "location",
    }[tag]
    return ident, {
        "label": native["label"],
        "synonyms": native["synonyms"],
        "source": source_key,
        "entity_type": "native_pathway" if role == "pathway" else "native_ethanolamine_" + role,
        "label_kind": "canonical"
        if native["label_origin"] == "direct_common_name"
        else "source_context",
    }


def validate_ethanolamine_assertions(sources: dict, claims: list[tuple[str, str]]) -> None:
    """Reject downgrades/conflicting original owners before selection and on load."""
    assertions = {}
    for metadata in sources.values():
        kind = metadata.get("kind")
        if kind in ETHANOLAMINE_KINDS:
            validate_ethanolamine_metadata(metadata)
            native = metadata[FIELD]
            ident = native["id"]
            assertion = json.dumps(native, sort_keys=True), metadata["version"], kind
            if ident in assertions:
                require(assertions[ident] == assertion, "conflicting complete native identity")
            assertions[ident] = assertion
        elif FIELD in metadata:
            raise ValueError("ethanolamine metadata requires its exact typed kind")
        url = urlsplit(metadata.get("url", ""))
        if url.hostname in {
            HOST,
            "biocyc.org",
            "www.biocyc.org",
            "metacyc.org",
            "www.metacyc.org",
            "ecocyc.org",
            "www.ecocyc.org",
        }:
            params = parse_qs(url.query)
            tokens = [v for name in ("id", "object") for v in params.get(name, [])]
            # Rejection recognition also preserves literal plus signs in legacy values.
            tokens += [
                unquote(value)
                for field in url.query.split("&")
                for key, sep, value in [field.partition("=")]
                if sep and unquote(key) in {"id", "object"}
            ]
            # Native receipts also use /getxml?META:FRAME (or ECOLI:FRAME).
            # Treat only the complete literal query on that HTTP(S) endpoint as
            # a bare request token. The exact profile lookup below must not turn
            # arbitrary query values, suffixes or unrelated paths into identities.
            if (
                url.scheme in {"http", "https"}
                and url.path == "/getxml"
                and unquote(url.query).startswith(("META:", "ECOLI:"))
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
                    expected = META_KIND if ident.startswith("MetaCyc:") else ECO_KIND
                    require(kind == expected, "complete native identity requires its typed source")
    for ident, source in claims:
        if ident in PROFILES:
            metadata = sources[source]
            expected = META_KIND if ident.startswith("MetaCyc:") else ECO_KIND
            require(
                metadata.get("kind") == expected and metadata[FIELD]["id"] == ident,
                "claimed native identity requires its complete typed owner",
            )
