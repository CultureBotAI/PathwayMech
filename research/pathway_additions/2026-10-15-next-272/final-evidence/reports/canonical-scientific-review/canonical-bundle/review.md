# Independent scientific review of ethanolamine utilization

- Review: 20261016T065424Z-ethanolamine-utilization-scientific
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-16T06:26:49Z
- Finished UTC: 2026-10-16T06:54:24Z
- Reviewer: Codex agent /root/next272_core_and_context_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The actual adopted ethanolamine-utilization record is supported at its stated source and experimental scope. Full maintained-record reading and independent canonical binding preserve all five core reactions, both branches, 97 scoped edges, 128 declarations and the accepted source conflicts/limitations. No new actionable scientific finding was identified. Required full-corpus gates passed; this observation does not close existing GitHub issues or claim literature exhaustion.

## Scope And Provenance

Scientific review of exactly one actual maintained PathwayRecord, including entire narrative, local graph, references and explicit source/assay limits.

Selection: Exact root-authorized data/pathways/ethanolamine-utilization.yaml after adoption at SHA f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 54e768a985d07705ea25445804c83b4758646e37.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY0-1477 | data/pathways/ethanolamine-utilization.yaml | maintained | ethanolamine utilization |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Governed actual maintained-target inspect | passed | True | MetaCyc:PWY0-1477 | Fresh inspect preceded formal assessment; expanded inspection added reviewed retained context and current justfile. All 12 originally inspected inputs remain byte-identical. Final inspection explicitly added the terminal gate package, binds 26 inputs and preserves all prior 24 hashes. |
| Independent finite canonical binding | passed | True | MetaCyc:PWY0-1477 | 5,513 checks passed; all 97 graph edges and 128 declarations unchanged; all original-hash references bound; final preparation physical inventory and coverage mappings verified. |
| git diff --check | passed | True | MetaCyc:PWY0-1477 | Actual worktree git diff --check passed. |
| just lint | passed | True | MetaCyc:PWY0-1477 | Documented repository lint command passed. |
| just review-check | passed | False | MetaCyc:PWY0-1477 | All196 existing review bundles passed before the new canonical save. |
| just test | passed | True | MetaCyc:PWY0-1477 | Entire documented pytest suite: 8,014 passed, 3 skipped, 7 warnings in1,014.26s. Exact output is retained. |
| just validate | passed | True | MetaCyc:PWY0-1477 | Full corpus QC passed: closed schema, identifiers, evidence and current generated pages for269 pathway records. |

## Scientific And Domain Assessments

### Exact pathway boundary and chemical identities

identity: supported. Targets: MetaCyc:PWY0-1477.

The record denotes the issued five-reaction ethanolamine-utilization pathway with both acetaldehyde branches. All 22 core material occurrences and four ordering edges survive. Charged native ethanolaminium is distinct from neutral EutH substrate; no broader GO process, KEGG biosynthetic module, normalized MetaNetX species or similarly named source object is asserted as an exact alias. EutT is ancillary rather than a sixth core member.

### Taxa, proteins and experimental preparations

scope: supported. Targets: MetaCyc:PWY0-1477.

Direct MG1655/LT2 pathway associations are retained without upgrading all experiments to those strains. K12 UniProt taxon 83333, LT2 proteins, NCIB8114 purification, JM109/BL21 recombinant hosts and engineered yeast/crude extracts remain distinct. The CPZ-55 caution is curator inference, not proof of route absence or intact native flux.

### Reactions, catalysts, composition and regulation

graph: supported. Targets: MetaCyc:PWY0-1477.

All 97 accepted edges and all endpoint qualifiers/evidence equal the reviewed complete selected graph. Seven selected native activities are represented; eight adjacent and 56 unrelated leads remain accounted context without unrelated catalysts. EutBC six-plus-six component slots and conflicting prose are explicit; subunits contribute through enables and qualified heteromer state. Nine in-scope regulation assertions retain exact activities and assay scope; three off-route backlinks do not become pathway members.

### Conditional activity, metal and localization evidence

evidence: supported. Targets: MetaCyc:PWY0-1477.

All 19 scoped options are included with their accepted qualifications. EutP/Q GTP is an assay input without invented GDP output; EDTA resistance occurs under documented added-Mg conditions. EutT FeII refers to a reconstituted preparation. EutA reactivates the exact source-associated inactive recombinant EAL material under specified ATP/Mg/free-AdoCbl conditions. The EutC19-EGFP location edge denotes the tested short reporter, not full-length EutC. EutH membrane location does not assert charged-substrate transport or BMC delivery.

### Biological context and unresolved source disagreements

completeness: supported. Targets: MetaCyc:PWY0-1477.

All 23 actual narrative paragraphs were read and compared with 32 accepted primary claims, 19 conflict groups, 34 proteins, 71 activities and 3,705 native slots. Supported EutR regulation, conditional growth/washing/GSSG effects, shell architecture, EutG alternative substrates, EutE biochemical updates and ancillary EutT chemistry survive even where no exact typed relation is justified. Corrected wording distinguishes nine EutT material slots from coefficient-two amounts. Source-native EC, CML, oligomer, location and proton-count disagreements remain explicit.

### Oxidation-state specificity and limits of followup evidence

evidence: supported. Targets: MetaCyc:PWY0-1477.

The actual record accurately attributes positive pre-reduced Co(I) cobinamide activity to the 2015 main report while retaining unavailable supporting assays and the native inactivity conflict. It does not mistake competitive inhibition for product detection, extend Co(II) coordination evidence to Co(I), invent physiological reductant identity or assert direct EutT-to-EAL delivery.

### Issuing references, labels and reproducible evidence placement

provenance: supported. Targets: MetaCyc:PWY0-1477.

All 291 reference IDs are unique and internal evidence links resolve. All present source_sha256 values matched actual retained original bytes; native references identify exact issuing own objects and 34 UniProt references identify the actual accessions/taxa. Sixteen narrative references extend the prior 275; nine prior rows change only title/citation metadata. Multi-artifact readings avoid invented aggregate-original hashes. Native structured source assertions stay attributed to the database, not misrepresented as quotations from cited papers.

