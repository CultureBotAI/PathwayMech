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
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import yaml

PATHWAYMECH_RECORD_URL = "https://culturebotai.github.io/PathwayMech/pages/records/{slug}.html"
# Matches a link to a PathwayMech record page wherever a sibling writes one.
PATHWAYMECH_URL = re.compile(
    r"https?://culturebotai\.github\.io/PathwayMech/pages/records/([A-Za-z0-9._~%-]+)\.html"
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
    protein and activity participants and reaction ids, so a sibling can also
    confirm that a linked protein is a participant. It is rendered with the
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

    def records_for(self, accession: str) -> list[str]:
        return sorted({protein.record_id for protein in self.proteins.get(accession, [])})


def build_pathway_index(
    records: Iterable[dict[str, Any]],
    sgd_to_uniprot: dict[str, list[str]] | None = None,
    annotations: dict[str, dict[str, list[str]]] | None = None,
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
    index = PathwayIndex()
    proteins: dict[str, list[PathwayProtein]] = defaultdict(list)
    for record in records:
        record_id = record["id"]
        index.labels[record_id] = record["label"]
        index.slugs[record_slug(record_id).casefold()] = record_id
        index.rhea[record_id] = {
            reaction["id"].split(":", 1)[1]
            for reaction in record.get("reactions") or []
            if str(reaction.get("id", "")).startswith("RHEA:")
        }
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
        rhea = {value.split(":")[-1] for value in annotation.get("rhea", [])}
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
    match = PATHWAYMECH_URL.search(target)
    slug = urllib.parse.unquote(match.group(1)) if match else target
    return index.slugs.get(slug.casefold())


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
    names = [name for name in _git(root, "ls-tree", "-r", "-z", "--name-only", commit)
             .decode("utf-8").split("\0") if name and any(p.match(name) for p in patterns)]
    names.sort()
    for start in range(0, len(names), 2000):
        chunk = names[start:start + 2000]
        request = "".join(f"{commit}:{name}\n" for name in chunk).encode("utf-8")
        stream = _git(root, "cat-file", "--batch", data=request)
        offset = 0
        for name in chunk:
            header_end = stream.index(b"\n", offset)
            header = stream[offset:header_end].split()
            if len(header) != 3 or header[1] != b"blob":
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
) -> tuple[list[SiblingProtein], list[SiblingLink], list[str]]:
    """Inventory one sibling Mech checkout: protein slots, PathwayMech links, errors.

    With ``ref``, records are read from that commit's git objects instead of the
    working tree. With ``spec.prefilter``, a file is parsed only when its text
    names one of ``prefilter_terms`` (PathwayMech accessions) or PathwayMech
    itself, so the inventory of a very large corpus is restricted to what can join.
    """
    loader = loader or _load_yaml
    proteins: list[SiblingProtein] = []
    links: list[SiblingLink] = []
    errors: list[str] = []
    terms = sorted(set(prefilter_terms))
    screen = (re.compile("|".join(["PathwayMech", "PATHWAYMECH",
                                   *(re.escape(term) for term in terms)]))
              if spec.prefilter else None)
    if ref is None:
        sources: Iterable[tuple[str, Any]] = (
            (path.relative_to(root).as_posix(), path) for path in sibling_files(root, spec))
    else:
        sources = git_documents(root, ref, spec)
    for relative, source in sources:
        try:
            if isinstance(source, bytes):
                text = source.decode("utf-8")
                if screen is not None and not screen.search(text):
                    continue
                document = yaml.load(text, Loader=_YAML_LOADER)  # noqa: S506 - safe loader
            else:
                if screen is not None and not screen.search(source.read_text(encoding="utf-8")):
                    continue
                document = loader(source)
        except (OSError, UnicodeDecodeError, yaml.YAMLError) as error:
            errors.append(f"{spec.name}:{relative}: unreadable: {error}")
            continue
        if not isinstance(document, dict):
            continue
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
        # A page URL written anywhere else in the record is still a PathwayMech link.
        for concrete, value in _strings(document, ""):
            for match in PATHWAYMECH_URL.finditer(value):
                if not any(concrete.startswith(slot_path) for slot_path, _ in seen):
                    links.append(SiblingLink(spec.name, relative, record_id, record_label,
                                             concrete, match.group(0), None))
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

    @property
    def broken_links(self) -> list[dict[str, Any]]:
        return [row for row in self.link_checks if row["status"] != "ok"]


def build_report(
    index: PathwayIndex,
    scans: dict[str, tuple[list[SiblingProtein], list[SiblingLink], list[str]]],
    annotations: dict[str, dict[str, list[str]]] | None = None,
) -> Report:
    """Join sibling inventories with the PathwayMech index."""
    annotations = annotations or {}
    proteins = [protein for found, _, _ in scans.values() for protein in found]
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
        if protein.accession in index.proteins:
            continue
        annotation = annotations.get(protein.accession) or {}
        rhea = {value.split(":")[-1] for value in annotation.get("rhea", [])}
        ec = {value for value in annotation.get("ec", []) if _COMPLETE_EC.match(value)}
        if not rhea and not ec:
            continue
        for record_id in sorted(index.labels):
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
    }
    if full:
        tables["sibling_proteins.tsv"] = [asdict(row) for row in report.sibling_proteins]
        tables["overlaps.tsv"] = report.overlaps
    written = []
    for name, rows in tables.items():
        path = out / name
        _write_tsv(path, rows)
        written.append(path)
    summary = out / "summary.md"
    summary.write_text(render_summary(report), encoding="utf-8")
    written.append(summary)
    return written


