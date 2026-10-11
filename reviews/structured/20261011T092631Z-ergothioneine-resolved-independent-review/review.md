# Independent ergothioneine successor review: verified EgtD scope correction

- Review: 20261011T092631Z-ergothioneine-resolved-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T09:19:41Z
- Finished UTC: 2026-10-11T09:26:31Z
- Reviewer: Codex independent reviewer (/root/pathway_authority_cache) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete seven-step bacterial pathway is supported with explicit strain, evidence-tier and donor limitations. Issue 371 is resolved by removing the exact-protein inhibition edge while retaining the measured preparation as context. Independent replay verified 54 original source bodies, 33 chemical sides, seven balances and all 54 edges with 100 evidence blocks. Final coordinated checks passed. There are no unresolved findings in this one-record scope.

## Scope And Provenance

Full independent scientific assessment of the corrected target, including explicit reassessment of all changed input bytes, the initial finding and its original sources. Final coordinated gate and generated-artifact receipts were inspected.

Selection: Corrected target SHA-256 238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527; one exact predecessor finding.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c555ecacc2b2708b246a68dcc9b64444791f526.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-7255 | data/pathways/ergothioneine-biosynthesis-i.yaml | maintained | ergothioneine biosynthesis I (bacteria) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical successor input inspections | passed | True | MetaCyc:PWY-7255 | Initial successor inspect at 09:19:41Z preceded changed-byte assessment. Final expanded inspect captured the reread author dossiers, preserved initial pair, archive, acceptance audit and sealed final integration receipts. Target and scientific inputs remained unchanged. |
| Independent source and correction acceptance replay | passed | True | MetaCyc:PWY-7255 | Reviewer session 97964 exited 0. All 54 original bodies, 33 sides, seven balances and actual KGX 54 edges/100 evidence passed. The original 21 review inputs were verified against preserved bytes. Only edge 048 was removed, retained edge 042 gained exact construct scope, and every other node, reaction, edge and reference remained unchanged. |
| Final coordinated render | passed | True | MetaCyc:PWY-7255 | Actual final coordinated command exited 0; original log body and receipt digest independently inspected. |
| Final coordinated validate | passed | True | MetaCyc:PWY-7255 | Actual final coordinated command exited 0; original log body and receipt digest independently inspected. Native and closed schemas, identifiers, evidence, append-only history and current pages passed on the corrected corpus. |
| Final coordinated test | passed | True | MetaCyc:PWY-7255 | Actual final coordinated command exited 0; original log body and receipt digest independently inspected. =========== 1059 passed, 3 skipped, 3 warnings in 300.19s (0:05:00) ============ |
| Final coordinated lint | passed | True | MetaCyc:PWY-7255 | Actual final coordinated command exited 0; original log body and receipt digest independently inspected. This is the final post-correction lint run, separate from the preserved initial failed lint attempt. |
| Final coordinated identifiers | passed | True | MetaCyc:PWY-7255 | Actual final coordinated command exited 0; original log body and receipt digest independently inspected. |
| Final coordinated kgx | passed | True | MetaCyc:PWY-7255 | Actual final coordinated command exited 0; original log body and receipt digest independently inspected. |
| Final coordinated diff | passed | True | MetaCyc:PWY-7255 | Actual final coordinated command exited 0; original log body and receipt digest independently inspected. |
| Canonical pre-resolution review history check | passed | True | MetaCyc:PWY-7255 | Parent session 67056 exited 0; inspected log reports 62 valid review pairs. Complete selected predecessor YAML and Markdown were read, all 21 captured inputs were preserved and rehashed, and the exact issue key and occurrence are retained. |
| Exact species dataset applicability | not_applicable | True | MetaCyc:PWY-7255 | The inspected inventory covers 20 organisms and 28 datasets but not M. smegmatis. M. tuberculosis is a different species. This is not negative evidence for pathway presence or expression. |
| Preserved superseded initial lint failure | failed | False | MetaCyc:PWY-7255 | The original helper formatting error caused wrapper session 98675 to exit 1. Its just-test child exited 0 with 1059 passed, 3 skipped and 3 warnings; separate corrected lint exited 0. The initial review phrase session98675 terminal0 conflated wrapper and child; this successor corrects that wording without rewriting the immutable observation. |

## Scientific And Domain Assessments

### Complete bacterial native boundary

identity: supported. Targets: MetaCyc:PWY-7255.

Seven exact native members, no combined EgtE-net double counting and no substitution of a fungal route. Existing shared glutamate-cysteine chemistry is not whole-route duplication.

### Stoichiometry, charge and neutral terminal forms

grounding: supported. Targets: MetaCyc:PWY-7255.

All seven equations balance. Native CML and current ChEBI SMILES distinguish thiol and thione despite a shared standard InChI. AH2/A remains formal; no exact physiological reductant is asserted.

### Protein function, assembly and cofactors

evidence: supported. Targets: MetaCyc:PWY-7255.

