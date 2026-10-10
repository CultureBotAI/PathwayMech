# Three remaining pathway leads: bounded research handoff

Research date: 2026-10-10. Baseline commit: `5766cf2fe227afc248a72e455f74f4c5ddda9d97` (161 maintained pathway records). This is candidate research, not a saved scientific review of a record. No records were created for these three candidates.

| Exact native candidate | Disposition | Next bounded action |
| --- | --- | --- |
| PathBank:SMP0002057, PW002043.owl, tetrahydromonapterin biosynthesis | Valid multi-enzyme route; archived compound is wrong and independent MetaCyc flags a hypothetical step. | Inspect exact MetaCyc:RXN0-6368 and subsequent phosphatase evidence; decide whether an explicitly incomplete/hypothetical-step graph is appropriate. |
| PathBank:SMP0002111, PW002099.owl, cyanate degradation | Strong next curation candidate after correcting catalyst, charge-form and spontaneous-step scope. | Verify complete native/Rhea equations, then represent the CynS+CynT bicarbonate-recycling cycle with its atmospheric-CO2 condition. |
| PathBank:SMP0001910, PW001896.owl, curcumin degradation | Real two-step CurA conversion, excluded by the current single-enzyme boundary. | Retain evidence; reconsider only after an explicit scope change or evidence for a distinct broader multi-enzyme route. |

## Tetrahydromonapterin: a source error and a genuine evidence gap

