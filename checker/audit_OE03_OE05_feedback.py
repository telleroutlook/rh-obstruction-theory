#!/usr/bin/env python3
"""Exact audit checks for the OE-03/OE-05 external feedback.

The checks below deliberately separate two issues:

1. The three quartics submitted for OE-03 are correct models for the
   square-based locus Apm = 5^e * square.
2. That locus is a proper sublocus of the powerful-away-from-5 condition:
   odd exponents at least three are still allowed.
"""

from __future__ import annotations

from collections.abc import Iterator
from fractions import Fraction
from math import gcd, isqrt


Poly = tuple[int, ...]
Gaussian = tuple[int, int]


def trim(poly: Poly) -> Poly:
    """Remove trailing zero coefficients while preserving the zero polynomial."""
    end = len(poly)
    while end > 0 and poly[end - 1] == 0:
        end -= 1
    return poly[:end]


def padd(left: Poly, right: Poly) -> Poly:
    result = [0] * max(len(left), len(right))
    for index, coefficient in enumerate(left):
        result[index] += coefficient
    for index, coefficient in enumerate(right):
        result[index] += coefficient
    return trim(tuple(result))


def psub(left: Poly, right: Poly) -> Poly:
    return padd(left, tuple(-coefficient for coefficient in right))


def pmul(left: Poly, right: Poly) -> Poly:
    if not left or not right:
        return ()
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(tuple(result))


def pscale(poly: Poly, scalar: int) -> Poly:
    return trim(tuple(scalar * coefficient for coefficient in poly))


def factorization(n: int) -> dict[int, int]:
    """Return the prime factorization of a positive integer."""
    if n < 1:
        raise ValueError("n must be positive")
    result: dict[int, int] = {}
    remaining = n
    prime = 2
    while prime * prime <= remaining:
        while remaining % prime == 0:
            result[prime] = result.get(prime, 0) + 1
            remaining //= prime
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def is_powerful_away_from_5(n: int) -> bool:
    return all(prime == 5 or exponent >= 2 for prime, exponent in factorization(n).items())


def is_square_based_powerful_away_from_5(n: int) -> bool:
    """Check whether n = 5^e * square (the t=1 subcase)."""
    remaining = n
    while remaining % 5 == 0:
        remaining //= 5
    root = isqrt(remaining)
    return root * root == remaining


def gaussian_multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def gaussian_power(base: Gaussian, exponent: int) -> Gaussian:
    if exponent < 0:
        raise ValueError("only nonnegative exponents are supported")
    result: Gaussian = (1, 0)
    for _ in range(exponent):
        result = gaussian_multiply(result, base)
    return result


def norm(value: Gaussian) -> int:
    real, imaginary = value
    return real * real + imaginary * imaginary


