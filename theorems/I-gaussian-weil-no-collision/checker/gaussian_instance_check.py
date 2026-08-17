#!/usr/bin/env python3
"""Deterministic exact replay for a finite Theorem I witness.

The checker reconstructs the Gaussian observation reduction from raw algebraic
data.  It does not prove Lindemann-Weierstrass and does not certify the full
analytic theorem.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

_RATIONAL = re.compile(r"^[+-]?\d+(?:/[+-]?\d+)?$")


class WitnessError(ValueError):
    """A witness failed one deterministic rejection condition."""


@dataclass(frozen=True)
class Quadratic:
    """An element q0 + q1 sqrt(radical) of a fixed real quadratic field."""

    rational: Fraction
    sqrt_coefficient: Fraction
    radical: int

    @classmethod
    def rational_in_field(cls, value: Fraction, radical: int) -> "Quadratic":
        return cls(value, Fraction(0), radical)

    @property
    def is_zero(self) -> bool:
        return self.rational == 0 and self.sqrt_coefficient == 0

    def sign(self) -> int:
        if self.is_zero:
            return 0
        r = self.rational
        s = self.sqrt_coefficient
        if r >= 0 and s >= 0:
            return 1
        if r <= 0 and s <= 0:
            return -1
        # Opposite signs: compare |r|^2 with |s|^2 * radical.
        left = r * r
        right = s * s * self.radical
        if r > 0:
            return 1 if left > right else (-1 if left < right else 0)
        return 1 if right > left else (-1 if right < left else 0)

    def __add__(self, other: "Quadratic") -> "Quadratic":
        self._require_same_field(other)
        return Quadratic(
            self.rational + other.rational,
            self.sqrt_coefficient + other.sqrt_coefficient,
            self.radical,
        )

    def __sub__(self, other: "Quadratic") -> "Quadratic":
        self._require_same_field(other)
        return Quadratic(
            self.rational - other.rational,
            self.sqrt_coefficient - other.sqrt_coefficient,
            self.radical,
        )

    def __mul__(self, other: "Quadratic") -> "Quadratic":
        self._require_same_field(other)
        return Quadratic(
            self.rational * other.rational
            + self.sqrt_coefficient * other.sqrt_coefficient * self.radical,
            self.rational * other.sqrt_coefficient
            + self.sqrt_coefficient * other.rational,
            self.radical,
        )

    def __neg__(self) -> "Quadratic":
        return Quadratic(-self.rational, -self.sqrt_coefficient, self.radical)

    def _require_same_field(self, other: "Quadratic") -> None:
        if self.radical != other.radical:
            raise WitnessError(
                f"mixed quadratic fields: sqrt({self.radical}) and sqrt({other.radical})"
            )


@dataclass(frozen=True)
class ComplexQuadratic:
    """A complex number whose real and imaginary parts are Quadratic."""

    real: Quadratic
    imaginary: Quadratic

    @property
    def is_zero(self) -> bool:
        return self.real.is_zero and self.imaginary.is_zero

    def conjugate(self) -> "ComplexQuadratic":
        return ComplexQuadratic(self.real, -self.imaginary)

    def scale(self, scalar: Quadratic) -> "ComplexQuadratic":
        return ComplexQuadratic(self.real * scalar, self.imaginary * scalar)

    def __add__(self, other: "ComplexQuadratic") -> "ComplexQuadratic":
        return ComplexQuadratic(
            self.real + other.real, self.imaginary + other.imaginary
        )

    def __sub__(self, other: "ComplexQuadratic") -> "ComplexQuadratic":
        return ComplexQuadratic(
            self.real - other.real, self.imaginary - other.imaginary
        )

    def __mul__(self, other: "ComplexQuadratic") -> "ComplexQuadratic":
        return ComplexQuadratic(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    def __neg__(self) -> "ComplexQuadratic":
        return ComplexQuadratic(-self.real, -self.imaginary)


@dataclass(frozen=True)
class Polynomial:
    """A sparse even polynomial over a fixed real quadratic field."""

    coefficients: dict[int, Quadratic]
    radical: int

    def evaluate(self, z: ComplexQuadratic) -> ComplexQuadratic:
        if z.real.radical != self.radical:
            raise WitnessError("polynomial and evaluation point use different fields")
        one = ComplexQuadratic(
            Quadratic.rational_in_field(Fraction(1), self.radical),
            Quadratic.rational_in_field(Fraction(0), self.radical),
        )
        result = ComplexQuadratic(
            Quadratic.rational_in_field(Fraction(0), self.radical),
            Quadratic.rational_in_field(Fraction(0), self.radical),
        )
        power = one
        previous_degree = 0
        for degree in sorted(self.coefficients):
            for _ in range(degree - previous_degree):
                power = power * z
            previous_degree = degree
            coefficient = ComplexQuadratic(
                self.coefficients[degree],
                Quadratic.rational_in_field(Fraction(0), self.radical),
            )
            result = result + coefficient * power
        return result


def parse_fraction(value: Any, field: str) -> Fraction:
    if not isinstance(value, str) or _RATIONAL.fullmatch(value) is None:
        raise WitnessError(f"{field} must be an exact rational string")
    numerator_text, separator, denominator_text = value.partition("/")
    numerator = Fraction(numerator_text)
    denominator = Fraction(denominator_text) if separator else Fraction(1)
    if denominator <= 0:
        raise WitnessError(f"{field} denominator must be positive")
    return numerator / denominator


def parse_quadratic(value: Any, radical: int, field: str) -> Quadratic:
    if isinstance(value, str):
        return Quadratic.rational_in_field(parse_fraction(value, field), radical)
    if not isinstance(value, dict) or set(value) != {
        "rational",
        "sqrt_coefficient",
    }:
        raise WitnessError(
            f"{field} must be a rational string or an exact quadratic object"
        )
    rational = parse_fraction(value["rational"], f"{field}.rational")
    sqrt_coefficient = parse_fraction(
        value["sqrt_coefficient"], f"{field}.sqrt_coefficient"
    )
    if radical == 1 and sqrt_coefficient != 0:
        raise WitnessError(f"{field} has nonzero sqrt coefficient in Q")
    return Quadratic(rational, sqrt_coefficient, radical)


def _strict_object(value: Any, required: set[str], field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise WitnessError(f"{field} must be an object")
    actual = set(value)
    if actual != required:
        raise WitnessError(
            f"{field} keys must be exactly {sorted(required)}; got {sorted(actual)}"
        )
    return value


def load_witness(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WitnessError(f"cannot read witness: {exc}") from exc
    if not isinstance(value, dict):
        raise WitnessError("witness root must be an object")
    return value


def parse_polynomial(value: Any, radical: int) -> Polynomial:
    obj = _strict_object(value, {"coefficients"}, "polynomial")
    entries = obj["coefficients"]
    if not isinstance(entries, list) or not entries:
        raise WitnessError("polynomial.coefficients must be a nonempty list")
    coefficients: dict[int, Quadratic] = {}
    for index, entry in enumerate(entries):
        entry_obj = _strict_object(
            entry, {"degree", "coefficient"}, f"polynomial.coefficients[{index}]"
        )
        degree = entry_obj["degree"]
        if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
            raise WitnessError(
                f"polynomial coefficient degree {degree!r} is not a nonnegative integer"
            )
        if degree in coefficients:
            raise WitnessError(f"duplicate polynomial degree {degree}")
        if degree % 2:
            raise WitnessError(
                f"odd degree {degree} has a nonzero coefficient; polynomial is not even"
            )
        coefficient = parse_quadratic(
            entry_obj["coefficient"],
            radical,
            f"polynomial.coefficients[{index}].coefficient",
        )
        coefficients[degree] = coefficient
    if not any(not coefficient.is_zero for coefficient in coefficients.values()):
        raise WitnessError("polynomial is zero")
    return Polynomial(coefficients, radical)


def group_terms(
    terms: Iterable[tuple[ComplexQuadratic, ComplexQuadratic]]
) -> dict[ComplexQuadratic, ComplexQuadratic]:
    groups: dict[ComplexQuadratic, ComplexQuadratic] = {}
    for coefficient, exponent in terms:
        if exponent in groups:
            groups[exponent] = groups[exponent] + coefficient
        else:
            groups[exponent] = coefficient
    return groups


def verify_witness(value: dict[str, Any]) -> list[str]:
    top = _strict_object(
        value,
        {
            "schema_version",
            "theorem_id",
            "field",
            "a",
            "online_heights",
            "polynomial",
            "quartets",
        },
        "witness",
    )
    if top["schema_version"] != 1:
        raise WitnessError(f"unsupported schema_version {top['schema_version']!r}")
    if top["theorem_id"] != "I-gaussian-weil-no-collision":
        raise WitnessError(f"wrong theorem_id {top['theorem_id']!r}")

    field = _strict_object(top["field"], {"squarefree_radical"}, "field")
    radical = field["squarefree_radical"]
    if (
        isinstance(radical, bool)
        or not isinstance(radical, int)
        or radical < 1
        or (
            radical > 1
            and any(
                radical % prime == 0
                for prime in range(2, math.isqrt(radical) + 1)
            )
        )
    ):
        raise WitnessError(
            f"field.squarefree_radical {radical!r} is not a positive squarefree integer"
        )

    a = parse_quadratic(top["a"], radical, "a")
    if a.sign() <= 0:
        raise WitnessError("a must be positive")

    raw_gammas = top["online_heights"]
    if not isinstance(raw_gammas, list) or not raw_gammas:
        raise WitnessError("online_heights must be a nonempty list")
    gammas = [
        parse_quadratic(raw_gamma, radical, f"online_heights[{index}]")
        for index, raw_gamma in enumerate(raw_gammas)
    ]
    if any(gamma.sign() == 0 for gamma in gammas):
        raise WitnessError("every online height must be nonzero")
    gamma_squares = [gamma * gamma for gamma in gammas]
    if len(set(gamma_squares)) != len(gamma_squares):
        raise WitnessError("online heights do not have pairwise distinct squares")

    polynomial = parse_polynomial(top["polynomial"], radical)
    zero_imaginary = Quadratic.rational_in_field(Fraction(0), radical)

    raw_quartets = top["quartets"]
    if not isinstance(raw_quartets, list) or not raw_quartets:
        raise WitnessError("quartets must be a nonempty list")
    quartets: list[tuple[Quadratic, Quadratic]] = []
    for index, raw_quartet in enumerate(raw_quartets):
        quartet = _strict_object(raw_quartet, {"g", "delta"}, f"quartets[{index}]")
        g = parse_quadratic(quartet["g"], radical, f"quartets[{index}].g")
        delta = parse_quadratic(
            quartet["delta"], radical, f"quartets[{index}].delta"
        )
        if g.sign() <= 0:
            raise WitnessError(f"quartets[{index}].g must be positive")
        if delta.sign() == 0:
            raise WitnessError(f"quartets[{index}].delta must be nonzero")
        quartets.append((g, delta))

    checks: list[str] = []
    for index, gamma in enumerate(gammas):
        gamma_z = ComplexQuadratic(gamma, zero_imaginary)
        if polynomial.evaluate(gamma_z).is_zero:
            raise WitnessError(f"polynomial annihilates online_heights[{index}]")
    checks.append("online polynomial nonvanishing")

    reconstructed_terms: list[tuple[ComplexQuadratic, ComplexQuadratic]] = []
    expected_groups: dict[ComplexQuadratic, ComplexQuadratic] = {}
    all_exponents: list[ComplexQuadratic] = []

    for gamma in gammas:
        for sign in (1, -1):
            signed_gamma = gamma if sign == 1 else -gamma
            gamma_z = ComplexQuadratic(signed_gamma, zero_imaginary)
            online_value = polynomial.evaluate(gamma_z)
            exponent = (gamma_z * gamma_z).scale(-a)
            if exponent.imaginary.sign() != 0:
                raise WitnessError("online exponent is not real")
            reconstructed_terms.append((online_value, exponent))
        collapsed_gamma_z = ComplexQuadratic(gamma, zero_imaginary)
        online_value = polynomial.evaluate(collapsed_gamma_z)
        expected_groups[exponent] = online_value + online_value
        all_exponents.append(exponent)

    for index, (g, delta) in enumerate(quartets):
        z_plus = ComplexQuadratic(g, delta)
        z_minus = ComplexQuadratic(g, -delta)
        plus_value = polynomial.evaluate(z_plus)
        minus_value = polynomial.evaluate(z_minus)
        if plus_value.is_zero or minus_value.is_zero:
            raise WitnessError(f"polynomial annihilates quartets[{index}]")
        if plus_value != minus_value.conjugate():
            raise WitnessError(
                f"real even polynomial fails conjugation for quartets[{index}]"
            )
        plus_exponent = (z_plus * z_plus).scale(-a)
        minus_exponent = (z_minus * z_minus).scale(-a)
        if plus_exponent.imaginary.sign() == 0:
            raise WitnessError(
                f"quartets[{index}] off-line exponent is unexpectedly real"
            )
        if minus_exponent != plus_exponent.conjugate():
            raise WitnessError(
                f"quartets[{index}] off-line exponents are not conjugate"
            )
        for signed_g in (g, -g):
            for signed_delta in (delta, -delta):
                raw_z = ComplexQuadratic(signed_g, signed_delta)
                reconstructed_terms.append(
                    (polynomial.evaluate(raw_z), (raw_z * raw_z).scale(-a))
                )
        expected_groups[plus_exponent] = plus_value + plus_value
        expected_groups[minus_exponent] = minus_value + minus_value
        all_exponents.extend((plus_exponent, minus_exponent))

    if len(set(all_exponents)) != len(all_exponents):
        raise WitnessError("observation exponents are not distinct")

    reconstructed_groups = group_terms(reconstructed_terms)
    if reconstructed_groups != expected_groups:
        raise WitnessError(
            "reconstructed observation does not match the collapsed formula"
        )
    checks.extend(
        [
            "even polynomial membership",
            "distinct algebraic exponents",
            "on-line pair collapse",
            "off-line quartet collapse",
        ]
    )
    return checks


def verify_path(path: Path) -> list[str]:
    return verify_witness(load_witness(path))


def main(argv: list[str] | None = None) -> int:
    default_witness = (
        Path(__file__).resolve().parents[1]
        / "witness"
        / "gaussian_hermite_witness_v1.json"
    )
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("witness", nargs="?", default=default_witness, type=Path)
    args = parser.parse_args(argv)
    try:
        checks = verify_path(args.witness)
    except (WitnessError, TypeError, ValueError) as exc:
        print(f"FAIL: {exc}", flush=True)
        return 1
    for check in checks:
        print(f"PASS: {check}", flush=True)
    print("PASS: exact Theorem I finite-witness replay", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
