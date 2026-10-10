# Independent scientific review of citrate lyase activation

- Review: 20261010T231224Z-citrate-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-10T23:02:01Z
- Finished UTC: 2026-10-10T23:12:24Z
- Reviewer: Codex independent citrate scientific reviewer (/root/pathway_authority_cache) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded E. coli K-12 citrate lyase activation record is supported. All 22 edges,36 evidence blocks and14 Rhea side occurrences match the inspected sources; distinct whole carrier states and species-specific evidence boundaries are preserved. No corrective finding was identified. The main limitation is the explicitly curated CitC accession-to-old-primary bridge, with the original ligase paper available only as a truncated indexed abstract.

## Scope And Provenance

Independent scientific review of one maintained activation record, including every local node/edge/reference and native source exclusions.

Selection: Exact target MetaCyc:P2-PWY and data/pathways/citrate-lyase-activation.yaml assigned by integration agent.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 722257adc1882495f8454cc229b8fa0c187cf868.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:P2-PWY | data/pathways/citrate-lyase-activation.yaml | maintained | citrate lyase activation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Initial governed input capture | passed | False | MetaCyc:P2-PWY | Exit 0 before scientific assessment; captures final target and then-current shared inputs. |
| Initial reviewer scratch environment probe | failed | False | MetaCyc:P2-PWY | System Python lacked PyYAML and exited 1. Subsequent checks use repository .venv; no repository source changed. |
| Initial reviewer replay harness field mismatch | failed | False | MetaCyc:P2-PWY | First non-gating replay used snippet instead of the actual quote field and failed its expected-quote-count assertion after chemistry/hash checks. Corrected the scratch harness; target unchanged. |
| Independent exact source replay | passed | False | MetaCyc:P2-PWY | Final replay exits 0 with all 22 edges/36 evidence,14 chemical-side occurrences and 10 reference digests supported. |
| Independent complete Rhea extraction | passed | False | MetaCyc:P2-PWY | Exit 0; independently selected 45 native subjects from the complete official compressed RDF. The resulting projection equals the maintained source projection. |
| Working-tree whitespace check | passed | True | MetaCyc:P2-PWY | Reviewer execution exited 0 on the final frozen inputs. |
| Staged whitespace check | passed | True | MetaCyc:P2-PWY | Reviewer execution exited 0. Corpus validation separately checks the new untracked records and generated pages. |
| Ignored-inclusive prior occurrence search | passed | False | MetaCyc:P2-PWY | No prior exact occurrence; exit 1 is the expected no-match result. |
| Baseline authority and manifest preservation | passed | False | MetaCyc:P2-PWY | All baseline values retained; exact target names and four new manifest bodies verified. |
| Integrated validate | passed | True | MetaCyc:P2-PWY | 167 native and closed-schema records,8731 evidence blocks,248 history records, identifiers,30 sources,6 documentation files,research contract and current pages pass. |
| Integrated test | passed | True | MetaCyc:P2-PWY | 1043 passed,3 skipped,3 upstream warnings in351.55 seconds; actual process exit0. |
| Integrated lint | passed | True | MetaCyc:P2-PWY | All Ruff checks passed; exit0. |
| Integrated render | passed | True | MetaCyc:P2-PWY | Rendered167 pathway records; exit0. |
| Integrated vendored | passed | True | MetaCyc:P2-PWY | 22 governed artifacts match; exit0. |
| Independent publication audit | passed | False | MetaCyc:P2-PWY | Actual independent graph audit and separate CLI export exit0. Citrate retains18 named nodes,22edges,36evidence and17drawn SVG nodes; valid links,endpoints,geometry and exact carrier categories/contexts. |
| Canonical iModulonDB datasets | passed | True | MetaCyc:P2-PWY | Delegated exit 0; exact output and digest independently inspected. |
| Canonical iModulonDB citG | passed | True | MetaCyc:P2-PWY | Delegated exit 0; exact output and digest independently inspected. |
| Canonical iModulonDB citX | passed | True | MetaCyc:P2-PWY | Delegated exit 0; exact output and digest independently inspected. |
| Canonical iModulonDB citC | passed | True | MetaCyc:P2-PWY | Delegated exit 0; exact output and digest independently inspected. |
| iModulon component summarize | not_applicable | False | MetaCyc:P2-PWY | No component returned by the three exact-locus searches; no relevant summarize call applies. |

## Scientific And Domain Assessments

### Exact activation pathway and endpoint

identity: supported. Targets: MetaCyc:P2-PWY.

MetaCyc:P2-PWY denotes citrate lyase activation. The record limits its E. coli K-12 molecular core to precursor synthesis, prosthetic-group transfer and acetylation; it does not substitute citrate cleavage or a whole fermentation route.

### All 14 substrate/product edges and exact stoichiometry

grounding: supported. Targets: MetaCyc:P2-PWY.

Edges 001-014 preserve all exact Rhea chemical forms and coefficients. Complete balanced chemistry includes adenine, AMP and diphosphate and does not copy charge-incompatible proton edges from the older native map. Each native side URI, Participant object and contains1 assertion is valid.

### Whole apo, holo and acetyl carrier states

representation: supported. Targets: MetaCyc:P2-PWY.

RHEA-COMP:10157/10158/13710 identify distinct generic polypeptide states. Protein categories are correct. Reactive-part ChEBI terms support the stoichiometric accounting but do not replace the complete carrier or imply a single accession-specific sequence.

### CitG/CitX catalytic edges 015-016

evidence: supported. Targets: MetaCyc:P2-PWY.

Exact reviewed K-12 proteins and scoped primary experiments support the first two reactions. The CitG precursor and CitX transfer claims are distinct. The experimental AMP-ACP side product is appropriately excluded from the physiological activation route.

### CitC catalytic edge 017 and accession evidence tier

