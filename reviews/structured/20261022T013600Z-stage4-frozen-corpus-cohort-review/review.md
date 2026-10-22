# Cycle 1 Stage 4 Full Frozen-Inventory Record and Cohort Review of 270 PathwayMech Maintained Records

- Review: 20261022T013600Z-stage4-frozen-corpus-cohort-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-22T01:00:00Z
- Finished UTC: 2026-10-22T01:36:00Z
- Reviewer: Antigravity (review-yaml-record + review-yaml-category) (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Completed a full-coverage frozen-inventory scientific record and cohort review of all 270 maintained pathway YAML records in data/pathways/*.yaml at Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930 across all 8 identifier namespaces (MetaCyc: 140, gomodel: 86, WikiPathways: 12, GO: 10, PathBank: 10, Reactome: 6, KEGG: 3, MIBiG: 3; 7,652 participants, 1,591 reactions including 693 RHEA:* reactions). All 270 records pass closed LinkML schema validation, authority snapshot identifier/label checks, history validation (537 records), and edge-level evidence verification (14,322 mechanistic edges, 20,959 edge-level evidence items, 22,085 total evidence blocks). Identified 2 minor open findings (F-STAGE4-001 on MetaCyc:GLCMANNANAUT-PWY and F-STAGE4-002 across 12 MetaCyc records) concerning omitted category: molecular_activity on 33 catalytic reactions inside mixed-typing reactions[] lists, preserved unedited for Stage 5 grouped remediation.

## Scope And Provenance

Full frozen-inventory record and category review of all 270 maintained pathway records in data/pathways/*.yaml at Git base 556074d91f600aa9e5ca97e0b4baef6d99513930.

Selection: All files matching data/pathways/*.yaml in CultureBotAI/PathwayMech.
Coverage: full; 270 reviewed / 270 in the declared population.
Source: git_commit at Git base 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
| Repository QC and closed-schema validation (just validate) | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | Validated all 270 maintained pathway records against the closed LinkML schema, local identifier/label authority snapshots, 537 history records, 22,085 evidence blocks, 33 source records, and pages/ synchrony. |
| Full pytest test suite (just test) | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | All 8,045 unit, schema, KGX, SSSOM, and record-review contract tests passed (3 skipped). |
| Ruff code and script lint check (just lint) | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | Ruff lint passed with zero warnings or errors. |
| Git whitespace and conflict marker gate | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | git diff --check passed with zero issues. |
| Structured review bundle contract check (just review-check) | passed | True | MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1 | All 197 pre-existing structured review bundles in reviews/structured/ passed schema and append-only checks. |

## Scientific And Domain Assessments

### Pathway identity, taxon grounding, and authority-verified participant/reaction CURIEs across all 270 maintained records

identity: supported. Targets: MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1.

All 270 maintained pathway records in data/pathways/*.yaml denote coherent microbial pathways or signaling/virulence modules with authority-verified pathway IDs, NCBITaxon groundings, CHEBI/UniProt/ComplexPortal/GO/NCBITaxon participant CURIEs, and RHEA/MetaCyc/BiGG reaction identifiers verified against local authority snapshots.

### Causal graph connectivity, reaction directionality, and edge-level evidence across all 270 maintained records

graph: supported. Targets: MetaCyc:PWY-5901, MetaCyc:PWY0-42, WikiPathways:WP5587, MetaCyc:PWY-2361, MetaCyc:PWY-6543, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-8130, MetaCyc:PWY-8131, gomodel:YeastPathways_PWY-6147, GO:0097288, MetaCyc:PWY0-1312, MetaCyc:ACETOACETATE-DEG-PWY, WikiPathways:WP5019, PathBank:SMP0002081, MetaCyc:P121-PWY, PathBank:SMP0002083, MetaCyc:PWY-6609, gomodel:YeastPathways_PWY-7220-1, MetaCyc:SALVADEHYPOX-PWY, gomodel:YeastPathways_PWY-7219, MetaCyc:PWY-5509, MetaCyc:PWY-7971, MetaCyc:PWY0-1241, GO:0019270, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, MetaCyc:PWY0-41, gomodel:YeastPathways_PWY-5694, MetaCyc:PWY-5705, gomodel:YeastPathways_PWY-5697, MetaCyc:GLCMANNANAUT-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, MetaCyc:PWY-5903, PathBank:SMP0002123, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CENTBENZCOA-PWY, MetaCyc:P321-PWY, gomodel:YeastPathways_PWY-5760-1, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, GO:0043427, gomodel:YeastPathways_PWY3O-4, MetaCyc:PWY-5415, MetaCyc:PWY-5420, MetaCyc:PWY-5417, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, gomodel:YeastPathways_PWY3O-15, MetaCyc:ARO-PWY, MIBiG:BGC0000829, MetaCyc:P2-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, MetaCyc:COA-PWY, GO:0036040, MetaCyc:CYANCAT-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:XYLCAT-PWY, MetaCyc:PWY-6376, KEGG:M00374, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-123, GO:0019305, MetaCyc:P101-PWY, KEGG:M00008, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-6075-1, MetaCyc:PWY-7255, gomodel:YeastPathways_PWY3O-4300, MetaCyc:PWY0-1477, MetaCyc:PWY0-1280, KEGG:M00373, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, MetaCyc:RIBOSYN2-PWY, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY-1801-1, MetaCyc:PWY0-521, GO:1901281, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:PWY-6223, gomodel:YeastPathways_GLUCONEO-PWY-1, WikiPathways:WP556, MetaCyc:PWY-5177, MetaCyc:GLUTATHIONESYN-PWY, gomodel:YeastPathways_PWYQT-4432, WikiPathways:WP392, gomodel:YeastPathways_PWY3O-48, MetaCyc:GLYCEROLMETAB-PWY, gomodel:YeastPathways_GLYCLEAV-PWY, WikiPathways:WP478, gomodel:YeastPathways_GLYCOLYSIS, MetaCyc:PWY-5744, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:PWY-6579, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, GO:1902000, MetaCyc:PWY-5789, MetaCyc:PWY-6123, MetaCyc:PWY-6124, gomodel:YeastPathways_PWY3O-402, WikiPathways:WP178, MetaCyc:PWY0-1338, MetaCyc:ARABCAT-PWY, MetaCyc:ARGSYN-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, MetaCyc:AST-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:PWY0-301, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, PathBank:SMP0002051, MetaCyc:CYSTSYN-PWY, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, MetaCyc:FUCCAT-PWY, MetaCyc:HISTSYN-PWY, gomodel:YeastPathways_PWY-5344, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, MetaCyc:LYXMET-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:PHESYN, MetaCyc:PROSYN-PWY, gomodel:YeastPathways_PROUT-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:SERSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRPSYN-PWY, gomodel:YeastPathways_PWY-5651, MetaCyc:TYRSYN, gomodel:YeastPathways_PWY3O-4108, MetaCyc:VALSYN-PWY, gomodel:YeastPathways_PWY3O-4112, MIBiG:BGC0002072, gomodel:6882d2b800000609, MetaCyc:PWY0-501, gomodel:YeastPathways_PWY3O-1743, MetaCyc:PWY0-1300, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, gomodel:YeastPathways_PWY3O-64, MetaCyc:NONMEVIPP-PWY, gomodel:YeastPathways_PWY-901, MetaCyc:PWY-5386, MetaCyc:PWY-5453, PathBank:SMP0002077, MetaCyc:PWY-6048, gomodel:YeastPathways_IPPSYN-PWY, MetaCyc:PWY-6823, Reactome:R-MTU-936721, Reactome:R-MTU-936654, Reactome:R-MTU-936635, Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, gomodel:YeastPathways_PWY-2301, MetaCyc:PWY-8383, MetaCyc:GLUAMCAT-PWY, gomodel:YeastPathways_PWY-5653, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:PYRIDNUCSAL-PWY, gomodel:YeastPathways_PWY3O-4106, WikiPathways:WP171, MetaCyc:PWY-6993, MetaCyc:DENITRIFICATION-PWY, MetaCyc:PWY0-1352, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-1801, MetaCyc:NONOXIPENT-PWY, MetaCyc:PWY-8178, MetaCyc:OXIDATIVEPENT-PWY, WikiPathways:WP5060, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, MetaCyc:PWY-6289, MetaCyc:PWY0-321, gomodel:YeastPathways_PWY3O-4153, MetaCyc:2PHENDEG-PWY, MetaCyc:PWY-6534, MetaCyc:PWY0-1277, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, WikiPathways:WP71, MetaCyc:PANTO-PWY, MetaCyc:PWY1-3, MetaCyc:PPGPPMET-PWY, MetaCyc:P184-PWY, GO:0019618, MetaCyc:PWY-6336, MetaCyc:PWY-6019, PathBank:SMP0002089, PathBank:SMP0002067, GO:0042864, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:PLPSAL-PWY, MetaCyc:PWY-7181, GO:0010139, PathBank:SMP0002038, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_PWY3O-440, MetaCyc:PWY-7545, MetaCyc:QUINATEDEG-PWY, MetaCyc:PWY-6416, PathBank:SMP0002406, MetaCyc:RIBOKIN-PWY, MetaCyc:PWY-6151, gomodel:YeastPathways_PWY-5041, MetaCyc:PWY-8132, gomodel:YeastPathways_YEAST-RNT-SALV, MetaCyc:PWY0-1517, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:PWY-6419, gomodel:YeastPathways_PWY-5194-1, PathBank:SMP0002097, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, MIBiG:BGC0000852, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY0-43, gomodel:YeastPathways_PWY-5340, MetaCyc:PWY-7446, MetaCyc:PWY-7722, gomodel:YeastPathways_DETOX1-PWY, MetaCyc:PWY-5838, WikiPathways:WP296, gomodel:YeastPathways_PWY-6614, MetaCyc:PWY0-1433, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-17, MetaCyc:THISYN-PWY, MetaCyc:THIOREDOX-PWY, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_PWY-5123, MetaCyc:TRESYN-PWY, WikiPathways:WP266, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-4120, WikiPathways:WP287, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, MetaCyc:PWY-5686, MetaCyc:PWY0-1471, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWY-6074-1.

All 270 maintained records contain connected participant-reaction-edge causal graphs (7,652 participants, 1,591 reactions including 693 RHEA:* reactions, 14,322 mechanistic_edges) with 100% edge-level evidence coverage (20,959 edge-level evidence items; 22,085 total evidence blocks across records, steps, and edges), explicit direction on 100% of 693 RHEA:* reaction nodes, and zero cross-record RHEA direction conflicts.

### Within-record reaction category typing consistency and KGX node category export in 12 MetaCyc records

consistency: concern. Targets: MetaCyc:SALVADEHYPOX-PWY, MetaCyc:PWY-7971, MetaCyc:PWY0-41, MetaCyc:GLCMANNANAUT-PWY, MetaCyc:PWY-2503, MetaCyc:PWY-1361, MetaCyc:CYANCAT-PWY, MetaCyc:PWY-7255, MetaCyc:PWY-5744, MetaCyc:PWY-5789, MetaCyc:PWY-6993, MetaCyc:PWY0-1471.

Twelve maintained MetaCyc records declare explicit category (molecular_activity or pathway) on a subset of their reactions[] entries while omitting category on 33 sibling catalytic reaction entries (30 RHEA:*, 2 MetaCyc:RXN-*, 1 BiGG:ACMANAptspp). In MetaCyc:GLCMANNANAUT-PWY (data/pathways/amino-sugar-superpathway.yaml), omitting category: molecular_activity on BiGG:ACMANAptspp (reactions[13]) causes KGX export (pages/downloads/nodes.tsv) to assign fallback biolink:NamedThing with empty source_category instead of biolink:MolecularActivity.

## Findings

### F-STAGE4-001: BiGG:ACMANAptspp reaction in MetaCyc:GLCMANNANAUT-PWY omits category: molecular_activity and exports as biolink:NamedThing

minor / open / confirmed; issue key: amino-sugar-superpathway-bigg-reaction-missing-category.

In data/pathways/amino-sugar-superpathway.yaml (MetaCyc:GLCMANNANAUT-PWY, superpathway of N-acetylglucosamine, N-acetylmannosamine and N-acetylneuraminate degradation), reactions[13] is BiGG:ACMANAptspp (N-acetyl-D-mannosamine transport via PTS  (periplasm)), which omits category: molecular_activity while 3 subpathway entries (MetaCyc:PWY0-1324, MetaCyc:GLUAMCAT-PWY, MetaCyc:GLYCOLYSIS at reactions[0..2]) in the same reactions list declare category: pathway. Because 'BiGG' is not in _PREFIX_CATEGORIES in src/pathwaymech/kgx.py, BiGG:ACMANAptspp falls back to DEFAULT_CATEGORY ('biolink:NamedThing') with an empty source_category in pages/downloads/nodes.tsv instead of 'biolink:MolecularActivity' (source_category='molecular_activity').

### F-STAGE4-002: Twelve maintained MetaCyc pathway records mix explicit and omitted reaction category fields within reactions[]

minor / open / confirmed; issue key: mixed-reaction-category-typing-in-maintained-pathways.

Across 12 maintained MetaCyc pathway records (MetaCyc:CYANCAT-PWY, MetaCyc:GLCMANNANAUT-PWY, MetaCyc:PWY-1361, MetaCyc:PWY-2503, MetaCyc:PWY-5744, MetaCyc:PWY-5789, MetaCyc:PWY-6993, MetaCyc:PWY-7255, MetaCyc:PWY-7971, MetaCyc:PWY0-1471, MetaCyc:PWY0-41, and MetaCyc:SALVADEHYPOX-PWY), reactions[] declares explicit category (molecular_activity or pathway) on a subset of entries while omitting category: molecular_activity on 33 sibling catalytic reaction entries (30 RHEA:*, 2 MetaCyc:RXN-*, and 1 BiGG:ACMANAptspp). This causes catalytic reactions within the same pathway graph to export with mixed Biolink categories (biolink:MolecularActivity with source_category=molecular_activity vs biolink:BiochemicalReaction or biolink:NamedThing with empty source_category) in pages/downloads/nodes.tsv.

## Recommended Actions And Acceptance Checks

### A-STAGE4-001

Add category: molecular_activity to reactions[13] (BiGG:ACMANAptspp) in data/pathways/amino-sugar-superpathway.yaml (MetaCyc:GLCMANNANAUT-PWY), record a curation history entry under history/records/amino-sugar-superpathway/, and regenerate pages/ so BiGG:ACMANAptspp exports as biolink:MolecularActivity in pages/downloads/nodes.tsv.

- data/pathways/amino-sugar-superpathway.yaml declares category: molecular_activity on BiGG:ACMANAptspp.
- pages/downloads/nodes.tsv lists biolink:MolecularActivity and source_category=molecular_activity for BiGG:ACMANAptspp.
- .venv/bin/pathwaymech-run-qc and .venv/bin/pytest -q exit 0.

### A-STAGE4-002

Add explicit category: molecular_activity to all 33 catalytic reaction entries (30 RHEA:*, 2 MetaCyc:RXN-*, 1 BiGG:ACMANAptspp) that currently omit category across the 12 mixed-typing MetaCyc pathway records, record curation history entries under history/records/, and regenerate pages/ artifacts.

- Zero maintained records in data/pathways/*.yaml mix catalytic reactions with and without category: molecular_activity.
- All 12 updated pathway records have matching history/records/&lt;slug&gt;/*.yaml provenance files.
- .venv/bin/pathwaymech-run-qc, .venv/bin/pytest -q, and .venv/bin/python scripts/record_review.py check exit 0.

## Category Boundaries

- retain: GO:0010139, GO:0019270, GO:0019305, GO:0019618, GO:0036040, GO:0042864, GO:0043427, GO:0097288, GO:1901281, GO:1902000. Retain all 10 maintained GO:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against GO authority snapshots and docs/HARMONIZATION.md.
- retain: KEGG:M00008, KEGG:M00373, KEGG:M00374. Retain all 3 maintained KEGG:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against KEGG authority snapshots and docs/HARMONIZATION.md.
- retain: MIBiG:BGC0000829, MIBiG:BGC0000852, MIBiG:BGC0002072. Retain all 3 maintained MIBiG:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against MIBiG authority snapshots and docs/HARMONIZATION.md.
- retain: MetaCyc:2PHENDEG-PWY, MetaCyc:ACETOACETATE-DEG-PWY, MetaCyc:ARABCAT-PWY, MetaCyc:ARGDEG-III-PWY, MetaCyc:ARGDEGRAD-PWY, MetaCyc:ARGSYN-PWY, MetaCyc:ARO-PWY, MetaCyc:AST-PWY, MetaCyc:BIOTIN-BIOSYNTHESIS-PWY, MetaCyc:CALVIN-PWY, MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY, MetaCyc:CENTBENZCOA-PWY, MetaCyc:COA-PWY, MetaCyc:CYANCAT-PWY, MetaCyc:CYSTSYN-PWY, MetaCyc:DAPLYSINESYN-PWY, MetaCyc:DARABCAT-PWY, MetaCyc:DENITRIFICATION-PWY, MetaCyc:FUCCAT-PWY, MetaCyc:GALACTARDEG-PWY, MetaCyc:GALACTCAT-PWY, MetaCyc:GALACTUROCAT-PWY, MetaCyc:GALLATE-DEGRADATION-I-PWY, MetaCyc:GALLATE-DEGRADATION-II-PWY, MetaCyc:GLCMANNANAUT-PWY, MetaCyc:GLUAMCAT-PWY, MetaCyc:GLUCARDEG-PWY, MetaCyc:GLUTATHIONESYN-PWY, MetaCyc:GLUTORN-PWY, MetaCyc:GLYCEROLMETAB-PWY, MetaCyc:GLYOXYLATE-BYPASS, MetaCyc:HISTSYN-PWY, MetaCyc:HOMOSER-METSYN-PWY, MetaCyc:HOMOSER-THRESYN-PWY, MetaCyc:HOMOSERSYN-PWY, MetaCyc:ILEUSYN-PWY, MetaCyc:LEUSYN-PWY, MetaCyc:LYXMET-PWY, MetaCyc:METH-ACETATE-PWY, MetaCyc:METHANOGENESIS-PWY, MetaCyc:NADPHOS-DEPHOS-PWY, MetaCyc:NONMEVIPP-PWY, MetaCyc:NONOXIPENT-PWY, MetaCyc:OXIDATIVEPENT-PWY, MetaCyc:P101-PWY, MetaCyc:P121-PWY, MetaCyc:P184-PWY, MetaCyc:P2-PWY, MetaCyc:P321-PWY, MetaCyc:PANTO-PWY, MetaCyc:PHESYN, MetaCyc:PLPSAL-PWY, MetaCyc:PPGPPMET-PWY, MetaCyc:PROSYN-PWY, MetaCyc:PWY-1361, MetaCyc:PWY-2361, MetaCyc:PWY-2503, MetaCyc:PWY-5177, MetaCyc:PWY-5386, MetaCyc:PWY-5415, MetaCyc:PWY-5417, MetaCyc:PWY-5420, MetaCyc:PWY-5453, MetaCyc:PWY-5509, MetaCyc:PWY-5686, MetaCyc:PWY-5705, MetaCyc:PWY-5744, MetaCyc:PWY-5789, MetaCyc:PWY-5838, MetaCyc:PWY-5901, MetaCyc:PWY-5903, MetaCyc:PWY-6019, MetaCyc:PWY-6048, MetaCyc:PWY-6121, MetaCyc:PWY-6122, MetaCyc:PWY-6123, MetaCyc:PWY-6124, MetaCyc:PWY-6151, MetaCyc:PWY-6223, MetaCyc:PWY-6289, MetaCyc:PWY-6336, MetaCyc:PWY-6376, MetaCyc:PWY-6416, MetaCyc:PWY-6419, MetaCyc:PWY-6534, MetaCyc:PWY-6543, MetaCyc:PWY-6579, MetaCyc:PWY-6609, MetaCyc:PWY-6823, MetaCyc:PWY-6993, MetaCyc:PWY-7181, MetaCyc:PWY-7255, MetaCyc:PWY-7446, MetaCyc:PWY-7545, MetaCyc:PWY-7722, MetaCyc:PWY-7971, MetaCyc:PWY-7990, MetaCyc:PWY-8008, MetaCyc:PWY-8130, MetaCyc:PWY-8131, MetaCyc:PWY-8132, MetaCyc:PWY-8178, MetaCyc:PWY-8383, MetaCyc:PWY0-1241, MetaCyc:PWY0-1277, MetaCyc:PWY0-1280, MetaCyc:PWY0-1300, MetaCyc:PWY0-1312, MetaCyc:PWY0-1338, MetaCyc:PWY0-1352, MetaCyc:PWY0-1433, MetaCyc:PWY0-1471, MetaCyc:PWY0-1477, MetaCyc:PWY0-1517, MetaCyc:PWY0-301, MetaCyc:PWY0-321, MetaCyc:PWY0-41, MetaCyc:PWY0-42, MetaCyc:PWY0-43, MetaCyc:PWY0-501, MetaCyc:PWY0-521, MetaCyc:PWY1-3, MetaCyc:PYRIDNUCSAL-PWY, MetaCyc:PYRIDNUCSYN-PWY, MetaCyc:PYRIDOXSYN-PWY, MetaCyc:QUINATEDEG-PWY, MetaCyc:RHAMCAT-PWY, MetaCyc:RIBOKIN-PWY, MetaCyc:RIBOSYN2-PWY, MetaCyc:SALVADEHYPOX-PWY, MetaCyc:SERSYN-PWY, MetaCyc:SHIKIMATEDEG-PWY, MetaCyc:THIOREDOX-PWY, MetaCyc:THISYN-PWY, MetaCyc:THRDLCTCAT-PWY, MetaCyc:TRESYN-PWY, MetaCyc:TRPSYN-PWY, MetaCyc:TYRSYN, MetaCyc:VALSYN-PWY, MetaCyc:XYLCAT-PWY. Retain all 140 maintained MetaCyc:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against MetaCyc authority snapshots and docs/HARMONIZATION.md.
- retain: PathBank:SMP0002038, PathBank:SMP0002051, PathBank:SMP0002067, PathBank:SMP0002077, PathBank:SMP0002081, PathBank:SMP0002083, PathBank:SMP0002089, PathBank:SMP0002097, PathBank:SMP0002123, PathBank:SMP0002406. Retain all 10 maintained PathBank:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against PathBank authority snapshots and docs/HARMONIZATION.md.
- retain: Reactome:R-MTU-868688, Reactome:R-MTU-879299, Reactome:R-MTU-879325, Reactome:R-MTU-936635, Reactome:R-MTU-936654, Reactome:R-MTU-936721. Retain all 6 maintained Reactome:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against Reactome authority snapshots and docs/HARMONIZATION.md.
- retain: WikiPathways:WP171, WikiPathways:WP178, WikiPathways:WP266, WikiPathways:WP287, WikiPathways:WP296, WikiPathways:WP392, WikiPathways:WP478, WikiPathways:WP5019, WikiPathways:WP5060, WikiPathways:WP556, WikiPathways:WP5587, WikiPathways:WP71. Retain all 12 maintained WikiPathways:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against WikiPathways authority snapshots and docs/HARMONIZATION.md.
- retain: gomodel:6882d2b800000609, gomodel:YeastPathways_AERO-GLYCEROL-CAT-PWY, gomodel:YeastPathways_ARGSPECAT-PWY, gomodel:YeastPathways_ARGSYNBSUB-PWY, gomodel:YeastPathways_ASPARAGINE-BIOSYNTHESIS-1, gomodel:YeastPathways_ASPARAGINE-DEG2-PWY, gomodel:YeastPathways_ASPBIO-PWY, gomodel:YeastPathways_BSUBPOLYAMSYN-PWY, gomodel:YeastPathways_CITRUL-BIO2-PWY, gomodel:YeastPathways_DETOX1-PWY, gomodel:YeastPathways_FASYN-ELONG2-PWY, gomodel:YeastPathways_GLUCONEO-PWY-1, gomodel:YeastPathways_GLYCLEAV-PWY, gomodel:YeastPathways_GLYCOLYSIS, gomodel:YeastPathways_HEME-BIOSYNTHESIS-II, gomodel:YeastPathways_HEXPPSYN-PWY-2, gomodel:YeastPathways_HOMOCYS-CYS-CONVERT, gomodel:YeastPathways_HOMOCYSDEGR-PWY-1, gomodel:YeastPathways_IPPSYN-PWY, gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2, gomodel:YeastPathways_PERIPLASMA-NAD-DEGRADATION, gomodel:YeastPathways_PHOSLIPSYN2-PWY-1, gomodel:YeastPathways_PROUT-PWY, gomodel:YeastPathways_PWY-1801-1, gomodel:YeastPathways_PWY-2301, gomodel:YeastPathways_PWY-5041, gomodel:YeastPathways_PWY-5080-1, gomodel:YeastPathways_PWY-5123, gomodel:YeastPathways_PWY-5194-1, gomodel:YeastPathways_PWY-5340, gomodel:YeastPathways_PWY-5344, gomodel:YeastPathways_PWY-5651, gomodel:YeastPathways_PWY-5653, gomodel:YeastPathways_PWY-5669, gomodel:YeastPathways_PWY-5670-1, gomodel:YeastPathways_PWY-5694, gomodel:YeastPathways_PWY-5697, gomodel:YeastPathways_PWY-5703, gomodel:YeastPathways_PWY-5760-1, gomodel:YeastPathways_PWY-6074-1, gomodel:YeastPathways_PWY-6075-1, gomodel:YeastPathways_PWY-6147, gomodel:YeastPathways_PWY-6614, gomodel:YeastPathways_PWY-7176, gomodel:YeastPathways_PWY-7219, gomodel:YeastPathways_PWY-7220-1, gomodel:YeastPathways_PWY-7221, gomodel:YeastPathways_PWY-901, gomodel:YeastPathways_PWY3O-123, gomodel:YeastPathways_PWY3O-15, gomodel:YeastPathways_PWY3O-1565, gomodel:YeastPathways_PWY3O-17, gomodel:YeastPathways_PWY3O-1743, gomodel:YeastPathways_PWY3O-1801, gomodel:YeastPathways_PWY3O-214, gomodel:YeastPathways_PWY3O-242, gomodel:YeastPathways_PWY3O-259, gomodel:YeastPathways_PWY3O-4, gomodel:YeastPathways_PWY3O-402, gomodel:YeastPathways_PWY3O-4105, gomodel:YeastPathways_PWY3O-4106, gomodel:YeastPathways_PWY3O-4108, gomodel:YeastPathways_PWY3O-4112, gomodel:YeastPathways_PWY3O-4120, gomodel:YeastPathways_PWY3O-4153, gomodel:YeastPathways_PWY3O-4300, gomodel:YeastPathways_PWY3O-440, gomodel:YeastPathways_PWY3O-450, gomodel:YeastPathways_PWY3O-48, gomodel:YeastPathways_PWY3O-50, gomodel:YeastPathways_PWY3O-5268, gomodel:YeastPathways_PWY3O-64, gomodel:YeastPathways_PWY3O-6407, gomodel:YeastPathways_PWY3O-6499, gomodel:YeastPathways_PWY3O-697, gomodel:YeastPathways_PWY3O-8, gomodel:YeastPathways_PWYQT-4432, gomodel:YeastPathways_PYRUVDEHYD-PWY, gomodel:YeastPathways_SO4ASSIM-PWY, gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1, gomodel:YeastPathways_THREOCAT2-PWY, gomodel:YeastPathways_UDPNAGSYN-YEAST-PWY, gomodel:YeastPathways_YEAST-4AMINOBUTMETAB-PWY, gomodel:YeastPathways_YEAST-FAO-PWY, gomodel:YeastPathways_YEAST-GALACT-METAB-PWY, gomodel:YeastPathways_YEAST-RNT-SALV. Retain all 86 maintained gomodel:* pathway records as distinct, non-duplicate source-scoped pathway definitions verified against gomodel authority snapshots and docs/HARMONIZATION.md.
- retain: MetaCyc:P121-PWY, MetaCyc:PWY-6609, PathBank:SMP0002081, PathBank:SMP0002083. Retain MetaCyc:P121-PWY, PathBank:SMP0002081, PathBank:SMP0002083, and MetaCyc:PWY-6609 as separate maintained records per docs/HARMONIZATION.md: PathBank:SMP0002081 models the Escherichia coli K-12 BioPAX PW002069 adenine/adenosine salvage network with explicit subcellular transport and ammonia lyase steps, whereas MetaCyc:P121-PWY, PathBank:SMP0002083, and MetaCyc:PWY-6609 represent distinct authority-scoped pathway boundaries and step topologies.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EV-QC-VALIDATE | .venv/bin/pathwaymech-run-qc; stdout summary (270 pathway records, 537 history records, 22,085 evidence blocks, 33 source records) | supports | Executed .venv/bin/pathwaymech-run-qc across the frozen working tree at 556074d91f600aa9e5ca97e0b4baef6d99513930: validated 270 pathway records against the closed LinkML schema, verified all identifiers and labels against local authority snapshots, validated 537 history records and 22,085 evidence blocks, and confirmed pages/ synchrony. |
| EV-PYTEST | .venv/bin/pytest -q; pytest suite execution across tests/ | supports | Executed the full pytest suite (8,045 passed, 3 skipped), verifying schema validation, identifier policy, KGX export, SSSOM export, source registry, and structured record-review contract invariants. |
| EV-RUFF | .venv/bin/ruff check --no-cache .; ruff check output | supports | Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks passed). |
| EV-GIT-DIFF | git diff --check; git worktree at 556074d91f600aa9e5ca97e0b4baef6d99513930 | supports | Executed git diff --check with exit code 0; no whitespace errors or conflict markers. |
| EV-REVIEW-CHECK | reviews/structured/; 197 retained structured review bundles | supports | Validated all 197 previously retained structured review bundles under reviews/structured/ via scripts/record_review.py check; confirmed all prior findings on maintained data/pathways/*.yaml records were resolved and the only 2 open finding heads in historical bundles target withheld research/pathway_additions/ drafts. |
| EV-CORPUS-INSPECTION | data/pathways/; 270 maintained pathway YAML files (7,652 participants, 1,591 reactions including 693 RHEA:* reactions, 14,322 mechanistic_edges) | supports | Inspected all 270 maintained pathway records in data/pathways/*.yaml: 100% declare valid pathway_type, 100% of 14,322 mechanistic_edges carry structured evidence blocks (20,959 edge-level evidence items; 22,085 total evidence blocks across records, steps, and edges), 100% of 693 RHEA:* reaction nodes declare explicit direction with zero cross-record direction conflicts, and zero duplicate xrefs exist across records. |
| EV-GLCMANNANAUT-PWY | data/pathways/amino-sugar-superpathway.yaml; lines 211-255 (reactions list in MetaCyc:GLCMANNANAUT-PWY) | supports | In data/pathways/amino-sugar-superpathway.yaml (MetaCyc:GLCMANNANAUT-PWY), reactions[13] (BiGG:ACMANAptspp, N-acetyl-D-mannosamine transport via PTS  (periplasm)) and 10 RHEA:* reactions (reactions[3..12]) omit category: molecular_activity while 3 subpathway entries (MetaCyc:PWY0-1324, MetaCyc:GLUAMCAT-PWY, MetaCyc:GLYCOLYSIS at reactions[0..2]) explicitly declare category: pathway. |
| EV-KGX-EXPORT | src/pathwaymech/kgx.py; lines 74-101 (_PREFIX_CATEGORIES and _node_category) | supports | In src/pathwaymech/kgx.py, _PREFIX_CATEGORIES maps RHEA to biolink:BiochemicalReaction when reaction.category is None, whereas explicit category: molecular_activity maps via _PARTICIPANT_CATEGORIES to biolink:MolecularActivity; BiGG is absent from _PREFIX_CATEGORIES, so a BiGG reaction without category: molecular_activity falls back to DEFAULT_CATEGORY (biolink:NamedThing) with empty source_category. |
| EV-NODES-TSV | pages/downloads/nodes.tsv; row BiGG:ACMANAptspp | supports | In pages/downloads/nodes.tsv, BiGG:ACMANAptspp is exported with category biolink:NamedThing and empty source_category because reactions[13] in data/pathways/amino-sugar-superpathway.yaml omits category: molecular_activity. |
| EV-MIXED-REACTION-CATEGORY-RECORDS | data/pathways/; 12 MetaCyc records: MetaCyc:CYANCAT-PWY, MetaCyc:GLCMANNANAUT-PWY, MetaCyc:PWY-1361, MetaCyc:PWY-2503, MetaCyc:PWY-5744, MetaCyc:PWY-5789, MetaCyc:PWY-6993, MetaCyc:PWY-7255, MetaCyc:PWY-7971, MetaCyc:PWY0-1471, MetaCyc:PWY0-41, MetaCyc:SALVADEHYPOX-PWY | supports | Across 12 maintained MetaCyc pathway records, reactions[*] entries mix explicit category declarations (molecular_activity or pathway) with 33 catalytic reaction entries (30 RHEA:*, 2 MetaCyc:RXN-*, 1 BiGG:ACMANAptspp) that omit category, producing mixed KGX node categories within the same pathway reaction graph. |

## Limits And Additional Notes

- Twelve maintained MetaCyc pathway records exhibit mixed within-record reaction category typing (33 catalytic reaction entries omit category: molecular_activity while sibling entries in the same reactions[] list declare category), including BiGG:ACMANAptspp in MetaCyc:GLCMANNANAUT-PWY which falls back to biolink:NamedThing in pages/downloads/nodes.tsv; these are recorded as open minor findings F-STAGE4-001 and F-STAGE4-002 for Stage 5 remediation.
- Verification of literature-backed evidence blocks relied on the repository's local authority snapshots and curated evidence quotes/abstracts at frozen commit 556074d91f600aa9e5ca97e0b4baef6d99513930 without re-fetching external publisher full texts over the network.
- Per Cycle 1 Stage 4 (record_review) workflow policy, no edits were made to data/pathways/*.yaml during this stage; open findings F-STAGE4-001 and F-STAGE4-002 are carried forward to Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T013600Z-stage4-frozen-corpus-cohort-review
kind: category
repository: CultureBotAI/PathwayMech
title: Cycle 1 Stage 4 Full Frozen-Inventory Record and Cohort Review of 270 PathwayMech
  Maintained Records
started_at: '2026-10-22T01:00:00Z'
finished_at: '2026-10-22T01:36:00Z'
reviewer:
  identity: Antigravity (review-yaml-record + review-yaml-category)
  kind: agent
  model: Claude Opus 4.6 (Thinking)
  independence: self_review
  independence_basis: Same agent session (a1d1e545-faee-4294-8a87-4c2d031a6538) executed
    Cycle 1 Stages 1-3 curation in CultureBotAI/PathwayMech prior to running this
    Stage 4 frozen-inventory review.
skill: review-yaml-category
completion: completed
verdict: pass_with_limitations
native_verdict: coherent
scientific_review: true
summary: 'Completed a full-coverage frozen-inventory scientific record and cohort
  review of all 270 maintained pathway YAML records in data/pathways/*.yaml at Git
  commit 556074d91f600aa9e5ca97e0b4baef6d99513930 across all 8 identifier namespaces
  (MetaCyc: 140, gomodel: 86, WikiPathways: 12, GO: 10, PathBank: 10, Reactome: 6,
  KEGG: 3, MIBiG: 3; 7,652 participants, 1,591 reactions including 693 RHEA:* reactions).
  All 270 records pass closed LinkML schema validation, authority snapshot identifier/label
  checks, history validation (537 records), and edge-level evidence verification (14,322
  mechanistic edges, 20,959 edge-level evidence items, 22,085 total evidence blocks).
  Identified 2 minor open findings (F-STAGE4-001 on MetaCyc:GLCMANNANAUT-PWY and F-STAGE4-002
  across 12 MetaCyc records) concerning omitted category: molecular_activity on 33
  catalytic reactions inside mixed-typing reactions[] lists, preserved unedited for
  Stage 5 grouped remediation.'
source:
  git_revision: 556074d91f600aa9e5ca97e0b4baef6d99513930
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
    sha256: cf1fc7347b88c2ecb1139564b24bd64018e0fc65793314061f3cf22eed5fd5ef
    role: target
  - path: data/pathways/3-oxoadipate-degradation.yaml
    sha256: 214ef2d38ede4bb4e919f6f53699491e7c53b8d9b5b858c6ba80084e5b067032
    role: target
  - path: data/pathways/4-aminobenzoate-biosynthesis-i.yaml
    sha256: b0150b47850d17acbbe560a7d40a82d49a2f976a92ea15ab43c44df1a83c4b91
    role: target
  - path: data/pathways/4-aminobutyrate-degradation.yaml
    sha256: dc220e2a4d394750d7adc8bbaa1a7060082c28daeaa077fb6e9c1f94f2168173
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
    sha256: e5f0507a6060dab794ffc5b0b11b125f23677a9d54c5b5440a07eb05c48a72a9
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
    sha256: 62929187a92825274450afa61508d3139a7a88865848a3c49e07ca045a361a95
    role: target
  - path: data/pathways/adenine-and-adenosine-salvage-i.yaml
    sha256: cc8721d24ba2236931ca151dcb035d9a9a671ce486acd950e724c9e7ffbf44d2
    role: target
  - path: data/pathways/adenine-and-adenosine-salvage-ii.yaml
    sha256: d0a6942e6b36af20e66dc5546d62028b7f8239c6b126d13fa0548006cd2c331a
    role: target
  - path: data/pathways/adenine-and-adenosine-salvage-iii.yaml
    sha256: acafd5863d376489873aa366db9359ccaf57a693b688b472f78c89e26e3eae86
    role: target
  - path: data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml
    sha256: 3cd2f4ba0bdbd27028fad8814a024a16cdca397bc09764ecba2597826bfc0625
    role: target
  - path: data/pathways/adenosine-nucleotides-degradation-ii.yaml
    sha256: b7f837be8676b08c9a8a0f417ca17a695664e8614b30e7847f4f7e05c845cbf6
    role: target
  - path: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
    sha256: 3840e82b7a5d9809e754222ac412b4321f3b99e73e085a3efdb9fbe6b402c9ef
    role: target
  - path: data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
    sha256: 8453146fc5cc438fd95be5acc623ba0f6fbe52e647ad21f1fa2dc535ee619184
    role: target
  - path: data/pathways/adenosylcobinamide-gdp-salvage-i.yaml
    sha256: 2e4943a2b36d529ef076e8a8ee561c120e65dc2e8e9c6c4452e2544a180645cd
    role: target
  - path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
    sha256: affa9eb37e5575d895dc7ae93173037ff18019e2a5e74012139b6aacb6febaf3
    role: target
  - path: data/pathways/aerobactin-biosynthesis.yaml
    sha256: 3e4e50965749a9fa9dfe6319fd1462cc8329c10b7f4ab5363e7b486f2f32e3d4
    role: target
  - path: data/pathways/aerobic-glycerol-degradation.yaml
    sha256: 6541509e6b50f5a7f462010541a7953ddcafa82c49959ffcbf7658a00b5e92fb
    role: target
  - path: data/pathways/allantoin-degradation-iv-anaerobic.yaml
    sha256: bd9c6c24677b6852478f2dd9e2846ade22d13dd722951a50acfb8b4516f1a8fb
    role: target
  - path: data/pathways/allantoin-degradation-to-glyoxylate-i.yaml
    sha256: 4d8f1c7aee53baaf61885814f0e6870ae480759cb825037725bfa39395921ac2
    role: target
  - path: data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
    sha256: 1fe731570ceb2038b0b153686be184c99afbd82ab6ba9a9516694b2277de1b37
    role: target
  - path: data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml
    sha256: adb71534db0d3300a6757b499b757a2d17f901910cc2417d99ad6f7f510fdc31
    role: target
  - path: data/pathways/amino-sugar-superpathway.yaml
    sha256: fc436f537303f50121c472a4ece19249f3e6eb74d7304933fbafb37e04a61978
    role: target
  - path: data/pathways/aspartate-biosynthesis.yaml
    sha256: 8c26f4bd655f7b13db25c70e817db9cb6b4232ccc941bf890bcbff54b25a180e
    role: target
  - path: data/pathways/assimilatory-sulfate-reduction.yaml
    sha256: 64aa47bf9da9d04d1e53d164f44d2ec4fb42adede455ea5dbbaa351917b398bc
    role: target
  - path: data/pathways/bacillibactin-biosynthesis.yaml
    sha256: aaf46730530dc9ae86fd18f8b382baebbcf0f37b79342b7eebf18e0e64ebeafa
    role: target
  - path: data/pathways/baesr-two-component-signal-transduction.yaml
    sha256: 1cf9262a0df376a19517b3f55ccaac67dacc8af8ce58bd8a1b2046e93a951824
    role: target
  - path: data/pathways/benzoate-degradation-i-aerobic.yaml
    sha256: 3f8bbb8eceaa4420fa822e87ce01cca6b9d1967908dc117628aba71f54030696
    role: target
  - path: data/pathways/benzoyl-coa-degradation-i-aerobic.yaml
    sha256: b2fc0cca6ac455fcc1820766caeb49a13beea64e49477bb774d3893e8bde3fff
    role: target
  - path: data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml
    sha256: e43e6ad5563c38af738e8f1c7b733510072b531196ce435395896b62951c6ab9
    role: target
  - path: data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml
    sha256: 40fa37e63c5be6ec6c9d33bf67f4bf06e597fc4c9b12514d34401379b124ad51
    role: target
  - path: data/pathways/beta-alanine-biosynthesis-iv.yaml
    sha256: f12c8f6ea8a7b774c0e596fec3c141de4a5ae60049aee7caec8018f2827aa2ee
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
    sha256: e7c9ab47f1cb65dd2ab0c467436da840f77e592fa9ca72293014350820cdb6af
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
    sha256: b7ab2d44d5694a1c1f56d15474c5d59ef66e7a0df36516e3325ea605b6c98c43
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
    sha256: bf40044ef709ce95ef9faafef7a724efbdac7764cce18fdd263520f0593f1924
    role: target
  - path: data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml
    sha256: bdca4a5ea4688a5a4f4ab4f18e93dc3501b40e0bfe00eb7fa1621998295f438d
    role: target
  - path: data/pathways/curcumin-degradation.yaml
    sha256: 814e063d50371068e9a7f3d6238b0f6ad76e172f6072c59b570cafdba0cb407b
    role: target
  - path: data/pathways/cyanate-degradation.yaml
    sha256: 7972d75389eb8cc316ff268467d6846351fc313850aa165ae51983bf87ed717f
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
    sha256: 3d4489e00bc5bc9d7c5160d1ad3e7ed4a8c64e1722ef80b562740a6699febe5b
    role: target
  - path: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
    sha256: acc8b361993a1db31e3bf253e05526b2998b7a91c0cf3b0e6628aaf530adb688
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
    sha256: c6bf14ce9e385df8aab07fb667d4aaecffcc53495d4b7372b02ea183f3898ccd
    role: target
  - path: data/pathways/ergosterol-biosynthesis-i.yaml
    sha256: 0439f963e2bcbb3e5e781df1338549c8963929747a721c72171cf533030344c5
    role: target
  - path: data/pathways/ergothioneine-biosynthesis-i.yaml
    sha256: 238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527
    role: target
  - path: data/pathways/ethanol-degradation.yaml
    sha256: d9df81a6d31bb732e2077798277c3b840c71596a482366603a93d22285aa6f84
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
    sha256: 2da686ea5b62f2e43585967a23b1739d819a42dfcf19d0492cef55c944137120
    role: target
  - path: data/pathways/fatty-acid-oxidation-pathway.yaml
    sha256: 2dcd1db7489ee7695bd99461bbee5c59064e15853b3ab3c413ea6b6118aefe36
    role: target
  - path: data/pathways/flavin-biosynthesis-i.yaml
    sha256: 417d94b49af861613f07f76e2f4dc0d6b4d44123a57547a1c05c2aca91e2a025
    role: target
  - path: data/pathways/folate-interconversions.yaml
    sha256: 6774526812ae134d049d2bd6f36941ff0d4453558aa68259a790e93149278d6a
    role: target
  - path: data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml
    sha256: e100dd411c9dc79be86d86d0b2ee76f9a0c228d673ecb4d4b8343b264cfaa054
    role: target
  - path: data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
    sha256: 3e5b25fc917a30aca70b1dbdce4c70cb7b2d69f595b1f0f13d391812b7cdcb93
    role: target
  - path: data/pathways/fructoselysine-catabolic-process.yaml
    sha256: e9e80038a8671da109e8453523439ed921fe7810bb96b24f55dc532b4dd6ca5f
    role: target
  - path: data/pathways/galactose-degradation.yaml
    sha256: 3d1cd470853a62a3373ee876e18ba1c49f1aec17b858acb929c49af89c4296ee
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
    sha256: 365e9c29df8a62dd3dd5d4a3a190e530f6e3beae4a8e159be04ec9e4a9a952ba
    role: target
  - path: data/pathways/glutamate-degradation-i.yaml
    sha256: a518e6f42cee9d981d3a2876da0aa0ba9ed1612b90163f69cbbac1d8b1be28c0
    role: target
  - path: data/pathways/glutaryl-coa-degradation.yaml
    sha256: 3c2ac2ae8443a7bdac87bd8ca9e612eee869fb479f3625231fadf84658e16317
    role: target
  - path: data/pathways/glutathione-biosynthesis.yaml
    sha256: e6b762e025742ca9cf0766d8d2d8b3f15e1c2b0078e7af2ab21bab1a43d8dba7
    role: target
  - path: data/pathways/glutathione-degradation.yaml
    sha256: f8f06c4612ab0c7e38f3b46378454ba449231a013816902262ef6bddcc4cf2e4
    role: target
  - path: data/pathways/glutathione-glutaredoxin-redox-reaction.yaml
    sha256: 670795c76c89c998d015e40536a5aba90acccb1430e7b4649aef2f738bad5e1b
    role: target
  - path: data/pathways/glycerol-biosynthesis.yaml
    sha256: 07b3f629ede35b4c42441295f1a3596a45ecbe776f9667633b3739c19bf742a6
    role: target
  - path: data/pathways/glycerol-degradation-v.yaml
    sha256: 17004e2911d28d42612c2010bf28d3339dc7f5f8a5af1e49b94cb4bae98ab2ba
    role: target
  - path: data/pathways/glycine-cleavage.yaml
    sha256: 14313c0e3e8c3af451b0946c2b7d8d20545af13e8e27c5441cea62648899a524
    role: target
  - path: data/pathways/glycogen-catabolism.yaml
    sha256: fc91636aa102a87bcb65d173ff28b2acbb356ea67beb831e00e7a93d9ae52aa4
    role: target
  - path: data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml
    sha256: ce99470da6b66a527a1a7ffe4e46e059afa4af75496a8fca96f2831049410be6
    role: target
  - path: data/pathways/glyoxylate-assimilation.yaml
    sha256: 218feaba4c438ac1f7dff5765e5993153040fa1b0cc80b135440ad4ece8622ea
    role: target
  - path: data/pathways/glyoxylate-cycle.yaml
    sha256: bd5793fee6b8af7da1e67eece20ebfd65004a48bdfe4d4afbbfb3d544c8138b9
    role: target
  - path: data/pathways/guanine-and-guanosine-salvage.yaml
    sha256: 7133352b12d3cd8579acc128b2896b9247dd8503f06c339d2526e137eb17e58e
    role: target
  - path: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
    sha256: 65c619b8dfdd73062ad25ec9757f617da2a1a5739502ea44004be38e20897df0
    role: target
  - path: data/pathways/heme-biosynthesis-i-aerobic.yaml
    sha256: 0b59dea7ec3eb1b01ba4b147d7532f7a395ef1d6d4128eb7f6be7e6a7cf8dcc3
    role: target
  - path: data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml
    sha256: d72784cfaf3d8bf0e30f226b687177eaf269358a3317327aaa2ca12686c7b1ff
    role: target
  - path: data/pathways/homocysteine-and-cysteine-interconversion.yaml
    sha256: 548a2a31db077211819e31504c16f45e3ce711858ef8bafc992d142e50fe095a
    role: target
  - path: data/pathways/homogentisate-degradation.yaml
    sha256: a833e707d3dbd92ff09194e1d19b7c419aa3e2c4c45d3a53064c8915a2d755d2
    role: target
  - path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    sha256: 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a
    role: target
  - path: data/pathways/inosine-5-phosphate-biosynthesis-i.yaml
    sha256: 74e4cd1621fc270ba365ef411b3079692de075024264f7e8866f6b0d9442938e
    role: target
  - path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    sha256: d676ccc1740fc538486cc7c9664bd5e3e2c89cc2aadd74bcffd586cce6aa7b97
    role: target
  - path: data/pathways/inositol-phosphate-biosynthesis.yaml
    sha256: add22f805f7a14a195c64a04e8b070f98c68626b30e768898e843213e7809fcc
    role: target
  - path: data/pathways/isoleucine-degradation.yaml
    sha256: 50585e2d8674b369b4aa5271ba78c57c18ea7556138e16e55140d77c42aa935e
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
    sha256: fa54ce93a653642b1fe2e0d9a1a02654ca238723ca6191a113c4f105ee1e07fe
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
    sha256: 766ba43c30ea3c6568779592c48aa667dd38880b0023a091979df2705161bb16
    role: target
  - path: data/pathways/l-asparagine-degradation.yaml
    sha256: 7df30c94062629ad64c6ed7d137a637f904a1f7428d2b530fde78b78bc5df5c2
    role: target
  - path: data/pathways/l-carnitine-degradation-i.yaml
    sha256: b007e4f9bf0d67c08c0c2262a46b6ddf4cbbc37d05ade639725f74bb008be767
    role: target
  - path: data/pathways/l-cysteine-biosynthesis-i.yaml
    sha256: 54fe6a258f21f5866d4051ad8b756f347191a9fe3a154b3749c8393367157476
    role: target
  - path: data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml
    sha256: acb2ce1d623b40d939a091bdbb3f9ce5d118a00aff3ebb873752ea323722de46
    role: target
  - path: data/pathways/l-fucose-degradation-i.yaml
    sha256: a00b36d76e86e0102822cd1d280e686310aa0ff1603d0f4e53a8ed7286b3dc9a
    role: target
  - path: data/pathways/l-histidine-biosynthesis.yaml
    sha256: d4f67cf6d398a8ed42fcd7a83588f93c0f81ee22ddc94308d8027a9aa39e6c58
    role: target
  - path: data/pathways/l-homocysteine-biosynthesis.yaml
    sha256: 5f4f330c4cee30dfe0ee244331adb501776c4e34c4f34811f428379cc99380e5
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
    sha256: 7f6375da56c7c53b27a336f385c71564c46ad7700e397063915bf6d6bdd18530
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
    sha256: 47625a371cab68efdf3f6e5deda9a982d8c309bda00f74827b03f0ae164ec49d
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
    sha256: 5e003a44a1519e0a121a39819b334e57feee397e033d6db2ccec01399898daa7
    role: target
  - path: data/pathways/l-tryptophan-biosynthesis.yaml
    sha256: 92206dbd7e6e9aba6fee6e9f866e3eb3fe019cd6b832a0ac6586cbcc65ce6dcc
    role: target
  - path: data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml
    sha256: 435fa7b9e72cb017859159a7eb2ba3c078248638810272043fb23a22e27a67ea
    role: target
  - path: data/pathways/l-tyrosine-biosynthesis-i.yaml
    sha256: e61553cc86414476cc4bc593114c2c0820b01246225450edffdef55910efe376
    role: target
  - path: data/pathways/l-tyrosine-degradation-iii.yaml
    sha256: 2ab3d77be1a21b236beb89a4b6c316c37f37bac708741ca496b552318ee96b7e
    role: target
  - path: data/pathways/l-valine-biosynthesis.yaml
    sha256: 9b58c4c2bdd0b065c6227492dda5c6bc998902739848ab4f2dc1f070e7bd9c19
    role: target
  - path: data/pathways/leucine-degradation.yaml
    sha256: b11427a45a2f33becfda49dee1e4a636844f2c1d8febf8042e0e5daf10892d6d
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
    sha256: dd4237f6d08801e661b2089644fcfb4c46fbbd1f65868d6853d51cae84293251
    role: target
  - path: data/pathways/mannosylglycerate-degradation.yaml
    sha256: b73c407b4315efc45a30ed7121cb3797945cf0a4e86ab010bf5554b276b0e0a6
    role: target
  - path: data/pathways/methanogenesis-from-acetate.yaml
    sha256: 47d1c71951ce5806e5c9570ee00b2ab9f8634158251ee06821a0f77017b0eca3
    role: target
  - path: data/pathways/methanogenesis-from-h2-and-co2.yaml
    sha256: 553922ede0ecdb12ebe569dbb9d8af1c70d4aa190e4fd60e69a9bc7ea0cf8e1e
    role: target
  - path: data/pathways/methionine-salvage-pathway.yaml
    sha256: 2220e5618ddc3f993788bf772fd20c560350c3752885a9d7bb07eb7e297d7b3c
    role: target
  - path: data/pathways/methylerythritol-phosphate-pathway-i.yaml
    sha256: 868d6af5bb463ac41869ed65820b0e87fadb1de7ccb018fb26170ffe423b2fea
    role: target
  - path: data/pathways/methylglyoxal-catabolism.yaml
    sha256: 4e0655e6c340986dbb79f846b237550d6d793e7ae5781d576df4fbd6fa5f1ba1
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
    sha256: 25a739d9e28a0dfaabc31f59bcaa98179ca4377f501a0f8a8a869039b786afdb
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
    sha256: f1131912336cddeb1e79f27e4c0087e7188d97ad775583fbef65b7056086a5e5
    role: target
  - path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    sha256: 5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2
    role: target
  - path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    sha256: 1ddbabfa3bad2292e49add564ee94283ff622c5dae55902f78aa5b4b1d6908b8
    role: target
  - path: data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml
    sha256: d9712d9291fdec2d7188a31d3eabf54dc198b880c996f39be3e5ada28c4684dc
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
    sha256: f41413a4a24571ece2b3e2d93490f778a1e8b9619c948fc4d6d1825db58d579a
    role: target
  - path: data/pathways/nad-salvage-pathway-v.yaml
    sha256: 5714f5fe02a834e4b4836d61524835501f8eeaa6241d7da5be3f6242ca572d5a
    role: target
  - path: data/pathways/nicotine-degradation-ii.yaml
    sha256: 59d1a699b4e40ce680715afa958f8a659feae11b6b1786a5867f25733b83d36c
    role: target
  - path: data/pathways/nitrate-reduction-i-denitrification.yaml
    sha256: 7c5b3ca9714dd9968901921b54bb82f44b08f85da322cb5527453ac685568ecd
    role: target
  - path: data/pathways/nitrate-reduction-viii.yaml
    sha256: 5243f546a62490581e35d29516f2ecb830b1284748d6b2b042b82e7d9f6303b7
    role: target
  - path: data/pathways/oleate-biosynthesis.yaml
    sha256: 3dcf719e913158bb23184d8ac68a8b6bce55f7f7ef0c69bee8c71a997d2cce2e
    role: target
  - path: data/pathways/palmitoleate-biosynthesis.yaml
    sha256: 47ad28d2b5f793ae9916a213e5b9522248d24e1415c32640f35c4908b6383b9e
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
    sha256: 0bba116121063c695033713548f5be6e79a09c875c08754785a86da58fdb7741
    role: target
  - path: data/pathways/petrobactin-biosynthesis.yaml
    sha256: 7d0737b9f0bb3a4673e7341e53c5763c80e4fb46fb2944db8c2199a6e66d645a
    role: target
  - path: data/pathways/phenylacetate-degradation-i-aerobic.yaml
    sha256: e99722d1ee920cf64aaeae7b00f1de9b59f939bd96a03a7ac5f2885933a72227
    role: target
  - path: data/pathways/phenylalanine-biosynthesis.yaml
    sha256: d83bf9681c328942b0da0101d675687d2772f8017e236df3e813272fe59927d7
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
    sha256: 5d41048d73ffc521a1d8aeaf79f9ff7ecffd80dffb6bd8915a2e7d512342b455
    role: target
  - path: data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml
    sha256: f0fb3e3b3a323efe8e435ecff37c2e870f208f0e05dae61c4d417e61a8bac720
    role: target
  - path: data/pathways/phosphatidylcholine-biosynthesis-i.yaml
    sha256: 9707f0bd75a5ade7eff2b25d0d8f8b7953b7749e2cdf2878156c09b9eb1d9d63
    role: target
  - path: data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml
    sha256: c1d5c378d7fff51a6ba181570520d299898891226f4f00662d30b4be6313be9c
    role: target
  - path: data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml
    sha256: 6e81302207f8ac3a9d1eee0a63cf89b4bed0d6813339819ac96a2d44eec6194b
    role: target
  - path: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
    sha256: f32a3b1cf37d1ee31de0900901860a17029ffe49f9d97deb4763f22d4fa580c7
    role: target
  - path: data/pathways/phospholipid-biosynthesis.yaml
    sha256: 69eb1a16bb8baa5beccd8d281522534ff29afe828826aae39532063d6d131669
    role: target
  - path: data/pathways/phospholipids-degradation.yaml
    sha256: fb0b58b847d80f1a68aac342f1974cb6f51171da44ffe3285030454221af5c19
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
    sha256: 308c60f798bdc3dd8d004c3b5c214dcb9ab4f1ed2a174d169ef4d0958300d145
    role: target
  - path: data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml
    sha256: ad122132b9b414dfdf4aff99f6b26b476cd0cdb98d9dacbfa85ea87f0ac269d6
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
    sha256: 81526ec7fcedf14ead1ef9be33747b3560e74f4293e08ac6b6653cf6cb85eb1b
    role: target
  - path: data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml
    sha256: 60750cb046b847a5d52458cff6eab771be2a9200755c259cfe8d87c4808e95fa
    role: target
  - path: data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml
    sha256: d283eb6065c21162774b7c8267ab48ce82766a20ce93a37b182bf205e5c14bff
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
    sha256: 9bb7972608c907fff78104cff4d93a54af3b5cffd6debfd9be9852d460dc297f
    role: target
  - path: data/pathways/spermidine-biosynthesis-and-metabolism-escherichia-coli.yaml
    sha256: 0adef1da2d818af7c62d7e3952b2115585b47b8f132ec189cde2b435d2721680
    role: target
  - path: data/pathways/spermidine-biosynthesis-i.yaml
    sha256: 7a59a97a06f5624a7c81b7aba90e909454eafbe37128e044b92fbd92bc82165b
    role: target
  - path: data/pathways/spermine-biosynthesis.yaml
    sha256: abc49bff88359eabe59d05ae6ba0c1255e6937f6748d738220253b31d7744d3c
    role: target
  - path: data/pathways/sphingolipid-biosynthesis-yeast.yaml
    sha256: d75f7d359601e9967fc0f47c0bf369b0c2fbf4759014b6839131600cbf46ef22
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
    sha256: 3e20747a383ef29d995e2eee4b93040423b7d49b27843c0ec1987edcf6d82588
    role: target
  - path: data/pathways/sulfoquinovose-degradation-i.yaml
    sha256: 741fc68daedf7cb7000b7cc5dc94ce5c0029fe9d30ce56d392c51a2aa9ac390c
    role: target
  - path: data/pathways/sulfoquinovose-degradation-ii.yaml
    sha256: 20a95c209243399b88a90fbecb0d8d310ebfb3094fc6ee4487352fdc2185c596
    role: target
  - path: data/pathways/superoxide-radicals-degradation.yaml
    sha256: 4d0224dd2604fa1cce375b2afa12e614f22e304153734504e03da6e83c797585
    role: target
  - path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    sha256: 8d24e6ff858759aa4eaecd04b456ffa1b79c992bc090637f5cc8805a5ecbf492
    role: target
  - path: data/pathways/tca-cycle-detailed.yaml
    sha256: e98639698c8b4f68286adbeb7d68305a2b3aedcbd9a548bc06feccc91eaf2e39
    role: target
  - path: data/pathways/tetrahydrofolate-biosynthesis.yaml
    sha256: ce15c57307f843c5773b7e5515d09077f8c7c4ef1bbc588e1223d26b4e340690
    role: target
  - path: data/pathways/tetrahydromonapterin-biosynthesis.yaml
    sha256: 0349c62d93993252bdab4e11a477eaca142eb516c59961721a317ed333eda182
    role: target
  - path: data/pathways/tetrapyrrole-biosynthesis.yaml
    sha256: b9b73976e6a55b8a24abfd22a8e239733d2f7edd2a746e9e774d5df3fe5e5296
    role: target
  - path: data/pathways/thiamine-biosynthesis.yaml
    sha256: b22273bb29300508a8446c84344cbe568a8ec56858c7d983dd951ba3fd04ca1e
    role: target
  - path: data/pathways/thiamine-diphosphate-biosynthesis-i.yaml
    sha256: 05fe1413e04fa3c2b95e44af1bda6c795ef53d3ea3529d18f6c42bac2e8079ea
    role: target
  - path: data/pathways/thioredoxin-pathway.yaml
    sha256: 8fa7373fe66807d9c12083c5fbe5e410ab5eaadf1100179590e488f74b8bafe0
    role: target
  - path: data/pathways/threonine-degradation.yaml
    sha256: 23cce07f43a32645d175d779eabcdfa873a8bcb5d2f2c10171b06cd2fd7dd9ae
    role: target
  - path: data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml
    sha256: be0cf90a07906abd1aec303dc0871e33e97510e961d77e4dcd1649f7fb7f1264
    role: target
  - path: data/pathways/trehalose-biosynthesis-i.yaml
    sha256: 2345d073b0ee434ab1a897653441d1bcd431ba0314e2265b9699fc6fd5a8eefb
    role: target
  - path: data/pathways/triglyceride-biosynthesis.yaml
    sha256: 0ab6fcab3fa418433fffcd68cc992090145bf43c16c1132bddd1e9834a1a6a2f
    role: target
  - path: data/pathways/tryptophan-degradation.yaml
    sha256: 08d5c4115a06db36842a5f384fc5d6f9c0a37f1fdf341d23286bc4e34773ebed
    role: target
  - path: data/pathways/tyrosine-biosynthesis.yaml
    sha256: 441df9779bbf64c1fd7919baac3baa4a3c332668848762ac2ae9f35b2217e967
    role: target
  - path: data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml
    sha256: e4debbe20da1e00f8b304bf272d96f676ac3e6e18e82994fce4f799665cb80fd
    role: target
  - path: data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml
    sha256: 03f1712aa87505464ec9d5f21e56adbce65401d3d554504b23c2fb1a8e603abb
    role: target
  - path: data/pathways/ump-biosynthesis-i.yaml
    sha256: 7360c32e29f0aa492c9b6e3c73b28ec1d1c152258e7efcfd540beb1394546f16
    role: target
  - path: data/pathways/uracil-degradation-iii.yaml
    sha256: ba58586f9b2eb4c29ff6ec99010da3618849dd29d4d023bf2ee82a1c155a4521
    role: target
  - path: data/pathways/urea-degradation-i.yaml
    sha256: 7c1b0c20488b920bff60f3bd07bedbd9e94d0649af2db5464169a4b5c76bb7b3
    role: target
  - path: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
    sha256: dc67a0bd30057f3eb9bebebf4498875a1f841f94e98059447b9b584909a8d43e
    role: target
  - path: data/pathways/valine-degradation.yaml
    sha256: fd0e23fb44bf92196391dfa4b8318fd5b8ae8136c8ebefde13a327348531ccc4
    role: target
  - path: data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml
    sha256: a5ebdc354315545ce4863cca5cbbb07880dc1f9629763a89cdaf93214c566434
    role: target
  - path: data/pathways/xylose-metabolism.yaml
    sha256: 61d17766dddacce9131e18c6f9b4678a7cc43fc304c00b151d2644b389e7be03
    role: target
  - path: data/pathways/zymosterol-biosynthesis.yaml
    sha256: 235d39afd5726b326c67763fb1da02075b60931d32b904050e577c7638cfa8a6
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
  - path: pages/downloads/nodes.tsv
    sha256: c895c1e930a8530f10fdb0471ee520f29a824a733f623b3048aa4930d27b4950
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: d7f44be9ac077c8eb700876ead551095c53ff8728cf8afe60cbee6307ee7dca5
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: f08c07c84685fc718a7465292efbf1546c4a684948ea363ef7524a4fcf6cd112
    role: context
scope:
  description: Full frozen-inventory record and category review of all 270 maintained
    pathway records in data/pathways/*.yaml at Git base 556074d91f600aa9e5ca97e0b4baef6d99513930.
  selection: All files matching data/pathways/*.yaml in CultureBotAI/PathwayMech.
  coverage: full
  population_size: 270
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: cf1fc7347b88c2ecb1139564b24bd64018e0fc65793314061f3cf22eed5fd5ef
    description: Raw SHA-256 file digest of data/pathways/2-phenylethanol-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: dc220e2a4d394750d7adc8bbaa1a7060082c28daeaa077fb6e9c1f94f2168173
    description: Raw SHA-256 file digest of data/pathways/4-aminobutyrate-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: e5f0507a6060dab794ffc5b0b11b125f23677a9d54c5b5440a07eb05c48a72a9
    description: Raw SHA-256 file digest of data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 62929187a92825274450afa61508d3139a7a88865848a3c49e07ca045a361a95
    description: Raw SHA-256 file digest of data/pathways/adenine-and-adenosine-salvage-i-escherichia-coli.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: d0a6942e6b36af20e66dc5546d62028b7f8239c6b126d13fa0548006cd2c331a
    description: Raw SHA-256 file digest of data/pathways/adenine-and-adenosine-salvage-ii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 3cd2f4ba0bdbd27028fad8814a024a16cdca397bc09764ecba2597826bfc0625
    description: Raw SHA-256 file digest of data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: b7f837be8676b08c9a8a0f417ca17a695664e8614b30e7847f4f7e05c845cbf6
    description: Raw SHA-256 file digest of data/pathways/adenosine-nucleotides-degradation-ii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 3840e82b7a5d9809e754222ac412b4321f3b99e73e085a3efdb9fbe6b402c9ef
    description: Raw SHA-256 file digest of data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 2e4943a2b36d529ef076e8a8ee561c120e65dc2e8e9c6c4452e2544a180645cd
    description: Raw SHA-256 file digest of data/pathways/adenosylcobinamide-gdp-salvage-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 6541509e6b50f5a7f462010541a7953ddcafa82c49959ffcbf7658a00b5e92fb
    description: Raw SHA-256 file digest of data/pathways/aerobic-glycerol-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: bd9c6c24677b6852478f2dd9e2846ade22d13dd722951a50acfb8b4516f1a8fb
    description: Raw SHA-256 file digest of data/pathways/allantoin-degradation-iv-anaerobic.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 4d8f1c7aee53baaf61885814f0e6870ae480759cb825037725bfa39395921ac2
    description: Raw SHA-256 file digest of data/pathways/allantoin-degradation-to-glyoxylate-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: adb71534db0d3300a6757b499b757a2d17f901910cc2417d99ad6f7f510fdc31
    description: Raw SHA-256 file digest of data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: fc436f537303f50121c472a4ece19249f3e6eb74d7304933fbafb37e04a61978
    description: Raw SHA-256 file digest of data/pathways/amino-sugar-superpathway.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 8c26f4bd655f7b13db25c70e817db9cb6b4232ccc941bf890bcbff54b25a180e
    description: Raw SHA-256 file digest of data/pathways/aspartate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 64aa47bf9da9d04d1e53d164f44d2ec4fb42adede455ea5dbbaa351917b398bc
    description: Raw SHA-256 file digest of data/pathways/assimilatory-sulfate-reduction.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 3f8bbb8eceaa4420fa822e87ce01cca6b9d1967908dc117628aba71f54030696
    description: Raw SHA-256 file digest of data/pathways/benzoate-degradation-i-aerobic.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: b2fc0cca6ac455fcc1820766caeb49a13beea64e49477bb774d3893e8bde3fff
    description: Raw SHA-256 file digest of data/pathways/benzoyl-coa-degradation-i-aerobic.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: f12c8f6ea8a7b774c0e596fec3c141de4a5ae60049aee7caec8018f2827aa2ee
    description: Raw SHA-256 file digest of data/pathways/beta-alanine-biosynthesis-iv.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: e7c9ab47f1cb65dd2ab0c467436da840f77e592fa9ca72293014350820cdb6af
    description: Raw SHA-256 file digest of data/pathways/carnitine-shuttle.yaml at
      frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: b7ab2d44d5694a1c1f56d15474c5d59ef66e7a0df36516e3325ea605b6c98c43
    description: Raw SHA-256 file digest of data/pathways/chitin-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: bf40044ef709ce95ef9faafef7a724efbdac7764cce18fdd263520f0593f1924
    description: Raw SHA-256 file digest of data/pathways/citrulline-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 7972d75389eb8cc316ff268467d6846351fc313850aa165ae51983bf87ed717f
    description: Raw SHA-256 file digest of data/pathways/cyanate-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 3d4489e00bc5bc9d7c5160d1ad3e7ed4a8c64e1722ef80b562740a6699febe5b
    description: Raw SHA-256 file digest of data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: acc8b361993a1db31e3bf253e05526b2998b7a91c0cf3b0e6628aaf530adb688
    description: Raw SHA-256 file digest of data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: c6bf14ce9e385df8aab07fb667d4aaecffcc53495d4b7372b02ea183f3898ccd
    description: Raw SHA-256 file digest of data/pathways/epoxysqualene-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 0439f963e2bcbb3e5e781df1338549c8963929747a721c72171cf533030344c5
    description: Raw SHA-256 file digest of data/pathways/ergosterol-biosynthesis-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527
    description: Raw SHA-256 file digest of data/pathways/ergothioneine-biosynthesis-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: d9df81a6d31bb732e2077798277c3b840c71596a482366603a93d22285aa6f84
    description: Raw SHA-256 file digest of data/pathways/ethanol-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 2da686ea5b62f2e43585967a23b1739d819a42dfcf19d0492cef55c944137120
    description: Raw SHA-256 file digest of data/pathways/fatty-acid-elongation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 2dcd1db7489ee7695bd99461bbee5c59064e15853b3ab3c413ea6b6118aefe36
    description: Raw SHA-256 file digest of data/pathways/fatty-acid-oxidation-pathway.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 6774526812ae134d049d2bd6f36941ff0d4453558aa68259a790e93149278d6a
    description: Raw SHA-256 file digest of data/pathways/folate-interconversions.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: e100dd411c9dc79be86d86d0b2ee76f9a0c228d673ecb4d4b8343b264cfaa054
    description: Raw SHA-256 file digest of data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 3d1cd470853a62a3373ee876e18ba1c49f1aec17b858acb929c49af89c4296ee
    description: Raw SHA-256 file digest of data/pathways/galactose-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 365e9c29df8a62dd3dd5d4a3a190e530f6e3beae4a8e159be04ec9e4a9a952ba
    description: Raw SHA-256 file digest of data/pathways/gluconeogenesis-i.yaml at
      frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: a518e6f42cee9d981d3a2876da0aa0ba9ed1612b90163f69cbbac1d8b1be28c0
    description: Raw SHA-256 file digest of data/pathways/glutamate-degradation-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: f8f06c4612ab0c7e38f3b46378454ba449231a013816902262ef6bddcc4cf2e4
    description: Raw SHA-256 file digest of data/pathways/glutathione-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 670795c76c89c998d015e40536a5aba90acccb1430e7b4649aef2f738bad5e1b
    description: Raw SHA-256 file digest of data/pathways/glutathione-glutaredoxin-redox-reaction.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 07b3f629ede35b4c42441295f1a3596a45ecbe776f9667633b3739c19bf742a6
    description: Raw SHA-256 file digest of data/pathways/glycerol-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 14313c0e3e8c3af451b0946c2b7d8d20545af13e8e27c5441cea62648899a524
    description: Raw SHA-256 file digest of data/pathways/glycine-cleavage.yaml at
      frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: fc91636aa102a87bcb65d173ff28b2acbb356ea67beb831e00e7a93d9ae52aa4
    description: Raw SHA-256 file digest of data/pathways/glycogen-catabolism.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: ce99470da6b66a527a1a7ffe4e46e059afa4af75496a8fca96f2831049410be6
    description: Raw SHA-256 file digest of data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 218feaba4c438ac1f7dff5765e5993153040fa1b0cc80b135440ad4ece8622ea
    description: Raw SHA-256 file digest of data/pathways/glyoxylate-assimilation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 65c619b8dfdd73062ad25ec9757f617da2a1a5739502ea44004be38e20897df0
    description: Raw SHA-256 file digest of data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 0b59dea7ec3eb1b01ba4b147d7532f7a395ef1d6d4128eb7f6be7e6a7cf8dcc3
    description: Raw SHA-256 file digest of data/pathways/heme-biosynthesis-i-aerobic.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: d72784cfaf3d8bf0e30f226b687177eaf269358a3317327aaa2ca12686c7b1ff
    description: Raw SHA-256 file digest of data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 548a2a31db077211819e31504c16f45e3ce711858ef8bafc992d142e50fe095a
    description: Raw SHA-256 file digest of data/pathways/homocysteine-and-cysteine-interconversion.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a
    description: Raw SHA-256 file digest of data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: add22f805f7a14a195c64a04e8b070f98c68626b30e768898e843213e7809fcc
    description: Raw SHA-256 file digest of data/pathways/inositol-phosphate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 50585e2d8674b369b4aa5271ba78c57c18ea7556138e16e55140d77c42aa935e
    description: Raw SHA-256 file digest of data/pathways/isoleucine-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: fa54ce93a653642b1fe2e0d9a1a02654ca238723ca6191a113c4f105ee1e07fe
    description: Raw SHA-256 file digest of data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 766ba43c30ea3c6568779592c48aa667dd38880b0023a091979df2705161bb16
    description: Raw SHA-256 file digest of data/pathways/l-asparagine-biosynthesis-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 7df30c94062629ad64c6ed7d137a637f904a1f7428d2b530fde78b78bc5df5c2
    description: Raw SHA-256 file digest of data/pathways/l-asparagine-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: acb2ce1d623b40d939a091bdbb3f9ce5d118a00aff3ebb873752ea323722de46
    description: Raw SHA-256 file digest of data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 5f4f330c4cee30dfe0ee244331adb501776c4e34c4f34811f428379cc99380e5
    description: Raw SHA-256 file digest of data/pathways/l-homocysteine-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 7f6375da56c7c53b27a336f385c71564c46ad7700e397063915bf6d6bdd18530
    description: Raw SHA-256 file digest of data/pathways/l-lysine-biosynthesis-iv.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 47625a371cab68efdf3f6e5deda9a982d8c309bda00f74827b03f0ae164ec49d
    description: Raw SHA-256 file digest of data/pathways/l-proline-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 5e003a44a1519e0a121a39819b334e57feee397e033d6db2ccec01399898daa7
    description: Raw SHA-256 file digest of data/pathways/l-threonine-degradation-iii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 435fa7b9e72cb017859159a7eb2ba3c078248638810272043fb23a22e27a67ea
    description: Raw SHA-256 file digest of data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 2ab3d77be1a21b236beb89a4b6c316c37f37bac708741ca496b552318ee96b7e
    description: Raw SHA-256 file digest of data/pathways/l-tyrosine-degradation-iii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: b11427a45a2f33becfda49dee1e4a636844f2c1d8febf8042e0e5daf10892d6d
    description: Raw SHA-256 file digest of data/pathways/leucine-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: dd4237f6d08801e661b2089644fcfb4c46fbbd1f65868d6853d51cae84293251
    description: Raw SHA-256 file digest of data/pathways/mannose-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: b73c407b4315efc45a30ed7121cb3797945cf0a4e86ab010bf5554b276b0e0a6
    description: Raw SHA-256 file digest of data/pathways/mannosylglycerate-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 2220e5618ddc3f993788bf772fd20c560350c3752885a9d7bb07eb7e297d7b3c
    description: Raw SHA-256 file digest of data/pathways/methionine-salvage-pathway.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 4e0655e6c340986dbb79f846b237550d6d793e7ae5781d576df4fbd6fa5f1ba1
    description: Raw SHA-256 file digest of data/pathways/methylglyoxal-catabolism.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 25a739d9e28a0dfaabc31f59bcaa98179ca4377f501a0f8a8a869039b786afdb
    description: Raw SHA-256 file digest of data/pathways/mevalonate-pathway.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: f1131912336cddeb1e79f27e4c0087e7188d97ad775583fbef65b7056086a5e5
    description: Raw SHA-256 file digest of data/pathways/myo-inositol-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: d9712d9291fdec2d7188a31d3eabf54dc198b880c996f39be3e5ada28c4684dc
    description: Raw SHA-256 file digest of data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: f41413a4a24571ece2b3e2d93490f778a1e8b9619c948fc4d6d1825db58d579a
    description: Raw SHA-256 file digest of data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 5714f5fe02a834e4b4836d61524835501f8eeaa6241d7da5be3f6242ca572d5a
    description: Raw SHA-256 file digest of data/pathways/nad-salvage-pathway-v.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 59d1a699b4e40ce680715afa958f8a659feae11b6b1786a5867f25733b83d36c
    description: Raw SHA-256 file digest of data/pathways/nicotine-degradation-ii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 3dcf719e913158bb23184d8ac68a8b6bce55f7f7ef0c69bee8c71a997d2cce2e
    description: Raw SHA-256 file digest of data/pathways/oleate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 47ad28d2b5f793ae9916a213e5b9522248d24e1415c32640f35c4908b6383b9e
    description: Raw SHA-256 file digest of data/pathways/palmitoleate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 0bba116121063c695033713548f5be6e79a09c875c08754785a86da58fdb7741
    description: Raw SHA-256 file digest of data/pathways/periplasmic-nad-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: d83bf9681c328942b0da0101d675687d2772f8017e236df3e813272fe59927d7
    description: Raw SHA-256 file digest of data/pathways/phenylalanine-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 5d41048d73ffc521a1d8aeaf79f9ff7ecffd80dffb6bd8915a2e7d512342b455
    description: Raw SHA-256 file digest of data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: f0fb3e3b3a323efe8e435ecff37c2e870f208f0e05dae61c4d417e61a8bac720
    description: Raw SHA-256 file digest of data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 9707f0bd75a5ade7eff2b25d0d8f8b7953b7749e2cdf2878156c09b9eb1d9d63
    description: Raw SHA-256 file digest of data/pathways/phosphatidylcholine-biosynthesis-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: c1d5c378d7fff51a6ba181570520d299898891226f4f00662d30b4be6313be9c
    description: Raw SHA-256 file digest of data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 6e81302207f8ac3a9d1eee0a63cf89b4bed0d6813339819ac96a2d44eec6194b
    description: Raw SHA-256 file digest of data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: f32a3b1cf37d1ee31de0900901860a17029ffe49f9d97deb4763f22d4fa580c7
    description: Raw SHA-256 file digest of data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 69eb1a16bb8baa5beccd8d281522534ff29afe828826aae39532063d6d131669
    description: Raw SHA-256 file digest of data/pathways/phospholipid-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: fb0b58b847d80f1a68aac342f1974cb6f51171da44ffe3285030454221af5c19
    description: Raw SHA-256 file digest of data/pathways/phospholipids-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 308c60f798bdc3dd8d004c3b5c214dcb9ab4f1ed2a174d169ef4d0958300d145
    description: Raw SHA-256 file digest of data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: ad122132b9b414dfdf4aff99f6b26b476cd0cdb98d9dacbfa85ea87f0ac269d6
    description: Raw SHA-256 file digest of data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 81526ec7fcedf14ead1ef9be33747b3560e74f4293e08ac6b6653cf6cb85eb1b
    description: Raw SHA-256 file digest of data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: d283eb6065c21162774b7c8267ab48ce82766a20ce93a37b182bf205e5c14bff
    description: Raw SHA-256 file digest of data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 9bb7972608c907fff78104cff4d93a54af3b5cffd6debfd9be9852d460dc297f
    description: Raw SHA-256 file digest of data/pathways/siroheme-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 7a59a97a06f5624a7c81b7aba90e909454eafbe37128e044b92fbd92bc82165b
    description: Raw SHA-256 file digest of data/pathways/spermidine-biosynthesis-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: abc49bff88359eabe59d05ae6ba0c1255e6937f6748d738220253b31d7744d3c
    description: Raw SHA-256 file digest of data/pathways/spermine-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: d75f7d359601e9967fc0f47c0bf369b0c2fbf4759014b6839131600cbf46ef22
    description: Raw SHA-256 file digest of data/pathways/sphingolipid-biosynthesis-yeast.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 3e20747a383ef29d995e2eee4b93040423b7d49b27843c0ec1987edcf6d82588
    description: Raw SHA-256 file digest of data/pathways/sulfate-activation-for-sulfonation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 4d0224dd2604fa1cce375b2afa12e614f22e304153734504e03da6e83c797585
    description: Raw SHA-256 file digest of data/pathways/superoxide-radicals-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: e98639698c8b4f68286adbeb7d68305a2b3aedcbd9a548bc06feccc91eaf2e39
    description: Raw SHA-256 file digest of data/pathways/tca-cycle-detailed.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: ce15c57307f843c5773b7e5515d09077f8c7c4ef1bbc588e1223d26b4e340690
    description: Raw SHA-256 file digest of data/pathways/tetrahydrofolate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: b9b73976e6a55b8a24abfd22a8e239733d2f7edd2a746e9e774d5df3fe5e5296
    description: Raw SHA-256 file digest of data/pathways/tetrapyrrole-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: b22273bb29300508a8446c84344cbe568a8ec56858c7d983dd951ba3fd04ca1e
    description: Raw SHA-256 file digest of data/pathways/thiamine-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/thioredoxin-pathway.yaml
    role: maintained pathway YAML
- target_id: gomodel:YeastPathways_THREOCAT2-PWY
  path: data/pathways/threonine-degradation.yaml
  label: threonine degradation (gomodel:YeastPathways_THREOCAT2-PWY)
  record_class: PathwayRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 23cce07f43a32645d175d779eabcdfa873a8bcb5d2f2c10171b06cd2fd7dd9ae
    description: Raw SHA-256 file digest of data/pathways/threonine-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: be0cf90a07906abd1aec303dc0871e33e97510e961d77e4dcd1649f7fb7f1264
    description: Raw SHA-256 file digest of data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 0ab6fcab3fa418433fffcd68cc992090145bf43c16c1132bddd1e9834a1a6a2f
    description: Raw SHA-256 file digest of data/pathways/triglyceride-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 08d5c4115a06db36842a5f384fc5d6f9c0a37f1fdf341d23286bc4e34773ebed
    description: Raw SHA-256 file digest of data/pathways/tryptophan-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 441df9779bbf64c1fd7919baac3baa4a3c332668848762ac2ae9f35b2217e967
    description: Raw SHA-256 file digest of data/pathways/tyrosine-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: e4debbe20da1e00f8b304bf272d96f676ac3e6e18e82994fce4f799665cb80fd
    description: Raw SHA-256 file digest of data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 03f1712aa87505464ec9d5f21e56adbce65401d3d554504b23c2fb1a8e603abb
    description: Raw SHA-256 file digest of data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: ba58586f9b2eb4c29ff6ec99010da3618849dd29d4d023bf2ee82a1c155a4521
    description: Raw SHA-256 file digest of data/pathways/uracil-degradation-iii.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 7c1b0c20488b920bff60f3bd07bedbd9e94d0649af2db5464169a4b5c76bb7b3
    description: Raw SHA-256 file digest of data/pathways/urea-degradation-i.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: dc67a0bd30057f3eb9bebebf4498875a1f841f94e98059447b9b584909a8d43e
    description: Raw SHA-256 file digest of data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: fd0e23fb44bf92196391dfa4b8318fd5b8ae8136c8ebefde13a327348531ccc4
    description: Raw SHA-256 file digest of data/pathways/valine-degradation.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: a5ebdc354315545ce4863cca5cbbb07880dc1f9629763a89cdaf93214c566434
    description: Raw SHA-256 file digest of data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 61d17766dddacce9131e18c6f9b4678a7cc43fc304c00b151d2644b389e7be03
    description: Raw SHA-256 file digest of data/pathways/xylose-metabolism.yaml at
      frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
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
    sha256: 235d39afd5726b326c67763fb1da02075b60931d32b904050e577c7638cfa8a6
    description: Raw SHA-256 file digest of data/pathways/zymosterol-biosynthesis.yaml
      at frozen Git commit 556074d91f600aa9e5ca97e0b4baef6d99513930.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/zymosterol-biosynthesis.yaml
    role: maintained pathway YAML
checks:
- check_id: validate
  name: Repository QC and closed-schema validation (just validate)
  status: passed
  required: true
  summary: Validated all 270 maintained pathway records against the closed LinkML
    schema, local identifier/label authority snapshots, 537 history records, 22,085
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
  - EV-QC-VALIDATE
  scope_note: Corpus-wide validation gate covering all 270 maintained records.
- check_id: test
  name: Full pytest test suite (just test)
  status: passed
  required: true
  summary: All 8,045 unit, schema, KGX, SSSOM, and record-review contract tests passed
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
  - EV-PYTEST
  scope_note: Repository-wide test suite covering all 270 maintained records and review
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
  - EV-RUFF
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
  - EV-GIT-DIFF
  scope_note: Worktree cleanliness check at frozen base commit.
- check_id: review-check
  name: Structured review bundle contract check (just review-check)
  status: passed
  required: true
  summary: All 197 pre-existing structured review bundles in reviews/structured/ passed
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
  - EV-REVIEW-CHECK
  scope_note: Validates all retained reviews/structured/ bundles against schema/record_review.yaml.
evidence:
- evidence_id: EV-QC-VALIDATE
  kind: validation
  reference: .venv/bin/pathwaymech-run-qc
  locator: stdout summary (270 pathway records, 537 history records, 22,085 evidence
    blocks, 33 source records)
  accessed_at: '2026-10-22T01:05:00Z'
  support: supports
  summary: 'Executed .venv/bin/pathwaymech-run-qc across the frozen working tree at
    556074d91f600aa9e5ca97e0b4baef6d99513930: validated 270 pathway records against
    the closed LinkML schema, verified all identifiers and labels against local authority
    snapshots, validated 537 history records and 22,085 evidence blocks, and confirmed
    pages/ synchrony.'
- evidence_id: EV-PYTEST
  kind: validation
  reference: .venv/bin/pytest -q
  locator: pytest suite execution across tests/
  accessed_at: '2026-10-22T01:35:00Z'
  support: supports
  summary: Executed the full pytest suite (8,045 passed, 3 skipped), verifying schema
    validation, identifier policy, KGX export, SSSOM export, source registry, and
    structured record-review contract invariants.
- evidence_id: EV-RUFF
  kind: validation
  reference: .venv/bin/ruff check --no-cache .
  locator: ruff check output
  accessed_at: '2026-10-22T01:06:00Z'
  support: supports
  summary: Executed .venv/bin/ruff check --no-cache . with exit code 0 (All checks
    passed).
- evidence_id: EV-GIT-DIFF
  kind: validation
  reference: git diff --check
  locator: git worktree at 556074d91f600aa9e5ca97e0b4baef6d99513930
  accessed_at: '2026-10-22T01:06:00Z'
  support: supports
  summary: Executed git diff --check with exit code 0; no whitespace errors or conflict
    markers.
- evidence_id: EV-REVIEW-CHECK
  kind: prior_review
  reference: reviews/structured/
  locator: 197 retained structured review bundles
  accessed_at: '2026-10-22T01:07:00Z'
  support: supports
  summary: Validated all 197 previously retained structured review bundles under reviews/structured/
    via scripts/record_review.py check; confirmed all prior findings on maintained
    data/pathways/*.yaml records were resolved and the only 2 open finding heads in
    historical bundles target withheld research/pathway_additions/ drafts.
- evidence_id: EV-CORPUS-INSPECTION
  kind: record_content
  reference: data/pathways/
  locator: 270 maintained pathway YAML files (7,652 participants, 1,591 reactions
    including 693 RHEA:* reactions, 14,322 mechanistic_edges)
  accessed_at: '2026-10-22T01:20:00Z'
  support: supports
  summary: 'Inspected all 270 maintained pathway records in data/pathways/*.yaml:
    100% declare valid pathway_type, 100% of 14,322 mechanistic_edges carry structured
    evidence blocks (20,959 edge-level evidence items; 22,085 total evidence blocks
    across records, steps, and edges), 100% of 693 RHEA:* reaction nodes declare explicit
    direction with zero cross-record direction conflicts, and zero duplicate xrefs
    exist across records.'
- evidence_id: EV-GLCMANNANAUT-PWY
  kind: record_content
  reference: data/pathways/amino-sugar-superpathway.yaml
  locator: lines 211-255 (reactions list in MetaCyc:GLCMANNANAUT-PWY)
  accessed_at: '2026-10-22T01:25:00Z'
  support: supports
  summary: 'In data/pathways/amino-sugar-superpathway.yaml (MetaCyc:GLCMANNANAUT-PWY),
    reactions[13] (BiGG:ACMANAptspp, N-acetyl-D-mannosamine transport via PTS  (periplasm))
    and 10 RHEA:* reactions (reactions[3..12]) omit category: molecular_activity while
    3 subpathway entries (MetaCyc:PWY0-1324, MetaCyc:GLUAMCAT-PWY, MetaCyc:GLYCOLYSIS
    at reactions[0..2]) explicitly declare category: pathway.'
  quote: "- id: BiGG:ACMANAptspp\n  label: N-acetyl-D-mannosamine transport via PTS\
    \  (periplasm)\n  direction: left_to_right"
  snapshot_sha256: fc436f537303f50121c472a4ece19249f3e6eb74d7304933fbafb37e04a61978
- evidence_id: EV-KGX-EXPORT
  kind: record_content
  reference: src/pathwaymech/kgx.py
  locator: lines 74-101 (_PREFIX_CATEGORIES and _node_category)
  accessed_at: '2026-10-22T01:26:00Z'
  support: supports
  summary: 'In src/pathwaymech/kgx.py, _PREFIX_CATEGORIES maps RHEA to biolink:BiochemicalReaction
    when reaction.category is None, whereas explicit category: molecular_activity
    maps via _PARTICIPANT_CATEGORIES to biolink:MolecularActivity; BiGG is absent
    from _PREFIX_CATEGORIES, so a BiGG reaction without category: molecular_activity
    falls back to DEFAULT_CATEGORY (biolink:NamedThing) with empty source_category.'
  quote: DEFAULT_CATEGORY = "biolink:NamedThing"
  snapshot_sha256: d7f44be9ac077c8eb700876ead551095c53ff8728cf8afe60cbee6307ee7dca5
- evidence_id: EV-NODES-TSV
  kind: record_content
  reference: pages/downloads/nodes.tsv
  locator: row BiGG:ACMANAptspp
  accessed_at: '2026-10-22T01:27:00Z'
  support: supports
  summary: 'In pages/downloads/nodes.tsv, BiGG:ACMANAptspp is exported with category
    biolink:NamedThing and empty source_category because reactions[13] in data/pathways/amino-sugar-superpathway.yaml
    omits category: molecular_activity.'
  quote: "BiGG:ACMANAptspp\tbiolink:NamedThing\tN-acetyl-D-mannosamine transport via\
    \ PTS  (periplasm)\t\t\tMetaCyc:GLCMANNANAUT-PWY\tPathwayMech"
  snapshot_sha256: c895c1e930a8530f10fdb0471ee520f29a824a733f623b3048aa4930d27b4950
- evidence_id: EV-MIXED-REACTION-CATEGORY-RECORDS
  kind: record_content
  reference: data/pathways/
  locator: '12 MetaCyc records: MetaCyc:CYANCAT-PWY, MetaCyc:GLCMANNANAUT-PWY, MetaCyc:PWY-1361,
    MetaCyc:PWY-2503, MetaCyc:PWY-5744, MetaCyc:PWY-5789, MetaCyc:PWY-6993, MetaCyc:PWY-7255,
    MetaCyc:PWY-7971, MetaCyc:PWY0-1471, MetaCyc:PWY0-41, MetaCyc:SALVADEHYPOX-PWY'
  accessed_at: '2026-10-22T01:28:00Z'
  support: supports
  summary: Across 12 maintained MetaCyc pathway records, reactions[*] entries mix
    explicit category declarations (molecular_activity or pathway) with 33 catalytic
    reaction entries (30 RHEA:*, 2 MetaCyc:RXN-*, 1 BiGG:ACMANAptspp) that omit category,
    producing mixed KGX node categories within the same pathway reaction graph.
assessments:
- assessment_id: ASSESS-IDENTITY-GROUNDING-ALL-270
  area: identity
  topic: Pathway identity, taxon grounding, and authority-verified participant/reaction
    CURIEs across all 270 maintained records
  outcome: supported
  summary: All 270 maintained pathway records in data/pathways/*.yaml denote coherent
    microbial pathways or signaling/virulence modules with authority-verified pathway
    IDs, NCBITaxon groundings, CHEBI/UniProt/ComplexPortal/GO/NCBITaxon participant
    CURIEs, and RHEA/MetaCyc/BiGG reaction identifiers verified against local authority
    snapshots.
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
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
  - EV-REVIEW-CHECK
  metrics:
  - name: maintained_pathway_records_reviewed
    value: 270.0
    unit: records
    definition: Count of maintained pathway YAML records in data/pathways/*.yaml inspected
      in full.
    denominator: 270
    minimum: 0.0
    maximum: 270.0
  - name: authority_identifier_verification_rate
    value: 100.0
    unit: percent
    definition: Percentage of maintained pathway records whose pathway, taxon, participant,
      and reaction identifiers pass local authority snapshot verification.
    denominator: 270
    minimum: 0.0
    maximum: 100.0
  dimensions:
  - name: corpus_scope
    value: full_maintained_inventory
    definition: All 270 maintained YAML records in data/pathways/*.yaml at frozen
      Git base 556074d91f600aa9e5ca97e0b4baef6d99513930.
    evidence_ids:
    - EV-CORPUS-INSPECTION
  - name: namespace_distribution
    value: MetaCyc:140, gomodel:86, WikiPathways:12, GO:10, PathBank:10, Reactome:6,
      KEGG:3, MIBiG:3
    definition: Distribution of primary pathway identifier prefixes across the 270
      maintained records.
    evidence_ids:
    - EV-CORPUS-INSPECTION
- assessment_id: ASSESS-CAUSAL-GRAPH-EVIDENCE-ALL-270
  area: graph
  topic: Causal graph connectivity, reaction directionality, and edge-level evidence
    across all 270 maintained records
  outcome: supported
  summary: All 270 maintained records contain connected participant-reaction-edge
    causal graphs (7,652 participants, 1,591 reactions including 693 RHEA:* reactions,
    14,322 mechanistic_edges) with 100% edge-level evidence coverage (20,959 edge-level
    evidence items; 22,085 total evidence blocks across records, steps, and edges),
    explicit direction on 100% of 693 RHEA:* reaction nodes, and zero cross-record
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
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
  - EV-PYTEST
  metrics:
  - name: mechanistic_edge_evidence_coverage
    value: 100.0
    unit: percent
    definition: Percentage of mechanistic_edges (14,322 / 14,322) carrying at least
      one valid structured evidence block.
    denominator: 14322
    minimum: 0.0
    maximum: 100.0
  - name: rhea_reaction_direction_coverage
    value: 100.0
    unit: percent
    definition: Percentage of RHEA:* reaction nodes (693 / 693) declaring an explicit
      direction enum value.
    denominator: 693
    minimum: 0.0
    maximum: 100.0
  dimensions:
  - name: evidence_tier
    value: authority_snapshot_and_cited_literature
    definition: Every mechanistic edge is backed by a verified database authority
      snapshot and/or primary literature PMID/DOI quote.
    evidence_ids:
    - EV-QC-VALIDATE
    - EV-CORPUS-INSPECTION
- assessment_id: ASSESS-REACTION-CATEGORY-CONCERN-12
  area: consistency
  topic: Within-record reaction category typing consistency and KGX node category
    export in 12 MetaCyc records
  outcome: concern
  summary: 'Twelve maintained MetaCyc records declare explicit category (molecular_activity
    or pathway) on a subset of their reactions[] entries while omitting category on
    33 sibling catalytic reaction entries (30 RHEA:*, 2 MetaCyc:RXN-*, 1 BiGG:ACMANAptspp).
    In MetaCyc:GLCMANNANAUT-PWY (data/pathways/amino-sugar-superpathway.yaml), omitting
    category: molecular_activity on BiGG:ACMANAptspp (reactions[13]) causes KGX export
    (pages/downloads/nodes.tsv) to assign fallback biolink:NamedThing with empty source_category
    instead of biolink:MolecularActivity.'
  target_ids:
  - MetaCyc:SALVADEHYPOX-PWY
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-41
  - MetaCyc:GLCMANNANAUT-PWY
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:PWY-7255
  - MetaCyc:PWY-5744
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6993
  - MetaCyc:PWY0-1471
  evidence_ids:
  - EV-GLCMANNANAUT-PWY
  - EV-KGX-EXPORT
  - EV-NODES-TSV
  - EV-MIXED-REACTION-CATEGORY-RECORDS
  metrics:
  - name: records_with_mixed_reaction_category_typing
    value: 12.0
    unit: records
    definition: Count of maintained pathway records where reactions[] mixes entries
      with explicit category and entries with category omitted.
    denominator: 270
    minimum: 0.0
    maximum: 270.0
  - name: reactions_missing_explicit_category_in_mixed_records
    value: 33.0
    unit: reactions
    definition: 'Count of catalytic reaction entries omitting category: molecular_activity
      inside the 12 mixed-typing records (out of 1,591 total reactions across all
      270 records).'
    denominator: 1591
    minimum: 0.0
    maximum: 1591.0
  dimensions:
  - name: kgx_export_impact
    value: BiGG:ACMANAptspp->biolink:NamedThing; 30 RHEA:* and 2 MetaCyc:RXN-*->biolink:BiochemicalReaction
      (empty source_category)
    definition: Downstream KGX node category and source_category effect in pages/downloads/nodes.tsv.
    evidence_ids:
    - EV-KGX-EXPORT
    - EV-NODES-TSV
findings:
- finding_id: F-STAGE4-001
  issue_key: amino-sugar-superpathway-bigg-reaction-missing-category
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: 'BiGG:ACMANAptspp reaction in MetaCyc:GLCMANNANAUT-PWY omits category: molecular_activity
    and exports as biolink:NamedThing'
  description: 'In data/pathways/amino-sugar-superpathway.yaml (MetaCyc:GLCMANNANAUT-PWY,
    superpathway of N-acetylglucosamine, N-acetylmannosamine and N-acetylneuraminate
    degradation), reactions[13] is BiGG:ACMANAptspp (N-acetyl-D-mannosamine transport
    via PTS  (periplasm)), which omits category: molecular_activity while 3 subpathway
    entries (MetaCyc:PWY0-1324, MetaCyc:GLUAMCAT-PWY, MetaCyc:GLYCOLYSIS at reactions[0..2])
    in the same reactions list declare category: pathway. Because ''BiGG'' is not
    in _PREFIX_CATEGORIES in src/pathwaymech/kgx.py, BiGG:ACMANAptspp falls back to
    DEFAULT_CATEGORY (''biolink:NamedThing'') with an empty source_category in pages/downloads/nodes.tsv
    instead of ''biolink:MolecularActivity'' (source_category=''molecular_activity'').'
  target_ids:
  - MetaCyc:GLCMANNANAUT-PWY
  field_paths:
  - data/pathways/amino-sugar-superpathway.yaml#reactions[13].category (BiGG:ACMANAptspp)
  evidence_ids:
  - EV-GLCMANNANAUT-PWY
  - EV-KGX-EXPORT
  - EV-NODES-TSV
  rule_id: CAUSAL_GRAPHS:reaction-category-typing
  native_severity: minor
  normalization_reason: 'Native minor representation defect maps directly to minor
    severity: pathway identity, stoichiometry, and edge evidence are valid, while
    adding category: molecular_activity to reactions[13] restores accurate biolink:MolecularActivity
    typing in KGX export.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/amino-sugar-superpathway.yaml
    role: maintained pathway YAML
  tags:
  - stage4-record-review
  - reaction-category
  - kgx-export
- finding_id: F-STAGE4-002
  issue_key: mixed-reaction-category-typing-in-maintained-pathways
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Twelve maintained MetaCyc pathway records mix explicit and omitted reaction
    category fields within reactions[]
  description: 'Across 12 maintained MetaCyc pathway records (MetaCyc:CYANCAT-PWY,
    MetaCyc:GLCMANNANAUT-PWY, MetaCyc:PWY-1361, MetaCyc:PWY-2503, MetaCyc:PWY-5744,
    MetaCyc:PWY-5789, MetaCyc:PWY-6993, MetaCyc:PWY-7255, MetaCyc:PWY-7971, MetaCyc:PWY0-1471,
    MetaCyc:PWY0-41, and MetaCyc:SALVADEHYPOX-PWY), reactions[] declares explicit
    category (molecular_activity or pathway) on a subset of entries while omitting
    category: molecular_activity on 33 sibling catalytic reaction entries (30 RHEA:*,
    2 MetaCyc:RXN-*, and 1 BiGG:ACMANAptspp). This causes catalytic reactions within
    the same pathway graph to export with mixed Biolink categories (biolink:MolecularActivity
    with source_category=molecular_activity vs biolink:BiochemicalReaction or biolink:NamedThing
    with empty source_category) in pages/downloads/nodes.tsv.'
  target_ids:
  - MetaCyc:SALVADEHYPOX-PWY
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-41
  - MetaCyc:GLCMANNANAUT-PWY
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:PWY-7255
  - MetaCyc:PWY-5744
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6993
  - MetaCyc:PWY0-1471
  field_paths:
  - data/pathways/adenosine-nucleotides-degradation-ii.yaml#reactions[1].category
    (RHEA:29376)
  - data/pathways/adenosine-nucleotides-degradation-ii.yaml#reactions[2].category
    (RHEA:24409)
  - data/pathways/adenosine-nucleotides-degradation-ii.yaml#reactions[3].category
    (RHEA:27647)
  - data/pathways/adenosine-nucleotides-degradation-ii.yaml#reactions[4].category
    (RHEA:24671)
  - data/pathways/adenosine-nucleotides-degradation-ii.yaml#reactions[5].category
    (RHEA:16670)
  - data/pathways/adenosylcobinamide-gdp-salvage-i.yaml#reactions[1].category (RHEA:57693)
  - data/pathways/allantoin-degradation-iv-anaerobic.yaml#reactions[6].category (RHEA:15650)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[3].category (RHEA:67737)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[4].category (RHEA:67741)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[5].category (RHEA:23297)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[6].category (RHEA:25254)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[7].category (RHEA:25259)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[8].category (RHEA:22937)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[9].category (RHEA:12173)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[10].category (RHEA:28989)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[11].category (RHEA:49241)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[12].category (RHEA:23881)
  - data/pathways/amino-sugar-superpathway.yaml#reactions[13].category (BiGG:ACMANAptspp)
  - data/pathways/benzoate-degradation-i-aerobic.yaml#reactions[5].category (RHEA:12634)
  - data/pathways/benzoate-degradation-i-aerobic.yaml#reactions[6].category (RHEA:11561)
  - data/pathways/benzoyl-coa-degradation-i-aerobic.yaml#reactions[0].category (RHEA:48313)
  - data/pathways/benzoyl-coa-degradation-i-aerobic.yaml#reactions[1].category (RHEA:48309)
  - data/pathways/benzoyl-coa-degradation-i-aerobic.yaml#reactions[2].category (RHEA:25392)
  - data/pathways/benzoyl-coa-degradation-i-aerobic.yaml#reactions[4].category (RHEA:76649)
  - data/pathways/benzoyl-coa-degradation-i-aerobic.yaml#reactions[5].category (RHEA:34852)
  - data/pathways/benzoyl-coa-degradation-i-aerobic.yaml#reactions[6].category (RHEA:19483)
  - data/pathways/cyanate-degradation.yaml#reactions[1].category (RHEA:15650)
  - data/pathways/ergothioneine-biosynthesis-i.yaml#reactions[5].category (MetaCyc:RXN-18089)
  - data/pathways/ergothioneine-biosynthesis-i.yaml#reactions[6].category (MetaCyc:RXN-15804)
  - data/pathways/glyoxylate-assimilation.yaml#reactions[0].category (RHEA:10750)
  - data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml#reactions[0].category
    (RHEA:10750)
  - data/pathways/nicotine-degradation-ii.yaml#reactions[1].category (RHEA:75416)
  - data/pathways/uracil-degradation-iii.yaml#reactions[3].category (RHEA:15650)
  evidence_ids:
  - EV-MIXED-REACTION-CATEGORY-RECORDS
  - EV-GLCMANNANAUT-PWY
  - EV-KGX-EXPORT
  - EV-NODES-TSV
  rule_id: CAUSAL_GRAPHS:within-record-reaction-category-consistency
  native_severity: minor
  normalization_reason: 'Native minor consistency defect maps directly to minor severity:
    RHEA:* and MetaCyc:RXN-* reactions remain valid under prefix fallback in kgx.py,
    but standardizing explicit category: molecular_activity across all 33 omitted
    catalytic reaction entries in these 12 records makes within-record reaction typing
    and KGX node export uniform.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosine-nucleotides-degradation-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosylcobinamide-gdp-salvage-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/allantoin-degradation-iv-anaerobic.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/amino-sugar-superpathway.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/benzoate-degradation-i-aerobic.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/benzoyl-coa-degradation-i-aerobic.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/cyanate-degradation.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-assimilation.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nicotine-degradation-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/uracil-degradation-iii.yaml
    role: maintained pathway YAML
  tags:
  - stage4-record-review
  - reaction-category
  - consistency
actions:
- action_id: A-STAGE4-001
  description: 'Add category: molecular_activity to reactions[13] (BiGG:ACMANAptspp)
    in data/pathways/amino-sugar-superpathway.yaml (MetaCyc:GLCMANNANAUT-PWY), record
    a curation history entry under history/records/amino-sugar-superpathway/, and
    regenerate pages/ so BiGG:ACMANAptspp exports as biolink:MolecularActivity in
    pages/downloads/nodes.tsv.'
  finding_ids:
  - F-STAGE4-001
  target_ids:
  - MetaCyc:GLCMANNANAUT-PWY
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/amino-sugar-superpathway.yaml
    role: maintained pathway YAML
  acceptance_checks:
  - 'data/pathways/amino-sugar-superpathway.yaml declares category: molecular_activity
    on BiGG:ACMANAptspp.'
  - pages/downloads/nodes.tsv lists biolink:MolecularActivity and source_category=molecular_activity
    for BiGG:ACMANAptspp.
  - .venv/bin/pathwaymech-run-qc and .venv/bin/pytest -q exit 0.
- action_id: A-STAGE4-002
  description: 'Add explicit category: molecular_activity to all 33 catalytic reaction
    entries (30 RHEA:*, 2 MetaCyc:RXN-*, 1 BiGG:ACMANAptspp) that currently omit category
    across the 12 mixed-typing MetaCyc pathway records, record curation history entries
    under history/records/, and regenerate pages/ artifacts.'
  finding_ids:
  - F-STAGE4-002
  target_ids:
  - MetaCyc:SALVADEHYPOX-PWY
  - MetaCyc:PWY-7971
  - MetaCyc:PWY0-41
  - MetaCyc:GLCMANNANAUT-PWY
  - MetaCyc:PWY-2503
  - MetaCyc:PWY-1361
  - MetaCyc:CYANCAT-PWY
  - MetaCyc:PWY-7255
  - MetaCyc:PWY-5744
  - MetaCyc:PWY-5789
  - MetaCyc:PWY-6993
  - MetaCyc:PWY0-1471
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosine-nucleotides-degradation-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosylcobinamide-gdp-salvage-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/allantoin-degradation-iv-anaerobic.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/amino-sugar-superpathway.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/benzoate-degradation-i-aerobic.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/benzoyl-coa-degradation-i-aerobic.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/cyanate-degradation.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ergothioneine-biosynthesis-i.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-assimilation.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/nicotine-degradation-ii.yaml
    role: maintained pathway YAML
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/uracil-degradation-iii.yaml
    role: maintained pathway YAML
  acceptance_checks:
  - 'Zero maintained records in data/pathways/*.yaml mix catalytic reactions with
    and without category: molecular_activity.'
  - All 12 updated pathway records have matching history/records/<slug>/*.yaml provenance
    files.
  - .venv/bin/pathwaymech-run-qc, .venv/bin/pytest -q, and .venv/bin/python scripts/record_review.py
    check exit 0.
  depends_on:
  - A-STAGE4-001
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
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
- action: retain
  target_ids:
  - KEGG:M00008
  - KEGG:M00373
  - KEGG:M00374
  rationale: Retain all 3 maintained KEGG:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against KEGG authority snapshots and
    docs/HARMONIZATION.md.
  evidence_ids:
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
- action: retain
  target_ids:
  - MIBiG:BGC0000829
  - MIBiG:BGC0000852
  - MIBiG:BGC0002072
  rationale: Retain all 3 maintained MIBiG:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against MIBiG authority snapshots and
    docs/HARMONIZATION.md.
  evidence_ids:
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
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
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
- action: retain
  target_ids:
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
  rationale: Retain all 10 maintained PathBank:* pathway records as distinct, non-duplicate
    source-scoped pathway definitions verified against PathBank authority snapshots
    and docs/HARMONIZATION.md.
  evidence_ids:
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
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
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
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
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
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
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
- action: retain
  target_ids:
  - MetaCyc:P121-PWY
  - MetaCyc:PWY-6609
  - PathBank:SMP0002081
  - PathBank:SMP0002083
  rationale: 'Retain MetaCyc:P121-PWY, PathBank:SMP0002081, PathBank:SMP0002083, and
    MetaCyc:PWY-6609 as separate maintained records per docs/HARMONIZATION.md: PathBank:SMP0002081
    models the Escherichia coli K-12 BioPAX PW002069 adenine/adenosine salvage network
    with explicit subcellular transport and ammonia lyase steps, whereas MetaCyc:P121-PWY,
    PathBank:SMP0002083, and MetaCyc:PWY-6609 represent distinct authority-scoped
    pathway boundaries and step topologies.'
  evidence_ids:
  - EV-QC-VALIDATE
  - EV-CORPUS-INSPECTION
limitations:
- 'Twelve maintained MetaCyc pathway records exhibit mixed within-record reaction
  category typing (33 catalytic reaction entries omit category: molecular_activity
  while sibling entries in the same reactions[] list declare category), including
  BiGG:ACMANAptspp in MetaCyc:GLCMANNANAUT-PWY which falls back to biolink:NamedThing
  in pages/downloads/nodes.tsv; these are recorded as open minor findings F-STAGE4-001
  and F-STAGE4-002 for Stage 5 remediation.'
- Verification of literature-backed evidence blocks relied on the repository's local
  authority snapshots and curated evidence quotes/abstracts at frozen commit 556074d91f600aa9e5ca97e0b4baef6d99513930
  without re-fetching external publisher full texts over the network.
notes:
- Per Cycle 1 Stage 4 (record_review) workflow policy, no edits were made to data/pathways/*.yaml
  during this stage; open findings F-STAGE4-001 and F-STAGE4-002 are carried forward
  to Stage 5 (resolve_review_findings).
tags:
- mech-goal-sequence-20261019
- cycle-1
- stage-4
- frozen-inventory
- full-corpus-review
```
