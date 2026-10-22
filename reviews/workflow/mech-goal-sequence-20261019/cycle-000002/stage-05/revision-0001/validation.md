# Cycle 2 Stage 5 Validation Report (`mech-goal-sequence-20261019`)

- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `2` / Stage `5` (`resolve_review_findings`) / Revision `1`
- **Source Git Base (`main`)**: `141d6b29ac5b00faa5d939dc6aaceea97af819b3`
- **GitHub Issue**: [CultureBotAI/PathwayMech#692](https://github.com/CultureBotAI/PathwayMech/issues/692)
- **Successor Structured Review Bundle**: `reviews/structured/20261022T152000Z-cycle2-stage5-resolve-review-findings/review.yaml` (`sha256: 387a3ec546a7d830a0cae56447e1c4469c01502fefe9fbea39ee3c7943786a74`)

## 1. Focused Acceptance Verification for `F-C2S4-001` & `F-C2S4-002`

1. **`F-C2S4-001` (`cross-record-shared-reaction-category-inconsistency`, 16 `MetaCyc:*` records / 28 occurrences across 23 shared reaction CURIEs)**:
   - Verified across all 16 affected `MetaCyc:*` records (`MetaCyc:ARABCAT-PWY`, `MetaCyc:ARGDEGRAD-PWY`, `MetaCyc:CALVIN-PWY`, `MetaCyc:DAPLYSINESYN-PWY`, `MetaCyc:GALACTUROCAT-PWY`, `MetaCyc:GLUAMCAT-PWY`, `MetaCyc:GLUCARDEG-PWY`, `MetaCyc:GLUTATHIONESYN-PWY`, `MetaCyc:HOMOSER-THRESYN-PWY`, `MetaCyc:HOMOSERSYN-PWY`, `MetaCyc:NONMEVIPP-PWY`, `MetaCyc:NONOXIPENT-PWY`, `MetaCyc:OXIDATIVEPENT-PWY`, `MetaCyc:P101-PWY`, `MetaCyc:PWY-8383`, `MetaCyc:PYRIDOXSYN-PWY`) that all 28 shared catalytic reaction entries now explicitly declare `category: molecular_activity`.
   - Verified in `pages/downloads/nodes.tsv` (`sha256: d1529fc70b2e1e341b81239c8586b1001ac1a176490583fcf19d937551583d3e`, `2546394` bytes) that all 23 shared reaction CURIEs (`22` `RHEA:*` and `1` `MetaCyc:DHBAMPLIG-RXN`) export as `category=biolink:MolecularActivity` with `source_category=molecular_activity` and uniform `source_contexts` where every participating record's reaction context declares `"category": "molecular_activity"`.
2. **`F-C2S4-002` (`corpus-wide-untyped-reactions-in-56-metacyc-records`, 56 `MetaCyc:*` records / 279 catalytic reaction entries across 254 unique reaction CURIEs)**:
   - Verified across all 271 maintained pathway records in `data/pathways/*.yaml` (`1597` total `reactions[]` entries: `1559` `molecular_activity`, `36` `pathway`, and `2` `biological_process`) that **0 records** omit `reactions[].category` (`268` records with non-empty `reactions[]` declare explicit `category` on 100% of their entries, and `3` signaling/transport `KEGG:*` records have `reactions: []`).
   - Verified in `pages/downloads/nodes.tsv` (`sha256: d1529fc70b2e1e341b81239c8586b1001ac1a176490583fcf19d937551583d3e`) that all 254 unique reaction CURIEs across the 56 remediated records (including all 231 reaction CURIEs exclusive to these 56 records that previously exported as `biolink:BiochemicalReaction` with empty `source_category`) now export with `category=biolink:MolecularActivity` and `source_category=molecular_activity`.
   - Verified that all 56 remediated records were published through `pathwaymech.curation.publish_curation` (`56 files changed, 279 insertions(+), 0 deletions(-)`) and have matching append-only provenance files at `history/records/<slug>/2026-10-22T151500Z-antigravity-a1d1e5.yaml` referencing `https://github.com/CultureBotAI/PathwayMech/issues/692`.

## 2. Repository & Workflow Gate Execution

| Gate / Command | Exit Code | Result Summary |
| --- | ---: | --- |
| `.venv/bin/pathwaymech-render-pages` | `0` | `rendered 271 pathway records to /Users/marcin/Documents/VIMSS/ontology/Mechs/PathwayMech/pages` |
| `.venv/bin/pathwaymech-run-qc` (`just validate`) | `0` | `QC passed: 271 pathway records, 711 history records, 22211 evidence blocks, 33 source records` |
| `.venv/bin/python scripts/record_review.py check --base main` (`just review-check`) | `0` | `{"repository": "CultureBotAI/PathwayMech", "valid_reviews": 201, "coverage": "declared_scopes_only"}` (verified append-only preservation of all 200 prior review bundles including `20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review`) |
| `.venv/bin/pytest -q` (`just test`) | `0` | `8066 passed, 3 skipped` |
| `.venv/bin/ruff check --no-cache .` (`just lint`) | `0` | `All checks passed!` |
| `.venv/bin/python scripts/validate_claude_skills.py` | `0` | `validated 13 project skills in /Users/marcin/Documents/VIMSS/ontology/Mechs/PathwayMech/.claude/skills` |
| `scripts/check_vendored_sync.sh` | `0` | `vendored copies match canonical sources.` |
| `git diff --check` | `0` | Clean (0 whitespace or conflict marker errors) |
| `python -m kg_microbe_workflows validate-evidence` | `0` | Validated `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml` against Cycle 2 Stage 4 `previous_evidence` and required outputs `issue_map` and `validation` |
