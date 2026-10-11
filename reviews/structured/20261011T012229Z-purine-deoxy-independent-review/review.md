# Independent scientific review of the complete purine deoxyribonucleoside degradation pathway

- Review: 20261011T012229Z-purine-deoxy-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T01:15:36Z
- Finished UTC: 2026-10-11T01:22:29Z
- Reviewer: Codex independent purine reviewer (/root/verify_graph_publication) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact six-reaction native pathway is supported across 32 named nodes, 49 edges and 80 evidence blocks, retaining strain, primary-access, assembly and cofactor limitations. No corrective finding identified in this target. Required integrated gates passed on the final frozen inputs.

## Scope And Provenance

Full scientific review of the one exact maintained purine deoxyribonucleoside record and its local mechanism, evidence and references.

Selection: Assigned PathBank:SMP0002089 at data/pathways/purine-deoxyribonucleosides-degradation.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 117e2e8b99989a846bd04901268a7a49cc0bd500.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PathBank:SMP0002089 | data/pathways/purine-deoxyribonucleosides-degradation.yaml | maintained | Purine Deoxyribonucleosides Degradation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Governed inspect before assessment | passed | False | PathBank:SMP0002089 | Initial actual terminal0 captured target and authority/dossier inputs before assessment; original eight inputs unchanged on final recheck. |
| Independent complete raw-source replay | passed | False | PathBank:SMP0002089 | Actual terminal exit0: 22 exact chemical-side assertions, six direction families and balances, full native boundary, protein/taxon and assembly bridges, ontology identities and all29 reference-body hashes. |
| Canonical structured-source console availability | unavailable | False | PathBank:SMP0002089 | Root console attempt exited1 before retrieval with missing dotenv; unchanged direct-client fallback exited0. Independently rehashed all38 bodies and inspected applicable exact responses. |
| just render-pages | passed | False | PathBank:SMP0002089 | Root actual terminal exit0; independently inspected and rehashed log. Final 177-record integrated scope passed. |
| just lint | passed | True | PathBank:SMP0002089 | Root actual terminal exit0; independently inspected and rehashed log. Final 177-record integrated scope passed. |
| just check-identifiers | passed | False | PathBank:SMP0002089 | Root actual terminal exit0; independently inspected and rehashed log. Final 177-record integrated scope passed. |
| git diff --check | passed | True | PathBank:SMP0002089 | Root actual terminal exit0; independently inspected and rehashed log. Final 177-record integrated scope passed. |
| just kgx-export --output-dir /private/tmp/pathwaymech-next-cohort-kgx | passed | False | PathBank:SMP0002089 | Root actual terminal exit0; independently inspected and rehashed log. Final 177-record integrated scope passed. |
| just validate | passed | True | PathBank:SMP0002089 | Root actual terminal exit0; independently inspected and rehashed log. Final 177-record integrated scope passed. |
| just test | passed | True | PathBank:SMP0002089 | Root actual terminal exit0; independently inspected and rehashed log. 1048 passed, 3 skipped, 3 warnings in 209.00s. |
| UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just vendored-check | passed | False | PathBank:SMP0002089 | Root actual terminal exit0; independently inspected and rehashed log. Final 177-record integrated scope passed. |

## Scientific And Domain Assessments

### Exact native six-reaction boundary

identity: supported. Targets: PathBank:SMP0002089.

PathBank identity preserves the complete assigned route and all parallel substrates. The larger MetaCyc superpathway and generic GO process are contextual, not asserted exact matches. No convenient partial module was substituted.

### Precise species, direction families and balances

representation: supported. Targets: PathBank:SMP0002089.

All22 chemical edges match exact Rhea species, coefficients and side locators; all six balances pass. Broad/uncharged native chemical forms are normalized through exact enzyme/Rhea grounding, not asserted identical to differently charged or stereochemically incomplete species. Five provides_input_for edges use identical shared intermediates.

### Correct catalytic entities and physical assembly limits

evidence: supported. Targets: PathBank:SMP0002089.

DeoD complex is the catalyst for all three phosphorolyses; its subunit only has membership. DeoB single-chain primary evidence supports its catalyzes edge. Add and DeoC use qualified functional roles; buffer-dependent monomer/dimer evidence is preserved.

### Taxon, cofactors and localization evidence

scope: supported. Targets: PathBank:SMP0002089.

MG1655 component annotations are explicit, K-12 source entry scope and experimental limits remain visible, and no whole-route in-vivo flux is asserted. Add zinc sequence inference and alternative DeoB metal activities retain their grades. Exact UniProt IDA:EcoCyc cytosol annotations and native complex location support bounded compartment assertions.

### Nearest inspected source and complete references

provenance: supported. Targets: PathBank:SMP0002089.

