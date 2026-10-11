import hashlib
import html
import json
import re
import sqlite3
from pathlib import Path

import yaml
from lxml import etree as E

ROOT = Path(__file__).parent
OUT = ROOT / "draft"
SCOUT = Path("/private/tmp/pathwaymech-bacillibactin-scout-20261011")
REPO = Path("/private/tmp/pathwaymech-next-210-20261011")
CACHE = Path("/private/tmp/pathwaymech-curation-authorities")


def sha(p):
    with Path(p).open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def source(n):
    p = ROOT / "originals" / n
    return p if p.exists() else SCOUT / n


def obj(n):
    return next(x for x in E.parse(str(source(n + ".xml"))).getroot() if x.tag != "metadata")


def clean(s):
    return " ".join(html.unescape(re.sub("<[^>]+>", "", s)).split())


steps = [
    "ISOCHORSYN-RXN",
    "ISOCHORMAT-RXN",
    "DHBDEHYD-RXN",
    "DHBAMPLIG-RXN",
    "RXN-19449",
    "RXN-9376",
    "RXN-19458",
    "RXN-19460",
    "RXN-9377",
    "RXN-19452",
    "RXN-19461",
    "RXN-19462",
]
step_labels = [
    "Chorismate isomerization",
    "Isochorismate hydrolysis",
    "Dihydrodihydroxybenzoate oxidation",
    "2,3-Dihydroxybenzoate adenylation",
    "2,3-Dihydroxybenzoyl loading of DhbB",
    "Glycine adenylation",
    "Glycyl loading of DhbF",
    "Dihydroxybenzoyl-glycyl condensation",
    "L-Threonine adenylation",
    "L-Threonyl loading of DhbF",
    "Dihydroxybenzoyl-glycyl-L-threonyl condensation",
    "Bacillibactin trimerization and cyclorelease",
]
raws = {n: obj(n) for n in steps}
side_projection = {}
for n, x in raws.items():
    d = {
        "direction": x.findtext("reaction-direction"),
        "left": [],
        "right": [],
        "path": str(source(n + ".xml")),
        "sha256": sha(source(n + ".xml")),
    }
    for side in ["left", "right"]:
        for slot in x.findall(side):
            entity = next(z for z in slot if z.get("frameid"))
            d[side].append(
                {"id": entity.get("frameid"), "coefficient": int(slot.findtext("coefficient") or 1)}
            )
    side_projection[n] = d
names = sorted(
    {x["id"] for d in side_projection.values() for side in ["left", "right"] for x in d[side]}
)
chemmap = {n: "MetaCyc:" + n for n in names}
chemmap.update(
    {
        "ATP": "CHEBI:30616",
        "AMP": "CHEBI:456215",
        "NADH": "CHEBI:57945",
        "DHB-glycyl-arginyl-DhbF": "metanetx.chemical:MNXM743865",
    }
)
carrier_names = {
    "Holo-DhbB",
    "23-dihydroxybenzoyl-DhbB",
    "DhbF",
    "Glycyl-DhbF",
    "Threonyl-DhbF",
    "DHB-glycyl-DhbF",
    "DHB-glycyl-arginyl-DhbF",
}
chebi = {}
with sqlite3.connect(f"file:{CACHE}/chebi.db?mode=ro", uri=True) as c:
    for cid in ["CHEBI:30616", "CHEBI:456215", "CHEBI:57945"]:
        chebi[cid] = dict(
            c.execute(
                "select predicate,value from statements where subject=? and value is not null",
                [cid],
            )
        )
proteins = E.parse(str(SCOUT / "followup/ncbi-kh34-proteins.xml")).getroot()
protein_rows = {p.findtext("GBSeq_accession-version"): p for p in proteins.findall("GBSeq")}
selected_proteins = [
    "BDG45611.1",
    "BDG45612.1",
    "BDG45613.1",
    "BDG45614.1",
    "BDG45615.1",
    "BDG45617.1",
]
mnx_path = SCOUT / "carrier-authority-followup/metanetx-MNXM743865.html"
mnx_objs = [
    json.loads(x.text)
    for x in E.HTML(mnx_path.read_text()).xpath('//script[@type="application/ld+json"]')
]
mnx = next(x for x in mnx_objs if x.get("@type") == "MolecularEntity")
assert mnx["identifier"] == "metanetx.chemical:MNXM743865"
refs = []
refpaths = {}