### iModulonDB crosscheck

scope: supported. Targets: MetaCyc:PWY0-1477.

The reused finite installed-adapter crosscheck supplies expression context only. Component 76 returns eutJ/G/H/A and negatively weighted ackA among 13 rows. Signed module weights do not define reaction direction, activation, catalyst identity, exact pathway membership or native-strain flux. The actual regulator:null failure and bounded raw fallback are retained; no dataset-exhaustion conclusion is made.

### Required corpus gates and ownership

schema: supported. Targets: MetaCyc:PWY0-1477.

Required full-corpus validation, tests, lint and diff checks have terminal successful root receipts for the actual adopted working tree. The scientific conclusion follows source interpretation and full-record review, with deterministic checks supporting schema/identifier/provenance integrity. This review changes neither the pathway, native status nor history and does not close GitHub issues.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| maintained | data/pathways/ethanolamine-utilization.yaml; Entire 3,805-line record; /description; /taxa; /participants; /reactions; /mechanistic_edges; /references | supports | Read the complete actual maintained target after fresh canonical inspect. It has 23 narrative paragraphs, 128 declarations including the root, 97 edges, and 291 references. Exact adopted candidate SHA f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e. |
| core | research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-core-context-review/REVIEW.md; Native pathway identity and chemical boundary; concrete species/source conflicts; taxon/provenance limits; iModulonDB context | supports | Earlier independent source reading by this reviewer verified exact native root, five reactions, 22 occurrences, 14 concrete species, two direct taxa and independently balanced equations. Native CML conflicts, EC2.7.2.15 specificity and charged/neutral identities remain qualified in the actual record. |
| biology | research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-scientific-source-review/REVIEW.md; All supported primary/native dispositions; magnesium/citation successor; explicit primary reading limits | supports | Separate independent scientific source review assessed all 32 primary claims, 19 source-conflict groups and 71 activity leads, and accepted the magnesium/citation successor. This canonical assessment checks their treatment in the actual record; it does not claim to have independently reread every paper in full. |
| graph | research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-graph-design-review/REVIEW.md; Exact 97-edge/128-declaration selection and all 19 scoped option dispositions | supports | This reviewer previously assessed the complete design against retained original sources. Canonical equality checks establish that every selected graph field, evidence payload and endpoint qualifier is unchanged in the actual record. Source-supported optional context survives alongside the five-member core. |
| eutt | research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-eutt-followup-review/REVIEW.md; Six accepted bounded 2015 source dispositions and operational correction | supports | Separate independent followup review accepts the main-text report of pre-reduced Co(I) cobinamide activity while distinguishing Co(II) coordination, competitive inhibition, unavailable SI, the unread 2006 main and the native inactivity annotation. Canonical targeted rereading of main paragraph P9 confirms this scope. |
| record-preparation | research/pathway_additions/2026-10-15-next-272/record-and-authority-review-evidence/archives/complete-record-preparation.part-001.tar.gz; complete-record-preparation/results/{primary-claim,conflict,protein,activity,native-slot,successor}-record-mapping.json; narrative-map.json; primary-reference-closure.json | supports | Independently decoded all 127 outer file payloads of this retained archive, matched sizes/hashes, and bound the actual record to the frozen candidate. Checked 32 claim, 19 conflict, 34 protein, 71 activity and 3,705 native-slot mappings. Mapping counts are coverage accounting, not scientific truth by themselves. |
| imodulon | research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/imodulondb-preparation/ASSESSMENT.md; Finite installed datasets/search/summarize receipts and raw fallback; e_coli/modulome/76 | context_only | Reused this task session’s actual installed-runner crosscheck: 28 dataset keys/20 organisms, 12 searches across six matching keys, 11 successes and one real regulator:null failure with retained raw fallback; successful component 76 summary. All 13 returned signed weights were independently checked earlier. This is expression context only. |
| authority | research/pathway_additions/2026-10-15-next-272/authority-source-originals/new-source-manifest.json; 97 retained native/UniProt source originals; finite selected identity set | supports | Separate completed independent authority/code review accepted the exact 63-native-original producer/consumer profile and additive snapshots. All 128 selected labels and roles were bound; existing owners remain unchanged. This is identity/provenance support, not independent proof of biological mechanism. |
| magnesium-primary | PMID:26448059; https://pmc.ncbi.nlm.nih.gov/articles/PMC4857615/; research/pathway_additions/2026-10-15-next-272/accepted-preparation/archives/native-magnesium-successor.part-001.tar.gz :: native-magnesium-successor/originals/PMC4857615-efetch.xml; .//p[@id="P13"], P14, P37, P39, P40 | supports | Directly reread exact primary paragraphs: EDTA-treatment resistance is reported, while kinetic and HPLC assays add 6.6 and 1 mM MgCl2. GTP acceptance and tag cleavage remain recombinant-assay facts. The record neither asserts magnesium-independent activity nor a demonstrated bound-Mg requirement. |
| cargo-primary | PMID:22428024; https://pubmed.ncbi.nlm.nih.gov/22428024/; research/pathway_additions/2026-10-15-next-272/accepted-preparation/archives/primary-evidence-preparation.part-001.tar.gz :: primary-evidence-preparation/originals/cargo-2012-primary.xml; /article/body/sec[4]/sec[2]/p[1], /body/sec[2]/sec[4]/p[1], /body/sec[2]/sec[8]/p[2] | supports | Directly reread LT2 19-residue EGFP motif construction, native Salmonella ethanolamine-host fluorescence and intact/broken-shell anti-GFP accessibility. The exact P19265 first 19 prefix/taxon binding was independently checked in design. Canonical edge 96 retains experimental_construct scope, not full-length EutC localization. |
| euta-primary | EcoCyc:ETHAMLY-CPLX; research/pathway_additions/2026-10-15-next-272/accepted-preparation/archives/euta-target-followup.part-001.tar.gz :: euta-target-followup/originals/ECOLI-ETHAMLY-CPLX.xml; own component[1], component[2] and comment[1] | supports | Prior independent direct intake accepted the newly acquired exact EcoCyc target, reciprocal EutA comment and six-plus-six components. It is not silently equated to the separately issued META complex. |
| euta-assay | PMID:15466038; https://journals.asm.org/doi/10.1128/jb.186.20.6845-6854.2004; research/pathway_additions/2026-10-15-next-272/accepted-preparation/archives/euta-target-followup.part-001.tar.gz :: euta-target-followup/inputs/EutA-2004-publisher-web-reading.json; publisher L112–115, L123–128, L189–200 | supports | Prior independent publisher-text reading supports the qualified JM109/recombinant EutA and substrate-inactivated holoEAL assay. Actual edge 93 retains free AdoCbl/ATP/Mg conditions and distinguishes the CN-Cbl model. Exact assay/native sequence identity is not established. |
| independent-binding | /private/tmp/pathwaymech-next-272-canonical-scientific-review/canonical-binding-results.json; /checks; /reference_bindings; /mapping_counts | supports | 5,513 finite independent canonical binding checks passed: actual/frozen equality, full preparation physical inventory, all reference original hashes, native issuing-object identities, UniProt accessions/taxa, mapping pointers and bibliographic metadata. The initial checker used the wrong activity-disposition token; corrected local checker/result and initial failure are both retained. |
| prior-search | /private/tmp/pathwaymech-next-272-canonical-scientific-review/prior-review-search.stdout; Complete stdout; command/result in canonical-binding-results.json | context_only | No earlier canonical or historical review target match was found in the explicitly searched review directories. |
| corpus-gates | research/pathway_additions/2026-10-15-next-272/integration-gates/gate-results.json; Terminal gate state, retained receipt bindings and exact log hashes | supports | Independently read and hash-verified root-executed final full-corpus gate receipts. Root ran these commands on the adopted working tree; this reviewer did not relabel them as personally rerun one-record checks. Independent intake passed 128 checks across all 62 retained original payloads. The 1,747-input inventory was observed after gates and is not a retroactive start-state attestation. |

