# Independent scientific review of complete Entner-Doudoroff pathway

- Review: 20261011T182037Z-entner-doudoroff-independent-scientific-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T18:16:47.135343Z
- Finished UTC: 2026-10-11T18:20:37Z
- Reviewer: Codex /root/ed_whole_record_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The entire maintained KEGG:M00008 record is supported within its stated scope:5 native reactions at4 positions,19participants,1taxon,37edges,92evidence occurrences and51references. All edges and source claims were independently assessed; current original-source/authority checks, completed integrated replay, full-corpus gates and graph preservation support final integration. No new actionable finding. The2012 article support belongs to the earlier web-only review and is not claimed as newly inspected or locally hashed full text.

## Scope And Provenance

Whole-record scientific review of the complete maintained Entner-Doudoroff module after final integration freeze, including exact authority/source/helper and graph context.

Selection: Single explicitly assigned maintained entner-doudoroff-pathway.yaml, SHA548eba1d34a081dd293db6d8bf0e00a0e620973e8f843dafa75bcded6a74e4af.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 721755c9b4af76d32d2b1f232571bbfeab232441.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| KEGG:M00008 | data/pathways/entner-doudoroff-pathway.yaml | maintained | Entner-Doudoroff pathway |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| render | passed | True | KEGG:M00008 | Rendered219 maintained records. |
| validate | passed | True | KEGG:M00008 | Full219-record validation including identifiers, schema, history and page currency passed. |
| lint | passed | True | KEGG:M00008 | Current full Ruff check passed. |
| diff-tracked | passed | True | KEGG:M00008 | Tracked whitespace passed. |
| test | passed | True | KEGG:M00008 | 1256passed,3skipped,3warnings; original test child exited0. |
| identifiers | passed | True | KEGG:M00008 | 219 records passed identifier/label policy. |
| kgx | passed | True | KEGG:M00008 | Separate full219-record KGX export passed. |
| Initial helper lint failure, superseded | failed | False | KEGG:M00008 | Initial driver12654 exited1 solely on Ruff I001; original helper preserved and one-blank-line successor passed current lint. |
| Independent original-source selection audit | passed | True | KEGG:M00008 | 94 response bodies,92 evidence selections,8 primary selections,18 SQL chemical/taxon/compartment rows and51reference metadata entries checked. |
| Independent authority preservation and original identity checks | passed | True | KEGG:M00008 | All prior production entries/metadata preserved against actual721755;4new native objects,4reused proteins and21 original SQL terms verified. |
| Completed source/runtime/authority integration | passed | True | KEGG:M00008 | All4 child commands and2291 endpoint input checks passed. |
| Current structural page/KGX preservation | passed | True | KEGG:M00008 | 37edges/92evidence,26KGX/25SVG nodes and prior corpus preservation passed. |
| Final canonical inspect | passed | True | KEGG:M00008 | Actual inspect captured489 input files at working-tree base721755 after explicit final freeze. |
| Final small-input, source-body, log and AST checks | passed | True | KEGG:M00008 | All489 inspected files,94 original bodies,171 adopted proofs,7 gate logs,4 child logs and exact helper AST relation passed. |

## Scientific And Domain Assessments

### Complete native module boundary and alternative membership

identity: supported. Targets: KEGG:M00008.

The record represents the entire four-position KEGG:M00008 module: R02736 andR10907 are alternatives at the first position, followed by hydrolysis/dehydration/aldol cleavage. Native M00008 membership governs the retained R10907 inverse-MODULE conflict. Glucose uptake/phosphorylation, lower glycolysis and ATP formation are outside this boundary; no adjacent MetaCyc shunt or sulfoED substitution is made.

### Exact beta-anomer chemistry and protonation normalization

grounding: supported. Targets: KEGG:M00008.

KEGG C01172 is native beta-glucose6P. Original ATOM/BOND and selected ChEBI58247 preserve connectivity/stereochemistry under explicit acid-base normalization; neutral CHEBI17719 is reference-only. Alpha58225 and generic61548 are distinct contextual references. No neutral/charged exactMatch or experimental exclusive beta specificity is inferred.

### Reaction sides, direction, coefficient and separate net accounting

quantity: supported. Targets: KEGG:M00008.

All20 chemical edges agree with the complete original sides. Rhea12557/17278/17090 direction is grounded in native masters and KEGG bidirectional cross-references, while reversible KEGG oxidation definitions retain their native directions. Five equations balance atoms and charge. Each separate donor branch yields GAP,pyruvate,reduced donor and2hydrons; water cancels and no ATP is asserted. Parallel alternatives are not summed.

### Taxon, current protein and historical construct distinctions

scope: supported. Targets: KEGG:M00008.

Current UniProt entries issue K-12 taxon83333 and lengths491/331/603/213. This establishes current identifiers, not exact equality to every historical/tagged experimental construct. K-12/MG1655 donors remain distinct from BL21 or SeMet expression hosts; current Edd603-residue PLR sequence difference from historical602-residue AC is explicit.

### Zwf donor use, preference and beta annotation

evidence: supported. Targets: KEGG:M00008.

Both first-position enables edges combine native KEGG beta attribution with experimental donor capacity and strong NADP preference. Generic G6P assays and current HAMAP annotation do not prove exclusive beta use or equal in-vivo donor flux. The2012 support is attributed to this reviewer's earlier web-only reading; current2016 original Methods/Table1 and workbook scope were freshly reassessed. S1Table P0AC53 is sequence-analysis mapping, not construct identity.

### Pgl genetics and extract hydrolysis

evidence: supported. Targets: KEGG:M00008.

Native Pgl assignment is supported by deletion/complementation and extract activity with explicit MG1655 background and DY378 construction scope. Unknown starting lactone concentration limits quantitation. The record does not invent purified assembly or obligatory metal evidence.

### Edd catalysis and cofactor evidence tiers

evidence: supported. Targets: KEGG:M00008.

K-12 amplified ORF expressed in BL21(DE3), coupled fractionated-lysate activity and native catalytic annotation support dehydration within historical-sequence limits. Edd peroxide sensitivity and iron/DTT recovery do not establish direct Edd EPR or measured cluster stoichiometry. One4Fe4S count is similarity/HAMAP inference; Mn supplementation is not an obligatory cofactor.

### Eda selected catalysis, native trimer and localization

evidence: supported. Targets: KEGG:M00008.

MetaCyc native complex component coefficient3, exact P0A955 link, experimental homotrimer annotation and original recombinant structure support selected Eda assembly. Only the module KDPG cleavage activity is represented. LDH reporter NADH is not a reactant; experimental donor-strain equality is not inferred. Cytoplasm remains ECO:0000305 curator inference.

### CsrA source conflict retained without direct regulation

consistency: supported. Targets: KEGG:M00008.

Original2005 Results and Discussion support generally positive indirect Eda expression effects; the negative heading/current annotation conflict is explicitly retained. Figure7 was inspected during the earlier external review. No unsupported direct inhibitory or activating edge is exported.

### Claim-specific evidence and reference coverage

evidence: supported. Targets: KEGG:M00008.

All37edges and92 evidence occurrences were scientifically assessed against nearest exact source locators and appropriately scoped original bodies, with all51 reference metadata entries checked. Structured source assertions are interpretations of native objects, not invented quotations from cited papers. 2012 is earlier web-only full text with no local article digest; current local403 is not substituted as article evidence.

### iModulonDB remains computational context

scope: supported. Targets: KEGG:M00008.

The original structured adapter21response/15query evidence identifies component25 for edd/b1851 and eda/b1850 in e_coli/precise_mg1655. It supplies expression-module context only; no direct mechanism, regulation, donor flux or broader taxon inference follows.

### Production authority preservation and final integrated gates

provenance: supported. Targets: KEGG:M00008.

Independent current authority audit preserves every prior entry/metadata against actual721755 merge.4source bodies,6source terms and3ontology terms are grounded in original issuing objects; reference-only CHEBI17719 and reused UniProt batch provenance are explicit. Completed current integration and required corpus checks support219-record runtime compatibility without implying scientific re-review of the other218 records.

### Helper lineage, meaningful controls and proof boundaries

provenance: supported. Targets: KEGG:M00008.

Original helperf67 is preserved; current3a9 successor differs by one blank line with identical executable AST. Issue406 has an evidence-backed formatting correction. Current wrapper binds2291 source/runtime/authority/policy/proof inputs and rechecks endpoints. Original reviewer guards,42 narrow wrapper controls and13 formatting-lineage controls remain scoped; seven invalid record variants are rejected. No claim is made that narrow fixtures are repeated full-source mutation replays or that digest endpoints exclude all transient state changes.

### Current graph representation and complete prior-context preservation

graph: supported. Targets: KEGG:M00008.

Current static/programmatic graph audit preserves37edges/92evidence,26KGXnodes and25visible SVGnodes, with taxon scope retained outside the visible mechanism layout. All218 prior pages,10416 prior edges and6883 source-context node entries remain. Three shared display labels change under the unchanged first-record rule; old context labels persist. Contributor graph audit is attributed structural evidence, separate from this reviewer's scientific judgment. No browser visual or interaction test is claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: KEGG:M00008. Retain the complete native four-position M00008 module with parallel NADP/NAD first reactions. Exclude glucose uptake/phosphorylation, lower glycolysis, ATP generation and distinct sulfoED or broad BRENDA map context.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/pathways/entner-doudoroff-pathway.yaml; entire maintained record, all37edges/92evidence/51references | supports | Complete KEGG module with5 native reaction objects in4 positions,19participants and1taxon. Current target is byte-identical to the independently reviewed external candidate. |
| source-audit | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/original-evidence-audit.json; source_checks; primary_original_selections; evidence_selections; issuing_sql_labels; reference_metadata | supports | Current reviewer freshly checked94 retained response bodies,16 prior proofs, all92 evidence occurrences,8 original primary selections,18 selected SQL chemical/taxon/compartment rows and51 reference metadata entries. Exact selectors and original values are recorded. Selector success is distinct from scientific entailment. |
| native-sources | research/pathway_additions/2026-10-11-next-218/draft/ed-source-manifest.json; original module M00008; reactions R02736/R10907/R02035/R02036/R05605; native compound bodies; Rhea142 original RDF; UniProt and MetaCyc objects | supports | Original source bodies support exact native membership and identifiers. Five native reaction objects are preserved; NAD/NADP alternatives are parallel. Native module includes R10907 despite inverse reaction MODULE omission. Issuing scientific Rhea142 RDF is distinct from production Rhea139 SQL authority. |
| chemical-proof | research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/independent-chemistry.json; five balances; ten original Rhea sides; twelve native structure bridges; two donor-dependent net equations | supports | This same independent reviewer previously derived complete chemical sides and atom/charge balances from original sources. Exact target and selected source bytes remain unchanged; current source/SQL readings and completed integration replay corroborate the proof. Initial reviewer RDF parser error and corrected successor are preserved, not a product defect. |
| prior-positive | research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/positive-replay.json; actual26000/0 complete original-source replay, record_sha256 and limits | supports | Earlier independent external full replay streamed three SQL databases plus Rhea142 RDF and checked94 retained responses, exact source/proposal claims, sequences, structured iModulon adapter and strict/KGX output. This is historical evidence, not current production-authority approval. |
| prior-review | research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/whole-record-review.json; all13 domains and37edge assessments; independence; actual executions and source-access limits | supports | Earlier external whole-record scientific review by this same reviewer. No target/helper/authority implementation contribution. It is external evidence, not an invented canonical predecessor or a second independent reviewer. |
| zwf-2012-web | research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/web-primary-observations.json; earlier official publisher PDF inspection; Table1, Discussion p2303, Purification pp2305-2306 | supports | The2012 full article was personally inspected on the web during the earlier independent review. It supports strong NADP preference, NAD capacity and the thrombin-cleaved construct retaining12 extra N-terminal residues. This final phase did not repeat that web inspection and has no local full-article digest; local403body is not article evidence. |
| zwf-2016 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4807051/; //sec[@id="sec005"]/p; //table-wrap[@id="pone.0152403.t001"]; original S1Table workbook row9 | supports | Original JATS Methods and Table1 were freshly read. Wild-type comparator shows NADP preference and measurable NAD activity; recombinant TEV processing leaves an expected Gly-His extension. S1Table links P0AC53 for sequence analysis, not exact experimental construct identity. Assay G6P does not prove exclusive beta-anomer usage. |
| pgl-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC532434/; //section[@id="sec4"]/p[1]; //section[@id="sec15"]/p[1]; Figure4 | supports | Original construction and Results passages support pgl/ybhE loss-of-function and complementation in MG1655-background strains after DY378 recombineering. The extract assay is not entirely quantitative because initial lactone concentration is unknown. |
| edd-eda-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2211689/; //section[@id="sec10"]/p[1..3]; //section[@id="sec11"]/p[1] | supports | Original Methods distinguish K-12 edd donor and BL21(DE3) expression host. Fractionated lysate activity supports dehydration; added Mn/Fe are preparation conditions. Eda cleavage uses LDH-coupled pyruvate detection: NADH is reporter reagent, not Eda substrate. |
| edd-cluster-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC5136138/; //*[@id="P9"]; //*[@id="P30"]; Figures4 and5 scope | supports | Original Edd lysate activity is peroxide-sensitive and recoverable with iron/DTT. The stated3Fe4S EPR spectrum is fumarase A. It is not an Edd cluster spectrum or direct occupancy measurement. |
| eda-trimer-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC31111/; //section[@id="sec2"]/p[1]; //section[@id="sec5"]/p[1] | supports | Original recombinant E.coli Eda structure has trimeric assembly. The pKK-223 preparation and expression/SeMet host details do not independently prove a specific MG1655 donor or exact current unmodified sequence. |
| csra-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC545716/; //section[@id="sec21"]/h3 and p[1]; //section[@id="sec22"]/p[1]; Figure7 | supports | Fresh original Results and Discussion reading shows decreased Eda/transcription in csrA mutant and generally positive indirect control, despite the negative section heading and conflicting current annotation. Earlier review also inspected original Figure7. No direct CsrA inhibition or activation edge is asserted. |
| protein-native | research/pathway_additions/2026-10-11-next-218/draft/ed-protein-projection.json; four original complete UniProt sequences/comments/ECO; MetaCyc Eda complex component and catalyzed-reaction XML | supports | Fresh original-pointer audit checks current K-12 taxon83333 and491/331/603/213-residue proteins, Eda native complex component coefficient3, homotrimer and inferred cytoplasm, Edd similarity/HAMAP cluster count. Projection is a locator index; original values in source-audit carry the evidentiary check. |
| authority-current | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/current-authority-audit.json; prior_entries_and_metadata_preserved; new_native_objects; existing_protein_authority_reuse; selected_ontology_rows | supports | Reviewer independently compared every prior authority/manifest entry against actual721755 merge, parsed4 new native objects and compared4 reused old UniProt batch records to current scientific entries, querying21 original SQL terms. Four source bodies,6 source terms and3 ontology terms added; CHEBI17719 is reference-only. No whole-DB rehash claimed in this audit. |
| authority-root | research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-next-218-authority-root-review.json; database_checks; version_checks; preservation | supports | Root independently streamed all4 production SQL bodies and derived selected labels/versions before adoption. Original batch2026_03 provenance is retained separately from fresh UniProt entryAudit. Actual merged-base equivalence and current preservation were separately verified by this reviewer. |
| imod | research/pathway_additions/2026-10-11-next-218/imod/context.json; 21 original response bodies;15queries; e_coli/precise_mg1655/component25 and edd/b1851,eda/b1850 | context_only | Original structured adapter replay supports bounded computational expression context for edd/eda. Membership is not direct catalysis, pathway identity, regulation or in-vivo donor flux. |
| dedup | research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/root-disposition.json; all current baseline search dispositions and explicit exclusions | context_only | Ignored/hidden/symlink-inclusive baseline search distinguishes exact M00008 from maintained sulfoED and historical BRENDA map/export canaries. Those canaries remain source context, not a completed equivalent maintained record or BRENDA ingestion. |
| formatting | research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/adoption.json; exact original/archive/successor bytes, AST equality, issue406 and initial gate receipts | supports | Initial required lint failed I001. A single blank line was added, preserving original f67 bytes and historical aliases; current3a9 helper has identical executable AST. Reviewer independently rechecked exact one-line relation and AST after canonical inspection. Current lint succeeds; issue406 is external lineage, not a canonical finding predecessor. |
| integration | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/integration-replay.json; commands;2291 bound inputs; formatting evidence; child receipt and limits | supports | Actual root-observed38656/0 terminaldff4d1 current integrated replay passed source replay, corpus identifiers, native schema and target strict schema. All2291 bindings rechecked at startup/completion. The complete wrapper was read; cached source/proposal replay and production authority selection remain distinct scopes. |
| source-replay-current | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/source-replay.json; native_members;rhea_sides;kegg_structure_bridges;balances;branch_nets;sequence_checks;negative_controls;all_evidence_anchors | supports | Current formatted helper checked94 bodies,5 native reaction objects,10 Rhea sides,12 native structure bridges,5 balanced equations,2 separate nets,4 sequences,8 primary selections and92 evidence anchors. Seven targeted invalid record variants were rejected. This is deterministic corroboration, not independent scientific interpretation. |
| integration-root | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/integrated-replay-root-adoption.json; actual terminal observation, receipt digests,2171 formal rechecks and limits | supports | Root inspected actual child exits/log digests and scientifically scoped summaries, freshly checked2171 non-source bindings and adopted current integration. Driver/child streamed whole source bodies; no extra root or current-reviewer database pass is implied. |
| boundary-controls | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/results.json; 42 narrow actual guard/environment controls including late changes, path retarget, inventories, stale cache and nested safe path | supports | Original wrapper successor rejects changed formal/source/proof/manifest bytes and identities, late mutation, inventory changes and collisions. Small real-function/CLI/environment fixtures are explicitly not42 full scientific-source replay mutations. Nested RDKit safe-path correction and earlier attempts remain preserved. |
| formatting-controls | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/controls-attempt-1/results.json; 13 current formatting-lineage cases and exact AST guard/orchestration reuse | supports | Formatting successor proves reuse of42 prior guard controls via unchanged functions and executes13 narrow lineage/byte/path checks, including forbidden extra edits and archive retarget. No claim of repeated full-source mutation runs. |
| gates | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/post-formatting-gates/receipt.json; current_checks;reused_unchanged_checks;423input reuse basis | supports | Current render, full validate, lint and tracked whitespace all exited0. Full test1256passed/3skipped/3warnings, identifier and KGX passes are reused because all423 inputs are unchanged except exact AST-identical helper separator. Reviewer freshly rehashed all7 actual logs and read terminal summaries. |
| gates-root | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/pathwaymech-next-218-current-gates-root-adoption.json; actual39297/0 terminal1e14c9;423 inputs; initial test child0 from12654 | supports | Root actual terminal current gate adoption preserves initial driver exit1 due solely to lint and successful test child0. Four current reruns and three justified unchanged checks satisfy required gates without concealing prior failure. |
| graph | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/completion.json; actual19946/0/e8d27e;37edges92evidence26KGX25SVG; prior corpus preservation and contributor disclosure | supports | Structural audit preserves218 prior record pages,10416 old edges and6883 record-context nodes. Three aggregate display labels follow unchanged first-record label policy; prior source-context labels remain. Auditor contributed ED preflight/authority preparations; this is attributed structural evidence, not its independent scientific approval or browser interaction test. |
| archive | research/pathway_additions/2026-10-11-next-218/external-evidence/final-proof-root-adoption.json; 171 adopted proof copies,255 original source bytes,11link and138directory observations | supports | Root byte-verified final evidence adoption. Reviewer freshly rehashed all171 adopted copies,94 original response bodies and489 canonical inputs after inspect; fixtures remain recoverable inert provenance, not additional scientific sources. |
| preassessment | research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/preassessment.json; all13 domains and37 current edge assessments; exact provisional scope | supports | This reviewer prepared the complete scientific assessment before final freeze and retained all earlier proofs unchanged. Final assessment follows actual canonical inspection at18:16:47Z and checks completed current replay/gate evidence. Preparatory pending statements remain historical, not current unresolved checks. |

