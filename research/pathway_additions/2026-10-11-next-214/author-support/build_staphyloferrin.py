"""Build an external, source-qualified complete staphyloferrin A draft."""

import hashlib
import json
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import etree as E
from lxml import html as H

B = Path(__file__).resolve().parent
D = B / "draft"
D.mkdir(exist_ok=True)
F = Path("/private/tmp/pathwaymech-staphyloferrin-a-followup-20261011")
ORIGINALS = Path("/private/tmp/pathwaymech-siderophore-next-scout-20261011/originals")
C = Path("/private/tmp/pathwaymech-curation-authorities")


def sha(p):
    with Path(p).open("rb") as s:
        return hashlib.file_digest(s, "sha256").hexdigest()


def read(p):
    return json.loads(Path(p).read_text())


def save(n, v):
    (D / n).write_text(json.dumps(v, indent=2, ensure_ascii=False) + "\n")


m = read(F / "source-manifest.json")
byname = {Path(x["path"]).name: x for x in m["sources"]}
chem = read(F / "chemistry.json")
refs = []
paths = {}


def ref(cid, name, title=None, version=None):
    x = byname[name]
    p = Path(x["path"])
    r = {
        "id": cid,
        "title": str(title or name),
        "url": x["url"],
        "source_version": version
        or "Original response retrieved 2026-10-11; hash covers complete response body",
        "source_sha256": x["sha256"],
    }
    assert sha(p) == r["source_sha256"]
    refs.append(r)
    paths[cid] = str(p)


for n in [
    "PWY-7990",
    "ORNITHINE-RACEMASE-RXN",
    "RXN-19522",
    "RXN-19521",
    "MONOMER-20490",
    "MONOMER-20491",
    "MONOMER-20492",
    "ENZRXN-26282",
    "ENZRXN-26283",
    "ENZRXN-26284",
    "L-ORNITHINE",
    "CPD-217",
    "CPD-21047",
    "CPD-12589",
]:
    ref(
        "MetaCyc:" + n,
        n + ".xml",
        "MetaCyc " + n + " native XML object",
        "MetaCyc 22.5; retrieved 2026-10-11; complete native XML response",
    )
ref(
    "KEGG:M00876",
    "M00876.txt",
    "KEGG M00876: Staphyloferrin A biosynthesis, L-ornithine => staphyloferrin A",
)
for ac in ["BAF68351.1", "BAF68352.1", "BAF68354.1"]:
    ref(
        "NCBIProtein:" + ac,
        "Newman-proteins.xml",
        "NCBI GenPept " + ac + " Newman protein identity",
        "GenPept original three-entry batch retrieved 2026-10-11; hash covers entire XML batch",
    )
for ac in ["Q2FW73", "Q2FW72", "Q2FW70"]:
    ref(
        "UniProtKB:" + ac,
        ac + ".json",
        "UniProtKB " + ac + " original entry; NCTC 8325 scope",
        "UniProt release 2026_03; original JSON retrieved 2026-10-11",
    )
ct = read(ORIGINALS / "PMID19138128.json")["resultList"]["result"][0]
ref(
    "PMID:19138128",
    "PMID19138128.json",
    ct["title"],
    (
        "Cotton et al. 2009; indexed abstract only; hash covers origina"
        "l Europe PMC core JSON, not full article"
    ),
)
p = F / "originals/PMC2856993.html"
html = H.fromstring(p.read_bytes())
ref(
    "PMID:20147287",
    "PMC2856993.html",
    html.xpath('//meta[@name="citation_title"]/@content')[0],
    (
        "Grigg et al. 2010; complete original PMC HTML inspected; Figur"
        "e 2A image separately inspected"
    ),
)
refs.append(
    {
        "id": "PMID:19400778",
        "title": (
            "Characterization of staphyloferrin A biosynthetic and transpor"
            "t mutants in Staphylococcus aureus."
        ),
        "url": "https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2009.06698.x",
        "source_version": (
            "Beasley et al. 2009; full original publisher text inspected th"
            "rough web access on 2026-10-11; no local full-body hash; index"
            "ed abstract separately retained"
        ),
    }
)
for r in chem["reactions"]:
    cid = "RHEA:" + str(r["directional"])
    refs.append(
        {
            "id": cid,
            "title": "Rhea "
            + str(r["directional"])
            + (" exact directional reaction and side graph"),
            "url": "https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz",
            "source_version": "Rhea 142, 2026-09-02; digest covers complete original gzip RDF",
            "source_sha256": chem["originals"][0]["sha256"],
        }
    )
    paths[cid] = chem["originals"][0]["path"]
