# DRAM1 local module-step ingestion — 2026-10-08

The pinned DRAM1 module-step table was acquired and ingested locally as **3,288
support rows**, spanning 399 native module values and 2,445 KO values. Every
native cell, duplicate row, and physical line locator survives the export. No
maintained pathway record, causal edge, organism assertion, or completeness
calculation was generated. Public-release licensing review remains deferred
under the user's local-ingestion instruction; attribution and source lineage
are retained.

## Snapshot and comparison

The [primary repository](https://github.com/BortonWrightonLabs/DRAM) distinguishes
DRAM2 development on `dev` from DRAM1 on `master`. On 2026-10-08, `master` still
resolved to `fe61d759303f30db058d5d505c448b28e41b03f1`, committed 2025-05-15.
The [pinned module table](https://raw.githubusercontent.com/BortonWrightonLabs/DRAM/fe61d759303f30db058d5d505c448b28e41b03f1/data/module_step_form.tsv)
is 579,664 bytes with SHA-256
`55a803dcd7fa10ed05403b36c3aa89b19f007c3601dc60cb703c38828e89a4d9`.
Its Git blob is `8cc5188287de0d487302714b2108cb4ead1f2024`, unchanged from the
[2026-10-03 inspection](2026-10-03-additional-sources-and-updates.md).
That comparison applies to this artifact, not the entire project.

`dev` resolved to `4536cd93c97c07d783fab9e9ef99e56b271f3782`, committed
2026-10-03; DRAM2 rules were not ingested or equated to DRAM1. METABOLIC and
DiTing were not needed to interpret this table and remain separate sources.
The [pinned repository license](https://github.com/BortonWrightonLabs/DRAM/blob/fe61d759303f30db058d5d505c448b28e41b03f1/LICENSE)
is GPL-3.0. This records the software terms without treating them as an
independent resolution of the KEGG-derived content's release terms.

## Native semantics and measured limits

The nine columns are `gene`, `ko`, `module`, `module_name`, `path`,
`product_ids`, `product_names`, `substrate_ids`, and `substrate_names`.
There are 3,029 two-part paths, 249 four-part paths, and ten six-part paths.
There are 801 blanks in each chemical-ID column and 835 in each chemical-name
column. Glycan identifiers occur in 109 rows. Chemical names contain commas;
splitting names and zipping them to ID lists would invent correspondences.

The complete rows at physical lines 1181 and 1184 are identical, including
`M00144`, `K00331`, and `0,0`; both remain distinct artifact locators. In total,
254 module/path groups contain multiple rows. The source's glycolysis canary
`M00001` occupies lines 2–31: 30 rows, 29 KO values, and nine distinct first
coordinates. Line 6 has KO-cell value `K08074` while its description embeds
`K00918`. Both cells are preserved; the description does not override the KO.

The [pinned upstream summarizer](https://github.com/BortonWrightonLabs/DRAM/blob/fe61d759303f30db058d5d505c448b28e41b03f1/mag_annotator/summarize_genomes.py#L282)
groups rows by the complete path string and uses its first integer to form
coverage stages. `get_module_step_coverage` retains a path node when any of its
associated KOs is present. Therefore repeated coordinates cannot automatically
be interpreted as required enzyme subunits, and deeper coordinate components
cannot automatically become ordered reactions. The adapter does not reproduce
that coverage algorithm or infer a Boolean rule from the table. These generic
annotation templates do not themselves supply experimental taxon evidence.

## Adapter and validation

The new offline adapter reads bytes once, checks the supplied SHA-256, validates
the exact native header and every row's width and mandatory fields, and returns
rows only after the entire artifact passes. A caller supplies a full source
commit; the offline loader does not remotely authenticate that commit-to-file
relationship. This acquisition separately verifies the pinned public URL and
GitHub tree blob. A changed schema fails visibly rather than dropping columns.

The 18-column TSV retains all nine native columns plus source basename, commit,
path, pinned URL, digest, start/end physical lines, a local artifact-row locator,
and ordered native header/value pairs as JSON. It preserves original whitespace
and quoted CR/LF/tab content, blank chemical fields, repeated paths, and exact
duplicates. Artifact-row locators are not biological identifiers. No namespace
approval or reaction/chemical identity validation is implied by retaining an ID.

Independent standard-library parsing compared all 3,288 exported rows against
the acquired native table: all 29,592 cells, JSON fields, digests, commit values,
and line locators matched. The export has 2,973,216 bytes and SHA-256
`060823b618d1a7fbbe4b072ccca0bb348014e085752bdbb1a346f5ff06cfb4cc`.
The [metadata and reproduction instructions](2026-10-08-dram-local/README.md)
record the acquisition and measured inventory. Raw source files and the full
export remain local, outside committed research metadata. Module tests use
synthetic rows and check duplicate preservation, multiline locators, lossless
export, digest/commit validation, and refusal of late malformed rows.

Future curation can inspect `M00001` alongside primary enzyme literature and
independent identifier authorities. It must resolve the observed label
discrepancy, define explicit alternative-step semantics, and establish evidence
for any organism or mechanistic assertion before promotion. The next source
refresh should compare this exact table's blob and bytes, while tracking DRAM2
rule artifacts separately.

The durable local bundle and batch boundaries are recorded in the
[DRAM/SEED batch report](2026-10-08-dram-seed-ingestion.md).