def ref(cid, title, path, url, version):
    assert cid not in refpaths
    refs.append(
        {
            "id": cid,
            "title": title,
            "url": url,
            "source_version": version,
            "source_sha256": sha(path),
        }
    )
    refpaths[cid] = str(path)


for n in ["PWY-5903", "PWY-5901", *steps, *names, "RXN-9374"]:
    if "MetaCyc:" + n in refpaths:
        continue
    ref(
        "MetaCyc:" + n,
        "MetaCyc 22.5 native " + n,
        source(n + ".xml"),
        "https://pathway.yeastgenome.org/getxml?META:" + n,
        "MetaCyc 22.5; exact original XML retrieved 2026-10-11",
    )
ref(
    "PMID:39870587",
    "Biosynthetic Characterization of Bacillibactin in Thermophilic "
    "Bacillaceae and its Potential for in Vitro Mutational Synthesis",
    SCOUT / "followup/Izumi2025-accepted.pdf",
    "https://ir.library.osaka-u.ac.jp/repo/ouka/all/100254/ChemBioChem_cbic.202400836.pdf",
    "2025 Osaka official accepted manuscript and complete supplement, 30 PDF pages; "
    "page numbers include repository cover; exact original PDF",
)
ref(
    "metanetx.chemical:MNXM743865",
    mnx["name"],
    mnx_path,
    "https://www.metanetx.org/chem_info/MNXM743865",
    "MNXref production 4.5 per separately retained release page; exact original HTML "
    "retrieved 2026-10-11; no versioned bulk dump claimed",
)
protein_url = (
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&"
    "id=BDG45611,BDG45612,BDG45613,BDG45614,BDG45615,BDG45616,BDG45617"
    "&rettype=gb&retmode=xml"
)
for a in selected_proteins:
    ref(
        "NCBIProtein:" + a,
        protein_rows[a].findtext("GBSeq_definition"),
        SCOUT / "followup/ncbi-kh34-proteins.xml",
        protein_url,
        "NCBI original complete seven-entry GenPept XML batch; versioned accession; "
        "retrieved 2026-10-11; reference hash covers the whole original response",
    )
ref(
    "NCBITaxon:2916802",
    "NCBI Taxonomy Parageobacillus sp. KH3-4",
    source("taxon2916802.xml"),
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2916802&retmode=xml",
    "NCBI Taxonomy original XML retrieved 2026-10-11",
)
ref(
    "CHEBI:30616",
    "ChEBI ionic ATP, AMP and NADH identity authorities",
    CACHE / "chebi.db",
    "http://purl.obolibrary.org/obo/chebi/255/chebi.owl",
    "ChEBI 255; hash covers full original uncompressed Semantic SQL database",
)
participants = []
for n in names:
    cid = chemmap[n]
    label = (
        mnx["name"]
        if cid.startswith("metanetx.")
        else chebi[cid]["rdfs:label"]
        if cid.startswith("CHEBI:")
        else clean(obj(n).findtext("common-name"))
    )
    participants.append(
        {
            "id": cid,
            "label": label,
            "category": "chemical_entity" if n in carrier_names else "small_molecule",
        }
    )
for a in selected_proteins:
    participants.append(
        {
            "id": "NCBIProtein:" + a,
            "label": protein_rows[a].findtext("GBSeq_definition"),
            "category": "protein",
        }
    )
reactions = [
    {
        "id": "MetaCyc:" + n,
        "label": label,
        "category": "molecular_activity",
        "direction": "reversible" if n == "ISOCHORSYN-RXN" else "left_to_right",
    }
    for n, label in zip(steps, step_labels, strict=True)
]
edges = []


def ev(cid, assertion, locator):
    assert len(assertion) <= 400, (cid, len(assertion), assertion)
    return {"reference_id": cid, "source_assertion": assertion, "source_locator": locator}


def primary(assertion, locator):
    return ev("PMID:39870587", assertion, locator)


def edge(s, p, o, evidence, description=None):
    d = {
        "id": f"bacillibactin-edge-{len(edges) + 1:03}",
        "subject": s,
        "predicate": p,
        "object": o,
        "evidence": evidence,
    }
    if description:
        d["description"] = description
    edges.append(d)


