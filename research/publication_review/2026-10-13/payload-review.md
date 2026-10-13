# Cumulative publication payload audit

Read-only audit of `/private/tmp/pathwaymech-next-243-local-20261012`, base `e1c66917e753105c4bf5b7b026193fcefa2b000f` through head `70903536191206d2586cd23e46f7d70c32fef92e`. Destination `https://github.com/CultureBotAI/PathwayMech` was confirmed PUBLIC by `gh repo view`. This report makes no public change, licensing-clearance claim, or decision on behalf of automatic approval review. No tests were repeated.

## Concrete transfer scope

- Nine commits, 2,865 changed paths: 2,844 additions and 21 modifications.
- 2,639 newly reachable Git objects, including 2,119 distinct blobs totaling **825,396,927 bytes** (787.16 MiB). This includes intermediate committed versions, not merely the final tree.
- Local thin-pack simulation (`git pack-objects --stdout --revs --thin --delta-base-offset`, head minus base) produced **583,692,811 bytes** (556.65 MiB). Actual push negotiation can differ; this was a local measurement, not an upload.
- The final changed-file footprint is **689,121,529 bytes**; deduplicating those final files by Git blob ID gives 664,794,483 bytes.
- Research dossiers account for **633,749,159 new blob bytes**; 51 files beneath their `archives/` directories total **559,295,298 bytes**. The payload retains original source bodies and extensive review/build provenance, not only pathway YAML and generated pages.
- Largest individual blob: `research/pathway_additions/2026-10-12-next-233/archives/author.zip`, **48,038,783 bytes**. Second: next-233 `archives/adapter-implementation.zip`, **46,392,864 bytes**. No new blob reaches 50 MiB or 100 MiB; 24 are at least 10 MiB. Several logical ZIPs are split into ordered parts of at most 32 MiB.
- Other substantial new-history blob populations: `output/kgx` 153,342,941 bytes (nine successive node/edge versions), identifier-authority snapshots 20,748,656 bytes, and saved structured reviews 5,872,203 bytes.

| Dossier | New distinct blobs | Bytes |
| --- | ---: | ---: |
| 233 | 194 | 158,380,402 |
| 234 | 123 | 177,780,560 |
| 235 | 184 | 42,934,678 |
| 236 | 197 | 43,682,136 |
| 237 | 245 | 37,204,912 |
| 238 | 287 | 13,794,317 |
| 239 | 222 | 98,495,765 |
| 240 | 199 | 35,039,779 |
| 243 | 229 | 26,436,610 |

The previously reviewed next-233 subset alone was 158,380,402 research blob bytes. The current authorization decision should identify the whole cumulative head above, not reuse that earlier size as if it covered all nine dossiers.

## Source and archive provenance

The evidence indexes retain complete original-response bodies, whole-paper PDFs where acquired, bibliography bodies, source-database XML/OWL/PWML, accepted and rejected review/build packets, command receipts, test fixtures, source hashes, and local historical path/link metadata. They deliberately preserve failures, unavailable/error responses and source-access qualifications; retention itself is not a claim that every stored response supports a scientific assertion.

The source manifest grows from 792 to 893 rows: 103 new keys, two retired keys, and no altered surviving old row. Of the 103 new rows, 16 carry `CC-BY-4.0`; the other 87 expressly carry upstream/source-owned/BioCyc/PathBank/PubChem terms with public-release review or release deferred. New URL hosts represent 67 BioCyc mirror sources, 21 UniProt, seven NCBI, and two each Rhea, SGD, PubChem and PathBank. These labels are retained source metadata, not an independent legal review. The dossier READMEs and retained indexes explicitly state that public release/licensing clearance was not established. User deferral of that review does not establish clearance.

Next-240 explicitly retains a whole ~27 MB parent PathBank archive as well as its selected members. The portable indexes inherit earlier original groups. Historical fixture omissions and SQL-file omissions remain documented; the package is portable retained evidence, not a claim that all external native build dependencies are included.

