# Navier-Stokes Program Lane v0.2 — Strategic Direction

Version: v0.2  
Claim grade: C0 method-grade structural commitment; C1 only for future executable diagnostics; no new C3 content  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: no Navier-Stokes regularity theorem, no Clay-direction commitment, no proof transfer from holography or Heller-Einstein, no assertion that either candidate bulk projection recovers 3D Navier-Stokes.

## Status target

v0.1 bootstrap -> v0.2 first-substantive-tranche.

Estimated Clay proximity after completed v0.2: 1-3%. This number is a portfolio planning estimate only. It is not evidence for smoothness, breakdown, or any Clay-relevant theorem.

## Architectural commitment

The v0.2 program opens a 4D-bulk / boundary-envelope workstream for investigating whether a higher-dimensional geometric formulation can produce the incompressible Navier-Stokes equations at an observer-accessible boundary or envelope.

The v0.2 architectural commitment is C0. It defines objects and diagnostics. It does not assert that the architecture succeeds.

The intended geometric vocabulary is:

- `M`: a 4-manifold carrying bulk dynamics.
- `Sigma`: a time-like boundary/envelope hypersurface in `M`.
- `v`: a velocity field recovered on the boundary/envelope, if recovery succeeds.
- `p`: a pressure field recovered on the boundary/envelope, if recovery succeeds.
- `E_bulk`: the candidate bulk equation on `M`.
- `pi`: a projection or trace map from admissible bulk solution data to boundary/envelope fluid data.
- `tau`: observer-trace access chain, using Heller-Einstein interface vocabulary where applicable.

## Dimension convention and obstruction check

The Clay Navier-Stokes problem is a three-spatial-dimensional incompressible fluid problem. A standard `AdS_{d+1}` bulk has a `d`-dimensional conformal boundary, where `d` is spacetime dimension, not spatial dimension alone.

Therefore, a naive `AdS_4 / fluid_3` phrase denotes a 2+1-dimensional boundary fluid in the standard convention. It does not automatically match the Clay 3+1 spacetime target.

v0.2 records this as a mandatory diagnostic obstruction, not as a reason to discard the direction prematurely. Candidate C must pass a dimension-matching check before it can be treated as structurally valid for the Clay 3D Navier-Stokes target.

## Candidate C — AdS/fluid-gravity adaptation

Candidate C studies a fluid-gravity adaptation rooted in the Bhattacharyya-Hubeny-Minwalla-Rangamani derivative-expansion framework and later extensions.

Candidate C starts with the user-proposed `AdS_4 / fluid_3` wording, but immediately subjects it to the dimension convention check above. The first diagnostic question is whether the program can define a boundary/envelope whose recovered equation is the three-spatial-dimensional incompressible Navier-Stokes equation, or whether the construction only yields a 2+1-dimensional relativistic conformal fluid.

Permitted Candidate C outcomes in v0.2:

1. `structurally-valid-exact`: the projection recovers the target Navier-Stokes equation to the declared order and limit.
2. `structurally-valid-deformed`: the projection recovers a known deformation, such as relativistic hydrodynamics, Euler flow, forced fluid dynamics, MHD-extended fluid dynamics, or a 2+1-dimensional analogue.
3. `failed-diagnostic`: the projection does not recover Navier-Stokes or a declared known deformation.

## Candidate D — Heller-Einstein-native bulk

Candidate D studies whether Heller-Einstein interface/projection apparatus can supply a native 4D bulk and typed observer trace for fluid dynamics.

The pinned Heller-Einstein repository currently canonicalizes interface/projection vocabulary and advertises `HE-PHYS-*` conservative physical-core work as a future direction. Therefore, v0.2 may cite `HE-INT-*` and `HE-PROJ-*` as available framework vocabulary at the pinned commit, while treating `HE-PHYS-001` as reserved/unimplemented unless a later pinned commit supplies the canonical document.

Candidate D does not assert that projection-induced stochasticity is a deterministic Navier-Stokes solution map. The D8 diagnostic must determine whether any typed trace instantiation yields the desired boundary/envelope equation of motion.

## Candidate C/D correspondence

A conjectured correspondence between Candidates C and D is recorded only as a method-grade organizing principle.

The correspondence's morphism class is not fixed in advance. It may be bijective, surjective, injective, functorial only after quotienting, or absent. v0.2 does not verify the correspondence.

The correspondence is useful only as cross-validation discipline: claims formulated in one candidate lane should expose a checkable target in the other lane.

## Claim discipline

v0.2 uses the following claim grades:

