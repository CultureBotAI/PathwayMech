# Cycle 1 Stage 5 Validation Report (`mech-goal-sequence-20261019`)

- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `1` / Stage `5` (`resolve_review_findings`) / Revision `1`
- **Source Git Base (`main`)**: `12a62259e1fa38b8a4094dd23df00d7edc41659f`
- **GitHub Issue**: [CultureBotAI/PathwayMech#670](https://github.com/CultureBotAI/PathwayMech/issues/670)
- **Successor Structured Review Bundle**: `reviews/structured/20261022T033000Z-stage5-resolve-review-findings/review.yaml` (`sha256: 1bfce8600667fac6006bfa93058051ab08ab1a8e3ad4825e0f02472cd33b5f89`)

## 1. Focused Acceptance Verification for `F-STAGE4-001` & `F-STAGE4-002`

1. **`F-STAGE4-001` (`amino-sugar-superpathway-bigg-reaction-missing-category`, `MetaCyc:GLCMANNANAUT-PWY`)**:
   - Verified `data/pathways/amino-sugar-superpathway.yaml` (`sha256: 1c93e912f2e349fbfab5458f309f526fcfc9d381560ac04ba35b7c442f2295f8`): `reactions[13]` (`BiGG:ACMANAptspp`, `N-acetyl-D-mannosamine transport via PTS  (periplasm)`) and `reactions[3..12]` (`10` `RHEA:*` reactions) now explicitly declare `category: molecular_activity`.
   - Verified `pages/downloads/nodes.tsv` (`sha256: 2cdc35a083b668ef3fdf21bac8c649f04e296fffaafb8b693e0804ce972a9d3b`): `BiGG:ACMANAptspp` now exports with `category=biolink:MolecularActivity` and `source_category=molecular_activity`:
     ```tsv
     BiGG:ACMANAptspp	N-acetyl-D-mannosamine transport via PTS  (periplasm)	biolink:MolecularActivity	infores:pathwaymech	molecular_activity	left_to_right	"[{""category"": ""molecular_activity"", ""collection"": ""reactions"", ""direction"": ""left_to_right"", ""id"": ""BiGG:ACMANAptspp"", ""label"": ""N-acetyl-D-mannosamine transport via PTS  (periplasm)"", ""record_id"": ""MetaCyc:GLCMANNANAUT-PWY""}]"
     ```
2. **`F-STAGE4-002` (`mixed-reaction-category-typing-in-maintained-pathways`, 12 `MetaCyc:*` records)**:
   - Verified across all 270 maintained pathway records in `data/pathways/*.yaml` that **0 records** mix explicit and omitted `reactions[].category` fields (`188` records declare `category` on 100% of their `reactions[]` entries; `82` records omit `category` on 100% of their `reactions[]` entries).
   - Verified across all 12 remediated records (`120` total reaction entries: `109` `molecular_activity` and `11` `pathway` subpathways) that all 33 previously untyped catalytic reaction entries (`30` `RHEA:*`, `2` `MetaCyc:RXN-*`, `1` `BiGG:ACMANAptspp`, corresponding to `25` unique reaction CURIEs in `pages/downloads/nodes.tsv`) export as `biolink:MolecularActivity` with `source_category=molecular_activity`.
   - Verified that all 12 remediated records have matching append-only provenance files at `history/records/<slug>/2026-10-22T032500Z-antigravity-a1d1e5.yaml` referencing `https://github.com/CultureBotAI/PathwayMech/issues/670`.

## 2. Repository & Workflow Gate Execution

| Gate / Command | Exit Code | Result Summary |
| --- | ---: | --- |
| `.venv/bin/pathwaymech-render-pages` | `0` | `rendered 270 pathway records to /Users/marcin/Documents/VIMSS/ontology/Mechs/PathwayMech/pages` |
| `.venv/bin/pathwaymech-run-qc` (`just validate`) | `0` | `QC passed: 270 pathway records, 549 history records, 22085 evidence blocks, 33 source records` |
| `.venv/bin/python scripts/record_review.py check --base main` (`just review-check`) | `0` | `{"repository": "CultureBotAI/PathwayMech", "valid_reviews": 199, "coverage": "declared_scopes_only"}` (verified append-only preservation of all 198 prior review bundles including `20261022T013600Z-stage4-frozen-corpus-cohort-review`) |
| `.venv/bin/pytest -q` (`just test`) | `0` | `8045 passed, 3 skipped` |
| `.venv/bin/ruff check --no-cache .` (`just lint`) | `0` | `All checks passed!` |
| `.venv/bin/python scripts/validate_claude_skills.py` | `0` | `validated 13 project skills in /Users/marcin/Documents/VIMSS/ontology/Mechs/PathwayMech/.claude/skills` |
| `scripts/check_vendored_sync.sh` | `0` | `vendored copies match canonical sources.` |
| `git diff --check` | `0` | Clean (0 whitespace or conflict marker errors) |
| `python -m kg_microbe_workflows validate-evidence` | `0` | Validated `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml` against Stage 4 `previous_evidence` and required outputs `issue_map` and `validation` |