All49 edges and80 evidence blocks are supported at their actual native or primary locators. Six pathway-membership bridges explicitly cite Rhea master directionalReaction and bidirectionalReaction properties as needed. Inaccessible full texts are not represented as inspected experimental evidence; all29 retained reference digests match actual source bodies.

### Structured expression cross-check

evidence: supported. Targets: PathBank:SMP0002089.

Exact iModulon context memberships agree with retained source bodies and do not create catalytic, regulatory, directional or flux assertions. Console availability limitation and successful direct-client fallback are explicit.

### Final gates and generated evidence preservation

graph: supported. Targets: PathBank:SMP0002089.

Final required gates passed and the programmatic SVG/KGX audit preserves all49 target edges and80 evidence blocks, including source metadata and context. Browser interaction and visual layout were not assessed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/purine-deoxyribonucleosides-degradation.yaml; Entire target: 24 participants, six reactions, 49 edges, 80 evidence blocks, 29 references | supports | Entire target read before assessment; every material edge assertion assessed at its nearest inspected source. Target unchanged from initial inspect to final save. |
| e-pathbank | https://pathbank.org/downloads/pathbank_primary_biopax.zip; Uncompressed PW002077.owl, SMP0002089 pathway, six reactions6067–6072, linked Catalysis and Protein objects, complex4056 | supports | The exact six-reaction route contains Add deamination, three DeoD phosphorolyses, sugar-phosphate rearrangement and cleavage. Native6068 is right-to-left. All source roles are retained; uptake and terminal acetaldehyde oxidation are outside this boundary. |
| e-boundary | https://pathway.yeastgenome.org/getxml?META:PWY0-1297; PWY0-1297 reaction-list; separately inspected PWY-7179 and PWY-7180 full reaction-lists and comments | supports | The broader MetaCyc superpathway expands to seven reactions, including acetaldehyde oxidation. It is not exact identity for this six-step PathBank pathway. GO parent and adjacent pyrimidine or ribonucleoside routes are also not substituted. |
| e-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Complete Rhea142 RDF: masters28190,27742,27750,27738,27658,12821 and selected directed members; directionalReaction/bidirectionalReaction, substrates/products, contains1, compound and chebi | supports | Independently streamed full raw RDF and directions TSV. All six master-relative directions are left-to-right; native6068 reverse orientation yields identical deamination chemistry. All22 chemical-side locators and coefficients match; six elemental/charge balances pass with complete ChEBI authority. |
| e-uniprot | https://rest.uniprot.org/uniprotkb/P22333.json; Full P22333 comments2/3 and entryAudit; separately inspected P0ABP8 comments6/7/8/10, P0A6K6 comments1/3, P0A6L0 comments1/4; exact organism, proteinDescription and cytosol GO cross-references | supports | All four reviewed K-12 accessions and canonical labels match. Exact reaction annotations are experimentally attributed where stated. Add Zn is ECO0000255 HAMAP MF00540 inference; DeoB alternative activators are separately qualified from by-similarity occupancy; DeoC monomer/homodimer alternatives retained. UniProt2026_03 is supported by retained release headers. |
| e-native | https://pathway.yeastgenome.org/getxml?META:DEOD-CPLX; DEOD-CPLX component coefficient6, native reaction links and CCO-CYTOSOL; all four monomer UniProt unifications and TAX511145 species; ADDALT-ENZRXN physiology/evidence slot | supports | Six DEOD-MONOMER copies form the named complex; PathBank independently agrees. Native MG1655 component annotations bridge reviewed K-12 entries without claiming experimental whole-route MG1655 flux. Add and DeoC use functional enables edges where a unique physical assembly is not established. |
| e-pnp-abstract | https://pubmed.ncbi.nlm.nih.gov/235429/; EuropePMC retained indexed primary abstract resultList.result[0].abstractText | supports | Inspected primary abstract describes six equal probably identical PNP subunits and association experiments suggesting the hexamer is active. This supports the native assembly rather than asserting three directly re-inspected deoxy-substrate assays. |
| e-deob-primary | https://pubmed.ncbi.nlm.nih.gov/1089430/; EuropePMC retained indexed primary abstract resultList.result[0].abstractText | supports | Inspected primary abstract describes four purified phosphodeoxyribomutase forms each as a single polypeptide chain of about45kDa, with differing cobalt-binding properties. This supports the single-protein catalytic representation. |
| e-deoc-primary | https://pubmed.ncbi.nlm.nih.gov/6749498/; EuropePMC retained indexed primary abstract resultList.result[0].abstractText | supports | Inspected K-12 primary abstract preserves monomer and dimer forms; native discussion adds buffer dependence. Salmonella active-site inference is not transferred. |
| e-deoc-cleavage | https://pubmed.ncbi.nlm.nih.gov/7675789/; EuropePMC retained indexed primary abstract resultList.result[0].abstractText | supports | Inspected primary abstract states reversible exact deoxyribose5-phosphate cleavage to glyceraldehyde3-phosphate and acetaldehyde; asymmetric-unit copy count is not used as a physiological assembly claim. |
| e-pnp-full | https://pmc.ncbi.nlm.nih.gov/articles/PMC6193948/; Relevant full-text Results and Discussion crystal structures paragraph beginning All PNP structures, assay context and concluding architecture discussion; PMID30337572 | supports | Primary full text corroborates a trimer-of-dimers PNP assembly and catalytic structural interpretation. Wild-type/mutant and ribonucleoside/analogue assay scope is retained; this is not direct measurement of every deoxy substrate or native whole-route flux. Live primary PMC page also independently corroborated citation identity. |
| e-replay | research/pathway_additions/2026-10-10-next-cohort/purine-independent-review-audit.json; Independent replay result, all49 edge-group assessments, raw body/reference hashes, initial-input parity and complete chemical replay | supports | Independent replay passed. Native reaction/catalyst objects, exact source locators, ontology labels, species bridges and29 reference hashes were checked. Scratch initial syntax failure and correction are retained honestly. |
| e-context | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/43/genes; Exact add/b1623 and deoB/b4383 rows in k43; deoC/b4381 in k33; eight relevant gene/locus search bodies and full acquisition receipts | context_only | Applicable raw API rows agree with preserved summaries. Broad add search also matches other genes, so exact loci are used. All38 retained bodies were independently rehashed. Membership supplies computational expression context only; zero module-name hits do not establish absence. |
| e-search | research/pathway_additions/2026-10-10-next-cohort/purine-deoxy-search-ledger.json; Author ignored-inclusive ledger and reviewer independent exact ID/member/name search across data,research,reports,reviews | context_only | Prior archive-screening appearances were candidates, not existing records. Exact maintained matching path is this new record; existing pyrimidine deoxy and yeast nucleotide routes have distinct substrate and endpoint boundaries. Original Documents checkout access remains unavailable. |
| e-gates | research/pathway_additions/2026-10-10-next-cohort/integration-validation.json; Final actual terminal receipts, independently read/rehashed logs and final graph/KGX scoped audit | supports | Parent executed complete final corpus gates. Reviewer checked exact results and log hashes, and target49-edge/80-evidence graph preservation. These deterministic checks do not scientifically review other records. |

