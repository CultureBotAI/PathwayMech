"""Deterministic mechanical retention. Read-only sources; fresh output required."""

import argparse
import gzip
import hashlib
import json
import stat
import tarfile
from pathlib import Path, PurePosixPath

SPECS = [
    (
        "graph-design",
        "c680126985a8447ac0ef5d9f3f6ea14512c55cb74e1a1cc3ca948c0dcf8e1882",
        "20d9e5413f12e6ce147897fa2534cec8bca8edf1f8f943893a21d59635ccc530",
    ),
    (
        "independent-graph-review",
        "04a24f56a0b657318fa2961a5bf041954ca7f5d0b00922b868f11463dc61b651",
        "8440331aaedbe44ded0baa515b853cb78995402f9501e24ae7459b3f246d3372",
    ),
]

CAP = 40 * 1024 * 1024
BUDGET = 36 * 1024 * 1024


def digest(stream):
    h = hashlib.sha256()
    size = 0
    for b in iter(lambda: stream.read(1024 * 1024), b""):
        h.update(b)
        size += len(b)
    return size, h.hexdigest()


def info(path):
    with path.open("rb") as f:
        n, h = digest(f)
    return {"bytes": n, "sha256": h}


def safe(name):
    p = PurePosixPath(name)
    return (
        bool(name)
        and not p.is_absolute()
        and "\\" not in name
        and "\x00" not in name
        and all(x not in ("", ".", "..") for x in name.split("/"))
        and p.as_posix() == name
    )


def inventory(root, slug, mh, fh):
    owner = root / ("pathwaymech-next-271-" + slug)
    mn, fn = "artifact-manifest.json", "freeze-proof.json"
    assert info(owner / mn)["sha256"] == mh, (slug, "manifest")
    assert info(owner / fn)["sha256"] == fh, (slug, "freeze")
    m = json.loads((owner / mn).read_text())
    f = json.loads((owner / fn).read_text())
    assert f["manifest_sha256"] == mh
    declared = {}
    for x in m["files"]:
        assert safe(x["path"]) and x["path"] not in declared
        declared[x["path"]] = x
    paths = []
    for p in owner.rglob("*"):
        s = p.lstat()
        assert not stat.S_ISLNK(s.st_mode), (slug, p, "symlink")
        if stat.S_ISDIR(s.st_mode):
            continue
        assert stat.S_ISREG(s.st_mode), (slug, p, "not regular")
        paths.append(p.relative_to(owner).as_posix())
    assert set(paths) == set(declared) | {mn, fn}, (slug, "physical inventory")
    rows = []
    for name in sorted(paths):
        assert safe(name)
        x = info(owner / name)
        if name in declared:
            assert (
                x["bytes"] == declared[name]["bytes"] and x["sha256"] == declared[name]["sha256"]
            ), (slug, name)
        rows.append({"path": name, **x})
    assert len(rows) == f["physical_files"]
    assert len(declared) == f["listed_files"]
    return owner, {
        "packet_id": slug,
        "source_owner_basename": owner.name,
        "manifest": {"path": mn, **info(owner / mn)},
        "freeze": {"path": fn, **info(owner / fn)},
        "listed_source_files": len(declared),
        "physical_source_files": len(rows),
        "source_bytes": sum(x["bytes"] for x in rows),
        "files": rows,
    }


class HashSink:
    def __init__(self):
        self.hash = hashlib.sha256()
        self.size = 0

    def write(self, b):
        self.hash.update(b)
        self.size += len(b)
        return len(b)

    def flush(self):
        pass


def emit(owner, slug, rows, dest):
    with gzip.GzipFile(filename="", mode="wb", fileobj=dest, mtime=0, compresslevel=9) as gz:
        with tarfile.open(fileobj=gz, mode="w|", format=tarfile.PAX_FORMAT) as tar:
            for row in rows:
                ti = tarfile.TarInfo(slug + "/" + row["path"])
                ti.size = row["bytes"]
                ti.mtime = 0
                ti.uid = ti.gid = 0
                ti.uname = ti.gname = ""
                ti.mode = 0o644
                ti.type = tarfile.REGTYPE
                ti.pax_headers = {}
                with (owner / row["path"]).open("rb") as stream:
                    tar.addfile(ti, stream)


