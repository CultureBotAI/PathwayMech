# Independent scientific review of riboneogenesis

- Review: 20261010T234344Z-riboneogenesis-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-10T23:31:33Z
- Finished UTC: 2026-10-10T23:43:44Z
- Reviewer: Codex independent riboneogenesis reviewer (/root/verify_graph_publication) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact six-reaction yeast riboneogenesis route is supported across all 50 edges and 78 evidence blocks. One minor reaction-direction metadata defect was found before saving, filed as issue326 and corrected in three fields; independent reassessment confirms the fix. No open corrective finding remains. Similarity evidence, abstract-only secondary primary support, unavailable supplement and formal sugar-representation limits remain explicit.

## Scope And Provenance

Full independent assessment of one maintained pathway target and every local node, edge and reference.

Selection: Exact assigned data/pathways/riboneogenesis.yaml, PathBank:SMP0002406.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base dbf399e6ac90f6240fa5da2fac27386d49966171.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PathBank:SMP0002406 | data/pathways/riboneogenesis.yaml | maintained | Riboneogenesis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Initial governed inspection | passed | False | PathBank:SMP0002406 | Terminal exit 0, session 2292; target and initial source inputs captured before assessment. |
| Initial scratch native-object parser | failed | False | PathBank:SMP0002406 | Non-gating initial replay incorrectly keyed BioPAX objects only by rdf:about, omitting rdf:ID; failed native count assertion. Reviewer corrected scratch parser; no target change resulted. |
| Independent source and chemistry replay | passed | False | PathBank:SMP0002406 | Terminal exit 0, session 40737: all 19 chemical edges/locators, six balances/directions, participant/reaction/taxon labels, 15 reference digests and 22 raw-body hashes match final target. |
| Initial scratch manifest shape probe | failed | False | PathBank:SMP0002406 | Non-gating initial integration helper assumed mapping for the manifest list; exited 1. Corrected scratch helper; no repository change resulted. |
| Independent baseline authority retention | passed | False | PathBank:SMP0002406 | All 110 prior manifest entries, 1319 prior ontology terms/4 metadata rows and 1622 source terms/102 metadata rows remain exactly equal. |
| Final working-tree and staged whitespace checks | passed | True | PathBank:SMP0002406 | Both reviewer-executed checks exited 0 after final source and generated-input inspection. |
| Ignored-inclusive prior review search | passed | False | PathBank:SMP0002406 | Search returned no exact prior target occurrence; wrapper accepts ordinary rg no-match exit 1 and itself returned 0. |
| Final governed changed-input capture | passed | False | PathBank:SMP0002406 | Terminal exit0, session62556; changed target, receipts, authority snapshots and generated page re-inspected after source reassessment. |
| Exact three-field issue326 correction | passed | False | PathBank:SMP0002406 | Reviewer reconstructed the original target bytes by reverting only the three corrected direction fields; resulting SHA256 exactly equals initial governed SHA. All other bytes were unchanged. |
| Generated artifact hash and direction recheck | passed | False | PathBank:SMP0002406 | Reviewer rehashed both separately generated KGX files, confirmed all three corrected target source contexts are right_to_left, and rehashed generated page to audit receipt. |
| Initial full-test run overlapping rendering | failed | False | PathBank:SMP0002406 | Actual root run exited1:1042 passed,1 failed,3 skipped. Sole failure was test_cross_mech.test_rendered_site_publishes_the_index_and_it_is_current because the suite started before rendering completed. This is retained as superseded pre-freeze check history; required final full suite is separately recorded below. Log /private/tmp/pathwaymech-next-test-before-render.log; SHA256 e51aee5e56ba1f61427b0093f60d1b04799e0e3e0a58f1fa33d17d3ee6372e3f. |
| Initial completed-draft serialization check | failed | False | PathBank:SMP0002406 | Two initial governed draft validations exited1: first PyYAML aliases, then the unsupported evidence kind record. Reviewer disabled aliases and used governed record_content. Scientific content and repository inputs did not change. |
| Integrated validation | passed | True | PathBank:SMP0002406 | Terminal exit0 session12091:169 native/closed-schema records,251 histories,8834 evidence blocks,30 sources, exact identifiers,6 documentation files,research contract and169 current pages pass. |
| Integrated lint | passed | True | PathBank:SMP0002406 | All Ruff checks passed; root confirms terminal exit0. |
| Integrated page rendering | passed | False | PathBank:SMP0002406 | Rendered169 records, including final issue326 correction; root confirms terminal exit0. |
| Governed artifact synchronization | passed | False | PathBank:SMP0002406 | All22 governed artifacts match pinned CLAW revision; root confirms terminal exit0. |
| Final integrated test suite | passed | True | PathBank:SMP0002406 | Final frozen-input rerun, terminal exit0 session88101:1043 passed,3 skipped,3 upstream warnings in242.23 seconds. Supersedes the separately retained initial pre-render run. |

## Scientific And Domain Assessments

### Exact route and yeast scope

identity: supported. Targets: PathBank:SMP0002406.

Native PathBank identity and primary experiments support a distinct SBP/Shb17 pathway, not the ordinary transaldolase branch or a generic ribose biosynthesis process. BY4743-derived mutant/FY4/FY5 primary scope and S288c protein identity are preserved; species placement does not claim universal strain flux.

### Edges001-019: exact directed chemistry

grounding: supported. Targets: PathBank:SMP0002406.

All selected Rhea substrates/products, formal charges and coefficients agree with the inspected native RDF and issuing identities. Six equations balance. Source charge/tautomer differences are explicit manual route correspondences, not exactMatch assertions or invented sugar-isomerization enzymes.

