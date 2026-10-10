# Independent scientific review of methylglyoxal degradation III

- Review: 20261010T234335Z-methylglyoxal-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-10T23:31:32Z
- Finished UTC: 2026-10-10T23:43:35Z
- Reviewer: Codex independent methylglyoxal reviewer (/root/pathway_authority_cache) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded E. coli MG1655 annotation for the acetol branch is supported. Every one of 17 edges and 25 evidence blocks was assessed; all ten chemical-side assertions match exact Rhea objects, coefficients and source locators. No corrective finding was identified. Stereochemistry remains explicitly a reviewed database assignment, and enzyme/strain/assembly/physiological limitations are preserved.

## Scope And Provenance

One complete maintained pathway record, including identity, every participant/reaction/edge/reference, source exclusions and generated representation.

Selection: Exact assigned file data/pathways/methylglyoxal-degradation-iii.yaml and MetaCyc:PWY-5453.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base dbf399e6ac90f6240fa5da2fac27386d49966171.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5453 | data/pathways/methylglyoxal-degradation-iii.yaml | maintained | methylglyoxal degradation III |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Initial governed-inspect path attempt | failed | False | MetaCyc:PWY-5453 | Exit 1 because the schema symlink was resolved incorrectly; canonical maintained src/pathwaymech/schema/pathwaymech.yaml used successfully next. Target untouched. |
| Governed initial capture | passed | False | MetaCyc:PWY-5453 | Exit 0 before assessment, frozen target captured with then-current shared authority inputs. |
| Initial source-manifest scratch replay | failed | False | MetaCyc:PWY-5453 | Exit 1 after all chemical checks: optional status key absent on native/archive source entries. Corrected reviewer harness; not a record defect. |
| Second scratch replay metadata correction | failed | False | MetaCyc:PWY-5453 | Exit 1 because filtering status 200 skipped a separately acquired successful primary body. Rehashed every source with a declared digest instead; target and source inputs unchanged. |
| Final comparison environment probe | failed | False | MetaCyc:PWY-5453 | System Python lacked PyYAML and exited 1 before reading inputs. The same probe completed with repository .venv and confirmed only the two authority files changed. |
| Partial review schema preflight | failed | False | MetaCyc:PWY-5453 | Initial unsaved draft exited 1 for missing explicit search_scope field on search evidence. Added the already documented bounded scope; no scientific input changed. |
| Independent source/chemistry replay | passed | False | MetaCyc:PWY-5453 | Exit 0: ten exact chemical sides, two balances, 22 source/member hashes, all native/protein locator assertions and local schema. |
| Canonical expression context 0 | failed | False | MetaCyc:PWY-5453 | Superseded by authorized network retry; no source change |
| Canonical expression context 1 | passed | True | MetaCyc:PWY-5453 | Actual output inspected and hashed; gene context only. |
| Canonical expression context 2 | passed | True | MetaCyc:PWY-5453 | Actual output inspected and hashed; gene context only. |
| Canonical expression context 3 | passed | True | MetaCyc:PWY-5453 | Actual output inspected and hashed; gene context only. |
| Canonical expression context 4 | passed | True | MetaCyc:PWY-5453 | Actual output inspected and hashed; gene context only. |
| iModulon summarize | not_applicable | False | MetaCyc:PWY-5453 | No module hits returned; no informative component to summarize. |
| Final integration validate | passed | True | MetaCyc:PWY-5453 | 169 native and closed records, identifier/label policy, 8834 evidence blocks, 251 histories, 30 source records, 6 documentation files, research contract and current pages all pass. |
| Final integration render | passed | True | MetaCyc:PWY-5453 | Rendered 169 records. |
| Final integration lint | passed | True | MetaCyc:PWY-5453 | All Ruff checks passed. |
| Final integration vendored | passed | True | MetaCyc:PWY-5453 | 22 governed artifacts match the pinned canonical revision. |
| Reviewer whitespace diff | passed | True | MetaCyc:PWY-5453 | Exit0 on final integration changes at review time. |
| Reviewer whitespace diff-staged | passed | False | MetaCyc:PWY-5453 | Exit0 on final integration changes at review time. |
| Generated SVG and KGX artifact audit | passed | False | MetaCyc:PWY-5453 | Actual structural audit passed; exact page and YAML bytes independently rehashed by reviewer. |
| Separate actual CLI KGX export | passed | False | MetaCyc:PWY-5453 | Separate export bytes match published downloads; all target evidence metadata is preserved. |
| Final governed inspect and reassessment | passed | False | MetaCyc:PWY-5453 | Target/research/schema inputs unchanged. The two authority snapshots changed since initial capture; reviewer assessed additive term/source preservation, exact target identities and rehashed all new manifest bodies before retaining their final hashes. Final generated/context inputs were inspected and captured. |
| Superseded full test before rendering finished | failed | False | MetaCyc:PWY-5453 | 1042 passed,1 failed,3 skipped; sole stale generated-index failure in test_rendered_site_publishes_the_index_and_it_is_current. Preserved honestly as the initial mixed-state attempt, not the final frozen-input gate. |
| Final full test on frozen inputs | passed | True | MetaCyc:PWY-5453 | 1043 passed, 3 skipped, 3 upstream deprecation warnings in 242.23 seconds. Terminal exit 0 from session88101; final complete suite supersedes the before-render attempt. |
| Corrected partial draft preflight | passed | False | MetaCyc:PWY-5453 | External unsaved partial-draft contract validation passed after adding the explicit bounded search scope. Final completed validation follows all actual terminal gates. |

## Scientific And Domain Assessments

### Exact acetol-branch pathway identity and scope

identity: supported. Targets: MetaCyc:PWY-5453.

