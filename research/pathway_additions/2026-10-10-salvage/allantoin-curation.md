# Allantoin degradation IV (anaerobic): author evidence ledger

Date: 2026-10-10, America/Los_Angeles. Some fresh request timestamps fall on October 11 UTC. Target: `data/pathways/allantoin-degradation-iv-anaerobic.yaml`, exact external pathway `MetaCyc:PWY0-41`. This is an authoring dossier, not an independent scientific review. Shared authorities, history, rendered pages and full-corpus gates are coordinated by the parent agent.

## Identity, prior disposition and novelty

The inspected native PWY0-41 XML explicitly includes upstream PWY-5698 and the oxalurate/oxamate branch, carbamate kinase and spontaneous carbamate decomposition. Its exact title is *allantoin degradation IV (anaerobic)* and its organism is E. coli K-12 MG1655. No exact GO process was established for this particular full route; the route-specific MetaCyc identifier is retained. The old PathBank member PW002050/SMP0002064 is a discovery lead, not the authority for current chemistry or protein assembly.

The prior committed `2026-10-10-citrate-sbm/allantoin-handoff.md` and source receipts were read. Their barrier was the lack of a verified whole-AllFGH assembly identifier. The present reassessment does not manufacture one: the current component-role contract permits source-supported functional `enables` assertions while retaining the experimentally supported joint requirement in every edge. This is not a shortened pathway, single-subunit catalyst assignment, asserted 1:1:1 stoichiometry, or formal AND semantics.

The pre-authoring and final exact-key searches include ignored and hidden content, excluding only .git/.venv internals. Commands, matches digest and the original search receipt are in `allantoin-dedup.json`. The original Documents checkout is inaccessible in this session; that checkout is not falsely claimed searched. The clean-base worktree contains all committed 169 records and prior research. Existing yeast allantoin/urea-producing pathways and overlapping carbamate-kinase/carbamate-decomposition reactions are distinct from this E. coli oxamate route. Prior research mentions were investigated, not mistaken for maintained pathway records. No exhaustive source-coverage claim is made.

## Complete route and the inorganic-carbon endpoint

The directed chemistry is extracted anew from official Rhea release 142 RDF and the direction TSV. Rhea compounds retain exact charge forms and S stereochemistry. Native source reaction membership and current direction-family correspondence have separate edge-level evidence.

| Native reaction | Directed Rhea | Decision |
| --- | --- | --- |
| ALLANTOINASE-RXN in PWY-5698 | 17030, left-to-right | S-allantoin + water → allantoate + proton |
| ALLANTOATE-DEIMINASE-RXN in PWY-5698 | 27486, left-to-right | allantoate + water + 2 protons → S-ureidoglycine + ammonium + CO2 |
| URUR-RXN in PWY-5698 | 25242, left-to-right | S-ureidoglycine + water → S-ureidoglycolate + ammonium |
| RXN0-7024 | 15330, left-to-right | S-ureidoglycolate + NAD+ → oxalurate + NADH + proton |
| OXAMATE-CARBAMOYLTRANSFERASE-RXN | 22986, right-to-left | oxalurate + phosphate → oxamate + carbamoyl phosphate |
| RXN-14196 | 30757, right-to-left | carbamoyl phosphate + ADP → carbamate + ATP |
| RXN0-5222 | 15650, left-to-right | carbamate + 2 protons → ammonium + CO2, spontaneous |

There are 31 source-side occurrences. Every individual reaction balances elements and formal charge. Their summed formal net consumes one S-allantoin, three waters, two protons, one NAD+, one hydrogenphosphate and one ADP; it produces one oxamate, three ammoniums, two CO2, one NADH and one ATP. This algebra is not a measured in vivo flux or universal ATP yield.

The AllK 2022 paper, Figure 2A and Results sec14, describes downstream bicarbonate/ammonium. Current UniProt includes both combined net RHEA:10154 and component 30757 plus spontaneous 57718. The native full pathway instead contains spontaneous RXN0-5222/RHEA:15650, which gives CO2. We select that native formal endpoint, explicitly avoiding a claim that dissolved inorganic carbon is exclusively CO2. Adding hydration RHEA:10750 would transform that endpoint into the bicarbonate representation, but is outside this native route. We do **not** add 10154, 57718 or 10750 and do not count enzyme and net reactions twice. RHEA:15650 has no molecular-activity category, enzyme, or catalytic edge; actual export must remain `biolink:BiochemicalReaction`.

