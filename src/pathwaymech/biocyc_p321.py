"""Complete native P321 support: whole ETF carriers, singleton and gene scope.

These bounded source profiles establish issuing identities, not enzyme activity,
assembly stoichiometry, physiological donors or organism-specific gene identity.
Original XML is retained as base64 bytes and reparsed using its declared encoding.
"""

from __future__ import annotations

import base64
import binascii
import copy
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from xml.etree import ElementTree as ET

from pathwaymech.biocyc_carrier import (
    HOST,
    PROVENANCE,
    PROVENANCE_ORDER,
    _TreeBuilder,
    keys,
    one,
    original_path,
    provenance,
    require,
    scalar,
)
from pathwaymech.biocyc_native_context import (
    activity,
    ancillary,
    attributes,
    blank,
    context_identity,
    direct_names,
    integer,
    publication_context,
    ref_node,
    refs,
    retained,
)

ETF_REACTION_KIND = "metacyc-etf-reaction-xml"
ETF_CLASS_KIND = "metacyc-etf-class-xml"
SINGLETON_KIND = "metacyc-singleton-activity-xml"
GENE_KIND = "metacyc-gene-xml"
P321_KINDS = {ETF_REACTION_KIND, ETF_CLASS_KIND, SINGLETON_KIND, GENE_KIND}
FIELDS = {kind: "native_p321" for kind in P321_KINDS}
FIELDS[GENE_KIND] = "native_metacyc_gene"
FRAMES = {
    ETF_REACTION_KIND: {"R265-RXN"},
    ETF_CLASS_KIND: {"ETF-Reduced", "ETF-Oxidized"},
    SINGLETON_KIND: {"CPLX-926"},
    GENE_KIND: {"G-545", "G-550"},
    "product": {"MONOMER-888", "MONOMER-893"},
}
PROTECTED = {"MetaCyc:" + frame: kind for kind in P321_KINDS for frame in FRAMES[kind]}
PROTECTED["MetaCyc:P321-PWY"] = "metacyc-pathway-xml"
GENES = {"G-545": ("badD", "MONOMER-888", "O07460"), "G-550": ("badH", "MONOMER-893", "O07457")}


def original_bytes(encoded: str) -> bytes:
    require(isinstance(encoded, str), "original bytes require base64 text")
    try:
        body = base64.b64decode(encoded, validate=True)
    except (ValueError, binascii.Error) as exc:
        raise ValueError("invalid original base64") from exc
    require(base64.b64encode(body).decode("ascii") == encoded, "noncanonical original base64")
    return body


def envelope(body: bytes, source: dict, tag: str, is_class: bool = False):
    frame = provenance(source, "META")
    require(source["version"] == "27.0", "unsupported complete native release")
    require(hashlib.sha256(body).hexdigest() == source["sha256"], "original hash mismatch")
    root = ET.fromstring(body, parser=ET.XMLParser(target=_TreeBuilder()))
    query = "META:" + frame
    legacy = f"http://{HOST}:443/"
    require(root.tag == "ptools-xml" and len(root) == 2, "requires one complete native object")
    require(
        root.attrib.keys() == {"ptools-version", "{http://www.w3.org/XML/1998/namespace}base"}
        and root.get("ptools-version") == source["version"]
        and root.get("{http://www.w3.org/XML/1998/namespace}base")
        in {source["url"], legacy + "getxml?" + query},
        "native envelope mismatch",
    )
    meta = one(root, "metadata")
    entity = next(n for n in root if n.tag != "metadata")
    for node in (root, meta, entity):
        blank(node)
    require(
        not meta.attrib
        and Counter(n.tag for n in meta)
        == Counter(["url", "service_name", "query", "num_results", "PGDB"]),
        "invalid complete metadata",
    )
    require(
        scalar(meta, "url") in {legacy, f"https://{HOST}/"}
        and scalar(meta, "service_name") == "getxml"
        and scalar(meta, "query") == query
        and scalar(meta, "num_results") == "1",
        "native request mismatch",
    )
    db = one(meta, "PGDB")
    blank(db)
    require(
        db.attrib == {"orgid": "META", "version": source["version"]}
        and [n.tag for n in db] == ["species"]
        and scalar(db, "species", True) == "MetaCyc",
        "native database mismatch",
    )
    attributes(entity, frame, "META", tag, is_class)
    return root, entity, frame