Current annotation tiers and exact experimental organism limits are retained. EgtC tetramer/EgtE dimer, iron and PLP claims are supported without invented assembly IDs or isolated-monomer sufficiency.

### Selected strain and context

evidence: supported. Targets: MetaCyc:PWY-7255.

The mc2155 genetic phenotype supports pathway production; no Mtb expression transfer or intracellular inhibition claim is established.

### EgtD product-inhibition construct attribution

provenance: supported. Targets: MetaCyc:PWY-7255.

The preparation-specific inhibition observation is retained as context, while the exact mc2155 inhibitory relation is removed. Edge 042 accurately distinguishes the original and current sequences without transferring inhibition or claiming a functional consequence of their one-residue difference.

### Current inputs and generated graph

consistency: supported. Targets: MetaCyc:PWY-7255.

Final coordinated schema, identifier, test, lint, rendering and export checks pass for the corrected record; original reviews remain immutable.

## Findings

### f-egtd-inhibition-construct: EgtD inhibition preparation scope is preserved without exact-protein transfer

minor / resolved / confirmed; issue key: ergothioneine-egtd-product-inhibition-construct-scope.

The original edge 048 cited a 2018 purified preparation as inhibition of selected native mc2155 A0R5M8 without its linked DSM 43465/ATCC 607 construct limitation. The original observation remains experimentally supported. The corrected target removes that exact-protein relation, retains contextual inhibition and documents the construct distinction on the relevant activity evidence.

Disposition: Verified against corrected target SHA-256 238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527 and original primary/current sequence bodies. Only edge 048 was removed; retained edge 042 now states both sequence prefixes and preparation scope. No inhibition-only evidence was placed on an activity edge. All seven native reactions, 33 chemical sides and other mechanistic assertions remain intact, independent acceptance replay passed, and final required gates passed. This resolves the bounded provenance defect, not whether residue 2 changes function or whether native mc2155 EgtD is inhibited in vivo.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | MetaCyc:PWY-7255 and seven original reaction XML objects; reaction-list, reaction-layout, spontaneous, reaction-direction, exact sides | supports | Complete seven-member native route includes five enzymatic transformations plus neutral spontaneous reduction and reversible thiol/thione interconversion. |
| replay | research/pathway_additions/2026-10-11-next-203/ergothioneine-independent-review-audit.json; original_source_replay, construct_comparison, bounded_duplicate_searches | supports | Initial independent original-body replay verified all 33 sides, seven balances and full evidence export. Hidden- and ignored-inclusive searches in data, research and reviews found earlier leads and shared precursor chemistry rather than another complete maintained route. |
| protein | Five current UniProt original individual JSON entries; comments/reaction, cofactor, subunit, organism and sequence | supports | Current mc2155 assignments and exact pointers were verified. EgtA ECO:0000250 remains inferred; early B/C/D experimental annotations retain their preparation limitations. |
| seebeck | DOI:10.1021/ja101721e.s001; S2-S4 cloning and EgtD; S5-S9 EgtB chemistry; S7 Figure S6; S10 combined B/C activity | supports | Original DSM 43465 clone and heterologous host distinctions, three SAM methyl groups, sulfur coupling, iron depletion/rescue and combined synthesis support appropriately scoped claims; the metal figure was independently rendered. |
| egtc | PMID:26079795; Accepted manuscript p. 2, Overall structure; pp. 5-6, Protein production | supports | Exact mc2155 A0R5M9 clone, tetramer supported by PISA and analytical SEC, C2A substrate complex and cross-species substrate-generation limit inspected. |
| egte2015 | PMID:26149121; JATS section 1, paragraphs 1 and 3-9; Figures 4-6 | supports | Purified PLP enzyme, sulfenic trapping, DTT dependence, pyruvate/ammonia and unspecified physiological reductant verified. Coupled NADH consumption is not the pathway donor. |
| egte2023 | PMID:38072054; Sections 3.2 paragraph 1, 1.1 paragraph 2 and 1.2 paragraph 1 | supports | Exact A0R5M7 mc2155 clone; solution-supported homodimer and neighboring-chain pocket. Pyruvate crystal tetramer is not generalized to solution. |
| inhibition | DOI:10.1021/acschembio.8b00127.s001; SI p. 3, Figure S2; p. 1, assay conditions; p. 11, Protein Production; reference 3 on p. 25 | supports | Product inhibition is supported for the purified preparation. The production cross-reference identifies the 2014 construct. The corrected record retains this observation as preparation-specific context and makes no exact mc2155 inhibition edge. |
| construct | PMID:24817736 / PMC4014345 and UniProtKB:A0R5M8; Original HTML section 2.1 paragraph 1, full construct; current UniProt /sequence/value | supports | The 2014 source identifies DSM 43465/ATCC 607. After tags are excluded, the 321-residue construct differs from the selected mc2155 sequence only at position 2 (A versus T). This does not establish a functional effect or refute product inhibition. |
| physiology | PMID:23629716; Original HTML section 5 paragraph 1; section 12 paragraph 1 and Table 3 | supports | Exact mc2155 egtD deletion loses detectable ergothioneine and complementation restores it; this supports pathway physiology without validating every formal intermediate. |
| context | research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json; candidate_dispositions entry for MetaCyc:PWY-7255 | supports | No dataset covers the selected species; unrelated M. tuberculosis context is not transferred. |
| fix-acceptance | research/pathway_additions/2026-10-11-next-203/ergothioneine-successor-review-audit.json; changed_inputs; source_and_graph_acceptance; independent_replay; source_assessment | supports | Independent original-source replay and parsed comparison verify the conservative correction. Edge 048 is absent; edge 042 cites the exact current and historical sequence prefixes; no inhibition-only evidence was moved onto catalytic evidence. The entire seven-reaction boundary and all 33 chemical sides remain unchanged. |
| prior-review | reviews/structured/20261011T091416Z-ergothioneine-initial-independent-review/review.yaml; finding f-egtd-inhibition-construct and all original source inputs | supports | The complete initial authoritative YAML and paired Markdown were read. Issue 371 is the only confirmed predecessor finding in this target scope. The successor preserves its stable key, target and exact occurrence. |
| input-archive | research/pathway_additions/2026-10-11-next-203/initial-review-inputs/20261011T091416Z-ergothioneine-initial-independent-review/manifest.json; All 21 original input entries | supports | All archived body hashes were independently checked against the initial review; original observations and source bytes remain recoverable. |
| gates | research/pathway_additions/2026-10-11-next-203/integration-receipt.json; Final coordinated gate receipts, log hashes and correction scope | supports | Final required checks and original terminal logs were inspected after the corrected target and author dossiers froze. The preserved initial lint failure and wrapper/child distinction remain explicit. |
| graph | research/pathway_additions/2026-10-11-next-203/generated-graph-kgx-audit.json; Ergothioneine record-local SVG, page and KGX comparison | supports | Final generated-artifact audit confirms the corrected graph and evidence export. Structural rendering and export checks do not replace the independently inspected scientific sources. |

