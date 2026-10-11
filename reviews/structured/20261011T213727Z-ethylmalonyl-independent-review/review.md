# Independent scientific review of the complete ethylmalonyl-CoA pathway

- Review: 20261011T213727Z-ethylmalonyl-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T21:19:38.475320Z
- Finished UTC: 2026-10-11T21:37:27.356806Z
- Reviewer: Codex /root/ethylmalonyl_successor_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete 14-reaction KEGG M00373 ethylmalonyl pathway is supported within its explicit native, experimental and inferred scopes. Preserved full original independent scientific coverage is combined with this reviewer's independently executed source-direction and two-paper correction reassessment and current maintained-byte inspection. External issues 416 and 417 are addressed, and the separate authority-parser successor addresses issue 418; no unresolved finding remains in this record scope. Actual maintained full gates pass. Formal balance, identifier admission and deterministic graph checks do not establish broader biological claims.

## Scope And Provenance

One complete maintained pathway record, including exact identity, taxon, participant/reaction/edge evidence, retained limitations, authority grounding, complete rendered graph and final maintained gates. Broader full-source coverage is inherited from the preserved original independent review; new work covers the complete maintained YAML, all 14 native directions, exact changed paper anchors, rejection controls, positive replay and current input reconciliation.

Selection: Explicit maintained KEGG:M00373 record adopted byte-identically from the independently accepted corrected draft at baseline 7b5201e93c0608631af73e629780d829efd26426.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7b5201e93c0608631af73e629780d829efd26426.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| KEGG:M00373 | data/pathways/ethylmalonyl-coa-pathway.yaml | maintained | Ethylmalonyl pathway |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Actual root render gate | passed | True | KEGG:M00373 | Recorded actual render command completed with exit zero. |
| Actual root validate gate | passed | True | KEGG:M00373 | Recorded actual validate command completed with exit zero. |
| Actual root test gate | passed | True | KEGG:M00373 | 1,378 passed; three empty command-frontmatter parametrization skips; no skipped scientific or source checks. |
| Actual root lint gate | passed | True | KEGG:M00373 | Recorded actual lint command completed with exit zero. |
| Actual root kgx gate | passed | True | KEGG:M00373 | Recorded actual kgx command completed with exit zero. |
| Actual root whitespace gate | passed | True | KEGG:M00373 | Recorded actual whitespace command completed with exit zero. |
| Complete maintained scientific assessment | passed | True | KEGG:M00373 | All 1,750 maintained YAML lines read; exact full original independent scientific coverage inherited unchanged and separately attributed; own scoped paper/direction corrections independently executed. |
| Independent direction and publication controls | passed | True | KEGG:M00373 | All 14 reversal negatives reject at the correct original-source direction; complete positive and late manifest/output controls satisfy their expected outcomes. |
| Current authority labels and preservation | passed | True | KEGG:M00373 | All 66 named IDs/labels agree; all prior terms, source objects, prior record bytes and original evidence copies are preserved. |
| Rendered graph and whole-corpus preservation | passed | True | KEGG:M00373 | Programmatic graph, anchor, geometry, full KGX and old-page preservation checks pass; no browser review claimed. |
| Initial governed review integrity | passed | True | KEGG:M00373 | All 93 existing canonical bundles passed before creating this new observation. This check does not claim that the new bundle already existed or was validated by the prior run. |
| Governed artifact synchronization | passed | True | KEGG:M00373 | All 22 governed artifacts match the pinned claw revision. |

## Scientific And Domain Assessments

### Exact complete pathway and native alternative boundary

identity: supported. Targets: KEGG:M00373.

The record denotes the complete KEGG M00373 ethylmalonyl pathway, with all 14 reaction rows and both terminal branches. The 11-member MetaCyc PWY-5741 route ends in different ATP-forming ligase chemistry and is not asserted to be an exact alias.

The original independently inspected source definition has 12 mandatory orthology groups and 13 KOs; K01965+K01966 is a joint requirement, and K05606/K08691 each cover two transformations. Mcl2 hydrolysis, all three propionyl conversions and the glyoxylate branch are retained. R09291 lacks a native KEGG Rhea DBLINK; its independently reviewed RXN-8957/chemistry bridge does not fabricate one. The inherited current-base dedup included hidden/ignored files and followed symlinks. DRAM contributes four rows/three coordinates/four RN identifiers including R09979, not a complete alternative definition.

### Native reaction orientation, complete chemical sides and material flow

graph: supported. Targets: KEGG:M00373.

All 14 maintained directions and equations agree with the pinned original RDF. Fifty chemical sides and coefficients, 13 material-transfer edges and both complete branches retain the independently reviewed chemistry.

This reviewer separately streamed all 326,097 native RDF descriptions to verify selected directional objects and unique master-side orientation. The independently executed corrected replay additionally checks all 50 native sides, elements/charge and the formal net. Full original chemistry/source-to-graph coverage is explicitly inherited from the preserved original independent review. The balanced net consumes three acetyl-CoA, CO2, bicarbonate, two NADPH, ATP, water and formal oxidized ETF, producing malate, succinyl-CoA, two CoA, two NADP, ADP, phosphate and formal reduced ETF. Formal balance is not a measured physiological flux or microscopic ETF stoichiometry.

### Exact proteins, assemblies and experimental/inferred tiers

grounding: supported. Targets: KEGG:M00373.

The maintained 12 UniProt proteins and four native complexes preserve exact identity and source-specific evidence tiers. Unresolved PhaB/crotonase assignments remain excluded while their chemical reactions remain complete.

The preserved original reviewer checked 19 exact sequence bridges and all selected issuing entries; this canonical observation does not claim those 19 alignments were newly rerun. D3JV03 is the native 548-aa ADC44452.1/strain 2.4.1 product, distinct from the 555-aa Q3J5V7 counterpart and purification tags. Native component copies 2/2/2/6 remain database assertions; primary Mcl1 evidence supports a hexamer. Ecm/Mcd homodimers retain reviewed database scope where primary full text was unavailable. Mcl2 dimer/trimer remains unresolved, and PCC/MCM assembly inference is not promoted to strain measurement. Automatic thiolase/PccA assignments remain enables edges.

### Cofactors, assay conditions and organism scope

evidence: supported. Targets: KEGG:M00373.

Cofactor and context claims remain appropriately narrow: bound Mcd FAD is distinct from whole ETF reaction states; divalent metals remain alternative assay supports; B12 and automatic biotin annotations retain their source tiers.

Mcl1/Mcl2 metal comparisons and structural buffers do not establish exclusive in-vivo occupancy. No zinc claim is inferred for Ccr. AM1 isotope, acetate and C1/C2 studies remain corroborating organism/condition context, not exact R. sphaeroides protein assignments. CPD-9409 stereochemical disagreement and AM1 figure/assay R/S wording conflict remain visible. PMID:18819910 and PMID:19703103 are abstract-only; detailed catalytic/assembly/cofactor assertions cite the actually inspected reviewed database entries. The broader primary/UniProt audit is inherited with its exact unchanged bindings, not presented as newly repeated.

### Verified disposition of ethylmalonyl-paper-anchors-and-etf-inference (issue 417)

evidence: supported. Targets: KEGG:M00373.

The eight-field correction is supported by precise native paper anchors. Observed Mcd semiquinone formation is distinguished from the cited ACAD-family two-ETF interpretation; PccR complementation is limited to growth and cellular PCC activity.

The added Introduction paragraph 2 in PMID:29283425 describes the ACAD-family two-successive-electron-transfer mechanism; Results 2.3 reports Mcd/ETF activity and semiquinone observation. The record no longer calls its microscopic two-ETF stoichiometry directly measured by those Mcd assays. PMID:26170412 Table 1 under sec3-1 reports complemented-cell PCC activity; sec3-3 supports growth rescue and mutant transcript effects. The record does not infer rescued transcript measurement, direct PccR DNA binding or a measured regulator ligand. The original external finding at findings.json index 1 is retained and linked by issue key/hash through the successor disposition; no canonical previous_occurrences is invented.

### Verified disposition of ethylmalonyl-author-replay-direction-false-pass (issue 416)

provenance: supported. Targets: KEGG:M00373.

The original external false-pass is corrected and independently reproduced as rejection for all 14 directions. A complete positive and final input/output mutation controls pass their intended acceptance conditions.

Every independent single-direction reversal fails at the matching original RDF direction before output-directory creation. The complete independent positive exits 0, binds 141 semantic inputs and 17 outputs, and produces the same 17 artifact hashes as the author positive. Late manifest and KGX mutations exit 1 without accepted output or a success receipt. All 133 original author, 397 original review and 183 correction artifacts were rehashed unchanged in the successor. The original external finding at findings.json index 0 and false-success proof remain historical evidence. Bounded final file rechecks are not an atomic filesystem snapshot.

### Maintained canonical authorities and strict native Protein XML admission

grounding: supported. Targets: KEGG:M00373.

All 66 maintained named IDs/labels are covered by independently sourced canonical authorities. The new native Protein XML parser and malformed-name fix preserve source identity, database version and original valid outputs.

Production builders produce 624 manifest entries, 1871 ontology terms and 2251 source terms, adding 17 original source inputs/terms and 13 ontology terms while preserving every prior term and source metadata object. Scientific Rhea 142 RDF is separate from production Rhea 139 labels: all 14 labels agree and no new Rhea-update selection is introduced. Four META Protein XML sources require exact request/native object identity, PGDB 27.0 and a direct common name. The independent code successor verifies issue 418 malformed references/noncharacters reject without creating/replacing output, while valid beta forms and four authentic originals remain byte-identical. This code review is attributed to its separate reviewer, not claimed as a new full code audit here.

### Maintained adoption, append-only history and inherited review scope

provenance: supported. Targets: KEGG:M00373.

The maintained target is byte-identical to the independently accepted corrected draft. The original and correction evidence remain separate, and prior corpus records and authority metadata are preserved.

This reviewer read all 1,750 maintained YAML lines and directly checked 66 labels, 221 prior record bytes, 90 adopted archives and 17 cached-original copies. The current corpus has 222 records. Historical author ledger statements remain historical where successor evidence corrects ETF wording or DRAM shorthand. Append-only record and parser history correctly describe their creation-time pending gates. Broader source-to-graph, primary literature and 19 sequence coverage comes from /root/ethylmalonyl_independent_review; this reviewer authored only the independent successor assessment, current input reconciliation and this governed review. Source originals and broad article passages remain external. Final root/peer preservation additionally checks all 221 old pages and complete graph contexts. ADOPTION-README.md retains the exact historical adoption narrative while the final README records later completed gates.

