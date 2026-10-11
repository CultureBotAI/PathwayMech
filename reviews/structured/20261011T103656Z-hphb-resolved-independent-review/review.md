# Independent HP/HB successor: verified primary metadata and locator corrections

- Review: 20261011T103656Z-hphb-resolved-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T10:22:50.622385Z
- Finished UTC: 2026-10-11T10:36:56Z
- Reviewer: Codex independent reviewer (/root/pathway_literature_candidates) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Both minor findings are resolved against exact original primary sources and the four-field semantic delta. The full archaeal cycle, strain-qualified proteins, explicitly bounded assembly/cofactor evidence and all graph assertions remain supported. Initial observations remain immutable; scientific source limitations are retained.

## Scope And Provenance

Complete scientific successor retaining the initial whole-record assessment, with independent original-source verification of all four changed provenance fields, full changed-input reassessment and current coordinated gates.

Selection: Corrected target SHA256 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a3a31179b0533cacbf59559a3151c8ebcaac4f97.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5789 | data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml | maintained | 3-hydroxypropanoate/4-hydroxybutanate cycle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical pre-assessment inspection | passed | True | MetaCyc:PWY-5789 | Canonical inspection of corrected target and final author inputs preceded successor assessment; final reinspection captured the sealed shared gates. Initial and current hashes are explicit. |
| Independent original-source replay | passed | False | MetaCyc:PWY-5789 | Initial independent full original-source replay passed and remains in the immutable predecessor. The exact four-field correction preserves all chemistry/protein assertions; current source-specific acceptance and actual KGX were independently rechecked. |
| Independent actual KGX and schema projection | passed | False | MetaCyc:PWY-5789 | Independent correction replay session 83623 exited 0, checked all 109 reference hashes and 12 primary titles, resolved three corrected source selections, confirmed exact four-field delta and preserved current 87-node/164-edge/291-evidence KGX. |
| Read-only whitespace check | passed | True | MetaCyc:PWY-5789 | Actual independent read-only command exited 0. |
| Final coordinated render | passed | False | MetaCyc:PWY-5789 | Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-render.log SHA256 395e49f0cf6605d21489d6cee71983c6cb09927bfcb0f50067bbe5f0fa0b2af0, completed 2026-10-11T10:26:08.262607+00:00. Independently rehashed and read after the correction freeze. |
| Final coordinated validate | passed | True | MetaCyc:PWY-5789 | Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-validate.log SHA256 4b9e48cc5b595a0d481ca44ff6ce88f3a94810a08c06136ab9d9db3372f5abad, completed 2026-10-11T10:28:47.181570+00:00. Independently rehashed and read after the correction freeze. |
| Final coordinated test | passed | True | MetaCyc:PWY-5789 | Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-test.log SHA256 d84d590ae6a678400b1c90134a712807e1099b8d9f9b39358173beab945842b3, completed 2026-10-11T10:35:22.933281+00:00. Independently rehashed and read after the correction freeze. |
| Final coordinated lint | passed | True | MetaCyc:PWY-5789 | Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-lint.log SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41, completed 2026-10-11T10:26:08.567321+00:00. Independently rehashed and read after the correction freeze. |
| Final coordinated identifiers | passed | False | MetaCyc:PWY-5789 | Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-identifiers.log SHA256 4ad4b68a4c7d4eae12aa19f78ac3f098726216950ec9ec0e937e24fe21b759ea, completed 2026-10-11T10:26:32.547598+00:00. Independently rehashed and read after the correction freeze. |
| Final coordinated kgx | passed | False | MetaCyc:PWY-5789 | Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-kgx.log SHA256 fda40ce2b6193e1033be7645e4ee257252e165623848d880b758fdeac4550177, completed 2026-10-11T10:26:57.666640+00:00. Independently rehashed and read after the correction freeze. |
| Final coordinated diff | passed | False | MetaCyc:PWY-5789 | Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-diff.log SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, completed 2026-10-11T10:26:58.086745+00:00. Independently rehashed and read after the correction freeze. |

## Scientific And Domain Assessments

### Complete archaeal HP/HB cycle

identity: supported. Targets: MetaCyc:PWY-5789.

Native and primary scope agree on the full cycle through 4-hydroxybutyryl-CoA and thiolysis. The Chloroflexus glyoxylate-producing GO:0043427 route is distinct. All 18 native reaction objects have dispositions; no difficult regeneration step was omitted.

### Directions, whole chemical states and biological closure

grounding: supported. Targets: MetaCyc:PWY-5789.

All 78 exact source sides and 17 equations balance by original ChEBI formula/charge. Native/current crotonyl-CoA differs by broader conserved CoA stereochemistry, not an unsupported opposite acyl isomer. Net cycle gains one acetyl-CoA, consumes two inorganic carbons, four ATP and five NADPH, and produces one NADH; auxiliary hydration convention is explicit.

### Exact strain, native cross-reference repair and preparation scope

scope: supported. Targets: MetaCyc:PWY-5789.

All 21 selected proteins have exact DSM 5348 taxon metadata. Original CDSs resolve the swapped carboxylase subunits. Native, recombinant and cross-species experiments are separated; current annotation conflicts are retained and direct experiments take priority only where explicitly supported.

