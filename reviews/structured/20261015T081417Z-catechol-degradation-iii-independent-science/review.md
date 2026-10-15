# Independent scientific review of catechol degradation III

- Review: 20261015T081417Z-catechol-degradation-iii-independent-science
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-15T07:10:36.185084Z
- Finished UTC: 2026-10-15T08:14:17.631404Z
- Reviewer: Codex /root/next263_chemistry_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact b30573a… record is scientifically supported within its stated source and preparation scope. All 117 edges, 123 named identifiers and 211 references were assessed. Issues 567–570 were corrected and independently reassessed during review; finite source limitations and the catA adapter failure remain transparently recorded. Required repository gates and production graph/export checks passed.

## Scope And Provenance

One complete maintained catechol degradation III record, all assertions, all local identifiers/references, source-to-graph and graph-to-source scope, plus exact generated owner checks.

Selection: Exact target data/pathways/catechol-degradation-iii.yaml, MetaCyc:PWY-5417; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 46ee133770039e8b21d1563166dec50eecd2c411.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5417 | data/pathways/catechol-degradation-iii.yaml | maintained | catechol degradation III (ortho-cleavage pathway) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical exact target inspection and successor reinspection | passed | True | MetaCyc:PWY-5417 | Actual inspect ran before assessment on 0ad615… and separately on 67ef6…, 886b188… and final b305…; reviewed semantic deltas are retained. Final complete inspection binds production evidence and maintained owners. |
| just render-pages | passed | False | MetaCyc:PWY-5417 | The initial full repository render completed with exit 0. Its exact generated page and downloads remain unchanged; the only later source-storage change was the verified lossless ADIPATE relocation, with proof additions and bounded report documentation changes. |
| just validate | passed | True | MetaCyc:PWY-5417 | The initial full repository validation completed with exit 0. Carry-forward is supported by the exact input inventory and the reviewed lossless storage and proof/documentation deltas; maintained scientific, schema and code inputs remain unchanged. |
| just test | passed | True | MetaCyc:PWY-5417 | The complete suite was rerun in the separate verified frozen-lock environment: 5255 passed, 3 skipped and 7 warnings in 793.34 seconds. The command exited 0; the initial failed attempt remains separately reported. |
| just lint | passed | True | MetaCyc:PWY-5417 | Parent-executed command completed with exit 0; retained receipt and raw log bind its actual full-corpus scope. |
| just vendored-check | passed | False | MetaCyc:PWY-5417 | Parent-executed command completed with exit 0; retained receipt and raw log bind its actual full-corpus scope. |
| git diff --check | passed | True | MetaCyc:PWY-5417 | Parent-executed command completed with exit 0; retained receipt and raw log bind its actual full-corpus scope. |
| git diff --cached --check | passed | False | MetaCyc:PWY-5417 | Parent-executed command completed with exit 0; retained receipt and raw log bind its actual full-corpus scope. |
| Independent chemical reconstruction | passed | True | MetaCyc:PWY-5417 | Thirteen formal chemicals, eight supplemental context entities and two additional endpoints were independently assessed using exact issuing/native originals. RDKit 2026.03.5 used supported RDBASE; source-author release differences produced no identity discrepancy. |
| Original-source protein and preparation review | passed | True | MetaCyc:PWY-5417 | Deposited CDS translations, current/deleted UniProt records, six PDB assemblies, high-risk primary conflicts and remaining paper families assessed independently. |
| Native locator and reference replay | passed | True | MetaCyc:PWY-5417 | Native slot/XPath completeness, graph endpoints, material coefficients, Rhea LR/RL side metadata and reference digest owners passed with explicit limits. |
| Structured iModulonDB cross-check | passed | True | MetaCyc:PWY-5417 | Dataset discovery, pca search and module 65 summary passed. The catA adapter returned exit 2 for a null regulator; the exact raw API fallback was retained and inspected. E. coli paaJ was a gene hit without a module. The absence of a matching Cupriavidus dataset is not negative pathway evidence. |
| Generated graph and KGX scope | passed | True | MetaCyc:PWY-5417 | Rendered graph and export preserve direction, qualifiers, edge-specific evidence and narrow preparation scope; completed production bindings inspected. |
| Original catA adapter attempt | failed | False | MetaCyc:PWY-5417 | Retained actual exit 2: a returned imodulon regulator was null rather than a list. This attempt is not reported as a pass; the raw API fallback supports the bounded context assessment. |
| Initial full-test attempt with disrupted shared environment | failed | False | MetaCyc:PWY-5417 | The initial full test run ended with 102 failed, 4975 passed, 3 skipped and 178 errors after files disappeared from the shared environment. The deletion actor is unknown. Two initial traces do not establish an exact cause; later full-suite success does not erase these observations. A separate frozen-lock environment completed all 5255 tests successfully, with 3 skipped and 7 warnings. |

## Scientific And Domain Assessments

### Exact catechol degradation III route

identity: supported. Targets: MetaCyc:PWY-5417.

PWY-5417 denotes the six-step ortho-cleavage route through stereospecific muconolactone and 3-oxoadipate to succinate and acetyl-CoA. Child modules, adjacent chlorinated activities and donor organisms remain separate.

### Whole equations, directions and net cancellation

quantity: supported. Targets: MetaCyc:PWY-5417.

All six whole equations and 21 material entries are supported. Cycloisomerase and thiolase Rhea nodes use issuing RL orientation; formatted forward equations are not contradictory. Succinyl-CoA cancels across the transferase/thiolase pair.

The fixed whole-Rhea scan covers 37068 equations and excludes 154 symbolic cases. Native incomplete SMILES and broader KEGG stereochemistry are explicit limits; formal identity does not assert historical substrate purity. The net route is catechol + O2 + H2O + CoA(4−) → succinate(2−) + acetyl-CoA(4−) + 2 H+. The succinyl-CoA carrier cancels between the transferase and thiolase steps.

