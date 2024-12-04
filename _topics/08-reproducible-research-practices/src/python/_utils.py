import inspect
import json
from enum import Enum
from typing import Any, Optional, Type, List
from os import PathLike
from subprocess import run, CompletedProcess

from pydantic import BaseModel, PydanticInvalidForJsonSchema
from pydantic.json_schema import (
    GenerateJsonSchema,
    JsonSchemaMode,
    JsonSchemaValue,
    _deduplicate_schemas,
    models_json_schema,
)
from pydantic_core import PydanticOmit, core_schema, to_jsonable_python


class CustomGenerateJsonSchema(GenerateJsonSchema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nullable_as_oneof = kwargs.get("nullable_as_oneof", True)
        self.unions_as_oneof = kwargs.get("unions_as_oneof", True)
        self.render_x_enum_names = kwargs.get("render_x_enum_names", True)

    def nullable_schema(self, schema: core_schema.NullableSchema) -> JsonSchemaValue:
        null_schema = {"type": "null"}
        inner_json_schema = self.generate_inner(schema["schema"])

        if inner_json_schema == null_schema:
            return null_schema
        else:
            if self.nullable_as_oneof:
                return self.get_flattened_oneof([inner_json_schema, null_schema])
            else:
                return super().get_flattened_anyof([inner_json_schema, null_schema])

    def get_flattened_oneof(self, schemas: list[JsonSchemaValue]) -> JsonSchemaValue:
        members = []
        for schema in schemas:
            if len(schema) == 1 and "oneOf" in schema:
                members.extend(schema["oneOf"])
            else:
                members.append(schema)
        members = _deduplicate_schemas(members)
        if len(members) == 1:
            return members[0]
        return {"oneOf": members}

    def enum_schema(self, schema: core_schema.EnumSchema) -> JsonSchemaValue:
        """Generates a JSON schema that matches an Enum value.

        Args:
            schema: The core schema.

        Returns:
            The generated JSON schema.
        """
        enum_type = schema["cls"]
        description = (
            None if not enum_type.__doc__ else inspect.cleandoc(enum_type.__doc__)
        )
        if (
            description == "An enumeration."
        ):  # This is the default value provided by enum.EnumMeta.__new__; don't use it
            description = None
        result: dict[str, Any] = {
            "title": enum_type.__name__,
            "description": description,
        }
        result = {k: v for k, v in result.items() if v is not None}

        expected = [to_jsonable_python(v.value) for v in schema["members"]]

        result["enum"] = expected
        if len(expected) == 1:
            result["const"] = expected[0]

        types = {type(e) for e in expected}
        if isinstance(enum_type, str) or types == {str}:
            result["type"] = "string"
        elif isinstance(enum_type, int) or types == {int}:
            result["type"] = "integer"
        elif isinstance(enum_type, float) or types == {float}:
            result["type"] = "numeric"
        elif types == {bool}:
            result["type"] = "boolean"
        elif types == {list}:
            result["type"] = "array"

        _type = result.get("type", None)
        if (self.render_x_enum_names) and (_type != "string"):
            result["x-enumNames"] = [
                screaming_snake_case_to_pascal_case(v.name) for v in schema["members"]
            ]

        return result

    def literal_schema(self, schema: core_schema.LiteralSchema) -> JsonSchemaValue:
        """Generates a JSON schema that matches a literal value.

        Args:
            schema: The core schema.

        Returns:
            The generated JSON schema.
        """
        expected = [v.value if isinstance(v, Enum) else v for v in schema["expected"]]
        # jsonify the expected values
        expected = [to_jsonable_python(v) for v in expected]

        types = {type(e) for e in expected}

        if len(expected) == 1:
            if isinstance(expected[0], str):
                return {"const": expected[0], "type": "string"}
            elif isinstance(expected[0], int):
                return {"const": expected[0], "type": "integer"}
            elif isinstance(expected[0], float):
                return {"const": expected[0], "type": "number"}
            elif isinstance(expected[0], bool):
                return {"const": expected[0], "type": "boolean"}
            elif isinstance(expected[0], list):
                return {"const": expected[0], "type": "array"}
            elif expected[0] is None:
                return {"const": expected[0], "type": "null"}
            else:
                return {"const": expected[0]}

        if types == {str}:
            return {"enum": expected, "type": "string"}
        elif types == {int}:
            return {"enum": expected, "type": "integer"}
        elif types == {float}:
            return {"enum": expected, "type": "number"}
        elif types == {bool}:
            return {"enum": expected, "type": "boolean"}
        elif types == {list}:
            return {"enum": expected, "type": "array"}
        # there is not None case because if it's mixed it hits the final `else`
        # if it's a single Literal[None] then it becomes a `const` schema above
        else:
            return {"enum": expected}

    def union_schema(self, schema: core_schema.UnionSchema) -> JsonSchemaValue:
        """Generates a JSON schema that matches a schema that allows values matching any of the given schemas.

        Args:
            schema: The core schema.

        Returns:
            The generated JSON schema.
        """
        generated: list[JsonSchemaValue] = []

        choices = schema["choices"]
        for choice in choices:
            # choice will be a tuple if an explicit label was provided
            choice_schema = choice[0] if isinstance(choice, tuple) else choice
            try:
                generated.append(self.generate_inner(choice_schema))
            except PydanticOmit:
                continue
            except PydanticInvalidForJsonSchema as exc:
                self.emit_warning("skipped-choice", exc.message)
        if len(generated) == 1:
            return generated[0]
        if self.unions_as_oneof is True:
            return self.get_flattened_oneof(generated)
        else:
            return self.get_flattened_anyof(generated)


def export_schema(
    model: BaseModel,
    schema_generator: Type[GenerateJsonSchema] = CustomGenerateJsonSchema,
    mode: JsonSchemaMode = "serialization",
    def_keyword: str = "definitions",
    models_title: Optional[str] = None,
):
    """Export the schema of a model to a json file"""
    if not isinstance(model, list):
        _model = model.model_json_schema(schema_generator=schema_generator, mode=mode)
    else:
        models = [(m, mode) for m in model]
        _, _model = models_json_schema(
            models, schema_generator=schema_generator, title=models_title
        )
    json_model = json.dumps(_model, indent=2)
    json_model = json_model.replace("$defs", def_keyword)
    return json_model


def screaming_snake_case_to_pascal_case(value: str) -> str:
    words = value.split("_")
    return "".join(word.capitalize() for word in words)


class BonsaiSgenSerializers(Enum):
    NONE = "None"
    JSON = "NewtonsoftJson"
    YAML = "YamlDotNet"


def bonsai_sgen(
    schema_path: PathLike,
    output_path: PathLike,
    namespace: str = "DataSchema",
    root_element: Optional[str] = None,
    serializer: Optional[List[BonsaiSgenSerializers]] = None,
    executable: PathLike | str = "dotnet tool run bonsai.sgen",
) -> CompletedProcess:
    """Runs Bonsai.SGen to generate a Bonsai-compatible schema from a json-schema model
    For more information run `bonsai.sgen --help` in the command line.

    Returns:
        CompletedProcess: The result of running the command.
    Args:
        schema_path (PathLike): Target Json Schema file
        output_path (PathLike): Specifies the name of the
          file containing the generated code.
        namespace (Optional[str], optional): Specifies the
          namespace to use for all generated serialization
          classes. Defaults to DataSchema.
        root_element (Optional[str], optional):  Specifies the
          name of the class used to represent the schema root element.
          If None, it will use the json schema root element. Defaults to None.
        serializer (Optional[List[BonsaiSgenSerializers]], optional):
          Specifies the serializer data annotations to include in the generated classes.
          Defaults to None.
    """

    if serializer is None:
        serializer = [BonsaiSgenSerializers.JSON]

    cmd_string = f'{executable} --schema "{schema_path}" --output "{output_path}"'
    cmd_string += "" if namespace is None else f" --namespace {namespace}"
    cmd_string += "" if root_element is None else f" --root {root_element}"

    if len(serializer) == 0 or BonsaiSgenSerializers.NONE in serializer:
        cmd_string += " --serializer none"
    else:
        cmd_string += " --serializer"
        cmd_string += " ".join([f" {sr.value}" for sr in serializer])
    return run(cmd_string, shell=True, check=True)


def pascal_to_snake_case(value: str) -> str:
    result = ""
    for i, char in enumerate(value):
        if char.isupper():
            if i != 0:
                result += "_"
            result += char.lower()
        else:
            result += char
    return result