### Assemblies, alternative activities and inferred cofactors

representation: supported. Targets: MetaCyc:PWY-5789.

Measured assembly models retain their method limits. Msed_2001 monomer/octamer is handled through functional enables; Msed_1424 dimer/pentamer is tied to the respective native model/preparation. Alternative metal and activity edges retain qualifiers, and no unsupported universal or simultaneous cofactor occupancy is asserted.

### Assay inhibition and transcriptomic context

evidence: supported. Targets: MetaCyc:PWY-5789.

Carboxylase inhibitor edges are limited to the reported in-vitro concentrations and activities. The iModulon inventory is not applicable to the selected organism; absence is not mechanism evidence.

### Verified corrections with immutable finding lineage

provenance: supported. Targets: MetaCyc:PWY-5789.

Both source retrieval defects are corrected in their maintained owner. Exact title equality and claim-specific original paragraphs support the four-field delta. No chemistry, protein, organism or evidence-strength assertion was changed.

### Local endpoints and exported evidence

graph: supported. Targets: MetaCyc:PWY-5789.

Independent source/graph and actual KGX checks preserve all local nodes, 164 edges, 291 evidence blocks and 18 separately grounded continuity edges. Deterministic checks supplement the full source reading and do not establish experimental truth.

## Findings

### f-primary-title: Primary reference title includes bibliography article titles

minor / resolved / confirmed; issue key: hphb-primary-reference-title-extraction.

Initial observation: PMID:32218776/title contains 5,895 characters from the main title and 53 cited-paper titles. The external author builder selects //article-title//text() across the full JATS. Restrict extraction to /article/front/article-meta/title-group/article-title and preserve only that article title. Other original HTML titles checked in this target are unaffected.

Disposition: Corrected target 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a exactly matches the single original JATS front title, excluding all bibliography titles. The independent 12-title sweep and author metadata regression pass; no other target field changed apart from the separately reviewed three paragraph selectors. Final required gates pass.

### f-terminal-module-locators: Three terminal-module assertions cite a preparation paragraph instead of the supporting results

minor / resolved / confirmed; issue key: hphb-terminal-module-primary-locators.

Initial observation: Edges 122, 124 and 125 evidence[2] all select PMC3993168 Results section4/section1/p[1]. That paragraph discusses generic preparations and Msed_1321 rather than the asserted Msed_0656/Msed_0399 activities and completed reconstruction. Select the exact Abstract, named enzyme results and reconstitution paragraphs appropriate to each assertion. The full original article supports the stated biology.

