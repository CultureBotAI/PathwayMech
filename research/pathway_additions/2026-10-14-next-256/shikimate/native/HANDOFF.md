# Shikimate degradation I native-source author handoff

This package is author support, not independent scientific approval. No maintained
repository files were edited. The exact native pathway is
`MetaCyc:SHIKIMATEDEG-PWY`, with two reactions: `SHIKIMATE-PQQ-RXN` followed by
`DHSHIKIMATE-DEHYDRO-RXN`. Root owns final chemical normalization and graph
assembly; the primary-source author owns experimental qualifications and the
2005 transcriptional-regulation edges.

Fresh MetaCyc 27.0 originals were acquired and parsed. The current pathway bytes
match the original next251 source; relevant shared reaction/protein bytes match
next255. The replay receipt records actual file hashes and byte comparisons.
Reuse does not import the quinate pathway's additional DHQ dehydration step.

## Coverage and proposed graph

`biological-coverage.json` accounts for the exact 17-object native neighborhood:
7 direct enzyme activities, 7 physical enzymes, 1 recursive complex subunit,
1 auxiliary activity and 1 regulator. Six objects are retained with scope;
eight are outside this pathway variant; two are lower-resolution duplicate
QuiA contexts; and one is adjacent quinate activity. `replay_coverage.py`
recomputes the complete source joins and verifies every disposition/hash.

`supplemental-context.json` separately accounts for six genes, the membrane
location object, and two G. oxydans QDH objects inspected because the pathway
prose and primary literature identify that preparation. These objects are not
silently folded into the direct-reaction denominator. The retained biological
identity proposal contains four catalytic protein preparations, PcaU, and the
two physical gene endpoints. `biological-edge-proposal.json` supplies 13 native
or issuing-authority facts for final reconciliation; primary regulation and
cofactor evidence may add further edges. Its proposed assertions all fit the
400-character limit and carry exact original hashes and locators.

## Required scientific distinctions

- `ENZRXN-11861` correctly joins the shikimate reaction to ADP1 QuiA, but its
  purified-protein code, 74% rate and 260 micromolar shikimate Km refer to
  SA1/AC3 experiments in PMID 14586098. Do not transfer those preparations or
  kinetics to ADP1. The original 1994 genetic/pathway work and reviewed Q59086
  independently support the ADP1 catalytic assignment.
- `MONOMER-1521`/`G-1021` is an accession-free genus-level QuiA representation
  citing the same 1994 ADP1 paper as `MONOMER-28`/`G-27`. It is not evidence for
  a second independent physical catalyst. It remains explicit in the exclusion
  ledger; no unverified exact sequence mapping is asserted.
- QuiA has PQQ as an enzyme cofactor. Native quinone and quinol reaction classes
  are separate participants. Its membrane annotation is curator inference
  (`ECO:0000305`); the original five segments are hydropathy predictions.
- ADP1 QuiC is `UniProtKB:Q43922`. Preserve the recombinant pZR564 crude-extract
  assay qualification. Native `MONOMER-37` prose mislabels its substrate as DHQ
  and gives suspect activity units; the exact activity/reaction join says DHS.
- G. oxydans `MONOMER-1` denotes a partially purified cytoplasmic DHS-dehydratase
  preparation, not a homogeneous or sequence-identified enzyme. Fractionation
  does not establish exclusive localization or every strain's complete route.
- G. oxydans `MONOMER-67` is the IFO3244 purified QDH preparation. Its formal
  activity slot is quinate oxidation, but the inspected `ENZRXN-68` comment
  explicitly reports shikimate activity at 25% of the quinate rate and names
  ferricyanide as the best artificial acceptor. A shikimate edge may cite that
  native assertion. The full 2004 kinetic paper was not independently read in
  this native-source task. Preserve the primary author's abstract-based
  possible-proteolysis qualification (108 kDa native; 65/21 kDa SDS bands).
- Fungal qa-4, Corynebacterium qsuB and its NAD-dependent route, and petrobactin
  AsbF with Mn/Zn regulation remain separately excluded. No biological complex
  is inferred from proximity or common chemistry.
- Pathway species slots list ADP1, A. calcoaceticus and G. oxydans. Historical
  LMD79.41/AC3 contexts do not rename modern ADP1 or prove an identical full
  purified route in all three contexts.

## Regulation identities

`UniProtKB:O83046` is the reviewed PcaU protein, gene `pcaU`, locus `ACIAD1702`,
ADP1 taxon 62977. Its entry notes uncertain initiation at Met1 versus Met5.
Use the primary 2005 evidence for transcriptional regulation, without implying
that PcaU directly activates QuiA or QuiC catalytic activity.

The exact native genes `MetaCyc:G-27` (`quiA`) and `MetaCyc:G-36` (`quiC`) are
verified by original XML product/coordinate joins and native HTML titles and
identity fields. The unchanged `metacyc-html` parser accepts both; see
`gene-html-acceptance.json`. NEW-IMAGE requests returned explicit JavaScript
redirects, preserved separately, and the final authority requests used their
actual `/gene?orgid=META&id=...` destinations.

The native NCBI Gene cross-references 2879574 and 2879469 are discontinued since
2015. Original issuing XML and bounded gene-name-plus-taxon searches are
preserved in `gene-retirement-assessment.json`. Do not add them as live gene
identifiers or conflate nucleotide accession L05770 with a gene ID. The exact
queries returned only those old records; that is not a global proof that no
current successor could exist. No promoter or transcription-unit CURIE was
invented.

## Retention and replay

Retain compact coverage/proposal/identity/context/retirement/acceptance JSON,
acquisition receipts, `original-bindings.json`, this handoff, and the helper
programs as `.py.txt` if useful. Keep all 45 raw XML/HTML/JSON originals external.
The larger `source-projection.json` is an external working projection, not an
independent authority export. Three XML files were downloaded by an erroneous
initial seed list; `original-bindings.json` explicitly excludes them from all
biological claims and the exact source closure does not include them.

Mechanical checks run successfully: `build_handoff.py`, `replay_coverage.py`,
`verify_identity.py`, and `write_identities.py`. The supported native pathway HTML identity also passed `verify_pathway_html.py`.
These are author-support checks;
they do not replace final record validation or independent scientific review.