### Edges020-027: supported gene-product functions

evidence: supported. Targets: PathBank:SMP0002406.

All eight enables assignments have scoped primary/native/reviewed support. Tkl2 similarity, Fba1 in-vivo perturbation versus current FBP-specific comment, Rpe1 similarity and Rki1 curator inference are explicit. Gene-product enables describes supported function without asserting isolated-monomer catalysis.

### Physical assembly boundary

representation: supported. Targets: PathBank:SMP0002406.

Unsupported native Tkl1/Tkl2 mixed complex is excluded. Current Tkl1 homodimer and similarity-supported Tkl2 homodimer, Fba1 homodimer and Shb17 dimer contexts are stated without invented physical assembly IDs. No absence of a SUBUNIT comment is promoted to monomer evidence.

### Edges028-033: exact six-step membership

graph: supported. Targets: PathBank:SMP0002406.

All six native reaction IDs are pathway members. The manual correspondence uses independent Rhea chemistry and primary equations1-5/Figure6E. Native reversible reactions remain noted while the curated graph selects riboneogenic direction.

### Edges034-048: cofactor scope

evidence: supported. Targets: PathBank:SMP0002406.

All fifteen exact metal/ThDP assignments match native reviewed comments and retain experimental versus similarity evidence. Alternative metals are not all required at once. Shb17 possible Mg crystal density and optional coordination are correctly not made an obligate cofactor edge.

### Edges049-050: protein localization

scope: supported. Targets: PathBank:SMP0002406.

Both cytoplasm and nucleus edges are nonexclusive Shb17 annotations with source attribution. Neither locates the entire route or supplies independent primary localization verification.

### Resolved pre-save minor issue326

provenance: supported. Targets: PathBank:SMP0002406.

Original target metadata disagreed with the established Rhea master-direction convention for three reactions. The author corrected only those fields after issue326 was filed. Reassessment confirms exact directions and unchanged chemistry/evidence. No correction remains open in the final target. The original finding is retained here because no defective interim structured bundle was saved.

### Bounded primary access and evidence tiers

completeness: unknown. Targets: PathBank:SMP0002406.

Primary2011 main article was inspected fully, but its supplement was unavailable as a PDF. PMID8929392 was abstract-only. Similarity-derived protein/cofactor assignments and curated localization remain clearly distinguished from direct primary proof. No new quantitative universal-flux claim is made.

### Final source and generated evidence integrity

graph: supported. Targets: PathBank:SMP0002406.

