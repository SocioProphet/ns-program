# Capture Gap Matrix — v0.2

Version: v0.2  
Claim grade: C0 capture / repo-provenance control  
Dependencies pinned: `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b`; `SocioProphet/Heller-Einstein @ 8fa5a804bd5cf7e9e37be6477db52ff33e070350`  
Non-claim summary: capture status records repository coverage of the v0.2 directive. It does not promote any Navier-Stokes theorem, diagnostic result, or Clay-direction claim.

## Purpose

This matrix records how the v0.2 strategic-direction directive is captured in the repository.

The matrix prevents chat-tranche work from outrunning repo capture and gives future agents a direct map from directive item to committed file path.

## D1-D10 capture map

| Directive | Required work | Repo capture | Status |
|---|---|---|---|
| D1 | Spec extension to v0.2 | `docs/program-spec/navier-stokes-program-v0_2.md` | captured |
| D2 | Add Heller-Einstein dependency pin and validate dual upstream | `DEPENDENCIES.md`; `.github/workflows/ns-program-pfk-dependency.yml`; `tests/test_pfk_dependency.py` | captured / CI wired |
| D3 | Citation discipline document | `docs/scope/ns-program-bridge-citation.md` | captured |
| D4 | 2D Navier-Stokes anchor | `docs/foundations/2d-ns-anchor.md` | captured |
| D5 | Workstream A foundational typing | `docs/workstream-a/README.md` | captured |
| D6 | Workstream B Candidate C development | `docs/workstream-b/README.md`; `docs/workstream-b/literature/bhmr-2008-and-extensions.md`; `docs/workstream-b/candidate-c-bulk-equation.md`; `docs/workstream-b/candidate-c-projection.md` | captured |
| D7 | Workstream C Candidate D development | `docs/workstream-c/README.md`; `docs/workstream-c/he-phys-001-as-bulk.md`; `docs/workstream-c/he-int-001-projection.md` | captured |
| D8 | Workstream D diagnostic question | `docs/workstream-d/README.md` | captured |
| D9 | C/D conjectured correspondence | `docs/correspondence/c-d-conjectured-correspondence.md` | captured |
| D10 | Non-claim box and obstruction / anti-seed register | `docs/scope/v0.2-non-claim-box.md`; `docs/anti-seed-ns.md` | captured |

## Intentional additions beyond specified paths

| Addition | Path | Reason | Claim grade |
|---|---|---|---|
| Top-level status update | `README.md` | make v0.2 status discoverable from repository root | C0 |
| Trust-surface declaration | `TRUST_SURFACE.yaml` | required by directive for any future executable D8 work; declares current tranche document-only | C0 |
| Structural validation tests | `tests/test_pfk_dependency.py` | enforce pins, required docs, claim-boundary text, and no silent downgrade of v0.2 guardrails | C0 validation |
| CI workflow update | `.github/workflows/ns-program-pfk-dependency.yml` | validate Heller-Godel and Heller-Einstein pins in pull requests and pushes | C0 validation |
| Capture-gap matrix | `docs/capture/capture-gap-matrix.md` | record repo capture and deviations explicitly | C0 |

## Corrections made during capture

### Candidate C dimensional correction

The directive proposed `AdS_4 / fluid_3`. During repo capture this was refined into a mandatory dimension-matching diagnostic: under standard `AdS_{d+1}` notation, `d` counts boundary spacetime dimensions, so `AdS_4` ordinarily gives a 2+1-dimensional boundary spacetime rather than the 3+1 spacetime accounting of the Clay three-spatial-dimensional target.

The repo does not discard the 4D-bulk direction. It requires Candidate C to explain an envelope construction, switch dimensions, classify a known deformation, or fail the diagnostic.

### Candidate D upstream-status correction

The directive named `HE-PHYS-001` as a Candidate D bulk source. At the pinned Heller-Einstein commit, interface/projection vocabulary is available for citation, while physical-core `HE-PHYS-*` work is treated as reserved/future unless canonical file-level evidence is present.

The repo therefore marks `HE-PHYS-001` as reserved/unimplemented at the current pin and uses `not-configured` as the Candidate D status when no canonical bulk equation exists.

## Capture pause condition

If future chat work introduces more than three uncaptured sub-tranches, pause ideation and update this matrix before creating new mathematical content.

## Current v0.2 capture status

All D1-D10 items are captured in repository files. The next valid step is review / CI validation, not additional architecture expansion.