for n in steps:
    d = side_projection[n]
    for side, predicate in [("left", "has_input"), ("right", "has_output")]:
        for x in d[side]:
            native = x["id"]
            cid = chemmap[native]
            coef = x["coefficient"]
            if native == "DHB-glycyl-arginyl-DhbF":
                es = [
                    ev(
                        "MetaCyc:" + n,
                        f"The original {side} slot has coefficient {coef} for "
                        "DHB-glycyl-arginyl-DhbF. That arginyl name conflicts with the "
                        "threonyl precursor and primary structure; this edge is a "
                        "curated threonyl correction, not native-equation equivalence.",
                        f'Reaction[@frameid="{n}"]/{side}/Protein; {side}/coefficient',
                    ),
                    ev(
                        "metanetx.chemical:MNXM743865",
                        "The independently issued canonical name is the DHB-glycyl-L-threonyl "
                        "DhbF state; native SMILES encodes a 2S,3R threonyl thioester and "
                        "protein-continuation wildcards. It is a reactive class, not an "
                        "exact full protein or a sameAs claim to the old arginyl frame.",
                        "Unique MolecularEntity JSON-LD: identifier, name, smiles; "
                        "visible Properties: global charge -1",
                    ),
                    primary(
                        "Figure 1b depicts DHB-Gly-L-Thr bound to the second DhbF CP "
                        "and its trimeric cyclorelease. Figure 5 supports L-Thr "
                        "selection; Figure 6 detects reconstituted bacillibactin.",
                        "PDF p.4 Figure 1b; p.8 Figure 5; pp.8-9 Figure 6",
                    ),
                ]
                desc = (
                    f"Coefficient {coef}. Primary-supported threonyl reactive-state "
                    "correction under the native transformation identity. The native "
                    "arginyl frame and imported MNX sameAs are not accepted as exact "
                    "equivalents. Coefficients count formal carrier states, not whole "
                    "DhbF polypeptides."
                )
            else:
                es = [
                    ev(
                        "MetaCyc:" + n,
                        f"The native {side} slot specifies {native} with coefficient {coef}. "
                        f"The source direction is {d['direction']}; the displayed side "
                        "follows the biosynthetic transformation.",
                        f'Reaction[@frameid="{n}"]/{side}/*[@frameid="{native}"]; '
                        f"{side}/coefficient; reaction-direction",
                    )
                ]
                if cid.startswith("CHEBI:"):
                    es.append(
                        ev(
                            "MetaCyc:" + native,
                            f"The native CML and InChI define the ionic structure "
                            f"selected as {cid}; identity is checked independently "
                            "against the complete ChEBI term, not its display name.",
                            f'Compound[@frameid="{native}"]/cml/molecule; inchi',
                        )
                    )
                    es.append(
                        ev(
                            "CHEBI:30616",
                            f"{cid} has the same complete InChI, elemental formula "
                            "and charge as this native compound; the selected label "
                            "is its canonical ChEBI label.",
                            f'statements WHERE subject="{cid}"; '
                            "chemrof:inchi_string, chemrof:generalized_empirical_formula, "
                            "chemrof:charge, rdfs:label",
                        )
                    )
                else:
                    es.append(
                        ev(
                            "MetaCyc:" + native,
                            (
                                "This native protein class names the specified covalent "
                                "carrier state. It does not identify a KH3-4 sequence "
                                "or establish whole-enzyme stoichiometry."
                                if native in carrier_names
                                else "The native compound frame supplies its exact chemical "
                                "structure, stereochemical InChI and charge; no neutral "
                                "or unspecified-anomer cross-reference is substituted."
                            ),
                            f'{obj(native).tag}[@frameid="{native}"]/'
                            + (
                                "common-name; parent; unmodified-form"
                                if native in carrier_names
                                else "common-name; cml/molecule; inchi"
                            ),
                        )
                    )
                desc = f"Coefficient {coef}."
                if native in carrier_names:
                    desc += (
                        " Native carrier-state class, not an exact full polypeptide. "
                        "DhbF contains two CP sites; state coefficients do not count "
                        "whole NRPS molecules."
                    )
            edge("MetaCyc:" + n, predicate, cid, es, desc)