## Limits And Additional Notes

- Full target coverage means the entire one-record surface was assessed, not that every cited article or atomic database field was independently reread in full during this canonical step. Prior independent exact-source readings and their limits are retained; direct canonical rereading targeted the Mg/GTP methods, cargo reporter paragraphs and EutT specificity main text.
- Several primary sources have abstract-only or retained publisher-tool-text scope; one acquired historical PDF was not semantically read in the source review. EutT 2015 supporting assays, the 2006 EutT main, Starai 2005 main and many figure pixels/supplements remain unavailable or uninspected. No new web search or global evidence-exhaustion claim is made.
- The native acetate-kinase EC annotation, five CML placeholder representations, EutBC prose/component wording, EutN assembly forms, several compartment annotations, EutT proton count and cobinamide specificity retain source disagreements. The record reports their scope and does not resolve them by a convenient alias or unsupported mechanistic edge.
- No physiological branch ratio, whole-route net flux, exact in-vivo EutT reductant, direct EutT-to-EAL delivery, universal enzyme essentiality or universal full-length cargo topology is established.
- iModulonDB results are finite computational expression context. One unchanged adapter search failed on regulator:null; exact raw fallback and successful component summary do not establish dataset exhaustion, complete sampled population or native-strain activity.
- Historical reuse of ACETALD and Pi original bytes in the core preparation does not invent missing historical HTTP receipts. Multi-artifact primary references intentionally have no fabricated aggregate-original hash.
- No browser pixel review is claimed. Root owns rendering/KGX integration and publication; passing science and corpus gates do not prove deployment or merged-state issue closure.
- The full suite completed with 8,014 passed, 3 skipped and 7 warnings. The skips and deprecation warnings are retained in the exact root log; they are not reported as successful executed tests.
- Findings: zero in this declared canonical scientific scope. The hidden/ignored-inclusive review-directory search found no predecessor record review for this target; it was not a global GitHub backlog search.
- Existing issues 634 (Mg interpretation), 635 (authority rejection hosts) and 636 (history argument forwarding) remain governed by their separately tracked merged-state acceptance. This clean review neither silently retires nor closes them.
- The root-authorized justfile new-history positional-argument fix was explicitly read before expanded inspect. Required validation/test/lint recipes are unchanged; its substantive command-injection review is separate.
- After the retained full gates, staging exposed upstream XML trailing spaces. Root tracked issue 637 and added a narrowly scoped source-file attribute exception; the staged successor receipt reports exit 0. That packaging change and its independent acceptance are operational work outside this scientific review. No prior inspected input changed, and the earlier unstaged diff check is not relabelled as a staged check.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T065424Z-ethanolamine-utilization-scientific
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of ethanolamine utilization
started_at: '2026-10-16T06:26:49Z'
finished_at: '2026-10-16T06:54:24Z'
reviewer:
  identity: Codex agent /root/next272_core_and_context_review
  kind: agent
  independence: independent
  independence_basis: Independent of the record, native-source, primary-source and
    adapter authors. Previously reviewed finite core/context, graph design and authority
    integration; gave review findings but authored no maintained record or source
    packet. Current writes are scratch and this governed review bundle only.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The actual adopted ethanolamine-utilization record is supported at its stated
  source and experimental scope. Full maintained-record reading and independent canonical
  binding preserve all five core reactions, both branches, 97 scoped edges, 128 declarations
  and the accepted source conflicts/limitations. No new actionable scientific finding
  was identified. Required full-corpus gates passed; this observation does not close
  existing GitHub issues or claim literature exhaustion.
