# MG canonical difference diagnosis

The actual native outputs are consistent with the production selection rules. The wrapper failed because its proposal-derived expectation retained one bibliography-only PathBank root term and nine unused UniProt source metadata objects. This diagnosis supports accepting those *specific differences* after root completes the interrupted postchecks; it is not final canonical acceptance and does not rewrite the original build or preparation.

Actual counts are **2433 source terms / 575 source metadata**, **1951 ontology terms / 5 ontology metadata**. Both actual builders exited 0. Their recorded stdout/stderr hashes were independently verified. The wrapper then compared output against its expected proposal and raised before completing the remaining verification and seal.

Every old object is preserved: all 2412 source terms, 563 source metadata objects, 1945 ontology terms and 5 ontology metadata objects are exactly equal to the captured baseline. The ordered first 717 manifest entries and first 19 Rhea selectors also match their baseline. The ontology output is exactly equal to the expected ontology snapshot. An independent deep comparison identifies only ten differing source terms and nine metadata entries, with no additional differences.

## Nine UniProt terms

The existing `uniprot-ecoli-reviewed-cofactors` source is manifest entry 74, before the nine fresh individual originals at entries 717–725 (zero-based). Its complete original hash is `754f9ed81673546fc431e009c1b979e9ce6db9cd2cc9b24ef62b5fdd1c3204e7`.

For **P54745, P54746, P23524, P0AA04, P13669, P37047, P0ACF8, P0A9A9 and P0A8M6**, I independently read/parsed the selected original bulk entry and the full individually fetched original, verified each original hash, unique primary accession and taxon83333, and compared the complete source-provided label/synonym result. All nine agree exactly. The actual terms are all new relative to the baseline; no existing term was overwritten. The fresh source versions and complete source-selected objects are retained in `nine-uniprot-source-diagnoses.json`.

Production `build_source_identifier_snapshot.py:1893` and surrounding code keep an already-selected identifier with its first source. A later distinct source does not merge assertions into that term. `sources[key] = metadata` occurs only when that entry actually contributes a selected term. Therefore the earlier bulk provenance is correct, and the nine later individual metadata objects are legitimately absent from the compact authority. Their originals remain present in the build inputs and the record’s scientific references; this does not discard the newer scientific evidence or equate the release versions.

A bounded replay invokes the actual production builder using only those ten original files and the nine real target identifiers. Original ordering exactly reproduces the actual terms and one bulk metadata object. A separately labelled sensitivity control reverses the order: the same labels/synonyms remain, but the nine fresh provenance objects are then selected. This control is not a proposed manifest reorder or an actual-corpus selector change.

## PathBank root and all 62 references

The target declares 53 unique named identifiers. Every one is present in the actual combined authorities. `PathBank:SMP0000839` is a declared native child and is present. `PathBank:SMP0002108` occurs in the bibliography, not in the named record/taxa/participant/reaction lists.

The source builder’s `corpus_ids()` at lines70–87 deliberately collects record IDs and named nodes; it does not collect `references`. The enforcing consumer’s `_named_nodes()` at lines193–204 similarly excludes bibliography entries. References have a separate schema/local-evidence contract. Thus the root need not acquire a compact authority term solely because it is cited.

This is not a claim that the root’s identity is irrelevant or unverified. I freshly verified the full ZIP and unique42234-byte `PW002096.owl` member against their exact hashes, and replayed the actual archive parser. It independently returns the exact root identity and title. The selected child’s authority metadata retains the full ZIP/member/root binding and native `pathway_accessions: [SMP0002108, SMP0000839]`. The reference hash correctly binds the native member rather than misrepresenting it as a ZIP hash.

All62 reference objects are unchanged from the original authored record. Each reference was freshly rebound to its retained source or qualified projection. The61 `source_sha256` values match their originals. PMID14645248 intentionally lacks `source_sha256` because its retained assembled indexed text is not an original publisher PDF; its access limitation and projection binding remain explicit. This check is reference identity/provenance replay, not a fresh scientific rereview of62 sources. Full reference roles and bindings are in `all-62-reference-role-diagnosis.json`.

## Consumer checks and limits

Against external copies of the untouched actual outputs, the actual target passes record-schema validation and the enforcing identifier consumer. Bounded negative controls correctly reject removing required P54746, removing the declared PathBank child, removing the selected bulk source provenance, and mismatching the PathBank root in archive metadata. A separate preservation control detects a changed old ontology label. The final consumer copy was restored byte-for-byte to the actual outputs and passes again.

No full SQL or full canonical rebuild was run. No maintained data, shared cache, build output, preparation input, Git or GitHub state was changed. Diagnostic fixture changes are confined to this separate directory.

Root should retain the original failed wrapper receipt, complete the interrupted original/staged-file/SQL metadata checks, bind exact actual outputs, and seal a successor verification with **2433/575/1951/5**. Do not add a root node or retention selector merely to reach2434, reorder sources merely to reach584, insert a term manually, rewrite labels, or waive arbitrary provenance differences. The accepted discrepancy set is exactly the ten source terms and nine metadata entries captured in `independent-exact-differences.json`.

Stable diagnosis key: `mg-canonical-proposal-selection-expectation`. This is a proposal/verification expectation mismatch, with no demonstrated biological or identifier-consumer defect in the actual outputs. Canonical acceptance remains pending root’s completion and seal.

Actual replay command: pinned195 Python `-B diagnose.py` with `PYTHONDONTWRITEBYTECODE=1 UV_NO_SYNC=1`; exited0 (`da50ab/0`). Independent exact-difference/selected-original read completed (`fe62db/0`), and all nine check results were read (`9265ab/0`). Initial broad inventory/combined expected-snapshot output was truncated and is not claimed as a full human read; bounded code reads and complete machine object comparisons establish the conclusions above.