### Complete graph rendering, source contexts and actual maintained gates

graph: supported. Targets: KEGG:M00373.

The rendered record faithfully exposes 65 incident nodes, 105 asserted edges and all 155 evidence items; all 326 checked in-page links resolve. Whole-corpus gates pass with no unresolved graph or identifier defect.

The taxon is declared but has no asserted graph edge, explaining 65 SVG nodes versus 66 KGX contexts. The 105 edges comprise 14 membership, 50 chemical-side, 13 flow, four assembly-component, ten catalysis, three enables, ten cofactor and one regulation assertion. Full export has 3,775 global nodes and 10,751 edges. Previous 10,646 edges, 3,745 contexts and 221 pages are preserved. Existing source-role unions explain shared-node category differences; all contextual directions match. RHEA:21037 and RHEA:45798 global names change to canonical equations through existing deterministic selection while prior contextual labels remain. Root ran all full gates; this reviewer inspected their actual receipts and verified original versus archived log hashes. The first preservation checker used an overstrict global-equals-target category assumption; its preserved failure and independently supported corrected checker do not indicate a product defect.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-target | data/pathways/ethylmalonyl-coa-pathway.yaml; Entire 1,750-line record; identity, participants, 14 reactions, 105 edges and 44 references | supports | Complete maintained target read directly. Corrected draft and maintained bytes agree; all 66 named identifiers and labels were independently reconciled with current authorities. |
| e-original-review | research/pathway_additions/2026-10-11-next-221/initial-review/review.json; complete scientific assessment and coverage; reviewer /root/ethylmalonyl_independent_review | supports | Preserved original independent scientific review covers every reaction, participant side, graph edge, evidence item, reference and declared ID, including exact sequence bridges. Its only two original findings are separately corrected. This is inherited evidence, not a claim that this reviewer repeated that entire original literature audit. |
| e-coverage | research/pathway_additions/2026-10-11-next-221/original-author/source-projections/coverage.json; Full native KEGG M00373 definition versus MetaCyc PWY-5741 boundary | supports | Source projection independently checked by the original scientific reviewer supports all 14 mandatory transformations, both terminal branches and the distinction from the native 11-member MetaCyc route. |
| e-dedup | research/pathway_additions/2026-10-11-next-221/dedup/current-dedup-compact.json; current-base complete/split route comparison and DRAM coordinates | supports | Current-base dedup supports the distinct full M00373 record; DRAM coordinates and RN identifiers remain contextual annotations rather than a complete competing pathway definition. |
| e-dedup-bind | research/pathway_additions/2026-10-11-next-221/dedup/actual-merge-binding.json; current baseline and external dedup input binding | supports | Dedup evidence is bound to the actual maintained baseline; the original search included ignored/hidden files and followed symlinks. |
| e-native-directions | research/pathway_additions/2026-10-11-next-221/scientific-reassessment/native-directions-independent.json; independent ElementTree streaming parse of original RDF; all 14 selected directional objects | supports | This reviewer independently streamed 326,097 RDF descriptions and checked unique master and left/right side orientation for all 14 selected reactions, without using the author projection or parser. |
| e-chemistry | research/pathway_additions/2026-10-11-next-221/correction/positive/native-direction-and-chemistry.json; all 14 native reactions and 50 chemical sides with coefficients and exact participants | supports | Corrected replay reparses original Rhea RDF and verifies direction, master/side identity and complete chemical sides. This author output is corroborated by the independent full positive and separate native-direction parser. |
| e-flow | research/pathway_additions/2026-10-11-next-221/initial-review/independent-flow-audit.json; 13 material-flow edges and full-route net balance | supports | Original independent flow audit supports material transfer between the complete reactions and formal balance. Physiological flux is not inferred from the formal net. |
| e-successor | research/pathway_additions/2026-10-11-next-221/scientific-reassessment/review.json; pass_for_scoped_corrections; exact predecessor/correction bindings and independent execution | supports | This reviewer independently reassessed the eight-field correction, exact paper anchors, all 14 direction negatives, complete positive, and late manifest/output mutation controls. Original complete scientific coverage is explicitly reused unchanged. |
| e-protein-scope | research/pathway_additions/2026-10-11-next-221/original-author/scientific-ledger.json; selected proteins, native complex components, assay/cofactor scope and uncertainties | supports | Original ledger and original independent scientific assessment retain source-specific protein, construct, complex and cofactor scope. Historical ledger ETF wording is superseded by the exact corrected target and successor assessment. |
| e-current-auth | research/pathway_additions/2026-10-11-next-221/integration-review/canonical-preparation-maintained-audit.json; 66 named IDs/labels; complete prior dictionary/metadata and manifest preservation | supports | This reviewer directly reconciled current record IDs/labels with 1,871 ontology and 2,251 source terms; all prior terms and source objects and the 607-entry manifest prefix are unchanged. This is identity evidence, not functional evidence. |
| e-scope | research/pathway_additions/2026-10-11-next-221/correction/source-scope-qualifications.json; retained scientific qualifications after the eight-field correction | supports | Explicit qualifications preserve abstract-only access, uncertain enzyme assignments, assembly inference, construct length, assay metals, formal ETF state and PccR limitations. |
| e-delta | research/pathway_additions/2026-10-11-next-221/scientific-reassessment/record-delta-independent.json; exact eight changed parsed fields; unchanged chemistry/IDs/graph/reference objects | supports | This reviewer independently calculated the original-to-corrected record delta. Changes are restricted to descriptions, evidence assertions and locators; all other parsed values are identical. |
| e-dispositions | research/pathway_additions/2026-10-11-next-221/scientific-reassessment/dispositions.json; ethylmalonyl-author-replay-direction-false-pass and ethylmalonyl-paper-anchors-and-etf-inference | supports | The independent successor links the original external issue keys and exact evidence hashes to verified correction outcomes for issues 416 and 417. These external observations are not fabricated governed previous occurrences. |
| e-original-findings | research/pathway_additions/2026-10-11-next-221/initial-review/findings.json; indices 0 and 1; exact stable external issue keys | supports | Historical independent findings remain immutable: direction replay false-pass was major, ETF/PccR source scope was minor. Their original existence and impact are retained even though current maintained bytes are corrected. |
| e-false-pass | research/pathway_additions/2026-10-11-next-221/initial-review/direction-false-pass-proof.json; original actual wrong-direction mutant accepted by original helper | supports | The original concrete negative control demonstrates the pre-correction false pass; successor negative controls verify correction of that exact mechanism. |
| e-directions-controls | research/pathway_additions/2026-10-11-next-221/scientific-reassessment/directions-results.json; 14 independently executed one-direction mutants | supports | Every individual reversal exits 1 with NATIVE_DIRECTION_MISMATCH for its corresponding reaction before an output directory exists. Each fixture updates the record binding so the intended direction check, rather than a byte guard, rejects it. |
| e-positive-control | research/pathway_additions/2026-10-11-next-221/scientific-reassessment/positive-results.json; independent complete positive process and 17 output hashes | supports | Independent replay exits 0 and verifies 141 semantic inputs and 17 outputs. Every final output hash agrees with the separately executed author positive. |
| e-final-controls | research/pathway_additions/2026-10-11-next-221/scientific-reassessment/final-manifest-results.json; actual mutation after semantic checks; companion final-output-results.json | supports | Late manifest mutation fails MANIFEST_CHANGED_AT_PUBLICATION; the separately bound companion late KGX-output mutation fails OUTPUT_HASH_MISMATCH. Both child processes exit 1 with no accepted output or success receipt. |
| e-final-output-control | research/pathway_additions/2026-10-11-next-221/scientific-reassessment/final-output-results.json; actual KGX work/edges.tsv mutation at pre-publication checkpoint | supports | Independently executed post-check output mutation is detected at final publication binding and leaves no accepted output. |
| e-authority-build | research/pathway_additions/2026-10-11-next-221/authorities/canonical-build/report.json; both canonical builders and before/final original source hashes | supports | Actual canonical ontology/source builds succeeded against the pinned 624-input source manifest and whole SQL sources; prior terms and metadata are preserved. This build execution is attributed to its recorded operator. |
| e-xml-review | research/pathway_additions/2026-10-11-next-221/authority-code/reassessment/assessment.json; independent successor for issue 418; results.json cases and exact parser binding | supports | Independent parser reviewer checked rejection of residual malformed character references and noncharacters, preserving existing output/no output on failure, while valid beta encodings and authentic originals remain unchanged. |
| e-adoption | research/pathway_additions/2026-10-11-next-221/integration-review/adoption-audit.json; 90 archives, 17 original cache copies, corrected target and three authority outputs | supports | Independent technical peer confirms exact adopted bytes and preservation of 772 historical record/review/history files. The peer explicitly excludes a new scientific audit and unfinished full gates. |
| e-history | history/records/ethylmalonyl-coa-pathway/2026-10-11T211820Z-codex-214a7d.yaml; complete native history entry and linked parser history | supports | Append-only creation history correctly records original issues 416/417, adoption evidence and gates pending at creation. It is not rewritten after later gates complete. |
| e-integration-peer | research/pathway_additions/2026-10-11-next-221/integration-review/review.json; complete bounded technical peer verdict and explicit scope exclusions | supports | Independent integration reviewer verifies authority labels, adoption, parsed graph/KGX output and prior corpus preservation. This is a bounded technical review, not a replacement for scientific evidence or final exact-head review. |
| e-generated-graph | research/pathway_additions/2026-10-11-next-221/integration-review/integrated-outputs.json; 65 interactive SVG nodes, 105 edges, 155 evidence items, 326 links and 66 KGX contexts | supports | Programmatic independent graph audit verifies complete new graph/evidence/context counts and prior 10,646 KGX edges, 3,745 node contexts and 221 index entries. Two global display names follow existing canonical selection while old record contexts remain unchanged. |
| e-old-pages | research/pathway_additions/2026-10-11-next-221/integration-review/old-page-preservation.json; all 221 prior record pages, ignored/hidden-aware symlink-following inventory | supports | All prior record-page bytes are preserved; current page population is 222. No interactive browser inspection is claimed. |
| e-preparation-incidents | research/pathway_additions/2026-10-11-next-221/integration-review/canonical-preparation-preparation-incidents.json; three bounded reviewer preparation errors and corrected audit execution | supports | Reviewer display/count assumptions were corrected before the final maintained reconciliation. Original failure observations are retained; these preparation errors made no maintained changes and are not product findings. |
| e-etf-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC6017585/; PMID:29283425; //section[@id="sec1-molecules-23-00068"]/p[2]; //section[@id="sec2dot3-molecules-23-00068"]; Table molecules-23-00068-t001 and Methods 4.1 | supports | Directly inspected pinned native HTML distinguishes the cited ACAD-family two-ETF electron-transfer interpretation from observed Mcd/ETF activity and semiquinone formation; construct table retains purified tagged-protein scope. |
| e-pccr-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4560284/; PMID:26170412; section#T1 under section#sec3-1; section#sec3-3; Figure 1; section#sec4/p[1] | supports | Directly inspected pinned native HTML supports complemented-cell PCC activity and growth rescue. Transcript figure compares wild type and deletion mutant, without measured complemented transcript rescue; unsuccessful soluble PccR purification does not establish direct promoter binding. |
| e-final-gates | research/pathway_additions/2026-10-11-next-221/final-validation/gates/execution.json; All six actual root-owned commands, times, log hashes and zero exit codes; each receipt and lossless log wrapper is a captured context input | supports | Rendering, full validation, 1,378 passing tests with three empty command-frontmatter parametrization skips, lint, full KGX export and tracked whitespace check passed. Actual log bytes were independently rehashed and compared with their lossless maintained JSON wrappers; these executions are attributed to root, not rerun by this reviewer. |
| e-final-preservation | research/pathway_additions/2026-10-11-next-221/final-validation/preservation-successor.json; Passed successor; 221 records/pages, 10,646 old edges, 3,745 old contexts, 105 target edges and 66 target contexts | supports | Final root preservation audit confirms exact old record/page bytes and all old and target graph contexts. Native explicit-role unions and contextual directions agree. Initial overstrict target-only-category checker failure remains preserved and did not require a product change. |
| e-category-peer | research/pathway_additions/2026-10-11-next-221/integration-review/shared-categories.json; All 66 target nodes; exact source-role union, explicit-role precedence and contextual directions | supports | Independent peer directly verified shared-node role reconciliation, including existing MolecularActivity versus new reaction-only context, without requiring corpus-global categories to equal isolated target-only categories. |
| e-final-geometry | research/pathway_additions/2026-10-11-next-221/final-validation/graph-audit.json; Actual target SVG node boxes, edge paths, labels, endpoints and anchors | supports | Root programmatic audit verifies complete rendered graph counts, evidence anchors and geometry within the SVG. This is not browser inspection or biological inference. |
| e-vendored | research/pathway_additions/2026-10-11-next-221/final-validation/vendored-check.json; Actual check_vendored_sync.sh terminal result | supports | All 22 governed artifacts match the pinned claw revision; root execution exited zero. |
| e-readme-provenance | research/pathway_additions/2026-10-11-next-221/final-validation/readme-provenance.json; Current README versus preserved exact ADOPTION-README.md and distinct PREPARATION.md | supports | Final narrative has completed gate status; original adoption README bytes remain separately preserved with the exact immutable historical hash. Historical evidence statements are not silently restamped. |

