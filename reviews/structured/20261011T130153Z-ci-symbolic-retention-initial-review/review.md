# Initial technical review of symbolic historical-review retention refs

- Review: 20261011T130153Z-ci-symbolic-retention-initial-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T12:59:26.182356Z
- Finished UTC: 2026-10-11T13:01:53.486723Z
- Reviewer: Codex independent technical reviewer (/root/pathway_authority_cache) (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

One confirmed minor ref-safety defect remains in the proposed helper: a dangling symbolic retention ref is followed and an unrelated branch ref is created. Reject symbolic retention refs and prevent dereference during the final compare-and-swap update.

## Scope And Provenance

The exact proposed helper at SHA f7eb85f3dac4c21a7e4b21d1efba3bb639bbd7d4dd12a4eae27f10ed045af0f2, its integration context and an isolated symbolic-ref safety probe.

Selection: Independent adversarial review of the issue386 correction; bounded new finding issue387.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 58bf19dcff135ef3b381350b96cae4b4dcb9c769.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PathwayMech:review-retention-helper | scripts/fetch_review_revisions.py | maintained | Historical review commit retention helper |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical proposed-helper input capture | passed | True | PathwayMech:review-retention-helper | Captured eight inputs from the frozen current working tree; all exact hashes rechecked before save. |
| Dangling symbolic retention ref rejects without unrelated ref creation | failed | True | PathwayMech:review-retention-helper | The diagnostic executed successfully and reproduced the failed safety invariant: unrelated-probe branch absent before restoration, present afterward; helper returned success. No network request, no owner repository mutation. |
| Exact helper branch and workflow inspection | passed | True | PathwayMech:review-retention-helper | The helper validates full SHA-1 IDs and an official remote, but rev-parse cannot distinguish a missing direct ref from a dangling symbolic ref; update-ref dereferences by default. Existing tests cover direct conflicts and non-commit objects, not this case. |

## Scientific And Domain Assessments

### Retention is confined to the declared local ref namespace

consistency: concern. Targets: PathwayMech:review-retention-helper.

The helper can create a ref outside refs/record-reviews when the existing retention name is symbolic. This contradicts the bounded retention behavior.

### Threat and impact are limited to pre-existing local symbolic refs

scope: supported. Targets: PathwayMech:review-retention-helper.

Fresh CI normally has no retention refs. This is a deterministic local ref-safety defect, not a demonstrated remote-code execution or GitHub token exposure. The reproduction performs no network fetch.

## Findings

### f-symbolic-review-retention-ref: A dangling symbolic retention ref creates an unrelated branch

minor / open / confirmed; issue key: ci-review-retention-symbolic-ref.

restore_revisions treats a dangling symbolic refs/record-reviews/&lt;sha&gt; as an absent ref. Its ordinary update-ref follows that symbolic name and creates its unrelated branch target, then returns success. Explicitly reject symbolic retention refs before fetching and updating; prevent dereference in the final compare-and-swap write so a concurrent replacement cannot redirect it.

## Recommended Actions And Acceptance Checks

### a-no-deref

Reject dangling and existing symbolic retention refs before mutation, and make the final compare-and-swap update no-dereference. Add isolated tests for dangling/existing symbolic refs and a race before final update.

- All symbolic-ref cases fail without changing their referent or any unrelated branch.
- A concurrent symbolic replacement cannot redirect the final ref update.
- Ordinary exact direct-ref restore remains idempotent and historical provenance verification stays unchanged.
- Re-run the independent official fresh-clone verification and appropriate final gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-inspect | /private/tmp/pathwaymech-pr383-technical-review/helper-initial-inspect.json | supports | Canonical capture and current-byte verification of eight scoped inputs. |
| e-probe | research/pathway_additions/2026-10-11-next-211/ci-provenance/symbolic-ref-initial-probe.json; before_returncode, restore_return, after_returncode and after_stdout | refutes | A temporary local repository has an existing commit and a dangling refs/record-reviews/&lt;sha&gt; symbolic ref pointing to refs/heads/unrelated-probe. Restoration creates that unrelated branch and reports success without fetching. |
| e-repeat | /private/tmp/pathwaymech-pr383-technical-review/symbolic-ref-repeat-probe.json | refutes | Independent second temporary repository repeats the same result after canonical input capture; helper bytes are unchanged. |
| e-helper | scripts/fetch_review_revisions.py; restore_revisions: retained rev-parse check and final git update-ref | supports | The missing-ref path treats a dangling symbolic ref as absent, and final update-ref follows that symbolic ref. A no-dereference update and explicit symbolic-ref rejection preserve unrelated refs. |

## Limits And Additional Notes

- Full cohort gates were still running when this bounded finding was saved. Their results are not needed to establish the isolated ref mutation, and are not claimed as passed here.
- No scientific record, rendered page, owner implementation or GitHub state was changed by this reviewer.
- The preliminary diagnostic preceded the helper capture; it was repeated in a new external repository after canonical inspection.
- Issue386 original workflow failure has its own immutable initial observation. The final technical successor should preserve both findings and their distinct exact predecessors.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T130153Z-ci-symbolic-retention-initial-review
kind: repository
repository: CultureBotAI/PathwayMech
title: Initial technical review of symbolic historical-review retention refs
started_at: '2026-10-11T12:59:26.182356Z'
finished_at: '2026-10-11T13:01:53.486723Z'
reviewer:
  identity: Codex independent technical reviewer (/root/pathway_authority_cache)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer did not author this helper or its tests. Reviewer independently
    constructed and repeated the isolated Git symbolic-ref probe; previous pathway
    work is outside this technical scope.
skill: 'review-yaml-record: bounded repository technical review'
completion: completed
verdict: needs_curation
scientific_review: false
summary: 'One confirmed minor ref-safety defect remains in the proposed helper: a
  dangling symbolic retention ref is followed and an unrelated branch ref is created.
  Reject symbolic retention refs and prevent dereference during the final compare-and-swap
  update.'
source:
  git_revision: 58bf19dcff135ef3b381350b96cae4b4dcb9c769
  state: working_tree
  inputs:
  - path: .github/workflows/main.yaml
    sha256: 09bdf8c9135e5696658e14fea56ddf0961f15f9e7ba31c6780ffb9952ac22f20
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: research/pathway_additions/2026-10-11-next-211/ci-provenance/symbolic-ref-initial-probe.json
    sha256: 93b04acf97249cb03f5ee4b51cbdc4cb2da40bae04ce3c1c247d6a659f870b34
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/fetch_review_revisions.py
    sha256: f7eb85f3dac4c21a7e4b21d1efba3bb639bbd7d4dd12a4eae27f10ed045af0f2
    role: target
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: tests/test_fetch_review_revisions.py
    sha256: 4afc0cf7f51cd278803e98cb2742759391b0f8384fe9e5b59fbb276d253f8559
    role: context
targets:
- target_id: PathwayMech:review-retention-helper
  path: scripts/fetch_review_revisions.py
  label: Historical review commit retention helper
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: scripts/fetch_review_revisions.py
    role: historical_revision_restoration_owner
scope:
  description: The exact proposed helper at SHA f7eb85f3dac4c21a7e4b21d1efba3bb639bbd7d4dd12a4eae27f10ed045af0f2,
    its integration context and an isolated symbolic-ref safety probe.
  selection: Independent adversarial review of the issue386 correction; bounded new
    finding issue387.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PathwayMech:review-retention-helper
  exclusions:
  - target: Scientific pathway records and final cohort-wide checks
    reason: No scientific reassessment; current full gates and final correction checks
      are separately owned and still pending.
checks:
- check_id: c-inspect
  name: Canonical proposed-helper input capture
  status: passed
  required: true
  command: scripts/record_review.py inspect --targets /private/tmp/pathwaymech-pr383-technical-review/helper-targets.json
    with explicit helper tests, workflow, contract, profile and maintained original
    probe inputs
  exit_code: 0
  summary: Captured eight inputs from the frozen current working tree; all exact hashes
    rechecked before save.
  target_ids:
  - PathwayMech:review-retention-helper
  evidence_ids:
  - e-inspect
- check_id: c-ref-probe
  name: Dangling symbolic retention ref rejects without unrelated ref creation
  status: failed
  required: true
  command: PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src .venv/bin/python /private/tmp/pathwaymech-pr383-technical-review/probe-symbolic-ref-repeat.py
  exit_code: 0
  summary: 'The diagnostic executed successfully and reproduced the failed safety
    invariant: unrelated-probe branch absent before restoration, present afterward;
    helper returned success. No network request, no owner repository mutation.'
  scope_note: The check status describes the ref-safety assertion, not the diagnostic
    process exit code. Original and post-inspection repeats agree.
  target_ids:
  - PathwayMech:review-retention-helper
  evidence_ids:
  - e-probe
  - e-repeat
- check_id: c-read
  name: Exact helper branch and workflow inspection
  status: passed
  required: true
  summary: The helper validates full SHA-1 IDs and an official remote, but rev-parse
    cannot distinguish a missing direct ref from a dangling symbolic ref; update-ref
    dereferences by default. Existing tests cover direct conflicts and non-commit
    objects, not this case.
  target_ids:
  - PathwayMech:review-retention-helper
  evidence_ids:
  - e-helper
evidence:
- evidence_id: e-inspect
  kind: validation
  reference: /private/tmp/pathwaymech-pr383-technical-review/helper-initial-inspect.json
  accessed_at: '2026-10-11T13:01:53.486723Z'
  support: supports
  summary: Canonical capture and current-byte verification of eight scoped inputs.
  snapshot_sha256: dacf2826066b42b2695c1ea395b677f5f6c4988c0946e0dc7af376f317291a40
- evidence_id: e-probe
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-211/ci-provenance/symbolic-ref-initial-probe.json
  accessed_at: '2026-10-11T13:01:53.486723Z'
  support: refutes
  locator: before_returncode, restore_return, after_returncode and after_stdout
  summary: A temporary local repository has an existing commit and a dangling refs/record-reviews/<sha>
    symbolic ref pointing to refs/heads/unrelated-probe. Restoration creates that
    unrelated branch and reports success without fetching.
  snapshot_sha256: 93b04acf97249cb03f5ee4b51cbdc4cb2da40bae04ce3c1c247d6a659f870b34
- evidence_id: e-repeat
  kind: validation
  reference: /private/tmp/pathwaymech-pr383-technical-review/symbolic-ref-repeat-probe.json
  accessed_at: '2026-10-11T13:01:53.486723Z'
  support: refutes
  summary: Independent second temporary repository repeats the same result after canonical
    input capture; helper bytes are unchanged.
  snapshot_sha256: 51e2c82f58523491214714dcc4e3057bd5c5d36b6302efedd0a381e725158778
- evidence_id: e-helper
  kind: record_content
  reference: scripts/fetch_review_revisions.py
  accessed_at: '2026-10-11T13:01:53.486723Z'
  support: supports
  locator: 'restore_revisions: retained rev-parse check and final git update-ref'
  summary: The missing-ref path treats a dangling symbolic ref as absent, and final
    update-ref follows that symbolic ref. A no-dereference update and explicit symbolic-ref
    rejection preserve unrelated refs.
  snapshot_sha256: f7eb85f3dac4c21a7e4b21d1efba3bb639bbd7d4dd12a4eae27f10ed045af0f2
assessments:
- assessment_id: a-ref
  area: consistency
  topic: Retention is confined to the declared local ref namespace
  outcome: concern
  summary: The helper can create a ref outside refs/record-reviews when the existing
    retention name is symbolic. This contradicts the bounded retention behavior.
  target_ids:
  - PathwayMech:review-retention-helper
  evidence_ids:
  - e-probe
  - e-repeat
  - e-helper
- assessment_id: a-risk
  area: scope
  topic: Threat and impact are limited to pre-existing local symbolic refs
  outcome: supported
  summary: Fresh CI normally has no retention refs. This is a deterministic local
    ref-safety defect, not a demonstrated remote-code execution or GitHub token exposure.
    The reproduction performs no network fetch.
  target_ids:
  - PathwayMech:review-retention-helper
  evidence_ids:
  - e-probe
  - e-repeat
findings:
- finding_id: f-symbolic-review-retention-ref
  issue_key: ci-review-retention-symbolic-ref
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: A dangling symbolic retention ref creates an unrelated branch
  description: restore_revisions treats a dangling symbolic refs/record-reviews/<sha>
    as an absent ref. Its ordinary update-ref follows that symbolic name and creates
    its unrelated branch target, then returns success. Explicitly reject symbolic
    retention refs before fetching and updating; prevent dereference in the final
    compare-and-swap write so a concurrent replacement cannot redirect it.
  target_ids:
  - PathwayMech:review-retention-helper
  field_paths:
  - scripts/fetch_review_revisions.py::restore_revisions
  evidence_ids:
  - e-probe
  - e-repeat
  - e-helper
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: scripts/fetch_review_revisions.py
    role: historical_revision_restoration_owner
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/387
actions:
- action_id: a-no-deref
  description: Reject dangling and existing symbolic retention refs before mutation,
    and make the final compare-and-swap update no-dereference. Add isolated tests
    for dangling/existing symbolic refs and a race before final update.
  finding_ids:
  - f-symbolic-review-retention-ref
  target_ids:
  - PathwayMech:review-retention-helper
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: scripts/fetch_review_revisions.py
    role: historical_revision_restoration_owner
  acceptance_checks:
  - All symbolic-ref cases fail without changing their referent or any unrelated branch.
  - A concurrent symbolic replacement cannot redirect the final ref update.
  - Ordinary exact direct-ref restore remains idempotent and historical provenance
    verification stays unchanged.
  - Re-run the independent official fresh-clone verification and appropriate final
    gates.
limitations:
- Full cohort gates were still running when this bounded finding was saved. Their
  results are not needed to establish the isolated ref mutation, and are not claimed
  as passed here.
- No scientific record, rendered page, owner implementation or GitHub state was changed
  by this reviewer.
notes:
- The preliminary diagnostic preceded the helper capture; it was repeated in a new
  external repository after canonical inspection.
- Issue386 original workflow failure has its own immutable initial observation. The
  final technical successor should preserve both findings and their distinct exact
  predecessors.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/387
- https://github.com/CultureBotAI/PathwayMech/issues/386
```
