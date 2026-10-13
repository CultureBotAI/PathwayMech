"""Typed whole META carrier classes; no chemical or sequence equivalence inference.

The generic protein and Compound cases remain distinct from Protein instances,
assemblies, reaction identities, and their reactive-part cross-references.
"""

from __future__ import annotations

import hashlib
import re
import stat
from html.entities import name2codepoint
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

CARRIER_CLASS_KIND = "metacyc-carrier-class-xml"
HOST = "bf2i-artsymbiocyc.insa-lyon.fr"
FRAME = r"[A-Za-z0-9][A-Za-z0-9_.-]*"
PROVENANCE = {"url", "version", "sha256", "license"}
# Keep canonical output ordering independent of interpreter hash randomization.
PROVENANCE_ORDER = ("license", "url", "version", "sha256")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError("BioCyc carrier: " + message)


def keys(value: Any, expected: set[str], message: str) -> None:
    require(isinstance(value, dict) and set(value) == expected, message)


def request(url: Any, pgdb: str) -> str:
    match = (
        re.fullmatch(rf"https://{re.escape(HOST)}/getxml\?id={pgdb}:({FRAME})", url)
        if isinstance(url, str)
        else None
    )
    require(match is not None, "requires exact native HTTPS " + pgdb + " request")
    return match[1]


def provenance(value: Any, pgdb: str) -> str:
    keys(value, PROVENANCE, "invalid source provenance fields")
    require(
        all(isinstance(v, str) and bool(v.strip()) for v in value.values()),
        "empty source provenance",
    )
    frame = request(value["url"], pgdb)
    require(
        re.fullmatch(r"[0-9]+(?:\.[0-9]+)+", value["version"]) is not None
        and re.fullmatch(r"[0-9a-f]{64}", value["sha256"]) is not None,
        "invalid provenance version/hash",
    )
    return frame


def original_path(entry: dict, cache_dir: Path) -> Path:
    value = entry["path"]
    require(isinstance(value, str) and bool(value), "original path must be relative")
    relative = Path(value)
    require(
        bool(relative.parts) and not relative.is_absolute() and ".." not in relative.parts,
        "original path must be relative without traversal",
    )
    path = cache_dir / relative
    # Canonical build staging can use deliberate original links. Validate the
    # resolved regular file and whole bytes; never accept a device. Literal link
    # identity/retention is also bound by the surrounding preparation contract.
    require(stat.S_ISREG(path.stat().st_mode), "original must resolve to a regular file")
    require(
        hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"],
        "original bytes do not match hash",
    )
    return path


def one(parent: ET.Element, tag: str) -> ET.Element:
    nodes = parent.findall(tag)
    require(len(nodes) == 1, "requires exactly one direct " + tag)
    return nodes[0]


def scalar(parent: ET.Element, tag: str, native: bool = False) -> str:
    node = one(parent, tag)
    require(
        not len(node)
        and node.attrib == ({"datatype": "string"} if native else {})
        and bool((node.text or "").strip())
        and not (node.tail or "").strip(),
        "invalid direct " + tag,
    )
    return node.text.strip()


class _TreeBuilder(ET.TreeBuilder):
    def doctype(self, name: str, pubid: str | None, system: str | None) -> None:
        raise ValueError("BioCyc carrier XML must not contain a DOCTYPE")

    def pi(self, target: str, text: str | None = None) -> None:
        raise ValueError("BioCyc carrier XML must not contain processing instructions")


def native_identity(
    path: Path, url: str, version: str, pgdb: str, *, is_class: bool
) -> tuple[ET.Element, str]:
    require(pgdb in {"META", "ECOLI"}, "unsupported native PGDB")
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
        len(entities) == 1
        and entities[0].tag in ({"Protein", "Compound"} if pgdb == "META" else {"Protein"}),
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
    if pgdb == "META":
        require(
            [node.tag for node in database] == ["species"]
            and scalar(database, "species", True) == "MetaCyc",
            "META species mismatch",
        )
    else:
        require(
            sorted(node.tag for node in database) == ["dblink", "species", "strain"]
            and scalar(database, "species", True) == "Escherichia coli"
            and scalar(database, "strain", True) == "K-12 substr. MG1655",
            "ECOLI species/strain mismatch",
        )
        taxon = one(database, "dblink")
        require(
            not taxon.attrib
            and not (taxon.text or "").strip()
            and sorted(node.tag for node in taxon)
            == sorted(["dblink-db", "dblink-oid", "dblink-relationship", "dblink-URL"])
            and scalar(taxon, "dblink-db") == "NCBI-TAXONOMY-DB"
            and scalar(taxon, "dblink-oid") == "511145"
            and scalar(taxon, "dblink-relationship") == "unification"
            and scalar(taxon, "dblink-URL")
            == "http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=511145",
            "ECOLI native taxon mismatch",
        )
    attributes = {"ID": requested, "orgid": pgdb, "frameid": frame, "detail": "full"}
    if is_class:
        attributes["class"] = "true"
    require(entity.attrib == attributes, "mismatched native top-level identity/type/class")
    return entity, frame