evidence: supported. Targets: MetaCyc:P2-PWY.

The selected chemistry is supported by reviewed P77390/Rhea assignment and historical E. coli acetylating ligase observation, linked through explicit EcoCyc IDA GO 0008771 annotation. The record honestly distinguishes this curated bridge from an independently verified sequence-specific purification. Klebsiella P45410 is not substituted for E. coli CitC.

### Native membership edges 018-020 and handoffs 021-022

graph: supported. Targets: MetaCyc:P2-PWY.

The three exact Rhea directional objects each carry the relevant native MetaCyc seeAlso bridge. The precursor and holo carrier are identical output/input entities across their adjacent reactions. The two handoff edges claim neither a stable maturation complex nor substrate channeling.

### Native source conflicts and omitted components

scope: supported. Targets: MetaCyc:P2-PWY.

Native alternative acetyl donor and deacetylase branches have different-organism evidence; the PathBank ATP-independent condensation is not silently treated as E. coli activation. Unsupported free-metal/compartment/assembly claims are omitted. Downstream cleavage-complex stoichiometry and the corrected old ACP mass are outside the retained mechanism.

### Limits of available primary ligase evidence

completeness: unknown. Targets: MetaCyc:P2-PWY.

The full 1983 ligase paper was not inspected, and its indexed abstract is truncated. The review cannot independently resolve the exact historical enzyme sequence or its complete purification/assay details. This is an explicitly retained limitation, not a hidden claim of direct modern-accession experimentation.

### Source hashes, shared integration and bounded context

provenance: supported. Targets: MetaCyc:P2-PWY.

All 10 target reference digests match exact preserved bodies. Rhea 139 identity authority, Rhea 142 mechanism/components, reviewed UniProt 2026_03 and public MetaCyc 22.5 are distinguished. Baseline source values are retained, and contextual expression queries are not used as catalytic proof.

### Publication and repository consistency

graph: supported. Targets: MetaCyc:P2-PWY.

