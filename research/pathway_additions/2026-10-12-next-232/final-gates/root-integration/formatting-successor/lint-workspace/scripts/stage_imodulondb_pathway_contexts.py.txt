#!/usr/bin/env python3
"""Stage exact iModulonDB-to-PathwayMech protein participant matches."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml

UNIPROT_ACCESSION = re.compile(
    r"^(?:[A-NR-Z][0-9][A-Z][A-Z0-9]{2}[0-9]|[OPQ][0-9][A-Z0-9]{3}[0-9])(?:-\d+)?$"
)
REVIEW_NOTE = (
    "iModulonDB membership is computational expression-module context; review "
    "the iModulonDB component, source organism, and primary literature before "
    "using it as PathwayMech protein-participant evidence."
)


@dataclass(frozen=True)
class ImodulonGeneRow:
    organism: str
    dataset: str
    k: int
    gene_id: str
    gene_locus: str | None
    gene_name: str | None
    gene_product: str | None
    weight: float
    in_imodulon: bool
    uniprot_id: str | None
    uniprot_protein_name: str | None
    all_regulators: str | None
    imodulon_name: str | None

    @property
    def imodulon_id(self) -> str:
        return f"{self.organism}/{self.dataset}/{self.k}"


@dataclass(frozen=True)
class PathwayParticipant:
    record_file: str
    pathway_id: str
    pathway_label: str
    pathway_type: str
    taxa: tuple[str, ...]
    participant_id: str
    participant_label: str
    edge_ids: tuple[str, ...]


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    pathway_file: str
    pathway_id: str
    pathway_label: str
    pathway_type: str
    taxa: tuple[str, ...]
    participant_id: str
    participant_label: str
    edge_ids: tuple[str, ...]
    organism: str
    dataset: str
    k: int
    imodulon_id: str
    imodulon_name: str | None
    gene_id: str
    gene_locus: str | None
    gene_name: str | None
    gene_product: str | None
    uniprot_id: str
    uniprot_protein_name: str | None
    weight: float
    all_regulators: str | None
    review_note: str


@dataclass(frozen=True)
class BlockedRow:
    reason: str
    organism: str
    dataset: str
    k: int
    gene_id: str
    uniprot_id: str | None
    detail: str


def load_imodulon_rows(path: Path) -> list[ImodulonGeneRow]:
    rows: list[ImodulonGeneRow] = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                raw = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {error.msg}") from error
            if not isinstance(raw, dict):
                raise ValueError(f"{path}:{line_number}: row must be a JSON object")
            rows.append(_load_imodulon_row(raw, path, line_number))
    return rows


def pathway_participants(records_dir: Path) -> dict[str, list[PathwayParticipant]]:
    by_uniprot: dict[str, list[PathwayParticipant]] = {}
    for path in sorted(records_dir.rglob("*.yaml")):
        record = _load_pathway_record(path)
        edges_by_node = _edges_by_node(record.get("mechanistic_edges", ()))
        taxa = tuple(
            f"{taxon['id']}|{taxon['label']}"
            for taxon in record.get("taxa", ())
            if isinstance(taxon, dict)
        )
        for participant in record.get("participants", ()):
            if not isinstance(participant, dict):
                continue
            participant_id = participant.get("id")
            if not isinstance(participant_id, str) or not participant_id.startswith(
                "UniProtKB:"
            ):
                continue
            accession = participant_id.removeprefix("UniProtKB:")
            by_uniprot.setdefault(accession, []).append(
                PathwayParticipant(
                    record_file=str(path),
                    pathway_id=record["id"],
                    pathway_label=record["label"],
                    pathway_type=record["pathway_type"],
                    taxa=taxa,
                    participant_id=participant_id,
                    participant_label=participant["label"],
                    edge_ids=tuple(sorted(edges_by_node.get(participant_id, ()))),
                )
            )

    for accession in by_uniprot:
        by_uniprot[accession].sort(
            key=lambda participant: (participant.record_file, participant.participant_id)
        )
    return by_uniprot


def stage_candidates(
    rows: Sequence[ImodulonGeneRow],
    participants_by_uniprot: Mapping[str, Sequence[PathwayParticipant]],
) -> tuple[list[Candidate], list[BlockedRow]]:
    candidates: list[Candidate] = []
    blocked: list[BlockedRow] = []
    seen_keys: set[tuple[str, str, str, str, str]] = set()

    for row in rows:
        uniprot_id = normalized_uniprot(row.uniprot_id)
        if not row.in_imodulon:
            blocked.append(_blocked(row, "OUTSIDE_IMODULON", "row is below the iModulon threshold"))
            continue
        if uniprot_id is None:
            blocked.append(_blocked(row, "NO_UNIPROT", "row has no UniProt accession"))
            continue
        if not UNIPROT_ACCESSION.fullmatch(uniprot_id):
            blocked.append(_blocked(row, "INVALID_UNIPROT", "row UniProt accession is invalid"))
            continue

        participants = participants_by_uniprot.get(uniprot_id)
        if not participants:
            blocked.append(
                _blocked(
                    row,
                    "NO_PATHWAY_PARTICIPANT",
                    f"UniProtKB:{uniprot_id} is not a PathwayMech participant",
                )
            )
            continue

        for participant in participants:
            key = (
                row.organism,
                row.dataset,
                str(row.k),
                uniprot_id,
                participant.pathway_id,
            )
            if key in seen_keys:
                raise ValueError(
                    "duplicate iModulonDB pathway candidate: " + "/".join(key)
                )
            seen_keys.add(key)
            candidates.append(_candidate(row, uniprot_id, participant))

    return candidates, blocked


def normalized_uniprot(value: str | None) -> str | None:
    if value is None:
        return None
    accession = value.strip().removeprefix("UniProtKB:")
    return accession or None


def write_reports(
    report_dir: Path,
    candidates: Sequence[Candidate],
    blocked: Sequence[BlockedRow],
) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)
    _write_jsonl(report_dir / "candidates.jsonl", candidates)
    _write_tsv(report_dir / "candidates.tsv", candidates, Candidate)
    _write_tsv(report_dir / "blocked.tsv", blocked, BlockedRow)
    (report_dir / "summary.md").write_text(_summary(candidates, blocked), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    rows = load_imodulon_rows(args.jsonl)
    participants = pathway_participants(args.records)
    candidates, blocked = stage_candidates(rows, participants)

    if args.apply:
        write_reports(args.report_dir, candidates, blocked)
        action = f"wrote reports to {args.report_dir}"
    else:
        action = f"dry-run; pass --apply to write {args.report_dir}"

    print(
        f"indexed {sum(len(matches) for matches in participants.values())} "
        f"UniProt pathway participants; staged {len(candidates)} candidate(s), "
        f"blocked {len(blocked)} row(s); {action}"
    )
    return 0


def _load_imodulon_row(
    raw: Mapping[str, Any],
    path: Path,
    line_number: int,
) -> ImodulonGeneRow:
    locus = f"{path}:{line_number}"
    return ImodulonGeneRow(
        organism=_required_string(raw, "organism", locus),
        dataset=_required_string(raw, "dataset", locus),
        k=_required_int(raw, "k", locus),
        gene_id=_required_string(raw, "gene_id", locus),
        gene_locus=_optional_string(raw, "gene_locus", locus),
        gene_name=_optional_string(raw, "gene_name", locus),
        gene_product=_optional_string(raw, "gene_product", locus),
        weight=_required_float(raw, "weight", locus),
        in_imodulon=_required_bool(raw, "in_imodulon", locus),
        uniprot_id=_optional_string(raw, "uniprot_id", locus),
        uniprot_protein_name=_optional_string(raw, "uniprot_protein_name", locus),
        all_regulators=_optional_string(raw, "all_regulators", locus),
        imodulon_name=(
            _optional_string(raw, "imodulon_name", locus)
            or _optional_string(raw, "imodulon", locus)
            or _optional_string(raw, "name", locus)
        ),
    )


def _load_pathway_record(path: Path) -> Mapping[str, Any]:
    with path.open(encoding="utf-8") as stream:
        record = yaml.safe_load(stream)
    if not isinstance(record, dict):
        raise ValueError(f"{path}: pathway record must be a YAML mapping")

    required = (
        "id",
        "label",
        "pathway_type",
        "taxa",
        "participants",
        "mechanistic_edges",
    )
    missing = [field for field in required if field not in record]
    if missing:
        raise ValueError(f"{path}: missing required field(s): {', '.join(missing)}")
    return record


def _edges_by_node(edges: Iterable[Any]) -> dict[str, set[str]]:
    edge_ids: dict[str, set[str]] = {}
    for edge in edges:
        if not isinstance(edge, dict):
            continue
        edge_id = edge.get("id")
        if not isinstance(edge_id, str):
            continue
        for endpoint in (edge.get("subject"), edge.get("object")):
            if isinstance(endpoint, str):
                edge_ids.setdefault(endpoint, set()).add(edge_id)
    return edge_ids


def _candidate(
    row: ImodulonGeneRow,
    uniprot_id: str,
    participant: PathwayParticipant,
) -> Candidate:
    digest = hashlib.sha256(
        "\0".join(
            (
                row.organism,
                row.dataset,
                str(row.k),
                uniprot_id,
                participant.pathway_id,
            )
        ).encode("utf-8")
    ).hexdigest()[:12]
    return Candidate(
        candidate_id=f"imodulondb-{digest}",
        pathway_file=participant.record_file,
        pathway_id=participant.pathway_id,
        pathway_label=participant.pathway_label,
        pathway_type=participant.pathway_type,
        taxa=participant.taxa,
        participant_id=participant.participant_id,
        participant_label=participant.participant_label,
        edge_ids=participant.edge_ids,
        organism=row.organism,
        dataset=row.dataset,
        k=row.k,
        imodulon_id=row.imodulon_id,
        imodulon_name=row.imodulon_name,
        gene_id=row.gene_id,
        gene_locus=row.gene_locus,
        gene_name=row.gene_name,
        gene_product=row.gene_product,
        uniprot_id=uniprot_id,
        uniprot_protein_name=row.uniprot_protein_name,
        weight=row.weight,
        all_regulators=row.all_regulators,
        review_note=REVIEW_NOTE,
    )


def _blocked(row: ImodulonGeneRow, reason: str, detail: str) -> BlockedRow:
    return BlockedRow(
        reason=reason,
        organism=row.organism,
        dataset=row.dataset,
        k=row.k,
        gene_id=row.gene_id,
        uniprot_id=normalized_uniprot(row.uniprot_id),
        detail=detail,
    )


def _write_jsonl(path: Path, rows: Sequence[Candidate]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(_row_dict(row), sort_keys=True) + "\n")


def _write_tsv(path: Path, rows: Sequence[Any], row_type: type) -> None:
    fields = tuple(row_type.__dataclass_fields__)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(_row_dict(row))


def _row_dict(row: Any) -> dict[str, Any]:
    return {
        key: ";".join(value) if isinstance(value, tuple) else value
        for key, value in asdict(row).items()
    }


def _summary(candidates: Sequence[Candidate], blocked: Sequence[BlockedRow]) -> str:
    reason_counts: dict[str, int] = {}
    for row in blocked:
        reason_counts[row.reason] = reason_counts.get(row.reason, 0) + 1
    reasons = "\n".join(
        f"- {reason}: {reason_counts[reason]}" for reason in sorted(reason_counts)
    )
    if not reasons:
        reasons = "- None"
    return (
        "# iModulonDB Pathway Participant Staging\n\n"
        f"- Candidates: {len(candidates)}\n"
        f"- Blocked rows: {len(blocked)}\n\n"
        "## Blocked Reasons\n\n"
        f"{reasons}\n\n"
        "## Review Guardrail\n\n"
        f"{REVIEW_NOTE}\n"
    )


def _required_string(raw: Mapping[str, Any], field: str, locus: str) -> str:
    value = raw.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{locus}: {field} must be a non-empty string")
    return value


def _optional_string(raw: Mapping[str, Any], field: str, locus: str) -> str | None:
    value = raw.get(field)
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"{locus}: {field} must be a string when present")
    return value.strip() or None


def _required_int(raw: Mapping[str, Any], field: str, locus: str) -> int:
    value = raw.get(field)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{locus}: {field} must be an integer")
    return value


def _required_float(raw: Mapping[str, Any], field: str, locus: str) -> float:
    value = raw.get(field)
    if isinstance(value, bool) or not isinstance(value, int | float):
        raise ValueError(f"{locus}: {field} must be a number")
    return float(value)


def _required_bool(raw: Mapping[str, Any], field: str, locus: str) -> bool:
    value = raw.get(field)
    if not isinstance(value, bool):
        raise ValueError(f"{locus}: {field} must be a boolean")
    return value


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Stage exact iModulonDB UniProt matches for PathwayMech pathway "
            "participant review."
        )
    )
    parser.add_argument(
        "jsonl",
        type=Path,
        help="normalized iModulonDB component-gene JSONL with a dataset-local k field",
    )
    parser.add_argument(
        "--records",
        type=Path,
        default=Path("data/pathways"),
        help="PathwayMech YAML record directory",
    )
    parser.add_argument(
        "--report-dir",
        type=Path,
        default=Path("reports/imodulondb"),
        help="directory for staged candidate and blocker reports",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write reports; the default is a dry-run count only",
    )
    return parser


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2) from error
