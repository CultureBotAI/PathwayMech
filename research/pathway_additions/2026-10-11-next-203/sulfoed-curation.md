# Sulfoquinovose degradation II: SQ1 author dossier

The selected identity is **MetaCyc:PWY-7722**, the complete native five-transformation
sulfo-Entner–Doudoroff route in **Pseudomonas putida SQ1 (DSM 100120)**. The maintained
target is `data/pathways/sulfoquinovose-degradation-ii.yaml`, SHA256
`20a95c209243399b88a90fbecb0d8d310ebfb3094fc6ee4487352fdc2185c596`.
It has 20 participants, six reaction activities, 48 edges, 86 evidence blocks and
22 references. The six activities cover five native transformations because the
last native NAD(P)-dependent oxidation has two experimentally supported cofactor
alternatives. They are alternatives, not consecutive oxidations.

## Exact boundary and novelty

The native pathway has exactly RXN-17096, RXN-17095, RXN-17097, RXN-17098 and
RXN-17101. All five are represented, in their native physiological order:
free SQ → sulfo-glucono-1,5-lactone → sulfogluconate → KDSG → pyruvate + SLA;
SLA → sulfolactate. Rhea142 resolves these as 47897, 47909, 47913, 47925 and
alternative 47929/47933. Every chemical side and coefficient is retained.

The existing PWY-7446 record is the distinct sulfo-EMP pathway. It uses an
isomerase/kinase route and yields DHAP/DHPS. Sharing SQ and SLA does not make
these pathways duplicates. Prior next201 discovery was a research handoff with
an unresolved access/identity gap, not a scientific rejection. The complete 2015
PMC HTML is now available, even though its EuropePMC full-XML endpoint still
returns 500. The original pathway XML hash equals the earlier scout's hash.

The retained `sulfoed-dedup.json` records searches of the new worktree and original
Documents checkout using `rg -uu`, including ignored and hidden files, for native
identities, labels, reaction/protein IDs and primary paper identifiers. Git metadata,
the task virtualenv and the prior dedup output itself are the only exclusions.
GO:1902777 is broader than the exact oxidative implementation and its native xref
points to PWY-7446. Its full original GO rows are retained in the identity ledger;
it is not claimed equivalent to this five-step route. No source-exhaustion claim
is made.

## Primary support, exact proteins and strain

Felux et al. 2015, PMID26195800, DOI10.1073/pnas.1507049112, is the central primary
source. Complete Results, Discussion, SI methods/tables and figure legends were
read. Figure1 was also visually inspected from the original deposited figure.
The work combines SQ-grown-cell proteomics/transcription, an SQDH insertion
mutant, and sequential reconstitution of all five recombinant SQ1 enzymes.
Figure4 follows each metabolite; pyruvate was independently checked using a
lactate-dehydrogenase reaction and cochromatography. The culture conditions were
mineral medium, SQ as sole carbon/energy source, shaking/rolling at 30°C. This
supports the selected SQ1 pathway, not every strain assigned to taxon303.

Reviewed original UniProt entries P0DOV5–P0DOV9 explicitly cite the genome and
experimental papers with `STRAIN=SQ1`. The corresponding original GenBank protein
records independently confirm strain, source taxon303, sequences and current
locus tags. Their old automated functional labels are not substituted for current
experimentally supported names.

| Activity | 2015 IMG locus | Current GenBank locus | Reviewed protein |
|---|---|---|---|
| SQ dehydrogenase | PpSQ1_00090 | PpSQ1_00405 | P0DOV5 |
| SGL lactonase | PpSQ1_00091 | PpSQ1_00410 | P0DOV6 |
| SG dehydratase | PpSQ1_00089 | PpSQ1_00400 | P0DOV7 |
| KDSG aldolase | PpSQ1_00100 | PpSQ1_00455 | P0DOV8 |
| SLA dehydrogenase | PpSQ1_00088 | PpSQ1_00395 | P0DOV9 |

The aldolase required an additional sequence check. Its2015 forward primer maps
exactly 36nt upstream of the current GenBank start on JTCJ01000004.1; the reverse
primer maps the same endpoint. The experimentally cloned interval is
complement(18793..19596), while KHL76360.1 is complement(18793..19560). The longer
construct adds `MSTAVTPPTFTP`; the current start is CTG, translated as initiator
Met in its annotation but internal Leu in the longer construct. The remaining
sequence matches exactly. This establishes the same genomic locus while retaining
the construct/start-call difference. There is no whole-sequence `sameAs` assertion.
The exact bases, coordinate checks and translation are independently replayable.

## Assemblies, cofactors and later evidence

Burchill et al.2025, PMID39840830, DOI10.1042/BCJ20240605, was inspected in full.
Its published SQDH sequence matches P0DOV5 after removal of the N-terminal tag.
SEC-MALLS gives a dominant approximately 119kDa species versus approximately 28kDa
monomer, consistent with the tetramer seen in crystals. This physical state is
preserved in the functional edge; a monomer is not declared sufficient and an
unissued complex identifier is not invented. Native `MONOMER-*` frame names
denote protein objects and do not establish biological monomers.

