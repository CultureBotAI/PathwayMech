"""Replay the bounded DesC correction against the preserved original primary body."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

import yaml


class Figures(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.depth = 0
        self.identifier = ""
        self.parts: list[str] = []
        self.figures: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        identifier = dict(attrs).get("id", "")
        if identifier in {"RSTB20170068F2", "RSTB20170068F3", "RSTB20170068F4"}:
            self.identifier = str(identifier)
            self.depth = 1
            self.parts = []
        elif self.depth and tag not in {"img", "br", "hr", "input", "meta", "link", "source"}:
            self.depth += 1

    def handle_endtag(self, tag: str) -> None:
        if self.depth:
            self.depth -= 1
            if not self.depth:
                self.figures[self.identifier] = " ".join(self.parts)

    def handle_data(self, data: str) -> None:
        if self.depth:
            self.parts.append(data.strip())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--record", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    dossier = Path(__file__).resolve().parent
    original = dossier / "initial-review-inputs/desferrioxamine-b-biosynthesis.yaml"
    assert sha(original) == "f9bb35866f883f0e47f5f5e98ba6ae2caf1d2d8ea967793b96f67d91e8fa1690"
    assert sha(args.source) == "1bd6c3e3a9a9048f03545ede3a17af2a8de138f070acc00827cec61ac5d557f3"
    figures = Figures()
    figures.feed(args.source.read_text())
    assert "Chemical structures" in figures.figures["RSTB20170068F2"]
    assert "Organization" in figures.figures["RSTB20170068F3"]
    caption = figures.figures["RSTB20170068F4"]
    assert "Extracted ion chromatograms" in caption and "DesC-catalysed reactions" in caption
    assert "HSC" in caption and "HAC" in caption and "( a )" in caption and "( b )" in caption
    before = yaml.safe_load(original.read_text())
    expected = copy.deepcopy(before)
    changes = json.loads((dossier / "initial-scientific-findings.json").read_text())
    for change in changes["findings"][0]["affected_evidence"]:
        edge = next(e for e in expected["mechanistic_edges"] if e["id"] == change["edge_id"])
        evidence = edge["evidence"][change["evidence_index"]]
        assert evidence == change["before"] and evidence["reference_id"] == "PMID:29685972"
        evidence["source_locator"] = change["proposed_source_locator"]
    current = yaml.safe_load(args.record.read_text())
    assert current == expected, "Correction must change exactly the two verified locators"
    assert before != expected, "Original wrong figure references must fail acceptance"
    report = {
        "status": "passed",
        "record_sha256": sha(args.record),
        "original_record_sha256": sha(original),
        "original_primary_sha256": sha(args.source),
        "changed_fields": 2,
        "original_locator_negative_probe_rejected": before != expected,
        "all_other_record_content_unchanged": True,
        "figure4_caption": caption,
        "limits": "Source-locator acceptance only; no full-corpus or publication claim.",
    }
    assert not args.output.exists(), "Preserve prior execution receipts"
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "sha256": sha(args.output), "status": "passed"}))


if __name__ == "__main__":
    main()
