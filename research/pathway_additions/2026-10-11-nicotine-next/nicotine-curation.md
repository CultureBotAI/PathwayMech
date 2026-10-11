# Complete nicotine degradation II in Pseudomonas putida S16

Selected record: `MetaCyc:PWY-6993`, nicotine degradation II (pyrrolidine pathway),
`data/pathways/nicotine-degradation-ii.yaml`. Author inspection used the complete
native MetaCyc 22.5 definition, all 11 reaction frames and their enzyme frames,
four primary full texts, current individual UniProt records, exact primary
sequence deposits, and Rhea 142. This is a complete named biochemical route with
explicit catalyst gaps, not a claim that every formal reaction has a purified
S16 enzyme assay. It does not cover the pyridine or hybrid nicotine routes.

## Scope and semantic deduplication

The accessible baseline is commit `e3bceba7613eb0525af3ff76ef32520201ae9f33`
with 180 records. `nicotine-dedup.json` records 22 exact and semantic searches
using hidden and ignored files, excluding Git metadata and the environment's
third-party dependencies. Existing nicotine follow-up notes were read before
authoring. The complete nicotine-specific route has no prior maintained record;
shared maleate/fumarate or succinate chemistry does not make it a duplicate.
The current draft and preserved research handoff account for expected hits.
The original Documents checkout is OS-inaccessible and was not searched or
claimed to have been searched. No source-exhaustion claim is made.

The exact biological scope is `NCBITaxon:1042876`, Pseudomonas putida S16.
The route begins with (S)-nicotine and ends with fumarate and succinate, releasing
methylamine, ammonium and formate. CycN reoxidation, transport, coproduct
assimilation, and subsequent central metabolism are outside this native route.

## All eleven native reactions

| Native reaction | Current graph reaction | Catalyst or retained limit |
|---|---|---|
| RXN-13076 | RHEA:73656, master 73655 | NicA2 F8G0P2; physiological CycN acceptor |
| RXN-13077 | RHEA:75416, master 75415 | Spontaneous N-methylmyosmine hydration; no catalyst/activity category |
| RXN-13088 | RHEA:75352, master 75351 | Pnao F8G0P1; physiological CycN acceptor |
| RXN-13089 | RHEA:34216, master 34215 | Native NADP aldehyde oxidation retained; exact S16 catalyst not asserted |
| RXN-13082 | MetaCyc:RXN-13082 | Native SpmABC; water plus unresolved generic acceptor |
| RXN-13081 | RHEA:33928, master 33927 | Native HspB dimer, F8G0M4; two NADH retained |
| 1.13.11.9-RXN | RHEA:27523, master 27522 | S16 Hpo F8G0M1 |
| RXN-11318 | RHEA:30844, master 30843 | S16 Nfo F8G0M2 |
| RXN-646 | RHEA:27386, master 27385 | S16 Ami F8G0M0 |
| MALEATE-ISOMERASE-RXN | RHEA:13170, master 13169 | Native maleate-isomerase dimer, F8G0M3; selected forward direction |
| SUCCSEMIALDDEHYDROG-RXN | RHEA:13214, master 13213 | Native NADP succinate-semialdehyde branch; exact S16 catalyst unresolved |

Every family claim cites and replays the actual Rhea master
`rh:directionalReaction` triple and selected directed sides. All selected Rhea
members are left-to-right relative to the master convention. The native
maleate reaction is reversible; forward direction denotes the selected pathway
use, not an assertion of chemical irreversibility. Ten native order edges join
carbon intermediates, including the HspB product branch to succinate. Shared
water, redox carriers and cofactor pools do not create extra ordering edges.

## Later physiological chemistry supersedes the old oxidase equations

The complete primary XML bodies for PMID:33432238 (2021, PMC7904663) and
PMID:35835223 (2022, PMC9396064) were read at the cited Results, Methods and
figure sections. They establish CycN as the physiological acceptor for NicA2
and Pnao by purified electron-transfer experiments, S16 genetic disruption and
complementation. Current reviewed UniProt/Rhea chemistry agrees. Each turnover
uses two oxidized cytochrome c molecules and produces two reduced molecules;
whole carrier states `RHEA-COMP:14399` and `RHEA-COMP:10350` are retained.
Oxygen/hydrogen-peroxide equations in older sources are not assigned to these
physiological reactions. Slow oxygen side reactivity does not contradict this
scope. The graph does not invent the downstream CycN oxidant: the 2021
Discussion explicitly leaves it unknown, and the later membrane-oxidase
suggestion is not treated as an established reaction.

