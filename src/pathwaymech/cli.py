from __future__ import annotations

import argparse
import functools
import hashlib
import html
import json
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode, urlsplit
from xml.etree import ElementTree

import yaml

from pathwaymech.bigg import bigg_reactions, bigg_seed_rows, load_bigg_model
from pathwaymech.biopax import biopax_to_pathway_record
from pathwaymech.brenda import brenda_seed_rows, load_brenda_role_bundle
from pathwaymech.bvbrc import bvbrc_seed_rows, load_bvbrc_pathways
from pathwaymech.chebi import load_chebi_xrefs
from pathwaymech.cross_mech import pathway_index_json
from pathwaymech.dbcan import dbcan_pul_seed_rows, load_dbcan_pul
from pathwaymech.dram import dram_seed_rows, load_dram_module_steps
from pathwaymech.gapmind import gapmind_seed_rows, load_gapmind_steps
from pathwaymech.go import go_seed_rows, load_go_obo
from pathwaymech.gocam import gocam_to_pathway_record, load_gocam_model
from pathwaymech.graph_view import graph_html
from pathwaymech.hadeg import hadeg_seed_rows, load_hadeg_memberships
from pathwaymech.identifiers import identifier_errors
from pathwaymech.kegg import kgml_to_pathway_record, load_kgml
from pathwaymech.kgx import render_kgx, write_kgx
from pathwaymech.mechanism_view import mechanism_anchor, mechanism_views
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
from pathwaymech.reaction_mechanisms import iter_mechanism_evidence
from pathwaymech.rhea import load_rhea_tsv, rhea_seed_rows
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.seed_subsystems import load_seed_subsystem_bundle, seed_subsystem_rows
from pathwaymech.site_display import (
    autolink_html,
    corpus_as_of,
    evidence_html,
    history_html,
    label_html,
    load_site_history,
    plain_label,
    record_kind,
    record_metadata,
    rich_text_html,
)
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
ASSETS = Path(__file__).parent / "assets"
SCHEMA_PATH = Path(__file__).parent / "schema" / "pathwaymech.yaml"
GITHUB_REPO = "https://github.com/CultureBotAI/PathwayMech"
GITHUB_BLOB = f"{GITHUB_REPO}/blob/main"
# Where GitHub Pages serves pages/. Only the not-found page needs it: it is
# served at whatever address was missing, so its links cannot be relative.
SITE_URL = "https://culturebotai.github.io/PathwayMech/pages/"


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
        len(edge["evidence"]) + sum(
            len(qualifier["evidence"]) for qualifier in edge.get("endpoint_qualifiers", [])
        )
        for record in records for edge in record.mechanistic_edges
    )
    evidence_count += sum(
        1 for record in records for _ in iter_mechanism_evidence(record.reaction_mechanisms)
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


def _record_facets(record: object) -> tuple[str, list[str], list[str]]:
    # The record's own pathway_type, which its page shows as "Pathway type".
    # record_kind() is an edge-count summary, not a class to filter by.
    kind = getattr(record, "pathway_type", "") or ""
    taxa = sorted({
        (taxon.get("label") or taxon["id"]).strip()
        for taxon in getattr(record, "taxa", [])
        if (taxon.get("label") or taxon.get("id"))
    })
    grounding: list[str] = []
    has_protein = any(
        str(p.get("id", "")).startswith("UniProtKB:")
        or p.get("category") in {"protein", "gene_product"}
        for p in getattr(record, "participants", [])
    )
    if has_protein:
        grounding.append("protein-grounded")
    if getattr(record, "reaction_mechanisms", []):
        grounding.append("reaction-mechanisms")
    if getattr(record, "gene_clusters", []):
        grounding.append("gene-clusters")
    if getattr(record, "mechanistic_edges", []):
        grounding.append("curated-edges")
    return kind, taxa, grounding


def _by_count(counts: dict[str, int]) -> list[tuple[str, int]]:
    """Facet values, most frequent first, then by name."""
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0].casefold()))


def _corpus_note(records: list, sessions: list[list[dict]]) -> str:
    """The dated corpus version every page footer states."""
    count = f"{len(records):,} pathway record{'' if len(records) == 1 else 's'}"
    as_of = corpus_as_of(records, sessions)
    return f"Corpus as of {as_of} · {count}" if as_of else count


def _map_urls(payload: dict[str, Any]) -> set[str]:
    """Every record page an embedding map's points open."""
    urls = set()
    for item in (*payload.get("points", []), *payload.get("pathways", []),
                 *payload.get("proteins", [])):
        urls.update(url for url in (item.get("url"), *item.get("pathway_urls", [])) if url)
    return urls


def render_site(records: list, source_paths: dict[str, str] | None = None,
                histories: dict[str, list[dict]] | None = None,
                *, root: Path = ROOT) -> dict[str, str]:
    """Every file the renderer owns under pages/, keyed by its path there."""
    files: dict[str, str] = {}
    claimed: dict[str, str] = {}
    rows = []
    type_counts: dict[str, int] = {}
    taxon_counts: dict[str, int] = {}
    grounding_counts: dict[str, int] = {}
    # A record page links another published record by this path, relative to
    # records/, rather than sending the reader to the identifier's authority.
    own_pages = {record.id: f"{_slug(record.id)}.html" for record in records}
    sessions = {record.id: (histories or {}).get((source_paths or {}).get(record.id), [])
                for record in records}
    note = _corpus_note(records, list(sessions.values()))
    for record in sorted(records, key=lambda r: (plain_label(r.label).casefold(), r.id)):
        slug = _slug(record.id)
        # Compared without case: on a case-insensitive filesystem two slugs that
        # differ only in case are one file, and one record would never publish.
        other = claimed.setdefault(slug.casefold(), record.id)
        if other != record.id:
            raise SiteError(
                f"{other} and {record.id} both render to pages/records/{slug}.html"
            )
        kind, taxa, grounding = _record_facets(record)
        if kind:
            type_counts[kind] = type_counts.get(kind, 0) + 1
        for t in taxa:
            taxon_counts[t] = taxon_counts.get(t, 0) + 1
        for g in grounding:
            grounding_counts[g] = grounding_counts.get(g, 0) + 1
        search = html.escape(f"{plain_label(record.label)} {record.id}", quote=True)
        label_attr = html.escape(plain_label(record.label).casefold(), quote=True)
        id_attr = html.escape(record.id, quote=True)
        edge_count = len(getattr(record, "mechanistic_edges", []))
        type_attr = html.escape(kind, quote=True)
        taxa_attr = html.escape("|".join(taxa), quote=True)
        grounding_attr = html.escape("|".join(grounding), quote=True)
        type_text = f"{html.escape(kind.replace('-', ' '))} · " if kind else ""
        rows.append(
            f'<li data-search="{search}" data-label="{label_attr}" data-id="{id_attr}" '
            f'data-edges="{edge_count}" data-type="{type_attr}" '
            f'data-taxa="{taxa_attr}" data-grounding="{grounding_attr}">'
            f'<a href="records/{slug}.html">'
            f'<strong>{label_html(record.label)}</strong>'
            f"<span>{html.escape(record.id)} — {type_text}{record_kind(record)}</span></a></li>"
        )
        source_path = (source_paths or {}).get(record.id)
        files[f"records/{slug}.html"] = _record_page(
            record, source_path, sessions[record.id], own_pages=own_pages, corpus_note=note,
        )

    browse_body = "\n".join(rows) if rows else "<p>No curated pathway records yet.</p>"
    files["browse.html"] = _page(
        "PathwayMech records",
        '<nav class="breadcrumb" aria-label="Breadcrumb">'
        '<a href="index.html">PathwayMech</a> <span aria-hidden="true">/</span> '
        '<span aria-current="page">Browse pathways</span></nav>'
        '<div class="browse-layout">'
        + _browse_controls(_by_count(type_counts), _by_count(taxon_counts), grounding_counts)
        + '<div class="browse-results">'
        + f'<ul class="record-list" id="pathway-list">{browse_body}</ul>'
        + "</div></div>",
        corpus_note=note,
    )
    corpus_map = _load_or_fallback_corpus_map(records, root)
    sequence_map = _load_or_fallback_sequence_map(records, root)
    for url in sorted(_map_urls(corpus_map) | _map_urls(sequence_map)):
        if url not in files:
            raise SiteError(f"an embedding map links pages/{url}, which no record renders")
    files["map.html"] = _map_page(records, root=root, payload=corpus_map, corpus_note=note)
    files["sequence-map.html"] = _sequence_map_page(
        records, root=root, payload=sequence_map, corpus_note=note,
    )
    files["schema.html"] = _schema_page(corpus_note=note)
    files["404.html"] = _not_found_page(root, record_count=len(records), corpus_note=note)
    exports = render_kgx(records)
    fingerprint = hashlib.sha256("".join(exports.values()).encode()).hexdigest()
    for name, text in exports.items():
        files[f"downloads/{name}"] = text
    manifest = {
        "format": "KGX TSV", "pathway_records": len(records),
        "version": "sha256:" + fingerprint,
        "data_license": "CC-BY-4.0", "third_party_terms": "Upstream source terms still apply.",
        "files": {name: {"sha256": hashlib.sha256(text.encode()).hexdigest(),
                          "rows": len(text.splitlines()) - 1}
                  for name, text in exports.items()},
    }
    files["downloads/manifest.json"] = json.dumps(manifest, indent=2) + "\n"
    files["index.html"] = _home_page(records, fingerprint, corpus_note=note)
    files["pathway_index.json"] = pathway_index_json(records)
    for name in ("pathway-network.css", "pathway-network.js", "theme.js"):
        files[f"assets/{name}"] = (ASSETS / name).read_text()
    return files


