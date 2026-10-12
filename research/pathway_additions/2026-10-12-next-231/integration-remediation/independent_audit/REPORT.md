# Independent PPi integration preparation audit

**Verdict: needs correction before maintained execution.** The sealed preparation has one reproducible provenance-preservation guard defect, `PPI-INTEGRATION-001`. Its accepted original bodies and native outputs currently verify. No scientific defect or current source corruption was found in this bounded integration audit.

## PPI-INTEGRATION-001 — old cache symlink destinations are not preserved

Severity: medium (blocking this preparation's stated preservation contract).

`common.py:inventory` records a path, byte size, body SHA-256 and `symlink` boolean, but no resolved destination or link text. `verify_cache_union` compares the inventory's keys and the old bodies; it does not compare old symlink identity. `prepare_inputs.py` likewise emits `expected-cache-baseline.json` without destination bindings. `adopt.py` compares entire cache inventories before adoption, but those inventories cannot distinguish two same-byte destinations. Preservation also compares old cache bodies and inventory keys only. Ninety of the 765 baseline cache entries are symlinks.

The isolated `cache-retarget-fixture` first binds `cache/old` to `first`, then repoints it to `second` with identical bytes. Both `verify_cache_union(cache, previous, {}, adopted=False)` and complete inventory equality still pass. `cache_retarget_probe.json` retains the exact result. No actual cache link was changed.

This contradicts the preparation's explicit claim that exact paths and link destinations are required. It can silently replace an established source location while preserving the body hash and can conceal loss of an established original's availability. The separate six-file recovery checks do correctly bind those six specific targets, but do not cover all old shared-cache links.

Prepare a successor packet that explicitly binds resolved destinations for all old cache paths and link type/text where exact link identity is required. Verify those bindings through initial merged-base binding, baseline capture, adoption and post-gate preservation. Keep new copies regular and retain the existing exact body/inventory checks. Add a same-byte different-destination negative control; also check regular-file-to-symlink and symlink-to-regular replacement as appropriate. Record current destinations as a fresh observation rather than retroactively claiming historical destination metadata was captured. Do not modify the original sealed packet or historical recovery/native receipts.

## Passed independent checks

- Rehashed the preparation's complete 199-artifact seal with hidden/ignored/followed inventory closure.
- Revalidated all 15 accepted packets, exact target `20541f…`, all actual canonical outputs, 780 selected original bodies and the complete 765-file pre-PPi cache union. Planned additions remain 24, with nine old cache files outside selected build paths protected by body/inventory checks.
- Verified the six recovered originals and symlinks against their recovery receipt. Current mtimes equal the receipt's new recovery mtimes; no old acquisition-time restoration is claimed.
- Verified 107 author and 101 original-science supplementary cache files as exact separate observations, without promoting them into scientific acceptance or introducing a generic ignored-cache exclusion.
- Checked all 385 dossier mappings: 346 exact mappings, 38 lossless UTF-8 wrappers and one prepared README. There are no executable archived `.py` destinations, duplicates or collisions with adoption/archive-map receipt names. No credential projection was needed in this actual mapping set.
- Revalidated the exact four-file Handle change: three replacements and one new test; exact before/after bytes match the accepted implementation and 223-file native runtime. No additional implementation owner is introduced by this integration plan.
- Read every current helper and all 42 bounded guard tests. Verified all ten recorded command receipts and streams, retaining four failed attempts. Final guard-tested helper code is unchanged except removal of two unused imports in the separate read-only preparation verifier; final verifier, lint and compilation receipts cover that version.
- Executed the real merged-binding CLI against EG-only `95ed7dee…`: it rejected the baseline with exit 1 before creating output. Reviewed the future guard's exact commit/tree/branch, local `origin/main` ancestry, clean maintained inventory, 231-record corrected-ATP bridge, four ATP authority files and pre-Handle runtime checks.
- Tested rejection of output paths inside the preparation, canonical build, shared cache, author successor and an existing output file.
- Reviewed history-before-render and immutable-history checks; the nine actual gate commands cover render, skills, full QC, full pytest, lint, KGX, vendored sync, whitespace and site-current. Final guard failures retain completed command receipts. Preservation protects old records/pages/reviews/history, authority objects/order, exact target-only inventories, old edge cells, target-only additions and source-context multiplicities, with separately bound display-cell approvals.

## Evidence and limits

`audit.py` completed successfully; its successful exit means the independent checks and defect reproduction completed, not that the preparation is approved. `checks.json`, per-check JSON, stdout/stderr, exact helper snapshots and the isolated retarget fixture retain the evidence. No full native builder, maintained gate suite, maintained adoption, history creation, Git or GitHub action was run. No maintained tree or shared cache was changed. The original package's 42 tests were inspected and receipt-verified rather than redundantly rerun. No actually merged ATP base, PPi integration or saved review is asserted here.