CycN's current unreviewed UniProt accession `A0A0E3ELC2` merges strain records
under taxon 303 and the gene name ndaB. Its exact application to S16 is therefore
not based on a shared name. The native `WP_080563818.1` full 132-aa sequence is
identical; RCSB 7TLX entity 1 explicitly gives S16 taxon 1042876, and its mature
105-aa sequence equals residues 28–132 with an explicit SIFTS alignment. The
2021 paper identifies S16 locus PPS_RS28240; the 2022 structure uses that CycN
construct. Two nonstoichiometric `has_input` edges identify this concrete
carrier realization; they add no additional molecule to the chemical equation.
They do not transfer the experiments to every strain merged into UniProt.

## Protein identity, assemblies and conditional evidence

Individual current UniProt JSON records and release headers document release
2026_03 and each entry/sequence version. NicA2, Pnao and HspB are reviewed.
Hpo, Nfo, Ami, maleate isomerase and CycN are unreviewed; their direct primary
function and exact sequence bridges are stated separately. The four lower
nic2 proteins exactly match the 2012 deposit GQ857548: ADN26549.1 (F8G0M3),
ADN26550.1 (F8G0M2), ADN26551.1 (F8G0M1), ADN26552.1 (F8G0M0).

- NicA2 has condition-dependent monomer/dimer reports in current UniProt and
  the primary literature. Its functional `enables` edge does not select a fixed
  physical assembly. Pnao is reported as a homodimer; its functional edge does
  not import the distinct HZN6 oxidase complex or invent a complex identifier.
- Native HspB `CPLX-8439` contains two `MONOMER-17159` copies, whose native
  unification xref is F8G0M4. Native maleate isomerase `CPLX-8990` contains two
  `MONOMER-19246` copies, xref F8G0M3. Both native frames explicitly identify S16.
- SpmABC `CPLX-8991` has source-defined components `MONOMER-19251`,
  `MONOMER-19252`, and `MONOMER-19253`, one each. The 2013 deletion/complementation
  experiments establish function but do not measure purified stoichiometry.
  Native legacy UniProt links F8G0N9 and F8G0N8 now return inactive deleted
  records; these are not used as graph participants. Exact native protein
  frames preserve identity without guessing replacement accessions.
- The Spm reaction consumes water and a generic acceptor, producing its paired
  hydrogen donor. It does not consume oxygen or a guessed CycN partner. The
  proposed Mo-MCD association follows family similarity and failed active
  expression in E. coli in the 2013 Discussion, with a matching native
  enzymatic-reaction annotation. This is not a direct cofactor determination.
- Native `CPD0-1882` has C19H22MoN8O15P2S2, charge −2, derived from its InChI
  components/proton adjustment and CML formal charge. Its current ChEBI71308
  xref instead has an additional oxygen and charge −4. The graph retains the
  native cofactor identity and does not assert oxidation-state equivalence.
- FAD remains a bound prosthetic cofactor for NicA2/Pnao/HspB. The HspB curator
  inference code is retained. Hpo's ferrous-iron activity enhancement and
  0.025 mM assay condition come from the 2012 primary study; no physiological
  occupancy or structural binding site is claimed. NAD/NADPH used by coupled
  reporting assays are not assigned as substrates of Nfo or Ami.
- The maleate-isomerase assay used 1-thioglycerol, retained as an experimental
  condition rather than an endogenous stoichiometric cofactor.
- NicA2/Pnao/CycN periplasmic localization is explicitly predicted from signal
  sequences (2022 Introduction p0015), not measured native fractionation.

## Catalyst gaps preserved without truncation

S16 Sapd PPS_4079 is induced during nicotine growth, and its deletion slows but
does not abolish growth (2013 Results). The exact genome identity can be traced
to AEJ14618.1 in CP002870.1; the old UniProt F8G0P0 is deleted. However, the
purified NADP-specific aldehyde dehydrogenase and tetramer described by native
`CPLX-8441` belong to Pseudomonas sp. HZN6. The record retains the full native
NADP aldehyde reaction but does not import the HZN6 complex or upgrade the S16
gene phenotype into a direct cofactor-specific enzyme assay.

The terminal succinate-semialdehyde reaction is explicitly present in PWY-6993.
The inspected enzyme frames belong to Paenarthrobacter nicotinovorans, E. coli,
M. tuberculosis, Cupriavidus and Synechococcus, not an exact S16 catalyst.
The reaction remains present with this limit; no foreign enzyme is transferred.

## Chemistry replacement and issue 341

