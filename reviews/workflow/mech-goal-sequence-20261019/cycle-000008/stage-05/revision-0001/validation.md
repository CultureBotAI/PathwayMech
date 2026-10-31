# Cycle 8 Stage 5 Validation Report (`mech-goal-sequence-20261019`)

- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `8` / Stage `5` (`resolve_review_findings`) / Revision `1`
- **Source Git Base (`main`)**: `f61a3ffbada676e10d3bcb89f07f364446d636aa`
- **GitHub Issues**: [CultureBotAI/PathwayMech#761](https://github.com/CultureBotAI/PathwayMech/issues/761), [CultureBotAI/PathwayMech#762](https://github.com/CultureBotAI/PathwayMech/issues/762)
- **Successor Structured Review Bundle**: `reviews/structured/20261031T112000Z-cycle8-stage5-resolve-review-findings/review.yaml` (`sha256: 542d4db72fa77dfb4984512615c0b82be6ce4a65974157cd0d86ad5ccc38b45e`)

## 1. Focused Acceptance Verification for `F-C8S4-001` & `F-C8S4-002`

1. **`F-C8S4-001` (`concrete-small-molecule-effector-participants-typed-as-chemical-entity-4-metacyc-records`, 4 `MetaCyc:*` records, issue [#761](https://github.com/CultureBotAI/PathwayMech/issues/761))**:
   - Verified across all 4 remediated pathway records (`adenosine-nucleotides-degradation-ii.yaml`, `protocatechuate-meta-cleavage.yaml`, `protocatechuate-para-cleavage.yaml`, and `pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml`), all 8 reassessed pathway records (`301` total `participants[]` occurrences), and all `277` maintained pathway records (`7,851` total `participants[]` occurrences) that **0 concrete `CHEBI:*` small-molecule participants with defined molecular formulas** remain typed as `category: chemical_entity` (`0 / 301` in the 8 reassessed records; `0 / 7,851` corpus-wide, down from `4`), while generic compound class `CHEBI:18274` (`2'-deoxyribonucleoside`) at `participants[64]` of `adenosine-nucleotides-degradation-ii.yaml` retains `category: chemical_entity`.
   - Verified in `pages/downloads/nodes.tsv` (`5,458` unique KGX nodes, `sha256: 39cc021f23d947aa3e4da019f0701d1ff473f7a5a0715816d6b683c976e7c589`) that `CHEBI:59640` (`N-acetylglucosamine`), `CHEBI:22651` (`ascorbate`), and `CHEBI:203056` (`Microcin J25`) export as `biolink:SmallMolecule` (`small_molecule`).
2. **`F-C8S4-002` (`raw-frame-id-reference-titles-17-metacyc-references-4-records`, 4 `MetaCyc:*` records, issue [#762](https://github.com/CultureBotAI/PathwayMech/issues/762))**:
   - Verified across all 4 remediated pathway records (`guanine-and-guanosine-salvage.yaml`, `sulfoquinovose-degradation-i.yaml`, `sulfoquinovose-degradation-ii.yaml`, and `nitrate-reduction-i-denitrification.yaml`), all 8 reassessed pathway records (`421` total `references[]` occurrences), and all `163` reference-bearing maintained pathway records in `data/pathways/*.yaml` (`7,099` total `references[]` occurrences) that **0 `references[]` entries** carry raw unprefixed database frame IDs (`title == local_id`) or bare CURIE strings (`title == id`) (`0 / 421` in the 8 reassessed records; `0 / 7,099` corpus-wide, down from `17`).
   - Verified that all 8 remediated pathway records were published through `pathwaymech.curation.publish_curation` and have matching append-only provenance files at `history/records/<slug>/2026-10-31T111000Z-antigravity-a1d1e5.yaml` referencing issues [#761](https://github.com/CultureBotAI/PathwayMech/issues/761) or [#762](https://github.com/CultureBotAI/PathwayMech/issues/762).
   - Verified in `pages/downloads/nodes.tsv` (`sha256: 39cc021f23d947aa3e4da019f0701d1ff473f7a5a0715816d6b683c976e7c589`) and `pages/downloads/edges.tsv` (`sha256: 95d20b276f323fb43b5b03528128e39cf863ee4b9416492f2ee6d504b2a3bc3c`) that all 277 rendered HTML pages and KGX exports are synchronized.

## 2. Repository & Workflow Gate Execution

| Gate / Command | Exit Code | Result Summary |
| --- | ---: | --- |
| `.venv/bin/pathwaymech-render-pages` | `0` | `rendered 277 pathway records` |
| `.venv/bin/pathwaymech-run-qc` (`just validate`) | `0` | `validated 277 pathway records, 963 history records, 22832 evidence blocks, 33 source records; pages/ is current with 277 pathway records` |
| `.venv/bin/python scripts/record_review.py check --base main` (`just review-check`) | `0` | `{"repository": "CultureBotAI/PathwayMech", "valid_reviews": 213, "coverage": "declared_scopes_only"}` (verified append-only preservation of all 212 prior review bundles including `20261031T094500Z-cycle8-stage4-frozen-corpus-cohort-review`) |
| `.venv/bin/pytest -q` (`just test`) | `0` | `8096 passed, 3 skipped, 12 warnings` |
| `.venv/bin/ruff check --no-cache .` (`just lint`) | `0` | `All checks passed!` |
| `.venv/bin/python scripts/validate_claude_skills.py` | `0` | `validated 13 Claude skills` |
| `scripts/check_vendored_sync.sh` | `0` | `OK: 22 governed artifacts match the pinned claw revision` |
| `git diff --check` | `0` | Clean (0 whitespace or conflict marker errors) |
| `python -m kg_microbe_workflows validate-evidence` | `0` | Validated `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-05/revision-0001/evidence.yaml` against Cycle 8 Stage 4 `previous_evidence` and required outputs `issue_map` and `validation` |
