#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture only, NEVER imported into proof
steps or theorem witnesses.  No RH assumption, no RH-equivalent input; all
objects are finite explicit multisets of complex rationals.

Probe for Paper A **Open Problem 1** (arithmetic-information-barriers-rh.tex:1067):

    "Is there an exact information obstruction for O_fin^{(K(T))} that remains
     valid even as K = K(T) grows ... while satisfying a uniform bound
     #Z_± <= T^A on total atom count or denominator height?"

Restated as a measurable quantity.  Theorem A's exact-collision pipeline
(see theorems/B2-exact-collision/checker/b2_certified_checker.py) matches the
first m Li-observations of an ON-line multiset Z_+ (P=1) and an OFF-line
multiset Z_- (P=0).  Its SIZE is governed by:

    C_{jk} = O_j(L(t_k)) = 4(1 - T_j(x_k)),  x_k = (4 t_k^2 - 1)/(4 t_k^2 + 1)
    d_j    = O_j(Q),   Q = {3/4+-iT, 1/4+-iT}  (an off-line quartet)
    beta   = -C^{-1} d,   R = lcm of denominators of beta,   n_k = R*beta_k
    M      = max_k |n_k|,   #Z_+ = 2 m M,   #Z_- = 2 sum_k (M+n_k) + 4 R.

So the collision's atom-count / height cost is captured by (R, M, #Z).
THE QUESTION: how do R and M scale with m?
  * polynomial(m)      => the barrier SURVIVES a polynomial size budget
                          (a strictly stronger obstruction than Theorem A).
  * super-polynomial   => a polynomial budget #Z<=T^A DEFEATS the standard
                          collision (evidence toward a resource-bounded
                          SEPARATION theorem -- the complementary result).

CALIBRATION (L9): the m=2, t=(1,2), T=1 instance MUST reproduce the certified
anchor R=6375, M=14518 before any scaling number is trusted.

