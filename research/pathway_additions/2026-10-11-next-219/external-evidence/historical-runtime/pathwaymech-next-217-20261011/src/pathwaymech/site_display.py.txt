"""Escaped presentation of recorded metadata; never adds biological assertions."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import quote

import yaml

_FORMAT = re.compile(r"(</?(?:sup|sub|i|em)>)", re.IGNORECASE)
_JSON_STRING_FIELD = re.compile(r'"([^"\\]+)"\s*:\s*("(?:[^"\\]|\\.)*")')


def plain_label(value: str) -> str:
    return _FORMAT.sub("", html.unescape(value))


def label_html(value: str) -> str:
    """Permit only attribute-free scientific formatting; escape everything else."""
    return "".join(part.lower() if _FORMAT.fullmatch(part) else html.escape(part)
                   for part in _FORMAT.split(html.unescape(value)))


def record_kind(record: object) -> str:
    if not record.mechanistic_edges and getattr(record, "gene_clusters", []):
        return "Source cluster summary; no mechanistic edges curated"
    return f"{len(record.mechanistic_edges)} mechanistic edges"


def record_metadata(record: object) -> str:
    pathway_type = getattr(record, "pathway_type", "")
    kind = html.escape(pathway_type.replace("-", " ")) if pathway_type else "Not recorded"
    taxa = []
    for taxon in getattr(record, "taxa", []):
        identifier = taxon["id"]
        content = (f'{label_html(taxon.get("label", identifier))} '
                   f'<code>{html.escape(identifier)}</code>')
        prefix, _, local = identifier.partition(":")
        if prefix == "NCBITaxon" and local.isdigit():
            content = ('<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id='
                       f'{local}">{content}</a>')
        taxa.append(f"<li>{content}</li>")
    organisms = f'<ul>{"".join(taxa)}</ul>' if taxa else "Not recorded"
    return (f"<dl><dt>Pathway type</dt><dd>{kind}</dd>"
            f"<dt>Organism scope</dt><dd>{organisms}</dd></dl>")


def evidence_html(reference: str, fragment: str) -> str:
    if not reference.startswith("gomodel:") or not _JSON_STRING_FIELD.search(fragment):
        return f"<blockquote>{html.escape(fragment)}</blockquote>"
    # Some original extracts are deliberately partial JSON. Decode only complete
    # string fields and retain the exact extract; do not repair or invent facts.
    fields = []
    for key, value in _JSON_STRING_FIELD.findall(fragment):
        try:
            fields.append((key, json.loads(value)))
        except json.JSONDecodeError:
            continue
    displayed = [(key, value) for key, value in fields
                 if key in {"subject", "property", "property-label", "object", "id"}]
    facts = "".join(f"<li>{html.escape(key)}: <code>{html.escape(value)}</code></li>"
                    for key, value in displayed)
    return ('<p>GO-CAM source assertion (machine-readable model evidence, '
            'not a quotation from an experimental publication).</p>'
            f'<ul>{facts}</ul><details><summary>Exact source fragment</summary>'
            f'<pre>{html.escape(fragment)}</pre></details>')


def load_site_history(root: Path) -> dict[str, list[dict]]:
    """Associate sessions only by their recorded target path, never by similarity."""
    result: dict[str, list[dict]] = {}
    for path in sorted((root / "history" / "records").glob("*/*.yaml")):
        item = yaml.safe_load(path.read_text())
        item = {**item, "source_path": path.relative_to(root).as_posix()}
        result.setdefault(item["target"]["path"], []).append(item)
    return result


def history_html(record: object, sessions: list[dict]) -> str:
    entries = []
    for event in getattr(record, "curation_history", []):
        details = "; ".join(str(event[key]) for key in ("curator", "action", "changes")
                            if event.get(key))
        entries.append(f'<li><time>{html.escape(str(event["timestamp"]))}</time> '
                       f'{html.escape(details)}</li>')
    for item in sessions:
        session = item["session"]
        actors = ", ".join(actor.get("name", actor["type"])
                           for actor in session.get("actors", []))
        events = "".join(f'<li>{html.escape(event["type"])} — '
                         f'{html.escape(event["summary"])}'
                         f'<p>{html.escape(event.get("details", ""))}</p></li>'
                         for event in item["events"])
        source = quote(item["source_path"], safe="/")
        entries.append(f'<li><time>{html.escape(str(session["timestamp"]))}</time> '
                       f'{html.escape(actors)}<ul>{events}</ul>'
                       f'<a href="https://github.com/CultureBotAI/PathwayMech/blob/main/{source}">'
                       'Read this curation session</a></li>')
    content = (f'<ul>{"".join(entries)}</ul>' if entries else
               '<p>No curation history recorded for this pathway. '
               'This does not imply that no curation occurred.</p>')
    return ('<section aria-labelledby="history-title">'
            f'<h2 id="history-title">Curation history</h2>{content}</section>')
