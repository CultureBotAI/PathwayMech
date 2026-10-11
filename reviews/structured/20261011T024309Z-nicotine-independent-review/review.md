# Independent scientific review of complete nicotine degradation II

- Review: 20261011T024309Z-nicotine-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T02:30:54Z
- Finished UTC: 2026-10-11T02:43:09Z
- Reviewer: Codex independent reviewer (/root/pathway_literature_candidates) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete native 11-step S16 route is supported across 99 edges and 169 evidence blocks. One minor provenance defect identified independently as issue343 was corrected and verified before this first immutable bundle. Full current chemistry and sequence identity replay pass; catalyst, carrier, cofactor, assembly and primary-access limits remain explicit.

## Scope And Provenance

Full independent scientific assessment of one maintained record, every local node, edge, reference and material qualifier.

Selection: Exact assigned MetaCyc:PWY-6993 record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e3bceba7613eb0525af3ff76ef32520201ae9f33.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-6993 | data/pathways/nicotine-degradation-ii.yaml | maintained | nicotine degradation II (pyrrolidine pathway) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Initial governed capture | passed | False | MetaCyc:PWY-6993 | Captured initial 559e7e39 target before assessment. Actual input ledger retained in maintained independent audit. |
| Independent replay | passed | False | MetaCyc:PWY-6993 | Actual terminal0; script hash d6071f088d6728af369261d44799ac7691d009c6142fd920601f17f8a522a99c and complete result retained in independent audit. |
| Independent identities | passed | False | MetaCyc:PWY-6993 | Actual terminal0; script hash a55b13aa4870837f96d9a6ec49d27e13d9eabfda96a66e28647e91edb6f9cd74 and complete result retained in independent audit. |
| Independent final_checks | passed | False | MetaCyc:PWY-6993 | Actual terminal0; script hash 57fff16c1d786dc8b2f69309eac268e8d7ee38170c51304a549fe59aa9c5ded5 and complete result retained in independent audit. |
| Independent imodulon_replay | passed | False | MetaCyc:PWY-6993 | Actual terminal0; script hash fb384fab0faea796c2cdd53cbfe6b1b21e345341654bbcc59b65d06b03f9d722 and complete result retained in independent audit. |
| Superseded reviewer helper assumption | failed | False | MetaCyc:PWY-6993 | Initial reviewer helper used generic has_input/has_output for chemical sides. It failed before producing a result, was corrected to actual consumes/produces orientation, and fresh original-RDF replay passed. No target defect inferred. |
| Reassessed final input capture | passed | False | MetaCyc:PWY-6993 | Changed target, source-scoped correction, author receipts, current authorities and generated/gate inputs were re-inspected before this capture. Actual exit0. |
| Integrated just render-pages | passed | False | MetaCyc:PWY-6993 | Coordinator executed actual terminal0; full suite began before final wording-only #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-render-final.log SHA256 257f6ce37e76e686b05cd30b14dadf3a8d6626f60686cc573b0c3537ad185f2b. Broad tests are not scientific review of other records. |
| Integrated just lint | passed | True | MetaCyc:PWY-6993 | Coordinator executed actual terminal0; full suite began before final wording-only #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-lint-final.log SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41. Broad tests are not scientific review of other records. |
| Integrated git diff --check | passed | True | MetaCyc:PWY-6993 | Coordinator executed actual terminal0; full suite began before final wording-only #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-diff-final.log SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Broad tests are not scientific review of other records. |
| Integrated just check-identifiers | passed | False | MetaCyc:PWY-6993 | Coordinator executed actual terminal0; full suite began before final wording-only #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-identifiers-final.log SHA256 bb7d961695675ba4275eec531acc369b8c65ccf0d282bac8db9183b78116ffad. Broad tests are not scientific review of other records. |
| Integrated just kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx | passed | False | MetaCyc:PWY-6993 | Coordinator executed actual terminal0; full suite began before final wording-only #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-kgx-audit-cli.log SHA256 0358b67cbfdfb81f11ab82031e7c1295657476daa9f07694b54a8a8b784039d8. Broad tests are not scientific review of other records. |
| Integrated just validate | passed | True | MetaCyc:PWY-6993 | Coordinator executed actual terminal0; full suite began before final wording-only #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-validate-final.log SHA256 6d4ef45263da9a15856ed329afba53baf9e0852fab77ab7c3cf1c667204180c3. Broad tests are not scientific review of other records. |
| Integrated just test | passed | True | MetaCyc:PWY-6993 | Coordinator executed actual terminal0; full suite began before final wording-only #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-test-final.log SHA256 a774bf956157bf5a83ee4889b43a036dce27e82b7a1363cedf12c51d08bb7bf3. Broad tests are not scientific review of other records. |
| Integrated UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just vendored-check | passed | False | MetaCyc:PWY-6993 | Coordinator executed actual terminal0; full suite began before final wording-only #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-vendored.log SHA256 b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6. Broad tests are not scientific review of other records. |
| Superseded stale generated-page check | failed | False | MetaCyc:PWY-6993 | Actual earlier exit1: target evidence changed after render, leaving stale pages. Regeneration and final2 full validation passed. Original log retained at /private/tmp/pathwaymech-nicotine-next-validate-final.log SHA256 2415768b7002d1cea4da3bc530a2463514b3114e1a069de0bbfaf03cfbc943f4. |
| Independent final generated artifact replay | passed | False | MetaCyc:PWY-6993 | Actual terminal0 session25892 after inspecting complete helper and final2 CLI log/exit assertions. All241 edges and419 evidence across cohort match; nicotine99 edges169 evidence match exactly. External proof SHA256 b90180bf5e281494b7006be54b40700887be1d10ac550b7428c95cfc3e0d816a. No browser visual claim. |

