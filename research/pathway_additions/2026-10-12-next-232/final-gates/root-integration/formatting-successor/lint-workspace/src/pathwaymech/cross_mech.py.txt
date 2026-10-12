"""Cross-Mech protein inventory: UniProt proteins in sibling Mechs versus PathwayMech.

Sibling Mechs (TraitMech, ProteinTraitsMech, NaturalProductMech, AntibioticMech,
CellStructureMech, ...) name proteins by UniProtKB accession in their own slots.
This module answers four questions from local checkouts, without a network:

1. Which accessions do the sibling Mechs hold, and in which record and slot?
2. Which of those are participants of a PathwayMech pathway record?
3. Does the sibling record link back to that PathwayMech record, and does every
   PathwayMech link in a sibling record resolve to a current record?
4. Which PathwayMech proteins of a linked or overlapping pathway does the
   sibling Mech not hold yet (candidate examples for a curator to judge)?

The slots each sibling uses are configuration (``conf/sibling_mechs.yaml``), not
guesses: a protein mentioned in prose or cited as evidence is not an example.
PathwayMech names yeast proteins by SGD gene id, so an SGD-to-UniProt map from
UniProtKB cross-references is an input (``fetch_sgd_uniprot_map`` builds one).
Reaction-level matches (a sibling protein whose Rhea reaction or complete EC
number appears in a pathway) need UniProt annotations, an optional input that
``fetch_uniprot_annotations`` builds. Both fetchers call UniProt anonymously.

A match is a lead for curation, never an assertion: sharing an accession says the
protein is a pathway participant, not that the sibling record's claim is about
that pathway. The curator decides, under the sibling Mech's own rules.
"""

from __future__ import annotations

import csv
import io
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from collections.abc import Callable, Iterable, Iterator
from dataclasses import asdict, dataclass, field, fields
from pathlib import Path
from typing import Any

import yaml

from pathwaymech.rhea_directions import master_ids

PATHWAYMECH_RECORD_URL = "https://culturebotai.github.io/PathwayMech/pages/records/{slug}.html"
# Matches a link to a PathwayMech record page wherever a sibling writes one.
PATHWAYMECH_URL = re.compile(
    r"(?i:https?://culturebotai\.github\.io/PathwayMech/pages/records/)[^\s<>\"']+"
)
# UniProtKB accession grammar (https://www.uniprot.org/help/accession_numbers),
# optionally followed by an isoform suffix.
_ACCESSION = r"(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})"
UNIPROT_VALUE = re.compile(rf"^(?:UniProtKB:)?({_ACCESSION})(?:-[0-9]+)?$")
_PATH_TOKEN = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(\[\])?$")
UNIPROT_REST = "https://rest.uniprot.org/uniprotkb/stream"
# Complete EC numbers only: "1.1.1.-" names a class, not an activity.
_COMPLETE_EC = re.compile(r"^\d+\.\d+\.\d+\.n?\d+$")


INDEX_FORMAT = "pathwaymech-pathway-index/1"
# Participant namespaces that name a gene product or an activity class.
PROTEIN_PREFIXES = ("UniProtKB", "SGD", "EC", "Ensembl", "Entrez", "NCBIProtein", "TubercuList")


def record_slug(record_id: str) -> str:
    """The page slug PathwayMech renders a record under (matches cli._slug)."""
    return record_id.replace(":", "_").replace("/", "_")


def record_url(record_id: str) -> str:
    return PATHWAYMECH_RECORD_URL.format(slug=record_slug(record_id))


def pathway_index_json(records: Iterable[Any]) -> str:
    """The published machine-readable index of PathwayMech records.

    Sibling Mechs check a PathwayMech link against this file (record id, label
    and page) instead of cloning the repository. It lists each record's
    protein and activity participants and reaction ids in their native namespaces.
    Confirming a UniProt protein against an SGD participant needs a separate
    provenance-bearing SGD mapping. It is rendered with the
    pages, so `just check-pages` fails while it is stale.
    """
    rows = []
    for record in sorted(records, key=lambda item: item.id):
        participants = getattr(record, "participants", None) or []
        rows.append({
            "id": record.id,
            "label": record.label,
            "pathway_type": getattr(record, "pathway_type", ""),
            "page": f"records/{record_slug(record.id)}.html",
            "url": record_url(record.id),
            "taxa": [{"id": taxon["id"], "label": taxon.get("label", "")}
                     for taxon in getattr(record, "taxa", None) or []],
            "proteins": [{"id": participant["id"], "label": participant.get("label", "")}
                         for participant in participants
                         if str(participant["id"]).split(":", 1)[0] in PROTEIN_PREFIXES],
            "reactions": [reaction["id"] for reaction in getattr(record, "reactions", None) or []],
        })
    document = {
        "format": INDEX_FORMAT,
        "source": "https://github.com/CultureBotAI/PathwayMech",
        "records": rows,
    }
    return json.dumps(document, indent=1, ensure_ascii=False) + "\n"


def normalize_accession(value: Any) -> str | None:
    """Return the canonical accession of a UniProtKB CURIE or bare accession.

    Isoform suffixes are dropped, so ``UniProtKB:P0A749-2`` matches ``P0A749``.
    Anything else, including prose that merely mentions an accession, is None.
    """
    if not isinstance(value, str):
        return None
    match = UNIPROT_VALUE.match(value.strip())
    return match.group(1) if match else None


# --------------------------------------------------------------------------
# PathwayMech side
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class PathwayProtein:
    """A protein participant of one PathwayMech record, resolved to UniProtKB."""

    accession: str
    record_id: str
    record_label: str
    participant_id: str
    participant_label: str


