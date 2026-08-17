#!/usr/bin/env python3
"""Exact rational sanity check for one instance of Theorem K.

The check is finite evidence only; it does not prove the p-adic theorem.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Iterable

RationalComplex = tuple[Fraction, Fraction]


def add(x: RationalComplex, y: RationalComplex) -> RationalComplex:
    return x[0] + y[0], x[1] + y[1]


def sub(x: RationalComplex, y: RationalComplex) -> RationalComplex:
    return x[0] - y[0], x[1] - y[1]


def mul(x: RationalComplex, y: RationalComplex) -> RationalComplex:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def scale(x: RationalComplex, c: Fraction) -> RationalComplex:
    return x[0] * c, x[1] * c


def conjugate(x: RationalComplex) -> RationalComplex:
    return x[0], -x[1]


def chebyshev(n: int, x: RationalComplex) -> RationalComplex:
    if n < 0:
        raise ValueError("n must be nonnegative")
    if n == 0:
        return Fraction(1), Fraction(0)
    previous: RationalComplex = (Fraction(1), Fraction(0))
    current = x
    two_x = scale(x, Fraction(2))
    for _ in range(2, n + 1):
        previous, current = current, sub(mul(two_x, current), previous)
    return current


def p_valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero is undefined here")
    num, den = value.numerator, value.denominator
    return _integer_valuation(num, prime) - _integer_valuation(den, prime)


def _integer_valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero is undefined here")
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def denominator_pole(values: Iterable[Fraction], prime: int) -> int:
    return max(max(0, -p_valuation(value, prime)) for value in values)


def reduced_fraction(numerator: int, denominator: int) -> Fraction:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    common = gcd(abs(numerator), denominator)
    return Fraction(numerator // common, denominator // common)


def check() -> None:
    prime = 3
    delay = 4
    maximum_order = 12
    u0: RationalComplex = (Fraction(0), Fraction(1, 3))

    d_values: list[Fraction] = []
    for degree in range(1, maximum_order + 1):
        value = chebyshev(degree, u0)
        real_part = (value[0] + conjugate(value)[0]) / 2
        d_values.append(Fraction(1) - real_part)

    observed_pole = denominator_pole(d_values, prime)
    expected_conservative_pole = maximum_order - delay
    assert observed_pole >= expected_conservative_pole

    # On-line conductors 4a^2+b^2 are not divisible by p=3.
    for numerator, denominator in ((1, 1), (1, 2), (2, 3), (5, 7)):
        assert (4 * numerator * numerator + denominator * denominator) % prime != 0

    # Adversarial mutation removes the inert denominator and therefore removes
    # the theorem hypothesis; the checker must detect this.
    mutated: RationalComplex = (Fraction(0), Fraction(1, 5))
    mutated_values: list[Fraction] = []
    for degree in range(1, maximum_order + 1):
        value = chebyshev(degree, mutated)
        real_part = (value[0] + conjugate(value)[0]) / 2
        mutated_values.append(Fraction(1) - real_part)
    assert all(p_valuation(value, prime) >= 0 for value in mutated_values)

    print(
        "PASS: inert-prime instance pole "
        f"{observed_pole} >= conservative bound {expected_conservative_pole}"
    )
    print("PASS: on-line conductors are p-integral")
    print("PASS: removing the inert denominator is detected as outside the hypothesis")


if __name__ == "__main__":
    check()

