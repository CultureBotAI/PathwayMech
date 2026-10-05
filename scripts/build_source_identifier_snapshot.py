#!/usr/bin/env python3
"""Extract identifier authority metadata from explicitly supplied primary sources.

The JSON manifest is a list of objects with key, kind, path, url, version,
license and sha256. Paths are relative to --cache-dir; supported kinds are enzyme,
gocam-tar, mibig-tar, uniprot, gpml, biopax and metacyc-html. Source files are
never generated from curated labels. The corpus only selects which identifiers
to retain, keeping the checked-in authority small and provenance auditable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tarfile
from collections.abc import Iterator
from html import unescape
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

import yaml

SOURCE_NAMESPACES = frozenset(
    {"EC", "MIBiG", "MetaCyc", "Reactome", "SGD", "UniProtKB", "WikiPathways", "gomodel"}
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


def source_terms(kind: str, path: Path) -> Iterator[tuple[str, str, list[str]]]:
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
    elif kind == "metacyc-html":
        yield from metacyc_terms(path.read_text(encoding="utf-8"))
    else:
        raise ValueError(f"unsupported source kind: {kind}")


def build_snapshot(manifest: Path, records: Path, cache_dir: Path) -> dict[str, Any]:
    wanted = corpus_ids(records)
    terms: dict[str, Any] = {}
    sources: dict[str, Any] = {}
    entries = json.loads(manifest.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise ValueError("source manifest must be a nonempty list")
    for entry in entries:
        key = entry["key"]
        if key in sources:
            raise ValueError(f"duplicate source key: {key}")
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
        for identifier, label, synonyms in source_terms(entry["kind"], path):
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
