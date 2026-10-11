# Complete ADP-L-glycero-beta-D-manno-heptose biosynthesis

The new record represents all five reactions of **MetaCyc:PWY0-1241**, from sedoheptulose 7-phosphate to ADP-L-glycero-beta-D-manno-heptose. It is not the shorter four-step boundary defined by GO:0097171, which begins with heptose 7-phosphate. The five biochemical reactions in the PathBank:SMP0002107/PW002095 lead correspond to this route, but that map contains identifier defects and is not accepted as a clean crosswalk. Upstream pentose-phosphate and downstream LPS subpathway connectors are explicitly outside the chosen complete native boundary.

The [record](../../../data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml) is accompanied by [native facts and dispositions](adhp-native-projection.json), [chemical projection](adhp-chemistry-projection.json), [protein projection](adhp-protein-projection.json), [source manifest](adhp-source-manifest.json), [identifier ledger](adhp-identifiers.json), [duplicate search](adhp-dedup.json), and [author replay](adhp-replay.py). The validation receipt is `adhp-validation.json`. Raw responses remain external under `/private/tmp/pathwaymech-nicotine-next-evidence/adhp`.

## Identity and novelty

Hidden and ignored files were included in the exact ID, reaction, assembly, protein, pathway-label, PMID and DOI searches across the accessible current worktree. Existing archive screenings and the prior `thiamine-scout-handoff.md` are research leads, not an existing maintained route. No equivalent maintained pathway was found. This is a repository-scoped finding, not a claim about inaccessible original Documents paths or all databases. The search receipts retain actual outputs and exit codes. Current source release pins are retained; old authority terms are the integration owner's responsibility.

All five native MetaCyc reaction members and all four predecessor links are preserved:

| Native reaction | Current selected Rhea | Function |
| --- | --- | --- |
| RXN0-4301 | RHEA:27490 | GmhA isomerization |
| RXN0-4341 | RHEA:27474 | HldE kinase |
| RXN0-4361 | RHEA:28519 | GmhB C7 phosphatase |
| RXN0-4342 | RHEA:27466 | HldE adenylyltransferase |
| 5.1.3.20-RXN | RHEA:17578 | HldD C6 epimerase |

Each native reaction directly cross-references the selected directional Rhea ID. The independent Rhea 142 RDF and directions table confirm all five are left-to-right variants. Nineteen reaction-side occurrences are retained, including water, proton, ATP, ADP, phosphate and diphosphate. All five elemental and formal-charge balances pass using exact charged species, not neutral display labels.

## Native defects and source-specific chemistry

The PathBank GmhA complex contains UniProt Q643R3, a human LPCAT4 acyltransferase, and its first reaction has the corresponding wrong EC 2.3.1.23. Neither is copied. Independent MetaCyc G6106-MONOMER explicitly unifies with the reviewed K-12 GmhA P63224; its native complex CPLX0-7660 contains four copies. The other native bridges are G7590-MONOMER/P76658 to HldE dimer CPLX0-3661, EG11736-MONOMER/P63228 to monomeric GmhB, and EG10838-MONOMER/P67910 to HldD pentamer CPLX0-3681.

The PathBank diphosphate object carries PubChem 3315 and an organic-dye formula. Its identifier mapping is rejected. CHEBI:33019 is selected independently from current Rhea. Several native display objects do not fully specify anomer or charge; current Rhea/ChEBI chemistry is used without asserting exact identity to those underspecified source objects.

Current Rhea represents GmhA as **two sedoheptulose 7-phosphate molecules → one alpha plus one beta heptose 7-phosphate**. All three occurrences and the coefficient two are retained. The alpha product is a declared terminal coproduct within this graph; only beta proceeds to HldE. This formal database equation does not establish an experimentally fixed 1:1 product ratio or flux. The native source groups both anomers in one chemical class. The record does not add an alpha-GDP branch or silently turn the equation into beta-only conversion.

HldE adenylylation transfers AMP from ATP with diphosphate release. Its current UniProt FUNCTION prose says ADP transfer, but its CATALYTIC ACTIVITY and the primary chemistry are correct. The misleading FUNCTION wording is not propagated.

## Experimental support and limitations

**PMID:11751812, DOI:10.1128/JB.184.2.363-369.2002**, full PMC139585 HTML, establishes the intervening HldE/GmhB chemistry with purified K-12 gene products. Constructs derive from MG1655; expression used BL21-SI and deletion/complementation experiments used W3110. The upstream GmhA reagent was from *Aneurinibacillus thermoaerophilus*, so this paper is not attached as a direct purified E. coli GmhA assay. HPAEC comparisons distinguish beta HldE phosphorylation and ATP/beta-specific adenylylation. The reaction buffer contains 10 mM MgCl2; that alone is not a separate HldE metal-binding measurement. The gmhB deletion caused a partial LPS-core defect, not a universally complete heptoseless or lethal phenotype. An unidentified compensating phosphatase is discussed but is not invented as a catalyst here.

