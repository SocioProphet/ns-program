# Workstream D — v0.2 Diagnostic Gate

Version: v0.2  
Claim grade: C0 diagnostic design; C1 only after certified symbolic/computational artifacts exist  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: the diagnostic asks whether Candidates C or D recover Navier-Stokes. This document does not assert either recovery.

Spec citation: `[NS-LANE-V0.2 @ <merge-sha>]:Workstream D`  
Framework citation: `[HG-FND-* @ 988307215ad38ccb16514311222184a1b757752b]`  
PFK citation: `[PFK-SCHEMA-* @ 988307215ad38ccb16514311222184a1b757752b]`  
Boundary anti-seed: `[A-MTH-001 @ 988307215ad38ccb16514311222184a1b757752b]`

## Status

v0.2 diagnostic lane populated. The previous v0.1 regularity-criteria registry remains valid background but is not the active first diagnostic in this tranche.

## Diagnostic question

For each candidate bulk equation, under its declared projection, does the recovered boundary/envelope equation of motion match the three-spatial-dimensional incompressible Navier-Stokes equations or a known deformation in a specified limit?

Candidate C projection:

```text
pi_C: Sol(E_bulk^C on M_C) -> FluidData(Sigma_C)
```

Candidate D projection:

```text
pi_D := rho_D o tau_D: X -> Y_O -> FluidData(Sigma_D)
```

## Target comparison

The target comparison equation is:

```text
partial_t v + (v · grad) v + grad p = nu Delta v + f
 div v = 0
```

The diagnostic must declare whether `f = 0`, whether `f` is known forcing, or whether the recovered equation is outside this target family.

## Candidate-level outcomes

| Outcome | Meaning | Permitted next step |
|---|---|---|
| `recovers-target-ns` | recovered equation matches 3D incompressible Navier-Stokes in a declared limit | Candidate may inform v0.3 Clay-direction framing |
| `known-deformation` | recovered equation is a known deformation, such as relativistic fluid, Euler, MHD, forced fluid, or 2+1-dimensional analogue | Candidate may inform revised architecture or deformation analysis |
| `no-recovery` | recovered equation does not match NS or a known deformation | Candidate demoted to documented negative result |
| `not-configured` | required bulk equation, projection, or upstream canonical content is missing | Candidate blocked; not counted as success or failure |

## Candidate C special diagnostic

Candidate C must include a dimension-matching decision:

| Check | Required answer |
|---|---|
| `bulk_dimension` | exact dimension of Candidate C bulk |
| `boundary_spacetime_dimension` | exact dimension of boundary/envelope spacetime |
| `fluid_spatial_dimension` | exact spatial dimension of recovered fluid |
| `standard_ads_counting` | whether standard `AdS_{d+1}` boundary counting is used |
| `clay_dimension_match` | yes/no, with reason |

If Candidate C uses `AdS_4` under standard counting, the default result is a 2+1-dimensional boundary spacetime. That cannot be treated as Clay-target recovery without an additional declared envelope argument.

## Candidate D special diagnostic

Candidate D must include a canonical-content decision:

| Check | Required answer |
|---|---|
| `canonical_bulk_equation_available` | yes/no, with pinned file evidence |
| `trace_map_declared` | yes/no |
| `fluid_recovery_map_declared` | yes/no |
| `deterministic_or_kernel` | deterministic equation, Markov kernel, ensemble dynamics, or unknown |
| `target_equation_recovered` | yes/no/known deformation/not configured |

If a canonical Heller-Einstein physical-core equation is unavailable at the pin, Candidate D status is `not-configured`, not `recovers-target-ns`.

## C0 derivation mode

A formal derivation may remain C0 if it only manipulates declared symbols and produces a derivation sketch without executable artifact, certified trace, or replay package.

C0 derivation outputs must include:

- exact assumptions;
- exact limit;
- declared equations;
- declared projection map;
- diagnostic classification;
- non-claim summary.

## C1 artifact mode

A symbolic or computational diagnostic may become C1 only if it emits:

- `RunSpec`;
- `RunReceipt`;
- input traces;
- output traces;
- artifact hashes;
- declared comparison target;
- diagnostic status.

Any C1 artifact touching executable code must be recorded in `TRUST_SURFACE.yaml`.

## Fallback configurations

If full symbolic derivation is intractable, the diagnostic may run around known configurations:

- Stokes flow;
- plane Couette flow;
- Taylor-Couette flow;
- linearized incompressible perturbations;
- shear-flow backgrounds.

Fallback diagnostics must mark the limit and configuration explicitly. They are not global statements.

## Pause and continue conditions

Pause condition: if both Candidates C and D return `no-recovery`, pause Clay-direction framing and open failure analysis.

Blocked condition: if both candidates return `not-configured`, pause and improve upstream specifications before claiming failure.

Continue condition: if either candidate returns `recovers-target-ns` or `known-deformation`, v0.3 may choose a Clay-direction or deformation-analysis workstream.

## Promotion gate status

| Gate | Status |
|---|---|
| Gate 0 — spec accepted | satisfied by v0.2 spec PR |
| Gate 1 — apparatus implemented | C0 diagnostic design populated |
| Gate 2 — fixture validated | pending first diagnostic artifact |
| Gate 3 — descriptive-grade claim | not opened |
| Gate 4 — methodology-grade claim | not opened beyond C0 architecture |
| Gate 5 — theorem-grade artifact | not opened |