Disposition: Corrected target 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a selects the exact original Results p2 and p4 for edges 122/124/125. Those paragraphs name the enzymes/activities and document completed in-vitro reconstitution. Original source hashes, four-field semantic equality and current KGX evidence were independently verified; final required gates pass. The source-specific scientific assertions remain unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-target | data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml; Complete record, all 164 edges and 109 references | supports | Corrected complete target was re-inspected. Only the title and three source locators changed; all 68 participants, 17 reactions, 164 edges, 291 evidence blocks and 109 references retain their scientific scope. |
| e-audit | research/pathway_additions/2026-10-11-next-206/hphb-initial-independent-review-audit.json; independent_checks; actual_kgx; primary_assertion_checks; findings | supports | Independent source replay verified 129 original bodies, 109 reference digests, 78 Rhea sides, 17 directions and atom/charge balances, 18 native members, 144 native XPath selections, 21 exact-taxon proteins and three original CDS translations. Separate actual KGX preserved 87 nodes, 164 edges and all 291 evidence blocks. |
| e-native | https://pathway.yeastgenome.org/getxml?META:PWY-5789; /ptools-xml/Pathway/reaction-list; reaction-layout; comment | supports | The complete native 18-object cycle is accounted for. Two acetyl-CoA carboxylase half-reactions are represented by independently issued net RHEA:11309; auxiliary carbon dioxide hydration is retained without an invented catalyst. |
| e-title | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7078158/fullTextXML; /article/front/article-meta/title-group/article-title versus //article-title | supports | The corrected reference title equals only the original JATS front title. The initial 5,895-character concatenation is preserved in the predecessor and archive; all 12 original primary article titles were checked. |
| e-module | https://pmc.ncbi.nlm.nih.gov/articles/PMC3993168/; Results / Purification and characterization of M. sedula enzymes / paragraphs 2 and 4 | supports | Corrected selectors retrieve paragraph 2 naming Msed_0656/Msed_0399 activities and paragraph 4 reporting the combined in-vitro reconstitution. The three source assertions now have their exact supporting passages. |
| e-strain | https://pmc.ncbi.nlm.nih.gov/articles/PMC3067578/; Abstract; Materials and Methods / bacterial strains and growth conditions | supports | The independent isotope study used autotrophic microaerobic TH2 (DSM 5348) at 75 degrees C and pH 2. Labeling supports cycle operation and succinyl-CoA as a major biosynthetic exit; it does not make acetyl-CoA the sole anabolic exit. |
| e-carboxylase | https://febs.onlinelibrary.wiley.com/doi/full/10.1046/j.1432-1033.2003.03434.x; Official publisher full-text web rendering: Molecular Properties; Catalytic Properties; Table 2; Methods | supports | The independently inspected publisher text supports the same purified archaeal holoenzyme acting on acetyl- and propionyl-CoA, a proposed tetramer of heterotrimers, divalent-ion dependence and specified in-vitro inhibitor conditions. Its retained digest is honestly scoped to tool-rendered JSON, not original publisher HTML. |
| e-cds | https://www.ebi.ac.uk/ena/browser/api/embl/AF461115?download=false; Original AF461115/AF461116 CDS translations AAO15571.1, AAO15572.1 and AAO15573.1 | supports | The three original translations exactly match A4YGI1 carboxyltransferase, A4YD22 biotin carboxylase and A4YD23 carrier. This corrects the reversed native BC/BCCP UniProt cross-references without silently transferring sequence or strain identities. |
| e-reductases | https://pmc.ncbi.nlm.nih.gov/articles/PMC2753041/; Results: native malonyl/succinyl-CoA reductase purification and peptide identification; recombinant Msed_1993 and Msed_1424; zinc analysis | supports | Native Msed_0709 activity/peptide evidence and directly characterized Msed_1993/Msed_1424 support the selected reductases. Zinc content and approximate assemblies are scoped to measured preparations; the unrelated current A4YGN0 catalytic annotation is explicitly rejected. |
| e-revised | https://pmc.ncbi.nlm.nih.gov/articles/PMC7845616/; Results and discussion of Msed_2001 activity and proteomic/kinetic capacity estimates | supports | Later data support Msed_2001 as the principal dehydratase/crotonase. The recorded percentages are protein-abundance and kinetics estimates, not flux or knockout measurements; measured alternative proteins remain qualified. |
| e-conflicts | https://pmc.ncbi.nlm.nih.gov/articles/PMC5433351/?pdf=render; Results: Msed_2001, HPCS/HPCD association, Msed_1426 coexpression and Msed_1424; source MCR labels | supports | The original study supports direct selected-protein activities while creating unresolved preparation-specific oligomer estimates and an MCR name/locus discrepancy. Those limitations are explicit, rather than treated as universally fixed assemblies or silent sequence corrections. |
| e-expression | research/pathway_additions/2026-10-11-next-206/imodulondb-dataset-inventory.json; datasets and originals[0]; imodulondb-applicability.json; offline replay | supports | The current hash-verified inventory has 20 organisms and 28 datasets, with no Metallosphaera dataset. Sulfolobus acidocaldarius is a different species. The appropriate disposition is not applicable to this strain; no biological absence is inferred. |
| e-prior | reviews/structured/20261011T101705Z-hphb-initial-independent-review/review.yaml; Complete initial YAML and paired Markdown; both findings | supports | The initial completed needs_curation observation and its two exact issue keys remain immutable. Hidden/ignored-inclusive search of reviews/structured found no competing occurrence before this successor. |
| e-correction | research/pathway_additions/2026-10-11-next-206/hphb-correction-independent-review-audit.json; semantic_delta; original_primary_hashes; actual_kgx | supports | Independent acceptance confirms exactly four changed fields, all original reference hashes, correct title and paragraph selection, unchanged node bytes and faithful current evidence export. |
| e-author-fix | research/pathway_additions/2026-10-11-next-206/hphb-provenance-fix.json; semantic_delta; source_proof; checks | supports | Author correction and meaningful negative guards are recorded separately from independent assessment. The first inline-HTML spacing guard failure and successful corrected full replay are retained honestly. |
| e-gates | research/pathway_additions/2026-10-11-next-206/integration-receipt.json; Final required command receipts, initial observations and graph/baseline checks | supports | Final coordinated checks were independently read and rehashed; current graph projection and baseline preservation pass. Deterministic success is distinct from scientific source review. |

## Limits And Additional Notes

- The 2003 publisher article was independently web-read; the retained local reference body is an explicitly labeled transformed/tool-rendered JSON. Unavailable original publisher HTML/PDF bodies are not called original scientific source bytes.
- The 2007 discovery paper was not available as inspected full text. Its FAD/Fe-S claim is retained only as explicit native database annotation, distinct from the 2014 measured activity.
- Oligomer estimates, source annotation/locus discrepancies, inferred cofactors and capacity-versus-flux limits remain source-specific; a completed review is not a claim that these scientific questions are settled.
- Reviewer replay initially required fixes to dependency and parser assumptions, documented in the independent audit; final actual replay passed. No target changes were made by the reviewer.
- The initial author and review evidence and gate results remain historical. Passing this successor resolves two provenance defects, not the source-specific unresolved oligomer or annotation questions already declared.
- Applied the review-resolution workflow while preserving the complete review-yaml-record scientific rubric. Read the entire initial YAML/Markdown pair and checked canonical history before successor assessment.
- All 16 formal initial-review input hashes match content-addressed archived copies. Current changed author projections, helper guards, source manifests, receipts and generated integration were explicitly re-inspected.
- No competing heads for either exact issue key were found in the bounded hidden/ignored-inclusive reviews/structured search. Both prior occurrences and the original target are retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T103656Z-hphb-resolved-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: 'Independent HP/HB successor: verified primary metadata and locator corrections'
started_at: '2026-10-11T10:22:50.622385Z'
finished_at: '2026-10-11T10:36:56Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_literature_candidates)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Did not author HP/HB target or author dossiers. Authored the
    separate Chloroflexus first-cycle record and discussed common chemistry/source
    facts; those contributions are disclosed and do not substitute for independent
    HP/HB original-source inspection.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Both minor findings are resolved against exact original primary sources and
  the four-field semantic delta. The full archaeal cycle, strain-qualified proteins,
  explicitly bounded assembly/cofactor evidence and all graph assertions remain supported.
  Initial observations remain immutable; scientific source limitations are retained.
