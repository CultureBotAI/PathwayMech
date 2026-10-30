# Cycle 7 Stage 5 Validation Report (`mech-goal-sequence-20261019`)

- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `7` / Stage `5` (`resolve_review_findings`) / Revision `1`
- **Source Git Base (`main`)**: `37f8fcb1e21bc105dd7b187ecc3ad780f0ff37c8`
- **GitHub Issues**: [CultureBotAI/PathwayMech#753](https://github.com/CultureBotAI/PathwayMech/issues/753), [CultureBotAI/PathwayMech#754](https://github.com/CultureBotAI/PathwayMech/issues/754)
- **Successor Structured Review Bundle**: `reviews/structured/20261030T221500Z-cycle7-stage5-resolve-review-findings/review.yaml` (`sha256: e5348ddc0624f8814a367b2a2f30129c34eae1f0d70cfc262946f1f073246fc5`)

## 1. Focused Acceptance Verification for `F-C7S4-001` & `F-C7S4-002`

1. **`F-C7S4-001` (`bare-curie-literature-reference-titles-3-metacyc-records`, 3 `MetaCyc:*` records, issue [#753](https://github.com/CultureBotAI/PathwayMech/issues/753))**:
   - Verified across all 3 remediated pathway records (`adenosine-nucleotides-degradation-ii.yaml`, `amino-sugar-superpathway.yaml`, and `gallate-degradation-i.yaml`), all 6 reassessed pathway records (`404` total `references[]` occurrences), and all `162` reference-bearing maintained pathway records in `data/pathways/*.yaml` (`7,094` total `references[]` occurrences) that **0 `references[]` entries** carry bare CURIE titles (`title == id`) (`0 / 404` in the 6 reassessed records; `0 / 7,094` corpus-wide, down from `16`).
2. **`F-C7S4-002` (`concrete-small-molecule-participants-typed-as-chemical-entity-3-metacyc-records`, 3 `MetaCyc:*` records, issue [#754](https://github.com/CultureBotAI/PathwayMech/issues/754))**:
   - Verified across all 3 remediated pathway records (`gallate-degradation-ii.yaml`, `pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`, and `thioredoxin-pathway.yaml`) that all 52 concrete small-molecule metabolites, cofactors, inorganic ions, and inhibitors (`39` `CHEBI:*`, `12` `MetaCyc:*`, and `1` `PubChem:*` `PubChem:6098323`) are typed as `category: small_molecule`, while generic electron-carrier compound classes `MetaCyc:Acceptor` and `MetaCyc:Donor-H2` at `participants[8..9]` of `thioredoxin-pathway.yaml` retain `category: chemical_entity`.
   - Verified across all `5,456` unique KGX nodes in `pages/downloads/nodes.tsv` (`sha256: a11d7ddec1368fecd0086149fc5d736dcc83e4a3ab17e66bea4ad8d571b7cc28`) that dual-typed `biolink:ChemicalEntity|biolink:SmallMolecule` node merges decreased from `59` to `42` (`17` pure `chemical_entity` vs `small_molecule` merges eliminated: `CHEBI:15422`, `CHEBI:16526`, `CHEBI:16761`, `CHEBI:16763`, `CHEBI:16810`, `CHEBI:16856`, `CHEBI:16947`, `CHEBI:18320`, `CHEBI:18407`, `CHEBI:29888`, `CHEBI:30616`, `CHEBI:31823`, `CHEBI:36655`, `CHEBI:57499`, `MetaCyc:PPI`, `MetaCyc:PROTON`, `MetaCyc:Pi`).
   - Verified that all 6 remediated pathway records were published through `pathwaymech.curation.publish_curation` and have matching append-only provenance files at `history/records/<slug>/2026-10-30T221000Z-antigravity-a1d1e5.yaml` referencing issues [#753](https://github.com/CultureBotAI/PathwayMech/issues/753) or [#754](https://github.com/CultureBotAI/PathwayMech/issues/754).
   - Verified in `pages/downloads/nodes.tsv` (`sha256: a11d7ddec1368fecd0086149fc5d736dcc83e4a3ab17e66bea4ad8d571b7cc28`) and `pages/downloads/edges.tsv` (`sha256: 7f9066d4d91bed56fd7b00a546d32845bd08cf1524f9797c4f6d7624b8722799`) that all 276 rendered HTML pages and KGX exports are synchronized.

## 2. Repository & Workflow Gate Execution

| Gate / Command | Exit Code | Result Summary |
| --- | ---: | --- |
| `.venv/bin/pathwaymech-render-pages` | `0` | `rendered 276 pathway records` |
| `.venv/bin/pathwaymech-run-qc` (`just validate`) | `0` | `validated 276 pathway records, 938 history records, 22794 evidence blocks, 33 source records; pages/ is current with 276 pathway records` |
| `.venv/bin/python scripts/record_review.py check --base main` (`just review-check`) | `0` | `{"repository": "CultureBotAI/PathwayMech", "valid_reviews": 211, "coverage": "declared_scopes_only"}` (verified append-only preservation of all 210 prior review bundles including `20261030T205500Z-cycle7-stage4-frozen-corpus-cohort-review`) |
| `.venv/bin/pytest -q` (`just test`) | `0` | `8118 passed, 3 skipped, 12 warnings` |
| `.venv/bin/ruff check --no-cache .` (`just lint`) | `0` | `All checks passed!` |
| `.venv/bin/python scripts/validate_claude_skills.py` | `0` | `validated 13 Claude skills` |
| `scripts/check_vendored_sync.sh` | `0` | `OK: 22 governed artifacts match the pinned claw revision` |
| `git diff --check` | `0` | Clean (0 whitespace or conflict marker errors) |
| `python -m kg_microbe_workflows validate-evidence` | `0` | Validated `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-05/revision-0001/evidence.yaml` against Cycle 7 Stage 4 `previous_evidence` and required outputs `issue_map` and `validation` |