## Limits And Additional Notes

- EgtA activity is similarity-based. Early B/C/D studies use DSM 43465 preparations; later EgtC/EgtE experiments and genetic physiology ground the selected mc2155 context.
- The physiological reductant for terminal reduction is unidentified. DTT is an experimental reagent, not an assigned physiological donor.
- The current terminal Rhea cationic equation differs from the explicitly selected, balanced native neutral forms. The record does not invent an acid-base or physiological donor assignment.
- The sequence difference does not establish altered EgtD function. Preparation-specific inhibition is retained without asserting its exact-strain transfer or intracellular effect.
- Primary PDF figures were rendered and inspected locally. Generated pages and graphs received structural checks; browser visual QA is not claimed.
- This review covers one maintained pathway. It does not certify all corpus science or convert computational expression context into experimental mechanism evidence.
- Applied the resolve-reviews workflow while preserving the full review-yaml-record scientific rubric. Initial and successor target inspections preceded their respective assessments; changed author inputs were explicitly reread and rechecked.
- The complete initial YAML and Markdown pair remains immutable. All 21 original input hashes match the archived bytes; the successor retains the exact predecessor finding identity and issue key.
- Execution clarification: initial wrapper session 98675 exited 1 because its lint child failed. The just-test child exited 0 with 1059 passed and 3 skipped; corrected lint separately exited 0. The initial report phrase session98675 terminal0 was imprecise about the wrapper, although its just-test command and exit_code 0 were correct. Final post-correction checks are recorded separately here.
- The reviewer authored the separate methylthiopropanoate record and did not author or edit this target or its correction. Source replay is one technical check within an independent source-by-source scientific assessment.
- The earlier acceptance audit records that global gates were pending at its own timestamp. This later immutable successor uses their actual completed terminal results and sealed integration receipts.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T092631Z-ergothioneine-resolved-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: 'Independent ergothioneine successor review: verified EgtD scope correction'
started_at: '2026-10-11T09:19:41Z'
finished_at: '2026-10-11T09:26:31Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_authority_cache)
  kind: agent
  independence: independent
  independence_basis: Authored the separate methylthiopropanoate record, not this
    target or its author dossiers. Independently read the full target, original sources,
    selected primary PDFs and current protein/Rhea/chemical authorities.
skill: pathwaymech-resolve-reviews
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete seven-step bacterial pathway is supported with explicit strain,
  evidence-tier and donor limitations. Issue 371 is resolved by removing the exact-protein
  inhibition edge while retaining the measured preparation as context. Independent
  replay verified 54 original source bodies, 33 chemical sides, seven balances and
  all 54 edges with 100 evidence blocks. Final coordinated checks passed. There are
  no unresolved findings in this one-record scope.
