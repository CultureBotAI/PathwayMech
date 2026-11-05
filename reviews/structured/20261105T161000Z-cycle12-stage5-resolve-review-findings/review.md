# Cycle 12 Stage 5 Successor Review Resolving F-C12S4-001 and F-C12S4-002 Across 10 Maintained Pathway Records

- Review: 20261105T161000Z-cycle12-stage5-resolve-review-findings
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-11-05T15:55:00Z
- Finished UTC: 2026-11-05T16:10:00Z
- Reviewer: Antigravity (pathwaymech-resolve-reviews + review-yaml-category) (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Re-inspected and verified all 10 maintained pathway YAML records affected by Cycle 12 Stage 4 findings F-C12S4-001 (missing-reference-urls-10-records across 10 maintained pathway records: Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, and WikiPathways:WP296) and F-C12S4-002 (placeholder-reactome-and-mibig-reference-titles-4-records across 4 maintained pathway records: Reactome:R-MTU-879299, Reactome:R-MTU-868688, Reactome:R-MTU-879325, and MIBiG:BGC0002072), grouped together under shared root-cause group G-C12S5-001 and GitHub issue #798. Remediated all 60 field defects across all 10 records via pathwaymech.curation.publish_curation: (1) across the 10 pathway records in F-C12S4-001, populated canonical resolvable url values across all 47 references[] entries (12 in Reactome:R-MTU-868688, 12 in Reactome:R-MTU-879299, 8 in Reactome:R-MTU-936721, 5 in Reactome:R-MTU-936635, 3 in Reactome:R-MTU-936654, 2 in Reactome:R-MTU-879325, 2 in WikiPathways:WP5060, 1 in WikiPathways:WP5587, 1 in MIBiG:BGC0002072, and 1 in WikiPathways:WP296; comprising 34 PubMed URLs https://pubmed.ncbi.nlm.nih.gov/&lt;pmid&gt;/, 12 Reactome reaction URLs https://reactome.org/content/detail/&lt;id&gt;, and 1 ChEBI URL https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:30744), bringing references missing a resolvable url to 0 / 116 across the 10 reassessed records and 0 / 7,132 across the entire 281-record corpus (100.0% reference URL coverage); and (2) across the 4 pathway records in F-C12S4-002, replaced all 13 generic placeholder references[].title entries (6 in Reactome:R-MTU-879299, 5 in Reactome:R-MTU-868688, 1 in Reactome:R-MTU-879325, and 1 in MIBiG:BGC0002072) with verified descriptive Reactome reaction titles (&lt;reaction label&gt; (&lt;reference_id&gt;)) and the verified PubMed peer-reviewed article title for PMID:29348524 ('Linearmycins are lytic membrane-targeting antibiotics', Stubbendieck et al., J Antibiot 2018), bringing placeholder reference titles to 0 / 116 across the 10 reassessed records and 0 / 7,132 across the entire 281-record corpus. Recorded 10 append-only curation history files under history/records/&lt;slug&gt;/2026-11-05T160500Z-antigravity-*.yaml, regenerated rendered pages (.venv/bin/pathwaymech-render-pages), and confirmed full pass across QC (281 pathway records, 1,053 history records, 23,009 evidence blocks, 33 source records).

## Scope And Provenance

Complete post-remediation reassessment of the 10 maintained pathway records in data/pathways/*.yaml that carried open findings (F-C12S4-001 and F-C12S4-002) in Cycle 12 Stage 4 review 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review.

Selection: All 10 maintained pathway records in CultureBotAI/PathwayMech carrying open findings in reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml (100% of open Cycle 12 Stage 4 maintained-record findings).
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 300d28486e8bf92557723036cb87e499dcb481ea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| Reactome:R-MTU-868688 | data/pathways/mycobacterium-trehalose-biosynthesis.yaml | maintained | Mycobacterium tuberculosis trehalose biosynthesis (Reactome:R-MTU-868688) |
| Reactome:R-MTU-879299 | data/pathways/mycothiol-biosynthesis.yaml | maintained | Mycothiol biosynthesis (Reactome:R-MTU-879299) |
| Reactome:R-MTU-936721 | data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml | maintained | Cysteine synthesis from O-acetylserine (Reactome:R-MTU-936721) |
| Reactome:R-MTU-936635 | data/pathways/mycobacterium-sulfate-assimilation.yaml | maintained | Sulfate assimilation (Reactome:R-MTU-936635) |
| Reactome:R-MTU-936654 | data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml | maintained | Cysteine synthesis from O-phosphoserine (Reactome:R-MTU-936654) |
| Reactome:R-MTU-879325 | data/pathways/mycothiol-catabolism.yaml | maintained | mycothiol S-conjugate catabolism (Reactome:R-MTU-879325) |
| WikiPathways:WP5060 | data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml | maintained | Peptidoglycan cytoplasmic synthesis and recycling pathways (WikiPathways:WP5060) |
| WikiPathways:WP5587 | data/pathways/2-phenylethanol-biosynthesis.yaml | maintained | 2-phenylethanol biosynthesis (WikiPathways:WP5587) |
| MIBiG:BGC0002072 | data/pathways/linearmycin-biosynthetic-gene-cluster.yaml | maintained | linearmycin A and related metabolites biosynthetic gene cluster (MIBiG:BGC0002072) |
| WikiPathways:WP296 | data/pathways/tca-cycle-detailed.yaml | maintained | TCA cycle - detailed (WikiPathways:WP296) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Repository QC and closed-schema validation (just validate) | passed | True | Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, WikiPathways:WP296 | Validated all 281 maintained pathway records (including the 10 reassessed records) against the closed LinkML schema, local identifier/label authority snapshots, 1,053 history records, 23,009 evidence blocks, 33 source records, and pages/ synchrony. |
| Pytest unit and integration test suite (just test) | passed | True | Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, WikiPathways:WP296 | All pytest unit and integration tests passed across schema, KGX export, SSSOM, and record-review checks. |
| Ruff lint check (just lint) | passed | True | Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, WikiPathways:WP296 | Ruff check passed with 0 errors. |
| Git whitespace and conflict marker check | passed | True | Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, WikiPathways:WP296 | git diff --check exited 0 with no whitespace or conflict marker issues. |
| Structured review bundle contract check (just review-check) | passed | True | Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, WikiPathways:WP296 | All retained structured review bundles in reviews/structured/ passed schema and append-only checks against main. |

## Scientific And Domain Assessments

### Post-remediation completion of reference URL coverage (116 / 116 reassessed references; 7,132 / 7,132 corpus-wide) and elimination of placeholder Reactome/MIBiG reference titles (0 / 116 reassessed references; 0 / 7,132 corpus-wide)

consistency: supported. Targets: Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, WikiPathways:WP296.

Populating canonical resolvable url values across all 47 references[] entries in the 10 F-C12S4-001 records brings missing reference URLs to 0 / 116 across the 10 reassessed records and 0 / 7,132 across the entire 281-record corpus (100.0% reference URL coverage). Replacing all 13 placeholder references[].title entries across the 4 F-C12S4-002 records with verified descriptive Reactome reaction titles and the peer-reviewed PubMed article title for PMID:29348524 brings placeholder reference titles to 0 / 116 across the 10 reassessed records and 0 / 7,132 across the entire 281-record corpus.

### Preservation of pathway identity, taxon grounding, participant connectivity, reaction directionality, stoichiometry, and edge-level evidence across the 10 reassessed pathway records

evidence: supported. Targets: Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, WikiPathways:WP296.

Structural verification across all 10 reassessed pathway YAML files confirms that all pathway IDs, taxon groundings, 7,912 connected participant entries (0 orphans), 1,640 reaction steps (740 RHEA:*), 14,814 non-reflexive mechanistic_edges, 1,078 source_mappings, and 23,009 structured evidence blocks remain 100% intact and pass closed LinkML and authority snapshot checks.

## Findings

### F-C12S4-001: All 47 references[] entries omitting a resolvable url field across 10 maintained Reactome, WikiPathways, and MIBiG pathway records are populated with canonical URLs

minor / resolved / confirmed; issue key: missing-reference-urls-10-records.

Across all 10 maintained pathway records in F-C12S4-001 (Reactome:R-MTU-868688 mycobacterium-trehalose-biosynthesis.yaml: 12; Reactome:R-MTU-879299 mycothiol-biosynthesis.yaml: 12; Reactome:R-MTU-936721 mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml: 8; Reactome:R-MTU-936635 mycobacterium-sulfate-assimilation.yaml: 5; Reactome:R-MTU-936654 mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml: 3; Reactome:R-MTU-879325 mycothiol-catabolism.yaml: 2; WikiPathways:WP5060 peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml: 2; WikiPathways:WP5587 2-phenylethanol-biosynthesis.yaml: 1; MIBiG:BGC0002072 linearmycin-biosynthetic-gene-cluster.yaml: 1; and WikiPathways:WP296 tca-cycle-detailed.yaml: 1), populated canonical resolvable url values across all 47 references[] entries (34 PubMed URLs, 12 Reactome reaction detail URLs, and 1 ChEBI URL) via pathwaymech.curation.publish_curation, recorded 10 history/records/&lt;slug&gt;/2026-11-05T160500Z-antigravity-*.yaml files, and regenerated pages/ under root-cause group G-C12S5-001 (#798).

Disposition: Resolved under GitHub issue #798 (group G-C12S5-001) by populating canonical resolvable url values across all 47 references[] entries in the 10 affected pathway records (34 PubMed URLs https://pubmed.ncbi.nlm.nih.gov/&lt;pmid&gt;/, 12 Reactome reaction detail URLs https://reactome.org/content/detail/&lt;id&gt;, and 1 ChEBI URL https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:30744) via pathwaymech.curation.publish_curation (with 10 history files and regenerated pages/).

### F-C12S4-002: All 13 generic placeholder references[].title strings across Reactome:R-MTU-879299, Reactome:R-MTU-868688, Reactome:R-MTU-879325, and MIBiG:BGC0002072 are replaced with descriptive reaction and peer-reviewed article titles

minor / resolved / confirmed; issue key: placeholder-reactome-and-mibig-reference-titles-4-records.

Across all 4 maintained pathway records in F-C12S4-002 (Reactome:R-MTU-879299 mycothiol-biosynthesis.yaml: 6; Reactome:R-MTU-868688 mycobacterium-trehalose-biosynthesis.yaml: 5; Reactome:R-MTU-879325 mycothiol-catabolism.yaml: 1; and MIBiG:BGC0002072 linearmycin-biosynthetic-gene-cluster.yaml: 1), replaced all 13 generic placeholder references[].title entries ('Reactome reaction &lt;id&gt;' and 'MIBiG literature reference PMID:29348524') with verified descriptive Reactome reaction titles (&lt;reaction label&gt; (&lt;reference_id&gt;)) and the verified PubMed article title for PMID:29348524 ('Linearmycins are lytic membrane-targeting antibiotics') via pathwaymech.curation.publish_curation, recorded curation history files, and regenerated pages/ under root-cause group G-C12S5-001 (#798).

Disposition: Resolved under GitHub issue #798 (group G-C12S5-001) by replacing all 13 generic placeholder references[].title entries across Reactome:R-MTU-879299 (6), Reactome:R-MTU-868688 (5), Reactome:R-MTU-879325 (1), and MIBiG:BGC0002072 (1) with verified descriptive Reactome reaction titles and the peer-reviewed PubMed article title for PMID:29348524 via pathwaymech.curation.publish_curation (with history files and regenerated pages/).

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, WikiPathways:WP296. Retain all 10 reassessed pathway records as distinct, non-duplicate source-scoped pathway definitions with 100.0% reference URL coverage (116 / 116 across reassessed records; 7,132 / 7,132 corpus-wide) and 0 placeholder reference titles (0 / 116 across reassessed records; 0 / 7,132 corpus-wide).

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EV-C12S4-PREDECESSOR | reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml; findings[0] (F-C12S4-001) and findings[1] (F-C12S4-002) | supports | Predecessor Cycle 12 Stage 4 cohort review recorded two minor open representation findings across 10 maintained pathway records: F-C12S4-001 (missing-reference-urls-10-records across Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587, MIBiG:BGC0002072, and WikiPathways:WP296) and F-C12S4-002 (placeholder-reactome-and-mibig-reference-titles-4-records across Reactome:R-MTU-879299, Reactome:R-MTU-868688, Reactome:R-MTU-879325, and MIBiG:BGC0002072). |
| EV-C12S4-WORKFLOW-EVIDENCE | reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-04/revision-0001/evidence.yaml; findings[0..1] (F-C12S4-001, F-C12S4-002) | supports | Cycle 12 Stage 4 workflow evidence manifest carried forward F-C12S4-001 and F-C12S4-002 as open findings for Cycle 12 Stage 5 grouped remediation. |
| EV-C12S5-REF-URLS-FIXED-10 | data/pathways/mycobacterium-trehalose-biosynthesis.yaml; references[0..11].url in mycobacterium-trehalose-biosynthesis.yaml, references[0..11].url in mycothiol-biosynthesis.yaml, references[0..7].url in mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml, references[0..4].url in mycobacterium-sulfate-assimilation.yaml, references[0..2].url in mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml, references[0..1].url in mycothiol-catabolism.yaml, references[0..1].url in peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml, references[0].url in 2-phenylethanol-biosynthesis.yaml, references[0].url in linearmycin-biosynthetic-gene-cluster.yaml, and references[0].url in tca-cycle-detailed.yaml | supports | Across all 10 maintained pathway records in F-C12S4-001, populated canonical resolvable url values on all 47 references[] entries (34 PubMed URLs, 12 Reactome reaction detail URLs, and 1 ChEBI URL) via pathwaymech.curation.publish_curation, achieving 116 / 116 (100.0%) reference URL coverage across the 10 reassessed records and 7,132 / 7,132 (100.0%) across the 281-record corpus. |
| EV-C12S5-REF-TITLES-FIXED-4 | data/pathways/mycothiol-biosynthesis.yaml; references[0..5].title in mycothiol-biosynthesis.yaml, references[0..4].title in mycobacterium-trehalose-biosynthesis.yaml, references[0].title in mycothiol-catabolism.yaml, and references[0].title in linearmycin-biosynthetic-gene-cluster.yaml | supports | Across all 4 maintained pathway records in F-C12S4-002 (Reactome:R-MTU-879299, Reactome:R-MTU-868688, Reactome:R-MTU-879325, and MIBiG:BGC0002072), replaced all 13 generic placeholder references[].title entries with verified descriptive Reactome reaction titles (&lt;reaction label&gt; (&lt;reference_id&gt;)) and the verified PubMed article title for PMID:29348524 ('Linearmycins are lytic membrane-targeting antibiotics') via pathwaymech.curation.publish_curation. |
| EV-C12S5-PUBMED-29348524 | data/pathways/linearmycin-biosynthetic-gene-cluster.yaml; references[0] (PMID:29348524) | supports | Updated references[0] in MIBiG:BGC0002072 (linearmycin-biosynthetic-gene-cluster.yaml) with the verified peer-reviewed PubMed article title ('Linearmycins are lytic membrane-targeting antibiotics', Stubbendieck et al., J Antibiot 2018) and canonical PubMed URL (https://pubmed.ncbi.nlm.nih.gov/29348524/). |
| EV-C12S5-RENDERED-PAGES | pages/records/Reactome_R-MTU-879299.html; 10 updated HTML pages in pages/records/ for the 10 remediated pathway records | supports | After running .venv/bin/pathwaymech-render-pages, verified that all 10 modified pathway record HTML pages in pages/records/ render clickable reference anchors with descriptive titles for all 47 newly populated URLs and 13 updated titles. |
| EV-C12S5-QC | .venv/bin/pathwaymech-run-qc; stdout summary (281 pathway records, 1053 history records, 23,009 evidence blocks, 33 source records) | supports | Executed .venv/bin/pathwaymech-run-qc: validated 281 pathway records against the closed LinkML schema, verified all identifiers and labels against local authority snapshots, validated 1,053 history records (including 10 new Cycle 12 Stage 5 record history entries referencing issue #798) and 23,009 evidence blocks, and confirmed pages/ synchrony. |
| EV-C12S5-PYTEST | TMPDIR=/tmp .venv/bin/pytest -p no:cacheprovider -q; pytest suite execution across tests/ | supports | Executed TMPDIR=/tmp .venv/bin/pytest -p no:cacheprovider -q across the full test suite. |
| EV-C12S5-RUFF | .venv/bin/ruff check --no-cache .; ruff check output | supports | Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks passed). |
| EV-C12S5-GIT-DIFF | git diff --check; git worktree on feat/cycle12-stage5-resolve-review-findings | supports | Executed git diff --check with exit code 0; no whitespace errors or conflict markers. |
| EV-C12S5-REVIEW-CHECK | TMPDIR=/tmp .venv/bin/python scripts/record_review.py check --base main; reviews/structured/ | supports | Validated all retained structured review bundles in reviews/structured/ against schema/record_review.yaml and verified byte-for-byte append-only preservation against main. |

## Limits And Additional Notes

- This Cycle 12 Stage 5 successor review is scoped to verifying the remediation of Cycle 12 Stage 4 findings F-C12S4-001 and F-C12S4-002 across the 10 affected maintained pathway records; the remaining 271 maintained records had zero findings in Cycle 12 Stage 4 and were verified via repository-wide QC and pytest gates.
- CLAW aggregator CLI (kg_microbe_reviews) is not installed in the local culturebotai-claw environment; finding lineage (predecessor review_id 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review, finding_ids F-C12S4-001 and F-C12S4-002, exact issue_keys, 100% target_ids retention, and absence of competing heads) was explicitly verified against reviews/structured/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T161000Z-cycle12-stage5-resolve-review-findings
kind: batch
repository: CultureBotAI/PathwayMech
title: Cycle 12 Stage 5 Successor Review Resolving F-C12S4-001 and F-C12S4-002 Across
  10 Maintained Pathway Records
started_at: '2026-11-05T15:55:00Z'
finished_at: '2026-11-05T16:10:00Z'
reviewer:
  identity: Antigravity (pathwaymech-resolve-reviews + review-yaml-category)
  kind: agent
  model: Claude Opus 4.6 (Thinking)
  independence: self_review
  independence_basis: 'Same agent session (a1d1e545-faee-4294-8a87-4c2d031a6538) implemented
    the Cycle 12 Stage 5 curation fixes for GitHub issue #798 and verified post-remediation
    records, curation history files, and rendered HTML pages.'
skill: pathwaymech-resolve-reviews
completion: completed
verdict: pass
native_verdict: coherent
scientific_review: true
summary: 'Re-inspected and verified all 10 maintained pathway YAML records affected
  by Cycle 12 Stage 4 findings F-C12S4-001 (missing-reference-urls-10-records across
  10 maintained pathway records: Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721,
  Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060,
  WikiPathways:WP5587, MIBiG:BGC0002072, and WikiPathways:WP296) and F-C12S4-002 (placeholder-reactome-and-mibig-reference-titles-4-records
  across 4 maintained pathway records: Reactome:R-MTU-879299, Reactome:R-MTU-868688,
  Reactome:R-MTU-879325, and MIBiG:BGC0002072), grouped together under shared root-cause
  group G-C12S5-001 and GitHub issue #798. Remediated all 60 field defects across
  all 10 records via pathwaymech.curation.publish_curation: (1) across the 10 pathway
  records in F-C12S4-001, populated canonical resolvable url values across all 47
  references[] entries (12 in Reactome:R-MTU-868688, 12 in Reactome:R-MTU-879299,
  8 in Reactome:R-MTU-936721, 5 in Reactome:R-MTU-936635, 3 in Reactome:R-MTU-936654,
  2 in Reactome:R-MTU-879325, 2 in WikiPathways:WP5060, 1 in WikiPathways:WP5587,
  1 in MIBiG:BGC0002072, and 1 in WikiPathways:WP296; comprising 34 PubMed URLs https://pubmed.ncbi.nlm.nih.gov/<pmid>/,
  12 Reactome reaction URLs https://reactome.org/content/detail/<id>, and 1 ChEBI
  URL https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:30744), bringing references
  missing a resolvable url to 0 / 116 across the 10 reassessed records and 0 / 7,132
  across the entire 281-record corpus (100.0% reference URL coverage); and (2) across
  the 4 pathway records in F-C12S4-002, replaced all 13 generic placeholder references[].title
  entries (6 in Reactome:R-MTU-879299, 5 in Reactome:R-MTU-868688, 1 in Reactome:R-MTU-879325,
  and 1 in MIBiG:BGC0002072) with verified descriptive Reactome reaction titles (<reaction
  label> (<reference_id>)) and the verified PubMed peer-reviewed article title for
  PMID:29348524 (''Linearmycins are lytic membrane-targeting antibiotics'', Stubbendieck
  et al., J Antibiot 2018), bringing placeholder reference titles to 0 / 116 across
  the 10 reassessed records and 0 / 7,132 across the entire 281-record corpus. Recorded
  10 append-only curation history files under history/records/<slug>/2026-11-05T160500Z-antigravity-*.yaml,
  regenerated rendered pages (.venv/bin/pathwaymech-render-pages), and confirmed full
  pass across QC (281 pathway records, 1,053 history records, 23,009 evidence blocks,
  33 source records).'
source:
  git_revision: 300d28486e8bf92557723036cb87e499dcb481ea
  state: working_tree
  inputs:
  - path: .claude/skills/pathwaymech-resolve-reviews/SKILL.md
    sha256: 3d3b9d3b9e56cc782cf4ff63d491c5b589e9bdcde71438a695384b228edc4aea
    role: context
  - path: conf/identifier_policy.yaml
    sha256: f57137cbec6ee2ffb4abc1c2e448dd93766e37edac9b07c43cab24c5809d27f7
    role: context
  - path: data/pathways/2-phenylethanol-biosynthesis.yaml
    sha256: a7a5e63709be01fb1d78d38ebf908878e008f7c8c8a6c2fafd51fbd67fc1782c
    role: target
  - path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
    sha256: 8cae725a5c0caf991a2bc6e2bf5d53e9e2910816d66bdd16dba29e59ba6217cc
    role: target
  - path: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
    sha256: 478a9c0093653374b69578b03b26cfb9a8f10c33c62b9934200d06f1a456ca56
    role: target
  - path: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
    sha256: 14e4d0dacc4c2e3e0b5e2bf0db5bb11045fc694a27dea62d5716772898cea9ba
    role: target
  - path: data/pathways/mycobacterium-sulfate-assimilation.yaml
    sha256: 94599e5b5a0d341ad2a29eb69b68ca48d73d2d228ca6a862ea776e61ab3fe01a
    role: target
  - path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
    sha256: 7e96c46849b5d4438f87c2e7ef8468ddd9e3736c90f1f56fbdc9674689d88330
    role: target
  - path: data/pathways/mycothiol-biosynthesis.yaml
    sha256: ae877d4a8ec7fabe728669c180807547dfe9617c4479d10c3bf60a9229d5b05c
    role: target
  - path: data/pathways/mycothiol-catabolism.yaml
    sha256: b9f168d7310502c8c1ec6fe29fef5e03b42e3805bd813348d950cd185f845ec7
    role: target
  - path: data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
    sha256: 6fa7c3486318e3630b693c3f0ce67176121c52ab99d04e3e8f3db6f095d1a6de
    role: target
  - path: data/pathways/tca-cycle-detailed.yaml
    sha256: f13cac35b226c3a2780ac349308cd749e47592d4517c81de6d67bd2a8056f1b4
    role: target
  - path: history/records/2-phenylethanol-biosynthesis/2026-11-05T160500Z-antigravity-f849f0.yaml
    sha256: c663c5f6073f360627c122a62ce8dc06e9f592dde4ac923a2f6649168f257a14
    role: context
  - path: history/records/linearmycin-biosynthetic-gene-cluster/2026-11-05T160500Z-antigravity-36b800.yaml
    sha256: fb6fac8ec962d4a1f7231ab21e62963b463bda8fd713217596ca3fdaef5ad88d
    role: context
  - path: history/records/mycobacterium-cysteine-synthesis-from-o-acetylserine/2026-11-05T160500Z-antigravity-c71bf1.yaml
    sha256: c266ed8c6f9bf0153838bae6334ccfddda7fab2816bae6fe1e4f59b29d1c6bf7
    role: context
  - path: history/records/mycobacterium-cysteine-synthesis-from-o-phosphoserine/2026-11-05T160500Z-antigravity-a4451a.yaml
    sha256: d63028e27f1c1030f89f21350b1f308040c7dfd68b64bf6c352c319c0147f84f
    role: context
  - path: history/records/mycobacterium-sulfate-assimilation/2026-11-05T160500Z-antigravity-a67be4.yaml
    sha256: 2bb00b4d58e7f7219896e547d159f811489c23bc7a6514cade7059c8ea6fa857
    role: context
  - path: history/records/mycobacterium-trehalose-biosynthesis/2026-11-05T160500Z-antigravity-b4812a.yaml
    sha256: 79b77453e96100f8c07d00f469c07b934779895c36f2562e4f333ee3126c17e9
    role: context
  - path: history/records/mycothiol-biosynthesis/2026-11-05T160500Z-antigravity-dbf8da.yaml
    sha256: d5b4b0c8008cf45e556641f12348e30a89fcc9576985ef9ce3ee68643e187a88
    role: context
  - path: history/records/mycothiol-catabolism/2026-11-05T160500Z-antigravity-4d257f.yaml
    sha256: 78cb07bb9e42e654850fb5d1a33b9d1dbb7f4da42ac7f4818702109a3bb17e98
    role: context
  - path: history/records/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways/2026-11-05T160500Z-antigravity-97aabe.yaml
    sha256: 03de7f4d2717ff2783631336367fac7f2c594c6ea3d52c041801adad762065cf
    role: context
  - path: history/records/tca-cycle-detailed/2026-11-05T160500Z-antigravity-5a803c.yaml
    sha256: bf8b82d474574573e465ee70646de63b2d40b08cb11cf6dd54d391d108542510
    role: context
  - path: pages/records/MIBiG_BGC0002072.html
    sha256: d97d3593316f0d5e6a1ef3a3674278f2d2f9d3baee6bc9be26fc8ac66b339eb9
    role: context
  - path: pages/records/Reactome_R-MTU-868688.html
    sha256: ff8be3cd912b3ca5b2c3c285e4b2e93f84920d2775ebccd6142fc78d3fbda915
    role: context
  - path: pages/records/Reactome_R-MTU-879299.html
    sha256: 77bd5c9f6fc6b01acd929937b49b7f9548d880a3ced8661c4d4ebd97a76088d2
    role: context
  - path: pages/records/Reactome_R-MTU-879325.html
    sha256: 50cdbb6cb2d9cd6a8d5d7003387bacf7cc7aaf4c4987db755b50f629f8648b35
    role: context
  - path: pages/records/Reactome_R-MTU-936635.html
    sha256: d056c5e5f863f26c1fd2f0ec679397010aa16bc1b6b9c2218569417967ecf491
    role: context
  - path: pages/records/Reactome_R-MTU-936654.html
    sha256: 4ec7dd38fab2154df6e90c852b57253f7b2a8d9215ad695020189c805aa0418e
    role: context
  - path: pages/records/Reactome_R-MTU-936721.html
    sha256: 1fd42dc8497e48e32369ef96d73791d5af0f3942be9ff0af150724d0a1c82981
    role: context
  - path: pages/records/WikiPathways_WP296.html
    sha256: ac4ac082ae7c2d65719b30e02f6979a9b80ea50d7f343d3d34a1c90ada3e4505
    role: context
  - path: pages/records/WikiPathways_WP5060.html
    sha256: 685f42306e4f0f9796dcfbce04e000b839921b4df3ea5bcaeebfc1e71e44da6a
    role: context
  - path: pages/records/WikiPathways_WP5587.html
    sha256: ee3cbe6064370de3b86b083d5b24c012fd2eccc6eca0b4f2be5efe08aa464556
    role: context
  - path: reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml
    sha256: 3b48a17bdc81244e86e7b367348c9f4d42e284b93f4122b5d52b76e47df089f2
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-04/revision-0001/evidence.yaml
    sha256: 87b916a21dc63c237a81de44bf63f4cf0b96af92c1a0d9ae6c82762402e8f0ee
    role: context
scope:
  description: Complete post-remediation reassessment of the 10 maintained pathway
    records in data/pathways/*.yaml that carried open findings (F-C12S4-001 and F-C12S4-002)
    in Cycle 12 Stage 4 review 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review.
  selection: All 10 maintained pathway records in CultureBotAI/PathwayMech carrying
    open findings in reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml
    (100% of open Cycle 12 Stage 4 maintained-record findings).
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  exclusions:
  - target: Remaining 271 maintained pathway records in data/pathways/*.yaml
    reason: Assessed with zero open findings in Cycle 12 Stage 4 review 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review
      and unchanged in Cycle 12 Stage 5.
  - target: research/pathway_additions/*.yaml (6 withheld staging drafts)
    reason: Non-maintained research staging drafts outside data/pathways/*.yaml; their
      2 historical open findings (F01 in 20261010T090124Z-siroheme-pathway-addition-blocked-review
      and F1 in 20261010T100956Z-ecoli-14dhna-octaprenyl-draft-review) remain untouched.
targets:
- target_id: Reactome:R-MTU-868688
  path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
  label: Mycobacterium tuberculosis trehalose biosynthesis (Reactome:R-MTU-868688)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7e96c46849b5d4438f87c2e7ef8468ddd9e3736c90f1f56fbdc9674689d88330
    description: 'Raw SHA-256 file digest of data/pathways/mycobacterium-trehalose-biosynthesis.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-879299
  path: data/pathways/mycothiol-biosynthesis.yaml
  label: Mycothiol biosynthesis (Reactome:R-MTU-879299)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ae877d4a8ec7fabe728669c180807547dfe9617c4479d10c3bf60a9229d5b05c
    description: 'Raw SHA-256 file digest of data/pathways/mycothiol-biosynthesis.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycothiol-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-936721
  path: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
  label: Cysteine synthesis from O-acetylserine (Reactome:R-MTU-936721)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 478a9c0093653374b69578b03b26cfb9a8f10c33c62b9934200d06f1a456ca56
    description: 'Raw SHA-256 file digest of data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-936635
  path: data/pathways/mycobacterium-sulfate-assimilation.yaml
  label: Sulfate assimilation (Reactome:R-MTU-936635)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 94599e5b5a0d341ad2a29eb69b68ca48d73d2d228ca6a862ea776e61ab3fe01a
    description: 'Raw SHA-256 file digest of data/pathways/mycobacterium-sulfate-assimilation.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-sulfate-assimilation.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-936654
  path: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
  label: Cysteine synthesis from O-phosphoserine (Reactome:R-MTU-936654)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 14e4d0dacc4c2e3e0b5e2bf0db5bb11045fc694a27dea62d5716772898cea9ba
    description: 'Raw SHA-256 file digest of data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-879325
  path: data/pathways/mycothiol-catabolism.yaml
  label: mycothiol S-conjugate catabolism (Reactome:R-MTU-879325)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b9f168d7310502c8c1ec6fe29fef5e03b42e3805bd813348d950cd185f845ec7
    description: 'Raw SHA-256 file digest of data/pathways/mycothiol-catabolism.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycothiol-catabolism.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP5060
  path: data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
  label: Peptidoglycan cytoplasmic synthesis and recycling pathways (WikiPathways:WP5060)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6fa7c3486318e3630b693c3f0ce67176121c52ab99d04e3e8f3db6f095d1a6de
    description: 'Raw SHA-256 file digest of data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP5587
  path: data/pathways/2-phenylethanol-biosynthesis.yaml
  label: 2-phenylethanol biosynthesis (WikiPathways:WP5587)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a7a5e63709be01fb1d78d38ebf908878e008f7c8c8a6c2fafd51fbd67fc1782c
    description: 'Raw SHA-256 file digest of data/pathways/2-phenylethanol-biosynthesis.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-phenylethanol-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MIBiG:BGC0002072
  path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
  label: linearmycin A and related metabolites biosynthetic gene cluster (MIBiG:BGC0002072)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8cae725a5c0caf991a2bc6e2bf5d53e9e2910816d66bdd16dba29e59ba6217cc
    description: 'Raw SHA-256 file digest of data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP296
  path: data/pathways/tca-cycle-detailed.yaml
  label: TCA cycle - detailed (WikiPathways:WP296)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: f13cac35b226c3a2780ac349308cd749e47592d4517c81de6d67bd2a8056f1b4
    description: 'Raw SHA-256 file digest of data/pathways/tca-cycle-detailed.yaml
      in Cycle 12 Stage 5 (issue #798).'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/tca-cycle-detailed.yaml
    role: maintained pathway YAML
checks:
- check_id: validate
  name: Repository QC and closed-schema validation (just validate)
  status: passed
  required: true
  summary: Validated all 281 maintained pathway records (including the 10 reassessed
    records) against the closed LinkML schema, local identifier/label authority snapshots,
    1,053 history records, 23,009 evidence blocks, 33 source records, and pages/ synchrony.
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  command: .venv/bin/pathwaymech-run-qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C12S5-QC
  scope_note: 'Full-repository QC gate after applying issue #798 fixes and regenerating
    pages/.'
- check_id: test
  name: Pytest unit and integration test suite (just test)
  status: passed
  required: true
  summary: All pytest unit and integration tests passed across schema, KGX export,
    SSSOM, and record-review checks.
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  command: TMPDIR=/tmp .venv/bin/pytest -p no:cacheprovider -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C12S5-PYTEST
  scope_note: Full pytest test suite.
- check_id: lint
  name: Ruff lint check (just lint)
  status: passed
  required: true
  summary: Ruff check passed with 0 errors.
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  command: .venv/bin/ruff check --no-cache .
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C12S5-RUFF
  scope_note: Repository-wide Python lint check.
- check_id: git-diff-check
  name: Git whitespace and conflict marker check
  status: passed
  required: true
  summary: git diff --check exited 0 with no whitespace or conflict marker issues.
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C12S5-GIT-DIFF
  scope_note: Worktree diff check across all Cycle 12 Stage 5 edits.
- check_id: review-check
  name: Structured review bundle contract check (just review-check)
  status: passed
  required: true
  summary: All retained structured review bundles in reviews/structured/ passed schema
    and append-only checks against main.
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  command: TMPDIR=/tmp .venv/bin/python scripts/record_review.py check --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C12S5-REVIEW-CHECK
  scope_note: Verifies append-only immutability of prior bundles and validity of current
    bundle.
evidence:
- evidence_id: EV-C12S4-PREDECESSOR
  kind: prior_review
  reference: reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml
  locator: findings[0] (F-C12S4-001) and findings[1] (F-C12S4-002)
  accessed_at: '2026-11-05T15:55:00Z'
  support: supports
  summary: 'Predecessor Cycle 12 Stage 4 cohort review recorded two minor open representation
    findings across 10 maintained pathway records: F-C12S4-001 (missing-reference-urls-10-records
    across Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-936721, Reactome:R-MTU-936635,
    Reactome:R-MTU-936654, Reactome:R-MTU-879325, WikiPathways:WP5060, WikiPathways:WP5587,
    MIBiG:BGC0002072, and WikiPathways:WP296) and F-C12S4-002 (placeholder-reactome-and-mibig-reference-titles-4-records
    across Reactome:R-MTU-879299, Reactome:R-MTU-868688, Reactome:R-MTU-879325, and
    MIBiG:BGC0002072).'
  snapshot_sha256: 3b48a17bdc81244e86e7b367348c9f4d42e284b93f4122b5d52b76e47df089f2
- evidence_id: EV-C12S4-WORKFLOW-EVIDENCE
  kind: prior_review
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-04/revision-0001/evidence.yaml
  locator: findings[0..1] (F-C12S4-001, F-C12S4-002)
  accessed_at: '2026-11-05T15:55:00Z'
  support: supports
  summary: Cycle 12 Stage 4 workflow evidence manifest carried forward F-C12S4-001
    and F-C12S4-002 as open findings for Cycle 12 Stage 5 grouped remediation.
  snapshot_sha256: 87b916a21dc63c237a81de44bf63f4cf0b96af92c1a0d9ae6c82762402e8f0ee
- evidence_id: EV-C12S5-REF-URLS-FIXED-10
  kind: record_content
  reference: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
  locator: references[0..11].url in mycobacterium-trehalose-biosynthesis.yaml, references[0..11].url
    in mycothiol-biosynthesis.yaml, references[0..7].url in mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml,
    references[0..4].url in mycobacterium-sulfate-assimilation.yaml, references[0..2].url
    in mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml, references[0..1].url
    in mycothiol-catabolism.yaml, references[0..1].url in peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml,
    references[0].url in 2-phenylethanol-biosynthesis.yaml, references[0].url in linearmycin-biosynthetic-gene-cluster.yaml,
    and references[0].url in tca-cycle-detailed.yaml
  accessed_at: '2026-11-05T16:06:00Z'
  support: supports
  summary: Across all 10 maintained pathway records in F-C12S4-001, populated canonical
    resolvable url values on all 47 references[] entries (34 PubMed URLs, 12 Reactome
    reaction detail URLs, and 1 ChEBI URL) via pathwaymech.curation.publish_curation,
    achieving 116 / 116 (100.0%) reference URL coverage across the 10 reassessed records
    and 7,132 / 7,132 (100.0%) across the 281-record corpus.
  quote: "- id: Reactome:R-MTU-868622\n  title: Glucose is transferred from UDP-glucose\
    \ onto glucose-6-phosphate (Reactome:R-MTU-868622)\n  url: https://reactome.org/content/detail/R-MTU-868622"
  snapshot_sha256: 7e96c46849b5d4438f87c2e7ef8468ddd9e3736c90f1f56fbdc9674689d88330
- evidence_id: EV-C12S5-REF-TITLES-FIXED-4
  kind: record_content
  reference: data/pathways/mycothiol-biosynthesis.yaml
  locator: references[0..5].title in mycothiol-biosynthesis.yaml, references[0..4].title
    in mycobacterium-trehalose-biosynthesis.yaml, references[0].title in mycothiol-catabolism.yaml,
    and references[0].title in linearmycin-biosynthetic-gene-cluster.yaml
  accessed_at: '2026-11-05T16:06:00Z'
  support: supports
  summary: Across all 4 maintained pathway records in F-C12S4-002 (Reactome:R-MTU-879299,
    Reactome:R-MTU-868688, Reactome:R-MTU-879325, and MIBiG:BGC0002072), replaced
    all 13 generic placeholder references[].title entries with verified descriptive
    Reactome reaction titles (<reaction label> (<reference_id>)) and the verified
    PubMed article title for PMID:29348524 ('Linearmycins are lytic membrane-targeting
    antibiotics') via pathwaymech.curation.publish_curation.
  quote: "- id: Reactome:R-MTU-879331\n  title: glucose-6-phosphate is converted to\
    \ inositol-1-phosphate (Reactome:R-MTU-879331)\n  url: https://reactome.org/content/detail/R-MTU-879331"
  snapshot_sha256: ae877d4a8ec7fabe728669c180807547dfe9617c4479d10c3bf60a9229d5b05c
- evidence_id: EV-C12S5-PUBMED-29348524
  kind: record_content
  reference: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
  locator: references[0] (PMID:29348524)
  accessed_at: '2026-11-05T16:06:00Z'
  support: supports
  summary: Updated references[0] in MIBiG:BGC0002072 (linearmycin-biosynthetic-gene-cluster.yaml)
    with the verified peer-reviewed PubMed article title ('Linearmycins are lytic
    membrane-targeting antibiotics', Stubbendieck et al., J Antibiot 2018) and canonical
    PubMed URL (https://pubmed.ncbi.nlm.nih.gov/29348524/).
  quote: "- id: PMID:29348524\n  title: Linearmycins are lytic membrane-targeting\
    \ antibiotics\n  url: https://pubmed.ncbi.nlm.nih.gov/29348524/"
  snapshot_sha256: 8cae725a5c0caf991a2bc6e2bf5d53e9e2910816d66bdd16dba29e59ba6217cc
- evidence_id: EV-C12S5-RENDERED-PAGES
  kind: record_content
  reference: pages/records/Reactome_R-MTU-879299.html
  locator: 10 updated HTML pages in pages/records/ for the 10 remediated pathway records
  accessed_at: '2026-11-05T16:08:00Z'
  support: supports
  summary: After running .venv/bin/pathwaymech-render-pages, verified that all 10
    modified pathway record HTML pages in pages/records/ render clickable reference
    anchors with descriptive titles for all 47 newly populated URLs and 13 updated
    titles.
  snapshot_sha256: 77bd5c9f6fc6b01acd929937b49b7f9548d880a3ced8661c4d4ebd97a76088d2
- evidence_id: EV-C12S5-QC
  kind: validation
  reference: .venv/bin/pathwaymech-run-qc
  locator: stdout summary (281 pathway records, 1053 history records, 23,009 evidence
    blocks, 33 source records)
  accessed_at: '2026-11-05T16:10:00Z'
  support: supports
  summary: 'Executed .venv/bin/pathwaymech-run-qc: validated 281 pathway records against
    the closed LinkML schema, verified all identifiers and labels against local authority
    snapshots, validated 1,053 history records (including 10 new Cycle 12 Stage 5
    record history entries referencing issue #798) and 23,009 evidence blocks, and
    confirmed pages/ synchrony.'
- evidence_id: EV-C12S5-PYTEST
  kind: validation
  reference: TMPDIR=/tmp .venv/bin/pytest -p no:cacheprovider -q
  locator: pytest suite execution across tests/
  accessed_at: '2026-11-05T16:10:00Z'
  support: supports
  summary: Executed TMPDIR=/tmp .venv/bin/pytest -p no:cacheprovider -q across the
    full test suite.
- evidence_id: EV-C12S5-RUFF
  kind: validation
  reference: .venv/bin/ruff check --no-cache .
  locator: ruff check output
  accessed_at: '2026-11-05T16:10:00Z'
  support: supports
  summary: Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks
    passed).
- evidence_id: EV-C12S5-GIT-DIFF
  kind: validation
  reference: git diff --check
  locator: git worktree on feat/cycle12-stage5-resolve-review-findings
  accessed_at: '2026-11-05T16:10:00Z'
  support: supports
  summary: Executed git diff --check with exit code 0; no whitespace errors or conflict
    markers.
- evidence_id: EV-C12S5-REVIEW-CHECK
  kind: validation
  reference: TMPDIR=/tmp .venv/bin/python scripts/record_review.py check --base main
  locator: reviews/structured/
  accessed_at: '2026-11-05T16:10:00Z'
  support: supports
  summary: Validated all retained structured review bundles in reviews/structured/
    against schema/record_review.yaml and verified byte-for-byte append-only preservation
    against main.
assessments:
- assessment_id: ASSESS-C12S5-REFERENCE-HYGIENE-10
  area: consistency
  topic: Post-remediation completion of reference URL coverage (116 / 116 reassessed
    references; 7,132 / 7,132 corpus-wide) and elimination of placeholder Reactome/MIBiG
    reference titles (0 / 116 reassessed references; 0 / 7,132 corpus-wide)
  outcome: supported
  summary: Populating canonical resolvable url values across all 47 references[] entries
    in the 10 F-C12S4-001 records brings missing reference URLs to 0 / 116 across
    the 10 reassessed records and 0 / 7,132 across the entire 281-record corpus (100.0%
    reference URL coverage). Replacing all 13 placeholder references[].title entries
    across the 4 F-C12S4-002 records with verified descriptive Reactome reaction titles
    and the peer-reviewed PubMed article title for PMID:29348524 brings placeholder
    reference titles to 0 / 116 across the 10 reassessed records and 0 / 7,132 across
    the entire 281-record corpus.
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  evidence_ids:
  - EV-C12S4-PREDECESSOR
  - EV-C12S5-REF-URLS-FIXED-10
  - EV-C12S5-REF-TITLES-FIXED-4
  - EV-C12S5-PUBMED-29348524
  - EV-C12S5-RENDERED-PAGES
  - EV-C12S5-QC
  - EV-C12S5-PYTEST
  metrics:
  - name: missing_reference_urls_across_reassessed_records
    value: 0.0
    unit: references
    definition: Count of references[] entries omitting a resolvable url field across
      the 10 reassessed pathway records after populating 47 URLs (0 / 116 across the
      10 reassessed records; 0 / 7,132 across the 281-record corpus).
    denominator: 116
    minimum: 0.0
    maximum: 116.0
  - name: placeholder_reference_titles_across_reassessed_records
    value: 0.0
    unit: references
    definition: Count of references[] entries carrying generic 'Reactome reaction
      <id>' or 'MIBiG literature reference <id>' placeholder titles across the 10
      reassessed pathway records after replacing 13 titles across Reactome:R-MTU-879299
      (6), Reactome:R-MTU-868688 (5), Reactome:R-MTU-879325 (1), and MIBiG:BGC0002072
      (1) (0 / 116 across the 10 reassessed records; 0 / 7,132 across the 281-record
      corpus).
    denominator: 116
    minimum: 0.0
    maximum: 116.0
  dimensions:
  - name: rendered_page_verification
    value: All 47 populated reference URLs and 13 updated reference titles rendered
      across the 10 updated pages/records/*.html pages
    definition: Verified post-remediation rendered HTML pages in pages/records/.
    evidence_ids:
    - EV-C12S5-RENDERED-PAGES
    - EV-C12S5-QC
- assessment_id: ASSESS-C12S5-SCIENTIFIC-INTEGRITY-10
  area: evidence
  topic: Preservation of pathway identity, taxon grounding, participant connectivity,
    reaction directionality, stoichiometry, and edge-level evidence across the 10
    reassessed pathway records
  outcome: supported
  summary: Structural verification across all 10 reassessed pathway YAML files confirms
    that all pathway IDs, taxon groundings, 7,912 connected participant entries (0
    orphans), 1,640 reaction steps (740 RHEA:*), 14,814 non-reflexive mechanistic_edges,
    1,078 source_mappings, and 23,009 structured evidence blocks remain 100% intact
    and pass closed LinkML and authority snapshot checks.
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  evidence_ids:
  - EV-C12S5-REF-URLS-FIXED-10
  - EV-C12S5-REF-TITLES-FIXED-4
  - EV-C12S5-PUBMED-29348524
  - EV-C12S5-QC
  - EV-C12S5-PYTEST
  - EV-C12S5-GIT-DIFF
findings:
- finding_id: F-C12S4-001
  issue_key: missing-reference-urls-10-records
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: All 47 references[] entries omitting a resolvable url field across 10 maintained
    Reactome, WikiPathways, and MIBiG pathway records are populated with canonical
    URLs
  description: 'Across all 10 maintained pathway records in F-C12S4-001 (Reactome:R-MTU-868688
    mycobacterium-trehalose-biosynthesis.yaml: 12; Reactome:R-MTU-879299 mycothiol-biosynthesis.yaml:
    12; Reactome:R-MTU-936721 mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml:
    8; Reactome:R-MTU-936635 mycobacterium-sulfate-assimilation.yaml: 5; Reactome:R-MTU-936654
    mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml: 3; Reactome:R-MTU-879325
    mycothiol-catabolism.yaml: 2; WikiPathways:WP5060 peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml:
    2; WikiPathways:WP5587 2-phenylethanol-biosynthesis.yaml: 1; MIBiG:BGC0002072
    linearmycin-biosynthetic-gene-cluster.yaml: 1; and WikiPathways:WP296 tca-cycle-detailed.yaml:
    1), populated canonical resolvable url values across all 47 references[] entries
    (34 PubMed URLs, 12 Reactome reaction detail URLs, and 1 ChEBI URL) via pathwaymech.curation.publish_curation,
    recorded 10 history/records/<slug>/2026-11-05T160500Z-antigravity-*.yaml files,
    and regenerated pages/ under root-cause group G-C12S5-001 (#798).'
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  field_paths:
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[0].url (Reactome:R-MTU-868622)
    (None -> https://reactome.org/content/detail/R-MTU-868622)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[1].url (Reactome:R-MTU-868608)
    (None -> https://reactome.org/content/detail/R-MTU-868608)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[2].url (Reactome:R-MTU-868709)
    (None -> https://reactome.org/content/detail/R-MTU-868709)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[3].url (Reactome:R-MTU-868658)
    (None -> https://reactome.org/content/detail/R-MTU-868658)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[4].url (Reactome:R-MTU-868657)
    (None -> https://reactome.org/content/detail/R-MTU-868657)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[5].url (PMID:10658666)
    (None -> https://pubmed.ncbi.nlm.nih.gov/10658666/)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[6].url (PMID:12473104)
    (None -> https://pubmed.ncbi.nlm.nih.gov/12473104/)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[7].url (PMID:15158675)
    (None -> https://pubmed.ncbi.nlm.nih.gov/15158675/)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[8].url (PMID:19177348)
    (None -> https://pubmed.ncbi.nlm.nih.gov/19177348/)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[9].url (PMID:15703182)
    (None -> https://pubmed.ncbi.nlm.nih.gov/15703182/)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[10].url (PMID:12626396)
    (None -> https://pubmed.ncbi.nlm.nih.gov/12626396/)
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[11].url (PMID:15901732)
    (None -> https://pubmed.ncbi.nlm.nih.gov/15901732/)
  - data/pathways/mycothiol-biosynthesis.yaml#references[0].url (Reactome:R-MTU-879331)
    (None -> https://reactome.org/content/detail/R-MTU-879331)
  - data/pathways/mycothiol-biosynthesis.yaml#references[1].url (Reactome:R-MTU-879298)
    (None -> https://reactome.org/content/detail/R-MTU-879298)
  - data/pathways/mycothiol-biosynthesis.yaml#references[2].url (Reactome:R-MTU-879274)
    (None -> https://reactome.org/content/detail/R-MTU-879274)
  - data/pathways/mycothiol-biosynthesis.yaml#references[3].url (Reactome:R-MTU-879327)
    (None -> https://reactome.org/content/detail/R-MTU-879327)
  - data/pathways/mycothiol-biosynthesis.yaml#references[4].url (Reactome:R-MTU-879319)
    (None -> https://reactome.org/content/detail/R-MTU-879319)
  - data/pathways/mycothiol-biosynthesis.yaml#references[5].url (Reactome:R-MTU-879248)
    (None -> https://reactome.org/content/detail/R-MTU-879248)
  - data/pathways/mycothiol-biosynthesis.yaml#references[6].url (PMID:14763976) (None
    -> https://pubmed.ncbi.nlm.nih.gov/14763976/)
  - data/pathways/mycothiol-biosynthesis.yaml#references[7].url (PMID:18390549) (None
    -> https://pubmed.ncbi.nlm.nih.gov/18390549/)
  - data/pathways/mycothiol-biosynthesis.yaml#references[8].url (PMID:20167072) (None
    -> https://pubmed.ncbi.nlm.nih.gov/20167072/)
  - data/pathways/mycothiol-biosynthesis.yaml#references[9].url (PMID:14556638) (None
    -> https://pubmed.ncbi.nlm.nih.gov/14556638/)
  - data/pathways/mycothiol-biosynthesis.yaml#references[10].url (PMID:12033919) (None
    -> https://pubmed.ncbi.nlm.nih.gov/12033919/)
  - data/pathways/mycothiol-biosynthesis.yaml#references[11].url (PMID:12375100) (None
    -> https://pubmed.ncbi.nlm.nih.gov/12375100/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml#references[0].url
    (PMID:12072441) (None -> https://pubmed.ncbi.nlm.nih.gov/12072441/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml#references[1].url
    (PMID:16008502) (None -> https://pubmed.ncbi.nlm.nih.gov/16008502/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml#references[2].url
    (PMID:17644602) (None -> https://pubmed.ncbi.nlm.nih.gov/17644602/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml#references[3].url
    (PMID:15917234) (None -> https://pubmed.ncbi.nlm.nih.gov/15917234/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml#references[4].url
    (PMID:17567578) (None -> https://pubmed.ncbi.nlm.nih.gov/17567578/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml#references[5].url
    (PMID:16436075) (None -> https://pubmed.ncbi.nlm.nih.gov/16436075/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml#references[6].url
    (PMID:19376862) (None -> https://pubmed.ncbi.nlm.nih.gov/19376862/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml#references[7].url
    (PMID:17970225) (None -> https://pubmed.ncbi.nlm.nih.gov/17970225/)
  - data/pathways/mycobacterium-sulfate-assimilation.yaml#references[0].url (PMID:11929522)
    (None -> https://pubmed.ncbi.nlm.nih.gov/11929522/)
  - data/pathways/mycobacterium-sulfate-assimilation.yaml#references[1].url (PMID:15184554)
    (None -> https://pubmed.ncbi.nlm.nih.gov/15184554/)
  - data/pathways/mycobacterium-sulfate-assimilation.yaml#references[2].url (PMID:15615729)
    (None -> https://pubmed.ncbi.nlm.nih.gov/15615729/)
  - data/pathways/mycobacterium-sulfate-assimilation.yaml#references[3].url (PMID:18454554)
    (None -> https://pubmed.ncbi.nlm.nih.gov/18454554/)
  - data/pathways/mycobacterium-sulfate-assimilation.yaml#references[4].url (PMID:17970225)
    (None -> https://pubmed.ncbi.nlm.nih.gov/17970225/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml#references[0].url
    (PMID:16104727) (None -> https://pubmed.ncbi.nlm.nih.gov/16104727/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml#references[1].url
    (PMID:18842002) (None -> https://pubmed.ncbi.nlm.nih.gov/18842002/)
  - data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml#references[2].url
    (PMID:18799456) (None -> https://pubmed.ncbi.nlm.nih.gov/18799456/)
  - data/pathways/mycothiol-catabolism.yaml#references[0].url (Reactome:R-MTU-879281)
    (None -> https://reactome.org/content/detail/R-MTU-879281)
  - data/pathways/mycothiol-catabolism.yaml#references[1].url (PMID:14556638) (None
    -> https://pubmed.ncbi.nlm.nih.gov/14556638/)
  - data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml#references[0].url
    (PMID:31296364) (None -> https://pubmed.ncbi.nlm.nih.gov/31296364/)
  - data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml#references[1].url
    (PMID:18266853) (None -> https://pubmed.ncbi.nlm.nih.gov/18266853/)
  - data/pathways/2-phenylethanol-biosynthesis.yaml#references[0].url (PMID:40724265)
    (None -> https://pubmed.ncbi.nlm.nih.gov/40724265/)
  - data/pathways/linearmycin-biosynthetic-gene-cluster.yaml#references[0].url (PMID:29348524)
    (None -> https://pubmed.ncbi.nlm.nih.gov/29348524/)
  - data/pathways/tca-cycle-detailed.yaml#references[0].url (CHEBI:30744) (None ->
    https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:30744)
  evidence_ids:
  - EV-C12S4-PREDECESSOR
  - EV-C12S4-WORKFLOW-EVIDENCE
  - EV-C12S5-REF-URLS-FIXED-10
  - EV-C12S5-RENDERED-PAGES
  - EV-C12S5-QC
  - EV-C12S5-PYTEST
  rule_id: CURATION:reference-entries-include-resolvable-url
  native_severity: minor
  normalization_reason: 'Native minor reference-metadata representation finding maps
    directly to minor severity: populating all 47 missing reference URLs across the
    10 affected pathway records achieves 100.0% reference URL coverage across all
    7,132 references in the 281-record corpus.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycothiol-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-sulfate-assimilation.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycothiol-catabolism.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-phenylethanol-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/tca-cycle-detailed.yaml
    role: maintained pathway YAML
  disposition_reason: 'Resolved under GitHub issue #798 (group G-C12S5-001) by populating
    canonical resolvable url values across all 47 references[] entries in the 10 affected
    pathway records (34 PubMed URLs https://pubmed.ncbi.nlm.nih.gov/<pmid>/, 12 Reactome
    reaction detail URLs https://reactome.org/content/detail/<id>, and 1 ChEBI URL
    https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:30744) via pathwaymech.curation.publish_curation
    (with 10 history files and regenerated pages/).'
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review
    finding_id: F-C12S4-001
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/798
  tags:
  - cycle12-stage5-resolve-review-findings
  - reference-url-hygiene
- finding_id: F-C12S4-002
  issue_key: placeholder-reactome-and-mibig-reference-titles-4-records
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: All 13 generic placeholder references[].title strings across Reactome:R-MTU-879299,
    Reactome:R-MTU-868688, Reactome:R-MTU-879325, and MIBiG:BGC0002072 are replaced
    with descriptive reaction and peer-reviewed article titles
  description: 'Across all 4 maintained pathway records in F-C12S4-002 (Reactome:R-MTU-879299
    mycothiol-biosynthesis.yaml: 6; Reactome:R-MTU-868688 mycobacterium-trehalose-biosynthesis.yaml:
    5; Reactome:R-MTU-879325 mycothiol-catabolism.yaml: 1; and MIBiG:BGC0002072 linearmycin-biosynthetic-gene-cluster.yaml:
    1), replaced all 13 generic placeholder references[].title entries (''Reactome
    reaction <id>'' and ''MIBiG literature reference PMID:29348524'') with verified
    descriptive Reactome reaction titles (<reaction label> (<reference_id>)) and the
    verified PubMed article title for PMID:29348524 (''Linearmycins are lytic membrane-targeting
    antibiotics'') via pathwaymech.curation.publish_curation, recorded curation history
    files, and regenerated pages/ under root-cause group G-C12S5-001 (#798).'
  target_ids:
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879325
  - MIBiG:BGC0002072
  field_paths:
  - data/pathways/mycothiol-biosynthesis.yaml#references[0].title (Reactome:R-MTU-879331)
    (Reactome reaction R-MTU-879331 -> glucose-6-phosphate is converted to inositol-1-phosphate
    (Reactome:R-MTU-879331))
  - data/pathways/mycothiol-biosynthesis.yaml#references[1].title (Reactome:R-MTU-879298)
    (Reactome reaction R-MTU-879298 -> acetylglucosamine is transferred from UDP-GlcNAc
    onto inositol-1-phosphate (Reactome:R-MTU-879298))
  - data/pathways/mycothiol-biosynthesis.yaml#references[2].title (Reactome:R-MTU-879274)
    (Reactome reaction R-MTU-879274 -> acetylglucosamine-inositol-phosphate is dephosphorylated
    (Reactome:R-MTU-879274))
  - data/pathways/mycothiol-biosynthesis.yaml#references[3].title (Reactome:R-MTU-879327)
    (Reactome reaction R-MTU-879327 -> acetylglucosamine-inositol is deacetylated
    by Mca (Reactome:R-MTU-879327))
  - data/pathways/mycothiol-biosynthesis.yaml#references[4].title (Reactome:R-MTU-879319)
    (Reactome reaction R-MTU-879319 -> glucosaminyl-inositol and cysteine are ligated
    to desacetylmycothiol (Reactome:R-MTU-879319))
  - data/pathways/mycothiol-biosynthesis.yaml#references[5].title (Reactome:R-MTU-879248)
    (Reactome reaction R-MTU-879248 -> desacetylmycothiol is acetylated to mycothiol
    using acetyl-CoA (Reactome:R-MTU-879248))
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[0].title (Reactome:R-MTU-868622)
    (Reactome reaction R-MTU-868622 -> Glucose is transferred from UDP-glucose onto
    glucose-6-phosphate (Reactome:R-MTU-868622))
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[1].title (Reactome:R-MTU-868608)
    (Reactome reaction R-MTU-868608 -> Trehalose-6-phosphate is hydrolyzed to trehalose
    (Reactome:R-MTU-868608))
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[2].title (Reactome:R-MTU-868709)
    (Reactome reaction R-MTU-868709 -> TreS interconverts trehalose and alpha-maltose
    (physiological trehalose consumption) (Reactome:R-MTU-868709))
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[3].title (Reactome:R-MTU-868658)
    (Reactome reaction R-MTU-868658 -> 1,4-alpha-glucan is converted to glucanotrehalose
    (Reactome:R-MTU-868658))
  - data/pathways/mycobacterium-trehalose-biosynthesis.yaml#references[4].title (Reactome:R-MTU-868657)
    (Reactome reaction R-MTU-868657 -> Glucanotrehalose is hydrolyzed to 1,4-alpha-glucan
    and trehalose (Reactome:R-MTU-868657))
  - data/pathways/mycothiol-catabolism.yaml#references[0].title (Reactome:R-MTU-879281)
    (Reactome reaction R-MTU-879281 -> Mca hydrolyzes mycothiol S-conjugates to mercapturic-acid
    conjugates and glucosaminyl-inositol (Reactome:R-MTU-879281))
  - data/pathways/linearmycin-biosynthetic-gene-cluster.yaml#references[0].title (PMID:29348524)
    (MIBiG literature reference PMID:29348524 -> Linearmycins are lytic membrane-targeting
    antibiotics)
  evidence_ids:
  - EV-C12S4-PREDECESSOR
  - EV-C12S4-WORKFLOW-EVIDENCE
  - EV-C12S5-REF-TITLES-FIXED-4
  - EV-C12S5-PUBMED-29348524
  - EV-C12S5-RENDERED-PAGES
  - EV-C12S5-QC
  - EV-C12S5-PYTEST
  rule_id: CURATION:no-placeholder-reference-titles
  native_severity: minor
  normalization_reason: 'Native minor reference-title representation finding maps
    directly to minor severity: replacing all 13 generic placeholder reference titles
    across the 4 affected pathway records eliminates all placeholder ''Reactome reaction
    <id>'' and ''MIBiG literature reference <id>'' titles across the 281-record corpus.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycothiol-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycothiol-catabolism.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
    role: maintained pathway YAML
  disposition_reason: 'Resolved under GitHub issue #798 (group G-C12S5-001) by replacing
    all 13 generic placeholder references[].title entries across Reactome:R-MTU-879299
    (6), Reactome:R-MTU-868688 (5), Reactome:R-MTU-879325 (1), and MIBiG:BGC0002072
    (1) with verified descriptive Reactome reaction titles and the peer-reviewed PubMed
    article title for PMID:29348524 via pathwaymech.curation.publish_curation (with
    history files and regenerated pages/).'
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review
    finding_id: F-C12S4-002
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/798
  tags:
  - cycle12-stage5-resolve-review-findings
  - reference-title-hygiene
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-879325
  - WikiPathways:WP5060
  - WikiPathways:WP5587
  - MIBiG:BGC0002072
  - WikiPathways:WP296
  rationale: Retain all 10 reassessed pathway records as distinct, non-duplicate source-scoped
    pathway definitions with 100.0% reference URL coverage (116 / 116 across reassessed
    records; 7,132 / 7,132 corpus-wide) and 0 placeholder reference titles (0 / 116
    across reassessed records; 0 / 7,132 corpus-wide).
  evidence_ids:
  - EV-C12S5-REF-URLS-FIXED-10
  - EV-C12S5-REF-TITLES-FIXED-4
  - EV-C12S5-PUBMED-29348524
  - EV-C12S5-QC
limitations:
- This Cycle 12 Stage 5 successor review is scoped to verifying the remediation of
  Cycle 12 Stage 4 findings F-C12S4-001 and F-C12S4-002 across the 10 affected maintained
  pathway records; the remaining 271 maintained records had zero findings in Cycle
  12 Stage 4 and were verified via repository-wide QC and pytest gates.
notes:
- CLAW aggregator CLI (kg_microbe_reviews) is not installed in the local culturebotai-claw
  environment; finding lineage (predecessor review_id 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review,
  finding_ids F-C12S4-001 and F-C12S4-002, exact issue_keys, 100% target_ids retention,
  and absence of competing heads) was explicitly verified against reviews/structured/.
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review
  relationship: resolves_findings_from
links:
- https://github.com/CultureBotAI/PathwayMech/issues/798
tags:
- mech-goal-sequence-20261019
- cycle-12
- stage-5
- resolve-review-findings
```
