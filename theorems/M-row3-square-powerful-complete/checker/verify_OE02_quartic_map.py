#!/usr/bin/env python3
"""Exact checks for the corrected OE-02 5-conic and quartic map."""
from __future__ import annotations

import argparse
from math import gcd
from fractions import Fraction

Polynomial = dict[tuple[int, int], int]


def constant(value: int) -> Polynomial:
    return {(0, 0): value}


def variable(first: bool) -> Polynomial:
    return {(1 if first else 0, 0 if first else 1): 1}


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for term, coefficient in right.items():
        result[term] = result.get(term, 0) + coefficient
        if result[term] == 0:
            del result[term]
    return result


def sub(left: Polynomial, right: Polynomial) -> Polynomial:
    return add(left, scale(right, -1))


def scale(value: Polynomial, factor: int) -> Polynomial:
    return {
        term: coefficient * factor
        for term, coefficient in value.items()
        if coefficient * factor != 0
    }


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_term, left_coefficient in left.items():
        for right_term, right_coefficient in right.items():
            term = (left_term[0] + right_term[0], left_term[1] + right_term[1])
            coefficient = left_coefficient * right_coefficient
            result[term] = result.get(term, 0) + coefficient
            if result[term] == 0:
                del result[term]
    return result


def power(value: Polynomial, exponent: int) -> Polynomial:
    if exponent < 0:
        raise ValueError("polynomial exponents must be nonnegative")
    result = constant(1)
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def conic_parameterization() -> bool:
    """Verify x=2(5t²-5t+1)/(5t²-1), r=-(5t²-4t+1)/(5t²-1)."""
    t = variable(True)
    numerator_x = scale(sub(add(scale(power(t, 2), 5), constant(1)), scale(t, 5)), 2)
    numerator_r = sub(add(scale(t, 4), constant(-1)), scale(power(t, 2), 5))
    denominator = sub(scale(power(t, 2), 5), constant(1))
    return polynomial_equal(
        add(power(numerator_x, 2), power(denominator, 2)),
        scale(power(numerator_r, 2), 5),
    )


def quartic_derivation() -> bool:
    """Verify the second 5-conic gives Y²=10t⁴-20t³+24t²-12t+2."""
    t = variable(True)
    y = variable(False)
    numerator_x = scale(sub(add(scale(power(t, 2), 5), constant(1)), scale(t, 5)), 2)
    denominator = sub(scale(power(t, 2), 5), constant(1))
    second_left = add(
        sub(power(numerator_x, 2), scale(multiply(numerator_x, denominator), 2)),
        scale(power(denominator, 2), 2),
    )
    quartic_polynomial = add(
        add(scale(power(t, 4), 10), scale(power(t, 3), -20)),
        add(
            add(scale(power(t, 2), 24), scale(t, -12)),
            constant(2),
        ),
    )
    # After clearing denominators, second_left=5F and second_left-5Y²=5(F-Y²).
    return polynomial_equal(
        sub(second_left, scale(power(y, 2), 5)),
        scale(sub(quartic_polynomial, power(y, 2)), 5),
    )


def forward_map_identity() -> bool:
    """Verify the corrected shifted-quartic map to y²=x³-32x+64."""
    u = variable(True)
    v = variable(False)
    shifted_quartic = add(
        sub(power(v, 2), scale(power(u, 4), 10)),
        add(
            add(scale(power(u, 3), -20), scale(power(u, 2), -24)),
            add(scale(u, -16), constant(-4)),
        ),
    )
    a = add(add(add(v, constant(2)), scale(u, 4)), scale(power(u, 2), 2))
    b = add(
        add(multiply(v, add(constant(1), u)), constant(2)),
        add(scale(u, 6), scale(power(u, 2), 6)),
    )
    y_numerator = add(scale(b, 16), scale(power(u, 3), 40))
    curve_numerator = add(
        sub(power(y_numerator, 2), scale(power(a, 3), 64)),
        add(
            scale(multiply(a, power(u, 4)), 128),
            scale(power(u, 6), -64),
        ),
    )
    return polynomial_equal(
        curve_numerator, multiply(scale(a, -64), shifted_quartic)
    )


def inverse_map_identity() -> bool:
    """Verify the inverse formula on y²=x³-32x+64."""
    x = variable(True)
    y = variable(False)
    denominator = add(sub(scale(x, 4), y), constant(8))
    t_numerator = sub(constant(8), y)
    v_numerator = add(
        scale(power(x, 3), 4),
        add(scale(power(y, 2), -2), scale(y, 32)),
    )
    v_numerator = add(v_numerator, constant(-128))
    quartic_numerator = add(
        sub(
            scale(power(t_numerator, 4), 10),
            scale(multiply(power(t_numerator, 3), denominator), 20),
        ),
        add(
            add(
                scale(multiply(power(t_numerator, 2), power(denominator, 2)), 24),
                scale(multiply(t_numerator, power(denominator, 3)), -12),
            ),
            add(scale(power(denominator, 4), 2), scale(power(v_numerator, 2), -1)),
        ),
    )
    elliptic_polynomial = add(
        sub(power(y, 2), power(x, 3)),
        add(scale(x, 32), constant(-64)),
    )
    expected = multiply(scale(power(x, 3), 16), elliptic_polynomial)
    return polynomial_equal(quartic_numerator, expected)


