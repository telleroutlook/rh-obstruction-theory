#!/usr/bin/env python3
"""Regression tests for the corrected OE-02 quartic normalization."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CHECKER = (
    ROOT
    / "theorems"
    / "M-row3-square-powerful-complete"
    / "checker"
    / "verify_OE02_quartic_map.py"
)


def _load() -> Any:
    spec = importlib.util.spec_from_file_location("theorem_m_quartic_map", CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import quartic map checker")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_checker_replays_exact_map() -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKER)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "PASS: OE-02 corrected 5-conic and quartic map replay" in result.stdout


def test_correct_conic_sign_is_used() -> None:
    module = _load()
    assert module.conic_parameterization()
    assert module.quartic_derivation()


def test_forward_and_inverse_polynomial_identities() -> None:
    module = _load()
    assert module.forward_map_identity()
    assert module.inverse_map_identity()
    assert len(module.torsion_pullback_toys()) == 4


def test_individual_square_counterexample_is_exact() -> None:
    module = _load()
    a, n, plus, minus = module.individual_square_counterexample()
    assert (a, n, plus, minus) == (15, 8, 289, 113)
    assert plus == 17**2


def test_statement_and_proof_use_correct_scope_and_sign() -> None:
    theorem_dir = CHECKER.parents[1]
    statement = (theorem_dir / "statement.md").read_text(encoding="utf-8")
    proof = (theorem_dir / "proof.md").read_text(encoding="utf-8")
    assert "cannot both be of the form" in statement
    assert "forces e even" not in statement
    assert "(a,n)=(15,8)" in statement
    assert "x²+1 = 5r²" in proof
    assert "x²-2x+2 = 5s²" in proof
    assert "Y² = 10t⁴-20t³+24t²-12t+2" in proof
    assert "Y² = t⁴-4t³+6t²+4t+1" not in proof


def test_external_oe02_verdict_is_retracted_as_written() -> None:
    verdict = (
        ROOT
        / "outsource"
        / "solutions"
        / "OE-02-5square-verdict.md"
    ).read_text(encoding="utf-8")
    assert "not accepted as written" in verdict
    assert "x²+1=5r²" in verdict
    assert "Y²=10t⁴-20t³+24t²-12t+2" in verdict
