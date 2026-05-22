# Candidate C Literature Consolidation — BHMR 2008 and Extensions

Version: v0.2  
Claim grade: C0 literature map with imported background only  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: literature consolidation does not assert Clay relevance. It records what fluid-gravity literature can and cannot supply for Candidate C.

## Purpose

This document consolidates the fluid-gravity literature surface that Candidate C may cite when designing its v0.2 diagnostic.

The main imported reference family is the derivative-expansion fluid-gravity construction associated with Bhattacharyya, Hubeny, Minwalla, and Rangamani. The relevant content is hydrodynamic boundary stress/velocity behavior derived from gravitational bulk data in asymptotically AdS settings.

## What the literature may supply

Candidate C may use fluid-gravity literature for:

- the idea that long-wavelength perturbations of black brane geometries can be organized as relativistic hydrodynamics on the boundary;
- stress-tensor and conservation-equation vocabulary;
- derivative expansion / hydrodynamic limit vocabulary;
- dimensional bookkeeping for `AdS_{d+1}` bulk and `d`-dimensional boundary spacetime;
- known routes from relativistic conformal hydrodynamics to non-relativistic limits, where properly declared.

## What the literature may not supply

Candidate C may not use the literature as:

- a proof of 3D incompressible Navier-Stokes regularity;
- a proof that bulk regularity preserves boundary smoothness in the Clay sense;
- a proof that an `AdS_4` construction reaches a 3+1-dimensional fluid target;
- a reason to skip D8's equation-recovery diagnostic;
- a reason to claim Candidate C/D equivalence.

## Dimension convention

In standard notation, `AdS_{d+1}` has a `d`-dimensional conformal boundary. That `d` counts spacetime dimensions.

Therefore:

- `AdS_4` normally gives a 2+1-dimensional boundary fluid.
- `AdS_5` normally gives a 3+1-dimensional boundary fluid.
- Clay-target Navier-Stokes is three spatial dimensions with time, so dimension matching must be explicit.

Candidate C may still study a 4D-bulk / 3D-envelope construction, but it must declare when it has left standard conformal-boundary counting.

## v0.2 use of BHMR-style material

The v0.2 use is limited to a diagnostic template:

```text
bulk metric / matter data
  -> boundary stress tensor or envelope stress data
  -> hydrodynamic conservation equation
  -> non-relativistic / incompressible / long-wavelength limit
  -> compare with 3D Navier-Stokes target equation
```

Every arrow must be declared. Missing arrows are diagnostic failures, not prose gaps.

## Candidate C literature checklist

Before any Candidate C derivation is accepted into the repo, record:

- bulk dimension;
- boundary/envelope dimension;
- whether the boundary is conformal or envelope-based;
- whether the fluid is relativistic or non-relativistic;
- whether the fluid is conformal or incompressible;
- whether viscosity arises and how it is normalized;
- whether pressure is recovered as a scalar field or stress component;
- whether forcing or matter coupling appears;
- whether the result is exact target recovery, known deformation, or failure.

## Imported-background boundary

Fluid-gravity literature is C3 only as imported background about its own claims. Its use inside `ns-program` remains C0 unless D8 emits a certified artifact.