def _write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    columns: list[str] = []
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


def fetch_sgd_uniprot_map(fetch: Fetcher = _http_get) -> dict[str, list[str]]:
    """Map SGD gene ids to reviewed S. cerevisiae S288C UniProtKB accessions."""
    query = urllib.parse.urlencode({
        "query": "(organism_id:559292) AND (reviewed:true)",
        "fields": "accession,xref_sgd",
        "format": "tsv",
    })
    mapping: dict[str, list[str]] = defaultdict(list)
    for row in csv.DictReader(io.StringIO(fetch(f"{UNIPROT_REST}?{query}")), delimiter="\t"):
        for sgd in (row.get("SGD") or "").split(";"):
            sgd = sgd.strip()
            if sgd:
                mapping[f"SGD:{sgd}"].append(row["Entry"])
    return {key: sorted(set(values)) for key, values in sorted(mapping.items())}


def fetch_uniprot_annotations(
    accessions: Iterable[str], fetch: Fetcher = _http_get, batch: int = 90
) -> dict[str, dict[str, list[str]]]:
    """Rhea, EC and pathway annotations for accessions that UniProt still serves."""
    wanted = sorted(set(accessions))
    annotations: dict[str, dict[str, list[str]]] = {}
    for start in range(0, len(wanted), batch):
        chunk = wanted[start:start + batch]
        query = urllib.parse.urlencode({
            "query": " OR ".join(f"accession:{accession}" for accession in chunk),
            "fields": "accession,reviewed,organism_id,ec,rhea,cc_pathway",
            "format": "tsv",
        })
        for row in csv.DictReader(io.StringIO(fetch(f"{UNIPROT_REST}?{query}")),
                                  delimiter="\t"):
            annotations[row["Entry"]] = {
                "reviewed": [row.get("Reviewed", "")],
                "organism": [row.get("Organism (ID)", "")],
                "ec": [value.strip() for value in (row.get("EC number") or "").split(";")
                       if value.strip()],
                "rhea": [value.strip() for value in (row.get("Rhea ID") or "").split()
                         if value.strip()],
                "pathway": [row.get("Pathway", "").strip()] if row.get("Pathway") else [],
            }
    return annotations


def load_json(path: Path | None) -> dict[str, Any]:
    if path is None or not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


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
    parser.add_argument("--out", type=Path, help="write TSV tables and summary.md here")
    parser.add_argument("--full-tables", action="store_true",
                        help="also write the per-slot sibling_proteins.tsv and overlaps.tsv")
    parser.add_argument("--check-links", action="store_true",
                        help="exit 1 when a sibling PathwayMech link does not resolve")
    args = parser.parse_args(argv)

    if (args.fetch_sgd_map and not args.sgd_map) or (args.fetch_annotations
                                                       and not args.annotations):
        parser.error("--fetch-sgd-map needs --sgd-map; --fetch-annotations needs --annotations")
    specs = load_config(args.config)
    overrides = {}
    for value in args.mech:
        name, sep, path = value.partition("=")
        if not sep or not path:
            parser.error(f"--mech expects NAME=PATH, got {value!r}")
        overrides[name] = Path(path)
    if args.only:
        unknown = sorted(set(args.only) - {spec.name for spec in specs})
        if unknown:
            parser.error(f"--only names Mechs missing from {args.config}: {', '.join(unknown)}")
        specs = [spec for spec in specs if spec.name in args.only]

    if args.fetch_sgd_map:
        _write_json(args.sgd_map, fetch_sgd_uniprot_map())
        print(f"wrote {args.sgd_map}")
    records = [load_yaml_file(path) for path in pathway_files(root / "data" / "pathways")]
    index = build_pathway_index(records, load_json(args.sgd_map))

    scans = {}
    for spec in specs:
        checkout = overrides.get(spec.name) or (args.mechs_root / spec.name
                                                if args.mechs_root else None)
        if checkout is None or not checkout.is_dir():
            print(f"skipped {spec.name}: no checkout (pass --mechs-root or --mech)",
                  file=sys.stderr)
            continue
        scans[spec.name] = scan_sibling(checkout, spec, prefilter_terms=index.proteins,
                                        ref=args.ref)
        print(f"read {spec.name} at {commit_of(checkout, args.ref or 'HEAD') or 'unknown'}"
              f" ({'ref ' + args.ref if args.ref else 'working tree'})", file=sys.stderr)
    if not scans:
        print("no sibling checkout was found; nothing to inventory", file=sys.stderr)
        return 2

    if args.fetch_annotations:
        accessions = {protein.accession for found, _, _ in scans.values() for protein in found}
        accessions.update(index.proteins)
        _write_json(args.annotations, fetch_uniprot_annotations(accessions))
        print(f"wrote {args.annotations}")
    annotations = load_json(args.annotations)
    if annotations:
        index = build_pathway_index(records, load_json(args.sgd_map), annotations)
    report = build_report(index, scans, annotations)
    if args.out:
        for path in write_report(report, args.out, full=args.full_tables):
            print(f"wrote {path}")
    else:
        print(render_summary(report))
    if args.check_links and report.broken_links:
        print(f"{len(report.broken_links)} sibling PathwayMech link(s) do not resolve",
              file=sys.stderr)
        return 1
    return 0
