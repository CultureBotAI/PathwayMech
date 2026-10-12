# Ethylene glycol degradation: full preflight author handoff

**Decision: viable for full authoring of MetaCyc:PWY0-1280, with the bounded evidence and unresolved details below.** The exact two-event pathway is novel against the observed 227-record baseline plus the two explicitly bound prospective records. This is a source-complete disposition of the selected scope, not a claim that every literature item or supplement was accessible. No record, canonical cache, repository code or Git state was changed.

Baseline: actual 227 at `6435622d08d0a3a8998968eaa96736c702550e9c`, tree `428c9ff0ab1294c2e4b5d6059d45a40ddf096974`, observed root `/private/tmp/pathwaymech-next-226-20261012`. Prospective lyxose `8ca651dc70a0dda2620ba09719a4e6861517d39f1736ca1971f283900accc121` and original MG `08fe9a6f3f0da2f66c4dc6cd68fc33fbe51a38770b6eeee743751f05f019d088` were included; their later successors/adoption do not retroactively alter this baseline.

The sealed root lead packet was verified (52 artifacts, manifest `4e585854345e0807da2eb7697754b2ed019bed412aa3a24b40e1f68610aa4203`). Its limited-read statements are superseded only where this preflight records actual additional reads. All original bindings are in `external-original-bindings.json` and `source-support-bindings.json`.

## Novelty and full boundary

`derived/novelty-v3-adjudication.json` contains all 227 actual and two prospective parsed record signatures. The repository search included ignored/hidden files and followed links, excluding only `.git` and `.venv`; 267 files matched broad cues. No exact pathway ID, defining reaction ID or complete candidate participant-side signature was represented. V3 deliberately removes the erroneous default coefficient=1 in earlier screen projections; candidate stoichiometry comes independently from Rhea originals, not that heuristic.

The earlier PathBank screening rejection was unresolved root/child membership, not a demonstrated duplicate. The existing D-arabinose record has Rhea13850/17602 (isomerization/phosphorylation), not EG oxidation. Existing fucose records cover their sugar core, not this two-event route. Allantoin/ureidoglycolate and yeast folate matches share words or metabolites; EGTA and PEG are reagents. The methylglyoxal protein report describes GldA glycolaldehyde reduction and Gpr promiscuity: related activities, not a curated two-event oxidative EG pathway. Prior-source adjudication and exact record/projection hashes are retained.

Core chemistry is Rhea27631 followed by20002: eleven side assertions, two NAD reduced, one water consumed and three protons produced overall. Complete pathway means both core events plus supported assembly, cofactor, inhibition, expression and native interface context. It does not mean adding the complete downstream glyoxylate-assimilation superpathway.

## Author dispositions required

### EG01-full-boundary — core

PWY0-1280 is an exact two-event oxidative pathway from ethylene glycol through glycolaldehyde to glycolate, ordered GLYCOLALDREDUCT-RXN then GLYCOLALD-DEHYDROG-RXN. It is neither a one-enzyme record nor a glycolate-assimilation umbrella.

Use MetaCyc:PWY0-1280 for the full definition. Downstream glycolate/glyoxylate routes are interfaces, not silently added core events. META and ECOLI version 27.0 differ in outgoing context. Broad native taxonomic range is not experimental degradation proof for every taxon.

Sources: `native-scope`, `ecoli-scope`, `1983` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG02-event1 — core

RHEA:27631: ethylene glycol (CHEBI:30742) + NAD(+) (57540) -> glycolaldehyde (17071) + NADH (57945) + H(+) (15378), each coefficient one. RHEA:27630 is master, 27632 reverse, 27633 bidirectional.

Oxidative route direction is supported independently of reversible enzyme chemistry. Achiral substrate/product require no anomer. Do not use the initial mistaken 27633-as-master extraction or 27634–27636 search-family lead.

Sources: `Rhea`, `native-E1`, `1983` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG03-event2 — core

RHEA:20002: glycolaldehyde + NAD(+) + water (15377) -> glycolate (29805) + NADH + 2 H(+). Master 20001, reverse 20003, bidirectional 20004.

Eleven core side assertions total (five plus six); coefficient two for event-2 proton must be explicit in evidence. Native ECOLI reaction comment accidentally repeats glycolate as substrate; participant fields and primary chemistry resolve it.

