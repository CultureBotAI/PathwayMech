# Three complete pathway networks

This cohort extends the 198-record baseline at
`720ebcddbc421fbc01a4a82461fcbf13da7ea44f` with three independently bounded
microbial pathways and their generated network pages.

| Record | Native boundary | Representation limits |
| --- | --- | --- |
| GO:0097288 — 7-cyano-7-deazaguanine biosynthetic process | Four transformations from GTP to free preQ₀, also defined by MetaCyc PWY-6703 | The current QueC equation uses two ATP-to-AMP activations. QueD assembly differences and inferred versus direct enzyme evidence remain explicit. Downstream queuosine and antibiotic pathways are separate. |
| GO:0010139 — pyrimidine deoxyribonucleotide salvage | Five EcoCyc PWY0-181 reactions forming dUMP and dTMP | This E. coli implementation is not equated with the differently composed MetaCyc PWY-7199. Transport is incoming context. Source reversibility, chosen salvage direction and strain-specific enzyme evidence remain distinct. |
| MetaCyc:PWY0-1338 — L-Ara4N-modified lipid A biosynthesis | Six native transformations from UDP-glucuronate to aminoarabinose-modified Kdo₂-lipid A | ArnE/ArnF transport roles do not establish a fixed complex assembly or transport energetics. Salmonella purified-enzyme findings remain separate from E. coli genetic evidence. |

PathBank maps supplied discovery leads. Each dossier records full native object
dispositions, pathway boundaries, independent identifiers, original-source hashes
and exact source projections. Original source bodies remain outside the
repository. The replay programs check these original inputs; projected tables
alone are not original evidence. iModulonDB supplies bounded computational
expression context, not proof of reaction membership or catalysis.

`authority-integration.json` records source-driven snapshot extraction and
preservation of all existing authority terms. The explicit Rhea RDF manifest
updates two newly selected equations corrected after the pinned Semantic SQL
release. Canonical label checks remain enforced, and obsolete equations are not
accepted as synonyms. The remaining ontology terms retain their prior sources.
This addresses the new-curation authority gap tracked in
[issue #363](https://github.com/CultureBotAI/PathwayMech/issues/363); it does not
assert that the older published corpus contained the newly selected reactions.

The record reviews, local gate receipt, generated SVG/KGX audit and baseline
preservation audit have separate scopes. Structural and schema checks do not
establish scientific correctness. Any review findings and successor dispositions
are indexed in `review-index.json`. This bounded cohort does not establish source
exhaustion.