def decode_check(path, archive, packet):
    assert info(path) == {k: archive[k] for k in ["bytes", "sha256"]}
    assert path.stat().st_size < CAP
    with path.open("rb") as h:
        header = h.read(10)
    assert header[:4] == b"\x1f\x8b\x08\x00" and header[4:8] == b"\x00" * 4
    with gzip.open(path, "rb") as h:
        n, d = digest(h)
    expected = {x["member_path"]: x for x in archive["members"]}
    seen = []
    with tarfile.open(path, "r|gz") as tar:
        for m in tar:
            assert m.isfile() and safe(m.name) and m.name in expected and m.name not in seen, (
                path,
                m.name,
            )
            assert (
                m.mode == 0o644
                and m.uid == m.gid == 0
                and m.uname == m.gname == ""
                and m.mtime == 0
            )
            assert set(m.pax_headers) <= {"path"}
            seen.append(m.name)
            row = expected[m.name]
            assert m.size == row["bytes"]
            with tar.extractfile(m) as h:
                size, sha = digest(h)
            assert size == row["bytes"] and sha == row["sha256"], (path, m.name)
    assert seen == sorted(expected) and len(seen) == len(expected)
    return {
        "decoded_tar_bytes": n,
        "decoded_tar_sha256": d,
        "decoded_outer_members": len(seen),
        "decoded_member_bytes": sum(x["bytes"] for x in expected.values()),
    }


def verify(out, sources=None):
    r = json.loads((out / "retention.json").read_text())
    allmembers = []
    archives = []
    for p in r["packets"]:
        covered = []
        for a in p["archives"]:
            assert safe(a["path"])
            v = decode_check(out / a["path"], a, p)
            assert all(v[k] == a[k] for k in v)
            covered += a["members"]
            archives.append(a["path"])
        rows = {x["path"]: x for x in p["files"]}
        assert len(rows) == len(p["files"])
        assert len(covered) == len(rows)
        assert {x["source_relative_path"] for x in covered} == set(rows)
        for x in covered:
            assert x["member_path"] == p["packet_id"] + "/" + x["source_relative_path"] and {
                k: x[k] for k in ["bytes", "sha256"]
            } == {k: rows[x["source_relative_path"]][k] for k in ["bytes", "sha256"]}
        allmembers += covered
        if sources:
            spec = next(s for s in SPECS if s[0] == p["packet_id"])
            _, actual = inventory(sources, *spec)
            assert all(actual[k] == p[k] for k in actual)
    assert len(archives) == len(set(archives))
    assert set(
        x.relative_to(out).as_posix() for x in (out / "archives").rglob("*") if x.is_file()
    ) == set(archives)
    assert len(allmembers) == r["totals"]["physical_source_files"]
    assert sum(x["bytes"] for x in allmembers) == r["totals"]["decoded_member_bytes"]
    return {
        "archives_verified": len(archives),
        "decoded_outer_members_verified": len(allmembers),
        "decoded_member_bytes": sum(x["bytes"] for x in allmembers),
        "source_originals_rechecked": bool(sources),
        "nested_containers": (
            "opaque byte-exact payloads; no inner inventory or scientific rereading claim"
        ),
    }