source:
  git_revision: a3a31179b0533cacbf59559a3151c8ebcaac4f97
  state: working_tree
  inputs:
  - path: data/identifier_authorities/ontology.json
    sha256: 62778b0fc25173af80c79041830e7fd04f34025aa782cd1f072e37aabb14cc48
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 18ae3d0007bd2e12d8848689791001efd6582541b2e8d395af585cb37f1c8a42
    role: context
  - path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    sha256: 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a
    role: target
  - path: research/pathway_additions/2026-10-11-next-206/baseline-preservation.json
    sha256: 11f74ca8dd31d8f98ab9439064546380cd473dac1a36a80943cd1a2373150932
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/generated-graph-kgx-audit.json
    sha256: 05eeca61db5e184a9ce9044ed7103c0a298ea4abfa6a2069b7f9c6fd000bb7f9
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-authority-inputs.json
    sha256: 1ab45ab44aad4bb2139e22b50362f62644a1c82ba91d80c2269dd6f0540d3776
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-correction-independent-review-audit.json
    sha256: f79d814feeaf1bbc0de20009192e45c4e60ee80a79222efe9705daf3019ea5da
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-curation.md
    sha256: 48d4894bda35fd33a0156b0def59fd04224b4eb4b83b4b61497f08e84ac5eca8
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-dedup.json
    sha256: 93a62d0d7af09e99e5a7916e6e23feb3e81b8073ba9fc05f4a0b2a9eadb51de0
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-identifiers.json
    sha256: c7c08d0fca02adf1d5ec0ab67172aac85069077fee8ce4052d0a49438c42d255
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-initial-independent-review-audit.json
    sha256: dc67520d6b5ab6dd401d6d74c7a71724a4adfdc1abf4e3e795060d3cd90fbd41
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-protein-projection.json
    sha256: 807cfde11bf4da90e071b8bcc482b9f1b6d6359f2ddae7fe3ae8156dc510c543
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-provenance-fix.json
    sha256: 44f32810a41659cfb006d04717722b34fb9befbd617fce0137780e62614595fb
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-replay.py
    sha256: eadc3046bd7da80c11827f36933fece2ab083341d61396fe0d7a308bf8f23461
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-source-manifest.json
    sha256: a360ac8dc66e315749ac72ea2b491ce4f485b1249bd908d3621073f8c18d32fb
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-source-projection.json
    sha256: d9e17f0278c3346530f7f35ee0e163b53ede5e6a8e933851d1861707d4b1d5dd
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/hphb-validation.json
    sha256: 12f857f70141720d28e770c5facc9b092dd832051e25aeeaf60c81bf4ecf0434
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/integration-receipt.json
    sha256: 0fe311ae293bc38532784a32b38261e4afcfabde7b140783fe9d8581e9157192
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/review-correction-audit.json
    sha256: 95ad9a191d99b1176d9c04f6e053c2a83eb468060e5b625934b28a9030c27485
    role: context
  - path: reviews/structured/20261011T101705Z-hphb-initial-independent-review/review.md
    sha256: ebabb9e84bde74997658ac9dcf7525ff1317b48a8de0d813f62e5411cf5241f2
    role: context
  - path: reviews/structured/20261011T101705Z-hphb-initial-independent-review/review.yaml
    sha256: 89c93a7c8a8c6d291678b50e0e1eb29920c5d1f6f0614747e9a9618fbbdadc50
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: ffa1107da83c8ff173833662e78ba73c779bbab9f2da33cea993b614e99d6345
    role: context
targets:
- target_id: MetaCyc:PWY-5789
  path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
  label: 3-hydroxypropanoate/4-hydroxybutanate cycle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    role: maintained pathway
scope:
  description: Complete scientific successor retaining the initial whole-record assessment,
    with independent original-source verification of all four changed provenance fields,
    full changed-input reassessment and current coordinated gates.
  selection: Corrected target SHA256 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5789
  exclusions:
  - target: Other two cohort pathway records
    reason: Different scientific review ownership; authored first-cycle science is
      explicitly excluded from self-review.
  - target: New laboratory replication and unspecified organism generalization
    reason: Evidence review only; exact source strain/preparation and recorded scientific
      limitations remain.
