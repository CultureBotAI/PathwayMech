# Reproduce the native draft

Keep this package and all four source-author packages immutable. Reproduction
must run in a separate copy, with helper `B` redirected to that copy. The
helpers import the unmodified PathwayMech schema and source parser from the
verified merged baseline `fbccbdc027f2a86ad4919e9dbbb16a736cc0746a`; exact hashes
are in `contract-and-input-bindings.json`. No repository files are written.

Run the repository Python environment on `helpers/build_native.py`, then
`helpers/check_and_disposition.py`. These helpers read captured baseline
authority snapshots and exact native original bytes, issuing chemistry,
biological identity, root-selected additional chemicals, and the captured
15-item primary override selector contract. `build_native.py` writes only
the external draft and its generated ledgers. Its expected draft SHA-256 is
`832e369a8aa0211ed2198b4aa6cbf4825bb24526ba0b7533a539513f6e005ab3`.

The second helper replays all 343 original objects and 5,148 direct slots,
checks every evidence locator and issuing Rhea equation, checks all 28
material facts and six exact joins, generates complete source dispositions,
replays absent source-authority candidates, and runs shape plus closed strict
validation. Its actual time-bearing verification receipt is deliberately
not byte-deterministic. Reproduction does not run `freeze.py` in the frozen
package. All package inventories include hidden and ignored files.

Large retention copies are lossless deterministic gzip (`mtime=0`), with
decoded hashes in `compact-retention-manifest.json`. These are storage
encodings, not new source versions. Native/chemistry/identity/primary source
packages have separate frozen manifests; their exact original inputs are
replayed and referenced, not copied wholesale into this package again.

Root must integrate the independent primary-author overlay, select only
identifiers used by the final integrated record, preserve all existing
authority objects, create record/report history, run full repository gates,
and obtain independent scientific and technical reviews. None of those
future steps is asserted complete by this author package.