source:
  git_revision: 7c555ecacc2b2708b246a68dcc9b64444791f526
  state: working_tree
  inputs:
  - path: .claude/skills/pathwaymech-resolve-reviews/SKILL.md
    sha256: 3d3b9d3b9e56cc782cf4ff63d491c5b589e9bdcde71438a695384b228edc4aea
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 6aa3c04fbb8dfebfba2a774e432764ee578f8951a140298a98c706396a2f690f
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 8185c5ca95a6c8eadc2e71c072916a85bfdb21d814e253ba65cec5c203f7e764
    role: context
  - path: data/pathways/ergothioneine-biosynthesis-i.yaml
    sha256: 238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527
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
  - path: docs/record-review-profile.md
    sha256: a3d4b48de5f227515f9b5de12dd172cd1eb626068235b2b2e58bc4f6a5ee567d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/baseline-preservation.json
    sha256: c0efe8e3da64ddc951dfad096d68349a6bc897dfdc5a00d1d7cb5587efcc0fc8
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-authority-delta.json
    sha256: e0d0871b9c9ae94476164a154e71d0fffff1aa6105be9cbb68ed3b6fe9fbd900
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-curation.md
    sha256: 49d6191a53f545b896ddad7dbffd97a9063b4c48b8ce72826c8ae4cd2905a3d2
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-dedup.json
    sha256: 5287a062cb850cc374fafe112aae7b83db7af69597eb8dafb81fc55d1ecea9fe
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-identifiers.json
    sha256: 1ed2ba5e297154f399ca2aaad408465ead9824714fcbbf17663b4cdc021e90a2
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-independent-review-audit.json
    sha256: 194ae0ac4081dab0c917243dd3dce00b9dd83aec7e45eb81cb6da3da4db3fb63
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-independent-review-findings.md
    sha256: dcef74aaf09b6ddff2f49b0aea9956d4b29cd8fce349eefe88ef6100739d1426
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-protein-projection.json
    sha256: ac65648cc48544125c323c07f459d957eae27b67722e0a03c96aaa9120bc6602
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-provenance-fix.json
    sha256: a4852bc784a212b99d4ec550657536fcae00411b65aec28a9237dac988e6a134
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-replay.py
    sha256: 0ad1c33e4f8f62de8855956eabeb1ce3a8aef150e2298a22ff6d6abed780b83c
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-source-manifest.json
    sha256: 0b3f17217d6e6124ed13f4961b6fb8a83f958aa094639b8c0e6fc7f88b5a36f9
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-source-projection.json
    sha256: 8a58bc7faca06707e8977b9577b2700688ae4016b8c9284dd33087774e1438ef
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-successor-review-audit.json
    sha256: 282f58c1ab2af3d6465369d4a410459ad1716972d81b8e8576059dc2fa7b27fb
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-validation.json
    sha256: dcdd57db84574e25f37e515825e543e0f30980c5dccb4b2af4ac3abfd288df5f
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/generated-graph-kgx-audit.json
    sha256: 4b51696f051b4f71fdfc0b7e505ff36401d283e7716a96b1f93d7bf7900f9efb
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json
    sha256: 57da9dbc37e8048aaf2a226985b1334a92ec6096cdaf8a81333069e3a93fb49f
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/initial-review-inputs/20261011T091416Z-ergothioneine-initial-independent-review/manifest.json
    sha256: 8d6e8ca35c597ce2e34d5f33e2ceb50bb1013b97b077049c9a67d17480e2a3e2
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/integration-receipt.json
    sha256: c2579bfcfed0e37e7c8d3e5ab6a952cbc15b0fae0463c4ae8c16da28994fa8a5
    role: context
  - path: reviews/structured/20261011T091416Z-ergothioneine-initial-independent-review/review.md
    sha256: f2f4f9aa388bad6c28574bd1fdb216733bc6c36bf50d072b9164fa365a2bb34e
    role: context
  - path: reviews/structured/20261011T091416Z-ergothioneine-initial-independent-review/review.yaml
    sha256: 778a5b38da3e65f87821f460174ca486a2ee0aa73e0eeddef332fde17b87182c
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: ffa1107da83c8ff173833662e78ba73c779bbab9f2da33cea993b614e99d6345
    role: context
targets:
- target_id: MetaCyc:PWY-7255
  path: data/pathways/ergothioneine-biosynthesis-i.yaml
  label: ergothioneine biosynthesis I (bacteria)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained_record
scope:
  description: Full independent scientific assessment of the corrected target, including
    explicit reassessment of all changed input bytes, the initial finding and its
    original sources. Final coordinated gate and generated-artifact receipts were
    inspected.
  selection: Corrected target SHA-256 238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527;
    one exact predecessor finding.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-7255
  exclusions:
  - target: Other cohort targets and corpus-wide scientific quality
    reason: Outside this individual independent review.
