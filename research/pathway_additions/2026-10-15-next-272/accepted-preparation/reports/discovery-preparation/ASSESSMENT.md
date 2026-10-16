# Ethanolamine utilization: bounded candidate assessment

## Identity and full source boundary

The candidate is **MetaCyc:PWY0-1477 — ethanolamine utilization**, obtained from `https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?META:PWY0-1477`. The response identifies one exact META Pathway, full detail, and PGDB/Pathway Tools 27.0. The literal XML base contains the source's HTTP/443 spelling; navigation and acquisition provenance use the successful HTTPS URL. `native-complete-own-slot-projections.json` preserves every own slot and `complete-root-slot-dispositions.json` disposes all 21 root occurrences.

This is an elementary branched biochemical route, not a superpathway, single reaction, isolated enzyme, taxon-only prediction or support-model subsystem. Native root membership is:

| Native member | Selected pathway direction | Complete selected native equation |
| --- | --- | --- |
| ETHAMLY-RXN | L2R | ETHANOL-AMINE → AMMONIUM + ACETALD |
| ACETALD-DEHYDROG-RXN | L2R | ACETALD + CO-A + NAD → ACETYL-COA + NADH + PROTON |
| PHOSACETYLTRANS-RXN | L2R | Pi + ACETYL-COA → ACETYL-P + CO-A |
| ACETATEKIN-RXN | R2L | ADP + ACETYL-P → ATP + ACET |
| ALCOHOL-DEHYDROG-RXN | R2L | ACETALD + NADH + PROTON → ETOH + NAD |

There are five memberships, four explicit predecessor links, 22 material occurrences and 14 native material IDs. Every material occurrence has implicit coefficient one and no explicit side compartment. The source-own ETHAMLY direction is LEFT-TO-RIGHT; all four other Reaction-own directions are REVERSIBLE. Preserve these separately from the selected pathway directions. The route branches after ETHAMLY: one branch consumes acetaldehyde in alcohol reduction, the other converts it to acetyl-CoA and then acetate. Do not sum one copy of each branch and call it a complete physiological net or impose an unmeasured flux ratio.

Acetate excretion is a textual root pathway-link. It is not an issued transport reaction. Adjacent propanediol utilization PWY-7013, phosphatidylethanolamine supply, acetate recapture by Acs, the TCA/glyoxylate pathways and cobalamin biosynthesis are contextual connections, not extra native members. Their relevant molecular interactions can be researched with exact scope; they must not disappear merely because they are outside the five reaction list.

Two direct native species entries are strains: E. coli K-12 MG1655 (native NCBI link 511145) and S. enterica subsp. enterica serovar Typhimurium LT2 (99287). The Bacteria taxonomic-range slot is broader context. Narrative mentions of full and short operons in other taxa do not establish all five reactions or a universal shell mechanism. Current taxonomy and primary experimental strain identities remain to be checked.

QuickGO's current GO:0046336 defines ethanolamine catabolism broadly and supplies breakdown/catabolism/degradation synonyms. It does not specify this five-member microcompartment route. It is a grounding lead, not accepted exact equivalence. Native EcoCyc:PWY0-1477 unification also needs independent counterpart inspection. A live KEGG module text search for ethanolamine returned M00092 and M00093 phosphatidylethanolamine biosynthesis modules; these are not candidate aliases. That bounded query is not proof that KEGG has no ethanolamine catabolic route.

## Distinctness and prior work

The exact root ID and label are absent from all 267 landed record roots and the one pending acetate root. This is a complete maintained-root check, not global novelty.

Existing chemistry is substantial and should be reused honestly. The complete retained Rhea quartet table places the five native xref leads in families 15313, 25290, 23288, 11352 and 19521. The older committed selected-quartet table omits two of these; absence there is not issuer invalidity. The aromatic pathways PWY-5415, PWY-5420 and PWY0-1277 contain RHEA:23289 acetaldehyde-dehydrogenase chemistry. Their E. coli heterologous EutE and Salmonella LT2 genetic EutE contexts do not amount to an ethanolamine pathway. The prior261/262 decisions explicitly distinguish those component and preparation scopes; retain them.

The landed Thermotoga PWY0-1312 contains the Pta/Ack acetate/ATP-producing module. The yeast GO-CAM ethanol-degradation record contains `gomodel:ALCOHOL-DEHYDROG-RXN` and selects ethanol oxidation followed by aldehyde oxidation/acetate activation. Those boundaries lack ethanolamine cleavage and the native branched utilization context. The pending acetate-methanogenesis route shares native Ack/Pta but selects the opposite physiological direction. Shared reactions or a pathway cited as a reference do not establish duplicate pathway identity.

Prior ordinary-text mentions include the cross-Mech priority list, EutE protein/authority/context records, acetaldehyde/ammonium reaction backlinks, and old support/report copies. The ignored SEED menu contains an ethanolamine-utilization selector, not an accepted biochemical graph. The retained old iModulon search mentions EutT as a cobalamin-related gene; it is not a new Eut module analysis. The selected 116-gzip history search found 17 files with candidate, shared-reaction, paper or numeric matches. Relevant pathway and EutE contexts were inspected. Numeric hits and unrelated shared-reactant history are not evidence of previous full-route curation, rejection or equivalence.

## Primary evidence actually inspected

The retained Europe PMC core response contains 11 exact MED records. Their complete supplied abstracts were read; PMID:784902 and PMID:1090845 have no supplied abstract. Metadata alone is not mechanism evidence. PMID:23920494 is a review, not a new primary experiment.

