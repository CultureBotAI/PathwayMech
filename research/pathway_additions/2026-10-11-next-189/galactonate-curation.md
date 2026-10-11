# D-galactonate degradation — author curation

The selected record is **MetaCyc:GALACTCAT-PWY, D-galactonate degradation**, with all three native reactions. It begins with supplied D-galactonate and ends with D-glyceraldehyde 3-phosphate and pyruvate. Native pathway XML, reaction XML, current reviewed proteins and original primary bodies were inspected before drafting. This is a new complete pathway record; it is not an assertion that all remaining source candidates have been exhausted.

## Boundary and duplicate assessment

Hidden and ignored files were included in searches of both the current worktree and the original Documents checkout. The original checkout was accessible. Exact identifiers, enzymes, reaction families, papers, names and broader pathway sources were searched. The search commands, full output paths/hashes and dispositions are in `galactonate-dedup.json`.

Prior PathBank screening marked PW000820/SMP0000840 for scientific review and membership selection. Its actual frozen BioPAX body contains the combined “Galactitol and Galactonate Degradation” pathway, transport and a linked glycolysis/pyruvate-dehydrogenase pathway. That broader map is a discovery lead, not the identity assigned here. The unchanged archive was independently streamed and hashed as `b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44`; the extracted member agrees with the frozen ledger.

The original checkout's ignored DRAM inventory includes M00552, a five-step module continuing through glyceraldehyde-phosphate dehydrogenase and phosphoglycerate kinase to glycerate 3-phosphate. This exact three-step MetaCyc record does not claim full M00552 coverage. Nonphosphorylative M00309 and the broader M00633 are also not equivalent. GO:0034194 names D-galactonate catabolism generally, without specifying this three-step phosphorylative route, so the narrower native MetaCyc identity is retained. The existing yeast galactose record is the Leloir pathway, while the D-glucarate record has different intermediates, enzymes and defining reactions.

## Complete chemical mechanism

| Native reaction | Rhea master | Selected member | Master orientation |
| --- | --- | --- | --- |
| GALACTONDEHYDRAT-RXN | 18649 | 18650 | left to right |
| DEHYDDEOXGALACTKIN-RXN | 16525 | 16526 | left to right |
| DEHYDDEOXPHOSGALACT-ALDOL-RXN | 24464 | 24465 | left to right |

The native aldolase reaction is reversible and links RHEA:24467. The pathway layout specifically selects L2R. The separate Rhea RDF assertion establishes master 24464's directional member 24465; it is not attributed to a nonexistent native 24465 cross-reference. The replay checks the actual family triples and all 11 chemical sides, including every `contains1` participant-to-compound-to-ChEBI path. General `contains` triples are not additional stoichiometric participants.

Rhea142 and ChEBI255 agree on formula and charge for all nine reaction chemicals. Each of the three reactions balances. The summed net is D-galactonate + ATP(4−) → D-glyceraldehyde 3-phosphate(2−) + pyruvate + ADP(3−) + H+ + H2O. The retained current ADP identifier is CHEBI:456216. Magnesium is a protein cofactor annotation, not a consumed or produced substrate. Galacto stereochemistry is retained; KDPG aldolase and its glucono substrate are not substituted.

## Enzymes, assembly and strain

| Protein | Current reviewed identity | Scope and evidence limit |
| --- | --- | --- |
| DgoD | Q6BF17; b4478/JW5629 | Native MG1655 frame and current K-12 catalytic annotation; Mg2+ binding has ECO:0000250 similarity evidence. |
| DgoK | P31459; b3693/JW3670 | Native and current reviewed catalytic assignment; gene-deletion physiology does not become a purified-enzyme assay. |
| DgoA | Q6BF16; b4477/JW5628 | Direct recombinant KDPGal aldolase assay, substrate stereochemistry and homotrimer evidence in PMID17981470. |
| DgoR | P31460; b4479/JW5627 | Transcriptional repressor, not a fourth pathway catalyst. |

The three native protein frames independently cross-reference the selected UniProt accessions and MG1655 taxon511145. Reviewed UniProt assigns K-12 taxon83333. The 2019 genetic/regulatory study used BW25113 derivatives; recombinant-protein expression hosts are not represented as proof that their endogenous pathway was tested. The 2007 DgoA study expressed cloned enzyme in an eda-deficient DF71 host to reduce KDPG-aldolase contamination. DgoA's native/His-tagged constructs and crystal trimer do not establish isolated-monomer sufficiency.

