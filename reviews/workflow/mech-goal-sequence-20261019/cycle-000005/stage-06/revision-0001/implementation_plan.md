# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019` / Cycle 5 / Stage 6)

## 1. Frozen Task Intake & Cutoff

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `5`, Stage `6` (`infrastructure`)
- **Base commit (`main`)**: `218d964fa5083fd0d0eeccbdc2b326e183153db9`
- **Previous stage evidence (`stage-05`)**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml` (`sha256: a5ad35ab3e54ad3f562ba0612165b39204b6493518ec41ba28d001380f51630c`)
- **Frozen `INFRA_TASKS.md` cutoff (`scope_frozen_at`)**: `2026-10-25T18:03:35Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `04495995fb7da54df85dd0a37170013f535407575f761d4bd776edcbde108570` (`52,769` bytes)
- **Frozen snapshot artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md`

### Frozen Inventory Summary (5 Total Tasks; 1 Pending/Deferred Task in Scope)

| Task ID | Pre-Stage-6 Status | Post-Stage-6 Status | GitHub Issue | Scope & Action in Cycle 5 Stage 6 |
| --- | --- | --- | --- | --- |
| `pathwaymech-infra-0001` | `deferred` | `deferred` (carried forward to Cycle 6 Stage 1) | [#673](https://github.com/CultureBotAI/PathwayMech/issues/673) | Added `audit_pathbank_archive_member_authority` in `src/pathwaymech/pathbank_provenance.py` (with unit tests in `tests/test_pathbank_identifier_authority.py`) to deterministically audit any `PW[0-9]+.owl` member in `pathbank_primary_biopax.zip` against `data/identifier_authorities/sources.json` (`manifest_key_registered`, `indexed_native_term_ids`, `missing_native_term_ids`, `indexed_external_xrefs`, `missing_external_xrefs`, and `ready_for_check_identifiers`); deferred the remaining 36 non-duplicate *E. coli* `.owl` entries to Cycle 6 Stage 1 (`add_records`) because `scripts/build_source_identifier_snapshot.py` strictly filters `data/identifier_authorities/sources.json` to `wanted = corpus_ids(records)` |
| `pathwaymech-infra-0002` | `resolved` (Cycle 1 Stage 6) | `resolved` | [#674](https://github.com/CultureBotAI/PathwayMech/issues/674) | Already resolved in Cycle 1 Stage 6 (`src/pathwaymech/curation.py`); verified intact |
| `pathwaymech-infra-0003` | `resolved` (Cycle 1 Stage 6) | `resolved` | [#675](https://github.com/CultureBotAI/PathwayMech/issues/675) | Already resolved in Cycle 1 Stage 6 (`src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`) and adopted across 33 records in Cycles 2–5 Stage 2 (`747` `MechanisticEdge.coefficient` edges, `197` `EvidenceItem.eco_code` qualifiers, and `396` `EvidenceItem.assay_taxon` qualifiers across the 274-record corpus); verified intact |
| `pathwaymech-infra-0004` | `resolved` (Cycle 1 Stage 6) | `resolved` | [#676](https://github.com/CultureBotAI/PathwayMech/issues/676) | Already resolved in Cycle 1 Stage 6 (`src/pathwaymech/sssom.py`) and adopted across 95 SGD records in Cycle 2 Stage 3 (`477` mappings), 53 records in Cycle 3 Stage 3 (`174` mappings), 50 records in Cycle 4 Stage 3 (`209` mappings), and 10 records in Cycle 5 Stage 3 (`31` mappings); verified intact |
| `pathwaymech-infra-0005` | `resolved` (Cycle 1 Stage 6) | `resolved` | [#677](https://github.com/CultureBotAI/PathwayMech/issues/677) | Already resolved in Cycle 1 Stage 6 (`src/pathwaymech/kgx.py`, `src/pathwaymech/schema.py`), adopted across all 56 untyped MetaCyc records in Cycle 2 Stage 5 ([#692](https://github.com/CultureBotAI/PathwayMech/issues/692)), and confirmed across all 274 records / 1,616 reactions in Cycle 5 Stage 4/5 ([#723](https://github.com/CultureBotAI/PathwayMech/issues/723), [#724](https://github.com/CultureBotAI/PathwayMech/issues/724)); verified intact |

## 2. Dependency-Aware Implementation Plan for `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673))