## Limits And Additional Notes

- Native beta chemistry is distinct from experimentally exclusive anomer use. NAD capacity and preference do not establish equal or quantified in-vivo donor flux.
- Current K-12 protein identities are not exact historical/tagged construct identities. Edd historical sequence differences, Pgl strain construction and Eda donor/host limits remain explicit.
- Edd cluster count uses similarity/HAMAP inference; no direct Edd EPR, measured occupancy or obligatory bound manganese is asserted. Eda assay reporter NADH is not pathway substrate.
- CsrA negative-heading/current-annotation conflict is retained against positive indirect original Results/Discussion; no direct regulatory edge is inferred.
- The2012 full article was inspected only in the earlier independent web-only review. No fresh final-phase web read, locally retained article bytes or full-byte replay is claimed.
- iModulonDB membership supplies computational transcriptomic context only, not direct pathway, catalytic, regulatory or donor-flux proof.
- Original independent whole-source chemistry/replay and current root-executed database streams are explicitly attributed. Current reviewer freshly rechecked94 small response bodies and selected SQL/source identities without another full20GB replay.
- Wrapper endpoint checks do not exclude arbitrary transient machine-state mutation or hash every installed dependency implementation.42 wrapper and13 formatting controls are narrow fixtures/CLI checks, not repeated full scientific replays.
- Full test/identifier/KGX results are reused after an exactly one-blank-line AST-identical helper successor, with423 original bindings preserved. Current render/full-validation/lint/whitespace were rerun. Initial lint failure is preserved and superseded.
- Graph audit is static/programmatic. No browser visual/interactivity or deployed-page inspection is claimed.
- Working-tree attestation binds489 local inputs at available base721755. It does not assert that the reviewed bytes are already committed, merged or published.
- Historical source inventories and BRENDA canaries remain context. No source exhaustion, complete BRENDA ingestion or public-release licensing determination is made.
- Preparatory scientific reading preceded root final freeze by instruction. Actual canonical inspect completed9594/0/af5f50 at18:16:47–18:16:51Z; final independent judgment follows that inspection and completed current proof review.
- Final reviewer30c836/0 rechecked489 canonical inputs,94 original bodies,171 adopted proofs,7 gate logs,4 integration child logs and exact helper formatting relation. External exact argv/receipts retain execution details.
- A final-phase display-only JSON summarizer initially raised TypeError on integer bound_inputs; corrected read2537bc/0 succeeded. It did not run a scientific check, alter files or affect product state. Earlier RDF parser, wrapper preparation and graph-harness attempts remain preserved with scoped successors.
- All frozen dossier bytes are captured for provenance; archived negative fixtures and historical failure wrappers are not additional scientific evidence. No canonical predecessor or finding lineage is invented from external reports.
- Only the canonical immutable review bundle is a maintained write by this reviewer. No target, source, authority, helper, history, page or dossier edit was made.
- Issue406 is external GitHub/preintegration lineage supported by exact formatting correction and current lint, not a fabricated previous_occurrences entry. Complete staged whitespace and PR lifecycle remain root tasks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T182037Z-entner-doudoroff-independent-scientific-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of complete Entner-Doudoroff pathway
started_at: '2026-10-11T18:16:47.135343Z'
finished_at: '2026-10-11T18:20:37Z'
reviewer:
  identity: Codex /root/ed_whole_record_review
  kind: agent
  independence: independent
  independence_basis: No contribution to ED target/helper authorship, production authorities,
    integration wrapper, history or rendered pages. I performed the earlier independent
    external scientific review and current fresh scientific/selected-source/authority
    checks; prior proofs are reused with explicit attribution to the same reviewer,
    not a second independent opinion. Root integrated/accepted changes. Other agents
    prepared ED preflight/authority/copy plans and graph audit or wrapper/packaging;
    their contributions are disclosed and do not self-approve this scientific judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: Complete four-position native module with five alternative-aware reaction
  objects is supported within stated biochemical, construct, annotation and source-access
  limits.
scientific_review: true
summary: The entire maintained KEGG:M00008 record is supported within its stated scope:5
  native reactions at4 positions,19participants,1taxon,37edges,92evidence occurrences
  and51references. All edges and source claims were independently assessed; current
  original-source/authority checks, completed integrated replay, full-corpus gates
  and graph preservation support final integration. No new actionable finding. The2012
  article support belongs to the earlier web-only review and is not claimed as newly
  inspected or locally hashed full text.
