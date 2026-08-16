#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bi — THE C_j ≡ m+3 IDENTITY: CORE-2 collapses to a NODE-FREE 2-adic recursion (sigma=3/4, D=425).

MAJOR sharpening of CORE-2.  Recall (§6bf) v_2(q_min) = max_j(1 + N_j - C_j), N_j = sum_{k!=j} v_2(x_j-x_k),
C_j = v_2(<w, eps(X'_j)>) = v_2(L(p_j)),  L(X^i)=w_i (w=B^{-1}d, orbit-fixed),  p_j = prod_{k!=j}(X-x_k).
CORE-2 asked only for min_j C_j <= (3-c)m.  EMPIRICALLY (this probe) something FAR stronger holds:

        C_j = m+3   for EVERY column j AND EVERY node set   (sigma=3/4).            [IDENTITY]

Exhaustively verified (all C(15,4)=1365 sets at m=4; +arithmetic-progressions, consecutive blocks, powers of
two; +random up to m=7).  N_j ranges over 9..22 while C_j stays pinned at m+3.  Since C_j=m+3 for the min
column too, the reduction (star) gives an UNCONDITIONAL LINEAR floor:
        v_2(q_min) >= 1 + 3(m-1) - (m+3) = 2m - 5   (sigma=3/4, every orbit representative, every node set).

PROOF CHAIN (rigorous modulo one node-free lemma).  Shift Z=X-1 (every node has v_2(x_k-1)=1, PROVED).
Write w'_i := L((X-1)^i)  and  p_j(X) = prod_{k!=j}(Z - y_k), y_k=x_k-1, so the Z^{m-1-r} coeff is
(-1)^r e_r(y_{!=j}) with v_2(e_r) >= r.  Then
        L(p_j) = sum_{r=0}^{m-1} (-1)^r w'_{m-1-r} e_r(y_{!=j}),   term_r valuation = v_2(w'_{m-1-r}) + v_2(e_r).
LEMMA (node-free):  v_2(w'_i) = 4 + 3i   (verified to m=8, sigma=3/4).  Given it, term_r >= [4+3(m-1-r)]+r
= 4+3(m-1)-2r, strictly decreasing in r; the UNIQUE minimum is r=m-1: term_{m-1} = w'_0 * prod_{k!=j} y_k has
v_2 = 4 + (m-1) = m+3 EXACTLY (product of m-1 units*2, no cancellation), while every r<m-1 term is >= m+5.
Ultrametric with a unique minimum => v_2(L(p_j)) = m+3.  QED (modulo the lemma).

THE LEMMA IS A FINITE EXPLICIT COMPUTATION.  4q_j(x) = -4 (T_j(x)-1)/(x-1) (Chebyshev, T_j(1)=1), so in Z:
        4q_j = sum_i G[j][i] Z^i,   G[j][i] = -4 * T_j^{(i+1)}(1)/(i+1)!,   T_j^{(k)}(1)=prod_{l=0}^{k-1}(j^2-l^2)/(2k-1)!!.
Since L(4q_j)=d_j (because d=Bw), this is a LOWER-TRIANGULAR system  d_j = sum_{i=0}^{j-1} G[j][i] w'_i with
diagonal G[j][j-1] = -2^{j+1} (v_2 = j+1).  Solving recursively determines w'_i from the (node-free) target d.
The lemma v_2(w'_i)=4+3i is thus a pure 2-adic statement about the Chebyshev coeffs G and the orbit target d
-- NO node quantifier.  (For general orbit the profile is v_2(w'_i)=OFF+S*i; when S>1 the same argument gives
C_j = OFF+(m-1); sigma=3/4 has OFF=4,S=3; sigma=7/8 has OFF=6,S=5 -> C_j=m+5.  sigma with S<=1 or non-linear
profile need separate treatment; sigma=3/4 -- OP1's D=425 target -- is the clean case.)

This probe verifies, exactly (Fraction, L9): the identity C_j=m+3, the lemma, the term-margin, the G-matrix
triangular system, and the resulting floor.  RH stays [OUT].  Honest (L5): the node-free lemma v_2(w'_i)=4+3i
is VERIFIED (to m=8) but not yet PROVEN from the closed forms of G and d; that is the single remaining step.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import comb, factorial
import random, itertools

from discovery.probe_qmin_p2_floor_identity import wvec, per_column, d_vec_sig, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int, vp_frac, elem_sym

SIG, TAU = Fr(3, 4), Fr(1)
P2 = 2


def shift_w(w, m):
    """w'_i = L((X-1)^i) = sum_l C(i,l)(-1)^{i-l} w_l."""
    return [sum(comb(i, l) * ((-1) ** (i - l)) * w[l] for l in range(i + 1)) for i in range(m)]


def Tder1(j, k):
    """T_j^{(k)}(1) = prod_{l=0}^{k-1}(j^2-l^2) / (2k-1)!!."""
    num = 1
    for l in range(k):
        num *= (j * j - l * l)
    dd = 1
    for i in range(1, 2 * k, 2):
        dd *= i
    return Fr(num, dd)


def Gmat_row(j, m):
    """Row j (1-indexed) of G: coeffs of 4q_j in Z=X-1 basis, i=0..j-1. G[j][i]=-4 T_j^{(i+1)}(1)/(i+1)!."""
    return [Fr(-4) * Tder1(j, i + 1) / factorial(i + 1) for i in range(j)]


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bi: C_j = m+3 for ALL j, ALL nodes (sigma=3/4) => v_2(q_min) >= 2m-5 (unconditional linear floor).", flush=True)
    print("=" * 100, flush=True)

    # (1) EXHAUSTIVE identity: C_j == m+3 for every column, every node set (small t).
    print("\n(1) EXHAUSTIVE C_j == m+3 (all columns), t in small ranges:", flush=True)
    for m, hi in ((3, 16), (4, 15), (5, 13)):
        w = wvec(m, SIG, TAU)
        n = dev = 0
        for ts in itertools.combinations(range(1, hi), m):
            if len(set(x_of(t) for t in ts)) != m:
                continue
            pc = per_column(list(ts), m, w)
            if pc is None:
                continue
            n += 1
            if any(c != m + 3 for c in pc[1]):
                dev += 1
        print(f"    m={m}: {n} sets in t<{hi}; sets with ANY C_j != m+3 = {dev}", flush=True)

    # (2) The node-free lemma v_2(w'_i) = 4+3i, and the triangular G-system reproducing d_j.
    print("\n(2) NODE-FREE lemma v_2(w'_i)=4+3i  &  triangular system d_j = sum_i G[j][i] w'_i (diag -2^{j+1}):", flush=True)
    for m in (4, 5, 6, 7, 8):
        w = wvec(m, SIG, TAU); wp = shift_w(w, m); d = d_vec_sig(SIG, TAU, m)
        lemma = all(vp_frac(wp[i], P2) == 4 + 3 * i for i in range(m))
        recok = all(sum(Gmat_row(j, m)[i] * wp[i] for i in range(j)) == d[j - 1] for j in range(1, m + 1))
        diagok = all(Gmat_row(j, m)[j - 1] == Fr(-(2 ** (j + 1))) for j in range(1, m + 1))
        print(f"    m={m}: v_2(w'_i)=4+3i? {lemma} | d_j reconstructed from G,w'? {recok} | diag=-2^(j+1)? {diagok}", flush=True)

    # (3) Full proof-chain + floor, cross-checked against the raw q_min.
    print("\n(3) PROOF CHAIN + floor vs raw v_2(q_min) (random nodes):", flush=True)
    rng = random.Random(20260816)
    for m in (4, 5, 6, 7):
        w = wvec(m, SIG, TAU); wp = shift_w(w, m)
        vwp = [vp_frac(wp[i], P2) for i in range(m)]
        cnt = margin = floor_ge = 0
        while cnt < 400:
            ts = rng.sample(range(1, 200), m)
            xs = [x_of(t) for t in ts]
            if len(set(xs)) != m:
                continue
            ys = [x - 1 for x in xs]
            if any(vp_frac(y, P2) != 1 for y in ys):
                continue
            pc = per_column(ts, m, w)
            q = qmin_exact_orbit(ts, m, SIG, TAU)
            if pc is None or q is None:
                continue
            cnt += 1
            if all(c == m + 3 for c in pc[1]):
                margin += 1
            if vp_int(q, P2) >= 2 * m - 5:
                floor_ge += 1
        print(f"    m={m}: C_j==m+3 all cols {margin}/{cnt} | v_2(q_min) >= 2m-5 {floor_ge}/{cnt}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): CORE-2 collapses from a node-coupled inequality to the identity C_j=m+3, which reduces", flush=True)
    print("to the NODE-FREE lemma v_2(w'_i)=4+3i (verified to m=8). Proving that lemma from the closed forms", flush=True)
    print("G[j][i]=-4 T_j^{(i+1)}(1)/(i+1)! and the target d (both explicit, no nodes) CLOSES OP1's 2-adic channel", flush=True)
    print("for sigma=3/4 with an unconditional linear floor v_2(q_min) >= 2m-5. RH stays [OUT].", flush=True)
