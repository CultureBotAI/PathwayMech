# Citrate activation and succinate-to-propanoate curation

This batch adds two pathway records to the 165-record baseline at
`722257adc1882495f8454cc229b8fa0c187cf868`.

| Record | Supported scope | Reactions | Edges |
| --- | --- | ---: | ---: |
| `MetaCyc:P2-PWY`, citrate lyase activation | CitG precursor synthesis, CitX carrier modification and CitC acetylation | 3 | 22 |
| `MetaCyc:PWY0-43`, conversion of succinate to propanoate | Proposed Sbm/ScpABC biochemical cycle with explicit stereochemistry and physiological limits | 3 | 22 |

The citrate graph distinguishes the generic apo, holo and acetylated carrier
states from an exact protein sequence and from reactive chemical residues.
CitG and CitX have direct experimental evidence. The CitC assignment retains
the explicit curated experimental bridge to the older ligase assay, whose
full text was unavailable. No unsupported assembly, bound metal or alternative
taxon branch is added. [Citrate curation](citrate-curation.md) records these
decisions and source limits.

The Sbm graph represents the native mutase dimer and decarboxylase hexamer,
the adenosylcobalamin cofactor and the three annotated reactions. It preserves
the disagreement between current Rhea/UniProt stereochemistry and later
engineered-strain epimerase requirements. The 2019 primary supplement uses
an R/S substrate mixture and does not resolve the disagreement. The record
does not establish wild-type pathway flux or invent a native epimerase.
[Sbm curation](sbm-curation.md) documents the experiments and exclusions.

[Issue #324](https://github.com/CultureBotAI/PathwayMech/issues/324) tracks the
independent review finding that the apo-Sbm oligomer evidence pointed to the
wrong figure. Its acceptance requires the corrected primary-source locator
to survive YAML, generated page and KGX export.

The [combined identifier ledger](record-identifiers.json), per-record source
manifests and source projections retain exact identities, source versions and
body hashes. [Authority integration](authority-integration.json) adds 14
ontology terms and 13 source identifiers while preserving all 1,305 baseline
ontology terms, 1,609 source terms and existing source metadata. Four new native
MetaCyc HTML inputs ground the pathway and assembly names. Duplicate searches
included hidden and ignored files in the original repository and worktree,
excluding Git internals, virtual environments and bytecode.
[iModulonDB lookups](imodulondb-context.json) returned each of the six exact
genes and no module-name hits. This is expression-context discovery, not
evidence of pathway flux or absence from all expression modules.

The [generated SVG/KGX audit](generated-graph-kgx-audit.md) verifies all 44 new
edges and 74 evidence blocks, the corrected issue #324 locator, and equality
with a separate CLI export. The [integration review](integration-review.json)
checks preservation of all 7,575 baseline edges and prior node contexts.
No browser surface was available; these are structural checks, not visual
browser inspection. Sbm's author performed the integration audit; a separate
reviewer assesses its scientific evidence.

The immutable independent scientific reviews for
[citrate](../../../reviews/structured/20261010T231224Z-citrate-independent-review/review.md)
and [Sbm](../../../reviews/structured/20261010T231218Z-sbm-independent-review/review.md)
both pass with explicit source limitations and no unresolved findings. Each
Markdown report has an authoritative sibling `review.yaml`. Sbm's review
preserves the initial issue #324 finding and its independently checked fix.
[Final verification](verification.json) records actual successful full-corpus
validation, 1,043 passing tests with three skips, lint, governed-file integrity
and all 11 immutable reviews. The [staged audit](staged-review.json) records
the independently reviewed integration snapshot before these final review
bundles and verification documents were added.

[Allantoin follow-up](allantoin-handoff.md) resolves several additional
chemistry and assembly questions, but its AllFGH complex still needs a
verified external identity. That candidate is not a record in this batch.
The frozen 528-row archive screening ledger is unchanged, and additional
pathway candidates remain. Raw source bodies stay in the external evidence
cache; data licensing for public release remains deferred under the user's
standing instruction.
