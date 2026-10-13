# Exact staged whitespace scope

The complete staged `git diff --cached --check` returned 2 with nine trailing-whitespace diagnostics on exactly eight retained original-byte paths. Five are accepted upstream XML originals, one is the exact successful pytest output, and two are retained unified-diff lineage artifacts whose blank context lines contain the format's single-space marker. Every body matches its accepted payload or source map and exact staged blob.

The additional authored-file staged check excludes only those eight literal paths and returns 0. The independent appraisal, full original failure and complete scoped command/streams are retained here. No original body or repository whitespace setting was changed. The original unscoped failure remains a reported scope limitation; it is not relabeled as a full whitespace pass. Prior successful native unstaged diff checks retain their actual scope.
