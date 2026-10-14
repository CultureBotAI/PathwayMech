# Shikimate degradation I curation

This addition covers `MetaCyc:SHIKIMATEDEG-PWY`: shikimate oxidation to
3-dehydroshikimate (DHS), followed by dehydration to protocatechuate. It preserves
the complete two-reaction native pathway boundary. QuiB and dehydroquinate belong
to the separate quinate branch and are outside this record. Downstream
protocatechuate ring cleavage and source superpathways remain explicit boundary
interfaces in `chemistry/core-coverage.json` and `native/pathway-coverage.json`.

Baseline: `b645cc4c0afd75f3eff521376b75602a3c2ad679`, with 252 records. The preflight
package records 515 distinct search patterns over three passes per root, covering
both the main checkout and active worktree with ignored and hidden files included.
It also verifies membership and bytes of all 252 baseline Git records. Its bounds
exclude Git internals and virtual environments, default binary content, unfollowed
directory symlinks and undecoded compressed archives. This is a bounded candidate
deduplication, not a claim that every external pathway source is exhausted.

## Chemistry and route

The first reaction remains `MetaCyc:SHIKIMATE-PQQ-RXN`, left to right, with native
quinone and quinol classes. The Rhea 47048 family uses narrower
1,4-benzoquinone/hydroquinone classes, so no exact whole-class mapping is made.
`RHEA:24849` supplies the second, left-to-right dehydration reaction, including
water. PQQ is a separately represented enzyme cofactor and is not the consumed
quinone. Five concrete compounds were checked by complete native structures,
charges, InChI/InChIKey and pinned ChEBI 255 data. The Rhea 142 RDF projection and
reaction balances are in the chemical audit. Current ChEBI shikimate API access
failed with HTTP 504 and then timeout; the exact shikimate mapping relies on the
pinned original SQL, without a claim of current-API verification.

## Biological and experimental scope

The native closure accounts for 17 objects: seven direct enzyme activities, seven
physical enzymes, one recursive subunit, one auxiliary activity and one regulator.
Six are retained with scope, eight belong to other variants, two are duplicate
lower-resolution QuiA contexts, and one is adjacent quinate activity. Nine
supplemental objects have their own ledger and are not silently added to that
denominator. The author proposal supplies 13 native or issuing-authority facts.

ADP1 QuiA (`UniProtKB:Q59086`) and QuiC (`UniProtKB:Q43922`) are distinguished from
other Acinetobacter preparations. The native ADP1 activity comment incorporates
SA1/AC3 purified kinetics; those numeric results and preparation identity are not
transferred to ADP1. QuiA membrane topology and its original five predicted
segments are inference. QuiC activity retains the E. coli DH5α(pZR564), 2.0 kb
HindIII insert, crude-extract qualification; exact expressed termini and a protein
tag were not established. The source substrate typo and suspect activity units are
not copied.

`MetaCyc:MONOMER-1` is a partially purified IFO3244 cytoplasmic DHS-dehydratase
fraction, separated from DQD. It has no resolved sequence or oligomer identity.
`MetaCyc:MONOMER-67` is the IFO3244 membrane QDH preparation with possible
proteolysis into approximately 65 and 21 kDa bands. Its shikimate activity is
supported by the inspected native ENZRXN-68 comment, which reports an
artificial-acceptor assay; the unavailable 2004 full article was not independently
verified for that claim. The inspected primary abstract supports PQQ and the
preparation qualification. Generic quinone grouping does not establish activity
with every quinone or physiological acceptor specificity.

The three taxon contexts remain distinct. ADP1 uses `NCBITaxon:62977`.
`NCBITaxon:471` records the historically identified LMD 79.41 context from the
1988 author reprint, including shikimate-growth and PQQ-mutant evidence, without
modern retyping. `NCBITaxon:442` is native G. oxydans oxidative-enzyme context, not
shikimate-supported growth, complete mineralization or a purified reconstruction
of the complete route. The 1988 discussion summarizes earlier reports of
G. oxydans oxidation without growth; it is not a new 1988 growth experiment, and
those historical contexts are not equated to the later IFO3244 preparations.

## Regulation and identity

The four PcaU/protocatechuate regulation edges describe expression effects in ADP1.
The 2005 work used a direct quiA probe and a shared quiC–quiX probe; quiC evidence
therefore has operon-level scope. Constitutive quiAp transcription remains
independent of PcaU/PCA. These data do not establish direct catalytic activation,
metabolite binding, an isolated quiC promoter or a directly detected full-length
14.4 kb transcript. `UniProtKB:O83046` retains the uncertain Met1/Met5 initiation
context. Article prose is represented by four short verbatim quotes, totaling
20 words, with original section locators; it is not mislabeled as structured data.

The exact native genes `MetaCyc:G-27` (quiA) and `MetaCyc:G-36` (quiC) are retained.
Their old NCBI Gene cross-references were discontinued in 2015. Exact gene-name
plus taxon searches returned the legacy entries, a bounded result rather than a
proof that no successor could exist. The native HTML identity adapter accepted
the genes. No promoter, transcription-unit or exact protein sequence identifier
was invented.

## Authority and assembly

The unchanged builders preserve all 4,907 prior authority terms and add six:
`MetaCyc:SHIKIMATEDEG-PWY`, `MetaCyc:SHIKIMATE-PQQ-RXN`, `MetaCyc:G-27`,
`MetaCyc:G-36`, `UniProtKB:O83046`, and `NCBITaxon:471`. The source manifest grows
from 1,008 to 1,013 entries with its entire baseline prefix preserved. The
independent original hash checks cover 1,028 descriptors and 1,012 distinct cache
paths. The failed typed pathway XML profile is preserved: four unsupported native
slots were rejected. The final authority uses the established native HTML identity
profile; the full XML remains scientific evidence. No source fact was stripped,
no schema/parser relaxation was introduced, and typed pathway metadata acceptance
is not claimed.

The assembled graph has 22 named nodes: the pathway, three taxa, 16 participants
and two reactions. It contains 31 edges and 27 references. `identifiers.json`
enumerates its identities; `chemistry/assembly-ledger.json` binds the record and
assembly inputs. The 13 chemical/context edges, 13 native biological facts, four
primary regulation edges and one qualified G. oxydans PQQ edge remain traceable.
Quote totals and preparation qualifications are recorded in that ledger.

These retained packages are author evidence and reproducibility support, not
independent scientific approval. Final validation, independent review records,
export checks and PR acceptance are maintained by the integration workflow; their
receipts must be consulted before treating the addition as accepted. Follow-up
quinate degradation II, shikimate degradation II, the 2010 membrane DHSase and the
2018 QDH sequence are leads, not claims of completed ingestion or exact mapping.
