# Socio-Traffic Thermodynamics v0.1.1-zenodo-safe-public-gate

This is the initial Zenodo-safe public-gate release package for the Socio-Traffic Thermodynamics (STT) manuscript and stochastic ring-road numerical validation materials.

## Scope

This release provides a reproducibility-oriented public archive for a theoretical and numerical STT study of traffic congestion as a nonequilibrium dissipative structure driven by social potential, finite network capacity, finite perceptual bandwidth, and decentralized residual control variance.

The numerical material centers on a stochastic Optimal Velocity ring-road simulation demonstrating stop-and-go wave formation without a fixed bottleneck.

## Included materials

- Manuscript PDF
- Original uploaded STT ring-road simulation script
- Cleaned reproducible simulation script with seed control
- Original uploaded simulation result image
- README and Japanese README
- Evaluation-only license
- Claim-boundary and AI-assistance disclosure documents
- Project consistency audit
- File manifest with SHA-256 hashes
- Zenodo-safe draft citation metadata under `docs/citation_metadata/`

## Excluded materials

The original uploaded ZIP contained a full Python virtual environment (`stt_env/`) with thousands of third-party dependency files. This environment is intentionally excluded. Dependencies are represented by `requirements.txt`.

## Claim boundary

This release supports a limited surrogate-level claim about spontaneous stop-and-go wave formation in a stochastic OV ring-road model. It does not claim real-network calibration, traffic-policy validation, universal decongestion, or safety-critical deployment readiness.

## Zenodo-safe citation handling

The active root `CITATION.cff` file has been intentionally omitted from this pre-DOI release to avoid metadata-validation conflicts during Zenodo archival.

Draft citation metadata is preserved at:

`docs/citation_metadata/CITATION_DRAFT_pre_doi.cff`

## Suggested tag

`v0.1.1-zenodo-safe-public-gate`