def publication(node: ET.Element, *, allow_url: bool = False) -> None:
    # Only the Gibbs citation extends the existing publication grammar with URL.
    if not allow_url:
        publication_context(node, "META")
        return
    require(len(node.findall("url")) == 1, "Gibbs publication requires one URL")
    scalar(node, "url", True)
    url = urlsplit(node.findtext("url", ""))
    require(url.scheme in {"http", "https"} and bool(url.netloc), "invalid publication URL")
    check = copy.deepcopy(node)
    check.remove(one(check, "url"))
    publication_context(check, "META")


def evidence(node: ET.Element, code: str, *, allow_url: bool = False) -> None:
    blank(node)
    require(
        not node.attrib and [n.tag for n in node] == ["Evidence-Code", "Publication"],
        "invalid complete evidence wrapper",
    )
    ev = node[0]
    attributes(ev, code, "META", "Evidence-Code", True)
    require(
        Counter(n.tag for n in ev)
        == Counter(
            {"comment": 1, "common-name": 1, **({"parent": 1} if code == "EV-EXP-IDA" else {})}
        ),
        "unsupported evidence code shape",
    )
    scalar(ev, "comment", True)
    direct_names(ev, code)
    if code == "EV-EXP-IDA":
        require(
            [v["id"] for v in refs(ev, "parent", "META", "Evidence-Code", is_class=True)]
            == ["MetaCyc:EV-EXP"],
            "wrong evidence parent",
        )
    publication(node[1], allow_url=allow_url)


def credits(node: ET.Element) -> None:
    """Validate complete credit identities and local references in source order."""
    blank(node)
    require(not node.attrib and len(node) > 0, "invalid credits wrapper")
    persons, organizations, seen = set(), set(), set()
    for event in node:
        blank(event)
        require(
            event.tag in {"created", "revised", "last-curated"}
            and not event.attrib
            and [n.tag for n in event] == ["date", "Person", "Organization"],
            "invalid credit event",
        )
        when = one(event, "date")
        require(
            when.attrib == {"datatype": "date"}
            and not len(when)
            and date.fromisoformat(when.text or "").isoformat() == when.text,
            "invalid credit date",
        )
        person = one(event, "Person")
        context_identity(person, "META", "Person")
        if "resource" in person.attrib:
            require(person.get("frameid") in persons, "unbound credit Person")
        else:
            require(
                person.get("detail") == "full"
                and set(n.tag for n in person)
                in [
                    {"affiliations", "comment", "common-name"},
                    {"email", "affiliations", "comment", "common-name"},
                ],
                "invalid complete Person",
            )
            for slot in {n.tag for n in person} - {"affiliations"}:
                scalar(person, slot, True)
            affiliation = one(person, "affiliations")
            blank(affiliation)
            require(not affiliation.attrib and len(affiliation) == 1, "invalid affiliation")
            organization = affiliation[0]
            context_identity(organization, "META", "Organization")
            require(
                organization.get("detail") == "full"
                and set(n.tag for n in organization)
                in [{"common-name"}, {"email", "abbrev-name", "url", "common-name"}],
                "invalid complete Organization",
            )
            for child in organization:
                scalar(organization, child.tag, True)
            organizations.add(organization.get("frameid"))
            persons.add(person.get("frameid"))
        org = ref_node(one(event, "Organization"), "META", "Organization", local=True)
        require(org["attributes"]["frameid"] in organizations, "unbound credit Organization")
        key = event.tag, when.text, person.get("frameid"), org["id"]
        require(key not in seen, "duplicate credit event")
        seen.add(key)


def reference_list(entity: ET.Element, slot: str, tag: str, *, is_class=False) -> list[dict]:
    wrapper = one(entity, slot)
    blank(wrapper)
    require(not wrapper.attrib and len(wrapper) > 0, "empty/attributed native list")
    result = [ref_node(n, "META", tag, is_class=is_class) for n in wrapper]
    require(len({v["id"] for v in result}) == len(result), "duplicate native list reference")
    return result


