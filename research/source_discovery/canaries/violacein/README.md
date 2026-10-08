# Reproduce the violacein sequence comparison

Obtain the four XML artifacts needed by `compare_sequences.py` from the exact
URLs in `source-manifest.json`, and keep the original returned bytes under their
manifest filenames in an external cache directory. The comparison uses only
`AF172851.1.xml`, `AB032799.1.xml`, `AE016825.1-region.xml`, and `AAQ60934.1.xml`.
The genome artifact is the explicit 3558500..3570000 interval, not the complete
genome. All four input digests must match before an output is produced.

```bash
python research/source_discovery/canaries/violacein/compare_sequences.py \
  /path/to/violacein-cache > /tmp/violacein-sequence-comparison.json
cmp research/source_discovery/canaries/violacein/sequence-comparison.json \
  /tmp/violacein-sequence-comparison.json
```

The script uses only Python's standard library. It compares the deposited VioA,
VioB, VioC and VioD protein translations without correcting them, then searches
all six reading frames for the complete deposited 191-aa VioE sequence. Internal
codon assignments are those shared by NCBI genetic codes 1 and 11; no alternative
start-codon override or approximate alignment is used. Reported matches exclude
the stop codon, which is recorded separately. NCBI feature coordinates include
that stop codon, explaining the three-base difference for the genome feature.

These computations establish sequence relationships, not new source annotations
or strain identity. The primary article and JCM catalogue provide the independent
experimental and strain context. The source lineage decision uses MIBiG's
explicit retirement of BGC0000828 as a duplicate of BGC0000829. It does not equate
the AF and AB proteins. Read the sibling review ledger before reusing this graph.

Only the comparison, small provenance manifest and review ledger are committed.
The MIBiG JSON, complete sequence artifacts, article and catalogue remain external;
the repository's own files do not relabel those third-party works. MIBiG source
facts retain attribution to its CC BY 4.0 release, and the RSC paper is copyrighted
by the Royal Society of Chemistry. The maintained record uses six short excerpt instances
from that paper, totaling 24 words including repetitions, with its reference. Browser-inspected
supplementary material has no local raw digest and is explicitly marked as such.
