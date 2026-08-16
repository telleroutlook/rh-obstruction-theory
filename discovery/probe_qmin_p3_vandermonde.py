#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

v_3(det A) VANDERMONDE REDUCTION (§6an) — make step (i) of the §6al/§6am p=3 route a provable identity.

The matrix is A_{j,k} = C_j(x_k) = 4(1 - T_j(x_k)), j=1..m, with x_k = (4 t_k^2 - 1)/(4 t_k^2 + 1).  Since
{T_j}_{j>=1} is a graded polynomial basis (deg T_j = j), the map from the pure Vandermonde [x_k^{i}] to
[T_j(x_k)] is a fixed unimodular-up-to-leading-coeff triangular change of basis, so classically
    det[T_j(x_k)]_{j,k=1..m} = (prod of leading coeffs) * Vandermonde(x_1..x_m) = const * prod_{k<l}(x_l - x_k).
The extra "4(1 - .)" and the all-ones shift only rescale / rank-1-correct.  3-ADICALLY this predicts
    v_3(det A) = sum_{k<l} v_3(x_k - x_l) + CORRECTION,     CORRECTION = O(m) (from the 4's, leading
    coeffs 2^{j-1}, and the rank-1 all-ones piece -- none of which involve node DIFFERENCES).
If CORRECTION is bounded/linear while the Vandermonde distance-sum carries the super-linear growth, step (i)
is essentially PROVED and the whole p=3 floor becomes a PURE 3-ADIC ULTRAMETRIC quantity on {x_k}:
    v_3(q_min) = max_j max(0, sum_{k!=j}[v_3(x_j - x_k) - (off-line distance term)]).
This probe measures, over random and adversarial-min-v3 node sets (exact, L9):
   VD := sum_{k<l} v_3(x_k - x_l),   v3det := v_3(det A),   CORR := v3det - VD.
If CORR is small and stable (independent of the super-linear part), the reduction holds.  Honest (L5): a
mismatch would mean the Chebyshev/all-ones structure contributes 3-adically at the node-difference level.
One orbit (D=425). Bounded search. RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows
from discovery.qmin_snf_fast import qmin_fast

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17
P = 3


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def vp_int(n, p):
    v = 0
    while n and n % p == 0:
        n //= p; v += 1
    return v


def vp_frac(fr, p):
    if fr == 0:
        return 10**9
    return vp_int(fr.numerator, p) - vp_int(fr.denominator, p)


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


def vandermonde_v3(ts):
    xs = [x_of(t) for t in ts]
    s = 0
    for a in range(len(xs)):
        for b in range(a + 1, len(xs)):
            s += vp_frac(xs[a] - xs[b], P)
    return s


def descent_minq3(ts, m, rng, rounds=18):
    best_ts = ts[:]
    b = build(best_ts, m)
    best = vp_int(qmin_fast(*b), P) if b and qmin_fast(*b) else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(8):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 300)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                b = build(cand, m)
                if not b:
                    continue
                q = qmin_fast(*b)
                if not q or q < 2:
                    continue
                v = vp_int(q, P)
                if v < best:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts


if __name__ == "__main__":
    print("=" * 92, flush=True)
    print("v_3(det A) VANDERMONDE REDUCTION (§6an): v3det =? sum_{k<l} v_3(x_k - x_l) + CORR, CORR=O(m).", flush=True)
    print("If CORR is small/stable, step (i) of the p=3 route is a provable identity; floor is ultrametric.", flush=True)
    print("=" * 92, flush=True)
    rng = random.Random(20260816)
    print(f"{'m':>3} | {'config':>8} | {'v3(detA)':>8} | {'VD=sum v3(xk-xl)':>16} | {'CORR=v3det-VD':>13} | "
          f"{'CORR/m':>7}", flush=True)
    print("-" * 76, flush=True)
    for m in range(3, 9):
        cfgs = []
        s0 = rng.sample(range(1, 300), m)
        cfgs.append(("min-v3", descent_minq3(s0, m, rng)))
        cnt = 0
        for _ in range(200):
            cand = rng.sample(range(1, 300), m)
            if build(cand, m):
                cfgs.append((f"rand{cnt}", cand)); cnt += 1
            if cnt >= 2:
                break
        for tag, ts in cfgs:
            b = build(ts, m)
            if not b:
                print(f"{m:>3} | {tag:>8} | (invalid)", flush=True); continue
            oc, vo = b
            dA = int_det(cols_to_rows(oc, m))
            if dA == 0:
                print(f"{m:>3} | {tag:>8} | detA=0", flush=True); continue
            v3det = vp_int(dA, P)
            vd = vandermonde_v3(ts)
            corr = v3det - vd
            print(f"{m:>3} | {tag:>8} | {v3det:>8} | {vd:>16} | {corr:>13} | {corr / m:7.3f}", flush=True)
    print("\n" + "=" * 92, flush=True)
    print("READING (L5): if CORR is small and ~constant/linear (bounded CORR/m) while v3det and VD both grow", flush=True)
    print("super-linearly TOGETHER, then v_3(det A) = Vandermonde-3-adic-distance-sum + O(m): step (i) is a", flush=True)
    print("classical confluent-Vandermonde identity and the p=3 floor is a PURE ultrametric quantity on the", flush=True)
    print("nodes' x-values. If CORR grows super-linearly or erratically, the Chebyshev/all-ones structure", flush=True)
    print("contributes at the difference level and the reduction needs care. One orbit (D=425). RH [OUT].", flush=True)
