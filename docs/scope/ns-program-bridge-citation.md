# ns-program Bridge Citation Discipline

Version: v0.2  
Claim grade: C0 citation-governance document  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: citation permission is not proof transfer; upstream framework vocabulary does not establish Navier-Stokes regularity, boundary recovery, or Candidate C/D equivalence.

## Purpose

This document controls how `ns-program` cites Heller-Godel and Heller-Einstein in the v0.2 4D-bulk / boundary-envelope tranche.

The document is modeled on the portfolio bridge-citation pattern used by other Clay-program repos: every upstream citation is pinned, grade-limited, and paired with explicit non-claim language.

## Allowed upstream citation surfaces

| Upstream | Pinned commit | Allowed surface | v0.2 claim grade |
|---|---:|---|---|
| `SocioProphet/Heller-Godel` | `988307215ad38ccb16514311222184a1b757752b` | PFK schemas, claim grammar, framework vocabulary, Universal Bridge method analogy | C0, with imported schema semantics only |
| `SocioProphet/Heller-Einstein` | `8fa5a804bd5cf7e9e37be6477db52ff33e070350` | `HE-INT-*` typed interface vocabulary; `HE-PROJ-*` projection-induced-stochasticity vocabulary | C0 for typing; imported C3 only if the upstream file is canonical at the pin |

## Heller-Godel citation rules

Heller-Godel may be cited for:

- claim-grade discipline;
- PFK schema and receipt vocabulary;
- anti-seed vocabulary;
- Universal Bridge as method-grade analogy only;
- downstream citation-form discipline.

Heller-Godel may not be cited as:

- a Navier-Stokes proof;
- a new regularity criterion;
- a transfer mechanism from any other Clay problem;
- evidence that a 4D-bulk equation projects to 3D Navier-Stokes.

## Heller-Einstein citation rules

Heller-Einstein may be cited for:

- interface ontology and typed access-chain vocabulary;
- observer-relative trace vocabulary;
- projection-induced-stochasticity vocabulary;
- Candidate D diagnostic setup.

Heller-Einstein may not be cited as:

- a deterministic Navier-Stokes solution operator;
- proof that a latent bulk equation recovers Navier-Stokes;
- proof that a many-to-one trace preserves smoothness, regularity, or uniqueness;
- evidence for Candidate C/D equivalence;
- canonical `HE-PHYS-001` content unless a pinned file at the cited commit provides it.

## Identifier table

| Identifier | Status in v0.2 | Citation posture |
|---|---|---|
| `HG-FND-*` | permitted | C0 foundational vocabulary only |
| `HG-MTH-005` | permitted | C0 method analogy; no proof transfer |
| `HG-MTH-010` | reserved | cite only as reserved/upstream taxonomy if present |
| `PFK-SCHEMA-*` | permitted | schema and receipt vocabulary only |
| `A-MTH-*` | permitted | anti-seed boundaries |
| `A-PFK-*` | permitted | operational and validation anti-seed boundaries |
| `HE-INT-*` | permitted | interface-typing vocabulary |
| `HE-INT-001` | permitted if canonical at pin | typed access-chain specification |
| `HE-PROJ-*` | permitted | projection discipline; not deterministic NS recovery |
| `HE-PROJ-001` | permitted if canonical at pin | imported projection-induced-stochasticity result; no NS transfer |
| `HE-PHYS-*` | reserved | future physical-core namespace |
| `HE-PHYS-001` | reserved/unimplemented at current pin unless proven by file-level citation | may be discussed as Candidate D target, not cited as completed upstream content |

## Required citation form

```text
[HG-MTH-005 @ 988307215ad38ccb16514311222184a1b757752b]
[PFK-SCHEMA-001 @ 988307215ad38ccb16514311222184a1b757752b]
[A-PFK-SCHEMA-002 @ 988307215ad38ccb16514311222184a1b757752b]
[HE-INT-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]
[HE-PROJ-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]
```

## Promotion-by-prose guard

Bridge citations do not promote claims.

Any sentence that cites upstream framework vocabulary and then states or implies `therefore Navier-Stokes regularity`, `therefore smoothness`, `therefore no blow-up`, `therefore C/D equivalence`, or `therefore Clay progress` violates this document.

## Required non-claim text

Documents using bridge citations must include a local non-claim statement equivalent to:

> This citation supplies upstream vocabulary only. It does not transfer proof content into `ns-program`, does not establish Navier-Stokes regularity, and does not establish that any bulk projection recovers the 3D Navier-Stokes equations.

## Review checklist

Before merging any v0.2 document with upstream citations, verify:

- all upstream references include pinned commit SHAs;
- the cited identifier exists or is explicitly marked reserved;
- Heller-Einstein physical-core language distinguishes reserved target from canonical upstream content;
- Candidate C fluid-gravity citations do not skip the dimension-matching diagnostic;
- no bridge citation is used as theorem evidence.
