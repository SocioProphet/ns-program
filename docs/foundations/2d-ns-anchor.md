# 2D Navier-Stokes Anchor

Version: v0.2  
Claim grade: imported C3 background; no new theorem content  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: the two-dimensional bootstrap is recorded as classical background only. It does not transfer to the 3D Clay problem and does not supply a new regularity criterion.

## Purpose

This document records the classical two-dimensional Navier-Stokes regularity anchor so the v0.2 bulk/boundary program does not confuse a closed 2D bootstrap with progress on the 3D Clay target.

The anchor is imported background. It is not a portfolio theorem.

## Classical 2D statement, informal form

For incompressible Navier-Stokes in two spatial dimensions, the standard Leray-Hopf weak-solution framework, energy inequality, Ladyzhenskaya inequality, enstrophy control, and Gronwall-type uniqueness/regularity bootstrap close under the usual hypotheses.

This is the background reason two-dimensional incompressible Navier-Stokes is not the Clay obstruction.

## Why the 2D bootstrap closes

The 2D mechanism is controlled by criticality.

In two spatial dimensions, the Sobolev and interpolation structure permits nonlinear terms to be controlled by energy/enstrophy quantities. The Ladyzhenskaya inequality supplies a key estimate of the form that `L^4` norms can be bounded by `L^2` and `H^1` quantities in the dimension needed for the nonlinear term.

At the level of vorticity, the two-dimensional equation lacks the 3D vortex-stretching term. This removes the central amplification mechanism that obstructs a direct 3D global regularity bootstrap.

## Why this does not solve the 3D problem

In three spatial dimensions, the Navier-Stokes scaling is supercritical relative to the basic energy estimate. The nonlinear transport/stretching structure cannot be controlled by the same 2D energy-enstrophy mechanism.

The 3D vorticity equation contains vortex stretching. This term is absent in 2D and is one of the central analytic obstructions in the Clay problem.

Therefore, any v0.2 document that cites the 2D anchor must include this boundary:

> The 2D bootstrap is imported C3 background. It does not transfer to the 3D Clay target and does not establish global smoothness, uniqueness, or singularity exclusion for 3D Navier-Stokes.

## Relation to v0.2 Candidate C

If Candidate C recovers a 2+1-dimensional boundary fluid rather than a 3+1-dimensional spacetime fluid, this anchor becomes a diagnostic warning. A recovered 2D spatial fluid may be mathematically meaningful, but it is not the Clay target unless an explicit dimension-raising or envelope argument is supplied.

## Relation to v0.2 Candidate D

If Candidate D's typed access chain recovers an observer-level two-dimensional or effectively two-dimensional fluid model, it may still be useful as a fixture or sanity check. It cannot be promoted to Clay-relevant evidence without an explicit 3D recovery argument.

## Imported references

Canonical background families include Ladyzhenskaya, Lions, Temam, and standard PDE treatments of Leray-Hopf solutions and two-dimensional global well-posedness. These are imported mathematical background, not repo-native proof objects.

## Anti-seed boundary

Forbidden inference:

```text
2D NS regularity is known.
The v0.2 bulk/envelope framework can express a 2D boundary fluid.
Therefore the framework has made Clay progress.
```

Correct inference:

```text
2D NS regularity is known background.
The v0.2 diagnostic must distinguish 2D recovery from 3D Clay-target recovery.
```
