# Cycle 3 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `6` (`infrastructure`)
- **Frozen `INFRA_TASKS.md` cutoff**: `2026-10-23T19:09:34Z`
- **Frozen snapshot path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md`
- **Frozen snapshot SHA-256**: `d7cb8e6e1a54bfaee8699df9f961687e4485512528b3899cb216fe78e9c3d405`

## Bounded Intake Inventory at Frozen Cutoff

| Task ID | Pre-Stage-6 Status | Post-Stage-6 Status | GitHub Issue | Dependency Order | Action in Cycle 3 Stage 6 |
| --- | --- | --- | --- | --- | --- |
| `pathwaymech-infra-0001` | `deferred` | `deferred` | [#673](https://github.com/CultureBotAI/PathwayMech/issues/673) | 1 (depends on per-slice corpus record selection in `add_records`) | Harden `build_pathbank_archive_manifest_entry` in `src/pathwaymech/pathbank_provenance.py` to verify unique ZIP member entries, native RDF/BioPAX XML object types, and primary `SMP[0-9]+` root pathway membership via `pathbank_terms`, add unit tests in `tests/test_pathbank_identifier_authority.py`, and explicitly carry forward the remaining 38 non-duplicate *E. coli* PathBank `.owl` entries to Cycle 4 Stage 1 (`add_records`) |
| `pathwaymech-infra-0002` | `resolved` | `resolved` | [#674](https://github.com/CultureBotAI/PathwayMech/issues/674) | — (resolved in Cycle 1 Stage 6) | Preserve resolved status and disposition in `INFRA_TASKS.md` |
| `pathwaymech-infra-0003` | `resolved` | `resolved` | [#675](https://github.com/CultureBotAI/PathwayMech/issues/675) | — (resolved in Cycle 1 Stage 6; adopted across 6 records in Cycle 2 Stage 2 and all 8 remaining `PathBank:*` records in Cycle 3 Stage 2) | Preserve resolved status and Cycle 2/3 Stage 2 adoption dispositions in `INFRA_TASKS.md` |
| `pathwaymech-infra-0004` | `resolved` | `resolved` | [#676](https://github.com/CultureBotAI/PathwayMech/issues/676) | — (resolved in Cycle 1 Stage 6; adopted across 95 SGD records in Cycle 2 Stage 3 and 53 monomer/CDS records in Cycle 3 Stage 3) | Preserve resolved status and Cycle 2/3 Stage 3 adoption dispositions in `INFRA_TASKS.md` |
| `pathwaymech-infra-0005` | `resolved` | `resolved` | [#677](https://github.com/CultureBotAI/PathwayMech/issues/677) | — (resolved in Cycle 1 Stage 6; confirmed across all 271 records in Cycle 2 Stage 4/5 and all 272 records in Cycle 3 Stage 4/5) | Preserve resolved status and append Cycle 3 Stage 4/5 verification note in `INFRA_TASKS.md` |

## Dependency Analysis and Implementation Scope

1. **Frozen Non-Resolved Scope (`pathwaymech-infra-0001`, [#673](https://github.com/CultureBotAI/PathwayMech/issues/673))**:
   - At the frozen cutoff (`2026-10-23T19:09:34Z`), `pathwaymech-infra-0001` is the sole non-resolved task in `INFRA_TASKS.md` (`status: deferred`), linked to existing open GitHub issue [#673](https://github.com/CultureBotAI/PathwayMech/issues/673). No new infrastructure tasks arrived during Cycle 3 Stages 1–5, and no duplicate GitHub issues are created.
   - In Cycle 3 Stage 1 (`add_records`), `PW000977.owl` (`PathBank:SMP0000993`, *Secondary Metabolites: Cysteine Biosynthesis from Serine* in *Escherichia coli*, `data/pathways/cysteine-biosynthesis-from-serine-escherichia-coli.yaml`) was curated and registered in `conf/identifier_sources.json` and `data/identifier_authorities/sources.json` as `pathbank-primary-2019-PW000977-SMP0000993` using `build_pathbank_archive_manifest_entry`, reducing the remaining non-duplicate *E. coli* PathBank primary BioPAX `.owl` entries in `reports/local_source_ingestion/2026-10-08-pathbank-dbcan/pathbank/pathbank_primary_biopax.zip` from 39 to 38 (`10` ingested as *E. coli* `PathBank:*` records, `265` duplicating existing `MetaCyc:*`, `KEGG:*`, or `BioCyc:*` records, and `38` remaining non-duplicate *E. coli* `.owl` entries).
   - **Selected Repository-Local Upgrade**: Strengthen `build_pathbank_archive_manifest_entry` in `src/pathwaymech/pathbank_provenance.py` so that manifest entry construction fails closed if the archive contains duplicate entries for `member`, if `member` is not valid XML with native RDF/BioPAX top-level tags (`rdf:RDF` containing `biopax-level3.owl#` or `owl#Ontology` elements), or if `root` is not verified by `pathbank_terms(xml_root, url=PATHBANK_ARCHIVE_URL, archive_root=root)` as the primary pathway of `member` (rejecting both unlisted `SMP[0-9]+` accessions and attached `SubPathway` child stubs). Add corresponding unit tests (`test_build_pathbank_archive_manifest_entry_rejects_invalid_inputs` and `test_build_pathbank_archive_manifest_entry_rejects_duplicate_or_non_rdf_member`) in `tests/test_pathbank_identifier_authority.py`.
   - **Dependency-Driven Deferral of Remaining 38 Archive Slices**: Because `scripts/build_source_identifier_snapshot.py` (`build_snapshot`) strictly filters `data/identifier_authorities/sources.json` by `wanted = corpus_ids(records)` (*"The corpus only selects which identifiers to retain, keeping the checked-in authority small and provenance auditable"*), registering authority sources for the remaining 38 non-duplicate *E. coli* `.owl` entries without corresponding curated `data/pathways/*.yaml` records cannot populate `data/identifier_authorities/sources.json`. Therefore, `pathwaymech-infra-0001` remains explicitly `deferred` ([#673](https://github.com/CultureBotAI/PathwayMech/issues/673)) and is carried forward to Cycle 4 Stage 1 (`add_records`) for per-slice curation alongside upstream `UniProtKB`, `RHEA`, `CHEBI`, and `PMID` authority verification.

## Acceptance Criteria

1. `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md` preserves the exact supervisor-frozen `INFRA_TASKS.md` byte content (`sha256: d7cb8e6e1a54bfaee8699df9f961687e4485512528b3899cb216fe78e9c3d405`).
2. `src/pathwaymech/pathbank_provenance.py` verifies unique ZIP member entries, native RDF/BioPAX XML object types, and primary `SMP[0-9]+` root pathway membership via `pathbank_terms` inside `build_pathbank_archive_manifest_entry`, and all unit tests in `tests/test_pathbank_identifier_authority.py` pass.
3. `INFRA_TASKS.md` updates `pathwaymech-infra-0001` and `pathwaymech-infra-0005` with Cycle 3 Stage 4/5/6 dispositions and carries forward `pathwaymech-infra-0001` (`status: deferred`, [#673](https://github.com/CultureBotAI/PathwayMech/issues/673)).
4. `.venv/bin/pathwaymech-run-qc`, `.venv/bin/pytest`, and `kg_microbe_workflows validate-evidence` pass with zero errors.