## Scientific And Domain Assessments

### Complete native route and exact S16 scope

identity: supported. Targets: MetaCyc:PWY-6993.

All eleven native steps and both carbon branches retained, without truncating uncertain catalyst assignments. S16 identities are exact; other-strain enzyme assays do not substitute for S16 proteins.

### All 55 chemical sides,10 reaction balances and physiological redox change

graph: supported. Targets: MetaCyc:PWY-6993.

Current two-CycN NicA2/Pnao equations are supported independently of the old oxidase map. Whole carriers and all protons/coefficients retained. Spontaneous hydration is a BiochemicalReaction without a fabricated catalyst. Spm generic acceptor permits only symbolic balance.

### Activity, components and cofactors

evidence: supported. Targets: MetaCyc:PWY-6993.

Source-defined assemblies, functional enables roles and exact sequence bridges are justified. Hpo Fe activation, HspB FAD inference, Spm proposed cofactor and unresolved S16 aldehyde catalysts remain explicit evidence limits. No isolated subunit sufficiency or foreign complex is asserted.

### All eleven memberships and ten dependencies

representation: supported. Targets: MetaCyc:PWY-6993.

Native memberships and predecessors correspond to current carbon-intermediate chemistry after source-attribution correction; carrier/cofactor shared pools create no extra causal edges.

### Predicted periplasmic locations

evidence: supported. Targets: MetaCyc:PWY-6993.

All three location edges are explicitly source predictions, with no claim of native fractionation or obligatory complete pathway compartment.

### References, issue343 and computational context

provenance: supported. Targets: MetaCyc:PWY-6993.

The minor provenance defect is corrected and independently verified before this first immutable bundle. All original digest scopes and unreviewed/abstract-only limits remain visible; adapter context is not mechanistic proof.

### Final integrated validation and generated output

schema: supported. Targets: MetaCyc:PWY-6993.

