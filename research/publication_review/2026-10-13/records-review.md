# Cumulative record/export review — 2026-10-13

Scope: checkout `/private/tmp/pathwaymech-next-243-local-20261012`, public baseline `e1c66917e753105c4bf5b7b026193fcefa2b000f`, reviewed HEAD `70903536191206d2586cd23e46f7d70c32fef92e`. Independent review of nine new records, two DFO carrier-label changes, saved review summaries/limitations, and cumulative record/export representations. Initial work was read-only; root subsequently assigned the SSSOM correction separately.

## Finding P2 — 52 new SSSOM mappings cannot expand their identifiers

Location: `output/sssom/source_mappings.sssom.tsv:4` (incomplete `curie_map`; first affected row at line 17), owner `src/pathwaymech/sssom.py:13` (`CURIE_MAP`) and `:112` (`_validate_row`).

The old hard-coded prefix map omits EcoCyc, MetaCyc and PathBank. All 12 baseline mapping rows have declared prefixes, but 52 of the 58 added rows introduce undeclared prefixes: EcoCyc 5, MetaCyc 45, PathBank 2. The installed SSSOM parser accepts all 70 rows, but its converter returns `None` for each affected identifier. Its normal prefix-cleaning operation raises `ValueError` because these prefixes are missing. Existing tests only parse a one-row UniProt fixture and check that export regeneration is current, so they miss this concrete consumer failure.

Reproduction (with the shared PathwayMech virtualenv):

```python
from pathlib import Path
from sssom.parsers import parse_sssom_table
m = parse_sssom_table(Path('output/sssom/source_mappings.sssom.tsv'))
assert len(m.df) == 70
assert m.converter.expand('MetaCyc:NADPH') is None
m.clean_prefix_map()  # ValueError: {'PathBank', 'MetaCyc', 'EcoCyc'} ... not ... prefix map
```

Recommendation: add semantically correct URI expansions, reject undeclared prefixes when exporting, regenerate the header while retaining every mapping row, and exercise prefix cleaning/expansion against the complete generated corpus. PathBank scoped local objects must remain distinguishable from registered upstream pathway accessions. This is separate from the earlier stale-SSSOM regeneration defect: the current file is freshly generated but its metadata is incomplete.

## Other results

- All 11,689 baseline KGX edges are retained exactly; 436 added edges correspond to the nine new records.
- Compared all 486 edges from the ten changed records (including DFO's 50 unchanged edges), their complete evidence arrays, cited-reference metadata, descriptions and 49 endpoint qualifiers with KGX. No discrepancies.
- Each changed page has exactly one SVG edge link per maintained edge. Complete edge descriptions, evidence text and qualifier descriptions are present in the rendered DOM. This is structural/text QA, not a new visual/browser review.
- `pages/downloads/{nodes,edges}.tsv` are byte-identical to KGX, and both download-manifest hashes match.
- The only old per-record node contexts replaced are DFO's two intended carrier labels. Other shared-node changes preserve per-record contexts. The new RHEA:21038 direction disagrees with two existing records and clears the aggregate direction; the saved aceto review accepted this as a disagreement. This reviewer escalated its source-orientation basis for separate adjudication rather than silently treating it as proven correct.
- All 18 saved review bindings to the changed record YAML files match their current hashes. Saved reviews explicitly limit primary access, inherited interpretation, assay/strain scope and static graphics. No new primary-paper reading is claimed here.

Limits: no broad test suite, authority-builder rerun, SQL rehash, full historical dossier reread, fresh primary literature audit, licensing assessment or interactive browser QA. Searches establishing absence (AGENTS.md and undeclared-prefix definitions) included ignored and hidden files within their named scope. Source-level scientific interpretation was assessed from the current records and saved judgments, not independently rederived from every original paper. Production runtime review is assigned separately.

## Assigned correction and focused verification

Root assigned correction after review and opened [issue #505](https://github.com/CultureBotAI/PathwayMech/issues/505). Modified only `src/pathwaymech/sssom.py`, `tests/test_sssom_export.py`, `docs/HARMONIZATION.md` and generated `output/sssom/source_mappings.sssom.tsv`; no Git/remote action by this reviewer.

- Added EcoCyc's native frame URL prefix and MetaCyc's generic frame URL prefix. EcoCyc agrees with existing `src/pathwaymech/cli.py` and the [EcoCyc registry provider](https://bioregistry.io/registry/ecocyc). MetaCyc's type-neutral `/META/NEW-IMAGE?object=` form occurs in retained native source fixtures (for example `tests/fixtures/nitrate_authority/META-Menaquinols.xml`); a compound-only registry expansion would misrepresent mapped protein monomers.
- [PathBank's registry grammar](https://bioregistry.io/registry/pathbank) only covers `(SMP|PW)` followed by digits. The actual new mapping subjects contain pathway-scoped `/Compound/...` suffixes. Their expansion therefore uses the explicitly documented project namespace `https://w3id.org/culturebotai/pathwaymech/pathbank/`; it preserves the complete source scope without claiming an upstream accession or live resolver. Existing CURIEs are unchanged.
- Prefix validation now covers subject, object, predicate and justification before opening/replacing the output. Regression cases show that any undeclared prefix fails and preserves an existing export.
- The regenerated TSV differs from reviewed HEAD only by three prefix declarations. All 70 mapping rows and column-header bytes remain exact. Final SHA-256: `f58b7a07ac6630c37d4df2e509b0e6ab96ee9c9a47b1d23ec10b3acd74c83efa`.
- Focused `PYTHONPATH=src .../.venv/bin/python -m pytest -q tests/test_sssom_export.py`: **15 passed, 7 warnings, 37.16 s**. Environment was `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech/.venv`; warnings were installed LinkML deprecation and pandas/SSSOM deprecations.
- Independent actual-file consumer check: 70 rows before and after strict prefix cleaning; all 280 subject/object/predicate/justification CURIE expansions resolve; complete data bytes match reviewed HEAD.
- Focused ruff and changed-file `git diff --check` passed. Full gates and independent correction review remain root-owned. The RHEA:21038 source-orientation question remains separately assigned to root; no aceto record edits were made here.

## Source-direction follow-up

The previously escalated RHEA:21038 question was independently confirmed from the retained original RDF and corrected at `data/pathways/acetoacetate-degradation.yaml:322`. See `/private/tmp/pathwaymech-publish243-rhea-direction-review-20261013.md` and its JSON proof. It was a concrete source-orientation defect, not a legitimate disagreement between source contexts. This updates the unresolved status above without rewriting the earlier inspection history.
