# Workstream A — Foundational Typing

Version: v0.2  
Claim grade: C0 definitions and typing only  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: foundational typing is not Navier-Stokes progress. It defines objects for the v0.2 diagnostic and does not prove regularity, smoothness, uniqueness, or boundary recovery.

Spec citation: `[NS-LANE-V0.2 @ <merge-sha>]:Workstream A`  
Framework citation: `[HG-FND-* @ 988307215ad38ccb16514311222184a1b757752b]`  
Heller-Einstein citation: `[HE-INT-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]`  
PFK citation: `[PFK-SCHEMA-001 @ 988307215ad38ccb16514311222184a1b757752b]`  
Boundary anti-seed: `[A-MTH-001 @ 988307215ad38ccb16514311222184a1b757752b]`

## Status

v0.2 foundational typing lane populated. This is still C0 apparatus, not theorem work.

## Purpose

Workstream A declares the objects that Candidates C and D must use so the v0.2 diagnostic can evaluate them without hidden vocabulary drift.

## Typed objects

| Symbol | Object | v0.2 role | Claim grade |
|---|---|---|---|
| `M` | 4-manifold / bulk carrier | carries candidate bulk equation `E_bulk` | C0 |
| `Sigma` | boundary/envelope hypersurface | receives projected/trace fluid data | C0 |
| `v` | velocity field on `Sigma` | target recovered boundary/envelope vector field | C0 |
| `p` | pressure field on `Sigma` | target recovered pressure scalar | C0 |
| `nu` | viscosity parameter | target positive viscosity in incompressible NS | C0 |
| `E_bulk` | bulk equation on `M` | candidate dynamics to be tested | C0 |
| `pi` | projection/trace map | maps admissible bulk solution data to boundary/envelope data | C0 |
| `tau` | observer trace/access chain | Heller-Einstein typed access-chain vocabulary when Candidate D is active | C0 |
| `D_C` | Candidate C diagnostic | tests AdS/fluid-gravity recovery | C0 design; C1 if executable/symbolic receipt emitted |
| `D_D` | Candidate D diagnostic | tests Heller-Einstein-native recovery | C0 design; C1 if executable/symbolic receipt emitted |

## Boundary/envelope convention

`Sigma` is not automatically the conformal boundary used in standard AdS/CFT. It may be:

1. a conformal boundary in Candidate C;
2. a time-like hypersurface/envelope embedded in a 4D bulk;
3. an observer-accessible trace surface in Candidate D.

Every document must say which meaning is active.

## Target equation form

The Clay target remains the three-spatial-dimensional incompressible Navier-Stokes equation under the official formulation surface:

```text
partial_t v + (v · grad) v + grad p = nu Delta v + f
 div v = 0
```

For unforced target comparisons, set `f = 0`. If a candidate recovers a forced, relativistic, MHD, Euler, or lower-dimensional variant, the result must be recorded as a known deformation rather than exact recovery.

## Candidate compatibility requirements

A candidate must declare:

- the bulk field variables;
- the boundary/envelope variables;
- the map from bulk variables to `v` and `p`;
- the limit in which comparison is made;
- whether the result is exact Navier-Stokes, a known deformation, or failure;
- whether the boundary dimension matches the Clay target.

## Dimension guard

A 4D bulk does not by itself imply a 3D spatial fluid. Standard `AdS_{d+1}` notation gives a `d`-dimensional spacetime boundary.

Therefore `AdS_4` normally supplies a 2+1-dimensional boundary spacetime, not a 3+1-dimensional spacetime. Candidate C must explicitly address this dimension issue before any Clay-facing interpretation is allowed.

## Promotion gate status

| Gate | Status |
|---|---|
| Gate 0 — spec accepted | satisfied by v0.1 bootstrap and v0.2 spec PR |
| Gate 1 — apparatus implemented | v0.2 C0 typing populated |
| Gate 2 — fixture validated | pending D8 diagnostic fixture |
| Gate 3 — descriptive-grade claim | not opened |
| Gate 4 — methodology-grade claim | not opened beyond C0 architecture |
| Gate 5 — theorem-grade artifact | not opened |
