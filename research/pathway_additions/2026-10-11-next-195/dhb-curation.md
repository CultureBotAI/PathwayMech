# 2,3-Dihydroxybenzoate biosynthesis: complete PWY-5901

The maintained target is `data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml`,
**MetaCyc:PWY-5901**, a complete three-reaction conversion from chorismate to
2,3-dihydroxybenzoate (DHB). It follows EntC → EntB → EntA through isochorismate
and (2S,3S)-2,3-dihydroxy-2,3-dihydrobenzoate. This is an independently defined
pathway, not a truncated interpretation of the discovery map.

## Identity, novelty and full boundary

Fresh searches included ignored and hidden files in both the owned worktree and
the original Documents checkout. Git metadata and virtualenv runtime were the
only excluded directories. Exact pathway identifiers, labels, synonyms, protein
accessions, native and Rhea reaction identifiers, and primary PMID/DOI identifiers
were searched before authoring. The retained command/output ledger is
`dhb-dedup.json`. No equivalent maintained record was found. Prior PathBank
screenings and taxonomy assessments were read; they identify a mixed map needing
membership selection, with no prior scientific rejection or completed record.
The 2026-10-05 cross-Mech report proposes enterobactin as a future connection; it
is not a maintained DHB pathway. Discovery annotations and protein crosslinks do
not establish corpus coverage.

PW000751.owl / PathBank:SMP0000774 includes three relevant transformations,
a nested chorismate-biosynthesis pathway (SMP0000836), and a downstream
CueO-associated DHB oxidation (reaction 5866). The complete original BioPAX
object projection and exact archive/member hashes are retained. These extra
objects are explicitly outside the independently inspected MetaCyc PWY-5901
boundary; no exactMatch with the broader PathBank map is asserted. Native
PWY-5901 directly lists ISOCHORSYN-RXN, ISOCHORMAT-RXN and DHBDEHYD-RXN and
orders all three toward DHB. Its other links concern substrate supply or
subsequent siderophore assembly. No exact GO biological-process term was found
in the pinned full ontology search. GO:0046279 denotes **3,4**-dihydroxybenzoate
biosynthesis and was rejected as the wrong positional isomer.

## Chemistry, directions and source bridges

The source projection retains all eleven Rhea chemical-side occurrences, their
coefficients, participant and compound URIs, and all three complete reactions:

| Native reaction | Selected direction | Decision |
| --- | --- | --- |
| ISOCHORSYN-RXN | RHEA:18986 | Native reversible xref 18988 belongs to master 18985; synthesis uses its LR member. |
| ISOCHORMAT-RXN | RHEA:11113 | Native master 11112 supplies the complete hydrolytic lyase reaction, including water and pyruvate. |
| DHBDEHYD-RXN | RHEA:23825 | Native directed xref agrees with the NAD-dependent net oxidation/aromatization. |

All nine native small-molecule objects explicitly cross-reference the selected
ChEBI identifiers and have exactly matching InChI strings, including charge and
stereochemistry, in ChEBI 255. Rhea 142 sides and the separate official direction
table are replayed against original bytes. The three atom and charge balances
pass. NAD is CHEBI:57540 (charge −1); NADH is CHEBI:57945 (charge −2).
Their biochemical display abbreviations do not substitute for whole-molecule
charges. The intermediate is the exact (2S,3S) species, CHEBI:58764.

EntC is experimentally reversible, with equilibrium favoring chorismate in the
purified-enzyme abstract (PMID:2139795). The selected direction is its pathway
role, not a claim of irreversibility. EntA oxidizes the C3 hydroxyl before rapid
aromatization; this is represented once by the complete net Rhea reaction.
Adding a separate keto-intermediate/aromatization reaction would double count
that conversion. PMID:2144454 describes reverse reduction for **analogues**;
it does not demonstrate physiological reduction of aromatic DHB.

## Enzymes, modified carrier state and assembly limits

- **EntC, P0AEJ2, entC/b0593:** a directly active purified monomer. The native
  ENTC-MONOMER cross-reference and current reviewed annotation identify the same
  gene product. EntA is not required for its isochorismate synthase activity.
  MenF is not substituted: PWY-5901 explicitly excludes the alternative native
  isozyme objects. Two magnesium ions per subunit are an explicit reviewed
  experimental annotation; the separately inspected primary abstract supports
  an EntC–isochorismate–magnesium crystal structure, but does not itself state
  the two-ion count.
- **EntB, P0ADI4, entB/entG/b0595:** the N-terminal isochorismatase performs the
  second reaction. The exact native catalyst ENTB-CPLX is **holo-EntB dimer**,
  with two HOLO-ENTB components. HOLO-ENTB explicitly links to its unmodified
  ENTB-MONOMER, which unifies P0ADI4. The graph therefore preserves the exact
  modified protein and assembly IDs rather than collapsing the modified state
  into an unmodified protein node. P0ADI4 remains an explicit source reference
  and sequence crosswalk. Native and reviewed annotations support the dimer;
  the native comment also records older pentamer/trimer estimates.