The record is the supported MG1655 annotation for native PWY-5453, with two distinct enzymatic reductions. It is not the yeast glutathione route, glycerol utilization, lactaldehyde branch or an all-organism statement.

### All chemical identities, coefficients and selected directions

grounding: supported. Targets: MetaCyc:PWY-5453.

Edges 001–010 exactly cover both directed Rhea equations; all coefficients are 1 and both atom/charge sums are zero. NADPH/NADP and NADH/NAD are correctly distinguished. Right-to-left metadata on 27988 is relative to its master oxidation equation.

### Gpr and GldA catalytic support

evidence: supported. Targets: MetaCyc:PWY-5453.

Edges 011/012 use direct purified YghZ evidence plus exact reviewed reaction assertions. The Gpr enables relation preserves function without inventing a monomeric physical catalyst. GldA catalysis is assigned to its native complex with an exact P0A9S5 component bridge; uninspected full papers are not presented as direct reviewer observations.

### Assembly and cofactor roles

representation: supported. Targets: MetaCyc:PWY-5453.

Edges 013/014 retain GldA complex membership and supported bound zinc while explicitly preserving variable oligomers and the modeled-NAD limitation. They do not infer a fixed octamer requirement, generic Mg cofactor, or metal-rescue result.

### Stereochemistry and physiology limits

scope: supported. Targets: MetaCyc:PWY-5453.

The S product is retained as a source annotation, not newly proven by NMR. R-diol in the AG1 study is scoped to its proposed lactaldehyde pathway. Native unrestricted MG1655 flux, exclusive Gpr roles and invariant stoichiometry are not asserted.

### Membership and direct shared intermediate

graph: supported. Targets: MetaCyc:PWY-5453.

Edges 015–017 match native reaction-list and ordering, with exact acetol output/input. The material link is not equated with a purified full-pathway reconstitution. Unsupported transport and neighboring pathways are explicitly excluded.

### Identifier and evidence fidelity

provenance: supported. Targets: MetaCyc:PWY-5453.

All references, native object locators and digests were checked; database statements remain attributed to the inspected databases. Final authority additions preserve baseline coverage and source provenance.

### Bounded expression-database context

scope: supported. Targets: MetaCyc:PWY-5453.

Required adapter retrieval succeeded after sandbox DNS retry. Exact gene matches add context, while no module hit or synonym miss changes the scientific interpretation.

### Validated publication representation

consistency: supported. Targets: MetaCyc:PWY-5453.

