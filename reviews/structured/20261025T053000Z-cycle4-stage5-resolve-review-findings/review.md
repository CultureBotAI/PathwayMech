# Cycle 4 Stage 5 Successor Review Resolving F-C4S4-001 and F-C4S4-002 Across 16 Maintained MetaCyc Pathway Records

- Review: 20261025T053000Z-cycle4-stage5-resolve-review-findings
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-25T05:16:00Z
- Finished UTC: 2026-10-25T05:30:00Z
- Reviewer: Antigravity (pathwaymech-resolve-reviews + review-yaml-category) (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Re-inspected and verified all 16 maintained MetaCyc:* pathway YAML records affected by Cycle 4 Stage 4 findings F-C4S4-001 (metacyc-argdegrad-pwy-stale-rhea10154-hydrogencarbonate-artifacts in MetaCyc:ARGDEGRAD-PWY, data/pathways/l-arginine-degradation-v.yaml) and F-C4S4-002 (metacyc-superseded-unreferenced-rhea-references-in-15-records across 15 additional MetaCyc:* pathway records) under GitHub issue #714. Remediated all 16 records via pathwaymech.curation.publish_curation: (1) in MetaCyc:ARGDEGRAD-PWY (l-arginine-degradation-v.yaml), updated description to reflect carbamate, ammonium, carbon dioxide, and ATP and spontaneous carbamate decarboxylation, removed orphan participant CHEBI:17544 (hydrogencarbonate, 0 incident edges), removed unreferenced superseded RHEA:10154 from references[], and replaced the 4 generic 'RHEA:&lt;ID&gt; authority record' titles on RHEA:30757, RHEA:15650, RHEA:19597, and RHEA:19513 with descriptive Rhea reaction direction titles; and (2) across the 15 MetaCyc:* records in F-C4S4-002, removed all 28 unreferenced superseded RHEA:* entries from references[] and replaced all 29 generic 'RHEA:&lt;ID&gt; authority record' placeholder titles with descriptive Rhea reaction direction titles. Recorded 16 append-only curation history files at history/records/&lt;slug&gt;/2026-10-25T052500Z-antigravity-a1d1e5.yaml, regenerated rendered pages and KGX exports (.venv/bin/pathwaymech-render-pages), and confirmed 100% participant connectivity across all 322 participant entries in the 16 reassessed MetaCyc:* records (0 orphan participants; 7,762 total participant entries across the 273-record corpus), 0 unreferenced RHEA:* entries across all 203 reference entries in the 16 reassessed MetaCyc:* records (7,053 total reference entries across the 273-record corpus), 0 generic 'RHEA:&lt;ID&gt; authority record' placeholder titles across the 16 reassessed records, and full pass across QC (273 pathway records, 859 history records, 22,533 evidence blocks, 33 source records) and pytest (190 passed).

## Scope And Provenance

Complete post-remediation reassessment of the 16 maintained MetaCyc:* pathway records in data/pathways/*.yaml that carried open findings (F-C4S4-001 and F-C4S4-002) in Cycle 4 Stage 4 review 20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review.

Selection: All 16 maintained pathway records in CultureBotAI/PathwayMech carrying open findings in reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.yaml (100% of open Cycle 4 Stage 4 maintained-record findings).
Coverage: full; 16 reviewed / 16 in the declared population.
Source: working_tree at Git base 2d84c7ec416d319bb3755d1fd5d04b32d6142f53.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:ARGDEGRAD-PWY | data/pathways/l-arginine-degradation-v.yaml | maintained | L-arginine degradation V (arginine deiminase pathway) (MetaCyc:ARGDEGRAD-PWY) |
| MetaCyc:DARABCAT-PWY | data/pathways/d-arabinose-degradation-i.yaml | maintained | D-arabinose degradation I (MetaCyc:DARABCAT-PWY) |
| MetaCyc:GALACTUROCAT-PWY | data/pathways/d-galacturonate-degradation-i.yaml | maintained | D-galacturonate degradation I (MetaCyc:GALACTUROCAT-PWY) |
| MetaCyc:GLUCARDEG-PWY | data/pathways/d-glucarate-degradation-i.yaml | maintained | D-glucarate degradation I (MetaCyc:GLUCARDEG-PWY) |
| MetaCyc:XYLCAT-PWY | data/pathways/d-xylose-degradation-i.yaml | maintained | D-xylose degradation I (MetaCyc:XYLCAT-PWY) |
| MetaCyc:GLYCEROLMETAB-PWY | data/pathways/glycerol-degradation-v.yaml | maintained | glycerol degradation V (MetaCyc:GLYCEROLMETAB-PWY) |
| MetaCyc:PWY-6124 | data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml | maintained | inosine-5'-phosphate biosynthesis II (MetaCyc:PWY-6124) |
| MetaCyc:ARABCAT-PWY | data/pathways/l-arabinose-degradation-i.yaml | maintained | L-arabinose degradation I (MetaCyc:ARABCAT-PWY) |
| MetaCyc:FUCCAT-PWY | data/pathways/l-fucose-degradation-i.yaml | maintained | L-fucose degradation I (MetaCyc:FUCCAT-PWY) |
| MetaCyc:ILEUSYN-PWY | data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml | maintained | L-isoleucine biosynthesis I (from threonine) (MetaCyc:ILEUSYN-PWY) |
| MetaCyc:LEUSYN-PWY | data/pathways/l-leucine-biosynthesis.yaml | maintained | L-leucine biosynthesis (MetaCyc:LEUSYN-PWY) |
| MetaCyc:HOMOSER-METSYN-PWY | data/pathways/l-methionine-biosynthesis-i.yaml | maintained | L-methionine biosynthesis I (MetaCyc:HOMOSER-METSYN-PWY) |
| MetaCyc:RHAMCAT-PWY | data/pathways/l-rhamnose-degradation-i.yaml | maintained | L-rhamnose degradation I (MetaCyc:RHAMCAT-PWY) |
| MetaCyc:TRPSYN-PWY | data/pathways/l-tryptophan-biosynthesis.yaml | maintained | L-tryptophan biosynthesis (MetaCyc:TRPSYN-PWY) |
| MetaCyc:GLUAMCAT-PWY | data/pathways/n-acetylglucosamine-degradation-i.yaml | maintained | N-acetylglucosamine degradation I (MetaCyc:GLUAMCAT-PWY) |
| MetaCyc:NONOXIPENT-PWY | data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml | maintained | pentose phosphate pathway (non-oxidative branch) I (MetaCyc:NONOXIPENT-PWY) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Repository QC and closed-schema validation (just validate) | passed | True | MetaCyc:ARGDEGRAD-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:NONOXIPENT-PWY | Validated all 273 maintained pathway records (including the 16 remediated MetaCyc:* records) against the closed LinkML schema, local identifier/label authority snapshots, 859 history records, 22,533 evidence blocks, 33 source records, and pages/ synchrony. |
| Pytest unit and integration test suite (just test) | passed | True | MetaCyc:ARGDEGRAD-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:NONOXIPENT-PWY | All 190 tests passed in pytest across schema, KGX export, SSSOM, and record-review checks. |
| Ruff lint check (just lint) | passed | True | MetaCyc:ARGDEGRAD-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:NONOXIPENT-PWY | Ruff check passed with 0 errors. |
| Git whitespace and conflict marker check | passed | True | MetaCyc:ARGDEGRAD-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:NONOXIPENT-PWY | git diff --check exited 0 with no whitespace or conflict marker issues. |
| Structured review bundle contract check (just review-check) | passed | True | MetaCyc:ARGDEGRAD-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:NONOXIPENT-PWY | All 205 retained structured review bundles in reviews/structured/ passed schema and append-only checks against main. |

## Scientific And Domain Assessments

### Post-remediation participant connectivity (0 orphan participants), RHEA reference usage (0 unreferenced RHEA:* references), and descriptive RHEA reference titles across all 16 reassessed MetaCyc:* pathway records

consistency: supported. Targets: MetaCyc:ARGDEGRAD-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:NONOXIPENT-PWY.

Removing orphan participant CHEBI:17544 (hydrogencarbonate) and unreferenced RHEA:10154 from MetaCyc:ARGDEGRAD-PWY (l-arginine-degradation-v.yaml), pruning all 28 unreferenced superseded RHEA:* references across the 15 F-C4S4-002 MetaCyc:* records, and replacing all 33 generic 'RHEA:&lt;ID&gt; authority record' placeholder titles across all 16 reassessed MetaCyc:* records brings participant connectivity across the 16 reassessed records to 100% (322 / 322 participant entries connected to at least one mechanistic_edge; 7,762 total participant entries across the 273-record corpus) and eliminates all unreferenced RHEA:* references (0 / 203 reference entries across the 16 reassessed records; 7,053 total reference entries across the 273-record corpus) and placeholder RHEA titles across the 16 reassessed records.

### Preservation of pathway identity, taxon grounding, reaction directionality, stoichiometry, and edge-level evidence across the 16 remediated MetaCyc:* pathway records

evidence: supported. Targets: MetaCyc:ARGDEGRAD-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:NONOXIPENT-PWY.

Structural verification across all 16 remediated MetaCyc:* YAML files confirms that all pathway IDs, taxon groundings, active participant CURIEs, reaction directions, step definitions, mechanistic_edges, source_mappings, and structured evidence blocks (22,533 total evidence blocks) remain 100% intact and pass closed LinkML and authority snapshot checks.

## Findings

### F-C4S4-001: MetaCyc:ARGDEGRAD-PWY (l-arginine-degradation-v.yaml) stale hydrogencarbonate description, orphan CHEBI:17544 participant, unreferenced RHEA:10154 reference, and 4 generic RHEA authority titles are resolved

minor / resolved / confirmed; issue key: metacyc-argdegrad-pwy-stale-rhea10154-hydrogencarbonate-artifacts.

In MetaCyc:ARGDEGRAD-PWY (data/pathways/l-arginine-degradation-v.yaml), updated description to replace superseded 'hydrogencarbonate' wording with 'carbamate, ammonium, carbon dioxide, and ATP' and 'spontaneous carbamate decarboxylation', removed orphan participant CHEBI:17544 (hydrogencarbonate, 0 incident edges), removed unreferenced superseded RHEA:10154 from references[], and replaced generic 'RHEA:&lt;ID&gt; authority record' placeholder titles on RHEA:30757, RHEA:15650, RHEA:19597, and RHEA:19513 (now at references[4..7]) with descriptive Rhea reaction direction titles via pathwaymech.curation.publish_curation, recorded history/records/l-arginine-degradation-v/2026-10-25T052500Z-antigravity-a1d1e5.yaml, and regenerated pages/.

Disposition: Resolved under GitHub issue #714 by updating description, removing orphan participant CHEBI:17544 and unreferenced RHEA:10154, and replacing the 4 generic RHEA authority titles on RHEA:30757, RHEA:15650, RHEA:19597, and RHEA:19513 in data/pathways/l-arginine-degradation-v.yaml via pathwaymech.curation.publish_curation, recording history/records/l-arginine-degradation-v/2026-10-25T052500Z-antigravity-a1d1e5.yaml, and regenerating pages/.

### F-C4S4-002: All 28 unreferenced superseded RHEA:* entries are removed and all 29 generic 'RHEA:&lt;ID&gt; authority record' titles are replaced across 15 maintained MetaCyc pathway records

minor / resolved / confirmed; issue key: metacyc-superseded-unreferenced-rhea-references-in-15-records.

Across all 15 maintained MetaCyc:* pathway records in F-C4S4-002 (MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, and MetaCyc:NONOXIPENT-PWY), removed all 28 unreferenced superseded RHEA:* entries from references[] and replaced all 29 generic 'RHEA:&lt;ID&gt; authority record' placeholder titles with descriptive Rhea reaction direction titles via pathwaymech.curation.publish_curation, recorded 15 history/records/&lt;slug&gt;/2026-10-25T052500Z-antigravity-a1d1e5.yaml files, and regenerated pages/.

Disposition: Resolved under GitHub issue #714 by removing all 28 unreferenced superseded RHEA:* entries from references[] and replacing all 29 generic 'RHEA:&lt;ID&gt; authority record' placeholder titles with descriptive Rhea reaction direction titles across the 15 affected MetaCyc:* pathway records via pathwaymech.curation.publish_curation, recording 15 history/records/&lt;slug&gt;/2026-10-25T052500Z-antigravity-a1d1e5.yaml provenance entries, and regenerating pages/.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: MetaCyc:ARGDEGRAD-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:NONOXIPENT-PWY. Retain all 16 remediated MetaCyc:* pathway records as distinct, non-duplicate source-scoped pathway definitions with 100% connected participants and clean, descriptive RHEA:* reference metadata.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EV-C4S4-PREDECESSOR | reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.yaml; findings[0] (F-C4S4-001) and findings[1] (F-C4S4-002) | supports | Predecessor Cycle 4 Stage 4 cohort review recorded two minor open findings across 16 maintained MetaCyc:* pathway records: F-C4S4-001 (metacyc-argdegrad-pwy-stale-rhea10154-hydrogencarbonate-artifacts in MetaCyc:ARGDEGRAD-PWY) and F-C4S4-002 (metacyc-superseded-unreferenced-rhea-references-in-15-records across 15 additional MetaCyc:* records). |
| EV-C4S4-WORKFLOW-EVIDENCE | reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml; findings[0..1] (F-C4S4-001, F-C4S4-002) | supports | Cycle 4 Stage 4 workflow evidence manifest carried forward F-C4S4-001 and F-C4S4-002 as open findings for Cycle 4 Stage 5 grouped remediation. |
| EV-C4S5-ARGDEGRAD-FIXED | data/pathways/l-arginine-degradation-v.yaml; description (lines 3-5), participants[0..17] (lines 11-64), and references[4..7] (RHEA:30757, RHEA:15650, RHEA:19597, RHEA:19513 at lines 345-360) | supports | In data/pathways/l-arginine-degradation-v.yaml (MetaCyc:ARGDEGRAD-PWY), updated description to list carbamate, ammonium, carbon dioxide, and ATP and spontaneous carbamate decarboxylation, removed orphan participant CHEBI:17544 (hydrogencarbonate), removed unreferenced superseded reference RHEA:10154, and replaced generic 'RHEA:&lt;ID&gt; authority record' titles on RHEA:30757, RHEA:15650, RHEA:19597, and RHEA:19513 (now at references[4..7]) with descriptive reaction direction titles. |
| EV-C4S5-RHEA-REFS-FIXED-15 | data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml; references[6..10] (RHEA:14659, RHEA:13678, RHEA:10510, RHEA:17054, RHEA:27627 at lines 569-588) and references[] across all 15 F-C4S4-002 MetaCyc:* records | supports | Across all 15 MetaCyc:* pathway records in F-C4S4-002, removed all 28 unreferenced superseded RHEA:* entries from references[] and replaced all 29 generic 'RHEA:&lt;ID&gt; authority record' placeholder titles with descriptive Rhea reaction direction titles via pathwaymech.curation.publish_curation. |
| EV-C4S5-RENDERED-PAGES-AND-KGX | pages/records/MetaCyc_ARGDEGRAD-PWY.html; Rendered HTML reference table in pages/records/MetaCyc_ARGDEGRAD-PWY.html and KGX exports pages/downloads/{nodes.tsv,edges.tsv} | supports | After running .venv/bin/pathwaymech-render-pages, verified that pages/records/MetaCyc_ARGDEGRAD-PWY.html and pages/downloads/{nodes.tsv,edges.tsv} no longer include orphan participant CHEBI:17544 or unreferenced RHEA:10154, and all 16 remediated MetaCyc:* record pages render descriptive Rhea reaction direction titles. |
| EV-C4S5-QC | .venv/bin/pathwaymech-run-qc; stdout summary (273 pathway records, 859 history records, 22,533 evidence blocks, 33 source records) | supports | Executed .venv/bin/pathwaymech-run-qc: validated 273 pathway records against the closed LinkML schema, verified all identifiers and labels against local authority snapshots, validated 859 history records (including 16 new Cycle 4 Stage 5 record history entries referencing issue #714) and 22,533 evidence blocks, and confirmed pages/ synchrony. |
| EV-C4S5-PYTEST | .venv/bin/pytest -q; pytest suite execution across tests/ | supports | Executed .venv/bin/pytest -q with 190 passed. |
| EV-C4S5-RUFF | .venv/bin/ruff check --no-cache .; ruff check output | supports | Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks passed). |
| EV-C4S5-GIT-DIFF | git diff --check; git worktree on feat/cycle4-stage5-resolve-review-findings | supports | Executed git diff --check with exit code 0; no whitespace errors or conflict markers. |
| EV-C4S5-REVIEW-CHECK | .venv/bin/python scripts/record_review.py check --base main; reviews/structured/ | supports | Validated all 205 retained structured review bundles in reviews/structured/ against schema/record_review.yaml and verified byte-for-byte append-only preservation against main. |

## Limits And Additional Notes

- This Cycle 4 Stage 5 successor review is scoped to verifying the remediation of Cycle 4 Stage 4 findings F-C4S4-001 and F-C4S4-002 across the 16 affected maintained MetaCyc:* pathway records; the remaining 257 maintained records had zero findings in Cycle 4 Stage 4 and were verified via repository-wide QC and pytest gates.
- CLAW aggregator CLI (kg_microbe_reviews) is not installed in the local culturebotai-claw environment; finding lineage (predecessor review_id 20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review, finding_ids F-C4S4-001 and F-C4S4-002, exact issue_keys, 100% target_ids retention, and absence of competing heads) was explicitly verified against reviews/structured/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T053000Z-cycle4-stage5-resolve-review-findings
kind: batch
repository: CultureBotAI/PathwayMech
title: Cycle 4 Stage 5 Successor Review Resolving F-C4S4-001 and F-C4S4-002 Across
  16 Maintained MetaCyc Pathway Records
started_at: '2026-10-25T05:16:00Z'
finished_at: '2026-10-25T05:30:00Z'
reviewer:
  identity: Antigravity (pathwaymech-resolve-reviews + review-yaml-category)
  kind: agent
  model: Claude Opus 4.6 (Thinking)
  independence: self_review
  independence_basis: 'Same agent session (a1d1e545-faee-4294-8a87-4c2d031a6538) implemented
    the Cycle 4 Stage 5 curation fixes for GitHub issue #714 and verified post-remediation
    records, rendered HTML pages, and KGX exports.'
skill: pathwaymech-resolve-reviews
completion: completed
verdict: pass
native_verdict: coherent
scientific_review: true
summary: 'Re-inspected and verified all 16 maintained MetaCyc:* pathway YAML records
  affected by Cycle 4 Stage 4 findings F-C4S4-001 (metacyc-argdegrad-pwy-stale-rhea10154-hydrogencarbonate-artifacts
  in MetaCyc:ARGDEGRAD-PWY, data/pathways/l-arginine-degradation-v.yaml) and F-C4S4-002
  (metacyc-superseded-unreferenced-rhea-references-in-15-records across 15 additional
  MetaCyc:* pathway records) under GitHub issue #714. Remediated all 16 records via
  pathwaymech.curation.publish_curation: (1) in MetaCyc:ARGDEGRAD-PWY (l-arginine-degradation-v.yaml),
  updated description to reflect carbamate, ammonium, carbon dioxide, and ATP and
  spontaneous carbamate decarboxylation, removed orphan participant CHEBI:17544 (hydrogencarbonate,
  0 incident edges), removed unreferenced superseded RHEA:10154 from references[],
  and replaced the 4 generic ''RHEA:<ID> authority record'' titles on RHEA:30757,
  RHEA:15650, RHEA:19597, and RHEA:19513 with descriptive Rhea reaction direction
  titles; and (2) across the 15 MetaCyc:* records in F-C4S4-002, removed all 28 unreferenced
  superseded RHEA:* entries from references[] and replaced all 29 generic ''RHEA:<ID>
  authority record'' placeholder titles with descriptive Rhea reaction direction titles.
  Recorded 16 append-only curation history files at history/records/<slug>/2026-10-25T052500Z-antigravity-a1d1e5.yaml,
  regenerated rendered pages and KGX exports (.venv/bin/pathwaymech-render-pages),
  and confirmed 100% participant connectivity across all 322 participant entries in
  the 16 reassessed MetaCyc:* records (0 orphan participants; 7,762 total participant
  entries across the 273-record corpus), 0 unreferenced RHEA:* entries across all
  203 reference entries in the 16 reassessed MetaCyc:* records (7,053 total reference
  entries across the 273-record corpus), 0 generic ''RHEA:<ID> authority record''
  placeholder titles across the 16 reassessed records, and full pass across QC (273
  pathway records, 859 history records, 22,533 evidence blocks, 33 source records)
  and pytest (190 passed).'
source:
  git_revision: 2d84c7ec416d319bb3755d1fd5d04b32d6142f53
  state: working_tree
  inputs:
  - path: .claude/skills/pathwaymech-resolve-reviews/SKILL.md
    sha256: 3d3b9d3b9e56cc782cf4ff63d491c5b589e9bdcde71438a695384b228edc4aea
    role: context
  - path: data/pathways/d-arabinose-degradation-i.yaml
    sha256: 0bf9ffd31ebe2fcd98a34b8b9de8d87aa4d2ca009c03067a507a1c52a3fcb3dc
    role: target
  - path: data/pathways/d-galacturonate-degradation-i.yaml
    sha256: bcba6b22043e2476b3becc03472ac7fcd95287ca643ec5d561404982fedf59db
    role: target
  - path: data/pathways/d-glucarate-degradation-i.yaml
    sha256: 7a16ccac6f89910cc214a8660964ab093c36ee9ebec9599abd8f67fbe89c40ac
    role: target
  - path: data/pathways/d-xylose-degradation-i.yaml
    sha256: dcea294990af98ec62667a1432f4970279eae2758776a8d27447e0860c237df4
    role: target
  - path: data/pathways/glycerol-degradation-v.yaml
    sha256: a8e36da3e055cd299c7501923fc54324c46882cd13d32314c30af8a23d7c9aea
    role: target
  - path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    sha256: e329c6b7bd73e7a033d279f667dd8519940127725a1abfe0184f5b96421bc289
    role: target
  - path: data/pathways/l-arabinose-degradation-i.yaml
    sha256: e3c1a570eb11080fb319921e3ae7cc49a6eb5b63d2b222c386f46049da2740a3
    role: target
  - path: data/pathways/l-arginine-degradation-v.yaml
    sha256: dd64f61f00b3602301ca583f72958783a994b4b2700a83dcfe6698d9fefa8070
    role: target
  - path: data/pathways/l-fucose-degradation-i.yaml
    sha256: 6335ac444b2f78b24d76b1f5d13a688bc659111ead39bca0c197b8f4f5d6d30e
    role: target
  - path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
    sha256: eeb3fb3becfca15fb139f6b784af05420fd7792f4bd7c7abdf75160b8d4d1d48
    role: target
  - path: data/pathways/l-leucine-biosynthesis.yaml
    sha256: 502da5c5afe05a3b596e2d2aa7aa4135b5a29b30a4273612130934cb5bfa1b7f
    role: target
  - path: data/pathways/l-methionine-biosynthesis-i.yaml
    sha256: 1e8cfbfc2ebeae0c6021245852c4c7b1df9368d25e97aaaaff70b3c76f020967
    role: target
  - path: data/pathways/l-rhamnose-degradation-i.yaml
    sha256: 897aea0cfa173a17407528ed614d4ac95f8c393c12c8efb213bb54f026eb821f
    role: target
  - path: data/pathways/l-tryptophan-biosynthesis.yaml
    sha256: 98ebda2da2e8cb992fe206721bea2befa828f8d579be49dd2890b5472e58056a
    role: target
  - path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    sha256: b568c61ee2bc7aa28f57cbde507cad7124184ad397be7ca8d02b44e402bd3739
    role: target
  - path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    sha256: ed22c55ef88a108b0b993196b06b3f0a487ba2c2f4b3e742c1f1cd811eb14370
    role: target
  - path: pages/downloads/nodes.tsv
    sha256: b5b5f87e0988813689c7880fc6db87e73be8289e9a9e285053bc7bb7991d84c5
    role: context
  - path: pages/downloads/edges.tsv
    sha256: 6b546fdb693a6cdd9248a4fd4ceb132bdd78cdbbf555474979f637083ccb2333
    role: context
  - path: pages/records/MetaCyc_ARGDEGRAD-PWY.html
    sha256: 03cb07b8a17a769f57bd5fbee08d9c26bd5285a907a718c1ee4578a9b887e96e
    role: context
  - path: reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.yaml
    sha256: 9ebc4024c30fe57826545bfdf98cbad38579f8f529ec477a2c715f276a282605
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml
    sha256: 4b256861b32dfe39f02c93dee87ce3805b444ad7749ffa499fba242a2de0c062
    role: context
scope:
  description: Complete post-remediation reassessment of the 16 maintained MetaCyc:*
    pathway records in data/pathways/*.yaml that carried open findings (F-C4S4-001
    and F-C4S4-002) in Cycle 4 Stage 4 review 20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review.
  selection: All 16 maintained pathway records in CultureBotAI/PathwayMech carrying
    open findings in reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.yaml
    (100% of open Cycle 4 Stage 4 maintained-record findings).
  coverage: full
  population_size: 16
  reviewed_target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  exclusions:
  - target: Remaining 257 maintained pathway records in data/pathways/*.yaml
    reason: Assessed with zero open findings in Cycle 4 Stage 4 review 20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review
      and unchanged in Cycle 4 Stage 5.
  - target: research/pathway_additions/*.yaml (6 withheld staging drafts)
    reason: Non-maintained research staging drafts outside data/pathways/*.yaml; their
      2 historical open findings (F01 in 20261010T090124Z-siroheme-pathway-addition-blocked-review
      and F1 in 20261010T100956Z-ecoli-14dhna-octaprenyl-draft-review) remain untouched.
targets:
- target_id: MetaCyc:ARGDEGRAD-PWY
  path: data/pathways/l-arginine-degradation-v.yaml
  label: L-arginine degradation V (arginine deiminase pathway) (MetaCyc:ARGDEGRAD-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: dd64f61f00b3602301ca583f72958783a994b4b2700a83dcfe6698d9fefa8070
    description: 'Raw SHA-256 file digest of data/pathways/l-arginine-degradation-v.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-v.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:DARABCAT-PWY
  path: data/pathways/d-arabinose-degradation-i.yaml
  label: D-arabinose degradation I (MetaCyc:DARABCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0bf9ffd31ebe2fcd98a34b8b9de8d87aa4d2ca009c03067a507a1c52a3fcb3dc
    description: 'Raw SHA-256 file digest of data/pathways/d-arabinose-degradation-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-arabinose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GALACTUROCAT-PWY
  path: data/pathways/d-galacturonate-degradation-i.yaml
  label: D-galacturonate degradation I (MetaCyc:GALACTUROCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bcba6b22043e2476b3becc03472ac7fcd95287ca643ec5d561404982fedf59db
    description: 'Raw SHA-256 file digest of data/pathways/d-galacturonate-degradation-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galacturonate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLUCARDEG-PWY
  path: data/pathways/d-glucarate-degradation-i.yaml
  label: D-glucarate degradation I (MetaCyc:GLUCARDEG-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7a16ccac6f89910cc214a8660964ab093c36ee9ebec9599abd8f67fbe89c40ac
    description: 'Raw SHA-256 file digest of data/pathways/d-glucarate-degradation-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-glucarate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:XYLCAT-PWY
  path: data/pathways/d-xylose-degradation-i.yaml
  label: D-xylose degradation I (MetaCyc:XYLCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: dcea294990af98ec62667a1432f4970279eae2758776a8d27447e0860c237df4
    description: 'Raw SHA-256 file digest of data/pathways/d-xylose-degradation-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-xylose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLYCEROLMETAB-PWY
  path: data/pathways/glycerol-degradation-v.yaml
  label: glycerol degradation V (MetaCyc:GLYCEROLMETAB-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a8e36da3e055cd299c7501923fc54324c46882cd13d32314c30af8a23d7c9aea
    description: 'Raw SHA-256 file digest of data/pathways/glycerol-degradation-v.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycerol-degradation-v.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6124
  path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
  label: inosine-5'-phosphate biosynthesis II (MetaCyc:PWY-6124)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e329c6b7bd73e7a033d279f667dd8519940127725a1abfe0184f5b96421bc289
    description: 'Raw SHA-256 file digest of data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ARABCAT-PWY
  path: data/pathways/l-arabinose-degradation-i.yaml
  label: L-arabinose degradation I (MetaCyc:ARABCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e3c1a570eb11080fb319921e3ae7cc49a6eb5b63d2b222c386f46049da2740a3
    description: 'Raw SHA-256 file digest of data/pathways/l-arabinose-degradation-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arabinose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:FUCCAT-PWY
  path: data/pathways/l-fucose-degradation-i.yaml
  label: L-fucose degradation I (MetaCyc:FUCCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6335ac444b2f78b24d76b1f5d13a688bc659111ead39bca0c197b8f4f5d6d30e
    description: 'Raw SHA-256 file digest of data/pathways/l-fucose-degradation-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-fucose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ILEUSYN-PWY
  path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
  label: L-isoleucine biosynthesis I (from threonine) (MetaCyc:ILEUSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: eeb3fb3becfca15fb139f6b784af05420fd7792f4bd7c7abdf75160b8d4d1d48
    description: 'Raw SHA-256 file digest of data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:LEUSYN-PWY
  path: data/pathways/l-leucine-biosynthesis.yaml
  label: L-leucine biosynthesis (MetaCyc:LEUSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 502da5c5afe05a3b596e2d2aa7aa4135b5a29b30a4273612130934cb5bfa1b7f
    description: 'Raw SHA-256 file digest of data/pathways/l-leucine-biosynthesis.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-leucine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:HOMOSER-METSYN-PWY
  path: data/pathways/l-methionine-biosynthesis-i.yaml
  label: L-methionine biosynthesis I (MetaCyc:HOMOSER-METSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1e8cfbfc2ebeae0c6021245852c4c7b1df9368d25e97aaaaff70b3c76f020967
    description: 'Raw SHA-256 file digest of data/pathways/l-methionine-biosynthesis-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-methionine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:RHAMCAT-PWY
  path: data/pathways/l-rhamnose-degradation-i.yaml
  label: L-rhamnose degradation I (MetaCyc:RHAMCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 897aea0cfa173a17407528ed614d4ac95f8c393c12c8efb213bb54f026eb821f
    description: 'Raw SHA-256 file digest of data/pathways/l-rhamnose-degradation-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-rhamnose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:TRPSYN-PWY
  path: data/pathways/l-tryptophan-biosynthesis.yaml
  label: L-tryptophan biosynthesis (MetaCyc:TRPSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 98ebda2da2e8cb992fe206721bea2befa828f8d579be49dd2890b5472e58056a
    description: 'Raw SHA-256 file digest of data/pathways/l-tryptophan-biosynthesis.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tryptophan-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLUAMCAT-PWY
  path: data/pathways/n-acetylglucosamine-degradation-i.yaml
  label: N-acetylglucosamine degradation I (MetaCyc:GLUAMCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b568c61ee2bc7aa28f57cbde507cad7124184ad397be7ca8d02b44e402bd3739
    description: 'Raw SHA-256 file digest of data/pathways/n-acetylglucosamine-degradation-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:NONOXIPENT-PWY
  path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
  label: pentose phosphate pathway (non-oxidative branch) I (MetaCyc:NONOXIPENT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ed22c55ef88a108b0b993196b06b3f0a487ba2c2f4b3e742c1f1cd811eb14370
    description: 'Raw SHA-256 file digest of data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
      in Cycle 4 Stage 5 (issue #714).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    role: maintained pathway YAML
checks:
- check_id: validate
  name: Repository QC and closed-schema validation (just validate)
  status: passed
  required: true
  summary: Validated all 273 maintained pathway records (including the 16 remediated
    MetaCyc:* records) against the closed LinkML schema, local identifier/label authority
    snapshots, 859 history records, 22,533 evidence blocks, 33 source records, and
    pages/ synchrony.
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  command: .venv/bin/pathwaymech-run-qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C4S5-QC
  scope_note: 'Full-repository QC gate after applying issue #714 fixes and regenerating
    pages/.'
- check_id: test
  name: Pytest unit and integration test suite (just test)
  status: passed
  required: true
  summary: All 190 tests passed in pytest across schema, KGX export, SSSOM, and record-review
    checks.
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  command: .venv/bin/pytest -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C4S5-PYTEST
  scope_note: Full pytest test suite (190 passed).
- check_id: lint
  name: Ruff lint check (just lint)
  status: passed
  required: true
  summary: Ruff check passed with 0 errors.
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  command: .venv/bin/ruff check --no-cache .
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C4S5-RUFF
  scope_note: Repository-wide Python lint check.
- check_id: git-diff-check
  name: Git whitespace and conflict marker check
  status: passed
  required: true
  summary: git diff --check exited 0 with no whitespace or conflict marker issues.
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C4S5-GIT-DIFF
  scope_note: Worktree diff check across all Cycle 4 Stage 5 edits.
- check_id: review-check
  name: Structured review bundle contract check (just review-check)
  status: passed
  required: true
  summary: All 205 retained structured review bundles in reviews/structured/ passed
    schema and append-only checks against main.
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  command: .venv/bin/python scripts/record_review.py check --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C4S5-REVIEW-CHECK
  scope_note: Verifies append-only immutability of prior 204 bundles and validity
    of current bundle.
evidence:
- evidence_id: EV-C4S4-PREDECESSOR
  kind: prior_review
  reference: reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.yaml
  locator: findings[0] (F-C4S4-001) and findings[1] (F-C4S4-002)
  accessed_at: '2026-10-25T05:16:00Z'
  support: supports
  summary: 'Predecessor Cycle 4 Stage 4 cohort review recorded two minor open findings
    across 16 maintained MetaCyc:* pathway records: F-C4S4-001 (metacyc-argdegrad-pwy-stale-rhea10154-hydrogencarbonate-artifacts
    in MetaCyc:ARGDEGRAD-PWY) and F-C4S4-002 (metacyc-superseded-unreferenced-rhea-references-in-15-records
    across 15 additional MetaCyc:* records).'
  snapshot_sha256: 9ebc4024c30fe57826545bfdf98cbad38579f8f529ec477a2c715f276a282605
- evidence_id: EV-C4S4-WORKFLOW-EVIDENCE
  kind: prior_review
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml
  locator: findings[0..1] (F-C4S4-001, F-C4S4-002)
  accessed_at: '2026-10-25T05:16:00Z'
  support: supports
  summary: Cycle 4 Stage 4 workflow evidence manifest carried forward F-C4S4-001 and
    F-C4S4-002 as open findings for Cycle 4 Stage 5 grouped remediation.
  snapshot_sha256: 4b256861b32dfe39f02c93dee87ce3805b444ad7749ffa499fba242a2de0c062
- evidence_id: EV-C4S5-ARGDEGRAD-FIXED
  kind: record_content
  reference: data/pathways/l-arginine-degradation-v.yaml
  locator: description (lines 3-5), participants[0..17] (lines 11-64), and references[4..7]
    (RHEA:30757, RHEA:15650, RHEA:19597, RHEA:19513 at lines 345-360)
  accessed_at: '2026-10-25T05:27:00Z'
  support: supports
  summary: In data/pathways/l-arginine-degradation-v.yaml (MetaCyc:ARGDEGRAD-PWY),
    updated description to list carbamate, ammonium, carbon dioxide, and ATP and spontaneous
    carbamate decarboxylation, removed orphan participant CHEBI:17544 (hydrogencarbonate),
    removed unreferenced superseded reference RHEA:10154, and replaced generic 'RHEA:<ID>
    authority record' titles on RHEA:30757, RHEA:15650, RHEA:19597, and RHEA:19513
    (now at references[4..7]) with descriptive reaction direction titles.
  quote: "description: L-arginine degradation through the arginine deiminase pathway\
    \ converts L-arginine to L-citrulline,\n  L-ornithine, carbamate, ammonium, carbon\
    \ dioxide, and ATP through arginine deiminase, catabolic ornithine\n  carbamoyltransferase,\
    \ carbamate kinase, and spontaneous carbamate decarboxylation."
  snapshot_sha256: dd64f61f00b3602301ca583f72958783a994b4b2700a83dcfe6698d9fefa8070
- evidence_id: EV-C4S5-RHEA-REFS-FIXED-15
  kind: record_content
  reference: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
  locator: references[6..10] (RHEA:14659, RHEA:13678, RHEA:10510, RHEA:17054, RHEA:27627
    at lines 569-588) and references[] across all 15 F-C4S4-002 MetaCyc:* records
  accessed_at: '2026-10-25T05:27:00Z'
  support: supports
  summary: Across all 15 MetaCyc:* pathway records in F-C4S4-002, removed all 28 unreferenced
    superseded RHEA:* entries from references[] and replaced all 29 generic 'RHEA:<ID>
    authority record' placeholder titles with descriptive Rhea reaction direction
    titles via pathwaymech.curation.publish_curation.
  quote: "- id: RHEA:14659\n  title: Rhea aldehydo-D-ribose-5-phosphate-forming ribose-5-phosphate\
    \ isomerase direction\n  url: https://www.rhea-db.org/rhea/14659\n  source_version:\
    \ '139'\n- id: RHEA:13678\n  title: Rhea D-xylulose-5-phosphate-forming ribulose-phosphate\
    \ 3-epimerase direction"
  snapshot_sha256: ed22c55ef88a108b0b993196b06b3f0a487ba2c2f4b3e742c1f1cd811eb14370
- evidence_id: EV-C4S5-RENDERED-PAGES-AND-KGX
  kind: record_content
  reference: pages/records/MetaCyc_ARGDEGRAD-PWY.html
  locator: Rendered HTML reference table in pages/records/MetaCyc_ARGDEGRAD-PWY.html
    and KGX exports pages/downloads/{nodes.tsv,edges.tsv}
  accessed_at: '2026-10-25T05:29:00Z'
  support: supports
  summary: After running .venv/bin/pathwaymech-render-pages, verified that pages/records/MetaCyc_ARGDEGRAD-PWY.html
    and pages/downloads/{nodes.tsv,edges.tsv} no longer include orphan participant
    CHEBI:17544 or unreferenced RHEA:10154, and all 16 remediated MetaCyc:* record
    pages render descriptive Rhea reaction direction titles.
  quote: Rhea carbamate- and ATP-forming carbamate kinase direction
  snapshot_sha256: 03cb07b8a17a769f57bd5fbee08d9c26bd5285a907a718c1ee4578a9b887e96e
- evidence_id: EV-C4S5-QC
  kind: validation
  reference: .venv/bin/pathwaymech-run-qc
  locator: stdout summary (273 pathway records, 859 history records, 22,533 evidence
    blocks, 33 source records)
  accessed_at: '2026-10-25T05:30:00Z'
  support: supports
  summary: 'Executed .venv/bin/pathwaymech-run-qc: validated 273 pathway records against
    the closed LinkML schema, verified all identifiers and labels against local authority
    snapshots, validated 859 history records (including 16 new Cycle 4 Stage 5 record
    history entries referencing issue #714) and 22,533 evidence blocks, and confirmed
    pages/ synchrony.'
- evidence_id: EV-C4S5-PYTEST
  kind: validation
  reference: .venv/bin/pytest -q
  locator: pytest suite execution across tests/
  accessed_at: '2026-10-25T05:30:00Z'
  support: supports
  summary: Executed .venv/bin/pytest -q with 190 passed.
- evidence_id: EV-C4S5-RUFF
  kind: validation
  reference: .venv/bin/ruff check --no-cache .
  locator: ruff check output
  accessed_at: '2026-10-25T05:30:00Z'
  support: supports
  summary: Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks
    passed).
- evidence_id: EV-C4S5-GIT-DIFF
  kind: validation
  reference: git diff --check
  locator: git worktree on feat/cycle4-stage5-resolve-review-findings
  accessed_at: '2026-10-25T05:30:00Z'
  support: supports
  summary: Executed git diff --check with exit code 0; no whitespace errors or conflict
    markers.
- evidence_id: EV-C4S5-REVIEW-CHECK
  kind: validation
  reference: .venv/bin/python scripts/record_review.py check --base main
  locator: reviews/structured/
  accessed_at: '2026-10-25T05:30:00Z'
  support: supports
  summary: Validated all 205 retained structured review bundles in reviews/structured/
    against schema/record_review.yaml and verified byte-for-byte append-only preservation
    against main.
assessments:
- assessment_id: ASSESS-C4S5-PARTICIPANT-AND-RHEA-REF-HYGIENE-16
  area: consistency
  topic: Post-remediation participant connectivity (0 orphan participants), RHEA reference
    usage (0 unreferenced RHEA:* references), and descriptive RHEA reference titles
    across all 16 reassessed MetaCyc:* pathway records
  outcome: supported
  summary: Removing orphan participant CHEBI:17544 (hydrogencarbonate) and unreferenced
    RHEA:10154 from MetaCyc:ARGDEGRAD-PWY (l-arginine-degradation-v.yaml), pruning
    all 28 unreferenced superseded RHEA:* references across the 15 F-C4S4-002 MetaCyc:*
    records, and replacing all 33 generic 'RHEA:<ID> authority record' placeholder
    titles across all 16 reassessed MetaCyc:* records brings participant connectivity
    across the 16 reassessed records to 100% (322 / 322 participant entries connected
    to at least one mechanistic_edge; 7,762 total participant entries across the 273-record
    corpus) and eliminates all unreferenced RHEA:* references (0 / 203 reference entries
    across the 16 reassessed records; 7,053 total reference entries across the 273-record
    corpus) and placeholder RHEA titles across the 16 reassessed records.
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  evidence_ids:
  - EV-C4S4-PREDECESSOR
  - EV-C4S5-ARGDEGRAD-FIXED
  - EV-C4S5-RHEA-REFS-FIXED-15
  - EV-C4S5-RENDERED-PAGES-AND-KGX
  - EV-C4S5-QC
  - EV-C4S5-PYTEST
  metrics:
  - name: orphan_participant_entries_across_reassessed_records
    value: 0.0
    unit: participants
    definition: Count of participants[] entries with zero incident edges in mechanistic_edges
      across the 16 reassessed MetaCyc:* pathway records (322 total participants after
      removing orphan CHEBI:17544 in MetaCyc:ARGDEGRAD-PWY, down from 323).
    denominator: 322
    minimum: 0.0
    maximum: 322.0
  - name: unreferenced_superseded_rhea_references_across_reassessed_records
    value: 0.0
    unit: references
    definition: Count of unreferenced RHEA:* entries in references[] across the 16
      reassessed MetaCyc:* pathway records (203 total references after removing 29
      unreferenced superseded RHEA:* entries, down from 232).
    denominator: 203
    minimum: 0.0
    maximum: 203.0
  - name: generic_rhea_authority_record_placeholder_titles_across_reassessed_records
    value: 0.0
    unit: references
    definition: Count of references[] entries with generic 'RHEA:<ID> authority record'
      placeholder titles across the 16 reassessed MetaCyc:* pathway records (203 total
      references after updating 33 entries).
    denominator: 203
    minimum: 0.0
    maximum: 203.0
  dimensions:
  - name: rendered_page_and_kgx_verification
    value: CHEBI:17544 and RHEA:10154 removed from MetaCyc:ARGDEGRAD-PWY rendered
      page and KGX exports; all 33 updated RHEA:* reference titles rendered across
      16 HTML pages
    definition: Verified post-remediation rendered HTML pages and KGX exports in pages/.
    evidence_ids:
    - EV-C4S5-RENDERED-PAGES-AND-KGX
    - EV-C4S5-QC
- assessment_id: ASSESS-C4S5-SCIENTIFIC-INTEGRITY-16
  area: evidence
  topic: Preservation of pathway identity, taxon grounding, reaction directionality,
    stoichiometry, and edge-level evidence across the 16 remediated MetaCyc:* pathway
    records
  outcome: supported
  summary: Structural verification across all 16 remediated MetaCyc:* YAML files confirms
    that all pathway IDs, taxon groundings, active participant CURIEs, reaction directions,
    step definitions, mechanistic_edges, source_mappings, and structured evidence
    blocks (22,533 total evidence blocks) remain 100% intact and pass closed LinkML
    and authority snapshot checks.
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  evidence_ids:
  - EV-C4S5-ARGDEGRAD-FIXED
  - EV-C4S5-RHEA-REFS-FIXED-15
  - EV-C4S5-QC
  - EV-C4S5-PYTEST
  - EV-C4S5-GIT-DIFF
findings:
- finding_id: F-C4S4-001
  issue_key: metacyc-argdegrad-pwy-stale-rhea10154-hydrogencarbonate-artifacts
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: MetaCyc:ARGDEGRAD-PWY (l-arginine-degradation-v.yaml) stale hydrogencarbonate
    description, orphan CHEBI:17544 participant, unreferenced RHEA:10154 reference,
    and 4 generic RHEA authority titles are resolved
  description: In MetaCyc:ARGDEGRAD-PWY (data/pathways/l-arginine-degradation-v.yaml),
    updated description to replace superseded 'hydrogencarbonate' wording with 'carbamate,
    ammonium, carbon dioxide, and ATP' and 'spontaneous carbamate decarboxylation',
    removed orphan participant CHEBI:17544 (hydrogencarbonate, 0 incident edges),
    removed unreferenced superseded RHEA:10154 from references[], and replaced generic
    'RHEA:<ID> authority record' placeholder titles on RHEA:30757, RHEA:15650, RHEA:19597,
    and RHEA:19513 (now at references[4..7]) with descriptive Rhea reaction direction
    titles via pathwaymech.curation.publish_curation, recorded history/records/l-arginine-degradation-v/2026-10-25T052500Z-antigravity-a1d1e5.yaml,
    and regenerated pages/.
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  field_paths:
  - data/pathways/l-arginine-degradation-v.yaml#description (updated carbamate and
    carbon dioxide wording)
  - data/pathways/l-arginine-degradation-v.yaml#participants[13] (removed orphan CHEBI:17544
    hydrogencarbonate)
  - data/pathways/l-arginine-degradation-v.yaml#references[3] (removed unreferenced
    RHEA:10154)
  - data/pathways/l-arginine-degradation-v.yaml#references[4].title (RHEA:30757 ->
    Rhea carbamate- and ATP-forming carbamate kinase direction)
  - data/pathways/l-arginine-degradation-v.yaml#references[5].title (RHEA:15650 ->
    Rhea spontaneous carbamate decarboxylation direction)
  - data/pathways/l-arginine-degradation-v.yaml#references[6].title (RHEA:19597 ->
    Rhea L-arginine deiminase reaction)
  - data/pathways/l-arginine-degradation-v.yaml#references[7].title (RHEA:19513 ->
    Rhea ornithine carbamoyltransferase reaction)
  evidence_ids:
  - EV-C4S4-PREDECESSOR
  - EV-C4S4-WORKFLOW-EVIDENCE
  - EV-C4S5-ARGDEGRAD-FIXED
  - EV-C4S5-RENDERED-PAGES-AND-KGX
  - EV-C4S5-QC
  - EV-C4S5-PYTEST
  rule_id: CAUSAL_GRAPHS:no-orphan-participants-or-stale-reaction-artifacts
  native_severity: minor
  normalization_reason: 'Native minor representation defect maps directly to minor
    severity: removing orphan participant CHEBI:17544 and unreferenced RHEA:10154,
    updating description to reflect carbamate and carbon dioxide, and replacing the
    4 generic RHEA authority titles brings participant connectivity across the 16
    reassessed MetaCyc:* records to 100% (322 / 322).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-v.yaml
    role: maintained pathway YAML
  disposition_reason: 'Resolved under GitHub issue #714 by updating description, removing
    orphan participant CHEBI:17544 and unreferenced RHEA:10154, and replacing the
    4 generic RHEA authority titles on RHEA:30757, RHEA:15650, RHEA:19597, and RHEA:19513
    in data/pathways/l-arginine-degradation-v.yaml via pathwaymech.curation.publish_curation,
    recording history/records/l-arginine-degradation-v/2026-10-25T052500Z-antigravity-a1d1e5.yaml,
    and regenerating pages/.'
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review
    finding_id: F-C4S4-001
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/714
  tags:
  - cycle4-stage5-resolve-review-findings
  - orphan-participant
  - stale-rhea-reference
- finding_id: F-C4S4-002
  issue_key: metacyc-superseded-unreferenced-rhea-references-in-15-records
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: All 28 unreferenced superseded RHEA:* entries are removed and all 29 generic
    'RHEA:<ID> authority record' titles are replaced across 15 maintained MetaCyc
    pathway records
  description: Across all 15 maintained MetaCyc:* pathway records in F-C4S4-002 (MetaCyc:DARABCAT-PWY,
    MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:GLYCEROLMETAB-PWY,
    MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:ILEUSYN-PWY,
    MetaCyc:LEUSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:TRPSYN-PWY,
    MetaCyc:GLUAMCAT-PWY, and MetaCyc:NONOXIPENT-PWY), removed all 28 unreferenced
    superseded RHEA:* entries from references[] and replaced all 29 generic 'RHEA:<ID>
    authority record' placeholder titles with descriptive Rhea reaction direction
    titles via pathwaymech.curation.publish_curation, recorded 15 history/records/<slug>/2026-10-25T052500Z-antigravity-a1d1e5.yaml
    files, and regenerated pages/.
  target_ids:
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  field_paths:
  - data/pathways/d-arabinose-degradation-i.yaml#references (removed unreferenced
    RHEA:13852)
  - data/pathways/d-arabinose-degradation-i.yaml#references[4].title (RHEA:13850 ->
    Rhea D-ribulose-forming D-arabinose isomerase direction)
  - data/pathways/d-galacturonate-degradation-i.yaml#references (removed unreferenced
    RHEA:27705)
  - data/pathways/d-galacturonate-degradation-i.yaml#references (removed unreferenced
    RHEA:17816)
  - data/pathways/d-galacturonate-degradation-i.yaml#references[9].title (RHEA:27703
    -> Rhea keto-D-tagaturonate-forming D-galacturonate isomerase direction)
  - data/pathways/d-galacturonate-degradation-i.yaml#references[10].title (RHEA:17815
    -> Rhea D-altronate-forming tagaturonate reductase direction)
  - data/pathways/d-glucarate-degradation-i.yaml#references (removed unreferenced
    RHEA:27726)
  - data/pathways/d-glucarate-degradation-i.yaml#references (removed unreferenced
    RHEA:27729)
  - data/pathways/d-glucarate-degradation-i.yaml#references[9].title (RHEA:27727 ->
    Rhea 5-dehydro-4-deoxy-D-glucarate-cleaving aldolase direction)
  - data/pathways/d-xylose-degradation-i.yaml#references (removed unreferenced RHEA:22819)
  - data/pathways/d-xylose-degradation-i.yaml#references[4].title (RHEA:22817 -> Rhea
    alpha-D-xylulofuranose-forming xylose isomerase direction)
  - data/pathways/glycerol-degradation-v.yaml#references (removed unreferenced RHEA:13772)
  - data/pathways/glycerol-degradation-v.yaml#references[4].title (RHEA:13770 -> Rhea
    dihydroxyacetone-forming glycerol dehydrogenase direction)
  - data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml#references (removed unreferenced
    RHEA:10795)
  - data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml#references[10].title (RHEA:10794
    -> Rhea CAIR-forming phosphoribosylaminoimidazole carboxylase direction)
  - data/pathways/l-arabinose-degradation-i.yaml#references (removed unreferenced
    RHEA:14824)
  - data/pathways/l-arabinose-degradation-i.yaml#references (removed unreferenced
    RHEA:22371)
  - data/pathways/l-arabinose-degradation-i.yaml#references[5].title (RHEA:14822 ->
    Rhea L-ribulose-forming L-arabinose isomerase direction)
  - data/pathways/l-arabinose-degradation-i.yaml#references[6].title (RHEA:22369 ->
    Rhea D-xylulose-5-phosphate-forming L-ribulose-5-phosphate 4-epimerase direction)
  - data/pathways/l-fucose-degradation-i.yaml#references (removed unreferenced RHEA:25583)
  - data/pathways/l-fucose-degradation-i.yaml#references (removed unreferenced RHEA:17236)
  - data/pathways/l-fucose-degradation-i.yaml#references[7].title (RHEA:25582 -> Rhea
    alpha-L-fucose-forming L-fucose mutarotase direction)
  - data/pathways/l-fucose-degradation-i.yaml#references[8].title (RHEA:17234 -> Rhea
    L-fuculose-forming L-fucose isomerase direction)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#references (removed
    unreferenced RHEA:22108)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#references (removed
    unreferenced RHEA:22109)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#references[14].title
    (RHEA:40676 -> Rhea L-threonine dehydration to 2-aminobut-2-enoate direction)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#references[15].title
    (RHEA:39968 -> Rhea 2-aminobut-2-enoate tautomerization to 2-iminobutanoate direction)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#references[16].title
    (RHEA:39976 -> Rhea 2-iminobutanoate hydrolysis to 2-oxobutanoate and ammonium
    direction)
  - data/pathways/l-leucine-biosynthesis.yaml#references (removed unreferenced RHEA:32287)
  - data/pathways/l-leucine-biosynthesis.yaml#references (removed unreferenced RHEA:32289)
  - data/pathways/l-leucine-biosynthesis.yaml#references (removed unreferenced RHEA:32271)
  - data/pathways/l-leucine-biosynthesis.yaml#references (removed unreferenced RHEA:32272)
  - data/pathways/l-leucine-biosynthesis.yaml#references[9].title (RHEA:16295 -> Rhea
    (2S)-2-isopropylmalate dehydration to 2-isopropylmaleate direction)
  - data/pathways/l-leucine-biosynthesis.yaml#references[10].title (RHEA:10678 ->
    Rhea 2-isopropylmaleate hydration to (2R,3S)-3-isopropylmalate direction)
  - data/pathways/l-leucine-biosynthesis.yaml#references[11].title (RHEA:10893 ->
    Rhea (2R,3S)-3-isopropylmalate oxidation to (2S)-2-isopropyl-3-oxosuccinate direction)
  - data/pathways/l-leucine-biosynthesis.yaml#references[12].title (RHEA:25079 ->
    Rhea (2S)-2-isopropyl-3-oxosuccinate decarboxylation to 4-methyl-2-oxopentanoate
    direction)
  - data/pathways/l-methionine-biosynthesis-i.yaml#references (removed unreferenced
    RHEA:13965)
  - data/pathways/l-methionine-biosynthesis-i.yaml#references (removed unreferenced
    RHEA:13966)
  - data/pathways/l-methionine-biosynthesis-i.yaml#references[15].title (RHEA:43021
    -> Rhea L,L-cystathionine elimination to L-homocysteine and 2-aminoprop-2-enoate
    direction)
  - data/pathways/l-methionine-biosynthesis-i.yaml#references[16].title (RHEA:40668
    -> Rhea 2-aminoprop-2-enoate tautomerization to 2-iminopropanoate direction)
  - data/pathways/l-methionine-biosynthesis-i.yaml#references[17].title (RHEA:40672
    -> Rhea 2-iminopropanoate hydrolysis to pyruvate and ammonium direction)
  - data/pathways/l-rhamnose-degradation-i.yaml#references (removed unreferenced RHEA:25587)
  - data/pathways/l-rhamnose-degradation-i.yaml#references (removed unreferenced RHEA:23163)
  - data/pathways/l-rhamnose-degradation-i.yaml#references (removed unreferenced RHEA:19692)
  - data/pathways/l-rhamnose-degradation-i.yaml#references[7].title (RHEA:25585 ->
    Rhea beta-L-rhamnose-forming L-rhamnose mutarotase direction)
  - data/pathways/l-rhamnose-degradation-i.yaml#references[8].title (RHEA:23161 ->
    Rhea L-rhamnulose-forming L-rhamnose isomerase direction)
  - data/pathways/l-rhamnose-degradation-i.yaml#references[9].title (RHEA:19690 ->
    Rhea L-rhamnulose-1-phosphate-cleaving aldolase direction)
  - data/pathways/l-tryptophan-biosynthesis.yaml#references (removed unreferenced
    RHEA:10532)
  - data/pathways/l-tryptophan-biosynthesis.yaml#references (removed unreferenced
    RHEA:10533)
  - data/pathways/l-tryptophan-biosynthesis.yaml#references[14].title (RHEA:14082
    -> Rhea indole- and D-glyceraldehyde-3-phosphate-forming tryptophan synthase alpha-reaction
    direction)
  - data/pathways/l-tryptophan-biosynthesis.yaml#references[15].title (RHEA:26435
    -> Rhea L-tryptophan-forming tryptophan synthase beta-reaction direction)
  - data/pathways/n-acetylglucosamine-degradation-i.yaml#references (removed unreferenced
    RHEA:12175)
  - data/pathways/n-acetylglucosamine-degradation-i.yaml#references[4].title (RHEA:12173
    -> Rhea beta-D-fructose-6-phosphate-forming glucosamine-6-phosphate deaminase
    direction)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references
    (removed unreferenced RHEA:14660)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references
    (removed unreferenced RHEA:13680)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references
    (removed unreferenced RHEA:10511)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references
    (removed unreferenced RHEA:17056)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references
    (removed unreferenced RHEA:27629)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references[6].title
    (RHEA:14659 -> Rhea aldehydo-D-ribose-5-phosphate-forming ribose-5-phosphate isomerase
    direction)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references[7].title
    (RHEA:13678 -> Rhea D-xylulose-5-phosphate-forming ribulose-phosphate 3-epimerase
    direction)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references[8].title
    (RHEA:10510 -> Rhea D-sedoheptulose-7-phosphate-forming transketolase direction)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references[9].title
    (RHEA:17054 -> Rhea D-erythrose-4-phosphate-forming transaldolase direction)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#references[10].title
    (RHEA:27627 -> Rhea beta-D-fructose-6-phosphate-forming transketolase direction)
  evidence_ids:
  - EV-C4S4-PREDECESSOR
  - EV-C4S4-WORKFLOW-EVIDENCE
  - EV-C4S5-RHEA-REFS-FIXED-15
  - EV-C4S5-RENDERED-PAGES-AND-KGX
  - EV-C4S5-QC
  - EV-C4S5-PYTEST
  rule_id: CURATION:no-unreferenced-superseded-rhea-references
  native_severity: minor
  normalization_reason: 'Native minor representation defect maps directly to minor
    severity: pruning the 28 unreferenced superseded RHEA:* entries from references[]
    and replacing the 29 generic ''RHEA:<ID> authority record'' titles across the
    15 affected MetaCyc:* records eliminates all dead RHEA:* reference entries and
    placeholder titles across the 16 reassessed MetaCyc:* records.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-arabinose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galacturonate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-glucarate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-xylose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycerol-degradation-v.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arabinose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-fucose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-leucine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-methionine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-rhamnose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tryptophan-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    role: maintained pathway YAML
  disposition_reason: 'Resolved under GitHub issue #714 by removing all 28 unreferenced
    superseded RHEA:* entries from references[] and replacing all 29 generic ''RHEA:<ID>
    authority record'' placeholder titles with descriptive Rhea reaction direction
    titles across the 15 affected MetaCyc:* pathway records via pathwaymech.curation.publish_curation,
    recording 15 history/records/<slug>/2026-10-25T052500Z-antigravity-a1d1e5.yaml
    provenance entries, and regenerating pages/.'
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review
    finding_id: F-C4S4-002
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/714
  tags:
  - cycle4-stage5-resolve-review-findings
  - stale-rhea-reference
  - reference-hygiene
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  rationale: Retain all 16 remediated MetaCyc:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions with 100% connected participants and clean,
    descriptive RHEA:* reference metadata.
  evidence_ids:
  - EV-C4S5-ARGDEGRAD-FIXED
  - EV-C4S5-RHEA-REFS-FIXED-15
  - EV-C4S5-QC
limitations:
- This Cycle 4 Stage 5 successor review is scoped to verifying the remediation of
  Cycle 4 Stage 4 findings F-C4S4-001 and F-C4S4-002 across the 16 affected maintained
  MetaCyc:* pathway records; the remaining 257 maintained records had zero findings
  in Cycle 4 Stage 4 and were verified via repository-wide QC and pytest gates.
notes:
- CLAW aggregator CLI (kg_microbe_reviews) is not installed in the local culturebotai-claw
  environment; finding lineage (predecessor review_id 20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review,
  finding_ids F-C4S4-001 and F-C4S4-002, exact issue_keys, 100% target_ids retention,
  and absence of competing heads) was explicitly verified against reviews/structured/.
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review
  relationship: resolves_findings_from
links:
- https://github.com/CultureBotAI/PathwayMech/issues/714
tags:
- mech-goal-sequence-20261019
- cycle-4
- stage-5
- resolve-review-findings
```
