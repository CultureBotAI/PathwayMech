Independent retention review found a minor destination-containment defect in the proposed next267 evidence decoder. Stable key: `next267-retention-scratch-root`.

Proposed owner: `research/pathway_additions/2026-10-15-next-267/evidence-retention/decode_retained.py`, `main()` handling of `--materialize`. Payload manifest SHA256: `9a81127803cb3e0688736a1aeab036d118d1e84f4f46a53f3e3a825d3eb5bcd7`; decoder SHA256: `76fb0382d33f1c7a8951bc46575aeb76c8cfd1f1fc37208aaa80105133beb031`.

The CLI checks lexical `is_relative_to('/private/tmp')` before creating its reconstruction root. A path containing `/private/tmp/../../Users/...` passes, as does a path under a temporary-directory symlink pointing outside scratch. The reviewer intercepted the first `mkdir` for both cases; root separately reproduced the parent-traversal acceptance with the same interception. No out-of-scope file was created.

The per-member relative-path guard does not repair the initial root decision: an escaped root becomes the later containment reference. This is a failure to enforce the documented scratch boundary, not a claim of source corruption or a remote attack.

Acceptance:

- Validate the resolved destination and its existing ancestors before any creation, rejecting traversal and symlink-parent escapes from the intended temporary root.
- Preserve valid fresh scratch reconstruction and rejection of an already existing destination.
- Reproduce both failures without writing outside owned scratch, then show both rejected before `mkdir` in the successor.
- Retain original proposal/findings and independently review the explicit correction successor before adoption.

Keep this issue open until the correction is merged and the landed tree is verified.
