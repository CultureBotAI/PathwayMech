# Independent integration successor review

This supersedes the finding disposition in `initial-review.md` for the reviewed working tree, while retaining that original report unchanged. Base commit: `4270a34ae30f4ccb5ce139d8a6f8fde35e938f5b`. Corrected record SHA-256: `03c1fced81d599136ea6577ef4ff314cc428aab9171c522f0334fa4ccba418d4`. Final rendered page SHA-256: `d63865c688b50e19596b4f2de58ac80a54cc6ae4b49682ac5d81ceb7964df7ae`.

## INT-250-01 / issue 526 — resolved

I independently read the code, policy, documentation and test diff. The new optional `authority_entity_types: [reaction]` selector is validated as a nonempty list containing only the supported `reaction` value. Its contextual match reads `term.entity_type` from the verified authority snapshot, rather than a curator-supplied node field. The existing typed-reaction placement check precedes the waiver and requires the reactions collection and molecular_activity category. Rules lacking this selector retain their old matching behavior.

Ten independent controls using copies of the actual maintained snapshots and record all produce their expected outcome. The unaltered record passes; missing identity, false GO/ChEBI/taxon/protein names, wrong native-reaction placement, false pathway-interface label and recategorized false pathway-interface label all fail. Seven malformed selector controls fail policy loading. The original failing pathway-interface case now reports LABEL_MISMATCH, including when the interface is recategorized molecular_activity. The documented acceptance criteria are met. See `successor/audit.json` and `successor/additional-controls.json`.

## Final rendered graph and export

The corrected record independently exports exactly 37 new KGX edges. Every endpoint, predicate, description, evidence object, reference ID and reference metadata object replays to YAML. All 12,329 baseline edges are unchanged, and all baseline node contexts remain present. The published node and edge TSV files byte-match the independent export. The one new record and the additive authority union still preserve all 247 prior YAML files, 4,786 authority terms and 758 source owners.

The final page has 25 graph nodes and 37 directed links. Every declared graph edge has the correct endpoints/predicate, an existing evidence-table anchor and geometric endpoints on its node boundaries. Node and control-point bounds are inside the SVG. There are no node overlaps or conservative edge-label collisions with labels or nodes. The final SVG differs from the visually reviewed initial SVG only in its generated digest namespace. I rerendered the final SVG using librsvg; its PNG is byte-identical to the visually reviewed initial PNG, SHA-256 `6435a99e2878a12d476e1bcb50577d64211347e3572179286df89da19276c587`. See `successor/diagram-audit.json` and `successor/visual-successor-binding.json`. Browser access remains unavailable; no browser-interaction QA is claimed.

## Provenance and source scope

Both authority snapshots were independently reproduced byte for byte using unchanged canonical builders. The 247 staged baseline records match exact baseline Git blobs, and the ID-only selector byte-identically reconstructs from retained and planned IDs. All 21 cited original artifacts were freshly hashed and match their reference bindings. All 27 retained projection files match their recorded external originals. The two chemistry-ledger snapshot digests describe the explicitly recorded baseline Git commit; both match those historical blobs exactly, so their difference from current additive snapshots is expected. See `rebuild-receipts.json` and `provenance-replay.json`.

An additional search including hidden and ignored files inventoried 1,083 raw-format files and found no untracked raw XML, PDF, archive, SQL, ontology or MOL download. This uses `rg --files --no-ignore --hidden` and `git ls-files --others` without exclusion flags. Symlink directories were not followed. See `raw-file-scope.json` and its inventories.

## Remaining review boundary

No unresolved integration finding remains in the inspected working tree. This is not committed-HEAD or full-gate approval: root's final full-gate run is still in progress, and exact committed HEAD remains to be reviewed. The first failed validation is preserved as a failed historical run; it must not be represented as passing. Final approval must bind the actual successful final receipts and verify that the committed code, record, authority and generated artifacts match this reviewed state.
