from __future__ import annotations

import csv
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from pathwaymech.schema import PathwayRecord

KNOWLEDGE_SOURCE = "infores:pathwaymech"
SSSOM_COLUMNS = (
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "mapping_justification",
    "comment",
)

SSSOM_HEADER = (
    "# mapping_set_id: https://w3id.org/culturebotai/pathwaymech/source-mappings",
    "# license: https://spdx.org/licenses/MIT",
    f"# mapping_provider: {KNOWLEDGE_SOURCE}",
)
_SPACE = re.compile(r"[\t\r\n]+")


@dataclass(frozen=True)
class SssomRow:
    subject_id: str
    subject_label: str
    predicate_id: str
    object_id: str
    object_label: str
    mapping_justification: str
    comment: str


def sssom_rows(records: list[PathwayRecord]) -> list[SssomRow]:
    rows: dict[tuple[str, ...], SssomRow] = {}
    for record in records:
        for mapping in record.source_mappings:
            row = SssomRow(
                subject_id=mapping["subject_id"],
                subject_label=mapping["subject_label"],
                predicate_id=mapping["predicate_id"],
                object_id=mapping["object_id"],
                object_label=mapping["object_label"],
                mapping_justification=mapping["mapping_justification"],
                comment=(
                    f"source_pathway_id={mapping['source_pathway_id']}; "
                    f"source_element_id={mapping['source_element_id']}"
                ),
            )
            _validate_row(row)
            rows.setdefault(tuple(asdict(row).values()), row)
    return sorted(
        rows.values(),
        key=lambda row: (row.subject_id, row.predicate_id, row.object_id, row.comment),
    )


def write_sssom(records: list[PathwayRecord], output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as stream:
        for line in SSSOM_HEADER:
            stream.write(f"{line}\n")
        writer = csv.DictWriter(
            stream,
            delimiter="\t",
            fieldnames=SSSOM_COLUMNS,
            lineterminator="\n",
        )
        writer.writeheader()
        for row in sssom_rows(records):
            writer.writerow(
                {column: _cell(asdict(row).get(column)) for column in SSSOM_COLUMNS}
            )
    return output_path


def _validate_row(row: SssomRow) -> None:
    if row.subject_id == row.object_id:
        raise ValueError(
            f"source mapping subject_id must differ from object_id: {row.subject_id}"
        )
    for field in ("subject_id", "predicate_id", "object_id", "mapping_justification"):
        value = getattr(row, field)
        if ":" not in value:
            raise ValueError(f"{field} must be a CURIE, not {value!r}")
        prefix, local = value.split(":", 1)
        if not prefix or not local or any(character.isspace() for character in value):
            raise ValueError(f"{field} must be a CURIE, not {value!r}")


def _cell(value: Any) -> str:
    if value is None:
        return ""
    return _SPACE.sub(" ", str(value)).strip()
