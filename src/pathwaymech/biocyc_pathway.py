"""Whole named META Pathway instances with native graph and taxon context.

The Pathway object, not an HTML template title, authorizes pathway identity.
Layouts retain source primaries and never stand in for complete reaction sides.
"""

from __future__ import annotations

import base64
import json
import re
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import (
    HOST,
    PROVENANCE,
    PROVENANCE_ORDER,
    _TreeBuilder,
    keys,
    one,
    original_path,
    provenance,
    request,
    require,
    scalar,
)
from pathwaymech.biocyc_native_context import (
    ancillary,
    attributes,
    blank,
    direct_names,
    metadata_build,
    metadata_validate,
    ref_node,
    refs,
    retained,
)
from pathwaymech.biocyc_p321 import credits, envelope, evidence, original_bytes, publication

PATHWAY_KIND = "metacyc-pathway-xml"
FIELD = "native_pathway"
CORE = {
    "parent",
    "common-name",
    "synonym",
    "reaction-list",
    "reaction-ordering",
    "reaction-layout",
    "taxonomic-range",
    "species",
}
ANCILLARY = {"credits", "comment", "dblink"}


def pathway_identity(path: Path, url: str, version: str) -> tuple[ET.Element, str]:
    frame = request(url, "META")
    requested = "META:" + frame
    root = ET.fromstring(path.read_bytes(), parser=ET.XMLParser(target=_TreeBuilder()))
    require(root.tag == "ptools-xml" and len(root) == 2, "requires metadata and one Pathway")
    metadata = one(root, "metadata")
    entities = [node for node in root if node.tag != "metadata"]
    require(len(entities) == 1 and entities[0].tag == "Pathway", "requires native Pathway type")
    entity = entities[0]
    require(
        set(root.attrib) == {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        and root.get("{http://www.w3.org/XML/1998/namespace}base")
        in {url, f"http://{HOST}:443/getxml?{requested}"}
        and isinstance(version, str)
        and re.fullmatch(r"[0-9]+(?:\.[0-9]+)+", version) is not None
        and root.get("ptools-version") == version,
        "Pathway XML base/version mismatch",
    )
    for node in (root, metadata, entity):
        blank(node)
    require(
        not metadata.attrib
        and sorted(node.tag for node in metadata)
        == sorted(["url", "service_name", "query", "num_results", "PGDB"]),
        "malformed Pathway metadata",
    )
    require(
        scalar(metadata, "url") in {f"https://{HOST}/", f"http://{HOST}:443/"}
        and scalar(metadata, "service_name") == "getxml"
        and scalar(metadata, "query") == requested
        and scalar(metadata, "num_results") == "1",
        "Pathway service/query identity mismatch",
    )
    database = one(metadata, "PGDB")
    blank(database)
    require(
        database.attrib == {"orgid": "META", "version": version}
        and [node.tag for node in database] == ["species"]
        and scalar(database, "species", True) == "MetaCyc",
        "Pathway PGDB/version/species mismatch",
    )
    attributes(entity, frame, "META", "Pathway", False)
    return entity, frame


def organism(node: ET.Element) -> None:
    """Retain the native class-marked taxon annotation, not a live-node claim."""
    frame = node.get("frameid", "")
    require(re.fullmatch(r"TAX-[0-9]+", frame) is not None, "invalid native taxon frame")
    attributes(node, frame, "META", "Organism", True)
    core = {"parent", "common-name", "synonym", "rank", "strain-name"}
    ancillary(node, {"comment", "citation", "dblink"}, core, "META")
    refs(node, "parent", "META", "Organism", is_class=True)
    # Context names may contain literal source angle brackets (e.g. <bacteria>).
    # They never supply a selected node's canonical name.
    scalar(node, "common-name", True)
    require(
        scalar(node, "rank")
        in {
            "superkingdom",
            "kingdom",
            "phylum",
            "class",
            "order",
            "family",
            "genus",
            "species",
            "subspecies",
            "strain",
        },
        "invalid native taxon rank",
    )
    require(len(node.findall("strain-name")) <= 1, "duplicate native strain name")
    if node.findall("strain-name"):
        scalar(node, "strain-name", True)
    for synonym in node.findall("synonym"):
        require(
            synonym.attrib == {"datatype": "string"}
            and not len(synonym)
            and bool((synonym.text or "").strip()),
            "invalid native taxon synonym",
        )


def p321_context(entity: ET.Element) -> dict:
    expected = {
        "parent": 1,
        "credits": 1,
        "comment": 1,
        "pathway-link": 3,
        "citation": 8,
        "evidence": 1,
        "synonym": 1,
        "taxonomic-range": 1,
        "reaction-ordering": 8,
        "species": 1,
        "reaction-layout": 9,
        "dblink": 1,
        "common-name": 1,
        "reaction-list": 1,
    }
    require(Counter(n.tag for n in entity) == expected, "incomplete P321 pathway slots")
    credits(one(entity, "credits"))
    citations = []
    for wrapper in entity.findall("citation"):
        blank(wrapper)
        require(not wrapper.attrib and len(wrapper) == 1, "invalid pathway citation")
        publication(wrapper[0])
        citations.append(wrapper[0].get("frameid"))
    require(len(set(citations)) == len(citations), "duplicate pathway citation")
    evidence(one(entity, "evidence"), "EV-EXP-IDA")
    links = []
    for wrapper in entity.findall("pathway-link"):
        blank(wrapper)
        require(
            not wrapper.attrib and [n.tag for n in wrapper] == ["Compound", "link-target"],
            "invalid pathway link",
        )
        compound = ref_node(wrapper[0], "META", "Compound")
        target = wrapper[1]
        blank(target)
        require(not target.attrib and len(target) == 1, "invalid pathway link target")
        pathway = ref_node(target[0], "META", "Pathway")
        links.append({"compound": compound, "pathway": pathway})
    require(
        [(v["compound"]["id"], v["pathway"]["id"]) for v in links]
        == [
            ("MetaCyc:CPD-533", "MetaCyc:PWY-301"),
            ("MetaCyc:BENZOYLCOA", "MetaCyc:PWY-283"),
            ("MetaCyc:GLUTARYL-COA", "MetaCyc:PWY-5177"),
        ],
        "wrong pathway link identities/order",
    )
    return {"citations": citations, "pathway_links": links}


def project(entity: ET.Element, frame: str) -> dict:
    attributes(entity, frame, "META", "Pathway", False)
    extra = {"citation", "evidence", "pathway-link"} if frame == "P321-PWY" else set()
    ancillary(entity, ANCILLARY, CORE | extra, "META")
    context = p321_context(entity) if extra else {}
    parents = refs(entity, "parent", "META", "Pathway", is_class=True)
    require(bool(parents), "Pathway lacks native parent classes")
    label, synonyms = direct_names(entity, frame)
    listing = one(entity, "reaction-list")
    blank(listing)
    require(not listing.attrib and len(listing) > 0, "empty/attributed pathway reaction list")
    members = [ref_node(n, "META", "Reaction") for n in listing]
    ids = {n["id"] for n in members}
    require(len(ids) == len(members), "duplicate pathway reaction member")
    ordering = []
    links = set()
    for wrapper in entity.findall("reaction-ordering"):
        blank(wrapper)
        require(
            not wrapper.attrib
            and sorted(n.tag for n in wrapper) == ["Reaction", "predecessor-reactions"],
            "invalid pathway ordering wrapper",
        )
        target = ref_node(one(wrapper, "Reaction"), "META", "Reaction")
        pred = one(wrapper, "predecessor-reactions")
        blank(pred)
        require(not pred.attrib and len(pred) > 0, "empty pathway predecessors")
        predecessors = [ref_node(n, "META", "Reaction") for n in pred]
        require(
            len({n["id"] for n in predecessors}) == len(predecessors),
            "duplicate pathway predecessor",
        )
        for previous in predecessors:
            link = previous["id"], target["id"]
            require(
                all(n in ids for n in link) and link[0] != link[1] and link not in links,
                "invalid pathway ordering membership/self/duplicate",
            )
            links.add(link)
        ordering.append({"target": target, "predecessors": predecessors})
    require(bool(ordering), "pathway lacks explicit reaction ordering")
    pending = set(ids)
    while pending:
        ready = {n for n in pending if not any(b == n and a in pending for a, b in links)}
        require(bool(ready), "cyclic pathway ordering")
        pending -= ready
    layouts = []
    for wrapper in entity.findall("reaction-layout"):
        blank(wrapper)
        require(
            not wrapper.attrib
            and sorted(n.tag for n in wrapper)
            == ["Reaction", "direction", "left-primaries", "right-primaries"],
            "invalid pathway layout wrapper",
        )
        reaction = ref_node(one(wrapper, "Reaction"), "META", "Reaction")
        direction = scalar(wrapper, "direction")
        require(direction in {"L2R", "R2L"}, "invalid pathway layout direction")
        primaries = {}
        for side in ("left-primaries", "right-primaries"):
            container = one(wrapper, side)
            blank(container)
            require(not container.attrib and len(container) > 0, "empty pathway layout primary")
            values = [
                ref_node(n, "META", "Compound", is_class=n.get("class") == "true")
                for n in container
            ]
            require(
                len({v["id"] for v in values}) == len(values), "duplicate pathway layout primary"
            )
            primaries[side] = values
        layouts.append({"reaction": reaction, "direction": direction, **primaries})
    require(
        len(layouts) == len(ids) and {v["reaction"]["id"] for v in layouts} == ids,
        "pathway layout/list membership mismatch",
    )
    for slot in ("taxonomic-range", "species"):
        wrapper = one(entity, slot)
        blank(wrapper)
        require(not wrapper.attrib and len(wrapper) > 0, "empty pathway organism context")
        for node in wrapper:
            organism(node)
        require(
            len({n.get("frameid") for n in wrapper}) == len(wrapper),
            "duplicate pathway organism context",
        )
    return {
        "id": "MetaCyc:" + frame,
        "native_type": "Pathway",
        "is_class": False,
        "parent_classes": parents,
        "direct_common_name": label,
        "direct_synonyms": synonyms,
        "reaction_list": members,
        "reaction_ordering": ordering,
        "reaction_layout": layouts,
        **retained(entity, CORE),
        **context,
    }


def complete_pathway(body: bytes, source: dict) -> dict:
    _, entity, frame = envelope(body, source, "Pathway")
    require(frame == "P321-PWY", "unsupported whole pathway profile")
    return {**project(entity, frame), "original_base64": base64.b64encode(body).decode("ascii")}


def pathway_metadata(entry: dict, cache_dir: Path) -> dict:
    if request(entry["url"], "META") == "P321-PWY":
        keys(entry, PROVENANCE | {"key", "kind", "path"}, "invalid complete pathway manifest")
        require(
            entry["kind"] == PATHWAY_KIND
            and isinstance(entry["key"], str)
            and bool(entry["key"].strip()),
            "wrong complete pathway kind/key",
        )
        source = {k: entry[k] for k in PROVENANCE_ORDER}
        result = {
            **source,
            "kind": PATHWAY_KIND,
            FIELD: complete_pathway(original_path(entry, cache_dir).read_bytes(), source),
        }
        validate_pathway_metadata(result)
        return result
    result = metadata_build(
        entry, cache_dir, PATHWAY_KIND, FIELD, "META", pathway_identity, project
    )
    validate_pathway_metadata(result)
    return result


def validate_pathway_metadata(metadata: dict) -> None:
    if (
        isinstance(metadata, dict)
        and isinstance(metadata.get(FIELD), dict)
        and (
            metadata[FIELD].get("id") == "MetaCyc:P321-PWY"
            or "original_base64" in metadata[FIELD]
            or "P321-PWY" in str(metadata.get("url", ""))
        )
    ):
        keys(metadata, PROVENANCE | {"kind", FIELD}, "invalid complete pathway metadata")
        require(metadata["kind"] == PATHWAY_KIND, "wrong complete pathway kind")
        source = {k: metadata[k] for k in PROVENANCE_ORDER}
        require(provenance(source, "META") == "P321-PWY", "wrong complete pathway request")
        native = metadata[FIELD]
        require("original_base64" in native, "complete pathway original required")
        expected = complete_pathway(original_bytes(native["original_base64"]), source)
        require(
            json.dumps(native, sort_keys=True) == json.dumps(expected, sort_keys=True),
            "complete pathway projection mismatch",
        )
        return
    metadata_validate(metadata, PATHWAY_KIND, FIELD, "META", "Pathway", project)


def pathway_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_pathway_metadata(metadata)
    native = metadata[FIELD]
    return native["id"], {
        "label": native["direct_common_name"],
        "synonyms": sorted(native["direct_synonyms"]),
        "source": source,
        "entity_type": "native_pathway",
        "label_kind": "canonical",
    }