The archived route has four reactions and three enzyme identities: FolE/P0A6T5, FolX/P0AC19 and FolM/P0AFS3. Both the product of `Reactions/5966` and substrate of `Reactions/5967` are the native object `Compound/PW_C011995`, explicitly **dihydromethysticin**, formula C15H16O5, CHEBI1034670 and PubChem229852. Thus this is not merely an incorrect display label. Current [PubChem229852](https://pubchem.ncbi.nlm.nih.gov/compound/229852) and CHEBI182794 confirm the unrelated dihydromethysticin structure. Failed current requests for CHEBI1034670 do not establish a formal obsolete/replacement relationship.

Independent [MetaCyc:PWY0-1433 XML](https://pathway.yeastgenome.org/getxml?META:PWY0-1433) gives the correct pterin intermediate CPD-11770; reviewed [FolM](https://www.uniprot.org/uniprotkb/P0AFS3/entry) links dihydromonapterin CHEBI71175 to tetrahydromonapterin CHEBI71177. Their formulas are C9H13N5O4 and C9H15N5O4. The inspected [primary abstract, PMID19897652](https://pubmed.ncbi.nlm.nih.gov/19897652/), supports FolX/FolM genetics and purified FolM activity, but does not identify the dephosphorylating enzyme.

Crucially, the independent MetaCyc22.5 pathway explicitly lists **RXN0-6368 under `hypothetical-reactions`**. Correcting the wrong compound does not make the whole route experimentally complete. Future curation must preserve that gap; no phosphatase or catalytic evidence should be invented. The Pseudomonas phenylalanine-hydroxylase cofactor role in the paper must not be transferred to E. coli.

## Cyanate: retain the two-enzyme cycle, repair its native details

The native graph has three chemical reactions plus CynX-associated transport. [MetaCyc:CYANCAT-PWY XML](https://pathway.yeastgenome.org/getxml?META:CYANCAT-PWY) independently defines a cycle: cyanase produces carbamate and CO2; carbamate spontaneously decomposes; carbonic anhydrase replenishes bicarbonate. In [PMID8444806](https://pubmed.ncbi.nlm.nih.gov/8444806/), loss of CynT blocked cyanate use at 0.03%CO2 despite active cyanase, while 3%CO2 rescued the phenotype. This supports a bounded two-enzyme pathway rather than only an isolated cyanase reaction.

The following archive details cannot be copied uncritically:

- `ProteinComplex/1171` combines CynT/P0ABE9 and Can/P61517. Reviewed entries and [PMID1740425](https://pubmed.ncbi.nlm.nih.gov/1740425/), [PMID11316870](https://pubmed.ncbi.nlm.nih.gov/11316870/) and [PMID14563877](https://pubmed.ncbi.nlm.nih.gov/14563877/) support separate carbonic anhydrases and condition-dependent substitution, not this mixed assembly.
- `Reactions/5907` has no enzyme but says `spontaneous=false`. The independent pathway explicitly describes spontaneous carbamate decomposition. Its neutral carbamic-acid object CHEBI28616 must also be reconciled with charged carbamate chemistry and proton coefficients before curation.
- The native CynX/P17583 transport assignment and the current UniProt function annotation exceed the inspected primary study's resolved role: PMID8444806 found no effect of CynX mutations on the tested traits and called its physiological function unknown. Preserve the evidence difference; it does not prove that transport is impossible.
- Rhea11120 is net cyanase chemistry. Do not count it and its explicit intermediate decomposition as separate additional fluxes. [PMID3110153](https://pubmed.ncbi.nlm.nih.gov/3110153/) establishes bicarbonate as substrate and supports the carbamate intermediate.

The shared carbamate decomposition is already represented as RHEA15650 in `data/pathways/l-arginine-degradation-v.yaml`; it does not duplicate the cyanate recycling pathway. Exact full reaction objects and Rhea directions/coefficients still need inspection. MetaCyc pathway layouts list primary reactants, not complete balanced equations.

## Curcumin: biological validity differs from record eligibility

Both native reductions have the same CurA/P76113 homodimer catalyst. The [primary abstract, PMID21467222](https://pubmed.ncbi.nlm.nih.gov/21467222/), describes an enzyme purified from a human-fecal E. coli isolate that performs both curcumin→dihydrocurcumin→tetrahydrocurcumin reductions. Reviewed [UniProt P76113](https://www.uniprot.org/uniprotkb/P76113/entry) assigns both activities to the same K-12 protein with experimental evidence. Rhea34819 and34811 represent the successive conversions;34815 is their net equation, not another independent step. The experimental isolate was not resolved as K-12 from the abstract.

The current [add-pathway skill](../../../.claude/skills/add-pathway/SKILL.md) explicitly excludes “single enzymes.” This handoff interprets that boundary as excluding the inspected two-reaction, one-enzyme CurA route. It does not reject the experimental chemistry or manufacture a second enzyme to meet the rule.

## Coverage and reproducibility

The [source manifest](triage-source-manifest.json) records URLs, retrieval dates, sanitized headers, hashes, failures and external raw paths. Native object projections preserve source claims and errors; the three `triage-*-assessment.json` files separate facts, sources, dispositions and next actions. Exact extracted native SHA256 values are:

- PW002043.owl: `03f2f79e67f9cfc36a279d2bc1c409d75df5b5a5c5952f830422f490429f635f`
- PW002099.owl: `d8616300c7c407dffc277f8247cfc95ea3a9f9c6ad4a3ef4dcd8dc2f3bfec604`
- PW001896.owl: `becce110780d247444c98ee0ed16b36e4d5f5ab9a9e61ba4201f82d3b36ebcbe`

Actual inspection covered three native pathway definitions, nine biochemical reactions, one transport, all eight native protein identities and four native complexes; eight fresh reviewed UniProt records; seven complete indexed primary abstracts; two independent MetaCyc pathway XML definitions; and current ChEBI/PubChem identity checks. UniProt reports release2026_03. The retrieved MetaCyc definitions report22.5. Native PathBank names E. coli taxon562; UniProt entries use K-12 taxon83333 and the independent MetaCyc E. coli definitions use MG1655 taxon511145. These scopes remain distinct.

No complete primary article was obtained. EuropePMC full-text requests failed; NCBI BioC requests returned HTML error pages despite successful HTTP responses. Those files are logged as access errors and were not treated as full text. This bounded pass did not independently audit every Rhea side/coefficient, later literature, all archive variants, or the other525 frozen screening rows.

[Duplicate-search receipts](triage-duplicate-searches.json) include ignored and hidden files in both the entire worktree and original repository, excluding Git internals, virtual environments and bytecode. Exact pathway, protein, defining reaction and paper searches found prior research/ledger mentions but no maintained target records. Additional reaction searches exposed the shared arginine-route reaction above. The frozen528-row screening ledger remains unchanged; each assessment retains its exact matching row. No pathway-exhaustion claim follows from this three-candidate triage.

Only JSON parsing, artifact hash/projection consistency and formatting checks were run for this research handoff; no full repository gates or new structured scientific reviews were run by this agent.