Final source identities, input hashes, scoped adapter context, generated graph evidence and required repository gates support a qualified pass. These checks do not imply a fresh scientific review of other records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/riboneogenesis.yaml; Complete target, 26 participants, 6 reactions, 50 edges, 78 evidence blocks and 15 references | supports | Full target read before assessment; final corrected content re-read. The independent reviewer did not author or edit this target. |
| e-native | https://pathbank.org/pathways/SMP0002406; PW002511.owl Pathway, Species/18, six Reactions/7089-7094, Catalysis7068-7072, ProteinComplex/4403 and exact entity references | supports | The native source identifies yeast Riboneogenesis and six steps. Five native steps are reversible; Shb17 hydrolysis is left-to-right. ProteinComplex/4403 mixes Tkl1 and Tkl2 and is correctly rejected as an unsupported physical heteromer. Native furanose ribose, unspecified GAP, and phosphate charge forms are not asserted to be exact matches to the Rhea representation. |
| e-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Rhea142 masters27626/30167/17461/10508/13677/14657; directed27628/30168/17462/10509/13679/14659; substrates/products, contains1, Participant/compound/accession; official direction TSV | supports | Independent full-RDF replay verifies all 19 chemical side assertions and exact locators; all coefficients1 and all six equations balance by elements and charge. Directed selection matches riboneogenic chemistry. The three reverse-to-master direction fields now agree with the official TSV. |
| e-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3163394/; PMID21663798; complete main article Introduction, equations1-5, Results/Figures3-6, Discussion and Experimental Procedures | supports | Inspected main HTML/text supports the Shb17-driven route, purified SBP hydrolysis, FBA1-DAmP labeling perturbation, Tkl1/Tkl2 roles, Rpe1/Rki1 pentose interconversion, experimental strain scope and Shb17 dimer structure. Main text calls Mg optional/metal-independent; no obligate Mg edge is warranted. Crystal beta-furanose SBP differs from Rhea formal open-chain form and this is explicit. |
| e-pentose-primary | https://pubmed.ncbi.nlm.nih.gov/8929392/; Complete indexed abstract preserved in EuropePMC core JSON; RPE1 deletion and RKI1 dosage-restoration sentences | supports | The abstract supports loss of RPE1 enzyme activity and RKI1 restoration of viability and specific ketol-isomerase activity. Two short target quotations are literal. Full article was not inspected; no detailed assay or assembly claim is attributed to it. |
| e-proteins | https://rest.uniprot.org/uniprotkb/P23254.json; Reviewed 2026_03 JSON P23254,P33315,P14540,P36136,P46969,Q12189: primary accession, organism559292, recommended name, catalytic/subunit/cofactor/subcellular comments and inline ECO codes | supports | All six gene products match. Tkl1 has experimental annotations; Tkl2 catalysis/assembly/cofactors remain by similarity. Fba1 current catalytic comment concerns FBP and its homodimer lacks inline code, while primary in-vivo evidence anchors SBP formation. Shb17 hydrolysis/dimer are experimental. Rpe1 catalytic/cofactor similarity and Rki1 ECO0000305 inference are correctly distinguished from the separate 1996 functional experiments. No missing SUBUNIT statement is treated as monomer proof. |
| e-cofactor | https://rest.uniprot.org/uniprotkb/P46969.json; Tkl1/Tkl2 comments[2-3], Fba1 cofactor comment, Rpe1 Co/Fe/Mn/Zn annotations; Shb17 subcellular location comment | supports | All 15 cofactor edges reproduce exact current annotations and evidence grades. Alternative metals are not simultaneous requirements. Both Shb17 localization statements are protein-specific, nonexclusive cytoplasm/nucleus annotations, not whole-pathway localization. The cited localization primary was not independently inspected. |
| e-replay | /private/tmp/pathwaymech-riboneogenesis-independent-review/replay.json; Independent reviewer full-RDF replay.py, native extraction, source/reference hashes, issuing authority labels, quote literals and dataset-output rehash | supports | Actual terminal exit0 confirms final SHA d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96, all 19 chemical edges and six balances, 15 references, 22 preserved bodies and bounded context receipt. |
| e-authority | research/pathway_additions/2026-10-10-next/authority-integration.json; Final regenerated snapshots and manifest compared independently with git base dbf399e6ac90f6240fa5da2fac27386d49966171 | supports | All original manifest/term/metadata values are retained. Final 121 manifest entries, 1331 ontology terms, 1633 source terms. Exact target labels were also independently queried from native/issuing sources. Rhea139 pinned label authority and explicitly versioned Rhea142 chemistry remain distinguished. |
| e-context | research/pathway_additions/2026-10-10-next/riboneogenesis-imodulondb-context.json; Canonical kg-microbe-sources imodulondb datasets; all 28 inventory rows and exact stdout hash | context_only | Author canonical command returned exit0 after DNS retry. Reviewer inspected/rehashed actual output. No Saccharomyces/yeast dataset key is supplied, so search/summarize are not applicable. This does not imply absent expression/module membership. |
| e-correction | https://github.com/CultureBotAI/PathwayMech/issues/326; Initial governed target f937afb93da295d6089762a409579244ddc07102b408744af2c9905f2974f746; final target d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96; reaction direction fields27628,13679,14659 | supports | Reviewer identified a minor source-direction metadata defect before saving a bundle. Integration agent filed issue326 and the author changed exactly three fields from left_to_right to right_to_left. Chemical edges/evidence/references did not change. Independent TSV/RDF replay verifies the correction. The local convention is corroborated by scripts/curate_metacyc_causal_graphs.py mapping RHEA_ID_RL to right_to_left. |
| e-generated | research/pathway_additions/2026-10-10-next/generated-graph-kgx-audit.json; Final delegated actual CLI KGX and generated SVG/evidence audit | supports | Complete target nodes, all 50 edges/78 evidence and reference metadata are retained; source-direction fields including issue326 are preserved in generated export contexts. This is a programmatic structural assessment, not visual browser QA. |
| e-gates | /private/tmp/pathwaymech-next-{validate,test,test-before-render,lint,render,vendored}.log; Root-executed final corpus logs and terminal outcomes; exact command environment and summaries retained in checks | supports | Reviewer inspected final delegated gate logs on frozen inputs and retained the superseded initial test failure. Deterministic consistency is separate from independent scientific judgement. Gate receipt binds actual final log hashes. |
| e-prior | reviews/ and reports/; rg -n -uu 'PathBank:SMP0002406&#124;riboneogenesis&#124;Riboneogenesis' reviews reports | supports | No prior exact target review/report match was returned; hidden and ignored files were included. This is bounded review-history search, not exhaustive literature absence. |

## Limits And Additional Notes

- PMID21663798 complete main HTML was read; the supplementary PDF endpoint returned HTML challenge data and no supplement-specific claim is verified. Browser recaptcha responses were not treated as article access.
- PMID8929392 was inspected as its complete indexed abstract, not the full paper. Other database-cited experimental publications are not represented as independently read full articles.
- Tkl2/Rpe1 and some cofactor assignments retain reviewed similarity evidence; Rki1 catalytic annotation retains curator inference. Reviewed localization is not independently inspected primary localization evidence.
- Formal Rhea sugar charge/tautomer identities differ from some PathBank native species and Shb17 bound beta-furanose structure. The target preserves route-level correspondence without unsupported exactMatch assertions.
- No verified physical homodimer source accession was used. Gene-product enables edges express function and preserve assembly context; no isolated-monomer catalysis is asserted.
- iModulonDB supplies no applicable yeast dataset in the current 28-row inventory; this coverage limit is not negative expression or mechanism evidence.
- Programmatic SVG/KGX verification is not browser visual QA. Required full-corpus gates were delegated and their actual logs/outcomes inspected.
- Generated page owner: data/pathways/riboneogenesis.yaml, src/pathwaymech/cli.py and src/pathwaymech/graph_view.py via just render-pages. Generated authority snapshots are owned by conf/identifier_sources.json, conf/identifier_policy.yaml and independently pinned issuing-source inputs; any future correction belongs in those maintained inputs and their generator.
- Initial governed target SHA f937afb93da295d6089762a409579244ddc07102b408744af2c9905f2974f746 was superseded by d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96 after exactly three source-direction corrections. The affected fields, owner, issue, old/new hashes and successful acceptance replay are retained in this review; there is no prior structured finding occurrence to fabricate.
- Final changed identifiers/validation receipts, regenerated authority snapshots and generated page were re-read and re-inspected before save.
- Two non-gating scratch harness failures are retained as actual checks; both were corrected in scratch and superseded by successful independent replay.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T234344Z-riboneogenesis-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of riboneogenesis
started_at: '2026-10-10T23:31:33Z'
finished_at: '2026-10-10T23:43:44Z'
reviewer:
  identity: Codex independent riboneogenesis reviewer (/root/verify_graph_publication)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: A different agent authored riboneogenesis and its scientific
    research. This reviewer read the whole target and exact native/primary evidence
    and did not edit it. This reviewer authored the separate methylglyoxal degradation
    III target; independence is claimed for this riboneogenesis scientific review,
    not for that separate record.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact six-reaction yeast riboneogenesis route is supported across all
  50 edges and 78 evidence blocks. One minor reaction-direction metadata defect was
  found before saving, filed as issue326 and corrected in three fields; independent
  reassessment confirms the fix. No open corrective finding remains. Similarity evidence,
  abstract-only secondary primary support, unavailable supplement and formal sugar-representation
  limits remain explicit.
