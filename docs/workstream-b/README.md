# Workstream B — Candidate C: AdS / Fluid-Gravity Adaptation

Version: v0.2  
Claim grade: C0 candidate-development lane; no theorem claim  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: Candidate C does not claim to recover Clay-target Navier-Stokes. It frames a fluid-gravity diagnostic and makes the dimension mismatch explicit.

Spec citation: `[NS-LANE-V0.2 @ <merge-sha>]:Workstream B`  
Framework citation: `[HG-MTH-005 @ 988307215ad38ccb16514311222184a1b757752b]`  
PFK citation: `[PFK-SCHEMA-003 @ 988307215ad38ccb16514311222184a1b757752b]`  
Boundary anti-seed: `[A-PFK-OP-001 @ 988307215ad38ccb16514311222184a1b757752b]`

## Status

v0.2 Candidate C lane opened. The previous v0.1 Kato-semigroup lane is not deleted; it is deferred behind the bulk/boundary diagnostic because v0.2 asks whether the proposed architecture reaches the target equation at all.

## Purpose

Workstream B develops Candidate C: a fluid-gravity adaptation based on AdS/boundary hydrodynamics.

The lane is disciplined by one first question:

> Does the Candidate C bulk equation and projection recover the three-spatial-dimensional incompressible Navier-Stokes equation, or only a known deformation/lower-dimensional analogue?

## Subdocuments

| Path | Purpose | Claim grade |
|---|---|---|
| `docs/workstream-b/literature/bhmr-2008-and-extensions.md` | consolidate fluid-gravity literature and dimension conventions | C0 / imported background |
| `docs/workstream-b/candidate-c-bulk-equation.md` | declare the Candidate C bulk equation template | C0 |
| `docs/workstream-b/candidate-c-projection.md` | declare the hydrodynamic-limit projection diagnostic | C0; future C1 if executed |

## Candidate C object map

| v0.2 object | Candidate C interpretation |
|---|---|
| `M` | asymptotically AdS bulk or adapted 4D bulk geometry |
| `Sigma` | conformal boundary or declared envelope hypersurface |
| `E_bulk` | Einstein-AdS equation with specified cosmological constant and matter/stress content |
| `pi_C` | holographic / boundary-stress / hydrodynamic projection |
| `v, p` | recovered fluid variables after declared non-relativistic/incompressible limit |

## Dimension guard

Standard `AdS_{d+1}` bulk has a `d`-dimensional spacetime boundary. Therefore:

- `AdS_4` normally gives a 2+1-dimensional boundary fluid.
- Clay-target 3D Navier-Stokes is a three-spatial-dimensional problem, usually represented as 3+1 spacetime.
- Candidate C must either explain a valid 4D-bulk / 3D-envelope construction outside standard conformal-boundary counting, or record failure/deformation.

This guard is load-bearing. It prevents the phrase `AdS_4/fluid_3` from silently becoming a Clay-target claim.

## Accepted diagnostic outputs

| Output | Meaning | Consequence |
|---|---|---|
| `structurally-valid-exact` | recovered equation matches target 3D incompressible NS in declared limit | Candidate C can inform v0.3 Clay-direction framing |
| `structurally-valid-deformed` | recovered equation is a known deformation or lower-dimensional analogue | Candidate C can inform failure analysis or revised architecture |
| `failed-diagnostic` | no NS or declared known deformation recovered | Candidate C is demoted to negative result |

## Promotion gate status

| Gate | Status |
|---|---|
| Gate 0 — spec accepted | satisfied by v0.2 spec PR |
| Gate 1 — apparatus implemented | C0 documents in progress |
| Gate 2 — fixture validated | pending D8 diagnostic |
| Gate 3 — descriptive-grade claim | not opened |
| Gate 4 — methodology-grade claim | not opened beyond C0 architecture |
| Gate 5 — theorem-grade artifact | not opened |
