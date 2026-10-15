# Next265 evidence retention: bounded issue 581 successor

This is the source-authored correction to the compact-manifest audit in the frozen 24-package retention payload. Only this `payload` directory is the proposed successor. It preserves all source occurrences and stored source bytes; the original v4 package and independent review remain immutable. Independent successor acceptance and maintained promotion are still pending.

The unchanged cutoff contains **24 frozen packages and 19 selected root snapshots: 9,629 source occurrences, 2,865 unique source byte objects and 369,961,437 source-occurrence bytes**. The corrected audit verifies **5,415 compact pairs**, comprising the original 5,095 checks plus 320 previously omitted checks. The 1,247 new gzip source objects (27,255,667 bytes), all package source maps, all inherited-owner bindings and the entire content map are byte-identical to v4. The [comparison proof](verification/v4-successor-comparison.json) records the exact scope. Read the [rehearsal receipt](dry-run-verification.json), [inventory](source-package-inventory.json), [explicit source specification](source-specification.json) and [issue evidence index](issue-evidence-index.md).

## Correction and original finding

[Issue 581](https://github.com/CultureBotAI/PathwayMech/issues/581) identifies an incomplete verification claim. The original builder silently used zero compact pairs when its default root manifest was absent. Three packages own `compact/storage-manifest.json`: native (128 pairs), cofactor-identities (78) and independent-cofactor-review (114). Their array key is `pairs`, their encoding field is `codec`, and every omitted row declares gzip. Exact map hashes, full schemas and counts are in the [correction record](issue-581-correction.json). The original finding and reviewer-authored handoff are retained exactly under [original review evidence](proof/original-review/findings.json); the review found no data loss or other defect.

Every package now has an explicit compact-map path, SHA256 and expected count, or an explicit no-map disposition. Chemical-design, taxonomy and dedup-preflight-review have no package-owned map at either recognized owner location in their complete hidden/ignored-inclusive inventories. Nested inherited maps remain source artifacts. The [corrected builder](proof/corrected-builder.py.txt) rejects missing or inconsistent bindings; it does not silently skip a declared map. The [21 map bindings and three no-map dispositions](explicit-package-compact-audit.json) and [all 5,415 verified pairs](verified-compact-pairs.json) are retained.

This correction adds audit metadata and selected exact finding/control documents. Those documents do not enlarge the frozen scientific-source cutoff or change any source claim. The [original v4 manifest](proof/original-v4/artifact-manifest.json), [original v4 receipt](proof/original-v4/dry-run-verification.json), [original specification](proof/original-v4/source-specification.json) and [evidence-copy bindings](proof/correction-evidence-bindings.json) preserve provenance. The complete original review remains externally frozen; only the explicitly bound correction documents are copied here.

## Read or reconstruct an original

The [unchanged decoder](decode_retained.py) uses Python's standard library and read-only Git object access. Run from this directory with a repository containing the pinned merged commit:

```sh
python -B decode_retained.py --root . --repo /path/to/PathwayMech --package native --artifact compact/storage-manifest.json
python -B decode_retained.py --root . --repo /path/to/PathwayMech --package locator-successor --materialize /private/tmp/new-retention-reconstruction
python -B decode_retained.py --root . --repo /path/to/PathwayMech --verify-all
```

The first command returns exact original bytes. The second reconstructs a complete original layout in a new external directory, preserving relative links. The third checks every mapped source occurrence. `--compare-originals` also compares available external originals; their paths are provenance and are not needed for normal reading. `--working-tree-owners` checks inherited storage in a target checkout instead of pinned Git objects. The bounded successor checks reconstruct the three previously omitted maps and verify all source occurrences with this unchanged reader; they do not repeat the earlier full guarded copy rehearsal.

## Storage and inherited owners

The [content map](content-map.json) gives each source hash an exact endpoint and ordered gzip decode steps. Every [package source map](packages/) preserves original paths, hashes and byte counts, including failed attempts and inherited copies. Distinct frozen compressed representations remain distinct even when decoded bytes match. The [new-storage mappings](new-storage-successor-mappings.json) record exact gzip representations without rewriting raw originals; all 814 XML occurrences remain losslessly mapped.

The [833 inherited owner rows](existing-owner-verification.json) bind actual Git blobs at merged commit `39b84c79eb9997fb6785ef040f571bad498846e7`, tree `e5c455667499283021774a6c3d5138cc8293f28e`. The predecessor XML-storage successor is explicit, and the full frozen Rhea RDF gzip is reused from its exact merged owner. Existing-owner discovery is bounded to the predecessor receipts and does not claim an exhaustive historical duplicate search.

## Cutoff and remaining work

The unchanged [pending register](pending-packages.json) describes the original historical cutoff. The subsequently frozen independent authority review is bound only as a [future extension input](proof/original-preparation/post-cutoff-authority-extension-input.json); its complete package is not retained or newly accepted here. Actual merged-baseline discovery/context adjudication and its independent acceptance likewise remain outside this cutoff. Any extension must use separately pinned frozen manifests and an explicit storage plan that reuses these source endpoints without copying this entire payload again. No global absence or source exhaustion is claimed.

The [read-only planning helper](plan_promotion.py) checks the final stage manifest, merged ancestry, inherited working-tree bytes, all source mappings and destination absence. It performs no maintained writes. After independent successor acceptance, the proposed destination is `research/pathway_additions/2026-10-15-next-265/evidence-retention`. Copy only this final payload; preserve earlier frozen rehearsals as external audit history. Scientific acceptance, canonical maintained-record reviews, production gates and issue closure remain separate. External database files mentioned by source ledgers but not listed in package manifests are not claimed bundled.

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