Final delegated corpus gates and the generated artifact audit pass on frozen inputs; technical consistency is separate from the scientific judgement.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/methylglyoxal-degradation-iii.yaml; Entire YAML: 12 participants, two reactions, one taxon, pathway identity, 17 edges, 25 evidence blocks and 12 references | supports | Governed input capture preceded assessment. Every local endpoint, identifier, evidence claim and source limitation was inspected. Target SHA remained unchanged throughout review. |
| e-native | https://pathway.yeastgenome.org/getxml?META:PWY-5453; Pathway common-name, species TAX-511145, reaction-list/layout/ordering; RXN0-4281 and RXN-8632 exact chemical sides, direction and Rhea cross-references | supports | The native acetol route is distinct from glutathione-dependent glyoxalase and glycerol degradation. Both native reactions select reduction; their master orientations differ from each other. The multispecies pathway is explicitly narrowed to E. coli MG1655 annotation. |
| e-complex | https://pathway.yeastgenome.org/getxml?META:GLYCDEH-CPLX; RXN-8632/ENZRXN0-6324/enzyme; GLYCDEH-CPLX component/comment/coefficient; GLYCDEH-MONOMER UNIPROT dblink | supports | The exact native GldA complex is the RXN-8632 catalyst and contains the monomer cross-referenced to P0A9S5. Native coefficient eight coexists with an explicit active-dimer note. Membership is retained without invariant oligomer stoichiometry. |
| e-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Release 142 masters 27986/28667; directed 27988/28668; substrates/products/contains1/Participant/compound/chebi and exact formula/charge values | supports | Fresh complete-RDF extraction merges repeated descriptions for each subject. Every one of ten retained chemical-side occurrences matches the target locator and coefficient. Both reactions balance by atoms and charge against independently queried ChEBI255. The whole gzip body was independently rehashed. |
| e-proteins | https://rest.uniprot.org/uniprotkb/Q46851.json; Reviewed 2026_03 Q46851 and P0A9S5 accession/taxon/genes; comments[2].reaction; P0A9S5 comments[4] cofactor/note and comments[8] subunit | supports | Gpr/YghZ/b3001 and GldA/b3945 resolve exactly. Reviewed reaction assignments match the selected Rhea families; GldA specifies S-diol. Zinc cofactor ECO:0000305 is distinguished from the binding-note ECO:0000269. Gpr tetramer/octamer reports and its more efficient L-GAP reaction remain qualified. |
| e-primary2005 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1196063/; Methods strain/cloning/NMR/assays; Results Figure 2, purified-AKR Figure 3B, Table 2 and mutant Figure 5 | supports | Purified MG1655-derived YghZ produces acetol using NADPH. NADH activity is below 3% and reverse reaction was undetected under tested conditions. CK281 engineered cells and crude extracts yield acetol then diol; purified AKRs do not yield detectable diol. Those measurements neither resolve diol enantiomers nor reconstitute the complete two-enzyme pathway. |
| e-primary2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6404857/; Methods 2.2 and Results 3.1/3.3; Figure 1b and Figure 3 descriptions | supports | The sequence-verified MG1655 gldA construct was expressed in BL21. Purified enzyme is tetrameric in 5% glycerol; the paper contrasts prior dimer/octamer mixtures. Active-site zinc is coordinated by His254/His271/Asp171 and interacts with glycerol. NAD+ was modeled, not observed in this crystal. |
| e-primary1999 | https://pmc.ncbi.nlm.nih.gov/articles/PMC91161/; Methods enantiomeric GC and MG1655 gldA cloning; Results Table 5; Discussion/Figure 2 | context_only | Engineered AG1 strains make R-diol. The proposed route uses R-lactaldehyde; purified-enzyme experiments use Klebsiella glycerol dehydrogenase. This is important context but does not directly test or refute an isolated E. coli GldA acetol-to-S-diol assignment. |
| e-abstracts | https://pubmed.ncbi.nlm.nih.gov/18179582/; Complete indexed/publisher abstract 18179582; indexed abstracts 18620424,6365902,40950,3920199 | context_only | The abstract-only evidence supports broad GldA substrate/physiological context and variable assemblies. The 6365902 abstract permits both NADH and NADPH for hydroxyacetone reduction, so the selected NADH branch is not exclusivity. No full-text acetol-specific assay or enantiomer proof is claimed from 18179582. |
| e-pathbank | https://pathbank.org/downloads/pathbank_primary_biopax.zip; Native member PW002079.owl: biochemical membership/controllers, transport 10317 and pathway identity SMP0002091 | context_only | The two-step native lead is consistent with the independent MetaCyc boundary. Unsupported transport and periplasmic placement are omitted with a recorded disposition, not treated as evidence that transport is biologically absent. |
| e-replay | /private/tmp/pathwaymech-next-mg-review/replay.json; Reviewer extraction/replay source, actual raw response digests, native XML/UniProt crosswalks and ChEBI formulas/charges | supports | Independent replay passes all 17 edges/25 evidence structure, ten chemical occurrences, two balances, 22 source/member digests, exact native pathway ordering and protein/component locators. Primary interpretation was checked separately from this deterministic script. |
| e-context | research/pathway_additions/2026-10-10-next/methylglyoxal-review-context.json; Canonical datasets and precise_mg1655 searches gpr,yghZ,gldA; preserved output hashes | context_only | gpr and gldA return expected b3001/b3945 loci and zero module hits. yghZ returns no name match while current synonym gpr resolves. No component requires summarize. These contextual results are not catalysis, stereo, flux or absence evidence. |
| e-identity-search | /private/tmp/pathwaymech-next-mg-review/duplicate-review.txt; Ignored/hidden-inclusive exact identity search over data/pathways,research,reviews,reports; author both-root search receipts and closest glycerol/yeast-methylglyoxal records | supports | Exact target identity appears in this addition and source leads. Independently read neighboring records have distinct reaction sets, products and taxon/branch boundaries. Search scope excludes Git internals and virtual environments; no fleet-wide absence claim is made. |
| e-authorities | research/pathway_additions/2026-10-10-next/authority-integration.json; Final source/ontology JSON compared with Git basedbf399e; all 11 new manifest cache bodies independently rehashed | supports | All 1319 baseline ontology and1622 source terms and their prior source metadata are unchanged. Final totals 1331/1633 include exact new target labels. Rhea 139 identity authority is distinguished from explicitly versioned Rhea 142 mechanistic RDF; no existence waiver or handpatched authority is introduced. |
| e-gates | /private/tmp/pathwaymech-next-{validate,test,lint,render,vendored}.log; Actual integration-agent terminal gate logs and exit receipts; reviewer read final outputs | supports | Final frozen-input corpus gates are delegated to the integration agent. Their actual exit results and logs were inspected; they establish technical consistency, separate from the scientific source review. |
| e-generated | research/pathway_additions/2026-10-10-next/generated-graph-kgx-audit.json; Actual CLI export, published TSV downloads, record SVG nodes/edges/evidence anchors and metadata | supports | Methylglyoxal retains all 16 named nodes including scope taxon, 15 drawn nodes, 17 edges and 25 evidence blocks. Complete KGX evidence/description/category/context and exact SVG endpoints/anchors/bounds pass. Reviewer independently rehashed actual target/page against the receipt. No browser visual inspection is claimed. |
| e-initial-test | /private/tmp/pathwaymech-next-test-before-render.log; Final pytest failure and summary; test_cross_mech.py:371 index comparison | context_only | Initial full run exited1:1042 passed,1 failed,3 skipped,3 warnings in418.31s. The failure compared the prior generated index against newly added records. Integration owner confirms this run began before rendering completed. The current-site validation subsequently passed; a complete frozen-input rerun is retained separately. |

## Limits And Additional Notes

