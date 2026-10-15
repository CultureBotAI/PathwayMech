"""Verify complete declared compact maps and read compact-only logical originals."""

import argparse
import gzip
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def sha(body):
    return hashlib.sha256(body).hexdigest()


def safe(root, name):
    relative = Path(name)
    assert not relative.is_absolute() and ".." not in relative.parts
    path = root / relative
    assert path.resolve().is_relative_to(root.resolve()) and not path.is_symlink()
    return path


def check(body, digest, size):
    assert sha(body) == digest and len(body) == size


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--verify-all", action="store_true")
    parser.add_argument("--package")
    parser.add_argument("--artifact")
    parser.add_argument("--materialize-logical", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    mappings = json.loads((root / "content-map.json").read_bytes())
    pairs = json.loads((root / "verified-compact-pairs.json").read_bytes())
    spec = json.loads((root / "source-specification.json").read_bytes())
    physical = {}
    for name in [p["name"] for p in spec["packages"]]:
        package = json.loads(safe(root, "packages/" + name + "/source-map.json").read_bytes())
        physical[name] = {r["path"]: r for r in package["source_occurrences"]}
    cache = {}
    endpoints = {}
    git = subprocess.Popen(
        ["git", "cat-file", "--batch"], cwd=args.repo, stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )

    def decode(digest):
        if digest in cache:
            return cache[digest]
        row = mappings[digest]
        endpoint = row["storage"]
        key = (endpoint["kind"], endpoint["path"])
        if key not in endpoints:
            if endpoint["kind"] == "new_retention_object":
                body = safe(root, endpoint["path"]).read_bytes()
            else:
                assert endpoint["kind"] == "existing_repository"
                safe(args.repo, endpoint["path"])
                git.stdin.write((endpoint["git_commit"] + ":" + endpoint["path"] + "\n").encode())
                git.stdin.flush()
                header = git.stdout.readline().split()
                assert len(header) == 3 and header[1] == b"blob"
                body = git.stdout.read(int(header[2]))
                assert git.stdout.read(1) == b"\n"
            check(body, endpoint["stored_sha256"], endpoint["stored_bytes"])
            endpoints[key] = body
        body = endpoints[key]
        for step in row["decode_steps"]:
            assert step["encoding"] == "gzip" and sha(body) == step["input_sha256"]
            body = gzip.decompress(body)
            check(body, step["output_sha256"], step["output_bytes"])
        check(body, digest, row["source_bytes"])
        cache[digest] = body
        return body

    def original(pair):
        owner = physical[pair["package"]][pair["stored_path"]]
        assert owner["sha256"] == pair["stored_sha256"] and owner["bytes"] == pair["stored_bytes"]
        stored = decode(owner["sha256"])
        assert pair["encoding"] in ("identity", "gzip")
        body = gzip.decompress(stored) if pair["encoding"] == "gzip" else stored
        check(body, pair["original_sha256"], pair["original_bytes"])
        if pair["original_physically_present"]:
            expected = physical[pair["package"]][pair["original_path"]]
            assert decode(expected["sha256"]) == body
        else:
            assert pair["original_path"] not in physical[pair["package"]]
        for payload in pair["preserved_original_gzip_payloads"]:
            check(gzip.decompress(body), payload["sha256"], payload["bytes"])
        return body

    if args.verify_all:
        assert not args.package and not args.artifact and not args.materialize_logical
        expected = set()
        map_count = 0
        for package in spec["packages"]:
            for binding in package["compact_maps"]:
                owner = physical[package["name"]][binding["path"]]
                assert owner["sha256"] == binding["sha256"] and owner["bytes"] == binding["bytes"]
                obj = json.loads(decode(owner["sha256"]))
                assert len(obj[binding["array"]]) == binding["expected_rows"]
                assert sorted(obj) == binding["top_level_keys"]
                for array in [binding["array"]] + (
                    ["already_compressed_originals"]
                    if "already_compressed_originals" in obj
                    else []
                ):
                    for index, declared in enumerate(obj[array]):
                        key = (package["name"], binding["path"], array, index)
                        expected.add(key)
                        matches = [
                            p
                            for p in pairs
                            if (
                                p["package"],
                                p["compact_map"],
                                p.get("array", binding["array"]),
                                p["index"],
                            )
                            == key
                        ]
                        assert len(matches) == 1 and matches[0]["declared_row"] == declared
                map_count += 1
        observed = set()
        for pair in pairs:
            binding = next(
                m
                for p in spec["packages"]
                if p["name"] == pair["package"]
                for m in p["compact_maps"]
                if m["path"] == pair["compact_map"]
            )
            key = (
                pair["package"],
                pair["compact_map"],
                pair.get("array", binding["array"]),
                pair["index"],
            )
            assert key not in observed
            observed.add(key)
            original(pair)
        assert observed == expected
        result = {
            "status": "passed",
            "compact_maps": map_count,
            "declared_pairs_including_already_compressed": len(pairs),
            "compact_only_logical_occurrences": sum(
                not p["original_physically_present"] for p in pairs
            ),
            "all_declared_rows_and_originals_exact": True,
            "all_declared_inner_gzip_payloads_exact": True,
        }
        print(json.dumps(result, indent=2))
    else:
        assert args.package and (
            (args.artifact is not None) != (args.materialize_logical is not None)
        )
        selected = [p for p in pairs if p["package"] == args.package]
        assert selected
        if args.artifact:
            selected = [p for p in selected if p["original_path"] == args.artifact]
            assert selected and len({p["original_sha256"] for p in selected}) == 1
            sys.stdout.buffer.write(original(selected[0]))
        else:
            target = args.materialize_logical.resolve()
            assert target.is_relative_to(Path("/private/tmp")) and not target.exists()
            target.mkdir()
            count = 0
            for pair in selected:
                if pair["original_physically_present"]:
                    continue
                body = original(pair)
                path = safe(target, pair["original_path"])
                path.parent.mkdir(parents=True, exist_ok=True)
                if path.exists():
                    assert path.read_bytes() == body
                else:
                    path.write_bytes(body)
                    count += 1
            print(
                json.dumps(
                    {
                        "status": "passed",
                        "package": args.package,
                        "compact_only_logical_originals_materialized": count,
                        "target": str(target),
                    }
                )
            )
    git.stdin.close()
    assert git.wait() == 0


if __name__ == "__main__":
    main()
