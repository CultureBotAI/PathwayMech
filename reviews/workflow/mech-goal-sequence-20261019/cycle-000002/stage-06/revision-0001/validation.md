# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019` / Cycle 2 / Stage 6)

## 1. Frozen Snapshot & Ledger Validation

- **Frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`)**:
  - Path: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md`
  - Cutoff (`scope_frozen_at`): `2026-10-23T07:14:09Z`
  - SHA-256: `0aac2ad0f049d63088e2dd3f9624b6f3feb58fc692104e5c78136bb4d9ea6904`
  - Size: `28320` bytes
  - Exact match with `status.json` `infra_scope`: verified (`True`).
  - Frozen non-resolved (`pending`) task scope in `infra_snapshot.md`: `1` task (`pathwaymech-infra-0001`, [#673](https://github.com/CultureBotAI/PathwayMech/issues/673)); the other `4` tasks (`pathwaymech-infra-0002` through `pathwaymech-infra-0005`, [#674](https://github.com/CultureBotAI/PathwayMech/issues/674)–[#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) were already `resolved` in Cycle 1 Stage 6.
- **Updated `INFRA_TASKS.md` notebook validation**:
  - Validated with `kg_microbe_workflows`: `0` errors.
  - Task statuses:
    - `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)): `deferred` (`build_pathbank_archive_manifest_entry` delivered in `src/pathwaymech/pathbank_provenance.py`; remaining 39 non-duplicate *E. coli* `.owl` entries carried forward to Cycle 3 Stage 1 `add_records`)
    - `pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)): `resolved`
    - `pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)): `resolved`
    - `pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)): `resolved`
    - `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)): `resolved`

## 2. Per-Task Unit & Integration Test Verification

1. **`pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) — `src/pathwaymech/pathbank_provenance.py` & `tests/test_pathbank_identifier_authority.py`**:
   - Command: `.venv/bin/pytest tests/test_pathbank_identifier_authority.py`
   - Result: `8 passed` (including `test_build_pathbank_archive_manifest_entry_computes_exact_closed_provenance` and `test_build_pathbank_archive_manifest_entry_rejects_invalid_inputs`).
2. **`pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)) — `src/pathwaymech/curation.py` & `tests/test_curation_publication.py`**:
   - Command: `.venv/bin/pytest tests/test_curation_publication.py`
   - Result: `16 passed` (including `test_publish_curation_preserves_existing_line_wrap_width` and `test_publish_curation_preserves_yaml_anchor_aliases_across_deep_copies`).
3. **`pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)) & `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) — `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`, `tests/test_linkml_schema.py` & `tests/test_kgx_export.py`**:
   - Command: `.venv/bin/pytest tests/test_linkml_schema.py tests/test_kgx_export.py`
   - Result: `417 passed` (`398 passed` in `tests/test_linkml_schema.py` including closed + open LinkML validation across all 271 pathway records, and `19 passed` in `tests/test_kgx_export.py`).
4. **`pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)) — `src/pathwaymech/sssom.py`, `output/sssom/source_mappings.sssom.tsv` & `tests/test_sssom_export.py`**:
   - Command: `.venv/bin/pytest tests/test_sssom_export.py`
   - Result: `20 passed`.
5. **Combined Stage 6 `pytest` and `ruff` suite**:
   - Command: `TMPDIR=/tmp .venv/bin/pytest --basetemp=/tmp/pytest-pathwaymech -o cache_dir=/tmp/pytest-cache -q tests/test_pathbank_identifier_authority.py tests/test_curation_publication.py tests/test_linkml_schema.py tests/test_kgx_export.py tests/test_sssom_export.py && .venv/bin/ruff check --no-cache src/ tests/ scripts/`
   - Result: `461 passed` in `pytest` (plus `202 passed` across the remaining non-parametrized test modules), `All checks passed!` in `ruff`.

## 3. Repository Quality Control Gates (`.venv/bin/pathwaymech-run-qc`)

- `pathwaymech-validate`: `validated 271 pathway records`
- `validate_strict.py`: `validated 271 records against the closed LinkML schema`
- `pathwaymech-check-identifiers`: `verified identifiers and label policies in 271 pathway records against authority snapshots`
- `history/`: `history links: 711 record(s), 0 invalid` (`711 history record(s) valid against src/pathwaymech/schema/history.yaml`)
- `pathwaymech-check-provenance`: `checked 22211 evidence blocks`
- `pathwaymech-validate-sources`: `validated 33 source records`
- `pathwaymech-check-docs`: `checked 6 documentation files`
- `pathwaymech-check-deep-research-contract`: `checked deep-research report contract`
- `pathwaymech-render-pages --check`: `pages/ is current with 271 pathway records`
- `record_review.py check --base main`: `valid_reviews: 201`
- `validate_claude_skills.py`: `validated 13 Claude skills`
- `check_vendored_sync.sh`: `OK: 22 governed artifacts match the pinned claw revision`
- `kg_microbe_workflows validate-evidence`: `validated reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml`
