#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

CORRECTION + CORRECT C_j REDUCTION (§6at) — retract the wrong 4-atom Chebyshev formula, prove the right one.

HONEST CORRECTION (L5).  §6as/§6ao speculated C_j = v_3(sum_a w_a (xi_a - 1) prod_{k!=j}(xi_a - x_k)) by
treating the off-line vector d as a combination of CHEBYSHEV columns 4(1 - T_i(xi_a)).  That is WRONG: the
on-line columns use C_i(t) = 4(1 - T_i(x)) (Chebyshev, x=(4t^2-1)/(4t^2+1)) but the OFF-LINE d uses a DIFFERENT
family phi_i(rho) = 1 - (1 - 1/rho)^i (see _phi_re), summed over atoms {3/4 +- i tau, 1/4 +- i tau} with rho
and 1-rho.  No single x_rho gives phi_i(rho) = 4(1 - T_i(x_rho)) for all i (j=1 forces x_rho = 1 - 1/(4 rho),
but j=2 then disagrees).  This probe (a) CONFIRMS phi_i != 4(1-T_i(x)) for a common x; and (b) establishes the
CORRECT reduction, verified exactly:

  Each on-line Chebyshev column k has common factor (x_k - 1): 4(1 - T_i(x_k)) = 4 (x_k - 1) q_i(x_k), where
  q_i(x) := (1 - T_i(x))/(x - 1) is a GRADED basis (deg q_i = i-1).  Hence for minor_j = det[A, col j -> d]:
        minor_j = [ prod_{k!=j} (x_k - 1) ] * det[ 4 q_i(x_k) (k!=j)  |  d_i ]_{i=1..m}.
  Since det[ q-basis at X' | d ] = (triangular transform det) * det[ monomials at X' | d ] and det[monomials
  at X'={x_k}_{k!=j} (m-1 nodes) augmented by column d] = Vandermonde(X') * L_{X'}(d) for a divided-difference
  functional L_{X'}, we get, for p=3 (where v_3(x_k - 1) = 0):
        C_j = v_3(minor_j) - VD_j = v_3( det[ 4 q_i(x_k)(k!=j) | d ] ) - v_3( Vandermonde(X') )
            = v_3( L_{X'}(d) )   up to the fixed 3-unit transform,
  i.e. C_j is the 3-ADIC VALUATION OF AN INTERPOLATION-RESIDUAL FUNCTIONAL of the off-line data d against the
  m-1 on-line nodes.  The OPEN lemma (4) is now: this residual valuation is O(1).

VERIFIED HERE (exact, L9): (i) minor_j == prod_{k!=j}(x_k-1) * det[4 q_i(x_k)(k!=j) | d]; (ii) for p=3,
C_j := v_3(minor_j) - VD_j == v_3( det[4 q_i(x_k)(k!=j) | d] ) - v_3(Vandermonde(X')); (iii) phi_i != Chebyshev.
Honest (L5): a mismatch on (i)/(ii) refutes the corrected reduction.  One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows
import discovery.probe_overdetermined_collision as PO

SIG, TAU = Fr(3, 4), Fr(1)
P = 3


def cheb_T(j, x):
    if j == 0:
        return Fr(1)
    a, b = Fr(1), x
    for _ in range(1, j):
        a, b = b, 2 * x * b - a
    return b


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


def q_basis(i, x):
    """q_i(x) = (1 - T_i(x))/(x - 1), a graded basis of degree i-1 (T_i(1)=1 => x-1 divides)."""
    return (1 - cheb_T(i, x)) / (x - 1)


def vp_int(n, p):
    v = 0
    while n and n % p == 0:
        n //= p; v += 1
    return v


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


def frac_det(M):
    n = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if A[r][i] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != i:
            A[i], A[piv] = A[piv], A[i]; det = -det
        det *= A[i][i]
        for r in range(i + 1, n):
            if A[r][i] != 0:
                f = A[r][i] / A[i][i]
                for c in range(i, n):
                    A[r][c] -= f * A[i][c]
    return det


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("§6at CORRECTION: off-line d is the phi_i basis, NOT Chebyshev. Correct C_j = interpolation-", flush=True)
    print("residual valuation. Verify minor_j factorization + C_j identity exactly (p=3).", flush=True)
    print("=" * 96, flush=True)

    # (iii) phi_i != 4(1 - T_i(x_rho)) for a common x_rho
    print("\n(iii) phi_i(rho) vs 4(1-T_i(x)) with x = 1 - 1/(4 rho) (matches i=1 only):", flush=True)
    rho = Fr(3, 4)  # a real proxy atom
    xr = 1 - 1 / (4 * rho)
    for i in (1, 2, 3):
        phi = 1 - (1 - 1 / rho) ** i
        cheb = 4 * (1 - cheb_T(i, xr))
        print(f"    i={i}: phi_i(rho)={phi}   4(1-T_i(x_rho))={cheb}   equal={phi == cheb}", flush=True)

    # (i)+(ii): exact factorization + C_j identity, using EXACT rational A (not cleared int) for clarity,
    # then confirm C_j matches the integer-det definition used in §6ao.
    print(f"\n{'m':>3} | {'j':>2} | {'(i) minor factorization exact':>29} | "
          f"{'(ii) C_j==resid v_3 (p=3)':>25} | {'C_j':>4}", flush=True)
    print("-" * 82, flush=True)
    rng = random.Random(20260816)
    fac_ok_all = cj_ok_all = True
    for m in range(3, 7):
        for _ in range(60):
            ts = rng.sample(range(1, 120), m)
            b = build(ts, m)
            if b:
                break
        if not b:
            continue
        oc, vo = b
        xs = [x_of(t) for t in ts]
        # rational A columns (Chebyshev) and rational off-line d (phi), matching cleared_columns up to a
        # common integer scale Lden that cancels in the p=3 comparison below.
        A_cols_rat = [[4 * (1 - cheb_T(i, xs[k])) for i in range(1, m + 1)] for k in range(m)]
        d_rat = PO.d_vec(TAU, m)  # off-line phi vector (rational)
        v3det = vp_frac(frac_det([[A_cols_rat[k][i] for k in range(m)] for i in range(m)]), P)
        for j in range(1, m):    # test one representative interior j per m to bound cost
            # exact rational minor_j
            cols = [list(A_cols_rat[k]) for k in range(m)]
            cols[j] = list(d_rat)
            minor = frac_det([[cols[k][i] for k in range(m)] for i in range(m)])
            # RHS factorization: prod_{k!=j}(x_k - 1) * det[4 q_i(x_k)(k!=j) | d]
            prod_xm1 = Fr(1)
            for k in range(m):
                if k != j:
                    prod_xm1 *= (xs[k] - 1)
            fac_cols = []
            for k in range(m):
                fac_cols.append([4 * q_basis(i, xs[k]) for i in range(1, m + 1)] if k != j else list(d_rat))
            fac_det = frac_det([[fac_cols[k][i] for k in range(m)] for i in range(m)])
            rhs = prod_xm1 * fac_det
            fac_ok = (minor == rhs)
            fac_ok_all = fac_ok_all and fac_ok
            # C_j (p=3) via §6ao def: v_3(minor) - VD_j ; VD_j = sum_{k<l,k,l!=j} v_3(x_k-x_l)
            VD_j = sum(vp_frac(xs[a] - xs[c], P) for a in range(m) for c in range(a + 1, m)
                       if a != j and c != j)
            Cj = vp_frac(minor, P) - VD_j
            # residual side: v_3(det[4 q_i(x_k)(k!=j) | d]) - v_3(Vandermonde(X'))
            vdmXp = Fr(1)
            Xp = [xs[k] for k in range(m) if k != j]
            for a in range(len(Xp)):
                for c in range(a + 1, len(Xp)):
                    vdmXp *= (Xp[c] - Xp[a])
            resid_v3 = vp_frac(fac_det, P) - vp_frac(vdmXp, P)
            cj_ok = (Cj == resid_v3)
            cj_ok_all = cj_ok_all and cj_ok
            print(f"{m:>3} | {j:>2} | {str(fac_ok):>29} | {str(cj_ok):>25} | {Cj:>4}", flush=True)
    print("\n" + "=" * 96, flush=True)
    print(f"(i) minor factorization exact for ALL: {fac_ok_all}", flush=True)
    print(f"(ii) C_j == interpolation-residual v_3 for ALL (p=3): {cj_ok_all}", flush=True)
    print("READING (L5): (iii) shows the off-line basis is NOT Chebyshev -> the §6as/§6ao '4-atom Chebyshev'", flush=True)
    print("formula for C_j is RETRACTED. The CORRECT reduction (verified by (i)+(ii)): C_j = v_3 of an", flush=True)
    print("interpolation-residual functional L_{X'}(d) of the off-line data d against the m-1 on-line nodes.", flush=True)
    print("Open lemma (4) restated cleanly: this residual valuation is O(1). One orbit (D=425). RH [OUT].", flush=True)