refs.append(
    {
        "id": "CHEBI:142973",
        "title": "ChEBI 255 chemical structures, charges and stereochemical names",
        "url": "https://www.ebi.ac.uk/chebi/",
        "source_version": (
            "ChEBI 255 Semantic SQL; digest covers full uncompressed original database"
        ),
        "source_sha256": chem["originals"][2]["sha256"],
    }
)
paths["CHEBI:142973"] = chem["originals"][2]["path"]
con = sqlite3.connect("file:" + str(C / "chebi.db") + "?mode=ro", uri=True)
chemids = {x["id"] for r in chem["reactions"] for s in r["sides"].values() for x in s} | {
    "CHEBI:597326",
    "CHEBI:18420",
}
participants = [
    {
        "id": cid,
        "label": con.execute(
            'select value from statements where subject=? and predicate="rdfs:label"', (cid,)
        ).fetchone()[0],
        "category": "cofactor" if cid in {"CHEBI:597326", "CHEBI:18420"} else "small_molecule",
    }
    for cid in sorted(chemids)
]
for a, locus_label in [
    ("BAF68351.1", "NWMN_2079"),
    ("BAF68352.1", "NWMN_2080"),
    ("BAF68354.1", ("NWMN_2082")),
]:
    participants.append({"id": "NCBIProtein:" + a, "label": locus_label, "category": "protein"})
tcon = sqlite3.connect("file:" + str(C / "ncbitaxon.db") + "?mode=ro", uri=True)
taxlabel = tcon.execute(
    'select value from statements where subject="NCBITaxon:426430" and predicate="rdfs:label"'
).fetchone()[0]
record = {
    "id": "MetaCyc:PWY-7990",
    "label": "staphyloferrin A biosynthesis",
    "description": (
        "Complete three-transformation staphyloferrin A biosynthesis sc"
        "oped to Staphylococcus aureus Newman: L-ornithine racemization"
        " supplies D-ornithine, followed by the ordered SfaD and SfaB c"
        "itrate ligations. The selected racemization direction is pathw"
        "ay flux; native MetaCyc and KEGG describe the reversible react"
        "ion. SfaC/NWMN_2079 activity remains inferred from locus funct"
        "ion, sequence-family evidence and the native assignment, not a"
        "n isolated Newman enzyme assay. Its PLP relation is an automat"
        "ic annotation transferred through exact sequence equality, not"
        " a direct binding measurement. Newman SfaB and SfaD coding reg"
        "ions were used in the inspected 2010 recombinant preparation; "
        "full engineered construct sequences and native assembly states"
        " are unresolved. The 2009 Cotton evidence for ordered individu"
        "al ligations was inspected as an abstract only. Current NCTC 8"
        "325 annotations inform reaction identity: SfaB is sequence-ide"
        "ntical to the selected Newman protein, whereas SfaD differs at"
        " residue 532 and is not treated as the same protein. The nativ"
        "e ligase Mg2+ assertions are retained as qualified curated cof"
        "actor assignments rather than a unique physiological metal or "
        "binding stoichiometry. Current Rhea/ChEBI chemistry specifies "
        "the N5-(S)-citryl intermediate and N2-(R),N5-(S)-citryl produc"
        "t, whereas native CPD-21047 and CPD-12589 leave the citryl cen"
        "ters unspecified. The inspected 2010 ferric receptor-bound str"
        "ucture supports final N2 R/N5 S stereochemistry; it does not d"
        "irectly establish the free intermediate's stereochemistry or t"
        "he selected free ionic forms. These forms remain explicit curr"
        "ent chemical-authority conventions, without exact native-compo"
        "und equivalence. Iron/Fur-dependent transcription is reported "
        "as context; transport, ferric loading, uptake, citrate product"
        "ion and the distinct staphyloferrin B route lie outside this c"
        "omplete biosynthetic boundary."
    ),
    "pathway_type": "staphyloferrin-a-biosynthesis",
    "taxa": [{"id": "NCBITaxon:426430", "label": taxlabel}],
    "participants": participants,
    "reactions": [
        {
            "id": "RHEA:" + str(r["directional"]),
            "label": label,
            "category": "molecular_activity",
            "direction": "left_to_right",
        }
        for r, label in zip(
            chem["reactions"],
            [
                "L-Ornithine racemization toward D-ornithine",
                "SfaD D-ornithine N5-citrylation",
                "SfaB terminal N2-citrylation",
            ],
            strict=True,
        )
    ],
    "mechanistic_edges": [],
    "references": refs,
}


