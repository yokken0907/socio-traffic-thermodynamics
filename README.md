# Socio-Traffic Thermodynamics (STT)

**Claim-bounded reduced-surrogate archive for stop-and-go traffic waves, synchronization risk, and risk-budgeted information release in finite-capacity toy traffic networks.**

Project website: https://yokken0907.github.io/socio-traffic-thermodynamics/  
Repository: https://github.com/yokken0907/socio-traffic-thermodynamics

## Current public package

**Repository package version:** `v0.3.2-public-landing-and-metadata-refresh`  
**Scientific manuscript baseline:** `v0.3.1-integrated-revision-source-license-checked`  
**Purpose of this refresh:** public landing-page cleanup, metadata refresh, GitHub Pages readiness, search/discovery support, and stronger claim-boundary placement.

This v0.3.2 package does **not** change the scientific claims of the v0.3.1 integrated manuscript. It reorganizes the public repository so that first-time readers, search engines, and GitHub users can find the current materials without navigating the previous nested repository structure.

## Read first

1. Project website / visual orientation: `https://yokken0907.github.io/socio-traffic-thermodynamics/`
2. Main integrated manuscript PDF: `paper/integrated_v0_3_1/STT_integrated_model_risk_budget_synthesis_v0_3_1.pdf`
3. Claim boundary: `CLAIM_BOUNDARY.md`
4. Reader guidance: `docs/STT_v031_reader_guidance.md`
5. Release note: `docs/release/RELEASE_DATA_v0_3_2.md`

## What this project is

STT is a claim-bounded toy-model and reduced-surrogate research package. It combines:

- a reduced stochastic ring-road surrogate that reproduces endogenous stop-and-go wave formation;
- finite-capacity toy-network audit outputs for synchronization risk under shared information;
- risk-budgeted information-release diagnostics in the tested frozen holdout setting;
- an integrated v0.3.1 manuscript and evidence package.

The intended use is **conceptual and diagnostic**: to document a bounded hypothesis-generating mechanism involving finite capacity, synchronization, overload risk, and information release in toy traffic networks.

## What this project is not

This repository does **not** claim:

- calibrated real-world traffic prediction;
- validated traffic policy;
- city-scale transportation planning guidance;
- deployment-ready route-guidance software;
- traffic-signal or route-control certification;
- a universal congestion solution;
- proof that information should generally be withheld from real drivers;
- a recommendation to restrict real-world public traffic information.

The information-release result is limited to tested finite-capacity toy networks and should be read as a synchronization-risk diagnostic, not as a real-world information-control policy.

## Repository contents

- `paper/integrated_v0_3_1/` — integrated v0.3.1 manuscript PDF, TeX source, and paper figures.
- `scripts/` — original and reproducible reduced ring-road surrogate scripts.
- `results/` — preserved output figures.
- `figures/` — selected figures used for orientation and manuscript support.
- `evidence/v030_synthesis_outputs/` — locked synthesis outputs, tables, figures, phase ledger, and claim lock.
- `docs/project_visual_orientation/` — GitHub Pages visual orientation.
- `docs/` — claim-boundary, release, Jxiv metadata, license notes, robots.txt, and sitemap.xml.
- `FILE_MANIFEST.csv/json` — regenerated SHA-256 manifest for this package.
- `tools/verify_manifest.py` — manifest verification utility.

## Reproduction of the ring-road surrogate

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/stt_ring_reproducible.py --seed 20260416 --out results/stt_result_seed20260416.png
```

The original uploaded script did not fix a random seed. Therefore, exact pixel-level reproduction of the uploaded figure is not claimed. The repository preserves the original uploaded figure and provides a deterministic representative rerun script.

## GitHub Pages setup

Recommended Pages configuration:

```text
Settings → Pages → Build and deployment
Source: Deploy from a branch
Branch: main
Folder: /docs
```

After deployment, use this Website URL in the repository About field:

```text
https://yokken0907.github.io/socio-traffic-thermodynamics/
```

Recommended Topics:

```text
traffic-flow traffic-congestion traffic-simulation stop-and-go-waves
optimal-velocity-model non-equilibrium information-design routing-games
synchronization-risk risk-budget toy-model transportation science-education
claim-boundary
```

Recommended Description:

```text
Claim-bounded reduced-surrogate archive for Socio-Traffic Thermodynamics: stop-and-go waves, synchronization risk, and risk-budgeted information release in toy traffic networks. No policy or deployment claim.
```

## License

This repository uses the source-defined **Evaluation-Only Public License Notice** provided in `LICENSE` and `LICENSE_EVALUATION_ONLY.txt`.

For Zenodo, use an "other/source-defined/license in repository" style license option rather than selecting CC-BY-NC-4.0. This package includes `.zenodo.json` with `license: other-open` and does not specify a DOI.

## AI assistance disclosure

AI assistance was used for drafting, restructuring, repository packaging, and claim-boundary wording support. The author remains responsible for public release decisions, claim boundaries, and content review. See `AI_ASSISTANCE_DISCLOSURE.md`.

## Contact and support

Author: Keiji Yoshimura, Independent Researcher  
Contact: yokken0907@gmail.com  
Optional support information: `SUPPORT.md`
