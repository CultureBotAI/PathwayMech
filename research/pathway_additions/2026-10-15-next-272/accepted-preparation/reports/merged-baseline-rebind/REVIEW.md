# Actual PR633 merged-baseline rebind

Qualified acceptance: the next272 candidate preparation is now bound to actual merge `54e768a985d07705ea25445804c83b4758646e37`, tree `d2c58cc6e8c7a7650bdf8d4a91f69b2a54ff8bdb`, in `/private/tmp/pathwaymech-next-272-20261015`. No blocking baseline finding was found. This review does not accept new biological claims, graph design or authority edits.

## Exact corpus binding

All 1,381 baseline checks passed. The actual merge has the exact reviewed PR633 tree from `90695df63225de6f7379c9b48f0519287ac1896e` and sole parent `63ebb3b3e29ca1ed6472597104347d9fbc98f4a5`. All prior 267 maintained record blobs and their discovery-bound SHA256 values are unchanged. The sole new maintained record is `data/pathways/methanogenesis-from-acetate.yaml`, SHA256 `47d1c71951ce5806e5c9570ee00b2ab9f8634158251ee06821a0f77017b0eca3` (206,461 bytes), exactly the accepted reviewed record. All 268 physical YAML records match their committed bytes; all 268 remained unchanged after the search. Read-only Git status was clean before and after.

The historical discovery packet's “pending271” / prospective268 comparison can now be read as the actual268 baseline. This is a successor interpretation, not a mutation of frozen history. The source snapshot, ontology snapshot, configuration, acetate adapter and causal graph documentation match the accepted reviewed bindings. `baseline-rebind-result.json` contains each check and record binding; `baseline-git-read-receipts.json` retains the read-only Git command receipts.

## Candidate and authority ownership

`MetaCyc:PWY0-1477` is not a maintained root or exact candidate-label record in the actual 268-record corpus. A direct `rg --no-ignore --hidden` literal search for `PWY0-1477` and `GO:0046336` in `data/pathways` returned exit 1 with empty output/error. Hidden and ignored files were included, and the separate physical YAML inventory was exactly the same 268 paths. This is not a claim that no ethanolamine-related component or research mention exists.

The historical native-core inventory's 13 present terms are now present in the actual merged source snapshot: `ACETATEKIN-RXN`, `PHOSACETYLTRANS-RXN`, `ACET`, `ACETYL-COA`, `ACETYL-P`, `ADP`, `AMMONIUM`, `ATP`, `CO-A`, `NAD`, `NADH`, `PROTON`, and `Pi` (all MetaCyc). Seven core terms remain absent from the snapshot term inventory: `PWY0-1477`, `ALCOHOL-DEHYDROG-RXN`, `ACETALD-DEHYDROG-RXN`, `ETHAMLY-RXN`, `ACETALD`, `ETHANOL-AMINE`, and `ETOH`. Backlinks to PWY0-1477 in existing source objects do not create a root term. These inventory results neither approve exact chemical identity nor bypass identifier/source integration gates.

## Bounded duplicate search and overlap interpretation

The fresh search used 64 literal patterns: the inherited 37 keys, seven additional exact identifiers/slugs and 20 explicit Rhea-family identifiers. `rg --no-ignore --hidden` included ignored and hidden content, excluded `.git` and `.venv`, retained default binary handling and did not follow external symlinks. It found 676 ordinary matching files. This broad match count includes shared chemicals, reactions, proteins and historical research; it is not a count of duplicate pathways.

The physical archive inventory contains 17,026 containers totaling 1,794,631,473 bytes. Exactly the inherited 116 selected gzip payloads were rehashed, fully decoded and searched: 3,991,511 compressed bytes and 24,849,128 decoded bytes, with 18 matching payloads under the expanded pattern list. Other and nested archive interiors remain unsearched. The historical and current match counts must not be compared as new pathway discoveries because the pattern list was expanded.

All 39 retained exact-root/label leads have bounded dispositions in `exact-root-lead-dispositions.json`: 15 EutE component-activity contexts, five native source backlinks, seven protein-identity contexts, eight historical broad catalog query strings, one dated candidate-gap row, one expression product annotation and two historical corpus copies. Context retention is capped at five occurrences per pattern. These dispositions do not constitute full scientific re-review of all matching files.

Six maintained overlap descriptions were separately read at bounded scope (`bounded-overlap-reading.json`). Acetyl-CoA-to-acetate/ATP formation and the new acetate-methanogenesis route share terminal Ack/Pta components. Three aromatic degradation records share an acetaldehyde/acetyl-CoA reaction family and reference-only native frame context. The yeast ethanol-degradation record has a different entry route and taxon. Those shared components do not replace the missing maintained PWY0-1477 root; they must still be respected when curating shared material/reaction identities. No historical, synonym, source or global pathway exhaustion is asserted.

## Independence and operational limits

This assignment used copied frozen discovery/core/review context and the root's actual worktree receipt; no broad primary-source acquisition was repeated. Prior core/context scientific acceptance, its operational cache correction, and later biological/graph work are separate owners. In particular, this baseline result does not adjudicate EutH substrate protonation, EutP/Q Mg dependence, strain-specific flux, primary-paper claims or graph edge design. Passing mechanical checks does not establish those scientific claims.

No maintained record, identifier authority, source packet, Git reference, GitHub state or runtime was modified. All temporary writes for this assignment are in this new owner. Ruff was invoked with `--no-cache`; initial helper lint/format iterations are retained, and the final helper lint passed. The original checkout's tracked status is clean at `fbccbdc027f2a86ad4919e9dbbb16a736cc0746a`; the inventoried Ruff cache showed no delta during this assignment. That audit is bounded to tracked status and inventoried cache, not a filesystem-wide no-write proof. The separate prior review's cache-write correction is retained and must accompany that prior review.

All started jobs are terminal: baseline session 28855 and search session 9687 both exited 0. The final exact-root command exited 1 because no literal match was found. Final verification rechecked all 268 current record hashes, 19 copied input bindings, the immutable root receipt, actual HEAD and clean worktree status. No full application test pipeline was needed or run for this read-only rebind.
