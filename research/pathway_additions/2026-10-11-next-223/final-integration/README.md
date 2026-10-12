# Final integration supplement

This static supplement preserves the late independent adversarial finding, its bounded correction, and the associated scientific and rendering checks. It was prepared externally by the independent reviewer; staging these copies made no maintained-file, Git, GitHub, or original-source changes. `archive-map.json` binds every selected original to its byte-identical copy. Archived Python helpers use an inert `.py.txt` suffix; they are evidence artifacts, not executable repository tests.

The latest reviewed record is SHA256 `fc436f537303f50121c472a4ece19249f3e6eb74d7304933fbafb37e04a61978`. Relative to the independently accepted scientific predecessor `ebbc3eb8334b28b975444285a6e0aab7315a3153a73492270a083cd87fb4f5ff`, its only semantic changes are `category: pathway` on `MetaCyc:PWY0-1324`, `MetaCyc:GLUAMCAT-PWY`, and `MetaCyc:GLYCOLYSIS`. All identifiers, labels, 114 edges, six endpoint qualifications and 66 references are preserved. The existing downstream glycolysis interface stays opaque.

## Review lineage and correction

The independent reviewer initially reported no actionable findings after reading the implementation and executing 49 source/qualification checks. Root then supplied the old-node preservation delta. The reviewer independently reproduced a real typing defect: the three native pathway contexts acquired `biolink:BiochemicalReaction`, and standalone GLUAMCAT-PWY acquired a false union with Pathway. The later `successor-report.md` supersedes the initial disposition and records [issue426](https://github.com/CultureBotAI/PathwayMech/issues/426). Both reports remain immutable.

Root implemented explicit pathway-category support in native and LinkML validation, KGX and graph rendering and added exactly those three annotations. The reviewer did not author the fix. The final `fix-review-report.md` and `fix-review.json` accept it after 15 independent probes, including both record orders, exact edge-payload preservation, real reaction types and physical-role exclusions. The exact native scientific reassessment is archived separately under `science/`; its original SHA256 begins `55c70be8`. Issue closure still belongs to the merged implementation.

## Preserved preparation outcomes

The first maintained gate sequence was deliberately interrupted at terminal `9287ba/130` to make the category correction. Render and skill checks had passed; validation was incomplete and later test/lint/export steps were not reached. `root-category-correction/prior-gate-interruption.json` records this honestly rather than treating the interrupted sequence as a pass.

A subsequent old-node display comparison initially assumed only four name changes and failed at terminal `325378/1`, writing no approval. Inspection exposed the fifth cell: GLUAMCAT-PWY's newly explicit `source_category` changes from empty to `pathway`, while its Biolink category stays exactly Pathway. Root's approval is restricted to the exact five cells in `approved-node-display-delta.json`: two chemical names, two Rhea reaction names, and that source-category annotation. `node-display-review.json` gives the supporting interpretation. It is not a broad preservation waiver; old per-record contexts, old edges and old biological categories must remain preserved by the final gates.

## Page, history and adoption receipts

The corrected actual page has 85 graph display nodes, 362 unique HTML IDs and 352 resolving local fragment links. The root inspected the static graph overview with explicit pathway presentation. The browser tool was unavailable, so these receipts do not claim a full-page screenshot or interactive-browser run. Images and complete SVGs remain external and are not duplicated here.

The initial native-history execution receipt and the category-correction history receipts are retained as exact JSON. The dossier-adoption receipt identifies the previously adopted 313-file compact dossier; this supplement adds later dispositions without rewriting those records.

## Pending final acceptance

No live gate execution file or growing log is archived here. At sealing, this supplement incorporates neither a completed successor full-gate receipt nor the final preservation output. Root will append stable final results separately. The supplement does not claim a completed whole-corpus test run, canonical review bundle, commit, PR acceptance, merge, publication parity or issue closure. Earlier scoped successes remain attributable to their actual executors and times.
