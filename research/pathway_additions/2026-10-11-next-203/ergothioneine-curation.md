# Ergothioneine biosynthesis I: complete bacterial route

Target: `MetaCyc:PWY-7255`, `data/pathways/ergothioneine-biosynthesis-i.yaml`.
This author assessment covers the complete seven-member native pathway, with current
mc(2)155 gene-product annotations and explicitly distinguished experimental preparations.
The adjacent generic GO process includes fungal routes and is not substituted for the
exact bacterial definition. Ignored and hidden files were included in both repository
searches; prior next201 references were discovery leads, not existing records.

## Native boundary and chemical projection

| Native member | Selected reaction | Disposition |
|---|---|---|
| GLUTCYSLIG-RXN | RHEA:13286 | Full glutamate/cysteine/ATP ligation with ADP, phosphate and proton products; EgtA's exact protein annotation is inferred by similarity. |
| RXN-14431 | RHEA:38472 | Full three-SAM histidine methylation, three SAH and three protons; no single-methyl truncation. |
| RXN-14430 | RHEA:42673 | Oxygen-consuming hercynine/gamma-glutamylcysteine coupling, including water product. |
| RXN-14429 | RHEA:42685 | Hydrolysis with water and released glutamate retained. |
| RXN-18088 | RHEA:52781 | PLP-enzyme cleavage including water, sulfenic acid, pyruvate and ammonium. |
| RXN-18089 | MetaCyc:RXN-18089 | Native spontaneous, generic AH2-driven reduction to neutral ergothioneine; no invented reductase or physiological thiol. |
| RXN-15804 | MetaCyc:RXN-15804 | Native spontaneous reversible thiol/thione equilibration, traversed toward thione in the native layout. |

All seven source members are retained. Both precursor branches converge at EgtB.
The full route begins with cysteine, glutamate, ATP, histidine and SAM, rather than
recursively incorporating amino-acid or SAM biosynthesis. Oxygen is a consumed
substrate; iron(II) is an enzyme cofactor, not a stoichiometric reaction substrate.
The combined EgtE/reduction equation RHEA:42689 is explicitly excluded to avoid
counting the same conversion twice.

The current Rhea reduction (52785) includes H+ and ergothioneine(1+) CHEBI:134344.
The older native reduction instead gives neutral CHEBI:4828 with no H+ term.
Both are charge-balanced conventions, but they are not the same explicit equation.
The latter joins the independently defined neutral tautomerization without inventing
an extra acid-base reaction. The graph therefore uses the native terminal reaction
identities and states, not a false current-Rhea crosswalk.

The native Acceptor frame links broad role CHEBI:15339. Its comment explicitly limits
this usage to an unknown partner transferring two electrons and two protons.
The independently inspected current Rhea reduction supplies formula-bearing
CHEBI:13193 (A) paired with CHEBI:17499 (AH2); the record names this formula-bearing
pair without asserting that the native broad-role cross-reference is an exact chemical
identity. Symbolic A is conserved in the atom balance. Neither this nor DTT turnover
establishes a particular physiological donor.

The thiol (4828) and thione (82707) have equal standard InChIs, reflecting tautomer
normalization. They remain distinct authoritative states: native CML gives C-S versus
C=S, and ChEBI SMILES, definitions and exact names distinguish them. A standard-InChI
match alone was not used to merge them. The obsolete native CPD-15276 cross-reference
returned 404 and is not used as an active identity bridge.

Current sulfoxide ChEBI classes 82703 and 82706 do not specify sulfur configuration.
Vit 2015's bound substrate has S sulfur configuration, but that substrate was made
with M. thermoresistibile EgtB and bound to the C2A M. smegmatis EgtC variant. The
record does not turn this into an absolute-stereochemistry measurement of the
DSM43465 or mc(2)155 EgtB reaction, nor claim acceptance of every stereoisomer.

## Original primary evidence and strain limits

The 2010 original ACS supplement, especially S2-S10, was read in full for cloning,
protein production, product identification, metal and substrate tests. The main paper
was accessible as its original primary abstract, not claimed as inspected full text.
Cloning explicitly names DSM43465. The current DSMZ issuing catalogue identifies
that strain as ATCC607; it is not mc(2)155/ATCC700084. Current UniProt mc(2)155 entries
cite those experiments, but that database curation does not change the original
preparation's strain. The record preserves the database activity tiers and separately
reports the experimental scope.

EgtA (A0R5N1, MSMEG_6250) activity has ECO:0000250 support from M. tuberculosis
P9WPK7. Harth 2005's inspected abstract concerns M. tuberculosis proteins expressed
in M. smegmatis; it is not a direct assay of the selected smegmatis EgtA. Native
MONOMER-17988's broad attribution is not promoted as direct exact-protein evidence.
The 2010 purified preparations comprise EgtB/C/D, with supplied gamma-glutamylcysteine.
The EgtA reaction is retained at its actual annotation tier, rather than omitted from
the full route or falsely upgraded.

EgtB (A0R5N0) is supported by current catalytic annotation and the DSM43465 2010
reconstitution. Supplement Figure S6, S7, distinguishes FeSO4 rescue of metal-depleted
enzyme from tested zinc, copper, manganese and EDTA conditions. The current monomer
annotation cites a 2015 M. thermoresistibile structural study. That citation is not
proof of the mc(2)155 solution assembly. Functional `enables` is used; Fe(II) is retained
with the original assay scope. The native monomer prose has egtD/fungal-fusion naming
typographical errors; the current gene and protein identities are used instead.

