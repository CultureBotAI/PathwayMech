# GarD primary evidence handoff

Completed external-only appraisal of PMID31811683 / PMC7021002 / DOI10.1002/pro.3796. Read `.claude/skills/add-pathway/SKILL.md`, `docs/CAUSAL_GRAPHS.md`, `CLAUDE.md`, and `docs/CURATION.md`. No repository or GitHub changes.

## Deliverables

- `primary-appraisal.txt`: concise primary findings and limitations.
- `edge-ready-excerpts.json`: three exact short excerpts, their printed-page/section locators, and proposed uses. Total verbatim excerpt length is 23 words; none is a database quotation misattributed to the paper.
- `identity-audit.json`: independently inspected UniProt and PDB identity, full sequence comparison, construct differences, donor/host scope, and reaction cross-references.
- `read-ledger.json`: all 12 PDF pages read and visually inspected, all six figures and both tables assessed, and supplement availability explicitly bounded.
- `provenance-manifest.json`: original URLs, retrieval times, byte lengths, hashes, and accepted/rejected-body distinctions.
- `reused-original-bindings.json`: exact previous-preflight acquisition receipts for four copied authority objects.

The complete original article is `originals/PMC7021002-europe.pdf`, 10,485,614 bytes, SHA-256 `0e574a7216c39c92082523acc48311e6220b53553afc60aca969bdda3512c3f5`. Successful public request: `https://europepmc.org/articles/PMC7021002?pdf=render`, resolving to `https://europepmc.org/api/getPdf?pmcid=PMC7021002`. The printed article runs pp.711–722. Derived text and page images are inspection aids, not source originals. Failed PDF-named responses are HTML and are rejected in the manifest.

## Independent identity and graph use

UniProt P39829 is GarD/GARD_ECOLI, 523 residues, E. coli K12 (issuing taxon 83333), ordered locus b3128. PDB6U7L's issuing `entity_src_gen` specifies the source variant MG1655 and expression host BL21(DE3), variant Magic, plasmid pMCSG53. Its SIFTS and native CIF cross-references cover P39829 residues1–523. The canonical deposited sequence is **exactly SNA + the retained UniProt sequence**, verified by direct equality, not similarity threshold. MSE/phospho-Asp are represented separately from canonical residue letters. The PDB native sample retains SNA at author positions -2/-1/0; entity1 (chainsA/B) has phospho-Asp and MSE, entity2 (C/D) has MSE without that phospho-Asp. These structural states do not establish the activity assay's modification occupancy.

The article's Methods4.1 locus b3218 conflicts with its Methods4.4 b3128. Both independently inspected issuing authorities support b3128. Treat b3218 as a source discrepancy, not a new gene identity. The article itself does not give the genomic donor strain in its cloning paragraph; the MG1655 link comes from the deposited source record.

Native MetaCyc27.0 `CPLX0-8537` has exact label “galactarate dehydratase,” native species511145, component coefficient2 for `GALACTARDEHYDRA-MONOMER`, and a `catalyzes` relation through `GALACTARDEHYDRA-ENZRXN` to `GALACTARDEHYDRA-RXN`. The monomer's UNIPROT dblink is P39829. This supports an identified assembly catalyst without pretending that each isolated subunit was assayed independently. Its whole XML is retained.

UniProt's inspected catalytic-activity block supplies master RHEA16005, physiological left-to-right RHEA16006, and galactarate → 5-dehydro-4-deoxy-D-glucarate + water. Native MetaCyc reaction XML independently preserves D-GALACTARATE → 5-KETO-4-DEOXY-D-GLUCARATE + WATER. UniProt supplies Fe2+ / CHEBI29033 with ECO0000269 linked to this paper. **ChEBI/Rhea issuing identities still need their own verification before adoption**; these inspected cross-references are not a substitute for it.

Recommended record treatment: native assembly membership and complete chemical sides can cite the structured authority; the catalytic/cofactor evidence can additionally cite the primary excerpts with a recombinant TEV-cleaved construct qualifier. Do not silently equate the SeMet crystal preparation with the activity preparation. Preserve assay conditions from `primary-appraisal.txt`; do not add untested calcium/manganese cofactor substitutions or a definite iron-binding site. The primary observation plus native reaction establishes forward entry-route support, not an experimental determination of thermodynamic irreversibility.

## Remaining checks for the author

- Independently verify the reaction and chemical identifiers, including complete water output and the native product stereochemical identity.
- Use the article's primary entry-enzyme evidence only for that scope; its pathway cartoon does not replace downstream primary evidence from dossier228/other inspected papers.
- Assess whether to include structural calcium binding at all; it is unnecessary for the physiological route and must not become `has_cofactor` by inference from a crystal ligand.
- No supplements were listed in the inspected article or EuropePMC metadata (`hasSuppl=N`); publisher access failed. This records the checked scope, not universal absence.

No 2025 paper was fetched or appraised in this assignment.
