#!/usr/bin/env python3
"""Exact elementary checks for the OE-02 elliptic model.

This checker does not compute the Mordell-Weil rank.  The independent PARI/GP
replay in verify_OE02_pari_replay.py certifies the rank-zero computation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import isqrt


def curve_value(x: int) -> int:
    """Evaluate y^2 = x^3 - 32x + 64."""
    return x**3 - 32 * x + 64


def add_points(
    p: tuple[Fraction, Fraction] | None,
    q: tuple[Fraction, Fraction] | None,
    a4: int = -32,
) -> tuple[Fraction, Fraction] | None:
    """Add points on y^2=x^3+a4*x+64 using exact rational arithmetic."""
    if p is None:
        return q
    if q is None:
        return p
    px, py = p
    qx, qy = q
    if px == qx:
        if py != qy or py == 0:
            return None
        slope = (3 * px * px + a4) / (2 * py)
    else:
        slope = (qy - py) / (qx - px)
    rx = slope * slope - px - qx
    ry = slope * (px - rx) - py
    return (rx, ry)


def divisors(value: int) -> list[int]:
    """Return nonnegative divisors of |value| (including 0 when value=0)."""
    value = abs(value)
    if value == 0:
        return [0]
    return [d for d in range(1, isqrt(value) + 1) if value % d == 0 for d in ({d, value // d})]


def nagell_lutz_points() -> list[tuple[int, int]]:
    """Reconstruct integral torsion candidates allowed by Nagell-Lutz."""
    cubic_discriminant = -4 * (-32) ** 3 - 27 * 64**2
    if cubic_discriminant != 20480:
        raise AssertionError("unexpected cubic discriminant")
    points: set[tuple[int, int]] = {(4, 0)}
    # A nonzero integral torsion ordinate has y^2 | 20480 = 2^12 * 5.
    # Thus y has no factor 5 and |y|=2^j with j <= 6.
    for absolute_y in (2**j for j in range(7)):
        for y in (absolute_y, -absolute_y):
            constant = 64 - y * y
            # Rational-root theorem: every integer root divides the constant.
            for x in divisors(constant):
                if curve_value(x) == y * y:
                    points.add((x, y))
    return sorted(points)


def corrected_quartic_value(t: Fraction) -> Fraction:
    """Evaluate the corrected OE-02 quartic."""
    return (
        10 * t**4
        - 20 * t**3
        + 24 * t**2
        - 12 * t
        + 2
    )


def integer_quartic_hits(limit: int) -> list[tuple[int, int]]:
    """Finite exact integer scan of the corrected OE-02 quartic."""
    hits: list[tuple[int, int]] = []
    for t in range(-limit, limit + 1):
        value = 10 * t**4 - 20 * t**3 + 24 * t**2 - 12 * t + 2
        root = isqrt(value)
        if root * root == value:
            hits.append((t, root))
    return hits


def quartic_torsion_pullbacks() -> list[tuple[Fraction, Fraction]]:
    """Return the four exact corrected-quartic torsion pullbacks."""
    values = [
        (Fraction(1), Fraction(2)),
        (Fraction(1, 3), Fraction(2, 9)),
        (Fraction(1), Fraction(-2)),
        (Fraction(1, 3), Fraction(-2, 9)),
    ]
    for t, y in values:
        if y * y != corrected_quartic_value(t):
            raise AssertionError("incorrect corrected-quartic torsion point")
    return values


def check(limit: int) -> list[str]:
    points = nagell_lutz_points()
    expected = [(0, -8), (0, 8), (4, 0)]
    if points != expected:
        raise AssertionError(f"Nagell-Lutz torsion candidates differ: {points}")

    generator = (Fraction(0), Fraction(8))
    double = add_points(generator, generator)
    quadruple = add_points(double, double)
    if double != (Fraction(4), Fraction(0)) or quadruple is not None:
        raise AssertionError("torsion group-law computation failed")

    integer_hits = integer_quartic_hits(limit)
    if integer_hits != [(1, 2)]:
        raise AssertionError(
            f"unexpected finite corrected-quartic hits: {integer_hits}"
        )
    if len(quartic_torsion_pullbacks()) != 4:
        raise AssertionError("missing corrected-quartic torsion pullbacks")
    return [
        "Nagell-Lutz integer torsion candidates",
        "exact Z/4Z group law",
        f"corrected quartic integer scan |t|<={limit}",
        "four exact corrected-quartic torsion pullbacks",
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=3000)
    args = parser.parse_args(argv)
    if args.limit < 0:
        print("FAIL: --limit must be nonnegative", flush=True)
        return 1
    try:
        checks = check(args.limit)
    except AssertionError as exc:
        print(f"FAIL: {exc}", flush=True)
        return 1
    for item in checks:
        print(f"PASS: {item}", flush=True)
    print("PASS: OE-02 elementary elliptic checks", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
