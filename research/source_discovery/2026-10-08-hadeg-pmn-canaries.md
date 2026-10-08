# HADEG and PMN canaries — 2026-10-08 UTC

This continuation adds a HADEG **support association adapter** and a reproducible
four-member evidence audit. It also repairs the PMN/MetaCyc flat-file adapter's
database identity, predecessor branching, and evidence handling. Neither source
adds a maintained pathway in this batch; the corpus remains at 156 records.
PMN still requires an authorized native export before a biological canary can
be completed. This follows the [October 3 source scan](2026-10-03-additional-sources-and-updates.md)
and [October 7 ingestion batch](2026-10-07-next-sources.md).

## HADEG: observed associations, independently scoped evidence

The inspected [HADEG repository](https://github.com/jarojasva/HADEG) is pinned at
`8f1ff8fb3b6452a0fd2667dc78686dced5cd4416`, unchanged from the prior source scan.
Its `Tables/7_All_pathways.csv` contains **629 rows**, 629 distinct raw
`Protein_ID` strings, and **115 distinct `(Compound, Pathway, Subpathway)`
groups**. It contains no organism, citation, reaction-side, or order columns.
Identifier patterns are candidates for verification; the table mixes UniProt,
NCBI protein, UniParc, structure/chain, nucleotide and local identifiers. The
complete input yields 562 UniProt-shaped candidates, 18 versioned NCBI protein
candidates and 49 unresolved strings; every adapter row remains explicitly
`not_verified`. The separate four-member audit supplies issuer evidence only
for its four accessions.

The adapter preserves raw source fields and physical CSV row locators, with
commit, checksum and source provenance. Its output represents
`source_reported_group_membership`; it does not construct mechanistic edges,
`skos:exactMatch` mappings, or a taxon for the group. Verified identity and
claim-specific biological evidence are separate annotations. Source-wide
coverage is therefore support-table coverage, not 115 established pathways.

The [bounded machine canary](canaries/hadeg/finnerty-canary.json) audits CSV
lines 11–14, joined to sheet `1`, rows 12–15, columns A:F of
`1_Aerobic_alkane_degradation_pathways_and_genes.xlsx`. Each join matches the
accession, group, pathway, subpathway and decoded gene exactly.

| CSV line / workbook row | Protein | Issuer-confirmed taxon | Evidence boundary |
| --- | --- | --- | --- |
| 11 / 12 | UniProtKB:Q02UU0, AhpC | NCBITaxon:208963, *P. aeruginosa* PA14 | Function annotation is similarity-based (`ECO:0000250`). |
| 12 / 13 | UniProtKB:Q9I6Z2, AhpF | NCBITaxon:208964, *P. aeruginosa* PAO1 | Similarity-based function; distinct strain from the AhpC row. |
| 13 / 14 | NCBIProtein:BAB33284.1, AlkMa | NCBITaxon:123502, *Acinetobacter* sp. M-1 | Direct gene-complementation evidence; Finnerty membership remains a source claim. |
| 14 / 15 | NCBIProtein:BAB33287.1, AlkMb | NCBITaxon:123502, *Acinetobacter* sp. M-1 | Same functional boundary. |

The four accessions resolve exactly in the issuer responses, including NCBI
version suffixes. UniProt entry versions are 95 and 133. A reviewed Swiss-Prot
entry does not turn its similarity-based function annotation into an experiment
establishing this HADEG group. Combining PA14 AhpC with PAO1 AhpF likewise does
not establish a native protein complex.

The [2001 primary study](https://journals.asm.org/doi/10.1128/jb.183.5.1819-1823.2001)
reports that each M-1 gene restores hexadecane growth in an ADP1 alkM mutant.
This supports gene function, but does not identify either accession as a soluble
Finnerty dioxygenase. Its biochemical reconstitution attempts were unsuccessful.
The [1996 abstract](https://journals.asm.org/doi/10.1128/jb.178.13.3695-3700.1996)
reports a purified flavin-containing oxygenase, without linking it to those
modern accessions. Keep the grouping discrepancy visible. NCBI maps AlkMa to
`AB049410.1:2216..3463` and AlkMb to `complement(AB049411.1:100..1287)`; the 2001
article's accession-number paragraph conflicts with its Figure 2 and the current
issuer mapping, so gene identities were not swapped to match that paragraph.

The publisher's 2001 full text and 1996 abstract were inspected through web
access. Direct article requests returned HTTP 403. The frozen PubMed XML is
citation/abstract provenance, not a substitute advertised as the inspected
2001 full text. The [acquisition manifest](canaries/hadeg/acquisition-manifest.json)
records exact URLs, retrieval times, hashes and sizes; no article or challenge
body is redistributed.

Across all five evidence workbooks, an accession-only lookup gives 538 unique,
87 ambiguous and four missing matches. The missing strings are `GOM1`,
`Q9HXE5`, `A0A031MKR8`, and `A0A1W6L438`. This is why the bounded evidence join
uses complete source context and does not generalize to a first-hit join.

### Reuse and reproducibility

The pinned root LICENSE contains GPL v3 text. The complete upstream tree's
license/readme/copyright paths, README and parsed cells of the five downloaded
workbooks yielded no separate table-data license. This search included all
listed paths irrespective of ignore rules; sequence-file contents were not
exhaustively searched. The four source-derived rows retain upstream terms and
attribution in [THIRD_PARTY_NOTICES.md](canaries/hadeg/THIRD_PARTY_NOTICES.md),
with the exact license text retained alongside them. They are not relabeled
under PathwayMech's repository license. Full tables and workbooks are external
inputs, not newly redistributed corpus files.

The [portable rebuild instructions](canaries/hadeg/README.md) reproduce the
projection from hash-checked original bytes, without an unpinned intermediate
workbook representation or automatic biological interpretation. The projection
sets `group_taxon` and each `reaction_topology` to null and creates zero
PathwayRecord files. A future M-1 alkane-hydroxylase record would require its
own organism-scoped literature curation.

## PMN / ChlamyCyc: adapter repaired, source still gated

The [live ChlamyCyc summary](https://pmn.plantcyc.org/organism-summary?object=Chlamy)
displayed **13.0.0**, *Chlamydomonas reinhardtii* (NCBITaxon:3055), and 354
pathways; its native database selector is `Chlamy`. The
[PMN 17 release table](https://plantcyc.org/release_notes/pmn-release-17-0/)
(2025-12-20) still lists ChlamyCyc **12.0.0** and 354 pathways. This is a first
baseline showing disagreement between two public artifacts, not a measured
change to a previously downloaded export. The PMN-wide release corresponding
to 13.0.0 and current archive version remain unverified.

The [download documentation](https://plantcyc.org/downloads/) describes native
flat-file and BioPAX exports. The [license form](https://plantcyc.org/?webform=license-agreement)
permits use, modification and redistribution subject to source attribution,
retained notices/authors and identified modifications; access requires
affirmative agreement followed by staff instructions. No agreement was accepted,
form submitted or staff message sent in this task.

The web reader displayed the live organism summary, but direct raw requests
for it and the glyoxylate candidate returned 212-byte Incapsula challenges.
These were not treated as source metadata or exports. `GLYOXYLATE-BYPASS`
remains an **unverified candidate frame** in Chlamy; no current native reactions,
directions, proteins or evidence codes were inspected. The
[2009 source paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC2688524/) establishes
the database's PathoLogic/curation lineage and use of prediction, not current
experimental support for every pathway.

No maintained PMN record or source-authority entry was found in an
ignored/hidden-inclusive search of `data/pathways` and
`conf/identifier_sources.json`. The scoped filename search of the original
repository, task/older worktrees, known source caches, and local ontology-data
cache found only synthetic PMN fixtures. `.git` and `.venv` were excluded;
arbitrarily named archives, other home directories and remote storage were not
exhaustively inventoried. The fixture's `CHLAMY-GLYOX` and `RXN-GLYOX-*` values
are synthetic, not inspected upstream identifiers.

### Adapter corrections and next acceptance gate

[SRI's format documentation](https://bioinformatics.ai.sri.com/ptools/flatfile-format.html)
defines UNIQUE-ID within a PGDB. PMN imports therefore require an explicit
`pgdb` argument, represented internally as `PMN:<pgdb>:<frame>` while preserving
the supplied database spelling. This is a PathwayMech source-scoped identity,
not an upstream-global accession. Source version is separate metadata;
MetaCyc identifiers retain their existing form.

[SRI's slot schema](https://bioinformatics.ai.sri.com/ptools/protein-features-ontology.html)
defines every member after the first in a PREDECESSORS tuple as a direct
predecessor. The adapter now preserves all incoming branches, records
structured assertions with indexed source locators instead of invented
quotations, and preserves continuation lines. Malformed, dangling, self-linked
or unresolved hierarchical input fails explicitly. Predecessor order alone
does not become chemical-transfer or stronger causal evidence. These repairs
are tested against transparent synthetic grammar fixtures, not a claimed
native PMN ingestion. Exact `--pathway-id` selection permits an elementary
canary from a mixed full export without rewriting the source; explicit
`--encoding latin-1` handles known non-UTF-8 exports with strict decoding.
Adversarial review independently exercised these behaviors, including SRI
public sample parsing. The defects and repairs are tracked in
[#290](https://github.com/CultureBotAI/PathwayMech/issues/290),
[#291](https://github.com/CultureBotAI/PathwayMech/issues/291), and
[#292](https://github.com/CultureBotAI/PathwayMech/issues/292).

The next useful input is an authorized, versioned native Chlamy export. Record
its archive hash, actual PGDB/version, author/notices and source URL; verify one
elementary pathway exists; inspect its complete linked reaction, chemical,
gene/protein, citation and organism facts; establish independent identifier
authority; and record the disposition of every source fact. Keep experimental,
predicted and curator-inferred evidence distinct before biological review and
the repository's validation gates. PMN remains license-gated pending that
actual canary.