Actual source graph, final publication audit and required corpus gates preserve the assessed nodes, edges, full evidence and references. These technical checks support representation integrity and do not replace the scientific assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/citrate-lyase-activation.yaml; Entire final YAML; all 18 named nodes, 22 edges, 36 evidence blocks and 10 references | supports | The exact final target was captured by governed inspect before assessment and independently reread at the end. Every local endpoint, source assertion, quotation, taxon and pathway boundary was assessed. |
| e-native | https://pathway.yeastgenome.org/getxml?META:P2-PWY; Full Pathway P2-PWY common-name, reaction-list, reaction-layout, species and comment; exact reaction XML 2.7.8.25-RXN, 2.7.7.61-RXN and CITC-RXN | supports | The exact native identity is citrate lyase activation. Its three selected reactions form precursor synthesis, prosthetic-group transfer and ATP-dependent acetylation. The broader native multi-organism map also contains an alternate donor route and a deacetylase; those are not automatically E. coli pathway claims. Public MetaCyc 22.5 is identified explicitly. |
| e-native-proteins | https://pathway.yeastgenome.org/getxml?META:G6339-MONOMER; G6339-MONOMER and G6340-MONOMER species/UniProt/catalyzes; MONOMER-17001, MONOMER-6581 and CPLX-7662 species and comment | supports | CitG/CitX native objects map exactly to P77231/P0A6G5 with MG1655 provenance. MONOMER-17001 maps to Klebsiella P45410 and is correctly excluded as the E. coli CitC identity. Alternative acetyltransferase MONOMER-6581 is K. aerogenes and deacetylase CPLX-7662 is Rubrivivax. Neither supplies an E. coli catalytic edge. |
| e-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Full official Rhea 142 RDF: masters 15117/16333/23788, directions 15118/16334/23789, exact substrates/products/contains1/Participant/compound/seeAlso objects and reactive parts | supports | Independent complete-RDF extraction selected 45 native subjects. All 14 chemical-side occurrences and coefficients agree with the target and exact source locators. The three equations balance by atoms and charge when the unchanged generic carrier backbone cancels. Generic polypeptide states 10157, 10158 and 13710 are distinct whole protein states; their reactive-part ChEBI terms are not substituted for the whole carriers. |
| e-proteins | https://rest.uniprot.org/uniprotkb/P77231.json; Reviewed 2026_03 JSON P77231, P0A6G5, P77390; accession/taxon, comments[1].reaction, cross-references, evidence codes and GO annotation | supports | The exact reviewed K-12 proteins map to the three Rhea masters and native whole carrier cross-references. CitG/CitX catalytic assignments carry experimental citation evidence; P77390 catalytic comment has no inline experimental ECO annotation. The record preserves that distinction rather than silently promoting database curation to an accession-specific purification experiment. |
| e-primary-citg-citx | https://juser.fz-juelich.de/record/26938/files/19821.pdf; PMID 10924139 original institutional PDF, abstract, methods pp9439-9442 and Results/Discussion pp9442-9447; inspected via web PDF parser; no PDF body digest claimed | supports | Purified-component experiments support CitG/CitX-dependent apo-to-holo conversion using ATP and dephospho-CoA. The AMP-modified side product did not become holo carrier upon subsequent CitG/dephospho-CoA treatment. Expression hosts and E. coli versus Klebsiella constructs were distinguished. The precursor structure was proposed in this study and established in the follow-up abstract; no assembly stoichiometry or obligatory bound metal is inferred from assay conditions. |
| e-primary-precursor | https://pubmed.ncbi.nlm.nih.gov/11042274/; Full indexed abstract, DOI 10.1016/S0014-5793(00)02105-0; ten-word quotation on edge016; snapshot digest covers preserved Europe PMC core JSON, not PubMed HTML | supports | The primary abstract reports precursor identification, adenine release in CitG chemistry and subsequent CitX transfer to apo carrier. The retained quotation is literal and short. Only the abstract was inspected for this paper; its full methods or figures are not claimed. |
| e-primary-citc | https://pubmed.ncbi.nlm.nih.gov/6354265/; Indexed 1983 E. coli primary abstract, DOI10.1021/bi00289a008, final ligase sentence; fourteen-word quotation on edge 017 | supports | The abstract reports a ligase that acetylates deacetylated citrate lyase with acetate and ATP. It does not independently identify the modern P77390 sequence. Its old ACP mass and subunit-ratio statements are not propagated. The indexed abstract is truncated at 250 words; the full article was unavailable to this review. |
| e-citc-bridge | https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:P77390; P77390 reviewed GO:0008771 IDA:EcoCyc with ECO:0000314/PMID 6354265; QuickGO row UniProtKB:P77390!237979601 | supports | The exact accession-specific EcoCyc IDA assignment supplies the curated connection between the historical E. coli ligase observation and P77390. This is an explicit database-to-primary bridge, not new primary sequence proof. Other IBA/IEA rows were distinguished from the IDA row. |
| e-old-assembly | https://pubmed.ncbi.nlm.nih.gov/3555623/; Complete indexed 1987 correction abstract; DOI 10.1016/0167-4838(87)90232-9; snapshot digest covers preserved Europe PMC core JSON, not PubMed HTML | context_only | The later study identifies the earlier high-mass ACP assignment as contamination and gives different citrate-cleavage complex subunit properties. The activation record correctly avoids copying either downstream cleavage-complex stoichiometry into its maturation-enzyme graph. |
| e-pathbank | https://pathbank.org/pathways/SMP0002087; Native archive member PW002075.owl: reactions6060-6064 and generic apo/holo/acetyl carrier object classes | context_only | The native apo carrier is typed SmallMolecule while the holo/acetyl carriers are Protein. Reaction 6062 is ATP-independent condensation in the reverse sense of a deacetylase branch, and 6064 uses another acetyl donor. These source facts were inspected but not imported as E. coli assertions; the target uses independent Rhea protein identities and supported ATP-dependent activation. |
| e-replay | /private/tmp/pathwaymech-citrate-review/source-replay.json; Reviewer replay.py and independent Rhea extraction, raw reference digests, native crosswalks and bounded context outputs | supports | Focused replay passes on the frozen target: 18 local nodes, 22 edges, 36 evidence blocks, all 14 chemical sides and source locators, three balanced equations, 10 reference body digests and two literal quotations. Native/protein identity and seven preserved adapter-output digests also agree. |
| e-authorities | research/pathway_additions/2026-10-10-citrate-sbm/authority-integration.json; Final ontology/source snapshots compared with base 722257a JSON values; manifest entries and four new native HTML bodies rehashed | supports | Every one of 1305 baseline ontology terms, 1609 source terms and their source metadata remains unchanged. Final totals are 1319/1622; manifest 106 grows to 110. Exact target labels are present. Rhea 139 identity authority is distinct from explicitly versioned Rhea 142 mechanistic RDF and component identity. No identifier exemption or handpatched source authority is introduced. |
| e-context | research/pathway_additions/2026-10-10-citrate-sbm/imodulondb-context.json; Canonical datasets and e_coli/precise_mg1655 exact-locus searches b0613, b0614, b0618; actual Markdown outputs inspected | context_only | The three queries return citG, citX and citC respectively, each one gene and zero module hits. No returned component requires summarize. These bounded query results support transcriptomic context only, not catalysis, pathway flux or absence from all expression modules. |
| e-generated | research/pathway_additions/2026-10-10-citrate-sbm/generated-graph-kgx-audit.json; Independent final actual CLI KGX, published download bytes, citrate SVG endpoints and evidence anchors | supports | The delegated publication audit checks complete graph/evidence preservation, exact carrier categories and target context, valid endpoints and links, and equality with separately generated CLI output. Programmatic structural checks are not a browser visual inspection. |
| e-gates | /private/tmp/pathwaymech-citrate-sbm-{validate,test,lint,render,vendored}.log; Actual root-executed final gate logs and process exit receipts | supports | The reviewer inspected delegated frozen-input corpus checks and actual final exit receipts. Deterministic consistency is separate from the independent scientific assessment. |
| e-prior | reviews/ and reports/; rg -n -uu 'MetaCyc:P2-PWY&#124;citrate-lyase-activation&#124;citrate lyase activation' reviews reports | supports | No previous exact target review/report occurrence was returned before this bundle. Hidden and ignored files were included; this is a bounded repository review search, not exhaustive literature discovery. |

## Limits And Additional Notes

