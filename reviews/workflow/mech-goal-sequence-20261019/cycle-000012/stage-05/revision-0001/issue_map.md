# Cycle 12 Stage 5 (`resolve_review_findings`) — Issue Map & Root-Cause Grouping

## 1. Predecessor Evidence & Review Linkage

- **Run / Cycle / Stage**: `mech-goal-sequence-20261019` / Cycle `12` / Stage `5` (`resolve_review_findings`)
- **Git base SHA**: `300d28486e8bf92557723036cb87e499dcb481ea`
- **Predecessor workflow evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-04/revision-0001/evidence.yaml` (SHA-256 `87b916a21dc63c237a81de44bf63f4cf0b96af92c1a0d9ae6c82762402e8f0ee`)
- **Predecessor structured review**: `reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml` (`review_id: 20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review`, SHA-256 `3b48a17bdc81244e86e7b367348c9f4d42e284b93f4122b5d52b76e47df089f2`)
- **Successor structured review**: `reviews/structured/20261105T161000Z-cycle12-stage5-resolve-review-findings/review.yaml` (`review_id: 20261105T161000Z-cycle12-stage5-resolve-review-findings`, SHA-256 `858febc647f5747c1d2b25a09a5da87d593b46999d3ff51abd0bccf7e405a281`)

## 2. Root-Cause Grouping & GitHub Issue Deduplication

Before creating any GitHub issue, open and closed issues in `CultureBotAI/PathwayMech` were searched via `gh issue list --repo CultureBotAI/PathwayMech --state all --limit 100`. Prior Stage 5 reference-hygiene issues (`#724`, `#745`, `#753`, `#762`, `#771`, `#781`, `#791`) were closed and scoped to earlier record cohorts. Neither `F-C12S4-001` nor `F-C12S4-002` duplicated an open issue. Because both findings share a single root cause and repair ownership—legacy Reactome BioPAX, WikiPathways GPML, and MIBiG importer reference-metadata omissions (`references[].url` omitted across `47` entries in `10` records and placeholder `references[].title` strings across `13` entries in `4` of those same records)—they were grouped into a single root-cause remediation group (`G-C12S5-001`) and tracked under new GitHub issue [#798](https://github.com/CultureBotAI/PathwayMech/issues/798).

