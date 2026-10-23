# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019` / Cycle 2 / Stage 6)

## 1. Frozen Scope & Provenance

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Source revision (`main` base)**: `a066b26f72d8d7ba3a0280adf90653387d26de75`
- **Supervisor-frozen `INFRA_TASKS.md` cutoff**: `2026-10-23T07:14:09Z`
- **Frozen snapshot artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md` (`sha256: 0aac2ad0f049d63088e2dd3f9624b6f3feb58fc692104e5c78136bb4d9ea6904`, `28320` bytes)
- **Frozen task inventory**: 5 tasks (`pathwaymech-infra-0001`, `pathwaymech-infra-0002`, `pathwaymech-infra-0003`, `pathwaymech-infra-0004`, `pathwaymech-infra-0005`)

## 2. Issue Intake & Dependency Graph

Every frozen task in `INFRA_TASKS.md` at cutoff `2026-10-23T07:14:09Z` was deduplicated against open and closed issues in `CultureBotAI/PathwayMech` and linked to a real GitHub issue:

| Task ID | Originating Stage | GitHub Issue | Frozen Status | Dependencies | Cycle 2 Stage 6 Disposition |
| --- | --- | --- | --- | --- | --- |
| `pathwaymech-infra-0001` | Cycle 1 Stage 1 (`add_records`) | [#673](https://github.com/CultureBotAI/PathwayMech/issues/673) | `open` | Reusable PathBank archive manifest builder (`src/pathwaymech/pathbank_provenance.py`) + per-slice upstream `UniProtKB` / `RHEA` / `CHEBI` / `PMID` authority verification during Stage 1 (`add_records`) | `deferred` (manifest-builder helper delivered in `src/pathwaymech/pathbank_provenance.py`; remaining 39 non-duplicate *E. coli* `.owl` entries carried forward to Cycle 3 Stage 1 `add_records`) |
| `pathwaymech-infra-0002` | Cycle 1 Stage 2 (`causal_graphs`) | [#674](https://github.com/CultureBotAI/PathwayMech/issues/674) | `resolved` | None (`src/pathwaymech/curation.py`) | `resolved` (preserved from Cycle 1 Stage 6; exercised across Cycle 2 Stages 2, 3, and 5) |
| `pathwaymech-infra-0003` | Cycle 1 Stage 2 (`causal_graphs`) | [#675](https://github.com/CultureBotAI/PathwayMech/issues/675) | `resolved` | None (`src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `src/pathwaymech/kgx.py`) | `resolved` (preserved from Cycle 1 Stage 6; adopted across 6 pathway records in Cycle 2 Stage 2) |
| `pathwaymech-infra-0004` | Cycle 1 Stage 3 (`protein_examples`) | [#676](https://github.com/CultureBotAI/PathwayMech/issues/676) | `resolved` | None (`src/pathwaymech/sssom.py`, `output/sssom/source_mappings.sssom.tsv`) | `resolved` (preserved from Cycle 1 Stage 6; adopted across all 95 `Saccharomyces cerevisiae` SGD pathway records in Cycle 2 Stage 3) |
| `pathwaymech-infra-0005` | Cycle 1 Stage 4 (`record_review`) | [#677](https://github.com/CultureBotAI/PathwayMech/issues/677) | `resolved` | None (`src/pathwaymech/kgx.py`, `src/pathwaymech/schema.py`) | `resolved` (preserved from Cycle 1 Stage 6; confirmed across all 271 records in Cycle 2 Stage 4 and followed by 100% explicit reaction `category` typing in Cycle 2 Stage 5 via [#692](https://github.com/CultureBotAI/PathwayMech/issues/692)) |

### Dependency Analysis & Execution Order

1. **Preserve and verify resolved Cycle 1 Stage 6 tasks (`pathwaymech-infra-0002`, `pathwaymech-infra-0003`, `pathwaymech-infra-0004`, `pathwaymech-infra-0005` — [#674](https://github.com/CultureBotAI/PathwayMech/issues/674)–[#677](https://github.com/CultureBotAI/PathwayMech/issues/677))**:
   - Tasks `0002`–`0005` were implemented in Cycle 1 Stage 6 and exercised in production across Cycle 2 Stages 2–5 (`6` causal-graph records in Stage 2, `95` SGD `source_mappings` records in Stage 3, `271`-record whole-corpus review in Stage 4, and `56` reaction-category remediations in Stage 5).
   - No new open infrastructure tasks arrived during Cycle 2 Stages 2–5.
2. **Implement reusable PathBank BioPAX archive manifest builder for `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) and carry forward corpus-selected authority indexing to Cycle 3 Stage 1 (`add_records`)**:
   - In Cycle 2 Stage 1 (`add_records`), registering `pathbank-primary-2019-PW000976-SMP0000992` (`PW000976.owl` -> `PathBank:SMP0000992`) in `conf/identifier_sources.json` required manual extraction of the `.owl` member's uncompressed byte size, SHA-256 digest, `Biopax.Pathway` `PathBank:SMP*` accession, and closed provenance metadata (`retrieved_at`, `source_version`, `license`) from `reports/local_source_ingestion/2026-10-08-pathbank-dbcan/pathbank/pathbank_primary_biopax.zip`.
   - Implementing `build_pathbank_archive_manifest_entry` (`PATHBANK_ARCHIVE_DEFAULT_PATH`, `PATHBANK_ARCHIVE_VERSION`, `PATHBANK_ARCHIVE_LICENSE`) in `src/pathwaymech/pathbank_provenance.py` automates closed, hash-verified `pathbank-biopax-zip` manifest entry construction and validates that the `.owl` member contains the expected `PathBank:SMP*` `Biopax.Pathway` accession.
   - Because `scripts/build_source_identifier_snapshot.py` (`lines 2366–2440`) strictly filters `data/identifier_authorities/sources.json` by `wanted = corpus_ids(records)` ("The corpus only selects which identifiers to retain, keeping the checked-in authority small and provenance auditable"), the remaining 39 non-duplicate *Escherichia coli* (`NCBITaxon:562`) BioPAX `.owl` entries in `pathbank_primary_biopax.zip` cannot be retained in `data/identifier_authorities/sources.json` without curating the corresponding pathway records in `data/pathways/*.yaml`. Under `CLAUDE.md` and the Stage 6 scope rules, record-level pathway curation belongs to Stage 1 (`add_records`), so `pathwaymech-infra-0001` is explicitly transitioned to `status: deferred` and carried forward under [#673](https://github.com/CultureBotAI/PathwayMech/issues/673) to Cycle 3 Stage 1 (`add_records`).

## 3. Detailed Implementation Specifications & Acceptance Criteria

### 3.1 `pathwaymech-infra-0001` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673))

- **Target files**: `src/pathwaymech/pathbank_provenance.py`, `tests/test_pathbank_identifier_authority.py`, `INFRA_TASKS.md`
- **Implementation**:
  - Add `PATHBANK_ARCHIVE_DEFAULT_PATH`, `PATHBANK_ARCHIVE_VERSION`, `PATHBANK_ARCHIVE_LICENSE`, and `build_pathbank_archive_manifest_entry(pw_id, smp_id, *, zip_path=..., archive_relpath=..., retrieved_at=..., source_version=..., license_url=..., notes=...)` in `src/pathwaymech/pathbank_provenance.py`.
  - Validate `pw_id` (`^PW[0-9]{6}$`), `smp_id` (`^SMP[0-9]{7}$`), non-empty `retrieved_at`/`source_version`/`license_url`, presence of `<PW_ID>.owl` inside the ZIP archive, and presence of the exact `Biopax.Pathway` `PathBank:<SMP_ID>` xref inside the `.owl` payload before returning a closed `pathbank-biopax-zip` manifest entry with verified `archive_member_bytes` and `archive_member_sha256` that passes `validate_pathbank_manifest_entry(..., require_closed=True)`.
  - Update `INFRA_TASKS.md` so `pathwaymech-infra-0001` records `status: deferred` with its Cycle 2 Stage 6 disposition and reconciles the `F-C2S4-001` sibling record count (`15` explicitly typed sibling records) under `pathwaymech-infra-0005`.
- **Acceptance criteria**:
  - `test_build_pathbank_archive_manifest_entry_computes_exact_closed_provenance` and `test_build_pathbank_archive_manifest_entry_rejects_invalid_inputs` in `tests/test_pathbank_identifier_authority.py` pass (`8 passed` in `tests/test_pathbank_identifier_authority.py`).
  - `INFRA_TASKS.md` passes `kg_microbe_workflows` notebook validation with `0` errors and `0` open tasks remaining (`4` `resolved`, `1` `deferred`).