source:
  git_revision: 721755c9b4af76d32d2b1f232571bbfeab232441
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
    sha256: 20e6c584796085fa8e9813e8398f68424b2da65732bfa51148f2559ddf016881
    role: context
  - path: conf/identifier_sources.json
    sha256: b1db9a993b090bb090f89e5d08be2e3532434492b96660557a8a44ddfdd2094a
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: conf/rhea_identifier_updates.json
    sha256: b6126588233559a7243fbcba3ff4c3a94594831d57c64b3841d4805b1b5a27a1
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: b88634735c0026d6e685fe963c990c0ff1cfaf3dd2a035b5c8bafcf573fa7437
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 36833d3ad51399f277ef6b0367dd9f4d71dd5d12894f47d61bc0d7b81daaffab
    role: context
  - path: data/pathways/entner-doudoroff-pathway.yaml
    sha256: 548eba1d34a081dd293db6d8bf0e00a0e620973e8f843dafa75bcded6a74e4af
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
  - path: docs/IDENTIFIERS.md
    sha256: 543bbaf6a79fa164ab18d45b110741b4c8c96141c8e72f395e5ac5ff06bc1da4
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/infrastructure/entner-doudoroff-authority-and-replay-evidence/2026-10-11T174909Z-codex-971a33.yaml
    sha256: b6a80389baef7ee8f69a746dcd06d82589d128fec4c73b2f79283fa3c0c3cb67
    role: context
  - path: history/infrastructure/entner-doudoroff-authority-and-replay-evidence/2026-10-11T175912Z-codex-b2f713.yaml
    sha256: 1212cc9e1a6fe7f8709547fc45ac5c862db71aa1d0dca6ea4458411a1644931f
    role: context
  - path: history/records/entner-doudoroff-pathway/2026-10-11T173703Z-codex-d014fa.yaml
    sha256: 56daa9fc7c9771d1aa01f9ee46e581d8192c6a323a277ae2c774d3a4efc58c53
    role: context
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: pages/browse.html
    sha256: cdb88039a5d6856db50f7055db0e5a4fa9078a80cb67a1d06504d5d83beafaa5
    role: context
  - path: pages/downloads/edges.tsv
    sha256: d4a4e07494e71cd1096884bcd822958badab836f63adc94e3d39ffa8124674d8
    role: context
  - path: pages/downloads/manifest.json
    sha256: 83a6a2d1e31f5750e453e62dbc80df3cacd90ce99a9e4de38c8e3c1b34ae7eec
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 05b018ed02aa1d12a32d5bd033571498c10b83db72219c98247924aae5eb0e37
    role: context
  - path: pages/index.html
    sha256: ab097ee762bc183f2896fb69b7bde35c73c4a1cea1a5c0d83b476bf9e05061e7
    role: context
  - path: pages/pathway_index.json
    sha256: 4e668d504c5ada21cc33c2101a9c8eb0b650ca427c899cea6018b7c839c4755e
    role: context
  - path: pages/records/KEGG_M00008.html
    sha256: 947255d3314ba4f605974472eb9f8eea46a8157d9cf0de51173683dec39ec47b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/README.md
    sha256: 824f613f47889e87a7d6aadd8a7141c17fa26b65a58a8c05c90b82af852b7bf8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/adopt-dossier.py.txt
    sha256: 2fa520b5adf40b06eb12ed0800c7ae9d541e5dabff81d0e09641856605380dd4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/dossier-adoption.json
    sha256: 3aa8aa2e860797c29a5b1f36866ea545193dd867930c30ddf541750c6d1e30e7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-authority-proposal.json
    sha256: 51b7672bb5e62510855081c9382018cd0bffaf8ba7a9ad7ab6aa536f1ca7245c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-authority-version-observations.json
    sha256: b584e47977df23c253512c031b20addb86b59440792210a7214bc2da9fef04c3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-chemical-identities.json
    sha256: 06997e8e0a2e1a47a06e0022642e22207c35f18269e2db4db5f030724db14d76
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-coverage.json
    sha256: b29c374c126f3d488c348abe525b7cd4a82b1d4914c8dc49df3b0504d32c0bba
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-curation.md
    sha256: 74d2f00a55a84abaea2858c98bd37dab28c7ba5b31ae67fd2e0b45e17ab335d4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-dedup.json
    sha256: 0ebf1f398e1a206988c5af5e557531f49f6ef30818972af115d29bdae58ee248
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-identifiers.json
    sha256: 7339fc46759bb33a670f93ce0cbea1b528715c6b5bf840c5e0e9694cead7a7e6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-protein-projection.json
    sha256: 311e94feceb6fdecff17d64d4ce7856db6ad46ad7349165cdf164b1f64a33f03
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-source-manifest.json
    sha256: a61f692824161ac9fd59cd01dc14ffdc608d75ba1ec6fc5b126486e5068b1506
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/draft/ed-source-projection.json
    sha256: d2699bad8bfb243bcdefce1ec907c636f640ad2be8fbb13704cea88930f0b31b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/ed-replay-final.py
    sha256: 3a9dd4147891e12af58bcffba333e94053c908c814184fe49b151d6c8e2ade74
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/adopt-final-proofs.py.txt
    sha256: f858736d191e444e29fe5e88130782ebe1a9616fae146fe2fff80b36340a669e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/acquire.py.txt
    sha256: 05141e641af9a480ca8a0a541668d0d5c02e0ce9ae007744078ac1f730b6617e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/acquisition-network.log.txt.json
    sha256: 9ebfe98b3f21d6dfbf0c7cef291bab53931afa65b90d7707e45bb5bdd114e37c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/acquisition.json
    sha256: 22018ed1316a15c3f8297171f49e911ebccfcf0595b030a279120e97f02965fd
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/acquisition.log.txt.json
    sha256: 1468df8a12ea0cdb62e92d1631012109a0f425966f783bcdb857e1f11973b5d8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/author-replay-complete.json
    sha256: 448f93e660767a7edbc0ae2f2df3efe3c3b151c4c51239fab84292d1f9056a4c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/author-replay-complete.kgx/edges.tsv.json
    sha256: 759981e4a31f73e808eb937b4fe5366be02fe1b51820110a449217730350983f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/author-replay-complete.kgx/nodes.tsv.json
    sha256: fe062ca28305bae20aa524709a0e31f4bf2306271cd22fb005de6b5defed65f6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/author-replay-complete.log.txt.json
    sha256: 5020076ea7a6e53b2067538108eb14fbd01e0af2dd7bfb16c63f82488cd06553
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/author-replay-final.log.txt.json
    sha256: e8e45a8fd061784519f43b7dd523510336b34b961cc5f3f60d2685946e7a4268
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/author-replay-initial.log.txt.json
    sha256: 58e762df60d9015254ef82a29d6157c459a05cbc30ccf7889b0d2de0aabeb211
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/author-replay-second.log.txt.json
    sha256: afb62de9332f6545e9464095b8e67164ad324ad7731f22726da3d1db49812a18
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/build-draft.log.txt.json
    sha256: 363c49b8e120a5bc14c5cd8a5e8a890ca3fdd315cdcf6e55d5ba418a3696fb95
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/build-draft.py.txt
    sha256: b21aee10bf3735dee0bd2aea17cb10dfffc822e3cdf4e794c0c88ae23b8cd6ec
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/correct-preparation.py.txt
    sha256: 3b61a30b7697a4b4cf0cecc02f4184817e586d9f859ce42fd1c89f9cdd36e3f4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/dedup-0.jsonl.json
    sha256: 40f7fa58bf69ce29ddd7b94ab3fa7a6c242dec76e706b4eab6f1995c6be387be
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/dedup-1.jsonl.json
    sha256: 7bf2fb6f8ab5be6704af5bebfe5c081399fe841abae5bdbafa6bf3af497439d9
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/dedup.log.txt.json
    sha256: 6e6efcd90985013472df70ef0d2a165928fb84a1787d0324b554fb86a79aebcf
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/dedup.py.txt
    sha256: fea784a48f25b32341c388d0b89638f4c532075b462d24748f660247e71c9416
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/draft/entner-doudoroff-pathway.yaml.txt.json
    sha256: d1c3e8148042ca4f0f9accafcc9500e35c70993e300d20068d867f160edb1c5b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/ed-replay.py.txt
    sha256: 660e302cd248e0fb855f7dcaaabef7cbebf5c738d8e8962faf449bfc7ce447e5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/execution-receipt.json
    sha256: b50fc5e8ab3a4d22a1a3cc166684e73ad5b9e55340c4d463cfa1ad5861dd6145
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/final-replay-serialization-correction.json
    sha256: 9778632a0e481771f703c0febffb22487208b1d7382598167a1bcf44156ce402
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/handoff.json
    sha256: 530a760e2bd5fdddab2dcaf372a140f1928b98db1c45b42bb124b97bcdb068f2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/imod-context.log.txt.json
    sha256: 9761d56a29ced1e530e61dbb3796477a8869893a90f7950cb9d2f605de38828e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/imod-context.py.txt
    sha256: 5e2e6276ede4c0a4a39221938f4e63b5431db930ed9cb9e4a6f756fc02867018
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-freeze-locator-preparation.json
    sha256: 7de8ff0c0d953b8176c29d2d3199c6ddace4b4d1501cdac00a67527555adee8b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/ed-authority-proposal-all-verified.json.txt
    sha256: 805c0a318122a6a4efccaa14c5df51cc6e658ec578e4efbca1dd26e37b8508df
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/ed-authority-proposal.json
    sha256: 3a4499d135edd3305101ae48b4684dbced6c656590d37ed77e74b2a58b091d50
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/ed-identifiers.json
    sha256: 30f6397053e29d9666acd4c937edb54b15f9e494065b787beab3823a72f01154
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/ed-replay-final-attempt.py.txt
    sha256: 622253c89e1dbf950d3737acbb63b18ee9fd46398556e9d3e229c5991fe27d0f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/ed-source-manifest.json
    sha256: a311c0a64c4aba43dc2a5b07362fba6a4abbd90fa65d3c31087dd3b064a31195
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/ed-source-projection.json
    sha256: de6abcbb36aa6ed416bf145986907d1047d0cb3c1876ad51a2700adcf369b495
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/entner-doudoroff-pathway.yaml.txt.json
    sha256: 117b4693efa437710ebc0a0c61f0641bbede2b0c548a81164106cf4a53274fde
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/manifest.json
    sha256: a934dfd3f98742f12c9ab285fce2fb7c76d5ab11ceb401528c258f7b54727833
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/pre-replay-inputs/prepare-dossier.py.txt
    sha256: 1697b7c4982fa0ce6c4ee76a437165e3f3c234a72343fc3c9db76917273ef6da
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/preparation-correction.json
    sha256: c67570c63a652de40128c67acf19ad7e398fd9281e9e9912fc0a69bf36119c1b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-dossier.log.txt.json
    sha256: 5e8807614239258bcf71649ff0ed3be2c84aded2a8623e5e127fdf2ca9c9e6c3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-dossier.py.txt
    sha256: e02eb12870a6ba047684d66479288dd035b259ae1052901eb4239801bd72cc28
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-facts-final.log.txt.json
    sha256: 66673b4220ec16f6f8c8879db4c7d7c7c8e6c35cfc7c32de48df321dea57bf11
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-facts-initial.py.txt
    sha256: 1725f8990c055271a64b962a77f504398eeea2cbad02fc34c9b55f6ab4184e51
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-facts-second.py.txt
    sha256: b8cc8cb11cce2d85e6e353eba660bac8f6dffc1e86aa81511e8b7398baa52a7e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-facts-successor.log.txt.json
    sha256: c7f4543dbb8dbc95b8dbf51d3f804c947331fdeda1f214209919582af3cc3bbd
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-facts.log.txt.json
    sha256: 85337a9f7f6a19564ca5462c1600ae2febe440d14278461bc1837ee29e07d461
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-facts.py.txt
    sha256: 0d0f111a0f68cff2cfff18645b2e9da2ac3fcaf329eaca37c7cc73b8eef90b0f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/prepare-final-replay.py.txt
    sha256: fc98f89ae84db11997d699a5b7aabf155bfad0af51f4def065140b71daf17e50
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/replay-final-format.log.txt.json
    sha256: 9da8e8ba9ed69806d74225788946ab9b00d373794cf898b16080f9ae0060f380
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/replay-final-lint-initial.log.txt.json
    sha256: 7d83b631f62ca59409e9af83c1dab0aed66220a5775c50bd3d90342a71b53b91
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/replay-lint-fixes.log.txt.json
    sha256: 0ee3e62cc285d70222a681e7601a69e487c63b4098230ad087e957fb36b284c1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/replay-lint-initial.log.txt.json
    sha256: 76d076dbdf1864769199d9be67e754155aa708450b11c2725d46e8cd83f0106c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/replay-root-lint-initial.log.txt.json
    sha256: 56bdebcabffb2799ff259b4c9a47a09ded2c4ef309b67428e3be13a4de86cc80
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/seal-handoff.log.txt.json
    sha256: b75b2542fda976df3d827891590e4655b1fe038bf0f6f2177671c4ba5bcb6603
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/seal-handoff.py.txt
    sha256: d5eb02b1b5b7d759082eef74065b08fe802f8005bcc629eeb95064f851d467cc
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/author-original/unsealed-initial-draft.yaml.txt.json
    sha256: 93151e57f25b8573d6ec28028d82b0040b272d2685775b1e9b7ae4fccb528a7d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/README.md
    sha256: 654ae0727c8d6a72a00fbd760f3b6cb612fd6b6e83ff14cc20cb7c65ceef018e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/baseline-lock-successor.json
    sha256: 4f4d297e0b9843a8bcc4b916039ded6456edf6df781ea4cb322896de093327d2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run-successor.log.txt.json
    sha256: 3f247926501146bbaa4a53f819cab07d27fc762b477bb99257cacc529d78034b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run-successor/execution.json
    sha256: 7f30dc9f9c8f0a78158e1eb0a421fb77645a9dfe1964fe17651658e1b8935d64
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run-successor/ontology.log.txt.json
    sha256: fdaf1a6f4283872668e71a4a8c8b6d0967ccb9a09af35b86a63c2c5bb355e832
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run-successor/report.json
    sha256: 8bd9fe8660490f5c4ff223513f61408cd983c5d1540465d41bd7af70570487e1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run.log.txt.json
    sha256: 29541a091e6fa8bb55dc1d71349332992bb217f5fe13a02545495a4be89fa371
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run/execution.json
    sha256: 2e2efdf8951ba554e1d195072181306d7bdd96a582e66fae4ca8b68c35050f69
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run/ontology.log.txt.json
    sha256: 24c1244ef091212a34309c82c24033eb990a947a8103d9a968e95294072ce2f1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run/selected-identifiers/ids.yaml.txt.json
    sha256: a275101f2a747451c75a3aa57b073231b91109b02183db68505a3c313e4b6273
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/canonical-dry-run/sources.log.txt.json
    sha256: 5433dc2c0c4bcc9ddbb8b6e2e5731548a3443c7c377355558b7decbfae90334d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/dry-run-authorities.py.txt
    sha256: 9c30b46ad47a87d1f09116cf29f1132d89218abdb73d8a7227b212a678860e30
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/execution-successor.json
    sha256: 4192d2e597bd54a67a24b3db6d589e4e53a9d3d37cf32a7152d50f4840744472
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/existing-batch-reuse-disposition.json
    sha256: bfcd4b24e1dae066fc466b8bf434c1481a3204cee71d17e04a976f89aee4baf8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final.log.txt.json
    sha256: e6ec79bd178e18d7b0c44f7c57bece26496fbcf7806faa82037c323915f2cbd1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/duplicate-key.json.json
    sha256: 9048f874331018a2066402fa244a45dc804111a4ccf53aab757ed82e8dc4a7fd
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/duplicate-key.log.txt.json
    sha256: f5cf22feac2629bdfb0de023831bbade539cf0a661fb7b378accb42c6c72213b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/duplicate-path.json.json
    sha256: 40999c91f456b619e9d135087157fef34ec9ae5dab3b16b2db00a6759c436413
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/duplicate-path.log.txt.json
    sha256: 0c1aae436dfd96f67d28a7b10ce83c41cbf2b4df19103fd694e60933c7727b51
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/existing-output-output/sentinel.bin.json
    sha256: 86a6d7eb575e04c9e82233a652ac946e99ba122762fa72bbf9d83f75732c1e79
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/existing-output.json.json
    sha256: 12fc6be35b354365e5aa707e7ab54ca02aac9c1185fef4c985355df8dc67a0ed
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/existing-output.log.txt.json
    sha256: 36d03bbe0fb261e2ffbf4600f86e15e7cbe4a2e0db8c1258e4c33f023b59aab5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/optimized-python.log.txt.json
    sha256: a88f39681d0feeaf286ca00cbe5eae79f6fa0541423a29d6c0e100931d6b679b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/receipt.json.json
    sha256: 2ae59073202641c705ea3d2828e26f574c18b2ef162fc3986093e2cb6719fb1d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/stale-policy.json.json
    sha256: d53f9842bde881006b3c43489f8ebab7bec0ba5b3b663fd4714b7945f70cde7f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/stale-policy.log.txt.json
    sha256: 884b95ea045621878554db97bff52c951c432ceda1e32e641f539b9af4616ecf
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/stale-target.json.json
    sha256: 56bfaeec3b9a547b157face02f9dfe608aae4b47625e67121030b54ce08b5d62
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls-final/stale-target.log.txt.json
    sha256: 145c3d7c22a409a82f110587f1523eb06d575f972ccc83e856e5b428aea7d227
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls.log.txt.json
    sha256: 3f3ad83a7d36bf18ad11c14eb933a4008380bfbc516b4eb4fb34cf842b4157d6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls/duplicate-key.json.json
    sha256: f822c422a0542c84a8670eb56e9f4306e3645bdfac57be9add8d28649379927f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls/duplicate-path.json.json
    sha256: bb7ebb2ae42d0d07345e430988585d417c5592b51335909d719b3fc9ed5911c8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls/existing-output.json.json
    sha256: 313df8510f3b253581734162c01dae46f5151abe9bf2cadea1724b6d65384a06
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls/existing-output.log.txt.json
    sha256: 692616cadd297032563789717d6ffe92f761df82f464dd0959cadcd691cde8ac
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls/receipt.json.json
    sha256: 84e0df1b807614e36a5e5550eaecc2e019261a9fe8c352f0063ef4dcdfc75d50
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls/stale-policy.json.json
    sha256: 7389b879a17d4fb0e36725c742df25a8c5af6eb55c2c2f46410ee0d4b776b5e7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/guard-controls/stale-target.json.json
    sha256: 6eee60599fb60964a99fed628957e791c7b9ea32051a82480c5bac8fb4c71402
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/handoff.json
    sha256: 8a36895fdd1e8e1587870c77a9f914877b6b48e9a9b7268f1f91bcf0e51d9a0e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/preparation-correction.json
    sha256: c48a76b771969de4895455a45d6292afdf20eae14b09c7b36cdcd093f7ce4e42
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/prepare-selection-initial.py.txt
    sha256: de78b977b6060ffc3721fa48360f2c7da44fa7b5fc8296491b78b26e4481f453
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/prepare-selection-successor-initial.py.txt
    sha256: 150095638fd1fa5dbff4eeb23e6fedc2ab2be4bae88017c42bf11bbcb6b2975f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/prepare-selection-successor.py.txt
    sha256: ada6fbdced88fbb0276b192d3a2f0e1548cfb18404a090e0f0004a78586fed88
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/prepare-selection.py.txt
    sha256: ddba08d81c6d225f4c89052497b66114f917369b040ebc2349fd07800de9a625
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/reuse-guard-preparation-correction.json
    sha256: 50bcfdb821f4e325b6040f99c180441b5dcebbea835397d79279d346e36ba765
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/run-guard-controls-final.py.txt
    sha256: 96605b276c9fb1978b4a3fb434ab3f04f90b9a8f1bf17a2b3dc2ecf257692182
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/run-guard-controls.py.txt
    sha256: 1aca5a3cb940655700a6126927397e603d549e6a2731b9d33e7a689dd4ec4fe1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/selected-successor/proposed-manifest-additions.json
    sha256: adbe623a9ddc9337a0aa5acdb3cc4789f145f104681ed55ad55bdf882523cf85
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/selected-successor/selection.json
    sha256: 732749701f8feef98a8afc40ba7bb9027fb452f54afc55de7e232ada82a3fae2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/selected/proposed-manifest-additions.json
    sha256: 4642339e5a92f5a04cc56b1091b95a0fedabcb8cb91776219843177bc952429a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/selected/selection.json
    sha256: 230874077ae93898939e75ad8091ab9fe7d7750cd4a35b8a6c615d25b1434a33
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/selection-final-success.log.txt.json
    sha256: 33269272b44f918c372155a1c1cb58d6e5908036d13a5b950deaa4232056e1f0
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/selection-final.log.txt.json
    sha256: 8ef99449e2685e97920e4fd4e452250622080f0423be723391d553b7bb66b235
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/selection-initial.log.txt.json
    sha256: 1fea20be83f7b9c044489e8b34f153ecf40675a85c673e7bbad778681caf1a12
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/authority-preparation/selection-successor.log.txt.json
    sha256: 543463a0d7399f68738c49ca3b6fe137f65b67b11c36b56c06b1353c7e9459d5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/check-final-plan.py.txt
    sha256: 46d87cdc100cc19688bfc9788630ffde0af75a51793fd1188b03c5d3a7c0298d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/copy-plan.json
    sha256: fba191e9956d8f58ff379b7e13b7004b84c071f289a6cdaa9560beee2664cebc
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/execution-completion.json
    sha256: 44e9c265cf46ae6eb3444fc741924e6255f9f3457425058972bb8e9adaae26fc
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/execution/completion.json
    sha256: 61195e63c5f6a21a5cfc4b9bf5f2d9794ec4e9ffd49bca320cb6c46480aaf80a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/execution/console.log.bytes.json
    sha256: 5ffc9651e07547e004ff6741d70d145a5ca88a65ea511cc050baeef381584b3e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/final-checks.json
    sha256: c81d34beaf31920d529528d54caf7f0c83eaa77da1696a0ffd2ec180abee75d8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/audit-harness-correction.json
    sha256: 05d485569a4904b3365eca92a1720559ac2e925a557a57513b4aa35b2675c44a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/completion.json
    sha256: f54cd9fcdb5eb86be7c8f76bb66dfdc1e6b02241121f2dec290cdfb9e21e42a9
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/graph-audit-successor.json
    sha256: 1f0b74b028f26290f86aea4fa6141e277559276cb8b923af715b7ba1752dace2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/graph-audit-successor.log.bytes.json
    sha256: 492d8cc764e9371b47d34076a47bb56b4134b648f8c0f340aa21370509f9b6e0
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/graph-audit-successor.py.txt
    sha256: 8d9c0d2bd474938fa0711b71cbc65cc0750db092ee61725ded713a4e600971f0
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/graph-audit.log.bytes.json
    sha256: 4c6787101c1248d7f6887d3a3607b830a40118a8c09ed2d9edf27d8e65845aea
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/graph-audit.py.txt
    sha256: f48e136539e8a36df86f6dcfacac439fc41285cf27568385767976d728d25cac
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/preparation.json
    sha256: ddccd995b5f54e4e7f526ce78b30f3fb101e5025c924bade1627830d9ceba709
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/root-kgx-child-observation.json
    sha256: c5b428993e3eb0e7b042d34d8bfb6a5db1df156625a3798d8298eff4f91139c5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/seal.py.txt
    sha256: 3f9241b0d08eef4cf980bc0ca39b1407ce41aad3dbaedae5bb07f50d22836266
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/shared-node-field-observation.json
    sha256: dfbdc3afee88f9afb80273acd9367160f05956f30ab9592d9f56a81202f1f5c8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/summary.md
    sha256: 221426db6ac0a395cb5c12804be05aa4eca74545d7f4bde363ddee97194b5c40
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/terminal-observation.json
    sha256: 5eb0a96c9278c4737011d37d88ecd67e6c54f5459fa2bf213db90991d3b9ab0c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/terminal-render-kgx.json
    sha256: d444cd6d8eba765c5ab23bcb417552bdbc265a485d435d8f1c903cf6738f855e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/handoff.json
    sha256: de35e31b7cc05eadd9f028adadc59c528aa97d7114e52e0dd8c2ebacaee3386e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/check-codecs.py.txt
    sha256: 049a264299611892e6969a69c39b24ef422acb6eb4b1b2709c1d9b08797adad7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/codec-check.json
    sha256: 768c8fda3718ea2a2c7be33689c09d78cf5e5d467c8ee738d1cd1c744416474c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/codec-execution.json
    sha256: 5367f975e551dec164ee3e305e40e3f93910879e99c4aeb4eb4ec04977af91f6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/packaging-review-disposition.json
    sha256: b9812b47d9e43293a5581d7a949b7060aa87101bff649c5f4b39799e2376428d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/preparation-execution.json
    sha256: a801b681dc4b8b7ca9366217d617e0745e8970cc1a2a1408753f0b3c54e7740e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/prepare-package.py.before-review.txt
    sha256: c0bd5164b3f009f8fc9619c9fcd1e7e220c0bd29b48086e537f840213fb2e69f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/prepare-package.py.before-terminal-wiring.txt
    sha256: 78ce319833775768cfca995a68527f89f1755cfb46d71e944d5c526eff54e1b4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/prepare-package.py.txt
    sha256: 5ee065975781aaad93d70f29eecf6b2bec7b21a7ad1638d90a2b0bd1db21f2ff
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/packaging/static-inputs.json
    sha256: 11b2556fab2399810d3d73f6e9af7f906b3a7666b31042b684a815e2b2d57891
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/identifiers.stdout.bytes.json
    sha256: a974fa25d039c75eceba5d14f335176f7b3505417407f7ed00d68918318f6e44
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/integration-replay.json
    sha256: e5c2730eab40f7bcfd9009ec2990c3efb730d59c6d03209a2ac76692f29ea83b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/native-schema.stdout.bytes.json
    sha256: 53c041d9588f8640863fe0aca1f957638578280edc1573a4f91efa4150c48feb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/source-replay.json
    sha256: 673e996aafb83addec0ce2a1418a82ff7e06f54b413ef1125a27310bdb488191
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/source-replay.stdout.bytes.json
    sha256: d02d5699a83fd635013059a7a94822d661f272a6510059b2e2b1288b48d5b961
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/strict-schema.stdout.bytes.json
    sha256: 5b8cb095b093a17e3cf78f9faaa9237766b26f9e3e28be17b80b9db9ea57dec1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/post-formatting-gates/inputs.json
    sha256: f5bfbb5135e0683c2bdb2a3db039b27f8052add43a1187318c77e379dacab75e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/post-formatting-gates/lint.log.bytes.json
    sha256: e055087dc9859d4ebb3894e8fb12e5588efaafceef9c91aecdb0ad85d6ca6be0
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/post-formatting-gates/receipt.json
    sha256: baf05edb0fbaaba290e8119d36ea54d81cad041f2c8187088588ad80c77e1627
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/post-formatting-gates/validate.log.bytes.json
    sha256: b33523e4f8401407bfef50bd4b3fc1a8c2047e4a0b74449878380cf4a165a6a3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/README.md
    sha256: b09b982166321eaae9b9544e1fd5119ee09057d2a7d4cb650847a29c5830a690
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/actual-execution.json
    sha256: eda0672c35fee56fe8c75f59012a9b38401346bdeb9d4b75a8bb8c772a177e88
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/completion.json
    sha256: 8d0b33adb715c2c28b72ad1a2aaaff42e6ad1810c6f84ea12aa652af90bec6cd
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/controls-attempt-1/archive-alias.txt.symlink.json
    sha256: 618b4df251d9c532fb2a4bbcfb9577d8e06d69abfab4d4c7fbc7a24687f906ea
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/controls-attempt-1/disposition-fixture.json.bytes.json
    sha256: 10511a1f4eafbea1c5f288a76ee1126c4f1cb65bd0ae5b0827cacd3aef8043eb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/controls-attempt-1/results.json
    sha256: b1290a0ba77a8c14541960976450b10bda34c25da39aeb976bc9d364c1c8a1cd
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/expected-bindings.json
    sha256: b4a286541e71e883f282c7e54379c732171787de85be7aa6e715a84d86be99fc
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/formatting-controls.py.txt
    sha256: d803922164cf4d1b2b7ffd366a8ebe3feabd3e326f9356214cec74e9fce4a535
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/integration-replay.py.txt
    sha256: c3a4023d8992b486ea9b1255dc4942f1da1db05d22262e38a7bbb49c06b86752
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/prepare-bindings.py.txt
    sha256: be385b8d4adc50127a9105afdd283af342d9bcc7178ec6a0a0ce893423ab2e7b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/proof-artifacts.json
    sha256: 758cb6cda2e9ba822df69007367437f2369602112c7c6be30f3db4587cc02d33
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/seal-preparation.py.txt
    sha256: 2bdb4d8fd5471f922921e3aeb77f092ee4cebd8c22de4b55cf6de995a2a36753
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/README.md
    sha256: ffea2ce543d7684a0ada962f308391de52dcb38f26aa9fd0f9e8362baa56ca56
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/README.md.before-safe-path.txt
    sha256: 830a6ffaf2214a42c8fdefb6ee6d265586d30faef2a6de92355054b3b0da7390
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/actual-execution.json
    sha256: b22544f7658027d95f0d03fd4ebc0d1cb317e1ec91c16caf08307991ab7a796a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/boundary-controls.py.before-safe-path.txt
    sha256: ff3422b13ff096366bdb08038489716d01b62ccb4e480e42b99e48ce75b8f3a5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/boundary-controls.py.txt
    sha256: 566f428ff79f3cbef472b67c28958308856815f8959ac0d8c206af4f8bb0c678
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/completion.json
    sha256: 7264b2f2898fcbd41e49e60e134dc11caf4e19be2170cc0a0ac737f9665a61d4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/argument-repo/helper.py.txt.bytes.json
    sha256: b0f79da099799df2cf93ce78ad93e2188f1058a2ece6ac06c5ca21a8f895337f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/bad-manifest-digest-cli.stderr.bytes.json
    sha256: a2af2298d1e777e8a8839f59fccdf755531b0eb64ee83850524610ef1f1f9b59
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/baseline-stale-pyc-consumed.stdout.bytes.json
    sha256: c8763b8e40ac83f2e17edcaf4c0de84fbe3aff828837f4a7f6585b70b9c83e27
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/duplicate-bindings/manifest.json.bytes.json
    sha256: 2edba10acc274c52702597d051bb52e022b4328adc173d0c85b054d6d57d5f99
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/duplicate-bindings/runtime/input.txt.bytes.json
    sha256: fc62fa4a27bf4a5c2b15826c4162b794bf25e4184d609b8aff8f4efe9321764c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-authority/manifest.json.bytes.json
    sha256: 83e7cd4ebbb3528bcebbd40cec644fcdf9beec1d2221d9b5600d1153dffd830c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-authority/runtime/input.txt.bytes.json
    sha256: a03115370818a1d89014a7d84d800cadefd5b4ea434b696936092469354263d1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-environment/manifest.json.bytes.json
    sha256: 6b07eb2d2e1084358c3210fca63d670a51c2b20cfa8f33bfdfda41aace609995
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-environment/runtime/input.txt.bytes.json
    sha256: 2fa64fd139c9aed30732b713b25ae022cba1731cf2fca07bfdc2abd9a3821794
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-inventory-add/manifest.json.bytes.json
    sha256: 12bc2acfa4f4ba326c92e0572c92109042eaeb85ed2b68fef757def3e43186d7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-inventory-add/runtime/.ignored-new-runtime.py.txt.bytes.json
    sha256: aaec237701c654211022f8fb9dc0146234d08950650963536e18cc83c2f446ea
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-inventory-remove/manifest.json.bytes.json
    sha256: 75165f23a7c57fc7ecd68b650420ddacf763c5f96fac03cbe5ca5aa12003bbf3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-manifest-symlink/manifest.json.symlink.json
    sha256: 3fe7af29475d8cf565236fef5cdc62b99b389221fdf079e89eb1252a3517bb42
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-manifest-symlink/original-manifest.json.bytes.json
    sha256: 4376e416573a1022f7e35ea82e8f329c645664bc63c00cb6411857bdfd65fd32
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-manifest/manifest.json.bytes.json
    sha256: 2ffbc21f9361346aec2c56064838b18672f016f85ccff720e680031f84c4142f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-manifest/runtime/input.txt.bytes.json
    sha256: ba1c75306d67a04f8ec342ab6134793112dc7db7f625b96727290d54261b179c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-own-manifest/manifest.json.bytes.json
    sha256: 7ae41d6a47e783979b94eb234848faaeb362533c43f6ad41364770045d2d2fe1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-policy/manifest.json.bytes.json
    sha256: aa308c7f86bfff7bf546bb1574895bf049112697aac058f5a4528e28cfd628a2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-policy/runtime/input.txt.bytes.json
    sha256: 6881ea132b8338dae07e86212a47a1c2e584889cb58987f24828532a34fcea3d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-prior_proof/manifest.json.bytes.json
    sha256: c4d10f7ef51713a387571a7bc2c43fecc9b3913894db7ace17087be6397538c3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-prior_proof/runtime/input.txt.bytes.json
    sha256: 52a3045e8eb2b3b2ac031a9be1b9ac370b5612fd16bbbb8cd4013e974a9f0d09
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-runtime/manifest.json.bytes.json
    sha256: 864ee8cb91398d266324d2f03aa4d88c4580081827109b9b07cd1dd1d8664042
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-runtime/runtime/input.txt.bytes.json
    sha256: 7c89753da0f284eef67105559bf0a25953e3f32fd61a3a87bb5b3dffdb0f6b64
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-source/manifest.json.bytes.json
    sha256: 1664896cb9421572af0f138ead0e8ef8fa7d6fe3e3eb96b89aebe00a6aaa5ed4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-source/runtime/input.txt.bytes.json
    sha256: b687f243fab63d971ebea1acfebc01364aac7730cbeda9227d3fcfc571c95e7f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-symlink/input-alias.txt.symlink.json
    sha256: 25eb5afc2accb728049cae3e7cdbed1ba4b9c9137689a3062909726c7e8f417f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/final-symlink/manifest.json.bytes.json
    sha256: ddc22a5b9ec4cab885d787111e8cd5dcf7385eaca605e20de8ab2fa8f7aa8a0c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/fresh-cache-prefix-uses-bound-source.stdout.bytes.json
    sha256: ad40ba62604611742c676554177ee2ed1ce2df304ebfdbb2e43c0507911570be
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/late-pre-import-formal-change/manifest.json.bytes.json
    sha256: 456d30d9ce454a8f08b81f074d125da13c0cfe37a23c65479ce48940ed2b5e7d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/late-pre-import-formal-change/runtime/input.txt.bytes.json
    sha256: 7bb68ec0a5bd915f974db0c68b7eb59f2702f6557395eb76e99ac1c31114d708
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/optimized-cli.stderr.bytes.json
    sha256: a810329503314911cb2506ac6f4b4f6c6db73d0bd22043bad76356b1b5b6a251
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/output-fixtures/dangling-symlink.symlink.json
    sha256: 6bd5ec7e3b88472f330e13b5610c91ccbd29d47aceeca4209388f9e369a3991f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/output-fixtures/file.bytes.json
    sha256: 21f5c9097148a40e5ea3117208a546a320fbf0e5f1a40543bc35c5ba26bb3c11
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/positive-narrow/manifest.json.bytes.json
    sha256: 6fbbaa05767837ab3aa787d0020a81ced1c390a3b8a74e06d682fa1addb14e0e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-authority/manifest.json.bytes.json
    sha256: f189e1af4f6e21c9180b99f1d2bf01736a44f2354d3fddbe6c5e85a6585aead1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-environment/manifest.json.bytes.json
    sha256: 658ed1b4c2a3bc0bacc722a705be69a3151472a67e432705f965cb5b53e0962b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-inventory-add/manifest.json.bytes.json
    sha256: 0f8d40bd115c51bde7683ed5ac8fe21c4233fbe3251ff7a235e4c92a6cd8009b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-inventory-remove/manifest.json.bytes.json
    sha256: a7f6e08c3136c2bc6f9dcc7845f79e289fd4c2e540077f4b72ee99a1846bd13f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-manifest-symlink/manifest.json.symlink.json
    sha256: 206159b7c373a7e41ef1e6b629d07677e57c727d2dbe610a62ba9cc7b819a1e2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-manifest-symlink/original-manifest.json.bytes.json
    sha256: f4349458a9a639abe932c3406da5f9119197c0b28879660a9b27bf3845d5c8ed
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-manifest/manifest.json.bytes.json
    sha256: b116e3e9ae5047fa6ec1d2d09de48afe4394c225a925ba9fadd597c53b77da36
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-own-manifest/manifest.json.bytes.json
    sha256: d3660b10b55924938de05e12629438b2f09f3f384c3c2c93809dcb8a00446508
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-policy/manifest.json.bytes.json
    sha256: 6434decaf88d15f05a723e53cc5ccf5129107e46229fa7e5a9b490e9d8451139
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-prior_proof/manifest.json.bytes.json
    sha256: 7c1acfb23c072259448fb2fd4f71784792fa3a9093c38e6c2bd8760fb1ca64c7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-runtime/manifest.json.bytes.json
    sha256: b73e66efea965cb0eac0c0504f0742a887dfa2c9ee7973a4176c720208e48573
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-source/manifest.json.bytes.json
    sha256: a5a6c09afe395e6c65ade71be1ff0267265120051ba12d153ce77d46df6ea20b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-symlink/input-alias.txt.symlink.json
    sha256: 47edb0754e007575c822785b06a442f7a71b42f61c79c0adc6836ec7e07da3d1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/preflight-symlink/manifest.json.bytes.json
    sha256: c6c68b869538cccf26e796af934eb4249e9c560852b51e63d7402f2cb8830531
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/pycache-fixture/bad-source.txt.bytes.json
    sha256: c3c9c2bd81b41dba481873042f7cb32e4602520ec5190e3389fb4872e5e02fa3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/pycache-fixture/src/captured-pycache/guarded_module.cpython-313.pyc.bytes.json
    sha256: c5e02c7dbba7b957f52a895d93f81597d3e60f6cf853b324a3fa80f3ea3bb5e3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/pycache-fixture/src/guarded_module.py.txt.bytes.json
    sha256: b3e31ec0dea2e29f816290c1c2f456928c309a4920637aad651ea9e4fa9b2ff6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-1/results.json
    sha256: 7945bbb0f72d99ce0ae2da846023a1304e60dbc4bfedf24f0ec247e71dd81024
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/bad-manifest-digest-cli.stderr.bytes.json
    sha256: 235a3c29eeb236a7df3e5a3d02674503e1e452321be8ef4a3788418e0f84efd3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/duplicate-bindings/manifest.json.bytes.json
    sha256: 735b63892ebba378de75c9c1024748e3cf1f15534080ee11d63f790bb7fb6a0b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-authority/manifest.json.bytes.json
    sha256: c957c5a8875903363c9fcc1c2560eb717e83ff34cd350bad3bd464ae5508fee6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-environment/manifest.json.bytes.json
    sha256: f73148f49a1b05f81169b20ac6a1b323d0a95ce873fa539d9e073a44b1282918
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-inventory-add/manifest.json.bytes.json
    sha256: fc196207a1fa2d07c0c6b0106811ca567b6990f232857fffaacd19f57d5ed306
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-inventory-remove/manifest.json.bytes.json
    sha256: fcbe892fd0339007a58e9a31fc2e542061e8340414ebdff6e1833784afa521fb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-manifest-symlink/manifest.json.symlink.json
    sha256: f48d2792fdb8faf15719cd98456c488aec96185e8e911bdf93469943c94c7d20
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-manifest-symlink/original-manifest.json.bytes.json
    sha256: 363340163acac1072da15921b15e70d1781d1a7c631a9bf2abc47bb564cd996d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-manifest/manifest.json.bytes.json
    sha256: abf99c1777c71d9d4614765bb177acd59a813024b6852ecf9d97e98d80d7f220
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-own-manifest/manifest.json.bytes.json
    sha256: 0ca38998ffbc6bea9f44f7b7504136ae73621fc0f9214e4fc2d9a0384b076c29
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-policy/manifest.json.bytes.json
    sha256: 4b82e519ae2ec1b45cbe8688b20be98a573c32e312d55d051787a18c1b12d492
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-prior_proof/manifest.json.bytes.json
    sha256: 332b7567118868158f112051e8369bd44d4b375a83b264a739739bfc76fe2dfb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-runtime/manifest.json.bytes.json
    sha256: 139f3d4e79a59e5bccfec8771345427f3d5fc6960d4ea55dfd90a9c2105115d2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-source/manifest.json.bytes.json
    sha256: 5de569c70b2b555a2c4a18c7b1fbc4efd456eea9879cac18123ed8d0f576d46b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-symlink/input-alias.txt.symlink.json
    sha256: 1c912bf08a48adc812b76cb7e4365b53ed4a30a0c9aedc748d500f403c01e7f7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/final-symlink/manifest.json.bytes.json
    sha256: 0a6452f7a46fb85c31024a1529af0388938e432580d76a7af9fa109dfbbb8b48
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/late-pre-import-formal-change/manifest.json.bytes.json
    sha256: 02cca6f759ace308e2d2a0099569fe39ee78ea6225929415347351a3b718a0d7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/output-fixtures/dangling-symlink.symlink.json
    sha256: bc6d9788a50b1edff2d544af6ca70c3572ac554f8cb2a04c8b91992cb872e00c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/positive-narrow/manifest.json.bytes.json
    sha256: a6273c0df23c68a64e564437fe4b62b3794f3b8ff8d9227e5c8aa458783b4bc1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-authority/manifest.json.bytes.json
    sha256: e99ec63a425d0e6a828d1fe6175c2eab7418c3d3afcf96c308c87cc2a5b3d87c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-environment/manifest.json.bytes.json
    sha256: 43ebd1ee648cb3f4d9b03e29a84c518508bcb6f607297f8800c69df7b66fb44a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-inventory-add/manifest.json.bytes.json
    sha256: 8b9cec6fc549b8577348ec263f39fc16b6f0042b52304dc0730f433265e811a1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-inventory-remove/manifest.json.bytes.json
    sha256: bec7746eb2b454a1b1ad5f536b7c40942102cd421978c93bf5cba9baabf68fe1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-manifest-symlink/manifest.json.symlink.json
    sha256: 3aa368849755473522c610741b97e35cba7c023e8d5cf6ca92d97eb01478584c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-manifest-symlink/original-manifest.json.bytes.json
    sha256: 288274c6aff188c9feadcbca0235266653aa572ad768d656fce827f355bdf96d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-manifest/manifest.json.bytes.json
    sha256: 363986d2c01e4bf62a71ccba015e231451b7a1990d3b68a7a2991699d194c474
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-own-manifest/manifest.json.bytes.json
    sha256: cd2309713a369264942a448586cd006a8bec246376f370382985286dc422ed6a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-policy/manifest.json.bytes.json
    sha256: 64ef05630db927eb7113998d2a608921f0a1f497722dc23335c7014fd557fc2e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-prior_proof/manifest.json.bytes.json
    sha256: 209099c549ca04427d86120edaebf45eea65e4427eab5d8f51f159d4b158b6ac
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-runtime/manifest.json.bytes.json
    sha256: 1516d7bf0a967da6f6af9c5ce5d21e92f9fbe9f0670671edbb9237527ec31abb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-source/manifest.json.bytes.json
    sha256: b56f35af0c7f795141bcda6b02b58123d87604e0fdd025f05216193cb2d0afcc
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-symlink/input-alias.txt.symlink.json
    sha256: 18dadcfa7fe9da2d4f89cf30bcad377d7ae8f8dc39f1e43373b405b4ae17cb26
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/preflight-symlink/manifest.json.bytes.json
    sha256: 78049a55710273a2e337f9df1ea904de60e840def920b70054a317b80de5bd07
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/pycache-fixture/src/captured-pycache/guarded_module.cpython-313.pyc.bytes.json
    sha256: 8e0a6afc919fbc0a40d20ed151a4376557b45ff4f9650fe89f1308a8512b2755
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/results.json
    sha256: f1c6811503a2d00f0cc31e26185cb1216826f8aff1f953856554fa6c8e7f61ca
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/expected-bindings.json
    sha256: 9098dfa9b03a3b5d3a161b4b7673fd7b50e3051ba0ef364a3e646ab501cbdd9e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/integration-replay.py.before-safe-path.txt
    sha256: 130566b640191e12d66ca8a2f083105d1eebf823ae034882cf4d2357bee4f36c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/integration-replay.py.txt
    sha256: a60587397a1f2b38dba30cfe8df0c69c621554424d1d5ceb9cfc308e01b75f8d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/prepare-bindings.py.txt
    sha256: a9baf969605ac68278b483094ef8dc6cb86365d78a43d0db4cea09a152781295
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/proof-artifacts.json
    sha256: e3a09402d5be7b9c9cbdd1323f132ab1d27289d28dcb13353f9dba312f73dc82
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/safe-path-correction.json
    sha256: 805504eeeaf858545e01f3f3047639d419d4be7de0e5bc40ab05e1dd6f1fe070
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/seal-preparation.py.txt
    sha256: c03ab4890186e964951bfc053e625d6ae0beabf57661f77885612ce2d25dc4d6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/actual-positive-terminal.json
    sha256: 785f9c9b2d1adb6591a8427d224c53d61b77041f4eca8643ca5ec953546b8ef8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/integrated-replay-root-adoption.json
    sha256: 126e217c172b050dacda5338c6c66ca6a31bbd139aab4b220e49a034355c647c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/pathwaymech-next-218-current-gates-root-adoption.json
    sha256: 965055f84b01272e00629521610521c91a9bd8551e093f49efae014b29801753
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/pathwaymech-next-218-dossier-adoption.json
    sha256: 3aa8aa2e860797c29a5b1f36866ea545193dd867930c30ddf541750c6d1e30e7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/pathwaymech-next-218-execute-integrated-replay.py.txt
    sha256: 1867084132021d4850f317b0624706508da1b77c3a50ae198bd7402f5a0060c4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/pathwaymech-next-218-graph-root-adoption.json
    sha256: affb37c255d61609c87f364c7bef01ac7a6149963e148e3d1f98a75ce6cf06b1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/pathwaymech-next-218-integrated-replay-root-acceptance.json
    sha256: 508fa90157eee4d27e24f256be74a8b43ea716e2c34d4d102dbf5403595bb886
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/pathwaymech-next-218-post-formatting-gates.py.txt
    sha256: 07b154e5983188a11b9b7bd8d8b3e5d19a1cf4315aea18b1c6523bfaa8caf7fa
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/audit-script-lineage.json
    sha256: 61aae53393e7504ad58a800cd83e6718f6c979f1825cfc9bcd94ca6049b842ad
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/current-authority-audit.json
    sha256: c84bc0e5efaf1bc018630e5a41135e6e85da2214299b1c256859413ba2c61bfa
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/current-authority-audit.py.txt
    sha256: f3c0d9892dacfd15ba0f21b86295eb2c02d1f38b77512d313b95f5265780efe7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/edges-compact.json
    sha256: 3d71a7b7c08fb028e7672fd09a045b7ca457526ba28e8f52771e4abd5a18e808
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/fresh-original-evidence-audit.py.txt
    sha256: 74377fece8ea23179203d0d2c39971bd53ababf6448d7b74a7ad87346f097a60
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/original-evidence-audit.json
    sha256: 88d84ac8e8a3b07a1cade10a797576f0d518ad49c3d4d7bd1a757b132cc4e5c9
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/preassessment-handoff.json
    sha256: 7e7aaeb52bfe985af0b2a4599b26b0109b06adb258113531ec5d48c0510bf22a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/preassessment.json
    sha256: a7112e22ed2340ac00bca610407507c18bf8c7ec1b9a142a2384a003ab2fd468
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/seal-preparation.py.txt
    sha256: 013056b0e3aaac87f2484f9f1aa0e0d2bafd9bc04b1ac9002b65d329bd3edd38
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/unique-evidence.json
    sha256: 11973c66cf9cd8f8eb96a3567a29c04f37b85a061f4251e15134f3f4aaed5ec3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/support-copy-plan.json
    sha256: 4ef7b1f4832078778ae6d46b40a96791f41ebae83170d521d39daeec90c6890b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/final-proof-root-adoption.json
    sha256: cc2ed821ae6a64347a7486858cf888bf1c7ea3ad38c38b5fba96321bb7e2066e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/adopt-formatting.py.txt
    sha256: 1ad0e24f862c7f4ceb2291afe3b20fc3822f21791535ebf7ae698afcf9ab23a2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/adoption.json
    sha256: 3fa6bb139a923d571b7c3a59df2583b3d159d91e0b3f9a35ee29a12657e3120e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/diff-tracked.log.txt.json
    sha256: 32a03e3251ae8a0391b5658b92cebe60442a1969d57db97566e053b20eea2ce9
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/ed-replay-final-original.py.txt
    sha256: f67d96bb1601ac0dce491886e9f28a119cfb355ba54d16f34d2e1121ec030e9e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/formatting-preparation.json
    sha256: 5e3b8a5075e507381577453442fdf93c935ac15242bcc28f6e5554d11414e118
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/identifiers.log.txt.json
    sha256: 4321c0c2495830a8039a5af321bdfe215c0fa2a572cc8afb453efb2f23191f3a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/initial-full-gate-driver.py.txt
    sha256: ed1db4c530aae4daa345d8078b66c286e55464ec05c97db3acf5a6e329327e4f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/initial-full-gate-inputs.json
    sha256: 2103deb563f75351a6c4ad48f29613ab71b42e572443c0f6df849cf043bdd28b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/initial-full-gate-receipts.json
    sha256: 4580f78d262386f6c45e3edfa7051d8c023a6a6e220aeae00c29c5ea4abf639a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/initial-full-gate-terminal.json
    sha256: 617f65a3c943cd20597fb8b4982f9d35ec148e7166a0d4ad08190d9f22928c49
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/kgx.log.txt.json
    sha256: 65c779dea689142c6e66e90027385355e3f32cc9b9d24453593be153e81139ef
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/lint.log.txt.json
    sha256: 50a9e9f1c65132e4a438bfd13f3647162ec8b10f1e9ef199f09f7d2958cda889
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/render.log.txt.json
    sha256: b6e0c8294e784b414bebde48a6ec8537d79c59b75b1bf0b5cebd1460ff8dbef2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/test.log.txt.json
    sha256: e6c26ed0f70595aeee7340102607cf56192487168bd3e7a9cbadc397f5a0585a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/validate.log.txt.json
    sha256: 11f4e3f3f151b3d4a76d418a6212f1d0485d27032f7409b1fe9c104f7470a572
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/authority-metadata-audit.json
    sha256: f726f1810194b907cee9d85f12214e53d158aeb8e0a779caaea25785b16f1f6c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/chemistry-debug.json
    sha256: 8c2a0f9e25839e8cd44dd4daae17a7844756d9740bb5891e3afcefdfdd79cbc1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/dedup-current.json
    sha256: 7129700eeba1f34f7a3b936e25cafc87542a749ee669bfe2b4fa2c0fb2996f0e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/dedup-current.jsonl.json
    sha256: 29b58f06f3e7442b4334a4f96430e0ca848fa3f16d08d45ec3bc4ac233caee63
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/execution-observations.json
    sha256: f05eec5a07986519722dc38aabab5e55fd71dc89c233557f98e75be2c69b27a7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/final-guard-exact.py.txt
    sha256: b601fb65ad0467683b5f685e8acfcc43ca231761a01973bd644bb3548143926b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-controls.json
    sha256: 65cc8bef4f353460788da6f49ad5ecc60092c05f5fa3f83a60e2801201e64ed7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-controls.py.txt
    sha256: e31827e3277227d66451c26dbc38a1060e312b4e4073cc98607521438e37336e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/clean_control/proof-0.txt.json
    sha256: f226c27db7eefeaa15899f1d20259eceafd1a82b229ae0c3b82f58421905dbbf
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/clean_control/result.json.json
    sha256: e2207063a6925bdb7988dd5950162a7ad1c4923c784da83ea24af8b714e62594
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_formal_bytes/formal-0.txt.json
    sha256: cf406a948f64319a3698b29071f8713867da83360c6610d2f3273221af43e24c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_output_collision/result.json.json
    sha256: a27c7b8d69e6f71bc195d4adf90e9f52444af538e868879ec0be70d4d9a35280
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/formal-1.txt.json
    sha256: 9f425754cde6e4309c8535e9e69e9f791d175cc8103ff9a7753857b9fed8680d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/formal-11.txt.json
    sha256: 8f598b045b160baf7a3333dc7fb9cb1da013dc91bdefb8b575e075eca23f3632
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/formal-12.txt.json
    sha256: 016bb7cefe5a904434e2a61215301e5177b69cfcb2f79f7b65104ff3abd0222e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/formal-13.txt.json
    sha256: 284c6aa7d4aeb3edc3c713596d4e51e45f1aec98da6f722dd0bb6f576e6dc227
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/formal-14.txt.json
    sha256: f57c9e95b7daa94907f463255b5b156fbf5dd13dd8ede61b5fe06c5857240a7c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/formal-17.txt.json
    sha256: a0363cda408a9ae7072a37aca4cf7f228a5d76191656cfef29139106619383be
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-1.txt.json
    sha256: 046f43158db22179c87d0afcdc96b9f3dbc3d8ed7d2166f9170ffafc9c1936c0
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-11.txt.json
    sha256: c6fe8cb458fb5dae20f86f1b7093c500abcf85b743cc699f157ce0c2e6c56ea4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-12.txt.json
    sha256: 34ab74386cfdca1b37d2c2f186c4be9112a201895de5c5485987aa592b8c6024
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-13.txt.json
    sha256: 648e11fbeabc9dc9899c14c8c8ef2fc3b4b026587030c8a4bb539ebab5972a20
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-14.txt.json
    sha256: b6c6c20b00754d6c7081f00feedbb7c14c8035391ab893a554d462a27bfdcb79
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-15.txt.json
    sha256: dd484157a63ffcec4d9d0909c4e09d748128e2ce8ac35ebb1033819949f76003
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-2.txt.json
    sha256: 4a0f7780e787429ac31c406e286880d7503375d4ff2a76f3adb976bbf9b9d630
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-3.txt.json
    sha256: 2bdc317c7718472cf76697915c16fffcdcf87b47154f4701831b4e5b3b1a3cbc
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-4.txt.json
    sha256: a949a3a210125ae24fd460479f57af3287eb7fda815a1f5b119ad87e1a9ad838
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-5.txt.json
    sha256: 28af9ee325b8f73dcc61cc2f1c63a0819aeb8a67cbd0ab2811416bc6a2daf52b
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/late_prior_proof_bytes/proof-6.txt.json
    sha256: 3f33044203502bd5ed3f690e0bc2ee60aca9f476fd114971de31a6db506f16a1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-collision/result.json.json
    sha256: 8b1540ebe47953412bdd96c7341be1238821eb2a118932291741f029eb7e6485
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-collision/stderr.txt.json
    sha256: b901713de279d7ec582f01515d36cbb192b8c9b730d913693802f637080af25e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-authority-proposal.json.json
    sha256: d2ec246055dfca2b0d953c698f3ef961b77fa6f951216bbe348da4588a58c569
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-authority-version-observations.json.json
    sha256: 98194180b3ba5ff30dec7b886e1b5d4d40599b01a6434268429c9b7706661765
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-chemical-identities.json.json
    sha256: 87f5307af39dc227b0bc0ee43f426895be00395f1b4cbbb558eac561afa0aea4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-coverage.json.json
    sha256: 84fc90550d0079ba54e5fd73246beba105624b795e5a64fdaf5939b3933c63c5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-curation.md.json
    sha256: 6e48eceaffa8dc7a20d0989847c201f73f925b4f708769703044e224a5b6825d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-dedup.json.json
    sha256: bd2f4859eaef4f2bdcf77bf922160eaf6e284e39656ce3f7bacee0c7021965ca
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-identifiers.json.json
    sha256: ab5022c66fc490a8f5ca73c72d203e23dadb35652f0c22a79140a57198734ac6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-protein-projection.json.json
    sha256: e2318f36e404c8ef4fba361fdcb1c03f965c07246db792d1e2e20c3433250a81
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-source-manifest.json.json
    sha256: 00cae7734cf278d02ee0d3b973a9fcdb19a0cdcdeddbc26369472c46b29903e3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/draft/ed-source-projection.json.json
    sha256: 9ba1533f760d138b46da8205fbae2b7218d0cd540e3f7842b1403781ede6ddd3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/ed-replay-final.py.txt.json
    sha256: e1c0a5418ee310971528b203e712615a5633a3f3271831194dbb7ebfe2f12c5e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/imod/context.json.json
    sha256: 76c990fa103fbd5b00a09e68171dba276e0cb406149512af764dfb32b618fe09
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/imod/manifest.json.json
    sha256: 9ca028e70423eb21e273e7362a2e5deb214285748e15e86982c7048e414ff9d3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/imod/runner-availability.json.json
    sha256: 50eeb42803d9134f7c2d7a20836bf547eb7fb7c0fe6003d544ab0595909a3729
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/prior-proof.txt.json
    sha256: dfaaaf8da29308f21eb933cc6e4cd40e2dc58d2af838ccd7eebc21d5eff264d4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/guard-fixtures/startup-proof/stderr.txt.json
    sha256: 2434becab778b2ca5505775ff2a9f4057844bcb35e04ddcda4954245dbd2a5d9
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/handoff.json
    sha256: 0ee3b8928116ee1281858b5b3342002242addf42f50447494ddac14a5c99be26
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/independent-chemistry-initial.py.txt
    sha256: 52aeef5f368bfded63f727ab72c86a8b5c0352a053de19a1fb9267d8985395bd
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/independent-chemistry-successor.py.txt
    sha256: 1978a7e8bedaa7210b37b2edd80948d34214e5fdcd03c389660c5f9a73df7f86
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/independent-chemistry.json
    sha256: 90d417893922c02da209e0c33a2abfc5d58481c3f33be68a2aeff5860df8a20a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/input-capture.json
    sha256: 0bcb990a0b88e1fbd3c69209081822a84267504a5cba02a5431e0a8a3237403d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/original-evidence-audit.json
    sha256: 36c9c2fc3c68919f4108ee284e636a72f49234a1db37ab858bd01cfe89099973
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/original-evidence-audit.py.txt
    sha256: 15dc9daf3dc24b8a67362fdc6f7390ef0372f943513d41878d3a8ea395a60da7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/positive-execution.json
    sha256: 80f01955385772e1fe76fabfa3511567e487d9eb2d7863ed1b50e0065b4889eb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/positive-replay.json
    sha256: 8512f36aa2c6f45d46d7639ae6deacec7c634e6767611e1a5721c6e602f7db3a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/positive-replay.log.txt.json
    sha256: a1bd5d2e3ba8c2379480d26c6077c80f2d3cbad3fc9cfbf307067968adb66651
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/00-handoff.json.txt
    sha256: 57e84afac48c28c97d4e5c3dbbb50e2f449d2777369adc079d99117f9232c6d0
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/01-handoff.json.txt
    sha256: 66de856cbccacbfd004161fb6dfa95d565e0537f63c183d57e2c3089cfdd4635
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/02-decision.json.txt
    sha256: a4776c699689484a68fce5b3059e443f33c4f731fcf3e8daf5ee8dc55e5f2f07
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/03-original-source-check.json.txt
    sha256: 093655981c24c6a13572d29706ef1a1fdcedda7ee9e0e1e505ebcf6cada43c74
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/04-source-observations.json.txt
    sha256: 9c0ffc0570b32635c3fe2a495fcca14c4664346fd200a76cff2bbeaf242bd38d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/05-pathwaymech-entner-doudoroff-root-authoring-acceptance-20261011.json.txt
    sha256: ecfadf3dc9e8546d3bc50bfaca35f764c1a50a7219a5a22aaaff18d6113884fd
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/06-completion.json.txt
    sha256: 97c9f538c34f36f72d07f03d2d088b599e370cae273e4c5b61b041138523d424
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/11-acquisition.json.txt
    sha256: dbb1d5455d80294befc2ec4af3b539088d8fa578d3fdd99f5848f6f52452c2cc
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/13-acquisition-network.json.txt
    sha256: 1fc43c20d27f571c3a904c39d435f8a4c0653f40c0060de6b999d8b38ac50ad4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/14-acquisition-extra.json.txt
    sha256: 29a17949b580af1a721758dd89c76713b82700922c892a70575002292631a027
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/prior-proof-archive/15-acquisition-figure.json.txt
    sha256: 5f2927f551e78281435f24b1b4473efa4c33ac28f8cb77969bca1536fe0f5b9c
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/run-positive.py.txt
    sha256: c81c125c4175f26c6a23ed0d3b87af42c69c1f6727126eb2b37c246d3df8e8fe
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/seal-review.py.txt
    sha256: 1d6fd97f3b9f8ecfd82c3af21d4dc19486aeb70943225e9a3acc8d3ca1ce9abb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/web-primary-observations.json
    sha256: 39768d5a2325f6f7d7dc002e35845f27fed03a0ec94407d108bbf9519736ef62
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/whole-record-review.json
    sha256: 461212427906d7d609c8d3373c355809640ac86a3cd720b2ad1ebba821322ee4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/whole-record-review.md
    sha256: f4ae08c3d129be8428476bc8e9c418667f5375541b44aa715d19e6dea478fd04
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/README.md
    sha256: 925223a98a05a091a3cbe6f29163767cfcc04d094b17f76467a2ef081507ea5e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/build-plan-initial.log.json
    sha256: 602ab571eeac6273905bf5402f011daf2831764868b9f7c74b5312291ea96665
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/build-plan-initial.py.txt
    sha256: 768d1ca4589e814f8d74876e6d01c62d7838dcad616c8a2592cd11e8284ef8f3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/build-plan-successor.log.json
    sha256: 37537757a1090e2b02ec48dfa63d0abcb202830e8ecbb3dc85c90147ec66c4b1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/build-plan.py.txt
    sha256: baedbed5406118d78ac9cdce997d5f5b0e0b0b704ca5e798b72a12018476bd56
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/copy-plan.json
    sha256: b7c6082c2450e9232b478424de9a640a12b2c5004d807ae573414a9a0778d566
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/execution.json
    sha256: 88b873ece0a6ea8ad8692971e30ac4acd78afd4496ada310da0dcc70d9caf3c5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/handoff.json
    sha256: 6e1af6dc984ec19185457a5295aeebafe7ae02c9cc37b905d164a2f77ac805bd
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/preparation-disposition.json
    sha256: 70cd408fa2686027ab66235f2f8b4c3aa2665dd8e6b562de68bbfa6e52532ee5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/seal.py.txt
    sha256: de9419d56f66e4b6f5cbf6c616f95f85420ec9b38b9a60b16f713916f695331e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/packaging/validation.json
    sha256: 24c99d1ebcbc02281b9c68d4ca4214f2aa7a17729822f293fc660b2094caad80
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/preflight-adjudication/acquisition.json
    sha256: 686ffd799fdbb5ffff7acee726db84bc9bc626adbc1f7d940ebc065766baf289
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/preflight-adjudication/audit-sources.py.txt
    sha256: ec2d7cba4e3a12b0f8a92dffdaf97c8ed3402611d94024c3e886c79da260f012
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/preflight-adjudication/decision.md
    sha256: 6605d2cbd8d6ec0a2a2f5bc3215ebf6345c863052528c45a00505de82089da3d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/preflight-adjudication/fetch-extra.py.txt
    sha256: 26511aea91da52737ccc0da126720d403b613fa7140dbaf3ef56eda8835023f9
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/preflight-adjudication/fetch-followup-network.py.txt
    sha256: cbc7f1f5029f7933c6441b4582732c83ffc9e8b06017c51428fa37d4fbfbdb33
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/preflight-adjudication/fetch-followup.py.txt
    sha256: f5014176262e3096387eac85b6faf8b9abc5a045b2e3c5f632ee7c4445c6aea9
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/preflight-adjudication/original-source-check.log.txt.json
    sha256: bf23c2087e5bd84de7d3627502709edb2014113f780109c62a428307b974a16e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/preflight-adjudication/seal.py.txt
    sha256: c3a7fb7c55c912df1488379001fc36b7b0447de228e2cfeeb98bc0edaec00552
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-ed-authority-metadata-check-20261011.json
    sha256: 319fa6d68935757dbddf5f8e080a593b6ea78e8251a38c705eb803cd86e54bdb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-ed-root-whole-review-adoption-20261011.json
    sha256: e1672a5e428901ec2d6a222940e8c3c838b832b01886946b32d7c16b8cd66755
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-entner-doudoroff-root-followup-selection-20261011.json
    sha256: 01e9aa1c684d667836d0e7f865f497136d6de655146fdbcb1986e418f2b2e4c3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-next-218-adopt-record-authorities.py.txt
    sha256: 83a7b179c1d9b1f23b71cc35387647ac66ff466c71ad99b9c749b61258f50bb1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-next-218-authority-root-review.json
    sha256: 7ae58b591bd3b71a9238ffa5f967beb361e0209ab9b49beb72764ba79baad576
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-next-218-authority-root-review.py.txt
    sha256: 158e234e32c5b80aec4cd60fc4876770f72080f9c5c81c9e1d40ad4206a63949
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-next-218-core-adoption.json
    sha256: 07bf9a2a0140bda8f610d788da6f12def052c11c669409e39c7ec3942eab1d43
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-next-218-current-duplicate-check.py.txt
    sha256: 4a51da14de7a41ffbb33587e3baad94b93172c33ba477b5d44c1f4dccf4f46d4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-adoption-successors/adopt-dossier-initial.py.txt
    sha256: 69df353030293a8d073d871a4e88c6a27398d29563ad7b3a96c0827b1f7f3837
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-adoption-successors/baseline-bridge-initial.py.txt
    sha256: eed1934c21ae16dcf120e5bb9183dcb6f5752e67bfc4d5abb02c8bd8edd4bfe8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-adoption-successors/baseline-bridge-successor.py.txt
    sha256: 641b3baedff5c35b47d0ca68194b4c591ec443942208b28cafec88da3cce7169
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-adoption-successors/bridge-independent-diagnostic.json
    sha256: c133e7a2bc61dae5dafea44b049599a6eb349594335848991aab0b3701d1b326
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-adoption-successors/dossier-adoption-preparation-disposition.json
    sha256: fbd90008abba0f4efa80b48fed83b86828af7733ba860c701625ba0b076c71a8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-adoption-successors/historical-mapping-check.json
    sha256: 8bf46d42530528cfa823c1cb527ee7c6a0208f07a97487a3cf8790c943c2f5b7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-adoption-successors/merged-baseline-bridge.json
    sha256: dac3f42cf709ae3fc9d4bc586a0fd8bdb0d6caa46266fb48ca80fa9e391bb2bb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-adoption-successors/myx-merge-finalized.json
    sha256: 2896cef9af3290a46b9b9e60d9c1f2ac99c46dd09d651511e4918e4e2362d018
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/00.jsonl.json
    sha256: 8ec039f6e7a403c8440acd601ea877e1bc09483d358317c1a85c8562e9a7d5d8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/01.jsonl.json
    sha256: 7cd3ab14c26eacf65de147e388392797ce22f05072f05a64dc8058a6155be6b5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/02.jsonl.json
    sha256: 9f8cdf97483f7630a2f3e0bae53203d17dfa41adec23a5741f03068a31136fbb
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/03.jsonl.json
    sha256: c50887648c81abdc550770a6b947fab5c297e1467122c723cac600c16ff174fe
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/04.jsonl.json
    sha256: 1e5bdd3afaf598abff25fcef1070fc7aa1de1e377f967d2f44c64ee251db9d80
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/05.jsonl.json
    sha256: 66bbb5257500494e4108488572f38bfb39bb301e1fa5928bcea7594d3104c8e7
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/06.jsonl.json
    sha256: 7a9e95dc6b2da1b83ea06fb250c78ef20190d5bd6d14d289f1a934882a983adc
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/receipt.json
    sha256: 0cd393d9a8007e68294008cfb8e6e35922c138089e78f7fdd114eb6b9fae1e18
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/root-disposition.json
    sha256: d28d85179484610caeca0087496bdf9647fda13400a4df0609b0adb720565de3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/root-normalization/structure-equation-check.json
    sha256: 7beabf584dea006e24a7674d0b5eb37c3b03ee8b04cb83f66cfac7d8915c0b06
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/acquisition-1.json
    sha256: c2d732c4c5793c4582182878b4dab3cc53e79973b7847e34fc83e3435e69a261
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/acquisition-2.json
    sha256: ea830d2b7ed40634f7552b1abbc5603943ce8c6607928cb9169128a0ee303279
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/acquisition-3.json
    sha256: 381503047116b9c6d9bfc77613264921e998faf8f81a58f2b6d265290e26b397
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/acquisition-4.json
    sha256: 140640719dfc1c5b3acc0be1e0d7422fe51ff61d269dda833e5c2130fc696bb0
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/acquisition-5.json
    sha256: f10642db32543f7962b5dd9b033ea5a65602c1fc915912852c10fbc1e59451c5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/acquisition-6.json
    sha256: aa200526e71ea5ba595222e8efba13e7033156ddb716369aa6b2a5381330e42e
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/assessment.md
    sha256: f6232e9b2ccfcb7d81ef17b87e2a5b0ea62b9d2b9b4b7f4af971819cd804791d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/dedup-0.jsonl.json
    sha256: c6bb1945eb27a3bf8e149d5773eb161cbea88f7497fcad1e739670cd09d05bb4
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/dedup-1.jsonl.json
    sha256: fd37f1d353aa5addc9b58dd575a67006fd0b6da02b2e42de98848b8240fa36c5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/dedup-2.jsonl.json
    sha256: e8eb827f13c2a27a0064403aebea100c54377ddd39af73ed80678f6dc886e00f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/dedup.json
    sha256: 0085dc9fab98f1c8bccf98a56412b85859094550de9757f7454a8198fe9cc79a
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/fetch.py.txt
    sha256: 4a88994047d438d1d9404867b3fb96d73348f87bcc4d0e18d59692d62907461f
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/fetch2.py.txt
    sha256: d1148ec86629235d79341e98edf9a2f56cc9ac345015d4f4621e7d4e96788434
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/fetch3.py.txt
    sha256: 07595dee44baeab9ba57a8160aa842ea48efe3d34f7918c3f78e83cf1dac6072
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/fetch4.py.txt
    sha256: 6ab919be012c5c80407283a86fc8e05b87bd56d7964b938e351d67730b935fce
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/fetch5.py.txt
    sha256: cc9dfbc7cb47411738607b0903e55ac10bef0e758cad5fee9a48903a16914a08
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/fetch6.py.txt
    sha256: 060729533a62ff747dfdd97ef198cc0bc00d73c07f27e415f5c57566877d8913
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/go-scope.json
    sha256: 0bc7d8822e094bba830daed845074ff87988bcb9ac98c12350e0a0cdc8a9d7f3
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/preflight-replay.json
    sha256: 717ea4b5b84d798d07435233a55561e77700e14303a0ac99bf1a06ec2f0f59d1
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/primary-scope-ledger.json
    sha256: a0e952d7d8aae732596dfe01fd2474305dd8757618a38a22c25e340b5bfeeae2
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/rhea-equations-v2.json
    sha256: d1c28be7c05e910d66cad0053e281cb1305320a73d275add64e66da66cc9d2c8
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/rhea-equations.json
    sha256: b537b78de01933e175a77b5acc51079f20e8669f3a1d23838fc9ec008e0f2274
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/rhea-preflight-v2.py.txt
    sha256: 21646924190a24fa0f6d240487fa23d973fd1030db319dcbba2b1a7a9c799bc9
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/rhea-preflight.py.txt
    sha256: 3009617b09455f03c58127c32216c12f89008c7c66bf59db015a1e2e29e0e6e5
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/seal-preflight.py.txt
    sha256: 379f632b936f62846872fb26f34e2b9cb635938dd969f27409c9f9d6532bc73d
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/source-manifest.json
    sha256: 7cdb94c72bee9ca744a9241eafa2290f153e2739d3cee950eb0037cee30f1c83
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/source-projection.json
    sha256: 1d6ad3d0b489a211f40614cb8210820be485c4a32f1e42cdd730e7b9f9ebd4b6
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/external-evidence/source-preflight/whole-route-dedup.json
    sha256: cda896593520e756a6db97d180b8c6b9d9b9a68d122a16e3c7a3a5a1387b24fe
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/imod/context.json
    sha256: 36a3d57d8a296e11a050450daa7c0464659d61083256c422e15f91979c5e4491
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/imod/manifest.json
    sha256: 65629fb23ddccf3d406dcc5a42a2f1c2f105748ff307c43b71b1b473cbe3eb27
    role: context
  - path: research/pathway_additions/2026-10-11-next-218/imod/runner-availability.json
    sha256: 86ad0ec152883c99688a5a8a9a90709eb5fa6cfaaffba38eff20ef4388bdce66
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: b2725526a658aa3d54e2ac3398fd499b71f0081ae2b3ed18c84f5872ee6f1af4
    role: context
  - path: src/pathwaymech/schema.py
    sha256: e81f95da70943090d470b1837d248fec2a592c5f4b53fc6587bc4214adbf35f3
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 5e4a0bcb5b4901b603e9e0e89ce8b2172efbd8fcbe5e68cac7283555c6a1c056
    role: context
