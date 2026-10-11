# Methylthiopropanoate degradation I: author curation

The new record represents the complete three-member MetaCyc PWY-6048 route in
Ruegeria pomeroyi DSS-3 (NCBITaxon:246200), not the larger DMSP demethylation
pathway. It begins with free MMPA and ends with methanethiol, acetaldehyde,
carbon dioxide and regenerated CoA. The native pathway, all three reaction
objects, their enzymatic-reaction and protein frames, and the four constituent
objects of the terminal composite were inspected from original MetaCyc 22.5
XML. Independent native HTML establishes the exact pathway identity and title.
No exact GO process was identified in the bounded label search; adjacent
methionine-to-MMPA terms do not define this cleavage route.

The baseline contains 203 maintained records. Initial and expanded searches
used `rg -uu` in both the current worktree and the original Documents checkout,
including ignored and hidden research. The `.git` and `.venv` internals were
excluded; the expanded search also excluded this newly authored target and its
owned dossier. Prior scout and handoff mentions were read and are preserved.
They describe the same candidate as future work, not an existing record or a
resolved rejection. Additional numeric matches are digest fragments and a
wheel size, while new authority-inspection hits are identity facts. The
search receipt records commands, output hashes and scope; this is a bounded
corpus novelty assessment, not a claim of absence elsewhere.

## Complete native boundary and chemistry

| Native member | Current directed reaction | Disposition |
| --- | --- | --- |
| RXN-12571 | RHEA:43053 | DmdB2 MMPA activation with ATP and CoA; AMP and diphosphate products. |
| RXN-12572 | RHEA:52613 | DmdC1 oxidation to trans-MTA-CoA. Generic whole ETF redox states are retained as the database convention. |
| RXN-12573 | RHEA:45145 | Complete two-water net cleavage, including all four native component transformations, represented once. |

Native RXN-12571 and RXN-12573 directly cross-reference the selected directed
Rhea identifiers. RXN-12572 lacks a native Rhea cross-reference; its enzyme
frame resolves Q5LLW7, whose current reviewed catalytic annotation supplies
RHEA:52612. The original Rhea master explicitly supplies direction 52613.
This distinction is preserved in the membership evidence rather than
attributing a newer cross-reference to the older XML.

The three distinctive native compounds CPD-7672, CPD-13546 and CPD-13547 have
full InChIs exactly equal to ChEBI 49016, 82815 and 84994, respectively. The
MTA-CoA structure includes the same trans double-bond layer `/b8-5+` in both
sources; the 2013 primary also describes the trans substrate. Rhea 142 supplies
all 17 retained chemical-side assertions with explicit `containsN`
coefficients, including two waters in the terminal net. The replay sums atoms
and charges for all three graph equations and four component equations. Whole
ETF nodes remain generic polypeptide states: their declared FAD/FADH2 reactive
parts are used only for formal balance, with the unchanged protein scaffold
canceling. A free FAD molecule is not substituted for either carrier state.

RXN-16010, RXN-16011, RXN-16012 and RXN-16013 correspond to Rhea directions
45149, 45153, 45157 and 45161. Their sum equals the single terminal net exactly.
They are not added alongside it as another catalytic route. The primary DmdD
mechanism proposes enzymatic hydration and thioester hydrolysis, spontaneous
methanethiol release after hydration, and expected spontaneous decarboxylation
of malonate semialdehyde. It does not establish four independent enzyme
activities or measure every transient intermediate. The record preserves the
net observed transformation and these limitations.

The native summary calls the middle transformation a reduction. Native sides,
loss of two hydrogens and both early and later primary experiments show
oxidation of MMPA-CoA. The incorrect summary word is retained in the original
source projection and is not copied as a biological assertion.

## Primary evidence, exact proteins and evidence limits

The complete six-page original 2011 Nature paper (PMID:21562561,
DOI:10.1038/nature10078) was recovered from institutional hosting. Its first
four pages are the printed article and the remaining pages are online Methods.
The PDF was independently text-extracted with pypdfium2 and rendered; Figure 1
and the physiological results on printed p.209 were visually inspected. Native
purification, recombinant expression, product identification and DSS-3 mutants
support the route. E. coli is the expression host, not the curated pathway
organism. The original work inferred diphosphate and carbon-dioxide formation
rather than directly identifying every side product; those formal species are
also supported by the exact current reaction definitions.

