# Putrescine Degradation II — bounded curation

Target: `PathBank:SMP0002067`, `data/pathways/putrescine-degradation-ii.yaml`.
The selected core contains the four PuuA/B/C/D conversions from putrescine to
GABA. The native PathBank map also contains uptake objects; their exclusion is
explicit. `GO:0009447` covers putrescine catabolism more broadly, including the
alternative aminotransferase route, so it is not substituted for this identity.
UniProt independently names all four steps of 4-aminobutanoate formation and
links them to UniPathway `UPA00188` (`UER00880`–`UER00883`). These legacy links
are contextual identifiers, not newly declared graph nodes.

Ignored and hidden files were included in exact identifier, name, synonym,
protein, reaction, PMID and DOI searches in both the clean worktree and the
original repository. Prior PathBank inventory entries were pending candidates.
The original repository additionally contains ignored DRAM support rows
1141–1144 for `M00136`, with `K09470`–`K09473` and `R07414`, `R07415`,
`R07417`, `R07418`, `R07419`; those rows were read. Neither repository had an
existing maintained exact core record. Substring hits in ALDH family names and
content hashes are unrelated. The duplicate-search receipt records both scopes;
this is not a claim that external sources are exhausted.

The chemical corrections are source-grounded, not repaired by name similarity:

| Native assertion | Disposition and independent support |
| --- | --- |
| `PW_C042556` γ-glutamyl-GABA has no xref and an incompatible SMILES | Use `CHEBI:58800`, the charge −1 L-glutamyl amide; `CHEBI:49260` explicitly defines GABA amino-group condensation with the glutamate γ-carboxyl group. Native SMILES lacks the amide topology and stereo annotation. |
| `PW_C044519` aldehyde SMILES conflicts with its `CHEBI:61508` xref | Retain the authority's exact glutamyl-amide aldehyde zwitterion used by both adjacent Rhea reactions; reject the native structure string. |
| Native PuuB reaction lists a hydron input and omits water | Use independently inspected `RHEA:28415`, which consumes water, dioxygen and glutamylputrescinium. |
| Native neutral or mixed charge forms | Retain Rhea's exact ChEBI forms, all 23 chemical-side occurrences and coefficients; `RHEA:28411` produces two hydrons. |

No exact-match mapping is invented for either defective native structure.
The projection retains their original strings, definitions and dispositions.
Rhea release 142 RDF supplies the selected directions `13634`, `28415`, `28411`
and `19738`; their equations match the independently queried Rhea 139 authority
labels exactly. The graph selects catabolic orientations without asserting a
thermodynamic irreversibility experiment.

Protein identity and activity are resolved through freshly fetched reviewed
UniProt JSON and primary literature. PuuA `P78061` and PuuD `P76038` retain
native complex instances `/ProteinComplex/4033` and `/ProteinComplex/1396`,
respectively: twelve PuuA copies and two PuuD copies. A component is not given an
independent monomer-catalysis edge. The PuuA dodecamer is explicit in the primary
2008 abstract; the PuuD homodimer is an experimental UniProt annotation to the
2006 paper. PuuA's magnesium requirement and substituting manganese are explicit
`ECO:0000269` annotations; the two metals are alternatives. These claims do not
rest only on MgATP assay wording.

`P37906` PuuB FUNCTION has `ECO:0000269` to PMID15590624, while its catalytic and
step 2/4 comments have no separate evidence codes. They retain those distinct
evidence grades. PuuC `P23883` has an experimental NADP-dependent catalytic
annotation and explicit left-to-right direction; its step 3/4 statement combines
experimental and inferred evidence. NAD-dependent activity is also supported
but is outside this map's selected NADP variant. NAD preference observed with
other aldehydes is not generalized to an intracellular cofactor ratio here.
PuuD's catalytic annotation is experimental; its step 4/4 comment has no
separate evidence code. All structured assertions are attributed to the inspected
database, not presented as paper quotations.

Primary sources inspected:

- PMID15590624, DOI `10.1074/jbc.M411114200`: indexed primary abstract identifies
  the sequential glutamylated pathway. The wider paper's import and downstream
  transamination scope is kept distinct from this four-reaction core.
- PMID18495664, DOI `10.1074/jbc.M800133200`: indexed abstract describes purified
  PuuA, ATP-dependent ligation and its dodecamer. Kinetic constants are excluded;
  the ATP Km differs between this abstract (2.35 mM) and UniProt (2.25 mM).
- PMID16499623, DOI `10.1111/j.1574-6968.2006.00137.x`: indexed abstract reports
  purified PuuD, catalytic Cys114, intermediate accumulation in its deletion
  strain and conditional physiology. No residue or transcriptional graph is
  inferred from these contextual observations.
- PMID22636776, DOI `10.1128/JB.05063-11`: indexed abstract and publisher full-text
  sections covering W3110 derivatives, growth conditions and the two catabolic
  routes were inspected. Genetic redundancy depends on conditions; a universal
  PuuA/B/C essentiality statement would be wrong. The study supports keeping
  uptake, the aminotransferase route and GABA-to-succinate reactions separate.
- PMID18668238, DOI `10.1007/s00253-008-1608-x`: indexed abstract describes broad
  PuuC aldehyde specificity and assay effects. Neither unrelated aldehydes nor
  laboratory reductants/inhibitors are promoted into this core.
- PMID35409114, DOI `10.3390/ijms23073752`: a newer Rhea citation was checked and
  concerns Streptomyces GlnA2, not E. coli PuuA; it is excluded from this taxon's
  experimental evidence.

Four short quotes are literal substrings of the indexed primary abstracts;
all other evidence is a traceable structured assertion. Full original 2005,
2008 and 2006 articles were not available for direct inspection. Publisher PDF
requests returned 403, Elsevier API attempts returned 429, and the Europe PMC
fullTextXML attempts returned 500. The 2012 publisher text was accessible through
the browser tool despite a direct-download 403. The manifest distinguishes
these attempts and does not invent full-text digests. Each PMID reference digest
covers the complete multi-record Europe PMC response identified in the manifest.

The canonical iModulonDB adapter, run by the integration agent on 2026-10-10,
returned seven `puu` genes in `e_coli/precise_mg1655` and module
`e_coli/precise_mg1655/71` (Putrescine). The required module summary was read:
its eight members include all four core proteins, PuuP, PuuR, PuuE and ymjE.
The four core weights are PuuC 0.32115, PuuB 0.306626, PuuA 0.291911 and
PuuD 0.276739, with module threshold 0.138472. This is computational expression
context; it does not establish catalysis, direct regulation or a requirement for
the additional proteins. Both rendered adapter outputs and hashes are retained
externally. Commands used the canonical runner with `imodulondb search
--organism e_coli --dataset precise_mg1655 --query puu` and `imodulondb summarize
--organism e_coli --dataset precise_mg1655 --k 71`, after dataset discovery.

Excluded source facts include PotABCD transport and its displayed stoichiometry,
transport compartments, PuuP-dependent physiology, PuuR regulation, downstream
PuuE/GabT and YneI/GabD/PuuC reactions, alternative PatA/PatD metabolism, and
unverified PuuB cofactor or core-compartment guesses. Their omission does not
assert biological absence or cofactor independence. The source projection has
explicit dispositions, including the older PuuA essentiality claim that cannot
be generalized across growth conditions.

The author performs only narrow schema, source, chemical-balance, quotation and
KGX checks. Shared authority snapshot integration, append-only history, generated
pages, full validation/tests/lint and independent scientific review remain the
parent's integration work. See the validation receipt for actual results.
