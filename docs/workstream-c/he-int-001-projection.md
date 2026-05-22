# Candidate D — HE-INT-001 Projection Scaffold

Version: v0.2  
Claim grade: C0 typed-projection scaffold; future C1 only with certified diagnostic receipts  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: typed interface vocabulary does not recover Navier-Stokes by itself. Projection-induced stochasticity must not be confused with a deterministic Navier-Stokes solution operator.

## Purpose

This document specifies how Candidate D instantiates Heller-Einstein typed-interface vocabulary for the v0.2 fluid-dynamics diagnostic.

## Typed access-chain slot

Candidate D uses the following access-chain slot notation:

```text
X -> Y_O -> M_O
```

where:

- `X` is latent/bulk state space;
- `Y_O` is observer-relative accessible trace data;
- `M_O` is observer-model or measurement-facing state;
- the fluid variables `v` and `p` must be explicitly recovered from `Y_O` or `M_O` if the diagnostic is to proceed.

## Candidate D projection template

```text
tau_D: X -> Y_O
rho_D: Y_O -> FluidData(Sigma)
pi_D := rho_D o tau_D
```

This is a C0 template. It is not an asserted solution map.

## Required fluid instantiation

To instantiate this template for Navier-Stokes, Candidate D must declare:

| Object | Required declaration |
|---|---|
| `X` | bulk state variables and admissible states |
| `Y_O` | observer-accessible trace variables |
| `M_O` | measurement/model state if distinct from `Y_O` |
| `Sigma` | boundary/envelope surface receiving fluid data |
| `rho_D` | map from trace variables to fluid velocity/pressure data |
| `v` | recovered velocity field and dimensionality |
| `p` | recovered pressure field or pressure surrogate |
| `nu` | viscosity or effective transport coefficient |
| equation of motion | recovered equation on `Sigma` |

## Stochasticity guard

If `tau_D` is many-to-one, observer-level dynamics may be stochastic or Markov-kernel-valued. That is not the same thing as a deterministic Navier-Stokes evolution map.

Therefore any Candidate D diagnostic must distinguish:

- deterministic equation recovery;
- stochastic observer-level evolution;
- ensemble or Markov-kernel dynamics;
- unknown / not configured.

## Diagnostic states

| State | Meaning |
|---|---|
| `not-configured` | required bulk equation, trace map, or fluid recovery map missing |
| `trace-only` | interface trace exists but no equation of motion recovered |
| `kernel-valued` | observer dynamics are Markov-kernel-valued and not deterministic NS |
| `known-deformation` | recovered equation is a declared known fluid deformation |
| `target-recovery` | recovered equation matches target 3D incompressible NS in declared limit |

## D8 artifact requirements

Any Candidate D C1 diagnostic must emit:

- RunSpec with all maps and spaces named;
- RunReceipt with artifact hashes;
- exact recovered equation;
- comparison target;
- status selected from the diagnostic states above;
- explicit reason if status is `not-configured`, `trace-only`, or `kernel-valued`.

## Non-claim guard

Forbidden inference:

```text
HE-PROJ vocabulary explains observer-level stochasticity.
Therefore Candidate D provides a Navier-Stokes solution operator.
```

Required inference:

```text
HE-PROJ vocabulary supplies a projection discipline.
D8 must determine whether a deterministic target equation, a known deformation, a kernel-valued evolution, or no equation is recovered.
```