source:
  git_revision: 54e768a985d07705ea25445804c83b4758646e37
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: 4836f2ecdec689c8ddec07e848b77dc120096b62dae6119e2a3948348adae4b8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: conf/identifier_policy.yaml
    sha256: f57137cbec6ee2ffb4abc1c2e448dd93766e37edac9b07c43cab24c5809d27f7
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 8ab396c8de205cbdbb8ade07795536a4b20eec59f5ad4fe5afbc08c1486975c6
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: e9f77bb01f30806cc76dc6ac7a952fb5ed9f03a9a7962a64f7ecb4e0f0c86ede
    role: context
  - path: data/pathways/ethanolamine-utilization.yaml
    sha256: f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 9d0eab4e76b22c194614cb7d309f2726e16331e5a7552c660bd5075e7497d8b2
    role: context
  - path: docs/CURATION.md
    sha256: 2a90c445177b52a179df6b4ee237dbff61e6bcf0e7918a798764dcb0e9292e0b
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 2d2c7d0a069f58fb74a9d44f5ccb8ecb61fee89360f9f0bca20798c801a02d16
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: f504ee9a297f95a3212c04be1993380fab88f1430367a192ad7aa7ec537900d2
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/accepted-preparation/package-manifest.json
    sha256: 2aafdbdd2e1831bbbdd61e75073405f6b221fe2dbaa06bc846e2ec2430806a72
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/imodulondb-preparation/ASSESSMENT.md
    sha256: cbb0d52db106e351159ea5b31d52864965cb47874950676cdf37ae71cf025f4e
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-core-context-review/REVIEW.md
    sha256: e582fbf8f703d80dfe859859bb192056ad7eb95fa368ee0c9443e2aa8d28ffed
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-eutt-followup-review/REVIEW.md
    sha256: 96f456948a13b1817079f7ff259dc9373deefae1c6af006c91e88d615301c4d7
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-graph-design-review/REVIEW.md
    sha256: 118eed75e792d2ee59ae7abb0e83ecf21396135522fb45c9441e246240143d84
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-scientific-source-review/REVIEW.md
    sha256: 3f12e4846b5cc8c5c5fb5c26edc5ad31b47be9ef457a8972d2f52edb463f9718
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/authority-source-originals/new-source-manifest.json
    sha256: 57eef2d9b9ba27372d5b0683f7118c09f32ea005805df7d5a9b8558f94621d23
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/authority-source-originals/source-bindings.json
    sha256: 19275855b954f6dc369cdab506a6af577e379b4e2ea151d77bb984a0e6a93f85
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/integration-gates/artifact-manifest.json
    sha256: 2ede4e0a469cf46678ce56c207bb432f9633edd93a5bd1e195ac28890c447b3a
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/integration-gates/gate-results.json
    sha256: 2847435cfe98c591b5edc85246df2f027e4b57fd735de0cde06202ea26a93026
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/record-and-authority-review-evidence/archives/complete-record-preparation.part-001.tar.gz
    sha256: 787f6ef6f27508733d18176511736b18958fffed4c7dfb7080d579263eb3317e
    role: context
  - path: research/pathway_additions/2026-10-15-next-272/record-and-authority-review-evidence/retention.json
    sha256: 87e7871d5753e0fdbfb0dea1a2d63fcd4ef70281dbc1fa0a330f12b45a86db50
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/schema.py
    sha256: b3f0c28ded2e0e665c15cf0a0e4a8e19ffc1d9bdfd397aa8383ad6a13baf4214
    role: context
scope:
  description: Scientific review of exactly one actual maintained PathwayRecord, including
    entire narrative, local graph, references and explicit source/assay limits.
  selection: Exact root-authorized data/pathways/ethanolamine-utilization.yaml after
    adoption at SHA f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY0-1477
  exclusions:
  - target: All other maintained pathway records
    reason: Only corpus gates cover them; no new scientific assessment.
  - target: Adapter code, browser pixels and publication/merge state
    reason: Separate code/integration work; this review concerns pathway science.
targets:
- target_id: MetaCyc:PWY0-1477
  path: data/pathways/ethanolamine-utilization.yaml
  label: ethanolamine utilization
  kind: maintained
  record_class: PathwayRecord
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ethanolamine-utilization.yaml
    role: maintained pathway identity, narrative, graph and evidence
checks:
- check_id: canonical-inspect
  name: Governed actual maintained-target inspect
  status: passed
  required: true
  summary: Fresh inspect preceded formal assessment; expanded inspection added reviewed
    retained context and current justfile. All 12 originally inspected inputs remain
    byte-identical. Final inspection explicitly added the terminal gate package, binds
    26 inputs and preserves all prior 24 hashes.
  target_ids:
  - MetaCyc:PWY0-1477
  exit_code: 0
  command: /private/tmp/pathwaymech-next-263-verified-venv/bin/python -B scripts/record_review.py
    --repo-root /private/tmp/pathwaymech-next-272-20261015 --schema schema/record_review.yaml
    inspect --targets /private/tmp/pathwaymech-next-272-canonical-scientific-review/targets.yaml
    --input conf/identifier_policy.yaml --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json --input docs/CAUSAL_GRAPHS.md
    --input docs/CURATION.md --input docs/HARMONIZATION.md --input research/pathway_additions/2026-10-15-next-272/accepted-preparation/package-manifest.json
    --input research/pathway_additions/2026-10-15-next-272/authority-source-originals/new-source-manifest.json
    --input research/pathway_additions/2026-10-15-next-272/authority-source-originals/source-bindings.json
    --input schema/record_review.yaml --input src/pathwaymech/schema.py --input justfile
    --input docs/record-reviews.md --input docs/record-review-profile.md --input .claude/skills/review-yaml-record/SKILL.md
    --input .claude/skills/add-pathway/SKILL.md --input research/pathway_additions/2026-10-15-next-272/record-and-authority-review-evidence/retention.json
    --input research/pathway_additions/2026-10-15-next-272/record-and-authority-review-evidence/archives/complete-record-preparation.part-001.tar.gz
    --input research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-core-context-review/REVIEW.md
    --input research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-scientific-source-review/REVIEW.md
    --input research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-graph-design-review/REVIEW.md
    --input research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-eutt-followup-review/REVIEW.md
    --input research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/imodulondb-preparation/ASSESSMENT.md
    --input research/pathway_additions/2026-10-15-next-272/integration-gates/gate-results.json
    --input research/pathway_additions/2026-10-15-next-272/integration-gates/artifact-manifest.json
  evidence_ids:
  - maintained