Rhea 142 still uses retired CHEBI:193521 for N-methylmyosmine. ChEBI 255 explicitly
marks it deprecated, points `IAO:0100001` to CHEBI:190393, and preserves the old ID
as an alternative on the active term. Both have the same C10H13N2, +1 state in
the inspected Rhea/current ChEBI data. The active graph uses CHEBI:190393, and
both incident edges cite this exact issuing-authority replacement.

Root integration reported [issue 341](https://github.com/CultureBotAI/PathwayMech/issues/341):
the initial `source_mappings.subject_id` also declared the retired ID in an
active identifier slot, causing the canonical ontology builder to reject it.
The correction removes only that active mapping stanza and preserves the
historical mapping in `nicotine-source-projection.json` and this dossier. It
retains both incident edge assertions and the active participant. The before
hash is `9ce8615af5768df3055df926fde6b65d1fee0104b12f8d26ea5b5bbc947a2830`;
the corrected target is
`559e7e393e76873e8b86e4bb14aa228208e4ec6ffda1bfb43dd147ff73d45aed`.
The full disposition is copied into `nicotine-validation.json`.

## Evidence access, computational context and reproducibility

The four complete inspected primary XML bodies are PMC3812094 (2013 route),
PMC7904663 (2021 NicA2/CycN), PMC9396064 (2022 Pnao/CycN), and PMC3332521 (2012
lower pathway). The latter includes complete Results/Methods and the exact
sequence accession GQ857548. PMC3234743 and PMC3302611 full-text retrievals
returned HTTP 500 and their PDF requests HTTP 403. Their facts are attributed
to inspected native MetaCyc or reviewed UniProt annotations, not to unread
primary full text. Other primary citations appearing in databases are not
silently treated as independently read papers.

The shared canonical iModulonDB dataset inventory lists p_putida/precise321 but
no explicitly S16-scoped dataset. It does not establish direct S16 applicability,
and no biochemical, regulatory, or absence-of-membership claim is inferred.
The shared receipts transparently document the console runner's missing dotenv
and the successful unchanged canonical client fallback; the E. coli context
queries concern other cohort records.

`nicotine-source-manifest.json` retains URLs, source versions, original-body
hashes, access failures and an allowlist of content/version headers. No session,
cookie or authentication headers are retained. The ChEBI digest is explicitly
for the uncompressed Semantic SQL database, not the downloaded OWL bytes.
All large bodies are hashed in 1 MiB chunks.

`nicotine-replay.py` re-reads original sources, checks all 10 Rhea families and
50 Rhea side occurrences, all five native Spm sides, all eleven pathway members,
source order, exact protein/sequence/assembly identities, reference/body hashes,
chemical replacement and full edge conservation. Ten reactions balance using
exact formula/charge data (reactive portions plus cancelling carrier backbones
for whole cytochromes). The generic Spm A→AH2 step has only a qualified formal
symbolic balance; no unknown carrier formula is invented. Native and closed
schemas and an actual isolated KGX export are included. Author results are in
`nicotine-validation.json`. Full corpus render, validation, tests, lint,
authority integration and independent scientific review are performed by the
coordinator/reviewer after this author freeze and are not claimed here as
already run by the author.

## Independent review attribution correction, issue 343

The independent reviewer identified two bounded source-attribution problems in
[issue 343](https://github.com/CultureBotAI/PathwayMech/issues/343). Edge 062
credited the HspB complex comment with the complete reaction; that comment
supports the assembly and selected cofactors, while the exact reaction link
is `catalyzes/ENZRXN-20030/reaction/RXN-13081`. The corrected edge cites that
actual link and preserves separate current UniProt/Rhea normalized chemistry.

Edges 082–091 credited the pathway XML with ChEBI identities that it does not
contain; its actual evidence is ordering and native compound frames. Those
native assertions now say precisely that. Each edge separately includes the
exact upstream product and downstream substrate evidence, including the
issuing-authority replacement for the active N-methylmyosmine identifier.
The descriptions identify the current shared carbon intermediate. No reaction,
participant, direction, catalyst or stoichiometry changed. The draft before
this correction was `559e7e393e76873e8b86e4bb14aa228208e4ec6ffda1bfb43dd147ff73d45aed`;
the corrected target is
`59d1a699b4e40ce680715afa958f8a659feae11b6b1786a5867f25733b83d36c`.
There are now 99 edges and 169 evidence blocks. The raw replay includes a
regression check requiring the native assertion to remain within native scope
and both separately grounded chemical sides to remain on every ordering edge.
The before/after assertions and observed hashes are retained in validation.