def _home_page(records: list, version: str = "", *, corpus_note: str = "") -> str:
    """Describe the same published records that populate the pathway browser."""
    metrics = [
        (len(records), "Pathway records"),
        (len({taxon["id"] for record in records for taxon in record.taxa}), "Taxa represented"),
        (sum(len(record.mechanistic_edges) for record in records), "Mechanistic edges"),
        (len({ref["id"] for record in records for ref in record.references}),
         "Distinct references"),
    ]
    statistics = "".join(
        f'<div class="home-stat"><dt>{label}</dt><dd>{count:,}</dd></div>'
        for count, label in metrics
    )
    gh_repo = GITHUB_REPO
    gh_blob = GITHUB_BLOB
    dated = f" {html.escape(corpus_note)}." if corpus_note else ""
    body = f"""<section class="home-hero" aria-labelledby="home-title">
      <p class="home-eyebrow">Microbial pathway knowledge base</p>
      <h1 id="home-title">PathwayMech</h1>
      <p class="home-tagline">Explore microbial pathways, their molecular participants,
        and the evidence behind their mechanistic connections.</p>
      <form class="hero-search" action="browse.html" method="get" role="search">
        <label class="visually-hidden" for="hero-search-input">\
Search pathways by name, organism, or identifier</label>
        <input id="hero-search-input" name="q" type="search"
               placeholder="Search {len(records):,} pathways by name, organism, \
reaction, or ID (e.g. methanogenesis, MetaCyc)...">
        <button type="submit">Search pathways</button>
      </form>
      <div class="home-actions">
        <a class="home-button" href="browse.html">Browse pathways
          <span aria-hidden="true">→</span></a>
        <a class="home-button home-button-secondary" href="map.html">Text embedding map</a>
        <a class="home-button home-button-secondary" \
href="sequence-map.html">Sequence map (ESM-2 pLM)</a>
        <a class="home-button home-button-secondary"
           href="{gh_repo}">View on GitHub</a>
      </div>
      <dl class="home-stats" aria-label="Published pathway collection">{statistics}</dl>
    </section>
    <section class="home-explore" aria-labelledby="explore-title">
      <h2 id="explore-title">Explore PathwayMech</h2>
      <p class="home-section-intro">Find a pathway, explore embedding spaces, \
follow its evidence, or contribute a record.</p>
      <div class="home-cards">
        <article class="home-card">
          <h3>Pathway browser</h3>
          <p>Filter and search the published collection by pathway type, \
organism, protein grounding, or identifier.</p>
          <a href="browse.html">Browse pathway records <span aria-hidden="true">→</span></a>
        </article>
        <article class="home-card">
          <h3>Corpus text embedding map</h3>
          <p>Interactive 2D PaCMAP projection of BAAI/bge-large-en-v1.5 \
embeddings across all {len(records):,} pathway records.</p>
          <a href="map.html">Explore text embedding map <span aria-hidden="true">→</span></a>
        </article>
        <article class="home-card">
          <h3>Sequence map (ESM-2 pLM)</h3>
          <p>Explore protein language model (ESM-2 650M) representations for \
UniProt-grounded pathway proteins and centroids.</p>
          <a href="sequence-map.html">Explore pLM sequence map <span aria-hidden="true">→</span></a>
        </article>
        <article class="home-card">
          <h3>Source records &amp; curation</h3>
          <p>Inspect the underlying YAML records and learn how to attach \
mechanistic evidence to individual pathway edges.</p>
          <a href="{gh_repo}/tree/main/data/pathways">
            Explore source records <span aria-hidden="true">→</span></a>
        </article>
      </div>
    </section>
    <section aria-labelledby="downloads-title">
      <h2 id="downloads-title">Downloads, schema &amp; complete pathway graph</h2>
      <p>KGX TSV exports from the same {len(records):,} pathway records shown here:
        <a href="downloads/nodes.tsv" download>All nodes (TSV)</a>,
        <a href="downloads/edges.tsv" download>All edges (TSV)</a>,
        <a href="pathway_index.json" download>Pathway index (JSON)</a>, and
        <a href="downloads/manifest.json">Version, row counts and file checksums</a>.</p>
      <p><strong>LinkML Schema &amp; Data Model:</strong>
        <a href="schema.html">Schema reference (every class, slot and enumeration, \
generated from the schema)</a> ·
        <a href="{gh_blob}/src/pathwaymech/schema/pathwaymech.yaml">\
PathwayMech LinkML schema (<code>pathwaymech.yaml</code>)</a> ·
        <a href="{gh_blob}/src/pathwaymech/schema/mech_shared.yaml">\
Shared X-Mech primitives (<code>mech_shared.yaml</code>)</a> ·
        <a href="{gh_blob}/src/pathwaymech/schema/history.yaml">\
Curation history schema (<code>history.yaml</code>)</a> ·
        <a href="{gh_blob}/conf/sources.yaml">\
Source authority registry (<code>sources.yaml</code>)</a> ·
        <a href="{gh_blob}/data/embeddings/corpus_map.json">\
Corpus text embedding coordinates (JSON)</a> ·
        <a href="{gh_blob}/data/embeddings/sequence_map.json">\
ESM-2 sequence embedding coordinates (JSON)</a>.</p>
      <p>Graph version: <code>{version or "See download manifest"}</code>.{dated}
        Project data: <a href="{gh_blob}/LICENSE-DATA">CC BY 4.0</a>.
        Code: <a href="{gh_blob}/LICENSE-CODE">BSD-3-Clause</a>.
        Third-party source material keeps its own terms
        (<a href="{gh_blob}/LICENSE">licence scope</a>).</p>
    </section>"""
    return _page("PathwayMech", body, homepage=True, corpus_note=corpus_note)


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
        expected = render_site(records, source_paths, load_site_history(root), root=root)
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
    rendered |= {
        name for name in ("browse.html", "index.html", "map.html", "sequence-map.html",
                          "schema.html", "404.html")
        if (pages / name).is_file()
    }
    orphaned = sorted(path for path in rendered - set(expected) if path.endswith(".html"))
    for path in orphaned:
        (pages / path).unlink()
    (pages / "records").mkdir(parents=True, exist_ok=True)
    for path, text in expected.items():
        (pages / path).parent.mkdir(parents=True, exist_ok=True)
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


def cross_mech_proteins_main(argv: list[str] | None = None, *, root: Path = ROOT) -> int:
    from pathwaymech.cross_mech import main

    return main(argv, root)


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
        try:
            records = [mibig_pathway_record(cluster) for cluster in clusters]
            for record in records:
                validate_record(record)
        except ValidationError as error:
            for line in error.errors:
                print(line, file=sys.stderr)
            return 1
        except ValueError as error:
            print(error, file=sys.stderr)
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
    parser.add_argument("--sha256", help="expected SHA-256 of the single local input")
    parser.add_argument("--source-url", help="source download URL for a single pinned input")
    parser.add_argument(
        "--source-version", help="release and archive member for a single pinned input",
    )
    args = parser.parse_args(argv)
    if (args.sha256 is not None or args.source_url or args.source_version) and len(args.paths) != 1:
        parser.error("source provenance options require exactly one input file")
    if (args.source_url or args.source_version) and not args.sha256:
        parser.error("--source-url and --source-version require --sha256")
    if args.source_url:
        try:
            parsed = urlsplit(args.source_url)
        except ValueError:
            parser.error("--source-url must be a valid absolute HTTP(S) URL")
        if (parsed.scheme not in {"http", "https"} or not parsed.netloc
                or any(char.isspace() for char in args.source_url)):
            parser.error("--source-url must be an absolute HTTP(S) URL without whitespace")

    records = []
    for path in args.paths:
        try:
            fallback_id = f"{args.source_prefix}:{path.stem}"
            payload = path.read_bytes()
            digest = hashlib.sha256(payload).hexdigest()
            if args.sha256 is not None:
                if not re.fullmatch(r"[0-9a-fA-F]{64}", args.sha256):
                    raise ValueError("--sha256 must contain exactly 64 hexadecimal characters")
                if digest != args.sha256.lower():
                    raise ValueError(
                        f"SHA-256 mismatch: expected {args.sha256.lower()}, got {digest}"
                    )
            record = biopax_to_pathway_record(ElementTree.fromstring(payload), fallback_id)
            reference = next(ref for ref in record["references"] if ref["id"] == record["id"])
            reference["source_sha256"] = digest
            if args.source_url:
                reference["url"] = args.source_url
            if args.source_version:
                reference["source_version"] = args.source_version
            validate_record(record)
            records.append(record)
        except (OSError, ElementTree.ParseError, ValidationError, ValueError) as error:
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


def import_hadeg_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract source-reported memberships from a pinned local HADEG CSV.",
    )
    parser.add_argument("path", type=Path, help="local Tables/7_All_pathways.csv")
    parser.add_argument("--source-commit", required=True, help="full upstream Git commit")
    parser.add_argument("--sha256", required=True, help="expected SHA-256 of the input bytes")
    args = parser.parse_args(argv)
    try:
        memberships = load_hadeg_memberships(
            args.path, source_commit=args.source_commit, expected_sha256=args.sha256,
        )
        output = "\n".join(hadeg_seed_rows(memberships))
    except (OSError, ValueError) as error:
        print(f"{args.path}: {error}", file=sys.stderr)
        return 1
    print(output)
    return 0


def import_dram_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract native module-step support rows from a pinned local DRAM1 table.",
    )
    parser.add_argument("path", type=Path, help="local data/module_step_form.tsv")
    parser.add_argument("--source-commit", required=True, help="full upstream Git commit")
    parser.add_argument("--sha256", required=True, help="expected SHA-256 of the input bytes")
    args = parser.parse_args(argv)
    try:
        records = load_dram_module_steps(
            args.path, source_commit=args.source_commit, expected_sha256=args.sha256,
        )
        output = "\n".join(dram_seed_rows(records))
    except (OSError, ValueError) as error:
        print(f"{args.path}: {error}", file=sys.stderr)
        return 1
    print(output)
    return 0


def import_seed_subsystems_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract native SEED subsystem support rows from a pinned local API bundle.",
    )
    parser.add_argument(
        "manifest", type=Path, help="local subsystem request/response manifest JSON",
    )
    args = parser.parse_args(argv)
    try:
        bundle = load_seed_subsystem_bundle(args.manifest)
        output = "\n".join(seed_subsystem_rows(bundle))
    except (OSError, ValueError) as error:
        print(f"{args.manifest}: {error}", file=sys.stderr)
        return 1
    print(output)
    return 0


def import_brenda_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract support rows from a pinned local BRENDA reaction-role query bundle.",
    )
    parser.add_argument("manifest", type=Path, help="local role-import manifest JSON")
    args = parser.parse_args(argv)
    try:
        bundle = load_brenda_role_bundle(args.manifest)
        output = "\n".join(brenda_seed_rows(bundle))
    except (OSError, ValueError) as error:
        print(f"{args.manifest}: {error}", file=sys.stderr)
        return 1
    print(output)
    return 0