## Limits And Additional Notes

- PathBank is the retained 2019 archive member; MetaCyc is the explicit public 22.5 snapshot. Current reviewed UniProt 2026_03 complements these sources without a newest licensed MetaCyc claim.
- Several older primary full texts were unavailable. Substantive abstracts for PMID235429,1089430,6749498,7675789 and relevant full-text sections of PMC6193948 were inspected. Detailed PMID357905/4992818 claims remain attributed to exact inspected UniProt/native slots; metadata is not experimental text.
- MG1655 native component annotations, K-12 reviewed entries and older E. coli experiments are distinct scopes; complete native MG1655 pathway flux is not established. Add zinc is sequence inference; alternative DeoB metal activities do not establish physiological metal occupancy; DeoC assembly is condition dependent.
- Canonical iModulon console invocation failed before retrieval because dotenv was missing; root successfully called the unchanged direct client. Reviewer rehashed all 38 raw responses and checked applicable searches and exact component rows. Expression evidence is context only and search misses are not biological absence.
- Original Documents checkout was inaccessible; hidden/ignored-inclusive search covers the accessible worktree data, research, reports and reviews. Browser surfaces were unavailable; graph QA is programmatic, not visual or interactive.
- This bounded review does not establish exhaustive literature coverage or source exhaustion.
- Initial governed inspect target SHA1412ec0cdb11458da71fd9b50a8c0827effefe28fe9ac949213db928d1e26087 remained unchanged. All eight initially captured inputs remained byte-identical through final recheck.
- Reviewer scratch replay initially failed with a missing closing parenthesis before running any assertions. The syntax was corrected and the complete independent replay subsequently exited0; no target changes resulted.
- Issue335 concerns the separate reviewer-authored pyrimidine route and is neither a purine finding nor reviewed here as an independent author assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T012229Z-purine-deoxy-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of the complete purine deoxyribonucleoside degradation
  pathway
