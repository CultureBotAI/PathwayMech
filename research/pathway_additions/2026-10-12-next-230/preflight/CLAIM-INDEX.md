# Full claim and authoring-disposition index

Every row below has original bindings and exact XML locators or explicitly descriptive structured-source selectors in `derived/claim-dispositions.json`. This is a research handoff, not a validated record.

## sbp-01 — core

ATP-dependent S7P phosphorylation followed by SBP cleavage defines PWY0-1517. Native taxonomic range is a database scope, not proof of ordinary wild-type complete flux.

**Disposition:** Two internal reaction events; keep physiological evidence restricted to tested strains and conditions.

**Bound sources:** 2.

## sbp-02 — core

Rhea31444 is S7P + ATP to SBP + ADP + proton. Rhea30169 is SBP to E4P + DHAP; native Rhea30170 is bidirectional, not a cleavage-direction identifier.

**Disposition:** Use exact native RDF orientation and eight unit chemical sides; never infer direction by number.

**Bound sources:** 3.

## sbp-03 — chemistry

The native generic S7P class links ChEBI57483; its alpha-pyranose child CPD-19339 links133984 and is a distinct source object. Native SBP links58335.

**Disposition:** Retain generic core identity; no fabricated anomerization or substitution of the alpha child.

**Bound sources:** 3.

## sbp-04 — source conflict

Frozen PathBank root SMP0002110 has two biochemical events and two child interfaces. Neutral ATP/ADP/S7P/E4P and SBP structures differ from curated anions; the DHAP reference has formula C3H5Li2O6P.

**Disposition:** Retain the exact salt/charge conflicts. PathBank provides structural context, not authority to collapse salt, generic/anomer or charge identities.

**Bound sources:** 1.

## sbp-05 — assembly

PfkA native homotetramer has four 6PFK-1-MONOMER components; FbaA native homodimer has two FRUCTBISALD-CLASSII-MONOMER components.

**Disposition:** Use exact native assemblies and source coefficients. Reference chains are not isolated active monomers.

**Bound sources:** 4.

## sbp-06 — assembly conflict

PathBank ProteinComplex1347 includes both PfkA7802 and PfkB7803, but assigns coefficient4 only to PfkA.

**Disposition:** Preserve conflict; do not invent mixed PfkA/PfkB tetramer or assign PfkB bypass activity.

**Bound sources:** 1.

## sbp-07 — identity

PfkA P0A796/b3916 and FbaA P0AB71/b2925 are reference anchors. Entrez948412 and947415 are MG1655 taxon511145; misleading alternative GeneID crossrefs93777982/93779073 issue from Shigella sonnei624.

**Disposition:** Keep paper BW25113/ASKA preparations separate from reference sequence/taxon. Reject off-taxon joins.

**Bound sources:** 6.

## sbp-08 — physiology

2009 BW25113 talA talB cells grow on xylose; additional pfkA deletion abolishes this growth. deoBC, fbp and tpiA tests distinguish alternatives with stated data-not-shown limits.

**Disposition:** Retain condition-specific genetics and negative results, not a wild-type flux or binding proof.

**Bound sources:** 2.

## sbp-09 — construct

2009 direct assay uses six-His ASKA PfkA/FbaA, 5mM S7P or F6P, 2uM enzyme, 2mM ATP, potassium MOPS, 37C, one hour, n5.

**Disposition:** Qualify each catalysis endpoint; do not merge with 2020 pET28b or assume host not stated for ASKA preparation.

**Bound sources:** 2.

## sbp-10 — direct assay

PfkA alone produces candidate SBP; adding FbaA produces E4P and DHAP. FbaA alone and no-enzyme controls do not show those products, while F6P comparison differs.

**Disposition:** Keep all five Table III preparations and uncertainty in SBP quantification.

**Bound sources:** 2.

## sbp-11 — analytical limit

The 2009 study lacked an authentic SBP standard, inferred migration from related phosphates and used F1,6BP calibration. Results report369.0 while Methods report367.0.

**Disposition:** Explicit unresolved internal mass inconsistency; do not silently correct source or claim standard-confirmed identification.

**Bound sources:** 3.

## sbp-12 — metabolomics

2009 S7P accumulation is substrate/strain specific; supplementary values show about45.67fold on xylose and101.63fold on gluconate.

**Disposition:** Use exact units and WT/mutant columns; avoid applying these numbers to all media.

