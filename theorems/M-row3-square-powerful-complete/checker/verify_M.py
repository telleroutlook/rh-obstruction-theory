"""
Theorem M checker: no Row-3 pair has both A+ and A- square-based powerful-away-from-5.
Also verifies the mod-8/16 obstruction arguments.
"""
from math import isqrt, gcd


def is_5e_sq(n: int) -> bool:
    """Return True if n = 5^e * m^2 for some e>=0, integer m."""
    while n % 5 == 0:
        n //= 5
    s = isqrt(n)
    return s * s == n


def verify_mod8_obstruction() -> None:
    squares_mod8 = {(x * x) % 8 for x in range(8)}
    five_sq_mod8 = {(5 * x * x) % 8 for x in range(8)}
    assert squares_mod8 == {0, 1, 4}, f"squares mod 8: {squares_mod8}"
    assert five_sq_mod8 == {0, 4, 5}, f"5m^2 mod 8: {five_sq_mod8}"
    assert 1 not in five_sq_mod8, "5m^2 ≡ 1 mod 8 should be impossible"
    print("  mod-8 obstruction verified: 5m^2 ∈ {0,4,5} mod 8, never 1")


def verify_mod16_obstruction() -> None:
    squares_mod16 = {(x * x) % 16 for x in range(16)}
    odd_sq_mod16 = {(x * x) % 16 for x in range(1, 16, 2)}
    five_odd_sq_mod16 = {(5 * x * x) % 16 for x in range(1, 16, 2)}
    ap_mod16 = {(a * a) % 16 for a in range(1, 16, 2)}  # a odd, 16k^2≡0
    assert squares_mod16 == {0, 1, 4, 9}, f"squares mod 16: {squares_mod16}"
    assert odd_sq_mod16 == {1, 9}, f"odd squares mod 16: {odd_sq_mod16}"
    assert ap_mod16 == {1, 9}, f"A+ mod 16 for 4|n: {ap_mod16}"
    assert five_odd_sq_mod16 == {5, 13}, f"5T^2 mod 16 (T odd): {five_odd_sq_mod16}"
    assert ap_mod16.isdisjoint(five_odd_sq_mod16), "Should not overlap"
    print("  mod-16 obstruction verified: A+≡{1,9} mod 16, 5T^2≡{5,13} mod 16 (T odd)")


def numerical_sweep(n_max: int = 3000) -> int:
    count = 0
    for n in range(4, n_max + 1, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n, 2):
            if gcd(a, n) != 1:
                continue
            Ap = a * a + n * n
            Am = (n - a) * (n - a) + n * n
            if is_5e_sq(Ap) and is_5e_sq(Am):
                count += 1
                print(f"  FOUND: a={a}, n={n}, A+={Ap}, A-={Am}")
    return count


def verify_casewise_mod8(n_max: int = 500) -> None:
    """Verify each case directly by checking A+ and A- mod 8."""
    for n in range(4, n_max + 1, 2):
        if n % 3 == 0:
            continue
        for a in range(1, n, 2):
            if gcd(a, n) != 1:
                continue
            Ap = a * a + n * n
            Am = (n - a) * (n - a) + n * n
            ap8, am8 = Ap % 8, Am % 8
            # Thm B (thm:mod4): 4|n → ≡1 mod 8; 4∤n → ≡5 mod 8
            if n % 4 == 0:
                assert ap8 == 1, f"Thm B violated: 4|n but A+={Ap}≡{ap8} mod 8, n={n},a={a}"
                assert am8 == 1, f"Thm B violated: 4|n but A-={Am}≡{am8} mod 8, n={n},a={a}"
            else:
                assert ap8 == 5, f"Thm B violated: 4∤n but A+={Ap}≡{ap8} mod 8, n={n},a={a}"
                assert am8 == 5, f"Thm B violated: 4∤n but A-={Am}≡{am8} mod 8, n={n},a={a}"
    print(f"  Theorem B mod-8 check PASS for all n≤{n_max}")


if __name__ == "__main__":
    print("Theorem M checker")
    print()
    print("1. Verifying mod-8 obstruction (5m^2 never ≡ 1 mod 8)...")
    verify_mod8_obstruction()

    print("2. Verifying mod-16 obstruction (for 4|n sub-family)...")
    verify_mod16_obstruction()

    print("3. Verifying Theorem B mod-8 congruences for n≤500...")
    verify_casewise_mod8(500)

    print("4. Numerical sweep n≤3000: checking for simultaneous 5^e*□ pairs...")
    count = numerical_sweep(3000)
    print(f"   {count} instances found")
    assert count == 0, f"Expected 0, found {count}"

    print()
    print("Theorem M checker: all checks PASSED")
    print("  - mod-8 obstruction: 5m^2 never ≡ 1 mod 8")
    print("  - mod-16 obstruction: A+≡{1,9} mod 16 disjoint from 5T^2≡{5,13} mod 16")
    print("  - Theorem B verified for n≤500")
    print("  - 0 simultaneous square-based powerful pairs found for n≤3000")
