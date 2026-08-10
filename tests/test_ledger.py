#!/usr/bin/env python3
"""Regression: the ledger checker parses all claims and they satisfy the derived rules.

Run: python3 -m pytest tests/ -x   (or: python3 tests/test_ledger.py)
stdlib-only.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from checker.validate_ledger import load_claims, validate  # noqa: E402


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


if __name__ == "__main__":
    test_all_claims_parse_and_validate()
    test_no_pending_gate_a_item_is_a_premise()
    test_checker_exit_code_zero()
    print("ok")
