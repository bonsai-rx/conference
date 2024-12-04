---
marp: true
---

# Workflow Explorer

## Features

- Explorer treeview
- Allow navigating to any level without opening previous levels
- Allow visualizers to run uncoupled from the workflow view
- Highlight build errors in explorer treeview

---

## Questions

- allowing opening of independent tabs and windows should be allowed:
  - should we allow opening multiple views to the same level?
- generalize tabs and floating windows into a single dock panel:
  - how to handle multiple windows pointing to the same path
  - what to do when deleting group nodes causes invalidation of multiple open tabs
  - keep track of dock panel layout in settings file
  - keep track of dock panel layout across undo / redo
- other ideas / feedback?
