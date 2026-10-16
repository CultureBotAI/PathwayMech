# Ethanolamine authority originals

These complete originals reproduce the 63 bounded MetaCyc/EcoCyc and 34 individual UniProt additions for the selected ethanolamine graph. The four ontology additions come from the separately inspected pinned Semantic SQL sources and their accepted, order-preserving delta. The baseline is actual merge `54e768a985d07705ea25445804c83b4758646e37`; every prior source owner and ontology term remains unchanged.

`new-source-manifest.json` uses paths relative to `cache/`. `source-bindings.json` records exact original bytes, retained receipt copies and historical source-owner paths. Those absolute paths are provenance, not reproduction dependencies. Acquisition receipts retain their original contents. ACETALD is an exact historical original with no matching acquisition receipt in the audited source packet. Its source URL establishes the issuing object and is not a claim of a new retrieval.

From the repository root, with its existing dependencies available:

```bash
PYTHONPATH=src:. python research/pathway_additions/2026-10-15-next-272/authority-source-originals/reproduce.py --output /tmp/pathwaymech-ethanolamine-replay
```

Use a fresh output directory. The script reads the immutable Git baseline and only the retained originals. It reproduces the complete additive source snapshot, ontology snapshot and source configuration without a network request or a historical full-cache rebuild. It replays the accepted four-term ontology delta; it does not independently rehash or re-query the external ontology databases. Complete source readings, fresh database hashes, scientific limitations, raw conflicts and independent reviews are retained in the adjacent accepted-preparation archives.

All 128 selected graph identities and labels are separately checked during integration. Reproduction establishes byte and projection consistency, not physiological flux, exact native/UniProt aliases, or independent scientific proof.
