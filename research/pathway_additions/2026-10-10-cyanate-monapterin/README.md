# Cyanate and tetrahydromonapterin pathway curation

This batch adds two independently grounded pathways to the 163-record baseline
at `b02726e03fd7e67d210057f150e029fcb343b928`.

| Record | Supported scope | Reactions | Edges |
| --- | --- | ---: | ---: |
| `MetaCyc:CYANCAT-PWY`, cyanate degradation | CynS conversion to carbamate, spontaneous decay, and conditional CynT bicarbonate recycling | 3 | 26 |
| `MetaCyc:PWY0-1433`, tetrahydromonapterin biosynthesis | FolE/FolX synthesis and FolM reduction, with the unresolved intervening dephosphorylation explicitly excluded | 3 | 24 |

The monapterin record describes an established pathway with an incomplete known
mechanism. It does not assign a phosphatase, assert the source's hypothetical
net reaction, or connect FolX to FolM through an invented edge. The full primary
FolX/FolM paper and later phosphatase studies were inspected. Their organisms,
substrates and experimental limits remain distinct. MG1655 pterin profiling
and JP2255 complementation support different claims within the K-12 scope.

The cyanate record retains the explicit intermediate chemistry instead of
double-counting the net cyanase reaction. It distinguishes native MG1655
annotation from K-12 physiology experiments, preserves the CO2 condition and
CynT oligomer uncertainty, and rejects the archived mixed CynT/Can complex.
[Issue #322](https://github.com/CultureBotAI/PathwayMech/issues/322) records the
corrected draft category on spontaneous carbamate decay. The reaction remains
complete and has no invented enzyme assignment.

[Cyanate curation](cyanate-curation.md) and
[monapterin curation](monapterin-curation.md) document the source-to-graph
decisions, primary evidence, historical conflicts and exclusions. Their
[combined identifier ledger](record-identifiers.json) lists every named node
and reference, including exact URLs, versions and hashes. Duplicate searches
included ignored and hidden files in
the original repository and worktree, excluding Git internals, virtual
environments and bytecode. Existing shared reactions and earlier research
mentions were examined rather than treated as pathway equivalence.

[Authority integration](authority-integration.json) preserves every baseline
term and source assertion. Six native MetaCyc HTML inputs establish the two
pathways and four complexes; independently acquired reviewed UniProt data
already cover the five proteins. The canonical builders rehashed their full
inputs. The snapshots add 12 ontology terms and 11 source identifiers without
removing or changing existing entries. Rhea142 chemical evidence and Rhea139
label authority remain explicitly versioned. No schema or policy waiver was
introduced.

Separate immutable scientific reviews assess each entire record: [cyanate](../../../reviews/structured/20261010T224258Z-cyanate-independent-review/review.md)
and [monapterin](../../../reviews/structured/20261010T224232Z-monapterin-independent-review/review.md),
each paired with authoritative YAML. The [batch verification](verification.json)
and [generated SVG/KGX audit](generated-graph-kgx-audit.md) retain actual gate
outcomes, exact target hashes and all 96 evidence blocks. No browser surface was available;
the generated-graph audit is structural, not a visual browser inspection.
[iModulonDB lookups](imodulondb-context.json) provide gene-level context only;
the three searches returned no module-name hits and do not establish absence
of membership in all expression modules.

[The next-candidate handoff](next-handoff.md) identifies citrate lyase
activation, anaerobic allantoin degradation through oxamate, and a qualified
succinate-to-propanoate cycle. The frozen 528-row archive screening ledger is
unchanged. These remain research leads requiring full curation and independent
review; the source landscape is not exhausted. Raw source bodies remain in
the external evidence cache, with data licensing for public release deferred
under the user's standing instruction.