### 2.1 Root Cause & Architectural Constraint

1. **Snapshot Selection Rule (`scripts/build_source_identifier_snapshot.py:2366–2440`)**:
   - `build_snapshot` computes `wanted = corpus_ids(records)` from `data/pathways/*.yaml` and retains only those terms referenced by a curated pathway record in `data/pathways/`.
   - Consequently, bulk-populating `data/identifier_authorities/sources.json` for the 36 uncurated *E. coli* PathBank `.owl` files without simultaneously curating those 36 records in `data/pathways/` is impossible under the builder's design contract (`"The corpus only selects which identifiers to retain, keeping the checked-in authority small and provenance auditable"`).
2. **Actionable Infrastructure Upgrade in `src/pathwaymech/pathbank_provenance.py`**:
   - In Cycles 2–4 Stage 6, we added and hardened `build_pathbank_archive_manifest_entry` and `inspect_pathbank_archive_member` in `src/pathwaymech/pathbank_provenance.py` to enforce relative manifest paths, valid ZIP archives, unique ZIP member entries, native RDF/BioPAX XML object types, primary `SMP[0-9]+` root pathway membership via `pathbank_terms`, and pre-ingestion external `CHEBI`/`NCBITaxon`/`UniProtKB` `UnificationXref` enumeration.
   - In Cycle 5 Stage 1 (`add_records`), `inspect_pathbank_archive_member` was used directly to register `pathbank-primary-2019-PW002041-SMP0002055` and curate `PathBank:SMP0002055` (*Thiazole Biosynthesis I*) in `data/pathways/thiazole-biosynthesis-i-escherichia-coli.yaml` (reducing the remaining non-duplicate *E. coli* `.owl` entries from 37 to 36).
   - In Cycle 5 Stage 6, we further advance `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) by adding `audit_pathbank_archive_member_authority(archive_path, member, root, authority_snapshot_path, ...)` in `src/pathwaymech/pathbank_provenance.py`, which validates both the PathBank ZIP member and the checked-in authority snapshot (`data/identifier_authorities/sources.json`) and deterministically partitions the member's `native_term_ids` and `external_xrefs` (`CHEBI`, `NCBITaxon`, `UniProtKB`) into indexed vs. missing CURIEs (`manifest_key_registered`, `indexed_native_term_ids`, `missing_native_term_ids`, `indexed_external_xrefs`, `missing_external_xrefs`, and `ready_for_check_identifiers`).

### 2.2 Acceptance Criteria

1. `audit_pathbank_archive_member_authority` in `src/pathwaymech/pathbank_provenance.py`:
   - Calls `inspect_pathbank_archive_member` to enforce all ZIP/XML/BioPAX provenance checks and extract `manifest_entry`, `pathway_id`, `pathway_label`, `native_term_ids`, and `external_xrefs`.
   - Validates that `authority_snapshot_path` is a valid UTF-8 JSON object containing mapping keys `'sources'` and `'terms'`.
   - Reports `manifest_key_registered`, `indexed_native_term_ids`, `missing_native_term_ids`, `indexed_external_xrefs`, `missing_external_xrefs`, and `ready_for_check_identifiers`.
2. `tests/test_pathbank_identifier_authority.py` includes unit tests verifying `audit_pathbank_archive_member_authority` across partial authority snapshots, complete authority snapshots, and invalid authority snapshot inputs.
3. `INFRA_TASKS.md` records the Cycle 5 Stage 6 disposition for `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) and explicitly carries forward the remaining 36 non-duplicate *E. coli* PathBank `.owl` entries to Cycle 6 Stage 1 (`add_records`).
4. All repository quality control gates (`.venv/bin/pathwaymech-run-qc`, `.venv/bin/pytest -q`, `.venv/bin/ruff check --no-cache .`, `scripts/check_vendored_sync.sh`, and `kg_microbe_workflows validate-evidence`) pass with 0 errors.
