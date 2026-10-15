#!/usr/bin/env python3
"""Extract a compact identifier authority from independently acquired OAK databases.

Only the requested identifiers come from the corpus. Labels, exact synonyms,
release identifiers and licenses are read from the authority's Semantic SQL
database, or explicitly selected original Rhea RDF with pinned provenance.
Missing identifiers abort the build, rather than seeding
the snapshot with the labels that it is intended to validate.

Example (replace the database paths with downloaded OAK Semantic SQL releases)::

    uv run python scripts/build_ontology_identifier_snapshot.py \
        --source GO=/path/to/go.db --source CHEBI=/path/to/chebi.db \
        --source NCBITaxon=/path/to/ncbitaxon.db --source RHEA=/path/to/rhea.db \
        --corpus data/pathways --include-id GO:0008150 --include-id GO:0006096 \
        --include-id GO:0005975 --output data/identifier_authorities/ontology.json

The recorded SHA-256 identifies the complete uncompressed Semantic SQL database
bytes, not the OWL/OBO version IRI in ``url`` or a compressed download archive.
``sha256_scope`` records that distinction. Acquiring a new release and refreshing
this artifact is an explicit, reviewable operation; ordinary QC consumes the
committed snapshot without a network dependency.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

import yaml


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def walk_identifiers(value: Any, prefixes: set[str]) -> set[str]:
    """Select nested identifier slots, excluding citation-only references.

    References may preserve obsolete source identifiers without declaring
    biological nodes. The same identifier elsewhere, or in --include-id,
    still requires independent authority resolution.
    """
    if isinstance(value, dict):
        identifiers = set()
        for key, item in value.items():
            if key == "references":
                continue
            if key in {"id", "subject_id", "object_id", "source_id", "target_id"}:
                identifiers.update(walk_identifiers(item, prefixes))
            elif isinstance(item, (dict, list)):
                identifiers.update(walk_identifiers(item, prefixes))
        return identifiers
    if isinstance(value, list):
        return set().union(*(walk_identifiers(item, prefixes) for item in value))
    if isinstance(value, str) and value.partition(":")[0] in prefixes:
        if any(character.isspace() for character in value):
            raise ValueError(f"Whitespace in selected identifier: {value!r}")
        return {value}
    return set()


def walk_labels(value: Any) -> list[tuple[str, str]]:
    if isinstance(value, dict):
        pairs = []
        if isinstance(value.get("id"), str) and isinstance(value.get("label"), str):
            pairs.append((value["id"], value["label"]))
        for key, item in value.items():
            if key != "references":
                pairs.extend(walk_labels(item))
        return pairs
    if isinstance(value, list):
        return [pair for item in value for pair in walk_labels(item)]
    return []


def expand_iri(value: str, prefixes: dict[str, str]) -> str:
    value = value.strip("<>")
    prefix, separator, local = value.partition(":")
    if separator and prefix in prefixes:
        return prefixes[prefix] + local
    return value


def read_source(connection: sqlite3.Connection, path: Path) -> dict[str, str]:
    prefixes = dict(connection.execute("SELECT prefix, base FROM prefix"))
    # Query the ontology's version declaration first, then use that same
    # subject for all metadata: imported ontologies cannot supply its license.
    declarations = list(connection.execute(
        "SELECT subject, object FROM statements WHERE predicate='owl:versionIRI'"
    ))
    if len(declarations) != 1 or not declarations[0][1]:
        raise ValueError(f"{path}: expected one ontology owl:versionIRI declaration")
    subject, release = declarations[0]
    metadata = {
        predicate: object_value or literal_value
        for predicate, object_value, literal_value in connection.execute(
            "SELECT predicate, object, value FROM statements WHERE subject=? "
            "AND predicate IN ('owl:versionInfo', 'dcterms:license')", (subject,)
        )
    }
    if not metadata.get("owl:versionInfo") or not metadata.get("dcterms:license"):
        raise ValueError(f"{path}: missing ontology release or license metadata")
    return {
        "url": expand_iri(release, prefixes),
        "version": metadata["owl:versionInfo"],
        "sha256": sha256_file(path),
        "sha256_scope": "uncompressed_semantic_sql_database",
        "license": expand_iri(metadata["dcterms:license"], prefixes),
    }


def extract_terms(
    connection: sqlite3.Connection, identifiers: list[str], source_key: str
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    terms = {}
    missing = []
    for identifier in identifiers:
        rows = list(connection.execute(
            "SELECT predicate, value FROM statements WHERE subject=? AND predicate "
            "IN ('rdfs:label', 'oio:hasExactSynonym')", (identifier,)
        ))
        labels = {value for predicate, value in rows if predicate == "rdfs:label" and value}
        if len(labels) != 1:
            missing.append(identifier)
            continue
        label = labels.pop()
        terms[identifier] = {
            "label": label,
            "synonyms": sorted({
                value for predicate, value in rows
                if predicate == "oio:hasExactSynonym" and value and value != label
            }),
            "source": source_key,
        }
    return terms, missing


def read_rhea_updates(
    manifest: Path, cache_dir: Path, selected: set[str]
) -> tuple[str, dict[str, str], dict[str, dict[str, Any]]]:
    """Extract explicitly selected current equations from original Rhea RDF.

    An older Semantic SQL release can predate a chemistry correction. Never
    turn its obsolete equation into a synonym of the corrected reaction.
    """
    entry = json.loads(manifest.read_text(encoding="utf-8"))
    fields = {"key", "path", "url", "version", "license", "sha256", "ids"}
    if not isinstance(entry, dict) or set(entry) != fields:
        raise ValueError("Rhea update manifest has unexpected or missing fields")
    if not all(isinstance(entry[k], str) and entry[k].strip() for k in fields - {"ids"}):
        raise ValueError("Rhea update requires nonempty provenance")
    ids = entry["ids"]
    if (not isinstance(ids, list) or not ids
            or any(not isinstance(i, str) or not re.fullmatch(r"RHEA:[0-9]+", i) for i in ids)
            or len(ids) != len(set(ids)) or not set(ids) <= selected):
        raise ValueError("Rhea update IDs must be unique selected RHEA identifiers")
    artifact = Path(entry["path"])
    if artifact.is_absolute() or ".." in artifact.parts:
        raise ValueError("Rhea update requires a relative cache path")
    path = cache_dir / artifact
    if sha256_file(path) != entry["sha256"]:
        raise ValueError("Rhea RDF bytes do not match manifest sha256")
    rh_uri = "http://rdf.rhea-db.org/"
    rh = "{" + rh_uri + "}"
    rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
    rdfs = "{http://www.w3.org/2000/01/rdf-schema#}"
    wanted = {rh_uri + i.split(":")[1]: i for i in ids}
    terms = {}
    with gzip.open(path, "rb") as stream:
        depth = 0
        for event, node in ElementTree.iterparse(stream, events=("start", "end")):
            if event == "start":
                depth += 1
                if depth == 1:
                    root = node
                continue
            if depth == 2:
                identifier = wanted.get(node.get(rdf + "about", ""))
                if identifier:
                    labels = [item.text for item in node.findall(rdfs + "label")]
                    classes = {item.get(rdf + "resource")
                               for item in node.findall(rdfs + "subClassOf")}
                    if (identifier in terms
                            or [item.text for item in node.findall(rh + "id")]
                            != [identifier.split(":")[1]]
                            or [item.text for item in node.findall(rh + "accession")]
                            != [identifier]
                            or not classes & {rh_uri + c for c in (
                                "Reaction", "DirectionalReaction", "BidirectionalReaction")}
                            or [item.get(rdf + "resource") for item in node.findall(rh + "status")]
                            != [rh_uri + "Approved"]
                            or len(labels) != 1 or not labels[0] or not labels[0].strip()
                            or [item.text for item in node.findall(rh + "equation")] != labels):
                        raise ValueError(
                            f"Invalid or duplicate approved Rhea reaction: {identifier}"
                        )
                    terms[identifier] = {
                        "label": labels[0], "synonyms": [], "source": entry["key"],
                    }
                root.clear()
            depth -= 1
    if set(terms) != set(ids):
        missing = sorted(set(ids) - terms.keys())
        raise ValueError("Rhea RDF lacks requested reactions: " + ", ".join(missing))
    metadata = {k: entry[k] for k in ("url", "version", "license", "sha256")}
    metadata["sha256_scope"] = "complete_original_gzip_rdf"
    return entry["key"], metadata, terms


def build_snapshot(
    sources: dict[str, Path], corpus: Path, include_ids: list[str], output: Path,
    rhea_manifest: Path | None = None, cache_dir: Path | None = None,
) -> int:
    paths = sorted(path for path in corpus.rglob("*.yaml") if path.is_file())
    if not paths:
        raise ValueError(f"No pathway YAML files under {corpus}")
    selected = set(include_ids)
    labels = []
    for path in paths:
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        selected.update(walk_identifiers(record, set(sources)))
        labels.extend((str(path), identifier, label) for identifier, label in walk_labels(record))
    if not selected:
        raise ValueError("No ontology identifiers selected")
    unconfigured = sorted(identifier for identifier in selected
                          if identifier.partition(":")[0] not in sources)
    if unconfigured:
        raise ValueError(f"No authority configured for: {', '.join(unconfigured)}")
    snapshot: dict[str, Any] = {"version": 1, "sources": {}, "terms": {}}
    updates = {}
    if rhea_manifest is not None:
        if cache_dir is None:
            raise ValueError("Rhea updates require --cache-dir")
        key, metadata, updates = read_rhea_updates(rhea_manifest, cache_dir, selected)
        snapshot["sources"][key] = metadata
        snapshot["terms"].update(updates)
    missing = []
    for prefix, path in sorted(sources.items()):
        identifiers = sorted(identifier for identifier in selected
                             if identifier.startswith(prefix + ":"))
        if not identifiers:
            raise ValueError(f"{prefix}: configured source has no selected identifiers")
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"{prefix}: unavailable or empty authority database: {path}")
        with sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True) as connection:
            # The SHA identifies the authority independently of any corpus value.
            source = read_source(connection, path)
            source_key = f"{prefix.lower()}-{source['version']}"
            if source_key in snapshot["sources"]:
                raise ValueError(f"Duplicate authority source key: {source_key}")
            terms, unresolved = extract_terms(
                connection, [i for i in identifiers if i not in updates], source_key
            )
        snapshot["sources"][source_key] = source
        snapshot["terms"].update(terms)
        missing.extend(unresolved)
        print(f"{prefix}: resolved {len(terms)}/{len(identifiers)} from {source['url']}")
    for path, identifier, label in labels:
        term = snapshot["terms"].get(identifier)
        if term and label != term["label"] and label not in term["synonyms"]:
            print(f"LABEL_DIFFERENCE\t{path}\t{identifier}\t{label}\t{term['label']}")
    if missing:
        for identifier in missing:
            print(f"UNRESOLVED\t{identifier}", file=sys.stderr)
        print("Snapshot not written: resolve missing authority identifiers first.", file=sys.stderr)
        return 1
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {len(snapshot['terms'])} authority terms to {output}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", action="append", required=True, metavar="PREFIX=SQLITE")
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--include-id", action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--rhea-updates", type=Path,
                        help="Explicit current-Rhea RDF manifest; never reads labels from records")
    parser.add_argument("--cache-dir", type=Path, help="Root for Rhea manifest artifact paths")
    args = parser.parse_args(argv)
    sources = {}
    for argument in args.source:
        prefix, separator, filename = argument.partition("=")
        if not separator or not prefix or not filename or prefix in sources:
            parser.error("each --source must be a unique PREFIX=SQLITE pair")
        sources[prefix] = Path(filename)
    try:
        if args.cache_dir is not None and args.rhea_updates is None:
            parser.error("--cache-dir requires --rhea-updates")
        return build_snapshot(sources, args.corpus, args.include_id, args.output,
                              args.rhea_updates, args.cache_dir)
    except (
        OSError, ValueError, EOFError, ElementTree.ParseError, sqlite3.Error, yaml.YAMLError
    ) as error:
        print(f"Authority snapshot failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
