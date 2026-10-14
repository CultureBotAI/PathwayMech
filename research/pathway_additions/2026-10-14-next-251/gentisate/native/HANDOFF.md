# Gentisate degradation I native-source handoff

Author research, not an independent scientific review. No repository files edited. All originals remain external in this directory. Root is curating in `/private/tmp/pathwaymech-next-251-20261014`.

## Exact identity and boundary

Use `MetaCyc:PWY-6223`, `gentisate degradation I`. The XML explicitly distinguishes the isomerization route from direct hydrolysis (`PWY-7469`). The inspected MetaCyc mirror exposes PGDB **27.0** and Pathway Tools **27.0**; do not label these originals 30.0 merely because the current BioCyc search result says 30.0.

The authority HTML is `originals/mirror-PWY-6223.html`, SHA256 `98925435f7aa34bbef9270c4a6eab2f3e6ec02f313ad609455ee5d3ab04b88be`, from `https://bf2i-artsymbiocyc.insa-lyon.fr/META/NEW-IMAGE?object=PWY-6223`. Its title is `MetaCyc gentisate degradation I`. The direct BioCyc request instead redirected to an account-required page: preserve that acquisition as a failed semantic retrieval, not a pathway authority.

All three native reactions are L2R in both `reaction-layout` and their reaction object. Two `reaction-ordering` tuples explicitly give:

1. `GENTISATE-12-DIOXYGENASE-RXN`: gentisate + O2 -> 3-maleylpyruvate + H+; EC1.13.11.4, native RHEA18238, KEGG R02656.
2. `MALEYLPYRUVATE-ISOMERASE-RXN`: 3-maleylpyruvate -> 3-fumarylpyruvate; EC5.2.1.4, native RHEA17394, KEGG R03868.
3. `RXN-10445`: 3-fumarylpyruvate + water -> fumarate + pyruvate + H+; EC3.7.1.20, native RHEA26169, KEGG R01085.

Issuing UniProt cites corresponding Rhea master IDs 18237,17393,26168. Root independently closes Rhea sides, direction and exact chemical identity.

The native pathway has upstream links to cresol/salicylate routes and downstream links through fumarate/pyruvate to TCA. These are pathway interfaces, not additional reactions inside this exact three-step route. In particular the pyruvate-to-TCA link must not imply that pyruvate directly enters a TCA reaction without its intervening chemistry.

## Chemical identities read from original native compound objects

| Native | ChEBI | Native identity |
|---|---|---|
| CPD-633 | 58044 | gentisate, anion |
| CPD-1070 | 16727 | 3-maleylpyruvate, dianion, InChI `/p-2/b2-1-` |
| CPD-277 | 16854 | 3-fumarylpyruvate, dianion, InChI `/p-2/b2-1+` |
| FUM | 29806 | fumarate dianion |
| PYRUVATE | 15361 | pyruvate anion |
| OXYGEN-MOLECULE | 15379 | dioxygen |
| PROTON | 15378 | H+ |
| WATER | 15377 | water |
| GLUTATHIONE | 57925 | glutathione |
| CPD1G-2 | 16768 | mycothiol |
| FE+2 | 29033 | Fe2+ |
| CU+2 | 29036 | Cu2+ |

Unencoded plus signs initially caused metal404s. The corrected URL-encoded requests succeeded; both attempts are preserved. This is transport encoding, not biological absence.

## GO exactness check

The full current pinned `go.db` statements table was searched for gentisate, maleylpyruvate, fumarylpyruvate, 2,5-dihydroxybenzo*, gentisic and exact PWY-6223. `go-candidates.json` and `go-identity-extension.json` preserve query/results. No matching exact gentisate biological process was found in this whole database search, including synonyms and definitions. GO0047922,GO0050077,GO0034545 are molecular activities, not the pathway; GO1902000 is **homogentisate** catabolism and biologically wrong. The database query does not use filesystem ignore rules.

## Native catalyst coverage and dispositions

Every enzymatic-reaction attached to each of the three native reactions was fetched in full (10 total), together with every referenced protein and all three complex subunits. Species below are native object contexts, not proof that every individual has every enzyme variant.

