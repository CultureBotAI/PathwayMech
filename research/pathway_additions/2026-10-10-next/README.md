# Riboneogenesis and methylglyoxal degradation III

This batch adds two independently reviewable pathways from the next-source
screen, with their generated network pages and KGX evidence. The maintained
baseline was `dbf399e6ac90f6240fa5da2fac27386d49966171` (167 records).

| Record | Mechanism and retained limits |
| --- | --- |
| [PathBank:SMP0002406](../../../data/pathways/riboneogenesis.yaml) | Six-reaction yeast riboneogenesis, with Shb17-driven pentose formation, functional protein roles and explicit cofactor/assembly limits. The native Tkl1–Tkl2 heteromer is rejected. |
| [MetaCyc:PWY-5453](../../../data/pathways/methylglyoxal-degradation-iii.yaml) | Two-reaction E. coli acetol branch, preserving distinct NADPH/NADH usage, GldA complex membership and the distinction between annotated S product and the inspected assays' stereochemical limits. |

The `riboneogenesis-*` and `methylglyoxal-*` files preserve native projections,
source manifests, exact identifier checks, ignored-inclusive duplicate searches,
chemical balances, primary-source limits and author verification. Full raw
downloads remain outside the repository. Independent review findings and their
dispositions are saved under `reviews/structured/`; those reviews are distinct
from the author checks.

Independent review found three incorrect riboneogenesis source-direction fields.
[Issue #326](https://github.com/CultureBotAI/PathwayMech/issues/326) tracks the
correction of RHEA:27628, RHEA:13679 and RHEA:14659 to `right_to_left`.
Their chemical edges were already correct and remain unchanged. The correction
has its own append-only history event.

Independent integration review also found that the taxonomy audit read its
14 GB authority database into memory to compute a digest.
[Issue #327](https://github.com/CultureBotAI/PathwayMech/issues/327) tracks the
fix to stream 1 MiB blocks. The interrupted attempts and final replay outcomes
are retained separately; the hashing change does not alter scientific results.

## Archive inventory and remaining coverage

The existing name-based helper replayed all 2,687 archived OWL members against
the 167-record baseline. Its 528 named-microbial rows retain the same member
hashes, identities, titles, counts and screening classes as the earlier frozen
ledger. Thirteen exact-match hints changed following recent additions; a title
match across taxa is not proof of a duplicate pathway. See `screening-replay.json`
and `current-screening/`. This is a baseline inventory, not a post-addition
coverage declaration.

`audit_pathbank_taxa.py` supplements that screen using native BioSource taxonomy
xrefs and independently checked NCBI Taxonomy labels. It reports explicit
Pathway organism links separately from a microbial BioSource elsewhere in the
same document. Its complete enumerated taxon set is retained; the selected
microbial IDs are Bacteria, E. coli, P. aeruginosa and S. cerevisiae. Generic
names and tissue labels are not substituted for these native identifiers.

Four previously missed documents require explicit disposition. PW002336 and
PW002337 each contain one E. coli regulatory conversion; they do not establish
a complete multistep pathway by themselves. PW000345 is an azithromycin action
map with a human main pathway and a co-occurring bacterial BioSource. PW064816
is a human GnRH signaling map with a co-occurring yeast BioSource; its 45
molecular interactions must not be mistaken for an empty graph simply because
it has no BiochemicalReaction object. These are source-scope observations,
not claims that related microbial mechanisms cannot exist.

The [cobalamin handoff](cobalamin-handoff.md) remains research only. It preserves
the full salvage and activation route as pending and identifies PWY-5509 as a
separate native candidate. It does not substitute the smaller pathway for the
full route. The prior [allantoin handoff](../2026-10-10-citrate-sbm/allantoin-handoff.md)
also remains pending. Other sources and unreviewed candidates remain; this batch
does not establish pathway or source exhaustion.

## Integration verification

`authority-integration.json` records canonical snapshot rebuilding and verifies
that every baseline term, source metadata entry and manifest input is retained.
`generated-graph-kgx-audit.json` records the actual generated SVG and KGX checks,
including node identities, metadata, edge direction, evidence links and full
reference preservation. `verification.json` records terminal local gate results
and the final independent review bundles. Publication CI and merge integrity
are verified separately against the pushed and merged commits.
