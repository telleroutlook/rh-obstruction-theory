#!/usr/bin/env python3
"""Exact finite sanity check for Theorem I.

This checks one rational instance of the algebraic identities used in the
proof.  It is not a proof of the analytic theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True)
class Gaussian:
    """The rational Gaussian exp(-a z^2), represented by -a."""

    negative_a: Fraction

    def value(self, real: Fraction, imag: Fraction) -> tuple[Fraction, Fraction]:
        """Return exp(negative_a * z^2) symbolically as (exponent, 0)."""
        square_real = real * real - imag * imag
        square_imag = 2 * real * imag
        return (
            self.negative_a * square_real,
            self.negative_a * square_imag,
        )


def distinct(items: Iterable[tuple[Fraction, Fraction]]) -> bool:
    return len(set(items)) == len(list(items))


def check() -> None:
    a = Fraction(1, 5000)
    gamma = [Fraction(n) for n in (10, 13, 17, 21, 25, 30, 35, 40)]
    g = Fraction(20)
    delta = Fraction(1, 5)
    gaussian = Gaussian(negative_a=-a)

    online_exponents = [gaussian.value(x, Fraction(0))[0] for x in gamma]
    off_plus = gaussian.value(g, delta)
    off_minus = gaussian.value(g, -delta)
    exponents = [off_plus, off_minus, *online_exponents]

    assert distinct(exponents)
    assert all(value != 0 for value in online_exponents)
    assert off_plus[1] != 0 and off_minus[1] == -off_plus[1]

    # Formula check for the exponents: beta_pm = -a(g +/- i delta)^2.
    assert off_plus == (-a * (g * g - delta * delta), -2 * a * g * delta)
    assert off_minus == (-a * (g * g - delta * delta), 2 * a * g * delta)
    assert online_exponents == [-a * x * x for x in gamma]

    # Adversarial mutation must break distinctness detection when it duplicates
    # an exponent.  The theorem checker must reject this mutated list.
    mutated = [off_plus, off_plus, *online_exponents]
    assert not distinct(mutated)

    print("PASS: exact Gaussian instance identities and distinct exponents")
    print("PASS: adversarial duplicate-exponent mutation is rejected")


if __name__ == "__main__":
    check()