started_at: '2026-10-11T01:15:36Z'
finished_at: '2026-10-11T01:22:29Z'
reviewer:
  identity: Codex independent purine reviewer (/root/verify_graph_publication)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: A different agent authored this purine record and its author
    dossiers. This reviewer did not edit that target; governed inspect preceded complete
    target/source assessment and independently written raw replay. This reviewer authored
    the separate pyrimidine ribonucleoside route, including its issue335 correction,
    and had prior familiarity with shared DeoB sources. That separate record is excluded
    from this scientific verdict.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact six-reaction native pathway is supported across 32 named nodes,
  49 edges and 80 evidence blocks, retaining strain, primary-access, assembly and
  cofactor limitations. No corrective finding identified in this target. Required
  integrated gates passed on the final frozen inputs.
source:
  git_revision: 117e2e8b99989a846bd04901268a7a49cc0bd500
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: 296ab1a206afa3aa9b487eae7f5f8d836c09001a4ce9ee8016c36abe198cdc0d
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: CLAUDE.md
    sha256: c067d99547f9e9e9a6edb892d71126b6765239348d0021b907f3102907a4cf00
    role: context
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: d0a5e6a269c287a9892e2ffd1b5cf3b66f307be21cb4a3e80b808e5314e2e5ea
    role: context
  - path: conf/sources.yaml
    sha256: 49507bca325f9529bd25b3507b062a1241c403916293dbab96d3cb598d6a7a95
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: ae975c3ad67b3366deec6b74229f34f89666e1ec5594c0e4d1ffc7402b453a47
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 67e5136727d23ae7cd52c3511b43523d258caffdfae9424dccfe6896c941551a
    role: context
  - path: data/pathways/purine-deoxyribonucleosides-degradation.yaml
    sha256: 1412ec0cdb11458da71fd9b50a8c0827effefe28fe9ac949213db928d1e26087
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 3c861f2ab78e3bc62146d05af5ed5c4c4ae3e65343fc9bd44afa76da7f0b62e7
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
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: pages/records/PathBank_SMP0002089.html
    sha256: 9ea07081e9d35041c4bc76d532bd649efbb74ba4ebe8c99ec24a18f92b27a444
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/authority-integration.json
    sha256: e5bec82ceedda98886742bf9fe269015e151fc278daa5f9de07dfe12eeb328a7
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/authority-protein-crosscheck.json
    sha256: f72010f3c5b60a4906238d4adde9773e5511fc3d6d6eec180c1303bdf2b02e7f
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/authority-source-inspection.json
    sha256: e72a0329864038e562e76c2d935840da8c272b20a00f8393f26e5711fa1a2639
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/baseline-preservation.json
    sha256: 09f148e179ad76b645b27cb8d7a173a9e6f4fd2be9000a7409cfda31dac28140
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/browser-availability.json
    sha256: 34ef0896c90cb5f41758db0e06c633c6a0dbdb6d92ab9b90da992e4abf7ccd68
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/generated-graph-kgx-audit.json
    sha256: 7a99dfdd6370ebab39c3d63d2e698049955416b74f7732bf5758e4de4b6b92a1
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/imodulondb-context.json
    sha256: cd09959330f33c6b808962e881755ad6d8d35e1c5a08b42835e8300ca70c4a32
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/imodulondb-parser-replay.json
    sha256: 0fac3b3a8e5f3f8f893613099746d21f906ba2e5fdb23be47fac411bf436c29f
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/imodulondb-runner-availability.json
    sha256: 22c60f1b4198096a055f3fd48610531146bfdb2f6c1e760b204585ba14f8152b
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/imodulondb-source-manifest.json
    sha256: ccc7dab02160c3ec5635a18605050a9f95ccbe601d796d938a19e4846ec65382
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/integration-validation.json
    sha256: dd58a6913ed745f8d941ef6fa15118c9d9b6e8e20182b366c55596bf8a8b408d
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/purine-deoxy-curation.md
    sha256: a78b0d6d54673211d2b8889e7541f1946ab0685291e8abe45f79d5849237738f
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/purine-deoxy-search-ledger.json
    sha256: 043d2e3782edbb1fa530a7d43e317b854a59587727eb3f69e41023a8aeaee13c
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/purine-deoxy-source-manifest.json
    sha256: 9797a0d5bc6641f41c8154628ba5188977de51e8b0f6921556a11667bbd2d9f3
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/purine-deoxy-source-projection.json
    sha256: dfce22567165511294153fd2cea6923db729a551f4786125adf1633679b33de5
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/purine-deoxy-validation.json
    sha256: 3689940867eba280dba262e083efc5915b7784398ed2eb85744acfc54e09b3c8
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/purine-independent-review-audit.json
    sha256: 0ca1bc14205e935db994b3efde504ffad7236a4af0fe07ea6ef8c7eb0786eabc
    role: context
  - path: research/pathway_additions/2026-10-10-next-cohort/vendored-check.json
    sha256: 73fa1a708d8d5a701098ad909eab516e635986efec793a2a84757f090658bcf1
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: Full scientific review of the one exact maintained purine deoxyribonucleoside
    record and its local mechanism, evidence and references.
  selection: Assigned PathBank:SMP0002089 at data/pathways/purine-deoxyribonucleosides-degradation.yaml
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PathBank:SMP0002089
  exclusions:
  - target: Other pathway records, including reviewer-authored pyrimidine ribonucleoside
      route
    reason: Outside this independent scientific verdict; corpus deterministic gates
      do not scientifically review other records.
  - target: Whole native in-vivo flux and inaccessible older paper full texts
    reason: Complete MG1655 flux is not demonstrated; detailed claims from inaccessible
      papers are evaluated as inspected reviewed/native annotations, never direct
      full-text results.
