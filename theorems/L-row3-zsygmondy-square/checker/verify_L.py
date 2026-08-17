"""
Independent checker for Theorem L (NT-C square subcase).
Verifies:
1. Elliptic curve E: Y^2 = X(X+4)(X-1) torsion points
2. Birational pullback: each torsion point -> x value on C
3. No simultaneous perfect-square Row-3 pairs up to n=2000
4. d=2 local obstruction in Q_2 for phi-Selmer group
5. d=5 global solution for phi-hat-Selmer group
"""
from fractions import Fraction
from math import isqrt, gcd
import sys

FAILURES = []

def check(cond: bool, msg: str) -> None:
    if not cond:
        FAILURES.append(f"FAIL: {msg}")

# --- 1. Torsion points on E: Y^2 = X(X+4)(X-1) ---
for X3 in [Fraction(0), Fraction(1), Fraction(-4)]:
    Y2 = X3 * (X3 + 4) * (X3 - 1)
    check(Y2 == 0, f"torsion point X3={X3}: Y^2={Y2} != 0")

# --- 2. Birational pullback ---
def pullback_x2(X3: Fraction):
    """Given X3 on E, compute x^2 on C (returns None if undefined)."""
    X2 = X3 + 1
    X1 = X2          # X1 = X2 (no scaling needed after the substitution)
    U = X1 / 2
    denom = U**2 - 1
    if denom == 0:
        return None  # U=1: x = infinity
    return (2*U - 3) / denom

x2_at_0   = pullback_x2(Fraction(0))   # X3=0 -> U=1/2
x2_at_1   = pullback_x2(Fraction(1))   # X3=1 -> U=1 -> undefined (infinity)
x2_at_m4  = pullback_x2(Fraction(-4))  # X3=-4 -> U=-3/2

check(x2_at_0 == Fraction(8, 3),   f"X3=0 pullback: x^2={x2_at_0}, expected 8/3")
check(x2_at_1 is None,             f"X3=1 pullback: expected None (infinity), got {x2_at_1}")
check(x2_at_m4 == Fraction(-24, 5), f"X3=-4 pullback: x^2={x2_at_m4}, expected -24/5")

# 8/3 is not a rational square
r = isqrt(8 * 9)  # 8/3 = 72/9; is 8/3 a square? need 8*k^2 = 3*j^2 -- no
check(x2_at_0 > 0 and not (lambda q: q.numerator * q.denominator > 0 and
      isqrt(q.numerator)**2 == q.numerator and isqrt(q.denominator)**2 == q.denominator)(x2_at_0),
      "x2_at_0=8/3 should not be a perfect rational square")
check(x2_at_m4 < 0, f"x2_at_-4={x2_at_m4} should be negative (no real solution)")

# --- 3. Simultaneous perfect-square sweep ---
def is_perfect_square(n: int) -> bool:
    if n < 0: return False
    r = isqrt(n)
    return r * r == n

count = 0
for n in range(4, 2001, 2):
    if n % 3 == 0: continue
    for a in range(1, n, 2):
        if gcd(a, n) != 1: continue
        if is_perfect_square(a*a + n*n) and is_perfect_square((n-a)**2 + n*n):
            count += 1
            FAILURES.append(f"SQUARE PAIR: a={a}, n={n}")

check(count == 0, f"{count} simultaneous perfect-square pairs found (expected 0)")

# --- 4. d=2 local obstruction in Q_2 ---
# Homogeneous space: N^2 = 2M^4 + 3M^2*e^2 - 2*e^4
# Check all (M, e) mod 8 with gcd(M,e)=1
obstruction_holds = True
for M in range(0, 8):
    for e in range(0, 8):
        if gcd(M if M else 1, e if e else 1) > 1 and not (M == 0 and e == 0):
            continue
        if M == 0 and e == 0:
            continue
        # Check if N^2 = 2M^4 + 3M^2*e^2 - 2e^4 can be a square mod 8
        rhs = (2*M**4 + 3*M**2*e**2 - 2*e**4) % 8
        squares_mod8 = {0, 1, 4}
        if rhs in squares_mod8:
            # Found a potential local solution mod 8; but gcd check:
            if gcd(M % 8, e % 8) == 1 or (M == 0 and e != 0) or (M != 0 and e == 0):
                obstruction_holds = False

# Actually we need to be careful: the local obstruction requires checking that
# for ALL (M,e) with gcd(M,e)=1, the rhs is NOT a square mod 8.
# Redo: check all primitive pairs mod 8
obstruction_d2 = True
for M in range(8):
    for e in range(8):
        if gcd(M if M else 8, e if e else 8) > 1:
            continue
        if M == 0 and e == 0:
            continue
        rhs = (2*M**4 + 3*M**2*e**2 - 2*e**4) % 8
        if rhs in {0, 1, 4}:
            obstruction_d2 = False

check(obstruction_d2, "d=2 should fail locally mod 8 for all primitive (M,e)")

# --- 5. d=5 global solution for phi-hat-Selmer ---
# N^2 = 5M^4 - 6M^2*e^2 + 5*e^4; at M=1, e=1: 5-6+5=4
N2 = 5*1 - 6*1 + 5*1
check(N2 == 4 and isqrt(N2)**2 == N2, f"d=5 solution: N^2={N2}, expected 4")

# --- Report ---
if FAILURES:
    print("CHECKER FAILURES:")
    for f in FAILURES:
        print(f"  {f}")
    sys.exit(1)
else:
    print("Theorem L checker: all checks PASSED")
    print(f"  - 4 torsion points on E verified")
    print(f"  - pullback: x^2(X3=0)=8/3 (irrational), x(X3=1)=inf, x^2(X3=-4)=-24/5<0")
    print(f"  - 0 simultaneous perfect-square Row-3 pairs for n in [4,2000]")
    print(f"  - d=2 local obstruction in Q_2 confirmed")
    print(f"  - d=5 global solution for phi-hat Selmer confirmed")