- PMID18179582 and several older GldA studies were inspected as complete indexed/publisher abstracts, not full experimental papers. The retained exact GldA activity is attributed to inspected UniProt and native MetaCyc statements.
- The (S)-diol node is a current Rhea/UniProt/native annotation. Inspected 2005 NMR did not resolve enantiomers; 1999 engineered R-diol production follows a proposed lactaldehyde route. This review does not newly establish acetol-step absolute stereochemistry.
- Gpr has other substrates and parallel methylglyoxal reductases exist. GldA assembly depends on conditions; the record does not fix all active enzyme as an octamer. Zinc binding is supported structurally, while an acetol-specific metal removal/rescue assay was not inspected.
- MG1655 source genes/native annotations are distinguished from CK281 engineered metabolic measurements and AG1 overexpression results. Native unrestricted flux, exclusivity and transport are not established.
- Generated graphics were checked structurally through actual SVG/evidence/KGX artifacts; no interactive browser visual review is claimed.
- No target YAML, authority configuration, generated page, history entry or GitHub state was edited by this review. Generated pages are owned by the target YAML plus src/pathwaymech rendering/graph code; fixes must not patch pages directly.
- The cobalamin research handoff in this batch is unrelated scientific work and does not count as pathway coverage or exhausted-source evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T234335Z-methylglyoxal-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of methylglyoxal degradation III
started_at: '2026-10-10T23:31:32Z'
finished_at: '2026-10-10T23:43:35Z'
reviewer:
  identity: Codex independent methylglyoxal reviewer (/root/pathway_authority_cache)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: A different agent authored this target and its mechanistic research.
    This reviewer did not edit the target or its source projections and independently
    inspected the raw primary/native sources and replayed exact chemistry. This reviewer
    authored separate cobalamin research and the review context receipt in this batch;
    prior merged authority-parser work is disclosed and is not the basis for scientific
    independence.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded E. coli MG1655 annotation for the acetol branch is supported.
  Every one of 17 edges and 25 evidence blocks was assessed; all ten chemical-side
  assertions match exact Rhea objects, coefficients and source locators. No corrective
  finding was identified. Stereochemistry remains explicitly a reviewed database assignment,
  and enzyme/strain/assembly/physiological limitations are preserved.
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
  - path: data/pathways/methylglyoxal-degradation-iii.yaml
    sha256: 904a0f1aabfc7ba215fa1c933357715414a0f0cbed8ec130f84420b07812a688
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 3c861f2ab78e3bc62146d05af5ed5c4c4ae3e65343fc9bd44afa76da7f0b62e7
    role: context
  - path: pages/records/MetaCyc_PWY-5453.html
    sha256: 01945f8a61b5767e4fe3eb9e79a6e068689bc1464700c47a5bad093f30e63e52
    role: context
  - path: research/pathway_additions/2026-10-10-next/authority-integration.json
    sha256: 76e569ddf2e9ba12dbfa6592036e78938aef8f3fd91ccf8dca9c5b1c6d09d189
    role: context
  - path: research/pathway_additions/2026-10-10-next/generated-graph-kgx-audit.json
    sha256: 2b3d20a77b87b26b17e1843e6db9910226afdb93799739400bbb4de57c773af7
    role: context
  - path: research/pathway_additions/2026-10-10-next/methylglyoxal-chemistry.json
    sha256: 268d3d4acca0248d5246aed30e1086d01b565b3378bf346e704ed4d892cce4df
    role: context
  - path: research/pathway_additions/2026-10-10-next/methylglyoxal-curation.md
    sha256: 4c68c97c3e0ac1a570c3fee05983b90759d8cb6f730b16564e57e5f0b7e80caa
    role: context
  - path: research/pathway_additions/2026-10-10-next/methylglyoxal-native-projection.json
    sha256: 6c048fc00334596ebe0584fc3621fc4da818ea10ce951f4605bbe6aa7b8215da
    role: context
  - path: research/pathway_additions/2026-10-10-next/methylglyoxal-protein-projection.json
    sha256: c55c86f4a5a364722841c48904eab7470cd41426102ef0d3dbc1c60f598a4eac
    role: context
  - path: research/pathway_additions/2026-10-10-next/methylglyoxal-review-context.json
    sha256: 14f07d92fba0ca691397cef0a86e17c6baea67a87652b40002b36560991a6a4f
    role: context
  - path: research/pathway_additions/2026-10-10-next/methylglyoxal-sources.json
    sha256: 4a735fd820485b86226d6af97d36776ec9c439aca759def998ccc7d561a463af
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: One complete maintained pathway record, including identity, every participant/reaction/edge/reference,
    source exclusions and generated representation.
  selection: Exact assigned file data/pathways/methylglyoxal-degradation-iii.yaml
    and MetaCyc:PWY-5453.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5453
  exclusions:
  - target: All other pathway records, including riboneogenesis
    reason: Their scientific correctness is outside this target review; corpus gates
      provide technical consistency only.
  - target: Uninspected full papers and all unobserved native flux conditions
    reason: No exhaustive literature or physiological claim. Abstract-only papers
      and context studies are identified explicitly.
targets:
- target_id: MetaCyc:PWY-5453
  path: data/pathways/methylglyoxal-degradation-iii.yaml
  label: methylglyoxal degradation III
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylglyoxal-degradation-iii.yaml
    role: maintained_curation
checks:
- check_id: c-inspect-path
  name: Initial governed-inspect path attempt
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: Exit 1 because the schema symlink was resolved incorrectly; canonical maintained
    src/pathwaymech/schema/pathwaymech.yaml used successfully next. Target untouched.
  evidence_ids:
  - e-record
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-mg-review-targets.yaml
    --input src/pathwaymech/schema.py --input schema/pathwaymech.yaml --input conf/identifier_policy.yaml
    --input data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-curation.md --input
    research/pathway_additions/2026-10-10-next/methylglyoxal-sources.json --input
    research/pathway_additions/2026-10-10-next/methylglyoxal-native-projection.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-protein-projection.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-chemistry.json
  exit_code: 1
  expected_exit_code: 0
- check_id: c-inspect
  name: Governed initial capture
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: Exit 0 before assessment, frozen target captured with then-current shared
    authority inputs.
  evidence_ids:
  - e-record
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-mg-review-targets.yaml
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
    --input conf/identifier_policy.yaml --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json --input research/pathway_additions/2026-10-10-next/methylglyoxal-curation.md
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-sources.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-native-projection.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-protein-projection.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-chemistry.json
  exit_code: 0
  expected_exit_code: 0
- check_id: c-replay-harness1
  name: Initial source-manifest scratch replay
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: 'Exit 1 after all chemical checks: optional status key absent on native/archive
    source entries. Corrected reviewer harness; not a record defect.'
  evidence_ids:
  - e-replay
  command: .venv/bin/python /private/tmp/pathwaymech-next-mg-review/replay.py
  exit_code: 1
  expected_exit_code: 0
