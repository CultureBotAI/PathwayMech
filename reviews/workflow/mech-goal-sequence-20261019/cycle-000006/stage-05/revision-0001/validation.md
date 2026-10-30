# Cycle 6 Stage 5 Validation Report (`mech-goal-sequence-20261019`)

- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `6` / Stage `5` (`resolve_review_findings`) / Revision `1`
- **Source Git Base (`main`)**: `a117b04488ca922f3fbb3491600958947a528dfa`
- **GitHub Issues**: [CultureBotAI/PathwayMech#744](https://github.com/CultureBotAI/PathwayMech/issues/744), [CultureBotAI/PathwayMech#745](https://github.com/CultureBotAI/PathwayMech/issues/745)
- **Successor Structured Review Bundle**: `reviews/structured/20261030T120000Z-cycle6-stage5-resolve-review-findings/review.yaml` (`sha256: ce1f0f7fff6a01cf6345206e3f4b3d48f0b2c8e6019df2e8c90e20d8ccfeafbd`)

## 1. Focused Acceptance Verification for `F-C6S4-001` & `F-C6S4-002`

1. **`F-C6S4-001` (`acetogenesis-ferredoxin-small-molecule-category-mismatch`, `WikiPathways:WP5019` / `data/pathways/acetogenesis.yaml`, issue [#744](https://github.com/CultureBotAI/PathwayMech/issues/744))**:
   - Verified in `data/pathways/acetogenesis.yaml` (`sha256: fdb19112a2c0e7f9ed80146367f380562896493d7b3d3a71903c83ce25a126f7`), rendered `pages/records/WikiPathways_WP5019.html`, and KGX export `pages/downloads/nodes.tsv` (`sha256: 4c03693b4fe19661da3add30ec3242e8f064edeb425b5cbe9f77cf7bd07e65f0`) that `CHEBI:17908` (`oxidized ferredoxin`) and `CHEBI:17513` (`reduced ferredoxin`) have `category: protein` (KGX `biolink:Protein`, `entity_type: protein`), matching `MetaCyc:PWY-8132` (`s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml`).
   - Verified across all `5,453` unique KGX nodes in `pages/downloads/nodes.tsv` that **0 nodes** carry conflicting `biolink:Protein|biolink:SmallMolecule` categories (`0 / 5,453`, down from `2`).
2. **`F-C6S4-002` (`bare-curie-reference-titles-5-metacyc-records`, 5 `MetaCyc:*` records, issue [#745](https://github.com/CultureBotAI/PathwayMech/issues/745))**:
   - Verified across all 6 reassessed pathway records (`209` total `references[]` occurrences; `7,082` total `references[]` occurrences across all 275 maintained records) that **0 non-literature structured-database `references[]` entries** (`MetaCyc:*`, `EcoCyc:*`, `Entrez:*`, `UniProtKB:*`) carry bare CURIE titles (`title == id`) (`0 / 209` in the 6 reassessed records; `0 / 7,082` corpus-wide).
   - Verified that all 6 remediated pathway records were published through `pathwaymech.curation.publish_curation` and have matching append-only provenance files at `history/records/<slug>/2026-10-30T115000Z-antigravity-a1d1e5.yaml` referencing issues [#744](https://github.com/CultureBotAI/PathwayMech/issues/744) or [#745](https://github.com/CultureBotAI/PathwayMech/issues/745).
   - Verified in `pages/downloads/nodes.tsv` (`sha256: 4c03693b4fe19661da3add30ec3242e8f064edeb425b5cbe9f77cf7bd07e65f0`) and `pages/downloads/edges.tsv` (`sha256: 6a279d0cb71a0197a283742e4451844898bd370c307db326f427ff990c6dbf76`) that all 275 rendered HTML pages and KGX exports are synchronized.

## 2. Repository & Workflow Gate Execution

| Gate / Command | Exit Code | Result Summary |
| --- | ---: | --- |
| `.venv/bin/pathwaymech-render-pages` | `0` | `rendered 275 pathway records` |
| `.venv/bin/pathwaymech-run-qc` (`just validate`) | `0` | `validated 275 pathway records, 915 history records, 22750 evidence blocks, 33 source records; pages/ is current with 275 pathway records` |
| `.venv/bin/python scripts/record_review.py check --base main` (`just review-check`) | `0` | `{"repository": "CultureBotAI/PathwayMech", "valid_reviews": 209, "coverage": "declared_scopes_only"}` (verified append-only preservation of all 208 prior review bundles including `20261030T095500Z-cycle6-stage4-frozen-corpus-cohort-review`) |
| `.venv/bin/pytest -q` (`just test`) | `0` | `8084 passed, 3 skipped, 12 warnings` |
| `.venv/bin/ruff check --no-cache .` (`just lint`) | `0` | `All checks passed!` |
| `.venv/bin/python scripts/validate_claude_skills.py` | `0` | `validated 13 Claude skills` |
| `scripts/check_vendored_sync.sh` | `0` | `OK: 22 governed artifacts match the pinned claw revision` |
| `git diff --check` | `0` | Clean (0 whitespace or conflict marker errors) |
| `python -m kg_microbe_workflows validate-evidence` | `0` | Validated `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-05/revision-0001/evidence.yaml` against Cycle 6 Stage 4 `previous_evidence` and required outputs `issue_map` and `validation` |