- The C-terminal EntB aryl-carrier domain is phosphopantetheinylated by EntD and
  subsequently loaded by EntE for enterobactin synthesis. Those transformations
  are outside PWY-5901. Representing the native holo form does **not** claim its
  carrier-domain modification is necessary for the independent N-terminal lyase
  activity or that apo-EntB is inactive. No free phosphopantetheine cofactor edge
  is added. The Mg edge preserves the exact reviewed EntB cofactor annotation
  (ECO:0000269, PMID:16632253), without inventing an occupancy count or promoting
  the inspected abstract to direct evidence of metal dependence.
- **EntA, P15047, entA/b0596:** the exact native ENTA-CPLX has four ENTA-MONOMER
  components, with a verified P15047 cross-reference. Current UniProt agrees on
  a homotetramer. The 1989 full primary paper (PMID:2521622, p.795) instead reports
  a Superose-12 native mass interpreted as an octamer; this explains the eight
  components in PathBank and is retained as a historical conflict. The 2011
  primary abstract (PMID:21166461) independently reports concentration-dependent
  dimer–tetramer self-association. The selected tetramer is not asserted to be
  the only populated or active state. EntA/EntE interactions concern later DHB
  activation and do not expand this pathway or establish a new fixed complex.

PMID:35952947 reports pairwise EntC–EntB interactions. Its channeling proposal
also uses docking; it does not establish obligatory channeling or a unique
stoichiometric full complex. That distinction is explicit in the target, with no
extra assembly invented. Native holo-EntB cytosol/membrane annotations concern
enterobactin synthase context and are not generalized into whole-pathway
localization edges.

## Primary evidence and microbial scope

The complete scanned **PMID:4928016 / PMC248643** paper was acquired as a real
seven-page PDF, extracted with pypdfium2, and pertinent original pages rendered
and inspected. The study uses K-12-derived strains (Table 1). Its mutant extract
complementation, intermediate accumulation, and Tables 2–3 distinguish the three
steps and genes. Table 2 shows entA extracts fail on all three inputs, entB
extracts retain activity only on dihydro-DHB, and entC extracts retain activity
on both downstream intermediates. This directly grounds the complete K-12
route. The historical route drawing also discusses Aerobacter chemistry; that
does not replace the paper's explicitly tested K-12 mutant results.

The complete eight-page **PMID:2521622 / PMC209666** PDF was similarly acquired,
extracted and rendered. Its purified EntA result and older octamer interpretation
were independently inspected; JM105 recombinant experiments are not relabeled
as MG1655 experiments. The three current reviewed UniProt entries have taxon
83333. MetaCyc protein/assembly objects have MG1655 attribution. The target uses
**NCBITaxon:83333, E. coli K-12**, with those source scopes distinguished.

Retained primary abstracts independently support purified EntC (2139795),
EntB (2139796), EntA mechanism (2144454), EntB structure (16632253), EntA
structure (16790929), EntC–Mg structure (20079748), EntA dimer–tetramer
association (21166461), and EntC–EntB interaction (35952947). Abstract-only
sources are never described as inspected full papers. The BioC request for
PMC248643 returned a no-result error despite HTTP 200; it was rejected and
replaced by the real Europe PMC PDF. The IUCr PDF URL returned purchase/abstract
HTML and the EntB publisher attempt returned 403; neither was accepted as full
text. A public primary EntA figure was visible in search but not used as a
hashed full-paper source. RCSB 2FQ1 coordinates provide corroborating dimer and
magnesium-binding context, with JM109 source and BL21 expression hosts kept
separate; magnesium crystal sites are not converted into an occupancy or
functional-dependence claim. The maintained record's metal claim instead cites
the reviewed cofactor annotation explicitly.

## Context, authority and checks

The root-acquired cohort iModulonDB dataset/search results and exact cached-body
parser replay are separate computational expression context. Ent gene/accession
queries were included. The sole retrieved component table (52) contains no exact
queried candidate members; this is not a biological absence conclusion and
creates no catalytic or regulatory edge.

`dhb-authority-inputs.json` proposes only independently fetched canonical native
HTML and complete current UniProt source inputs. It does not modify shared
snapshots or create an identifier waiver. The source manifest records exact
body hashes, URLs, versions, dates and non-equivalent hash scopes; original
response cookies, session identifiers and authorization headers are excluded.
The source projection records every retained edge's exact source locator and
all deliberate source exclusions. The author replay verifies original RDF,
compound identities, native complete membership, catalysts, holo-state bridge,
assembly coefficients, formal atom/charge balance and actual target KGX evidence
preservation. This is technical reproduction, not independent scientific review.
Root owns the full corpus gates, generated pages, history and publication.

## Independent review correction (#359)

The initial independent review identified a supplementary page-locator error on
edge015. The 1989 primary PDF's EntA octamer Discussion is printed page796
(PDF page6); Results/Purification remains page795. The locator now cites those
exact pages. No biological claim, entity, coefficient or evidence source changed.
The original target and every changed author input are preserved under
`initial-review-inputs/dhb/` with a hash manifest, and the replay now guards this
exact source locator. Issue: https://github.com/CultureBotAI/PathwayMech/issues/359.
