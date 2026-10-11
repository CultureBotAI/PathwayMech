# Independent MetaCyc Protein XML code review

Changes requested: one P2 finding in the new name-decoding guard. Reviewed the three implementation files at base `7b5201e`, matching the author's frozen file hashes.

`_MetaCycProteinName` and the final label check accept malformed numeric references as canonical names. A well-formed XML common name `protein &amp;#-1;` becomes `protein &#-1;`; an extra-escaped numeric entity remains `protein &#946;`. The escaped numeric reference `protein &amp;#xFFFF;` produces literal U+FFFF. Two actual canonical CLI runs accepted malformed numeric/U+FFFF bodies, exited zero and replaced existing authority-output sentinels. The numeric-reference callback and final residual-entity guard need to reject these forms before emitting a term. Preserve ordinary numeric/Greek decoding and add direct plus CLI output-preservation regressions. Evidence and exact fixtures are in `probe-results.json` and `review.json`.

The four untouched intended native sources pass and retain their exact native names. Identity and database-version mutations reject; nested unresolved objects do not become terms. DTD tests reject (UTF-8/UTF-16 through the callback). XML/HTML conflicts in both orders fail before writing and preserve output. Existing parser definitions and the writer remain unchanged; the existing dispatch and builder are the only modified prior definitions.

This was a bounded code review with 23 independent parser probes and four CLI invocations. The author's 106 focused tests, 309 relevant regressions and lint receipts were inspected; no full canonical rebuild or scientific approval is claimed. No maintained files or Git/GitHub state were changed.