- check_id: canonical-binding
  name: Independent finite canonical binding
  status: passed
  required: true
  summary: 5,513 checks passed; all 97 graph edges and 128 declarations unchanged;
    all original-hash references bound; final preparation physical inventory and coverage
    mappings verified.
  target_ids:
  - MetaCyc:PWY0-1477
  command: PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 /private/tmp/pathwaymech-next-263-verified-venv/bin/python
    -B check_canonical_binding.py
  exit_code: 0
  evidence_ids:
  - independent-binding
  scope_note: Owned scratch checker, not a new substitute corpus validator or proof
    that counts establish science.
- check_id: full-diff-check
  name: git diff --check
  status: passed
  required: true
  summary: Actual worktree git diff --check passed.
  target_ids:
  - MetaCyc:PWY0-1477
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - corpus-gates
  scope_note: Root executed the exact documented command on the actual worktree; reviewer
    read terminal receipts/logs and verified their hashes.
- check_id: full-lint
  name: just lint
  status: passed
  required: true
  summary: Documented repository lint command passed.
  target_ids:
  - MetaCyc:PWY0-1477
  command: just lint
  exit_code: 0
  evidence_ids:
  - corpus-gates
  scope_note: Root executed the exact documented command on the actual worktree; reviewer
    read terminal receipts/logs and verified their hashes.
- check_id: full-review-check
  name: just review-check
  status: passed
  required: false
  summary: All196 existing review bundles passed before the new canonical save.
  target_ids:
  - MetaCyc:PWY0-1477
  command: just review-check
  exit_code: 0
  evidence_ids:
  - corpus-gates
  scope_note: Root executed the exact documented command on the actual worktree; reviewer
    read terminal receipts/logs and verified their hashes.
- check_id: full-test
  name: just test
  status: passed
  required: true
  summary: 'Entire documented pytest suite: 8,014 passed, 3 skipped, 7 warnings in1,014.26s.
    Exact output is retained.'
  target_ids:
  - MetaCyc:PWY0-1477
  command: just test
  exit_code: 0
  evidence_ids:
  - corpus-gates
  scope_note: Root executed the exact documented command on the actual worktree; reviewer
    read terminal receipts/logs and verified their hashes.
- check_id: full-validate
  name: just validate
  status: passed
  required: true
  summary: 'Full corpus QC passed: closed schema, identifiers, evidence and current
    generated pages for269 pathway records.'
  target_ids:
  - MetaCyc:PWY0-1477
  command: just validate
  exit_code: 0
  evidence_ids:
  - corpus-gates
  scope_note: Root executed the exact documented command on the actual worktree; reviewer
    read terminal receipts/logs and verified their hashes.
evidence:
- evidence_id: maintained
  kind: record_content
  reference: data/pathways/ethanolamine-utilization.yaml
  locator: Entire 3,805-line record; /description; /taxa; /participants; /reactions;
    /mechanistic_edges; /references
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Read the complete actual maintained target after fresh canonical inspect.
    It has 23 narrative paragraphs, 128 declarations including the root, 97 edges,
    and 291 references. Exact adopted candidate SHA f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e.
  snapshot_sha256: f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e
- evidence_id: core
  kind: prior_review
  reference: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-core-context-review/REVIEW.md
  locator: Native pathway identity and chemical boundary; concrete species/source
    conflicts; taxon/provenance limits; iModulonDB context
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Earlier independent source reading by this reviewer verified exact native
    root, five reactions, 22 occurrences, 14 concrete species, two direct taxa and
    independently balanced equations. Native CML conflicts, EC2.7.2.15 specificity
    and charged/neutral identities remain qualified in the actual record.
  snapshot_sha256: e582fbf8f703d80dfe859859bb192056ad7eb95fa368ee0c9443e2aa8d28ffed
- evidence_id: biology
  kind: prior_review
  reference: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-scientific-source-review/REVIEW.md
  locator: All supported primary/native dispositions; magnesium/citation successor;
    explicit primary reading limits
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Separate independent scientific source review assessed all 32 primary claims,
    19 source-conflict groups and 71 activity leads, and accepted the magnesium/citation
    successor. This canonical assessment checks their treatment in the actual record;
    it does not claim to have independently reread every paper in full.
  snapshot_sha256: 3f12e4846b5cc8c5c5fb5c26edc5ad31b47be9ef457a8972d2f52edb463f9718
- evidence_id: graph
  kind: prior_review
  reference: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-graph-design-review/REVIEW.md
  locator: Exact 97-edge/128-declaration selection and all 19 scoped option dispositions
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: This reviewer previously assessed the complete design against retained
    original sources. Canonical equality checks establish that every selected graph
    field, evidence payload and endpoint qualifier is unchanged in the actual record.
    Source-supported optional context survives alongside the five-member core.
  snapshot_sha256: 118eed75e792d2ee59ae7abb0e83ecf21396135522fb45c9441e246240143d84
- evidence_id: eutt
  kind: prior_review
  reference: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/independent-eutt-followup-review/REVIEW.md
  locator: Six accepted bounded 2015 source dispositions and operational correction
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Separate independent followup review accepts the main-text report of pre-reduced
    Co(I) cobinamide activity while distinguishing Co(II) coordination, competitive
    inhibition, unavailable SI, the unread 2006 main and the native inactivity annotation.
    Canonical targeted rereading of main paragraph P9 confirms this scope.
  snapshot_sha256: 96f456948a13b1817079f7ff259dc9373deefae1c6af006c91e88d615301c4d7
- evidence_id: record-preparation
  kind: record_content
  reference: research/pathway_additions/2026-10-15-next-272/record-and-authority-review-evidence/archives/complete-record-preparation.part-001.tar.gz
  locator: complete-record-preparation/results/{primary-claim,conflict,protein,activity,native-slot,successor}-record-mapping.json;
    narrative-map.json; primary-reference-closure.json
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Independently decoded all 127 outer file payloads of this retained archive,
    matched sizes/hashes, and bound the actual record to the frozen candidate. Checked
    32 claim, 19 conflict, 34 protein, 71 activity and 3,705 native-slot mappings.
    Mapping counts are coverage accounting, not scientific truth by themselves.
  snapshot_sha256: 787f6ef6f27508733d18176511736b18958fffed4c7dfb7080d579263eb3317e
