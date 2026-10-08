# BRENDA and violacein ingestion follow-up

Date: 2026-10-08. This bounded batch continues the
[HADEG/PMN work](2026-10-08-hadeg-pmn-canaries.md). It adds one maintained record
and a BRENDA support adapter; it is not a bulk pathway import.

## Outcomes

| Source | Result | Scope retained |
| --- | --- | --- |
| BRENDA | Enabled local reaction-role support adapter; 62 bindings across 15 reaction objects and 28 compound URIs in the pinned canary | Lossless raw RDF terms and native source locators; no automatic enzyme, organism or reference joins |
| BRENDA native website | Audited two enzyme-class context rows | Website row context remains distinct from RDF assertions and from experimental pathway topology |
| MIBiG / primary literature | One maintained violacein cluster record, five protein contributions and one product edge | Explicit retired BGC0000828 → active BGC0000829 lineage; AB032799.1 experimental proteins are not equated with differing AF172851.1 proteins |
| PathBank | Rechecked a microbial candidate and current data terms | Fixture scope retained; no export was acquired and no new maintained record added |
| dbCAN-PUL | Bounded rights recheck | License-gated status retained; no external data license inferred from software or article licensing |

## Reproducible evidence and remaining boundaries

The BRENDA adapter consumes the original byte-pinned
[role manifest](2026-10-07-brenda-canary/role-import-manifest.json), checks the
exact saved query and source URL, refuses limit-saturated responses, and emits
every original binding as JSON alongside explicit reaction/role/compound URIs.
This validates the saved query bundle, not biochemical correctness or complete
database coverage. See the [native context audit](2026-10-08-brenda-context.md)
and its reconstruction script for the separate two-row evidence.

The [violacein follow-up](2026-10-08-violacein-followup.md),
[source manifest](canaries/violacein/source-manifest.json), and
[review ledger](canaries/violacein/review-ledger.json) preserve the experimental
locus, all four alternative AF-protein dispositions, the independent exact VioE
translation match, and the spontaneous final chemistry boundary. The native
active entry remains quality questionable and completeness complete. The record
uses independent NCBI/OAK authority terms and short verified primary quotations.

The source review also exposed a general MIBiG draft defect: native assessments
and retirement lineage were discarded, while every draft was called
experimentally characterized. [Issue #294](https://github.com/CultureBotAI/PathwayMech/issues/294)
tracks preserving those fields, neutral drafting, and atomic refusal of retired
entries. Independent biological review raised
[issue #295](https://github.com/CultureBotAI/PathwayMech/issues/295), requiring
direct primary support on each asserted gene contribution.

The [PathBank/dbCAN-PUL assessment](2026-10-08-pathbank-dbcan-rights.md) records
the inspected pages, failed export attempts and data-rights conclusions. Those
sources remain deferred. BRENDA enzyme/context joins and broader MIBiG cluster
coverage still need individual evidence review; neither is implied by this batch.
