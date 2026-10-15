"""Verify every inherited content-map endpoint against actual pinned Git owners."""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def sha(body):
    return hashlib.sha256(body).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    content = json.loads((args.root / "content-map.json").read_bytes())
    proofs = json.loads((args.root / "existing-owner-verification.json").read_bytes())
    owners = {row["path"]: row for row in proofs}
    assert len(owners) == len(proofs)
    actual_trees = {}
    endpoints = {}
    inherited = with_tree = 0
    for digest, row in content.items():
        endpoint = row["storage"]
        if endpoint["kind"] != "existing_repository":
            continue
        inherited += 1
        commit, path = endpoint["git_commit"], endpoint["path"]
        assert not Path(path).is_absolute() and ".." not in Path(path).parts
        assert digest == row["source_sha256"]
        if commit not in actual_trees:
            actual_trees[commit] = (
                subprocess.check_output(["git", "rev-parse", commit + "^{tree}"], cwd=args.repo)
                .decode()
                .strip()
            )
        if "git_tree" in endpoint:
            assert endpoint["git_tree"] == actual_trees[commit], ("stale inherited tree", digest)
            with_tree += 1
        proof = owners[path]
        assert proof["git_commit"] == commit
        assert proof["git_tree"] == actual_trees[commit]
        assert proof["sha256"] == endpoint["stored_sha256"]
        assert proof["bytes"] == endpoint["stored_bytes"]
        key = (commit, path)
        if key in endpoints:
            assert endpoints[key] == (endpoint["stored_sha256"], endpoint["stored_bytes"])
        endpoints[key] = (endpoint["stored_sha256"], endpoint["stored_bytes"])
    assert {path for _, path in endpoints} == set(owners)
    keys = sorted(endpoints)
    queries = "".join(commit + ":" + path + "\n" for commit, path in keys).encode()
    raw = subprocess.run(
        ["git", "cat-file", "--batch"],
        cwd=args.repo,
        input=queries,
        capture_output=True,
        check=True,
    ).stdout
    offset = 0
    for commit, path in keys:
        end = raw.index(b"\n", offset)
        header = raw[offset:end].split()
        assert len(header) == 3 and header[1] == b"blob"
        size = int(header[2])
        body = raw[end + 1 : end + 1 + size]
        offset = end + 2 + size
        assert raw[offset - 1 : offset] == b"\n"
        assert (sha(body), len(body)) == endpoints[(commit, path)]
        assert header[0].decode() == owners[path]["git_blob"]
    assert offset == len(raw)
    print(
        json.dumps(
            {
                "status": "passed",
                "inherited_content_rows": inherited,
                "rows_with_optional_tree": with_tree,
                "verified_git_storage_owners": len(keys),
                "actual_trees": actual_trees,
                "every_present_tree_and_exact_owner_verified": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
