Issue #390 is resolved in helper `9e21130baba661d36b46d8f25692e111db67ceae4d1d78821649d0d55ae4507e`. The real race now exits with FileExistsError and preserves the exact sentinel, while a fresh-output CLI replay passes 52 original bodies, 54 chemical sides, 10 balances and 94 edges / 149 evidence blocks. All ten independent invalid-input controls reject.

Only final receipt creation changed. The earlier applicability failure against the outdated authority policy is retained and is not counted as a successful race test. The final tests use settled actual next213 authorities and all captured bytes remain unchanged.

This is external technical acceptance, not maintained scientific approval or independent approval of my own authority-selection implementation. Initial observation: /private/tmp/pathwaymech-petrobactin-portable-independent-review-20261011/audit.json.
