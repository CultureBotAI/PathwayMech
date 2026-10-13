# Exact staged whitespace scope

The full staged `git diff --cached --check` returned 2 with 14 trailing-whitespace diagnostics across exactly four retained original-byte paths. Thirteen lines are the unified-diff format's blank-context space marker; one is the original successful pytest output's two-space blank line. Every staged blob matches its worktree and accepted source or payload.

The additional authored-file check excludes only those four literal paths and returns 0. The independent appraisal, full original failure and exact scoped command/streams remain here. No original body or Git whitespace setting changed. The full unscoped check remains a reported failure; previous successful unstaged checks retain their original scope.
