# Release data - v0.3.2-public-landing-and-metadata-refresh

## Release title

Socio-Traffic Thermodynamics v0.3.2: Public Landing and Metadata Refresh

## Release tag

`v0.3.2-public-landing-and-metadata-refresh`

## Release summary

This release is a non-theory-expansion public repository refresh for Socio-Traffic Thermodynamics (STT). It preserves the v0.3.1 integrated manuscript and evidence package as the scientific content baseline, while reorganizing the repository for public discoverability, GitHub Pages deployment, manifest consistency, and stronger claim-boundary visibility.

## Main changes

- Promotes the previous nested v0.3.1 integrated repository to the repository root.
- Removes the confusing old v0.3.0 / nested-v0.3.1 public structure from the distributed package.
- Adds GitHub Pages-ready files under `docs/`:
  - `docs/index.html`
  - `docs/project_visual_orientation/index.html`
  - `docs/style.css`
  - `docs/robots.txt`
  - `docs/sitemap.xml`
- Strengthens public claim-boundary wording, especially around information-release interpretation.
- Adds `.github/FUNDING.yml` and `.zenodo.json` with source-defined `other-open` licensing metadata and no fixed DOI.
- Updates `README.md`, `README_ja.md`, `CITATION.cff`, and support/disclosure notes.
- Regenerates `FILE_MANIFEST.csv` and `FILE_MANIFEST.json` for this package.
- Adds a manifest verification utility under `tools/verify_manifest.py`.

## Scientific-content boundary

This release does not modify the v0.3.1 integrated manuscript PDF or expand its claim scope. The scientific baseline remains:

`paper/integrated_v0_3_1/STT_integrated_model_risk_budget_synthesis_v0_3_1.pdf`

## Claim boundary

This repository does not claim:

- real-world traffic prediction;
- validated traffic policy;
- route-guidance deployment readiness;
- public traffic-information control guidance;
- a universal congestion solution;
- proof that real-world traffic information should be withheld.

The information-release result is limited to tested finite-capacity toy-network diagnostics.

## Recommended GitHub About settings

Description:

```text
Claim-bounded reduced-surrogate archive for Socio-Traffic Thermodynamics: stop-and-go waves, synchronization risk, and risk-budgeted information release in toy traffic networks. No policy or deployment claim.
```

Website:

```text
https://yokken0907.github.io/socio-traffic-thermodynamics/
```

Topics:

```text
traffic-flow traffic-congestion traffic-simulation stop-and-go-waves optimal-velocity-model non-equilibrium information-design routing-games synchronization-risk risk-budget toy-model transportation science-education claim-boundary
```

## Zenodo note

Use source-defined / other-open / license-in-repository style metadata. Do not manually enter an existing DOI as the DOI for this release; allow Zenodo to generate archive identifiers from GitHub releases.
