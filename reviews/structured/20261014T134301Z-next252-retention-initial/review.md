# Committed protocatechuate evidence omits three retained logs

- Review: 20261014T134301Z-next252-retention-initial
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T13:41:20Z
- Finished UTC: 2026-10-14T13:43:01.439591Z
- Reviewer: Codex /root/next252_integration_review (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

The initial feature commit omits three authority-build logs that committed retention manifests promise. All exist in the reviewed working tree but were excluded by the existing *.log rule. Exact committed-head acceptance is withheld; no pathway-science defect is claimed.

## Scope And Provenance

Bounded authoritative commit retention audit for the sole new pathway.

Selection: Every maintained_path recursively declared in every committed JSON under next252/para at exact head 37e8e0516636c901666360826e4403774162050a.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 37e8e0516636c901666360826e4403774162050a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-6336 | data/pathways/protocatechuate-para-cleavage.yaml | maintained | protocatechuate para-cleavage pathway |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Every declared retained path is committed with its declared hash | failed | True | MetaCyc:PWY-6336 | Three of 111 declared path references are absent from the committed tree, despite existing locally. The independent command exits 1. |

## Scientific And Domain Assessments

### Declared retained evidence in the actual committed snapshot

provenance: concern. Targets: MetaCyc:PWY-6336.

The committed mapping promises three files absent from that snapshot, making its reproduction/retention manifest incomplete for fresh checkouts. Working-tree review hashes do not prove committed membership.

## Findings

### F1: Three declared authority logs are missing from the feature commit

major / open / confirmed; issue key: protocatechuate-para-committed-retained-logs.

Initial head 37e8e0516636c901666360826e4403774162050a omits source_builder.log, ontology_builder.log and redox-followup/ontology-builder.log even though their exact bytes and destinations are promised by committed retention manifests. The files remain locally present and ignored.

## Recommended Actions And Acceptance Checks

### A1

Track the three existing exact-byte log artifacts and preserve the initial failed commit and review.

- Force-add only the three promised artifacts without changing ignore policy, record data or log bytes.
- Verify every committed maintained_path and declared SHA-256 in the entire final dossier against actual Git blobs.
- Verify all 901 tested core inputs are unchanged, retain an explicit successor finding disposition, and inspect final committed head/tree.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| retention-check | /private/tmp/pathwaymech-next-252-integration-review/committed-retention-initial.json | supports | Independent git archive of exact head 37e8e0516636c901666360826e4403774162050a enumerates the complete committed dossier; three declared retained logs are absent. All other retained references are present and hash-match. |
| ignore-rule | .gitignore; line 19 (*.log); git check-ignore -v on each missing authority log | supports | All three local files match the unchanged *.log ignore rule. Existing working-tree presence therefore did not establish tracked publication. |

## Limits And Additional Notes

- This observation assesses the exact initial feature commit, not any later correction.
- No new scientific judgement is made. The prior working-tree integration review remains a truthful observation of its inspected working-tree bytes; it did not prove that all those artifacts were committed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T134301Z-next252-retention-initial
kind: record
repository: CultureBotAI/PathwayMech
title: Committed protocatechuate evidence omits three retained logs
started_at: '2026-10-14T13:41:20Z'
finished_at: '2026-10-14T13:43:01.439591Z'
reviewer:
  identity: Codex /root/next252_integration_review
  kind: agent
  independence: independent
  independence_basis: The root flagged a suspicious commit stat; this reviewer independently
    enumerated every retained maintained_path in the committed dossier, reproduced
    the three missing blobs and ignore rule, and has no authorship of the packaging
    or fix.
skill: .claude/skills/pathwaymech-resolve-reviews/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: false
summary: The initial feature commit omits three authority-build logs that committed
  retention manifests promise. All exist in the reviewed working tree but were excluded
  by the existing *.log rule. Exact committed-head acceptance is withheld; no pathway-science
  defect is claimed.
source:
  git_revision: 37e8e0516636c901666360826e4403774162050a
  state: git_commit
  inputs:
  - path: .gitignore
    sha256: 70389633ea1b22b8ced2da3f97a54db912f5c1c96045b1468fadbf6329853f64
    role: context
  - path: data/pathways/protocatechuate-para-cleavage.yaml
    sha256: 2a5e42e39a4e8eadb77eabf6f95896ecc7f001bafba04dec6eb74e7251169d89
    role: target
  - path: research/pathway_additions/2026-10-14-next-252/para/authorities/redox-followup/retention.json
    sha256: 9f679f1cbdd0bf9f5d15a0c95b9b39243124c61546368f3eab61b4ec80af345c
    role: context
  - path: research/pathway_additions/2026-10-14-next-252/para/authorities/retention.json
    sha256: 99629a745e3360f3dcd495ec361b40b3e9ce230f4e8fd7dc90a819a266ae4ef7
    role: context
scope:
  description: Bounded authoritative commit retention audit for the sole new pathway.
  selection: Every maintained_path recursively declared in every committed JSON under
    next252/para at exact head 37e8e0516636c901666360826e4403774162050a.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-6336
  exclusions:
  - target: New literature/scientific judgement and duplicate complete test execution
    reason: Record/core outputs are unchanged; this check concerns tracked artifact
      membership, which working-tree hash checks and the prior green gates did not
      establish.
targets:
- target_id: MetaCyc:PWY-6336
  path: data/pathways/protocatechuate-para-cleavage.yaml
  label: protocatechuate para-cleavage pathway
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/protocatechuate-para-cleavage.yaml
    role: maintained pathway record
checks:
- check_id: committed-retention
  name: Every declared retained path is committed with its declared hash
  status: failed
  required: true
  summary: Three of 111 declared path references are absent from the committed tree,
    despite existing locally. The independent command exits 1.
  target_ids:
  - MetaCyc:PWY-6336
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-252-integration-review/audit_committed_retention.py
    37e8e0516636c901666360826e4403774162050a committed-retention-initial
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - retention-check
evidence:
- evidence_id: retention-check
  kind: validation
  reference: /private/tmp/pathwaymech-next-252-integration-review/committed-retention-initial.json
  accessed_at: '2026-10-14T13:43:01.439591Z'
  support: supports
  summary: Independent git archive of exact head 37e8e0516636c901666360826e4403774162050a
    enumerates the complete committed dossier; three declared retained logs are absent.
    All other retained references are present and hash-match.
  snapshot_sha256: 019a7d62ab96fea965a88fb9887ccf07899409b367247cbbb2e11f38ebac8a2d
  search_scope: Every maintained_path reference recursively in every committed JSON
    under the complete next252/para dossier; git archive enumerates the authoritative
    tracked tree. Working-tree existence checks include ignored files. No ignored
    exclusion is used to infer absence.
- evidence_id: ignore-rule
  kind: validation
  reference: .gitignore
  locator: line 19 (*.log); git check-ignore -v on each missing authority log
  accessed_at: '2026-10-14T13:43:01.439591Z'
  support: supports
  summary: All three local files match the unchanged *.log ignore rule. Existing working-tree
    presence therefore did not establish tracked publication.
assessments:
- assessment_id: retention
  area: provenance
  topic: Declared retained evidence in the actual committed snapshot
  outcome: concern
  summary: The committed mapping promises three files absent from that snapshot, making
    its reproduction/retention manifest incomplete for fresh checkouts. Working-tree
    review hashes do not prove committed membership.
  target_ids:
  - MetaCyc:PWY-6336
  evidence_ids:
  - retention-check
  - ignore-rule
findings:
- finding_id: F1
  issue_key: protocatechuate-para-committed-retained-logs
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Three declared authority logs are missing from the feature commit
  description: Initial head 37e8e0516636c901666360826e4403774162050a omits source_builder.log,
    ontology_builder.log and redox-followup/ontology-builder.log even though their
    exact bytes and destinations are promised by committed retention manifests. The
    files remain locally present and ignored.
  target_ids:
  - MetaCyc:PWY-6336
  field_paths:
  - research/pathway_additions/2026-10-14-next-252/para/authorities/redox-followup/ontology-builder.log
  - research/pathway_additions/2026-10-14-next-252/para/authorities/source_builder.log
  - research/pathway_additions/2026-10-14-next-252/para/authorities/ontology_builder.log
  evidence_ids:
  - retention-check
  - ignore-rule
  rule_id: docs/CAUSAL_GRAPHS.md evidence and provenance; declared authorities retention
    mappings
  native_severity: major
  normalization_reason: A systematic staging exclusion makes explicitly retained audit
    artifacts unavailable in the committed reviewable result; the biological pathway
    remains unchanged.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-252/para/authorities/redox-followup/ontology-builder.log
    role: declared retained authority build log
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-252/para/authorities/source_builder.log
    role: declared retained authority build log
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-252/para/authorities/ontology_builder.log
    role: declared retained authority build log
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/532
actions:
- action_id: A1
  description: Track the three existing exact-byte log artifacts and preserve the
    initial failed commit and review.
  finding_ids:
  - F1
  target_ids:
  - MetaCyc:PWY-6336
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-252/para/authorities/redox-followup/ontology-builder.log
    role: declared retained authority build log
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-252/para/authorities/source_builder.log
    role: declared retained authority build log
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-252/para/authorities/ontology_builder.log
    role: declared retained authority build log
  acceptance_checks:
  - Force-add only the three promised artifacts without changing ignore policy, record
    data or log bytes.
  - Verify every committed maintained_path and declared SHA-256 in the entire final
    dossier against actual Git blobs.
  - Verify all 901 tested core inputs are unchanged, retain an explicit successor
    finding disposition, and inspect final committed head/tree.
limitations:
- This observation assesses the exact initial feature commit, not any later correction.
- No new scientific judgement is made. The prior working-tree integration review remains
  a truthful observation of its inspected working-tree bytes; it did not prove that
  all those artifacts were committed.
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261014T133634Z-next252-para-integration-final
  relationship: Additional committed-artifact audit exposes a staging defect outside
    the prior working-tree-byte attestation.
tags:
- next252
- integration
- retention
- initial
- issue-532
```
