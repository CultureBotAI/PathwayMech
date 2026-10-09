# YAML Record Review: thiamine biosynthesis

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/thiamine-biosynthesis.yaml
- Started UTC: 2026-09-25T11:35:00Z
- Finished UTC: 2026-09-25T11:41:43Z
- Verdict: Pass. None found.

## Target

- Pull request: #117, open against `main`
- Head ref: `add-gocam-thiamine-biosynthesis`
- Expected head commit: `b4428560ed71e4a7393a0625f37802476a6c1fe7`
- Verified local head commit: `b4428560ed71e4a7393a0625f37802476a6c1fe7`
- Target record: `data/pathways/thiamine-biosynthesis.yaml`
- Target id: `gomodel:YeastPathways_PWY3O-17`
- Maintained mechanistic edges: 67
- Raw Noctua source: `/private/tmp/gocam-noctua/YeastPathways_PWY3O-17.json`
- Compact SGD source: `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY3O-17.json`

## Validation

- `gh pr view 117 --json number,title,state,baseRefName,headRefName,headRefOid,mergeCommit,author,isCrossRepository,reviewDecision,url` passed and verified PR #117 is open, uses base `main`, uses head `add-gocam-thiamine-biosynthesis`, has head OID `b4428560ed71e4a7393a0625f37802476a6c1fe7`, and has no merge commit.
- `git rev-parse HEAD` passed and matched the expected head commit exactly.
- `git branch --show-current` passed and returned `add-gocam-thiamine-biosynthesis`.
- `just validate` passed: 5 Claude skills, 100 pathway records, 4,454 evidence blocks, 12 source records, 6 documentation files, and the deep-research report contract all validated.
- `just test` passed: 34 tests.
- `just lint` initially reached Ruff but failed because the read-only cache guard used `RUFF_NO_CACHE=1`; Ruff 0.16.8 requires `RUFF_NO_CACHE=true`. Retried with `RUFF_NO_CACHE=true`; `just lint` passed.
- `git diff --check` passed.
- Skipped validators: None.

## Identity and Grounding

- The YAML `id` is exactly `gomodel:YeastPathways_PWY3O-17`.
- The raw Noctua JSON `id` is exactly `gomodel:YeastPathways_PWY3O-17`.
- The compact SGD GO-CAM JSON `id` is exactly `gomodel:YeastPathways_PWY3O-17`.
- The compact SGD title is `thiamine biosynthesis - imported from: Saccharomyces Genome Database`.
- The compact SGD taxon is `NCBITaxon:559292`, matching the YAML taxon `Saccharomyces cerevisiae S288C`.
- The compact SGD status is `production`.
- The raw pathway individual `gomodel:YeastPathways_PWY3O-17/YeastPathways_PWY3O-17` is typed as `GO:0009228` with label `thiamine biosynthetic process` and has `rdfs:label` `thiamine biosynthesis`.
- Hidden-and-ignored duplicate checks used `rg --hidden --no-ignore`, excluding only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`. Searches for `YeastPathways_PWY3O-17`, `thiamine biosynthesis`, thiamine-specific raw reaction ids, and thiamine-specific GO-CAM reaction ids found only the maintained YAML and generated page/browse references for this record.

## Graph and Local References

- The maintained YAML declares 1 taxon, 28 participants, 10 reactions, 67 mechanistic edges, and 1 reference.
- Predicate distribution is exactly 21 `consumes`, 24 `produces`, 10 `enables`, and 12 `precedes`.
- All 67 edge ids are unique.
- All 67 `mechanistic_edges` endpoints resolve to the record id or to a declared taxon, participant, or reaction.
- All 67 `mechanistic_edges` use predicates from `ALLOWED_EDGE_PREDICATES`.
- All 67 `mechanistic_edges` cite declared reference `gomodel:YeastPathways_PWY3O-17`.
- No maintained YAML or rendered record page leak of `BFO:0000050`, `BFO:0000066`, `GO:0009228`, `GO:0005829`, or `lociGO` was found.

## Edge Evidence

- Raw Noctua fact counts are exactly:
  - 21 `RO:0002233`
  - 24 `RO:0002234`
  - 10 `RO:0002333`
  - 12 `RO:0002413`
  - 0 `RO:0002411`
  - 10 `BFO:0000050`
  - 10 `BFO:0000066`
- Translating the raw in-scope Noctua facts to PathwayMech predicates produced exactly 67 distinct edge triples.
- Translating the compact SGD `has_input`, `has_output`, `enabled_by`, and `causal_associations` associations produced exactly 67 distinct edge triples.
- The maintained YAML edge set exactly equals the translated raw Noctua edge set.
- The maintained YAML edge set exactly equals the translated compact SGD edge set.
- Every YAML evidence quote is an exact substring of `/private/tmp/gocam-noctua/YeastPathways_PWY3O-17.json`.
- The ten raw `BFO:0000050` and ten raw `BFO:0000066` facts were correctly excluded from the maintained 67 molecular mechanistic edges.

## Completeness

- The maintained YAML covers every in-scope raw `RO:0002233`, `RO:0002234`, `RO:0002333`, `RO:0002413`, and `RO:0002411` fact.
- The maintained YAML covers every corresponding compact SGD `has_input`, `has_output`, `enabled_by`, and `causal_associations` association.
- `pages/records/gomodel_YeastPathways_PWY3O-17.html` renders the same 67 mechanistic edges present in the YAML.
- `pages/browse.html` lists `gomodel:YeastPathways_PWY3O-17` as `thiamine biosynthesis` with `67 mechanistic edges`.

## Findings

None found.

## Recommended Edits

None found. No YAML, generated page, source-code, GitHub issue, or PR edits are recommended.

## Follow-up Checks

- After any future regeneration of generated pages, rerun `just validate`, `just test`, `just lint`, and `git diff --check`.
- No GitHub issues are recommended for this record.

## Additional Notes

- The review used the local rubric in `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/add-pathway/SKILL.md`, `docs/CURATION.md`, `docs/HARMONIZATION.md`, and `src/pathwaymech/schema.py`.
- The failed first `just lint` invocation was caused solely by an invalid environment variable value for Ruff's `--no-cache` option; the recipe passed with Ruff's documented `RUFF_NO_CACHE=true` spelling.
