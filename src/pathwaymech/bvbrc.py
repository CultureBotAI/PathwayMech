from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

BV_BRC_SEED_HEADER = "genome_id\tgene_id\tec_number\tpathway_id\tpathway_name"


@dataclass(frozen=True)
class BvBrcPathwayCall:
    genome_id: str
    gene_id: str
    ec_number: str
    pathway_id: str
    pathway_name: str


def load_bvbrc_pathways(path: Path) -> list[BvBrcPathwayCall]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        return [
            BvBrcPathwayCall(
                genome_id=row.get("genome_id", ""),
                gene_id=row.get("gene_id", ""),
                ec_number=_ec(row.get("ec_number", "")),
                pathway_id=f"KEGG:{row.get('pathway_id', '').removeprefix('KEGG:')}",
                pathway_name=row.get("pathway_name", ""),
            )
            for row in reader
        ]


def bvbrc_seed_rows(calls: list[BvBrcPathwayCall]) -> list[str]:
    return [
        BV_BRC_SEED_HEADER,
        *[
            "\t".join(
                [
                    call.genome_id,
                    call.gene_id,
                    call.ec_number,
                    call.pathway_id,
                    call.pathway_name,
                ]
            )
            for call in calls
        ],
    ]


def _ec(value: str) -> str:
    return f"EC:{value.removeprefix('EC:')}" if value else ""
