# Retention review and actual adoption evidence

Issue 591's original independent finding, complete authored successor and
independent acceptance are preserved as separate packages. The exact successor
was copied into the maintained worktree as 3,343 files. Its physical, compact
and inherited-provenance helpers passed on that actual copy.

[The complete source inventory](source-file-manifest.json) binds every file,
including hidden and ignored files. Original-review files (72), authored
successor files (3,448) and acceptance-review files (50) are fully represented.
The author's 3,343 payload files use their exact maintained owners under
`../../evidence-retention/`; they are not duplicated in the archive. Every
other original is a regular member of [files.tar.gz](files.tar.gz), read back
and compared byte for byte with its source. The manifest records each storage
kind and owner path explicitly.

To reconstruct the three original layouts into a new directory, extract the
archive, then copy the complete maintained `evidence-retention` directory to
`authored-successor/payload`. Check every reconstructed file against the source
manifest. The older 3,357-file preparation can additionally be reconstructed
using `../../evidence-retention/reconstruct_predecessor.py` and its exact map.

Selected root observations include the read-only plan, guarded copy, actual
maintained verifier results and research-history creation. The vendored gate
passed 22 canonical artifacts. Its original wrapper named an 18-file manual
snapshot from older repository prose; the separate complete-scope addendum
retains the actual canonical manifest and all 22 authoritative target hashes.
The native gate itself checked all 22. Neither original receipt was rewritten.

The source cutoff remains seventeen frozen packages and twenty-eight source
snapshots. This is subsequent technical verification, not a new scientific
review or proof of PR publication. Issue closure and final production gates
remain separate observations.
