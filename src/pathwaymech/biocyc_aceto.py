"""Closed aceto authority profiles with complete originals and companion proof.

Retained source context is not a new scientific claim. Offline reconstruction
checks internal coherence; only the producer hashes the issuing response bytes.
"""

from __future__ import annotations

import copy
import json
import math
import re
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import (
    FRAME,
    HOST,
    PROVENANCE,
    PROVENANCE_ORDER,
    _TreeBuilder,
    keys,
    name,
    one,
    original_path,
    request,
    require,
    scalar,
)
from pathwaymech.biocyc_native_context import (
    ancillary,
    attributes,
    blank,
    context_identity,
    direct_names,
    integer,
    rebuild,
    ref_node,
    refs,
    retained,
)
from pathwaymech.biocyc_pathway import CORE as PATHWAY_CORE
from pathwaymech.biocyc_pathway import project as pathway_project
from pathwaymech.ecocyc_complex import ECOCYC_COMPLEX_KIND
from pathwaymech.ecocyc_named_complex import NAMED_COMPLEX_KIND, validate_named_complex_graph
from pathwaymech.ecocyc_named_complex import project as named_project

SGD_KIND = "metacyc-sgd-pathway-xml"
NESTED_KIND = "ecocyc-nested-complex-xml"
ACYL_KIND = "metacyc-acyl-transfer-composite-xml"
RESIDUE_KIND = "metacyc-protein-residue-class-xml"
ACETO_KINDS = {SGD_KIND, NESTED_KIND, ACYL_KIND, RESIDUE_KIND}
FIELD = "native_aceto"
COMPANION_FIELDS = {
    NESTED_KIND: "component_sources",
    ACYL_KIND: "constituent_sources",
    RESIDUE_KIND: "parent_source",
}
MODES = {
    SGD_KIND: ("META", "Pathway", False),
    NESTED_KIND: ("ECOLI", "Protein", False),
    ACYL_KIND: ("META", "Reaction", False),
    RESIDUE_KIND: ("META", "Compound", True),
    "named": ("ECOLI", "Protein", False),
    "constituent": ("META", "Reaction", False),
    "residue-parent": ("META", "Compound", True),
}


def source_frame(source: dict, mode: str) -> str:
    keys(source, PROVENANCE, "invalid aceto provenance")
    require(
        all(isinstance(v, str) and v.strip() for v in source.values()), "empty aceto provenance"
    )
    require(re.fullmatch(r"[0-9a-f]{64}", source["sha256"]) is not None, "invalid original hash")
    if mode == SGD_KIND:
        match = re.fullmatch(
            rf"https://pathway\.yeastgenome\.org/getxml\?META:({FRAME})", source["url"]
        )
        require(
            match is not None and source["version"] == "22.5", "unsupported SGD request/release"
        )
        return match[1]
    require(source["version"] == "27.0", "unsupported native aceto release")
    return request(source["url"], MODES[mode][0])