Sources: `Rhea`, `native-E2`, `1983`, `2006` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG04-balance-energy — core

Both reactions balance elements and charge in the retained Rhea 142 original. Net: EG + 2 NAD(+) + water -> glycolate + 2 NADH + 3 H(+).

NAD(+) 57540 is charge -1, NADH 57945 charge -2 in these exact chemical species. No ATP, O2 consumption, proton symport or respiratory chain is a core reaction side. Reoxidation of NADH is cellular context; energy yield is not fixed by this record.

Sources: `Rhea` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG05-FucO-identity — identity

Native LACTALDREDUCT-CPLX catalysis joins FucO P0A9S1, fucO/b2799/JW2770, EcoCyc EG10351, Entrez 947273, MG1655 NP_417279. Current UniProt sequence is 382 aa; the old secondary accession P11549 and 383-aa paper numbering are historical.

UniProt K-12 taxon 83333 is distinct from GeneID MG1655 taxon 511145 and selected E15 strains. P0A9S1 also cross-references Shigella GeneID 93779199; do not select it for MG1655. Fresh sequence numbering must not be silently substituted into older mutant descriptions.

Sources: `native-FucO`, `native-E1`, `UP-FucO`, `genes` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG06-AldA-identity — identity

Native ALD-CPLX joins P25553/AldA, aldA or ald, b1415/JW1412, EG10035, Entrez 945672, MG1655 NP_415933; current protein is 479 aa.

Author the actual accession and source-version joins. Gene/protein identity is not proof that unmodified MG1655 grows on EG alone. Native cytosolic GO annotation is database evidence, not a freshly inspected localization experiment.

Sources: `native-AldA`, `native-E2`, `UP-AldA`, `genes` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG07-assemblies — assembly

FucO is a homodimer, native coefficient 2; AldA is a homotetramer, native coefficient 4. FucO 2005 structure supports N-terminal domain swapping and loss of assembly/activity after N-terminal deletion. AldA 2006 ultracentrifugation and 2007 crystal independently support tetramer.

Use exact native complex identities, not a monomer falsely carrying assembly stoichiometry. FucO ΔN10 historical construct is not the current 382-aa reference deletion without alignment. Older AldA dimer estimate conflicts with later tetramer data; preserve the conflict, use supported tetramer.

Sources: `native-FucO`, `native-AldA`, `2005`, `2006`, `2007` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG08-FucO-metal — cofactor

FucO has one iron site per subunit in the 2005 structure. Historical residue ligands are Asp196, His200, His263, His277. Fe content measured in preparation was about 0.53 per subunit; mutants D196/H200 lost detectable binding.

Crystal site count is not proof of full solution occupancy in every preparation. Older H267 ligand assignment is superseded by later structure; H267 participates in a proposed proton network. Current P0A9S1 numbering shifts after the historical initial residue; preserve paper positions explicitly.

Sources: `2005`, `2023`, `native-E1` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG09-FucO-zinc — qualified inhibition

Native REG0-9194 and direct 2005 experiment support Zn(II) inhibition of FucO. The primary assay measures glycolaldehyde reduction; added iron protects against zinc inhibition.

Retain the measured direction/substrate and metal concentrations (Fig4: 0.1 mM Zn; tested added Fe 0.1 or 1 mM). Do not present this as a direct EG-oxidation-specific IC50 or physiological zinc regulation.

Sources: `FucO-Zn`, `2005` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG10-FucO-coenzyme — qualified biochemical context

2005 structure has two coenzyme sites per dimer. G97E abolished tested activity whereas G17D did not; D39G allowed NADPH use. The historical wild type prefers NAD(H).

Mutant cofactor expansion is not wild-type NADPH-dependent EG oxidation. The 2023 reduction work uses 0.4 mM NADH and is not a measured EG oxidation kinetic dataset. Native EG Km ~7 mM cites PMID4306747, whose abstract rather than full paper was inspected.

Sources: `2005`, `UP-FucO` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG11-FucO-2023-network — qualified mechanistic context

The 2023 FucO study reports positive substrate cooperativity and preliminary ordered Bi-Bi interpretation during L-lactaldehyde reduction; H267Q/D360N retain activity with altered apparent substrate response. Chemistry is implicated in the reduction rate limit by deuterium effects.