def import_pmn_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert local PMN Pathway Tools pathways.dat files to drafts.",
    )
    parser.add_argument("paths", nargs="+", type=Path, help="PMN pathways.dat path")
    parser.add_argument("--pgdb", required=True, help="native PGDB identifier (e.g. Chlamy)")
    parser.add_argument("--source-version", help="version of the supplied PGDB export")
    parser.add_argument(
        "--pathway-id", action="append", help="select an exact native frame; repeatable"
    )
    parser.add_argument("--encoding", choices=["utf-8", "latin-1"], default="utf-8")
    args = parser.parse_args(argv)
    return _convert_pathway_tools_files(
        args.paths,
        lambda records: pmn_pathway_records(
            records, pgdb=args.pgdb, source_version=args.source_version
        ),
        selected_ids=args.pathway_id, encoding=args.encoding,
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
    parser.add_argument(
        "--pathway-id", action="append", help="select an exact native frame; repeatable"
    )
    parser.add_argument("--encoding", choices=["utf-8", "latin-1"], default="utf-8")
    args = parser.parse_args(argv)
    return _convert_pathway_tools_files(
        args.paths, record_factory, selected_ids=args.pathway_id, encoding=args.encoding
    )


def _convert_pathway_tools_files(
    paths: list[Path],
    record_factory: Callable[[list[dict[str, list[str]]]], list[dict[str, Any]]],
    *,
    selected_ids: list[str] | None = None,
    encoding: str = "utf-8",
) -> int:
    records = []
    seen_ids: set[str] = set()
    requested = set(selected_ids or [])
    found: set[str] = set()
    for path in paths:
        try:
            native_records = load_pathway_tools_dat(path, encoding=encoding)
            if requested:
                native_records = [
                    record for record in native_records
                    if requested.intersection(record.get("UNIQUE-ID", []))
                ]
                for record in native_records:
                    found.update(record.get("UNIQUE-ID", []))
            path_records = record_factory(native_records)
            for record in path_records:
                validate_record(record)
                if record["id"] in seen_ids:
                    raise ValueError(f"duplicate pathway across input files: {record['id']}")
                seen_ids.add(record["id"])
            records.extend(path_records)
        except (OSError, ValidationError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    if requested - found:
        print(f"pathway frames not found: {', '.join(sorted(requested - found))}", file=sys.stderr)
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
    parser.add_argument("--sha256", help="expected SHA-256 of the single local input")
    parser.add_argument(
        "--include-provenance", action="store_true",
        help="include file hash, worksheet/row locator and ordered original cells",
    )
    args = parser.parse_args(argv)
    if args.sha256 is not None and len(args.paths) != 1:
        parser.error("--sha256 requires exactly one input file")

    records = []
    for path in args.paths:
        try:
            records.extend(load_dbcan_pul(path, expected_sha256=args.sha256))
        except (OSError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            return 1

    for row in dbcan_pul_seed_rows(records, include_provenance=args.include_provenance):
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


def _page(
    title: str, body: str, stylesheet_href: str = "style.css", *, homepage: bool = False,
    extra_head: str = "", corpus_note: str = "", site_root: str | None = None,
    inline_css: str | None = None,
) -> str:
    """One page in the site shell.

    `inline_css` makes a page that needs no other file -- the stylesheet and the
    theme script are embedded -- for the not-found page, which is served at
    addresses where no relative link resolves; it passes an absolute `site_root`.
    """
    root = html.escape(stylesheet_href.removesuffix("style.css") if site_root is None
                       else site_root)
    if inline_css is None:
        assets = (f'<link rel="stylesheet" href="{html.escape(stylesheet_href)}">\n'
                  f'  <script src="{root}assets/theme.js"></script>')
    else:
        script = (ASSETS / "theme.js").read_text()
        if "</style" in inline_css.lower() or "</script" in script.lower():
            raise SiteError("an inlined stylesheet or script would end its own element")
        assets = f"<style>\n{inline_css}</style>\n  <script>\n{script}</script>"
    body_class = ' class="home-page"' if homepage else ""
    heading = "" if homepage else f"    <h1>{label_html(title)}</h1>"
    corpus = f"\n    <p>{html.escape(corpus_note)}</p>" if corpus_note else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(plain_label(title))}</title>
  {assets}
{extra_head}
</head>
<body{body_class}>
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <header><nav aria-label="Main navigation">
    <a href="{root}index.html">PathwayMech overview</a>
    <a href="{root}browse.html">Browse pathways</a>
    <a href="{root}map.html">Text map</a>
    <a href="{root}sequence-map.html">Sequence map (pLM)</a>
    <a href="{root}index.html#downloads-title">Downloads</a>
    <a href="{root}schema.html">Schema</a>
    <a href="{GITHUB_REPO}">Source</a>
    <a href="https://culturebotai.github.io/mechs/">All Mech projects</a>
    <button type="button" id="theme-toggle" class="theme-toggle" \
aria-label="Toggle dark mode">Theme</button>
  </nav></header>
  <main id="main-content" tabindex="-1">
{heading}
    {body}
  </main>
  <footer class="site-footer">
    <p>Project data: <a href="{GITHUB_BLOB}/LICENSE-DATA">CC BY 4.0</a>.
      Code: <a href="{GITHUB_BLOB}/LICENSE-CODE">BSD-3-Clause</a>.
      Third-party source material keeps its own terms
      (<a href="{GITHUB_BLOB}/LICENSE">licence scope</a>).</p>{corpus}
    <p>Part of the CultureBotAI Mech knowledge bases.
      <a href="https://culturebotai.github.io/mechs/">Explore all Mech projects</a></p>
  </footer>
</body>
</html>
"""


_GROUNDING_OPTIONS = (
    ("protein-grounded", "Protein-grounded (UniProtKB)"),
    ("reaction-mechanisms", "Detailed reaction mechanisms"),
    ("gene-clusters", "Biosynthetic gene clusters"),
    ("curated-edges", "Curated mechanistic edges"),
)


def _browse_controls(
    types: list[tuple[str, int]] | None = None,
    taxa: list[tuple[str, int]] | None = None,
    grounding: dict[str, int] | None = None,
) -> str:
    """Filters whose options state how many records each one keeps."""
    type_opts = "".join(
        f'<option value="{html.escape(value, quote=True)}">'
        f'{html.escape(value.replace("-", " "))} ({count:,})</option>'
        for value, count in (types or [])
    )
    taxon_opts = "".join(
        f'<option value="{html.escape(value, quote=True)}">'
        f'{html.escape(value)} ({count:,})</option>'
        for value, count in (taxa or [])[:150]
    )
    grounding_opts = "".join(
        f'<option value="{value}">{label} ({(grounding or {}).get(value, 0):,})</option>'
        for value, label in _GROUNDING_OPTIONS
    )
    return f"""<aside class="facet-sidebar" aria-label="Pathway filters">
<form id="pathway-search" class="facet-form" hidden>
  <div class="facet-group">
    <label for="pathway-query">Search pathway name, organism, or identifier</label>
    <input id="pathway-query" name="q" type="search" \
placeholder="e.g. methanogenesis, MetaCyc...">
  </div>
  <div class="facet-group">
    <label for="pathway-type">Pathway type</label>
    <select id="pathway-type">
      <option value="">All pathway types</option>
      {type_opts}
    </select>
  </div>
  <div class="facet-group">
    <label for="pathway-taxon">Organism / Taxon</label>
    <select id="pathway-taxon">
      <option value="">All organisms / taxa</option>
      {taxon_opts}
    </select>
  </div>
  <div class="facet-group">
    <label for="pathway-grounding">Grounding &amp; mechanism</label>
    <select id="pathway-grounding">
      <option value="">All records</option>
      {grounding_opts}
    </select>
  </div>
  <div class="facet-group">
    <label for="pathway-sort">Sort pathways</label>
    <select id="pathway-sort">
      <option value="label-asc">Pathway name (A–Z)</option>
      <option value="label-desc">Pathway name (Z–A)</option>
      <option value="edges-desc">Mechanistic edges (high–low)</option>
      <option value="edges-asc">Mechanistic edges (low–high)</option>
      <option value="id-asc">Identifier (A–Z)</option>
      <option value="type-asc">Pathway type (A–Z)</option>
    </select>
  </div>
  <div class="facet-actions">
    <button type="reset">Reset</button>
  </div>
</form>
<p id="pathway-status" class="facet-status" role="status" aria-live="polite"></p>
<p id="pathway-empty" hidden>No pathways match. Try another term or reset the search.</p>
<div class="facet-links">
  <a href="map.html">Explore 2D text map →</a>
  <a href="sequence-map.html">Explore ESM-2 sequence map →</a>
</div>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  'use strict';
  const form = document.getElementById('pathway-search');
  const query = document.getElementById('pathway-query');
  const typeFilter = document.getElementById('pathway-type');
  const taxonFilter = document.getElementById('pathway-taxon');
  const groundingFilter = document.getElementById('pathway-grounding');
  const sortSelect = document.getElementById('pathway-sort');
  const listEl = document.getElementById('pathway-list');
  const rows = Array.from(document.querySelectorAll('#pathway-list li'));
  function filter() {{
    const term = query.value.trim().toLowerCase();
    const typeVal = typeFilter ? typeFilter.value : '';
    const taxonVal = taxonFilter ? taxonFilter.value : '';
    const groundingVal = groundingFilter ? groundingFilter.value : '';
    const sortVal = sortSelect ? sortSelect.value : 'label-asc';
    let count = 0;
    rows.forEach(row => {{
      const extraTaxa = row.dataset.taxa ? ' ' + row.dataset.taxa : '';
      const searchText = row.dataset.search + extraTaxa;
      const matchesTerm = searchText.toLowerCase().includes(term);
      const matchesType = !typeVal || (row.dataset.type || '') === typeVal;
      const rTaxa = (row.dataset.taxa || '').split('|');
      const matchesTaxon = !taxonVal || rTaxa.includes(taxonVal);
      const rGround = (row.dataset.grounding || '').split('|');
      const matchesGrounding = !groundingVal || rGround.includes(groundingVal);
      row.hidden = !(matchesTerm && matchesType && matchesTaxon && matchesGrounding);
      if (!row.hidden) count += 1;
    }});
    if (listEl && listEl.appendChild && sortSelect) {{
      const sorted = rows.slice().sort((a, b) => {{
        const la = a.dataset.label || '';
        const lb = b.dataset.label || '';
        const ia = a.dataset.id || '';
        const ib = b.dataset.id || '';
        const ea = Number(a.dataset.edges || '0');
        const eb = Number(b.dataset.edges || '0');
        const ta = a.dataset.type || '';
        const tb = b.dataset.type || '';
        if (sortVal === 'label-desc') return lb.localeCompare(la) || ia.localeCompare(ib);
        if (sortVal === 'edges-desc') return (eb - ea) || la.localeCompare(lb);
        if (sortVal === 'edges-asc') return (ea - eb) || la.localeCompare(lb);
        if (sortVal === 'id-asc') return ia.localeCompare(ib);
        if (sortVal === 'type-asc') return ta.localeCompare(tb) || la.localeCompare(lb);
        return la.localeCompare(lb) || ia.localeCompare(ib);
      }});
      sorted.forEach(r => listEl.appendChild(r));
    }}
    document.getElementById('pathway-status').textContent =
      count + ' of ' + rows.length + ' pathways match';
    document.getElementById('pathway-empty').hidden = count !== 0;
  }}
  function remember() {{
    const url = new URL(window.location.href);
    if (query.value) url.searchParams.set('q', query.value); else url.searchParams.delete('q');
    if (typeFilter && typeFilter.value) {{
      url.searchParams.set('type', typeFilter.value);
    }} else {{
      url.searchParams.delete('type');
    }}
    if (taxonFilter && taxonFilter.value) {{
      url.searchParams.set('taxon', taxonFilter.value);
    }} else {{
      url.searchParams.delete('taxon');
    }}
    if (groundingFilter && groundingFilter.value) {{
      url.searchParams.set('grounding', groundingFilter.value);
    }} else {{
      url.searchParams.delete('grounding');
    }}
    if (sortSelect && sortSelect.value && sortSelect.value !== 'label-asc') {{
      url.searchParams.set('sort', sortSelect.value);
    }} else {{
      url.searchParams.delete('sort');
    }}
    history.replaceState(null, '', url);
    filter();
  }}
  // A value no option carries -- a link shared before the options changed --
  // selects the default rather than leaving the control blank.
  function choose(select, value, fallback) {{
    if (!select) return;
    select.value = value || fallback;
    if (select.selectedIndex < 0) select.value = fallback;
  }}
  function restore() {{
    const params = new URLSearchParams(window.location.search);
    query.value = params.get('q') || '';
    choose(typeFilter, params.get('type'), '');
    choose(taxonFilter, params.get('taxon'), '');
    choose(groundingFilter, params.get('grounding'), '');
    choose(sortSelect, params.get('sort'), 'label-asc');
    filter();
  }}
  query.addEventListener('input', remember);
  [typeFilter, taxonFilter, groundingFilter, sortSelect].forEach(el => {{
    if (el) el.addEventListener('change', remember);
  }});
  window.addEventListener('pageshow', restore);
  form.addEventListener('submit', event => {{ event.preventDefault(); filter(); }});
  form.addEventListener('reset', event => {{
    event.preventDefault();
    query.value = '';
    if (typeFilter) typeFilter.value = '';
    if (taxonFilter) taxonFilter.value = '';
    if (groundingFilter) groundingFilter.value = '';
    if (sortSelect) sortSelect.value = 'label-asc';
    remember();
    query.focus();
  }});
  form.hidden = false;
  restore();
}});
</script>
</aside>"""


def _record_url(identifier: object, published: dict | set) -> str:
    """The page a map point opens, relative to pages/; empty if none is published.

    Derived from the record id, as the renderer names the page. The embedding
    files also store hrefs, but those were written from YAML file stems, which
    are not page names, and every one of them opened a 404.
    """
    if not isinstance(identifier, str) or identifier not in published:
        return ""
    return f"records/{_slug(identifier)}.html"


def _load_or_fallback_corpus_map(records: list, root: Path) -> dict[str, Any]:
    map_path = root / "data" / "embeddings" / "corpus_map.json"
    rec_by_id = {r.id: r for r in records}
    if map_path.is_file():
        try:
            raw = json.loads(map_path.read_text(encoding="utf-8"))
            classes = raw.get("classes") or []
            norm_points = []
            for pt in raw.get("points") or []:
                if isinstance(pt, list) and len(pt) >= 7:
                    x, y, cidx, ident, lbl, ptype, taxon = pt[:7]
                    rec = rec_by_id.get(ident)
                    kind, taxa, grounding = (
                        _record_facets(rec) if rec else (ptype, [taxon] if taxon else [], [])
                    )
                    p_count = sum(
                        1 for p in getattr(rec, "participants", [])
                        if str(p.get("id", "")).startswith("UniProtKB:")
                    ) if rec else 0
                    norm_points.append({
                        "id": ident,
                        "slug": _slug(ident),
                        "label": lbl,
                        "url": _record_url(ident, rec_by_id),
                        "x": x,
                        "y": y,
                        "pathway_type": classes[cidx] if 0 <= cidx < len(classes) else kind,
                        "top_taxon": taxon or (taxa[0] if taxa else "Unspecified"),
                        "taxa": taxa or ([taxon] if taxon else []),
                        "has_proteins": "protein-grounded" in grounding,
                        "edge_count": len(getattr(rec, "mechanistic_edges", [])) if rec else 0,
                        "reaction_count": len(getattr(rec, "reactions", [])) if rec else 0,
                        "protein_count": p_count,
                    })
                elif isinstance(pt, dict):
                    norm_points.append({**pt, "url": _record_url(pt.get("id"), rec_by_id)})
            return {
                "model": raw.get("model", "BAAI/bge-large-en-v1.5"),
                "method": raw.get("method", "pacmap"),
                "dim": raw.get("dim", 1024),
                "count": len(norm_points),
                "points": norm_points,
            }
        except (OSError, ValueError):
            pass
    points = []
    for idx, rec in enumerate(records):
        kind, taxa, grounding = _record_facets(rec)
        points.append({
            "id": rec.id,
            "slug": _slug(rec.id),
            "label": plain_label(rec.label),
            "url": f"records/{_slug(rec.id)}.html",
            "x": round((idx % 10) / 10.0, 4),
            "y": round((idx // 10) / max(1.0, len(records) / 10.0), 4),
            "pathway_type": kind,
            "top_taxon": taxa[0] if taxa else "Unspecified",
            "taxa": taxa[:5],
            "has_proteins": "protein-grounded" in grounding,
            "edge_count": len(getattr(rec, "mechanistic_edges", [])),
            "reaction_count": len(getattr(rec, "reactions", [])),
            "protein_count": 0,
        })
    return {
        "model": "BAAI/bge-large-en-v1.5",
        "method": "pacmap",
        "dim": 1024,
        "count": len(points),
        "points": points,
    }


def _load_or_fallback_sequence_map(records: list, root: Path) -> dict[str, Any]:
    seq_path = root / "data" / "embeddings" / "sequence_map.json"
    published = {record.id for record in records}
    if seq_path.is_file():
        try:
            raw = json.loads(seq_path.read_text(encoding="utf-8"))
            if "proteins" in raw and "pathways" in raw:
                pages = {_record_url(identifier, published) for identifier in published}
                return {
                    **raw,
                    "pathways": [{**item, "url": _record_url(item.get("id"), published)}
                                 for item in raw["pathways"]],
                    "proteins": [{**item,
                                  "url": item.get("url") if item.get("url") in pages else "",
                                  "pathway_urls": [url for url in item.get("pathway_urls", [])
                                                   if url in pages]}
                                 for item in raw["proteins"]],
                }
            proteins = []
            by_pw: dict[str, dict[str, Any]] = {}
            for pt in raw.get("points") or []:
                recs = pt.get("records") or []
                pw_labels = [r["label"] for r in recs if r.get("label")]
                pw_urls = [url for url in (_record_url(r.get("id"), published) for r in recs)
                           if url]
                org = pt.get("organism") or "Unspecified"
                p_cls = pt.get("class") or "pathway"
                proteins.append({
                    "id": pt.get("protein_id", ""),
                    "label": pt.get("label", ""),
                    "x": pt.get("x", 0.5),
                    "y": pt.get("y", 0.5),
                    "pathway_type": p_cls,
                    "taxon": org,
                    "taxa": [org],
                    "length": pt.get("length", 0),
                    "pathway_labels": pw_labels,
                    "pathway_urls": pw_urls,
                    "url": pw_urls[0] if pw_urls else "",
                })
                for r in recs:
                    pw_id = r.get("id")
                    if not pw_id:
                        continue
                    entry = by_pw.setdefault(pw_id, {
                        "id": pw_id,
                        "label": r.get("label", pw_id),
                        "url": _record_url(pw_id, published),
                        "pathway_type": r.get("class") or p_cls,
                        "top_taxon": org,
                        "taxa": set(),
                        "xs": [],
                        "ys": [],
                        "proteins": [],
                    })
                    entry["taxa"].add(org)
                    entry["xs"].append(float(pt.get("x", 0.5)))
                    entry["ys"].append(float(pt.get("y", 0.5)))
                    entry["proteins"].append(pt.get("protein_id", ""))
            pathways = []
            for _, entry in sorted(by_pw.items()):
                xs, ys = entry["xs"], entry["ys"]
                pathways.append({
                    "id": entry["id"],
                    "label": entry["label"],
                    "url": entry["url"],
                    "x": round(sum(xs) / len(xs), 4),
                    "y": round(sum(ys) / len(ys), 4),
                    "pathway_type": entry["pathway_type"],
                    "top_taxon": entry["top_taxon"],
                    "taxa": sorted(entry["taxa"]),
                    "protein_count": len(entry["proteins"]),
                    "proteins": entry["proteins"],
                })
            return {
                "model": raw.get("model", "facebook/esm2_t33_650M_UR50D"),
                "method": raw.get("method", "pacmap"),
                "dim": raw.get("dim", 1280),
                "protein_count": len(proteins),
                "pathway_count": len(pathways),
                "proteins": proteins,
                "pathways": pathways,
            }
        except (OSError, ValueError):
            pass
    return {
        "model": "facebook/esm2_t33_650M_UR50D",
        "method": "pacmap",
        "dim": 1280,
        "protein_count": 0,
        "pathway_count": 0,
        "proteins": [],
        "pathways": [],
    }


def _map_page(records: list, *, root: Path = ROOT, payload: dict[str, Any] | None = None,
              corpus_note: str = "") -> str:
    if payload is None:
        payload = _load_or_fallback_corpus_map(records, root)
    points = payload.get("points", [])
    plotted = {point.get("id") for point in points}
    unplotted = sorted((record for record in records if record.id not in plotted),
                       key=lambda record: record.id)
    coverage = ""
    if unplotted:
        missing = ", ".join(
            f'<a href="records/{_slug(record.id)}.html">{label_html(record.label)}</a> '
            f'(<code>{html.escape(record.id)}</code>)' for record in unplotted)
        shown = len(records) - len(unplotted)
        coverage = (f'<p class="map-coverage">{shown:,} of {len(records):,} published '
                    f'pathway records are plotted. Not on this map, because '
                    f'<code>data/embeddings/corpus_map.json</code> has no point for them '
                    f'yet: {missing}.</p>')
    types = sorted({str(p.get("pathway_type", "pathway")) for p in points})
    taxon_counts: dict[str, int] = {}
    for p in points:
        for t in p.get("taxa", []):
            taxon_counts[str(t)] = taxon_counts.get(str(t), 0) + 1
    top_taxa = [
        t for t, _ in sorted(taxon_counts.items(), key=lambda kv: (-kv[1], kv[0].casefold()))
    ][:100]
    type_opts = "".join(
        f'<option value="{html.escape(k, quote=True)}">{html.escape(k)}</option>'
        for k in types
    )
    taxon_opts = "".join(
        f'<option value="{html.escape(t, quote=True)}">{html.escape(t)}</option>'
        for t in top_taxa
    )
    json_blob = json.dumps(payload, separators=(",", ":")).replace("</", "<\\/")
    method_str = html.escape(str(payload.get("method", "pacmap")))
    model_str = html.escape(str(payload.get("model", "BAAI/bge-large-en-v1.5")))
    dim_val = int(payload.get("dim", 1024))
    body = f"""<nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="index.html">PathwayMech</a> <span aria-hidden="true">/</span>
      <span aria-current="page">Text embedding map</span>
    </nav>
    <p class="map-intro">Interactive 2D projection (<code>{method_str}</code>)
      of <code>{model_str}</code>
      ({dim_val}-d) text embeddings across {len(points):,} curated pathways.
      Drag to pan, scroll to zoom, hover for details, and click any point \
