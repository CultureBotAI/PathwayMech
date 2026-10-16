"""Portable cross-check of decoded frozen manifests against every indexed outer member."""

import argparse
import hashlib
import json
import tarfile
from pathlib import Path, PurePosixPath


def check(base):
    index = json.loads((base / "retention.json").read_text())
    checks = []
    for packet in index["packets"]:
        slug = packet["packet_id"]
        rows = {x["path"]: x for x in packet["files"]}
        assert len(rows) == len(packet["files"])
        meta = {}
        for role in ["manifest", "freeze"]:
            rel = packet[role]["path"]
            member = slug + "/" + rel
            candidates = [
                a
                for a in packet["archives"]
                if any(m["member_path"] == member for m in a["members"])
            ]
            assert len(candidates) == 1
            with tarfile.open(base / candidates[0]["path"], "r:gz") as tar:
                matches = [m for m in tar if m.name == member]
                assert len(matches) == 1 and matches[0].isfile()
                raw = tar.extractfile(matches[0]).read()
            assert (
                len(raw) == packet[role]["bytes"]
                and hashlib.sha256(raw).hexdigest() == packet[role]["sha256"]
            )
            meta[role] = json.loads(raw)
        declared = {x["path"]: x for x in meta["manifest"]["files"]}
        assert len(declared) == len(meta["manifest"]["files"])
        assert set(rows) == set(declared) | {packet["manifest"]["path"], packet["freeze"]["path"]}
        for path, row in declared.items():
            assert not PurePosixPath(path).is_absolute() and all(
                x not in ("", ".", "..") for x in path.split("/")
            )
            assert row["bytes"] == rows[path]["bytes"] and row["sha256"] == rows[path]["sha256"]
        assert meta["freeze"]["manifest_sha256"] == packet["manifest"]["sha256"]
        assert meta["freeze"]["physical_files"] == len(rows) and meta["freeze"][
            "listed_files"
        ] == len(declared)
        covered = []
        for number, archive in enumerate(packet["archives"], 1):
            assert (
                archive["packet_id"] == slug
                and archive["part"] == number
                and archive["parts"] == len(packet["archives"])
            )
            for member in archive["members"]:
                assert member["member_path"] == slug + "/" + member["source_relative_path"]
                row = rows[member["source_relative_path"]]
                assert member["bytes"] == row["bytes"] and member["sha256"] == row["sha256"]
                covered.append(member["source_relative_path"])
        assert covered == sorted(rows) and len(covered) == len(set(covered))
        checks.append(
            {
                "packet_id": slug,
                "archived_manifest_sha256": packet["manifest"]["sha256"],
                "archived_freeze_sha256": packet["freeze"]["sha256"],
                "manifest_files_checked": len(declared),
                "all_physical_files_covered": len(rows),
                "parts": len(packet["archives"]),
                "all_passed": True,
            }
        )
    return {
        "status": "pass",
        "packets": checks,
        "listed_manifest_files": sum(x["manifest_files_checked"] for x in checks),
        "physical_files": sum(x["all_physical_files_covered"] for x in checks),
        "scope": (
            "Archived source manifest/freezes decoded and checked against every portable "
            "indexed member. Full member-byte verification is retain.py verify; nested "
            "containers remain opaque."
        ),
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("directory", type=Path)
    a = p.parse_args()
    print(json.dumps(check(a.directory), indent=2))