Hill K0.5 is not Michaelis Km; cooperative behavior limits ordered-mechanism inference. Neither residue is established as the unique rate-limiting base. EG is achiral, so L-lactaldehyde stereoselectivity cannot be copied into its mechanism.

Sources: `2023` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG12-FucO-crystal-EG — scope exclusion with retained context

2023 N151G/L259V crystal 7QNF includes ethylene glycol used as cryoprotectant and ADPR; nicotinamide density is unresolved. Open apo L259V 7QNI lacks Fe and coenzyme; holo F254I 7R5T is closed.

Do not assert a productive WT EG/NAD ternary intermediate from this mutant cryoprotection structure. Keep mutant construct/state on any structural context; the 2005 attempted glycolaldehyde complex also lacked substrate density.

Sources: `2023` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG13-AldA-glycolaldehyde-assays — direct catalysis

AldA directly oxidizes glycolaldehyde. 2006 Table1 reports Km 0.14 mM and kcat 1100 min-1; 1983 crude extracts and product chromatography independently support glycolate production. 2019 purified MG1655-derived His-tag AldA assay also directly uses glycolaldehyde.

Do not combine assay values: 1983 pH9.5/25°C versus 2006 phosphate pH7.5 and 2019 Tris pH7.5/37°C with 10 mM Mg. The 2019 Table4 reported Vmax/kcat are internally inconsistent in units; preserve the report without certifying the numerical conversion.

Sources: `2006`, `1983`, `2019` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG14-AldA-NADH-direct — direct qualified inhibition

Baldoma 1988 Fig5 directly shows NADH inhibition of glycolaldehyde oxidation by purified ECL3 AldA: about half inhibition at 0.45 mM NADH and almost complete inhibition near 1 mM.

Assay: 1 mM glycolaldehyde, 2.5 mM NAD(+), glycine pH9.5, 25°C. This is direct enzyme-product inhibition, distinct from reduced growth or pathway expression. Carry exact assay/strain preparation qualifiers.

Sources: `1988` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG15-AldA-NADH-assay-sign — qualified biochemical context

2006 NADH competition and Mg inhibition were measured using propionaldehyde dehydrogenase activity. NADH activates the separate esterase assay, so activity signs differ by measured function.

2006 Tables4–6: NADH Ki 157±40 µM; 2/10 mM Mg leaves about 55/44% dehydrogenase activity. Esterase NADH activation ~2.4-fold is not activation of EG pathway catalysis. F180T 2008 is engineered, not wild type; mutant Ki/abstract values differ slightly.

Sources: `2006`, `2008` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG16-AldA-native-inhibition — qualified native mechanism

Native REG0-9207 assigns glycolaldehyde substrate inhibition; REG0-9208 assigns Zn(II) inhibition. Preserve both even though the oldest complete PDF is unavailable.

These are explicit curated native assertions linked to PMID3308886, not primary quotations. Contemporary assay concentrations can support activity while differing in inhibition; no single physiological threshold inferred.

Sources: `AldA-substrate`, `AldA-Zn`, `native-E2` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG17-AldA-old-primary-details — qualified indexed primary context

The 1987 text identifies JA-102 as earlier EG3, reports tetrameric enzyme, four NAD-binding sites, glycolaldehyde Km 0.38 mM, NAD Km 0.28 mM in that assay, and substrate inhibition above an optimum near 1 mM. NADP 6.25 mM is Km, not Kd. Ion inhibition includes Zn and Cu; exact OCR values remain source-bound.

Indexed primary text rather than acquired original PDF; see explicit retained-line limits. Do not reverse Zn/Cu values based on secondary snippets, call NADP Km a binding constant, or imply inhibitor effects in native intracellular conditions. This row is the bounded, copyright-safe summary of the indexed 1987 source.

Sources: `1987` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG18-AldA-structural-mechanism — qualified mechanistic context

2007 endogenous AldA from BL21(DE3) co-purified as a contaminant of His-tagged taxadiene synthase; AldA itself was not the tagged target. Crystal/model work supports C285/E251 roles and coenzyme conformations, with lactate/NADH partial occupancies.

Mechanism proposed for lactaldehyde; no direct glycolaldehyde covalent intermediate measurement. NADPH can bind in crystals despite poor functional cofactor activity. Hg/Pt/Sm/Mg crystallization or derivative conditions are not evidence for physiological metal cofactors.

Sources: `2007` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG19-foundation-lineage — taxon and strain