### Bidirectional source coverage and all 117 edges

completeness: supported. Targets: MetaCyc:PWY-5417.

The complete finite record and source closure are assessed, including 20 formal enzyme/activity assignments, two adjacent activities, complex components, cofactors, regulation, five joins and five predecessor relations. No material finite-scope omission remains after n100 evidence strengthening.

### Organisms, proteins, assemblies and historical preparations

scope: supported. Targets: MetaCyc:PWY-5417.

Nine grounded parent taxa preserve 11 native organism rows and two ungrounded strain contexts. Native parent annotation is not all-step experimental evidence. Historical PRS/C1/MT1 preparations, current KT2440 accessions, H16 loci, engineered hosts and PDB variants remain distinct.

### Evidence placement and endpoint qualifiers

evidence: supported. Targets: MetaCyc:PWY-5417.

Native database assertions remain separate from paper excerpts. MT1 purity, metal-free CcaC, PcaR expression versus recombinant DNA binding, B13 inhibitor targets and adjacent EDTA activity are attached to the proper edge or endpoint context.

### Native conflicts and retained uncertainty

consistency: supported. Targets: MetaCyc:PWY-5417.

All 18 bounded native conflicts are preserved, corrected or explicitly excluded without upgrading ambiguous source metadata. PcaD historical mass, deleted Q9AEQ0, H16 pcaI/J/F, NaCN/HCN and broad muconolactone forms are not silently equated.

### Within-review corrections and external issues 567–570

provenance: supported. Targets: MetaCyc:PWY-5417.

The current b30573a target and explicit correction notice satisfy issues 567–570: the pcaF benzoate exception, Results prose locator, AY029000 strain-unspecified deposit and EDTA charge wording. The observed defects and fixes occurred within this review before its first canonical save; no canonical predecessor or previous_occurrences is invented.

### Selected issuing identifiers and reference provenance

grounding: supported. Targets: MetaCyc:PWY-5417.

All 123 named identifiers have exact selected authority ownership; all 211 references have declared complete-file or explicitly stated whole-database digest scope. Twenty-three chemical endpoints and protein/genome/PDB identities are independently distinguished from preparation equivalence.

### Computational expression context

evidence: supported. Targets: MetaCyc:PWY-5417.

PcaR module 65 membership for current KT2440 pca genes supports bounded expression context only. The adapter failure is retained with raw fallback. No membership, absence or broad substring hit is treated as catalytic or pathway proof.

### Generated graph, exports and repository gates

representation: supported. Targets: MetaCyc:PWY-5417.

Required full-corpus checks and exact production outputs passed. SVG and KGX retain authored direction, descriptions, evidence and endpoint qualification. Generated owners remain the maintained YAML and existing render/export implementation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| chemical-equations | research/pathway_additions/2026-10-14-next-263/independent-chemistry/adjudication.json.gz; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Independent original-source reconstruction supports thirteen formal chemical identities, six whole equations, twenty-one material roles, five joins and net carrier cancellation. Separate native and issuing structures retain stereochemistry, charge and protonation limits. |
| biological-preparation | research/pathway_additions/2026-10-14-next-263/independent-science-source-preparation/independent/source-preparation-adjudication.json.gz; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Independent complete-source and visual-page preparation assesses B13 inhibitor target conflicts, MT1 enzyme purity, H16 gene identity, historical PcaD, deleted CatA pointer, deposited sequences, PDB assemblies and PcaR expression/binding scope. |
| remaining-primary-papers | research/pathway_additions/2026-10-14-next-263/independent-scientific-review/primary-edge-audit/independent/adjudication.json; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | An independent delegated reviewer read the remaining finite primary families, visually inspected critical tables, identified the AY029000 strain-scope defect and rechecked its correction. Access and preparation limits remain explicit. |
| all-edge-adjudication | research/pathway_additions/2026-10-14-next-263/independent-scientific-review/final-scientific-adjudication.json; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Independent final assessment assigns all 117 edges to sixteen evidence-specific groups and reviews source-to-graph omissions, identifier/preparation scope, taxonomy and evidence placement. |
| within-review-corrections | research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/initial-findings-and-reassessments.json; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Exact initial observations and successor reassessments preserve issues 567–570 without fabricating an earlier canonical review. Current target has no remaining supported defect from those observations. |
| formal-graph-replay | research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/final-graph-reference-replay.json.gz; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Actual maintained graph matches six independently reconstructed equations, twenty-one coefficients and five joins; all 211 reference digests are bound. Later reviewed changes leave these triples, identifiers, chemical structures and digest ownership unchanged. |
| source-authority-replay | research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/source-coverage-authority-replay.json.gz; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Fresh replay resolves all 3252 retained native slot locators, 22 native enzyme/activity links including two adjacent activities, 11 organism objects, 48 PMID bibliographic identities and 123 selected authority owners. Counts do not substitute for scientific assessment. |
| two-context-chemicals | research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/context-chemistry-independent.json; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Independent CML, formula, charge and full InChI/key checks accept CHEBI:16810 and CHEBI:17128; fresh read-only SQL retrieves all 41 and 29 subject rows. Exact recent whole-database hash receipt is reused transparently after stat verification. |
| imodulon-context | research/pathway_additions/2026-10-14-next-263/independent-science-source-preparation/independent/imodulondb/pcaR-65-raw.json.gz; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | context_only | Pseudomonas putida precise321 PcaR module 65 contains the relevant current KT2440 genes; module membership remains computational expression context only. The retained preparation includes datasets/search/summarize, a null-regulator adapter failure and exact raw-source fallback. |
| frozen-summary-notice | research/pathway_additions/2026-10-14-next-263/source-evidence/primary/CORRECTIONS.md; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Explicit source-bound notice supersedes incorrect frozen P263-C48 pcaF repression and P263-C43 Table 1 locator while retaining immutable originals. |
| initial-failed-production | research/pathway_additions/2026-10-14-next-263/verification/full-gates/initial/receipts.json; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | context_only | Failed initial production attempt preserved after files disappeared from the shared environment; the deletion actor remains unknown; successor gates use a separately verified isolated environment. |
| production-gates | research/pathway_additions/2026-10-14-next-263/verification/full-gates/successful-receipts.json; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Actual parent-executed full production commands, exit codes, raw logs and exact tested inputs were independently inspected. All seven successful log digests and decoded retained logs match their originals. The 2972 initial inputs, 3178 recovered inputs and nine critical runtime files were rechecked with explicit storage/documentation deltas. These checks establish deterministic validation, not scientific truth. |
| generated-scope | research/pathway_additions/2026-10-14-next-263/independent-scientific-review/generated-verification/generated-scientific-scope.json.gz; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | Independent SVG semantic inspection maps all 117 graph edges to authored triples, complete descriptions and preparation-qualified endpoints; 129 display nodes include 15 qualified contexts. |
| browser | research/pathway_additions/2026-10-14-next-263/verification/browser/browser-cdp-result.json; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | The parent performed live browser interactions and retained exact page and screenshot bindings. This reviewer independently viewed both exact screenshots: controls, legend and graph render on desktop and mobile; fitted labels are dense and require zoom or node selection. This is not a claim that this reviewer repeated live browser interactions. |
| kgx | research/pathway_additions/2026-10-14-next-263/verification/kgx-export-receipt.json; Complete retained file; original and stored SHA-256 bindings in owning retention manifest. | supports | The actual production CLI export completed successfully and its complete node/edge TSV bytes equal the tracked page downloads. Independent scientific payload checks preserved all 117 target edge triples, descriptions, reference metadata and endpoint qualifiers, including the issuing Rhea RL direction metadata. |