## Limits And Additional Notes

- The broader full original scientific review is reused explicitly with byte-identical unchanged inputs; this reviewer newly checked the complete maintained YAML, current bindings, all 14 native directions and the two-paper correction, but does not claim a second full literature/protein-sequence audit.
- PMID:18819910 and PMID:19703103 full texts were unavailable; abstract metadata and reviewed database annotations retain their distinct evidence scope. Uninspected primary methods or supplements are not asserted verified.
- Exact PhaB and crotonase protein assignments remain unresolved; their chemical steps are present. Mcl2 oligomer ambiguity, inferred PCC/MCM assemblies, alternative assay metals, AM1 stereochemical wording and the native CPD9409 conflict remain explicit.
- The native 548-aa Mcd product, its 555-aa counterpart and purification tags are separate evidence scopes; no processing explanation or construct equivalence is inferred.
- Formal reaction balance and whole-ETF states do not prove physiological flux or microscopic two-ETF stoichiometry. PccR direct promoter binding and a propionyl-CoA ligand remain unestablished.
- Pinned source bodies and the earlier successful 20-organism iModulonDB inventory inform this review. No fresh whole-source discovery, database-exhaustion claim or new iModulonDB inventory is made; a nonmatching dataset is not negative biological evidence.
- Static SVG/KGX checks are programmatic; no browser interaction or whole-figure/supplement visual review is claimed. The full-corpus gate outcomes are attributed to the actual root execution, not falsely claimed as separately rerun here.
- External original findings have no governed review identities. Their verified fixes are recorded in evidence-linked assessments with exact issue keys and source hashes, without fabricated canonical previous_occurrences.
- The source replay performs bounded filesystem checks, not an atomic snapshot. Interpreter and every installed third-party dependency are not individually hashed.
- Public-release licensing remains deferred by the user. This scientific observation does not grant redistribution rights or itself authorize publication or native status promotion.
- Original external findings retain exact stable keys and preserved proof files. No governed predecessor exists for these target findings, so verified external corrections are assessments rather than fabricated terminal findings.
- Root full gates used UV_NO_SYNC=1, bytecode disabled and the existing 195 environment; no dependency synchronization was performed. Maintained gate logs are lossless JSON wrappers verified against original raw bytes.
- Reviewer preparation display/count assumptions and peer/root checker assumptions are preserved separately with their corrected actual outcomes; no product source was changed by this reviewer. A later read initially used the wrong directory for readme-provenance.json, then located the exact final-validation file with an ignored-aware inventory; this was a read-only path correction.
- This review is an immutable scoped observation and does not promote native status or grant source redistribution rights.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T213727Z-ethylmalonyl-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of the complete ethylmalonyl-CoA pathway
started_at: '2026-10-11T21:19:38.475320Z'
finished_at: '2026-10-11T21:37:27.356806Z'
reviewer:
  identity: Codex /root/ethylmalonyl_successor_review
  kind: agent
  independence: independent
  independence_basis: Reviewer authored neither the maintained pathway nor its correction,
    parser, authority selection, history or generated outputs. This reviewer independently
    reassessed the two original scientific/replay findings and performed current maintained-input
    reconciliation. The earlier complete scientific source/sequence review belongs
    to /root/ethylmalonyl_independent_review and is explicitly inherited with unchanged
    bindings; the bounded integration and parser reviews are attributed to their separate
    reviewers.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete 14-reaction KEGG M00373 ethylmalonyl pathway is supported within
  its explicit native, experimental and inferred scopes. Preserved full original independent
  scientific coverage is combined with this reviewer's independently executed source-direction
  and two-paper correction reassessment and current maintained-byte inspection. External
  issues 416 and 417 are addressed, and the separate authority-parser successor addresses
  issue 418; no unresolved finding remains in this record scope. Actual maintained
  full gates pass. Formal balance, identifier admission and deterministic graph checks
  do not establish broader biological claims.
