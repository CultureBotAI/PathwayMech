# Sbm / ScpABC biochemical pathway curation

The new record is [succinate-to-propanoate.yaml](../../../data/pathways/succinate-to-propanoate.yaml), **MetaCyc:PWY0-43**, “conversion of succinate to propanoate.” It represents a named, experimentally motivated three-enzyme biochemical proposal annotated for E. coli K-12 MG1655, with explicit unresolved physiological and stereochemical limits. It meets the add-pathway multi-step boundary; it is not a wild-type flux assertion.

Ignored and hidden files were included in both exact and expanded semantic searches of the original checkout and this worktree. The prior `next-handoff.md`, source inventory, native projections and frozen PathBank screening were inspected. Original checkout: no maintained pathway record hit. Worktree: only this new record. Prior research already identified the candidate, so this is follow-up curation, not a claim of newly discovered source coverage. See `sbm-duplicate-searches.json` and `sbm-semantic-dedup-final.json` for exact commands, hits and hashes.

## Evidence and decisions

- [Haller 2000](https://doi.org/10.1021/bi992888d), full primary PDF, supports the three measured activities and coupled Sbm/ScpB assay. The cloning donor was strain 1655 and recombinant expression host BL21. The coupled assay does not separately resolve ScpB substrate enantiomers. The pathway proposal is distinct from a demonstrated physiological cycle.
- [Froese 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2741639/), complete primary HTML, supports native protein expression and Sbm–YgfD interaction, with apo-Sbm monomer/dimer mixture. Native complex membership represents the annotated Sbm dimer without making every protein state dimeric.
- [Gonzalez-Garcia 2017](https://doi.org/10.1186/s12934-017-0735-4), primary full text, reports epimerase rescue in engineered minimal-medium cultures. This conflicts with a physiologically complete three-enzyme cycle; it does not provide a direct isolated ScpB R-versus-S assay.
- [Stunkard 2019 supporting information](https://doi.org/10.1021/jacs.9b00650.s001), independently resolved through ACS Figshare article 7863569/file 14641211, uses an R/S substrate mixture in the MMCD-His6 assay (Sections V–VIII; Figures S4–S6/S9). The S2A construct is used for crystallization. This provides later direct decarboxylation/hydrolysis evidence but leaves enantiomer specificity unresolved. The main article remains inaccessible; only its abstract and the primary supplement were inspected.
- Reviewed UniProt retains ScpB's R-specific Rhea assignment. The graph preserves that annotation and its evidence codes, with explicit per-edge qualifications. It does not silently replace R with S or invent a native epimerase.
- Native MetaCyc complex CPLX0-7741 contains two P27253-mapped subunits; CPLX0-254 contains six P52045-mapped subunits. The older ScpB crystal-assembly paper PMID:10769118 was inspected at complete indexed-abstract level and agrees with the native/UniProt hexamer assignment. ScpC uses its protein identifier; no unsupported oligomeric state is asserted.
- Rhea 142 RDF and directional table independently resolve reactions 22890 (right-to-left), 27667 and 28011 (left-to-right). All 10 chemical-side edges are replayed through actual directed Rhea sides and contain coefficients, then checked against ChEBI 255 formulas, charges and canonical labels. Net: succinate(2-) + H+ → propionate + CO2. CoA carriers cancel. CHEBI:18408 is canonical **cobamamide**, the adenosylcobalamin cofactor, and is not consumed by the cycle.
- Native PathBank SMP0002070/PW002058 has the corresponding three activities; its older protein labels are resolved using current reviewed UniProt. Adjacent SMP0002069/PW002057 is a broader map and is not conflated with this record.

## Deliberate exclusions

YgfD/ArgK is not a fourth carbon-conversion catalyst; its interaction does not supply a missing native epimerase or prove complete flux. No engineered heterologous epimerase, amino-acid feed pathway, propanol branch, sodium pumping, biotin requirement, generic B12 substrate, or ScpB hydrolysis branch is imported. Magnesium in a 2019 assay mixture alone does not establish a required catalytic metal. No crystal analog is treated as an endogenous substrate. No mammalian homolog function or sodium-translocating decarboxylase EC classification is transferred to this biotin-independent E. coli protein.

The root's six exact-locus iModulonDB queries include scpA/b2917, scpB/b2919 and scpC/b2920, with one gene hit and zero module hits per query. This is contextual search output, not proof that the genes lack regulatory-module membership; no regulatory edge is added. See `imodulondb-context.json`.

## Identifiers

Record and native references: MetaCyc:PWY0-43, MetaCyc:CPLX0-7741, MetaCyc:CPLX0-254, MetaCyc:METHYLMALONYL-COA-MUT-MONOMER, MetaCyc:G7516-MONOMER, MetaCyc:G7517-MONOMER, MetaCyc:METHYLMALONYL-COA-MUT-RXN, MetaCyc:RXN0-310, MetaCyc:RXN0-268.

Nodes: NCBITaxon:511145; UniProtKB:P27253, UniProtKB:P52045, UniProtKB:P52043; RHEA:22890, RHEA:27667, RHEA:28011; CHEBI:30031, CHEBI:57292, CHEBI:57326, CHEBI:57392, CHEBI:17272, CHEBI:15378, CHEBI:16526, CHEBI:18408. Literature references: PMID:10769117, PMID:18950999, PMID:10769118, PMID:28716098 and DOI:10.1021/jacs.9b00650.s001. Additional inspected contextual PMID:11955068, PMID:30869886, PMID:28407739; mapping leads PathBank:SMP0002070/PW002058 and excluded adjacent PathBank:SMP0002069/PW002057.

## Author checks and reproducibility

`sbm-sources.json` records exact bodies, SHA256 digests, reuse provenance, failed attempts, and full-text inspection scope. Downloaded publications remain external; committed projections are bounded. Signed download redirects are not preserved in committed metadata. `sbm-native-projection.json`, `sbm-protein-projection.json`, and `sbm-chemistry.json` retain the defining structured source fields.

Run the author replay from the worktree:

```bash
UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv run python research/pathway_additions/2026-10-10-citrate-sbm/sbm-verify.py --raw /private/tmp/pathwaymech-citrate-sbm-evidence/sbm --authorities /private/tmp/pathwaymech-curation-authorities --output /private/tmp/sbm-checks-replay.json
```

The replay checks the local contract, closed LinkML schema, every chemical side, elemental/charge balance, native assembly mappings and exact referenced source-body hashes. `sbm-checks.json` records the actual author run and target hash. Full render/validate/test/lint and shared authority/history integration are delegated to the root and are not claimed as author-run checks. An initial author check caught the unsupported draft key `context`; it was corrected to the schema's `description` before passing. An initial native predecessor locator was tightened to include the `predecessor-reactions` element before freezing. Neither correction changes the biochemical claims.

## Independent finding resolved

[Issue #324](https://github.com/CultureBotAI/PathwayMech/issues/324) corrected the PMID:18950999 locator on `sbm-edge-011`. The actual native-PAGE monomer/dimer evidence is Results “Interaction of YgfD and Sbm in vitro” (P17), Figure 4B and Figure 4C panel 2, with Discussion corroboration. Figure 3 concerns in-vivo immunoprecipitation. The scientific assertion is unchanged. Before SHA256: `6ee1a9265b1f8e0a6392a73009815a690fdc9a8395357707aa8dc7916c049a75`. After SHA256: `d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268`. Author replay was rerun after this correction; the independent reviewer verifies the final bytes.

Author-owned helper `ruff check` and `ruff format --check` passed; all 10 owned text files passed trailing-whitespace checks and all owned JSON parsed. The scoped ignored-inclusive scan found no signed download URL or credential marker in these artifacts. No full repository gates were rerun by this author.
