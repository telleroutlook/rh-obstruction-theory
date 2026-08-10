#!/usr/bin/env python3
"""Regression tests: ledger + B1 theorem scaffold integrity.

Run: python3 -m pytest tests/ -x
stdlib-only.
"""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from checker.validate_ledger import load_claims, validate  # noqa: E402


# ---- Ledger tests ----

def test_all_claims_parse_and_validate():
    claims = load_claims(ROOT / "baseline" / "CLAIM_LEDGER.yaml")
    assert len(claims) == 10, f"expected 10 claims, parsed {len(claims)}"
    for c in claims:
        assert not validate(c), f"{c.get('id')}: {validate(c)}"


def test_no_pending_gate_a_item_is_a_premise():
    """Gate A: nothing awaiting inspection may be used as an established premise."""
    for c in load_claims(ROOT / "baseline" / "CLAIM_LEDGER.yaml"):
        if c.get("gate_a_status") == "PENDING":
            assert c.get("usable_as_premise") is False, c.get("id")


def test_checker_exit_code_zero():
    r = subprocess.run([sys.executable, str(ROOT / "checker" / "validate_ledger.py")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


# ---- B1 theorem scaffold tests ----

B1_DIR = ROOT / "theorems" / "B1-finite-inequality"
B1_CONTRACT = ROOT / "domain" / "contracts" / "B1-finite-inequality.json"

REQUIRED_FILES = [
    "statement.md",
    "dependencies.yaml",
    "proof.md",
    "limitations.md",
    "novelty.md",
    "witness/README.md",
    "checker/README.md",
]


def test_b1_required_files_exist():
    """Every §12.2 artifact must be present."""
    for rel in REQUIRED_FILES:
        p = B1_DIR / rel
        assert p.exists(), f"missing B1 file: {rel}"


def test_b1_contract_exists_and_parses():
    assert B1_CONTRACT.exists(), "missing B1 domain contract"
    with B1_CONTRACT.open() as f:
        data = json.load(f)
    assert data["theorem_id"] == "B1-finite-inequality"
    assert data["metadata"]["is_barrier_claim"] is True
    assert data["metadata"]["escape_route_present"] is True


def test_b1_contract_required_metadata_keys():
    """policy-v2.json required_metadata_keys must all be present."""
    with (ROOT / "domain" / "policy-v2.json").open() as f:
        policy = json.load(f)
    required = set(policy["required_metadata_keys"])
    with B1_CONTRACT.open() as f:
        contract = json.load(f)
    meta = set(contract.get("metadata", {}).keys())
    missing = required - meta
    assert not missing, f"B1 contract missing metadata keys: {missing}"


def test_b1_no_rh_in_dependencies():
    """Gate A: B1 must not use a PENDING or CONJECTURE item as a premise."""
    with B1_CONTRACT.open() as f:
        contract = json.load(f)
    ledger_claims = {c["id"]: c for c in load_claims(ROOT / "baseline" / "CLAIM_LEDGER.yaml")}
    for dep in contract.get("dependencies", []):
        cid = dep["claim_id"]
        if cid in ledger_claims:
            c = ledger_claims[cid]
            if c.get("usable_as_premise") is False:
                assert dep.get("role", "").lower().startswith("background") or \
                       "not a premise" in dep.get("role", "").lower() or \
                       "object of study" in dep.get("role", "").lower(), \
                    f"B1 uses non-premise claim {cid} without marking it background/non-premise"


def test_b1_statement_has_escape_section():
    stmt = (B1_DIR / "statement.md").read_text()
    assert "Escape" in stmt or "escape" in stmt, \
        "statement.md must contain an escape route section"


def test_b1_limitations_has_fixed_k_warning():
    lim = (B1_DIR / "limitations.md").read_text()
    assert "fixed" in lim.lower() or "Fixed" in lim, \
        "limitations.md must warn about fixed-K restriction"
    # Must not contain forbidden overclaim phrases
    forbidden = ["proves rh", "disproves rh", "barrier for all", "all rh methods"]
    for phrase in forbidden:
        assert phrase not in lim.lower(), \
            f"limitations.md contains forbidden phrase: {phrase!r}"


def test_b1_proof_separates_analytic_from_finite():
    proof = (B1_DIR / "proof.md").read_text()
    # Proof must be marked as analytic only (no finite certificate claimed)
    assert "NONE" in proof or "analytic" in proof.lower(), \
        "proof.md should state it is analytic-only (no finite certificate)"


# ---- B2 theorem scaffold tests ----

B2_DIR = ROOT / "theorems" / "B2-exact-collision"
B2_CONTRACT = ROOT / "domain" / "contracts" / "B2-exact-collision.json"


def test_b2_required_files_exist():
    """Every §12.2 artifact must be present for B2."""
    for rel in REQUIRED_FILES:
        p = B2_DIR / rel
        assert p.exists(), f"missing B2 file: {rel}"


def test_b2_contract_exists_and_parses():
    assert B2_CONTRACT.exists(), "missing B2 domain contract"
    with B2_CONTRACT.open() as f:
        data = json.load(f)
    assert data["theorem_id"] == "B2-exact-collision"
    assert data["metadata"]["is_barrier_claim"] is True
    assert data["metadata"]["escape_route_present"] is True


def test_b2_contract_required_metadata_keys():
    with (ROOT / "domain" / "policy-v2.json").open() as f:
        policy = json.load(f)
    required = set(policy["required_metadata_keys"])
    with B2_CONTRACT.open() as f:
        contract = json.load(f)
    meta = set(contract.get("metadata", {}).keys())
    missing = required - meta
    assert not missing, f"B2 contract missing metadata keys: {missing}"


def test_b2_conditionality_stated():
    """B2 must state it is conditional on the rank step."""
    with B2_CONTRACT.open() as f:
        data = json.load(f)
    status = data.get("spec_status", "")
    assert "CONDITIONAL" in status or "conditional" in status.lower(), \
        "B2 contract must mark spec_status as conditional"
    # limitations must mention the rank / open item
    lim = (B2_DIR / "limitations.md").read_text()
    assert "rank" in lim.lower() or "conditional" in lim.lower(), \
        "B2 limitations.md must mention the rank condition"


def test_b2_proof_has_rank_section():
    proof = (B2_DIR / "proof.md").read_text()
    assert "Vandermonde" in proof or "Chebyshev" in proof or "rank" in proof.lower(), \
        "B2 proof.md must contain a rank analysis section"


def test_b2_discovery_not_in_witness():
    """discovery/ outputs must not be placed in witness/."""
    witness_dir = B2_DIR / "witness"
    for f in witness_dir.iterdir():
        content = f.read_text()
        assert "discovery" not in content.lower() or "belong" in content.lower() or \
               "discovery/" in content, \
            f"B2 witness/{f.name} may be importing discovery-tier data"


def test_discovery_jacobian_script_runnable():
    """The discovery Jacobian script must exit 0."""
    r = subprocess.run(
        [sys.executable, str(ROOT / "discovery" / "jacobian_analysis.py")],
        capture_output=True, text=True
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "FULL RANK" in r.stdout, "Jacobian analysis should report FULL RANK for test cases"


# ---- E-compactness theorem scaffold tests ----

E_DIR = ROOT / "theorems" / "E-compactness"
E_CONTRACT = ROOT / "domain" / "contracts" / "E-compactness.json"


def test_e_required_files_exist():
    """Every §12.2 artifact must be present for E-compactness."""
    for rel in REQUIRED_FILES:
        p = E_DIR / rel
        assert p.exists(), f"missing E file: {rel}"


def test_e_contract_exists_and_parses():
    assert E_CONTRACT.exists(), "missing E-compactness domain contract"
    with E_CONTRACT.open() as f:
        data = json.load(f)
    assert data["theorem_id"] == "E-compactness"
    assert data["metadata"]["is_barrier_claim"] is True
    assert data["metadata"]["escape_route_present"] is True


def test_e_contract_required_metadata_keys():
    with (ROOT / "domain" / "policy-v2.json").open() as f:
        policy = json.load(f)
    required = set(policy["required_metadata_keys"])
    with E_CONTRACT.open() as f:
        contract = json.load(f)
    meta = set(contract.get("metadata", {}).keys())
    missing = required - meta
    assert not missing, f"E contract missing metadata keys: {missing}"


def test_e_normalization_frozen_to_ccm():
    """Theorem E must freeze to CCM entire target, not Suzuki meromorphic."""
    with E_CONTRACT.open() as f:
        data = json.load(f)
    norm = data.get("normalization_choice", {}).get("selected", "")
    assert "ccm" in norm.lower(), \
        "E-compactness must be frozen to CCM entire target"
    # Suzuki target must NOT be selected
    assert "suzuki" not in norm.lower(), \
        "E-compactness must not select Suzuki meromorphic target"


def test_e_ccm_convergence_open_not_a_premise():
    """CCM-CONVERGENCE-OPEN is the object of study, never a usable premise."""
    with E_CONTRACT.open() as f:
        data = json.load(f)
    for dep in data.get("dependencies", []):
        if dep["claim_id"] == "CCM-CONVERGENCE-OPEN":
            role = dep.get("role", "").lower()
            assert "not a hypothesis" in role or "object of study" in role or \
                   "not a premise" in role, \
                "CCM-CONVERGENCE-OPEN must be labeled as object of study, not hypothesis"
            assert dep.get("usable_as_premise") is not True, \
                "CCM-CONVERGENCE-OPEN must not be usable_as_premise"


def test_e_statement_has_two_parts():
    """E-compactness statement must contain both negative and positive theorems."""
    stmt = (E_DIR / "statement.md").read_text()
    assert "E-neg" in stmt or "Negative" in stmt or "negative" in stmt, \
        "E statement must contain negative (counterexample) theorem"
    assert "E-pos" in stmt or "Positive" in stmt or "escape" in stmt.lower(), \
        "E statement must contain positive (escape) theorem"


def test_e_limitations_excludes_suzuki():
    """Limitations must explicitly exclude the Suzuki meromorphic target."""
    lim = (E_DIR / "limitations.md").read_text()
    assert "Suzuki" in lim or "meromorphic" in lim.lower(), \
        "E limitations.md must state Suzuki meromorphic target is excluded"
    assert "pole" in lim.lower() or "meromorphic" in lim.lower(), \
        "E limitations.md must mention the pole/residue issue"


def test_e_no_rh_claim():
    """Theorem E must not claim to prove RH."""
    for fname in ["statement.md", "proof.md", "limitations.md"]:
        content = (E_DIR / fname).read_text()
        forbidden = ["proves rh", "disproves rh", "rh is proved", "therefore rh"]
        for phrase in forbidden:
            assert phrase not in content.lower(), \
                f"E {fname} contains forbidden phrase: {phrase!r}"


# ---- C-euler-tail theorem scaffold tests ----

C_DIR = ROOT / "theorems" / "C-euler-tail"
C_CONTRACT = ROOT / "domain" / "contracts" / "C-euler-tail.json"


def test_c_required_files_exist():
    for rel in REQUIRED_FILES:
        assert (C_DIR / rel).exists(), f"missing C file: {rel}"


def test_c_contract_exists_and_parses():
    assert C_CONTRACT.exists()
    with C_CONTRACT.open() as f:
        data = json.load(f)
    assert data["theorem_id"] == "C-euler-tail"
    assert data["metadata"]["is_barrier_claim"] is True
    assert data["metadata"]["escape_route_present"] is True


def test_c_contract_required_metadata_keys():
    with (ROOT / "domain" / "policy-v2.json").open() as f:
        policy = json.load(f)
    required = set(policy["required_metadata_keys"])
    with C_CONTRACT.open() as f:
        contract = json.load(f)
    missing = required - set(contract.get("metadata", {}).keys())
    assert not missing, f"C contract missing metadata keys: {missing}"


def test_c_andersson_gate_a_pending():
    """Andersson dependency must be marked PENDING (Gate A not yet cleared)."""
    with C_CONTRACT.open() as f:
        data = json.load(f)
    andersson_deps = [d for d in data.get("dependencies", [])
                      if "ANDERSSON" in d["claim_id"]]
    assert andersson_deps, "C contract must list Andersson as a dependency"
    dep = andersson_deps[0]
    assert dep.get("usable_as_premise") is not True, \
        "Andersson dep must not be usable_as_premise=true until Gate A clears"


def test_c_davenport_heilbronn_kept_separate():
    """Davenport-Heilbronn must be a comparison only, not combined with C."""
    lim = (C_DIR / "limitations.md").read_text()
    assert "Davenport" in lim or "Heilbronn" in lim or "functional equation" in lim.lower(), \
        "C limitations.md must mention Davenport-Heilbronn separation"
    # The combination is explicitly forbidden
    proof = (C_DIR / "proof.md").read_text()
    assert "separate" in proof.lower() or "Davenport" in proof or "§8.C.2" in proof, \
        "C proof.md must keep Davenport-Heilbronn logically separate"


# ---- D-spectral-asymptotic theorem scaffold tests ----

D_DIR = ROOT / "theorems" / "D-spectral-asymptotic"
D_CONTRACT = ROOT / "domain" / "contracts" / "D-spectral-asymptotic.json"


def test_d_required_files_exist():
    for rel in REQUIRED_FILES:
        assert (D_DIR / rel).exists(), f"missing D file: {rel}"


def test_d_contract_exists_and_parses():
    assert D_CONTRACT.exists()
    with D_CONTRACT.open() as f:
        data = json.load(f)
    assert data["theorem_id"] == "D-spectral-asymptotic"
    assert data["metadata"]["is_barrier_claim"] is True
    assert data["metadata"]["escape_route_present"] is True


def test_d_contract_required_metadata_keys():
    with (ROOT / "domain" / "policy-v2.json").open() as f:
        policy = json.load(f)
    required = set(policy["required_metadata_keys"])
    with D_CONTRACT.open() as f:
        contract = json.load(f)
    missing = required - set(contract.get("metadata", {}).keys())
    assert not missing, f"D contract missing metadata keys: {missing}"


def test_d_novelty_gate_stated():
    """D must state novelty gate is OPEN and not overclaim Paper B."""
    nov = (D_DIR / "novelty.md").read_text()
    assert "Endres" in nov or "Steiner" in nov, \
        "D novelty.md must reference Endres-Steiner prior art"
    assert "THIN" in nov or "thin" in nov.lower() or "not yet cleared" in nov.lower(), \
        "D novelty.md must state THIN / novelty gate not cleared"


def test_d_escape_example_present():
    """D must include an explicit escape example with T log T counting."""
    stmt = (D_DIR / "statement.md").read_text()
    assert "hyperbolic" in stmt.lower() or "Selberg" in stmt or "T log T" in stmt, \
        "D statement.md must give an explicit T log T escape example"


def test_d_no_rh_claim():
    for fname in ["statement.md", "proof.md", "limitations.md"]:
        content = (D_DIR / fname).read_text()
        forbidden = ["proves rh", "disproves rh", "rh is proved"]
        for phrase in forbidden:
            assert phrase not in content.lower(), \
                f"D {fname} contains forbidden phrase: {phrase!r}"


if __name__ == "__main__":
    test_all_claims_parse_and_validate()
    test_no_pending_gate_a_item_is_a_premise()
    test_checker_exit_code_zero()
    test_b1_required_files_exist()
    test_b1_contract_exists_and_parses()
    test_b1_contract_required_metadata_keys()
    test_b1_no_rh_in_dependencies()
    test_b1_statement_has_escape_section()
    test_b1_limitations_has_fixed_k_warning()
    test_b1_proof_separates_analytic_from_finite()
    test_b2_required_files_exist()
    test_b2_contract_exists_and_parses()
    test_b2_contract_required_metadata_keys()
    test_b2_conditionality_stated()
    test_b2_proof_has_rank_section()
    test_b2_discovery_not_in_witness()
    test_discovery_jacobian_script_runnable()
    test_e_required_files_exist()
    test_e_contract_exists_and_parses()
    test_e_contract_required_metadata_keys()
    test_e_normalization_frozen_to_ccm()
    test_e_ccm_convergence_open_not_a_premise()
    test_e_statement_has_two_parts()
    test_e_limitations_excludes_suzuki()
    test_e_no_rh_claim()
    test_c_required_files_exist()
    test_c_contract_exists_and_parses()
    test_c_contract_required_metadata_keys()
    test_c_andersson_gate_a_pending()
    test_c_davenport_heilbronn_kept_separate()
    test_d_required_files_exist()
    test_d_contract_exists_and_parses()
    test_d_contract_required_metadata_keys()
    test_d_novelty_gate_stated()
    test_d_escape_example_present()
    test_d_no_rh_claim()
    print("ok")