checks:
- check_id: inspect
  name: Canonical successor input inspections
  command: PYTHONPATH=src .venv/bin/python scripts/record_review.py inspect --targets
    /private/tmp/pathwaymech-next-203-ergothioneine-review/targets-successor.yaml
    --input data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input docs/CAUSAL_GRAPHS.md --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/record-review-profile.md --input research/pathway_additions/2026-10-11-next-203/ergothioneine-authority-delta.json
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-curation.md
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-dedup.json
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-identifiers.json
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-independent-review-findings.md
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-protein-projection.json
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-replay.py
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-source-projection.json
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-validation.json
    --input research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-successor-review-audit.json
    --input research/pathway_additions/2026-10-11-next-203/ergothioneine-provenance-fix.json
    --input research/pathway_additions/2026-10-11-next-203/integration-receipt.json
    --input research/pathway_additions/2026-10-11-next-203/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-11-next-203/baseline-preservation.json
    --input reviews/structured/20261011T091416Z-ergothioneine-initial-independent-review/review.yaml
    --input reviews/structured/20261011T091416Z-ergothioneine-initial-independent-review/review.md
    --input research/pathway_additions/2026-10-11-next-203/initial-review-inputs/20261011T091416Z-ergothioneine-initial-independent-review/manifest.json
    --input .claude/skills/pathwaymech-resolve-reviews/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input docs/record-reviews.md --input conf/record_review.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Initial successor inspect at 09:19:41Z preceded changed-byte assessment.
    Final expanded inspect captured the reread author dossiers, preserved initial
    pair, archive, acceptance audit and sealed final integration receipts. Target
    and scientific inputs remained unchanged.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: independent-replay
  name: Independent source and correction acceptance replay
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python /private/tmp/pathwaymech-next-203-ergothioneine-review/independent-successor-replay.py
  status: passed
  required: true
  exit_code: 0
  summary: Reviewer session 97964 exited 0. All 54 original bodies, 33 sides, seven
    balances and actual KGX 54 edges/100 evidence passed. The original 21 review inputs
    were verified against preserved bytes. Only edge 048 was removed, retained edge
    042 gained exact construct scope, and every other node, reaction, edge and reference
    remained unchanged.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: final-render
  name: Final coordinated render
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just render-pages
  status: passed
  required: true
  exit_code: 0
  summary: Actual final coordinated command exited 0; original log body and receipt
    digest independently inspected.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: final-validate
  name: Final coordinated validate
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just validate
  status: passed
  required: true
  exit_code: 0
  summary: Actual final coordinated command exited 0; original log body and receipt
    digest independently inspected. Native and closed schemas, identifiers, evidence,
    append-only history and current pages passed on the corrected corpus.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: final-test
  name: Final coordinated test
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just test
  status: passed
  required: true
  exit_code: 0
  summary: Actual final coordinated command exited 0; original log body and receipt
    digest independently inspected. =========== 1059 passed, 3 skipped, 3 warnings
    in 300.19s (0:05:00) ============
  target_ids:
  - MetaCyc:PWY-7255
- check_id: final-lint
  name: Final coordinated lint
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just lint
  status: passed
  required: true
  exit_code: 0
  summary: Actual final coordinated command exited 0; original log body and receipt
    digest independently inspected. This is the final post-correction lint run, separate
    from the preserved initial failed lint attempt.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: final-identifiers
  name: Final coordinated identifiers
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just check-identifiers
  status: passed
  required: true
  exit_code: 0
  summary: Actual final coordinated command exited 0; original log body and receipt
    digest independently inspected.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: final-kgx
  name: Final coordinated kgx
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just kgx-export --output-dir
    /private/tmp/pathwaymech-next-203-kgx
  status: passed
  required: true
  exit_code: 0
  summary: Actual final coordinated command exited 0; original log body and receipt
    digest independently inspected.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: final-diff
  name: Final coordinated diff
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache git diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Actual final coordinated command exited 0; original log body and receipt
    digest independently inspected.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: initial-lineage
  name: Canonical pre-resolution review history check
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just review-check --base 7c555ecacc2b2708b246a68dcc9b64444791f526 --require-reviews
  status: passed
  required: true
  exit_code: 0
  summary: Parent session 67056 exited 0; inspected log reports 62 valid review pairs.
    Complete selected predecessor YAML and Markdown were read, all 21 captured inputs
    were preserved and rehashed, and the exact issue key and occurrence are retained.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: imodulondb
  name: Exact species dataset applicability
  command: Read the retained canonical-client dataset inventory and imodulondb-applicability.json
  status: not_applicable
  required: true
  summary: The inspected inventory covers 20 organisms and 28 datasets but not M.
    smegmatis. M. tuberculosis is a different species. This is not negative evidence
    for pathway presence or expression.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: initial-lint
  name: Preserved superseded initial lint failure
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just lint
  status: failed
  required: false
  exit_code: 1
  summary: The original helper formatting error caused wrapper session 98675 to exit
    1. Its just-test child exited 0 with 1059 passed, 3 skipped and 3 warnings; separate
    corrected lint exited 0. The initial review phrase session98675 terminal0 conflated
    wrapper and child; this successor corrects that wording without rewriting the
    immutable observation.
  target_ids:
  - MetaCyc:PWY-7255
