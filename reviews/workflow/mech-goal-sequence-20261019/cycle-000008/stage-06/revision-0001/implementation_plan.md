# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019` / Cycle 8 / Stage 6)

## 1. Frozen Scope & Cutoff

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage**: `8` / `6` (`infrastructure`)
- **Frozen `INFRA_TASKS.md` snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/infra_snapshot.md`
- **Frozen `INFRA_TASKS.md` SHA-256**: `60fb4a9ce73c29211edbc12bebc8216502cba05ced1aea06218c61c77acd7481` (`87831` bytes)
- **Supervisor freeze timestamp (`scope_frozen_at`)**: `2026-10-31T13:14:58Z`
- **Base commit on `main`**: `67ab6656e659c1d617d1879bade0de362731f3bd` (PR `#763`)

## 2. Frozen Task Inventory & Dependency Graph

| Task ID | Issue | Pre-Stage 6 Status | Priority | Dependencies | Stage 6 Action | Post-Stage 6 Status |
|---|---|---|---|---|---|---|
| `pathwaymech-infra-0001` | [#673](https://github.com/CultureBotAI/PathwayMech/issues/673) | `deferred` | medium | Per-slice upstream `UniProtKB`, `Rhea` (releases 139/142), and `PubMed` authority verification alongside curated `data/pathways/*.yaml` records during Stage 1 (`add_records`) because `scripts/build_source_identifier_snapshot.py` strictly filters `data/identifier_authorities/sources.json` by `wanted = corpus_ids(records)` | Deliver `summarize_pathbank_archive_candidate_frontier` (and shared `_validate_candidate_selection_filters`) in `src/pathwaymech/pathbank_provenance.py` + unit tests in `tests/test_pathbank_identifier_authority.py` to deterministically partition any sequence of `(member, root)` candidate slices from `pathbank_primary_biopax.zip` against `data/identifier_authorities/sources.json` into registered, excluded, and remaining candidates, select `next_candidate`, and aggregate the sorted deduplicated union of missing external `UnificationXref` CURIEs (`CHEBI`, `NCBITaxon`, `UniProtKB`) across the remaining frontier; explicitly carry forward remaining 33 non-duplicate *E. coli* `.owl` slices to Cycle 9 Stage 1 (`add_records`) | `deferred` |
| `pathwaymech-infra-0002` | [#674](https://github.com/CultureBotAI/PathwayMech/issues/674) | `resolved` | medium | None | Preserve resolved implementation in `src/pathwaymech/curation.py` and re-verify unit tests in `tests/test_curation_publication.py` | `resolved` |
| `pathwaymech-infra-0003` | [#675](https://github.com/CultureBotAI/PathwayMech/issues/675) | `resolved` | low | None | Preserve resolved schema & exporter implementation in `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, and `src/pathwaymech/kgx.py` (now adopted across 78 pathway records after Cycle 8 Stage 1, Stage 2, and Stage 3: `1,474` `MechanisticEdge.coefficient` edges, `21` `EdgePredicateEnum.encodes` edges, `440` `EvidenceItem.eco_code` qualifiers, and `768` `EvidenceItem.assay_taxon` qualifiers) and re-verify unit tests | `resolved` |
| `pathwaymech-infra-0004` | [#676](https://github.com/CultureBotAI/PathwayMech/issues/676) | `resolved` | medium | None | Preserve resolved `CURIE_MAP` implementation in `src/pathwaymech/sssom.py` and `output/sssom/source_mappings.sssom.tsv` (now `1,061` total mappings across `218` records after Cycle 8 Stage 1 and Stage 3) and re-verify unit tests in `tests/test_sssom_export.py` | `resolved` |
| `pathwaymech-infra-0005` | [#677](https://github.com/CultureBotAI/PathwayMech/issues/677) | `resolved` | medium | None | Preserve resolved `BiGG` reaction prefix mapping in `src/pathwaymech/kgx.py` and within-record reaction category consistency validation in `src/pathwaymech/schema.py` (confirmed across all 277 records / 1,630 reactions in Cycle 8 Stage 4/5) and re-verify unit tests | `resolved` |

### Dependency Analysis

- `pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)), `pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)), `pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)), and `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) were resolved in Cycle 1 Stage 6 and adopted across the corpus in Cycles 2–8.
- `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) is the sole non-resolved (`deferred`) task in the frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`). In Cycle 2 Stage 6 we added `build_pathbank_archive_manifest_entry` in `src/pathwaymech/pathbank_provenance.py`; in Cycle 3 Stage 6 we hardened `build_pathbank_archive_manifest_entry` to verify unique ZIP member entries, native RDF/BioPAX XML object types, and primary `SMP[0-9]+` root pathway membership via `pathbank_terms`; in Cycle 4 Stage 6 we added `inspect_pathbank_archive_member`; in Cycle 5 Stage 6 we added `audit_pathbank_archive_member_authority`; in Cycle 6 Stage 6 we added `rank_pathbank_archive_member_candidates`; in Cycle 7 Stage 6 we added `select_next_pathbank_archive_candidate`; and in Cycle 8 Stage 1 (`add_records`) we used `select_next_pathbank_archive_candidate`, `audit_pathbank_archive_member_authority`, and `build_pathbank_archive_manifest_entry` to register `pathbank-primary-2019-PW001896-SMP0001910` (`PW001896.owl`, 25,869 bytes, SHA-256 `becce110780d247444c98ee0ed16b36e4d5f5ab9a9e61ba4201f82d3b36ebcbe`) and curate `PathBank:SMP0001910` (*Curcumin Degradation*) in `data/pathways/curcumin-degradation-escherichia-coli.yaml`, reducing the uningested non-duplicate *E. coli* PathBank `.owl` backlog from 34 to 33 files (`15` ingested *E. coli* `PathBank:*` records + `265` duplicates of existing `MetaCyc:*`/`KEGG:*`/`BioCyc:*` records + `33` remaining non-duplicate *E. coli* `.owl` files = `313` total *E. coli* `.owl` files in `pathbank_primary_biopax.zip`).
- Because `scripts/build_source_identifier_snapshot.py` (`lines 2366–2440`) strictly filters `data/identifier_authorities/sources.json` by `wanted = corpus_ids(records)` (*"The corpus only selects which identifiers to retain, keeping the checked-in authority small and provenance auditable"*), unreferenced authority identifiers for uningested `.owl` pathways cannot be bulk-populated into `data/identifier_authorities/sources.json` ahead of curating the corresponding `data/pathways/*.yaml` records.
- However, Stage 6 can further advance `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) in `src/pathwaymech/pathbank_provenance.py` by adding a deterministic whole-frontier summary helper (`summarize_pathbank_archive_candidate_frontier`) that partitions ranked `(member, root)` candidate slices into registered, excluded, and remaining candidates, selects `next_candidate`, and aggregates the sorted deduplicated union of missing external `UnificationXref` CURIEs (`CHEBI`, `NCBITaxon`, `UniProtKB`) across all remaining candidates.

## 3. Selected Implementation Work & Acceptance Criteria

### 3.1 `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) — PathBank Archive Candidate Frontier Summary & Explicit Carry-Forward