source:
  git_revision: dbf399e6ac90f6240fa5da2fac27386d49966171
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: d1d18735600fe87f44822cfbc2448c82c10764fec2d45a9780a52c694a892d63
    role: context
  - path: conf/identifier_sources.json
    sha256: a7721b59eda937c30996ca8ceebbfaf292c7e860fcee4cc838cf4f64370da3fc
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: e454259ff88df93fb00b59537175421e1e594e67554ad6585fbe3ceb1587f88f
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 56725c311bc14ba7e1d649ba1c7faeeeac4f9785e1aa12fbee1707f4249afe9c
    role: context
  - path: data/pathways/riboneogenesis.yaml
    sha256: d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 3c861f2ab78e3bc62146d05af5ed5c4c4ae3e65343fc9bd44afa76da7f0b62e7
    role: context
  - path: pages/records/PathBank_SMP0002406.html
    sha256: 177da9aa755392dcdc1422266aff94b97eb2211138e89976a50389d2629b14ec
    role: context
  - path: research/pathway_additions/2026-10-10-next/authority-integration.json
    sha256: 76e569ddf2e9ba12dbfa6592036e78938aef8f3fd91ccf8dca9c5b1c6d09d189
    role: context
  - path: research/pathway_additions/2026-10-10-next/generated-graph-kgx-audit.json
    sha256: 2b3d20a77b87b26b17e1843e6db9910226afdb93799739400bbb4de57c773af7
    role: context
  - path: research/pathway_additions/2026-10-10-next/riboneogenesis-curation.md
    sha256: a2ee5edc391996aba7e99541841c44512d4eeb7536824b445a6ce69be13dad48
    role: context
  - path: research/pathway_additions/2026-10-10-next/riboneogenesis-identifiers.json
    sha256: 64e922b2d5a03f4013e31bd2c3f49cbc32df4d574c44b48bf5ab2bf5ef6e1b4d
    role: context
  - path: research/pathway_additions/2026-10-10-next/riboneogenesis-imodulondb-context.json
    sha256: 351cd9cb22aecc1cd881c994089d36fa08638a39333c6a4f6cb93ee385e3d23c
    role: context
  - path: research/pathway_additions/2026-10-10-next/riboneogenesis-source-manifest.json
    sha256: f712ae9d99c40f4d23e6161c2fde32acf48edc396a4dba7b3219eaa65e489dd8
    role: context
  - path: research/pathway_additions/2026-10-10-next/riboneogenesis-source-projection.json
    sha256: 048281ed4d5401b7798dd663f3e52d24f8aa34d3343864c81836648db589ce49
    role: context
  - path: research/pathway_additions/2026-10-10-next/riboneogenesis-validation.json
    sha256: 20ae0f3364428b712869276c75fa81c20104061316a8239a4f975cac6a8eab38
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: Full independent assessment of one maintained pathway target and every
    local node, edge and reference.
  selection: Exact assigned data/pathways/riboneogenesis.yaml, PathBank:SMP0002406.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PathBank:SMP0002406
  exclusions:
  - target: All other pathway records including methylglyoxal-degradation-iii.yaml
    reason: Separate authorship/reviews; shared corpus gates do not constitute scientific
      assessment of other records.
  - target: Uninspected supplementary PDF and other uninspected literature
    reason: No claims of full supplementary access or exhaustive literature coverage.
targets:
- target_id: PathBank:SMP0002406
  path: data/pathways/riboneogenesis.yaml
  label: Riboneogenesis
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/riboneogenesis.yaml
    role: maintained_curation
checks:
- check_id: c-inspect
  name: Initial governed inspection
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Terminal exit 0, session 2292; target and initial source inputs captured
    before assessment.
  evidence_ids:
  - e-record
  - e-correction
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-riboneogenesis-independent-review/targets.yaml
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
    --input docs/CAUSAL_GRAPHS.md --input research/pathway_additions/2026-10-10-next/riboneogenesis-identifiers.json
    --input research/pathway_additions/2026-10-10-next/riboneogenesis-validation.json
  exit_code: 0
  expected_exit_code: 0
- check_id: c-replay-initial
  name: Initial scratch native-object parser
  status: failed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Non-gating initial replay incorrectly keyed BioPAX objects only by rdf:about,
    omitting rdf:ID; failed native count assertion. Reviewer corrected scratch parser;
    no target change resulted.
  evidence_ids:
  - e-replay
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    /private/tmp/pathwaymech-riboneogenesis-independent-review/replay.py
  exit_code: 1
  expected_exit_code: 0
- check_id: c-replay
  name: Independent source and chemistry replay
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: 'Terminal exit 0, session 40737: all 19 chemical edges/locators, six balances/directions,
    participant/reaction/taxon labels, 15 reference digests and 22 raw-body hashes
    match final target.'
  evidence_ids:
  - e-replay
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    /private/tmp/pathwaymech-riboneogenesis-independent-review/replay.py
  exit_code: 0
  expected_exit_code: 0