def ev(ref, text, loc):
    assert len(text) <= 400, (len(text), text)
    return {"reference_id": ref, "source_assertion": text, "source_locator": loc}


def edge(sub, pred, obj, evidence, description=None):
    d = {
        "id": f"sfa-edge-{len(record['mechanistic_edges']) + 1:03d}",
        "subject": sub,
        "predicate": pred,
        "object": obj,
        "evidence": evidence,
    }
    if description:
        d["description"] = description.strip()
    record["mechanistic_edges"].append(d)
    return d["id"]


sideproj = []
for r in chem["reactions"]:
    rid = "RHEA:" + str(r["directional"])
    for role, sides in r["sides"].items():
        for t in sides:
            evid = [
                ev(
                    rid,
                    (
                        "The selected Rhea direction assigns "
                        f"{t['id']}"
                        " to its "
                        f"{role}"
                        " with coefficient "
                        f"{t['coefficient']}"
                        "."
                    ),
                    (
                        "rh:"
                        f"{r['directional']}"
                        "/rh:"
                        f"{role}"
                        " -> "
                        f"{t['side_uri']}"
                        "; rh:contains"
                        f"{t['coefficient']}"
                        " -> "
                        f"{t['participant_uri']}"
                        "; rh:compound -> "
                        f"{t['compound_uri']}"
                        "; rh:chebi"
                    ),
                )
            ]
            desc = None
            if t["id"] in {"CHEBI:142972", "CHEBI:142973"}:
                desc = (
                    "This edge uses the current Rhea/ChEBI stereospecific free ioni"
                    "c form. The corresponding native MetaCyc compound leaves citry"
                    "l stereochemistry unspecified; no exact equivalence is asserte"
                    "d."
                )
                evid.append(
                    ev(
                        "CHEBI:142973",
                        (
                            f"{t['id']}"
                            " defines "
                            f"{t['label']}"
                            " with its specified stereochemistry and charge "
                            f"{t['charge']}"
                            ". This is the current free chemical identity, distinct from th"
                            "e broader native compound."
                        ),
                        (
                            'statements[subject="'
                            f"{t['id']}"
                            '",predicate=rdfs:label|chemrof:inchi_string|chemrof:charge]'
                        ),
                    )
                )
            if t["id"] == "CHEBI:142973":
                evid.append(
                    ev(
                        "PMID:20147287",
                        (
                            "The ferric receptor-bound product model assigns ornithine R an"
                            "d citryl centers N2 R/N5 S; an S,S model fits less well. This "
                            "supports final product stereochemistry, not a direct free-ion "
                            "measurement."
                        ),
                        (
                            "PMC2856993 HTML Results, Structure of Staphyloferrin A (sec18)"
                            ", paragraph 2; Figure 2A-C"
                        ),
                    )
                )
            eid = edge(
                t["id"] if role == "substrates" else rid,
                "consumes" if role == "substrates" else "produces",
                rid if role == "substrates" else t["id"],
                evid,
                desc,
            )
            sideproj.append({"edge_id": eid, "reaction": rid, "role": role, **t})
