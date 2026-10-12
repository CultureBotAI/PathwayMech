The PPi integration preparation's cache-preservation guards accept replacing an old symlink with a different destination containing the same bytes. The independent audit reproduced this in an isolated fixture; no actual shared-cache mutation or scientific defect was found.

Stable key: `PPI-INTEGRATION-001` (cache link identity). Severity: medium; blocks executing this preparation's stated exact-provenance contract.

Owners in the integration preparation: `common.py:inventory`, `common.py:verify_cache_union`, `prepare_inputs.py`, `adopt.py`, and `preserve-maintained.py`. Ninety of the 765 baseline cache paths are symlinks, but captured inventories retain only path, body hash, size and a symlink boolean. Full inventory equality therefore cannot detect same-byte retargeting. The six recovered-source checks bind those six targets correctly but do not cover the other old links.

Prepare a successor that freshly binds resolved destinations and exact link type/text for all old cache paths, checks them at merged-base binding, baseline capture, adoption and preservation, and keeps new cache copies regular. Preserve original sealed packets and historical native/recovery receipts; do not retroactively claim old destination metadata existed. Add isolated controls for same-byte retargeting, regular-to-symlink and symlink-to-regular replacement, and verify actual cache remains unchanged.

Independent audit: `/private/tmp/pathwaymech-next-231-integration-preparation-audit-20261012/handoff.json`, SHA256 `a3df3abbd78c385e8420c5f1f6f589519975e4dd956a48cc9674c4cc1ccb2a2d`. Reproduction SHA256 `1aa8154b2379dadbf35c3e1bad1d713458591bbf7b7684a896a41b0fd7ca2704`. Evidence will be archived with the integration dossier before merge.
