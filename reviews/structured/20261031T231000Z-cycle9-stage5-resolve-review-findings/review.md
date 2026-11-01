# Cycle 9 Stage 5 Successor Review Resolving F-C9S4-001 and F-C9S4-002 Across 5 Maintained Pathway Records

- Review: 20261031T231000Z-cycle9-stage5-resolve-review-findings
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-31T22:55:00Z
- Finished UTC: 2026-10-31T23:10:00Z
- Reviewer: Antigravity (pathwaymech-resolve-reviews + review-yaml-category) (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Re-inspected and verified all 5 maintained pathway YAML records affected by Cycle 9 Stage 4 findings F-C9S4-001 (raw-local-id-structured-reference-titles-3-metacyc-records across 3 maintained MetaCyc:* pathway records) and F-C9S4-002 (raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records across 2 maintained MetaCyc:* pathway records), grouped together under shared root-cause group G-C9S5-001 and GitHub issue #771. Remediated all 5 records via pathwaymech.curation.publish_curation: (1) across the 3 MetaCyc pathway records in F-C9S4-001 (s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml, ergothioneine-biosynthesis-i.yaml, and adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml), replaced all 16 structured MetaCyc:* cofactor, reaction, and enzyme-monomer references[] titles that retained raw unprefixed database frame IDs (title == local_id) with verified descriptive chemical cofactor, reaction, and enzyme monomer titles; and (2) across the 2 MetaCyc pathway records in F-C9S4-002 (thioredoxin-pathway.yaml and pentose-phosphate-pathway-non-oxidative-branch-ii.yaml), replaced all 11 paired MetaCyc:*/EcoCyc:* structured references[] titles in MetaCyc:THIOREDOX-PWY and all 6 MetaCyc:* reactions[].label entries in MetaCyc:PWY-8178 that retained raw unprefixed database frame IDs (title == local_id or label == local_id) with verified descriptive enzyme complex, cofactor, regulatory interaction, and reaction titles and labels (bringing raw frame-ID reference titles to 0 / 225 across the 5 reassessed records and 0 / 7,107 across all 164 reference-bearing records in the 278-record corpus, and bringing raw frame-ID reaction labels to 0 / 26 across the 5 reassessed records and 0 / 1,633 across all 278 maintained records). Recorded 5 append-only curation history files at history/records/&lt;slug&gt;/2026-10-31T230500Z-antigravity-a1d1e5.yaml, regenerated rendered pages and KGX exports (.venv/bin/pathwaymech-render-pages), and confirmed full pass across QC (278 pathway records, 985 history records, 22,889 evidence blocks, 33 source records).

## Scope And Provenance

Complete post-remediation reassessment of the 5 maintained pathway records in data/pathways/*.yaml (5 MetaCyc:*) that carried open findings (F-C9S4-001 and F-C9S4-002) in Cycle 9 Stage 4 review 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review.

Selection: All 5 maintained pathway records in CultureBotAI/PathwayMech carrying open findings in reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.yaml (100% of open Cycle 9 Stage 4 maintained-record findings).
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base 8f2f8900a1700102259d5cf86cd3c03134c57fcb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-8132 | data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml | maintained | S-methyl-5-thio-α-D-ribose 1-phosphate degradation III (MetaCyc:PWY-8132) |
| MetaCyc:PWY-7255 | data/pathways/ergothioneine-biosynthesis-i.yaml | maintained | ergothioneine biosynthesis I (bacteria) (MetaCyc:PWY-7255) |
| MetaCyc:PWY0-1241 | data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml | maintained | ADP-L-glycero-beta-D-manno-heptose biosynthesis (MetaCyc:PWY0-1241) |
| MetaCyc:THIOREDOX-PWY | data/pathways/thioredoxin-pathway.yaml | maintained | thioredoxin pathway (MetaCyc:THIOREDOX-PWY) |
| MetaCyc:PWY-8178 | data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml | maintained | pentose phosphate pathway (non-oxidative branch) II (MetaCyc:PWY-8178) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Repository QC and closed-schema validation (just validate) | passed | True | MetaCyc:PWY-8132, MetaCyc:PWY-7255, MetaCyc:PWY0-1241, MetaCyc:THIOREDOX-PWY, MetaCyc:PWY-8178 | Validated all 278 maintained pathway records (including the 5 remediated records) against the closed LinkML schema, local identifier/label authority snapshots, 985 history records, 22,889 evidence blocks, 33 source records, and pages/ synchrony. |
| Pytest unit and integration test suite (just test) | passed | True | MetaCyc:PWY-8132, MetaCyc:PWY-7255, MetaCyc:PWY0-1241, MetaCyc:THIOREDOX-PWY, MetaCyc:PWY-8178 | All pytest unit and integration tests passed across schema, KGX export, SSSOM, and record-review checks. |
| Ruff lint check (just lint) | passed | True | MetaCyc:PWY-8132, MetaCyc:PWY-7255, MetaCyc:PWY0-1241, MetaCyc:THIOREDOX-PWY, MetaCyc:PWY-8178 | Ruff check passed with 0 errors. |
| Git whitespace and conflict marker check | passed | True | MetaCyc:PWY-8132, MetaCyc:PWY-7255, MetaCyc:PWY0-1241, MetaCyc:THIOREDOX-PWY, MetaCyc:PWY-8178 | git diff --check exited 0 with no whitespace or conflict marker issues. |
| Structured review bundle contract check (just review-check) | passed | True | MetaCyc:PWY-8132, MetaCyc:PWY-7255, MetaCyc:PWY0-1241, MetaCyc:THIOREDOX-PWY, MetaCyc:PWY-8178 | All retained structured review bundles in reviews/structured/ passed schema and append-only checks against main. |

## Scientific And Domain Assessments

### Post-remediation elimination of raw unprefixed MetaCyc/EcoCyc frame-ID reference titles (0 / 225 reassessed references and 0 / 7,107 corpus references) and raw unprefixed MetaCyc frame-ID reaction labels (0 / 26 reassessed reactions and 0 / 1,633 corpus reactions) across the 5 reassessed MetaCyc pathway records

consistency: supported. Targets: MetaCyc:PWY-8132, MetaCyc:PWY-7255, MetaCyc:PWY0-1241, MetaCyc:THIOREDOX-PWY, MetaCyc:PWY-8178.

Replacing all 27 raw unprefixed MetaCyc/EcoCyc frame-ID reference titles (title == local_id) across MetaCyc:PWY-8132 (1), MetaCyc:PWY-7255 (7), MetaCyc:PWY0-1241 (8), and MetaCyc:THIOREDOX-PWY (11) brings raw frame-ID reference titles to 0 / 225 across the 5 reassessed records and 0 / 7,107 corpus-wide, and replacing all 6 raw unprefixed MetaCyc frame-ID reaction labels (label == local_id) in MetaCyc:PWY-8178 brings raw frame-ID reaction labels to 0 / 26 across the 5 reassessed records and 0 / 1,633 corpus-wide.

### Preservation of pathway identity, taxon grounding, participant connectivity, reaction directionality, stoichiometry, and edge-level evidence across the 5 remediated pathway records

evidence: supported. Targets: MetaCyc:PWY-8132, MetaCyc:PWY-7255, MetaCyc:PWY0-1241, MetaCyc:THIOREDOX-PWY, MetaCyc:PWY-8178.

Structural verification across all 5 remediated pathway YAML files confirms that all pathway IDs, taxon groundings, 7,868 connected participant entries (0 orphans), 1,633 reaction steps (733 RHEA:*), 14,753 non-reflexive mechanistic_edges, 1,064 source_mappings, and 22,889 structured evidence blocks remain 100% intact and pass closed LinkML and authority snapshot checks.

## Findings

### F-C9S4-001: All 16 structured MetaCyc:* cofactor, reaction, and enzyme-monomer references carrying raw unprefixed database frame IDs (title == local_id) are replaced with descriptive titles across 3 maintained MetaCyc pathway records

minor / resolved / confirmed; issue key: raw-local-id-structured-reference-titles-3-metacyc-records.

Across all 3 maintained MetaCyc pathway records in F-C9S4-001 (MetaCyc:PWY-8132, MetaCyc:PWY-7255, and MetaCyc:PWY0-1241), replaced all 16 structured MetaCyc:* cofactor, reaction, and enzyme-monomer references[] entries carrying raw unprefixed database frame IDs (title == local_id) with verified descriptive titles via pathwaymech.curation.publish_curation, recorded 3 history/records/&lt;slug&gt;/2026-10-31T230500Z-antigravity-a1d1e5.yaml files, and regenerated pages/ under root-cause group G-C9S5-001 (#771).

Disposition: Resolved under GitHub issue #771 (group G-C9S5-001) by replacing all 16 structured MetaCyc:* references[] entries carrying raw unprefixed database frame IDs (title == local_id) with descriptive cofactor, reaction, and enzyme monomer titles across the 3 affected MetaCyc pathway records via pathwaymech.curation.publish_curation, recording 3 history/records/&lt;slug&gt;/2026-10-31T230500Z-antigravity-a1d1e5.yaml provenance entries, and regenerating pages/.

### F-C9S4-002: All 11 paired MetaCyc:*/EcoCyc:* structured references in MetaCyc:THIOREDOX-PWY and all 6 MetaCyc:* reaction labels in MetaCyc:PWY-8178 carrying raw unprefixed database frame IDs are replaced with descriptive titles and reaction labels

minor / resolved / confirmed; issue key: raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records.

Across both maintained MetaCyc pathway records in F-C9S4-002 (MetaCyc:THIOREDOX-PWY and MetaCyc:PWY-8178), replaced all 11 paired MetaCyc:*/EcoCyc:* structured references[] entries in MetaCyc:THIOREDOX-PWY and all 6 MetaCyc:* reactions[].label entries in MetaCyc:PWY-8178 carrying raw unprefixed database frame IDs (title == local_id or label == local_id) with verified descriptive enzyme complex, cofactor, regulatory interaction, and reaction titles and labels via pathwaymech.curation.publish_curation, recorded 2 history/records/&lt;slug&gt;/2026-10-31T230500Z-antigravity-a1d1e5.yaml files, and regenerated pages/ and pages/downloads/nodes.tsv under root-cause group G-C9S5-001 (#771) (bringing raw frame-ID reference titles to 0 / 7,107 and raw frame-ID reaction labels to 0 / 1,633 corpus-wide).

Disposition: Resolved under GitHub issue #771 (group G-C9S5-001) by replacing all 11 paired MetaCyc:*/EcoCyc:* structured references[] entries in MetaCyc:THIOREDOX-PWY and all 6 MetaCyc:* reactions[].label entries in MetaCyc:PWY-8178 carrying raw unprefixed database frame IDs with descriptive titles and reaction labels via pathwaymech.curation.publish_curation, recording 2 history/records/&lt;slug&gt;/2026-10-31T230500Z-antigravity-a1d1e5.yaml provenance entries, and regenerating pages/.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: MetaCyc:PWY-8132, MetaCyc:PWY-7255, MetaCyc:PWY0-1241, MetaCyc:THIOREDOX-PWY, MetaCyc:PWY-8178. Retain all 5 remediated MetaCyc:* pathway records as distinct, non-duplicate source-scoped pathway definitions with 0 raw database frame-ID reference titles and 0 raw database frame-ID reaction labels.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EV-C9S4-PREDECESSOR | reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.yaml; findings[0] (F-C9S4-001) and findings[1] (F-C9S4-002) | supports | Predecessor Cycle 9 Stage 4 cohort review recorded two minor open representation findings across 5 maintained pathway records: F-C9S4-001 (raw-local-id-structured-reference-titles-3-metacyc-records across 3 MetaCyc:* records) and F-C9S4-002 (raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records across 2 MetaCyc:* records). |
| EV-C9S4-WORKFLOW-EVIDENCE | reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-04/revision-0001/evidence.yaml; findings[0..1] (F-C9S4-001, F-C9S4-002) | supports | Cycle 9 Stage 4 workflow evidence manifest carried forward F-C9S4-001 and F-C9S4-002 as open findings for Cycle 9 Stage 5 grouped remediation. |
| EV-C9S5-RAW-TITLES-FIXED-3 | data/pathways/ergothioneine-biosynthesis-i.yaml; references[26] in s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml, references[1..7] in ergothioneine-biosynthesis-i.yaml, and references[0,4,5,6,8,9,10,11] in adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml | supports | Across all 3 maintained MetaCyc pathway records in F-C9S4-001 (MetaCyc:PWY-8132, MetaCyc:PWY-7255, and MetaCyc:PWY0-1241), replaced all 16 structured MetaCyc:* references[] entries carrying raw unprefixed database frame ID titles (title == local_id) with verified descriptive cofactor, reaction, and enzyme monomer titles via pathwaymech.curation.publish_curation. |
| EV-C9S5-THIOREDOX-AND-PWY8178-FIXED-2 | data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml; references[60,61,66,70,77,78,106,108,110,112,114] in thioredoxin-pathway.yaml and reactions[0..5].label in pentose-phosphate-pathway-non-oxidative-branch-ii.yaml | supports | Across both maintained MetaCyc pathway records in F-C9S4-002 (MetaCyc:THIOREDOX-PWY and MetaCyc:PWY-8178), replaced all 11 paired MetaCyc:*/EcoCyc:* structured references[] entries in MetaCyc:THIOREDOX-PWY and all 6 MetaCyc:* reactions[].label entries in MetaCyc:PWY-8178 carrying raw unprefixed database frame IDs (title == local_id or label == local_id) with verified descriptive enzyme complex, cofactor, regulatory interaction, and reaction titles and labels via pathwaymech.curation.publish_curation. |
| EV-C9S5-RENDERED-PAGES-AND-KGX | pages/downloads/nodes.tsv; MetaCyc:RXN-21730, MetaCyc:SEDOBISALDOL-RXN, MetaCyc:1TRANSKETO-RXN, MetaCyc:2TRANSKETO-RXN, MetaCyc:RIB5PISOM-RXN, and MetaCyc:RIBULP3EPIM-RXN rows in pages/downloads/nodes.tsv and rendered HTML pages in pages/records/ | supports | After running .venv/bin/pathwaymech-render-pages, verified that pages/downloads/nodes.tsv exports descriptive reaction labels for MetaCyc:PWY-8178 reactions and all 5 remediated record HTML pages are current. |
| EV-C9S5-QC | .venv/bin/pathwaymech-run-qc; stdout summary (278 pathway records, 985 history records, 22,889 evidence blocks, 33 source records) | supports | Executed .venv/bin/pathwaymech-run-qc: validated 278 pathway records against the closed LinkML schema, verified all identifiers and labels against local authority snapshots, validated 985 history records (including 5 new Cycle 9 Stage 5 record history entries referencing issue #771) and 22,889 evidence blocks, and confirmed pages/ synchrony. |
| EV-C9S5-PYTEST | .venv/bin/pytest -q; pytest suite execution across tests/ | supports | Executed .venv/bin/pytest -q across the full test suite. |
| EV-C9S5-RUFF | .venv/bin/ruff check --no-cache .; ruff check output | supports | Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks passed). |
| EV-C9S5-GIT-DIFF | git diff --check; git worktree on feat/cycle9-stage5-resolve-review-findings | supports | Executed git diff --check with exit code 0; no whitespace errors or conflict markers. |
| EV-C9S5-REVIEW-CHECK | .venv/bin/python scripts/record_review.py check --base main; reviews/structured/ | supports | Validated all retained structured review bundles in reviews/structured/ against schema/record_review.yaml and verified byte-for-byte append-only preservation against main. |

## Limits And Additional Notes

- This Cycle 9 Stage 5 successor review is scoped to verifying the remediation of Cycle 9 Stage 4 findings F-C9S4-001 and F-C9S4-002 across the 5 affected maintained pathway records; the remaining 273 maintained records had zero findings in Cycle 9 Stage 4 and were verified via repository-wide QC and pytest gates.
- CLAW aggregator CLI (kg_microbe_reviews) is not installed in the local culturebotai-claw environment; finding lineage (predecessor review_id 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review, finding_ids F-C9S4-001 and F-C9S4-002, exact issue_keys, 100% target_ids retention, and absence of competing heads) was explicitly verified against reviews/structured/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T231000Z-cycle9-stage5-resolve-review-findings
kind: batch
repository: CultureBotAI/PathwayMech
title: Cycle 9 Stage 5 Successor Review Resolving F-C9S4-001 and F-C9S4-002 Across
  5 Maintained Pathway Records
started_at: '2026-10-31T22:55:00Z'
finished_at: '2026-10-31T23:10:00Z'
reviewer:
  identity: Antigravity (pathwaymech-resolve-reviews + review-yaml-category)
  kind: agent
  model: Claude Opus 4.6 (Thinking)
  independence: self_review
  independence_basis: 'Same agent session (a1d1e545-faee-4294-8a87-4c2d031a6538) implemented
    the Cycle 9 Stage 5 curation fixes for GitHub issue #771 and verified post-remediation
    records, rendered HTML pages, and KGX exports.'
skill: pathwaymech-resolve-reviews
completion: completed
verdict: pass
native_verdict: coherent
scientific_review: true
summary: 'Re-inspected and verified all 5 maintained pathway YAML records affected
  by Cycle 9 Stage 4 findings F-C9S4-001 (raw-local-id-structured-reference-titles-3-metacyc-records
  across 3 maintained MetaCyc:* pathway records) and F-C9S4-002 (raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records
  across 2 maintained MetaCyc:* pathway records), grouped together under shared root-cause
  group G-C9S5-001 and GitHub issue #771. Remediated all 5 records via pathwaymech.curation.publish_curation:
  (1) across the 3 MetaCyc pathway records in F-C9S4-001 (s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml,
  ergothioneine-biosynthesis-i.yaml, and adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml),
  replaced all 16 structured MetaCyc:* cofactor, reaction, and enzyme-monomer references[]
  titles that retained raw unprefixed database frame IDs (title == local_id) with
  verified descriptive chemical cofactor, reaction, and enzyme monomer titles; and
  (2) across the 2 MetaCyc pathway records in F-C9S4-002 (thioredoxin-pathway.yaml
  and pentose-phosphate-pathway-non-oxidative-branch-ii.yaml), replaced all 11 paired
  MetaCyc:*/EcoCyc:* structured references[] titles in MetaCyc:THIOREDOX-PWY and all
  6 MetaCyc:* reactions[].label entries in MetaCyc:PWY-8178 that retained raw unprefixed
  database frame IDs (title == local_id or label == local_id) with verified descriptive
  enzyme complex, cofactor, regulatory interaction, and reaction titles and labels
  (bringing raw frame-ID reference titles to 0 / 225 across the 5 reassessed records
  and 0 / 7,107 across all 164 reference-bearing records in the 278-record corpus,
  and bringing raw frame-ID reaction labels to 0 / 26 across the 5 reassessed records
  and 0 / 1,633 across all 278 maintained records). Recorded 5 append-only curation
  history files at history/records/<slug>/2026-10-31T230500Z-antigravity-a1d1e5.yaml,
  regenerated rendered pages and KGX exports (.venv/bin/pathwaymech-render-pages),
  and confirmed full pass across QC (278 pathway records, 985 history records, 22,889
  evidence blocks, 33 source records).'
source:
  git_revision: 8f2f8900a1700102259d5cf86cd3c03134c57fcb
  state: working_tree
  inputs:
  - path: .claude/skills/pathwaymech-resolve-reviews/SKILL.md
    sha256: 3d3b9d3b9e56cc782cf4ff63d491c5b589e9bdcde71438a695384b228edc4aea
    role: context
  - path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
    sha256: 54f54fb3e1ba485704a342681578ec8f8bb1e0c8dc9c93a5f1e5636cc046f3e1
    role: target
  - path: data/pathways/ergothioneine-biosynthesis-i.yaml
    sha256: e94253e682dc839e3917b7f1f28d2b7c384758be6dcfa17439e451ec3804aa73
    role: target
  - path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
    sha256: 01e7513a09bcdd3f0cac559a377757d145bb3764838743469bd811409f8a793a
    role: target
  - path: data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
    sha256: 9824120ec979ae03f95b9ac2ebcee6506c62f25b352e56a4d4dc47a6612efa32
    role: target
  - path: data/pathways/thioredoxin-pathway.yaml
    sha256: 6ba7bd4434c799c0576ced58654dba8c79058d2288498c5cd9e0a2cec14fac42
    role: target
  - path: pages/downloads/edges.tsv
    sha256: 9ff3b4fc68fc608f80c2dc042960f1518170e20e27f47a6b8c1a36ce8b5efa55
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 50b53a248c0beaf3e1be32bc87d45e1de17c16452eba23e00621a7365bc936d4
    role: context
  - path: pages/records/MetaCyc_PWY-7255.html
    sha256: 2d099efb8a71e1ce38aa1111e492ec3104fbf62515032623ce827707690dcd6f
    role: context
  - path: pages/records/MetaCyc_PWY-8132.html
    sha256: 0b3005c9402f40ca0b31925abb03ee5e4db9c62c29faed8f7de3ad26749c854d
    role: context
  - path: pages/records/MetaCyc_PWY-8178.html
    sha256: a1205eae07e3151df2597a9f27b72c85eb67e1a7f90cdc9a8cbefb42eb06fe45
    role: context
  - path: pages/records/MetaCyc_PWY0-1241.html
    sha256: a256e424ce95ebeb9d2d61f751d0d266aa52d2ddb622e2bd447eb5109cd72861
    role: context
  - path: pages/records/MetaCyc_THIOREDOX-PWY.html
    sha256: 62cd6161cfa35268394716695b4f51738806ab6278f17e8def8f88748c87c013
    role: context
  - path: reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.yaml
    sha256: 0150bc9f1333a79e2113c4932d5ddb742e4fb177b3d9f2bedb07df7d194b40d2
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-04/revision-0001/evidence.yaml
    sha256: 408845b19529fccbfbf0a42923a1a238ed6bc1cf8c6b260fd8baf0e230c1ed0d
    role: context
scope:
  description: Complete post-remediation reassessment of the 5 maintained pathway
    records in data/pathways/*.yaml (5 MetaCyc:*) that carried open findings (F-C9S4-001
    and F-C9S4-002) in Cycle 9 Stage 4 review 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review.
  selection: All 5 maintained pathway records in CultureBotAI/PathwayMech carrying
    open findings in reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.yaml
    (100% of open Cycle 9 Stage 4 maintained-record findings).
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  exclusions:
  - target: Remaining 273 maintained pathway records in data/pathways/*.yaml
    reason: Assessed with zero open findings in Cycle 9 Stage 4 review 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review
      and unchanged in Cycle 9 Stage 5.
  - target: research/pathway_additions/*.yaml (6 withheld staging drafts)
    reason: Non-maintained research staging drafts outside data/pathways/*.yaml; their
      2 historical open findings (F01 in 20261010T090124Z-siroheme-pathway-addition-blocked-review
      and F1 in 20261010T100956Z-ecoli-14dhna-octaprenyl-draft-review) remain untouched.
targets:
- target_id: MetaCyc:PWY-8132
  path: data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
  label: S-methyl-5-thio-α-D-ribose 1-phosphate degradation III (MetaCyc:PWY-8132)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9824120ec979ae03f95b9ac2ebcee6506c62f25b352e56a4d4dc47a6612efa32
    description: 'Raw SHA-256 file digest of data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
      in Cycle 9 Stage 5 (issue #771).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-7255
  path: data/pathways/ergothioneine-biosynthesis-i.yaml
  label: ergothioneine biosynthesis I (bacteria) (MetaCyc:PWY-7255)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e94253e682dc839e3917b7f1f28d2b7c384758be6dcfa17439e451ec3804aa73
    description: 'Raw SHA-256 file digest of data/pathways/ergothioneine-biosynthesis-i.yaml
      in Cycle 9 Stage 5 (issue #771).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1241
  path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
  label: ADP-L-glycero-beta-D-manno-heptose biosynthesis (MetaCyc:PWY0-1241)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 54f54fb3e1ba485704a342681578ec8f8bb1e0c8dc9c93a5f1e5636cc046f3e1
    description: 'Raw SHA-256 file digest of data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
      in Cycle 9 Stage 5 (issue #771).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:THIOREDOX-PWY
  path: data/pathways/thioredoxin-pathway.yaml
  label: thioredoxin pathway (MetaCyc:THIOREDOX-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6ba7bd4434c799c0576ced58654dba8c79058d2288498c5cd9e0a2cec14fac42
    description: 'Raw SHA-256 file digest of data/pathways/thioredoxin-pathway.yaml
      in Cycle 9 Stage 5 (issue #771).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/thioredoxin-pathway.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-8178
  path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
  label: pentose phosphate pathway (non-oxidative branch) II (MetaCyc:PWY-8178)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 01e7513a09bcdd3f0cac559a377757d145bb3764838743469bd811409f8a793a
    description: 'Raw SHA-256 file digest of data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
      in Cycle 9 Stage 5 (issue #771).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
    role: maintained pathway YAML
checks:
- check_id: validate
  name: Repository QC and closed-schema validation (just validate)
  status: passed
  required: true
  summary: Validated all 278 maintained pathway records (including the 5 remediated
    records) against the closed LinkML schema, local identifier/label authority snapshots,
    985 history records, 22,889 evidence blocks, 33 source records, and pages/ synchrony.
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  command: .venv/bin/pathwaymech-run-qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C9S5-QC
  scope_note: 'Full-repository QC gate after applying issue #771 fixes and regenerating
    pages/.'
- check_id: test
  name: Pytest unit and integration test suite (just test)
  status: passed
  required: true
  summary: All pytest unit and integration tests passed across schema, KGX export,
    SSSOM, and record-review checks.
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  command: .venv/bin/pytest -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C9S5-PYTEST
  scope_note: Full pytest test suite.
- check_id: lint
  name: Ruff lint check (just lint)
  status: passed
  required: true
  summary: Ruff check passed with 0 errors.
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  command: .venv/bin/ruff check --no-cache .
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C9S5-RUFF
  scope_note: Repository-wide Python lint check.
- check_id: git-diff-check
  name: Git whitespace and conflict marker check
  status: passed
  required: true
  summary: git diff --check exited 0 with no whitespace or conflict marker issues.
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C9S5-GIT-DIFF
  scope_note: Worktree diff check across all Cycle 9 Stage 5 edits.
- check_id: review-check
  name: Structured review bundle contract check (just review-check)
  status: passed
  required: true
  summary: All retained structured review bundles in reviews/structured/ passed schema
    and append-only checks against main.
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  command: .venv/bin/python scripts/record_review.py check --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C9S5-REVIEW-CHECK
  scope_note: Verifies append-only immutability of prior bundles and validity of current
    bundle.
evidence:
- evidence_id: EV-C9S4-PREDECESSOR
  kind: prior_review
  reference: reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.yaml
  locator: findings[0] (F-C9S4-001) and findings[1] (F-C9S4-002)
  accessed_at: '2026-10-31T22:55:00Z'
  support: supports
  summary: 'Predecessor Cycle 9 Stage 4 cohort review recorded two minor open representation
    findings across 5 maintained pathway records: F-C9S4-001 (raw-local-id-structured-reference-titles-3-metacyc-records
    across 3 MetaCyc:* records) and F-C9S4-002 (raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records
    across 2 MetaCyc:* records).'
  snapshot_sha256: 0150bc9f1333a79e2113c4932d5ddb742e4fb177b3d9f2bedb07df7d194b40d2
- evidence_id: EV-C9S4-WORKFLOW-EVIDENCE
  kind: prior_review
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-04/revision-0001/evidence.yaml
  locator: findings[0..1] (F-C9S4-001, F-C9S4-002)
  accessed_at: '2026-10-31T22:55:00Z'
  support: supports
  summary: Cycle 9 Stage 4 workflow evidence manifest carried forward F-C9S4-001 and
    F-C9S4-002 as open findings for Cycle 9 Stage 5 grouped remediation.
  snapshot_sha256: 408845b19529fccbfbf0a42923a1a238ed6bc1cf8c6b260fd8baf0e230c1ed0d
- evidence_id: EV-C9S5-RAW-TITLES-FIXED-3
  kind: record_content
  reference: data/pathways/ergothioneine-biosynthesis-i.yaml
  locator: references[26] in s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml,
    references[1..7] in ergothioneine-biosynthesis-i.yaml, and references[0,4,5,6,8,9,10,11]
    in adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
  accessed_at: '2026-10-31T23:05:00Z'
  support: supports
  summary: Across all 3 maintained MetaCyc pathway records in F-C9S4-001 (MetaCyc:PWY-8132,
    MetaCyc:PWY-7255, and MetaCyc:PWY0-1241), replaced all 16 structured MetaCyc:*
    references[] entries carrying raw unprefixed database frame ID titles (title ==
    local_id) with verified descriptive cofactor, reaction, and enzyme monomer titles
    via pathwaymech.curation.publish_curation.
  quote: "- id: MetaCyc:GLUTCYSLIG-RXN\n  title: glutamate--cysteine ligase reaction\
    \ (MetaCyc:GLUTCYSLIG-RXN)\n  url: https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=GLUTCYSLIG-RXN"
  snapshot_sha256: e94253e682dc839e3917b7f1f28d2b7c384758be6dcfa17439e451ec3804aa73
- evidence_id: EV-C9S5-THIOREDOX-AND-PWY8178-FIXED-2
  kind: record_content
  reference: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
  locator: references[60,61,66,70,77,78,106,108,110,112,114] in thioredoxin-pathway.yaml
    and reactions[0..5].label in pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
  accessed_at: '2026-10-31T23:05:00Z'
  support: supports
  summary: Across both maintained MetaCyc pathway records in F-C9S4-002 (MetaCyc:THIOREDOX-PWY
    and MetaCyc:PWY-8178), replaced all 11 paired MetaCyc:*/EcoCyc:* structured references[]
    entries in MetaCyc:THIOREDOX-PWY and all 6 MetaCyc:* reactions[].label entries
    in MetaCyc:PWY-8178 carrying raw unprefixed database frame IDs (title == local_id
    or label == local_id) with verified descriptive enzyme complex, cofactor, regulatory
    interaction, and reaction titles and labels via pathwaymech.curation.publish_curation.
  quote: "- id: MetaCyc:RXN-21730\n  label: diphosphate-dependent D-sedoheptulose\
    \ 7-phosphate 1-phosphotransferase reaction\n  reaction_type: enzymatic\n  ec_number:\
    \ EC:2.7.1.147\n  category: molecular_activity"
  snapshot_sha256: 01e7513a09bcdd3f0cac559a377757d145bb3764838743469bd811409f8a793a
- evidence_id: EV-C9S5-RENDERED-PAGES-AND-KGX
  kind: record_content
  reference: pages/downloads/nodes.tsv
  locator: MetaCyc:RXN-21730, MetaCyc:SEDOBISALDOL-RXN, MetaCyc:1TRANSKETO-RXN, MetaCyc:2TRANSKETO-RXN,
    MetaCyc:RIB5PISOM-RXN, and MetaCyc:RIBULP3EPIM-RXN rows in pages/downloads/nodes.tsv
    and rendered HTML pages in pages/records/
  accessed_at: '2026-10-31T23:08:00Z'
  support: supports
  summary: After running .venv/bin/pathwaymech-render-pages, verified that pages/downloads/nodes.tsv
    exports descriptive reaction labels for MetaCyc:PWY-8178 reactions and all 5 remediated
    record HTML pages are current.
  quote: "MetaCyc:RXN-21730\tdiphosphate-dependent D-sedoheptulose 7-phosphate 1-phosphotransferase\
    \ reaction\tbiolink:BiochemicalReaction\tinfores:pathwaymech\tmolecular_activity"
  snapshot_sha256: 50b53a248c0beaf3e1be32bc87d45e1de17c16452eba23e00621a7365bc936d4
- evidence_id: EV-C9S5-QC
  kind: validation
  reference: .venv/bin/pathwaymech-run-qc
  locator: stdout summary (278 pathway records, 985 history records, 22,889 evidence
    blocks, 33 source records)
  accessed_at: '2026-10-31T23:10:00Z'
  support: supports
  summary: 'Executed .venv/bin/pathwaymech-run-qc: validated 278 pathway records against
    the closed LinkML schema, verified all identifiers and labels against local authority
    snapshots, validated 985 history records (including 5 new Cycle 9 Stage 5 record
    history entries referencing issue #771) and 22,889 evidence blocks, and confirmed
    pages/ synchrony.'
- evidence_id: EV-C9S5-PYTEST
  kind: validation
  reference: .venv/bin/pytest -q
  locator: pytest suite execution across tests/
  accessed_at: '2026-10-31T23:10:00Z'
  support: supports
  summary: Executed .venv/bin/pytest -q across the full test suite.
- evidence_id: EV-C9S5-RUFF
  kind: validation
  reference: .venv/bin/ruff check --no-cache .
  locator: ruff check output
  accessed_at: '2026-10-31T23:10:00Z'
  support: supports
  summary: Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks
    passed).
- evidence_id: EV-C9S5-GIT-DIFF
  kind: validation
  reference: git diff --check
  locator: git worktree on feat/cycle9-stage5-resolve-review-findings
  accessed_at: '2026-10-31T23:10:00Z'
  support: supports
  summary: Executed git diff --check with exit code 0; no whitespace errors or conflict
    markers.
- evidence_id: EV-C9S5-REVIEW-CHECK
  kind: validation
  reference: .venv/bin/python scripts/record_review.py check --base main
  locator: reviews/structured/
  accessed_at: '2026-10-31T23:10:00Z'
  support: supports
  summary: Validated all retained structured review bundles in reviews/structured/
    against schema/record_review.yaml and verified byte-for-byte append-only preservation
    against main.
assessments:
- assessment_id: ASSESS-C9S5-RAW-FRAME-ID-HYGIENE-5
  area: consistency
  topic: Post-remediation elimination of raw unprefixed MetaCyc/EcoCyc frame-ID reference
    titles (0 / 225 reassessed references and 0 / 7,107 corpus references) and raw
    unprefixed MetaCyc frame-ID reaction labels (0 / 26 reassessed reactions and 0
    / 1,633 corpus reactions) across the 5 reassessed MetaCyc pathway records
  outcome: supported
  summary: Replacing all 27 raw unprefixed MetaCyc/EcoCyc frame-ID reference titles
    (title == local_id) across MetaCyc:PWY-8132 (1), MetaCyc:PWY-7255 (7), MetaCyc:PWY0-1241
    (8), and MetaCyc:THIOREDOX-PWY (11) brings raw frame-ID reference titles to 0
    / 225 across the 5 reassessed records and 0 / 7,107 corpus-wide, and replacing
    all 6 raw unprefixed MetaCyc frame-ID reaction labels (label == local_id) in MetaCyc:PWY-8178
    brings raw frame-ID reaction labels to 0 / 26 across the 5 reassessed records
    and 0 / 1,633 corpus-wide.
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  evidence_ids:
  - EV-C9S4-PREDECESSOR
  - EV-C9S5-RAW-TITLES-FIXED-3
  - EV-C9S5-THIOREDOX-AND-PWY8178-FIXED-2
  - EV-C9S5-RENDERED-PAGES-AND-KGX
  - EV-C9S5-QC
  - EV-C9S5-PYTEST
  metrics:
  - name: raw_frame_id_reference_titles_across_reassessed_records
    value: 0.0
    unit: references
    definition: Count of structured references[] entries carrying raw unprefixed database
      frame IDs (title == local_id) across the 5 reassessed pathway records after
      updating 27 MetaCyc:*/EcoCyc:* entries (0 / 225 in reassessed records; 0 / 7,107
      corpus-wide).
    denominator: 225
    minimum: 0.0
    maximum: 225.0
  - name: raw_frame_id_reaction_labels_across_reassessed_records
    value: 0.0
    unit: reactions
    definition: Count of reactions[] entries carrying raw unprefixed database frame
      IDs (label == local_id) across the 5 reassessed pathway records after updating
      6 MetaCyc:* reaction labels in MetaCyc:PWY-8178 (0 / 26 in reassessed records;
      0 / 1,633 corpus-wide).
    denominator: 26
    minimum: 0.0
    maximum: 26.0
  dimensions:
  - name: rendered_page_and_kgx_verification
    value: All 27 updated MetaCyc/EcoCyc reference titles and 6 updated MetaCyc reaction
      labels rendered in MetaCyc_PWY-8132.html, MetaCyc_PWY-7255.html, MetaCyc_PWY0-1241.html,
      MetaCyc_THIOREDOX-PWY.html, MetaCyc_PWY-8178.html, and pages/downloads/nodes.tsv
    definition: Verified post-remediation rendered HTML pages and KGX exports in pages/.
    evidence_ids:
    - EV-C9S5-RENDERED-PAGES-AND-KGX
    - EV-C9S5-QC
- assessment_id: ASSESS-C9S5-SCIENTIFIC-INTEGRITY-5
  area: evidence
  topic: Preservation of pathway identity, taxon grounding, participant connectivity,
    reaction directionality, stoichiometry, and edge-level evidence across the 5 remediated
    pathway records
  outcome: supported
  summary: Structural verification across all 5 remediated pathway YAML files confirms
    that all pathway IDs, taxon groundings, 7,868 connected participant entries (0
    orphans), 1,633 reaction steps (733 RHEA:*), 14,753 non-reflexive mechanistic_edges,
    1,064 source_mappings, and 22,889 structured evidence blocks remain 100% intact
    and pass closed LinkML and authority snapshot checks.
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  evidence_ids:
  - EV-C9S5-RAW-TITLES-FIXED-3
  - EV-C9S5-THIOREDOX-AND-PWY8178-FIXED-2
  - EV-C9S5-QC
  - EV-C9S5-PYTEST
  - EV-C9S5-GIT-DIFF
findings:
- finding_id: F-C9S4-001
  issue_key: raw-local-id-structured-reference-titles-3-metacyc-records
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: All 16 structured MetaCyc:* cofactor, reaction, and enzyme-monomer references
    carrying raw unprefixed database frame IDs (title == local_id) are replaced with
    descriptive titles across 3 maintained MetaCyc pathway records
  description: Across all 3 maintained MetaCyc pathway records in F-C9S4-001 (MetaCyc:PWY-8132,
    MetaCyc:PWY-7255, and MetaCyc:PWY0-1241), replaced all 16 structured MetaCyc:*
    cofactor, reaction, and enzyme-monomer references[] entries carrying raw unprefixed
    database frame IDs (title == local_id) with verified descriptive titles via pathwaymech.curation.publish_curation,
    recorded 3 history/records/<slug>/2026-10-31T230500Z-antigravity-a1d1e5.yaml files,
    and regenerated pages/ under root-cause group G-C9S5-001 (#771).
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  field_paths:
  - data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml#references[26].title
    (MetaCyc:NADH) (NADH -> NADH (MetaCyc:NADH))
  - data/pathways/ergothioneine-biosynthesis-i.yaml#references[1].title (MetaCyc:GLUTCYSLIG-RXN)
    (GLUTCYSLIG-RXN -> glutamate--cysteine ligase reaction (MetaCyc:GLUTCYSLIG-RXN))
  - data/pathways/ergothioneine-biosynthesis-i.yaml#references[2].title (MetaCyc:RXN-14431)
    (RXN-14431 -> L-histidine N-alpha-methyltransferase reaction (MetaCyc:RXN-14431))
  - data/pathways/ergothioneine-biosynthesis-i.yaml#references[3].title (MetaCyc:RXN-14430)
    (RXN-14430 -> N-alpha,N-alpha-dimethyl-L-histidine N-alpha-methyltransferase reaction
    (MetaCyc:RXN-14430))
  - data/pathways/ergothioneine-biosynthesis-i.yaml#references[4].title (MetaCyc:RXN-14429)
    (RXN-14429 -> hercynine/gamma-L-glutamyl-L-cysteine sulfoxide synthase reaction
    (MetaCyc:RXN-14429))
  - data/pathways/ergothioneine-biosynthesis-i.yaml#references[5].title (MetaCyc:RXN-18088)
    (RXN-18088 -> gamma-glutamyl-hercynylcysteine sulfoxide hydrolase reaction (MetaCyc:RXN-18088))
  - data/pathways/ergothioneine-biosynthesis-i.yaml#references[6].title (MetaCyc:RXN-18089)
    (RXN-18089 -> hercynylcysteine sulfoxide lyase reaction (MetaCyc:RXN-18089))
  - data/pathways/ergothioneine-biosynthesis-i.yaml#references[7].title (MetaCyc:RXN-15804)
    (RXN-15804 -> 2-(hydroxysulfanyl)hercynine reduction to ergothioneine (MetaCyc:RXN-15804))
  - data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml#references[0].title
    (MetaCyc:5.1.3.20-RXN) (5.1.3.20-RXN -> ADP-glyceromanno-heptose 6-epimerase reaction
    (MetaCyc:5.1.3.20-RXN))
  - data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml#references[4].title
    (MetaCyc:EG10838-MONOMER) (EG10838-MONOMER -> ADP-L-glycero-D-manno-heptose-6-epimerase
    HldD monomer (MetaCyc:EG10838-MONOMER))
  - data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml#references[5].title
    (MetaCyc:G6106-MONOMER) (G6106-MONOMER -> D-sedoheptulose 7-phosphate isomerase
    GmhA monomer (MetaCyc:G6106-MONOMER))
  - data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml#references[6].title
    (MetaCyc:G7590-MONOMER) (G7590-MONOMER -> bifunctional D-glycero-beta-D-manno-heptose
    7-phosphate kinase / 1-phosphate adenylyltransferase HldE monomer (MetaCyc:G7590-MONOMER))
  - data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml#references[8].title
    (MetaCyc:RXN0-4301) (RXN0-4301 -> D-sedoheptulose 7-phosphate isomerase reaction
    (MetaCyc:RXN0-4301))
  - data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml#references[9].title
    (MetaCyc:RXN0-4341) (RXN0-4341 -> D-glycero-beta-D-manno-heptose 7-phosphate 1-kinase
    reaction (MetaCyc:RXN0-4341))
  - data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml#references[10].title
    (MetaCyc:RXN0-4342) (RXN0-4342 -> D-glycero-beta-D-manno-heptose 1,7-bisphosphate
    7-phosphatase reaction (MetaCyc:RXN0-4342))
  - data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml#references[11].title
    (MetaCyc:RXN0-4361) (RXN0-4361 -> D-glycero-beta-D-manno-heptose 1-phosphate adenylyltransferase
    reaction (MetaCyc:RXN0-4361))
  evidence_ids:
  - EV-C9S4-PREDECESSOR
  - EV-C9S4-WORKFLOW-EVIDENCE
  - EV-C9S5-RAW-TITLES-FIXED-3
  - EV-C9S5-RENDERED-PAGES-AND-KGX
  - EV-C9S5-QC
  - EV-C9S5-PYTEST
  rule_id: CURATION:no-raw-local-id-structured-reference-titles
  native_severity: minor
  normalization_reason: 'Native minor representation defect maps directly to minor
    severity: replacing the 16 raw unprefixed MetaCyc frame-ID reference titles across
    the 3 affected MetaCyc records with descriptive cofactor, reaction, and enzyme
    monomer titles eliminates raw frame-ID reference titles in these records.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
    role: maintained pathway YAML
  disposition_reason: 'Resolved under GitHub issue #771 (group G-C9S5-001) by replacing
    all 16 structured MetaCyc:* references[] entries carrying raw unprefixed database
    frame IDs (title == local_id) with descriptive cofactor, reaction, and enzyme
    monomer titles across the 3 affected MetaCyc pathway records via pathwaymech.curation.publish_curation,
    recording 3 history/records/<slug>/2026-10-31T230500Z-antigravity-a1d1e5.yaml
    provenance entries, and regenerating pages/.'
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review
    finding_id: F-C9S4-001
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/771
  tags:
  - cycle9-stage5-resolve-review-findings
  - raw-frame-id-reference-title
  - reference-hygiene
- finding_id: F-C9S4-002
  issue_key: raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: All 11 paired MetaCyc:*/EcoCyc:* structured references in MetaCyc:THIOREDOX-PWY
    and all 6 MetaCyc:* reaction labels in MetaCyc:PWY-8178 carrying raw unprefixed
    database frame IDs are replaced with descriptive titles and reaction labels
  description: Across both maintained MetaCyc pathway records in F-C9S4-002 (MetaCyc:THIOREDOX-PWY
    and MetaCyc:PWY-8178), replaced all 11 paired MetaCyc:*/EcoCyc:* structured references[]
    entries in MetaCyc:THIOREDOX-PWY and all 6 MetaCyc:* reactions[].label entries
    in MetaCyc:PWY-8178 carrying raw unprefixed database frame IDs (title == local_id
    or label == local_id) with verified descriptive enzyme complex, cofactor, regulatory
    interaction, and reaction titles and labels via pathwaymech.curation.publish_curation,
    recorded 2 history/records/<slug>/2026-10-31T230500Z-antigravity-a1d1e5.yaml files,
    and regenerated pages/ and pages/downloads/nodes.tsv under root-cause group G-C9S5-001
    (#771) (bringing raw frame-ID reference titles to 0 / 7,107 and raw frame-ID reaction
    labels to 0 / 1,633 corpus-wide).
  target_ids:
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  field_paths:
  - data/pathways/thioredoxin-pathway.yaml#references[60].title (MetaCyc:THIOREDOXIN-REDUCT-NADPH-RXN)
    (THIOREDOXIN-REDUCT-NADPH-RXN -> thioredoxin-disulfide reductase reaction (MetaCyc:THIOREDOXIN-REDUCT-NADPH-RXN))
  - data/pathways/thioredoxin-pathway.yaml#references[61].title (MetaCyc:THIOREDOXIN-RXN)
    (THIOREDOXIN-RXN -> thioredoxin oxidation reaction (MetaCyc:THIOREDOXIN-RXN))
  - data/pathways/thioredoxin-pathway.yaml#references[66].title (MetaCyc:NADPH) (NADPH
    -> reduced nicotinamide adenine dinucleotide phosphate (MetaCyc:NADPH))
  - data/pathways/thioredoxin-pathway.yaml#references[70].title (EcoCyc:THIOREDOXIN-REDUCT-NADPH-CPLX)
    (THIOREDOXIN-REDUCT-NADPH-CPLX -> thioredoxin reductase complex TrxB (EcoCyc:THIOREDOXIN-REDUCT-NADPH-CPLX))
  - data/pathways/thioredoxin-pathway.yaml#references[77].title (EcoCyc:REG0-6357)
    (REG0-6357 -> OxyR transcriptional activation of trxC (EcoCyc:REG0-6357))
  - data/pathways/thioredoxin-pathway.yaml#references[78].title (EcoCyc:REG0-6358)
    (REG0-6358 -> IscR transcriptional repression of trxC (EcoCyc:REG0-6358))
  - data/pathways/thioredoxin-pathway.yaml#references[106].title (EcoCyc:THIOREDOXIN-REDUCT-NADPH-RXN)
    (THIOREDOXIN-REDUCT-NADPH-RXN -> thioredoxin-disulfide reductase reaction (EcoCyc:THIOREDOXIN-REDUCT-NADPH-RXN))
  - data/pathways/thioredoxin-pathway.yaml#references[108].title (EcoCyc:REG0-10687)
    (REG0-10687 -> SoxS transcriptional activation of trxA (EcoCyc:REG0-10687))
  - data/pathways/thioredoxin-pathway.yaml#references[110].title (EcoCyc:REG0-9797)
    (REG0-9797 -> BaeR transcriptional activation of trxA (EcoCyc:REG0-9797))
  - data/pathways/thioredoxin-pathway.yaml#references[112].title (EcoCyc:REG0-9025)
    (REG0-9025 -> ppGpp/DksA transcriptional activation of trxA (EcoCyc:REG0-9025))
  - data/pathways/thioredoxin-pathway.yaml#references[114].title (EcoCyc:REG0-9024)
    (REG0-9024 -> Fis transcriptional repression of trxA (EcoCyc:REG0-9024))
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml#reactions[0].label
    (MetaCyc:RXN-21730) (RXN-21730 -> diphosphate-dependent D-sedoheptulose 7-phosphate
    1-phosphotransferase reaction)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml#reactions[1].label
    (MetaCyc:SEDOBISALDOL-RXN) (SEDOBISALDOL-RXN -> D-sedoheptulose 1,7-bisphosphate
    aldolase reaction)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml#reactions[2].label
    (MetaCyc:1TRANSKETO-RXN) (1TRANSKETO-RXN -> transketolase reaction (D-ribose 5-phosphate
    and D-xylulose 5-phosphate))
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml#reactions[3].label
    (MetaCyc:2TRANSKETO-RXN) (2TRANSKETO-RXN -> transketolase reaction (D-erythrose
    4-phosphate and D-xylulose 5-phosphate))
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml#reactions[4].label
    (MetaCyc:RIB5PISOM-RXN) (RIB5PISOM-RXN -> D-ribose 5-phosphate isomerase reaction)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml#reactions[5].label
    (MetaCyc:RIBULP3EPIM-RXN) (RIBULP3EPIM-RXN -> D-ribulose 5-phosphate 3-epimerase
    reaction)
  evidence_ids:
  - EV-C9S4-PREDECESSOR
  - EV-C9S4-WORKFLOW-EVIDENCE
  - EV-C9S5-THIOREDOX-AND-PWY8178-FIXED-2
  - EV-C9S5-RENDERED-PAGES-AND-KGX
  - EV-C9S5-QC
  - EV-C9S5-PYTEST
  rule_id: CURATION:no-raw-local-id-structured-reference-titles
  native_severity: minor
  normalization_reason: 'Native minor representation defect maps directly to minor
    severity: replacing the 11 raw unprefixed MetaCyc/EcoCyc frame-ID reference titles
    in MetaCyc:THIOREDOX-PWY and 6 raw unprefixed MetaCyc frame-ID reaction labels
    in MetaCyc:PWY-8178 eliminates all remaining raw database frame-ID reference titles
    (0 / 7,107) and reaction labels (0 / 1,633) across the 278-record corpus.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/thioredoxin-pathway.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
    role: maintained pathway YAML
  disposition_reason: 'Resolved under GitHub issue #771 (group G-C9S5-001) by replacing
    all 11 paired MetaCyc:*/EcoCyc:* structured references[] entries in MetaCyc:THIOREDOX-PWY
    and all 6 MetaCyc:* reactions[].label entries in MetaCyc:PWY-8178 carrying raw
    unprefixed database frame IDs with descriptive titles and reaction labels via
    pathwaymech.curation.publish_curation, recording 2 history/records/<slug>/2026-10-31T230500Z-antigravity-a1d1e5.yaml
    provenance entries, and regenerating pages/.'
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review
    finding_id: F-C9S4-002
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/771
  tags:
  - cycle9-stage5-resolve-review-findings
  - raw-frame-id-reference-title
  - reaction-label-hygiene
  - reference-hygiene
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-7255
  - MetaCyc:PWY0-1241
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:PWY-8178
  rationale: Retain all 5 remediated MetaCyc:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions with 0 raw database frame-ID reference titles
    and 0 raw database frame-ID reaction labels.
  evidence_ids:
  - EV-C9S5-RAW-TITLES-FIXED-3
  - EV-C9S5-THIOREDOX-AND-PWY8178-FIXED-2
  - EV-C9S5-QC
limitations:
- This Cycle 9 Stage 5 successor review is scoped to verifying the remediation of
  Cycle 9 Stage 4 findings F-C9S4-001 and F-C9S4-002 across the 5 affected maintained
  pathway records; the remaining 273 maintained records had zero findings in Cycle
  9 Stage 4 and were verified via repository-wide QC and pytest gates.
notes:
- CLAW aggregator CLI (kg_microbe_reviews) is not installed in the local culturebotai-claw
  environment; finding lineage (predecessor review_id 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review,
  finding_ids F-C9S4-001 and F-C9S4-002, exact issue_keys, 100% target_ids retention,
  and absence of competing heads) was explicitly verified against reviews/structured/.
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review
  relationship: resolves_findings_from
links:
- https://github.com/CultureBotAI/PathwayMech/issues/771
tags:
- mech-goal-sequence-20261019
- cycle-9
- stage-5
- resolve-review-findings
```