# Functional gene-product roles preserve evidence tier and do not assert monomer sufficiency.
roles = {
    "ISOCHORSYN-RXN": "BDG45612.1",
    "ISOCHORMAT-RXN": "BDG45614.1",
    "DHBDEHYD-RXN": "BDG45611.1",
    "DHBAMPLIG-RXN": "BDG45613.1",
    "RXN-19449": "BDG45613.1",
}
roles.update({n: "BDG45615.1" for n in steps[5:]})
for n in steps:
    a = roles[n]
    pe = ev(
        "NCBIProtein:" + a,
        f"The versioned GenPept entry {a} identifies Parageobacillus sp. KH3-4, "
        "taxon 2916802, and its AP025627.1 coding region. The native gene product "
        "is distinguished from tagged experimental constructs and carrier classes.",
        f'GBSeq[GBSeq_accession-version="{a}"]/GBSeq_definition; '
        "GBSeq_feature-table/GBFeature/GBFeature_quals (coded_by, db_xref, locus_tag)",
    )
    if n in steps[:3]:
        es = [
            pe,
            primary(
                "The KH3-4 cluster on AP025627 contains dhbACB assigned to "
                "2,3-DHB production from chorismate. These upstream activities "
                "were not individually assayed in the NRPS reconstitution "
                "that begins with supplied 2,3-DHB.",
                "PDF p.4, Results and Discussion, KH3-4 gene cluster; Figure 1a",
            ),
            ev(
                "NCBIProtein:" + a,
                "The product annotation and similarity-based CDS inference support "
                "this proposed upstream activity. They are annotation evidence, "
                "not direct purified-enzyme evidence for the selected KH3-4 protein.",
                f'GBSeq[GBSeq_accession-version="{a}"]/GBSeq_feature-table/'
                "GBFeature/GBFeature_quals (product, inference)",
            ),
        ]
        desc = (
            "Annotation-supported KH3-4 gene-product assignment for the complete "
            "upstream DHB module. No purified activity or active oligomer is "
            "established for this selected protein by the 2025 study."
        )
    else:
        assertion = (
            "DhbE preferentially activates 2,3-DHB; the loading model transfers "
            "the activated acyl group to DhbB. The purified KH3-4-derived "
            "preparations support complete NRPS product formation, not a "
            "separate kinetic assay of every bound transfer."
            if a == "BDG45613.1"
            else "DhbF module 1 prefers glycine and module 2 L-threonine. Figure 1b "
            "assigns loading, condensations and TE cyclorelease; purified "
            "KH3-4-derived NRPS preparations generate bacillibactin. Not every "
            "bound transfer was assayed separately."
        )
        es = [
            pe,
            primary(
                assertion,
                "PDF p.4 Figure 1b; pp.7-8 Figure 5 and substrate-specificity "
                "paragraphs; pp.8-9 Figure 6",
            ),
            primary(
                f"Methods explicitly identify {a.split('.')[0]} as the KH3-4 "
                "gene source for the recombinant protein. Tags and coexpression "
                "mean the preparation is not claimed to be an independently "
                "sequence-verified native full protein.",
                "PDF p.12, Experimental Section, Plasmid construction; "
                "pp.12-13 Production and purification",
            ),
        ]
        desc = (
            "Functional gene-product role supported by the primary mechanistic model "
            "and KH3-4-derived recombinant preparations. This does not establish "
            "monomer sufficiency, fixed assembly stoichiometry or separately "
            "measured flux for every carrier-bound step."
        )
    edge("NCBIProtein:" + a, "enables", "MetaCyc:" + n, es, desc)

for n in steps:
    module = "PWY-5901" if n in steps[:3] else "PWY-5903"
    es = [
        ev(
            "MetaCyc:" + module,
            f"The original reaction-list includes {n}; this complete module member "
            "is retained in the chorismate-to-bacillibactin route.",
            f'Pathway[@frameid="{module}"]/reaction-list/Reaction',
        )
    ]
    if module == "PWY-5901":
        es.append(
            ev(
                "MetaCyc:PWY-5903",
                "PWY-5903 explicitly includes PWY-5901 as its upstream nested pathway.",
                'Pathway[@frameid="PWY-5903"]/reaction-list/Pathway',
            )
        )
    edge("MetaCyc:" + n, "part_of", "MetaCyc:PWY-5903", es)