The 2025 SQDH experiments show an approximately 10^6 catalytic-efficiency preference
for NAD over NADP under their conditions, unlike the smaller preference measured
in 2015. Trace G6P turnover was detected at high enzyme concentration, superseding
any unqualified reading of the earlier negative test. Product inhibition by NADH
is retained as conditional recombinant-enzyme evidence, not cellular regulation.
The productive ternary complex was not directly trapped; its geometry was modeled
from binary structures, and no separate ternary-complex claim is added.

Current P0DOV6 and P0DOV8 divalent-metal annotations are ECO:0000250 inferences
from Q15493 and Q47098. P0DOV7's homodimer and [4Fe-4S] annotation are similarly
inferred from Q1JUQ1. These are not SQ1 metal-occupancy or assembly measurements.
Functional `enables` edges retain the correct evidence level. The other four
protein activities are not converted to invented physical-complex nodes.

A fresh current-literature search identified Kaur et al.2026, PMID41830472,
DOI10.1002/chem.70857. Its primary abstract reports a P.putida homohexameric KDSG
aldolase, optimal Co/Mn activity and modest KDPG cross-reactivity. The publisher's
article and supplement requests returned 403, while announced PDB9TDO APIs
returned 404. Root independently tested the actual downloadSupplement URL with
the same 403 result; the York institutional record links only the DOI. Therefore,
this is explicitly abstract-only contextual evidence. The inspected source does
not expose the strain or construct sequence. Its assembly and exact metal
preferences are not transferred to SQ1, and the older negative KDPG assay is
not presented as absolute specificity. These access results are not a claim that
the article or structural data do not exist.

Li et al.2023, PMID37886098, was inspected in full. Its SLA dehydrogenase
tetramer, racemic-substrate consumption and stereoselectivity concern
Rhizobium leguminosarum SRDI565. They are not experimental results for SQ1 P0DOV9.
The 2015 SQ1 kinetic table instead measured succinate semialdehyde as a surrogate;
no exact SLA Km is assigned. Both NAD and NADP support its observed SLA oxidation.

## Chemical identities and source disagreements

The six selected native organic compound InChIs exactly match current ChEBI255:
CPD-10247/77132, CPD-18481/88091, CPD-18482/88093, CPD-18483/88094,
CPD-18718/90109 and CPD-11799/61289. Formula, charge, exact reaction sides and
integer coefficients are replayed from the original full Rhea142 RDF, merging
all descriptions for each subject. All six equations balance atomically and
electrically. The two alternative complete-route net equations are checked
separately; both yield one pyruvate and one sulfolactate while consuming one SQ.

Old native protein prose links R-SLA (CPD-16503), but the actual native aldolase
and dehydrogenase reaction sides select S-SLA and S-SL. The current reviewed
UniProt/Rhea assignments and the selected exact native InChIs agree. Those stale
comment links are rejected explicitly. The 2015 HPLC-MS assay is not redescribed
as independent enantiomer-resolved characterization. Figure1's drawn structures
and current explicit structural identities are retained without assigning CIP
configuration from informal D/L naming alone.

Other source dispositions are explicit: the native SQDH comment's
“2-dehydrogenase” wording conflicts with its C1 reaction; the old aldolase
KDPG-family analogy conflicts with the primary's distinct COG3836 assignment;
and the broad CPD-367 pathway link does not replace the actual CPD-11799 endpoint.
Each native reaction is accounted for rather than dropping inconvenient objects.

## Exclusions and context

The exact native boundary starts at free SQ. Glycoside release, mutarotation,
predicted import/export proteins and the uncharacterized regulator are not added
as extra reactions or causal edges. SQ-dependent expression is not itself evidence
that SQ directly activates each enzyme. The soluble-fraction assays do not prove
exclusive cellular localization. Central pyruvate metabolism and separate-organism
desulfonation/mineralization are downstream of this complete native pathway.

Root's current canonical iModulon inventory and original precise321 metadata
identify KT2440, not SQ1. `imodulondb-applicability.json` preserves the exact source
scope and runner limitations. No SQ1 expression equivalence, module-membership
absence or biochemical conclusion is inferred from that dataset.

## Verification and provenance

`sulfoed-replay.py` is an author check, not an independent scientific review. Its
actual exit 0 execution is recorded in `sulfoed-validation.json` and external
`/private/tmp/pathwaymech-next-203-sulfoed-replay.log`. It verifies67 original
response bodies (including honestly retained unsuccessful attempts),22 reference
digests,27 chemical side occurrences, six balances, six exact native/current
structure bridges, five sequence/strain identities, native membership/directions,
primary locator assertions, and actual KGX export of 28 nodes/48 edges/86 evidence.
All reference text and descriptions survive export byte-for-byte. Full ChEBI255
and Rhea142 are streamed for hashing; the selected taxon label is queried and
the full 14GB taxon-cache hash is delegated to shared integration.

Raw originals are external; maintained files contain reproducible projections,
source/version/hash manifests, identity decisions and safe acquisition metadata.
No session, cookie or authorization headers are retained. Licensing remains
source-specific; user has deferred public-release licensing decisions, not provenance.
Root owns shared authorities, histories, rendered pages, full-corpus gates and
independent review. Their completion is not claimed by this author receipt.