def reference(wrapper: ET.Element, pgdb: str, native_type: str, *, is_class: bool) -> str:
    require(
        not wrapper.attrib
        and not (wrapper.text or "").strip()
        and not (wrapper.tail or "").strip()
        and len(wrapper) == 1,
        "malformed direct reference wrapper",
    )
    node = one(wrapper, native_type)
    frame = node.get("frameid", "")
    attrs = {"resource": f"getxml?{pgdb}:" + frame, "orgid": pgdb, "frameid": frame}
    if is_class:
        attrs["class"] = "true"
    require(
        re.fullmatch(FRAME, frame) is not None
        and node.attrib == attrs
        and not len(node)
        and not (node.text or "").strip()
        and not (node.tail or "").strip(),
        "invalid native reference identity/type/class",
    )
    return frame


def valid_label(value: Any, frame: str) -> bool:
    return (
        isinstance(value, str)
        and bool(value.strip())
        and value == " ".join(value.split())
        and value
        not in {frame, "META:" + frame, "MetaCyc:" + frame, "ECOLI:" + frame, "EcoCyc:" + frame}
        and not value.casefold().startswith(("error", "unknown", "not found"))
        and not any(
            ord(c) < 32
            or 127 <= ord(c) <= 159
            or 0xD800 <= ord(c) <= 0xDFFF
            or ord(c) in {0xFFFE, 0xFFFF}
            for c in value
        )
        and "<" not in value
        and ">" not in value
        and re.search(r"&(?:#|[A-Za-z][A-Za-z0-9]*;)", value) is None
    )


