from __future__ import annotations

import html
import sys
from pathlib import Path

import yaml

from pathwaymech.schema import ValidationError
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
        check_docs_main,
        deep_research_contract_main,
    ]:
        exit_code = check()
        if exit_code:
            return exit_code
    return 0


def seed_from_sources_main() -> int:
    with (ROOT / "conf" / "sources.yaml").open(encoding="utf-8") as stream:
        config = yaml.safe_load(stream) or {}
    sources = [source for source in config.get("sources", []) if source.get("enabled")]
    for source in sources:
        print(f"{source['id']}\t{source['label']}\t{source['role']}")
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
