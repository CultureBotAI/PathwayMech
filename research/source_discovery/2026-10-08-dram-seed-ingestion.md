# DRAM and SEED local ingestion

Date: 2026-10-08 UTC. This batch continues actual local source ingestion after
[PathBank and dbCAN-PUL](2026-10-08-local-data-ingestion.md). Public-release
licensing review remains deferred; source attribution, software terms and
upstream data lineage remain part of the acquisition record.

| Source | Acquired input | Admitted local output |
| --- | --- | --- |
| DRAM1 | Pinned `data/module_step_form.tsv`, commit `fe61d759303f30db058d5d505c448b28e41b03f1` | All 3,288 rows across 399 modules, with every native cell and physical locator |
| SEED / PubSEED | Five native API responses for `Glyoxylate bypass`, observed subsystem version `140` | 13 role positions, 4,445 genome rows and three metadata rows; 31,933 feature memberships retained |

The [DRAM audit](2026-10-08-dram-local.md) distinguishes raw path coordinates
from causal order and completeness logic. It records duplicated rows, blank
chemical fields, glycan IDs and a KO/description discrepancy. The adapter
preserves those source facts without collapsing alternatives or splitting
chemical names. Independent full-table comparison verified all 29,592 native
cells and their line locators.

The [SEED audit](2026-10-08-seed-local.md) preserves native role abbreviations,
variant strings and complete feature cells. Independent reconstruction of all
five response payloads from the exported TSV matched exactly. Seven feature
IDs appear under two source roles; those memberships remain distinct. Genome
IDs are not converted into taxonomy identifiers, and variant codes are not
interpreted as experimental phenotypes. The separately acquired responses do
not constitute an atomic database snapshot.

An additional `Alanine biosynthesis` snapshot was acquired but rejected: its
role definitions and feature assignments use different names for one role.
Its 6,690 genome rows are excluded from the ingestion count. Original responses
and the rejection audit are retained; no synonym mapping was invented.

Both admitted sources now have `enabled: true`, `ingest_status: support` in
`conf/sources.yaml`. New offline CLI commands and literal-argument `just`
recipes reproduce the exports; see [HARMONIZATION](../../docs/HARMONIZATION.md).
Synthetic tests cover source integrity, full-input failure, raw-value
preservation and command argument handling. Neither adapter produces a
maintained pathway record; the curated corpus remains 157 records.

The durable local bundle is
`reports/local_source_ingestion/2026-10-08-dram-seed/` in the original checkout.
Its `bundle-manifest.json` pins retained inputs, manifests, outputs and audit
receipts by SHA-256. This ignored directory survives task-worktree cleanup.
Raw database responses and full support exports are not committed to Git.

This batch does not ingest DRAM2, DiTing, METABOLIC or the rest of the SEED
catalogue. DRAM's exact table is unchanged from the October 3 baseline; SEED
is a first successful native acquisition, with no earlier source snapshot for
an update comparison. The remaining sources retain their inventory state.