@dataclass
class PathwayIndex:
    """What PathwayMech holds, keyed for joins with sibling Mechs."""

    labels: dict[str, str] = field(default_factory=dict)
    slugs: dict[str, str] = field(default_factory=dict)
    proteins: dict[str, list[PathwayProtein]] = field(default_factory=dict)
    # Reactions and activities the record states (RHEA reaction nodes, EC
    # participants) and those its protein participants carry in UniProtKB.
    # GO-CAM and WikiPathways records state neither, so the second pair is
    # what lets a yeast pathway match at the reaction level at all.
    rhea: dict[str, set[str]] = field(default_factory=dict)
    ec: dict[str, set[str]] = field(default_factory=dict)
    participant_rhea: dict[str, set[str]] = field(default_factory=dict)
    participant_ec: dict[str, set[str]] = field(default_factory=dict)
    unmapped_sgd: set[str] = field(default_factory=set)
    rhea_directions: dict[str, str] = field(default_factory=dict)

    def records_for(self, accession: str) -> list[str]:
        return sorted({protein.record_id for protein in self.proteins.get(accession, [])})


def build_pathway_index(
    records: Iterable[dict[str, Any]],
    sgd_to_uniprot: dict[str, list[str]] | None = None,
    annotations: dict[str, dict[str, list[str]]] | None = None,
    rhea_directions: dict[str, str] | None = None,
) -> PathwayIndex:
    """Index PathwayMech records by protein accession, Rhea reaction and EC number.

    UniProtKB participants are used as written. An SGD participant contributes
    the UniProtKB accessions that ``sgd_to_uniprot`` maps it to; an SGD id with
    no mapping is reported in ``unmapped_sgd`` rather than silently skipped.
    ``annotations`` (UniProtKB Rhea and EC per accession) add the reactions of
    each record's protein participants, kept apart from what the record states.
    """
    sgd_to_uniprot = sgd_to_uniprot or {}
    annotations = annotations or {}
    validate_sgd_map(sgd_to_uniprot)
    validate_annotations(annotations)
    index = PathwayIndex(rhea_directions=rhea_directions or {})
    proteins: dict[str, list[PathwayProtein]] = defaultdict(list)
    for record in records:
        record_id = record["id"]
        index.labels[record_id] = record["label"]
        index.slugs[record_slug(record_id).casefold()] = record_id
        index.rhea[record_id] = master_ids({
            reaction["id"].split(":", 1)[1]
            for reaction in record.get("reactions") or []
            if str(reaction.get("id", "")).startswith("RHEA:")
        }, index.rhea_directions)
        index.ec[record_id] = {
            participant["id"].split(":", 1)[1]
            for participant in record.get("participants") or []
            if str(participant.get("id", "")).startswith("EC:")
            and _COMPLETE_EC.match(participant["id"].split(":", 1)[1])
        }
        for participant in record.get("participants") or []:
            participant_id = str(participant.get("id", ""))
            if participant_id.startswith("UniProtKB:"):
                accessions = [normalize_accession(participant_id)]
            elif participant_id.startswith("SGD:"):
                accessions = sgd_to_uniprot.get(participant_id, [])
                if not accessions:
                    index.unmapped_sgd.add(participant_id)
            else:
                continue
            for accession in accessions:
                if accession:
                    proteins[accession].append(
                        PathwayProtein(
                            accession=accession,
                            record_id=record_id,
                            record_label=record["label"],
                            participant_id=participant_id,
                            participant_label=str(participant.get("label", "")),
                        )
                    )
    index.proteins = dict(proteins)
    for accession, entries in index.proteins.items():
        annotation = annotations.get(accession) or {}
        rhea = master_ids(annotation.get("rhea", []), index.rhea_directions)
        ec = {value for value in annotation.get("ec", []) if _COMPLETE_EC.match(value)}
        for entry in entries:
            index.participant_rhea.setdefault(entry.record_id, set()).update(rhea)
            index.participant_ec.setdefault(entry.record_id, set()).update(ec)
    return index


def resolve_target(index: PathwayIndex, target: str) -> str | None:
    """Resolve a sibling link value (record id, page slug or page URL) to a record id."""
    target = target.strip()
    if target in index.labels:
        return target
    if target.lower().startswith(("http://", "https://")):
        try:
            parsed = urllib.parse.urlsplit(target)
        except ValueError:
            return None
        if parsed.netloc.lower() != "culturebotai.github.io":
            return None
        match = re.fullmatch(r"/PathwayMech/pages/records/([^/]+)\.html", parsed.path)
        if not match:
            return None
        slug = urllib.parse.unquote(match.group(1))
        record_id = index.slugs.get(slug.casefold())
        # Published paths are case-sensitive, even when the local filesystem
        # is not. A forgiving slug lookup must not bless a broken page URL.
        return record_id if record_id and record_slug(record_id) == slug else None
    return index.slugs.get(target.casefold())


# --------------------------------------------------------------------------
# Sibling side
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class SlotSpec:
    """A configured location of protein accessions or PathwayMech links."""

    path: str
    role: str = ""
    id_key: str | None = None
    label_key: str | None = None
    # Keep a list item only when these keys equal (when) or fully match the
    # regular expression (when_match) given here.
    when: dict[str, str] = field(default_factory=dict)
    when_match: dict[str, str] = field(default_factory=dict)
    # A mixed slot also holds other identifiers (e.g. CHEBI graph nodes); only
    # UniProtKB values count, and other values are not inventory errors.
    mixed: bool = False

    def selects(self, item: dict[str, Any]) -> bool:
        if any(str(item.get(key)) != value for key, value in self.when.items()):
            return False
        return all(re.fullmatch(pattern, str(item.get(key, "")))
                   for key, pattern in self.when_match.items())


@dataclass(frozen=True)
class MechSpec:
    name: str
    records: list[str]
    id_key: str = "identifier"
    label_key: str = "label"
    protein_slots: list[SlotSpec] = field(default_factory=list)
    link_slots: list[SlotSpec] = field(default_factory=list)
    # Parse only files whose text mentions a PathwayMech protein or PathwayMech.
    prefilter: bool = False


@dataclass(frozen=True)
class SiblingProtein:
    mech: str
    file: str
    record_id: str
    record_label: str
    slot: str
    role: str
    accession: str


@dataclass(frozen=True)
class SiblingLink:
    mech: str
    file: str
    record_id: str
    record_label: str
    slot: str
    target: str
    label: str | None


@dataclass
class ScanCoverage:
    """The part of a sibling checkout actually inspected by an inventory."""

    scope: str = "full"
    status: str = "complete"
    source: str = "working tree"
    commit: str = ""
    files_seen: int = 0
    files_parsed: int = 0
    files_filtered: int = 0
    unreadable_files: int = 0
    distinct_accessions: int = 0
    annotated_accessions: int = 0
    errors: int = 0