# Explicitly supported substrate handoffs, not a falsely linear order of parallel A domains.
flows = [
    (0, 1, "ISOCHORISMATE"),
    (1, 2, "DIHYDRO-DIOH-BENZOATE"),
    (2, 3, "2-3-DIHYDROXYBENZOATE"),
    (3, 4, "CPD-62"),
    (4, 7, "23-dihydroxybenzoyl-DhbB"),
    (5, 6, "CPD-9993"),
    (6, 7, "Glycyl-DhbF"),
    (7, 10, "DHB-glycyl-DhbF"),
    (8, 9, "CPD-9994"),
    (9, 10, "Threonyl-DhbF"),
    (10, 11, "DHB-glycyl-arginyl-DhbF"),
]
for i, j, mid in flows:
    a, b = steps[i], steps[j]
    if mid == "DHB-glycyl-arginyl-DhbF":
        es = [
            primary(
                "The second DhbF condensation domain forms the DHB-Gly-L-Thr "
                "carrier-bound unit; the TE domain then mediates trimeric "
                "cyclorelease to bacillibactin.",
                "PDF p.4 Figure 1b and caption",
            ),
            ev(
                "metanetx.chemical:MNXM743865",
                "The selected intermediate is the independently named DHB-glycyl-L-threonyl "
                "DhbF reactive class; old arginyl cross-references are not exact mappings.",
                "Unique MolecularEntity JSON-LD: identifier, name, smiles",
            ),
        ]
    else:
        es = [
            ev(
                "MetaCyc:" + a,
                f"The native product slot contains {mid}.",
                f'Reaction[@frameid="{a}"]/right/*[@frameid="{mid}"]',
            ),
            ev(
                "MetaCyc:" + b,
                f"The native substrate slot contains {mid}.",
                f'Reaction[@frameid="{b}"]/left/*[@frameid="{mid}"]',
            ),
        ]
    edge(
        "MetaCyc:" + a,
        "provides_input_for",
        "MetaCyc:" + b,
        es,
        "Shared intermediate: " + chemmap[mid] + ". This is a chemical handoff, "
        "not an assertion of physical channeling or a single linear activation order.",
    )

for a, state in [("BDG45614.1", "DhbB"), ("BDG45615.1", "DhbF")]:
    es = [
        ev(
            "NCBIProtein:BDG45617.1",
            "The original versioned KH3-4 GenPept entry identifies the cluster "
            "4-prime-phosphopantetheinyl transferase and its AP025627.1 coding region.",
            'GBSeq[GBSeq_accession-version="BDG45617.1"]/GBSeq_definition; '
            "GBSeq_feature-table/GBFeature/GBFeature_quals",
        ),
        primary(
            "Methods identify BDG45617 as the KH3-4 PPTase gene and "
            "BDG45614/BDG45615 as DhbB/DhbF. The proteins were expressed with tags "
            "and/or coexpression; this identifies native gene sources, not fully "
            "verified engineered construct sequences.",
            "PDF p.12, Plasmid construction; pp.12-13, Production and purification",
        ),
    ]
    if state == "DhbB":
        es.append(
            primary(
                "Purified PPTase and CoA increase apo-DhbB mass by about 340 Da. "
                "The no-PPTase control and coexpression preparation support "
                "phosphopantetheinylation. The printed coexpression primer "
                "discrepancy limits exact construct reconstruction.",
                "PDF pp.5-6, PPTase Results and Figure 3; p.14, PPTase assay; p.19, SI Table S1",
            )
        )
        desc = (
            "Activation by phosphopantetheinylation in the KH3-4-derived preparation; "
            "DhbB modification was measured directly. The printed coexpression "
            "primer mismatch does not prove that an incorrect plasmid was used."
        )
    else:
        es.append(
            primary(
                "DhbF was coexpressed with PPTase and the resulting preparation "
                "was used as holo-DhbF in active NRPS reconstitution. Its large "
                "mass excluded direct MALDI modification analysis; full "
                "site occupancy was not independently measured.",
                "PDF pp.5-7, PPTase Results and Figure 3 discussion; "
                "pp.12-14, coexpression and reconstitution Methods",
            )
        )
        desc = (
            "PPTase-dependent activation model supported by coexpression and function. "
            "Both DhbF carrier-site occupancies were not directly measured; "
            "this is weaker evidence than the measured DhbB mass shift."
        )
    edge("NCBIProtein:BDG45617.1", "activates", "NCBIProtein:" + a, es, desc)