| Grade | Meaning in v0.2 |
|---|---|
| C0 | Definitions, architectural commitments, typing, dependency declarations, diagnostic design |
| C1 | Certified finite empirical or computational/symbolic artifacts with RunSpec, RunReceipt, traces, and artifact hashes |
| C2 | Reproducible empirical structure after replay under null models and perturbations |
| C3 | Imported theorem-level background only |

No new C3 theorem-grade content is permitted in v0.2.

Any sentence containing `theorem`, `for all`, `asymptotically`, `regular`, `smooth`, `singularity-free`, `global existence`, `uniqueness`, or analogous promotion language must be either:

- C0 definitional or diagnostic-scoping language;
- C3 imported classical background with citation; or
- removed.

## Imported C3 background allowed in v0.2

The only C3-grade content allowed in v0.2 is imported background, including:

- classical 2D Navier-Stokes global well-posedness / regularity background as summarized in `docs/foundations/2d-ns-anchor.md`;
- official Clay problem statements and standard formulation surfaces;
- fluid-gravity boundary-stress and hydrodynamic-limit results from the cited literature, limited to what those results actually establish;
- Heller-Einstein projection/interface results at the pinned commit, only where canonicalized in that repository.

Imported C3 background does not transfer to portfolio-specific theorem claims.

## v0.2 deliverables

### D1 — Spec extension

Create this v0.2 strategic-direction document. Mark architecture C0.

### D2 — Dependency pin

Update `DEPENDENCIES.md` and CI so `ns-program` declares dual upstream dependencies on Heller-Godel and Heller-Einstein.

### D3 — Citation discipline document

Create `docs/scope/ns-program-bridge-citation.md` recording which upstream identifiers may be cited, at which claim grade, and with which non-claim boundaries.

### D4 — 2D Navier-Stokes anchor document

Create `docs/foundations/2d-ns-anchor.md` as imported C3 background and as a guardrail against pretending the 2D bootstrap solves the 3D Clay problem.

### D5 — Workstream A foundational typing

Populate `docs/workstream-a/README.md` with typed objects for `M`, `Sigma`, `v`, `p`, `E_bulk`, `pi`, and `tau`.

### D6 — Workstream B Candidate C development

Populate `docs/workstream-b/README.md` and add Candidate C subdocuments for literature consolidation, bulk equation framing, and projection framing.

### D7 — Workstream C Candidate D development

Populate `docs/workstream-c/README.md` and add Candidate D subdocuments for Heller-Einstein bulk status and typed projection instantiation.

### D8 — Workstream D diagnostic question

Populate `docs/workstream-d/README.md` with the first diagnostic: does either candidate produce a boundary/envelope equation matching 3D Navier-Stokes or a known deformation in a declared limit?

### D9 — Conjectured correspondence

Create `docs/correspondence/c-d-conjectured-correspondence.md` as method-grade organizing structure only.

### D10 — Non-claim box and anti-seed register

Create `docs/scope/v0.2-non-claim-box.md` and `docs/anti-seed-ns.md`.

## Out of scope for v0.2

The following material is excluded from ns-program v0.2 and must be routed to a separate time-theory strategic direction unless later admitted through an explicit dependency pin:

- quasicrystalline temporal structure;
- plastic-number or metallic-ratio substitution dynamics;
- cut-and-project geometry as a time-foliation tool;
- almost-periodic homogenization;
- wave-archetype analysis;
- force-generator decomposition;
- Kozyrev empirical-replication program;
- time-as-physical-substance reformulations.

## Clay-direction commitment

Deferred to v0.3 or v0.4.

v0.2 produces architecture and diagnostic discipline. It does not choose smoothness-via-bulk-regularity or singularity-via-boundary-concentration as a Clay attack.

If D8 shows that one or both candidates recover Navier-Stokes exactly or through a declared known deformation, v0.3 may choose a Clay-direction workstream.

If D8 shows that neither candidate recovers Navier-Stokes or a declared known deformation, v0.3 becomes failure analysis and revised architecture.

Both outcomes advance the repository because both reduce ambiguity.

## Progress thresholds and pause conditions

Pause condition, architectural: if both Candidates C and D fail D8, pause Clay-direction framing and open a failure-analysis tranche.

Pause condition, capture: if chat-tranche ideation outruns repo capture by more than three sub-tranches, pause new tranche generation and capture first.

Continue condition: D1-D10 complete in repo, CI validates dependency pins and structural docs, capture-gap matrix updated, and anti-seed register updated for newly discovered failure modes.

## Citation form

```text
[NS-LANE-V0.2 @ <merge-sha>]
[HG-MTH-005 @ 988307215ad38ccb16514311222184a1b757752b]
[HE-INT-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]
[HE-PROJ-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]
```

Replace `<merge-sha>` after merge. Until then, v0.2 remains PR-head material.
