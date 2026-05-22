# Navier-Stokes Program Anti-Seed Register

Version: v0.2  
Claim grade: C0 anti-seed / failure-mode register  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: this register prevents false promotion. It does not assert any positive Navier-Stokes result.

## Purpose

This file records failure modes that `ns-program` v0.2 explicitly guards against.

Anti-seeds are not optional prose. They are claim-boundary controls for review and CI-facing documentation tests.

## A-NS-001 — Holographic vocabulary is not mathematical work

Failure mode:

```text
The document uses holography, bulk/boundary, AdS, envelope, or duality language as if vocabulary itself were a derivation.
```

Guard:

Candidate C must state a bulk equation, projection map, limit, dimension convention, and recovered equation before any diagnostic status is assigned.

## A-NS-002 — Projection-induced stochasticity is not a deterministic NS solution operator

Failure mode:

```text
HE-PROJ vocabulary or many-to-one observer trace language is treated as if it supplied a deterministic Navier-Stokes flow map.
```

Guard:

Candidate D must distinguish deterministic PDE recovery, kernel-valued observer dynamics, trace-only output, not-configured state, and no-recovery.

## A-NS-003 — Bulk regularity is not boundary regularity

Failure mode:

```text
A regular 4D bulk solution is assumed to imply smooth 3D boundary/envelope Navier-Stokes solution without a projection theorem.
```

Guard:

D8 must provide a projection argument. No document may infer boundary smoothness from bulk smoothness by analogy.

## A-NS-004 — Fluid-gravity hydrodynamics is not Clay relevance

Failure mode:

```text
Fluid-gravity literature is cited as if boundary hydrodynamics solves or advances the Clay Navier-Stokes problem.
```

Guard:

Candidate C must classify recovery as exact target, known deformation, no-recovery, or not-configured. Lower-dimensional or relativistic hydrodynamics is not the Clay target unless an explicit dimension/limit argument is supplied.

## A-NS-005 — AdS dimension mismatch must not be hidden

Failure mode:

```text
AdS_4/fluid_3 is used as if it automatically meant a three-spatial-dimensional incompressible fluid target.
```

Guard:

Standard `AdS_{d+1}` boundary counting treats `d` as spacetime dimension. Candidate C must explicitly record bulk dimension, boundary spacetime dimension, and recovered spatial fluid dimension.

## A-NS-006 — Reserved upstream namespace is not implemented content

Failure mode:

```text
HE-PHYS-001 is cited as if canonical physical-core content exists at the pinned Heller-Einstein commit when only a namespace or future-work statement exists.
```

Guard:

Candidate D must mark the physical-core bulk equation as unavailable/not-configured unless file-level pinned evidence exists.

## A-NS-007 — 2D regularity does not transfer to 3D Clay target

Failure mode:

```text
The known 2D bootstrap is treated as evidence that the v0.2 architecture controls the 3D problem.
```

Guard:

The 2D anchor is imported C3 background only. It guards dimension discipline and does not supply portfolio theorem content.

## A-NS-008 — Candidate C/D correspondence is not equivalence

Failure mode:

```text
A result, failure, or intuition from one candidate lane is transferred to the other through the conjectured correspondence.
```

Guard:

The correspondence is C0 organizing structure only. It has no theorem status and no promotion authority.

## A-NS-009 — Time-theory material must not leak into ns-program v0.2

Failure mode:

```text
Quasicrystalline temporal structure, plastic-number dynamics, cut-and-project time foliation, wave archetypes, force-generator decomposition, Kozyrev replication, or time-as-substance language is incorporated into ns-program v0.2.
```

Guard:

Those topics are routed to the separate time-theory strategic-direction track. They may enter `ns-program` only through a future pinned dependency and method-grade citation.

## A-NS-010 — Diagnostic fallback is not global evidence

Failure mode:

```text
A perturbative, asymptotic, Stokes-flow, Couette-flow, or other fixture-level diagnostic is promoted to global smoothness or singularity evidence.
```

Guard:

Fallback diagnostics are C1 at most and only for the declared configuration and limit.

## Review checklist

Before merging v0.2 or later documents, verify:

- no document uses `regular`, `smooth`, `global`, or `singularity-free` as a new claim;
- Candidate C includes dimension bookkeeping;
- Candidate D distinguishes canonical upstream content from reserved namespace;
- D8 outcomes are candidate-specific;
- no time-theory out-of-scope material appears in v0.2 docs;
- no imported classical result is used as proof transfer.
