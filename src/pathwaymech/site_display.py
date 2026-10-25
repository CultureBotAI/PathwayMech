"""Escaped presentation of recorded metadata; never adds biological assertions."""
from __future__ import annotations

import html
import json
import re
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import quote, urlsplit

import yaml

_FORMAT = re.compile(r"(</?(?:sup|sub|i|em)>)", re.IGNORECASE)
_JSON_STRING_FIELD = re.compile(r'"([^"\\]+)"\s*:\s*("(?:[^"\\]|\\.)*")')

# Citation tokens inside record prose. URLs come first so that a DOI inside a
# URL stays part of that URL. Matching runs on the raw text and every piece is
# escaped on the way out, so record text never becomes markup.
_CITATION_TOKEN = re.compile(
    r"(?P<url>\b(?i:https?)://[^\s<>\"\\]+)"
    r"|(?P<doi>(?:\b(?i:doi)(?::\s?|=|\s))?(?<![\w./])10\.[0-9]{4,9}/[^\s<>\"\\]+)"
    r"|(?P<pmid>\b(?i:pmid)(?::\s?|\s)(?P<pmid_number>[0-9]{1,9})\b)"
    r"|(?P<pmcid>\bPMC[0-9]{4,9}\b)"
)
_CLOSERS = {")": "(", "]": "[", "}": "{"}


def plain_label(value: str) -> str:
    return _FORMAT.sub("", html.unescape(value))


def label_html(value: str) -> str:
    """Permit only attribute-free scientific formatting; escape everything else."""
    return "".join(part.lower() if _FORMAT.fullmatch(part) else html.escape(part)
                   for part in _FORMAT.split(html.unescape(value)))


def _trim_token(token: str) -> str:
    """Drop the sentence punctuation and unbalanced closers that end a token."""
    while token:
        last = token[-1]
        if last in ".,;:!?'\"" or (last in _CLOSERS
                                   and token.count(last) > token.count(_CLOSERS[last])):
            token = token[:-1]
            continue
        break
    return token


def _web_url(value: str) -> str | None:
    """An http(s) URL with a host and no credentials, else None."""
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        return None
    try:
        parts = urlsplit(value)
        _ = parts.port  # rejects a malformed port
    except ValueError:
        return None
    if (parts.scheme.lower() in {"http", "https"} and parts.hostname
            and parts.username is None and parts.password is None):
        return value
    return None


def _token_url(kind: str, token: str, match: re.Match[str]) -> str | None:
    if kind == "url":
        return _web_url(token)
    if kind == "doi":
        doi = token[token.index("10."):]
        return "https://doi.org/" + quote(doi, safe="/") if "/" in doi else None
    if kind == "pmid":
        return f"https://pubmed.ncbi.nlm.nih.gov/{match.group('pmid_number')}/"
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{token}/"


def autolink_html(value: str) -> str:
    """Escape record prose and link the PMID, PMCID, DOI and http(s) URL tokens in it.

    Only the token becomes the anchor and its visible text is unchanged, so a
    citation inside a source assertion, an edge description or a curation note
    can be followed without the sentence around it being reworded.
    """
    text = str(value)
    out: list[str] = []
    position = 0
    for match in _CITATION_TOKEN.finditer(text):
        kind = match.lastgroup if match.lastgroup != "pmid_number" else "pmid"
        token = match.group(0)
        if kind in {"url", "doi"}:
            token = _trim_token(token)
        url = _token_url(kind, token, match) if token else None
        if not url:
            continue
        out.append(html.escape(text[position:match.start()]))
        out.append(f'<a href="{html.escape(url)}">{html.escape(token)}</a>')
        position = match.start() + len(token)
    out.append(html.escape(text[position:]))
    return "".join(out)


def rich_text_html(value: str) -> str:
    """label_html() for record prose: the same formatting, with citations linked."""
    return "".join(part.lower() if _FORMAT.fullmatch(part) else autolink_html(part)
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
        return f"<blockquote>{autolink_html(fragment)}</blockquote>"
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


def _as_utc(value: object) -> datetime | None:
    """A timezone-aware timestamp in UTC; None for anything else."""
    if isinstance(value, datetime):
        moment = value
    else:
        try:
            moment = datetime.fromisoformat(str(value).strip())
        except ValueError:
            return None
    return moment.astimezone(UTC) if moment.tzinfo else None


def corpus_as_of(records: list, sessions: list[list[dict]]) -> str:
    """The latest curation event or session recorded for the published records.

    Taken from the records themselves, never from the clock, so rendering
    unchanged records twice gives the same bytes and `pages/` stays checkable.
    `sessions` holds each record's matched history sessions; a session whose
    target is not a published record does not date the corpus. Empty when
    nothing carries a usable timestamp: there is then no date to claim.
    """
    moments = [_as_utc(event.get("timestamp"))
               for record in records for event in getattr(record, "curation_history", [])]
    moments += [_as_utc(item["session"].get("timestamp"))
                for matched in sessions for item in matched]
    known = [moment for moment in moments if moment is not None]
    return max(known).strftime("%Y-%m-%d %H:%M UTC") if known else ""


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
                       f'{autolink_html(details)}</li>')
    for item in sessions:
        session = item["session"]
        actors = ", ".join(actor.get("name", actor["type"])
                           for actor in session.get("actors", []))
        events = "".join(f'<li>{html.escape(event["type"])} — '
                         f'{autolink_html(event["summary"])}'
                         f'<p>{autolink_html(event.get("details", ""))}</p></li>'
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
