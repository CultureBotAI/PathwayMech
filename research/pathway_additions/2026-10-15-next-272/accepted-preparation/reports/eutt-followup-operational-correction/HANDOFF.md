# EutT followup operational correction

This immutable addendum supersedes only the false `ruff_format_and_check` status in `results/pre-freeze-verification.json` of `/private/tmp/pathwaymech-next-272-eutt-specificity-followup`. The frozen parent and its scientific evidence remain unchanged. Parent manifest: `1bad82f0d7f0c4856089af17879d90992fc871c9f0383b93e1eaa1a6d0b5b3fc`.

The parent statement that Ruff passed was incorrect: the original check failed with two I001 import-order findings and BLE001 for a broad exception. The freeze script continued despite that failure. The separate pre-freeze evidence verification did pass 49 checks; the frozen parent verification passes 110. Neither constitutes independent scientific acceptance.

The fresh read-only replay with explicit actual-worktree `pyproject.toml` also fails, reporting I001, UP017 and E501 (that config does not select BLE001). Its actual command and output are retained in `results/parent-lint-replay.json`. These are distinct configurations, not an assertion of identical diagnostics. The first correction lint attempt fixed imports/UTC but still failed E501; its failure is retained in `results/helper-lint-fix.json`.

The corrected helper copies sort imports, use UTC, wrap the long message, and restrict acquisition error handling to expected OSError, ValueError and HTTPException classes. The read-only verifier now accepts an explicit source-owner path. Final format and lint pass using the actual-worktree configuration plus explicit BLE001. Running the corrected verifier against the unchanged frozen parent passes 110 checks. Exact commands, exit codes and output are in `results/format.json`, `results/lint.json`, and `results/verify-parent.json`.

No acquisition was rerun; no new network operation, maintained record, Git/GitHub state, runtime or parent file was changed. The corrected acquisition helper was linted but not executed. This addendum fixes operational reporting and helper quality only; independent scientific review of the parent remains required. All jobs are terminal. Preserve this addendum and parent together, without rewriting either.
