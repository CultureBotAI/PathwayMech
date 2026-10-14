# Gentisate integration review: retained executable helpers fail required lint

- Review: 20261014T122806Z-gentisate251-integration-initial
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T12:15:32Z
- Finished UTC: 2026-10-14T12:28:06Z
- Reviewer: Codex /root/next251_integration_review (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

The final pathway representation and generated graph/export pass the independent integration audit, but six copied author-helper Python files introduce 108 Ruff violations. Remaining native full-suite gates are still running; this observation does not certify scientific support.

## Scope And Provenance

One gentisate record and its newly retained research integration; initial observation of a confirmed mandatory lint defect.

Selection: The sole new next251 record MetaCyc:PWY-6223 and retained helper artifacts in its dossier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cd42a526b06ce531e8326a2717d54d7ff770bd2b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-6223 | data/pathways/gentisate-degradation-i.yaml | maintained | gentisate degradation I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Retained executable helper lint | failed | True | MetaCyc:PWY-6223 | All six author helper Python files are lint-selected and produce 108 violations, preventing the required repository lint gate. |
| Remaining required native gates | unavailable | True | MetaCyc:PWY-6223 | The author runner completed render-pages and validate but is still running the full test suite; final test/lint/vendored/diff receipts are not yet available. |

## Scientific And Domain Assessments

### Required lint compatibility of retained research helpers

consistency: concern. Targets: MetaCyc:PWY-6223.

Exact external author scripts were copied as active .py files even though they are source artifacts; repository-wide Ruff selects them and fails.

## Findings

### retained-helper-lint: Retained author helpers fail required repository lint

major / open / confirmed; issue key: gentisate251-retained-helper-lint.

Six newly retained native helper files end in .py and are therefore active Python inputs to just lint. Independent Ruff reports 108 violations. Preserve the original bytes as explicitly typed text artifacts with corrected retention bindings, or maintain lint-compliant scripts with distinct source-original provenance.

## Recommended Actions And Acceptance Checks

### retain-helpers-as-artifacts

Preserve the six original helper byte streams as text artifacts and update retained-projection paths and replay instructions without changing their original hashes.

- All six retained text artifacts have hashes identical to the original helpers and their prior recorded hashes.
- No new helper .py path remains in the next251 dossier, including hidden/ignored files.
- Retained-projections and reproduction instructions identify the actual text-artifact paths and original source paths.
- The complete required just lint gate passes after the retention correction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| helper-lint | research/pathway_additions/2026-10-14-next-251/gentisate/integration-review/native-helper-lint.json; 108 Ruff diagnostics across the six native/*.py author helpers; exact command receipt in native-helper-lint-receipt.json | supports | Independent focused Ruff invocation exited 1; errors include import ordering, long lines, multiple statements, unused imports and ambiguous variables. |

## Limits And Additional Notes

- This is non-scientific integration review; literature support is not reassessed.
- The full native gate sequence is still running, so completion is partial.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T122806Z-gentisate251-integration-initial
kind: record
repository: CultureBotAI/PathwayMech
title: 'Gentisate integration review: retained executable helpers fail required lint'
started_at: '2026-10-14T12:15:32Z'
finished_at: '2026-10-14T12:28:06Z'
reviewer:
  identity: Codex /root/next251_integration_review
  kind: agent
  independence: independent
  independence_basis: No authorship of the pathway, authorities, retained research
    or product code. Independently replayed authority builders, record/KGX/diagram
    fidelity and provenance audits, then ran the focused lint diagnostic.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: false
summary: The final pathway representation and generated graph/export pass the independent
  integration audit, but six copied author-helper Python files introduce 108 Ruff
  violations. Remaining native full-suite gates are still running; this observation
  does not certify scientific support.
source:
  git_revision: cd42a526b06ce531e8326a2717d54d7ff770bd2b
  state: working_tree
  inputs:
  - path: data/pathways/gentisate-degradation-i.yaml
    sha256: 272e475b3bb872475bba938c5e5016b52b63e21dc8c9dea772e25ba78524c064
    role: target
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/integration-review/native-helper-lint.json
    sha256: 9f97cb4490f0cc11a8dd3b04907afbd8f0ce317fc91f8399f3553b7f888afccb
    role: context
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/native/acquire.py
    sha256: 71ee0feb91039a3f89b3b1932e7c665245a42fa3965c37ba46bd15209b7975b6
    role: context
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/native/close_cofactors.py
    sha256: 5a1d20dc2b65bdcc11cb79bd099818377a6759c84834b3bc05957f469a079e6c
    role: context
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/native/close_variant_cofactors.py
    sha256: a76c78a2cbd37bc01f6d3262f976970f1d04a3894144b783f6ce0cf6f1b66112
    role: context
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/native/draft_support.py
    sha256: fd74f0a307bc024e5fb60bcf88b42332e542c82aac8b547ac9b8b621b3f218d5
    role: context
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/native/finalize_handoff.py
    sha256: b7f121190090ef9cea5663ec8392adf3ab7acebd9e82ddbe56a8150c05328ca0
    role: context
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/native/project.py
    sha256: cd15b82ca1c0860610b4a7219c094d512449c9cb508a3e3178b8d3346951e8ea
    role: context
scope:
  description: One gentisate record and its newly retained research integration; initial
    observation of a confirmed mandatory lint defect.
  selection: The sole new next251 record MetaCyc:PWY-6223 and retained helper artifacts
    in its dossier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-6223
  exclusions:
  - target: Fresh literature interpretation
    reason: Assigned to a separate independent scientific reviewer.
  - target: Completion of remaining native gates
    reason: Author-owned full gate runner is still running; no future pass is assumed.
targets:
- target_id: MetaCyc:PWY-6223
  path: data/pathways/gentisate-degradation-i.yaml
  label: gentisate degradation I
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/gentisate-degradation-i.yaml
    role: maintained pathway record
checks:
- check_id: retained-helper-lint
  name: Retained executable helper lint
  status: failed
  required: true
  summary: All six author helper Python files are lint-selected and produce 108 violations,
    preventing the required repository lint gate.
  target_ids:
  - MetaCyc:PWY-6223
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/ruff check research/pathway_additions/2026-10-14-next-251/gentisate/native
    --output-format=json
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - helper-lint
- check_id: native-gates-pending
  name: Remaining required native gates
  status: unavailable
  required: true
  summary: The author runner completed render-pages and validate but is still running
    the full test suite; final test/lint/vendored/diff receipts are not yet available.
  target_ids:
  - MetaCyc:PWY-6223
evidence:
- evidence_id: helper-lint
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-251/gentisate/integration-review/native-helper-lint.json
  locator: 108 Ruff diagnostics across the six native/*.py author helpers; exact command
    receipt in native-helper-lint-receipt.json
  accessed_at: '2026-10-14T12:28:06Z'
  support: supports
  summary: Independent focused Ruff invocation exited 1; errors include import ordering,
    long lines, multiple statements, unused imports and ambiguous variables.
  snapshot_sha256: 9f97cb4490f0cc11a8dd3b04907afbd8f0ce317fc91f8399f3553b7f888afccb
assessments:
- assessment_id: retained-helper-integration
  area: consistency
  topic: Required lint compatibility of retained research helpers
  outcome: concern
  summary: Exact external author scripts were copied as active .py files even though
    they are source artifacts; repository-wide Ruff selects them and fails.
  target_ids:
  - MetaCyc:PWY-6223
  evidence_ids:
  - helper-lint
findings:
- finding_id: retained-helper-lint
  issue_key: gentisate251-retained-helper-lint
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Retained author helpers fail required repository lint
  description: Six newly retained native helper files end in .py and are therefore
    active Python inputs to just lint. Independent Ruff reports 108 violations. Preserve
    the original bytes as explicitly typed text artifacts with corrected retention
    bindings, or maintain lint-compliant scripts with distinct source-original provenance.
  target_ids:
  - MetaCyc:PWY-6223
  field_paths:
  - research/pathway_additions/2026-10-14-next-251/gentisate/native/acquire.py
  - research/pathway_additions/2026-10-14-next-251/gentisate/native/close_cofactors.py
  - research/pathway_additions/2026-10-14-next-251/gentisate/native/close_variant_cofactors.py
  - research/pathway_additions/2026-10-14-next-251/gentisate/native/draft_support.py
  - research/pathway_additions/2026-10-14-next-251/gentisate/native/finalize_handoff.py
  - research/pathway_additions/2026-10-14-next-251/gentisate/native/project.py
  evidence_ids:
  - helper-lint
  rule_id: docs/CURATION.md required review gates; justfile lint
  native_severity: major
  normalization_reason: A confirmed integration defect prevents a required CI gate;
    the biological record itself is not invalidated.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/acquire.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/close_cofactors.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/close_variant_cofactors.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/draft_support.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/finalize_handoff.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/project.py
    role: retained author helper artifact
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/529
actions:
- action_id: retain-helpers-as-artifacts
  description: Preserve the six original helper byte streams as text artifacts and
    update retained-projection paths and replay instructions without changing their
    original hashes.
  finding_ids:
  - retained-helper-lint
  target_ids:
  - MetaCyc:PWY-6223
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/acquire.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/close_cofactors.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/close_variant_cofactors.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/draft_support.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/finalize_handoff.py
    role: retained author helper artifact
  - repository: CultureBotAI/PathwayMech
    path: research/pathway_additions/2026-10-14-next-251/gentisate/native/project.py
    role: retained author helper artifact
  acceptance_checks:
  - All six retained text artifacts have hashes identical to the original helpers
    and their prior recorded hashes.
  - No new helper .py path remains in the next251 dossier, including hidden/ignored
    files.
  - Retained-projections and reproduction instructions identify the actual text-artifact
    paths and original source paths.
  - The complete required just lint gate passes after the retention correction.
limitations:
- This is non-scientific integration review; literature support is not reassessed.
- The full native gate sequence is still running, so completion is partial.
tags:
- integration
- gentisate
- next251
```