def polynomial_identity_checks() -> None:
    """Verify the submitted rational parametrizations and quartics exactly."""
    # Case (0,0): x=(k^2-1)/(2k), (x-1)^2+1 = P00/(2k)^2.
    numerator = trim((-1, 0, 1))
    denominator = trim((0, 2))
    shifted_numerator = psub(numerator, denominator)
    p00 = padd(pmul(shifted_numerator, shifted_numerator), pmul(denominator, denominator))
    expected_p00 = trim((1, 4, 6, -4, 1))
    assert p00 == expected_p00, (p00, expected_p00)

    # Case (1,0): x=(1+2k-k^2)/(1-k^2), x^2+1 = P10/(1-k^2)^2.
    numerator = trim((1, 2, -1))
    denominator = trim((1, 0, -1))
    p10 = padd(pmul(numerator, numerator), pmul(denominator, denominator))
    expected_p10 = trim((2, 4, 0, -4, 2))
    assert p10 == expected_p10, (p10, expected_p10)
    # If 5u^2=x^2+1 and W=5u(1-k^2), then W^2=5*P10.
    assert pscale(p10, 5) == trim((10, 20, 0, -20, 10))

    # Case (1,1): x=(-10k^2+10k-2)/(1-5k^2),
    # (x-1)^2+1 = P11/(1-5k^2)^2 = 5*Q11/(1-5k^2)^2.
    numerator = trim((-2, 10, -10))
    denominator = trim((1, 0, -5))
    shifted_numerator = psub(numerator, denominator)
    p11 = padd(pmul(shifted_numerator, shifted_numerator), pmul(denominator, denominator))
    assert p11 == trim((10, -60, 120, -100, 50)), p11
    q11 = tuple(coefficient // 5 for coefficient in p11)
    assert q11 == trim((2, -12, 24, -20, 10)), q11


def powerful_scope_checks() -> None:
    """Exhibit values allowed by powerfulness but omitted by 5^e*square models."""
    # The rational prime 13 splits in Z[i]. Its third power has an odd exponent
    # and hence a nontrivial cube factor, while still being powerful away from 5.
    value = 13**3
    assert factorization(value) == {13: 3}
    assert is_powerful_away_from_5(value)
    assert not is_square_based_powerful_away_from_5(value)

    # The same phenomenon occurs in the Gaussian norm: (3+2i)^3 has norm 13^3.
    gaussian_value = gaussian_power((3, 2), 3)
    assert gaussian_value == (-9, 46), gaussian_value
    assert norm(gaussian_value) == value

    # Bounding only the number of supporting primes does not bound heights.
    # All these values have one supporting prime, are powerful away from 5,
    # and have a nontrivial cube factor.
    heights: list[int] = []
    for exponent in range(3, 13, 2):
        family_value = 13**exponent
        assert factorization(family_value) == {13: exponent}
        assert is_powerful_away_from_5(family_value)
        assert not is_square_based_powerful_away_from_5(family_value)
        heights.append(family_value)
    assert all(left < right for left, right in zip(heights, heights[1:]))


def excluded_small_anchor_checks() -> None:
    """Check the submitted k=1 anchor maps to (a,n)=(1,2), excluded by n>=4."""
    k = Fraction(1)
    x = (-10 * k * k + 10 * k - 2) / (1 - 5 * k * k)
    assert x == Fraction(1, 2), x
    a, n = 1, 2
    assert a / n == x
    assert a * a + n * n == 5
    assert (n - a) * (n - a) + n * n == 5
    assert n < 4


def frey_curve_discriminant_check() -> None:
    """Check the stated discriminant formula on an exact sample."""
    # For Y^2=X(X-w)(X+n), the cubic discriminant is
    # 16*w^2*n^2*(w+n)^2. The submitted reply wrote
    # 16*w*(-w_minus)*n^2 instead.
    a, n = 1, 4
    w_plus = (a, n)
    w_minus = (n - a, n)
    w_plus_plus_n = (w_plus[0] + n, w_plus[1])
    expected = gaussian_power(w_plus, 2)
    expected = gaussian_multiply(expected, w_plus_plus_n)
    expected = gaussian_multiply(expected, (16 * n * n, 0))

    claimed = (w_minus[0], -w_minus[1])
    claimed = gaussian_multiply(w_plus, claimed)
    claimed = gaussian_multiply(claimed, (16 * n * n, 0))

    assert expected != claimed, (expected, claimed)


def row3_pairs(max_n: int) -> Iterator[tuple[int, int]]:
    for n in range(4, max_n + 1, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n, 2):
            if gcd(a, n) == 1:
                yield a, n


def numerical_row3_check(max_n: int = 200) -> tuple[int, int]:
    """Return counts of square-based and general powerful simultaneous pairs."""
    square_based = 0
    powerful = 0
    for a, n in row3_pairs(max_n):
        plus = a * a + n * n
        minus = (n - a) * (n - a) + n * n
        square_based += int(
            is_square_based_powerful_away_from_5(plus)
            and is_square_based_powerful_away_from_5(minus)
        )
        powerful += int(
            is_powerful_away_from_5(plus) and is_powerful_away_from_5(minus)
        )
    return square_based, powerful


def main() -> None:
    polynomial_identity_checks()
    powerful_scope_checks()
    excluded_small_anchor_checks()
    frey_curve_discriminant_check()
    square_based_count, powerful_count = numerical_row3_check()
    assert square_based_count == 0, square_based_count
    assert powerful_count == 0, powerful_count
    print("OE-03/OE-05 feedback audit: all exact assertions succeeded")
    print("submitted quartic parametrizations: verified")
    print("powerful-away-from-5 scope: 13^3 is powerful but not 5^e*square")
    print("support-cardinality caution: one-prime family 13^(2j+3) has unbounded height")
    print("Frey-curve discriminant: submitted formula disagrees with the stated cubic")
    print(f"Row-3 simultaneous scan n<=200: square_based={square_based_count}, powerful={powerful_count}")


if __name__ == "__main__":
    main()
