# Adenine and adenosine salvage I

## Exact pathway and decision

The selected record is **MetaCyc:P121-PWY**, the complete two-reaction route from adenosine through adenine to AMP. Fresh original MetaCyc 22.5 XML contains exactly ADENPHOSPHOR-RXN (L2R) and ADENPRIBOSYLTRAN-RXN (R2L), with the former preceding the latter. The current record selects RHEA:27643 and RHEA:16611, respectively. The issuing-source labels are not inferred from legacy PathBank numeric names.

This is a separate exact pathway after rejection of the Glutathione Metabolism III map. That rejection and the original seven biochemical plus four transport conversions are preserved in `glutathione-*`; no convenient subset was substituted as its full boundary.

GO:0006168 denotes generation of adenine; GO:0006169 denotes generation of adenosine; GO:0006166 denotes purine nucleoside production. Their inspected definitions do not describe this complete AMP-producing two-step route. The native MetaCyc identifier gives the narrower exact boundary.

Hidden- and ignored-inclusive searches in both the worktree and original checkout, plus a baseline 192-record semantic comparison, found no maintained P121-PWY route. The exact queries and explicit excluded implementation/generated directories are in the dedup ledger. The previous cohort's salvage III dossier already distinguished P121-PWY as a different variant; those earlier research mentions are retained, not mistaken for absence of prior research. The existing complete salvage III record converts adenine through adenosine, inosine and hypoxanthine to IMP. P121 uses the opposite selected DeoD direction and the distinct Apt AMP-forming reaction. Purine deoxyribonucleoside degradation, yeast de novo AMP synthesis, periplasmic NAD breakdown and methionine salvage have different substrates or endpoints.

The legacy PathBank variants were fully inspected for identification, not silently relabeled: PW002071/SMP0002083 (“II”) has three biochemical steps matching the current PWY-6611 (“V”) core plus adenine transport. PW002072/SMP0002084 (“III”) combines adenosine hydrolysis, Apt, AMP hydrolysis and transport; it is not the phosphorolysis pathway P121. Current PWY-6605 (“II”) explicitly defines the distinct two-step nucleoside-hydrolase route.

## Organism and physiological scope

The native P121 species list includes Halobacterium salinarum, human and Mycoplasma pneumoniae; it does **not** list E. coli. This is not concealed or converted into source-reported E. coli pathway membership. The curated K-12 enzyme implementation is independently supported by current reviewed proteins P0ABP8 (deoD/pup, b4384) and P69503 (apt, b0469), exact native E. coli enzyme frames, and the primary E. coli salvage scheme (Jochimsen et al. 1975, PMID765747, p.85 Fig.1). Table1 identifies the K-12 derivatives; they are not indiscriminately relabeled as MG1655 experiments.

The 1975 PDF was inspected as text and its actual Figure1 page image was inspected to check the two arrows and numbered enzyme legend. Its proposed adenosine kinase branch is not imported into P121. The 2018 DeoD paper (PMID30337572/PMC6193948) independently assays adenosine phosphorolysis and describes the functional hexamer. The 2011 Apt paper (PMID21111048/PMC4125576) uses His-tagged recombinant E. coli protein expressed in BL21(AI); it is activity evidence for that construct, not proof of complete wild-type pathway flux or a particular MG1655 sequence assay.

The full 2022 paper (PMID35575513/PMC9239199) was also inspected as contextual later evidence: BW25113 add/deoD deletion/complementation experiments support purine salvage under the tested starvation/adenosine conditions. The paper identifies Add-mediated deamination as the predominant initial route in that context and discusses residual rihC activity. It does not isolate Apt flux through P121; no dominant-flux or exclusive-route claim is made. Its antibiotic outcomes are not encoded as pathway edges.

## Assemblies, metals and localization

DeoD is represented as native MetaCyc:DEOD-CPLX, containing six DEOD-MONOMER subunits, each exactly cross-referenced to P0ABP8. The 2018 primary work distinguishes wild type from double mutants and formycin analog structures, and explains the trimer-of-dimers architecture; no isolated monomer is asserted to catalyze the whole reaction.

