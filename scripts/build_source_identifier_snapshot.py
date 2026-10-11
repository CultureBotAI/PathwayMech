#!/usr/bin/env python3
"""Extract identifier authority metadata from explicitly supplied primary sources.

The JSON manifest is a list of objects with key, kind, path, url, version,
license and sha256. Paths are relative to --cache-dir; supported kinds are enzyme,
gocam-tar, mibig-tar, uniprot, gpml, biopax, pathbank-biopax, metacyc-html and
ncbi-protein-xml, rhea-components-rdf-gz, kegg-module-flatfile,
kegg-reaction-flatfile and kegg-compound-flatfile. Source files are
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
from pathlib import Path
from typing import Any
from urllib.parse import urldefrag, urljoin
from xml.etree import ElementTree

import yaml

SOURCE_NAMESPACES = frozenset(
    {
        "EC", "MIBiG", "MetaCyc", "NCBIProtein", "PathBank", "Reactome", "SGD", "UniProtKB",
        "WikiPathways", "gomodel", "RHEA-COMP", "KEGG",
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


def pathbank_terms(root: ElementTree.Element) -> Iterator[tuple[str, str, list[str]]]:
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
    pathways = root.findall(bp + "Pathway")
    if len(pathways) != 1:
        raise ValueError("PathBank authority requires exactly one native Pathway")
    pathway = pathways[0]
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
        raise ValueError("PathBank pathway requires one unambiguous SMPDB unification accession")
    accession = next(iter(accessions))
    about = pathway.get(rdf + "about", "")
    if about.startswith(("http://identifiers.org/smpdb/", "https://identifiers.org/smpdb/")):
        if not re.fullmatch(r"https?://identifiers\.org/smpdb/" + accession, about):
            raise ValueError("PathBank pathway URI and SMPDB xref must agree")
    names = labels(pathway)
    if not names:
        raise ValueError("PathBank pathway lacks a native label")
    identifier = "PathBank:" + accession
    yield identifier, names[0], names[1:]

    graph_types = {
        bp + kind for kind in (
            "BiochemicalReaction", "Complex", "PhysicalEntity", "SmallMolecule",
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


def metacyc_terms(text: str) -> Iterator[tuple[str, str, list[str]]]:
    """Read native ID and native title from a public Pathway Tools object page."""
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


def source_terms(
    kind: str, path: Path, *, url: str | None = None,
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
        yield from pathbank_terms(ElementTree.parse(path).getroot())
    elif kind == "rhea-components-rdf-gz":
        yield from rhea_component_terms(path)
    elif kind == "metacyc-html":
        yield from metacyc_terms(path.read_text(encoding="utf-8"))
    elif kind in KEGG_SOURCE_TYPES:
        yield from kegg_terms(path.read_text(encoding="utf-8"), kind, url or "")
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
        for identifier, label, synonyms in source_terms(entry["kind"], path, url=entry["url"]):
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
