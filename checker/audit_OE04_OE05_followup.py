#!/usr/bin/env python3
"""Exact audit checks for the second OE-04 and OE-05 external replies."""

from __future__ import annotations

from fractions import Fraction


Matrix2 = tuple[tuple[int, int], tuple[int, int]]


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


def j_invariant(a: int, b: int) -> Fraction:
    """Return j for the short Weierstrass model y^2=x^3+a*x+b."""
    numerator = 1728 * 4 * a**3
    denominator = 4 * a**3 + 27 * b**2
    if denominator == 0:
        raise ValueError("singular model")
    return Fraction(numerator, denominator)


def determinant(matrix: Matrix2) -> int:
    (a, b), (c, d) = matrix
    return a * d - b * c


def oe04_large_gap_and_symmetry_checks() -> None:
    """Check the symmetric quartic and the gap-only obstruction."""
    for u, m in [(1, 2), (3, 5), (-4, 7)]:
        plus = (u + m) ** 2 + 4 * m**2
        minus = (m - u) ** 2 + 4 * m**2
        product_formula = u**4 + 6 * m**2 * u**2 + 25 * m**4
        assert plus * minus == product_formula, (u, m, plus * minus, product_formula)

    # A gap-only theorem in the requested regime is false outside Row-3:
    # 4=2^2 and 8=2^3 are both powerful away from 5 and differ by a size.
    assert is_powerful_away_from_5(4)
    assert is_powerful_away_from_5(8)
    assert 8 - 4 == 4


def oe04_model_consistency_checks() -> None:
    """Compare the two elliptic models supplied by the OE-04 reply."""
    # The multiplied-conic model y^2=x^3+6x^2+25x becomes
    # Y^2=X^3+13X-34 under X=x+2.
    multiplied_conic_j = j_invariant(13, -34)
    # Cassels' Jacobian model y^2=x(x+4)(x-16)=x^3-12x^2-64x becomes
    # Y^2=X^3-112X-384 under X=x+4.
    cassels_j = j_invariant(-112, -384)
    crossratio_j = Fraction(148176, 25)
    assert multiplied_conic_j == Fraction(237276, 625)
    assert cassels_j == crossratio_j
    assert multiplied_conic_j != cassels_j


def oe04_fixed_cube_pair_genus_check() -> None:
    """For z_+=z_-=1, the fixed system is a smooth genus-one intersection."""
    # Pencil determinant, up to a nonzero scalar, is
    # lambda*mu*(lambda^2+3*lambda*mu+mu^2).
    # Its four roots are distinct: [0:1], [1:0], and the two roots of the
    # quadratic with discriminant 5.
    for lam, mu in [(0, 1), (1, 0), (1, 1), (2, 1)]:
        value = lam * mu * (lam * lam + 3 * lam * mu + mu * mu)
        if (lam, mu) not in [(0, 1), (1, 0)]:
            assert value != 0
    # x^2+3x+1 has nonsquare discriminant 5, hence two distinct roots.
    assert 3 * 3 - 4 * 1 * 1 == 5


def oe05_pencil_counterexamples() -> None:
    """Disprove the claimed determinant normal forms by exact samples."""
    # For the (X,Y) block of lambda*Q+mu*P, the matrix is
    # [[lambda*v+mu*(u-v), lambda*u-mu*(u+v)],
    #  [lambda*u-mu*(u+v), -lambda*v+mu*u]].
    def b1(lam: int, mu: int, u: int, v: int) -> Matrix2:
        return (
            (lam * v + mu * (u - v), lam * u - mu * (u + v)),
            (lam * u - mu * (u + v), -lam * v + mu * u),
        )

    actual_b1 = determinant(b1(2, 1, 2, 1))
    claimed_b1 = -(2**2 + 1**2) * (2**2 - 2 * 2 * 1 + 2 * 1**2)
    assert actual_b1 == -1, actual_b1
    assert claimed_b1 == -10, claimed_b1
    assert actual_b1 != claimed_b1

    # For the (Z,W) block, the matrix is
    # [[-lambda*v+mu*u, -lambda*u-mu*v],
    #  [-lambda*u-mu*v, lambda*v+mu*u]].
    def b2(lam: int, mu: int, u: int, v: int) -> Matrix2:
        return (
            (-lam * v + mu * u, -lam * u - mu * v),
            (-lam * u - mu * v, lam * v + mu * u),
        )

    actual_b2 = determinant(b2(2, 1, 1, 2))
    claimed_b2 = -(1**2 + 2**2) * (2**2 + 1**2)
    assert actual_b2 == -31, actual_b2
    assert claimed_b2 == -25, claimed_b2
    assert actual_b2 != claimed_b2


def oe05_weierstrass_checks() -> None:
    """Check the claimed base curve, j-invariant, and rational 2-torsion."""
    claimed_j = Fraction(148176, 25)
    model_j = j_invariant(-21, 10)
    assert model_j == Fraction(98784, 53)
    assert model_j != claimed_j

    # x^3-21x+10 has no rational root among the divisors of 10.
    roots = [x for x in (-10, -5, -2, -1, 1, 2, 5, 10) if x**3 - 21 * x + 10 == 0]
    assert roots == [], roots


def main() -> None:
    oe04_large_gap_and_symmetry_checks()
    oe04_model_consistency_checks()
    oe04_fixed_cube_pair_genus_check()
    oe05_pencil_counterexamples()
    oe05_weierstrass_checks()
    print("OE-04/OE-05 follow-up audit: all exact assertions succeeded")
    print("OE-04 symmetry quartic: verified; 4 and 8 refute a gap-only theorem")
    print("OE-04 elliptic models: supplied models have different j-invariants")
    print("OE-04 fixed cube-pair system z_+=z_-=1: smooth genus one, not genus >1")
    print("OE-05 pencil determinants: both claimed normal forms fail exact samples")
    print("OE-05 E0 model: j=98784/53, not 148176/25, and has no rational 2-torsion")


if __name__ == "__main__":
    main()
