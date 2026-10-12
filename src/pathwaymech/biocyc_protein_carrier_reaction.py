"""Whole unnamed chemical reactions with explicit Protein-class carrier sides.

This mode retains the historical native EC context locally. It neither changes
the public EC grammar nor turns a formal protein class into a small molecule.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import HOST, name, one, require, scalar
from pathwaymech.biocyc_electron_transfer import reaction_identity
from pathwaymech.biocyc_native_context import (
    activity,
    ancillary,
    attributes,
    blank,
    context_identity,
    integer,
    metadata_build,
    metadata_validate,
    ref_node,
    refs,
    retained,
)

PROTEIN_CARRIER_REACTION_KIND = "metacyc-protein-carrier-reaction-xml"
FIELD = "native_protein_carrier_reaction"
CORE = {"parent", "reaction-direction", "left", "right"}
ANCILLARY = {
    "orphan",
    "physiologically-relevant",
    "credits",
    "comment",
    "in-pathway",
    "enzymatic-reaction",
    "ec-number",
}
# This known frame must not be accepted with its whole typed scope stripped,
# even when the downgraded owner is the only owner or contributes no term.
PROTECTED_IDS = {"MetaCyc:RXN-21320"}


def _strings(node: ET.Element, tags: set[str]) -> None:
    require(len(node) == len(tags) and {n.tag for n in node} == tags, "invalid credit fields")
    for child in node:
        scalar(node, child.tag, True)


def _credits(node: ET.Element) -> None:
    blank(node)
    created = one(node, "created")
    require(not node.attrib and len(node) == 1, "unsupported credit event")
    blank(created)
    require(
        not created.attrib
        and len(created) == 3
        and {n.tag for n in created} == {"date", "Person", "Organization"},
        "invalid created credit",
    )
    when = one(created, "date")
    require(when.attrib == {"datatype": "date"} and not len(when), "invalid credit date")
    require(date.fromisoformat(when.text or "").isoformat() == when.text, "invalid credit date")
    person = one(created, "Person")
    context_identity(person, "META", "Person")
    require(person.get("detail") == "full", "credit requires complete Person")
    require(
        len(person) == 4
        and {n.tag for n in person} == {"email", "affiliations", "comment", "common-name"},
        "invalid Person context",
    )
    for tag in ("email", "comment", "common-name"):
        scalar(person, tag, True)
    affiliation = one(person, "affiliations")
    blank(affiliation)
    require(not affiliation.attrib and len(affiliation) == 1, "invalid affiliation")
    organization = one(affiliation, "Organization")
    context_identity(organization, "META", "Organization")
    require(organization.get("detail") == "full", "credit requires complete Organization")
    _strings(organization, {"email", "abbrev-name", "url", "common-name"})
    reference = ref_node(one(created, "Organization"), "META", "Organization", local=True)
    require(
        reference["attributes"]["frameid"] == organization.get("frameid"),
        "credit Organization disagreement",
    )


def project(entity: ET.Element, frame: str) -> dict:
    attributes(entity, frame, "META", "Reaction", False)
    # Only this profile bypasses the shared numeric/partial EC validator; the
    # entire observed historical slot is independently validated below.
    ancillary(entity, ANCILLARY - {"ec-number"}, CORE | {"ec-number"}, "META")
    for tag in ANCILLARY:
        one(entity, tag)
    require(one(entity, "orphan").text == "NO", "unsupported orphan status")
    _credits(one(entity, "credits"))
    ec = one(entity, "ec-number")
    require(
        not ec.attrib and ec.text == "EC-1.18.98.M1" and len(ec) == 1,
        "unsupported local historical EC context",
    )
    official = one(ec, "official")
    require(
        not official.attrib
        and not len(official)
        and official.text == "T"
        and not (official.tail or "").strip(),
        "invalid historical EC official flag",
    )
    parents = refs(entity, "parent", "META", "Reaction", is_class=True)
    require(
        {p["attributes"]["frameid"] for p in parents}
        == {"Chemical-Reactions", "Small-Molecule-Reactions"},
        "unsupported protein-carrier reaction parents",
    )
    direction = scalar(entity, "reaction-direction")
    require(direction == "PHYSIOL-LEFT-TO-RIGHT", "unsupported protein-carrier direction")
    sides = []
    for side in ("left", "right"):
        occurrences = entity.findall(side)
        require(bool(occurrences), "empty protein-carrier side")
        seen = set()
        carrier = False
        for ordinal, wrapper in enumerate(occurrences, 1):
            blank(wrapper)
            require(
                not wrapper.attrib
                and len(wrapper) in {1, 2}
                and wrapper[0].tag in {"Compound", "Protein"}
                and (len(wrapper) == 1 or wrapper[1].tag == "coefficient"),
                "invalid typed carrier side wrapper",
            )
            target = wrapper[0]
            is_protein = target.tag == "Protein"
            ref = ref_node(target, "META", target.tag, is_class=is_protein)
            require(ref["id"] not in seen, "duplicate protein-carrier side occurrence")
            seen.add(ref["id"])
            carrier |= is_protein
            sides.append(
                {
                    "side": side,
                    "ordinal": ordinal,
                    "source_position": list(entity).index(wrapper),
                    "entity": ref,
                    "coefficient": integer(wrapper[1]) if len(wrapper) == 2 else 1,
                    "coefficient_explicit": len(wrapper) == 2,
                }
            )
        require(carrier, "each side requires an explicit Protein class")
    membership = one(entity, "in-pathway")
    for child in membership:
        ref_node(child, "META", "Pathway")
    require(
        len({child.get("frameid") for child in membership}) == len(membership),
        "duplicate pathway membership",
    )
    wrapper = one(entity, "enzymatic-reaction")
    require(len(wrapper) == 1, "requires one embedded activity")
    enzyme = wrapper[0]
    activity(enzyme, "META")
    require(
        len(enzyme) == 3 and {n.tag for n in enzyme} == {"enzyme", "reaction", "common-name"},
        "unsupported embedded activity context",
    )
    name(one(enzyme, "common-name"), enzyme.get("frameid", ""))
    ref_node(one(enzyme, "enzyme")[0], "META", "Protein")
    back = ref_node(one(enzyme, "reaction")[0], "META", "Reaction", local=True)
    require(back["id"] == "MetaCyc:" + frame, "activity reaction back-reference mismatch")
    return {
        "id": "MetaCyc:" + frame,
        "native_type": "Reaction",
        "is_class": False,
        "parent_classes": parents,
        "direction": direction,
        "sides": sides,
        **retained(entity, CORE),
    }


def carrier_reaction_metadata(entry: dict, cache_dir: Path) -> dict:
    result = metadata_build(
        entry, cache_dir, PROTEIN_CARRIER_REACTION_KIND, FIELD, "META", reaction_identity, project
    )
    validate_carrier_reaction_metadata(result)
    return result


def validate_carrier_reaction_metadata(metadata: dict) -> None:
    metadata_validate(metadata, PROTEIN_CARRIER_REACTION_KIND, FIELD, "META", "Reaction", project)


def carrier_reaction_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_carrier_reaction_metadata(metadata)
    ident = metadata[FIELD]["id"]
    return ident, {
        "label": ident.split(":", 1)[1],
        "synonyms": [],
        "source": source,
        "entity_type": "reaction",
        "label_kind": "source_context",
    }


def validate_carrier_reaction_assertions(sources: dict) -> set[str]:
    """Compare complete owners before selection, including request-only claims."""
    protected = set(PROTECTED_IDS)
    assertions = {}
    for metadata in sources.values():
        if metadata.get("kind") == PROTEIN_CARRIER_REACTION_KIND:
            validate_carrier_reaction_metadata(metadata)
            native = metadata[FIELD]
            ident = native["id"]
            value = (metadata["kind"], json.dumps(native, sort_keys=True), metadata["version"])
            require(
                ident not in assertions or assertions[ident] == value,
                "conflicting whole protein-carrier reaction assertion for " + ident,
            )
            assertions[ident] = value
            protected.add(ident)
    for metadata in sources.values():
        claimed = set()
        url = urlsplit(metadata.get("url", ""))
        if url.hostname in {
            HOST,
            "biocyc.org",
            "www.biocyc.org",
            "metacyc.org",
            "www.metacyc.org",
        }:
            query = parse_qs(url.query)
            for value in query.get("id", []):
                if value.startswith("META:"):
                    claimed.add("MetaCyc:" + value[5:])
                elif query.get("orgid") == ["META"]:
                    claimed.add("MetaCyc:" + value)
            if url.path.startswith("/META/"):
                claimed.update("MetaCyc:" + v for v in query.get("object", []))
        for field, native in metadata.items():
            if field.startswith("native_") and isinstance(native, dict):
                if isinstance(native.get("id"), str):
                    claimed.add(native["id"])
                if field == "native_aceto":
                    claimed.add(native["document"]["native"]["id"])
        require(
            not claimed.intersection(protected)
            or metadata.get("kind") == PROTEIN_CARRIER_REACTION_KIND,
            "protein-carrier native identity requires its complete typed scope",
        )
    return protected