- evidence_id: imodulon
  kind: database
  reference: research/pathway_additions/2026-10-15-next-272/accepted-preparation/reports/imodulondb-preparation/ASSESSMENT.md
  locator: Finite installed datasets/search/summarize receipts and raw fallback; e_coli/modulome/76
  accessed_at: '2026-10-16T06:54:24Z'
  support: context_only
  summary: 'Reused this task session’s actual installed-runner crosscheck: 28 dataset
    keys/20 organisms, 12 searches across six matching keys, 11 successes and one
    real regulator:null failure with retained raw fallback; successful component 76
    summary. All 13 returned signed weights were independently checked earlier. This
    is expression context only.'
  snapshot_sha256: cbb0d52db106e351159ea5b31d52864965cb47874950676cdf37ae71cf025f4e
- evidence_id: authority
  kind: authority
  reference: research/pathway_additions/2026-10-15-next-272/authority-source-originals/new-source-manifest.json
  locator: 97 retained native/UniProt source originals; finite selected identity set
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Separate completed independent authority/code review accepted the exact
    63-native-original producer/consumer profile and additive snapshots. All 128 selected
    labels and roles were bound; existing owners remain unchanged. This is identity/provenance
    support, not independent proof of biological mechanism.
  snapshot_sha256: 57eef2d9b9ba27372d5b0683f7118c09f32ea005805df7d5a9b8558f94621d23
- evidence_id: magnesium-primary
  kind: primary_source
  reference: PMID:26448059; https://pmc.ncbi.nlm.nih.gov/articles/PMC4857615/
  locator: 'research/pathway_additions/2026-10-15-next-272/accepted-preparation/archives/native-magnesium-successor.part-001.tar.gz
    :: native-magnesium-successor/originals/PMC4857615-efetch.xml; .//p[@id="P13"],
    P14, P37, P39, P40'
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: 'Directly reread exact primary paragraphs: EDTA-treatment resistance is
    reported, while kinetic and HPLC assays add 6.6 and 1 mM MgCl2. GTP acceptance
    and tag cleavage remain recombinant-assay facts. The record neither asserts magnesium-independent
    activity nor a demonstrated bound-Mg requirement.'
  snapshot_sha256: 44360d646bf5b6b3f123b0655788eb27a8a9ce470ba493ba4e6fc4c4ab725d26
- evidence_id: cargo-primary
  kind: primary_source
  reference: PMID:22428024; https://pubmed.ncbi.nlm.nih.gov/22428024/
  locator: 'research/pathway_additions/2026-10-15-next-272/accepted-preparation/archives/primary-evidence-preparation.part-001.tar.gz
    :: primary-evidence-preparation/originals/cargo-2012-primary.xml; /article/body/sec[4]/sec[2]/p[1],
    /body/sec[2]/sec[4]/p[1], /body/sec[2]/sec[8]/p[2]'
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Directly reread LT2 19-residue EGFP motif construction, native Salmonella
    ethanolamine-host fluorescence and intact/broken-shell anti-GFP accessibility.
    The exact P19265 first 19 prefix/taxon binding was independently checked in design.
    Canonical edge 96 retains experimental_construct scope, not full-length EutC localization.
  snapshot_sha256: b31a9952234134bbcdad7022160ba80498eb19c9402d409dd01b53aceb5657e3
- evidence_id: euta-primary
  kind: database
  reference: EcoCyc:ETHAMLY-CPLX
  locator: 'research/pathway_additions/2026-10-15-next-272/accepted-preparation/archives/euta-target-followup.part-001.tar.gz
    :: euta-target-followup/originals/ECOLI-ETHAMLY-CPLX.xml; own component[1], component[2]
    and comment[1]'
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Prior independent direct intake accepted the newly acquired exact EcoCyc
    target, reciprocal EutA comment and six-plus-six components. It is not silently
    equated to the separately issued META complex.
  snapshot_sha256: 796c3185af98fa998262835441853476388ed0ca2ba6ac28484e87bb5eedd55c
- evidence_id: euta-assay
  kind: primary_source
  reference: PMID:15466038; https://journals.asm.org/doi/10.1128/jb.186.20.6845-6854.2004
  locator: 'research/pathway_additions/2026-10-15-next-272/accepted-preparation/archives/euta-target-followup.part-001.tar.gz
    :: euta-target-followup/inputs/EutA-2004-publisher-web-reading.json; publisher
    L112–115, L123–128, L189–200'
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  summary: Prior independent publisher-text reading supports the qualified JM109/recombinant
    EutA and substrate-inactivated holoEAL assay. Actual edge 93 retains free AdoCbl/ATP/Mg
    conditions and distinguishes the CN-Cbl model. Exact assay/native sequence identity
    is not established.
  snapshot_sha256: 47c0d8f4c042f2d9319485c297be0b4db4ed2a650e72155c347ef9645b5461f5
- evidence_id: independent-binding
  kind: validation
  reference: /private/tmp/pathwaymech-next-272-canonical-scientific-review/canonical-binding-results.json
  locator: /checks; /reference_bindings; /mapping_counts
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  snapshot_sha256: 9c131cb8de68810c6199b51f463b0343b1f5fbf2b49334e6e2e6958e2bab9f33
  summary: '5,513 finite independent canonical binding checks passed: actual/frozen
    equality, full preparation physical inventory, all reference original hashes,
    native issuing-object identities, UniProt accessions/taxa, mapping pointers and
    bibliographic metadata. The initial checker used the wrong activity-disposition
    token; corrected local checker/result and initial failure are both retained.'