## Limits And Additional Notes

- Some primary evidence is abstract-only, partial article reproduction or historical scan material. Each access boundary remains declared; unreadable miniprint methods are not reconstructed.
- Modern protein sequence and assembly annotation does not retrospectively prove a historical preparation identity. The deleted CatA pointer, unqualified AY029000 strain and historical PcaD discrepancies remain bounded uncertainties.
- Formal chemical identities preserve exact structure/charge/stereochemistry; they do not measure assay solution speciation, salt identity or historical enantiomeric purity.
- Whole-Rhea equality is limited to the 37068 fixed equations tested; 154 symbolic equations were excluded. No broader provider equivalence is claimed.
- iModulonDB evidence is computational expression context. The catA adapter failed on a null regulator; an exact retained raw API fallback was inspected.
- A clean final observation does not erase immutable source-author defects or initial review findings. Their exact observations, fixes and external issues are retained without invented canonical lineage.
- At the fitted full-graph scale, labels are dense on both desktop and mobile. The verified zoom and node picker provide readable selected contexts.
- Scientific source evidence frozen before production gates remains immutable and explicitly labels its then-pending gate status. This complete review additionally binds actual later gate and generated-output receipts.
- Helpers preserve real failed parser/check attempts and corrected bounded reruns; those implementation errors are not relabeled as scientific source failures.
- All completeness/absence inventories explicitly include ignored and hidden files where applicable.
- This content was prepared and validated externally by the independent reviewer. The parent performs the canonical immutable save and consumer check; preparation alone is not saved-review persistence.
- Successful initial render and validation are carried forward through exact input accounting. A separately isolated full-suite rerun passed after the shared environment lost files. The deletion actor and the exact causes of two initial traces remain unknown. The later success does not erase the preserved failures.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T081417Z-catechol-degradation-iii-independent-science
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of catechol degradation III
started_at: '2026-10-15T07:10:36.185084Z'
finished_at: '2026-10-15T08:14:17.631404Z'
reviewer:
  identity: Codex /root/next263_chemistry_review
  kind: agent
  independence: independent
  independence_basis: Did not author native, primary, identity, additional chemistry,
    authority or maintained record packages. Independently reconstructed chemical
    identities/equations, read high-risk originals, delegated a bounded independent
    primary audit, and reviewed root-authored fixes against exact successors. No maintained
    curation or GitHub mutations performed by this reviewer.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: No remaining supported scientific defect in exact final maintained
  record; source-access and preparation limits remain explicit.
scientific_review: true
summary: The exact b30573a… record is scientifically supported within its stated source
  and preparation scope. All 117 edges, 123 named identifiers and 211 references were
  assessed. Issues 567–570 were corrected and independently reassessed during review;
  finite source limitations and the catA adapter failure remain transparently recorded.
  Required repository gates and production graph/export checks passed.
