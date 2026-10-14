# Pathway mechanism research: catechol degradation to β-ketoadipate

## Pathway scope

`MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY` is the complete four-reaction
catechol-to-3-oxoadipate module in META PGDB 27.0. The record selects the
native *Pseudomonas putida* species annotation and its four native catalyst
frames. It does not assert that every strain has this pathway or that the
historical preparations have the sequences of a modern reference genome.

The neighboring `MetaCyc:PWY-2361` is a downstream pathway interface, not a
fifth core reaction. Its CoA transfer and thiolysis belong to a separate module.
`MetaCyc:PWY-5417` is the larger superpathway containing both modules. Frozen
`GO:0019615` has narrow-match links to both boundaries; its name alone does not
establish exact identity with this selected four-step module. The retained
DRAM M00568 rows are a discovery lead, not the record's authority.

The hidden- and ignored-inclusive duplicate audit inventories all 245 baseline
pathway YAML files and bridges their exact bytes from ca9a6940 to 22f4279d.
The existing aromatic meta-cleavage record `MetaCyc:PWY0-1277` has a different
boundary and chemistry. The whole-worktree searches found the candidate in
two retained DRAM source files. Compressed archive interiors were not decoded,
symlink directories were not followed, and external caches were not exhaustively
searched. These bounds are retained in the audit, not represented as global
source exhaustion.

## Mechanistic summary

Catechol 1,2-dioxygenase opens the ring to cis,cis-muconate. Muconate
cycloisomerase forms (S)-muconolactone; muconolactone isomerase moves the
double bond; enol-lactone hydrolase yields 3-oxoadipate. All formal reaction
sides, including oxygen, water and protons, are represented. Each consecutive
step shares the exact same charged, stereochemically specified intermediate.

The selected directional equations are `RHEA:23853`, `RHEA:30033`,
`RHEA:12349` and `RHEA:10185`. RHEA:30033 is the **right-to-left** member of
its Rhea family, even though its displayed directional equation lists the
consumed muconate first. Direction metadata follows the authority's family
orientation, and the consumed/produced graph endpoints follow its explicit
substrate/product assertions. All four equations balance atoms and charge.

Native complete InChIs, formal charges and formulas agree with ChEBI 255 for
all eight core chemicals. Two native SMILES fields are generic carboxylate
placeholders, and the pinned ChEBI:32379 SMILES omits cis/cis stereo markers.
The full native/pinned InChIs and current issuing ChEBI structures establish
the precise identities; the incomplete SMILES do not. Native R03959 is a
broader, neutral muconolactone cross-reference. KEGG R06989 retains the S
route but also uses neutral compounds. Neither is an exact charged-equation
substitute for the selected Rhea reaction.

## Catalyst identity and evidence boundaries

The native CatA dimer, CatB octamer, CatC decamer and historical hydrolase
assembly retain their native complex and component IDs. Their native activity
objects assign catalysis and retain their own experimental evidence codes.
Those database annotations are not described as personally reproduced assays.
The CatB manganese annotation belongs to the catalyst; manganese is not a
consumed core substrate.

CatA's native UniProt cross-reference Q9AEQ0 is deleted. The retained UniParc
sequence does not authorize selecting a replacement protein accession. CatB
P08310 and CatC P00948 provide useful independent annotation context, but the
graph consistently retains native components rather than silently converting
all assemblies to modern sequence identities.

The hydrolase native component combines an experimental 11-kDa annotation
with a 28.6-kDa sequence annotation and Q88N36 cross-reference. The 1980
paper's historical trimer inference is distinct from an assertion that three
modern 263-residue Q88N36 proteins form that preparation. Its source organism
was PRS2260, a derivative of PRS2178. The historical interpretation may be
represented with its measurement limits; the modern sequence/strain join is
not propagated. Neither a current mismatched GeneID nor a discontinued
KT2440 locus establishes the identity of that historical preparation.

## Evidence table

| Inspected source | Supported claim | Limit retained |
| --- | --- | --- |
| Complete native pathway and four reaction XML objects | Four-step boundary, full sides, order, species annotation and downstream interface | Cross-database chemistry checked independently |
| Rhea 142 complete original RDF and directional table | Exact sides, coefficients, directional member and ChEBI participants | Rhea 139 remains the pinned canonical-name authority |
| ChEBI 255 and current issuing structures; native compound originals | Exact charge and stereochemistry of eight core chemicals | Incomplete individual SMILES fields are not treated as exact structure evidence |
| Native complex, component and enzymatic-reaction objects | Source-scoped catalysis, assembly and manganese annotations | No automatic modern UniProt, strain or gene identity transfer |
| 1980 historical hydrolase primary text | PRS2260 preparation and inferred subunit organization | Original figure pixels unavailable; no modern sequence equivalence |
| 2010 A1501 primary PDF, figures and HPLC supplement | Separate organism's genetic, growth and expression experiments | Not evidence for the P. putida catalyst identities; conflicting peak labels preclude unqualified metabolite attribution |

## Gaps and deliberate exclusions

The 2010 *P. stutzeri* A1501 paper is assessed as an independent biological
context. Its predicted pathway figure does not purify or test each of the four
catalysts. Its Crc mechanism is proposed, and benzoate induction of catBC
survives benR disruption. Neither direct Crc repression nor BenR activation of
catBC is inferred. The HPLC Methods and figure/supplement assignments disagree
on the catechol and cis,cis-muconate retention peaks. Growth and transcript
observations do not resolve that chromatographic identity conflict.

No upstream benzoate conversion, transporter, downstream CoA reaction,
cross-species regulator, or universal cellular localization is added from a
neighboring map or a broad annotation. Source-reading and identity limitations
are retained in the accompanying projections and coverage ledgers. The exact
four-step biochemical boundary is not shortened to avoid an unresolved join.

## Candidate YAML

The maintained record is
`data/pathways/catechol-degradation-to-beta-ketoadipate.yaml`.
Its pages are generated from that file. Complete source bodies, paper figures,
HTTP responses and acquisition helpers remain outside the repository; this
dossier retains compact source projections, original-body hashes and review
receipts. Final validation and independent review results are recorded alongside
this dossier and in the immutable structured review bundle.