## Configuration and privacy scope

The only changed top-level configuration paths are `conf/identifier_sources.json` and `conf/rhea_identifier_updates.json`; neither is an account-authentication configuration. No changed tracked path has a dot-prefixed component. The source manifest contains no authentication/token/secret/password/credential-named field and no `/Users/` value. Git object inventory is independent of `.gitignore`, and therefore is complete for the requested committed range, including all intermediate new blobs. Ignored uncommitted workspace files are not part of a Git push.

All nine commits use one author/committer identity with a `users.noreply.github.com` address; this audit did not reproduce the address. Provenance packets do retain local paths, agent names, command streams and inventories; those are themselves part of the public payload.

## Credential-content inspection

The completed heuristic scan visited **22,879 distinct byte bodies / 4,810,462,895 bytes**, including compressed container bytes and their decoded contents, across **253 ZIP containers, 743 gzip containers and 76,097 ZIP member views**. Seven actual multipart evidence ZIPs were reconstructed in committed part order and decoded. Deduplication used SHA-256, not file paths or gitignore rules. Nineteen distinct bodies began with a PDF header; this count is not a full-paper reading claim.

**No confirmed credential was found.** The patterns covered private-key headers; GitHub, AWS, Google API, Slack and OpenAI-style keys; AWS secret fields; bearer authorization fields; and HTTP URLs carrying user/password information. The only matches were three appearances of the same synthetic URL credential placeholder in two retained bodies: `tests/test_seed_subsystems.py` inside the next-233 adapter archive, and the same test line in next-234 formatter stdout. The URL uses `seed.example`; both userinfo strings are conventional four-character test placeholders. Values are not reproduced in this report. There were no sensitive-filename matches among tracked paths or decoded ZIP member names. Because content-addressed archives name many members by hash, content scanning—not member naming alone—is the substantive check.

Twelve ZIP-decode diagnostics are confined to **129- or 136-byte intentionally malformed/truncated test fixture fragments** under `test_portable_part_identity_*` / `test_portable_original_cannot_*`. Their raw bytes were scanned; every actual multipart evidence archive decoded successfully. No 256 MiB member-size or nesting-depth limit was reached. This is a pattern-based credential inspection, not proof that arbitrary secrets cannot occur in prose, images, PDF internals, or unrecognized encodings.

Privacy metadata is concrete: **310 distinct scanned bodies contain `/Users/` paths, and 7,057 contain `/private/tmp/` paths**. These include retained diagnostics, source inventories and historical receipts; those strings become public with the archives. The exact inventory and redacted hit dispositions remain in the external JSON scan artifact.

## Publication assessment

The material change relevant to approval is the cumulative **583,692,811-byte locally measured thin pack**, containing whole retained source/evidence bodies and local provenance metadata across all nine dossiers. I found no confirmed credential exposure or individual new Git blob at or above 50 MiB. Source release/licensing qualifications remain explicitly deferred in the payload; this audit neither clears them nor labels them an infringement. Approval should bind the exact cumulative head and public destination above. The earlier next-233-only payload description does not describe this transfer.

## Audit artifacts

All artifacts are outside the checkout; no publication payload was edited.

- `/private/tmp/pathwaymech-publish243-payload-inventory-20261013.json`: complete new-object inventory, changed paths, sizes and grouping.
- `/private/tmp/pathwaymech-publish243-pack-size-20261013.json`: exact local thin-pack measurement.
- `/private/tmp/pathwaymech-publish243-final-tree-20261013.json`: final changed-file sizes and source-label observations.
- `/private/tmp/pathwaymech-publish243-source-scope-20261013.json`: exact added source rows and term/domain counts.
- `/private/tmp/pathwaymech-publish243-content-scan-20261013.json`: archive-aware scan coverage, redacted credential-pattern fingerprints, container/member inventory and any scan limits.
- `/private/tmp/pathwaymech-publish243-scan-20261013.py`: scan implementation, retained for reproducibility.