- check_id: c-integration-initial
  name: Initial scratch manifest shape probe
  status: failed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Non-gating initial integration helper assumed mapping for the manifest
    list; exited 1. Corrected scratch helper; no repository change resulted.
  evidence_ids:
  - e-authority
  command: .venv/bin/python /private/tmp/pathwaymech-riboneogenesis-independent-review/integration.py
  exit_code: 1
  expected_exit_code: 0
- check_id: c-integration
  name: Independent baseline authority retention
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: All 110 prior manifest entries, 1319 prior ontology terms/4 metadata rows
    and 1622 source terms/102 metadata rows remain exactly equal.
  evidence_ids:
  - e-authority
  command: .venv/bin/python /private/tmp/pathwaymech-riboneogenesis-independent-review/integration.py
  exit_code: 0
  expected_exit_code: 0
- check_id: c-diff
  name: Final working-tree and staged whitespace checks
  status: passed
  required: true
  target_ids:
  - PathBank:SMP0002406
  summary: Both reviewer-executed checks exited 0 after final source and generated-input
    inspection.
  evidence_ids:
  - e-record
  command: git diff --check; git diff --cached --check
  exit_code: 0
  expected_exit_code: 0
- check_id: c-prior
  name: Ignored-inclusive prior review search
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Search returned no exact prior target occurrence; wrapper accepts ordinary
    rg no-match exit 1 and itself returned 0.
  evidence_ids:
  - e-prior
  command: rg -n -uu 'PathBank:SMP0002406|riboneogenesis|Riboneogenesis' reviews reports
    > /private/tmp/pathwaymech-riboneogenesis-independent-review/prior-reviews.txt;
    code=$?; test "$code" = 0 -o "$code" = 1
  exit_code: 0
  expected_exit_code: 0
- check_id: c-final-inspect
  name: Final governed changed-input capture
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Terminal exit0, session62556; changed target, receipts, authority snapshots
    and generated page re-inspected after source reassessment.
  evidence_ids:
  - e-record
  - e-correction
  - e-generated
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-riboneogenesis-independent-review/targets.yaml
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
    --input docs/CAUSAL_GRAPHS.md --input conf/identifier_policy.yaml --input conf/identifier_sources.json
    --input data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input research/pathway_additions/2026-10-10-next/riboneogenesis-identifiers.json
    --input research/pathway_additions/2026-10-10-next/riboneogenesis-validation.json
    --input research/pathway_additions/2026-10-10-next/riboneogenesis-curation.md
    --input research/pathway_additions/2026-10-10-next/riboneogenesis-source-manifest.json
    --input research/pathway_additions/2026-10-10-next/riboneogenesis-source-projection.json
    --input research/pathway_additions/2026-10-10-next/riboneogenesis-imodulondb-context.json
    --input research/pathway_additions/2026-10-10-next/authority-integration.json
    --input research/pathway_additions/2026-10-10-next/generated-graph-kgx-audit.json
    --input pages/records/PathBank_SMP0002406.html
  exit_code: 0
  expected_exit_code: 0
- check_id: c-correction
  name: Exact three-field issue326 correction
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Reviewer reconstructed the original target bytes by reverting only the
    three corrected direction fields; resulting SHA256 exactly equals initial governed
    SHA. All other bytes were unchanged.
  evidence_ids:
  - e-correction
  command: python3 reviewer scratch reconstruction of direction fields27628,13679,14659
    and SHA256 assertion
  exit_code: 0
  expected_exit_code: 0
- check_id: c-generated-recheck
  name: Generated artifact hash and direction recheck
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Reviewer rehashed both separately generated KGX files, confirmed all three
    corrected target source contexts are right_to_left, and rehashed generated page
    to audit receipt.
  evidence_ids:
  - e-generated
  - e-correction
  command: python3 reviewer CSV/JSON/SHA256 check of /private/tmp/pathwaymech-next-kgx
    and pages/records/PathBank_SMP0002406.html
  exit_code: 0
  expected_exit_code: 0
- check_id: c-test-before-render
  name: Initial full-test run overlapping rendering
  status: failed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Actual root run exited1:1042 passed,1 failed,3 skipped. Sole failure was
    test_cross_mech.test_rendered_site_publishes_the_index_and_it_is_current because
    the suite started before rendering completed. This is retained as superseded pre-freeze
    check history; required final full suite is separately recorded below. Log /private/tmp/pathwaymech-next-test-before-render.log;
    SHA256 e51aee5e56ba1f61427b0093f60d1b04799e0e3e0a58f1fa33d17d3ee6372e3f.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 1
  expected_exit_code: 0
  scope_note: Delegated initial root run, not the final frozen-input gate. No scientific
    target change resulted; complete suite rerun on final generated pages.
- check_id: c-review-draft-format
  name: Initial completed-draft serialization check
  status: failed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: 'Two initial governed draft validations exited1: first PyYAML aliases,
    then the unsupported evidence kind record. Reviewer disabled aliases and used
    governed record_content. Scientific content and repository inputs did not change.'
  evidence_ids:
  - e-record
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py validate /private/tmp/pathwaymech-riboneogenesis-independent-review/completed-review.yaml
  exit_code: 1
  expected_exit_code: 0
- check_id: c-validate
  name: Integrated validation
  status: passed
  required: true
  target_ids:
  - PathBank:SMP0002406
  summary: Terminal exit0 session12091:169 native/closed-schema records,251 histories,8834
    evidence blocks,30 sources, exact identifiers,6 documentation files,research contract
    and169 current pages pass.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on the frozen target; reviewer inspected
    actual final log and terminal outcome. Full corpus gates were not duplicated and
    are not a scientific review of other records.
