# Pathway mechanism research: catechol degradation III

## Pathway scope

The candidate is **MetaCyc:PWY-5417 — catechol degradation III (ortho-cleavage)**,
the complete six-step route joining the four-step catechol ortho-cleavage module
and the two-step 3-oxoadipate degradation module. The existing child records
remain separate, narrower pathways. The hydrolytic and oxidative meta-cleavage
routes have different boundaries and chemistry.

The [merged-baseline duplicate assessment](root-verification/dedup/HANDOFF.md)
binds the addition decision to commit `46ee133770039e8b21d1563166dec50eecd2c411`.
It covers all 259 maintained records in that checkout and all 258 records in the
preserved original checkout. No individual record has the exact parent identity
or all six defining reaction families. The 719 matching root/file occurrences
have explicit dispositions. Searches included ignored and hidden files, with
documented Git/environment, binary, archive, directory-symlink and external-cache
limits. This is a bounded duplicate decision, not source exhaustion.

Eleven native parent-organism annotations contain nine direct taxonomy joins and
two ungrounded strain contexts, mt-2 and Rm2011. Native occurrence annotations,
component donors, expression hosts and experimental preparations retain their
different evidential scopes. Neither a parent annotation nor a single enzyme
assay proves an independently demonstrated complete route in every named taxon.

## Mechanistic summary

The route comprises catechol 1,2-dioxygenation, muconate cycloisomerization,
muconolactone isomerization, enol-lactone hydrolysis, CoA transfer and thiolysis.
The exact selected directional equations are RHEA:23853, RHEA:30033,
RHEA:12349, RHEA:10185, RHEA:12049 and RHEA:19483, respectively.
Native cycloisomerase and thiolase equations are written in the opposite
orientation to their route traversal. Native reversible annotations for the
transferase and thiolase remain distinct from the selected route direction.

The [independent chemical assessment](independent-chemistry/HANDOFF.md) verifies
13 formal chemical identities, six complete equations, 21 material-side entries
and five joins. Summation gives catechol + oxygen + water + CoA(4−) →
succinate(2−) + acetyl-CoA(4−) + two hydrons. Succinyl-CoA is consumed and
regenerated, so it cancels. Both sides contain C27H40N7O21P3S with charge −4.
This is stoichiometric bookkeeping, not an extra elementary reaction or a
measured flux. Exact stereochemical and protonation boundaries remain explicit.

## Evidence table

| Evidence package | Completed scope | Interpretation boundary |
| --- | --- | --- |
| [Discovery](source-evidence/discovery/HANDOFF.md) | Native parent, children, alternatives and prior mentions | The initial baseline is superseded by the bounded merged-baseline duplicate assessment. |
| [Native closure](source-evidence/native/HANDOFF.md) | 247 complete native originals, 3,252 direct slots, 420 required relations, 20 formal activities and 19 catalysts | Database evidence codes and adjacent activities do not establish direct experimental catalysis or whole-route occurrence. |
| [Chemistry source work](source-evidence/chemistry/HANDOFF.md) | Complete formal chemistry and issuing structure comparisons | Structural identity does not establish an unresolved historical assay preparation. |
| [Primary evidence](source-evidence/primary/HANDOFF.md) | 48 source-access records, 63 supported claim dispositions and 18 native conflicts | Article bodies, transformed text, page scans, abstracts and metadata retain their individual access limits. |
| [Biological identity](source-evidence/biological-identity/HANDOFF.md) | 59 biological objects, 98 issuing originals, 45 translated CDSs and six PDB preparations | Exact sequence identity does not establish the same assay, construct, assembly or strain. |
| [Additional chemicals](source-evidence/additional-chemistry/HANDOFF.md) | Eight exact metal, nucleotide, chelator and inhibitor identities | Enzyme-context endpoints do not add formal route steps or establish an inhibition target. |
| [Expression and inhibitor chemicals](source-evidence/context-chemistry/HANDOFF.md) | Exact 2-oxoglutarate and adipate identities | Existing authority owners are preserved; structural identity does not establish assay protonation. |
| [Selected authority integration](authority-integration/HANDOFF.md) | 77 selected additions; complete old term and owner preservation | The final-draft ontology replay covers 37 selected terms and does not rebuild legacy ontology ownership. |