**Bound sources:** 2.

## sbp-13 — transcription

Main text says no notable related-gene transcriptional changes; supplementary fbaA ratio1.18 and pfkA1.241 are not literally unchanged.

**Disposition:** Retain numerical/wording distinction; no claim transcription cannot regulate the enzymes.

**Bound sources:** 2.

## sbp-14 — flux model

The 2009 isotopomer fit supports bypass flux in talAB under tested xylose conditions. Supplement best-fit WT bypass values are small nonzero0.004/0.005 when uptake normalized100; mutant both-pathway fit about29.923/29.181.

**Disposition:** Model-specific relative flux; not direct enzyme measurement or universal absence in WT.

**Bound sources:** 2.

## sbp-15 — model conflict

Supplement MFA stoichiometric tables sometimes label SBP cleavage product G3P/GAP instead of DHAP, including the current/novel versus L-type comparison.

**Disposition:** Keep source-model discrepancy; direct products and Rhea determine curated chemistry. No invented triose-isomerase core event.

**Bound sources:** 1.

## sbp-16 — cross-species assay

Lactococcus lactis pfk in pTRC99A complements the E. coli talAB pfkA triple-mutant xylose phenotype with IPTG.

**Disposition:** Retain heterologous complementation only; no L. lactis wild-type complete pathway/taxon claim or inferred protein accession.

**Bound sources:** 2.

## sbp-17 — construct

2009 supplementary strain/culture tables distinguish talA:tet/talB:Cm constructs, growth-screen and metabolomics carbon concentrations.

**Disposition:** Preserve separate assay contexts; no merged universal medium.

**Bound sources:** 2.

## sbp-18 — 2020 physiology

2020 reconstructed BW25113 talAB cells grow on xylose0.33±0.01h−1 versus WT0.39±0.01; M9 conditions differ from 2009. Trace WT-xylose SBP is present.

**Disposition:** Do not infer quantitative wild-type bypass flux from metabolite detection.

**Bound sources:** 2.

## sbp-19 — 2020 analytical limit

Later Orbitrap analysis identifies368.99 [M-H]− with199/271 fragments using E. coli talAB material, not a commercial standard; SBP stability and a368.804 blank peak are noted.

**Disposition:** Strengthens identity while preserving analytic limitations and distinction from 2009 signal.

**Bound sources:** 3.

## sbp-20 — 2020 construct

E. coli PfkA BW25113_3916 was cloned in pET28b and expressed in Rosetta after DH5alpha cloning; His-affinity preparation differs from 2009 ASKA. talAB cassette Methods mention both pKD3 and pKD4.

**Disposition:** Keep protein preparation and deletion-source inconsistency explicit.

**Bound sources:** 2.

## sbp-21 — 2020 kinetics

PfkA comparison gives apparent F6P Km0.065mM and kcat1.2s−1 versus S7P Km2.5mM and kcat0.25s−1 at55C; the tabulated S7P efficiency0.15×10^3 differs from arithmetic of rounded values.

**Disposition:** Use reported figures with source limit; no recalculated replacement, no physiological-temperature equivalence.

**Bound sources:** 2.

## sbp-22 — 2020 assay cofactors

PfkA kinase assay contains Mg5mM, ATP2mM and ADP0.25mM. Rabbit aldolase/G3PDH/NADH couple detection; no added TPI, and suspected trace TPI explains unequal downstream peaks.

**Disposition:** Auxiliary proteins/NADH are assay context, not E. coli pathway participants; no revised core stoichiometry.

**Bound sources:** 3.

## sbp-23 — thesis supplement

Author thesis chapter6 FigureS4 preserves both Michaelis–Menten and Hill fits for E. coli PfkA; FigureS1 is the no-enzyme time-course control.

**Disposition:** Cite separate thesis/pages137,140; no claim byte-identical to inaccessible journal supplement. Preserve fit alternatives; no derived physiological cooperativity claim.

**Bound sources:** 2.

## sbp-24 — donor variant

Native PWY-8178 has six events and PPi kinase RXN21730, unlike ATP PWY0-1517. The 2020 clostridial route has a different donor/taxon scope.

**Disposition:** Separate next231 lead/preflight; do not subsume it into this two-event definition.

**Bound sources:** 3.

## sbp-25 — negative donor evidence

C. thermosuccinogenes ATP/GTP-PFK has no S7P activity up to4mM; its F6P NH4 dependence, high Hill coefficient and relief-valve hypothesis concern another enzyme/organism.

