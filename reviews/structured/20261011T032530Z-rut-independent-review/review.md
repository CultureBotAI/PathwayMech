# Independent scientific review of uracil degradation III

- Review: 20261011T032530Z-rut-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T03:13:39Z
- Finished UTC: 2026-10-11T03:25:30.336829Z
- Reviewer: Codex /root/pathway_authority_cache (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All 53 edges and 92 evidence blocks support the complete corrected Rut pathway with explicit prediction, elementary-chemistry and strain/condition limits. Independent raw-source and primary-evidence review found no actionable defect. Final required repository gates pass.

## Scope And Provenance

Full single maintained target:24 participants,6 reactions,53 edges,92 evidence blocks,22 references.

Selection: Parent assigned a nonauthor independent scientific review; governed inspect preceded assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3886f14c33d37054dc92e8133bb65aced30ee4ef.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY0-1471 | data/pathways/uracil-degradation-iii.yaml | maintained | uracil degradation III |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Superseded initial inspect path attempt | failed | False | MetaCyc:PWY0-1471 | The first command misspelled ontology.json as ontologies.json and failed before assessment. Corrected exact existing path on the next inspect; no source or record change. |
| Governed inspect before source assessment | passed | True | MetaCyc:PWY0-1471 | Successful initial governed inspect captured frozen ba58586f target before full assessment. Final target kind normalized from scratch pathway label to maintained schema classification. |
| Independent full-source replay | passed | True | MetaCyc:PWY0-1471 | Independently extracted 86 Rhea nodes and all selected master/directed families from full release142 RDF. |
| Independent full-source replay | passed | True | MetaCyc:PWY0-1471 | 32 bodies and22 reference digests,33 chemical sides,6 balances,12 exact family locators, all6 fresh UniProt identities/pointers, native YdfG assembly, spontaneous category, hidden/ignored duplicate searches pass. |
| Superseded exploratory export checks | failed | False | MetaCyc:PWY0-1471 | Reviewer scratch checks initially assumed source_records contained target JSON and that all predicate CURIEs used the local namespace. Actual source_records contains evidence references; part_of/provides_input_for map to BFO/RO. Corrected reviewer check below; no data change. |
| Independent actual published Rut projection check | passed | True | MetaCyc:PWY0-1471 | All 53 target edges, 92 evidence blocks, exact descriptions/endpoints and documented predicate CURIEs match YAML; 53 page evidence anchors exist and spontaneous RHEA15650 exports as BiochemicalReaction. |
| just render-pages | passed | True | MetaCyc:PWY0-1471 | Root executed this command; reviewer inspected actual terminal receipt and retained log bytes.  |
| just lint | passed | True | MetaCyc:PWY0-1471 | Root executed this command; reviewer inspected actual terminal receipt and retained log bytes.  |
| git diff --check | passed | True | MetaCyc:PWY0-1471 | Root executed this command; reviewer inspected actual terminal receipt and retained log bytes.  |
| just check-identifiers | passed | True | MetaCyc:PWY0-1471 | Root executed this command; reviewer inspected actual terminal receipt and retained log bytes.  |
| just kgx-export --output-dir /private/tmp/pathwaymech-next-184-kgx | passed | True | MetaCyc:PWY0-1471 | Root executed this command; reviewer inspected actual terminal receipt and retained log bytes.  |
| just validate | passed | True | MetaCyc:PWY0-1471 | Root executed command; actual terminal receipt and rehashed log inspected. Final 186-record corpus passes native/closed schemas, identifier policy, 10,287 evidence blocks, 274 history records, 30 sources, six documentation files, research contract and current pages. |
| just test | passed | True | MetaCyc:PWY0-1471 | Root executed full suite: 1,048 passed, 3 skipped and 3 upstream warnings in 312.20 seconds. It ran on the 187-record superset before Kdo withdrawal; final 186-record rendering, validation, identifiers, lint and KGX were rerun. Implementation, tests and Rut scientific bytes were unchanged. This is not a claimed second full suite on the reduced corpus. |
| UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just vendored-check | passed | True | MetaCyc:PWY0-1471 | Root executed this command; reviewer inspected actual terminal receipt and retained log bytes.  |
| Final input reinspection and byte recheck | passed | True | MetaCyc:PWY0-1471 | All final input hashes verified; any changed context explicitly reassessed, stable scientific target unchanged. |

## Scientific And Domain Assessments

### Exact complete modern Rut pathway

identity: supported. Targets: MetaCyc:PWY0-1471.

MetaCyc PWY0-1471 is the exact uracil degradation III route. GO:0006212 is broader. Six selected reactions retain the whole uracil-to-3HP/2NH4/CO2 boundary with flavin recycling; obsolete native peracid/RutC/RutD assignments are explicitly superseded by inspected primary evidence, not silently treated as equivalent chemistry. Upstream transport, nucleoside cleavage, thymine and regulation are outside this boundary.

### All chemical sides, directions and balances

grounding: supported. Targets: MetaCyc:PWY0-1471.

Independent full Rhea 142 replay checks all 33 source sides and coefficient-specific triple chains against actual YAML. Four left-to-right and two right-to-left members match their masters; all 6 atom/charge balances and complete net pass with ChEBI formulas. Explicit 31604 plus spontaneous 15650 avoids duplicate net 42624. Net 31588 includes spontaneous flavin-N5-oxide reduction without attributing every elementary step to RutA.

### Measured functional activities and physical assembly

evidence: supported. Targets: MetaCyc:PWY0-1471.

RutA/F, B, C and YdfG are supported at their declared experimental scopes. RutF primary material was partially purified and Fre substituted in vitro. RutC deaminase has a 2021 inactive-mutant/background control; its homotrimer has 2012 physical evidence. Native YdfG contains four copies of EG12345/P39831 with exact enzyme-reaction link and current experimental assembly annotation. Qualified enables assertions do not establish monomer sufficiency.

### Explicit RutE uncertainty

evidence: supported. Targets: MetaCyc:PWY0-1471.

RutE reduction is genetic/current-annotation prediction, not a purified-enzyme assay or established NADPH specificity. Its FMN code is curator inference ECO:0000305. Both are explicitly described as probable and not contradicted by inspected experiments; measured YdfG independently grounds the displayed terminal chemical conversion.

### K-12 strain and temperature limits

scope: supported. Targets: MetaCyc:PWY0-1471.

All 6 full reviewed proteins are taxon 83333; native YdfG assembly is MG1655. Primary NCM3722 and derivatives ground K-12 pathway support at the stated room-temperature conditions. This is not universal 37°C growth, uracil carbon assimilation, or proof of essential RutC/RutD. Modern polarity-controlled experiments explicitly qualify earlier deletion interpretations.

### Every endpoint, role, dependency and exported evidence

graph: supported. Targets: MetaCyc:PWY0-1471.

All 53 edges have local endpoints and source references. Carbamate decay remains a biochemical reaction without an enzyme or molecular-activity override. Six dependencies reflect shared chemicals and primary topology, not channeling or physical complexes. Generated artifact checks preserve descriptions and all 92 evidence blocks.

### iModulon expression context

evidence: supported. Targets: MetaCyc:PWY0-1471.

The canonical adapter fallback and 83 exact body rehashes support only dataset/gene-context observations. No Rut module-name hits and accession misses are not negative biology; YoaB/YjgH product substrings are not RutC mechanism support.

### Versioned native objects, reference bodies and final gates

provenance: supported. Targets: MetaCyc:PWY0-1471.

All 22 references map to exact retained source bodies and declared hashes; all 32 acquired bodies independently rehashed. Current UniProt pointers and 12 directional-family locators exist. Final shared identity artifacts and gate/log hashes rechecked on frozen Rut; deterministic checks supplement full scientific assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/pathways/uracil-degradation-iii.yaml; Entire YAML:24 participants,6 reactions,53 edges,92 evidence blocks,22 references | supports | Complete exact Rut chemical route with explicit source modernization and assay/prediction/strain limits. |
| independent-audit | research/pathway_additions/2026-10-11-next-184/rut-independent-review-audit.json; Independent source replay, all edge groups, primary read receipts, hidden/ignored searches | supports | All 33 exact chemical sides,6 balances,12 directional-family locators,32 bodies / 22 reference digests,6 protein entries and native YdfG tetramer were independently checked. Eighty-three retained iModulon bodies rehashed; not a fresh network call. |
| dedup | Current worktree and original Documents checkout; Exact pathway identity, label,proteins, primary PMIDs and uracil-route chemistry | supports | No pre-existing complete Rut mechanism. Shared carbamate reaction,  inventories and uracil-producing nucleoside pathways are distinct. |
| source-1 | https://pathway.yeastgenome.org/getxml?META:PWY0-1471; Exact native identity and stated pathway boundary | supports | uracil degradation III. Inspected retained body at declared version and exact edge locators. Native identity and boundary context. |
| source-2 | https://pathway.yeastgenome.org/getxml?META:CPLX0-1962; Protein[@frameid='CPLX0-1962']/component/Protein; component/coefficient; species; Protein[@frameid='CPLX0-1962']/catalyzes/Enzymatic-Reaction[@frameid='ENZRXN0-7359']/reaction | supports | 3-hydroxy acid dehydrogenase. Inspected retained body at declared version and exact edge locators. Used on rut-edge-038, rut-edge-039. |
| source-3 | https://pathway.yeastgenome.org/getxml?META:EG12345-MONOMER; Protein[@frameid='EG12345-MONOMER']/dblink; component-of | supports | YdfG native subunit identity. Inspected retained body at declared version and exact edge locators. Used on rut-edge-038. |
| source-4 | https://pathway.yeastgenome.org/getxml?META:RXN0-5222; Reaction[@frameid='RXN0-5222']/spontaneous; left; right | supports | spontaneous carbamate decomposition. Inspected retained body at declared version and exact edge locators. Used on rut-edge-020, rut-edge-021, rut-edge-022, rut-edge-023. |
| source-5 | https://pathway.yeastgenome.org/getxml?META:RXN-8974; Exact native identity and stated pathway boundary | supports | 3-hydroxypropionate:NADP+ oxidoreductase. Inspected retained body at declared version and exact edge locators. Native identity and boundary context. |
| source-6 | https://rest.uniprot.org/uniprotkb/P75893.json; /comments/1/reaction/reactionCrossReferences; /comments/1/reaction/evidences | supports | FMN reductase (NADH) RutF. Inspected retained body at declared version and exact edge locators. Used on rut-edge-034. |
| source-7 | https://rest.uniprot.org/uniprotkb/P75898.json; /comments/1/reaction/reactionCrossReferences; /comments/1/reaction/evidences | supports | Pyrimidine monooxygenase RutA. Inspected retained body at declared version and exact edge locators. Used on rut-edge-035. |
| source-8 | https://rest.uniprot.org/uniprotkb/P75897.json; /comments/2/reaction/reactionCrossReferences; /comments/2/reaction/evidences | supports | Ureidoacrylate amidohydrolase RutB. Inspected retained body at declared version and exact edge locators. Used on rut-edge-036. |
| source-9 | https://rest.uniprot.org/uniprotkb/P0AFQ5.json; /comments/1/reaction/reactionCrossReferences; /comments/1/reaction/evidences | supports | 3-aminoacrylate deaminase RutC. Inspected retained body at declared version and exact edge locators. Used on rut-edge-037. |
| source-10 | https://rest.uniprot.org/uniprotkb/P39831.json; /comments/7/texts; /comments/5/reaction; /comments/5/physiologicalReactions | supports | NADP-dependent 3-hydroxy acid dehydrogenase YdfG. Inspected retained body at declared version and exact edge locators. Used on rut-edge-038, rut-edge-039. |
| source-11 | https://rest.uniprot.org/uniprotkb/P75894.json; /proteinDescription/recommendedName; /comments/0/texts; /comments/1/reaction; /comments/2/cofactors/0 | supports | Probable malonic semialdehyde reductase RutE. Inspected retained body at declared version and exact edge locators. Used on rut-edge-040, rut-edge-041. |
| source-12 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2873085/; PMC2873085 paragraphs P1-P2; Figure 1; Scheme 1 | supports | Catalysis of a flavoenzyme-mediated amide hydrolysis. Inspected retained body at declared version and exact edge locators. Used on rut-edge-034. |
| source-13 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2916427/; PMC2916427 Results section sec18 The RutB reaction; Figure 5B; Table 4; PMC2916427 Methods sec13; Results sec18; Table 4; Figure 5C; PMC2916427 Results sec24; Discussion sec26 | supports | The Rut Pathway for Pyrimidine Degradation: Novel Chemistry and Toxicity Problems. Inspected retained body at declared version and exact edge locators. Used on rut-edge-036, rut-edge-039, rut-edge-040. |
| source-14 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6040642/; PMC6040642 main text following Figure 3; Figure 4A-F; PMC6040642 Figure 1 legend | supports | RutA-Catalyzed Oxidative Cleavage of the Uracil Amide Involves Formation of a Flavin-N5-oxide. Inspected retained body at declared version and exact edge locators. Used on rut-edge-035, rut-edge-042. |
| source-15 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8113886/fullTextXML; PMC8113886 Results: RutC is a 3-AA deaminase; Figure 2; Table 1; Assay for 3-AA deaminase activity; PMC8113886 Figure 1 legend; PMC8113886 Figure 1 and legend; Introduction; Results; PMC8113886 Figure 1 and legend | supports | The Rid family member RutC of Escherichia coli is a 3-aminoacrylate deaminase. Inspected retained body at declared version and exact edge locators. Used on rut-edge-037, rut-edge-040, rut-edge-043, rut-edge-044, rut-edge-045, rut-edge-046, rut-edge-047, rut-edge-048, rut-edge-049, rut-edge-050, rut-edge-051, rut-edge-052, rut-edge-053. |
| source-16 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3515367/; PMC3515367 Results and discussion 3.1; Figure 2 | supports | Structure of Escherichia coli RutC, a member of the YjgF family and putative aminoacrylate peracid reductase of the rut operon. Inspected retained body at declared version and exact edge locators. Used on rut-edge-037. |
| source-17 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/21622 rh:substrates http://rdf.rhea-db.org/21620_R; http://rdf.rhea-db.org/21620_R rh:contains1 http://rdf.rhea-db.org/Participant_21620_compound_2613; http://rdf.rhea-db.org/Participant_21620_compound_2613 rh:compound http://rdf.rhea-db.org/Compound_2613; http://rdf.rhea-db.org/Compound_2613 rh:chebi; http://rdf.rhea-db.org/21622 rh:substrates http://rdf.rhea-db.org/21620_R; http://rdf.rhea-db.org/21620_R rh:contains1 http://rdf.rhea-db.org/Participant_21620_compound_1650; http://rdf.rhea-db.org/Participant_21620_compound_1650 rh:compound http://rdf.rhea-db.org/Compound_1650; http://rdf.rhea-db.org/Compound_1650 rh:chebi; http://rdf.rhea-db.org/21622 rh:substrates http://rdf.rhea-db.org/21620_R; http://rdf.rhea-db.org/21620_R rh:contains2 http://rdf.rhea-db.org/Participant_21620_compound_3249; http://rdf.rhea-db.org/Participant_21620_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/21622 rh:products http://rdf.rhea-db.org/21620_L; http://rdf.rhea-db.org/21620_L rh:contains1 http://rdf.rhea-db.org/Participant_21620_compound_1829; http://rdf.rhea-db.org/Participant_21620_compound_1829 rh:compound http://rdf.rhea-db.org/Compound_1829; http://rdf.rhea-db.org/Compound_1829 rh:chebi; http://rdf.rhea-db.org/21622 rh:products http://rdf.rhea-db.org/21620_L; http://rdf.rhea-db.org/21620_L rh:contains1 http://rdf.rhea-db.org/Participant_21620_compound_3484; http://rdf.rhea-db.org/Participant_21620_compound_3484 rh:compound http://rdf.rhea-db.org/Compound_3484; http://rdf.rhea-db.org/Compound_3484 rh:chebi; http://rdf.rhea-db.org/21620 rh:directionalReaction http://rdf.rhea-db.org/21622; http://rdf.rhea-db.org/21622 rh:substrates; rh:products; rh:equation; http://rdf.rhea-db.org/21622 rh:products; corresponding rh:contains/rh:compound/rh:chebi; http://rdf.rhea-db.org/21622 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi | supports | FMN + NADH + 2 H(+) =&gt; FMNH2 + NAD(+). Inspected retained body at declared version and exact edge locators. Used on rut-edge-001, rut-edge-002, rut-edge-003, rut-edge-004, rut-edge-005, rut-edge-034, rut-edge-042, rut-edge-048, rut-edge-049. |
| source-18 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/31588 rh:substrates http://rdf.rhea-db.org/31587_L; http://rdf.rhea-db.org/31587_L rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_4063; http://rdf.rhea-db.org/Participant_31587_compound_4063 rh:compound http://rdf.rhea-db.org/Compound_4063; http://rdf.rhea-db.org/Compound_4063 rh:chebi; http://rdf.rhea-db.org/31588 rh:substrates http://rdf.rhea-db.org/31587_L; http://rdf.rhea-db.org/31587_L rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_1829; http://rdf.rhea-db.org/Participant_31587_compound_1829 rh:compound http://rdf.rhea-db.org/Compound_1829; http://rdf.rhea-db.org/Compound_1829 rh:chebi; http://rdf.rhea-db.org/31588 rh:substrates http://rdf.rhea-db.org/31587_L; http://rdf.rhea-db.org/31587_L rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_1650; http://rdf.rhea-db.org/Participant_31587_compound_1650 rh:compound http://rdf.rhea-db.org/Compound_1650; http://rdf.rhea-db.org/Compound_1650 rh:chebi; http://rdf.rhea-db.org/31588 rh:substrates http://rdf.rhea-db.org/31587_L; http://rdf.rhea-db.org/31587_L rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_1198; http://rdf.rhea-db.org/Participant_31587_compound_1198 rh:compound http://rdf.rhea-db.org/Compound_1198; http://rdf.rhea-db.org/Compound_1198 rh:chebi; http://rdf.rhea-db.org/31588 rh:products http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_6882; http://rdf.rhea-db.org/Participant_31587_compound_6882 rh:compound http://rdf.rhea-db.org/Compound_6882; http://rdf.rhea-db.org/Compound_6882 rh:chebi; http://rdf.rhea-db.org/31588 rh:products http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_2613; http://rdf.rhea-db.org/Participant_31587_compound_2613 rh:compound http://rdf.rhea-db.org/Compound_2613; http://rdf.rhea-db.org/Compound_2613 rh:chebi; http://rdf.rhea-db.org/31588 rh:products http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_3484; http://rdf.rhea-db.org/Participant_31587_compound_3484 rh:compound http://rdf.rhea-db.org/Compound_3484; http://rdf.rhea-db.org/Compound_3484 rh:chebi; http://rdf.rhea-db.org/31588 rh:products http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_1283; http://rdf.rhea-db.org/Participant_31587_compound_1283 rh:compound http://rdf.rhea-db.org/Compound_1283; http://rdf.rhea-db.org/Compound_1283 rh:chebi; http://rdf.rhea-db.org/31588 rh:products http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_3249; http://rdf.rhea-db.org/Participant_31587_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/31587 rh:directionalReaction http://rdf.rhea-db.org/31588; http://rdf.rhea-db.org/31588 rh:substrates; rh:products; rh:equation; http://rdf.rhea-db.org/31588 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi; http://rdf.rhea-db.org/31588 rh:products; corresponding rh:contains/rh:compound/rh:chebi | supports | uracil + FMNH2 + NADH + O2 =&gt; (Z)-3-ureidoacrylate + FMN + NAD(+) + H2O + H(+). Inspected retained body at declared version and exact edge locators. Used on rut-edge-006, rut-edge-007, rut-edge-008, rut-edge-009, rut-edge-010, rut-edge-011, rut-edge-012, rut-edge-013, rut-edge-014, rut-edge-035, rut-edge-043, rut-edge-048, rut-edge-049, rut-edge-050. |
| source-19 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/31604 rh:substrates http://rdf.rhea-db.org/31603_L; http://rdf.rhea-db.org/31603_L rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_6882; http://rdf.rhea-db.org/Participant_31603_compound_6882 rh:compound http://rdf.rhea-db.org/Compound_6882; http://rdf.rhea-db.org/Compound_6882 rh:chebi; http://rdf.rhea-db.org/31604 rh:substrates http://rdf.rhea-db.org/31603_L; http://rdf.rhea-db.org/31603_L rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_1283; http://rdf.rhea-db.org/Participant_31603_compound_1283 rh:compound http://rdf.rhea-db.org/Compound_1283; http://rdf.rhea-db.org/Compound_1283 rh:chebi; http://rdf.rhea-db.org/31604 rh:products http://rdf.rhea-db.org/31603_R; http://rdf.rhea-db.org/31603_R rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_6886; http://rdf.rhea-db.org/Participant_31603_compound_6886 rh:compound http://rdf.rhea-db.org/Compound_6886; http://rdf.rhea-db.org/Compound_6886 rh:chebi; http://rdf.rhea-db.org/31604 rh:products http://rdf.rhea-db.org/31603_R; http://rdf.rhea-db.org/31603_R rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_4239; http://rdf.rhea-db.org/Participant_31603_compound_4239 rh:compound http://rdf.rhea-db.org/Compound_4239; http://rdf.rhea-db.org/Compound_4239 rh:chebi; http://rdf.rhea-db.org/31604 rh:products http://rdf.rhea-db.org/31603_R; http://rdf.rhea-db.org/31603_R rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_3249; http://rdf.rhea-db.org/Participant_31603_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/31603 rh:directionalReaction http://rdf.rhea-db.org/31604; http://rdf.rhea-db.org/31604 rh:substrates; rh:products; rh:equation; http://rdf.rhea-db.org/31604 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi; http://rdf.rhea-db.org/31604 rh:products; corresponding rh:contains/rh:compound/rh:chebi | supports | (Z)-3-ureidoacrylate + H2O =&gt; (Z)-3-aminoacrylate + carbamate + H(+). Inspected retained body at declared version and exact edge locators. Used on rut-edge-015, rut-edge-016, rut-edge-017, rut-edge-018, rut-edge-019, rut-edge-036, rut-edge-044, rut-edge-050, rut-edge-051, rut-edge-052. |
| source-20 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/15650 rh:substrates http://rdf.rhea-db.org/15649_L; http://rdf.rhea-db.org/15649_L rh:contains1 http://rdf.rhea-db.org/Participant_15649_compound_4239; http://rdf.rhea-db.org/Participant_15649_compound_4239 rh:compound http://rdf.rhea-db.org/Compound_4239; http://rdf.rhea-db.org/Compound_4239 rh:chebi; http://rdf.rhea-db.org/15650 rh:substrates http://rdf.rhea-db.org/15649_L; http://rdf.rhea-db.org/15649_L rh:contains2 http://rdf.rhea-db.org/Participant_15649_compound_3249; http://rdf.rhea-db.org/Participant_15649_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/15650 rh:products http://rdf.rhea-db.org/15649_R; http://rdf.rhea-db.org/15649_R rh:contains1 http://rdf.rhea-db.org/Participant_15649_compound_1012; http://rdf.rhea-db.org/Participant_15649_compound_1012 rh:compound http://rdf.rhea-db.org/Compound_1012; http://rdf.rhea-db.org/Compound_1012 rh:chebi; http://rdf.rhea-db.org/15650 rh:products http://rdf.rhea-db.org/15649_R; http://rdf.rhea-db.org/15649_R rh:contains1 http://rdf.rhea-db.org/Participant_15649_compound_4391; http://rdf.rhea-db.org/Participant_15649_compound_4391 rh:compound http://rdf.rhea-db.org/Compound_4391; http://rdf.rhea-db.org/Compound_4391 rh:chebi; http://rdf.rhea-db.org/15649 rh:directionalReaction http://rdf.rhea-db.org/15650; http://rdf.rhea-db.org/15650 rh:substrates; rh:products; rh:equation; http://rdf.rhea-db.org/15650 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi | supports | carbamate + 2 H(+) =&gt; NH4(+) + CO2. Inspected retained body at declared version and exact edge locators. Used on rut-edge-020, rut-edge-021, rut-edge-022, rut-edge-023, rut-edge-045, rut-edge-051. |
| source-21 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/34948 rh:substrates http://rdf.rhea-db.org/34947_L; http://rdf.rhea-db.org/34947_L rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_6886; http://rdf.rhea-db.org/Participant_34947_compound_6886 rh:compound http://rdf.rhea-db.org/Compound_6886; http://rdf.rhea-db.org/Compound_6886 rh:chebi; http://rdf.rhea-db.org/34948 rh:substrates http://rdf.rhea-db.org/34947_L; http://rdf.rhea-db.org/34947_L rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_1283; http://rdf.rhea-db.org/Participant_34947_compound_1283 rh:compound http://rdf.rhea-db.org/Compound_1283; http://rdf.rhea-db.org/Compound_1283 rh:chebi; http://rdf.rhea-db.org/34948 rh:substrates http://rdf.rhea-db.org/34947_L; http://rdf.rhea-db.org/34947_L rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_3249; http://rdf.rhea-db.org/Participant_34947_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/34948 rh:products http://rdf.rhea-db.org/34947_R; http://rdf.rhea-db.org/34947_R rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_5274; http://rdf.rhea-db.org/Participant_34947_compound_5274 rh:compound http://rdf.rhea-db.org/Compound_5274; http://rdf.rhea-db.org/Compound_5274 rh:chebi; http://rdf.rhea-db.org/34948 rh:products http://rdf.rhea-db.org/34947_R; http://rdf.rhea-db.org/34947_R rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_1012; http://rdf.rhea-db.org/Participant_34947_compound_1012 rh:compound http://rdf.rhea-db.org/Compound_1012; http://rdf.rhea-db.org/Compound_1012 rh:chebi; http://rdf.rhea-db.org/34947 rh:directionalReaction http://rdf.rhea-db.org/34948; http://rdf.rhea-db.org/34948 rh:substrates; rh:products; rh:equation; http://rdf.rhea-db.org/34948 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi; http://rdf.rhea-db.org/34948 rh:products; corresponding rh:contains/rh:compound/rh:chebi | supports | (Z)-3-aminoacrylate + H2O + H(+) =&gt; 3-oxopropanoate + NH4(+). Inspected retained body at declared version and exact edge locators. Used on rut-edge-024, rut-edge-025, rut-edge-026, rut-edge-027, rut-edge-028, rut-edge-037, rut-edge-046, rut-edge-052, rut-edge-053. |
| source-22 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/26440 rh:substrates http://rdf.rhea-db.org/26438_R; http://rdf.rhea-db.org/26438_R rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_5274; http://rdf.rhea-db.org/Participant_26438_compound_5274 rh:compound http://rdf.rhea-db.org/Compound_5274; http://rdf.rhea-db.org/Compound_5274 rh:chebi; http://rdf.rhea-db.org/26440 rh:substrates http://rdf.rhea-db.org/26438_R; http://rdf.rhea-db.org/26438_R rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_3438; http://rdf.rhea-db.org/Participant_26438_compound_3438 rh:compound http://rdf.rhea-db.org/Compound_3438; http://rdf.rhea-db.org/Compound_3438 rh:chebi; http://rdf.rhea-db.org/26440 rh:substrates http://rdf.rhea-db.org/26438_R; http://rdf.rhea-db.org/26438_R rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_3249; http://rdf.rhea-db.org/Participant_26438_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/26440 rh:products http://rdf.rhea-db.org/26438_L; http://rdf.rhea-db.org/26438_L rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_3378; http://rdf.rhea-db.org/Participant_26438_compound_3378 rh:compound http://rdf.rhea-db.org/Compound_3378; http://rdf.rhea-db.org/Compound_3378 rh:chebi; http://rdf.rhea-db.org/26440 rh:products http://rdf.rhea-db.org/26438_L; http://rdf.rhea-db.org/26438_L rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_5188; http://rdf.rhea-db.org/Participant_26438_compound_5188 rh:compound http://rdf.rhea-db.org/Compound_5188; http://rdf.rhea-db.org/Compound_5188 rh:chebi; http://rdf.rhea-db.org/26438 rh:directionalReaction http://rdf.rhea-db.org/26440; http://rdf.rhea-db.org/26440 rh:substrates; rh:products; rh:equation; http://rdf.rhea-db.org/26440 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi | supports | 3-oxopropanoate + NADPH + H(+) =&gt; 3-hydroxypropanoate + NADP(+). Inspected retained body at declared version and exact edge locators. Used on rut-edge-029, rut-edge-030, rut-edge-031, rut-edge-032, rut-edge-033, rut-edge-039, rut-edge-040, rut-edge-047, rut-edge-053. |
| expression-context | research/pathway_additions/2026-10-11-next-184/imodulondb-context.json; e_coli/precise_mg1655;rutA/b1012,rutB/b1011,rutC/b1010,rutD/b1009,rutE/b1008,rutF/b1007,ydfG/b1539 | context_only | Root used unchanged canonical ImodulonDBClient after runner unavailability. Gene hits and no Rut module-name hits are context only; RutC search also returns YoaB/YjgH family hits. Shared module99/100 summaries concern biotin, not Rut chemistry. |
| authority-final | research/pathway_additions/2026-10-11-next-184/authority-integration.json; Final ontology/source identity metadata and baseline preservation | supports | Canonical authority labels support every Rut identifier; source identity scope may also retain independently verified labels for the separately withheld Kdo candidate, without importing its disputed biological assertions. |
| final-gates | research/pathway_additions/2026-10-11-next-184/integration-validation.json; Actual final command receipts and rehashed retained log bodies | supports | Full repository gates delegated to root; their actual final outcomes are assessed independently from scientific source reading. |
| generated-audit | research/pathway_additions/2026-10-11-next-184/generated-graph-kgx-audit.json; Rut YAML/HTML/SVG/CLI and published KGX | supports | Final artifact audit covers endpoints, all evidence/description preservation and published/CLI equality; no interactive browser assertion. |
| input-recheck | /private/tmp/pathwaymech-next-184-review-rut/input-recheck.json; Initial-to-final inspected input comparison and reassessment | supports | Target frozen bytes unchanged. Every changed shared context input was explicitly compared and relevant Rut identities reassessed before this save. |

## Limits And Additional Notes

- Net Rhea chemistry is a current formal reaction convention; exact elementary RutA/N5-oxide steps are not all enzymatic.
- RutE reaction and FMN requirement remain a qualified prediction; a purified RutE reaction/cofactor assay would resolve specificity. Direct YdfG assays ground the displayed terminal chemistry.
- Physiological support concerns K-12/NCM3722 and stated derivatives near22–23C; no universal37C wild-type or uracil carbon-assimilation claim.
- Native MetaCyc22.5 membership is old; later experimental evidence, not silent synonym replacement, supports the corrected modern mechanism.
- 2020 PMID32066967 complete Results/supplement unavailable in retained publisher access; no detailed target claim depends on uninspected full text.
- YdfG assembly includes inspected native/current structured experimental annotation; this review did not independently acquire full2003/2011 assembly papers cited within UniProt.
- iModulonDB provides expression context only; no Rut module-name hit or accession search failure implies biological absence.
- Full test suite passed on the 187-record draft superset. After withholding the separate Kdo candidate, the final 186-record corpus passed rerendering, full validation, identifier checks, lint and KGX; implementation, tests and Rut scientific bytes did not change.
- No enabled CUA browser surface was available. Actual generated HTML/SVG/KGX were structurally checked; visual rendering and interaction were not inspected.
- No structured predecessor or resolved finding is fabricated. Empty findings applies only to this reviewed frozen Rut target.
- Shared identifier snapshots may retain exact independently verified names for the separately withheld Kdo candidate; that does not certify or export its disputed catalytic graph.
- Initial scratch python3 metadata reads failed due absent system PyYAML/incorrect assumed context shape; re-executed in repository .venv with actual dict shape. These were non-gating reviewer scratch reads and required no record change.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T032530Z-rut-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of uracil degradation III
started_at: '2026-10-11T03:13:39Z'
finished_at: '2026-10-11T03:25:30.336829Z'
reviewer:
  identity: Codex /root/pathway_authority_cache
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Did not author or edit Rut YAML or its author dossiers. Authored
    separate Kdo candidate. Root integrates shared authorities/gates; verify_graph_publication
    authored Rut.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All 53 edges and 92 evidence blocks support the complete corrected Rut pathway
  with explicit prediction, elementary-chemistry and strain/condition limits. Independent
  raw-source and primary-evidence review found no actionable defect. Final required
  repository gates pass.
source:
  git_revision: 3886f14c33d37054dc92e8133bb65aced30ee4ef
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
    sha256: 661ba15fad01d42ad74de3e18d5f90d6aa8829b5c999ae7d7865aa47aa24bcfa
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 01c56339018869d7f5fe65b2f432ad0a5c750d4adbba8425f76947f310cf0322
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 32822e7fdd5194edca3c02ddaa92c4907c1894e59c8a66d07cb99e6eb47003d3
    role: context
  - path: data/pathways/uracil-degradation-iii.yaml
    sha256: ba58586f9b2eb4c29ff6ec99010da3618849dd29d4d023bf2ee82a1c155a4521
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
  - path: pages/records/MetaCyc_PWY0-1471.html
    sha256: a502d25b9e01373fad5ffc6972286cab35412974927c0efed0df36d699c54ba7
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/authority-integration.json
    sha256: f43c42c70de58f21c50d47e933444c77e906429ca6056d6e19a1da326a676d94
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/authority-protein-crosscheck.json
    sha256: a072d287db56a7f1b89edfec20fbf655f862949d0eb7dc80288ea4f855b15993
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/authority-source-inspection.json
    sha256: 60f9ae2644a71813266c22028da8ecae85a11c6c4be77a5365afbb173e620f96
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/baseline-preservation.json
    sha256: 04105cb56160302dcfaef827b4c013ec15025748250684d498f71f784e4a8b11
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/browser-availability.json
    sha256: 144cd5cb3f296b2859cb4c26ddfa43054b1887884101e4267da420618f133228
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/generated-graph-kgx-audit.json
    sha256: 8ae1cd19b62e7bf95e640da133624f1d0465d8d8f62be9e003461bbec3adffa8
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/imodulondb-context.json
    sha256: 1bb951de28d1fa0efe7c2e441432d7abffdd2995a9f97892d553456c8e89d7fe
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/imodulondb-parser-replay.json
    sha256: c82ff2c1db863b3fedf35727749943e94a0a260424131edb2b717922eccf3b11
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/imodulondb-runner-availability.json
    sha256: 77e86bda6a06951103928b4e65039533f60c3254d958cab4bf8dcd8805728c7c
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/imodulondb-source-manifest.json
    sha256: de358d7fcc44f162392e04589c238c5c3649c0b90c8669565a92cba0befec3f5
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/integration-validation.json
    sha256: 9aa62e86c7bc9391cca423ca230a226137d65df7ce48006b23a2087677d81d32
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/publication-scope-audit.json
    sha256: 445e25976da89bdc0c94b15ebe19d1faa592c0b7e2d1dd2f72613479e8aabe02
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/rut-curation.md
    sha256: 5c972bbfd9a93ac8f2f39c349e36b23e8240a0197386b3a8cbb0921ade32c023
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/rut-dedup.json
    sha256: fa7e1fdce08030164c457c28dc58ea5260f225476f46c0313d79720d275d1032
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/rut-identifiers.json
    sha256: 407dbae489147ce457f6a9f66ce1db974431e4ca3f911d5870bfd2b37e000c2d
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/rut-independent-review-audit.json
    sha256: 649b3729f295518364fa8b27f080e5931bb4f94de0fedf74438371b10b280e96
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/rut-replay.py
    sha256: b622ecc55776cf68aff09010fdd1f3350588a6ea0ebbf847c0a369f83fcc4e45
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/rut-source-manifest.json
    sha256: e2b99727da66e674b5163142f80744092762800d687c0385e91d47ecdefdcd4c
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/rut-source-projection.json
    sha256: 4528e60417433b6aaaa46a47d8bde21b39f1e7cc01e7ab39f973b37d81f9a549
    role: context
  - path: research/pathway_additions/2026-10-11-next-184/rut-validation.json
    sha256: 2e8446df65718e37317d67fd0008b58d09b664f45f0c936585e51c07f9bc487c
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: e1d2f085f8e257170a434400265a400ffac07e4aa23b1b830a8fde990ba6a520
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
targets:
- target_id: MetaCyc:PWY0-1471
  path: data/pathways/uracil-degradation-iii.yaml
  label: uracil degradation III
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/uracil-degradation-iii.yaml
    role: maintained pathway mechanism and evidence
  record_class: Pathway
scope:
  description: Full single maintained target:24 participants,6 reactions,53 edges,92
    evidence blocks,22 references.
  selection: Parent assigned a nonauthor independent scientific review; governed inspect
    preceded assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY0-1471
  exclusions:
  - target: Other cohort and baseline pathways
    reason: Only read for identity/boundary and shared integration context; no independent
      scientific verdict on those records.
  - target: Wet-lab reproduction and interactive browser QA
    reason: Not performed or claimed; source review and programmatic artifact audit
      only.
checks:
- check_id: initial-inspect-typo
  name: Superseded initial inspect path attempt
  status: failed
  required: false
  summary: The first command misspelled ontology.json as ontologies.json and failed
    before assessment. Corrected exact existing path on the next inspect; no source
    or record change.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - input-recheck
  command: uv run python scripts/record_review.py inspect ... --input data/identifier_authorities/ontologies.json
  exit_code: 1
  expected_exit_code: 0
- check_id: initial-inspect
  name: Governed inspect before source assessment
  status: passed
  required: true
  summary: Successful initial governed inspect captured frozen ba58586f target before
    full assessment. Final target kind normalized from scratch pathway label to maintained
    schema classification.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - input-recheck
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-184-review-rut/targets.yaml
    --input docs/CAUSAL_GRAPHS.md --input conf/identifier_policy.yaml --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json --input research/pathway_additions/2026-10-11-next-184/rut-curation.md
    --input research/pathway_additions/2026-10-11-next-184/rut-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-184/rut-source-projection.json
    --input research/pathway_additions/2026-10-11-next-184/rut-validation.json
  exit_code: 0
  expected_exit_code: 0
- check_id: independent-1
  name: Independent full-source replay
  status: passed
  required: true
  summary: Independently extracted 86 Rhea nodes and all selected master/directed
    families from full release142 RDF.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - independent-audit
  command: python3 /private/tmp/pathwaymech-next-184-review-rut/extract-rhea.py
  exit_code: 0
  expected_exit_code: 0
- check_id: independent-2
  name: Independent full-source replay
  status: passed
  required: true
  summary: 32 bodies and22 reference digests,33 chemical sides,6 balances,12 exact
    family locators, all6 fresh UniProt identities/pointers, native YdfG assembly,
    spontaneous category, hidden/ignored duplicate searches pass.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - independent-audit
  command: .venv/bin/python /private/tmp/pathwaymech-next-184-review-rut/audit-rut.py
  exit_code: 0
  expected_exit_code: 0
- check_id: publication-exploratory
  name: Superseded exploratory export checks
  status: failed
  required: false
  summary: Reviewer scratch checks initially assumed source_records contained target
    JSON and that all predicate CURIEs used the local namespace. Actual source_records
    contains evidence references; part_of/provides_input_for map to BFO/RO. Corrected
    reviewer check below; no data change.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - generated-audit
  command: .venv/bin/python - (exploratory published TSV checks with incorrect column/predicate
    assumptions)
  exit_code: 1
  expected_exit_code: 0
- check_id: published-replay
  name: Independent actual published Rut projection check
  status: passed
  required: true
  summary: All 53 target edges, 92 evidence blocks, exact descriptions/endpoints and
    documented predicate CURIEs match YAML; 53 page evidence anchors exist and spontaneous
    RHEA15650 exports as BiochemicalReaction.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - generated-audit
  command: .venv/bin/python /private/tmp/pathwaymech-next-184-review-rut/check-published.py
  exit_code: 0
  expected_exit_code: 0
- check_id: final-1
  name: just render-pages
  status: passed
  required: true
  summary: 'Root executed this command; reviewer inspected actual terminal receipt
    and retained log bytes. '
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
- check_id: final-2
  name: just lint
  status: passed
  required: true
  summary: 'Root executed this command; reviewer inspected actual terminal receipt
    and retained log bytes. '
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
- check_id: final-3
  name: git diff --check
  status: passed
  required: true
  summary: 'Root executed this command; reviewer inspected actual terminal receipt
    and retained log bytes. '
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - final-gates
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
- check_id: final-4
  name: just check-identifiers
  status: passed
  required: true
  summary: 'Root executed this command; reviewer inspected actual terminal receipt
    and retained log bytes. '
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  exit_code: 0
  expected_exit_code: 0
- check_id: final-5
  name: just kgx-export --output-dir /private/tmp/pathwaymech-next-184-kgx
  status: passed
  required: true
  summary: 'Root executed this command; reviewer inspected actual terminal receipt
    and retained log bytes. '
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-184-kgx
  exit_code: 0
  expected_exit_code: 0
- check_id: final-6
  name: just validate
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and rehashed log inspected.
    Final 186-record corpus passes native/closed schemas, identifier policy, 10,287
    evidence blocks, 274 history records, 30 sources, six documentation files, research
    contract and current pages.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
- check_id: final-7
  name: just test
  status: passed
  required: true
  summary: 'Root executed full suite: 1,048 passed, 3 skipped and 3 upstream warnings
    in 312.20 seconds. It ran on the 187-record superset before Kdo withdrawal; final
    186-record rendering, validation, identifiers, lint and KGX were rerun. Implementation,
    tests and Rut scientific bytes were unchanged. This is not a claimed second full
    suite on the reduced corpus.'
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
- check_id: final-8
  name: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  status: passed
  required: true
  summary: 'Root executed this command; reviewer inspected actual terminal receipt
    and retained log bytes. '
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - final-gates
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
- check_id: final-inspect
  name: Final input reinspection and byte recheck
  status: passed
  required: true
  summary: All final input hashes verified; any changed context explicitly reassessed,
    stable scientific target unchanged.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - input-recheck
  - target
  - authority-final
  command: .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-184-review-rut/targets.yaml
    (all final local inputs recorded in source)
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: target
  kind: record_content
  reference: data/pathways/uracil-degradation-iii.yaml
  locator: Entire YAML:24 participants,6 reactions,53 edges,92 evidence blocks,22
    references
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Complete exact Rut chemical route with explicit source modernization and
    assay/prediction/strain limits.
  snapshot_sha256: ba58586f9b2eb4c29ff6ec99010da3618849dd29d4d023bf2ee82a1c155a4521
- evidence_id: independent-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-184/rut-independent-review-audit.json
  locator: Independent source replay, all edge groups, primary read receipts, hidden/ignored
    searches
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: All 33 exact chemical sides,6 balances,12 directional-family locators,32
    bodies / 22 reference digests,6 protein entries and native YdfG tetramer were
    independently checked. Eighty-three retained iModulon bodies rehashed; not a fresh
    network call.
  snapshot_sha256: 649b3729f295518364fa8b27f080e5931bb4f94de0fedf74438371b10b280e96
- evidence_id: dedup
  kind: search
  reference: Current worktree and original Documents checkout
  locator: Exact pathway identity, label,proteins, primary PMIDs and uracil-route
    chemistry
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: No pre-existing complete Rut mechanism. Shared carbamate reaction,  inventories
    and uracil-producing nucleoside pathways are distinct.
  search_scope: rg --no-ignore --hidden -l -i -F with exact identifiers/labels/PMIDs;
    both repositories searched, excluding Git internals and installed .venv only.
    Original checkout is older but readable; no claim of whole-computer absence.
  snapshot_sha256: 649b3729f295518364fa8b27f080e5931bb4f94de0fedf74438371b10b280e96
- evidence_id: source-1
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY0-1471
  locator: Exact native identity and stated pathway boundary
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: uracil degradation III. Inspected retained body at declared version and
    exact edge locators. Native identity and boundary context.
  snapshot_sha256: fd49f4ee665e035d8de260dc725fc5af02580945b81f11a641a8a7820a98ea0f
- evidence_id: source-2
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:CPLX0-1962
  locator: Protein[@frameid='CPLX0-1962']/component/Protein; component/coefficient;
    species; Protein[@frameid='CPLX0-1962']/catalyzes/Enzymatic-Reaction[@frameid='ENZRXN0-7359']/reaction
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: 3-hydroxy acid dehydrogenase. Inspected retained body at declared version
    and exact edge locators. Used on rut-edge-038, rut-edge-039.
  snapshot_sha256: ed00ac937d62cc9bc28620be2f1de65744d48c795af0a9efdd11a0c8685c78e6
- evidence_id: source-3
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:EG12345-MONOMER
  locator: Protein[@frameid='EG12345-MONOMER']/dblink; component-of
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: YdfG native subunit identity. Inspected retained body at declared version
    and exact edge locators. Used on rut-edge-038.
  snapshot_sha256: 5722521e0fa986f6bd4846b2dc2fbb80324e3063c60d34cfc2de3b1af58f20ae
- evidence_id: source-4
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:RXN0-5222
  locator: Reaction[@frameid='RXN0-5222']/spontaneous; left; right
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: spontaneous carbamate decomposition. Inspected retained body at declared
    version and exact edge locators. Used on rut-edge-020, rut-edge-021, rut-edge-022,
    rut-edge-023.
  snapshot_sha256: 079f6290beaaa757c83d0ef8fdf3e0eeef3ed2c02cd9aa37f8e469e068b21d36
- evidence_id: source-5
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:RXN-8974
  locator: Exact native identity and stated pathway boundary
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: 3-hydroxypropionate:NADP+ oxidoreductase. Inspected retained body at declared
    version and exact edge locators. Native identity and boundary context.
  snapshot_sha256: ddb5c15214b2047cc5aeae0076f7fc8783861858b628c566363887a83208a824
- evidence_id: source-6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P75893.json
  locator: /comments/1/reaction/reactionCrossReferences; /comments/1/reaction/evidences
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: FMN reductase (NADH) RutF. Inspected retained body at declared version
    and exact edge locators. Used on rut-edge-034.
  snapshot_sha256: 2bd36b7086bfe303be185ba74bf02c2564f4cc63facbc728f3615fe564281fd1
- evidence_id: source-7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P75898.json
  locator: /comments/1/reaction/reactionCrossReferences; /comments/1/reaction/evidences
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Pyrimidine monooxygenase RutA. Inspected retained body at declared version
    and exact edge locators. Used on rut-edge-035.
  snapshot_sha256: d6dd57671d6b310fb05e9de37dfbbd180f6bf25ba48a0a86c28882549613622d
- evidence_id: source-8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P75897.json
  locator: /comments/2/reaction/reactionCrossReferences; /comments/2/reaction/evidences
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Ureidoacrylate amidohydrolase RutB. Inspected retained body at declared
    version and exact edge locators. Used on rut-edge-036.
  snapshot_sha256: 691c608780c38a2e6404384ce0b6d4f1f46746674fa29605926204180c39f9e3
- evidence_id: source-9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AFQ5.json
  locator: /comments/1/reaction/reactionCrossReferences; /comments/1/reaction/evidences
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: 3-aminoacrylate deaminase RutC. Inspected retained body at declared version
    and exact edge locators. Used on rut-edge-037.
  snapshot_sha256: 97e829fb19861b20e28ec7b3d1baaff1ea6763393b46c1428bbdcc2300055457
- evidence_id: source-10
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39831.json
  locator: /comments/7/texts; /comments/5/reaction; /comments/5/physiologicalReactions
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: NADP-dependent 3-hydroxy acid dehydrogenase YdfG. Inspected retained body
    at declared version and exact edge locators. Used on rut-edge-038, rut-edge-039.
  snapshot_sha256: 9c9baf51126ddda9f5d627542c12c7737aed6f4f909e7d9453c71f00e752f528
- evidence_id: source-11
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P75894.json
  locator: /proteinDescription/recommendedName; /comments/0/texts; /comments/1/reaction;
    /comments/2/cofactors/0
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Probable malonic semialdehyde reductase RutE. Inspected retained body at
    declared version and exact edge locators. Used on rut-edge-040, rut-edge-041.
  snapshot_sha256: befb68c7eecba05a370124ec6b079306fd9fd71b1e3ac65e532520e5104170ee
- evidence_id: source-12
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2873085/
  locator: PMC2873085 paragraphs P1-P2; Figure 1; Scheme 1
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Catalysis of a flavoenzyme-mediated amide hydrolysis. Inspected retained
    body at declared version and exact edge locators. Used on rut-edge-034.
  snapshot_sha256: 90d17c95672e67a431a030970ee81d5cca4e94723f85a8bc3aef998c3ea4d31d
- evidence_id: source-13
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2916427/
  locator: PMC2916427 Results section sec18 The RutB reaction; Figure 5B; Table 4;
    PMC2916427 Methods sec13; Results sec18; Table 4; Figure 5C; PMC2916427 Results
    sec24; Discussion sec26
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: 'The Rut Pathway for Pyrimidine Degradation: Novel Chemistry and Toxicity
    Problems. Inspected retained body at declared version and exact edge locators.
    Used on rut-edge-036, rut-edge-039, rut-edge-040.'
  snapshot_sha256: c60789961943bfc9ab58db4ef2315c2cb79aca20744dbbafe6371e551157feb8
- evidence_id: source-14
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6040642/
  locator: PMC6040642 main text following Figure 3; Figure 4A-F; PMC6040642 Figure
    1 legend
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: RutA-Catalyzed Oxidative Cleavage of the Uracil Amide Involves Formation
    of a Flavin-N5-oxide. Inspected retained body at declared version and exact edge
    locators. Used on rut-edge-035, rut-edge-042.
  snapshot_sha256: 0af939b882d577ee4671ef678a2fac3582aa5edbc73a0616b811e944408c3d7c
- evidence_id: source-15
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8113886/fullTextXML
  locator: 'PMC8113886 Results: RutC is a 3-AA deaminase; Figure 2; Table 1; Assay
    for 3-AA deaminase activity; PMC8113886 Figure 1 legend; PMC8113886 Figure 1 and
    legend; Introduction; Results; PMC8113886 Figure 1 and legend'
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: The Rid family member RutC of Escherichia coli is a 3-aminoacrylate deaminase.
    Inspected retained body at declared version and exact edge locators. Used on rut-edge-037,
    rut-edge-040, rut-edge-043, rut-edge-044, rut-edge-045, rut-edge-046, rut-edge-047,
    rut-edge-048, rut-edge-049, rut-edge-050, rut-edge-051, rut-edge-052, rut-edge-053.
  snapshot_sha256: 29c1e99ada2cc0b0b4119f3d734ed2bc155d80acd8ecb730a99c61017118ea34
- evidence_id: source-16
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3515367/
  locator: PMC3515367 Results and discussion 3.1; Figure 2
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Structure of Escherichia coli RutC, a member of the YjgF family and putative
    aminoacrylate peracid reductase of the rut operon. Inspected retained body at
    declared version and exact edge locators. Used on rut-edge-037.
  snapshot_sha256: 925aff4917add679383419b8b1c39a1d4aa0bb6b93ace02fffa8289a01e352bf
- evidence_id: source-17
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/21622 rh:substrates http://rdf.rhea-db.org/21620_R;
    http://rdf.rhea-db.org/21620_R rh:contains1 http://rdf.rhea-db.org/Participant_21620_compound_2613;
    http://rdf.rhea-db.org/Participant_21620_compound_2613 rh:compound http://rdf.rhea-db.org/Compound_2613;
    http://rdf.rhea-db.org/Compound_2613 rh:chebi; http://rdf.rhea-db.org/21622 rh:substrates
    http://rdf.rhea-db.org/21620_R; http://rdf.rhea-db.org/21620_R rh:contains1 http://rdf.rhea-db.org/Participant_21620_compound_1650;
    http://rdf.rhea-db.org/Participant_21620_compound_1650 rh:compound http://rdf.rhea-db.org/Compound_1650;
    http://rdf.rhea-db.org/Compound_1650 rh:chebi; http://rdf.rhea-db.org/21622 rh:substrates
    http://rdf.rhea-db.org/21620_R; http://rdf.rhea-db.org/21620_R rh:contains2 http://rdf.rhea-db.org/Participant_21620_compound_3249;
    http://rdf.rhea-db.org/Participant_21620_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249;
    http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/21622 rh:products
    http://rdf.rhea-db.org/21620_L; http://rdf.rhea-db.org/21620_L rh:contains1 http://rdf.rhea-db.org/Participant_21620_compound_1829;
    http://rdf.rhea-db.org/Participant_21620_compound_1829 rh:compound http://rdf.rhea-db.org/Compound_1829;
    http://rdf.rhea-db.org/Compound_1829 rh:chebi; http://rdf.rhea-db.org/21622 rh:products
    http://rdf.rhea-db.org/21620_L; http://rdf.rhea-db.org/21620_L rh:contains1 http://rdf.rhea-db.org/Participant_21620_compound_3484;
    http://rdf.rhea-db.org/Participant_21620_compound_3484 rh:compound http://rdf.rhea-db.org/Compound_3484;
    http://rdf.rhea-db.org/Compound_3484 rh:chebi; http://rdf.rhea-db.org/21620 rh:directionalReaction
    http://rdf.rhea-db.org/21622; http://rdf.rhea-db.org/21622 rh:substrates; rh:products;
    rh:equation; http://rdf.rhea-db.org/21622 rh:products; corresponding rh:contains/rh:compound/rh:chebi;
    http://rdf.rhea-db.org/21622 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: FMN + NADH + 2 H(+) => FMNH2 + NAD(+). Inspected retained body at declared
    version and exact edge locators. Used on rut-edge-001, rut-edge-002, rut-edge-003,
    rut-edge-004, rut-edge-005, rut-edge-034, rut-edge-042, rut-edge-048, rut-edge-049.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: source-18
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/31588 rh:substrates http://rdf.rhea-db.org/31587_L;
    http://rdf.rhea-db.org/31587_L rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_4063;
    http://rdf.rhea-db.org/Participant_31587_compound_4063 rh:compound http://rdf.rhea-db.org/Compound_4063;
    http://rdf.rhea-db.org/Compound_4063 rh:chebi; http://rdf.rhea-db.org/31588 rh:substrates
    http://rdf.rhea-db.org/31587_L; http://rdf.rhea-db.org/31587_L rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_1829;
    http://rdf.rhea-db.org/Participant_31587_compound_1829 rh:compound http://rdf.rhea-db.org/Compound_1829;
    http://rdf.rhea-db.org/Compound_1829 rh:chebi; http://rdf.rhea-db.org/31588 rh:substrates
    http://rdf.rhea-db.org/31587_L; http://rdf.rhea-db.org/31587_L rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_1650;
    http://rdf.rhea-db.org/Participant_31587_compound_1650 rh:compound http://rdf.rhea-db.org/Compound_1650;
    http://rdf.rhea-db.org/Compound_1650 rh:chebi; http://rdf.rhea-db.org/31588 rh:substrates
    http://rdf.rhea-db.org/31587_L; http://rdf.rhea-db.org/31587_L rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_1198;
    http://rdf.rhea-db.org/Participant_31587_compound_1198 rh:compound http://rdf.rhea-db.org/Compound_1198;
    http://rdf.rhea-db.org/Compound_1198 rh:chebi; http://rdf.rhea-db.org/31588 rh:products
    http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_6882;
    http://rdf.rhea-db.org/Participant_31587_compound_6882 rh:compound http://rdf.rhea-db.org/Compound_6882;
    http://rdf.rhea-db.org/Compound_6882 rh:chebi; http://rdf.rhea-db.org/31588 rh:products
    http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_2613;
    http://rdf.rhea-db.org/Participant_31587_compound_2613 rh:compound http://rdf.rhea-db.org/Compound_2613;
    http://rdf.rhea-db.org/Compound_2613 rh:chebi; http://rdf.rhea-db.org/31588 rh:products
    http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_3484;
    http://rdf.rhea-db.org/Participant_31587_compound_3484 rh:compound http://rdf.rhea-db.org/Compound_3484;
    http://rdf.rhea-db.org/Compound_3484 rh:chebi; http://rdf.rhea-db.org/31588 rh:products
    http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_1283;
    http://rdf.rhea-db.org/Participant_31587_compound_1283 rh:compound http://rdf.rhea-db.org/Compound_1283;
    http://rdf.rhea-db.org/Compound_1283 rh:chebi; http://rdf.rhea-db.org/31588 rh:products
    http://rdf.rhea-db.org/31587_R; http://rdf.rhea-db.org/31587_R rh:contains1 http://rdf.rhea-db.org/Participant_31587_compound_3249;
    http://rdf.rhea-db.org/Participant_31587_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249;
    http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/31587 rh:directionalReaction
    http://rdf.rhea-db.org/31588; http://rdf.rhea-db.org/31588 rh:substrates; rh:products;
    rh:equation; http://rdf.rhea-db.org/31588 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi;
    http://rdf.rhea-db.org/31588 rh:products; corresponding rh:contains/rh:compound/rh:chebi
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: uracil + FMNH2 + NADH + O2 => (Z)-3-ureidoacrylate + FMN + NAD(+) + H2O
    + H(+). Inspected retained body at declared version and exact edge locators. Used
    on rut-edge-006, rut-edge-007, rut-edge-008, rut-edge-009, rut-edge-010, rut-edge-011,
    rut-edge-012, rut-edge-013, rut-edge-014, rut-edge-035, rut-edge-043, rut-edge-048,
    rut-edge-049, rut-edge-050.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: source-19
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/31604 rh:substrates http://rdf.rhea-db.org/31603_L;
    http://rdf.rhea-db.org/31603_L rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_6882;
    http://rdf.rhea-db.org/Participant_31603_compound_6882 rh:compound http://rdf.rhea-db.org/Compound_6882;
    http://rdf.rhea-db.org/Compound_6882 rh:chebi; http://rdf.rhea-db.org/31604 rh:substrates
    http://rdf.rhea-db.org/31603_L; http://rdf.rhea-db.org/31603_L rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_1283;
    http://rdf.rhea-db.org/Participant_31603_compound_1283 rh:compound http://rdf.rhea-db.org/Compound_1283;
    http://rdf.rhea-db.org/Compound_1283 rh:chebi; http://rdf.rhea-db.org/31604 rh:products
    http://rdf.rhea-db.org/31603_R; http://rdf.rhea-db.org/31603_R rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_6886;
    http://rdf.rhea-db.org/Participant_31603_compound_6886 rh:compound http://rdf.rhea-db.org/Compound_6886;
    http://rdf.rhea-db.org/Compound_6886 rh:chebi; http://rdf.rhea-db.org/31604 rh:products
    http://rdf.rhea-db.org/31603_R; http://rdf.rhea-db.org/31603_R rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_4239;
    http://rdf.rhea-db.org/Participant_31603_compound_4239 rh:compound http://rdf.rhea-db.org/Compound_4239;
    http://rdf.rhea-db.org/Compound_4239 rh:chebi; http://rdf.rhea-db.org/31604 rh:products
    http://rdf.rhea-db.org/31603_R; http://rdf.rhea-db.org/31603_R rh:contains1 http://rdf.rhea-db.org/Participant_31603_compound_3249;
    http://rdf.rhea-db.org/Participant_31603_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249;
    http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/31603 rh:directionalReaction
    http://rdf.rhea-db.org/31604; http://rdf.rhea-db.org/31604 rh:substrates; rh:products;
    rh:equation; http://rdf.rhea-db.org/31604 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi;
    http://rdf.rhea-db.org/31604 rh:products; corresponding rh:contains/rh:compound/rh:chebi
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: (Z)-3-ureidoacrylate + H2O => (Z)-3-aminoacrylate + carbamate + H(+). Inspected
    retained body at declared version and exact edge locators. Used on rut-edge-015,
    rut-edge-016, rut-edge-017, rut-edge-018, rut-edge-019, rut-edge-036, rut-edge-044,
    rut-edge-050, rut-edge-051, rut-edge-052.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: source-20
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/15650 rh:substrates http://rdf.rhea-db.org/15649_L;
    http://rdf.rhea-db.org/15649_L rh:contains1 http://rdf.rhea-db.org/Participant_15649_compound_4239;
    http://rdf.rhea-db.org/Participant_15649_compound_4239 rh:compound http://rdf.rhea-db.org/Compound_4239;
    http://rdf.rhea-db.org/Compound_4239 rh:chebi; http://rdf.rhea-db.org/15650 rh:substrates
    http://rdf.rhea-db.org/15649_L; http://rdf.rhea-db.org/15649_L rh:contains2 http://rdf.rhea-db.org/Participant_15649_compound_3249;
    http://rdf.rhea-db.org/Participant_15649_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249;
    http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/15650 rh:products
    http://rdf.rhea-db.org/15649_R; http://rdf.rhea-db.org/15649_R rh:contains1 http://rdf.rhea-db.org/Participant_15649_compound_1012;
    http://rdf.rhea-db.org/Participant_15649_compound_1012 rh:compound http://rdf.rhea-db.org/Compound_1012;
    http://rdf.rhea-db.org/Compound_1012 rh:chebi; http://rdf.rhea-db.org/15650 rh:products
    http://rdf.rhea-db.org/15649_R; http://rdf.rhea-db.org/15649_R rh:contains1 http://rdf.rhea-db.org/Participant_15649_compound_4391;
    http://rdf.rhea-db.org/Participant_15649_compound_4391 rh:compound http://rdf.rhea-db.org/Compound_4391;
    http://rdf.rhea-db.org/Compound_4391 rh:chebi; http://rdf.rhea-db.org/15649 rh:directionalReaction
    http://rdf.rhea-db.org/15650; http://rdf.rhea-db.org/15650 rh:substrates; rh:products;
    rh:equation; http://rdf.rhea-db.org/15650 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: carbamate + 2 H(+) => NH4(+) + CO2. Inspected retained body at declared
    version and exact edge locators. Used on rut-edge-020, rut-edge-021, rut-edge-022,
    rut-edge-023, rut-edge-045, rut-edge-051.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: source-21
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/34948 rh:substrates http://rdf.rhea-db.org/34947_L;
    http://rdf.rhea-db.org/34947_L rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_6886;
    http://rdf.rhea-db.org/Participant_34947_compound_6886 rh:compound http://rdf.rhea-db.org/Compound_6886;
    http://rdf.rhea-db.org/Compound_6886 rh:chebi; http://rdf.rhea-db.org/34948 rh:substrates
    http://rdf.rhea-db.org/34947_L; http://rdf.rhea-db.org/34947_L rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_1283;
    http://rdf.rhea-db.org/Participant_34947_compound_1283 rh:compound http://rdf.rhea-db.org/Compound_1283;
    http://rdf.rhea-db.org/Compound_1283 rh:chebi; http://rdf.rhea-db.org/34948 rh:substrates
    http://rdf.rhea-db.org/34947_L; http://rdf.rhea-db.org/34947_L rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_3249;
    http://rdf.rhea-db.org/Participant_34947_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249;
    http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/34948 rh:products
    http://rdf.rhea-db.org/34947_R; http://rdf.rhea-db.org/34947_R rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_5274;
    http://rdf.rhea-db.org/Participant_34947_compound_5274 rh:compound http://rdf.rhea-db.org/Compound_5274;
    http://rdf.rhea-db.org/Compound_5274 rh:chebi; http://rdf.rhea-db.org/34948 rh:products
    http://rdf.rhea-db.org/34947_R; http://rdf.rhea-db.org/34947_R rh:contains1 http://rdf.rhea-db.org/Participant_34947_compound_1012;
    http://rdf.rhea-db.org/Participant_34947_compound_1012 rh:compound http://rdf.rhea-db.org/Compound_1012;
    http://rdf.rhea-db.org/Compound_1012 rh:chebi; http://rdf.rhea-db.org/34947 rh:directionalReaction
    http://rdf.rhea-db.org/34948; http://rdf.rhea-db.org/34948 rh:substrates; rh:products;
    rh:equation; http://rdf.rhea-db.org/34948 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi;
    http://rdf.rhea-db.org/34948 rh:products; corresponding rh:contains/rh:compound/rh:chebi
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: (Z)-3-aminoacrylate + H2O + H(+) => 3-oxopropanoate + NH4(+). Inspected
    retained body at declared version and exact edge locators. Used on rut-edge-024,
    rut-edge-025, rut-edge-026, rut-edge-027, rut-edge-028, rut-edge-037, rut-edge-046,
    rut-edge-052, rut-edge-053.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: source-22
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/26440 rh:substrates http://rdf.rhea-db.org/26438_R;
    http://rdf.rhea-db.org/26438_R rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_5274;
    http://rdf.rhea-db.org/Participant_26438_compound_5274 rh:compound http://rdf.rhea-db.org/Compound_5274;
    http://rdf.rhea-db.org/Compound_5274 rh:chebi; http://rdf.rhea-db.org/26440 rh:substrates
    http://rdf.rhea-db.org/26438_R; http://rdf.rhea-db.org/26438_R rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_3438;
    http://rdf.rhea-db.org/Participant_26438_compound_3438 rh:compound http://rdf.rhea-db.org/Compound_3438;
    http://rdf.rhea-db.org/Compound_3438 rh:chebi; http://rdf.rhea-db.org/26440 rh:substrates
    http://rdf.rhea-db.org/26438_R; http://rdf.rhea-db.org/26438_R rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_3249;
    http://rdf.rhea-db.org/Participant_26438_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249;
    http://rdf.rhea-db.org/Compound_3249 rh:chebi; http://rdf.rhea-db.org/26440 rh:products
    http://rdf.rhea-db.org/26438_L; http://rdf.rhea-db.org/26438_L rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_3378;
    http://rdf.rhea-db.org/Participant_26438_compound_3378 rh:compound http://rdf.rhea-db.org/Compound_3378;
    http://rdf.rhea-db.org/Compound_3378 rh:chebi; http://rdf.rhea-db.org/26440 rh:products
    http://rdf.rhea-db.org/26438_L; http://rdf.rhea-db.org/26438_L rh:contains1 http://rdf.rhea-db.org/Participant_26438_compound_5188;
    http://rdf.rhea-db.org/Participant_26438_compound_5188 rh:compound http://rdf.rhea-db.org/Compound_5188;
    http://rdf.rhea-db.org/Compound_5188 rh:chebi; http://rdf.rhea-db.org/26438 rh:directionalReaction
    http://rdf.rhea-db.org/26440; http://rdf.rhea-db.org/26440 rh:substrates; rh:products;
    rh:equation; http://rdf.rhea-db.org/26440 rh:substrates; corresponding rh:contains/rh:compound/rh:chebi
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: 3-oxopropanoate + NADPH + H(+) => 3-hydroxypropanoate + NADP(+). Inspected
    retained body at declared version and exact edge locators. Used on rut-edge-029,
    rut-edge-030, rut-edge-031, rut-edge-032, rut-edge-033, rut-edge-039, rut-edge-040,
    rut-edge-047, rut-edge-053.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: expression-context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-184/imodulondb-context.json
  locator: e_coli/precise_mg1655;rutA/b1012,rutB/b1011,rutC/b1010,rutD/b1009,rutE/b1008,rutF/b1007,ydfG/b1539
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: context_only
  summary: Root used unchanged canonical ImodulonDBClient after runner unavailability.
    Gene hits and no Rut module-name hits are context only; RutC search also returns
    YoaB/YjgH family hits. Shared module99/100 summaries concern biotin, not Rut chemistry.
  snapshot_sha256: 1bb951de28d1fa0efe7c2e441432d7abffdd2995a9f97892d553456c8e89d7fe
- evidence_id: authority-final
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-184/authority-integration.json
  locator: Final ontology/source identity metadata and baseline preservation
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Canonical authority labels support every Rut identifier; source identity
    scope may also retain independently verified labels for the separately withheld
    Kdo candidate, without importing its disputed biological assertions.
  snapshot_sha256: f43c42c70de58f21c50d47e933444c77e906429ca6056d6e19a1da326a676d94
- evidence_id: final-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-184/integration-validation.json
  locator: Actual final command receipts and rehashed retained log bodies
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Full repository gates delegated to root; their actual final outcomes are
    assessed independently from scientific source reading.
  snapshot_sha256: 9aa62e86c7bc9391cca423ca230a226137d65df7ce48006b23a2087677d81d32
- evidence_id: generated-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-184/generated-graph-kgx-audit.json
  locator: Rut YAML/HTML/SVG/CLI and published KGX
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Final artifact audit covers endpoints, all evidence/description preservation
    and published/CLI equality; no interactive browser assertion.
  snapshot_sha256: 8ae1cd19b62e7bf95e640da133624f1d0465d8d8f62be9e003461bbec3adffa8
- evidence_id: input-recheck
  kind: validation
  reference: /private/tmp/pathwaymech-next-184-review-rut/input-recheck.json
  locator: Initial-to-final inspected input comparison and reassessment
  accessed_at: '2026-10-11T03:25:06.812091Z'
  support: supports
  summary: Target frozen bytes unchanged. Every changed shared context input was explicitly
    compared and relevant Rut identities reassessed before this save.
  snapshot_sha256: 0ca9bf1721046be465a5d1a551d78fc73787422c39d7c9bf9306e53209419fb4
assessments:
- assessment_id: identity
  area: identity
  topic: Exact complete modern Rut pathway
  outcome: supported
  summary: MetaCyc PWY0-1471 is the exact uracil degradation III route. GO:0006212
    is broader. Six selected reactions retain the whole uracil-to-3HP/2NH4/CO2 boundary
    with flavin recycling; obsolete native peracid/RutC/RutD assignments are explicitly
    superseded by inspected primary evidence, not silently treated as equivalent chemistry.
    Upstream transport, nucleoside cleavage, thymine and regulation are outside this
    boundary.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - dedup
  - independent-audit
  - source-1
  - source-15
- assessment_id: chemistry
  area: grounding
  topic: All chemical sides, directions and balances
  outcome: supported
  summary: Independent full Rhea 142 replay checks all 33 source sides and coefficient-specific
    triple chains against actual YAML. Four left-to-right and two right-to-left members
    match their masters; all 6 atom/charge balances and complete net pass with ChEBI
    formulas. Explicit 31604 plus spontaneous 15650 avoids duplicate net 42624. Net
    31588 includes spontaneous flavin-N5-oxide reduction without attributing every
    elementary step to RutA.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - independent-audit
  - source-17
  - source-18
  - source-19
  - source-20
  - source-21
  - source-22
- assessment_id: catalysis
  area: evidence
  topic: Measured functional activities and physical assembly
  outcome: supported
  summary: RutA/F, B, C and YdfG are supported at their declared experimental scopes.
    RutF primary material was partially purified and Fre substituted in vitro. RutC
    deaminase has a 2021 inactive-mutant/background control; its homotrimer has 2012
    physical evidence. Native YdfG contains four copies of EG12345/P39831 with exact
    enzyme-reaction link and current experimental assembly annotation. Qualified enables
    assertions do not establish monomer sufficiency.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - independent-audit
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
  - source-9
  - source-10
  - source-11
  - source-12
  - source-13
  - source-14
  - source-15
  - source-16
  - source-17
  - source-18
  - source-19
  - source-20
  - source-21
  - source-22
- assessment_id: prediction
  area: evidence
  topic: Explicit RutE uncertainty
  outcome: supported
  summary: RutE reduction is genetic/current-annotation prediction, not a purified-enzyme
    assay or established NADPH specificity. Its FMN code is curator inference ECO:0000305.
    Both are explicitly described as probable and not contradicted by inspected experiments;
    measured YdfG independently grounds the displayed terminal chemical conversion.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - independent-audit
  - source-11
  - source-13
  - source-15
  dimensions:
  - name: evidence-tier
    value: RutE predicted; YdfG measured
    definition: Avoid upgrading function/genetic or curator evidence to experimental
      exact reaction/cofactor specificity.
    evidence_ids:
    - independent-audit
    - source-11
- assessment_id: taxon
  area: scope
  topic: K-12 strain and temperature limits
  outcome: supported
  summary: All 6 full reviewed proteins are taxon 83333; native YdfG assembly is MG1655.
    Primary NCM3722 and derivatives ground K-12 pathway support at the stated room-temperature
    conditions. This is not universal 37°C growth, uracil carbon assimilation, or
    proof of essential RutC/RutD. Modern polarity-controlled experiments explicitly
    qualify earlier deletion interpretations.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - independent-audit
  - source-13
  - source-15
  dimensions:
  - name: taxon-condition
    value: E. coli K-12; NCM3722 and derivatives near 22–23°C; native MG1655 annotation
    definition: Organism and assay/growth limits actually supported by the inspected
      sources.
    evidence_ids:
    - target
    - independent-audit
- assessment_id: graph
  area: graph
  topic: Every endpoint, role, dependency and exported evidence
  outcome: supported
  summary: All 53 edges have local endpoints and source references. Carbamate decay
    remains a biochemical reaction without an enzyme or molecular-activity override.
    Six dependencies reflect shared chemicals and primary topology, not channeling
    or physical complexes. Generated artifact checks preserve descriptions and all
    92 evidence blocks.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - independent-audit
  - generated-audit
- assessment_id: context
  area: evidence
  topic: iModulon expression context
  outcome: supported
  summary: The canonical adapter fallback and 83 exact body rehashes support only
    dataset/gene-context observations. No Rut module-name hits and accession misses
    are not negative biology; YoaB/YjgH product substrings are not RutC mechanism
    support.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - expression-context
  - independent-audit
- assessment_id: provenance
  area: provenance
  topic: Versioned native objects, reference bodies and final gates
  outcome: supported
  summary: All 22 references map to exact retained source bodies and declared hashes;
    all 32 acquired bodies independently rehashed. Current UniProt pointers and 12
    directional-family locators exist. Final shared identity artifacts and gate/log
    hashes rechecked on frozen Rut; deterministic checks supplement full scientific
    assessment.
  target_ids:
  - MetaCyc:PWY0-1471
  evidence_ids:
  - target
  - independent-audit
  - authority-final
  - final-gates
  - input-recheck
findings: []
actions: []
limitations:
- Net Rhea chemistry is a current formal reaction convention; exact elementary RutA/N5-oxide
  steps are not all enzymatic.
- RutE reaction and FMN requirement remain a qualified prediction; a purified RutE
  reaction/cofactor assay would resolve specificity. Direct YdfG assays ground the
  displayed terminal chemistry.
- Physiological support concerns K-12/NCM3722 and stated derivatives near22–23C; no
  universal37C wild-type or uracil carbon-assimilation claim.
- Native MetaCyc22.5 membership is old; later experimental evidence, not silent synonym
  replacement, supports the corrected modern mechanism.
- 2020 PMID32066967 complete Results/supplement unavailable in retained publisher
  access; no detailed target claim depends on uninspected full text.
- YdfG assembly includes inspected native/current structured experimental annotation;
  this review did not independently acquire full2003/2011 assembly papers cited within
  UniProt.
- iModulonDB provides expression context only; no Rut module-name hit or accession
  search failure implies biological absence.
- Full test suite passed on the 187-record draft superset. After withholding the separate
  Kdo candidate, the final 186-record corpus passed rerendering, full validation,
  identifier checks, lint and KGX; implementation, tests and Rut scientific bytes
  did not change.
- No enabled CUA browser surface was available. Actual generated HTML/SVG/KGX were
  structurally checked; visual rendering and interaction were not inspected.
notes:
- No structured predecessor or resolved finding is fabricated. Empty findings applies
  only to this reviewed frozen Rut target.
- Shared identifier snapshots may retain exact independently verified names for the
  separately withheld Kdo candidate; that does not certify or export its disputed
  catalytic graph.
- Initial scratch python3 metadata reads failed due absent system PyYAML/incorrect
  assumed context shape; re-executed in repository .venv with actual dict shape. These
  were non-gating reviewer scratch reads and required no record change.
tags:
- independent-scientific-review
- uracil-catabolism
- rut
- source-replay
```
