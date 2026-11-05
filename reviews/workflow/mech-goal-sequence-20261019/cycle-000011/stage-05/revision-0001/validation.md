# Cycle 11 Stage 5 (`resolve_review_findings`) — Validation Report

## 1. Executive Summary

- **Run / Cycle / Stage**: `mech-goal-sequence-20261019` / Cycle `11` / Stage `5` (`resolve_review_findings`)
- **Git base SHA**: `76578ff449edb6a71d13000353f0832e2a12710e`
- **Predecessor workflow evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0002/evidence.yaml` (SHA-256 `20ef127fa86a0db4ee596a79048b06dfc0e8fbfde5f5667ec94b3e39ccdd7e90`)
- **Predecessor structured review**: `reviews/structured/20261105T040000Z-cycle11-stage4-frozen-corpus-cohort-review-rev2/review.yaml` (SHA-256 `b6a7e63c23499db8d51132257739195a952955755301c97c3e6c167dd2d13cb7`)
- **Successor structured review**: `reviews/structured/20261105T054000Z-cycle11-stage5-resolve-review-findings/review.yaml` (SHA-256 `3f33c9acce72d931426546775c460845f414946d36dd3504bef21b5a6d532a98`)
- **GitHub Issue**: [#791](https://github.com/CultureBotAI/PathwayMech/issues/791)
- **Outcome**: `completed` (`2 / 2` predecessor findings resolved; `0` unresolved findings; `0` carry-forward findings)

## 2. Post-Remediation Invariant Audit (11 Reassessed Records & 280-Record Maintained Corpus)

| Invariant Check | Pre-Stage 5 (`76578ff449ed`) | Post-Stage 5 (`feat/cycle11-stage5-resolve-review-findings`) | Status |
| --- | --- | --- | --- |
| Maintained pathway YAML records (`data/pathways/*.yaml`) | `280 / 280` valid (open + closed LinkML) | `280 / 280` valid (open + closed LinkML) | PASS |
| Authority-snapshot ID & label compliance (`pathwaymech-check-identifiers`) | `280 / 280` records | `280 / 280` records | PASS |
| Explicit `reactions[].category` & `reaction_type` typing | `1,637 / 1,637` (`1,599` `molecular_activity`, `36` `pathway`, `2` `biological_process`) | `1,637 / 1,637` (`1,599` `molecular_activity`, `36` `pathway`, `2` `biological_process`) | PASS |
| Explicit `RHEA:*` reaction `direction` | `737 / 737` | `737 / 737` | PASS |
| Concrete `participants[].category` typing | `7,887 / 7,887` (`+ 5` generic `gomodel:*` physical participant instances) | `7,887 / 7,887` (`+ 5` generic `gomodel:*` physical participant instances) | PASS |
| Connected `participants[]` (`0` orphans) | `7,892 / 7,892` | `7,892 / 7,892` | PASS |
| Reflexive reaction self-loops (`subject == object`) | `0 / 14,782` edges | `0 / 14,782` edges | PASS |
| Bare CURIE `references[].title` (`title == id`) | `0 / 7,121` across `166` reference-bearing records | `0 / 7,121` across `166` reference-bearing records | PASS |
| Raw local frame-token `references[].title` in `BIOTIN-BIOSYNTHESIS-PWY` + `PWY-6823` + `CALVIN-PWY` + `THISYN-PWY` (`F-C11S4-001`) | `79 / 137` structured (`79 / 225` total; `79 / 546` across 11 reassessed records; `79 / 7,121` corpus-wide) | `0 / 137` structured (`0 / 225` total; `0 / 546` across 11 reassessed records; `0 / 7,121` corpus-wide) | PASS |
| Remediable `source_context` raw local frame-token `reactions[].label` (`F-C11S4-002`) | `16 / 16` across `P321-PWY` (8), `CENTBENZCOA-PWY` (7), `PWY-5177[0]` (1) (`16 / 1,604` non-`native_roles` reactions corpus-wide) | `0 / 16` across `P321-PWY`, `CENTBENZCOA-PWY`, `PWY-5177[0]` (`0 / 1,604` non-`native_roles` reactions corpus-wide; `33 / 33` `native_roles` reactions verified as authority-locked frame-only fallbacks) | PASS |
| Append-only curation history records (`history/**/*.yaml`) | `1,029` valid records | `1,036` valid records (`+7` Stage 5 curation history records, `0` invalid links) | PASS |
| Evidence blocks (`pathwaymech-check-evidence`) | `22,954` checked | `22,954` checked | PASS |
| Rendered HTML pages & KGX exports (`pages/`) | `280` records current | `280` records current (`7` record pages + `pages/index.html` + `pages/downloads/{nodes,edges,manifest}` updated) | PASS |

## 3. Verification Commands & Gate Outputs

1. **Guarded Curation Publication (`pathwaymech.curation.publish_curation`)**:
   - Executed `apply_c11s5.py` across all 7 remediated pathway files (`data/pathways/biotin-biosynthesis-i.yaml`, `data/pathways/molybdenum-cofactor-biosynthesis.yaml`, `data/pathways/calvin-cycle.yaml`, `data/pathways/thiamine-diphosphate-biosynthesis-i.yaml`, `data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml`, `data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml`, and `data/pathways/glutaryl-coa-degradation.yaml`), writing 7 append-only curation history files at `history/records/<slug>/2026-11-05T053500Z-antigravity-a1d1e5.yaml`.
2. **Page & KGX Export Regeneration (`.venv/bin/pathwaymech-render-pages`)**:
   - Output: `rendered 280 pathway records` (exit code `0`).
3. **Full Repository QC Suite (`.venv/bin/pathwaymech-run-qc`)**:
   - `validated 280 pathway records`
   - `validated 280 records against the closed LinkML schema`
   - `verified identifiers and label policies in 280 pathway records against authority snapshots`
   - `history links: 1036 record(s), 0 invalid`
   - `No issues found` / `1036 history record(s) valid against src/pathwaymech/schema/history.yaml`
   - `checked 22954 evidence blocks`
   - `validated 33 source records`
   - `checked 6 documentation files`
   - `checked deep-research report contract`
   - `pages/ is current with 280 pathway records` (exit code `0`).
4. **Structured Review Check (`.venv/bin/python scripts/record_review.py check --base main`)**:
   - Verified `reviews/structured/20261105T054000Z-cycle11-stage5-resolve-review-findings/review.yaml` and `reviews/structured/20261105T054000Z-cycle11-stage5-resolve-review-findings/review.md` pass all schema, SHA-256 target, and predecessor-finding link checks (`resolves_findings_from` `20261105T040000Z-cycle11-stage4-frozen-corpus-cohort-review-rev2` and `20261105T030500Z-cycle11-stage4-frozen-corpus-cohort-review`).
5. **Workflow Evidence Validation (`python -m kg_microbe_workflows validate-evidence`)**:
   - Validated `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-05/revision-0001/evidence.yaml` against `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0002/evidence.yaml` with `--required-output issue_map --required-output validation`.
