# Pathway mechanism research: protocatechuate ortho cleavage

## Pathway scope

GO:0019618, protocatechuate catabolic process, ortho-cleavage, denotes the
complete four-reaction conversion of protocatechuate to 3-oxoadipate. The pinned
GO definition and input/output restrictions agree with the complete native
MetaCyc PROTOCATECHUATE-ORTHO-CLEAVAGE-PWY object. The catechol branch,
alternative protocatechuate cleavage routes, and terminal CoA-transfer and
thiolysis module remain separate. PWY-2361 is retained only as a downstream
pathway interface.

The preflight inventories all 247 baseline pathway YAMLs and searches exact
identifiers, labels, reaction identifiers and source accessions in both the
worktree and original repository, including hidden and ignored files. Git
metadata, virtual environments and binary archives are bounded exclusions;
symlink directories are not recursively followed. Prior research mentions are
leads, not an existing pathway record or a reason to claim source exhaustion.

## Mechanistic summary

The route performs ring cleavage, cycloisomerization, decarboxylation and
enol-lactone hydrolysis. Its three material intermediates are
3-carboxy-cis,cis-muconate, the stereospecific R carboxymuconolactone, and
3-oxoadipate enol-lactone. Complete formal chemical sides include dioxygen,
water, carbon dioxide and hydrons. Each equation balances atoms and charge.
The cycloisomerase retains its native right-to-left orientation; the remaining
three native pathway traversals are left to right.

MetaCyc:5.5.1.2-RXN cross-references RHEA:23658, whose lactone has unspecified
stereochemistry. The native product instead matches CHEBI:58771 with a defined
R stereocenter. Complete Rhea 142 reverse traversal from that exact chemical
finds only the decarboxylation reaction family. The graph therefore preserves
the exact native cycloisomerase identifier and documents the rejected exact
mapping. No pathway step or stereocenter is discarded to obtain a convenient
Rhea match.

Canonical ChEBI labels and pinned Rhea 139 equation labels remain distinct from
Rhea 142 chemical evidence. Full native InChIs, formal charges, formulas and
original CML connectivity were checked against ChEBI. Several native SMILES
fields contain incomplete placeholders. The pinned CHEBI:57496 SMILES also
omits double-bond stereochemistry, while its pinned InChI and current issuing
ChEBI structure agree with the native cis,cis identity. These representation
limits remain explicit in the chemistry ledger.

## Evidence table

| Source | Supported assertion | Boundary retained |
| --- | --- | --- |
| Pinned GO term and complete META 27.0 pathway | Exact four-step biological process, native order and downstream interface | Pathway layout primaries are not complete equations |
| Complete native reaction and chemical objects; Rhea 142 RDF; ChEBI 255 and current issuing structures | Complete chemical sides, stereochemistry, formal charge and selected traversal | Native cycloisomerase cross-reference is not an exact stereochemical mapping |
| Native enzyme, complex and subunit objects | Pseudomonas putida catalytic machinery, assembly annotations, ferric cofactor and reported induction | Historical preparation scopes and source evidence codes are retained |
| Primary studies assessed in the primary evidence ledger | Experimental context, preparation differences and limits of regulatory interpretation | Full scans, partial text and metadata-only access are distinguished |
| iModulonDB P. putida KT2440 precise321 PcaR component 65 | Computational expression context for modern KT2440 genes | Membership does not establish direct regulation, historical sequence identity or pathway chemistry |

## Gaps

The native pathway carries two unrelated literature pointers, PMID:761399 and
PMID:916393. Both are rejected without guessing replacement identifiers.

The native PcaHG complex combines discussion of distinct preparations. Its
four-alpha/four-beta annotation refers to the historical PHK enzyme; the
ATCC23975 enzyme was reported as twelve-alpha/twelve-beta. Structural iron
sites do not establish full iron occupancy. The graph preserves native
component identity and qualifies historical assembly claims rather than
replacing them with modern homologs.

The historical PcaD trimer interpretation is not an assertion that three
263-residue KT2440 Q88N36 proteins were measured. The existing native identities
retain that distinction. Induction means an expression-level response and
does not imply direct metabolite binding or catalytic activation. No generic
compartment, unsupported physiological cofactor, or engineered salicylate
induction is inferred.

The authority policy adds a reaction-only contextual-label rule for native
MetaCyc reactions inside exact GO biological-process records. The rule still
requires independent reaction identity and does not weaken canonical pathway,
chemical, taxon or protein names. Original scientific downloads remain outside
the repository. Public-release licensing remains deferred as requested.

## Proposed record updates

Create `data/pathways/protocatechuate-ortho-cleavage.yaml`, generate its graph
and evidence page, preserve all baseline records and authority owners, and
retain compact provenance and chemistry projections. Validate the complete
corpus, save independent scientific review, and inspect generated graph and
KGX evidence before the authorized PR and merge workflow.
