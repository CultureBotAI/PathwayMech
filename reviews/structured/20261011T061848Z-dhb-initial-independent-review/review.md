# Initial independent DHB review: EntA historical source locator

- Review: 20261011T061848Z-dhb-initial-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T06:14:11Z
- Finished UTC: 2026-10-11T06:18:48Z
- Reviewer: Codex independent reviewer (/root/verify_graph_publication) (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor citation locator defect: the EntA octamer Discussion is printed page 796, not page 797. The separately cited Results page 795 already supports the scientific assertion. Full source replay and coordinated final gates are pending; this observation preserves the original finding before correction.

## Scope And Provenance

One entire DHB target read and original primary/structured sources inspected; this partial observation preserves a confirmed page locator finding.

Selection: Exact native complete PWY-5901 at SHA94a671009cfae9c61381d26067a07e80edaeb5d6e4f73a00ae8c81bfb35b1144
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d776b82c9c598bb79885ad01514b07900a678de0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5901 | data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml | maintained | 2,3-dihydroxybenzoate biosynthesis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| inspect | passed | True | MetaCyc:PWY-5901 | Canonical inspect ran before assessment and captured exact target/source inputs. |
| just-validate | unavailable | True | MetaCyc:PWY-5901 | Coordinated root checks in progress; complete actual receipt not inspected for this partial observation. |
| just-test | unavailable | True | MetaCyc:PWY-5901 | Coordinated root checks in progress; complete actual receipt not inspected for this partial observation. |
| just-lint | unavailable | True | MetaCyc:PWY-5901 | Coordinated root checks in progress; complete actual receipt not inspected for this partial observation. |
| diff | unavailable | True | MetaCyc:PWY-5901 | Final coordinated receipt has not yet been inspected. |

## Scientific And Domain Assessments

### Exact primary page location for historical EntA assembly conflict

provenance: concern. Targets: MetaCyc:PWY-5901.

Scientific assertion supported at the correctly cited Results page; the second locator must change from printed p797 to p796.

## Findings

### f-enta-discussion-page: Historical EntA octamer Discussion page is 796, not 797

minor / open / confirmed; issue key: dhb-enta-octamer-discussion-page.

dhb-edge-015 PMID:2521622 evidence locates Discussion on printed p797. Original PDF places that octamer discussion at printed p796. Correctly cited Results p795 already supports the assertion; no chemistry or assembly change requested. Matching projected evidence in dhb-source-projection.json should follow the correction.

## Recommended Actions And Acceptance Checks

### correct-page

Replace p.797 Discussion with p.796 Discussion in the maintained evidence; refresh corresponding projection/replay and generated outputs, then preserve this finding lineage in a successor review.

- Visually compare final locator with original PDF printed pages795–797.
- Verify only bounded locator/provenance changes and run final source replay and coordinated corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-target | data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml; Complete target; dhb-edge-015 evidence reference PMID:2521622/source_locator | refutes | Locator includes correct Results p795 but incorrectly names Discussion p797. |
| e-primary | https://europepmc.org/articles/PMC209666?pdf=render; Printed p795 Results/Purification of diDHB-DH; printed p796 Discussion, lower right column; printed p797 inspected as contrast | supports | Independently extracted original PDF with pypdfium2 and rendered pages 795,796,797. The 210000 molecular-mass/octamer result is on p795, repeated in Discussion on p796. Page797 discusses EntC and references, not the octamer result. |

## Limits And Additional Notes

- Partial observation; complete independent source replay and full coordinated gates not yet accepted.
- Primary abstract-only scope and qualified EntB/EntA assembly distinctions remain part of the ongoing scientific review.
- Initial canonical inspection completed time is used as review start; original target and source inputs remain unchanged for this save.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T061848Z-dhb-initial-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: 'Initial independent DHB review: EntA historical source locator'
started_at: '2026-10-11T06:14:11Z'
finished_at: '2026-10-11T06:18:48Z'
reviewer:
  identity: Codex independent reviewer (/root/verify_graph_publication)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Did not author DHB or its dossiers; authored menaquinol in the
    same cohort, excluded from this review. Read complete DHB target and original
    primary/database evidence independently.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One minor citation locator defect: the EntA octamer Discussion is printed
  page 796, not page 797. The separately cited Results page 795 already supports the
  scientific assertion. Full source replay and coordinated final gates are pending;
  this observation preserves the original finding before correction.'
source:
  git_revision: d776b82c9c598bb79885ad01514b07900a678de0
  state: working_tree
  inputs:
  - path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    sha256: 94a671009cfae9c61381d26067a07e80edaeb5d6e4f73a00ae8c81bfb35b1144
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: c635a91493a53b519ed2c8e0f825adcca320e1c8d96ef87a69459c8a2cb14937
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 3af37b2e92b0103da74bc462bedda1021c6bd262d3da13c030eb47344d08b61f
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-curation.md
    sha256: b38a12b8d00703d18cb1207e8adb2432f78289db89fbfa6709ba2ff364d88df2
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-dedup.json
    sha256: 1766ee8819662a07fef302275f229cefe36cc65db9e459143835f829a9c8ab56
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-identifiers.json
    sha256: f8e4cf3ee5bdebe7bad4aec5660066bb5e9e83a43b53220ec31bdcb2caf86b1a
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-source-manifest.json
    sha256: f0f48dcc3620d236da9b21da969937fb6b8afa66470011d03db686fb5724c49b
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-source-projection.json
    sha256: a6f3ee0e1361115a6456244f0af251cdbd8f5b9d7a8a37154068b20cfc2e563e
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-validation.json
    sha256: 44640f37a16c7eaf8f8bf504cfab3404e46fb7a2a786feff86fd979f9f679b28
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
targets:
- target_id: MetaCyc:PWY-5901
  path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
  label: 2,3-dihydroxybenzoate biosynthesis
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    role: maintained pathway record
scope:
  description: One entire DHB target read and original primary/structured sources
    inspected; this partial observation preserves a confirmed page locator finding.
  selection: Exact native complete PWY-5901 at SHA94a671009cfae9c61381d26067a07e80edaeb5d6e4f73a00ae8c81bfb35b1144
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5901
  exclusions:
  - target: Other cohort records and final coordinated gates
    reason: Outside this partial scientific observation or still in progress.
checks:
- check_id: inspect
  name: inspect
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-195-dhb-review-targets.yaml
    --input research/pathway_additions/2026-10-11-next-195/dhb-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-195/dhb-source-projection.json
    --input research/pathway_additions/2026-10-11-next-195/dhb-curation.md --input
    research/pathway_additions/2026-10-11-next-195/dhb-identifiers.json --input research/pathway_additions/2026-10-11-next-195/dhb-dedup.json
    --input research/pathway_additions/2026-10-11-next-195/dhb-validation.json --input
    src/pathwaymech/schema.py --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/CAUSAL_GRAPHS.md
  status: passed
  required: true
  summary: Canonical inspect ran before assessment and captured exact target/source
    inputs.
  target_ids:
  - MetaCyc:PWY-5901
  exit_code: 0
- check_id: just-validate
  name: just-validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  status: unavailable
  required: true
  summary: Coordinated root checks in progress; complete actual receipt not inspected
    for this partial observation.
  target_ids:
  - MetaCyc:PWY-5901
- check_id: just-test
  name: just-test
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: unavailable
  required: true
  summary: Coordinated root checks in progress; complete actual receipt not inspected
    for this partial observation.
  target_ids:
  - MetaCyc:PWY-5901
- check_id: just-lint
  name: just-lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  status: unavailable
  required: true
  summary: Coordinated root checks in progress; complete actual receipt not inspected
    for this partial observation.
  target_ids:
  - MetaCyc:PWY-5901
- check_id: diff
  name: diff
  command: git diff --check
  status: unavailable
  required: true
  summary: Final coordinated receipt has not yet been inspected.
  target_ids:
  - MetaCyc:PWY-5901
evidence:
- evidence_id: e-target
  kind: record_content
  reference: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
  locator: Complete target; dhb-edge-015 evidence reference PMID:2521622/source_locator
  accessed_at: '2026-10-11T06:18:48Z'
  support: refutes
  summary: Locator includes correct Results p795 but incorrectly names Discussion
    p797.
  snapshot_sha256: 94a671009cfae9c61381d26067a07e80edaeb5d6e4f73a00ae8c81bfb35b1144
- evidence_id: e-primary
  kind: primary_source
  reference: https://europepmc.org/articles/PMC209666?pdf=render
  locator: Printed p795 Results/Purification of diDHB-DH; printed p796 Discussion,
    lower right column; printed p797 inspected as contrast
  accessed_at: '2026-10-11T06:18:48Z'
  support: supports
  summary: Independently extracted original PDF with pypdfium2 and rendered pages
    795,796,797. The 210000 molecular-mass/octamer result is on p795, repeated in
    Discussion on p796. Page797 discusses EntC and references, not the octamer result.
  snapshot_sha256: 7202c514814dfe9e67fc5838273b600f8479a0e43d7588f3313f7591e9d1a19f
assessments:
- assessment_id: a-locator
  area: provenance
  topic: Exact primary page location for historical EntA assembly conflict
  outcome: concern
  summary: Scientific assertion supported at the correctly cited Results page; the
    second locator must change from printed p797 to p796.
  target_ids:
  - MetaCyc:PWY-5901
  evidence_ids:
  - e-target
  - e-primary
findings:
- finding_id: f-enta-discussion-page
  issue_key: dhb-enta-octamer-discussion-page
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical EntA octamer Discussion page is 796, not 797
  description: dhb-edge-015 PMID:2521622 evidence locates Discussion on printed p797.
    Original PDF places that octamer discussion at printed p796. Correctly cited Results
    p795 already supports the assertion; no chemistry or assembly change requested.
    Matching projected evidence in dhb-source-projection.json should follow the correction.
  target_ids:
  - MetaCyc:PWY-5901
  field_paths:
  - mechanistic_edges[id=dhb-edge-015]/evidence[reference_id=PMID:2521622]/source_locator
  evidence_ids:
  - e-target
  - e-primary
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    role: maintained pathway record
  rule_id: review-yaml-record precise source locators
  native_severity: minor
  normalization_reason: Bounded retrieval/provenance error, with scientifically supported
    assertion and one correct existing primary locator.
actions:
- action_id: correct-page
  description: Replace p.797 Discussion with p.796 Discussion in the maintained evidence;
    refresh corresponding projection/replay and generated outputs, then preserve this
    finding lineage in a successor review.
  finding_ids:
  - f-enta-discussion-page
  target_ids:
  - MetaCyc:PWY-5901
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    role: maintained pathway record
  acceptance_checks:
  - Visually compare final locator with original PDF printed pages795–797.
  - Verify only bounded locator/provenance changes and run final source replay and
    coordinated corpus gates.
limitations:
- Partial observation; complete independent source replay and full coordinated gates
  not yet accepted.
- Primary abstract-only scope and qualified EntB/EntA assembly distinctions remain
  part of the ongoing scientific review.
notes:
- Initial canonical inspection completed time is used as review start; original target
  and source inputs remain unchanged for this save.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/359
```