| Native enzyme / ENZRXN | Identity and scope | Evidence and disposition |
|---|---|---|
| MONOMER-14769 / ENZRXN-16398 | NagI, UniProt O86041, Ralstonia sp. U2 | PMID11133965; unpurified heterologous-host assay; core complete-route anchor |
| MONOMER-14770 / ENZRXN-16399 | NagL, O86043, U2 | PMID11133965 unpurified heterologous assay; explicit glutathione cofactor; core anchor |
| MONOMER-14771 / ENZRXN-16400 | NagK, O86042, U2 | PMID11133965 unpurified heterologous assay, product HPLC; core anchor. Native prose incorrectly calls gene nagL: reject typo, preserve gene/synonym/issuing sequence NagK |
| G18NG-12642-MONOMER / ENZRXN-16404 | C. glutamicum ATCC13032 mycothiol-dependent isomerase, native Q8NLC1 crosslink | PMID16000747 and16481315 purified heterologous assays; explicit mycothiol cofactor. Separate variant, not U2 protein |
| CPLX-8846 / ENZRXN-22655 | GDOI/XlnE, P. alcaligenes NCIMB9867 | PMID10049846 native purified tetramer. Component4×MONOMER18566, UniProtQ9S3U6. REG14729 Fe2+ positive, REG14728 Cu2+ negative; both cite10049846. Native protein prose also describes promoter induction12909360; do not call it direct ligand binding. Additional first-step example, not necessary to complete U2 route |
| CPLX-8845 / ENZRXN-22654 | GDOII/HbzE, P. alcaligenes NCIMB9867 | PMID17720458 purified heterologous His6-tagged protein; component4×MONOMER18565, Q0QFQ2. Native prose incorrectly calls cloned gene xlnE: reject typo; gene/synonym/paper identify hbzE. Construct-qualified claims needed if retained |
| CPLX-6363 / ENZRXN-11167 | Haloferax sp.D1227 GDO | PMID9827334 purified protein and10086844 unpurified. Component4×MONOMER10867; Q330M9 xref. Native comment says accessionAF069949 once partial; do not assume complete sequence equivalence without independent issuing check. Native enzyme comment records highest activity2M KCl/NaCl. Additional archaeal first-step example |
| MONOMER-10866 / ENZRXN-11166 | Haloferax sp.D1227 maleylpyruvate isomerase | PMID10086844 unpurified activity; no UniProt in acquired object; no assembly known. Do not infer GSH/mycothiol independence from absent cofactor annotation |
| MONOMER-15921 / ENZRXN-18244 | SdgD, Q7X284, Streptomyces sp.WA46 | PMID15006746 unpurified heterologous assay; subunit structure explicitly unknown. Source salicylate degradation IV feeds gentisate; additional first-step example |
| MONOMER-17375 / ENZRXN-20385 | NaaD, F8QQ75, Bradyrhizobium sp.JS329 | PMID21498645. Native ENZRXN evidence code says unpurified heterologous assay while protein narrative says obvious candidate/not thoroughly characterized. Distinct5-nitroanthranilate pathway and uncertain isomerase speculation: exclude from gentisate graph pending primary resolution |

Native MetaCyc27.0 has **no L-cysteine-dependent BagL enzyme attached to this reaction**. The broader literature supports that separate variant, being researched by the primary-source agent; this bound is only this native attachment list, not universal biological absence.

## Complete native pathway species/range list

`species`: Corynebacterium glutamicum TAX1718; C.glutamicum ATCC13032 TAX196627; Haloferax sp.D1227 TAX78509; Klebsiella michiganensis M5al TAX290336 (historical papers call K.pneumoniae M5a1); Ralstonia sp.U2 TAX70356; Rhodococcus sp.NCIMB12038 TAX933800; Salmonella enterica serovar Typhimurium TAX90371; Streptomyces sp.WA46 TAX235278; native ORG5928 P.alcaligenes NCIMB9867 (parent TAX43263, no exactstrain taxon dblink).

`taxonomic-range`: TAX2 Bacteria and TAX2157 Archaea. These range statements are not experimental universal coverage. Recommend exact U2 taxon for the complete experimental anchor, plus exact taxa of separately retained variant proteins; do not automatically reproduce all nine species merely because a native list contains them.

## Independent issuing UniProt and ENA identity checks

All O86041,O86043,O86042,Q8NLC1 full JSON originals retrieved. Native reciprocal xrefs agree. For U2, current UniProt organism is broad tax54061 `Ralstonia sp`, but its source references explicitly say strainU2. Native MetaCyc gives exacttax70356. ENA AF036940.2's `/strain="U2"` and AAD12619.1(nagI),AAD12620.1(nagK),AAD12621.1(nagL) translations were read, extracted and compared against the entire UniProt sequence strings: **all exactly equal** at355,192,212aa. See `u2-sequence-identity.json` for sourcehash, sequencehash and explicit context.

O86043 reviewed entry98: NagL homodimer and GSH cofactor have ECO0000269 citing PMID18824004. Keep dimer description; no exact native dimer assembly identifier was established by this bounded acquisition, so no invented complex CURIE or self-part_of edge.

O86042 reviewed entry74: Mg2+(CHEBI18420) and Mn2+(CHEBI29035) cofactors are explicitly **ECO0000250 by similarity**, no direct U2 experimental citation. Preserve alternatives/inference if added; do not attach them to11133965 as experimentally measured, and do not assert simultaneous metal occupancy.

O86041 reviewed entry65 has catalytic evidence11133965 but no COFACTOR or SUBUNIT comment. This does not prove cofactor independence or monomeric activity.

Q8NLC1 entry141 is unreviewed, named `Uncharacterized protein`, with Cgl3021, exacttax196627,241aa,26449Da. PDB2NSF/2NSG map1–241 and cite17428791; Zn2+ binding sites are structure-supported, not automatically catalytic-cofactor evidence. Native apparent34kDa is an experimental gel/mass statement distinct from calculated26449Da; do not silently replace one with the other. Prefer native G18NG12642 protein label if retaining that variant, or honor issuing unreviewed label explicitly; do not overwrite the canonical UniProt label.