scope:
  description: Whole-record scientific review of the complete maintained Entner-Doudoroff
    module after final integration freeze, including exact authority/source/helper
    and graph context.
  selection: Single explicitly assigned maintained entner-doudoroff-pathway.yaml,
    SHA548eba1d34a081dd293db6d8bf0e00a0e620973e8f843dafa75bcded6a74e4af.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - KEGG:M00008
  exclusions:
  - target: Scientific validity of the other218 maintained records
    reason: Full-corpus deterministic gates and prior-artifact preservation are not
      whole-corpus scientific re-review.
  - target: New current web inspection or local full-byte replay of2012 article
    reason: Earlier independent official web-only reading is attributed; original
      full local article bytes remain unavailable.
  - target: Browser visual/interactivity acceptance and deployed publication
    reason: Current graph evidence is static/programmatic and this review does not
      attest publication.
targets:
- target_id: KEGG:M00008
  path: data/pathways/entner-doudoroff-pathway.yaml
  label: Entner-Doudoroff pathway
  record_class: PathwayRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/entner-doudoroff-pathway.yaml
    role: maintained pathway identity, scientific scope and mechanistic evidence
  ownership_note: Generated pages and KGX are contextual artifacts owned by maintained
    YAML and renderer. This review authorizes no target, helper, source, authority,
    history or page edits.