Boronat 1983 begins with E15 strain1, EMS-derived strain3, G1/G3 glycolate-positive derivatives and EG-selected EG3 from G3. EG3 was selected with EG plus small initial glucose supplementation then purified on EG-only plates.

Keep E15/G1/G3/EG3 names and unresolved genetic lesion identity. Modern accession joins identify the enzyme family, not a claim that these historical strains are MG1655. Native comment says two mutations; primary Discussion leaves one versus two unresolved.

Sources: `1983` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG20-foundation-assays — direct physiological support

1983 selected cells show increased EG oxidation and glycolaldehyde dehydrogenase, labelled glycolaldehyde/glycolate intermediates, chromatographic glycolate product, and linked fucose/propanediol phenotypes. The EG oxidation assay used 250 mM EG and 0.33 mM NAD at pH9.5, 25°C.

G1/G3/EG3 CAA crude FucO activities 0.005/0.130/0.415 U per mg and AldA 0.145/0.165/0.560 are strain/condition specific. P1 transduction is genetic association, not a sequenced allele or protein accession proof. 1983 identity paper was abstract only.

Sources: `1983`, `1983identity` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG21-uptake-effects — qualified physiological context

1983 EG3 labelled-EG uptake is higher than G1/G3. Table2 co-substrate effects (25 mM) are control100, glucose105, acetate72, malate54, glyoxylate48, glycolate39 and glycolaldehyde18 relative uptake.

Preserve the full tested set. Authors discuss isotope dilution/mass action; these are not direct binding or inhibition assays of a named transporter. No resolved transport protein, transport stoichiometry, or EG/H symport was established.

Sources: `1983` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG22-transport-boundary — unknown retained

Passive EG diffusion is proposed in early interpretation and assumed in a modern flux model; proton symport is a discussed alternative.

No supported named transporter or obligatory energy coupling. Preserve uncertainty in research/record description; do not invent a transport reaction or turn an FBA assumption into experimental evidence.

Sources: `1983`, `2021` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG23-1988-induction — qualified expression context

Baldoma 1988 sugar-mutant comparisons support a proposed role of L-lactaldehyde in ald expression, with stronger aerobic induction. The enzyme remains stable after anaerobic shifts under tested carbon supply but carbon starvation causes activity loss without immediate protein degradation.

ECL1/ECL3, JA104, JA105, ET6016 and ECL493 genetic states must remain visible. Direct addition of lactaldehyde arrested growth rather than providing a clean induction test; regulator identity remains unresolved. Do not assert direct effector binding from these experiments.

Sources: `1988` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG24-CRP-aldA — direct binding plus expression

Limon 1997 directly supports CRP-cAMP promoter binding and positive aldA expression. Proximal site centered near -60 is protected around -47 to -74; distal -134 consensus did not bind in the test.

Purified CRP binding used 20 µM cAMP. Exogenous 5 mM cAMP partly relieved glucose repression; glycerol repression was cAMP-independent. Keep proximal physical evidence separate from distal motif similarity, and use CRP-cAMP state/native assembly.

Sources: `1997`, `CRP-ald-reg` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG25-unknown-ald-regulator — unresolved identity retained

1997 ECL1 crude extracts form complexes with the aldA -59 to -6 region; glycolaldehyde or 2-oxoglutarate increases the observed binding. The binding factor was not identified.

Retain as source/condition context without inventing a regulator protein or direct purified effector-binding edge. Higher bands suggesting multimerization are a hypothesis, not resolved stoichiometry.

Sources: `1997` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG26-ArcA-aldA — qualified negative expression and binding

1997 arcA mutant ECL968 versus parental ECL547 abolishes strong anaerobic aldA repression in the fusion experiment. Native phosphorylated ArcA regulations 5998/5999/6000/6002/6003 cite later binding/mutation work; PMID10071223 abstract supports direct promoter recognition.

Source native ArcA-P state, exact promoter site and study evidence class separately. A consensus motif alone is not physical binding. 1997 rhamnose minimal culture/fusion values are not MG1655 EG-growth measurements; later full binding paper not acquired.

Sources: `1997`, `REG5998`, `REG5999`, `REG6000`, `REG6002`, `REG6003`, `mechanism-abstracts` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG27-IHF-binding — unsigned direct binding; expression negative control