checks:
- check_id: inspect
  name: Canonical pre-assessment inspection
  command: PYTHONPATH=src .venv/bin/python scripts/record_review.py inspect --targets
    /private/tmp/pathwaymech-next-206-hphb-independent-review/targets.yaml with explicit
    authority, schema and author input paths
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Canonical inspection of corrected target and final author inputs preceded
    successor assessment; final reinspection captured the sealed shared gates. Initial
    and current hashes are explicit.
- check_id: independent-original-replay
  name: Independent original-source replay
  command: PYTHONPATH=src .venv/bin/python /private/tmp/pathwaymech-next-206-hphb-independent-review/replay.py
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Initial independent full original-source replay passed and remains in the
    immutable predecessor. The exact four-field correction preserves all chemistry/protein
    assertions; current source-specific acceptance and actual KGX were independently
    rechecked.
- check_id: actual-kgx
  name: Independent actual KGX and schema projection
  command: PYTHONPATH=src .venv/bin/python /private/tmp/pathwaymech-next-206-hphb-independent-review/recheck-correction.py
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Independent correction replay session 83623 exited 0, checked all 109 reference
    hashes and 12 primary titles, resolved three corrected source selections, confirmed
    exact four-field delta and preserved current 87-node/164-edge/291-evidence KGX.
- check_id: diff
  name: Read-only whitespace check
  command: git diff --check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Actual independent read-only command exited 0.
- check_id: final-render
  name: Final coordinated render
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just render-pages
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-render.log
    SHA256 395e49f0cf6605d21489d6cee71983c6cb09927bfcb0f50067bbe5f0fa0b2af0, completed
    2026-10-11T10:26:08.262607+00:00. Independently rehashed and read after the correction
    freeze.
- check_id: final-validate
  name: Final coordinated validate
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just validate
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-validate.log
    SHA256 4b9e48cc5b595a0d481ca44ff6ce88f3a94810a08c06136ab9d9db3372f5abad, completed
    2026-10-11T10:28:47.181570+00:00. Independently rehashed and read after the correction
    freeze.
- check_id: final-test
  name: Final coordinated test
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just test
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-test.log
    SHA256 d84d590ae6a678400b1c90134a712807e1099b8d9f9b39358173beab945842b3, completed
    2026-10-11T10:35:22.933281+00:00. Independently rehashed and read after the correction
    freeze.
- check_id: final-lint
  name: Final coordinated lint
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just lint
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-lint.log
    SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41, completed
    2026-10-11T10:26:08.567321+00:00. Independently rehashed and read after the correction
    freeze.
- check_id: final-identifiers
  name: Final coordinated identifiers
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just check-identifiers
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-identifiers.log
    SHA256 4ad4b68a4c7d4eae12aa19f78ac3f098726216950ec9ec0e937e24fe21b759ea, completed
    2026-10-11T10:26:32.547598+00:00. Independently rehashed and read after the correction
    freeze.
- check_id: final-kgx
  name: Final coordinated kgx
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just kgx-export --output-dir /private/tmp/pathwaymech-next-206-kgx
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-kgx.log
    SHA256 fda40ce2b6193e1033be7645e4ee257252e165623848d880b758fdeac4550177, completed
    2026-10-11T10:26:57.666640+00:00. Independently rehashed and read after the correction
    freeze.
- check_id: final-diff
  name: Final coordinated diff
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    git diff --check
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-5789
  summary: Actual root-coordinated terminal 0; log /private/tmp/pathwaymech-next-206-verification-publication-diff.log
    SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, completed
    2026-10-11T10:26:58.086745+00:00. Independently rehashed and read after the correction
    freeze.
evidence:
- evidence_id: e-target
  kind: record_content
  reference: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
  locator: Complete record, all 164 edges and 109 references
  accessed_at: '2026-10-11T10:36:56Z'
  support: supports
  summary: Corrected complete target was re-inspected. Only the title and three source
    locators changed; all 68 participants, 17 reactions, 164 edges, 291 evidence blocks
    and 109 references retain their scientific scope.
  snapshot_sha256: 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a
- evidence_id: e-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-206/hphb-initial-independent-review-audit.json
  locator: independent_checks; actual_kgx; primary_assertion_checks; findings
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: Independent source replay verified 129 original bodies, 109 reference digests,
    78 Rhea sides, 17 directions and atom/charge balances, 18 native members, 144
    native XPath selections, 21 exact-taxon proteins and three original CDS translations.
    Separate actual KGX preserved 87 nodes, 164 edges and all 291 evidence blocks.
  snapshot_sha256: dc67520d6b5ab6dd401d6d74c7a71724a4adfdc1abf4e3e795060d3cd90fbd41
- evidence_id: e-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY-5789
  locator: /ptools-xml/Pathway/reaction-list; reaction-layout; comment
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: The complete native 18-object cycle is accounted for. Two acetyl-CoA carboxylase
    half-reactions are represented by independently issued net RHEA:11309; auxiliary
    carbon dioxide hydration is retained without an invented catalyst.
  snapshot_sha256: 134f07865db2c2e86fcddf093a2e1cc1188f91a6a1f54a004d328efa52c5ab54
