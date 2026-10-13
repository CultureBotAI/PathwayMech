"""Shared native PathBank parsing and opt-in whole-document context authority."""

from __future__ import annotations

import hashlib
import math
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, unquote, urldefrag, urljoin, urlsplit
from xml.etree import ElementTree

from pathwaymech.pathbank_provenance import PATHBANK_ARCHIVE_URL


def _pathbank_request(url: str) -> str | None:
    """Only a native per-pathway request can select a multi-Pathway export."""
    parsed = urlsplit(url)
    if not (parsed.path.startswith("/view/") or parsed.path.endswith("/download")):
        return None  # Legacy archive artifacts still require a single Pathway.
    request = re.fullmatch(r"/view/(SMP[0-9]+)/download", parsed.path)
    if (
        parsed.scheme != "https"
        or parsed.netloc != "pathbank.org"
        or parsed.fragment
        or any(char.isspace() for char in url)
        or not request
        or parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True)
        != [("type", "owl_markup")]
    ):
        raise ValueError("PathBank selection requires an exact official BioPAX download URL")
    return request[1]


def pathbank_terms(
    root: ElementTree.Element,
    *,
    url: str = "",
    archive_root: str | None = None,
) -> Iterator[tuple[str, str, list[str]]]:
    """Read one native pathway and its declared local graph objects, not xref labels.

    SMPDB unification assertions establish the PathBank accession; a PathWhiz
    filename is never an accession authority. Local objects assert source-graph
    existence only, not membership, catalysis or an external chemical identity.
    """
    bp = "{http://www.biopax.org/release/biopax-level3.owl#}"
    rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
    base = root.get("{http://www.w3.org/XML/1998/namespace}base", "")
    if any(
        "{http://www.w3.org/XML/1998/namespace}base" in node.attrib
        for node in root.iter()
        if node is not root
    ):
        raise ValueError("PathBank authority does not support nested XML base overrides")

    def subject(node: ElementTree.Element) -> str:
        native_id = node.get(rdf + "ID")
        if native_id is not None and node.get(rdf + "about") is not None:
            raise ValueError("PathBank RDF subject cannot declare both ID and about")
        value = "#" + native_id if native_id else node.get(rdf + "about", "")
        return urljoin(base, value) if value else ""

    def labels(node: ElementTree.Element) -> list[str]:
        return [
            item.text.strip()
            for name in ("displayName", "standardName", "name")
            for item in node.findall(bp + name)
            if item.text and item.text.strip()
        ]

    index: dict[str, ElementTree.Element] = {}
    for node in root:
        uri = subject(node)
        if uri:
            if uri in index:
                raise ValueError(f"PathBank source has duplicate RDF subject: {uri}")
            index[uri] = node

    def native_accession(pathway: ElementTree.Element) -> str:
        accessions = set()
        for link in pathway.findall(bp + "xref"):
            xref = index.get(urljoin(base, link.get(rdf + "resource", "")))
            if xref is None or xref.tag != bp + "UnificationXref":
                continue
            databases = {(item.text or "").strip().casefold() for item in xref.findall(bp + "db")}
            if "smpdb" not in databases:
                continue
            if databases != {"smpdb"}:
                raise ValueError("PathBank SMPDB unification xref has conflicting databases")
            values = {(item.text or "").strip() for item in xref.findall(bp + "id")}
            if not values or any(not re.fullmatch(r"SMP[0-9]+", value) for value in values):
                raise ValueError("PathBank pathway has an invalid native SMPDB accession")
            accessions.update(values)
        if len(accessions) != 1:
            raise ValueError(
                "PathBank pathway requires one unambiguous SMPDB unification accession"
            )
        accession = next(iter(accessions))
        about = pathway.get(rdf + "about", "")
        if about.startswith(("http://identifiers.org/smpdb/", "https://identifiers.org/smpdb/")):
            if not re.fullmatch(r"https?://identifiers\.org/smpdb/" + accession, about):
                raise ValueError("PathBank pathway URI and SMPDB xref must agree")
        return accession

    pathways = root.findall(bp + "Pathway")
    child_terms: list[tuple[str, str, list[str]]] = []
    if archive_root is None:
        requested = _pathbank_request(url)
    else:
        if (
            url != PATHBANK_ARCHIVE_URL
            or not isinstance(archive_root, str)
            or not re.fullmatch(r"SMP[0-9]+", archive_root)
        ):
            raise ValueError("PathBank archive selection requires exact archive/root provenance")
        requested = archive_root
    if requested is None:
        if len(pathways) != 1:
            raise ValueError("PathBank authority requires exactly one native Pathway")
        pathway = pathways[0]
        accession = native_accession(pathway)
    else:
        by_accession: dict[str, ElementTree.Element] = {}
        for candidate in pathways:
            accession = native_accession(candidate)
            if not re.fullmatch(
                r"https?://identifiers\.org/smpdb/" + accession,
                candidate.get(rdf + "about", ""),
            ):
                raise ValueError("PathBank selected export requires matching native pathway URIs")
            if accession in by_accession:
                raise ValueError("PathBank source repeats a native pathway accession")
            by_accession[accession] = candidate
        if requested not in by_accession:
            raise ValueError("PathBank request and native pathway accessions disagree")
        pathway, accession = by_accession[requested], requested

        def resolve(link: ElementTree.Element) -> ElementTree.Element:
            uri = urljoin(base, link.get(rdf + "resource", ""))
            if uri not in index:
                raise ValueError(f"PathBank source has an unresolved pathway link: {uri}")
            return index[uri]

        def processes(node: ElementTree.Element) -> list[ElementTree.Element]:
            result = [resolve(link) for link in node.findall(bp + "pathwayComponent")]
            for link in node.findall(bp + "pathwayOrder"):
                step = resolve(link)
                if step.tag not in {bp + "PathwayStep", bp + "BiochemicalPathwayStep"}:
                    raise ValueError("PathBank pathwayOrder must identify a native pathway step")
                result.extend(
                    resolve(link)
                    for tag in ("stepProcess", "stepConversion")
                    for link in step.findall(bp + tag)
                )
            return result

        primary = processes(pathway)
        expanded = list(primary)
        for node in primary:
            if node.tag == bp + "Catalysis":
                expanded.extend(resolve(link) for link in node.findall(bp + "controlled"))
        if "SubPathway" in labels(pathway) or not any(
            node.tag in {bp + "BiochemicalReaction", bp + "Transport"} for node in expanded
        ):
            raise ValueError(
                "PathBank requested source must contain the primary pathway definition"
            )
        attached = {subject(node) for node in primary if node.tag == bp + "Pathway"}

        def local_object(node: ElementTree.Element) -> str:
            uri = subject(node)
            document, fragment = urldefrag(uri)
            if (
                set(node.attrib) not in ({rdf + "ID"}, {rdf + "about"})
                or document != urldefrag(base)[0]
                or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._~/-]*", fragment)
                or any(part in {".", "..", ""} for part in fragment.split("/"))
            ):
                raise ValueError("PathBank interface bridge requires exact local RDF objects")
            return uri

        def literal(node: ElementTree.Element, tag: str, count: int) -> list[str]:
            values = node.findall(bp + tag)
            if len(values) != count or any(
                len(value)
                or not (value.text or "").strip()
                or value.attrib
                not in ({}, {rdf + "datatype": "http://www.w3.org/2001/XMLSchema#string"})
                for value in values
            ):
                raise ValueError("PathBank interface bridge has unsupported literal fields")
            return [value.text.strip() for value in values]

        def pointer(link: ElementTree.Element) -> ElementTree.Element:
            if (
                set(link.attrib) != {rdf + "resource"}
                or len(link)
                or (link.text or "").strip()
                or not link.get(rdf + "resource", "")
            ):
                raise ValueError("PathBank interface bridge requires exact resource pointers")
            return resolve(link)

        def bridge_child(node: ElementTree.Element) -> ElementTree.Element:
            # This closed issuing format identifies an opaque adjacent Pathway.
            # Its marker names do not establish an inhibition edge or mechanism.
            local_object(node)
            if node.tag != bp + "Interaction" or any(
                item.tag not in {bp + "displayName", bp + "name", bp + "participant"}
                for item in node
            ):
                raise ValueError("PathBank interface bridge requires a native Interaction")
            literal(node, "displayName", 1)
            names = literal(node, "name", 2)
            if len(set(names)) != 2 or names.count("InhibitorySubPathwayControl") != 1:
                raise ValueError("PathBank interface bridge has an unsupported source marker")
            direct = [
                link for link in pathway.findall(bp + "pathwayComponent") if resolve(link) is node
            ]
            ordered = []
            for link in pathway.findall(bp + "pathwayOrder"):
                step = resolve(link)
                links = [
                    item
                    for item in step
                    if item.tag
                    in {
                        bp + "stepProcess",
                        bp + "stepConversion",
                    }
                    and resolve(item) is node
                ]
                if not links:
                    continue
                pointer(link)
                local_object(step)
                if (
                    step.tag != bp + "PathwayStep"
                    or len(step) != 1
                    or (step[0].tag != bp + "stepProcess" or pointer(step[0]) is not node)
                ):
                    raise ValueError("PathBank interface bridge requires an exact PathwayStep")
                ordered.append(step)
            if not (direct or ordered) or len(direct) > 1 or len(ordered) > 1:
                raise ValueError("PathBank interface bridge must be owned by the primary pathway")
            for link in direct:
                pointer(link)
            links = node.findall(bp + "participant")
            if len(links) != 2:
                raise ValueError("PathBank interface bridge requires exactly two participants")
            targets = [pointer(link) for link in links]
            children = [item for item in targets if item.tag == bp + "Pathway"]
            compounds = [item for item in targets if item.tag == bp + "SmallMolecule"]
            if len(children) != 1 or len(compounds) != 1 or children[0] is pathway:
                raise ValueError("PathBank interface bridge requires one compound and one child")
            compound = compounds[0]
            local_object(compound)
            if any(
                item.tag not in {bp + "displayName", bp + "name", bp + "entityReference"}
                for item in compound
            ):
                raise ValueError("PathBank interface compound has unsupported fields")
            literal(compound, "displayName", 1)
            if literal(compound, "name", 1) != ["SubPathwayInhibitor"]:
                raise ValueError("PathBank interface compound has an unsupported source marker")
            references = compound.findall(bp + "entityReference")
            if len(references) != 1 or pointer(references[0]).tag != bp + "SmallMoleculeReference":
                raise ValueError("PathBank interface compound requires its native reference")
            local_object(pointer(references[0]))
            child = children[0]
            if (
                set(child.attrib) != {rdf + "about"}
                or any(
                    item.tag not in {bp + "displayName", bp + "name", bp + "xref"} for item in child
                )
                or literal(child, "name", 1) != ["InhibitorySubPathway"]
            ):
                raise ValueError("PathBank interface bridge requires an empty native child stub")
            literal(child, "displayName", 1)
            xrefs = [pointer(link) for link in child.findall(bp + "xref")]
            if not xrefs or len({subject(item) for item in xrefs}) != len(xrefs):
                raise ValueError("PathBank interface child requires unique native xrefs")
            for xref in xrefs:
                if xref.tag != bp + "UnificationXref":
                    raise ValueError("PathBank interface child requires native unification xrefs")
                literal(xref, "db", 1)
                literal(xref, "id", 1)
            return child

        bridged: set[str] = set()
        seen_bridges: set[str] = set()
        for node in primary:
            if "InhibitorySubPathwayControl" not in labels(node):
                continue
            uri = subject(node)
            if uri in seen_bridges:
                continue  # The direct and ordered paths may name the same object.
            seen_bridges.add(uri)
            child_uri = subject(bridge_child(node))
            if child_uri in bridged:
                raise ValueError("PathBank interface child has duplicate primary-owned bridges")
            bridged.add(child_uri)
        for other in pathways:
            if other is pathway:
                continue
            members = processes(other)
            direct_stub = (
                subject(other) in attached
                and "SubPathway" in labels(other)
                and members
                and all(node.tag == bp + "Interaction" for node in members)
            )
            if not direct_stub and subject(other) not in bridged:
                raise ValueError(
                    "PathBank additional pathways must be attached native interface stubs"
                )
            display_names = other.findall(bp + "displayName")
            if (
                len(display_names) != 1
                or len(display_names[0])
                or not (display_names[0].text or "").strip()
            ):
                raise ValueError("PathBank attached pathway requires one direct displayName")
            child_name = display_names[0].text.strip()
            if child_name.casefold() in {"subpathway", "inhibitorysubpathway"}:
                raise ValueError("PathBank attached pathway requires a biological displayName")
            # The issuing source names this exact attached pathway. Its generic
            # SubPathway marker is not a synonym, and its interface is not an
            # independently retrieved or expanded biochemical definition.
            child_terms.append(("PathBank:" + native_accession(other), child_name, []))
    names = labels(pathway)
    if not names:
        raise ValueError("PathBank pathway lacks a native label")
    identifier = "PathBank:" + accession
    yield identifier, names[0], names[1:]
    yield from child_terms

    graph_types = {
        bp + kind
        for kind in (
            "BiochemicalReaction",
            "Transport",
            "Complex",
            "PhysicalEntity",
            "SmallMolecule",
            "Protein",
            "Dna",
            "Rna",
            "DnaRegion",
            "RnaRegion",
        )
    }
    for node in root:
        if node.tag not in graph_types:
            continue
        uri = subject(node)
        document, native = urldefrag(uri)
        if (
            not native
            or document != urldefrag(base)[0]
            or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._~/-]*", native)
            or any(part in {".", "..", ""} for part in native.split("/"))
        ):
            raise ValueError(f"PathBank graph object lacks an unambiguous local identity: {uri}")
        names = labels(node) or [native]
        yield identifier + "/" + native, names[0], names[1:]