Final corpus gates and exact generated serialization checks pass for the frozen record. Shared checks are not an independent scientific verdict on other batch records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/nicotine-degradation-ii.yaml; Complete initial and final target; 45 participants, 11 reactions, 99 edges, 169 evidence; every field and all material qualifiers | supports | Full selected route begins with (S)-nicotine and ends in fumarate and succinate, with all eleven native reactions retained. No transport, downstream carrier reoxidation or alternative nicotine route is added. |
| e-native | https://pathway.yeastgenome.org/getxml?META:PWY-6993; MetaCyc 22.5 exact PWY-6993 reaction-list, reaction-layout, ten reaction-ordering objects; all eleven separate reaction XMLs | supports | Independently read and parsed exact source boundary and order. Current NicA2/Pnao physiological redox chemistry is explicitly sourced separately from old native oxygen/acceptor equations; two catalyst gaps remain visible. |
| e-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Rhea 142 families73655,75415,75351,34215,33927,27522,30843,27385,13169,13213; all directed side/containsN/participant/compound triples; official directions TSV | supports | Independent original-RDF streaming replay reproduces all 50 Rhea side occurrences and master-relative left_to_right directions. Ten exact atom/charge balances pass; whole cytochrome carrier backbones cancel while reactive portions are used only for balance, not graph fragmentation. Native Spm contributes five separately checked sides and only symbolic generic A/AH2 balance. |
| e-identities | https://rest.uniprot.org/uniprotkb/A0A0E3ELC2.json; Eight full current UniProt records; GQ857548 four deposited CDS translations; WP_080563818.1; RCSB7TLX entity1 sequence, source taxon and SIFTS mapping | supports | All accession labels/statuses and source organisms were inspected. CycN full132 aa equals RefSeq, and S16 mature105 aa equals residues 28–132 with explicit SIFTS. The four nic2 enzymes exactly match primary deposited sequences; unreviewed entries are not treated as experimental annotation authorities. |
| e-assemblies | https://pathway.yeastgenome.org/getxml?META:CPLX-8439; CPLX-8439 two MONOMER-17159; CPLX-8990 two MONOMER-19246; CPLX-8991 three native monomers19251/19252/19253 one each; native species, unification and catalytic frames | supports | All three source identities denote S16. HspB and Iso component bridges are exact; Spm stoichiometry remains source-defined rather than purified measurement. Deleted historical UniProt entries are excluded. Foreign HZN6 Sap tetramer is not transferred. Conditional NicA2 monomer/dimer and Pnao homodimer requirements remain qualified. |
| e-primary2021 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7904663/fullTextXML; PMID33432238 Introduction P5; Results P8–P25; Methods P26–P40; extended Fig2/P46 and P50 | supports | Purified NicA2 uses two one-electron CycN acceptors, supported by S16 disruption/complementation. N-methylmyosmine hydrolysis is spontaneous. Oxygen is slow side reactivity; downstream CycN oxidant remains unknown. Conditional NicA2 assembly does not define a fixed complex. |
| e-primary2022 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9396064/fullTextXML; PMID35835223 Introduction p0015; Results p0030–p0080; Discussion p0110; Methods p0115–p0175 | supports | Pnao transfers two electrons to CycN and S16 genetic complementation supports the physiological partner. Recombinant signal-deleted construct, homodimer, and primary 7TLX structure are bounded. All three periplasmic locations are signal-sequence predictions, not native fractionation. |
| e-primary2013 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3812094/fullTextXML; PMID24204321 Results proteomics, spm polar disruption/complementation and sapd; Fig5; Discussion Mo-MCD proposal; gene-disruption/complementation Methods | supports | SpmABC genetics support SP hydroxylation without direct purified assembly or cofactor determination. Mo-MCD proposal follows family similarity/failed active E. coli expression. S16 Sapd deletion slows but does not abolish nicotine growth, without proving NADP specificity. |
| e-primary2012 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3332521/fullTextXML; PMID22530095 Full Results/Discussion/Methods and captions; zero-based //body//p ordinals5,7,8,17,24,26; GQ857548 deposit | supports | Purified Hpo forms N-formylmaleamate, Fe2 enhances activity, and assay uses 0.025 mM iron. Nfo formate and Ami ammonium use coupled reporting enzymes; NAD/NADPH reporters are not graph substrates. Iso maleate-to-fumarate assay uses thioglycerol as condition, not physiological cofactor. |
| e-abstracts | https://pubmed.ncbi.nlm.nih.gov/21949128/; Complete indexed primary abstracts PMID21949128,23347155,22267672 | supports | HspB abstract establishes S16 NADH-dependent product formation and oxygen labeling, but detailed assembly/stoichiometry uses separately inspected current databases. Iso abstract supports S16 structural/enzymatic study. HZN6 Sap abstract supports NADP-specific activity in that strain. Full texts for first/third were unavailable; no claim they were read. |
| e-chebi | http://purl.obolibrary.org/obo/chebi/255/chebi.owl; Pinned ChEBI 255 SemanticSQL: CHEBI193521 deprecated/IAO0100001→190393 and active alternative ID; exact formula and charge | supports | Explicit issuing-authority replacement supports the active N-methylmyosmine state. Native CPD0-1882 differs in formula/charge from its ChEBI71308 cross-reference, so native cofactor identity is retained without asserting chemical equivalence. Digest is the uncompressed SemanticSQL database, not the OWL download. |
| e-audit | research/pathway_additions/2026-10-11-nicotine-next/nicotine-independent-review-audit.json; Every-edge coverage; independent original-source chemistry, protein/sequence/assembly, digest, correction and offline adapter replays | supports | All 99 edges and 169 evidence blocks assessed. Sixty retained original source bodies rehashed; all reference digests resolve. Exact script hashes and corrected reviewer-helper failure retained. No literal quotation fields occur; assertions remain source-scoped. |
| e-343 | https://github.com/CultureBotAI/PathwayMech/issues/343; Initial inspected559e7e393e76873e8b86e4bb14aa228208e4ec6ffda1bfb43dd147ff73d45aed; final59d1a699b4e40ce680715afa958f8a659feae11b6b1786a5867f25733b83d36c; edges062,082–091 | supports | Independent review found native-source over-attribution: CPLX comment did not give full equation and PWY XML did not give ChEBI IDs. Exactly 11 edges corrected; native catalytic/order facts now have separate current-chemistry evidence. Old retired intermediate is no longer called the active retained state. No prior immutable bundle existed, so no structured resolved lineage is invented. |
| e-context | research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json; Canonical adapter dataset inventory and independent offline replay of 45 retained responses/44 E. coli searches | context_only | Twenty organisms / 28 datasets, including p_putida/precise321, do not establish S16 applicability. Nicotine receives no biochemical support/refutation from this inventory. Console missing-dotenv failure/fallback disclosed. Zero module-name hits never establish absence of membership. |
| e-gates | research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json; Actual final coordinator terminal receipts/log hashes and generated-output audit | supports | All required checks reached terminal success. Full tests began before final wording-only #343/#344 corrections; implementation/tests did not change. Fresh full-corpus validation, render, lint, identifiers and KGX cover corrected frozen bytes. Earlier stale-page failure after the first render is retained and corrected by rerendering. Reviewer inspected final logs and digests; deterministic gates do not establish biological truth. |

## Limits And Additional Notes

- Two native aldehyde reactions lack exact supported S16 catalyst assignments; complete chemistry retained with explicit gaps.
- Spm physiological electron acceptor and CycN reoxidation partner remain unresolved. Generic Spm balance is symbolic only.
- Spm Mo-MCD is an explicitly proposed family-based association, not purified cofactor occupancy. Source-defined subunit coefficients are not measured stoichiometry.
- NicA2 assembly depends on conditions; Pnao functional role does not invent an external complex. Unreviewed proteins retain their statuses despite exact primary sequence bridges.
- Periplasmic locations are predictions; Hpo metal activation and thioglycerol assay conditions do not establish physiological occupancy.
- Four primary full XML bodies and three primary abstracts inspected. PMID21949128 and22267672 full-text/PDF access failed; database assertions are not recast as independently read primary text.
- iModulon dataset inventory does not establish S16 applicability; no absence or mechanistic claim follows from searches.
- Initial independent replay used the wrong chemical predicate convention, failed, was corrected and rerun successfully. No record defect inferred from reviewer helper failure.
- No browser visual inspection claimed; generated output is checked programmatically.
- Current hidden/ignored-inclusive search covers accessible worktree records/research/docs; original Documents checkout remains OS-inaccessible. No exhaustive pathway-source claim.
- Issue343 discovery and initial target are retained in inspected evidence and maintained audit. Empty final findings does not fabricate a prior resolved structured finding.
- Root separately identified active retired-ID slot issue341; final target has no such source_mapping and explicit replacement remains on its chemical edges.
- Final changed inputs were reassessed before canonical final capture. Future fixes belong to maintained YAML/source inputs; generated outputs must be regenerated.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T024309Z-nicotine-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of complete nicotine degradation II
started_at: '2026-10-11T02:30:54Z'
finished_at: '2026-10-11T02:43:09Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_literature_candidates)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: A different agent authored nicotine. Reviewer independently
    read target and original sources, without target edits. Reviewer-authored ADP-heptose
    record is excluded.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete native 11-step S16 route is supported across 99 edges and 169
  evidence blocks. One minor provenance defect identified independently as issue343
  was corrected and verified before this first immutable bundle. Full current chemistry
  and sequence identity replay pass; catalyst, carrier, cofactor, assembly and primary-access
  limits remain explicit.
