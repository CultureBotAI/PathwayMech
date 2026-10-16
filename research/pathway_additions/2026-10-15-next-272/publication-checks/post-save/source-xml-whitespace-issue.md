Stable key: `next272-authority-original-xml-whitespace`.

The initial staged `git diff --cached --check` for the ethanolamine addition exits 2 on 116 original end-of-line whitespace occurrences across 39 retained XML source originals under `research/pathway_additions/2026-10-15-next-272/authority-source-originals/cache/ethanolamine272/`. The complete failure is retained in `initial-stage-check.json`.

Those XML bytes are evidence bound by upstream hashes and the independent authority review; trimming them would corrupt the retained originals. The existing `-text` attribute prevents newline conversion but does not exempt original end-of-line spaces from the whitespace gate.

Apply the established narrow preservation rule (`whitespace=-blank-at-eol`) only to this directory's original `*.xml` files. Preserve all original sizes/hashes and retain other whitespace checks and ordinary product-file checks. Verify exact staged blobs, the effective Git attributes, the successful staged whitespace successor, and unchanged snapshot reproduction.

This is a new path-specific recurrence of closed #632 (acetate), #628 and #621. Open #493 is scoped to THIO source storage and is not resolved by this ethanolamine correction. Close this issue only after independent acceptance and actual merged-tree verification.
