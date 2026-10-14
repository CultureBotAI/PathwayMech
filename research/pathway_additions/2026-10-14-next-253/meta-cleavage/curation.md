# Pathway mechanism research: protocatechuate meta-cleavage

## Pathway scope

This is a research checkpoint for **MetaCyc:P184-PWY**, protocatechuate
degradation I (meta-cleavage pathway). It does not add a curated pathway record.
The baseline is commit `d2ac9ebc5595f1208e4ffc8863fc7d44aed7907b`, containing
250 pathway records. Candidate discovery remains active.

The inspected META 27.0 definition has eight reaction members, including
spontaneous cyclization and terminal oxaloacetate decarboxylation. The native
pathway combines evidence from several organisms. It cannot be treated as a
complete experimentally demonstrated route in every listed organism.
GO:0019617 ends at oxaloacetate and pyruvate, so it is narrower than this native
boundary. Retaining the MetaCyc identity does not resolve the organism-specific
mechanism questions below.

## Mechanistic summary

The native scheme proceeds through ring cleavage, cyclization, oxidation,
hydrolysis, tautomerization, hydration, aldol cleavage, and oxaloacetate
decarboxylation. Reaction layouts and full equations must be read together:
RXN-2463 is selected right-to-left in the pathway.

The downstream enzyme assignments need further reconciliation. Experiments on
the Pseudomonas putida gallate route establish shared chemistry under their own
conditions; they do not by themselves establish a complete protocatechuate route
in that strain. Later LigU/LigJ evidence distinguishes intermediate identities
and protein scope. A recombinant-protein qualifier cannot repair an incorrect
substrate or species assignment.

## Evidence table

| Evidence surface | Supported use | Limit |
| --- | --- | --- |
| META 27.0 P184-PWY and its native reaction objects | Native membership, order, source orientation, and database scope | Database membership is not a same-strain experimental reconstruction |
| GO:0019617 definition | Boundary comparison | Does not include the native terminal decarboxylation |
| Native, ChEBI, and Rhea chemical projections | Exact structures, equations, directions, and cross-reference checks | Chemical equality does not establish enzyme specificity |
| Inspected primary literature and protein authorities | Source-specific mechanistic constraints and research priorities | Preserve full-text versus abstract-only access and exact assay/organism scope |

The [preflight](preflight/HANDOFF.md), [native chemistry](native/HANDOFF.md),
and [primary evidence](primary/HANDOFF.md) handoffs accompany this report. Their
retention manifests bind exact source-analysis bytes. Full articles, figures,
XML/JSON downloads, SQL, and RDF remain in external caches.

All eight native equations balance atoms and charge. Seven selected equations
have exact Rhea matches; R107-RXN retains its native identity. The obsolete
RHEA:10889 cross-reference is replaced in the analysis by RHEA:29588 after
checking complete equations. Historical Rhea display names do not establish a
structure error: the native structured E,E enol and its Rhea counterpart match.
The distinct enol linked in native GalD/GalB prose remains a separate question.

The protein authority projection identifies Q0KJL4 as a KA1 protein and maps
the older Q9KWL6 accession to SYK-6 LigJ G2IQQ5. This does not establish the
identity of a paper's assayed construct. The 2016 comparison tested Comamonas E6
LigJ; its results must retain that scope. The primary ledger distinguishes
complete main-article reading from abstract-only or inaccessible sources, and
discloses one superseded acquisition whose original bytes were not preserved.

## Gaps

Before adding a graph, resolve the exact intermediate and protein identities for
each proposed organism-specific downstream edge; inspect the decisive newer
full papers and assay constructs where access remains incomplete; and distinguish
experimentally supported route variants from native database membership.
Do not map a modern protein onto an older reaction solely through a shared name.
The [continuation requirements](primary/continuation-requirements.json) identify
the exact source, chemical, construct, and kinetic-provenance questions.
[Issue #534](https://github.com/CultureBotAI/PathwayMech/issues/534) tracks this
scientific continuation and remains open after the research checkpoint merges.

The preflight records the duplicate-search bounds, including ignored and hidden
files, all 250 baseline records, and the configured source-family inventory.
This is a bounded candidate audit, not proof that all pathway sources are
exhausted. Quinate and shikimate degradation remain separate leads.

## Candidate YAML

No candidate YAML is promoted in this checkpoint. A later addition must first
close the source-to-graph and graph-to-source mappings, independently establish
every identifier, and pass the normal record, authority, page, and review gates.
The current PR preserves research progress without making new graph claims.