- check_id: c-replay-harness2
  name: Second scratch replay metadata correction
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: Exit 1 because filtering status 200 skipped a separately acquired successful
    primary body. Rehashed every source with a declared digest instead; target and
    source inputs unchanged.
  evidence_ids:
  - e-replay
  command: .venv/bin/python /private/tmp/pathwaymech-next-mg-review/replay.py
  exit_code: 1
  expected_exit_code: 0
- check_id: c-python-probe
  name: Final comparison environment probe
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: System Python lacked PyYAML and exited 1 before reading inputs. The same
    probe completed with repository .venv and confirmed only the two authority files
    changed.
  evidence_ids:
  - e-record
  command: python3 -
  exit_code: 1
  expected_exit_code: 0
- check_id: c-draft-schema
  name: Partial review schema preflight
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: Initial unsaved draft exited 1 for missing explicit search_scope field
    on search evidence. Added the already documented bounded scope; no scientific
    input changed.
  evidence_ids:
  - e-identity-search
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py validate /private/tmp/pathwaymech-next-mg-review/partial-preflight.yaml
  exit_code: 1
  expected_exit_code: 0
- check_id: c-replay
  name: Independent source/chemistry replay
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: 'Exit 0: ten exact chemical sides, two balances, 22 source/member hashes,
    all native/protein locator assertions and local schema.'
  evidence_ids:
  - e-replay
  - e-rhea
  command: .venv/bin/python /private/tmp/pathwaymech-next-mg-review/replay.py
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-0
  name: Canonical expression context 0
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: Superseded by authorized network retry; no source change
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 2
  expected_exit_code: 0
- check_id: c-context-1
  name: Canonical expression context 1
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-5453
  summary: Actual output inspected and hashed; gene context only.
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-2
  name: Canonical expression context 2
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-5453
  summary: Actual output inspected and hashed; gene context only.
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise_mg1655 --query gpr
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-3
  name: Canonical expression context 3
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-5453
  summary: Actual output inspected and hashed; gene context only.
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise_mg1655 --query yghZ
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-4
  name: Canonical expression context 4
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-5453
  summary: Actual output inspected and hashed; gene context only.
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise_mg1655 --query gldA
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-summary
  name: iModulon summarize
  status: not_applicable
  required: false
  target_ids:
  - MetaCyc:PWY-5453
  summary: No module hits returned; no informative component to summarize.
  evidence_ids:
  - e-context
- check_id: c-validate
  name: Final integration validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: 169 native and closed records, identifier/label policy, 8834 evidence blocks,
    251 histories, 30 source records, 6 documentation files, research contract and
    current pages all pass.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; actual terminal
    exit receipt and output log independently inspected rather than duplicating corpus
    checks.
- check_id: c-render
  name: Final integration render
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: Rendered 169 records.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; actual terminal
    exit receipt and output log independently inspected rather than duplicating corpus
    checks.
- check_id: c-lint
  name: Final integration lint
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: All Ruff checks passed.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; actual terminal
    exit receipt and output log independently inspected rather than duplicating corpus
    checks.
- check_id: c-vendored
  name: Final integration vendored
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: 22 governed artifacts match the pinned canonical revision.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; actual terminal
    exit receipt and output log independently inspected rather than duplicating corpus
    checks.
- check_id: c-diff
  name: Reviewer whitespace diff
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: Exit0 on final integration changes at review time.
  evidence_ids:
  - e-record
- check_id: c-diff-staged
  name: Reviewer whitespace diff-staged
  status: passed
  required: false
  command: git diff --cached --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: Exit0 on final integration changes at review time.
  evidence_ids:
  - e-record
- check_id: c-graph
  name: Generated SVG and KGX artifact audit
  status: passed
  required: false
  command: /private/tmp/pathwaymech-next-graph-audit.py --root /private/tmp/pathwaymech-next-20261010
    --comparison-kgx-dir /private/tmp/pathwaymech-next-kgx
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: Actual structural audit passed; exact page and YAML bytes independently
    rehashed by reviewer.
  evidence_ids:
  - e-generated
  scope_note: Delegated programmatic artifact check, not browser visual inspection
    or primary scientific evidence.
- check_id: c-kgx
  name: Separate actual CLI KGX export
  status: passed
  required: false
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-kgx
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: Separate export bytes match published downloads; all target evidence metadata
    is preserved.
  evidence_ids:
  - e-generated
- check_id: c-input-final
  name: Final governed inspect and reassessment
  status: passed
  required: false
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-mg-review-targets.yaml
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
    --input docs/CAUSAL_GRAPHS.md --input conf/identifier_policy.yaml --input conf/identifier_sources.json
    --input data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input pages/records/MetaCyc_PWY-5453.html --input research/pathway_additions/2026-10-10-next/methylglyoxal-curation.md
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-sources.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-native-projection.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-protein-projection.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-chemistry.json
    --input research/pathway_additions/2026-10-10-next/methylglyoxal-review-context.json
    --input research/pathway_additions/2026-10-10-next/authority-integration.json
    --input research/pathway_additions/2026-10-10-next/generated-graph-kgx-audit.json
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: Target/research/schema inputs unchanged. The two authority snapshots changed
    since initial capture; reviewer assessed additive term/source preservation, exact
    target identities and rehashed all new manifest bodies before retaining their
    final hashes. Final generated/context inputs were inspected and captured.
  evidence_ids:
  - e-record
  - e-authorities
  - e-generated
- check_id: c-initial-test
  name: Superseded full test before rendering finished
  status: failed
  required: false
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: 1042 passed,1 failed,3 skipped; sole stale generated-index failure in test_rendered_site_publishes_the_index_and_it_is_current.
    Preserved honestly as the initial mixed-state attempt, not the final frozen-input
    gate.
  evidence_ids:
  - e-initial-test
  scope_note: Not used to attest final frozen inputs; the required complete test gate
    is the subsequent rerun.
