# Workstream C — Candidate D: Heller-Einstein-Native Bulk

Version: v0.2  
Claim grade: C0 candidate-development lane; no theorem claim  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: Candidate D does not claim that Heller-Einstein projection apparatus recovers Navier-Stokes. It defines a diagnostic lane and distinguishes canonical upstream content from reserved physical-core targets.

Spec citation: `[NS-LANE-V0.2 @ <merge-sha>]:Workstream C`  
Framework citation: `[HG-MTH-005 @ 988307215ad38ccb16514311222184a1b757752b]`  
Heller-Einstein citation: `[HE-INT-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]`; `[HE-PROJ-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]`  
PFK citation: `[PFK-SCHEMA-003 @ 988307215ad38ccb16514311222184a1b757752b]`  
Boundary anti-seed: projection-induced stochasticity is not a deterministic Navier-Stokes solution operator.

## Status

v0.2 Candidate D lane opened. The previous v0.1 Leray-Hopf/energy-structure lane remains valid background but is deferred behind the bulk/boundary diagnostic.

## Purpose

Workstream C develops Candidate D: a Heller-Einstein-native bulk / typed observer-trace formulation for fluid dynamics.

The lane is disciplined by one first question:

> Does Heller-Einstein interface/projection apparatus, when instantiated for a fluid-dynamics boundary/envelope, produce an equation of motion matching 3D Navier-Stokes or a known deformation?

## Upstream status boundary

At the pinned Heller-Einstein commit, the repository advertises interface/projection vocabulary as canonicalized and identifies `HE-PHYS-*` conservative physical-core work as future direction. Therefore, Candidate D may use `HE-INT-*` and `HE-PROJ-*` as pinned vocabulary, but must treat `HE-PHYS-001` as reserved/unimplemented unless a later pinned file supplies canonical content.

## Subdocuments

| Path | Purpose | Claim grade |
|---|---|---|
| `docs/workstream-c/he-phys-001-as-bulk.md` | evaluate whether a future/available Heller-Einstein physical core can serve as `E_bulk` | C0 |
| `docs/workstream-c/he-int-001-projection.md` | instantiate typed access-chain vocabulary for fluid trace diagnostics | C0; future C1 if executed |

## Candidate D object map

| v0.2 object | Candidate D interpretation |
|---|---|
| `M` | Heller-Einstein bulk carrier or physical-core manifold once specified |
| `Sigma` | observer-accessible boundary/envelope trace surface |
| `E_bulk` | Heller-Einstein-native bulk equation if canonical; otherwise reserved target |
| `tau` | typed access chain from latent/bulk state to observer-accessible structure |
| `pi_D` | projection from bulk/interface data to fluid data |
| `v, p` | recovered fluid velocity and pressure if diagnostic succeeds |

## Accepted diagnostic outputs

| Output | Meaning | Consequence |
|---|---|---|
| `structurally-valid-exact` | typed trace recovers target 3D incompressible NS in declared limit | Candidate D can inform v0.3 Clay-direction framing |
| `structurally-valid-deformed` | typed trace recovers a known deformation or lower-dimensional analogue | Candidate D can inform revised architecture or negative result |
| `failed-diagnostic` | typed trace does not recover NS or declared known deformation | Candidate D is demoted to negative result |
| `not-configured` | upstream physical-core equation or required trace data are unavailable | Candidate D remains blocked, not failed |

## Promotion gate status

| Gate | Status |
|---|---|
| Gate 0 — spec accepted | satisfied by v0.2 spec PR |
| Gate 1 — apparatus implemented | C0 documents in progress |
| Gate 2 — fixture validated | pending D8 diagnostic |
| Gate 3 — descriptive-grade claim | not opened |
| Gate 4 — methodology-grade claim | not opened beyond C0 architecture |
| Gate 5 — theorem-grade artifact | not opened |