def load_config(path: Path) -> list[MechSpec]:
    """Read ``conf/sibling_mechs.yaml``."""
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if data.get("version") != 1:
        raise ValueError(f"{path}: unsupported config version {data.get('version')!r}")
    specs = []
    for name, body in (data.get("mechs") or {}).items():
        records = body.get("records")
        if isinstance(records, str):
            records = [records]
        if not records:
            raise ValueError(f"{path}: {name} declares no record globs")
        for pattern in records:
            glob_regex(pattern)  # reject unsupported shapes in both scan modes
        specs.append(
            MechSpec(
                name=name,
                records=list(records),
                id_key=body.get("id_key", "identifier"),
                label_key=body.get("label_key", "label"),
                protein_slots=[_slot(name, row) for row in body.get("protein_slots") or []],
                link_slots=[_slot(name, row) for row in body.get("link_slots") or []],
                prefilter=bool(body.get("prefilter", False)),
            )
        )
    return specs


def _slot(mech: str, row: dict[str, Any]) -> SlotSpec:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise ValueError(f"{mech}: every slot needs a string path")
    _parse_path(row["path"])
    conditions = {}
    for key in ("when", "when_match"):
        value = row.get(key) or {}
        if not isinstance(value, dict):
            raise ValueError(f"{mech}: slot {row['path']} has a non-mapping {key!r}")
        conditions[key] = {str(name): str(expected) for name, expected in value.items()}
    for pattern in conditions["when_match"].values():
        try:
            re.compile(pattern)
        except re.error as error:
            raise ValueError(f"{mech}: slot {row['path']} has a bad pattern: {error}") from error
    return SlotSpec(
        path=row["path"],
        role=str(row.get("role", "")),
        id_key=row.get("id_key"),
        label_key=row.get("label_key"),
        when=conditions["when"],
        when_match=conditions["when_match"],
        mixed=bool(row.get("mixed", False)),
    )


def _parse_path(path: str) -> list[tuple[str, bool]]:
    tokens = []
    for part in path.split("."):
        match = _PATH_TOKEN.match(part)
        if not match:
            raise ValueError(f"invalid slot path {path!r} at {part!r}")
        tokens.append((match.group(1), bool(match.group(2))))
    return tokens


def walk_path(document: Any, path: str) -> Iterator[tuple[str, Any]]:
    """Yield (concrete path, value) for every value a slot path reaches.

    ``causal_graphs[].nodes[].protein_examples[].uniprot_id`` visits each list
    item, so one record can yield many values. Missing keys yield nothing.
    """
    nodes: list[tuple[str, Any]] = [("", document)]
    for key, iterate in _parse_path(path):
        next_nodes = []
        for prefix, node in nodes:
            if not isinstance(node, dict) or key not in node:
                continue
            value = node[key]
            here = f"{prefix}.{key}" if prefix else key
            if iterate:
                if isinstance(value, list):
                    next_nodes.extend((f"{here}[{i}]", item) for i, item in enumerate(value))
            else:
                next_nodes.append((here, value))
        nodes = next_nodes
    yield from nodes


def sibling_files(root: Path, spec: MechSpec) -> list[Path]:
    files: set[Path] = set()
    for pattern in spec.records:
        files.update(path for path in root.glob(pattern) if path.is_file())
    return sorted(files)


def glob_regex(pattern: str) -> re.Pattern[str]:
    """A repository-relative glob as pathlib reads it: ``**/`` spans zero or more dirs."""
    if (any(char in pattern for char in "[]")
            or any("**" in part and part != "**" for part in pattern.split("/"))
            or pattern.endswith("**")):
        raise ValueError(f"unsupported record glob: {pattern!r}")
    out, i = [], 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out.append("(?:[^/]+/)*")
            i += 3
        elif pattern.startswith("**", i):
            out.append(".*")
            i += 2
        elif pattern[i] == "*":
            out.append("[^/]*")
            i += 1
        elif pattern[i] == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(pattern[i]))
            i += 1
    return re.compile("".join(out) + r"\Z")


def _git(root: Path, *args: str, data: bytes | None = None) -> bytes:
    result = subprocess.run(["git", "-C", str(root), *args], input=data, capture_output=True,
                            check=False)
    if result.returncode != 0:
        raise OSError(f"git {' '.join(args[:2])} failed in {root}: "
                      f"{result.stderr.decode(errors='replace').strip()}")
    return result.stdout


def commit_of(root: Path, ref: str = "HEAD") -> str:
    """The commit a checkout or ref resolves to, or '' outside a git repository."""
    try:
        return _git(root, "rev-parse", "--verify", f"{ref}^{{commit}}").decode().strip()
    except OSError:
        return ""


def git_documents(root: Path, ref: str, spec: MechSpec) -> Iterator[tuple[str, bytes]]:
    """(path, bytes) of every record blob the spec selects, read at ``ref``.

    Reading committed objects, not the working tree, keeps an inventory honest
    when a sibling checkout sits on a feature branch or has local edits.
    """
    commit = commit_of(root, ref)
    if not commit:
        raise OSError(f"{root}: {ref!r} is not a commit")
    patterns = [glob_regex(pattern) for pattern in spec.records]
    entries = []
    for entry in _git(root, "ls-tree", "-r", "-z", commit).split(b"\0"):
        if not entry:
            continue
        header, raw_name = entry.split(b"\t", 1)
        name = raw_name.decode("utf-8")
        if not any(pattern.match(name) for pattern in patterns):
            continue
        _, kind, oid = header.split()
        if kind != b"blob":
            raise OSError(f"{root}: {name} is not a record blob at {commit}")
        entries.append((name, oid))
    entries.sort()
    for start in range(0, len(entries), 2000):
        chunk = entries[start:start + 2000]
        # Resolve paths once in ls-tree. Repeating commit:path lookups for
        # hundreds of thousands of records repeatedly scans the same trees.
        request = b"".join(oid + b"\n" for _, oid in chunk)
        stream = _git(root, "cat-file", "--batch", data=request)
        offset = 0
        for name, oid in chunk:
            header_end = stream.index(b"\n", offset)
            header = stream[offset:header_end].split()
            if len(header) != 3 or header[0] != oid or header[1] != b"blob":
                raise OSError(f"{root}: cannot read {name} at {commit}")
            size = int(header[2])
            body_start = header_end + 1
            yield name, stream[body_start:body_start + size]
            offset = body_start + size + 1