- evidence_id: e-title
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7078158/fullTextXML
  locator: /article/front/article-meta/title-group/article-title versus //article-title
  accessed_at: '2026-10-11T10:36:56Z'
  support: supports
  summary: The corrected reference title equals only the original JATS front title.
    The initial 5,895-character concatenation is preserved in the predecessor and
    archive; all 12 original primary article titles were checked.
  snapshot_sha256: 6a86bad3966f1aa6c2d17b2a2383bd9a1184b762ff3901bae38b39cc52cc4f84
- evidence_id: e-module
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3993168/
  locator: Results / Purification and characterization of M. sedula enzymes / paragraphs
    2 and 4
  accessed_at: '2026-10-11T10:36:56Z'
  support: supports
  summary: Corrected selectors retrieve paragraph 2 naming Msed_0656/Msed_0399 activities
    and paragraph 4 reporting the combined in-vitro reconstitution. The three source
    assertions now have their exact supporting passages.
  snapshot_sha256: e31d389454b3fa78e2ae08593a07fdb9772cb9f46411593f6fa86b8630913fa0
- evidence_id: e-strain
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3067578/
  locator: Abstract; Materials and Methods / bacterial strains and growth conditions
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: The independent isotope study used autotrophic microaerobic TH2 (DSM 5348)
    at 75 degrees C and pH 2. Labeling supports cycle operation and succinyl-CoA as
    a major biosynthetic exit; it does not make acetyl-CoA the sole anabolic exit.
  snapshot_sha256: 2381c35a8ca1991eb874fa97df5c3358d8d512b690d32f4c6563b5eedc28b586
- evidence_id: e-carboxylase
  kind: primary_source
  reference: https://febs.onlinelibrary.wiley.com/doi/full/10.1046/j.1432-1033.2003.03434.x
  locator: 'Official publisher full-text web rendering: Molecular Properties; Catalytic
    Properties; Table 2; Methods'
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: The independently inspected publisher text supports the same purified archaeal
    holoenzyme acting on acetyl- and propionyl-CoA, a proposed tetramer of heterotrimers,
    divalent-ion dependence and specified in-vitro inhibitor conditions. Its retained
    digest is honestly scoped to tool-rendered JSON, not original publisher HTML.
  snapshot_sha256: 1bf5ef7240acd43a7d99617eb7c06fcf6f72216af1d90781686c1959ea5a3baf
- evidence_id: e-cds
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/AF461115?download=false
  locator: Original AF461115/AF461116 CDS translations AAO15571.1, AAO15572.1 and
    AAO15573.1
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: The three original translations exactly match A4YGI1 carboxyltransferase,
    A4YD22 biotin carboxylase and A4YD23 carrier. This corrects the reversed native
    BC/BCCP UniProt cross-references without silently transferring sequence or strain
    identities.
  snapshot_sha256: ad39cca1e4b0f521bfcee44566406ae2355a32914fb7bc4a34023ec2eaa26d01
- evidence_id: e-reductases
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2753041/
  locator: 'Results: native malonyl/succinyl-CoA reductase purification and peptide
    identification; recombinant Msed_1993 and Msed_1424; zinc analysis'
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: Native Msed_0709 activity/peptide evidence and directly characterized Msed_1993/Msed_1424
    support the selected reductases. Zinc content and approximate assemblies are scoped
    to measured preparations; the unrelated current A4YGN0 catalytic annotation is
    explicitly rejected.
  snapshot_sha256: 007d86b186a3da978f6ca10256d101d930828314380fa1071fafbeefa0ee6807
- evidence_id: e-revised
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7845616/
  locator: Results and discussion of Msed_2001 activity and proteomic/kinetic capacity
    estimates
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: Later data support Msed_2001 as the principal dehydratase/crotonase. The
    recorded percentages are protein-abundance and kinetics estimates, not flux or
    knockout measurements; measured alternative proteins remain qualified.
  snapshot_sha256: 2247c350a1f9667908142b512fc4669bcfe7e8cf897087f0c4579beb7ff54961
- evidence_id: e-conflicts
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5433351/?pdf=render
  locator: 'Results: Msed_2001, HPCS/HPCD association, Msed_1426 coexpression and
    Msed_1424; source MCR labels'
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: The original study supports direct selected-protein activities while creating
    unresolved preparation-specific oligomer estimates and an MCR name/locus discrepancy.
    Those limitations are explicit, rather than treated as universally fixed assemblies
    or silent sequence corrections.
  snapshot_sha256: 426c21ac77b49b5d82ca871d3d0eb4cd523b22454b4084fea626fc592febeedd
- evidence_id: e-expression
  kind: database
  reference: research/pathway_additions/2026-10-11-next-206/imodulondb-dataset-inventory.json
  locator: datasets and originals[0]; imodulondb-applicability.json; offline replay
  accessed_at: '2026-10-11T10:17:05Z'
  support: supports
  summary: The current hash-verified inventory has 20 organisms and 28 datasets, with
    no Metallosphaera dataset. Sulfolobus acidocaldarius is a different species. The
    appropriate disposition is not applicable to this strain; no biological absence
    is inferred.
  snapshot_sha256: d84677b8bd4bcb4114f4ae918186f28fe5faceba702fc195e62296f259c42fce