source:
  git_revision: 46ee133770039e8b21d1563166dec50eecd2c411
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: f0d394f29cad1a1cd6a004abceb5f59f8e567d6b885cd6c4ff07c629c4d6db7a
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: CLAUDE.md
    sha256: c067d99547f9e9e9a6edb892d71126b6765239348d0021b907f3102907a4cf00
    role: context
  - path: conf/identifier_policy.yaml
    sha256: f57137cbec6ee2ffb4abc1c2e448dd93766e37edac9b07c43cab24c5809d27f7
    role: context
  - path: conf/identifier_sources.json
    sha256: b3979ee6641278a92ccb019285ab64f8b4571248a28937aa7f297828df536040
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 9e717a5bf9831965b4610ae4e66190fc5db141e154a70d5c26f1cdbebc3e2cdd
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 977b581923eecc5b372a04cbf41337ccc7f11899199485cffc5791704497769a
    role: context
  - path: data/pathways/catechol-degradation-iii.yaml
    sha256: b30573a380b358a9b0228f8e3e2689943ecf828aa01ae790f281ba3fe617e603
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 072884773d626ea909bd1e4f275901f0a6053f660d5e68a294ee54149b6496b0
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: pages/downloads/edges.tsv
    sha256: 30c786eb86937624d60d1c96b3be0e3b4cf32407e0b417c01973df6a2ef77618
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: e432e03377e33acf3fd27c92f5fc77f55e2ac738b62d18e5fe87b5a057ac5934
    role: context
  - path: pages/records/MetaCyc_PWY-5417.html
    sha256: 96321f5174aebebfa93df9ad01cc565540a90f754dd17b9745e47a7d1b322c6e
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/README.md
    sha256: 812bc1058b441e9bd67870108a3450654b60e7256f5f7dd4a2e0e5db076ab9f6
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-chemistry/adjudication.json.gz
    sha256: 245bb67c56305c357204cc1aed47dbf97a1aa30dcb0270481f7c1354cdbbe944
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-science-source-preparation/independent/imodulondb/pcaR-65-raw.json.gz
    sha256: ec719cc8cb6610f96dc9db358ffb685e475780d139e29b8deb8a46ba0a230045
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-science-source-preparation/independent/source-preparation-adjudication.json.gz
    sha256: 136fe81e2034c799cbabd25da6c01bef574cca036b890b7fa320533a60febf7c
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/artifact-manifest.json
    sha256: 303e29b55f5bd96e4dc541a591a25ba55dd0ed8ccb87eb581b5f06c24a642358
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/context-chemistry-independent.json
    sha256: 55cdd056047cac41cecd9f6bb62bb301c4bef6becc0786e3f55e7496cdee0e85
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/final-graph-reference-replay.json.gz
    sha256: d8bf30e655f867aae41db01d58646fd4f15861196ae052611e024d35d58206cb
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/initial-findings-and-reassessments.json
    sha256: 2d8fb573a193c27eb7b4040838787081438058f13b8cf4e9147fdb0055239279
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/source-coverage-authority-replay.json.gz
    sha256: d3e64eebb657830b65c93db79ca16d8d4039157be7915461685afc4a992b8b86
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/final-scientific-adjudication.json
    sha256: 6c301c320358fbe597baeec7c4dfcee500bee4da6c0029175e5b76d24d4ea470
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/generated-verification/artifact-manifest.json
    sha256: 696d489ee7b418ec3e9572b035a32f4d88ef097e6f765213a0438a960650cf72
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/generated-verification/generated-scientific-scope.json.gz
    sha256: 91e3d286467c700d8c4573cf98646cb794c2c221854007739dc4dd1321c1ca6a
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/generated-verification/kgx-scientific-scope.json.gz
    sha256: 6a38dd82a9dbdd7b231236603b842da334a71a09f6275811cf47c0b33fb998b5
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/primary-edge-audit/independent/adjudication.json
    sha256: 7bb2fd3c8d57a5adb5f4106a5b30b854aebc4f06648e163af4a99f8ed3b07221
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/root-verification/context-adipate-storage-successor.json
    sha256: da312c7771fa4a691553a32c6c48573fbc7b9194612310e4a5d5627c5144a5b7
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/root-verification/edta-charge-wording-successor.json
    sha256: ecc12c1ea83bea12ccceeba35c5175724b5e042d81f0108c7e76a2c7bee713b5
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/root-verification/edta-primary-evidence-successor.json
    sha256: a5971b1001e7834639eb9596eabf1102c464f8a29a1673ef19c8d3eab10fc297
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/root-verification/independent-review-retention-promotion.json
    sha256: 8cee17d0a227587c310fb7e5f09135c76b5b4c9ae5cbfe15480dd9d27e9c96c3
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/root-verification/issue-568-reference-metadata-correction.json
    sha256: a8f8cafdc08a4ba0cda89a2716454d8dbf0bf62d94d96f4953c47b93764b7007
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/root-verification/issue-569-cata-preparation-correction.json
    sha256: c2e024e5a0ce7ad668a8ebe00e4dea0d5c373735378bb0145f8bfa7330e11217
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/source-evidence/primary/CORRECTIONS.md
    sha256: 0d1aa33c3fb0db085a37f3904010b34b2591e65c99ac429fa1d23531aa446f24
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/verification.md
    sha256: 746c877f07487182fa50965d841e577dbfa59ecdf2e1fe0305d1493fe22202f2
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/verification/browser/browser-cdp-result.json
    sha256: 3c3be36f1255a4f615a3149fc9308bea8055b848ef031dbf4b641aa192e59c46
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/verification/browser/browser-visual-assessment.json
    sha256: 4a86b608dd70ce817ffa15e245f6531c99fef3d2fe59264f216c68fa7f573aa1
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/verification/full-gates/initial/receipts.json
    sha256: cf1ebe5a9feb3ce8f5ad57bb72575403c9896eb28873f47f7863f04e71f380fe
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/verification/full-gates/recovered/final-input-preservation.json
    sha256: 183d4bfb8d02bede185aab0462aaa150d083a4f771ef09cd8882a6673282f413
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/verification/full-gates/successful-receipts.json
    sha256: 3659f01521e474affa1b8fc404e7462316ef54ce654e0a5f0937aad5f653beae
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/verification/kgx-export-receipt.json
    sha256: 7c332768f357925859890b49c863902995570af1e77cedafddbc7c2b9508f547
    role: context
  - path: research/pathway_additions/2026-10-14-next-263/verification/recovery-preparation.json
    sha256: b2d1de33657997c4e4adaca182613f401b6b17d46668b4ebda259e9d67977ec3
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: c66be7d0ae830e5041608eb6b2ce9755c601ed596ec9df5fb3567d41b202478b
    role: context
scope:
  description: One complete maintained catechol degradation III record, all assertions,
    all local identifiers/references, source-to-graph and graph-to-source scope, plus
    exact generated owner checks.
  selection: Exact target data/pathways/catechol-degradation-iii.yaml, MetaCyc:PWY-5417;
    no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5417
  exclusions:
  - target: Other 259 maintained pathway records
    reason: Only corpus-wide deterministic checks and unchanged-input accounting apply;
      no new scientific review of those records.
  - target: Public-release data licensing
    reason: User deferred licensing decisions; scientific review does not authorize
      public redistribution or settle license compatibility.
  - target: Open-ended literature or pathway expansion
    reason: Bounded complete existing-source scope; no speculative expansion beyond
      retained candidate evidence.