source:
  git_revision: 7b5201e93c0608631af73e629780d829efd26426
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
    sha256: 8986e0aa609719692dbb07dfd78cadc3acf99dded0ce0f3641665d77ea5f7e26
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: conf/rhea_identifier_updates.json
    sha256: b6126588233559a7243fbcba3ff4c3a94594831d57c64b3841d4805b1b5a27a1
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 505d40e7422ddc43aea7e0dd934d8ba8d448815a160a56d78663b4f3051e8da9
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: bb462c5cc88cce38a85a557b190c01a96b3a6b113f4d18333d360192714fea6a
    role: context
  - path: data/pathways/ethylmalonyl-coa-pathway.yaml
    sha256: 1c58f2d1b27fd7a8a3928971a49311a742e004a1b28f349b9331b8fe0f369912
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
    sha256: 9c2e12392d11b8f3073f29e92928c005e8c59eb8d94ee040ab25fb41b70a38f2
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/infrastructure/metacyc-protein-xml-authority/2026-10-11T211823Z-codex-94e406.yaml
    sha256: 72422b60fd1c4be5730f661cea0941ff96a1471abf05dbe33d4cb0ffe3cf4c0d
    role: context
  - path: history/records/ethylmalonyl-coa-pathway/2026-10-11T211820Z-codex-214a7d.yaml
    sha256: 7fa19c38c4157bfcfb457048703a35eb5d367054e341c18651e6d89546ce65a3
    role: context
  - path: pages/downloads/edges.tsv
    sha256: efc22a1cf3c22f20bc5103dedfd33ceb26cf6a10cad7a9324e09c7e5fcc2b543
    role: context
  - path: pages/downloads/manifest.json
    sha256: 9575cfcf1d680f355aeb0216f738f75ef44621a8e9aba80d6bbe8f402293b898
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 921d019c2dcd922358c267a3e70f2563150e3f1e473d8f69232042732f9b48f1
    role: context
  - path: pages/pathway_index.json
    sha256: 65073868f62d070a5e66a36dfb978a122443dfd2a11963366efa2f6abfdb329c
    role: context
  - path: pages/records/KEGG_M00373.html
    sha256: f8e7a7461dd08637b4941c7735fb1a0e053cb41c773d6150c747ddd63f49d03a
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/ADOPTION-README.md
    sha256: 050f2b20e6384f46e3b23d0f2d31ee818d9bc90ff1bb0ca90ab1ef388b1cd867
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/PREPARATION.md
    sha256: fca1ba81240cb52254d0d9d6cc772ee792681fb42174b00884f85404e5c66a30
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/README.md
    sha256: efbf508e65d2f294f0a9602cbda3731e427e89f3a20b637f9f25751b4e208dbf
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authorities/assessment.md
    sha256: 10b5ac555b77494268e30ca902c03b2ad1e00ee4f29ca1e182a700be6c054e1b
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authorities/canonical-build/before-original-hashes.json
    sha256: e99af726650ec45919ac9763317664e0d154ebdc6b63be511428518dddbc1dea
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authorities/canonical-build/execution.json
    sha256: 771df854b8d53e5c5bd3706d4d75a5ab01e375f909715b348e0cda0768681763
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authorities/canonical-build/final-original-hashes.json
    sha256: 1a8c02797f409c13df8141f4316f1ac82c09b0f62fc818f14cf010f05d593e74
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authorities/canonical-build/report.json
    sha256: eb9fc9121007aba86085e5415fcb851d53d77cd644382d99db286c55310d64d8
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authorities/selection-provisional.json
    sha256: 844e85f33f1d17cf4f2c8ec5284f980aea4d25bc443b3dfb7e68e2639496af41
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authority-code/initial-review/review.json
    sha256: c3ff6251c4fc77911c53df0838068d01e6895ebf91025fd4baa14cf69ceeec7e
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authority-code/reassessment/assessment.json
    sha256: 882c1d99dcfd1d389fd5c0267c87c176e72822d4477cfd7becac8153a5f3fb2c
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authority-code/reassessment/assessment.md
    sha256: 3e35c714d17a84d3aa3404ebbfbc51be01e3310d1fb27a1594e070e45ad7ee21
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/authority-code/reassessment/results.json
    sha256: 2c894ebdd23c161aa588a5167d382adda9f49088bfa5d3e10f6cb04f626e2db3
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/README.md
    sha256: 2a93a63eff8a91a64e32e4d142408ac54b9bce5ebcd055be732689de4d035642
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/early-control-results.json
    sha256: e450244e19bbd5c58970d8770c43d0ea5b9451c13bb59c2bc69558eee6a06018
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/late-control-results.json
    sha256: 020dad74355fc4691a6769f7ac168f234d4b483ad6ba224369df500056a018ff
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/positive-control-result.json
    sha256: 81b223cca1cbf9b039b568e638c2126218765b52575c47c6fe3e3d10f44b6b0a
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/positive/author-checks.json
    sha256: 6de7c0eb81fe6e1846be0fbfc8cb7e9806eebdb07ad33be7c161847543a79be6
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/positive/native-direction-and-chemistry.json
    sha256: 3e7f178b17218c50a12ea419f447c81af52c41977b236ed4e369dbf24b95cf19
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/positive/success-receipt.json
    sha256: 4dc18012a6d3df28fe296fa8ebdd85aa4b93c2baab7319d60c4702601a9bdfe0
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/record-delta.json
    sha256: 8c47971d76b4db714eb5084968a6e8075301baace488a2d58d90764a73ae1594
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/replay-author.py.txt
    sha256: 69b75d3aa7ef4d92288e116bf028b123555d79dd98a15def44f734bae0bd82e2
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/correction/source-scope-qualifications.json
    sha256: 80630d522d21757e1f53ecfba35e1f94546bb4fd455ead19a3fa8b3950e34406
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/dedup/actual-merge-binding.json
    sha256: 60b7710eebdac02faa7ea8f3bce54acbee2b00f215da00ff9e69dfbb8d85ac83
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/dedup/assessment.md
    sha256: 48672c5aa1d1a35a97354788ad23026f3001c76db8f7d7e5ee39212087eb791e
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/dedup/current-dedup-compact.json
    sha256: 16698a5a23881b0db87f4545772a19cb3d1fd4c8cf5ee1ada1dceb5c76b1f208
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/dedup/dram-source-recheck.json
    sha256: 2d936fe026fe995688393348de61b448c2b5b341cbb82ee370e4cd25da277ba5
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/archive-receipt.json
    sha256: 5d14b6f8c1cd9fc4fc59eaa279dbd76ba81ff35ba29881d95f8022e2e33368c3
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/execution.json
    sha256: ca60d29c913efcd09192af8e24eeab8c2cb28c01ab97a667d9d9bdb567eebcac
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/kgx-log.json
    sha256: 2ff16355fdface5b45fa44a16324bfa94f5265803d5e233d5093e29f5b822aeb
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/kgx-receipt.json
    sha256: 955d8b878551d6d514b1d5aab60f44a3c55163e4fbe8a9c2141e8a7760afada3
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/lint-log.json
    sha256: 73651373649a818131cd599cd498feee2b5f78426ba9ddd1246fb8a38c7d86a8
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/lint-receipt.json
    sha256: 6e0e10e0719cb61071ed5889a5353aa408f35a5262037794863745715c12d3a4
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/render-log.json
    sha256: d4d7ce2dc586e799285211f605bc44f3590c4aa6cb868bf0a50c8a7b20e9af0c
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/render-receipt.json
    sha256: 37a0b16f5266f8b80cee045f6c04926fc27855c2db3a36be834bae0560b3d390
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/test-log.json
    sha256: 94cbfb0210b4f129878a0be3588e97eef52504a5458f84d5404d5876b9b24607
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/test-receipt.json
    sha256: 1d3e84efcc12f4c3cbb98905d455dddfb8e20c9c2af17cc747b9f9f08950e90d
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/validate-log.json
    sha256: 40c824ec7df781bc9a38676e5aa8bdb10260d313034bd8e7f412a369dd434e00
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/validate-receipt.json
    sha256: 156a67b495d02f96682efeae6efd86df762a1cf7f9a6a4f6ddf9e45fe8ca64ed
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/whitespace-log.json
    sha256: cdc2a1dedf052adea82d48b4fa74b96cf922f6fbd6fc9ef753f84ccbe3134d79
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/gates/whitespace-receipt.json
    sha256: ba8ed1d38b6effa01c5dd190602ef7aaf7268e9cc4fe5b6be8e79220a9050d7f
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/graph-audit.json
    sha256: 04dc1ffafe741929a7ebf86d4a0fe0dd1aa6477c2341b745b6821f9350546c0e
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/history-scaffold.json
    sha256: d7cf6e4f24a75ff0277370309c6b867c70d004227a1c0f13326afcd77424ab62
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/preservation-checker-incident.json
    sha256: ff85b7d71ae42435e29bd8c979e6214ab602466edf2fb7c39b95fb02de46ace9
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/preservation-successor.json
    sha256: d00b37727a83aa1827e2d9261cb3475d360688b7b02f6cdbc03d6b08ea7a17be
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/readme-provenance.json
    sha256: 6a07cb7c9187f7ae5e4fc4b100a65949d8eb68711d2610518db11a2e3842fad1
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/final-validation/vendored-check.json
    sha256: 3cf03d0650ee5e7869ea914cd6c572979d78b4f99005620909549ff07b48ee69
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/initial-review/direction-false-pass-proof.json
    sha256: 4d0284e8bd1b0e8b708be7f287c0eaffc2533b704321a04cb395758c57fd11e2
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/initial-review/findings.json
    sha256: b0e48858c2896435f8f407510a24c4607a8a3c22fc803a9fe18437f864510324
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/initial-review/independent-dram-source-audit.json
    sha256: 6ba4806b97cda0faf4667a092ef28bb702ca53a48c883da201e75b773bbe8170
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/initial-review/independent-flow-audit.json
    sha256: 3fe71db81ecebdecccf8d19f717d47cecc40614248dc6211db5205ff19f38053
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/initial-review/review.json
    sha256: b24601e12243caa89c72d4ca8da9f73db9726d35577390485a24050832f47492
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/initial-review/review.md
    sha256: 88e324098425772276221cec1347ad741f036a8bdd422b802c1071a3fb2de1aa
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/adoption-audit.json
    sha256: 39daa441d851bf793a682029ff4ffbce9d76c8ed60f11f0f0820f2e7aa9bea0a
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/authority-preservation.json
    sha256: 4cdf7b7e1d232987dda1516619164564f19a555a0eca21fb79adb566288cbe6f
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/canonical-preparation-maintained-audit.json
    sha256: e42bd0e33a0faee3f82e1163f78b439fc085fdbbdd4580409f7dcf7054626f8e
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/canonical-preparation-preparation-incidents.json
    sha256: 282bc5d6f0389183b7b016f353d0d39d18510d73a36994d5c2beb1c2c469dc5b
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/completed-gates.json
    sha256: 5cd784178a6cca2b06f6aab29dc28dc7a673b1bfe45758a3bea88b091b6172f6
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/handoff.json
    sha256: 606656a95153b037804d1782586a930634f2a31d5f68b0e3658bea21872248d2
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/initial-checker-failure.json
    sha256: 8087b97609f52c7476860fcc9f4e9e5b67080bf3d05388fb9e340579f0030a79
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/integrated-outputs.json
    sha256: 816e797b435277b95e6e22b2ff6a19098516055e49134792851f84d1eaa8c782
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/new-issuing-labels.json
    sha256: 79f275ea827dd1b91a097978c07096c6131b58a6d5dbd562d35d088c22cfbefa
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/old-page-preservation.json
    sha256: dfd22dca1d1ef4f80749ee7f238c56715bd332e9f2ff44a3a35393e611a645cc
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/preflight.json
    sha256: 296f6f91f86bd17b372fe200882c5b1f45aa9d5aedd9b68d3efc27421b558d37
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/review.json
    sha256: 22c5f0becb329bc93a944651d0e4fa9e6da2c3d5d2ef321e40f27f2c14b774a5
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/shared-categories.json
    sha256: 78282f08670f8197b183525c5bda9ecc711bb9d7c6ec9971bdd3841a655589bc
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/integration-review/supplement-copy-receipt.json
    sha256: abf2abe1926adc31a38cc41714d0433267c3a3d7a9c516d1b7fd853300c15855
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/original-author/edge-count-reconciliation.json
    sha256: 462da6f0c5a5f08faf775b94a93652d845491e984af124be7fff5de6b09757f1
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/original-author/scientific-ledger.json
    sha256: 89d4e64ad7687278bfe856064b7f50b3203ee4fc8966f52001996cde1282a64e
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/original-author/source-manifest.json
    sha256: 0ee20174e4fc6c834fb58f4ac2c71e86c1ce21e582abe9ea695779b8893f69ca
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/original-author/source-projections/coverage.json
    sha256: 22de5d20dc7b395d59f924cf300fe9418efeca03714f4063bcdb452d2aa940db
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/original-author/source-projections/reference-bindings.json
    sha256: cc5e958bed456ee5936d6ecee8687a9a9170334e6425c14e7af05c2ddb101f03
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/record-integration.json
    sha256: 78e22274b0dfa476a5bb006cef888269df2a97d799ac8eabc91536ec9e25af4b
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/directions-results.json
    sha256: 8c147e7b93c1d7d2b78184a0be90b9a5aa4fd4d3d491c70c37a70f2f329c5059
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/dispositions.json
    sha256: 0bc48d2b8b1540811cb43404eb1e854f2553a90fbb5439944a2b84fac61c6fb3
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/evidence-summary.json
    sha256: 69d09afc44b3b38ba8e5d3435061b2ff71876d8473134d5086856be0786ef10c
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/final-manifest-results.json
    sha256: afcdfffa1f736f060d02520bf4aa49b495e4190eff7a87db39ed2cfff91f3d44
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/final-output-results.json
    sha256: d416e61d1242082b61a9893865f8171e5f14eaca4be9f6c5364f01f75db52d2e
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/handoff.json
    sha256: 0171ea11a2348429c83c22eb50f27c8b564d28ae2b46f99ba3cffde074a7b63c
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/native-directions-independent.json
    sha256: 5661ad05a83ddd58790e8cb32c35d041213dddedec3a5da9cf99d608b74cd899
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/positive-results.json
    sha256: 6f9a437cd689230b9516b8871e881d38e1415d39200f6dfb7ed002923bd66f9b
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/record-delta-independent.json
    sha256: 152805a97985d84d610e86793819d16b0eafbd1887113c8a9eaebeed2ef77f45
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/review.json
    sha256: bf480dd09ba0bbc78f7da7b0ef07a85fbe920aad6ee622ab955f536dfe755be6
    role: context
  - path: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/review.md
    sha256: 3cbb1c1484ccf1261eddd1a479622e04d5f8d8b32443380899e184a835adced4
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/build_ontology_identifier_snapshot.py
    sha256: 538dc16bbe67b5f5a3faacf01c968f32900b6fdb76e71f55ebb933ccf8e7a715
    role: context
  - path: scripts/build_source_identifier_snapshot.py
    sha256: ed21fee4f6bd60e095c45a57b69ceb0a94db3fc672b1820c02eeaf6a11d96e4c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/pathwaymech/schema.py
    sha256: e81f95da70943090d470b1837d248fec2a592c5f4b53fc6587bc4214adbf35f3
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 5e4a0bcb5b4901b603e9e0e89ce8b2172efbd8fcbe5e68cac7283555c6a1c056
    role: context
  - path: tests/test_metacyc_protein_authority.py
    sha256: a62e324ecf90f1f9e7ebcf9f06a923be0926e8a9c23ee8c580c951322aea2880
    role: context
