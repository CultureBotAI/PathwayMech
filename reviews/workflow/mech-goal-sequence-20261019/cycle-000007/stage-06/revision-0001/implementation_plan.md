# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019` / Cycle 7 / Stage 6)

## 1. Frozen Scope & Cutoff

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage**: `7` / `6` (`infrastructure`)
- **Frozen `INFRA_TASKS.md` snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/infra_snapshot.md`
- **Frozen `INFRA_TASKS.md` SHA-256**: `e074a99f0f2421381d0b8f64c23ff535d44d34391abba1088c65a7ca4190c57a` (`75756` bytes)
- **Supervisor freeze timestamp (`scope_frozen_at`)**: `2026-10-30T23:56:48Z`
- **Base commit on `main`**: `a2dc85419c61943c2603b2e7059b3a7032292a58` (PR `#755`)

## 2. Frozen Task Inventory & Dependency Graph

| Task ID | Issue | Pre-Stage 6 Status | Priority | Dependencies | Stage 6 Action | Post-Stage 6 Status |
|---|---|---|---|---|---|---|
| `pathwaymech-infra-0001` | [#673](https://github.com/CultureBotAI/PathwayMech/issues/673) | `deferred` | medium | Per-slice upstream `UniProtKB`, `Rhea` (releases 139/142), and `PubMed` authority verification alongside curated `data/pathways/*.yaml` records during Stage 1 (`add_records`) because `scripts/build_source_identifier_snapshot.py` strictly filters `data/identifier_authorities/sources.json` by `wanted = corpus_ids(records)` | Deliver `select_next_pathbank_archive_candidate` in `src/pathwaymech/pathbank_provenance.py` + unit tests in `tests/test_pathbank_identifier_authority.py` to deterministically filter out already-registered manifest keys and excluded `PathBank:SMP[0-9]+` CURIEs while selecting the highest-readiness remaining `(member, root)` candidate slice from `pathbank_primary_biopax.zip` against `data/identifier_authorities/sources.json`; explicitly carry forward remaining 34 non-duplicate *E. coli* `.owl` slices to Cycle 8 Stage 1 (`add_records`) | `deferred` |
| `pathwaymech-infra-0002` | [#674](https://github.com/CultureBotAI/PathwayMech/issues/674) | `resolved` | medium | None | Preserve resolved implementation in `src/pathwaymech/curation.py` and re-verify unit tests in `tests/test_curation_publication.py` | `resolved` |
| `pathwaymech-infra-0003` | [#675](https://github.com/CultureBotAI/PathwayMech/issues/675) | `resolved` | low | None | Preserve resolved schema & exporter implementation in `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, and `src/pathwaymech/kgx.py` (now adopted across 63 pathway records after Cycle 7 Stage 1, Stage 2, and Stage 3: `1,347` `MechanisticEdge.coefficient` edges, `21` `EdgePredicateEnum.encodes` edges, `368` `EvidenceItem.eco_code` qualifiers, and `629` `EvidenceItem.assay_taxon` qualifiers) and re-verify unit tests | `resolved` |
| `pathwaymech-infra-0004` | [#676](https://github.com/CultureBotAI/PathwayMech/issues/676) | `resolved` | medium | None | Preserve resolved `CURIE_MAP` implementation in `src/pathwaymech/sssom.py` and `output/sssom/source_mappings.sssom.tsv` (now `1,060` total mappings across `217` records after Cycle 7 Stage 1 and Stage 3) and re-verify unit tests in `tests/test_sssom_export.py` | `resolved` |
| `pathwaymech-infra-0005` | [#677](https://github.com/CultureBotAI/PathwayMech/issues/677) | `resolved` | medium | None | Preserve resolved `BiGG` reaction prefix mapping in `src/pathwaymech/kgx.py` and within-record reaction category consistency validation in `src/pathwaymech/schema.py` (confirmed across all 276 records / 1,628 reactions in Cycle 7 Stage 4/5) and re-verify unit tests | `resolved` |

### Dependency Analysis

- `pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)), `pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)), `pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)), and `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) were resolved in Cycle 1 Stage 6 and adopted across the corpus in Cycles 2–7.
- `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) is the sole non-resolved (`deferred`) task in the frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`). In Cycle 2 Stage 6 we added `build_pathbank_archive_manifest_entry` in `src/pathwaymech/pathbank_provenance.py`; in Cycle 3 Stage 6 we hardened `build_pathbank_archive_manifest_entry` to verify unique ZIP member entries, native RDF/BioPAX XML object types, and primary `SMP[0-9]+` root pathway membership via `pathbank_terms`; in Cycle 4 Stage 6 we added `inspect_pathbank_archive_member`; in Cycle 5 Stage 6 we added `audit_pathbank_archive_member_authority`; in Cycle 6 Stage 6 we added `rank_pathbank_archive_member_candidates`; and in Cycle 7 Stage 1 (`add_records`) we used `rank_pathbank_archive_member_candidates`, `audit_pathbank_archive_member_authority`, and `build_pathbank_archive_manifest_entry` to register `pathbank-primary-2019-PW002058-SMP0002070` (`PW002058.owl`, 33,359 bytes, SHA-256 `a01b8e8f275be2d6f655d65a308ca88ffb92b4c757320db579ddba7235292f74`) and curate `PathBank:SMP0002070` (*Conversion of Succinate to Propanoate*) in `data/pathways/conversion-of-succinate-to-propanoate-escherichia-coli.yaml`, reducing the uningested non-duplicate *E. coli* PathBank `.owl` backlog from 35 to 34 files (`14` ingested *E. coli* `PathBank:*` records + `265` duplicates of existing `MetaCyc:*`/`KEGG:*`/`BioCyc:*` records + `34` remaining non-duplicate *E. coli* `.owl` files = `313` total *E. coli* `.owl` files in `pathbank_primary_biopax.zip`).
- Because `scripts/build_source_identifier_snapshot.py` (`lines 2366–2440`) strictly filters `data/identifier_authorities/sources.json` by `wanted = corpus_ids(records)` (*"The corpus only selects which identifiers to retain, keeping the checked-in authority small and provenance auditable"*), unreferenced authority identifiers for uningested `.owl` pathways cannot be bulk-populated into `data/identifier_authorities/sources.json` ahead of curating the corresponding `data/pathways/*.yaml` records.
- However, Stage 6 can further advance `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) in `src/pathwaymech/pathbank_provenance.py` by adding a deterministic candidate selector (`select_next_pathbank_archive_candidate`) that validates `excluded_pathway_ids` (`PathBank:SMP[0-9]+` CURIEs) and `require_unregistered_manifest` (`bool`), ranks candidate `(member, root)` slices via `rank_pathbank_archive_member_candidates`, filters out already-curated/excluded pathway IDs and (when `require_unregistered_manifest=True`) already-registered manifest keys, and returns the highest-readiness remaining candidate audit dictionary (or `None` when none remain).

## 3. Selected Implementation Work & Acceptance Criteria

### 3.1 `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) — PathBank Archive Candidate Selector & Explicit Carry-Forward