def build(out, sources):
    assert not out.exists(), "Use a fresh output directory; no overwrite of frozen retention."
    out.mkdir(parents=True)
    (out / "archives").mkdir()
    packets = []
    for slug, mh, fh in SPECS:
        owner, p = inventory(sources, slug, mh, fh)
        chunks = []
        chunk = []
        size = 10240
        for row in p["files"]:
            weight = ((row["bytes"] + 511) // 512) * 512 + 4096
            if chunk and size + weight > BUDGET:
                chunks.append(chunk)
                chunk = []
                size = 10240
            chunk.append(row)
            size += weight
        if chunk:
            chunks.append(chunk)
        archives = []
        for j, rows in enumerate(chunks, 1):
            rel = f"archives/{slug}.part-{j:03d}.tar.gz"
            target = out / rel
            with target.open("xb") as stream:
                emit(owner, slug, rows, stream)
            a = {
                "path": rel,
                "packet_id": slug,
                "part": j,
                "parts": len(chunks),
                **info(target),
                "members": [
                    {
                        "member_path": slug + "/" + x["path"],
                        "source_relative_path": x["path"],
                        "bytes": x["bytes"],
                        "sha256": x["sha256"],
                    }
                    for x in rows
                ],
            }
            assert a["bytes"] < CAP, (slug, j, "oversized artifact; no member omitted")
            a.update(decode_check(target, a, p))
            sink = HashSink()
            emit(owner, slug, rows, sink)
            assert sink.size == a["bytes"] and sink.hash.hexdigest() == a["sha256"]
            a["second_stream_exact"] = True
            archives.append(a)
        p["archives"] = archives
        packets.append(p)
        print(
            "PACKED",
            slug,
            p["physical_source_files"],
            "files",
            len(archives),
            "parts",
            sum(x["bytes"] for x in archives),
            "compressed bytes",
            flush=True,
        )
    r = {
        "schema_version": 1,
        "scope": (
            "Mechanical retention of two explicitly authorized frozen graph-design and "
            "independent-graph-review packets only. Scientific verdicts and reviewer "
            "independence remain in each byte-exact packet; this retention is not a new "
            "acceptance."
        ),
        "baseline": {
            "actual_merge": "63ebb3b3e29ca1ed6472597104347d9fbc98f4a5",
            "tree": "5448122efcfbd8ae2ac90ad42e70557b03d9b78e",
            "qualification": (
                "Both packets bind the actual merged baseline; the separately accepted "
                "endpoint successor is retained distinctly in their original provenance."
            ),
        },
        "portable_paths": (
            "Archive and member paths are relative; source_owner_basename identifies "
            "provenance, not an extraction destination or required absolute path."
        ),
        "format": {
            "container": "tar+gzip",
            "regular_members_only": True,
            "member_order": "lexicographically sorted per packet; consecutive split parts",
            "tar_format": "PAX",
            "mode": "0644",
            "uid": 0,
            "gid": 0,
            "uname": "",
            "gname": "",
            "mtime": 0,
            "gzip_filename": "",
            "gzip_mtime": 0,
            "gzip_level": 9,
            "compressed_limit_bytes": CAP,
            "partition_budget_bytes": BUDGET,
            "partition_method": (
                "Conservative payload padded to512 plus4096 bytes per member; no member "
                "split or omission."
            ),
            "second_stream_byte_reproduction": True,
        },
        "limits": [
            (
                "Every physical source-owner file included, including manifest/freeze, "
                "failures and hidden/ignored files."
            ),
            (
                "Nested containers are retained and hashed as opaque outer file "
                "payloads; their contents are not decoded or newly scientifically "
                "reviewed."
            ),
            (
                "Only the frozen graph-design and independent-graph-review owners are "
                "packaged. Later authority/record implementation and maintained "
                "integration/history are outside this packaging scope."
            ),
            (
                "This index carries no new scientific verdict, global "
                "discovery/exhaustion claim or issue closure."
            ),
        ],
        "packets": packets,
    }
    aa = [a for p in packets for a in p["archives"]]
    r["totals"] = {
        "packets": len(packets),
        "archives": len(aa),
        "physical_source_files": sum(p["physical_source_files"] for p in packets),
        "decoded_member_bytes": sum(p["source_bytes"] for p in packets),
        "compressed_archive_bytes": sum(a["bytes"] for a in aa),
        "decoded_tar_bytes": sum(a["decoded_tar_bytes"] for a in aa),
        "largest_compressed_archive_bytes": max(a["bytes"] for a in aa),
    }
    (out / "retention.json").write_text(json.dumps(r, indent=2) + "\n")
    v = verify(out, sources)
    print(json.dumps({"totals": r["totals"], "final_verification": v}, indent=2), flush=True)
    return r, v


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["build", "verify"])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--sources-root", type=Path)
    args = parser.parse_args()
    if args.action == "build":
        assert args.sources_root, "build requires read-only source root"
        build(args.output, args.sources_root)
    else:
        print(json.dumps(verify(args.output, args.sources_root), indent=2))
