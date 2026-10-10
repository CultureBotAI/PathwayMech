# Tetrahydromonapterin biosynthesis: supported modules with an unresolved step

Author curation under `.claude/skills/add-pathway/SKILL.md`, 2026-10-10. This is an author evidence ledger, not an independent scientific review. The record is `data/pathways/tetrahydromonapterin-biosynthesis.yaml`, identified by **MetaCyc:PWY0-1433**. Its full mechanism is deliberately incomplete: supported FolE/FolX chemistry and FolM chemistry are retained, but no asserted reaction connects dihydromonapterin triphosphate to dihydromonapterin.

## Identity and novelty

The public MetaCyc 22.5 XML explicitly identifies this pathway, its four native reactions, MG1655 scope and the hypothetical reaction RXN0-6368. PathBank's independently inspected primary archive member PW002043.owl identifies SMP0002057, the same named E. coli pathway, with four reactions and three catalysis objects. The selected record identity follows the skill's preference for an exact curated MetaCyc definition. The inspected GO label search returned monapterin molecular activities, but no exact monapterin biological-process label; it does not establish that all possible ontology synonyms were searched.

Fresh exact-accession, label, synonym, reaction, protein, PMID and DOI searches covered both the working tree and original repository with `rg --no-ignore --hidden`. Only `.git` internals, the installed `.venv`, and bytecode were excluded. No pre-existing maintained exact pathway was found. Prior native inventories and triage were read, and the follow-up search distinguishes those hits and the newly written draft. Raw commands, hits, digests and search limits are recorded in `monapterin-search-ledger.json`. This is bounded novelty, not an exhaustive coverage claim.

## Scientific disposition

The pathway's existence has experimental support, while the exact intervening dephosphorylation does not. The original study ([PMID19897652](https://pmc.ncbi.nlm.nih.gov/articles/PMC2805310/)) provides genetic complementation and purified-FolM evidence. Pterin profiling used MG1655 and iodine oxidation before HPLC; the redox state of secreted pterins was uncertain. Complementation used the K-12 tyrA strain JP2255 expressing heterologous Pseudomonas PhhA/PhhB. These experiments are not reassigned to one strain or interpreted as endogenous E. coli phenylalanine hydroxylation. The record therefore uses K-12 taxonomic scope and states the MG1655 grounding of native assembly identities.

MetaCyc lists RXN0-6368 under `hypothetical-reactions`. Its exact native reaction XML unifies to directed RHEA:34844: CHEBI:61186 + 3 CHEBI:15377 → CHEBI:71175 + 3 CHEBI:43474 + 2 CHEBI:15378. The equation is retained only in the research projection, with its coefficients. An authoritative reaction identifier establishes chemical identity; it does not establish the biological enzyme, intermediate sequence, or measured phosphate-release mechanism. No unknown phosphatase node, fabricated catalyst, net dephosphorylation reaction, or FolX-to-FolM connecting edge is introduced. Generic water/proton participation does not constitute a pathway-intermediate bridge. Reaction membership and gene-enables evidence support the pathway, not the missing chemistry.

Later primary literature was checked beyond the original abstract:

