#!/usr/bin/env python3
"""Exact structural checks and finite scan for the OB-44A reduction.

The scan factors the two quadratic factors of N rather than N itself. It is
deterministic exact arithmetic and finite sanity evidence only, not a proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt

import argparse


@dataclass(frozen=True)
class ScanStats:
    pairs: int
    powerful_n: int
    no_simple_prime: int
    plus_powerful_away_from_5: int
    minus_powerful_away_from_5: int
    simultaneous_powerful_away_from_5: int


def sieve(limit: int) -> list[int]:
    """Return primes <= limit using a bytearray sieve."""
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for value in range(2, isqrt(limit) + 1):
        if is_prime[value]:
            start = value * value
            is_prime[start : limit + 1 : value] = b"\x00" * (
                (limit - start) // value + 1
            )
    return [value for value in range(limit + 1) if is_prime[value]]


def factorize(value: int, primes: list[int]) -> dict[int, int]:
    """Factor positive value using a prime list covering sqrt(value)."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: dict[int, int] = {}
    remaining = value
    for prime in primes:
        if prime * prime > remaining:
            break
        while remaining % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            remaining //= prime
    if remaining != 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def powerful(factors: dict[int, int], excluded: int = 1) -> bool:
    return all(
        exponent >= 2
        for prime, exponent in factors.items()
        if prime != excluded
    )


def scan(max_n: int = 1000) -> ScanStats:
    """Scan Row-3 pairs 1<=a<n with n even, 3∤n, and n<max_n."""
    if max_n < 5:
        raise ValueError("max_n must be at least 5")

    # For max_n=1000, both quadratic factors are below 2,000,000.
    maximum_factor = 2 * (max_n - 1) ** 2
    primes = sieve(isqrt(maximum_factor) + 1)
    if not primes:
        raise AssertionError("empty prime sieve")

    stats = ScanStats(0, 0, 0, 0, 0, 0)
    for n in range(4, max_n, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n, 2):
            if gcd(a, n) != 1:
                continue

            r = a * a + n * n - n * a
            n_value = r * r + n**4
            plus = a * a + n * n
            minus = (a - n) ** 2 + n * n
            if n_value != plus * minus:
                raise AssertionError("factorization identity failed")
            if gcd(plus, minus) not in (1, 5):
                raise AssertionError("gcd reduction failed")

            plus_factors = factorize(plus, primes)
            minus_factors = factorize(minus, primes)
            combined: dict[int, int] = dict(plus_factors)
            for prime, exponent in minus_factors.items():
                combined[prime] = combined.get(prime, 0) + exponent

            plus_bad = powerful(plus_factors, 5)
            minus_bad = powerful(minus_factors, 5)
            stats = ScanStats(
                pairs=stats.pairs + 1,
                powerful_n=stats.powerful_n + int(powerful(combined)),
                no_simple_prime=stats.no_simple_prime
                + int(all(value != 1 for value in combined.values())),
                plus_powerful_away_from_5=stats.plus_powerful_away_from_5
                + int(plus_bad),
                minus_powerful_away_from_5=stats.minus_powerful_away_from_5
                + int(minus_bad),
                simultaneous_powerful_away_from_5=(
                    stats.simultaneous_powerful_away_from_5
                    + int(plus_bad and minus_bad)
                ),
            )
    return stats


def check() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-n",
        type=int,
        choices=(1000, 5000),
        default=1000,
        help="upper exclusive bound for n (5000 takes about twenty seconds)",
    )
    arguments = parser.parse_args()
    print(f"Scanning Row-3 pairs with n<{arguments.max_n}...", flush=True)
    stats = scan(arguments.max_n)
    expected = {
        1000: ScanStats(75840, 0, 0, 127, 127, 0),
        5000: ScanStats(1898236, 0, 0, 633, 633, 0),
    }[arguments.max_n]
    if stats != expected:
        raise AssertionError(f"unexpected scan stats: {stats}")
    print(f"PASS: OB-44A factorization and gcd scan through n<{arguments.max_n}")
    print(
        "PASS: stats "
        f"(pairs, powerful_N, no_simple, A_bad, B_bad, simultaneous) = {stats}"
    )


if __name__ == "__main__":
    check()