checks:
- check_id: gate-render
  name: render
  status: passed
  required: true
  summary: Rendered219 maintained records.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
  - gates-root
  command: just render-pages
  scope_note: Root-executed actual command, not reviewer rerun. Current post-formatting
    run; original log freshly verified.
- check_id: gate-validate
  name: validate
  status: passed
  required: true
  summary: Full219-record validation including identifiers, schema, history and page
    currency passed.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
  - gates-root
  command: just validate
  scope_note: Root-executed actual command, not reviewer rerun. Current post-formatting
    run; original log freshly verified.
- check_id: gate-lint
  name: lint
  status: passed
  required: true
  summary: Current full Ruff check passed.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
  - gates-root
  command: just lint
  scope_note: Root-executed actual command, not reviewer rerun. Current post-formatting
    run; original log freshly verified.
- check_id: gate-diff-tracked
  name: diff-tracked
  status: passed
  required: true
  summary: Tracked whitespace passed.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
  - gates-root
  command: git diff --check
  scope_note: Root-executed actual command, not reviewer rerun. Current post-formatting
    run; original log freshly verified.
- check_id: gate-test
  name: test
  status: passed
  required: true
  summary: 1256passed,3skipped,3warnings; original test child exited0.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
  - gates-root
  command: just test
  scope_note: Root-executed actual command, not reviewer rerun. Reused with423-bound-input
    preservation and exact AST-identical helper change; original log freshly verified.