**Disposition:** Retain negative comparison and explicitly hypothetical function, not E. coli regulation.

**Bound sources:** 3.

## sbp-26 — PfkA cofactor/localization

PfkA reference annotation supports Mg2+, homotetramer and cytoplasm, with experimental/HAMAP evidence roles.

**Disposition:** Separate cofactor requirement from core ATP; localization uses SUBCELLULAR LOCATION rather than SUBUNIT text.

**Bound sources:** 2.

## sbp-27 — PfkA canonical allostery

Native canonical F6P reaction is inhibited by PEP and activated by ADP/GDP; F6P cooperative substrate response is separate.

**Disposition:** Retain all signs with F6P assay scope; source does not directly measure their effects on S7P turnover.

**Bound sources:** 4.

## sbp-28 — PfkA context

Canonical PFK I accounts for >90% wild-type F6P-PFK activity, has cooperative F6P but not ATP kinetics, pH/active-site/allostery studies and in-vitro reverse activity.

**Disposition:** Preserve enzyme context without transferring percentage, direction reversal, or detailed uninspected mutant mechanisms to bypass flux.

**Bound sources:** 2.

## sbp-29 — FbaA cofactor

FbaA is a classII metal-dependent dimer; UniProt reports two Zn per subunit, catalytic plus structural. Older8436219 abstract reports two Zn per dimer; later2011 measured preparation-specific loading differs.

**Disposition:** Preserve capacity versus occupancy, construct and historical-numbering limits. No blanket reconciliation.

**Bound sources:** 3.

## sbp-30 — FbaA alternatives

Native annotation reports Co2+, Fe2+ and Mn2+ active metalloprotein alternatives to Zn.

**Disposition:** Qualified older-study annotation, not evidence that adding Mn stimulates the assayed2011 holoenzyme.

**Bound sources:** 2.

## sbp-31 — FbaA native modifiers

Native canonical activity lists K+ and ammonium activation and Ni2+/EDTA inhibition; K/NH4 are explicitly attributed to personal communication cited in1996.

**Disposition:** Retain provenance strength and Crookes-strain earlier enzyme context; no direct S7P-effect upgrade.

**Bound sources:** 5.

## sbp-32 — 2011 construct

2011 untagged MG1655 FbaA in pLEM1/pWKS30 is ≥70% pure; His-tagged pLEM5/pET28b BL21(DE3) WT/mutants ≥95% are a separate preparation. N-terminal methionine removal sets paper residue numbering.

**Disposition:** Separate original constructs and both site classes; do not silently renumber legacy His108/111 or paperHis110/226/264.

**Bound sources:** 3.

## sbp-33 — 2011 metal dose

Ni inhibits FbaA through the noncatalytic Zn site; Cu strongly inhibits, low Zn slightly activates/high Zn inhibits, Co slightly activates, Ca/Mg/Mn had no effect in that preparation.

**Disposition:** Retain dose/assay-specific negative effects and no-effects. Canonical FBP cleavage, not direct SBP kinetics.

**Bound sources:** 3.

## sbp-34 — 2011 modifiers

Histidine100uM protects against16uM Ni while GSH1mM enhances Ni inhibition; gshA/rcnA deletion contexts and site mutants qualify the mechanism.

**Disposition:** No generic direct GSH→FbaA inhibition or histidine activation; preserve Ni-dependent assay context and hypothesized Ni delivery.

**Bound sources:** 3.

## sbp-35 — 2011 physiology

MG1655 Ni growth inhibition depends on carbon source, is bacteriostatic and recovery after removal occurs without new protein synthesis; active versus passive repair is unresolved.

**Disposition:** Context for Ni toxicity, not evidence of bypass flux or transport.

**Bound sources:** 3.

## sbp-36 — FbaA reaction conflict

UniProt FUNCTION text names GAP plus E4P for SBP cleavage, while its own structured catalytic/physiological reaction and direct2009 assay support DHAP plus E4P.

**Disposition:** Record explicit database internal conflict; use direct products and Rhea30169.

**Bound sources:** 2.

## sbp-37 — FbaA mechanism/structure

Primary1995 abstract supports carbonyl substrates, Zn-dependent enediol(ate)-DHAP intermediate and pH dependence;2003 Cd substitution structure distinguishes catalytic and structural metal positions.