targets:
- target_id: MetaCyc:PWY-5417
  path: data/pathways/catechol-degradation-iii.yaml
  label: catechol degradation III (ortho-cleavage pathway)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/catechol-degradation-iii.yaml
    role: maintained pathway record
  ownership_note: The maintained scientific owner is this YAML. The inspected generated
    page and downloads derive from src/pathwaymech/cli.py (render_site), src/pathwaymech/graph_view.py
    (graph_html), src/pathwaymech/site_display.py and src/pathwaymech/kgx.py (render_kgx).
    These implementation inputs were unchanged in the full production input inventories.
    Any future scientific correction belongs in the YAML and must be regenerated through
    these owners.
checks:
- check_id: canonical-inspect
  name: Canonical exact target inspection and successor reinspection
  status: passed
  required: true
  summary: Actual inspect ran before assessment on 0ad615… and separately on 67ef6…,
    886b188… and final b305…; reviewed semantic deltas are retained. Final complete
    inspection binds production evidence and maintained owners.
  target_ids:
  - MetaCyc:PWY-5417
  command: /private/tmp/pathwaymech-next-263-verified-venv/bin/python -B /private/tmp/pathwaymech-next-263-review-completion/run_final_inspection.py.txt
  exit_code: 0
  evidence_ids:
  - within-review-corrections
  - all-edge-adjudication
  scope_note: This wrapper executed scripts/record_review.py inspect with the exact
    target manifest and 48 explicit context inputs. The final-inspect-command.json
    receipt records all 49 bound inputs and the actual arguments.
- check_id: gate-1
  name: just render-pages
  status: passed
  required: false
  summary: The initial full repository render completed with exit 0. Its exact generated
    page and downloads remain unchanged; the only later source-storage change was
    the verified lossless ADIPATE relocation, with proof additions and bounded report
    documentation changes.
  target_ids:
  - MetaCyc:PWY-5417
  command: just render-pages
  exit_code: 0
  evidence_ids:
  - production-gates
  scope_note: Full repository scope; no invented one-record validator. This reviewer
    inspected the actual parent receipt rather than repeating the command.
- check_id: gate-2
  name: just validate
  status: passed
  required: true
  summary: The initial full repository validation completed with exit 0. Carry-forward
    is supported by the exact input inventory and the reviewed lossless storage and
    proof/documentation deltas; maintained scientific, schema and code inputs remain
    unchanged.
  target_ids:
  - MetaCyc:PWY-5417
  command: just validate
  exit_code: 0
  evidence_ids:
  - production-gates
  scope_note: Full repository scope; no invented one-record validator. This reviewer
    inspected the actual parent receipt rather than repeating the command.
- check_id: gate-3
  name: just test
  status: passed
  required: true
  summary: 'The complete suite was rerun in the separate verified frozen-lock environment:
    5255 passed, 3 skipped and 7 warnings in 793.34 seconds. The command exited 0;
    the initial failed attempt remains separately reported.'
  target_ids:
  - MetaCyc:PWY-5417
  command: just test
  exit_code: 0
  evidence_ids:
  - production-gates
  scope_note: Full repository scope; no invented one-record validator. This reviewer
    inspected the actual parent receipt rather than repeating the command.
- check_id: gate-4
  name: just lint
  status: passed
  required: true
  summary: Parent-executed command completed with exit 0; retained receipt and raw
    log bind its actual full-corpus scope.
  target_ids:
  - MetaCyc:PWY-5417
  command: just lint
  exit_code: 0
  evidence_ids:
  - production-gates
  scope_note: Full repository scope; no invented one-record validator. This reviewer
    inspected the actual parent receipt rather than repeating the command.
- check_id: gate-5
  name: just vendored-check
  status: passed
  required: false
  summary: Parent-executed command completed with exit 0; retained receipt and raw
    log bind its actual full-corpus scope.
  target_ids:
  - MetaCyc:PWY-5417
  command: just vendored-check
  exit_code: 0
  evidence_ids:
  - production-gates
  scope_note: Full repository scope; no invented one-record validator. This reviewer
    inspected the actual parent receipt rather than repeating the command.
- check_id: gate-6
  name: git diff --check
  status: passed
  required: true
  summary: Parent-executed command completed with exit 0; retained receipt and raw
    log bind its actual full-corpus scope.
  target_ids:
  - MetaCyc:PWY-5417
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - production-gates
  scope_note: Full repository scope; no invented one-record validator. This reviewer
    inspected the actual parent receipt rather than repeating the command.
- check_id: gate-7
  name: git diff --cached --check
  status: passed
  required: false
  summary: Parent-executed command completed with exit 0; retained receipt and raw
    log bind its actual full-corpus scope.
  target_ids:
  - MetaCyc:PWY-5417
  command: git diff --cached --check
  exit_code: 0
  evidence_ids:
  - production-gates
  scope_note: Full repository scope; no invented one-record validator. This reviewer
    inspected the actual parent receipt rather than repeating the command.
- check_id: chemical-source-reconstruction
  name: Independent chemical reconstruction
  status: passed
  required: true
  summary: Thirteen formal chemicals, eight supplemental context entities and two
    additional endpoints were independently assessed using exact issuing/native originals.
    RDKit 2026.03.5 used supported RDBASE; source-author release differences produced
    no identity discrepancy.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - chemical-equations
  - two-context-chemicals
- check_id: original-protein-primary-review
  name: Original-source protein and preparation review
  status: passed
  required: true
  summary: Deposited CDS translations, current/deleted UniProt records, six PDB assemblies,
    high-risk primary conflicts and remaining paper families assessed independently.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - biological-preparation
  - remaining-primary-papers
