#!/usr/bin/env python3
"""Extract identifier authority metadata from explicitly supplied primary sources.

The JSON manifest is a list of objects with key, kind, path, url, version,
license and sha256. Paths are relative to --cache-dir; supported kinds are enzyme,
gocam-tar, mibig-tar, uniprot, gpml, biopax, pathbank-biopax, metacyc-html,
metacyc-protein-xml, ncbi-entrezgene-xml,
ncbi-protein-xml, rhea-components-rdf-gz, kegg-module-flatfile,
kegg-reaction-flatfile, kegg-compound-flatfile and metanetx-chemical-html. Source files are
never generated from curated labels. The corpus only selects which identifiers
to retain, keeping the checked-in authority small and provenance auditable.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import tarfile
from collections.abc import Iterator
from html import unescape
from html.entities import name2codepoint
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, unquote, urldefrag, urljoin, urlsplit
from xml.etree import ElementTree
from xml.parsers import expat

import yaml

SOURCE_NAMESPACES = frozenset(
    {
        "EC", "Entrez", "MIBiG", "MetaCyc", "NCBIProtein", "PathBank", "Reactome", "SGD",
        "UniProtKB", "WikiPathways", "gomodel", "RHEA-COMP", "KEGG", "metanetx.chemical",
    }
)


def corpus_ids(root: Path) -> set[str]:
    """Use the same recursive YAML scope as the curated record loader."""
    paths = sorted(path for path in root.rglob("*.yaml") if path.is_file())
    if not paths:
        raise ValueError(f"no YAML records under {root}")
    identifiers: set[str] = set()
    for path in paths:
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        for node in [
            record,
            *(
                node
                for field in ("taxa", "participants", "reactions", "gene_clusters")
                for node in record.get(field, [])
            ),
        ]:
            identifiers.add(node["id"])
    return identifiers


def annotations(value: dict[str, Any], key: str) -> list[str]:
    return [
        item["value"]
        for item in value.get("annotations", [])
        if item.get("key") == key and isinstance(item.get("value"), str)
    ]


def gocam_terms(model: dict[str, Any]) -> Iterator[tuple[str, str, list[str]]]:
    labels = annotations(model, "title")
    if labels:
        yield model["id"], labels[0], labels[1:]
    for individual in model.get("individuals", []):
        labels = annotations(individual, "rdfs:label")
        type_labels = [
            item["label"]
            for item in individual.get("type", [])
            if isinstance(item.get("label"), str)
        ]
        if labels or type_labels:
            names = labels + type_labels
            yield individual["id"], names[0], names[1:]
        elif individual.get("id"):
            # A native graph instance can lack a canonical biological label.
            # Its ID still exists; source_context below prevents this native
            # identifier from being used as a canonical name assertion.
            yield individual["id"], individual["id"], []
        # These are SGD-submitted primary GO-CAM class annotations, not a claim
        # that their contextual display names equal SGD's canonical locus name.
        for item in individual.get("type", []):
            if str(item.get("id", "")).startswith("SGD:") and item.get("label"):
                yield item["id"], item["label"], []


def enzyme_terms(text: str) -> Iterator[tuple[str, str, list[str]]]:
    for entry in text.split("//"):
        fields: dict[str, list[str]] = {}
        for line in entry.splitlines():
            if len(line) >= 5:
                fields.setdefault(line[:2], []).append(line[5:].strip())
        if fields.get("ID") and fields.get("DE"):
            label = " ".join(fields["DE"]).removesuffix(".")
            if label.startswith(("Deleted entry", "Transferred entry")):
                continue
            synonyms = " ".join(fields.get("AN", [])).split(". ")
            yield "EC:" + fields["ID"][0], label, [s.removesuffix(".") for s in synonyms if s]


def uniprot_terms(data: dict[str, Any]) -> Iterator[tuple[str, str, list[str]]]:
    for entry in data.get("results", [data]):
        description = entry.get("proteinDescription", {})
        names: list[str] = []
        for name in [
            description.get("recommendedName", {}),
            *description.get("submissionNames", []),
            *description.get("alternativeNames", []),
        ]:
            if name.get("fullName", {}).get("value"):
                names.append(name["fullName"]["value"])
            names.extend(item["value"] for item in name.get("shortNames", []))
        if names:
            yield "UniProtKB:" + entry["primaryAccession"], names[0], names[1:]


def mibig_terms(data: dict[str, Any]) -> Iterator[tuple[str, str, list[str]]]:
    cluster = data.get("cluster", data)
    accession = cluster.get("mibig_accession") or cluster.get("accession")
    compounds = cluster.get("compounds", [])
    names = [item.get("compound") or item.get("name") for item in compounds]
    names = [name for name in names if isinstance(name, str) and name]
    if accession and names:
        # Products are the native labels. The pathway's curator-written cluster
        # description remains contextual and is not recorded as a synonym.
        yield "MIBiG:" + accession, names[0], names[1:]


def gpml_terms(root: ElementTree.Element) -> Iterator[tuple[str, str, list[str]]]:
    accession = None
    for node in root:
        if node.tag.rsplit("}", 1)[-1] == "Xref" and node.get("Database") == "WikiPathways":
            accession = node.get("ID")
    if not accession:
        match = re.search(r"WP\d+", root.get("Version", ""))
        accession = match.group() if match else None
    if not accession:
        raise ValueError("GPML source has no native WikiPathways accession")
    identifier = "WikiPathways:" + accession
    label = root.get("Name")
    if not label:
        raise ValueError("GPML source has no pathway Name")
    yield identifier, label, []
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] == "Interaction" and node.get("GraphId"):
            # GPML interactions have no canonical biological name. The native
            # GraphId is their source label; record prose remains contextual.
            yield identifier + "/" + node.attrib["GraphId"], node.attrib["GraphId"], []
        elif node.tag.rsplit("}", 1)[-1] == "DataNode" and node.get("GraphId"):
            # Keep diagram entities whose precise external grounding remains
            # unresolved. Native existence is independent of a guessed ChEBI ID.
            label = node.get("TextLabel") or node.attrib["GraphId"]
            yield identifier + "/" + node.attrib["GraphId"], label, []


def biopax_terms(root: ElementTree.Element) -> Iterator[tuple[str, str, list[str]]]:
    bp = "{http://www.biopax.org/release/biopax-level3.owl#}"
    rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
    xrefs: dict[str, str] = {}
    for node in root:
        if node.tag not in {bp + "UnificationXref", bp + "RelationshipXref"}:
            continue
        database, value = node.findtext(bp + "db"), node.findtext(bp + "id")
        if database and database.lower() == "reactome" and value:
            key = node.get(rdf + "ID") or node.get(rdf + "about")
            if key:
                xrefs[key.removeprefix("#")] = "Reactome:" + value
    for node in root:
        labels = [node.findtext(bp + name) for name in ("displayName", "standardName", "name")]
        labels = [label for label in labels if label]
        if not labels:
            continue
        for xref in node.findall(bp + "xref"):
            key = xref.get(rdf + "resource", "").removeprefix("#")
            if key in xrefs:
                yield xrefs[key], labels[0], labels[1:]


def _pathbank_request(url: str) -> str | None:
    """Only a native per-pathway request can select a multi-Pathway export."""
    parsed = urlsplit(url)
    if not (parsed.path.startswith("/view/") or parsed.path.endswith("/download")):
        return None  # Legacy archive artifacts still require a single Pathway.
    request = re.fullmatch(r"/view/(SMP[0-9]+)/download", parsed.path)
    if (
        parsed.scheme != "https" or parsed.netloc != "pathbank.org"
        or parsed.fragment or any(char.isspace() for char in url) or not request
        or parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True)
        != [("type", "owl_markup")]
    ):
        raise ValueError("PathBank selection requires an exact official BioPAX download URL")
    return request[1]


def pathbank_terms(
    root: ElementTree.Element, *, url: str = "",
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
        for node in root.iter() if node is not root
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
            databases = {
                (item.text or "").strip().casefold() for item in xref.findall(bp + "db")
            }
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
    requested = _pathbank_request(url)
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
                    resolve(link) for tag in ("stepProcess", "stepConversion")
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
        for other in pathways:
            if other is pathway:
                continue
            members = processes(other)
            if (
                subject(other) not in attached or "SubPathway" not in labels(other)
                or not members or any(node.tag != bp + "Interaction" for node in members)
            ):
                raise ValueError(
                    "PathBank additional pathways must be attached native interface stubs"
                )
    names = labels(pathway)
    if not names:
        raise ValueError("PathBank pathway lacks a native label")
    identifier = "PathBank:" + accession
    yield identifier, names[0], names[1:]

    graph_types = {
        bp + kind for kind in (
            "BiochemicalReaction", "Transport", "Complex", "PhysicalEntity", "SmallMolecule",
            "Protein", "Dna", "Rna", "DnaRegion", "RnaRegion",
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


def _metacyc_metadata_fields(text: str) -> Iterator[str]:
    """Bound native object literals without interpreting JavaScript values."""
    for match in re.finditer(r"typeObjectPage\s*=\s*\{", text):
        depth = 1
        quote = None
        escaped = False
        for index in range(match.end(), len(text)):
            char = text[index]
            if quote is not None:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == quote:
                    quote = None
            elif char in {"'", '"'}:
                quote = char
            elif char in {"/", "`"}:
                # Native metadata uses strings and simple values. Do not guess
                # the extent of comments, regex literals or template strings.
                raise ValueError("MetaCyc native metadata uses an unsupported literal")
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    yield text[match.start():index + 1]
                    break
        else:
            raise ValueError("MetaCyc source has unfinished native metadata")


def metacyc_terms(text: str) -> Iterator[tuple[str, str, list[str]]]:
    """Read native ID and native title from a public Pathway Tools object page."""
    # A few native UTF-8-declared pages contain stray bytes in unrelated prose.
    # source_terms preserves those bytes as surrogates rather than guessing an
    # encoding. None may enter an issuing identity or title, even in markup that
    # would later be stripped. Check all such fields before emitting any term.
    fields = [
        *_metacyc_metadata_fields(text),
        *re.findall(r"<TITLE\b[^>]*>.*?(?:</TITLE\s*>|$)", text, re.DOTALL | re.IGNORECASE),
    ]
    for field in fields:
        try:
            field.encode("utf-8", errors="strict")
        except UnicodeEncodeError as error:
            raise ValueError("MetaCyc native identity/title contains undecodable bytes") from error
    identity = re.search(r"typeObjectPage\s*=\s*\{object:'([^']+)',orgid:'META'", text)
    title = re.search(r"<TITLE>MetaCyc (.*?)</TITLE>", text, re.DOTALL | re.IGNORECASE)
    if identity is None or title is None:
        raise ValueError("MetaCyc source has no native META identity and title")
    label = " ".join(unescape(re.sub(r"<[^>]+>", "", title[1])).split())
    if (
        not label
        or label == identity[1]
        or label.lower().startswith(("error", "unknown", "not found"))
    ):
        raise ValueError("MetaCyc source lacks a resolved native label")
    yield "MetaCyc:" + identity[1], label, []


class _MetaCycProteinTreeBuilder(ElementTree.TreeBuilder):
    def doctype(self, name: str, pubid: str | None, system: str | None) -> None:
        # Reject before any entity declarations are processed, including in
        # UTF-16 documents. Scanning raw ASCII bytes would miss that encoding.
        raise ValueError("MetaCyc protein XML must not contain a DOCTYPE")


def _metacyc_protein_name_character(number: int) -> bool:
    # Preserve the name lower bound and XML 1.0 ranges after HTML decoding too.
    return (
        0x20 <= number <= 0xD7FF
        or 0xE000 <= number <= 0xFFFD
        or 0x10000 <= number <= 0x10FFFF
    )


class _MetaCycProteinName(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.parts: list[str] = []
        self.tags: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"i", "b", "em", "strong", "sub", "sup"} or attrs:
            raise ValueError("MetaCyc protein name has unsupported markup")
        self.tags.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if not self.tags or self.tags.pop() != tag:
            raise ValueError("MetaCyc protein name has unbalanced markup")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if name not in name2codepoint:
            raise ValueError("MetaCyc protein name contains an unknown entity")
        self.parts.append(chr(name2codepoint[name]))

    def handle_charref(self, name: str) -> None:
        number = int(name[1:], 16) if name.lower().startswith("x") else int(name)
        if not _metacyc_protein_name_character(number):
            raise ValueError("MetaCyc protein name contains an invalid character reference")
        self.parts.append(chr(number))

    def handle_comment(self, data: str) -> None:
        raise ValueError("MetaCyc protein name contains a comment")

    def handle_decl(self, decl: str) -> None:
        raise ValueError("MetaCyc protein name contains a declaration")

    def unknown_decl(self, data: str) -> None:
        raise ValueError("MetaCyc protein name contains an unsupported declaration")

    def handle_pi(self, data: str) -> None:
        raise ValueError("MetaCyc protein name contains a processing instruction")


def _metacyc_protein_request(url: str, *, legacy: bool = False) -> tuple[str, str]:
    parsed = urlsplit(url)
    if (
        any(char.isspace() for char in url)
        or parsed.scheme not in {"http", "https"}
        or not parsed.hostname or parsed.username is not None or parsed.password is not None
        or parsed.port == 0
        or parsed.path != "/getxml" or parsed.fragment
    ):
        raise ValueError("MetaCyc protein source requires a native getxml URL")
    if legacy and "=" not in parsed.query:
        query = unquote(parsed.query)
    else:
        fields = parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True)
        ids = [value for key, value in fields if key == "id"]
        if (
            len(ids) != 1 or len(fields) != len(set(fields))
            or any(key != "id" and (key, value) != ("detail", "full") for key, value in fields)
        ):
            raise ValueError("MetaCyc protein URL requires one META frame request")
        query = ids[0]
    if not re.fullmatch(r"META:[A-Za-z0-9][A-Za-z0-9_.-]*", query):
        raise ValueError("MetaCyc protein URL requires one META frame request")
    return query, parsed.hostname


def metacyc_protein_terms(
    path: Path, *, url: str, version: str,
) -> list[tuple[str, str, list[str]]]:
    """Extract one full META Protein; nested names and references are not terms."""
    requested, host = _metacyc_protein_request(url)
    root = ElementTree.fromstring(
        path.read_bytes(), parser=ElementTree.XMLParser(target=_MetaCycProteinTreeBuilder()),
    )
    if root.tag != "ptools-xml" or [node.tag for node in root].count("metadata") != 1:
        raise ValueError("MetaCyc protein source lacks native XML metadata")
    if len(root) != 2 or len(root.findall("Protein")) != 1:
        raise ValueError("MetaCyc protein source requires exactly one direct Protein")
    metadata = root.find("metadata")
    protein = root.find("Protein")
    assert metadata is not None and protein is not None  # checked above

    def text(parent: ElementTree.Element, tag: str) -> str:
        nodes = parent.findall(tag)
        if len(nodes) != 1 or len(nodes[0]) or not (nodes[0].text or "").strip():
            raise ValueError(f"MetaCyc protein source requires one nonempty {tag}")
        return nodes[0].text.strip()

    pgdbs = metadata.findall("PGDB")
    if (
        text(metadata, "service_name") != "getxml"
        or text(metadata, "num_results") != "1"
        or text(metadata, "query") != requested
        or len(pgdbs) != 1 or pgdbs[0].get("orgid") != "META"
        or not re.fullmatch(r"[0-9]+(?:\.[0-9]+)*", version)
        or pgdbs[0].get("version") != version
        or text(pgdbs[0], "species") != "MetaCyc"
    ):
        raise ValueError("MetaCyc protein query/PGDB identity or native version mismatch")
    base = root.get("{http://www.w3.org/XML/1998/namespace}base", "")
    if _metacyc_protein_request(base, legacy=True) != (requested, host):
        raise ValueError("MetaCyc protein XML base and manifest request disagree")
    native_url = text(metadata, "url")
    service_url = urlsplit(native_url)
    if (
        any(char.isspace() for char in native_url)
        or service_url.scheme not in {"http", "https"} or service_url.hostname != host
        or service_url.username is not None or service_url.password is not None
        or service_url.port == 0
        or service_url.query or service_url.fragment or service_url.path not in {"", "/"}
    ):
        raise ValueError("MetaCyc protein metadata names a different source service")
    frame = requested.removeprefix("META:")
    if (
        protein.get("ID") != requested or protein.get("frameid") != frame
        or protein.get("orgid") != "META" or protein.get("detail") != "full"
        or "resource" in protein.attrib or protein.get("class", "false") != "false"
    ):
        raise ValueError("MetaCyc protein source has mismatched or unresolved top-level identity")
    native_name = text(protein, "common-name")
    if protein.find("common-name").get("datatype") != "string":
        raise ValueError("MetaCyc protein common-name must be a native string")
    name = _MetaCycProteinName()
    name.feed(native_name)
    name.close()
    label = " ".join("".join(name.parts).split())
    if (
        name.tags or not label or "<" in label or ">" in label
        or re.search(r"&(?:#|[A-Za-z][A-Za-z0-9]*;)", label)
        or any(not _metacyc_protein_name_character(ord(char)) for char in label)
        or label in {frame, requested, "MetaCyc:" + frame}
        or label.casefold().startswith(("error", "unknown", "not found"))
    ):
        raise ValueError("MetaCyc protein source lacks a resolved native common-name")
    return [("MetaCyc:" + frame, label, [])]


def rhea_component_terms(path: Path) -> Iterator[tuple[str, str, list[str]]]:
    """Read whole generic polypeptides, never their ChEBI reactive parts.

    Rhea RDF calls these GENERIC:<id>; UniProt catalytic-activity xrefs expose
    the same Compound_<id> objects as RHEA-COMP:<id>. Require the RDF identity,
    accession, numeric id and explicit GenericPolypeptide class to agree.
    """
    rh = "{http://rdf.rhea-db.org/}"
    rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
    rdfs = "{http://www.w3.org/2000/01/rdf-schema#}"
    seen: set[str] = set()
    with gzip.open(path, "rb") as stream:
        depth = 0
        for event, node in ElementTree.iterparse(stream, events=("start", "end")):
            if event == "start":
                depth += 1
                if depth == 1:
                    root = node
                continue
            if depth == 2:
                classes = {item.get(rdf + "resource")
                           for item in node.findall(rdfs + "subClassOf")}
                if "http://rdf.rhea-db.org/GenericPolypeptide" in classes:
                    uri = node.get(rdf + "about", "")
                    match = re.fullmatch(r"http://rdf\.rhea-db\.org/Compound_([0-9]+)", uri)
                    values = {key: [item.text for item in node.findall(rh + key)]
                              for key in ("id", "accession", "name")}
                    if (not match or values["id"] != [match[1]]
                            or values["accession"] != ["GENERIC:" + match[1]]
                            or len(values["name"]) != 1 or not values["name"][0]
                            or not values["name"][0].strip()):
                        raise ValueError(f"Rhea component has ambiguous identity or name: {uri}")
                    identifier = "RHEA-COMP:" + match[1]
                    if identifier in seen:
                        raise ValueError(f"duplicate Rhea component: {identifier}")
                    seen.add(identifier)
                    yield identifier, values["name"][0].strip(), []
                # Clear only complete top-level subjects, keeping child facts
                # intact until their enclosing subject has been interpreted.
                root.clear()
            depth -= 1


KEGG_SOURCE_TYPES = {
    "kegg-module-flatfile": ("M", "Pathway Module"),
    "kegg-reaction-flatfile": ("R", "Reaction"),
    "kegg-compound-flatfile": ("C", "Compound"),
}


class _MetaNetXPage(HTMLParser):
    """Read native identity surfaces without executing page scripts."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.jsonld: list[str] = []
        self.headings: list[str] = []
        self.rows: list[list[str]] = []
        self._script: list[str] | None = None
        self._heading: list[str] | None = None
        self._rows: list[list[str]] = []
        self._cells: list[tuple[list[str], list[str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "script" and dict(attrs).get("type") == "application/ld+json":
            self._script = []
        elif tag == "h1":
            if self._heading is not None:
                raise ValueError("MetaNetX source has nested identity headings")
            self._heading = []
        elif tag == "tr":
            self._rows.append([])
        elif tag == "td" and self._rows:
            self._cells.append((self._rows[-1], []))

    def handle_data(self, data: str) -> None:
        if self._script is not None:
            self._script.append(data)
            return
        if self._heading is not None:
            self._heading.append(data)
        if self._cells:
            self._cells[-1][1].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script is not None:
            self.jsonld.append("".join(self._script))
            self._script = None
        elif tag == "h1" and self._heading is not None:
            self.headings.append(" ".join("".join(self._heading).split()))
            self._heading = None
        elif tag == "td" and self._cells:
            row, parts = self._cells.pop()
            row.append(" ".join("".join(parts).split()))
        elif tag == "tr" and self._rows:
            self.rows.append(self._rows.pop())


def _unique_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"MetaNetX JSON-LD has duplicate key: {key}")
        result[key] = value
    return result


def metanetx_chemical_terms(text: str, url: str) -> list[tuple[str, str, list[str]]]:
    """Verify one production MNXM entry; xrefs and aliases are not authorities.

    The JSON-LD identity must agree with its URL and the visible native ID/name.
    A native chemical class may describe an entire generic carrier; admitting its
    name does not establish cross-database structure equivalence or a sequence.
    """
    request = re.fullmatch(r"https://www\.metanetx\.org/chem_info/(MNXM[0-9]+)", url)
    if not request:
        raise ValueError("MetaNetX chemical source requires an official production MNXM URL")
    page = _MetaNetXPage()
    page.feed(text)
    page.close()
    if (page._script is not None or page._heading is not None
            or page._rows or page._cells):
        raise ValueError("MetaNetX source has an unfinished identity surface")

    entities: list[dict[str, Any]] = []

    def collect(value: Any) -> None:
        if isinstance(value, dict):
            kind = value.get("@type")
            if kind == "MolecularEntity" or isinstance(kind, list) and "MolecularEntity" in kind:
                entities.append(value)
            for child in value.values():
                collect(child)
        elif isinstance(value, list):
            for child in value:
                collect(child)

    for body in page.jsonld:
        try:
            collect(json.loads(body, object_pairs_hook=_unique_json_keys))
        except json.JSONDecodeError as error:
            raise ValueError("MetaNetX source has malformed JSON-LD") from error
    if len(entities) != 1:
        raise ValueError("MetaNetX source requires exactly one MolecularEntity")
    entity = entities[0]
    identifier = "metanetx.chemical:" + request[1]
    if (entity.get("@context") != "https://schema.org"
            or entity.get("@type") != "MolecularEntity"
            or entity.get("identifier") != identifier
            or entity.get("@id") != url or entity.get("url") != url):
        raise ValueError("MetaNetX JSON-LD identity, class and production URL must agree")
    label = entity.get("name")
    if (not isinstance(label, str) or not label.strip()
            or label.strip() in {request[1], identifier}
            or label.strip().casefold().startswith(("error", "unknown", "not found"))):
        raise ValueError("MetaNetX source lacks a resolved native name")
    label = " ".join(label.split())
    visible_ids = [row[1:] for row in page.rows if row and row[0] == "MNX_ID"]
    # The production row also includes an image cell; its text is not identity.
    if (len(visible_ids) != 1 or not visible_ids[0] or visible_ids[0][0] != request[1]
            or page.headings != [label]):
        raise ValueError("MetaNetX visible native ID/name and JSON-LD must agree")
    return [(identifier, label, [])]


def kegg_terms(text: str, kind: str, url: str) -> list[tuple[str, str, list[str]]]:
    """Read native ENTRY/NAME assertions, bound to an exact official REST request.

    The whole homogeneous batch is validated before returning any terms. Module
    cross-reference lists and KGML display names are not issuing authorities.
    """
    if kind not in KEGG_SOURCE_TYPES:
        raise ValueError(f"unsupported KEGG source kind: {kind}")
    prefix, entry_type = KEGG_SOURCE_TYPES[kind]
    identifier_pattern = rf"{prefix}[0-9]{{5}}"
    request = re.fullmatch(
        rf"https://rest\.kegg\.jp/get/({identifier_pattern}(?:\+{identifier_pattern}){{0,9}})",
        url,
    )
    if not request:
        raise ValueError("KEGG source requires an official same-class flatfile get URL")
    requested = request.group(1).split("+")
    if len(set(requested)) != len(requested):
        raise ValueError("KEGG request has duplicate identifiers")

    terms: list[tuple[str, str, list[str]]] = []
    seen: set[str] = set()
    fields: dict[str, list[str]] = {}
    current = ""
    for line in text.splitlines():
        if not line.strip():
            continue
        if line.rstrip() == "///":
            entry = " ".join(" ".join(fields.get("ENTRY", [])).split())
            match = re.fullmatch(rf"({identifier_pattern})\s+{entry_type}", entry)
            if not match:
                raise ValueError("KEGG ENTRY identity and class do not match source kind")
            identifier = match.group(1)
            if identifier in seen:
                raise ValueError(f"KEGG source has duplicate ENTRY: {identifier}")
            name = " ".join(" ".join(fields.get("NAME", [])).split())
            names = [part.strip() for part in name.removesuffix(";").split(";")]
            if not all(names) or any(
                value in {identifier, f"KEGG:{identifier}"} for value in names
            ):
                raise ValueError(f"KEGG ENTRY {identifier} lacks a native biological NAME")
            terms.append((f"KEGG:{identifier}", names[0], sorted(set(names[1:]) - {names[0]})))
            seen.add(identifier)
            fields = {}
            current = ""
            continue
        column, value = line[:12], line[12:].strip()
        tag = column.strip()
        if "\t" in line or not fields and tag != "ENTRY":
            raise ValueError("KEGG flatfile has an orphan field or malformed field columns")
        if not tag:
            if not current or not value:
                raise ValueError("KEGG flatfile has an orphan continuation")
            fields[current].append(value)
        elif not re.fullmatch(r"[A-Z][A-Z0-9_]*", tag):
            raise ValueError("KEGG flatfile has a malformed field")
        elif column.startswith(" "):
            # Indented AUTHORS/TITLE/JOURNAL belong to REFERENCE, not NAME.
            if current != "REFERENCE" or tag not in {"AUTHORS", "TITLE", "JOURNAL"}:
                raise ValueError("KEGG flatfile has an unsupported nested field")
        else:
            if tag in {"ENTRY", "NAME"} and tag in fields:
                raise ValueError(f"KEGG flatfile has duplicate {tag} fields")
            if not value:
                raise ValueError(f"KEGG flatfile has an empty {tag} field")
            fields.setdefault(tag, []).append(value)
            current = tag
    if fields:
        raise ValueError("KEGG flatfile has an unterminated ENTRY")
    if not terms or seen != set(requested):
        raise ValueError("KEGG ENTRY identities do not equal the requested identifiers")
    return terms


def _ncbi_gene_record(path: Path, url: str) -> tuple[tuple[str, str, list[str]], str]:
    """Read one directly requested, non-redirected Gene record and its native taxon.

    Status omission is accepted as omission, not an explicit live assertion.
    The official external DOCTYPE is allowed without loading its DTD. Internal
    subsets and entities are rejected by the XML parser in every encoding.
    """
    request = urlsplit(url)
    fields = parse_qsl(request.query, keep_blank_values=True, strict_parsing=True)
    query = dict(fields)
    if (
        request.scheme != "https" or request.netloc != "eutils.ncbi.nlm.nih.gov"
        or request.path != "/entrez/eutils/efetch.fcgi" or request.fragment
        or any(char.isspace() for char in url)
        or len(fields) != 3 or set(query) != {"db", "id", "rettype"}
        or query.get("db") != "gene" or query.get("rettype") != "xml"
        or not re.fullmatch(r"[1-9][0-9]*", query.get("id", ""))
    ):
        raise ValueError("NCBI Gene source requires one exact official gene EFetch XML request")

    def doctype(name: str, system: str | None, public: str | None, internal: int) -> None:
        if (
            name != "Entrezgene-Set" or internal
            or system != "https://www.ncbi.nlm.nih.gov/data_specs/dtd/NCBI_Entrezgene.dtd"
            or public != "-//NLM//DTD NCBI-Entrezgene, 21st January 2005//EN"
        ):
            raise ValueError("NCBI Gene source has an unsupported DOCTYPE")

    def entity(*args: Any) -> None:
        raise ValueError("NCBI Gene authority does not allow XML entities")

    raw = path.read_bytes()
    parser = expat.ParserCreate()
    parser.StartDoctypeDeclHandler = doctype
    parser.EntityDeclHandler = entity
    parser.ExternalEntityRefHandler = entity
    parser.SetParamEntityParsing(expat.XML_PARAM_ENTITY_PARSING_NEVER)
    parser.Parse(raw, True)
    root = ElementTree.fromstring(raw)

    def one(
        parent: ElementTree.Element, tag: str, *, optional: bool = False,
    ) -> ElementTree.Element:
        nodes = parent.findall(tag)
        if len(nodes) != 1 and not (optional and not nodes):
            raise ValueError(f"NCBI Gene source requires one direct {tag}")
        return nodes[0] if nodes else ElementTree.Element(tag)

    def text(parent: ElementTree.Element, tag: str, *, optional: bool = False) -> str:
        nodes = parent.findall(tag)
        if optional and not nodes:
            return ""
        node = one(parent, tag)
        value = (node.text or "").strip()
        if len(node) or not value:
            raise ValueError(f"NCBI Gene source requires a nonempty scalar {tag}")
        if any(not _metacyc_protein_name_character(ord(char)) for char in value):
            raise ValueError(f"NCBI Gene source has invalid characters in {tag}")
        return value

    if root.tag != "Entrezgene-Set" or len(root) != 1 or root[0].tag != "Entrezgene":
        raise ValueError("NCBI Gene source requires exactly one direct Entrezgene")
    gene = root[0]
    track = one(one(gene, "Entrezgene_track-info"), "Gene-track")
    gid = text(track, "Gene-track_geneid")
    if gid != query["id"]:
        raise ValueError("NCBI Gene native ID and requested ID disagree")
    status = one(track, "Gene-track_status", optional=True)
    if track.findall("Gene-track_status") and (
        len(status) or status.attrib != {"value": "live"}
        or (status.text or "").strip() not in {"", "0"}
    ):
        raise ValueError("NCBI Gene explicit status is not an unambiguous live record")
    if track.findall("Gene-track_current-id") or track.findall("Gene-track_discontinue-date"):
        raise ValueError("NCBI Gene redirected or discontinued records are not supported")
    gene_ref = one(one(gene, "Entrezgene_gene"), "Gene-ref")
    label = text(gene_ref, "Gene-ref_locus")
    if (
        any(char.isspace() for char in label) or any(char in label for char in "<>&")
        or label in {gid, "Entrez:" + gid}
        or label.casefold() in {"unknown", "error", "not-found", "not_found", "null"}
    ):
        raise ValueError("NCBI Gene source lacks a resolved native locus symbol")
    formal = one(gene_ref, "Gene-ref_formal-name", optional=True)
    if gene_ref.findall("Gene-ref_formal-name"):
        nomenclature = one(formal, "Gene-nomenclature")
        symbol = text(nomenclature, "Gene-nomenclature_symbol", optional=True)
        if symbol and symbol != label:
            raise ValueError("NCBI Gene locus and formal symbol disagree")
    synonyms = []
    syn = one(gene_ref, "Gene-ref_syn", optional=True)
    for node in syn:
        if node.tag != "Gene-ref_syn_E" or len(node) or not (node.text or "").strip():
            raise ValueError("NCBI Gene source has a malformed native synonym")
        value = node.text.strip()
        if (
            any(char in value for char in "<>&")
            or any(not _metacyc_protein_name_character(ord(char)) for char in value)
        ):
            raise ValueError("NCBI Gene source has an invalid native synonym")
        synonyms.append(value)
    locus_tag = text(gene_ref, "Gene-ref_locus-tag", optional=True)
    if locus_tag:
        if any(char.isspace() for char in locus_tag) or any(char in locus_tag for char in "<>&"):
            raise ValueError("NCBI Gene source has an invalid native locus tag")
        synonyms.append(locus_tag)

    org = one(one(one(one(gene, "Entrezgene_source"), "BioSource"), "BioSource_org"), "Org-ref")
    text(org, "Org-ref_taxname")
    tags = one(org, "Org-ref_db")
    taxon_tags = [
        node for node in tags if node.tag == "Dbtag" and text(node, "Dbtag_db") == "taxon"
    ]
    if len(taxon_tags) != 1:
        raise ValueError("NCBI Gene source requires one unambiguous native taxon")
    native_taxon = one(one(taxon_tags[0], "Dbtag_tag"), "Object-id")
    taxon = text(native_taxon, "Object-id_id")
    if len(native_taxon) != 1 or not re.fullmatch(r"[1-9][0-9]*", taxon):
        raise ValueError("NCBI Gene source requires a positive numeric taxon ID")
    return ("Entrez:" + gid, label, sorted(set(synonyms) - {label})), taxon


def source_terms(
    kind: str, path: Path, *, url: str | None = None, version: str | None = None,
) -> Iterator[tuple[str, str, list[str]]]:
    if kind in {"gocam-tar", "mibig-tar"}:
        parser = gocam_terms if kind == "gocam-tar" else mibig_terms
        with tarfile.open(path, "r:gz") as archive:
            for member in archive:
                if member.isfile() and member.name.endswith(".json"):
                    stream = archive.extractfile(member)
                    if stream is not None:
                        yield from parser(json.load(stream))
    elif kind == "enzyme":
        yield from enzyme_terms(path.read_text(encoding="utf-8"))
    elif kind == "uniprot":
        yield from uniprot_terms(json.loads(path.read_text(encoding="utf-8")))
    elif kind == "gpml":
        yield from gpml_terms(ElementTree.parse(path).getroot())
    elif kind == "biopax":
        yield from biopax_terms(ElementTree.parse(path).getroot())
    elif kind == "pathbank-biopax":
        yield from pathbank_terms(ElementTree.parse(path).getroot(), url=url or "")
    elif kind == "rhea-components-rdf-gz":
        yield from rhea_component_terms(path)
    elif kind == "metacyc-html":
        yield from metacyc_terms(path.read_bytes().decode("utf-8", errors="surrogateescape"))
    elif kind == "metacyc-protein-xml":
        yield from metacyc_protein_terms(path, url=url or "", version=version or "")
    elif kind == "ncbi-entrezgene-xml":
        term, _ = _ncbi_gene_record(path, url or "")
        yield term
    elif kind in KEGG_SOURCE_TYPES:
        yield from kegg_terms(path.read_text(encoding="utf-8"), kind, url or "")
    elif kind == "metanetx-chemical-html":
        yield from metanetx_chemical_terms(path.read_text(encoding="utf-8"), url or "")
    elif kind == "ncbi-protein-xml":
        for protein in ElementTree.parse(path).getroot().findall("GBSeq"):
            accession = protein.findtext("GBSeq_accession-version")
            label = protein.findtext("GBSeq_definition")
            if not accession or not label:
                raise ValueError("NCBI protein lacks an accession-version or definition")
            synonyms = [
                qualifier.findtext("GBQualifier_value")
                for qualifier in protein.findall(".//GBQualifier")
                if qualifier.findtext("GBQualifier_name") in {"gene", "product", "locus_tag"}
                and qualifier.findtext("GBQualifier_value")
            ]
            yield "NCBIProtein:" + accession, label, synonyms
    else:
        raise ValueError(f"unsupported source kind: {kind}")


def build_snapshot(manifest: Path, records: Path, cache_dir: Path) -> dict[str, Any]:
    wanted = corpus_ids(records)
    terms: dict[str, Any] = {}
    sources: dict[str, Any] = {}
    source_keys: set[str] = set()
    kegg_assertions: dict[str, tuple[str, tuple[str, ...]]] = {}
    metanetx_assertions: dict[str, str] = {}
    metacyc_names: dict[str, set[str]] = {}
    metacyc_xml_ids: set[str] = set()
    gene_assertions: dict[str, tuple[str, tuple[str, ...], str]] = {}
    entries = json.loads(manifest.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise ValueError("source manifest must be a nonempty list")
    for entry in entries:
        key = entry["key"]
        if key in source_keys:
            raise ValueError(f"duplicate source key: {key}")
        source_keys.add(key)
        artifact = Path(entry["path"])
        if artifact.is_absolute() or ".." in artifact.parts:
            raise ValueError(f"source {key} requires a relative cache path")
        path = cache_dir / artifact
        metadata = {name: entry[name] for name in ("url", "version", "license")}
        if "sha256_scope" in entry:
            metadata["sha256_scope"] = entry["sha256_scope"]
        if not all(isinstance(value, str) and value for value in metadata.values()):
            raise ValueError(f"source {key} requires nonempty provenance")
        metadata["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        if metadata["sha256"] != entry.get("sha256"):
            raise ValueError(f"source {key} bytes do not match manifest sha256")
        if entry["kind"] == "ncbi-entrezgene-xml":
            term, taxon = _ncbi_gene_record(path, entry["url"])
            identifier, label, synonyms = term
            assertion = (label, tuple(synonyms), taxon)
            if identifier in gene_assertions and gene_assertions[identifier] != assertion:
                raise ValueError(f"conflicting NCBI Gene native assertions for {identifier}")
            gene_assertions[identifier] = assertion
            parsed_terms = [term]
        else:
            parsed_terms = source_terms(
                entry["kind"], path, url=entry["url"], version=entry["version"],
            )
        for identifier, label, synonyms in parsed_terms:
            if entry["kind"] in {"metacyc-protein-xml", "metacyc-html"}:
                names = metacyc_names.setdefault(identifier, set())
                names.add(label)
                if entry["kind"] == "metacyc-protein-xml":
                    metacyc_xml_ids.add(identifier)
                if identifier in metacyc_xml_ids and len(names) != 1:
                    raise ValueError(f"conflicting MetaCyc protein native names for {identifier}")
            if (identifier.startswith("metanetx.chemical:")
                    and entry["kind"] != "metanetx-chemical-html"):
                raise ValueError("MetaNetX chemical identifiers require native chemical HTML")
            if entry["kind"] == "metanetx-chemical-html":
                if identifier in metanetx_assertions and metanetx_assertions[identifier] != label:
                    raise ValueError(f"conflicting MetaNetX native names for {identifier}")
                metanetx_assertions[identifier] = label
            if entry["kind"] in KEGG_SOURCE_TYPES:
                assertion = (label, tuple(sorted(set(synonyms))))
                if identifier in kegg_assertions and kegg_assertions[identifier] != assertion:
                    raise ValueError(f"conflicting KEGG native names for {identifier}")
                kegg_assertions[identifier] = assertion
            if identifier not in wanted:
                continue
            if identifier in terms:
                # Keep one source's assertions together. When source entries
                # repeat an ID, merge source-provided labels into synonyms.
                if terms[identifier]["source"] == key:
                    terms[identifier]["synonyms"] = sorted(
                        set(terms[identifier]["synonyms"] + [label] + synonyms)
                        - {terms[identifier]["label"]}
                    )
                continue
            terms[identifier] = {
                "label": label,
                "synonyms": sorted(set(synonyms) - {label}),
                "source": key,
            }
            if (
                (identifier.startswith("WikiPathways:") and "/" in identifier)
                or (entry["kind"] == "pathbank-biopax" and "/" in identifier)
                or identifier.startswith("MIBiG:")
                or (
                    entry["kind"] == "gocam-tar"
                    and identifier.split(":", 1)[0] in {"SGD", "gomodel"}
                )
            ):
                terms[identifier]["label_kind"] = "source_context"
            sources[key] = metadata
    if not terms:
        raise ValueError("no corpus identifiers matched the supplied sources")
    required = {
        identifier for identifier in wanted if identifier.split(":", 1)[0] in SOURCE_NAMESPACES
    }
    missing = sorted(required - terms.keys())
    if missing:
        raise ValueError("unresolved source identifiers: " + ", ".join(missing))
    return {
        "version": 1,
        "sources": dict(sorted(sources.items())),
        "terms": dict(sorted(terms.items())),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--cache-dir", required=True, type=Path)
    parser.add_argument("--records", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    snapshot = build_snapshot(args.manifest, args.records, args.cache_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"Retained {len(snapshot['terms'])} independently sourced identifiers "
        f"from {len(snapshot['sources'])} sources"
    )


if __name__ == "__main__":
    main()
