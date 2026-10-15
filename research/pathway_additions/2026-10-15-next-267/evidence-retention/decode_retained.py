"""Verify and reconstruct exact retained bytes without executing source helpers."""

import argparse
import gzip
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path

BASE = "02bc234143d40e0e825737f27dfdcb5fd358322f"
TREE = "08c04c1808980164ab90512f83e6e1c9bb5f16af"
LIMIT = 100 * 1024 * 1024
HISTORICAL_BINDING = {
    "bytes": 6512597,
    "git_blob": "0f1c0f47dc4f0a2bd754e38900eca22f38be4f03",
    "git_commit": BASE,
    "git_tree": TREE,
    "path": (
        "research/pathway_additions/2026-10-15-next-266/"
        "evidence-retention/verified-compact-pairs.json"
    ),
    "retained_gzip": "proof/prior266-verified-compact-pairs.json.gz",
    "retained_sha256": "e44690c02448f0ea3bce3747a2ffcc75b4122aeec337acd1bef5324c0776964f",
    "sha256": "6a53dd595aac851dc2ae462c09a610a0bf13be3c24d1854e118cf224cc4b17fc",
}
HISTORICAL_MAPS = (
    (
        "primary",
        "compact-originals-manifest.json",
        "inputs/prior-primary/compact-originals-manifest.json",
        408,
    ),
    (
        "independent-primary-review",
        "compact-review-manifest.json",
        "inputs/prior-primary-review/compact-review-manifest.json",
        69,
    ),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(body):
    return hashlib.sha256(body).hexdigest()


def check(body, digest, size):
    require(isinstance(size, int) and size >= 0, "invalid size")
    require(re.fullmatch(r"[0-9a-f]{64}", digest) is not None, "invalid digest")
    require(len(body) == size and sha(body) == digest, "byte identity mismatch")


def safe(root, name):
    require(isinstance(name, str) and name and "\\" not in name, "invalid path")
    rel = Path(name)
    require(not rel.is_absolute() and ".." not in rel.parts, "unsafe relative path")
    require(str(rel) == name and name != ".", "noncanonical path")
    target = root / rel
    require(target.resolve().is_relative_to(root.resolve()), "path escapes root")
    for parent in (target, *target.parents):
        if parent == root:
            break
        require(not parent.is_symlink(), "symlink path rejected")
    return target


def gunzip(body, digest, size):
    require(isinstance(size, int) and size >= 0, "invalid decoded size")
    with gzip.GzipFile(fileobj=io.BytesIO(body)) as stream:
        decoded = stream.read(size + 1)
    check(decoded, digest, size)
    return decoded


def parse_json(body):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            require(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    return json.loads(body, object_pairs_hook=unique)


def load(path):
    return parse_json(path.read_bytes())


def validate_destination(destination):
    """Reject traversal, existing targets and symlink ancestry before any write."""
    allowed = Path("/private/tmp")
    require(destination.is_absolute(), "scratch destination must be absolute")
    require(".." not in destination.parts, "scratch destination traversal rejected")
    require(destination.is_relative_to(allowed), "scratch destination prefix rejected")
    require(destination != allowed, "scratch root is not a fresh destination")
    for ancestor in (destination, *destination.parents):
        require(
            not ancestor.is_symlink(), "scratch destination symlink ancestry rejected"
        )
        if ancestor != destination and ancestor.exists():
            require(ancestor.is_dir(), "scratch ancestor is not a directory")
        if ancestor == allowed:
            break
    resolved = destination.resolve()
    require(
        resolved.is_relative_to(allowed.resolve()),
        "resolved scratch destination escapes root",
    )
    require(not destination.exists(), "materialization requires a new directory")
    return resolved


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


class Decoder:
    def __init__(self, root, repo):
        self.root = root
        self.repo = repo
        self.contents = load(root / "content-map.json")
        proof_rows = load(root / "existing-owner-verification.json")
        self.proofs = {(r["git_commit"], r["path"]): r for r in proof_rows}
        require(len(self.proofs) == len(proof_rows), "duplicate inherited proof")
        expected_owners = {
            (r["storage"]["git_commit"], r["storage"]["path"])
            for r in self.contents.values()
            if r["storage"]["kind"] == "existing_repository"
        }
        require(
            set(self.proofs) == expected_owners, "inherited proof coverage mismatch"
        )
        self.baseline = load(root / "merged-baseline-binding.json")
        require(self.baseline["git_commit"] == BASE, "unexpected baseline commit")
        require(self.baseline["git_tree"] == TREE, "unexpected baseline tree")
        actual = (
            subprocess.check_output(["git", "rev-parse", BASE + "^{tree}"], cwd=repo)
            .decode()
            .strip()
        )
        require(actual == TREE, "actual baseline tree mismatch")
        self.batch = subprocess.Popen(
            ["git", "cat-file", "--batch"],
            cwd=repo,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        self.cache = {}

    def close(self):
        self.batch.stdin.close()
        require(self.batch.wait() == 0, "git batch failed")

    def endpoint(self, storage):
        kind = storage["kind"]
        if kind == "existing_repository":
            require(storage["git_commit"] == BASE, "inherited commit mismatch")
            require(storage["git_tree"] == TREE, "inherited tree mismatch")
            path = storage["path"]
            safe(Path("/bounded-git-owner"), path)
            proof = self.proofs[(BASE, path)]
            require(proof["git_tree"] == TREE, "proof tree mismatch")
            require(
                proof["sha256"] == storage["stored_sha256"], "proof digest mismatch"
            )
            require(proof["bytes"] == storage["stored_bytes"], "proof size mismatch")
            self.batch.stdin.write((BASE + ":" + path + "\n").encode())
            self.batch.stdin.flush()
            header = self.batch.stdout.readline().split()
            require(len(header) == 3 and header[1] == b"blob", "missing Git blob")
            require(
                header[0].decode() == proof["git_blob"], "Git blob identity mismatch"
            )
            require(int(header[2]) == storage["stored_bytes"], "Git blob size mismatch")
            body = self.batch.stdout.read(int(header[2]))
            require(self.batch.stdout.read(1) == b"\n", "invalid Git batch boundary")
        elif kind == "new_retention_object":
            require(storage["stored_bytes"] < LIMIT, "oversize new endpoint")
            body = safe(self.root, storage["path"]).read_bytes()
        elif kind == "new_retention_chunks":
            chunks = storage["chunks"]
            require(bool(chunks), "empty chunk list")
            require(
                sum(c["bytes"] for c in chunks) == storage["stored_bytes"],
                "chunk total",
            )
            pieces = []
            offset = 0
            for chunk in chunks:
                require(chunk["offset"] == offset, "chunk order or offset mismatch")
                require(0 < chunk["bytes"] < LIMIT, "oversize or empty chunk")
                piece = safe(self.root, chunk["path"]).read_bytes()
                check(piece, chunk["sha256"], chunk["bytes"])
                pieces.append(piece)
                offset += len(piece)
            body = b"".join(pieces)
        else:
            raise ValueError("unknown storage kind")
        check(body, storage["stored_sha256"], storage["stored_bytes"])
        return body

    def decode(self, digest):
        if digest in self.cache:
            return self.cache[digest]
        row = self.contents[digest]
        require(row["source_sha256"] == digest, "content key mismatch")
        body = self.endpoint(row["storage"])
        require(len(row["decode_steps"]) <= 16, "excessive decode chain")
        for step in row["decode_steps"]:
            require(step["encoding"] == "gzip", "unsupported decode encoding")
            require(sha(body) == step["input_sha256"], "decode input mismatch")
            body = gunzip(body, step["output_sha256"], step["output_bytes"])
        check(body, digest, row["source_bytes"])
        # Bounded cache: large originals remain transient, never silently truncated.
        if len(body) < 1024 * 1024:
            if len(self.cache) > 12000:
                self.cache.clear()
            self.cache[digest] = body
        return body


def physical_maps(root):
    spec = load(root / "source-specification.json")
    result = {}
    for package in spec["packages"]:
        name = package["name"]
        safe(Path("/package"), name)
        obj = load(root / "packages" / name / "source-map.json")
        require(obj["name"] == name, "package name mismatch")
        rows = obj["source_occurrences"]
        for row in rows:
            safe(Path("/physical-package"), row["path"])
        require(len({r["path"] for r in rows}) == len(rows), "duplicate physical path")
        require(len(rows) == package["physical_artifacts"], "physical count mismatch")
        result[name] = {r["path"]: r for r in rows}
    return result


def declared_compact_identity(row):
    encoding = row.get("encoding", row.get("rule", "gzip"))
    identity = encoding in (
        "identity_existing_gzip",
        "source-gzip-identity",
        "identity",
    )
    require(
        identity
        or encoding
        in (
            "gzip",
            "lossless_gzip_companion",
            "lossless-gzip-companion-deduplicated-by-raw-sha256",
        ),
        "unknown declared compact encoding",
    )
    return {
        "original_path": row.get(
            "original_path", row.get("logical_path", row.get("original"))
        ),
        "original_sha256": row.get("original_sha256", row.get("raw_sha256")),
        "original_bytes": row.get("original_bytes", row.get("raw_bytes")),
        "stored_path": row.get("stored_path", row.get("stored")),
        "stored_sha256": row["stored_sha256"],
        "stored_bytes": row["stored_bytes"],
        "encoding": "identity" if identity else "gzip",
    }


def verify_compact(root, decoder, maps, destination=None):
    pairs = load(root / "verified-compact-pairs.json")
    index = {}
    for pair in pairs:
        key = (pair["package"], pair["compact_map"], pair["array"], pair["index"])
        require(key not in index, "duplicate compact pair")
        index[key] = pair
    expected = set()
    logical = {}
    spec = load(root / "source-specification.json")
    for package in spec["packages"]:
        name = package["name"]
        for compact in package["compact_maps"]:
            require(
                maps[name][compact["path"]]["sha256"] == compact["sha256"],
                "compact manifest physical owner mismatch",
            )
            manifest = decoder.decode(compact["sha256"])
            check(manifest, compact["sha256"], compact["bytes"])
            obj = json.loads(manifest)
            require(
                sorted(obj) == compact["top_level_keys"],
                "compact manifest keys changed",
            )
            rows = obj[compact["array"]]
            require(len(rows) == compact["expected_rows"], "compact manifest count")
            for i, declared in enumerate(rows):
                key = (name, compact["path"], compact["array"], i)
                expected.add(key)
                pair = index[key]
                require(pair["declared_row"] == declared, "compact declaration changed")
                expected_identity = declared_compact_identity(declared)
                require(
                    all(pair[k] == v for k, v in expected_identity.items()),
                    "compact normalized identity changed",
                )
                require(
                    maps[name][pair["stored_path"]]["sha256"] == pair["stored_sha256"],
                    "compact physical owner mismatch",
                )
                stored = decoder.decode(pair["stored_sha256"])
                check(stored, pair["stored_sha256"], pair["stored_bytes"])
                if pair["encoding"] == "gzip":
                    original = gunzip(
                        stored, pair["original_sha256"], pair["original_bytes"]
                    )
                else:
                    require(pair["encoding"] == "identity", "unknown compact encoding")
                    original = stored
                    check(original, pair["original_sha256"], pair["original_bytes"])
                for inner in pair["inner_payloads"]:
                    gunzip(original, inner["sha256"], inner["bytes"])
                present = pair["original_path"] in maps[name]
                require(
                    present == pair["original_physically_present"],
                    "logical presence mismatch",
                )
                if present:
                    require(
                        decoder.decode(maps[name][pair["original_path"]]["sha256"])
                        == original,
                        "physical and logical originals differ",
                    )
                else:
                    logical_key = (name, pair["original_path"])
                    require(
                        logical.get(logical_key, pair["original_sha256"])
                        == pair["original_sha256"],
                        "conflicting logical path",
                    )
                    logical[logical_key] = pair["original_sha256"]
                    if destination:
                        path = safe(destination / name, pair["original_path"])
                        path.parent.mkdir(parents=True, exist_ok=True)
                        if path.exists():
                            require(
                                path.read_bytes() == original,
                                "logical overwrite conflict",
                            )
                        else:
                            path.write_bytes(original)
                        check(
                            path.read_bytes(),
                            pair["original_sha256"],
                            pair["original_bytes"],
                        )
    require(expected == set(index), "compact coverage mismatch")
    return {
        "declared_rows_verified": len(expected),
        "compact_only_originals": len(logical),
    }


def historical_plan(root, decoder):
    """Derive the complete expected history from pinned originals, not surviving rows."""
    path = root / "historical-compact-references.json"
    require(path.is_file(), "final historical compact metadata is required")
    obj = load(path)
    binding = obj["prior_pairs_binding"]
    require(binding == HISTORICAL_BINDING, "historical compact pinned binding changed")
    stored = safe(root, binding["retained_gzip"]).read_bytes()
    require(
        sha(stored) == binding["retained_sha256"],
        "historical compact map representation",
    )
    original = gunzip(stored, binding["sha256"], binding["bytes"])
    git_original = subprocess.check_output(
        ["git", "show", BASE + ":" + binding["path"]], cwd=decoder.repo
    )
    check(git_original, binding["sha256"], binding["bytes"])
    blob = hashlib.sha1(
        b"blob " + str(len(git_original)).encode() + b"\0" + git_original
    ).hexdigest()
    require(
        blob == binding["git_blob"] and git_original == original,
        "historical compact actual Git owner mismatch",
    )
    canonical = parse_json(original)
    maps = physical_maps(root)
    physical_contents = {
        row["sha256"] for rows in maps.values() for row in rows.values()
    }
    accounted_contents = set(physical_contents)
    additional = []
    expected_rows = []
    expected_paths = {}
    manifest_bindings = []
    for owner, prior_manifest, copied_manifest, expected_count in HISTORICAL_MAPS:
        pairs = [
            p
            for p in canonical
            if p["package"] == owner and p["compact_map"] == prior_manifest
        ]
        require(
            len(pairs) == expected_count,
            "historical canonical declaration count changed",
        )
        indexed = {p["index"]: p for p in pairs}
        require(
            len(indexed) == expected_count
            and set(indexed) == set(range(expected_count)),
            "historical canonical indexes are incomplete or duplicated",
        )
        manifest_hashes = {p["compact_map_sha256"] for p in pairs}
        require(
            len(manifest_hashes) == 1, "historical source manifest identity conflict"
        )
        manifest_hash = manifest_hashes.pop()
        occurrence = maps["primary"][copied_manifest]
        require(
            occurrence["sha256"] == manifest_hash,
            "copied historical source manifest binding changed",
        )
        manifest_body = decoder.decode(manifest_hash)
        check(manifest_body, manifest_hash, occurrence["bytes"])
        declarations = parse_json(manifest_body)["rows"]
        require(
            len(declarations) == expected_count,
            "copied historical declaration count changed",
        )
        manifest_bindings.append(
            {
                "current_package": "primary",
                "path": copied_manifest,
                "sha256": manifest_hash,
                "bytes": len(manifest_body),
                "original_owner_package": "next266-" + owner,
                "declarations": expected_count,
            }
        )
        for index, declared in enumerate(declarations):
            pair = indexed[index]
            require(
                pair["declared_row"] == declared,
                "copied historical declaration changed",
            )
            require(
                all(
                    pair[k] == v for k, v in declared_compact_identity(declared).items()
                ),
                "historical declaration normalization changed",
            )
            expected_rows.append(
                {
                    "current_package": "primary",
                    "current_manifest": copied_manifest,
                    "current_manifest_sha256": manifest_hash,
                    "original_owner_package": "next266-" + owner,
                    "original_compact_pair": pair,
                }
            )
            for kind in ("original", "stored"):
                digest = pair[kind + "_sha256"]
                if digest not in accounted_contents:
                    additional.append(digest)
                    accounted_contents.add(digest)
                relative = "next266-" + owner + "/" + pair[kind + "_path"]
                safe(Path("/historical-root"), relative)
                require(
                    expected_paths.get(relative, digest) == digest,
                    "historical canonical path conflict",
                )
                expected_paths[relative] = digest
    require(
        len(expected_rows) == 477 and len(expected_paths) == 926,
        "historical expected coverage changed",
    )
    require(
        obj["rows"] == expected_rows,
        "historical declarations or original owner roles changed",
    )
    require(
        obj["additional_content_rows"] == additional and len(additional) == 388,
        "historical supplemental content coverage changed",
    )
    return {
        "rows": expected_rows,
        "expected_paths": expected_paths,
        "source_manifest_bindings": manifest_bindings,
        "control_sha256": {
            "historical-compact-references.json": sha(path.read_bytes()),
            binding["retained_gzip"]: sha(stored),
            "physical_source_maps": {
                name: sha((root / "packages" / name / "source-map.json").read_bytes())
                for name in maps
            },
        },
    }


def verify_historical(root, decoder, destination=None):
    plan = historical_plan(root, decoder)
    count = 0
    paths = {}
    for row in plan["rows"]:
        pair = row["original_compact_pair"]
        stored = decoder.decode(pair["stored_sha256"])
        original = decoder.decode(pair["original_sha256"])
        require(
            gunzip(stored, pair["original_sha256"], pair["original_bytes"]) == original,
            "historical compact decoding mismatch",
        )
        for kind, body in (("original", original), ("stored", stored)):
            relative = row["original_owner_package"] + "/" + pair[kind + "_path"]
            require(
                paths.get(relative, sha(body)) == sha(body), "historical path conflict"
            )
            paths[relative] = sha(body)
            if destination:
                target = safe(destination, relative)
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    require(
                        target.read_bytes() == body, "historical overwrite conflict"
                    )
                else:
                    target.write_bytes(body)
                require(
                    sha(target.read_bytes()) == sha(body),
                    "historical materialization mismatch",
                )
        count += 1
    require(
        count == 477 and paths == plan["expected_paths"],
        "historical reconstruction coverage mismatch",
    )
    return {
        "status": "pass",
        "declared_rows": count,
        "distinct_reference_paths": len(paths),
        "source_manifest_bindings": plan["source_manifest_bindings"],
        "control_sha256": plan["control_sha256"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).parent)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--materialize", type=Path)
    parser.add_argument("--compare-originals", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    dest = args.materialize
    if dest:
        dest = validate_destination(dest)
    decoder = Decoder(args.root, args.repo)
    maps = physical_maps(args.root)
    count = 0
    total = 0
    try:
        historical_plan(args.root, decoder)
        if dest:
            dest.mkdir(parents=True)
        for name, rows in maps.items():
            for relative, row in rows.items():
                body = decoder.decode(row["sha256"])
                check(body, row["sha256"], row["bytes"])
                if args.compare_originals:
                    require(
                        Path(row["source"]).read_bytes() == body, "original changed"
                    )
                if dest:
                    path = safe(dest / "physical" / name, relative)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    require(not path.exists(), "physical overwrite rejected")
                    path.write_bytes(body)
                    check(path.read_bytes(), row["sha256"], row["bytes"])
                count += 1
                total += len(body)
            print("verified", name, len(rows), flush=True)
        compact = verify_compact(
            args.root, decoder, maps, dest / "logical" if dest else None
        )
        historical = verify_historical(
            args.root, decoder, dest / "historical" if dest else None
        )
    finally:
        decoder.close()
    result = {
        "status": "pass",
        "physical_occurrences": count,
        "physical_bytes": total,
        "compact": compact,
        "historical": historical,
        "fresh_materialization": str(dest) if dest else None,
        "originals_compared": args.compare_originals,
        "actual_git_commit": BASE,
        "actual_git_tree": TREE,
        "control_sha256": {
            name: sha((args.root / name).read_bytes())
            for name in (
                "content-map.json",
                "source-specification.json",
                "existing-owner-verification.json",
                "verified-compact-pairs.json",
                "decode_retained.py",
                "historical-compact-references.json",
            )
        },
    }
    if args.receipt:
        dump(args.receipt, result)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
