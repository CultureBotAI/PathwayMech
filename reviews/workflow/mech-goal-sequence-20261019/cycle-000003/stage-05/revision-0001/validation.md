# Cycle 3 Stage 5 Validation Report (`mech-goal-sequence-20261019`)

- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `3` / Stage `5` (`resolve_review_findings`) / Revision `1`
- **Source Git Base (`main`)**: `b34c8de1eaa4976d0bb6b0d08e6df35934662f6f`
- **GitHub Issue**: [CultureBotAI/PathwayMech#704](https://github.com/CultureBotAI/PathwayMech/issues/704)
- **Successor Structured Review Bundle**: `reviews/structured/20261023T171500Z-cycle3-stage5-resolve-review-findings/review.yaml` (`sha256: 602cbe1ae001b75f9297268d1fd4cd15b67078081d9538263de60026bda60158`)

## 1. Focused Acceptance Verification for `F-C3S4-001` & `F-C3S4-002`

1. **`F-C3S4-001` (`gomodel-missing-participant-category-in-7-records`, 7 `gomodel:YeastPathways_*` records / 11 participant entries)**:
   - Verified across all 272 maintained pathway records in `data/pathways/*.yaml` (`7,721` total `participants[]` occurrences across `3,685` unique participant CURIEs) that **0 concrete (`CHEBI:*` / non-generic) participant entries** omit `category` (`7,716 / 7,716` concrete participant occurrences declare an explicit `category`).
   - Verified in `pages/downloads/nodes.tsv` (`sha256: 832cc0b867ef1e6426336ecdba398b7466eb1d01644ee9966f1ee874b56b6de1`) that all 6 previously untyped concrete `CHEBI:*` participant CURIEs (`CHEBI:17029` -> `polymer`, `CHEBI:134413` -> `small_molecule`, and `CHEBI:143915`, `CHEBI:29979`, `CHEBI:29950`, `CHEBI:90873` -> `chemical_entity`) now export with explicit `source_category`.
   - Verified that the 5 `gomodel:*` generic physical participant instances (`gomodel:YeastPathways_PWY-5670-1/654d809000002591`, `gomodel:YeastPathways_PWY-5670-1/654d809000002611`, `gomodel:YeastPathways_PWY-1801-1/65692e7e00001183`, `gomodel:ba4cc2f6-35b0-45f1-a3b5-7bf7a1e71bf8_RXN-7605`, and `gomodel:46fed9f2-cf0b-4568-b40e-557bd0cfffe5_RXN3O-9813`) intentionally omit `participants[].category` and pass `tests/test_kgx_export.py::test_unresolved_corpus_participants_are_not_exported_as_reactions`.
2. **`F-C3S4-002` (`gomodel-oxobutanoate-mislabeled-as-lipid-in-4-records`, 4 `gomodel:YeastPathways_*` records / 4 keto-acid `CHEBI:*` participant entries)**:
   - Verified that `CHEBI:11851` (*3-methyl-2-oxobutanoate*) in `gomodel:YeastPathways_PWY3O-4105` (`data/pathways/valine-degradation.yaml`) and `CHEBI:16763` (*2-oxobutanoate*) in `gomodel:YeastPathways_HOMOCYS-CYS-CONVERT` (`data/pathways/homocysteine-and-cysteine-interconversion.yaml`), `gomodel:YeastPathways_HOMOCYSDEGR-PWY-1` (`data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml`), and `gomodel:YeastPathways_THREOCAT2-PWY` (`data/pathways/threonine-degradation.yaml`) now declare `category: small_molecule`.
   - Verified in `pages/downloads/nodes.tsv` (`sha256: 832cc0b867ef1e6426336ecdba398b7466eb1d01644ee9966f1ee874b56b6de1`) that `CHEBI:11851` now exports with `category=biolink:SmallMolecule` and `source_category=small_molecule` across all 4 participating records (`MetaCyc:LEUSYN-PWY`, `MetaCyc:PANTO-PWY`, `MetaCyc:VALSYN-PWY`, `gomodel:YeastPathways_PWY3O-4105`), and `CHEBI:16763` now exports with `category=biolink:SmallMolecule` and `source_category=chemical_entity|small_molecule` (no `lipid` misclassification).
   - Verified that all 7 remediated records were published through `pathwaymech.curation.publish_curation` (`7 files changed, 10 insertions(+), 4 deletions(-)`) and have matching append-only provenance files at `history/records/<slug>/2026-10-23T171000Z-antigravity-a1d1e5.yaml` referencing `https://github.com/CultureBotAI/PathwayMech/issues/704`.

## 2. Repository & Workflow Gate Execution

| Gate / Command | Exit Code | Result Summary |
| --- | ---: | --- |
| `.venv/bin/pathwaymech-render-pages` | `0` | `rendered 272 pathway records` |
| `.venv/bin/pathwaymech-run-qc` (`just validate`) | `0` | `QC passed: 272 pathway records, 782 history records, 22340 evidence blocks, 33 source records` |
| `.venv/bin/python scripts/record_review.py check --base main` (`just review-check`) | `0` | `{"repository": "CultureBotAI/PathwayMech", "valid_reviews": 203, "coverage": "declared_scopes_only"}` (verified append-only preservation of all 202 prior review bundles including `20261023T152000Z-cycle3-stage4-frozen-corpus-cohort-review`) |
| `.venv/bin/pytest -q` (`just test`) | `0` | `190 passed` |
| `.venv/bin/ruff check --no-cache .` (`just lint`) | `0` | `All checks passed!` |
| `.venv/bin/python scripts/validate_claude_skills.py` | `0` | `validated 13 project skills in /Users/marcin/Documents/VIMSS/ontology/Mechs/PathwayMech/.claude/skills` |
| `scripts/check_vendored_sync.sh` | `0` | `vendored copies match canonical sources.` |
| `git diff --check` | `0` | Clean (0 whitespace or conflict marker errors) |
| `python -m kg_microbe_workflows validate-evidence` | `0` | Validated `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml` against Cycle 3 Stage 4 `previous_evidence` and required outputs `issue_map` and `validation` |
