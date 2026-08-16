#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bh — THE LAGRANGE-WEIGHT FACTORIZATION of the p=2 floor (a PROVED single-vector repackaging of §6bf).

The coefficient matrix E (rows = eps(X'_j), the coeffs of p_j(X)=prod_{k!=j}(X-x_k)) satisfies
    E . V^T = diag(P'(x_j))          because  p_j(x_l) = delta_{jl} * P'(x_j),   V = Vandermonde in the x_l.
Hence the pairing vector S = E.w factors as
    S = diag(P') . (V^T)^{-1} w,   so   C_j = v_2(S_j) = N_j + v_2(u_j),   u := (V^T)^{-1} w,
and the §6bf floor identity  v_2(q_min) = max_j(1 + N_j - C_j)  collapses to a SINGLE vector:
    v_2(q_min) = 1 - min_j v_2(u_j).                                             (**)
u_l = L(ell_l) are the QUADRATURE WEIGHTS of the fixed orbit functional L (L(X^i)=w_i) on the Lagrange
basis ell_l, so  sum_l u_l = L(1) = w_0  (a fixed orbit constant).

This probe VERIFIES, exactly (Fraction, L9):
  (A)  C_j == N_j + v_2(u_j)                    with u solving V^T u = w (sum_l x_l^i u_l = w_i);
  (B)  v_2(q_min) == 1 - min_j v_2(u_j);
  (C)  sum_l u_l == w_0.
Reported per m over random node sets. σ=3/4 orbit. RH stays [OUT]. Honest (L5): this is a PROVED identity;
it does NOT by itself close CORE-2 (min_l v_2(u_l) <= v_2(w_0)=O(1) via ultrametric on (C) is the same lossy
cancellation wall as §6bg).
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import qmin_exact_orbit, per_column, wvec
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int, vp_frac

P2 = 2
SIG, TAU = Fr(3, 4), Fr(1)


def solve_VT(w, xs, m):
    """Solve V^T u = w, i.e. sum_l x_l^i u_l = w_i (i=0..m-1). Gaussian elim over Fraction. Return u or None."""
    A = [[xs[l] ** i for l in range(m)] + [w[i]] for i in range(m)]
    for c in range(m):
        piv = next((r for r in range(c, m) if A[r][c] != 0), None)
        if piv is None:
            return None
        A[c], A[piv] = A[piv], A[c]
        inv = A[c][c]
        A[c] = [v / inv for v in A[c]]
        for r in range(m):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return [A[r][m] for r in range(m)]


def check_m(m, rng, want=40, tries_cap=4000):
    w = wvec(m, SIG, TAU)
    okA = okB = okC = cnt = tries = 0
    while cnt < want and tries < tries_cap:
        tries += 1
        ts = rng.sample(range(1, 150), m)
        xs = [x_of(t) for t in ts]
        if len(set(xs)) != m:
            continue
        pc = per_column(ts, m, w)          # (Nlist, Clist) or None
        if pc is None:
            continue
        u = solve_VT(w, xs, m)
        if u is None or any(x == 0 for x in u):
            continue
        q = qmin_exact_orbit(ts, m, SIG, TAU)
        if q is None:
            continue
        cnt += 1
        Ns, Cs = pc
        vu = [vp_frac(u[l], P2) for l in range(m)]
        if all(Cs[j] == Ns[j] + vu[j] for j in range(m)):
            okA += 1
        if vp_int(q, P2) == 1 - min(vu):
            okB += 1
        if sum(u) == w[0]:
            okC += 1
    return cnt, okA, okB, okC, vp_frac(w[0], P2)


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bh: Lagrange-weight factorization  v_2(q_min) = 1 - min_j v_2(u_j),  u = (V^T)^{-1} w.", flush=True)
    print("Checks (exact, L9):  (A) C_j = N_j + v_2(u_j);  (B) v_2(q_min) = 1 - min v_2(u_j);  (C) sum u_l = w_0.", flush=True)
    print("=" * 100, flush=True)
    print(f"{'m':>3} | {'#cfg':>5} | {'(A) C=N+v(u)':>12} | {'(B) floor':>10} | {'(C) sum=w0':>10} | {'v_2(w0)':>7}", flush=True)
    print("-" * 66, flush=True)
    rng = random.Random(20260816)
    allok = True
    for m in (3, 4, 5, 6, 7):
        cnt, okA, okB, okC, vw0 = check_m(m, rng)
        allok &= (okA == cnt == okB == okC) and cnt > 0
        print(f"{m:>3} | {cnt:>5} | {f'{okA}/{cnt}':>12} | {f'{okB}/{cnt}':>10} | {f'{okC}/{cnt}':>10} | {vw0:>7}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): all three columns matching = the §6bf identity is EXACTLY the single-vector form (**).", flush=True)
    print("This is a PROVED repackaging, NOT a proof of CORE-2: sum u_l = w_0 with v_2(w_0)=O(1) forces the", flush=True)
    print("deep-denominator weights to CANCEL to a shallow sum — the same cancellation wall as §6bg. The value", flush=True)
    print("is a cleaner Step-4 target: bound the deepest 2-adic denominator of the fixed vector (V^T)^{-1} w.", flush=True)
    print("RESULT:", "ALL MATCH" if allok else "MISMATCH — investigate", flush=True)