- check_id: c-test
  name: Final full test on frozen inputs
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: 1043 passed, 3 skipped, 3 upstream deprecation warnings in 242.23 seconds.
    Terminal exit 0 from session88101; final complete suite supersedes the before-render
    attempt.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root after rendering and inputs froze;
    actual final log independently inspected.
- check_id: c-draft-schema-passed
  name: Corrected partial draft preflight
  status: passed
  required: false
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py validate /private/tmp/pathwaymech-next-mg-review/partial-preflight.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - MetaCyc:PWY-5453
  summary: External unsaved partial-draft contract validation passed after adding
    the explicit bounded search scope. Final completed validation follows all actual
    terminal gates.
  evidence_ids:
  - e-record
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/methylglyoxal-degradation-iii.yaml
  locator: 'Entire YAML: 12 participants, two reactions, one taxon, pathway identity,
    17 edges, 25 evidence blocks and 12 references'
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: Governed input capture preceded assessment. Every local endpoint, identifier,
    evidence claim and source limitation was inspected. Target SHA remained unchanged
    throughout review.
  snapshot_sha256: 904a0f1aabfc7ba215fa1c933357715414a0f0cbed8ec130f84420b07812a688
- evidence_id: e-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY-5453
  locator: Pathway common-name, species TAX-511145, reaction-list/layout/ordering;
    RXN0-4281 and RXN-8632 exact chemical sides, direction and Rhea cross-references
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: The native acetol route is distinct from glutathione-dependent glyoxalase
    and glycerol degradation. Both native reactions select reduction; their master
    orientations differ from each other. The multispecies pathway is explicitly narrowed
    to E. coli MG1655 annotation.
  snapshot_sha256: b2797839b180a1ff3be49882b2cb658b7fd0e826a972d29339fec76605beea07
- evidence_id: e-complex
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:GLYCDEH-CPLX
  locator: RXN-8632/ENZRXN0-6324/enzyme; GLYCDEH-CPLX component/comment/coefficient;
    GLYCDEH-MONOMER UNIPROT dblink
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: The exact native GldA complex is the RXN-8632 catalyst and contains the
    monomer cross-referenced to P0A9S5. Native coefficient eight coexists with an
    explicit active-dimer note. Membership is retained without invariant oligomer
    stoichiometry.
  snapshot_sha256: 8f0f6b3c38dbb2084640908e907ab4ac7ff90ac8edb741f766f72202a6f1f5f3
- evidence_id: e-rhea
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Release 142 masters 27986/28667; directed 27988/28668; substrates/products/contains1/Participant/compound/chebi
    and exact formula/charge values
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: Fresh complete-RDF extraction merges repeated descriptions for each subject.
    Every one of ten retained chemical-side occurrences matches the target locator
    and coefficient. Both reactions balance by atoms and charge against independently
    queried ChEBI255. The whole gzip body was independently rehashed.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q46851.json
  locator: Reviewed 2026_03 Q46851 and P0A9S5 accession/taxon/genes; comments[2].reaction;
    P0A9S5 comments[4] cofactor/note and comments[8] subunit
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: Gpr/YghZ/b3001 and GldA/b3945 resolve exactly. Reviewed reaction assignments
    match the selected Rhea families; GldA specifies S-diol. Zinc cofactor ECO:0000305
    is distinguished from the binding-note ECO:0000269. Gpr tetramer/octamer reports
    and its more efficient L-GAP reaction remain qualified.
- evidence_id: e-primary2005
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1196063/
  locator: Methods strain/cloning/NMR/assays; Results Figure 2, purified-AKR Figure
    3B, Table 2 and mutant Figure 5
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: Purified MG1655-derived YghZ produces acetol using NADPH. NADH activity
    is below 3% and reverse reaction was undetected under tested conditions. CK281
    engineered cells and crude extracts yield acetol then diol; purified AKRs do not
    yield detectable diol. Those measurements neither resolve diol enantiomers nor
    reconstitute the complete two-enzyme pathway.
  snapshot_sha256: 7edca4dd5ce4a7ab4903200f3bacbdbc3d35a276cc7a241e7cecd4d3992cd574
- evidence_id: e-primary2019
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6404857/
  locator: Methods 2.2 and Results 3.1/3.3; Figure 1b and Figure 3 descriptions
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: The sequence-verified MG1655 gldA construct was expressed in BL21. Purified
    enzyme is tetrameric in 5% glycerol; the paper contrasts prior dimer/octamer mixtures.
    Active-site zinc is coordinated by His254/His271/Asp171 and interacts with glycerol.
    NAD+ was modeled, not observed in this crystal.
  snapshot_sha256: 40df653530af56649dbfb283428b1e8d9fce15b945ce649c1db8ae7223e0e53e
- evidence_id: e-primary1999
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC91161/
  locator: Methods enantiomeric GC and MG1655 gldA cloning; Results Table 5; Discussion/Figure
    2
  accessed_at: '2026-10-10T23:43:35Z'
  support: context_only
  summary: Engineered AG1 strains make R-diol. The proposed route uses R-lactaldehyde;
    purified-enzyme experiments use Klebsiella glycerol dehydrogenase. This is important
    context but does not directly test or refute an isolated E. coli GldA acetol-to-S-diol
    assignment.
  snapshot_sha256: 6488881bcba91a133320f164e9be3e7757ad4be8f19dbfa4e71613cd1e724767