EgtC (A0R5M9) has direct mc(2)155/ATCC700084 cloning in the original 2015 accepted
manuscript (Experimental Section, pp5-6). The complete nine-page manuscript was
retrieved from the institutional repository content API after two landing-page
responses were rejected as PDFs. Results/Overall structure (p2) supports a tetramer
with crystal contacts, PISA and analytical size exclusion. The substrate-binding pocket
uses two chains; the depicted dimer is not substituted for the supported tetramer.
The source reports initial construct mutations, a regenerated construct, and the C2A
substrate-trapping variant. These are not silently treated as identical wild-type assays.
No verified whole-tetramer CURIE was established in the inspected native objects;
functional `enables` preserves this assembly context without a fabricated complex.

EgtD (A0R5M8) performs all three methyl transfers. The 2014 full article's Methods
sec2.1 also names DSM43465/ATCC607 and supports a solution monomer, distinct from
crystal asymmetric-unit multiplicity. The 2013 mc(2)155 deletion/complementation
study (PMC3697313, Methods sec5, Results sec12 and Table3) directly supports the
pathway-level EgtD role. The 2018 original supplementary Figure S2, p3, supports
in vitro TMH/hercynine product inhibition in the earlier engineered preparation.
Its p11 protein-production section refers back to Vit 2014, whose complete printed
construct begins MALSLANY, while current A0R5M8 begins MTLSLANY (residue 2 A/T).
This is not an exact mc(2)155 inhibition assay. The result is retained as explicit
preparation context in the record description and reference; no exact-protein inhibitory edge or
physiological feedback-strength claim is made. MnII in the coupled assay is not evidence
for an obligatory EgtD metal cofactor. M. tuberculosis PknD regulation is not transferred.

EgtE (A0R5M7) is directly cloned from mc(2)155 in the 2023 article (2024 collection),
PMC10805701 sec3.2 p1. Results sec1.1 p2 and sec1.2 p1 support a solution homodimer
and a pocket involving the neighboring chain. A pyruvate-bound crystal tetramer is
not promoted as its solution assembly; mutant-trapped intermediates are not proof
of all wild-type elementary steps. No exact native whole-dimer identifier was found
in the inspected MONOMER-17987/gene objects, so `enables` is qualified accordingly.
PLP is supported independently in current UniProt and the original 2015 measurements.

The entire 2015 JATS body was inspected, including Results p3-p9 and Figures4-6.
Trapping, NMR/MS, reductant-dependent products and pyruvate/ammonia measurements
support separate cleavage and reduction. Potential physiological cysteine, glutathione
or mycothiol donors are suggestions, not demonstrated partners. The Methods heading
for the purported absence-of-reductant experiment conflicts with its listed DTT;
that paragraph is not used as absence-condition evidence. Results and figure-defined
conditions support the bounded assertion. Its supplement does not independently
supply the exact cloning/strain bridge; the later primary supplies that bridge.

## Scope, exclusions and source coverage

All five Egt functional roles, both nonenzymatic terminal events, full chemical sides,
Fe(II), PLP, contextual product-inhibition evidence and mc(2)155 EgtD physiology
are represented. The native pathway's five-gene narrative and seven-reaction list
are reconciled explicitly. No automatic physical-complex ID, subunit stoichiometry
edge, specific reductant, cellular compartment, transport mechanism, antioxidant
phenotype or universal species distribution is invented. Fungal Egt1/Egt2 bypasses,
Erwinia substitute lyase used in the early coupled assay, sulfinic-acid side products,
assay reductants and LDH/NADH reporter chemistry are not pathway members.

The current iModulonDB inventory was independently acquired by root. No dataset for
this smegmatis strain/species was returned; the available M. tuberculosis dataset is
not substituted. This is an applicability limitation, not evidence that expression
modules or the biological pathway are absent.

The source manifest records 54 successful original bodies and rejected/failed attempts
without retained authentication headers. Individual UniProt references use their
entry versions and annotation dates because release response headers were not
retained. All named identifiers and original-body authority proposals are listed in
`ergothioneine-identifiers.json` and `ergothioneine-authority-delta.json`.
The replay re-extracts current Rhea from original RDF, verifies every chemical side
and seven balances, checks native membership and relevant source pointers, rehashes
original bodies and authority inputs, and compares actual KGX evidence and categories.
It is author verification, not an independent scientific review or a claim that the
entire shared corpus has been validated.

## Execution history

The first original-source replay reached the KGX comparison but failed because the
author helper incorrectly expected duplicate, unsorted reference metadata. KGX
correctly deduplicates and sorts references. The helper was corrected; the second
actual replay exited zero, including all seven balances and original source hashes.
A final lint-only string wrap prompted the final recorded replay. Initial and final
logs remain external; this is a method correction, not a record defect.

## Independent review correction #371

The initial target `a0a26b897757e072ec5640805db8ab9ed0961b6499e1c576d0751996a0f97b37` assigned product inhibition to the exact current
mc(2)155 protein despite a different earlier engineered preparation. Independent
review identified this bounded scope defect. After immutable initial review and
root archival, only inhibitory edge048 was removed. The experimental observation
was retained explicitly as non-transferred record description/reference context;
EgtD edge042 retains exact construct scope with original
references and exact construct evidence. The seven-member biological route, all
chemical sides and all other mechanistic relations remain unchanged. Corrected
target: `238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527`. The original-source regression and actual export were rerun;
execution and source hashes are preserved in the validation and provenance-fix receipts.
