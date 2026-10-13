"""Closed original-context helpers for the explicit native authority modes.

Opaque scientific context is retained, never interpreted as a direct name.
The old carrier, state and unnamed-complex contracts remain unchanged.
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections.abc import Callable
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import (
    FRAME,
    PROVENANCE,
    _TreeBuilder,
    keys,
    name,
    one,
    original_path,
    provenance,
    reference,
    require,
)

PROVENANCE_ORDER = ("license", "url", "version", "sha256")


def blank(node: ET.Element) -> None:
    require(
        not (node.text or "").strip() and all(not (c.tail or "").strip() for c in node),
        "mixed native container text",
    )


def attributes(entity: ET.Element, frame: str, pgdb: str, tag: str, is_class: bool) -> None:
    wanted = {"ID": pgdb + ":" + frame, "orgid": pgdb, "frameid": frame, "detail": "full"}
    if is_class:
        wanted["class"] = "true"
    require(entity.tag == tag and entity.attrib == wanted, "invalid native entity identity")
    blank(entity)


def ref_node(
    node: ET.Element, pgdb: str, tag: str, *, is_class: bool = False, local: bool = False
) -> dict:
    frame = node.get("frameid", "")
    attrs = {"resource": "getxml?" + pgdb + ":" + frame, "orgid": pgdb, "frameid": frame}
    if is_class:
        attrs["class"] = "true"
    accepted = [attrs]
    if local:
        accepted.append({**attrs, "resource": "#" + pgdb + ":" + frame})
    require(
        re.fullmatch(FRAME, frame) is not None
        and node.tag == tag
        and node.attrib in accepted
        and not len(node)
        and not (node.text or "").strip()
        and not (node.tail or "").strip(),
        "invalid native reference",
    )
    prefix = "MetaCyc" if pgdb == "META" else "EcoCyc"
    return {
        "id": prefix + ":" + frame,
        "native_type": tag,
        "is_class": is_class,
        "attributes": dict(node.attrib),
    }


def charged_context_reference(node: ET.Element, pgdb: str, tag: str, *, is_class: bool) -> dict:
    """Literal charged frame tokens in two retained META context roles only.

    These are native XML references, not form-encoded requests or selected
    public identifiers. In particular, never decode a literal '+' as a space.
    The carrier/request/public-ID contracts deliberately remain unchanged.
    """
    require(
        pgdb == "META" and (tag, is_class) in {("Compound", True), ("Reaction", False)},
        "unsupported charged context role",
    )
    frame = node.get("frameid", "")
    attrs = {"resource": "getxml?META:" + frame, "orgid": "META", "frameid": frame}
    if is_class:
        attrs["class"] = "true"
    require(
        frame
        in (
            {"4Fe-4S+1", "4Fe-4S+2", "4Fe-4S+3"}
            if tag == "Compound"
            else {"PYRUVATE-DEHYDROGENASE-NADP+-RXN"}
        )
        and node.tag == tag
        and node.attrib == attrs
        and not len(node)
        and not (node.text or "").strip()
        and not (node.tail or "").strip(),
        "invalid charged context reference",
    )
    return {
        "id": "MetaCyc:" + frame,
        "native_type": tag,
        "is_class": is_class,
        "attributes": dict(node.attrib),
    }


def refs(entity: ET.Element, slot: str, pgdb: str, tag: str, *, is_class: bool) -> list[dict]:
    result = []
    for wrapper in entity.findall(slot):
        reference(wrapper, pgdb, tag, is_class=is_class)
        result.append(ref_node(wrapper[0], pgdb, tag, is_class=is_class))
    require(len({r["id"] for r in result}) == len(result), "duplicate " + slot + " references")
    require(
        all(r["attributes"]["frameid"] != entity.get("frameid") for r in result),
        "self " + slot + " reference",
    )
    return result


def direct_names(entity: ET.Element, frame: str) -> tuple[str, list[str]]:
    label = name(one(entity, "common-name"), frame)
    aliases = [name(n, frame) for n in entity.findall("synonym")]

    def normalize(value: str) -> str:
        return " ".join(unicodedata.normalize("NFKC", value).split()).casefold()

    all_names = [normalize(v) for v in [label, *aliases]]
    require(len(set(all_names)) == len(all_names), "duplicate canonical name or synonyms")
    return label, aliases


def integer(node: ET.Element) -> int:
    require(
        node.attrib == {"datatype": "integer"}
        and not len(node)
        and re.fullmatch(r"[1-9][0-9]*", node.text or "") is not None
        and not (node.tail or "").strip(),
        "invalid explicit positive integer",
    )
    return int(node.text)


def context_identity(node: ET.Element, pgdb: str, tag: str) -> None:
    frame = node.get("frameid", "")
    require(
        re.fullmatch(FRAME, frame) is not None and node.tag == tag,
        "invalid context native identity",
    )
    if "resource" in node.attrib:
        ref_node(node, pgdb, tag, is_class=node.get("class") == "true", local=True)
    else:
        require(
            node.attrib
            == {
                "ID": pgdb + ":" + frame,
                "orgid": pgdb,
                "frameid": frame,
                "detail": node.get("detail"),
            }
            and node.get("detail") in {"low", "full"},
            "invalid context native attributes",
        )
        blank(node)


def activity(node: ET.Element, pgdb: str, *, charged_reaction: bool = False) -> None:
    context_identity(node, pgdb, "Enzymatic-Reaction")
    require("resource" not in node.attrib, "cofactor/activity proof requires whole context")
    for slot, tag in [("enzyme", "Protein"), ("reaction", "Reaction")]:
        wrapper = one(node, slot)
        require(not wrapper.attrib and len(wrapper) == 1, "invalid activity " + slot)
        blank(wrapper)
        target = wrapper[0]
        if charged_reaction and tag == "Reaction" and "+" in target.get("frameid", ""):
            charged_context_reference(target, pgdb, tag, is_class=False)
        else:
            ref_node(target, pgdb, tag, is_class=target.get("class") == "true", local=True)


def publication_context(node: ET.Element, pgdb: str) -> None:
    """Closed publication context used by GO and quantitative annotations."""
    require("class" not in node.attrib, "publication must be an instance")
    context_identity(node, pgdb, "Publication")
    if "resource" in node.attrib:
        return
    allowed = {"title", "source", "pubmed-id", "author", "year"}
    require(all(c.tag in allowed for c in node), "unsupported annotation publication slot")
    for tag in allowed - {"author"}:
        require(len(node.findall(tag)) <= 1, "duplicate annotation publication slot")
    require(len(node) > 0, "empty annotation publication")
    for child in node:
        datatype = "integer" if child.tag == "year" else "string"
        require(
            child.attrib == {"datatype": datatype}
            and not len(child)
            and bool((child.text or "").strip())
            and not (child.tail or "").strip(),
            "invalid annotation publication value",
        )
        if child.tag in {"year", "pubmed-id"}:
            require(
                re.fullmatch(r"[0-9]+", child.text or "") is not None,
                "invalid annotation publication number",
            )


def go_annotation(node: ET.Element, pgdb: str) -> None:
    blank(node)
    require(
        pgdb == "ECOLI"
        and not node.attrib
        and all(c.tag in {"GO-Term", "evidence"} for c in node)
        and bool(node.findall("evidence")),
        "invalid GO annotation wrapper",
    )
    term = one(node, "GO-Term")
    frame = term.get("frameid", "")
    require(
        re.fullmatch(r"GO:[0-9]{7}", frame) is not None
        and term.attrib
        == {"resource": "getxml?ECOLI:" + frame, "orgid": pgdb, "frameid": frame, "class": "true"}
        and not len(term)
        and not (term.text or "").strip()
        and not (term.tail or "").strip(),
        "invalid native GO class reference",
    )
    for evidence in node.findall("evidence"):
        blank(evidence)
        require(
            not evidence.attrib
            and all(c.tag in {"Evidence-Code", "Publication", "with"} for c in evidence),
            "invalid GO evidence wrapper",
        )
        code = one(evidence, "Evidence-Code")
        if "resource" in code.attrib:
            ref_node(code, pgdb, "Evidence-Code", is_class=True, local=True)
        else:
            code_frame = code.get("frameid", "")
            require(re.fullmatch(FRAME, code_frame) is not None, "invalid evidence code frame")
            attributes(code, code_frame, pgdb, "Evidence-Code", True)
            require(
                all(c.tag in {"parent", "common-name", "comment"} for c in code)
                and len(code.findall("comment")) <= 1,
                "invalid whole evidence code context",
            )
            name(one(code, "common-name"), code_frame)
            for parent in code.findall("parent"):
                blank(parent)
                require(not parent.attrib and len(parent) == 1, "invalid evidence parent")
                ref_node(parent[0], pgdb, "Evidence-Code", is_class=True, local=True)
            for comment in code.findall("comment"):
                require(
                    comment.attrib == {"datatype": "string"}
                    and not len(comment)
                    and bool((comment.text or "").strip()),
                    "invalid evidence code comment",
                )
        for publication in evidence.findall("Publication"):
            publication_context(publication, pgdb)
        require(len(evidence.findall("with")) <= 1, "duplicate GO evidence with context")
        for with_node in evidence.findall("with"):
            require(
                with_node.attrib == {"datatype": "string"}
                and not len(with_node)
                and not (with_node.tail or "").strip(),
                "invalid GO evidence with context",
            )


def ancillary(entity: ET.Element, allowed: set[str], core: set[str], pgdb: str) -> None:
    require(all(n.tag in allowed | core for n in entity), "unsupported direct native slot")
    singles = {
        "cml",
        "gibbs-0",
        "orphan",
        "physiologically-relevant",
        "molecular-weight-exp",
        "molecular-weight",
        "monoisotopic-mw",
        "inchi",
        "inchi-key",
        "abbrev-name",
        "regulates",
        "cofactors-of",
        "catalyzes",
        "species",
        "credits",
        "appears-in-left-side-of",
        "appears-in-right-side-of",
        "in-pathway",
        "enzymatic-reaction",
        "component-of",
        "location",
    }
    require(all(len(entity.findall(tag)) <= 1 for tag in singles), "duplicate scalar/context slot")
    xrefs = {}
    for n in entity:
        if n.tag in core:
            continue
        require(not (n.tail or "").strip(), "mixed native slot tail")
        if n.tag in {"comment", "abbrev-name", "inchi", "inchi-key"}:
            require(
                n.attrib == {"datatype": "string"} and not len(n) and bool((n.text or "").strip()),
                "invalid native string context",
            )
        elif n.tag in {"molecular-weight", "monoisotopic-mw", "molecular-weight-exp", "gibbs-0"}:
            unit = (
                "kcal/mol"
                if n.tag == "gibbs-0"
                else "kD"
                if n.tag == "molecular-weight-exp"
                else "Daltons"
            )
            require(
                n.attrib == {"datatype": "float", "units": unit}
                and re.fullmatch(
                    r"-?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[Ee][+-]?[0-9]+)?", n.text or ""
                )
                is not None
                and (
                    all(c.tag == "evidence" for c in n)
                    if n.tag == "gibbs-0"
                    else len(n) <= 1 and all(c.tag == "citation" for c in n)
                    if n.tag == "molecular-weight-exp"
                    else not len(n)
                ),
                "invalid native quantitative context",
            )
            if n.tag == "molecular-weight-exp":
                for citation in n:
                    blank(citation)
                    require(not citation.attrib and len(citation) > 0, "invalid mass citation")
                    for publication in citation:
                        publication_context(publication, pgdb)
        elif n.tag == "orphan":
            require(
                not n.attrib and not len(n) and n.text in {"NO", "YES"}, "invalid orphan context"
            )
        elif n.tag == "physiologically-relevant":
            require(
                n.attrib == {"datatype": "boolean"} and not len(n) and n.text in {"true", "false"},
                "invalid physiological boolean",
            )
        elif n.tag == "ec-number":
            require(
                not n.attrib
                and re.fullmatch(
                    r"EC-(?:[0-9]+(?:\.(?:[0-9]+|-)){3}|[0-9]+(?:\.[0-9]+){2})",
                    n.text or "",
                )
                is not None
                and len(n) <= 1
                and all(
                    c.tag == "official"
                    and not c.attrib
                    and not len(c)
                    and c.text in {"true", "false", "T", "NIL"}
                    for c in n
                ),
                "invalid EC context",
            )
        elif n.tag == "has-go-term":
            go_annotation(n, pgdb)
        elif n.tag in {"component-of", "location"}:
            blank(n)
            require(not n.attrib and len(n) > 0, "invalid component/location context")
            tag = "Protein" if n.tag == "component-of" else "cco"
            values = [ref_node(child, pgdb, tag) for child in n]
            require(
                len({v["id"] for v in values}) == len(values)
                and all(v["attributes"]["frameid"] != entity.get("frameid") for v in values),
                "duplicate/self component/location context",
            )
        elif n.tag == "cml":
            blank(n)
            require(
                not n.attrib
                and len(n) == 1
                and n[0].tag == "molecule"
                and n[0].get("id") == entity.get("frameid"),
                "CML identity mismatch",
            )
            molecule = n[0]
            blank(molecule)
            require(
                set(molecule.attrib) == {"id", "title", "formalCharge"}
                and bool(molecule.get("title"))
                and re.fullmatch(r"-?[0-9]+", molecule.get("formalCharge", "")) is not None,
                "invalid CML molecule attributes",
            )
            tags = [c.tag for c in molecule]
            require(
                set(tags)
                in [
                    {"atomArray", "bondArray", "formula", "string"},
                    {"atomArray", "bondArray", "formula", "string", "float"},
                ]
                and len(tags) == len(set(tags)),
                "invalid CML child cardinality",
            )
            formula = one(molecule, "formula")
            require(
                set(formula.attrib) == {"concise"}
                and not len(formula)
                and not (formula.text or "").strip(),
                "invalid CML formula",
            )
        elif n.tag == "dblink":
            blank(n)
            required = {"dblink-db", "dblink-oid", "dblink-relationship"}
            require(
                not n.attrib
                and set(c.tag for c in n) in [required, required | {"dblink-URL"}]
                and len(n) == len(set(c.tag for c in n))
                and all(not c.attrib and not len(c) and bool((c.text or "").strip()) for c in n),
                "invalid direct dblink",
            )
            identity = (n.findtext("dblink-db"), n.findtext("dblink-oid"))
            value = [(c.tag, c.text) for c in n]
            require(identity not in xrefs or xrefs[identity] == value, "conflicting direct xref")
            xrefs[identity] = value
        else:
            blank(n)
            require(not n.attrib and len(n) > 0, "empty or attributed native context")
            if n.tag == "credits":
                require(
                    all(c.tag in {"created", "revised", "last-curated"} for c in n),
                    "invalid credits context",
                )
            elif n.tag in {"catalyzes", "cofactors-of", "enzymatic-reaction"}:
                for c in n:
                    activity(
                        c,
                        pgdb,
                        charged_reaction=n.tag == "cofactors-of" and entity.tag == "Compound",
                    )
            else:
                tag = {
                    "citation": "Publication",
                    "species": "Organism",
                    "regulates": "Regulation",
                    "appears-in-left-side-of": "Reaction",
                    "appears-in-right-side-of": "Reaction",
                    "in-pathway": "Pathway",
                }[n.tag]
                for c in n:
                    context_identity(c, pgdb, tag)


def retained(entity: ET.Element, core: set[str]) -> dict:
    slots = [{"tag": n.tag, "xml": ET.tostring(n, encoding="unicode")} for n in entity]
    return {
        "native_attributes": dict(entity.attrib),
        "direct_slot_order": [n.tag for n in entity],
        "source_slots": slots,
        "context_slots": [s for s in slots if s["tag"] not in core],
    }


def rebuild(native: Any, tag: str) -> ET.Element:
    require(
        isinstance(native, dict) and isinstance(native.get("native_attributes"), dict),
        "missing original native attributes",
    )
    require(
        all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in native["native_attributes"].items()
        ),
        "invalid original native attributes",
    )
    slots = native.get("source_slots")
    require(isinstance(slots, list) and bool(slots), "missing original native slots")
    entity = ET.Element(tag, native["native_attributes"])
    for slot in slots:
        keys(slot, {"tag", "xml"}, "invalid retained native slot wrapper")
        require(
            isinstance(slot["tag"], str) and isinstance(slot["xml"], str),
            "invalid retained slot text",
        )
        holder = ET.fromstring(
            "<retained>" + slot["xml"] + "</retained>", parser=ET.XMLParser(target=_TreeBuilder())
        )
        require(
            len(holder) == 1 and not (holder.text or "").strip(),
            "retained slot must contain one subtree",
        )
        n = holder[0]
        require(
            n.tag == slot["tag"] and not (n.tail or "").strip(), "retained slot tag/text mismatch"
        )
        entity.append(n)
    return entity


def metadata_validate(
    metadata: Any, kind: str, field: str, pgdb: str, tag: str, projector: Callable
) -> None:
    keys(metadata, PROVENANCE | {"kind", field}, "incomplete typed native provenance")
    frame = provenance({k: metadata[k] for k in PROVENANCE_ORDER}, pgdb)
    require(metadata["kind"] == kind, "wrong typed native kind")
    native = metadata[field]
    projected = projector(rebuild(native, tag), frame)
    require(
        json.dumps(native, sort_keys=True) == json.dumps(projected, sort_keys=True),
        "native metadata differs from complete original slot projection",
    )


def metadata_build(
    entry: dict,
    cache_dir: Path,
    kind: str,
    field: str,
    pgdb: str,
    reader: Callable,
    projector: Callable,
) -> dict:
    keys(entry, PROVENANCE | {"key", "kind", "path"}, "unsupported native manifest fields")
    require(
        entry["kind"] == kind and isinstance(entry["key"], str) and bool(entry["key"].strip()),
        "wrong native kind/key",
    )
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    provenance(source, pgdb)
    path = original_path(entry, cache_dir)
    entity, frame = reader(path, entry["url"], entry["version"])
    return {**source, "kind": kind, field: projector(entity, frame)}
