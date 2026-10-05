from __future__ import annotations

import argparse
import html
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any
from urllib.parse import quote
from xml.etree import ElementTree

import yaml

from pathwaymech.bigg import bigg_reactions, bigg_seed_rows, load_bigg_model
from pathwaymech.biopax import biopax_to_pathway_record, load_biopax
from pathwaymech.bvbrc import bvbrc_seed_rows, load_bvbrc_pathways
from pathwaymech.chebi import load_chebi_xrefs
from pathwaymech.dbcan import dbcan_pul_seed_rows, load_dbcan_pul
from pathwaymech.gapmind import gapmind_seed_rows, load_gapmind_steps
from pathwaymech.go import go_seed_rows, load_go_obo
from pathwaymech.gocam import gocam_to_pathway_record, load_gocam_model
from pathwaymech.identifiers import identifier_errors
from pathwaymech.kegg import kgml_to_pathway_record, load_kgml
from pathwaymech.kgx import write_kgx
from pathwaymech.mibig import (
    load_mibig_json,
    mibig_cluster,
    mibig_pathway_record,
    mibig_seed_rows,
)
from pathwaymech.modelseed import load_modelseed_tsv, modelseed_seed_rows
from pathwaymech.pathway_tools import (
    load_pathway_tools_dat,
    metacyc_pathway_records,
    pmn_pathway_records,
)
from pathwaymech.rhea import load_rhea_tsv, rhea_seed_rows
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.sources import (
    SourceInventoryError,
    load_source_inventory,
    source_seed_rows,
)
from pathwaymech.sssom import write_sssom
from pathwaymech.unipathway import load_unipathway_obo, unipathway_seed_rows
from pathwaymech.veupathdb import load_veupathdb_pathways, veupathdb_seed_rows
from pathwaymech.wikipathways import (
    gpml_to_pathway_record,
    load_gpml_pathway,
    wikipathways_fallback_id,
)
from pathwaymech.yaml_io import load_pathway_records, pathway_files

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


