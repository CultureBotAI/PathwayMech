# Prospective Entner–Doudoroff authority selection

Canonical external builders and isolated ED identifier checks passed. The prospective selection preserves every current Myx authority term, source record and manifest entry. No maintained or shared cache file was changed.

The full scope is six newly selected source terms but only four new source bodies: KEGG M00008, R02736, R10907 and the MetaCyc KHG/KDPG aldolase complex. P0A955 and P0ADF6 are extracted from the already retained E. coli UniProt batch at `/results/410/proteinDescription` and `/results/1882/proteinDescription`; their canonical names and complete synonym sets match the fresh individual entries. The original batch's `2026_03` metadata is preserved. The fresh entries' audit versions remain scoped to their original scientific evidence bodies.

Ontology additions are named CHEBI:58247 and RHEA:17278 plus reference-only CHEBI:17719. The neutral reference and dianionic participant stay distinct. Manifest count is 568 → 572, source terms 2181 → 2187 and ontology terms 1832 → 1835. All 572 source bodies were freshly rehashed at dry-run completion; canonical ontology extraction streamed the complete issuing databases.

This binds the prospective 218-record Myx working-tree snapshots while HEAD was the prior merged Pyochelin commit babe44ad1992d2950701e432f400965631d538a7. It is not a merged Myx baseline claim; an eventual exact current/merged bridge remains necessary. This is production preparation, not scientific approval or a full-corpus gate. The unchanged ED target/helper and independent external review remain separate.

Use `selected-successor/selection.json` and `canonical-dry-run-successor/{identifier_sources,ontology,sources}.json`. Earlier selected/dry-run outputs remain immutable diagnostics and must not be adopted. The initial ontology-count assumption and redundant UniProt source-owner expectation both failed closed; their exact scripts/logs and dispositions remain present. Six final boundary controls rejected duplicate keys/paths, stale target/policy, optimized Python and existing output directories before source builds.
