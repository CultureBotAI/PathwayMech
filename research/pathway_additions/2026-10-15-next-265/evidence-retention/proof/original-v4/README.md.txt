# Next265 frozen evidence retention plan

This is a verified external storage rehearsal. No maintained file, scientific claim, Git state or GitHub state was changed. Only this `dry-run-v4` directory is the proposed payload; earlier external rehearsals are audit evidence, not additional payloads.

Every frozen source artifact occurrence, including the source manifest, original and compact bytes, inherited copies, failed attempts, review findings and limitations, has an exact source-to-storage mapping. Sharing storage never erases an occurrence or rewrites a frozen source. Read the [verification receipt](dry-run-verification.json), [source inventory](source-package-inventory.json), [source specification](source-specification.json), and [issue evidence index](issue-evidence-index.md).

The cutoff covers 24 frozen packages and 19 selected root snapshots: 9,629 occurrences (369,961,437 bytes), backed by 1,247 new gzip objects (27,255,667 bytes) plus exact inherited owners. All 5,095 declared compact pairs and all complete hidden/ignored-inclusive frozen inventories passed. All 814 XML occurrences are losslessly mapped.

## Read or reconstruct an original

The [decoder](decode_retained.py) uses only the Python standard library and read-only Git object access. Run from this directory, replacing the repository argument with a repository containing the pinned merged commit:

```sh
python -B decode_retained.py --root . --repo /path/to/PathwayMech --package locator-successor --artifact HANDOFF.md
python -B decode_retained.py --root . --repo /path/to/PathwayMech --package locator-successor --materialize /private/tmp/new-retention-reconstruction
python -B decode_retained.py --root . --repo /path/to/PathwayMech --verify-all
```

The first command displays exact original bytes. The second reconstructs the original complete layout in a new external directory so original relative links remain usable. The third verifies every mapped original and compact artifact. `--compare-originals` additionally checks still-available external input files; those absolute paths are provenance, not required for normal reading. `--working-tree-owners` checks inherited storage in a proposed target checkout rather than the pinned Git objects.

## Storage and inheritance

[content-map.json](content-map.json) maps a source SHA256 to a stored endpoint and ordered gzip decode steps. Each [package source map](packages/) retains all original paths, hashes and byte counts. All new physical source objects are gzip. Identical source bytes and embedded copies share endpoints; different frozen compressed byte representations remain preserved even if their decoded payloads coincide. Uncovered raw XML receives a new exact gzip storage representation recorded in [new-storage-successor-mappings.json](new-storage-successor-mappings.json), never an edit to its frozen original.

[Existing owners](existing-owner-verification.json) were read as exact Git blobs at merged commit `39b84c79eb9997fb6785ef040f571bad498846e7`, tree `e5c455667499283021774a6c3d5138cc8293f28e`. The predecessor XML storage successor is resolved explicitly. The full frozen Rhea RDF gzip is reused from its exact merged owner; it is not dropped or duplicated. Existing-owner coverage is bounded to the predecessor initial-retention receipt and its explicit storage successor. No claim is made to find every historical duplicate in the repository.

## Remaining work and integration boundary

[Pending packages](pending-packages.json) remain separate: independent authority acceptance and actual merged-baseline discovery/context adjudication and acceptance were not frozen at this cutoff. The frozen original integrated review and bounded locator acceptance are preserved as reviewer-authored evidence; retention itself performs no scientific acceptance. Canonical maintained-record reviews and production gates remain separate.

Promotion requires root-owned independent acceptance of this plan, target baseline/owner-byte verification, and an exact copy of this payload to `research/pathway_additions/2026-10-15-next-265/evidence-retention`. No helper here performs maintained promotion. The external `plan_promotion.py` produces a read-only copy plan after checking the frozen stage manifest, merged ancestry, exact inherited owner bytes and destination absence. Do not copy earlier dry runs alongside this payload.

When pending packages freeze, create a new specification and new output directory, explicitly pin their complete manifests and actual compact formats, and rerun the builder plus standalone verification. Preserve this cutoff and all earlier frozen packages unchanged. Never append a guessed manifest or reinterpret an unfinished review as accepted.

## Frozen packages

- [discovery](packages/discovery/README.md)
- [native](packages/native/README.md)
- [chemistry](packages/chemistry/README.md)
- [chemistry-primary](packages/chemistry-primary/README.md)
- [biological-primary](packages/biological-primary/README.md)
- [biological-identities](packages/biological-identities/README.md)
- [cofactor-identities](packages/cofactor-identities/README.md)
- [chemical-design](packages/chemical-design/README.md)
- [taxonomy](packages/taxonomy/README.md)
- [integrated-design](packages/integrated-design/README.md)
- [category-successor](packages/category-successor/README.md)
- [independent-discovery-review](packages/independent-discovery-review/README.md)
- [independent-native-review](packages/independent-native-review/README.md)
- [independent-chemistry-review](packages/independent-chemistry-review/README.md)
- [independent-primary-review](packages/independent-primary-review/README.md)
- [independent-biological-primary-review](packages/independent-biological-primary-review/README.md)
- [independent-biological-identity-review](packages/independent-biological-identity-review/README.md)
- [independent-cofactor-review](packages/independent-cofactor-review/README.md)
- [independent-chemical-design-review](packages/independent-chemical-design-review/README.md)
- [dedup-preflight-review](packages/dedup-preflight-review/README.md)
- [authority](packages/authority/README.md)
- [locator-successor](packages/locator-successor/README.md)
- [independent-integrated-design-review](packages/independent-integrated-design-review/README.md)
- [independent-locator-successor-review](packages/independent-locator-successor-review/README.md)
- [root-intake-and-issue-evidence](packages/root-intake-and-issue-evidence/README.md)