scope:
  description: One complete maintained pathway record, including exact identity, taxon,
    participant/reaction/edge evidence, retained limitations, authority grounding,
    complete rendered graph and final maintained gates. Broader full-source coverage
    is inherited from the preserved original independent review; new work covers the
    complete maintained YAML, all 14 native directions, exact changed paper anchors,
    rejection controls, positive replay and current input reconciliation.
  selection: Explicit maintained KEGG:M00373 record adopted byte-identically from
    the independently accepted corrected draft at baseline 7b5201e93c0608631af73e629780d829efd26426.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - KEGG:M00373
  exclusions:
  - target: Other 221 scientific record contents
    reason: Preservation is verified, but they are not newly scientifically reviewed.
  - target: A second full literature/protein-sequence audit
    reason: Complete prior independent coverage is explicitly inherited with exact
      unchanged evidence bindings; only the identified corrections were newly re-audited
      at source level.
  - target: PR head, merge, deployment and public release
    reason: This observation binds current maintained input bytes; those later operations
      and licensing decisions are separate.
targets:
- target_id: KEGG:M00373
  path: data/pathways/ethylmalonyl-coa-pathway.yaml
  label: Ethylmalonyl pathway
  record_class: PathwayRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ethylmalonyl-coa-pathway.yaml
    role: Maintained scientific record; source-to-graph claims are curated here.
checks:
- check_id: c-render
  name: Actual root render gate
  status: passed
  required: true
  summary: Recorded actual render command completed with exit zero.
  target_ids:
  - KEGG:M00373
  command: just render-pages
  exit_code: 0
  evidence_ids:
  - e-final-gates
  scope_note: Executed by root in this maintained worktree using the pinned 195 runtime;
    actual receipts and log bytes inspected by this reviewer. Full-corpus scope where
    applicable.
- check_id: c-validate
  name: Actual root validate gate
  status: passed
  required: true
  summary: Recorded actual validate command completed with exit zero.
  target_ids:
  - KEGG:M00373
  command: just validate
  exit_code: 0
  evidence_ids:
  - e-final-gates
  scope_note: Executed by root in this maintained worktree using the pinned 195 runtime;
    actual receipts and log bytes inspected by this reviewer. Full-corpus scope where
    applicable.
- check_id: c-test
  name: Actual root test gate
  status: passed
  required: true
  summary: 1,378 passed; three empty command-frontmatter parametrization skips; no
    skipped scientific or source checks.
  target_ids:
  - KEGG:M00373
  command: just test
  exit_code: 0
  evidence_ids:
  - e-final-gates
  scope_note: Executed by root in this maintained worktree using the pinned 195 runtime;
    actual receipts and log bytes inspected by this reviewer. Full-corpus scope where
    applicable.
- check_id: c-lint
  name: Actual root lint gate
  status: passed
  required: true
  summary: Recorded actual lint command completed with exit zero.
  target_ids:
  - KEGG:M00373
  command: just lint
  exit_code: 0
  evidence_ids:
  - e-final-gates
  scope_note: Executed by root in this maintained worktree using the pinned 195 runtime;
    actual receipts and log bytes inspected by this reviewer. Full-corpus scope where
    applicable.
- check_id: c-kgx
  name: Actual root kgx gate
  status: passed
  required: true
  summary: Recorded actual kgx command completed with exit zero.
  target_ids:
  - KEGG:M00373
  command: just kgx-export --output-dir /private/tmp/pathwaymech-ethylmalonyl-integration-20261011/gates/kgx
  exit_code: 0
  evidence_ids:
  - e-final-gates
  scope_note: Executed by root in this maintained worktree using the pinned 195 runtime;
    actual receipts and log bytes inspected by this reviewer. Full-corpus scope where
    applicable.
- check_id: c-whitespace
  name: Actual root whitespace gate
  status: passed
  required: true
  summary: Recorded actual whitespace command completed with exit zero.
  target_ids:
  - KEGG:M00373
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - e-final-gates
  scope_note: Executed by root in this maintained worktree using the pinned 195 runtime;
    actual receipts and log bytes inspected by this reviewer. Full-corpus scope where
    applicable.
- check_id: c-scientific
  name: Complete maintained scientific assessment
  status: passed
  required: true
  summary: All 1,750 maintained YAML lines read; exact full original independent scientific
    coverage inherited unchanged and separately attributed; own scoped paper/direction
    corrections independently executed.
  target_ids:
  - KEGG:M00373
  evidence_ids:
  - e-target
  - e-original-review
  - e-successor
  - e-etf-primary
  - e-pccr-primary
- check_id: c-replay
  name: Independent direction and publication controls
  status: passed
  required: true
  summary: All 14 reversal negatives reject at the correct original-source direction;
    complete positive and late manifest/output controls satisfy their expected outcomes.
  target_ids:
  - KEGG:M00373
  evidence_ids:
  - e-directions-controls
  - e-positive-control
  - e-final-controls
  - e-final-output-control
- check_id: c-authorities
  name: Current authority labels and preservation
  status: passed
  required: true
  summary: All 66 named IDs/labels agree; all prior terms, source objects, prior record
    bytes and original evidence copies are preserved.
  target_ids:
  - KEGG:M00373
  evidence_ids:
  - e-current-auth
  - e-adoption
- check_id: c-graph
  name: Rendered graph and whole-corpus preservation
  status: passed
  required: true
  summary: Programmatic graph, anchor, geometry, full KGX and old-page preservation
    checks pass; no browser review claimed.
  target_ids:
  - KEGG:M00373
  evidence_ids:
  - e-generated-graph
  - e-final-geometry
  - e-final-preservation
  - e-category-peer
  - e-old-pages
- check_id: c-existing-reviews
  name: Initial governed review integrity
  status: passed
  required: true
  summary: All 93 existing canonical bundles passed before creating this new observation.
    This check does not claim that the new bundle already existed or was validated
    by the prior run.
  target_ids:
  - KEGG:M00373
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/record_review.py
    check --base 7b5201e93c0608631af73e629780d829efd26426
  exit_code: 0
  scope_note: Executed by this reviewer; external initial-review-check.json/log, session
    64014, terminal 2ff25a/0. Post-save native check is a subsequent operation, not
    preclaimed here.
- check_id: c-vendored
  name: Governed artifact synchronization
  status: passed
  required: true
  summary: All 22 governed artifacts match the pinned claw revision.
  target_ids:
  - KEGG:M00373
  command: bash scripts/check_vendored_sync.sh
  exit_code: 0
  evidence_ids:
  - e-vendored
  scope_note: Actual root execution; inspected receipt records session 15656 terminal
    c774d2/0.
evidence:
- evidence_id: e-target
  kind: record_content
  reference: data/pathways/ethylmalonyl-coa-pathway.yaml
  locator: Entire 1,750-line record; identity, participants, 14 reactions, 105 edges
    and 44 references
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Complete maintained target read directly. Corrected draft and maintained
    bytes agree; all 66 named identifiers and labels were independently reconciled
    with current authorities.
  snapshot_sha256: 1c58f2d1b27fd7a8a3928971a49311a742e004a1b28f349b9331b8fe0f369912
- evidence_id: e-original-review
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-221/initial-review/review.json
  locator: complete scientific assessment and coverage; reviewer /root/ethylmalonyl_independent_review
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Preserved original independent scientific review covers every reaction,
    participant side, graph edge, evidence item, reference and declared ID, including
    exact sequence bridges. Its only two original findings are separately corrected.
    This is inherited evidence, not a claim that this reviewer repeated that entire
    original literature audit.
  snapshot_sha256: b24601e12243caa89c72d4ca8da9f73db9726d35577390485a24050832f47492
- evidence_id: e-coverage
  kind: database
  reference: research/pathway_additions/2026-10-11-next-221/original-author/source-projections/coverage.json
  locator: Full native KEGG M00373 definition versus MetaCyc PWY-5741 boundary
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Source projection independently checked by the original scientific reviewer
    supports all 14 mandatory transformations, both terminal branches and the distinction
    from the native 11-member MetaCyc route.
  snapshot_sha256: 22de5d20dc7b395d59f924cf300fe9418efeca03714f4063bcdb452d2aa940db
- evidence_id: e-dedup
  kind: search
  reference: research/pathway_additions/2026-10-11-next-221/dedup/current-dedup-compact.json
  locator: current-base complete/split route comparison and DRAM coordinates
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Current-base dedup supports the distinct full M00373 record; DRAM coordinates
    and RN identifiers remain contextual annotations rather than a complete competing
    pathway definition.
  snapshot_sha256: 16698a5a23881b0db87f4545772a19cb3d1fd4c8cf5ee1ada1dceb5c76b1f208
  search_scope: Pinned current-base route/source inventory with identifier, label,
    slug, exact reaction-set and boundary comparisons; ignored and hidden files included
    and symlinks followed. No database exhaustion claim.
