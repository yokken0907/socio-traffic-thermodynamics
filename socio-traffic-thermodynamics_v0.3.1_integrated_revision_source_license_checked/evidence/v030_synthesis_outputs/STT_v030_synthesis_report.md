# STT v0.3.0 Synthesis Lock Report

## Status

`PASS-STT-V030-SYNTHESIS-LOCKED`

This report synthesizes STT v0.2.x toy-model audits found under `/home/kei/stt`.

Phase outputs found: 10/10  
PASS-like phase statuses: 10/10

## Frozen holdout result used for final lock

v0.2.9 status: `PASS-STT-V029-RUN-COMPLETE`  
Raw rows: 1134  
Holdout scenario count: 27  
Seed count: 3  
Policy count: 14

### Best frozen holdout policy

Best mean-cost policy: `budget_common_u0.055_s0.00`  
Family: `budget_common`  
Mean cost: 1.734372  
No-information mean cost: 1.758804  
Improvement vs no-information: 0.024432  
Overload severity: 0.022745  
Delta overload severity vs no-information: -0.004088  
Sync index: 0.002837

### Common-precision and delayed-common stress comparison

Common precise mean cost: 3.568163  
Common precise overload severity: 0.217678  
Common precise sync index: 0.924393

Delayed common mean cost: 6.715559  
Delayed common overload severity: 0.438071  
Delayed common sync index: 0.939120

## Zero-budget holdout finding

At severity budget epsilon = 0, the candidate families that won across holdout conditions were:

- `budget_common`: 20 wins
- `coarse_zone`: 7 wins

Total zero-budget wins: 27

Strict per-condition check: 27/27 best candidates improved mean cost while not increasing overload severity relative to the no-information baseline.

## Locked claim

Finite-capacity toy networks showed a recurring mechanism: high-sensitivity, high-frequency, synchronous response to shared information can amplify overload, oscillation, and social cost. Conversely, low-rate, coarse, staggered, guarded, or otherwise risk-budgeted information release can improve mean cost while keeping overload severity within or below a conservative no-information baseline in the tested frozen holdout design.

## Correct interpretation

The result is not "information should be withheld." The result is that traffic information release should be treated as a risk-budgeted synchronization-control problem rather than a simple precision-maximization problem.

The strongest tested policy family was low-rate common information release. Coarse-zone guidance also appeared as a zero-budget winner under some topology and pulse-mode combinations.

## Claim boundary

This is a toy-model synthesis only. It does not establish city-scale traffic prediction, policy effectiveness, real-world deployment readiness, or a universal traffic-control prescription.

## Recommended manuscript framing

Use phrasing such as:

- claim-bounded toy-model diagnostics
- finite-capacity network synchronization risk
- risk-budgeted information release
- frozen-policy holdout audit
- hypothesis-generating framework

Avoid phrasing such as:

- solved traffic congestion
- validated traffic policy
- proven urban traffic control method
- real-world deployment-ready route guidance
- universal law of social traffic
