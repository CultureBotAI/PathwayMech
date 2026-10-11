# Two reviewed pathway networks and one withheld candidate

This cohort extends the 201-record baseline at
`9e936b267374181f7f87402045777534d2f17508` with two microbial pathways
and their generated network pages, bringing the published catalog to 203 records.

| Record | Native boundary | Representation limits |
| --- | --- | --- |
| MetaCyc:PWY-7446 — sulfoquinovose degradation I | Four transformations from free sulfoquinovose to DHAP and DHPS | E. coli findings remain separate from Salmonella kinetic and solution-assembly measurements. Chemical stereochemistry and conflicting historical wording are documented. |
| MetaCyc:PWY0-1277 — 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation | Eight reactions across both entry branches and their common route to succinate, pyruvate and acetyl-CoA | HcaB assignment remains putative where the primary source did not demonstrate its activity separately. Direct W3110 MhpA experiments support activity and FAD binding; its apparent polymer mass does not establish a fixed subunit count. Exact chemical classes remain distinct. |

The full nine-step staphyloxanthin candidate is retained at
`withheld/staphyloxanthin-biosynthesis.yaml` and excluded from the published catalog,
pages and KGX. Independent review found three conflicting presqualene diphosphate
stereochemical encodings in native MetaCyc CPD-465, current ChEBI:57310 and RCSB PS7.
The structural study used human-SQS-prepared ligand soaked into CrtM, so it does
not establish an exact Newman-produced stereochemical bridge. No replacement
structure is inferred. [Issue #369](https://github.com/CultureBotAI/PathwayMech/issues/369)
remains open; `deferred-records.json` records the unchanged draft and disposition.

Each source dossier records the full native boundary, identifier decisions,
source projections and replay checks against original retained bodies. Original
source bodies remain outside the repository. The Tao 2020 AldH paper was
inspected through its primary web PDF; it has no invented local-body checksum.

`authority-integration.json` records canonical extraction from original inputs
and preservation of every existing authority term and source metadata entry.
The snapshots retain the previously approved Rhea142 equation updates.

iModulonDB supplies computational expression context only. The canonical runner
was unavailable, so its unchanged parser module was used on retained original
responses. The staph_precise165 adapter rejected null metadata and an unrelated
gene row with no organism. Those failures are preserved and reproduced; a
bounded inspection of the native objects records four selected crt genes without
imputing values or claiming a complete adapter pass.

The scientific reviews, local gates, generated SVG/KGX audit and baseline
preservation checks have separate scopes. Structural checks do not establish
scientific correctness. Review findings and dispositions are indexed in
`review-index.json`. A provenance-only resolution of the withheld draft's locator
fix is not a scientific approval of its stereochemical grounding.

The adversarial review identified three groups of evidence-locator defects
([#365](https://github.com/CultureBotAI/PathwayMech/issues/365),
[#366](https://github.com/CultureBotAI/PathwayMech/issues/366),
[#368](https://github.com/CultureBotAI/PathwayMech/issues/368)) and an omitted
direct MhpA characterization
([#367](https://github.com/CultureBotAI/PathwayMech/issues/367)). Initial review
bundles and their exact input bytes are retained alongside successor dispositions.

Discovery scouts retain additional candidates, including methylthiopropanoate
degradation, ergothioneine synthesis, sulfo-ED and siderophore routes. Broader
source screens remain incomplete. This cohort does not establish source exhaustion.
