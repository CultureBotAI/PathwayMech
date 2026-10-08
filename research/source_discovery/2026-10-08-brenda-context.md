# BRENDA assertion context — 2026-10-08 UTC

The [October 7 pathway canary](2026-10-07-brenda-canary.md) exposed reaction
components but left enzyme, organism and reference context unresolved. This
follow-up recovers two bounded assertions from native website rows, checks the
second against its primary paper and protein authority, and preserves a
[reproducible context audit](2026-10-08-brenda-context/native-context-audit.json).
It adds no maintained pathway or inferred enzyme–organism–reference join.

## Native rows recover context that the RDF enzyme subject does not

The [EC 4.2.1.12 page](https://brenda-enzymes.org/enzyme.php?ecno=4.2.1.12)
contains the following complete, individually scoped rows. Hidden row cells
were read from the acquired HTML, including their original cell IDs and links.

| Native row | Native reaction window | Context in that same row | Boundary |
| --- | --- | --- | --- |
| `tab27r0sr0` | `('3385','I')` | *Pseudomonas fluorescens*, organism argument `294`, literature `33656`; no UniProt accession | An enzyme-class/reaction assertion, not an identified protein. |
| `tab37r0sr1` | `('429165','S')` | *Caulobacter vibrioides* NA1000, organism argument `565050`, UniProt `A0A0H3CB86`, literature `771327`, reversibility code `ir` | A scoped substrate/product assertion, distinct from I/3385. |

The first row describes phosphogluconate dehydration. The adjacent A3.12 strain
row has native organism argument `-3890` and an empty reference cell; its
negative native identifier is not converted into an NCBI taxonomy accession.
The second row explicitly groups substrate, products, strain, protein,
reference and the source's reversibility code. No field is assembled by
crossing unrelated rows.

The bounded [SPARQL query](2026-10-08-brenda-context/scoped-triples.rq) retrieves
four exact subjects, with 825 result bindings below its 2,000-row limit.
`reference/33656` supplies PMID 14245409; `reference/771327` supplies PMID
32266226 and PMCID PMC7099567. `reaction/S/429165` is present as its own native
object, with EC 4.2.1.12 and several enzyme/reference links. Those links do not
identify pairwise enzyme–reference combinations.

The direct `enzyme/329` subject is unsuitable for that join: its 791 triples
contain 210 EC classifications, 71 organism links, 507 references and three
type triples. The complete subject has no identifier predicate. This extends
the previous `enzyme/16699` finding; it does not establish an error in the
provider's underlying enzyme curation. The website rows supply the qualified
context independently. Equal reaction chemistry does not make `I/3385` and
`S/429165` the same native object, and this audit asserts no equivalence between
them.

## Primary evidence and strain identity remain separate checks

The [reference-scoped BRENDA page](https://brenda-enzymes.org/literature.php?e=4.2.1.12&r=771327)
also pairs the Caulobacter substrate/product assertion with accession
`A0A0H3CB86`. The [UniProt issuer response](https://rest.uniprot.org/uniprotkb/A0A0H3CB86.json)
resolves that accession to locus `CCNA_02134` and NCBITaxon:565050, named
*Caulobacter vibrioides* strain NA1000 / CB15N. Its functional annotation uses
`ECO:0000256`; experimental support is checked in the paper rather than
inferred from that annotation.

[Krevet et al. (2020), PMID 32266226](https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2020.00185/full)
characterized purified recombinant CCNA_02134 dehydratase and production of
KDPG from 6-phosphogluconate. The paper names *C. crescentus* and that locus;
the strain scope in this audit comes from the matching BRENDA and UniProt
records, not a separately located strain statement in the paper. Expression
in *E. coli* is an experimental host context. The coupled assay uses
*Sulfolobus acidocaldarius* Saci_0225 aldolase and rabbit lactate dehydrogenase;
these auxiliary enzymes do not establish a native two-enzyme Caulobacter route.
The inspected [corrigendum](https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2020.00761/full)
corrects funding, authorship/contributions and conflicts; its authors report
unchanged scientific conclusions.

The complete downloaded EC 4.1.2.14 HTML contains no ASCII `Caulobacter`
occurrence, including hidden rows. Its declared UTF-8 response has invalid
UTF-8 bytes, so this limited check searches raw bytes without replacement
decoding. It is not an exhaustive search of BRENDA or the literature. The
[older reference page](https://brenda-enzymes.org/literature.php?e=4.2.1.12&r=33656)
provides contextual curation for the Pseudomonas assertion; the 1964 full text
was not independently inspected in this follow-up, and no paper quotation or
new experimental claim is attributed to it.

## Access, provenance and supported ingestion boundary

The [current license page](https://brenda-enzymes.org/license.php) still states
CC BY 4.0; attribution is retained to BRENDA and its requested
[2026 publication](https://doi.org/10.1093/nar/gkaf1113). The website displays
release 2026.1 (March 2026). The RDF response has no demonstrated release
identifier, so it is pinned by retrieval time, exact query and checksum rather
than assigned the website's version. The [bulk-download page](https://brenda-enzymes.org/download.php)
requires affirmative agreement; no bulk archive, acceptance submission,
account action or provider message was used.

The [acquisition manifest](2026-10-08-brenda-context/acquisition-manifest.json)
records exact URLs, UTC times, sizes, content types and SHA-256 digests for ten
external responses. Full pages, articles and the full RDF response remain
outside the repository. The projection retains two native row/cell contexts,
34 exact selected RDF triples, the protein identity and reviewed limitations.
The [standard-library rebuild script](2026-10-08-brenda-context/rebuild_canary.py)
checks all original hashes and the exact transmitted query before regenerating
the projection. It performs no download and does not infer biology from text.

The useful ingestion contract is therefore **component support**, preserving
pathway–reaction–role–compound identity and its original provenance. Website
context requires a separately inspected native row. Neither shared EC numbers,
shared metabolites nor the aggregate enzyme subject supplies organism-specific
pathway topology. The component adapter and this context audit create no
PathwayRecord, protein equivalence, physiological ordering, or whole-pathway
experimental claim.