def scan_sibling(
    root: Path,
    spec: MechSpec,
    loader: Callable[[Path], Any] | None = None,
    prefilter_terms: Iterable[str] = (),
    ref: str | None = None,
    coverage: ScanCoverage | None = None,
) -> tuple[list[SiblingProtein], list[SiblingLink], list[str]]:
    """Inventory one sibling Mech checkout: protein slots, PathwayMech links, errors.

    With ``ref``, records are read from that commit's git objects instead of the
    working tree. With ``spec.prefilter``, a file is parsed only when its text
    names one of ``prefilter_terms`` (PathwayMech accessions) or PathwayMech
    itself. This selects an accession-overlap and link subset; reaction-only
    leads outside that subset remain unknown.
    """
    loader = loader or _load_yaml
    proteins: list[SiblingProtein] = []
    links: list[SiblingLink] = []
    errors: list[str] = []
    coverage = coverage if coverage is not None else ScanCoverage()
    coverage.scope = "accession-prefiltered" if spec.prefilter else "full"
    terms = sorted(set(prefilter_terms))
    screen = re.compile("|".join(re.escape(term) for term in terms)) if terms else None

    def selected(text: str) -> bool:
        # Keep the literal corpus marker separate: mixing an ignore-case
        # alternative into hundreds of accessions disables the regex fast path.
        return ("pathwaymech" in text.casefold()
                or (screen is not None and screen.search(text) is not None))
    if ref is None:
        sources: Iterable[tuple[str, Any]] = (
            (path.relative_to(root).as_posix(), path) for path in sibling_files(root, spec))
    else:
        sources = git_documents(root, ref, spec)
    for relative, source in sources:
        coverage.files_seen += 1
        try:
            if isinstance(source, bytes):
                text = source.decode("utf-8")
                if spec.prefilter and not selected(text):
                    coverage.files_filtered += 1
                    continue
                document = yaml.load(text, Loader=_YAML_LOADER)  # noqa: S506 - safe loader
            else:
                if spec.prefilter and not selected(source.read_text(encoding="utf-8")):
                    coverage.files_filtered += 1
                    continue
                document = loader(source)
        except (OSError, UnicodeDecodeError, yaml.YAMLError, ValueError, TypeError,
                RecursionError) as error:
            coverage.unreadable_files += 1
            errors.append(f"{spec.name}:{relative}: unreadable: {error}")
            continue
        if not isinstance(document, dict):
            coverage.unreadable_files += 1
            errors.append(f"{spec.name}:{relative}: expected a YAML record mapping")
            continue
        coverage.files_parsed += 1
        record_id = str(document.get(spec.id_key, ""))
        record_label = str(document.get(spec.label_key, ""))
        for slot in spec.protein_slots:
            for concrete, value in walk_path(document, slot.path):
                accession = normalize_accession(value)
                if accession:
                    proteins.append(
                        SiblingProtein(spec.name, relative, record_id, record_label, concrete,
                                       slot.role, accession)
                    )
                elif value not in (None, "") and not slot.mixed:
                    errors.append(f"{spec.name}:{relative}:{concrete}: not a UniProtKB "
                                  f"accession: {value!r}")
        seen: set[tuple[str, str]] = set()
        for slot in spec.link_slots:
            for concrete, value in walk_path(document, slot.path):
                if isinstance(value, dict):
                    if not slot.selects(value):
                        continue
                    target = value.get(slot.id_key) if slot.id_key else None
                    label = value.get(slot.label_key) if slot.label_key else None
                else:
                    target, label = value, None
                if isinstance(target, str) and target.strip():
                    seen.add((concrete, target))
                    links.append(SiblingLink(spec.name, relative, record_id, record_label,
                                             concrete, target.strip(),
                                             label if isinstance(label, str) else None))
                else:
                    errors.append(f"{spec.name}:{relative}:{concrete}: "
                                  "configured PathwayMech link has no nonempty string target")
        # A page URL written anywhere else in the record is still a PathwayMech link.
        for concrete, value in _strings(document, ""):
            for match in PATHWAYMECH_URL.finditer(value):
                if not any(concrete.startswith(slot_path) for slot_path, _ in seen):
                    target = match.group(0).rstrip(".,;:)]}")
                    links.append(SiblingLink(spec.name, relative, record_id, record_label,
                                             concrete, target, None))
    if coverage.files_seen == 0:
        errors.append(f"{spec.name}: no records match configured globs: {spec.records!r}")
    coverage.errors = len(errors)
    if errors:
        coverage.status = "incomplete"
    return proteins, links, errors


def _strings(node: Any, prefix: str) -> Iterator[tuple[str, str]]:
    if isinstance(node, dict):
        for key, value in node.items():
            yield from _strings(value, f"{prefix}.{key}" if prefix else str(key))
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from _strings(value, f"{prefix}[{i}]")
    elif isinstance(node, str):
        yield prefix, node


_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def _load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as stream:
        return yaml.load(stream, Loader=_YAML_LOADER)  # noqa: S506 - safe loader


# --------------------------------------------------------------------------
# Joins
# --------------------------------------------------------------------------


@dataclass
class Report:
    mechs: list[str]
    sibling_proteins: list[SiblingProtein]
    links: list[SiblingLink]
    errors: list[str]
    overlaps: list[dict[str, Any]]
    link_checks: list[dict[str, Any]]
    reaction_matches: list[dict[str, Any]]
    example_candidates: list[dict[str, Any]]
    unmapped_sgd: list[str]
    coverage: dict[str, ScanCoverage] = field(default_factory=dict)
    rhea_normalized: bool = False

    @property
    def broken_links(self) -> list[dict[str, Any]]:
        return [row for row in self.link_checks if row["status"] != "ok"]


