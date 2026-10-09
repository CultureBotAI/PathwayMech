# YAML Record Review: tetrahydrofolate biosynthesis

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/tetrahydrofolate-biosynthesis.yaml
- Started UTC: 2026-09-25T10:28:34Z
- Finished UTC: 2026-09-25T10:28:43Z
- Verdict: pass; 0 blocker, 0 major, 0 minor findings

## Target

Reviewed exactly one maintained record:
`data/pathways/tetrahydrofolate-biosynthesis.yaml`.

Resolved identity and shape:

- id: `gomodel:YeastPathways_PWY-6614`
- label: `tetrahydrofolate biosynthesis`
- description: Saccharomyces cerevisiae S288C tetrahydrofolate biosynthesis from
  4-aminobenzoate and
  `(7,8-dihydropterin-6-yl)methyl diphosphate` through FOL1, FOL3, and DFR1
  activities
- pathway_type: `folate-biosynthesis`
- taxa: 1, `NCBITaxon:559292`
- participants: 16, all projected from Noctua SGD or ChEBI individuals
- reactions: 3, all `gomodel` GO-CAM activity nodes
- mechanistic_edges: 20
- references: 1, `gomodel:YeastPathways_PWY-6614`

The maintained YAML was checked against:

- raw Noctua JSON:
  `/private/tmp/gocam-noctua/YeastPathways_PWY-6614.json`
- compact SGD GO-CAM JSON:
  `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-6614.json`

## Validation

All skill-required read-only validators passed:

```text
just validate
validated 5 Claude skills
validated 88 pathway records
checked 3380 evidence blocks
validated 12 source records
checked 6 documentation files
checked deep-research report contract
```

```text
just test
34 passed in 0.31s
```

```text
just lint
All checks passed!
```

```text
git diff --check
passed with no whitespace errors
```

Generated-page drift was checked without rewriting `pages/`: importing the
current renderer and rendering the loaded corpus in memory reproduced both
`pages/records/gomodel_YeastPathways_PWY-6614.html` and `pages/browse.html`
byte-for-byte. The renderer loaded 88 pathway records and generated slug
`gomodel_YeastPathways_PWY-6614`.

## Identity and Grounding

The record identity is the narrow GO-CAM model
`gomodel:YeastPathways_PWY-6614`, not a broad GO parent, a single reaction, or a
second pathway source. The compact SGD GO-CAM source carries id
`gomodel:YeastPathways_PWY-6614`, taxon `NCBITaxon:559292`, and title
`tetrahydrofolate biosynthesis - imported from: Saccharomyces Genome Database`;
the raw Noctua JSON carries the same model id and taxon annotation.

Hidden and ignored files were included in duplicate searches with
`rg --no-ignore --hidden -n -F`, excluding only `/.git` and `/.venv`. Searched
identifiers and labels included:

- `gomodel:YeastPathways_PWY-6614`
- `YeastPathways_PWY-6614`
- `PWY-6614`
- `tetrahydrofolate`
- `tetrahydrofolate biosynthetic process`
- `GO:0046654`
- `H2PTEROATESYNTH-RXN`
- `DIHYDROFOLATESYNTH-RXN`
- `DIHYDROFOLATEREDUCT-RXN`
- `6690711d00000586`
- `CHEBI:67016`

No duplicate record or duplicate pathway identity was found. Exact
`YeastPathways_PWY-6614`/`PWY-6614` hits were confined to the target YAML and
generated browse page. The three GO-CAM reaction ids occurred only in the
target YAML and the generated target record page. Broad `tetrahydrofolate`
hits in other YAML files were participant/metabolite mentions in unrelated
records such as IMP biosynthesis, glycine cleavage, methionine biosynthesis,
phosphopantothenate biosynthesis, and acetogenesis; the broad GO process
`GO:0046654` and label `tetrahydrofolate biosynthetic process` were absent
from the repository search.

## Graph and Local References

The target YAML passed `src/pathwaymech/schema.py` validation:

- every `mechanistic_edges` endpoint resolves to the record id or to a declared
  local participant/reaction;
- every predicate is one of `enables`, `consumes`, `produces`, or `precedes`,
  all allowed by `ALLOWED_EDGE_PREDICATES`;
- every edge has evidence pointing to the declared
  `gomodel:YeastPathways_PWY-6614` reference;
- all edge ids are unique;
- all mechanistic edge triples are unique.

The raw Noctua file contains 27 facts:

- 3 `RO:0002333` enables facts
- 8 `RO:0002233` input facts
- 8 `RO:0002234` output facts
- 1 `RO:0002413` supported causal fact
- 1 `RO:0002411` unsupported causal fact
- 3 `BFO:0000050` part-of facts
- 3 `BFO:0000066` occurs-in facts

The YAML contains exactly the 20 supported non-BFO facts:

- expected supported raw Noctua edge triples: 20
- actual YAML edge triples: 20
- extra YAML triples: 0
- missing YAML triples: 0

The 6 BFO part/location facts are omitted, as expected. The unsupported
`RO:0002411` fact from `gomodel:DIHYDROFOLATESYNTH-RXN` to
`gomodel:DIHYDROFOLATEREDUCT-RXN` is also omitted. In the raw Noctua JSON that
`RO:0002411` fact has no evidence annotation; in the compact SGD JSON it appears
as a `CausalAssociation` with empty `evidence`.

## Edge Evidence

All 39 YAML evidence quotes are exact substrings of
`/private/tmp/gocam-noctua/YeastPathways_PWY-6614.json`.

Edge projection from raw Noctua facts is exact:

- each `RO:0002333` fact is projected to `SGD:* enables gomodel:*`;
- each `RO:0002233` fact is projected to `CHEBI:* consumes gomodel:*`;
- each `RO:0002234` fact is projected to `gomodel:* produces CHEBI:*`;
- the supported `RO:0002413` fact is projected to
  `gomodel:H2PTEROATESYNTH-RXN precedes
  gomodel:DIHYDROFOLATESYNTH-RXN`.

The raw-only local tetrahydrofolate individual
`gomodel:YeastPathways_PWY-6614/6690711d00000586` is correctly projected to
`CHEBI:67016`: the individual in the raw Noctua `individuals` list has primary
type `CHEBI:67016`, the raw `RO:0002234` output fact from
`gomodel:DIHYDROFOLATEREDUCT-RXN` points at that local individual, and the
compact SGD GO-CAM projection represents the corresponding `has_output` term as
`CHEBI:67016`.

## Completeness

The maintained record contains every supported Noctua `RO:0002333`,
`RO:0002233`, `RO:0002234`, and evidence-bearing `RO:0002413` fact expected for
`YeastPathways_PWY-6614`.

It deliberately leaves out the 6 BFO facts and the one unsupported
`RO:0002411` causal association, which are raw-source facts but not maintained
YAML mechanistic edges.

## Findings

None found.

### Blocker

None found.

### Major

None found.

### Minor

None found.

## Recommended Edits

None found.

## Follow-up Checks

No follow-up is required for this record.

If `data/pathways/tetrahydrofolate-biosynthesis.yaml` changes later, re-run:

```bash
just validate
just test
just lint
git diff --check
```

If changes alter any rendered fields or edge counts, also refresh generated
pages with `just render-pages` and verify
`pages/records/gomodel_YeastPathways_PWY-6614.html` plus `pages/browse.html`
again.

## Additional Notes

No maintained YAML, generated page, existing report, or GitHub state was edited
during this review. This report created the previously absent
`reports/yaml_record_review/` directory and added only this timestamped file.