- evidence_id: e-prior
  kind: prior_review
  reference: reviews/structured/20261011T101705Z-hphb-initial-independent-review/review.yaml
  locator: Complete initial YAML and paired Markdown; both findings
  accessed_at: '2026-10-11T10:36:56Z'
  support: supports
  summary: The initial completed needs_curation observation and its two exact issue
    keys remain immutable. Hidden/ignored-inclusive search of reviews/structured found
    no competing occurrence before this successor.
  snapshot_sha256: 89c93a7c8a8c6d291678b50e0e1eb29920c5d1f6f0614747e9a9618fbbdadc50
- evidence_id: e-correction
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-206/hphb-correction-independent-review-audit.json
  locator: semantic_delta; original_primary_hashes; actual_kgx
  accessed_at: '2026-10-11T10:36:56Z'
  support: supports
  summary: Independent acceptance confirms exactly four changed fields, all original
    reference hashes, correct title and paragraph selection, unchanged node bytes
    and faithful current evidence export.
  snapshot_sha256: f79d814feeaf1bbc0de20009192e45c4e60ee80a79222efe9705daf3019ea5da
- evidence_id: e-author-fix
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-206/hphb-provenance-fix.json
  locator: semantic_delta; source_proof; checks
  accessed_at: '2026-10-11T10:36:56Z'
  support: supports
  summary: Author correction and meaningful negative guards are recorded separately
    from independent assessment. The first inline-HTML spacing guard failure and successful
    corrected full replay are retained honestly.
  snapshot_sha256: 44f32810a41659cfb006d04717722b34fb9befbd617fce0137780e62614595fb
- evidence_id: e-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-206/integration-receipt.json
  locator: Final required command receipts, initial observations and graph/baseline
    checks
  accessed_at: '2026-10-11T10:36:56Z'
  support: supports
  summary: Final coordinated checks were independently read and rehashed; current
    graph projection and baseline preservation pass. Deterministic success is distinct
    from scientific source review.
  snapshot_sha256: 0fe311ae293bc38532784a32b38261e4afcfabde7b140783fe9d8581e9157192
assessments:
- assessment_id: a-boundary
  area: identity
  topic: Complete archaeal HP/HB cycle
  outcome: supported
  summary: Native and primary scope agree on the full cycle through 4-hydroxybutyryl-CoA
    and thiolysis. The Chloroflexus glyoxylate-producing GO:0043427 route is distinct.
    All 18 native reaction objects have dispositions; no difficult regeneration step
    was omitted.
  target_ids:
  - MetaCyc:PWY-5789
  evidence_ids:
  - e-native
  - e-strain
  - e-audit
- assessment_id: a-chemistry
  area: grounding
  topic: Directions, whole chemical states and biological closure
  outcome: supported
  summary: All 78 exact source sides and 17 equations balance by original ChEBI formula/charge.
    Native/current crotonyl-CoA differs by broader conserved CoA stereochemistry,
    not an unsupported opposite acyl isomer. Net cycle gains one acetyl-CoA, consumes
    two inorganic carbons, four ATP and five NADPH, and produces one NADH; auxiliary
    hydration convention is explicit.
  target_ids:
  - MetaCyc:PWY-5789
  evidence_ids:
  - e-audit
  - e-native
- assessment_id: a-protein
  area: scope
  topic: Exact strain, native cross-reference repair and preparation scope
  outcome: supported
  summary: All 21 selected proteins have exact DSM 5348 taxon metadata. Original CDSs
    resolve the swapped carboxylase subunits. Native, recombinant and cross-species
    experiments are separated; current annotation conflicts are retained and direct
    experiments take priority only where explicitly supported.
  target_ids:
  - MetaCyc:PWY-5789
  evidence_ids:
  - e-cds
  - e-carboxylase
  - e-reductases
  - e-conflicts
- assessment_id: a-assemblies
  area: representation
  topic: Assemblies, alternative activities and inferred cofactors
  outcome: supported
  summary: Measured assembly models retain their method limits. Msed_2001 monomer/octamer
    is handled through functional enables; Msed_1424 dimer/pentamer is tied to the
    respective native model/preparation. Alternative metal and activity edges retain
    qualifiers, and no unsupported universal or simultaneous cofactor occupancy is
    asserted.
  target_ids:
  - MetaCyc:PWY-5789
  evidence_ids:
  - e-reductases
  - e-conflicts
  - e-revised
  - e-audit
- assessment_id: a-regulation
  area: evidence
  topic: Assay inhibition and transcriptomic context
  outcome: supported
  summary: Carboxylase inhibitor edges are limited to the reported in-vitro concentrations
    and activities. The iModulon inventory is not applicable to the selected organism;
    absence is not mechanism evidence.
  target_ids:
  - MetaCyc:PWY-5789
  evidence_ids:
  - e-carboxylase
  - e-expression
- assessment_id: a-provenance
  area: provenance
  topic: Verified corrections with immutable finding lineage
  outcome: supported
  summary: Both source retrieval defects are corrected in their maintained owner.
    Exact title equality and claim-specific original paragraphs support the four-field
    delta. No chemistry, protein, organism or evidence-strength assertion was changed.
  target_ids:
  - MetaCyc:PWY-5789
  evidence_ids:
  - e-title
  - e-module
  - e-prior
  - e-correction
  - e-author-fix
  - e-gates
