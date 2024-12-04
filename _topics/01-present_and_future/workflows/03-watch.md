---
marp: true
---

# Workflow state watch

The new "watch" features aims to make it easier to understand the runtime state of each operator in the workflow for learning and debugging.

---

## Watch infrastructure

There are five main stages in the life of a subscription to an observable sequence:

- `Subscribe`: the observable receives a subscription from a downstream operator
- `OnNext`: the observable emits a new value notification
- `OnCompleted`: the observable terminates successfully
- `OnError`: the observable terminates exceptionally
- `Unsubscribe`: the subscription is disposed, either following termination or cancellation

---

## Watch infrastructure (2)

There can be multiple parallel subscriptions to a single operator, so these stages can potentially run in parallel for each independent subscription.

We adopted a strategy for combining or aggregating the state of each sequence into a single value using the following rules:

---

| Status | Annotation | Description |
| ------ | ---------- | ----------- |
| Ready | ![ready](https://github.com/user-attachments/assets/721901be-b260-40a2-b049-accbb0b31622) | no subscriptions have been made yet |
| Active | ![active](https://github.com/user-attachments/assets/c6720204-75e9-4e34-919f-e0df33b70d05) | at least one active subscription but no values have been emitted yet |
| Notifying | ![notifying](https://github.com/user-attachments/assets/8bb003f6-59dd-4aea-bae2-41eb6fde6bc5) | at least one active subscription and emitted at least one value (spins whenever a new value is emitted) |
| Completed | ![completed](https://github.com/user-attachments/assets/16420eda-d8ab-4e32-b6d9-b5f3971c211d) | no active subscriptions and at least one subscription terminated successfully |
| Error | ![error](https://github.com/user-attachments/assets/2ac3a3f5-e068-4891-86f6-84940ebaf884) | no active subscriptions and at least one subscription terminated exceptionally |
| Canceled | ![canceled](https://github.com/user-attachments/assets/7245e852-750a-4a44-a4f1-0f5deb7fb161) | no active subscriptions and at least one subscription was canceled without termination |

---

The `Error` status has precedence over `Completed`, and both have precedence over `Canceled`. Each of the status values is mapped into a visual annotation which is updated and overlaid periodically on top of each operator. The `Notifying` status will actively spin as long as values continue to be emitted.

---

## Watch Example

![watch-example](https://github.com/user-attachments/assets/eac1ee62-8c6b-4325-a816-6075d647e8c7)

---

## Caveats and limitations

- Since the live watch refreshes at a maximum rate of 10 Hz this feature should not be relied upon for debugging race conditions, high-frequency streams, or any other aspects of the workflow behavior depending on precise timing.
- When overlaying multiple subscriptions to the same node, some of the indicators may be misleading, as there is no way of visually overlaying the state of individual subscriptions and there are precedence rules for the visual annotations.
- This feature should not be relied upon if knowing how many subscriptions are running over each operator is important.

---

## Questions

- introduce a complementary "trace" feature:
  - log all changes in subscription state, for all subscriptions
  - include timestamp and operator source
  - pause / stop logging to allow consulting the file
- allow selective "watch" / "trace":
  - display / log state of only specific operators
- other ideas / suggestions / feedback?