targets:
- target_id: PathBank:SMP0002089
  path: data/pathways/purine-deoxyribonucleosides-degradation.yaml
  label: Purine Deoxyribonucleosides Degradation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/purine-deoxyribonucleosides-degradation.yaml
    role: maintained pathway owner
checks:
- check_id: c-inspect
  name: Governed inspect before assessment
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-purine-independent-review/targets.yaml
    [explicit inputs retained in source]
  status: passed
  required: false
  summary: Initial actual terminal0 captured target and authority/dossier inputs before
    assessment; original eight inputs unchanged on final recheck.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-record
  exit_code: 0
  expected_exit_code: 0
- check_id: c-replay
  name: Independent complete raw-source replay
  command: .venv/bin/python /private/tmp/pathwaymech-purine-independent-review/replay.py
  status: passed
  required: false
  summary: 'Actual terminal exit0: 22 exact chemical-side assertions, six direction
    families and balances, full native boundary, protein/taxon and assembly bridges,
    ontology identities and all29 reference-body hashes.'
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-replay
  - e-rhea
  exit_code: 0
  expected_exit_code: 0
- check_id: c-imodulon
  name: Canonical structured-source console availability
  command: PYTHONPATH=/private/tmp/claw-published-duf-offline-20261007/src .venv/bin/python
    -m kg_microbe_sources imodulondb datasets
  status: unavailable
  required: false
  summary: Root console attempt exited1 before retrieval with missing dotenv; unchanged
    direct-client fallback exited0. Independently rehashed all38 bodies and inspected
    applicable exact responses.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-context
  scope_note: Availability failure is reported explicitly; successful fallback supplies
    bounded computational context.
- check_id: c-final-0
  name: just render-pages
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Root actual terminal exit0; independently inspected and rehashed log. Final
    177-record integrated scope passed.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent on frozen final inputs; reviewer audited actual
    receipt and log, did not repeat complete corpus gate. Log: /private/tmp/pathwaymech-next-cohort-render-final.log'
- check_id: c-final-1
  name: just lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: Root actual terminal exit0; independently inspected and rehashed log. Final
    177-record integrated scope passed.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent on frozen final inputs; reviewer audited actual
    receipt and log, did not repeat complete corpus gate. Log: /private/tmp/pathwaymech-next-cohort-lint-final.log'
- check_id: c-final-2
  name: just check-identifiers
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Root actual terminal exit0; independently inspected and rehashed log. Final
    177-record integrated scope passed.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent on frozen final inputs; reviewer audited actual
    receipt and log, did not repeat complete corpus gate. Log: /private/tmp/pathwaymech-next-cohort-identifiers-final.log'
- check_id: c-final-3
  name: git diff --check
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: Root actual terminal exit0; independently inspected and rehashed log. Final
    177-record integrated scope passed.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent on frozen final inputs; reviewer audited actual
    receipt and log, did not repeat complete corpus gate. Log: /private/tmp/pathwaymech-next-cohort-diff-final.log'
- check_id: c-final-4
  name: just kgx-export --output-dir /private/tmp/pathwaymech-next-cohort-kgx
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-cohort-kgx
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Root actual terminal exit0; independently inspected and rehashed log. Final
    177-record integrated scope passed.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent on frozen final inputs; reviewer audited actual
    receipt and log, did not repeat complete corpus gate. Log: /private/tmp/pathwaymech-next-cohort-kgx-audit-cli.log'
- check_id: c-final-5
  name: just validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: Root actual terminal exit0; independently inspected and rehashed log. Final
    177-record integrated scope passed.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent on frozen final inputs; reviewer audited actual
    receipt and log, did not repeat complete corpus gate. Log: /private/tmp/pathwaymech-next-cohort-validate-final.log'
- check_id: c-final-6
  name: just test
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: Root actual terminal exit0; independently inspected and rehashed log. 1048
    passed, 3 skipped, 3 warnings in 209.00s.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent on frozen final inputs; reviewer audited actual
    receipt and log, did not repeat complete corpus gate. Log: /private/tmp/pathwaymech-next-cohort-test-final.log'
