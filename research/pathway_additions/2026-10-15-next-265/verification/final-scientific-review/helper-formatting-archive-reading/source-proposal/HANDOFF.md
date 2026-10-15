# Issue 583: retained-helper formatting successor proposal

**Bounded external proposal complete; independent acceptance and maintained adoption remain pending.** This package prepares the minimal honest-documentation correction for [issue 583](https://github.com/CultureBotAI/PathwayMech/issues/583), stable key `next265-retained-helper-lint`. No maintained files, frozen source packages, Git objects or GitHub objects were changed by this author.

The hidden/ignored-inclusive inventory of the entire actual maintained next265 tree finds exactly **four executable `.py` paths**, representing **two unique helper bodies**: `decode_retained.py` and `plan_promotion.py` in each of `evidence-retention` and `evidence-extension`. See [the complete inventory](maintained-helper-inventory.json). The first intake occurred before extension promotion and found two paths; the final direct inventory after promotion establishes all four. The [original root failure receipt](root-initial-failure/retained-helper-initial-lint-receipt.json) and [complete raw failure](root-initial-failure/retained-helper-initial-lint.json) are exact retained copies: 78 diagnostics across four paths, codes `I001`, `E701`, `E702` and `E501`. No broad production-gate result is implied.

## Exact helper candidates and semantic scope

| Helper | Original SHA256 | Proposed SHA256 |
| --- | --- | --- |
| `decode_retained.py` | `c257ac9e52759a5fdf99091adacdd80619bb474d143376d34e189b4ceb0b8ba7` | `7c0ffd8a73a478c4c9a9b408fa9dc59268e6a08135a99fd2871ff523808807fe` |
| `plan_promotion.py` | `8f07f526aa882635626de5af0b53446c981ae6f9cc08e2df0f6076df59bf095b` | `65156d451ca20a385aa39297168b6a431af7d08565c2ef5a013c52b2e854bb01` |

The [semantic proof](formatting-semantics.json) compares every AST node without source-location attributes. The sole permitted AST difference is precisely the move of each module's top-level `from pathlib import Path` statement from the start to the end of its contiguous standard-library import block. The remaining import nodes preserve their exact order, names and aliases. Restoring only that move makes the entire AST identical. There are no renamed variables, removed assertions, changed constants, changed string values, altered functions or other normalizations. All comment tokens are unchanged; no `noqa` or other suppression was added. Both candidates compile without writing bytecode.

Ruff import fixing and formatting were applied only to external copies. One long planner string then required adjacent literal wrapping; its resulting AST constant is exact. The initial formatting attempt and remaining `E501` are retained in the command receipts. Final [native lint](commands/final-candidate-lint.json), [format check](commands/candidate-format-check.json), and the [four-path proposed-layout lint](commands/proposed-four-helper-lint.json) all pass using the exact unchanged current repository configuration. The original `pyproject.toml` is retained and hash-bound. There is no new lint exclusion, rule weakening or changed lint policy.

## Proposed current manifests and historical owners

Only the [20 exact paths](proposed-adoption.json) under the two maintained package directories are proposed: **eight replacements** and **12 newly appended evidence files**. Per package, replace the two live helpers, prefix one current-successor notice to the README, and update the current artifact manifest. Append six files: the complete original artifact manifest, exact original helper bytes as `.py.txt`, exact original README as `.md.txt`, a successor mapping and a short explanation.

Every unrelated original manifest row is preserved as an identical row object, with identical bytes at its original location. All source maps, content maps, object bytes, historical receipts, scientific records and frozen external packages remain unchanged. The old full artifact manifest remains exact historical evidence. To resolve it, the three changed original paths use their explicit archived historical owners; all other original paths keep their existing owners. The original manifest itself has an explicit archived owner. This bridge verifies every original artifact, preserving the full original archive without copying all unchanged storage objects again.

| Package | Original manifest | Proposed current manifest | Current files including manifest |
| --- | --- | --- | ---: |
| `evidence-retention` | `7ad8339a9bdd7ac669475c305ca43096f113f5015766fdd54a0ea05ed86a1b3c` | `e45367b82412ca3bab98c59a8424bc7aa2914553dad318668b8fd18eeed1923a` | 1,343 |
| `evidence-extension` | `ae8b079a63ea634629ea3768560a9e9d5ab73a0acf213e4f74bcb182ac6b40ff` | `e352ec096f59e32f5f67f50cac2475bc107d068cd3464107cc9c6e535a70de5a` | 862 |

The retained base has 1,333 unchanged original rows; the extension has 852. Each prospective manifest changes only three original data rows and adds six evidence rows; it excludes only itself. All prospective file hashes and byte lengths were verified through an overlay of exact unchanged maintained files and proposed external patch files. These are patch directories, **not complete payload copies**: do not replace either whole maintained directory with `proposed/`.

The README change is a prefix only, and its original is both the exact remaining suffix and a separate archived byte owner. The notice makes current helper status explicit because the source-era documentation describes byte-identical helpers. Original acceptance and promotion statements remain historical facts, while current-format helper adoption has a separate receipt. The [base bridge](proposed/evidence-retention/helper-formatting/successor.json) and [extension bridge](proposed/evidence-extension/helper-formatting/successor.json) are explicit proposed dispositions; their pending statements are historical preparation status and need not be silently rewritten during adoption.

## Bounded checks and adoption boundary

The actual formatted decoder passed `--verify-all --working-tree-owners` against both unchanged current packages: [9,629 base occurrences](commands/evidence-retention-candidate-decoder.json) and [2,782 extension occurrences](commands/evidence-extension-candidate-decoder.json). This is a bounded helper behavior check using retained data; no new source acquisition, scientific assessment, corpus rebuild or broad copy laboratory was performed. Planner equivalence is established by the exact AST/import proof and native lint, not a claim that an already occupied maintained destination can pass a new-promotion absence check.

The [adoption specification](proposed-adoption.json) pins all expected old and new hashes, operations and exact destinations. Independent review should verify both current original full manifests, inspect the semantic exception and each prospective current manifest, and confirm full historical resolution. Root should create the six history/bridge files per package exclusively, guard all four replacements per package against their expected old hashes, and verify the complete current and historical inventories afterward. The prospective current manifests must be adopted last. Root then runs current lint and all production gates using the adopted hashes. No generic overwrite or recursive directory replacement is authorized by this proposal.

This follows the historical preservation and narrowly declared AST-equivalence approach used in next219 and next232, without reusing their acceptance for this new change. All jobs are terminal. The proposal is now immutable; any requested correction requires a separate successor. Independent acceptance, actual maintained integration, complete production gates and issue closure are root-owned subsequent work.