source:
  git_revision: e3bceba7613eb0525af3ff76ef32520201ae9f33
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: 563ace71ecbab2ccdf71e353813afe89988024b9f46288611cbfb97db726c67f
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 88dfc909cc4efc39e0c4c05a7c4d721ec6f2e68d4d4f431df1f1d4c4307d80fe
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: c5efa10d14da146c39262662f330c6a39be9be71c5072dd619d644bc2724be6c
    role: context
  - path: data/pathways/nicotine-degradation-ii.yaml
    sha256: 59d1a699b4e40ce680715afa958f8a659feae11b6b1786a5867f25733b83d36c
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
  - path: pages/records/MetaCyc_PWY-6993.html
    sha256: 9c594980d90b56e99d7e0bb052e26350f294db01c7fb5d10354fe132871d6694
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-integration.json
    sha256: 508115133210b4b274705562e606b38ce33b774d0b26f9779dc1cd539eff34f1
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-protein-crosscheck.json
    sha256: 7865b01494836dd3e6b104bc804cc013cdefd424f6ee2fcbcdbd3661fcb571eb
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-source-inspection.json
    sha256: 6819051b3cde54f86e72f75c4ddcf7a576a5d56334b32a338125fa211fb4b216
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/baseline-preservation.json
    sha256: 1759ef38d27e253e1f35206ac7a5d0269ff0d8e1325ceb710b58676624229492
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/generated-graph-kgx-audit.json
    sha256: 2012413903397cabd2554fcd7a80841f8db8e3e6c059dc2d2d4f390860d7720a
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json
    sha256: 44fe95b9cef24af8f4ba69d7b845142d40e63e1ed42ac29db6e8a26361c0c0a9
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-parser-replay.json
    sha256: e0615d4d3eade07658e352e572426479dac155c525c1cf460daaa6846f601f91
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-runner-availability.json
    sha256: f996c636a02f9e017b5831003fa27d0577576dfe355fa9a5097f59644c880698
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-source-manifest.json
    sha256: 4ae60106c78976dcf8396ec0646e69f74d70ea70c018659430223d37e66a9af6
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json
    sha256: 33ca08ff4c31d5f2c03c0b3732b731e2b9d64ad583066f4360cfcddcf5797975
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/nicotine-curation.md
    sha256: be6957d2cac147d69c6b7e28a7d6517accf44a56d56eb6ef3b2ba787d0c4b573
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/nicotine-dedup.json
    sha256: 6dd44a402448c043afc927238db057d3408bebca4fc6f8250364e1a08efd6997
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/nicotine-identifiers.json
    sha256: 1afbbaf8552593d4e5f2e4240383d7bbcba5d367ae805d7dd93d69f82f2df43c
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/nicotine-independent-review-audit.json
    sha256: 8e16e6a43782ab833af79508a890e78c7bf90bbbe2fd391522793ff3e9d27004
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/nicotine-replay.py
    sha256: 6a0dfb06f2bc804b85ab3c904d78f2e54af71cb9ba87c30ba71b1d137e3a3fa2
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/nicotine-source-manifest.json
    sha256: ef5d887bb469114c8438f61c9a3ba73c77eb6cc22ef62e2bc6011e3497150c8e
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/nicotine-source-projection.json
    sha256: cebf701d6f9c8108e29f799253459284ce84b8c06c500964b10a26b82c9890ef
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/nicotine-validation.json
    sha256: ed5d137a510a135b60a04a14b2863d45b96bec75207969ae044ca27590aec489
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: Full independent scientific assessment of one maintained record, every
    local node, edge, reference and material qualifier.
  selection: Exact assigned MetaCyc:PWY-6993 record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-6993
  exclusions:
  - target: Other 183 pathway records, including reviewer-authored ADP-heptose
    reason: Shared deterministic corpus checks are not scientific review of other
      records.
  - target: CycN reoxidation, transport, alternative nicotine pathways and downstream
      central metabolism
    reason: Outside the full selected native route; unresolved downstream oxidant
      not invented.
targets:
- target_id: MetaCyc:PWY-6993
  path: data/pathways/nicotine-degradation-ii.yaml
  label: nicotine degradation II (pyrrolidine pathway)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nicotine-degradation-ii.yaml
    role: maintained record
checks:
- check_id: c-inspect
  name: Initial governed capture
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-nicotine-independent-review/targets.yaml
    --input src/pathwaymech/schema.py --input docs/CAUSAL_GRAPHS.md --input docs/CURATION.md
    --input docs/HARMONIZATION.md --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-source-projection.json
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-source-manifest.json
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-curation.md
  exit_code: 0
  expected_exit_code: 0
  summary: Captured initial 559e7e39 target before assessment. Actual input ledger
    retained in maintained independent audit.
  evidence_ids:
  - e-audit