def check_identifiers_main(argv: list[str] | None = None, *, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(
        prog="pathwaymech-check-identifiers",
        description="Resolve pathway identifiers and asserted labels against authority snapshots.",
    )
    parser.add_argument("--config", type=Path, help="identifier policy (default: conf/)")
    args = parser.parse_args(argv)
    errors = identifier_errors(root, args.config)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    count = len(pathway_files(root / "data" / "pathways"))
    print(
        f"verified identifiers and label policies in {count} "
        "pathway records against authority snapshots"
    )
    return 0


def _validate_identifier_gate() -> int:
    return check_identifiers_main([], root=ROOT)


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


# Files under pages/ that are maintained by hand. Everything else there is
# rendered from the records, and the check refuses anything that is neither.
HAND_KEPT_PAGES = frozenset({"style.css", ".nojekyll"})


class SiteError(ValueError):
    """The records cannot be rendered to one unambiguous site."""


def render_site(records: list, source_paths: dict[str, str] | None = None) -> dict[str, str]:
    """Every file the renderer owns under pages/, keyed by its path there."""
    files: dict[str, str] = {}
    claimed: dict[str, str] = {}
    rows = []
    for record in records:
        slug = _slug(record.id)
        # Compared without case: on a case-insensitive filesystem two slugs that
        # differ only in case are one file, and one record would never publish.
        other = claimed.setdefault(slug.casefold(), record.id)
        if other != record.id:
            raise SiteError(
                f"{other} and {record.id} both render to pages/records/{slug}.html"
            )
        rows.append(
            f'<li><a href="records/{slug}.html"><strong>{html.escape(record.label)}</strong>'
            f"<span>{html.escape(record.id)} - "
            f"{len(record.mechanistic_edges)} mechanistic edges</span></a></li>"
        )
        files[f"records/{slug}.html"] = _record_page(record, (source_paths or {}).get(record.id))

    browse_body = "\n".join(rows) if rows else "<p>No curated pathway records yet.</p>"
    files["browse.html"] = _page(
        "PathwayMech records",
        _browse_controls() + f'<ul class="record-list" id="pathway-list">{browse_body}</ul>'
    )
    files["index.html"] = _page(
        "PathwayMech",
        "<p>Evidence-backed microbial pathway mechanism records.</p>"
        '<p><a href="browse.html">Browse pathways</a></p>',
    )
    return files


def _files_under(pages: Path) -> set[str]:
    if not pages.is_dir():
        return set()
    return {path.relative_to(pages).as_posix() for path in pages.rglob("*") if path.is_file()}


def _site_problems(pages: Path, expected: dict[str, str]) -> list[str]:
    """Every way pages/ differs from what the records render to."""
    problems = []
    for path, text in sorted(expected.items()):
        target = pages / path
        # Bytes, not text: reading with newline translation would turn a
        # rendered "\r\n" into "\n" and fail a page that was just written.
        if not target.is_file() or target.read_bytes() != text.encode("utf-8"):
            problems.append(f"pages/{path}: not what its record renders to")
    for path in sorted(_files_under(pages) - set(expected) - HAND_KEPT_PAGES):
        problems.append(f"pages/{path}: neither rendered from a record nor hand-kept")
    for path in sorted(HAND_KEPT_PAGES - _files_under(pages)):
        problems.append(f"pages/{path}: hand-kept file is missing")
    return problems


def render_pages_main(argv: list[str] | None = None, *, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(
        prog="pathwaymech-render-pages",
        description="Render pages/ from data/pathways, or check that it is current.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 if pages/ differs from what the records render to",
    )
    args = parser.parse_args(argv)

    records = load_pathway_records(root / "data" / "pathways")
    pages = root / "pages"
    try:
        source_paths = {
            yaml.safe_load(path.read_text())["id"]: path.relative_to(root).as_posix()
            for path in pathway_files(root / "data" / "pathways")
        }
        expected = render_site(records, source_paths)
    except SiteError as error:
        print(str(error), file=sys.stderr)
        return 1

    if args.check:
        problems = _site_problems(pages, expected)
        for line in problems:
            print(line, file=sys.stderr)
        if problems:
            print("pages/ is stale; run `just render-pages` and commit it", file=sys.stderr)
            return 1
        print(f"pages/ is current with {len(records)} pathway records")
        return 0

    # Rendered pages whose name no record produces any more -- a removed
    # record, or an id whose case changed -- are removed first, so that on a
    # case-insensitive filesystem the new name is written rather than kept
    # under the old one. Other unexpected files are left for the check to name.
    rendered = {path for path in _files_under(pages) if path.startswith("records/")}
    rendered |= {name for name in ("browse.html", "index.html") if (pages / name).is_file()}
    orphaned = sorted(path for path in rendered - set(expected) if path.endswith(".html"))
    for path in orphaned:
        (pages / path).unlink()
    (pages / "records").mkdir(parents=True, exist_ok=True)
    for path, text in expected.items():
        (pages / path).write_bytes(text.encode("utf-8"))
    print(f"rendered {len(records)} pathway records" + (
        f"; removed {len(orphaned)} orphaned page(s)" if orphaned else ""
    ))
    return 0


def check_pages_main(*, root: Path = ROOT) -> int:
    """The committed site is what the records render to."""
    return render_pages_main(["--check"], root=root)


def validate_strict_main(argv: list[str] | None = None, *, root: Path = ROOT) -> int:
    """Every record against the closed LinkML schema (src/pathwaymech/schema/)."""
    from pathwaymech.strict import strict_errors

    parser = argparse.ArgumentParser(
        prog="pathwaymech-validate-strict",
        description="Validate records against the closed LinkML schema.",
    )
    parser.add_argument("paths", nargs="*", type=Path, help="records (default: data/pathways)")
    args = parser.parse_args(argv)
    # The same list validate_main, the provenance check and the renderer read:
    # a record in a subdirectory must not escape the closed schema (#191).
    paths = [path.resolve() for path in args.paths] or [
        path.resolve() for path in pathway_files(root / "data" / "pathways")
    ]
    errors = strict_errors(paths, root.resolve())
    for line in errors:
        print(line, file=sys.stderr)
    if errors:
        return 1
    print(f"validated {len(paths)} records against the closed LinkML schema")
    return 0


def _validate_strict_gate() -> int:
    return validate_strict_main([])


def _validate_history_gate() -> int:
    """Every history/ record against the vendored HistoryRecord schema.

    The same script `just validate-history` runs, so the gate needs no task
    runner in CI.
    """
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_history.py")],
        cwd=ROOT,
        check=False,
    ).returncode


def export_kgx_main(argv: list[str] | None = None, *, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(
        prog="pathwaymech-export-kgx",
        description="Export data/pathways as KGX node and edge TSV files.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=root / "output" / "kgx",
        help="destination directory for nodes.tsv and edges.tsv",
    )
    args = parser.parse_args(argv)

    records = load_pathway_records(root / "data" / "pathways")
    nodes_path, edges_path = write_kgx(records, args.output_dir)
    print(f"wrote {nodes_path} and {edges_path} from {len(records)} pathway records")
    return 0


def export_sssom_main(argv: list[str] | None = None, *, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(
        prog="pathwaymech-export-sssom",
        description="Export retained source mappings as an SSSOM TSV file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=root / "output" / "sssom" / "source_mappings.sssom.tsv",
        help="destination SSSOM TSV path",
    )
    args = parser.parse_args(argv)

    records = load_pathway_records(root / "data" / "pathways")
    path = write_sssom(records, args.output)
    print(f"wrote {path} from {len(records)} pathway records")
    return 0


def run_qc_main() -> int:
    for check in [
        validate_main,
        _validate_strict_gate,
        _validate_identifier_gate,
        _validate_history_gate,
        check_provenance_main,
        validate_sources_main,
        check_docs_main,
        deep_research_contract_main,
        check_pages_main,
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
    parser.add_argument(
        "--chebi-obo",
        type=Path,
        help="optional ChEBI OBO file with chemical database xrefs",
    )
    args = parser.parse_args(argv)

    compound_mappings = load_chebi_xrefs(args.chebi_obo) if args.chebi_obo else {}
    records = []
    for path in args.paths:
        try:
            fallback_id = wikipathways_fallback_id(path)
            record = gpml_to_pathway_record(
                load_gpml_pathway(path),
                fallback_id,
                compound_mappings,
            )
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
    parser.add_argument(
        "--yaml",
        action="store_true",
        help="emit draft PathwayMech records instead of seed rows",
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

    if args.yaml:
        records = [mibig_pathway_record(cluster) for cluster in clusters]
        try:
            for record in records:
                validate_record(record)
        except ValidationError as error:
            for line in error.errors:
                print(line, file=sys.stderr)
            return 1
        print(yaml.safe_dump_all(records, sort_keys=False), end="")
    else:
        for row in mibig_seed_rows(clusters):
            print(row)
    return 0


def import_biopax_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert local BioPAX pathway files to PathwayMech YAML drafts.",
    )
    parser.add_argument("source_prefix", choices=["PANTHER", "PathBank", "Reactome"])
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


def import_panther_main(argv: list[str] | None = None) -> int:
    return import_biopax_main(["PANTHER", *(sys.argv[1:] if argv is None else argv)])


def import_metacyc_main(argv: list[str] | None = None) -> int:
    return _import_pathway_tools_main(
        argv,
        description="Convert local MetaCyc Pathway Tools pathways.dat files to drafts.",
        path_help="MetaCyc pathways.dat path",
        record_factory=metacyc_pathway_records,
    )


def import_pmn_main(argv: list[str] | None = None) -> int:
    return _import_pathway_tools_main(
        argv,
        description="Convert local PMN Pathway Tools pathways.dat files to drafts.",
        path_help="PMN pathways.dat path",
        record_factory=pmn_pathway_records,
    )


def _import_pathway_tools_main(
    argv: list[str] | None,
    *,
    description: str,
    path_help: str,
    record_factory: Callable[[list[dict[str, list[str]]]], list[dict[str, Any]]],
) -> int:
    parser = argparse.ArgumentParser(
        description=description,
    )
    parser.add_argument("paths", nargs="+", type=Path, help=path_help)
    args = parser.parse_args(argv)

    records = []
    for path in args.paths:
        try:
            path_records = record_factory(load_pathway_tools_dat(path))
            for record in path_records:
                validate_record(record)
            records.extend(path_records)
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
    parser.add_argument(
        "--chebi-obo",
        type=Path,
        help="optional ChEBI OBO file with chemical database xrefs",
    )
    args = parser.parse_args(argv)

    compound_mappings = load_chebi_xrefs(args.chebi_obo) if args.chebi_obo else {}
    records = []
    for path in args.paths:
        try:
            record = kgml_to_pathway_record(load_kgml(path), compound_mappings)
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


def import_gapmind_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract GapMind .steps rule elements for manual pathway triage.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="GapMind .steps path")
    args = parser.parse_args(argv)

    elements = []
    for path in args.paths:
        elements.extend(load_gapmind_steps(path))

    for row in gapmind_seed_rows(elements):
        print(row)
    return 0


def import_dbcan_pul_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract dbCAN-PUL workbook or TSV glycan-locus seed rows.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="dbCAN-PUL XLSX, TSV, or CSV")
    args = parser.parse_args(argv)

    records = []
    for path in args.paths:
        records.extend(load_dbcan_pul(path))

    for row in dbcan_pul_seed_rows(records):
        print(row)
    return 0


def import_unipathway_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract UniPathway UPA OBO crosswalk rows.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="UniPathway UPA OBO")
    args = parser.parse_args(argv)

    terms = []
    for path in args.paths:
        terms.extend(load_unipathway_obo(path))

    for row in unipathway_seed_rows(terms):
        print(row)
    return 0


def import_veupathdb_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract VEuPathDB WDK MetabolicPathways seed rows.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="VEuPathDB pathway TSV")
    args = parser.parse_args(argv)

    calls = []
    for path in args.paths:
        calls.extend(load_veupathdb_pathways(path))

    for row in veupathdb_seed_rows(calls):
        print(row)
    return 0


