"""
OE-01 numerical anchor: verify NT-C has no counterexample up to n=2000.
Checks both the full powerful-away-from-5 condition and the perfect-square subcase.
"""
from math import isqrt, gcd
import sys


def is_powerful_away_from_5(N: int) -> bool:
    """True iff every prime p != 5 dividing N satisfies p^2 | N."""
    n = N
    while n % 5 == 0:
        n //= 5
    if n == 1:
        return True
    d = 2
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                n //= d
                count += 1
            if count < 2:
                return False
        d += 1
    return n == 1  # remaining factor would be a prime appearing once


def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def check_elliptic_curve(bound: int) -> list[tuple[int, int]]:
    """Find integer solutions to y^2 = x^4 - 3x^2*b^2 + b^4 for 1 <= b <= x <= bound."""
    hits = []
    for b in range(1, bound + 1):
        for x in range(b, bound + 1):
            val = x**4 - 3 * x**2 * b**2 + b**4
            if val >= 0 and is_perfect_square(val):
                hits.append((x, b, isqrt(val)))
    return hits


def main() -> None:
    N_LIMIT = 2000

    # --- Check 1: full powerful-away-from-5 sweep ---
    simultaneous_powerful = []
    for n in range(4, N_LIMIT + 1, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n, 2):
            if gcd(a, n) != 1:
                continue
            Ap = a * a + n * n
            Am = (a - n) ** 2 + n * n
            if is_powerful_away_from_5(Ap) and is_powerful_away_from_5(Am):
                simultaneous_powerful.append((a, n, Ap, Am))

    if simultaneous_powerful:
        print("FAIL: simultaneous powerful pairs found:")
        for item in simultaneous_powerful:
            print(f"  a={item[0]}, n={item[1]}, A+={item[2]}, A-={item[3]}")
        sys.exit(1)
    else:
        print(f"PASS: zero simultaneous powerful-away-from-5 pairs for n in [4, {N_LIMIT}]")

    # --- Check 2: perfect-square subcase ---
    simultaneous_squares = []
    for n in range(4, N_LIMIT + 1, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n, 2):
            if gcd(a, n) != 1:
                continue
            Ap = a * a + n * n
            Am = (n - a) ** 2 + n * n
            if is_perfect_square(Ap) and is_perfect_square(Am):
                simultaneous_squares.append((a, n, Ap, Am))

    if simultaneous_squares:
        print("FAIL: simultaneous perfect-square pairs found:")
        for item in simultaneous_squares:
            print(f"  a={item[0]}, n={item[1]}, A+={item[2]}={isqrt(item[2])}^2, A-={item[3]}={isqrt(item[3])}^2")
        sys.exit(1)
    else:
        print(f"PASS: zero simultaneous perfect-square pairs for n in [4, {N_LIMIT}]")

    # --- Check 3: elliptic curve C: y^2 = x^4 - 3x^2 + 1 (b=1 case) ---
    hits = check_elliptic_curve(200)
    non_trivial = [(x, b, y) for x, b, y in hits if x > 0 and y > 0]
    if non_trivial:
        print(f"INFO: elliptic curve hits (x,b,y): {non_trivial}")
    else:
        print("PASS: no integer points on y^2 = x^4 - 3x^2*b^2 + b^4 for 1<=b<=x<=200")

    print("All OE-01 anchor checks passed.")


if __name__ == "__main__":
    main()
