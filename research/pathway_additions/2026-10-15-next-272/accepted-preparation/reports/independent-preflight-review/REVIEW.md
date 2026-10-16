# Independent next272 preflight review

Qualified acceptance for complete source preparation of **MetaCyc:PWY0-1477, ethanolamine utilization**. No actionable defect was found in the frozen discovery packet at this preflight scope. This is not acceptance of a maintained record, identifier adapter, complete biological mechanism, or exhaustive pathway discovery.

The reviewed author is `/root/next272_candidate_discovery`; this reviewer is `/root/next268_reaction_review_completion`. I did not author the candidate or its discovery packet. My earlier next270/271 reviews do not substitute for the checks reported here. The source release is bound by manifest `3b9ffe9f7c87c7d924aa6a2a5ac701ac9c5c5f01a04e1f0fd66935a88c8c7206`. All 408 listed files and both integrity-envelope files were independently inventoried, hashed and copied before review. Local `add-pathway` guidance and applicable curation, harmonization and graph contracts were read.

## Candidate identity and source boundary

Direct XML replay confirms one exact full META 27.0 Pathway, 21 own root slots, five Reaction members, four predecessor links and 22 material occurrences across 14 material IDs. Each of the 21 root-slot dispositions matches the corresponding original XML, including the direct species and broader range distinction. The five selected equations are:

| Member | Pathway traversal | Inputs → outputs |
| --- | --- | --- |
| ETHAMLY-RXN | L2R | ETHANOL-AMINE → AMMONIUM + ACETALD |
| ACETALD-DEHYDROG-RXN | L2R | ACETALD + CO-A + NAD → ACETYL-COA + NADH + PROTON |
| PHOSACETYLTRANS-RXN | L2R | Pi + ACETYL-COA → ACETYL-P + CO-A |
| ACETATEKIN-RXN | R2L | ADP + ACETYL-P → ATP + ACET |
| ALCOHOL-DEHYDROG-RXN | R2L | ACETALD + NADH + PROTON → ETOH + NAD |

The Reaction-own direction is LEFT-TO-RIGHT only for ETHAMLY; the other four are REVERSIBLE. These are separate from the pathway traversal. Every material coefficient is omitted in the source, with effective multiplicity one; no side compartment is supplied. Both acetaldehyde branches must remain. Neither a one-copy sum nor an unmeasured branch ratio establishes a physiological net flux. Acetate excretion is a textual pathway link, not an issued transport equation.

All 71 attached Enzymatic-Reaction occurrences are low-detail, with 71 distinct IDs. They are unresolved biological closure leads, not 71 demonstrated ethanolamine catalysts. The full root's broad microcompartment narrative and its assumed EutE assignment do not establish every enzyme's lumen location or purified activity. EutBC subunits, EutE/D/G, shell composition, EutA/T cofactor handling, EutR regulation, EutH entry and source-selected ancillary roles remain necessary preparation scope; unrelated shared-reaction catalysts require explicit dispositions rather than automatic inclusion. Adjacent propanediol, phosphatidylethanolamine supply, Acs recapture and central metabolism remain visible context without becoming extra native members by inference.

The direct native taxa are E. coli K-12 MG1655 and Salmonella Typhimurium LT2. The Bacteria range and narrative full/short-operon distributions are not proof of a universal five-reaction microcompartment route. LT2 derivative experiments cannot silently become MG1655 experiments. Material formulas, charge/stereo and independent issuer equivalences have not been accepted here. The ATP/acetate equation's native EC-2.7.2.15 assignment is an explicit unresolved source anomaly. All five own Reaction common-name slots are absent; a verified native frame fallback is distinct from an invented biochemical label.

## Distinctness with precise search limits

All 267 copied YAML records were byte-rebound to actual landed commit `63ebb3b3e29ca1ed6472597104347d9fbc98f4a5`, tree `5448122efcfbd8ae2ac90ad42e70557b03d9b78e`. Pending acetate SHA `47d1c71951ce5806e5c9570ee00b2ab9f8634158251ee06821a0f77017b0eca3` was checked separately. A hidden/ignored-inclusive physical traversal of the owned worktree's `data/pathways` found precisely those 268 YAML/YML files. Parsed roots, taxa, participants and reactions independently reproduce all corrected author rows; references are kept separate. There is no exact candidate root or label among these 268 records.

The corrected result properly limits native Ack/Pta overlap to pending acetate. Three aromatic records cite ACETALD-DEHYDROG-RXN as a reference rather than declaring that native ID. Their Rhea reaction chemistry is independently recognized through the retained complete quartet table: PWY-5415, PWY-5420 and PWY0-1277 share the 23288 family. Thermotoga PWY0-1312 contains the Pta/Ack module, families 19521 and 11352. The yeast GO-CAM ethanol-degradation record represents ethanol oxidation and acetate activation. None supplies the complete ethanolamine cleavage and branched boundary. Prior261/262 EutE dispositions were read at their exact component/heterologous/genetic scope; they are not prior full-route curation.

