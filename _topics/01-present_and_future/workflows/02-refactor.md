---
marp: true
---

# Code refactoring

Functionality for consistently replacing, renaming, and finding operators.

---

## Features

* go to definition
* replace:
  * operator nodes
  * group operator types (inner workflow will be preserved)
  * subject types
* rename subjects:
  * scoping rules apply
  * subjects inside include workflows are not renamed since include is read-only
* find function:
  * subjects (subscribe and multicast)
  * operator types (e.g. find all camera nodes)

---

## Questions

* improve find function:
  * "find all" support
  * additional find options (e.g. search by property value, search by subject type)
  * highlight search results in explorer
* improve rename subject for include workflows:
  * allow renaming if subject name is externalized
* improve find/replace of property values:
  * allow replacing all property values matching specific conditions
* other ideas / suggestions?