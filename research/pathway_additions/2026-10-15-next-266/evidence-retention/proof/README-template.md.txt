# Next266 lossless source evidence retention

This payload retains the complete seventeen-package source cutoff for the seven-step anaerobic benzoyl-CoA degradation II addition, including the accepted issue 590 provenance successor and its independent acceptance. It preserves author and reviewer roles as separate packages. Technical retention acceptance, maintained promotion, production gates and publication are separate observations.

The source inventory contains **7,337 physical occurrences**, **4,757 distinct source contents** and **790,042,247 occurrence bytes**, plus **1,334 compact-only logical original occurrences**. Every hidden and ignored physical source file is included. The explicit specifications bind all **11 package-owned compact map versions** and verify **4,339 declared rows**, including already-compressed originals. A missing default filename never means zero pairs. Earlier native review controls remain historical evidence; `artifact-manifest.final.json`, `HANDOFF.final.md` and the final freeze are authoritative for the independent native review.

The [source specification](source-specification.json), [inventory](source-package-inventory.json), [compact owner audit](explicit-package-compact-audit.json) and [complete verified pairs](verified-compact-pairs.json) define the scope. Nested source copies of another package's map remain source artifacts; the owner audit states its exact boundary. [Issue 590](https://github.com/CultureBotAI/PathwayMech/issues/590) remains represented by the original finding, complete correction package, independent successor acceptance and exact selected root snapshots. The old provenance observations are not rewritten.

## Read and reconstruct

The formatted predecessor decoder is retained byte-identically. It reads physical source files and reconstructs the exact original physical layout:

```sh
python -B decode_retained.py --root . --repo /path/to/PathwayMech --verify-all
python -B decode_retained.py --root . --repo /path/to/PathwayMech --package native --artifact HANDOFF.md
python -B decode_retained.py --root . --repo /path/to/PathwayMech --package merged-discovery --materialize /private/tmp/new-physical-source
```

The additional compact verifier checks every declared row and reads logical originals even when their raw paths intentionally are absent from the physical source:

```sh
python -B verify_compact.py --root . --repo /path/to/PathwayMech --verify-all
python -B verify_compact.py --root . --repo /path/to/PathwayMech --package merged-discovery --artifact source-bindings.json
python -B verify_compact.py --root . --repo /path/to/PathwayMech --package merged-discovery --materialize-logical /private/tmp/new-logical-originals
```

Physical materialization does not invent absent raw files. Logical materialization writes only compact-only originals to a separate new external directory. Every stored representation, logical hash, size and declared inner gzip payload is checked. The original gzip bodies remain distinct source contents even when their decoded payloads agree. `--compare-originals` on the physical decoder additionally compares currently available external originals; those paths are provenance, not dependencies for reconstruction. External database files referenced by source ledgers but absent from source inventories are not claimed bundled.

## Merged owners and storage size

The payload reuses **502 exact Git storage owners** at merged commit `dd780ef273323efd638eacd63625963062e0b105`, tree `93edcbf621df2ca0551830151be39eed5ce21232`. The merge receipt, exact blob identities and decode steps are retained. Inherited lookup is bounded to the two next265 retained content maps and their physical manifests. This is not an exhaustive historical or cross-repository deduplication claim.

There are **3,141 new source endpoints totaling 339,264,576 bytes**. [Storage accounting](storage-size-accounting.json) names the largest endpoints, original package paths and merged-discovery scan owners. The largest endpoint is **46,024,886 bytes**; all new payload files are checked below 100 MiB. The primary independent review preserves both its 46,014,970-byte source tar.gz and its separately frozen 46,024,886-byte gzip representation. The chemistry independent review contributes a 26,699,560-byte archive. Several complete merged-discovery snapshots contribute another 8–9 MB each. Complete inputs and distinct compressed originals are retained without truncation.

All newly stored source bodies, including whitespace-sensitive text, XML, archived helpers and ignored log names, use explicit gzip object storage. The content map preserves exact raw bytes without changing repository ignore or whitespace rules. The two live predecessor helpers retain their accepted formatting. All new live helpers pass the repository Ruff configuration; archived helper bytes are inert evidence.

## Verification and promotion boundary

[Physical verification](verification/physical-standalone-verification.json) and [compact verification](verification/compact-standalone-verification.json) passed. Preparation logs, including transient authoring lint failures and their corrections, are retained through exact [gzip bindings](proof/preparation-observations.json). A complete guarded external copy, physical reconstruction of all source packages, logical reconstruction and negative guard checks are recorded in the outer handoff after this payload freezes; those results do not create a circular payload manifest.

Only this `payload` directory is proposed for `research/pathway_additions/2026-10-15-next-266/evidence-retention`. The read-only planner verifies the pinned final manifest, merged ancestry, actual inherited working-tree owner bytes, all physical mappings and absence of the maintained destination. Independent acceptance is required before guarded copying. Later record integration, history, reviews, gates and publication belong in separate verification evidence. No global source exhaustion or new scientific acceptance is claimed here.
