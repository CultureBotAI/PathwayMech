# Retained next271 accepted preparation packets

This is mechanical, byte-exact retention of nine frozen preparation/review owners. Scientific verdicts, independence disclosures, failures and limits remain in their original packet files; packaging does not create a new scientific acceptance. Graph-design/review and later authority/record implementation are outside this set.

All 6,131 physical files (590,815,477 bytes) are retained in 24 archives (171,943,051 compressed bytes). The largest is 33,124,638 bytes, below 40 MiB. Every archive was streamed from its original, decoded exhaustively, compared with the frozen source inventory and reproduced byte-identically in a second stream. No source was copied into an intermediate working tree or modified.

| Frozen packet | Physical files | Parts | Compressed bytes |
| --- | ---: | ---: | ---: |
| discovery | 472 | 2 | 7207503 |
| independent-preflight-review | 499 | 2 | 7461703 |
| source-preparation | 1708 | 8 | 92405812 |
| independent-source-review | 1013 | 4 | 15845758 |
| issuer-preparation | 881 | 2 | 17843242 |
| independent-issuer-review | 968 | 2 | 20420339 |
| merged-baseline-independent-rebind | 362 | 2 | 9974512 |
| activity-endpoint-review | 62 | 1 | 247646 |
| activity-endpoint-implementation-review | 166 | 1 | 536536 |

`retention.json` is the portable index: it binds every source manifest/freeze, every relative source/member path and digest/size, every compressed archive and decoded outer tar stream. Tar members are regular files in sorted order with fixed metadata; gzip has no filename and mtime 0. Parts are consecutive segments of one packet inventory, never mixed across packets. Every hidden/ignored file, failed attempt and freeze/manifest is included.

Nested containers are preserved as opaque outer-file payloads. Their inner members are not decoded or newly scientifically reviewed by this retention. Earlier discovery/preflight baseline chronology is retained unchanged; the included actual baseline rebind concerns merge 63ebb3b3e29ca1ed6472597104347d9fbc98f4a5/tree 5448122efcfbd8ae2ac90ad42e70557b03d9b78e. No global novelty, source-exhaustion, alias or final-record claim is made.

With an existing Python3 runtime, portable verification needs only this directory:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 python3 -B retain.py verify --output .
PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 python3 -B check_archived_manifests.py .
```

The first command checks archive bytes, stable metadata, safe/unique/expected member paths, every decoded member and complete coverage. The second independently reads the archived manifests/freezes and cross-checks them against all indexed members. Both are read-only. Rebuilding requires the nine original frozen owners under a supplied source root and a fresh output directory; `retain.py build --sources-root ROOT --output FRESH` rejects overwrite and verifies each expected manifest/freeze. No installation is needed.

The original packets retain any absolute provenance paths verbatim. The new index and archive paths are relative and require no original path for portable verification. Parent owns maintained integration and any later review or issue closure.

## Maintained verification helper correction

The initial full-repository lint check found style errors in the copied verification helpers ([issue #631](https://github.com/CultureBotAI/PathwayMech/issues/631)). The maintained Python copies now use repository-compliant formatting and imports. `script-originals/` preserves both original copies as `.py.txt` files. `helper-formatting-successor.json` binds old and new hashes, exact non-import AST and literal-value equality, the passing repository lint check, and independent successful portable replays with their complete logs. The frozen packets, archives, index and original verification receipts remain byte-identical. This correction does not revise their scientific findings.
