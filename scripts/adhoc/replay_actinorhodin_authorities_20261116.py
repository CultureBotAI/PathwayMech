"""Replay the four additive actinorhodin authorities from checksum-bound originals."""

import argparse
import json
import tempfile
from pathlib import Path

from scripts.build_source_identifier_snapshot import build_snapshot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--scratch-dir", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    if not args.scratch_dir.is_dir():
        parser.error("scratch-dir must be an existing durable directory")
    if str(args.scratch_dir.resolve()).startswith(("/tmp/", "/private/tmp/")):
        parser.error("scratch-dir must not be a system temporary directory")
    with tempfile.TemporaryDirectory(dir=args.scratch_dir) as directory:
        stage = Path(directory)
        records = stage / "records"
        records.mkdir()
        name = "actinorhodin-biosynthetic-gene-cluster.yaml"
        (records / name).write_bytes((root / "data/pathways" / name).read_bytes())
        projected = build_snapshot(
            root / "research/source_discovery/2026-11-16-actinorhodin-authorities.json",
            records, args.cache_dir,
        )
    retained = json.loads((root / "data/identifier_authorities/sources.json").read_text())
    for section in ("sources", "terms"):
        for key, value in projected[section].items():
            if retained[section].get(key) != value:
                raise ValueError(f"retained authority differs: {section}/{key}")
    print(f"Replayed {len(projected['terms'])} authority terms")


if __name__ == "__main__":
    main()