**Disposition:** Retain primary abstract/native scope only, no Cd cofactor or direct inhibition claim inferred from a crystal.

**Bound sources:** 3.

## sbp-38 — FbaA modification conflict

1988 labeling supports phosphate-associated FbaA, while1995 mass analysis ruled out phosphorylation for its +76Da mercaptoethanol adduct at source Cys36 with no significant activity effect;2022 phosphoproteome annotation is a different source.

**Disposition:** Keep distinct preparations and evidence roles, no unique constitutively phosphorylated active identity.

**Bound sources:** 3.

## sbp-39 — FbaA synthetic inhibitors

N-sulfonyl hydroxamate phosphate derivatives competitively inhibit classII canonical FBP reaction; phosphonate isosteres are weaker.

**Disposition:** Retain bounded synthetic-inhibitor context, no invented exact chemical CURIE or physiological effector.

**Bound sources:** 2.

## sbp-40 — 2019 NMR

2019 ASKA His-tagged screen detected eleven FbaA and six PfkA metabolite interactions in EV2 under its RF/FPR threshold.

**Disposition:** Preserve every listed binder and assay criteria in context; binding alone gives no causal regulatory sign.

**Bound sources:** 3.

## sbp-41 — 2019 activity

FbaA is activated by ATP,3PG and PEP in canonical FBP cleavage at30C; hypoxanthine and IMP have no measurable effect. Concentrations:5mM modifiers,3.22mM hypoxanthine,FBP1mM,Mg1mM.

**Disposition:** Add supported signed effects with exact assay and ASKA preparation; not bypass-specific. ATP within expected range,3PG/PEP above physiological range.

**Bound sources:** 3.

## sbp-42 — 2019 source conflict

2019 reports earlier3PG inhibition, whereas its own assay activates; the1995 primary abstract says glycolytic intermediates/ATP did not affect activity.

**Disposition:** Preserve three source statements and access limits. Do not replace signs or infer allostery from similarity alone.

**Bound sources:** 2.

## sbp-43 — 2019 assay controls

FIA TOF-MS combines same-mass DHAP/GAP signals with mixture-specific standards; assays triplicate and calibration quadruplicate.

**Disposition:** Retain method controls and no SBP substrate inference. Appendix generic inhibitor caption does not override measured activation.

**Bound sources:** 2.

## sbp-44 — 2016 binding

2016 NMR paper and2019 comparison detect PfkA binding under different buffers and thresholds;2019 only overlaps some prior interactions.

**Disposition:** Native2016 functional wording is not sufficient for unobserved signed effects; retain binding/source-limited context.

**Bound sources:** 2.

## sbp-45 — Cra transcription

Native Cra repression of pfkA maps promoter recordsPM46536/PM933 to shared BS785; fbaA is in epd-pgk-fbaA with Cra repression through epd promotersBS264.

**Disposition:** Deduplicate shared biological binding site across native transcript-unit records; retain exact gene endpoints and source His6FruR context.

**Bound sources:** 6.

## sbp-46 — Cra assembly

Native CraPC00061 is a tetramer of PD00521/P0ACP1.1994 assembly experiment used six-His FruR; CPLX127 is Cra plus beta-D-fructofuranose1P with no component coefficient asserted.

**Disposition:** Retain exact native assembly and reference chain, distinguish genericF1P assay from beta native ligand and avoid invented ligand stoichiometry.

**Bound sources:** 4.

## sbp-47 — Cra effector conflict

Native and2018 primary abstract support F1P reducing Cra DNA binding, and report FBP neither binds nor impairs binding; older2009 discussion repeats FBP effector model.

**Disposition:** Retain negative FBP result and historical conflict; no FBP→Cra inhibition edge. F1P assay anomer unspecified; nativeFRU1Pbeta138881 differs from generic58674.

**Bound sources:** 6.

## sbp-48 — Cra preparation

2021 Cra can cleave at source Asn50 during aging/crystallization, separating DNA and effector domains; NTD retains DNA binding.

**Disposition:** Contextual preparation warning from abstract/native; do not apply cleavage to earlier preparations or create a canonical truncated chain.

**Bound sources:** 2.

## sbp-49 — CRP transcription

Native cAMP-CRP positive epd-pgk-fbaA regulation is qualified by1998 abstract: binding-site deletion has little effect while crp/cya deletion strongly reduces P0, implying an indirect glucose response.