to open its pathway record.</p>
    {coverage}
    <div class="browse-layout">
      <aside class="facet-sidebar" aria-label="Embedding map filters">
        <form id="map-filter-form" class="facet-form">
          <div class="facet-group">
            <label for="map-query">Search pathways</label>
            <input id="map-query" name="q" type="search" placeholder="Name, ID, or organism...">
          </div>
          <div class="facet-group">
            <label for="map-color">Color points by</label>
            <select id="map-color">
              <option value="pathway_type">Pathway class</option>
              <option value="top_taxon">Primary organism / taxon</option>
              <option value="has_proteins">Protein grounding (UniProtKB)</option>
            </select>
          </div>
          <div class="facet-group">
            <label for="map-type">Pathway class</label>
            <select id="map-type">
              <option value="">All pathway classes</option>
              {type_opts}
            </select>
          </div>
          <div class="facet-group">
            <label for="map-taxon">Organism / Taxon</label>
            <select id="map-taxon">
              <option value="">All organisms / taxa</option>
              {taxon_opts}
            </select>
          </div>
          <div class="facet-group">
            <label for="map-grounding">Protein grounding</label>
            <select id="map-grounding">
              <option value="">All pathways</option>
              <option value="yes">Has UniProtKB proteins</option>
              <option value="no">No UniProtKB proteins</option>
            </select>
          </div>
          <div class="facet-actions">
            <button type="reset" id="map-reset">Reset filters &amp; zoom</button>
          </div>
        </form>
        <p id="map-status" class="facet-status" role="status" aria-live="polite"></p>
        <div id="map-legend" class="map-legend" aria-label="Color legend"></div>
      </aside>
      <div class="browse-results">
        <div class="map-canvas-wrap">
          <canvas id="map-canvas" width="920" height="620" \