- PMID 6354265 was inspected only as its indexed 250-word truncated abstract; no full article or modern-accession-specific purification was verified. The P77390 assignment relies on explicit reviewed/EcoCyc IDA curation, which the record discloses.
- PMID 11042274 and the 1987 cleavage-complex correction were inspected as full indexed abstracts, not full articles. Relevant original Schneider 2000 PDF text was independently read; figure pixels and supplements were not inspected.
- Generic Rhea carrier states preserve complete-protein identity classes and modification states, not exact sequences or assembly stoichiometry. Reactive-part balance assumes the same unchanged polypeptide backbone cancels.
- The public MetaCyc mechanism snapshot is 22.5; the review makes no claim about the latest licensed release. Rhea 139 identity authority is distinct from 142 mechanistic evidence.
- The record supports a bounded maturation mechanism, not an assertion that every K-12 strain expresses the pathway or supports a particular citrate-fermentation flux under arbitrary conditions.
- iModulonDB exact-locus hits are context only; zero returned module hits is not negative evidence for expression, regulation or catalysis.
- Programmatic SVG/KGX audit does not replace browser visual review. No browser inspection is claimed.
- The target remained at c76b50f65ef43e599ca16a9789144840660b52a4dc1d9adcd46fb8c5fecdd450 from initial governed inspect through final save. Shared authority inputs changed during integration and were explicitly compared against baseline values, checked against exact sources and re-inspected before saving.
- Two non-required scratch execution failures are retained honestly: system-Python missing PyYAML and reviewer quote-field mismatch. Both were superseded with repository-environment checks; no target/source correction resulted. All required final gates passed.
- The ignored-inclusive prior review/report search found no exact target occurrence in the bounded directories. Empty findings does not retire unrelated prior issues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T231224Z-citrate-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of citrate lyase activation
started_at: '2026-10-10T23:02:01Z'
finished_at: '2026-10-10T23:12:24Z'
reviewer:
  identity: Codex independent citrate scientific reviewer (/root/pathway_authority_cache)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: A different agent authored the citrate target and its mechanistic
    research. This reviewer did not edit those files and independently inspected all
    target content, native objects, raw primary evidence and exact Rhea chemistry.
    This reviewer authored the separate allantoin research handoff in this batch and
    previously merged supporting PathBank authority-parser/policy work; independence
    is claimed for this target scientific assessment, not that implementation.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded E. coli K-12 citrate lyase activation record is supported. All
  22 edges,36 evidence blocks and14 Rhea side occurrences match the inspected sources;
  distinct whole carrier states and species-specific evidence boundaries are preserved.
  No corrective finding was identified. The main limitation is the explicitly curated
  CitC accession-to-old-primary bridge, with the original ligase paper available only
  as a truncated indexed abstract.
source:
  git_revision: 722257adc1882495f8454cc229b8fa0c187cf868
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: d1d18735600fe87f44822cfbc2448c82c10764fec2d45a9780a52c694a892d63
    role: context
  - path: conf/identifier_sources.json
    sha256: 33192380665155203ef45ef7d6a143078dc030bbfd281754f383d602107175d5
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 1d4a27d8e22ebe51808d4b0e180f57818e0693263c9eaa768019693bf35c596a
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 12ef38773f0fe35a8df5a923775efeea6130f092c785cda45f0dfd30bfc90ae2
    role: context
  - path: data/pathways/citrate-lyase-activation.yaml
    sha256: c76b50f65ef43e599ca16a9789144840660b52a4dc1d9adcd46fb8c5fecdd450
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 3c861f2ab78e3bc62146d05af5ed5c4c4ae3e65343fc9bd44afa76da7f0b62e7
    role: context
  - path: pages/records/MetaCyc_P2-PWY.html
    sha256: 2e04c2be614199de4ba15bb588ca90a76d8a5be0903a1bc095c2519011a1907d
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/authority-integration.json
    sha256: 46371b13cc93b314b41f59583370ec4dea718b23fb98c16fc521bcb7ad5e764c
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/citrate-curation.md
    sha256: 12e3104abb0284cdc21434ccea49925e2eab6a63caf1cb872ae12e56d08db273
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/citrate-source-manifest.json
    sha256: d174a5c2730339398519797bb579d63058a544e2b8a11f281014a458f4e168c5
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/citrate-source-projection.json
    sha256: c29987a97de30a7f0061d3c9428c19806d03a90799443a1d0a3eb45c41322f08
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/citrate-validation.json
    sha256: 59af3fc79ff02eb946fd40bb481d006a051fbb3e43bf9cc21798ac013cacd576
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/generated-graph-kgx-audit.json
    sha256: 7dd446cd0b98282d0986c31661f6d217d824fbf036af1cc903406bb44e507dfd
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/imodulondb-context.json
    sha256: e49c7b0a498e9af1cda54a961bc37989e3a034f922043f44e21a73300957040f
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: Independent scientific review of one maintained activation record,
    including every local node/edge/reference and native source exclusions.
  selection: Exact target MetaCyc:P2-PWY and data/pathways/citrate-lyase-activation.yaml
    assigned by integration agent.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:P2-PWY
  exclusions:
  - target: data/pathways/succinate-to-propanoate.yaml and all other pathway records
    reason: Separate scientific reviews; corpus gates are technical checks, not fresh
      scientific assessment of every record.
  - target: Allantoin research handoff and all uninspected literature
    reason: Not part of this record verdict; no exhaustive literature-absence claim.
targets:
- target_id: MetaCyc:P2-PWY
  path: data/pathways/citrate-lyase-activation.yaml
  label: citrate lyase activation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/citrate-lyase-activation.yaml
    role: maintained_curation
checks:
- check_id: c-inspect
  name: Initial governed input capture
  status: passed
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: Exit 0 before scientific assessment; captures final target and then-current
    shared inputs.
  evidence_ids:
  - e-record
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-citrate-review/targets.yaml
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
    --input docs/CAUSAL_GRAPHS.md --input conf/identifier_policy.yaml --input conf/identifier_sources.json
    --input data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
  exit_code: 0
  expected_exit_code: 0
- check_id: c-system-python
  name: Initial reviewer scratch environment probe
  status: failed
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: System Python lacked PyYAML and exited 1. Subsequent checks use repository
    .venv; no repository source changed.
  evidence_ids:
  - e-replay
  command: python3 - <<PY (reviewer read-only JSON/YAML inspection) PY
  exit_code: 1
  expected_exit_code: 0
- check_id: c-replay-attempt
  name: Initial reviewer replay harness field mismatch
  status: failed
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: First non-gating replay used snippet instead of the actual quote field
    and failed its expected-quote-count assertion after chemistry/hash checks. Corrected
    the scratch harness; target unchanged.
  evidence_ids:
  - e-replay
  command: .venv/bin/python /private/tmp/pathwaymech-citrate-review/replay.py
  exit_code: 1
  expected_exit_code: 0