- evidence_id: prior-search
  kind: search
  reference: /private/tmp/pathwaymech-next-272-canonical-scientific-review/prior-review-search.stdout
  locator: Complete stdout; command/result in canonical-binding-results.json
  accessed_at: '2026-10-16T06:54:24Z'
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  summary: No earlier canonical or historical review target match was found in the
    explicitly searched review directories.
  search_scope: rg --no-ignore --hidden -n PWY0-1477|ethanolamine-utilization reviews
    reports/yaml_record_review reports/yaml_category_review; exit1; stderr empty.
    Hidden and ignored files included. Archive contents not decoded; this is not a
    global issue or literature search.
- evidence_id: corpus-gates
  kind: validation
  reference: research/pathway_additions/2026-10-15-next-272/integration-gates/gate-results.json
  locator: Terminal gate state, retained receipt bindings and exact log hashes
  accessed_at: '2026-10-16T06:54:24Z'
  support: supports
  snapshot_sha256: 2847435cfe98c591b5edc85246df2f027e4b57fd735de0cde06202ea26a93026
  summary: Independently read and hash-verified root-executed final full-corpus gate
    receipts. Root ran these commands on the adopted working tree; this reviewer did
    not relabel them as personally rerun one-record checks. Independent intake passed
    128 checks across all 62 retained original payloads. The 1,747-input inventory
    was observed after gates and is not a retroactive start-state attestation.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact pathway boundary and chemical identities
  outcome: supported
  summary: The record denotes the issued five-reaction ethanolamine-utilization pathway
    with both acetaldehyde branches. All 22 core material occurrences and four ordering
    edges survive. Charged native ethanolaminium is distinct from neutral EutH substrate;
    no broader GO process, KEGG biosynthetic module, normalized MetaNetX species or
    similarly named source object is asserted as an exact alias. EutT is ancillary
    rather than a sixth core member.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - core
  - graph
  dimensions:
  - name: source-object
    value: META:PWY0-1477, release 27.0
    definition: Exact issuing object and boundary
    evidence_ids:
    - maintained
    - core
    - graph
  - name: reaction-direction
    value: One own L2R and four own reversible; selected traversal has two R2L reactions
    definition: Own direction, pathway traversal and assay direction remain separate
    evidence_ids:
    - maintained
    - core
    - graph
- assessment_id: taxa
  area: scope
  topic: Taxa, proteins and experimental preparations
  outcome: supported
  summary: Direct MG1655/LT2 pathway associations are retained without upgrading all
    experiments to those strains. K12 UniProt taxon 83333, LT2 proteins, NCIB8114
    purification, JM109/BL21 recombinant hosts and engineered yeast/crude extracts
    remain distinct. The CPZ-55 caution is curator inference, not proof of route absence
    or intact native flux.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - core
  - biology
  - graph
  dimensions:
  - name: taxon-condition
    value: NCBITaxon:511145 and 99287 direct associations; K12 protein 83333; exact
      experimental host in narrative/qualifiers
    definition: Source taxon does not define every assay material
    evidence_ids:
    - maintained
    - core
    - biology
    - graph
  - name: evidence-tier
    value: Direct assays, unpurified extracts, mutant phenotypes, similarity and curator
      inference are distinguished
    definition: No evidence-tier promotion across issued proteins
    evidence_ids:
    - maintained
    - core
    - biology
    - graph
- assessment_id: core-graph
  area: graph
  topic: Reactions, catalysts, composition and regulation
  outcome: supported
  summary: All 97 accepted edges and all endpoint qualifiers/evidence equal the reviewed
    complete selected graph. Seven selected native activities are represented; eight
    adjacent and 56 unrelated leads remain accounted context without unrelated catalysts.
    EutBC six-plus-six component slots and conflicting prose are explicit; subunits
    contribute through enables and qualified heteromer state. Nine in-scope regulation
    assertions retain exact activities and assay scope; three off-route backlinks
    do not become pathway members.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - graph
  - biology
  - independent-binding
  dimensions:
  - name: component-role
    value: EutBC complete catalysis versus subunit contribution; EutL three-chain
      pseudohexamer; EutN preparation-dependent assembly
    definition: Chain count, geometric shape and activity role are not conflated
    evidence_ids:
    - maintained
    - graph
    - biology
    - independent-binding
  - name: branch-quantity
    value: No physiological branch ratio or single whole-route net asserted
    definition: Balanced individual equations do not establish route flux
    evidence_ids:
    - maintained
    - graph
    - biology
    - independent-binding
- assessment_id: conditional-context
  area: evidence
  topic: Conditional activity, metal and localization evidence
  outcome: supported
  summary: All 19 scoped options are included with their accepted qualifications.
    EutP/Q GTP is an assay input without invented GDP output; EDTA resistance occurs
    under documented added-Mg conditions. EutT FeII refers to a reconstituted preparation.
    EutA reactivates the exact source-associated inactive recombinant EAL material
    under specified ATP/Mg/free-AdoCbl conditions. The EutC19-EGFP location edge denotes
    the tested short reporter, not full-length EutC. EutH membrane location does not
    assert charged-substrate transport or BMC delivery.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - graph
  - magnesium-primary
  - cargo-primary
  - euta-primary
  - euta-assay
  dimensions:
  - name: experimental-construct
    value: P/Q cleaved tags; Q GT remnant; A JM109/EAL state; EutC1–19-EGFP motif
    definition: Assay materials travel in edge descriptions and endpoint qualifiers
    evidence_ids:
    - maintained
    - graph
    - magnesium-primary
    - cargo-primary
    - euta-primary
    - euta-assay
  - name: compartment
    value: Native association, inferred lumen/side, engineered shells and reporter
      encapsulation retain distinct scopes
    definition: GO identity alone is not enzyme-localization evidence
    evidence_ids:
    - maintained
    - graph
    - magnesium-primary
    - cargo-primary
    - euta-primary
    - euta-assay
