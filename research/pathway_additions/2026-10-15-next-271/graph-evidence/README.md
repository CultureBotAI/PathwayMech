# Retained next271 graph evidence

This directory mechanically retains the complete frozen graph-design and independent-graph-review packets. It creates no new scientific acceptance. Original verdicts, independence, limitations, failed attempts, manifests and freeze proofs remain byte-exact. Subsequent authority implementation, maintained record changes and publication are outside this packaging task.

All 3,497 physical source files (327,605,938 decoded member bytes) are retained in 12 deterministic archives (70,031,342 compressed bytes). The largest archive is 16,206,214 bytes, strictly below 40 MiB. Every part was fully decoded and reproduced byte-identically by a second stream from the originals, without an intermediate source-copy tree.

| Frozen packet | Physical files | Parts | Compressed bytes |
| --- | ---: | ---: | ---: |
| graph-design | 1698 | 6 | 34634267 |
| independent-graph-review | 1799 | 6 | 35397075 |

`retention.json` binds each source manifest/freeze, every physical relative file/member name, size and SHA-256, each compressed archive and the complete decoded outer tar stream. All hidden/ignored files and failed attempts are included. Members are regular files sorted by source-relative name, split into consecutive parts without splitting or omitting a file. Tar mode/uid/gid/names/mtime are fixed; gzip has no filename and mtime 0. Empty directory metadata is not a retained payload; original manifests preserve any declared directory inventory.

Nested predecessor archives are opaque byte-exact file payloads; their inner members are not newly decoded or reviewed. Absolute paths inside original evidence remain unchanged provenance. The new index, archives and portable commands use relative paths.

Portable verification needs only this directory and an existing standard-library Python3 runtime:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 python3 -B retain.py verify --output .
PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 python3 -B check_archived_manifests.py .
```

The first checks complete compressed bytes, full decoded tar bytes, safe/unique/expected regular members, stable metadata and every member hash. The second reads the archived manifests/freezes and cross-checks their declared files against every indexed outer member. Both are read-only and require no original owner paths.

Reproduction from the two unchanged frozen owners requires a fresh output directory:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 python3 -B retain.py build --sources-root ROOT --output FRESH
```

The builder refuses overwrite and binds the exact expected manifest/freezes before streaming originals. No installation or network is required. The copied source packet histories keep the actual merged baseline and endpoint successor distinct. No new source-exhaustion, alias, final-record, browser/pixel or issue-closure claim is made. Parent owns maintained integration and subsequent gates.

## Maintained verification helper correction

The initial full-repository lint check found style errors in the copied verification helpers ([issue #631](https://github.com/CultureBotAI/PathwayMech/issues/631)). The maintained Python copies now use repository-compliant formatting and imports. `script-originals/` preserves both original copies as `.py.txt` files. `helper-formatting-successor.json` binds old and new hashes, exact non-import AST and literal-value equality, the passing repository lint check, and independent successful portable replays with their complete logs. The frozen packets, archives, index and original verification receipts remain byte-identical. This correction does not revise their scientific findings.