evidence:
- evidence_id: native
  kind: database
  reference: MetaCyc:PWY-7255 and seven original reaction XML objects
  locator: reaction-list, reaction-layout, spontaneous, reaction-direction, exact
    sides
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Complete seven-member native route includes five enzymatic transformations
    plus neutral spontaneous reduction and reversible thiol/thione interconversion.
  snapshot_sha256: 28518a958f37dfa2424c77b5c08db6eb9057e7a26cb61448f4dcbb513ddaf617
- evidence_id: replay
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/ergothioneine-independent-review-audit.json
  locator: original_source_replay, construct_comparison, bounded_duplicate_searches
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Initial independent original-body replay verified all 33 sides, seven balances
    and full evidence export. Hidden- and ignored-inclusive searches in data, research
    and reviews found earlier leads and shared precursor chemistry rather than another
    complete maintained route.
  snapshot_sha256: 194ae0ac4081dab0c917243dd3dce00b9dd83aec7e45eb81cb6da3da4db3fb63
- evidence_id: protein
  kind: database
  reference: Five current UniProt original individual JSON entries
  locator: comments/reaction, cofactor, subunit, organism and sequence
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Current mc2155 assignments and exact pointers were verified. EgtA ECO:0000250
    remains inferred; early B/C/D experimental annotations retain their preparation
    limitations.
- evidence_id: seebeck
  kind: primary_source
  reference: DOI:10.1021/ja101721e.s001
  locator: S2-S4 cloning and EgtD; S5-S9 EgtB chemistry; S7 Figure S6; S10 combined
    B/C activity
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Original DSM 43465 clone and heterologous host distinctions, three SAM
    methyl groups, sulfur coupling, iron depletion/rescue and combined synthesis support
    appropriately scoped claims; the metal figure was independently rendered.
  snapshot_sha256: 8865d33ccc48125663acdcf27c5af5e10f1eead72258d95b5270c5e08ad18847
- evidence_id: egtc
  kind: primary_source
  reference: PMID:26079795
  locator: Accepted manuscript p. 2, Overall structure; pp. 5-6, Protein production
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Exact mc2155 A0R5M9 clone, tetramer supported by PISA and analytical SEC,
    C2A substrate complex and cross-species substrate-generation limit inspected.
  snapshot_sha256: 6e7a43aa9e761c39b86386355b6ca1e2b2005ba9674ad41b280265fe1aea344e
- evidence_id: egte2015
  kind: primary_source
  reference: PMID:26149121
  locator: JATS section 1, paragraphs 1 and 3-9; Figures 4-6
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Purified PLP enzyme, sulfenic trapping, DTT dependence, pyruvate/ammonia
    and unspecified physiological reductant verified. Coupled NADH consumption is
    not the pathway donor.
  snapshot_sha256: 5567e312f5e3fef6298af1b64dfc37ae9675ac8a9f003dcfd898f096d616b125
- evidence_id: egte2023
  kind: primary_source
  reference: PMID:38072054
  locator: Sections 3.2 paragraph 1, 1.1 paragraph 2 and 1.2 paragraph 1
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Exact A0R5M7 mc2155 clone; solution-supported homodimer and neighboring-chain
    pocket. Pyruvate crystal tetramer is not generalized to solution.
  snapshot_sha256: d9c105c4d6b82abfba24f236558d6cd1719ae8cb1b5e7657acc2cf88864583ad
- evidence_id: inhibition
  kind: primary_source
  reference: DOI:10.1021/acschembio.8b00127.s001
  locator: SI p. 3, Figure S2; p. 1, assay conditions; p. 11, Protein Production;
    reference 3 on p. 25
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Product inhibition is supported for the purified preparation. The production
    cross-reference identifies the 2014 construct. The corrected record retains this
    observation as preparation-specific context and makes no exact mc2155 inhibition
    edge.
  snapshot_sha256: 20e0596c264994c847c2e19c11896a0d014081454b55cd555d5c58eb24060b64
- evidence_id: construct
  kind: primary_source
  reference: PMID:24817736 / PMC4014345 and UniProtKB:A0R5M8
  locator: Original HTML section 2.1 paragraph 1, full construct; current UniProt
    /sequence/value
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: The 2014 source identifies DSM 43465/ATCC 607. After tags are excluded,
    the 321-residue construct differs from the selected mc2155 sequence only at position
    2 (A versus T). This does not establish a functional effect or refute product
    inhibition.
  snapshot_sha256: 89ced1b7b2b1aad3ace06e7d0656d79285140ac46293e03f78f19a2a5f4701dd
