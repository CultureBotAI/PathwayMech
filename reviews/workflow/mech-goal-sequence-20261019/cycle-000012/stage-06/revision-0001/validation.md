# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019` / Cycle 12 / Stage 6)

## 1. Frozen Snapshot & Ledger Validation

- **Frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`)**:
  - Path: `reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-06/revision-0001/infra_snapshot.md`
  - Cutoff (`scope_frozen_at`): `2026-11-05T17:31:58Z`
  - SHA-256: `1759bb8ed4ca9dce101cb42c4f77116088a61167c5305e11c03099757c528aaf`
  - Size: `138791` bytes
  - Exact match with `status.json` `infra_scope`: verified (`True`).
  - Frozen non-resolved (`deferred`) task scope in `infra_snapshot.md`: `1` task (`pathwaymech-infra-0001`, [#673](https://github.com/CultureBotAI/PathwayMech/issues/673)); the other `4` tasks (`pathwaymech-infra-0002` through `pathwaymech-infra-0005`, [#674](https://github.com/CultureBotAI/PathwayMech/issues/674)–[#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) were already `resolved` in Cycle 1 Stage 6.
- **Updated `INFRA_TASKS.md` notebook validation**:
  - Validated with `kg_microbe_workflows`: `0` errors.
  - Task statuses:
    - `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)): `deferred` (`summarize_registered_pathbank_archive_slices` added alongside `verify_pathbank_archive_candidate_post_registration`, `audit_pathbank_manifest_snapshot_sync`, `plan_next_pathbank_archive_candidate_registration`, `summarize_pathbank_archive_candidate_frontier`, `select_next_pathbank_archive_candidate`, `rank_pathbank_archive_member_candidates`, `audit_pathbank_archive_member_authority`, `inspect_pathbank_archive_member`, and `build_pathbank_archive_manifest_entry` in `src/pathwaymech/pathbank_provenance.py` to deterministically audit and partition all registered `pathbank-biopax-zip` entries across `conf/identifier_sources.json` and `data/identifier_authorities/sources.json`; remaining 29 non-duplicate *E. coli* `.owl` entries carried forward to Cycle 13 Stage 1 `add_records`)
    - `pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)): `resolved`
    - `pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)): `resolved`
    - `pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)): `resolved`
    - `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)): `resolved`

## 2. Per-Task Unit & Integration Test Verification

1. **`pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) — `src/pathwaymech/pathbank_provenance.py` & `tests/test_pathbank_identifier_authority.py`**:
  - Command: `.venv/bin/pytest tests/test_pathbank_identifier_authority.py`
  - Result: `264 passed` (including `test_build_pathbank_archive_manifest_entry_computes_exact_closed_provenance`, `test_build_pathbank_archive_manifest_entry_rejects_invalid_inputs`, `test_build_pathbank_archive_manifest_entry_rejects_duplicate_or_non_rdf_member`, `test_inspect_pathbank_archive_member_enumerates_native_terms_and_external_xrefs`, `test_audit_pathbank_archive_member_authority_partitions_indexed_and_missing_curies`, `test_audit_pathbank_archive_member_authority_rejects_invalid_snapshot`, `test_rank_pathbank_archive_member_candidates_orders_by_readiness_and_missing_counts`, `test_rank_pathbank_archive_member_candidates_rejects_invalid_candidates`, `test_select_next_pathbank_archive_candidate_skips_registered_and_excluded_pathways`, `test_select_next_pathbank_archive_candidate_rejects_invalid_filters`, `test_summarize_pathbank_archive_candidate_frontier_aggregates_remaining_and_missing_xrefs`, `test_summarize_pathbank_archive_candidate_frontier_rejects_invalid_filters`, `test_plan_next_pathbank_archive_candidate_registration_builds_updated_manifest`, `test_plan_next_pathbank_archive_candidate_registration_rejects_invalid_or_conflicting_manifests`, `test_audit_pathbank_manifest_snapshot_sync_partitions_synchronized_pending_and_orphan_keys`, `test_audit_pathbank_manifest_snapshot_sync_rejects_invalid_or_drifted_provenance`, `test_verify_pathbank_archive_candidate_post_registration_tracks_pending_and_verified_states`, `test_verify_pathbank_archive_candidate_post_registration_rejects_invalid_or_conflicting_states`, `test_summarize_registered_pathbank_archive_slices_partitions_corpus_and_auxiliary_slices`, and `test_summarize_registered_pathbank_archive_slices_rejects_invalid_inputs`).
2. **`pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)) — `src/pathwaymech/curation.py` & `tests/test_curation_publication.py`**:
  - Command: `.venv/bin/pytest tests/test_curation_publication.py`
  - Result: `16 passed` (including `test_publish_curation_preserves_existing_line_wrap_width` and `test_publish_curation_preserves_yaml_anchor_aliases_across_deep_copies`).
3. **`pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)) & `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) — `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`, `tests/test_linkml_schema.py` & `tests/test_kgx_export.py`**:
  - Command: `.venv/bin/pytest tests/test_linkml_schema.py tests/test_kgx_export.py`
  - Result: `223 passed` (`204 passed` in `tests/test_linkml_schema.py` and `19 passed` in `tests/test_kgx_export.py`).
4. **`pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)) — `src/pathwaymech/sssom.py`, `output/sssom/source_mappings.sssom.tsv` & `tests/test_sssom_export.py`**:
  - Command: `.venv/bin/pytest tests/test_sssom_export.py`
  - Result: `20 passed`.
5. **Full Repository `pytest` and `ruff` Suite**:
  - Command: `.venv/bin/pytest -q && .venv/bin/ruff check --no-cache .`
  - Result: `8134 passed, 3 skipped` in `pytest`, `All checks passed!` in `ruff`.

## 3. Repository Quality Control Gates (`.venv/bin/pathwaymech-run-qc`)

- `pathwaymech-validate`: `validated 281 pathway records`
- `validate_strict.py`: `validated 281 records against the closed LinkML schema`
- `pathwaymech-check-identifiers`: `verified identifiers and label policies in 281 pathway records against authority snapshots`
- `history/`: `history links: 1063 record(s), 0 invalid` (`1063 history record(s) valid against src/pathwaymech/schema/history.yaml`)
- `pathwaymech-check-provenance`: `checked 23009 evidence blocks`
- `pathwaymech-validate-sources`: `validated 33 source records`
- `pathwaymech-check-docs`: `checked 6 documentation files`
- `pathwaymech-check-deep-research-contract`: `checked deep-research report contract`
- `pathwaymech-render-pages --check`: `pages/ is current with 281 pathway records`
- `record_review.py check --base main`: `valid_reviews: 223` (`coverage: declared_scopes_only`)
- `validate_claude_skills.py`: `validated 13 Claude skills`
- `check_vendored_sync.sh`: `OK: 22 governed artifacts match the pinned claw revision`
- `kg_microbe_workflows validate-evidence`: `validated reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-06/revision-0001/evidence.yaml`