This file only measures the *standard* (m-node, m-equation) construction.
Whether an OVER-DETERMINED (K>m node) construction can achieve polynomial size
is the separate follow-up (probe_overdetermined_collision.py).
"""
from __future__ import annotations
from fractions import Fraction as Fr
import math


# --------------------------------------------------------------------------
# exact complex-rational arithmetic (self-contained; mirrors the checker)
# --------------------------------------------------------------------------
class CFrac:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = o if isinstance(o, CFrac) else CFrac(o)
        return CFrac(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, CFrac) else CFrac(o)
        return CFrac(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        if isinstance(o, CFrac):
            return CFrac(self.re * o.re - self.im * o.im,
                         self.re * o.im + self.im * o.re)
        return CFrac(self.re * o, self.im * o)

    __rmul__ = __mul__

    def recip(self):
        d = self.re * self.re + self.im * self.im
        assert d != 0
        return CFrac(self.re / d, -self.im / d)


ONE = CFrac(1, 0)


def cpow(z, j):
    p = CFrac(1, 0)
    for _ in range(j):
        p = p * z
    return p


def phi(j, rho):
    """phi_j(rho) = 1 - (1 - 1/rho)^j."""
    return ONE - cpow(ONE - rho.recip(), j)


def O(j, multiset):
    """O_j(Z) = sum_{rho in Z} mult * [phi_j(rho) + phi_j(1-rho)] (real)."""
    total = CFrac(0, 0)
    for atom, mult in multiset:
        total = total + mult * (phi(j, atom) + phi(j, ONE - atom))
    assert total.im == 0, f"O_{j} not real: im={total.im}"
    return total.re


def L(t):
    t = Fr(t)
    return [(CFrac(Fr(1, 2), t), 1), (CFrac(Fr(1, 2), -t), 1)]


def Qset(T):
    T = Fr(T)
    return [(CFrac(Fr(3, 4), T), 1), (CFrac(Fr(3, 4), -T), 1),
            (CFrac(Fr(1, 4), T), 1), (CFrac(Fr(1, 4), -T), 1)]


# --------------------------------------------------------------------------
# exact rational solve  C beta = d   (Fraction Gaussian elimination)
# --------------------------------------------------------------------------
def solve(Cmat, dvec):
    m = len(Cmat)
    A = [list(row) + [dvec[i]] for i, row in enumerate(Cmat)]
    det = Fr(1)
    sign = 1
    for col in range(m):
        piv = next((r for r in range(col, m) if A[r][col] != 0), None)
        if piv is None:
            return Fr(0), None
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            sign = -sign
        pv = A[col][col]
        det *= pv
        for r in range(col + 1, m):
            f = A[r][col] / pv
            if f:
                for c in range(col, m + 1):
                    A[r][c] -= f * A[col][c]
    det *= sign
    x = [Fr(0)] * m
    for i in range(m - 1, -1, -1):
        s = A[i][m] - sum(A[i][j] * x[j] for j in range(i + 1, m))
        x[i] = s / A[i][i]
    return det, x


# --------------------------------------------------------------------------
# the standard Theorem-A collision, returning its SIZE profile
# --------------------------------------------------------------------------
def construct(m, ts, T):
    ts = [Fr(t) for t in ts]
    Lsets = [L(t) for t in ts]
    Qs = Qset(T)
    Cmat = [[O(j, Lsets[k]) for k in range(m)] for j in range(1, m + 1)]
    dvec = [O(j, Qs) for j in range(1, m + 1)]
    det, x = solve(Cmat, dvec)
    assert det != 0, f"det C == 0 at m={m}"
    beta = [-xi for xi in x]                       # C beta = -d
    R = 1
    for b in beta:
        R = R * b.denominator // math.gcd(R, b.denominator)
    n = [int(R * b) for b in beta]
    for k in range(m):
        assert (R * beta[k]).denominator == 1
    M = max(abs(v) for v in n)
    # exact-collision residual check  C n + R d = 0
    for j in range(m):
        row = sum(Cmat[j][k] * n[k] for k in range(m)) + R * dvec[j]
        assert row == 0, f"collision residual nonzero at m={m}, j={j+1}"
    sum_abs_n = sum(abs(v) for v in n)
    Zplus = 2 * m * M
    Zminus = 2 * sum(M + nk for nk in n) + 4 * R
    return dict(m=m, det=det, R=R, M=M, sum_abs_n=sum_abs_n,
                Zplus=Zplus, Zminus=Zminus, n=n)


# --------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 72)
    print("Probe: resource cost of the STANDARD Theorem-A Li-collision vs m")
    print("DISCOVERY TIER (conjecture only; not a proof, not a witness).")
    print("=" * 72)

    # ---- CALIBRATION (L9): must reproduce the certified anchor ----
    a = construct(2, [1, 2], 1)
    assert a["R"] == 6375, f"CALIB FAIL R={a['R']}"
    assert a["M"] == 14518, f"CALIB FAIL M={a['M']}"
    assert a["n"] == [-7130, -14518], f"CALIB FAIL n={a['n']}"
    print("\nCALIBRATION m=2 t=(1,2) T=1 : R=6375, M=14518, n=[-7130,-14518]  -> PASS")

    # ---- scaling scan: t_k = 1..m, T = 1 ----
    print("\nStandard construction, t_k = 1..m, T = 1:")
    print(f"{'m':>3} | {'R':>22} | {'M = max|n_k|':>26} | "
          f"{'log2 M':>8} | {'#Z_-':>26}")
    print("-" * 100)
    prev_log = None
    rows = []
    for m in range(2, 12):
        r = construct(m, list(range(1, m + 1)), 1)
        log2M = math.log2(r["M"]) if r["M"] > 0 else 0.0
        ratio = f"{log2M - prev_log:+.2f}" if prev_log is not None else "  -  "
        rows.append((m, log2M))
        print(f"{m:>3} | {r['R']:>22} | {r['M']:>26} | "
              f"{log2M:>8.2f} | {r['Zminus']:>26}   dlog2={ratio}")
        prev_log = log2M

    # ---- growth diagnosis ----
    print("\nGrowth diagnosis (log2 M vs m):")
    # fit log2 M ~ a*m*log2(m) + b*m + c  crudely by successive differences
    print("  m, log2M, log2M/m, log2M/(m*log2 m):")
    for m, lg in rows:
        per_m = lg / m
        per_mlogm = lg / (m * math.log2(m)) if m > 1 else 0
        print(f"    m={m:>2}  log2M={lg:8.2f}  /m={per_m:6.2f}  "
              f"/(m log m)={per_mlogm:6.3f}")
    print("\n  If log2M grows ~linearly in m (per-m ratio ~const) => M ~ 2^{c m}")
    print("  => SUPER-POLYNOMIAL: standard construction violates any #Z<=T^A")
    print("     budget for K(T)=m growing with T.  (Motivates the")
    print("     over-determined-node follow-up for a polynomial construction.)")
