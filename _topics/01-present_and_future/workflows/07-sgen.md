---
marp: true
---

# Serializer Generator Tool

Tool for automatically generating JSON / YAML serialization classes and constructor operators from schema files.

---

## Features

- data definition language
- automatic serialization to JSON / YAML
- allow building data objects directly in the workflow
- support for class hierarchy and custom namespaces
- interop with JSON schema tools, e.g. pydantic

---

## Questions

- allow cross-referencing existing types:
  - composition of multiple namespace-scoped schemas
  - reuse of existing types in a schema
- export to other serialization formats:
  - interop with Python scripting package
- should generated classes be extended with processing features?
- other ideas / suggestions / feedback?