- evidence_id: e-dedup-bind
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/dedup/actual-merge-binding.json
  locator: current baseline and external dedup input binding
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Dedup evidence is bound to the actual maintained baseline; the original
    search included ignored/hidden files and followed symlinks.
  snapshot_sha256: 60b7710eebdac02faa7ea8f3bce54acbee2b00f215da00ff9e69dfbb8d85ac83
- evidence_id: e-native-directions
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/native-directions-independent.json
  locator: independent ElementTree streaming parse of original RDF; all 14 selected
    directional objects
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: This reviewer independently streamed 326,097 RDF descriptions and checked
    unique master and left/right side orientation for all 14 selected reactions, without
    using the author projection or parser.
  snapshot_sha256: 5661ad05a83ddd58790e8cb32c35d041213dddedec3a5da9cf99d608b74cd899
- evidence_id: e-chemistry
  kind: database
  reference: research/pathway_additions/2026-10-11-next-221/correction/positive/native-direction-and-chemistry.json
  locator: all 14 native reactions and 50 chemical sides with coefficients and exact
    participants
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Corrected replay reparses original Rhea RDF and verifies direction, master/side
    identity and complete chemical sides. This author output is corroborated by the
    independent full positive and separate native-direction parser.
  snapshot_sha256: 3e7f178b17218c50a12ea419f447c81af52c41977b236ed4e369dbf24b95cf19
- evidence_id: e-flow
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-221/initial-review/independent-flow-audit.json
  locator: 13 material-flow edges and full-route net balance
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Original independent flow audit supports material transfer between the
    complete reactions and formal balance. Physiological flux is not inferred from
    the formal net.
  snapshot_sha256: 3fe71db81ecebdecccf8d19f717d47cecc40614248dc6211db5205ff19f38053
- evidence_id: e-successor
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/review.json
  locator: pass_for_scoped_corrections; exact predecessor/correction bindings and
    independent execution
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: This reviewer independently reassessed the eight-field correction, exact
    paper anchors, all 14 direction negatives, complete positive, and late manifest/output
    mutation controls. Original complete scientific coverage is explicitly reused
    unchanged.
  snapshot_sha256: bf480dd09ba0bbc78f7da7b0ef07a85fbe920aad6ee622ab955f536dfe755be6
- evidence_id: e-protein-scope
  kind: database
  reference: research/pathway_additions/2026-10-11-next-221/original-author/scientific-ledger.json
  locator: selected proteins, native complex components, assay/cofactor scope and
    uncertainties
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Original ledger and original independent scientific assessment retain source-specific
    protein, construct, complex and cofactor scope. Historical ledger ETF wording
    is superseded by the exact corrected target and successor assessment.
  snapshot_sha256: 89d4e64ad7687278bfe856064b7f50b3203ee4fc8966f52001996cde1282a64e
- evidence_id: e-current-auth
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/integration-review/canonical-preparation-maintained-audit.json
  locator: 66 named IDs/labels; complete prior dictionary/metadata and manifest preservation
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: This reviewer directly reconciled current record IDs/labels with 1,871
    ontology and 2,251 source terms; all prior terms and source objects and the 607-entry
    manifest prefix are unchanged. This is identity evidence, not functional evidence.
  snapshot_sha256: e42bd0e33a0faee3f82e1163f78b439fc085fdbbdd4580409f7dcf7054626f8e
- evidence_id: e-scope
  kind: record_content
  reference: research/pathway_additions/2026-10-11-next-221/correction/source-scope-qualifications.json
  locator: retained scientific qualifications after the eight-field correction
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Explicit qualifications preserve abstract-only access, uncertain enzyme
    assignments, assembly inference, construct length, assay metals, formal ETF state
    and PccR limitations.
  snapshot_sha256: 80630d522d21757e1f53ecfba35e1f94546bb4fd455ead19a3fa8b3950e34406
- evidence_id: e-delta
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/record-delta-independent.json
  locator: exact eight changed parsed fields; unchanged chemistry/IDs/graph/reference
    objects
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: This reviewer independently calculated the original-to-corrected record
    delta. Changes are restricted to descriptions, evidence assertions and locators;
    all other parsed values are identical.
  snapshot_sha256: 152805a97985d84d610e86793819d16b0eafbd1887113c8a9eaebeed2ef77f45
- evidence_id: e-dispositions
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/dispositions.json
  locator: ethylmalonyl-author-replay-direction-false-pass and ethylmalonyl-paper-anchors-and-etf-inference
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: The independent successor links the original external issue keys and exact
    evidence hashes to verified correction outcomes for issues 416 and 417. These
    external observations are not fabricated governed previous occurrences.
  snapshot_sha256: 0bc48d2b8b1540811cb43404eb1e854f2553a90fbb5439944a2b84fac61c6fb3
- evidence_id: e-original-findings
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-221/initial-review/findings.json
  locator: indices 0 and 1; exact stable external issue keys
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: 'Historical independent findings remain immutable: direction replay false-pass
    was major, ETF/PccR source scope was minor. Their original existence and impact
    are retained even though current maintained bytes are corrected.'
  snapshot_sha256: b0e48858c2896435f8f407510a24c4607a8a3c22fc803a9fe18437f864510324
- evidence_id: e-false-pass
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/initial-review/direction-false-pass-proof.json
  locator: original actual wrong-direction mutant accepted by original helper
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: The original concrete negative control demonstrates the pre-correction
    false pass; successor negative controls verify correction of that exact mechanism.
  snapshot_sha256: 4d0284e8bd1b0e8b708be7f287c0eaffc2533b704321a04cb395758c57fd11e2
- evidence_id: e-directions-controls
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/directions-results.json
  locator: 14 independently executed one-direction mutants
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Every individual reversal exits 1 with NATIVE_DIRECTION_MISMATCH for its
    corresponding reaction before an output directory exists. Each fixture updates
    the record binding so the intended direction check, rather than a byte guard,
    rejects it.
  snapshot_sha256: 8c147e7b93c1d7d2b78184a0be90b9a5aa4fd4d3d491c70c37a70f2f329c5059
- evidence_id: e-positive-control
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/positive-results.json
  locator: independent complete positive process and 17 output hashes
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Independent replay exits 0 and verifies 141 semantic inputs and 17 outputs.
    Every final output hash agrees with the separately executed author positive.
  snapshot_sha256: 6f9a437cd689230b9516b8871e881d38e1415d39200f6dfb7ed002923bd66f9b
- evidence_id: e-final-controls
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/final-manifest-results.json
  locator: actual mutation after semantic checks; companion final-output-results.json
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Late manifest mutation fails MANIFEST_CHANGED_AT_PUBLICATION; the separately
    bound companion late KGX-output mutation fails OUTPUT_HASH_MISMATCH. Both child
    processes exit 1 with no accepted output or success receipt.
  snapshot_sha256: afcdfffa1f736f060d02520bf4aa49b495e4190eff7a87db39ed2cfff91f3d44
- evidence_id: e-final-output-control
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/scientific-reassessment/final-output-results.json
  locator: actual KGX work/edges.tsv mutation at pre-publication checkpoint
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Independently executed post-check output mutation is detected at final
    publication binding and leaves no accepted output.
  snapshot_sha256: d416e61d1242082b61a9893865f8171e5f14eaca4be9f6c5364f01f75db52d2e
- evidence_id: e-authority-build
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/authorities/canonical-build/report.json
  locator: both canonical builders and before/final original source hashes
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Actual canonical ontology/source builds succeeded against the pinned 624-input
    source manifest and whole SQL sources; prior terms and metadata are preserved.
    This build execution is attributed to its recorded operator.
  snapshot_sha256: eb9fc9121007aba86085e5415fcb851d53d77cd644382d99db286c55310d64d8
- evidence_id: e-xml-review
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-221/authority-code/reassessment/assessment.json
  locator: independent successor for issue 418; results.json cases and exact parser
    binding
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Independent parser reviewer checked rejection of residual malformed character
    references and noncharacters, preserving existing output/no output on failure,
    while valid beta encodings and authentic originals remain unchanged.
  snapshot_sha256: 882c1d99dcfd1d389fd5c0267c87c176e72822d4477cfd7becac8153a5f3fb2c
- evidence_id: e-adoption
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/integration-review/adoption-audit.json
  locator: 90 archives, 17 original cache copies, corrected target and three authority
    outputs
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Independent technical peer confirms exact adopted bytes and preservation
    of 772 historical record/review/history files. The peer explicitly excludes a
    new scientific audit and unfinished full gates.
  snapshot_sha256: 39daa441d851bf793a682029ff4ffbce9d76c8ed60f11f0f0820f2e7aa9bea0a
- evidence_id: e-history
  kind: record_content
  reference: history/records/ethylmalonyl-coa-pathway/2026-10-11T211820Z-codex-214a7d.yaml
  locator: complete native history entry and linked parser history
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Append-only creation history correctly records original issues 416/417,
    adoption evidence and gates pending at creation. It is not rewritten after later
    gates complete.
  snapshot_sha256: 7fa19c38c4157bfcfb457048703a35eb5d367054e341c18651e6d89546ce65a3
- evidence_id: e-integration-peer
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-221/integration-review/review.json
  locator: complete bounded technical peer verdict and explicit scope exclusions
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Independent integration reviewer verifies authority labels, adoption, parsed
    graph/KGX output and prior corpus preservation. This is a bounded technical review,
    not a replacement for scientific evidence or final exact-head review.
  snapshot_sha256: 22c5f0becb329bc93a944651d0e4fa9e6da2c3d5d2ef321e40f27f2c14b774a5
- evidence_id: e-generated-graph
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/integration-review/integrated-outputs.json
  locator: 65 interactive SVG nodes, 105 edges, 155 evidence items, 326 links and
    66 KGX contexts
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Programmatic independent graph audit verifies complete new graph/evidence/context
    counts and prior 10,646 KGX edges, 3,745 node contexts and 221 index entries.
    Two global display names follow existing canonical selection while old record
    contexts remain unchanged.
  snapshot_sha256: 816e797b435277b95e6e22b2ff6a19098516055e49134792851f84d1eaa8c782
- evidence_id: e-old-pages
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/integration-review/old-page-preservation.json
  locator: all 221 prior record pages, ignored/hidden-aware symlink-following inventory
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: All prior record-page bytes are preserved; current page population is 222.
    No interactive browser inspection is claimed.
  snapshot_sha256: dfd22dca1d1ef4f80749ee7f238c56715bd332e9f2ff44a3a35393e611a645cc
