"""Read or reconstruct exact frozen artifacts from the explicit retention mapping."""

import argparse
import gzip
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def sha(b):
    return hashlib.sha256(b).hexdigest()


def safe(root, name):
    p = Path(name)
    assert not p.is_absolute() and ".." not in p.parts
    result = root / p
    assert result.resolve().is_relative_to(root.resolve())
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--package")
    ap.add_argument("--artifact")
    ap.add_argument("--materialize", type=Path)
    ap.add_argument("--verify-all", action="store_true")
    ap.add_argument("--compare-originals", action="store_true")
    ap.add_argument(
        "--working-tree-owners",
        action="store_true",
        help="Verify existing owners from current filesystem instead of pinned Git objects.",
    )
    args = ap.parse_args()
    root = args.root.resolve()
    mappings = json.loads((root / "content-map.json").read_bytes())
    cache = {}
    endpoint_cache = {}
    if args.verify_all and not args.working_tree_owners:
        owners = {
            r["storage"]["path"]: r["storage"]
            for r in mappings.values()
            if r["storage"]["kind"] == "existing_repository"
        }
        paths = sorted(owners)
        if paths:
            queries = "".join(owners[p]["git_commit"] + ":" + p + "\n" for p in paths).encode()
            result = subprocess.run(
                ["git", "cat-file", "--batch"],
                cwd=args.repo,
                input=queries,
                capture_output=True,
                check=True,
            ).stdout
            offset = 0
            for path in paths:
                end = result.index(b"\n", offset)
                header = result[offset:end].split()
                assert header[1] == b"blob"
                size = int(header[2])
                offset = end + 1
                body = result[offset : offset + size]
                offset += size
                assert result[offset : offset + 1] == b"\n"
                offset += 1
                owner = owners[path]
                assert sha(body) == owner["stored_sha256"] and len(body) == owner["stored_bytes"]
                endpoint_cache[("existing_repository", path)] = body
            assert offset == len(result)

    def decode(digest):
        if digest in cache:
            return cache[digest]
        row = mappings[digest]
        storage = row["storage"]
        key = (storage["kind"], storage["path"])
        if key not in endpoint_cache:
            if storage["kind"] == "new_retention_object":
                body = safe(root, storage["path"]).read_bytes()
            elif storage["kind"] == "existing_repository":
                safe(args.repo, storage["path"])
                if args.working_tree_owners:
                    body = (args.repo / storage["path"]).read_bytes()
                else:
                    body = subprocess.check_output(
                        ["git", "show", storage["git_commit"] + ":" + storage["path"]],
                        cwd=args.repo,
                    )
            else:
                raise AssertionError(storage)
            assert sha(body) == storage["stored_sha256"] and len(body) == storage["stored_bytes"]
            endpoint_cache[key] = body
        body = endpoint_cache[key]
        for step in row["decode_steps"]:
            assert step["encoding"] == "gzip" and sha(body) == step["input_sha256"]
            body = gzip.decompress(body)
            assert sha(body) == step["output_sha256"] and len(body) == step["output_bytes"]
        assert sha(body) == digest == row["source_sha256"] and len(body) == row["source_bytes"]
        cache[digest] = body
        return body

    if args.verify_all:
        assert not args.package and not args.artifact and not args.materialize
        count = 0
        packages = 0
        for p in sorted((root / "packages").glob("*/source-map.json")):
            packages += 1
            for row in json.loads(p.read_bytes())["source_occurrences"]:
                body = decode(row["sha256"])
                assert len(body) == row["bytes"]
                count += 1
                if args.compare_originals:
                    assert body == Path(row["source"]).read_bytes()
        print(
            json.dumps(
                {
                    "status": "passed",
                    "package_or_selected_snapshot_groups": packages,
                    "source_occurrences": count,
                    "unique_contents": len(cache),
                    "unique_storage_endpoints": len(endpoint_cache),
                    "all_hashes_sizes_decode_steps_exact": True,
                    "compared_with_originals": args.compare_originals,
                    "existing_owner_mode": "working_tree"
                    if args.working_tree_owners
                    else "pinned_merged_git_objects",
                },
                indent=2,
            )
        )
        return
    assert args.package and ((args.artifact is not None) != (args.materialize is not None))
    package = safe(root / "packages", args.package)
    rows = json.loads((package / "source-map.json").read_bytes())["source_occurrences"]
    if args.artifact:
        matches = [r for r in rows if r["path"] == args.artifact]
        assert len(matches) == 1
        sys.stdout.buffer.write(decode(matches[0]["sha256"]))
        return
    target = args.materialize.resolve()
    assert target.is_relative_to(Path("/private/tmp")) and not target.exists(), (
        "Materialization is allowed only to a new external /private/tmp directory."
    )
    target.mkdir()
    for row in rows:
        p = safe(target, row["path"])
        assert not p.exists()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(decode(row["sha256"]))
        assert sha(p.read_bytes()) == row["sha256"]
    print(
        json.dumps(
            {
                "status": "materialized_exactly",
                "package": args.package,
                "external_target": str(target),
                "artifacts": len(rows),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
