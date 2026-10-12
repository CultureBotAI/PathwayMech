# Independent ATP full native canonical build audit

Verdict: **pass for the actual external canonical build; no findings**. Both native builders completed successfully and the actual outputs independently satisfy the accepted input, preservation and output requirements. This audit does not constitute maintained adoption, a new scientific review, merged-base acceptance, or source exhaustion.

The audited build is `/private/tmp/pathwaymech-next-230-canonical-build-20261012`, handoff SHA-256 `38f95c5b38672f8c23de6deea3e182dd3df7b44ceba5087469bb504e67ffcd93`. Root reported terminal result `3d1d39/0` for session 98559 and supplied the outer execution receipt. I read and verified that receipt, both individual native execution receipts, the complete execution ledger, actual logs, full verification, and sealed handoff. The source builder ran for 88.186 seconds and ontology builder for 124.385 seconds; both exited zero with empty stderr. Commands select the staged runtime, original sources and corpus explicitly. Neither builder was rerun by this audit.

All 479 sealed build artifacts, all 756 original symlinks and their contents, and the complete hidden/ignored/followed inventory passed independent verification. I also reverified the accepted preparation and its independent audit. All 459 staged input files are exactly accounted for, including 222 unchanged runtime files, the complete 230-pathway prospective baseline, final ATP target `cd59859d1dbcbc6c36961822b02daebc519a80a224ba8fa63d3235933b328101`, four baseline authority files and the build-only retention selector. The selector contains only the 4,411 retained IDs, with no labels or injected authority objects. Frozen old records, current target and native code are byte-identical to the accepted preparation.

Actual output contains 2,474 source terms / 595 source metadata objects and 1,963 ontology terms / five ontology metadata objects. Every decoded object equals the accepted expected snapshot. Every old object is preserved exactly: 2,454 source terms, 587 source metadata objects, 1,957 ontology terms and five ontology metadata objects. The only additions are 20 source terms, eight source metadata objects and six ontology terms. I read the complete recorded additions. The actual key sets exactly match the earlier independent native replay of the full old corpus, new target and retention IDs. All source links resolve to metadata present in the actual snapshots.

The 750-entry old manifest prefix is preserved exactly, with eight appended entries for a total of 758. The 22 old ordered Rhea selections and all other Rhea configuration fields are unchanged; two selections give 24 total. Actual manifest/configuration bytes equal the accepted staged inputs. The selected original paths, original hashes and symlink targets match the preparation and execution intake. Whole-archive and exact-member PathBank provenance is retained; no fresh per-pathway download is claimed.

All four actual native SQL full hashes equal their accepted pins. I verified the unchanged code path that performs full-file hashing during every native database read and checked the corresponding actual execution, output metadata, source pins and current file size/mtime. I independently queried release IRI, version and license from each database using read-only SQLite connections; all agree with actual output. This audit did not repeat the large full-file SQL hashes and does not claim a separate audit-time rehash. The native execution, rather than inherited stat checks, supplied the accepted full hashes.

The source log reports all 2,474 identifiers from 595 sources. The ontology log accounts for 978 CHEBI, 132 GO, 38 NCBITaxon and 815 Rhea terms. Rhea's `791/815` SQL message is completed by 24 selected original-RDF terms; it is not an unresolved-identifier report. All 916 `LABEL_DIFFERENCE` diagnostics match the prior accepted EG build exactly after normalizing the corpus directory. None concerns the ATP target. The diagnostic replay retained every original message and introduced no label-based output edits.

Actual native snapshot bytes differ from proposal-file bytes while their decoded objects are exactly equal. Both actual files match their native serializer's formatting. Keep these actual output files for adoption:

| File | SHA-256 |
| --- | --- |
| `sources.json` | `1793e59e5342d4fe56c81760a2c1a55f9c9a277896d6ae4f487b039d50fa05c4` |
| `ontology.json` | `e4cd8cace79ac5e3f2593afb5bae89ba01acf39a5a0ba7a36b56dec9c1146045` |
| `manifest.json` | `ffb86fce9bf012930260cbf79871f791d777c8bd6de20b62358c8cda3ccef0b4` |
| `rhea-updates.json` | `50ff4a4f5f035a5542fd70831dd4bd0872f6d4df97cd8970f82d3f3d5df45fa9` |

Nine independent audit checks and the separate complete diagnostic replay passed. The subject build and preparation remained unchanged. No failed audit attempt, source-cache modification, maintained change, Git operation, installation, synchronization, or builder rerun occurred.

The captured baseline remains explicitly prospective: actual 229-record main at `ed6337d0adbcee81f962c80391e12c0dcc084908` plus the captured EG integration record. An eventual actual EG merge must be checked with a separate exact baseline bridge before maintained adoption. Root separately accepted the final scientific successor; this audit preserves that scope without replacing or extending the scientific review. Maintained curation/history, native review persistence, corpus gates, PR review/merge/publication and remaining pathway discovery are still separate work.
