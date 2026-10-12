Stable finding key: `nad-nadp-cross-study-locator`

Independent scientific review found a minor source-ownership defect in edge `nad-041` of the NAD phosphorylation/dephosphorylation candidate (`MetaCyc:NADPHOS-DEPHOS-PWY`, target SHA-256 `c2fec44e8c4f9a10f3ba96148a88afd7f3a16c25ac075167286bb81ef975f503`). Its single PMID:11488932 evidence assertion combines the 2001 NADP assay results with a 1987 no-significant-effect contrast. The selected 2001 primary rendering lines L253–L264 contain Table 5 only; PMID:3025169 does not own evidence on this edge. The exact reviewed bytes are now sealed in the author packet.

Root independently read that retained 2001 table (rendering bundle SHA-256 `5f38b08bbd3b4f48a24799f1e4587022c20879925643afa899c0f9eec077c8d5`): NADP at 0.050 and 0.100 mM gives 83% and 79% relative activity. The independent reviewer identifies the separate 1987 evidence in PDF page 2, Table 2 and adjacent text (whole PDF SHA-256 `e23a001f6a149cc59e705caf30bbd5def870282395f10ae1b115e97812b53253`). This is an evidence-attribution gap; neither the contrast nor the graph should be discarded to avoid the correction.

Acceptance criteria:
- Limit the existing PMID:11488932 assertion to the 2001 findings it supports.
- Add separately scoped PMID:3025169 evidence with its exact page/table/text locator.
- Preserve the 2001 construct qualifier and distinguish the 1987 preparation and conditions; retain graph IDs, endpoints and sign.
- Preserve the immutable original author packet, update evidence accounting in a successor, and obtain independent verification against the final exact target.

The full independent review is still underway. No maintained NAD record, canonical build, final scientific acceptance or issue resolution is claimed.
