---
marp: true
---

# Bonsai - GUI

A collection of packages for quickly composing user interfaces and real-time data visualization.

---

## Features

- common user interface controls, including buttons, sliders, combo boxes, text boxes, etc.
- container controls, such as group boxes, tab controls, or table layout panels
- hierarchically overlay the controls using `VisualizerMapping`
- a framework for assembling complex real-time reactive plots using bar graphs, line graphs or rolling graphs
- combine multiple independent graph visualizers asynchronously using graph panels

---

## Questions

- tweaks to existing controls:
  - nicer visual layout
  - easier to combine
- exposing existing control events:
  - click, key pressed, resize, etc
- how to allow dynamic creation?
  - create on subscription
- other ideas / feedback?