maprows = []
for n, r in zip(
    ["ORNITHINE-RACEMASE-RXN", "RXN-19522", "RXN-19521"], chem["reactions"], strict=True
):
    rid = "RHEA:" + str(r["directional"])
    master = r["master"]
    evid = [
        ev(
            "MetaCyc:PWY-7990",
            (
                "The complete native pathway explicitly includes "
                f"{n}"
                "; its pathway layout selects the left-to-right biosynthetic di"
                "rection."
            ),
            (
                'Pathway[@frameid="PWY-7990"]/reaction-list/Reaction[@frameid="'
                f"{n}"
                '"]; reaction-layout[Reaction/@frameid="'
                f"{n}"
                '"]/direction'
            ),
        )
    ]
    if n == "ORNITHINE-RACEMASE-RXN":
        evid.extend(
            [
                ev(
                    "MetaCyc:" + n,
                    (
                        "The native ornithine racemase reaction is reversible and cross"
                        "-references RHEA:11587. The pathway selects L- to D-ornithine "
                        "flux."
                    ),
                    'Reaction/reaction-direction; dblink[dblink-db="RHEA"]/dblink-oid',
                ),
                ev(
                    rid,
                    (
                        "Rhea master 11584 links bidirectional 11587 and left-to-right "
                        "11585, preserving the explicit direction-family bridge."
                    ),
                    (
                        "rh:11584/rh:bidirectionalReaction -> rh:11587; rh:directionalR"
                        "eaction -> rh:11585"
                    ),
                ),
            ]
        )
    else:
        evid.extend(
            [
                ev(
                    "MetaCyc:" + n,
                    (
                        "The native equation specifies the ordered citrate ligation wit"
                        "h ATP, AMP, diphosphate and proton; its citryl compound identi"
                        "ty is less stereospecific than the selected current reaction."
                    ),
                    "Reaction/left; right; reaction-direction",
                ),
                ev(
                    rid,
                    (
                        "Current master "
                        f"{master}"
                        " links the selected left-to-right direction "
                        f"{r['directional']}"
                        " and defines the complete stereospecific equation independentl"
                        "y of native MetaCyc."
                    ),
                    "rh:"
                    + str(master)
                    + "/rh:directionalReaction -> rh:"
                    + str(r["directional"])
                    + "; rh:equation",
                ),
            ]
        )
    edge(rid, "part_of", record["id"], evid)
    x = E.parse(str(ORIGINALS / (n + ".xml"))).find("Reaction")
    maprows.append(
        {
            "native": n,
            "reaction": rid,
            "native_direction": x.findtext("reaction-direction"),
            "native_sides": {
                s: [
                    {"id": z[0].get("frameid"), "coefficient": int(z.findtext("coefficient") or 1)}
                    for z in x.findall(s)
                ]
                for s in ["left", "right"]
            },
            "disposition": (
                "Full transformation retained; source direction and stereochemi"
                "cal specificity limits preserved."
            ),
        }
    )
# Gene-product roles do not imply a monomeric or multienzyme assembly.
edge(
    "NCBIProtein:BAF68351.1",
    "enables",
    "RHEA:11585",
    [
        ev(
            "MetaCyc:MONOMER-20490",
            (
                "The native comment explicitly assumes ornithine racemase activ"
                "ity from the functional locus and states that the enzyme was n"
                "ot purified. The mapped UniProt accession is Q2FW73."
            ),
            'Protein[@frameid="MONOMER-20490"]/comment; dblink[dblink-db="UNIPROT"]',
        ),
        ev(
            "NCBIProtein:BAF68351.1",
            (
                "The original Newman entry identifies NWMN_2079 and provides it"
                "s complete 356-residue sequence; this is genomic protein ident"
                "ity, not a functional assay."
            ),
            'GBSeq[GBSeq_accession-version="BAF68351.1"]/GBSeq_feature-table; GBSeq_sequence',
        ),
        ev(
            "UniProtKB:Q2FW73",
            (
                "The unreviewed NCTC 8325 entry supplies its 356-residue sequen"
                "ce. Comparison with the independently retrieved Newman sequenc"
                "e gives exact equality; functional evidence remains inferred."
            ),
            "/sequence/value; /organism/taxonId; /entryType",
        ),
        ev(
            "PMID:19400778",
            (
                "Table 2 identifies Newman NWMN_2079 as SfaC by amino-acid-race"
                "mase similarity. Locus-level product evidence does not establi"
                "sh purified SfaC catalysis."
            ),
            "Results, Table 2 (NWMN_2079); Figure 5; original publisher web text",
        ),
    ],
    (
        "Inferred SfaC gene-product role. Neither exact sequence equali"
        "ty nor whole-locus function demonstrates isolated Newman racem"
        "ase activity or oligomeric state."
    ),
)
for ac, up, _native, rid, gene in [
    ("BAF68354.1", "Q2FW70", "MONOMER-20492", "RHEA:59137", "SfaD"),
    ("BAF68352.1", "Q2FW72", "MONOMER-20491", "RHEA:59141", "SfaB"),
]:
    loc = 'GBSeq[GBSeq_accession-version="' + ac + '"]/GBSeq_feature-table; GBSeq_sequence'
    comparison = (
        "The Newman sequence differs from Q2FW70 at residue 532; exact identity is not claimed."
        if gene == "SfaD"
        else (
            "The Newman sequence is identical to Q2FW72; strain provenance still remains distinct."
        )
    )
    edge(
        "NCBIProtein:" + ac,
        "enables",
        rid,
        [
            ev(
                "NCBIProtein:" + ac,
                (
                    "The versioned entry identifies the Newman coding product, locu"
                    "s and complete protein sequence. Comparison with NCTC 8325 is "
                    "a separate curation calculation."
                ),
                loc,
            ),
            ev(
                "PMID:20147287",
                (
                    "The study used Newman sfaB and sfaD coding regions for recombi"
                    "nant protein preparations and jointly synthesized staphyloferr"
                    "in A. This supports the Newman implementation but does not res"
                    "olve native assemblies."
                ),
                (
                    "PMC2856993 HTML Experimental Procedures, Cloning and Protein E"
                    "xpression (sec5), paragraph 2; Staphyloferrin A Synthesis and "
                    "Purification (sec7)"
                ),
            ),
            ev(
                "PMID:19138128",
                (
                    "The inspected abstract assigns the first delta-amine citrate l"
                    "igation to SfnaD and the terminal alpha-amine ligation to Sfna"
                    "B. Full methods and exact Cotton construct sequences were not "
                    "inspected."
                ),
                "Europe PMC core resultList.result[0].abstractText",
            ),
            ev(
                "UniProtKB:" + up,
                (
                    "The reviewed NCTC 8325 entry assigns this reaction and left-to"
                    "-right physiological direction with ECO:0000269 citing Cotton."
                    " This source annotation is kept separate from Newman protein i"
                    "dentity."
                ),
                "/comments/1/reaction; /comments/1/physiologicalReactions; /organism/taxonId",
            ),
            ev(
                "UniProtKB:" + up,
                (
                    "The current entry provides the complete NCTC 8325 protein sequ"
                    "ence. This supplies the independent comparison source, not an "
                    "assertion that Newman and NCTC 8325 are the same strain."
                ),
                "/sequence/value; /organism/taxonId",
            ),
        ],
        comparison
        + " "
        + gene
        + (
            " functional role supported by Newman recombinant biosynthesis "
            "plus independently ordered ligation evidence. Exact engineered"
            " sequences and native oligomeric sufficiency remain unresolved"
            "."
        ),
    )
