# Maintained integration checks

Full suite: `7149 passed, 3 skipped, 7 warnings in 1093.26s (0:18:13)`.

`just render-pages`, `just validate`, `just test`, `just lint`, `just vendored-check`, `git diff --check` and the corrected complete staged `git diff --cached --check` passed. [gates.json](gates.json) binds exact commands, timestamps, logs, baseline and unchanged integrated owner bytes. Final canonical review, later metadata staging and publication are separate.

Raw command logs are stored as deterministic gzip files. Each was decoded and compared byte-for-byte to the original, including trailing whitespace; the receipt records both compressed and decoded hashes. No check result or log was filtered. The initial staged check failed on 137 native XML trailing-space lines in 72 originals. Issue628 records the scoped Git-attribute fix; every source byte and all previous proposed owners remain unchanged. Both the original failure and passing successor are retained. The record and infrastructure history calls and integration receipts are also retained.