aria-label="2D corpus embedding scatter plot"></canvas>
          <div id="map-tooltip" class="map-tooltip" hidden></div>
        </div>
      </div>
    </div>
    <script id="corpus-map-data" type="application/json">{json_blob}</script>
    <script>
    document.addEventListener('DOMContentLoaded', function () {{
      'use strict';
      const payload = JSON.parse(document.getElementById('corpus-map-data').textContent);
      const points = payload.points || [];
      const canvas = document.getElementById('map-canvas');
      const ctx = canvas.getContext('2d');
      const tooltip = document.getElementById('map-tooltip');
      const queryEl = document.getElementById('map-query');
      const colorEl = document.getElementById('map-color');
      const typeEl = document.getElementById('map-type');
      const taxonEl = document.getElementById('map-taxon');
      const groundEl = document.getElementById('map-grounding');
      const statusEl = document.getElementById('map-status');
      const legendEl = document.getElementById('map-legend');
      const formEl = document.getElementById('map-filter-form');
      const PALETTE = [
        '#0f766e', '#2563eb', '#d97706', '#9333ea', '#dc2626',
        '#059669', '#4f46e5', '#db2777', '#0284c7', '#65a30d', '#64748b'
      ];
      let scale = 1, panX = 0, panY = 0;
      let dragging = false, lastX = 0, lastY = 0, hovered = null;
      let colorMap = new Map();

      function esc(s) {{
        return String(s == null ? '' : s)
          .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
      }}

      function pointFieldVal(p, field) {{
        if (field === 'has_proteins') {{
          return p.has_proteins ? 'Protein-grounded' : 'Other';
        }}
        return String(p[field] || 'Other');
      }}

      function buildLegend() {{
        const field = colorEl.value;
        const counts = new Map();
        points.forEach(p => {{
          const val = pointFieldVal(p, field);
          counts.set(val, (counts.get(val) || 0) + 1);
        }});
        const entries = Array.from(counts.entries());
        const top = entries.sort((a, b) => b[1] - a[1]).slice(0, 10);
        colorMap = new Map();
        legendEl.innerHTML = '';
        top.forEach(([val, cnt], idx) => {{
          const col = PALETTE[idx % (PALETTE.length - 1)];
          colorMap.set(val, col);
          const item = document.createElement('div');
          item.className = 'legend-item';
          item.innerHTML = '<span class="legend-swatch" style="background:' + col + '"></span>' +
            '<span class="legend-label">' + esc(val) + ' (' + cnt + ')</span>';
          legendEl.appendChild(item);
        }});
      }}

      function matches(p) {{
        const q = queryEl.value.trim().toLowerCase();
        if (q) {{
          const hay = (p.label + ' ' + p.id + ' ' + (p.taxa || []).join(' ')).toLowerCase();
          if (!hay.includes(q)) return false;
        }}
        if (typeEl.value && p.pathway_type !== typeEl.value) return false;
        if (taxonEl.value && !(p.taxa || []).includes(taxonEl.value)) return false;
        if (groundEl.value === 'yes' && !p.has_proteins) return false;
        if (groundEl.value === 'no' && p.has_proteins) return false;
        return true;
      }}

      function project(p) {{
        const pad = 42;
        const w = canvas.width - pad * 2;
        const h = canvas.height - pad * 2;
        return {{
          cx: (pad + p.x * w) * scale + panX,
          cy: (pad + (1 - p.y) * h) * scale + panY,
        }};
      }}

      function draw() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const field = colorEl.value;
        let activeCount = 0;
        points.forEach(p => {{
          p._active = matches(p);
          if (p._active) activeCount += 1;
        }});
        points.forEach(p => {{
          if (p._active) return;
          const pos = project(p);
          p._cx = pos.cx; p._cy = pos.cy;
          ctx.beginPath();
          ctx.arc(pos.cx, pos.cy, 4, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(148, 163, 184, 0.22)';
          ctx.fill();
        }});
        points.forEach(p => {{
          if (!p._active) return;
          const pos = project(p);
          p._cx = pos.cx; p._cy = pos.cy;
          const val = pointFieldVal(p, field);
          const col = colorMap.get(val) || '#64748b';
          ctx.beginPath();
          ctx.arc(pos.cx, pos.cy, p === hovered ? 8 : 5.5, 0, Math.PI * 2);
          ctx.fillStyle = col;
          ctx.fill();
          ctx.lineWidth = p === hovered ? 2 : 1;
          ctx.strokeStyle = p === hovered ? '#0f172a' : '#ffffff';
          ctx.stroke();
        }});
        statusEl.textContent = activeCount + ' of ' + points.length + ' pathways visible';
      }}

      function syncUrl() {{
        const url = new URL(window.location.href);
        if (queryEl.value) url.searchParams.set('q', queryEl.value);
        else url.searchParams.delete('q');
        if (colorEl.value && colorEl.value !== 'pathway_type') {{
          url.searchParams.set('color', colorEl.value);
        }} else {{
          url.searchParams.delete('color');
        }}
        if (typeEl.value) url.searchParams.set('type', typeEl.value);
        else url.searchParams.delete('type');
        if (taxonEl.value) url.searchParams.set('taxon', taxonEl.value);
        else url.searchParams.delete('taxon');
        if (groundEl.value) url.searchParams.set('grounding', groundEl.value);
        else url.searchParams.delete('grounding');
        history.replaceState(null, '', url);
        draw();
      }}

      canvas.addEventListener('mousedown', e => {{
        dragging = true; lastX = e.clientX; lastY = e.clientY;
      }});
      window.addEventListener('mouseup', () => {{ dragging = false; }});
      canvas.addEventListener('mousemove', e => {{
        const rect = canvas.getBoundingClientRect();
        const mx = (e.clientX - rect.left) * (canvas.width / rect.width);
        const my = (e.clientY - rect.top) * (canvas.height / rect.height);
        if (dragging) {{
          panX += (e.clientX - lastX) * (canvas.width / rect.width);
          panY += (e.clientY - lastY) * (canvas.height / rect.height);
          lastX = e.clientX; lastY = e.clientY;
          draw();
          return;
        }}
        let best = null, bestDist = 144;
        points.forEach(p => {{
          if (!p._active) return;
          const dx = (p._cx || 0) - mx, dy = (p._cy || 0) - my;
          const d2 = dx * dx + dy * dy;
          if (d2 < bestDist) {{ bestDist = d2; best = p; }}
        }});
        if (best !== hovered) {{
          hovered = best;
          draw();
        }}
        if (best) {{
          tooltip.hidden = false;
          const tx = Math.min(rect.width - 260, Math.max(8, e.clientX - rect.left + 14));
          tooltip.style.left = tx + 'px';
          tooltip.style.top = Math.max(8, e.clientY - rect.top - 10) + 'px';
          tooltip.innerHTML = '<strong>' + esc(best.label) + '</strong><br>' +
            '<code>' + esc(best.id) + '</code><br>' +
            '<span>' + esc(best.pathway_type) + ' · ' + esc(best.top_taxon) + '</span><br>' +
            '<span>' + esc(best.edge_count) + ' edges · ' +
            esc(best.reaction_count) + ' reactions · ' +
            esc(best.protein_count) + ' proteins</span>';
        }} else {{
          tooltip.hidden = true;
        }}
      }});
      canvas.addEventListener('click', () => {{
        if (hovered && hovered.url) window.location.href = hovered.url;
      }});
      canvas.addEventListener('wheel', e => {{
        e.preventDefault();
        const factor = e.deltaY < 0 ? 1.15 : 1 / 1.15;
        scale = Math.min(8, Math.max(0.5, scale * factor));
        draw();
      }}, {{ passive: false }});

      queryEl.addEventListener('input', syncUrl);
      colorEl.addEventListener('change', () => {{ buildLegend(); syncUrl(); }});
      [typeEl, taxonEl, groundEl].forEach(el => el.addEventListener('change', syncUrl));
      formEl.addEventListener('submit', e => {{ e.preventDefault(); syncUrl(); }});
      formEl.addEventListener('reset', e => {{
        e.preventDefault();
        queryEl.value = ''; colorEl.value = 'pathway_type';
        typeEl.value = ''; taxonEl.value = ''; groundEl.value = '';
        scale = 1; panX = 0; panY = 0;
        buildLegend();
        syncUrl();
      }});
      const mapParams = new URLSearchParams(window.location.search);
      queryEl.value = mapParams.get('q') || '';
      if (mapParams.get('color')) colorEl.value = mapParams.get('color');
      if (mapParams.get('type')) typeEl.value = mapParams.get('type');
      if (mapParams.get('taxon')) taxonEl.value = mapParams.get('taxon');
      if (mapParams.get('grounding')) groundEl.value = mapParams.get('grounding');
      buildLegend();
      draw();
    }});
    </script>"""
    return _page("PathwayMech text embedding map", body, corpus_note=corpus_note)


def _sequence_map_page(records: list, *, root: Path = ROOT,
                       payload: dict[str, Any] | None = None, corpus_note: str = "") -> str:
    if payload is None:
        payload = _load_or_fallback_sequence_map(records, root)
    proteins = payload.get("proteins", [])
    pathways = payload.get("pathways", [])
    published = {record.id for record in records}
    covered = len(published & {pathway.get("id") for pathway in pathways})
    types = sorted({
        str(p.get("pathway_type", "pathway"))
        for item in (*pathways, *proteins)
        for p in ([item] if "pathway_type" in item else [])
    })
    taxa = sorted({
        str(t)
        for item in (*pathways, *proteins)
        for t in (item.get("taxa") or ([item["taxon"]] if item.get("taxon") else []))
        if t
    })[:100]
    type_opts = "".join(
        f'<option value="{html.escape(k, quote=True)}">{html.escape(k)}</option>'
        for k in types
    )
    taxon_opts = "".join(
        f'<option value="{html.escape(t, quote=True)}">{html.escape(t)}</option>'
        for t in taxa
    )
    json_blob = json.dumps(payload, separators=(",", ":")).replace("</", "<\\/")
    seq_model = html.escape(str(payload.get("model", "facebook/esm2_t33_650M_UR50D")))
    seq_dim = int(payload.get("dim", 1280))
    body = f"""<nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="index.html">PathwayMech</a> <span aria-hidden="true">/</span>
      <span aria-current="page">Sequence map (ESM-2 pLM)</span>
    </nav>
    <p class="map-intro">Protein language model (<code>{seq_model}</code>,
      {seq_dim}-d) PaCMAP projection across \
<strong>{len(proteins):,}</strong> UniProtKB proteins
      and <strong>{len(pathways):,}</strong> mean-pooled pathway sequence centroids.
      Switch between pathway centroids and individual proteins in the sidebar.</p>
    <p class="map-coverage">Centroids cover {covered:,} of the {len(records):,} published
      pathway records: a record appears only when
      <code>data/embeddings/sequence_map.json</code> holds an embedded UniProtKB protein
      for it.</p>
    <div class="browse-layout">
      <aside class="facet-sidebar" aria-label="Sequence map filters">
        <form id="seq-filter-form" class="facet-form">
          <div class="facet-group">
            <label for="seq-mode">Projection view</label>
            <select id="seq-mode">
              <option value="pathways">Pathway centroids ({len(pathways):,})</option>
              <option value="proteins">Individual proteins ({len(proteins):,})</option>
            </select>
          </div>
          <div class="facet-group">
            <label for="seq-query">Search protein, pathway, or UniProtKB ID</label>
            <input id="seq-query" name="q" type="search" \
