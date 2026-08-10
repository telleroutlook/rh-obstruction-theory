#!/usr/bin/env python3
"""
Discovery-tier: symbolic Jacobian analysis for Theorem B2.

Compute J_{jk} = phi_j(1/2 + i*t_k) + phi_j(1/2 - i*t_k) for Li-type and
moment-type test families at rational heights t_k.  Check det(J) != 0 via
EXACT rational arithmetic (Python's built-in Fraction).

This is discovery tier (program §12.1): conjectures only, never imported
into proof steps or theorem witnesses.

Run: python3 discovery/jacobian_analysis.py
"""
from __future__ import annotations
from fractions import Fraction
import sys

# ---------------------------------------------------------------------------
# Exact rational complex arithmetic (no third-party deps)
# ---------------------------------------------------------------------------

class RatComplex:
    """Exact complex number with Fraction real and imaginary parts."""
    __slots__ = ("r", "i")

    def __init__(self, r: Fraction | int, i: Fraction | int = 0):
        self.r = Fraction(r)
        self.i = Fraction(i)

    def __add__(self, other: "RatComplex") -> "RatComplex":
        return RatComplex(self.r + other.r, self.i + other.i)

    def __sub__(self, other: "RatComplex") -> "RatComplex":
        return RatComplex(self.r - other.r, self.i - other.i)

    def __mul__(self, other: "RatComplex") -> "RatComplex":
        return RatComplex(self.r*other.r - self.i*other.i,
                          self.r*other.i + self.i*other.r)

    def __truediv__(self, other: "RatComplex") -> "RatComplex":
        denom = other.r*other.r + other.i*other.i
        if denom == 0:
            raise ZeroDivisionError
        return RatComplex((self.r*other.r + self.i*other.i) / denom,
                          (self.i*other.r - self.r*other.i) / denom)

    def __neg__(self) -> "RatComplex":
        return RatComplex(-self.r, -self.i)

    def conj(self) -> "RatComplex":
        return RatComplex(self.r, -self.i)

    def __pow__(self, n: int) -> "RatComplex":
        if n == 0:
            return RatComplex(1)
        result = RatComplex(1)
        base = self
        while n > 0:
            if n % 2 == 1:
                result = result * base
            base = base * base
            n //= 2
        return result

    def __repr__(self) -> str:
        return f"({self.r} + {self.i}i)"

    def real_part(self) -> Fraction:
        return self.r


ONE = RatComplex(1)
HALF = RatComplex(Fraction(1, 2))


# ---------------------------------------------------------------------------
# Test functions
# ---------------------------------------------------------------------------

def li_test(j: int, rho: RatComplex) -> RatComplex:
    """Li-type: phi_j(rho) = 1 - (1 - 1/rho)^j."""
    inv_rho = ONE / rho
    return ONE - (ONE - inv_rho)**j


def moment_test(k: int, rho: RatComplex) -> RatComplex:
    """Moment-type: phi_k(rho) = rho^{-k} (real part of sum is used)."""
    return ONE / (rho**k)


def symmetrized(phi_fn, j_or_k: int, t: Fraction) -> Fraction:
    """
    Compute A = phi(1/2 + it) + phi(1/2 - it).
    For Li and moment tests this equals 2 * Re[phi(1/2 + it)].
    """
    rho_plus  = RatComplex(Fraction(1, 2),  t)
    rho_minus = RatComplex(Fraction(1, 2), -t)
    val = phi_fn(j_or_k, rho_plus) + phi_fn(j_or_k, rho_minus)
    # imaginary part should cancel
    assert abs(val.i) < Fraction(1, 10**15), f"Im part nonzero: {val.i}"
    return val.r


# ---------------------------------------------------------------------------
# Jacobian matrix (exact rational)
# ---------------------------------------------------------------------------

def build_jacobian(phi_fn, indices: list[int], heights: list[Fraction]) -> list[list[Fraction]]:
    """
    J[j][k] = phi_{indices[j]}(1/2+it_k) + phi_{indices[j]}(1/2-it_k)
    Returns J as list of lists (row-major).
    """
    m = len(indices)
    n = len(heights)
    J = [[Fraction(0)] * n for _ in range(m)]
    for j, idx in enumerate(indices):
        for k, t in enumerate(heights):
            J[j][k] = symmetrized(phi_fn, idx, t)
    return J


