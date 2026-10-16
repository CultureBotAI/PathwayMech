"""Bounded complete source originals for the native METH-ACETATE-PWY graph.

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

KIND = "metacyc-acetate-methanogenesis-xml"
ACETATE_METHANOGENESIS_KINDS = {KIND}
FIELD = "native_acetate_methanogenesis"
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
    "MetaCyc:1.2.7.4-RXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Enzymatic-Reaction", "", "low"): 3,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Pathway", "", ""): 4,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 3,
            ("Protein", "true", ""): 2,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 7,
            ("Reaction", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Reaction", "Protein-Modification-Reactions")],
        "slots": {
            "credits": 1,
            "dblink": 23,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 3,
            "orphan": 1,
            "parent": 1,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 3,
        },
        "tag": "Reaction",
    },
    "MetaCyc:ACET": {
        "embedded_shapes": {
            ("Compound", "", ""): 15,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 10,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 10,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 225,
            ("Regulation", "", "low"): 10,
            ("Regulation", "true", ""): 10,
        },
        "is_class": False,
        "parents": [("Compound", "Short-Chain-Carboxylates")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 18,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 3,
            "systematic-name": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:ACETATEKIN-RXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Enzymatic-Reaction", "", "low"): 18,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Pathway", "", ""): 17,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 18,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 18,
            ("Reaction", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Reaction", "Chemical-Reactions"), ("Reaction", "Small-Molecule-Reactions")],
        "slots": {
            "credits": 1,
            "dblink": 14,
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
    "MetaCyc:ACETYL-P": {
        "embedded_shapes": {
            ("Compound", "", ""): 2,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 2,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 2,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 15,
            ("Regulation", "", "low"): 2,
            ("Regulation", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Compound", "Acyl-Phosphates")],
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
            "parent": 1,
            "regulates": 1,
            "synonym": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:ACETYLSYNCLTH-RXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Enzymatic-Reaction", "", "low"): 2,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Pathway", "", ""): 2,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 2,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 5,
            ("Reaction", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Reaction", "Protein-Modification-Reactions")],
        "slots": {
            "credits": 1,
            "dblink": 2,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 3,
            "orphan": 1,
            "parent": 1,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 3,
        },
        "tag": "Reaction",
    },
    "MetaCyc:ACKMSARC-MONOMER": {
        "embedded_shapes": {
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:ADP": {
        "embedded_shapes": {
            ("Compound", "", ""): 87,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 84,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 84,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 983,
            ("Regulation", "", "low"): 86,
            ("Regulation", "true", ""): 86,
        },
        "is_class": False,
        "parents": [("Compound", "All-Nucleosides")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 12,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 5,
        },
        "tag": "Compound",
    },
    "MetaCyc:AMMONIUM": {
        "embedded_shapes": {
            ("Compound", "", ""): 69,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 52,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 52,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 488,
            ("Regulation", "", "low"): 51,
            ("Regulation", "true", ""): 51,
        },
        "is_class": False,
        "parents": [("Compound", "Monovalent-Inorganic-Cations")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 9,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:ARSENATE": {
        "embedded_shapes": {
            ("Compound", "", ""): 21,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 21,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 21,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 40,
            ("Regulation", "", "low"): 21,
            ("Regulation", "true", ""): 21,
        },
        "is_class": False,
        "parents": [("Compound", "Inorganic-Anions")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "dblink": 9,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 5,
        },
        "tag": "Compound",
    },
    "MetaCyc:CA+2": {
        "embedded_shapes": {
            ("Compound", "", ""): 214,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", ""): 5,
            ("Enzymatic-Reaction", "", "low"): 301,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 300,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 309,
            ("Regulation", "", "low"): 203,
            ("Regulation", "true", ""): 203,
        },
        "is_class": False,
        "parents": [
            ("Compound", "Alkaline-Earth-Cations"),
            ("Compound", "Divalent-Inorganic-Cations"),
        ],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 9,
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
    "MetaCyc:CARBON-MONOXIDE": {
        "embedded_shapes": {
            ("Compound", "", ""): 40,
            ("Enzymatic-Reaction", "", "low"): 40,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 40,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 63,
            ("Regulation", "", "low"): 40,
            ("Regulation", "true", ""): 40,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "abbrev-name": 1,
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "dblink": 10,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "regulates": 1,
            "synonym": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:CDHAMSARC-MONOMER": {
        "embedded_shapes": {
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 13,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CDHBMSARC-MONOMER": {
        "embedded_shapes": {
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "common-name": 1,
            "component-of": 1,
            "dblink": 5,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CDHCMSARC-MONOMER": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 9,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "pi": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CDHDMSARC-MONOMER": {
        "embedded_shapes": {
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 6,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CDHEMSARC-MONOMER": {
        "embedded_shapes": {
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Protein", "Corrinoid-Fe-S-Proteins"), ("Protein", "Polypeptides")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "component-of": 1,
            "credits": 1,
            "dblink": 10,
            "gene": 1,
            "molecular-weight-seq": 1,
            "parent": 2,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CO+2": {
        "embedded_shapes": {
            ("Compound", "", ""): 173,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 249,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 249,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 259,
            ("Regulation", "", "low"): 168,
            ("Regulation", "true", ""): 168,
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
            "dblink": 9,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPD-8": {
        "embedded_shapes": {
            ("Compound", "true", ""): 2,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Publication", "", "full"): 4,
            ("Reaction", "", ""): 6,
        },
        "is_class": False,
        "parents": [("Compound", "Cofactors"), ("Compound", "Tetrahydropterins")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "citation": 3,
            "cml": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 5,
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
    "MetaCyc:CPD-9": {
        "embedded_shapes": {
            ("Compound", "true", ""): 2,
            ("Evidence-Code", "true", "full"): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 5,
        },
        "is_class": False,
        "parents": [("Compound", "Cofactors"), ("Compound", "Tetrahydropterins")],
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
            "synonym": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:CPLX-322": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("GO-Term", "true", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
            ("cco", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "has-go-term": 1,
            "location": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-441": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-442": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 4,
            ("Protein", "true", ""): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 2,
            "component-of": 1,
            "credits": 1,
            "parent": 1,
            "species": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-443": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 4,
            ("Protein", "true", ""): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 2,
            "component-of": 1,
            "parent": 1,
            "species": 1,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-461": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 4,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "common-name": 1,
            "component": 3,
            "credits": 1,
            "molecular-weight-exp": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CPLX-481": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("GO-Term", "true", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Reaction", "", ""): 1,
            ("cco", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Protein-Complexes")],
        "slots": {
            "catalyzes": 1,
            "comment": 1,
            "has-go-term": 1,
            "location": 1,
            "parent": 1,
            "species": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:CTP": {
        "embedded_shapes": {
            ("Compound", "", ""): 13,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 12,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 12,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 70,
            ("Regulation", "", "low"): 12,
            ("Regulation", "true", ""): 12,
        },
        "is_class": False,
        "parents": [("Compound", "Pyrimidine-ribonucleosides-5-PPP"), ("Compound", "Pyrimidines")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 12,
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
    "MetaCyc:CoI-Corrinoid-Fe-S-proteins": {
        "embedded_shapes": {
            ("Organization", "", ""): 2,
            ("Organization", "", "full"): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 3,
            ("Reaction", "", ""): 6,
        },
        "is_class": True,
        "parents": [
            ("Protein", "Cobalt-I-Corrinoid-Proteins"),
            ("Protein", "Corrinoid-Fe-S-Proteins"),
            ("Protein", "Protein-Complexes"),
        ],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 1,
            "instance": 1,
            "parent": 3,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "MetaCyc:Corrinoids": {
        "embedded_shapes": {
            ("Compound", "true", ""): 4,
            ("Enzymatic-Reaction", "", "low"): 2,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 2,
            ("Reaction", "", ""): 2,
        },
        "is_class": True,
        "parents": [("Compound", "Cyclic-tetrapyrroles")],
        "slots": {
            "cofactors-of": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 2,
            "parent": 1,
            "subclass": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:DIETHYLPYROCARBONATE": {
        "embedded_shapes": {
            ("Compound", "", ""): 38,
            ("Enzymatic-Reaction", "", "low"): 38,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 38,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 38,
            ("Regulation", "", "low"): 38,
            ("Regulation", "true", ""): 38,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cml": 1,
            "common-name": 1,
            "dblink": 8,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "regulates": 1,
            "synonym": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:ENZRXN-18980": {
        "embedded_shapes": {
            ("Compound", "", ""): 3,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", ""): 1,
            ("Evidence-Code", "true", ""): 1,
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
            "cofactor": 3,
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "regulated-by": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-19881": {
        "embedded_shapes": {
            ("Compound", "true", ""): 2,
            ("Protein", "", ""): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cofactor": 2,
            "common-name": 1,
            "enzyme": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-24491": {
        "embedded_shapes": {("Protein", "", ""): 1, ("Reaction", "", ""): 1},
        "is_class": False,
        "parents": [],
        "slots": {"common-name": 1, "enzyme": 1, "physiologically-relevant": 1, "reaction": 1},
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-362": {
        "embedded_shapes": {
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Reaction", "", ""): 1,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "enzyme": 1,
            "evidence": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "synonym": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:ENZRXN-481": {
        "embedded_shapes": {
            ("Compound", "", ""): 21,
            ("Enzymatic-Reaction", "", ""): 2,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Reaction", "", ""): 1,
            ("Regulation", "", "low"): 2,
            ("Regulation", "true", ""): 2,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "alternative-cofactor": 3,
            "alternative-substrate": 6,
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
    "MetaCyc:ENZRXN-482": {
        "embedded_shapes": {
            ("Compound", "", ""): 7,
            ("Enzymatic-Reaction", "", ""): 4,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Reaction", "", ""): 1,
            ("Regulation", "", "low"): 4,
            ("Regulation", "true", ""): 4,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "alternative-cofactor": 1,
            "cofactor": 1,
            "comment": 1,
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
    "MetaCyc:ENZRXN-541": {
        "embedded_shapes": {("Protein", "", ""): 1, ("Reaction", "", ""): 1},
        "is_class": False,
        "parents": [],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "enzyme": 1,
            "physiologically-relevant": 1,
            "reaction": 1,
            "reaction-direction": 1,
            "synonym": 1,
        },
        "tag": "Enzymatic-Reaction",
    },
    "MetaCyc:GTP": {
        "embedded_shapes": {
            ("Compound", "", ""): 41,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 40,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 40,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 132,
            ("Regulation", "", "low"): 41,
            ("Regulation", "true", ""): 41,
        },
        "is_class": False,
        "parents": [("Compound", "All-Nucleosides"), ("Compound", "Purine-ribonucleosides-5-PPP")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "cofactors-of": 1,
            "common-name": 1,
            "dblink": 12,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:ITP": {
        "embedded_shapes": {
            ("Compound", "", ""): 6,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 5,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 5,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 11,
            ("Regulation", "", "low"): 5,
            ("Regulation", "true", ""): 5,
        },
        "is_class": False,
        "parents": [("Compound", "All-Nucleosides"), ("Compound", "Purine-ribonucleosides-5-PPP")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
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
            "systematic-name": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:K+": {
        "embedded_shapes": {
            ("Compound", "", ""): 132,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 159,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 159,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 181,
            ("Regulation", "", "low"): 118,
            ("Regulation", "true", ""): 118,
        },
        "is_class": False,
        "parents": [
            ("Compound", "Alkali-Metal-Cations"),
            ("Compound", "Monovalent-Inorganic-Cations"),
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
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:METH-ACETATE-PWY": {
        "embedded_shapes": {
            ("Compound", "", ""): 15,
            ("Evidence-Code", "true", ""): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Organism", "true", ""): 8,
            ("Organism", "true", "full"): 8,
            ("Organization", "", ""): 3,
            ("Organization", "", "full"): 2,
            ("Pathway", "", ""): 5,
            ("Pathway", "true", ""): 1,
            ("Person", "", ""): 1,
            ("Person", "", "full"): 2,
            ("Protein", "true", ""): 2,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 22,
        },
        "is_class": False,
        "parents": [("Pathway", "METHANOGENESIS")],
        "slots": {
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "evidence": 1,
            "in-pathway": 1,
            "parent": 1,
            "pathway-link": 3,
            "reaction-layout": 6,
            "reaction-list": 1,
            "reaction-ordering": 5,
            "species": 7,
            "super-pathways": 1,
            "synonym": 4,
            "taxonomic-range": 1,
        },
        "tag": "Pathway",
    },
    "MetaCyc:MTRMBARK-RXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Enzymatic-Reaction", "", "low"): 2,
            ("Evidence-Code", "true", "full"): 1,
            ("Pathway", "", ""): 2,
            ("Protein", "", ""): 2,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 2,
            ("Reaction", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Reaction", "Chemical-Reactions"), ("Reaction", "Small-Molecule-Reactions")],
        "slots": {
            "dblink": 1,
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
    "MetaCyc:Methylated-corrinoid-Fe-S-Proteins": {
        "embedded_shapes": {
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Person", "", "full"): 1,
            ("Protein", "true", ""): 2,
            ("Reaction", "", ""): 6,
        },
        "is_class": True,
        "parents": [
            ("Protein", "Corrinoid-Fe-S-Proteins"),
            ("Protein", "Methyl-Cobalt-III-Corrinoid-Proteins"),
        ],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "comment": 1,
            "common-name": 1,
            "credits": 1,
            "dblink": 2,
            "parent": 2,
            "synonym": 3,
        },
        "tag": "Protein",
    },
    "MetaCyc:NI+2": {
        "embedded_shapes": {
            ("Compound", "", ""): 93,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 122,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 122,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 132,
            ("Regulation", "", "low"): 90,
            ("Regulation", "true", ""): 90,
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
            "dblink": 8,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 2,
            "regulates": 1,
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:PHENYLGLYOXAL": {
        "embedded_shapes": {
            ("Compound", "", ""): 8,
            ("Enzymatic-Reaction", "", "low"): 8,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 8,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 8,
            ("Regulation", "", "low"): 8,
            ("Regulation", "true", ""): 8,
        },
        "is_class": False,
        "parents": [],
        "slots": {
            "cml": 1,
            "common-name": 1,
            "dblink": 7,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "regulates": 1,
            "synonym": 6,
        },
        "tag": "Compound",
    },
    "MetaCyc:PHOSACETYLTRANS-RXN": {
        "embedded_shapes": {
            ("Compound", "", ""): 4,
            ("Enzymatic-Reaction", "", "low"): 19,
            ("Evidence-Code", "true", "full"): 1,
            ("Pathway", "", ""): 16,
            ("Protein", "", ""): 19,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 19,
            ("Reaction", "true", ""): 2,
        },
        "is_class": False,
        "parents": [("Reaction", "Chemical-Reactions"), ("Reaction", "Small-Molecule-Reactions")],
        "slots": {
            "dblink": 12,
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
    "MetaCyc:PROPIONATE": {
        "embedded_shapes": {
            ("Compound", "", ""): 7,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 7,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 7,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 25,
            ("Regulation", "", "low"): 7,
            ("Regulation", "true", ""): 7,
        },
        "is_class": False,
        "parents": [("Compound", "Short-Chain-234-Saturated-Fatty-Acids")],
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
            "synonym": 4,
        },
        "tag": "Compound",
    },
    "MetaCyc:PTAMSARC-MONOMER": {
        "embedded_shapes": {
            ("Enzymatic-Reaction", "", "low"): 1,
            ("GO-Term", "true", ""): 1,
            ("Gene", "", ""): 1,
            ("Organism", "true", ""): 1,
            ("Organism", "true", "full"): 1,
            ("Protein", "", ""): 1,
            ("Protein", "true", ""): 1,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 1,
            ("cco", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Protein", "Polypeptides")],
        "slots": {
            "catalyzes": 1,
            "gene": 1,
            "has-go-term": 1,
            "location": 1,
            "molecular-weight-seq": 1,
            "parent": 1,
            "species": 1,
            "synonym": 1,
        },
        "tag": "Protein",
    },
    "MetaCyc:RXN-12908": {
        "embedded_shapes": {
            ("Compound", "", ""): 3,
            ("Enzymatic-Reaction", "", "low"): 1,
            ("Evidence-Code", "true", "full"): 1,
            ("Organization", "", ""): 1,
            ("Organization", "", "full"): 1,
            ("Pathway", "", ""): 1,
            ("Person", "", "full"): 1,
            ("Protein", "", ""): 2,
            ("Protein", "true", ""): 2,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 2,
            ("Reaction", "true", ""): 1,
        },
        "is_class": False,
        "parents": [("Reaction", "Protein-Modification-Reactions")],
        "slots": {
            "credits": 1,
            "dblink": 1,
            "ec-number": 1,
            "enzymatic-reaction": 1,
            "enzymes-not-used": 1,
            "gibbs-0": 1,
            "in-pathway": 1,
            "left": 2,
            "orphan": 1,
            "parent": 1,
            "physiologically-relevant": 1,
            "reaction-direction": 1,
            "right": 3,
        },
        "tag": "Reaction",
    },
    "MetaCyc:SULFATE": {
        "embedded_shapes": {
            ("Compound", "", ""): 36,
            ("Compound", "true", ""): 1,
            ("Enzymatic-Reaction", "", "low"): 13,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 13,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 99,
            ("Regulation", "", "low"): 13,
            ("Regulation", "true", ""): 13,
        },
        "is_class": False,
        "parents": [("Compound", "Inorganic-Anions")],
        "slots": {
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "cml": 1,
            "common-name": 1,
            "component-of": 1,
            "dblink": 9,
            "gibbs-0": 1,
            "inchi": 1,
            "inchi-key": 1,
            "molecular-weight": 1,
            "monoisotopic-mw": 1,
            "parent": 1,
            "regulates": 1,
            "synonym": 6,
            "systematic-name": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:TTP": {
        "embedded_shapes": {
            ("Compound", "", ""): 17,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 17,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 17,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 24,
            ("Regulation", "", "low"): 17,
            ("Regulation", "true", ""): 17,
        },
        "is_class": False,
        "parents": [
            ("Compound", "Pyrimidine-deoxyribonucleosides-5-PPP"),
            ("Compound", "Pyrimidines"),
        ],
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
            "synonym": 3,
            "systematic-name": 1,
        },
        "tag": "Compound",
    },
    "MetaCyc:UTP": {
        "embedded_shapes": {
            ("Compound", "", ""): 27,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", "low"): 27,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 27,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 51,
            ("Regulation", "", "low"): 27,
            ("Regulation", "true", ""): 27,
        },
        "is_class": False,
        "parents": [("Compound", "Pyrimidine-ribonucleosides-5-PPP"), ("Compound", "Pyrimidines")],
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
            "synonym": 3,
        },
        "tag": "Compound",
    },
    "MetaCyc:ZN+2": {
        "embedded_shapes": {
            ("Compound", "", ""): 368,
            ("Compound", "true", ""): 2,
            ("Enzymatic-Reaction", "", ""): 6,
            ("Enzymatic-Reaction", "", "low"): 578,
            ("Evidence-Code", "true", "full"): 1,
            ("Protein", "", ""): 578,
            ("Publication", "", "full"): 1,
            ("Reaction", "", ""): 592,
            ("Regulation", "", "low"): 363,
            ("Regulation", "true", ""): 363,
        },
        "is_class": False,
        "parents": [
            ("Compound", "Divalent-Inorganic-Cations"),
            ("Compound", "Post-Transition-Metal-Cations"),
        ],
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
            "synonym": 3,
        },
        "tag": "Compound",
    },
}
COMPLEXES = {
    "MetaCyc:CPLX-322",
    "MetaCyc:CPLX-441",
    "MetaCyc:CPLX-442",
    "MetaCyc:CPLX-443",
    "MetaCyc:CPLX-461",
    "MetaCyc:CPLX-481",
}
MATERIAL_ROLES = {
    "ACET": {"is_class": False, "tag": "Compound"},
    "ACETYL-COA": {"is_class": False, "tag": "Compound"},
    "ACETYL-P": {"is_class": False, "tag": "Compound"},
    "ADP": {"is_class": False, "tag": "Compound"},
    "ATP": {"is_class": False, "tag": "Compound"},
    "CARBON-DIOXIDE": {"is_class": False, "tag": "Compound"},
    "CARBON-MONOXIDE": {"is_class": False, "tag": "Compound"},
    "CO-A": {"is_class": False, "tag": "Compound"},
    "CPD-8": {"is_class": False, "tag": "Compound"},
    "CPD-9": {"is_class": False, "tag": "Compound"},
    "CoI-Corrinoid-Fe-S-proteins": {"is_class": True, "tag": "Protein"},
    "CoM": {"is_class": False, "tag": "Compound"},
    "Me-CoM": {"is_class": False, "tag": "Compound"},
    "Methylated-corrinoid-Fe-S-Proteins": {"is_class": True, "tag": "Protein"},
    "Oxidized-ferredoxins": {"is_class": True, "tag": "Protein"},
    "PROTON": {"is_class": False, "tag": "Compound"},
    "Pi": {"is_class": False, "tag": "Compound"},
    "Reduced-ferredoxins": {"is_class": True, "tag": "Protein"},
    "WATER": {"is_class": False, "tag": "Compound"},
}
NATIVE_MEMBERS = {
    "1.2.7.4-RXN",
    "ACETATEKIN-RXN",
    "ACETYLSYNCLTH-RXN",
    "MTRMBARK-RXN",
    "PHOSACETYLTRANS-RXN",
    "RXN-12908",
}
EXACT_EQUATIONS = {
    "MetaCyc:1.2.7.4-RXN": {
        "direction": "REVERSIBLE",
        "left": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CARBON-MONOXIDE",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:WATER",
                "native_type": "Compound",
            },
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": True,
                "material": "MetaCyc:Oxidized-ferredoxins",
                "native_type": "Protein",
            },
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CARBON-DIOXIDE",
                "native_type": "Compound",
            },
            {
                "coefficient": 2,
                "compartment": None,
                "is_class": True,
                "material": "MetaCyc:Reduced-ferredoxins",
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
    "MetaCyc:ACETATEKIN-RXN": {
        "direction": "REVERSIBLE",
        "left": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ATP",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ACET",
                "native_type": "Compound",
            },
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ADP",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ACETYL-P",
                "native_type": "Compound",
            },
        ],
    },
    "MetaCyc:ACETYLSYNCLTH-RXN": {
        "direction": "REVERSIBLE",
        "left": [
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
                "is_class": True,
                "material": "MetaCyc:CoI-Corrinoid-Fe-S-proteins",
                "native_type": "Protein",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:PROTON",
                "native_type": "Compound",
            },
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CARBON-MONOXIDE",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": True,
                "material": "MetaCyc:Methylated-corrinoid-Fe-S-Proteins",
                "native_type": "Protein",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CO-A",
                "native_type": "Compound",
            },
        ],
    },
    "MetaCyc:MTRMBARK-RXN": {
        "direction": "REVERSIBLE",
        "left": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:Me-CoM",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CPD-8",
                "native_type": "Compound",
            },
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CPD-9",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CoM",
                "native_type": "Compound",
            },
        ],
    },
    "MetaCyc:PHOSACETYLTRANS-RXN": {
        "direction": "REVERSIBLE",
        "left": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:Pi",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ACETYL-COA",
                "native_type": "Compound",
            },
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:ACETYL-P",
                "native_type": "Compound",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CO-A",
                "native_type": "Compound",
            },
        ],
    },
    "MetaCyc:RXN-12908": {
        "direction": "REVERSIBLE",
        "left": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": True,
                "material": "MetaCyc:Methylated-corrinoid-Fe-S-Proteins",
                "native_type": "Protein",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CPD-8",
                "native_type": "Compound",
            },
        ],
        "right": [
            {
                "coefficient": None,
                "compartment": None,
                "is_class": True,
                "material": "MetaCyc:CoI-Corrinoid-Fe-S-proteins",
                "native_type": "Protein",
            },
            {
                "coefficient": None,
                "compartment": None,
                "is_class": False,
                "material": "MetaCyc:CPD-9",
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
}
EXACT_ACTIVITIES = {
    "MetaCyc:ENZRXN-18980": {"enzyme": "MetaCyc:CPLX-443", "reaction": "MetaCyc:1.2.7.4-RXN"},
    "MetaCyc:ENZRXN-19881": {"enzyme": "MetaCyc:CPLX-442", "reaction": "MetaCyc:RXN-12908"},
    "MetaCyc:ENZRXN-24491": {
        "enzyme": "MetaCyc:CDHCMSARC-MONOMER",
        "reaction": "MetaCyc:ACETYLSYNCLTH-RXN",
    },
    "MetaCyc:ENZRXN-362": {"enzyme": "MetaCyc:CPLX-322", "reaction": "MetaCyc:MTRMBARK-RXN"},
    "MetaCyc:ENZRXN-481": {"enzyme": "MetaCyc:CPLX-441", "reaction": "MetaCyc:ACETATEKIN-RXN"},
    "MetaCyc:ENZRXN-482": {
        "enzyme": "MetaCyc:PTAMSARC-MONOMER",
        "reaction": "MetaCyc:PHOSACETYLTRANS-RXN",
    },
    "MetaCyc:ENZRXN-541": {"enzyme": "MetaCyc:CPLX-481", "reaction": "MetaCyc:MTRMBARK-RXN"},
}
EXACT_COMPONENTS = {
    "MetaCyc:CPLX-322": [],
    "MetaCyc:CPLX-441": [{"coefficient": 2, "id": "MetaCyc:ACKMSARC-MONOMER"}],
    "MetaCyc:CPLX-442": [
        {"coefficient": 1, "id": "MetaCyc:CDHDMSARC-MONOMER"},
        {"coefficient": 1, "id": "MetaCyc:CDHEMSARC-MONOMER"},
    ],
    "MetaCyc:CPLX-443": [
        {"coefficient": 2, "id": "MetaCyc:CDHAMSARC-MONOMER"},
        {"coefficient": 2, "id": "MetaCyc:CDHBMSARC-MONOMER"},
    ],
    "MetaCyc:CPLX-461": [
        {"coefficient": 4, "id": "MetaCyc:CPLX-443"},
        {"coefficient": 8, "id": "MetaCyc:CPLX-442"},
        {"coefficient": 8, "id": "MetaCyc:CDHCMSARC-MONOMER"},
    ],
    "MetaCyc:CPLX-481": [],
}
NODE_ROLES = {
    "native_acetate_methanogenesis_compound": ("participants", {"small_molecule", "cofactor"}),
    "native_acetate_methanogenesis_compound_class": (
        "participants",
        {"chemical_entity", "cofactor"},
    ),
    "native_acetate_methanogenesis_protein_class": ("participants", {"protein"}),
    "native_acetate_methanogenesis_protein": ("participants", {"protein"}),
    "native_acetate_methanogenesis_complex": ("participants", {"complex"}),
    "native_acetate_methanogenesis_activity": ("participants", {"molecular_activity"}),
    "native_acetate_methanogenesis_reaction": ("reactions", {"molecular_activity"}),
}


def _identity(kind: str) -> tuple[str, str]:
    require(kind in ACETATE_METHANOGENESIS_KINDS, "unsupported acetate_methanogenesis kind")
    return "META", "MetaCyc"


def _source_frame(source: dict) -> str:
    """Retain the exact bare request syntax of all 52 selected acquisition receipts.

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
    require(ident in PROFILES, "outside the reviewed acetate_methanogenesis frame scope")
    require(source["version"] == "27.0", "unsupported acetate_methanogenesis source release")
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
        "acetate_methanogenesis envelope mismatch",
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
        require(compartment is None, "acetate pathway equation materials are unlocated")
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
            len(members) == 6 and set(members) == {prefix + ":" + f for f in NATIVE_MEMBERS},
            "wrong complete METH-ACETATE-PWY native membership",
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


