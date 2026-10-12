"""Whole Rhea Polymer subjects, distinct from GenericPolypeptide components."""

from __future__ import annotations

import gzip
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import PROVENANCE, _TreeBuilder, keys, original_path, require

RHEA_POLYMER_KIND = "rhea-polymer-rdf"
RHEA_URL = "https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RDFS = "{http://www.w3.org/2000/01/rdf-schema#}"
RH = "{http://rdf.rhea-db.org/}"
URI = "http://rdf.rhea-db.org/"
TRANS = {"α": "alpha", "β": "beta", "γ": "gamma", "ω": "omega", "→": "->", "↔": "<->", "−": "-"}
TOKEN = re.compile(r"<(/?)(i|small|sub|sup)>|&#(x[0-9a-fA-F]+|[0-9]+);|([^<&]+)")


PROVENANCE_ORDER = ("license", "url", "version", "sha256")


def comparison_projection(value: str) -> str:
    require(isinstance(value, str) and bool(value), "missing Polymer markup value")
    stack = [("root", [])]
    offset = 0
    while offset < len(value):
        token = TOKEN.match(value, offset)
        require(token is not None, "unsupported Polymer markup/reference")
        offset = token.end()
        closing, tag, code, text = token.groups()
        if tag:
            if not closing:
                require(stack[-1][0] != "sup", "nested Polymer superscript")
                stack.append((tag, []))
            else:
                require(len(stack) > 1 and stack[-1][0] == tag, "unbalanced Polymer markup")
                _, parts = stack.pop()
                result = "".join(parts)
                require(bool(result), "empty Polymer markup")
                if tag == "sup":
                    require(
                        re.fullmatch(r"[1-9][0-9]*|-", result) is not None,
                        "unsupported Polymer superscript",
                    )
                    result = "(" + result + ")"
                stack[-1][1].append(result)
        else:
            if code:
                number = int(code[1:], 16) if code.startswith("x") else int(code)
                require(number <= 0x10FFFF, "invalid Polymer Unicode reference")
                text = chr(number)
            require(all(32 <= ord(c) < 127 or c in TRANS for c in text), "unsafe Polymer character")
            stack[-1][1].append("".join(TRANS.get(c, c) for c in text))
    require(len(stack) == 1, "unclosed Polymer markup")
    return "".join(stack[0][1])


def plain_name(value: Any) -> None:
    require(
        isinstance(value, str)
        and bool(value.strip())
        and value == value.strip()
        and all(32 <= ord(c) < 127 for c in value),
        "unsafe Polymer plain name",
    )
    without_arrows = value.replace("<->", "").replace("->", "")
    require(
        "<" not in without_arrows
        and ">" not in without_arrows
        and "&" not in value
        and not value.casefold().startswith(("error", "unknown", "not found")),
        "unsafe Polymer plain name markup",
    )


def fragment_node(xml: str) -> ET.Element:
    require(isinstance(xml, str) and bool(xml), "missing Polymer RDF fragment")
    holder = ET.fromstring(
        "<retained>" + xml + "</retained>", parser=ET.XMLParser(target=_TreeBuilder())
    )
    require(
        len(holder) == 1 and not (holder.text or "").strip() and not (holder[0].tail or "").strip(),
        "invalid Polymer fragment wrapper",
    )
    return holder[0]


def project(uri: str, fragments: list[str]) -> dict:
    match = re.fullmatch(r"http://rdf\.rhea-db\.org/Compound_([0-9]+)", uri)
    require(
        match is not None and isinstance(fragments, list) and bool(fragments),
        "invalid Polymer URI/fragments",
    )
    values = defaultdict(list)
    for fragment in fragments:
        n = fragment_node(fragment)
        require(
            n.tag == RDF + "Description"
            and n.attrib == {RDF + "about": uri}
            and not (n.text or "").strip(),
            "invalid Polymer description identity",
        )
        for c in n:
            require(not len(c) and not (c.tail or "").strip(), "nested Polymer RDF fact")
            semantic = (c.tag, tuple(sorted(c.attrib.items())), c.text)
            if semantic not in values[c.tag]:
                values[c.tag].append(semantic)
    expected = {
        RH + k
        for k in [
            "id",
            "accession",
            "name",
            "htmlName",
            "formula",
            "charge",
            "polymerizationIndex",
            "underlyingChebi",
        ]
    } | {RDFS + "subClassOf", RDF + "type"}
    require(
        set(values) == expected and all(len(v) == 1 for v in values.values()),
        "missing/conflicting/unknown Polymer assertions",
    )
    result = {}
    for tag, facts in values.items():
        _, attrs_tuple, text = facts[0]
        attrs = dict(attrs_tuple)
        key = tag.rsplit("}", 1)[1]
        if key in {"type", "subClassOf", "underlyingChebi"}:
            require(
                set(attrs) == {RDF + "resource"} and not (text or "").strip(),
                "invalid Polymer resource property",
            )
            result[key] = attrs[RDF + "resource"]
        else:
            expected_attrs = (
                {RDF + "datatype": "http://www.w3.org/2001/XMLSchema#long"} if key == "id" else {}
            )
            require(
                attrs == expected_attrs and isinstance(text, str) and bool(text),
                "invalid Polymer literal property",
            )
            result[key] = text
    ident = match[1]
    require(
        result["id"] == ident
        and result["accession"] == "POLYMER:" + ident
        and result["type"] == "http://www.w3.org/2000/01/rdf-schema#Class"
        and result["subClassOf"] == URI + "Polymer"
        and re.fullmatch(r"n(?:[+-][1-9][0-9]*)?", result["polymerizationIndex"]) is not None
        and re.fullmatch(
            r"http://purl\.obolibrary\.org/obo/CHEBI_[0-9]+", result["underlyingChebi"]
        )
        is not None,
        "inconsistent Polymer identity/type/index/underlying ChEBI",
    )
    plain_name(result["name"])
    require(
        comparison_projection(result["htmlName"]) == result["name"],
        "Polymer HTML/plain names disagree",
    )
    for key, pattern in [("formula", r"[A-Za-z0-9().+\-]+"), ("charge", r"[0-9()n+\-]+")]:
        require(
            re.fullmatch(pattern, comparison_projection(result[key])) is not None,
            "unsafe Polymer " + key,
        )
    return {
        "id": "RHEA-COMP:" + ident,
        "uri": uri,
        "native_accession": result["accession"],
        "name": result["name"],
        "html_name": result["htmlName"],
        "formula": result["formula"],
        "charge": result["charge"],
        "polymerization_index": result["polymerizationIndex"],
        "underlying_chebi": result["underlyingChebi"],
        "rdf_type": result["type"],
        "native_subclass": result["subClassOf"],
        "fragments": fragments,
    }


def polymer_hint(node: ET.Element) -> bool:
    return any(
        c.tag == RH + "polymerizationIndex"
        or c.tag == RH + "accession"
        and (c.text or "").strip().upper().startswith("POLYMER")
        or c.tag == RDFS + "subClassOf"
        and c.get(RDF + "resource") == URI + "Polymer"
        for c in node
    )


def read_polymers(path: Path) -> dict[str, dict]:
    # Check all decompressed input for DTD/entity declarations before XML expansion.
    # PI events are rejected by the actual streaming parse below.
    with gzip.open(path, "rb") as stream:
        tail = b""
        while chunk := stream.read(1024 * 1024):
            block = tail + chunk
            require(
                re.search(rb"<!\s*(?:DOCTYPE|ENTITY)\b", block.replace(b"\x00", b""), re.I) is None,
                "Rhea RDF must not contain a DTD/entity declaration",
            )
            tail = block[-64:]
    subjects = defaultdict(list)
    candidates = set()
    with gzip.open(path, "rb") as stream:
        depth = 0
        for event, node in ET.iterparse(stream, events=("start", "end", "pi")):
            require(event != "pi", "Rhea RDF must not contain processing instructions")
            if event == "start":
                depth += 1
                if depth == 1:
                    root = node
                    require(
                        root.tag == RDF + "RDF" and not root.attrib, "invalid Rhea RDF container"
                    )
                continue
            if depth == 2:
                require(
                    not (root.text or "").strip() and not (node.tail or "").strip(),
                    "mixed Rhea RDF container text",
                )
                uri = node.get(RDF + "about", "")
                hint = polymer_hint(node)
                # All Compound fragments are retained until all later identities
                # are resolved; malformed Polymer-looking subjects are also kept.
                if "Compound" in uri or hint:
                    subjects[uri].append(ET.tostring(node, encoding="unicode"))
                if hint:
                    candidates.add(uri)
                root.clear()
            depth -= 1
    projected = {}
    for uri in sorted(candidates):
        native = project(uri, subjects[uri])
        require(native["id"] not in projected, "duplicate Polymer accession")
        projected[native["id"]] = native
    require(bool(projected), "Rhea source contains no whole Polymers")
    return projected


def validate_polymer_metadata(metadata: Any) -> None:
    keys(metadata, PROVENANCE | {"kind", "native_polymers"}, "incomplete Polymer provenance")
    require(
        metadata["kind"] == RHEA_POLYMER_KIND
        and metadata["url"] == RHEA_URL
        and all(isinstance(metadata[k], str) and bool(metadata[k].strip()) for k in PROVENANCE)
        and re.fullmatch(r"[0-9a-f]{64}", metadata["sha256"]) is not None,
        "invalid Polymer provenance",
    )
    natives = metadata["native_polymers"]
    require(isinstance(natives, dict) and bool(natives), "missing whole Polymer metadata")
    for identifier, native in natives.items():
        require(isinstance(native, dict), "invalid Polymer native mapping")
        expected = project(native.get("uri"), native.get("fragments"))
        require(
            identifier == expected["id"]
            and json.dumps(native, sort_keys=True) == json.dumps(expected, sort_keys=True),
            "Polymer metadata differs from complete RDF projection",
        )


def polymer_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(entry, PROVENANCE | {"key", "kind", "path"}, "unsupported Polymer manifest fields")
    require(
        entry["kind"] == RHEA_POLYMER_KIND
        and isinstance(entry["key"], str)
        and bool(entry["key"].strip()),
        "invalid Polymer kind/key",
    )
    path = original_path(entry, cache_dir)
    result = {
        **{k: entry[k] for k in PROVENANCE_ORDER},
        "kind": RHEA_POLYMER_KIND,
        "native_polymers": read_polymers(path),
    }
    validate_polymer_metadata(result)
    return result


def polymer_term(metadata: dict, source: str, identifier: str) -> tuple[str, dict]:
    # Validate the complete selected source, not only a convenient first entry.
    validate_polymer_metadata(metadata)
    native = metadata["native_polymers"][identifier]
    return identifier, {
        "label": native["name"],
        "synonyms": [],
        "source": source,
        "entity_type": "rhea_polymer",
        "label_kind": "canonical",
    }
