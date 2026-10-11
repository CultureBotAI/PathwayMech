# Independent initial ergothioneine pathway review: EgtD preparation scope

- Review: 20261011T091416Z-ergothioneine-initial-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T09:04:27Z
- Finished UTC: 2026-10-11T09:14:16Z
- Reviewer: Codex independent reviewer (/root/pathway_authority_cache) (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The complete seven-step native pathway and 33 chemical sides are supported with stated EgtA, strain, donor and assembly limitations. One minor EgtD product-inhibition attribution finding requires the experimental construct scope to be preserved. Coordinated tests passed; a source-corrected successor is still required.

## Scope And Provenance

Full independent scientific assessment of one author-frozen target, with original-source replay and inspected coordinated terminal gate receipts.

Selection: Exact author-frozen a0a26b897757e072ec5640805db8ab9ed0961b6499e1c576d0751996a0f97b37.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c555ecacc2b2708b246a68dcc9b64444791f526.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-7255 | data/pathways/ergothioneine-biosynthesis-i.yaml | maintained | ergothioneine biosynthesis I (bacteria) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical initial and expanded input inspection | passed | True | MetaCyc:PWY-7255 | Initial inspect preceded scientific assessment at 09:04:27Z. Expanded capture rechecked unchanged target and the final authored dossiers. A first expanded attempt used an incorrect schema path; the actual source schema path was then inspected successfully. |
| Independent original-source and KGX replay | passed | True | MetaCyc:PWY-7255 | Actual reviewer session30119 exit0:54 original bodies,33 chemical sides,7 atom/charge balances,exact native boundary and protein pointers,55 edges/101 evidence in actual KGX. Initial helper-only attempt assumed a nonexistent RDF direction property; corrected to exact native side and master predicates. |
| Coordinated validate | passed | True | MetaCyc:PWY-7255 | Parent reported actual terminal0 and reviewer inspected preserved 206-record native/closed/identifier/evidence/history/page QC log. |
| Coordinated lint | passed | True | MetaCyc:PWY-7255 | Parent reported actual terminal0 and reviewer inspected preserved corrected lint log: All checks passed. Earlier helper formatting failure was superseded. |
| Coordinated full test suite | passed | True | MetaCyc:PWY-7255 | Actual session98675 terminal0 and preserved log inspected: 1059 passed, 3 skipped, 3 upstream warnings in 498.43 seconds. Finished 09:13:36Z. This is the original pre-correction test result, not an attestation to future edits. |
| Whitespace check | passed | True | MetaCyc:PWY-7255 | Reviewer actually executed exit0. Untracked additions require parent staging/final checks. |
| Exact taxon dataset applicability | not_applicable | True | MetaCyc:PWY-7255 | Inspected20-organism/28-dataset inventory does not cover M. smegmatis; M. tuberculosis is a different species. No negative pathway or expression inference. |
| Superseded original lint attempt | failed | False | MetaCyc:PWY-7255 | Original gate receipt retains author/helper formatting failure; parent corrected formatting and reran lint terminal0, whose actual All checks passed log was inspected. |

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

provenance: concern. Targets: MetaCyc:PWY-7255.

Edge048 names native A0R5M8 but its source describes a linked DSM43465-derived engineered preparation. A source-specific construct/transfer qualification or contextual-only representation is required.

## Findings

### f-egtd-inhibition-construct: EgtD inhibition evidence needs exact experimental preparation scope

minor / open / confirmed; issue key: ergothioneine-egtd-product-inhibition-construct-scope.

Edge048 links hercynine inhibition to current mc2155 A0R5M8 while citing the 2018 purified preparation without its linked DSM43465/ATCC607 construct limitation. The 2014 complete sequence differs at position 2 after tags are excluded. The experiment supports product inhibition; it does not independently establish unqualified inhibition of the exact native mc2155 form. Preserve measured preparation context and explicitly grade transfer, or keep the observation contextual without that specific regulatory edge.

## Recommended Actions And Acceptance Checks

### scope-inhibition

Archive initial inputs, correct the exact-protein inhibition representation while retaining the experimental observation and complete seven-step pathway.

- Preserve original review and exact inspected input bytes before mutation.
- Explicitly document DSM43465/ATCC607 construct source and distinguish direct observation from mc2155 transfer, or move the observation to contextual EgtD evidence.
- Recheck all changed source assertions and run applicable source/schema/KGX and coordinated gates.
- Save an immutable successor retaining the exact issue key and previous occurrence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | MetaCyc:PWY-7255 and seven original reaction XML objects; reaction-list, reaction-layout, spontaneous, reaction-direction, exact sides | supports | Complete seven-member native route includes five enzymatic transformations plus neutral spontaneous reduction and reversible thiol/thione interconversion. |
| replay | research/pathway_additions/2026-10-11-next-203/ergothioneine-independent-review-audit.json; original_source_replay, construct_comparison, bounded_duplicate_searches | supports | Independent original-body replay validates33 sides/seven balances and full evidence export; hidden/ignored-inclusive searches of data, research and reviews find prior leads/shared precursor chemistry, not another complete maintained route. |
| protein | Five current UniProt original individual JSON entries; comments/reaction, cofactor, subunit, organism and sequence | supports | Current mc2155 assignments and exact pointers verified. EgtA ECO0000250 remains inferred; B/C/D experimental annotations are not promoted beyond the source preparation limitations. |
| seebeck | DOI:10.1021/ja101721e.s001; S2-S4 cloning and EgtD; S5-S9 EgtB chemistry; S7 FigureS6; S10 combined B/C activity | supports | Original DSM43465 clone/host distinctions, three SAM methyl groups, sulfur coupling, iron depletion/rescue and combined synthesis support source-scoped claims; metal figure independently rendered. |
| egtc | PMID:26079795; Accepted manuscript p2 Overall structure; pp5-6 Protein production | supports | Exact mc2155 A0R5M9 clone, tetramer supported by PISA and analytical SEC, C2A substrate complex and cross-species substrate-generation limit inspected. |
| egte2015 | PMID:26149121; JATS sec1 paragraphs1,3-9, Figures4-6 | supports | Purified PLP enzyme, sulfenic trapping, DTT dependence, pyruvate/ammonia and unspecified physiological reductant verified. Coupled NADH consumption is not the pathway donor. |
| egte2023 | PMID:38072054; sec3.2/p1, sec1.1/p2, sec1.2/p1 | supports | Exact A0R5M7 mc2155 clone; solution-supported homodimer and neighboring-chain pocket. Pyruvate crystal tetramer is not generalized to solution. |
| inhibition | DOI:10.1021/acschembio.8b00127.s001; p3 FigureS2; p1 assay conditions; p11 Protein Production; reference3 p25 | supports | Product inhibition is real in the purified preparation. Production cross-reference identifies the 2014 construct; current edge omits the relevant construct and strain-transfer limitation. |
| construct | PMID:24817736 / PMC4014345 and UniProtKB:A0R5M8; Original HTML sec2.1 paragraph1 full construct; current sequence.value | supports | 2014 source names DSM43465/ATCC607. After tags are excluded,321 residues compare with only position2 A in the construct versus T in current mc2155. This difference does not prove a functional effect or refute inhibition. |
| physiology | PMID:23629716; HTML sec5/p1; sec12/p1 and Table3 | supports | Exact mc2155 egtD deletion loses detectable ergothioneine and complementation restores it; this supports pathway physiology without validating every formal intermediate. |
| context | research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json; candidate_dispositions PWY7255 | supports | No covered selected species dataset; unrelated Mtb context not transferred. |
| gates | /private/tmp/pathwaymech-next-203-final-gate-receipts.json; All seven original per-command receipts; corrected lint log separately | supports | Actual original full test1059 passed/3 skipped;206-record validate, render, identifiers, KGX and diff exit0. Initial lint1 followed by corrected lint0. Root reported terminal results and reviewer inspected logs. |

## Limits And Additional Notes

- EgtA activity is similarity-based; early B/C/D studies use DSM43465, while later EgtC/EgtE and genetic physiology ground mc2155.
- A physiological reductant is not identified; DTT is an experimental reductant, not a physiological assignment.
- Current terminal Rhea cationic equation differs from the explicitly selected balanced native neutral forms.
- PDF figures were rendered and inspected locally; no browser page visual QA is claimed.
- The current observation precedes the scoped issue371 correction and regenerated final publication artifacts; the successor must inspect those changed bytes and applicable checks.
- Initial canonical inspect preceded assessment. Expanded inspect rechecked the unchanged target and author-final dossiers.
- Minor construct finding does not establish that the N-terminal substitution changes inhibition.
- All current named IDs were independently looked up in final shared authority snapshots; current source pointers and exact primary clauses were independently inspected.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T091416Z-ergothioneine-initial-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: 'Independent initial ergothioneine pathway review: EgtD preparation scope'
started_at: '2026-10-11T09:04:27Z'
finished_at: '2026-10-11T09:14:16Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_authority_cache)
  kind: agent
  independence: independent
  independence_basis: Authored the separate methylthiopropanoate record, not this
    target or its author dossiers. Independently read the full target, original sources,
    selected primary PDFs and current protein/Rhea/chemical authorities.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The complete seven-step native pathway and 33 chemical sides are supported
  with stated EgtA, strain, donor and assembly limitations. One minor EgtD product-inhibition
  attribution finding requires the experimental construct scope to be preserved. Coordinated
  tests passed; a source-corrected successor is still required.
source:
  git_revision: 7c555ecacc2b2708b246a68dcc9b64444791f526
  state: working_tree
  inputs:
  - path: data/identifier_authorities/ontology.json
    sha256: 6aa3c04fbb8dfebfba2a774e432764ee578f8951a140298a98c706396a2f690f
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 8185c5ca95a6c8eadc2e71c072916a85bfdb21d814e253ba65cec5c203f7e764
    role: context
  - path: data/pathways/ergothioneine-biosynthesis-i.yaml
    sha256: a0a26b897757e072ec5640805db8ab9ed0961b6499e1c576d0751996a0f97b37
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
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-authority-delta.json
    sha256: e0d0871b9c9ae94476164a154e71d0fffff1aa6105be9cbb68ed3b6fe9fbd900
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-curation.md
    sha256: 6486099f5225f0fb4f7117a9ae2cafd1030821106b0a48932d17c9e5843de248
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-dedup.json
    sha256: 15af28df8375b68da5e58e95018f5e42f759b5f903488f91f4a2340676e25a83
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-identifiers.json
    sha256: 854bb45d97e6b614663125b26c646069c8ce31deb0ac40a54ea1611d5824b8d0
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
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-replay.py
    sha256: 9ee0841c23dae4ddd593b53bff5ee0124fb547dc15e25165f1e4757b18ac3f75
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-source-manifest.json
    sha256: ccd05eb786f2dd1b7dd041e3c1ccf69ee0e6bb1aa7861d7071db45a87812da5e
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-source-projection.json
    sha256: 1f928fb46ac27e150d549fce08087d3d18aeac568897ec33dd19918f86f03ae8
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/ergothioneine-validation.json
    sha256: db32c90da8522eb936dda1e416f3e9a031b8a40fc0ae78dae8a7e97cb9da1fd8
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json
    sha256: 57da9dbc37e8048aaf2a226985b1334a92ec6096cdaf8a81333069e3a93fb49f
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
  description: Full independent scientific assessment of one author-frozen target,
    with original-source replay and inspected coordinated terminal gate receipts.
  selection: Exact author-frozen a0a26b897757e072ec5640805db8ab9ed0961b6499e1c576d0751996a0f97b37.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-7255
  exclusions:
  - target: Other cohort targets and corpus-wide scientific quality
    reason: Outside this individual independent review.
checks:
- check_id: inspect
  name: Canonical initial and expanded input inspection
  command: PYTHONPATH=src .venv/bin/python scripts/record_review.py inspect --targets
    /private/tmp/pathwaymech-next-203-ergothioneine-review/targets.yaml --input research/pathway_additions/2026-10-11-next-203/ergothioneine-authority-delta.json
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
    --input docs/CURATION.md --input docs/HARMONIZATION.md --input docs/CAUSAL_GRAPHS.md
    --input docs/record-review-profile.md --input src/pathwaymech/schema/pathwaymech.yaml
    --input src/pathwaymech/schema.py --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json --input research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json
  status: passed
  required: true
  exit_code: 0
  summary: Initial inspect preceded scientific assessment at 09:04:27Z. Expanded capture
    rechecked unchanged target and the final authored dossiers. A first expanded attempt
    used an incorrect schema path; the actual source schema path was then inspected
    successfully.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: independent-replay
  name: Independent original-source and KGX replay
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python /private/tmp/pathwaymech-next-203-ergothioneine-review/independent-replay.py
  status: passed
  required: true
  exit_code: 0
  summary: Actual reviewer session30119 exit0:54 original bodies,33 chemical sides,7
    atom/charge balances,exact native boundary and protein pointers,55 edges/101 evidence
    in actual KGX. Initial helper-only attempt assumed a nonexistent RDF direction
    property; corrected to exact native side and master predicates.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: root-validate
  name: Coordinated validate
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just validate
  status: passed
  required: true
  exit_code: 0
  summary: Parent reported actual terminal0 and reviewer inspected preserved 206-record
    native/closed/identifier/evidence/history/page QC log.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: root-lint
  name: Coordinated lint
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just lint
  status: passed
  required: true
  exit_code: 0
  summary: 'Parent reported actual terminal0 and reviewer inspected preserved corrected
    lint log: All checks passed. Earlier helper formatting failure was superseded.'
  target_ids:
  - MetaCyc:PWY-7255
- check_id: root-test
  name: Coordinated full test suite
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just test
  status: passed
  required: true
  summary: 'Actual session98675 terminal0 and preserved log inspected: 1059 passed,
    3 skipped, 3 upstream warnings in 498.43 seconds. Finished 09:13:36Z. This is
    the original pre-correction test result, not an attestation to future edits.'
  target_ids:
  - MetaCyc:PWY-7255
  exit_code: 0
- check_id: diff
  name: Whitespace check
  command: git diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Reviewer actually executed exit0. Untracked additions require parent staging/final
    checks.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: imodulondb
  name: Exact taxon dataset applicability
  command: Read retained canonical-client dataset inventory and imodulondb-applicability.json
  status: not_applicable
  required: true
  summary: Inspected20-organism/28-dataset inventory does not cover M. smegmatis;
    M. tuberculosis is a different species. No negative pathway or expression inference.
  target_ids:
  - MetaCyc:PWY-7255
- check_id: root-lint-initial
  name: Superseded original lint attempt
  command: PYTHONPATH=/private/tmp/pathwaymech-next-203-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just lint
  status: failed
  required: false
  exit_code: 1
  summary: Original gate receipt retains author/helper formatting failure; parent
    corrected formatting and reran lint terminal0, whose actual All checks passed
    log was inspected.
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
  summary: Independent original-body replay validates33 sides/seven balances and full
    evidence export; hidden/ignored-inclusive searches of data, research and reviews
    find prior leads/shared precursor chemistry, not another complete maintained route.
  snapshot_sha256: 194ae0ac4081dab0c917243dd3dce00b9dd83aec7e45eb81cb6da3da4db3fb63
- evidence_id: protein
  kind: database
  reference: Five current UniProt original individual JSON entries
  locator: comments/reaction, cofactor, subunit, organism and sequence
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Current mc2155 assignments and exact pointers verified. EgtA ECO0000250
    remains inferred; B/C/D experimental annotations are not promoted beyond the source
    preparation limitations.
- evidence_id: seebeck
  kind: primary_source
  reference: DOI:10.1021/ja101721e.s001
  locator: S2-S4 cloning and EgtD; S5-S9 EgtB chemistry; S7 FigureS6; S10 combined
    B/C activity
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Original DSM43465 clone/host distinctions, three SAM methyl groups, sulfur
    coupling, iron depletion/rescue and combined synthesis support source-scoped claims;
    metal figure independently rendered.
  snapshot_sha256: 8865d33ccc48125663acdcf27c5af5e10f1eead72258d95b5270c5e08ad18847
- evidence_id: egtc
  kind: primary_source
  reference: PMID:26079795
  locator: Accepted manuscript p2 Overall structure; pp5-6 Protein production
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Exact mc2155 A0R5M9 clone, tetramer supported by PISA and analytical SEC,
    C2A substrate complex and cross-species substrate-generation limit inspected.
  snapshot_sha256: 6e7a43aa9e761c39b86386355b6ca1e2b2005ba9674ad41b280265fe1aea344e
- evidence_id: egte2015
  kind: primary_source
  reference: PMID:26149121
  locator: JATS sec1 paragraphs1,3-9, Figures4-6
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Purified PLP enzyme, sulfenic trapping, DTT dependence, pyruvate/ammonia
    and unspecified physiological reductant verified. Coupled NADH consumption is
    not the pathway donor.
  snapshot_sha256: 5567e312f5e3fef6298af1b64dfc37ae9675ac8a9f003dcfd898f096d616b125
- evidence_id: egte2023
  kind: primary_source
  reference: PMID:38072054
  locator: sec3.2/p1, sec1.1/p2, sec1.2/p1
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Exact A0R5M7 mc2155 clone; solution-supported homodimer and neighboring-chain
    pocket. Pyruvate crystal tetramer is not generalized to solution.
  snapshot_sha256: d9c105c4d6b82abfba24f236558d6cd1719ae8cb1b5e7657acc2cf88864583ad
- evidence_id: inhibition
  kind: primary_source
  reference: DOI:10.1021/acschembio.8b00127.s001
  locator: p3 FigureS2; p1 assay conditions; p11 Protein Production; reference3 p25
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Product inhibition is real in the purified preparation. Production cross-reference
    identifies the 2014 construct; current edge omits the relevant construct and strain-transfer
    limitation.
  snapshot_sha256: 20e0596c264994c847c2e19c11896a0d014081454b55cd555d5c58eb24060b64
- evidence_id: construct
  kind: primary_source
  reference: PMID:24817736 / PMC4014345 and UniProtKB:A0R5M8
  locator: Original HTML sec2.1 paragraph1 full construct; current sequence.value
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: 2014 source names DSM43465/ATCC607. After tags are excluded,321 residues
    compare with only position2 A in the construct versus T in current mc2155. This
    difference does not prove a functional effect or refute inhibition.
  snapshot_sha256: 89ced1b7b2b1aad3ace06e7d0656d79285140ac46293e03f78f19a2a5f4701dd
- evidence_id: physiology
  kind: primary_source
  reference: PMID:23629716
  locator: HTML sec5/p1; sec12/p1 and Table3
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: Exact mc2155 egtD deletion loses detectable ergothioneine and complementation
    restores it; this supports pathway physiology without validating every formal
    intermediate.
  snapshot_sha256: 6551e9000cd0f815c48f5d55f827aae32a05094f92c2ebdaecbee94f59c12e61
- evidence_id: context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json
  locator: candidate_dispositions PWY7255
  accessed_at: '2026-10-11T09:13:50Z'
  support: supports
  summary: No covered selected species dataset; unrelated Mtb context not transferred.
  snapshot_sha256: 57da9dbc37e8048aaf2a226985b1334a92ec6096cdaf8a81333069e3a93fb49f
- evidence_id: gates
  kind: validation
  reference: /private/tmp/pathwaymech-next-203-final-gate-receipts.json
  locator: All seven original per-command receipts; corrected lint log separately
  accessed_at: '2026-10-11T09:14:16Z'
  support: supports
  summary: Actual original full test1059 passed/3 skipped;206-record validate, render,
    identifiers, KGX and diff exit0. Initial lint1 followed by corrected lint0. Root
    reported terminal results and reviewer inspected logs.
  snapshot_sha256: 9b4b74250e5e9cd6b615bf3c7c4513d1c0d111c660d803e9ace2f36b73c44bb3
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
  outcome: concern
  summary: Edge048 names native A0R5M8 but its source describes a linked DSM43465-derived
    engineered preparation. A source-specific construct/transfer qualification or
    contextual-only representation is required.
  target_ids:
  - MetaCyc:PWY-7255
  evidence_ids:
  - inhibition
  - construct
findings:
- finding_id: f-egtd-inhibition-construct
  issue_key: ergothioneine-egtd-product-inhibition-construct-scope
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: EgtD inhibition evidence needs exact experimental preparation scope
  description: Edge048 links hercynine inhibition to current mc2155 A0R5M8 while citing
    the 2018 purified preparation without its linked DSM43465/ATCC607 construct limitation.
    The 2014 complete sequence differs at position 2 after tags are excluded. The
    experiment supports product inhibition; it does not independently establish unqualified
    inhibition of the exact native mc2155 form. Preserve measured preparation context
    and explicitly grade transfer, or keep the observation contextual without that
    specific regulatory edge.
  target_ids:
  - MetaCyc:PWY-7255
  field_paths:
  - mechanistic_edges[id=ergothioneine-edge-048]
  evidence_ids:
  - inhibition
  - construct
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained_record
  rule_id: review-yaml-record strain, construct and evidence scope
  native_severity: minor
  normalization_reason: Bounded attribution/qualification problem; the observed product
    inhibition is supported, sequence similarity is high and complete pathway chemistry
    remains intact.
actions:
- action_id: scope-inhibition
  description: Archive initial inputs, correct the exact-protein inhibition representation
    while retaining the experimental observation and complete seven-step pathway.
  finding_ids:
  - f-egtd-inhibition-construct
  target_ids:
  - MetaCyc:PWY-7255
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained_record
  acceptance_checks:
  - Preserve original review and exact inspected input bytes before mutation.
  - Explicitly document DSM43465/ATCC607 construct source and distinguish direct observation
    from mc2155 transfer, or move the observation to contextual EgtD evidence.
  - Recheck all changed source assertions and run applicable source/schema/KGX and
    coordinated gates.
  - Save an immutable successor retaining the exact issue key and previous occurrence.
limitations:
- EgtA activity is similarity-based; early B/C/D studies use DSM43465, while later
  EgtC/EgtE and genetic physiology ground mc2155.
- A physiological reductant is not identified; DTT is an experimental reductant, not
  a physiological assignment.
- Current terminal Rhea cationic equation differs from the explicitly selected balanced
  native neutral forms.
- PDF figures were rendered and inspected locally; no browser page visual QA is claimed.
- The current observation precedes the scoped issue371 correction and regenerated
  final publication artifacts; the successor must inspect those changed bytes and
  applicable checks.
notes:
- Initial canonical inspect preceded assessment. Expanded inspect rechecked the unchanged
  target and author-final dossiers.
- Minor construct finding does not establish that the N-terminal substitution changes
  inhibition.
- All current named IDs were independently looked up in final shared authority snapshots;
  current source pointers and exact primary clauses were independently inspected.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/371
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4014345/
- https://doi.org/10.1021/acschembio.8b00127
```