def acetate_methanogenesis_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(entry, PROVENANCE | {"key", "kind", "path"}, "invalid acetate_methanogenesis manifest")
    require(isinstance(entry["key"], str) and bool(entry["key"].strip()), "empty source key")
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    result = {
        **source,
        "kind": entry["kind"],
        FIELD: document(original_path(entry, cache_dir).read_bytes(), source, entry["kind"]),
    }
    validate_acetate_methanogenesis_metadata(result)
    return result


def validate_acetate_methanogenesis_metadata(metadata: dict) -> None:
    keys(metadata, PROVENANCE | {"kind", FIELD}, "invalid acetate_methanogenesis metadata")
    source = {k: metadata[k] for k in PROVENANCE_ORDER}
    native = metadata[FIELD]
    keys(
        native,
        {"id", "original_base64", "root_attributes", "metadata_xml", "projection"},
        "incomplete original acetate_methanogenesis document",
    )
    expected = document(original_bytes(native["original_base64"]), source, metadata["kind"])
    require(
        json.dumps(native, sort_keys=True) == json.dumps(expected, sort_keys=True),
        "acetate_methanogenesis projection does not match original bytes",
    )


def acetate_methanogenesis_term(metadata: dict, source_key: str) -> tuple[str, dict]:
    validate_acetate_methanogenesis_metadata(metadata)
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
        "entity_type": "native_pathway"
        if role == "pathway"
        else "native_acetate_methanogenesis_" + role,
        "label_kind": "canonical"
        if native["label_origin"] == "direct_common_name"
        else "source_context",
    }


def validate_acetate_methanogenesis_assertions(
    sources: dict, claims: list[tuple[str, str]]
) -> None:
    """Reject downgrades/conflicting original owners before selection and on load."""
    assertions = {}
    for metadata in sources.values():
        kind = metadata.get("kind")
        if kind in ACETATE_METHANOGENESIS_KINDS:
            validate_acetate_methanogenesis_metadata(metadata)
            native = metadata[FIELD]
            ident = native["id"]
            assertion = json.dumps(native, sort_keys=True), metadata["version"], kind
            if ident in assertions:
                require(assertions[ident] == assertion, "conflicting complete native identity")
            assertions[ident] = assertion
        elif FIELD in metadata:
            raise ValueError("acetate_methanogenesis metadata requires its exact typed kind")
        url = urlsplit(metadata.get("url", ""))
        if url.hostname in {HOST, "biocyc.org", "www.biocyc.org", "metacyc.org", "www.metacyc.org"}:
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