def det_rat(M: list[list[Fraction]]) -> Fraction:
    """Exact determinant of a square rational matrix via Bareiss algorithm."""
    n = len(M)
    A = [row[:] for row in M]  # copy
    sign = 1
    for col in range(n):
        # find pivot
        pivot_row = None
        for row in range(col, n):
            if A[row][col] != 0:
                pivot_row = row
                break
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != col:
            A[col], A[pivot_row] = A[pivot_row], A[col]
            sign *= -1
        pivot = A[col][col]
        for row in range(col + 1, n):
            factor = A[row][col] / pivot
            for c in range(col, n):
                A[row][c] -= factor * A[col][c]
    d = Fraction(sign)
    for i in range(n):
        d *= A[i][i]
    return d


def print_matrix(label: str, M: list[list[Fraction]]) -> None:
    print(f"\n{label}:")
    for row in M:
        print("  [" + "  ".join(f"{v}" for v in row) + "]")


# ---------------------------------------------------------------------------
# Main: run analysis for m=3, n=3 with rational heights
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("B2 Jacobian analysis (discovery tier, exact rational)")
    print("=" * 60)
    print("NOTE: results are DISCOVERY TIER (conjecture only).")
    print("      Do NOT import into proof steps or theorem witnesses.")
    print()

    # Heights: small rational values
    heights_3 = [Fraction(1, 2), Fraction(1, 1), Fraction(3, 2)]
    heights_5 = [Fraction(1, 2), Fraction(1, 1), Fraction(3, 2),
                 Fraction(2, 1), Fraction(5, 2)]

    # ---- Li-type tests, indices j=1,2,3,4,5 (square matrices only) ----
    print("=== Li-type tests: phi_j(rho) = 1 - (1 - 1/rho)^j ===")
    for m, heights in [(3, heights_3), (5, heights_5)]:
        idxs = list(range(1, m+1))
        hs = heights[:m]
        J = build_jacobian(li_test, idxs, hs)
        print_matrix(f"J_Li (m={m}, heights={[str(h) for h in hs]})", J)
        d = det_rat(J)
        print(f"  det(J_Li, m={m}) = {d}  {'!= 0 -> FULL RANK' if d != 0 else '== 0 -> SINGULAR'}")

    # ---- Moment-type tests, k=1,2,3,4 (square matrices only) ----
    print("\n=== Moment-type tests: phi_k(rho) = rho^{-k} ===")
    for m, heights in [(3, heights_3), (4, heights_5[:4])]:
        idxs = list(range(1, m+1))
        hs = heights[:m]
        J = build_jacobian(moment_test, idxs, hs)
        print_matrix(f"J_moment (m={m}, heights={[str(h) for h in hs]})", J)
        d = det_rat(J)
        print(f"  det(J_moment, m={m}) = {d}  {'!= 0 -> FULL RANK' if d != 0 else '== 0 -> SINGULAR'}")

    # ---- Li heights sensitivity: try different t_k ----
    print("\n=== Li m=3: vary heights ===")
    test_sets = [
        [Fraction(1,4), Fraction(1,2), Fraction(3,4)],
        [Fraction(1,3), Fraction(2,3), Fraction(1,1)],
        [Fraction(1,10), Fraction(1,5), Fraction(3,10)],
        [Fraction(2,1), Fraction(3,1), Fraction(5,1)],
    ]
    idxs = [1, 2, 3]
    for hs in test_sets:
        J = build_jacobian(li_test, idxs, hs)
        d = det_rat(J)
        print(f"  t={[str(h) for h in hs]}  det={d}  {'FULL RANK' if d != 0 else 'SINGULAR'}")

    # ---- Summary ----
    print()
    print("=" * 60)
    print("Summary (DISCOVERY TIER — conjecture only):")
    print("  If det(J) != 0 for specific heights, the Jacobian is")
    print("  generically nonsingular. This MOTIVATES the rank conjecture")
    print("  in proof.md §4 but does not prove it analytically.")
    print("  The analytic proof of generic full rank is still OPEN.")
    print("=" * 60)


if __name__ == "__main__":
    main()
