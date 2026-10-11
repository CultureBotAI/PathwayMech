# Heme b biosynthesis IV: retain the complete route, defer its chemical graph

MetaCyc:PWY-7766 is a distinct, experimentally supported microbial pathway. Its
five-reaction native boundary is worth curating, but the inspected source states
do not yet support a complete, chemically faithful maintained record. No
`data/pathways/heme-b-biosynthesis-iv.yaml` was created. This is a specific
redox-state and representation blocker, not a duplicate disposition or a claim
that the pathway does not exist.

## Exact identity and native boundary

The inspected MetaCyc XML is version **22.5**, not an assertion about the latest
MetaCyc release. Its title is *heme b biosynthesis IV (Gram-positive bacteria)*.
It contains the following five reactions, ordered here by the biochemical route:

| Native member | Independently inspected Rhea direction | Transformation in the source |
| --- | --- | --- |
| UROGENDECARBOX-RXN | RHEA:19866, left_to_right | uroporphyrinogen III + 4 H+ → coproporphyrinogen III + 4 CO2 |
| RXN-17517 | RHEA:43437, left_to_right | coproporphyrinogen III + 3 O2 → coproporphyrin III + 3 H2O2 |
| RXN-17518 | RHEA:49574, right_to_left relative to master 49572 | coproporphyrin III + Fe2+ → Fe-coproporphyrin III + 2 H+ |
| RXN-19755 | RHEA:57941, left_to_right | Fe-coproporphyrin III + H2O2 + H+ → harderoheme III + CO2 + 2 H2O |
| RXN-19756 | RHEA:57945, left_to_right | harderoheme III + H2O2 + H+ → ferroheme b + CO2 + 2 H2O |

These are **source equations under investigation**, not accepted biological
assertions. RHEA:56517 is the net of the last two source equations; adding it as
another sequential step would double-count the chemistry. The independently
extracted RDF retains every chemical-side occurrence and its `rh:containsN`
coefficient. All five equations and the net equation balance for atoms and
charge. Balance does not establish their biological iron-state correctness.

PWY-5188 is an upstream pathway link, not a child member. The chosen native route
starts at uroporphyrinogen III; it does not require silently expanding into
5-aminolevulinate synthesis. GO:0006785 is broader, links five alternative
MetaCyc pathways by `skos:narrowMatch`, and defines heme B with Fe(II). It is not
an exact replacement for this route identifier.

The yeast aerobic heme record uses the protoporphyrinogen/protoporphyrin branch.
The tetrapyrrole record supplies the common precursor; the siroheme record makes
a different product. Their shared UroD step does not duplicate this complete
coproporphyrin-dependent route. Both repository searches included hidden and
ignored curation/source files; commands, excluded dependency directories,
matched paths and the initial pre-authoring search are retained in the dossier.

## The terminal iron-state conflict

The three inspected native compounds are not oxidation-state-neutral labels:
CPD-17070, CPD-21388 and PROTOHEME each encode iron `/q;+2` in their InChI.
The current pinned Rhea 142 equations use CHEBI:68438, CHEBI:142463 and
CHEBI:60344. ChEBI 255 records their respective charges as −4, −3 and −2 and
encodes Fe(II) in the structures. CHEBI:60344 is explicitly *ferroheme b(2-)*.
Renaming these nodes “ferric” would not change their chemical identity.

