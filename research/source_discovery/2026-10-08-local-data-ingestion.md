# PathBank and dbCAN-PUL local ingestion

Date: 2026-10-08 UTC. This batch follows the user's instruction to continue
data ingestion and address public-release licensing later. It advances the
[previous access/rights assessment](2026-10-08-pathbank-dbcan-rights.md) by
actually acquiring and processing both sources through their public downloads.
The prior licensing observations remain source metadata; they do not block
this authorized local processing.

| Source | Acquired artifact | Local ingestion result |
| --- | --- | --- |
| PathBank | Primary BioPAX ZIP, 2,687 members; HTTP Last-Modified 2019-08-16 | SMP0000983 from PW000967.owl: 7 reactions, 27 participants, 43 structured-evidence edges in one draft |
| dbCAN-PUL | February 2025 workbook, 633 unique locus rows | Complete support TSV with original ordered fields, worksheet/physical-row identity and file digest |

The [PathBank report](2026-10-08-pathbank-local.md) and its manifest pin the
archive, selected member and generated draft. The actual native file exposed
unsupported direction spelling, unrecognized native accession/taxonomy aliases
and lost chemical xrefs. [Issue #299](https://github.com/CultureBotAI/PathwayMech/issues/299)
tracks these corrections. The draft preserves explicit reaction roles and
catalytic assemblies; its omitted stoichiometry, pathway-step membership and
named inhibitory interaction are documented. The archived bytes are not
equated with the current website or promoted to experimentally validated
mechanism records.
Independent review also raised
[issue #300](https://github.com/CultureBotAI/PathwayMech/issues/300): conflicting
taxon identities and unlinked reactions must be refused rather than attributed
to the selected pathway. The acquired canary has neither ambiguity.

The [dbCAN-PUL report](2026-10-08-dbcan-local.md) records the full workbook
audit and a two-locus beta-mannan evidence canary. It distinguishes historical
gene aliases, protein domain grouping and source verification methods.
[Issue #298](https://github.com/CultureBotAI/PathwayMech/issues/298) fixes the
yes/no prediction flag being mistaken for a CAZyme family and provides a
complete original-cell export. The compact legacy lookup columns remain
available, while the provenance view supports exact row reconciliation.

Both inventory entries now use `support` for real-source local ingestion.
Original source files and complete derived outputs are retained in the local
artifact bundle rather than copied into the maintained record corpus.
The durable local bundle is
`reports/local_source_ingestion/2026-10-08-pathbank-dbcan/` in the original
checkout, with a byte-verified `bundle-manifest.json`, original inputs,
`pathbank/SMP0000983-draft.yaml`, and `dbcan/ingested-native.tsv`. This directory
is ignored by Git and remains available after task-worktree cleanup.
No new pathway is added to `data/pathways`; the maintained corpus remains
157 records. Public-release terms, independent identifier approval and
experimental mechanism curation remain separate work items.

Reproduction commands are in [HARMONIZATION](../../docs/HARMONIZATION.md).
Both CLIs validate complete input before printing, and an expected hash binds
the input bytes. BioPAX references retain that digest and supplied source
URL/version; dbCAN provenance retains every ordered native field and locator.
Synthetic regressions exercise the acquired shapes without embedding source
database exports in the test suite.
