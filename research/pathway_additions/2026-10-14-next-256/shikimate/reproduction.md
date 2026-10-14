# Reproducing the next256 author evidence

The dossier retains byte-exact compact projections, decisions, source bindings,
command receipts and helper programs. Each subdirectory has a `retention.json`
that names the external original, repository destination, byte length and SHA256.
Python helpers have a `.py.txt` suffix so they are reviewable evidence rather than
production modules. Original XML, HTML, API JSON, PDF/page images, full text,
SQLite databases and RDF stay outside the repository at their hash-bound paths.
Reproduction requires those exact originals; later downloads may differ.

## Source and scientific checks

1. Verify the retained native `artifact-manifest.json` and primary
   `package-index.json` against their sealed hashes in the respective retention
   files. Rehash every listed artifact and original before reuse. Native and
   primary original-binding structures distinguish issuing payloads, derived text,
   reused bytes and renderings.
2. Restore helpers to external scratch paths without changing their bytes. Read
   their path constants before execution. Native `project.py`, `build_handoff.py`,
   `replay_coverage.py`, `verify_identity.py`, `write_identities.py` and
   `verify_pathway_html.py` document the parsed source joins and bounded coverage.
   Do not rerun acquisition helpers over preserved originals or interpret a later
   response as the original observation.
3. The primary reading ledger identifies inspected full bodies, tables, figures,
   abstract-only sources and unavailable material. The 1988 dissertation reprint
   and 2005 PMC article are separate from the older reused article originals.
   `build_package.py` documents the compact proposal and quote checks. Its earlier
   proposal is external and explicitly superseded in `package-index.json`; the
   final retained proposal uses quotations for article prose.
4. In chemistry, `extract_rhea.py` parses the original Rhea RDF using
   coefficient-specific `containsN` relations. `compare_chemistry.py` checks
   pinned ChEBI structures and reaction balance with RDKit 2024.03.5.
   `assemble_core.py` and `assemble_record.py` document the chemical core and final
   source integration. `core-record.json` is an assembly input, not the complete
   maintained graph. Read the current record hash in `assembly-ledger.json` before
   replaying assembly. These helpers target the recorded external scratch paths
   and the active worktree; adapt destinations in a fresh staging copy before
   any replay that would write files.

## Authority replay

Baseline commit: `b645cc4c0afd75f3eff521376b75602a3c2ad679`.
The exact working directory, argument arrays, environment, builder hashes,
manifest hash and selector hash are in
`authorities/canonical-build-commands.json`. All 252 baseline records came from
exact Git blobs. An ID-only selector preserves all 4,907 baseline terms and the
22 planned named identifiers; it supplies no names or scientific claims.

To reproduce the successful union in the original evidence environment, read
those command arrays and change only the two `--output` destinations to fresh
external paths. Run the unchanged builders with their recorded working directory
and environment. Verify whole-file hashes against:

| Maintained output | SHA256 |
| --- | --- |
| `data/identifier_authorities/sources.json` | `4a1963c5b61ea7906ce5e5ad09f8f6865fc7e18a86e9f5a5a0f2c85bde62cc45` |
| `data/identifier_authorities/ontology.json` | `cc16a3703d5ee7d07b141d33b0f5ed9943caf885ecd791e9565800bbfad5df64` |
| `conf/identifier_sources.json` | `3ce7f3ed376451d625be862b8f56f45771f57dbaf0ffd7203ac011ebdc189e59` |

For new staging, `prepare_baseline.py` recovers the exact baseline and verifies
its external cache. `prepare_union.py` describes the final five manifest
additions and selector. Both assume a fresh stage and enforce guards; do not rerun
them over the promoted worktree. `run_builds.py` preserves existing receipts, and
`promote.py` verifies baseline objects and all original hashes before promotion.
The source snapshot contains 2,829 terms from 832 owners; the ontology snapshot
contains 2,084 terms from the unchanged five owners. All prior objects remain
unchanged and the final union contains 4,913 terms.

The failed `metacyc-pathway-xml` attempt is preserved separately under
`authorities/attempt-pathway-xml/`. It rejected `evidence`, `in-pathway`,
`pathway-link` and `super-pathways`. Reconstruct its external full manifest from
the baseline manifest plus the retained failed-attempt additions, then compare
with the hash in `pathway-authority-profile-assessment.json`. The final source
build uses `metacyc-html` only for canonical pathway identity. The ontology build
already passed on the unchanged selection and was not rerun needlessly.

Builder `.log.json` files are lossless UTF-8 wrappers. Their retention hash is the
wrapper hash, while the embedded SHA256 identifies the original raw log. The
failed attempt's embedded historical log path was reused by the successful retry;
`authorities/failed-attempt-log-relocation.json` explicitly binds the unchanged
wrapper to the archived raw log and explains that relocation. Validate its payload
against the archived original, not against the later log now at the old path.

## Acceptance boundary

Authority builder success and author helper checks are necessary evidence, not
final pathway validation or scientific approval. The integration workflow owns
rendering, validation/tests/lint, governed-file checks, immutable independent
reviews, committed-blob checks and PR/merge receipts. Those final results must be
read separately. The dossier does not assert that source discovery is exhausted.
