# EG native canonical build preparation

This is a sealed external preparation for a root-owned full native source and ontology build. No full builder was executed, no build output directory was created, and no maintained repository, shared source cache, Git, GitHub, or environment was changed. Scientific acceptance remains separate.

The prospective baseline is exactly 229 pathway records: the actual 228 lyxose records observed at HEAD `fa762a185248fad5b41af6b3efa356fad5fec11e`, tree `6fc1d09d2b5f8c4863c9b97827592f14e0e82940`, byte-checked against the accepted MG input capture, plus the accepted external MG target `b73c407b4315efc45a30ed7121cb3797945cf0a4e86ab010bf5554b276b0e0a6`. This is a prospective composition, not a claim that MG is maintained or merged. Adding the exact EG author target `c24808501b16cc9ad53b1d9c52cd503f0eb5d9be55af4c1406ec6ad47803f704` gives 230 pathway records. The additional retention selector is build-only and is not a pathway record.

The prior canonical state comes from the actual MG `canonical-build` outputs accepted through its separate `canonical-completion` and independent audit packets. There is no invented MG build handoff. It contains 2,433 source terms / 575 source metadata objects and 1,951 ontology terms / 5 metadata objects. All of these objects are retained exactly. The historical MG preparation's former count expectation and wrapper failure remain immutable; those expectations are not reused here.

The expected native EG outputs are 2,454 source terms / 587 source metadata objects, 1,957 ontology terms / 5 metadata objects, 750 ordered manifest entries, and 22 ordered Rhea selectors. These expected snapshots are comparison data only. Both native builders derive their outputs from the original source bodies and SQL originals. No term labels are seeded into a builder, and no source is reordered to force a preferred provenance. Frozen UniProt bulk originals retain their native first-source priority; fresh single-protein originals remain scientific evidence without forcing metadata replacement.

`capture_inputs.py` verified 593 artifacts across five sealed packets, the three root intake receipts, the actual MG build artifact bindings, the 229 prior records, 222 accepted MG runtime files, and 749 original source paths. The runtime includes the accepted three-file MG adapter overlay. Captured runtime config files retain their original historical values; the build commands explicitly select the staged EG manifest and Rhea selectors. The unchanged whole PathBank ZIP is reused with exact typed member bindings. The four SQL hashes are inherited from the accepted actual native MG build, with current byte count and modification time checked; the ontology builder performs the next full SQL hash during its actual root-owned run.

Root may inspect the inert plan or recheck inputs with:

```sh
PYTHONDONTWRITEBYTECODE=1 UV_NO_SYNC=1 /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-229-canonical-preparation-20261012/prepare_and_build.py --check-inputs
```

After independent helper review, root may execute once with:

```sh
PYTHONDONTWRITEBYTECODE=1 UV_NO_SYNC=1 /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-229-canonical-preparation-20261012/prepare_and_build.py --execute
```

Execution requires the sealed preparation and a nonexistent fixed output directory `/private/tmp/pathwaymech-next-229-canonical-build-20261012`. It rehashes every original before the first output write, copies captured code and corpus, creates only external original symlinks, and invokes each native builder once. The two builders run concurrently with separate output files and read-only common inputs. Exact command, environment, working directory, exit status, and stdout/stderr bindings are retained. Postchecks bind actual output counts, preserve every prior source and ontology object, check full native SQL hashes, and recheck the entire staged input inventory. Unexpected native differences are recorded before rejection and require review; the helper never rewrites outputs to satisfy expectations.

Validation: 15 bounded guard tests passed; focused Ruff F checks and non-bytecode compilation passed. The actual input check passed without creating build outputs. Meaningful negatives cover changed target, old record, code, root receipt, retention list, original mapping, prior manifest, shared-cache collision, Rhea ordering, old term and metadata, original hash before staging, wrong output path, and SQL state. The initial preparation failure caused by incorrectly rejecting declared exact-original symlinks is retained with its original script and terminal receipt; no input was changed.

All inventories include hidden and ignored files and follow symlinks. Exact originals remain externally bound rather than copied into this packet. Root still owns full native execution, independent canonical audit, scientific acceptance, any later maintained bridge/adoption, full integration gates, and publication.