- check_id: c-replay
  name: Independent exact source replay
  status: passed
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: Final replay exits 0 with all 22 edges/36 evidence,14 chemical-side occurrences
    and 10 reference digests supported.
  evidence_ids:
  - e-replay
  - e-rhea
  command: .venv/bin/python /private/tmp/pathwaymech-citrate-review/replay.py
  exit_code: 0
  expected_exit_code: 0
- check_id: c-full-rdf
  name: Independent complete Rhea extraction
  status: passed
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: Exit 0; independently selected 45 native subjects from the complete official
    compressed RDF. The resulting projection equals the maintained source projection.
  evidence_ids:
  - e-rhea
  - e-replay
  command: python3 /private/tmp/pathwaymech-citrate-review/extract-rhea.py
  exit_code: 0
  expected_exit_code: 0
- check_id: c-diff
  name: Working-tree whitespace check
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: Reviewer execution exited 0 on the final frozen inputs.
  evidence_ids:
  - e-record
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
- check_id: c-staged-diff
  name: Staged whitespace check
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: Reviewer execution exited 0. Corpus validation separately checks the new
    untracked records and generated pages.
  evidence_ids:
  - e-record
  command: git diff --cached --check
  exit_code: 0
  expected_exit_code: 0
- check_id: c-prior
  name: Ignored-inclusive prior occurrence search
  status: passed
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: No prior exact occurrence; exit 1 is the expected no-match result.
  evidence_ids:
  - e-prior
  command: rg -n -uu 'MetaCyc:P2-PWY|citrate-lyase-activation|citrate lyase activation'
    reviews reports
  exit_code: 1
  expected_exit_code: 1
- check_id: c-authority
  name: Baseline authority and manifest preservation
  status: passed
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: All baseline values retained; exact target names and four new manifest
    bodies verified.
  evidence_ids:
  - e-authorities
  command: Reviewer Python comparison of git show 722257a snapshots/manifest with
    final JSON; SHA256 of new native HTML bodies
  exit_code: 0
  expected_exit_code: 0
- check_id: c-validate
  name: Integrated validate
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: 167 native and closed-schema records,8731 evidence blocks,248 history records,
    identifiers,30 sources,6 documentation files,research contract and current pages
    pass.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual logs and final exit receipts rather than duplicating heavy corpus
    gates.
- check_id: c-test
  name: Integrated test
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: 1043 passed,3 skipped,3 upstream warnings in351.55 seconds; actual process
    exit0.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual logs and final exit receipts rather than duplicating heavy corpus
    gates.
- check_id: c-lint
  name: Integrated lint
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: All Ruff checks passed; exit0.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual logs and final exit receipts rather than duplicating heavy corpus
    gates.
- check_id: c-render
  name: Integrated render
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: Rendered167 pathway records; exit0.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual logs and final exit receipts rather than duplicating heavy corpus
    gates.
- check_id: c-vendored
  name: Integrated vendored
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: 22 governed artifacts match; exit0.
  evidence_ids:
  - e-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual logs and final exit receipts rather than duplicating heavy corpus
    gates.
- check_id: c-generated
  name: Independent publication audit
  status: passed
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: Actual independent graph audit and separate CLI export exit0. Citrate retains18
    named nodes,22edges,36evidence and17drawn SVG nodes; valid links,endpoints,geometry
    and exact carrier categories/contexts.
  evidence_ids:
  - e-generated
  command: .venv/bin/python /private/tmp/pathwaymech-citrate-sbm-graph-audit.py --root
    /private/tmp/pathwaymech-citrate-sbm-20261010 --comparison-kgx-dir /private/tmp/pathwaymech-citrate-sbm-kgx
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by the independent publication audit agent; reviewer inspected
    final preserved receipt.
- check_id: c-context-datasets
  name: Canonical iModulonDB datasets
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: Delegated exit 0; exact output and digest independently inspected.
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-citG
  name: Canonical iModulonDB citG
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: Delegated exit 0; exact output and digest independently inspected.
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise_mg1655 --query b0613
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-citX
  name: Canonical iModulonDB citX
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: Delegated exit 0; exact output and digest independently inspected.
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise_mg1655 --query b0614
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-citC
  name: Canonical iModulonDB citC
  status: passed
  required: true
  target_ids:
  - MetaCyc:P2-PWY
  summary: Delegated exit 0; exact output and digest independently inspected.
  evidence_ids:
  - e-context
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise_mg1655 --query b0618
  exit_code: 0
  expected_exit_code: 0
- check_id: c-context-summary
  name: iModulon component summarize
  status: not_applicable
  required: false
  target_ids:
  - MetaCyc:P2-PWY
  summary: No component returned by the three exact-locus searches; no relevant summarize
    call applies.
  evidence_ids:
  - e-context
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/citrate-lyase-activation.yaml
  locator: Entire final YAML; all 18 named nodes, 22 edges, 36 evidence blocks and
    10 references
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: The exact final target was captured by governed inspect before assessment
    and independently reread at the end. Every local endpoint, source assertion, quotation,
    taxon and pathway boundary was assessed.
  snapshot_sha256: c76b50f65ef43e599ca16a9789144840660b52a4dc1d9adcd46fb8c5fecdd450
- evidence_id: e-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:P2-PWY
  locator: Full Pathway P2-PWY common-name, reaction-list, reaction-layout, species
    and comment; exact reaction XML 2.7.8.25-RXN, 2.7.7.61-RXN and CITC-RXN
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: The exact native identity is citrate lyase activation. Its three selected
    reactions form precursor synthesis, prosthetic-group transfer and ATP-dependent
    acetylation. The broader native multi-organism map also contains an alternate
    donor route and a deacetylase; those are not automatically E. coli pathway claims.
    Public MetaCyc 22.5 is identified explicitly.
  snapshot_sha256: 8e12d1a7b0351c9cb1713d5000431f2f66d4ac35f1162ee1a412d72e4ec86f21
