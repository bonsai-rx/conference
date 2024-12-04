---
marp: true
---

# Package Manager

The default package feed for Bonsai on MyGet is nearing obsolescence and also misses important NuGet features. We modernized the package manager to finalize the move of all packages to the [NuGet Gallery](https://www.nuget.org/).

---

## Features (1)

- updated styling and functionality:
  - deprecation warnings
  - latest version strings for all packages
  - inline package title, package authors, and total package download counts
  - package prefix reservation icons
  - operator icons consistent with VS NuGet client

---

## Features (2)

- default filtering for gallery and library packages:
  - avoid seeing everything on NuGet
  - checkbox enables search for all dependency package types if necessary
  - requires updating all package metadata
- dedicated dialog for viewing embedded license files:
  - modern package servers will serve embedded license files and provide the URL
  - recommendation now will be to embed icon, license and README in the package directly

---

## Questions

- improve terminology of "Show dependencies":
  - official package type terminology is "dependency" but open to consider alternatives
- there is an issue specific to Visual Studio installing packages with multiple package types:
  - there is agreement this will be solved, question is how long
- update template to include new package type:
  - facilitate transition
- other suggestions / feedback?