- check_id: c-lint
  name: Integrated lint
  status: passed
  required: true
  target_ids:
  - PathBank:SMP0002406
  summary: All Ruff checks passed; root confirms terminal exit0.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on the frozen target; reviewer inspected
    actual final log and terminal outcome. Full corpus gates were not duplicated and
    are not a scientific review of other records.
- check_id: c-render
  name: Integrated page rendering
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: Rendered169 records, including final issue326 correction; root confirms
    terminal exit0.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on the frozen target; reviewer inspected
    actual final log and terminal outcome. Full corpus gates were not duplicated and
    are not a scientific review of other records.
- check_id: c-vendored
  name: Governed artifact synchronization
  status: passed
  required: false
  target_ids:
  - PathBank:SMP0002406
  summary: All22 governed artifacts match pinned CLAW revision; root confirms terminal
    exit0.
  evidence_ids:
  - e-gates
  command: bash scripts/check_vendored_sync.sh
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on the frozen target; reviewer inspected
    actual final log and terminal outcome. Full corpus gates were not duplicated and
    are not a scientific review of other records.
- check_id: c-test
  name: Final integrated test suite
  status: passed
  required: true
  target_ids:
  - PathBank:SMP0002406
  summary: Final frozen-input rerun, terminal exit0 session88101:1043 passed,3 skipped,3
    upstream warnings in242.23 seconds. Supersedes the separately retained initial
    pre-render run.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on the frozen target; reviewer inspected
    actual final log and terminal outcome. Full corpus gates were not duplicated and
    are not a scientific review of other records.
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/riboneogenesis.yaml
  locator: Complete target, 26 participants, 6 reactions, 50 edges, 78 evidence blocks
    and 15 references
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: Full target read before assessment; final corrected content re-read. The
    independent reviewer did not author or edit this target.
  snapshot_sha256: d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96
- evidence_id: e-native
  kind: database
  reference: https://pathbank.org/pathways/SMP0002406
  locator: PW002511.owl Pathway, Species/18, six Reactions/7089-7094, Catalysis7068-7072,
    ProteinComplex/4403 and exact entity references
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: The native source identifies yeast Riboneogenesis and six steps. Five native
    steps are reversible; Shb17 hydrolysis is left-to-right. ProteinComplex/4403 mixes
    Tkl1 and Tkl2 and is correctly rejected as an unsupported physical heteromer.
    Native furanose ribose, unspecified GAP, and phosphate charge forms are not asserted
    to be exact matches to the Rhea representation.
  snapshot_sha256: 1f8af4af7f79034296739e1f0ef313974de23119528c4401c3f8b41f46594c2e
- evidence_id: e-rhea
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Rhea142 masters27626/30167/17461/10508/13677/14657; directed27628/30168/17462/10509/13679/14659;
    substrates/products, contains1, Participant/compound/accession; official direction
    TSV
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: Independent full-RDF replay verifies all 19 chemical side assertions and
    exact locators; all coefficients1 and all six equations balance by elements and
    charge. Directed selection matches riboneogenic chemistry. The three reverse-to-master
    direction fields now agree with the official TSV.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3163394/
  locator: PMID21663798; complete main article Introduction, equations1-5, Results/Figures3-6,
    Discussion and Experimental Procedures
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: Inspected main HTML/text supports the Shb17-driven route, purified SBP
    hydrolysis, FBA1-DAmP labeling perturbation, Tkl1/Tkl2 roles, Rpe1/Rki1 pentose
    interconversion, experimental strain scope and Shb17 dimer structure. Main text
    calls Mg optional/metal-independent; no obligate Mg edge is warranted. Crystal
    beta-furanose SBP differs from Rhea formal open-chain form and this is explicit.
  snapshot_sha256: 831fcc40f7344b7e0a68164e48e7e131183ba8743d3e86d30a5f15c3d5ba0278
- evidence_id: e-pentose-primary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/8929392/
  locator: Complete indexed abstract preserved in EuropePMC core JSON; RPE1 deletion
    and RKI1 dosage-restoration sentences
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: The abstract supports loss of RPE1 enzyme activity and RKI1 restoration
    of viability and specific ketol-isomerase activity. Two short target quotations
    are literal. Full article was not inspected; no detailed assay or assembly claim
    is attributed to it.
  snapshot_sha256: 09f27448fa755c6e8d9f2b224c172f2925568ab558e3f5d907dfe7578a6d1e28
- evidence_id: e-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P23254.json
  locator: 'Reviewed 2026_03 JSON P23254,P33315,P14540,P36136,P46969,Q12189: primary
    accession, organism559292, recommended name, catalytic/subunit/cofactor/subcellular
    comments and inline ECO codes'
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: All six gene products match. Tkl1 has experimental annotations; Tkl2 catalysis/assembly/cofactors
    remain by similarity. Fba1 current catalytic comment concerns FBP and its homodimer
    lacks inline code, while primary in-vivo evidence anchors SBP formation. Shb17
    hydrolysis/dimer are experimental. Rpe1 catalytic/cofactor similarity and Rki1
    ECO0000305 inference are correctly distinguished from the separate 1996 functional
    experiments. No missing SUBUNIT statement is treated as monomer proof.
- evidence_id: e-cofactor
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P46969.json
  locator: Tkl1/Tkl2 comments[2-3], Fba1 cofactor comment, Rpe1 Co/Fe/Mn/Zn annotations;
    Shb17 subcellular location comment
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: All 15 cofactor edges reproduce exact current annotations and evidence
    grades. Alternative metals are not simultaneous requirements. Both Shb17 localization
    statements are protein-specific, nonexclusive cytoplasm/nucleus annotations, not
    whole-pathway localization. The cited localization primary was not independently
    inspected.
