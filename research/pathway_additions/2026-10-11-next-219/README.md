# Complete nitrate reduction I (denitrification)

This addition represents **MetaCyc:DENITRIFICATION-PWY**, nitrate reduction I
(denitrification), with PAO1 protein and experimental context. The selected native
boundary has five reaction objects, including nitrate/nitrite exchange. The
broader GO:0019333 process and the alternative-rich KEGG:M00529 module are not
asserted to be exact equivalents.

The corrected record contains five reactions, 39 participants, 75 mechanistic
edges, 156 evidence blocks and 73 references. Its SHA-256 is
`7c5b3ca9714dd9968901921b54bb82f44b08f85da322cb5527453ac685568ecd`.
The native equations retain compartment-specific protons and waters, generic
whole-carrier states, and the distinction between cytochrome c551 and generic
c-type cytochrome. Formal balancing does not establish measured flux, transport
stoichiometry, energetic coupling or ATP yield.

## Scientific scope

The original full-record review inspected all five native members and the entire
edge/evidence population. Two minor findings became
[issue #407](https://github.com/CultureBotAI/PathwayMech/issues/407). The corrected
successor expands the Anr motif-mutation source locator to include both relevant
paragraphs, and changes NarK1 localization to the supported generic membrane
term GO:0016020. It retains ARBA/IEA inference and adds exact GO identity evidence.
Independent reassessment confirms the eight changed fields and unchanged
reaction chemistry and other 73 edges. Both external findings are resolved in
the corrected maintained record. The original findings and verified corrections
remain separate evidence for the canonical review and GitHub issue closure.

Material limitations remain explicit:

- NarK2 physiology does not resolve antiport versus uniport. The native exchange
  object has no asserted exact PAO1 catalyst.
- Native protein-complex identifiers from other species are not transferred to
  PAO1. Subunit participation does not imply isolated-subunit catalysis.
- Cofactor, assembly and localization annotations retain their evidence tiers.
  The inferred NorB proton-pump assertion conflicts with the inspected cNOR
  structural evidence and is excluded.
- PDB 3O0R differs from current NorB/NorC sequences; antibody Fab entities do not
  become physiological NOR subunits. Historical preparation identity is retained.
- The 2010 Science main article was inspected through the web, with its indexed
  abstract and original structure files retained locally. No local full-main-text
  digest or fresh complete article acquisition is claimed.
- iModulonDB observations remain computational expression context, including
  preserved precise411 parser errors. They do not establish catalysis or flux.

## Evidence preservation and replay

The dossier preserves original author evidence, the full independent review,
the corrected successor, its independent reassessment, root acceptance receipts
and current duplicate searches as distinct records. Historical scripts are inert
text; whitespace-sensitive and fixture artifacts use lossless JSON wrappers.
Content-addressed aliases preserve exact historical bytes without installing
filesystem links or rewriting old findings. No external review is relabelled as
a canonical predecessor.

The active `denitrification-replay.py` has SHA-256
`70387ce2410f5582ce1f5a9073ec37ed723caf0789eac75445df6c37f0422d5e`.
The prior `4b5a7559…` helper remains byte-exact in
`external-evidence/helper-formatting/denitrification-replay-original.py.txt`.
[Issue #409](https://github.com/CultureBotAI/PathwayMech/issues/409) records the
lint correction. Complete executable ASTs agree after two explicit variable
renames; guarded import order is preserved. Historical packaging references
continue to identify the original bytes, with their successor mapping recorded
separately. Independent reassessment confirmed this limited equivalence.

It retains explicit original external dependencies: source bodies, iMod metadata
and responses, predecessor proofs, issuing databases and the selected runtime.
Archived copies alone do not make the helper portable. Full source bodies and
databases remain outside the repository; packaging does not establish licensing
clearance for public redistribution.

Current duplicate searches included ignored and hidden files and followed
relevant symlinks. Historical research mentions, broader DRAM definitions,
SEED menus and a terminal NosZ lead were adjudicated; they do not constitute an
existing complete maintained record. This is a bounded absence result, not
source exhaustion.

The working branch is based on the actual Entner–Doudoroff merge
`ae9279447c78b868289f24a847efe06efce2e167`, whose tree equals the reviewed ED head.
Canonical production authority builders added 25 source entries and 11 ChEBI
terms while preserving prior entries and metadata. Original scientific sources
(three SQL databases plus Rhea 142 RDF) remain distinct from production
authorities (597 source bodies and four SQL databases, including Rhea 139).

The initial complete gates passed: rendering, validation, lint, KGX export,
tracked whitespace, and 1,256 tests with three skips. The independent graph
audit checked all 75 edges, 156 evidence blocks and 73 references, with 46 KGX
nodes and 45 SVG nodes; the isolated PAO1 taxon is omitted only from the SVG.
All 219 prior records, pages and graph contexts were preserved. The original
three history entries retain their mistaken scaffolder-default actor name; an
append-only Codex attribution correction identifies each original entry.

The integration wrapper has an independent bounded technical review with no
actionable findings. Its 65 author guard checks and three independent mutation
checks are distinct from the actual source replay. The wrapper binds current
runtime, corpus, authority, original-source and retained proof inputs. Mutable
history, pages and the canonical scientific review have separate checks.

Completed technical and preassessment evidence is archived under
`external-evidence/current-integration-checks/`; original and successor wrapper
preparations are under `external-evidence/integration-preparations/`. The final
attribution-history validation and actual integrated replay passed and are
preserved under `external-evidence/final-integration/`. The integrated run
rechecked 2,652 bound inputs and completed the source helper, current corpus
identifier and native-schema checks, and the target's strict-schema check.
The source helper verified all five native objects, 29 stoichiometric sides,
five formal balances and the retained correction guards. Its web-only primary
passage remains outside byte replay.

The post-history graph audit again preserved all baseline records and graph
contexts. A separate final reassessment verified the completed checks and
current bindings without duplicating or relabelling the source replay as an
independent scientific experiment. Canonical scientific review and remote PR
review retain their own reviewed-input records.