- assessment_id: a-graph
  area: graph
  topic: Local endpoints and exported evidence
  outcome: supported
  summary: Independent source/graph and actual KGX checks preserve all local nodes,
    164 edges, 291 evidence blocks and 18 separately grounded continuity edges. Deterministic
    checks supplement the full source reading and do not establish experimental truth.
  target_ids:
  - MetaCyc:PWY-5789
  evidence_ids:
  - e-audit
  - e-correction
  - e-gates
findings:
- finding_id: f-primary-title
  issue_key: hphb-primary-reference-title-extraction
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Primary reference title includes bibliography article titles
  description: 'Initial observation: PMID:32218776/title contains 5,895 characters
    from the main title and 53 cited-paper titles. The external author builder selects
    //article-title//text() across the full JATS. Restrict extraction to /article/front/article-meta/title-group/article-title
    and preserve only that article title. Other original HTML titles checked in this
    target are unaffected.'
  target_ids:
  - MetaCyc:PWY-5789
  field_paths:
  - references[id=PMID:32218776]/title
  evidence_ids:
  - e-title
  - e-target
  - e-audit
  - e-prior
  - e-correction
  - e-author-fix
  - e-gates
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    role: maintained pathway record
  rule_id: review-yaml-record precise original reference metadata
  native_severity: minor
  normalization_reason: Source attribution/display contamination does not change the
    supported pathway chemistry or primary evidence.
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T101705Z-hphb-initial-independent-review
    finding_id: f-primary-title
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/373
  disposition_reason: Corrected target 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a
    exactly matches the single original JATS front title, excluding all bibliography
    titles. The independent 12-title sweep and author metadata regression pass; no
    other target field changed apart from the separately reviewed three paragraph
    selectors. Final required gates pass.
- finding_id: f-terminal-module-locators
  issue_key: hphb-terminal-module-primary-locators
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Three terminal-module assertions cite a preparation paragraph instead of
    the supporting results
  description: 'Initial observation: Edges 122, 124 and 125 evidence[2] all select
    PMC3993168 Results section4/section1/p[1]. That paragraph discusses generic preparations
    and Msed_1321 rather than the asserted Msed_0656/Msed_0399 activities and completed
    reconstruction. Select the exact Abstract, named enzyme results and reconstitution
    paragraphs appropriate to each assertion. The full original article supports the
    stated biology.'
  target_ids:
  - MetaCyc:PWY-5789
  field_paths:
  - mechanistic_edges[id=hphb-edge-122]/evidence[2]/source_locator
  - mechanistic_edges[id=hphb-edge-124]/evidence[2]/source_locator
  - mechanistic_edges[id=hphb-edge-125]/evidence[2]/source_locator
  evidence_ids:
  - e-module
  - e-target
  - e-audit
  - e-prior
  - e-correction
  - e-author-fix
  - e-gates
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    role: maintained pathway record
  rule_id: review-yaml-record nearest source assertion and exact locator
  native_severity: minor
  normalization_reason: Bounded retrievability defect; no reaction, protein identity
    or complete-pathway change is required.
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T101705Z-hphb-initial-independent-review
    finding_id: f-terminal-module-locators
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/374
  disposition_reason: Corrected target 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a
    selects the exact original Results p2 and p4 for edges 122/124/125. Those paragraphs
    name the enzymes/activities and document completed in-vitro reconstitution. Original
    source hashes, four-field semantic equality and current KGX evidence were independently
    verified; final required gates pass. The source-specific scientific assertions
    remain unchanged.
actions: []
limitations:
- The 2003 publisher article was independently web-read; the retained local reference
  body is an explicitly labeled transformed/tool-rendered JSON. Unavailable original
  publisher HTML/PDF bodies are not called original scientific source bytes.
- The 2007 discovery paper was not available as inspected full text. Its FAD/Fe-S
  claim is retained only as explicit native database annotation, distinct from the
  2014 measured activity.
- Oligomer estimates, source annotation/locus discrepancies, inferred cofactors and
  capacity-versus-flux limits remain source-specific; a completed review is not a
  claim that these scientific questions are settled.
- Reviewer replay initially required fixes to dependency and parser assumptions, documented
  in the independent audit; final actual replay passed. No target changes were made
  by the reviewer.
- The initial author and review evidence and gate results remain historical. Passing
  this successor resolves two provenance defects, not the source-specific unresolved
  oligomer or annotation questions already declared.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/373
- https://github.com/CultureBotAI/PathwayMech/issues/374
notes:
- Applied the review-resolution workflow while preserving the complete review-yaml-record
  scientific rubric. Read the entire initial YAML/Markdown pair and checked canonical
  history before successor assessment.
- All 16 formal initial-review input hashes match content-addressed archived copies.
  Current changed author projections, helper guards, source manifests, receipts and
  generated integration were explicitly re-inspected.
- No competing heads for either exact issue key were found in the bounded hidden/ignored-inclusive
  reviews/structured search. Both prior occurrences and the original target are retained.
```