1997 purified IHF bound promoter-containing fragments, while himA and himD mutants showed no significant aldA expression effect under the tested conditions.

Do not create a signed activation/repression edge from binding alone. Native IHF subunits P0A6X7 ihfA/b1712 and P0A6Y1 ihfB/b0912 are verified in raw/ihf-issuing.json. No stoichiometry inferred from absence of complex-original evidence in this preflight.

Sources: `1997` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG28-DnaA-FNR-aldA — qualified curated regulation

Native REG0-6001 assigns negative DnaA-ATP control, and REG0-5997 assigns negative FNR regulation of aldA. PMID11160809 abstract reports DnaA binding/repression; PMID16377617 is anaerobic expression profiling with predicted motifs.

DnaA full publisher paper returned403. Use native model state without claiming the abstract proves ATP-specific binding. FNR motif BS0-7160 is computational and is not direct binding proof. Preserve media and MG1655/fnr mutant context from the abstract.

Sources: `DnaA-reg`, `FNR-reg`, `regulation-abstracts`, `abstracts` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG29-MarA-SoxS-Rob — qualified potentially indirect expression

Native REG0-12708/12709/12710 indicate positive MarA, Rob and SoxS influence on aldA, with explicit possible indirectness and PMID12067348 support.

Do not assert direct promoter binding; full gene-level supplemental data were not read. Preserve native expression-evidence role and study limitation rather than omitting the source-defined regulations.

Sources: `REG12708`, `REG12709`, `REG12710`, `regulation-abstracts` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG30-ArcA-genomics — qualified native expression context

Native REG0-14027 assigns negative ArcA-P influence on aldA from PMID24699140. That full primary study used MG1655 deletion/expression and tagged ChIP comparisons in anaerobic glucose conditions.

Gene-specific supplemental rows were not acquired, so no fresh aldA-specific primary binding or expression result is claimed beyond explicit native assertion. ChIP resolution is regional; modelled flux is not measured pathway flux.

Sources: `ArcA-array`, `2014` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG31-fucAO-native-regulation — qualified curated regulation

Native fucAO TU00135 is positively regulated by CRP-cAMP and FucR-fuculose-1-phosphate. A separate mapped fucO transcript TU0-42697 also exists in the native source.

CRP motif BS00333 is computational. PMID10601201 specifically studies fucPIK; do not transplant that physical mechanism wholesale onto fucAO. Older selected IS5/crp201 states are not reference WT. Preserve native evidence role where full primary fucAO assay details are unavailable.

Sources: `FucO-TU`, `CRP-fuc-reg`, `FucR-reg`, `regulation-abstracts` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG32-SrsR-fucO-expression — direct qualified positive expression

2022 Figure5 directly measures fucO mRNA: ΔsrsR lower by 8.3-fold and SrsR overexpression higher by 23.9-fold, with fucA/fucP/fucR also measured. BW25113 and JW5476 plus pCA24N-derived overexpression/empty-vector controls were compared after 24h LB at37°C.

RT-qPCR with16S normalization, at least three experiments; 0.5 mM IPTG per Methods. The negative plotted deletion fold value denotes lower abundance, not negative RNA concentration. Use positive SrsR-to-fucO expression edge with exact strain/construct and indirectness limits.

Sources: `2022`, `2022fig5`, `SrsR-reg` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG33-SrsR-spacer-binding — direct locus binding

2022 purified C-terminal His-SrsR from W3110 cloned in pET21a/BL21(DE3) binds the fucA/fucP intergenic spacer in gel shift; gSELEX peak and candidate motif occur there.

Physical binding is to the shared promoter region, not independently mapped fucO internal promoter. DNase footprint was performed for yfdP/yfdO, not this locus. Unknown SrsR coinducer remains unknown; do not invent a ligand. Keep purified W3110 protein separate from BW25113 expression assay.

Sources: `2022` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG34-regulator-components — identity and assembly

Issuing ECOLI frames resolve FNR PD00197/P0A9E5/EG10325; CRP dimer PC00004=2×PD00257/P0ACJ8/EG10164; FucR PD00444/P0ACK8/EG10353; DnaA PD03831/P03004/EG10235; ArcA P0A9Q1/EG10061. Native FNR complex CPLX0-7797 contains2 monomers.