- **Implementation changes**:
  1. Add `select_next_pathbank_archive_candidate` in `src/pathwaymech/pathbank_provenance.py` to:
     - Validate that `require_unregistered_manifest` is a `bool` and that `excluded_pathway_ids` is a collection (`set`, `frozenset`, `list`, or `tuple`) of exact `PathBank:SMP[0-9]+` CURIE strings.
     - Rank `candidates` with `rank_pathbank_archive_member_candidates` against `authority_snapshot_path`.
     - Skip candidates whose `pathway_id` is in `excluded_pathway_ids` or (when `require_unregistered_manifest=True`) whose `manifest_key_registered` is `True`, and return the first remaining candidate audit dictionary (or `None` when no eligible candidate remains).
  2. Add unit tests `test_select_next_pathbank_archive_candidate_skips_registered_and_excluded_pathways` and `test_select_next_pathbank_archive_candidate_rejects_invalid_filters` in `tests/test_pathbank_identifier_authority.py`.
  3. Update `INFRA_TASKS.md` (`pathwaymech-infra-0001` machine-readable inventory entry and narrative section) to record the Cycle 7 Stage 6 disposition and explicitly carry forward (`status: deferred`) the remaining 34 non-duplicate *E. coli* `.owl` entries to Cycle 8 Stage 1 (`add_records`).
- **Acceptance criteria**:
  - `.venv/bin/pytest tests/test_pathbank_identifier_authority.py` passes (`226 passed`).
  - `INFRA_TASKS.md` parses cleanly under `kg_microbe_workflows` notebook validation with `pathwaymech-infra-0001` explicitly `deferred` and linked to `https://github.com/CultureBotAI/PathwayMech/issues/673`.

### 3.2 Verification of Previously Resolved Tasks (`pathwaymech-infra-0002` through `pathwaymech-infra-0005`)

- **Acceptance criteria**:
  - `.venv/bin/pytest tests/test_curation_publication.py tests/test_linkml_schema.py tests/test_kgx_export.py tests/test_sssom_export.py` passes with 0 failures.
  - `.venv/bin/pathwaymech-run-qc`, `.venv/bin/python scripts/record_review.py check --base main`, `.venv/bin/pytest -q`, `.venv/bin/ruff check --no-cache .`, `.venv/bin/python scripts/validate_claude_skills.py`, and `scripts/check_vendored_sync.sh` all exit `0`.