- **Implementation changes**:
  1. Add `summarize_pathbank_archive_candidate_frontier` (and shared `_validate_candidate_selection_filters`) in `src/pathwaymech/pathbank_provenance.py` to:
     - Validate that `require_unregistered_manifest` is a `bool` and that `excluded_pathway_ids` is a collection (`set`, `frozenset`, `list`, or `tuple`) of exact `PathBank:SMP[0-9]+` CURIE strings.
     - Rank `candidates` with `rank_pathbank_archive_member_candidates` against `authority_snapshot_path`.
     - Partition ranked candidates into `registered_pathway_ids`, `excluded_pathway_ids`, and `remaining_candidates`, identify `next_candidate`, and compute `missing_external_xrefs_union` across the remaining candidate frontier.
  2. Add unit tests `test_summarize_pathbank_archive_candidate_frontier_aggregates_remaining_and_missing_xrefs` and `test_summarize_pathbank_archive_candidate_frontier_rejects_invalid_filters` in `tests/test_pathbank_identifier_authority.py`.
  3. Update `INFRA_TASKS.md` (`pathwaymech-infra-0001` machine-readable inventory entry and narrative section) to record the Cycle 8 Stage 6 disposition and explicitly carry forward (`status: deferred`) the remaining 33 non-duplicate *E. coli* `.owl` entries to Cycle 9 Stage 1 (`add_records`).
- **Acceptance criteria**:
  - `.venv/bin/pytest tests/test_pathbank_identifier_authority.py` passes (`231 passed`).
  - `INFRA_TASKS.md` parses cleanly under `kg_microbe_workflows` notebook validation with `pathwaymech-infra-0001` explicitly `deferred` and linked to `https://github.com/CultureBotAI/PathwayMech/issues/673`.

### 3.2 Verification of Previously Resolved Tasks (`pathwaymech-infra-0002` through `pathwaymech-infra-0005`)

- **Acceptance criteria**:
  - `.venv/bin/pytest tests/test_curation_publication.py tests/test_linkml_schema.py tests/test_kgx_export.py tests/test_sssom_export.py` passes with 0 failures.
  - `.venv/bin/pathwaymech-run-qc`, `.venv/bin/python scripts/record_review.py check --base main`, `.venv/bin/pytest -q`, `.venv/bin/ruff check --no-cache .`, `.venv/bin/python scripts/validate_claude_skills.py`, and `scripts/check_vendored_sync.sh` all exit `0`.
