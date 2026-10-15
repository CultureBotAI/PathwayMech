# Initial independent scientific observation: catechol degradation I

- Review: 20261015T025017Z-pwy5415-independent-science-initial
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-15T02:41:42Z
- Finished UTC: 2026-10-15T02:50:17Z
- Reviewer: Codex /root/next261_science_review (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole integrated target read and actionable primary evidence-format defect confirmed. Initial observation only; full source-to-record coverage assessment and shared required gates are pending. Formal five-step chemistry independently agrees with issuing structures/directions and balances atoms/charge.

## Scope And Provenance

Independent whole-record scientific review in progress; this initial observation records an immediately actionable evidence-format defect.

Selection: New maintained MetaCyc:PWY-5415 record supplied by parent at SHA256 38b3460b24131e7ee2d442e23d226618557bbc5ba56181d7ef9de9ac9e2a0255.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 62b8798b0044f422a59f1527b0801ff09a27d368.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5415 | data/pathways/catechol-degradation-i.yaml | maintained | catechol degradation I (meta-cleavage pathway) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical inspect and full target read | passed | True | MetaCyc:PWY-5415 | record_review.py inspect exit 0; actual target hash verified; all 3018 lines inspected. Initial invalid target-kind metadata was corrected to maintained before this observation. |
| Original source integrity and formal chemistry | passed | True | MetaCyc:PWY-5415 | Rehashed 493 native,18 chemistry,69 primary,72 primary integration,257 native foundation files with no mismatches. Independently replayed actual complete Rhea RDF/direction source, actual ChEBI SQL structures and 5 native equations; 16 chemical identity comparisons and all 5 atom/charge balances passed. |
| Full source-to-record scientific coverage | unavailable | True | MetaCyc:PWY-5415 | In progress; remaining descriptive claim/source coverage and review handoff have not yet been finalized. |
| Shared validate/test/lint/render/KGX/diff gates | unavailable | True | MetaCyc:PWY-5415 | Parent will run canonical shared corpus gates after repairs; none claimed passed by this initial observation. |

## Scientific And Domain Assessments

### Primary graph evidence format

representation: concern. Targets: MetaCyc:PWY-5415.

The 35 evidence occurrences on primary-p001–primary-p016 (28 edge evidence entries and 7 endpoint-qualifier entries; 18 unique assertions) use source_assertion for narrative methods/results/discussion/abstract summaries, citing transformed page/line ranges and an authored claim ledger rather than a native structured statement. This violates the evidence representation rule even where the scientific content is supported. Eight occurrences have mixed table/narrative support (F04, F05, K07 and the 1996 preparation); those can be repaired with exact table facts and row/column locators, while their prose claims require short verified quotes or separate description. Native MetaCyc XML assertions are outside this finding. The complete item-by-item set and classifications are retained in primary-evidence-item-audit.initial.json.

## Findings

### SCI-F01: Primary narrative paraphrases are stored as structured-source assertions

major / open / confirmed; issue key: pwy5415-primary-evidence-representation.

The 35 evidence occurrences on primary-p001–primary-p016 (28 edge evidence entries and 7 endpoint-qualifier entries; 18 unique assertions) use source_assertion for narrative methods/results/discussion/abstract summaries, citing transformed page/line ranges and an authored claim ledger rather than a native structured statement. This violates the evidence representation rule even where the scientific content is supported. Eight occurrences have mixed table/narrative support (F04, F05, K07 and the 1996 preparation); those can be repaired with exact table facts and row/column locators, while their prose claims require short verified quotes or separate description. Native MetaCyc XML assertions are outside this finding. The complete item-by-item set and classifications are retained in primary-evidence-item-audit.initial.json.

## Recommended Actions And Acceptance Checks

### SCI-ACT01

Repair the complete 35-item primary evidence set while preserving supported catalytic, regulatory, assembly and preparation claims.

- Every narrative support item uses an exact short excerpt from the inspected source, or a faithful native structured statement with an original field/table locator.
- Exact table-derived statements distinguish data rows/columns from prose interpretation; pRO1985 enzyme assay and pRO1996 growth preparations remain separate.
- All endpoint qualifier assertions remain independently supported for their exact host/construct/molecular state.
- Keep per-source quotation totals short; do not relabel paraphrases as quotations or cite an authored ledger as upstream authority.
- Reinspect final maintained bytes and regenerate/rerun required shared gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EV-rule | docs/CAUSAL_GRAPHS.md; lines 95–110 | supports | Evidence must use either a short verbatim quote or a faithful inspected structured source statement with locator for its native triple/object/JSON path/XML element. A generated sentence is not a quotation. |
| EV-target | data/pathways/catechol-degradation-i.yaml; mechanistic_edges primary-p001–primary-p016, all 35 primary evidence items including 7 qualifier evidence occurrences | supports | All primary evidence items use source_assertion. Locators are publisher page/extraction lines, indexed abstract descriptions and author claim-ledger anchors. Several statements have genuine table support, but none currently identifies a native structured statement; many are purely narrative paraphrases. Full 3018-line target read. |
| EV-23237860 | https://pubmed.ncbi.nlm.nih.gov/23237860/; PubMed indexed abstract | supports | The actual indexed abstract supports active monomeric MhpF; p014 edge and qualifier nevertheless paraphrase it as source_assertion with no native field locator. |
| EV-7890778 | https://pubmed.ncbi.nlm.nih.gov/7890778/; indexed abstract sentences 1–5 | supports | Actual indexed abstract supports XylF 3-alkylcatechol-product hydrolysis; p013 paraphrases narrative abstract. |
| EV-8419288 | https://journals.asm.org/doi/pdf/10.1128/jb.175.2.377-385.1993?download=true; publisher transformed text pp377–385; Table1, Table2, Fig2/Fig6 captions, results/discussion | supports | Scientific claims were independently checked in original publisher transformed text. F01,F06,F09,F10,F11,F13 are narrative; F04/F05 have actual table data that can support more precise structured assertions. |
| EV-2681159 | https://journals.asm.org/doi/pdf/10.1128/jb.171.11.6251-6258.1989?download=true; publisher transformed text pp6252,6256–6257 | supports | H01/H08 are narrative methods/results statements, not identified native structured objects. |
| EV-1856161 | https://journals.asm.org/doi/pdf/10.1128/jb.173.15.4587-4594.1991?download=true; publisher transformed text p4588 methods; p4590 Fig3/results; p4592 Table5 and following prose | supports | K02/K03 are narrative synthesis. K07 combines pRO1985 table activities with a distinct pRO1996 growth report; separate table support from prose. |
| EV-12764229 | https://www.pnas.org/doi/pdf/10.1073/pnas.1236794100; publisher transformed text p6993 L94–115 | supports | S01 biological tetramer/catalytic-pair conclusion occurs in narrative structural description, not a native structured field. |
| EV-8633871 | https://journals.asm.org/doi/pdf/10.1128/aem.62.5.1728-1740.1996?download=true; publisher transformed text p1729 methods L113–119; p1732 Tables2–3 L390–415 | supports | Partial-purification and construct identity come from methods prose; kinetic tables provide separate actual structured facts. |

## Limits And Additional Notes

- Initial needs_curation observation; required full gates and final full coverage judgment remain pending.
- Primary papers were inspected as publisher transformed text, not raw PDF pages or figure images. Several sources are abstract-only; PNAS structural source limited to pages 6992–6993.
- No maintained/Git/GitHub mutations performed by this reviewer.
- Source-preparation checks began before record integration; 02:41:42Z is actual canonical target-inspection start.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T025017Z-pwy5415-independent-science-initial
kind: record
repository: CultureBotAI/PathwayMech
title: 'Initial independent scientific observation: catechol degradation I'
started_at: '2026-10-15T02:41:42Z'
finished_at: '2026-10-15T02:50:17Z'
reviewer:
  identity: Codex /root/next261_science_review
  kind: agent
  independence: independent
  independence_basis: Did not author or modify maintained record or source integration;
    independently read original native XML, Rhea RDF/directions, ChEBI SQL and bounded
    primary source text before inspecting actual integrated target.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Whole integrated target read and actionable primary evidence-format defect
  confirmed. Initial observation only; full source-to-record coverage assessment and
  shared required gates are pending. Formal five-step chemistry independently agrees
  with issuing structures/directions and balances atoms/charge.
source:
  git_revision: 62b8798b0044f422a59f1527b0801ff09a27d368
  state: working_tree
  inputs:
  - path: data/pathways/catechol-degradation-i.yaml
    sha256: 38b3460b24131e7ee2d442e23d226618557bbc5ba56181d7ef9de9ac9e2a0255
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: review_rubric
scope:
  description: Independent whole-record scientific review in progress; this initial
    observation records an immediately actionable evidence-format defect.
  selection: New maintained MetaCyc:PWY-5415 record supplied by parent at SHA256 38b3460b24131e7ee2d442e23d226618557bbc5ba56181d7ef9de9ac9e2a0255.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5415
targets:
- target_id: MetaCyc:PWY-5415
  path: data/pathways/catechol-degradation-i.yaml
  label: catechol degradation I (meta-cleavage pathway)
  kind: maintained
  ownership_note: Maintained YAML record; generated page is owned by the pathway renderer.
checks:
- check_id: target-inspection
  name: Canonical inspect and full target read
  status: passed
  required: true
  summary: record_review.py inspect exit 0; actual target hash verified; all 3018
    lines inspected. Initial invalid target-kind metadata was corrected to maintained
    before this observation.
  target_ids:
  - MetaCyc:PWY-5415
  command: PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python
    -B scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-261-independent-science/targets.yaml
  exit_code: 0
- check_id: originals-replay
  name: Original source integrity and formal chemistry
  status: passed
  required: true
  summary: Rehashed 493 native,18 chemistry,69 primary,72 primary integration,257
    native foundation files with no mismatches. Independently replayed actual complete
    Rhea RDF/direction source, actual ChEBI SQL structures and 5 native equations;
    16 chemical identity comparisons and all 5 atom/charge balances passed.
  target_ids:
  - MetaCyc:PWY-5415
- check_id: full-source-coverage
  name: Full source-to-record scientific coverage
  status: unavailable
  required: true
  summary: In progress; remaining descriptive claim/source coverage and review handoff
    have not yet been finalized.
  target_ids:
  - MetaCyc:PWY-5415
- check_id: shared-gates
  name: Shared validate/test/lint/render/KGX/diff gates
  status: unavailable
  required: true
  summary: Parent will run canonical shared corpus gates after repairs; none claimed
    passed by this initial observation.
  target_ids:
  - MetaCyc:PWY-5415
evidence:
- evidence_id: EV-rule
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: lines 95–110
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: Evidence must use either a short verbatim quote or a faithful inspected
    structured source statement with locator for its native triple/object/JSON path/XML
    element. A generated sentence is not a quotation.
  snapshot_sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
- evidence_id: EV-target
  kind: record_content
  reference: data/pathways/catechol-degradation-i.yaml
  locator: mechanistic_edges primary-p001–primary-p016, all 35 primary evidence items
    including 7 qualifier evidence occurrences
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: All primary evidence items use source_assertion. Locators are publisher
    page/extraction lines, indexed abstract descriptions and author claim-ledger anchors.
    Several statements have genuine table support, but none currently identifies a
    native structured statement; many are purely narrative paraphrases. Full 3018-line
    target read.
  snapshot_sha256: 38b3460b24131e7ee2d442e23d226618557bbc5ba56181d7ef9de9ac9e2a0255
- evidence_id: EV-23237860
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/23237860/
  locator: PubMed indexed abstract
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: The actual indexed abstract supports active monomeric MhpF; p014 edge and
    qualifier nevertheless paraphrase it as source_assertion with no native field
    locator.
  snapshot_sha256: aa060f8fc9db83b948edd3a1909932720ddc3671b88648f273c5d82d1c0aa862
- evidence_id: EV-7890778
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/7890778/
  locator: indexed abstract sentences 1–5
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: Actual indexed abstract supports XylF 3-alkylcatechol-product hydrolysis;
    p013 paraphrases narrative abstract.
  snapshot_sha256: 04d7c2181d93fc4eda6dcbe37e56045811e66fe7b820a6efcd5fa43dbc42c355
- evidence_id: EV-8419288
  kind: primary_source
  reference: https://journals.asm.org/doi/pdf/10.1128/jb.175.2.377-385.1993?download=true
  locator: publisher transformed text pp377–385; Table1, Table2, Fig2/Fig6 captions,
    results/discussion
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: Scientific claims were independently checked in original publisher transformed
    text. F01,F06,F09,F10,F11,F13 are narrative; F04/F05 have actual table data that
    can support more precise structured assertions.
  snapshot_sha256: 5393894d821b69e824408098aa702f2da2a84422be7c4682b1afc2455511c8ad
- evidence_id: EV-2681159
  kind: primary_source
  reference: https://journals.asm.org/doi/pdf/10.1128/jb.171.11.6251-6258.1989?download=true
  locator: publisher transformed text pp6252,6256–6257
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: H01/H08 are narrative methods/results statements, not identified native
    structured objects.
  snapshot_sha256: 0392ce2bf76757f72132a0be2b0bcc4fd24af531286e06362535299034a7a0c1
- evidence_id: EV-1856161
  kind: primary_source
  reference: https://journals.asm.org/doi/pdf/10.1128/jb.173.15.4587-4594.1991?download=true
  locator: publisher transformed text p4588 methods; p4590 Fig3/results; p4592 Table5
    and following prose
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: K02/K03 are narrative synthesis. K07 combines pRO1985 table activities
    with a distinct pRO1996 growth report; separate table support from prose.
  snapshot_sha256: 581fdcf0cd875066952b2c0a10f2ef971e99c0841471f062f39fe26c1a77133e
- evidence_id: EV-12764229
  kind: primary_source
  reference: https://www.pnas.org/doi/pdf/10.1073/pnas.1236794100
  locator: publisher transformed text p6993 L94–115
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: S01 biological tetramer/catalytic-pair conclusion occurs in narrative structural
    description, not a native structured field.
  snapshot_sha256: 7d7a4d836066c5596ab60f06f4f6f6009337aecf8391269b3a0d2ac83620d0cc
- evidence_id: EV-8633871
  kind: primary_source
  reference: https://journals.asm.org/doi/pdf/10.1128/aem.62.5.1728-1740.1996?download=true
  locator: publisher transformed text p1729 methods L113–119; p1732 Tables2–3 L390–415
  accessed_at: '2026-10-15T02:50:17Z'
  support: supports
  summary: Partial-purification and construct identity come from methods prose; kinetic
    tables provide separate actual structured facts.
  snapshot_sha256: a26e4f7f7c7f3dfc1da2bd415b7d9a053c864d79944700f50e73c48b5b633426
assessments:
- assessment_id: SCI-A01
  area: representation
  topic: Primary graph evidence format
  outcome: concern
  summary: The 35 evidence occurrences on primary-p001–primary-p016 (28 edge evidence
    entries and 7 endpoint-qualifier entries; 18 unique assertions) use source_assertion
    for narrative methods/results/discussion/abstract summaries, citing transformed
    page/line ranges and an authored claim ledger rather than a native structured
    statement. This violates the evidence representation rule even where the scientific
    content is supported. Eight occurrences have mixed table/narrative support (F04,
    F05, K07 and the 1996 preparation); those can be repaired with exact table facts
    and row/column locators, while their prose claims require short verified quotes
    or separate description. Native MetaCyc XML assertions are outside this finding.
    The complete item-by-item set and classifications are retained in primary-evidence-item-audit.initial.json.
  target_ids:
  - MetaCyc:PWY-5415
  evidence_ids:
  - EV-rule
  - EV-target
  - EV-23237860
  - EV-7890778
  - EV-8419288
  - EV-2681159
  - EV-1856161
  - EV-12764229
  - EV-8633871
findings:
- finding_id: SCI-F01
  issue_key: pwy5415-primary-evidence-representation
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Primary narrative paraphrases are stored as structured-source assertions
  description: The 35 evidence occurrences on primary-p001–primary-p016 (28 edge evidence
    entries and 7 endpoint-qualifier entries; 18 unique assertions) use source_assertion
    for narrative methods/results/discussion/abstract summaries, citing transformed
    page/line ranges and an authored claim ledger rather than a native structured
    statement. This violates the evidence representation rule even where the scientific
    content is supported. Eight occurrences have mixed table/narrative support (F04,
    F05, K07 and the 1996 preparation); those can be repaired with exact table facts
    and row/column locators, while their prose claims require short verified quotes
    or separate description. Native MetaCyc XML assertions are outside this finding.
    The complete item-by-item set and classifications are retained in primary-evidence-item-audit.initial.json.
  target_ids:
  - MetaCyc:PWY-5415
  field_paths:
  - mechanistic_edges[112].evidence[0]
  - mechanistic_edges[112].evidence[1]
  - mechanistic_edges[113].evidence[0]
  - mechanistic_edges[113].evidence[1]
  - mechanistic_edges[113].evidence[2]
  - mechanistic_edges[114].evidence[0]
  - mechanistic_edges[114].evidence[1]
  - mechanistic_edges[114].endpoint_qualifiers[0].evidence[0]
  - mechanistic_edges[115].evidence[0]
  - mechanistic_edges[115].evidence[1]
  - mechanistic_edges[116].evidence[0]
  - mechanistic_edges[117].evidence[0]
  - mechanistic_edges[118].evidence[0]
  - mechanistic_edges[119].evidence[0]
  - mechanistic_edges[119].evidence[1]
  - mechanistic_edges[119].evidence[2]
  - mechanistic_edges[120].evidence[0]
  - mechanistic_edges[120].evidence[1]
  - mechanistic_edges[120].evidence[2]
  - mechanistic_edges[121].evidence[0]
  - mechanistic_edges[121].evidence[1]
  - mechanistic_edges[121].endpoint_qualifiers[0].evidence[0]
  - mechanistic_edges[122].evidence[0]
  - mechanistic_edges[122].evidence[1]
  - mechanistic_edges[122].endpoint_qualifiers[0].evidence[0]
  - mechanistic_edges[123].evidence[0]
  - mechanistic_edges[123].evidence[1]
  - mechanistic_edges[123].endpoint_qualifiers[0].evidence[0]
  - mechanistic_edges[124].evidence[0]
  - mechanistic_edges[125].evidence[0]
  - mechanistic_edges[125].endpoint_qualifiers[0].evidence[0]
  - mechanistic_edges[126].evidence[0]
  - mechanistic_edges[126].endpoint_qualifiers[0].evidence[0]
  - mechanistic_edges[127].evidence[0]
  - mechanistic_edges[127].endpoint_qualifiers[0].evidence[0]
  evidence_ids:
  - EV-rule
  - EV-target
  - EV-23237860
  - EV-7890778
  - EV-8419288
  - EV-2681159
  - EV-1856161
  - EV-12764229
  - EV-8633871
  rule_id: docs/CAUSAL_GRAPHS.md:97–102
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/catechol-degradation-i.yaml
    role: maintained scientific record
actions:
- action_id: SCI-ACT01
  description: Repair the complete 35-item primary evidence set while preserving supported
    catalytic, regulatory, assembly and preparation claims.
  finding_ids:
  - SCI-F01
  target_ids:
  - MetaCyc:PWY-5415
  acceptance_checks:
  - Every narrative support item uses an exact short excerpt from the inspected source,
    or a faithful native structured statement with an original field/table locator.
  - Exact table-derived statements distinguish data rows/columns from prose interpretation;
    pRO1985 enzyme assay and pRO1996 growth preparations remain separate.
  - All endpoint qualifier assertions remain independently supported for their exact
    host/construct/molecular state.
  - Keep per-source quotation totals short; do not relabel paraphrases as quotations
    or cite an authored ledger as upstream authority.
  - Reinspect final maintained bytes and regenerate/rerun required shared gates.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/catechol-degradation-i.yaml
    role: maintained scientific record
limitations:
- Initial needs_curation observation; required full gates and final full coverage
  judgment remain pending.
- Primary papers were inspected as publisher transformed text, not raw PDF pages or
  figure images. Several sources are abstract-only; PNAS structural source limited
  to pages 6992–6993.
- No maintained/Git/GitHub mutations performed by this reviewer.
- Source-preparation checks began before record integration; 02:41:42Z is actual canonical
  target-inspection start.
```
