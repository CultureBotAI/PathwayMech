# PPi maintained integration preparation

This external packet prepares adoption of `MetaCyc:PWY-8178`, pentose phosphate pathway (non-oxidative branch) II. It does not execute maintained adoption, append history, run maintained gates, save native review, or perform Git/GitHub operations. Root must independently inspect and accept these helpers before using them.

The exact accepted target is `20541f677f9228b670aac99a94e4d19ef89b5c20e0f6fdbb288d18ec7a9d98f5`: 6 core events, 20 chemical sides, 51 mechanistic edges, 14 endpoint qualifiers, 120 evidence uses and 53 references. Original full scientific review, bounded successor correction of issues 455–459, successor review/export probe and root acceptance remain separately attributed. This preparation adds no scientific acceptance claim and does not imply source exhaustion.

## Native outputs and implementation

Use the actual full native build's four original output files without reserialization or a proposal union. Source authority: 2,507 terms and 617 metadata entries; ontology: 1,969 terms and 5 metadata entries; manifest: 782 entries; Rhea selection: 24 IDs. Old authority objects and relative map order remain exact. The delta is 33 source terms, 22 source metadata entries, 6 ontology terms and 24 manifest entries; Rhea has no delta.

The accepted Handle overlay has exactly three replacements (`schema.py`, LinkML schema, `test_linkml_schema.py`) and one new test file (`test_handle_references.py`). Exact before/after hashes are required. Handles are permitted only as reference identifiers under the accepted grammar; the global biological identifier-prefix policy does not change. No CLI, rendering or source-builder code delta is introduced.

Native build selected 780 whole-original paths. The future ATP shared-cache baseline is 765 files; the plan adds exactly 24 new originals, producing 789 files. Nine existing shared-cache files are outside the selected native-build inputs and still must remain exact. Every old body and complete hidden/ignored inventory is checked, including symlink destinations. No shared-cache copy occurs during preparation.

Root recovered six missing originals at their established locations from exact retained copies. The pinned recovery receipt is bound in `accepted-inputs.json`; its new mtimes represent recovery, not acquisition. Historical native receipts are immutable. These helpers require exact paths, link destinations, sizes and body hashes, with no claim that old acquisition mtimes were restored.

## Actual merge is a separate prerequisite

The native build truthfully captured 230 actual EG-main records plus the prospective corrected ATP record (`6ed1607a4c17ffe56a6f5f8f123c44a0ff410c9a9965e11c3cde9ef23a4affe2`) and this PPi target. It did not build against an already merged ATP commit. Current EG-only commit `95ed7deec1ea749f3ebe60e170bb4463921b80dc` is explicitly rejected as the 231-record baseline.

Root must supply a future actually merged corrected ATP commit/tree and a clean worktree at `/private/tmp/pathwaymech-next-231-20261012`, branch `feat/pathway-next-231-20261012`. The merge-binding helper requires ancestry in observed local `origin/main`; all 231 record YAML files and `.gitkeep`, all four actual ATP authority files, and pre-Handle runtime bytes must match the accepted capture. New PPi target, dossier and Handle test must be absent. The separate baseline capture freezes every old maintained file, page, history, review, authority and cache original plus all old KGX edge cells and source-context multiplicities.

Root sequence, using the pinned interpreter, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `UV_NO_SYNC=1`, and new external output paths:

1. Run `bind_merged_base.py --root WORKTREE --base ACTUAL_MERGED_ATP --tree ACTUAL_TREE --branch feat/pathway-next-231-20261012 --output NEW_MERGED_BINDING.json` with `PATHWAYMECH_PPI_MERGED_BASE` unset.
2. Set `PATHWAYMECH_PPI_MERGED_BASE` to that exact external receipt. Run `capture-baseline.py --root WORKTREE --base ACTUAL_MERGED_ATP --output NEW_BASELINE_DIRECTORY`.
3. Run `adopt.py --root WORKTREE --base ACTUAL_MERGED_ATP --baseline-receipt NEW_BASELINE_DIRECTORY/receipt.json --receipt-output NEW_ADOPTION.json` for the inert dry plan. Add `--apply` only for the root-authorized actual adoption; no dry-run output file is created.
4. Root creates truthful native curation history for the record and implementation change **before render**. Capture exact bindings for all new history files in the root-approved extra-file list. Do not append history after rendering or native review save.
5. Run `run-gates.py --root WORKTREE --base ACTUAL_MERGED_ATP --adoption-receipt NEW_ADOPTION.json --output NEW_GATE_DIRECTORY`. This runs render, skill validation, full QC, full pytest, lint, KGX export, vendored sync, diff whitespace, and site-current checks. Full QC covers LinkML, strict record and identifier gates; full pytest includes the new Handle tests. Inherited focused Handle checks are provenance, not substitutes for these maintained gates.
6. Run `preserve-maintained.py --root WORKTREE --base ACTUAL_MERGED_ATP --adoption-receipt NEW_ADOPTION.json --baseline NEW_BASELINE_DIRECTORY/baseline.json --baseline-kgx NEW_BASELINE_DIRECTORY/baseline-kgx.json --gate-receipt NEW_GATE_DIRECTORY/execution.json --approved-extra-files ROOT_EXACT_NEW_FILE_BINDINGS.json --output NEW_PRESERVATION.json`. Supply `--approved-node-display-delta` only if root separately assesses the exact sorted shared-node cell differences.
7. Page/graph visual QA, reference-owner QA, native review save, final archive additions, PR/adversarial review, merge and cleanup remain root-owned subsequent work. After new review/archive files, rerun preservation against exact new-file bindings and the unchanged original gate inputs/history; check newly staged whitespace separately.

No old file, arbitrary `.pyc`, hidden file or altered gate input can be waived as an extra. Root approvals may bind exact new files only under the current dossier, history or structured reviews. Generated owners are the explicitly listed outputs. Late history fails even if listed as an approved extra. Any failed command/guard is retained; this helper does not silently retry or claim a command executed from an inherited receipt. A failure in final input/output guards produces a `failed_guard` execution receipt retaining the actual completed commands.

## Provenance and preparation checks

The dossier is selective: handoffs, complete manifests, reviews, root receipts, issue bodies/creation ledger and useful analysis/command receipts. It does not duplicate every source body or runtime/corpus file; omitted paths remain exactly bound in immutable manifests. Archived Python uses `.py.txt`; whitespace-bearing text uses lossless UTF-8 JSON wrappers. Explicit credential-header projections name omissions and retain original bindings.

A complete hidden/ignored sweep found 107 author packet build-cache files and 101 original science-review Swift cache files outside those original manifests. Their exact supplementary observations are bound separately; they are not newly accepted scientific artifacts. No generic cache-path exclusion is used. Further additions or byte changes fail. The original input guard failures, including the incorrect intermediate count of 106, are preserved with helper snapshots.

`validation/` retains actual preparation commands, stdout/stderr, exit codes and helper snapshots, including every failure. Fixture tests cover absence of a merged binding, exact Handle owners, source-cache union, old authority ordering, history timing, full gate-input closure and explicit new-file limitations. `preparation-checks.json` is a read-only prospective byte comparison and plan check. None of these receipts asserts that maintained integration or the future ATP merge has occurred.