- check_id: gate-identifiers
  name: identifiers
  status: passed
  required: true
  summary: 219 records passed identifier/label policy.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
  - gates-root
  command: just check-identifiers
  scope_note: Root-executed actual command, not reviewer rerun. Reused with423-bound-input
    preservation and exact AST-identical helper change; original log freshly verified.
- check_id: gate-kgx
  name: kgx
  status: passed
  required: true
  summary: Separate full219-record KGX export passed.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
  - gates-root
  command: just kgx-export --output-dir /private/tmp/pathwaymech-next-218-final-kgx
  scope_note: Root-executed actual command, not reviewer rerun. Reused with423-bound-input
    preservation and exact AST-identical helper change; original log freshly verified.
- check_id: historical-lint
  name: Initial helper lint failure, superseded
  status: failed
  required: false
  summary: Initial driver12654 exited1 solely on Ruff I001; original helper preserved
    and one-blank-line successor passed current lint.
  target_ids:
  - KEGG:M00008
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - formatting
  - gates-root
  command: just lint
  scope_note: Historical pre-fix result retained transparently; current required lint
    is the separate passed check above.
- check_id: fresh-sources
  name: Independent original-source selection audit
  status: passed
  required: true
  summary: 94 response bodies,92 evidence selections,8 primary selections,18 SQL chemical/taxon/compartment
    rows and51reference metadata entries checked.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - source-audit
  command: PYTHONPATH=src /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python
    /private/tmp/pathwaymech-next-218-independent-scientific-review/fresh-original-evidence-audit.py
  scope_note: Actual reviewer5902a4/0; exact bodies rehashed again after final inspect.
    Scientific entailment separately assessed.