- check_id: c-replay-0
  name: Independent replay
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: .venv/bin/python /private/tmp/pathwaymech-nicotine-independent-review/replay.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal0; script hash d6071f088d6728af369261d44799ac7691d009c6142fd920601f17f8a522a99c
    and complete result retained in independent audit.
  evidence_ids:
  - e-audit
- check_id: c-replay-1
  name: Independent identities
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: .venv/bin/python /private/tmp/pathwaymech-nicotine-independent-review/identities.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal0; script hash a55b13aa4870837f96d9a6ec49d27e13d9eabfda96a66e28647e91edb6f9cd74
    and complete result retained in independent audit.
  evidence_ids:
  - e-audit
- check_id: c-replay-2
  name: Independent final_checks
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: .venv/bin/python /private/tmp/pathwaymech-nicotine-independent-review/final_checks.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal0; script hash 57fff16c1d786dc8b2f69309eac268e8d7ee38170c51304a549fe59aa9c5ded5
    and complete result retained in independent audit.
  evidence_ids:
  - e-audit
- check_id: c-replay-3
  name: Independent imodulon_replay
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: .venv/bin/python /private/tmp/pathwaymech-nicotine-independent-review/imodulon_replay.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal0; script hash fb384fab0faea796c2cdd53cbfe6b1b21e345341654bbcc59b65d06b03f9d722
    and complete result retained in independent audit.
  evidence_ids:
  - e-audit
- check_id: c-method
  name: Superseded reviewer helper assumption
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: .venv/bin/python /private/tmp/pathwaymech-nicotine-independent-review/replay.py
  exit_code: 1
  expected_exit_code: 0
  summary: Initial reviewer helper used generic has_input/has_output for chemical
    sides. It failed before producing a result, was corrected to actual consumes/produces
    orientation, and fresh original-RDF replay passed. No target defect inferred.
  evidence_ids:
  - e-audit
- check_id: c-final-inspect
  name: Reassessed final input capture
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-nicotine-independent-review/targets.yaml
    --input conf/identifier_policy.yaml --input conf/identifier_sources.json --input
    data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input docs/CAUSAL_GRAPHS.md --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input pages/records/MetaCyc_PWY-6993.html --input research/pathway_additions/2026-10-11-nicotine-next/authority-integration.json
    --input research/pathway_additions/2026-10-11-nicotine-next/authority-protein-crosscheck.json
    --input research/pathway_additions/2026-10-11-nicotine-next/authority-source-inspection.json
    --input research/pathway_additions/2026-10-11-nicotine-next/baseline-preservation.json
    --input research/pathway_additions/2026-10-11-nicotine-next/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json
    --input research/pathway_additions/2026-10-11-nicotine-next/imodulondb-parser-replay.json
    --input research/pathway_additions/2026-10-11-nicotine-next/imodulondb-runner-availability.json
    --input research/pathway_additions/2026-10-11-nicotine-next/imodulondb-source-manifest.json
    --input research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-curation.md
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-dedup.json
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-identifiers.json
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-replay.py
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-source-manifest.json
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-source-projection.json
    --input research/pathway_additions/2026-10-11-nicotine-next/nicotine-validation.json
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Changed target, source-scoped correction, author receipts, current authorities
    and generated/gate inputs were re-inspected before this capture. Actual exit0.
  evidence_ids:
  - e-audit
- check_id: c-gate-0
  name: Integrated just render-pages
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: just render-pages
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed actual terminal0; full suite began before final wording-only
    #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX
    checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-render-final.log
    SHA256 257f6ce37e76e686b05cd30b14dadf3a8d6626f60686cc573b0c3537ad185f2b. Broad
    tests are not scientific review of other records.'
  evidence_ids:
  - e-gates
- check_id: c-gate-1
  name: Integrated just lint
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-6993
  command: just lint
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed actual terminal0; full suite began before final wording-only
    #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX
    checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-lint-final.log
    SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41. Broad
    tests are not scientific review of other records.'
  evidence_ids:
  - e-gates
- check_id: c-gate-2
  name: Integrated git diff --check
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-6993
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed actual terminal0; full suite began before final wording-only
    #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX
    checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-diff-final.log
    SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Broad
    tests are not scientific review of other records.'
  evidence_ids:
  - e-gates
- check_id: c-gate-3
  name: Integrated just check-identifiers
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: just check-identifiers
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed actual terminal0; full suite began before final wording-only
    #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX
    checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-identifiers-final.log
    SHA256 bb7d961695675ba4275eec531acc369b8c65ccf0d282bac8db9183b78116ffad. Broad
    tests are not scientific review of other records.'
  evidence_ids:
  - e-gates
- check_id: c-gate-4
  name: Integrated just kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: just kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed actual terminal0; full suite began before final wording-only
    #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX
    checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-kgx-audit-cli.log
    SHA256 0358b67cbfdfb81f11ab82031e7c1295657476daa9f07694b54a8a8b784039d8. Broad
    tests are not scientific review of other records.'
  evidence_ids:
  - e-gates
- check_id: c-gate-5
  name: Integrated just validate
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-6993
  command: just validate
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed actual terminal0; full suite began before final wording-only
    #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX
    checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-final2-validate-final.log
    SHA256 6d4ef45263da9a15856ed329afba53baf9e0852fab77ab7c3cf1c667204180c3. Broad
    tests are not scientific review of other records.'
  evidence_ids:
  - e-gates