- evidence_id: e-abstracts
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/18179582/
  locator: Complete indexed/publisher abstract 18179582; indexed abstracts 18620424,6365902,40950,3920199
  accessed_at: '2026-10-10T23:43:35Z'
  support: context_only
  summary: The abstract-only evidence supports broad GldA substrate/physiological
    context and variable assemblies. The 6365902 abstract permits both NADH and NADPH
    for hydroxyacetone reduction, so the selected NADH branch is not exclusivity.
    No full-text acetol-specific assay or enantiomer proof is claimed from 18179582.
  snapshot_sha256: ddf808efbaabe87cedf1ec3c83c5e463dac60ef4f91a1b5b47b7578b7c557011
- evidence_id: e-pathbank
  kind: database
  reference: https://pathbank.org/downloads/pathbank_primary_biopax.zip
  locator: 'Native member PW002079.owl: biochemical membership/controllers, transport
    10317 and pathway identity SMP0002091'
  accessed_at: '2026-10-10T23:43:35Z'
  support: context_only
  summary: The two-step native lead is consistent with the independent MetaCyc boundary.
    Unsupported transport and periplasmic placement are omitted with a recorded disposition,
    not treated as evidence that transport is biologically absent.
  snapshot_sha256: b075efabab51c7cc0d01e978dce0199e1359f8e5c3bcc47b3e4e422346e65cf2
- evidence_id: e-replay
  kind: validation
  reference: /private/tmp/pathwaymech-next-mg-review/replay.json
  locator: Reviewer extraction/replay source, actual raw response digests, native
    XML/UniProt crosswalks and ChEBI formulas/charges
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: Independent replay passes all 17 edges/25 evidence structure, ten chemical
    occurrences, two balances, 22 source/member digests, exact native pathway ordering
    and protein/component locators. Primary interpretation was checked separately
    from this deterministic script.
  snapshot_sha256: be005edf50a0c58453fe1469e7abc1010848d3ceef8b50f14b3c88b56817059a
- evidence_id: e-context
  kind: database
  reference: research/pathway_additions/2026-10-10-next/methylglyoxal-review-context.json
  locator: Canonical datasets and precise_mg1655 searches gpr,yghZ,gldA; preserved
    output hashes
  accessed_at: '2026-10-10T23:43:35Z'
  support: context_only
  summary: gpr and gldA return expected b3001/b3945 loci and zero module hits. yghZ
    returns no name match while current synonym gpr resolves. No component requires
    summarize. These contextual results are not catalysis, stereo, flux or absence
    evidence.
  snapshot_sha256: 14f07d92fba0ca691397cef0a86e17c6baea67a87652b40002b36560991a6a4f
- evidence_id: e-identity-search
  kind: search
  reference: /private/tmp/pathwaymech-next-mg-review/duplicate-review.txt
  locator: Ignored/hidden-inclusive exact identity search over data/pathways,research,reviews,reports;
    author both-root search receipts and closest glycerol/yeast-methylglyoxal records
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: Exact target identity appears in this addition and source leads. Independently
    read neighboring records have distinct reaction sets, products and taxon/branch
    boundaries. Search scope excludes Git internals and virtual environments; no fleet-wide
    absence claim is made.
  snapshot_sha256: 008c0ce7f73f0908c96b6d211027410d4227ab40c4fb04f458a60b6a35eec135
  search_scope: rg -n -uu exact MetaCyc:PWY-5453|SMP0002091|PW002079 across data/pathways,
    research, reviews and reports in the active worktree, including hidden and ignored
    files; Git internals, virtual environments and bytecode excluded. Both-root broader
    author searches were inspected as context.
- evidence_id: e-authorities
  kind: authority
  reference: research/pathway_additions/2026-10-10-next/authority-integration.json
  locator: Final source/ontology JSON compared with Git basedbf399e; all 11 new manifest
    cache bodies independently rehashed
  accessed_at: '2026-10-10T23:43:35Z'
  support: supports
  summary: All 1319 baseline ontology and1622 source terms and their prior source
    metadata are unchanged. Final totals 1331/1633 include exact new target labels.
    Rhea 139 identity authority is distinguished from explicitly versioned Rhea 142
    mechanistic RDF; no existence waiver or handpatched authority is introduced.
  snapshot_sha256: 76e569ddf2e9ba12dbfa6592036e78938aef8f3fd91ccf8dca9c5b1c6d09d189
- evidence_id: e-gates
  kind: validation
  reference: /private/tmp/pathwaymech-next-{validate,test,lint,render,vendored}.log
  locator: Actual integration-agent terminal gate logs and exit receipts; reviewer
    read final outputs
  accessed_at: '2026-10-10T23:37:38Z'
  support: supports
  summary: Final frozen-input corpus gates are delegated to the integration agent.
    Their actual exit results and logs were inspected; they establish technical consistency,
    separate from the scientific source review.
- evidence_id: e-generated
  kind: validation
  reference: research/pathway_additions/2026-10-10-next/generated-graph-kgx-audit.json
  locator: Actual CLI export, published TSV downloads, record SVG nodes/edges/evidence
    anchors and metadata
  accessed_at: '2026-10-10T23:37:38Z'
  support: supports
  summary: Methylglyoxal retains all 16 named nodes including scope taxon, 15 drawn
    nodes, 17 edges and 25 evidence blocks. Complete KGX evidence/description/category/context
    and exact SVG endpoints/anchors/bounds pass. Reviewer independently rehashed actual
    target/page against the receipt. No browser visual inspection is claimed.
  snapshot_sha256: 2b3d20a77b87b26b17e1843e6db9910226afdb93799739400bbb4de57c773af7