The mirror's AllC Rhea13594 cross-reference is absent from the current official direction TSV. It is rejected without guessing a successor by numeric offset. Native chemical sides explicitly yield S-ureidoglycine, while current reviewed P77425 names family27485. Those independent observations ground27486; no current native-Rhea exact cross-reference is invented. Generic native R165-RXN (NAD-P-OR-NOP) is an alternate duplicate and is excluded in favor of NAD-specific RXN0-7024. Native RXN-14196 points to bidirectional30758; its relationship to30757 is evidenced through the actual Rhea `bidirectionalReaction` and `directionalReaction` properties.

## Protein identities, assemblies and evidence grades

All eight reviewed UniProt proteins are annotated to E. coli K-12 taxon83333. Native pathway/complex identities and MG1655 primary experiments support the narrower record scope511145; we do not claim that UniProt's organism field itself is MG1655. Recombinant BL21 expression in the AllFGH paper is an assay host, not the physiological route scope.

| Role | Identity and representation | Evidence and limits |
| --- | --- | --- |
| AllB | P77671 part_of MetaCyc:CPLX-64; complex catalyzes17030 | Native4copies of G6281-MONOMER; UniProt BioCyc monomer cross-reference and experimental homotetramer annotation; PMID11092864 native-mass/crosslink results. |
| AllC | P77425 part_of MetaCyc:CPLX-7524; complex catalyzes27486 | Native2copies G6285-MONOMER; current homodimer annotation ECO:0000269/17362992. The abstract describes a dimerization domain; the exact dimer assertion is also independently native/UniProt grounded. Old2007 direct ureidoglycolate product assignment is superseded by2009/2010 ureidoglycine work. |
| AllE | P75713 catalyzes25242 | Catalytic evidence ECO:0000269/19935661 and ECO:0000305/20038185; monomer annotation itself ECO:0000305. Existing RCSB1RC6 assembly1 was inspected as monomer context, not used to invent a new whole-enzyme identifier. |
| AllD | P77555 part_of MetaCyc:CPLX0-7993; complex catalyzes15330 | Newly inspected native2copies G6286-MONOMER, current annotation, full PMID23284870 Results s2a solution SEC/structure. NAD+ versus NADP+ FigureS2 independently inspected, including PDF rendering. |
| AllF/G/H | Q47208/P77129/P0AAS5 each enables22986 | Current names and locus aliases; whole-enzyme FUNCTION/CAT/SUBUNIT statements plus full2024 PMID38888336. Each edge states joint requirement, no isolated sufficiency/stoichiometry/formalAND assertion. Physiological direction is UniProt ECO:0000305, not misreported as a directly purified forward assay. |
| AllK | P37306 enables30757 | Full PMID36384810 purified substrate-dependent ATP production; component30757 UniProt evidence is ECO:0000305 even though combinednet10154 has ECO:0000269. No unverified oligomeric state. |

The three native assemblies have independently fetched XML bodies and parent-acquired HTML identity authorities; their exact IDs and expected labels are in `allantoin-identifiers.json`. AllF's PDB3DMY is a fragment (SIFTS82–555) homodimer, not AllFGH. Exact RCSB accession queries did not return G/H experimental objects; those bounded no-hits and prior ComplexPortal queries are not evidence that no assembly can exist. Prior account-required EcoCyc bodies are retained externally as access failures and never passed off as XML authority.

## AllFGH primary experiment and later-literature limits

PMID38888336/PMC11326118 full main XML Methods, Results, Discussion, Tables1–5 and captions were inspected. MG1655 deletions/complementation support joint component involvement: three-gene complementation restores the wild-type oxamate result; single genes do not restore the triple deletion, while partial combinations produce limited rescue. The purified coexpressed preparation was assayed in the reverse direction, oxamate plus carbamoyl phosphate to oxalurate, because the forward oxalurate substrate was unavailable. It does not directly measure isolated subunit catalysis.

