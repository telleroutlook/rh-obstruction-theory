#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

C_j AS AN EXPLICIT BILINEAR FORM (§6au) — turn open lemma (4) into a cheap, large-m-testable statement.

From §6at: C_j = v_3(det[4 q_i(x_k)(k!=j) | d]) - v_3(Vandermonde(X')), q_i=(1-T_i)/(x-1) graded basis,
X' = {x_k}_{k!=j} (m-1 nodes).  Write 4 q_i(x) = sum_l B[i][l] x^l (B is m x m LOWER-TRIANGULAR, diagonal =
4*(-2^{i-1}) all 3-units, so v_3(det B)=0).  Then [node-cols | d] = B [monomials | w] with w := B^{-1} d
(a FIXED vector, independent of the nodes).  The augmented-Vandermonde identity
      det[ (x_k^l)_{l=0..m-1, k in X'} | w ] = Vandermonde(X') * sum_{i=0}^{m-1} (-1)^{m-1-i} e_{m-1-i}(X') w_i
gives the FULLY EXPLICIT reduction (for p=3, v_3(x_k-1)=0, v_3(det B)=0):
      C_j = v_3(  sum_{i=0}^{m-1} (-1)^{m-1-i} e_{m-1-i}(X') * w_i  ),   w = B^{-1} d,
i.e. the 3-adic valuation of a BILINEAR PAIRING of the fixed off-line vector w against the elementary
symmetric functions of the on-line nodes X'.  This probe:
  (a) VERIFIES this equals the §6at/§6ao C_j exactly (integer-det definition), m=3..7;
  (b) since (a)-form is CHEAP (no determinants: w once, e_l(X') by product, one dot product), ADVERSARIALLY
      MAXIMIZES C_j = v_3(pairing) over m=4..24 to test lemma (4): does max_j C_j stay O(1)?
Exact arithmetic (L9).  Honest (L5): (a) mismatch refutes the bilinear form; ascent = LOWER bound on max C_j.
One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows
import discovery.probe_overdetermined_collision as PO

SIG, TAU = Fr(3, 4), Fr(1)
P = 3


def cheb_T_poly(j):
    """T_j as coefficient list (low->high), exact."""
    if j == 0:
        return [Fr(1)]
    a, b = [Fr(1)], [Fr(0), Fr(1)]      # T_0=1, T_1=x
    for _ in range(2, j + 1):
        # b = 2x*b - a
        xb = [Fr(0)] + b
        nb = [2 * xb[l] - (a[l] if l < len(a) else 0) for l in range(len(xb))]
        a, b = b, nb
    return b


def q_poly(i):
    """4 q_i(x) = 4 (1 - T_i(x))/(x-1) as coeff list (degree i-1). Synthetic division by (x-1), root=1."""
    T = cheb_T_poly(i)
    # 1 - T_i : coeff list
    p = [-c for c in T]
    p[0] += 1                             # (1 - T_i), degree i, leading coeff -2^{i-1}
    # divide p(x) by (x - 1): synthetic division at root 1, exact (remainder must be 0 since p(1)=0)
    n = len(p) - 1                        # degree
    quo = [Fr(0)] * n                     # degree n-1
    carry = Fr(0)
    for d in range(n, 0, -1):             # from high degree down
        carry = p[d] + carry              # coeff of x^d plus carry
        quo[d - 1] = carry                # quotient coeff of x^{d-1}
    # remainder = p[0] + carry ; should be 0
    return [4 * c for c in quo]           # 4 q_i, degree i-1


def Bmatrix(m):
    """B[i][l] = coeff of x^l in 4 q_{i+1}(x), i,l = 0..m-1. Lower triangular (row i has support l<=i)."""
    B = [[Fr(0)] * m for _ in range(m)]
    for i in range(1, m + 1):
        qc = q_poly(i)                    # degrees 0..i-1
        for l, c in enumerate(qc):
            B[i - 1][l] = c
    return B


def solve_lower(B, d, m):
    """Solve B w = d for lower-triangular B (forward substitution). d indexed 0..m-1 (row i-1 <-> deg index)."""
    w = [Fr(0)] * m
    for i in range(m):
        s = d[i] - sum(B[i][l] * w[l] for l in range(i))
        w[i] = s / B[i][i]
    return w


def elem_sym(xs):
    """elementary symmetric e_0..e_n of list xs (n=len). e[k] returned for k=0..n."""
    e = [Fr(1)] + [Fr(0)] * len(xs)
    for x in xs:
        for k in range(len(xs), 0, -1):
            e[k] += e[k - 1] * x
    return e


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


def vp_int(n, p):
    v = 0
    while n and n % p == 0:
        n //= p; v += 1
    return v


def vp_frac(fr, p):
    if fr == 0:
        return 10**9
    n, dd = fr.numerator, fr.denominator
    v = 0
    while n % p == 0:
        n //= p; v += 1
    while dd % p == 0:
        dd //= p; v -= 1
    return v


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def Cj_bilinear(ts, m, j, B=None, w=None):
    """C_j via the explicit bilinear form: v_3( sum_i (-1)^{m-1-i} e_{m-1-i}(X') w_i )."""
    if B is None:
        B = Bmatrix(m)
    if w is None:
        d = PO.d_vec(TAU, m)
        w = solve_lower(B, d, m)
    Xp = [x_of(ts[k]) for k in range(m) if k != j]
    e = elem_sym(Xp)                      # e[0..m-1]
    S = Fr(0)
    for i in range(m):
        S += ((-1) ** (m - 1 - i)) * e[m - 1 - i] * w[i]
    return vp_frac(S, P)


def Cj_reference(ts, m, j):
    """C_j via §6ao integer-det definition: v_3(minor_j) - VD_j."""
    b = build(ts, m)
    if not b:
        return None
    oc, vo = b
    cols = [list(oc[k]) for k in range(m)]
    cols[j] = list(vo)
    dj = int_det(cols_to_rows(cols, m))
    if dj == 0:
        return None
    xs = [x_of(t) for t in ts]
    VD_j = sum(vp_frac(xs[a] - xs[c], P) for a in range(m) for c in range(a + 1, m) if a != j and c != j)
    return vp_int(dj, P) - VD_j


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("§6au: C_j = v_3( sum_i (-1)^{m-1-i} e_{m-1-i}(X') w_i ), w=B^{-1}d fixed. Explicit bilinear form.", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(20260816)
    # (a) verify bilinear form == reference C_j
    print("\n(a) verify explicit bilinear C_j == integer-det reference C_j (m=3..7):", flush=True)
    ok_all = True
    for m in range(3, 8):
        B = Bmatrix(m)
        w = solve_lower(B, PO.d_vec(TAU, m), m)
        got = False
        for _ in range(80):
            ts = rng.sample(range(1, 150), m)
            if not build(ts, m):
                continue
            for j in range(m):
                cb = Cj_bilinear(ts, m, j, B, w)
                cr = Cj_reference(ts, m, j)
                if cr is None:
                    continue
                match = (cb == cr)
                ok_all = ok_all and match
                if not match:
                    print(f"    MISMATCH m={m} j={j}: bilinear={cb} ref={cr}", flush=True)
            got = True
            print(f"    m={m}: checked all j on one config, matches so far={ok_all}", flush=True)
            break
        if not got:
            print(f"    m={m}: no valid config", flush=True)
    print(f"  ALL MATCH: {ok_all}", flush=True)
    # (b) adversarially MAXIMIZE C_j (cheap bilinear form; no build()/rank guard -- distinct x-values suffice
    # for the form, which equals true C_j on valid configs per (a)) to large m.
    print(f"\n(b) adversarially MAXIMIZE max_j C_j via the cheap bilinear form (lemma 4 test):", flush=True)
    print(f"{'m':>3} | {'max_j C_j (ascent, best of restarts)':>36}", flush=True)
    print("-" * 44, flush=True)

    def distinct_x(ts, m):
        if any(t == 0 for t in ts) or len(set(ts)) != m:
            return False
        xs = [x_of(t) for t in ts]
        return len(set(xs)) == m

    for m in range(4, 25):
        B = Bmatrix(m)
        w = solve_lower(B, PO.d_vec(TAU, m), m)
        NR = 8 if m <= 16 else 5
        best = None
        for _ in range(NR):
            ts = rng.sample(range(1, 600), m)
            if not distinct_x(ts, m):
                continue
            cur = max(Cj_bilinear(ts, m, j, B, w) for j in range(m))
            for _rnd in range(12):
                improved = False
                for i in range(m):
                    for _ in range(6):
                        cand = ts[:]
                        cand[i] = rng.randrange(1, 600)
                        if not distinct_x(cand, m):
                            continue
                        v = max(Cj_bilinear(cand, m, j, B, w) for j in range(m))
                        if v > cur:
                            cur, ts, improved = v, cand, True
                if not improved:
                    break
            if best is None or cur > best:
                best = cur
        print(f"{m:>3} | {str(best):>36}", flush=True)
    print("\n" + "=" * 96, flush=True)
    print("READING (L5): (a) must be ALL MATCH (else the bilinear form is wrong). In (b), if max_j C_j stays", flush=True)
    print("BOUNDED as m grows to 24, lemma (4) [v_3 of the pairing <w, e(X')> = O(1)] holds empirically at", flush=True)
    print("scale => p=3 floor proof essentially closes for D=425. If it GROWS, the off-line w can 3-adically", flush=True)
    print("align with node symmetric functions and (4) fails. Ascent = LOWER bound on max C_j. RH [OUT].", flush=True)
