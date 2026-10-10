# Generated graph and KGX integration audit

**PASS**, executed 2026-10-10T22:37:23.667513+00:00. This is a programmatic artifact audit of the two final records, not an independent scientific review or a browser visual inspection.

The actual CLI export completed with exit 0 for 165 records:

```bash
UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just kgx-export --output-dir /private/tmp/pathwaymech-cyanate-monapterin-kgx
```

The independently inspected helper was corrected for the current `enables` predicate, exact rendered descriptions and node types, SVG path syntax and coordinate checks, node-picker coverage, and the explicit monapterin gap. Its actual execution also returned exit 0:

```bash
UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python /private/tmp/pathwaymech-cyanate-monapterin-graph-audit.py --root /private/tmp/pathwaymech-cyanate-monapterin-20261010 --comparison-kgx-dir /private/tmp/pathwaymech-cyanate-monapterin-kgx
```

Script SHA256: `777f9095d0cbb811120742e4a2bb9bdf195ad986b9783c3d3c17378c2b037612`. The full helper and execution logs remain outside the repository at `/private/tmp/pathwaymech-cyanate-monapterin-graph-audit.py`, `/private/tmp/pathwaymech-cyanate-monapterin-graph-audit.log`, and `/private/tmp/pathwaymech-cyanate-monapterin-kgx-audit-cli.log`. CLI log SHA256: `1063bf2940299e097f7c7a7940b6e90abb1e06217fe728c096c0d656f4968086`. The JSON receipt contains record/page hashes, artifact hashes and exact verification counts.

| Record | Local named nodes including scope taxon | SVG nodes | Edges | Evidence items |
|---|---:|---:|---:|---:|
| `MetaCyc:CYANCAT-PWY` | 18 | 17 | 26 | 53 |
| `MetaCyc:PWY0-1433` | 21 | 20 | 24 | 43 |

All 39 local declarations were checked against page component tables and KGX context. The two isolated scope taxa remain represented in the component tables and export; they are not diagram nodes because no mechanistic edge uses them. Every one of the 37 SVG nodes and 50 arrows matches the current local graph. Arrow endpoints touch the correct source/target boxes; paths, Bézier control points, boxes and label coordinates lie within SVG bounds. Node and evidence anchors, reference links, titles, URLs and versions resolve as expected. No rendered-text pixel bounds or interaction behavior is claimed.

Published `pages/downloads/nodes.tsv` and `edges.tsv` are byte-identical to the separately executed CLI output. The audit verifies complete source contexts across the full corpus for all 36 distinct target IDs, including labels, explicit categories and reaction directions. All 96 evidence items, source locators, reference metadata, edge descriptions and provenance fields are preserved exactly; there are no extra or missing target edges. Download-manifest row counts and hashes also match. Record and download hashes remained stable throughout the audit.

- `nodes.tsv`: `e6671a414ca46dcd3108432938848f89270ca62ff14f0b22caf34a23254a290b`
- `edges.tsv`: `926ff51f3a1b28ae5ca25a514487549c2635863e6e2809ac35e5de1badac6cc0`

Issue 322's spontaneous carbamate decay (`RHEA:15650`) has no declared molecular-activity category and exports as `biolink:BiochemicalReaction`; there is no catalyst or enzyme-enables edge to that reaction. The monapterin graph contains only the three supported reactions, no hypothetical `RHEA:34844`/`MetaCyc:RXN0-6368`, no FolX-to-FolM connecting edge, no production of unphosphorylated dihydromonapterin, and no consumption of its triphosphate. The exact rendered description explicitly states the incomplete mechanism.

Root reported no available CUA app/browser surfaces. This audit makes no browser visual-inspection claim and does not replace source-level scientific review or root's full corpus gates.
