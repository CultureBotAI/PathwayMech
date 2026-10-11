# Partial independent galactonate review: two figure locator defects

- Review: 20261011T043907Z-galactonate-initial-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T04:37:00Z
- Finished UTC: 2026-10-11T04:39:07Z
- Reviewer: Codex independent reviewer (/root/pathway_literature_candidates) (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Two confirmed minor figure-locator defects require correction. Original primary sections support the associated growth and effector assertions. Complete independent native chemistry/identity replay and final shared gates are still pending.

## Scope And Provenance

Complete target read; bounded primary-source figure/section and experimental-scope assessment.

Selection: Exactly the assigned frozen GALACTCAT-PWY record at SHA5672802eca1a1f61c2fb08fe29b89899eafe8e1e96e868f7a26449de7ef9a5b8.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7bab6407d811db928abe049854ccb6107e591a3e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:GALACTCAT-PWY | data/pathways/d-galactonate-degradation.yaml | maintained | D-galactonate degradation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical inspect before assessment | passed | True | MetaCyc:GALACTCAT-PWY | Initial target captured before assessment; context inputs separately inspected without target changes. |
| Whitespace check | passed | True | MetaCyc:GALACTCAT-PWY | Actual command exited zero. |
| just validate | unavailable | True | MetaCyc:GALACTCAT-PWY | Root shared gates are running; no terminal result relied upon at this partial observation. |
| just test | unavailable | True | MetaCyc:GALACTCAT-PWY | Root shared gates are running; no terminal result relied upon at this partial observation. |
| just lint | unavailable | True | MetaCyc:GALACTCAT-PWY | Root shared gates are running; no terminal result relied upon at this partial observation. |

## Scientific And Domain Assessments

### Strain and conditional primary observations

scope: supported. Targets: MetaCyc:GALACTCAT-PWY.

Inspected original sections support BW25113 knockout growth and conditional D-galactonate inhibition of DgoR DNA binding, without extending that evidence to purified DgoD/DgoK catalysis.

### Exact figure attribution

provenance: concern. Targets: MetaCyc:GALACTCAT-PWY.

Two figure references need exact correction; the corresponding source sections support the scientific assertions.

## Findings

### f-growth-figure: Knockout-growth locator cites the pathway cartoon

minor / open / confirmed; issue key: galactonate-growth-figure-locator.

Edge025 cites Fig.1B for loss of growth of dgoD/dgoK/dgoA deletions, but original Results #s2.1 and Fig.1 caption place growth spots in Fig.1C. The cited section itself supports the assertion.

### f-effector-figure: Effector-response locator cites the wrong figure

minor / open / confirmed; issue key: galactonate-effector-figure-locator.

Edge027 cites Fig.7 for D-galactonate-dependent DNA release and altered proteolysis; original Results #s2.7 explicitly places these observations in Fig.8A/B and Fig.8C.

## Recommended Actions And Acceptance Checks

### a-fix-growth

Correct the exact figure locator in the maintained record and refresh affected author receipts/generated outputs.

- Compare corrected locator directly with original PMC6351737 section and caption.
- Reinspect changed input bytes and preserve this finding lineage in a successor review after final shared gates.

### a-fix-effector

Correct the exact figure locator in the maintained record and refresh affected author receipts/generated outputs.

- Compare corrected locator directly with original PMC6351737 section and caption.
- Reinspect changed input bytes and preserve this finding lineage in a successor review after final shared gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-target | data/pathways/d-galactonate-degradation.yaml; Entire record; edges025 and027 | refutes | Complete target read. Two figure locators mismatch the original body; section locators and scientific assertions are supported. |
| e-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC6351737/; Results #s2.1; figure #F1 caption; Results #s2.7 and Fig.8 caption; Methods #s4.3, #s4.9, #s4.12 | supports | Original body identifies knockout-growth experiments as Fig.1C and galactonate-dependent EMSA/proteolysis as Fig.8A-C. Fig.1B is the pathway cartoon. Relevant Results sections support the retained strain/conditional effects. |

## Limits And Additional Notes

- This is a partial review, not a completed whole-record pass. Native source chemistry, all identifiers and complete independent evidence attachment checks remain in progress.
- Final shared validate/test/lint outputs were pending at save time; no passing exit is claimed.
- No iModulon context conclusion is made in this partial observation.
- Initial target and inspected context bytes are retained externally for historical replay. No author-owned record or source files were edited by the reviewer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T043907Z-galactonate-initial-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: 'Partial independent galactonate review: two figure locator defects'
started_at: '2026-10-11T04:37:00Z'
finished_at: '2026-10-11T04:39:07Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_literature_candidates)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer did not author this target or its dossiers. Entire
    target and cited primary sections were independently read; reviewer-authored phenylethylamine-II
    is outside this review.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: Two confirmed minor figure-locator defects require correction. Original primary
  sections support the associated growth and effector assertions. Complete independent
  native chemistry/identity replay and final shared gates are still pending.
source:
  git_revision: 7bab6407d811db928abe049854ccb6107e591a3e
  state: working_tree
  inputs:
  - path: data/pathways/d-galactonate-degradation.yaml
    sha256: 5672802eca1a1f61c2fb08fe29b89899eafe8e1e96e868f7a26449de7ef9a5b8
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 3c861f2ab78e3bc62146d05af5ed5c4c4ae3e65343fc9bd44afa76da7f0b62e7
    role: context
  - path: research/pathway_additions/2026-10-11-next-189/galactonate-source-manifest.json
    sha256: ea4fb7ae23605820fa7b9fa2eecb4b787057d80af939cea22eb4e0decbe3b0f2
    role: context
  - path: research/pathway_additions/2026-10-11-next-189/galactonate-source-projection.json
    sha256: b6120f0aa8144d8efd8c9119de19bb026ba1184f756dab0bad32e28f0f811e79
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
targets:
- target_id: MetaCyc:GALACTCAT-PWY
  path: data/pathways/d-galactonate-degradation.yaml
  label: D-galactonate degradation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galactonate-degradation.yaml
    role: maintained_record
scope:
  description: Complete target read; bounded primary-source figure/section and experimental-scope
    assessment.
  selection: Exactly the assigned frozen GALACTCAT-PWY record at SHA5672802eca1a1f61c2fb08fe29b89899eafe8e1e96e868f7a26449de7ef9a5b8.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:GALACTCAT-PWY
  exclusions:
  - target: Remaining native/Rhea/ChEBI all-edge replay and shared final gates
    reason: Still pending; follow-up review will assess the corrected frozen surface.
  - target: Other pathway records
    reason: Outside one-record scientific scope.
checks:
- check_id: inspect
  name: Canonical inspect before assessment
  command: .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-189-galactonate-review/targets.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Initial target captured before assessment; context inputs separately inspected
    without target changes.
  target_ids:
  - MetaCyc:GALACTCAT-PWY
- check_id: diff
  name: Whitespace check
  command: git diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Actual command exited zero.
  target_ids:
  - MetaCyc:GALACTCAT-PWY
- check_id: just-validate
  name: just validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  status: unavailable
  required: true
  summary: Root shared gates are running; no terminal result relied upon at this partial
    observation.
  target_ids:
  - MetaCyc:GALACTCAT-PWY
- check_id: just-test
  name: just test
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: unavailable
  required: true
  summary: Root shared gates are running; no terminal result relied upon at this partial
    observation.
  target_ids:
  - MetaCyc:GALACTCAT-PWY
- check_id: just-lint
  name: just lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  status: unavailable
  required: true
  summary: Root shared gates are running; no terminal result relied upon at this partial
    observation.
  target_ids:
  - MetaCyc:GALACTCAT-PWY
evidence:
- evidence_id: e-target
  kind: record_content
  reference: data/pathways/d-galactonate-degradation.yaml
  locator: Entire record; edges025 and027
  accessed_at: '2026-10-11T04:39:07Z'
  support: refutes
  summary: Complete target read. Two figure locators mismatch the original body; section
    locators and scientific assertions are supported.
  snapshot_sha256: 5672802eca1a1f61c2fb08fe29b89899eafe8e1e96e868f7a26449de7ef9a5b8
- evidence_id: e-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6351737/
  locator: 'Results #s2.1; figure #F1 caption; Results #s2.7 and Fig.8 caption; Methods
    #s4.3, #s4.9, #s4.12'
  accessed_at: '2026-10-11T04:39:07Z'
  support: supports
  summary: Original body identifies knockout-growth experiments as Fig.1C and galactonate-dependent
    EMSA/proteolysis as Fig.8A-C. Fig.1B is the pathway cartoon. Relevant Results
    sections support the retained strain/conditional effects.
  snapshot_sha256: 1bab347e98dafa6dfb04253e6b080cad78cff4b2c6139a1b77e6ff29509fec07
assessments:
- assessment_id: a-primary-scope
  area: scope
  topic: Strain and conditional primary observations
  outcome: supported
  summary: Inspected original sections support BW25113 knockout growth and conditional
    D-galactonate inhibition of DgoR DNA binding, without extending that evidence
    to purified DgoD/DgoK catalysis.
  target_ids:
  - MetaCyc:GALACTCAT-PWY
  evidence_ids:
  - e-primary
- assessment_id: a-locators
  area: provenance
  topic: Exact figure attribution
  outcome: concern
  summary: Two figure references need exact correction; the corresponding source sections
    support the scientific assertions.
  target_ids:
  - MetaCyc:GALACTCAT-PWY
  evidence_ids:
  - e-target
  - e-primary
findings:
- finding_id: f-growth-figure
  issue_key: galactonate-growth-figure-locator
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Knockout-growth locator cites the pathway cartoon
  description: 'Edge025 cites Fig.1B for loss of growth of dgoD/dgoK/dgoA deletions,
    but original Results #s2.1 and Fig.1 caption place growth spots in Fig.1C. The
    cited section itself supports the assertion.'
  target_ids:
  - MetaCyc:GALACTCAT-PWY
  field_paths:
  - mechanistic_edges[id=galactonate-edge-025]/evidence[reference_id=PMID:30455279]/source_locator
  evidence_ids:
  - e-target
  - e-primary
  rule_id: review-yaml-record Evidence Rules; docs/CAUSAL_GRAPHS.md precise source
    locators
  native_severity: minor
  normalization_reason: 'Bounded provenance defect: scientific assertion is supported
    by the correctly named source section, but the exact figure locator is wrong.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galactonate-degradation.yaml
    role: maintained_record
- finding_id: f-effector-figure
  issue_key: galactonate-effector-figure-locator
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Effector-response locator cites the wrong figure
  description: 'Edge027 cites Fig.7 for D-galactonate-dependent DNA release and altered
    proteolysis; original Results #s2.7 explicitly places these observations in Fig.8A/B
    and Fig.8C.'
  target_ids:
  - MetaCyc:GALACTCAT-PWY
  field_paths:
  - mechanistic_edges[id=galactonate-edge-027]/evidence[reference_id=PMID:30455279]/source_locator
  evidence_ids:
  - e-target
  - e-primary
  rule_id: review-yaml-record Evidence Rules; docs/CAUSAL_GRAPHS.md precise source
    locators
  native_severity: minor
  normalization_reason: 'Bounded provenance defect: scientific assertion is supported
    by the correctly named source section, but the exact figure locator is wrong.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galactonate-degradation.yaml
    role: maintained_record
actions:
- action_id: a-fix-growth
  description: Correct the exact figure locator in the maintained record and refresh
    affected author receipts/generated outputs.
  finding_ids:
  - f-growth-figure
  target_ids:
  - MetaCyc:GALACTCAT-PWY
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galactonate-degradation.yaml
    role: maintained_record
  acceptance_checks:
  - Compare corrected locator directly with original PMC6351737 section and caption.
  - Reinspect changed input bytes and preserve this finding lineage in a successor
    review after final shared gates.
- action_id: a-fix-effector
  description: Correct the exact figure locator in the maintained record and refresh
    affected author receipts/generated outputs.
  finding_ids:
  - f-effector-figure
  target_ids:
  - MetaCyc:GALACTCAT-PWY
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galactonate-degradation.yaml
    role: maintained_record
  acceptance_checks:
  - Compare corrected locator directly with original PMC6351737 section and caption.
  - Reinspect changed input bytes and preserve this finding lineage in a successor
    review after final shared gates.
limitations:
- This is a partial review, not a completed whole-record pass. Native source chemistry,
  all identifiers and complete independent evidence attachment checks remain in progress.
- Final shared validate/test/lint outputs were pending at save time; no passing exit
  is claimed.
- No iModulon context conclusion is made in this partial observation.
notes:
- Initial target and inspected context bytes are retained externally for historical
  replay. No author-owned record or source files were edited by the reviewer.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/352
```