- evidence_id: e-native-proteins
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:G6339-MONOMER
  locator: G6339-MONOMER and G6340-MONOMER species/UniProt/catalyzes; MONOMER-17001,
    MONOMER-6581 and CPLX-7662 species and comment
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: CitG/CitX native objects map exactly to P77231/P0A6G5 with MG1655 provenance.
    MONOMER-17001 maps to Klebsiella P45410 and is correctly excluded as the E. coli
    CitC identity. Alternative acetyltransferase MONOMER-6581 is K. aerogenes and
    deacetylase CPLX-7662 is Rubrivivax. Neither supplies an E. coli catalytic edge.
- evidence_id: e-rhea
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: 'Full official Rhea 142 RDF: masters 15117/16333/23788, directions 15118/16334/23789,
    exact substrates/products/contains1/Participant/compound/seeAlso objects and reactive
    parts'
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: Independent complete-RDF extraction selected 45 native subjects. All 14
    chemical-side occurrences and coefficients agree with the target and exact source
    locators. The three equations balance by atoms and charge when the unchanged generic
    carrier backbone cancels. Generic polypeptide states 10157, 10158 and 13710 are
    distinct whole protein states; their reactive-part ChEBI terms are not substituted
    for the whole carriers.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P77231.json
  locator: Reviewed 2026_03 JSON P77231, P0A6G5, P77390; accession/taxon, comments[1].reaction,
    cross-references, evidence codes and GO annotation
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: The exact reviewed K-12 proteins map to the three Rhea masters and native
    whole carrier cross-references. CitG/CitX catalytic assignments carry experimental
    citation evidence; P77390 catalytic comment has no inline experimental ECO annotation.
    The record preserves that distinction rather than silently promoting database
    curation to an accession-specific purification experiment.
- evidence_id: e-primary-citg-citx
  kind: primary_source
  reference: https://juser.fz-juelich.de/record/26938/files/19821.pdf
  locator: PMID 10924139 original institutional PDF, abstract, methods pp9439-9442
    and Results/Discussion pp9442-9447; inspected via web PDF parser; no PDF body
    digest claimed
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: Purified-component experiments support CitG/CitX-dependent apo-to-holo
    conversion using ATP and dephospho-CoA. The AMP-modified side product did not
    become holo carrier upon subsequent CitG/dephospho-CoA treatment. Expression hosts
    and E. coli versus Klebsiella constructs were distinguished. The precursor structure
    was proposed in this study and established in the follow-up abstract; no assembly
    stoichiometry or obligatory bound metal is inferred from assay conditions.
- evidence_id: e-primary-precursor
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11042274/
  locator: Full indexed abstract, DOI 10.1016/S0014-5793(00)02105-0; ten-word quotation
    on edge016; snapshot digest covers preserved Europe PMC core JSON, not PubMed
    HTML
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: The primary abstract reports precursor identification, adenine release
    in CitG chemistry and subsequent CitX transfer to apo carrier. The retained quotation
    is literal and short. Only the abstract was inspected for this paper; its full
    methods or figures are not claimed.
  snapshot_sha256: ae1fe40a496c1fb91f4a30112b75ebb330dbce81a6e32f3facaacd236c8112e2
- evidence_id: e-primary-citc
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/6354265/
  locator: Indexed 1983 E. coli primary abstract, DOI10.1021/bi00289a008, final ligase
    sentence; fourteen-word quotation on edge 017
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: The abstract reports a ligase that acetylates deacetylated citrate lyase
    with acetate and ATP. It does not independently identify the modern P77390 sequence.
    Its old ACP mass and subunit-ratio statements are not propagated. The indexed
    abstract is truncated at 250 words; the full article was unavailable to this review.
  snapshot_sha256: ae2214c67694c78febd8336927e60dd9bef00fb862f1546481bb0f7cc7593552
- evidence_id: e-citc-bridge
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:P77390
  locator: P77390 reviewed GO:0008771 IDA:EcoCyc with ECO:0000314/PMID 6354265; QuickGO
    row UniProtKB:P77390!237979601
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: The exact accession-specific EcoCyc IDA assignment supplies the curated
    connection between the historical E. coli ligase observation and P77390. This
    is an explicit database-to-primary bridge, not new primary sequence proof. Other
    IBA/IEA rows were distinguished from the IDA row.
  snapshot_sha256: ce5448cb0c60486e719082f6f6dad67c63b16dfbac1ea3b4cb10e850b9862a81
- evidence_id: e-old-assembly
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/3555623/
  locator: Complete indexed 1987 correction abstract; DOI 10.1016/0167-4838(87)90232-9;
    snapshot digest covers preserved Europe PMC core JSON, not PubMed HTML
  accessed_at: '2026-10-10T23:12:24Z'
  support: context_only
  summary: The later study identifies the earlier high-mass ACP assignment as contamination
    and gives different citrate-cleavage complex subunit properties. The activation
    record correctly avoids copying either downstream cleavage-complex stoichiometry
    into its maturation-enzyme graph.
  snapshot_sha256: 1d2b506fee9f32ceb5ad0c0bc9f22c3a1e2736d7ea6d1ca71e41cbc2783c6da4
- evidence_id: e-pathbank
  kind: database
  reference: https://pathbank.org/pathways/SMP0002087
  locator: 'Native archive member PW002075.owl: reactions6060-6064 and generic apo/holo/acetyl
    carrier object classes'
  accessed_at: '2026-10-10T23:12:24Z'
  support: context_only
  summary: The native apo carrier is typed SmallMolecule while the holo/acetyl carriers
    are Protein. Reaction 6062 is ATP-independent condensation in the reverse sense
    of a deacetylase branch, and 6064 uses another acetyl donor. These source facts
    were inspected but not imported as E. coli assertions; the target uses independent
    Rhea protein identities and supported ATP-dependent activation.
  snapshot_sha256: 7af41798f5e0c499aa5a9a917a82c193ccf5f31b17051022a0488016e84bce61
