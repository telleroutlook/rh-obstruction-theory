#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

STEP (1) as an EXACT ALGEBRAIC IDENTITY (§6as) — prove the §6an Vandermonde reduction outright.

§6an found (p-adically, CORR=0) v_p(det A) = sum_{k<l} v_p(x_k - x_l) for odd p, with A_{j,k}=4(1-T_j(x_k)),
j,k=1..m.  Here we test the STRONGER exact-rational closed form that would PROVE it:

    CLAIM:  det[ 4(1 - T_j(x_k)) ]_{j,k=1..m}  =  4^m * (-1)^m * 2^{m(m-1)/2}
                                                 * prod_k (x_k - 1) * prod_{k<l} (x_l - x_k).

REASONING (to be certified by this exact test).  1 - T_j(x) has degree j and leading coeff -2^{j-1}, and
VANISHES at x=1 (since T_j(1)=1), so 1 - T_j(x) = (x-1) q_j(x) with deg q_j = j-1, leadcoeff q_j = -2^{j-1}.
Hence det[1 - T_j(x_k)] = (prod_k (x_k - 1)) * det[q_j(x_k)], and {q_j}_{j=1..m} is a graded basis (degrees
0..m-1, leading coeffs -2^{j-1}), so det[q_j(x_k)] = (prod_j -2^{j-1}) * Vandermonde(x) =
(-1)^m 2^{m(m-1)/2} prod_{k<l}(x_l - x_k).  The 4^m is the per-row factor.

If LHS == RHS EXACTLY (as Fractions) for all tested node sets, step (1) is a PROVEN algebraic identity, and
the §6an p-adic statement follows.  Taking v_p (odd p): v_p(det A) = sum_k v_p(x_k - 1) + sum_{k<l} v_p(x_l -
x_k) (the 4^m, 2^{...} are odd-p units).  This probe ALSO reports sum_k v_p(x_k - 1) for p=3,5,17 to explain
WHY §6an's integer det had CORR=0: x_k - 1 = -2/(4 t_k^2 + 1), and the cleared_columns integer normalization
(multiplying column k to clear its denominator) exactly cancels the sum_k v_p(x_k - 1) term.  Exact
arithmetic (L9).  Honest (L5): a single exact mismatch REFUTES the closed form.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random


def cheb_T(j, x):
    """Chebyshev T_j(x) exact via recurrence."""
    if j == 0:
        return Fr(1)
    a, b = Fr(1), x       # T_0, T_1
    for _ in range(2, j + 1):
        a, b = b, 2 * x * b - a
    return b if j >= 1 else a


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


def frac_det(M):
    """Exact determinant of a list-of-rows Fraction matrix via fraction-free-ish Gaussian elimination."""
    n = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for i in range(n):
        piv = None
        for r in range(i, n):
            if A[r][i] != 0:
                piv = r; break
        if piv is None:
            return Fr(0)
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            det = -det
        det *= A[i][i]
        inv = A[i][i]
        for r in range(i + 1, n):
            if A[r][i] != 0:
                f = A[r][i] / inv
                for c in range(i, n):
                    A[r][c] -= f * A[i][c]
    return det


def lhs_det(ts, m):
    xs = [x_of(t) for t in ts]
    M = [[4 * (1 - cheb_T(j, xs[k])) for k in range(m)] for j in range(1, m + 1)]
    return frac_det(M)


def rhs_closed(ts, m):
    xs = [x_of(t) for t in ts]
    prod_xm1 = Fr(1)
    for xk in xs:
        prod_xm1 *= (xk - 1)
    vdm = Fr(1)
    for k in range(m):
        for l in range(k + 1, m):
            vdm *= (xs[l] - xs[k])
    two_pow = Fr(2) ** (m * (m - 1) // 2)
    return (Fr(4) ** m) * ((-1) ** m) * two_pow * prod_xm1 * vdm


def vp_frac(fr, p):
    if fr == 0:
        return 10**9
    n, d = fr.numerator, fr.denominator
    v = 0
    while n % p == 0:
        n //= p; v += 1
    while d % p == 0:
        d //= p; v -= 1
    return v


if __name__ == "__main__":
    print("=" * 94, flush=True)
    print("STEP (1) EXACT IDENTITY (§6as): det[4(1-T_j(x_k))] =? 4^m (-1)^m 2^{m(m-1)/2} prod(x_k-1) Vdm(x).", flush=True)
    print("If LHS==RHS exactly for all node sets, step (1) is a PROVEN algebraic identity (=> §6an p-adic).", flush=True)
    print("=" * 94, flush=True)
    rng = random.Random(20260816)
    all_ok = True
    print(f"\n{'m':>3} | {'config':>18} | {'LHS==RHS (exact)':>16} | {'sum_k v_p(x_k-1) p=3,5,17':>28}", flush=True)
    print("-" * 78, flush=True)
    for m in range(2, 9):
        for rep in range(3):
            ts = rng.sample(range(1, 200), m)
            if len(set(ts)) != m:
                continue
            L = lhs_det(ts, m)
            R = rhs_closed(ts, m)
            ok = (L == R)
            all_ok = all_ok and ok
            xs = [x_of(t) for t in ts]
            sums = {p: sum(vp_frac(xk - 1, p) for xk in xs) for p in (3, 5, 17)}
            tag = ",".join(str(t) for t in ts)
            if len(tag) > 18:
                tag = tag[:15] + "..."
            print(f"{m:>3} | {tag:>18} | {str(ok):>16} | "
                  f"p3={sums[3]:>3} p5={sums[5]:>3} p17={sums[17]:>3}", flush=True)
    # targeted: pick t with 4t^2+1 divisible by 5 (t=+-1 mod 5) to show sum_k v_5(x_k-1) != 0 yet identity holds
    print("\ntargeted (t chosen so 5 | 4t^2+1, i.e. sum_k v_5(x_k-1) < 0) -- identity must STILL hold exactly:",
          flush=True)
    ts5 = [1, 4, 6, 9]     # 4t^2+1 = 5,65,145,325 all divisible by 5
    m5 = len(ts5)
    L, R = lhs_det(ts5, m5), rhs_closed(ts5, m5)
    v5 = sum(vp_frac(x_of(t) - 1, 5) for t in ts5)
    print(f"    ts={ts5}: LHS==RHS = {L == R};  sum_k v_5(x_k-1) = {v5} (nonzero => extra term is real)",
          flush=True)
    all_ok = all_ok and (L == R)
    print("\n" + "=" * 94, flush=True)
    print(f"ALL EXACT MATCHES: {all_ok}", flush=True)
    print("READING (L5): if ALL matches True, step (1) is a PROVEN exact algebraic identity (Vandermonde via", flush=True)
    print("graded basis {q_j}, with 1-T_j = (x-1) q_j since T_j(1)=1). Then v_p(det A) = sum_k v_p(x_k-1) +", flush=True)
    print("sum_{k<l} v_p(x_l-x_k) for odd p; §6an's integer-det CORR=0 is because cleared_columns cancels the", flush=True)
    print("sum_k v_p(x_k-1) term (x_k-1 = -2/(4t^2+1)). A single mismatch REFUTES the closed form. RH [OUT].", flush=True)