Use derived/native-issuing-identity-proposals.json for exact original hashes/components. CRP-cAMP and FucR-ligand binding objects omit some ligand coefficients; do not invent multiplicity. SrsR P52044/G7518/b2921, MarA P0ACH5, SoxS P0A9E2, Rob P0ACI0 come from actual acquired native frames, not the earlier guessed UniProt query results.

Sources: `FNR-reg`, `CRP-ald-reg`, `FucR-reg`, `DnaA-reg` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG35-catabolite-repression — qualified expression context

Eppler 2002 identifies lower AldA protein in MC4100 grown in TB plus glycerol by two-dimensional gels/mass fingerprint. Limon 1997 separates glucose/cAMP effects from glycerol repression.

Do not infer direct glycerol or glycerol-3-phosphate binding to AldA. Eppler malT reporter/EIIA experiments do not prove each intervening regulatory arrow for aldA. Negative expression is a condition-specific observation, not enzyme inhibition.

Sources: `2002`, `1997` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG36-oxygen-FucO — qualified biochemical and engineering context

Native FucO annotations and inspected abstracts support iron/oxygen-dependent enzyme inactivation and selected oxygen-resistant mutants; catalase protection and anaerobic H2O2 effects are described in PMID1730033. Modern EG engineering uses this context.

PMID8120011 proposes His277 oxidation; do not claim universal direct oxygen binding or a stoichiometric O2 reaction in the EG core. Historical I7L/L8V labels require construct qualification/alignment, not automatic current-sequence renumbering.

Sources: `native-FucO`, `mechanism-abstracts`, `2021` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG37-2021-engineering — full-route engineering context

2021 engineered MG1655 overexpresses fucO/aldA variants on pTrc99a, including I7L/L8V and L8M constructs. Oxygen/process conditions affect growth and glycolate production; the two-stage process is engineered physiology.

Media contain2 g/L yeast extract, so do not call all tests sole-organic-carbon EG growth. Free diffusion is an FBA assumption. Do not merge LMSE constructs into wild-type protein evidence or import fixed productivity as a native property.

Sources: `2021` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG38-2024-module-requirements — full-route engineering context

2024 UV-selected EG01 and evolved EG02 are derivatives of MG1655, with engineered four-module comparisons. Figure4 shows native FucO/AldA module alone insufficient in that assay, glycerate module III supports utilization, and combined downstream modules improve it.

Preserve strain/ALE/UV state and plasmid origins. Source body contains a module III/IV wording contradiction resolved against inspected Figure4; no silent rewriting. Defined M9 tests differ from PET hydrolysate with glycine/TPA/MHET. RNA comparisons EG medium versus LB are confounded by media.

Sources: `2024modules` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG39-2024-alternative-enzyme — parallel engineering context

2024 glycolate engineering compares native FucO I7L/L8V, heterologous Gox0313 and PedE alternatives, with fucO/yqhD/glcDEF deletions and aldA expression.

Native FucO route is one compared module; Gox0313/PedE are not interchangeable native core catalysts. MG1655 versus MG1655(DE3) source descriptions conflict; media contain2 g/L yeast extract. Glycolate growth toxicity is not direct AldA enzyme inhibition, and metabolite pools are not flux measurements.

Sources: `2024glycolate` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG40-2024-2025-leads — abstract-only engineering context

PMID39079834 reports FucO engineering with D23E/E222K/G363S and additional L377H construct changes; synonymous/positional changes also alter aldA expression. PMID41308929 reports engineered chromosomal EG assimilation and ALE.

Do not call these naturally growing WT MG1655, or attribute every productivity increase to FucO catalytic activity. Full papers not read. Retain as explicit future evidence leads, not new core chemistry or completed primary mechanisms.

Sources: `abstracts`, `mechanism-abstracts` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG41-reverse-eukaryotic-archaeal — source-defined alternative direction retained

META first-reaction enzyme references include archaeal VNG6270G/Q9HHR2 (MONOMER-124396) and yeast YLL056C/Q12177 (G3O-32155-MONOMER). Native enzyme direction and inspected primary abstracts concern glycolaldehyde reduction to EG.

Retain native reverse contexts without claiming archaeal/yeast two-step EG degradation. Halobacterial high salt and yeast His-tag constructs/cofactor specificity belong to their own reactions. Exact source bodies raw/META-ENZRXN-31359.xml and META-ENZRXN3O-11572.xml bind this distinction.