- evidence_id: e-replay
  kind: validation
  reference: /private/tmp/pathwaymech-citrate-review/source-replay.json
  locator: Reviewer replay.py and independent Rhea extraction, raw reference digests,
    native crosswalks and bounded context outputs
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: 'Focused replay passes on the frozen target: 18 local nodes, 22 edges,
    36 evidence blocks, all 14 chemical sides and source locators, three balanced
    equations, 10 reference body digests and two literal quotations. Native/protein
    identity and seven preserved adapter-output digests also agree.'
  snapshot_sha256: b546ebfdfca93cdc2819461413b3efbf6d54cebd1f62d5e14c7053c40fcbf086
- evidence_id: e-authorities
  kind: authority
  reference: research/pathway_additions/2026-10-10-citrate-sbm/authority-integration.json
  locator: Final ontology/source snapshots compared with base 722257a JSON values;
    manifest entries and four new native HTML bodies rehashed
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: Every one of 1305 baseline ontology terms, 1609 source terms and their
    source metadata remains unchanged. Final totals are 1319/1622; manifest 106 grows
    to 110. Exact target labels are present. Rhea 139 identity authority is distinct
    from explicitly versioned Rhea 142 mechanistic RDF and component identity. No
    identifier exemption or handpatched source authority is introduced.
  snapshot_sha256: 46371b13cc93b314b41f59583370ec4dea718b23fb98c16fc521bcb7ad5e764c
- evidence_id: e-context
  kind: database
  reference: research/pathway_additions/2026-10-10-citrate-sbm/imodulondb-context.json
  locator: Canonical datasets and e_coli/precise_mg1655 exact-locus searches b0613,
    b0614, b0618; actual Markdown outputs inspected
  accessed_at: '2026-10-10T23:12:24Z'
  support: context_only
  summary: The three queries return citG, citX and citC respectively, each one gene
    and zero module hits. No returned component requires summarize. These bounded
    query results support transcriptomic context only, not catalysis, pathway flux
    or absence from all expression modules.
  snapshot_sha256: e49c7b0a498e9af1cda54a961bc37989e3a034f922043f44e21a73300957040f
- evidence_id: e-generated
  kind: validation
  reference: research/pathway_additions/2026-10-10-citrate-sbm/generated-graph-kgx-audit.json
  locator: Independent final actual CLI KGX, published download bytes, citrate SVG
    endpoints and evidence anchors
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: The delegated publication audit checks complete graph/evidence preservation,
    exact carrier categories and target context, valid endpoints and links, and equality
    with separately generated CLI output. Programmatic structural checks are not a
    browser visual inspection.
  snapshot_sha256: 7dd446cd0b98282d0986c31661f6d217d824fbf036af1cc903406bb44e507dfd
- evidence_id: e-gates
  kind: validation
  reference: /private/tmp/pathwaymech-citrate-sbm-{validate,test,lint,render,vendored}.log
  locator: Actual root-executed final gate logs and process exit receipts
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: The reviewer inspected delegated frozen-input corpus checks and actual
    final exit receipts. Deterministic consistency is separate from the independent
    scientific assessment.
- evidence_id: e-prior
  kind: search
  reference: reviews/ and reports/
  locator: rg -n -uu 'MetaCyc:P2-PWY|citrate-lyase-activation|citrate lyase activation'
    reviews reports
  accessed_at: '2026-10-10T23:12:24Z'
  support: supports
  summary: No previous exact target review/report occurrence was returned before this
    bundle. Hidden and ignored files were included; this is a bounded repository review
    search, not exhaustive literature discovery.
  search_scope: All reviews/ and reports/ in the active worktree, including hidden
    and ignored files.
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact activation pathway and endpoint
  outcome: supported
  summary: MetaCyc:P2-PWY denotes citrate lyase activation. The record limits its
    E. coli K-12 molecular core to precursor synthesis, prosthetic-group transfer
    and acetylation; it does not substitute citrate cleavage or a whole fermentation
    route.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-record
  - e-native
  - e-proteins
  dimensions:
  - name: taxon
    value: NCBITaxon:83333 Escherichia coli K-12
    definition: Reviewed protein provenance. Native CitG/CitX object strain and primary
      experimental expression hosts remain distinguished; no all-strains activity
      claim.
    evidence_ids:
    - e-native-proteins
    - e-proteins
    - e-primary-citg-citx
- assessment_id: a-sides
  area: grounding
  topic: All 14 substrate/product edges and exact stoichiometry
  outcome: supported
  summary: Edges 001-014 preserve all exact Rhea chemical forms and coefficients.
    Complete balanced chemistry includes adenine, AMP and diphosphate and does not
    copy charge-incompatible proton edges from the older native map. Each native side
    URI, Participant object and contains1 assertion is valid.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-rhea
  - e-replay
  - e-authorities
- assessment_id: a-carriers
  area: representation
  topic: Whole apo, holo and acetyl carrier states
  outcome: supported
  summary: RHEA-COMP:10157/10158/13710 identify distinct generic polypeptide states.
    Protein categories are correct. Reactive-part ChEBI terms support the stoichiometric
    accounting but do not replace the complete carrier or imply a single accession-specific
    sequence.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-rhea
  - e-proteins
  - e-record
  - e-generated