- check_id: c-final-7
  name: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Root actual terminal exit0; independently inspected and rehashed log. Final
    177-record integrated scope passed.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent on frozen final inputs; reviewer audited actual
    receipt and log, did not repeat complete corpus gate. Log: /private/tmp/pathwaymech-next-cohort-vendored.log'
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/purine-deoxyribonucleosides-degradation.yaml
  locator: 'Entire target: 24 participants, six reactions, 49 edges, 80 evidence blocks,
    29 references'
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Entire target read before assessment; every material edge assertion assessed
    at its nearest inspected source. Target unchanged from initial inspect to final
    save.
  snapshot_sha256: 1412ec0cdb11458da71fd9b50a8c0827effefe28fe9ac949213db928d1e26087
- evidence_id: e-pathbank
  kind: database
  reference: https://pathbank.org/downloads/pathbank_primary_biopax.zip
  locator: Uncompressed PW002077.owl, SMP0002089 pathway, six reactions6067–6072,
    linked Catalysis and Protein objects, complex4056
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: The exact six-reaction route contains Add deamination, three DeoD phosphorolyses,
    sugar-phosphate rearrangement and cleavage. Native6068 is right-to-left. All source
    roles are retained; uptake and terminal acetaldehyde oxidation are outside this
    boundary.
  snapshot_sha256: c515d4778a7c92d66060ceeffac95c89149cc5400e388e1110fc2cd95fc040a6
- evidence_id: e-boundary
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY0-1297
  locator: PWY0-1297 reaction-list; separately inspected PWY-7179 and PWY-7180 full
    reaction-lists and comments
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: The broader MetaCyc superpathway expands to seven reactions, including
    acetaldehyde oxidation. It is not exact identity for this six-step PathBank pathway.
    GO parent and adjacent pyrimidine or ribonucleoside routes are also not substituted.
  snapshot_sha256: 1bca1d324702af426153ad98dd6a14bbea6020d7682b0a159e85a07f67b040b8
- evidence_id: e-rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: 'Complete Rhea142 RDF: masters28190,27742,27750,27738,27658,12821 and selected
    directed members; directionalReaction/bidirectionalReaction, substrates/products,
    contains1, compound and chebi'
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Independently streamed full raw RDF and directions TSV. All six master-relative
    directions are left-to-right; native6068 reverse orientation yields identical
    deamination chemistry. All22 chemical-side locators and coefficients match; six
    elemental/charge balances pass with complete ChEBI authority.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-uniprot
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22333.json
  locator: Full P22333 comments2/3 and entryAudit; separately inspected P0ABP8 comments6/7/8/10,
    P0A6K6 comments1/3, P0A6L0 comments1/4; exact organism, proteinDescription and
    cytosol GO cross-references
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: All four reviewed K-12 accessions and canonical labels match. Exact reaction
    annotations are experimentally attributed where stated. Add Zn is ECO0000255 HAMAP
    MF00540 inference; DeoB alternative activators are separately qualified from by-similarity
    occupancy; DeoC monomer/homodimer alternatives retained. UniProt2026_03 is supported
    by retained release headers.
  snapshot_sha256: 23e32e2f4a9fc0b04d71ef7ccef5441c01b1b100951453b1f47d623fe4782181
- evidence_id: e-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:DEOD-CPLX
  locator: DEOD-CPLX component coefficient6, native reaction links and CCO-CYTOSOL;
    all four monomer UniProt unifications and TAX511145 species; ADDALT-ENZRXN physiology/evidence
    slot
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Six DEOD-MONOMER copies form the named complex; PathBank independently
    agrees. Native MG1655 component annotations bridge reviewed K-12 entries without
    claiming experimental whole-route MG1655 flux. Add and DeoC use functional enables
    edges where a unique physical assembly is not established.
  snapshot_sha256: f362dcc29babaf5d23e730a329a7c436a0944d811a36ad1adb8ee8569e7962e5
- evidence_id: e-pnp-abstract
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/235429/
  locator: EuropePMC retained indexed primary abstract resultList.result[0].abstractText
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Inspected primary abstract describes six equal probably identical PNP subunits
    and association experiments suggesting the hexamer is active. This supports the
    native assembly rather than asserting three directly re-inspected deoxy-substrate
    assays.
  snapshot_sha256: 27b6d685708a8029c74c2b075ce547478d088766ce3af6011bbd22db57458432
- evidence_id: e-deob-primary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/1089430/
  locator: EuropePMC retained indexed primary abstract resultList.result[0].abstractText
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Inspected primary abstract describes four purified phosphodeoxyribomutase
    forms each as a single polypeptide chain of about45kDa, with differing cobalt-binding
    properties. This supports the single-protein catalytic representation.
  snapshot_sha256: b43ff5def2d79a3a67e05538ff51ae632c8f72fa957138e597467294d00c84e2
