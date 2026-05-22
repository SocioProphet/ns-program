# Candidate C Projection Scaffold

Version: v0.2  
Claim grade: C0 projection-design document; future C1 only with certified diagnostic receipts  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: this document defines the Candidate C projection question. It does not assert that any projection recovers Navier-Stokes.

## Purpose

This document declares how Candidate C must express its projection from bulk data to boundary/envelope fluid data.

The projection is not accepted by prose. It must be stated as a map with declared domain, codomain, limit, and comparison equation.

## Projection template

```text
pi_C: Sol(E_bulk on M; boundary/envelope conditions) -> FluidData(Sigma)
```

where `FluidData(Sigma)` must include, at minimum:

- a velocity field `v` on `Sigma` or on a declared spatial slice of `Sigma`;
- a pressure scalar or pressure-equivalent stress component `p`;
- a viscosity parameter or effective transport coefficient `nu`;
- a divergence constraint or replacement constraint;
- an equation of motion after the declared limit.

## Required comparison equation

The target comparison equation is:

```text
partial_t v + (v · grad) v + grad p = nu Delta v + f
 div v = 0
```

Candidate C must declare whether `f = 0`, whether `f` is a known forcing term, or whether the recovered equation is not in this class.

## Limit declaration

Each projection attempt must specify:

| Limit | Required declaration |
|---|---|
| hydrodynamic | derivative expansion order and small parameter |
| non-relativistic | scaling of velocity, pressure, time, and stress tensor |
| incompressible | divergence constraint and density/temperature assumptions |
| boundary/envelope | whether `Sigma` is conformal boundary, cutoff surface, membrane surface, or nonstandard envelope |
| dimension | bulk dimension, boundary spacetime dimension, spatial fluid dimension |

## Diagnostic classification

The projection output must be classified as exactly one of:

1. `recovers-target-ns`: recovered equation matches 3D incompressible Navier-Stokes in a declared limit.
2. `known-deformation`: recovered equation is a known deformation, such as relativistic conformal hydrodynamics, Euler flow without viscosity, forced fluid dynamics, MHD, or 2+1-dimensional Navier-Stokes analogue.
3. `no-recovery`: recovered equation does not match target or known deformation.
4. `not-configured`: required projection data are missing.

## Artifact requirements for C1

If any symbolic or computational diagnostic is added later, it must emit:

- `RunSpec` describing equation, projection, assumptions, and limits;
- `RunReceipt` with artifact hashes;
- input and output traces;
- exact comparison target;
- null or perturbation cases if promoted toward C2.

Without those artifacts, the result remains C0 derivation prose.

## Promotion guard

Forbidden inference:

```text
Fluid-gravity gives boundary hydrodynamics.
Therefore Candidate C recovers Clay-target Navier-Stokes.
```

Required inference:

```text
Fluid-gravity supplies a candidate projection architecture.
D8 must determine whether the recovered equation matches the Clay target, a known deformation, or neither.
```