def polynomial_equal(left: Polynomial, right: Polynomial) -> bool:
    return left == right


def individual_square_counterexample() -> tuple[int, int, int, int]:
    """Return (a,n,A+,A-) showing individual 4|n squares are not excluded."""
    a, n = 15, 8
    plus = a * a + n * n
    minus = (n - a) * (n - a) + n * n
    if gcd(a, n) != 1 or n % 4 != 0 or n % 3 == 0 or a % 2 == 0:
        raise AssertionError("counterexample is not a Row-3 pair")
    if plus != 289 or minus != 113:
        raise AssertionError("counterexample values changed")
    return a, n, plus, minus


def forward_quartic_to_curve(
    t: Fraction, y: Fraction
) -> tuple[Fraction, Fraction]:
    """Apply the non-exceptional corrected-quartic map to E."""
    if t == 1:
        raise ValueError("t=1 is handled on the projective completion")
    u = t - 1
    a = y + 2 + 4 * u + 2 * u * u
    b = y * (1 + u) + 2 + 6 * u + 6 * u * u
    x_curve = 4 * a / (u * u)
    y_curve = 16 * b / (u**3) + 40
    if y_curve**2 != x_curve**3 - 32 * x_curve + 64:
        raise AssertionError("forward map does not land on E")
    return x_curve, y_curve


def inverse_curve_to_quartic(
    x: Fraction, y: Fraction
) -> tuple[Fraction, Fraction]:
    """Apply the non-exceptional inverse map on E."""
    if y**2 != x**3 - 32 * x + 64:
        raise AssertionError("input is not on E")
    denominator = 4 * x - y + 8
    if denominator == 0:
        raise ValueError("exceptional torsion point (0,8)")
    u = -4 * x / denominator
    v = (
        2
        * (2 * x**3 - y**2 + 16 * y - 64)
        / (denominator * denominator)
    )
    t = 1 + u
    if v**2 != (
        10 * t**4 - 20 * t**3 + 24 * t**2 - 12 * t + 2
    ):
        raise AssertionError("inverse map does not land on the quartic")
    return t, v


def torsion_pullback_toys() -> list[tuple[Fraction, Fraction, Fraction]]:
    """Return the four torsion pullbacks (t,Y_quartic,x_conic)."""
    values = [
        (Fraction(1), Fraction(2)),
        (Fraction(1), Fraction(-2)),
        (Fraction(1, 3), Fraction(2, 9)),
        (Fraction(1, 3), Fraction(-2, 9)),
    ]
    normalized: list[tuple[Fraction, Fraction, Fraction]] = []
    for t, y_quartic in values:
        quartic_value = (
            10 * t**4
            - 20 * t**3
            + 24 * t**2
            - 12 * t
            + 2
        )
        if y_quartic**2 != quartic_value:
            raise AssertionError("torsion pullback is not on the corrected quartic")
        x = Fraction(2 * (5 * t * t - 5 * t + 1), 5 * t * t - 1)
        normalized.append((t, y_quartic, x))
    if any(pair[2] != Fraction(1, 2) for pair in normalized):
        raise AssertionError("torsion pullbacks do not give x=1/2")
    if forward_quartic_to_curve(Fraction(1, 3), Fraction(2, 9)) != (
        Fraction(4),
        Fraction(0),
    ):
        raise AssertionError("(4,0) torsion pullback failed")
    if forward_quartic_to_curve(Fraction(1, 3), Fraction(-2, 9)) != (
        Fraction(0),
        Fraction(8),
    ):
        raise AssertionError("(0,8) torsion pullback failed")
    if inverse_curve_to_quartic(Fraction(4), Fraction(0)) != (
        Fraction(1, 3),
        Fraction(2, 9),
    ):
        raise AssertionError("inverse of (4,0) failed")
    if inverse_curve_to_quartic(Fraction(0), Fraction(-8)) != (
        Fraction(1),
        Fraction(-2),
    ):
        raise AssertionError("inverse of (0,-8) failed")
    return normalized


def check() -> list[str]:
    if not conic_parameterization():
        raise AssertionError("5-conic parameterization identity failed")
    if not quartic_derivation():
        raise AssertionError("quartic derivation identity failed")
    if not forward_map_identity():
        raise AssertionError("corrected quartic-to-E identity failed")
    if not inverse_map_identity():
        raise AssertionError("corrected E-to-quartic identity failed")
    if len(torsion_pullback_toys()) != 4:
        raise AssertionError("torsion pullback toy count failed")
    a, n, plus, _ = individual_square_counterexample()
    if plus != 17 * 17:
        raise AssertionError("individual-square counterexample failed")
    return [
        "5-conic parameterization",
        "correct quartic derivation",
        "forward corrected-quartic-to-E polynomial identity",
        "inverse E-to-quartic polynomial identity",
        "four torsion pullbacks and two exact inverse correspondences",
        f"individual-square boundary witness (a,n)=({a},{n})",
    ]


def main(argv: list[str] | None = None) -> int:
    argparse.ArgumentParser(description=__doc__).parse_args(argv)
    try:
        checks = check()
    except AssertionError as exc:
        print(f"FAIL: {exc}", flush=True)
        return 1
    for item in checks:
        print(f"PASS: {item}", flush=True)
    print("PASS: OE-02 corrected 5-conic and quartic map replay", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
