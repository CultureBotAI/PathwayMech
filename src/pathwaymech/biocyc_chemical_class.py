"""Whole native Compound classes with source-derived structural parent profiles."""

from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import native_identity, require
from pathwaymech.biocyc_native_context import (
    ancillary,
    attributes,
    blank,
    charged_context_reference,
    direct_names,
    metadata_build,
    metadata_validate,
    ref_node,
    refs,
    retained,
)

CHEMICAL_CLASS_KIND = "metacyc-chemical-class-xml"
FIELD = "native_chemical_class"
CORE = {"parent", "subclass", "instance", "common-name", "synonym"}
ANCILLARY = {
    "cml",
    "regulates",
    "credits",
    "comment",
    "citation",
    "appears-in-left-side-of",
    "appears-in-right-side-of",
    "cofactors-of",
    "dblink",
    "abbrev-name",
    "gibbs-0",
    "inchi",
    "inchi-key",
    "molecular-weight",
    "monoisotopic-mw",
    "component-of",
}
PROFILES = {
    frozenset({"ETR-Quinones"}): ("quinone", ("chemical_entity",)),
    frozenset({"ETR-Quinols", "Methoxybenzenes"}): ("quinol", ("chemical_entity",)),
    frozenset({"Cofactors", "Hemes", "Organometallics"}): (
        "heme-family",
        ("chemical_entity", "cofactor"),
    ),
    frozenset({"Organometallics"}): ("organometallic-cofactor", ("chemical_entity", "cofactor")),
    frozenset({"Glycerolipids"}): ("glycerolipid", ("chemical_entity", "lipid")),
    frozenset({"CPD-11501", "ETR-Quinones"}): ("naphthoquinone", ("chemical_entity",)),
    frozenset({"ETR-Quinols"}): ("unsubstituted-quinol", ("chemical_entity",)),
    frozenset({"FeS-Centers"}): ("iron-sulfur-cofactor", ("chemical_entity", "cofactor")),
    frozenset({"Metal-sulfur-Clusters"}): ("iron-sulfur-family", ("chemical_entity", "cofactor")),
}


def project(entity: ET.Element, frame: str) -> dict:
    attributes(entity, frame, "META", "Compound", True)
    ancillary(entity, ANCILLARY, CORE, "META")
    parents = refs(entity, "parent", "META", "Compound", is_class=True)
    parent_set = frozenset(p["attributes"]["frameid"] for p in parents)
    require(parent_set in PROFILES, "unsupported whole chemical class parents")
    profile, categories = PROFILES[parent_set]
    if "cofactor" in categories:
        require(
            len(entity.findall("cofactors-of")) == 1, "cofactor profile needs whole activity proof"
        )
    # Charge-bearing subclass frames remain retained native class references;
    # they do not broaden the public selected-ID or legacy carrier grammar.
    subclasses = []
    for wrapper in entity.findall("subclass"):
        blank(wrapper)
        require(not wrapper.attrib and len(wrapper) == 1, "invalid chemical subclass wrapper")
        reader = charged_context_reference if "+" in wrapper[0].get("frameid", "") else ref_node
        subclasses.append(reader(wrapper[0], "META", "Compound", is_class=True))
    require(
        len({p["id"] for p in subclasses}) == len(subclasses)
        and all(p["attributes"]["frameid"] != frame for p in subclasses),
        "duplicate/self chemical subclass",
    )
    instances = refs(entity, "instance", "META", "Compound", is_class=False)
    class_ids = {p["id"] for p in parents + subclasses}
    require(
        not class_ids.intersection(p["id"] for p in instances), "same class/member is also instance"
    )
    label, aliases = direct_names(entity, frame)
    return {
        "id": "MetaCyc:" + frame,
        "native_type": "Compound",
        "is_class": True,
        "profile": profile,
        "parent_classes": parents,
        "subclasses": subclasses,
        "instances": instances,
        "direct_common_name": label,
        "direct_synonyms": aliases,
        "allowed_categories": list(categories),
        **retained(entity, CORE),
    }


def reader(path: Path, url: str, version: str) -> tuple[ET.Element, str]:
    return native_identity(path, url, version, "META", is_class=True)


def chemical_class_metadata(entry: dict, cache_dir: Path) -> dict:
    result = metadata_build(entry, cache_dir, CHEMICAL_CLASS_KIND, FIELD, "META", reader, project)
    validate_chemical_class_metadata(result)
    return result


def validate_chemical_class_metadata(metadata: dict) -> None:
    metadata_validate(metadata, CHEMICAL_CLASS_KIND, FIELD, "META", "Compound", project)


def chemical_class_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_chemical_class_metadata(metadata)
    native = metadata[FIELD]
    return native["id"], {
        "label": native["direct_common_name"],
        "synonyms": sorted(native["direct_synonyms"]),
        "source": source,
        "entity_type": "native_chemical_class",
        "label_kind": "canonical",
        "allowed_categories": list(native["allowed_categories"]),
    }