- check_id: native-and-reference-replay
  name: Native locator and reference replay
  status: passed
  required: true
  summary: Native slot/XPath completeness, graph endpoints, material coefficients,
    Rhea LR/RL side metadata and reference digest owners passed with explicit limits.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - formal-graph-replay
  - source-authority-replay
- check_id: imodulon-adapter
  name: Structured iModulonDB cross-check
  status: passed
  required: true
  summary: Dataset discovery, pca search and module 65 summary passed. The catA adapter
    returned exit 2 for a null regulator; the exact raw API fallback was retained
    and inspected. E. coli paaJ was a gene hit without a module. The absence of a
    matching Cupriavidus dataset is not negative pathway evidence.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - imodulon-context
  - biological-preparation
- check_id: generated-graph
  name: Generated graph and KGX scope
  status: passed
  required: true
  summary: Rendered graph and export preserve direction, qualifiers, edge-specific
    evidence and narrow preparation scope; completed production bindings inspected.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - generated-scope
  - browser
  - kgx
- check_id: imodulon-catA-original-attempt
  name: Original catA adapter attempt
  status: failed
  required: false
  summary: 'Retained actual exit 2: a returned imodulon regulator was null rather
    than a list. This attempt is not reported as a pass; the raw API fallback supports
    the bounded context assessment.'
  target_ids:
  - MetaCyc:PWY-5417
  command: kg-microbe-sources imodulondb search --organism p_putida --dataset precise321
    --query catA
  exit_code: 2
  evidence_ids:
  - biological-preparation
  - imodulon-context
- check_id: initial-production-environment-failure
  name: Initial full-test attempt with disrupted shared environment
  status: failed
  required: false
  summary: The initial full test run ended with 102 failed, 4975 passed, 3 skipped
    and 178 errors after files disappeared from the shared environment. The deletion
    actor is unknown. Two initial traces do not establish an exact cause; later full-suite
    success does not erase these observations. A separate frozen-lock environment
    completed all 5255 tests successfully, with 3 skipped and 7 warnings.
  target_ids:
  - MetaCyc:PWY-5417
  command: just test
  exit_code: 1
  evidence_ids:
  - initial-failed-production
evidence:
- evidence_id: chemical-equations
  kind: database
  reference: research/pathway_additions/2026-10-14-next-263/independent-chemistry/adjudication.json.gz
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Independent original-source reconstruction supports thirteen formal chemical
    identities, six whole equations, twenty-one material roles, five joins and net
    carrier cancellation. Separate native and issuing structures retain stereochemistry,
    charge and protonation limits.
  snapshot_sha256: 245bb67c56305c357204cc1aed47dbf97a1aa30dcb0270481f7c1354cdbbe944
- evidence_id: biological-preparation
  kind: primary_source
  reference: research/pathway_additions/2026-10-14-next-263/independent-science-source-preparation/independent/source-preparation-adjudication.json.gz
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Independent complete-source and visual-page preparation assesses B13 inhibitor
    target conflicts, MT1 enzyme purity, H16 gene identity, historical PcaD, deleted
    CatA pointer, deposited sequences, PDB assemblies and PcaR expression/binding
    scope.
  snapshot_sha256: 136fe81e2034c799cbabd25da6c01bef574cca036b890b7fa320533a60febf7c
- evidence_id: remaining-primary-papers
  kind: primary_source
  reference: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/primary-edge-audit/independent/adjudication.json
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: An independent delegated reviewer read the remaining finite primary families,
    visually inspected critical tables, identified the AY029000 strain-scope defect
    and rechecked its correction. Access and preparation limits remain explicit.
  snapshot_sha256: 7bb2fd3c8d57a5adb5f4106a5b30b854aebc4f06648e163af4a99f8ed3b07221
- evidence_id: all-edge-adjudication
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/final-scientific-adjudication.json
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Independent final assessment assigns all 117 edges to sixteen evidence-specific
    groups and reviews source-to-graph omissions, identifier/preparation scope, taxonomy
    and evidence placement.
  snapshot_sha256: 6c301c320358fbe597baeec7c4dfcee500bee4da6c0029175e5b76d24d4ea470
- evidence_id: within-review-corrections
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/initial-findings-and-reassessments.json
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Exact initial observations and successor reassessments preserve issues
    567–570 without fabricating an earlier canonical review. Current target has no
    remaining supported defect from those observations.
  snapshot_sha256: 2d8fb573a193c27eb7b4040838787081438058f13b8cf4e9147fdb0055239279
- evidence_id: formal-graph-replay
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/final-graph-reference-replay.json.gz
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Actual maintained graph matches six independently reconstructed equations,
    twenty-one coefficients and five joins; all 211 reference digests are bound. Later
    reviewed changes leave these triples, identifiers, chemical structures and digest
    ownership unchanged.
  snapshot_sha256: d8bf30e655f867aae41db01d58646fd4f15861196ae052611e024d35d58206cb
- evidence_id: source-authority-replay
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/source-coverage-authority-replay.json.gz
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Fresh replay resolves all 3252 retained native slot locators, 22 native
    enzyme/activity links including two adjacent activities, 11 organism objects,
    48 PMID bibliographic identities and 123 selected authority owners. Counts do
    not substitute for scientific assessment.
  snapshot_sha256: d3e64eebb657830b65c93db79ca16d8d4039157be7915461685afc4a992b8b86
- evidence_id: two-context-chemicals
  kind: database
  reference: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/checks/context-chemistry-independent.json
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Independent CML, formula, charge and full InChI/key checks accept CHEBI:16810
    and CHEBI:17128; fresh read-only SQL retrieves all 41 and 29 subject rows. Exact
    recent whole-database hash receipt is reused transparently after stat verification.
  snapshot_sha256: 55cdd056047cac41cecd9f6bb62bb301c4bef6becc0786e3f55e7496cdee0e85
