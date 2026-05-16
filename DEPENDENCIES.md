# Dependencies

## Upstream

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `988307215ad38ccb16514311222184a1b757752b` | Framework objects (`HG-*`) from `docs/framework-core/`; PFK operational substrate from `proof_fabric_kernel/` |

Heller-Dirac is not yet a dependency of `ns-program`. When the program enters spectral, semigroup, or Hopf-scaffold territory, a follow-up PR may add `SocioProphet/Heller-Dirac` as a second upstream pin.

## Cited objects

### Framework-grade (HG-*)

| Identifier | Role | Notes |
|---|---|---|
| `HG-FND-*` | Foundational vocabulary | typing for workstreams A-F |
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

## Forbidden edges

- `ns-program` -> any other Clay-program repo.
- `ns-program` -> Heller-Godel-other-than-pinned-commit.
- `ns-program` -> analytic-regularity methodology from RH, Hodge, Yang-Mills, P vs NP, or BSD except through `HG-MTH-005` as method-grade analogy.

## Citation form

```text
[HG-MTH-005 @ 988307215ad38ccb16514311222184a1b757752b]
[HG-MTH-010 @ 988307215ad38ccb16514311222184a1b757752b]  # reserved
[PFK-SCHEMA-001 @ 988307215ad38ccb16514311222184a1b757752b]
[A-MTH-001 @ 988307215ad38ccb16514311222184a1b757752b]
```

## Schema-version pinning policy

Per `A-PFK-SCHEMA-002`, the Heller-Godel pin is not floating.
