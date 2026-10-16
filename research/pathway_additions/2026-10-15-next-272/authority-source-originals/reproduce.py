"""Reproduce only accepted ethanolamine additions over the exact merge baseline."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

from pathwaymech.identifiers import _load_authority
from scripts.build_source_identifier_snapshot import build_snapshot

BASE = "54e768a985d07705ea25445804c83b4758646e37"
OWN = Path(__file__).resolve().parent
REPO = OWN.parents[3]


def dump(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def baseline(relative: str) -> object:
    result = subprocess.run(
        ["git", "show", f"{BASE}:{relative}"],
        cwd=REPO,
        check=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    output = parser.parse_args().output.resolve()
    if output == OWN or OWN in output.parents:
        parser.error("Choose an output directory outside this retained evidence owner")
    output.mkdir(parents=True, exist_ok=True)
    old_source = baseline("data/identifier_authorities/sources.json")
    old_ontology = baseline("data/identifier_authorities/ontology.json")
    old_conf = baseline("conf/identifier_sources.json")
    graph = json.loads((OWN / "selected-graph-identities.json").read_text())
    old_ids = old_source["terms"].keys() | old_ontology["terms"].keys()
    selection = {"id": graph["id"]}
    for section in ("participants", "reactions"):
        selection[section] = [
            node
            for node in graph[section]
            if node["id"] not in old_ids
            and node["id"].split(":", 1)[0] in {"MetaCyc", "EcoCyc", "UniProtKB"}
        ]
    selected = output / "selection"
    selected.mkdir(exist_ok=True)
    (selected / "authority-routing-only.yaml").write_text(
        yaml.safe_dump(selection, sort_keys=False), encoding="utf-8"
    )
    manifest = OWN / "new-source-manifest.json"
    delta = build_snapshot(manifest, selected, OWN / "cache")
    if len(delta["sources"]) != 97 or len(delta["terms"]) != 97:
        raise ValueError("Expected exactly63 native and34 UniProt source additions")
    for section in ("sources", "terms"):
        if old_source[section].keys() & delta[section].keys():
            raise ValueError("An addition would replace a prior source owner")
        old_source[section].update(delta[section])
    ontology_delta = json.loads((OWN / "accepted-four-term-delta.json").read_text())
    old_bytes = (json.dumps(old_ontology, indent=2, ensure_ascii=False) + "\n").encode()
    if hashlib.sha256(old_bytes).hexdigest() != ontology_delta["baseline_sha256"]:
        raise ValueError("The pinned ontology baseline differs from the accepted delta")
    if any(
        ontology_delta[key]
        for key in ("sources_added", "sources_modified", "terms_modified", "terms_removed")
    ):
        raise ValueError("Ontology proposal must contain additions only")
    terms = ontology_delta["terms_added"]
    if len(terms) != 4 or old_ontology["terms"].keys() & terms.keys():
        raise ValueError("Expected four new, nonoverlapping pinned ontology terms")
    old_ontology["terms"].update(terms)
    entries = json.loads(manifest.read_text())
    if {row["key"] for row in entries} & {row["key"] for row in old_conf}:
        raise ValueError("An addition would replace a prior configured source")
    dump(output / "sources.json", old_source)
    dump(output / "ontology.json", old_ontology)
    dump(output / "identifier_sources.json", old_conf + entries)
    _load_authority(output / "sources.json")
    _load_authority(output / "ontology.json")
    print("Reproduced97 source terms and4 accepted pinned ontology additions")


if __name__ == "__main__":
    main()
