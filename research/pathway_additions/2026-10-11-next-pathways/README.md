# Pseudouridine, homogentisate and thiamine pathway additions

This cohort adds three complete, separately bounded pathways to the 177-record
baseline at `6a331b8b9fd7bf4d9f7b6d2f6626b29157b47a69`.

| Record | Maintained source | Curation and boundaries |
| --- | --- | --- |
| MetaCyc:PWY-6019, pseudouridine degradation | [YAML](../../../data/pathways/pseudouridine-degradation.yaml) | [Dossier](pseudouridine-curation.md) |
| GO:1902000, homogentisate catabolic process | [YAML](../../../data/pathways/homogentisate-degradation.yaml) | [Dossier](homogentisate-curation.md) |
| MetaCyc:THISYN-PWY, superpathway of thiamine diphosphate biosynthesis I | [YAML](../../../data/pathways/thiamine-diphosphate-biosynthesis-i.yaml) | [Dossier](thiamine-curation.md) |

Each dossier has a corresponding identifier ledger, source manifest, native
source projection, duplicate-search receipt and exact-source replay. Raw source
bodies are retained outside the repository; their local paths, hashes, retrieval
URLs and access limitations are provenance records, not published download links.
The independent review bundles under `reviews/structured/` preserve the scientific
judgements and the exact inputs reviewed.

The thiamine review found a supported zinc structural-role claim attached to a
UniProt cofactor locator that did not contain that interpretation.
[Issue 338](https://github.com/CultureBotAI/PathwayMech/issues/338) tracks its
reattribution to the primary paper's Results, “ThiF active site” section and verification of the fix.

The [baseline](baseline.json) records the starting state, and
[coverage hints](current-coverage-hints.json) retain bounded candidate screening.
Searches included hidden and ignored files in the accessible worktree, except
Git internals and the virtual environment. The original Documents checkout
remained OS-inaccessible, so no absence claim covers its ignored files.

The three iModulonDB projections retain computational expression context only.
The Pur module investigation concerns precursor reactions outside the selected
thiamine boundary. The homogentisate module concerns KT2440 and is not direct
evidence for strain U. Runner availability and canonical-parser replay receipts
document the fallback used.

Nicotine degradation II (MetaCyc:PWY-6993) remains follow-up research, with a
[bounded initial search](nicotine-initial-duplicate-search.json). No nicotine
record is included in this cohort. Its complete eleven-step boundary includes
spontaneous hydration and the succinate-semialdehyde branch. Later NicA2/Pnao
electron-transfer work requires checking the exact S16 CycN sequence and carrier
states before curation; downstream cytochrome reoxidation must not be inferred.
Source discovery is still in progress; this cohort does not establish exhaustion.
