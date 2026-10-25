# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019` / Cycle 5 / Stage 6)

## 1. Frozen Snapshot & Ledger Validation

- **Frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`)**:
  - Path: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md`
  - Cutoff (`scope_frozen_at`): `2026-10-25T18:03:35Z`
  - SHA-256: `04495995fb7da54df85dd0a37170013f535407575f761d4bd776edcbde108570`
  - Size: `52769` bytes
  - Exact match with `status.json` `infra_scope`: verified (`True`).
  - Frozen non-resolved (`deferred`) task scope in `infra_snapshot.md`: `1` task (`pathwaymech-infra-0001`, [#673](https://github.com/CultureBotAI/PathwayMech/issues/673)); the other `4` tasks (`pathwaymech-infra-0002` through `pathwaymech-infra-0005`, [#674](https://github.com/CultureBotAI/PathwayMech/issues/674)–[#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) were already `resolved` in Cycle 1 Stage 6.
- **Updated `INFRA_TASKS.md` notebook validation**:
  - Validated with `kg_microbe_workflows`: `0` errors.
  - Task statuses:
    - `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)): `deferred` (`audit_pathbank_archive_member_authority` added alongside `inspect_pathbank_archive_member` and `build_pathbank_archive_manifest_entry` in `src/pathwaymech/pathbank_provenance.py` to deterministically audit any `PW[0-9]+.owl` member in `pathbank_primary_biopax.zip` against `data/identifier_authorities/sources.json` for `manifest_key_registered`, `indexed_native_term_ids`, `missing_native_term_ids`, `indexed_external_xrefs`, `missing_external_xrefs`, and `ready_for_check_identifiers`; remaining 36 non-duplicate *E. coli* `.owl` entries carried forward to Cycle 6 Stage 1 `add_records`)
    - `pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)): `resolved`
    - `pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)): `resolved`
    - `pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)): `resolved`
    - `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)): `resolved`

## 2. Per-Task Unit & Integration Test Verification

1. **`pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) — `src/pathwaymech/pathbank_provenance.py` & `tests/test_pathbank_identifier_authority.py`**:
  - Command: `.venv/bin/pytest tests/test_pathbank_identifier_authority.py`
  - Result: `214 passed` (including `test_build_pathbank_archive_manifest_entry_computes_exact_closed_provenance`, `test_build_pathbank_archive_manifest_entry_rejects_invalid_inputs`, `test_build_pathbank_archive_manifest_entry_rejects_duplicate_or_non_rdf_member`, `test_inspect_pathbank_archive_member_enumerates_native_terms_and_external_xrefs`, `test_audit_pathbank_archive_member_authority_partitions_indexed_and_missing_curies`, and `test_audit_pathbank_archive_member_authority_rejects_invalid_snapshot`).
2. **`pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)) — `src/pathwaymech/curation.py` & `tests/test_curation_publication.py`**:
  - Command: `.venv/bin/pytest tests/test_curation_publication.py`
  - Result: `16 passed` (including `test_publish_curation_preserves_existing_line_wrap_width` and `test_publish_curation_preserves_yaml_anchor_aliases_across_deep_copies`).
3. **`pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)) & `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) — `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`, `tests/test_linkml_schema.py` & `tests/test_kgx_export.py`**:
  - Command: `.venv/bin/pytest tests/test_linkml_schema.py tests/test_kgx_export.py`
  - Result: `223 passed` (`204 passed` in `tests/test_linkml_schema.py` including closed + open LinkML validation across all 274 pathway records, and `19 passed` in `tests/test_kgx_export.py`).
4. **`pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)) — `src/pathwaymech/sssom.py`, `output/sssom/source_mappings.sssom.tsv` & `tests/test_sssom_export.py`**:
  - Command: `.venv/bin/pytest tests/test_sssom_export.py`
  - Result: `20 passed`.
5. **Full Repository `pytest` and `ruff` Suite**:
  - Command: `.venv/bin/pytest -q && .venv/bin/ruff check --no-cache .`
  - Result: `8084 passed, 3 skipped` in `pytest`, `All checks passed!` in `ruff`.

## 3. Repository Quality Control Gates (`.venv/bin/pathwaymech-run-qc`)

- `pathwaymech-validate`: `validated 274 pathway records`
- `validate_strict.py`: `validated 274 records against the closed LinkML schema`
- `pathwaymech-check-identifiers`: `verified identifiers and label policies in 274 pathway records against authority snapshots`
- `history/`: `history links: 892 record(s), 0 invalid` (`892 history record(s) valid against src/pathwaymech/schema/history.yaml`)
- `pathwaymech-check-provenance`: `checked 22607 evidence blocks`
- `pathwaymech-validate-sources`: `validated 33 source records`
- `pathwaymech-check-docs`: `checked 6 documentation files`
- `pathwaymech-check-deep-research-contract`: `checked deep-research report contract`
- `pathwaymech-render-pages --check`: `pages/ is current with 274 pathway records`
- `record_review.py check --base main`: `valid_reviews: 207` (`coverage: declared_scopes_only`)
- `validate_claude_skills.py`: `validated 13 Claude skills`
- `check_vendored_sync.sh`: `OK: 22 governed artifacts match the pinned claw revision`
- `kg_microbe_workflows validate-evidence`: `validated reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/evidence.yaml`