# Cofactor relations preserve their actual evidence grade and strain transfer.
edge(
    "NCBIProtein:BAF68351.1",
    "has_cofactor",
    "CHEBI:597326",
    [
        ev(
            "UniProtKB:Q2FW73",
            (
                "The unreviewed NCTC 8325 entry assigns pyridoxal 5-prime-phosp"
                "hate (CHEBI:597326) through automatic ARBA evidence ECO:000025"
                "6; it is not a direct cofactor experiment."
            ),
            (
                "/comments/0/cofactors/0/cofactorCrossReference; /comments/0/co"
                "factors/0/evidences/0; /sequence/value"
            ),
        ),
        ev(
            "NCBIProtein:BAF68351.1",
            (
                "The selected entry provides the complete Newman protein sequen"
                "ce. Its identity and genomic origin do not independently estab"
                "lish cofactor binding."
            ),
            'GBSeq[GBSeq_accession-version="BAF68351.1"]/GBSeq_sequence',
        ),
    ],
    (
        "Automatic cofactor inference transferred through exact sequenc"
        "e equality; no binding count or direct Newman measurement is a"
        "sserted."
    ),
)
for ac, n in [("BAF68352.1", "ENZRXN-26283"), ("BAF68354.1", "ENZRXN-26284")]:
    edge(
        "NCBIProtein:" + ac,
        "has_cofactor",
        "CHEBI:18420",
        [
            ev(
                "MetaCyc:" + n,
                (
                    "The native ligase enzymatic-reaction object explicitly lists M"
                    "G+2 as cofactor and cites Cotton. The cited full article was u"
                    "navailable; this is a curated database assertion rather than a"
                    "n independently inspected metal assay."
                ),
                'Enzymatic-Reaction[@frameid="'
                + n
                + '"]/cofactor/Compound[@frameid="MG+2"]; cofactor/citation',
            ),
            ev(
                "PMID:20147287",
                (
                    "The complete article identifies Newman SfaB and SfaD recombina"
                    "nt preparations used in joint biosynthesis. It supports the se"
                    "lected implementation, not a unique physiological metal or bin"
                    "ding stoichiometry."
                ),
                "PMC2856993 HTML sec5 paragraph 2; sec7",
            ),
        ],
        (
            "Qualified native ligase cofactor assignment applied to the New"
            "man role; no independently measured Newman metal specificity, "
            "binding stoichiometry or metal-exclusive requirement is claime"
            "d."
        ),
    )
