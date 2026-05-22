# Candidate D — HE-PHYS-001 as Bulk Candidate

Version: v0.2  
Claim grade: C0 evaluation scaffold; no theorem claim  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: this document does not assert that `HE-PHYS-001` exists as canonical upstream content at the pinned commit, nor that any Heller-Einstein physical-core action recovers Navier-Stokes.

## Purpose

This document records how Candidate D would evaluate a Heller-Einstein physical-core equation as `E_bulk` for the v0.2 diagnostic.

## Current upstream status

At the pinned Heller-Einstein commit, the repository-level README identifies the conservative Einstein-Cartan-Dirac physical core as part of the Heller-Einstein purpose and lists `HE-PHYS-*` as a namespace, while subsequent-status language says physical-action apparatus / `HE-PHYS-*` drafting remains future work.

Therefore, in `ns-program` v0.2:

- `HE-PHYS-*` may be named as a reserved Candidate D target;
- `HE-PHYS-001` may not be treated as canonical imported content unless a file-level citation at the pinned commit proves it;
- the diagnostic status for Candidate D may be `not-configured` if the physical-core equation is unavailable.

## Candidate physical-core requirements

Before any Heller-Einstein physical core can serve as `E_bulk`, the following must be specified:

| Requirement | Description | Status at v0.2 pin |
|---|---|---|
| action functional | bulk action with fields and coupling constants | reserved / not assumed |
| field equations | Euler-Lagrange equations or equivalent bulk equations | reserved / not assumed |
| scalar projection field | definition and coupling role | reserved / not assumed |
| pseudoscalar coherence field | definition and coupling role | reserved / not assumed |
| boundary/interface term | observer-interface boundary contribution | reserved / not assumed |
| admissible boundary data | data on `Sigma` used for fluid recovery | not configured |
| gauge / frame choices | choices required to compare to fluid variables | not configured |
| projection map | `pi_D` or `tau` from bulk/interface data to `v,p` | not configured |

## Candidate D equation slot

Until canonical upstream content exists, Candidate D should use a slot notation rather than an asserted equation:

```text
E_bulk^D := <Heller-Einstein physical-core equation at pinned commit>
```

If no canonical physical-core equation is available, the diagnostic outcome is:

```text
Candidate D status: not-configured
Reason: physical-core bulk equation unavailable at pinned upstream commit
```

## Required non-claim

Any use of this document must include the following boundary:

> A reserved physical-core namespace is not an implemented bulk equation. Candidate D remains C0 until canonical upstream content and a declared projection map exist.

## D8 handoff

D8 may evaluate Candidate D only if it has:

1. a canonical `E_bulk^D`;
2. a declared boundary/envelope `Sigma`;
3. a declared typed access chain `tau`;
4. a declared projection `pi_D` to `v,p`;
5. a target equation comparison.

If any item is missing, D8 records `not-configured`, not success or failure.