Apt is represented as native MetaCyc:ADENPRIBOSYLTRAN-CPLX, with two ADENPRIBOSYLTRAN-MONOMER subunits and exact P69503 unification. The complex lacks a top-level common-name in the XML; its catalytic enzymatic-reaction name is “adenine phosphoribosyltransferase,” independently checked by root's canonical HTML authority. Current UniProt homodimer annotation has no attached experimental evidence code, and its RHEA16609 catalytic annotation is HAMAP MF_00004 inference. These annotations are not inflated to directly inspected primary assays.

The exact native Apt enzymatic reaction lists Mg2+ and alternative Mn2+. The 2011 coupled recombinant assay includes 10 mM MgCl2, adenine and PRPP; it does not measure physiological metal occupancy. Mn2+ remains explicitly native annotation, and the two edges do not imply simultaneous binding. The cited 1971 primary paper's publisher PDF returned 403 HTML; no PDF hash, quote or directly inspected result is fabricated. The paper's title alone is not used as metal evidence. The 2011 assay's coupling enzymes, ATP, PEP and NADH are assay reagents, not Apt reaction substrates.

Apt's cytoplasm edge follows current UniProt and the inspected PMID365172 abstract showing intracellular localization and no significant association with purified membrane fractions. The native commentary preserves earlier preparation-dependent membrane-vesicle association. No exclusive membrane location is asserted. The attempted PMC1185975 BioC full-text endpoint returned HTML despite HTTP200, so the ledger and reference explicitly say abstract-only. DeoD phosphate is a substrate, not an added cofactor; absence of a metal annotation is not a claim of cofactor independence.

## Source-to-graph chemistry and provenance

All eight stoichiometric reaction-side entries are retained. Rhea27642→27643 and16609→16611 bridges cite the exact master `rh:directionalReaction` triples separately from native reaction cross-references. Native ADENPHOSPHOR-RXN references bidirectional27645; that is preserved and resolved through the inspected family, not asserted to directly cite27643. Apt's source direction is right-to-left relative to its master equation.

The connecting adenine edge separately cites native ordering/native ADENINE plus the current Rhea upstream product and downstream substrate. It does not attribute ChEBI identifiers to native pathway XML. Formula and charge replay checks both reactions and the full net: adenosine + hydrogenphosphate + PRPP → alpha-D-ribose 1-phosphate + AMP + diphosphate. All coefficients are1; no water or proton is added to these exact charge-balanced Rhea equations.

Every record ID has an independent source in the identifier ledger. There are no project-minted complex identities, source mappings equating unlike legacy variants, anonymous catalysts, or omitted native P121 reactions. Transport, PRPP production, hydrolase variants and AMP phosphorylation are outside P121's explicit two-reaction list, not overlooked parts of it. Primary PMID35674474 was accidentally included in an initial abstract query and proved unrelated; it is explicitly rejected and no maintained assertion cites it.

## Verification and handoff

The author replay rereads all retained native/UniProt bodies, streams the complete original Rhea RDF, reconstructs exact source projections, checks all eight sides/two atom-charge balances/net, verifies both native assemblies/accession bridges, and executes actual KGX export with full evidence preservation. Narrow native/closed schema checks run in the same helper. An initial helper projection check failed because it compared an extra ontology definition field. That check and a KGX dataclass access issue were corrected before the successful replay; neither changed scientific bytes. Only actual terminal success is recorded in validation. Root owns final shared authority integration, generated page checks, whole-corpus gates, independent review and publication.

Root's fresh iModulonDB context uses the E. coli precise_mg1655 dataset and includes apt/deoD queries. It is expression context only; no catalytic/regulatory edge or missing-gene inference follows from those query results. Public-release licensing remains deferred by the user; retained MetaCyc/PathBank provenance does not imply new license clearance.