- assessment_id: a-citg-citx
  area: evidence
  topic: CitG/CitX catalytic edges 015-016
  outcome: supported
  summary: Exact reviewed K-12 proteins and scoped primary experiments support the
    first two reactions. The CitG precursor and CitX transfer claims are distinct.
    The experimental AMP-ACP side product is appropriately excluded from the physiological
    activation route.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-proteins
  - e-primary-citg-citx
  - e-primary-precursor
  - e-native-proteins
- assessment_id: a-citc
  area: evidence
  topic: CitC catalytic edge 017 and accession evidence tier
  outcome: supported
  summary: The selected chemistry is supported by reviewed P77390/Rhea assignment
    and historical E. coli acetylating ligase observation, linked through explicit
    EcoCyc IDA GO 0008771 annotation. The record honestly distinguishes this curated
    bridge from an independently verified sequence-specific purification. Klebsiella
    P45410 is not substituted for E. coli CitC.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-primary-citc
  - e-citc-bridge
  - e-proteins
  - e-native-proteins
  dimensions:
  - name: evidence_tier
    value: Explicit reviewed accession assignment plus EcoCyc IDA primary-literature
      bridge
    definition: The old primary abstract supports ligase activity but does not by
      itself identify modern accession P77390. Its sequence-specific catalytic assignment
      remains curated evidence.
    evidence_ids:
    - e-citc-bridge
    - e-primary-citc
    - e-proteins
- assessment_id: a-membership
  area: graph
  topic: Native membership edges 018-020 and handoffs 021-022
  outcome: supported
  summary: The three exact Rhea directional objects each carry the relevant native
    MetaCyc seeAlso bridge. The precursor and holo carrier are identical output/input
    entities across their adjacent reactions. The two handoff edges claim neither
    a stable maturation complex nor substrate channeling.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-native
  - e-rhea
  - e-replay
  - e-record
- assessment_id: a-exclusions
  area: scope
  topic: Native source conflicts and omitted components
  outcome: supported
  summary: Native alternative acetyl donor and deacetylase branches have different-organism
    evidence; the PathBank ATP-independent condensation is not silently treated as
    E. coli activation. Unsupported free-metal/compartment/assembly claims are omitted.
    Downstream cleavage-complex stoichiometry and the corrected old ACP mass are outside
    the retained mechanism.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-native-proteins
  - e-pathbank
  - e-old-assembly
  - e-record
- assessment_id: a-citc-limit
  area: completeness
  topic: Limits of available primary ligase evidence
  outcome: unknown
  summary: The full 1983 ligase paper was not inspected, and its indexed abstract
    is truncated. The review cannot independently resolve the exact historical enzyme
    sequence or its complete purification/assay details. This is an explicitly retained
    limitation, not a hidden claim of direct modern-accession experimentation.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-primary-citc
  - e-citc-bridge
  - e-record
- assessment_id: a-provenance
  area: provenance
  topic: Source hashes, shared integration and bounded context
  outcome: supported
  summary: All 10 target reference digests match exact preserved bodies. Rhea 139
    identity authority, Rhea 142 mechanism/components, reviewed UniProt 2026_03 and
    public MetaCyc 22.5 are distinguished. Baseline source values are retained, and
    contextual expression queries are not used as catalytic proof.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-replay
  - e-authorities
  - e-context
- assessment_id: a-artifacts
  area: graph
  topic: Publication and repository consistency
  outcome: supported
  summary: Actual source graph, final publication audit and required corpus gates
    preserve the assessed nodes, edges, full evidence and references. These technical
    checks support representation integrity and do not replace the scientific assessment.
  target_ids:
  - MetaCyc:P2-PWY
  evidence_ids:
  - e-record
  - e-generated
  - e-gates
findings: []
actions: []
limitations:
- PMID 6354265 was inspected only as its indexed 250-word truncated abstract; no full
  article or modern-accession-specific purification was verified. The P77390 assignment
  relies on explicit reviewed/EcoCyc IDA curation, which the record discloses.
- PMID 11042274 and the 1987 cleavage-complex correction were inspected as full indexed
  abstracts, not full articles. Relevant original Schneider 2000 PDF text was independently
  read; figure pixels and supplements were not inspected.
- Generic Rhea carrier states preserve complete-protein identity classes and modification
  states, not exact sequences or assembly stoichiometry. Reactive-part balance assumes
  the same unchanged polypeptide backbone cancels.
- The public MetaCyc mechanism snapshot is 22.5; the review makes no claim about the
  latest licensed release. Rhea 139 identity authority is distinct from 142 mechanistic
  evidence.
- The record supports a bounded maturation mechanism, not an assertion that every
  K-12 strain expresses the pathway or supports a particular citrate-fermentation
  flux under arbitrary conditions.
- iModulonDB exact-locus hits are context only; zero returned module hits is not negative
  evidence for expression, regulation or catalysis.
- Programmatic SVG/KGX audit does not replace browser visual review. No browser inspection
  is claimed.
notes:
- The target remained at c76b50f65ef43e599ca16a9789144840660b52a4dc1d9adcd46fb8c5fecdd450
  from initial governed inspect through final save. Shared authority inputs changed
  during integration and were explicitly compared against baseline values, checked
  against exact sources and re-inspected before saving.
- 'Two non-required scratch execution failures are retained honestly: system-Python
  missing PyYAML and reviewer quote-field mismatch. Both were superseded with repository-environment
  checks; no target/source correction resulted. All required final gates passed.'
- The ignored-inclusive prior review/report search found no exact target occurrence
  in the bounded directories. Empty findings does not retire unrelated prior issues.
links:
- https://juser.fz-juelich.de/record/26938/files/19821.pdf
- https://pubmed.ncbi.nlm.nih.gov/11042274/
- https://pubmed.ncbi.nlm.nih.gov/6354265/
tags:
- citrate
- independent-scientific-review
- whole-protein-carrier-states
- rhea
- metacyc
```