| Group ID | Predecessor Findings | Rule ID(s) | Issue Key(s) | GitHub Issue | Target Records | Total Field Updates & Dispositions | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `G-C12S5-001` | `F-C12S4-001`, `F-C12S4-002` | `CURATION:reference-entries-include-resolvable-url`, `CURATION:no-placeholder-reference-titles` | `missing-reference-urls-10-records`, `placeholder-reactome-and-mibig-reference-titles-4-records` | [#798](https://github.com/CultureBotAI/PathwayMech/issues/798) | `Reactome:R-MTU-868688`, `Reactome:R-MTU-879299`, `Reactome:R-MTU-936721`, `Reactome:R-MTU-936635`, `Reactome:R-MTU-936654`, `Reactome:R-MTU-879325`, `WikiPathways:WP5060`, `WikiPathways:WP5587`, `MIBiG:BGC0002072`, `WikiPathways:WP296` | `47` `references[].url` + `13` `references[].title` updated (`60` YAML field edits across `10` records) | `resolved` |

## 3. Record-Level Curation Ledger (`G-C12S5-001`)

| Target ID | File Path | Pre-Curation SHA-256 | Post-Curation SHA-256 | Curation History Path | Updated Fields |
| --- | --- | --- | --- | --- | --- |
| `Reactome:R-MTU-868688` | `data/pathways/mycobacterium-trehalose-biosynthesis.yaml` | `7c3915665fbbe8cfe1d695354f471a1c832ccf972d2302c0910a96144ec1cd49` | `7e96c46849b5d4438f87c2e7ef8468ddd9e3736c90f1f56fbdc9674689d88330` | `history/records/mycobacterium-trehalose-biosynthesis/2026-11-05T160500Z-antigravity-b4812a.yaml` | `17` (`references[0].url, references[1].url, references[2].url, references[3].url, references[4].url, references[5].url, references[6].url, references[7].url, references[8].url, references[9].url, references[10].url, references[11].url, references[0].title, references[1].title, references[2].title, references[3].title, references[4].title`) |
| `Reactome:R-MTU-879299` | `data/pathways/mycothiol-biosynthesis.yaml` | `35dfb77de4fcc447aeb649bb478c6a840e78ab39f5921469a154ec3768c32f4f` | `ae877d4a8ec7fabe728669c180807547dfe9617c4479d10c3bf60a9229d5b05c` | `history/records/mycothiol-biosynthesis/2026-11-05T160500Z-antigravity-dbf8da.yaml` | `18` (`references[0].url, references[1].url, references[2].url, references[3].url, references[4].url, references[5].url, references[6].url, references[7].url, references[8].url, references[9].url, references[10].url, references[11].url, references[0].title, references[1].title, references[2].title, references[3].title, references[4].title, references[5].title`) |
| `Reactome:R-MTU-936721` | `data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml` | `cdbfd2cae9e281dc1a1722f65b2f019841b0a84b6e53e755bce049d495ed7f44` | `478a9c0093653374b69578b03b26cfb9a8f10c33c62b9934200d06f1a456ca56` | `history/records/mycobacterium-cysteine-synthesis-from-o-acetylserine/2026-11-05T160500Z-antigravity-c71bf1.yaml` | `8` (`references[0].url, references[1].url, references[2].url, references[3].url, references[4].url, references[5].url, references[6].url, references[7].url`) |
| `Reactome:R-MTU-936635` | `data/pathways/mycobacterium-sulfate-assimilation.yaml` | `aecb344e6ec330b48884cafd9bab879f5e3c623f66e315d90ad93910da12f931` | `94599e5b5a0d341ad2a29eb69b68ca48d73d2d228ca6a862ea776e61ab3fe01a` | `history/records/mycobacterium-sulfate-assimilation/2026-11-05T160500Z-antigravity-a67be4.yaml` | `5` (`references[0].url, references[1].url, references[2].url, references[3].url, references[4].url`) |
| `Reactome:R-MTU-936654` | `data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml` | `99b0c6d3e04ab2d3c310bbe8099cd5fa716f251632e5320ba83444bd7ebff82d` | `14e4d0dacc4c2e3e0b5e2bf0db5bb11045fc694a27dea62d5716772898cea9ba` | `history/records/mycobacterium-cysteine-synthesis-from-o-phosphoserine/2026-11-05T160500Z-antigravity-a4451a.yaml` | `3` (`references[0].url, references[1].url, references[2].url`) |
| `Reactome:R-MTU-879325` | `data/pathways/mycothiol-catabolism.yaml` | `9d1f2496015cee969712712da363456ac0cac63dcd5cb46cfa5ace763f8388b1` | `b9f168d7310502c8c1ec6fe29fef5e03b42e3805bd813348d950cd185f845ec7` | `history/records/mycothiol-catabolism/2026-11-05T160500Z-antigravity-4d257f.yaml` | `3` (`references[0].url, references[1].url, references[0].title`) |
| `WikiPathways:WP5060` | `data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml` | `41137e969f7960cddb59b6452079b9424b87b0bfaa8402172969c230965cb36a` | `6fa7c3486318e3630b693c3f0ce67176121c52ab99d04e3e8f3db6f095d1a6de` | `history/records/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways/2026-11-05T160500Z-antigravity-97aabe.yaml` | `2` (`references[0].url, references[1].url`) |
| `WikiPathways:WP5587` | `data/pathways/2-phenylethanol-biosynthesis.yaml` | `70936b88da1b369d40b0b68205cc3b31ab67df9df7b003aa0fad049594128798` | `a7a5e63709be01fb1d78d38ebf908878e008f7c8c8a6c2fafd51fbd67fc1782c` | `history/records/2-phenylethanol-biosynthesis/2026-11-05T160500Z-antigravity-f849f0.yaml` | `1` (`references[0].url`) |
| `MIBiG:BGC0002072` | `data/pathways/linearmycin-biosynthetic-gene-cluster.yaml` | `a5a908285f06357add5292777ea7be2226263c1448097361f9b3d87be0001cbe` | `8cae725a5c0caf991a2bc6e2bf5d53e9e2910816d66bdd16dba29e59ba6217cc` | `history/records/linearmycin-biosynthetic-gene-cluster/2026-11-05T160500Z-antigravity-36b800.yaml` | `2` (`references[0].url, references[0].title`) |
| `WikiPathways:WP296` | `data/pathways/tca-cycle-detailed.yaml` | `c574f799eef6b8b793decf52b1934a9f65ddac42893bb56ed5ed9d4134f837fe` | `f13cac35b226c3a2780ac349308cd749e47592d4517c81de6d67bd2a8056f1b4` | `history/records/tca-cycle-detailed/2026-11-05T160500Z-antigravity-5a803c.yaml` | `1` (`references[0].url`) |

## 4. Field-Level Remediation & Disposition Details

### 4.1 `F-C12S4-001` (`10` Pathway Records — `47` `references[].url` updates)

| Pathway ID | Field Path | Reference ID | Before (`url`) | After (Canonical Resolvable URL) |
| --- | --- | --- | --- | --- |
| `Reactome:R-MTU-868688` | `references[0].url` | `Reactome:R-MTU-868622` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-868622` |
| `Reactome:R-MTU-868688` | `references[1].url` | `Reactome:R-MTU-868608` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-868608` |
| `Reactome:R-MTU-868688` | `references[2].url` | `Reactome:R-MTU-868709` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-868709` |
| `Reactome:R-MTU-868688` | `references[3].url` | `Reactome:R-MTU-868658` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-868658` |
| `Reactome:R-MTU-868688` | `references[4].url` | `Reactome:R-MTU-868657` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-868657` |
| `Reactome:R-MTU-868688` | `references[5].url` | `PMID:10658666` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/10658666/` |
| `Reactome:R-MTU-868688` | `references[6].url` | `PMID:12473104` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/12473104/` |
| `Reactome:R-MTU-868688` | `references[7].url` | `PMID:15158675` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/15158675/` |
| `Reactome:R-MTU-868688` | `references[8].url` | `PMID:19177348` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/19177348/` |
| `Reactome:R-MTU-868688` | `references[9].url` | `PMID:15703182` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/15703182/` |
| `Reactome:R-MTU-868688` | `references[10].url` | `PMID:12626396` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/12626396/` |
| `Reactome:R-MTU-868688` | `references[11].url` | `PMID:15901732` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/15901732/` |
| `Reactome:R-MTU-879299` | `references[0].url` | `Reactome:R-MTU-879331` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-879331` |
| `Reactome:R-MTU-879299` | `references[1].url` | `Reactome:R-MTU-879298` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-879298` |
| `Reactome:R-MTU-879299` | `references[2].url` | `Reactome:R-MTU-879274` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-879274` |
| `Reactome:R-MTU-879299` | `references[3].url` | `Reactome:R-MTU-879327` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-879327` |
| `Reactome:R-MTU-879299` | `references[4].url` | `Reactome:R-MTU-879319` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-879319` |
| `Reactome:R-MTU-879299` | `references[5].url` | `Reactome:R-MTU-879248` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-879248` |
| `Reactome:R-MTU-879299` | `references[6].url` | `PMID:14763976` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/14763976/` |
| `Reactome:R-MTU-879299` | `references[7].url` | `PMID:18390549` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/18390549/` |
| `Reactome:R-MTU-879299` | `references[8].url` | `PMID:20167072` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/20167072/` |
| `Reactome:R-MTU-879299` | `references[9].url` | `PMID:14556638` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/14556638/` |
| `Reactome:R-MTU-879299` | `references[10].url` | `PMID:12033919` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/12033919/` |
| `Reactome:R-MTU-879299` | `references[11].url` | `PMID:12375100` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/12375100/` |
| `Reactome:R-MTU-936721` | `references[0].url` | `PMID:12072441` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/12072441/` |
| `Reactome:R-MTU-936721` | `references[1].url` | `PMID:16008502` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/16008502/` |
| `Reactome:R-MTU-936721` | `references[2].url` | `PMID:17644602` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/17644602/` |
| `Reactome:R-MTU-936721` | `references[3].url` | `PMID:15917234` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/15917234/` |
| `Reactome:R-MTU-936721` | `references[4].url` | `PMID:17567578` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/17567578/` |
| `Reactome:R-MTU-936721` | `references[5].url` | `PMID:16436075` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/16436075/` |
| `Reactome:R-MTU-936721` | `references[6].url` | `PMID:19376862` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/19376862/` |
| `Reactome:R-MTU-936721` | `references[7].url` | `PMID:17970225` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/17970225/` |
| `Reactome:R-MTU-936635` | `references[0].url` | `PMID:11929522` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/11929522/` |
| `Reactome:R-MTU-936635` | `references[1].url` | `PMID:15184554` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/15184554/` |
| `Reactome:R-MTU-936635` | `references[2].url` | `PMID:15615729` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/15615729/` |
| `Reactome:R-MTU-936635` | `references[3].url` | `PMID:18454554` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/18454554/` |
| `Reactome:R-MTU-936635` | `references[4].url` | `PMID:17970225` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/17970225/` |
| `Reactome:R-MTU-936654` | `references[0].url` | `PMID:16104727` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/16104727/` |
| `Reactome:R-MTU-936654` | `references[1].url` | `PMID:18842002` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/18842002/` |
| `Reactome:R-MTU-936654` | `references[2].url` | `PMID:18799456` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/18799456/` |
| `Reactome:R-MTU-879325` | `references[0].url` | `Reactome:R-MTU-879281` | `(omitted)` | `https://reactome.org/content/detail/R-MTU-879281` |
| `Reactome:R-MTU-879325` | `references[1].url` | `PMID:14556638` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/14556638/` |
| `WikiPathways:WP5060` | `references[0].url` | `PMID:31296364` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/31296364/` |
| `WikiPathways:WP5060` | `references[1].url` | `PMID:18266853` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/18266853/` |
| `WikiPathways:WP5587` | `references[0].url` | `PMID:40724265` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/40724265/` |
| `MIBiG:BGC0002072` | `references[0].url` | `PMID:29348524` | `(omitted)` | `https://pubmed.ncbi.nlm.nih.gov/29348524/` |
| `WikiPathways:WP296` | `references[0].url` | `CHEBI:30744` | `(omitted)` | `https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:30744` |

### 4.2 `F-C12S4-002` (`4` Pathway Records — `13` `references[].title` updates)

| Pathway ID | Field Path | Reference ID | Before (Placeholder Title) | After (Verified Descriptive Reaction / Article Title) |
| --- | --- | --- | --- | --- |
| `Reactome:R-MTU-868688` | `references[0].title` | `Reactome:R-MTU-868622` | `Reactome reaction R-MTU-868622` | `Glucose is transferred from UDP-glucose onto glucose-6-phosphate (Reactome:R-MTU-868622)` |
| `Reactome:R-MTU-868688` | `references[1].title` | `Reactome:R-MTU-868608` | `Reactome reaction R-MTU-868608` | `Trehalose-6-phosphate is hydrolyzed to trehalose (Reactome:R-MTU-868608)` |
| `Reactome:R-MTU-868688` | `references[2].title` | `Reactome:R-MTU-868709` | `Reactome reaction R-MTU-868709` | `TreS interconverts trehalose and alpha-maltose (physiological trehalose consumption) (Reactome:R-MTU-868709)` |
| `Reactome:R-MTU-868688` | `references[3].title` | `Reactome:R-MTU-868658` | `Reactome reaction R-MTU-868658` | `1,4-alpha-glucan is converted to glucanotrehalose (Reactome:R-MTU-868658)` |
| `Reactome:R-MTU-868688` | `references[4].title` | `Reactome:R-MTU-868657` | `Reactome reaction R-MTU-868657` | `Glucanotrehalose is hydrolyzed to 1,4-alpha-glucan and trehalose (Reactome:R-MTU-868657)` |
| `Reactome:R-MTU-879299` | `references[0].title` | `Reactome:R-MTU-879331` | `Reactome reaction R-MTU-879331` | `glucose-6-phosphate is converted to inositol-1-phosphate (Reactome:R-MTU-879331)` |
| `Reactome:R-MTU-879299` | `references[1].title` | `Reactome:R-MTU-879298` | `Reactome reaction R-MTU-879298` | `acetylglucosamine is transferred from UDP-GlcNAc onto inositol-1-phosphate (Reactome:R-MTU-879298)` |
| `Reactome:R-MTU-879299` | `references[2].title` | `Reactome:R-MTU-879274` | `Reactome reaction R-MTU-879274` | `acetylglucosamine-inositol-phosphate is dephosphorylated (Reactome:R-MTU-879274)` |
| `Reactome:R-MTU-879299` | `references[3].title` | `Reactome:R-MTU-879327` | `Reactome reaction R-MTU-879327` | `acetylglucosamine-inositol is deacetylated by Mca (Reactome:R-MTU-879327)` |
| `Reactome:R-MTU-879299` | `references[4].title` | `Reactome:R-MTU-879319` | `Reactome reaction R-MTU-879319` | `glucosaminyl-inositol and cysteine are ligated to desacetylmycothiol (Reactome:R-MTU-879319)` |
| `Reactome:R-MTU-879299` | `references[5].title` | `Reactome:R-MTU-879248` | `Reactome reaction R-MTU-879248` | `desacetylmycothiol is acetylated to mycothiol using acetyl-CoA (Reactome:R-MTU-879248)` |
| `Reactome:R-MTU-879325` | `references[0].title` | `Reactome:R-MTU-879281` | `Reactome reaction R-MTU-879281` | `Mca hydrolyzes mycothiol S-conjugates to mercapturic-acid conjugates and glucosaminyl-inositol (Reactome:R-MTU-879281)` |
| `MIBiG:BGC0002072` | `references[0].title` | `PMID:29348524` | `MIBiG literature reference PMID:29348524` | `Linearmycins are lytic membrane-targeting antibiotics` |