- evidence_id: imodulon-context
  kind: database
  reference: research/pathway_additions/2026-10-14-next-263/independent-science-source-preparation/independent/imodulondb/pcaR-65-raw.json.gz
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: context_only
  summary: Pseudomonas putida precise321 PcaR module 65 contains the relevant current
    KT2440 genes; module membership remains computational expression context only.
    The retained preparation includes datasets/search/summarize, a null-regulator
    adapter failure and exact raw-source fallback.
  snapshot_sha256: ec719cc8cb6610f96dc9db358ffb685e475780d139e29b8deb8a46ba0a230045
- evidence_id: frozen-summary-notice
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-263/source-evidence/primary/CORRECTIONS.md
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Explicit source-bound notice supersedes incorrect frozen P263-C48 pcaF
    repression and P263-C43 Table 1 locator while retaining immutable originals.
  snapshot_sha256: 0d1aa33c3fb0db085a37f3904010b34b2591e65c99ac429fa1d23531aa446f24
- evidence_id: initial-failed-production
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-263/verification/full-gates/initial/receipts.json
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: context_only
  summary: Failed initial production attempt preserved after files disappeared from
    the shared environment; the deletion actor remains unknown; successor gates use
    a separately verified isolated environment.
  snapshot_sha256: cf1ebe5a9feb3ce8f5ad57bb72575403c9896eb28873f47f7863f04e71f380fe
- evidence_id: production-gates
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-263/verification/full-gates/successful-receipts.json
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Actual parent-executed full production commands, exit codes, raw logs and
    exact tested inputs were independently inspected. All seven successful log digests
    and decoded retained logs match their originals. The 2972 initial inputs, 3178
    recovered inputs and nine critical runtime files were rechecked with explicit
    storage/documentation deltas. These checks establish deterministic validation,
    not scientific truth.
  snapshot_sha256: 3659f01521e474affa1b8fc404e7462316ef54ce654e0a5f0937aad5f653beae
- evidence_id: generated-scope
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-263/independent-scientific-review/generated-verification/generated-scientific-scope.json.gz
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: Independent SVG semantic inspection maps all 117 graph edges to authored
    triples, complete descriptions and preparation-qualified endpoints; 129 display
    nodes include 15 qualified contexts.
  snapshot_sha256: 91e3d286467c700d8c4573cf98646cb794c2c221854007739dc4dd1321c1ca6a
- evidence_id: browser
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-263/verification/browser/browser-cdp-result.json
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: 'The parent performed live browser interactions and retained exact page
    and screenshot bindings. This reviewer independently viewed both exact screenshots:
    controls, legend and graph render on desktop and mobile; fitted labels are dense
    and require zoom or node selection. This is not a claim that this reviewer repeated
    live browser interactions.'
  snapshot_sha256: 3c3be36f1255a4f615a3149fc9308bea8055b848ef031dbf4b641aa192e59c46
- evidence_id: kgx
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-263/verification/kgx-export-receipt.json
  locator: Complete retained file; original and stored SHA-256 bindings in owning
    retention manifest.
  accessed_at: '2026-10-15T08:09:29.273134Z'
  support: supports
  summary: The actual production CLI export completed successfully and its complete
    node/edge TSV bytes equal the tracked page downloads. Independent scientific payload
    checks preserved all 117 target edge triples, descriptions, reference metadata
    and endpoint qualifiers, including the issuing Rhea RL direction metadata.
  snapshot_sha256: 7c332768f357925859890b49c863902995570af1e77cedafddbc7c2b9508f547
assessments:
- assessment_id: identity
  area: identity
  topic: Exact catechol degradation III route
  outcome: supported
  summary: PWY-5417 denotes the six-step ortho-cleavage route through stereospecific
    muconolactone and 3-oxoadipate to succinate and acetyl-CoA. Child modules, adjacent
    chlorinated activities and donor organisms remain separate.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - chemical-equations
  - all-edge-adjudication
  - source-authority-replay
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - chemical-equations
    - all-edge-adjudication
    - source-authority-replay
- assessment_id: formal-chemistry
  area: quantity
  topic: Whole equations, directions and net cancellation
  outcome: supported
  summary: All six whole equations and 21 material entries are supported. Cycloisomerase
    and thiolase Rhea nodes use issuing RL orientation; formatted forward equations
    are not contradictory. Succinyl-CoA cancels across the transferase/thiolase pair.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - chemical-equations
  - formal-graph-replay
  - two-context-chemicals
  details: The fixed whole-Rhea scan covers 37068 equations and excludes 154 symbolic
    cases. Native incomplete SMILES and broader KEGG stereochemistry are explicit
    limits; formal identity does not assert historical substrate purity. The net route
    is catechol + O2 + H2O + CoA(4−) → succinate(2−) + acetyl-CoA(4−) + 2 H+. The
    succinyl-CoA carrier cancels between the transferase and thiolase steps.
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - chemical-equations
    - formal-graph-replay
    - two-context-chemicals
- assessment_id: source-graph
  area: completeness
  topic: Bidirectional source coverage and all 117 edges
  outcome: supported
  summary: The complete finite record and source closure are assessed, including 20
    formal enzyme/activity assignments, two adjacent activities, complex components,
    cofactors, regulation, five joins and five predecessor relations. No material
    finite-scope omission remains after n100 evidence strengthening.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - all-edge-adjudication
  - source-authority-replay
  - remaining-primary-papers
  - biological-preparation
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - all-edge-adjudication
    - source-authority-replay
    - remaining-primary-papers
    - biological-preparation
- assessment_id: taxon-preparation
  area: scope
  topic: Organisms, proteins, assemblies and historical preparations
  outcome: supported
  summary: Nine grounded parent taxa preserve 11 native organism rows and two ungrounded
    strain contexts. Native parent annotation is not all-step experimental evidence.
    Historical PRS/C1/MT1 preparations, current KT2440 accessions, H16 loci, engineered
    hosts and PDB variants remain distinct.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - biological-preparation
  - remaining-primary-papers
  - source-authority-replay
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - biological-preparation
    - remaining-primary-papers
    - source-authority-replay