placeholder="e.g. UniProtKB, rubisco, E. coli...">
          </div>
          <div class="facet-group">
            <label for="seq-color">Color points by</label>
            <select id="seq-color">
              <option value="pathway_type">Pathway class</option>
              <option value="top_taxon">Organism / Taxon</option>
            </select>
          </div>
          <div class="facet-group">
            <label for="seq-type">Pathway class</label>
            <select id="seq-type">
              <option value="">All pathway classes</option>
              {type_opts}
            </select>
          </div>
          <div class="facet-group">
            <label for="seq-taxon">Organism / Taxon</label>
            <select id="seq-taxon">
              <option value="">All organisms / taxa</option>
              {taxon_opts}
            </select>
          </div>
          <div class="facet-actions">
            <button type="reset" id="seq-reset">Reset filters &amp; zoom</button>
          </div>
        </form>
        <p id="seq-status" class="facet-status" role="status" aria-live="polite"></p>
        <div id="seq-legend" class="map-legend" aria-label="Color legend"></div>
      </aside>
      <div class="browse-results">
        <div class="map-canvas-wrap">
          <canvas id="seq-canvas" width="920" height="620" \
aria-label="2D ESM-2 sequence embedding scatter plot"></canvas>
          <div id="seq-tooltip" class="map-tooltip" hidden></div>
        </div>
      </div>
    </div>
    <script id="seq-map-data" type="application/json">{json_blob}</script>
    <script>
    document.addEventListener('DOMContentLoaded', function () {{
      'use strict';
      const payload = JSON.parse(document.getElementById('seq-map-data').textContent);
      const canvas = document.getElementById('seq-canvas');
      const ctx = canvas.getContext('2d');
      const tooltip = document.getElementById('seq-tooltip');
      const modeEl = document.getElementById('seq-mode');
      const queryEl = document.getElementById('seq-query');
      const colorEl = document.getElementById('seq-color');
      const typeEl = document.getElementById('seq-type');
      const taxonEl = document.getElementById('seq-taxon');
      const statusEl = document.getElementById('seq-status');
      const legendEl = document.getElementById('seq-legend');
      const formEl = document.getElementById('seq-filter-form');
      const PALETTE = [
        '#0f766e', '#2563eb', '#d97706', '#9333ea', '#dc2626',
        '#059669', '#4f46e5', '#db2777', '#0284c7', '#65a30d', '#64748b'
      ];
      let scale = 1, panX = 0, panY = 0;
      let dragging = false, lastX = 0, lastY = 0, hovered = null;
      let colorMap = new Map();

      function esc(s) {{
        return String(s == null ? '' : s)
          .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
      }}

      function activePoints() {{
        return modeEl.value === 'proteins'
          ? (payload.proteins || [])
          : (payload.pathways || []);
      }}

      function pointGroup(p) {{
        if (colorEl.value === 'top_taxon') {{
          return p.top_taxon || p.taxon || 'Unspecified';
        }}
        return p.pathway_type || 'pathway';
      }}

      function buildLegend() {{
        const pts = activePoints();
        const counts = new Map();
        pts.forEach(p => {{
          const g = pointGroup(p);
          counts.set(g, (counts.get(g) || 0) + 1);
        }});
        const entries = Array.from(counts.entries());
        const top = entries.sort((a, b) => b[1] - a[1]).slice(0, 10);
        colorMap = new Map();
        legendEl.innerHTML = '';
        top.forEach(([val, cnt], idx) => {{
          const col = PALETTE[idx % (PALETTE.length - 1)];
          colorMap.set(val, col);
          const item = document.createElement('div');
          item.className = 'legend-item';
          item.innerHTML = '<span class="legend-swatch" style="background:' + col + '"></span>' +
            '<span class="legend-label">' + esc(val) + ' (' + cnt + ')</span>';
          legendEl.appendChild(item);
        }});
      }}

      function matches(p) {{
        const q = queryEl.value.trim().toLowerCase();
        if (q) {{
          const extra = (p.pathway_labels || []).join(' ') + ' ' +
            (p.proteins || []).join(' ') + ' ' +
            (p.gene_symbol || '') + ' ' + (p.taxon || '');
          const hay = (p.label + ' ' + p.id + ' ' + extra).toLowerCase();
          if (!hay.includes(q)) return false;
        }}
        if (typeEl.value && p.pathway_type !== typeEl.value) return false;
        if (taxonEl.value) {{
          const pTaxa = p.taxa || (p.taxon ? [p.taxon] : []);
          if (!pTaxa.includes(taxonEl.value)) return false;
        }}
        return true;
      }}

      function project(p) {{
        const pad = 42;
        const w = canvas.width - pad * 2;
        const h = canvas.height - pad * 2;
        return {{
          cx: (pad + p.x * w) * scale + panX,
          cy: (pad + (1 - p.y) * h) * scale + panY,
        }};
      }}

      function draw() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const pts = activePoints();
        let activeCount = 0;
        pts.forEach(p => {{
          p._active = matches(p);
          if (p._active) activeCount += 1;
        }});
        pts.forEach(p => {{
          if (p._active) return;
          const pos = project(p);
          p._cx = pos.cx; p._cy = pos.cy;
          ctx.beginPath();
          ctx.arc(pos.cx, pos.cy, 4, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(148, 163, 184, 0.22)';
          ctx.fill();
        }});
        pts.forEach(p => {{
          if (!p._active) return;
          const pos = project(p);
          p._cx = pos.cx; p._cy = pos.cy;
          const col = colorMap.get(pointGroup(p)) || '#64748b';
          ctx.beginPath();
          ctx.arc(pos.cx, pos.cy, p === hovered ? 8 : 5.5, 0, Math.PI * 2);
          ctx.fillStyle = col;
          ctx.fill();
          ctx.lineWidth = p === hovered ? 2 : 1;
          ctx.strokeStyle = p === hovered ? '#0f172a' : '#ffffff';
          ctx.stroke();
        }});
        const unit = modeEl.value === 'proteins' ? 'proteins' : 'pathway centroids';
        statusEl.textContent = activeCount + ' of ' + pts.length + ' ' + unit + ' visible';
      }}

      function syncSeqUrl() {{
        const url = new URL(window.location.href);
        if (queryEl.value) url.searchParams.set('q', queryEl.value);
        else url.searchParams.delete('q');
        if (modeEl.value && modeEl.value !== 'pathways') {{
          url.searchParams.set('mode', modeEl.value);
        }} else {{
          url.searchParams.delete('mode');
        }}
        if (colorEl.value && colorEl.value !== 'pathway_type') {{
          url.searchParams.set('color', colorEl.value);
        }} else {{
          url.searchParams.delete('color');
        }}
        if (typeEl.value) url.searchParams.set('type', typeEl.value);
        else url.searchParams.delete('type');
        if (taxonEl.value) url.searchParams.set('taxon', taxonEl.value);
        else url.searchParams.delete('taxon');
        history.replaceState(null, '', url);
        draw();
      }}

      canvas.addEventListener('mousedown', e => {{
        dragging = true; lastX = e.clientX; lastY = e.clientY;
      }});
      window.addEventListener('mouseup', () => {{ dragging = false; }});
      canvas.addEventListener('mousemove', e => {{
        const rect = canvas.getBoundingClientRect();
        const mx = (e.clientX - rect.left) * (canvas.width / rect.width);
        const my = (e.clientY - rect.top) * (canvas.height / rect.height);
        if (dragging) {{
          panX += (e.clientX - lastX) * (canvas.width / rect.width);
          panY += (e.clientY - lastY) * (canvas.height / rect.height);
          lastX = e.clientX; lastY = e.clientY;
          draw();
          return;
        }}
        const pts = activePoints();
        let best = null, bestDist = 144;
        pts.forEach(p => {{
          if (!p._active) return;
          const dx = (p._cx || 0) - mx, dy = (p._cy || 0) - my;
          const d2 = dx * dx + dy * dy;
          if (d2 < bestDist) {{ bestDist = d2; best = p; }}
        }});
        if (best !== hovered) {{ hovered = best; draw(); }}
        if (best) {{
          tooltip.hidden = false;
          const tx = Math.min(rect.width - 260, Math.max(8, e.clientX - rect.left + 14));
          tooltip.style.left = tx + 'px';
          tooltip.style.top = Math.max(8, e.clientY - rect.top - 10) + 'px';
          if (modeEl.value === 'proteins') {{
            tooltip.innerHTML = '<strong>' + esc(best.label) + '</strong><br>' +
              '<code>' + esc(best.id) + '</code><br>' +
              '<span>' + esc(best.taxon || 'Unspecified') + ' · ' +
              esc(best.length || 0) + ' aa</span><br>' +
              '<span>Pathways: ' + esc((best.pathway_labels || []).join(', ')) + '</span>';
          }} else {{
            tooltip.innerHTML = '<strong>' + esc(best.label) + '</strong><br>' +
              '<code>' + esc(best.id) + '</code><br>' +
              '<span>' + esc(best.pathway_type) + ' · ' + esc(best.top_taxon) + '</span><br>' +
              '<span>' + esc(best.protein_count) + ' ESM-2 grounded protein(s)</span>';
          }}
        }} else {{
          tooltip.hidden = true;
        }}
      }});
      canvas.addEventListener('click', () => {{
        if (!hovered) return;
        const url = hovered.url || (hovered.pathway_urls && hovered.pathway_urls[0]);
        if (url) window.location.href = url;
      }});
      canvas.addEventListener('wheel', e => {{
        e.preventDefault();
        const factor = e.deltaY < 0 ? 1.15 : 1 / 1.15;
        scale = Math.min(8, Math.max(0.5, scale * factor));
        draw();
      }}, {{ passive: false }});

      modeEl.addEventListener('change', () => {{
        hovered = null; buildLegend(); syncSeqUrl();
      }});
      colorEl.addEventListener('change', () => {{ buildLegend(); syncSeqUrl(); }});
      queryEl.addEventListener('input', syncSeqUrl);
      [typeEl, taxonEl].forEach(el => el.addEventListener('change', syncSeqUrl));
      formEl.addEventListener('submit', e => {{ e.preventDefault(); syncSeqUrl(); }});
      formEl.addEventListener('reset', e => {{
        e.preventDefault();
        queryEl.value = ''; modeEl.value = 'pathways'; colorEl.value = 'pathway_type';
        typeEl.value = ''; taxonEl.value = '';
        scale = 1; panX = 0; panY = 0;
        buildLegend(); syncSeqUrl();
      }});
      const seqParams = new URLSearchParams(window.location.search);
      queryEl.value = seqParams.get('q') || '';
      if (seqParams.get('mode')) modeEl.value = seqParams.get('mode');
      if (seqParams.get('color')) colorEl.value = seqParams.get('color');
      if (seqParams.get('type')) typeEl.value = seqParams.get('type');
      if (seqParams.get('taxon')) taxonEl.value = seqParams.get('taxon');
      buildLegend();
      draw();
    }});
    </script>"""
    return _page("PathwayMech sequence embedding map (ESM-2 pLM)", body,
                 corpus_note=corpus_note)


# The public page for each namespace a record page shows: the local-id shape a
# page exists for, and its URL. An identifier whose shape does not match has no
# page of its own and is left unlinked rather than sent to a 404 -- the GO-CAM
# and GPML node ids scoped to their source model, PathBank's BioPAX objects and
# PathWhiz PW ids. MetaCyc and EcoCyc are the citation routes this repository
# already used; _term_url() types them by what the record declares.
_ROUTES: dict[str, tuple[str, str]] = {
    "CHEBI": (r"[0-9]+", "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:{}"),
    "EC": (r"[0-9]+\.[0-9]+\.[0-9]+\.n?[0-9]+", "https://enzyme.expasy.org/EC/{}"),
    "EcoCyc": (r"[A-Za-z0-9][A-Za-z0-9_.-]*", "https://ecocyc.org/gene?id={}"),
    "Entrez": (r"[0-9]+", "https://www.ncbi.nlm.nih.gov/gene/{}"),
    "GO": (r"[0-9]{7}", "https://www.ebi.ac.uk/QuickGO/term/GO:{}"),
    "gomodel": (r"[0-9a-f]{16}|YeastPathways_[A-Za-z0-9+_.-]+",
                "https://model.geneontology.org/{}"),
    "hdl": (r"[0-9][0-9.]*/[A-Za-z0-9._-]+", "https://hdl.handle.net/{}"),
    "KEGG": (r"[CDGKMR][0-9]{5}|[a-z]{3,4}:[A-Za-z0-9_.-]+", "https://www.kegg.jp/entry/{}"),
    "MetaCyc": (r"[A-Za-z0-9_.-]+", "https://metacyc.org/META/NEW-IMAGE?type=PATHWAY&object={}"),
    "metanetx.chemical": (r"MNXM[0-9]+", "https://www.metanetx.org/chem_info/{}"),
    "MIBiG": (r"BGC[0-9]+(?:\.[0-9]+)?", "https://mibig.secondarymetabolites.org/go/{}"),
    "NCBIProtein": (r"[A-Z]{1,3}_?[0-9]+(?:\.[0-9]+)?", "https://www.ncbi.nlm.nih.gov/protein/{}"),
    "NCBITaxon": (r"[0-9]+", "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={}"),
    "PathBank": (r"SMP[0-9]{7}", "https://pathbank.org/view/{}"),
    "PubChem": (r"[0-9]+", "https://pubchem.ncbi.nlm.nih.gov/compound/{}"),
    "Reactome": (r"R-[A-Z]+-[0-9]+(?:\.[0-9]+)?", "https://reactome.org/content/detail/{}"),
    "RHEA": (r"[0-9]+", "https://www.rhea-db.org/rhea/{}"),
    "SGD": (r"S[0-9]{9}", "https://www.yeastgenome.org/locus/{}"),
    "UniProtKB": (r"[A-Z0-9]{6,10}(?:-[0-9]+)?", "https://www.uniprot.org/uniprotkb/{}/entry"),
    "WikiPathways": (r"WP[0-9]+", "https://www.wikipathways.org/instance/{}"),
}
# BioCyc and BiGG pages are typed (biocyc.org/linking.shtml): the route follows
# the category a record declares for the node. With no declared category --
# a reference the record cites but does not declare -- there is no link rather
# than a page of the wrong type.
_KIND_OF_CATEGORY = {
    "pathway": "pathway", "biological_process": "pathway",
    "molecular_activity": "reaction",
    "chemical_entity": "compound", "small_molecule": "compound", "cofactor": "compound",
    "lipid": "compound", "polymer": "compound",
    "protein": "gene", "complex": "gene", "rna": "gene", "gene": "gene",
}
_TYPED_ROUTES = {
    ("MetaCyc", "pathway"): "https://metacyc.org/META/NEW-IMAGE?type=PATHWAY&object={}",
    ("MetaCyc", "reaction"): "https://metacyc.org/META/NEW-IMAGE?type=REACTION&object={}",
    ("MetaCyc", "compound"): "https://metacyc.org/compound?orgid=META&id={}",
    ("MetaCyc", "gene"): "https://metacyc.org/gene?orgid=META&id={}",
    ("EcoCyc", "pathway"): "https://ecocyc.org/ECOLI/NEW-IMAGE?type=PATHWAY&object={}",
    ("EcoCyc", "reaction"): "https://ecocyc.org/ECOLI/NEW-IMAGE?type=REACTION&object={}",
    ("EcoCyc", "compound"): "https://ecocyc.org/compound?orgid=ECOLI&id={}",
    ("EcoCyc", "gene"): "https://ecocyc.org/gene?id={}",
    ("BiGG", "reaction"): "https://bigg.ucsd.edu/universal/reactions/{}",
    ("BiGG", "compound"): "https://bigg.ucsd.edu/universal/metabolites/{}",
}
_TYPED_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9+_.-]*")
# Namespaces this repository uses whose identifiers have no page outside the
# routes above: bioregistry resolves neither RHEA-COMP nor a bare BiGG id.
_KNOWN_PREFIXES = frozenset({*_ROUTES, "PMID", "DOI", "BiGG", "RHEA-COMP"})
_CURIE = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*:[^\s<>\"'\\]+")


def _reference_url(identifier: str) -> str | None:
    """Resolve only namespaces with a known public route for the identifier's shape."""
    prefix, _, local_id = identifier.partition(":")
    if prefix == "PMID" and local_id.isdigit():
        return f"https://pubmed.ncbi.nlm.nih.gov/{local_id}/"
    if prefix == "DOI" and local_id.startswith("10.") and "/" in local_id:
        return "https://doi.org/" + quote(local_id, safe="/")
    route = _ROUTES.get(prefix)
    if route and re.fullmatch(route[0], local_id):
        return route[1].format(quote(local_id, safe=":/"))
    return None