The full 2014 primary (PMID:24443527; original PMC3957724 HTML) distinguishes
SPO2045/DmdB2 from SPO0677/DmdB1. DmdB2 was an active purified recombinant
homodimer, measured by gel filtration. It is inhibited by DMSP, and MMPA above
2 mM relieves that inhibition, with approximately 80% recovery at 8 mM. The
record’s `activates` edge is explicitly conditional relief, not unqualified
activation. ADP relief belongs to DmdB1 and is not transferred. The paper
explicitly says magnesium was required for activity; current UniProt's Mg
annotation remains marked ECO:0000250 by similarity. Neither source provides
a protein-bound Mg stoichiometry or resolves MgATP versus free-ion mechanisms.
High-concentration salt responses and proposed feedback models are retained
as context, not expanded into transcriptional regulation or universal flux.

The full later DmdC1 paper (PMID:34818101; original PMC8824276 HTML, published
online 2021 and in the February 2022 issue) directly studies cloned DSS-3
SPO3804. Its native apparent mass of 130.5 kDa is consistent with a homodimer.
Oxidation required artificial PMS plus DCPIP or INT. DCPIP, free FAD, FMN and
NADP+ alone did not support activity; the authors infer an uncharacterized
flavoprotein in vivo. This later evidence was searched and inspected before
curation. It does not identify a particular ETF gene or complex.

MetaCyc RXN-12572, reviewed UniProt Q5LLW7 and Rhea 52613 explicitly use the
generic ETF class. These database assertions support the two carrier edges;
PMID:21562561 is not cited on those edges as direct carrier-physiology proof.
The Q5LLW7-bound FAD annotation is separately retained at its actual
ECO:0000250 similarity tier. Twenty-percent stimulation by added FAD in the
later experiment is not recast as physiological regulation or measured
cofactor occupancy. The 2019 mechanistic paper (PMID:30677184; full
PMC6850173 XML) uses R. lacuscaerulensis ITI-1157 DmdB and R. nubinhibens ISM
DmdC, not DSS-3 enzymes. Its free-FAD activity, docking and detailed structural
mechanism are not transferred to the present strain. Independent scientific
review should specifically reassess the acceptability of the generic carrier
convention with these explicit limits.

The full 2013 DmdD primary (PMID:23704947; original PMC3660561 JATS) directly
studies DSS-3 SPO3805. Crystal and gel-filtration evidence support a homohexamer,
a dimer of trimers, with active sites at subunit interfaces. The retained
RCSB 4IZB entity response is supporting context; the primary supplies the
assembly claim. The three native MONOMER frames cross-reference the reviewed
proteins Q5LRT0, Q5LLW7 and Q5LLW6 and native taxon 246200. They do not supply
independent assembly identifiers. Qualified `enables` edges preserve the
functional gene-product roles and the known dimer/dimer/hexamer context;
none asserts active monomer sufficiency or invents a complex identifier.

DSS-3 has other experimentally functional DmdB and DmdC paralogs. This record
preserves the exact three native enzyme assignments, rather than claiming
that those paralogs do not exist. Their distinct regulatory and acceptor
properties are not merged into DmdB2 or DmdC1. The 2014 expression results
identify DmdB2 as the major form under the tested DMSP-related growth
conditions. Direct growth and biochemical support in DSS-3 does not establish
activity in all environmental settings or all species carrying homologs.

## Deliberate exclusions and access

DmdA-mediated DMSP demethylation, downstream acetaldehyde oxidation, methanethiol
assimilation and alternate nonorthologous AcuH routes fall outside this exact
native pathway. DMSP is present only as a measured DmdB2 inhibitor. No
compartment is inferred from soluble purification, no membrane transporter is
invented, and transcription changes are not turned into a regulator-binding
edge. The separately retrieved 2020 sulfur-assimilation paper is downstream
context, not evidence that extends the named boundary.

The 2011 supplementary endpoints failed, so no unavailable supplement is
quoted. Later full primary papers resolve key assembly, magnesium and
acceptor questions. Two Europe PMC full-text XML requests returned HTTP 500;
original PMC HTML acquisition succeeded instead. The manifest preserves
failed attempts and successful body hashes, with only a safe response-header
allowlist. Text extractions and renders are derivative artifacts, never
substitutes for the original body identity. The full ChEBI Semantic SQL
hash is explicitly for database bytes, not its upstream OWL URL body.

The root’s current iModulonDB applicability receipt inspected 20 organisms and
28 datasets and found no Ruegeria dataset. No unrelated strain was queried as
a surrogate. This is dataset applicability, not negative biological evidence.

The author replay checks original bodies, exact source chains, all seven
formula/charge balances, full native membership, composite-to-net equivalence,
primary locator guards, current issuing-authority labels, both schemas and
actual target KGX evidence/description preservation. It is not an independent
scientific review. Root runs the full corpus gates after the cohort freezes;
those results will be reported separately and are not pre-claimed here.
