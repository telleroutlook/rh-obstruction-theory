#!/usr/bin/env python3
"""Exact replay and mutation tests for Theorem I."""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

import pytest


ROOT = Path(__file__).resolve().parents[1]
THEOREM_DIR = ROOT / "theorems" / "I-gaussian-weil-no-collision"
WITNESS_PATH = THEOREM_DIR / "witness" / "gaussian_hermite_witness_v1.json"
CHECKER_PATH = THEOREM_DIR / "checker" / "gaussian_instance_check.py"


def _load_checker() -> Any:
    spec = importlib.util.spec_from_file_location("theorem_i_checker", CHECKER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import Theorem I checker")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _witness() -> dict[str, Any]:
    return json.loads(WITNESS_PATH.read_text(encoding="utf-8"))


def _reject(mutate: Callable[[dict[str, Any]], None]) -> None:
    data = _witness()
    mutate(data)
    module = _load_checker()
    with pytest.raises(module.WitnessError):
        module.verify_witness(data)


def test_exact_quadratic_instance_passes() -> None:
    module = _load_checker()
    checks = module.verify_path(WITNESS_PATH)
    assert checks == [
        "online polynomial nonvanishing",
        "even polynomial membership",
        "distinct algebraic exponents",
        "on-line pair collapse",
        "off-line quartet collapse",
    ]


def test_cli_replays_default_witness() -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKER_PATH)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "PASS: exact Theorem I finite-witness replay" in result.stdout


def test_schema_version_is_pinned() -> None:
    _reject(lambda data: data.__setitem__("schema_version", 2))


def test_theorem_id_is_pinned() -> None:
    _reject(lambda data: data.__setitem__("theorem_id", "wrong-theorem"))


def test_field_radical_is_squarefree() -> None:
    _reject(lambda data: data["field"].__setitem__("squarefree_radical", 4))


def test_a_must_be_positive() -> None:
    _reject(lambda data: data.__setitem__("a", "0"))


def test_online_height_must_be_nonzero() -> None:
    _reject(lambda data: data["online_heights"][0].__setitem__("sqrt_coefficient", "0"))


def test_online_height_squares_must_be_distinct() -> None:
    def mutate(data: dict[str, Any]) -> None:
        data["online_heights"][2] = {
            "rational": "0",
            "sqrt_coefficient": "1",
        }

    _reject(mutate)


def test_polynomial_must_not_annihilate_online_height() -> None:
    # H_4(sqrt(2)) = 32 - 96 + 64 = 0.
    _reject(lambda data: data["polynomial"]["coefficients"][0].__setitem__(
        "coefficient", "32"
    ))


def test_polynomial_must_be_even() -> None:
    def mutate(data: dict[str, Any]) -> None:
        data["polynomial"]["coefficients"].append(
            {"degree": 1, "coefficient": "1"}
        )

    _reject(mutate)


def test_zero_polynomial_is_rejected() -> None:
    def mutate(data: dict[str, Any]) -> None:
        for entry in data["polynomial"]["coefficients"]:
            entry["coefficient"] = "0"

    _reject(mutate)


def test_offline_delta_must_be_nonzero() -> None:
    _reject(lambda data: data["quartets"][0].__setitem__("delta", "0"))


def test_offline_g_must_be_positive() -> None:
    _reject(lambda data: data["quartets"][0].__setitem__(
        "g", {"rational": "0", "sqrt_coefficient": "0"}
    ))


def test_duplicate_offline_exponents_are_rejected() -> None:
    def mutate(data: dict[str, Any]) -> None:
        data["quartets"].append(copy.deepcopy(data["quartets"][0]))

    _reject(mutate)


def test_unknown_witness_property_is_rejected() -> None:
    _reject(lambda data: data.__setitem__("producer_summary", "PASS"))


def test_float_inputs_are_rejected() -> None:
    _reject(lambda data: data.__setitem__("a", 0.01))


def test_cli_rejects_mutated_witness(tmp_path: Path) -> None:
    data = _witness()
    data["online_heights"][0] = "0"
    path = tmp_path / "mutated.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(CHECKER_PATH), str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1, result.stdout + result.stderr
    assert "FAIL: every online height must be nonzero" in result.stdout
