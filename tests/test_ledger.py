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
    print("ok")
