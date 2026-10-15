# Lossless publication storage successor

Issue [607](https://github.com/CultureBotAI/PathwayMech/issues/607) records the actual staged whitespace failure on 11
single-space context markers in the retained `decoder-exact.diff`. Those spaces
are required patch syntax. The exact diff is stored as deterministic gzip at
`../../evidence-retention/successor-proof/decoder-exact.diff.gz`. `storage-map.json` binds both paths, lengths
and hashes. Decompression recovers every original byte; no whitespace policy
changes. The complete failed stage attempts are preserved in the named archive.

The current physical payload manifest replaces that one entry. The predecessor
manifest and report remain here. All 5,967 other payload files are byte-identical,
including the decoder and every source map. Reconstruction against the complete
predecessor inventory recovers all 5,969 original files exactly. The scientific
record, authorities, implementation, pages and earlier canonical reviews are
unchanged. Those reviews keep their original working-tree cutoffs; their old
physical paths are reconciled through this explicit storage map, not silently
claimed to remain current. The bounded successor review and actual native gates
are separate subsequent observations, and issue closure requires verified merge.
