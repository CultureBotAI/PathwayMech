#!/usr/bin/env python3
"""Backfill retained source-mapping rows from raw provider pathway files."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

import yaml

from pathwaymech.biopax import biopax_to_pathway_record, load_biopax
from pathwaymech.chebi import load_chebi_xrefs
from pathwaymech.schema import validate_record
from pathwaymech.source_mapping import unique_source_mappings
from pathwaymech.wikipathways import (
    gpml_to_pathway_record,
    load_gpml_pathway,
    wikipathways_fallback_id,
)
from pathwaymech.yaml_io import load_yaml_file, pathway_files

ROOT = Path(__file__).resolve().parents[1]
TOP_LEVEL_KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*:", re.MULTILINE)


class IndentDumper(yaml.SafeDumper):
    """Emit block sequences under their mapping key."""

    def increase_indent(self, flow: bool = False, indentless: bool = False) -> None:
        return super().increase_indent(flow, False)


class BackfillError(ValueError):
    """Raised when a raw import cannot safely update the curated corpus."""


@dataclass(frozen=True)
class BackfillResult:
    path: Path
    record_id: str
    added: int


@dataclass(frozen=True)
class PendingBackfill:
    path: Path
    text: str
    result: BackfillResult


def raw_source_records(
    *,
    wikipathways_gpml: list[Path],
    reactome_biopax: list[Path],
    chebi_obo: Path | None = None,
) -> list[dict[str, Any]]:
    records = []
    compound_mappings = (
        load_chebi_xrefs(chebi_obo) if chebi_obo and wikipathways_gpml else {}
    )

    for path in wikipathways_gpml:
        records.append(
            gpml_to_pathway_record(
                load_gpml_pathway(path),
                wikipathways_fallback_id(path),
                compound_mappings,
            )
        )
    for path in reactome_biopax:
        records.append(biopax_to_pathway_record(load_biopax(path), f"Reactome:{path.stem}"))

    return records


def backfill_source_mappings(
    data_dir: Path,
    source_records: list[dict[str, Any]],
    *,
    check: bool = False,
) -> list[BackfillResult]:
    records_by_id: dict[str, dict[str, Any]] = {}
    paths_by_id: dict[str, Path] = {}
    for path in pathway_files(data_dir):
        record = load_yaml_file(path)
        record_id = record.get("id")
        if isinstance(record_id, str):
            records_by_id[record_id] = record
            paths_by_id[record_id] = path

    pending = []
    for source_record in source_records:
        rows = _usable_source_mappings(source_record)
        if not rows:
            continue

        record_id = source_record["id"]
        if record_id not in records_by_id:
            raise BackfillError(f"{record_id}: no matching record in {data_dir}")

        target_record = records_by_id[record_id]
        _check_reactions(record_id, target_record, source_record)
        participant_ids = _ids(target_record, "participants")
        rows = [row for row in rows if row["object_id"] in participant_ids]
        if not rows:
            continue

        existing = _usable_source_mappings(target_record)
        merged = _sorted_mappings(unique_source_mappings([*existing, *rows]))
        added = len(merged) - len(_sorted_mappings(unique_source_mappings(existing)))
        if added <= 0:
            continue

        updated = dict(target_record, source_mappings=merged)
        validate_record(updated)
        records_by_id[record_id] = updated
        path = paths_by_id[record_id]
        new_text = _with_source_mappings(path.read_text(encoding="utf-8"), merged)
        pending.append(
            PendingBackfill(
                path=path,
                text=new_text,
                result=BackfillResult(path=path, record_id=record_id, added=added),
            )
        )

    if not check:
        for change in pending:
            change.path.write_text(change.text, encoding="utf-8")

    return [change.result for change in pending]


def _usable_source_mappings(record: dict[str, Any]) -> list[dict[str, str]]:
    rows = record.get("source_mappings") or []
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def _check_reactions(
    record_id: str,
    target_record: dict[str, Any],
    source_record: dict[str, Any],
) -> None:
    target_reactions = _ids(target_record, "reactions")
    source_reactions = _ids(source_record, "reactions")
    missing = sorted(target_reactions - source_reactions)
    if missing:
        raise BackfillError(
            f"{record_id}: raw source is missing {len(missing)} curated reactions: "
            + ", ".join(missing[:3])
        )


def _ids(record: dict[str, Any], slot: str) -> set[str]:
    values = record.get(slot) or []
    if not isinstance(values, list):
        return set()
    return {value["id"] for value in values if isinstance(value, dict) and "id" in value}


def _sorted_mappings(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(
        rows,
        key=lambda row: (
            row["source_pathway_id"],
            row["source_element_id"],
            row["subject_id"],
            row["predicate_id"],
            row["object_id"],
        ),
    )


def _with_source_mappings(text: str, source_mappings: list[dict[str, str]]) -> str:
    block = yaml.dump(
        {"source_mappings": source_mappings},
        allow_unicode=False,
        Dumper=IndentDumper,
        sort_keys=False,
    )
    source_bounds = _top_level_section(text, "source_mappings")
    if source_bounds:
        start, end = source_bounds
        return f"{text[:start]}{block}{text[end:]}"

    reference_bounds = _top_level_section(text, "references")
    if not reference_bounds:
        raise BackfillError("record text has no top-level references section")
    start, _ = reference_bounds
    return f"{text[:start]}{block}{text[start:]}"


def _top_level_section(text: str, key: str) -> tuple[int, int] | None:
    for match in TOP_LEVEL_KEY.finditer(text):
        if match.group(0) != f"{key}:":
            continue
        next_match = TOP_LEVEL_KEY.search(text, match.end())
        end = next_match.start() if next_match else len(text)
        return match.start(), end
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Backfill source_mappings from raw WikiPathways and Reactome XML.",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=ROOT / "data" / "pathways",
        help="directory containing curated PathwayMech YAML records",
    )
    parser.add_argument(
        "--chebi-obo",
        type=Path,
        help="ChEBI OBO file with chemical database xrefs for WikiPathways GPML",
    )
    parser.add_argument(
        "--wikipathways-gpml",
        nargs="*",
        type=Path,
        default=[],
        help="raw WikiPathways GPML files to replay",
    )
    parser.add_argument(
        "--reactome-biopax",
        nargs="*",
        type=Path,
        default=[],
        help="raw Reactome BioPAX Level 3 RDF/XML files to replay",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="check what would change without writing files",
    )
    args = parser.parse_args(argv)

    if args.wikipathways_gpml and not args.chebi_obo:
        print("--chebi-obo is required for --wikipathways-gpml", file=sys.stderr)
        return 2

    try:
        source_records = raw_source_records(
            wikipathways_gpml=args.wikipathways_gpml,
            reactome_biopax=args.reactome_biopax,
            chebi_obo=args.chebi_obo,
        )
        results = backfill_source_mappings(
            args.data_dir,
            source_records,
            check=args.check,
        )
    except (BackfillError, ElementTree.ParseError, OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    action = "would update" if args.check else "updated"
    for result in results:
        print(f"{action} {result.path}: +{result.added} source_mappings")
    print(f"{action} {len(results)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