PATHBANK_CONTEXT_KIND = "pathbank-context-biopax"
_BP = "{http://www.biopax.org/release/biopax-level3.owl#}"
_RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
_XSD_STRING = "http://www.w3.org/2001/XMLSchema#string"


def _context_tree(raw: bytes) -> ElementTree.Element:
    try:
        text = raw.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("PathBank context requires complete UTF-8 XML") from exc
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)\b", text, re.I):
        raise ValueError("PathBank context forbids DTD/entity declarations")
    declaration = re.match(r'\s*<\?xml\b[^?]*encoding\s*=\s*[\'"]([^\'"]+)', text)
    if declaration and declaration[1].lower() not in {"utf-8", "utf8"}:
        raise ValueError("PathBank context requires UTF-8 encoding")
    try:
        root = ElementTree.fromstring(raw)
    except ElementTree.ParseError as exc:
        raise ValueError("PathBank context requires a complete XML document") from exc
    if root.tag != _RDF + "RDF" or set(root.attrib) != {
        "{http://www.w3.org/XML/1998/namespace}base"
    }:
        raise ValueError("PathBank context requires a single native RDF document base")
    return root


def context_terms(raw: bytes, url: str) -> list[tuple[str, str, list[str]]]:
    """Validate the whole native issuer before adding its closed context types."""
    accession = _pathbank_request(url)
    if accession is None:
        raise ValueError("PathBank context requires the official per-pathway request")
    root = _context_tree(raw)
    legacy = list(pathbank_terms(root, url=url))
    base = root.attrib["{http://www.w3.org/XML/1998/namespace}base"]
    document = urldefrag(base)[0]
    index = {}
    for node in root:
        if set(node.attrib) not in ({_RDF + "ID"}, {_RDF + "about"}):
            raise ValueError("PathBank context requires unambiguous native subject attributes")
        native = node.get(_RDF + "ID")
        uri = urljoin(base, "#" + native if native is not None else node.attrib[_RDF + "about"])
        if uri in index:
            raise ValueError("PathBank context has duplicate subjects")
        index[uri] = node

    def local(node: ElementTree.Element) -> str:
        native = node.get(_RDF + "ID")
        uri = urljoin(base, "#" + native if native is not None else node.attrib[_RDF + "about"])
        owner, fragment = urldefrag(uri)
        if (
            owner != document
            or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._~/-]*", fragment)
            or any(part in {".", "..", ""} for part in fragment.split("/"))
        ):
            raise ValueError("PathBank context object requires an unambiguous local identity")
        return "PathBank:" + accession + "/" + fragment

    def fields(node: ElementTree.Element, allowed: set[str]) -> None:
        if any(child.tag not in {_BP + field for field in allowed} for child in node):
            raise ValueError("PathBank context object has unsupported native fields")

    def literals(node: ElementTree.Element, field: str, count: int) -> list[str]:
        values = node.findall(_BP + field)
        if len(values) != count or any(
            len(v)
            or set(v.attrib) != {_RDF + "datatype"}
            or v.attrib[_RDF + "datatype"] != _XSD_STRING
            or not (v.text or "").strip()
            for v in values
        ):
            raise ValueError("PathBank context requires exact nonempty native literals")
        return [(v.text or "").strip() for v in values]

    def pointer(link: ElementTree.Element) -> ElementTree.Element:
        if set(link.attrib) != {_RDF + "resource"} or len(link) or (link.text or "").strip():
            raise ValueError("PathBank context requires an exact native pointer")
        uri = urljoin(base, link.attrib[_RDF + "resource"])
        if uri not in index:
            raise ValueError("PathBank context has a dangling native pointer")
        return index[uri]

    def one(node: ElementTree.Element, field: str, tag: str) -> ElementTree.Element:
        links = node.findall(_BP + field)
        if len(links) != 1:
            raise ValueError("PathBank context requires exactly one native pointer")
        target = pointer(links[0])
        if target.tag != _BP + tag:
            raise ValueError("PathBank context pointer has the wrong native type")
        return target

    def xrefs(node: ElementTree.Element, required: set[str]) -> dict[str, str]:
        assertions = {}
        for link in node.findall(_BP + "xref"):
            xref = pointer(link)
            if xref.tag != _BP + "UnificationXref":
                raise ValueError("PathBank context requires native unification xrefs")
            local(xref)
            fields(xref, {"id", "db"})
            db = literals(xref, "db", 1)[0]
            ident = literals(xref, "id", 1)[0]
            if db in assertions:
                raise ValueError("PathBank context has duplicate native xref databases")
            assertions[db] = ident
        if set(assertions) != required:
            raise ValueError("PathBank context lacks its complete native xref set")
        return assertions

    vocabularies = root.findall(_BP + "CellularLocationVocabulary")
    if not vocabularies:
        raise ValueError("PathBank context requires its native location vocabulary")
    extra = []
    for node in vocabularies:
        ident = local(node)
        fields(node, {"term", "xref"})
        label = literals(node, "term", 1)[0]
        xref = one(node, "xref", "UnificationXref")
        local(xref)
        fields(xref, {"id", "db"})
        if literals(xref, "db", 1) != ["GENE ONTOLOGY"] or not re.fullmatch(
            r"GO:[0-9]{7}", literals(xref, "id", 1)[0]
        ):
            raise ValueError("PathBank context location requires its native GO assertion")
        extra.append((ident, label, []))
    physical = {
        _BP + kind
        for kind in (
            "SmallMolecule",
            "Protein",
            "Complex",
            "PhysicalEntity",
            "Dna",
            "Rna",
            "DnaRegion",
            "RnaRegion",
        )
    }
    used_locations = set()
    for node in root:
        links = node.findall(_BP + "cellularLocation")
        if not links:
            continue
        if node.tag not in physical or len(links) != 1:
            raise ValueError("PathBank context requires one location per native physical state")
        target = pointer(links[0])
        if target not in vocabularies:
            raise ValueError("PathBank context physical state lacks its location vocabulary")
        local(node)
        used_locations.add(local(target))
    if used_locations != {local(node) for node in vocabularies}:
        raise ValueError("PathBank context contains an unreferenced location vocabulary")

    pathways = root.findall(_BP + "Pathway")
    primary_uri = "http://identifiers.org/smpdb/" + accession
    primary = index.get(primary_uri)
    if len(pathways) != 2 or primary not in pathways:
        raise ValueError("PathBank context requires the primary and one attached native pathway")
    child = next(node for node in pathways if node is not primary)
    fields(child, {"displayName", "name", "xref", "pathwayOrder", "pathwayComponent"})
    literals(child, "displayName", 1)
    if literals(child, "name", 1) != ["SubPathway"]:
        raise ValueError("PathBank context requires a direct native SubPathway")
    child_xrefs = xrefs(child, {"SMPDB", "PathWhiz"})
    if child.get(_RDF + "about") != "http://identifiers.org/smpdb/" + child_xrefs[
        "SMPDB"
    ] or not re.fullmatch(r"PW[0-9]+", child_xrefs["PathWhiz"]):
        raise ValueError("PathBank context child requires its accession and PathWhiz identity")
    # The legacy parser proves accession/xref consistency and primary attachment.
    # The context profile additionally requires the exact direct-and-ordered chain.
    direct = [pointer(link) for link in primary.findall(_BP + "pathwayComponent")]
    if direct.count(child) != 1:
        raise ValueError("PathBank context requires one primary child membership")
    primary_steps = [pointer(link) for link in primary.findall(_BP + "pathwayOrder")]
    child_steps = []
    for step in primary_steps:
        if any(pointer(link) is child for link in step.findall(_BP + "stepProcess")):
            child_steps.append(step)
    if len(child_steps) != 1 or child_steps[0].tag != _BP + "PathwayStep":
        raise ValueError("PathBank context requires one primary child step")
    fields(child_steps[0], {"stepProcess"})
    local(child_steps[0])
    if one(child_steps[0], "stepProcess", "Pathway") is not child:
        raise ValueError("PathBank context child step disagrees")
    interaction = one(child, "pathwayComponent", "Interaction")
    step = one(child, "pathwayOrder", "PathwayStep")
    fields(step, {"stepProcess"})
    local(step)
    if one(step, "stepProcess", "Interaction") is not interaction:
        raise ValueError("PathBank context direct and ordered interface disagree")
    if root.findall(_BP + "Interaction") != [interaction]:
        raise ValueError("PathBank context contains unsupported or multiply owned interfaces")
    # No other direct owner or ordering step may claim this generic interface.
    for node in root:
        for link in node:
            if link.tag in {_BP + "pathwayComponent", _BP + "stepProcess", _BP + "stepConversion"}:
                if pointer(link) is interaction and node not in (child, step):
                    raise ValueError("PathBank context interface has conflicting ownership")
    fields(interaction, {"displayName", "name", "participant"})
    label = literals(interaction, "displayName", 1)[0]
    names = literals(interaction, "name", 2)
    if (
        len(set(names)) != 2
        or "SubPathwayReaction" not in names
        or any("Inhibitory" in name for name in [label, *names])
    ):
        raise ValueError("PathBank context requires a generic native interface marker")
    compound = one(interaction, "participant", "SmallMolecule")
    fields(compound, {"displayName", "name", "cellularLocation", "entityReference"})
    local(compound)
    literals(compound, "displayName", 1)
    if literals(compound, "name", 1) != ["SubPathwayOutput"]:
        raise ValueError("PathBank context interface requires its output-marked native state")
    location = one(compound, "cellularLocation", "CellularLocationVocabulary")
    reference = one(compound, "entityReference", "SmallMoleculeReference")
    local(location)
    local(reference)
    fields(reference, {"displayName", "chemicalFormula", "molecularWeight", "structure", "xref"})
    literals(reference, "displayName", 1)
    literals(reference, "chemicalFormula", 1)
    masses = reference.findall(_BP + "molecularWeight")
    if (
        len(masses) != 1
        or len(masses[0])
        or masses[0].attrib != {_RDF + "datatype": "http://www.w3.org/2001/XMLSchema#float"}
    ):
        raise ValueError("PathBank context reference requires one native molecular weight")
    try:
        mass = float(masses[0].text or "")
    except ValueError as exc:
        raise ValueError(
            "PathBank context molecular weight must be a finite positive literal"
        ) from exc
    if not math.isfinite(mass) or mass <= 0:
        raise ValueError("PathBank context molecular weight must be a finite positive literal")
    xrefs(
        reference,
        {"PubChem-compound", "KEGG Compound", "ChemSpider", "ChEBI", "CAS", "BioCyc", "HMDB"},
    )
    structure = one(reference, "structure", "ChemicalStructure")
    local(structure)
    fields(structure, {"structureFormat", "structureData"})
    if literals(structure, "structureFormat", 1) != ["SMILES"]:
        raise ValueError("PathBank context reference requires its native SMILES structure")
    literals(structure, "structureData", 1)
    extra.append((local(interaction), label, names))
    result = legacy + extra
    if len({row[0] for row in result}) != len(result):
        raise ValueError("PathBank context projection contains duplicate identities")
    return result


