"""Verify or materialize the complete immutable predecessor retention preparation."""

import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(body):
    return hashlib.sha256(body).hexdigest()


def safe(root, name):
    relative = Path(name)
    assert not relative.is_absolute() and ".." not in relative.parts
    path = root / relative
    assert path.resolve().is_relative_to(root.resolve()) and not path.is_symlink()
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--materialize", type=Path)
    parser.add_argument("--compare-original", type=Path)
    args = parser.parse_args()
    mapping = json.loads((args.root / "provenance-successor/predecessor-map.json").read_bytes())
    rows = mapping["files"]
    assert len({r["original_path"] for r in rows}) == len(rows)
    target = None
    if args.materialize:
        target = args.materialize.resolve()
        assert target.is_relative_to(Path("/private/tmp")) and not target.exists()
        target.mkdir()
    reconstructed = {}
    for row in rows:
        body = safe(args.root, row["retained_path"]).read_bytes()
        assert sha(body) == row["stored_sha256"] and len(body) == row["stored_bytes"]
        assert row["encoding"] in ("identity", "gzip")
        if row["encoding"] == "gzip":
            body = gzip.decompress(body)
        assert sha(body) == row["original_sha256"] and len(body) == row["original_bytes"]
        reconstructed[row["original_path"]] = (sha(body), len(body))
        if args.compare_original:
            assert body == safe(args.compare_original, row["original_path"]).read_bytes()
        if target:
            path = safe(target, row["original_path"])
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(body)
            assert path.read_bytes() == body
    if args.compare_original:
        paths = list(args.compare_original.rglob("*"))
        assert not any(p.is_symlink() for p in paths)
        assert {str(p.relative_to(args.compare_original)) for p in paths if p.is_file()} == set(
            reconstructed
        )
    if target:
        assert {str(p.relative_to(target)) for p in target.rglob("*") if p.is_file()} == set(
            reconstructed
        )
    print(
        json.dumps(
            {
                "status": "passed",
                "complete_original_preparation_files": len(rows),
                "original_outer_manifest_sha256": mapping["original_outer_manifest_sha256"],
                "original_payload_manifest_sha256": mapping["original_payload_manifest_sha256"],
                "all_hidden_and_ignored_original_files_exact": True,
                "compared_original": str(args.compare_original) if args.compare_original else None,
                "materialized": str(target) if target else None,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
