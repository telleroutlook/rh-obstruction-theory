#!/usr/bin/env python3
"""Tests for the independent OE-02 PARI/GP replay."""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[1]
THEOREM_DIR = ROOT / "theorems" / "M-row3-square-powerful-complete"
CHECKER_PATH = THEOREM_DIR / "checker" / "verify_OE02_pari_replay.py"
SCRIPT_PATH = THEOREM_DIR / "witness" / "oe02_pari_replay_v1.gp"
TRANSCRIPT_PATH = THEOREM_DIR / "witness" / "oe02_pari_replay_v1.txt"


def _load_checker() -> Any:
    spec = importlib.util.spec_from_file_location("theorem_m_pari_replay", CHECKER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import Theorem M PARI replay checker")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _transcript() -> str:
    return TRANSCRIPT_PATH.read_text(encoding="utf-8")


def _reject_transcript(text: str) -> None:
    module = _load_checker()
    with pytest.raises(ValueError):
        module._parse_transcript(text)


def test_pinned_offline_replay_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKER_PATH)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "PASS: certified rank bounds 0 <= rank <= 0" in result.stdout


@pytest.mark.skipif(shutil.which("gp") is None, reason="PARI/GP is not installed")
def test_live_pari_replay_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKER_PATH), "--run"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "PASS: OE-02 independent PARI elliptic-rank replay" in result.stdout


def test_nonzero_rank_transcript_rejected() -> None:
    _reject_transcript(
        _transcript().replace(
            "E_RANK=[0, 0, 0, []]",
            "E_RANK=[1, 1, 0, [[1, 1]]]",
        )
    )


def test_uncertified_rank_bounds_rejected() -> None:
    _reject_transcript(
        _transcript().replace("E_RANK=[0, 0, 0, []]", "E_RANK=[0, 1, 0, []]")
    )


def test_wrong_torsion_transcript_rejected() -> None:
    _reject_transcript(
        _transcript().replace(
            "E_TORS=[4, [4], [[0, 8]]]",
            "E_TORS=[8, [8], [[0, 8]]]",
        )
    )


def test_missing_transcript_field_rejected() -> None:
    text = "\n".join(
        line
        for line in _transcript().splitlines()
        if not line.startswith("E_RANK=")
    )
    _reject_transcript(text)


def test_script_digest_is_pinned(tmp_path: Path) -> None:
    module = _load_checker()
    script = tmp_path / "script.gp"
    script.write_text("print(\"tampered\")\n", encoding="utf-8")
    transcript = tmp_path / "output.txt"
    transcript.write_text(_transcript(), encoding="utf-8")
    with pytest.raises(ValueError):
        module.verify(script, transcript, run=False)