The139kDa,1:1:1 composition was assumed for kinetic normalization, not established quaternary stoichiometry. The authors explicitly leave quaternary structure unresolved. Predicted subunit oligomers and a repeated AllG text label in Table5 are not converted into a whole assembly. The old mirror22.5 hypothetical-enzyme marker predates this2024 experimental assignment; preserving that marker as the current scientific conclusion would be misleading.

The targeted2024–2026 literature followup and2025 full regulatory paper PMC12535856/PMID41016821 were inspected at the relevant Results/Methods/Discussion sections. The latter concerns MC4100 AllS/ArcA regulation, not a new resolved assembly. Additional nitrifier MAG and comparative-genomic abstracts do not resolve AllFGH quaternary identity. These regulatory/prediction studies are context/exclusions, not new catalytic proof or taxon expansion.

## Metals, compartments and exclusions

AllB Zn/Ni/Co/Mn edges denote alternative supported metal preparations. They do not assert all four metals are simultaneously required. The annotated two-Zn-per-subunit description is not a universal measured occupancy: the metal-substitution primary paper reports preparation-dependent substoichiometric metal contents and stereoselectivity differences. The selected pathway is S-allantoin; cobalt-dependent weaker R-allantoin activity does not add an R route.

AllC's earlier binuclear zinc structure and later manganese-dependent functional chemistry are preserved as source-specific observations, not a unique physiological metal claim. PMID25020232 abstract covers a substrate-bound E. coli AllC comparison to plant UAH; only reviewed UniProt explicitly supplies the Mn-binding annotation. Plant ureidoglycolate-amidohydrolase chemistry is excluded. AllE uses Mn and can use Co as an alternative.

AllFGH Mg dependence was tested on an enzyme preparation (Figure4C), and purified assays used10mM MgCl2. This supports whole-enzyme assay context, without localizing a binding site to each isolated subunit. AllK assays used30mM MgCl2, which alone does not establish an isolated AllK metal-binding requirement. CHEBI:18420 is retained as a declared contextual cofactor node described in the record and relevant edges; no unsupported subunit has_cofactor edge is created. The record does not claim either enzyme is Mg-independent.

Cytoplasmic annotations are attached only to AllC, AllE, AllD and AllK. AllE has experimental annotation; the others retain ECO:0000305. No unsupported compartment is assigned to AllFGH or the entire pathway. Transport, transcriptional regulation, downstream assimilation/glyoxylate metabolism, yeast urea-producing routes, other taxa, NADP substitution and duplicate net chemistry are deliberately outside scope.

## Source access, provenance and checks

Raw bodies remain outside the repository at `/private/tmp/pathwaymech-salvage-evidence/allantoin`. `allantoin-source-manifest.json` distinguishes exact prior same-day body reuse from fresh retrieval and records every retained body hash/scope. Rhea gzip hashes cover compressed bytes; the direction-table hash covers plain TSV bytes. Source assertions preserve primary XML section, native object, UniProt JSON and exact Rhea side/participant locators. No verbatim primary quote is used in the YAML; source assertions are not presented as quotations.

Full-text access was obtained for AllFGH2024, AllK2022, AllD2012 and the AllB2000/2002 articles. The AllC/AllE PMID17362992/25020232/20038185/19935661 evidence was inspected at abstract and current reviewed-UniProt levels; no inaccessible full text is claimed. AllD supplementary FigureS2's separate PDF hash is in the source manifest. Fresh exploratory RXN-11209/RXN-11210 proved unrelated and are explicitly rejected. Temporary headers, cookies and signed URLs are not committed.

The parent-owned iModulon adapter fallback and exact-locus queries are documented in `imodulondb-context.json` and its source manifest. The old aliases fdrA/ylbE/ylbF/ybcF correspond to b0518/b4572/b0520/b0521; oldb0519 is unreturned. Gene hits and absent name-query hits are bounded expression-context results, not catalytic proof or evidence of absent module membership.

`allantoin-validation.json` captures the actual final narrow command, script hash, target hash, native and closed schema checks, independently resolved named identities,31exact side coefficients/directions/locators, seven element/charge balances, source-body digests and actual target KGX export. All107 evidence objects and cited reference metadata are compared to output. The initial scratch Rhea guessed-family lookup failure, unsupported evidence_code draft key, and mistaken validator assumption about UniProt taxon are preserved as corrected development attempts; no failed result is claimed as a pass. Full shared gates and independent scientific review remain the parent workflow.
