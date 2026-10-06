# Adversarial review of PR #262

PR: https://github.com/CultureBotAI/PathwayMech/pull/262

Three independent review tracks inspected biochemistry, import/replay behavior, and schema/export behavior. Findings were reproduced or checked against primary evidence, filed as eight GitHub issues, and addressed before merge. The initial reviewed head was `97e937942200df330ddd84a033aeca33128a1413`; the integration base was `d8ec2b69f7a4c615aecddff80498fef1e1fab0ce`.

| Issue | Confirmed failure | Correction and acceptance evidence |
|---|---|---|
| [#263](https://github.com/CultureBotAI/PathwayMech/issues/263) | Five unresolved native GO-CAM participants were exported as biochemical reactions. | Collection-aware KGX fallback preserves unresolved participants as `NamedThing`; explicit kinds and reaction defaults remain intact. All five corpus cases are covered by regressions. |
| [#264](https://github.com/CultureBotAI/PathwayMech/issues/264) | A label heuristic classified choline and sn-glycerol 3-phosphate as lipids. | Corrected both records and replaced the heuristic with ChEBI `is_a` ancestry. Legitimate fatty-acid lipid classifications remain supported. |
| [#265](https://github.com/CultureBotAI/PathwayMech/issues/265) | ARG82 calcium was imported as a cofactor although the underlying primary observation describes a crystal contact. | Removed the edge and added a source-pinned exclusion so replay cannot restore it. No substitute metal assignment is inferred. |
| [#266](https://github.com/CultureBotAI/PathwayMech/issues/266) | THI13's exact iron redox, small-product and modified-residue equation omitted conflicting THI5 homolog evidence. | Retained only the bounded protein-bound histidyl/PLP inputs and HMP-P output; quarantined the disputed endpoints and balance terms, preserving every removed assertion in a correction ledger. Evidence remains explicitly inferred by similarity, with no transfer of an exact Candida equation to THI13. |
| [#267](https://github.com/CultureBotAI/PathwayMech/issues/267) | Local backlog guidance required a quotation even for structured database assertions. | Aligned the local rule with the schema's quotation-or-traceable-assertion contract. Governed files remain unchanged. |
| [#268](https://github.com/CultureBotAI/PathwayMech/issues/268) | Older migration replays could restore rejected biology, erase later cofactor additions, overwrite applied audit ledgers, or publish a partial cohort before failure. | Explicit apply modes, baseline guards, full-cohort preflight, and protected applied/legacy ledgers cover the curation mutators. Regression cases include default dry run, late failure, no-op replay, and optimized Python. |
| [#269](https://github.com/CultureBotAI/PathwayMech/issues/269) | BioPAX rejected reversible pathway steps and discarded valid catalytic orientation/provenance. | Retained conversion reversibility and contextual orientation separately, kept direction locators, and continued rejecting contradictory assertions. |
| [#270](https://github.com/CultureBotAI/PathwayMech/issues/270) | BioPAX rejected missing optional catalyst identities and valid RNA catalysts. | Unknown catalysts remain unknown, source-declared physical catalysts are accepted, and explicit dangling controller references still fail. |

## Evidence limits

The scientific correction ledger retains original assertions and source locators. THI13's detailed net chemistry remains unresolved in this record; omitted edges do not assert cofactor independence or the absence of physical products. The ARG82 crystal-contact observation is retained as review evidence, not a physiological calcium claim. Historical phase ledgers describe their original applied stages and are not overwritten by later no-op runs.

## Verification

Final validation and corpus measurements are recorded in the companion `adversarial-validation.json` and the current [corpus overview](README.md). Regression tests for KGX/BioPAX failed against the original production code before the fixes (21 failures), then passed after correction. The chemical-supplement replay regressions likewise failed against the original implementation before publication safeguards were added.

The first PR CI run found a stale generated landing page when combined with the newer main-branch renderer. Regenerating the site after integrating main resolves that integration failure.

Final checks completed 2026-10-05T19:44:03.818446+00:00: **580 tests passed, 3 skipped**; Ruff, skill validation, full QC, all 18 governed artifacts, and diff whitespace checks passed. Pages, KGX and SSSOM were regenerated. All 93 distinct cited source hashes were verified against retained raw artifacts.

A second reviewer independently retested the replay fixes, including supplemental-ledger collisions, invalid output destinations, closed-schema failures, late cohort failures under normal and optimized Python, and baseline refusal on current reviewed records. These checks passed. Staged publication prevents preflight failures from partially publishing a cohort; it does not claim cross-file crash atomicity.

The final ontology query join-order optimization was checked separately with four passing category regressions and four lookups against the complete ChEBI database (30.83 ms); Ruff also passed after that change. GitHub CI validates the final committed head. The three suite skips are empty vendored skill-frontmatter parametrizations; the local validator checked all seven skills.