- evidence_id: physiology
  kind: primary_source
  reference: PMID:23629716
  locator: Original HTML section 5 paragraph 1; section 12 paragraph 1 and Table 3
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Exact mc2155 egtD deletion loses detectable ergothioneine and complementation
    restores it; this supports pathway physiology without validating every formal
    intermediate.
  snapshot_sha256: 6551e9000cd0f815c48f5d55f827aae32a05094f92c2ebdaecbee94f59c12e61
- evidence_id: context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json
  locator: candidate_dispositions entry for MetaCyc:PWY-7255
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: No dataset covers the selected species; unrelated M. tuberculosis context
    is not transferred.
  snapshot_sha256: 57da9dbc37e8048aaf2a226985b1334a92ec6096cdaf8a81333069e3a93fb49f
- evidence_id: fix-acceptance
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/ergothioneine-successor-review-audit.json
  locator: changed_inputs; source_and_graph_acceptance; independent_replay; source_assessment
  accessed_at: '2026-10-11T09:26:31Z'
  support: supports
  summary: Independent original-source replay and parsed comparison verify the conservative
    correction. Edge 048 is absent; edge 042 cites the exact current and historical
    sequence prefixes; no inhibition-only evidence was moved onto catalytic evidence.
    The entire seven-reaction boundary and all 33 chemical sides remain unchanged.
  snapshot_sha256: 282f58c1ab2af3d6465369d4a410459ad1716972d81b8e8576059dc2fa7b27fb
- evidence_id: prior-review
  kind: prior_review
  reference: reviews/structured/20261011T091416Z-ergothioneine-initial-independent-review/review.yaml
  locator: finding f-egtd-inhibition-construct and all original source inputs
  accessed_at: '2026-10-11T09:26:31Z'
  support: supports
  summary: The complete initial authoritative YAML and paired Markdown were read.
    Issue 371 is the only confirmed predecessor finding in this target scope. The
    successor preserves its stable key, target and exact occurrence.
  snapshot_sha256: 778a5b38da3e65f87821f460174ca486a2ee0aa73e0eeddef332fde17b87182c
- evidence_id: input-archive
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/initial-review-inputs/20261011T091416Z-ergothioneine-initial-independent-review/manifest.json
  locator: All 21 original input entries
  accessed_at: '2026-10-11T09:26:31Z'
  support: supports
  summary: All archived body hashes were independently checked against the initial
    review; original observations and source bytes remain recoverable.
  snapshot_sha256: 8d6e8ca35c597ce2e34d5f33e2ceb50bb1013b97b077049c9a67d17480e2a3e2
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/integration-receipt.json
  locator: Final coordinated gate receipts, log hashes and correction scope
  accessed_at: '2026-10-11T09:26:31Z'
  support: supports
  summary: Final required checks and original terminal logs were inspected after the
    corrected target and author dossiers froze. The preserved initial lint failure
    and wrapper/child distinction remain explicit.
  snapshot_sha256: c2579bfcfed0e37e7c8d3e5ab6a952cbc15b0fae0463c4ae8c16da28994fa8a5
- evidence_id: graph
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/generated-graph-kgx-audit.json
  locator: Ergothioneine record-local SVG, page and KGX comparison
  accessed_at: '2026-10-11T09:26:31Z'
  support: supports
  summary: Final generated-artifact audit confirms the corrected graph and evidence
    export. Structural rendering and export checks do not replace the independently
    inspected scientific sources.
  snapshot_sha256: 4b51696f051b4f71fdfc0b7e505ff36401d283e7716a96b1f93d7bf7900f9efb
assessments:
- assessment_id: identity
  area: identity
  topic: Complete bacterial native boundary
  outcome: supported
  summary: Seven exact native members, no combined EgtE-net double counting and no
    substitution of a fungal route. Existing shared glutamate-cysteine chemistry is
    not whole-route duplication.
  target_ids:
  - MetaCyc:PWY-7255
  evidence_ids:
  - native
  - replay
  - fix-acceptance
- assessment_id: chemistry
  area: grounding
  topic: Stoichiometry, charge and neutral terminal forms
  outcome: supported
  summary: All seven equations balance. Native CML and current ChEBI SMILES distinguish
    thiol and thione despite a shared standard InChI. AH2/A remains formal; no exact
    physiological reductant is asserted.
  target_ids:
  - MetaCyc:PWY-7255
  evidence_ids:
  - native
  - replay
  - egte2015
  - fix-acceptance
- assessment_id: enzymes
  area: evidence
  topic: Protein function, assembly and cofactors
  outcome: supported
  summary: Current annotation tiers and exact experimental organism limits are retained.
    EgtC tetramer/EgtE dimer, iron and PLP claims are supported without invented assembly
    IDs or isolated-monomer sufficiency.
  target_ids:
  - MetaCyc:PWY-7255
  evidence_ids:
  - protein
  - seebeck
  - egtc
  - egte2015
  - egte2023