- evidence_id: e-initial-test
  kind: validation
  reference: /private/tmp/pathwaymech-next-test-before-render.log
  locator: Final pytest failure and summary; test_cross_mech.py:371 index comparison
  accessed_at: '2026-10-10T23:38:56Z'
  support: context_only
  summary: Initial full run exited1:1042 passed,1 failed,3 skipped,3 warnings in418.31s.
    The failure compared the prior generated index against newly added records. Integration
    owner confirms this run began before rendering completed. The current-site validation
    subsequently passed; a complete frozen-input rerun is retained separately.
  snapshot_sha256: e51aee5e56ba1f61427b0093f60d1b04799e0e3e0a58f1fa33d17d3ee6372e3f
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact acetol-branch pathway identity and scope
  outcome: supported
  summary: The record is the supported MG1655 annotation for native PWY-5453, with
    two distinct enzymatic reductions. It is not the yeast glutathione route, glycerol
    utilization, lactaldehyde branch or an all-organism statement.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-record
  - e-native
  - e-identity-search
  dimensions:
  - name: taxon_scope
    value: NCBITaxon:511145 native annotation, with K-12 enzyme/engineered-strain
      evidence explicitly bounded
    definition: Taxon and condition are not silently broadened.
    evidence_ids:
    - e-native
    - e-primary2005
    - e-primary2019
- assessment_id: a-chemistry
  area: grounding
  topic: All chemical identities, coefficients and selected directions
  outcome: supported
  summary: Edges 001–010 exactly cover both directed Rhea equations; all coefficients
    are 1 and both atom/charge sums are zero. NADPH/NADP and NADH/NAD are correctly
    distinguished. Right-to-left metadata on 27988 is relative to its master oxidation
    equation.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-rhea
  - e-replay
- assessment_id: a-catalysis
  area: evidence
  topic: Gpr and GldA catalytic support
  outcome: supported
  summary: Edges 011/012 use direct purified YghZ evidence plus exact reviewed reaction
    assertions. The Gpr enables relation preserves function without inventing a monomeric
    physical catalyst. GldA catalysis is assigned to its native complex with an exact
    P0A9S5 component bridge; uninspected full papers are not presented as direct reviewer
    observations.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-proteins
  - e-complex
  - e-primary2005
  - e-abstracts
- assessment_id: a-assembly
  area: representation
  topic: Assembly and cofactor roles
  outcome: supported
  summary: Edges 013/014 retain GldA complex membership and supported bound zinc while
    explicitly preserving variable oligomers and the modeled-NAD limitation. They
    do not infer a fixed octamer requirement, generic Mg cofactor, or metal-rescue
    result.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-complex
  - e-proteins
  - e-primary2019
- assessment_id: a-stereo
  area: scope
  topic: Stereochemistry and physiology limits
  outcome: supported
  summary: The S product is retained as a source annotation, not newly proven by NMR.
    R-diol in the AG1 study is scoped to its proposed lactaldehyde pathway. Native
    unrestricted MG1655 flux, exclusive Gpr roles and invariant stoichiometry are
    not asserted.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-record
  - e-proteins
  - e-primary1999
  - e-primary2005
- assessment_id: a-sequence
  area: graph
  topic: Membership and direct shared intermediate
  outcome: supported
  summary: Edges 015–017 match native reaction-list and ordering, with exact acetol
    output/input. The material link is not equated with a purified full-pathway reconstitution.
    Unsupported transport and neighboring pathways are explicitly excluded.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-native
  - e-rhea
  - e-pathbank
  - e-primary2005
- assessment_id: a-provenance
  area: provenance
  topic: Identifier and evidence fidelity
  outcome: supported
  summary: All references, native object locators and digests were checked; database
    statements remain attributed to the inspected databases. Final authority additions
    preserve baseline coverage and source provenance.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-authorities
  - e-replay
  - e-record
- assessment_id: a-context
  area: scope
  topic: Bounded expression-database context
  outcome: supported
  summary: Required adapter retrieval succeeded after sandbox DNS retry. Exact gene
    matches add context, while no module hit or synonym miss changes the scientific
    interpretation.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-context
- assessment_id: a-publication
  area: consistency
  topic: Validated publication representation
  outcome: supported
  summary: Final delegated corpus gates and the generated artifact audit pass on frozen
    inputs; technical consistency is separate from the scientific judgement.
  target_ids:
  - MetaCyc:PWY-5453
  evidence_ids:
  - e-gates
  - e-generated
findings: []
actions: []
limitations:
- PMID18179582 and several older GldA studies were inspected as complete indexed/publisher
  abstracts, not full experimental papers. The retained exact GldA activity is attributed
  to inspected UniProt and native MetaCyc statements.
- The (S)-diol node is a current Rhea/UniProt/native annotation. Inspected 2005 NMR
  did not resolve enantiomers; 1999 engineered R-diol production follows a proposed
  lactaldehyde route. This review does not newly establish acetol-step absolute stereochemistry.
- Gpr has other substrates and parallel methylglyoxal reductases exist. GldA assembly
  depends on conditions; the record does not fix all active enzyme as an octamer.
  Zinc binding is supported structurally, while an acetol-specific metal removal/rescue
  assay was not inspected.
- MG1655 source genes/native annotations are distinguished from CK281 engineered metabolic
  measurements and AG1 overexpression results. Native unrestricted flux, exclusivity
  and transport are not established.
- Generated graphics were checked structurally through actual SVG/evidence/KGX artifacts;
  no interactive browser visual review is claimed.
notes:
- No target YAML, authority configuration, generated page, history entry or GitHub
  state was edited by this review. Generated pages are owned by the target YAML plus
  src/pathwaymech rendering/graph code; fixes must not patch pages directly.
- The cobalamin research handoff in this batch is unrelated scientific work and does
  not count as pathway coverage or exhausted-source evidence.
tags:
- independent-scientific-review
- methylglyoxal
- stereochemistry
- source-scope
```
