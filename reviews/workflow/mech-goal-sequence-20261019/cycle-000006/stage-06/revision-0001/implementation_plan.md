# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019` / Cycle 6 / Stage 6)

## 1. Frozen Scope & Cutoff

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage**: `6` / `6` (`infrastructure`)
- **Frozen `INFRA_TASKS.md` snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/infra_snapshot.md`
- **Frozen `INFRA_TASKS.md` SHA-256**: `8c8f7957095d1b7d7696623b27ae2626abf0575ab77fc4f72082d90e50104344` (`64084` bytes)
- **Supervisor freeze timestamp (`scope_frozen_at`)**: `2026-10-30T13:39:28Z`
- **Base commit on `main`**: `8420a007dadb09bad6d03cd79350c7c970edf975` (PR `#746`)

## 2. Frozen Task Inventory & Dependency Graph

| Task ID | Issue | Pre-Stage 6 Status | Priority | Dependencies | Stage 6 Action | Post-Stage 6 Status |
|---|---|---|---|---|---|---|
| `pathwaymech-infra-0001` | [#673](https://github.com/CultureBotAI/PathwayMech/issues/673) | `deferred` | medium | Per-slice upstream `UniProtKB`, `Rhea` (releases 139/142), and `PubMed` authority verification alongside curated `data/pathways/*.yaml` records during Stage 1 (`add_records`) because `scripts/build_source_identifier_snapshot.py` strictly filters `data/identifier_authorities/sources.json` by `wanted = corpus_ids(records)` | Deliver `rank_pathbank_archive_member_candidates` in `src/pathwaymech/pathbank_provenance.py` + unit tests in `tests/test_pathbank_identifier_authority.py` to deterministically audit and rank multiple `(member, root)` candidate slices from `pathbank_primary_biopax.zip` against `data/identifier_authorities/sources.json` by `ready_for_check_identifiers`, `missing_external_xref_count`, and `missing_native_term_count`; explicitly carry forward remaining 35 non-duplicate *E. coli* `.owl` slices to Cycle 7 Stage 1 (`add_records`) | `deferred` |
| `pathwaymech-infra-0002` | [#674](https://github.com/CultureBotAI/PathwayMech/issues/674) | `resolved` | medium | None | Preserve resolved implementation in `src/pathwaymech/curation.py` and re-verify unit tests in `tests/test_curation_publication.py` | `resolved` |
| `pathwaymech-infra-0003` | [#675](https://github.com/CultureBotAI/PathwayMech/issues/675) | `resolved` | low | None | Preserve resolved schema & exporter implementation in `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, and `src/pathwaymech/kgx.py` (now adopted across 48 pathway records after Cycle 6 Stage 2 and Stage 3: `1,177` `MechanisticEdge.coefficient` edges, `21` `EdgePredicateEnum.encodes` edges, `298` `EvidenceItem.eco_code` qualifiers, and `535` `EvidenceItem.assay_taxon` qualifiers) and re-verify unit tests | `resolved` |
| `pathwaymech-infra-0004` | [#676](https://github.com/CultureBotAI/PathwayMech/issues/676) | `resolved` | medium | None | Preserve resolved `CURIE_MAP` implementation in `src/pathwaymech/sssom.py` and `output/sssom/source_mappings.sssom.tsv` (now `1,057` total mappings across `216` records after Cycle 6 Stage 1 and Stage 3) and re-verify unit tests in `tests/test_sssom_export.py` | `resolved` |
| `pathwaymech-infra-0005` | [#677](https://github.com/CultureBotAI/PathwayMech/issues/677) | `resolved` | medium | None | Preserve resolved `BiGG` reaction prefix mapping in `src/pathwaymech/kgx.py` and within-record reaction category consistency validation in `src/pathwaymech/schema.py` (confirmed across all 275 records / 1,625 reactions in Cycle 6 Stage 4/5) and re-verify unit tests | `resolved` |

### Dependency Analysis

- `pathwaymech-infra-0002` ([#674](https://github.com/CultureBotAI/PathwayMech/issues/674)), `pathwaymech-infra-0003` ([#675](https://github.com/CultureBotAI/PathwayMech/issues/675)), `pathwaymech-infra-0004` ([#676](https://github.com/CultureBotAI/PathwayMech/issues/676)), and `pathwaymech-infra-0005` ([#677](https://github.com/CultureBotAI/PathwayMech/issues/677)) were resolved in Cycle 1 Stage 6 and adopted across the corpus in Cycles 2–6.
- `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) is the sole non-resolved (`deferred`) task in the frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`). In Cycle 2 Stage 6 we added `build_pathbank_archive_manifest_entry` in `src/pathwaymech/pathbank_provenance.py`; in Cycle 3 Stage 6 we hardened `build_pathbank_archive_manifest_entry` to verify unique ZIP member entries, native RDF/BioPAX XML object types, and primary `SMP[0-9]+` root pathway membership via `pathbank_terms`; in Cycle 4 Stage 6 we added `inspect_pathbank_archive_member`; in Cycle 5 Stage 6 we added `audit_pathbank_archive_member_authority`; and in Cycle 6 Stage 1 (`add_records`) we used `audit_pathbank_archive_member_authority` and `build_pathbank_archive_manifest_entry` to register `pathbank-primary-2019-PW000975-SMP0000991` (`PW000975.owl`, 94,153 bytes, SHA-256 `6d4127c479ff0d567a7d27b147b47acea00d89992f423fb4317be677dfd82736`) and curate `PathBank:SMP0000991` (*Secondary Metabolites: Isoprenoid Biosynthesis (Nonmevalonate Pathway)*) in `data/pathways/isoprenoid-biosynthesis-nonmevalonate-pathway-escherichia-coli.yaml`, reducing the uningested non-duplicate *E. coli* PathBank `.owl` backlog from 36 to 35 files (`13` ingested *E. coli* `PathBank:*` records + `265` duplicates of existing `MetaCyc:*`/`KEGG:*`/`BioCyc:*` records + `35` remaining non-duplicate *E. coli* `.owl` files = `313` total *E. coli* `.owl` files in `pathbank_primary_biopax.zip`).
- Because `scripts/build_source_identifier_snapshot.py` (`lines 2366–2440`) strictly filters `data/identifier_authorities/sources.json` by `wanted = corpus_ids(records)` (*"The corpus only selects which identifiers to retain, keeping the checked-in authority small and provenance auditable"*), unreferenced authority identifiers for uningested `.owl` pathways cannot be bulk-populated into `data/identifier_authorities/sources.json` ahead of curating the corresponding `data/pathways/*.yaml` records.
- However, Stage 6 can further advance `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) in `src/pathwaymech/pathbank_provenance.py` by adding a deterministic multi-candidate readiness ranker (`rank_pathbank_archive_member_candidates`) that audits a sequence of unique `(member, root)` candidate slices against `data/identifier_authorities/sources.json`, computes `missing_external_xref_count` and `missing_native_term_count`, and orders the candidates from most ready (`ready_for_check_identifiers=True`, then fewest missing external `UnificationXref` CURIEs, then fewest missing native `PathBank:*` terms, then lexical `member` and `root`) to least ready.

## 3. Selected Implementation Work & Acceptance Criteria

### 3.1 `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) — Multi-Candidate PathBank Archive Readiness Ranker & Explicit Carry-Forward

- **Implementation changes**:
  1. Add `rank_pathbank_archive_member_candidates` in `src/pathwaymech/pathbank_provenance.py` to:
     - Validate that `candidates` is a non-empty sequence of unique 2-element `(member, root)` string pairs (rejecting empty inputs, non-2-element tuples, non-string elements, duplicate `member` names, or duplicate `root` accessions).
     - Call `audit_pathbank_archive_member_authority` for each `(member, root)` pair against `authority_snapshot_path`.
     - Attach `"missing_external_xref_count"` (`sum(len(curies) for curies in audit["missing_external_xrefs"].values())`) and `"missing_native_term_count"` (`len(audit["missing_native_term_ids"])`) to each candidate audit dictionary.
     - Return the candidate audit dictionaries sorted deterministically by `(not entry["ready_for_check_identifiers"], entry["missing_external_xref_count"], entry["missing_native_term_count"], entry["manifest_entry"]["archive"]["member"], entry["manifest_entry"]["archive"]["root"])`.
  2. Add unit tests `test_rank_pathbank_archive_member_candidates_orders_by_readiness_and_missing_counts` and `test_rank_pathbank_archive_member_candidates_rejects_invalid_candidates` in `tests/test_pathbank_identifier_authority.py`.
  3. Update `INFRA_TASKS.md` (`pathwaymech-infra-0001` machine-readable inventory entry and narrative section) to record the Cycle 6 Stage 6 disposition and explicitly carry forward (`status: deferred`) the remaining 35 non-duplicate *E. coli* `.owl` entries to Cycle 7 Stage 1 (`add_records`).
- **Acceptance criteria**:
  - `.venv/bin/pytest tests/test_pathbank_identifier_authority.py` passes (`221 passed`).
  - `INFRA_TASKS.md` parses cleanly under `kg_microbe_workflows` notebook validation with `pathwaymech-infra-0001` explicitly `deferred` and linked to `https://github.com/CultureBotAI/PathwayMech/issues/673`.

### 3.2 Verification of Previously Resolved Tasks (`pathwaymech-infra-0002` through `pathwaymech-infra-0005`)

- **Acceptance criteria**:
  - `.venv/bin/pytest tests/test_curation_publication.py tests/test_linkml_schema.py tests/test_kgx_export.py tests/test_sssom_export.py` passes with 0 failures.
  - `.venv/bin/pathwaymech-run-qc`, `.venv/bin/python scripts/record_review.py check --base main`, `.venv/bin/pytest -q`, `.venv/bin/ruff check --no-cache .`, `.venv/bin/python scripts/validate_claude_skills.py`, and `scripts/check_vendored_sync.sh` all exit `0`.