- check_id: c-gate-6
  name: Integrated just test
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-6993
  command: just test
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed actual terminal0; full suite began before final wording-only
    #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX
    checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-test-final.log
    SHA256 a774bf956157bf5a83ee4889b43a036dce27e82b7a1363cedf12c51d08bb7bf3. Broad
    tests are not scientific review of other records.'
  evidence_ids:
  - e-gates
- check_id: c-gate-7
  name: Integrated UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just vendored-check
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed actual terminal0; full suite began before final wording-only
    #343/#344 corrections, with no code/test change; fresh validation/render/lint/identifier/KGX
    checks cover final frozen bytes. Reviewer read and rehashed log /private/tmp/pathwaymech-nicotine-next-vendored.log
    SHA256 b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6. Broad
    tests are not scientific review of other records.'
  evidence_ids:
  - e-gates
- check_id: c-superseded-0
  name: Superseded stale generated-page check
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: just validate
  exit_code: 1
  expected_exit_code: 0
  summary: 'Actual earlier exit1: target evidence changed after render, leaving stale
    pages. Regeneration and final2 full validation passed. Original log retained at
    /private/tmp/pathwaymech-nicotine-next-validate-final.log SHA256 2415768b7002d1cea4da3bc530a2463514b3114e1a069de0bbfaf03cfbc943f4.'
  evidence_ids:
  - e-gates
- check_id: c-independent-graph
  name: Independent final generated artifact replay
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-6993
  command: .venv/bin/python /private/tmp/pathwaymech-nicotine-next-graph-audit.py
    --comparison-kgx-dir /private/tmp/pathwaymech-nicotine-next-kgx --receipt /private/tmp/pathwaymech-nicotine-next-independent-graph-replay-final.json
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal0 session25892 after inspecting complete helper and final2
    CLI log/exit assertions. All241 edges and419 evidence across cohort match; nicotine99
    edges169 evidence match exactly. External proof SHA256 b90180bf5e281494b7006be54b40700887be1d10ac550b7428c95cfc3e0d816a.
    No browser visual claim.
  evidence_ids:
  - e-gates
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/nicotine-degradation-ii.yaml
  locator: Complete initial and final target; 45 participants, 11 reactions, 99 edges,
    169 evidence; every field and all material qualifiers
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: Full selected route begins with (S)-nicotine and ends in fumarate and succinate,
    with all eleven native reactions retained. No transport, downstream carrier reoxidation
    or alternative nicotine route is added.
  snapshot_sha256: 59d1a699b4e40ce680715afa958f8a659feae11b6b1786a5867f25733b83d36c
- evidence_id: e-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY-6993
  locator: MetaCyc 22.5 exact PWY-6993 reaction-list, reaction-layout, ten reaction-ordering
    objects; all eleven separate reaction XMLs
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: Independently read and parsed exact source boundary and order. Current
    NicA2/Pnao physiological redox chemistry is explicitly sourced separately from
    old native oxygen/acceptor equations; two catalyst gaps remain visible.
  snapshot_sha256: f3fdd212ea8a22f80d23fd62fb2f47b54b367445deeeffd8954fdf121ea860e8
- evidence_id: e-rhea
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Rhea 142 families73655,75415,75351,34215,33927,27522,30843,27385,13169,13213;
    all directed side/containsN/participant/compound triples; official directions
    TSV
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: Independent original-RDF streaming replay reproduces all 50 Rhea side occurrences
    and master-relative left_to_right directions. Ten exact atom/charge balances pass;
    whole cytochrome carrier backbones cancel while reactive portions are used only
    for balance, not graph fragmentation. Native Spm contributes five separately checked
    sides and only symbolic generic A/AH2 balance.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-identities
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A0E3ELC2.json
  locator: Eight full current UniProt records; GQ857548 four deposited CDS translations;
    WP_080563818.1; RCSB7TLX entity1 sequence, source taxon and SIFTS mapping
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: All accession labels/statuses and source organisms were inspected. CycN
    full132 aa equals RefSeq, and S16 mature105 aa equals residues 28–132 with explicit
    SIFTS. The four nic2 enzymes exactly match primary deposited sequences; unreviewed
    entries are not treated as experimental annotation authorities.
  snapshot_sha256: c283c70c8900d3f544dc096a4a12204b1aab70c0eba8222469e064f2cef07fba
- evidence_id: e-assemblies
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:CPLX-8439
  locator: CPLX-8439 two MONOMER-17159; CPLX-8990 two MONOMER-19246; CPLX-8991 three
    native monomers19251/19252/19253 one each; native species, unification and catalytic
    frames
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: All three source identities denote S16. HspB and Iso component bridges
    are exact; Spm stoichiometry remains source-defined rather than purified measurement.
    Deleted historical UniProt entries are excluded. Foreign HZN6 Sap tetramer is
    not transferred. Conditional NicA2 monomer/dimer and Pnao homodimer requirements
    remain qualified.
  snapshot_sha256: c719524c0b70efa36407c44bcbd9f3a5435cc86eb6b8466f3314c47680c7b806
- evidence_id: e-primary2021
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7904663/fullTextXML
  locator: PMID33432238 Introduction P5; Results P8–P25; Methods P26–P40; extended
    Fig2/P46 and P50
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: Purified NicA2 uses two one-electron CycN acceptors, supported by S16 disruption/complementation.
    N-methylmyosmine hydrolysis is spontaneous. Oxygen is slow side reactivity; downstream
    CycN oxidant remains unknown. Conditional NicA2 assembly does not define a fixed
    complex.
  snapshot_sha256: a2aed7a7d4d5202ecad0908dd77a87f73adc9edfce80547504cdc61e87d4ee2b