- check_id: current-authorities
  name: Independent authority preservation and original identity checks
  status: passed
  required: true
  summary: All prior production entries/metadata preserved against actual721755;4new
    native objects,4reused proteins and21 original SQL terms verified.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - authority-current
  - authority-root
  command: PYTHONPATH=src /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python
    /private/tmp/pathwaymech-next-218-independent-scientific-review/current-authority-audit.py
  scope_note: Actual reviewerea4258/0, selected SQL checks only; root whole-DB hashes
    explicitly attributed.
- check_id: current-integration
  name: Completed source/runtime/authority integration
  status: passed
  required: true
  summary: All4 child commands and2291 endpoint input checks passed.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - integration
  - source-replay-current
  - integration-root
  - boundary-controls
  - formatting-controls
  scope_note: Actual root-owned38656/0; reviewer read complete current wrapper and
    control scopes and freshly verified receipt and child-log digests.
- check_id: graph-current
  name: Current structural page/KGX preservation
  status: passed
  required: true
  summary: 37edges/92evidence,26KGX/25SVG nodes and prior corpus preservation passed.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - graph
  scope_note: Attributed19946/0/e8d27e static/programmatic audit. The graph auditor
    contributed prior preparations. No browser visual claim.
- check_id: canonical-inspect
  name: Final canonical inspect
  status: passed
  required: true
  summary: Actual inspect captured489 input files at working-tree base721755 after
    explicit final freeze.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - record
  - archive
  - preassessment
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python scripts/record_review.py
    inspect --targets /private/tmp/pathwaymech-next-218-canonical-scientific-review/targets.json
    [488 explicit --input arguments]
  scope_note: Actual9594/0/af5f50; exact full argv and start/finish retained externally.
    All471 root-frozen files plus18 context contracts/runtime files are bound; archived
    fixture bytes are provenance inputs only.
- check_id: final-byte-check
  name: Final small-input, source-body, log and AST checks
  status: passed
  required: true
  summary: All489 inspected files,94 original bodies,171 adopted proofs,7 gate logs,4
    child logs and exact helper AST relation passed.
  target_ids:
  - KEGG:M00008
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - archive
  - source-audit
  - formatting
  - integration
  - gates
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python /private/tmp/pathwaymech-next-218-canonical-scientific-review/final-input-check.py
  scope_note: Actual reviewer30c836/0; receiptSHAf497a0fbc21d49336f45c95ab1b8b23df37fb93f1bf404a34fdcaa291654c6e5.
    No redundant whole database stream.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/pathways/entner-doudoroff-pathway.yaml
  locator: entire maintained record, all37edges/92evidence/51references
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Complete KEGG module with5 native reaction objects in4 positions,19participants
    and1taxon. Current target is byte-identical to the independently reviewed external
    candidate.
  snapshot_sha256: 548eba1d34a081dd293db6d8bf0e00a0e620973e8f843dafa75bcded6a74e4af
- evidence_id: source-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/original-evidence-audit.json
  locator: source_checks; primary_original_selections; evidence_selections; issuing_sql_labels;
    reference_metadata
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Current reviewer freshly checked94 retained response bodies,16 prior proofs,
    all92 evidence occurrences,8 original primary selections,18 selected SQL chemical/taxon/compartment
    rows and51 reference metadata entries. Exact selectors and original values are
    recorded. Selector success is distinct from scientific entailment.
  snapshot_sha256: 88d84ac8e8a3b07a1cade10a797576f0d518ad49c3d4d7bd1a757b132cc4e5c9
- evidence_id: native-sources
  kind: database
  reference: research/pathway_additions/2026-10-11-next-218/draft/ed-source-manifest.json
  locator: original module M00008; reactions R02736/R10907/R02035/R02036/R05605; native
    compound bodies; Rhea142 original RDF; UniProt and MetaCyc objects
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Original source bodies support exact native membership and identifiers.
    Five native reaction objects are preserved; NAD/NADP alternatives are parallel.
    Native module includes R10907 despite inverse reaction MODULE omission. Issuing
    scientific Rhea142 RDF is distinct from production Rhea139 SQL authority.
  snapshot_sha256: a61f692824161ac9fd59cd01dc14ffdc608d75ba1ec6fc5b126486e5068b1506
- evidence_id: chemical-proof
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/independent-chemistry.json
  locator: five balances; ten original Rhea sides; twelve native structure bridges;
    two donor-dependent net equations
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: This same independent reviewer previously derived complete chemical sides
    and atom/charge balances from original sources. Exact target and selected source
    bytes remain unchanged; current source/SQL readings and completed integration
    replay corroborate the proof. Initial reviewer RDF parser error and corrected
    successor are preserved, not a product defect.
  snapshot_sha256: 90d417893922c02da209e0c33a2abfc5d58481c3f33be68a2aeff5860df8a20a
- evidence_id: prior-positive
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/positive-replay.json
  locator: actual26000/0 complete original-source replay, record_sha256 and limits
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Earlier independent external full replay streamed three SQL databases plus
    Rhea142 RDF and checked94 retained responses, exact source/proposal claims, sequences,
    structured iModulon adapter and strict/KGX output. This is historical evidence,
    not current production-authority approval.
  snapshot_sha256: 8512f36aa2c6f45d46d7639ae6deacec7c634e6767611e1a5721c6e602f7db3a
- evidence_id: prior-review
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/whole-record-review.json
  locator: all13 domains and37edge assessments; independence; actual executions and
    source-access limits
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Earlier external whole-record scientific review by this same reviewer.
    No target/helper/authority implementation contribution. It is external evidence,
    not an invented canonical predecessor or a second independent reviewer.
  snapshot_sha256: 461212427906d7d609c8d3373c355809640ac86a3cd720b2ad1ebba821322ee4
- evidence_id: zwf-2012-web
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/independent-review/web-primary-observations.json
  locator: earlier official publisher PDF inspection; Table1, Discussion p2303, Purification
    pp2305-2306
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: The2012 full article was personally inspected on the web during the earlier
    independent review. It supports strong NADP preference, NAD capacity and the thrombin-cleaved
    construct retaining12 extra N-terminal residues. This final phase did not repeat
    that web inspection and has no local full-article digest; local403body is not
    article evidence.
  snapshot_sha256: 39768d5a2325f6f7d7dc002e35845f27fed03a0ec94407d108bbf9519736ef62
- evidence_id: zwf-2016
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4807051/
  locator: //sec[@id="sec005"]/p; //table-wrap[@id="pone.0152403.t001"]; original
    S1Table workbook row9
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Original JATS Methods and Table1 were freshly read. Wild-type comparator
    shows NADP preference and measurable NAD activity; recombinant TEV processing
    leaves an expected Gly-His extension. S1Table links P0AC53 for sequence analysis,
    not exact experimental construct identity. Assay G6P does not prove exclusive
    beta-anomer usage.
  snapshot_sha256: 9435e6924beaed5f2a67c890b563663d9ebac6388265f23a66a298ccd3f05658
- evidence_id: pgl-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC532434/
  locator: //section[@id="sec4"]/p[1]; //section[@id="sec15"]/p[1]; Figure4
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Original construction and Results passages support pgl/ybhE loss-of-function
    and complementation in MG1655-background strains after DY378 recombineering. The
    extract assay is not entirely quantitative because initial lactone concentration
    is unknown.
  snapshot_sha256: 5ab279ed68ec09f37a713dc74f4f29f2606ca55da8c424542a70f5d1922aaeab
- evidence_id: edd-eda-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2211689/
  locator: //section[@id="sec10"]/p[1..3]; //section[@id="sec11"]/p[1]
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: 'Original Methods distinguish K-12 edd donor and BL21(DE3) expression host.
    Fractionated lysate activity supports dehydration; added Mn/Fe are preparation
    conditions. Eda cleavage uses LDH-coupled pyruvate detection: NADH is reporter
    reagent, not Eda substrate.'
  snapshot_sha256: 7deed7c767741d64c1e2826d569b3ad570a6f0f950758838678fca9268966c7f
- evidence_id: edd-cluster-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5136138/
  locator: //*[@id="P9"]; //*[@id="P30"]; Figures4 and5 scope
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Original Edd lysate activity is peroxide-sensitive and recoverable with
    iron/DTT. The stated3Fe4S EPR spectrum is fumarase A. It is not an Edd cluster
    spectrum or direct occupancy measurement.
  snapshot_sha256: e57d324fa18469cc926407fa14c681488d9acf38f0c2ba86539162da1735c075
- evidence_id: eda-trimer-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC31111/
  locator: //section[@id="sec2"]/p[1]; //section[@id="sec5"]/p[1]
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Original recombinant E.coli Eda structure has trimeric assembly. The pKK-223
    preparation and expression/SeMet host details do not independently prove a specific
    MG1655 donor or exact current unmodified sequence.
  snapshot_sha256: 41f5604bedb4857764f066bee775ef55f99e434a601b9d40596d9344139fa719
- evidence_id: csra-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC545716/
  locator: //section[@id="sec21"]/h3 and p[1]; //section[@id="sec22"]/p[1]; Figure7
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Fresh original Results and Discussion reading shows decreased Eda/transcription
    in csrA mutant and generally positive indirect control, despite the negative section
    heading and conflicting current annotation. Earlier review also inspected original
    Figure7. No direct CsrA inhibition or activation edge is asserted.
  snapshot_sha256: b82771e913c915aa5ee899d9f3cf209a1a943dd827b5a49e53c47fcac05f015f
- evidence_id: protein-native
  kind: database
  reference: research/pathway_additions/2026-10-11-next-218/draft/ed-protein-projection.json
  locator: four original complete UniProt sequences/comments/ECO; MetaCyc Eda complex
    component and catalyzed-reaction XML
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Fresh original-pointer audit checks current K-12 taxon83333 and491/331/603/213-residue
    proteins, Eda native complex component coefficient3, homotrimer and inferred cytoplasm,
    Edd similarity/HAMAP cluster count. Projection is a locator index; original values
    in source-audit carry the evidentiary check.
  snapshot_sha256: 311e94feceb6fdecff17d64d4ce7856db6ad46ad7349165cdf164b1f64a33f03
- evidence_id: authority-current
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/current-authority-audit.json
  locator: prior_entries_and_metadata_preserved; new_native_objects; existing_protein_authority_reuse;
    selected_ontology_rows
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Reviewer independently compared every prior authority/manifest entry against
    actual721755 merge, parsed4 new native objects and compared4 reused old UniProt
    batch records to current scientific entries, querying21 original SQL terms. Four
    source bodies,6 source terms and3 ontology terms added; CHEBI17719 is reference-only.
    No whole-DB rehash claimed in this audit.
  snapshot_sha256: c84bc0e5efaf1bc018630e5a41135e6e85da2214299b1c256859413ba2c61bfa
- evidence_id: authority-root
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/root-acceptance/pathwaymech-next-218-authority-root-review.json
  locator: database_checks; version_checks; preservation
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Root independently streamed all4 production SQL bodies and derived selected
    labels/versions before adoption. Original batch2026_03 provenance is retained
    separately from fresh UniProt entryAudit. Actual merged-base equivalence and current
    preservation were separately verified by this reviewer.
  snapshot_sha256: 7ae58b591bd3b71a9238ffa5f967beb361e0209ab9b49beb72764ba79baad576
- evidence_id: imod
  kind: search
  reference: research/pathway_additions/2026-10-11-next-218/imod/context.json
  locator: 21 original response bodies;15queries; e_coli/precise_mg1655/component25
    and edd/b1851,eda/b1850
  accessed_at: '2026-10-11T18:20:37Z'
  support: context_only
  summary: Original structured adapter replay supports bounded computational expression
    context for edd/eda. Membership is not direct catalysis, pathway identity, regulation
    or in-vivo donor flux.
  snapshot_sha256: 36a3d57d8a296e11a050450daa7c0464659d61083256c422e15f91979c5e4491
  search_scope: Original iModulonDB datasets/search/component responses through the
    inspected unchanged canonical adapter:15queries,4 direct genes and selected component25.
    Not an organism-wide absence claim.
- evidence_id: dedup
  kind: search
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/root-current-dedup/root-disposition.json
  locator: all current baseline search dispositions and explicit exclusions
  accessed_at: '2026-10-11T18:20:37Z'
  support: context_only
  summary: Ignored/hidden/symlink-inclusive baseline search distinguishes exact M00008
    from maintained sulfoED and historical BRENDA map/export canaries. Those canaries
    remain source context, not a completed equivalent maintained record or BRENDA
    ingestion.
  snapshot_sha256: d28d85179484610caeca0087496bdf9647fda13400a4df0609b0adb720565de3
  search_scope: Root actual baseline search used rg-uu/hidden/follow, excluding only
    Git/dependency trees. Earlier broader reviewer search is preserved. Final reviewer
    exact target-ID/path lookup in reviews/reports/localskill/docs also included ignored/hidden
    content, with no exact predecessor hit; no alias-exhaustion claim.
- evidence_id: formatting
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/helper-formatting-successor/adoption.json
  locator: exact original/archive/successor bytes, AST equality, issue406 and initial
    gate receipts
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Initial required lint failed I001. A single blank line was added, preserving
    original f67 bytes and historical aliases; current3a9 helper has identical executable
    AST. Reviewer independently rechecked exact one-line relation and AST after canonical
    inspection. Current lint succeeds; issue406 is external lineage, not a canonical
    finding predecessor.
  snapshot_sha256: 3fa6bb139a923d571b7c3a59df2583b3d159d91e0b3f9a35ee29a12657e3120e
- evidence_id: integration
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/integration-replay.json
  locator: commands;2291 bound inputs; formatting evidence; child receipt and limits
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Actual root-observed38656/0 terminaldff4d1 current integrated replay passed
    source replay, corpus identifiers, native schema and target strict schema. All2291
    bindings rechecked at startup/completion. The complete wrapper was read; cached
    source/proposal replay and production authority selection remain distinct scopes.
  snapshot_sha256: e5c2730eab40f7bcfd9009ec2990c3efb730d59c6d03209a2ac76692f29ea83b
- evidence_id: source-replay-current
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/positive/source-replay.json
  locator: native_members;rhea_sides;kegg_structure_bridges;balances;branch_nets;sequence_checks;negative_controls;all_evidence_anchors
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Current formatted helper checked94 bodies,5 native reaction objects,10
    Rhea sides,12 native structure bridges,5 balanced equations,2 separate nets,4
    sequences,8 primary selections and92 evidence anchors. Seven targeted invalid
    record variants were rejected. This is deterministic corroboration, not independent
    scientific interpretation.
  snapshot_sha256: 673e996aafb83addec0ce2a1418a82ff7e06f54b413ef1125a27310bdb488191
- evidence_id: integration-root
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/integrated-replay-root-adoption.json
  locator: actual terminal observation, receipt digests,2171 formal rechecks and limits
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Root inspected actual child exits/log digests and scientifically scoped
    summaries, freshly checked2171 non-source bindings and adopted current integration.
    Driver/child streamed whole source bodies; no extra root or current-reviewer database
    pass is implied.
  snapshot_sha256: 126e217c172b050dacda5338c6c66ca6a31bbd139aab4b220e49a034355c647c
