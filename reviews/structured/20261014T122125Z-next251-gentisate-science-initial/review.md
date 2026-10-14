# Independent initial scientific review of gentisate degradation I

- Review: 20261014T122125Z-next251-gentisate-science-initial
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T12:14:56.498169Z
- Finished UTC: 2026-10-14T12:21:25Z
- Reviewer: codex:/root/next251_scientific_review (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The complete 35-edge record was read. Pathway identity, chemistry, enzyme variants and bounded metal/cofactor claims are supported by inspected sources, but the NagI assay endpoint omits a source primer conflict. One major finding; final corpus checks have not run.

## Scope And Provenance

One maintained gentisate record, all31 named identities and35 edges, source and construct scope.

Selection: Exact author-nominated data/pathways/gentisate-degradation-i.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cd42a526b06ce531e8326a2717d54d7ff770bd2b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-6223 | data/pathways/gentisate-degradation-i.yaml | maintained | gentisate degradation I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native review input inspection | passed | True | MetaCyc:PWY-6223 | Helper captured exact target bytes and current Git base before assessment. |
| just validate | skipped | True | MetaCyc:PWY-6223 | Draft-stage initial observation. Author has not yet rendered/scaffolded history or run final corpus gates; successor review will inspect actual final receipts. |
| just test | skipped | True | MetaCyc:PWY-6223 | Draft-stage initial observation. Author has not yet rendered/scaffolded history or run final corpus gates; successor review will inspect actual final receipts. |
| just lint | skipped | True | MetaCyc:PWY-6223 | Draft-stage initial observation. Author has not yet rendered/scaffolded history or run final corpus gates; successor review will inspect actual final receipts. |
| git diff --check | skipped | True | MetaCyc:PWY-6223 | Draft-stage initial observation. Author has not yet rendered/scaffolded history or run final corpus gates; successor review will inspect actual final receipts. |

## Scientific And Domain Assessments

### Exact pathway boundary

identity: supported. Targets: MetaCyc:PWY-6223.

PWY-6223 and three complete native reactions describe gentisate isomerization through fumarylpyruvate, not homogentisate or direct maleate hydrolysis.

### Chemical and directional identities

grounding: supported. Targets: MetaCyc:PWY-6223.

Inspected complete structure identities, formal charge states and Rhea direction assignments agree; automated original RDF replay passed all three atom/charge balances.

### Protein and taxon identity

grounding: supported. Targets: MetaCyc:PWY-6223.

Five proteins and three taxa are grounded to exact native/deposited identities. Cgl/BagL alternate isomerases do not imply complete enzyme realizations for every taxon.

### Experimental endpoint scope

scope: concern. Targets: MetaCyc:PWY-6223.

Cgl and BagL tagged endpoints are qualified correctly. NagI pWWF19-25 assay evidence is incorrectly attached to an unqualified full-length base protein while its primer conflicts with that sequence.

### Cofactor and metal edge scope

evidence: supported. Targets: MetaCyc:PWY-6223.

GSH/MSH and BagL thiol alternatives, similarity-only NagK Mg/Mn annotations and the condition-limited tagged enzyme metal effects retain the source limits.

### Reference source bounds

provenance: supported. Targets: MetaCyc:PWY-6223.

Native hashes identify originals. Primary text extraction hashes are explicitly typed and are not represented as full article or PubMed-abstract support for unarchived full text.

## Findings

### F1: NagI assay evidence lacks the primer-conflict construct qualification

major / open / confirmed; issue key: gentisate-nagi-pwwf1925-construct-scope.

gentisate-017 attaches PMID11133965 Figure2 pWWF19-25 activity directly to unqualified UniProtKB:O86041. The reported forward primer starts at native Met10 (AF036940.2 nt14163), while Table2/native deposit starts at nt14136 and the paper calls the construct complete. Exact expressed sequence is unverified. Current unqualified representation suppresses this material source conflict.

## Recommended Actions And Acceptance Checks

### A1

Qualify the gentisate-017 subject as the reported pWWF19-25 experimental construct, retain the complete-reading-frame versus Met10 primer conflict, and distinguish native deposited identity from actual expressed sequence. Do not claim a proven exact nine-residue deletion. Regenerate the record page after curation.

- Qualifier endpoint is subject, kind experimental_construct, supported by exact Methods primer/Table2 locators and native sequence provenance.
- Full expressed sequence remains explicitly unverified; a proven Δ1–9 construct is not invented.
- Record summary and research ledger preserve the conflict while retaining supported native catalytic identity and pathway boundary.
- Run final just render-pages, just validate, just test, just lint and git diff --check; successor review reassesses the changed target and actual receipts.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/pathways/gentisate-degradation-i.yaml; Entire record, all 35 edges and 15 references | partial | Read the complete maintained target. gentisate-017 uses unqualified UniProtKB:O86041 and attaches the pWWF19-25 Figure 2 assay. |
| nagi-conflict | https://pmc.ncbi.nlm.nih.gov/articles/PMC94927/; Methods: Expression of nag genes, nagI forward primer; Table 2 nagI; Results NagI catalyzes gentisate transformation | refutes | The reported forward coding primer maps to AF036940.2 nt 14163 (27 nt beyond start 14136), beginning at native O86041 Met10. The same paper calls the construct complete. The experimentally expressed sequence therefore remains uncertain, despite the native identity match. |
| sequence | research/pathway_additions/2026-10-14-next-251/gentisate/scientific-review/sequence-audit.json; Complete sequence comparisons against original ENA/UniProt/NCBI files | supports | All three U2 native sequences match deposited U2 proteins. Q8NLC1 matches NP_602215.1/BAC00415.1, and H6TG59 matches ADZ54051.1 and HQ897158 BagL. Native sequence equality does not resolve NagI assay primer conflict. |
| native | https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:PWY-6223; PGDB 27.0 Pathway, reaction-list, reaction-ordering, reaction-layout; full native reaction XML objects | supports | Native pathway is the complete three-reaction isomerization route. Native Rhea xrefs are directional 18238,17394,26169. Maleate hydrolysis is a distinct route. |
| u2-paper | https://pmc.ncbi.nlm.nih.gov/articles/PMC94927/; Methods, Tables 1–3, Results NagI/NagL/NagK, Figures 5–6 visually inspected | supports | U2 extracts and cloned enzymes support the complete gentisate-to-fumarate/pyruvate route. NagL uses GSH. NagK pWWF96 assays yield both products; pET construct was inactive. Source conflict on the NagI construct remains distinct. |
| bagl-paper | https://journals.asm.org/doi/10.1128/jb.00050-12; Methods; Table 1; Table 2; Results Biochemical properties; original Figure 3 visually inspected | supports | His6 BagL, its three thiol alternatives and the explicitly bounded metal perturbations agree with the inspected paper; no physiological Ni cofactor requirement follows. |
| cgl-paper | https://www.researchgate.net/publication/7296304_The_Gene_ncgl2918_Encodes_a_Novel_Maleylpyruvate_Isomerase_That_Needs_Mycothiol_as_Cofactor_and_Links_Mycothiol_Biosynthesis_and_Gentisate_Assimilation_in_Corynebacterium_glutamicum; Author-uploaded full-paper extracted text, Table 1, purification/metal Methods, Results mycothiol/metal effects, Figure 5 legend | supports | Tagged ncgl2918 catalysis and mycothiol use, Zn2+ at 121% and Fe3+ at 85% activity with 1mM/15min room-temperature conditions match the source. Figure5 image was not independently read. |
| rules | docs/CAUSAL_GRAPHS.md; Experimental constructs and molecular states | supports | Source-limited constructs differing or uncertain relative to named native proteins require the affected protein endpoint to be qualified. Generic graph validation cannot detect this omission. |
| chemical | Original MetaCyc compound XML; pinned ChEBI255 SQL; current ChEBI JSON; 19 chemicals; full InChI; current SMILES; native CML charge/connectivity; Rhea142 RDF | supports | Native full InChI preserves cis maleylpyruvate and trans fumarylpyruvate/fumarate; current ChEBI structures agree. ChEBI zwitterion/anion normalization is explicitly distinguished from assay protonation. Independent original RDF replay passed for all three complete sides and atom/charge balances. No chemical disagreement found in inspected originals. |

## Limits And Additional Notes

- Initial draft-stage observation; required full-corpus gates intentionally remain pending and completion is partial.
- Cgl2006 full-paper text and Figure5 legend were read through an author-uploaded text extraction; no independent visual inspection of its Figure5 image or original PDF download.
- Full-paper access to later NagL2008/Cgl2007 structural articles was not established; no additional mechanistic claims borrowed from their unseen text.
- The reviewer corrected an RDF audit implementation to aggregate repeated source subjects before the successful final check; the initial failed attempt was a reviewer-script defect, not a record defect.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T122125Z-next251-gentisate-science-initial
kind: record
repository: CultureBotAI/PathwayMech
title: Independent initial scientific review of gentisate degradation I
started_at: '2026-10-14T12:14:56.498169Z'
finished_at: '2026-10-14T12:21:25Z'
reviewer:
  identity: codex:/root/next251_scientific_review
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or edit pathway YAML, authorities, history,
    pages, or author research. Independently read raw sources and original papers;
    author artifacts were leads.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major experimental-construct scope defect; final gates pending
scientific_review: true
summary: The complete 35-edge record was read. Pathway identity, chemistry, enzyme
  variants and bounded metal/cofactor claims are supported by inspected sources, but
  the NagI assay endpoint omits a source primer conflict. One major finding; final
  corpus checks have not run.
source:
  git_revision: cd42a526b06ce531e8326a2717d54d7ff770bd2b
  state: working_tree
  inputs:
  - path: data/pathways/gentisate-degradation-i.yaml
    sha256: 73c361d79045aafb8563d0668756e77ddb2747685b035e8c440cac955b8a00dd
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: context
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/scientific-review/nagi-primer-conflict.json
    sha256: d8df142279aed9087bb279420fc723db4897f5ff8e2a34465db80ab60cdccb9c
    role: context
  - path: research/pathway_additions/2026-10-14-next-251/gentisate/scientific-review/sequence-audit.json
    sha256: bd1499142b2a97985e35b1c1123f2b240454f54b3ff44dd37c8317c6221e7548
    role: context
scope:
  description: One maintained gentisate record, all31 named identities and35 edges,
    source and construct scope.
  selection: Exact author-nominated data/pathways/gentisate-degradation-i.yaml
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-6223
  exclusions:
  - target: Other248 records
    reason: Not scientifically rereviewed in this single-record observation.
targets:
- target_id: MetaCyc:PWY-6223
  path: data/pathways/gentisate-degradation-i.yaml
  label: gentisate degradation I
  kind: maintained
  record_class: PathwayRecord
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/gentisate-degradation-i.yaml
    role: maintained scientific record
checks:
- check_id: inspect
  name: Native review input inspection
  status: passed
  required: true
  summary: Helper captured exact target bytes and current Git base before assessment.
  target_ids:
  - MetaCyc:PWY-6223
  command: python -B scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-251-scientific-review/targets.yaml
    --input docs/CAUSAL_GRAPHS.md --input scientific review receipts
  exit_code: 0
  expected_exit_code: 0
- check_id: validate
  name: just validate
  status: skipped
  required: true
  summary: Draft-stage initial observation. Author has not yet rendered/scaffolded
    history or run final corpus gates; successor review will inspect actual final
    receipts.
  target_ids:
  - MetaCyc:PWY-6223
  command: just validate
  scope_note: No passing result claimed.
- check_id: test
  name: just test
  status: skipped
  required: true
  summary: Draft-stage initial observation. Author has not yet rendered/scaffolded
    history or run final corpus gates; successor review will inspect actual final
    receipts.
  target_ids:
  - MetaCyc:PWY-6223
  command: just test
  scope_note: No passing result claimed.
- check_id: lint
  name: just lint
  status: skipped
  required: true
  summary: Draft-stage initial observation. Author has not yet rendered/scaffolded
    history or run final corpus gates; successor review will inspect actual final
    receipts.
  target_ids:
  - MetaCyc:PWY-6223
  command: just lint
  scope_note: No passing result claimed.
- check_id: diff-check
  name: git diff --check
  status: skipped
  required: true
  summary: Draft-stage initial observation. Author has not yet rendered/scaffolded
    history or run final corpus gates; successor review will inspect actual final
    receipts.
  target_ids:
  - MetaCyc:PWY-6223
  command: git diff --check
  scope_note: No passing result claimed.
evidence:
- evidence_id: target
  kind: record_content
  reference: data/pathways/gentisate-degradation-i.yaml
  locator: Entire record, all 35 edges and 15 references
  accessed_at: '2026-10-14T12:21:25Z'
  support: partial
  summary: Read the complete maintained target. gentisate-017 uses unqualified UniProtKB:O86041
    and attaches the pWWF19-25 Figure 2 assay.
  snapshot_sha256: 73c361d79045aafb8563d0668756e77ddb2747685b035e8c440cac955b8a00dd
- evidence_id: nagi-conflict
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC94927/
  locator: 'Methods: Expression of nag genes, nagI forward primer; Table 2 nagI; Results
    NagI catalyzes gentisate transformation'
  accessed_at: '2026-10-14T12:21:25Z'
  support: refutes
  summary: The reported forward coding primer maps to AF036940.2 nt 14163 (27 nt beyond
    start 14136), beginning at native O86041 Met10. The same paper calls the construct
    complete. The experimentally expressed sequence therefore remains uncertain, despite
    the native identity match.
- evidence_id: sequence
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-251/gentisate/scientific-review/sequence-audit.json
  locator: Complete sequence comparisons against original ENA/UniProt/NCBI files
  accessed_at: '2026-10-14T12:21:25Z'
  support: supports
  summary: All three U2 native sequences match deposited U2 proteins. Q8NLC1 matches
    NP_602215.1/BAC00415.1, and H6TG59 matches ADZ54051.1 and HQ897158 BagL. Native
    sequence equality does not resolve NagI assay primer conflict.
  snapshot_sha256: bd1499142b2a97985e35b1c1123f2b240454f54b3ff44dd37c8317c6221e7548
- evidence_id: native
  kind: database
  reference: https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:PWY-6223
  locator: PGDB 27.0 Pathway, reaction-list, reaction-ordering, reaction-layout; full
    native reaction XML objects
  accessed_at: '2026-10-14T12:21:25Z'
  support: supports
  summary: Native pathway is the complete three-reaction isomerization route. Native
    Rhea xrefs are directional 18238,17394,26169. Maleate hydrolysis is a distinct
    route.
  snapshot_sha256: 898e1be79846e91642bc26d65d6557a931ffc94499a4073741be76aa9af4753c
- evidence_id: u2-paper
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC94927/
  locator: Methods, Tables 1–3, Results NagI/NagL/NagK, Figures 5–6 visually inspected
  accessed_at: '2026-10-14T12:21:25Z'
  support: supports
  summary: U2 extracts and cloned enzymes support the complete gentisate-to-fumarate/pyruvate
    route. NagL uses GSH. NagK pWWF96 assays yield both products; pET construct was
    inactive. Source conflict on the NagI construct remains distinct.
- evidence_id: bagl-paper
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/jb.00050-12
  locator: Methods; Table 1; Table 2; Results Biochemical properties; original Figure
    3 visually inspected
  accessed_at: '2026-10-14T12:21:25Z'
  support: supports
  summary: His6 BagL, its three thiol alternatives and the explicitly bounded metal
    perturbations agree with the inspected paper; no physiological Ni cofactor requirement
    follows.
- evidence_id: cgl-paper
  kind: primary_source
  reference: https://www.researchgate.net/publication/7296304_The_Gene_ncgl2918_Encodes_a_Novel_Maleylpyruvate_Isomerase_That_Needs_Mycothiol_as_Cofactor_and_Links_Mycothiol_Biosynthesis_and_Gentisate_Assimilation_in_Corynebacterium_glutamicum
  locator: Author-uploaded full-paper extracted text, Table 1, purification/metal
    Methods, Results mycothiol/metal effects, Figure 5 legend
  accessed_at: '2026-10-14T12:21:25Z'
  support: supports
  summary: Tagged ncgl2918 catalysis and mycothiol use, Zn2+ at 121% and Fe3+ at 85%
    activity with 1mM/15min room-temperature conditions match the source. Figure5
    image was not independently read.
- evidence_id: rules
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Experimental constructs and molecular states
  accessed_at: '2026-10-14T12:21:25Z'
  support: supports
  summary: Source-limited constructs differing or uncertain relative to named native
    proteins require the affected protein endpoint to be qualified. Generic graph
    validation cannot detect this omission.
- evidence_id: chemical
  kind: authority
  reference: Original MetaCyc compound XML; pinned ChEBI255 SQL; current ChEBI JSON
  locator: 19 chemicals; full InChI; current SMILES; native CML charge/connectivity;
    Rhea142 RDF
  accessed_at: '2026-10-14T12:21:25Z'
  support: supports
  summary: Native full InChI preserves cis maleylpyruvate and trans fumarylpyruvate/fumarate;
    current ChEBI structures agree. ChEBI zwitterion/anion normalization is explicitly
    distinguished from assay protonation. Independent original RDF replay passed for
    all three complete sides and atom/charge balances. No chemical disagreement found
    in inspected originals.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact pathway boundary
  outcome: supported
  summary: PWY-6223 and three complete native reactions describe gentisate isomerization
    through fumarylpyruvate, not homogentisate or direct maleate hydrolysis.
  target_ids:
  - MetaCyc:PWY-6223
  evidence_ids:
  - native
  - u2-paper
- assessment_id: chemistry
  area: grounding
  topic: Chemical and directional identities
  outcome: supported
  summary: Inspected complete structure identities, formal charge states and Rhea
    direction assignments agree; automated original RDF replay passed all three atom/charge
    balances.
  target_ids:
  - MetaCyc:PWY-6223
  evidence_ids:
  - chemical
  - native
- assessment_id: proteins
  area: grounding
  topic: Protein and taxon identity
  outcome: supported
  summary: Five proteins and three taxa are grounded to exact native/deposited identities.
    Cgl/BagL alternate isomerases do not imply complete enzyme realizations for every
    taxon.
  target_ids:
  - MetaCyc:PWY-6223
  evidence_ids:
  - sequence
  - cgl-paper
  - bagl-paper
- assessment_id: assay-scope
  area: scope
  topic: Experimental endpoint scope
  outcome: concern
  summary: Cgl and BagL tagged endpoints are qualified correctly. NagI pWWF19-25 assay
    evidence is incorrectly attached to an unqualified full-length base protein while
    its primer conflicts with that sequence.
  target_ids:
  - MetaCyc:PWY-6223
  evidence_ids:
  - target
  - nagi-conflict
  - rules
- assessment_id: variants
  area: evidence
  topic: Cofactor and metal edge scope
  outcome: supported
  summary: GSH/MSH and BagL thiol alternatives, similarity-only NagK Mg/Mn annotations
    and the condition-limited tagged enzyme metal effects retain the source limits.
  target_ids:
  - MetaCyc:PWY-6223
  evidence_ids:
  - u2-paper
  - cgl-paper
  - bagl-paper
- assessment_id: provenance
  area: provenance
  topic: Reference source bounds
  outcome: supported
  summary: Native hashes identify originals. Primary text extraction hashes are explicitly
    typed and are not represented as full article or PubMed-abstract support for unarchived
    full text.
  target_ids:
  - MetaCyc:PWY-6223
  evidence_ids:
  - target
findings:
- external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/528
  finding_id: F1
  issue_key: gentisate-nagi-pwwf1925-construct-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: NagI assay evidence lacks the primer-conflict construct qualification
  description: gentisate-017 attaches PMID11133965 Figure2 pWWF19-25 activity directly
    to unqualified UniProtKB:O86041. The reported forward primer starts at native
    Met10 (AF036940.2 nt14163), while Table2/native deposit starts at nt14136 and
    the paper calls the construct complete. Exact expressed sequence is unverified.
    Current unqualified representation suppresses this material source conflict.
  target_ids:
  - MetaCyc:PWY-6223
  field_paths:
  - mechanistic_edges[id=gentisate-017].endpoint_qualifiers
  - mechanistic_edges[id=gentisate-017].description
  - description
  evidence_ids:
  - target
  - nagi-conflict
  - sequence
  - rules
  rule_id: docs/CAUSAL_GRAPHS.md#experimental-constructs-and-molecular-states
  native_severity: major
  normalization_reason: A source-specific assay is transferred to an unqualified native
    protein despite unresolved construct identity; pathway identity itself remains
    supported.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/gentisate-degradation-i.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Qualify the gentisate-017 subject as the reported pWWF19-25 experimental
    construct, retain the complete-reading-frame versus Met10 primer conflict, and
    distinguish native deposited identity from actual expressed sequence. Do not claim
    a proven exact nine-residue deletion. Regenerate the record page after curation.
  finding_ids:
  - F1
  target_ids:
  - MetaCyc:PWY-6223
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/gentisate-degradation-i.yaml
    role: maintained scientific record
  acceptance_checks:
  - Qualifier endpoint is subject, kind experimental_construct, supported by exact
    Methods primer/Table2 locators and native sequence provenance.
  - Full expressed sequence remains explicitly unverified; a proven Δ1–9 construct
    is not invented.
  - Record summary and research ledger preserve the conflict while retaining supported
    native catalytic identity and pathway boundary.
  - Run final just render-pages, just validate, just test, just lint and git diff
    --check; successor review reassesses the changed target and actual receipts.
limitations:
- Initial draft-stage observation; required full-corpus gates intentionally remain
  pending and completion is partial.
- Cgl2006 full-paper text and Figure5 legend were read through an author-uploaded
  text extraction; no independent visual inspection of its Figure5 image or original
  PDF download.
- Full-paper access to later NagL2008/Cgl2007 structural articles was not established;
  no additional mechanistic claims borrowed from their unseen text.
- The reviewer corrected an RDF audit implementation to aggregate repeated source
  subjects before the successful final check; the initial failed attempt was a reviewer-script
  defect, not a record defect.
tags:
- next251
- gentisate
- independent-science
```