- assessment_id: edge-evidence
  area: evidence
  topic: Evidence placement and endpoint qualifiers
  outcome: supported
  summary: Native database assertions remain separate from paper excerpts. MT1 purity,
    metal-free CcaC, PcaR expression versus recombinant DNA binding, B13 inhibitor
    targets and adjacent EDTA activity are attached to the proper edge or endpoint
    context.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - all-edge-adjudication
  - biological-preparation
  - remaining-primary-papers
  - generated-scope
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - all-edge-adjudication
    - biological-preparation
    - remaining-primary-papers
    - generated-scope
- assessment_id: source-conflicts
  area: consistency
  topic: Native conflicts and retained uncertainty
  outcome: supported
  summary: All 18 bounded native conflicts are preserved, corrected or explicitly
    excluded without upgrading ambiguous source metadata. PcaD historical mass, deleted
    Q9AEQ0, H16 pcaI/J/F, NaCN/HCN and broad muconolactone forms are not silently
    equated.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - all-edge-adjudication
  - biological-preparation
  - chemical-equations
  - remaining-primary-papers
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - all-edge-adjudication
    - biological-preparation
    - chemical-equations
    - remaining-primary-papers
- assessment_id: issue-dispositions
  area: provenance
  topic: Within-review corrections and external issues 567–570
  outcome: supported
  summary: 'The current b30573a target and explicit correction notice satisfy issues
    567–570: the pcaF benzoate exception, Results prose locator, AY029000 strain-unspecified
    deposit and EDTA charge wording. The observed defects and fixes occurred within
    this review before its first canonical save; no canonical predecessor or previous_occurrences
    is invented.'
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - within-review-corrections
  - frozen-summary-notice
  - remaining-primary-papers
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - within-review-corrections
    - frozen-summary-notice
    - remaining-primary-papers
- assessment_id: authority
  area: grounding
  topic: Selected issuing identifiers and reference provenance
  outcome: supported
  summary: All 123 named identifiers have exact selected authority ownership; all
    211 references have declared complete-file or explicitly stated whole-database
    digest scope. Twenty-three chemical endpoints and protein/genome/PDB identities
    are independently distinguished from preparation equivalence.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - source-authority-replay
  - formal-graph-replay
  - two-context-chemicals
  - biological-preparation
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - source-authority-replay
    - formal-graph-replay
    - two-context-chemicals
    - biological-preparation
- assessment_id: imodulon
  area: evidence
  topic: Computational expression context
  outcome: supported
  summary: PcaR module 65 membership for current KT2440 pca genes supports bounded
    expression context only. The adapter failure is retained with raw fallback. No
    membership, absence or broad substring hit is treated as catalytic or pathway
    proof.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - imodulon-context
  - biological-preparation
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - imodulon-context
    - biological-preparation
- assessment_id: production
  area: representation
  topic: Generated graph, exports and repository gates
  outcome: supported
  summary: Required full-corpus checks and exact production outputs passed. SVG and
    KGX retain authored direction, descriptions, evidence and endpoint qualification.
    Generated owners remain the maintained YAML and existing render/export implementation.
  target_ids:
  - MetaCyc:PWY-5417
  evidence_ids:
  - production-gates
  - generated-scope
  - browser
  - kgx
  dimensions:
  - name: evidence-tier
    value: Claim-specific original source evidence with separately identified deterministic
      checks
    definition: Primary assay, structured source annotation, sequence/assembly context
      and expression-module context are not interchangeable.
    evidence_ids:
    - production-gates
    - generated-scope
    - browser
    - kgx
findings: []
actions: []
limitations:
- Some primary evidence is abstract-only, partial article reproduction or historical
  scan material. Each access boundary remains declared; unreadable miniprint methods
  are not reconstructed.
- Modern protein sequence and assembly annotation does not retrospectively prove a
  historical preparation identity. The deleted CatA pointer, unqualified AY029000
  strain and historical PcaD discrepancies remain bounded uncertainties.
- Formal chemical identities preserve exact structure/charge/stereochemistry; they
  do not measure assay solution speciation, salt identity or historical enantiomeric
  purity.
- Whole-Rhea equality is limited to the 37068 fixed equations tested; 154 symbolic
  equations were excluded. No broader provider equivalence is claimed.
- iModulonDB evidence is computational expression context. The catA adapter failed
  on a null regulator; an exact retained raw API fallback was inspected.
- A clean final observation does not erase immutable source-author defects or initial
  review findings. Their exact observations, fixes and external issues are retained
  without invented canonical lineage.
- At the fitted full-graph scale, labels are dense on both desktop and mobile. The
  verified zoom and node picker provide readable selected contexts.
notes:
- Scientific source evidence frozen before production gates remains immutable and
  explicitly labels its then-pending gate status. This complete review additionally
  binds actual later gate and generated-output receipts.
- Helpers preserve real failed parser/check attempts and corrected bounded reruns;
  those implementation errors are not relabeled as scientific source failures.
- All completeness/absence inventories explicitly include ignored and hidden files
  where applicable.
- This content was prepared and validated externally by the independent reviewer.
  The parent performs the canonical immutable save and consumer check; preparation
  alone is not saved-review persistence.
- Successful initial render and validation are carried forward through exact input
  accounting. A separately isolated full-suite rerun passed after the shared environment
  lost files. The deletion actor and the exact causes of two initial traces remain
  unknown. The later success does not erase the preserved failures.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/567
- https://github.com/CultureBotAI/PathwayMech/issues/568
- https://github.com/CultureBotAI/PathwayMech/issues/569
- https://github.com/CultureBotAI/PathwayMech/issues/570
tags:
- next263
- independent-science
- catechol
- source-conflicts
```