- evidence_id: boundary-controls
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-original/controls-attempt-2/results.json
  locator: 42 narrow actual guard/environment controls including late changes, path
    retarget, inventories, stale cache and nested safe path
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Original wrapper successor rejects changed formal/source/proof/manifest
    bytes and identities, late mutation, inventory changes and collisions. Small real-function/CLI/environment
    fixtures are explicitly not42 full scientific-source replay mutations. Nested
    RDKit safe-path correction and earlier attempts remain preserved.
  snapshot_sha256: f1c6811503a2d00f0cc31e26185cb1216826f8aff1f953856554fa6c8e7f61ca
- evidence_id: formatting-controls
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/preparation-formatting-successor/controls-attempt-1/results.json
  locator: 13 current formatting-lineage cases and exact AST guard/orchestration reuse
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Formatting successor proves reuse of42 prior guard controls via unchanged
    functions and executes13 narrow lineage/byte/path checks, including forbidden
    extra edits and archive retarget. No claim of repeated full-source mutation runs.
  snapshot_sha256: b1290a0ba77a8c14541960976450b10bda34c25da39aeb976bc9d364c1c8a1cd
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/post-formatting-gates/receipt.json
  locator: current_checks;reused_unchanged_checks;423input reuse basis
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Current render, full validate, lint and tracked whitespace all exited0.
    Full test1256passed/3skipped/3warnings, identifier and KGX passes are reused because
    all423 inputs are unchanged except exact AST-identical helper separator. Reviewer
    freshly rehashed all7 actual logs and read terminal summaries.
  snapshot_sha256: baf05edb0fbaaba290e8119d36ea54d81cad041f2c8187088588ad80c77e1627
- evidence_id: gates-root
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/root/pathwaymech-next-218-current-gates-root-adoption.json
  locator: actual39297/0 terminal1e14c9;423 inputs; initial test child0 from12654
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Root actual terminal current gate adoption preserves initial driver exit1
    due solely to lint and successful test child0. Four current reruns and three justified
    unchanged checks satisfy required gates without concealing prior failure.
  snapshot_sha256: 965055f84b01272e00629521610521c91a9bd8551e093f49efae014b29801753
- evidence_id: graph
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/graph-audit/completion.json
  locator: actual19946/0/e8d27e;37edges92evidence26KGX25SVG; prior corpus preservation
    and contributor disclosure
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Structural audit preserves218 prior record pages,10416 old edges and6883
    record-context nodes. Three aggregate display labels follow unchanged first-record
    label policy; prior source-context labels remain. Auditor contributed ED preflight/authority
    preparations; this is attributed structural evidence, not its independent scientific
    approval or browser interaction test.
  snapshot_sha256: f54cd9fcdb5eb86be7c8f76bb66dfdc1e6b02241121f2dec290cdfb9e21e42a9
- evidence_id: archive
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-proof-root-adoption.json
  locator: 171 adopted proof copies,255 original source bytes,11link and138directory
    observations
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: Root byte-verified final evidence adoption. Reviewer freshly rehashed all171
    adopted copies,94 original response bodies and489 canonical inputs after inspect;
    fixtures remain recoverable inert provenance, not additional scientific sources.
  snapshot_sha256: cc2ed821ae6a64347a7486858cf888bf1c7ea3ad38c38b5fba96321bb7e2066e
- evidence_id: preassessment
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-218/external-evidence/final-integration-proofs/scientific-preassessment/preassessment.json
  locator: all13 domains and37 current edge assessments; exact provisional scope
  accessed_at: '2026-10-11T18:20:37Z'
  support: supports
  summary: This reviewer prepared the complete scientific assessment before final
    freeze and retained all earlier proofs unchanged. Final assessment follows actual
    canonical inspection at18:16:47Z and checks completed current replay/gate evidence.
    Preparatory pending statements remain historical, not current unresolved checks.
  snapshot_sha256: a7112e22ed2340ac00bca610407507c18bf8c7ec1b9a142a2384a003ab2fd468
assessments:
- assessment_id: assessment-01
  area: identity
  topic: Complete native module boundary and alternative membership
  outcome: supported
  summary: 'The record represents the entire four-position KEGG:M00008 module: R02736
    andR10907 are alternatives at the first position, followed by hydrolysis/dehydration/aldol
    cleavage. Native M00008 membership governs the retained R10907 inverse-MODULE
    conflict. Glucose uptake/phosphorylation, lower glycolysis and ATP formation are
    outside this boundary; no adjacent MetaCyc shunt or sulfoED substitution is made.'
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - record
  - native-sources
  - source-audit
  - dedup
- assessment_id: assessment-02
  area: grounding
  topic: Exact beta-anomer chemistry and protonation normalization
  outcome: supported
  summary: KEGG C01172 is native beta-glucose6P. Original ATOM/BOND and selected ChEBI58247
    preserve connectivity/stereochemistry under explicit acid-base normalization;
    neutral CHEBI17719 is reference-only. Alpha58225 and generic61548 are distinct
    contextual references. No neutral/charged exactMatch or experimental exclusive
    beta specificity is inferred.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - native-sources
  - chemical-proof
  - source-audit
  - source-replay-current
- assessment_id: assessment-03
  area: quantity
  topic: Reaction sides, direction, coefficient and separate net accounting
  outcome: supported
  summary: All20 chemical edges agree with the complete original sides. Rhea12557/17278/17090
    direction is grounded in native masters and KEGG bidirectional cross-references,
    while reversible KEGG oxidation definitions retain their native directions. Five
    equations balance atoms and charge. Each separate donor branch yields GAP,pyruvate,reduced
    donor and2hydrons; water cancels and no ATP is asserted. Parallel alternatives
    are not summed.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - chemical-proof
  - native-sources
  - source-replay-current
- assessment_id: assessment-04
  area: scope
  topic: Taxon, current protein and historical construct distinctions
  outcome: supported
  summary: Current UniProt entries issue K-12 taxon83333 and lengths491/331/603/213.
    This establishes current identifiers, not exact equality to every historical/tagged
    experimental construct. K-12/MG1655 donors remain distinct from BL21 or SeMet
    expression hosts; current Edd603-residue PLR sequence difference from historical602-residue
    AC is explicit.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - protein-native
  - source-audit
  - zwf-2016
  - edd-eda-primary
  - eda-trimer-primary
  dimensions:
  - name: taxon_scope
    value: NCBITaxon:83333 Escherichia coli K-12
    definition: Current record/UniProt scope; primary assay strain and donor/host
      qualifications remain narrower and explicit.
    evidence_ids:
    - record
    - protein-native
    - source-audit
  - name: construct_scope
    value: Historical/tagged or processed recombinant preparations, not asserted current
      native chain identity
    definition: Zwf2012/2016 extensions, Edd historical sequence and Eda donor limitations
      constrain transfer.
    evidence_ids:
    - zwf-2012-web
    - zwf-2016
    - edd-eda-primary
    - eda-trimer-primary
- assessment_id: assessment-05
  area: evidence
  topic: Zwf donor use, preference and beta annotation
  outcome: supported
  summary: Both first-position enables edges combine native KEGG beta attribution
    with experimental donor capacity and strong NADP preference. Generic G6P assays
    and current HAMAP annotation do not prove exclusive beta use or equal in-vivo
    donor flux. The2012 support is attributed to this reviewer's earlier web-only
    reading; current2016 original Methods/Table1 and workbook scope were freshly reassessed.
    S1Table P0AC53 is sequence-analysis mapping, not construct identity.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - zwf-2012-web
  - zwf-2016
  - protein-native
  - source-audit
  - record
- assessment_id: assessment-06
  area: evidence
  topic: Pgl genetics and extract hydrolysis
  outcome: supported
  summary: Native Pgl assignment is supported by deletion/complementation and extract
    activity with explicit MG1655 background and DY378 construction scope. Unknown
    starting lactone concentration limits quantitation. The record does not invent
    purified assembly or obligatory metal evidence.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - pgl-primary
  - protein-native
  - source-audit
- assessment_id: assessment-07
  area: evidence
  topic: Edd catalysis and cofactor evidence tiers
  outcome: supported
  summary: K-12 amplified ORF expressed in BL21(DE3), coupled fractionated-lysate
    activity and native catalytic annotation support dehydration within historical-sequence
    limits. Edd peroxide sensitivity and iron/DTT recovery do not establish direct
    Edd EPR or measured cluster stoichiometry. One4Fe4S count is similarity/HAMAP
    inference; Mn supplementation is not an obligatory cofactor.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - edd-eda-primary
  - edd-cluster-primary
  - protein-native
  - source-audit
  dimensions:
  - name: evidence_tier
    value: Cofactor count ECO:0000250/0000255; broader cluster annotation also ECO:0000305
    definition: Similarity/HAMAP and curator inference are distinguished from original
      biochemical activity/repair observations.
    evidence_ids:
    - protein-native
    - edd-cluster-primary
    - source-audit
  - name: component_role
    value: Edd enzyme with qualified iron-sulfur cofactor
    definition: No obligatory bound manganese, direct Edd cluster spectrum or measured
      cluster occupancy asserted.
    evidence_ids:
    - record
    - edd-eda-primary
    - edd-cluster-primary
- assessment_id: assessment-08
  area: evidence
  topic: Eda selected catalysis, native trimer and localization
  outcome: supported
  summary: MetaCyc native complex component coefficient3, exact P0A955 link, experimental
    homotrimer annotation and original recombinant structure support selected Eda
    assembly. Only the module KDPG cleavage activity is represented. LDH reporter
    NADH is not a reactant; experimental donor-strain equality is not inferred. Cytoplasm
    remains ECO:0000305 curator inference.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - protein-native
  - eda-trimer-primary
  - edd-eda-primary
  - source-audit
- assessment_id: assessment-09
  area: consistency
  topic: CsrA source conflict retained without direct regulation
  outcome: supported
  summary: Original2005 Results and Discussion support generally positive indirect
    Eda expression effects; the negative heading/current annotation conflict is explicitly
    retained. Figure7 was inspected during the earlier external review. No unsupported
    direct inhibitory or activating edge is exported.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - csra-primary
  - prior-review
  - record
- assessment_id: assessment-10
  area: evidence
  topic: Claim-specific evidence and reference coverage
  outcome: supported
  summary: All37edges and92 evidence occurrences were scientifically assessed against
    nearest exact source locators and appropriately scoped original bodies, with all51
    reference metadata entries checked. Structured source assertions are interpretations
    of native objects, not invented quotations from cited papers. 2012 is earlier
    web-only full text with no local article digest; current local403 is not substituted
    as article evidence.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - source-audit
  - native-sources
  - prior-review
  - zwf-2012-web
  - preassessment
  metrics:
  - name: Evidence occurrences assessed
    value: 92
    unit: evidence occurrences
    definition: Entire maintained record;59 distinct assertion objects reused across92
      edge occurrences.
    denominator: 92
  - name: Mechanistic edges assessed
    value: 37
    unit: edges
    definition: All local graph edges including membership, chemistry, enzyme/complex/cofactor/location
      and ordering.
    denominator: 37
- assessment_id: assessment-11
  area: scope
  topic: iModulonDB remains computational context
  outcome: supported
  summary: The original structured adapter21response/15query evidence identifies component25
    for edd/b1851 and eda/b1850 in e_coli/precise_mg1655. It supplies expression-module
    context only; no direct mechanism, regulation, donor flux or broader taxon inference
    follows.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - imod
  - source-replay-current
- assessment_id: assessment-12
  area: provenance
  topic: Production authority preservation and final integrated gates
  outcome: supported
  summary: Independent current authority audit preserves every prior entry/metadata
    against actual721755 merge.4source bodies,6source terms and3ontology terms are
    grounded in original issuing objects; reference-only CHEBI17719 and reused UniProt
    batch provenance are explicit. Completed current integration and required corpus
    checks support219-record runtime compatibility without implying scientific re-review
    of the other218 records.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - authority-current
  - authority-root
  - integration
  - integration-root
  - gates
  - gates-root
- assessment_id: assessment-13
  area: provenance
  topic: Helper lineage, meaningful controls and proof boundaries
  outcome: supported
  summary: Original helperf67 is preserved; current3a9 successor differs by one blank
    line with identical executable AST. Issue406 has an evidence-backed formatting
    correction. Current wrapper binds2291 source/runtime/authority/policy/proof inputs
    and rechecks endpoints. Original reviewer guards,42 narrow wrapper controls and13
    formatting-lineage controls remain scoped; seven invalid record variants are rejected.
    No claim is made that narrow fixtures are repeated full-source mutation replays
    or that digest endpoints exclude all transient state changes.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - formatting
  - integration
  - source-replay-current
  - boundary-controls
  - formatting-controls
  - prior-positive
- assessment_id: assessment-14
  area: graph
  topic: Current graph representation and complete prior-context preservation
  outcome: supported
  summary: Current static/programmatic graph audit preserves37edges/92evidence,26KGXnodes
    and25visible SVGnodes, with taxon scope retained outside the visible mechanism
    layout. All218 prior pages,10416 prior edges and6883 source-context node entries
    remain. Three shared display labels change under the unchanged first-record rule;
    old context labels persist. Contributor graph audit is attributed structural evidence,
    separate from this reviewer's scientific judgment. No browser visual or interaction
    test is claimed.
  target_ids:
  - KEGG:M00008
  evidence_ids:
  - graph
  - record
  - gates
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - KEGG:M00008
  rationale: Retain the complete native four-position M00008 module with parallel
    NADP/NAD first reactions. Exclude glucose uptake/phosphorylation, lower glycolysis,
    ATP generation and distinct sulfoED or broad BRENDA map context.
  evidence_ids:
  - record
  - native-sources
  - dedup
  - chemical-proof
limitations:
- Native beta chemistry is distinct from experimentally exclusive anomer use. NAD
  capacity and preference do not establish equal or quantified in-vivo donor flux.
- Current K-12 protein identities are not exact historical/tagged construct identities.
  Edd historical sequence differences, Pgl strain construction and Eda donor/host
  limits remain explicit.
- Edd cluster count uses similarity/HAMAP inference; no direct Edd EPR, measured occupancy
  or obligatory bound manganese is asserted. Eda assay reporter NADH is not pathway
  substrate.
- CsrA negative-heading/current-annotation conflict is retained against positive indirect
  original Results/Discussion; no direct regulatory edge is inferred.
- The2012 full article was inspected only in the earlier independent web-only review.
  No fresh final-phase web read, locally retained article bytes or full-byte replay
  is claimed.
- iModulonDB membership supplies computational transcriptomic context only, not direct
  pathway, catalytic, regulatory or donor-flux proof.
- Original independent whole-source chemistry/replay and current root-executed database
  streams are explicitly attributed. Current reviewer freshly rechecked94 small response
  bodies and selected SQL/source identities without another full20GB replay.
- Wrapper endpoint checks do not exclude arbitrary transient machine-state mutation
  or hash every installed dependency implementation.42 wrapper and13 formatting controls
  are narrow fixtures/CLI checks, not repeated full scientific replays.
- Full test/identifier/KGX results are reused after an exactly one-blank-line AST-identical
  helper successor, with423 original bindings preserved. Current render/full-validation/lint/whitespace
  were rerun. Initial lint failure is preserved and superseded.
- Graph audit is static/programmatic. No browser visual/interactivity or deployed-page
  inspection is claimed.
- Working-tree attestation binds489 local inputs at available base721755. It does
  not assert that the reviewed bytes are already committed, merged or published.
- Historical source inventories and BRENDA canaries remain context. No source exhaustion,
  complete BRENDA ingestion or public-release licensing determination is made.
notes:
- Preparatory scientific reading preceded root final freeze by instruction. Actual
  canonical inspect completed9594/0/af5f50 at18:16:47–18:16:51Z; final independent
  judgment follows that inspection and completed current proof review.
- Final reviewer30c836/0 rechecked489 canonical inputs,94 original bodies,171 adopted
  proofs,7 gate logs,4 integration child logs and exact helper formatting relation.
  External exact argv/receipts retain execution details.
- A final-phase display-only JSON summarizer initially raised TypeError on integer
  bound_inputs; corrected read2537bc/0 succeeded. It did not run a scientific check,
  alter files or affect product state. Earlier RDF parser, wrapper preparation and
  graph-harness attempts remain preserved with scoped successors.
- All frozen dossier bytes are captured for provenance; archived negative fixtures
  and historical failure wrappers are not additional scientific evidence. No canonical
  predecessor or finding lineage is invented from external reports.
- Only the canonical immutable review bundle is a maintained write by this reviewer.
  No target, source, authority, helper, history, page or dossier edit was made.
- Issue406 is external GitHub/preintegration lineage supported by exact formatting
  correction and current lint, not a fabricated previous_occurrences entry. Complete
  staged whitespace and PR lifecycle remain root tasks.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/406
- https://febs.onlinelibrary.wiley.com/doi/10.1111/j.1742-4658.2012.08610.x
tags:
- scientific-review
- whole-record
- entner-doudoroff
- independent
- complete-native-module
```