def validate_context_metadata(metadata: dict[str, Any]) -> list[tuple[str, str, list[str]]]:
    required = {"kind", "url", "version", "license", "sha256", "native_pathbank_context"}
    if (
        set(metadata) not in (required, required | {"sha256_scope"})
        or metadata.get("kind") != PATHBANK_CONTEXT_KIND
    ):
        raise ValueError("PathBank context requires closed typed owner metadata")
    if any(
        not isinstance(metadata[k], str) or not metadata[k].strip()
        for k in metadata.keys() - {"native_pathbank_context"}
    ):
        raise ValueError("PathBank context requires nonempty provenance")
    native = metadata["native_pathbank_context"]
    if not isinstance(native, dict) or set(native) != {"xml", "bytes"}:
        raise ValueError("PathBank context requires its complete original XML and byte length")
    if not isinstance(native["xml"], str) or type(native["bytes"]) is not int:
        raise ValueError("PathBank context original has invalid types")
    raw = native["xml"].encode("utf-8")
    if len(raw) != native["bytes"] or hashlib.sha256(raw).hexdigest() != metadata["sha256"]:
        raise ValueError("PathBank context original disagrees with owner hash/length")
    return context_terms(raw, metadata["url"])


def context_metadata(entry: dict[str, Any], cache: Path) -> dict[str, Any]:
    required = {"key", "kind", "path", "url", "version", "license", "sha256"}
    if set(entry) not in (required, required | {"sha256_scope"}):
        raise ValueError("PathBank context requires closed source manifest fields")
    relative = Path(entry["path"])
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("PathBank context requires a relative original path")
    path = cache / relative
    if not path.is_file():
        raise ValueError("PathBank context requires a regular complete original")
    raw = path.read_bytes()
    try:
        xml = raw.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("PathBank context requires UTF-8 original bytes") from exc
    # Keep owner serialization stable across Python hash seeds and producer runs.
    fields = ("kind", "url", "version", "license", "sha256")
    metadata = {key: entry[key] for key in fields}
    if "sha256_scope" in entry:
        metadata["sha256_scope"] = entry["sha256_scope"]
    metadata["native_pathbank_context"] = {"xml": xml, "bytes": len(raw)}
    validate_context_metadata(metadata)
    return metadata


