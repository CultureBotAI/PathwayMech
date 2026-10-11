# Technical review of aerobactin generated-page currency after PR379 CI failure

- Review: 20261011T120654Z-aerobactin-page-currency-initial-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T12:05:40.229180Z
- Finished UTC: 2026-10-11T12:06:54.116485Z
- Reviewer: Codex independent publication reviewer (/root/verify_graph_publication) (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

One confirmed minor generated-artifact currency finding blocks required CI: the committed aerobactin page omits the final REVIEW history entry added after rendering. It exactly matches the canonical render with that one event removed. The scientific record and graph are unchanged; regenerate the page from all current maintained inputs.

## Scope And Provenance

Exact generated aerobactin page at PR379 head6647fd6, its maintained record/history owners, renderer and remote CI failure.

Selection: Explicit parent assignment following the isolated stale-page CI test failure.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 6647fd69597d516ca41dec6e6c8314032cbd7c3a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0019270#generated-page | pages/records/GO_0019270.html | generated | Generated aerobactin record page |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical generated-target inspection | passed | True | GO:0019270#generated-page | Actual session33611 completed0 before formal assessment. All9 inputs rechecked against current bytes and exact published Git tree. |
| Exact-head remote full test suite | failed | True | GO:0019270#generated-page | Run38137531447/job114464375650 at head6647fd6:1failed1126passed7skipped3warnings184.86s. Sole failure test_the_committed_site_is_current identifies pages/records/GO_0019270.html; remote quality gate was skipped. |
| Exact-head remote lint | passed | False | GO:0019270#generated-page | Remote lint step passed before the failed test step. |
| Read-only canonical-render causal comparison | passed | True | GO:0019270#generated-page | Committed page equals exactly the rendering without final REVIEW history, and differs from full current rendering only by that history list item. No maintained file written. |

## Scientific And Domain Assessments

### Generated page agrees with current maintained history

consistency: concern. Targets: GO:0019270#generated-page.

Page is stale by one final REVIEW history list item; exact remote test and local causal comparison agree.

### Bounded canonical regeneration without scientific changes

ownership: supported. Targets: GO:0019270#generated-page.

The owner inputs are already correct. Rerun the canonical renderer after the final history event; do not hand-edit HTML, rewrite the original scientific review, or create another record REVIEW history solely for this refresh.

## Findings

### f-post-review-page-currency: Aerobactin page predates its final review-history event

minor / open / confirmed; issue key: aerobactin-post-review-page-currency.

Required CI fails because pages/records/GO_0019270.html lacks the11:55:15REVIEW history event. The page exactly matches the current renderer when that single event is removed. Scientific YAML, graph/evidence and renderer are unchanged.

## Recommended Actions And Acceptance Checks

### a-rerender

Regenerate pages through the canonical renderer after the final history event; commit only the expected generated delta plus new append-only technical review/receipts as needed.

- Expected rendered page SHA b5874ada97fa95703f265b5a5f58ffe07f94b559d8fe0b0013f7c092a3f29fb5 if maintained inputs remain unchanged.
- Fresh canonical page --check and test_the_committed_site_is_current pass; full QC and exact-head remote required CI pass.
- Scientific YAML, graph/evidence/download bytes and original canonical scientific review remain unchanged; preserve historical source inputs.
- Save a linked technical successor with the same issue_key and explicit previous_occurrences after observed correction/checks; do not add a new record REVIEW history for this technical refresh.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-capture | /private/tmp/pathwaymech-pr379-page-currency-review/inspect.json; Canonical source and target capture;9tracked files independently verified with git show at6647fd6 | supports | Exact current and committed input bytes agree. The observation uses git_commit provenance for this CI-failed published revision. |
| e-ci | https://github.com/CultureBotAI/PathwayMech/actions/runs/38137531447/job/114464375650; Test step, captured stderr, finalpytestsummary; exact raw job log /private/tmp/pathwaymech-pr379-failed-job.log | refutes | Sole failed test names the aerobactin generated page as stale. Full test summary is1failed1126passed7skipped; lint passed and later quality gate skipped. |
| e-delta | /private/tmp/pathwaymech-pr379-page-currency-review/diagnosis.json; Canonical _record_page full-history comparison and exact equality with final REVIEW event removed; external page diff | supports | Old page SHAabeb61a0 has125540bytes; full current render SHAb5874ada has126680bytes. The only delta is the missing final REVIEW history list item. |
| e-history | history/records/aerobactin-biosynthesis/2026-10-11T115515Z-codex-9ae380.yaml; Entire REVIEW event and session timestamp11:55:15Z | supports | The history is a maintained input added after the sealed scientific-review rendering; it truthfully describes the saved review and does not change science. |
| e-renderer | src/pathwaymech/cli.py; render_site lines181–204; render_pages_main lines322–367; _record_page history_html call | supports | Canonical page currency depends on both record YAML and record history. Rerender is required after adding a history event. |
| e-prior | reviews/structured/20261011T115435Z-aerobactin-independent-review/review.yaml; Entire original scientific review; generated-page hash and input scope | context_only | Earlier science review remains an immutable observation of its actually inspected inputs. This technical finding does not overturn the source-based scientific assessment or silently refresh that historical page hash. |

## Limits And Additional Notes

- This technical observation does not repeat primary literature review and does not claim a current full-suite pass.
- Required remote full tests failed; remote quality gate was skipped. Initial local full gates from the prior scientific review preceded the added REVIEW history event.
- No generated page or scientific source was modified by this reviewer; the external expected render is diagnostic only.
- Preliminary read-only CI diagnosis preceded the formal generated-target inspect; the complete causal comparison was repeated after canonical capture.
- Raw CI bytes include terminal color escape sequences; the original log and its hash are retained separately from the readable ANSI-stripped derivative.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T120654Z-aerobactin-page-currency-initial-review
kind: record
repository: CultureBotAI/PathwayMech
title: Technical review of aerobactin generated-page currency after PR379 CI failure
started_at: '2026-10-11T12:05:40.229180Z'
finished_at: '2026-10-11T12:06:54.116485Z'
reviewer:
  identity: Codex independent publication reviewer (/root/verify_graph_publication)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer did not author the pathway, renderer, late REVIEW history
    event or Git publication. Reviewer authored the earlier scientific review described
    by the history event; that contribution is disclosed. This separate review independently
    compares the generated page with the current canonical rendering and exact remote
    CI logs, and does not reassess literature or its own prior scientific verdict.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: false
summary: 'One confirmed minor generated-artifact currency finding blocks required
  CI: the committed aerobactin page omits the final REVIEW history entry added after
  rendering. It exactly matches the canonical render with that one event removed.
  The scientific record and graph are unchanged; regenerate the page from all current
  maintained inputs.'
source:
  git_revision: 6647fd69597d516ca41dec6e6c8314032cbd7c3a
  state: git_commit
  inputs:
  - path: data/pathways/aerobactin-biosynthesis.yaml
    sha256: 3e4e50965749a9fa9dfe6319fd1462cc8329c10b7f4ab5363e7b486f2f32e3d4
    role: context
  - path: docs/record-review-profile.md
    sha256: a3d4b48de5f227515f9b5de12dd172cd1eb626068235b2b2e58bc4f6a5ee567d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/aerobactin-biosynthesis/2026-10-11T113540Z-codex-d73b1b.yaml
    sha256: 1761da323f010e69404d4ac4a8c0f377b667466a238167d1c0d476c23076741c
    role: context
  - path: history/records/aerobactin-biosynthesis/2026-10-11T115515Z-codex-9ae380.yaml
    sha256: 280fac9193ea88def809aa58b9bfb0ba84b187c1e81e9a23b22fe2de05b42928
    role: context
  - path: pages/records/GO_0019270.html
    sha256: abeb61a0d9deb317aaa009e9d92980068c9a95c112ae9d50fb1bf0c42c0ec174
    role: target
  - path: reviews/structured/20261011T115435Z-aerobactin-independent-review/review.yaml
    sha256: 99cd59a195e10988a0c0a5329d487c3dcca31eb90a6c0fa2ae836e8978c9083d
    role: context
  - path: src/pathwaymech/cli.py
    sha256: ab045fb947cfb93323886079abc2e7632d292679b2866fa7a0e39719310cc738
    role: context
  - path: tests/test_render_pages.py
    sha256: 80191f1e0f928eab1698e64c3ead7add2d9550e82c1fe0a23d6989cfda9a2308
    role: context
scope:
  description: Exact generated aerobactin page at PR379 head6647fd6, its maintained
    record/history owners, renderer and remote CI failure.
  selection: Explicit parent assignment following the isolated stale-page CI test
    failure.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0019270#generated-page
  exclusions:
  - target: Fresh biochemical/literature review and other pathway pages
    reason: This is a bounded technical generated-artifact assessment; the prior scientific
      review remains immutable.
targets:
- target_id: GO:0019270#generated-page
  path: pages/records/GO_0019270.html
  label: Generated aerobactin record page
  kind: generated
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/aerobactin-biosynthesis.yaml
    role: maintained_scientific_source
  - repository: CultureBotAI/PathwayMech
    path: history/records/aerobactin-biosynthesis/2026-10-11T115515Z-codex-9ae380.yaml
    role: maintained_history_source
  - repository: CultureBotAI/PathwayMech
    path: src/pathwaymech/cli.py
    role: canonical_page_renderer
checks:
- check_id: c-inspect
  name: Canonical generated-target inspection
  status: passed
  required: true
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-pr379-page-currency-review/targets.yaml
    --input data/pathways/aerobactin-biosynthesis.yaml --input history/records/aerobactin-biosynthesis/2026-10-11T113540Z-codex-d73b1b.yaml
    --input history/records/aerobactin-biosynthesis/2026-10-11T115515Z-codex-9ae380.yaml
    --input src/pathwaymech/cli.py --input tests/test_render_pages.py --input reviews/structured/20261011T115435Z-aerobactin-independent-review/review.yaml
    --input docs/record-reviews.md --input docs/record-review-profile.md
  exit_code: 0
  summary: Actual session33611 completed0 before formal assessment. All9 inputs rechecked
    against current bytes and exact published Git tree.
  target_ids:
  - GO:0019270#generated-page
  evidence_ids:
  - e-capture
- check_id: c-ci-test
  name: Exact-head remote full test suite
  status: failed
  required: true
  command: uv run --locked --extra dev pytest -q
  exit_code: 1
  expected_exit_code: 0
  summary: Run38137531447/job114464375650 at head6647fd6:1failed1126passed7skipped3warnings184.86s.
    Sole failure test_the_committed_site_is_current identifies pages/records/GO_0019270.html;
    remote quality gate was skipped.
  target_ids:
  - GO:0019270#generated-page
  evidence_ids:
  - e-ci
  scope_note: Root-executed remote GitHub Actions command observed from exact raw
    job log; not a new local full-suite run.
- check_id: c-lint
  name: Exact-head remote lint
  status: passed
  required: false
  command: uv run --locked --extra dev ruff check .
  exit_code: 0
  summary: Remote lint step passed before the failed test step.
  target_ids:
  - GO:0019270#generated-page
  evidence_ids:
  - e-ci
- check_id: c-delta
  name: Read-only canonical-render causal comparison
  status: passed
  required: true
  command: 'PYTHONPATH=src .venv/bin/python inline diagnostic: validate_record, load_site_history,
    _record_page; compare full history versus history excluding final REVIEW event;
    write external expected page and delta'
  exit_code: 0
  summary: Committed page equals exactly the rendering without final REVIEW history,
    and differs from full current rendering only by that history list item. No maintained
    file written.
  target_ids:
  - GO:0019270#generated-page
  evidence_ids:
  - e-delta
  - e-history
  - e-renderer
evidence:
- evidence_id: e-capture
  kind: validation
  reference: /private/tmp/pathwaymech-pr379-page-currency-review/inspect.json
  locator: Canonical source and target capture;9tracked files independently verified
    with git show at6647fd6
  accessed_at: '2026-10-11T12:06:54.116485Z'
  support: supports
  summary: Exact current and committed input bytes agree. The observation uses git_commit
    provenance for this CI-failed published revision.
  snapshot_sha256: 3a728479a045c1c5c9b584ff509a95480829bd63378fc1c38ccac24da98bd2dd
- evidence_id: e-ci
  kind: validation
  reference: https://github.com/CultureBotAI/PathwayMech/actions/runs/38137531447/job/114464375650
  locator: Test step, captured stderr, finalpytestsummary; exact raw job log /private/tmp/pathwaymech-pr379-failed-job.log
  accessed_at: '2026-10-11T12:06:54.116485Z'
  support: refutes
  summary: Sole failed test names the aerobactin generated page as stale. Full test
    summary is1failed1126passed7skipped; lint passed and later quality gate skipped.
  snapshot_sha256: be714c3a4f3b0f1fd158179c520bca70539588da17acd6175b28258f405cff96
- evidence_id: e-delta
  kind: validation
  reference: /private/tmp/pathwaymech-pr379-page-currency-review/diagnosis.json
  locator: Canonical _record_page full-history comparison and exact equality with
    final REVIEW event removed; external page diff
  accessed_at: '2026-10-11T12:06:54.116485Z'
  support: supports
  summary: Old page SHAabeb61a0 has125540bytes; full current render SHAb5874ada has126680bytes.
    The only delta is the missing final REVIEW history list item.
  snapshot_sha256: a4f822ff8664a79ab9e3e8eca1494830951c3c24a613d8a902cc372b08323721
- evidence_id: e-history
  kind: record_content
  reference: history/records/aerobactin-biosynthesis/2026-10-11T115515Z-codex-9ae380.yaml
  locator: Entire REVIEW event and session timestamp11:55:15Z
  accessed_at: '2026-10-11T12:06:54.116485Z'
  support: supports
  summary: The history is a maintained input added after the sealed scientific-review
    rendering; it truthfully describes the saved review and does not change science.
  snapshot_sha256: 280fac9193ea88def809aa58b9bfb0ba84b187c1e81e9a23b22fe2de05b42928
- evidence_id: e-renderer
  kind: record_content
  reference: src/pathwaymech/cli.py
  locator: render_site lines181–204; render_pages_main lines322–367; _record_page
    history_html call
  accessed_at: '2026-10-11T12:06:54.116485Z'
  support: supports
  summary: Canonical page currency depends on both record YAML and record history.
    Rerender is required after adding a history event.
  snapshot_sha256: ab045fb947cfb93323886079abc2e7632d292679b2866fa7a0e39719310cc738
- evidence_id: e-prior
  kind: prior_review
  reference: reviews/structured/20261011T115435Z-aerobactin-independent-review/review.yaml
  locator: Entire original scientific review; generated-page hash and input scope
  accessed_at: '2026-10-11T12:06:54.116485Z'
  support: context_only
  summary: Earlier science review remains an immutable observation of its actually
    inspected inputs. This technical finding does not overturn the source-based scientific
    assessment or silently refresh that historical page hash.
  snapshot_sha256: 99cd59a195e10988a0c0a5329d487c3dcca31eb90a6c0fa2ae836e8978c9083d
assessments:
- assessment_id: a-currency
  area: consistency
  topic: Generated page agrees with current maintained history
  outcome: concern
  summary: Page is stale by one final REVIEW history list item; exact remote test
    and local causal comparison agree.
  target_ids:
  - GO:0019270#generated-page
  evidence_ids:
  - e-ci
  - e-delta
  - e-history
  - e-renderer
- assessment_id: a-owner
  area: ownership
  topic: Bounded canonical regeneration without scientific changes
  outcome: supported
  summary: The owner inputs are already correct. Rerun the canonical renderer after
    the final history event; do not hand-edit HTML, rewrite the original scientific
    review, or create another record REVIEW history solely for this refresh.
  target_ids:
  - GO:0019270#generated-page
  evidence_ids:
  - e-delta
  - e-history
  - e-renderer
  - e-prior
findings:
- finding_id: f-post-review-page-currency
  issue_key: aerobactin-post-review-page-currency
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Aerobactin page predates its final review-history event
  description: Required CI fails because pages/records/GO_0019270.html lacks the11:55:15REVIEW
    history event. The page exactly matches the current renderer when that single
    event is removed. Scientific YAML, graph/evidence and renderer are unchanged.
  target_ids:
  - GO:0019270#generated-page
  field_paths:
  - pages/records/GO_0019270.html::curation-history
  evidence_ids:
  - e-ci
  - e-delta
  - e-history
  - e-renderer
  rule_id: tests/test_render_pages.py::test_the_committed_site_is_current
  native_severity: minor generated-artifact drift; publication-blocking required check
  normalization_reason: The missing history display is a bounded provenance/currency
    defect, not wrong biological identity or unsupported science. It must nevertheless
    be fixed before required CI can pass.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/aerobactin-biosynthesis.yaml
    role: maintained_scientific_source
  - repository: CultureBotAI/PathwayMech
    path: history/records/aerobactin-biosynthesis/2026-10-11T115515Z-codex-9ae380.yaml
    role: maintained_history_source
  - repository: CultureBotAI/PathwayMech
    path: src/pathwaymech/cli.py
    role: canonical_page_renderer
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/380
actions:
- action_id: a-rerender
  description: Regenerate pages through the canonical renderer after the final history
    event; commit only the expected generated delta plus new append-only technical
    review/receipts as needed.
  finding_ids:
  - f-post-review-page-currency
  target_ids:
  - GO:0019270#generated-page
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/aerobactin-biosynthesis.yaml
    role: maintained_scientific_source
  - repository: CultureBotAI/PathwayMech
    path: history/records/aerobactin-biosynthesis/2026-10-11T115515Z-codex-9ae380.yaml
    role: maintained_history_source
  - repository: CultureBotAI/PathwayMech
    path: src/pathwaymech/cli.py
    role: canonical_page_renderer
  generator: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just render-pages
  acceptance_checks:
  - Expected rendered page SHA b5874ada97fa95703f265b5a5f58ffe07f94b559d8fe0b0013f7c092a3f29fb5
    if maintained inputs remain unchanged.
  - Fresh canonical page --check and test_the_committed_site_is_current pass; full
    QC and exact-head remote required CI pass.
  - Scientific YAML, graph/evidence/download bytes and original canonical scientific
    review remain unchanged; preserve historical source inputs.
  - Save a linked technical successor with the same issue_key and explicit previous_occurrences
    after observed correction/checks; do not add a new record REVIEW history for this
    technical refresh.
limitations:
- This technical observation does not repeat primary literature review and does not
  claim a current full-suite pass.
- Required remote full tests failed; remote quality gate was skipped. Initial local
  full gates from the prior scientific review preceded the added REVIEW history event.
- No generated page or scientific source was modified by this reviewer; the external
  expected render is diagnostic only.
notes:
- Preliminary read-only CI diagnosis preceded the formal generated-target inspect;
  the complete causal comparison was repeated after canonical capture.
- Raw CI bytes include terminal color escape sequences; the original log and its hash
  are retained separately from the readable ANSI-stripped derivative.
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261011T115435Z-aerobactin-independent-review
  relationship: Separate later technical page-currency observation; original scientific
    review retained unchanged.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/380
- https://github.com/CultureBotAI/PathwayMech/pull/379
```