def _page(title: str, body: str, stylesheet_href: str = "style.css") -> str:
    site_root = html.escape(stylesheet_href.removesuffix("style.css"))
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{html.escape(stylesheet_href)}">
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <header><nav aria-label="Main navigation">
    <a href="{site_root}index.html">PathwayMech overview</a>
    <a href="{site_root}browse.html">Browse pathways</a>
    <a href="https://github.com/CultureBotAI/PathwayMech">Source</a>
    <a href="https://culturebotai.github.io/mechs/">All Mech projects</a>
  </nav></header>
  <main id="main-content" tabindex="-1">
    <h1>{html.escape(title)}</h1>
    {body}
  </main>
</body>
</html>
"""


def _browse_controls() -> str:
    return """<form id="pathway-search" hidden>
<label for="pathway-query">Search pathway name or identifier</label>
<input id="pathway-query" type="search"><button type="reset">Reset</button>
</form><p id="pathway-status" role="status" aria-live="polite"></p>
<p id="pathway-empty" hidden>No pathways match. Try another term or reset the search.</p>
<script>
document.addEventListener('DOMContentLoaded', function () {
  'use strict';
  const form = document.getElementById('pathway-search');
  const query = document.getElementById('pathway-query');
  const rows = Array.from(document.querySelectorAll('#pathway-list li'));
  function filter() {
    const term = query.value.trim().toLowerCase();
    let count = 0;
    rows.forEach(row => { row.hidden = !row.textContent.toLowerCase().includes(term);
      if (!row.hidden) count += 1; });
    document.getElementById('pathway-status').textContent =
      count + ' of ' + rows.length + ' pathways match';
    document.getElementById('pathway-empty').hidden = count !== 0;
  }
  query.addEventListener('input', filter);
  form.addEventListener('submit', event => { event.preventDefault(); filter(); });
  form.addEventListener('reset', event => {
    event.preventDefault(); query.value = ''; filter(); query.focus();
  });
  form.hidden = false;
  filter();
});
</script>"""


def _reference_url(identifier: str) -> str | None:
    """Resolve only citation namespaces with a known public source route."""
    prefix, _, local_id = identifier.partition(":")
    if prefix == "PMID" and local_id.isdigit():
        return f"https://pubmed.ncbi.nlm.nih.gov/{local_id}/"
    if prefix == "DOI" and local_id.startswith("10.") and "/" in local_id:
        return "https://doi.org/" + quote(local_id, safe="/")
    if prefix == "RHEA" and local_id.isdigit():
        return f"https://www.rhea-db.org/rhea/{local_id}"
    return None


def _record_page(record: object, source_path: str | None = None) -> str:
    """Publish the declared endpoints and evidence without interpreting them."""
    labels: dict[str, set[str]] = {}
    for field in ("taxa", "participants", "reactions", "gene_clusters"):
        for node in getattr(record, field, []):
            labels.setdefault(node["id"], set()).add(node.get("label") or node["id"])
    nodes = {identifier: next(iter(values)) if len(values) == 1 else identifier
             for identifier, values in labels.items()}
    components = []
    for field in ("taxa", "participants", "reactions"):
        for node in getattr(record, field, []):
            kind = node.get("category") or {"taxa": "taxon"}.get(field, field.removesuffix("s"))
            direction = node.get("direction", "")
            components.append(
                f"<tr><td>{html.escape(nodes[node['id']])}<br>"
                f"<code>{html.escape(node['id'])}</code></td>"
                f"<td>{html.escape(kind.replace('_', ' '))}</td>"
                f"<td>{html.escape(direction.replace('_', ' '))}</td></tr>"
            )
    component_section = (
        '<h2>Components and activities</h2><div class="table-scroll" role="region" '
        'tabindex="0" aria-label="Biological components and reaction directions">'
        "<table><caption>Declared biological components and source reaction directions</caption>"
        "<thead><tr><th scope=\"col\">Node</th><th scope=\"col\">Kind or role</th>"
        "<th scope=\"col\">Source direction</th></tr></thead>"
        f"<tbody>{''.join(components)}</tbody></table></div>"
    ) if components else ""

    def endpoint(identifier: str) -> str:
        label = nodes.get(identifier, identifier)
        return (f"{html.escape(label)}<br><code>{html.escape(identifier)}</code>"
                if label != identifier else f"<code>{html.escape(identifier)}</code>")

    references = getattr(record, "references", [])
    ref_anchors = {ref["id"]: f"reference-{number}" for number, ref in enumerate(references, 1)}
    rows = []
    for edge in record.mechanistic_edges:
        citations = []
        for evidence in edge.get("evidence", []):
            reference = html.escape(evidence["reference_id"])
            anchor = ref_anchors.get(evidence["reference_id"])
            citation = f'<a href="#{anchor}">{reference}</a>' if anchor else reference
            if "quote" in evidence:
                support = f"<blockquote>{html.escape(evidence['quote'])}</blockquote>"
            else:
                support = ("<p><strong>Source assertion:</strong> "
                           f"{html.escape(evidence['source_assertion'])}</p>")
            if evidence.get("source_locator"):
                support += ("<details><summary>Source location</summary><code>"
                            f"{html.escape(evidence['source_locator'])}</code></details>")
            citations.append(f"<li>{citation}{support}</li>")
        description = html.escape(edge.get("description", ""))
        rows.append(f"<tr><td>{endpoint(edge['subject'])}</td>"
                    f"<td>{html.escape(edge['predicate'])}<p>{description}</p></td>"
                    f"<td>{endpoint(edge['object'])}</td><td><ul>{''.join(citations)}</ul></td></tr>")
    edges = ('<div class="table-scroll" role="region" tabindex="0" '
             'aria-label="Mechanistic edges and evidence">'
             '<table><caption>Mechanistic edges and their cited evidence</caption><thead><tr>'
             '<th scope="col">Subject</th><th scope="col">Predicate and description</th>'
             '<th scope="col">Object</th><th scope="col">Evidence</th></tr></thead>'
             f"<tbody>{''.join(rows)}</tbody></table></div>")
    if not rows:
        edges = '<p>No mechanistic edges recorded.</p>'
    cited = []
    for ref in references:
        details = " — ".join(html.escape(ref[field])
                             for field in ("title", "citation") if ref.get(field))
        identifier = html.escape(ref["id"])
        source_url = ref.get("url") or _reference_url(ref["id"])
        if ref.get("source_version"):
            details += f" (source version: {html.escape(ref['source_version'])})"
        reference = (f'<a href="{html.escape(source_url)}">{identifier}</a>'
                     if source_url else identifier)
        cited.append(f'<li id="{ref_anchors[ref["id"]]}"><code>{reference}</code> {details}</li>')
    reference_section = f"<h2>References</h2><ul>{''.join(cited)}</ul>" if cited else ""
    provenance = (f'<p><a href="https://github.com/CultureBotAI/PathwayMech/blob/main/'
                  f'{quote(source_path, safe="/")}">Read the source YAML</a></p>'
                  if source_path else "")
    clusters = _gene_clusters(getattr(record, "gene_clusters", []))
    identifier = html.escape(getattr(record, "id", ""))
    return _page(
        record.label,
        f"<p><code>{identifier}</code></p><p>{html.escape(record.description)}</p>"
        f"{provenance}{component_section}<h2>Mechanistic edges</h2>"
        f"{edges}{clusters}{reference_section}",
        stylesheet_href="../style.css",
    )


def _gene_clusters(clusters: list[dict[str, object]]) -> str:
    if not clusters:
        return ""

    rendered = []
    for cluster in clusters:
        detail_items = []
        for label, key in [
            ("Products", "products"),
            ("Classes", "biosynthetic_classes"),
        ]:
            values = cluster.get(key)
            if isinstance(values, list) and values:
                detail_items.append(f"{label}: {html.escape(', '.join(map(str, values)))}")

        loci = cluster.get("loci")
        if isinstance(loci, list) and loci:
            accessions = [
                str(locus.get("accession"))
                for locus in loci
                if isinstance(locus, dict) and locus.get("accession")
            ]
            if accessions:
                detail_items.append(f"Loci: {html.escape(', '.join(accessions))}")

        genes = cluster.get("genes")
        if isinstance(genes, list) and genes:
            gene_count = sum(isinstance(gene, dict) for gene in genes)
            detail_items.append(f"Genes: {gene_count}")

        details = "".join(f"<li>{item}</li>" for item in detail_items)
        rendered.append(
            "<li>"
            f"<strong>{html.escape(str(cluster['label']))}</strong>"
            f"<span>{html.escape(str(cluster['id']))}</span>"
            f"<ul>{details}</ul>"
            "</li>"
        )
    return f"<h2>Biosynthetic gene clusters</h2><ul>{''.join(rendered)}</ul>"


def _slug(identifier: str) -> str:
    return identifier.replace(":", "_").replace("/", "_")
