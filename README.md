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

## Status

Bootstrap v0.1. No workstream apparatus implemented yet. No descriptive-grade or theorem-grade artifact emitted. Clay proximity: 0%.

## Structure

| Path | Content |
|---|---|
| `docs/program-spec/navier-stokes-program-v0_1.md` | Program spec authored from framework principles |
| `docs/workstream-a/` | Foundational typing |
| `docs/workstream-b/` | Mild solutions and Kato semigroup apparatus |
| `docs/workstream-c/` | Weak / Leray-Hopf class and energy structure |
| `docs/workstream-d/` | Regularity criteria registry |
| `docs/workstream-e/` | Numerical / empirical apparatus with strong anti-seed boundary |
| `docs/workstream-f/` | Promotion gates and audit |
| `DEPENDENCIES.md` | Pins Heller-Godel @ `988307215ad38ccb16514311222184a1b757752b` |
| `tests/test_pfk_dependency.py` | Validates dependency pin and skeleton structure |
| `.github/workflows/ns-program-pfk-dependency.yml` | CI dependency validation |

## Non-claims

This repository does not:

- claim existence or smoothness of global `R^3` or `T^3` solutions;
- claim a finite-time breakdown construction;
- claim a new blow-up criterion;
- promote any numerical simulation or energy-spectrum measurement beyond descriptive-grade;
- transfer methodology from RH, Hodge, Yang-Mills, P vs NP, or BSD as proof in the Navier-Stokes domain;
- treat Heller-Dirac spectral-triple reformulation as Navier-Stokes progress;
- treat Catalan / mu2 or any other framework fixture as Navier-Stokes-relevant beyond fixture-grade.

## Heller-Dirac relevance

Heller-Dirac is not yet a declared dependency of `ns-program`.

The natural future entry points are:

- Workstream B: mild solutions and analytic semigroup theory for the Stokes operator;
- Workstream D: regularity criteria where spectral multipliers and Littlewood-Paley apparatus may be relevant.

A follow-up PR may add Heller-Dirac as a second upstream pin when that content becomes active. Until then, the only declared dependency is Heller-Godel at the pinned commit in `DEPENDENCIES.md`.