def _term_url(identifier: str, category: str = "") -> str | None:
    """Where a reader can look up a displayed identifier, or None if nowhere.

    `category` is the node category the record declares for it (or "pathway"
    for the record's own id), which the typed BioCyc and BiGG routes need.
    Other known namespaces use their routes; an identifier of any other
    well-formed prefix falls back to bioregistry.io, which resolves or explains
    every registered prefix.
    """
    prefix, _, local_id = identifier.partition(":")
    if prefix in {"MetaCyc", "EcoCyc", "BiGG"}:
        route = _TYPED_ROUTES.get((prefix, _KIND_OF_CATEGORY.get(category, "")))
        if route and _TYPED_ID.fullmatch(local_id):
            return route.format(quote(local_id, safe=""))
        return None
    url = _reference_url(identifier)
    if url:
        return url
    if prefix in _KNOWN_PREFIXES or not _CURIE.fullmatch(identifier):
        return None
    return "https://bioregistry.io/" + quote(identifier, safe=":/")


def _record_page(record: object, source_path: str | None = None,
                 sessions: list[dict] | None = None, *,
                 own_pages: dict[str, str] | None = None, corpus_note: str = "") -> str:
    """Publish the declared endpoints and evidence without interpreting them.

    `own_pages` maps every published record id to its page beside this one, so
    an identifier naming another PathwayMech record opens that record.
    """
    labels: dict[str, set[str]] = {}
    for field in ("taxa", "participants", "reactions", "gene_clusters"):
        for node in getattr(record, field, []):
            labels.setdefault(node["id"], set()).add(node.get("label") or node["id"])
    nodes = {identifier: next(iter(values)) if len(values) == 1 else identifier
             for identifier, values in labels.items()}
    record_id = getattr(record, "id", "")
    # The declared category types a BioCyc or BiGG link; the record itself is a pathway.
    categories = {record_id: "pathway"}
    for field, default in (("participants", ""), ("reactions", "molecular_activity")):
        for node in getattr(record, field, []):
            categories.setdefault(node["id"], node.get("category") or default)

    def curie_html(identifier: str) -> str:
        """The identifier as code, linked to where a reader can look it up."""
        code = f"<code>{html.escape(identifier)}</code>"
        if identifier != record_id and identifier in (own_pages or {}):
            return f'<a href="{html.escape(own_pages[identifier])}">{code}</a>'
        url = _term_url(identifier, categories.get(identifier, ""))
        return f'<a href="{html.escape(url)}">{code}</a>' if url else code

    components = []
    component_anchors: dict[str, str] = {}
    detail_only = set(getattr(record, "detail_only_participant_ids", []))
    for field in ("taxa", "participants", "reactions"):
        for node in getattr(record, field, []):
            component_anchor = f"component-{len(components) + 1}"
            component_anchors.setdefault(node["id"], component_anchor)
            kind = node.get("category") or {"taxa": "taxon"}.get(field, field.removesuffix("s"))
            direction = node.get("direction", "")
            scope = ('<br><strong class="mechanism-status">Detail only</strong>'
                     if node["id"] in detail_only else "")
            components.append(
                f'<tr id="{component_anchor}"><td>{label_html(nodes[node["id"]])}<br>'
                f"{curie_html(node['id'])}</td>"
                f"<td>{html.escape(kind.replace('_', ' '))}{scope}</td>"
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

    def endpoint(identifier: str, edge: dict, number: int, role: str) -> str:
        label = nodes.get(identifier, identifier)
        rendered = (f"{label_html(label)}<br>{curie_html(identifier)}"
                    if label != identifier else curie_html(identifier))
        for qualifier in edge.get("endpoint_qualifiers", []):
            if qualifier["endpoint"] == role:
                rendered += (
                    '<div class="endpoint-qualifier" '
                    f'id="mechanism-edge-{number}-qualifier-{role}">'
                    f'<p><strong>{html.escape(qualifier["kind"].replace("_", " "))}:</strong> '
                    f'{autolink_html(qualifier["description"])}</p>'
                    '<details><summary>Qualification evidence</summary><ul>'
                    + citations_html(qualifier["evidence"]) + '</ul></details></div>'
                )
        return rendered

    references = getattr(record, "references", [])
    ref_anchors = {ref["id"]: f"reference-{number}" for number, ref in enumerate(references, 1)}
    def citations_html(items: list[dict]) -> str:
        citations = []
        for evidence in items:
            reference = html.escape(evidence["reference_id"])
            anchor = ref_anchors.get(evidence["reference_id"])
            citation = f'<a href="#{anchor}">{reference}</a>' if anchor else reference
            if "quote" in evidence:
                support = evidence_html(evidence["reference_id"], evidence["quote"])
            else:
                support = ("<p><strong>Source assertion:</strong> "
                           f"{autolink_html(evidence['source_assertion'])}</p>")
            if evidence.get("source_locator"):
                support += ("<details><summary>Source location</summary><code>"
                            f"{html.escape(evidence['source_locator'])}</code></details>")
            citations.append(f"<li>{citation}{support}</li>")
        return "".join(citations)

    rows = []
    for edge_number, edge in enumerate(record.mechanistic_edges, 1):
        description = autolink_html(edge.get("description", ""))
        for mechanism in getattr(record, "reaction_mechanisms", []):
            if (mechanism["relation_to_source"] == "alternative_interpretation"
                    and mechanism["source_reaction_id"] in {edge["subject"], edge["object"]}):
                target = mechanism_anchor(record.id, mechanism["key"], "section")
                description += ('<br><strong>Source-reported assertion.</strong> '
                                f'<a href="#{target}">See the alternative interpretation '
                                'and its unresolved or revised differences.</a>')
        rows.append(f'<tr id="mechanism-edge-{edge_number}">'
                    f"<td>{endpoint(edge['subject'], edge, edge_number, 'subject')}</td>"
                    f"<td>{html.escape(edge['predicate'])}<p>{description}</p></td>"
                    f"<td>{endpoint(edge['object'], edge, edge_number, 'object')}</td>"
                    f"<td><ul>{citations_html(edge.get('evidence', []))}</ul></td></tr>")
    edges = ('<div class="table-scroll" role="region" tabindex="0" '
             'aria-label="Mechanistic edges and evidence">'
             '<table><caption>Mechanistic edges and their cited evidence</caption><thead><tr>'
             '<th scope="col">Subject</th><th scope="col">Predicate and description</th>'
             '<th scope="col">Object</th><th scope="col">Evidence</th></tr></thead>'
             f"<tbody>{''.join(rows)}</tbody></table></div>")
    if not rows:
        edges = ('<p>Source cluster summary: this record contains cluster metadata and references, '
                 'but no curated mechanistic edges.</p>' if getattr(record, 'gene_clusters', [])
                 else '<p>No mechanistic edges recorded.</p>')
    cited = []
    for ref in references:
        details = " — ".join(rich_text_html(ref[field])
                             for field in ("title", "citation") if ref.get(field))
        identifier = html.escape(ref["id"])
        # The identifier opens the source's own page; `url` is the exact file or
        # API response the evidence was read from, which is often machine-readable,
        # so it stays beside it rather than replacing it.
        landing = _term_url(ref["id"], categories.get(ref["id"], ""))
        retrieved = ref.get("url")
        source_url = landing or retrieved or _reference_url(ref["id"])
        if ref.get("source_version"):
            details += f" (source version: {autolink_html(ref['source_version'])})"
        if landing and retrieved and retrieved != landing:
            details += f' · <a href="{html.escape(retrieved)}">retrieved source</a>'
        reference = (f'<a href="{html.escape(source_url)}">{identifier}</a>'
                     if source_url else identifier)
        cited.append(f'<li id="{ref_anchors[ref["id"]]}"><code>{reference}</code> {details}</li>')
    reference_section = f"<h2>References</h2><ul>{''.join(cited)}</ul>" if cited else ""
    actions = []
    if source_path:
        actions.append(f'<a href="{GITHUB_BLOB}/{quote(source_path, safe="/")}">'
                       "Read the source YAML</a>")
    if record_id:
        page_url = f"{SITE_URL}records/{_slug(record_id)}.html"
        report = urlencode({"title": record_id, "body": f"Record page: {page_url}\n"},
                           quote_via=quote)
        actions.append(f'<a href="{GITHUB_REPO}/issues/new?{html.escape(report)}">'
                       "Report a problem with this record</a>")
    provenance = (f'<p class="record-actions">{" · ".join(actions)}</p>' if actions else "")
    clusters = _gene_clusters(getattr(record, "gene_clusters", []))
    if record_id:
        component_anchors.setdefault(record_id, "pathway-identity")
    details = mechanism_views(record, nodes, component_anchors, citations_html)
    top_bar = (
        '<div class="downstream-top-bar">'
        '<nav class="breadcrumb" aria-label="Breadcrumb">'
        '<a href="../index.html">PathwayMech</a> <span aria-hidden="true">/</span> '
        '<a href="../browse.html">Browse pathways</a> <span aria-hidden="true">/</span> '
        f'<span aria-current="page">{html.escape(record_id)}</span></nav>'
        '<form class="page-search" action="../browse.html" method="get" role="search">'
        '<label class="visually-hidden" for="record-page-search">Search pathways</label>'
        '<input id="record-page-search" name="q" type="search" '
        'placeholder="Search pathways, organisms, or IDs...">'
        '<button type="submit">Search</button></form></div>'
    )
    return _page(
        record.label,
        f'{top_bar}<p id="pathway-identity">{curie_html(record_id)}</p>'
        + "".join(f"<p>{rich_text_html(paragraph)}</p>"
                  for paragraph in re.split(r"\n\s*\n", record.description))
        + f"{record_metadata(record)}{provenance}{graph_html(record, nodes, component_anchors)}"
        f"{details}"
        f"{component_section}<h2 id=\"mechanistic-edges\">Mechanistic edges</h2>"
        f"{edges}{clusters}{reference_section}{history_html(record, sessions or [])}",
        stylesheet_href="../style.css",
        extra_head=('<link rel="stylesheet" href="../assets/pathway-network.css">\n'
                    '<script src="../assets/pathway-network.js" defer></script>'),
        corpus_note=corpus_note,
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
            f"<strong>{label_html(str(cluster['label']))}</strong>"
            f"<span>{html.escape(str(cluster['id']))}</span>"
            f"<ul>{details}</ul>"
            "</li>"
        )
    return f"<h2>Biosynthetic gene clusters</h2><ul>{''.join(rendered)}</ul>"


@functools.lru_cache(maxsize=4)
def _schema_reference(schema_path: str, _digest: str) -> str:
    """The schema page's content, cached on the schema's bytes (`_digest`)."""
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(schema_path)
    classes = view.all_classes()
    enums = view.all_enums()

    def ranges(slot: Any) -> str:
        names = [alt.range for alt in (slot.any_of or slot.exactly_one_of or []) if alt.range]
        out = []
        for name in names or [slot.range or view.schema.default_range or "string"]:
            code = f"<code>{html.escape(name)}</code>"
            kind = "class" if name in classes else "enum" if name in enums else ""
            out.append(f'<a href="#{kind}-{html.escape(name)}">{code}</a>' if kind else code)
        return " or ".join(out)

    def slot_row(owner: str, slot: Any) -> str:
        name = html.escape(slot.name)
        note = " (identifier)" if slot.identifier else ""
        cardinality = ("Required" if slot.required or slot.identifier else "Optional") + (
            ", multivalued" if slot.multivalued else "")
        pattern = (f'<br><span class="schema-pattern">Pattern '
                   f'<code>{html.escape(slot.pattern)}</code></span>' if slot.pattern else "")
        return (f'<tr id="class-{html.escape(owner)}-{name}"><th scope="row"><code>{name}</code>'
                f"{note}</th><td>{ranges(slot)}</td><td>{cardinality}</td>"
                f"<td>{html.escape(slot.description or '')}{pattern}</td></tr>")

    sections = []
    for name, element in classes.items():
        slots = view.class_induced_slots(name)
        anchor = html.escape(name)
        table = (f'<div class="table-scroll" role="region" tabindex="0" '
                 f'aria-label="{anchor} slots"><table><caption>{anchor} slots ({len(slots)})'
                 '</caption><thead><tr><th scope="col">Slot</th><th scope="col">Range</th>'
                 '<th scope="col">Cardinality</th><th scope="col">Description</th></tr>'
                 f"</thead><tbody>{''.join(slot_row(name, slot) for slot in slots)}</tbody>"
                 "</table></div>" if slots else "<p>This class declares no slots.</p>")
        parent = (f' <span class="schema-meta">is a <a href="#class-{html.escape(element.is_a)}">'
                  f"{html.escape(element.is_a)}</a></span>" if element.is_a else "")
        sections.append(
            f'<section class="schema-class" id="class-{anchor}" '
            f'aria-labelledby="class-{anchor}-heading">'
            f'<h3 id="class-{anchor}-heading">{anchor}{parent}</h3>'
            f"<p>{html.escape(element.description or '')}</p>{table}</section>")
    values = []
    for name, enum in enums.items():
        anchor = html.escape(name)
        entries = []
        for text, value in (enum.permissible_values or {}).items():
            meaning = ""
            if value.meaning:
                url = _term_url(value.meaning)
                code = f"<code>{html.escape(value.meaning)}</code>"
                meaning = f' <a href="{html.escape(url)}">{code}</a>' if url else f" {code}"
            entries.append(f"<dt><code>{html.escape(text)}</code>{meaning}</dt>"
                           f"<dd>{html.escape(value.description or 'No description.')}</dd>")
        values.append(
            f'<section class="schema-enum" id="enum-{anchor}" '
            f'aria-labelledby="enum-{anchor}-heading">'
            f'<h3 id="enum-{anchor}-heading">{anchor}</h3>'
            f"<p>{html.escape(enum.description or '')}</p>"
            f'<dl class="schema-values">{"".join(entries)}</dl></section>')
    source = f"src/pathwaymech/schema/{Path(schema_path).name}"
    shared = " and ".join(
        f'<a href="{GITHUB_BLOB}/src/pathwaymech/schema/{name}"><code>{name}</code></a>'
        for name in ("mech_shared.yaml", "history.yaml"))
    contents = " · ".join(f'<a href="#class-{html.escape(n)}">{html.escape(n)}</a>'
                          for n in classes)
    enum_contents = " · ".join(f'<a href="#enum-{html.escape(n)}">{html.escape(n)}</a>'
                               for n in enums)
    return f"""<nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="index.html">PathwayMech</a> <span aria-hidden="true">/</span>
      <span aria-current="page">Schema</span></nav>
    <p>{html.escape(view.schema.description or "")}</p>
    <p class="schema-meta">Generated by <code>just render-pages</code> from
      <a href="{GITHUB_BLOB}/{source}"><code>{source}</code></a>, version
      {html.escape(str(view.schema.version or "not stated"))}. Each class lists the slots
      LinkML resolves for it. Descriptions are shown as written, without links: the
      identifiers in them are format examples. Schema licence:
      <a href="{GITHUB_BLOB}/LICENSE-CODE">{html.escape(view.schema.license or "BSD-3-Clause")}</a>.
      The vendored fleet schemas {shared} are published as YAML.</p>
    <nav class="schema-contents" aria-labelledby="schema-contents-title">
      <h2 id="schema-contents-title">Contents</h2>
      <p><strong>Classes:</strong> {contents}</p>
      <p><strong>Enumerations:</strong> {enum_contents}</p></nav>
    <section aria-labelledby="schema-classes">
      <h2 id="schema-classes">Classes ({len(classes)})</h2>{"".join(sections)}</section>
    <section aria-labelledby="schema-enums">
      <h2 id="schema-enums">Enumerations ({len(enums)})</h2>{"".join(values)}</section>"""


def _schema_page(*, corpus_note: str = "", schema_path: Path = SCHEMA_PATH) -> str:
    """Readable documentation of the record schema, read from the schema itself.

    Every class with its induced slots and every enumeration with its values,
    in the schema's own order and with no clock, so an unchanged schema renders
    the same bytes and the pages/ check covers it.
    """
    digest = hashlib.sha256(schema_path.read_bytes()).hexdigest()
    return _page("PathwayMech schema", _schema_reference(str(schema_path), digest),
                 corpus_note=corpus_note)


def _not_found_page(root: Path, *, record_count: int = 0, corpus_note: str = "") -> str:
    """What GitHub Pages serves, with HTTP 404, at any address the site lacks.

    The Pages workflow copies it to the artifact root, where GitHub looks for
    it. It is served at the missing address, where no relative link resolves,
    so its links are absolute, and the stylesheet and theme script are embedded
    rather than loaded from culturebotai.github.io, which the site check counts
    as a third-party asset.
    """
    stylesheet = root / "pages" / "style.css"
    css = stylesheet.read_text(encoding="utf-8") if stylesheet.is_file() else ""
    count = f"{record_count:,} " if record_count else ""
    body = f"""<p>There is no page at this address. Record pages are named after the
      record's identifier, with <code>:</code> and <code>/</code> replaced by
      <code>_</code>.</p>
    <form class="page-search" action="{SITE_URL}browse.html" method="get" role="search">
      <label class="visually-hidden" for="not-found-search">Search pathways</label>
      <input id="not-found-search" name="q" type="search"
             placeholder="Search pathways, organisms, or IDs...">
      <button type="submit">Search</button></form>
    <ul class="not-found-routes">
      <li><a href="{SITE_URL}browse.html">Browse all {count}pathway records</a></li>
      <li><a href="{SITE_URL}index.html">PathwayMech overview</a></li>
      <li><a href="{GITHUB_REPO}/issues/new">Report a broken link</a></li>
    </ul>"""
    return _page("PathwayMech: page not found", body, site_root=SITE_URL, inline_css=css,
                 corpus_note=corpus_note, extra_head='<meta name="robots" content="noindex">')


def _slug(identifier: str) -> str:
    return identifier.replace(":", "_").replace("/", "_")
