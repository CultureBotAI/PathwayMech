# Retained complete record and independent authority review

This package preserves exactly two frozen packets as original bytes. It adds no scientific claim or new acceptance. Active canonical/scientific/integration review, root CI and later maintained-state history are outside its scope.

| Packet | Readable reports | Complete files | Archive parts |
| --- | --- | ---: | ---: |
| Complete ethanolamine record preparation | [Handoff](reports/complete-record-preparation/HANDOFF.md), [record preparation](reports/complete-record-preparation/RECORD_PREPARATION.md), [operations](reports/complete-record-preparation/OPERATIONS.md) | 127 | 1 |
| Independent authority review | [Handoff](reports/independent-authority-review/HANDOFF.md), [review](reports/independent-authority-review/REVIEW.md), [result](reports/independent-authority-review/RESULT.json) | 552 | 4 |

The five deterministic archives retain all **679 physical files and 142,887,807 original bytes**, including hidden/ignored files, exact source manifests and freeze proofs, initial failed receipts, superseded drafts and corrections. The archives total **17,958,120 compressed bytes**; the largest is **5,193,668 bytes**, below the 40 MiB bound. Every archive was fully decoded, checked member by member and reproduced byte-identically in a second stream. No full source-packet mirror is required outside these archives.

`packet-specifications.json` pins the exact source releases. `retention.json` records every original relative path, byte count and hash; each archive/member hash; decoded tar stream hashes; and the six exact readable report copies. The two pinned source manifest hashes are:

- Complete record preparation: `fa1fca048f61b47ab3f626f888006962d19b7b730cd412c6678f4984c3879758`.
- Independent authority review: `2be3465bf19b4e3b428ba224a4fee0d85c2ed2efdd59b66818f1b22b161b5cef`.

The record-preparation packet contains the corrected candidate `ethanolamine-utilization.yaml`, SHA256 `f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e`, its exact 97-edge/128-declaration graph preservation, source-to-record mappings and structural checks. The historical `results/pre-coefficient-wording-candidate.yaml` remains preserved but is not the recommended candidate. Its correction receipt distinguishes nine distinct ancillary EutT material slots from coefficient-two material amounts. Finding 634's magnesium/citation corrections are retained at their original scope; neither this preparation nor packaging closes the issue.

The independent authority packet preserves its qualified acceptance of the finite 63-original adapter, the issue 635 host-guard successor and hash-bound additive integration candidates. It retains the initial failing mutation, later successful tests and reproduction receipts. Authority/code/integration acceptance is separate from canonical pathway science, rendered behavior and publication. Packaging does not extend that verdict or establish actual merged issue closure.

All tar members are regular files, sorted within each packet, with fixed mode, owner and time. Gzip has no filename and an mtime of zero. Consecutive parts never mix packets or omit individual files. Nested containers remain opaque byte-exact payloads; no new interior inventory, primary reading or scientific review is claimed. An unsuccessful download remains its exact failure body irrespective of its extension. Original absolute provenance paths remain unchanged inside the packets and are not portable-verifier inputs.

## Portable checks

From this directory, an existing Python 3.10+ runtime is sufficient; no dependency installation, network, Git, caches or temporary source owners are needed:

```sh
python3 -I -B retain.py verify --output .
python3 -I -B check_archived_manifests.py .
```

The first command checks scope pins, archive/member bytes and metadata, complete physical coverage and readable-copy correspondence. The second independently decodes the archived manifests/freezes and checks their declared files against the portable index. Both are read-only and perform no extraction.

The same checks were also run through an audit guard that rejects reads from unrelated `/private/tmp/pathwaymech-*` owners:

```sh
python3 -I -B portable_guard.py . retain
python3 -I -B portable_guard.py . manifests
```

Portable receipts report `source_originals_rechecked: false`; source originals were checked only during initial build. Exact commands, exits and output are retained in `verification/`. The maintained helpers pass Ruff with the repository configuration, BLE001 and `--no-cache`, plus format-check. Historical Python originals remain inside their byte-exact archives rather than becoming unreviewed active source files.

A fresh rebuild can use `retain.py build --sources-root ROOT --output FRESH` with the two pinned frozen owner directories beneath ROOT. Existing output is rejected. `verification/pattern-bindings.json` records the proven `accepted-preparation` helper origin; archive/verification logic is reused, with packet-scope prose adjusted to these two packets. This directory does not modify or replace the prior retention package.