I repeated eight candidate-specific ordinary-text searches in both trees with `rg --no-ignore --hidden`, excluding `.git` and `.venv`: 37 matched owned-worktree files and 29 original-checkout files. Those are file matches, not distinct pathways. Source backlinks, generated record views, cross-Mech priority entries, old EutE decisions, the ignored SEED selector and historical iModulon context are retained leads, not duplicate route definitions. Wider author numeric/reaction searches remain available with their explicit substring caveat.

I independently decoded and hash-checked exactly the author's 116 selected gzip payloads, reproducing every pattern/count: 3,991,511 compressed bytes, 24,849,128 decoded bytes, 17 matched payloads. The 17,025-container / 1,794,475,047-byte denominator is the author's historical physical inventory, not a fresh current inventory and not an interior search. Other and nested archive interiors remain unsearched. There is no global historical absence, synonym exhaustion, or source exhaustion claim. QuickGO:0046336 is broad catabolic grounding, and the returned KEGG M00092/M00093 biosynthetic modules are not exact route aliases.

**Actual next271 merged-baseline rebind is still required before maintained curation or adapter work.** This review uses the landed270 plus separately pending271 chronology and does not silently upgrade pending work to merged status.

## Primary evidence and limitations

Every supplied abstract in the retained 11-record Europe PMC core response was read; two records have no abstract, and PMID23920494 is a review. Acquisition hashes were independently checked. The retained 2005 and 2006 PMC bodies have the correct article titles/DOIs and real main text; the 2013 and 2004 HTML bodies are CAPTCHA documents despite HTTP200. Their XML requests returned HTTP500. They are not credited as full texts.

The independent targeted 2005 reading covers abstract, LT2 derivative culture conditions, the mutant/complementation and shell-bypass results, relevant figure captions and discussion. It supports conditional growth with altered expression, oxygen conditions and glutathione supplementation, not shell irrelevance or universal enzyme sufficiency. The methods and captions specify oxidized GSSG supplementation; the article's discussion uses GSH terminology. Future construct/chemical claims must retain that distinction. Microtiter conditions include a small glycerol supplement. EutE genetic rescue is not a purified EutE assay, and proposed toxicity/free-CoA explanations remain proposals.

The targeted 2006 reading covers abstract, LT2 strain scope and medium/release methods, standard versus pH/gas-exchange-dependent results, selected captions and discussion. The low-pH/acetal compartment mechanism is proposed, not measured universal localization. EutG alternatives remain hypotheses. The explicitly conflicting EutD phenotype is attributed tentatively to genetic background; this cannot be resolved by choosing the easier claim. The authors' inability to demonstrate anaerobic fermentation without an external acceptor is not a universal impossibility claim. The speculative alternative EutBC-bypass route is not an additional issued member.

The 2013 abstract explicitly marks external EutBC as a model prediction and describes private NAD/CoA recycling under stringent genetic tests. This conflicts with blanket all-lumen language in the native source and the earlier model; it must stay qualified until the relevant main/assay evidence is assessed. The 2004 EutD abstract identifies acetyl-CoA as assay product and acetate-growth complementation; it does not directly establish the opposite physiological flux. EutT adenosylation and EutA protection are distinct in PMID15516577. The older operon and induction abstracts retain their preparation, inference and strain limits.

No figure pixels, complete tables, supplements or inaccessible mains were reviewed. Text extraction is not full semantic reading. The targeted excerpts and exact reading boundaries are retained separately. Subsequent source preparation should pursue the consequential missing evidence within a bounded scope, then preserve any remaining access gaps. Unavailable historical full texts do not invalidate faithfully identified authoritative structured-source assertions; they prevent unsupported stronger primary, construct or localization claims.

## Required next-stage dispositions

1. Complete and independently review the 71 activity leads and selected enzyme/complex/component, cofactor, regulator, location and organism originals. Preserve both native branches and the full microcompartment context; do not reduce the route to acetyl-CoA formation.
2. Resolve each primary claim at its actual preparation, strain, expression and assay conditions. Retain model/negative/conditional statements as such. A lack of purified evidence must not become a positive purified-catalysis edge.
3. Verify all selected chemical, reaction, protein, activity and taxon identities from their issuers; retain source EC, direction, class, charge/stereo and localization conflicts. No Rhea/KEGG/MetaNetX or EcoCyc exact mapping is accepted from backlinks alone.
4. Rebind to the actual landed271 baseline and revisit exact aliases as the identifier set expands before curation/adapter work. No new schema work or graph simplification is justified merely by this preflight.
5. Sulfate remains OPEN issue410 with its donor-resolved DsrC evidence prerequisite. Its newly acquired native objects do not close that issue. Nitrogen fixation and ammonia oxidation remain unassessed here; none is counted as exhausted.

The reproducible structural/integrity replay passed 593 checks. All owned commands are terminal. No maintained file, Git/GitHub state, runtime or source owner was changed. There are no issue-ready defects at this stage; the qualifications above are acceptance boundaries and next-stage requirements, not newly invented source failures.
