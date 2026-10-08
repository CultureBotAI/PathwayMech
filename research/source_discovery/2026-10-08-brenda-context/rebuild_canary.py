"""Rebuild the bounded BRENDA context audit from hash-checked external bytes.

Standard library only. No network access, RDF enzyme joins, pathway writes,
or automatic interpretation of primary-paper experiments occurs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlsplit

HERE = Path(__file__).resolve().parent
BASE = "https://purl.dsmz.de/brenda/"
ROWS = {
    "tab27r0sr0": (
        "reaction",
        "reaction_diagram",
        "commentary",
        "organism",
        "uniprot",
        "literature",
    ),
    "tab37r0sr1": (
        "substrate",
        "product",
        "reaction_diagram",
        "organism",
        "uniprot",
        "literature",
        "commentary",
        "reversibility",
    ),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


class NativeCells(HTMLParser):
    """Read only explicitly selected div cells, including hidden source cells."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.active: dict[str, Any] | None = None
        self.cells: dict[str, dict[str, Any]] = {}
        self.expected = {
            f"{row}c{index}" for row, columns in ROWS.items() for index in range(len(columns))
        }

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "div":
            self.depth += 1
            cell_id = values.get("id")
            if cell_id in self.expected:
                require(self.active is None, "selected cells overlap")
                require(cell_id not in self.cells, f"duplicate cell: {cell_id}")
                self.active = {"cell_id": cell_id, "text": [], "hrefs": [], "depth": self.depth}
        if self.active is not None and tag == "a" and values.get("href"):
            self.active["hrefs"].append(values["href"])
        if self.active is not None and tag == "br":
            self.active["text"].append(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag == "div":
            if self.active is not None and self.active["depth"] == self.depth:
                cell = self.active
                cell.pop("depth")
                cell["text"] = " ".join("".join(cell["text"]).split())
                self.cells[cell["cell_id"]] = cell
                self.active = None
            self.depth -= 1

    def handle_data(self, data: str) -> None:
        if self.active is not None:
            self.active["text"].append(data)


def rebuild(cache: Path) -> dict[str, Any]:
    manifest = json.loads((HERE / "acquisition-manifest.json").read_text())
    sources = {item["artifact"]: item for item in manifest}
    original: dict[str, bytes] = {}
    for name, item in sources.items():
        data = (cache / name).read_bytes()
        require(len(data) == item["bytes"], f"size mismatch: {name}")
        require(hashlib.sha256(data).hexdigest() == item["sha256"], f"SHA-256 mismatch: {name}")
        original[name] = data
    query_bytes = (HERE / "scoped-triples.rq").read_bytes()
    rdf_source = sources["scoped-triples.json"]
    require(
        hashlib.sha256(query_bytes).hexdigest() == rdf_source["query_sha256"],
        "query checksum mismatch",
    )
    require(
        parse_qs(urlsplit(rdf_source["url"]).query)["query"] == [query_bytes.decode()],
        "query differs from acquisition URL",
    )
    page = "ec-4.2.1.12.html"
    parser = NativeCells()
    parser.feed(original[page].decode("utf-8"))
    parser.close()
    require(set(parser.cells) == parser.expected, "missing selected native cells")
    rows = []
    for row, columns in ROWS.items():
        rows.append(
            {
                "source_url": sources[page]["url"],
                "source_sha256": sources[page]["sha256"],
                "retrieved_at": sources[page]["retrieved_at"],
                "native_row_id": row,
                "fields": {
                    column: parser.cells[f"{row}c{index}"] for index, column in enumerate(columns)
                },
            }
        )
    triples = json.loads(original["scoped-triples.json"])["results"]["bindings"]
    require(
        len(triples) == rdf_source["binding_count"] < rdf_source["row_limit"], "query truncated"
    )
    enzyme = [row for row in triples if row["subject"]["value"] == BASE + "enzyme/329"]
    require(len(enzyme) == 791, "unexpected enzyme subject size")
    counts = Counter(row["predicate"]["value"] for row in enzyme)
    selected = [row for row in triples if row["subject"]["value"] != BASE + "enzyme/329"]
    uniprot = json.loads(original["uniprot-A0A0H3CB86.json"])
    require(uniprot["primaryAccession"] == "A0A0H3CB86", "wrong UniProt accession")
    require(uniprot["organism"]["taxonId"] == 565050, "wrong UniProt taxon")
    loci = [x["value"] for gene in uniprot["genes"] for x in gene.get("orderedLocusNames", [])]
    require(loci == ["CCNA_02134"], "wrong UniProt locus")
    projection = json.loads((HERE / "review-assessments.json").read_text())
    projection.update(
        {
            "rows": rows,
            "rdf_projection": {
                "source_sha256": rdf_source["sha256"],
                "source_locator": "results.bindings, subject/predicate/object exact terms",
                "source_binding_count": len(triples),
                "enzyme_329_predicate_counts": dict(sorted(counts.items())),
                "selected_triples": selected,
            },
            "protein_identity": {
                "source_url": sources["uniprot-A0A0H3CB86.json"]["url"],
                "source_sha256": sources["uniprot-A0A0H3CB86.json"]["sha256"],
                "source_locator": "primaryAccession; organism; genes[*].orderedLocusNames",
                "accession": uniprot["primaryAccession"],
                "organism": uniprot["organism"],
                "locus": loci[0],
            },
            "absence_check": {
                "scope": "complete downloaded EC4.1.2.14 HTML bytes, including hidden rows",
                "source_sha256": sources["ec-4.1.2.14.html"]["sha256"],
                "needle_ascii": "Caulobacter",
                "count": original["ec-4.1.2.14.html"].count(b"Caulobacter"),
                "limit": (
                    "No claim about all BRENDA records or all Caulobacter aldolase literature."
                ),
            },
        }
    )
    return projection


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    parser.add_argument(
        "--check", action="store_true", help="Compare with the committed projection."
    )
    args = parser.parse_args()
    projection = rebuild(args.cache)
    if args.check:
        expected = json.loads((HERE / "native-context-audit.json").read_text())
        require(projection == expected, "rebuilt projection differs")
        print("BRENDA context projection and source hashes verified.")
    else:
        print(json.dumps(projection, indent=2))


if __name__ == "__main__":
    main()