- assessment_id: narrative
  area: completeness
  topic: Biological context and unresolved source disagreements
  outcome: supported
  summary: All 23 actual narrative paragraphs were read and compared with 32 accepted
    primary claims, 19 conflict groups, 34 proteins, 71 activities and 3,705 native
    slots. Supported EutR regulation, conditional growth/washing/GSSG effects, shell
    architecture, EutG alternative substrates, EutE biochemical updates and ancillary
    EutT chemistry survive even where no exact typed relation is justified. Corrected
    wording distinguishes nine EutT material slots from coefficient-two amounts. Source-native
    EC, CML, oligomer, location and proton-count disagreements remain explicit.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - record-preparation
  - biology
  - graph
  - independent-binding
- assessment_id: eutt-specificity
  area: evidence
  topic: Oxidation-state specificity and limits of followup evidence
  outcome: supported
  summary: The actual record accurately attributes positive pre-reduced Co(I) cobinamide
    activity to the 2015 main report while retaining unavailable supporting assays
    and the native inactivity conflict. It does not mistake competitive inhibition
    for product detection, extend Co(II) coordination evidence to Co(I), invent physiological
    reductant identity or assert direct EutT-to-EAL delivery.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - eutt
  - biology
  dimensions:
  - name: source-access
    value: 2015 main/captions/Table 1 accepted; SI unavailable; 2006 main unread
    definition: Availability and scientific reading scope remain distinct
    evidence_ids:
    - maintained
    - eutt
    - biology
- assessment_id: references
  area: provenance
  topic: Issuing references, labels and reproducible evidence placement
  outcome: supported
  summary: All 291 reference IDs are unique and internal evidence links resolve. All
    present source_sha256 values matched actual retained original bytes; native references
    identify exact issuing own objects and 34 UniProt references identify the actual
    accessions/taxa. Sixteen narrative references extend the prior 275; nine prior
    rows change only title/citation metadata. Multi-artifact readings avoid invented
    aggregate-original hashes. Native structured source assertions stay attributed
    to the database, not misrepresented as quotations from cited papers.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - authority
  - record-preparation
  - independent-binding
- assessment_id: expression-context
  area: scope
  topic: iModulonDB crosscheck
  outcome: supported
  summary: The reused finite installed-adapter crosscheck supplies expression context
    only. Component 76 returns eutJ/G/H/A and negatively weighted ackA among 13 rows.
    Signed module weights do not define reaction direction, activation, catalyst identity,
    exact pathway membership or native-strain flux. The actual regulator:null failure
    and bounded raw fallback are retained; no dataset-exhaustion conclusion is made.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - imodulon
  - core
  dimensions:
  - name: dataset-scope
    value: 28 dataset keys/20 organisms; 12 actual searches in six matching keys;
      one component 76 summary
    definition: Finite returned results, not all transcriptomic genes or all experiments
    evidence_ids:
    - maintained
    - imodulon
    - core
- assessment_id: gates
  area: schema
  topic: Required corpus gates and ownership
  outcome: supported
  summary: Required full-corpus validation, tests, lint and diff checks have terminal
    successful root receipts for the actual adopted working tree. The scientific conclusion
    follows source interpretation and full-record review, with deterministic checks
    supporting schema/identifier/provenance integrity. This review changes neither
    the pathway, native status nor history and does not close GitHub issues.
  target_ids:
  - MetaCyc:PWY0-1477
  evidence_ids:
  - maintained
  - corpus-gates
findings: []
actions: []
limitations:
- Full target coverage means the entire one-record surface was assessed, not that
  every cited article or atomic database field was independently reread in full during
  this canonical step. Prior independent exact-source readings and their limits are
  retained; direct canonical rereading targeted the Mg/GTP methods, cargo reporter
  paragraphs and EutT specificity main text.
- Several primary sources have abstract-only or retained publisher-tool-text scope;
  one acquired historical PDF was not semantically read in the source review. EutT
  2015 supporting assays, the 2006 EutT main, Starai 2005 main and many figure pixels/supplements
  remain unavailable or uninspected. No new web search or global evidence-exhaustion
  claim is made.
- The native acetate-kinase EC annotation, five CML placeholder representations, EutBC
  prose/component wording, EutN assembly forms, several compartment annotations, EutT
  proton count and cobinamide specificity retain source disagreements. The record
  reports their scope and does not resolve them by a convenient alias or unsupported
  mechanistic edge.
- No physiological branch ratio, whole-route net flux, exact in-vivo EutT reductant,
  direct EutT-to-EAL delivery, universal enzyme essentiality or universal full-length
  cargo topology is established.
- iModulonDB results are finite computational expression context. One unchanged adapter
  search failed on regulator:null; exact raw fallback and successful component summary
  do not establish dataset exhaustion, complete sampled population or native-strain
  activity.
- Historical reuse of ACETALD and Pi original bytes in the core preparation does not
  invent missing historical HTTP receipts. Multi-artifact primary references intentionally
  have no fabricated aggregate-original hash.
- No browser pixel review is claimed. Root owns rendering/KGX integration and publication;
  passing science and corpus gates do not prove deployment or merged-state issue closure.
- The full suite completed with 8,014 passed, 3 skipped and 7 warnings. The skips
  and deprecation warnings are retained in the exact root log; they are not reported
  as successful executed tests.
notes:
- 'Findings: zero in this declared canonical scientific scope. The hidden/ignored-inclusive
  review-directory search found no predecessor record review for this target; it was
  not a global GitHub backlog search.'
- Existing issues 634 (Mg interpretation), 635 (authority rejection hosts) and 636
  (history argument forwarding) remain governed by their separately tracked merged-state
  acceptance. This clean review neither silently retires nor closes them.
- The root-authorized justfile new-history positional-argument fix was explicitly
  read before expanded inspect. Required validation/test/lint recipes are unchanged;
  its substantive command-injection review is separate.
- After the retained full gates, staging exposed upstream XML trailing spaces. Root
  tracked issue 637 and added a narrowly scoped source-file attribute exception; the
  staged successor receipt reports exit 0. That packaging change and its independent
  acceptance are operational work outside this scientific review. No prior inspected
  input changed, and the earlier unstaged diff check is not relabelled as a staged
  check.
tags:
- ethanolamine
- scientific-review
- source-scoped
- next272
```