- evidence_id: e-replay
  kind: validation
  reference: /private/tmp/pathwaymech-riboneogenesis-independent-review/replay.json
  locator: Independent reviewer full-RDF replay.py, native extraction, source/reference
    hashes, issuing authority labels, quote literals and dataset-output rehash
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: Actual terminal exit0 confirms final SHA d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96,
    all 19 chemical edges and six balances, 15 references, 22 preserved bodies and
    bounded context receipt.
  snapshot_sha256: a6bcc83eef2fe525ecda67687b2abe89caa9922e02f1fc8a7d908601e789f193
- evidence_id: e-authority
  kind: authority
  reference: research/pathway_additions/2026-10-10-next/authority-integration.json
  locator: Final regenerated snapshots and manifest compared independently with git
    base dbf399e6ac90f6240fa5da2fac27386d49966171
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: All original manifest/term/metadata values are retained. Final 121 manifest
    entries, 1331 ontology terms, 1633 source terms. Exact target labels were also
    independently queried from native/issuing sources. Rhea139 pinned label authority
    and explicitly versioned Rhea142 chemistry remain distinguished.
  snapshot_sha256: 76e569ddf2e9ba12dbfa6592036e78938aef8f3fd91ccf8dca9c5b1c6d09d189
- evidence_id: e-context
  kind: database
  reference: research/pathway_additions/2026-10-10-next/riboneogenesis-imodulondb-context.json
  locator: Canonical kg-microbe-sources imodulondb datasets; all 28 inventory rows
    and exact stdout hash
  accessed_at: '2026-10-10T23:43:44Z'
  support: context_only
  summary: Author canonical command returned exit0 after DNS retry. Reviewer inspected/rehashed
    actual output. No Saccharomyces/yeast dataset key is supplied, so search/summarize
    are not applicable. This does not imply absent expression/module membership.
  snapshot_sha256: 351cd9cb22aecc1cd881c994089d36fa08638a39333c6a4f6cb93ee385e3d23c
- evidence_id: e-correction
  kind: validation
  reference: https://github.com/CultureBotAI/PathwayMech/issues/326
  locator: Initial governed target f937afb93da295d6089762a409579244ddc07102b408744af2c9905f2974f746;
    final target d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96;
    reaction direction fields27628,13679,14659
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: Reviewer identified a minor source-direction metadata defect before saving
    a bundle. Integration agent filed issue326 and the author changed exactly three
    fields from left_to_right to right_to_left. Chemical edges/evidence/references
    did not change. Independent TSV/RDF replay verifies the correction. The local
    convention is corroborated by scripts/curate_metacyc_causal_graphs.py mapping
    RHEA_ID_RL to right_to_left.
- evidence_id: e-generated
  kind: validation
  reference: research/pathway_additions/2026-10-10-next/generated-graph-kgx-audit.json
  locator: Final delegated actual CLI KGX and generated SVG/evidence audit
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: Complete target nodes, all 50 edges/78 evidence and reference metadata
    are retained; source-direction fields including issue326 are preserved in generated
    export contexts. This is a programmatic structural assessment, not visual browser
    QA.
  snapshot_sha256: 2b3d20a77b87b26b17e1843e6db9910226afdb93799739400bbb4de57c773af7
- evidence_id: e-gates
  kind: validation
  reference: /private/tmp/pathwaymech-next-{validate,test,test-before-render,lint,render,vendored}.log
  locator: Root-executed final corpus logs and terminal outcomes; exact command environment
    and summaries retained in checks
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: Reviewer inspected final delegated gate logs on frozen inputs and retained
    the superseded initial test failure. Deterministic consistency is separate from
    independent scientific judgement. Gate receipt binds actual final log hashes.
  snapshot_sha256: 70629b32dbca5fffdfc0887cb6d100b0ec3f2643ab422be8fb80b0cb80d9b3c4
- evidence_id: e-prior
  kind: search
  reference: reviews/ and reports/
  locator: rg -n -uu 'PathBank:SMP0002406|riboneogenesis|Riboneogenesis' reviews reports
  accessed_at: '2026-10-10T23:43:44Z'
  support: supports
  summary: No prior exact target review/report match was returned; hidden and ignored
    files were included. This is bounded review-history search, not exhaustive literature
    absence.
  search_scope: All reviews/ and reports/ in the active worktree, hidden and ignored
    files included.
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact route and yeast scope
  outcome: supported
  summary: Native PathBank identity and primary experiments support a distinct SBP/Shb17
    pathway, not the ordinary transaldolase branch or a generic ribose biosynthesis
    process. BY4743-derived mutant/FY4/FY5 primary scope and S288c protein identity
    are preserved; species placement does not claim universal strain flux.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-native
  - e-primary
  - e-proteins
- assessment_id: a-chemistry
  area: grounding
  topic: 'Edges001-019: exact directed chemistry'
  outcome: supported
  summary: All selected Rhea substrates/products, formal charges and coefficients
    agree with the inspected native RDF and issuing identities. Six equations balance.
    Source charge/tautomer differences are explicit manual route correspondences,
    not exactMatch assertions or invented sugar-isomerization enzymes.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-rhea
  - e-native
  - e-replay
  - e-primary
