"""Whole unnamed native composite electron-transfer reaction authorities."""

from __future__ import annotations

import re
from pathlib import Path
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import HOST, _TreeBuilder, one, request, require, scalar
from pathwaymech.biocyc_native_context import (
    ancillary,
    attributes,
    blank,
    integer,
    metadata_build,
    metadata_validate,
    ref_node,
    refs,
    retained,
)

ELECTRON_TRANSFER_KIND = "metacyc-electron-transfer-reaction-xml"
FIELD = "native_electron_transfer"
CORE = {"parent", "reaction-direction", "left", "right", "reaction-list", "reaction-ordering"}
ANCILLARY = {
    "gibbs-0",
    "orphan",
    "physiologically-relevant",
    "credits",
    "in-pathway",
    "enzymatic-reaction",
    "dblink",
    "ec-number",
}


def reaction_identity(path: Path, url: str, version: str) -> tuple[ET.Element, str]:
    pgdb = "META"
    frame = request(url, pgdb)
    requested = pgdb + ":" + frame
    root = ET.fromstring(path.read_bytes(), parser=ET.XMLParser(target=_TreeBuilder()))
    require(
        root.tag == "ptools-xml" and len(root) == 2,
        "requires metadata and one direct native object",
    )
    metadata = one(root, "metadata")
    entities = [node for node in root if node.tag != "metadata"]
    require(
        len(entities) == 1 and entities[0].tag == "Reaction",
        "unsupported native object type",
    )
    entity = entities[0]
    require(
        set(root.attrib) == {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        and root.get("{http://www.w3.org/XML/1998/namespace}base")
        in {url, f"http://{HOST}:443/getxml?{requested}"}
        and isinstance(version, str)
        and re.fullmatch(r"[0-9]+(?:\.[0-9]+)+", version) is not None
        and root.get("ptools-version") == version,
        "XML base/version mismatch",
    )
    for node in (root, metadata, entity):
        require(
            not (node.text or "").strip() and all(not (child.tail or "").strip() for child in node),
            "non-whitespace native container text",
        )
    require(
        not metadata.attrib
        and sorted(node.tag for node in metadata)
        == sorted(["url", "service_name", "query", "num_results", "PGDB"]),
        "malformed metadata",
    )
    require(
        scalar(metadata, "url") in {f"https://{HOST}/", f"http://{HOST}:443/"}
        and scalar(metadata, "service_name") == "getxml"
        and scalar(metadata, "query") == requested
        and scalar(metadata, "num_results") == "1",
        "service/query identity mismatch",
    )
    database = one(metadata, "PGDB")
    require(
        database.attrib == {"orgid": pgdb, "version": version}
        and not (database.text or "").strip()
        and all(not (node.tail or "").strip() for node in database),
        "PGDB/version mismatch",
    )
    require(
        [node.tag for node in database] == ["species"]
        and scalar(database, "species", True) == "MetaCyc",
        "META species mismatch",
    )
    attributes = {"ID": requested, "orgid": pgdb, "frameid": frame, "detail": "full"}
    require(entity.attrib == attributes, "mismatched native top-level identity/type/class")
    return entity, frame


def project(entity: ET.Element, frame: str) -> dict:
    attributes(entity, frame, "META", "Reaction", False)
    ancillary(entity, ANCILLARY, CORE, "META")
    parents = refs(entity, "parent", "META", "Reaction", is_class=True)
    require(
        {p["attributes"]["frameid"] for p in parents}
        == {"Electron-Transfer-Reactions", "Small-Molecule-Reactions"},
        "unsupported composite parents",
    )
    direction = scalar(entity, "reaction-direction")
    require(
        direction in {"LEFT-TO-RIGHT", "PHYSIOL-LEFT-TO-RIGHT"}, "unsupported composite direction"
    )
    sides = []
    for side in ["left", "right"]:
        seen = set()
        require(bool(entity.findall(side)), "empty composite side")
        for ordinal, wrapper in enumerate(entity.findall(side), 1):
            blank(wrapper)
            require(
                not wrapper.attrib
                and all(n.tag in {"Compound", "coefficient", "compartment"} for n in wrapper),
                "invalid composite side wrapper",
            )
            compound = one(wrapper, "Compound")
            ref = ref_node(compound, "META", "Compound", is_class=compound.get("class") == "true")
            coefficients, compartments = (
                wrapper.findall("coefficient"),
                wrapper.findall("compartment"),
            )
            require(
                len(coefficients) <= 1 and len(compartments) <= 1,
                "duplicate side coefficient/compartment",
            )
            coefficient = integer(coefficients[0]) if coefficients else 1
            compartment = None
            if compartments:
                c = compartments[0]
                blank(c)
                require(not c.attrib and len(c) == 1, "invalid side compartment wrapper")
                compartment = ref_node(c[0], "META", "cco")
                require(
                    compartment["attributes"]["frameid"] in {"CCO-IN", "CCO-OUT"},
                    "unsupported membrane-side compartment",
                )
            identity = (
                ref["id"],
                ref["is_class"],
                None if compartment is None else compartment["id"],
            )
            require(identity not in seen, "duplicate composite side occurrence")
            seen.add(identity)
            sides.append(
                {
                    "side": side,
                    "ordinal": ordinal,
                    "source_position": list(entity).index(wrapper),
                    "entity": ref,
                    "coefficient": coefficient,
                    "coefficient_explicit": bool(coefficients),
                    "compartment": compartment,
                }
            )
    listing = one(entity, "reaction-list")
    blank(listing)
    require(not listing.attrib and len(listing) >= 2, "incomplete composite decomposition")
    members = [ref_node(n, "META", "Reaction") for n in listing]
    ids = {n["id"] for n in members}
    require(
        len(ids) == len(members) and "MetaCyc:" + frame not in ids,
        "duplicate/self composite member",
    )
    ordering = []
    links = set()
    for w in entity.findall("reaction-ordering"):
        blank(w)
        require(
            not w.attrib and sorted(n.tag for n in w) == ["Reaction", "predecessor-reactions"],
            "invalid ordering wrapper",
        )
        target = ref_node(one(w, "Reaction"), "META", "Reaction")
        pred = one(w, "predecessor-reactions")
        blank(pred)
        require(not pred.attrib and len(pred) > 0, "empty ordering predecessors")
        predecessors = [ref_node(n, "META", "Reaction") for n in pred]
        require(
            len({n["id"] for n in predecessors}) == len(predecessors),
            "duplicate ordering predecessors",
        )
        for predecessor in predecessors:
            link = (predecessor["id"], target["id"])
            require(
                all(n in ids for n in link) and link[0] != link[1] and link not in links,
                "invalid ordering membership/self/duplicate",
            )
            links.add(link)
        ordering.append({"target": target, "predecessors": predecessors})
    require(bool(ordering), "composite lacks explicit ordering")
    pending = set(ids)
    while pending:
        ready = {n for n in pending if not any(b == n and a in pending for a, b in links)}
        require(bool(ready), "cyclic composite ordering")
        pending -= ready
    return {
        "id": "MetaCyc:" + frame,
        "native_type": "Reaction",
        "is_class": False,
        "parent_classes": parents,
        "direction": direction,
        "sides": sides,
        "reaction_list": members,
        "reaction_ordering": ordering,
        **retained(entity, CORE),
    }


def reaction_metadata(entry: dict, cache_dir: Path) -> dict:
    result = metadata_build(
        entry, cache_dir, ELECTRON_TRANSFER_KIND, FIELD, "META", reaction_identity, project
    )
    validate_reaction_metadata(result)
    return result


def validate_reaction_metadata(metadata: dict) -> None:
    metadata_validate(metadata, ELECTRON_TRANSFER_KIND, FIELD, "META", "Reaction", project)


def reaction_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_reaction_metadata(metadata)
    ident = metadata[FIELD]["id"]
    return ident, {
        "label": ident.split(":", 1)[1],
        "synonyms": [],
        "source": source,
        "entity_type": "reaction",
        "label_kind": "source_context",
    }