- evidence_id: e-preparation-incidents
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/integration-review/canonical-preparation-preparation-incidents.json
  locator: three bounded reviewer preparation errors and corrected audit execution
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Reviewer display/count assumptions were corrected before the final maintained
    reconciliation. Original failure observations are retained; these preparation
    errors made no maintained changes and are not product findings.
  snapshot_sha256: 282bc5d6f0389183b7b016f353d0d39d18510d73a36994d5c2beb1c2c469dc5b
- evidence_id: e-etf-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6017585/
  locator: PMID:29283425; //section[@id="sec1-molecules-23-00068"]/p[2]; //section[@id="sec2dot3-molecules-23-00068"];
    Table molecules-23-00068-t001 and Methods 4.1
  snapshot_sha256: 92a39a7536d77a990a12c9da65af1e4ad87f30c1cb13208d9f794981595daf7e
  support: supports
  summary: Directly inspected pinned native HTML distinguishes the cited ACAD-family
    two-ETF electron-transfer interpretation from observed Mcd/ETF activity and semiquinone
    formation; construct table retains purified tagged-protein scope.
  accessed_at: '2026-10-11T21:34:16.990821Z'
- evidence_id: e-pccr-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4560284/
  locator: PMID:26170412; section#T1 under section#sec3-1; section#sec3-3; Figure
    1; section#sec4/p[1]
  snapshot_sha256: c8715fbfc2c36bd045e1ebd0d05c7a34410bf4c9e9af47daae901f604639b470
  support: supports
  summary: Directly inspected pinned native HTML supports complemented-cell PCC activity
    and growth rescue. Transcript figure compares wild type and deletion mutant, without
    measured complemented transcript rescue; unsuccessful soluble PccR purification
    does not establish direct promoter binding.
  accessed_at: '2026-10-11T21:34:16.990821Z'
- evidence_id: e-final-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/final-validation/gates/execution.json
  locator: All six actual root-owned commands, times, log hashes and zero exit codes;
    each receipt and lossless log wrapper is a captured context input
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Rendering, full validation, 1,378 passing tests with three empty command-frontmatter
    parametrization skips, lint, full KGX export and tracked whitespace check passed.
    Actual log bytes were independently rehashed and compared with their lossless
    maintained JSON wrappers; these executions are attributed to root, not rerun by
    this reviewer.
  snapshot_sha256: ca60d29c913efcd09192af8e24eeab8c2cb28c01ab97a667d9d9bdb567eebcac
- evidence_id: e-final-preservation
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/final-validation/preservation-successor.json
  locator: Passed successor; 221 records/pages, 10,646 old edges, 3,745 old contexts,
    105 target edges and 66 target contexts
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Final root preservation audit confirms exact old record/page bytes and
    all old and target graph contexts. Native explicit-role unions and contextual
    directions agree. Initial overstrict target-only-category checker failure remains
    preserved and did not require a product change.
  snapshot_sha256: d00b37727a83aa1827e2d9261cb3475d360688b7b02f6cdbc03d6b08ea7a17be
- evidence_id: e-category-peer
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/integration-review/shared-categories.json
  locator: All 66 target nodes; exact source-role union, explicit-role precedence
    and contextual directions
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Independent peer directly verified shared-node role reconciliation, including
    existing MolecularActivity versus new reaction-only context, without requiring
    corpus-global categories to equal isolated target-only categories.
  snapshot_sha256: 78282f08670f8197b183525c5bda9ecc711bb9d7c6ec9971bdd3841a655589bc
- evidence_id: e-final-geometry
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/final-validation/graph-audit.json
  locator: Actual target SVG node boxes, edge paths, labels, endpoints and anchors
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Root programmatic audit verifies complete rendered graph counts, evidence
    anchors and geometry within the SVG. This is not browser inspection or biological
    inference.
  snapshot_sha256: 04dc1ffafe741929a7ebf86d4a0fe0dd1aa6477c2341b745b6821f9350546c0e
- evidence_id: e-vendored
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/final-validation/vendored-check.json
  locator: Actual check_vendored_sync.sh terminal result
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: All 22 governed artifacts match the pinned claw revision; root execution
    exited zero.
  snapshot_sha256: 3cf03d0650ee5e7869ea914cd6c572979d78b4f99005620909549ff07b48ee69
- evidence_id: e-readme-provenance
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-221/final-validation/readme-provenance.json
  locator: Current README versus preserved exact ADOPTION-README.md and distinct PREPARATION.md
  accessed_at: '2026-10-11T21:37:27.335683Z'
  support: supports
  summary: Final narrative has completed gate status; original adoption README bytes
    remain separately preserved with the exact immutable historical hash. Historical
    evidence statements are not silently restamped.
  snapshot_sha256: 6a07cb7c9187f7ae5e4fc4b100a65949d8eb68711d2610518db11a2e3842fad1
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact complete pathway and native alternative boundary
  summary: The record denotes the complete KEGG M00373 ethylmalonyl pathway, with
    all 14 reaction rows and both terminal branches. The 11-member MetaCyc PWY-5741
    route ends in different ATP-forming ligase chemistry and is not asserted to be
    an exact alias.
  evidence_ids:
  - e-target
  - e-original-review
  - e-coverage
  - e-dedup
  - e-dedup-bind
  details: The original independently inspected source definition has 12 mandatory
    orthology groups and 13 KOs; K01965+K01966 is a joint requirement, and K05606/K08691
    each cover two transformations. Mcl2 hydrolysis, all three propionyl conversions
    and the glyoxylate branch are retained. R09291 lacks a native KEGG Rhea DBLINK;
    its independently reviewed RXN-8957/chemistry bridge does not fabricate one. The
    inherited current-base dedup included hidden/ignored files and followed symlinks.
    DRAM contributes four rows/three coordinates/four RN identifiers including R09979,
    not a complete alternative definition.
  dimensions:
  - name: pathway-definition
    value: KEGG:M00373; 14 reactions; 12 mandatory KO groups; 13 KOs
    definition: Exact source-defined module boundary, distinct from a generic acetyl-CoA
      assimilation process.
    evidence_ids:
    - e-coverage
  - name: native-alternative
    value: MetaCyc:PWY-5741 held separately
    definition: ATP-forming terminal ligase differs from the maintained Mcl2 hydrolysis
      boundary.
    evidence_ids:
    - e-original-review
    - e-coverage
  outcome: supported
  target_ids:
  - KEGG:M00373
- assessment_id: a-chemistry
  area: graph
  topic: Native reaction orientation, complete chemical sides and material flow
  summary: All 14 maintained directions and equations agree with the pinned original
    RDF. Fifty chemical sides and coefficients, 13 material-transfer edges and both
    complete branches retain the independently reviewed chemistry.
  evidence_ids:
  - e-target
  - e-native-directions
  - e-chemistry
  - e-flow
  - e-successor
  details: This reviewer separately streamed all 326,097 native RDF descriptions to
    verify selected directional objects and unique master-side orientation. The independently
    executed corrected replay additionally checks all 50 native sides, elements/charge
    and the formal net. Full original chemistry/source-to-graph coverage is explicitly
    inherited from the preserved original independent review. The balanced net consumes
    three acetyl-CoA, CO2, bicarbonate, two NADPH, ATP, water and formal oxidized
    ETF, producing malate, succinyl-CoA, two CoA, two NADP, ADP, phosphate and formal
    reduced ETF. Formal balance is not a measured physiological flux or microscopic
    ETF stoichiometry.
  dimensions:
  - name: reaction-evidence
    value: Native Rhea RDF release 142 chemistry; selected master_L/master_R orientation
    definition: Source orientation is checked independently of display arrows or physiological
      reversibility.
    evidence_ids:
    - e-native-directions
    - e-chemistry
  - name: carrier-scope
    value: RHEA-COMP:10685 and RHEA-COMP:10686 are whole ETF states
    definition: Formal participant states retain the whole carrier; FAD cofactor and
      microscopic semiquinone interpretation are separate.
    evidence_ids:
    - e-target
    - e-successor
  outcome: supported
  target_ids:
  - KEGG:M00373
- assessment_id: a-proteins
  area: grounding
  topic: Exact proteins, assemblies and experimental/inferred tiers
  summary: The maintained 12 UniProt proteins and four native complexes preserve exact
    identity and source-specific evidence tiers. Unresolved PhaB/crotonase assignments
    remain excluded while their chemical reactions remain complete.
  evidence_ids:
  - e-target
  - e-original-review
  - e-protein-scope
  - e-current-auth
  - e-scope
  details: The preserved original reviewer checked 19 exact sequence bridges and all
    selected issuing entries; this canonical observation does not claim those 19 alignments
    were newly rerun. D3JV03 is the native 548-aa ADC44452.1/strain 2.4.1 product,
    distinct from the 555-aa Q3J5V7 counterpart and purification tags. Native component
    copies 2/2/2/6 remain database assertions; primary Mcl1 evidence supports a hexamer.
    Ecm/Mcd homodimers retain reviewed database scope where primary full text was
    unavailable. Mcl2 dimer/trimer remains unresolved, and PCC/MCM assembly inference
    is not promoted to strain measurement. Automatic thiolase/PccA assignments remain
    enables edges.
  dimensions:
  - name: experimental-organism
    value: Cereibacter sphaeroides 2.4.1 / DSM158; historical Rhodobacter name
    definition: Taxon 272943 is the maintained strain context; species 1063 protein
      records require the retained original strain/sequence bridge.
    evidence_ids:
    - e-original-review
    - e-target
  - name: component-evidence-tier
    value: Reviewed experimental annotations, native assembly records and explicitly
      marked automatic/inferred assignments
    definition: Authority labels establish identity; they do not by themselves establish
      catalysis, assembly or experimental scope.
    evidence_ids:
    - e-original-review
    - e-protein-scope
    - e-scope
  outcome: supported
  target_ids:
  - KEGG:M00373