- evidence_id: e-primary2022
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9396064/fullTextXML
  locator: PMID35835223 Introduction p0015; Results p0030–p0080; Discussion p0110;
    Methods p0115–p0175
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: Pnao transfers two electrons to CycN and S16 genetic complementation supports
    the physiological partner. Recombinant signal-deleted construct, homodimer, and
    primary 7TLX structure are bounded. All three periplasmic locations are signal-sequence
    predictions, not native fractionation.
  snapshot_sha256: d7c879b84237ffc553ad714d4a2d746bba878bb74f2d5476035d503d27281a89
- evidence_id: e-primary2013
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3812094/fullTextXML
  locator: PMID24204321 Results proteomics, spm polar disruption/complementation and
    sapd; Fig5; Discussion Mo-MCD proposal; gene-disruption/complementation Methods
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: SpmABC genetics support SP hydroxylation without direct purified assembly
    or cofactor determination. Mo-MCD proposal follows family similarity/failed active
    E. coli expression. S16 Sapd deletion slows but does not abolish nicotine growth,
    without proving NADP specificity.
  snapshot_sha256: 8e34eaa3e528e674a94ea47b9ef1cff68ce73b97e4a806d8544b13442734bfe0
- evidence_id: e-primary2012
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3332521/fullTextXML
  locator: PMID22530095 Full Results/Discussion/Methods and captions; zero-based //body//p
    ordinals5,7,8,17,24,26; GQ857548 deposit
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: Purified Hpo forms N-formylmaleamate, Fe2 enhances activity, and assay
    uses 0.025 mM iron. Nfo formate and Ami ammonium use coupled reporting enzymes;
    NAD/NADPH reporters are not graph substrates. Iso maleate-to-fumarate assay uses
    thioglycerol as condition, not physiological cofactor.
  snapshot_sha256: 3992e04ad2ee4a89a774dde2b148343b4de0fd8cf7fd82fa96541c71dcdb88ff
- evidence_id: e-abstracts
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/21949128/
  locator: Complete indexed primary abstracts PMID21949128,23347155,22267672
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: HspB abstract establishes S16 NADH-dependent product formation and oxygen
    labeling, but detailed assembly/stoichiometry uses separately inspected current
    databases. Iso abstract supports S16 structural/enzymatic study. HZN6 Sap abstract
    supports NADP-specific activity in that strain. Full texts for first/third were
    unavailable; no claim they were read.
  snapshot_sha256: 05e3602b9bb82057334ca2e4479574c86f7558affe5e8a527f26e45ccff058c4
- evidence_id: e-chebi
  kind: authority
  reference: http://purl.obolibrary.org/obo/chebi/255/chebi.owl
  locator: 'Pinned ChEBI 255 SemanticSQL: CHEBI193521 deprecated/IAO0100001→190393
    and active alternative ID; exact formula and charge'
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: Explicit issuing-authority replacement supports the active N-methylmyosmine
    state. Native CPD0-1882 differs in formula/charge from its ChEBI71308 cross-reference,
    so native cofactor identity is retained without asserting chemical equivalence.
    Digest is the uncompressed SemanticSQL database, not the OWL download.
  snapshot_sha256: 26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f
- evidence_id: e-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/nicotine-independent-review-audit.json
  locator: Every-edge coverage; independent original-source chemistry, protein/sequence/assembly,
    digest, correction and offline adapter replays
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: All 99 edges and 169 evidence blocks assessed. Sixty retained original
    source bodies rehashed; all reference digests resolve. Exact script hashes and
    corrected reviewer-helper failure retained. No literal quotation fields occur;
    assertions remain source-scoped.
  snapshot_sha256: 8e16e6a43782ab833af79508a890e78c7bf90bbbe2fd391522793ff3e9d27004
- evidence_id: e-343
  kind: validation
  reference: https://github.com/CultureBotAI/PathwayMech/issues/343
  locator: Initial inspected559e7e393e76873e8b86e4bb14aa228208e4ec6ffda1bfb43dd147ff73d45aed;
    final59d1a699b4e40ce680715afa958f8a659feae11b6b1786a5867f25733b83d36c; edges062,082–091
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: 'Independent review found native-source over-attribution: CPLX comment
    did not give full equation and PWY XML did not give ChEBI IDs. Exactly 11 edges
    corrected; native catalytic/order facts now have separate current-chemistry evidence.
    Old retired intermediate is no longer called the active retained state. No prior
    immutable bundle existed, so no structured resolved lineage is invented.'
- evidence_id: e-context
  kind: database
  reference: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json
  locator: Canonical adapter dataset inventory and independent offline replay of 45
    retained responses/44 E. coli searches
  accessed_at: '2026-10-11T02:43:09Z'
  support: context_only
  summary: Twenty organisms / 28 datasets, including p_putida/precise321, do not establish
    S16 applicability. Nicotine receives no biochemical support/refutation from this
    inventory. Console missing-dotenv failure/fallback disclosed. Zero module-name
    hits never establish absence of membership.
  snapshot_sha256: 44fe95b9cef24af8f4ba69d7b845142d40e63e1ed42ac29db6e8a26361c0c0a9
