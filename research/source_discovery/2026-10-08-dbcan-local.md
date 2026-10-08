# dbCAN-PUL local ingestion — 2026-10-08

The current official workbook was acquired and processed locally: **633 unique
PUL records**, with every native field and its worksheet row retained in the
provenance export. This is a support-table ingestion, not a set of automatically
curated pathways. Original source bytes and the full export remain outside the
repository. Public-release decisions are deferred under the user's local-use
instruction; this report does not reassess licensing.

## Source snapshot and actual coverage

The [official directory](https://pro.unl.edu/static/DBCAN-PUL/) and its
[README](https://pro.unl.edu/static/DBCAN-PUL/README.txt) identify
`dbCAN-PUL_Feb-2025.xlsx` as the current release, based on searches through
February 2025, and report 633 PULs. The downloaded file has SHA-256
`9be758d08cdfd0e36de816819cbcecd04224e4db53a83866369594ecbf3df949`,
115,031 bytes, and a source Last-Modified date of 2025-06-27. Acquisition was
2026-10-08 UTC. The separately retained change log has a newer modification
date; that does not change the workbook's release label.

Independent OOXML inspection found one worksheet, `Add_to_DB`, with data in
physical rows 2–634. There are 20 named columns A:T plus a styled blank header
cell U1, which the provenance export also preserves. Native IDs are unique and
nonblank. After whitespace trimming, the source has 626 degradation and seven
biosynthesis rows. The source contains 209 distinct trimmed taxonomy strings
and 353 distinct PubMed number tokens; these counts do not establish independent
authority validation.

Source evidence is heterogeneous: 25 rows list only sequence homology analysis,
and PUL0751 has an empty verification cell. Twenty rows have no primary locus
tag field, and 13 have no predicted-family field. These are retained as source
blanks, not replaced with inferred experiments, proteins, or reactions.

## Importer defect and verified repair

The earlier importer read all 633 rows but omitted seven columns: old/other locus
identifiers and six prediction/settings fields. It also flattened domain groups
into a deduplicated family summary without preserving the original field.
This affected 162 nonempty old-locus cells and 222 family cells containing a
pipe. [Issue #298](https://github.com/CultureBotAI/PathwayMech/issues/298)
tracks that loss.

The repaired opt-in provenance export retains all ordered native header/value
pairs, source basename, SHA-256, worksheet, and physical row. The original
13-column output remains a normalized search summary; its family list does not
express domain grouping. The source's `cazymes_predicted_dbCAN2` yes/no flag is
not treated as a CAZyme family. On this snapshot, the earlier fallback had
turned 13 blank native family cells into the literal family value `no`; the
repair keeps those summaries empty.

The real workbook was imported with `--sha256` and `--include-provenance`.
An independent standard-library OOXML audit compared all 633 output rows,
including each native cell and artifact locator, against the pinned workbook;
all matched. Reproduction commands and metadata are in the
[audit bundle](2026-10-08-dbcan-local/README.md).

## Bounded candidate and experimental boundary

[PUL0001](https://pro.unl.edu/dbCAN_PUL/dbCAN_PUL/CGC?clusterid=PUL0001),
worksheet row 2, names a 15-gene *Roseburia intestinalis* locus and nine CAZymes.
Its native identifier range is `ROSINTL182_05469–ROSINTL182_05483`. The companion
[PUL0099](https://pro.unl.edu/dbCAN_PUL/dbCAN_PUL/CGC?clusterid=PUL0099), row 76,
has three genes. Crucially, H76 preserves the historical
`ROSINTL182_07683–ROSINTL182_07685` identifiers alongside newer locus tags in G76.
Both rows cite PMID:30796211. These page snapshots are pinned separately from
the workbook; a shared citation does not make two loci identical.

The [primary study](https://www.nature.com/articles/s41467-019-08812-y)
experimentally examines strain L1–82 and describes two loci, MULL and MULS,
in β-mannan utilization (Results, “Two multi-gene loci mediate β-mannan
utilization”; Fig. 2). The workbook's PUL0001 corresponds to the larger locus;
the historical identifiers retained for PUL0099 correspond to the smaller one.
The latter includes RiGH26, with a GH26 catalytic domain and CBM27/CBM23 domains
(Results, “Degradation of the β-mannan backbone”). Thus the raw
`CBM27|GH26|CBM23` grouping is useful biological context, not disposable
punctuation. The study combines growth, expression, protein, binding, and enzyme
experiments; it does not make every imported family prediction an independently
assayed activity.

This candidate is ready for a later evidence-scoped curation handoff. PUL0001
alone must not be promoted to the complete utilization pathway, source species
labels must not silently become experimental strain assertions, and worksheet
order must not become reaction order. No maintained pathway record or causal
graph was created in this ingestion batch.
