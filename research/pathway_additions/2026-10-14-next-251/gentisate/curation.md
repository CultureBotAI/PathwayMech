# Pathway mechanism research: gentisate degradation I

## Pathway scope

MetaCyc:PWY-6223 defines the complete three-step isomerization route from
gentisate to fumarate and pyruvate. Gentisate ring cleavage produces cis
3-maleylpyruvate, its isomerase produces trans 3-fumarylpyruvate, and hydrolysis
releases the two terminal products. The direct maleylpyruvate-to-maleate route
PWY-7469 and upstream aromatic-substrate conversions are separate pathways.
No exact GO biological-process term was found in the pinned keyword/xref
search; the similarly named homogentisate route has a different substrate.

The preflight inventories all 248 baseline records and searches 151 exact
identifier/label/source patterns in both main and the worktree, including hidden
and ignored text files. Git metadata, virtual environments, binary archives,
compressed interiors and external/symlink trees are bounded exclusions. Prior
SEED selectors and the adjacent DRAM salicylate module are leads, not a duplicate
maintained pathway or a reason to claim source exhaustion.

## Mechanistic summary

The three selected left-to-right reactions are RHEA:18238, RHEA:17394 and
RHEA:26169. Complete native chemical sides, coefficients, formulas, formal
charges, full InChIs, CML connectivity and issuing ChEBI structures agree with
the Rhea mappings. Every equation balances atoms and charge. The first
intermediate is cis and the second is trans. The pinned maleylpyruvate SMILES
omits complete stereochemistry, but the full pinned InChI and current structure
agree; native pyruvate SMILES has a placeholder that the full CML/InChI resolves.
Canonical pinned labels are kept separate from newer reaction evidence.

Ralstonia sp. U2 NagI, NagL and NagK anchor the full route. Their complete
UniProt sequences match the deposited U2 coding sequences despite the broader
current UniProt taxon label. Recombinant assay constructs require their own
scope assessment; complete native-sequence identity does not by itself establish
the sequence of an expressed preparation. NagL uses glutathione. The NagK
magnesium/manganese annotations explicitly remain evidence by similarity.

Corynebacterium glutamicum and Paenibacillus sp. NyZ101 provide distinct
isomerase examples, not additional proof of a complete route in every listed
taxon. The C. glutamicum enzyme uses mycothiol. BagL accepts L-cysteine,
cysteinylglycine and glutathione in the assayed system; physiological cysteine
preference is an inference. Every tagged-protein assay edge qualifies the
protein endpoint. Reported metal activity effects retain concentrations and
preparation limits and are not represented as physiological metal requirements.

## Evidence table

| Source | Supported scope | Limit retained |
| --- | --- | --- |
| Complete MetaCyc 27.0 pathway, reactions and chemical objects | Three native members, order, chemical identity and native examples | Current BioCyc version is not asserted; account redirects are failed retrievals |
| Rhea RDF and ChEBI authority/issuing structures | Exact sides, charge, coefficient and stereochemical closure | A shorthand SMILES or source cross-reference alone is insufficient |
| UniProt, ENA/NCBI sequence records and native enzyme objects | U2, C. glutamicum and BagL base-protein identities | Native gene-name errors and unreviewed generic protein names are not propagated |
| PMID:11133965 | U2 recombinant and native-extract evidence for the complete route | Full-length native sequence and assay construct are separate identity questions |
| PMID:16481315 and PMID:22636771 | Mycothiol and alternative thiol activities, tagged preparations and in-vitro metal effects | Preparation, dose and assay conditions remain claim-local |
| PDB 2JL4, 2V6K and 2NSF plus sequence mapping | Deposited assembly/construct context | Structural deposits do not establish physiological metal requirements or other papers' tags |

## Gaps

Primary reading coverage distinguishes full publisher text, parsed author-copy
text, inspected original figures, abstracts and unavailable raw articles or
supplements. Full paper text and downloaded originals remain external. Hashes
of PubMed metadata do not stand in for a full article. The corrected metadata
projection uses each PubMed record's direct ArticleIdList, excluding cited-paper
identifiers; the correction is retained in the primary audit.

No direct regulator, transporter, generic compartment, physiological Ni cofactor,
or unqualified native BagL dimer is inferred. Exact tagged PDB sequences are
not borrowed for experiments in another publication. Chemical charge states
for assay thiols are an explicit curation normalization, not a measurement of
protonation in the paper. iModulonDB yielded no justified direct regulatory
edge; its C. glutamicum gene hit has an unresolved inactive-accession bridge.

Independent scientific review identified a NagI construct conflict, tracked in
issue #528. The reported forward primer maps 27 nucleotides downstream of the
deposited nagI start, at native Met10, while the paper describes a complete
reading frame. The affected catalytic edge now carries an experimental subject
qualifier. The actual expressed sequence remains unresolved; a proven nine-residue
deletion is not asserted. The initial review and its successor preserve the
finding and evidence-backed disposition separately.

The source inventory remains available for later licensing assessment as
requested. No raw source redistribution or public-release clearance is claimed.
Further pathway leads remain in preflight/CANDIDATES.md.

## Proposed record updates

Add one maintained gentisate record and its generated graph/evidence page.
Preserve all baseline records and authority objects, retain compact evidence
projections, run the required corpus gates, and save independent scientific and
integration reviews with explicit dispositions for any findings before merge.
