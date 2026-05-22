# Dependencies

## Upstream

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `988307215ad38ccb16514311222184a1b757752b` | Framework objects (`HG-*`) from `docs/framework-core/`; PFK operational substrate from `proof_fabric_kernel/` |
| `SocioProphet/Heller-Einstein` | `8fa5a804bd5cf7e9e37be6477db52ff33e070350` | Interface ontology (`HE-INT-*`) and projection-induced-stochasticity apparatus (`HE-PROJ-*`) from the Heller-Einstein scaffold; conservative physical core only where explicitly canonicalized at the pinned commit |

`ns-program` is now a dual-upstream consumer: Heller-Godel for PFK, claim grammar, and framework vocabulary; Heller-Einstein for interface/projection vocabulary required by the v0.2 Candidate D diagnostic.

Heller-Dirac is not yet a dependency of `ns-program`. When the program enters spectral, semigroup, or Hopf-scaffold territory, a follow-up PR may add `SocioProphet/Heller-Dirac` as another upstream pin.

## Cited objects

### Framework-grade (HG-*)

| Identifier | Role | Notes |
|---|---|---|
| `HG-FND-*` | Foundational vocabulary | typing for workstreams A-D |
| `HG-MTH-005` | Universal Bridge formal specification | method-grade conceptual scaffold; no proof transfer |
| `HG-MTH-010` | Clay-coverage taxonomy | reserved upstream; not yet drafted |

### PFK operational substrate

| Identifier | Role | ns-program use |
|---|---|---|
| `PFK-OP-001` | Event ingestion | future workstream receipt emission |
| `PFK-OP-030` | Calibration operator | numerical-baseline checks for analytic-PDE benchmarks |

### PFK schemas

| Identifier | Canonical path | Use |
|---|---|---|
| `PFK-SCHEMA-001` | `proof_fabric_kernel/schemas/claim_ledger_row.schema.json` | future workstream claim ledgers |
| `PFK-SCHEMA-002` | `proof_fabric_kernel/schemas/event_ir.schema.json` | operator invocation receipts |
| `PFK-SCHEMA-003` | `proof_fabric_kernel/schemas/proof_artifact.schema.json` | proof-step envelopes |
| `PFK-SCHEMA-004` | `proof_fabric_kernel/schemas/calibration_bundle.schema.json` | analytical-PDE numerical baselines |

### Heller-Einstein interface / projection surface

| Identifier | Role | ns-program use |
|---|---|---|
| `HE-INT-*` | typed interface ontology and access-chain vocabulary | Candidate D observer trace and envelope typing |
| `HE-INT-001` | active formal interface ontology specification | Candidate D typed access chain; citation permitted only if present/canonical at the pinned commit |
| `HE-PROJ-*` | projection-induced stochasticity namespace | Candidate D projection discipline and anti-confusion boundary |
| `HE-PROJ-001` | projection-induced-stochasticity theorem/surface | cited only as Heller-Einstein imported apparatus; does not become deterministic Navier-Stokes solution map |
| `HE-PHYS-*` | conservative physical core namespace | reserved/future unless a pinned canonical document is present |
| `HE-PHYS-001` | conservative Einstein-Cartan-Dirac action candidate | reserved/unimplemented at this pin unless separately proven by file-level citation |

### PFK anti-seed

| Identifier | Applies because |
|---|---|
| `A-PFK-OP-001` | operator invocation is not evidence |
| `A-PFK-PROTOCOL-001` | null passage is not theorem-grade |
| `A-PFK-PROTOCOL-002` | window-shopping prevention |
| `A-PFK-SCHEMA-001` | schema validity is not content validity |
| `A-PFK-SCHEMA-002` | schema-version drift; pin is not floating |
| `A-PFK-VAL-001` | validator green is not audit completion |

### Framework anti-seed

| Identifier | Applies because |
|---|---|
| `A-MTH-001` | Universal Bridge does not transfer proofs |
| `A-MTH-003` | Catalan / mu2 fixture is not Clay progress |

### Heller-Einstein anti-seed boundary

| Boundary | Applies because |
|---|---|
| projection-is-not-deterministic-solution | A many-to-one observer trace must not be confused with a deterministic Navier-Stokes solution operator |
| interface-vocabulary-is-not-equation-recovery | typed access-chain vocabulary does not prove that a boundary/envelope equation recovers Navier-Stokes |
| reserved-physical-core-is-not-citable-content | `HE-PHYS-001` cannot be treated as canonical until present at a pinned commit |

## Forbidden edges

- `ns-program` -> any other Clay-program repo.
- `ns-program` -> Heller-Godel-other-than-pinned-commit.
- `ns-program` -> Heller-Einstein-other-than-pinned-commit.
- `ns-program` -> analytic-regularity methodology from RH, Hodge, Yang-Mills, P vs NP, or BSD except through `HG-MTH-005` as method-grade analogy.
- `ns-program` -> time-theory material unless and until a separate time-theory repository exists and is pinned.

## Citation form

```text
[HG-MTH-005 @ 988307215ad38ccb16514311222184a1b757752b]
[HG-MTH-010 @ 988307215ad38ccb16514311222184a1b757752b]  # reserved
[PFK-SCHEMA-001 @ 988307215ad38ccb16514311222184a1b757752b]
[A-MTH-001 @ 988307215ad38ccb16514311222184a1b757752b]
[HE-INT-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]
[HE-PROJ-* @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350]
```

## Schema-version pinning policy

Per `A-PFK-SCHEMA-002`, upstream pins are not floating.