- assessment_id: a-cofactors
  area: evidence
  topic: Cofactors, assay conditions and organism scope
  summary: 'Cofactor and context claims remain appropriately narrow: bound Mcd FAD
    is distinct from whole ETF reaction states; divalent metals remain alternative
    assay supports; B12 and automatic biotin annotations retain their source tiers.'
  evidence_ids:
  - e-target
  - e-original-review
  - e-scope
  - e-protein-scope
  details: Mcl1/Mcl2 metal comparisons and structural buffers do not establish exclusive
    in-vivo occupancy. No zinc claim is inferred for Ccr. AM1 isotope, acetate and
    C1/C2 studies remain corroborating organism/condition context, not exact R. sphaeroides
    protein assignments. CPD-9409 stereochemical disagreement and AM1 figure/assay
    R/S wording conflict remain visible. PMID:18819910 and PMID:19703103 are abstract-only;
    detailed catalytic/assembly/cofactor assertions cite the actually inspected reviewed
    database entries. The broader primary/UniProt audit is inherited with its exact
    unchanged bindings, not presented as newly repeated.
  dimensions:
  - name: metal-conditions
    value: Alternative Co/Mn or Mg/Mn assay support; no simultaneous or exclusive
      physiological occupancy
    definition: Keeps assay conditions distinct from a mechanistic in-vivo metal assignment.
    evidence_ids:
    - e-target
    - e-original-review
  outcome: supported
  target_ids:
  - KEGG:M00373
- assessment_id: a-paper-correction
  area: evidence
  topic: Verified disposition of ethylmalonyl-paper-anchors-and-etf-inference (issue
    417)
  summary: The eight-field correction is supported by precise native paper anchors.
    Observed Mcd semiquinone formation is distinguished from the cited ACAD-family
    two-ETF interpretation; PccR complementation is limited to growth and cellular
    PCC activity.
  evidence_ids:
  - e-target
  - e-delta
  - e-dispositions
  - e-etf-primary
  - e-pccr-primary
  details: The added Introduction paragraph 2 in PMID:29283425 describes the ACAD-family
    two-successive-electron-transfer mechanism; Results 2.3 reports Mcd/ETF activity
    and semiquinone observation. The record no longer calls its microscopic two-ETF
    stoichiometry directly measured by those Mcd assays. PMID:26170412 Table 1 under
    sec3-1 reports complemented-cell PCC activity; sec3-3 supports growth rescue and
    mutant transcript effects. The record does not infer rescued transcript measurement,
    direct PccR DNA binding or a measured regulator ligand. The original external
    finding at findings.json index 1 is retained and linked by issue key/hash through
    the successor disposition; no canonical previous_occurrences is invented.
  outcome: supported
  target_ids:
  - KEGG:M00373
- assessment_id: a-replay-correction
  area: provenance
  topic: Verified disposition of ethylmalonyl-author-replay-direction-false-pass (issue
    416)
  summary: The original external false-pass is corrected and independently reproduced
    as rejection for all 14 directions. A complete positive and final input/output
    mutation controls pass their intended acceptance conditions.
  evidence_ids:
  - e-original-findings
  - e-false-pass
  - e-successor
  - e-dispositions
  - e-directions-controls
  - e-positive-control
  - e-final-controls
  - e-final-output-control
  details: Every independent single-direction reversal fails at the matching original
    RDF direction before output-directory creation. The complete independent positive
    exits 0, binds 141 semantic inputs and 17 outputs, and produces the same 17 artifact
    hashes as the author positive. Late manifest and KGX mutations exit 1 without
    accepted output or a success receipt. All 133 original author, 397 original review
    and 183 correction artifacts were rehashed unchanged in the successor. The original
    external finding at findings.json index 0 and false-success proof remain historical
    evidence. Bounded final file rechecks are not an atomic filesystem snapshot.
  outcome: supported
  target_ids:
  - KEGG:M00373
- assessment_id: a-authorities
  area: grounding
  topic: Maintained canonical authorities and strict native Protein XML admission
  summary: All 66 maintained named IDs/labels are covered by independently sourced
    canonical authorities. The new native Protein XML parser and malformed-name fix
    preserve source identity, database version and original valid outputs.
  evidence_ids:
  - e-target
  - e-current-auth
  - e-authority-build
  - e-xml-review
  details: 'Production builders produce 624 manifest entries, 1871 ontology terms
    and 2251 source terms, adding 17 original source inputs/terms and 13 ontology
    terms while preserving every prior term and source metadata object. Scientific
    Rhea 142 RDF is separate from production Rhea 139 labels: all 14 labels agree
    and no new Rhea-update selection is introduced. Four META Protein XML sources
    require exact request/native object identity, PGDB 27.0 and a direct common name.
    The independent code successor verifies issue 418 malformed references/noncharacters
    reject without creating/replacing output, while valid beta forms and four authentic
    originals remain byte-identical. This code review is attributed to its separate
    reviewer, not claimed as a new full code audit here.'
  outcome: supported
  target_ids:
  - KEGG:M00373
- assessment_id: a-preservation
  area: provenance
  topic: Maintained adoption, append-only history and inherited review scope
  summary: The maintained target is byte-identical to the independently accepted corrected
    draft. The original and correction evidence remain separate, and prior corpus
    records and authority metadata are preserved.
  evidence_ids:
  - e-target
  - e-adoption
  - e-current-auth
  - e-history
  - e-successor
  - e-final-preservation
  - e-readme-provenance
  - e-preparation-incidents
  details: This reviewer read all 1,750 maintained YAML lines and directly checked
    66 labels, 221 prior record bytes, 90 adopted archives and 17 cached-original
    copies. The current corpus has 222 records. Historical author ledger statements
    remain historical where successor evidence corrects ETF wording or DRAM shorthand.
    Append-only record and parser history correctly describe their creation-time pending
    gates. Broader source-to-graph, primary literature and 19 sequence coverage comes
    from /root/ethylmalonyl_independent_review; this reviewer authored only the independent
    successor assessment, current input reconciliation and this governed review. Source
    originals and broad article passages remain external. Final root/peer preservation
    additionally checks all 221 old pages and complete graph contexts. ADOPTION-README.md
    retains the exact historical adoption narrative while the final README records
    later completed gates.
  outcome: supported
  target_ids:
  - KEGG:M00373
- assessment_id: a-graph-integration
  area: graph
  outcome: supported
  topic: Complete graph rendering, source contexts and actual maintained gates
  summary: The rendered record faithfully exposes 65 incident nodes, 105 asserted
    edges and all 155 evidence items; all 326 checked in-page links resolve. Whole-corpus
    gates pass with no unresolved graph or identifier defect.
  target_ids:
  - KEGG:M00373
  evidence_ids:
  - e-target
  - e-generated-graph
  - e-final-geometry
  - e-integration-peer
  - e-final-gates
  - e-final-preservation
  - e-category-peer
  - e-old-pages
  - e-vendored
  details: The taxon is declared but has no asserted graph edge, explaining 65 SVG
    nodes versus 66 KGX contexts. The 105 edges comprise 14 membership, 50 chemical-side,
    13 flow, four assembly-component, ten catalysis, three enables, ten cofactor and
    one regulation assertion. Full export has 3,775 global nodes and 10,751 edges.
    Previous 10,646 edges, 3,745 contexts and 221 pages are preserved. Existing source-role
    unions explain shared-node category differences; all contextual directions match.
    RHEA:21037 and RHEA:45798 global names change to canonical equations through existing
    deterministic selection while prior contextual labels remain. Root ran all full
    gates; this reviewer inspected their actual receipts and verified original versus
    archived log hashes. The first preservation checker used an overstrict global-equals-target
    category assumption; its preserved failure and independently supported corrected
    checker do not indicate a product defect.
  dimensions:
  - name: graph-support
    value: 65 SVG nodes / 105 edges / 155 evidence items / 326 resolved in-page links
      / 66 KGX contexts
    definition: Exact assertion and evidence representation, separately checked from
      scientific support.
    evidence_ids:
    - e-generated-graph
    - e-final-geometry
  - name: validation-scope
    value: 222-record corpus; 1,378 tests passed; three empty command-frontmatter
      parametrization skips
    definition: Actual root full-corpus execution, not an invented focused validator
      or an independent rerun.
    evidence_ids:
    - e-final-gates
findings: []
actions: []
limitations:
- The broader full original scientific review is reused explicitly with byte-identical
  unchanged inputs; this reviewer newly checked the complete maintained YAML, current
  bindings, all 14 native directions and the two-paper correction, but does not claim
  a second full literature/protein-sequence audit.
- PMID:18819910 and PMID:19703103 full texts were unavailable; abstract metadata and
  reviewed database annotations retain their distinct evidence scope. Uninspected
  primary methods or supplements are not asserted verified.
- Exact PhaB and crotonase protein assignments remain unresolved; their chemical steps
  are present. Mcl2 oligomer ambiguity, inferred PCC/MCM assemblies, alternative assay
  metals, AM1 stereochemical wording and the native CPD9409 conflict remain explicit.
- The native 548-aa Mcd product, its 555-aa counterpart and purification tags are
  separate evidence scopes; no processing explanation or construct equivalence is
  inferred.
- Formal reaction balance and whole-ETF states do not prove physiological flux or
  microscopic two-ETF stoichiometry. PccR direct promoter binding and a propionyl-CoA
  ligand remain unestablished.
- Pinned source bodies and the earlier successful 20-organism iModulonDB inventory
  inform this review. No fresh whole-source discovery, database-exhaustion claim or
  new iModulonDB inventory is made; a nonmatching dataset is not negative biological
  evidence.
- Static SVG/KGX checks are programmatic; no browser interaction or whole-figure/supplement
  visual review is claimed. The full-corpus gate outcomes are attributed to the actual
  root execution, not falsely claimed as separately rerun here.
- External original findings have no governed review identities. Their verified fixes
  are recorded in evidence-linked assessments with exact issue keys and source hashes,
  without fabricated canonical previous_occurrences.
- The source replay performs bounded filesystem checks, not an atomic snapshot. Interpreter
  and every installed third-party dependency are not individually hashed.
- Public-release licensing remains deferred by the user. This scientific observation
  does not grant redistribution rights or itself authorize publication or native status
  promotion.
notes:
- Original external findings retain exact stable keys and preserved proof files. No
  governed predecessor exists for these target findings, so verified external corrections
  are assessments rather than fabricated terminal findings.
- Root full gates used UV_NO_SYNC=1, bytecode disabled and the existing 195 environment;
  no dependency synchronization was performed. Maintained gate logs are lossless JSON
  wrappers verified against original raw bytes.
- Reviewer preparation display/count assumptions and peer/root checker assumptions
  are preserved separately with their corrected actual outcomes; no product source
  was changed by this reviewer. A later read initially used the wrong directory for
  readme-provenance.json, then located the exact final-validation file with an ignored-aware
  inventory; this was a read-only path correction.
- This review is an immutable scoped observation and does not promote native status
  or grant source redistribution rights.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/416
- https://github.com/CultureBotAI/PathwayMech/issues/417
- https://github.com/CultureBotAI/PathwayMech/issues/418
tags:
- pathway
- ethylmalonyl
- independent
- scientific-review
```
