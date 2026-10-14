# KEGG complete-CDS adapter author handoff

Frozen 2026-10-14T20:15:49.102978+00:00 for independent review. Author: next258_preflight. This is an implementation and verification handoff, not an independent review.

Task worktree: `/private/tmp/pathwaymech-next-258-20261014`; branch `feat/pathway-next-258-20261014`; base `495de27ec09f99367d1cdd5c457a5e54a93c9a0b`.

## Stable author files

- `src/pathwaymech/kegg_gene.py` — SHA256 `cd55029144f0ed438ca026a607423956d21dae5ccc28b34b13523f68e6d1ec1d`, 9,360 bytes.
- `src/pathwaymech/identifiers.py` — SHA256 `d1a014fa77c4f1affd82ce999f98334493e0363dd250fd546f34e5fa26253165`, 33,808 bytes.
- `scripts/build_source_identifier_snapshot.py` — SHA256 `5b9d72448d9c6b798f4a054a5119c3cc8f000c693c4b26cf6d01e29100e959dd`, 103,780 bytes.
- `tests/test_kegg_gene_authority.py` — SHA256 `b9def406bb9b54215b0fcd8acce06907449e4e660450e76bd5c9cb3902025a04`, 19,569 bytes.
- `docs/IDENTIFIERS.md` — SHA256 `bef68ac2a8e6f5c08d563b6d969ff040e1099a170dd568c4e436a20c4034b25d`, 52,742 bytes.

## Behavior

The new `kegg-gene-flatfile` profile binds one exact official HTTPS REST request to a complete native CDS original. Canonical gene labels are ENTRY loci; NAME remains verbatim functional annotation. The whole original, ordered fields, organism/genome identities, position and AA/NT sequences are preserved. Consumer loading rehashes and reparses the original and compares the complete projection. Typed terms require participants/category gene and the existing canonical label policy. All supplied owners are checked before selection for incompatible same-gene originals or versions and source-kind laundering. The existing KEGG module/reaction/compound profiles are unchanged.

The profile deliberately does not validate translation or independently prove the genome-ID/organism-code crosswalk. Independent scientific proof remains external in the native acquisition bundle. Sequence alphabets, declared counts, simple inclusive genomic span, complete-CDS length relationship and terminal stop are checked. Joined/partial/ambiguous CDS representations are unsupported in this bounded profile.

## Verification

- Initial adapter plus legacy KEGG tests: **229 passed**, retained `targeted-initial.log`.
- Expanded relevant authority regressions: **432 passed in 16.26s**, retained `regression.log.txt` with command/timing/hash in `verification-receipts.json`.
- Ruff passed for all four touched Python files. `git diff --check` passed.
- `input-preservation.json` confirms all five tested files were unchanged across verification.
- Canonical builder and consumer replay accepted all four real native originals: cgR_0492, cgR_0495, cgR_2523, cgR_2524. `real-source-replay.json` binds exact original, implementation and output hashes. `replay/authority.json` is an external trial only; `replay/selectors/selector.yaml` is synthetic test selection and asserts no maintained pathway biology.
- Adversarial tests cover request-body swaps; organism/locus/CDS identity; duplicate/trailing objects; UTF-8/columns; sequence counts/alphabets/spans; whole-payload and projection tampering; all-owner selection-independent conflicts; term/source laundering; participant type/placement; canonical labels; and preservation of existing module behavior. A shape-valid translation mismatch is explicitly preserved for the separate scientific audit.

## Boundaries and reproduction

No record, maintained authority snapshot, policy, schema, governed file, source inventory, or gate was modified by this implementation. No commit was made. Parent owns promotion, independent review, PR lifecycle and full corpus checks.

Run the retained `run_verification.py` with `/usr/local/bin/python3.11 -B` to repeat the listed relevant tests, Ruff and diff check; it invokes the existing project interpreter at `/private/tmp/pathwaymech-next-195-20261011/.venv/bin/python` with task-worktree PYTHONPATH. Run `replay_real_sources.py` under that project interpreter with task-worktree `src` and root on PYTHONPATH to repeat the four-source builder/consumer trial. Scripts retain explicit absolute paths to the original acquisition and native independent reconciliation proof.

The completed candidate preflight is separately frozen at `/private/tmp/pathwaymech-next-258-preflight/fresh/HANDOFF.md`. This adapter does not expand that candidate-selection or source-exhaustion claim.