Native frames have no `component-of` assembly identity. Functional `enables` edges retain the measured/annotated function, with the homotrimer limitation explicit. No physical-complex accession is invented. Current UniProt warns that an older AAA62044.1 frameshift predicted a fused DgoA–DgoD ORF; the record uses their corrected separate sequences. DgoD's inferred magnesium occupancy is not a direct metal assay. DgoK magnesium binding is not added simply because the protein is a kinase. NADH in the DgoA coupled lactate-dehydrogenase assay is not its pathway cofactor.

## Regulation and later literature

The full 2019 primary HTML (PMID30455279) supports the BW25113 growth phenotype, negative transcriptional regulation by DgoR and inhibition of repressor DNA binding by D-galactonate. The graph's `regulates` edge denotes operon transcription, not direct inhibition of the three catalytic proteins. The `inhibits` edge denotes DgoR DNA-binding activity under the assayed conditions.

The full 2020 primary body (PMID33224125) was additionally inspected. Its Results Fig.6 shows that EDTA-treated DgoR retains DNA binding, whereas D-galactonate plus Zn2+, Ca2+ or Mg2+ can destabilize the protein–DNA complex. This supports a conditional metal-dependent effector response, not an exclusive physiological-metal assignment. The paper's abstract and some prose invert or blur the derepression wording; the retained assertion follows the actual Results and Discussion. Its ligand-bound pose was modeled after cocrystallization failed, not directly observed in a ligand-bound crystal. No residue-level docking claim or unique metal edge is added.

Later abstracts PMID33068046, PMID39777470 and PMID40497739 were inspected as an update check. They support the importance of effector binding/allostery and naturally varying repressor behavior. Their full texts were not inspected, and they are not direct record references. They reinforce keeping the record's experimentally qualified strain/condition scope instead of generalizing an invariant phenotype to every E. coli isolate.

## Access and provenance

Full primary HTML was inspected for PMID17981470, PMID30455279 and PMID33224125. PMID211976 is a publisher abstract-only citation, explicitly labeled as such. PMID324806 full-text retrieval returned403; the paper is not used as a directly inspected record reference. Current UniProt and native annotations that cite older papers remain database assertions attributed to those databases.

The source manifest keeps original body URLs, hashes, versions and safe metadata. No session/cookie/authentication headers or signed redirect URLs are maintained. UniProt release2026_03 is documented by the actual response headers, separately from entry/sequence version numbers. Raw bodies remain outside the repository. Source provenance is retained; public redistribution licensing is deferred as requested by the user.

Fresh canonical iModulonDB context was acquired by root for this cohort: exact dgo gene/locus searches found the selected genes in e_coli/precise_mg1655. No matching module-name search hit is not evidence that these genes lack module membership. The context is not used as biochemical or regulatory evidence in the graph.

## Exclusions and verification

Excluded from this exact boundary: DgoT uptake, galactitol metabolism, upstream D-galactose oxidation, downstream GAP oxidation/phosphorylation, archaeal enzyme assignments and unrelated KDPG chemistry. No exclusive DgoR metal, transport stoichiometry, subcellular localization, constitutive assembly for DgoD/DgoK, or host-colonization mechanism is inferred.

`galactonate-replay.py` reopens retained native/Rhea/ChEBI/UniProt bodies, checks every source digest, reaction side and balance, native complete membership/order, master direction, protein identity, taxon, assembly/cofactor limits, paper-to-edge attachment, native and closed schemas and actual KGX edge/evidence preservation. Its terminal outcome and exact target/script hashes are in `galactonate-validation.json`. Whole-corpus rendering, testing, authority integration and independent scientific review are separate root/reviewer tasks and are not claimed by this author receipt.

## Independent review correction (#352)

The initial independent review `20261011T043907Z-galactonate-initial-independent-review` identified two exact figure-locator errors. The original PMC6351737 Fig. 1 caption assigns growth spots to panel C; Fig. 8A-C contains effector EMSA and proteolysis. Accordingly edge025 now cites Fig. 1C and edge027 Fig. 8A-C. Only these two locator strings changed; original source digests and all scientific assertions/identifiers remain unchanged. Issue: https://github.com/CultureBotAI/PathwayMech/issues/352. Initial SHA256 `5672802eca1a1f61c2fb08fe29b89899eafe8e1e96e868f7a26449de7ef9a5b8`; corrected SHA256 `51e71bf9bd2d0888f6f3e56f98eb4b4fab32034266bfe8dfeeb375529afc3f84`. The author replay now independently checks the actual original figure-caption panel content against these attachments. A separate reviewer verifies the disposition.