def build_report(
    index: PathwayIndex,
    scans: dict[str, tuple[list[SiblingProtein], list[SiblingLink], list[str]]],
    annotations: dict[str, dict[str, list[str]]] | None = None,
    *,
    coverage: dict[str, ScanCoverage] | None = None,
    rhea_normalized: bool = False,
) -> Report:
    """Join sibling inventories with the PathwayMech index."""
    annotations = annotations or {}
    validate_annotations(annotations)
    proteins = [protein for found, _, _ in scans.values() for protein in found]
    for mech, details in (coverage or {}).items():
        accessions = {protein.accession for protein in proteins if protein.mech == mech}
        details.distinct_accessions = len(accessions)
        details.annotated_accessions = len(accessions & annotations.keys())
    links = [link for _, found, _ in scans.values() for link in found]
    errors = [error for _, _, found in scans.values() for error in found]

    linked: dict[tuple[str, str], set[str]] = defaultdict(set)
    link_checks = []
    for link in links:
        resolved = resolve_target(index, link.target)
        if resolved is None:
            status = "unknown_record"
        elif link.label is not None and link.label.casefold() != index.labels[resolved].casefold():
            status = "label_mismatch"
        else:
            status = "ok"
        if resolved:
            linked[(link.mech, link.file)].add(resolved)
        link_checks.append({**asdict(link), "resolved_record": resolved or "",
                            "pathwaymech_label": index.labels.get(resolved or "", ""),
                            "status": status})

    overlaps = []
    for protein in proteins:
        for pathway in index.proteins.get(protein.accession, []):
            overlaps.append({
                **asdict(protein),
                "pathway_record": pathway.record_id,
                "pathway_label": pathway.record_label,
                "pathway_participant": pathway.participant_id,
                "pathway_url": record_url(pathway.record_id),
                "record_links_pathway": pathway.record_id in linked[(protein.mech, protein.file)],
            })

    reaction_matches = []
    for protein in proteins:
        direct_records = set(index.records_for(protein.accession))
        annotation = annotations.get(protein.accession) or {}
        rhea = master_ids(annotation.get("rhea", []), index.rhea_directions)
        ec = {value for value in annotation.get("ec", []) if _COMPLETE_EC.match(value)}
        if not rhea and not ec:
            continue
        for record_id in sorted(index.labels):
            if record_id in direct_records:
                continue
            stated_rhea = rhea & index.rhea.get(record_id, set())
            stated_ec = ec & index.ec.get(record_id, set())
            via_rhea = (rhea & index.participant_rhea.get(record_id, set())) - stated_rhea
            via_ec = (ec & index.participant_ec.get(record_id, set())) - stated_ec
            if not (stated_rhea or stated_ec or via_rhea or via_ec):
                continue
            # Strongest basis first: a shared Rhea reaction pins the chemistry;
            # a complete EC number only the activity class.
            if stated_rhea or via_rhea:
                basis = "record_rhea" if stated_rhea else "participant_rhea"
            else:
                basis = "record_ec" if stated_ec else "participant_ec"
            reaction_matches.append({
                **asdict(protein),
                "pathway_record": record_id,
                "pathway_label": index.labels[record_id],
                "shared_rhea": ";".join(f"RHEA:{value}" for value in
                                        sorted(stated_rhea | via_rhea)),
                "shared_ec": ";".join(f"EC:{value}" for value in sorted(stated_ec | via_ec)),
                "basis": basis,
                "record_links_pathway": record_id in linked[(protein.mech, protein.file)],
            })

    held: dict[str, set[str]] = defaultdict(set)
    for protein in proteins:
        held[protein.mech].add(protein.accession)
    pathways_by_mech: dict[str, set[str]] = defaultdict(set)
    for (mech, _), records in linked.items():
        pathways_by_mech[mech].update(records)
    for row in overlaps:
        pathways_by_mech[row["mech"]].add(row["pathway_record"])
    candidates = []
    for mech in sorted(pathways_by_mech):
        for record_id in sorted(pathways_by_mech[mech]):
            for accession, entries in sorted(index.proteins.items()):
                for entry in entries:
                    if entry.record_id == record_id and accession not in held[mech]:
                        candidates.append({
                            "mech": mech,
                            "pathway_record": record_id,
                            "pathway_label": entry.record_label,
                            "accession": accession,
                            "participant_id": entry.participant_id,
                            "participant_label": entry.participant_label,
                        })
    return Report(
        mechs=sorted(scans),
        sibling_proteins=proteins,
        links=links,
        errors=errors,
        overlaps=overlaps,
        link_checks=link_checks,
        reaction_matches=reaction_matches,
        example_candidates=candidates,
        unmapped_sgd=sorted(index.unmapped_sgd),
        coverage=coverage or {},
        rhea_normalized=rhea_normalized,
    )


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------


def overlap_pairs(report: Report) -> list[dict[str, Any]]:
    """One row per (sibling record, PathwayMech record) sharing a protein."""
    pairs: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in report.overlaps:
        key = (row["mech"], row["file"], row["pathway_record"])
        pair = pairs.setdefault(key, {
            "mech": row["mech"], "file": row["file"], "record_id": row["record_id"],
            "record_label": row["record_label"], "pathway_record": row["pathway_record"],
            "pathway_label": row["pathway_label"], "accessions": set(), "roles": set(),
            "slot_values": 0, "record_links_pathway": row["record_links_pathway"],
        })
        pair["accessions"].add(row["accession"])
        pair["roles"].add(row["role"])
        pair["slot_values"] += 1
    rows = []
    for key in sorted(pairs):
        pair = pairs[key]
        rows.append({**pair, "accessions": ";".join(sorted(pair["accessions"])),
                     "roles": ";".join(sorted(pair["roles"]))})
    return rows