Sources: `native-scope`, `abstracts` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG42-PathBank-membership — source boundary

Frozen member PW002093.owl has one primary root SMP0002105, exactly two biochemical reactions6109/5957, two catalyses6070/5920, and two attached child pathways SMP0002052 and SMP0000847. FucO and AldA complexes have coefficients2 and4.

Native root membership was resolved before chemistry. ZIP is uniquely bound to original archive SHA b3a9b955…; member SHA816294f1… . Presence of a D-arabinose child does not rename or duplicate the root pathway.

Sources: `PathBank` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG43-PathBank-children — opaque interface retained

PathBank child SMP0002052 (D-arabinose degradation I, PW002038) contains Interaction109875 with glycolaldehyde; child SMP0000847 (glycolate/glyoxylate degradation, PW000827) contains Interaction109876 with glycolic acid.

These are native attached Interaction objects without an asserted sign or resolved biochemical direction. Preserve root-child provenance and uncertainty; never convert a generic interaction into inhibition, transport, or an extra core reaction. Archive-aware authority attachment must be validated at authoring.

Sources: `PathBank` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG44-PathBank-chemistry-conflicts — conflict retained

PathBank names glycolic acid CHEBI17497 whereas Rhea uses glycolate29805; its NAD/NADH protonation differs from the selected Rhea species. Glycolaldehyde has CHEBI17071 but an inconsistent BioCyc DIHYDROXYPHENYLGLYCOLALDEHYDE cross-reference.

Use exact Rhea chemical species for balanced core, retain native conflicts in source ledger. Do not silently equate neutral acid and anion or promote the incompatible BioCyc cross-reference. PathBank event6109 reversible versus source-selected oxidative route is an evidence distinction.

Sources: `PathBank`, `Rhea` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG45-downstream-context — bounded native interfaces

META pathway-links point from glycolate to PWY-6649, GLYOXDEG-PWY and GLYCOLATEMET-PWY, while ECOLI retains GLYCOLATEMET-PWY and superpathway GLYCOL-GLYOXDEG-PWY.

Glycolate oxidase and glycerate/glyoxylate assimilation are required cellular contexts in selected strains, not omitted core events of PWY0-1280. Native links alone support pathway interface, not detailed downstream enzyme stoichiometry in this record.

Sources: `native-scope`, `ecoli-scope`, `1983` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG46-no-transporter-or-unknown-TF-invention — unknowns

No resolved EG transport protein/energy coupling or molecular identity for the 1997 aldehyde-responsive binding factor was established by inspected evidence.

This is scoped uncertainty, not proof that no transporter/regulator exists. Keep these gaps in the record/research, without local invented CURIEs or unsupported absent-field assertions.

Sources: `1983`, `1997`, `2021` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG47-assay-construct-completeness — authoring requirement

Every structural, kinetic, inhibition and expression assertion must retain its protein preparation, source strain, variant and assay direction from the construct ledger.

Reference protein identity does not license the unqualified transfer of N-terminal His tags, BL21 production host, mutant sequence, lattice ligand, or engineering growth phenotype to native MG1655. Where methods only cite another paper, the missing construct details remain unknown.

Sources: `2005`, `2006`, `2007`, `2008`, `2019`, `2022`, `2023` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG48-FucO-reactivation — qualified native activity context

Native FucO monomer comments explicitly report in-vitro reactivation by high NAD concentrations after aerobic inactivation, citing PMID2203757. The inspected abstract confirms respiratory-condition-dependent inactivation but does not give the reactivation assay details.

Retain the native source assertion with its own evidence role. NAD reactivation is different from NAD as a consumed redox cosubstrate. Do not invent concentration, binding mechanism, or an EG-specific activity assay from the abstract.

Sources: `native-FucO-monomer`, `mechanism-abstracts` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG49-native-adjacent-functions — explicit scope disposition

Native monomer comments also cover FucO propanediol/isobutanol and engineered reverse beta-oxidation, mouse colonization and slow-codon translation effects; AldA folate-derived glycolaldehyde removal, other sugar pathways, glucose limitation, oleate induction and environmental expression variation.

Retain native context in the dossier without expanding PWY0-1280 into those complete pathways. AldA/prpC synthetic lethality does not prove PrpC catalyzes the same reaction. Sequence-based succinate-semialdehyde activity prediction is not experimental EG chemistry. These cited papers were not all freshly read; no new direct-regulatory edges should be manufactured.

