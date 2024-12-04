---
marp: true
---

# Annotations

Code comments are an essential part of any programming language, and Bonsai is no exception.

---

## Features

* markdown support using [Markdig](https://github.com/xoofx/markdig)
* rich HTML support leveraged by the new built-in browser panel
* `Annotation` operator:
  * can be attached to any node or placed by itself
  * if placed by itself it works as a separator and breaks the current flow

---

## Questions (1)

* how to handle documentation of group / included workflows?
  * render all embedded annotations as docs if no custom docs found (i.e. when clicking `View Help`)
  * add syntax to mark specific annotations as top-level docs (similar to XML code comments)
* expand default styling for HTML / markdown annotations:
  * mermaid support
  * workflow support
  * code / tables / etc improved styling and copy features?
  * custom CSS (no Javascript for now)

---

## Questions (2)

* how to improve asset links?
  * currently local file links
* leverage annotations to help creation of examples
  * create `docfx` processor that interleaves markdown annotations with workflow copy blocks
  * should annotations be included with the copied workflows in this case?
* other patterns / applications / ideas?