def activity_projection(
    entity: ET.Element, slot: str, activity_id: str, enzyme: str, reaction: str
) -> dict:
    wrapper = one(entity, slot)
    blank(wrapper)
    require(not wrapper.attrib and len(wrapper) == 1, "requires one complete activity")
    node = wrapper[0]
    activity(node, "META")
    require(
        node.get("frameid") == activity_id
        and node.get("detail") == "low"
        and Counter(n.tag for n in node) == Counter(["enzyme", "reaction", "common-name"]),
        "wrong activity identity or shape",
    )
    enz = ref_node(one(node, "enzyme")[0], "META", "Protein", local=True)
    rxn = ref_node(one(node, "reaction")[0], "META", "Reaction", local=True)
    require(
        (enz["id"], rxn["id"]) == ("MetaCyc:" + enzyme, "MetaCyc:" + reaction),
        "activity backlink mismatch",
    )
    label, synonyms = direct_names(node, activity_id)
    return {
        "id": "MetaCyc:" + activity_id,
        "enzyme": enz,
        "reaction": rxn,
        "label": label,
        "synonyms": synonyms,
    }


def species(entity: ET.Element) -> dict:
    from pathwaymech.biocyc_pathway import organism

    wrapper = one(entity, "species")
    blank(wrapper)
    require(not wrapper.attrib and len(wrapper) == 1, "invalid species context")
    organism(wrapper[0])
    require(wrapper[0].get("frameid") == "TAX-1076", "unexpected native species")
    return {"id": "MetaCyc:TAX-1076", "context": ET.tostring(wrapper[0], encoding="unicode")}