| Source | Actual reading and supported preflight implication |
| --- | --- |
| PMID:16291677, Brinsmade et al. 2005, PMC1291257 | Original PMC HTML retained. Targeted abstract, strain/culture methods, mutant/complementation results and discussion read. LT2 derivatives under altered expression, glutathione and oxygen conditions can bypass shell requirements. This does not justify deleting the native shell context or treating every gene as universally essential. Genetic rescue is not a purified EutE assay. |
| PMID:16585748, Penrod/Roth 2006, PMC1447003 | Original PMC HTML retained. Targeted abstract, growth/release results and discussion read. Shell and eutG phenotypes depend on pH/gas exchange; endogenous aldehyde toxicity was not generally observed under the tested conditions. The low-pH/acetal explanation and alternative pathway are proposals. EutD background-dependent discrepancies are explicitly discussed. No figure-image, full-table or supplement audit is claimed. |
| PMID:23585538, Huseby/Roth 2013 | Complete retained abstract read. Genetic tests support private NAD/CoA recycling, with conditional importance of EutD/EutG. The external EutBC position is a model prediction. Full XML requests returned HTTP500 and the direct PMC HTML request returned a CAPTCHA document; neither is credited as main text. Obtain the main and relevant supplements before adopting detailed compartment claims. |
| PMID:14996820, Brinsmade/Escalante-Semerena 2004 | Complete retained abstract read. EutD product identification supports acetyl-CoA formation in the tested direction and rescue of acetate growth. Full XML/HTML access was unsuccessful, with raw failure bodies retained. Native catabolic direction still requires assay-specific interpretation. |
| PMID:7868611; PMID:10464203 | Complete abstracts read. Operon/mutant and shell-homology evidence is conditional, not universal localization or proof of every inferred enzyme. Native EutE/EutG assignments require full papers and preparation resolution. |
| PMID:6374020 | Complete abstract read. E. coli enzyme induction/isoenzyme evidence; exact strain and preparation remain to be closed from main text. Do not substitute it silently for MG1655-specific proof. |
| PMID:15516577 | Complete abstract read. EutT supplies adenosylation during high demand; EutA protective effects are distinct. These are cofactor-management context, not an extra native member reaction. |

No source-database paragraph is treated as a quotation from its cited paper. Raw HTML failure bodies are explicitly identified as access failures. No browser/PDF-image inspection, main-text reading of the inaccessible papers, or complete primary closure is claimed.

## Concrete prerequisites for source preparation and curation

1. Close the 71 low-detail activity occurrences into complete activity/enzyme/complex/component originals. Decide every candidate's route relevance, taxon, evidence code, preparation, cofactor, location and regulation. Broad alcohol/Ack/Pta/aldehyde reaction lists include unrelated species and side activities; a backlink does not certify an ethanolamine catalyst.
2. Preserve the whole Eut microcompartment mechanism. Research exact shell-protein identities/composition, cargo association and compartment identities; EutBC subunits; EutE, EutD and EutG; EutA reactivation; EutT/cobalamin handling; EutR induction; EutH membrane entry; and any other full-source operon assertions. Distinguish physical composition, catalytic activity, transport, regulation and proposed roles. Do not infer that all five reactions occur inside the lumen, locate Ack there by convenience, or invent a membrane-bounded compartment.
3. Obtain the 2013 main/relevant supplement, 2004 EutD main, exact EutBC and EutG biochemical papers, and source-selected regulator/transport/localization evidence. Resolve the 2005/2006/2013 condition/genetic-background differences without choosing only convenient statements. Keep mutant and heterologous constructs local to their claims, and distinguish predicted compartment organization from measured location.
4. Inspect all 14 native material originals and external issuing records for any chosen aliases. Verify protonation, coefficients and compartment-unspecified status. Check each Rhea/KEGG/MetaNetX lead against actual equations rather than frame-name similarity. A generic family or an EC label is not a protein identity. ACETATEKIN-RXN currently reports EC-2.7.2.15 despite its ATP/acetate equation and acetate-kinase activities; investigate and preserve this anomaly rather than silently replace it. All five Reaction common-name slots are absent, so any naming fallback requires explicit authority policy review.
5. Rebind to actual271 merged records, authority sources and code. Reuse accepted source owners where exact bytes/semantics agree; the 20 core IDs have 7 landed and 13 prospective source-snapshot owners. Missing native snapshot terms do not mean issuing IDs are invalid. The biological closure will increase the eventual identifier set.
6. Repeat exact alias/source/primary deduplication as identities expand. Read any newly uncovered historical disposition. The current search is bounded, especially archives and alternative-source coverage. Neither this candidate nor the remaining sulfate lead exhausts pathway discovery.
7. Obtain independent preflight/source/issuer/graph reviews before maintained authoring, then governed record review, generated pages and full repository checks. Current iModulon applicability must be assessed at scientific review, rather than reusing the old cobalamin search as route validation.

## Unresolved sulfate comparison

Current issue410's full body and empty comments were read from authenticated GitHub. Its donor-specific DsrC gap remains open. Newly acquired DISSULFRED-PWY and all five member Reaction bodies establish the native source version and boundary only; they do not satisfy that experimental prerequisite. The source's Bilophila strain association and broad generic commentary also require careful scope review if that task resumes. No new sulfate scientific acceptance, rejection or closure is issued here. The prior hold and fresh failed/successful requests remain visible.
