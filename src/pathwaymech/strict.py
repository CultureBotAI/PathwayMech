"""Closed-schema validation of pathway records against the LinkML schema.

`linkml-validate`'s default open mode lets an undeclared key pass, and so does
the hand-written validator in `pathwaymech.schema`. This validates in closed
mode, the way the other Mechs' strict gates do, so a misspelt or invented key
is an error.

The JSON Schema is generated with `include_null=False`. LinkML reads a null
optional slot as "not provided", but its default JSON Schema types every
optional slot as nullable, so `title: null` satisfied the rule that a
reference needs a title or a citation (#193). Here an explicit null is an
error: omit the key instead.

The cross-record rules LinkML cannot state -- endpoints resolve locally,
evidence cites a declared reference, ids are unique -- stay in
`pathwaymech.schema`.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import yaml

SCHEMA_PATH = Path(__file__).resolve().parent / "schema" / "pathwaymech.yaml"
TARGET_CLASS = "PathwayRecord"

# Holds the generated JSON Schema for the life of the process.
_GENERATED: tempfile.TemporaryDirectory | None = None


def json_schema() -> str:
    """The closed, null-free JSON Schema the gate validates against."""
    from linkml.generators.jsonschemagen import JsonSchemaGenerator

    return JsonSchemaGenerator(
        str(SCHEMA_PATH), top_class=TARGET_CLASS, include_null=False, not_closed=False
    ).serialize()


def validator():
    # Imported here: linkml is heavy, and only this gate needs it.
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    global _GENERATED
    if _GENERATED is None:
        _GENERATED = tempfile.TemporaryDirectory(prefix="pathwaymech-schema-")
    path = Path(_GENERATED.name) / "pathwaymech.schema.json"
    path.write_text(json_schema(), encoding="utf-8")
    return Validator(
        schema=str(SCHEMA_PATH),
        validation_plugins=[JsonschemaValidationPlugin(closed=True, json_schema_path=path)],
    )


def _shown(path: Path, root: Path) -> str:
    # A draft saved outside the repository is still worth checking (#192).
    return path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path)


def strict_errors(paths: list[Path], root: Path) -> list[str]:
    """One line per error, `path: message`, for every record in `paths`."""
    checker = validator()
    errors: list[str] = []
    for path in paths:
        shown = _shown(path, root)
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f"{shown}: unreadable: {error}")
            continue
        for result in checker.validate(record, TARGET_CLASS).results:
            errors.append(f"{shown}: {result.message}")
    return errors