def envelope(root: ET.Element, source: dict, mode: str) -> tuple[ET.Element, str, dict]:
    frame = source_frame(source, mode)
    pgdb, tag, is_class = MODES[mode]
    requested = pgdb + ":" + frame
    require(root.tag == "ptools-xml" and len(root) == 2, "requires one whole native object")
    meta = one(root, "metadata")
    entity = next(n for n in root if n.tag != "metadata")
    for n in (root, meta, entity):
        blank(n)
    legacy = (
        "http://pathway-2a.yeastgenome.org:8080/" if mode == SGD_KIND else f"http://{HOST}:443/"
    )
    bases = {legacy + "getxml?" + requested}
    services = {legacy}
    if mode != SGD_KIND:
        bases.add(source["url"])
        services.add(f"https://{HOST}/")
    require(
        root.attrib.keys() == {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        and root.get("ptools-version") == source["version"]
        and root.get("{http://www.w3.org/XML/1998/namespace}base") in bases,
        "native envelope version/base mismatch",
    )
    require(
        not meta.attrib
        and sorted(n.tag for n in meta)
        == sorted(["url", "service_name", "query", "num_results", "PGDB"]),
        "malformed metadata",
    )
    require(
        scalar(meta, "url") in services
        and scalar(meta, "service_name") == "getxml"
        and scalar(meta, "query") == requested
        and scalar(meta, "num_results") == "1",
        "native service/query mismatch",
    )
    database = one(meta, "PGDB")
    blank(database)
    require(database.attrib == {"orgid": pgdb, "version": source["version"]}, "PGDB mismatch")
    if pgdb == "META":
        require(
            [n.tag for n in database] == ["species"]
            and scalar(database, "species", True) == "MetaCyc",
            "META species mismatch",
        )
    else:
        require(
            sorted(n.tag for n in database) == ["dblink", "species", "strain"]
            and scalar(database, "species", True) == "Escherichia coli"
            and scalar(database, "strain", True) == "K-12 substr. MG1655",
            "ECOLI taxon mismatch",
        )
        db = one(database, "dblink")
        blank(db)
        require(
            not db.attrib
            and sorted(n.tag for n in db)
            == sorted(["dblink-db", "dblink-oid", "dblink-relationship", "dblink-URL"])
            and scalar(db, "dblink-db") == "NCBI-TAXONOMY-DB"
            and scalar(db, "dblink-oid") == "511145"
            and scalar(db, "dblink-relationship") == "unification"
            and scalar(db, "dblink-URL")
            == "http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=511145",
            "ECOLI native taxon mismatch",
        )
    attributes(entity, frame, pgdb, tag, is_class)
    return (
        entity,
        frame,
        {"attributes": dict(root.attrib), "metadata_xml": ET.tostring(meta, encoding="unicode")},
    )


def evidence(node: ET.Element, code: str, *, publication: bool = False) -> None:
    blank(node)
    require(
        not node.attrib
        and sorted(n.tag for n in node)
        == (["Evidence-Code", "Publication"] if publication else ["Evidence-Code"]),
        "invalid evidence wrapper",
    )
    ev = one(node, "Evidence-Code")
    attributes(ev, code, "META", "Evidence-Code", True)
    require(
        sorted(n.tag for n in ev) == ["comment", "common-name"], "unsupported whole evidence code"
    )
    name(one(ev, "common-name"), code)
    scalar(ev, "comment", True)
    if publication:
        pub = one(node, "Publication")
        context_identity(pub, "META", "Publication")
        require(
            "class" not in pub.attrib and "resource" not in pub.attrib,
            "requires whole publication instance",
        )
        allowed = {"author", "title", "year", "url", "source", "pubmed-id"}
        require(
            all(n.tag in allowed for n in pub) and len(pub) > 0, "unsupported publication context"
        )
        for tag in allowed - {"author"}:
            require(len(pub.findall(tag)) <= 1, "duplicate publication field")
        for n in pub:
            require(
                n.attrib == {"datatype": "integer" if n.tag == "year" else "string"}
                and not len(n)
                and bool((n.text or "").strip()),
                "invalid publication scalar",
            )
            if n.tag in {"year", "pubmed-id"}:
                require(
                    re.fullmatch(r"[0-9]+", n.text or "") is not None, "invalid publication number"
                )


def sgd_project(entity: ET.Element, frame: str) -> dict:
    reduced = copy.deepcopy(entity)
    for n in list(reduced):
        if n.tag in {"evidence", "pathway-link"}:
            reduced.remove(n)
    native = pathway_project(reduced, frame)
    evidence(one(entity, "evidence"), "EV-EXP")
    links, seen = [], set()
    for wrapper in entity.findall("pathway-link"):
        blank(wrapper)
        require(
            not wrapper.attrib and all(n.tag in {"Compound", "link-target"} for n in wrapper),
            "invalid pathway link",
        )
        compound = ref_node(one(wrapper, "Compound"), "META", "Compound")
        targets = []
        for target in wrapper.findall("link-target"):
            blank(target)
            require(not target.attrib and len(target) == 1, "invalid pathway link target")
            targets.append(ref_node(target[0], "META", "Pathway"))
        require(
            targets and len({n["id"] for n in targets}) == len(targets),
            "empty/duplicate pathway link target",
        )
        require(compound["id"] not in seen, "duplicate pathway link compound")
        seen.add(compound["id"])
        links.append({"compound": compound, "targets": targets})
    require(len(links) == 2, "requires two whole pathway interfaces")
    return {**native, "pathway_links": links, **retained(entity, PATHWAY_CORE)}


def nested_project(entity: ET.Element, frame: str) -> dict:
    attributes(entity, frame, "ECOLI", "Protein", False)
    core = {"parent", "component"}
    ancillary(entity, {"comment", "molecular-weight-exp", "catalyzes"}, core, "ECOLI")
    parents = refs(entity, "parent", "ECOLI", "Protein", is_class=True)
    require(
        [n["attributes"]["frameid"] for n in parents] == ["Protein-Complexes"],
        "unsupported nested parent",
    )
    components = []
    for n in entity.findall("component"):
        blank(n)
        require(
            not n.attrib and sorted(c.tag for c in n) == ["Protein", "coefficient"],
            "invalid nested component",
        )
        child = ref_node(one(n, "Protein"), "ECOLI", "Protein")
        require(
            child["attributes"]["frameid"] != frame and integer(one(n, "coefficient")) == 1,
            "requires nonself coefficient-one child",
        )
        components.append({"entity": child, "coefficient": 1})
    require(
        len(components) == 2 and len({n["entity"]["id"] for n in components}) == 2,
        "requires two distinct nested children",
    )
    activity = one(one(entity, "catalyzes"), "Enzymatic-Reaction")
    require(
        all(n.tag in {"enzyme", "reaction", "common-name", "synonym"} for n in activity),
        "unsupported nested activity context",
    )
    require(
        one(one(activity, "enzyme"), "Protein").get("frameid") == frame,
        "activity enzyme backreference mismatch",
    )
    one(entity, "molecular-weight-exp")
    return {
        "id": "EcoCyc:" + frame,
        "native_type": "Protein",
        "is_class": False,
        "parent_classes": parents,
        "components": components,
        **retained(entity, core),
    }


def reaction_project(entity: ET.Element, frame: str, *, constituent: bool = False) -> dict:
    attributes(entity, frame, "META", "Reaction", False)
    core = {"parent", "reaction-direction", "left", "right"}
    if constituent:
        core.add("in-pathway")
    else:
        core.add("reaction-list")
    ancillary(
        entity,
        {
            "gibbs-0",
            "orphan",
            "physiologically-relevant",
            "credits",
            "in-pathway",
            "enzymatic-reaction",
            "dblink",
            "ec-number",
        },
        core,
        "META",
    )
    parents = refs(entity, "parent", "META", "Reaction", is_class=True)
    require(
        {n["attributes"]["frameid"] for n in parents}
        == {
            "Chemical-Reactions" if constituent else "Composite-Reactions",
            "Small-Molecule-Reactions",
        },
        "unsupported acyl reaction parents",
    )
    require(
        scalar(entity, "reaction-direction") == "REVERSIBLE", "requires native reversible direction"
    )
    if not constituent:
        require(
            one(entity, "ec-number").text == "EC-2.3.1.16", "unsupported acyl transfer EC context"
        )
    for g in entity.findall("gibbs-0"):
        for ev in g:
            evidence(ev, "EV-COMP", publication=True)
    sides = []
    for side in ["left", "right"]:
        seen = set()
        require(bool(entity.findall(side)), "empty acyl side")
        for ordinal, wrapper in enumerate(entity.findall(side), 1):
            blank(wrapper)
            require(
                not wrapper.attrib and all(n.tag in {"Compound", "coefficient"} for n in wrapper),
                "unsupported acyl side",
            )
            c = one(wrapper, "Compound")
            ref = ref_node(c, "META", "Compound", is_class=c.get("class") == "true")
            if c.get("frameid") in {"PROT-CYS", "Protein-S-Acetyl-Cysteines"}:
                require(ref["is_class"], "residue occurrence must remain a class")
            coeffs = wrapper.findall("coefficient")
            require(len(coeffs) <= 1, "duplicate side coefficient")
            coefficient = integer(coeffs[0]) if coeffs else 1
            key = ref["id"], ref["is_class"]
            require(key not in seen, "duplicate same-side occurrence")
            seen.add(key)
            sides.append(
                {
                    "side": side,
                    "ordinal": ordinal,
                    "source_position": list(entity).index(wrapper),
                    "entity": ref,
                    "coefficient": coefficient,
                    "coefficient_explicit": bool(coeffs),
                }
            )
    native = {
        "id": "MetaCyc:" + frame,
        "native_type": "Reaction",
        "is_class": False,
        "parent_classes": parents,
        "direction": "REVERSIBLE",
        "sides": sides,
    }
    if constituent:
        wrapper = one(entity, "in-pathway")
        blank(wrapper)
        require(not wrapper.attrib and len(wrapper) == 1, "invalid constituent backlink")
        native["parent_reaction"] = ref_node(wrapper[0], "META", "Reaction")
    else:
        listing = one(entity, "reaction-list")
        blank(listing)
        require(not listing.attrib and len(listing) == 2, "requires two constituent reactions")
        members = [ref_node(n, "META", "Reaction") for n in listing]
        require(
            len({n["id"] for n in members}) == 2
            and "MetaCyc:" + frame not in {n["id"] for n in members},
            "duplicate/self constituent",
        )
        native["reaction_list"] = members
    return {**native, **retained(entity, core)}


def cml(entity: ET.Element) -> None:
    molecule = one(one(entity, "cml"), "molecule")
    # Basic closed molecule/formula fields were checked by ancillary().
    require(
        [n.tag for n in molecule] == ["atomArray", "bondArray", "formula", "string"],
        "unsupported residue CML shape",
    )
    atoms, elements = set(), []
    array = one(molecule, "atomArray")
    blank(array)
    require(not array.attrib and len(array) > 0, "empty/attributed atom array")
    for atom in array:
        require(
            atom.tag == "atom"
            and set(atom.attrib) == {"id", "elementType", "x2", "y2"}
            and not len(atom)
            and not (atom.text or "").strip(),
            "invalid CML atom",
        )
        ident = atom.get("id")
        require(ident and ident not in atoms, "duplicate/empty CML atom ID")
        atoms.add(ident)
        elements.append(atom.get("elementType"))
        require(
            elements[-1] in {"C", "N", "O", "S", "Proteins", "R"}, "unsupported residue atom type"
        )
        for coord in ["x2", "y2"]:
            require(math.isfinite(float(atom.get(coord))), "nonfinite atom coordinate")
    require(
        elements.count("Proteins") == 2,
        "protein-bound residue requires two literal Proteins endpoints",
    )
    if entity.get("frameid") in {"Protein-L-amino-Acids", "Protein-S-Acyl-Cysteines"}:
        require("R" in elements, "generic parent requires literal R endpoint")
    bonds = set()
    array = one(molecule, "bondArray")
    blank(array)
    require(not array.attrib and len(array) > 0, "empty/attributed bond array")
    for bond in array:
        require(
            bond.tag == "bond"
            and set(bond.attrib) == {"id", "atomRefs", "order"}
            and not len(bond)
            and not (bond.text or "").strip(),
            "invalid CML bond",
        )
        ident = bond.get("id")
        require(ident and ident not in bonds and ident not in atoms, "duplicate CML bond ID")
        bonds.add(ident)
        targets = bond.get("atomRefs").split()
        require(
            len(targets) == 2
            and len(set(targets)) == 2
            and set(targets) <= atoms
            and bond.get("order") in {"1", "2", "3"},
            "invalid bond reference/order",
        )
    require(
        one(molecule, "formula").attrib == {"concise": ""},
        "generic residue formula must remain unspecified",
    )
    string = one(molecule, "string")
    require(
        string.attrib == {"title": "smiles"}
        and not len(string)
        and bool((string.text or "").strip()),
        "invalid residue smiles serialization",
    )


def residue_project(entity: ET.Element, frame: str, *, parent: bool = False) -> dict:
    attributes(entity, frame, "META", "Compound", True)
    core = {"parent", "subclass", "common-name", "synonym", "n-name"}
    ancillary(
        entity,
        {
            "cml",
            "credits",
            "comment",
            "appears-in-left-side-of",
            "appears-in-right-side-of",
            "citation",
            "dblink",
        },
        core,
        "META",
    )
    parents = refs(entity, "parent", "META", "Compound", is_class=True)
    expected = (
        {
            "Protein-L-amino-Acids": "Protein-Amino-Acids",
            "Protein-S-Acyl-Cysteines": "Protein-Modified-Amino-Acids",
        }
        if parent
        else {
            "PROT-CYS": "Protein-L-amino-Acids",
            "Protein-S-Acetyl-Cysteines": "Protein-S-Acyl-Cysteines",
        }
    )
    require(
        frame in expected and [n["attributes"]["frameid"] for n in parents] == [expected[frame]],
        "unsupported protein-residue parent profile",
    )
    label, synonyms = direct_names(entity, frame)
    require(len(entity.findall("n-name")) <= 1, "duplicate native n-name")
    if entity.findall("n-name"):
        scalar(entity, "n-name", True)
    subclasses = []
    for w in entity.findall("subclass"):
        blank(w)
        require(not w.attrib and len(w) == 1, "invalid subclass wrapper")
        tag = (
            "Protein"
            if parent and w[0].get("frameid") == "Apo-Base-off-His-on-Enzymes"
            else "Compound"
        )
        subclasses.append(ref_node(w[0], "META", tag, is_class=True))
    require(
        len({n["id"] for n in subclasses}) == len(subclasses)
        and "MetaCyc:" + frame not in {n["id"] for n in subclasses},
        "duplicate/self residue subclass",
    )
    cml(entity)
    return {
        "id": "MetaCyc:" + frame,
        "native_type": "Compound",
        "is_class": True,
        "parent_classes": parents,
        "direct_common_name": label,
        "direct_synonyms": synonyms,
        "subclasses": subclasses,
        **retained(entity, core),
    }


def project(entity: ET.Element, frame: str, mode: str) -> dict:
    if mode == SGD_KIND:
        return sgd_project(entity, frame)
    if mode == NESTED_KIND:
        return nested_project(entity, frame)
    if mode == "named":
        return named_project(entity, frame)
    if mode in {ACYL_KIND, "constituent"}:
        return reaction_project(entity, frame, constituent=mode == "constituent")
    return residue_project(entity, frame, parent=mode == "residue-parent")


def document(root: ET.Element, source: dict, mode: str) -> dict:
    entity, frame, env = envelope(root, source, mode)
    return {"envelope": env, "native": project(entity, frame, mode)}


def restore(value: dict, source: dict, mode: str) -> dict:
    keys(value, {"envelope", "native"}, "invalid whole document fields")
    env = value["envelope"]
    keys(env, {"attributes", "metadata_xml"}, "invalid retained envelope")
    require(
        isinstance(env["attributes"], dict)
        and all(isinstance(k, str) and isinstance(v, str) for k, v in env["attributes"].items())
        and isinstance(env["metadata_xml"], str),
        "invalid retained envelope values",
    )
    root = ET.Element("ptools-xml", env["attributes"])
    holder = ET.fromstring(
        "<retained>" + env["metadata_xml"] + "</retained>",
        parser=ET.XMLParser(target=_TreeBuilder()),
    )
    require(
        len(holder) == 1 and not (holder.text or "").strip(), "invalid retained metadata wrapper"
    )
    root.append(holder[0])
    root.append(rebuild(value["native"], MODES[mode][1]))
    result = document(root, source, mode)
    require(
        json.dumps(result, sort_keys=True) == json.dumps(value, sort_keys=True),
        "whole document projection mismatch",
    )
    return result


def relations(mode: str, native: dict, companions: list[dict]) -> None:
    if mode == SGD_KIND:
        require(not companions, "SGD pathway has no companions")
    elif mode == NESTED_KIND:
        require(
            [c["document"]["native"]["id"] for c in companions]
            == [c["entity"]["id"] for c in native["components"]],
            "nested companion identities/order mismatch",
        )
        leaves = []
        for c in companions:
            child = c["document"]["native"]
            require(
                len(child["components"]) == 1 and child["components"][0]["coefficient"] >= 2,
                "child must be named homomer",
            )
            leaf = child["components"][0]["entity"]["id"]
            require(
                leaf not in {native["id"], *[v["entity"]["id"] for v in native["components"]]},
                "forward nested cycle",
            )
            leaves.append(leaf)
            back = refs(
                rebuild(child, "Protein"), "component-of", "ECOLI", "Protein", is_class=False
            )
            require([n["id"] for n in back] == [native["id"]], "child reciprocal parent mismatch")
        require(len(set(leaves)) == 2, "duplicate leaf across nested children")
    elif mode == ACYL_KIND:
        require(
            [c["document"]["native"]["id"] for c in companions]
            == [c["id"] for c in native["reaction_list"]],
            "constituent identities/order mismatch",
        )

        def net(n):
            counter = Counter()
            for s in n["sides"]:
                counter[
                    (s["entity"]["id"], s["entity"]["native_type"], s["entity"]["is_class"])
                ] += s["coefficient"] * (1 if s["side"] == "right" else -1)
            return counter

        total = Counter()
        for c in companions:
            child = c["document"]["native"]
            require(
                child["parent_reaction"]["id"] == native["id"],
                "constituent parent reaction mismatch",
            )
            total.update(net(child))
        require(
            {k: v for k, v in total.items() if v} == {k: v for k, v in net(native).items() if v},
            "constituent sum differs from composite",
        )
    else:
        require(
            len(companions) == 1
            and companions[0]["document"]["native"]["id"] == native["parent_classes"][0]["id"],
            "residue parent identity mismatch",
        )
        require(
            sum(
                n["id"] == native["id"] and n["native_type"] == "Compound" and n["is_class"]
                for n in companions[0]["document"]["native"]["subclasses"]
            )
            == 1,
            "parent lacks reciprocal selected residue",
        )


def companion_mode(kind: str) -> str:
    return {NESTED_KIND: "named", ACYL_KIND: "constituent", RESIDUE_KIND: "residue-parent"}[kind]


def aceto_metadata(entry: dict, cache_dir: Path) -> dict:
    kind = entry.get("kind")
    require(kind in ACETO_KINDS, "unknown aceto source kind")
    optional = {COMPANION_FIELDS[kind]} if kind in COMPANION_FIELDS else set()
    keys(
        entry, PROVENANCE | {"key", "kind", "path"} | optional, "unsupported aceto manifest fields"
    )
    require(isinstance(entry["key"], str) and entry["key"].strip(), "invalid source key")
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    root = ET.fromstring(
        original_path(entry, cache_dir).read_bytes(), parser=ET.XMLParser(target=_TreeBuilder())
    )
    doc = document(root, source, kind)
    companions = []
    if optional:
        descriptors = entry[COMPANION_FIELDS[kind]]
        descriptors = [descriptors] if kind == RESIDUE_KIND else descriptors
        require(
            isinstance(descriptors, list)
            and len(descriptors) == (1 if kind == RESIDUE_KIND else 2),
            "invalid companion count",
        )
        for descriptor in descriptors:
            keys(descriptor, PROVENANCE | {"path"}, "unsupported companion original fields")
            prov = {k: descriptor[k] for k in PROVENANCE_ORDER}
            body = original_path(descriptor, cache_dir).read_bytes()
            other = document(
                ET.fromstring(body, parser=ET.XMLParser(target=_TreeBuilder())),
                prov,
                companion_mode(kind),
            )
            companions.append({**prov, "document": other})
    result = {**source, "kind": kind, FIELD: {"document": doc, "companions": companions}}
    validate_aceto_metadata(result)
    return result


def validate_aceto_metadata(metadata: dict) -> None:
    keys(metadata, PROVENANCE | {"kind", FIELD}, "invalid aceto metadata fields")
    kind = metadata["kind"]
    require(kind in ACETO_KINDS, "unsupported aceto kind")
    source = {k: metadata[k] for k in PROVENANCE_ORDER}
    native = metadata[FIELD]
    keys(native, {"document", "companions"}, "invalid aceto native fields")
    restore(native["document"], source, kind)
    companions = native["companions"]
    require(isinstance(companions, list), "companions must be a list")
    require(
        len(companions) == (0 if kind == SGD_KIND else 1 if kind == RESIDUE_KIND else 2),
        "wrong companion cardinality",
    )
    for companion in companions:
        keys(companion, PROVENANCE | {"document"}, "invalid companion provenance")
        prov = {k: companion[k] for k in PROVENANCE_ORDER}
        require(prov["version"] == source["version"], "companion release mismatch")
        restore(companion["document"], prov, companion_mode(kind))
    relations(kind, native["document"]["native"], companions)


def aceto_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_aceto_metadata(metadata)
    native = metadata[FIELD]["document"]["native"]
    kind, ident = metadata["kind"], native["id"]
    frame = ident.split(":", 1)[1]
    label = native.get(
        "direct_common_name", "unnamed protein complex " + frame if kind == NESTED_KIND else frame
    )
    term = {
        "label": label,
        "synonyms": sorted(native.get("direct_synonyms", [])),
        "source": source,
        "entity_type": {
            SGD_KIND: "native_pathway",
            NESTED_KIND: "protein_complex",
            ACYL_KIND: "reaction",
            RESIDUE_KIND: "native_chemical_class",
        }[kind],
        "label_kind": "source_context" if kind in {NESTED_KIND, ACYL_KIND} else "canonical",
    }
    if kind == RESIDUE_KIND:
        term["allowed_categories"] = ["chemical_entity"]
    return ident, term


def validate_aceto_assertions(sources: dict, claims: list[tuple[str, str]]) -> None:
    """Compare all owners and embedded originals before corpus selection.

    Existing reduced ordinary Reaction metadata can prove only its typed ID and
    identical original provenance; it cannot replace the whole companion body.
    """
    assertions, origins, kinds, assemblies = {}, {}, {}, []
    protected = set()

    def add(ident, native, prov, kind):
        value = (json.dumps(native, sort_keys=True), prov["version"])
        require(
            ident not in assertions or assertions[ident] == value,
            "conflicting complete aceto assertion for " + ident,
        )
        origin = tuple(prov[k] for k in ("url", "version", "sha256"))
        require(
            ident not in origins or origins[ident] == origin,
            "conflicting companion original provenance for " + ident,
        )
        assertions[ident], origins[ident] = value, origin
        kinds.setdefault(ident, set()).add(kind)
        if "components" in native:
            assemblies.append(native)

    for metadata in sources.values():
        kind = metadata.get("kind")
        if kind in ACETO_KINDS:
            native = metadata[FIELD]["document"]["native"]
            add(native["id"], native, metadata, kind)
            protected.add(native["id"])
            for child in metadata[FIELD]["companions"]:
                n = child["document"]["native"]
                childkind = {
                    NESTED_KIND: NAMED_COMPLEX_KIND,
                    ACYL_KIND: "metacyc-reaction-xml",
                    RESIDUE_KIND: "residue-parent",
                }[kind]
                add(n["id"], n, child, childkind)
                protected.add(n["id"])
    if not protected:
        return
    for metadata in sources.values():
        kind = metadata.get("kind")
        if kind == NAMED_COMPLEX_KIND:
            n = metadata["native_named_complex"]
            if n["id"] in protected:
                add(n["id"], n, metadata, kind)
            else:
                assemblies.append(n)
        elif kind == ECOCYC_COMPLEX_KIND:
            # Legacy components use direct IDs. Adapt only the temporary forward
            # graph; preserve the validated source projection and reverse context.
            n = metadata["native_complex"]
            assemblies.append(
                {
                    "id": n["id"],
                    "components": [{"entity": {"id": c["id"]}} for c in n["components"]],
                }
            )
        elif kind == "metacyc-reaction-xml":
            ident = "MetaCyc:" + request(metadata["url"], "META")
            if ident in protected:
                require(
                    kind in kinds[ident]
                    and origins[ident] == tuple(metadata[k] for k in ("url", "version", "sha256")),
                    "constituent source provenance/type mismatch",
                )
    for metadata in sources.values():
        kind = metadata.get("kind")
        if kind in ACETO_KINDS:
            continue
        for field, native in metadata.items():
            if field.startswith("native_") and isinstance(native, dict):
                ident = native.get("id")
                if ident in protected:
                    require(
                        kind in kinds[ident], "conflicting unselected typed native identity scope"
                    )
    for ident, source in claims:
        if ident in protected:
            require(
                sources[source].get("kind") in kinds[ident],
                "typed aceto identity overwritten by another source kind",
            )
    validate_named_complex_graph(assemblies)