- evidence_id: e-deoc-primary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/6749498/
  locator: EuropePMC retained indexed primary abstract resultList.result[0].abstractText
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Inspected K-12 primary abstract preserves monomer and dimer forms; native
    discussion adds buffer dependence. Salmonella active-site inference is not transferred.
  snapshot_sha256: 62d1dc57a84eb2477f4bef142fb3d8f84681b7e628439c2838294a3d35d12f89
- evidence_id: e-deoc-cleavage
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/7675789/
  locator: EuropePMC retained indexed primary abstract resultList.result[0].abstractText
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Inspected primary abstract states reversible exact deoxyribose5-phosphate
    cleavage to glyceraldehyde3-phosphate and acetaldehyde; asymmetric-unit copy count
    is not used as a physiological assembly claim.
  snapshot_sha256: f95a349302cf3e77b3e883f012cfa00eb0b898c39b87a01280fc0f0afa6c3722
- evidence_id: e-pnp-full
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6193948/
  locator: Relevant full-text Results and Discussion crystal structures paragraph
    beginning All PNP structures, assay context and concluding architecture discussion;
    PMID30337572
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Primary full text corroborates a trimer-of-dimers PNP assembly and catalytic
    structural interpretation. Wild-type/mutant and ribonucleoside/analogue assay
    scope is retained; this is not direct measurement of every deoxy substrate or
    native whole-route flux. Live primary PMC page also independently corroborated
    citation identity.
  snapshot_sha256: 0c51eed472206bdb260953635e23b7354cf89098eb6abc75e21c6c0bc8e1fd63
- evidence_id: e-replay
  kind: validation
  reference: research/pathway_additions/2026-10-10-next-cohort/purine-independent-review-audit.json
  locator: Independent replay result, all49 edge-group assessments, raw body/reference
    hashes, initial-input parity and complete chemical replay
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Independent replay passed. Native reaction/catalyst objects, exact source
    locators, ontology labels, species bridges and29 reference hashes were checked.
    Scratch initial syntax failure and correction are retained honestly.
  snapshot_sha256: 0ca1bc14205e935db994b3efde504ffad7236a4af0fe07ea6ef8c7eb0786eabc
- evidence_id: e-context
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/43/genes
  locator: Exact add/b1623 and deoB/b4383 rows in k43; deoC/b4381 in k33; eight relevant
    gene/locus search bodies and full acquisition receipts
  accessed_at: '2026-10-11T01:22:29Z'
  support: context_only
  summary: Applicable raw API rows agree with preserved summaries. Broad add search
    also matches other genes, so exact loci are used. All38 retained bodies were independently
    rehashed. Membership supplies computational expression context only; zero module-name
    hits do not establish absence.
- evidence_id: e-search
  kind: search
  reference: research/pathway_additions/2026-10-10-next-cohort/purine-deoxy-search-ledger.json
  locator: Author ignored-inclusive ledger and reviewer independent exact ID/member/name
    search across data,research,reports,reviews
  accessed_at: '2026-10-11T01:22:29Z'
  support: context_only
  summary: Prior archive-screening appearances were candidates, not existing records.
    Exact maintained matching path is this new record; existing pyrimidine deoxy and
    yeast nucleotide routes have distinct substrate and endpoint boundaries. Original
    Documents checkout access remains unavailable.
  search_scope: rg --no-ignore --hidden -n -i -g '!.git/**' -g '!.venv/**' 'SMP0002089|PW002077|purine
    deoxyribonucleosides degradation|PWY0-1297' data research reports reviews; accessible
    worktree only, hidden and ignored included.
  snapshot_sha256: 043d2e3782edbb1fa530a7d43e317b854a59587727eb3f69e41023a8aeaee13c
- evidence_id: e-gates
  kind: validation
  reference: research/pathway_additions/2026-10-10-next-cohort/integration-validation.json
  locator: Final actual terminal receipts, independently read/rehashed logs and final
    graph/KGX scoped audit
  accessed_at: '2026-10-11T01:22:29Z'
  support: supports
  summary: Parent executed complete final corpus gates. Reviewer checked exact results
    and log hashes, and target49-edge/80-evidence graph preservation. These deterministic
    checks do not scientifically review other records.
  snapshot_sha256: dd58a6913ed745f8d941ef6fa15118c9d9b6e8e20182b366c55596bf8a8b408d
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact native six-reaction boundary
  outcome: supported
  summary: PathBank identity preserves the complete assigned route and all parallel
    substrates. The larger MetaCyc superpathway and generic GO process are contextual,
    not asserted exact matches. No convenient partial module was substituted.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-record
  - e-pathbank
  - e-boundary
  - e-search