def write_report(report: Report, out: Path, full: bool = False) -> list[Path]:
    """Write TSV tables and a Markdown summary; return the paths written.

    The per-slot tables (``sibling_proteins.tsv``, ``overlaps.tsv``) can run to
    megabytes for a large corpus, so they are written only with ``full``; the
    aggregated ``pairs.tsv`` carries the same joins one row per record pair.
    """
    out.mkdir(parents=True, exist_ok=True)
    tables: dict[str, list[dict[str, Any]]] = {
        "pairs.tsv": overlap_pairs(report),
        "link_checks.tsv": report.link_checks,
        "reaction_matches.tsv": report.reaction_matches,
        "example_candidates.tsv": report.example_candidates,
        "coverage.tsv": [{"mech": mech, **asdict(coverage)}
                         for mech, coverage in sorted(report.coverage.items())],
    }
    if full:
        tables["sibling_proteins.tsv"] = [asdict(row) for row in report.sibling_proteins]
        tables["overlaps.tsv"] = report.overlaps
    else:
        for name in ("sibling_proteins.tsv", "overlaps.tsv"):
            (out / name).unlink(missing_ok=True)
    written = []
    for name, rows in tables.items():
        path = out / name
        _write_tsv(path, rows, TABLE_COLUMNS[name])
        written.append(path)
    summary = out / "summary.md"
    summary.write_text(render_summary(report), encoding="utf-8")
    written.append(summary)
    return written


_PROTEIN_COLUMNS = [item.name for item in fields(SiblingProtein)]
TABLE_COLUMNS = {
    "pairs.tsv": ["mech", "file", "record_id", "record_label", "pathway_record",
                  "pathway_label", "accessions", "roles", "slot_values", "record_links_pathway"],
    "link_checks.tsv": [item.name for item in fields(SiblingLink)] + [
        "resolved_record", "pathwaymech_label", "status"],
    "reaction_matches.tsv": _PROTEIN_COLUMNS + ["pathway_record", "pathway_label", "shared_rhea",
                                               "shared_ec", "basis", "record_links_pathway"],
    "example_candidates.tsv": ["mech", "pathway_record", "pathway_label", "accession",
                               "participant_id", "participant_label"],
    "sibling_proteins.tsv": _PROTEIN_COLUMNS,
    "overlaps.tsv": _PROTEIN_COLUMNS + ["pathway_record", "pathway_label", "pathway_participant",
                                       "pathway_url", "record_links_pathway"],
    "coverage.tsv": ["mech"] + [item.name for item in fields(ScanCoverage)],
}


def _write_tsv(path: Path, rows: list[dict[str, Any]], columns: list[str]) -> None:
    columns = list(columns)
    for row in rows:
        columns.extend(key for key in row if key not in columns)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t",
                                lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


SUMMARY_LIST_LIMIT = 25


