"""Directly named whole ECOLI assemblies; separate from unnamed NAD modes."""

from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import native_identity, one, require
from pathwaymech.biocyc_native_context import (
    ancillary,
    attributes,
    blank,
    direct_names,
    integer,
    metadata_build,
    metadata_validate,
    ref_node,
    refs,
    retained,
)

NAMED_COMPLEX_KIND = "ecocyc-named-protein-complex-xml"
FIELD = "native_named_complex"
CORE = {"parent", "common-name", "synonym", "component"}
ANCILLARY = {
    "catalyzes",
    "credits",
    "molecular-weight-exp",
    "species",
    "citation",
    "comment",
    "dblink",
    "has-go-term",
    "component-of",
    "location",
}


def project(entity: ET.Element, frame: str) -> dict:
    attributes(entity, frame, "ECOLI", "Protein", False)
    ancillary(entity, ANCILLARY, CORE, "ECOLI")
    parents = refs(entity, "parent", "ECOLI", "Protein", is_class=True)
    require(
        [p["attributes"]["frameid"] for p in parents] == ["Protein-Complexes"],
        "named complex requires sole Protein-Complexes parent",
    )
    label, aliases = direct_names(entity, frame)
    components = []
    for wrapper in entity.findall("component"):
        blank(wrapper)
        require(
            not wrapper.attrib and sorted(n.tag for n in wrapper) == ["Protein", "coefficient"],
            "invalid named complex component wrapper",
        )
        component = ref_node(one(wrapper, "Protein"), "ECOLI", "Protein")
        require(component["attributes"]["frameid"] != frame, "self component")
        components.append(
            {"entity": component, "coefficient": integer(one(wrapper, "coefficient"))}
        )
    require(
        bool(components) and len({p["entity"]["id"] for p in components}) == len(components),
        "missing or duplicate named complex components",
    )
    require(len(components) > 1 or components[0]["coefficient"] >= 2, "monomer is not a homomer")
    return {
        "id": "EcoCyc:" + frame,
        "native_type": "Protein",
        "is_class": False,
        "parent_classes": parents,
        "direct_common_name": label,
        "direct_synonyms": aliases,
        "components": components,
        **retained(entity, CORE),
    }


def reader(path: Path, url: str, version: str) -> tuple[ET.Element, str]:
    return native_identity(path, url, version, "ECOLI", is_class=False)


def named_complex_metadata(entry: dict, cache_dir: Path) -> dict:
    result = metadata_build(entry, cache_dir, NAMED_COMPLEX_KIND, FIELD, "ECOLI", reader, project)
    validate_named_complex_metadata(result)
    return result


def validate_named_complex_metadata(metadata: dict) -> None:
    metadata_validate(metadata, NAMED_COMPLEX_KIND, FIELD, "ECOLI", "Protein", project)


def named_complex_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_named_complex_metadata(metadata)
    native = metadata[FIELD]
    return native["id"], {
        "label": native["direct_common_name"],
        "synonyms": sorted(native["direct_synonyms"]),
        "source": source,
        "entity_type": "protein_complex",
        "label_kind": "canonical",
    }


def validate_named_complex_graph(natives: list[dict]) -> None:
    """Reject forward assembly cycles; component-of is retained reverse context.

    Only supplied whole assemblies are traversed. Unresolved leaf references are
    not inferred to be complexes or claimed as independently verified monomers.
    """
    graph = {}
    for native in natives:
        children = tuple(c["entity"]["id"] for c in native["components"])
        require(
            native["id"] not in graph or graph[native["id"]] == children,
            "conflicting forward assembly components",
        )
        graph[native["id"]] = children
    pending = set(graph)
    while pending:
        leaves = {n for n in pending if not pending.intersection(graph[n])}
        require(bool(leaves), "cyclic forward assembly components")
        pending -= leaves
