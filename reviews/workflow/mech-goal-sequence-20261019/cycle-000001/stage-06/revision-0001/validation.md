# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019` / Cycle 1 / Stage 6)

## 1. Frozen Snapshot & Ledger Validation

- **Frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`)**:
  - Path: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`
  - Cutoff (`scope_frozen_at`): `2026-10-22T04:59:06Z`
  - SHA-256: `842d392d3e6a1dcec5507c958d4add01b8a1f270943c5d0788f88d151dd08c94`
  - Size: `14811` bytes
  - Exact match with `status.json` `infra_scope`: verified (`True`).
- **Updated `INFRA_TASKS.md` notebook validation**:
  - Validated with `kg_microbe_workflows.validate_infra_notebook`: `0` errors.
  - Task statuses:
    - `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)): `deferred` (carried forward to Cycle 2 Stage 1 `add_records`)
    - `pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)): `resolved`
    - `pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)): `resolved`
    - `pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)): `resolved`
    - `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)): `resolved`

## 2. Per-Task Unit & Integration Test Verification

1. **`pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)) — `src/pathwaymech/curation.py` & `tests/test_curation_publication.py`**:
   - Command: `.venv/bin/pytest tests/test_curation_publication.py`
   - Result: `16 passed` (including `test_publish_curation_preserves_existing_line_wrap_width` and `test_publish_curation_preserves_yaml_anchor_aliases_across_deep_copies`).
2. **`pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)) — `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py` & `tests/test_linkml_schema.py`**:
   - Command: `.venv/bin/pytest tests/test_linkml_schema.py`
   - Result: `204 passed` (including `test_mechanistic_edge_coefficient_and_evidence_annotations_validate_in_both`, `test_mechanistic_edge_coefficient_must_be_a_positive_int_in_both`, `test_evidence_assay_taxon_must_be_an_ncbitaxon_curie_in_both`, `test_evidence_eco_code_must_be_a_7_digit_eco_curie_in_both`, and `test_encodes_predicate_accepts_gene_to_protein_in_both_and_rejects_bad_endpoints`).
3. **`pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)) — `src/pathwaymech/sssom.py`, `output/sssom/source_mappings.sssom.tsv` & `tests/test_sssom_export.py`**:
   - Command: `.venv/bin/pytest tests/test_sssom_export.py`
   - Result: `20 passed` (including `test_write_sssom_uses_yaml_safe_curie_map_for_all_source_prefixes` and `test_sssom_expands_native_frame_and_scoped_instance_ids` covering `Entrez`, `gomodel`, `NCBIProtein`, `Reactome`, and `SGD`).
4. **`pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) — `src/pathwaymech/kgx.py`, `src/pathwaymech/schema.py`, `tests/test_kgx_export.py` & `tests/test_linkml_schema.py`**:
   - Command: `.venv/bin/pytest tests/test_kgx_export.py tests/test_linkml_schema.py`
   - Result: `223 passed` (`19 passed` in `tests/test_kgx_export.py` including `test_native_participant_fallback_retains_reaction_defaults[BiGG]`, and `204 passed` in `tests/test_linkml_schema.py` including `test_reactions_mixing_explicit_and_omitted_categories_are_rejected`).

## 3. Repository Quality Control Gates (`.venv/bin/pathwaymech-run-qc`)

- `pathwaymech-validate`: `validated 270 pathway records`
- `validate_strict.py`: `validated 270 records against the closed LinkML schema`
- `pathwaymech-check-identifiers`: `verified identifiers and label policies in 270 pathway records against authority snapshots`
- `history/`: `history links: 550 record(s), 0 invalid` (`550 history record(s) valid against src/pathwaymech/schema/history.yaml`)
- `pathwaymech-check-provenance`: `checked 22085 evidence blocks`
- `pathwaymech-validate-sources`: `validated 33 source records`
- `pathwaymech-check-docs`: `checked 6 documentation files`
- `pathwaymech-check-deep-research-contract`: `checked deep-research report contract`
- `pathwaymech-render-pages --check`: `pages/ is current with 270 pathway records`
- `record_review.py validate`: `validated 2 review bundles`
- `kg_microbe_workflows validate-evidence`: `validated reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/evidence.yaml`