def project(entity: ET.Element, frame: str, kind: str) -> dict:
    require(frame in FRAMES[kind], "unsupported complete native profile")
    core = set()
    if kind == ETF_REACTION_KIND:
        slots = {
            "parent": 2,
            "gibbs-0": 1,
            "reaction-direction": 1,
            "orphan": 1,
            "physiologically-relevant": 1,
            "right": 2,
            "in-pathway": 1,
            "left": 3,
            "enzymatic-reaction": 1,
            "dblink": 3,
            "ec-number": 1,
        }
        require(Counter(n.tag for n in entity) == slots, "incomplete ETF reaction slots")
        core = {"parent", "reaction-direction", "left", "right", "in-pathway", "enzymatic-reaction"}
        ancillary(entity, set(slots) - core, core, "META")
        parents = refs(entity, "parent", "META", "Reaction", is_class=True)
        require(
            [v["id"] for v in parents]
            == ["MetaCyc:Chemical-Reactions", "MetaCyc:Small-Molecule-Reactions"],
            "wrong ETF reaction parents",
        )
        require(
            scalar(entity, "reaction-direction") == "REVERSIBLE"
            and scalar(entity, "orphan") == "NO"
            and one(entity, "physiologically-relevant").text == "true",
            "wrong reaction scope",
        )
        gibbs = one(entity, "gibbs-0")
        require(len(gibbs) == 1, "requires Gibbs evidence")
        evidence(gibbs[0], "EV-COMP", allow_url=True)
        ec = one(entity, "ec-number")
        require(ec.text == "EC-1.3.8.10" and len(ec) == 1 and ec[0].text == "T", "wrong EC context")
        sides = []
        wanted = {
            "left": ["CPD-533", "ETF-Oxidized", "PROTON"],
            "right": ["CYCLOHEXA-15-DIENE-1-CARBONYL-COA", "ETF-Reduced"],
        }
        for side in ("left", "right"):
            for ordinal, (wrapper, expected) in enumerate(
                zip(entity.findall(side), wanted[side], strict=True), 1
            ):
                blank(wrapper)
                require(
                    not wrapper.attrib
                    and len(wrapper) in {1, 2}
                    and (len(wrapper) == 1 or wrapper[1].tag == "coefficient"),
                    "invalid ETF side",
                )
                carrier = expected.startswith("ETF-")
                target = ref_node(
                    wrapper[0], "META", "Protein" if carrier else "Compound", is_class=carrier
                )
                require(target["id"] == "MetaCyc:" + expected, "wrong ETF reaction material")
                coefficient = integer(wrapper[1]) if len(wrapper) == 2 else 1
                require(coefficient == 1, "unsupported ETF coefficient")
                sides.append(
                    {
                        "side": side,
                        "ordinal": ordinal,
                        "entity": target,
                        "coefficient": coefficient,
                        "coefficient_explicit": len(wrapper) == 2,
                    }
                )
        memberships = reference_list(entity, "in-pathway", "Pathway")
        require(
            [v["id"] for v in memberships]
            == ["MetaCyc:PWY-7402", "MetaCyc:PWY-7401", "MetaCyc:P321-PWY"],
            "wrong ETF memberships",
        )
        act = activity_projection(entity, "enzymatic-reaction", "ENZRXN-22280", "CPLX-8778", frame)
        result = {
            "parent_classes": parents,
            "direction": "REVERSIBLE",
            "sides": sides,
            "memberships": memberships,
            "activity": act,
            "label": frame,
            "synonyms": [],
        }
    elif kind == ETF_CLASS_KIND:
        reduced = frame == "ETF-Reduced"
        state = "modified-form" if reduced else "unmodified-form"
        slots = {
            "parent": 2 if reduced else 3,
            "credits": 1,
            "comment": 1,
            "appears-in-left-side-of": 1,
            "appears-in-right-side-of": 1,
            "synonym": 3 if reduced else 2,
            state: 1,
            "dblink": 1 if reduced else 2,
            "common-name": 1,
        }
        require(Counter(n.tag for n in entity) == slots, "incomplete ETF class slots")
        core = {"parent", "common-name", "synonym", state}
        ancillary(entity, set(slots) - core, core, "META")
        credits(one(entity, "credits"))
        parents = refs(entity, "parent", "META", "Protein", is_class=True)
        require(
            [v["id"] for v in parents]
            == [
                "MetaCyc:Etf",
                *([] if reduced else ["MetaCyc:Modified-Proteins"]),
                "MetaCyc:" + ("Reduced" if reduced else "Oxidized") + "-Flavoproteins",
            ],
            "wrong ETF parents",
        )
        links = reference_list(entity, state, "Protein", is_class=True)
        require(
            [v["id"] for v in links]
            == (
                ["MetaCyc:ETF-Semiquinone", "MetaCyc:ETF-Oxidized"]
                if reduced
                else ["MetaCyc:ETF-Reduced"]
            ),
            "wrong ETF state links",
        )
        label, synonyms = direct_names(entity, frame)
        require(
            label
            == ("a reduced" if reduced else "an oxidized") + " electron-transfer flavoprotein",
            "wrong whole ETF name",
        )
        context = {
            side: reference_list(entity, "appears-in-" + side + "-side-of", "Reaction")
            for side in ("left", "right")
        }
        require(
            len(context["left"]) == (3 if reduced else 65)
            and len(context["right"]) == (65 if reduced else 3),
            "incomplete ETF reaction context",
        )
        result = {
            "parent_classes": parents,
            "state_links": {state: links},
            "reaction_context": context,
            "label": label,
            "synonyms": synonyms,
        }
    elif kind == SINGLETON_KIND:
        slots = {"parent": 1, "catalyzes": 1, "comment": 1, "species": 1, "component": 1}
        require(Counter(n.tag for n in entity) == slots, "incomplete singleton slots")
        core = {"parent", "component", "catalyzes", "species"}
        ancillary(entity, {"comment"}, core, "META")
        parents = refs(entity, "parent", "META", "Protein", is_class=True)
        require(
            [v["id"] for v in parents] == ["MetaCyc:Protein-Complexes"], "wrong singleton parent"
        )
        component = reference_list(entity, "component", "Protein")
        require(
            [v["id"] for v in component] == ["MetaCyc:MONOMER-943"], "wrong singleton component"
        )
        act = activity_projection(entity, "catalyzes", "ENZRXN-1144", frame, "R266-RXN")
        result = {
            "parent_classes": parents,
            "component": component[0],
            "coefficient": None,
            "coefficient_explicit": False,
            "activity": act,
            "species": species(entity),
            "label": act["label"],
            "synonyms": [],
        }
    elif kind == GENE_KIND:
        require(
            Counter(n.tag for n in entity) == Counter(["parent", "product", "common-name"]),
            "invalid gene slots",
        )
        core = {"parent", "product", "common-name"}
        parents = refs(entity, "parent", "META", "Gene", is_class=True)
        product = reference_list(entity, "product", "Protein")
        label, synonyms = direct_names(entity, frame)
        require(
            [v["id"] for v in parents] == ["MetaCyc:Genes"]
            and [v["id"] for v in product] == ["MetaCyc:" + GENES[frame][1]]
            and label == GENES[frame][0],
            "wrong native gene identity/product",
        )
        result = {
            "parent_classes": parents,
            "product": product[0],
            "label": label,
            "synonyms": synonyms,
        }
    else:
        gene = next(g for g, v in GENES.items() if v[1] == frame)
        bad_d = frame == "MONOMER-888"
        slots = {
            "parent": 1,
            "comment": 1,
            "citation": 1,
            "gene": 1,
            "component-of": 1,
            "species": 1,
            "dblink": 5 if bad_d else 9,
            "common-name": 1,
            "molecular-weight-seq": 1,
            **({"synonym": 1} if bad_d else {"molecular-weight-exp": 1}),
        }
        require(Counter(n.tag for n in entity) == slots, "incomplete gene product slots")
        core = {"parent", "gene", "common-name", "synonym", "species", "molecular-weight-seq"}
        ancillary(entity, set(slots) - core, core, "META")
        parents = refs(entity, "parent", "META", "Protein", is_class=True)
        genes = refs(entity, "gene", "META", "Gene", is_class=False)
        require(
            [v["id"] for v in parents] == ["MetaCyc:Polypeptides"]
            and [v["id"] for v in genes] == ["MetaCyc:" + gene],
            "wrong product reciprocal gene",
        )
        for wrapper in entity.findall("citation"):
            for pub in wrapper:
                publication(pub)
        weight = one(entity, "molecular-weight-seq")
        require(
            weight.attrib == {"datatype": "float", "units": "kD"}
            and not len(weight)
            and re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", weight.text or ""),
            "invalid sequence mass",
        )
        uniprot = [
            n.findtext("dblink-oid")
            for n in entity.findall("dblink")
            if n.findtext("dblink-db") == "UNIPROT"
        ]
        require(uniprot == [GENES[gene][2]], "wrong product UniProt crosslink")
        label, synonyms = direct_names(entity, frame)
        result = {
            "parent_classes": parents,
            "gene": genes[0],
            "species": species(entity),
            "uniprot": uniprot[0],
            "label": label,
            "synonyms": synonyms,
        }
    return {**result, **retained(entity, core)}