## Proposed graph support and source files

`author-support-proposal.json` contains4protein nodes and8proposed catalytic/cofactor edges, including the optional similarity-marked NagK metals and separate mycothiol variant. It is an external proposal, not a complete YAML or independent review. It uses UniProt's Rhea masterIDs; root closes final reactionIDs/directions. Primary-tag construct qualification remains for the primary-source agent/root.

`source-manifest.json`:50acquisition entries,48downloaded artifacts,2initial404attempts. One of the48downloads is the account-required HTML, not valid pathway evidence. The manifest excludes HTTP cookies. **Never copy `pathway-html-acquisition.json` into the repository:** it is a raw external receipt containing full headers. `object-projection.json`:41nativeobjects, structural fields only, excluding narrative comments, credits and email. `u2-sequence-identity.json` retains hashes/context rather than raw sequences. All sources have original artifact SHA256 bindings.

## Variant identity and chemistry closure follow-up

The current issuing ChEBI structures, pinned full InChI/SMILES, and native full CML atom/bond graphs close both cofactors exactly. `cofactor-identity-closure.json` and `close_cofactors.py` are reproducible with cached RDKit 2024.03.5. GSH CHEBI:57925 is C10H16N3O6S, charge -1. Mycothiol CHEBI:16768 is C17H30N2O12S, neutral. Both native SMILES are only `S[R]` placeholders and were rejected as full structural identities; native CML connectivity and full stereochemical InChI, plus independently issued ChEBI, close the structures.

`q8nlc1-sequence-identity.json` verifies Q8NLC1 against NCBI BAC00415.1. `variant-protein-identity.json` adds the exact NP_602215.1 accession printed in PMID:22636771 Fig.6; all 241 residues are identical. PDB 2NSF entity 1 is a **261-residue experimental construct**: `MGSSHHHHHHSSGLVPRGSH` followed by all 241 base residues. Its SIFTS mapping starts at entity position 21. The full 20-residue extension belongs to that structure; do not transfer it automatically to the earlier 2006 assay. The primary-source agent independently reports that Feng2006 used pET28a-ncgl2918, N-terminal His6, BL21(DE3).

For the third isomerase variant, the paper's deposited ENA HQ897158.1 sequence contains bagL CDS 1778..2266, protein ADZ54051.1, UniProt H6TG59. Direct NCBI ADZ54051.1 and issuing UniProt H6TG59 agree on all 162 amino acids; ENA source and UniProt both identify Paenibacillus sp. NyZ101, NCBITaxon:980079. The current UniProt submitted label is `Cysteine dependent-maleylpyruvate isomerase` (unreviewed). This closes the **base protein**, not the experimentally tagged preparation. The primary-source agent independently read the original 2012 paper: pET28a bagL, NdeI/EcoRI, N-terminal His6, BL21(DE3), Ni-NTA purification; no full extension sequence printed. Qualify catalytic and cofactor assay claims with that tag class. Physiological cysteine choice remains the authors' inference; L-cysteinylglycine and GSH also support the purified assay.

The final sanitized source manifest now additionally includes the variant/cofactor/sequence acquisitions. Earlier counts in this handoff describe the initial native-only snapshot. Use current `source-manifest.json` entries and their hashes as authoritative.

## Final selected variant chemicals and deposited U2 NagL assemblies

`variant-cofactor-identity-closure.json` closes the selected CHEBI:35235 L-cysteine zwitterion and CHEBI:61694 L-cysteinylglycine zwitterion against pinned and issuing current structures. Each has one R stereocenter, a +1 ammonium, a -1 carboxylate and a neutral thiol. These are explicit graph normalization choices; the original assays did not measure protonation states. Canonical single ions also close: nickel(2+) CHEBI:49786, magnesium(2+) CHEBI:18420, calcium(2+) CHEBI:29108, copper(2+) CHEBI:29036, zinc(2+) CHEBI:29105 and iron(3+) CHEBI:29034. RDKit appends formal charge to its molecular-formula string for single ions; the closure compares the element composition and formal charge independently. Their assay activation/inhibition conditions must remain on construct-qualified edges and do not establish physiological metal cofactors.

`u2-nagl-assembly-identity.json` verifies the entire deposited samples: 2JL4 entity 1 is exactly an extra N-terminal K plus O86043 (213 total residues); 2V6K entity 1 is exactly N-terminal AK plus O86043 (214 total residues). Both deposited assembly 1 records are dimeric, oligomeric_count 2, author_and_software_defined_assembly with PQS method. Preserve these construct distinctions for deposit-based claims. The reviewed UniProt homodimer annotation is separately attributable to UniProt and PMID:18824004; no exact native complex CURIE was established here.

All proposed reference hashes are independently reconciled to the final sanitized acquisition manifest by `author-reference-bindings.json`. The exact maintained-safe file allowlist and final hashes are in `retained-artifacts.json`; originals, full acquisition receipts with headers, and primary papers stay external.
