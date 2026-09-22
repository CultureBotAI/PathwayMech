from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path
from xml.etree import ElementTree

import yaml

from pathwaymech.bigg import bigg_reactions, bigg_seed_rows, load_bigg_model
from pathwaymech.biopax import biopax_to_pathway_record, load_biopax
from pathwaymech.bvbrc import bvbrc_seed_rows, load_bvbrc_pathways
from pathwaymech.go import go_seed_rows, load_go_obo
from pathwaymech.gocam import gocam_to_pathway_record, load_gocam_model
from pathwaymech.kegg import kgml_to_pathway_record, load_kgml
from pathwaymech.metacyc import load_metacyc_dat, metacyc_pathway_records
from pathwaymech.mibig import load_mibig_json, mibig_cluster, mibig_seed_rows
from pathwaymech.modelseed import load_modelseed_tsv, modelseed_seed_rows
from pathwaymech.rhea import load_rhea_tsv, rhea_seed_rows
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.sources import (
    SourceInventoryError,
    load_source_inventory,
    source_seed_rows,
)
from pathwaymech.wikipathways import gpml_to_pathway_record, load_gpml_pathway
from pathwaymech.yaml_io import load_pathway_records

ROOT = Path(__file__).resolve().parents[2]


def validate_main() -> int:
    try:
        records = load_pathway_records(ROOT / "data" / "pathways")
    except ValidationError as error:
        for line in error.errors:
            print(line, file=sys.stderr)
        return 1
    print(f"validated {len(records)} pathway records")
    return 0


def check_provenance_main() -> int:
    records = load_pathway_records(ROOT / "data" / "pathways")
    evidence_count = sum(
        len(edge["evidence"]) for record in records for edge in record.mechanistic_edges
    )
    print(f"checked {evidence_count} evidence blocks")
    return 0