- assessment_id: a-chemistry
  area: representation
  topic: Precise species, direction families and balances
  outcome: supported
  summary: All22 chemical edges match exact Rhea species, coefficients and side locators;
    all six balances pass. Broad/uncharged native chemical forms are normalized through
    exact enzyme/Rhea grounding, not asserted identical to differently charged or
    stereochemically incomplete species. Five provides_input_for edges use identical
    shared intermediates.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-pathbank
  - e-rhea
  - e-replay
- assessment_id: a-catalysts
  area: evidence
  topic: Correct catalytic entities and physical assembly limits
  outcome: supported
  summary: DeoD complex is the catalyst for all three phosphorolyses; its subunit
    only has membership. DeoB single-chain primary evidence supports its catalyzes
    edge. Add and DeoC use qualified functional roles; buffer-dependent monomer/dimer
    evidence is preserved.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-native
  - e-uniprot
  - e-pnp-abstract
  - e-pnp-full
  - e-deob-primary
  - e-deoc-primary
  - e-deoc-cleavage
- assessment_id: a-scope
  area: scope
  topic: Taxon, cofactors and localization evidence
  outcome: supported
  summary: MG1655 component annotations are explicit, K-12 source entry scope and
    experimental limits remain visible, and no whole-route in-vivo flux is asserted.
    Add zinc sequence inference and alternative DeoB metal activities retain their
    grades. Exact UniProt IDA:EcoCyc cytosol annotations and native complex location
    support bounded compartment assertions.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-native
  - e-uniprot
  - e-replay
- assessment_id: a-provenance
  area: provenance
  topic: Nearest inspected source and complete references
  outcome: supported
  summary: All49 edges and80 evidence blocks are supported at their actual native
    or primary locators. Six pathway-membership bridges explicitly cite Rhea master
    directionalReaction and bidirectionalReaction properties as needed. Inaccessible
    full texts are not represented as inspected experimental evidence; all29 retained
    reference digests match actual source bodies.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-record
  - e-replay
  - e-native
  - e-rhea
  - e-pnp-full
- assessment_id: a-context
  area: evidence
  topic: Structured expression cross-check
  outcome: supported
  summary: Exact iModulon context memberships agree with retained source bodies and
    do not create catalytic, regulatory, directional or flux assertions. Console availability
    limitation and successful direct-client fallback are explicit.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-context
- assessment_id: a-integration
  area: graph
  topic: Final gates and generated evidence preservation
  outcome: supported
  summary: Final required gates passed and the programmatic SVG/KGX audit preserves
    all49 target edges and80 evidence blocks, including source metadata and context.
    Browser interaction and visual layout were not assessed.
  target_ids:
  - PathBank:SMP0002089
  evidence_ids:
  - e-gates
  - e-record
findings: []
actions: []
limitations:
- PathBank is the retained 2019 archive member; MetaCyc is the explicit public 22.5
  snapshot. Current reviewed UniProt 2026_03 complements these sources without a newest
  licensed MetaCyc claim.
- Several older primary full texts were unavailable. Substantive abstracts for PMID235429,1089430,6749498,7675789
  and relevant full-text sections of PMC6193948 were inspected. Detailed PMID357905/4992818
  claims remain attributed to exact inspected UniProt/native slots; metadata is not
  experimental text.
- MG1655 native component annotations, K-12 reviewed entries and older E. coli experiments
  are distinct scopes; complete native MG1655 pathway flux is not established. Add
  zinc is sequence inference; alternative DeoB metal activities do not establish physiological
  metal occupancy; DeoC assembly is condition dependent.
- Canonical iModulon console invocation failed before retrieval because dotenv was
  missing; root successfully called the unchanged direct client. Reviewer rehashed
  all 38 raw responses and checked applicable searches and exact component rows. Expression
  evidence is context only and search misses are not biological absence.
- Original Documents checkout was inaccessible; hidden/ignored-inclusive search covers
  the accessible worktree data, research, reports and reviews. Browser surfaces were
  unavailable; graph QA is programmatic, not visual or interactive.
- This bounded review does not establish exhaustive literature coverage or source
  exhaustion.
notes:
- Initial governed inspect target SHA1412ec0cdb11458da71fd9b50a8c0827effefe28fe9ac949213db928d1e26087
  remained unchanged. All eight initially captured inputs remained byte-identical
  through final recheck.
- Reviewer scratch replay initially failed with a missing closing parenthesis before
  running any assertions. The syntax was corrected and the complete independent replay
  subsequently exited0; no target changes resulted.
- Issue335 concerns the separate reviewer-authored pyrimidine route and is neither
  a purine finding nor reviewed here as an independent author assessment.
tags:
- pathway
- purine-deoxyribonucleosides
- independent
- scientific-review
```