**PMID:18056714, DOI:10.1074/jbc.M706163200**, inspected primary abstract and current reviewed GmhA annotation, supports E. coli GmhA structure/function with mutant biochemistry. The abstract spans both E. coli and Pseudomonas; no result is indiscriminately transferred between species. Tetramer stoichiometry is from the explicit native complex and experimentally coded UniProt SUBUNIT annotation; the inspected abstract itself does not specify four subunits. UniProt's one-Zn-per-subunit statement is **ECO:0000250**, so its inference by similarity remains explicit.

**PMID:16030223, DOI:10.1128/JB.187.15.5292-5300.2005**, inspected abstract, reports functional complementation, dominant-negative and copurification evidence for the HldE functional dimer. Its gel-filtration result is specifically the isolated HldE1 kinase domain. The literal phrase “the HldE functional unit is a dimer” is retained as a bounded seven-word primary excerpt. Full HldE activity is not claimed to have an independently repeated SEC measurement from this abstract.

**PMID:20050615, DOI:10.1021/bi902018y**, full PMC2844805 HTML, establishes K-12 GmhB C7-selective hydrolysis, approximately 100-fold beta preference and no further hydrolysis of the monophosphate product. It does not show absolute inactivity toward alpha bisphosphate. **PMID:20050614, DOI:10.1021/bi902019q**, full PMC2844806 BioC, independently supports solution monomer, catalytic Mg coordination and the separate Zn-binding loop. The Zn ion does not contact substrate or directly participate in catalysis; mutation effects do not resolve the loop motif's physiological function. This primary source prints P63288 in Materials; that accession typo is rejected in favor of independent P63228 authorities. Zn-site statements are cited to offsets 20251, 21102 and 23631; Mg statements to offsets 15508–17361. Manganese/cobalt activity alternatives are kept as the explicit **ECO:0000269** UniProt annotation citing PMID:16990279; the original full paper was unavailable, so no uninspected metal-assay details are added. Alternative catalytic metals do not mean simultaneous occupancy, and Zn is not mislabeled as an interchangeable catalytic metal.

**PMID:31449400, DOI:10.1021/acs.biochem.9b00548**, full PMC6859792 BioC, was checked because it appears in current GmhB annotation. It experimentally uses cloned K-12 P63228 as a preparative substitute in a C. jejuni **alpha-GDP** route; its beta kinetic values reproduce earlier work. It does not establish the complete K-12 route anew. **PMC3976583** was inspected for its abstract and introductory route account only; it is additional chemical-synthesis context, not a source for an uninspected experiment in the record.

**PMID:7929099**, inspected primary abstract, establishes purified K-12 HldD epimerization but historically identified NAD. **PMID:10896473, DOI:10.1016/S0969-2126(00)00128-3**, inspected abstract, establishes the pentameric structure with two pentamers per crystallographic asymmetric unit. The literal excerpt “AGME is a homopentameric enzyme” is five words; it does not justify a physiological decamer. Earlier apparent native mass does not independently resolve pentamer stoichiometry. **PMID:11313358, DOI:10.1074/jbc.M102258200**, inspected abstract, refines the physiological cofactor to NADP through reconstitution and extract analysis; NAD supports lower activity, whereas FAD does not restore activity. **PMID:17316025, DOI:10.1021/bi602641m**, inspected abstract, supports bound-NADP oxidation/reduction during epimerization. Cofactor recycling adds no net NAD(P) consumption to Rhea:17578. The 1983 genetic abstract and 2010 phosphoaspartate abstract were considered supporting historical context; no extra reaction is added from them.

No cellular-compartment node is required to convey the five-step chemistry. GmhA's cytoplasmic annotation and GmhB's similarity-based cytoplasmic annotation were considered in the protein projection; unsupported compartment claims are not assigned to all enzymes. The taxon list scopes curated K-12 proteins; it is not an invented taxon-to-flux edge or proof that every K-12 derivative has identical measured flux.

## Source access, reproducibility and context

Full primary bodies were available for PMC139585, PMC2844805 and PMC2844806 BioC and were read for the assertions used. PMC6859792 BioC and PMC3976583 were inspected for the bounded purposes above. Other named studies were available as indexed primary abstracts. HTTP 200 reCAPTCHA pages, publisher redirect shells, a BioC HTML error, and an empty PDF response are explicitly marked unusable. No signed redirect URLs, cookie/session/authorization fields or transient keys are included in maintained receipts. Hash scopes distinguish compressed RDF, plain TSV, full native XML, complete UniProt JSON, indexed abstract responses and uncompressed SemanticSQL bytes.

The integration owner's [iModulon context](imodulondb-context.json) and [parser replay](imodulondb-parser-replay.json) preserve fresh computational queries. E. coli gene hits provide expression-context lookup only. Zero module-name hits do not prove absent module membership, absence of pathway biology, or catalytic activity. These responses contribute no mechanistic edge.

The author replay checks exact native membership and precursor links, all four protein bridges, three assembly stoichiometries, current UniProt catalytic families, every Rhea side and coefficient, five balances, declared chemical identities, 43 local edges, source response hashes and bounded literal excerpts. The strict validator is run on this one record. Shared authority resolution, generated pages, full tests and scientific review belong to root's integration gates; author checks do not substitute for those gates.
