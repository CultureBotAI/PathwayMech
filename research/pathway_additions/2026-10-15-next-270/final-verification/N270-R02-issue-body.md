The initial complete staged whitespace check for the H2/CO2 methanogenesis addition fails with 137 trailing-whitespace diagnostics in 72 source-native XML files. All affected bytes exactly match the independently accepted authority preparation; the spaces are part of the retained issuing-source originals.

Reproduction: stage the accepted addition and run `git diff --cached --check` (exit 2). Affected paths are limited to `research/pathway_additions/2026-10-15-next-270/authority-source-originals/originals/*.xml` and `authority-source-originals/all-reference-originals/*.xml`. The initial logs and complete path/line inventory are retained under the root verification receipts and will be committed with the fix.

Finding key: **N270-R02**. Severity: minor publication/integration metadata defect; no scientific or source-content defect. The earlier tracked-only diff check did not cover these newly added files.

Fix: preserve every original XML byte and add owner-local Git attributes disabling only the end-of-line blank check for these two native-XML locations. Disable Git text conversion for those same exact-source paths, matching existing source-retention practice. Keep ordinary code, YAML, Markdown and all other whitespace rules unaffected. Do not strip or rewrite the original evidence.

Acceptance: independent review of exact attribute scope; unchanged hashes for all approved scientific/source/product owners; complete staged whitespace check passes; probes outside those XML patterns retain their normal attributes. Preserve the original failed check and successor passing receipt. Close only after the fix is merged and the actual landed tree is verified.