- [PMID28223385](https://pmc.ncbi.nlm.nih.gov/articles/PMC5404538/) examines `nudB` deletion and suppression by `folX`/`folM` disruption. NudB acts on the competing dihydroneopterin/folate branch. The genetics do not identify a monapterin phosphatase, and proposed pterin flux changes were not direct metabolite measurements.
- [DOI10.1128/aem.00814-24](https://pmc.ncbi.nlm.nih.gov/articles/PMC11267939/) identifies Lreu_1276/FolQ3 as a dihydroneopterin-triphosphate pyrophosphohydrolase in Limosilactobacillus. Reaction-product stoichiometry and Table 1 were inspected. Dihydromonapterin triphosphate was not among the tested substrates; no positive or negative activity inference is made for it.
- [PMID39603333](https://pubmed.ncbi.nlm.nih.gov/39603333/) concerns engineered N-methylserotonin production. Its abstract and available publisher excerpt do not resolve the enzyme. Direct publisher access returned 403, so full-text inspection is not claimed.

These bounded results justify the supported incomplete record. They do not prove no later phosphatase evidence exists anywhere. A future identified enzyme or directly measured dephosphorylation mechanism can justify extending the graph after fresh review. If hypothetical reactions are later displayed, a genuine evidence-status contract would be needed because current KGX edges carry `knowledge_assertion`.

## Exact enzyme and chemistry evidence

All three selected Rhea directions are left-to-right: 17474 (master 17473), 28347 (master 28346), and 34848 (master 34847). Official release 142 RDF and the direction TSV were read independently. The RDF uses `directionalReaction` for left/right directions and `bidirectionalReaction` for 28349, the native FolX cross-reference. All 12 selected side occurrences have coefficient 1 and balance for elements and charge. FolX reversibility is retained in text; its biosynthetic direction is selected explicitly.

MetaCyc:FOLE-CPLX and FOLXTET-CPLX provide exact assembly identifiers, coefficients 10 and 8, respectively, and native component-monomer links. Independently fetched monomer XML explicitly unifies to UniProtKB:P0A6T5 and P0AC19. Reviewed protein records, primary assembly abstracts and both source-native assemblies agree on the selected subunit counts. PMID9182560's earlier probable hexamer estimate is preserved as a historical conflict; PMID9651328 and PMID10378270 support the FolX octamer. PMID12297008 supports the FolE pentamer of five dimers. The awkward UniProt FolE phrase about two pentamers is not multiplied into 20 subunits.

The [full primary zinc paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC17616/) was inspected. Its E. coli analysis identifies bound active-site zinc and measures 0.9 ± 0.1 zinc ions per subunit. CHEBI:29105 is therefore an enzyme cofactor, with direct primary support, not a conclusion drawn only from assay additives. FolE's reviewed catalytic comment and zinc features lack explicit experimental ECO tags; that absence is retained. FolX catalytic annotation and FolM's specific dihydromonapterin catalytic annotation explicitly carry ECO:0000269, preserved in their evidence assertions. FolM's separate dihydrofolate reaction is not substituted for the selected reaction.

The sole record quotation is 8 words, matched literally against the full primary body. Primary statements were paraphrased as located assertions, never presented as database-generated quotations. FolM assay conditions and NADPH dependence are bounded to the inspected experiments.

ChEBI255 structures independently distinguish the correct pterin CHEBI:71175 (C9H13N5O4) from native PathBank Compound/PW_C011995, dihydromethysticin (C15H16O5). The latter's native CHEBI1034670/PubChem229852 identifiers are retained as rejected source facts, not repaired by an assumed obsolete-ID mapping. Current CHEBI:182794 corroborates the unrelated dihydromethysticin structure. Exact charged Rhea chemical forms are used, and CHEBI:71177's unspecified ring-C6 configuration remains unspecified; side-chain stereochemistry is retained.

## Boundaries and access limits

No compartment is asserted without inspected support. No FolB alternative, folate branch, queuosine branch, Pseudomonas hydroxylation, broad antimicrobial susceptibility mechanism, or quinonoid-pterin recycling is added. The physiological downstream role in native E. coli is not assigned. A typo describing final “oxidation” in old MetaCyc FolX prose does not override measured FolM reduction and Rhea chemistry.

The canonical iModulonDB dataset inventory and `folX`/`folM` searches were inspected. The MG1655 dataset returns b2303 and b1606, one gene per query and zero iModulon hits. These are computational gene-context results, not direct catalytic evidence or evidence that regulation is absent.

Full primary article text was available for PMC2805310 and PMC17616. Relevant full-text sections of PMC5404538 and PMC11267939 were inspected. PMID9182560,9651328,10378270 and12297008 were read as primary abstracts only. Figure captions were inspected; no figure-pixel or supplementary-material inspection is claimed. The public MetaCyc export is 22.5, not a claim of access to the latest licensed release. Europe PMC fullTextXML for PMC2805310 failed with 500, but direct PMC HTML succeeded. Two exploratory mistaken-ID responses were rejected after metadata inspection and are explicitly unused. Successful source bodies, exact URL/date/version/hash scopes and failures are retained externally; no cookies or session headers are committed.

## Author verification

`monapterin-validation.json` records narrow native and closed-schema checks, direct authority-label replay, all 12 Rhea side occurrences, atom/charge balance, literal quotation matching, exact source-body hashes and actual KGX preservation. It explicitly checks that dihydromonapterin triphosphate has no consuming edge and dihydromonapterin has no producing edge, preserving the unresolved gap. An early draft used an undeclared evidence-code field; the closed-schema check rejected it, and source ECO codes were moved into supported evidence text before final verification. This draft correction is not represented as a post-review finding.

Root owns shared snapshots, generated artifacts, history, full corpus gates and the independent review. Their results are not preclaimed here. This author ledger does not substitute for that review.
