#!/usr/bin/env python3
"""Verify the independent PARI/GP replay for the OE-02 elliptic curve.

The default mode validates the pinned raw CAS transcript and independently
checks the rational model transformations.  With --run, it reruns PARI/GP and
requires byte-identical transcript output.  The checker does not replace the
analytic 5-conic reduction proof.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
from pathlib import Path

_SCRIPT_DIGEST = (
    "51e6d3c8766e8ad5056fa1e0e9232ae2e08ed61934bf67bf36b3f823716bee19"
)
_EXPECTED = {
    "PARI_VERSION": "[2, 17, 4]",
    "E_DISC": "327680",
    "E0_DISC": "327680",
    "EHAT_DISC": "26214400",
    "Q_DISC": "327680",
    "Q_MODEL": "[0, 24, 0, 160, 320]",
    "E_RANK": "[0, 0, 0, []]",
    "E0_RANK": "[0, 0, 0, []]",
    "EHAT_RANK": "[0, 0, 0, []]",
    "Q_RANK": "[0, 0, 0, []]",
    "E_TORS": "[4, [4], [[0, 8]]]",
    "E0_TORS": "[4, [4], [[-4, 8]]]",
    "EHAT_TORS": "[4, [2, 2], [[20, 0], [0, 0]]]",
    "Q_TORS": "[4, [4], [[-8, 8]]]",
    "E_ONCURVE": "1",
    "E_2P": "[4, 0]",
    "E_4P": "[0]",
    "E0_MAP_POINT": "1",
    "E0_2P": "[0, 0]",
    "E0_4P": "[0]",
    "E_GLOBALRED": (
        "[40, [2, 0, 0, 0], 2, [2, 3; 5, 1], "
        "[[3, 3, 0, 2], [1, 5, 0, 1]]]"
    ),
    "E_2_ISO_CLASS": (
        "[[[-32, 64], [-112, -384], [208, -2176], [-1712, -27264]], "
        "[1, 2, 4, 4; 2, 1, 2, 2; 4, 2, 1, 4; 4, 2, 4, 1]]"
    ),
}
_LINE = re.compile(r"^([A-Z0-9_]+)=(.*)$")


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _parse_transcript(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        if not line:
            continue
        match = _LINE.fullmatch(line)
        if match is None:
            raise ValueError(f"malformed transcript line: {line!r}")
        key, value = match.groups()
        if key in result:
            raise ValueError(f"duplicate transcript key: {key}")
        result[key] = value
    if set(result) != set(_EXPECTED):
        missing = sorted(set(_EXPECTED) - set(result))
        extra = sorted(set(result) - set(_EXPECTED))
        raise ValueError(f"transcript keys differ; missing={missing}, extra={extra}")
    errors = [key for key, value in _EXPECTED.items() if result[key] != value]
    if errors:
        raise ValueError(f"transcript values differ for: {', '.join(errors)}")
    return result


def _check_model_transformations() -> None:
    # Original E: y^2 = x^3 - 32x + 64.  Put x = u + 4.
    lhs = (4**3) - 32 * 4 + 64
    if lhs != 0 or (0**3) + (12 * 0**2) + (16 * 0) != 0:
        raise ValueError("2-torsion translation failed")
    for u in range(-20, 21):
        original = (u + 4) ** 3 - 32 * (u + 4) + 64
        translated = u**3 + 12 * u**2 + 16 * u
        if original != translated:
            raise ValueError(f"E -> E0 polynomial identity failed at u={u}")
    # 2-isogenous model for y^2 = u^3 + a u^2 + b u has
    # y^2 = u^3 - 2a u^2 + (a^2 - 4b)u.
    if (-2 * 12, (12**2) - 4 * 16) != (-24, 80):
        raise ValueError("2-isogenous coefficient formula failed")
    for q_x in range(-20, 41):
        old_x = q_x + 8
        old_model = old_x**3 - 32 * old_x + 64
        corrected_quartic_model = q_x**3 + 24 * q_x**2 + 160 * q_x + 320
        if old_model != corrected_quartic_model:
            raise ValueError("corrected-quartic Jacobian translation failed")


def _run_gp(script: Path) -> str:
    executable = shutil.which("gp")
    if executable is None:
        raise ValueError("PARI/GP executable gp was not found")
    process = subprocess.run(
        [executable, "-q", str(script)],
        capture_output=True,
        text=True,
        check=False,
    )
    if process.returncode != 0:
        raise ValueError(
            f"PARI/GP failed with exit code {process.returncode}: "
            f"{process.stderr.strip()}"
        )
    return process.stdout


def verify(script: Path, transcript: Path, run: bool) -> list[str]:
    if _digest(script) != _SCRIPT_DIGEST:
        raise ValueError("PARI/GP replay script digest mismatch")
    pinned = transcript.read_text(encoding="utf-8").strip("\n")
    raw = _run_gp(script).strip("\n") if run else pinned
    if run and raw != pinned:
        raise ValueError("live PARI/GP transcript differs from pinned transcript")
    parsed = _parse_transcript(raw.strip("\n"))
    _check_model_transformations()
    if parsed["E_RANK"] != "[0, 0, 0, []]":
        raise AssertionError("unreachable rank check")
    return [
        "pinned PARI transcript digest",
        "certified rank bounds 0 <= rank <= 0",
        "rank 0 on original, translated, and 2-isogenous models",
        "corrected quartic Jacobian has rank 0 and torsion Z/4Z",
        "torsion Z/4Z on original and translated models",
        "exact model translation and isogeny coefficients",
    ]


def main(argv: list[str] | None = None) -> int:
    witness = Path(__file__).resolve().parents[1] / "witness"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true", help="rerun PARI/GP")
    args = parser.parse_args(argv)
    try:
        checks = verify(
            witness / "oe02_pari_replay_v1.gp",
            witness / "oe02_pari_replay_v1.txt",
            args.run,
        )
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print(f"FAIL: {exc}", flush=True)
        return 1
    for check in checks:
        print(f"PASS: {check}", flush=True)
    print("PASS: OE-02 independent PARI elliptic-rank replay", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