def render_summary(report: Report, list_limit: int = SUMMARY_LIST_LIMIT) -> str:
    lines = ["# Cross-Mech protein inventory", ""]
    if report.coverage:
        lines += ["## Coverage", "",
                  "Counts below describe the parsed records. An accession-prefiltered scan "
                  "is not a complete sibling protein inventory; reaction-only matches, "
                  "held proteins and example availability outside that subset are unknown.", "",
                  "| Mech | Scope | Status | Files considered | Parsed | Filtered out "
                  "| Unreadable | Errors | Accessions annotated / held |",
                  "|---|---|---|---:|---:|---:|---:|---:|---:|",]
        for mech, coverage in sorted(report.coverage.items()):
            lines.append(f"| {mech} | {coverage.scope} | {coverage.status} "
                         f"| {coverage.files_seen} | {coverage.files_parsed} "
                         f"| {coverage.files_filtered} | {coverage.unreadable_files} "
                         f"| {coverage.errors} | {coverage.annotated_accessions} / "
                         f"{coverage.distinct_accessions} |")
        lines += ["", "Missing annotation entries are unknown, not negative reaction evidence."]
        lines += ["", "Rhea comparisons normalize covered directional identifiers to their "
                  "master reaction using the supplied mapping." if report.rhea_normalized else
                  "Rhea comparisons use identifiers as supplied; no direction mapping was loaded.",
                  "", "## Protein and link counts", ""]
    lines.append("| Mech | Protein slot values | Distinct accessions | In a PathwayMech pathway "
                 "| Record-pathway pairs | Unlinked pairs | PathwayMech links | Broken links |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    pairs = overlap_pairs(report)
    for mech in report.mechs:
        values = [row for row in report.sibling_proteins if row.mech == mech]
        overlap = {row["accession"] for row in report.overlaps if row["mech"] == mech}
        mech_pairs = [row for row in pairs if row["mech"] == mech]
        unlinked = [row for row in mech_pairs if not row["record_links_pathway"]]
        links = [row for row in report.link_checks if row["mech"] == mech]
        broken = [row for row in links if row["status"] != "ok"]
        lines.append(f"| {mech} | {len(values)} | {len({row.accession for row in values})} "
                     f"| {len(overlap)} | {len(mech_pairs)} | {len(unlinked)} | {len(links)} "
                     f"| {len(broken)} |")
    lines += ["", "## Unlinked record-pathway pairs", "",
              "A sibling record holds a protein of a PathwayMech pathway but does not link "
              "that pathway. Whether it should depends on what the record is: a pathway or "
              "activity trait usually should, a domain or family trait usually should not. "
              f"At most {list_limit} pairs per Mech are listed; `pairs.tsv` has all of them.", ""]
    for mech in report.mechs:
        unlinked = [row for row in pairs if row["mech"] == mech and not row["record_links_pathway"]]
        for row in unlinked[:list_limit]:
            lines.append(f"- {mech} `{row['record_id']}` ({row['record_label']}) -> "
                         f"`{row['pathway_record']}` via {row['accessions']}")
        if len(unlinked) > list_limit:
            lines.append(f"- {mech}: {len(unlinked) - list_limit} more pairs not listed here")
    if report.broken_links:
        lines += ["", "## Broken PathwayMech links", ""]
        for row in report.broken_links:
            lines.append(f"- {row['mech']} `{row['file']}` {row['slot']}: `{row['target']}` "
                         f"({row['status']})")
    if report.unmapped_sgd:
        lines += ["", f"SGD participants without a UniProtKB mapping: "
                  f"{', '.join(report.unmapped_sgd)}."]
    if report.errors:
        lines += ["", "## Inventory errors", ""]
        lines.extend(f"- {error}" for error in report.errors)
    lines += ["", "Every row is a curation lead. A shared accession shows pathway "
              "participation, not that the sibling record's claim concerns that pathway.", ""]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# UniProt inputs (anonymous REST; never part of validation)
# --------------------------------------------------------------------------

Fetcher = Callable[[str], str]


def _http_get(url: str) -> str:
    request = urllib.request.Request(url, headers={"Accept": "text/plain"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:  # noqa: S310
                return response.read().decode("utf-8")
        except OSError:
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))
    raise AssertionError("unreachable")


def _uniprot_rows(text: str, columns: set[str]) -> Iterator[dict[str, str]]:
    """Reject transport/error pages and malformed rows before publishing inputs."""
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    if (not reader.fieldnames or set(reader.fieldnames) != columns
            or len(reader.fieldnames) != len(columns)):
        raise ValueError("unexpected UniProt TSV headers")
    seen = set()
    for row in reader:
        if None in row or any(value is None for value in row.values()):
            raise ValueError("malformed UniProt TSV row")
        accession = row["Entry"]
        if not accession or normalize_accession(accession) != accession or accession in seen:
            raise ValueError(f"invalid or duplicate UniProt TSV accession: {accession!r}")
        seen.add(accession)
        yield row


def validate_sgd_map(mapping: dict) -> None:
    for identifier, accessions in mapping.items():
        if (not isinstance(identifier, str) or not re.fullmatch(r"SGD:S\d{9}", identifier)
                or not isinstance(accessions, list)
                or any(not isinstance(value, str) or not value
                       or normalize_accession(value) != value for value in accessions)):
            raise ValueError(f"invalid SGD-to-UniProt mapping: {identifier!r}")


def validate_annotations(annotations: dict) -> None:
    for accession, annotation in annotations.items():
        if (not isinstance(accession, str) or not accession
                or normalize_accession(accession) != accession or not isinstance(annotation, dict)
                or any(not isinstance(values, list)
                       or any(not isinstance(value, str) for value in values)
                       for values in annotation.values())
                or any(not re.fullmatch(r"(?:RHEA:)?\d+", value)
                       for value in annotation.get("rhea", []))):
            raise ValueError(f"invalid UniProt annotation mapping: {accession!r}")


def fetch_sgd_uniprot_map(fetch: Fetcher = _http_get) -> dict[str, list[str]]:
    """Map SGD gene ids to reviewed S. cerevisiae S288C UniProtKB accessions."""
    query = urllib.parse.urlencode({
        "query": "(organism_id:559292) AND (reviewed:true)",
        "fields": "accession,xref_sgd",
        "format": "tsv",
    })
    mapping: dict[str, list[str]] = defaultdict(list)
    for row in _uniprot_rows(fetch(f"{UNIPROT_REST}?{query}"), {"Entry", "SGD"}):
        for sgd in (row.get("SGD") or "").split(";"):
            sgd = sgd.strip()
            if sgd:
                mapping[f"SGD:{sgd}"].append(row["Entry"])
    result = {key: sorted(set(values)) for key, values in sorted(mapping.items())}
    validate_sgd_map(result)
    return result


def fetch_uniprot_annotations(
    accessions: Iterable[str], fetch: Fetcher = _http_get, batch: int = 90
) -> dict[str, dict[str, list[str]]]:
    """Rhea, EC and pathway annotations for accessions that UniProt still serves."""
    wanted = sorted(set(accessions))
    if batch < 1 or any(not value or normalize_accession(value) != value for value in wanted):
        raise ValueError("annotation queries require valid accessions and a positive batch size")
    annotations: dict[str, dict[str, list[str]]] = {}
    for start in range(0, len(wanted), batch):
        chunk = wanted[start:start + batch]
        query = urllib.parse.urlencode({
            "query": " OR ".join(f"accession:{accession}" for accession in chunk),
            "fields": "accession,reviewed,organism_id,ec,rhea,cc_pathway",
            "format": "tsv",
        })
        for row in _uniprot_rows(fetch(f"{UNIPROT_REST}?{query}"), {
            "Entry", "Reviewed", "Organism (ID)", "EC number", "Rhea ID", "Pathway",
        }):
            if row["Entry"] not in chunk:
                raise ValueError("UniProt returned an accession outside the requested batch")
            if (row["Reviewed"] not in {"reviewed", "unreviewed"}
                    or not row["Organism (ID)"].isdigit()):
                raise ValueError("invalid UniProt review status or organism identifier")
            annotations[row["Entry"]] = {
                "reviewed": [row.get("Reviewed", "")],
                "organism": [row.get("Organism (ID)", "")],
                "ec": [value.strip() for value in (row.get("EC number") or "").split(";")
                       if value.strip()],
                "rhea": [value.strip() for value in (row.get("Rhea ID") or "").split()
                         if value.strip()],
                "pathway": [row.get("Pathway", "").strip()] if row.get("Pathway") else [],
            }
    validate_annotations(annotations)
    return annotations


def load_json(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------


def main(argv: list[str] | None, root: Path) -> int:
    import argparse

    from pathwaymech.yaml_io import load_yaml_file, pathway_files

    parser = argparse.ArgumentParser(
        prog="pathwaymech-cross-mech-proteins",
        description=(
            "Inventory UniProt proteins in sibling Mech checkouts, join them with "
            "PathwayMech pathway participants, and check sibling PathwayMech links. "
            "Reads local files only, unless a --fetch option asks UniProt (anonymously)."
        ),
    )
    parser.add_argument("--config", type=Path, default=root / "conf" / "sibling_mechs.yaml")
    parser.add_argument("--mechs-root", type=Path,
                        help="directory holding sibling checkouts, one per Mech name")
    parser.add_argument("--mech", action="append", default=[], metavar="NAME=PATH",
                        help="checkout of one sibling Mech (overrides --mechs-root)")
    parser.add_argument("--only", action="append", default=[], metavar="NAME",
                        help="restrict the inventory to these Mechs")
    parser.add_argument("--ref", metavar="REF",
                        help="read sibling records from this git ref (e.g. origin/main) "
                             "instead of the working tree")
    parser.add_argument("--sgd-map", type=Path,
                        help="JSON map of SGD ids to UniProtKB accessions")
    parser.add_argument("--fetch-sgd-map", action="store_true",
                        help="rebuild --sgd-map from UniProtKB SGD cross-references")
    parser.add_argument("--annotations", type=Path,
                        help="JSON UniProt annotations (Rhea, EC) for sibling and "
                             "PathwayMech accessions")
    parser.add_argument("--fetch-annotations", action="store_true",
                        help="fetch --annotations for every sibling and PathwayMech "
                             "accession from UniProt")
    parser.add_argument("--rhea-directions", type=Path,
                        help="JSON directional-to-master Rhea mapping "
                             "(defaults to conf/rhea_directions.json when available)")
    parser.add_argument("--out", type=Path, help="write TSV tables and summary.md here")
    parser.add_argument("--full-tables", action="store_true",
                        help="also write the per-slot sibling_proteins.tsv and overlaps.tsv")
    parser.add_argument("--check-links", action="store_true",
                        help="exit nonzero for unresolved links or mismatched labels "
                             "or a selected sibling checkout could not be checked")
    args = parser.parse_args(argv)

    if (args.fetch_sgd_map and not args.sgd_map) or (args.fetch_annotations
                                                       and not args.annotations):
        parser.error("--fetch-sgd-map needs --sgd-map; --fetch-annotations needs --annotations")
    try:
        specs = load_config(args.config)
    except (OSError, ValueError, yaml.YAMLError) as error:
        parser.error(str(error))
    overrides = {}
    for value in args.mech:
        name, sep, path = value.partition("=")
        if not sep or not path:
            parser.error(f"--mech expects NAME=PATH, got {value!r}")
        overrides[name] = Path(path)
    unknown_overrides = sorted(set(overrides) - {spec.name for spec in specs})
    if unknown_overrides:
        parser.error(f"--mech names Mechs missing from {args.config}: "
                     f"{', '.join(unknown_overrides)}")
    if args.only:
        unknown = sorted(set(args.only) - {spec.name for spec in specs})
        if unknown:
            parser.error(f"--only names Mechs missing from {args.config}: {', '.join(unknown)}")
        specs = [spec for spec in specs if spec.name in args.only]

    try:
        sgd_map = {} if args.fetch_sgd_map else load_json(args.sgd_map)
        annotations = {} if args.fetch_annotations else load_json(args.annotations)
        validate_sgd_map(sgd_map)
        validate_annotations(annotations)
        from pathwaymech.rhea_directions import load_rhea_directions

        rhea_path = args.rhea_directions
        if rhea_path is None and (root / "conf" / "rhea_directions.json").exists():
            rhea_path = root / "conf" / "rhea_directions.json"
        rhea_directions = load_rhea_directions(rhea_path) if rhea_path is not None else {}
    except (OSError, ValueError) as error:
        parser.error(str(error))

    if args.fetch_sgd_map:
        try:
            sgd_map = fetch_sgd_uniprot_map()
        except (OSError, ValueError) as error:
            parser.error(str(error))
    records = [load_yaml_file(path) for path in pathway_files(root / "data" / "pathways")]
    if not records:
        parser.error("no PathwayMech records found in data/pathways")
    index = build_pathway_index(records, sgd_map, rhea_directions=rhea_directions)

    scans = {}
    coverage = {}
    missing_required = []
    for spec in specs:
        coverage[spec.name] = ScanCoverage(
            scope="accession-prefiltered" if spec.prefilter else "full",
            source=f"ref {args.ref}" if args.ref else "working tree",
        )
        checkout = overrides.get(spec.name) or (args.mechs_root / spec.name
                                                if args.mechs_root else None)
        if checkout is None or not checkout.is_dir():
            coverage[spec.name].status = "missing checkout"
            if args.check_links or spec.name in overrides or spec.name in args.only:
                missing_required.append(spec.name)
            print(f"skipped {spec.name}: no checkout (pass --mechs-root or --mech)",
                  file=sys.stderr)
            continue
        coverage[spec.name].commit = commit_of(checkout, args.ref or "HEAD")
        try:
            scans[spec.name] = scan_sibling(checkout, spec, prefilter_terms=index.proteins,
                                            ref=args.ref, coverage=coverage[spec.name])
        except OSError as error:
            coverage[spec.name].status = "incomplete"
            coverage[spec.name].errors += 1
            scans[spec.name] = ([], [], [f"{spec.name}: {error}"])
        print(f"read {spec.name} at {coverage[spec.name].commit or 'unknown'}"
              f" ({'ref ' + args.ref if args.ref else 'working tree'})", file=sys.stderr)
    if not scans:
        print("no sibling checkout was found; nothing to inventory", file=sys.stderr)
        return 2

    if args.fetch_annotations:
        accessions = {protein.accession for found, _, _ in scans.values() for protein in found}
        accessions.update(index.proteins)
        try:
            annotations = fetch_uniprot_annotations(accessions)
        except (OSError, ValueError) as error:
            parser.error(str(error))
    if annotations:
        index = build_pathway_index(records, sgd_map, annotations,
                                    rhea_directions=rhea_directions)
    report = build_report(index, scans, annotations, coverage=coverage,
                          rhea_normalized=bool(rhea_directions))
    if report.errors or missing_required:
        print(render_summary(report))
        print("inventory is incomplete: "
              f"{len(report.errors)} scan error(s), "
              f"{len(missing_required)} required checkout(s) unavailable", file=sys.stderr)
        return 1
    if args.check_links and report.broken_links:
        print(render_summary(report))
        print(f"{len(report.broken_links)} sibling PathwayMech link(s) failed validation "
              "(unknown record or label mismatch)",
              file=sys.stderr)
        return 1
    if args.fetch_sgd_map:
        _write_json(args.sgd_map, sgd_map)
        print(f"wrote {args.sgd_map}")
    if args.fetch_annotations:
        _write_json(args.annotations, annotations)
        print(f"wrote {args.annotations}")
    if args.out:
        for path in write_report(report, args.out, full=args.full_tables):
            print(f"wrote {path}")
    else:
        print(render_summary(report))
    return 0
