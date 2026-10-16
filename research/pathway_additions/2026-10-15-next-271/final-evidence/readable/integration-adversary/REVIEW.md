# Independent pre-PR integration review

**Accepted at the bounded integration scope, with no unresolved actionable
finding.** The reviewed successor is the exact 251-file candidate listed in
`candidate-input-bindings.json`, SHA256
`a736235d36a83930e83e8ade1c4b60e098dd758eec4c1ac78dc83255acabf4af`.
Its base is `63ebb3b3e29ca1ed6472597104347d9fbc98f4a5`, tree
`5448122efcfbd8ae2ac90ad42e70557b03d9b78e`. This is a pre-PR worktree review;
it is not approval of an uncreated PR, subsequent support additions, or a later
commit. Full project gates and exact-head/actual-merge verification remain
separate requirements.

I did not author the maintained changes, source science, finite authority
adapter, accepted graph, or endpoint patch. I made no maintained, Git, GitHub,
network, or runtime installation changes. Dedicated reviewers own the primary
science and authority implementation acceptance. This review examines their
integration boundaries rather than claiming another complete primary-source
review or repeating the full test suite.

## Findings and dispositions

- **P2, root-discovered, fixed: issue #631.** Four copied verification helpers
  failed full repository lint with 269 diagnostics. The formatted successors
  preserve the complete non-import AST, literal values and archived original
  scripts. I independently checked the original/current hashes and ASTs, then
  ran all four actual portable verification commands successfully. Root's
  terminal full-lint successor reports exit 0. The repository lint policy and
  frozen packets are unchanged.
- **P2, root-discovered, fixed: issue #632.** Staged whitespace checks rejected
  16 original-source XML lines. The remedy preserves exact issuing bytes and
  adds only a directory-local `whitespace=-blank-at-eol` attribute to the 52
  direct original XML files. Actual Git attribute checks confirm these 52
  targets receive the rule and Python/YAML/README controls do not. All 52 XML
  bodies remain exact; 174 of the 175 authority-author owned files are unchanged,
  with only the local attributes file changed. Root's
  staged diff successor is terminal/pass. This was a packaging defect, not
  incorrect source content.
- **Generated-page synchronization, corrected.** The first full validation
  found the new page stale after the record history was added. The successful
  rerender changes only the acetate page and inserts the already saved history.
  Its network and scientific content are unchanged. The reviewed page hash is
  `f0e4deed2fa3d938282c68883294dbd53d057d3868513b7cdd3adb977bf60ef6`.
  Refreshed full validation remains root-owned and was not counted as complete
  by this review.

Issues #630, #631 and #632 must remain open until the actual merged tree has
been verified. The existing issue #630 endpoint implementation has a separate
independent review; the present integration confirms the actual maintained
record passes the production semantic validator and KGX consumers with all six
alternative input assertions.

## Independent evidence

The final integration probe completed **29,404 assertions with zero failures**.
This count is the final run only; it does not add the earlier attempt, other
reviewers' counts, or the portable archive counts.

- The exact physical YAML inventory includes ignored and hidden files. It has
  the 267 prior records plus exactly one new pathway. Every prior record and
  all 267 prior record pages remain byte-identical to the actual Git base.
  The candidate paths and governed files were checked against that base.
- All prior authority source/term objects and insertion order are preserved.
  The finite additions are exactly 52 native graph identities and five taxa;
  the manifest preserves its complete prior prefix. All 175 authority-author
  copies match their frozen bindings, with only the disclosed local attributes
  successor differing in the maintained owner. All 52 new native authority
  terms join record references with the same original SHA256 and acquired URL.
- Every one of the 14,074 pre-existing KGX edges is unchanged. All prior node
  contexts survive. The only non-context changes among shared nodes are the
  intended category unions: Mg/Mn acquire cofactor roles while retaining
  small-molecule roles; phosphate acquires a small-molecule role while retaining
  chemical-entity context. No unrelated node changes.
- All 89 new KGX edges preserve exact endpoints, predicates, descriptions,
  evidence arrays, reference metadata and qualifiers. The new record has 75
  public declarations: 69 native nodes and six taxa. Its six issued reactions
  remain separate from seven activity participants. All six alternative inputs
  originate at ENZRXN-481; the 29 canonical material edges remain unchanged.
- The new page contains all 69 native graph nodes and 89 correctly oriented
  edges, valid evidence links and the complete edge descriptions, assertions
  and locators. Taxa remain in the ordinary page and KGX. Every one of the 428
  structured evidence items is marked as a source assertion, without blockquote
  markup. The network SVG matches the frozen accepted graph; the only YAML
  change from that accepted design removes its prospective opening disclaimer.
- The actual production `validate_record`, `kgx_nodes` and `kgx_edges` accept
  the maintained record and emit 75 nodes, 89 edges and six activity inputs.
  This is a bounded production-consumer check, not a replacement for closed
  LinkML, identifier or full-corpus gates.

The four independent portable commands all terminated with exit 0 and empty
stderr. They checked **36 archives and 9,628 decoded outer members**, totaling
918,421,415 decoded member bytes, and cross-checked all 11 archived
manifest/freeze pairs against the portable indexes. Preparation contributes
24 archives/6,131 members; graph evidence contributes 12 archives/3,497 members.
Nested containers remain opaque byte-exact payloads. This mechanical check does
not add scientific acceptance or a new exhaustive inner-container search.

The helper AST check preserves semantics apart from standard-library import
ordering and unused imports. The portable commands ran with assertions enabled
(`sys.flags.optimize == 0`), bytecode writes disabled and user site disabled.
Their commands, script hashes, stdout/stderr hashes and full results are in
`portable-replay-independent-result.json` and `portable-runtime.json`.

## Preserved unsuccessful observations

The initial probe and its ten failed observations are retained. Three reviewer
assumptions were corrected: counting `.gitkeep` as a prior YAML record,
forbidding the documented shared-node category union, and counting six legend
symbols as biological nodes. The other five observations were the root's
disclosed helper/attribute edits during that first probe. None is concealed as
an initially clean run. `initial-observation-dispositions.json` explains every
observation; the final successor run has no failures.

Earlier navigation commands guessed three non-existent module filenames and
returned ordinary read errors; inspection then used the hidden/ignored-inclusive
Python file inventory and the actual `cli.py`, `kgx.py` and `graph_view.py`
owners. No absence conclusion or product change was based on those guesses.

## Remaining boundaries

No browser interaction or pixel inspection was performed. Static SVG, DOM,
table, export and accepted-design equality are the visual evidence. Source
licensing remains deferred as authorized. No global source-exhaustion claim is
made. Full tests, the refreshed full validation, final canonical scientific
record, later support-only retention, PR checks, native merge and cleanup remain
root-owned steps. A later exact-head review must bind any additions after these
251 files without overwriting this frozen packet.
