# Violacein locus reconciliation — 2026-10-08 UTC

Added a bounded [violacein cluster record](../../data/pathways/chromobacterium-violaceum-violacein-biosynthetic-gene-cluster.yaml)
under active **MIBiG:BGC0000829**, after resolving the previous missing-VioE
blocker through explicit source lineage. The graph uses the experimentally
studied **AB032799.1** proteins, not the different proteins in AF172851.1.
Five gene-product `enables` edges and one observed-product edge are retained;
there are no elementary reaction or isolated-enzyme catalysis assertions.

The [active entry](https://mibig.secondarymetabolites.org/repository/BGC0000829.5/annotations.json)
is version 5, **questionable / active / complete**, and points to AF172851.1.
The official MIBiG 4.0 archive also contains **BGC0000828**, version 2,
**questionable / retired / unknown completeness**. That historical entry points
to AB032799.1 and explicitly names BGC0000829 in both its duplicate retirement
reason and `see_also`. This establishes cluster identity lineage; it does not
establish identical nucleotide or protein sequences. The retired identifier
is retained as a provenance reference, not revived as a maintained record.
The current BGC0000828.2 JSON URL returned 404, so its evidence is the exact
member of the pinned official archive. No upstream quality flag was changed.

## Protein and strain scope

The [2007 paper](https://doi.org/10.1039/b705358d), Figure 1, names the JCM 1249
AB032799/pVBG04 clone. Its [supplement](https://www.rsc.org/suppdata/cc/b7/b705358d/b705358d.pdf),
S2, specifies that the assay genes were amplified from this plasmid or its
vioB-containing derivative. The [JCM catalogue](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=1249)
independently equates JCM 1249 with ATCC 12472, supporting strain scope
NCBITaxon:243365. The AB deposit itself carries JCM 1249.

| Gene | Retained assay-locus protein | AF172851.1 protein excluded from this scope | AF versus AB substitutions |
| --- | --- | --- | --- |
| vioA | BAA84782.1 | AAD51808.1 | 1 / 418 aa |
| vioB | BAA84783.1 | AAD51809.1 | 7 / 998 aa |
| vioC | BAA84784.1 | AAD51810.1 | 1 / 429 aa |
| vioD | BAA84785.1 | AAD51811.1 | 2 / 373 aa |
| vioE | AAQ60934.1 | No identical full translation in any of six AF frames | See exact AB match below |

The VioE protein **AAQ60934.1** is deposited on the ATCC 12472 genome at
`complement(AE016825.1:3558964..3559539)`, including its stop codon. Its entire
191-aa sequence matches the translation of **AB032799.1:7301..7873**, followed
by `TAG` at 7874..7876. The AB record does not annotate that CDS; the coordinate
mapping is a reproducible curator computation over issuing-authority sequence
bytes, corroborated by the paper's vioE cloning information. It is not presented
as a GenBank annotation. NCBI's preferred protein name remains **hypothetical
protein**; its domain feature identifies VioE. The functional gene label is
preserved separately.

The AF downstream sequence does not encode an identical full VioE translation
in any reading frame. This finding does not establish the cause of the sequence
discrepancy. Even the AB VioB protein differs from the corresponding AE genome
protein at one residue, so the four AB proteins were retained rather than
replaced with genome representatives. Complete substitutions and exact
coordinates are in the [reproducible comparison](canaries/violacein/sequence-comparison.json).

## Mechanism boundary

The 2006 studies ([PMID:16874749](https://pubmed.ncbi.nlm.nih.gov/16874749/),
[PMID:17176066](https://pubmed.ncbi.nlm.nih.gov/17176066/)) establish the need
for five proteins. Their abstracts were inspected; full texts were not available
in this scan. They do not supply the exact AB-locus assay provenance used here.

The inspected 2007 full paper and supplement identify protoviolaceinic and
protodeoxyviolaceinic acids as the relevant intermediates. Proviolacein and
prodeoxyviolacein are shunt products, and final oxidative decarboxylation is
nonenzymatic. The maintained graph therefore records observed **violacein**
(CHEBI:131914) at the pathway endpoint, without converting an older pathway
cartoon into enzyme-specific reaction assertions. Intermediate, cofactor,
compartment, regulatory and biological-activity nodes remain outside this
bounded cluster record. The product identity is supported by the primary
paper and [ChEBI](https://www.ebi.ac.uk/chebi/CHEBI:131914); MIBiG's historical
structure string alone does not fix every stereochemical detail.

The [review ledger](canaries/violacein/review-ledger.json) records every source
gene and exclusion. The [manifest](canaries/violacein/source-manifest.json)
distinguishes the complete author-hosted paper, abstract-only XML, exact MIBiG
archive member, live entry, protein batch and nucleotide interval. Full raw
artifacts remain external. [Rebuild instructions](canaries/violacein/README.md)
verify original hashes before reproducing the comparison.

The repository and original checkout's `reports/` were searched with ignored
and hidden files included, excluding Git internals and virtual environments.
The prior deferred canary and two cross-Mech protein annotation mentions were
reviewed; no maintained violacein pathway existed before this addition.
Semantic validation and byte-identical comparison reproduction passed.
Repository-wide authority, schema, generated-artifact and QC verification are
reported by the integration workflow.

Independent review [#295](https://github.com/CultureBotAI/PathwayMech/issues/295)
identified missing direct experimental citations on the first four enables
edges. Each now includes the inspected paper's short experimental clause:
VioA/B/D are supported within the precursor-producing mixture, and VioC by its
assayed substrates. The graph retains gene-level contributions without claiming
individual elementary reaction catalysis.