class _NativeName(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.parts: list[str] = []
        self.tags: list[str] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        require(
            tag in {"b", "i", "em", "strong", "sub", "sup"} and not attrs,
            "unsafe native name markup",
        )
        self.tags.append(tag)

    def handle_endtag(self, tag: str) -> None:
        require(bool(self.tags) and self.tags.pop() == tag, "unbalanced native name markup")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def handle_entityref(self, entity: str) -> None:
        require(entity in name2codepoint, "unknown native name entity")
        self.parts.append(chr(name2codepoint[entity]))

    def handle_charref(self, entity: str) -> None:
        number = int(entity[1:], 16) if entity.lower().startswith("x") else int(entity)
        require(
            (
                0x20 <= number <= 0xD7FF
                or 0xE000 <= number <= 0xFFFD
                or 0x10000 <= number <= 0x10FFFF
            )
            and not 127 <= number <= 159,
            "invalid native name character reference",
        )
        self.parts.append(chr(number))

    def unknown_decl(self, data: str) -> None:
        raise ValueError("BioCyc carrier: unsupported native name declaration")

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        raise ValueError("BioCyc carrier: unsupported empty native name markup")

    def handle_comment(self, data: str) -> None:
        raise ValueError("BioCyc carrier: native name contains comment")

    def handle_decl(self, decl: str) -> None:
        raise ValueError("BioCyc carrier: native name contains declaration")

    def handle_pi(self, data: str) -> None:
        raise ValueError("BioCyc carrier: native name contains processing instruction")


def name(node: ET.Element, frame: str) -> str:
    require(
        node.attrib == {"datatype": "string"}
        and not len(node)
        and bool((node.text or "").strip())
        and not (node.tail or "").strip(),
        "invalid direct native name",
    )
    decoder = _NativeName()
    decoder.feed(node.text)
    decoder.close()
    label = " ".join("".join(decoder.parts).split())
    require(not decoder.tags and valid_label(label, frame), "unresolved or unsafe native name")
    return label


def names(entity: ET.Element, frame: str) -> tuple[str, list[str]]:
    label = name(one(entity, "common-name"), frame)
    aliases = [name(node, frame) for node in entity.findall("synonym")]
    require(len(aliases) == len(set(aliases)), "duplicate direct native synonyms")
    return label, sorted(aliases)


def class_native(path: Path, url: str, version: str) -> dict:
    entity, frame = native_identity(path, url, version, "META", is_class=True)
    common = {
        "parent",
        "common-name",
        "synonym",
        "comment",
        "dblink",
        "credits",
        "citation",
        "appears-in-left-side-of",
        "appears-in-right-side-of",
    }
    allowed = common | (
        {"modified-form", "unmodified-form", "instance", "subclass", "location"}
        if entity.tag == "Protein"
        else {"abbrev-name", "n-name", "cml", "cofactors-of"}
    )
    require(all(node.tag in allowed for node in entity), "unsupported direct carrier-class slots")
    parents = [
        reference(node, "META", entity.tag, is_class=True) for node in entity.findall("parent")
    ]
    require(len(parents) == len(set(parents)), "duplicate native parents")
    label, aliases = names(entity, frame)
    result = {
        "id": "MetaCyc:" + frame,
        "native_type": entity.tag,
        "is_class": True,
        "parent_classes": sorted(parents),
        "direct_common_name": label,
        "direct_synonyms": aliases,
    }
    if entity.tag == "Protein":
        require(
            set(parents) in ({"Thioredoxin"}, {"Thioredoxin", "Modified-Proteins"}),
            "unsupported Protein carrier parents",
        )
        relation = "unmodified-form" if "Modified-Proteins" in parents else "modified-form"
        opposite = "modified-form" if relation == "unmodified-form" else "unmodified-form"
        require(not entity.findall(opposite), "conflicting state relations")
        target = reference(one(entity, relation), "META", "Protein", is_class=True)
        require(target != frame, "self state relation")
        result["state_link"] = {"kind": relation, "id": "MetaCyc:" + target}
    else:
        require(parents == ["Hydride-Acceptors"], "unsupported Compound carrier parents")
    return result


def validate_native_class(native: Any, frame: str) -> None:
    require(isinstance(native, dict), "native class metadata must be a mapping")
    protein = native.get("native_type") == "Protein"
    expected = {
        "id",
        "native_type",
        "is_class",
        "parent_classes",
        "direct_common_name",
        "direct_synonyms",
    }
    keys(
        native,
        expected | ({"state_link"} if protein else set()),
        "incomplete native class metadata",
    )
    require(
        native["id"] == "MetaCyc:" + frame
        and native["is_class"] is True
        and isinstance(native["native_type"], str)
        and native["native_type"] in {"Protein", "Compound"},
        "invalid native class identity/type",
    )
    parents = native["parent_classes"]
    allowed = (
        [["Thioredoxin"], ["Modified-Proteins", "Thioredoxin"]]
        if protein
        else [["Hydride-Acceptors"]]
    )
    require(parents in allowed, "invalid native class parents")
    require(valid_label(native["direct_common_name"], frame), "invalid native class common-name")
    aliases = native["direct_synonyms"]
    require(
        isinstance(aliases, list)
        and all(valid_label(item, frame) for item in aliases)
        and aliases == sorted(set(aliases)),
        "invalid native class synonyms",
    )
    if protein:
        link = native["state_link"]
        keys(link, {"kind", "id"}, "invalid class state link")
        require(
            link["kind"]
            == ("unmodified-form" if "Modified-Proteins" in parents else "modified-form")
            and isinstance(link["id"], str)
            and re.fullmatch("MetaCyc:" + FRAME, link["id"]) is not None
            and link["id"] != native["id"],
            "invalid class state link identity",
        )


def validate_class_metadata(metadata: Any) -> None:
    keys(
        metadata,
        PROVENANCE | {"kind", "native_carrier_class"},
        "incomplete typed carrier-class provenance",
    )
    frame = provenance({key: metadata[key] for key in PROVENANCE}, "META")
    require(metadata["kind"] == CARRIER_CLASS_KIND, "wrong carrier-class source kind")
    validate_native_class(metadata["native_carrier_class"], frame)


def class_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(entry, PROVENANCE | {"key", "kind", "path"}, "unsupported carrier-class manifest fields")
    require(
        entry["kind"] == CARRIER_CLASS_KIND
        and isinstance(entry["key"], str)
        and bool(entry["key"]),
        "wrong carrier-class kind/key",
    )
    source = {key: entry[key] for key in PROVENANCE_ORDER}
    provenance(source, "META")
    path = original_path(entry, cache_dir)
    result = {
        **source,
        "kind": CARRIER_CLASS_KIND,
        "native_carrier_class": class_native(path, entry["url"], entry["version"]),
    }
    validate_class_metadata(result)
    return result


def class_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_class_metadata(metadata)
    native = metadata["native_carrier_class"]
    return native["id"], {
        "label": native["direct_common_name"],
        "synonyms": sorted(set(native["direct_synonyms"]) - {native["direct_common_name"]}),
        "source": source,
        "entity_type": "protein_class" if native["native_type"] == "Protein" else "chemical_class",
    }
