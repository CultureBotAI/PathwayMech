# Initial technical review of unavailable historical review commits in PR383 CI

- Review: 20261011T125829Z-ci-review-provenance-initial-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T12:57:14.249563Z
- Finished UTC: 2026-10-11T12:58:29.946461Z
- Reviewer: Codex independent technical reviewer (/root/pathway_authority_cache) (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

One confirmed CI preparation defect prevents fresh checkouts from verifying a valid historical review source commit. The canonical provenance rejection is correct. Restore exact official historical commit objects before validation and retain all immutable review and scientific input bytes.

## Scope And Provenance

Original committed CI workflow and exact historical failure at PR383 head 58bf19dc, with its canonical provenance contract and affected retained review.

Selection: Explicit independent technical assignment for issue386.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 58bf19dcff135ef3b381350b96cae4b4dcb9c769.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PathwayMech:review-provenance-ci | .github/workflows/main.yaml | maintained | CI restoration of historical review provenance |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical historical workflow capture | passed | True | PathwayMech:review-provenance-ci | Canonical inspect completed successfully; all 10 captured hashes equal regular tracked blobs at the original commit. Historical source state is explicitly git_commit. |
| Original exact-head full CI test suite | failed | True | PathwayMech:review-provenance-ci | Actual original remote job failed only on missing historical review commit: 1 failed, 1126 passed, 7 skipped, 3 warnings in 169.67 seconds. |
| Exact historical contract and source claim inspection | passed | True | PathwayMech:review-provenance-ci | Read captured workflow, canonical provenance implementation, CI test and affected review after canonical inspection. Its provenance rejection is retained as the required contract. |

## Scientific And Domain Assessments

### Fresh CI checkout contains every declared historical source commit

provenance: concern. Targets: PathwayMech:review-provenance-ci.

Full ordinary branch history is insufficient for the prior feature commit named by the saved technical review. Actual CI cannot resolve the required commit and fails closed.

### Correct preparation without changing governed provenance rules

ownership: supported. Targets: PathwayMech:review-provenance-ci.

The defect belongs to workflow preparation. Preserve saved review pairs, historical hashes, scientific records and the canonical rejection of unavailable or mismatched provenance. A bounded official-repository fetch can supply missing original objects; it does not approve scientific claims.

## Findings

### f-missing-historical-review-commits: Fresh CI checkout cannot resolve an immutable review source commit

minor / open / confirmed; issue key: ci-missing-historical-review-commits.

The original workflow at 58bf19dc checks out full ordinary history but does not restore historical feature commits referenced by saved reviews. The required test fails resolving 6647fd69597d516ca41dec6e6c8314032cbd7c3a. Local object availability is not portable to a fresh clone. Keep the review source claim and rejection semantics unchanged; restore verifiable exact objects before validation.

## Recommended Actions And Acceptance Checks

### a-restore

Add fail-closed preparation that validates review pairs and repository claims, obtains only exact full commit IDs from the official repository, verifies object type and identity, and runs the unchanged canonical gate afterward.

- Official fresh-clone reproduction fails before restoration and passes afterward without changing saved review or scientific input bytes.
- Malformed revision, foreign repository, invalid pair, unavailable object, non-commit object and conflicting retained ref must fail.
- Trusted event base, canonical hash/append-only checks and governed contract remain unchanged.
- Save a successor with the same issue key and exact previous occurrence after actual focused and full checks pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-capture | /private/tmp/pathwaymech-pr383-technical-review/initial-inspect.json; Canonical inspect on an external sparse checkout of the exact original commit; all 10 tracked blobs independently rehashed. | supports | The original workflow and governed validation context were captured at 58bf19dcff135ef3b381350b96cae4b4dcb9c769. No corrected working-tree bytes are claimed as historical. |
| e-ci | https://github.com/CultureBotAI/PathwayMech/actions/runs/38140206532/job/114472350329; Test step; exact retained original log /private/tmp/pathwaymech-pr383-failed-job.log | refutes | The full remote suite exited 1: 1 failed, 1126 passed, 7 skipped, 3 warnings in 169.67 seconds. Its only failure is test_every_saved_structured_bundle_is_valid because the saved technical review references unavailable commit 6647fd69597d516ca41dec6e6c8314032cbd7c3a. |
| e-workflow | .github/workflows/main.yaml; jobs.qc.steps, checkout fetch-depth and preparation before Test | supports | The original checkout fetches ordinary branch history with fetch-depth 0, then proceeds directly from dependency installation to lint and tests. It has no restoration of exact historical review commits. |
| e-contract | scripts/record_review.py; read_review, source_provenance and review_paths | supports | The unchanged canonical contract verifies source commit availability before accepting saved provenance and rejects invalid or unverified claims. The historical review correctly names a full source revision; this review requests restoring available original objects, not weakening that rejection. |
| e-history | reviews/structured/20261011T120654Z-aerobactin-page-currency-initial-review/review.yaml; source.state and source.git_revision | supports | The retained earlier technical observation declares git_commit provenance at 6647fd69597d516ca41dec6e6c8314032cbd7c3a. Its immutable source claim must remain intact. |

## Limits And Additional Notes

- This is an original-commit technical observation, not a completed scientific review or approval of the in-progress fix.
- The original full CI test command failed. Current patch full gates and the independent official fresh-clone replay are not yet complete and are not claimed here.
- Source-object retrieval depends on the official remote retaining the historical object; ordinary full-history checkout alone does not guarantee this.
- Preliminary failure-log and patch reading preceded formal capture. The original workflow, contract and affected review were re-read and verified against the historical capture before this assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T125829Z-ci-review-provenance-initial-review
kind: repository
repository: CultureBotAI/PathwayMech
title: Initial technical review of unavailable historical review commits in PR383
  CI
started_at: '2026-10-11T12:57:14.249563Z'
finished_at: '2026-10-11T12:58:29.946461Z'
reviewer:
  identity: Codex independent technical reviewer (/root/pathway_authority_cache)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer did not author the CI workflow, provenance restoration
    helper or proposed correction. Prior unrelated pathway authoring and scientific
    reviews are disclosed; they are not reassessed here.
skill: 'review-yaml-record: bounded repository technical review'
completion: completed
verdict: needs_curation
scientific_review: false
summary: One confirmed CI preparation defect prevents fresh checkouts from verifying
  a valid historical review source commit. The canonical provenance rejection is correct.
  Restore exact official historical commit objects before validation and retain all
  immutable review and scientific input bytes.
source:
  git_revision: 58bf19dcff135ef3b381350b96cae4b4dcb9c769
  state: git_commit
  inputs:
  - path: .github/workflows/main.yaml
    sha256: e269d4542ec0831bc5d6a864831aa5d4767ad7987657a8dfba5b1b4fac73840b
    role: target
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: docs/record-review-profile.md
    sha256: a3d4b48de5f227515f9b5de12dd172cd1eb626068235b2b2e58bc4f6a5ee567d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reviews/structured/20261011T120654Z-aerobactin-page-currency-initial-review/review.md
    sha256: d086b993785c228b76ff040ddd69a30b27a2664390f73644223e667cf0149a6c
    role: context
  - path: reviews/structured/20261011T120654Z-aerobactin-page-currency-initial-review/review.yaml
    sha256: 7cf028b0959703cc20e0d18bd464c602d39dcf3b8d317577f9954e9384394829
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: tests/test_record_review_ci.py
    sha256: a673543f4dead0c295d921e80d17abe86aaa831b4cc8c659b883fe0006bf6c3f
    role: context
  - path: tests/test_record_review_contract.py
    sha256: 7be08e684dcd235ddeae8f3c6a5d45b0ee74a60d1c1818cc81467e38901e5d56
    role: context
scope:
  description: Original committed CI workflow and exact historical failure at PR383
    head 58bf19dc, with its canonical provenance contract and affected retained review.
  selection: Explicit independent technical assignment for issue386.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PathwayMech:review-provenance-ci
  exclusions:
  - target: Pathway scientific content and current correction implementation
    reason: This initial observation preserves the original failure. The correction
      receives an independent successor after actual verification.
targets:
- target_id: PathwayMech:review-provenance-ci
  path: .github/workflows/main.yaml
  label: CI restoration of historical review provenance
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: .github/workflows/main.yaml
    role: workflow_preparation_owner
checks:
- check_id: c-inspect
  name: Canonical historical workflow capture
  status: passed
  required: true
  command: Current unchanged scripts/record_review.py --repo-root /private/tmp/pathwaymech-pr383-technical-review/historical
    inspect --targets /private/tmp/pathwaymech-pr383-technical-review/targets.json
    with nine explicit context inputs; exact argv preserved in initial-capture-receipt.json
  exit_code: 0
  summary: Canonical inspect completed successfully; all 10 captured hashes equal
    regular tracked blobs at the original commit. Historical source state is explicitly
    git_commit.
  target_ids:
  - PathwayMech:review-provenance-ci
  evidence_ids:
  - e-capture
- check_id: c-original-ci
  name: Original exact-head full CI test suite
  status: failed
  required: true
  command: uv run --locked --extra dev pytest -q
  exit_code: 1
  expected_exit_code: 0
  summary: 'Actual original remote job failed only on missing historical review commit:
    1 failed, 1126 passed, 7 skipped, 3 warnings in 169.67 seconds.'
  scope_note: Observed original remote log, not a new local execution or a statement
    about the patched workflow.
  target_ids:
  - PathwayMech:review-provenance-ci
  evidence_ids:
  - e-ci
- check_id: c-contract
  name: Exact historical contract and source claim inspection
  status: passed
  required: true
  summary: Read captured workflow, canonical provenance implementation, CI test and
    affected review after canonical inspection. Its provenance rejection is retained
    as the required contract.
  target_ids:
  - PathwayMech:review-provenance-ci
  evidence_ids:
  - e-workflow
  - e-contract
  - e-history
evidence:
- evidence_id: e-capture
  kind: validation
  reference: /private/tmp/pathwaymech-pr383-technical-review/initial-inspect.json
  locator: Canonical inspect on an external sparse checkout of the exact original
    commit; all 10 tracked blobs independently rehashed.
  accessed_at: '2026-10-11T12:58:29.946461Z'
  support: supports
  summary: The original workflow and governed validation context were captured at
    58bf19dcff135ef3b381350b96cae4b4dcb9c769. No corrected working-tree bytes are
    claimed as historical.
  snapshot_sha256: 6899ec97e53eff39ac7df14faa055d85ada8678073e3fd8b7d5e89476f98623c
- evidence_id: e-ci
  kind: validation
  reference: https://github.com/CultureBotAI/PathwayMech/actions/runs/38140206532/job/114472350329
  locator: Test step; exact retained original log /private/tmp/pathwaymech-pr383-failed-job.log
  accessed_at: '2026-10-11T12:58:29.946461Z'
  support: refutes
  summary: 'The full remote suite exited 1: 1 failed, 1126 passed, 7 skipped, 3 warnings
    in 169.67 seconds. Its only failure is test_every_saved_structured_bundle_is_valid
    because the saved technical review references unavailable commit 6647fd69597d516ca41dec6e6c8314032cbd7c3a.'
  snapshot_sha256: c3ca651fc813273ada7d8099c43e1f1b2c71b09106fbfb7a618cf26b8e2dbd65
- evidence_id: e-workflow
  kind: record_content
  reference: .github/workflows/main.yaml
  locator: jobs.qc.steps, checkout fetch-depth and preparation before Test
  accessed_at: '2026-10-11T12:58:29.946461Z'
  support: supports
  summary: The original checkout fetches ordinary branch history with fetch-depth
    0, then proceeds directly from dependency installation to lint and tests. It has
    no restoration of exact historical review commits.
  snapshot_sha256: e269d4542ec0831bc5d6a864831aa5d4767ad7987657a8dfba5b1b4fac73840b
- evidence_id: e-contract
  kind: record_content
  reference: scripts/record_review.py
  locator: read_review, source_provenance and review_paths
  accessed_at: '2026-10-11T12:58:29.946461Z'
  support: supports
  summary: The unchanged canonical contract verifies source commit availability before
    accepting saved provenance and rejects invalid or unverified claims. The historical
    review correctly names a full source revision; this review requests restoring
    available original objects, not weakening that rejection.
  snapshot_sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
- evidence_id: e-history
  kind: prior_review
  reference: reviews/structured/20261011T120654Z-aerobactin-page-currency-initial-review/review.yaml
  locator: source.state and source.git_revision
  accessed_at: '2026-10-11T12:58:29.946461Z'
  support: supports
  summary: The retained earlier technical observation declares git_commit provenance
    at 6647fd69597d516ca41dec6e6c8314032cbd7c3a. Its immutable source claim must remain
    intact.
  snapshot_sha256: 7cf028b0959703cc20e0d18bd464c602d39dcf3b8d317577f9954e9384394829
assessments:
- assessment_id: a-preparation
  area: provenance
  topic: Fresh CI checkout contains every declared historical source commit
  outcome: concern
  summary: Full ordinary branch history is insufficient for the prior feature commit
    named by the saved technical review. Actual CI cannot resolve the required commit
    and fails closed.
  target_ids:
  - PathwayMech:review-provenance-ci
  evidence_ids:
  - e-ci
  - e-workflow
  - e-history
- assessment_id: a-contract
  area: ownership
  topic: Correct preparation without changing governed provenance rules
  outcome: supported
  summary: The defect belongs to workflow preparation. Preserve saved review pairs,
    historical hashes, scientific records and the canonical rejection of unavailable
    or mismatched provenance. A bounded official-repository fetch can supply missing
    original objects; it does not approve scientific claims.
  target_ids:
  - PathwayMech:review-provenance-ci
  evidence_ids:
  - e-contract
  - e-history
findings:
- finding_id: f-missing-historical-review-commits
  issue_key: ci-missing-historical-review-commits
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Fresh CI checkout cannot resolve an immutable review source commit
  description: The original workflow at 58bf19dc checks out full ordinary history
    but does not restore historical feature commits referenced by saved reviews. The
    required test fails resolving 6647fd69597d516ca41dec6e6c8314032cbd7c3a. Local
    object availability is not portable to a fresh clone. Keep the review source claim
    and rejection semantics unchanged; restore verifiable exact objects before validation.
  target_ids:
  - PathwayMech:review-provenance-ci
  field_paths:
  - .github/workflows/main.yaml::jobs.qc.steps
  evidence_ids:
  - e-ci
  - e-workflow
  - e-contract
  - e-history
  rule_id: tests/test_record_review_contract.py::test_every_saved_structured_bundle_is_valid
  native_severity: Required CI blocker caused by missing historical Git object preparation
  normalization_reason: This is a bounded infrastructure provenance availability defect,
    not incorrect biological data or evidence. Required CI must still pass before
    publication.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: .github/workflows/main.yaml
    role: workflow_preparation_owner
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/386
actions:
- action_id: a-restore
  description: Add fail-closed preparation that validates review pairs and repository
    claims, obtains only exact full commit IDs from the official repository, verifies
    object type and identity, and runs the unchanged canonical gate afterward.
  finding_ids:
  - f-missing-historical-review-commits
  target_ids:
  - PathwayMech:review-provenance-ci
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: .github/workflows/main.yaml
    role: workflow_preparation_owner
  acceptance_checks:
  - Official fresh-clone reproduction fails before restoration and passes afterward
    without changing saved review or scientific input bytes.
  - Malformed revision, foreign repository, invalid pair, unavailable object, non-commit
    object and conflicting retained ref must fail.
  - Trusted event base, canonical hash/append-only checks and governed contract remain
    unchanged.
  - Save a successor with the same issue key and exact previous occurrence after actual
    focused and full checks pass.
limitations:
- This is an original-commit technical observation, not a completed scientific review
  or approval of the in-progress fix.
- The original full CI test command failed. Current patch full gates and the independent
  official fresh-clone replay are not yet complete and are not claimed here.
- Source-object retrieval depends on the official remote retaining the historical
  object; ordinary full-history checkout alone does not guarantee this.
notes:
- Preliminary failure-log and patch reading preceded formal capture. The original
  workflow, contract and affected review were re-read and verified against the historical
  capture before this assessment.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/386
- https://github.com/CultureBotAI/PathwayMech/pull/383
```