The full primary text of [PMID 27982566](https://pmc.ncbi.nlm.nih.gov/articles/PMC5368639/)
directly tests **Staphylococcus aureus**, not Bacillus subtilis. BioC passage
offset 4273 identifies the enzyme and the ferric pathway. Results offsets 20324–22035
separate iron oxidation from propionate decarboxylation; offsets 25935–27957
describe the ferric coproheme and ferric harderoheme reactions. Its conclusion
is explicit: “the coproheme decarboxylase yields ferric heme b.” Discussion
offset 46564 also distinguishes the iron-oxidation connection from subsequent
decarboxylation. This is evidence against exporting the database Fe(II)-only
chain as an unqualified general HemQ mechanism. It is not direct proof of every
B. subtilis reaction condition. The paper appeared online in 2016 and in the
2017 journal volume; both dates are retained in source metadata.

An independent [Listeria study, PMID 27758026](https://pmc.ncbi.nlm.nih.gov/articles/PMC5157759/)
supports ferric coproheme, ferric heme product, consecutive decarboxylations and
two H2O2 equivalents. Exact XML locations are Results
`febs13930-sec-0006`, stoichiometry `febs13930-sec-0008`, Discussion
`febs13930-sec-0009`, and sample preparation `febs13930-sec-0019`.
The latter explicitly distinguishes peroxide-generated ferric product from
ferrous samples made afterward with dithionite. Its homopentamer is a Listeria
assembly observation, not automatic B. subtilis assembly evidence.

## The newer B. subtilis evidence does not repair the source equations

[PMID 40850531](https://doi.org/10.1016/j.freeradbiomed.2025.08.046) studies
168-derived strains and recombinant ChdC, with free FMN and YkuN/YkuP as
alternative co-substrates. Main text §2.1 and §3.1 establish the knockout/growth
scope; §§3.2–3.4 describe low-oxygen and anaerobic conversion assays.
The oxygen-electrode setup could not achieve complete anaerobicity (§3.2).
The HPLC method omitted heme b (§3.3), whereas LC-MS and spectroscopy separately
supported product conversion. YkuN/YkuP reduction was assigned to semiquinone
formation (§3.4). The conclusion leaves the detailed FMN mechanism unresolved.
These results do not assign an Fe(II) product or validate a complete balanced
FMN replacement equation. No such equation or flavodoxin edge was invented.

This paper was inspected through overlapping indexed main-text extracts of the
author-uploaded article. Their hashes identify **serialized web-tool outputs**,
not original PDF/HTML bytes. The original PDF, figures and supplement were not
retrieved or visually inspected. Direct author-upload retrieval returned 403;
the publisher API returned bibliography only. These access limits remain material.

## Protein identities and remaining evidence limits

Fresh full UniProtKB 2026_03 entries identify B. subtilis 168 proteins HemE/P32395
(BSU10120), CpfC/P32396 (BSU10130), CgoX/P32397 (BSU10140), and ChdC/P39645
(BSU37670). Their exact comments, evidence codes and source locators are retained.
CgoX has directly annotated FAD and monomer evidence; CpfC has monomer evidence.
Native CPLX-9084 is the two-subunit UroD assembly. P39645 terminal catalytic
equations and intermediate specificity carry ECO:0000255/HAMAP inference,
whereas its pathway involvement also cites primary evidence. These different
grades must not be flattened into direct experimental proof.

The original pathway-discovery lead [PMID 25646457](https://doi.org/10.1073/pnas.1416285112)
supports investigating the route. Its abstract and structured citations were
inspected, but full paper/supplement acquisition failed here. The prior scout's
PMC HTML is a recaptcha response, and a fresh BioC HTTP 200 response is an error
body. Neither is full-text evidence. No whole-pathway experimental sufficiency,
universal Gram-positive occurrence, exclusive oxygen requirement, missing-gene
claim or unverified B. subtilis oligomer stoichiometry is asserted.

## Bounded identifier search and reopening criteria

Complete ChEBI 255 statement-value searches covered coproheme, coproporphyrin,
harderoheme, harderoporphyrin, ferric coproheme and ferriheme terms, including
labels, synonyms, definitions and annotations. Complete Rhea 142 RDF text-property
searches returned 26 matching description blocks; Rhea 139 SemanticSQL was also
queried. The exact native pathway, five member reactions, net lead, three iron
compounds and named enzyme frames were inspected. CHEBI:55376 supplies ferriheme
b(1-), but the inspected source set did not resolve corresponding ferric
coproheme and ferric harderoheme states. This is **not** a global absence claim
about every database, structure search or later release.

Reopen curation when all of the following are satisfied:

1. Resolve the relevant ferric and ferrous intermediate structures at an issuing
   authority, including protonation, charge and exact harderoheme isomer.
2. Ground a complete connected mechanism for a stated microbial/assay scope.
   Account explicitly for the Fe(II) insertion product, its oxidation if needed,
   and the terminal product; do not invent an unobserved reduction to ferroheme.
3. Use reaction identities that actually support those chemical states, or an
   independently reviewed representation of uncertainty whose machine-readable
   meaning does not assert the contradicted Fe(II)-only chain.
4. Preserve all five native pathway transformations and independently adjudicate
   source-versus-current differences. Do not publish only the first three steps
   under the full pathway name or add net and component reactions redundantly.
5. Complete primary/assembly review for the selected organism, recover any
   necessary main-text/supplement details, then run the required author and
   independent scientific reviews before maintained publication.

Raw evidence remains external under
`/private/tmp/pathwaymech-next-186-evidence/heme`. The source projection,
identifier ledger, manifest, dedup receipt and offline replay are the durable
handoff. No shared authorities, generated pages, history or maintained record
were changed by this task.
