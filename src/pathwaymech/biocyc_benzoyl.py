"""Closed native benzoyl source shapes, with exact original-byte reconstruction.

These profiles establish source identity and context, not experimental support
for a catalyst or whole pathway. Existing generic profiles remain unchanged.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_aceto import evidence
from pathwaymech.biocyc_carrier import (
    HOST,
    PROVENANCE,
    PROVENANCE_ORDER,
    _TreeBuilder,
    keys,
    one,
    original_path,
    provenance,
    require,
    scalar,
)
from pathwaymech.biocyc_native_context import (
    activity,
    ancillary,
    attributes,
    blank,
    direct_names,
    integer,
    publication_context,
    ref_node,
    refs,
)
from pathwaymech.biocyc_protein_carrier_reaction import _credits as carrier_credits

HETEROMER_KIND = "metacyc-heteromer-activity-xml"
FERREDOXIN_REACTION_KIND = "metacyc-ferredoxin-reaction-xml"
FERREDOXIN_CLASS_KIND = "metacyc-ferredoxin-class-xml"
HYDROLYTIC_KIND = "metacyc-hydrolytic-composite-xml"
NAMED_REACTION_KIND = "metacyc-named-reaction-xml"
BENZOYL_KINDS = {
    HETEROMER_KIND,
    FERREDOXIN_REACTION_KIND,
    FERREDOXIN_CLASS_KIND,
    HYDROLYTIC_KIND,
    NAMED_REACTION_KIND,
}
FIELD = "native_benzoyl"
FRAMES = {
    HETEROMER_KIND: {"CPLX-1341"},
    FERREDOXIN_REACTION_KIND: {"1.3.99.15-RXN"},
    FERREDOXIN_CLASS_KIND: {"Reduced-ferredoxins", "Oxidized-ferredoxins"},
    HYDROLYTIC_KIND: {"OAHTHAUERA-RXN"},
    NAMED_REACTION_KIND: {"RXN-8032"},
    "constituent": {"RXN-15012", "RXN-15013"},
}
PROTECTED = {"MetaCyc:" + f: k for k in BENZOYL_KINDS for f in FRAMES[k]}
CONSTITUENTS = ["MetaCyc:RXN-15012", "MetaCyc:RXN-15013"]
SLOTS = {
    "CPLX-1341": {
        "parent": 1,
        "catalyzes": 1,
        "credits": 1,
        "comment": 1,
        "species": 1,
        "component": 4,
    },
    "1.3.99.15-RXN": {
        "parent": 2,
        "gibbs-0": 1,
        "reaction-direction": 1,
        "orphan": 1,
        "physiologically-relevant": 1,
        "right": 4,
        "credits": 1,
        "in-pathway": 1,
        "citation": 2,
        "left": 4,
        "enzymatic-reaction": 1,
        "dblink": 3,
        "ec-number": 1,
    },
    "Reduced-ferredoxins": {
        "parent": 1,
        "subclass": 3,
        "instance": 1,
        "credits": 1,
        "unmodified-form": 1,
        "comment": 1,
        "n-name": 1,
        "appears-in-left-side-of": 1,
        "appears-in-right-side-of": 1,
        "synonym": 1,
        "modified-form": 1,
        "dblink": 4,
        "common-name": 1,
    },
    "Oxidized-ferredoxins": {
        "parent": 2,
        "subclass": 2,
        "instance": 1,
        "credits": 1,
        "unmodified-form": 1,
        "comment": 1,
        "n-name": 1,
        "appears-in-left-side-of": 1,
        "appears-in-right-side-of": 1,
        "synonym": 1,
        "dblink": 4,
        "common-name": 1,
    },
    "OAHTHAUERA-RXN": {
        "parent": 2,
        "gibbs-0": 1,
        "reaction-direction": 1,
        "orphan": 1,
        "physiologically-relevant": 1,
        "right": 2,
        "left": 2,
        "enzymatic-reaction": 1,
        "dblink": 3,
        "ec-number": 1,
        "reaction-list": 1,
    },
    "RXN-8032": {
        "parent": 2,
        "gibbs-0": 1,
        "reaction-direction": 1,
        "orphan": 1,
        "physiologically-relevant": 1,
        "right": 2,
        "in-pathway": 1,
        "left": 2,
        "enzymatic-reaction": 1,
        "dblink": 2,
        "ec-number": 1,
        "common-name": 1,
    },
}
for _frame, _right in [("RXN-15012", 1), ("RXN-15013", 2)]:
    SLOTS[_frame] = {
        "parent": 2,
        "gibbs-0": 1,
        "reaction-direction": 1,
        "orphan": 1,
        "physiologically-relevant": 1,
        "right": _right,
        "credits": 1,
        "in-pathway": 1,
        "left": 2,
        "dblink": 3,
    }


def _envelope(body: str, source: dict, kind: str) -> tuple[ET.Element, str]:
    frame = provenance(source, "META")
    require(source["version"] == "27.0" and frame in FRAMES[kind], "unsupported native profile")
    require(
        hashlib.sha256(body.encode("utf-8")).hexdigest() == source["sha256"],
        "complete original differs from source hash",
    )
    root = ET.fromstring(body, parser=ET.XMLParser(target=_TreeBuilder()))
    requested = "META:" + frame
    legacy = f"http://{HOST}:443/"
    require(root.tag == "ptools-xml" and len(root) == 2, "requires one complete native object")
    require(
        root.attrib.keys() == {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        and root.get("ptools-version") == source["version"]
        and root.get("{http://www.w3.org/XML/1998/namespace}base")
        in {source["url"], legacy + "getxml?" + requested},
        "native envelope mismatch",
    )
    meta = one(root, "metadata")
    entity = next(n for n in root if n.tag != "metadata")
    for node in (root, meta, entity):
        blank(node)
    require(
        not meta.attrib
        and sorted(n.tag for n in meta)
        == sorted(["url", "service_name", "query", "num_results", "PGDB"]),
        "invalid complete metadata",
    )
    require(
        scalar(meta, "url") in {legacy, f"https://{HOST}/"}
        and scalar(meta, "service_name") == "getxml"
        and scalar(meta, "query") == requested
        and scalar(meta, "num_results") == "1",
        "native request mismatch",
    )
    db = one(meta, "PGDB")
    blank(db)
    require(
        db.attrib == {"orgid": "META", "version": source["version"]}
        and [n.tag for n in db] == ["species"]
        and scalar(db, "species", True) == "MetaCyc",
        "native database mismatch",
    )
    tag = "Protein" if kind in {HETEROMER_KIND, FERREDOXIN_CLASS_KIND} else "Reaction"
    attributes(entity, frame, "META", tag, kind == FERREDOXIN_CLASS_KIND)
    require(Counter(n.tag for n in entity) == SLOTS[frame], "incomplete native slot inventory")
    for credit in entity.findall("credits"):
        event = (
            "last-curated"
            if kind == HETEROMER_KIND
            else ("revised" if kind == FERREDOXIN_REACTION_KIND else "created")
        )
        require([n.tag for n in credit] == [event], "wrong native credit event")
        # The event has the same complete person/organization shape as the
        # existing created-credit validator. Only its temporary validation
        # copy changes tag; the source body remains exact, including the event.
        validation_copy = copy.deepcopy(credit)
        validation_copy[0].tag = "created"
        carrier_credits(validation_copy)
    for citation in entity.findall("citation"):
        for publication in citation:
            publication_context(publication, "META")
    return entity, frame


def _activities(entity: ET.Element, slot: str, frame: str, expected: dict[str, str]) -> list[dict]:
    wrapper = one(entity, slot)
    blank(wrapper)
    require(not wrapper.attrib and len(wrapper) == len(expected), "activity cardinality mismatch")
    result = []
    for node in wrapper:
        activity(node, "META")
        require(
            all(n.tag in {"enzyme", "reaction", "common-name", "synonym"} for n in node),
            "unsupported linked activity context",
        )
        label, aliases = direct_names(node, node.get("frameid", ""))
        enz = ref_node(one(node, "enzyme")[0], "META", "Protein", local=True)
        rxn = ref_node(one(node, "reaction")[0], "META", "Reaction", local=True)
        activity_id = node.get("frameid")
        require(activity_id in expected, "unexpected activity identity")
        require(
            (enz["id"], rxn["id"])
            == (
                ("MetaCyc:" + frame, "MetaCyc:" + expected[activity_id])
                if slot == "catalyzes"
                else ("MetaCyc:" + expected[activity_id], "MetaCyc:" + frame)
            ),
            "activity enzyme/reaction backlink mismatch",
        )
        result.append(
            {
                "id": "MetaCyc:" + activity_id,
                "enzyme": enz,
                "reaction": rxn,
                "label": label,
                "synonyms": aliases,
            }
        )
    require(len({a["id"] for a in result}) == len(expected), "duplicate activity")
    return result


def _heteromer(entity: ET.Element, frame: str) -> dict:
    core = {"parent", "component", "catalyzes", "species"}
    ancillary(entity, {"credits", "comment"}, core, "META")
    for tag in {"credits", "comment", "species"}:
        one(entity, tag)
    parents = refs(entity, "parent", "META", "Protein", is_class=True)
    require([p["id"] for p in parents] == ["MetaCyc:Protein-Complexes"], "wrong complex parent")
    components = []
    for wrapper in entity.findall("component"):
        blank(wrapper)
        require(
            not wrapper.attrib and [n.tag for n in wrapper] == ["Protein", "coefficient"],
            "invalid heteromer component wrapper",
        )
        target = ref_node(wrapper[0], "META", "Protein")
        coefficient = integer(wrapper[1])
        require(coefficient == 1, "heteromer component requires coefficient one")
        components.append({"entity": target, "coefficient": coefficient})
    require(
        len(components) == 4
        and {c["entity"]["id"] for c in components}
        == {
            "MetaCyc:BCRATHAUERA-MONOMER",
            "MetaCyc:BCRBTHAUERA-MONOMER",
            "MetaCyc:BCRCTHAUER-MONOMER",
            "MetaCyc:BCRDTHAUERA-MONOMER",
        },
        "incomplete, duplicate or wrong heteromer components",
    )
    activities = _activities(entity, "catalyzes", frame, {"ENZRXN-1821": "1.3.99.15-RXN"})
    species = one(entity, "species")
    blank(species)
    require(not species.attrib and len(species) == 1, "invalid complete species wrapper")
    organism = species[0]
    attributes(organism, "TAX-59405", "META", "Organism", True)
    ancillary(organism, {"dblink"}, {"parent", "rank", "synonym", "common-name"}, "META")
    require(
        [p["id"] for p in refs(organism, "parent", "META", "Organism", is_class=True)]
        == ["MetaCyc:TAX-33057"]
        and scalar(organism, "rank") == "species",
        "wrong complex species ancestry",
    )
    taxon_label, taxon_aliases = direct_names(organism, "TAX-59405")
    return {
        "parent_classes": parents,
        "components": components,
        "activities": activities,
        "species": {"id": "MetaCyc:TAX-59405", "label": taxon_label, "synonyms": taxon_aliases},
        "label": activities[0]["label"],
        "synonyms": [],
    }


def _ferredoxin(entity: ET.Element, frame: str) -> dict:
    core = {
        "parent",
        "subclass",
        "instance",
        "common-name",
        "synonym",
        "n-name",
        "unmodified-form",
        "modified-form",
    }
    ancillary(
        entity,
        {"credits", "comment", "appears-in-left-side-of", "appears-in-right-side-of", "dblink"},
        core,
        "META",
    )
    for tag in {
        "credits",
        "comment",
        "n-name",
        "appears-in-left-side-of",
        "appears-in-right-side-of",
    }:
        one(entity, tag)
    reduced = frame == "Reduced-ferredoxins"
    parents = refs(entity, "parent", "META", "Protein", is_class=True)
    require(
        {p["id"] for p in parents}
        == (
            {"MetaCyc:Ferredoxins"}
            if reduced
            else {"MetaCyc:Ferredoxins", "MetaCyc:Modified-Proteins"}
        ),
        "wrong ferredoxin parent profile",
    )
    label, synonyms = direct_names(entity, frame)
    require(
        label == ("a reduced" if reduced else "an oxidized") + " ferredoxin [iron-sulfur] cluster",
        "generic cluster-unit name required",
    )
    require(
        scalar(entity, "n-name", True) == ("reduced" if reduced else "oxidized") + " ferredoxins",
        "wrong ferredoxin n-name",
    )
    subclasses = refs(entity, "subclass", "META", "Protein", is_class=True)
    instances = refs(entity, "instance", "META", "Protein", is_class=False)
    require(
        len(subclasses) == (3 if reduced else 2) and len(instances) == 1,
        "incomplete ferredoxin class members",
    )
    links = {}
    for slot in ("unmodified-form", "modified-form"):
        links[slot] = refs(entity, slot, "META", "Protein", is_class=True)
    require(
        {k: [v["id"] for v in vals] for k, vals in links.items()}
        == {
            "unmodified-form": [
                "MetaCyc:Apo-Ferredoxins" if reduced else "MetaCyc:Reduced-ferredoxins"
            ],
            "modified-form": ["MetaCyc:Oxidized-ferredoxins"] if reduced else [],
        },
        "wrong ferredoxin state counterpart",
    )
    return {
        "parent_classes": parents,
        "subclasses": subclasses,
        "instances": instances,
        "state_links": links,
        "label": label,
        "synonyms": synonyms,
    }


def _reaction(entity: ET.Element, frame: str, kind: str) -> dict:
    core = {
        "parent",
        "left",
        "right",
        "reaction-direction",
        "common-name",
        "reaction-list",
        "in-pathway",
        "enzymatic-reaction",
    }
    ancillary(
        entity,
        {
            "gibbs-0",
            "orphan",
            "physiologically-relevant",
            "credits",
            "citation",
            "dblink",
            "ec-number",
        },
        core,
        "META",
    )
    require(one(entity, "orphan").text == "NO", "unsupported orphan status")
    require(
        one(entity, "physiologically-relevant").text == "true",
        "requires physiological native reaction",
    )
    gibbs = one(entity, "gibbs-0")
    for ev in gibbs:
        evidence(ev, "EV-COMP", publication=True)
    parents = refs(entity, "parent", "META", "Reaction", is_class=True)
    require(
        {p["id"] for p in parents}
        == {
            "MetaCyc:Composite-Reactions"
            if kind == HYDROLYTIC_KIND
            else "MetaCyc:Chemical-Reactions",
            "MetaCyc:Small-Molecule-Reactions",
        },
        "wrong reaction parent profile",
    )
    direction = scalar(entity, "reaction-direction")
    require(
        direction
        == ("PHYSIOL-RIGHT-TO-LEFT" if kind == FERREDOXIN_REACTION_KIND else "REVERSIBLE"),
        "wrong native reaction direction",
    )
    sides = []
    for side in ("left", "right"):
        for wrapper in entity.findall(side):
            blank(wrapper)
            require(
                not wrapper.attrib
                and len(wrapper) in {1, 2}
                and wrapper[0].tag in {"Compound", "Protein"}
                and (len(wrapper) == 1 or wrapper[1].tag == "coefficient"),
                "invalid reaction side wrapper",
            )
            target = wrapper[0]
            value = ref_node(target, "META", target.tag, is_class=target.tag == "Protein")
            coefficient = integer(wrapper[1]) if len(wrapper) == 2 else 1
            sides.append(
                {
                    "side": side,
                    "entity": value,
                    "coefficient": coefficient,
                    "coefficient_explicit": len(wrapper) == 2,
                }
            )
    equations = {
        "1.3.99.15-RXN": (
            [
                ("CYCLOHEXA-15-DIENE-1-CARBONYL-COA", 1),
                ("Oxidized-ferredoxins", 2),
                ("ADP", 2),
                ("Pi", 2),
            ],
            [("BENZOYLCOA", 1), ("Reduced-ferredoxins", 2), ("ATP", 2), ("WATER", 2)],
        ),
        "OAHTHAUERA-RXN": (
            [("6-OXOCYCLOHEX-1-ENE-1-CARBONYL-COA", 1), ("WATER", 2)],
            [("PROTON", 1), ("3-HYDROXYPIMELYL-COA", 1)],
        ),
        "RXN-15012": (
            [("6-OXOCYCLOHEX-1-ENE-1-CARBONYL-COA", 1), ("WATER", 1)],
            [("CPD-15900", 1)],
        ),
        "RXN-15013": (
            [("CPD-15900", 1), ("WATER", 1)],
            [("3-HYDROXYPIMELYL-COA", 1), ("PROTON", 1)],
        ),
        "RXN-8032": (
            [("3-OXOPIMELOYL-COA", 1), ("CO-A", 1)],
            [("GLUTARYL-COA", 1), ("ACETYL-COA", 1)],
        ),
    }
    for side, expected in zip(("left", "right"), equations[frame], strict=True):
        observed = [
            (s["entity"]["id"].split(":", 1)[1], s["coefficient"])
            for s in sides
            if s["side"] == side
        ]
        require(Counter(observed) == Counter(expected), "equation/coefficient profile mismatch")
    for s in sides:
        carrier = s["entity"]["id"] in {
            "MetaCyc:Reduced-ferredoxins",
            "MetaCyc:Oxidized-ferredoxins",
        }
        require(
            s["entity"]["native_type"] == ("Protein" if carrier else "Compound"),
            "wrong material native type",
        )
        require(s["coefficient_explicit"] == (s["coefficient"] != 1), "wrong coefficient scope")
    memberships = []
    for wrapper in entity.findall("in-pathway"):
        blank(wrapper)
        require(not wrapper.attrib and len(wrapper), "invalid membership wrapper")
        for child in wrapper:
            require(
                child.tag in ({"Pathway", "Reaction"} if kind == "constituent" else {"Pathway"}),
                "wrong native membership type",
            )
            memberships.append(ref_node(child, "META", child.tag))
    require(len({m["id"] for m in memberships}) == len(memberships), "duplicate membership")
    if kind == "constituent":
        require(
            [m["id"] for m in memberships if m["native_type"] == "Reaction"]
            == ["MetaCyc:OAHTHAUERA-RXN"],
            "wrong constituent composite backlink",
        )
    ec = {
        FERREDOXIN_REACTION_KIND: "EC-1.3.7.8",
        HYDROLYTIC_KIND: "EC-3.7.1.21",
        NAMED_REACTION_KIND: "EC-2.3.1",
    }.get(kind)
    require(
        ([n.text for n in entity.findall("ec-number")]) == ([ec] if ec else []),
        "wrong native EC profile",
    )
    if ec:
        official = one(entity, "ec-number").findall("official")
        require(
            [n.text for n in official] == ([] if kind == NAMED_REACTION_KIND else ["T"]),
            "wrong native EC official context",
        )
    expected_activities = {
        FERREDOXIN_REACTION_KIND: {"ENZRXN-1102": "CPLX-883", "ENZRXN-1821": "CPLX-1341"},
        HYDROLYTIC_KIND: {"ENZRXN-22284": "CPLX-8780", "ENZRXN-1841": "CPLX-1361"},
        NAMED_REACTION_KIND: {"ENZRXN-26773": "MONOMER-20679"},
    }
    activities = (
        _activities(entity, "enzymatic-reaction", frame, expected_activities[kind])
        if kind in expected_activities
        else []
    )
    require(
        kind in expected_activities or not entity.findall("enzymatic-reaction"),
        "unexpected constituent activity",
    )
    members = []
    if kind == HYDROLYTIC_KIND:
        listing = one(entity, "reaction-list")
        blank(listing)
        require(not listing.attrib, "invalid constituent list")
        members = [ref_node(n, "META", "Reaction") for n in listing]
        require([n["id"] for n in members] == CONSTITUENTS, "wrong composite constituents/order")
        require(not memberships, "auxiliary composite must not claim selected pathway membership")
    else:
        require(not entity.findall("reaction-list"), "unexpected reaction decomposition")
    if kind == NAMED_REACTION_KIND:
        label, synonyms = direct_names(entity, frame)
    else:
        require(not entity.findall("common-name"), "unnamed profile rejects direct names")
        label, synonyms = frame, []
    return {
        "parent_classes": parents,
        "direction": direction,
        "sides": sides,
        "memberships": memberships,
        "activities": activities,
        "reaction_list": members,
        "label": label,
        "synonyms": synonyms,
    }


def _document(body: str, source: dict, kind: str) -> dict:
    require(isinstance(body, str), "original XML must be text")
    entity, frame = _envelope(body, source, kind)
    projection = (
        _heteromer(entity, frame)
        if kind == HETEROMER_KIND
        else _ferredoxin(entity, frame)
        if kind == FERREDOXIN_CLASS_KIND
        else _reaction(entity, frame, kind)
    )
    return {"id": "MetaCyc:" + frame, "original_xml": body, "projection": projection}


def _restore(doc: dict, source: dict, kind: str) -> None:
    keys(doc, {"id", "original_xml", "projection"}, "invalid complete native document")
    require(
        json.dumps(doc, sort_keys=True)
        == json.dumps(_document(doc["original_xml"], source, kind), sort_keys=True),
        "complete native projection mismatch",
    )


def _relations(native: dict) -> None:
    companions = native["companions"]
    require(
        [c["document"]["id"] for c in companions] == CONSTITUENTS,
        "wrong complete companion identities/order",
    )

    def net(projection):
        result = Counter()
        for side in projection["sides"]:
            result[side["entity"]["id"]] += side["coefficient"] * (
                1 if side["side"] == "right" else -1
            )
        return result

    total = Counter()
    for child in companions:
        total.update(net(child["document"]["projection"]))
    require(
        {k: v for k, v in total.items() if v}
        == {k: v for k, v in net(native["document"]["projection"]).items() if v},
        "constituent signed sum differs from composite",
    )


def benzoyl_metadata(entry: dict, cache_dir: Path) -> dict:
    kind = entry.get("kind")
    require(kind in BENZOYL_KINDS, "unsupported bounded native kind")
    keys(
        entry,
        PROVENANCE
        | {"key", "kind", "path"}
        | ({"constituent_sources"} if kind == HYDROLYTIC_KIND else set()),
        "invalid bounded native manifest fields",
    )
    require(isinstance(entry["key"], str) and entry["key"].strip(), "invalid source key")
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    doc = _document(original_path(entry, cache_dir).read_bytes().decode("utf-8"), source, kind)
    companions = []
    if kind == HYDROLYTIC_KIND:
        descriptors = entry["constituent_sources"]
        require(isinstance(descriptors, list) and len(descriptors) == 2, "requires two originals")
        for descriptor in descriptors:
            keys(descriptor, PROVENANCE | {"path"}, "invalid constituent original fields")
            prov = {k: descriptor[k] for k in PROVENANCE_ORDER}
            body = original_path(descriptor, cache_dir).read_bytes().decode("utf-8")
            companions.append({**prov, "document": _document(body, prov, "constituent")})
    result = {
        **source,
        "kind": kind,
        FIELD: {
            "id": doc["id"],
            "document": doc,
            "companions": companions,
        },
    }
    validate_benzoyl_metadata(result)
    return result


def validate_benzoyl_metadata(metadata: dict) -> None:
    keys(metadata, PROVENANCE | {"kind", FIELD}, "invalid bounded native metadata")
    kind = metadata["kind"]
    require(kind in BENZOYL_KINDS, "unsupported bounded native kind")
    native = metadata[FIELD]
    keys(native, {"id", "document", "companions"}, "invalid bounded native scope")
    source = {k: metadata[k] for k in PROVENANCE_ORDER}
    _restore(native["document"], source, kind)
    require(native["id"] == native["document"]["id"], "native identity mismatch")
    companions = native["companions"]
    require(
        isinstance(companions, list) and len(companions) == (2 if kind == HYDROLYTIC_KIND else 0),
        "wrong companion cardinality",
    )
    for child in companions:
        keys(child, PROVENANCE | {"document"}, "invalid companion provenance")
        prov = {k: child[k] for k in PROVENANCE_ORDER}
        require(prov["version"] == source["version"], "companion release mismatch")
        _restore(child["document"], prov, "constituent")
    if kind == HYDROLYTIC_KIND:
        _relations(native)


def benzoyl_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_benzoyl_metadata(metadata)
    native = metadata[FIELD]
    projection = native["document"]["projection"]
    kind = metadata["kind"]
    return native["id"], {
        "label": projection["label"],
        "synonyms": sorted(projection["synonyms"]),
        "source": source,
        "entity_type": "protein_complex"
        if kind == HETEROMER_KIND
        else "protein_class"
        if kind == FERREDOXIN_CLASS_KIND
        else "reaction",
        "label_kind": "source_context"
        if kind in {FERREDOXIN_REACTION_KIND, HYDROLYTIC_KIND}
        else "canonical",
    }


def validate_benzoyl_assertions(sources: dict, claims: list[tuple[str, str]]) -> None:
    """Check all complete owners and companion provenance before selection."""
    assertions, companion_origins = {}, {}
    for metadata in sources.values():
        if metadata.get("kind") not in BENZOYL_KINDS:
            continue
        validate_benzoyl_metadata(metadata)
        native = metadata[FIELD]
        ident = native["id"]
        signature = (metadata["kind"], json.dumps(native, sort_keys=True), metadata["version"])
        require(
            ident not in assertions or assertions[ident] == signature,
            "conflicting complete bounded native assertion for " + ident,
        )
        assertions[ident] = signature
        for child in native["companions"]:
            child_id = child["document"]["id"]
            origin = tuple(child[k] for k in ("url", "version", "sha256"))
            require(
                child_id not in companion_origins or companion_origins[child_id] == origin,
                "conflicting companion original provenance",
            )
            companion_origins[child_id] = origin
    observations = list(claims)
    for key, metadata in sources.items():
        url = urlsplit(metadata.get("url", ""))
        if url.hostname in {HOST, "biocyc.org", "www.biocyc.org", "metacyc.org", "www.metacyc.org"}:
            query = parse_qs(url.query)
            values = query.get("id", [])
            if url.query.startswith("META:"):
                values += [url.query]
            for value in values:
                if value.startswith("META:"):
                    observations.append(("MetaCyc:" + value[5:], key))
                elif query.get("orgid") == ["META"]:
                    observations.append(("MetaCyc:" + value, key))
            if url.path.startswith("/META/"):
                observations.extend(("MetaCyc:" + v, key) for v in query.get("object", []))
        for field, value in metadata.items():
            if (
                field.startswith("native_")
                and isinstance(value, dict)
                and isinstance(value.get("id"), str)
            ):
                observations.append((value["id"], key))
    for ident, key in observations:
        metadata = sources[key]
        if ident in PROTECTED:
            require(
                metadata.get("kind") == PROTECTED[ident],
                "bounded native identity requires its complete typed scope: " + ident,
            )
        if ident in companion_origins:
            require(
                metadata.get("kind") == "metacyc-reaction-xml"
                and tuple(metadata.get(k) for k in ("url", "version", "sha256"))
                == companion_origins[ident],
                "companion owner differs from complete original",
            )