def check_docs_main() -> int:
    required = [
        ROOT / "README.md",
        ROOT / "CLAUDE.md",
        ROOT / "docs" / "CURATION.md",
        ROOT / "docs" / "DEEP_RESEARCH_PROVIDERS.md",
        ROOT / "docs" / "HARMONIZATION.md",
        ROOT / "docs" / "MERGE_QUEUE.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        for path in missing:
            print(f"missing required doc: {path}", file=sys.stderr)
        return 1
    print(f"checked {len(required)} documentation files")
    return 0


def validate_sources_main() -> int:
    try:
        sources = load_source_inventory(ROOT / "conf" / "sources.yaml")
    except SourceInventoryError as error:
        for line in error.errors:
            print(line, file=sys.stderr)
        return 1
    print(f"validated {len(sources)} source records")
    return 0


def deep_research_contract_main() -> int:
    required_headings = [
        "## Pathway scope",
        "## Mechanistic summary",
        "## Evidence table",
        "## Gaps",
    ]
    failures: list[str] = []
    for path in sorted((ROOT / "research").glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        missing = [heading for heading in required_headings if heading not in text]
        for heading in missing:
            failures.append(f"{path.relative_to(ROOT)} missing {heading}")
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print("checked deep-research report contract")
    return 0


def render_pages_main() -> int:
    records = load_pathway_records(ROOT / "data" / "pathways")
    pages = ROOT / "pages"
    records_dir = pages / "records"
    records_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for record in records:
        slug = _slug(record.id)
        rows.append(
            f'<li><a href="records/{slug}.html"><strong>{html.escape(record.label)}</strong>'
            f"<span>{html.escape(record.id)} - "
            f"{len(record.mechanistic_edges)} mechanistic edges</span></a></li>"
        )
        (records_dir / f"{slug}.html").write_text(_record_page(record), encoding="utf-8")

    browse_body = "\n".join(rows) if rows else "<p>No curated pathway records yet.</p>"
    (pages / "browse.html").write_text(
        _page("PathwayMech records", f'<ul class="record-list">{browse_body}</ul>'),
        encoding="utf-8",
    )
    (pages / "index.html").write_text(
        _page(
            "PathwayMech",
            "<p>Evidence-backed microbial pathway mechanism records.</p>"
            '<p><a href="browse.html">Browse pathways</a></p>',
        ),
        encoding="utf-8",
    )
    print(f"rendered {len(records)} pathway records")
    return 0


def run_qc_main() -> int:
    for check in [
        validate_main,
        check_provenance_main,
        validate_sources_main,
        check_docs_main,
        deep_research_contract_main,
    ]:
        exit_code = check()
        if exit_code:
            return exit_code
    return 0


def seed_from_sources_main() -> int:
    try:
        sources = load_source_inventory(ROOT / "conf" / "sources.yaml")
    except SourceInventoryError as error:
        for line in error.errors:
            print(line, file=sys.stderr)
        return 1

    for row in source_seed_rows(sources):
        print(row)
    return 0


def import_gocam_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert local GO-CAM JSON models to PathwayMech YAML drafts.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="GO-CAM JSON model path")
    args = parser.parse_args(argv)

    records = []
    for path in args.paths:
        try:
            record = gocam_to_pathway_record(load_gocam_model(path))
            validate_record(record)
            records.append(record)
        except (ValidationError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    print(yaml.safe_dump_all(records, sort_keys=False), end="")
    return 0


def import_wikipathways_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert local WikiPathways GPML files to PathwayMech YAML drafts.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="GPML pathway path")
    args = parser.parse_args(argv)

    records = []
    for path in args.paths:
        try:
            fallback_id = f"WikiPathways:{path.stem}"
            record = gpml_to_pathway_record(load_gpml_pathway(path), fallback_id)
            validate_record(record)
            records.append(record)
        except (ElementTree.ParseError, ValidationError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    print(yaml.safe_dump_all(records, sort_keys=False), end="")
    return 0


def import_rhea_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract Rhea TSV reaction crosswalk rows for PathwayMech imports.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Rhea TSV path")
    args = parser.parse_args(argv)

    reactions = []
    for path in args.paths:
        try:
            reactions.extend(load_rhea_tsv(path))
        except ValueError as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    for row in rhea_seed_rows(reactions):
        print(row)
    return 0


def import_mibig_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract MIBiG JSON biosynthetic gene cluster seed rows.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="MIBiG JSON path")
    args = parser.parse_args(argv)

    clusters = []
    for path in args.paths:
        try:
            clusters.append(mibig_cluster(load_mibig_json(path)))
        except ValueError as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    for row in mibig_seed_rows(clusters):
        print(row)
    return 0


def import_biopax_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert local BioPAX pathway files to PathwayMech YAML drafts.",
    )
    parser.add_argument("source_prefix", choices=["PathBank", "Reactome"])
    parser.add_argument("paths", nargs="+", type=Path, help="BioPAX RDF/XML path")
    args = parser.parse_args(argv)

    records = []
    for path in args.paths:
        try:
            fallback_id = f"{args.source_prefix}:{path.stem}"
            record = biopax_to_pathway_record(load_biopax(path), fallback_id)
            validate_record(record)
            records.append(record)
        except (ElementTree.ParseError, ValidationError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    print(yaml.safe_dump_all(records, sort_keys=False), end="")
    return 0


def import_metacyc_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert local MetaCyc Pathway Tools pathways.dat files to drafts.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="MetaCyc pathways.dat path")
    args = parser.parse_args(argv)

    records = []
    for path in args.paths:
        try:
            records.extend(metacyc_pathway_records(load_metacyc_dat(path)))
            for record in records:
                validate_record(record)
        except (ValidationError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    print(yaml.safe_dump_all(records, sort_keys=False), end="")
    return 0


def import_kegg_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert local KEGG KGML files to PathwayMech YAML drafts.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="KEGG KGML path")
    args = parser.parse_args(argv)

    records = []
    for path in args.paths:
        try:
            record = kgml_to_pathway_record(load_kgml(path))
            validate_record(record)
            records.append(record)
        except (ElementTree.ParseError, ValidationError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    print(yaml.safe_dump_all(records, sort_keys=False), end="")
    return 0


def import_go_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract GO OBO term seed rows for PathwayMech grounding.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="GO OBO path")
    args = parser.parse_args(argv)

    terms = []
    for path in args.paths:
        terms.extend(load_go_obo(path))

    for row in go_seed_rows(terms):
        print(row)
    return 0


def import_modelseed_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extract ModelSEED reaction TSV rows.")
    parser.add_argument("paths", nargs="+", type=Path, help="ModelSEED reactions TSV")
    args = parser.parse_args(argv)

    reactions = []
    for path in args.paths:
        reactions.extend(load_modelseed_tsv(path))

    for row in modelseed_seed_rows(reactions):
        print(row)
    return 0


def import_bigg_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extract BiGG model reaction rows.")
    parser.add_argument("paths", nargs="+", type=Path, help="BiGG model JSON")
    args = parser.parse_args(argv)

    reactions = []
    for path in args.paths:
        reactions.extend(bigg_reactions(load_bigg_model(path)))

    for row in bigg_seed_rows(reactions):
        print(row)
    return 0


def import_bvbrc_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extract BV-BRC pathway call rows.")
    parser.add_argument("paths", nargs="+", type=Path, help="BV-BRC pathway TSV")
    args = parser.parse_args(argv)

    calls = []
    for path in args.paths:
        calls.extend(load_bvbrc_pathways(path))

    for row in bvbrc_seed_rows(calls):
        print(row)
    return 0


def _page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    <h1>{html.escape(title)}</h1>
    {body}
  </main>
</body>
</html>
"""


def _record_page(record: object) -> str:
    title = html.escape(record.label)
    edges = "\n".join(
        "<li>"
        f"{html.escape(edge['subject'])} "
        f"{html.escape(edge['predicate'])} "
        f"{html.escape(edge['object'])}"
        "</li>"
        for edge in record.mechanistic_edges
    )
    return _page(title, f"<p>{html.escape(record.description)}</p><ul>{edges}</ul>")


def _slug(identifier: str) -> str:
    return identifier.replace(":", "_").replace("/", "_")
