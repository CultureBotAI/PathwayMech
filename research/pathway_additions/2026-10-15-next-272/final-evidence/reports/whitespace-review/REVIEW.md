# Independent issue637 packaging review

**Accept the narrow source-XML whitespace successor for issue637.** The change preserves original evidence bytes and allows their existing end-of-line spaces through the staged whitespace check. No supported defect remains in this packaging change. Issue closure still requires the parent's actual merged-tree verification.

Reviewed worktree: `/private/tmp/pathwaymech-next-272-20261015`.

Reviewed maintained owner: `research/pathway_additions/2026-10-15-next-272/authority-source-originals/`.

This is a packaging review, not a new full scientific or authority acceptance. The earlier independent authority review remains its own immutable record, bound by manifest `2be3465bf19b4e3b428ba224a4fee0d85c2ed2efdd59b66818f1b22b161b5cef`.

## Exact change and retained originals

The accepted earlier source-owner inventory contains 207 files. A complete current physical walk, including hidden and ignored files, finds exactly that inventory and no symlinks. Every one of its 206 files other than `.gitattributes` remains byte-identical to the independently accepted inventory. Every current file, including `.gitattributes`, is identical to its staged Git blob.

The prior attributes were exactly:

```gitattributes
cache/**/* -text
acquisition/*.json -text
```

The successor adds only one explanatory comment and this rule:

```gitattributes
/cache/ethanolamine272/*.xml whitespace=-blank-at-eol
```

The existing `-text` rules are unchanged. No source bytes were trimmed or normalized. All 63 native XML and 34 UniProt JSON originals match their exact source-bindings hashes and sizes, source-manifest hashes, accepted inventory hashes, and staged bytes. Both complete source manifests and their hash provenance are included in the unchanged-owner comparison.

The retained original staged failure contains exactly 116 trailing-whitespace diagnostics in 39 files, all within these native XML originals. Its exit code was 2. The parent's retained successor has exit code 0 and empty output. An independent complete `git diff --cached --check` also completed with exit code 0 and empty output.

## Narrow effective scope and adverse controls

Git's effective attributes were queried independently from both the working tree and the index. All 63 actual native XML files have `text: unset` and `whitespace: -blank-at-eol`; all 34 actual UniProt JSON files retain `text: unset` and unspecified whitespace. Nine outside/deeper controls have unspecified whitespace, including a nested XML under `ethanolamine272/nested/`, another cache directory, acquisition XML, source-owner README and Python helper, an XML beside the owner, product Python, and the maintained pathway YAML. The leading slash and single-directory glob therefore do not exempt nested or unrelated files.

Separate scratch controls exercised Git's whitespace engine with the exact observed `-blank-at-eol` setting. They use a command-line `core.attributesFile` argument, which does not persist any configuration or change the repository's attributes. These engine probes are deliberately distinguished from the actual path-scope queries above.

| Probe | Observed result |
|---|---|
| Native-style XML with only trailing spaces | Allowed; no whitespace diagnostic |
| XML with a space before an indentation tab | Rejected with `space before tab in indent` |
| XML with an added blank line at EOF | Rejected with `new blank line at EOF` |
| XML containing merge-conflict markers | Rejected; all three markers detected |
| Ordinary `.py` file with trailing spaces | Rejected with `trailing whitespace` |

For `git diff --no-index --check`, exit 1 means ordinary file differences without a check error; exit 3 means file differences plus a check error. The retained results use those actual meanings, rather than treating a nonzero difference status as a failed probe. No ordinary product whitespace rule or conflict detection was disabled.

## Portable reproduction

The existing maintained `reproduce.py` was run with the verified interpreter, no dependency installation, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONNOUSERSITE=1`, and `PYTHONPATH=src:.`. It consumed its pinned actual Git baseline `54e768a985d07705ea25445804c83b4758646e37` and the retained local source inputs, and wrote only to this review owner's fresh `reproduction/` directory. The original process was observed terminal with exit 0; stdout reports 97 source terms and four accepted ontology additions.

Each complete output equals both the maintained file and its staged blob:

| Output | Bytes | SHA256 |
|---|---:|---|
| sources.json | 23,407,387 | `e9f77bb01f30806cc76dc6ac7a952fb5ed9f03a9a7962a64f7ecb4e0f0c86ede` |
| ontology.json | 410,269 | `8ab396c8de205cbdbb8ade07795536a4b20eec59f5ad4fe5afbc08c1486975c6` |
| identifier_sources.json | 742,442 | `0ff47a8894f3fd9d28cd9ee96afd1c64ade828980371a920a6a1d921e2fddf7b` |

Complete reproduction outputs and routing selection are retained in this packet. Reproduction proves source-byte and projection consistency; it does not independently establish physiological claims or rerun the external ontology-database audit.

The independent checker passed **1,040 checks**. `source-originals-verification.json`, `effective-attributes.json`, `whitespace-engine-controls.json`, `snapshot-reproduction.json`, and `command-receipts.json` contain the detailed evidence. Read-only `git show` receipts retain output hashes and byte lengths instead of duplicating every complete blob in the command log; the source bytes remain in their accepted owner and reproduction outputs are retained here.

## Limits and operational record

Only `/private/tmp/pathwaymech-next-272-whitespace-review` was written. No maintained file, Git index, branch, GitHub issue, source original, source owner, schema, code, record, environment, or governed file was changed. There were no installations, runtime repairs, network acquisitions, source normalization, or active jobs left running.

One initial concatenated exploratory read exceeded its display budget. Bounded subsequent reads and exact programmatic receipt analysis supplied the decision-bearing content; the truncated display was not treated as a complete read. An initial controlled probe confirmed default Git behavior and the exact setting's effect; both results are retained. The independent verification itself passed on its first run. Expected adverse-control failures are intentionally retained and are not product failures.

The issue body identifies closed issue632 as the prior acetate analogue, along with earlier 628 and 621. It keeps open issue493's THIO scope separate. This review does not freshly certify those GitHub statuses or close any issue. Issue637 acceptance is limited to this ethanolamine source owner's packaging successor, pending publication and actual merged-state verification.
