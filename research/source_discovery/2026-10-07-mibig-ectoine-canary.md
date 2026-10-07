# MIBiG ectoine cluster canary — 2026-10-07

Added [MIBiG:BGC0000852](https://mibig.secondarymetabolites.org/repository/BGC0000852.5/index.html),
the *Sporosarcina pasteurii* ectABC cluster, as
[`data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml`](../../data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml).
This adds a distinct native cluster and organism scope to the existing
*Halomonas elongata* ectoine pathway; it does not replace that record.

MIBiG labels this entry **questionable**, **active**, and **completeness unknown**.
Those upstream assessments remain unchanged. The acceptance basis is the
independently inspected [primary study](https://doi.org/10.1128/AEM.68.2.772-783.2002)
and its deposited sequence AF316874.1. The study tested the complete operon;
individual enzyme assignments rely on sequence comparison. The graph therefore
records qualified gene support and the observed ectoine output, without isolated
enzyme activity, reaction, cofactor or localization claims. All three deposited
core genes are included. The [DSMZ strain record](https://www.dsmz.de/collection/catalogue/details/culture/DSM-33)
confirms DSM 33 and ATCC 11859 refer to the same type strain.

The output uses CHEBI:27592, **ectoine**, matching the neutral structure supplied
by MIBiG. The related CHEBI:58515 identifier already used elsewhere in the corpus
denotes ectoine zwitterion and was not substituted solely to reuse existing
identifier coverage.

The current entry JSON is byte-identical to its member in the pinned MIBiG 4.0
archive. The official site's current asset declares CC BY 4.0. Exact URLs,
versions, byte digests and digest scopes are in the
[source manifest](2026-10-07-mibig-ectoine-canary-sources.json). Raw downloads
remain outside the repository. The publisher's full article was inspected through
the browser; the preserved NCBI article XML contains only abstract and metadata,
and is explicitly identified as such.

The [review ledger](2026-10-07-mibig-ectoine-canary-review.json) records every gene,
evidence limitation, deduplication result, and three deferred alternatives:
violacein BGC0000829, radicicol BGC0002887 and kotanin BGC0003126. Searches included
ignored and hidden files. No exact cluster, protein, organism or primary-paper
match existed before this addition; the related Halomonas pathway was assessed
explicitly.

Semantic record validation passed. Repository-wide authority, schema, generated
artifact and QC verification belongs to the integration validation report.