def document(body: bytes, source: dict, kind: str) -> dict:
    tag = "Gene" if kind == GENE_KIND else "Reaction" if kind == ETF_REACTION_KIND else "Protein"
    root, entity, frame = envelope(body, source, tag, kind == ETF_CLASS_KIND)
    return {
        "id": "MetaCyc:" + frame,
        "original_base64": base64.b64encode(body).decode("ascii"),
        "root_attributes": dict(root.attrib),
        "metadata_xml": ET.tostring(one(root, "metadata"), encoding="unicode"),
        "projection": project(entity, frame, kind),
    }


def p321_metadata(entry: dict, cache_dir: Path) -> dict:
    kind = entry.get("kind")
    require(kind in P321_KINDS, "unsupported P321 profile")
    keys(
        entry,
        PROVENANCE | {"key", "kind", "path"} | ({"product_source"} if kind == GENE_KIND else set()),
        "invalid P321 manifest fields",
    )
    require(isinstance(entry["key"], str) and entry["key"].strip(), "invalid source key")
    source = {k: entry[k] for k in PROVENANCE_ORDER}
    doc = document(original_path(entry, cache_dir).read_bytes(), source, kind)
    native = {"id": doc["id"], "document": doc}
    if kind == GENE_KIND:
        child = entry["product_source"]
        keys(child, PROVENANCE | {"path"}, "invalid gene product source")
        prov = {k: child[k] for k in PROVENANCE_ORDER}
        native["product_source"] = {
            **prov,
            "document": document(original_path(child, cache_dir).read_bytes(), prov, "product"),
        }
    result = {**source, "kind": kind, FIELDS[kind]: native}
    validate_p321_metadata(result)
    return result


def restore(doc: dict, source: dict, kind: str) -> None:
    keys(
        doc,
        {"id", "original_base64", "root_attributes", "metadata_xml", "projection"},
        "invalid complete P321 document",
    )
    require(
        json.dumps(doc, sort_keys=True)
        == json.dumps(
            document(original_bytes(doc["original_base64"]), source, kind), sort_keys=True
        ),
        "complete P321 projection mismatch",
    )


