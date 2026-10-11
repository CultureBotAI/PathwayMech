Resolve coproheme-route iron states before adding MetaCyc:PWY-7766

The complete five-member heme b biosynthesis IV candidate is deferred. No
maintained record was created, and this finding does not identify an existing
published-record defect.

Current inspected Rhea 142 reactions 57941/57945 and net 56517 point to
CHEBI:68438 → CHEBI:142463 → CHEBI:60344. ChEBI 255 structures and native
MetaCyc 22.5 CPD-17070/CPD-21388/PROTOHEME InChIs encode Fe(II). These are not
oxidation-state-neutral nodes. Simply relabeling them or adding a caveat would
still export specific Fe(II) consumes/produces assertions.

Primary sources establish a conflicting ferric mechanism in specific organisms:

- PMID:27982566, DOI:10.1021/acs.biochem.6b00958, S. aureus: full BioC passage
  offset 4273; Results offsets 20324–22035 and 25935–27957; Discussion offset 46564.
- PMID:27758026, DOI:10.1111/febs.13930, L. monocytogenes: full XML sections
  `febs13930-sec-0006`, `-0008`, `-0009`, and `-0019`.
- The newer B. subtilis PMID:40850531 main text, §§2.1/3.1–3.4/4, was also
  inspected through retained author-uploaded text extracts. Its FMN alternative
  does not resolve the exact iron-state/stoichiometry gap; PDF/supplement access
  remains incomplete. Species-specific evidence must remain separate.

The inspected pinned ChEBI/Rhea/native-object searches resolve ferriheme
CHEBI:55376 but not a complete compatible set of ferric intermediate/reaction
identities. This is a bounded result, not global identifier absence.

Acceptance requires verified chemical structures and reaction identities for a
complete source-supported microbial route, explicit handling of the Fe(II)
insertion-to-decarboxylation transition and consecutive intermediate, and
independent scientific review. A genuinely supported machine-readable uncertainty
representation is also eligible for review; unsupported specific states with
prose caveats are not. Do not truncate the full pathway or double-count its net
reaction. The exact checks and source limits are in
[heme-handoff.md](heme-handoff.md), with source-body digests in
[heme-source-manifest.json](heme-source-manifest.json) and complete source
equations in [heme-source-projection.json](heme-source-projection.json).