for ac in ["BAF68351.1", "BAF68352.1", "BAF68354.1"]:
    edge(
        "NCBIProtein:" + ac,
        "part_of",
        "NCBITaxon:426430",
        [
            ev(
                "NCBIProtein:" + ac,
                (
                    "The source feature explicitly identifies strain Newman and tax"
                    "on 426430 for this versioned protein."
                ),
                'GBSeq[GBSeq_accession-version="'
                + ac
                + '"]/GBSeq_feature-table/GBFeature[GBFeature_key="source"]/GBFeature_quals',
            )
        ],
    )
edge(
    record["id"],
    "part_of",
    "NCBITaxon:426430",
    [
        ev(
            "PMID:19400778",
            (
                "The Newman locus and product analyses support staphyloferrin A"
                " biosynthesis; these organism-level observations do not indepe"
                "ndently assay every encoded activity."
            ),
            (
                "Results, The NWMN_2082-2079 locus mediates staphyloferrin A bi"
                "osynthesis; Figure 5; original publisher web text"
            ),
        )
    ],
)
for first, second, n1, n2, cid in [
    ("RHEA:11585", "RHEA:59137", "ORNITHINE-RACEMASE-RXN", "RXN-19522", "CHEBI:57668"),
    ("RHEA:59137", "RHEA:59141", "RXN-19522", "RXN-19521", "CHEBI:142972"),
]:
    edge(
        first,
        "provides_input_for",
        second,
        [
            ev(
                "MetaCyc:PWY-7990",
                (
                    "The native ordering puts "
                    f"{n1}"
                    " before "
                    f"{n2}"
                    "; native frames define the shared intermediate without a ChEBI"
                    " equivalence claim."
                ),
                'Pathway/reaction-ordering[Reaction/@frameid="' + n2 + '"]/predecessor-reactions',
            ),
            ev(
                first,
                (
                    "The selected upstream direction produces "
                    f"{cid}"
                    ", the same chemical identity independently consumed by the sel"
                    "ected downstream direction."
                ),
                "rh:"
                + first.split(":")[1]
                + "/rh:products -> side/rh:contains1 -> participant/rh:compound/rh:chebi",
            ),
            ev(
                second,
                (
                    "The selected downstream direction consumes "
                    f"{cid}"
                    "; the explicit common chemical supports material continuity."
                ),
                "rh:"
                + second.split(":")[1]
                + "/rh:substrates -> side/rh:contains1 -> participant/rh:compound/rh:chebi",
            ),
        ],
    )
target = D / "staphyloferrin-a-biosynthesis.yaml"
target.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=100))
# Only selected facts/locators are retained, never whole source articles or comments.
save(
    "staphyloferrin-a-source-projection.json",
    {
        "created_at": datetime.now(UTC).isoformat(),
        "target_sha256": sha(target),
        "native_identity": "MetaCyc:PWY-7990",
        "counterpart": "KEGG:M00876",
        "source_to_graph": maprows,
        "chemical_sides": sideproj,
        "graph_to_source": record["mechanistic_edges"],
        "reference_original_paths": paths,
        "web_only_references": ["PMID:19400778"],
        "native_chemical_bridges": chem["native_current_bridges"],
        "net": chem["route_net"],
        "exclusions": [
            {
                "object": "SfaA/htsABC/FhuC",
                "disposition": "Export and uptake lie beyond native biosynthesis boundary.",
            },
            {
                "object": "CPLX-7173",
                "disposition": (
                    "Alternate reaction controller from another organism; not trans"
                    "ferred into Newman."
                ),
            },
            {
                "object": "citrate biosynthesis",
                "disposition": (
                    "External precursor supply, not one of PWY-7990 three native members."
                ),
            },
            {"object": "staphyloferrin B", "disposition": "Distinct complete pathway."},
            {
                "object": "Fur-dependent transcription",
                "disposition": (
                    "Primary Figure3 context retained in dossier, not a new exact N"
                    "ewman regulatory protein claim."
                ),
            },
        ],
    },
)
save(
    "staphyloferrin-a-identifiers.json",
    {
        "record": record["id"],
        "target_sha256": sha(target),
        **{
            k: [x["id"] for x in record[k]]
            for k in ["taxa", "participants", "reactions", "references"]
        },
    },
)
print(
    json.dumps(
        {
            "target": str(target),
            "sha256": sha(target),
            "participants": len(participants),
            "reactions": 3,
            "edges": len(record["mechanistic_edges"]),
            "evidence": sum(len(e["evidence"]) for e in record["mechanistic_edges"]),
            "references": len(refs),
        },
        indent=2,
    )
)