def validate_p321_metadata(metadata: dict) -> None:
    require(
        isinstance(metadata, dict) and metadata.get("kind") in P321_KINDS,
        "unsupported P321 metadata",
    )
    kind = metadata["kind"]
    keys(metadata, PROVENANCE | {"kind", FIELDS[kind]}, "invalid P321 metadata fields")
    native = metadata[FIELDS[kind]]
    keys(
        native,
        {"id", "document"} | ({"product_source"} if kind == GENE_KIND else set()),
        "invalid P321 native scope",
    )
    restore(native["document"], {k: metadata[k] for k in PROVENANCE_ORDER}, kind)
    require(native["id"] == native["document"]["id"], "P321 identity mismatch")
    if kind == GENE_KIND:
        child = native["product_source"]
        keys(child, PROVENANCE | {"document"}, "invalid retained gene product provenance")
        require(child["version"] == metadata["version"], "gene product release mismatch")
        restore(child["document"], {k: child[k] for k in PROVENANCE_ORDER}, "product")
        projection = native["document"]["projection"]
        require(
            projection["product"]["id"] == child["document"]["id"]
            and child["document"]["projection"]["gene"]["id"] == native["id"],
            "gene product pair mismatch",
        )


def p321_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_p321_metadata(metadata)
    kind = metadata["kind"]
    native = metadata[FIELDS[kind]]
    p = native["document"]["projection"]
    return native["id"], {
        "label": p["label"],
        "synonyms": sorted(p["synonyms"]),
        "source": source,
        "entity_type": {
            ETF_REACTION_KIND: "reaction",
            ETF_CLASS_KIND: "protein_class",
            SINGLETON_KIND: "protein_complex",
            GENE_KIND: "native_gene",
        }[kind],
        "label_kind": "source_context" if kind == ETF_REACTION_KIND else "canonical",
    }


def validate_p321_assertions(
    sources: dict, claims: list[tuple[str, str]], *, allow_legacy_products: bool = False
) -> None:
    """Check complete product origins without changing legacy serialization.

    The builder supplies actual manifest kinds in its temporary inventories.
    The consumer opts into the existing four-field ordinary metadata shape;
    only an exact companion URL, release and raw hash can authorize that shape.
    """
    assertions, carriers, products = {}, {}, {}
    observations = list(claims)
    for key, metadata in sources.items():
        kind = metadata.get("kind")
        if kind in P321_KINDS:
            validate_p321_metadata(metadata)
            native = metadata[FIELDS[kind]]
            ident = native["id"]
            signature = kind, json.dumps(native, sort_keys=True), metadata["version"]
            require(
                ident not in assertions or assertions[ident] == signature,
                "conflicting complete P321 owner",
            )
            assertions[ident] = signature
            if kind == ETF_CLASS_KIND:
                carriers[ident] = native["document"]["projection"]
            if kind == GENE_KIND:
                child = native["product_source"]
                child_id = child["document"]["id"]
                origin = tuple(child[k] for k in ("url", "version", "sha256"))
                require(
                    child_id not in products or products[child_id] == origin,
                    "conflicting gene product original",
                )
                products[child_id] = origin
        url = urlsplit(metadata.get("url", ""))
        if url.hostname in {HOST, "biocyc.org", "www.biocyc.org", "metacyc.org", "www.metacyc.org"}:
            query = parse_qs(url.query)
            values = query.get("id", []) + ([url.query] if url.query.startswith("META:") else [])
            for value in values:
                if value.startswith("META:"):
                    observations.append(("MetaCyc:" + value[5:], key))
                elif query.get("orgid") == ["META"]:
                    observations.append(("MetaCyc:" + value, key))
            if url.path.startswith("/META/"):
                observations.extend(("MetaCyc:" + v, key) for v in query.get("object", []))
        for field, value in metadata.items():
            if (
                field.startswith("native_")
                and isinstance(value, dict)
                and isinstance(value.get("id"), str)
            ):
                observations.append((value["id"], key))
    if len(carriers) == 2:
        reduced, oxidized = [carriers["MetaCyc:ETF-" + state] for state in ("Reduced", "Oxidized")]
        require(
            reduced["reaction_context"]["left"] == oxidized["reaction_context"]["right"]
            and reduced["reaction_context"]["right"] == oxidized["reaction_context"]["left"],
            "ETF pair reaction context mismatch",
        )
    for ident, key in observations:
        metadata = sources[key]
        if ident in PROTECTED:
            require(
                metadata.get("kind") == PROTECTED[ident],
                "P321 identity requires complete typed scope: " + ident,
            )
        if ident in products:
            require(
                (
                    metadata.get("kind") == "metacyc-protein-xml"
                    or (allow_legacy_products and set(metadata) == PROVENANCE)
                )
                and tuple(metadata.get(k) for k in ("url", "version", "sha256")) == products[ident],
                "gene product owner differs from complete original",
            )