Sources: `native-FucO-monomer`, `native-AldA-monomer` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

### EG50-metal-and-expression-conflicts — source conflict disposition

PMID4306747 abstract reports activity of partially purified propanediol oxidoreductase with added iron or manganese. Native broad statements that FucO is only active anaerobically or AldA only present aerobically simplify the condition-dependent behavior in primary assays.

Retain manganese as older preparation-specific metal support, not a proven obligatory cofactor of EG oxidation. Preserve residual/stable AldA after anaerobic shift and selected oxygen-resistant FucO variants. Do not convert oxygen/redox conditions into absolute protein absence or universal activity rules.

Sources: `abstracts`, `native-FucO-monomer`, `native-AldA-monomer`, `1988`, `2005` (original hashes and exact locator crosswalk in `source-support-bindings.json`; paragraph ordinals/XPaths in `exact-paragraph-locator-index.json`).

## Assemblies, constructs and source access

`construct-and-assay-ledger.json` retains preparations and state differences for every selected full-text experimental study. `source-read-receipts.json` distinguishes full bodies, original PDFs, indexed primary text, abstracts, native annotations, images and unread supplements. The correct SrsR Figure5 image was independently viewed; it directly contains fucO and resolves an earlier operon-inference gap. The 2024 module Figure4 and six 2006/three 2008 table images were inspected. An acquired file with `.pdf`, `.xml` or `.docx` extension is not necessarily that format; failed/challenge bodies remain explicitly identified.

The indexed 1987 primary summary is intentionally bounded (EG17), with major original access limits preserved. Precise Zn/Cu concentrations are not proposed as universal biological parameters. Native regulation objects carry their own evidence and do not become quotations from unavailable papers.

## Computational context

The fresh iModulonDB search at precise_mg1655 resolved fucO/b2799 and aldA/b1415. A text search for fucO also returned Fucose module73, annotated with SrsR/Crp/RpoD/FucR, but this search response alone does not demonstrate gene membership or causal regulation. Exact gene-ID queries returned genes and no modules. Retain this only as computational search context; do not infer an aldA module absence or replace primary SrsR/CRP evidence.

## Remaining gates and limits

- No source exhaustion claim; no claim to have read every cited paper or supplement.
- PMID6345530 is abstract-only. PMID3308886 major indexed primary text inspected, but original PDF was not obtained. Paper-specific access limits are mandatory in authoring evidence roles.
- DnaA2001 full publisher body403; FNR/MarA/SoxS/Rob gene-level full results not freshly read. Explicit curated native mechanisms may be retained with native evidence roles and indirectness, not invented direct physical claims.
- Federowicz2014 whole body was read but aldA-specific supplemental rows/GEO data were not. Native REG0-14027 is the exact available gene-specific support.
- Limon1997 full body was read; complete strain-table cells/figure image panels were not acquired. Only body-stated constructs are established.
- Several structural/engineering supplements remain unread; 2023 earlier expression methods are by reference. Do not infer missing tags, preparation states or variant boundaries.
- No EG transporter identity or coupling stoichiometry; no identity for the aldehyde-responsive factor; SrsR effector unknown. These are preserved unknowns, not evidence of absence.
- PathBank archive root/child identities and Interaction attachment need canonical consumer validation during authoring; preflight did not mutate adapter code or canonical cache.
- No YAML was authored in this task; schema/strict/identifier/render/full-test gates were therefore not run and are not claimed to pass.
- Native source-derived node proposals must be validated against actual issuing bodies by the authoring/canonical workflow; no snapshot-label seed substitutions.

Author acceptance should verify both ordered reactions and all eleven coefficients/sides; all 50 ledger keys must be retained or explicitly disposed with source proof. Require source-specific strain, construct, assay direction and inference qualifiers; bind every evidence role to a valid local reference/locator. In particular preserve uptake co-substrate observations, NADH’s opposite signs in dehydrogenase versus esterase assays, IHF binding without an expression effect, the unidentified aldehyde-responsive factor, historical FucO numbering and both PathBank child interfaces.

Then perform schema/strict/identifier gates, edge/reference/qualifier replay, independent scientific review and a canonical authority build before adoption. This preflight does not certify those later steps and does not authorize hand insertion into authority outputs. Source exhaustion remains false.