**Disposition:** Do not label the inferred fbaA expression effect as proven direct CRP activation at its own promoter.

**Bound sources:** 3.

## sbp-50 — CRP effector/assembly

Native CPLX0-226 contains CRP dimerPC00004 and cAMP; dimer contains two PD00257/P0ACJ8 chains. No cAMP coefficient is provided.

**Disposition:** Retain native active-complex identity, effector58165 and known dimer stoichiometry only.

**Bound sources:** 4.

## sbp-51 — PTS context

1998 abstract implicates ptsG-encoded IICBGlc in positive glucose regulation of epd P0.

**Disposition:** Retain indirect expression context; do not substitute crr-encoded IIA or invent pathway sugar transport.

**Bound sources:** 3.

## sbp-52 — RpoS/RpoD

2009 JM101-derived PB11/PB12 PTS-deficient cells and rpoS deletions support sigma38-dependent expression contexts for pfkA/fbaA. Reconstituted core RNAP plus His-tagged RpoS or RpoD transcribes pfkA first promoter.

**Disposition:** Preserve direct reconstituted assay versus indirect fbaA expression; reference sigma chain is not an autonomous polymerase.

**Bound sources:** 3.

## sbp-53 — RpoS constructs

RpoS/RpoD were cloned pET28b+ and expressed in ER2566; purified His-sigma plus commercial RNAP core at1:5 ratio. PB11/PB12 are JM101 ΔptsH ptsI crr derivatives, not BW25113 talAB.

**Disposition:** Separate source constructs and physiological cohorts; preserve source MG1665 spelling and promoter pykA/pfkA typo as source discrepancies.

**Bound sources:** 3.

## sbp-54 — operon/RNA

epd-pgk-fbaA is cotranscribed;2005 abstract describes RNaseE cleavage/segment stability;2009 found no immediate fbaA promoter in tested conditions.

**Disposition:** Retain RNA-processing context without invented RNaseE signed enzyme edge or general absence of promoters.

**Bound sources:** 3.

## sbp-55 — CsrA expression

csrA51 hypomorphic cells in M9glucose reduce PfkA expression and restoring PfkA partially rescues glucose growth/stress.

**Disposition:** Positive expression context with allele limitation; abstract/native evidence does not demonstrate a new pfkA RNA binding site.

**Bound sources:** 3.

## sbp-56 — indirect deletions

2011 BW25113 cyoA,cydB,fnr,fur single deletions increase pfkA transcript in aerobic carbon/nitrogen-limited continuous cultures, with broader network shifts.

**Disposition:** Keep each deletion comparison and tested C/N conditions; no direct binding or claim of active anaerobic FNR state under oxygen.

**Bound sources:** 4.

## sbp-57 — environment

Native pfkA context reports acid response under aerobic but not microaerobic conditions from23274360.

**Disposition:** Retain source-qualified environmental context; no specific unmeasured PhoB→pfkA binding edge.

**Bound sources:** 2.

## sbp-58 — interfaces

Native PathBank PPP child connects S7P input and E4P output, glycolysis/PDH child connects DHAP output.

**Disposition:** Retain opaque exact child IDs and original compound conflicts; no stoichiometric expansion, transporter or causal regulatory sign from SubPathwayInteraction marker.

**Bound sources:** 1.

## sbp-59 — novelty

Existing Calvin and riboneogenesis use reverse E4P+DHAP condensation plus SBP hydrolysis; nonoxidative PPP transaldolase uses S7P+GAP; ADPheptose isomerizes S7P.

**Disposition:** These are related routes, not the two-event ATP bypass. Preserve prior lead mentions and explicit PPi next231 comparison.

**Bound sources:** 2.

## sbp-60 — scope boundary

Native PfkA NAD kinase prediction, engineered antisense/production applications and FbaA ts8/h8/RNA/engineered substrate variants are broader enzyme contexts.

**Disposition:** Preserve as annotated context/disposition, not unsupported extra bypass events or universal flux. No physical channeling complex from1995 speculation.

**Bound sources:** 3.

## sbp-61 — FbaA localization

FbaA native monomer is located in CCI-CYTOSOL-GN; UniProt carries GO0005829 cytosol with IDA:EcoCyc evidence citing15911532 and18304323.

**Disposition:** Retain cytosol identity and annotation evidence role; do not derive location from homodimer SUBUNIT text.

**Bound sources:** 2.
