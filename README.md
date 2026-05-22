# ns-program — Navier-Stokes Program

Navier-Stokes program in the SocioProphet Clay-program portfolio.

## Clay target

The Clay Navier-Stokes problem asks whether smooth, finite-energy, divergence-free initial data extends to a smooth solution of the incompressible Navier-Stokes equations for all time, or whether a smooth finite-time breakdown example exists.

There are four official solution surfaces:

- existence and smoothness on `R^3`;
- existence and smoothness on `T^3`;
- breakdown on `R^3`;
- breakdown on `T^3`.

A proof of any one official version resolves the Clay problem.

## Framework restatement

The vorticity `omega = curl u` is the curvature-like obstruction associated with Eulerian flow. The Clay question can be organized as whether this curvature remains controlled on every finite time interval.

The Stokes operator `A = -P Delta`, with `P` the Leray projection onto divergence-free vector fields, supplies the analytic-semigroup surface for mild-solution work.

This program treats that restatement as framework vocabulary only. It is not a proof and not progress by itself.

## Current status

v0.2 strategic-direction tranche in progress.

v0.1 bootstrapped the repository with Heller-Godel dependency, program spec, workstream skeletons, tests, and CI. v0.2 opens the first substantive architectural tranche: a 4D-bulk / boundary-envelope investigation with two diagnostic candidates and explicit anti-seed boundaries.

Claim posture remains method-grade / C0 unless a future diagnostic emits certified artifacts. No theorem-grade content is produced in v0.2. No Clay-direction commitment is made in v0.2.

Estimated Clay proximity after v0.2 completion: 1-3%. This is a planning estimate only, not evidence.

## v0.2 architecture

Candidate C: AdS / fluid-gravity adaptation. This lane studies whether a declared bulk Einstein-AdS-style equation and hydrodynamic projection can recover the target 3D incompressible Navier-Stokes equation or a known deformation.

Candidate D: Heller-Einstein-native typed projection. This lane studies whether Heller-Einstein interface/projection vocabulary can be instantiated to recover a deterministic fluid equation, a known deformation, kernel-valued observer dynamics, or no configured equation.

The conjectured C/D correspondence is recorded only as a C0 organizing principle. It is not an equivalence theorem and does not transfer claims between lanes.

## Dimension guard

A standard `AdS_{d+1}` bulk has a `d`-dimensional conformal boundary, with `d` counted as spacetime dimension. Therefore `AdS_4` normally yields a 2+1-dimensional boundary fluid, not a 3+1-dimensional Clay-target fluid. Candidate C must explicitly resolve or record that dimensional issue.

## Structure

| Path | Content |
|---|---|
| `docs/program-spec/navier-stokes-program-v0_1.md` | v0.1 bootstrap spec |
| `docs/program-spec/navier-stokes-program-v0_2.md` | v0.2 strategic direction |
| `docs/scope/ns-program-bridge-citation.md` | Heller-Godel / Heller-Einstein citation discipline |
| `docs/scope/v0.2-non-claim-box.md` | controlling v0.2 non-claim box |
| `docs/foundations/2d-ns-anchor.md` | imported 2D Navier-Stokes background and 3D non-transfer guard |
| `docs/workstream-a/` | v0.2 foundational typing |
| `docs/workstream-b/` | Candidate C fluid-gravity development |
| `docs/workstream-c/` | Candidate D Heller-Einstein-native development |
| `docs/workstream-d/` | v0.2 diagnostic gate |
| `docs/correspondence/c-d-conjectured-correspondence.md` | C/D organizing conjecture and non-equivalence boundary |
| `docs/anti-seed-ns.md` | Navier-Stokes anti-seed register |
| `DEPENDENCIES.md` | Pins Heller-Godel and Heller-Einstein |
| `TRUST_SURFACE.yaml` | Trust-surface declaration for current docs and future diagnostics |
| `tests/test_pfk_dependency.py` | Validates dependency pins and v0.2 structure |
| `.github/workflows/ns-program-pfk-dependency.yml` | CI dependency validation |

## Non-claims

This repository does not:

- claim existence or smoothness of global `R^3` or `T^3` solutions;
- claim a finite-time breakdown construction;
- claim a new blow-up criterion;
- promote any numerical simulation or energy-spectrum measurement beyond descriptive-grade;
- transfer methodology from RH, Hodge, Yang-Mills, P vs NP, or BSD as proof in the Navier-Stokes domain;
- treat Heller-Dirac spectral-triple reformulation as Navier-Stokes progress;
- treat Heller-Godel framework vocabulary as proof transfer;
- treat Heller-Einstein projection vocabulary as a deterministic Navier-Stokes solution operator;
- claim Candidate C recovers Navier-Stokes before D8 emits a diagnostic result;
- claim Candidate D recovers Navier-Stokes before D8 emits a diagnostic result;
- claim Candidate C and Candidate D are equivalent;
- import time-theory material into v0.2.

## Heller-Einstein relevance

Heller-Einstein is now a declared v0.2 dependency for typed interface and projection vocabulary.

At the pinned commit, `HE-INT-*` and `HE-PROJ-*` are permitted as framework vocabulary. `HE-PHYS-*` and `HE-PHYS-001` are treated as reserved/future unless a pinned canonical file proves otherwise.

## Heller-Dirac relevance

Heller-Dirac is not yet a declared dependency of `ns-program`.

The natural future entry points are:

- mild solutions and analytic semigroup theory for the Stokes operator;
- regularity criteria where spectral multipliers and Littlewood-Paley apparatus may be relevant.

A follow-up PR may add Heller-Dirac as another upstream pin when that content becomes active.
