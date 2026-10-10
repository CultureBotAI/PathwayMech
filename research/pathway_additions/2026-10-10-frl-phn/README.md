# Fructoselysine and methylphosphonate pathway additions

This batch starts from the 159-record corpus at
`d83a2f0bc4f2a3eb54fe732a1b94082b71b1657c`. It follows the repository's
add-pathway workflow and continues the [earlier candidate inventory](../2026-10-10/README.md).
Sources are not exhausted.

The two selected routes are `GO:1901281` (fructoselysine catabolic process) and
`PathBank:SMP0002077` (methylphosphonate degradation I). Their separate source
projections and curation notes preserve exact native statements, experimental
scope, and exclusions. Full downloaded artifacts remain outside the repository.

## Inventory of remaining PathBank leads

[pathbank-screening.tsv](pathbank-screening.tsv) records every archive member
containing an explicitly named E. coli, P. aeruginosa, or S. cerevisiae BioSource,
with its original-byte hash, native pathway IDs and titles, and document counts.
[pathbank-screening.json](pathbank-screening.json) records the complete archive
digest and counts, all observed BioSource labels, and the screen's limits.

The scan parses all 2,687 OWL members. Of the 528 files with these named microbial
BioSources, 205 have one Pathway object and at least two document reactions,
265 have multiple Pathway objects, and 58 have one Pathway object and fewer than
two document reactions. The scan reproduces the earlier aggregate counts and
makes their individual members inspectable.

These are screening classes, not approvals or counts of unique new pathways.
Document reaction counts do not prove native membership. Exact title matches
can cross organisms or route variants and must not cause automatic deduplication.
The 205-member class includes broad maps that may fail the record contract.
BiologicalState and unnamed BioSources remain unclassified; absence from this
named-microbe screen is not a rejection. Multiple-pathway files still need
selection and membership review. The TSV is frozen against the starting corpus;
pathway-specific dispositions below supersede its initial unreviewed status.

Reproduce the screen against that same base corpus and preserved archive:

```bash
.venv/bin/python research/pathway_additions/2026-10-10-frl-phn/screen_pathbank_archive.py \
  --archive /path/to/pathbank_primary_biopax.zip \
  --records /path/to/d83a2f0/data/pathways \
  --output /path/to/screening-output
```

This records candidate discovery progress without claiming that this archive,
the 30-source inventory, or the literature has no additional microbial routes.

One next lead is `PathBank:SMP0002051`, the E. coli L-carnitine degradation I
map in `PW002037.owl`. Inspection finds four native reactions and protein xrefs
P31552, P31572, P31551, and P60584. These remain candidate mappings requiring
independent verification and duplicate searches. The primary
[CaiB/CaiD study](https://pubmed.ncbi.nlm.nih.gov/11551212/) supports a reversible
CoA-dependent conversion, and the [CaiB structure study](https://pubmed.ncbi.nlm.nih.gov/15518548/)
places the route in anaerobic electron-acceptor metabolism. Neither source makes
it interchangeable with all aerobic carnitine degradation.

The similarly titled P. aeruginosa map `PathBank:SMP0122226` in `PW123534.owl`
contains a protein reference named `Unknown` without xrefs and a reference to
A6V382 labelled fatty acid oxidation complex subunit alpha. Its title and four
reactions therefore cannot establish equivalent catalyst coverage. The
[P. aeruginosa CdhR study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5806209/)
is a lead for a separate aerobic route and regulatory context, not validation of
that archived map. No carnitine record is added in this batch.

## Shared evidence boundaries

All 96 pre-existing source-authority artifacts were recovered from the preserved
cache and verified against their committed SHA-256 values before integration.
Existing identifier coverage and provenance must survive the rebuild. PathBank
uses its native SMPDB unification accession, not its distinct PathWhiz filename.
Local graph identities assert existence in the source graph; they do not establish
external chemical identity, pathway membership, or catalysis by themselves.

The canonical iModulonDB adapter found five `frl` gene matches and ten `phn` gene
matches in `e_coli/precise_mg1655`, with no matching iModulon names. These results
provide gene context only. They do not establish a reaction, promoter mechanism,
expression-module membership, or absence of unreturned genes.

Fructoselysine's two-enzyme core must remain distinct from the psicoselysine
extension, promoter regulation, and Enterococcus glycation-product routes.
Methylphosphonate's native four-step route ends at ribose 1,5-bisphosphate.
Purified-protein activity must not imply universal K-12 growth on phosphonates:
the phnE transport state and later PhnK/PhnL complex evidence need explicit scope.

## Integration and review

The two new maintained records bring the corpus to **161 pathways**:

| Record | Bounded network | Edges |
| --- | --- | --- |
| [GO:1901281](../../../data/pathways/fructoselysine-catabolic-process.yaml) | E. coli K-12 FrlD/FrlB fructoselysine catabolism | 14 |
| [PathBank:SMP0002077](../../../data/pathways/methylphosphonate-degradation-i.yaml) | Four-step methylphosphonate conversion through ribose 1,5-bisphosphate | 40 |

[record-identifiers.json](record-identifiers.json) lists every maintained node
and reference ID, its record, and the IDs introduced against the base corpus.
The pathway-specific curation notes, source projections and manifests retain
identity, mechanism evidence, excluded edges, access limits and duplicate-search
scope. Those searches included ignored and hidden source files.

[authority-integration.json](authority-integration.json) records 17 added ontology
terms and 11 source-derived terms, with every previous term and provenance block
unchanged. All 96 previous source artifacts and four ontology databases matched
their pinned hashes. The final 97-input source manifest reproduced its snapshot
byte-for-byte. [pathbank-technical-audit.md](pathbank-technical-audit.md) records
independent parser, policy, archive-screening and regression review.

Adversarial review found and corrected two concrete issues:

- [#317](https://github.com/CultureBotAI/PathwayMech/issues/317): removed an
  unsupported assembly-to-magnesium cofactor assertion. The first catalytic
  edge retains the observed MgATP condition; no magnesium independence is claimed.
- [#318](https://github.com/CultureBotAI/PathwayMech/issues/318): updated the existing
  source-inventory regression to match the reviewed PathBank adoption as active.

[verification.json](verification.json) preserves actual commands, log hashes and
the initial failed test run as well as the successful rerun: **1,034 passed,
three skipped**. Full native/closed-schema, identifier, evidence, source,
documentation, history and generated-page checks pass, as do lint and the
22-artifact governed-file check.
[generated-graph-kgx-audit.json](generated-graph-kgx-audit.json) verifies all 54 new
edges and 88 evidence blocks, SVG endpoints and evidence links, source contexts
and categories, and byte-identical published/CLI exports. No browser preview was
available; structural audits do not claim visual or interaction testing.

Both independent scientific reviews are complete with **pass with limitations**
and no remaining findings. Their specific primary-text and biological-scope
limits remain explicit; full-corpus gates do not scientifically re-review the
existing corpus.

- Fructoselysine: [YAML](../../../reviews/structured/20261010T213921Z-fructoselysine-independent-review/review.yaml)
  and [rendered review](../../../reviews/structured/20261010T213921Z-fructoselysine-independent-review/review.md).
- Methylphosphonate: [YAML](../../../reviews/structured/20261010T213852Z-methylphosphonate-i-independent-review/review.yaml)
  and [rendered review](../../../reviews/structured/20261010T213852Z-methylphosphonate-i-independent-review/review.md).
