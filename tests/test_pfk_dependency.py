from pathlib import Path
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]
HG_PIN = "988307215ad38ccb16514311222184a1b757752b"
HE_PIN = "8fa5a804bd5cf7e9e37be6477db52ff33e070350"

REQUIRED_PFK_PATHS = [
    "proof_fabric_kernel/docs/OperatorCatalog_PrimePolicyOperators_v1.md",
    "proof_fabric_kernel/docs/SchemaCatalog_v1.md",
    "proof_fabric_kernel/docs/anti-seed-pfk.md",
    "proof_fabric_kernel/schemas/claim_ledger_row.schema.json",
    "proof_fabric_kernel/schemas/event_ir.schema.json",
    "proof_fabric_kernel/schemas/proof_artifact.schema.json",
    "proof_fabric_kernel/schemas/calibration_bundle.schema.json",
]

CANONICAL_SCHEMA_NAMES = {
    "claim_ledger_row.schema.json",
    "event_ir.schema.json",
    "proof_artifact.schema.json",
    "calibration_bundle.schema.json",
}

REQUIRED_V02_DOCS = [
    "docs/program-spec/navier-stokes-program-v0_2.md",
    "docs/scope/ns-program-bridge-citation.md",
    "docs/scope/v0.2-non-claim-box.md",
    "docs/foundations/2d-ns-anchor.md",
    "docs/workstream-a/README.md",
    "docs/workstream-b/README.md",
    "docs/workstream-b/literature/bhmr-2008-and-extensions.md",
    "docs/workstream-b/candidate-c-bulk-equation.md",
    "docs/workstream-b/candidate-c-projection.md",
    "docs/workstream-c/README.md",
    "docs/workstream-c/he-phys-001-as-bulk.md",
    "docs/workstream-c/he-int-001-projection.md",
    "docs/workstream-d/README.md",
    "docs/correspondence/c-d-conjectured-correspondence.md",
    "docs/anti-seed-ns.md",
    "docs/capture/capture-gap-matrix.md",
]


class TestPFKDependency(unittest.TestCase):
    def test_dependencies_file_exists_and_pins_commits(self) -> None:
        path = ROOT / "DEPENDENCIES.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn(HG_PIN, text)
        self.assertIn(HE_PIN, text)
        self.assertIn("HG-MTH-005", text)
        self.assertIn("PFK-SCHEMA-001", text)
        self.assertIn("A-PFK-OP-001", text)
        self.assertIn("HE-INT-*", text)
        self.assertIn("HE-PROJ-*", text)
        self.assertIn("HE-PHYS-001", text)
        self.assertIn("reserved/unimplemented", text)

    def test_no_local_canonical_schema_shadowing(self) -> None:
        local_schemas = ROOT / "schemas"
        if not local_schemas.exists():
            return
        local_names = {path.name for path in local_schemas.rglob("*.json")}
        shadowed = sorted(local_names & CANONICAL_SCHEMA_NAMES)
        self.assertFalse(shadowed, f"local schemas shadow canonical PFK schemas: {shadowed}")

    def test_canonical_pfk_paths_resolve_when_available(self) -> None:
        hg_root_value = os.environ.get("HELLER_GODEL_ROOT")
        if not hg_root_value:
            self.skipTest("HELLER_GODEL_ROOT not set; dependency-resolution check runs in dedicated workflow")
        hg_root = Path(hg_root_value)
        missing = [path for path in REQUIRED_PFK_PATHS if not (hg_root / path).exists()]
        self.assertFalse(missing, f"Missing canonical Heller-Godel PFK paths: {missing}")

    def test_heller_einstein_pin_resolves_when_available(self) -> None:
        he_root_value = os.environ.get("HELLER_EINSTEIN_ROOT")
        if not he_root_value:
            self.skipTest("HELLER_EINSTEIN_ROOT not set; dependency-resolution check runs in dedicated workflow")
        he_root = Path(he_root_value)
        readme = he_root / "README.md"
        self.assertTrue(readme.exists(), "Missing Heller-Einstein README at pinned checkout")
        text = readme.read_text(encoding="utf-8")
        self.assertIn("Heller-Einstein", text)
        self.assertIn("HE-INT", text)
        self.assertIn("HE-PROJ", text)

    def test_v02_required_documents_exist_and_have_headers(self) -> None:
        missing = [path for path in REQUIRED_V02_DOCS if not (ROOT / path).exists()]
        self.assertFalse(missing, f"Missing v0.2 docs: {missing}")
        for rel in REQUIRED_V02_DOCS:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn("Version: v0.2", text, rel)
            self.assertIn("Claim grade:", text, rel)
            self.assertIn("Non-claim summary:", text, rel)
            self.assertIn(HG_PIN, text, rel)

    def test_candidate_c_dimension_guard_is_present(self) -> None:
        paths = [
            ROOT / "docs/program-spec/navier-stokes-program-v0_2.md",
            ROOT / "docs/workstream-b/README.md",
            ROOT / "docs/workstream-b/candidate-c-bulk-equation.md",
            ROOT / "docs/anti-seed-ns.md",
        ]
        joined = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        self.assertIn("AdS_4", joined)
        self.assertIn("2+1", joined)
        self.assertIn("3+1", joined)
        self.assertIn("dimension", joined.lower())
        self.assertIn("Clay", joined)

    def test_candidate_d_reserved_physical_core_guard_is_present(self) -> None:
        paths = [
            ROOT / "DEPENDENCIES.md",
            ROOT / "docs/workstream-c/README.md",
            ROOT / "docs/workstream-c/he-phys-001-as-bulk.md",
            ROOT / "docs/workstream-d/README.md",
            ROOT / "docs/anti-seed-ns.md",
        ]
        joined = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        self.assertIn("HE-PHYS-001", joined)
        self.assertIn("reserved", joined)
        self.assertIn("not-configured", joined)
        self.assertIn("canonical", joined)

    def test_non_claim_box_blocks_clay_direction_and_equivalence(self) -> None:
        text = (ROOT / "docs/scope/v0.2-non-claim-box.md").read_text(encoding="utf-8")
        required = [
            "No Clay-direction commitment",
            "No Navier-Stokes regularity theorem",
            "No claim is made that Candidate C recovers Navier-Stokes",
            "No claim is made that Candidate D recovers Navier-Stokes",
            "No claim is made that Candidates C and D are equivalent",
            "time-theory",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

    def test_trust_surface_declares_no_live_or_destructive_behavior(self) -> None:
        text = (ROOT / "TRUST_SURFACE.yaml").read_text(encoding="utf-8")
        required = [
            "document_only: true",
            "executable_diagnostics_present: false",
            "live_target_actions: false",
            "network_access: false",
            "credential_access: false",
            "payload_delivery: false",
            "destructive_behavior: false",
            "no_clay_direction_commitment: true",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

    def test_capture_gap_matrix_captures_all_directives(self) -> None:
        text = (ROOT / "docs/capture/capture-gap-matrix.md").read_text(encoding="utf-8")
        for item in [f"D{i}" for i in range(1, 11)]:
            self.assertIn(item, text)
        self.assertIn("All D1-D10 items are captured", text)
        self.assertIn("Intentional additions", text)

    def test_program_spec_exists(self) -> None:
        spec_path = ROOT / "docs" / "program-spec" / "navier-stokes-program-v0_1.md"
        self.assertTrue(spec_path.exists())
        content = spec_path.read_text(encoding="utf-8")
        for letter in "ABCDEF":
            self.assertIn(f"Workstream {letter}", content)
        self.assertIn("Clay proximity", content)
        self.assertIn("0%", content)


if __name__ == "__main__":
    unittest.main()
