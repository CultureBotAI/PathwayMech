# Next263 authority candidate preparation

This is external authority source-author work for MetaCyc:PWY-5417, bound to merged commit `46ee133770039e8b21d1563166dec50eecd2c411`. It is not an independent scientific review, a maintained authority update, or a final record selection. Only a separately supplied, exact hash-bound record may select additions. All work remains outside the repository.

Use `candidate-lookup.final.json` for the complete finite inventory and `record-author-name-category-lookup.final.json` for the 121 prospective record endpoints requested by the record author and root. The latter includes optional Q52154; it does not decide that PcaR will be selected. Current owner labels are retained exactly. Suggested categories follow the source object and intended role and do not add experimental facts.

The inventory contains 141 candidates: 84 native biological/activity/pathway identities, 35 ontology identities, 21 UniProt accession contexts including one excluded inactive accession, and one PubChem identity. Of these, 44 already have owners and must remain unchanged, 89 have prepared missing-source authority candidates, seven have pinned-ontology additions, and Q9AEQ0 is explicitly excluded. The 89 source candidates comprise 69 native identities (50 exact HTML originals and 19 supported Protein XML originals), 19 optional active UniProt contexts, and one exact PubChem property original. These are availability candidates, not a proposal to add every ID.

All 89 missing-source candidates were extracted by the unmodified canonical source builder and accepted by the current consumer loader. Both earlier candidate stages remain immutable observations within this package. The five newly covered parent taxa are NCBITaxon358,384,386,5554,65741; the two additional ChEBI terms are149587 and57712. Complete pinned NCBITaxon, ChEBI and Rhea database bytes were hashed during this preparation and match their current authority owners; all selected rows were queried read-only. All formal13 ChEBI and six directional Rhea terms were already present and remain exact.

The baseline is 5172 terms (3021 source and2151 ontology),1029 snapshot owners (1024 source and five ontology), and1205 source-manifest rows. Baseline config/snapshot bytes and relevant contracts are copied and hash-bound. Do not replace a current term, owner or manifest row with a new source merely because its wording is newer. Current issuing display contexts and historical preparations remain in the separately frozen scientific packages.

## Authority boundaries

- The parent pathway's whole XML does not fit the current typed-pathway profile: direct `in-pathway`, `pathway-link`, `sub-pathways` and `super-pathways` slots are unsupported. Its failed probe is preserved. The existing, supported native HTML adapter supplies exact object identity and native title; no typed biological entity assertion is inferred from the generic HTML template. Root explicitly accepted this route. No adapter or policy was weakened.
- All23 missing native Gene names, four unnamed Protein names,22 activities and the parent name have exact new HTML originals. The complete existing509 HTML authority sources were parsed first, with hash checks independent of gitignore; none supplied these missing identities. This bounded search does not claim global filesystem absence. Default-network DNS failures and subsequent successful acquisitions are separate receipts.
- Native protein/complex and gene participants require canonical or authority-supplied synonym labels. MetaCyc reaction/activity display labels may be contextual under the existing policy. A contextual display rule never substitutes for identifier existence or biological scope.
- Q9AEQ0's issuing deletion response supplies no active term or replacement. The four discontinued Entrez pointers and two ungrounded native parent-strain contexts remain explicitly excluded. Neither these nor PDB mappings supply replacement biological identities.
- Optional UniProt contexts are available only if actually selected. Exact sequence or accession identity does not identify historical PcaD, C-1 isozymes, native assemblies or experimental preparations. Q52154 retains the uncertain initiator and construct limitations in the biological and primary source packages.
- PubChem:25240959 requires the canonical label `5-Chloro-4-oxopentanoate`. Its authority original uses the exact adapter-required Title/IUPACName/MolecularFormula/InChIKey request. Root's separate chemical original supplies full InChI and explicit charge−1. CID, formula, InChIKey and IUPACName agree between the two responses; the authority title is not used to infer charge or assay speciation.

## Exact selected-union helper

Run only after the actual record draft and SHA-256 are supplied:

```text
/private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B \
  /private/tmp/pathwaymech-next-263-authority-author/helpers/prepare_selected_authority_union.py.txt \
  --record /absolute/path/to/actual-draft.yaml \
  --record-sha256 ACTUAL_SHA256 \
  --output /private/tmp/NEW-selected-authority-successor
```

The output must be new and external. The helper freezes the actual named-ID selection, rejects unprepared/inactive/ungrounded additions, preserves all prior terms and source owners exactly, and appends only selected missing source entries. It verifies original source-cache descriptors including nested companions, runs the canonical source builder, compares its result to the exact preserved union, and runs the identifier consumer on the supplied draft. Resolver selection fixtures are clearly separate from the observed draft. Whole-corpus gates and promotion belong to root. No maintained writes occur.

Pure selection/preservation guard checks pass, including exact retention of all5172 terms, selected-only additions, inactive/ungrounded rejection and empty-selection behavior. These are synthetic helper checks, not a claim to have received or validated the actual final record. The helper refuses changed baseline authority/runtime files until an explicit context rebind is prepared.

## Retention

`compact-retention-manifest.json` is the finite copy contract. Every row binds an actual original path, bytes and SHA-256 to the exact stored relative path, bytes, SHA-256 and encoding. Gzip is deterministic (mtime zero) and lossless. Python source is retained as inert `.py.txt`; baseline YAML and resolver fixtures use `.yaml.txt` where retained. Original response bytes remain unchanged. The compact files are evidence archives; run helpers from the complete external author package, whose source-cache paths and frozen inputs remain available.

`receipts/baseline-and-package-intake.json` independently verifies the complete native, chemistry and biological packages including hidden/ignored inventory. Root's additional chemistry is separately bound by exact verification and original hashes. All previous source owners and their source caches remain owned by their existing frozen packages. A successor, rather than an edit to this package, must bind actual final selection or later changes.
