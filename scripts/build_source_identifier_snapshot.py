#!/usr/bin/env python3
"""Extract identifier authority metadata from explicitly supplied primary sources.

The JSON manifest is a list of objects with key, kind, path, url, version,
license and sha256. Paths are relative to --cache-dir; supported kinds are enzyme,
gocam-tar, mibig-tar, uniprot, gpml, biopax, pathbank-biopax, pathbank-biopax-zip,
pathbank-context-biopax, metacyc-html,
metacyc-protein-xml, metacyc-reaction-xml, metacyc-carrier-class-xml,
ecocyc-protein-state-xml (separate counterpart_source original), ecocyc-protein-xml, ecocyc-rna-xml,
ecocyc-complex-xml (typed originals and optional class_source companion), ncbi-entrezgene-xml,
ncbi-protein-xml, rhea-components-rdf-gz, rhea-polymer-rdf,
metacyc-electron-transfer-reaction-xml, metacyc-chemical-class-xml, metacyc-pathway-xml,
ecocyc-named-protein-complex-xml, kegg-module-flatfile,
kegg-reaction-flatfile, kegg-compound-flatfile, kegg-gene-flatfile,
kegg-pseudogene-flatfile, metanetx-chemical-html,
bigg-universal-metabolite-json, bigg-universal-reaction-json and
pubchem-compound-property-json. Source files are
never generated from curated labels. The corpus only selects which identifiers
to retain, keeping the checked-in authority small and provenance auditable.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import math
import re
import tarfile
import zipfile
from collections.abc import Iterator
from datetime import date, datetime
from html import unescape
from html.entities import name2codepoint
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, unquote, urlsplit
from xml.etree import ElementTree
from xml.parsers import expat

import yaml

from pathwaymech.biocyc_aceto import (
    ACETO_KINDS,
    COMPANION_FIELDS,
    NESTED_KIND,
    aceto_metadata,
    aceto_term,
    validate_aceto_assertions,
)
from pathwaymech.biocyc_carrier import (
    CARRIER_CLASS_KIND,
    class_metadata,
    class_native,
    class_term,
)
from pathwaymech.biocyc_carrier import (
    original_path as carrier_original_path,
)
from pathwaymech.biocyc_chemical_class import (
    CHEMICAL_CLASS_KIND,
    chemical_class_metadata,
    chemical_class_term,
)
from pathwaymech.biocyc_electron_transfer import (
    ELECTRON_TRANSFER_KIND,
    reaction_metadata,
    reaction_term,
)
from pathwaymech.biocyc_pathway import PATHWAY_KIND, pathway_metadata, pathway_term
from pathwaymech.biocyc_protein_carrier_reaction import (
    PROTEIN_CARRIER_REACTION_KIND,
    carrier_reaction_metadata,
    carrier_reaction_term,
    validate_carrier_reaction_assertions,
)
from pathwaymech.ecocyc_complex import ECOCYC_COMPLEX_KIND, complex_metadata, complex_term
from pathwaymech.ecocyc_named_complex import (
    NAMED_COMPLEX_KIND,
    named_complex_metadata,
    named_complex_term,
    validate_named_complex_graph,
)
from pathwaymech.ecocyc_state import ECOCYC_STATE_KIND, state_metadata, state_term
from pathwaymech.kegg_gene import (
    GENE_KIND,
    GENE_KINDS,
    gene_metadata,
    gene_term,
    is_gene_id,
    validate_gene_assertions,
)
from pathwaymech.kegg_gene import project as kegg_gene_project
from pathwaymech.kegg_gene import project_pseudogene as kegg_pseudogene_project
from pathwaymech.pathbank_context import (
    PATHBANK_CONTEXT_KIND,
    context_metadata,
    context_term,
    context_terms,
    pathbank_body_roots,
    pathbank_terms,
    validate_context_assertions,
)
from pathwaymech.pathbank_provenance import (
    PATHBANK_ARCHIVE_KIND,
    validate_pathbank_archive,
)
from pathwaymech.rhea_polymer import RHEA_POLYMER_KIND, polymer_metadata, polymer_term

SOURCE_NAMESPACES = frozenset(
    {
        "BiGG",
        "EC",
        "EcoCyc",
        "Entrez",
        "MIBiG",
        "MetaCyc",
        "NCBIProtein",
        "PathBank",
        "PubChem",
        "Reactome",
        "SGD",
        "UniProtKB",
        "WikiPathways",
        "gomodel",
        "RHEA-COMP",
        "KEGG",
        "metanetx.chemical",
    }
)

BIGG_SOURCE_TYPES = {
    "bigg-universal-metabolite-json": "metabolites",
    "bigg-universal-reaction-json": "reactions",
}

ECOCYC_SOURCE_TYPES = {
    "ecocyc-protein-xml": ("Protein", {"Protein-Complexes", "Protein-Small-Molecule-Complexes"}),
    "ecocyc-rna-xml": ("RNA", {"Regulatory-RNAs"}),
}
ECOCYC_HOST = "bf2i-artsymbiocyc.insa-lyon.fr"


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


def _pathbank_archive_terms(
    path: Path,
    *,
    url: str,
    sha256: str,
    archive: Any,
) -> list[tuple[str, str, list[str]]]:
    """Verify actual ZIP and member bytes before native membership selection."""
    validate_pathbank_archive(url, sha256, archive)
    raw = path.read_bytes()
    if len(raw) != archive["bytes"] or hashlib.sha256(raw).hexdigest() != sha256:
        raise ValueError("PathBank ZIP original bytes disagree with archive provenance")
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as source:
            members = [info for info in source.infolist() if info.filename == archive["member"]]
            if (
                len(members) != 1
                or members[0].is_dir()
                or members[0].file_size != archive["member_bytes"]
            ):
                raise ValueError("PathBank ZIP requires one exact member with bound byte count")
            member = source.read(members[0])
    except (zipfile.BadZipFile, RuntimeError, NotImplementedError) as error:
        raise ValueError("PathBank ZIP member could not be verified") from error
    if (
        len(member) != archive["member_bytes"]
        or hashlib.sha256(member).hexdigest() != archive["member_sha256"]
    ):
        raise ValueError("PathBank ZIP member bytes disagree with member provenance")
    root = ElementTree.fromstring(member)
    if root.tag != "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF" or any(
        not node.tag.startswith("{http://www.biopax.org/release/biopax-level3.owl#}")
        and node.tag != "{http://www.w3.org/2002/07/owl#}Ontology"
        for node in root
    ):
        raise ValueError("PathBank ZIP member requires native RDF/BioPAX object types")
    return list(pathbank_terms(root, url=url, archive_root=archive["root"]))


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
                    yield text[match.start() : index + 1]
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
    return 0x20 <= number <= 0xD7FF or 0xE000 <= number <= 0xFFFD or 0x10000 <= number <= 0x10FFFF


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
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.port == 0
        or parsed.path != "/getxml"
        or parsed.fragment
    ):
        raise ValueError("MetaCyc protein source requires a native getxml URL")
    if legacy and "=" not in parsed.query:
        query = unquote(parsed.query)
    else:
        fields = parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True)
        ids = [value for key, value in fields if key == "id"]
        if (
            len(ids) != 1
            or len(fields) != len(set(fields))
            or any(key != "id" and (key, value) != ("detail", "full") for key, value in fields)
        ):
            raise ValueError("MetaCyc protein URL requires one META frame request")
        query = ids[0]
    if not re.fullmatch(r"META:[A-Za-z0-9][A-Za-z0-9_.-]*", query):
        raise ValueError("MetaCyc protein URL requires one META frame request")
    return query, parsed.hostname


def _metacyc_protein_identity(
    path: Path,
    *,
    url: str,
    version: str,
) -> tuple[ElementTree.Element, str]:
    """Validate the request, native service/version and one full Protein instance."""
    requested, host = _metacyc_protein_request(url)
    root = ElementTree.fromstring(
        path.read_bytes(),
        parser=ElementTree.XMLParser(target=_MetaCycProteinTreeBuilder()),
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
        or len(pgdbs) != 1
        or pgdbs[0].get("orgid") != "META"
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
        or service_url.scheme not in {"http", "https"}
        or service_url.hostname != host
        or service_url.username is not None
        or service_url.password is not None
        or service_url.port == 0
        or service_url.query
        or service_url.fragment
        or service_url.path not in {"", "/"}
    ):
        raise ValueError("MetaCyc protein metadata names a different source service")
    frame = requested.removeprefix("META:")
    if (
        protein.get("ID") != requested
        or protein.get("frameid") != frame
        or protein.get("orgid") != "META"
        or protein.get("detail") != "full"
        or "resource" in protein.attrib
        or protein.get("class", "false") != "false"
    ):
        raise ValueError("MetaCyc protein source has mismatched or unresolved top-level identity")
    return protein, frame


def _metacyc_protein_one(parent: ElementTree.Element, tag: str) -> ElementTree.Element:
    nodes = parent.findall(tag)
    if len(nodes) != 1:
        raise ValueError(f"MetaCyc protein source requires exactly one {tag}")
    return nodes[0]


def _metacyc_protein_label(
    parent: ElementTree.Element,
    frame: str,
    *,
    activity_frame: str | None = None,
) -> str:
    """Decode a native name after its owning Protein or activity is validated."""
    node = _metacyc_protein_one(parent, "common-name")
    return _metacyc_protein_name(node, frame, activity_frame=activity_frame)


def _metacyc_protein_name(
    node: ElementTree.Element,
    frame: str,
    *,
    activity_frame: str | None = None,
) -> str:
    """Apply the same bounded presentation decoder to a native name slot."""
    if len(node) or not (node.text or "").strip():
        raise ValueError("MetaCyc protein source requires one nonempty common-name")
    if node.get("datatype") != "string" or (
        activity_frame is not None and node.attrib != {"datatype": "string"}
    ):
        raise ValueError("MetaCyc protein common-name must be a native string")
    name = _MetaCycProteinName()
    name.feed(node.text.strip())
    name.close()
    label = " ".join("".join(name.parts).split())
    unresolved = {frame, "META:" + frame, "MetaCyc:" + frame}
    if activity_frame is not None:
        unresolved.update({activity_frame, "META:" + activity_frame, "MetaCyc:" + activity_frame})
    if (
        name.tags
        or not label
        or "<" in label
        or ">" in label
        or re.search(r"&(?:#|[A-Za-z][A-Za-z0-9]*;)", label)
        or any(not _metacyc_protein_name_character(ord(char)) for char in label)
        or label in unresolved
        or label.casefold().startswith(("error", "unknown", "not found"))
    ):
        raise ValueError("MetaCyc protein source lacks a resolved native common-name")
    return label


def _metacyc_protein_reference(node: ElementTree.Element, frame: str, resource: str) -> None:
    if (
        len(node)
        or (node.text or "").strip()
        or node.attrib != {"resource": resource, "orgid": "META", "frameid": frame}
    ):
        raise ValueError("MetaCyc protein source requires an exact empty native reference")


def _metacyc_complex_activities(
    protein: ElementTree.Element,
    frame: str,
) -> list[tuple[ElementTree.Element, str]]:
    """Validate every native enzyme-name relation for an unnamed homomer.

    Pathway Tools documents linked enzymatic-reaction names as protein names
    when COMMON-NAME is absent. This bounded case requires a native homomer
    and an exact enzyme back-reference; it is not a descendant-name search.
    """
    parent = _metacyc_protein_one(protein, "parent")
    parent_class = _metacyc_protein_one(parent, "Protein")
    if (
        len(parent) != 1
        or len(parent_class)
        or (parent_class.text or "").strip()
        or parent_class.attrib
        != {
            "resource": "getxml?META:Protein-Complexes",
            "orgid": "META",
            "frameid": "Protein-Complexes",
            "class": "true",
        }
    ):
        raise ValueError(
            "MetaCyc enzyme-name fallback requires native Protein-Complexes membership"
        )
    component = _metacyc_protein_one(protein, "component")
    subunit = _metacyc_protein_one(component, "Protein")
    subunit_frame = subunit.get("frameid", "")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", subunit_frame) or subunit_frame == frame:
        raise ValueError("MetaCyc enzyme-name fallback has an invalid component frame")
    _metacyc_protein_reference(subunit, subunit_frame, "getxml?META:" + subunit_frame)
    coefficient = _metacyc_protein_one(component, "coefficient")
    if (
        len(coefficient)
        or coefficient.attrib != {"datatype": "integer"}
        or not re.fullmatch(r"[1-9][0-9]*", (coefficient.text or "").strip())
        or int(coefficient.text.strip()) < 2
    ):
        raise ValueError("MetaCyc enzyme-name fallback requires a homomer coefficient at least two")
    catalyzes = _metacyc_protein_one(protein, "catalyzes")
    activities = catalyzes.findall("Enzymatic-Reaction")
    if not activities or len(catalyzes) != len(activities):
        raise ValueError("MetaCyc enzyme-name fallback requires resolved native activities")
    result = []
    seen = set()
    for activity in activities:
        activity_frame = _metacyc_complex_activity_identity(activity, frame)
        if activity_frame in seen:
            raise ValueError("MetaCyc enzyme-name fallback has duplicate activity identities")
        seen.add(activity_frame)
        result.append((activity, activity_frame))
    return result


def _metacyc_complex_activity_identity(activity: ElementTree.Element, frame: str) -> str:
    """Validate one resolved activity and its exact enzyme/reaction references."""
    activity_frame = activity.get("frameid", "")
    if (
        not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", activity_frame)
        or activity.get("ID") != "META:" + activity_frame
        or activity.get("orgid") != "META"
        or activity.get("detail") not in {"low", "full"}
        or set(activity.attrib) != {"ID", "orgid", "frameid", "detail"}
    ):
        raise ValueError(
            "MetaCyc enzyme-name fallback requires one resolved native Enzymatic-Reaction"
        )
    enzyme = _metacyc_protein_one(activity, "enzyme")
    if len(enzyme) != 1:
        raise ValueError("MetaCyc enzyme-name fallback requires one exact enzyme back-reference")
    _metacyc_protein_reference(_metacyc_protein_one(enzyme, "Protein"), frame, "#META:" + frame)
    reaction = _metacyc_protein_one(activity, "reaction")
    native_reaction = _metacyc_protein_one(reaction, "Reaction")
    reaction_frame = native_reaction.get("frameid", "")
    if len(reaction) != 1 or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", reaction_frame):
        raise ValueError(
            "MetaCyc enzyme-name fallback requires one exact native reaction reference"
        )
    _metacyc_protein_reference(native_reaction, reaction_frame, "getxml?META:" + reaction_frame)
    return activity_frame


def _metacyc_protein_aliases(
    parent: ElementTree.Element,
    frame: str,
    *,
    activity_frame: str | None = None,
) -> list[str]:
    """Decode direct native aliases without borrowing names from descendants."""
    aliases = []
    for node in parent.findall("synonym"):
        if node.attrib != {"datatype": "string"}:
            raise ValueError("MetaCyc protein synonym must be an exact native string")
        alias = _metacyc_protein_name(node, frame, activity_frame=activity_frame)
        if alias in aliases:
            raise ValueError("MetaCyc protein source has duplicate native synonyms")
        aliases.append(alias)
    return aliases


def metacyc_protein_terms(
    path: Path,
    *,
    url: str,
    version: str,
) -> list[tuple[str, str, list[str]]]:
    """Extract one native Protein name, including a guarded homomer enzyme name."""
    term, _ = _metacyc_protein_record(path, url=url, version=version)
    return [term]


def _metacyc_protein_record(
    path: Path,
    *,
    url: str,
    version: str,
) -> tuple[tuple[str, str, list[str]], tuple | None]:
    """Return a bounded signature only for the multi-activity alias branch."""
    protein, frame = _metacyc_protein_identity(path, url=url, version=version)
    synonyms: list[str] = []
    signature = None
    if protein.findall("common-name"):
        # Any direct slot takes precedence, including an invalid one that must fail.
        label = _metacyc_protein_label(protein, frame)
    else:
        activities = _metacyc_complex_activities(protein, frame)
        if len(activities) == 1:
            activity, activity_frame = activities[0]
            label = _metacyc_protein_label(activity, frame, activity_frame=activity_frame)
        else:
            aliases = _metacyc_protein_aliases(protein, frame)
            observations = []
            matches = []
            for activity, activity_frame in activities:
                activity_label = _metacyc_protein_label(
                    activity, frame, activity_frame=activity_frame,
                )
                activity_aliases = _metacyc_protein_aliases(
                    activity, frame, activity_frame=activity_frame,
                )
                names = {activity_label, *activity_aliases}
                matches.extend((alias, activity_frame) for alias in aliases if alias in names)
                reaction = activity.find("reaction/Reaction")
                assert reaction is not None  # exact reference validated above
                observations.append((
                    activity_frame, reaction.attrib["frameid"], activity_label,
                    tuple(sorted(activity_aliases)),
                ))
            if len(matches) != 1:
                raise ValueError(
                    "MetaCyc multi-activity homomer requires one unambiguous native alias match"
                )
            label = matches[0][0]
            synonyms = [alias for alias in aliases if alias != label]
            component = protein.find("component/Protein")
            coefficient = protein.find("component/coefficient")
            assert component is not None and coefficient is not None
            signature = (
                version, component.attrib["frameid"], int(coefficient.text.strip()),
                tuple(sorted(observations)), label, tuple(sorted(aliases)),
            )
    return ("MetaCyc:" + frame, label, synonyms), signature


class _MetaCycReactionTreeBuilder(ElementTree.TreeBuilder):
    def doctype(self, name: str, pubid: str | None, system: str | None) -> None:
        raise ValueError("MetaCyc reaction XML must not contain a DOCTYPE")


def _metacyc_reaction_record(
    path: Path,
    *,
    url: str,
    version: str,
) -> tuple[tuple[str, str, list[str]], tuple]:
    """Establish typed native identity for bounded unnamed native reactions.

    This deliberately does not name a reaction from nested curator/evidence
    objects, its equation, or a curated record. Named reactions and more complex
    participant serialization remain unsupported by this bounded adapter.
    """
    request = re.fullmatch(
        rf"https://{re.escape(ECOCYC_HOST)}/getxml\?id=(META:([A-Za-z0-9][A-Za-z0-9_.-]*))",
        url,
    )
    if request is None:
        raise ValueError("MetaCyc reaction requires an exact native HTTPS META request")
    requested, frame = request.groups()
    root = ElementTree.fromstring(
        path.read_bytes(),
        parser=ElementTree.XMLParser(target=_MetaCycReactionTreeBuilder()),
    )

    def one(parent: ElementTree.Element, tag: str) -> ElementTree.Element:
        nodes = parent.findall(tag)
        if len(nodes) != 1:
            raise ValueError(f"MetaCyc reaction requires exactly one direct {tag}")
        return nodes[0]

    def text(parent: ElementTree.Element, tag: str, *, native: bool = False) -> str:
        node = one(parent, tag)
        if (
            len(node)
            or node.attrib != ({"datatype": "string"} if native else {})
            or not (node.text or "").strip()
        ):
            raise ValueError(f"MetaCyc reaction requires one nonempty native {tag}")
        return node.text.strip()

    if root.tag != "ptools-xml" or len(root) != 2:
        raise ValueError("MetaCyc reaction requires native metadata and one direct Reaction")
    metadata, reaction = one(root, "metadata"), one(root, "Reaction")
    if (
        set(root.attrib) != {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        or root.get("{http://www.w3.org/XML/1998/namespace}base")
        not in {
            url,
            f"http://{ECOCYC_HOST}:443/getxml?{requested}",
        }
        or not re.fullmatch(r"[0-9]+(?:\.[0-9]+)+", version)
        or root.get("ptools-version") != version
        or (root.text or "").strip()
        or any((child.tail or "").strip() for child in root)
    ):
        raise ValueError("MetaCyc reaction XML base or native version disagrees with request")
    if metadata.attrib or sorted(n.tag for n in metadata) != sorted(
        ["url", "service_name", "query", "num_results", "PGDB"]
    ):
        raise ValueError("MetaCyc reaction has malformed native metadata")
    if (
        text(metadata, "url")
        not in {
            f"https://{ECOCYC_HOST}/",
            f"http://{ECOCYC_HOST}:443/",
        }
        or text(metadata, "service_name") != "getxml"
        or text(metadata, "query") != requested
        or text(metadata, "num_results") != "1"
    ):
        raise ValueError("MetaCyc reaction service/query identity mismatch")
    pgdb = one(metadata, "PGDB")
    if (
        pgdb.attrib != {"orgid": "META", "version": version}
        or [child.tag for child in pgdb] != ["species"]
        or text(pgdb, "species", native=True) != "MetaCyc"
    ):
        raise ValueError("MetaCyc reaction PGDB/version/species mismatch")
    if reaction.attrib != {
        "ID": requested,
        "orgid": "META",
        "frameid": frame,
        "detail": "full",
    }:
        raise ValueError("MetaCyc reaction has a mismatched or unresolved top-level identity")
    # Any direct slot prevents the identity-only path, including an empty,
    # duplicate, malformed or nested-object name copied into a direct slot.
    if reaction.findall("common-name"):
        raise ValueError("MetaCyc reaction identity-only adapter requires an absent common-name")
    parents = []
    for parent in reaction.findall("parent"):
        child = one(parent, "Reaction")
        parent_frame = child.get("frameid", "")
        if (
            len(parent) != 1
            or parent.attrib
            or (parent.text or "").strip()
            or len(child)
            or (child.text or "").strip()
            or parent_frame
            not in {
                "Chemical-Reactions",
                "Small-Molecule-Reactions",
                "Protein-Modification-Reactions",
            }
            or child.attrib
            != {
                "resource": "getxml?META:" + parent_frame,
                "orgid": "META",
                "frameid": parent_frame,
                "class": "true",
            }
        ):
            raise ValueError("MetaCyc reaction has an unsupported native parent class")
        parents.append(parent_frame)
    protein_mode = parents == ["Protein-Modification-Reactions"]
    if not protein_mode and sorted(parents) != ["Chemical-Reactions", "Small-Molecule-Reactions"]:
        raise ValueError(
            "MetaCyc reaction requires chemical and small-molecule parent classes "
            "or one protein-modification parent"
        )
    if protein_mode and any(
        (node.tail or "").strip() or (node[0].tail or "").strip()
        for node in reaction.findall("parent")
    ):
        raise ValueError("MetaCyc reaction has malformed protein-modification parent text")
    direction = text(reaction, "reaction-direction")
    if direction not in {
        "REVERSIBLE",
        "LEFT-TO-RIGHT",
        "RIGHT-TO-LEFT",
        "PHYSIOL-LEFT-TO-RIGHT",
        "PHYSIOL-RIGHT-TO-LEFT",
    }:
        raise ValueError("MetaCyc reaction has an unsupported native direction")
    sides = []
    for side in ("left", "right"):
        slots = reaction.findall(side)
        if not slots:
            raise ValueError(f"MetaCyc reaction requires nonempty native {side} slots")
        participants = []
        for slot in slots:
            if protein_mode:
                if len(slot) != 1 or slot[0].tag not in {"Protein", "Compound"}:
                    raise ValueError(
                        "MetaCyc reaction requires one typed Protein or Compound side reference"
                    )
                compound = slot[0]
            else:
                compound = one(slot, "Compound")
            compound_frame = compound.get("frameid", "")
            if (
                len(slot) != 1
                or slot.attrib
                or (slot.text or "").strip()
                or len(compound)
                or (compound.text or "").strip()
                or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", compound_frame)
                or compound.attrib
                not in (
                    {
                        "resource": "getxml?META:" + compound_frame,
                        "orgid": "META",
                        "frameid": compound_frame,
                    },
                    {
                        "resource": "getxml?META:" + compound_frame,
                        "orgid": "META",
                        "frameid": compound_frame,
                        "class": "true",
                    },
                )
            ):
                raise ValueError("MetaCyc reaction requires exact native Compound side references")
            # Keep the source's class assertion in conflict comparisons. It
            # does not establish an external chemical/anomer equivalence.
            if protein_mode:
                if (
                    (compound.tag == "Protein" and compound.get("class") != "true")
                    or (slot.tail or "").strip()
                    or (compound.tail or "").strip()
                ):
                    raise ValueError(
                        "MetaCyc reaction requires an exact Protein class/typed side reference"
                    )
                participants.append((compound.tag, compound_frame, compound.get("class")))
            else:
                # Preserve the exact historical old-mode conflict signature.
                participants.append((compound_frame, compound.get("class")))
        frames = [item[1] if protein_mode else item[0] for item in participants]
        if len(participants) != len(set(frames)):
            raise ValueError("MetaCyc reaction repeats a native side participant")
        if protein_mode and not any(item[0] == "Protein" for item in participants):
            raise ValueError(
                "MetaCyc protein-modification reaction requires a Protein class on each side"
            )
        sides.append(tuple(sorted(participants)))
    flags = []
    for tag in ("spontaneous", "physiologically-relevant"):
        if reaction.findall(tag):
            node = one(reaction, tag)
            if (
                node.attrib != {"datatype": "boolean"}
                or len(node)
                or node.text not in {"true", "false"}
            ):
                raise ValueError(f"MetaCyc reaction has a malformed native {tag}")
            flags.append((tag, node.text))
    if reaction.findall("orphan"):
        flags.append(("orphan", text(reaction, "orphan")))
    assertion = (version, tuple(sorted(parents)), direction, *sides, tuple(flags))
    return ("MetaCyc:" + frame, frame, []), assertion


class _EcoCycTreeBuilder(ElementTree.TreeBuilder):
    def doctype(self, name: str, pubid: str | None, system: str | None) -> None:
        raise ValueError("EcoCyc XML must not contain a DOCTYPE")


def _ecocyc_one(parent: ElementTree.Element, tag: str) -> ElementTree.Element:
    nodes = parent.findall(tag)
    if len(nodes) != 1:
        raise ValueError(f"EcoCyc source requires exactly one direct {tag}")
    return nodes[0]


def _ecocyc_text(parent: ElementTree.Element, tag: str, *, native: bool = False) -> str:
    node = _ecocyc_one(parent, tag)
    if (
        len(node)
        or node.attrib != ({"datatype": "string"} if native else {})
        or not (node.text or "").strip()
    ):
        raise ValueError(f"EcoCyc source requires one nonempty native {tag}")
    return node.text.strip()


def _ecocyc_name(node: ElementTree.Element, frame: str) -> str:
    if (
        len(node)
        or node.attrib != {"datatype": "string"}
        or not (node.text or "").strip()
        or any(not _metacyc_protein_name_character(ord(c)) for c in node.text)
    ):
        raise ValueError("EcoCyc name/alias requires one safe native string")
    name = _MetaCycProteinName()
    try:
        name.feed(node.text.strip())
        name.close()
    except ValueError as error:
        raise ValueError("EcoCyc name/alias contains unsafe markup") from error
    label = " ".join("".join(name.parts).split())
    if (
        name.tags
        or not label
        or "<" in label
        or ">" in label
        or re.search(r"&(?:#|[A-Za-z][A-Za-z0-9]*;)", label)
        or any(not _metacyc_protein_name_character(ord(c)) for c in label)
        or label in {frame, "ECOLI:" + frame, "EcoCyc:" + frame}
        or label.casefold().startswith(("error", "unknown", "not found"))
    ):
        raise ValueError("EcoCyc source lacks a resolved native name/alias")
    return label


def _ecocyc_record(
    kind: str,
    path: Path,
    *,
    url: str,
    version: str,
) -> tuple[tuple[str, str, list[str]], str]:
    """Read one ECOLI complex or regulatory RNA, never a nested frame or xref.

    The observed service serializes its HTTPS transport as HTTP on port 443.
    This literal compatibility case does not permit HTTP issuing requests.
    """
    request = re.fullmatch(
        rf"https://{re.escape(ECOCYC_HOST)}/getxml\?id=(ECOLI:([A-Za-z0-9][A-Za-z0-9_.-]*))",
        url,
    )
    if request is None:
        raise ValueError("EcoCyc source requires an exact native HTTPS ECOLI request")
    requested, frame = request.groups()
    root = ElementTree.fromstring(
        path.read_bytes(),
        parser=ElementTree.XMLParser(target=_EcoCycTreeBuilder()),
    )
    tag, parent_classes = ECOCYC_SOURCE_TYPES[kind]
    if root.tag != "ptools-xml" or len(root) != 2:
        raise ValueError("EcoCyc source requires native metadata and one direct entity")
    metadata, entity = _ecocyc_one(root, "metadata"), _ecocyc_one(root, tag)
    base = root.get("{http://www.w3.org/XML/1998/namespace}base", "")
    if (
        set(root.attrib) != {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        or base not in {url, f"http://{ECOCYC_HOST}:443/getxml?{requested}"}
        or not re.fullmatch(r"[0-9]+(?:\.[0-9]+)+", version)
        or root.get("ptools-version") != version
    ):
        raise ValueError("EcoCyc XML base or native version disagrees with the request")
    if metadata.attrib or sorted(n.tag for n in metadata) != sorted(
        ["url", "service_name", "query", "num_results", "PGDB"]
    ):
        raise ValueError("EcoCyc source has malformed native metadata")
    if (
        _ecocyc_text(metadata, "url")
        not in {
            f"https://{ECOCYC_HOST}/",
            f"http://{ECOCYC_HOST}:443/",
        }
        or _ecocyc_text(metadata, "service_name") != "getxml"
        or _ecocyc_text(metadata, "query") != requested
        or _ecocyc_text(metadata, "num_results") != "1"
    ):
        raise ValueError("EcoCyc service/query identity mismatch")
    pgdb = _ecocyc_one(metadata, "PGDB")
    if (
        pgdb.attrib != {"orgid": "ECOLI", "version": version}
        or sorted(n.tag for n in pgdb) != ["dblink", "species", "strain"]
        or _ecocyc_text(pgdb, "species", native=True) != "Escherichia coli"
        or _ecocyc_text(pgdb, "strain", native=True) != "K-12 substr. MG1655"
    ):
        raise ValueError("EcoCyc PGDB/version/species/strain mismatch")
    taxonomy = _ecocyc_one(pgdb, "dblink")
    if (
        taxonomy.attrib
        or sorted(n.tag for n in taxonomy)
        != sorted(["dblink-db", "dblink-oid", "dblink-relationship", "dblink-URL"])
        or _ecocyc_text(taxonomy, "dblink-db") != "NCBI-TAXONOMY-DB"
        or _ecocyc_text(taxonomy, "dblink-oid") != "511145"
        or _ecocyc_text(taxonomy, "dblink-relationship") != "unification"
        or _ecocyc_text(taxonomy, "dblink-URL")
        != ("http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=511145")
    ):
        raise ValueError("EcoCyc native taxon mismatch")
    if entity.attrib != {"ID": requested, "orgid": "ECOLI", "frameid": frame, "detail": "full"}:
        raise ValueError("EcoCyc source has a mismatched or unresolved top-level identity")
    parent = _ecocyc_one(entity, "parent")
    parent_class = _ecocyc_one(parent, tag)
    parent_frame = parent_class.get("frameid", "")
    if (
        len(parent) != 1
        or parent.attrib
        or (parent.text or "").strip()
        or len(parent_class)
        or (parent_class.text or "").strip()
        or parent_frame not in parent_classes
        or parent_class.attrib
        != {
            "resource": "getxml?ECOLI:" + parent_frame,
            "orgid": "ECOLI",
            "frameid": parent_frame,
            "class": "true",
        }
    ):
        raise ValueError("EcoCyc source has a mismatched native RNA/complex parent class")
    label = _ecocyc_name(_ecocyc_one(entity, "common-name"), frame)
    synonyms = [_ecocyc_name(node, frame) for node in entity.findall("synonym")]
    if len(set(synonyms)) != len(synonyms) or label in synonyms:
        raise ValueError("EcoCyc source contains duplicate native names/aliases")
    return ("EcoCyc:" + frame, label, sorted(synonyms)), parent_frame


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
                classes = {item.get(rdf + "resource") for item in node.findall(rdfs + "subClassOf")}
                if "http://rdf.rhea-db.org/GenericPolypeptide" in classes:
                    uri = node.get(rdf + "about", "")
                    match = re.fullmatch(r"http://rdf\.rhea-db\.org/Compound_([0-9]+)", uri)
                    values = {
                        key: [item.text for item in node.findall(rh + key)]
                        for key in ("id", "accession", "name")
                    }
                    if (
                        not match
                        or values["id"] != [match[1]]
                        or values["accession"] != ["GENERIC:" + match[1]]
                        or len(values["name"]) != 1
                        or not values["name"][0]
                        or not values["name"][0].strip()
                    ):
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
    if page._script is not None or page._heading is not None or page._rows or page._cells:
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
    if (
        entity.get("@context") != "https://schema.org"
        or entity.get("@type") != "MolecularEntity"
        or entity.get("identifier") != identifier
        or entity.get("@id") != url
        or entity.get("url") != url
    ):
        raise ValueError("MetaNetX JSON-LD identity, class and production URL must agree")
    label = entity.get("name")
    if (
        not isinstance(label, str)
        or not label.strip()
        or label.strip() in {request[1], identifier}
        or label.strip().casefold().startswith(("error", "unknown", "not found"))
    ):
        raise ValueError("MetaNetX source lacks a resolved native name")
    label = " ".join(label.split())
    visible_ids = [row[1:] for row in page.rows if row and row[0] == "MNX_ID"]
    # The production row also includes an image cell; its text is not identity.
    if (
        len(visible_ids) != 1
        or not visible_ids[0]
        or visible_ids[0][0] != request[1]
        or page.headings != [label]
    ):
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
        request.scheme != "https"
        or request.netloc != "eutils.ncbi.nlm.nih.gov"
        or request.path != "/entrez/eutils/efetch.fcgi"
        or request.fragment
        or any(char.isspace() for char in url)
        or len(fields) != 3
        or set(query) != {"db", "id", "rettype"}
        or query.get("db") != "gene"
        or query.get("rettype") != "xml"
        or not re.fullmatch(r"[1-9][0-9]*", query.get("id", ""))
    ):
        raise ValueError("NCBI Gene source requires one exact official gene EFetch XML request")

    def doctype(name: str, system: str | None, public: str | None, internal: int) -> None:
        if (
            name != "Entrezgene-Set"
            or internal
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
        parent: ElementTree.Element,
        tag: str,
        *,
        optional: bool = False,
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
        len(status)
        or status.attrib != {"value": "live"}
        or (status.text or "").strip() not in {"", "0"}
    ):
        raise ValueError("NCBI Gene explicit status is not an unambiguous live record")
    if track.findall("Gene-track_current-id") or track.findall("Gene-track_discontinue-date"):
        raise ValueError("NCBI Gene redirected or discontinued records are not supported")
    gene_ref = one(one(gene, "Entrezgene_gene"), "Gene-ref")
    label = text(gene_ref, "Gene-ref_locus")
    if (
        any(char.isspace() for char in label)
        or any(char in label for char in "<>&")
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
        if any(char in value for char in "<>&") or any(
            not _metacyc_protein_name_character(ord(char)) for char in value
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


def _bigg_json(path: Path) -> dict[str, Any]:
    """Reject ambiguous JSON, including duplicate keys in nested source objects."""

    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"BiGG source repeats JSON key {key!r}")
            result[key] = value
        return result

    def nonfinite(value: str) -> None:
        raise ValueError(f"BiGG source contains nonfinite JSON value {value}")

    try:
        value = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=unique, parse_constant=nonfinite
        )
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("BiGG source requires original JSON, not HTML or an error page") from error
    if not isinstance(value, dict):
        raise ValueError("BiGG source requires one JSON object")
    return value


def _bigg_record(kind: str, path: Path, url: str) -> tuple[str, str, list[str]]:
    """Extract only a universal native identity and name, never model chemistry."""
    category = BIGG_SOURCE_TYPES[kind]
    request = re.fullmatch(
        r"https://bigg\.ucsd\.edu/api/v2/universal/" + category + r"/([A-Za-z0-9][A-Za-z0-9_]*)",
        url,
    )
    if request is None:
        raise ValueError("BiGG source requires an exact official universal API URL of its kind")
    body = _bigg_json(path)
    common = {"bigg_id", "name", "old_identifiers", "database_links"}
    lists = (
        {"compartments_in_models", "charges", "formulae"}
        if category == "metabolites"
        else {"models_containing_reaction", "metabolites"}
    )
    fields = common | lists
    if category == "reactions":
        fields |= {"reaction_string", "pseudoreaction"}
    if body.keys() != fields or any(not isinstance(body[key], list) for key in lists):
        raise ValueError("BiGG body must be one native universal object of the requested kind")
    if body["bigg_id"] != request[1]:
        raise ValueError("BiGG native bigg_id and requested identity disagree")
    label = body["name"]
    if (
        not isinstance(label, str)
        or not label.strip()
        or any(char in label for char in "<>")
        or any(not _metacyc_protein_name_character(ord(char)) for char in label)
        or label.strip() == body["bigg_id"]
        or label.strip().casefold() in {"unknown", "error", "not found", "not-found", "null"}
    ):
        raise ValueError("BiGG source requires one resolved native name")
    if (
        not isinstance(body["database_links"], dict)
        or not isinstance(body["old_identifiers"], list)
        or any(not isinstance(item, str) or not item.strip() for item in body["old_identifiers"])
    ):
        raise ValueError("BiGG source has malformed native cross-reference containers")
    if category == "reactions" and (
        type(body["pseudoreaction"]) is not bool
        or not isinstance(body["reaction_string"], str)
        or not body["reaction_string"].strip()
    ):
        raise ValueError("BiGG reaction source lacks its native reaction fields")
    # Old identifiers are accessions, not name synonyms. Cross-database links,
    # model bounds, formulae and the displayed universal arrow are not exported.
    return "BiGG:" + request[1], label.strip(), []


def _bigg_version(entry: dict[str, Any], cache_dir: Path) -> tuple[str, str]:
    """Bind a BiGG manifest release to a separately hashed native version original."""
    companion = entry.get("version_source")
    if not isinstance(companion, dict) or companion.keys() != {"url", "path", "sha256"}:
        raise ValueError("BiGG source requires a hashed native version_source companion")
    if companion["url"] != "https://bigg.ucsd.edu/api/v2/database_version":
        raise ValueError("BiGG version source requires the exact official API URL")
    if not isinstance(companion["path"], str) or not companion["path"]:
        raise ValueError("BiGG version source requires a relative cache path")
    relative = Path(companion["path"])
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("BiGG version source requires a relative cache path")
    path = cache_dir / relative
    if hashlib.sha256(path.read_bytes()).hexdigest() != companion["sha256"]:
        raise ValueError("BiGG native version bytes do not match their declared digest")
    body = _bigg_json(path)
    if body.keys() != {"api_version", "bigg_models_version", "last_updated"}:
        raise ValueError("BiGG version source requires the native database version object")
    version = body["bigg_models_version"]
    if (
        body["api_version"] != "v2"
        or not isinstance(version, str)
        or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version)
        or not isinstance(body["last_updated"], str)
        or not re.fullmatch(
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?:\.\d{1,6})?", body["last_updated"]
        )
    ):
        raise ValueError("BiGG version source has an unsupported release or API version")
    match = re.fullmatch(
        r"BiGG Models " + re.escape(version) + r"; retrieved (\d{4}-\d{2}-\d{2})", entry["version"]
    )
    if match is None:
        raise ValueError("BiGG manifest release and native database version disagree")
    try:
        date.fromisoformat(match[1])
        datetime.fromisoformat(body["last_updated"])
    except ValueError as error:
        raise ValueError(
            "BiGG version provenance has an invalid native or acquisition date"
        ) from error
    return version, body["last_updated"]


def _pubchem_record(path: Path, url: str) -> tuple[str, str, list[str]]:
    """Bind one native compound Title to its exact official CID property request."""
    request = re.fullmatch(
        r"https://pubchem\.ncbi\.nlm\.nih\.gov/rest/pug/compound/cid/([1-9][0-9]*)/"
        r"property/Title,IUPACName,MolecularFormula,InChIKey/JSON",
        url,
    )
    if request is None:
        raise ValueError("PubChem requires the exact official single-CID property URL")

    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"PubChem source repeats JSON key {key!r}")
            result[key] = value
        return result

    def nonfinite(value: str) -> None:
        raise ValueError(f"PubChem source contains nonfinite JSON value {value}")

    def finite_float(value: str) -> float:
        number = float(value)
        if not math.isfinite(number):
            nonfinite(value)
        return number

    try:
        body = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=unique,
            parse_constant=nonfinite,
            parse_float=finite_float,
        )
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("PubChem source requires original UTF-8 JSON") from error
    if not isinstance(body, dict) or body.keys() != {"PropertyTable"}:
        raise ValueError("PubChem source requires one native PropertyTable")
    table = body["PropertyTable"]
    if not isinstance(table, dict) or table.keys() != {"Properties"}:
        raise ValueError("PubChem source requires one native Properties array")
    rows = table["Properties"]
    if not isinstance(rows, list) or len(rows) != 1:
        raise ValueError("PubChem source requires exactly one compound property object")
    compound = rows[0]
    if not isinstance(compound, dict) or compound.keys() != {
        "CID",
        "Title",
        "IUPACName",
        "MolecularFormula",
        "InChIKey",
    }:
        raise ValueError("PubChem source lacks the requested native compound properties")
    if type(compound["CID"]) is not int or compound["CID"] != int(request[1]):
        raise ValueError("PubChem request and native CID disagree")
    for field in ("Title", "IUPACName", "MolecularFormula", "InChIKey"):
        value = compound[field]
        if (
            not isinstance(value, str)
            or not value.strip()
            or any(
                ord(char) < 32 or 127 <= ord(char) <= 159 or 0xD800 <= ord(char) <= 0xDFFF
                for char in value
            )
        ):
            raise ValueError(f"PubChem source has an invalid native {field}")
    if not re.fullmatch(r"[A-Z]{14}-[A-Z]{10}-[A-Z]", compound["InChIKey"]):
        raise ValueError("PubChem source has an invalid native InChIKey")
    # Neither IUPACName nor a separately downloaded synonym list is promoted.
    # Formula and InChIKey establish response shape, not cross-source equivalence.
    return "PubChem:" + request[1], compound["Title"].strip(), []


def source_terms(
    kind: str,
    path: Path,
    *,
    url: str | None = None,
    version: str | None = None,
    archive: dict[str, Any] | None = None,
    sha256: str | None = None,
) -> Iterator[tuple[str, str, list[str]]]:
    if archive is not None and kind != PATHBANK_ARCHIVE_KIND:
        raise ValueError("PathBank archive provenance requires the typed ZIP source kind")
    if kind == PATHBANK_ARCHIVE_KIND:
        yield from _pathbank_archive_terms(
            path,
            url=url or "",
            sha256=sha256 or "",
            archive=archive,
        )
    elif kind in {"gocam-tar", "mibig-tar"}:
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
    elif kind == PATHBANK_CONTEXT_KIND:
        yield from context_terms(path.read_bytes(), url or "")
    elif kind == "pathbank-biopax":
        yield from pathbank_terms(ElementTree.parse(path).getroot(), url=url or "")
    elif kind == "rhea-components-rdf-gz":
        yield from rhea_component_terms(path)
    elif kind == "metacyc-html":
        yield from metacyc_terms(path.read_bytes().decode("utf-8", errors="surrogateescape"))
    elif kind == "metacyc-protein-xml":
        yield from metacyc_protein_terms(path, url=url or "", version=version or "")
    elif kind in ECOCYC_SOURCE_TYPES:
        yield _ecocyc_record(kind, path, url=url or "", version=version or "")[0]
    elif kind == "ncbi-entrezgene-xml":
        term, _ = _ncbi_gene_record(path, url or "")
        yield term
    elif kind == "metacyc-reaction-xml":
        term, _ = _metacyc_reaction_record(path, url=url or "", version=version or "")
        yield term
    elif kind == CARRIER_CLASS_KIND:
        native = class_native(path, url or "", version or "")
        yield native["id"], native["direct_common_name"], native["direct_synonyms"]
    elif kind in BIGG_SOURCE_TYPES:
        yield _bigg_record(kind, path, url or "")
    elif kind == "pubchem-compound-property-json":
        yield _pubchem_record(path, url or "")
    elif kind in KEGG_SOURCE_TYPES:
        yield from kegg_terms(path.read_text(encoding="utf-8"), kind, url or "")
    elif kind in GENE_KINDS:
        projector = kegg_gene_project if kind == GENE_KIND else kegg_pseudogene_project
        native = projector(path.read_bytes(), url or "")
        yield native["id"], native["locus"], []
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
    all_aceto_sources = {}
    all_aceto_claims = []
    terms: dict[str, Any] = {}
    sources: dict[str, Any] = {}
    source_keys: set[str] = set()
    kegg_assertions: dict[str, tuple[str, tuple[str, ...]]] = {}
    metanetx_assertions: dict[str, str] = {}
    metacyc_names: dict[str, set[str]] = {}
    metacyc_xml_ids: set[str] = set()
    metacyc_multi_activity_assertions: dict[str, set[tuple | None]] = {}
    metacyc_kinds: dict[str, set[str]] = {}
    metacyc_reaction_assertions: dict[str, tuple] = {}
    metacyc_carrier_assertions: dict[str, tuple] = {}
    new_native_assertions: dict[str, tuple] = {}
    named_assemblies: list[dict] = []
    component_assertions: dict[str, tuple] = {}
    gene_assertions: dict[str, tuple[str, tuple[str, ...], str]] = {}
    bigg_assertions: dict[str, tuple[str, str, str, str]] = {}
    bigg_versions: dict[str, str] = {}
    ecocyc_assertions: dict[str, tuple] = {}
    ecocyc_versions: set[str] = set()
    pubchem_assertions: dict[str, str] = {}
    pathbank_assertions: dict[str, str] = {}
    entries = json.loads(manifest.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise ValueError("source manifest must be a nonempty list")
    gene_sources = {
        index: gene_metadata(entry, cache_dir)
        if entry["kind"] in GENE_KINDS
        else {name: entry[name] for name in ("url", "kind", "native_gene") if name in entry}
        for index, entry in enumerate(entries)
    }
    validate_gene_assertions(gene_sources)
    # Validate complete carrier-reaction assertions and request-only downgrade
    # claims before any source contributes a selected term. Keep ordinary owner
    # serialization unchanged; this temporary inventory is not persisted.
    carrier_sources = {
        index: carrier_reaction_metadata(entry, cache_dir)
        if entry["kind"] == PROTEIN_CARRIER_REACTION_KIND
        else {"url": entry["url"], "kind": entry["kind"]}
        for index, entry in enumerate(entries)
    }
    carrier_reaction_ids = validate_carrier_reaction_assertions(carrier_sources)
    context_sources = {
        index: context_metadata(entry, cache_dir)
        if entry["kind"] == PATHBANK_CONTEXT_KIND
        else {
            name: entry[name]
            for name in ("url", "kind", "archive", "native_pathbank_context")
            if name in entry
        }
        for index, entry in enumerate(entries)
    }
    context_projections = validate_context_assertions(context_sources)
    context_ids = {ident for projection in context_projections.values() for ident in projection}
    context_roots = {
        next(iter(projection)).removeprefix("PathBank:")
        for projection in context_projections.values()
    }
    for entry_index, entry in enumerate(entries):
        for native_kind, companion_field in COMPANION_FIELDS.items():
            if companion_field in entry and entry["kind"] != native_kind:
                raise ValueError("companion source field requires its matching native kind")
        if "counterpart_source" in entry and entry["kind"] != ECOCYC_STATE_KIND:
            raise ValueError(
                "EcoCyc counterpart_source requires the typed protein-state source kind"
            )
        if "class_source" in entry and entry["kind"] != ECOCYC_COMPLEX_KIND:
            raise ValueError("EcoCyc class_source requires the typed complex source kind")
        key = entry["key"]
        if key in source_keys:
            raise ValueError(f"duplicate source key: {key}")
        source_keys.add(key)
        artifact = Path(entry["path"])
        if artifact.is_absolute() or ".." in artifact.parts:
            raise ValueError(f"source {key} requires a relative cache path")
        path = cache_dir / artifact
        if entry["kind"] in ACETO_KINDS | {
            CARRIER_CLASS_KIND,
            ECOCYC_STATE_KIND,
            ELECTRON_TRANSFER_KIND,
            CHEMICAL_CLASS_KIND,
            NAMED_COMPLEX_KIND,
            PATHWAY_KIND,
            RHEA_POLYMER_KIND,
        }:
            # Refuse non-regular resolved originals before the common byte read.
            carrier_original_path(entry, cache_dir)
        metadata = {name: entry[name] for name in ("url", "version", "license")}
        multi_activity_assertion = None
        if "sha256_scope" in entry:
            metadata["sha256_scope"] = entry["sha256_scope"]
        if not all(isinstance(value, str) and value for value in metadata.values()):
            raise ValueError(f"source {key} requires nonempty provenance")
        metadata["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        if metadata["sha256"] != entry.get("sha256"):
            raise ValueError(f"source {key} bytes do not match manifest sha256")
        if "archive" in entry and entry["kind"] != PATHBANK_ARCHIVE_KIND:
            raise ValueError("PathBank archive provenance requires the typed ZIP source kind")
        if context_roots and entry["kind"] in {"biopax", "pathbank-biopax"}:
            if pathbank_body_roots(path) & context_roots:
                raise ValueError("PathBank context rejects an untyped native body identity")
        if entry["kind"] in GENE_KINDS:
            metadata = gene_sources[entry_index]
            identifier, typed_term = gene_term(metadata, key)
            parsed_terms = [(identifier, typed_term["label"], typed_term["synonyms"])]
        elif entry["kind"] == PATHBANK_CONTEXT_KIND:
            metadata = context_sources[entry_index]
            parsed_terms = context_projections[entry_index].values()
        elif entry["kind"] == PATHBANK_ARCHIVE_KIND:
            if entry.keys() != {
                "key",
                "kind",
                "path",
                "url",
                "version",
                "license",
                "sha256",
                "archive",
            }:
                raise ValueError("PathBank ZIP requires closed source manifest fields")
            parsed_terms = _pathbank_archive_terms(
                path,
                url=entry["url"],
                sha256=entry["sha256"],
                archive=entry["archive"],
            )
            metadata.update(
                kind=PATHBANK_ARCHIVE_KIND,
                archive=dict(entry["archive"]),
                pathway_accessions=[
                    identifier.split(":", 1)[1]
                    for identifier, _, _ in parsed_terms
                    if "/" not in identifier
                ],
            )
        elif entry["kind"] in ACETO_KINDS:
            metadata = aceto_metadata(entry, cache_dir)
            identifier, typed_term = aceto_term(metadata, key)
            parsed_terms = [(identifier, typed_term["label"], typed_term["synonyms"])]
        elif entry["kind"] == PROTEIN_CARRIER_REACTION_KIND:
            metadata = carrier_sources[entry_index]
            identifier, typed_term = carrier_reaction_term(metadata, key)
            parsed_terms = [(identifier, typed_term["label"], typed_term["synonyms"])]
        elif entry["kind"] in {
            ELECTRON_TRANSFER_KIND,
            CHEMICAL_CLASS_KIND,
            NAMED_COMPLEX_KIND,
            PATHWAY_KIND,
        }:
            builder, projector, field = {
                PATHWAY_KIND: (pathway_metadata, pathway_term, "native_pathway"),
                ELECTRON_TRANSFER_KIND: (
                    reaction_metadata,
                    reaction_term,
                    "native_electron_transfer",
                ),
                CHEMICAL_CLASS_KIND: (
                    chemical_class_metadata,
                    chemical_class_term,
                    "native_chemical_class",
                ),
                NAMED_COMPLEX_KIND: (
                    named_complex_metadata,
                    named_complex_term,
                    "native_named_complex",
                ),
            }[entry["kind"]]
            metadata = builder(entry, cache_dir)
            identifier, typed_term = projector(metadata, key)
            assertion = (
                entry["kind"],
                json.dumps(metadata[field], sort_keys=True),
                entry["version"],
            )
            registry = (
                ecocyc_assertions if entry["kind"] == NAMED_COMPLEX_KIND else new_native_assertions
            )
            if identifier in registry and registry[identifier] != assertion:
                raise ValueError(f"conflicting native identity/context assertions for {identifier}")
            registry[identifier] = assertion
            if entry["kind"] == NAMED_COMPLEX_KIND:
                named_assemblies.append(metadata["native_named_complex"])
                ecocyc_versions.add(entry["version"])
                if len(ecocyc_versions) != 1:
                    raise ValueError("conflicting EcoCyc native PGDB versions")
            parsed_terms = [(identifier, typed_term["label"], typed_term["synonyms"])]
        elif entry["kind"] == RHEA_POLYMER_KIND:
            metadata = polymer_metadata(entry, cache_dir)
            parsed_terms = [
                (identifier, native["name"], [])
                for identifier, native in metadata["native_polymers"].items()
            ]
        elif entry["kind"] == "metacyc-reaction-xml":
            term, assertion = _metacyc_reaction_record(
                path,
                url=entry["url"],
                version=entry["version"],
            )
            identifier = term[0]
            if (
                identifier in metacyc_reaction_assertions
                and metacyc_reaction_assertions[identifier] != assertion
            ):
                raise ValueError(f"conflicting MetaCyc reaction native assertions for {identifier}")
            metacyc_reaction_assertions[identifier] = assertion
            metadata["kind"] = "metacyc-reaction-xml"
            parsed_terms = [term]
        elif entry["kind"] == CARRIER_CLASS_KIND:
            metadata = class_metadata(entry, cache_dir)
            identifier, typed_term = class_term(metadata, key)
            assertion = (
                json.dumps(metadata["native_carrier_class"], sort_keys=True),
                entry["version"],
            )
            if (
                identifier in metacyc_carrier_assertions
                and metacyc_carrier_assertions[identifier] != assertion
            ):
                raise ValueError(
                    f"conflicting MetaCyc carrier-class native assertions for {identifier}"
                )
            metacyc_carrier_assertions[identifier] = assertion
            parsed_terms = [(identifier, typed_term["label"], typed_term["synonyms"])]
        elif entry["kind"] == ECOCYC_STATE_KIND:
            metadata = state_metadata(entry, cache_dir)
            identifier, typed_term = state_term(metadata, key)
            # Both whole originals assert a native instance identity, including
            # when the companion is not selected as its own corpus term.
            for observation in (metadata, metadata["counterpart"]):
                native = observation["native_protein_state"]
                assertion = (
                    ECOCYC_STATE_KIND,
                    json.dumps(native, sort_keys=True),
                    observation["version"],
                )
                observed_id = native["id"]
                if observed_id in ecocyc_assertions and ecocyc_assertions[observed_id] != assertion:
                    raise ValueError(
                        f"conflicting EcoCyc native identity assertions for {observed_id}"
                    )
                ecocyc_assertions[observed_id] = assertion
            ecocyc_versions.add(entry["version"])
            if len(ecocyc_versions) != 1:
                raise ValueError("conflicting EcoCyc native PGDB versions")
            parsed_terms = [(identifier, typed_term["label"], typed_term["synonyms"])]
        elif entry["kind"] in BIGG_SOURCE_TYPES:
            version = _bigg_version(entry, cache_dir)
            if version[0] in bigg_versions and bigg_versions[version[0]] != version[1]:
                raise ValueError("conflicting BiGG native database version observations")
            bigg_versions[version[0]] = version[1]
            term = _bigg_record(entry["kind"], path, entry["url"])
            identifier, label, _ = term
            assertion = (entry["kind"], label, *version)
            if identifier in bigg_assertions and bigg_assertions[identifier] != assertion:
                raise ValueError(f"conflicting BiGG native identity assertions for {identifier}")
            bigg_assertions[identifier] = assertion
            parsed_terms = [term]
        elif entry["kind"] == ECOCYC_COMPLEX_KIND:
            metadata = complex_metadata(entry, cache_dir)
            identifier, typed_term = complex_term(metadata, key)
            assertion = (
                entry["kind"],
                json.dumps(metadata["native_complex"], sort_keys=True),
                entry["version"],
            )
            if identifier in ecocyc_assertions and ecocyc_assertions[identifier] != assertion:
                raise ValueError(f"conflicting EcoCyc native identity assertions for {identifier}")
            ecocyc_assertions[identifier] = assertion
            ecocyc_versions.add(entry["version"])
            if len(ecocyc_versions) != 1:
                raise ValueError("conflicting EcoCyc native PGDB versions")
            parsed_terms = [(identifier, typed_term["label"], typed_term["synonyms"])]
        elif entry["kind"] in ECOCYC_SOURCE_TYPES:
            term, parent_class = _ecocyc_record(
                entry["kind"],
                path,
                url=entry["url"],
                version=entry["version"],
            )
            identifier, label, synonyms = term
            assertion = (entry["kind"], parent_class, label, tuple(synonyms), entry["version"])
            if identifier in ecocyc_assertions and ecocyc_assertions[identifier] != assertion:
                raise ValueError(f"conflicting EcoCyc native identity assertions for {identifier}")
            ecocyc_assertions[identifier] = assertion
            ecocyc_versions.add(entry["version"])
            if len(ecocyc_versions) != 1:
                raise ValueError("conflicting EcoCyc native PGDB versions")
            parsed_terms = [term]
        elif entry["kind"] == "metacyc-protein-xml":
            term, multi_activity_assertion = _metacyc_protein_record(
                path, url=entry["url"], version=entry["version"],
            )
            parsed_terms = [term]
        elif entry["kind"] == "ncbi-entrezgene-xml":
            term, taxon = _ncbi_gene_record(path, entry["url"])
            identifier, label, synonyms = term
            assertion = (label, tuple(synonyms), taxon)
            if identifier in gene_assertions and gene_assertions[identifier] != assertion:
                raise ValueError(f"conflicting NCBI Gene native assertions for {identifier}")
            gene_assertions[identifier] = assertion
            parsed_terms = [term]
        else:
            parsed_terms = source_terms(
                entry["kind"],
                path,
                url=entry["url"],
                version=entry["version"],
            )
        all_aceto_sources[key] = metadata
        for identifier, label, synonyms in parsed_terms:
            if is_gene_id(identifier) and entry["kind"] not in GENE_KINDS:
                raise ValueError("KEGG gene identity requires its complete typed source")
            if identifier in context_ids and entry["kind"] != PATHBANK_CONTEXT_KIND:
                raise ValueError("PathBank context rejects a competing parsed native identity")
            # Body-derived identity is authoritative even when its request URL
            # has no frame identifier. Check every claim before corpus selection.
            if (
                identifier in carrier_reaction_ids
                and entry["kind"] != PROTEIN_CARRIER_REACTION_KIND
            ):
                raise ValueError(
                    f"{identifier}: protein-carrier native identity requires "
                    "its complete typed scope"
                )
            if identifier.startswith(("MetaCyc:", "EcoCyc:")):
                all_aceto_claims.append((identifier, key))
            if identifier.startswith("MetaCyc:"):
                kinds = metacyc_kinds.setdefault(identifier, set())
                kinds.add(entry["kind"])
                if "metacyc-reaction-xml" in kinds and len(kinds) != 1:
                    raise ValueError(
                        f"conflicting MetaCyc reaction identity scope for {identifier}"
                    )
                if (
                    kinds.intersection(
                        {
                            ELECTRON_TRANSFER_KIND,
                            CHEMICAL_CLASS_KIND,
                            PATHWAY_KIND,
                            PROTEIN_CARRIER_REACTION_KIND,
                        }
                    )
                    and len(kinds) != 1
                ):
                    raise ValueError(
                        f"conflicting MetaCyc typed native identity scope for {identifier}"
                    )
                if CARRIER_CLASS_KIND in kinds and len(kinds) != 1:
                    raise ValueError(
                        f"conflicting MetaCyc carrier-class identity scope for {identifier}"
                    )
            if identifier.startswith("RHEA-COMP:"):
                native = (
                    metadata["native_polymers"][identifier]
                    if entry["kind"] == RHEA_POLYMER_KIND
                    else None
                )
                assertion = (
                    entry["kind"],
                    json.dumps(native, sort_keys=True) if native else (label, tuple(synonyms)),
                )
                previous = component_assertions.get(identifier)
                if (
                    previous is not None
                    and (RHEA_POLYMER_KIND in {previous[0], entry["kind"]})
                    and previous != assertion
                ):
                    raise ValueError(
                        f"conflicting Rhea component identity assertions for {identifier}"
                    )
                component_assertions[identifier] = assertion
            if identifier.startswith("PubChem:"):
                if entry["kind"] != "pubchem-compound-property-json":
                    raise ValueError(
                        "PubChem identifiers require native compound property authority"
                    )
                if identifier in pubchem_assertions and pubchem_assertions[identifier] != label:
                    raise ValueError(f"conflicting PubChem native names for {identifier}")
                pubchem_assertions[identifier] = label
            if (
                entry["kind"] in {"pathbank-biopax", PATHBANK_ARCHIVE_KIND, PATHBANK_CONTEXT_KIND}
                and "/" not in identifier
            ):
                if identifier in pathbank_assertions and pathbank_assertions[identifier] != label:
                    raise ValueError(f"conflicting PathBank native pathway names for {identifier}")
                pathbank_assertions[identifier] = label
            if (
                identifier.startswith("EcoCyc:")
                and entry["kind"] not in ECOCYC_SOURCE_TYPES
                and entry["kind"]
                not in {ECOCYC_COMPLEX_KIND, ECOCYC_STATE_KIND, NAMED_COMPLEX_KIND, NESTED_KIND}
            ):
                raise ValueError("EcoCyc identifiers require native ECOLI XML authority")
            if identifier.startswith("BiGG:") and entry["kind"] not in BIGG_SOURCE_TYPES:
                raise ValueError("BiGG identifiers require native universal JSON authority")
            if entry["kind"] in {"metacyc-protein-xml", "metacyc-html"}:
                scopes = metacyc_multi_activity_assertions.setdefault(identifier, set())
                scopes.add(multi_activity_assertion)
                if len(scopes) != 1:
                    raise ValueError(
                        f"conflicting MetaCyc multi-activity native assertions for {identifier}"
                    )
                names = metacyc_names.setdefault(identifier, set())
                names.add(label)
                if entry["kind"] == "metacyc-protein-xml":
                    metacyc_xml_ids.add(identifier)
                if identifier in metacyc_xml_ids and len(names) != 1:
                    raise ValueError(f"conflicting MetaCyc protein native names for {identifier}")
            if (
                identifier.startswith("metanetx.chemical:")
                and entry["kind"] != "metanetx-chemical-html"
            ):
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
            if entry["kind"] in {
                ELECTRON_TRANSFER_KIND,
                CHEMICAL_CLASS_KIND,
                NAMED_COMPLEX_KIND,
                PATHWAY_KIND,
            }:
                projector = {
                    PATHWAY_KIND: pathway_term,
                    ELECTRON_TRANSFER_KIND: reaction_term,
                    CHEMICAL_CLASS_KIND: chemical_class_term,
                    NAMED_COMPLEX_KIND: named_complex_term,
                }[entry["kind"]]
                terms[identifier] = projector(metadata, key)[1]
            if entry["kind"] == PATHBANK_CONTEXT_KIND:
                terms[identifier] = context_term(identifier, context_projections[entry_index], key)
            if entry["kind"] in GENE_KINDS:
                terms[identifier] = gene_term(metadata, key)[1]
            if entry["kind"] in ACETO_KINDS:
                terms[identifier] = aceto_term(metadata, key)[1]
            if entry["kind"] == PROTEIN_CARRIER_REACTION_KIND:
                terms[identifier] = carrier_reaction_term(metadata, key)[1]
            if entry["kind"] == RHEA_POLYMER_KIND:
                terms[identifier] = polymer_term(metadata, key, identifier)[1]
            if entry["kind"] == ECOCYC_COMPLEX_KIND:
                terms[identifier] = complex_term(metadata, key)[1]
            if entry["kind"] == CARRIER_CLASS_KIND:
                terms[identifier] = class_term(metadata, key)[1]
            if entry["kind"] == ECOCYC_STATE_KIND:
                terms[identifier] = state_term(metadata, key)[1]
            if entry["kind"] == "metacyc-reaction-xml":
                terms[identifier].update(label_kind="source_context", entity_type="reaction")
            if (
                (identifier.startswith("WikiPathways:") and "/" in identifier)
                or (
                    entry["kind"] in {"pathbank-biopax", PATHBANK_ARCHIVE_KIND}
                    and "/" in identifier
                )
                or identifier.startswith("MIBiG:")
                or (
                    entry["kind"] == "gocam-tar"
                    and identifier.split(":", 1)[0] in {"SGD", "gomodel"}
                )
            ):
                terms[identifier]["label_kind"] = "source_context"
            sources[key] = metadata
    validate_aceto_assertions(all_aceto_sources, all_aceto_claims)
    validate_named_complex_graph(named_assemblies)
    for source, metadata in sources.items():
        if metadata.get("kind") == RHEA_POLYMER_KIND:
            metadata["native_polymers"] = {
                identifier: native
                for identifier, native in metadata["native_polymers"].items()
                if identifier in terms and terms[identifier]["source"] == source
            }
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