- assessment_id: a-enzymes
  area: evidence
  topic: 'Edges020-027: supported gene-product functions'
  outcome: supported
  summary: All eight enables assignments have scoped primary/native/reviewed support.
    Tkl2 similarity, Fba1 in-vivo perturbation versus current FBP-specific comment,
    Rpe1 similarity and Rki1 curator inference are explicit. Gene-product enables
    describes supported function without asserting isolated-monomer catalysis.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-proteins
  - e-primary
  - e-pentose-primary
- assessment_id: a-assembly
  area: representation
  topic: Physical assembly boundary
  outcome: supported
  summary: Unsupported native Tkl1/Tkl2 mixed complex is excluded. Current Tkl1 homodimer
    and similarity-supported Tkl2 homodimer, Fba1 homodimer and Shb17 dimer contexts
    are stated without invented physical assembly IDs. No absence of a SUBUNIT comment
    is promoted to monomer evidence.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-native
  - e-proteins
  - e-primary
- assessment_id: a-membership
  area: graph
  topic: 'Edges028-033: exact six-step membership'
  outcome: supported
  summary: All six native reaction IDs are pathway members. The manual correspondence
    uses independent Rhea chemistry and primary equations1-5/Figure6E. Native reversible
    reactions remain noted while the curated graph selects riboneogenic direction.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-native
  - e-rhea
  - e-primary
  - e-replay
- assessment_id: a-cofactors
  area: evidence
  topic: 'Edges034-048: cofactor scope'
  outcome: supported
  summary: All fifteen exact metal/ThDP assignments match native reviewed comments
    and retain experimental versus similarity evidence. Alternative metals are not
    all required at once. Shb17 possible Mg crystal density and optional coordination
    are correctly not made an obligate cofactor edge.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-cofactor
  - e-primary
  - e-proteins
- assessment_id: a-location
  area: scope
  topic: 'Edges049-050: protein localization'
  outcome: supported
  summary: Both cytoplasm and nucleus edges are nonexclusive Shb17 annotations with
    source attribution. Neither locates the entire route or supplies independent primary
    localization verification.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-cofactor
  - e-proteins
- assessment_id: a-direction-correction
  area: provenance
  topic: Resolved pre-save minor issue326
  outcome: supported
  summary: Original target metadata disagreed with the established Rhea master-direction
    convention for three reactions. The author corrected only those fields after issue326
    was filed. Reassessment confirms exact directions and unchanged chemistry/evidence.
    No correction remains open in the final target. The original finding is retained
    here because no defective interim structured bundle was saved.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-correction
  - e-rhea
  - e-replay
  - e-generated
- assessment_id: a-limits
  area: completeness
  topic: Bounded primary access and evidence tiers
  outcome: unknown
  summary: Primary2011 main article was inspected fully, but its supplement was unavailable
    as a PDF. PMID8929392 was abstract-only. Similarity-derived protein/cofactor assignments
    and curated localization remain clearly distinguished from direct primary proof.
    No new quantitative universal-flux claim is made.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-primary
  - e-pentose-primary
  - e-proteins
  - e-context
- assessment_id: a-publication
  area: graph
  topic: Final source and generated evidence integrity
  outcome: supported
  summary: Final source identities, input hashes, scoped adapter context, generated
    graph evidence and required repository gates support a qualified pass. These checks
    do not imply a fresh scientific review of other records.
  target_ids:
  - PathBank:SMP0002406
  evidence_ids:
  - e-record
  - e-replay
  - e-authority
  - e-generated
  - e-gates
findings: []
actions: []
limitations:
- PMID21663798 complete main HTML was read; the supplementary PDF endpoint returned
  HTML challenge data and no supplement-specific claim is verified. Browser recaptcha
  responses were not treated as article access.
- PMID8929392 was inspected as its complete indexed abstract, not the full paper.
  Other database-cited experimental publications are not represented as independently
  read full articles.
- Tkl2/Rpe1 and some cofactor assignments retain reviewed similarity evidence; Rki1
  catalytic annotation retains curator inference. Reviewed localization is not independently
  inspected primary localization evidence.
- Formal Rhea sugar charge/tautomer identities differ from some PathBank native species
  and Shb17 bound beta-furanose structure. The target preserves route-level correspondence
  without unsupported exactMatch assertions.
- No verified physical homodimer source accession was used. Gene-product enables edges
  express function and preserve assembly context; no isolated-monomer catalysis is
  asserted.
- iModulonDB supplies no applicable yeast dataset in the current 28-row inventory;
  this coverage limit is not negative expression or mechanism evidence.
- Programmatic SVG/KGX verification is not browser visual QA. Required full-corpus
  gates were delegated and their actual logs/outcomes inspected.
notes:
- 'Generated page owner: data/pathways/riboneogenesis.yaml, src/pathwaymech/cli.py
  and src/pathwaymech/graph_view.py via just render-pages. Generated authority snapshots
  are owned by conf/identifier_sources.json, conf/identifier_policy.yaml and independently
  pinned issuing-source inputs; any future correction belongs in those maintained
  inputs and their generator.'
- Initial governed target SHA f937afb93da295d6089762a409579244ddc07102b408744af2c9905f2974f746
  was superseded by d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96
  after exactly three source-direction corrections. The affected fields, owner, issue,
  old/new hashes and successful acceptance replay are retained in this review; there
  is no prior structured finding occurrence to fabricate.
- Final changed identifiers/validation receipts, regenerated authority snapshots and
  generated page were re-read and re-inspected before save.
- Two non-gating scratch harness failures are retained as actual checks; both were
  corrected in scratch and superseded by successful independent replay.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/326
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3163394/
- https://pubmed.ncbi.nlm.nih.gov/8929392/
tags:
- riboneogenesis
- independent-scientific-review
- rhea
- pathbank
- issue326
```