def context_term(identifier: str, parsed: dict[str, tuple], source: str) -> dict[str, Any]:
    if identifier not in parsed:
        raise ValueError("PathBank context term is absent from the whole native document")
    _, label, synonyms = parsed[identifier]
    term = {"label": label, "synonyms": sorted(set(synonyms) - {label}), "source": source}
    if "/" in identifier:
        term["label_kind"] = "source_context"
    return term


def _request_claim(url: str) -> str | None:
    parsed = urlsplit(url)
    if unquote(parsed.hostname or "").lower().rstrip(".") not in {
        "pathbank.org",
        "www.pathbank.org",
    }:
        return None
    match = re.search(r"/view/(SMP[0-9]+)(?:/|$)", unquote(parsed.path), re.I)
    return match[1].upper() if match else None


def validate_context_assertions(sources: dict[Any, dict]) -> dict[str, dict[str, tuple]]:
    """Register all complete owners before selected terms, including downgrades."""
    roots = {}
    projections = {}
    pathway_names = {}
    for key, owner in sources.items():
        if owner.get("kind") == PATHBANK_CONTEXT_KIND:
            parsed = validate_context_metadata(owner)
            root = _pathbank_request(owner["url"])
            signature = owner["native_pathbank_context"]
            if root in roots and roots[root] != signature:
                raise ValueError("PathBank context has conflicting complete issuer assertions")
            roots[root] = signature
            projections[key] = {row[0]: row for row in parsed}
            for identifier, label, _ in parsed:
                if "/" not in identifier:
                    if identifier in pathway_names and pathway_names[identifier] != label:
                        raise ValueError("conflicting PathBank native pathway names")
                    pathway_names[identifier] = label
        elif "native_pathbank_context" in owner:
            raise ValueError("PathBank context native metadata requires its typed source kind")
    for owner in sources.values():
        claim = _request_claim(owner.get("url", ""))
        archive = owner.get("archive")
        archive_claim = archive.get("root") if isinstance(archive, dict) else None
        if ({claim, archive_claim} & roots.keys()) and owner.get("kind") != PATHBANK_CONTEXT_KIND:
            raise ValueError("PathBank context rejects an untyped competing issuer claim")
    return projections


def pathbank_body_roots(path: Path) -> set[str]:
    """Read native subjects and accession links independently of the request URL."""
    root = ElementTree.parse(path).getroot()
    base = root.get("{http://www.w3.org/XML/1998/namespace}base", "")
    index = {}
    for node in root:
        native = node.get(_RDF + "ID")
        about = node.get(_RDF + "about")
        if native is not None or about is not None:
            index[urljoin(base, "#" + native if native is not None else about)] = node
    roots = set()
    for node in root.findall(_BP + "Pathway"):
        about = node.get(_RDF + "about", "")
        match = re.fullmatch(r"https?://identifiers.org/smpdb/(SMP[0-9]+)", about)
        if match:
            roots.add(match[1])
        for link in node.findall(_BP + "xref"):
            xref = index.get(urljoin(base, link.get(_RDF + "resource", "")))
            if xref is not None and xref.tag == _BP + "UnificationXref":
                accession = xref.findtext(_BP + "id", "")
                if xref.findtext(_BP + "db", "") == "SMPDB" and re.fullmatch(
                    r"SMP[0-9]+", accession
                ):
                    roots.add(accession)
    return roots
