## Finding

Stable issue key: `thio-review-evidence-python-lint-collection` (P3 / evidence packaging).

After the 131 review-evidence files were copied into the THIO worktree, the actual repository-wide Ruff command exited 1 with 136 diagnostics. All diagnostics are confined to five archived historical scripts under `research/pathway_additions/2026-10-12-next-233/native-integration/`:

- `history-actor-finding/correction-helper-before-sssom.py` (10)
- `history-correction/executed-helper.py` (16)
- `history-correction/imported-stages.py` (10)
- `reviewer-qa/check_final.py` (48)
- `reviewer-qa/qa_rendered.py` (52)

These are retained execution evidence. Preserve their exact original bytes using deterministic gzip and update the portable storage map. Do not reformat the originals or change lint exclusions. Keep the original copy plan, actual adoption receipt and failed lint output as historical evidence. The other 125 adopted receipts must remain byte-identical.

All nine earlier gates passed before these receipt files were added. Those results remain evidence for that source state; they do not establish that the later artifact state passes lint.

## Acceptance checks

- Each of the five compressed bodies decodes to its exact accepted original hash and size.
- Only the five raw untracked copies, their replacement files, the portable map and explicitly enumerated correction evidence change.
- Actual repository-wide lint and final staged whitespace pass against the corrected package.
- Final native reviews bind the real correction and checks without relabeling the earlier failure.

Actual failed lint stdout SHA256: `907e598135407ae1a0f973b573af7e3a2ce78558d60ff069ef01a5623549dda2` (84,276 bytes). The actual command receipt and complete output are retained with the integration evidence.