- evidence_id: e-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json
  locator: Actual final coordinator terminal receipts/log hashes and generated-output
    audit
  accessed_at: '2026-10-11T02:43:09Z'
  support: supports
  summary: 'All required checks reached terminal success. Full tests began before
    final wording-only #343/#344 corrections; implementation/tests did not change.
    Fresh full-corpus validation, render, lint, identifiers and KGX cover corrected
    frozen bytes. Earlier stale-page failure after the first render is retained and
    corrected by rerendering. Reviewer inspected final logs and digests; deterministic
    gates do not establish biological truth.'
  snapshot_sha256: 33ca08ff4c31d5f2c03c0b3732b731e2b9d64ad583066f4360cfcddcf5797975
assessments:
- assessment_id: a-identity
  area: identity
  topic: Complete native route and exact S16 scope
  outcome: supported
  target_ids:
  - MetaCyc:PWY-6993
  evidence_ids:
  - e-record
  - e-native
  - e-primary2013
  - e-identities
  summary: All eleven native steps and both carbon branches retained, without truncating
    uncertain catalyst assignments. S16 identities are exact; other-strain enzyme
    assays do not substitute for S16 proteins.
- assessment_id: a-chemistry
  area: graph
  topic: All 55 chemical sides,10 reaction balances and physiological redox change
  outcome: supported
  target_ids:
  - MetaCyc:PWY-6993
  evidence_ids:
  - e-rhea
  - e-chebi
  - e-primary2021
  - e-primary2022
  summary: Current two-CycN NicA2/Pnao equations are supported independently of the
    old oxidase map. Whole carriers and all protons/coefficients retained. Spontaneous
    hydration is a BiochemicalReaction without a fabricated catalyst. Spm generic
    acceptor permits only symbolic balance.
- assessment_id: a-catalysts
  area: evidence
  topic: Activity, components and cofactors
  outcome: supported
  target_ids:
  - MetaCyc:PWY-6993
  evidence_ids:
  - e-identities
  - e-assemblies
  - e-primary2012
  - e-primary2013
  - e-abstracts
  summary: Source-defined assemblies, functional enables roles and exact sequence
    bridges are justified. Hpo Fe activation, HspB FAD inference, Spm proposed cofactor
    and unresolved S16 aldehyde catalysts remain explicit evidence limits. No isolated
    subunit sufficiency or foreign complex is asserted.
- assessment_id: a-order
  area: representation
  topic: All eleven memberships and ten dependencies
  outcome: supported
  target_ids:
  - MetaCyc:PWY-6993
  evidence_ids:
  - e-native
  - e-rhea
  - e-343
  summary: Native memberships and predecessors correspond to current carbon-intermediate
    chemistry after source-attribution correction; carrier/cofactor shared pools create
    no extra causal edges.
- assessment_id: a-location
  area: evidence
  topic: Predicted periplasmic locations
  outcome: supported
  target_ids:
  - MetaCyc:PWY-6993
  evidence_ids:
  - e-primary2022
  - e-record
  summary: All three location edges are explicitly source predictions, with no claim
    of native fractionation or obligatory complete pathway compartment.
- assessment_id: a-provenance
  area: provenance
  topic: References, issue343 and computational context
  outcome: supported
  target_ids:
  - MetaCyc:PWY-6993
  evidence_ids:
  - e-audit
  - e-343
  - e-context
  - e-chebi
  summary: The minor provenance defect is corrected and independently verified before
    this first immutable bundle. All original digest scopes and unreviewed/abstract-only
    limits remain visible; adapter context is not mechanistic proof.
- assessment_id: a-gates
  area: schema
  topic: Final integrated validation and generated output
  outcome: supported
  target_ids:
  - MetaCyc:PWY-6993
  evidence_ids:
  - e-gates
  - e-audit
  summary: Final corpus gates and exact generated serialization checks pass for the
    frozen record. Shared checks are not an independent scientific verdict on other
    batch records.
findings: []
actions: []
limitations:
- Two native aldehyde reactions lack exact supported S16 catalyst assignments; complete
  chemistry retained with explicit gaps.
- Spm physiological electron acceptor and CycN reoxidation partner remain unresolved.
  Generic Spm balance is symbolic only.
- Spm Mo-MCD is an explicitly proposed family-based association, not purified cofactor
  occupancy. Source-defined subunit coefficients are not measured stoichiometry.
- NicA2 assembly depends on conditions; Pnao functional role does not invent an external
  complex. Unreviewed proteins retain their statuses despite exact primary sequence
  bridges.
- Periplasmic locations are predictions; Hpo metal activation and thioglycerol assay
  conditions do not establish physiological occupancy.
- Four primary full XML bodies and three primary abstracts inspected. PMID21949128
  and22267672 full-text/PDF access failed; database assertions are not recast as independently
  read primary text.
- iModulon dataset inventory does not establish S16 applicability; no absence or mechanistic
  claim follows from searches.
- Initial independent replay used the wrong chemical predicate convention, failed,
  was corrected and rerun successfully. No record defect inferred from reviewer helper
  failure.
- No browser visual inspection claimed; generated output is checked programmatically.
- Current hidden/ignored-inclusive search covers accessible worktree records/research/docs;
  original Documents checkout remains OS-inaccessible. No exhaustive pathway-source
  claim.
notes:
- Issue343 discovery and initial target are retained in inspected evidence and maintained
  audit. Empty final findings does not fabricate a prior resolved structured finding.
- Root separately identified active retired-ID slot issue341; final target has no
  such source_mapping and explicit replacement remains on its chemical edges.
- Final changed inputs were reassessed before canonical final capture. Future fixes
  belong to maintained YAML/source inputs; generated outputs must be regenerated.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/343
- https://github.com/CultureBotAI/PathwayMech/issues/341
```