## Gaps

A primary-author summary incorrectly assigned benzoate repression to pcaF.
The [explicit P263-C48 correction](source-evidence/primary/CORRECTIONS.md),
tracked in [issue 567](https://github.com/CultureBotAI/PathwayMech/issues/567),
retains the original abstract's distinction: pcaK is repressed, pcaF is not.
The frozen historical summary is preserved and its incorrect portion superseded.
The same correction notice also links [issue 568](https://github.com/CultureBotAI/PathwayMech/issues/568):
P263-C43's thiolase activities occur in prose on printed page 6485, not Table 1.
The measured values and their crude-extract scope are unchanged.

The primary B13 study assigns three uncompetitive analog inhibitors to the
transferase, contradicting their native thiolase targets. Its thiolase salt
assays, NADH results and substrate-destroying mercury reagents have distinct
interpretations. NaCN is not an HCN assay. Primary EDTA assays in PMID14617643
support only the adjacent CcaC trans-dienelactone activity. Its distinct
4-chloromuconolactone activity retains native-only inhibition support because
that substrate was unavailable in the paper; the PMID18789896 abstract reports
metal reactivation without an EDTA statement. The
[bounded evidence successor](root-verification/edta-primary-evidence-successor.json)
and [charge-wording correction](root-verification/edta-charge-wording-successor.json)
preserve the exact assay and chemical-identity limits.

The MT1 native CatA and SalD preparations have different substrate preferences;
their assays are not reassigned to cloning hosts. CatC remains inferred.
Historical PcaD mass and oligomer observations are not measurements of modern
Q88N36. Deleted Q9AEQ0 has no inferred replacement. Exact PDB constructs and
native enzyme preparations remain separate. H16 pcaI, pcaJ and pcaF identities
follow their direct accession/locus bindings rather than conflicting prose.
The [CatA preparation correction](root-verification/issue-569-cata-preparation-correction.json),
tracked in [issue 569](https://github.com/CultureBotAI/PathwayMech/issues/569),
separates the strain-unspecified AY029000.1/AAK33066.1 deposit from the mt-2
clone and mt-2/C-1 sequence comparison in PMID7646060.

## Candidate YAML

The [maintained record](../../../data/pathways/catechol-degradation-iii.yaml)
is integrated from the [frozen author proposal](record-author/HANDOFF.md), whose
SHA-256 is `0ad615b268d0f63ff253287401b4a978d4c7d1603157717e7e57eab5e1816ec6`.
The maintained successor has SHA-256
`b30573a380b358a9b0228f8e3e2689943ecf828aa01ae790f281ba3fe617e603`;
the explicit corrections above and the
[reference-metadata correction](root-verification/issue-568-reference-metadata-correction.json)
account for its changes without rewriting the author package.
It contains nine taxa, 83 participants, 30 reaction nodes, 117 edges and 211
references. The 259 pre-existing pathway records remain byte-identical.
Root's native validation and separate closed JSON-schema validation passed on
the initial integration; the complete gates are being run on the successor.
The [author validation wording correction](record-author-validation-wording/correction.json)
preserves the distinction between those two checks without rewriting the frozen
author receipts. The selected authority snapshots are promoted and the actual
260-record identifier consumer passed after the reference correction; subsequent
changes preserve every named identifier and label. Generated outputs, full
repository gates, independent final review and protected publication are still
being completed.

## Retained artifacts

The [source retention map](root-verification/source-retention-manifest.json)
records exact source-to-repository storage paths for six frozen evidence
contracts. The [duplicate retention map](root-verification/dedup-retention-map.json)
and [supplemental chemical map](source-evidence/additional-chemistry/retention-map.json)
cover their separate finite payloads. Source digests retain their original
artifact meanings. Inert helper filenames and lossless gzip storage do not
rewrite scientific evidence. Source-package inventories and root intake receipts
remain distinct from scientific acceptance.

Large originals excluded by the finite retention contracts remain external and
hash-bound. Stored projections do not claim to replace those originals. Public
release licensing remains deferred as instructed.