edge(
    "MetaCyc:PWY-5903",
    "occurs_in",
    "NCBITaxon:2916802",
    [
        ev(
            "NCBITaxon:2916802",
            "NCBI Taxonomy identifies Parageobacillus sp. KH3-4 as taxon 2916802.",
            'TaxaSet/Taxon[TaxId="2916802"]/ScientificName',
        ),
        primary(
            "KH3-4 cultures produced bacillibactin, and purified KH3-4-derived "
            "NRPS proteins reconstituted it from supplied DHB, glycine and "
            "L-threonine. The complete upstream chorismate module remains annotated.",
            "PDF pp.4-5, Figure 2 and gene cluster; pp.8-9, Figure 6; "
            "pp.11-14, strains, construct and reconstitution Methods",
        ),
    ],
)
# Schema occurs_in is cellular-component only: organism scope is declared by taxa, not a false edge.
edges.pop()
record = {
    "id": "MetaCyc:PWY-5903",
    "label": "bacillibactin biosynthesis",
    "description": (
        "Complete twelve-transformation chorismate-to-bacillibactin pathway in "
        "Parageobacillus sp. KH3-4: three upstream 2,3-dihydroxybenzoate reactions "
        "and nine carrier-dependent NRPS transformations. The upstream DhbA/C/B "
        "activities are genome and cluster annotations; the 2025 purified reconstitution "
        "starts with supplied 2,3-DHB, glycine and L-threonine. The native DhbF model "
        "retains both CP sites, condensations and TE-mediated trimeric cyclorelease. "
        "The old MetaCyc terminal arginyl carrier is chemically inconsistent with "
        "its threonyl precursor and primary structure. The independently issued "
        "MetaNetX threonyl reactive-state class is selected explicitly under the "
        "same native transformation identities; no exact equivalence to the old "
        "arginyl frame or imported ModelSEED alias is asserted. Carrier classes "
        "represent covalent reactive states with unspecified protein continuations, "
        "not exact KH3-4 sequences or whole-polypeptide stoichiometry. Three ATP "
        "adenylations per repeat imply nine ATP per trimer as mechanistic bookkeeping, "
        "not a measured ATP/product ratio; the conflicting native six-ATP composite "
        "is excluded rather than added to these twelve steps. The primary accession "
        "bridge identifies native gene sources, while tags, domain truncations and "
        "a contradictory printed DhbB coexpression primer limit exact engineered "
        "construct identity. DhbB phosphopantetheinylation was measured; DhbF maturation "
        "is supported by coexpression and function without direct occupancy measurement. "
        "MbtH was included in reconstitution, but its isolated requirement and stable "
        "complex stoichiometry were not established. Mg2+ was an assay condition, "
        "not an independently demonstrated free cofactor dependency. No native "
        "assembly stoichiometry, cellular location, transporter or regulation is "
        "transferred from B. subtilis. The strain-168 sfp0 defect and engineered "
        "E. coli expression host do not define KH3-4 biology. Ferric loading, uptake, "
        "mutasynthetic analogues and downstream utilization are outside this "
        "complete biosynthetic boundary."
    ),
    "pathway_type": "bacillibactin-biosynthesis",
    "taxa": [{"id": "NCBITaxon:2916802", "label": "Parageobacillus sp. KH3-4"}],
    "participants": participants,
    "reactions": reactions,
    "mechanistic_edges": edges,
    "references": refs,
}
OUT.mkdir(exist_ok=True)
p = OUT / "bacillibactin-biosynthesis.yaml"
p.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=98))
projection = {
    "record_sha256": sha(p),
    "native_pathway": "MetaCyc:PWY-5903",
    "native_nested_pathway": "MetaCyc:PWY-5901",
    "native_reactions": side_projection,
    "selected_native_to_graph": chemmap,
    "native_boundary": {"direct": steps[3:], "nested": steps[:3], "total": 12},
    "graph_to_source": [
        {
            "edge_id": x["id"],
            "subject": x["subject"],
            "predicate": x["predicate"],
            "object": x["object"],
            "evidence": x["evidence"],
        }
        for x in edges
    ],
    "rejected_equivalence": ["MetaCyc:DHB-glycyl-arginyl-DhbF", "ModelSEED:cpd36242"],
    "excluded_composite": "MetaCyc:RXN-9374",
    "whole_polypeptide_balance_claimed": False,
}
(OUT / "bacillibactin-source-projection.json").write_text(json.dumps(projection, indent=2) + "\n")
(ROOT / "reference-paths.json").write_text(json.dumps(refpaths, indent=2) + "\n")
ids = {
    section: [{"id": x["id"], "label": x["label"]} for x in record[section]]
    for section in ["taxa", "participants", "reactions"]
}
ids["record"] = {"id": record["id"], "label": record["label"]}
ids["record_sha256"] = sha(p)
(OUT / "bacillibactin-identifiers.json").write_text(json.dumps(ids, indent=2) + "\n")
print(
    json.dumps(
        {
            "target_sha256": sha(p),
            "participants": len(participants),
            "reactions": len(reactions),
            "edges": len(edges),
            "evidence": sum(len(x["evidence"]) for x in edges),
            "references": len(refs),
        },
        indent=2,
    )
)
