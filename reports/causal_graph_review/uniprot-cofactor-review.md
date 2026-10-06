# UniProt cofactor annotation review

All current positive annotations were checked for existing curated overrides, exact identifier mapping, source cautions, and conditional or covalent states. The expanded twelve-batch manifest produced the same ten unprotected caution-bearing proteins. Existing reviewed cofactor decisions remain intact. Source hashes, native JSON positions, evidence codes and per-accession decisions are in `uniprot-cofactor-decisions.json`.

| Protein | Decision | Reason |
|---|---|---|
| P53128 | retain | Historical assignment as a mitochondrial ribosomal protein does not contradict the current FAD annotation; retain its similarity-based evidence grade. |
| P38891 | retain | Disputed growth phenotypes do not address PLP binding; retain the similarity-based PLP annotation. |
| Q05584 | retain | The caution concerns identities of older glyoxalase preparations, not the current GLO2 zinc annotation; retain the explicit inference from a human homolog. |
| Q12320 | retain | The caution concerns identities of older glyoxalase preparations, not the current GLO4 zinc annotation; retain the explicit inference from a human homolog. |
| P06700 | retain | Historical ADP-ribosyltransferase assignment does not negate the directly evidenced SIR2 zinc annotation. |
| P39006 | project_covalent_group | The cofactor note explicitly describes a covalently bound pyruvoyl group; use the exact group class rather than free pyruvate. |
| Q07560 | retain | The caution corrects the historical species attribution of a sequence; the current reviewed yeast entry and magnesium annotation remain applicable. |
| P15700 | retain | The dispute concerns nucleoside substrate specificity, not magnesium dependence; keep the metal assertion without expanding substrate scope. |
| P53318 | retain | The caution limits deamination in other taxa and does not negate the yeast FAD cofactor annotation. |
| P41735 | retain | Carbon catabolite repression was an indirect phenotype, not the enzyme function; retain the inferred iron cofactor annotation without adding regulatory causality. |
| P53037 | project_covalent_group | The cofactor note explicitly describes a covalently bound pyruvoyl group; use the exact group class rather than free pyruvate. |
| P21182 | project_covalent_group | The cofactor note explicitly describes a covalently bound pyruvoyl group; use the exact group class rather than free pyruvate. |
| P00561 | exclude_tentative | Sodium is a crystallographic observation with only tentative activity/stability effects; this is not an established physiological cofactor requirement. |
| P00562 | exclude_tentative | Sodium is a crystallographic observation with only tentative activity/stability effects; this is not an established physiological cofactor requirement. |
| Q03677 | qualify_branches | ADI1 metal identity changes the chemical products. These are alternatives, not simultaneous requirements of one reaction. |
| P39726 | retain_covalent_note | The source describes a covalently attached cofactor moiety. Keep that bound-state qualification; no free cosubstrate consumption is inferred. |
| P12695 | retain_covalent_note | The source describes a covalently attached cofactor moiety. Keep that bound-state qualification; no free cosubstrate consumption is inferred. |
| P19262 | retain_covalent_note | The source describes a covalently attached cofactor moiety. Keep that bound-state qualification; no free cosubstrate consumption is inferred. |
| P07702 | retain_covalent_note | The source describes a covalently attached cofactor moiety. Keep that bound-state qualification; no free cosubstrate consumption is inferred. |
| P28789 | retain_covalent_note | The source describes a covalently attached cofactor moiety. Keep that bound-state qualification; no free cosubstrate consumption is inferred. |

General alternatives such as magnesium/manganese remain separately annotated possibilities with the complete source condition visible; they are not asserted to be jointly required. Fe/Ni changes ADI1 reaction products and receives explicit branch qualifiers. Three pyruvoyl prosthetic groups map to CHEBI:45360 through exact ChEBI naming and the source note; native generic pyruvate cross-references remain traceable. Tentative crystallographic sodium associations are excluded.

The six lipid IV(A) native protein instances require two independently checked mapping statements: the GO-CAM individual has an EcoCyc type; the reviewed UniProt entry cross-references exactly that EcoCyc identifier. A UniProt entry does not directly cross-reference the native gomodel individual.

The final join audit found no species mismatch among 418 direct GO-CAM protein occurrences. All six native lipid IV(A) joins are reviewed Swiss-Prot entries for taxon 83333; the extractor now rejects an unreviewed entry in this native-identity join. Elsewhere, exact direct UniProt identifiers can refer to unreviewed entries: H6LBE7, H6LD21 and H6LFG3 carry positive automated cofactor annotations. Their TrEMBL status and ECO:0000256 HAMAP/ARBA attribution remain explicit; they are not represented as experimental or manually reviewed assignments.

The only additional chemical identifier required by these semantic projections is CHEBI:45360. The final integration applied 371 new cofactor edges across 93 records after checking all 152 records. The applied ledger is `uniprot-cofactor-plan.json`.
