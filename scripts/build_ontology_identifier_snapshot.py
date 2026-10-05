#!/usr/bin/env python3
"""Extract a compact identifier authority from independently acquired OAK databases.

Only the requested identifiers come from the corpus. Labels, exact synonyms,
release identifiers and licenses are read exclusively from the authority's
Semantic SQL database. Missing identifiers abort the build, rather than seeding
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
import hashlib
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any

import yaml


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def walk_identifiers(value: Any, prefixes: set[str]) -> set[str]:
    """Select identifier slots, including those in nested files and mappings."""
    if isinstance(value, dict):
        identifiers = set()
        for key, item in value.items():
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
        for item in value.values():
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


def build_snapshot(
    sources: dict[str, Path], corpus: Path, include_ids: list[str], output: Path
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
            terms, unresolved = extract_terms(connection, identifiers, source_key)
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
    args = parser.parse_args(argv)
    sources = {}
    for argument in args.source:
        prefix, separator, filename = argument.partition("=")
        if not separator or not prefix or not filename or prefix in sources:
            parser.error("each --source must be a unique PREFIX=SQLITE pair")
        sources[prefix] = Path(filename)
    try:
        return build_snapshot(sources, args.corpus, args.include_id, args.output)
    except (OSError, ValueError, sqlite3.Error, yaml.YAMLError) as error:
        print(f"Authority snapshot failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
