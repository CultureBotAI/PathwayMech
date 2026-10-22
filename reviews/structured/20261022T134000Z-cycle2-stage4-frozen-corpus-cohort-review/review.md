# Cycle 2 Stage 4 Full Frozen-Inventory Record and Cohort Review of 271 PathwayMech Maintained Records

- Review: 20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-22T13:15:00Z
- Finished UTC: 2026-10-22T13:40:00Z
- Reviewer: Antigravity (review-yaml-record + review-yaml-category) (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Completed a full-coverage frozen-inventory scientific record and cohort review of all 271 maintained pathway YAML records in data/pathways/*.yaml at Git commit e369fa425e64d4f794ce84e2fd71138a43660467 across all 8 identifier namespaces (MetaCyc: 140, gomodel: 86, WikiPathways: 12, PathBank: 11, GO: 10, Reactome: 6, KEGG: 3, MIBiG: 3; 7,684 participants, 1,597 reactions including 699 RHEA:* reactions, 14,393 mechanistic_edges, 7,042 references, and 615 source_mappings across 112 records exporting to 612 unique SSSOM rows). All 271 records pass closed LinkML schema validation, authority snapshot identifier/label checks, history validation (654 records), and edge-level evidence verification (14,393 mechanistic edges, 21,085 edge-level evidence items, 22,211 total evidence blocks). Identified 2 minor open findings (F-C2S4-001 across 16 MetaCyc records containing 28 untyped occurrences of 23 shared reaction CURIEs that are explicitly typed in sibling records, and F-C2S4-002 across all 56 MetaCyc records that omit category: molecular_activity on 279 catalytic reactions), preserved unedited for Cycle 2 Stage 5 grouped remediation.

## Scope And Provenance

Full frozen-inventory record and category review of all 271 maintained pathway records in data/pathways/*.yaml at Git base e369fa425e64d4f794ce84e2fd71138a43660467.

Selection: All files matching data/pathways/*.yaml in CultureBotAI/PathwayMech.
Coverage: full; 271 reviewed / 271 in the declared population.
Source: git_commit at Git base e369fa425e64d4f794ce84e2fd71138a43660467.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5901 | data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml | maintained | 2,3-dihydroxybenzoate biosynthesis (MetaCyc:PWY-5901) |
| MetaCyc:PWY0-42 | data/pathways/2-methylcitrate-cycle-i.yaml | maintained | 2-methylcitrate cycle I (MetaCyc:PWY0-42) |
| WikiPathways:WP5587 | data/pathways/2-phenylethanol-biosynthesis.yaml | maintained | 2-phenylethanol biosynthesis (WikiPathways:WP5587) |
| MetaCyc:PWY-2361 | data/pathways/3-oxoadipate-degradation.yaml | maintained | 3-oxoadipate degradation (MetaCyc:PWY-2361) |
| MetaCyc:PWY-6543 | data/pathways/4-aminobenzoate-biosynthesis-i.yaml | maintained | 4-aminobenzoate biosynthesis I (MetaCyc:PWY-6543) |
| gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY | data/pathways/4-aminobutyrate-degradation.yaml | maintained | 4-aminobutyrate degradation (gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY) |
| MetaCyc:PWY-6121 | data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml | maintained | 5-aminoimidazole ribonucleotide biosynthesis I (MetaCyc:PWY-6121) |
| MetaCyc:PWY-6122 | data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml | maintained | 5-aminoimidazole ribonucleotide biosynthesis II (MetaCyc:PWY-6122) |
| MetaCyc:PWY-8130 | data/pathways/5-prime-deoxyadenosine-degradation-i.yaml | maintained | 5'-deoxyadenosine degradation I (MetaCyc:PWY-8130) |
| MetaCyc:PWY-8131 | data/pathways/5-prime-deoxyadenosine-degradation-ii.yaml | maintained | 5'-deoxyadenosine degradation II (MetaCyc:PWY-8131) |
| gomodel:YeastPathways_PWY-6147 | data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml | maintained | 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (gomodel:YeastPathways_PWY-6147) |
| GO:0097288 | data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml | maintained | 7-cyano-7-deazaguanine biosynthetic process (GO:0097288) |
| MetaCyc:PWY0-1312 | data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml | maintained | acetate and ATP formation from acetyl-CoA I (MetaCyc:PWY0-1312) |
| MetaCyc:ACETOACETATE-DEG-PWY | data/pathways/acetoacetate-degradation.yaml | maintained | acetoacetate degradation (to acetyl CoA) (MetaCyc:ACETOACETATE-DEG-PWY) |
| WikiPathways:WP5019 | data/pathways/acetogenesis.yaml | maintained | Acetogenesis (WikiPathways:WP5019) |
| PathBank:SMP0002081 | data/pathways/adenine-and-adenosine-salvage-i-escherichia-coli.yaml | maintained | Adenine and Adenosine Salvage I (PathBank:SMP0002081) |
| MetaCyc:P121-PWY | data/pathways/adenine-and-adenosine-salvage-i.yaml | maintained | adenine and adenosine salvage I (MetaCyc:P121-PWY) |
| PathBank:SMP0002083 | data/pathways/adenine-and-adenosine-salvage-ii.yaml | maintained | Adenine and Adenosine Salvage II (PathBank:SMP0002083) |
| MetaCyc:PWY-6609 | data/pathways/adenine-and-adenosine-salvage-iii.yaml | maintained | adenine and adenosine salvage III (MetaCyc:PWY-6609) |
| gomodel:YeastPathways_PWY-7220-1 | data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml | maintained | adenosine deoxyribonucleotides de novo biosynthesis II (gomodel:YeastPathways_PWY-7220-1) |
| MetaCyc:SALVADEHYPOX-PWY | data/pathways/adenosine-nucleotides-degradation-ii.yaml | maintained | adenosine nucleotides degradation II (MetaCyc:SALVADEHYPOX-PWY) |
| gomodel:YeastPathways_PWY-7219 | data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml | maintained | adenosine ribonucleotides de novo biosynthesis (gomodel:YeastPathways_PWY-7219) |
| MetaCyc:PWY-5509 | data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml | maintained | adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I (MetaCyc:PWY-5509) |
| MetaCyc:PWY-7971 | data/pathways/adenosylcobinamide-gdp-salvage-i.yaml | maintained | adenosylcobinamide-GDP salvage from cobinamide I (MetaCyc:PWY-7971) |
| MetaCyc:PWY0-1241 | data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml | maintained | ADP-L-glycero-beta-D-manno-heptose biosynthesis (MetaCyc:PWY0-1241) |
| GO:0019270 | data/pathways/aerobactin-biosynthesis.yaml | maintained | aerobactin biosynthetic process (GO:0019270) |
| gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY | data/pathways/aerobic-glycerol-degradation.yaml | maintained | aerobic glycerol degradation (gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY) |
| MetaCyc:PWY0-41 | data/pathways/allantoin-degradation-iv-anaerobic.yaml | maintained | allantoin degradation IV (anaerobic) (MetaCyc:PWY0-41) |
| gomodel:YeastPathways_PWY-5694 | data/pathways/allantoin-degradation-to-glyoxylate-i.yaml | maintained | allantoin degradation to glyoxylate I (gomodel:YeastPathways_PWY-5694) |
| MetaCyc:PWY-5705 | data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml | maintained | allantoin degradation to glyoxylate III (MetaCyc:PWY-5705) |
| gomodel:YeastPathways_PWY-5697 | data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml | maintained | allantoin degradation to ureidoglycolate I (urea producing) (gomodel:YeastPathways_PWY-5697) |
| MetaCyc:GLCMANNANAUT-PWY | data/pathways/amino-sugar-superpathway.yaml | maintained | superpathway of N-acetylglucosamine, N-acetylmannosamine and N-acetylneuraminate degradation (MetaCyc:GLCMANNANAUT-PWY) |
| gomodel:YeastPathways_ASPBIO-PWY | data/pathways/aspartate-biosynthesis.yaml | maintained | aspartate biosynthesis (gomodel:YeastPathways_ASPBIO-PWY) |
| gomodel:YeastPathways_SO4ASSIM-PWY | data/pathways/assimilatory-sulfate-reduction.yaml | maintained | assimilatory sulfate reduction I (gomodel:YeastPathways_SO4ASSIM-PWY) |
| MetaCyc:PWY-5903 | data/pathways/bacillibactin-biosynthesis.yaml | maintained | bacillibactin biosynthesis (MetaCyc:PWY-5903) |
| PathBank:SMP0002123 | data/pathways/baesr-two-component-signal-transduction.yaml | maintained | BaeSR Two-Component Signal Transduction System (PathBank:SMP0002123) |
| MetaCyc:PWY-2503 | data/pathways/benzoate-degradation-i-aerobic.yaml | maintained | benzoate degradation I (aerobic) (MetaCyc:PWY-2503) |
| MetaCyc:PWY-1361 | data/pathways/benzoyl-coa-degradation-i-aerobic.yaml | maintained | benzoyl-CoA degradation I (aerobic) (MetaCyc:PWY-1361) |
| MetaCyc:CENTBENZCOA-PWY | data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml | maintained | benzoyl-CoA degradation II (anaerobic) (MetaCyc:CENTBENZCOA-PWY) |
| MetaCyc:P321-PWY | data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml | maintained | benzoyl-CoA degradation III (anaerobic) (MetaCyc:P321-PWY) |
| gomodel:YeastPathways_PWY-5760-1 | data/pathways/beta-alanine-biosynthesis-iv.yaml | maintained | beta-alanine biosynthesis IV (gomodel:YeastPathways_PWY-5760-1) |
| MetaCyc:BIOTIN-BIOSYNTHESIS-PWY | data/pathways/biotin-biosynthesis-i.yaml | maintained | biotin biosynthesis I (MetaCyc:BIOTIN-BIOSYNTHESIS-PWY) |
| MetaCyc:CALVIN-PWY | data/pathways/calvin-cycle.yaml | maintained | Calvin-Benson-Bassham cycle (MetaCyc:CALVIN-PWY) |
| GO:0043427 | data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml | maintained | carbon fixation by 3-hydroxypropionate cycle (GO:0043427) |
| gomodel:YeastPathways_PWY3O-4 | data/pathways/carnitine-shuttle.yaml | maintained | carnitine shuttle (gomodel:YeastPathways_PWY3O-4) |
| MetaCyc:PWY-5415 | data/pathways/catechol-degradation-i.yaml | maintained | catechol degradation I (meta-cleavage pathway) (MetaCyc:PWY-5415) |
| MetaCyc:PWY-5420 | data/pathways/catechol-degradation-ii.yaml | maintained | catechol degradation II (meta-cleavage pathway) (MetaCyc:PWY-5420) |
| MetaCyc:PWY-5417 | data/pathways/catechol-degradation-iii.yaml | maintained | catechol degradation III (ortho-cleavage pathway) (MetaCyc:PWY-5417) |
| MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | data/pathways/catechol-degradation-to-beta-ketoadipate.yaml | maintained | catechol degradation to β-ketoadipate (MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY) |
| gomodel:YeastPathways_PWY3O-15 | data/pathways/chitin-biosynthesis.yaml | maintained | chitin biosynthesis (gomodel:YeastPathways_PWY3O-15) |
| MetaCyc:ARO-PWY | data/pathways/chorismate-biosynthesis-i.yaml | maintained | chorismate biosynthesis I (MetaCyc:ARO-PWY) |
| MIBiG:BGC0000829 | data/pathways/chromobacterium-violaceum-violacein-biosynthetic-gene-cluster.yaml | maintained | Chromobacterium violaceum violacein biosynthetic gene cluster (MIBiG:BGC0000829) |
| MetaCyc:P2-PWY | data/pathways/citrate-lyase-activation.yaml | maintained | citrate lyase activation (MetaCyc:P2-PWY) |
| gomodel:YeastPathways_CITRUL-BIO2-PWY | data/pathways/citrulline-biosynthesis.yaml | maintained | citrulline biosynthesis (gomodel:YeastPathways_CITRUL-BIO2-PWY) |
| MetaCyc:COA-PWY | data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml | maintained | coenzyme A biosynthesis I (prokaryotic) (MetaCyc:COA-PWY) |
| GO:0036040 | data/pathways/curcumin-degradation.yaml | maintained | curcumin catabolic process (GO:0036040) |
| MetaCyc:CYANCAT-PWY | data/pathways/cyanate-degradation.yaml | maintained | cyanate degradation (MetaCyc:CYANCAT-PWY) |
| MetaCyc:DARABCAT-PWY | data/pathways/d-arabinose-degradation-i.yaml | maintained | D-arabinose degradation I (MetaCyc:DARABCAT-PWY) |
| MetaCyc:GALACTARDEG-PWY | data/pathways/d-galactarate-degradation-i.yaml | maintained | D-galactarate degradation I (MetaCyc:GALACTARDEG-PWY) |
| MetaCyc:GALACTCAT-PWY | data/pathways/d-galactonate-degradation.yaml | maintained | D-galactonate degradation (MetaCyc:GALACTCAT-PWY) |
| MetaCyc:GALACTUROCAT-PWY | data/pathways/d-galacturonate-degradation-i.yaml | maintained | D-galacturonate degradation I (MetaCyc:GALACTUROCAT-PWY) |
| MetaCyc:GLUCARDEG-PWY | data/pathways/d-glucarate-degradation-i.yaml | maintained | D-glucarate degradation I (MetaCyc:GLUCARDEG-PWY) |
| MetaCyc:XYLCAT-PWY | data/pathways/d-xylose-degradation-i.yaml | maintained | D-xylose degradation I (MetaCyc:XYLCAT-PWY) |
| MetaCyc:PWY-6376 | data/pathways/desferrioxamine-b-biosynthesis.yaml | maintained | desferrioxamine B biosynthesis (MetaCyc:PWY-6376) |
| KEGG:M00374 | data/pathways/dicarboxylate-hydroxybutyrate-cycle.yaml | maintained | Dicarboxylate-hydroxybutyrate cycle (KEGG:M00374) |
| gomodel:YeastPathways_PWY3O-1565 | data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml | maintained | dolichyl glucosyl phosphate biosynthesis (gomodel:YeastPathways_PWY3O-1565) |
| gomodel:YeastPathways_PWY3O-123 | data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml | maintained | dolichyl phosphate D-mannose biosynthesis (gomodel:YeastPathways_PWY3O-123) |
| GO:0019305 | data/pathways/dtdp-l-rhamnose-biosynthesis.yaml | maintained | dTDP-rhamnose biosynthetic process (GO:0019305) |
| MetaCyc:P101-PWY | data/pathways/ectoine-biosynthesis.yaml | maintained | ectoine biosynthesis (MetaCyc:P101-PWY) |
| KEGG:M00008 | data/pathways/entner-doudoroff-pathway.yaml | maintained | Entner-Doudoroff pathway, glucose-6P =&gt; glyceraldehyde-3P + pyruvate (KEGG:M00008) |
| gomodel:YeastPathways_PWY-5670-1 | data/pathways/epoxysqualene-biosynthesis.yaml | maintained | epoxysqualene biosynthesis (gomodel:YeastPathways_PWY-5670-1) |
| gomodel:YeastPathways_PWY-6075-1 | data/pathways/ergosterol-biosynthesis-i.yaml | maintained | ergosterol biosynthesis I (gomodel:YeastPathways_PWY-6075-1) |
| MetaCyc:PWY-7255 | data/pathways/ergothioneine-biosynthesis-i.yaml | maintained | ergothioneine biosynthesis I (bacteria) (MetaCyc:PWY-7255) |
| gomodel:YeastPathways_PWY3O-4300 | data/pathways/ethanol-degradation.yaml | maintained | ethanol degradation (gomodel:YeastPathways_PWY3O-4300) |
| MetaCyc:PWY0-1477 | data/pathways/ethanolamine-utilization.yaml | maintained | ethanolamine utilization (MetaCyc:PWY0-1477) |
| MetaCyc:PWY0-1280 | data/pathways/ethylene-glycol-degradation.yaml | maintained | ethylene glycol degradation (MetaCyc:PWY0-1280) |
| KEGG:M00373 | data/pathways/ethylmalonyl-coa-pathway.yaml | maintained | Ethylmalonyl pathway (KEGG:M00373) |
| gomodel:YeastPathways_FASYN-ELONG2-PWY | data/pathways/fatty-acid-elongation.yaml | maintained | fatty acid elongation (gomodel:YeastPathways_FASYN-ELONG2-PWY) |
| gomodel:YeastPathways_YEAST-FAO-PWY | data/pathways/fatty-acid-oxidation-pathway.yaml | maintained | fatty acid oxidation pathway (gomodel:YeastPathways_YEAST-FAO-PWY) |
| MetaCyc:RIBOSYN2-PWY | data/pathways/flavin-biosynthesis-i.yaml | maintained | flavin biosynthesis I (MetaCyc:RIBOSYN2-PWY) |
| gomodel:YeastPathways_PWY3O-697 | data/pathways/folate-interconversions.yaml | maintained | folate interconversions (gomodel:YeastPathways_PWY3O-697) |
| gomodel:YeastPathways_PWY-1801-1 | data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml | maintained | formaldehyde oxidation II (glutathione-dependent) (gomodel:YeastPathways_PWY-1801-1) |
| MetaCyc:PWY0-521 | data/pathways/fructoselysine-and-psicoselysine-degradation.yaml | maintained | fructoselysine and psicoselysine degradation (MetaCyc:PWY0-521) |
| GO:1901281 | data/pathways/fructoselysine-catabolic-process.yaml | maintained | fructoselysine catabolic process (GO:1901281) |
| gomodel:YeastPathways_YEAST-GALACT-METAB-PWY | data/pathways/galactose-degradation.yaml | maintained | galactose degradation (gomodel:YeastPathways_YEAST-GALACT-METAB-PWY) |
| MetaCyc:GALLATE-DEGRADATION-II-PWY | data/pathways/gallate-degradation-i.yaml | maintained | gallate degradation I (MetaCyc:GALLATE-DEGRADATION-II-PWY) |
| MetaCyc:GALLATE-DEGRADATION-I-PWY | data/pathways/gallate-degradation-ii.yaml | maintained | gallate degradation II (MetaCyc:GALLATE-DEGRADATION-I-PWY) |
| MetaCyc:PWY-6223 | data/pathways/gentisate-degradation-i.yaml | maintained | gentisate degradation I (MetaCyc:PWY-6223) |
| gomodel:YeastPathways_GLUCONEO-PWY-1 | data/pathways/gluconeogenesis-i.yaml | maintained | gluconeogenesis I (gomodel:YeastPathways_GLUCONEO-PWY-1) |
| WikiPathways:WP556 | data/pathways/glutamate-degradation-i.yaml | maintained | Glutamate degradation I (WikiPathways:WP556) |
| MetaCyc:PWY-5177 | data/pathways/glutaryl-coa-degradation.yaml | maintained | glutaryl-CoA degradation (MetaCyc:PWY-5177) |
| MetaCyc:GLUTATHIONESYN-PWY | data/pathways/glutathione-biosynthesis.yaml | maintained | glutathione biosynthesis (MetaCyc:GLUTATHIONESYN-PWY) |
| gomodel:YeastPathways_PWYQT-4432 | data/pathways/glutathione-degradation.yaml | maintained | glutathione degradation (gomodel:YeastPathways_PWYQT-4432) |
| WikiPathways:WP392 | data/pathways/glutathione-glutaredoxin-redox-reaction.yaml | maintained | Glutathione-glutaredoxin redox reaction (WikiPathways:WP392) |
| gomodel:YeastPathways_PWY3O-48 | data/pathways/glycerol-biosynthesis.yaml | maintained | glycerol biosynthesis (gomodel:YeastPathways_PWY3O-48) |
| MetaCyc:GLYCEROLMETAB-PWY | data/pathways/glycerol-degradation-v.yaml | maintained | glycerol degradation V (MetaCyc:GLYCEROLMETAB-PWY) |
| gomodel:YeastPathways_GLYCLEAV-PWY | data/pathways/glycine-cleavage.yaml | maintained | glycine cleavage (gomodel:YeastPathways_GLYCLEAV-PWY) |
| WikiPathways:WP478 | data/pathways/glycogen-catabolism.yaml | maintained | Glycogen catabolism (WikiPathways:WP478) |
| gomodel:YeastPathways_GLYCOLYSIS | data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml | maintained | glycolysis I (from glucose 6-phosphate) (gomodel:YeastPathways_GLYCOLYSIS) |
| MetaCyc:PWY-5744 | data/pathways/glyoxylate-assimilation.yaml | maintained | glyoxylate assimilation (MetaCyc:PWY-5744) |
| MetaCyc:GLYOXYLATE-BYPASS | data/pathways/glyoxylate-cycle.yaml | maintained | glyoxylate cycle (MetaCyc:GLYOXYLATE-BYPASS) |
| MetaCyc:PWY-6579 | data/pathways/guanine-and-guanosine-salvage.yaml | maintained | superpathway of guanine and guanosine salvage (MetaCyc:PWY-6579) |
| gomodel:YeastPathways_PWY-7221 | data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml | maintained | guanosine ribonucleotides de novo biosynthesis (gomodel:YeastPathways_PWY-7221) |
| gomodel:YeastPathways_HEME-BIOSYNTHESIS-II | data/pathways/heme-biosynthesis-i-aerobic.yaml | maintained | heme b biosynthesis I (aerobic) (gomodel:YeastPathways_HEME-BIOSYNTHESIS-II) |
| gomodel:YeastPathways_HEXPPSYN-PWY-2 | data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml | maintained | hexaprenyl diphosphate biosynthesis (gomodel:YeastPathways_HEXPPSYN-PWY-2) |
| gomodel:YeastPathways_HOMOCYS-CYS-CONVERT | data/pathways/homocysteine-and-cysteine-interconversion.yaml | maintained | homocysteine and cysteine interconversion (gomodel:YeastPathways_HOMOCYS-CYS-CONVERT) |
| GO:1902000 | data/pathways/homogentisate-degradation.yaml | maintained | homogentisate catabolic process (GO:1902000) |
| MetaCyc:PWY-5789 | data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml | maintained | 3-hydroxypropanoate/4-hydroxybutanate cycle (MetaCyc:PWY-5789) |
| MetaCyc:PWY-6123 | data/pathways/inosine-5-phosphate-biosynthesis-i.yaml | maintained | inosine-5'-phosphate biosynthesis I (MetaCyc:PWY-6123) |
| MetaCyc:PWY-6124 | data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml | maintained | inosine-5'-phosphate biosynthesis II (MetaCyc:PWY-6124) |
| gomodel:YeastPathways_PWY3O-402 | data/pathways/inositol-phosphate-biosynthesis.yaml | maintained | inositol phosphate biosynthesis (gomodel:YeastPathways_PWY3O-402) |
| WikiPathways:WP178 | data/pathways/isoleucine-degradation.yaml | maintained | Isoleucine degradation (WikiPathways:WP178) |
| MetaCyc:PWY0-1338 | data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml | maintained | polymyxin resistance (MetaCyc:PWY0-1338) |
| MetaCyc:ARABCAT-PWY | data/pathways/l-arabinose-degradation-i.yaml | maintained | L-arabinose degradation I (MetaCyc:ARABCAT-PWY) |
| MetaCyc:ARGSYN-PWY | data/pathways/l-arginine-biosynthesis-i.yaml | maintained | L-arginine biosynthesis I (via L-ornithine) (MetaCyc:ARGSYN-PWY) |
| gomodel:YeastPathways_ARGSYNBSUB-PWY | data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml | maintained | L-arginine biosynthesis II (acetyl cycle) (gomodel:YeastPathways_ARGSYNBSUB-PWY) |
| MetaCyc:AST-PWY | data/pathways/l-arginine-degradation-ii-ast-pathway.yaml | maintained | L-arginine degradation II (AST pathway) (MetaCyc:AST-PWY) |
| MetaCyc:ARGDEG-III-PWY | data/pathways/l-arginine-degradation-iv.yaml | maintained | L-arginine degradation IV (arginine decarboxylase/agmatine deiminase pathway) (MetaCyc:ARGDEG-III-PWY) |
| MetaCyc:ARGDEGRAD-PWY | data/pathways/l-arginine-degradation-v.yaml | maintained | L-arginine degradation V (arginine deiminase pathway) (MetaCyc:ARGDEGRAD-PWY) |
| MetaCyc:PWY0-301 | data/pathways/l-ascorbate-degradation-i.yaml | maintained | L-ascorbate degradation I (bacterial, anaerobic) (MetaCyc:PWY0-301) |
| gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1 | data/pathways/l-asparagine-biosynthesis-i.yaml | maintained | L-asparagine biosynthesis I (gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1) |
| gomodel:YeastPathways_ASPARAGINE-DEG2-PWY | data/pathways/l-asparagine-degradation.yaml | maintained | asparagine degradation (gomodel:YeastPathways_ASPARAGINE-DEG2-PWY) |
| PathBank:SMP0002051 | data/pathways/l-carnitine-degradation-i.yaml | maintained | L-Carnitine Degradation I (PathBank:SMP0002051) |
| MetaCyc:CYSTSYN-PWY | data/pathways/l-cysteine-biosynthesis-i.yaml | maintained | L-cysteine biosynthesis I (MetaCyc:CYSTSYN-PWY) |
| gomodel:YeastPathways_HOMOCYSDEGR-PWY-1 | data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml | maintained | L-cysteine biosynthesis III (from L-homocysteine) (gomodel:YeastPathways_HOMOCYSDEGR-PWY-1) |
| MetaCyc:FUCCAT-PWY | data/pathways/l-fucose-degradation-i.yaml | maintained | L-fucose degradation I (MetaCyc:FUCCAT-PWY) |
| MetaCyc:HISTSYN-PWY | data/pathways/l-histidine-biosynthesis.yaml | maintained | L-histidine biosynthesis (MetaCyc:HISTSYN-PWY) |
| gomodel:YeastPathways_PWY-5344 | data/pathways/l-homocysteine-biosynthesis.yaml | maintained | L-homocysteine biosynthesis (gomodel:YeastPathways_PWY-5344) |
| MetaCyc:HOMOSERSYN-PWY | data/pathways/l-homoserine-biosynthesis.yaml | maintained | L-homoserine biosynthesis (MetaCyc:HOMOSERSYN-PWY) |
| MetaCyc:ILEUSYN-PWY | data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml | maintained | L-isoleucine biosynthesis I (from threonine) (MetaCyc:ILEUSYN-PWY) |
| MetaCyc:LEUSYN-PWY | data/pathways/l-leucine-biosynthesis.yaml | maintained | L-leucine biosynthesis (MetaCyc:LEUSYN-PWY) |
| MetaCyc:DAPLYSINESYN-PWY | data/pathways/l-lysine-biosynthesis-i.yaml | maintained | L-lysine biosynthesis I (MetaCyc:DAPLYSINESYN-PWY) |
| gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2 | data/pathways/l-lysine-biosynthesis-iv.yaml | maintained | L-lysine biosynthesis IV (gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2) |
| MetaCyc:LYXMET-PWY | data/pathways/l-lyxose-degradation.yaml | maintained | L-lyxose degradation (MetaCyc:LYXMET-PWY) |
| MetaCyc:HOMOSER-METSYN-PWY | data/pathways/l-methionine-biosynthesis-i.yaml | maintained | L-methionine biosynthesis I (MetaCyc:HOMOSER-METSYN-PWY) |
| MetaCyc:GLUTORN-PWY | data/pathways/l-ornithine-biosynthesis-i.yaml | maintained | L-ornithine biosynthesis I (MetaCyc:GLUTORN-PWY) |
| MetaCyc:PHESYN | data/pathways/l-phenylalanine-biosynthesis-i.yaml | maintained | L-phenylalanine biosynthesis I (MetaCyc:PHESYN) |
| MetaCyc:PROSYN-PWY | data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml | maintained | L-proline biosynthesis I (from L-glutamate) (MetaCyc:PROSYN-PWY) |
| gomodel:YeastPathways_PROUT-PWY | data/pathways/l-proline-degradation.yaml | maintained | L-proline degradation (gomodel:YeastPathways_PROUT-PWY) |
| MetaCyc:RHAMCAT-PWY | data/pathways/l-rhamnose-degradation-i.yaml | maintained | L-rhamnose degradation I (MetaCyc:RHAMCAT-PWY) |
| MetaCyc:SERSYN-PWY | data/pathways/l-serine-biosynthesis-i.yaml | maintained | L-serine biosynthesis I (MetaCyc:SERSYN-PWY) |
| MetaCyc:HOMOSER-THRESYN-PWY | data/pathways/l-threonine-biosynthesis.yaml | maintained | L-threonine biosynthesis (MetaCyc:HOMOSER-THRESYN-PWY) |
| MetaCyc:THRDLCTCAT-PWY | data/pathways/l-threonine-degradation-iii.yaml | maintained | L-threonine degradation III (to methylglyoxal) (MetaCyc:THRDLCTCAT-PWY) |
| MetaCyc:TRPSYN-PWY | data/pathways/l-tryptophan-biosynthesis.yaml | maintained | L-tryptophan biosynthesis (MetaCyc:TRPSYN-PWY) |
| gomodel:YeastPathways_PWY-5651 | data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml | maintained | L-tryptophan degradation to 2-amino-3-carboxymuconate semialdehyde (gomodel:YeastPathways_PWY-5651) |
| MetaCyc:TYRSYN | data/pathways/l-tyrosine-biosynthesis-i.yaml | maintained | L-tyrosine biosynthesis I (MetaCyc:TYRSYN) |
| gomodel:YeastPathways_PWY3O-4108 | data/pathways/l-tyrosine-degradation-iii.yaml | maintained | L-tyrosine degradation III (gomodel:YeastPathways_PWY3O-4108) |
| MetaCyc:VALSYN-PWY | data/pathways/l-valine-biosynthesis.yaml | maintained | L-valine biosynthesis (MetaCyc:VALSYN-PWY) |
| gomodel:YeastPathways_PWY3O-4112 | data/pathways/leucine-degradation.yaml | maintained | leucine degradation (gomodel:YeastPathways_PWY3O-4112) |
| MIBiG:BGC0002072 | data/pathways/linearmycin-biosynthetic-gene-cluster.yaml | maintained | linearmycin A and related metabolites biosynthetic gene cluster (MIBiG:BGC0002072) |
| gomodel:6882d2b800000609 | data/pathways/lipid-iva-biosynthesis.yaml | maintained | lipid IV(A) biosynthesis pathway (gomodel:6882d2b800000609) |
| MetaCyc:PWY0-501 | data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml | maintained | lipoate biosynthesis and incorporation I (MetaCyc:PWY0-501) |
| gomodel:YeastPathways_PWY3O-1743 | data/pathways/mannose-degradation.yaml | maintained | mannose degradation (gomodel:YeastPathways_PWY3O-1743) |
| MetaCyc:PWY0-1300 | data/pathways/mannosylglycerate-degradation.yaml | maintained | 2-O-alpha-mannosyl-D-glycerate degradation (MetaCyc:PWY0-1300) |
| MetaCyc:METH-ACETATE-PWY | data/pathways/methanogenesis-from-acetate.yaml | maintained | methanogenesis from acetate (MetaCyc:METH-ACETATE-PWY) |
| MetaCyc:METHANOGENESIS-PWY | data/pathways/methanogenesis-from-h2-and-co2.yaml | maintained | methanogenesis from H2 and CO2 (MetaCyc:METHANOGENESIS-PWY) |
| gomodel:YeastPathways_PWY3O-64 | data/pathways/methionine-salvage-pathway.yaml | maintained | methionine salvage pathway (gomodel:YeastPathways_PWY3O-64) |
| MetaCyc:NONMEVIPP-PWY | data/pathways/methylerythritol-phosphate-pathway-i.yaml | maintained | methylerythritol phosphate pathway I (MetaCyc:NONMEVIPP-PWY) |
| gomodel:YeastPathways_PWY-901 | data/pathways/methylglyoxal-catabolism.yaml | maintained | methylglyoxal catabolism (gomodel:YeastPathways_PWY-901) |
| MetaCyc:PWY-5386 | data/pathways/methylglyoxal-degradation-i.yaml | maintained | methylglyoxal degradation I (MetaCyc:PWY-5386) |
| MetaCyc:PWY-5453 | data/pathways/methylglyoxal-degradation-iii.yaml | maintained | methylglyoxal degradation III (MetaCyc:PWY-5453) |
| PathBank:SMP0002077 | data/pathways/methylphosphonate-degradation-i.yaml | maintained | Methylphosphonate Degradation I (PathBank:SMP0002077) |
| MetaCyc:PWY-6048 | data/pathways/methylthiopropanoate-degradation-i.yaml | maintained | methylthiopropanoate degradation I (cleavage) (MetaCyc:PWY-6048) |
| gomodel:YeastPathways_IPPSYN-PWY | data/pathways/mevalonate-pathway.yaml | maintained | mevalonate pathway (gomodel:YeastPathways_IPPSYN-PWY) |
| MetaCyc:PWY-6823 | data/pathways/molybdenum-cofactor-biosynthesis.yaml | maintained | molybdenum cofactor biosynthesis (MetaCyc:PWY-6823) |
| Reactome:R-MTU-936721 | data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml | maintained | Cysteine synthesis from O-acetylserine (Reactome:R-MTU-936721) |
| Reactome:R-MTU-936654 | data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml | maintained | Cysteine synthesis from O-phosphoserine (Reactome:R-MTU-936654) |
| Reactome:R-MTU-936635 | data/pathways/mycobacterium-sulfate-assimilation.yaml | maintained | Sulfate assimilation (Reactome:R-MTU-936635) |
| Reactome:R-MTU-868688 | data/pathways/mycobacterium-trehalose-biosynthesis.yaml | maintained | Mycobacterium tuberculosis trehalose biosynthesis (Reactome:R-MTU-868688) |
| Reactome:R-MTU-879299 | data/pathways/mycothiol-biosynthesis.yaml | maintained | Mycothiol biosynthesis (Reactome:R-MTU-879299) |
| Reactome:R-MTU-879325 | data/pathways/mycothiol-catabolism.yaml | maintained | mycothiol S-conjugate catabolism (Reactome:R-MTU-879325) |
| gomodel:YeastPathways_PWY-2301 | data/pathways/myo-inositol-biosynthesis.yaml | maintained | myo-inositol biosynthesis (gomodel:YeastPathways_PWY-2301) |
| MetaCyc:PWY-8383 | data/pathways/myxochelin-a-and-b-biosynthesis.yaml | maintained | myxochelin A and B biosynthesis (MetaCyc:PWY-8383) |
| MetaCyc:GLUAMCAT-PWY | data/pathways/n-acetylglucosamine-degradation-i.yaml | maintained | N-acetylglucosamine degradation I (MetaCyc:GLUAMCAT-PWY) |
| gomodel:YeastPathways_PWY-5653 | data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml | maintained | NAD biosynthesis from 2-amino-3-carboxymuconate semialdehyde (gomodel:YeastPathways_PWY-5653) |
| MetaCyc:PYRIDNUCSYN-PWY | data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml | maintained | NAD de novo biosynthesis I (from aspartate) (MetaCyc:PYRIDNUCSYN-PWY) |
| MetaCyc:NADPHOS-DEPHOS-PWY | data/pathways/nad-phosphorylation-and-dephosphorylation.yaml | maintained | NAD phosphorylation and dephosphorylation (MetaCyc:NADPHOS-DEPHOS-PWY) |
| MetaCyc:PYRIDNUCSAL-PWY | data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml | maintained | NAD salvage pathway I (PNC VI cycle) (MetaCyc:PYRIDNUCSAL-PWY) |
| gomodel:YeastPathways_PWY3O-4106 | data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml | maintained | NAD salvage pathway IV (from nicotinamide riboside) (gomodel:YeastPathways_PWY3O-4106) |
| WikiPathways:WP171 | data/pathways/nad-salvage-pathway-v.yaml | maintained | NAD salvage pathway V (WikiPathways:WP171) |
| MetaCyc:PWY-6993 | data/pathways/nicotine-degradation-ii.yaml | maintained | nicotine degradation II (pyrrolidine pathway) (MetaCyc:PWY-6993) |
| MetaCyc:DENITRIFICATION-PWY | data/pathways/nitrate-reduction-i-denitrification.yaml | maintained | nitrate reduction I (denitrification) (MetaCyc:DENITRIFICATION-PWY) |
| MetaCyc:PWY0-1352 | data/pathways/nitrate-reduction-viii.yaml | maintained | nitrate reduction VIII (dissimilatory) (MetaCyc:PWY0-1352) |
| gomodel:YeastPathways_PWY3O-5268 | data/pathways/oleate-biosynthesis.yaml | maintained | oleate biosynthesis (gomodel:YeastPathways_PWY3O-5268) |
| gomodel:YeastPathways_PWY3O-1801 | data/pathways/palmitoleate-biosynthesis.yaml | maintained | palmitoleate biosynthesis (gomodel:YeastPathways_PWY3O-1801) |
| MetaCyc:NONOXIPENT-PWY | data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml | maintained | pentose phosphate pathway (non-oxidative branch) I (MetaCyc:NONOXIPENT-PWY) |
| MetaCyc:PWY-8178 | data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml | maintained | pentose phosphate pathway (non-oxidative branch) II (MetaCyc:PWY-8178) |
| MetaCyc:OXIDATIVEPENT-PWY | data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml | maintained | pentose phosphate pathway (oxidative branch) I (MetaCyc:OXIDATIVEPENT-PWY) |
| WikiPathways:WP5060 | data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml | maintained | Peptidoglycan cytoplasmic synthesis and recycling pathways (WikiPathways:WP5060) |
| gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION | data/pathways/periplasmic-nad-degradation.yaml | maintained | periplasmic NAD degradation (gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION) |
| MetaCyc:PWY-6289 | data/pathways/petrobactin-biosynthesis.yaml | maintained | petrobactin biosynthesis (MetaCyc:PWY-6289) |
| MetaCyc:PWY0-321 | data/pathways/phenylacetate-degradation-i-aerobic.yaml | maintained | phenylacetate degradation I (aerobic) (MetaCyc:PWY0-321) |
| gomodel:YeastPathways_PWY3O-4153 | data/pathways/phenylalanine-biosynthesis.yaml | maintained | phenylalanine biosynthesis (gomodel:YeastPathways_PWY3O-4153) |
| MetaCyc:2PHENDEG-PWY | data/pathways/phenylethylamine-degradation-i.yaml | maintained | phenylethylamine degradation I (MetaCyc:2PHENDEG-PWY) |
| MetaCyc:PWY-6534 | data/pathways/phenylethylamine-degradation-ii.yaml | maintained | phenylethylamine degradation II (MetaCyc:PWY-6534) |
| MetaCyc:PWY0-1277 | data/pathways/phenylpropanoate-and-hydroxyphenylpropanoate-degradation.yaml | maintained | 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation (MetaCyc:PWY0-1277) |
| gomodel:YeastPathways_PWY3O-6407 | data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml | maintained | phosphatidate biosynthesis I (the dihydroxyacetone pathway) (gomodel:YeastPathways_PWY3O-6407) |
| gomodel:YeastPathways_PWY3O-6499 | data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml | maintained | phosphatidate biosynthesis II (the glycerol-3-phosphate pathway) (gomodel:YeastPathways_PWY3O-6499) |
| gomodel:YeastPathways_PWY3O-450 | data/pathways/phosphatidylcholine-biosynthesis-i.yaml | maintained | phosphatidylcholine biosynthesis I (gomodel:YeastPathways_PWY3O-450) |
| gomodel:YeastPathways_PWY-5669 | data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml | maintained | phosphatidylethanolamine biosynthesis I (gomodel:YeastPathways_PWY-5669) |
| gomodel:YeastPathways_PWY3O-242 | data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml | maintained | phosphatidylinositol phosphate biosynthesis (gomodel:YeastPathways_PWY3O-242) |
| gomodel:YeastPathways_PWY3O-259 | data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml | maintained | phospholipid biosynthesis II (Kennedy pathway) (gomodel:YeastPathways_PWY3O-259) |
| gomodel:YeastPathways_PHOSLIPSYN2-PWY-1 | data/pathways/phospholipid-biosynthesis.yaml | maintained | phospholipid biosynthesis (gomodel:YeastPathways_PHOSLIPSYN2-PWY-1) |
| WikiPathways:WP71 | data/pathways/phospholipids-degradation.yaml | maintained | Phospholipids degradation (WikiPathways:WP71) |
| MetaCyc:PANTO-PWY | data/pathways/phosphopantothenate-biosynthesis-i.yaml | maintained | phosphopantothenate biosynthesis I (MetaCyc:PANTO-PWY) |
| MetaCyc:PWY1-3 | data/pathways/polyhydroxybutanoate-biosynthesis.yaml | maintained | polyhydroxybutanoate biosynthesis (MetaCyc:PWY1-3) |
| MetaCyc:PPGPPMET-PWY | data/pathways/ppgpp-metabolism.yaml | maintained | ppGpp metabolism (MetaCyc:PPGPPMET-PWY) |
| MetaCyc:P184-PWY | data/pathways/protocatechuate-meta-cleavage.yaml | maintained | protocatechuate degradation I (meta-cleavage pathway) (MetaCyc:P184-PWY) |
| GO:0019618 | data/pathways/protocatechuate-ortho-cleavage.yaml | maintained | protocatechuate catabolic process, ortho-cleavage (GO:0019618) |
| MetaCyc:PWY-6336 | data/pathways/protocatechuate-para-cleavage.yaml | maintained | protocatechuate degradation III (para-cleavage pathway) (MetaCyc:PWY-6336) |
| MetaCyc:PWY-6019 | data/pathways/pseudouridine-degradation.yaml | maintained | pseudouridine degradation (MetaCyc:PWY-6019) |
| PathBank:SMP0002089 | data/pathways/purine-deoxyribonucleosides-degradation.yaml | maintained | Purine Deoxyribonucleosides Degradation (PathBank:SMP0002089) |
| PathBank:SMP0002067 | data/pathways/putrescine-degradation-ii.yaml | maintained | Putrescine Degradation II (PathBank:SMP0002067) |
| GO:0042864 | data/pathways/pyochelin-biosynthesis.yaml | maintained | pyochelin biosynthetic process (GO:0042864) |
| MetaCyc:PYRIDOXSYN-PWY | data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml | maintained | pyridoxal 5'-phosphate biosynthesis I (MetaCyc:PYRIDOXSYN-PWY) |
| MetaCyc:PLPSAL-PWY | data/pathways/pyridoxal-5-phosphate-salvage-i.yaml | maintained | pyridoxal 5'-phosphate salvage I (MetaCyc:PLPSAL-PWY) |
| MetaCyc:PWY-7181 | data/pathways/pyrimidine-deoxyribonucleosides-degradation.yaml | maintained | pyrimidine deoxyribonucleosides degradation (MetaCyc:PWY-7181) |
| GO:0010139 | data/pathways/pyrimidine-deoxyribonucleotide-salvage.yaml | maintained | pyrimidine deoxyribonucleotide salvage (GO:0010139) |
| PathBank:SMP0002038 | data/pathways/pyrimidine-ribonucleosides-degradation.yaml | maintained | Pyrimidine Ribonucleosides Degradation (PathBank:SMP0002038) |
| gomodel:YeastPathways_PYRUVDEHYD-PWY | data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml | maintained | pyruvate decarboxylation to acetyl CoA (gomodel:YeastPathways_PYRUVDEHYD-PWY) |
| gomodel:YeastPathways_PWY3O-440 | data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml | maintained | pyruvate fermentation to acetoin III (gomodel:YeastPathways_PWY3O-440) |
| MetaCyc:PWY-7545 | data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml | maintained | pyruvate to cytochrome bd oxidase electron transfer (MetaCyc:PWY-7545) |
| MetaCyc:QUINATEDEG-PWY | data/pathways/quinate-degradation-i.yaml | maintained | quinate degradation I (MetaCyc:QUINATEDEG-PWY) |
| MetaCyc:PWY-6416 | data/pathways/quinate-degradation-ii.yaml | maintained | quinate degradation II (MetaCyc:PWY-6416) |
| PathBank:SMP0002406 | data/pathways/riboneogenesis.yaml | maintained | Riboneogenesis (PathBank:SMP0002406) |
| MetaCyc:RIBOKIN-PWY | data/pathways/ribose-phosphorylation.yaml | maintained | ribose phosphorylation (MetaCyc:RIBOKIN-PWY) |
| MetaCyc:PWY-6151 | data/pathways/s-adenosyl-l-methionine-cycle-i.yaml | maintained | S-adenosyl-L-methionine cycle I (MetaCyc:PWY-6151) |
| gomodel:YeastPathways_PWY-5041 | data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml | maintained | S-adenosyl-L-methionine cycle II (gomodel:YeastPathways_PWY-5041) |
| MetaCyc:PWY-8132 | data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml | maintained | S-methyl-5-thio-α-D-ribose 1-phosphate degradation III (MetaCyc:PWY-8132) |
| gomodel:YeastPathways_YEAST-RNT-SALV | data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml | maintained | salvage pathways of pyrimidine ribonucleotides (gomodel:YeastPathways_YEAST-RNT-SALV) |
| MetaCyc:PWY0-1517 | data/pathways/sedoheptulose-bisphosphate-bypass.yaml | maintained | sedoheptulose bisphosphate bypass (MetaCyc:PWY0-1517) |
| MetaCyc:SHIKIMATEDEG-PWY | data/pathways/shikimate-degradation-i.yaml | maintained | shikimate degradation I (MetaCyc:SHIKIMATEDEG-PWY) |
| MetaCyc:PWY-6419 | data/pathways/shikimate-degradation-ii.yaml | maintained | shikimate degradation II (MetaCyc:PWY-6419) |
| gomodel:YeastPathways_PWY-5194-1 | data/pathways/siroheme-biosynthesis.yaml | maintained | siroheme biosynthesis (gomodel:YeastPathways_PWY-5194-1) |
| PathBank:SMP0002097 | data/pathways/spermidine-biosynthesis-and-metabolism-escherichia-coli.yaml | maintained | Spermidine Biosynthesis and Metabolism (PathBank:SMP0002097) |
| gomodel:YeastPathways_BSUBPOLYAMSYN-PWY | data/pathways/spermidine-biosynthesis-i.yaml | maintained | spermidine biosynthesis I (gomodel:YeastPathways_BSUBPOLYAMSYN-PWY) |
| gomodel:YeastPathways_ARGSPECAT-PWY | data/pathways/spermine-biosynthesis.yaml | maintained | spermine biosynthesis (gomodel:YeastPathways_ARGSPECAT-PWY) |
| gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1 | data/pathways/sphingolipid-biosynthesis-yeast.yaml | maintained | sphingolipid biosynthesis (yeast) (gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1) |
| MIBiG:BGC0000852 | data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml | maintained | Sporosarcina pasteurii ectoine biosynthetic gene cluster (MIBiG:BGC0000852) |
| MetaCyc:PWY-7990 | data/pathways/staphyloferrin-a-biosynthesis.yaml | maintained | staphyloferrin A biosynthesis (MetaCyc:PWY-7990) |
| MetaCyc:PWY-8008 | data/pathways/staphyloferrin-b-biosynthesis.yaml | maintained | staphyloferrin B biosynthesis (MetaCyc:PWY-8008) |
| MetaCyc:PWY0-43 | data/pathways/succinate-to-propanoate.yaml | maintained | conversion of succinate to propanoate (MetaCyc:PWY0-43) |
| gomodel:YeastPathways_PWY-5340 | data/pathways/sulfate-activation-for-sulfonation.yaml | maintained | sulfate activation (for sulfonation) (gomodel:YeastPathways_PWY-5340) |
| MetaCyc:PWY-7446 | data/pathways/sulfoquinovose-degradation-i.yaml | maintained | sulfoquinovose degradation I (MetaCyc:PWY-7446) |
| MetaCyc:PWY-7722 | data/pathways/sulfoquinovose-degradation-ii.yaml | maintained | sulfoquinovose degradation II (MetaCyc:PWY-7722) |
| gomodel:YeastPathways_DETOX1-PWY | data/pathways/superoxide-radicals-degradation.yaml | maintained | superoxide radicals degradation (gomodel:YeastPathways_DETOX1-PWY) |
| MetaCyc:PWY-5838 | data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml | maintained | superpathway of menaquinol-8 biosynthesis I (MetaCyc:PWY-5838) |
| WikiPathways:WP296 | data/pathways/tca-cycle-detailed.yaml | maintained | TCA cycle - detailed (WikiPathways:WP296) |
| gomodel:YeastPathways_PWY-6614 | data/pathways/tetrahydrofolate-biosynthesis.yaml | maintained | tetrahydrofolate biosynthesis (gomodel:YeastPathways_PWY-6614) |
| MetaCyc:PWY0-1433 | data/pathways/tetrahydromonapterin-biosynthesis.yaml | maintained | tetrahydromonapterin biosynthesis (MetaCyc:PWY0-1433) |
| gomodel:YeastPathways_PWY3O-50 | data/pathways/tetrapyrrole-biosynthesis.yaml | maintained | tetrapyrrole biosynthesis (gomodel:YeastPathways_PWY3O-50) |
| gomodel:YeastPathways_PWY3O-17 | data/pathways/thiamine-biosynthesis.yaml | maintained | thiamine biosynthesis (gomodel:YeastPathways_PWY3O-17) |
| MetaCyc:THISYN-PWY | data/pathways/thiamine-diphosphate-biosynthesis-i.yaml | maintained | superpathway of thiamine diphosphate biosynthesis I (MetaCyc:THISYN-PWY) |
| MetaCyc:THIOREDOX-PWY | data/pathways/thioredoxin-pathway.yaml | maintained | thioredoxin pathway (MetaCyc:THIOREDOX-PWY) |
| PathBank:SMP0000992 | data/pathways/threonine-biosynthesis-from-aspartate-escherichia-coli.yaml | maintained | Secondary Metabolites: Threonine Biosynthesis from Aspartate (PathBank:SMP0000992) |
| gomodel:YeastPathways_THREOCAT2-PWY | data/pathways/threonine-degradation.yaml | maintained | threonine degradation (gomodel:YeastPathways_THREOCAT2-PWY) |
| gomodel:YeastPathways_PWY-5123 | data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml | maintained | trans, trans-farnesyl diphosphate biosynthesis (gomodel:YeastPathways_PWY-5123) |
| MetaCyc:TRESYN-PWY | data/pathways/trehalose-biosynthesis-i.yaml | maintained | trehalose biosynthesis I (MetaCyc:TRESYN-PWY) |
| WikiPathways:WP266 | data/pathways/triglyceride-biosynthesis.yaml | maintained | Triglyceride biosynthesis (WikiPathways:WP266) |
| gomodel:YeastPathways_PWY3O-214 | data/pathways/tryptophan-degradation.yaml | maintained | tryptophan degradation (gomodel:YeastPathways_PWY3O-214) |
| gomodel:YeastPathways_PWY3O-4120 | data/pathways/tyrosine-biosynthesis.yaml | maintained | tyrosine biosynthesis (gomodel:YeastPathways_PWY3O-4120) |
| WikiPathways:WP287 | data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml | maintained | Ubiquinol-6 biosynthesis from 4-hydroxybenzoate (WikiPathways:WP287) |
| gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY | data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml | maintained | UDP-N-acetylglucosamine biosynthesis (gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY) |
| MetaCyc:PWY-5686 | data/pathways/ump-biosynthesis-i.yaml | maintained | UMP biosynthesis I (MetaCyc:PWY-5686) |
| MetaCyc:PWY0-1471 | data/pathways/uracil-degradation-iii.yaml | maintained | uracil degradation III (MetaCyc:PWY0-1471) |
| gomodel:YeastPathways_PWY-5703 | data/pathways/urea-degradation-i.yaml | maintained | urea degradation I (gomodel:YeastPathways_PWY-5703) |
| gomodel:YeastPathways_PWY-7176 | data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml | maintained | UTP and CTP de novo biosynthesis (gomodel:YeastPathways_PWY-7176) |
| gomodel:YeastPathways_PWY3O-4105 | data/pathways/valine-degradation.yaml | maintained | valine degradation (gomodel:YeastPathways_PWY3O-4105) |
| gomodel:YeastPathways_PWY-5080-1 | data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml | maintained | very long chain fatty acid biosynthesis I (gomodel:YeastPathways_PWY-5080-1) |
| gomodel:YeastPathways_PWY3O-8 | data/pathways/xylose-metabolism.yaml | maintained | xylose metabolism (gomodel:YeastPathways_PWY3O-8) |
| gomodel:YeastPathways_PWY-6074-1 | data/pathways/zymosterol-biosynthesis.yaml | maintained | zymosterol biosynthesis (gomodel:YeastPathways_PWY-6074-1) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Repository QC and closed-schema validation (just validate) | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, PathBank:SMP0000992, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | Validated all 271 maintained pathway records against the closed LinkML schema, local identifier/label authority snapshots, 654 history records, 22,211 evidence blocks, 33 source records, and pages/ synchrony. |
| Full pytest test suite (just test) | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, PathBank:SMP0000992, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | All 8,066 unit, schema, KGX, SSSOM, and record-review contract tests passed (3 skipped). |
| Ruff code and script lint check (just lint) | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, PathBank:SMP0000992, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | Ruff lint passed with zero warnings or errors. |
| Git whitespace and conflict marker gate | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, PathBank:SMP0000992, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | git diff --check passed with zero issues. |
| Structured review bundle contract check (just review-check) | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, PathBank:SMP0000992, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | All 199 pre-existing structured review bundles in reviews/structured/ passed schema and append-only checks. |

## Scientific And Domain Assessments

### Pathway identity, taxon grounding, authority-verified CURIEs, and SSSOM source_mappings across all 271 maintained records

identity: supported. Targets: MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, PathBank:SMP0000992, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1.

All 271 maintained pathway records in data/pathways/*.yaml denote coherent microbial pathways, gene clusters, or signaling/virulence modules with authority-verified pathway IDs, NCBITaxon groundings, CHEBI/UniProtKB/ComplexPortal/GO/SGD participant CURIEs, RHEA/MetaCyc/BiGG/Reactome/WikiPathways reaction identifiers, and 615 source_mappings rows across 112 records exporting cleanly to 612 unique SSSOM rows in output/sssom/source_mappings.sssom.tsv.

### Causal graph connectivity, reaction directionality, stoichiometry, and edge-level evidence across all 271 maintained records

graph: supported. Targets: MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, PathBank:SMP0000992, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1.

All 271 maintained records contain connected participant-reaction-edge causal graphs (7,684 participants, 1,597 reactions including 699 RHEA:* reactions, 14,393 mechanistic_edges) with 100% edge-level evidence coverage (21,085 edge-level evidence items; 22,211 total evidence blocks across records, steps, and edges), explicit direction on 100% of 699 RHEA:* reaction nodes, and zero cross-record RHEA direction conflicts.

### Cross-record reaction category typing consistency and KGX node category/source_category export across 56 untyped MetaCyc records

consistency: concern. Targets: MetaCyc:PWY-6543, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY0-1312, MetaCyc:CALVIN-PWY, MetaCyc:ARO-PWY, MetaCyc:COA-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:P101-PWY, MetaCyc:RIBOSYN2-PWY, MetaCyc:GLUTATHIONESYN-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, MetaCyc:PWY-6123, MetaCyc:PWY-6124, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:CYSTSYN-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:TYRSYN, MetaCyc:VALSYN-PWY, MetaCyc:NONMEVIPP-PWY, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:PYRIDNUCSAL-PWY, MetaCyc:DENITRIFICATION-PWY, MetaCyc:NONOXIPENT-PWY, MetaCyc:OXIDATIVEPENT-PWY, MetaCyc:PANTO-PWY, MetaCyc:PPGPPMET-PWY, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-6151, MetaCyc:TRESYN-PWY, MetaCyc:PWY-5686.

While 212 maintained pathway records with reactions[] explicitly declare category on 100% of their 1,318 reaction entries (1,312 molecular_activity and 6 pathway) and zero within-record mixed reaction lists remain after Cycle 1 Stage 5, 56 maintained MetaCyc:* records omit category: molecular_activity across all 279 of their reactions[] entries (263 RHEA:* and 16 MetaCyc:*). Sixteen of those 56 records contain 28 untyped occurrences of 23 shared reaction CURIEs (22 RHEA:* + 1 MetaCyc:DHBAMPLIG-RXN) that explicitly declare category: molecular_activity in sibling records, producing mixed source_contexts in pages/downloads/nodes.tsv, while 231 unique reaction CURIEs appearing exclusively in those 56 records fall back to biolink:BiochemicalReaction with empty source_category instead of biolink:MolecularActivity (source_category=molecular_activity).

## Findings

### F-C2S4-001: Sixteen maintained MetaCyc pathway records omit category: molecular_activity on 28 occurrences of 23 reaction CURIEs that are explicitly typed in sibling records

minor / open / confirmed; issue key: cross-record-shared-reaction-category-inconsistency.

Across 16 maintained MetaCyc pathway records (MetaCyc:ARABCAT-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:CALVIN-PWY, MetaCyc:DAPLYSINESYN-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:GLUTATHIONESYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:HOMOSERSYN-PWY, MetaCyc:NONMEVIPP-PWY, MetaCyc:NONOXIPENT-PWY, MetaCyc:OXIDATIVEPENT-PWY, MetaCyc:P101-PWY, MetaCyc:PWY-8383, and MetaCyc:PYRIDOXSYN-PWY), 28 reaction entries spanning 23 shared catalytic reaction CURIEs (MetaCyc:DHBAMPLIG-RXN, RHEA:10509, RHEA:10841, RHEA:12173, RHEA:12557, RHEA:12606, RHEA:13286, RHEA:13679, RHEA:13986, RHEA:14659, RHEA:15650, RHEA:15763, RHEA:17090, RHEA:17462, RHEA:22369, RHEA:22937, RHEA:23777, RHEA:24286, RHEA:27378, RHEA:27628, RHEA:30168, RHEA:30757, and RHEA:34172) omit category: molecular_activity even though those exact same 23 reaction CURIEs explicitly declare category: molecular_activity in sibling maintained pathway records (PathBank:SMP0000992, PathBank:SMP0002406, KEGG:M00008, MetaCyc:CYANCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GLCMANNANAUT-PWY, MetaCyc:LYXMET-PWY, MetaCyc:PWY-5903, MetaCyc:PWY-7255, MetaCyc:PWY0-1300, MetaCyc:PWY0-1471, MetaCyc:PWY0-301, MetaCyc:PWY0-41, and MetaCyc:THISYN-PWY). In pages/downloads/nodes.tsv, _add_node in src/pathwaymech/kgx.py promotes each of these 23 deduplicated nodes to biolink:MolecularActivity (source_category='molecular_activity') while serializing mixed reaction contexts (with and without 'category': 'molecular_activity') inside source_contexts.

### F-C2S4-002: Fifty-six maintained MetaCyc pathway records omit explicit category: molecular_activity across all 279 reactions[] entries

minor / open / confirmed; issue key: corpus-wide-untyped-reactions-in-56-metacyc-records.

Across 56 maintained MetaCyc pathway records (the 16 records in F-C2S4-001 plus 40 additional MetaCyc:* records), all 279 catalytic reaction entries in reactions[] (263 RHEA:* and 16 MetaCyc:*, spanning 254 unique reaction CURIEs) omit explicit category: molecular_activity, whereas all 212 other maintained pathway records with reactions[] (86 gomodel:*, 84 MetaCyc:*, 12 WikiPathways:*, 11 PathBank:*, 10 GO:*, 6 Reactome:*, 3 KEGG:*) explicitly declare category on 100% of their 1,318 reaction entries (1,312 molecular_activity and 6 pathway). Because 231 unique reaction CURIEs (216 RHEA:* and 15 MetaCyc:*) appear exclusively in these 56 records, src/pathwaymech/kgx.py exports them in pages/downloads/nodes.tsv via _PREFIX_CATEGORIES fallback as biolink:BiochemicalReaction with an empty source_category ('') instead of biolink:MolecularActivity with source_category='molecular_activity'.

## Recommended Actions And Acceptance Checks

### A-C2S4-001

Add explicit category: molecular_activity to all 28 untyped occurrences of the 23 shared catalytic reaction CURIEs across the 16 affected MetaCyc pathway records so shared reaction nodes carry uniform category declarations across all records in source_contexts.

- All 23 shared reaction CURIEs declare category: molecular_activity in every maintained record where they appear.
- Zero reaction nodes in pages/downloads/nodes.tsv have mixed typed and untyped reaction entries in source_contexts.
- .venv/bin/pathwaymech-run-qc and .venv/bin/pytest -q exit 0.

### A-C2S4-002

Add explicit category: molecular_activity to all 279 catalytic reaction entries (263 RHEA:* and 16 MetaCyc:*) across all 56 untyped MetaCyc pathway records, record curation history entries under history/records/&lt;slug&gt;/, and regenerate pages/ so 100% of catalytic reactions across all 271 maintained records declare category: molecular_activity and export as biolink:MolecularActivity with source_category=molecular_activity in pages/downloads/nodes.tsv.

- Zero maintained records in data/pathways/*.yaml omit category on any reactions[] entry (1,591 molecular_activity + 6 pathway = 1,597/1,597 explicitly typed).
- All 56 updated pathway records have matching history/records/&lt;slug&gt;/*.yaml provenance files.
- .venv/bin/pathwaymech-run-qc, .venv/bin/pytest -q, and .venv/bin/python scripts/record_review.py check exit 0.

## Category Boundaries

- retain: GO:0010139, GO:0019270, GO:0019305, GO:0019618, GO:0036040, GO:0042864, GO:0043427, GO:0097288, GO:1901281, GO:1902000. Retain all 10 maintained GO:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against GO authority snapshots and docs/HARMONIZATION.md.
- retain: KEGG:M00008, KEGG:M00373, KEGG:M00374. Retain all 3 maintained KEGG:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against KEGG authority snapshots and docs/HARMONIZATION.md.
- retain: MIBiG:BGC0000829, MIBiG:BGC0000852, MIBiG:BGC0002072. Retain all 3 maintained MIBiG:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against MIBiG authority snapshots and docs/HARMONIZATION.md.
- retain: MetaCyc:2PHENDEG-PWY, MetaCyc:ACETOACETATE-DEG-PWY, MetaCyc:ARABCAT-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:ARGSYN-PWY, MetaCyc:ARO-PWY, MetaCyc:AST-PWY, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, MetaCyc:CENTBENZCOA-PWY, MetaCyc:COA-PWY, MetaCyc:CYANCAT-PWY, MetaCyc:CYSTSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:DENITRIFICATION-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GLCMANNANAUT-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:GLUTATHIONESYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:HISTSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:LYXMET-PWY, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:NONMEVIPP-PWY, MetaCyc:NONOXIPENT-PWY, MetaCyc:OXIDATIVEPENT-PWY, MetaCyc:P101-PWY, MetaCyc:P121-PWY, MetaCyc:P184-PWY, MetaCyc:P2-PWY, MetaCyc:P321-PWY, MetaCyc:PANTO-PWY, MetaCyc:PHESYN, MetaCyc:PLPSAL-PWY, MetaCyc:PPGPPMET-PWY, MetaCyc:PROSYN-PWY, MetaCyc:PWY-1361, MetaCyc:PWY-2361, MetaCyc:PWY-2503, MetaCyc:PWY-5177, MetaCyc:PWY-5386, MetaCyc:PWY-5415, MetaCyc:PWY-5417, MetaCyc:PWY-5420, MetaCyc:PWY-5453, MetaCyc:PWY-5509, MetaCyc:PWY-5686, MetaCyc:PWY-5705, MetaCyc:PWY-5744, MetaCyc:PWY-5789, MetaCyc:PWY-5838, MetaCyc:PWY-5901, MetaCyc:PWY-5903, MetaCyc:PWY-6019, MetaCyc:PWY-6048, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-6123, MetaCyc:PWY-6124, MetaCyc:PWY-6151, MetaCyc:PWY-6223, MetaCyc:PWY-6289, MetaCyc:PWY-6336, MetaCyc:PWY-6376, MetaCyc:PWY-6416, MetaCyc:PWY-6419, MetaCyc:PWY-6534, MetaCyc:PWY-6543, MetaCyc:PWY-6579, MetaCyc:PWY-6609, MetaCyc:PWY-6823, MetaCyc:PWY-6993, MetaCyc:PWY-7181, MetaCyc:PWY-7255, MetaCyc:PWY-7446, MetaCyc:PWY-7545, MetaCyc:PWY-7722, MetaCyc:PWY-7971, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY-8130, MetaCyc:PWY-8131, MetaCyc:PWY-8132, MetaCyc:PWY-8178, MetaCyc:PWY-8383, MetaCyc:PWY0-1241, MetaCyc:PWY0-1277, MetaCyc:PWY0-1280, MetaCyc:PWY0-1300, MetaCyc:PWY0-1312, MetaCyc:PWY0-1338, MetaCyc:PWY0-1352, MetaCyc:PWY0-1433, MetaCyc:PWY0-1471, MetaCyc:PWY0-1477, MetaCyc:PWY0-1517, MetaCyc:PWY0-301, MetaCyc:PWY0-321, MetaCyc:PWY0-41, MetaCyc:PWY0-42, MetaCyc:PWY0-43, MetaCyc:PWY0-501, MetaCyc:PWY0-521, MetaCyc:PWY1-3, MetaCyc:PYRIDNUCSAL-PWY, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:QUINATEDEG-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:RIBOKIN-PWY, MetaCyc:RIBOSYN2-PWY, MetaCyc:SALVADEHYPOX-PWY, MetaCyc:SERSYN-PWY, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:THIOREDOX-PWY, MetaCyc:THISYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRESYN-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:TYRSYN, MetaCyc:VALSYN-PWY, MetaCyc:XYLCAT-PWY. Retain all 140 maintained MetaCyc:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against MetaCyc authority snapshots and docs/HARMONIZATION.md.
- retain: PathBank:SMP0000992, PathBank:SMP0002038, PathBank:SMP0002051, PathBank:SMP0002067, PathBank:SMP0002077, PathBank:SMP0002081, PathBank:SMP0002083, PathBank:SMP0002089, PathBank:SMP0002097, PathBank:SMP0002123, PathBank:SMP0002406. Retain all 11 maintained PathBank:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against PathBank authority snapshots and docs/HARMONIZATION.md.
- retain: Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-936721. Retain all 6 maintained Reactome:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against Reactome authority snapshots and docs/HARMONIZATION.md.
- retain: WikiPathways:WP171, WikiPathways:WP178, WikiPathways:WP266, WikiPathways:WP287, WikiPathways:WP296, WikiPathways:WP392, WikiPathways:WP478, WikiPathways:WP5019, WikiPathways:WP5060, WikiPathways:WP556, WikiPathways:WP5587, WikiPathways:WP71. Retain all 12 maintained WikiPathways:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against WikiPathways authority snapshots and docs/HARMONIZATION.md.
- retain: gomodel:6882d2b800000609, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, gomodel:YeastPathways_DETOX1-PWY, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_GLUCONEO-PWY-1, gomodel:YeastPathways_GLYCLEAV-PWY, gomodel:YeastPathways_GLYCOLYSIS, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, gomodel:YeastPathways_IPPSYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, gomodel:YeastPathways_PROUT-PWY, gomodel:YeastPathways_PWY-1801-1, gomodel:YeastPathways_PWY-2301, gomodel:YeastPathways_PWY-5041, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY-5123, gomodel:YeastPathways_PWY-5194-1, gomodel:YeastPathways_PWY-5340, gomodel:YeastPathways_PWY-5344, gomodel:YeastPathways_PWY-5651, gomodel:YeastPathways_PWY-5653, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-5694, gomodel:YeastPathways_PWY-5697, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-5760-1, gomodel:YeastPathways_PWY-6074-1, gomodel:YeastPathways_PWY-6075-1, gomodel:YeastPathways_PWY-6147, gomodel:YeastPathways_PWY-6614, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY-7219, gomodel:YeastPathways_PWY-7220-1, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_PWY-901, gomodel:YeastPathways_PWY3O-123, gomodel:YeastPathways_PWY3O-15, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-17, gomodel:YeastPathways_PWY3O-1743, gomodel:YeastPathways_PWY3O-1801, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PWY3O-4, gomodel:YeastPathways_PWY3O-402, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY3O-4106, gomodel:YeastPathways_PWY3O-4108, gomodel:YeastPathways_PWY3O-4112, gomodel:YeastPathways_PWY3O-4120, gomodel:YeastPathways_PWY3O-4153, gomodel:YeastPathways_PWY3O-4300, gomodel:YeastPathways_PWY3O-440, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY3O-48, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-64, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWYQT-4432, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, gomodel:YeastPathways_YEAST-RNT-SALV. Retain all 86 maintained gomodel:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against gomodel authority snapshots and docs/HARMONIZATION.md.
- retain: MetaCyc:DAPLYSINESYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:HOMOSERSYN-PWY, MetaCyc:P101-PWY, PathBank:SMP0000992. Retain PathBank:SMP0000992 (Threonine Biosynthesis from Aspartate in Escherichia coli K-12, PW000976.owl, 6 steps: 5-step L-aspartate to L-threonine biosynthetic sequence RHEA:23777 -&gt; RHEA:24286 -&gt; RHEA:15763 -&gt; RHEA:13986 -&gt; RHEA:10841 plus the L-aspartate 4-semialdehyde branch step to lysine/diaminopimelate biosynthesis RHEA:34172) alongside MetaCyc:HOMOSERSYN-PWY (3-step L-aspartate to L-homoserine module), MetaCyc:HOMOSER-THRESYN-PWY (2-step L-homoserine to L-threonine module), MetaCyc:DAPLYSINESYN-PWY (L-lysine biosynthesis I), and MetaCyc:P101-PWY (ectoine biosynthesis) as distinct authority-scoped pathway boundaries and step topologies per docs/HARMONIZATION.md.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EV-C2-QC-VALIDATE | .venv/bin/pathwaymech-run-qc; stdout summary (271 pathway records, 654 history records, 22,211 evidence blocks, 33 source records) | supports | Executed .venv/bin/pathwaymech-run-qc across the frozen working tree at e369fa425e64d4f794ce84e2fd71138a43660467: validated 271 pathway records against the closed LinkML schema, verified all identifiers and labels against local authority snapshots, validated 654 history records and 22,211 evidence blocks, validated 33 source records, and confirmed pages/ synchrony with 271 pathway records. |
| EV-C2-PYTEST | .venv/bin/pytest -q; pytest suite execution across tests/ (8,066 passed, 3 skipped) | supports | Executed the full pytest suite (8,066 passed, 3 skipped), verifying closed LinkML schema validation, identifier policy, KGX export, SSSOM export, source registry, and structured record-review contract invariants. |
| EV-C2-RUFF | .venv/bin/ruff check --no-cache .; ruff check output | supports | Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks passed). |
| EV-C2-GIT-DIFF | git diff --check; git worktree at e369fa425e64d4f794ce84e2fd71138a43660467 | supports | Executed git diff --check with exit code 0; no whitespace errors or conflict markers. |
| EV-C2-REVIEW-CHECK | reviews/structured/; 199 retained structured review bundles | supports | Validated all 199 previously retained structured review bundles under reviews/structured/ via scripts/record_review.py check; confirmed Cycle 1 Stage 4 findings (F-STAGE4-001 and F-STAGE4-002) were resolved in 20261022T033000Z-stage5-resolve-review-findings and zero open finding heads exist on maintained data/pathways/*.yaml records prior to this Cycle 2 Stage 4 review. |
| EV-C2-CORPUS-INSPECTION | data/pathways/; 271 maintained pathway YAML files (7,684 participants, 1,597 reactions including 699 RHEA:* reactions, 14,393 mechanistic_edges, 7,042 references, 615 source_mappings across 112 records) | supports | Inspected all 271 maintained pathway records in data/pathways/*.yaml: 100% declare valid pathway_type, 100% of 14,393 mechanistic_edges carry structured evidence blocks (21,085 edge-level evidence items; 22,211 total evidence blocks across records, steps, and edges), 100% of 699 RHEA:* reaction nodes declare explicit direction with zero cross-record direction conflicts, zero within-record mixed reaction category lists remain, and 615 source_mappings across 112 records export to 612 unique rows in output/sssom/source_mappings.sssom.tsv. |
| EV-C2-SHARED-REACTION-INCONSISTENCY | data/pathways/l-threonine-biosynthesis.yaml; lines 37-43 (reactions[0..1] in MetaCyc:HOMOSER-THRESYN-PWY vs PathBank:SMP0000992) | supports | Across 16 maintained MetaCyc pathway records, 28 reaction occurrences spanning 23 shared catalytic reaction CURIEs (22 RHEA:* + 1 MetaCyc:DHBAMPLIG-RXN) omit category: molecular_activity even though those same 23 reaction CURIEs explicitly declare category: molecular_activity in sibling maintained records (e.g., RHEA:13986 and RHEA:10841 in MetaCyc:HOMOSER-THRESYN-PWY omit category while declaring category: molecular_activity in PathBank:SMP0000992). |
| EV-C2-KGX-EXPORT | src/pathwaymech/kgx.py; lines 70-103, 173-177, and 254-275 (EXPLICIT_CATEGORIES, _PREFIX_CATEGORIES, and _add_node) | supports | In src/pathwaymech/kgx.py, reactions with explicit category: molecular_activity map to biolink:MolecularActivity with source_category='molecular_activity', whereas RHEA:* and MetaCyc:* reactions omitting category fall back via _PREFIX_CATEGORIES to biolink:BiochemicalReaction with empty source_category=''; when a reaction CURIE is shared between a typed record and an untyped record, _add_node promotes the node's top-level category to biolink:MolecularActivity while preserving mixed typed and untyped entries in source_contexts. |
| EV-C2-NODES-TSV | pages/downloads/nodes.tsv; 23 shared reaction rows with mixed source_contexts and 231 untyped-only reaction rows with biolink:BiochemicalReaction | supports | In pages/downloads/nodes.tsv, 23 shared reaction CURIEs (e.g., RHEA:10841, RHEA:13986, RHEA:15763, RHEA:23777, RHEA:24286, RHEA:34172) carry top-level category biolink:MolecularActivity and source_category=molecular_activity while their source_contexts JSON array mixes contexts with and without category, and 231 unique reaction CURIEs (216 RHEA:* and 15 MetaCyc:*) appearing only in the 56 untyped MetaCyc records export as biolink:BiochemicalReaction with empty source_category. |
| EV-C2-UNTYPED-56-METACYC-RECORDS | data/pathways/; 56 maintained MetaCyc pathway records (279 reactions: 263 RHEA:* and 16 MetaCyc:*) | supports | Across the 271 maintained pathway records, 212 records with reactions[] (86 gomodel:*, 84 MetaCyc:*, 12 WikiPathways:*, 11 PathBank:*, 10 GO:*, 6 Reactome:*, 3 KEGG:*) explicitly declare category on 100% of their 1,318 reactions[] entries (1,312 molecular_activity and 6 pathway) and 3 MIBiG:* records have 0 reactions[], whereas 56 maintained MetaCyc:* records omit category: molecular_activity across all 279 of their reactions[] entries (263 RHEA:* and 16 MetaCyc:*). |

## Limits And Additional Notes

- Fifty-six maintained MetaCyc pathway records omit explicit category: molecular_activity across all 279 of their reactions[] entries (263 RHEA:* and 16 MetaCyc:*), including 28 occurrences across 16 MetaCyc records of 23 shared reaction CURIEs that are explicitly typed in sibling records; these are recorded as open minor findings F-C2S4-001 and F-C2S4-002 for Cycle 2 Stage 5 grouped remediation.
- Verification of literature-backed evidence blocks relied on the repository's local authority snapshots and curated evidence quotes/abstracts at frozen commit e369fa425e64d4f794ce84e2fd71138a43660467 without re-fetching external publisher full texts over the network.
- Per Cycle 2 Stage 4 (record_review) workflow policy, no edits were made to data/pathways/*.yaml during this stage; open findings F-C2S4-001 and F-C2S4-002 are carried forward to Cycle 2 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review
kind: category
repository: CultureBotAI/PathwayMech
title: Cycle 2 Stage 4 Full Frozen-Inventory Record and Cohort Review of 271 PathwayMech
  Maintained Records
started_at: '2026-10-22T13:15:00Z'
finished_at: '2026-10-22T13:40:00Z'
reviewer:
  identity: Antigravity (review-yaml-record + review-yaml-category)
  kind: agent
  model: Claude Opus 4.6 (Thinking)
  independence: self_review
  independence_basis: Same agent session (a1d1e545-faee-4294-8a87-4c2d031a6538) executed
    Cycle 2 Stages 1-3 curation in CultureBotAI/PathwayMech prior to running this
    Cycle 2 Stage 4 frozen-inventory review.
skill: review-yaml-category
completion: completed
verdict: pass_with_limitations
native_verdict: coherent
scientific_review: true
summary: 'Completed a full-coverage frozen-inventory scientific record and cohort
  review of all 271 maintained pathway YAML records in data/pathways/*.yaml at Git
  commit e369fa425e64d4f794ce84e2fd71138a43660467 across all 8 identifier namespaces
  (MetaCyc: 140, gomodel: 86, WikiPathways: 12, PathBank: 11, GO: 10, Reactome: 6,
  KEGG: 3, MIBiG: 3; 7,684 participants, 1,597 reactions including 699 RHEA:* reactions,
  14,393 mechanistic_edges, 7,042 references, and 615 source_mappings across 112 records
  exporting to 612 unique SSSOM rows). All 271 records pass closed LinkML schema validation,
  authority snapshot identifier/label checks, history validation (654 records), and
  edge-level evidence verification (14,393 mechanistic edges, 21,085 edge-level evidence
  items, 22,211 total evidence blocks). Identified 2 minor open findings (F-C2S4-001
  across 16 MetaCyc records containing 28 untyped occurrences of 23 shared reaction
  CURIEs that are explicitly typed in sibling records, and F-C2S4-002 across all 56
  MetaCyc records that omit category: molecular_activity on 279 catalytic reactions),
  preserved unedited for Cycle 2 Stage 5 grouped remediation.'
source:
  git_revision: e369fa425e64d4f794ce84e2fd71138a43660467
  state: git_commit
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: 4836f2ecdec689c8ddec07e848b77dc120096b62dae6119e2a3948348adae4b8
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 6b407a3b3f3c4679e49b14843d274e95693a23a6cb3916062a8d3ad07bb13c76
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: CLAUDE.md
    sha256: c067d99547f9e9e9a6edb892d71126b6765239348d0021b907f3102907a4cf00
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    sha256: bdb60326e2ffa5db8e15939ce29bf57a12b992c1f2e56899c1cec3ecf01e2859
    role: target
  - path: data/pathways/2-methylcitrate-cycle-i.yaml
    sha256: 0ccbcbcee61777f9f3265f5dec8c19ad5ce2ccf6051b54afe36fd1ed3bde40b7
    role: target
  - path: data/pathways/2-phenylethanol-biosynthesis.yaml
    sha256: 70936b88da1b369d40b0b68205cc3b31ab67df9df7b003aa0fad049594128798
    role: target
  - path: data/pathways/3-oxoadipate-degradation.yaml
    sha256: 214ef2d38ede4bb4e919f6f53699491e7c53b8d9b5b858c6ba80084e5b067032
    role: target
  - path: data/pathways/4-aminobenzoate-biosynthesis-i.yaml
    sha256: b0150b47850d17acbbe560a7d40a82d49a2f976a92ea15ab43c44df1a83c4b91
    role: target
  - path: data/pathways/4-aminobutyrate-degradation.yaml
    sha256: e953a88e595f3446060152fa7cf2060859dc88b1693138768854c767bece6dda
    role: target
  - path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml
    sha256: 74516388c180b8832fbaf1f8a24a3e8f71ff737a4812191b8c3807dfd91ec250
    role: target
  - path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml
    sha256: 324c587f1e7943d75cc48d6958fdf5f9e8b37d7427e2e132507192e670ba5ec9
    role: target
  - path: data/pathways/5-prime-deoxyadenosine-degradation-i.yaml
    sha256: c8ae12061fd62a5ff8c6861b6665e3ac6938b0fe611b9e3d8d6a1e11f33199a5
    role: target
  - path: data/pathways/5-prime-deoxyadenosine-degradation-ii.yaml
    sha256: a367fac8ac036416baaabc9d64ae1d9927e66e87ad1bb96e2883725fd14ce68b
    role: target
  - path: data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml
    sha256: 5d6d425f52d44d54819deed6bedf672322a09a2333db5305601003376bd327b3
    role: target
  - path: data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml
    sha256: bbcf3f41f8c8996e045827f21672281f8f3040c2e51357eafb74e14fc050d4a6
    role: target
  - path: data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml
    sha256: 98fa4218caba0e95fbee8fc6ce63d97166499afb3609391db88ab6f82a1f4e22
    role: target
  - path: data/pathways/acetoacetate-degradation.yaml
    sha256: 83b7cc0fe5a924f5531d7eb27d09f1a2f0a98b1252b92446f7fb3a198eed12e8
    role: target
  - path: data/pathways/acetogenesis.yaml
    sha256: 355b97b8d2c45e437b853c2447bfb14900507b40923991d49d0b68e9e7d3d54a
    role: target
  - path: data/pathways/adenine-and-adenosine-salvage-i-escherichia-coli.yaml
    sha256: 11725db09e52dcd4de50dd62370510ce85319943078778485e8345ce3bd9b02c
    role: target
  - path: data/pathways/adenine-and-adenosine-salvage-i.yaml
    sha256: cc8721d24ba2236931ca151dcb035d9a9a671ce486acd950e724c9e7ffbf44d2
    role: target
  - path: data/pathways/adenine-and-adenosine-salvage-ii.yaml
    sha256: ceac8c379a61f80a5b532e0c05834e5839cd9511b3446d386748c444092f8c57
    role: target
  - path: data/pathways/adenine-and-adenosine-salvage-iii.yaml
    sha256: acafd5863d376489873aa366db9359ccaf57a693b688b472f78c89e26e3eae86
    role: target
  - path: data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml
    sha256: e7db816bd072061b45da17ca3dec4302f76c91781184501a28ebbc81f570123e
    role: target
  - path: data/pathways/adenosine-nucleotides-degradation-ii.yaml
    sha256: dc082d3edc6391cd6d85a503e3fbf3e77b96d34f0ee93eecad51f6e6272b1025
    role: target
  - path: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
    sha256: 027459e5a871dcdb8f394ba6b30f2a6e01b92c4f98c8b6f9f232dfc12dbfb010
    role: target
  - path: data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
    sha256: 8453146fc5cc438fd95be5acc623ba0f6fbe52e647ad21f1fa2dc535ee619184
    role: target
  - path: data/pathways/adenosylcobinamide-gdp-salvage-i.yaml
    sha256: ee0c344a18b4b981b244ee8fcd00e651258990a3323d973fb0d978f47e26efef
    role: target
  - path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
    sha256: affa9eb37e5575d895dc7ae93173037ff18019e2a5e74012139b6aacb6febaf3
    role: target
  - path: data/pathways/aerobactin-biosynthesis.yaml
    sha256: 3e4e50965749a9fa9dfe6319fd1462cc8329c10b7f4ab5363e7b486f2f32e3d4
    role: target
  - path: data/pathways/aerobic-glycerol-degradation.yaml
    sha256: 89d0c0e1202bcc20bdc120764d454b4a1fa4112d14d82aa61bebbc46dcf92699
    role: target
  - path: data/pathways/allantoin-degradation-iv-anaerobic.yaml
    sha256: bf7b150b5b6d0647a1f2b7f4d90c8b3e5ff3c6e73c36f00acc1fe542ba1f034c
    role: target
  - path: data/pathways/allantoin-degradation-to-glyoxylate-i.yaml
    sha256: 20a2143fca48392111bbf273148db8cd7128139ade7a74c00e1b8c26e3f4e58b
    role: target
  - path: data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
    sha256: 1fe731570ceb2038b0b153686be184c99afbd82ab6ba9a9516694b2277de1b37
    role: target
  - path: data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml
    sha256: 962f07ce5ea3130396bc51df0bab3892ceb8bbfc45326a76a50f7a82579168d0
    role: target
  - path: data/pathways/amino-sugar-superpathway.yaml
    sha256: 1c93e912f2e349fbfab5458f309f526fcfc9d381560ac04ba35b7c442f2295f8
    role: target
  - path: data/pathways/aspartate-biosynthesis.yaml
    sha256: 20016b7d818f0dc7e4cb17610ef76abfba9265db8d24b0af5b3fab496685bf87
    role: target
  - path: data/pathways/assimilatory-sulfate-reduction.yaml
    sha256: 376aa99c28b3b509414bdec962bfcc75a5a7199cf3b12eb815466dc035084223
    role: target
  - path: data/pathways/bacillibactin-biosynthesis.yaml
    sha256: aaf46730530dc9ae86fd18f8b382baebbcf0f37b79342b7eebf18e0e64ebeafa
    role: target
  - path: data/pathways/baesr-two-component-signal-transduction.yaml
    sha256: 1cf9262a0df376a19517b3f55ccaac67dacc8af8ce58bd8a1b2046e93a951824
    role: target
  - path: data/pathways/benzoate-degradation-i-aerobic.yaml
    sha256: 1f5d025ef0b00ff3a1bdbaa90bff4f7e38068ba608d9b5e179604c705e0de8f7
    role: target
  - path: data/pathways/benzoyl-coa-degradation-i-aerobic.yaml
    sha256: 009e8e6796052e3c1dca8af95a55edaf69273545d6606ebd41aed4369cb7624f
    role: target
  - path: data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml
    sha256: e43e6ad5563c38af738e8f1c7b733510072b531196ce435395896b62951c6ab9
    role: target
  - path: data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml
    sha256: 40fa37e63c5be6ec6c9d33bf67f4bf06e597fc4c9b12514d34401379b124ad51
    role: target
  - path: data/pathways/beta-alanine-biosynthesis-iv.yaml
    sha256: 0b24a16ea8a7fb91fe1ead37cb5868d9ce4c8b8d36f04e788e2e9030da6b8972
    role: target
  - path: data/pathways/biotin-biosynthesis-i.yaml
    sha256: b95b35d22f813ecb167b068554b4cee9e44bdb2d0ce4765338e82ecd84df0dff
    role: target
  - path: data/pathways/calvin-cycle.yaml
    sha256: e5b770e60e481068b847e7dfe60b3f85681e36f25952f2c4308f82b0133d05a9
    role: target
  - path: data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml
    sha256: c2c307e749e73e33de865c3ea92bee0b22a5828396af79066061299976a89bec
    role: target
  - path: data/pathways/carnitine-shuttle.yaml
    sha256: b30ce5a608752d19a0f22de39a50c261be96e4d8f7cd5940759a4de49eff8e28
    role: target
  - path: data/pathways/catechol-degradation-i.yaml
    sha256: 29b073a0a5aca884b9decf6b86a41c2a018c62dc0818c7e33ec17065152d781c
    role: target
  - path: data/pathways/catechol-degradation-ii.yaml
    sha256: 4931e9a8cc5ae9f55c434d942c70fc65c75ad73a49e878bd34fbcfc4250df110
    role: target
  - path: data/pathways/catechol-degradation-iii.yaml
    sha256: b30573a380b358a9b0228f8e3e2689943ecf828aa01ae790f281ba3fe617e603
    role: target
  - path: data/pathways/catechol-degradation-to-beta-ketoadipate.yaml
    sha256: 39ca1eedee87cb3ee01d9d698359bdfdee505b1fa05e160154e976fa6514e6c6
    role: target
  - path: data/pathways/chitin-biosynthesis.yaml
    sha256: 46627a456564e07dfc4dcb1e41383e6aeefebc3e52f1fe3a5b26e18f92da8361
    role: target
  - path: data/pathways/chorismate-biosynthesis-i.yaml
    sha256: dc5c2fa8d319b3e1909f59982d6891e0de76eecc00bd3850da469507f0a1875a
    role: target
  - path: data/pathways/chromobacterium-violaceum-violacein-biosynthetic-gene-cluster.yaml
    sha256: a2c389bdea0ba8574ded73b47ae67cc5011105f4579401661197ffcb0e689d0a
    role: target
  - path: data/pathways/citrate-lyase-activation.yaml
    sha256: c76b50f65ef43e599ca16a9789144840660b52a4dc1d9adcd46fb8c5fecdd450
    role: target
  - path: data/pathways/citrulline-biosynthesis.yaml
    sha256: 990b97ed6aec1c619dfb5a4a53b098a3c4ca4b5ab46ab537d275cbfe7d10d80b
    role: target
  - path: data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml
    sha256: bdca4a5ea4688a5a4f4ab4f18e93dc3501b40e0bfe00eb7fa1621998295f438d
    role: target
  - path: data/pathways/curcumin-degradation.yaml
    sha256: 814e063d50371068e9a7f3d6238b0f6ad76e172f6072c59b570cafdba0cb407b
    role: target
  - path: data/pathways/cyanate-degradation.yaml
    sha256: bc0ac1b2ce20a5c3e0eeb98d220e6dc55513ed5eb4fcd9aaadcace5ec1899d84
    role: target
  - path: data/pathways/d-arabinose-degradation-i.yaml
    sha256: e4c05a00929557b8cabcdc26f057f7ac788d85ae82de515828806a79dd98f886
    role: target
  - path: data/pathways/d-galactarate-degradation-i.yaml
    sha256: 6f637a08b7bb39df952c27a96313c60883ae53ff15fd9597972ded54bf31bc26
    role: target
  - path: data/pathways/d-galactonate-degradation.yaml
    sha256: 51e71bf9bd2d0888f6f3e56f98eb4b4fab32034266bfe8dfeeb375529afc3f84
    role: target
  - path: data/pathways/d-galacturonate-degradation-i.yaml
    sha256: dafcc96c28d5d1e9c36f38a9b9701217e64b32cebffcb7fd4516bb1557a5d562
    role: target
  - path: data/pathways/d-glucarate-degradation-i.yaml
    sha256: c48cbb09d6b97812ea6d84a3229eae34400a68bccc38192553fff2d376ba4ad1
    role: target
  - path: data/pathways/d-xylose-degradation-i.yaml
    sha256: 4faccd4d9a05d6132f6f24e06d481e0c1be1386f4914cecd8abcab6e23c50ce2
    role: target
  - path: data/pathways/desferrioxamine-b-biosynthesis.yaml
    sha256: ab6b7808c564fc2bbddaa1fea159f0927e2ec2f73b9890e7ab360c5e3718a9dd
    role: target
  - path: data/pathways/dicarboxylate-hydroxybutyrate-cycle.yaml
    sha256: bf5316958e94eae4e2e09a864dca8e45d8997b041d7e26c991c9633f24449209
    role: target
  - path: data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml
    sha256: 1fe23e30c0e1d0e14fff70678f966812c1c1a4bc602441076ad041c232190ef8
    role: target
  - path: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
    sha256: 6fa9f8a6697af1bb35b060943f7b16c0d350366bbaa8ae9268456c45683f5c62
    role: target
  - path: data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
    sha256: 75ec1f4ffa088e6647182cde01b7959df161261cb03d48cd471609b2a9b42de9
    role: target
  - path: data/pathways/ectoine-biosynthesis.yaml
    sha256: 9f9d3c2c3de5ca5a3c59df1c3cb056fdf8cd60c0fb922feb902d5549151478dc
    role: target
  - path: data/pathways/entner-doudoroff-pathway.yaml
    sha256: 6ff158fbca9a78f73f9ebf493e1f068fd2d5115ec73a0e42657a18f35a8867ad
    role: target
  - path: data/pathways/epoxysqualene-biosynthesis.yaml
    sha256: da3b71fd30801bc13f92ba2226badc86c1376f40b78bd622c9b8a4ff132d1fd2
    role: target
  - path: data/pathways/ergosterol-biosynthesis-i.yaml
    sha256: b8f7c7cd77268474d0b3d17f2109c0f4da9131eb2e040907a188127ed7b98bc6
    role: target
  - path: data/pathways/ergothioneine-biosynthesis-i.yaml
    sha256: 6d2fb20f5a664a6b7e43e9efb48ac1b65fd59a3e5c5daa1aa95b6bae35184dec
    role: target
  - path: data/pathways/ethanol-degradation.yaml
    sha256: fc50f4fe0251b9a24c2c0be359c4349ef12194556f510f390132dc556094031a
    role: target
  - path: data/pathways/ethanolamine-utilization.yaml
    sha256: f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e
    role: target
  - path: data/pathways/ethylene-glycol-degradation.yaml
    sha256: c247d9c205fc14ac5bb0d1e6de57c54d06aca5a484eb99b9e8e694c9d6f2e6de
    role: target
  - path: data/pathways/ethylmalonyl-coa-pathway.yaml
    sha256: 8c4d525a0285213cbc92bed1045a3c69125135abede0b66fed548dcab8e8913d
    role: target
  - path: data/pathways/fatty-acid-elongation.yaml
    sha256: b62921d961d820d8ff589720e08dd002e146b9989aee2c82b045d810bf0351b3
    role: target
  - path: data/pathways/fatty-acid-oxidation-pathway.yaml
    sha256: bfde333f007a3a73eb3172619e731d189e131a628653ad171bf4252798ed593e
    role: target
  - path: data/pathways/flavin-biosynthesis-i.yaml
    sha256: 417d94b49af861613f07f76e2f4dc0d6b4d44123a57547a1c05c2aca91e2a025
    role: target
  - path: data/pathways/folate-interconversions.yaml
    sha256: 0823d8deed478b16f05f0df675c9b453eb65714f78aed067188bbc168b1cbcb5
    role: target
  - path: data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml
    sha256: cad662956612f880a1fa23e5dd729af944a7cee3c09d93eb8abce7b2a2aceebb
    role: target
  - path: data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
    sha256: 3e5b25fc917a30aca70b1dbdce4c70cb7b2d69f595b1f0f13d391812b7cdcb93
    role: target
  - path: data/pathways/fructoselysine-catabolic-process.yaml
    sha256: e9e80038a8671da109e8453523439ed921fe7810bb96b24f55dc532b4dd6ca5f
    role: target
  - path: data/pathways/galactose-degradation.yaml
    sha256: afb4d246ee5305b34e0d960cabb3a25e30d6289e0899133cf5eb5cd6aaba2860
    role: target
  - path: data/pathways/gallate-degradation-i.yaml
    sha256: a6e0e8f52880ccb651e02526dbd627240ec7e46a637d2eabfd790846156d21b0
    role: target
  - path: data/pathways/gallate-degradation-ii.yaml
    sha256: 72e4685f14ff3a6a9d5cd5c7b9cd27d5fa54592355a5191fa5cf821d07a19353
    role: target
  - path: data/pathways/gentisate-degradation-i.yaml
    sha256: 272e475b3bb872475bba938c5e5016b52b63e21dc8c9dea772e25ba78524c064
    role: target
  - path: data/pathways/gluconeogenesis-i.yaml
    sha256: ed359fc88a819b1ff6c51b8b2e10cf399b184cbe25df7c74883d560311296a15
    role: target
  - path: data/pathways/glutamate-degradation-i.yaml
    sha256: 5bfde8cb993cedc9cfc1534157d0c63121bcdbcc75b1c915274e381ada8524ce
    role: target
  - path: data/pathways/glutaryl-coa-degradation.yaml
    sha256: 3c2ac2ae8443a7bdac87bd8ca9e612eee869fb479f3625231fadf84658e16317
    role: target
  - path: data/pathways/glutathione-biosynthesis.yaml
    sha256: e6b762e025742ca9cf0766d8d2d8b3f15e1c2b0078e7af2ab21bab1a43d8dba7
    role: target
  - path: data/pathways/glutathione-degradation.yaml
    sha256: 90700db818d7b32cf46b41e4bf53c234f070829e779a5b80ee8537b32f4a808a
    role: target
  - path: data/pathways/glutathione-glutaredoxin-redox-reaction.yaml
    sha256: cbee4a5a80e9340376ae64bdd05ccc7a3aa6096630f24324af11fca9eca97977
    role: target
  - path: data/pathways/glycerol-biosynthesis.yaml
    sha256: ac0ea900a57b2147297dc7bde6c767bda334664a92c406cc367b6f6ee8430cbc
    role: target
  - path: data/pathways/glycerol-degradation-v.yaml
    sha256: 17004e2911d28d42612c2010bf28d3339dc7f5f8a5af1e49b94cb4bae98ab2ba
    role: target
  - path: data/pathways/glycine-cleavage.yaml
    sha256: 74b9d679808b3950cd1bd0bf2ed8574e4abf9f61f203c8b5538e5e4b46a483db
    role: target
  - path: data/pathways/glycogen-catabolism.yaml
    sha256: 72b8e29697334f849212bd9827055265fb375fbc3f2847b7b062d6a9705e6cce
    role: target
  - path: data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml
    sha256: 0a9fd40d1eaa77a75af58968732d361457618636d5d81775200f3cf88c88193d
    role: target
  - path: data/pathways/glyoxylate-assimilation.yaml
    sha256: 462022906e961f49ceb92c32fcc7d6f834b6e55f89ead1b1f786a91d11258969
    role: target
  - path: data/pathways/glyoxylate-cycle.yaml
    sha256: bd5793fee6b8af7da1e67eece20ebfd65004a48bdfe4d4afbbfb3d544c8138b9
    role: target
  - path: data/pathways/guanine-and-guanosine-salvage.yaml
    sha256: 7133352b12d3cd8579acc128b2896b9247dd8503f06c339d2526e137eb17e58e
    role: target
  - path: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
    sha256: 2d1a05f95a978e13f16c2fb551b60633b34b8bd5397de9214411b99c95e090be
    role: target
  - path: data/pathways/heme-biosynthesis-i-aerobic.yaml
    sha256: a82d6893480d683143a1d54350b3f183de5a0d1fcb4ff59a16d146f054d9fa66
    role: target
  - path: data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml
    sha256: e97493175ab78edaaa100e8e0924f5c8ad4ef3d31ce7b13368c9ca067707a02e
    role: target
  - path: data/pathways/homocysteine-and-cysteine-interconversion.yaml
    sha256: c9fde1235193ea94d4ba624d0c7966c994ec54ef0e30fb71dde686a5c6a78630
    role: target
  - path: data/pathways/homogentisate-degradation.yaml
    sha256: a833e707d3dbd92ff09194e1d19b7c419aa3e2c4c45d3a53064c8915a2d755d2
    role: target
  - path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    sha256: 254d42b0e04165e9b84f95692e1f4cd482f259fe28b2fd1fbd45485bbf3536fa
    role: target
  - path: data/pathways/inosine-5-phosphate-biosynthesis-i.yaml
    sha256: 74e4cd1621fc270ba365ef411b3079692de075024264f7e8866f6b0d9442938e
    role: target
  - path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    sha256: d676ccc1740fc538486cc7c9664bd5e3e2c89cc2aadd74bcffd586cce6aa7b97
    role: target
  - path: data/pathways/inositol-phosphate-biosynthesis.yaml
    sha256: 2fe2d2ba88e85693135d52e2bb72ab7ca37cf41d2e9f879fdb602241d63a6fc3
    role: target
  - path: data/pathways/isoleucine-degradation.yaml
    sha256: 8d93b27c9181bb58990868d80e7443b52c161f5878909d0ff70f0c7147b1857b
    role: target
  - path: data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml
    sha256: 6c9f87fc7a7b6ae411092a5e34330df52f18bb574a09b25eae79fc48182d3955
    role: target
  - path: data/pathways/l-arabinose-degradation-i.yaml
    sha256: 37cfa161adf3d8ab8b4b01a018d387d60b33817bd5908b0d1dc73c91ee7d001e
    role: target
  - path: data/pathways/l-arginine-biosynthesis-i.yaml
    sha256: bf299cc075fee4f21e6cb76b71cdcddc70c06dbd8db17ab9448144f95dd7535c
    role: target
  - path: data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml
    sha256: cce1353fcdd659940db26fec1dd8dce7df198977f01837354798ac91756f5ac4
    role: target
  - path: data/pathways/l-arginine-degradation-ii-ast-pathway.yaml
    sha256: fe02deb131bfe53eedb770ed50278885955e7a67d97859184142aea6ae35c86b
    role: target
  - path: data/pathways/l-arginine-degradation-iv.yaml
    sha256: e9769441139f7047c2d2c83338b03deffc61bc3ec7b84990e0487e4f5e8eaa92
    role: target
  - path: data/pathways/l-arginine-degradation-v.yaml
    sha256: 869563ce5c7be07d5d4bd976ff53030082e518f913822b09f2c01033aee801df
    role: target
  - path: data/pathways/l-ascorbate-degradation-i.yaml
    sha256: fbd52a2c7fdf4cee6091b65b6dc744fc50f0c4e53c42992e750c013839850b26
    role: target
  - path: data/pathways/l-asparagine-biosynthesis-i.yaml
    sha256: 4c2ab031a5eec78aa751ddf4dc8753fc9523b1c18209abee6c237fd96d48628b
    role: target
  - path: data/pathways/l-asparagine-degradation.yaml
    sha256: 427034ee8a5311f807010c76d58368f822040bdec093c44c8638211b3a4cc1ef
    role: target
  - path: data/pathways/l-carnitine-degradation-i.yaml
    sha256: b007e4f9bf0d67c08c0c2262a46b6ddf4cbbc37d05ade639725f74bb008be767
    role: target
  - path: data/pathways/l-cysteine-biosynthesis-i.yaml
    sha256: 54fe6a258f21f5866d4051ad8b756f347191a9fe3a154b3749c8393367157476
    role: target
  - path: data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml
    sha256: 367aed6701c731ec5d920226f082ab99b443debd7b353e84cf9b578eb1836459
    role: target
  - path: data/pathways/l-fucose-degradation-i.yaml
    sha256: a00b36d76e86e0102822cd1d280e686310aa0ff1603d0f4e53a8ed7286b3dc9a
    role: target
  - path: data/pathways/l-histidine-biosynthesis.yaml
    sha256: d4f67cf6d398a8ed42fcd7a83588f93c0f81ee22ddc94308d8027a9aa39e6c58
    role: target
  - path: data/pathways/l-homocysteine-biosynthesis.yaml
    sha256: ba66c588436c87397735f545b7e85accde4ae1e836f617b4041926e07f155f17
    role: target
  - path: data/pathways/l-homoserine-biosynthesis.yaml
    sha256: 2ba55d5db3be34827890a544718c9759c4a606e464b0e46d3c263bf4dcff30d1
    role: target
  - path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
    sha256: 6f478576730ca9224f355d5f04730464a7a7fa4e4dcca9a16c206b21669d8445
    role: target
  - path: data/pathways/l-leucine-biosynthesis.yaml
    sha256: 7c11ab8c3970d6ac699b9a6d55bcfb8e31fa936fd8be9a8cffec49cb0f63bc1d
    role: target
  - path: data/pathways/l-lysine-biosynthesis-i.yaml
    sha256: f9e140eb9a5d886b826e5b77d03b44ad9bbad4b46dac54cdd676ad067e68705e
    role: target
  - path: data/pathways/l-lysine-biosynthesis-iv.yaml
    sha256: 1677f106fb798345712261c31d55df8175810494d8988bcf6ad6cf5f28debf28
    role: target
  - path: data/pathways/l-lyxose-degradation.yaml
    sha256: 8ca651dc70a0dda2620ba09719a4e6861517d39f1736ca1971f283900accc121
    role: target
  - path: data/pathways/l-methionine-biosynthesis-i.yaml
    sha256: d3f600b8cf7da3ca2d5027327097c08e11bf562bbdceea90b1c5e9e7faaf2e89
    role: target
  - path: data/pathways/l-ornithine-biosynthesis-i.yaml
    sha256: 922abf2efb71d2ba60e3913a9c0827bdcf419bd8800d900d66d4b8752e075d7f
    role: target
  - path: data/pathways/l-phenylalanine-biosynthesis-i.yaml
    sha256: 9b816a653a709e59bd9cd25b249d0e8e0ad58fcb90d072c981bd8c2748811d88
    role: target
  - path: data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml
    sha256: e812af6b8f5879d39859ff0203088ddb6c298f1df13167d4e76f39f98f4da252
    role: target
  - path: data/pathways/l-proline-degradation.yaml
    sha256: 219603aea97d72075b8af5b9127026b3b397438b4fcaa4729e7a231f346c4160
    role: target
  - path: data/pathways/l-rhamnose-degradation-i.yaml
    sha256: f7afcfa11188882427f316b02209fcb4fe4544c1e45c0290259858a5c28ed970
    role: target
  - path: data/pathways/l-serine-biosynthesis-i.yaml
    sha256: b8fd90eb060911cf62737caa12f9b4899cc89119a2369aa3281bc700a64313a9
    role: target
  - path: data/pathways/l-threonine-biosynthesis.yaml
    sha256: e277951647e3da86c7ad92ac40a3e8d795c36f1550d67825898927540fe5dfa3
    role: target
  - path: data/pathways/l-threonine-degradation-iii.yaml
    sha256: ce2bdf9706345cd51044e413276b8908f28508da333fa72faea8e65145e58a9c
    role: target
  - path: data/pathways/l-tryptophan-biosynthesis.yaml
    sha256: 92206dbd7e6e9aba6fee6e9f866e3eb3fe019cd6b832a0ac6586cbcc65ce6dcc
    role: target
  - path: data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml
    sha256: 7c69e4796385026c8d9f6fd0746183965cfa757a93b397e1fc6ae4cbfc40ab78
    role: target
  - path: data/pathways/l-tyrosine-biosynthesis-i.yaml
    sha256: e61553cc86414476cc4bc593114c2c0820b01246225450edffdef55910efe376
    role: target
  - path: data/pathways/l-tyrosine-degradation-iii.yaml
    sha256: e284eb14b32872c68b2914eebf0a511d6c6793803a2b7fb464dc5b65d6436f17
    role: target
  - path: data/pathways/l-valine-biosynthesis.yaml
    sha256: 9b58c4c2bdd0b065c6227492dda5c6bc998902739848ab4f2dc1f070e7bd9c19
    role: target
  - path: data/pathways/leucine-degradation.yaml
    sha256: 970f3bd13ea75cf742fc23a5410e4fe2e8f728e07e9d64049575e17480296b31
    role: target
  - path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
    sha256: a5a908285f06357add5292777ea7be2226263c1448097361f9b3d87be0001cbe
    role: target
  - path: data/pathways/lipid-iva-biosynthesis.yaml
    sha256: 5fdcc02a40f15844d1ba8a2ca67979afd58bd34781af21d8e2380a46df7faad5
    role: target
  - path: data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml
    sha256: 917b7a976e9fad4d84e43e5497105ac58670ccd419f09dc147aa8ebd93fc2e2e
    role: target
  - path: data/pathways/mannose-degradation.yaml
    sha256: 28b58d00df8bc90ca2167213378d240f784502ee3d38cd044f0b9f708645d17a
    role: target
  - path: data/pathways/mannosylglycerate-degradation.yaml
    sha256: 39d1a3fa83a5d41ad8e9b2f8f26e22d881e6379a4beee76561e6fa34fa94da08
    role: target
  - path: data/pathways/methanogenesis-from-acetate.yaml
    sha256: 47d1c71951ce5806e5c9570ee00b2ab9f8634158251ee06821a0f77017b0eca3
    role: target
  - path: data/pathways/methanogenesis-from-h2-and-co2.yaml
    sha256: 553922ede0ecdb12ebe569dbb9d8af1c70d4aa190e4fd60e69a9bc7ea0cf8e1e
    role: target
  - path: data/pathways/methionine-salvage-pathway.yaml
    sha256: 7d9173433d90f1344b909cbd4d147923e5acf5acd18c2132df357c892c68f503
    role: target
  - path: data/pathways/methylerythritol-phosphate-pathway-i.yaml
    sha256: 868d6af5bb463ac41869ed65820b0e87fadb1de7ccb018fb26170ffe423b2fea
    role: target
  - path: data/pathways/methylglyoxal-catabolism.yaml
    sha256: d1409031c98be3795d39fc4d2e5362d951cbd86c8b4c2868810a70c61582947a
    role: target
  - path: data/pathways/methylglyoxal-degradation-i.yaml
    sha256: d714bf32e64b16682b2c451e90732644dcf4fae7453150a53f3d490316550f3f
    role: target
  - path: data/pathways/methylglyoxal-degradation-iii.yaml
    sha256: 904a0f1aabfc7ba215fa1c933357715414a0f0cbed8ec130f84420b07812a688
    role: target
  - path: data/pathways/methylphosphonate-degradation-i.yaml
    sha256: 204b86bef2371a61586a7c9b4c0a33880e23c8999620fdeefb575900f5ddfdbe
    role: target
  - path: data/pathways/methylthiopropanoate-degradation-i.yaml
    sha256: 7810e21c690b17fe781fd249ea6fc0ec86220913a55947df75ec29c15cffe5dd
    role: target
  - path: data/pathways/mevalonate-pathway.yaml
    sha256: 1a3aaaf143564f9f1d345596cff4b961219716288a656791de7bf51bdba0307c
    role: target
  - path: data/pathways/molybdenum-cofactor-biosynthesis.yaml
    sha256: 84a67af129e307b0f67a8eb4aed8027a6b12733467e61c66249e1a8a9d751cc3
    role: target
  - path: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
    sha256: cdbfd2cae9e281dc1a1722f65b2f019841b0a84b6e53e755bce049d495ed7f44
    role: target
  - path: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
    sha256: 99b0c6d3e04ab2d3c310bbe8099cd5fa716f251632e5320ba83444bd7ebff82d
    role: target
  - path: data/pathways/mycobacterium-sulfate-assimilation.yaml
    sha256: aecb344e6ec330b48884cafd9bab879f5e3c623f66e315d90ad93910da12f931
    role: target
  - path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
    sha256: 7c3915665fbbe8cfe1d695354f471a1c832ccf972d2302c0910a96144ec1cd49
    role: target
  - path: data/pathways/mycothiol-biosynthesis.yaml
    sha256: 35dfb77de4fcc447aeb649bb478c6a840e78ab39f5921469a154ec3768c32f4f
    role: target
  - path: data/pathways/mycothiol-catabolism.yaml
    sha256: 9d1f2496015cee969712712da363456ac0cac63dcd5cb46cfa5ace763f8388b1
    role: target
  - path: data/pathways/myo-inositol-biosynthesis.yaml
    sha256: 361f6547c51db754e8f9b68069e874d314ed2c7d0b2ee8c1716f6ac9fbcdff96
    role: target
  - path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    sha256: 5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2
    role: target
  - path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    sha256: 1ddbabfa3bad2292e49add564ee94283ff622c5dae55902f78aa5b4b1d6908b8
    role: target
  - path: data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml
    sha256: bcd51a74589e80d1ff361bad234b690c487330acc238450bcd5e3215f25ea7cd
    role: target
  - path: data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml
    sha256: 36b0c2675cf844a236ee4e20a9f89874f137726026b1a713618cb6b4a51a280a
    role: target
  - path: data/pathways/nad-phosphorylation-and-dephosphorylation.yaml
    sha256: 2da6fc3e5d1c1e5ce4b4d0c8a9d1857b1f234c4c872cdf73d364f1c73ad87cb2
    role: target
  - path: data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml
    sha256: dc3a803eb1890953f16cf92fe012d9f780aa5e376ec30cfa2fc467cd80645885
    role: target
  - path: data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml
    sha256: 04f04356990ef06c793936970668528f4e4a3fadc52a32d161ab8c5175673101
    role: target
  - path: data/pathways/nad-salvage-pathway-v.yaml
    sha256: 6f1e3a5883d8c6fba1aa10c90d089d3d8c19a54a6b7b9e1b1b0a4e24c2a0fdf8
    role: target
  - path: data/pathways/nicotine-degradation-ii.yaml
    sha256: 462730b0c0b3679197226dc89dfbf04cac932cf004cea194a8fc3db89be82b0c
    role: target
  - path: data/pathways/nitrate-reduction-i-denitrification.yaml
    sha256: 7c5b3ca9714dd9968901921b54bb82f44b08f85da322cb5527453ac685568ecd
    role: target
  - path: data/pathways/nitrate-reduction-viii.yaml
    sha256: 5243f546a62490581e35d29516f2ecb830b1284748d6b2b042b82e7d9f6303b7
    role: target
  - path: data/pathways/oleate-biosynthesis.yaml
    sha256: 15992b5f8df117cec7bf73691cd2765cd60ea6db24aaa37b9b36861ee08909f7
    role: target
  - path: data/pathways/palmitoleate-biosynthesis.yaml
    sha256: b19047b3b055d4f065267230e639742d344b7aabe2edaa8a64bc0bfda88320b8
    role: target
  - path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    sha256: 4fa7115243982e1fc30e5f492f66ab43225152be9e14cf114d5c67857af6032f
    role: target
  - path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
    sha256: 20541f677f9228b670aac99a94e4d19ef89b5c20e0f6fdbb288d18ec7a9d98f5
    role: target
  - path: data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
    sha256: 37f5e7f93e971f867f00890b758411f59e84117ce1f9a76f310e64e82c5393e8
    role: target
  - path: data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
    sha256: 41137e969f7960cddb59b6452079b9424b87b0bfaa8402172969c230965cb36a
    role: target
  - path: data/pathways/periplasmic-nad-degradation.yaml
    sha256: b9186a25e2fe115e1f86d2d40024117d5424f5c1f1addd35d6d60fedd9c037bd
    role: target
  - path: data/pathways/petrobactin-biosynthesis.yaml
    sha256: 7d0737b9f0bb3a4673e7341e53c5763c80e4fb46fb2944db8c2199a6e66d645a
    role: target
  - path: data/pathways/phenylacetate-degradation-i-aerobic.yaml
    sha256: e99722d1ee920cf64aaeae7b00f1de9b59f939bd96a03a7ac5f2885933a72227
    role: target
  - path: data/pathways/phenylalanine-biosynthesis.yaml
    sha256: b8903227908a29e6abaa9e8b9f9999b9f381aac31f8902702fa76591ae781f65
    role: target
  - path: data/pathways/phenylethylamine-degradation-i.yaml
    sha256: 3bdb2e4ae2eacefe5abf1611f89a58099f47b3264e58bc4195a55404833fe7f8
    role: target
  - path: data/pathways/phenylethylamine-degradation-ii.yaml
    sha256: 8ea61243fca5d7d4a1974cf6b6eb8c9663a1c43a4f182709a7910eb56256d299
    role: target
  - path: data/pathways/phenylpropanoate-and-hydroxyphenylpropanoate-degradation.yaml
    sha256: ff78d0911bb6ebe9e9780a8dce4fd11943228d67639ef44f63daf1cd7c362745
    role: target
  - path: data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml
    sha256: fc29837d25bb30779601d0cd011092833be57b2040370f5b656108c6351f3e5c
    role: target
  - path: data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml
    sha256: 3754f2cc7edc6996237b0bd5cdc96602bdb41c94abd1bd4ea010029d42ac51d7
    role: target
  - path: data/pathways/phosphatidylcholine-biosynthesis-i.yaml
    sha256: 72b66339971241b0e2bf89a17bf5b9dc1297cdb82d01fc4857d0a5379ba03cb6
    role: target
  - path: data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml
    sha256: 48257f89bbe473bd0cb155f35cb5e8b5745d7cca8adb13f9f00c0d88018804f3
    role: target
  - path: data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml
    sha256: 3e02f66d204a5b899920d7d45cec37f2a83bbe57a321b1a394716a247f5ada26
    role: target
  - path: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
    sha256: b9378fa6c051f50743bf57b8cf280cc44f702f4266470898a88aec0b3b222591
    role: target
  - path: data/pathways/phospholipid-biosynthesis.yaml
    sha256: 417bf20d9ae6714e5055e015952829c2fd20f34c1f532dcc9116eb76983fa8e0
    role: target
  - path: data/pathways/phospholipids-degradation.yaml
    sha256: 1623a953f29c91d49e189b163e6d91a21803e9d9176e53fcd7b76b9cb874ec30
    role: target
  - path: data/pathways/phosphopantothenate-biosynthesis-i.yaml
    sha256: 7d16b766666d040ee91d6e4c56415c69312440fa6f7a3db1482c3f807719c6f0
    role: target
  - path: data/pathways/polyhydroxybutanoate-biosynthesis.yaml
    sha256: 31480b5959f3b596fa758d0272b7b2400a9b23b33b52af7349f999ae6dad8d45
    role: target
  - path: data/pathways/ppgpp-metabolism.yaml
    sha256: 81e8642cd792bbe351a43638303a7232e92679d2b47e8c308170bc6a0ad36a20
    role: target
  - path: data/pathways/protocatechuate-meta-cleavage.yaml
    sha256: c36339efcbc6aeef084826b2b8a66fcbea46240aeed6c68c0275602fae21ea49
    role: target
  - path: data/pathways/protocatechuate-ortho-cleavage.yaml
    sha256: 03c1fced81d599136ea6577ef4ff314cc428aab9171c522f0334fa4ccba418d4
    role: target
  - path: data/pathways/protocatechuate-para-cleavage.yaml
    sha256: 2a5e42e39a4e8eadb77eabf6f95896ecc7f001bafba04dec6eb74e7251169d89
    role: target
  - path: data/pathways/pseudouridine-degradation.yaml
    sha256: a11010f36c6af2d7f3304357cb920ba75fda74b067f01e0a64e9855123452159
    role: target
  - path: data/pathways/purine-deoxyribonucleosides-degradation.yaml
    sha256: 1412ec0cdb11458da71fd9b50a8c0827effefe28fe9ac949213db928d1e26087
    role: target
  - path: data/pathways/putrescine-degradation-ii.yaml
    sha256: 92dd03c0886b7b6a30ad87219f380e80c9e10ef087f3b10dacccdb69f3ab2b3f
    role: target
  - path: data/pathways/pyochelin-biosynthesis.yaml
    sha256: b3dfb5d0879dacd052e151477d6a48e422941752ea9b98ebd613064d5e3cde1b
    role: target
  - path: data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
    sha256: 03219ffa92913bcc306f4824c2c72aa39f862b17d14c96a0a9dd6daa9834bc42
    role: target
  - path: data/pathways/pyridoxal-5-phosphate-salvage-i.yaml
    sha256: 4fa125485b95ff8518056a42c7f22764cac006f812e66effbf250261ee7e4c29
    role: target
  - path: data/pathways/pyrimidine-deoxyribonucleosides-degradation.yaml
    sha256: 58ba6e176122f244f2bf59c155605347765e151e668699199d4ec3b474b273e6
    role: target
  - path: data/pathways/pyrimidine-deoxyribonucleotide-salvage.yaml
    sha256: 7e4d179cc40816a549edde196f4270960c09cfcb6dbc15882b85427e85013498
    role: target
  - path: data/pathways/pyrimidine-ribonucleosides-degradation.yaml
    sha256: e1f562227ad8aaf01f1a762e93c27030e4cae8779869670a416bfec79562c6d9
    role: target
  - path: data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml
    sha256: 78370a3d929d7580ff372192b4362e2a48c430e20e79066262a2aa5371b11baa
    role: target
  - path: data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml
    sha256: 6a91a3bcbe9679c27ae30c57357772f3ccd7fe98ec9ead2b6097c89e34f6a6a7
    role: target
  - path: data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml
    sha256: 1f4ea5bcf744449a6ad04d0da03b69c2e87e33dbfadc6db16a4de84d69407e31
    role: target
  - path: data/pathways/quinate-degradation-i.yaml
    sha256: a0c21af8e01b7a2653b226656b405fc197b0376b2d9ea4a6dbb6d003a3cc36cb
    role: target
  - path: data/pathways/quinate-degradation-ii.yaml
    sha256: 83445c4f5cedd104d29cd065771b384f0ea277ed74291e3569315a9d42b01d97
    role: target
  - path: data/pathways/riboneogenesis.yaml
    sha256: d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96
    role: target
  - path: data/pathways/ribose-phosphorylation.yaml
    sha256: 385101d166c9150936d81bb0f1c6c0d134b6ac1e6a6454d86e238ac0576e3d71
    role: target
  - path: data/pathways/s-adenosyl-l-methionine-cycle-i.yaml
    sha256: f400f02c796aeca00d11aa29f8783f7f672bd7f87d7d07f827bfbca36eac3e22
    role: target
  - path: data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml
    sha256: 4907cf3e7dc0469ef74274da8f536c99a4bfced9a177938d793c448e1db7724c
    role: target
  - path: data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
    sha256: 60750cb046b847a5d52458cff6eab771be2a9200755c259cfe8d87c4808e95fa
    role: target
  - path: data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml
    sha256: c703f90bedcee65918e9dda8a322c76984eac65759b018811030c42557ba81ce
    role: target
  - path: data/pathways/sedoheptulose-bisphosphate-bypass.yaml
    sha256: 6ed1607a4c17ffe56a6f5f8f123c44a0ff410c9a9965e11c3cde9ef23a4affe2
    role: target
  - path: data/pathways/shikimate-degradation-i.yaml
    sha256: ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808
    role: target
  - path: data/pathways/shikimate-degradation-ii.yaml
    sha256: a0f96cded480818165c794e5e954e96b2fa7f11e46910ad6574b6233480d13c1
    role: target
  - path: data/pathways/siroheme-biosynthesis.yaml
    sha256: 266f51a79c6f909fb6179937bf4c367f1f1d1c3a6fa1d314bec790466955548e
    role: target
  - path: data/pathways/spermidine-biosynthesis-and-metabolism-escherichia-coli.yaml
    sha256: 0adef1da2d818af7c62d7e3952b2115585b47b8f132ec189cde2b435d2721680
    role: target
  - path: data/pathways/spermidine-biosynthesis-i.yaml
    sha256: 6d94af196efc361a35dc72c2f8ef30fdf7def3a9e2597bd8bba8a2daaf235260
    role: target
  - path: data/pathways/spermine-biosynthesis.yaml
    sha256: da1f3ef31eb3d56e724b06474a42acb883f1947d17dd46415e36e0e99b5d3f56
    role: target
  - path: data/pathways/sphingolipid-biosynthesis-yeast.yaml
    sha256: d7c01da786b8f7261fbf51f1b83cd3125d5dd9a3dbbd4945e8a195c1e8cab6b7
    role: target
  - path: data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml
    sha256: 0c2e4ef99740885129888a71cf927b1ac8af45e7061c3e3b55ac0913d68dc224
    role: target
  - path: data/pathways/staphyloferrin-a-biosynthesis.yaml
    sha256: 5b4cd8d7838a19de2ba9c623bd59d321def6fffca45553895df646852d780e42
    role: target
  - path: data/pathways/staphyloferrin-b-biosynthesis.yaml
    sha256: 742930db9f8be218e6d69bf81c8b5d5ab3f460ed36d22d1660a4f18be6db26c1
    role: target
  - path: data/pathways/succinate-to-propanoate.yaml
    sha256: d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268
    role: target
  - path: data/pathways/sulfate-activation-for-sulfonation.yaml
    sha256: bcfb1267bed7de24a78f54d271e10b5ad9251648adcdd73c6882c5fb203cf904
    role: target
  - path: data/pathways/sulfoquinovose-degradation-i.yaml
    sha256: 741fc68daedf7cb7000b7cc5dc94ce5c0029fe9d30ce56d392c51a2aa9ac390c
    role: target
  - path: data/pathways/sulfoquinovose-degradation-ii.yaml
    sha256: 20a95c209243399b88a90fbecb0d8d310ebfb3094fc6ee4487352fdc2185c596
    role: target
  - path: data/pathways/superoxide-radicals-degradation.yaml
    sha256: f55995b9eac815491d9b7f5a57daa252e6111c9680612188fb1ff09a7a8698b9
    role: target
  - path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    sha256: 8d24e6ff858759aa4eaecd04b456ffa1b79c992bc090637f5cc8805a5ecbf492
    role: target
  - path: data/pathways/tca-cycle-detailed.yaml
    sha256: c574f799eef6b8b793decf52b1934a9f65ddac42893bb56ed5ed9d4134f837fe
    role: target
  - path: data/pathways/tetrahydrofolate-biosynthesis.yaml
    sha256: 926aeb5bbfafd09fa1e6d0599456545cfa89186f2f8bc88e5f6bb3a55d7b0d19
    role: target
  - path: data/pathways/tetrahydromonapterin-biosynthesis.yaml
    sha256: 0349c62d93993252bdab4e11a477eaca142eb516c59961721a317ed333eda182
    role: target
  - path: data/pathways/tetrapyrrole-biosynthesis.yaml
    sha256: 75ebed65fc0c1f3a60cb1941f878481a38a5ad719cc4f2512930fd96cd1a7df7
    role: target
  - path: data/pathways/thiamine-biosynthesis.yaml
    sha256: d8fbce15fc5a176811eef4f906bc148ef949814b3fd31c9fec756cdf08f3f0b4
    role: target
  - path: data/pathways/thiamine-diphosphate-biosynthesis-i.yaml
    sha256: 05fe1413e04fa3c2b95e44af1bda6c795ef53d3ea3529d18f6c42bac2e8079ea
    role: target
  - path: data/pathways/thioredoxin-pathway.yaml
    sha256: 8fa7373fe66807d9c12083c5fbe5e410ab5eaadf1100179590e488f74b8bafe0
    role: target
  - path: data/pathways/threonine-biosynthesis-from-aspartate-escherichia-coli.yaml
    sha256: 057078439b415869dfc977fafe4ae09029c11dd4c352fa25caaff70552a9d339
    role: target
  - path: data/pathways/threonine-degradation.yaml
    sha256: 267955a3bc387e34570713b9e42cb97528811728e89697c133654db94742d3c0
    role: target
  - path: data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml
    sha256: 2c9a01d5a4cbf5dd9b5a4d165cbe64e705ea2d7570f385f0b8dbf242a980be77
    role: target
  - path: data/pathways/trehalose-biosynthesis-i.yaml
    sha256: 2345d073b0ee434ab1a897653441d1bcd431ba0314e2265b9699fc6fd5a8eefb
    role: target
  - path: data/pathways/triglyceride-biosynthesis.yaml
    sha256: a6cf5919fcfd1d23095258909f13c819a81dbaf8fdae4d8f5aebb862428ac07a
    role: target
  - path: data/pathways/tryptophan-degradation.yaml
    sha256: caeb051e798194e96fac5ae22959fd91b6c3314fe69d6c0175721e6c6250bb01
    role: target
  - path: data/pathways/tyrosine-biosynthesis.yaml
    sha256: 97f352fdb43fa188391dc1a79702296c03c34fbdd8564cce53610528ca9793b0
    role: target
  - path: data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml
    sha256: 2546ba7c2b4a4b8d1ec2ff21d48672a1d164a7caf987b71aa67763c67a013efd
    role: target
  - path: data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml
    sha256: 4e8b67155682a12a450182016df2250fb9ab3ea340f059b8a620998c38407cb5
    role: target
  - path: data/pathways/ump-biosynthesis-i.yaml
    sha256: 7360c32e29f0aa492c9b6e3c73b28ec1d1c152258e7efcfd540beb1394546f16
    role: target
  - path: data/pathways/uracil-degradation-iii.yaml
    sha256: 2c155041e378508c99a430e72bd5fad82bde8bfc3c2b7b72569589a24c14f1c6
    role: target
  - path: data/pathways/urea-degradation-i.yaml
    sha256: 0c163d8fa329237abc323929210505f9f1051d0dcd5ae7756cdde96924236ab9
    role: target
  - path: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
    sha256: 9a13a458e243bec38a792d1b4f85346a6fd4ef9d53e531b3aaf02cc0b13ef831
    role: target
  - path: data/pathways/valine-degradation.yaml
    sha256: 5e0861fa7734fb946a476027e53a705ba475ea2052aa220e9cf5068b1e041202
    role: target
  - path: data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml
    sha256: 21b1b8c472788467007f47443a2d57bd00f47386f2f5222b5a8236a3e4e2681a
    role: target
  - path: data/pathways/xylose-metabolism.yaml
    sha256: 9d940d5a968e3b77aa250ff035c84eeb897f51a7f125e8b42bc9993840da7fc9
    role: target
  - path: data/pathways/zymosterol-biosynthesis.yaml
    sha256: b5f06648c0c03826ebe45a208140962b1d164edae1fa129ed3a1d70b9691408b
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 9d0eab4e76b22c194614cb7d309f2726e16331e5a7552c660bd5075e7497d8b2
    role: context
  - path: docs/CURATION.md
    sha256: 2a90c445177b52a179df6b4ee237dbff61e6bcf0e7918a798764dcb0e9292e0b
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 2d2c7d0a069f58fb74a9d44f5ccb8ecb61fee89360f9f0bca20798c801a02d16
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: output/sssom/source_mappings.sssom.tsv
    sha256: 3bdbdeb0c4ee7bf3ec64ea913565b1283dbf8821eb5af970406eeaa34792f9ae
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 58a152c9a02ae003bb7398292cb33a2ec22994c29b8273eb290bafe122134ce3
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: 23296ae17aeeea4518a972ee140640a69bf00e6b09203d04a3e13f9e13fc4790
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 46b16aba7e33cce89083077f64403769e6d2a890d58d269dca3dd79eb4829f9d
    role: context
scope:
  description: Full frozen-inventory record and category review of all 271 maintained
    pathway records in data/pathways/*.yaml at Git base e369fa425e64d4f794ce84e2fd71138a43660467.
  selection: All files matching data/pathways/*.yaml in CultureBotAI/PathwayMech.
  coverage: full
  population_size: 271
  reviewed_target_ids:
  - MetaCyc:PWY-5901
  - MetaCyc:PWY0-42
  - WikiPathways:WP5587
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-6543
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - gomodel:YeastPathways_PWY-6147
  - GO:0097288
  - MetaCyc:PWY0-1312
  - MetaCyc:ACETOACETATE-DEG-PWY
  - WikiPathways:WP5019
  - PathBank:SMP0002081
  - MetaCyc:P121-PWY
  - PathBank:SMP0002083
  - MetaCyc:PWY-6609
  - gomodel:YeastPathways_PWY-7220-1
  - MetaCyc:SALVADEHYPOX-PWY
  - gomodel:YeastPathways_PWY-7219
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-1241
  - GO:0019270
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - MetaCyc:PWY0-41
  - gomodel:YeastPathways_PWY-5694
  - MetaCyc:PWY-5705
  - gomodel:YeastPathways_PWY-5697
  - MetaCyc:GLCMANNANAUT-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - MetaCyc:PWY-5903
  - PathBank:SMP0002123
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:P321-PWY
  - gomodel:YeastPathways_PWY-5760-1
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - GO:0043427
  - gomodel:YeastPathways_PWY3O-4
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5417
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - gomodel:YeastPathways_PWY3O-15
  - MetaCyc:ARO-PWY
  - MIBiG:BGC0000829
  - MetaCyc:P2-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - MetaCyc:COA-PWY
  - GO:0036040
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:PWY-6376
  - KEGG:M00374
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-123
  - GO:0019305
  - MetaCyc:P101-PWY
  - KEGG:M00008
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-6075-1
  - MetaCyc:PWY-7255
  - gomodel:YeastPathways_PWY3O-4300
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1280
  - KEGG:M00373
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - MetaCyc:RIBOSYN2-PWY
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY-1801-1
  - MetaCyc:PWY0-521
  - GO:1901281
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:PWY-6223
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - WikiPathways:WP556
  - MetaCyc:PWY-5177
  - MetaCyc:GLUTATHIONESYN-PWY
  - gomodel:YeastPathways_PWYQT-4432
  - WikiPathways:WP392
  - gomodel:YeastPathways_PWY3O-48
  - MetaCyc:GLYCEROLMETAB-PWY
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - WikiPathways:WP478
  - gomodel:YeastPathways_GLYCOLYSIS
  - MetaCyc:PWY-5744
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - GO:1902000
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - gomodel:YeastPathways_PWY3O-402
  - WikiPathways:WP178
  - MetaCyc:PWY0-1338
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:PWY0-301
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - PathBank:SMP0002051
  - MetaCyc:CYSTSYN-PWY
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - gomodel:YeastPathways_PWY-5344
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - MetaCyc:LYXMET-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - gomodel:YeastPathways_PROUT-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - gomodel:YeastPathways_PWY-5651
  - MetaCyc:TYRSYN
  - gomodel:YeastPathways_PWY3O-4108
  - MetaCyc:VALSYN-PWY
  - gomodel:YeastPathways_PWY3O-4112
  - MIBiG:BGC0002072
  - gomodel:6882d2b800000609
  - MetaCyc:PWY0-501
  - gomodel:YeastPathways_PWY3O-1743
  - MetaCyc:PWY0-1300
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - gomodel:YeastPathways_PWY3O-64
  - MetaCyc:NONMEVIPP-PWY
  - gomodel:YeastPathways_PWY-901
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5453
  - PathBank:SMP0002077
  - MetaCyc:PWY-6048
  - gomodel:YeastPathways_IPPSYN-PWY
  - MetaCyc:PWY-6823
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - gomodel:YeastPathways_PWY-2301
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - gomodel:YeastPathways_PWY-5653
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - gomodel:YeastPathways_PWY3O-4106
  - WikiPathways:WP171
  - MetaCyc:PWY-6993
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:PWY0-1352
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-1801
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:PWY-8178
  - MetaCyc:OXIDATIVEPENT-PWY
  - WikiPathways:WP5060
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - MetaCyc:PWY-6289
  - MetaCyc:PWY0-321
  - gomodel:YeastPathways_PWY3O-4153
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:PWY-6534
  - MetaCyc:PWY0-1277
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - WikiPathways:WP71
  - MetaCyc:PANTO-PWY
  - MetaCyc:PWY1-3
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:P184-PWY
  - GO:0019618
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6019
  - PathBank:SMP0002089
  - PathBank:SMP0002067
  - GO:0042864
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-7181
  - GO:0010139
  - PathBank:SMP0002038
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_PWY3O-440
  - MetaCyc:PWY-7545
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:PWY-6416
  - PathBank:SMP0002406
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:PWY-6151
  - gomodel:YeastPathways_PWY-5041
  - MetaCyc:PWY-8132
  - gomodel:YeastPathways_YEAST-RNT-SALV
  - MetaCyc:PWY0-1517
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:PWY-6419
  - gomodel:YeastPathways_PWY-5194-1
  - PathBank:SMP0002097
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - MIBiG:BGC0000852
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY0-43
  - gomodel:YeastPathways_PWY-5340
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7722
  - gomodel:YeastPathways_DETOX1-PWY
  - MetaCyc:PWY-5838
  - WikiPathways:WP296
  - gomodel:YeastPathways_PWY-6614
  - MetaCyc:PWY0-1433
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-17
  - MetaCyc:THISYN-PWY
  - MetaCyc:THIOREDOX-PWY
  - PathBank:SMP0000992
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_PWY-5123
  - MetaCyc:TRESYN-PWY
  - WikiPathways:WP266
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-4120
  - WikiPathways:WP287
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - MetaCyc:PWY-5686
  - MetaCyc:PWY0-1471
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWY-6074-1
  exclusions:
  - target: research/pathway_additions/
    reason: Withheld research draft pathways (GO:0033468 and MetaCyc:PWY-5875) are
      not maintained records in data/pathways/*.yaml.
  - target: reports/yaml_record_review/ and reports/yaml_category_review/
    reason: Legacy prose reports remain historical evidence and are not maintained
      pathway targets.
targets:
- target_id: MetaCyc:PWY-5901
  path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
  label: 2,3-dihydroxybenzoate biosynthesis (MetaCyc:PWY-5901)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bdb60326e2ffa5db8e15939ce29bf57a12b992c1f2e56899c1cec3ecf01e2859
    description: Raw SHA-256 file digest of data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-42
  path: data/pathways/2-methylcitrate-cycle-i.yaml
  label: 2-methylcitrate cycle I (MetaCyc:PWY0-42)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0ccbcbcee61777f9f3265f5dec8c19ad5ce2ccf6051b54afe36fd1ed3bde40b7
    description: Raw SHA-256 file digest of data/pathways/2-methylcitrate-cycle-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-methylcitrate-cycle-i.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP5587
  path: data/pathways/2-phenylethanol-biosynthesis.yaml
  label: 2-phenylethanol biosynthesis (WikiPathways:WP5587)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 70936b88da1b369d40b0b68205cc3b31ab67df9df7b003aa0fad049594128798
    description: Raw SHA-256 file digest of data/pathways/2-phenylethanol-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-phenylethanol-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-2361
  path: data/pathways/3-oxoadipate-degradation.yaml
  label: 3-oxoadipate degradation (MetaCyc:PWY-2361)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 214ef2d38ede4bb4e919f6f53699491e7c53b8d9b5b858c6ba80084e5b067032
    description: Raw SHA-256 file digest of data/pathways/3-oxoadipate-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/3-oxoadipate-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6543
  path: data/pathways/4-aminobenzoate-biosynthesis-i.yaml
  label: 4-aminobenzoate biosynthesis I (MetaCyc:PWY-6543)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b0150b47850d17acbbe560a7d40a82d49a2f976a92ea15ab43c44df1a83c4b91
    description: Raw SHA-256 file digest of data/pathways/4-aminobenzoate-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/4-aminobenzoate-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  path: data/pathways/4-aminobutyrate-degradation.yaml
  label: 4-aminobutyrate degradation (gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e953a88e595f3446060152fa7cf2060859dc88b1693138768854c767bece6dda
    description: Raw SHA-256 file digest of data/pathways/4-aminobutyrate-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/4-aminobutyrate-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6121
  path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml
  label: 5-aminoimidazole ribonucleotide biosynthesis I (MetaCyc:PWY-6121)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 74516388c180b8832fbaf1f8a24a3e8f71ff737a4812191b8c3807dfd91ec250
    description: Raw SHA-256 file digest of data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6122
  path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml
  label: 5-aminoimidazole ribonucleotide biosynthesis II (MetaCyc:PWY-6122)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 324c587f1e7943d75cc48d6958fdf5f9e8b37d7427e2e132507192e670ba5ec9
    description: Raw SHA-256 file digest of data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-8130
  path: data/pathways/5-prime-deoxyadenosine-degradation-i.yaml
  label: 5'-deoxyadenosine degradation I (MetaCyc:PWY-8130)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c8ae12061fd62a5ff8c6861b6665e3ac6938b0fe611b9e3d8d6a1e11f33199a5
    description: Raw SHA-256 file digest of data/pathways/5-prime-deoxyadenosine-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/5-prime-deoxyadenosine-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-8131
  path: data/pathways/5-prime-deoxyadenosine-degradation-ii.yaml
  label: 5'-deoxyadenosine degradation II (MetaCyc:PWY-8131)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a367fac8ac036416baaabc9d64ae1d9927e66e87ad1bb96e2883725fd14ce68b
    description: Raw SHA-256 file digest of data/pathways/5-prime-deoxyadenosine-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/5-prime-deoxyadenosine-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-6147
  path: data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml
  label: 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (gomodel:YeastPathways_PWY-6147)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5d6d425f52d44d54819deed6bedf672322a09a2333db5305601003376bd327b3
    description: Raw SHA-256 file digest of data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: GO:0097288
  path: data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml
  label: 7-cyano-7-deazaguanine biosynthetic process (GO:0097288)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bbcf3f41f8c8996e045827f21672281f8f3040c2e51357eafb74e14fc050d4a6
    description: Raw SHA-256 file digest of data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1312
  path: data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml
  label: acetate and ATP formation from acetyl-CoA I (MetaCyc:PWY0-1312)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 98fa4218caba0e95fbee8fc6ce63d97166499afb3609391db88ab6f82a1f4e22
    description: Raw SHA-256 file digest of data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ACETOACETATE-DEG-PWY
  path: data/pathways/acetoacetate-degradation.yaml
  label: acetoacetate degradation (to acetyl CoA) (MetaCyc:ACETOACETATE-DEG-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 83b7cc0fe5a924f5531d7eb27d09f1a2f0a98b1252b92446f7fb3a198eed12e8
    description: Raw SHA-256 file digest of data/pathways/acetoacetate-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/acetoacetate-degradation.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP5019
  path: data/pathways/acetogenesis.yaml
  label: Acetogenesis (WikiPathways:WP5019)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 355b97b8d2c45e437b853c2447bfb14900507b40923991d49d0b68e9e7d3d54a
    description: Raw SHA-256 file digest of data/pathways/acetogenesis.yaml at frozen
      Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/acetogenesis.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002081
  path: data/pathways/adenine-and-adenosine-salvage-i-escherichia-coli.yaml
  label: Adenine and Adenosine Salvage I (PathBank:SMP0002081)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 11725db09e52dcd4de50dd62370510ce85319943078778485e8345ce3bd9b02c
    description: Raw SHA-256 file digest of data/pathways/adenine-and-adenosine-salvage-i-escherichia-coli.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenine-and-adenosine-salvage-i-escherichia-coli.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:P121-PWY
  path: data/pathways/adenine-and-adenosine-salvage-i.yaml
  label: adenine and adenosine salvage I (MetaCyc:P121-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: cc8721d24ba2236931ca151dcb035d9a9a671ce486acd950e724c9e7ffbf44d2
    description: Raw SHA-256 file digest of data/pathways/adenine-and-adenosine-salvage-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenine-and-adenosine-salvage-i.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002083
  path: data/pathways/adenine-and-adenosine-salvage-ii.yaml
  label: Adenine and Adenosine Salvage II (PathBank:SMP0002083)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ceac8c379a61f80a5b532e0c05834e5839cd9511b3446d386748c444092f8c57
    description: Raw SHA-256 file digest of data/pathways/adenine-and-adenosine-salvage-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenine-and-adenosine-salvage-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6609
  path: data/pathways/adenine-and-adenosine-salvage-iii.yaml
  label: adenine and adenosine salvage III (MetaCyc:PWY-6609)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: acafd5863d376489873aa366db9359ccaf57a693b688b472f78c89e26e3eae86
    description: Raw SHA-256 file digest of data/pathways/adenine-and-adenosine-salvage-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenine-and-adenosine-salvage-iii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-7220-1
  path: data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml
  label: adenosine deoxyribonucleotides de novo biosynthesis II (gomodel:YeastPathways_PWY-7220-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e7db816bd072061b45da17ca3dec4302f76c91781184501a28ebbc81f570123e
    description: Raw SHA-256 file digest of data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:SALVADEHYPOX-PWY
  path: data/pathways/adenosine-nucleotides-degradation-ii.yaml
  label: adenosine nucleotides degradation II (MetaCyc:SALVADEHYPOX-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: dc082d3edc6391cd6d85a503e3fbf3e77b96d34f0ee93eecad51f6e6272b1025
    description: Raw SHA-256 file digest of data/pathways/adenosine-nucleotides-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosine-nucleotides-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-7219
  path: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
  label: adenosine ribonucleotides de novo biosynthesis (gomodel:YeastPathways_PWY-7219)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 027459e5a871dcdb8f394ba6b30f2a6e01b92c4f98c8b6f9f232dfc12dbfb010
    description: Raw SHA-256 file digest of data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5509
  path: data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
  label: adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I (MetaCyc:PWY-5509)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8453146fc5cc438fd95be5acc623ba0f6fbe52e647ad21f1fa2dc535ee619184
    description: Raw SHA-256 file digest of data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-7971
  path: data/pathways/adenosylcobinamide-gdp-salvage-i.yaml
  label: adenosylcobinamide-GDP salvage from cobinamide I (MetaCyc:PWY-7971)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ee0c344a18b4b981b244ee8fcd00e651258990a3323d973fb0d978f47e26efef
    description: Raw SHA-256 file digest of data/pathways/adenosylcobinamide-gdp-salvage-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosylcobinamide-gdp-salvage-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1241
  path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
  label: ADP-L-glycero-beta-D-manno-heptose biosynthesis (MetaCyc:PWY0-1241)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: affa9eb37e5575d895dc7ae93173037ff18019e2a5e74012139b6aacb6febaf3
    description: Raw SHA-256 file digest of data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: GO:0019270
  path: data/pathways/aerobactin-biosynthesis.yaml
  label: aerobactin biosynthetic process (GO:0019270)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3e4e50965749a9fa9dfe6319fd1462cc8329c10b7f4ab5363e7b486f2f32e3d4
    description: Raw SHA-256 file digest of data/pathways/aerobactin-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/aerobactin-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  path: data/pathways/aerobic-glycerol-degradation.yaml
  label: aerobic glycerol degradation (gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 89d0c0e1202bcc20bdc120764d454b4a1fa4112d14d82aa61bebbc46dcf92699
    description: Raw SHA-256 file digest of data/pathways/aerobic-glycerol-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/aerobic-glycerol-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-41
  path: data/pathways/allantoin-degradation-iv-anaerobic.yaml
  label: allantoin degradation IV (anaerobic) (MetaCyc:PWY0-41)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bf7b150b5b6d0647a1f2b7f4d90c8b3e5ff3c6e73c36f00acc1fe542ba1f034c
    description: Raw SHA-256 file digest of data/pathways/allantoin-degradation-iv-anaerobic.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/allantoin-degradation-iv-anaerobic.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5694
  path: data/pathways/allantoin-degradation-to-glyoxylate-i.yaml
  label: allantoin degradation to glyoxylate I (gomodel:YeastPathways_PWY-5694)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 20a2143fca48392111bbf273148db8cd7128139ade7a74c00e1b8c26e3f4e58b
    description: Raw SHA-256 file digest of data/pathways/allantoin-degradation-to-glyoxylate-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/allantoin-degradation-to-glyoxylate-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5705
  path: data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
  label: allantoin degradation to glyoxylate III (MetaCyc:PWY-5705)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1fe731570ceb2038b0b153686be184c99afbd82ab6ba9a9516694b2277de1b37
    description: Raw SHA-256 file digest of data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5697
  path: data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml
  label: allantoin degradation to ureidoglycolate I (urea producing) (gomodel:YeastPathways_PWY-5697)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 962f07ce5ea3130396bc51df0bab3892ceb8bbfc45326a76a50f7a82579168d0
    description: Raw SHA-256 file digest of data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLCMANNANAUT-PWY
  path: data/pathways/amino-sugar-superpathway.yaml
  label: superpathway of N-acetylglucosamine, N-acetylmannosamine and N-acetylneuraminate
    degradation (MetaCyc:GLCMANNANAUT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1c93e912f2e349fbfab5458f309f526fcfc9d381560ac04ba35b7c442f2295f8
    description: Raw SHA-256 file digest of data/pathways/amino-sugar-superpathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/amino-sugar-superpathway.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_ASPBIO-PWY
  path: data/pathways/aspartate-biosynthesis.yaml
  label: aspartate biosynthesis (gomodel:YeastPathways_ASPBIO-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 20016b7d818f0dc7e4cb17610ef76abfba9265db8d24b0af5b3fab496685bf87
    description: Raw SHA-256 file digest of data/pathways/aspartate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/aspartate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_SO4ASSIM-PWY
  path: data/pathways/assimilatory-sulfate-reduction.yaml
  label: assimilatory sulfate reduction I (gomodel:YeastPathways_SO4ASSIM-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 376aa99c28b3b509414bdec962bfcc75a5a7199cf3b12eb815466dc035084223
    description: Raw SHA-256 file digest of data/pathways/assimilatory-sulfate-reduction.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/assimilatory-sulfate-reduction.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5903
  path: data/pathways/bacillibactin-biosynthesis.yaml
  label: bacillibactin biosynthesis (MetaCyc:PWY-5903)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: aaf46730530dc9ae86fd18f8b382baebbcf0f37b79342b7eebf18e0e64ebeafa
    description: Raw SHA-256 file digest of data/pathways/bacillibactin-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/bacillibactin-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002123
  path: data/pathways/baesr-two-component-signal-transduction.yaml
  label: BaeSR Two-Component Signal Transduction System (PathBank:SMP0002123)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1cf9262a0df376a19517b3f55ccaac67dacc8af8ce58bd8a1b2046e93a951824
    description: Raw SHA-256 file digest of data/pathways/baesr-two-component-signal-transduction.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/baesr-two-component-signal-transduction.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-2503
  path: data/pathways/benzoate-degradation-i-aerobic.yaml
  label: benzoate degradation I (aerobic) (MetaCyc:PWY-2503)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1f5d025ef0b00ff3a1bdbaa90bff4f7e38068ba608d9b5e179604c705e0de8f7
    description: Raw SHA-256 file digest of data/pathways/benzoate-degradation-i-aerobic.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/benzoate-degradation-i-aerobic.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-1361
  path: data/pathways/benzoyl-coa-degradation-i-aerobic.yaml
  label: benzoyl-CoA degradation I (aerobic) (MetaCyc:PWY-1361)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 009e8e6796052e3c1dca8af95a55edaf69273545d6606ebd41aed4369cb7624f
    description: Raw SHA-256 file digest of data/pathways/benzoyl-coa-degradation-i-aerobic.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/benzoyl-coa-degradation-i-aerobic.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:CENTBENZCOA-PWY
  path: data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml
  label: benzoyl-CoA degradation II (anaerobic) (MetaCyc:CENTBENZCOA-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e43e6ad5563c38af738e8f1c7b733510072b531196ce435395896b62951c6ab9
    description: Raw SHA-256 file digest of data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:P321-PWY
  path: data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml
  label: benzoyl-CoA degradation III (anaerobic) (MetaCyc:P321-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 40fa37e63c5be6ec6c9d33bf67f4bf06e597fc4c9b12514d34401379b124ad51
    description: Raw SHA-256 file digest of data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5760-1
  path: data/pathways/beta-alanine-biosynthesis-iv.yaml
  label: beta-alanine biosynthesis IV (gomodel:YeastPathways_PWY-5760-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0b24a16ea8a7fb91fe1ead37cb5868d9ce4c8b8d36f04e788e2e9030da6b8972
    description: Raw SHA-256 file digest of data/pathways/beta-alanine-biosynthesis-iv.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/beta-alanine-biosynthesis-iv.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  path: data/pathways/biotin-biosynthesis-i.yaml
  label: biotin biosynthesis I (MetaCyc:BIOTIN-BIOSYNTHESIS-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b95b35d22f813ecb167b068554b4cee9e44bdb2d0ce4765338e82ecd84df0dff
    description: Raw SHA-256 file digest of data/pathways/biotin-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/biotin-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:CALVIN-PWY
  path: data/pathways/calvin-cycle.yaml
  label: Calvin-Benson-Bassham cycle (MetaCyc:CALVIN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e5b770e60e481068b847e7dfe60b3f85681e36f25952f2c4308f82b0133d05a9
    description: Raw SHA-256 file digest of data/pathways/calvin-cycle.yaml at frozen
      Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/calvin-cycle.yaml
    role: maintained pathway YAML
- target_id: GO:0043427
  path: data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml
  label: carbon fixation by 3-hydroxypropionate cycle (GO:0043427)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c2c307e749e73e33de865c3ea92bee0b22a5828396af79066061299976a89bec
    description: Raw SHA-256 file digest of data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-4
  path: data/pathways/carnitine-shuttle.yaml
  label: carnitine shuttle (gomodel:YeastPathways_PWY3O-4)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b30ce5a608752d19a0f22de39a50c261be96e4d8f7cd5940759a4de49eff8e28
    description: Raw SHA-256 file digest of data/pathways/carnitine-shuttle.yaml at
      frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/carnitine-shuttle.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5415
  path: data/pathways/catechol-degradation-i.yaml
  label: catechol degradation I (meta-cleavage pathway) (MetaCyc:PWY-5415)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 29b073a0a5aca884b9decf6b86a41c2a018c62dc0818c7e33ec17065152d781c
    description: Raw SHA-256 file digest of data/pathways/catechol-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/catechol-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5420
  path: data/pathways/catechol-degradation-ii.yaml
  label: catechol degradation II (meta-cleavage pathway) (MetaCyc:PWY-5420)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4931e9a8cc5ae9f55c434d942c70fc65c75ad73a49e878bd34fbcfc4250df110
    description: Raw SHA-256 file digest of data/pathways/catechol-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/catechol-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5417
  path: data/pathways/catechol-degradation-iii.yaml
  label: catechol degradation III (ortho-cleavage pathway) (MetaCyc:PWY-5417)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b30573a380b358a9b0228f8e3e2689943ecf828aa01ae790f281ba3fe617e603
    description: Raw SHA-256 file digest of data/pathways/catechol-degradation-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/catechol-degradation-iii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  path: data/pathways/catechol-degradation-to-beta-ketoadipate.yaml
  label: catechol degradation to β-ketoadipate (MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 39ca1eedee87cb3ee01d9d698359bdfdee505b1fa05e160154e976fa6514e6c6
    description: Raw SHA-256 file digest of data/pathways/catechol-degradation-to-beta-ketoadipate.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/catechol-degradation-to-beta-ketoadipate.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-15
  path: data/pathways/chitin-biosynthesis.yaml
  label: chitin biosynthesis (gomodel:YeastPathways_PWY3O-15)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 46627a456564e07dfc4dcb1e41383e6aeefebc3e52f1fe3a5b26e18f92da8361
    description: Raw SHA-256 file digest of data/pathways/chitin-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/chitin-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ARO-PWY
  path: data/pathways/chorismate-biosynthesis-i.yaml
  label: chorismate biosynthesis I (MetaCyc:ARO-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: dc5c2fa8d319b3e1909f59982d6891e0de76eecc00bd3850da469507f0a1875a
    description: Raw SHA-256 file digest of data/pathways/chorismate-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/chorismate-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MIBiG:BGC0000829
  path: data/pathways/chromobacterium-violaceum-violacein-biosynthetic-gene-cluster.yaml
  label: Chromobacterium violaceum violacein biosynthetic gene cluster (MIBiG:BGC0000829)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a2c389bdea0ba8574ded73b47ae67cc5011105f4579401661197ffcb0e689d0a
    description: Raw SHA-256 file digest of data/pathways/chromobacterium-violaceum-violacein-biosynthetic-gene-cluster.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/chromobacterium-violaceum-violacein-biosynthetic-gene-cluster.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:P2-PWY
  path: data/pathways/citrate-lyase-activation.yaml
  label: citrate lyase activation (MetaCyc:P2-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c76b50f65ef43e599ca16a9789144840660b52a4dc1d9adcd46fb8c5fecdd450
    description: Raw SHA-256 file digest of data/pathways/citrate-lyase-activation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/citrate-lyase-activation.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_CITRUL-BIO2-PWY
  path: data/pathways/citrulline-biosynthesis.yaml
  label: citrulline biosynthesis (gomodel:YeastPathways_CITRUL-BIO2-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 990b97ed6aec1c619dfb5a4a53b098a3c4ca4b5ab46ab537d275cbfe7d10d80b
    description: Raw SHA-256 file digest of data/pathways/citrulline-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/citrulline-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:COA-PWY
  path: data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml
  label: coenzyme A biosynthesis I (prokaryotic) (MetaCyc:COA-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bdca4a5ea4688a5a4f4ab4f18e93dc3501b40e0bfe00eb7fa1621998295f438d
    description: Raw SHA-256 file digest of data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml
    role: maintained pathway YAML
- target_id: GO:0036040
  path: data/pathways/curcumin-degradation.yaml
  label: curcumin catabolic process (GO:0036040)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 814e063d50371068e9a7f3d6238b0f6ad76e172f6072c59b570cafdba0cb407b
    description: Raw SHA-256 file digest of data/pathways/curcumin-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/curcumin-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:CYANCAT-PWY
  path: data/pathways/cyanate-degradation.yaml
  label: cyanate degradation (MetaCyc:CYANCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bc0ac1b2ce20a5c3e0eeb98d220e6dc55513ed5eb4fcd9aaadcace5ec1899d84
    description: Raw SHA-256 file digest of data/pathways/cyanate-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/cyanate-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:DARABCAT-PWY
  path: data/pathways/d-arabinose-degradation-i.yaml
  label: D-arabinose degradation I (MetaCyc:DARABCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e4c05a00929557b8cabcdc26f057f7ac788d85ae82de515828806a79dd98f886
    description: Raw SHA-256 file digest of data/pathways/d-arabinose-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-arabinose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GALACTARDEG-PWY
  path: data/pathways/d-galactarate-degradation-i.yaml
  label: D-galactarate degradation I (MetaCyc:GALACTARDEG-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6f637a08b7bb39df952c27a96313c60883ae53ff15fd9597972ded54bf31bc26
    description: Raw SHA-256 file digest of data/pathways/d-galactarate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galactarate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GALACTCAT-PWY
  path: data/pathways/d-galactonate-degradation.yaml
  label: D-galactonate degradation (MetaCyc:GALACTCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 51e71bf9bd2d0888f6f3e56f98eb4b4fab32034266bfe8dfeeb375529afc3f84
    description: Raw SHA-256 file digest of data/pathways/d-galactonate-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galactonate-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GALACTUROCAT-PWY
  path: data/pathways/d-galacturonate-degradation-i.yaml
  label: D-galacturonate degradation I (MetaCyc:GALACTUROCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: dafcc96c28d5d1e9c36f38a9b9701217e64b32cebffcb7fd4516bb1557a5d562
    description: Raw SHA-256 file digest of data/pathways/d-galacturonate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galacturonate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLUCARDEG-PWY
  path: data/pathways/d-glucarate-degradation-i.yaml
  label: D-glucarate degradation I (MetaCyc:GLUCARDEG-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c48cbb09d6b97812ea6d84a3229eae34400a68bccc38192553fff2d376ba4ad1
    description: Raw SHA-256 file digest of data/pathways/d-glucarate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-glucarate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:XYLCAT-PWY
  path: data/pathways/d-xylose-degradation-i.yaml
  label: D-xylose degradation I (MetaCyc:XYLCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4faccd4d9a05d6132f6f24e06d481e0c1be1386f4914cecd8abcab6e23c50ce2
    description: Raw SHA-256 file digest of data/pathways/d-xylose-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-xylose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6376
  path: data/pathways/desferrioxamine-b-biosynthesis.yaml
  label: desferrioxamine B biosynthesis (MetaCyc:PWY-6376)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ab6b7808c564fc2bbddaa1fea159f0927e2ec2f73b9890e7ab360c5e3718a9dd
    description: Raw SHA-256 file digest of data/pathways/desferrioxamine-b-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/desferrioxamine-b-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: KEGG:M00374
  path: data/pathways/dicarboxylate-hydroxybutyrate-cycle.yaml
  label: Dicarboxylate-hydroxybutyrate cycle (KEGG:M00374)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bf5316958e94eae4e2e09a864dca8e45d8997b041d7e26c991c9633f24449209
    description: Raw SHA-256 file digest of data/pathways/dicarboxylate-hydroxybutyrate-cycle.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/dicarboxylate-hydroxybutyrate-cycle.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-1565
  path: data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml
  label: dolichyl glucosyl phosphate biosynthesis (gomodel:YeastPathways_PWY3O-1565)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1fe23e30c0e1d0e14fff70678f966812c1c1a4bc602441076ad041c232190ef8
    description: Raw SHA-256 file digest of data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-123
  path: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
  label: dolichyl phosphate D-mannose biosynthesis (gomodel:YeastPathways_PWY3O-123)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6fa9f8a6697af1bb35b060943f7b16c0d350366bbaa8ae9268456c45683f5c62
    description: Raw SHA-256 file digest of data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: GO:0019305
  path: data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
  label: dTDP-rhamnose biosynthetic process (GO:0019305)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 75ec1f4ffa088e6647182cde01b7959df161261cb03d48cd471609b2a9b42de9
    description: Raw SHA-256 file digest of data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:P101-PWY
  path: data/pathways/ectoine-biosynthesis.yaml
  label: ectoine biosynthesis (MetaCyc:P101-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9f9d3c2c3de5ca5a3c59df1c3cb056fdf8cd60c0fb922feb902d5549151478dc
    description: Raw SHA-256 file digest of data/pathways/ectoine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ectoine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: KEGG:M00008
  path: data/pathways/entner-doudoroff-pathway.yaml
  label: Entner-Doudoroff pathway, glucose-6P => glyceraldehyde-3P + pyruvate (KEGG:M00008)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6ff158fbca9a78f73f9ebf493e1f068fd2d5115ec73a0e42657a18f35a8867ad
    description: Raw SHA-256 file digest of data/pathways/entner-doudoroff-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/entner-doudoroff-pathway.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5670-1
  path: data/pathways/epoxysqualene-biosynthesis.yaml
  label: epoxysqualene biosynthesis (gomodel:YeastPathways_PWY-5670-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: da3b71fd30801bc13f92ba2226badc86c1376f40b78bd622c9b8a4ff132d1fd2
    description: Raw SHA-256 file digest of data/pathways/epoxysqualene-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/epoxysqualene-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-6075-1
  path: data/pathways/ergosterol-biosynthesis-i.yaml
  label: ergosterol biosynthesis I (gomodel:YeastPathways_PWY-6075-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b8f7c7cd77268474d0b3d17f2109c0f4da9131eb2e040907a188127ed7b98bc6
    description: Raw SHA-256 file digest of data/pathways/ergosterol-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergosterol-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-7255
  path: data/pathways/ergothioneine-biosynthesis-i.yaml
  label: ergothioneine biosynthesis I (bacteria) (MetaCyc:PWY-7255)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6d2fb20f5a664a6b7e43e9efb48ac1b65fd59a3e5c5daa1aa95b6bae35184dec
    description: Raw SHA-256 file digest of data/pathways/ergothioneine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-4300
  path: data/pathways/ethanol-degradation.yaml
  label: ethanol degradation (gomodel:YeastPathways_PWY3O-4300)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: fc50f4fe0251b9a24c2c0be359c4349ef12194556f510f390132dc556094031a
    description: Raw SHA-256 file digest of data/pathways/ethanol-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ethanol-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1477
  path: data/pathways/ethanolamine-utilization.yaml
  label: ethanolamine utilization (MetaCyc:PWY0-1477)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e
    description: Raw SHA-256 file digest of data/pathways/ethanolamine-utilization.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ethanolamine-utilization.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1280
  path: data/pathways/ethylene-glycol-degradation.yaml
  label: ethylene glycol degradation (MetaCyc:PWY0-1280)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c247d9c205fc14ac5bb0d1e6de57c54d06aca5a484eb99b9e8e694c9d6f2e6de
    description: Raw SHA-256 file digest of data/pathways/ethylene-glycol-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ethylene-glycol-degradation.yaml
    role: maintained pathway YAML
- target_id: KEGG:M00373
  path: data/pathways/ethylmalonyl-coa-pathway.yaml
  label: Ethylmalonyl pathway (KEGG:M00373)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8c4d525a0285213cbc92bed1045a3c69125135abede0b66fed548dcab8e8913d
    description: Raw SHA-256 file digest of data/pathways/ethylmalonyl-coa-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ethylmalonyl-coa-pathway.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_FASYN-ELONG2-PWY
  path: data/pathways/fatty-acid-elongation.yaml
  label: fatty acid elongation (gomodel:YeastPathways_FASYN-ELONG2-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b62921d961d820d8ff589720e08dd002e146b9989aee2c82b045d810bf0351b3
    description: Raw SHA-256 file digest of data/pathways/fatty-acid-elongation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/fatty-acid-elongation.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_YEAST-FAO-PWY
  path: data/pathways/fatty-acid-oxidation-pathway.yaml
  label: fatty acid oxidation pathway (gomodel:YeastPathways_YEAST-FAO-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bfde333f007a3a73eb3172619e731d189e131a628653ad171bf4252798ed593e
    description: Raw SHA-256 file digest of data/pathways/fatty-acid-oxidation-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/fatty-acid-oxidation-pathway.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:RIBOSYN2-PWY
  path: data/pathways/flavin-biosynthesis-i.yaml
  label: flavin biosynthesis I (MetaCyc:RIBOSYN2-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 417d94b49af861613f07f76e2f4dc0d6b4d44123a57547a1c05c2aca91e2a025
    description: Raw SHA-256 file digest of data/pathways/flavin-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/flavin-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-697
  path: data/pathways/folate-interconversions.yaml
  label: folate interconversions (gomodel:YeastPathways_PWY3O-697)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0823d8deed478b16f05f0df675c9b453eb65714f78aed067188bbc168b1cbcb5
    description: Raw SHA-256 file digest of data/pathways/folate-interconversions.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/folate-interconversions.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-1801-1
  path: data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml
  label: formaldehyde oxidation II (glutathione-dependent) (gomodel:YeastPathways_PWY-1801-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: cad662956612f880a1fa23e5dd729af944a7cee3c09d93eb8abce7b2a2aceebb
    description: Raw SHA-256 file digest of data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-521
  path: data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
  label: fructoselysine and psicoselysine degradation (MetaCyc:PWY0-521)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3e5b25fc917a30aca70b1dbdce4c70cb7b2d69f595b1f0f13d391812b7cdcb93
    description: Raw SHA-256 file digest of data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
    role: maintained pathway YAML
- target_id: GO:1901281
  path: data/pathways/fructoselysine-catabolic-process.yaml
  label: fructoselysine catabolic process (GO:1901281)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e9e80038a8671da109e8453523439ed921fe7810bb96b24f55dc532b4dd6ca5f
    description: Raw SHA-256 file digest of data/pathways/fructoselysine-catabolic-process.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/fructoselysine-catabolic-process.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  path: data/pathways/galactose-degradation.yaml
  label: galactose degradation (gomodel:YeastPathways_YEAST-GALACT-METAB-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: afb4d246ee5305b34e0d960cabb3a25e30d6289e0899133cf5eb5cd6aaba2860
    description: Raw SHA-256 file digest of data/pathways/galactose-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/galactose-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GALLATE-DEGRADATION-II-PWY
  path: data/pathways/gallate-degradation-i.yaml
  label: gallate degradation I (MetaCyc:GALLATE-DEGRADATION-II-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a6e0e8f52880ccb651e02526dbd627240ec7e46a637d2eabfd790846156d21b0
    description: Raw SHA-256 file digest of data/pathways/gallate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/gallate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GALLATE-DEGRADATION-I-PWY
  path: data/pathways/gallate-degradation-ii.yaml
  label: gallate degradation II (MetaCyc:GALLATE-DEGRADATION-I-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 72e4685f14ff3a6a9d5cd5c7b9cd27d5fa54592355a5191fa5cf821d07a19353
    description: Raw SHA-256 file digest of data/pathways/gallate-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/gallate-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6223
  path: data/pathways/gentisate-degradation-i.yaml
  label: gentisate degradation I (MetaCyc:PWY-6223)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 272e475b3bb872475bba938c5e5016b52b63e21dc8c9dea772e25ba78524c064
    description: Raw SHA-256 file digest of data/pathways/gentisate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/gentisate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_GLUCONEO-PWY-1
  path: data/pathways/gluconeogenesis-i.yaml
  label: gluconeogenesis I (gomodel:YeastPathways_GLUCONEO-PWY-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ed359fc88a819b1ff6c51b8b2e10cf399b184cbe25df7c74883d560311296a15
    description: Raw SHA-256 file digest of data/pathways/gluconeogenesis-i.yaml at
      frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/gluconeogenesis-i.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP556
  path: data/pathways/glutamate-degradation-i.yaml
  label: Glutamate degradation I (WikiPathways:WP556)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5bfde8cb993cedc9cfc1534157d0c63121bcdbcc75b1c915274e381ada8524ce
    description: Raw SHA-256 file digest of data/pathways/glutamate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutamate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5177
  path: data/pathways/glutaryl-coa-degradation.yaml
  label: glutaryl-CoA degradation (MetaCyc:PWY-5177)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3c2ac2ae8443a7bdac87bd8ca9e612eee869fb479f3625231fadf84658e16317
    description: Raw SHA-256 file digest of data/pathways/glutaryl-coa-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutaryl-coa-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLUTATHIONESYN-PWY
  path: data/pathways/glutathione-biosynthesis.yaml
  label: glutathione biosynthesis (MetaCyc:GLUTATHIONESYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e6b762e025742ca9cf0766d8d2d8b3f15e1c2b0078e7af2ab21bab1a43d8dba7
    description: Raw SHA-256 file digest of data/pathways/glutathione-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutathione-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWYQT-4432
  path: data/pathways/glutathione-degradation.yaml
  label: glutathione degradation (gomodel:YeastPathways_PWYQT-4432)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 90700db818d7b32cf46b41e4bf53c234f070829e779a5b80ee8537b32f4a808a
    description: Raw SHA-256 file digest of data/pathways/glutathione-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutathione-degradation.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP392
  path: data/pathways/glutathione-glutaredoxin-redox-reaction.yaml
  label: Glutathione-glutaredoxin redox reaction (WikiPathways:WP392)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: cbee4a5a80e9340376ae64bdd05ccc7a3aa6096630f24324af11fca9eca97977
    description: Raw SHA-256 file digest of data/pathways/glutathione-glutaredoxin-redox-reaction.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutathione-glutaredoxin-redox-reaction.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-48
  path: data/pathways/glycerol-biosynthesis.yaml
  label: glycerol biosynthesis (gomodel:YeastPathways_PWY3O-48)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ac0ea900a57b2147297dc7bde6c767bda334664a92c406cc367b6f6ee8430cbc
    description: Raw SHA-256 file digest of data/pathways/glycerol-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycerol-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLYCEROLMETAB-PWY
  path: data/pathways/glycerol-degradation-v.yaml
  label: glycerol degradation V (MetaCyc:GLYCEROLMETAB-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 17004e2911d28d42612c2010bf28d3339dc7f5f8a5af1e49b94cb4bae98ab2ba
    description: Raw SHA-256 file digest of data/pathways/glycerol-degradation-v.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycerol-degradation-v.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_GLYCLEAV-PWY
  path: data/pathways/glycine-cleavage.yaml
  label: glycine cleavage (gomodel:YeastPathways_GLYCLEAV-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 74b9d679808b3950cd1bd0bf2ed8574e4abf9f61f203c8b5538e5e4b46a483db
    description: Raw SHA-256 file digest of data/pathways/glycine-cleavage.yaml at
      frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycine-cleavage.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP478
  path: data/pathways/glycogen-catabolism.yaml
  label: Glycogen catabolism (WikiPathways:WP478)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 72b8e29697334f849212bd9827055265fb375fbc3f2847b7b062d6a9705e6cce
    description: Raw SHA-256 file digest of data/pathways/glycogen-catabolism.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycogen-catabolism.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_GLYCOLYSIS
  path: data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml
  label: glycolysis I (from glucose 6-phosphate) (gomodel:YeastPathways_GLYCOLYSIS)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0a9fd40d1eaa77a75af58968732d361457618636d5d81775200f3cf88c88193d
    description: Raw SHA-256 file digest of data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5744
  path: data/pathways/glyoxylate-assimilation.yaml
  label: glyoxylate assimilation (MetaCyc:PWY-5744)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 462022906e961f49ceb92c32fcc7d6f834b6e55f89ead1b1f786a91d11258969
    description: Raw SHA-256 file digest of data/pathways/glyoxylate-assimilation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-assimilation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLYOXYLATE-BYPASS
  path: data/pathways/glyoxylate-cycle.yaml
  label: glyoxylate cycle (MetaCyc:GLYOXYLATE-BYPASS)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bd5793fee6b8af7da1e67eece20ebfd65004a48bdfe4d4afbbfb3d544c8138b9
    description: Raw SHA-256 file digest of data/pathways/glyoxylate-cycle.yaml at
      frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-cycle.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6579
  path: data/pathways/guanine-and-guanosine-salvage.yaml
  label: superpathway of guanine and guanosine salvage (MetaCyc:PWY-6579)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7133352b12d3cd8579acc128b2896b9247dd8503f06c339d2526e137eb17e58e
    description: Raw SHA-256 file digest of data/pathways/guanine-and-guanosine-salvage.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/guanine-and-guanosine-salvage.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-7221
  path: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
  label: guanosine ribonucleotides de novo biosynthesis (gomodel:YeastPathways_PWY-7221)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2d1a05f95a978e13f16c2fb551b60633b34b8bd5397de9214411b99c95e090be
    description: Raw SHA-256 file digest of data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  path: data/pathways/heme-biosynthesis-i-aerobic.yaml
  label: heme b biosynthesis I (aerobic) (gomodel:YeastPathways_HEME-BIOSYNTHESIS-II)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a82d6893480d683143a1d54350b3f183de5a0d1fcb4ff59a16d146f054d9fa66
    description: Raw SHA-256 file digest of data/pathways/heme-biosynthesis-i-aerobic.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/heme-biosynthesis-i-aerobic.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_HEXPPSYN-PWY-2
  path: data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml
  label: hexaprenyl diphosphate biosynthesis (gomodel:YeastPathways_HEXPPSYN-PWY-2)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e97493175ab78edaaa100e8e0924f5c8ad4ef3d31ce7b13368c9ca067707a02e
    description: Raw SHA-256 file digest of data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  path: data/pathways/homocysteine-and-cysteine-interconversion.yaml
  label: homocysteine and cysteine interconversion (gomodel:YeastPathways_HOMOCYS-CYS-CONVERT)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c9fde1235193ea94d4ba624d0c7966c994ec54ef0e30fb71dde686a5c6a78630
    description: Raw SHA-256 file digest of data/pathways/homocysteine-and-cysteine-interconversion.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/homocysteine-and-cysteine-interconversion.yaml
    role: maintained pathway YAML
- target_id: GO:1902000
  path: data/pathways/homogentisate-degradation.yaml
  label: homogentisate catabolic process (GO:1902000)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a833e707d3dbd92ff09194e1d19b7c419aa3e2c4c45d3a53064c8915a2d755d2
    description: Raw SHA-256 file digest of data/pathways/homogentisate-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/homogentisate-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5789
  path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
  label: 3-hydroxypropanoate/4-hydroxybutanate cycle (MetaCyc:PWY-5789)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 254d42b0e04165e9b84f95692e1f4cd482f259fe28b2fd1fbd45485bbf3536fa
    description: Raw SHA-256 file digest of data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6123
  path: data/pathways/inosine-5-phosphate-biosynthesis-i.yaml
  label: inosine-5'-phosphate biosynthesis I (MetaCyc:PWY-6123)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 74e4cd1621fc270ba365ef411b3079692de075024264f7e8866f6b0d9442938e
    description: Raw SHA-256 file digest of data/pathways/inosine-5-phosphate-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inosine-5-phosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6124
  path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
  label: inosine-5'-phosphate biosynthesis II (MetaCyc:PWY-6124)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d676ccc1740fc538486cc7c9664bd5e3e2c89cc2aadd74bcffd586cce6aa7b97
    description: Raw SHA-256 file digest of data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-402
  path: data/pathways/inositol-phosphate-biosynthesis.yaml
  label: inositol phosphate biosynthesis (gomodel:YeastPathways_PWY3O-402)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2fe2d2ba88e85693135d52e2bb72ab7ca37cf41d2e9f879fdb602241d63a6fc3
    description: Raw SHA-256 file digest of data/pathways/inositol-phosphate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inositol-phosphate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP178
  path: data/pathways/isoleucine-degradation.yaml
  label: Isoleucine degradation (WikiPathways:WP178)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8d93b27c9181bb58990868d80e7443b52c161f5878909d0ff70f0c7147b1857b
    description: Raw SHA-256 file digest of data/pathways/isoleucine-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/isoleucine-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1338
  path: data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml
  label: polymyxin resistance (MetaCyc:PWY0-1338)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6c9f87fc7a7b6ae411092a5e34330df52f18bb574a09b25eae79fc48182d3955
    description: Raw SHA-256 file digest of data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ARABCAT-PWY
  path: data/pathways/l-arabinose-degradation-i.yaml
  label: L-arabinose degradation I (MetaCyc:ARABCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 37cfa161adf3d8ab8b4b01a018d387d60b33817bd5908b0d1dc73c91ee7d001e
    description: Raw SHA-256 file digest of data/pathways/l-arabinose-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arabinose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ARGSYN-PWY
  path: data/pathways/l-arginine-biosynthesis-i.yaml
  label: L-arginine biosynthesis I (via L-ornithine) (MetaCyc:ARGSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bf299cc075fee4f21e6cb76b71cdcddc70c06dbd8db17ab9448144f95dd7535c
    description: Raw SHA-256 file digest of data/pathways/l-arginine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_ARGSYNBSUB-PWY
  path: data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml
  label: L-arginine biosynthesis II (acetyl cycle) (gomodel:YeastPathways_ARGSYNBSUB-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: cce1353fcdd659940db26fec1dd8dce7df198977f01837354798ac91756f5ac4
    description: Raw SHA-256 file digest of data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:AST-PWY
  path: data/pathways/l-arginine-degradation-ii-ast-pathway.yaml
  label: L-arginine degradation II (AST pathway) (MetaCyc:AST-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: fe02deb131bfe53eedb770ed50278885955e7a67d97859184142aea6ae35c86b
    description: Raw SHA-256 file digest of data/pathways/l-arginine-degradation-ii-ast-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-ii-ast-pathway.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ARGDEG-III-PWY
  path: data/pathways/l-arginine-degradation-iv.yaml
  label: L-arginine degradation IV (arginine decarboxylase/agmatine deiminase pathway)
    (MetaCyc:ARGDEG-III-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e9769441139f7047c2d2c83338b03deffc61bc3ec7b84990e0487e4f5e8eaa92
    description: Raw SHA-256 file digest of data/pathways/l-arginine-degradation-iv.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-iv.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ARGDEGRAD-PWY
  path: data/pathways/l-arginine-degradation-v.yaml
  label: L-arginine degradation V (arginine deiminase pathway) (MetaCyc:ARGDEGRAD-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 869563ce5c7be07d5d4bd976ff53030082e518f913822b09f2c01033aee801df
    description: Raw SHA-256 file digest of data/pathways/l-arginine-degradation-v.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-v.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-301
  path: data/pathways/l-ascorbate-degradation-i.yaml
  label: L-ascorbate degradation I (bacterial, anaerobic) (MetaCyc:PWY0-301)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: fbd52a2c7fdf4cee6091b65b6dc744fc50f0c4e53c42992e750c013839850b26
    description: Raw SHA-256 file digest of data/pathways/l-ascorbate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-ascorbate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  path: data/pathways/l-asparagine-biosynthesis-i.yaml
  label: L-asparagine biosynthesis I (gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4c2ab031a5eec78aa751ddf4dc8753fc9523b1c18209abee6c237fd96d48628b
    description: Raw SHA-256 file digest of data/pathways/l-asparagine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-asparagine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  path: data/pathways/l-asparagine-degradation.yaml
  label: asparagine degradation (gomodel:YeastPathways_ASPARAGINE-DEG2-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 427034ee8a5311f807010c76d58368f822040bdec093c44c8638211b3a4cc1ef
    description: Raw SHA-256 file digest of data/pathways/l-asparagine-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-asparagine-degradation.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002051
  path: data/pathways/l-carnitine-degradation-i.yaml
  label: L-Carnitine Degradation I (PathBank:SMP0002051)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b007e4f9bf0d67c08c0c2262a46b6ddf4cbbc37d05ade639725f74bb008be767
    description: Raw SHA-256 file digest of data/pathways/l-carnitine-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-carnitine-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:CYSTSYN-PWY
  path: data/pathways/l-cysteine-biosynthesis-i.yaml
  label: L-cysteine biosynthesis I (MetaCyc:CYSTSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 54fe6a258f21f5866d4051ad8b756f347191a9fe3a154b3749c8393367157476
    description: Raw SHA-256 file digest of data/pathways/l-cysteine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-cysteine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  path: data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml
  label: L-cysteine biosynthesis III (from L-homocysteine) (gomodel:YeastPathways_HOMOCYSDEGR-PWY-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 367aed6701c731ec5d920226f082ab99b443debd7b353e84cf9b578eb1836459
    description: Raw SHA-256 file digest of data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:FUCCAT-PWY
  path: data/pathways/l-fucose-degradation-i.yaml
  label: L-fucose degradation I (MetaCyc:FUCCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a00b36d76e86e0102822cd1d280e686310aa0ff1603d0f4e53a8ed7286b3dc9a
    description: Raw SHA-256 file digest of data/pathways/l-fucose-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-fucose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:HISTSYN-PWY
  path: data/pathways/l-histidine-biosynthesis.yaml
  label: L-histidine biosynthesis (MetaCyc:HISTSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d4f67cf6d398a8ed42fcd7a83588f93c0f81ee22ddc94308d8027a9aa39e6c58
    description: Raw SHA-256 file digest of data/pathways/l-histidine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-histidine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5344
  path: data/pathways/l-homocysteine-biosynthesis.yaml
  label: L-homocysteine biosynthesis (gomodel:YeastPathways_PWY-5344)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ba66c588436c87397735f545b7e85accde4ae1e836f617b4041926e07f155f17
    description: Raw SHA-256 file digest of data/pathways/l-homocysteine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-homocysteine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:HOMOSERSYN-PWY
  path: data/pathways/l-homoserine-biosynthesis.yaml
  label: L-homoserine biosynthesis (MetaCyc:HOMOSERSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2ba55d5db3be34827890a544718c9759c4a606e464b0e46d3c263bf4dcff30d1
    description: Raw SHA-256 file digest of data/pathways/l-homoserine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-homoserine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:ILEUSYN-PWY
  path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
  label: L-isoleucine biosynthesis I (from threonine) (MetaCyc:ILEUSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6f478576730ca9224f355d5f04730464a7a7fa4e4dcca9a16c206b21669d8445
    description: Raw SHA-256 file digest of data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:LEUSYN-PWY
  path: data/pathways/l-leucine-biosynthesis.yaml
  label: L-leucine biosynthesis (MetaCyc:LEUSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7c11ab8c3970d6ac699b9a6d55bcfb8e31fa936fd8be9a8cffec49cb0f63bc1d
    description: Raw SHA-256 file digest of data/pathways/l-leucine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-leucine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:DAPLYSINESYN-PWY
  path: data/pathways/l-lysine-biosynthesis-i.yaml
  label: L-lysine biosynthesis I (MetaCyc:DAPLYSINESYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: f9e140eb9a5d886b826e5b77d03b44ad9bbad4b46dac54cdd676ad067e68705e
    description: Raw SHA-256 file digest of data/pathways/l-lysine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-lysine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  path: data/pathways/l-lysine-biosynthesis-iv.yaml
  label: L-lysine biosynthesis IV (gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1677f106fb798345712261c31d55df8175810494d8988bcf6ad6cf5f28debf28
    description: Raw SHA-256 file digest of data/pathways/l-lysine-biosynthesis-iv.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-lysine-biosynthesis-iv.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:LYXMET-PWY
  path: data/pathways/l-lyxose-degradation.yaml
  label: L-lyxose degradation (MetaCyc:LYXMET-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8ca651dc70a0dda2620ba09719a4e6861517d39f1736ca1971f283900accc121
    description: Raw SHA-256 file digest of data/pathways/l-lyxose-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-lyxose-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:HOMOSER-METSYN-PWY
  path: data/pathways/l-methionine-biosynthesis-i.yaml
  label: L-methionine biosynthesis I (MetaCyc:HOMOSER-METSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d3f600b8cf7da3ca2d5027327097c08e11bf562bbdceea90b1c5e9e7faaf2e89
    description: Raw SHA-256 file digest of data/pathways/l-methionine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-methionine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLUTORN-PWY
  path: data/pathways/l-ornithine-biosynthesis-i.yaml
  label: L-ornithine biosynthesis I (MetaCyc:GLUTORN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 922abf2efb71d2ba60e3913a9c0827bdcf419bd8800d900d66d4b8752e075d7f
    description: Raw SHA-256 file digest of data/pathways/l-ornithine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-ornithine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PHESYN
  path: data/pathways/l-phenylalanine-biosynthesis-i.yaml
  label: L-phenylalanine biosynthesis I (MetaCyc:PHESYN)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9b816a653a709e59bd9cd25b249d0e8e0ad58fcb90d072c981bd8c2748811d88
    description: Raw SHA-256 file digest of data/pathways/l-phenylalanine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-phenylalanine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PROSYN-PWY
  path: data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml
  label: L-proline biosynthesis I (from L-glutamate) (MetaCyc:PROSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e812af6b8f5879d39859ff0203088ddb6c298f1df13167d4e76f39f98f4da252
    description: Raw SHA-256 file digest of data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PROUT-PWY
  path: data/pathways/l-proline-degradation.yaml
  label: L-proline degradation (gomodel:YeastPathways_PROUT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 219603aea97d72075b8af5b9127026b3b397438b4fcaa4729e7a231f346c4160
    description: Raw SHA-256 file digest of data/pathways/l-proline-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-proline-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:RHAMCAT-PWY
  path: data/pathways/l-rhamnose-degradation-i.yaml
  label: L-rhamnose degradation I (MetaCyc:RHAMCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: f7afcfa11188882427f316b02209fcb4fe4544c1e45c0290259858a5c28ed970
    description: Raw SHA-256 file digest of data/pathways/l-rhamnose-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-rhamnose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:SERSYN-PWY
  path: data/pathways/l-serine-biosynthesis-i.yaml
  label: L-serine biosynthesis I (MetaCyc:SERSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b8fd90eb060911cf62737caa12f9b4899cc89119a2369aa3281bc700a64313a9
    description: Raw SHA-256 file digest of data/pathways/l-serine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-serine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:HOMOSER-THRESYN-PWY
  path: data/pathways/l-threonine-biosynthesis.yaml
  label: L-threonine biosynthesis (MetaCyc:HOMOSER-THRESYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e277951647e3da86c7ad92ac40a3e8d795c36f1550d67825898927540fe5dfa3
    description: Raw SHA-256 file digest of data/pathways/l-threonine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-threonine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:THRDLCTCAT-PWY
  path: data/pathways/l-threonine-degradation-iii.yaml
  label: L-threonine degradation III (to methylglyoxal) (MetaCyc:THRDLCTCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ce2bdf9706345cd51044e413276b8908f28508da333fa72faea8e65145e58a9c
    description: Raw SHA-256 file digest of data/pathways/l-threonine-degradation-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-threonine-degradation-iii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:TRPSYN-PWY
  path: data/pathways/l-tryptophan-biosynthesis.yaml
  label: L-tryptophan biosynthesis (MetaCyc:TRPSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 92206dbd7e6e9aba6fee6e9f866e3eb3fe019cd6b832a0ac6586cbcc65ce6dcc
    description: Raw SHA-256 file digest of data/pathways/l-tryptophan-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tryptophan-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5651
  path: data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml
  label: L-tryptophan degradation to 2-amino-3-carboxymuconate semialdehyde (gomodel:YeastPathways_PWY-5651)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7c69e4796385026c8d9f6fd0746183965cfa757a93b397e1fc6ae4cbfc40ab78
    description: Raw SHA-256 file digest of data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:TYRSYN
  path: data/pathways/l-tyrosine-biosynthesis-i.yaml
  label: L-tyrosine biosynthesis I (MetaCyc:TYRSYN)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e61553cc86414476cc4bc593114c2c0820b01246225450edffdef55910efe376
    description: Raw SHA-256 file digest of data/pathways/l-tyrosine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tyrosine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-4108
  path: data/pathways/l-tyrosine-degradation-iii.yaml
  label: L-tyrosine degradation III (gomodel:YeastPathways_PWY3O-4108)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e284eb14b32872c68b2914eebf0a511d6c6793803a2b7fb464dc5b65d6436f17
    description: Raw SHA-256 file digest of data/pathways/l-tyrosine-degradation-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tyrosine-degradation-iii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:VALSYN-PWY
  path: data/pathways/l-valine-biosynthesis.yaml
  label: L-valine biosynthesis (MetaCyc:VALSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9b58c4c2bdd0b065c6227492dda5c6bc998902739848ab4f2dc1f070e7bd9c19
    description: Raw SHA-256 file digest of data/pathways/l-valine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-valine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-4112
  path: data/pathways/leucine-degradation.yaml
  label: leucine degradation (gomodel:YeastPathways_PWY3O-4112)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 970f3bd13ea75cf742fc23a5410e4fe2e8f728e07e9d64049575e17480296b31
    description: Raw SHA-256 file digest of data/pathways/leucine-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/leucine-degradation.yaml
    role: maintained pathway YAML
- target_id: MIBiG:BGC0002072
  path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
  label: linearmycin A and related metabolites biosynthetic gene cluster (MIBiG:BGC0002072)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a5a908285f06357add5292777ea7be2226263c1448097361f9b3d87be0001cbe
    description: Raw SHA-256 file digest of data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
    role: maintained pathway YAML
- target_id: gomodel:6882d2b800000609
  path: data/pathways/lipid-iva-biosynthesis.yaml
  label: lipid IV(A) biosynthesis pathway (gomodel:6882d2b800000609)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5fdcc02a40f15844d1ba8a2ca67979afd58bd34781af21d8e2380a46df7faad5
    description: Raw SHA-256 file digest of data/pathways/lipid-iva-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/lipid-iva-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-501
  path: data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml
  label: lipoate biosynthesis and incorporation I (MetaCyc:PWY0-501)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 917b7a976e9fad4d84e43e5497105ac58670ccd419f09dc147aa8ebd93fc2e2e
    description: Raw SHA-256 file digest of data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-1743
  path: data/pathways/mannose-degradation.yaml
  label: mannose degradation (gomodel:YeastPathways_PWY3O-1743)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 28b58d00df8bc90ca2167213378d240f784502ee3d38cd044f0b9f708645d17a
    description: Raw SHA-256 file digest of data/pathways/mannose-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mannose-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1300
  path: data/pathways/mannosylglycerate-degradation.yaml
  label: 2-O-alpha-mannosyl-D-glycerate degradation (MetaCyc:PWY0-1300)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 39d1a3fa83a5d41ad8e9b2f8f26e22d881e6379a4beee76561e6fa34fa94da08
    description: Raw SHA-256 file digest of data/pathways/mannosylglycerate-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mannosylglycerate-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:METH-ACETATE-PWY
  path: data/pathways/methanogenesis-from-acetate.yaml
  label: methanogenesis from acetate (MetaCyc:METH-ACETATE-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 47d1c71951ce5806e5c9570ee00b2ab9f8634158251ee06821a0f77017b0eca3
    description: Raw SHA-256 file digest of data/pathways/methanogenesis-from-acetate.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methanogenesis-from-acetate.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:METHANOGENESIS-PWY
  path: data/pathways/methanogenesis-from-h2-and-co2.yaml
  label: methanogenesis from H2 and CO2 (MetaCyc:METHANOGENESIS-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 553922ede0ecdb12ebe569dbb9d8af1c70d4aa190e4fd60e69a9bc7ea0cf8e1e
    description: Raw SHA-256 file digest of data/pathways/methanogenesis-from-h2-and-co2.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methanogenesis-from-h2-and-co2.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-64
  path: data/pathways/methionine-salvage-pathway.yaml
  label: methionine salvage pathway (gomodel:YeastPathways_PWY3O-64)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7d9173433d90f1344b909cbd4d147923e5acf5acd18c2132df357c892c68f503
    description: Raw SHA-256 file digest of data/pathways/methionine-salvage-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methionine-salvage-pathway.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:NONMEVIPP-PWY
  path: data/pathways/methylerythritol-phosphate-pathway-i.yaml
  label: methylerythritol phosphate pathway I (MetaCyc:NONMEVIPP-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 868d6af5bb463ac41869ed65820b0e87fadb1de7ccb018fb26170ffe423b2fea
    description: Raw SHA-256 file digest of data/pathways/methylerythritol-phosphate-pathway-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylerythritol-phosphate-pathway-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-901
  path: data/pathways/methylglyoxal-catabolism.yaml
  label: methylglyoxal catabolism (gomodel:YeastPathways_PWY-901)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d1409031c98be3795d39fc4d2e5362d951cbd86c8b4c2868810a70c61582947a
    description: Raw SHA-256 file digest of data/pathways/methylglyoxal-catabolism.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylglyoxal-catabolism.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5386
  path: data/pathways/methylglyoxal-degradation-i.yaml
  label: methylglyoxal degradation I (MetaCyc:PWY-5386)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d714bf32e64b16682b2c451e90732644dcf4fae7453150a53f3d490316550f3f
    description: Raw SHA-256 file digest of data/pathways/methylglyoxal-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylglyoxal-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5453
  path: data/pathways/methylglyoxal-degradation-iii.yaml
  label: methylglyoxal degradation III (MetaCyc:PWY-5453)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 904a0f1aabfc7ba215fa1c933357715414a0f0cbed8ec130f84420b07812a688
    description: Raw SHA-256 file digest of data/pathways/methylglyoxal-degradation-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylglyoxal-degradation-iii.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002077
  path: data/pathways/methylphosphonate-degradation-i.yaml
  label: Methylphosphonate Degradation I (PathBank:SMP0002077)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 204b86bef2371a61586a7c9b4c0a33880e23c8999620fdeefb575900f5ddfdbe
    description: Raw SHA-256 file digest of data/pathways/methylphosphonate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylphosphonate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6048
  path: data/pathways/methylthiopropanoate-degradation-i.yaml
  label: methylthiopropanoate degradation I (cleavage) (MetaCyc:PWY-6048)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7810e21c690b17fe781fd249ea6fc0ec86220913a55947df75ec29c15cffe5dd
    description: Raw SHA-256 file digest of data/pathways/methylthiopropanoate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylthiopropanoate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_IPPSYN-PWY
  path: data/pathways/mevalonate-pathway.yaml
  label: mevalonate pathway (gomodel:YeastPathways_IPPSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1a3aaaf143564f9f1d345596cff4b961219716288a656791de7bf51bdba0307c
    description: Raw SHA-256 file digest of data/pathways/mevalonate-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mevalonate-pathway.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6823
  path: data/pathways/molybdenum-cofactor-biosynthesis.yaml
  label: molybdenum cofactor biosynthesis (MetaCyc:PWY-6823)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 84a67af129e307b0f67a8eb4aed8027a6b12733467e61c66249e1a8a9d751cc3
    description: Raw SHA-256 file digest of data/pathways/molybdenum-cofactor-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/molybdenum-cofactor-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-936721
  path: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
  label: Cysteine synthesis from O-acetylserine (Reactome:R-MTU-936721)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: cdbfd2cae9e281dc1a1722f65b2f019841b0a84b6e53e755bce049d495ed7f44
    description: Raw SHA-256 file digest of data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-936654
  path: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
  label: Cysteine synthesis from O-phosphoserine (Reactome:R-MTU-936654)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 99b0c6d3e04ab2d3c310bbe8099cd5fa716f251632e5320ba83444bd7ebff82d
    description: Raw SHA-256 file digest of data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-936635
  path: data/pathways/mycobacterium-sulfate-assimilation.yaml
  label: Sulfate assimilation (Reactome:R-MTU-936635)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: aecb344e6ec330b48884cafd9bab879f5e3c623f66e315d90ad93910da12f931
    description: Raw SHA-256 file digest of data/pathways/mycobacterium-sulfate-assimilation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-sulfate-assimilation.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-868688
  path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
  label: Mycobacterium tuberculosis trehalose biosynthesis (Reactome:R-MTU-868688)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7c3915665fbbe8cfe1d695354f471a1c832ccf972d2302c0910a96144ec1cd49
    description: Raw SHA-256 file digest of data/pathways/mycobacterium-trehalose-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-879299
  path: data/pathways/mycothiol-biosynthesis.yaml
  label: Mycothiol biosynthesis (Reactome:R-MTU-879299)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 35dfb77de4fcc447aeb649bb478c6a840e78ab39f5921469a154ec3768c32f4f
    description: Raw SHA-256 file digest of data/pathways/mycothiol-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycothiol-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: Reactome:R-MTU-879325
  path: data/pathways/mycothiol-catabolism.yaml
  label: mycothiol S-conjugate catabolism (Reactome:R-MTU-879325)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9d1f2496015cee969712712da363456ac0cac63dcd5cb46cfa5ace763f8388b1
    description: Raw SHA-256 file digest of data/pathways/mycothiol-catabolism.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/mycothiol-catabolism.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-2301
  path: data/pathways/myo-inositol-biosynthesis.yaml
  label: myo-inositol biosynthesis (gomodel:YeastPathways_PWY-2301)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 361f6547c51db754e8f9b68069e874d314ed2c7d0b2ee8c1716f6ac9fbcdff96
    description: Raw SHA-256 file digest of data/pathways/myo-inositol-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/myo-inositol-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-8383
  path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
  label: myxochelin A and B biosynthesis (MetaCyc:PWY-8383)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2
    description: Raw SHA-256 file digest of data/pathways/myxochelin-a-and-b-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:GLUAMCAT-PWY
  path: data/pathways/n-acetylglucosamine-degradation-i.yaml
  label: N-acetylglucosamine degradation I (MetaCyc:GLUAMCAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1ddbabfa3bad2292e49add564ee94283ff622c5dae55902f78aa5b4b1d6908b8
    description: Raw SHA-256 file digest of data/pathways/n-acetylglucosamine-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5653
  path: data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml
  label: NAD biosynthesis from 2-amino-3-carboxymuconate semialdehyde (gomodel:YeastPathways_PWY-5653)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bcd51a74589e80d1ff361bad234b690c487330acc238450bcd5e3215f25ea7cd
    description: Raw SHA-256 file digest of data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PYRIDNUCSYN-PWY
  path: data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml
  label: NAD de novo biosynthesis I (from aspartate) (MetaCyc:PYRIDNUCSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 36b0c2675cf844a236ee4e20a9f89874f137726026b1a713618cb6b4a51a280a
    description: Raw SHA-256 file digest of data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:NADPHOS-DEPHOS-PWY
  path: data/pathways/nad-phosphorylation-and-dephosphorylation.yaml
  label: NAD phosphorylation and dephosphorylation (MetaCyc:NADPHOS-DEPHOS-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2da6fc3e5d1c1e5ce4b4d0c8a9d1857b1f234c4c872cdf73d364f1c73ad87cb2
    description: Raw SHA-256 file digest of data/pathways/nad-phosphorylation-and-dephosphorylation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-phosphorylation-and-dephosphorylation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PYRIDNUCSAL-PWY
  path: data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml
  label: NAD salvage pathway I (PNC VI cycle) (MetaCyc:PYRIDNUCSAL-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: dc3a803eb1890953f16cf92fe012d9f780aa5e376ec30cfa2fc467cd80645885
    description: Raw SHA-256 file digest of data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-4106
  path: data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml
  label: NAD salvage pathway IV (from nicotinamide riboside) (gomodel:YeastPathways_PWY3O-4106)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 04f04356990ef06c793936970668528f4e4a3fadc52a32d161ab8c5175673101
    description: Raw SHA-256 file digest of data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP171
  path: data/pathways/nad-salvage-pathway-v.yaml
  label: NAD salvage pathway V (WikiPathways:WP171)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6f1e3a5883d8c6fba1aa10c90d089d3d8c19a54a6b7b9e1b1b0a4e24c2a0fdf8
    description: Raw SHA-256 file digest of data/pathways/nad-salvage-pathway-v.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-salvage-pathway-v.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6993
  path: data/pathways/nicotine-degradation-ii.yaml
  label: nicotine degradation II (pyrrolidine pathway) (MetaCyc:PWY-6993)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 462730b0c0b3679197226dc89dfbf04cac932cf004cea194a8fc3db89be82b0c
    description: Raw SHA-256 file digest of data/pathways/nicotine-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nicotine-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:DENITRIFICATION-PWY
  path: data/pathways/nitrate-reduction-i-denitrification.yaml
  label: nitrate reduction I (denitrification) (MetaCyc:DENITRIFICATION-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7c5b3ca9714dd9968901921b54bb82f44b08f85da322cb5527453ac685568ecd
    description: Raw SHA-256 file digest of data/pathways/nitrate-reduction-i-denitrification.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nitrate-reduction-i-denitrification.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1352
  path: data/pathways/nitrate-reduction-viii.yaml
  label: nitrate reduction VIII (dissimilatory) (MetaCyc:PWY0-1352)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5243f546a62490581e35d29516f2ecb830b1284748d6b2b042b82e7d9f6303b7
    description: Raw SHA-256 file digest of data/pathways/nitrate-reduction-viii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nitrate-reduction-viii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-5268
  path: data/pathways/oleate-biosynthesis.yaml
  label: oleate biosynthesis (gomodel:YeastPathways_PWY3O-5268)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 15992b5f8df117cec7bf73691cd2765cd60ea6db24aaa37b9b36861ee08909f7
    description: Raw SHA-256 file digest of data/pathways/oleate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/oleate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-1801
  path: data/pathways/palmitoleate-biosynthesis.yaml
  label: palmitoleate biosynthesis (gomodel:YeastPathways_PWY3O-1801)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b19047b3b055d4f065267230e639742d344b7aabe2edaa8a64bc0bfda88320b8
    description: Raw SHA-256 file digest of data/pathways/palmitoleate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/palmitoleate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:NONOXIPENT-PWY
  path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
  label: pentose phosphate pathway (non-oxidative branch) I (MetaCyc:NONOXIPENT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4fa7115243982e1fc30e5f492f66ab43225152be9e14cf114d5c67857af6032f
    description: Raw SHA-256 file digest of data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-8178
  path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
  label: pentose phosphate pathway (non-oxidative branch) II (MetaCyc:PWY-8178)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 20541f677f9228b670aac99a94e4d19ef89b5c20e0f6fdbb288d18ec7a9d98f5
    description: Raw SHA-256 file digest of data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:OXIDATIVEPENT-PWY
  path: data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
  label: pentose phosphate pathway (oxidative branch) I (MetaCyc:OXIDATIVEPENT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 37f5e7f93e971f867f00890b758411f59e84117ce1f9a76f310e64e82c5393e8
    description: Raw SHA-256 file digest of data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP5060
  path: data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
  label: Peptidoglycan cytoplasmic synthesis and recycling pathways (WikiPathways:WP5060)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 41137e969f7960cddb59b6452079b9424b87b0bfaa8402172969c230965cb36a
    description: Raw SHA-256 file digest of data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  path: data/pathways/periplasmic-nad-degradation.yaml
  label: periplasmic NAD degradation (gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b9186a25e2fe115e1f86d2d40024117d5424f5c1f1addd35d6d60fedd9c037bd
    description: Raw SHA-256 file digest of data/pathways/periplasmic-nad-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/periplasmic-nad-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6289
  path: data/pathways/petrobactin-biosynthesis.yaml
  label: petrobactin biosynthesis (MetaCyc:PWY-6289)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7d0737b9f0bb3a4673e7341e53c5763c80e4fb46fb2944db8c2199a6e66d645a
    description: Raw SHA-256 file digest of data/pathways/petrobactin-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/petrobactin-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-321
  path: data/pathways/phenylacetate-degradation-i-aerobic.yaml
  label: phenylacetate degradation I (aerobic) (MetaCyc:PWY0-321)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e99722d1ee920cf64aaeae7b00f1de9b59f939bd96a03a7ac5f2885933a72227
    description: Raw SHA-256 file digest of data/pathways/phenylacetate-degradation-i-aerobic.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phenylacetate-degradation-i-aerobic.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-4153
  path: data/pathways/phenylalanine-biosynthesis.yaml
  label: phenylalanine biosynthesis (gomodel:YeastPathways_PWY3O-4153)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b8903227908a29e6abaa9e8b9f9999b9f381aac31f8902702fa76591ae781f65
    description: Raw SHA-256 file digest of data/pathways/phenylalanine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phenylalanine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:2PHENDEG-PWY
  path: data/pathways/phenylethylamine-degradation-i.yaml
  label: phenylethylamine degradation I (MetaCyc:2PHENDEG-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3bdb2e4ae2eacefe5abf1611f89a58099f47b3264e58bc4195a55404833fe7f8
    description: Raw SHA-256 file digest of data/pathways/phenylethylamine-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phenylethylamine-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6534
  path: data/pathways/phenylethylamine-degradation-ii.yaml
  label: phenylethylamine degradation II (MetaCyc:PWY-6534)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8ea61243fca5d7d4a1974cf6b6eb8c9663a1c43a4f182709a7910eb56256d299
    description: Raw SHA-256 file digest of data/pathways/phenylethylamine-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phenylethylamine-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1277
  path: data/pathways/phenylpropanoate-and-hydroxyphenylpropanoate-degradation.yaml
  label: 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation (MetaCyc:PWY0-1277)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ff78d0911bb6ebe9e9780a8dce4fd11943228d67639ef44f63daf1cd7c362745
    description: Raw SHA-256 file digest of data/pathways/phenylpropanoate-and-hydroxyphenylpropanoate-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phenylpropanoate-and-hydroxyphenylpropanoate-degradation.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-6407
  path: data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml
  label: phosphatidate biosynthesis I (the dihydroxyacetone pathway) (gomodel:YeastPathways_PWY3O-6407)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: fc29837d25bb30779601d0cd011092833be57b2040370f5b656108c6351f3e5c
    description: Raw SHA-256 file digest of data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-6499
  path: data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml
  label: phosphatidate biosynthesis II (the glycerol-3-phosphate pathway) (gomodel:YeastPathways_PWY3O-6499)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3754f2cc7edc6996237b0bd5cdc96602bdb41c94abd1bd4ea010029d42ac51d7
    description: Raw SHA-256 file digest of data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-450
  path: data/pathways/phosphatidylcholine-biosynthesis-i.yaml
  label: phosphatidylcholine biosynthesis I (gomodel:YeastPathways_PWY3O-450)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 72b66339971241b0e2bf89a17bf5b9dc1297cdb82d01fc4857d0a5379ba03cb6
    description: Raw SHA-256 file digest of data/pathways/phosphatidylcholine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phosphatidylcholine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5669
  path: data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml
  label: phosphatidylethanolamine biosynthesis I (gomodel:YeastPathways_PWY-5669)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 48257f89bbe473bd0cb155f35cb5e8b5745d7cca8adb13f9f00c0d88018804f3
    description: Raw SHA-256 file digest of data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-242
  path: data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml
  label: phosphatidylinositol phosphate biosynthesis (gomodel:YeastPathways_PWY3O-242)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 3e02f66d204a5b899920d7d45cec37f2a83bbe57a321b1a394716a247f5ada26
    description: Raw SHA-256 file digest of data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-259
  path: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
  label: phospholipid biosynthesis II (Kennedy pathway) (gomodel:YeastPathways_PWY3O-259)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b9378fa6c051f50743bf57b8cf280cc44f702f4266470898a88aec0b3b222591
    description: Raw SHA-256 file digest of data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  path: data/pathways/phospholipid-biosynthesis.yaml
  label: phospholipid biosynthesis (gomodel:YeastPathways_PHOSLIPSYN2-PWY-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 417bf20d9ae6714e5055e015952829c2fd20f34c1f532dcc9116eb76983fa8e0
    description: Raw SHA-256 file digest of data/pathways/phospholipid-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phospholipid-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP71
  path: data/pathways/phospholipids-degradation.yaml
  label: Phospholipids degradation (WikiPathways:WP71)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1623a953f29c91d49e189b163e6d91a21803e9d9176e53fcd7b76b9cb874ec30
    description: Raw SHA-256 file digest of data/pathways/phospholipids-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phospholipids-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PANTO-PWY
  path: data/pathways/phosphopantothenate-biosynthesis-i.yaml
  label: phosphopantothenate biosynthesis I (MetaCyc:PANTO-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7d16b766666d040ee91d6e4c56415c69312440fa6f7a3db1482c3f807719c6f0
    description: Raw SHA-256 file digest of data/pathways/phosphopantothenate-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phosphopantothenate-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY1-3
  path: data/pathways/polyhydroxybutanoate-biosynthesis.yaml
  label: polyhydroxybutanoate biosynthesis (MetaCyc:PWY1-3)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 31480b5959f3b596fa758d0272b7b2400a9b23b33b52af7349f999ae6dad8d45
    description: Raw SHA-256 file digest of data/pathways/polyhydroxybutanoate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/polyhydroxybutanoate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PPGPPMET-PWY
  path: data/pathways/ppgpp-metabolism.yaml
  label: ppGpp metabolism (MetaCyc:PPGPPMET-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 81e8642cd792bbe351a43638303a7232e92679d2b47e8c308170bc6a0ad36a20
    description: Raw SHA-256 file digest of data/pathways/ppgpp-metabolism.yaml at
      frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ppgpp-metabolism.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:P184-PWY
  path: data/pathways/protocatechuate-meta-cleavage.yaml
  label: protocatechuate degradation I (meta-cleavage pathway) (MetaCyc:P184-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c36339efcbc6aeef084826b2b8a66fcbea46240aeed6c68c0275602fae21ea49
    description: Raw SHA-256 file digest of data/pathways/protocatechuate-meta-cleavage.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/protocatechuate-meta-cleavage.yaml
    role: maintained pathway YAML
- target_id: GO:0019618
  path: data/pathways/protocatechuate-ortho-cleavage.yaml
  label: protocatechuate catabolic process, ortho-cleavage (GO:0019618)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 03c1fced81d599136ea6577ef4ff314cc428aab9171c522f0334fa4ccba418d4
    description: Raw SHA-256 file digest of data/pathways/protocatechuate-ortho-cleavage.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/protocatechuate-ortho-cleavage.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6336
  path: data/pathways/protocatechuate-para-cleavage.yaml
  label: protocatechuate degradation III (para-cleavage pathway) (MetaCyc:PWY-6336)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2a5e42e39a4e8eadb77eabf6f95896ecc7f001bafba04dec6eb74e7251169d89
    description: Raw SHA-256 file digest of data/pathways/protocatechuate-para-cleavage.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/protocatechuate-para-cleavage.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6019
  path: data/pathways/pseudouridine-degradation.yaml
  label: pseudouridine degradation (MetaCyc:PWY-6019)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a11010f36c6af2d7f3304357cb920ba75fda74b067f01e0a64e9855123452159
    description: Raw SHA-256 file digest of data/pathways/pseudouridine-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pseudouridine-degradation.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002089
  path: data/pathways/purine-deoxyribonucleosides-degradation.yaml
  label: Purine Deoxyribonucleosides Degradation (PathBank:SMP0002089)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1412ec0cdb11458da71fd9b50a8c0827effefe28fe9ac949213db928d1e26087
    description: Raw SHA-256 file digest of data/pathways/purine-deoxyribonucleosides-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/purine-deoxyribonucleosides-degradation.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002067
  path: data/pathways/putrescine-degradation-ii.yaml
  label: Putrescine Degradation II (PathBank:SMP0002067)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 92dd03c0886b7b6a30ad87219f380e80c9e10ef087f3b10dacccdb69f3ab2b3f
    description: Raw SHA-256 file digest of data/pathways/putrescine-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/putrescine-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: GO:0042864
  path: data/pathways/pyochelin-biosynthesis.yaml
  label: pyochelin biosynthetic process (GO:0042864)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b3dfb5d0879dacd052e151477d6a48e422941752ea9b98ebd613064d5e3cde1b
    description: Raw SHA-256 file digest of data/pathways/pyochelin-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyochelin-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PYRIDOXSYN-PWY
  path: data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
  label: pyridoxal 5'-phosphate biosynthesis I (MetaCyc:PYRIDOXSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 03219ffa92913bcc306f4824c2c72aa39f862b17d14c96a0a9dd6daa9834bc42
    description: Raw SHA-256 file digest of data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PLPSAL-PWY
  path: data/pathways/pyridoxal-5-phosphate-salvage-i.yaml
  label: pyridoxal 5'-phosphate salvage I (MetaCyc:PLPSAL-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4fa125485b95ff8518056a42c7f22764cac006f812e66effbf250261ee7e4c29
    description: Raw SHA-256 file digest of data/pathways/pyridoxal-5-phosphate-salvage-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyridoxal-5-phosphate-salvage-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-7181
  path: data/pathways/pyrimidine-deoxyribonucleosides-degradation.yaml
  label: pyrimidine deoxyribonucleosides degradation (MetaCyc:PWY-7181)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 58ba6e176122f244f2bf59c155605347765e151e668699199d4ec3b474b273e6
    description: Raw SHA-256 file digest of data/pathways/pyrimidine-deoxyribonucleosides-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyrimidine-deoxyribonucleosides-degradation.yaml
    role: maintained pathway YAML
- target_id: GO:0010139
  path: data/pathways/pyrimidine-deoxyribonucleotide-salvage.yaml
  label: pyrimidine deoxyribonucleotide salvage (GO:0010139)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7e4d179cc40816a549edde196f4270960c09cfcb6dbc15882b85427e85013498
    description: Raw SHA-256 file digest of data/pathways/pyrimidine-deoxyribonucleotide-salvage.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyrimidine-deoxyribonucleotide-salvage.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002038
  path: data/pathways/pyrimidine-ribonucleosides-degradation.yaml
  label: Pyrimidine Ribonucleosides Degradation (PathBank:SMP0002038)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: e1f562227ad8aaf01f1a762e93c27030e4cae8779869670a416bfec79562c6d9
    description: Raw SHA-256 file digest of data/pathways/pyrimidine-ribonucleosides-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyrimidine-ribonucleosides-degradation.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PYRUVDEHYD-PWY
  path: data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml
  label: pyruvate decarboxylation to acetyl CoA (gomodel:YeastPathways_PYRUVDEHYD-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 78370a3d929d7580ff372192b4362e2a48c430e20e79066262a2aa5371b11baa
    description: Raw SHA-256 file digest of data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-440
  path: data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml
  label: pyruvate fermentation to acetoin III (gomodel:YeastPathways_PWY3O-440)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6a91a3bcbe9679c27ae30c57357772f3ccd7fe98ec9ead2b6097c89e34f6a6a7
    description: Raw SHA-256 file digest of data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-7545
  path: data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml
  label: pyruvate to cytochrome bd oxidase electron transfer (MetaCyc:PWY-7545)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1f4ea5bcf744449a6ad04d0da03b69c2e87e33dbfadc6db16a4de84d69407e31
    description: Raw SHA-256 file digest of data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:QUINATEDEG-PWY
  path: data/pathways/quinate-degradation-i.yaml
  label: quinate degradation I (MetaCyc:QUINATEDEG-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a0c21af8e01b7a2653b226656b405fc197b0376b2d9ea4a6dbb6d003a3cc36cb
    description: Raw SHA-256 file digest of data/pathways/quinate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6416
  path: data/pathways/quinate-degradation-ii.yaml
  label: quinate degradation II (MetaCyc:PWY-6416)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 83445c4f5cedd104d29cd065771b384f0ea277ed74291e3569315a9d42b01d97
    description: Raw SHA-256 file digest of data/pathways/quinate-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002406
  path: data/pathways/riboneogenesis.yaml
  label: Riboneogenesis (PathBank:SMP0002406)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d2fa67f221476a346e85dd794a9f55351aa35115150efc767457359f40433b96
    description: Raw SHA-256 file digest of data/pathways/riboneogenesis.yaml at frozen
      Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/riboneogenesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:RIBOKIN-PWY
  path: data/pathways/ribose-phosphorylation.yaml
  label: ribose phosphorylation (MetaCyc:RIBOKIN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 385101d166c9150936d81bb0f1c6c0d134b6ac1e6a6454d86e238ac0576e3d71
    description: Raw SHA-256 file digest of data/pathways/ribose-phosphorylation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ribose-phosphorylation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6151
  path: data/pathways/s-adenosyl-l-methionine-cycle-i.yaml
  label: S-adenosyl-L-methionine cycle I (MetaCyc:PWY-6151)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: f400f02c796aeca00d11aa29f8783f7f672bd7f87d7d07f827bfbca36eac3e22
    description: Raw SHA-256 file digest of data/pathways/s-adenosyl-l-methionine-cycle-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/s-adenosyl-l-methionine-cycle-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5041
  path: data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml
  label: S-adenosyl-L-methionine cycle II (gomodel:YeastPathways_PWY-5041)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4907cf3e7dc0469ef74274da8f536c99a4bfced9a177938d793c448e1db7724c
    description: Raw SHA-256 file digest of data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-8132
  path: data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
  label: S-methyl-5-thio-α-D-ribose 1-phosphate degradation III (MetaCyc:PWY-8132)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 60750cb046b847a5d52458cff6eab771be2a9200755c259cfe8d87c4808e95fa
    description: Raw SHA-256 file digest of data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_YEAST-RNT-SALV
  path: data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml
  label: salvage pathways of pyrimidine ribonucleotides (gomodel:YeastPathways_YEAST-RNT-SALV)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c703f90bedcee65918e9dda8a322c76984eac65759b018811030c42557ba81ce
    description: Raw SHA-256 file digest of data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1517
  path: data/pathways/sedoheptulose-bisphosphate-bypass.yaml
  label: sedoheptulose bisphosphate bypass (MetaCyc:PWY0-1517)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6ed1607a4c17ffe56a6f5f8f123c44a0ff410c9a9965e11c3cde9ef23a4affe2
    description: Raw SHA-256 file digest of data/pathways/sedoheptulose-bisphosphate-bypass.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/sedoheptulose-bisphosphate-bypass.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:SHIKIMATEDEG-PWY
  path: data/pathways/shikimate-degradation-i.yaml
  label: shikimate degradation I (MetaCyc:SHIKIMATEDEG-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808
    description: Raw SHA-256 file digest of data/pathways/shikimate-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/shikimate-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-6419
  path: data/pathways/shikimate-degradation-ii.yaml
  label: shikimate degradation II (MetaCyc:PWY-6419)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a0f96cded480818165c794e5e954e96b2fa7f11e46910ad6574b6233480d13c1
    description: Raw SHA-256 file digest of data/pathways/shikimate-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/shikimate-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5194-1
  path: data/pathways/siroheme-biosynthesis.yaml
  label: siroheme biosynthesis (gomodel:YeastPathways_PWY-5194-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 266f51a79c6f909fb6179937bf4c367f1f1d1c3a6fa1d314bec790466955548e
    description: Raw SHA-256 file digest of data/pathways/siroheme-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/siroheme-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0002097
  path: data/pathways/spermidine-biosynthesis-and-metabolism-escherichia-coli.yaml
  label: Spermidine Biosynthesis and Metabolism (PathBank:SMP0002097)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0adef1da2d818af7c62d7e3952b2115585b47b8f132ec189cde2b435d2721680
    description: Raw SHA-256 file digest of data/pathways/spermidine-biosynthesis-and-metabolism-escherichia-coli.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/spermidine-biosynthesis-and-metabolism-escherichia-coli.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  path: data/pathways/spermidine-biosynthesis-i.yaml
  label: spermidine biosynthesis I (gomodel:YeastPathways_BSUBPOLYAMSYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 6d94af196efc361a35dc72c2f8ef30fdf7def3a9e2597bd8bba8a2daaf235260
    description: Raw SHA-256 file digest of data/pathways/spermidine-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/spermidine-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_ARGSPECAT-PWY
  path: data/pathways/spermine-biosynthesis.yaml
  label: spermine biosynthesis (gomodel:YeastPathways_ARGSPECAT-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: da1f3ef31eb3d56e724b06474a42acb883f1947d17dd46415e36e0e99b5d3f56
    description: Raw SHA-256 file digest of data/pathways/spermine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/spermine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  path: data/pathways/sphingolipid-biosynthesis-yeast.yaml
  label: sphingolipid biosynthesis (yeast) (gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d7c01da786b8f7261fbf51f1b83cd3125d5dd9a3dbbd4945e8a195c1e8cab6b7
    description: Raw SHA-256 file digest of data/pathways/sphingolipid-biosynthesis-yeast.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/sphingolipid-biosynthesis-yeast.yaml
    role: maintained pathway YAML
- target_id: MIBiG:BGC0000852
  path: data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml
  label: Sporosarcina pasteurii ectoine biosynthetic gene cluster (MIBiG:BGC0000852)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0c2e4ef99740885129888a71cf927b1ac8af45e7061c3e3b55ac0913d68dc224
    description: Raw SHA-256 file digest of data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-7990
  path: data/pathways/staphyloferrin-a-biosynthesis.yaml
  label: staphyloferrin A biosynthesis (MetaCyc:PWY-7990)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5b4cd8d7838a19de2ba9c623bd59d321def6fffca45553895df646852d780e42
    description: Raw SHA-256 file digest of data/pathways/staphyloferrin-a-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/staphyloferrin-a-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-8008
  path: data/pathways/staphyloferrin-b-biosynthesis.yaml
  label: staphyloferrin B biosynthesis (MetaCyc:PWY-8008)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 742930db9f8be218e6d69bf81c8b5d5ab3f460ed36d22d1660a4f18be6db26c1
    description: Raw SHA-256 file digest of data/pathways/staphyloferrin-b-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/staphyloferrin-b-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-43
  path: data/pathways/succinate-to-propanoate.yaml
  label: conversion of succinate to propanoate (MetaCyc:PWY0-43)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268
    description: Raw SHA-256 file digest of data/pathways/succinate-to-propanoate.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/succinate-to-propanoate.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5340
  path: data/pathways/sulfate-activation-for-sulfonation.yaml
  label: sulfate activation (for sulfonation) (gomodel:YeastPathways_PWY-5340)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: bcfb1267bed7de24a78f54d271e10b5ad9251648adcdd73c6882c5fb203cf904
    description: Raw SHA-256 file digest of data/pathways/sulfate-activation-for-sulfonation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/sulfate-activation-for-sulfonation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-7446
  path: data/pathways/sulfoquinovose-degradation-i.yaml
  label: sulfoquinovose degradation I (MetaCyc:PWY-7446)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 741fc68daedf7cb7000b7cc5dc94ce5c0029fe9d30ce56d392c51a2aa9ac390c
    description: Raw SHA-256 file digest of data/pathways/sulfoquinovose-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/sulfoquinovose-degradation-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-7722
  path: data/pathways/sulfoquinovose-degradation-ii.yaml
  label: sulfoquinovose degradation II (MetaCyc:PWY-7722)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 20a95c209243399b88a90fbecb0d8d310ebfb3094fc6ee4487352fdc2185c596
    description: Raw SHA-256 file digest of data/pathways/sulfoquinovose-degradation-ii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/sulfoquinovose-degradation-ii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_DETOX1-PWY
  path: data/pathways/superoxide-radicals-degradation.yaml
  label: superoxide radicals degradation (gomodel:YeastPathways_DETOX1-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: f55995b9eac815491d9b7f5a57daa252e6111c9680612188fb1ff09a7a8698b9
    description: Raw SHA-256 file digest of data/pathways/superoxide-radicals-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/superoxide-radicals-degradation.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5838
  path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
  label: superpathway of menaquinol-8 biosynthesis I (MetaCyc:PWY-5838)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8d24e6ff858759aa4eaecd04b456ffa1b79c992bc090637f5cc8805a5ecbf492
    description: Raw SHA-256 file digest of data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP296
  path: data/pathways/tca-cycle-detailed.yaml
  label: TCA cycle - detailed (WikiPathways:WP296)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c574f799eef6b8b793decf52b1934a9f65ddac42893bb56ed5ed9d4134f837fe
    description: Raw SHA-256 file digest of data/pathways/tca-cycle-detailed.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/tca-cycle-detailed.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-6614
  path: data/pathways/tetrahydrofolate-biosynthesis.yaml
  label: tetrahydrofolate biosynthesis (gomodel:YeastPathways_PWY-6614)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 926aeb5bbfafd09fa1e6d0599456545cfa89186f2f8bc88e5f6bb3a55d7b0d19
    description: Raw SHA-256 file digest of data/pathways/tetrahydrofolate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/tetrahydrofolate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1433
  path: data/pathways/tetrahydromonapterin-biosynthesis.yaml
  label: tetrahydromonapterin biosynthesis (MetaCyc:PWY0-1433)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0349c62d93993252bdab4e11a477eaca142eb516c59961721a317ed333eda182
    description: Raw SHA-256 file digest of data/pathways/tetrahydromonapterin-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/tetrahydromonapterin-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-50
  path: data/pathways/tetrapyrrole-biosynthesis.yaml
  label: tetrapyrrole biosynthesis (gomodel:YeastPathways_PWY3O-50)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 75ebed65fc0c1f3a60cb1941f878481a38a5ad719cc4f2512930fd96cd1a7df7
    description: Raw SHA-256 file digest of data/pathways/tetrapyrrole-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/tetrapyrrole-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-17
  path: data/pathways/thiamine-biosynthesis.yaml
  label: thiamine biosynthesis (gomodel:YeastPathways_PWY3O-17)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d8fbce15fc5a176811eef4f906bc148ef949814b3fd31c9fec756cdf08f3f0b4
    description: Raw SHA-256 file digest of data/pathways/thiamine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/thiamine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:THISYN-PWY
  path: data/pathways/thiamine-diphosphate-biosynthesis-i.yaml
  label: superpathway of thiamine diphosphate biosynthesis I (MetaCyc:THISYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 05fe1413e04fa3c2b95e44af1bda6c795ef53d3ea3529d18f6c42bac2e8079ea
    description: Raw SHA-256 file digest of data/pathways/thiamine-diphosphate-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/thiamine-diphosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:THIOREDOX-PWY
  path: data/pathways/thioredoxin-pathway.yaml
  label: thioredoxin pathway (MetaCyc:THIOREDOX-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 8fa7373fe66807d9c12083c5fbe5e410ab5eaadf1100179590e488f74b8bafe0
    description: Raw SHA-256 file digest of data/pathways/thioredoxin-pathway.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/thioredoxin-pathway.yaml
    role: maintained pathway YAML
- target_id: PathBank:SMP0000992
  path: data/pathways/threonine-biosynthesis-from-aspartate-escherichia-coli.yaml
  label: 'Secondary Metabolites: Threonine Biosynthesis from Aspartate (PathBank:SMP0000992)'
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 057078439b415869dfc977fafe4ae09029c11dd4c352fa25caaff70552a9d339
    description: Raw SHA-256 file digest of data/pathways/threonine-biosynthesis-from-aspartate-escherichia-coli.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/threonine-biosynthesis-from-aspartate-escherichia-coli.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_THREOCAT2-PWY
  path: data/pathways/threonine-degradation.yaml
  label: threonine degradation (gomodel:YeastPathways_THREOCAT2-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 267955a3bc387e34570713b9e42cb97528811728e89697c133654db94742d3c0
    description: Raw SHA-256 file digest of data/pathways/threonine-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/threonine-degradation.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5123
  path: data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml
  label: trans, trans-farnesyl diphosphate biosynthesis (gomodel:YeastPathways_PWY-5123)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2c9a01d5a4cbf5dd9b5a4d165cbe64e705ea2d7570f385f0b8dbf242a980be77
    description: Raw SHA-256 file digest of data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:TRESYN-PWY
  path: data/pathways/trehalose-biosynthesis-i.yaml
  label: trehalose biosynthesis I (MetaCyc:TRESYN-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2345d073b0ee434ab1a897653441d1bcd431ba0314e2265b9699fc6fd5a8eefb
    description: Raw SHA-256 file digest of data/pathways/trehalose-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/trehalose-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP266
  path: data/pathways/triglyceride-biosynthesis.yaml
  label: Triglyceride biosynthesis (WikiPathways:WP266)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: a6cf5919fcfd1d23095258909f13c819a81dbaf8fdae4d8f5aebb862428ac07a
    description: Raw SHA-256 file digest of data/pathways/triglyceride-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/triglyceride-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-214
  path: data/pathways/tryptophan-degradation.yaml
  label: tryptophan degradation (gomodel:YeastPathways_PWY3O-214)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: caeb051e798194e96fac5ae22959fd91b6c3314fe69d6c0175721e6c6250bb01
    description: Raw SHA-256 file digest of data/pathways/tryptophan-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/tryptophan-degradation.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-4120
  path: data/pathways/tyrosine-biosynthesis.yaml
  label: tyrosine biosynthesis (gomodel:YeastPathways_PWY3O-4120)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 97f352fdb43fa188391dc1a79702296c03c34fbdd8564cce53610528ca9793b0
    description: Raw SHA-256 file digest of data/pathways/tyrosine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/tyrosine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: WikiPathways:WP287
  path: data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml
  label: Ubiquinol-6 biosynthesis from 4-hydroxybenzoate (WikiPathways:WP287)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2546ba7c2b4a4b8d1ec2ff21d48672a1d164a7caf987b71aa67763c67a013efd
    description: Raw SHA-256 file digest of data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  path: data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml
  label: UDP-N-acetylglucosamine biosynthesis (gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4e8b67155682a12a450182016df2250fb9ab3ea340f059b8a620998c38407cb5
    description: Raw SHA-256 file digest of data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY-5686
  path: data/pathways/ump-biosynthesis-i.yaml
  label: UMP biosynthesis I (MetaCyc:PWY-5686)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7360c32e29f0aa492c9b6e3c73b28ec1d1c152258e7efcfd540beb1394546f16
    description: Raw SHA-256 file digest of data/pathways/ump-biosynthesis-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ump-biosynthesis-i.yaml
    role: maintained pathway YAML
- target_id: MetaCyc:PWY0-1471
  path: data/pathways/uracil-degradation-iii.yaml
  label: uracil degradation III (MetaCyc:PWY0-1471)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 2c155041e378508c99a430e72bd5fad82bde8bfc3c2b7b72569589a24c14f1c6
    description: Raw SHA-256 file digest of data/pathways/uracil-degradation-iii.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/uracil-degradation-iii.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5703
  path: data/pathways/urea-degradation-i.yaml
  label: urea degradation I (gomodel:YeastPathways_PWY-5703)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 0c163d8fa329237abc323929210505f9f1051d0dcd5ae7756cdde96924236ab9
    description: Raw SHA-256 file digest of data/pathways/urea-degradation-i.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/urea-degradation-i.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-7176
  path: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
  label: UTP and CTP de novo biosynthesis (gomodel:YeastPathways_PWY-7176)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9a13a458e243bec38a792d1b4f85346a6fd4ef9d53e531b3aaf02cc0b13ef831
    description: Raw SHA-256 file digest of data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-4105
  path: data/pathways/valine-degradation.yaml
  label: valine degradation (gomodel:YeastPathways_PWY3O-4105)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5e0861fa7734fb946a476027e53a705ba475ea2052aa220e9cf5068b1e041202
    description: Raw SHA-256 file digest of data/pathways/valine-degradation.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/valine-degradation.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-5080-1
  path: data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml
  label: very long chain fatty acid biosynthesis I (gomodel:YeastPathways_PWY-5080-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 21b1b8c472788467007f47443a2d57bd00f47386f2f5222b5a8236a3e4e2681a
    description: Raw SHA-256 file digest of data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY3O-8
  path: data/pathways/xylose-metabolism.yaml
  label: xylose metabolism (gomodel:YeastPathways_PWY3O-8)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9d940d5a968e3b77aa250ff035c84eeb897f51a7f125e8b42bc9993840da7fc9
    description: Raw SHA-256 file digest of data/pathways/xylose-metabolism.yaml at
      frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/xylose-metabolism.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_PWY-6074-1
  path: data/pathways/zymosterol-biosynthesis.yaml
  label: zymosterol biosynthesis (gomodel:YeastPathways_PWY-6074-1)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: b5f06648c0c03826ebe45a208140962b1d164edae1fa129ed3a1d70b9691408b
    description: Raw SHA-256 file digest of data/pathways/zymosterol-biosynthesis.yaml
      at frozen Git commit e369fa425e64d4f794ce84e2fd71138a43660467.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/zymosterol-biosynthesis.yaml
    role: maintained pathway YAML
checks:
- check_id: validate
  name: Repository QC and closed-schema validation (just validate)
  status: passed
  required: true
  summary: Validated all 271 maintained pathway records against the closed LinkML
    schema, local identifier/label authority snapshots, 654 history records, 22,211
    evidence blocks, 33 source records, and pages/ synchrony.
  target_ids:
  - MetaCyc:PWY-5901
  - MetaCyc:PWY0-42
  - WikiPathways:WP5587
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-6543
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - gomodel:YeastPathways_PWY-6147
  - GO:0097288
  - MetaCyc:PWY0-1312
  - MetaCyc:ACETOACETATE-DEG-PWY
  - WikiPathways:WP5019
  - PathBank:SMP0002081
  - MetaCyc:P121-PWY
  - PathBank:SMP0002083
  - MetaCyc:PWY-6609
  - gomodel:YeastPathways_PWY-7220-1
  - MetaCyc:SALVADEHYPOX-PWY
  - gomodel:YeastPathways_PWY-7219
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-1241
  - GO:0019270
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - MetaCyc:PWY0-41
  - gomodel:YeastPathways_PWY-5694
  - MetaCyc:PWY-5705
  - gomodel:YeastPathways_PWY-5697
  - MetaCyc:GLCMANNANAUT-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - MetaCyc:PWY-5903
  - PathBank:SMP0002123
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:P321-PWY
  - gomodel:YeastPathways_PWY-5760-1
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - GO:0043427
  - gomodel:YeastPathways_PWY3O-4
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5417
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - gomodel:YeastPathways_PWY3O-15
  - MetaCyc:ARO-PWY
  - MIBiG:BGC0000829
  - MetaCyc:P2-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - MetaCyc:COA-PWY
  - GO:0036040
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:PWY-6376
  - KEGG:M00374
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-123
  - GO:0019305
  - MetaCyc:P101-PWY
  - KEGG:M00008
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-6075-1
  - MetaCyc:PWY-7255
  - gomodel:YeastPathways_PWY3O-4300
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1280
  - KEGG:M00373
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - MetaCyc:RIBOSYN2-PWY
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY-1801-1
  - MetaCyc:PWY0-521
  - GO:1901281
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:PWY-6223
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - WikiPathways:WP556
  - MetaCyc:PWY-5177
  - MetaCyc:GLUTATHIONESYN-PWY
  - gomodel:YeastPathways_PWYQT-4432
  - WikiPathways:WP392
  - gomodel:YeastPathways_PWY3O-48
  - MetaCyc:GLYCEROLMETAB-PWY
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - WikiPathways:WP478
  - gomodel:YeastPathways_GLYCOLYSIS
  - MetaCyc:PWY-5744
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - GO:1902000
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - gomodel:YeastPathways_PWY3O-402
  - WikiPathways:WP178
  - MetaCyc:PWY0-1338
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:PWY0-301
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - PathBank:SMP0002051
  - MetaCyc:CYSTSYN-PWY
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - gomodel:YeastPathways_PWY-5344
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - MetaCyc:LYXMET-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - gomodel:YeastPathways_PROUT-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - gomodel:YeastPathways_PWY-5651
  - MetaCyc:TYRSYN
  - gomodel:YeastPathways_PWY3O-4108
  - MetaCyc:VALSYN-PWY
  - gomodel:YeastPathways_PWY3O-4112
  - MIBiG:BGC0002072
  - gomodel:6882d2b800000609
  - MetaCyc:PWY0-501
  - gomodel:YeastPathways_PWY3O-1743
  - MetaCyc:PWY0-1300
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - gomodel:YeastPathways_PWY3O-64
  - MetaCyc:NONMEVIPP-PWY
  - gomodel:YeastPathways_PWY-901
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5453
  - PathBank:SMP0002077
  - MetaCyc:PWY-6048
  - gomodel:YeastPathways_IPPSYN-PWY
  - MetaCyc:PWY-6823
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - gomodel:YeastPathways_PWY-2301
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - gomodel:YeastPathways_PWY-5653
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - gomodel:YeastPathways_PWY3O-4106
  - WikiPathways:WP171
  - MetaCyc:PWY-6993
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:PWY0-1352
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-1801
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:PWY-8178
  - MetaCyc:OXIDATIVEPENT-PWY
  - WikiPathways:WP5060
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - MetaCyc:PWY-6289
  - MetaCyc:PWY0-321
  - gomodel:YeastPathways_PWY3O-4153
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:PWY-6534
  - MetaCyc:PWY0-1277
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - WikiPathways:WP71
  - MetaCyc:PANTO-PWY
  - MetaCyc:PWY1-3
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:P184-PWY
  - GO:0019618
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6019
  - PathBank:SMP0002089
  - PathBank:SMP0002067
  - GO:0042864
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-7181
  - GO:0010139
  - PathBank:SMP0002038
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_PWY3O-440
  - MetaCyc:PWY-7545
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:PWY-6416
  - PathBank:SMP0002406
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:PWY-6151
  - gomodel:YeastPathways_PWY-5041
  - MetaCyc:PWY-8132
  - gomodel:YeastPathways_YEAST-RNT-SALV
  - MetaCyc:PWY0-1517
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:PWY-6419
  - gomodel:YeastPathways_PWY-5194-1
  - PathBank:SMP0002097
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - MIBiG:BGC0000852
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY0-43
  - gomodel:YeastPathways_PWY-5340
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7722
  - gomodel:YeastPathways_DETOX1-PWY
  - MetaCyc:PWY-5838
  - WikiPathways:WP296
  - gomodel:YeastPathways_PWY-6614
  - MetaCyc:PWY0-1433
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-17
  - MetaCyc:THISYN-PWY
  - MetaCyc:THIOREDOX-PWY
  - PathBank:SMP0000992
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_PWY-5123
  - MetaCyc:TRESYN-PWY
  - WikiPathways:WP266
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-4120
  - WikiPathways:WP287
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - MetaCyc:PWY-5686
  - MetaCyc:PWY0-1471
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWY-6074-1
  command: .venv/bin/pathwaymech-run-qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C2-QC-VALIDATE
  scope_note: Corpus-wide validation gate covering all 271 maintained records.
- check_id: test
  name: Full pytest test suite (just test)
  status: passed
  required: true
  summary: All 8,066 unit, schema, KGX, SSSOM, and record-review contract tests passed
    (3 skipped).
  target_ids:
  - MetaCyc:PWY-5901
  - MetaCyc:PWY0-42
  - WikiPathways:WP5587
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-6543
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - gomodel:YeastPathways_PWY-6147
  - GO:0097288
  - MetaCyc:PWY0-1312
  - MetaCyc:ACETOACETATE-DEG-PWY
  - WikiPathways:WP5019
  - PathBank:SMP0002081
  - MetaCyc:P121-PWY
  - PathBank:SMP0002083
  - MetaCyc:PWY-6609
  - gomodel:YeastPathways_PWY-7220-1
  - MetaCyc:SALVADEHYPOX-PWY
  - gomodel:YeastPathways_PWY-7219
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-1241
  - GO:0019270
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - MetaCyc:PWY0-41
  - gomodel:YeastPathways_PWY-5694
  - MetaCyc:PWY-5705
  - gomodel:YeastPathways_PWY-5697
  - MetaCyc:GLCMANNANAUT-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - MetaCyc:PWY-5903
  - PathBank:SMP0002123
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:P321-PWY
  - gomodel:YeastPathways_PWY-5760-1
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - GO:0043427
  - gomodel:YeastPathways_PWY3O-4
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5417
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - gomodel:YeastPathways_PWY3O-15
  - MetaCyc:ARO-PWY
  - MIBiG:BGC0000829
  - MetaCyc:P2-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - MetaCyc:COA-PWY
  - GO:0036040
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:PWY-6376
  - KEGG:M00374
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-123
  - GO:0019305
  - MetaCyc:P101-PWY
  - KEGG:M00008
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-6075-1
  - MetaCyc:PWY-7255
  - gomodel:YeastPathways_PWY3O-4300
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1280
  - KEGG:M00373
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - MetaCyc:RIBOSYN2-PWY
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY-1801-1
  - MetaCyc:PWY0-521
  - GO:1901281
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:PWY-6223
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - WikiPathways:WP556
  - MetaCyc:PWY-5177
  - MetaCyc:GLUTATHIONESYN-PWY
  - gomodel:YeastPathways_PWYQT-4432
  - WikiPathways:WP392
  - gomodel:YeastPathways_PWY3O-48
  - MetaCyc:GLYCEROLMETAB-PWY
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - WikiPathways:WP478
  - gomodel:YeastPathways_GLYCOLYSIS
  - MetaCyc:PWY-5744
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - GO:1902000
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - gomodel:YeastPathways_PWY3O-402
  - WikiPathways:WP178
  - MetaCyc:PWY0-1338
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:PWY0-301
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - PathBank:SMP0002051
  - MetaCyc:CYSTSYN-PWY
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - gomodel:YeastPathways_PWY-5344
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - MetaCyc:LYXMET-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - gomodel:YeastPathways_PROUT-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - gomodel:YeastPathways_PWY-5651
  - MetaCyc:TYRSYN
  - gomodel:YeastPathways_PWY3O-4108
  - MetaCyc:VALSYN-PWY
  - gomodel:YeastPathways_PWY3O-4112
  - MIBiG:BGC0002072
  - gomodel:6882d2b800000609
  - MetaCyc:PWY0-501
  - gomodel:YeastPathways_PWY3O-1743
  - MetaCyc:PWY0-1300
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - gomodel:YeastPathways_PWY3O-64
  - MetaCyc:NONMEVIPP-PWY
  - gomodel:YeastPathways_PWY-901
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5453
  - PathBank:SMP0002077
  - MetaCyc:PWY-6048
  - gomodel:YeastPathways_IPPSYN-PWY
  - MetaCyc:PWY-6823
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - gomodel:YeastPathways_PWY-2301
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - gomodel:YeastPathways_PWY-5653
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - gomodel:YeastPathways_PWY3O-4106
  - WikiPathways:WP171
  - MetaCyc:PWY-6993
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:PWY0-1352
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-1801
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:PWY-8178
  - MetaCyc:OXIDATIVEPENT-PWY
  - WikiPathways:WP5060
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - MetaCyc:PWY-6289
  - MetaCyc:PWY0-321
  - gomodel:YeastPathways_PWY3O-4153
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:PWY-6534
  - MetaCyc:PWY0-1277
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - WikiPathways:WP71
  - MetaCyc:PANTO-PWY
  - MetaCyc:PWY1-3
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:P184-PWY
  - GO:0019618
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6019
  - PathBank:SMP0002089
  - PathBank:SMP0002067
  - GO:0042864
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-7181
  - GO:0010139
  - PathBank:SMP0002038
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_PWY3O-440
  - MetaCyc:PWY-7545
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:PWY-6416
  - PathBank:SMP0002406
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:PWY-6151
  - gomodel:YeastPathways_PWY-5041
  - MetaCyc:PWY-8132
  - gomodel:YeastPathways_YEAST-RNT-SALV
  - MetaCyc:PWY0-1517
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:PWY-6419
  - gomodel:YeastPathways_PWY-5194-1
  - PathBank:SMP0002097
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - MIBiG:BGC0000852
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY0-43
  - gomodel:YeastPathways_PWY-5340
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7722
  - gomodel:YeastPathways_DETOX1-PWY
  - MetaCyc:PWY-5838
  - WikiPathways:WP296
  - gomodel:YeastPathways_PWY-6614
  - MetaCyc:PWY0-1433
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-17
  - MetaCyc:THISYN-PWY
  - MetaCyc:THIOREDOX-PWY
  - PathBank:SMP0000992
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_PWY-5123
  - MetaCyc:TRESYN-PWY
  - WikiPathways:WP266
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-4120
  - WikiPathways:WP287
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - MetaCyc:PWY-5686
  - MetaCyc:PWY0-1471
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWY-6074-1
  command: .venv/bin/pytest -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C2-PYTEST
  scope_note: Repository-wide test suite covering all 271 maintained records and review
    contracts.
- check_id: lint
  name: Ruff code and script lint check (just lint)
  status: passed
  required: true
  summary: Ruff lint passed with zero warnings or errors.
  target_ids:
  - MetaCyc:PWY-5901
  - MetaCyc:PWY0-42
  - WikiPathways:WP5587
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-6543
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - gomodel:YeastPathways_PWY-6147
  - GO:0097288
  - MetaCyc:PWY0-1312
  - MetaCyc:ACETOACETATE-DEG-PWY
  - WikiPathways:WP5019
  - PathBank:SMP0002081
  - MetaCyc:P121-PWY
  - PathBank:SMP0002083
  - MetaCyc:PWY-6609
  - gomodel:YeastPathways_PWY-7220-1
  - MetaCyc:SALVADEHYPOX-PWY
  - gomodel:YeastPathways_PWY-7219
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-1241
  - GO:0019270
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - MetaCyc:PWY0-41
  - gomodel:YeastPathways_PWY-5694
  - MetaCyc:PWY-5705
  - gomodel:YeastPathways_PWY-5697
  - MetaCyc:GLCMANNANAUT-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - MetaCyc:PWY-5903
  - PathBank:SMP0002123
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:P321-PWY
  - gomodel:YeastPathways_PWY-5760-1
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - GO:0043427
  - gomodel:YeastPathways_PWY3O-4
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5417
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - gomodel:YeastPathways_PWY3O-15
  - MetaCyc:ARO-PWY
  - MIBiG:BGC0000829
  - MetaCyc:P2-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - MetaCyc:COA-PWY
  - GO:0036040
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:PWY-6376
  - KEGG:M00374
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-123
  - GO:0019305
  - MetaCyc:P101-PWY
  - KEGG:M00008
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-6075-1
  - MetaCyc:PWY-7255
  - gomodel:YeastPathways_PWY3O-4300
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1280
  - KEGG:M00373
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - MetaCyc:RIBOSYN2-PWY
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY-1801-1
  - MetaCyc:PWY0-521
  - GO:1901281
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:PWY-6223
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - WikiPathways:WP556
  - MetaCyc:PWY-5177
  - MetaCyc:GLUTATHIONESYN-PWY
  - gomodel:YeastPathways_PWYQT-4432
  - WikiPathways:WP392
  - gomodel:YeastPathways_PWY3O-48
  - MetaCyc:GLYCEROLMETAB-PWY
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - WikiPathways:WP478
  - gomodel:YeastPathways_GLYCOLYSIS
  - MetaCyc:PWY-5744
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - GO:1902000
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - gomodel:YeastPathways_PWY3O-402
  - WikiPathways:WP178
  - MetaCyc:PWY0-1338
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:PWY0-301
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - PathBank:SMP0002051
  - MetaCyc:CYSTSYN-PWY
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - gomodel:YeastPathways_PWY-5344
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - MetaCyc:LYXMET-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - gomodel:YeastPathways_PROUT-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - gomodel:YeastPathways_PWY-5651
  - MetaCyc:TYRSYN
  - gomodel:YeastPathways_PWY3O-4108
  - MetaCyc:VALSYN-PWY
  - gomodel:YeastPathways_PWY3O-4112
  - MIBiG:BGC0002072
  - gomodel:6882d2b800000609
  - MetaCyc:PWY0-501
  - gomodel:YeastPathways_PWY3O-1743
  - MetaCyc:PWY0-1300
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - gomodel:YeastPathways_PWY3O-64
  - MetaCyc:NONMEVIPP-PWY
  - gomodel:YeastPathways_PWY-901
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5453
  - PathBank:SMP0002077
  - MetaCyc:PWY-6048
  - gomodel:YeastPathways_IPPSYN-PWY
  - MetaCyc:PWY-6823
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - gomodel:YeastPathways_PWY-2301
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - gomodel:YeastPathways_PWY-5653
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - gomodel:YeastPathways_PWY3O-4106
  - WikiPathways:WP171
  - MetaCyc:PWY-6993
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:PWY0-1352
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-1801
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:PWY-8178
  - MetaCyc:OXIDATIVEPENT-PWY
  - WikiPathways:WP5060
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - MetaCyc:PWY-6289
  - MetaCyc:PWY0-321
  - gomodel:YeastPathways_PWY3O-4153
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:PWY-6534
  - MetaCyc:PWY0-1277
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - WikiPathways:WP71
  - MetaCyc:PANTO-PWY
  - MetaCyc:PWY1-3
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:P184-PWY
  - GO:0019618
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6019
  - PathBank:SMP0002089
  - PathBank:SMP0002067
  - GO:0042864
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-7181
  - GO:0010139
  - PathBank:SMP0002038
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_PWY3O-440
  - MetaCyc:PWY-7545
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:PWY-6416
  - PathBank:SMP0002406
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:PWY-6151
  - gomodel:YeastPathways_PWY-5041
  - MetaCyc:PWY-8132
  - gomodel:YeastPathways_YEAST-RNT-SALV
  - MetaCyc:PWY0-1517
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:PWY-6419
  - gomodel:YeastPathways_PWY-5194-1
  - PathBank:SMP0002097
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - MIBiG:BGC0000852
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY0-43
  - gomodel:YeastPathways_PWY-5340
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7722
  - gomodel:YeastPathways_DETOX1-PWY
  - MetaCyc:PWY-5838
  - WikiPathways:WP296
  - gomodel:YeastPathways_PWY-6614
  - MetaCyc:PWY0-1433
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-17
  - MetaCyc:THISYN-PWY
  - MetaCyc:THIOREDOX-PWY
  - PathBank:SMP0000992
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_PWY-5123
  - MetaCyc:TRESYN-PWY
  - WikiPathways:WP266
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-4120
  - WikiPathways:WP287
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - MetaCyc:PWY-5686
  - MetaCyc:PWY0-1471
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWY-6074-1
  command: .venv/bin/ruff check --no-cache .
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C2-RUFF
  scope_note: Repository-wide Python lint check.
- check_id: diff-check
  name: Git whitespace and conflict marker gate
  status: passed
  required: true
  summary: git diff --check passed with zero issues.
  target_ids:
  - MetaCyc:PWY-5901
  - MetaCyc:PWY0-42
  - WikiPathways:WP5587
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-6543
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - gomodel:YeastPathways_PWY-6147
  - GO:0097288
  - MetaCyc:PWY0-1312
  - MetaCyc:ACETOACETATE-DEG-PWY
  - WikiPathways:WP5019
  - PathBank:SMP0002081
  - MetaCyc:P121-PWY
  - PathBank:SMP0002083
  - MetaCyc:PWY-6609
  - gomodel:YeastPathways_PWY-7220-1
  - MetaCyc:SALVADEHYPOX-PWY
  - gomodel:YeastPathways_PWY-7219
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-1241
  - GO:0019270
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - MetaCyc:PWY0-41
  - gomodel:YeastPathways_PWY-5694
  - MetaCyc:PWY-5705
  - gomodel:YeastPathways_PWY-5697
  - MetaCyc:GLCMANNANAUT-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - MetaCyc:PWY-5903
  - PathBank:SMP0002123
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:P321-PWY
  - gomodel:YeastPathways_PWY-5760-1
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - GO:0043427
  - gomodel:YeastPathways_PWY3O-4
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5417
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - gomodel:YeastPathways_PWY3O-15
  - MetaCyc:ARO-PWY
  - MIBiG:BGC0000829
  - MetaCyc:P2-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - MetaCyc:COA-PWY
  - GO:0036040
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:PWY-6376
  - KEGG:M00374
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-123
  - GO:0019305
  - MetaCyc:P101-PWY
  - KEGG:M00008
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-6075-1
  - MetaCyc:PWY-7255
  - gomodel:YeastPathways_PWY3O-4300
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1280
  - KEGG:M00373
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - MetaCyc:RIBOSYN2-PWY
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY-1801-1
  - MetaCyc:PWY0-521
  - GO:1901281
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:PWY-6223
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - WikiPathways:WP556
  - MetaCyc:PWY-5177
  - MetaCyc:GLUTATHIONESYN-PWY
  - gomodel:YeastPathways_PWYQT-4432
  - WikiPathways:WP392
  - gomodel:YeastPathways_PWY3O-48
  - MetaCyc:GLYCEROLMETAB-PWY
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - WikiPathways:WP478
  - gomodel:YeastPathways_GLYCOLYSIS
  - MetaCyc:PWY-5744
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - GO:1902000
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - gomodel:YeastPathways_PWY3O-402
  - WikiPathways:WP178
  - MetaCyc:PWY0-1338
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:PWY0-301
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - PathBank:SMP0002051
  - MetaCyc:CYSTSYN-PWY
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - gomodel:YeastPathways_PWY-5344
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - MetaCyc:LYXMET-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - gomodel:YeastPathways_PROUT-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - gomodel:YeastPathways_PWY-5651
  - MetaCyc:TYRSYN
  - gomodel:YeastPathways_PWY3O-4108
  - MetaCyc:VALSYN-PWY
  - gomodel:YeastPathways_PWY3O-4112
  - MIBiG:BGC0002072
  - gomodel:6882d2b800000609
  - MetaCyc:PWY0-501
  - gomodel:YeastPathways_PWY3O-1743
  - MetaCyc:PWY0-1300
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - gomodel:YeastPathways_PWY3O-64
  - MetaCyc:NONMEVIPP-PWY
  - gomodel:YeastPathways_PWY-901
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5453
  - PathBank:SMP0002077
  - MetaCyc:PWY-6048
  - gomodel:YeastPathways_IPPSYN-PWY
  - MetaCyc:PWY-6823
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - gomodel:YeastPathways_PWY-2301
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - gomodel:YeastPathways_PWY-5653
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - gomodel:YeastPathways_PWY3O-4106
  - WikiPathways:WP171
  - MetaCyc:PWY-6993
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:PWY0-1352
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-1801
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:PWY-8178
  - MetaCyc:OXIDATIVEPENT-PWY
  - WikiPathways:WP5060
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - MetaCyc:PWY-6289
  - MetaCyc:PWY0-321
  - gomodel:YeastPathways_PWY3O-4153
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:PWY-6534
  - MetaCyc:PWY0-1277
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - WikiPathways:WP71
  - MetaCyc:PANTO-PWY
  - MetaCyc:PWY1-3
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:P184-PWY
  - GO:0019618
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6019
  - PathBank:SMP0002089
  - PathBank:SMP0002067
  - GO:0042864
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-7181
  - GO:0010139
  - PathBank:SMP0002038
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_PWY3O-440
  - MetaCyc:PWY-7545
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:PWY-6416
  - PathBank:SMP0002406
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:PWY-6151
  - gomodel:YeastPathways_PWY-5041
  - MetaCyc:PWY-8132
  - gomodel:YeastPathways_YEAST-RNT-SALV
  - MetaCyc:PWY0-1517
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:PWY-6419
  - gomodel:YeastPathways_PWY-5194-1
  - PathBank:SMP0002097
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - MIBiG:BGC0000852
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY0-43
  - gomodel:YeastPathways_PWY-5340
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7722
  - gomodel:YeastPathways_DETOX1-PWY
  - MetaCyc:PWY-5838
  - WikiPathways:WP296
  - gomodel:YeastPathways_PWY-6614
  - MetaCyc:PWY0-1433
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-17
  - MetaCyc:THISYN-PWY
  - MetaCyc:THIOREDOX-PWY
  - PathBank:SMP0000992
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_PWY-5123
  - MetaCyc:TRESYN-PWY
  - WikiPathways:WP266
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-4120
  - WikiPathways:WP287
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - MetaCyc:PWY-5686
  - MetaCyc:PWY0-1471
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWY-6074-1
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C2-GIT-DIFF
  scope_note: Worktree cleanliness check at frozen base commit.
- check_id: review-check
  name: Structured review bundle contract check (just review-check)
  status: passed
  required: true
  summary: All 199 pre-existing structured review bundles in reviews/structured/ passed
    schema and append-only checks.
  target_ids:
  - MetaCyc:PWY-5901
  - MetaCyc:PWY0-42
  - WikiPathways:WP5587
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-6543
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - gomodel:YeastPathways_PWY-6147
  - GO:0097288
  - MetaCyc:PWY0-1312
  - MetaCyc:ACETOACETATE-DEG-PWY
  - WikiPathways:WP5019
  - PathBank:SMP0002081
  - MetaCyc:P121-PWY
  - PathBank:SMP0002083
  - MetaCyc:PWY-6609
  - gomodel:YeastPathways_PWY-7220-1
  - MetaCyc:SALVADEHYPOX-PWY
  - gomodel:YeastPathways_PWY-7219
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-1241
  - GO:0019270
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - MetaCyc:PWY0-41
  - gomodel:YeastPathways_PWY-5694
  - MetaCyc:PWY-5705
  - gomodel:YeastPathways_PWY-5697
  - MetaCyc:GLCMANNANAUT-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - MetaCyc:PWY-5903
  - PathBank:SMP0002123
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:P321-PWY
  - gomodel:YeastPathways_PWY-5760-1
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - GO:0043427
  - gomodel:YeastPathways_PWY3O-4
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5417
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - gomodel:YeastPathways_PWY3O-15
  - MetaCyc:ARO-PWY
  - MIBiG:BGC0000829
  - MetaCyc:P2-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - MetaCyc:COA-PWY
  - GO:0036040
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:PWY-6376
  - KEGG:M00374
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-123
  - GO:0019305
  - MetaCyc:P101-PWY
  - KEGG:M00008
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-6075-1
  - MetaCyc:PWY-7255
  - gomodel:YeastPathways_PWY3O-4300
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1280
  - KEGG:M00373
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - MetaCyc:RIBOSYN2-PWY
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY-1801-1
  - MetaCyc:PWY0-521
  - GO:1901281
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:PWY-6223
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - WikiPathways:WP556
  - MetaCyc:PWY-5177
  - MetaCyc:GLUTATHIONESYN-PWY
  - gomodel:YeastPathways_PWYQT-4432
  - WikiPathways:WP392
  - gomodel:YeastPathways_PWY3O-48
  - MetaCyc:GLYCEROLMETAB-PWY
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - WikiPathways:WP478
  - gomodel:YeastPathways_GLYCOLYSIS
  - MetaCyc:PWY-5744
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - GO:1902000
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - gomodel:YeastPathways_PWY3O-402
  - WikiPathways:WP178
  - MetaCyc:PWY0-1338
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:PWY0-301
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - PathBank:SMP0002051
  - MetaCyc:CYSTSYN-PWY
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - gomodel:YeastPathways_PWY-5344
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - MetaCyc:LYXMET-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - gomodel:YeastPathways_PROUT-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - gomodel:YeastPathways_PWY-5651
  - MetaCyc:TYRSYN
  - gomodel:YeastPathways_PWY3O-4108
  - MetaCyc:VALSYN-PWY
  - gomodel:YeastPathways_PWY3O-4112
  - MIBiG:BGC0002072
  - gomodel:6882d2b800000609
  - MetaCyc:PWY0-501
  - gomodel:YeastPathways_PWY3O-1743
  - MetaCyc:PWY0-1300
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - gomodel:YeastPathways_PWY3O-64
  - MetaCyc:NONMEVIPP-PWY
  - gomodel:YeastPathways_PWY-901
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5453
  - PathBank:SMP0002077
  - MetaCyc:PWY-6048
  - gomodel:YeastPathways_IPPSYN-PWY
  - MetaCyc:PWY-6823
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - gomodel:YeastPathways_PWY-2301
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - gomodel:YeastPathways_PWY-5653
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - gomodel:YeastPathways_PWY3O-4106
  - WikiPathways:WP171
  - MetaCyc:PWY-6993
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:PWY0-1352
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-1801
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:PWY-8178
  - MetaCyc:OXIDATIVEPENT-PWY
  - WikiPathways:WP5060
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - MetaCyc:PWY-6289
  - MetaCyc:PWY0-321
  - gomodel:YeastPathways_PWY3O-4153
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:PWY-6534
  - MetaCyc:PWY0-1277
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - WikiPathways:WP71
  - MetaCyc:PANTO-PWY
  - MetaCyc:PWY1-3
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:P184-PWY
  - GO:0019618
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6019
  - PathBank:SMP0002089
  - PathBank:SMP0002067
  - GO:0042864
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-7181
  - GO:0010139
  - PathBank:SMP0002038
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_PWY3O-440
  - MetaCyc:PWY-7545
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:PWY-6416
  - PathBank:SMP0002406
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:PWY-6151
  - gomodel:YeastPathways_PWY-5041
  - MetaCyc:PWY-8132
  - gomodel:YeastPathways_YEAST-RNT-SALV
  - MetaCyc:PWY0-1517
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:PWY-6419
  - gomodel:YeastPathways_PWY-5194-1
  - PathBank:SMP0002097
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - MIBiG:BGC0000852
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY0-43
  - gomodel:YeastPathways_PWY-5340
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7722
  - gomodel:YeastPathways_DETOX1-PWY
  - MetaCyc:PWY-5838
  - WikiPathways:WP296
  - gomodel:YeastPathways_PWY-6614
  - MetaCyc:PWY0-1433
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-17
  - MetaCyc:THISYN-PWY
  - MetaCyc:THIOREDOX-PWY
  - PathBank:SMP0000992
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_PWY-5123
  - MetaCyc:TRESYN-PWY
  - WikiPathways:WP266
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-4120
  - WikiPathways:WP287
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - MetaCyc:PWY-5686
  - MetaCyc:PWY0-1471
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWY-6074-1
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - EV-C2-REVIEW-CHECK
  scope_note: Validates all retained reviews/structured/ bundles against schema/record_review.yaml.
evidence:
- evidence_id: EV-C2-QC-VALIDATE
  kind: validation
  reference: .venv/bin/pathwaymech-run-qc
  locator: stdout summary (271 pathway records, 654 history records, 22,211 evidence
    blocks, 33 source records)
  accessed_at: '2026-10-22T13:18:00Z'
  support: supports
  summary: 'Executed .venv/bin/pathwaymech-run-qc across the frozen working tree at
    e369fa425e64d4f794ce84e2fd71138a43660467: validated 271 pathway records against
    the closed LinkML schema, verified all identifiers and labels against local authority
    snapshots, validated 654 history records and 22,211 evidence blocks, validated
    33 source records, and confirmed pages/ synchrony with 271 pathway records.'
- evidence_id: EV-C2-PYTEST
  kind: validation
  reference: .venv/bin/pytest -q
  locator: pytest suite execution across tests/ (8,066 passed, 3 skipped)
  accessed_at: '2026-10-22T13:33:00Z'
  support: supports
  summary: Executed the full pytest suite (8,066 passed, 3 skipped), verifying closed
    LinkML schema validation, identifier policy, KGX export, SSSOM export, source
    registry, and structured record-review contract invariants.
- evidence_id: EV-C2-RUFF
  kind: validation
  reference: .venv/bin/ruff check --no-cache .
  locator: ruff check output
  accessed_at: '2026-10-22T13:18:00Z'
  support: supports
  summary: Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks
    passed).
- evidence_id: EV-C2-GIT-DIFF
  kind: validation
  reference: git diff --check
  locator: git worktree at e369fa425e64d4f794ce84e2fd71138a43660467
  accessed_at: '2026-10-22T13:18:00Z'
  support: supports
  summary: Executed git diff --check with exit code 0; no whitespace errors or conflict
    markers.
- evidence_id: EV-C2-REVIEW-CHECK
  kind: prior_review
  reference: reviews/structured/
  locator: 199 retained structured review bundles
  accessed_at: '2026-10-22T13:18:00Z'
  support: supports
  summary: Validated all 199 previously retained structured review bundles under reviews/structured/
    via scripts/record_review.py check; confirmed Cycle 1 Stage 4 findings (F-STAGE4-001
    and F-STAGE4-002) were resolved in 20261022T033000Z-stage5-resolve-review-findings
    and zero open finding heads exist on maintained data/pathways/*.yaml records prior
    to this Cycle 2 Stage 4 review.
- evidence_id: EV-C2-CORPUS-INSPECTION
  kind: record_content
  reference: data/pathways/
  locator: 271 maintained pathway YAML files (7,684 participants, 1,597 reactions
    including 699 RHEA:* reactions, 14,393 mechanistic_edges, 7,042 references, 615
    source_mappings across 112 records)
  accessed_at: '2026-10-22T13:20:00Z'
  support: supports
  summary: 'Inspected all 271 maintained pathway records in data/pathways/*.yaml:
    100% declare valid pathway_type, 100% of 14,393 mechanistic_edges carry structured
    evidence blocks (21,085 edge-level evidence items; 22,211 total evidence blocks
    across records, steps, and edges), 100% of 699 RHEA:* reaction nodes declare explicit
    direction with zero cross-record direction conflicts, zero within-record mixed
    reaction category lists remain, and 615 source_mappings across 112 records export
    to 612 unique rows in output/sssom/source_mappings.sssom.tsv.'
- evidence_id: EV-C2-SHARED-REACTION-INCONSISTENCY
  kind: record_content
  reference: data/pathways/l-threonine-biosynthesis.yaml
  locator: lines 37-43 (reactions[0..1] in MetaCyc:HOMOSER-THRESYN-PWY vs PathBank:SMP0000992)
  accessed_at: '2026-10-22T13:34:00Z'
  support: supports
  summary: 'Across 16 maintained MetaCyc pathway records, 28 reaction occurrences
    spanning 23 shared catalytic reaction CURIEs (22 RHEA:* + 1 MetaCyc:DHBAMPLIG-RXN)
    omit category: molecular_activity even though those same 23 reaction CURIEs explicitly
    declare category: molecular_activity in sibling maintained records (e.g., RHEA:13986
    and RHEA:10841 in MetaCyc:HOMOSER-THRESYN-PWY omit category while declaring category:
    molecular_activity in PathBank:SMP0000992).'
  quote: "reactions:\n- id: RHEA:13986\n  label: L-homoserine + ATP = O-phospho-L-homoserine\
    \ + ADP + H+\n  direction: left_to_right\n- id: RHEA:10841\n  label: O-phospho-L-homoserine\
    \ + H2O = L-threonine + phosphate\n  direction: left_to_right"
  snapshot_sha256: e277951647e3da86c7ad92ac40a3e8d795c36f1550d67825898927540fe5dfa3
- evidence_id: EV-C2-KGX-EXPORT
  kind: record_content
  reference: src/pathwaymech/kgx.py
  locator: lines 70-103, 173-177, and 254-275 (EXPLICIT_CATEGORIES, _PREFIX_CATEGORIES,
    and _add_node)
  accessed_at: '2026-10-22T13:34:00Z'
  support: supports
  summary: 'In src/pathwaymech/kgx.py, reactions with explicit category: molecular_activity
    map to biolink:MolecularActivity with source_category=''molecular_activity'',
    whereas RHEA:* and MetaCyc:* reactions omitting category fall back via _PREFIX_CATEGORIES
    to biolink:BiochemicalReaction with empty source_category=''''; when a reaction
    CURIE is shared between a typed record and an untyped record, _add_node promotes
    the node''s top-level category to biolink:MolecularActivity while preserving mixed
    typed and untyped entries in source_contexts.'
  quote: "if source_category and not existing.source_category:\n        merged_category\
    \ = category\n    elif existing.source_category and not source_category:\n   \
    \     merged_category = existing.category"
  snapshot_sha256: 23296ae17aeeea4518a972ee140640a69bf00e6b09203d04a3e13f9e13fc4790
- evidence_id: EV-C2-NODES-TSV
  kind: record_content
  reference: pages/downloads/nodes.tsv
  locator: 23 shared reaction rows with mixed source_contexts and 231 untyped-only
    reaction rows with biolink:BiochemicalReaction
  accessed_at: '2026-10-22T13:35:00Z'
  support: supports
  summary: In pages/downloads/nodes.tsv, 23 shared reaction CURIEs (e.g., RHEA:10841,
    RHEA:13986, RHEA:15763, RHEA:23777, RHEA:24286, RHEA:34172) carry top-level category
    biolink:MolecularActivity and source_category=molecular_activity while their source_contexts
    JSON array mixes contexts with and without category, and 231 unique reaction CURIEs
    (216 RHEA:* and 15 MetaCyc:*) appearing only in the 56 untyped MetaCyc records
    export as biolink:BiochemicalReaction with empty source_category.
  quote: "RHEA:10052\tbiolink:BiochemicalReaction\t3-oxoadipyl-CoA + CoA = acetyl-CoA\
    \ + succinyl-CoA\t\tleft_to_right"
  snapshot_sha256: 58a152c9a02ae003bb7398292cb33a2ec22994c29b8273eb290bafe122134ce3
- evidence_id: EV-C2-UNTYPED-56-METACYC-RECORDS
  kind: record_content
  reference: data/pathways/
  locator: '56 maintained MetaCyc pathway records (279 reactions: 263 RHEA:* and 16
    MetaCyc:*)'
  accessed_at: '2026-10-22T13:35:00Z'
  support: supports
  summary: 'Across the 271 maintained pathway records, 212 records with reactions[]
    (86 gomodel:*, 84 MetaCyc:*, 12 WikiPathways:*, 11 PathBank:*, 10 GO:*, 6 Reactome:*,
    3 KEGG:*) explicitly declare category on 100% of their 1,318 reactions[] entries
    (1,312 molecular_activity and 6 pathway) and 3 MIBiG:* records have 0 reactions[],
    whereas 56 maintained MetaCyc:* records omit category: molecular_activity across
    all 279 of their reactions[] entries (263 RHEA:* and 16 MetaCyc:*).'
assessments:
- assessment_id: ASSESS-C2-IDENTITY-GROUNDING-ALL-271
  area: identity
  topic: Pathway identity, taxon grounding, authority-verified CURIEs, and SSSOM source_mappings
    across all 271 maintained records
  outcome: supported
  summary: All 271 maintained pathway records in data/pathways/*.yaml denote coherent
    microbial pathways, gene clusters, or signaling/virulence modules with authority-verified
    pathway IDs, NCBITaxon groundings, CHEBI/UniProtKB/ComplexPortal/GO/SGD participant
    CURIEs, RHEA/MetaCyc/BiGG/Reactome/WikiPathways reaction identifiers, and 615
    source_mappings rows across 112 records exporting cleanly to 612 unique SSSOM
    rows in output/sssom/source_mappings.sssom.tsv.
  target_ids:
  - MetaCyc:PWY-5901
  - MetaCyc:PWY0-42
  - WikiPathways:WP5587
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-6543
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - gomodel:YeastPathways_PWY-6147
  - GO:0097288
  - MetaCyc:PWY0-1312
  - MetaCyc:ACETOACETATE-DEG-PWY
  - WikiPathways:WP5019
  - PathBank:SMP0002081
  - MetaCyc:P121-PWY
  - PathBank:SMP0002083
  - MetaCyc:PWY-6609
  - gomodel:YeastPathways_PWY-7220-1
  - MetaCyc:SALVADEHYPOX-PWY
  - gomodel:YeastPathways_PWY-7219
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-1241
  - GO:0019270
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - MetaCyc:PWY0-41
  - gomodel:YeastPathways_PWY-5694
  - MetaCyc:PWY-5705
  - gomodel:YeastPathways_PWY-5697
  - MetaCyc:GLCMANNANAUT-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - MetaCyc:PWY-5903
  - PathBank:SMP0002123
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:P321-PWY
  - gomodel:YeastPathways_PWY-5760-1
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - GO:0043427
  - gomodel:YeastPathways_PWY3O-4
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5417
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - gomodel:YeastPathways_PWY3O-15
  - MetaCyc:ARO-PWY
  - MIBiG:BGC0000829
  - MetaCyc:P2-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - MetaCyc:COA-PWY
  - GO:0036040
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:PWY-6376
  - KEGG:M00374
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-123
  - GO:0019305
  - MetaCyc:P101-PWY
  - KEGG:M00008
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-6075-1
  - MetaCyc:PWY-7255
  - gomodel:YeastPathways_PWY3O-4300
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1280
  - KEGG:M00373
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - MetaCyc:RIBOSYN2-PWY
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY-1801-1
  - MetaCyc:PWY0-521
  - GO:1901281
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:PWY-6223
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - WikiPathways:WP556
  - MetaCyc:PWY-5177
  - MetaCyc:GLUTATHIONESYN-PWY
  - gomodel:YeastPathways_PWYQT-4432
  - WikiPathways:WP392
  - gomodel:YeastPathways_PWY3O-48
  - MetaCyc:GLYCEROLMETAB-PWY
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - WikiPathways:WP478
  - gomodel:YeastPathways_GLYCOLYSIS
  - MetaCyc:PWY-5744
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - GO:1902000
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - gomodel:YeastPathways_PWY3O-402
  - WikiPathways:WP178
  - MetaCyc:PWY0-1338
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:PWY0-301
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - PathBank:SMP0002051
  - MetaCyc:CYSTSYN-PWY
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - gomodel:YeastPathways_PWY-5344
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - MetaCyc:LYXMET-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - gomodel:YeastPathways_PROUT-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - gomodel:YeastPathways_PWY-5651
  - MetaCyc:TYRSYN
  - gomodel:YeastPathways_PWY3O-4108
  - MetaCyc:VALSYN-PWY
  - gomodel:YeastPathways_PWY3O-4112
  - MIBiG:BGC0002072
  - gomodel:6882d2b800000609
  - MetaCyc:PWY0-501
  - gomodel:YeastPathways_PWY3O-1743
  - MetaCyc:PWY0-1300
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - gomodel:YeastPathways_PWY3O-64
  - MetaCyc:NONMEVIPP-PWY
  - gomodel:YeastPathways_PWY-901
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5453
  - PathBank:SMP0002077
  - MetaCyc:PWY-6048
  - gomodel:YeastPathways_IPPSYN-PWY
  - MetaCyc:PWY-6823
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - gomodel:YeastPathways_PWY-2301
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - gomodel:YeastPathways_PWY-5653
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - gomodel:YeastPathways_PWY3O-4106
  - WikiPathways:WP171
  - MetaCyc:PWY-6993
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:PWY0-1352
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-1801
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:PWY-8178
  - MetaCyc:OXIDATIVEPENT-PWY
  - WikiPathways:WP5060
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - MetaCyc:PWY-6289
  - MetaCyc:PWY0-321
  - gomodel:YeastPathways_PWY3O-4153
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:PWY-6534
  - MetaCyc:PWY0-1277
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - WikiPathways:WP71
  - MetaCyc:PANTO-PWY
  - MetaCyc:PWY1-3
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:P184-PWY
  - GO:0019618
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6019
  - PathBank:SMP0002089
  - PathBank:SMP0002067
  - GO:0042864
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-7181
  - GO:0010139
  - PathBank:SMP0002038
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_PWY3O-440
  - MetaCyc:PWY-7545
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:PWY-6416
  - PathBank:SMP0002406
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:PWY-6151
  - gomodel:YeastPathways_PWY-5041
  - MetaCyc:PWY-8132
  - gomodel:YeastPathways_YEAST-RNT-SALV
  - MetaCyc:PWY0-1517
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:PWY-6419
  - gomodel:YeastPathways_PWY-5194-1
  - PathBank:SMP0002097
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - MIBiG:BGC0000852
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY0-43
  - gomodel:YeastPathways_PWY-5340
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7722
  - gomodel:YeastPathways_DETOX1-PWY
  - MetaCyc:PWY-5838
  - WikiPathways:WP296
  - gomodel:YeastPathways_PWY-6614
  - MetaCyc:PWY0-1433
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-17
  - MetaCyc:THISYN-PWY
  - MetaCyc:THIOREDOX-PWY
  - PathBank:SMP0000992
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_PWY-5123
  - MetaCyc:TRESYN-PWY
  - WikiPathways:WP266
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-4120
  - WikiPathways:WP287
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - MetaCyc:PWY-5686
  - MetaCyc:PWY0-1471
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWY-6074-1
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
  - EV-C2-REVIEW-CHECK
  metrics:
  - name: maintained_pathway_records_reviewed
    value: 271.0
    unit: records
    definition: Count of maintained pathway YAML records in data/pathways/*.yaml inspected
      in full.
    denominator: 271
    minimum: 0.0
    maximum: 271.0
  - name: authority_identifier_verification_rate
    value: 100.0
    unit: percent
    definition: Percentage of maintained pathway records whose pathway, taxon, participant,
      and reaction identifiers pass local authority snapshot verification.
    denominator: 271
    minimum: 0.0
    maximum: 100.0
  dimensions:
  - name: corpus_scope
    value: full_maintained_inventory
    definition: All 271 maintained YAML records in data/pathways/*.yaml at frozen
      Git base e369fa425e64d4f794ce84e2fd71138a43660467.
    evidence_ids:
    - EV-C2-CORPUS-INSPECTION
  - name: namespace_distribution
    value: MetaCyc:140, gomodel:86, WikiPathways:12, PathBank:11, GO:10, Reactome:6,
      KEGG:3, MIBiG:3
    definition: Distribution of primary pathway identifier prefixes across the 271
      maintained records.
    evidence_ids:
    - EV-C2-CORPUS-INSPECTION
- assessment_id: ASSESS-C2-CAUSAL-GRAPH-EVIDENCE-ALL-271
  area: graph
  topic: Causal graph connectivity, reaction directionality, stoichiometry, and edge-level
    evidence across all 271 maintained records
  outcome: supported
  summary: All 271 maintained records contain connected participant-reaction-edge
    causal graphs (7,684 participants, 1,597 reactions including 699 RHEA:* reactions,
    14,393 mechanistic_edges) with 100% edge-level evidence coverage (21,085 edge-level
    evidence items; 22,211 total evidence blocks across records, steps, and edges),
    explicit direction on 100% of 699 RHEA:* reaction nodes, and zero cross-record
    RHEA direction conflicts.
  target_ids:
  - MetaCyc:PWY-5901
  - MetaCyc:PWY0-42
  - WikiPathways:WP5587
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-6543
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - gomodel:YeastPathways_PWY-6147
  - GO:0097288
  - MetaCyc:PWY0-1312
  - MetaCyc:ACETOACETATE-DEG-PWY
  - WikiPathways:WP5019
  - PathBank:SMP0002081
  - MetaCyc:P121-PWY
  - PathBank:SMP0002083
  - MetaCyc:PWY-6609
  - gomodel:YeastPathways_PWY-7220-1
  - MetaCyc:SALVADEHYPOX-PWY
  - gomodel:YeastPathways_PWY-7219
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-1241
  - GO:0019270
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - MetaCyc:PWY0-41
  - gomodel:YeastPathways_PWY-5694
  - MetaCyc:PWY-5705
  - gomodel:YeastPathways_PWY-5697
  - MetaCyc:GLCMANNANAUT-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - MetaCyc:PWY-5903
  - PathBank:SMP0002123
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:P321-PWY
  - gomodel:YeastPathways_PWY-5760-1
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - GO:0043427
  - gomodel:YeastPathways_PWY3O-4
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5417
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - gomodel:YeastPathways_PWY3O-15
  - MetaCyc:ARO-PWY
  - MIBiG:BGC0000829
  - MetaCyc:P2-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - MetaCyc:COA-PWY
  - GO:0036040
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:PWY-6376
  - KEGG:M00374
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-123
  - GO:0019305
  - MetaCyc:P101-PWY
  - KEGG:M00008
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-6075-1
  - MetaCyc:PWY-7255
  - gomodel:YeastPathways_PWY3O-4300
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1280
  - KEGG:M00373
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - MetaCyc:RIBOSYN2-PWY
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY-1801-1
  - MetaCyc:PWY0-521
  - GO:1901281
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:PWY-6223
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - WikiPathways:WP556
  - MetaCyc:PWY-5177
  - MetaCyc:GLUTATHIONESYN-PWY
  - gomodel:YeastPathways_PWYQT-4432
  - WikiPathways:WP392
  - gomodel:YeastPathways_PWY3O-48
  - MetaCyc:GLYCEROLMETAB-PWY
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - WikiPathways:WP478
  - gomodel:YeastPathways_GLYCOLYSIS
  - MetaCyc:PWY-5744
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - GO:1902000
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - gomodel:YeastPathways_PWY3O-402
  - WikiPathways:WP178
  - MetaCyc:PWY0-1338
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:PWY0-301
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - PathBank:SMP0002051
  - MetaCyc:CYSTSYN-PWY
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - gomodel:YeastPathways_PWY-5344
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - MetaCyc:LYXMET-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - gomodel:YeastPathways_PROUT-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRPSYN-PWY
  - gomodel:YeastPathways_PWY-5651
  - MetaCyc:TYRSYN
  - gomodel:YeastPathways_PWY3O-4108
  - MetaCyc:VALSYN-PWY
  - gomodel:YeastPathways_PWY3O-4112
  - MIBiG:BGC0002072
  - gomodel:6882d2b800000609
  - MetaCyc:PWY0-501
  - gomodel:YeastPathways_PWY3O-1743
  - MetaCyc:PWY0-1300
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - gomodel:YeastPathways_PWY3O-64
  - MetaCyc:NONMEVIPP-PWY
  - gomodel:YeastPathways_PWY-901
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5453
  - PathBank:SMP0002077
  - MetaCyc:PWY-6048
  - gomodel:YeastPathways_IPPSYN-PWY
  - MetaCyc:PWY-6823
  - Reactome:R-MTU-936721
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - gomodel:YeastPathways_PWY-2301
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - gomodel:YeastPathways_PWY-5653
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - gomodel:YeastPathways_PWY3O-4106
  - WikiPathways:WP171
  - MetaCyc:PWY-6993
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:PWY0-1352
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-1801
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:PWY-8178
  - MetaCyc:OXIDATIVEPENT-PWY
  - WikiPathways:WP5060
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - MetaCyc:PWY-6289
  - MetaCyc:PWY0-321
  - gomodel:YeastPathways_PWY3O-4153
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:PWY-6534
  - MetaCyc:PWY0-1277
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - WikiPathways:WP71
  - MetaCyc:PANTO-PWY
  - MetaCyc:PWY1-3
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:P184-PWY
  - GO:0019618
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6019
  - PathBank:SMP0002089
  - PathBank:SMP0002067
  - GO:0042864
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-7181
  - GO:0010139
  - PathBank:SMP0002038
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_PWY3O-440
  - MetaCyc:PWY-7545
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:PWY-6416
  - PathBank:SMP0002406
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:PWY-6151
  - gomodel:YeastPathways_PWY-5041
  - MetaCyc:PWY-8132
  - gomodel:YeastPathways_YEAST-RNT-SALV
  - MetaCyc:PWY0-1517
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:PWY-6419
  - gomodel:YeastPathways_PWY-5194-1
  - PathBank:SMP0002097
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - MIBiG:BGC0000852
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY0-43
  - gomodel:YeastPathways_PWY-5340
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7722
  - gomodel:YeastPathways_DETOX1-PWY
  - MetaCyc:PWY-5838
  - WikiPathways:WP296
  - gomodel:YeastPathways_PWY-6614
  - MetaCyc:PWY0-1433
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-17
  - MetaCyc:THISYN-PWY
  - MetaCyc:THIOREDOX-PWY
  - PathBank:SMP0000992
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_PWY-5123
  - MetaCyc:TRESYN-PWY
  - WikiPathways:WP266
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-4120
  - WikiPathways:WP287
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - MetaCyc:PWY-5686
  - MetaCyc:PWY0-1471
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWY-6074-1
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
  - EV-C2-PYTEST
  metrics:
  - name: mechanistic_edge_evidence_coverage
    value: 100.0
    unit: percent
    definition: Percentage of mechanistic_edges (14,393 / 14,393) carrying at least
      one valid structured evidence block.
    denominator: 14393
    minimum: 0.0
    maximum: 100.0
  - name: rhea_reaction_direction_coverage
    value: 100.0
    unit: percent
    definition: Percentage of RHEA:* reaction nodes (699 / 699) declaring an explicit
      direction enum value.
    denominator: 699
    minimum: 0.0
    maximum: 100.0
  dimensions:
  - name: evidence_tier
    value: authority_snapshot_and_cited_literature
    definition: Every mechanistic edge is backed by a verified database authority
      snapshot and/or primary literature PMID/DOI quote.
    evidence_ids:
    - EV-C2-QC-VALIDATE
    - EV-C2-CORPUS-INSPECTION
- assessment_id: ASSESS-C2-CROSS-RECORD-REACTION-CATEGORY-CONCERN-56
  area: consistency
  topic: Cross-record reaction category typing consistency and KGX node category/source_category
    export across 56 untyped MetaCyc records
  outcome: concern
  summary: 'While 212 maintained pathway records with reactions[] explicitly declare
    category on 100% of their 1,318 reaction entries (1,312 molecular_activity and
    6 pathway) and zero within-record mixed reaction lists remain after Cycle 1 Stage
    5, 56 maintained MetaCyc:* records omit category: molecular_activity across all
    279 of their reactions[] entries (263 RHEA:* and 16 MetaCyc:*). Sixteen of those
    56 records contain 28 untyped occurrences of 23 shared reaction CURIEs (22 RHEA:*
    + 1 MetaCyc:DHBAMPLIG-RXN) that explicitly declare category: molecular_activity
    in sibling records, producing mixed source_contexts in pages/downloads/nodes.tsv,
    while 231 unique reaction CURIEs appearing exclusively in those 56 records fall
    back to biolink:BiochemicalReaction with empty source_category instead of biolink:MolecularActivity
    (source_category=molecular_activity).'
  target_ids:
  - MetaCyc:PWY-6543
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY0-1312
  - MetaCyc:CALVIN-PWY
  - MetaCyc:ARO-PWY
  - MetaCyc:COA-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:P101-PWY
  - MetaCyc:RIBOSYN2-PWY
  - MetaCyc:GLUTATHIONESYN-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:CYSTSYN-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:TYRSYN
  - MetaCyc:VALSYN-PWY
  - MetaCyc:NONMEVIPP-PWY
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:OXIDATIVEPENT-PWY
  - MetaCyc:PANTO-PWY
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-6151
  - MetaCyc:TRESYN-PWY
  - MetaCyc:PWY-5686
  evidence_ids:
  - EV-C2-SHARED-REACTION-INCONSISTENCY
  - EV-C2-KGX-EXPORT
  - EV-C2-NODES-TSV
  - EV-C2-UNTYPED-56-METACYC-RECORDS
  metrics:
  - name: records_with_shared_reaction_category_inconsistency
    value: 16.0
    unit: records
    definition: 'Count of maintained MetaCyc records omitting category on reaction
      CURIEs that explicitly declare category: molecular_activity in sibling records.'
    denominator: 271
    minimum: 0.0
    maximum: 271.0
  - name: records_omitting_reaction_category
    value: 56.0
    unit: records
    definition: 'Count of maintained pathway records where reactions[] entries omit
      explicit category: molecular_activity.'
    denominator: 271
    minimum: 0.0
    maximum: 271.0
  - name: reactions_missing_explicit_category_corpus_wide
    value: 279.0
    unit: reactions
    definition: 'Count of catalytic reaction occurrences omitting category: molecular_activity
      across all 56 untyped MetaCyc records (out of 1,597 total reactions across all
      271 records).'
    denominator: 1597
    minimum: 0.0
    maximum: 1597.0
  dimensions:
  - name: kgx_export_impact
    value: 23 shared CURIEs->mixed source_contexts on biolink:MolecularActivity; 231
      unique CURIEs->biolink:BiochemicalReaction (empty source_category)
    definition: Downstream KGX node category, source_category, and source_contexts
      effect in pages/downloads/nodes.tsv.
    evidence_ids:
    - EV-C2-KGX-EXPORT
    - EV-C2-NODES-TSV
findings:
- finding_id: F-C2S4-001
  issue_key: cross-record-shared-reaction-category-inconsistency
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: 'Sixteen maintained MetaCyc pathway records omit category: molecular_activity
    on 28 occurrences of 23 reaction CURIEs that are explicitly typed in sibling records'
  description: 'Across 16 maintained MetaCyc pathway records (MetaCyc:ARABCAT-PWY,
    MetaCyc:ARGDEGRAD-PWY, MetaCyc:CALVIN-PWY, MetaCyc:DAPLYSINESYN-PWY, MetaCyc:GALACTUROCAT-PWY,
    MetaCyc:GLUAMCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:GLUTATHIONESYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY,
    MetaCyc:HOMOSERSYN-PWY, MetaCyc:NONMEVIPP-PWY, MetaCyc:NONOXIPENT-PWY, MetaCyc:OXIDATIVEPENT-PWY,
    MetaCyc:P101-PWY, MetaCyc:PWY-8383, and MetaCyc:PYRIDOXSYN-PWY), 28 reaction entries
    spanning 23 shared catalytic reaction CURIEs (MetaCyc:DHBAMPLIG-RXN, RHEA:10509,
    RHEA:10841, RHEA:12173, RHEA:12557, RHEA:12606, RHEA:13286, RHEA:13679, RHEA:13986,
    RHEA:14659, RHEA:15650, RHEA:15763, RHEA:17090, RHEA:17462, RHEA:22369, RHEA:22937,
    RHEA:23777, RHEA:24286, RHEA:27378, RHEA:27628, RHEA:30168, RHEA:30757, and RHEA:34172)
    omit category: molecular_activity even though those exact same 23 reaction CURIEs
    explicitly declare category: molecular_activity in sibling maintained pathway
    records (PathBank:SMP0000992, PathBank:SMP0002406, KEGG:M00008, MetaCyc:CYANCAT-PWY,
    MetaCyc:GALACTARDEG-PWY, MetaCyc:GLCMANNANAUT-PWY, MetaCyc:LYXMET-PWY, MetaCyc:PWY-5903,
    MetaCyc:PWY-7255, MetaCyc:PWY0-1300, MetaCyc:PWY0-1471, MetaCyc:PWY0-301, MetaCyc:PWY0-41,
    and MetaCyc:THISYN-PWY). In pages/downloads/nodes.tsv, _add_node in src/pathwaymech/kgx.py
    promotes each of these 23 deduplicated nodes to biolink:MolecularActivity (source_category=''molecular_activity'')
    while serializing mixed reaction contexts (with and without ''category'': ''molecular_activity'')
    inside source_contexts.'
  target_ids:
  - MetaCyc:CALVIN-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:P101-PWY
  - MetaCyc:GLUTATHIONESYN-PWY
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:NONMEVIPP-PWY
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:OXIDATIVEPENT-PWY
  - MetaCyc:PYRIDOXSYN-PWY
  field_paths:
  - data/pathways/calvin-cycle.yaml#reactions[2].category (RHEA:13679)
  - data/pathways/calvin-cycle.yaml#reactions[3].category (RHEA:17462)
  - data/pathways/calvin-cycle.yaml#reactions[4].category (RHEA:27628)
  - data/pathways/calvin-cycle.yaml#reactions[5].category (RHEA:10509)
  - data/pathways/calvin-cycle.yaml#reactions[7].category (RHEA:30168)
  - data/pathways/d-galacturonate-degradation-i.yaml#reactions[2].category (RHEA:17090)
  - data/pathways/d-glucarate-degradation-i.yaml#reactions[3].category (RHEA:27378)
  - data/pathways/ectoine-biosynthesis.yaml#reactions[0].category (RHEA:23777)
  - data/pathways/ectoine-biosynthesis.yaml#reactions[1].category (RHEA:24286)
  - data/pathways/glutathione-biosynthesis.yaml#reactions[0].category (RHEA:13286)
  - data/pathways/l-arabinose-degradation-i.yaml#reactions[2].category (RHEA:22369)
  - data/pathways/l-arginine-degradation-v.yaml#reactions[2].category (RHEA:30757)
  - data/pathways/l-arginine-degradation-v.yaml#reactions[3].category (RHEA:15650)
  - data/pathways/l-homoserine-biosynthesis.yaml#reactions[0].category (RHEA:23777)
  - data/pathways/l-homoserine-biosynthesis.yaml#reactions[1].category (RHEA:24286)
  - data/pathways/l-homoserine-biosynthesis.yaml#reactions[2].category (RHEA:15763)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[0].category (RHEA:23777)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[1].category (RHEA:24286)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[2].category (RHEA:34172)
  - data/pathways/l-threonine-biosynthesis.yaml#reactions[0].category (RHEA:13986)
  - data/pathways/l-threonine-biosynthesis.yaml#reactions[1].category (RHEA:10841)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[0].category
    (RHEA:12606)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[0].category (MetaCyc:DHBAMPLIG-RXN)
  - data/pathways/n-acetylglucosamine-degradation-i.yaml#reactions[0].category (RHEA:22937)
  - data/pathways/n-acetylglucosamine-degradation-i.yaml#reactions[1].category (RHEA:12173)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#reactions[0].category
    (RHEA:14659)
  - data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml#reactions[1].category
    (RHEA:12557)
  - data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml#reactions[4].category
    (RHEA:12606)
  evidence_ids:
  - EV-C2-SHARED-REACTION-INCONSISTENCY
  - EV-C2-KGX-EXPORT
  - EV-C2-NODES-TSV
  rule_id: CAUSAL_GRAPHS:cross-record-reaction-category-consistency
  native_severity: minor
  normalization_reason: 'Native minor cross-record consistency defect maps directly
    to minor severity: reaction identities, directions, and edge evidence are valid,
    while adding category: molecular_activity harmonizes shared reaction node contexts
    across sibling records.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/calvin-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galacturonate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-glucarate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ectoine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutathione-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arabinose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-v.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-homoserine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-lysine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-threonine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylerythritol-phosphate-pathway-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
  tags:
  - cycle2-stage4-record-review
  - reaction-category
  - cross-record-consistency
- finding_id: F-C2S4-002
  issue_key: corpus-wide-untyped-reactions-in-56-metacyc-records
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: 'Fifty-six maintained MetaCyc pathway records omit explicit category: molecular_activity
    across all 279 reactions[] entries'
  description: 'Across 56 maintained MetaCyc pathway records (the 16 records in F-C2S4-001
    plus 40 additional MetaCyc:* records), all 279 catalytic reaction entries in reactions[]
    (263 RHEA:* and 16 MetaCyc:*, spanning 254 unique reaction CURIEs) omit explicit
    category: molecular_activity, whereas all 212 other maintained pathway records
    with reactions[] (86 gomodel:*, 84 MetaCyc:*, 12 WikiPathways:*, 11 PathBank:*,
    10 GO:*, 6 Reactome:*, 3 KEGG:*) explicitly declare category on 100% of their
    1,318 reaction entries (1,312 molecular_activity and 6 pathway). Because 231 unique
    reaction CURIEs (216 RHEA:* and 15 MetaCyc:*) appear exclusively in these 56 records,
    src/pathwaymech/kgx.py exports them in pages/downloads/nodes.tsv via _PREFIX_CATEGORIES
    fallback as biolink:BiochemicalReaction with an empty source_category ('''') instead
    of biolink:MolecularActivity with source_category=''molecular_activity''.'
  target_ids:
  - MetaCyc:PWY-6543
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY0-1312
  - MetaCyc:CALVIN-PWY
  - MetaCyc:ARO-PWY
  - MetaCyc:COA-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:P101-PWY
  - MetaCyc:RIBOSYN2-PWY
  - MetaCyc:GLUTATHIONESYN-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:CYSTSYN-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:TYRSYN
  - MetaCyc:VALSYN-PWY
  - MetaCyc:NONMEVIPP-PWY
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:OXIDATIVEPENT-PWY
  - MetaCyc:PANTO-PWY
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-6151
  - MetaCyc:TRESYN-PWY
  - MetaCyc:PWY-5686
  field_paths:
  - data/pathways/4-aminobenzoate-biosynthesis-i.yaml#reactions[0].category (RHEA:11673)
  - data/pathways/4-aminobenzoate-biosynthesis-i.yaml#reactions[1].category (RHEA:16202)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml#reactions[0].category
    (RHEA:14907)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml#reactions[1].category
    (RHEA:17454)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml#reactions[2].category
    (RHEA:15054)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml#reactions[3].category
    (RHEA:17130)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml#reactions[4].category
    (RHEA:23033)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml#reactions[0].category
    (RHEA:14907)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml#reactions[1].category
    (RHEA:17454)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml#reactions[2].category
    (RHEA:24830)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml#reactions[3].category
    (RHEA:17130)
  - data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml#reactions[4].category
    (RHEA:23033)
  - data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml#reactions[0].category
    (RHEA:19522)
  - data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml#reactions[1].category
    (RHEA:11354)
  - data/pathways/calvin-cycle.yaml#reactions[0].category (RHEA:14658)
  - data/pathways/calvin-cycle.yaml#reactions[1].category (RHEA:19366)
  - data/pathways/calvin-cycle.yaml#reactions[2].category (RHEA:13679)
  - data/pathways/calvin-cycle.yaml#reactions[3].category (RHEA:17462)
  - data/pathways/calvin-cycle.yaml#reactions[4].category (RHEA:27628)
  - data/pathways/calvin-cycle.yaml#reactions[5].category (RHEA:10509)
  - data/pathways/calvin-cycle.yaml#reactions[6].category (RHEA:11065)
  - data/pathways/calvin-cycle.yaml#reactions[7].category (RHEA:30168)
  - data/pathways/calvin-cycle.yaml#reactions[8].category (RHEA:14731)
  - data/pathways/calvin-cycle.yaml#reactions[9].category (RHEA:18586)
  - data/pathways/calvin-cycle.yaml#reactions[10].category (RHEA:10298)
  - data/pathways/calvin-cycle.yaml#reactions[11].category (RHEA:14802)
  - data/pathways/calvin-cycle.yaml#reactions[12].category (RHEA:23126)
  - data/pathways/chorismate-biosynthesis-i.yaml#reactions[0].category (RHEA:14718)
  - data/pathways/chorismate-biosynthesis-i.yaml#reactions[1].category (RHEA:21969)
  - data/pathways/chorismate-biosynthesis-i.yaml#reactions[2].category (RHEA:21097)
  - data/pathways/chorismate-biosynthesis-i.yaml#reactions[3].category (RHEA:17739)
  - data/pathways/chorismate-biosynthesis-i.yaml#reactions[4].category (RHEA:13122)
  - data/pathways/chorismate-biosynthesis-i.yaml#reactions[5].category (RHEA:21257)
  - data/pathways/chorismate-biosynthesis-i.yaml#reactions[6].category (RHEA:21021)
  - data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml#reactions[0].category
    (RHEA:19398)
  - data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml#reactions[1].category
    (RHEA:16794)
  - data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml#reactions[2].category
    (RHEA:19802)
  - data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml#reactions[3].category
    (RHEA:18246)
  - data/pathways/d-arabinose-degradation-i.yaml#reactions[0].category (RHEA:17602)
  - data/pathways/d-arabinose-degradation-i.yaml#reactions[1].category (RHEA:13850)
  - data/pathways/d-galacturonate-degradation-i.yaml#reactions[0].category (RHEA:15958)
  - data/pathways/d-galacturonate-degradation-i.yaml#reactions[1].category (RHEA:14798)
  - data/pathways/d-galacturonate-degradation-i.yaml#reactions[2].category (RHEA:17090)
  - data/pathways/d-galacturonate-degradation-i.yaml#reactions[3].category (RHEA:27703)
  - data/pathways/d-galacturonate-degradation-i.yaml#reactions[4].category (RHEA:17815)
  - data/pathways/d-glucarate-degradation-i.yaml#reactions[0].category (RHEA:14574)
  - data/pathways/d-glucarate-degradation-i.yaml#reactions[1].category (RHEA:18843)
  - data/pathways/d-glucarate-degradation-i.yaml#reactions[2].category (RHEA:18847)
  - data/pathways/d-glucarate-degradation-i.yaml#reactions[3].category (RHEA:27378)
  - data/pathways/d-glucarate-degradation-i.yaml#reactions[4].category (RHEA:27727)
  - data/pathways/d-xylose-degradation-i.yaml#reactions[0].category (RHEA:10965)
  - data/pathways/d-xylose-degradation-i.yaml#reactions[1].category (RHEA:22817)
  - data/pathways/ectoine-biosynthesis.yaml#reactions[0].category (RHEA:23777)
  - data/pathways/ectoine-biosynthesis.yaml#reactions[1].category (RHEA:24286)
  - data/pathways/ectoine-biosynthesis.yaml#reactions[2].category (RHEA:11162)
  - data/pathways/ectoine-biosynthesis.yaml#reactions[3].category (RHEA:16902)
  - data/pathways/ectoine-biosynthesis.yaml#reactions[4].category (RHEA:17282)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[0].category (RHEA:23705)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[1].category (RHEA:21869)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[2].category (RHEA:17847)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[3].category (RHEA:18458)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[4].category (RHEA:25198)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[5].category (RHEA:26153)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[6].category (RHEA:20773)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[7].category (RHEA:14358)
  - data/pathways/flavin-biosynthesis-i.yaml#reactions[8].category (RHEA:17238)
  - data/pathways/glutathione-biosynthesis.yaml#reactions[0].category (RHEA:13286)
  - data/pathways/glutathione-biosynthesis.yaml#reactions[1].category (RHEA:13558)
  - data/pathways/glycerol-degradation-v.yaml#reactions[0].category (RHEA:18382)
  - data/pathways/glycerol-degradation-v.yaml#reactions[1].category (RHEA:13770)
  - data/pathways/glyoxylate-cycle.yaml#reactions[0].category (RHEA:13246)
  - data/pathways/glyoxylate-cycle.yaml#reactions[1].category (RHEA:18182)
  - data/pathways/glyoxylate-cycle.yaml#reactions[2].category (RHEA:16846)
  - data/pathways/glyoxylate-cycle.yaml#reactions[3].category (RHEA:10229)
  - data/pathways/glyoxylate-cycle.yaml#reactions[4].category (RHEA:22145)
  - data/pathways/glyoxylate-cycle.yaml#reactions[5].category (RHEA:21433)
  - data/pathways/guanine-and-guanosine-salvage.yaml#reactions[0].category (RHEA:27711)
  - data/pathways/guanine-and-guanosine-salvage.yaml#reactions[1].category (RHEA:13234)
  - data/pathways/guanine-and-guanosine-salvage.yaml#reactions[2].category (RHEA:25426)
  - data/pathways/inosine-5-phosphate-biosynthesis-i.yaml#reactions[0].category (RHEA:19318)
  - data/pathways/inosine-5-phosphate-biosynthesis-i.yaml#reactions[1].category (RHEA:13194)
  - data/pathways/inosine-5-phosphate-biosynthesis-i.yaml#reactions[2].category (RHEA:22629)
  - data/pathways/inosine-5-phosphate-biosynthesis-i.yaml#reactions[3].category (RHEA:23921)
  - data/pathways/inosine-5-phosphate-biosynthesis-i.yaml#reactions[4].category (RHEA:22193)
  - data/pathways/inosine-5-phosphate-biosynthesis-i.yaml#reactions[5].category (RHEA:18447)
  - data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml#reactions[0].category (RHEA:22629)
  - data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml#reactions[1].category (RHEA:23921)
  - data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml#reactions[2].category (RHEA:22193)
  - data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml#reactions[3].category (RHEA:18447)
  - data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml#reactions[4].category (RHEA:10794)
  - data/pathways/l-arabinose-degradation-i.yaml#reactions[0].category (RHEA:22073)
  - data/pathways/l-arabinose-degradation-i.yaml#reactions[1].category (RHEA:14822)
  - data/pathways/l-arabinose-degradation-i.yaml#reactions[2].category (RHEA:22369)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[0].category (RHEA:24293)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[1].category (RHEA:14630)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[2].category (RHEA:21590)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[3].category (RHEA:18051)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[4].category (RHEA:15942)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[5].category (RHEA:19514)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[6].category (RHEA:10933)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[7].category (RHEA:24021)
  - data/pathways/l-arginine-biosynthesis-i.yaml#reactions[8].category (RHEA:18634)
  - data/pathways/l-arginine-degradation-ii-ast-pathway.yaml#reactions[0].category
    (RHEA:15186)
  - data/pathways/l-arginine-degradation-ii-ast-pathway.yaml#reactions[1].category
    (RHEA:19534)
  - data/pathways/l-arginine-degradation-ii-ast-pathway.yaml#reactions[2].category
    (RHEA:16954)
  - data/pathways/l-arginine-degradation-ii-ast-pathway.yaml#reactions[3].category
    (RHEA:10813)
  - data/pathways/l-arginine-degradation-ii-ast-pathway.yaml#reactions[4].category
    (RHEA:15170)
  - data/pathways/l-arginine-degradation-iv.yaml#reactions[0].category (RHEA:17642)
  - data/pathways/l-arginine-degradation-iv.yaml#reactions[1].category (RHEA:18038)
  - data/pathways/l-arginine-degradation-iv.yaml#reactions[2].category (RHEA:22285)
  - data/pathways/l-arginine-degradation-v.yaml#reactions[0].category (RHEA:19598)
  - data/pathways/l-arginine-degradation-v.yaml#reactions[1].category (RHEA:19515)
  - data/pathways/l-arginine-degradation-v.yaml#reactions[2].category (RHEA:30757)
  - data/pathways/l-arginine-degradation-v.yaml#reactions[3].category (RHEA:15650)
  - data/pathways/l-cysteine-biosynthesis-i.yaml#reactions[0].category (RHEA:24561)
  - data/pathways/l-cysteine-biosynthesis-i.yaml#reactions[1].category (RHEA:14830)
  - data/pathways/l-fucose-degradation-i.yaml#reactions[0].category (RHEA:12377)
  - data/pathways/l-fucose-degradation-i.yaml#reactions[1].category (RHEA:12934)
  - data/pathways/l-fucose-degradation-i.yaml#reactions[2].category (RHEA:25582)
  - data/pathways/l-fucose-degradation-i.yaml#reactions[3].category (RHEA:17234)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[0].category (RHEA:18475)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[1].category (RHEA:22829)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[2].category (RHEA:20050)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[3].category (RHEA:15470)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[4].category (RHEA:24794)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[5].category (RHEA:11041)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[6].category (RHEA:23746)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[7].category (RHEA:14466)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[8].category (RHEA:33800)
  - data/pathways/l-histidine-biosynthesis.yaml#reactions[9].category (RHEA:33804)
  - data/pathways/l-homoserine-biosynthesis.yaml#reactions[0].category (RHEA:23777)
  - data/pathways/l-homoserine-biosynthesis.yaml#reactions[1].category (RHEA:24286)
  - data/pathways/l-homoserine-biosynthesis.yaml#reactions[2].category (RHEA:15763)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#reactions[0].category
    (RHEA:27655)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#reactions[1].category
    (RHEA:13495)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#reactions[2].category
    (RHEA:27695)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#reactions[3].category
    (RHEA:24803)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#reactions[4].category
    (RHEA:40676)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#reactions[5].category
    (RHEA:39968)
  - data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml#reactions[6].category
    (RHEA:39976)
  - data/pathways/l-leucine-biosynthesis.yaml#reactions[0].category (RHEA:21525)
  - data/pathways/l-leucine-biosynthesis.yaml#reactions[1].category (RHEA:18323)
  - data/pathways/l-leucine-biosynthesis.yaml#reactions[2].category (RHEA:16295)
  - data/pathways/l-leucine-biosynthesis.yaml#reactions[3].category (RHEA:10678)
  - data/pathways/l-leucine-biosynthesis.yaml#reactions[4].category (RHEA:10893)
  - data/pathways/l-leucine-biosynthesis.yaml#reactions[5].category (RHEA:25079)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[0].category (RHEA:23777)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[1].category (RHEA:24286)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[2].category (RHEA:34172)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[3].category (RHEA:35325)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[4].category (RHEA:35333)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[5].category (RHEA:17326)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[6].category (RHEA:11962)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[7].category (RHEA:22609)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[8].category (RHEA:15394)
  - data/pathways/l-lysine-biosynthesis-i.yaml#reactions[9].category (RHEA:15102)
  - data/pathways/l-methionine-biosynthesis-i.yaml#reactions[0].category (RHEA:22009)
  - data/pathways/l-methionine-biosynthesis-i.yaml#reactions[1].category (RHEA:20398)
  - data/pathways/l-methionine-biosynthesis-i.yaml#reactions[2].category (RHEA:11173)
  - data/pathways/l-methionine-biosynthesis-i.yaml#reactions[3].category (RHEA:21197)
  - data/pathways/l-methionine-biosynthesis-i.yaml#reactions[4].category (RHEA:43021)
  - data/pathways/l-methionine-biosynthesis-i.yaml#reactions[5].category (RHEA:40668)
  - data/pathways/l-methionine-biosynthesis-i.yaml#reactions[6].category (RHEA:40672)
  - data/pathways/l-ornithine-biosynthesis-i.yaml#reactions[0].category (RHEA:24293)
  - data/pathways/l-ornithine-biosynthesis-i.yaml#reactions[1].category (RHEA:14630)
  - data/pathways/l-ornithine-biosynthesis-i.yaml#reactions[2].category (RHEA:21590)
  - data/pathways/l-ornithine-biosynthesis-i.yaml#reactions[3].category (RHEA:18051)
  - data/pathways/l-ornithine-biosynthesis-i.yaml#reactions[4].category (RHEA:15942)
  - data/pathways/l-phenylalanine-biosynthesis-i.yaml#reactions[0].category (RHEA:13898)
  - data/pathways/l-phenylalanine-biosynthesis-i.yaml#reactions[1].category (RHEA:21649)
  - data/pathways/l-phenylalanine-biosynthesis-i.yaml#reactions[2].category (RHEA:25154)
  - data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml#reactions[0].category
    (RHEA:14878)
  - data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml#reactions[1].category
    (RHEA:19543)
  - data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml#reactions[2].category
    (RHEA:28235)
  - data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml#reactions[3].category
    (RHEA:14111)
  - data/pathways/l-rhamnose-degradation-i.yaml#reactions[0].category (MetaCyc:RXN-15356)
  - data/pathways/l-rhamnose-degradation-i.yaml#reactions[1].category (RHEA:20118)
  - data/pathways/l-rhamnose-degradation-i.yaml#reactions[2].category (RHEA:25585)
  - data/pathways/l-rhamnose-degradation-i.yaml#reactions[3].category (RHEA:23161)
  - data/pathways/l-rhamnose-degradation-i.yaml#reactions[4].category (RHEA:19690)
  - data/pathways/l-serine-biosynthesis-i.yaml#reactions[0].category (RHEA:12642)
  - data/pathways/l-serine-biosynthesis-i.yaml#reactions[1].category (RHEA:14331)
  - data/pathways/l-serine-biosynthesis-i.yaml#reactions[2].category (RHEA:21209)
  - data/pathways/l-threonine-biosynthesis.yaml#reactions[0].category (RHEA:13986)
  - data/pathways/l-threonine-biosynthesis.yaml#reactions[1].category (RHEA:10841)
  - data/pathways/l-tryptophan-biosynthesis.yaml#reactions[0].category (RHEA:21733)
  - data/pathways/l-tryptophan-biosynthesis.yaml#reactions[1].category (RHEA:11770)
  - data/pathways/l-tryptophan-biosynthesis.yaml#reactions[2].category (RHEA:21541)
  - data/pathways/l-tryptophan-biosynthesis.yaml#reactions[3].category (RHEA:23477)
  - data/pathways/l-tryptophan-biosynthesis.yaml#reactions[4].category (RHEA:14082)
  - data/pathways/l-tryptophan-biosynthesis.yaml#reactions[5].category (RHEA:26435)
  - data/pathways/l-tyrosine-biosynthesis-i.yaml#reactions[0].category (RHEA:13898)
  - data/pathways/l-tyrosine-biosynthesis-i.yaml#reactions[1].category (RHEA:13870)
  - data/pathways/l-tyrosine-biosynthesis-i.yaml#reactions[2].category (RHEA:15095)
  - data/pathways/l-valine-biosynthesis.yaml#reactions[0].category (RHEA:25250)
  - data/pathways/l-valine-biosynthesis.yaml#reactions[1].category (RHEA:22070)
  - data/pathways/l-valine-biosynthesis.yaml#reactions[2].category (RHEA:24810)
  - data/pathways/l-valine-biosynthesis.yaml#reactions[3].category (RHEA:24815)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[0].category
    (RHEA:12606)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[1].category
    (RHEA:13719)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[2].category
    (RHEA:13430)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[3].category
    (RHEA:18438)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[4].category
    (RHEA:23865)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[5].category
    (RHEA:43606)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[6].category
    (RHEA:24490)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[7].category
    (RHEA:24827)
  - data/pathways/methylerythritol-phosphate-pathway-i.yaml#reactions[8].category
    (RHEA:23285)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[0].category (MetaCyc:DHBAMPLIG-RXN)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[1].category (MetaCyc:RXN-23310)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[2].category (MetaCyc:RXN-22679)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[3].category (MetaCyc:RXN-23308)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[4].category (MetaCyc:RXN-23316)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[5].category (MetaCyc:RXN-23312)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[6].category (MetaCyc:RXN-23313)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[7].category (MetaCyc:RXN-23314)
  - data/pathways/myxochelin-a-and-b-biosynthesis.yaml#reactions[8].category (MetaCyc:RXN-23315)
  - data/pathways/n-acetylglucosamine-degradation-i.yaml#reactions[0].category (RHEA:22937)
  - data/pathways/n-acetylglucosamine-degradation-i.yaml#reactions[1].category (RHEA:12173)
  - data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml#reactions[0].category
    (RHEA:25877)
  - data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml#reactions[1].category
    (RHEA:25889)
  - data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml#reactions[2].category
    (RHEA:12735)
  - data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml#reactions[3].category
    (RHEA:22861)
  - data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml#reactions[4].category
    (RHEA:21189)
  - data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml#reactions[5].category
    (RHEA:24385)
  - data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml#reactions[0].category (RHEA:11801)
  - data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml#reactions[1].category (RHEA:23141)
  - data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml#reactions[2].category (RHEA:14546)
  - data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml#reactions[3].category (RHEA:36164)
  - data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml#reactions[4].category (RHEA:22861)
  - data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml#reactions[5].category (RHEA:24385)
  - data/pathways/nitrate-reduction-i-denitrification.yaml#reactions[0].category (MetaCyc:RXN-11236)
  - data/pathways/nitrate-reduction-i-denitrification.yaml#reactions[1].category (MetaCyc:TRANS-RXN0-239)
  - data/pathways/nitrate-reduction-i-denitrification.yaml#reactions[2].category (MetaCyc:RXN-15838)
  - data/pathways/nitrate-reduction-i-denitrification.yaml#reactions[3].category (MetaCyc:NITRIC-OXIDE-REDUCTASE-RXN)
  - data/pathways/nitrate-reduction-i-denitrification.yaml#reactions[4].category (MetaCyc:RXN-12130)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#reactions[0].category
    (RHEA:14659)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#reactions[1].category
    (RHEA:13678)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#reactions[2].category
    (RHEA:10510)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#reactions[3].category
    (RHEA:17054)
  - data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml#reactions[4].category
    (RHEA:27627)
  - data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml#reactions[0].category
    (RHEA:15842)
  - data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml#reactions[1].category
    (RHEA:12557)
  - data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml#reactions[2].category
    (RHEA:10117)
  - data/pathways/phosphopantothenate-biosynthesis-i.yaml#reactions[0].category (RHEA:11825)
  - data/pathways/phosphopantothenate-biosynthesis-i.yaml#reactions[1].category (RHEA:16235)
  - data/pathways/phosphopantothenate-biosynthesis-i.yaml#reactions[2].category (RHEA:10913)
  - data/pathways/phosphopantothenate-biosynthesis-i.yaml#reactions[3].category (RHEA:16374)
  - data/pathways/ppgpp-metabolism.yaml#reactions[0].category (RHEA:27687)
  - data/pathways/ppgpp-metabolism.yaml#reactions[1].category (RHEA:33056)
  - data/pathways/ppgpp-metabolism.yaml#reactions[2].category (RHEA:28099)
  - data/pathways/ppgpp-metabolism.yaml#reactions[3].category (RHEA:22089)
  - data/pathways/ppgpp-metabolism.yaml#reactions[4].category (RHEA:14254)
  - data/pathways/ppgpp-metabolism.yaml#reactions[5].category (RHEA:13074)
  - data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml#reactions[0].category
    (RHEA:12057)
  - data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml#reactions[1].category
    (RHEA:18830)
  - data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml#reactions[2].category
    (RHEA:16575)
  - data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml#reactions[3].category
    (RHEA:32276)
  - data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml#reactions[4].category
    (RHEA:12606)
  - data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml#reactions[5].category
    (RHEA:15266)
  - data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml#reactions[6].category
    (RHEA:15150)
  - data/pathways/pyridoxal-5-phosphate-salvage-i.yaml#reactions[0].category (RHEA:10225)
  - data/pathways/pyridoxal-5-phosphate-salvage-i.yaml#reactions[1].category (RHEA:25105)
  - data/pathways/pyridoxal-5-phosphate-salvage-i.yaml#reactions[2].category (RHEA:15818)
  - data/pathways/pyridoxal-5-phosphate-salvage-i.yaml#reactions[3].category (RHEA:25109)
  - data/pathways/pyridoxal-5-phosphate-salvage-i.yaml#reactions[4].category (RHEA:15150)
  - data/pathways/s-adenosyl-l-methionine-cycle-i.yaml#reactions[0].category (RHEA:21081)
  - data/pathways/s-adenosyl-l-methionine-cycle-i.yaml#reactions[1].category (MetaCyc:RXN-7605)
  - data/pathways/s-adenosyl-l-methionine-cycle-i.yaml#reactions[2].category (RHEA:17806)
  - data/pathways/s-adenosyl-l-methionine-cycle-i.yaml#reactions[3].category (RHEA:17754)
  - data/pathways/s-adenosyl-l-methionine-cycle-i.yaml#reactions[4].category (RHEA:21197)
  - data/pathways/s-adenosyl-l-methionine-cycle-i.yaml#reactions[5].category (RHEA:11173)
  - data/pathways/trehalose-biosynthesis-i.yaml#reactions[0].category (RHEA:18890)
  - data/pathways/trehalose-biosynthesis-i.yaml#reactions[1].category (RHEA:23421)
  - data/pathways/ump-biosynthesis-i.yaml#reactions[0].category (RHEA:18634)
  - data/pathways/ump-biosynthesis-i.yaml#reactions[1].category (RHEA:20014)
  - data/pathways/ump-biosynthesis-i.yaml#reactions[2].category (RHEA:24298)
  - data/pathways/ump-biosynthesis-i.yaml#reactions[3].category (RHEA:30188)
  - data/pathways/ump-biosynthesis-i.yaml#reactions[4].category (RHEA:10382)
  - data/pathways/ump-biosynthesis-i.yaml#reactions[5].category (RHEA:11597)
  evidence_ids:
  - EV-C2-UNTYPED-56-METACYC-RECORDS
  - EV-C2-SHARED-REACTION-INCONSISTENCY
  - EV-C2-KGX-EXPORT
  - EV-C2-NODES-TSV
  rule_id: CAUSAL_GRAPHS:corpus-wide-reaction-category-typing
  native_severity: minor
  normalization_reason: 'Native minor representation defect maps directly to minor
    severity: prefix fallback in kgx.py keeps the 231 unique reaction CURIEs valid,
    but adding explicit category: molecular_activity across all 279 reactions in these
    56 MetaCyc records brings 100% of the 271-record corpus (1,597 reactions) to explicit
    category typing and uniform biolink:MolecularActivity KGX export.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/4-aminobenzoate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/calvin-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/chorismate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-arabinose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galacturonate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-glucarate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-xylose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ectoine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/flavin-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutathione-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycerol-degradation-v.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/guanine-and-guanosine-salvage.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inosine-5-phosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arabinose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-ii-ast-pathway.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-iv.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-v.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-cysteine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-fucose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-histidine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-homoserine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-leucine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-lysine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-methionine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-ornithine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-phenylalanine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-rhamnose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-serine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-threonine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tryptophan-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tyrosine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-valine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylerythritol-phosphate-pathway-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nitrate-reduction-i-denitrification.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phosphopantothenate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ppgpp-metabolism.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyridoxal-5-phosphate-salvage-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/s-adenosyl-l-methionine-cycle-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/trehalose-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ump-biosynthesis-i.yaml
    role: maintained pathway YAML
  tags:
  - cycle2-stage4-record-review
  - reaction-category
  - kgx-export
  - consistency
actions:
- action_id: A-C2S4-001
  description: 'Add explicit category: molecular_activity to all 28 untyped occurrences
    of the 23 shared catalytic reaction CURIEs across the 16 affected MetaCyc pathway
    records so shared reaction nodes carry uniform category declarations across all
    records in source_contexts.'
  finding_ids:
  - F-C2S4-001
  target_ids:
  - MetaCyc:CALVIN-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:P101-PWY
  - MetaCyc:GLUTATHIONESYN-PWY
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:NONMEVIPP-PWY
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:OXIDATIVEPENT-PWY
  - MetaCyc:PYRIDOXSYN-PWY
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/calvin-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galacturonate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-glucarate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ectoine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutathione-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arabinose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-v.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-homoserine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-lysine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-threonine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylerythritol-phosphate-pathway-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
  acceptance_checks:
  - 'All 23 shared reaction CURIEs declare category: molecular_activity in every maintained
    record where they appear.'
  - Zero reaction nodes in pages/downloads/nodes.tsv have mixed typed and untyped
    reaction entries in source_contexts.
  - .venv/bin/pathwaymech-run-qc and .venv/bin/pytest -q exit 0.
- action_id: A-C2S4-002
  description: 'Add explicit category: molecular_activity to all 279 catalytic reaction
    entries (263 RHEA:* and 16 MetaCyc:*) across all 56 untyped MetaCyc pathway records,
    record curation history entries under history/records/<slug>/, and regenerate
    pages/ so 100% of catalytic reactions across all 271 maintained records declare
    category: molecular_activity and export as biolink:MolecularActivity with source_category=molecular_activity
    in pages/downloads/nodes.tsv.'
  finding_ids:
  - F-C2S4-001
  - F-C2S4-002
  target_ids:
  - MetaCyc:PWY-6543
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY0-1312
  - MetaCyc:CALVIN-PWY
  - MetaCyc:ARO-PWY
  - MetaCyc:COA-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:XYLCAT-PWY
  - MetaCyc:P101-PWY
  - MetaCyc:RIBOSYN2-PWY
  - MetaCyc:GLUTATHIONESYN-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:PWY-6579
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGSYN-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:CYSTSYN-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:HISTSYN-PWY
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PROSYN-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:TYRSYN
  - MetaCyc:VALSYN-PWY
  - MetaCyc:NONMEVIPP-PWY
  - MetaCyc:PWY-8383
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:PYRIDNUCSAL-PWY
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:OXIDATIVEPENT-PWY
  - MetaCyc:PANTO-PWY
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PWY-6151
  - MetaCyc:TRESYN-PWY
  - MetaCyc:PWY-5686
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/4-aminobenzoate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/calvin-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/chorismate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-arabinose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-galacturonate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-glucarate-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/d-xylose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ectoine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/flavin-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glutathione-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glycerol-degradation-v.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/guanine-and-guanosine-salvage.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inosine-5-phosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arabinose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-ii-ast-pathway.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-iv.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-arginine-degradation-v.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-cysteine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-fucose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-histidine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-homoserine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-leucine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-lysine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-methionine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-ornithine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-phenylalanine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-rhamnose-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-serine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-threonine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tryptophan-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-tyrosine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-valine-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/methylerythritol-phosphate-pathway-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nitrate-reduction-i-denitrification.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/phosphopantothenate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ppgpp-metabolism.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pyridoxal-5-phosphate-salvage-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/s-adenosyl-l-methionine-cycle-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/trehalose-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ump-biosynthesis-i.yaml
    role: maintained pathway YAML
  acceptance_checks:
  - Zero maintained records in data/pathways/*.yaml omit category on any reactions[]
    entry (1,591 molecular_activity + 6 pathway = 1,597/1,597 explicitly typed).
  - All 56 updated pathway records have matching history/records/<slug>/*.yaml provenance
    files.
  - .venv/bin/pathwaymech-run-qc, .venv/bin/pytest -q, and .venv/bin/python scripts/record_review.py
    check exit 0.
  depends_on:
  - A-C2S4-001
boundary_decisions:
- action: retain
  target_ids:
  - GO:0010139
  - GO:0019270
  - GO:0019305
  - GO:0019618
  - GO:0036040
  - GO:0042864
  - GO:0043427
  - GO:0097288
  - GO:1901281
  - GO:1902000
  rationale: Retain all 10 maintained GO:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against GO authority snapshots and
    docs/HARMONIZATION.md.
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
- action: retain
  target_ids:
  - KEGG:M00008
  - KEGG:M00373
  - KEGG:M00374
  rationale: Retain all 3 maintained KEGG:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against KEGG authority snapshots and
    docs/HARMONIZATION.md.
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
- action: retain
  target_ids:
  - MIBiG:BGC0000829
  - MIBiG:BGC0000852
  - MIBiG:BGC0002072
  rationale: Retain all 3 maintained MIBiG:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against MIBiG authority snapshots and
    docs/HARMONIZATION.md.
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
- action: retain
  target_ids:
  - MetaCyc:2PHENDEG-PWY
  - MetaCyc:ACETOACETATE-DEG-PWY
  - MetaCyc:ARABCAT-PWY
  - MetaCyc:ARGDEG-III-PWY
  - MetaCyc:ARGDEGRAD-PWY
  - MetaCyc:ARGSYN-PWY
  - MetaCyc:ARO-PWY
  - MetaCyc:AST-PWY
  - MetaCyc:BIOTIN-BIOSYNTHESIS-PWY
  - MetaCyc:CALVIN-PWY
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  - MetaCyc:CENTBENZCOA-PWY
  - MetaCyc:COA-PWY
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:CYSTSYN-PWY
  - MetaCyc:DAPLYSINESYN-PWY
  - MetaCyc:DARABCAT-PWY
  - MetaCyc:DENITRIFICATION-PWY
  - MetaCyc:FUCCAT-PWY
  - MetaCyc:GALACTARDEG-PWY
  - MetaCyc:GALACTCAT-PWY
  - MetaCyc:GALACTUROCAT-PWY
  - MetaCyc:GALLATE-DEGRADATION-I-PWY
  - MetaCyc:GALLATE-DEGRADATION-II-PWY
  - MetaCyc:GLCMANNANAUT-PWY
  - MetaCyc:GLUAMCAT-PWY
  - MetaCyc:GLUCARDEG-PWY
  - MetaCyc:GLUTATHIONESYN-PWY
  - MetaCyc:GLUTORN-PWY
  - MetaCyc:GLYCEROLMETAB-PWY
  - MetaCyc:GLYOXYLATE-BYPASS
  - MetaCyc:HISTSYN-PWY
  - MetaCyc:HOMOSER-METSYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:ILEUSYN-PWY
  - MetaCyc:LEUSYN-PWY
  - MetaCyc:LYXMET-PWY
  - MetaCyc:METH-ACETATE-PWY
  - MetaCyc:METHANOGENESIS-PWY
  - MetaCyc:NADPHOS-DEPHOS-PWY
  - MetaCyc:NONMEVIPP-PWY
  - MetaCyc:NONOXIPENT-PWY
  - MetaCyc:OXIDATIVEPENT-PWY
  - MetaCyc:P101-PWY
  - MetaCyc:P121-PWY
  - MetaCyc:P184-PWY
  - MetaCyc:P2-PWY
  - MetaCyc:P321-PWY
  - MetaCyc:PANTO-PWY
  - MetaCyc:PHESYN
  - MetaCyc:PLPSAL-PWY
  - MetaCyc:PPGPPMET-PWY
  - MetaCyc:PROSYN-PWY
  - MetaCyc:PWY-1361
  - MetaCyc:PWY-2361
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-5177
  - MetaCyc:PWY-5386
  - MetaCyc:PWY-5415
  - MetaCyc:PWY-5417
  - MetaCyc:PWY-5420
  - MetaCyc:PWY-5453
  - MetaCyc:PWY-5509
  - MetaCyc:PWY-5686
  - MetaCyc:PWY-5705
  - MetaCyc:PWY-5744
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-5838
  - MetaCyc:PWY-5901
  - MetaCyc:PWY-5903
  - MetaCyc:PWY-6019
  - MetaCyc:PWY-6048
  - MetaCyc:PWY-6121
  - MetaCyc:PWY-6122
  - MetaCyc:PWY-6123
  - MetaCyc:PWY-6124
  - MetaCyc:PWY-6151
  - MetaCyc:PWY-6223
  - MetaCyc:PWY-6289
  - MetaCyc:PWY-6336
  - MetaCyc:PWY-6376
  - MetaCyc:PWY-6416
  - MetaCyc:PWY-6419
  - MetaCyc:PWY-6534
  - MetaCyc:PWY-6543
  - MetaCyc:PWY-6579
  - MetaCyc:PWY-6609
  - MetaCyc:PWY-6823
  - MetaCyc:PWY-6993
  - MetaCyc:PWY-7181
  - MetaCyc:PWY-7255
  - MetaCyc:PWY-7446
  - MetaCyc:PWY-7545
  - MetaCyc:PWY-7722
  - MetaCyc:PWY-7971
  - MetaCyc:PWY-7990
  - MetaCyc:PWY-8008
  - MetaCyc:PWY-8130
  - MetaCyc:PWY-8131
  - MetaCyc:PWY-8132
  - MetaCyc:PWY-8178
  - MetaCyc:PWY-8383
  - MetaCyc:PWY0-1241
  - MetaCyc:PWY0-1277
  - MetaCyc:PWY0-1280
  - MetaCyc:PWY0-1300
  - MetaCyc:PWY0-1312
  - MetaCyc:PWY0-1338
  - MetaCyc:PWY0-1352
  - MetaCyc:PWY0-1433
  - MetaCyc:PWY0-1471
  - MetaCyc:PWY0-1477
  - MetaCyc:PWY0-1517
  - MetaCyc:PWY0-301
  - MetaCyc:PWY0-321
  - MetaCyc:PWY0-41
  - MetaCyc:PWY0-42
  - MetaCyc:PWY0-43
  - MetaCyc:PWY0-501
  - MetaCyc:PWY0-521
  - MetaCyc:PWY1-3
  - MetaCyc:PYRIDNUCSAL-PWY
  - MetaCyc:PYRIDNUCSYN-PWY
  - MetaCyc:PYRIDOXSYN-PWY
  - MetaCyc:QUINATEDEG-PWY
  - MetaCyc:RHAMCAT-PWY
  - MetaCyc:RIBOKIN-PWY
  - MetaCyc:RIBOSYN2-PWY
  - MetaCyc:SALVADEHYPOX-PWY
  - MetaCyc:SERSYN-PWY
  - MetaCyc:SHIKIMATEDEG-PWY
  - MetaCyc:THIOREDOX-PWY
  - MetaCyc:THISYN-PWY
  - MetaCyc:THRDLCTCAT-PWY
  - MetaCyc:TRESYN-PWY
  - MetaCyc:TRPSYN-PWY
  - MetaCyc:TYRSYN
  - MetaCyc:VALSYN-PWY
  - MetaCyc:XYLCAT-PWY
  rationale: Retain all 140 maintained MetaCyc:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against MetaCyc authority snapshots
    and docs/HARMONIZATION.md.
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
- action: retain
  target_ids:
  - PathBank:SMP0000992
  - PathBank:SMP0002038
  - PathBank:SMP0002051
  - PathBank:SMP0002067
  - PathBank:SMP0002077
  - PathBank:SMP0002081
  - PathBank:SMP0002083
  - PathBank:SMP0002089
  - PathBank:SMP0002097
  - PathBank:SMP0002123
  - PathBank:SMP0002406
  rationale: Retain all 11 maintained PathBank:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against PathBank authority snapshots
    and docs/HARMONIZATION.md.
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
- action: retain
  target_ids:
  - Reactome:R-MTU-868688
  - Reactome:R-MTU-879299
  - Reactome:R-MTU-879325
  - Reactome:R-MTU-936635
  - Reactome:R-MTU-936654
  - Reactome:R-MTU-936721
  rationale: Retain all 6 maintained Reactome:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against Reactome authority snapshots
    and docs/HARMONIZATION.md.
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
- action: retain
  target_ids:
  - WikiPathways:WP171
  - WikiPathways:WP178
  - WikiPathways:WP266
  - WikiPathways:WP287
  - WikiPathways:WP296
  - WikiPathways:WP392
  - WikiPathways:WP478
  - WikiPathways:WP5019
  - WikiPathways:WP5060
  - WikiPathways:WP556
  - WikiPathways:WP5587
  - WikiPathways:WP71
  rationale: Retain all 12 maintained WikiPathways:* pathway records as distinct,
    non-duplicate source-scoped pathway definitions verified against WikiPathways
    authority snapshots and docs/HARMONIZATION.md.
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
- action: retain
  target_ids:
  - gomodel:6882d2b800000609
  - gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY
  - gomodel:YeastPathways_ARGSPECAT-PWY
  - gomodel:YeastPathways_ARGSYNBSUB-PWY
  - gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1
  - gomodel:YeastPathways_ASPARAGINE-DEG2-PWY
  - gomodel:YeastPathways_ASPBIO-PWY
  - gomodel:YeastPathways_BSUBPOLYAMSYN-PWY
  - gomodel:YeastPathways_CITRUL-BIO2-PWY
  - gomodel:YeastPathways_DETOX1-PWY
  - gomodel:YeastPathways_FASYN-ELONG2-PWY
  - gomodel:YeastPathways_GLUCONEO-PWY-1
  - gomodel:YeastPathways_GLYCLEAV-PWY
  - gomodel:YeastPathways_GLYCOLYSIS
  - gomodel:YeastPathways_HEME-BIOSYNTHESIS-II
  - gomodel:YeastPathways_HEXPPSYN-PWY-2
  - gomodel:YeastPathways_HOMOCYS-CYS-CONVERT
  - gomodel:YeastPathways_HOMOCYSDEGR-PWY-1
  - gomodel:YeastPathways_IPPSYN-PWY
  - gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2
  - gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION
  - gomodel:YeastPathways_PHOSLIPSYN2-PWY-1
  - gomodel:YeastPathways_PROUT-PWY
  - gomodel:YeastPathways_PWY-1801-1
  - gomodel:YeastPathways_PWY-2301
  - gomodel:YeastPathways_PWY-5041
  - gomodel:YeastPathways_PWY-5080-1
  - gomodel:YeastPathways_PWY-5123
  - gomodel:YeastPathways_PWY-5194-1
  - gomodel:YeastPathways_PWY-5340
  - gomodel:YeastPathways_PWY-5344
  - gomodel:YeastPathways_PWY-5651
  - gomodel:YeastPathways_PWY-5653
  - gomodel:YeastPathways_PWY-5669
  - gomodel:YeastPathways_PWY-5670-1
  - gomodel:YeastPathways_PWY-5694
  - gomodel:YeastPathways_PWY-5697
  - gomodel:YeastPathways_PWY-5703
  - gomodel:YeastPathways_PWY-5760-1
  - gomodel:YeastPathways_PWY-6074-1
  - gomodel:YeastPathways_PWY-6075-1
  - gomodel:YeastPathways_PWY-6147
  - gomodel:YeastPathways_PWY-6614
  - gomodel:YeastPathways_PWY-7176
  - gomodel:YeastPathways_PWY-7219
  - gomodel:YeastPathways_PWY-7220-1
  - gomodel:YeastPathways_PWY-7221
  - gomodel:YeastPathways_PWY-901
  - gomodel:YeastPathways_PWY3O-123
  - gomodel:YeastPathways_PWY3O-15
  - gomodel:YeastPathways_PWY3O-1565
  - gomodel:YeastPathways_PWY3O-17
  - gomodel:YeastPathways_PWY3O-1743
  - gomodel:YeastPathways_PWY3O-1801
  - gomodel:YeastPathways_PWY3O-214
  - gomodel:YeastPathways_PWY3O-242
  - gomodel:YeastPathways_PWY3O-259
  - gomodel:YeastPathways_PWY3O-4
  - gomodel:YeastPathways_PWY3O-402
  - gomodel:YeastPathways_PWY3O-4105
  - gomodel:YeastPathways_PWY3O-4106
  - gomodel:YeastPathways_PWY3O-4108
  - gomodel:YeastPathways_PWY3O-4112
  - gomodel:YeastPathways_PWY3O-4120
  - gomodel:YeastPathways_PWY3O-4153
  - gomodel:YeastPathways_PWY3O-4300
  - gomodel:YeastPathways_PWY3O-440
  - gomodel:YeastPathways_PWY3O-450
  - gomodel:YeastPathways_PWY3O-48
  - gomodel:YeastPathways_PWY3O-50
  - gomodel:YeastPathways_PWY3O-5268
  - gomodel:YeastPathways_PWY3O-64
  - gomodel:YeastPathways_PWY3O-6407
  - gomodel:YeastPathways_PWY3O-6499
  - gomodel:YeastPathways_PWY3O-697
  - gomodel:YeastPathways_PWY3O-8
  - gomodel:YeastPathways_PWYQT-4432
  - gomodel:YeastPathways_PYRUVDEHYD-PWY
  - gomodel:YeastPathways_SO4ASSIM-PWY
  - gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1
  - gomodel:YeastPathways_THREOCAT2-PWY
  - gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY
  - gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY
  - gomodel:YeastPathways_YEAST-FAO-PWY
  - gomodel:YeastPathways_YEAST-GALACT-METAB-PWY
  - gomodel:YeastPathways_YEAST-RNT-SALV
  rationale: Retain all 86 maintained gomodel:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against gomodel authority snapshots
    and docs/HARMONIZATION.md.
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
- action: retain
  target_ids:
  - MetaCyc:DAPLYSINESYN-PWY
  - MetaCyc:HOMOSER-THRESYN-PWY
  - MetaCyc:HOMOSERSYN-PWY
  - MetaCyc:P101-PWY
  - PathBank:SMP0000992
  rationale: 'Retain PathBank:SMP0000992 (Threonine Biosynthesis from Aspartate in
    Escherichia coli K-12, PW000976.owl, 6 steps: 5-step L-aspartate to L-threonine
    biosynthetic sequence RHEA:23777 -> RHEA:24286 -> RHEA:15763 -> RHEA:13986 ->
    RHEA:10841 plus the L-aspartate 4-semialdehyde branch step to lysine/diaminopimelate
    biosynthesis RHEA:34172) alongside MetaCyc:HOMOSERSYN-PWY (3-step L-aspartate
    to L-homoserine module), MetaCyc:HOMOSER-THRESYN-PWY (2-step L-homoserine to L-threonine
    module), MetaCyc:DAPLYSINESYN-PWY (L-lysine biosynthesis I), and MetaCyc:P101-PWY
    (ectoine biosynthesis) as distinct authority-scoped pathway boundaries and step
    topologies per docs/HARMONIZATION.md.'
  evidence_ids:
  - EV-C2-QC-VALIDATE
  - EV-C2-CORPUS-INSPECTION
limitations:
- 'Fifty-six maintained MetaCyc pathway records omit explicit category: molecular_activity
  across all 279 of their reactions[] entries (263 RHEA:* and 16 MetaCyc:*), including
  28 occurrences across 16 MetaCyc records of 23 shared reaction CURIEs that are explicitly
  typed in sibling records; these are recorded as open minor findings F-C2S4-001 and
  F-C2S4-002 for Cycle 2 Stage 5 grouped remediation.'
- Verification of literature-backed evidence blocks relied on the repository's local
  authority snapshots and curated evidence quotes/abstracts at frozen commit e369fa425e64d4f794ce84e2fd71138a43660467
  without re-fetching external publisher full texts over the network.
notes:
- Per Cycle 2 Stage 4 (record_review) workflow policy, no edits were made to data/pathways/*.yaml
  during this stage; open findings F-C2S4-001 and F-C2S4-002 are carried forward to
  Cycle 2 Stage 5 (resolve_review_findings).
tags:
- mech-goal-sequence-20261019
- cycle-2
- stage-4
- frozen-inventory
- full-corpus-review
```
