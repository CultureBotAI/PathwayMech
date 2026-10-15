Independent scientific review of the new `data/pathways/catechol-degradation-i.yaml` draft found that all 35 primary evidence occurrences on `primary-p001` through `primary-p016` use `source_assertion` for paper narrative or mixed table/prose summaries. This comprises 28 edge evidence entries and 7 endpoint-qualifier entries, with 18 unique assertions. The issue is evidence representation even where the underlying scientific claim is supported.

Stable finding key: `pwy5415-primary-evidence-representation`, SCI-F01 (major). Reviewed record SHA-256: `38b3460b24131e7ee2d442e23d226618557bbc5ba56181d7ef9de9ac9e2a0255`; branch `feat/pathway-next-261-20261014`. The complete item inventory is retained in `primary-evidence-item-audit.initial.json` in the independent scientific review package.

`docs/CAUSAL_GRAPHS.md` requires short verbatim quotations or faithful structured-source assertions with exact native locators. Publisher page ranges, indexed abstract summaries and an authored claim ledger do not turn narrative paraphrases into structured statements. Eight occurrences have mixed table/prose support and can retain precise table facts after correction. The native MetaCyc XML assertions are outside this finding.

Acceptance:

- Review and repair every affected edge and qualifier evidence item against the actual inspected original text.
- Use exact short excerpts for prose, or precise table facts with original table/row/column locators. Keep quotation totals short and preserve source access limitations.
- Preserve all supported catalytic, regulatory, assembly and preparation claims. Keep the 1991 pRO1985 enzyme assay separate from the pRO1996 growth report, and the 1996 partial-purification preparation distinct.
- Regenerate pages, pass required repository checks, and save a successor scientific review that explicitly resolves SCI-F01.
