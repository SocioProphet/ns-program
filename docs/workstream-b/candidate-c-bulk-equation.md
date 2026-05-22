# Candidate C Bulk Equation Scaffold

Version: v0.2  
Claim grade: C0 bulk-equation declaration only  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: this document declares the Candidate C equation template. It does not solve the equation, prove regularity, or prove that the projection recovers Navier-Stokes.

## Purpose

This document declares the Candidate C bulk equation surface before any derivation or diagnostic is attempted.

## Bulk template

Candidate C uses an Einstein-AdS-style bulk equation template:

```text
G_{AB} + Lambda g_{AB} = kappa T_{AB}^{matter}
```

where:

- `g_{AB}` is the bulk metric on `M`;
- `G_{AB}` is the Einstein tensor of `g`;
- `Lambda < 0` for AdS-style geometry when the AdS interpretation is active;
- `T_{AB}^{matter}` is declared matter/stress content;
- `A, B` are bulk indices.

This is a C0 template. The actual diagnostic must specify the exact bulk dimension, boundary/envelope dimension, matter content, boundary conditions, and hydrodynamic limit.

## Required declarations before D8

Any Candidate C diagnostic must declare:

| Field | Requirement |
|---|---|
| bulk dimension | exact dimension of `M` |
| boundary/envelope dimension | exact dimension of `Sigma` and whether it is conformal boundary or envelope hypersurface |
| cosmological constant | sign and normalization |
| matter content | whether `T_{AB}^{matter}` is zero, effective, scalar, gauge, or other |
| boundary conditions | conformal boundary, cutoff surface, membrane paradigm surface, or envelope data |
| fluid variables | definition of recovered `v`, `p`, `rho`, temperature, stress tensor, and viscosity |
| comparison limit | non-relativistic, incompressible, long-wavelength, near-equilibrium, or other |
| forcing | whether recovered equation is forced or unforced |

## Dimension diagnostic

If the bulk is declared as `AdS_4`, the default boundary is 2+1 spacetime. That does not match the 3+1 spacetime accounting of the Clay three-spatial-dimensional target.

Therefore an `AdS_4` implementation must choose one of the following:

1. record a lower-dimensional known-deformation result;
2. supply a nonstandard envelope construction that explains how a 3D spatial fluid state lives on `Sigma`;
3. switch to a dimensionally matched `AdS_5`-style bulk if the target is a conformal-boundary 3+1 fluid;
4. fail the diagnostic.

## Candidate C non-claims

This document does not claim:

- bulk existence;
- bulk regularity;
- boundary regularity;
- Navier-Stokes recovery;
- viscosity matching;
- pressure recovery;
- Clay-direction progress.

## D8 handoff

D8 must decide whether this template, once specified, recovers:

- exact 3D incompressible Navier-Stokes;
- a known deformation;
- nothing relevant.