- assessment_id: physiology
  area: evidence
  topic: Selected strain and context
  outcome: supported
  summary: The mc2155 genetic phenotype supports pathway production; no Mtb expression
    transfer or intracellular inhibition claim is established.
  target_ids:
  - MetaCyc:PWY-7255
  evidence_ids:
  - physiology
  - context
- assessment_id: regulation
  area: provenance
  topic: EgtD product-inhibition construct attribution
  outcome: supported
  summary: The preparation-specific inhibition observation is retained as context,
    while the exact mc2155 inhibitory relation is removed. Edge 042 accurately distinguishes
    the original and current sequences without transferring inhibition or claiming
    a functional consequence of their one-residue difference.
  target_ids:
  - MetaCyc:PWY-7255
  evidence_ids:
  - inhibition
  - construct
  - fix-acceptance
  - prior-review
- assessment_id: publication
  area: consistency
  topic: Current inputs and generated graph
  outcome: supported
  summary: Final coordinated schema, identifier, test, lint, rendering and export
    checks pass for the corrected record; original reviews remain immutable.
  target_ids:
  - MetaCyc:PWY-7255
  evidence_ids:
  - gates
  - graph
  - input-archive
findings:
- finding_id: f-egtd-inhibition-construct
  issue_key: ergothioneine-egtd-product-inhibition-construct-scope
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: EgtD inhibition preparation scope is preserved without exact-protein transfer
  description: The original edge 048 cited a 2018 purified preparation as inhibition
    of selected native mc2155 A0R5M8 without its linked DSM 43465/ATCC 607 construct
    limitation. The original observation remains experimentally supported. The corrected
    target removes that exact-protein relation, retains contextual inhibition and
    documents the construct distinction on the relevant activity evidence.
  target_ids:
  - MetaCyc:PWY-7255
  field_paths:
  - mechanistic_edges[id=ergothioneine-edge-048]
  evidence_ids:
  - inhibition
  - construct
  - fix-acceptance
  - prior-review
  - input-archive
  - gates
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained_record
  rule_id: review-yaml-record strain, construct and evidence scope
  native_severity: minor
  normalization_reason: Bounded attribution/qualification problem; the observed product
    inhibition is supported, sequence similarity is high and complete pathway chemistry
    remains intact.
  disposition_reason: Verified against corrected target SHA-256 238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527
    and original primary/current sequence bodies. Only edge 048 was removed; retained
    edge 042 now states both sequence prefixes and preparation scope. No inhibition-only
    evidence was placed on an activity edge. All seven native reactions, 33 chemical
    sides and other mechanistic assertions remain intact, independent acceptance replay
    passed, and final required gates passed. This resolves the bounded provenance
    defect, not whether residue 2 changes function or whether native mc2155 EgtD is
    inhibited in vivo.
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T091416Z-ergothioneine-initial-independent-review
    finding_id: f-egtd-inhibition-construct
actions: []
limitations:
- EgtA activity is similarity-based. Early B/C/D studies use DSM 43465 preparations;
  later EgtC/EgtE experiments and genetic physiology ground the selected mc2155 context.
- The physiological reductant for terminal reduction is unidentified. DTT is an experimental
  reagent, not an assigned physiological donor.
- The current terminal Rhea cationic equation differs from the explicitly selected,
  balanced native neutral forms. The record does not invent an acid-base or physiological
  donor assignment.
- The sequence difference does not establish altered EgtD function. Preparation-specific
  inhibition is retained without asserting its exact-strain transfer or intracellular
  effect.
- Primary PDF figures were rendered and inspected locally. Generated pages and graphs
  received structural checks; browser visual QA is not claimed.
- This review covers one maintained pathway. It does not certify all corpus science
  or convert computational expression context into experimental mechanism evidence.
notes:
- Applied the resolve-reviews workflow while preserving the full review-yaml-record
  scientific rubric. Initial and successor target inspections preceded their respective
  assessments; changed author inputs were explicitly reread and rechecked.
- The complete initial YAML and Markdown pair remains immutable. All 21 original input
  hashes match the archived bytes; the successor retains the exact predecessor finding
  identity and issue key.
- 'Execution clarification: initial wrapper session 98675 exited 1 because its lint
  child failed. The just-test child exited 0 with 1059 passed and 3 skipped; corrected
  lint separately exited 0. The initial report phrase session98675 terminal0 was imprecise
  about the wrapper, although its just-test command and exit_code 0 were correct.
  Final post-correction checks are recorded separately here.'
- The reviewer authored the separate methylthiopropanoate record and did not author
  or edit this target or its correction. Source replay is one technical check within
  an independent source-by-source scientific assessment.
- The earlier acceptance audit records that global gates were pending at its own timestamp.
  This later immutable successor uses their actual completed terminal results and
  sealed integration receipts.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/371
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4014345/
- https://doi.org/10.1021/acschembio.8b00127
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261011T091416Z-ergothioneine-initial-independent-review
  relationship: Resolves the sole minor finding after independent source reassessment;
    preserves the original complete review and input archive.
```
