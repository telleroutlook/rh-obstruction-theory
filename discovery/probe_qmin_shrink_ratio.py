#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE SHRINK-RATIO TEST (§6ah) — the §6ag-suggested direct (non-channel-split) route.

§6ag killed the frontier-convexity reduction and pointed to a DIRECT determinantal bound on
    log q_min = log|det A| - log D_m([A|d])   (K=m; det A = D_m(A), D_m([A|d]) = gcd(det A, minors)).
The adversary shrinks q_min BELOW |det A| via the augmented gcd D_m([A|d]) (its ONLY tool -- it can
only enlarge the gcd, never |det A|).  Define the SHRINK RATIO
    kappa(node set) := log|det A| / log q_min    ( >= 1, since D_m([A|d]) >= 1 => q_min <= |det A| ).
IF kappa is UNIFORMLY BOUNDED (kappa <= K for all node sets), then log q_min >= log|det A| / K, so a
lower bound on the PURE determinant |det A| (no gcd, classical Vandermonde/Hadamard tools) transfers
to q_min -- a clean reduction avoiding the two-channel interior entirely.

BUT the danger q_min->1 is EXACTLY kappa->infinity (the gcd eats almost all of det A).  So this probe
adversarially MAXIMIZES kappa (min q_min while tracking |det A|) to test whether kappa is bounded:
  * min log2 q_min and the log2|det A| there, and kappa = ratio, m=2..7;
  * also the adversary that maximizes kappa directly (min log q_min / log|det A| is wrong sign; we
    maximize log|det A| - large? no): we MINIMIZE q_min and separately report the WORST (largest)
    kappa seen, since large kappa = gcd absorbing = the OP1 danger.
If max kappa GROWS with m, the shrink ratio is unbounded => the determinant route FAILS (the gcd is
too powerful), reported honestly (L5).  If max kappa stays bounded, log|det A| lower bound => OP1
floor: a clean rigorous target.  Exact integer arithmetic (L9).  Bounded search.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def logdetA(oc, m):
    d = int_det(cols_to_rows(oc, m))
    return (log2(abs(d)) if d else None), abs(d)


def stats(ts, m):
    b = build(ts, m)
    if not b:
        return None
    oc, vo = b
    q = qmin_fast(oc, vo)
    if not q or q < 2:
        return None
    ld, _ = logdetA(oc, m)
    if ld is None or ld < 1e-9:
        return None
    lq = log2(q)
    return lq, ld, ld / lq        # (log2 q_min, log2|detA|, kappa)


def descent(ts, m, rng, key, rounds=15):
    best_ts = ts[:]
    s = stats(best_ts, m)
    best = key(s) if s else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(6):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 320)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                s = stats(cand, m)
                if not s:
                    continue
                v = key(s)
                if v < best - 1e-9:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("SHRINK-RATIO TEST (§6ah): kappa = log|detA| / log q_min. Bounded kappa => det LB gives OP1", flush=True)
    print("floor; kappa->inf (gcd absorbs det) => q_min->1 danger, determinant route FAILS.", flush=True)
    print("=" * 100, flush=True)
    print(f"{'m':>3} | {'min log2 q':>10} | {'log2|detA| there':>16} | {'kappa there':>11} | "
          f"{'MAX kappa seen':>14} | {'q@maxk':>8}", flush=True)
    rng = random.Random(20260816)
    for m in range(2, 8):
        min_q = None      # (lq, ld, kappa)
        max_k = None      # (kappa, lq, ld)
        def consider(ts):
            global min_q, max_k
            s = stats(ts, m)
            if not s:
                return
            lq, ld, k = s
            if min_q is None or lq < min_q[0]:
                min_q = (lq, ld, k)
            if max_k is None or k > max_k[0]:
                max_k = (k, lq, ld)
        for _ in range(700):
            consider(rng.sample(range(1, 320), m))
        # descent minimizing q_min (drives kappa up), from many starts
        for _ in range(25):
            s = rng.sample(range(1, 320), m)
            consider(descent(s, m, rng, lambda st: st[0]))            # min log q
            consider(descent(s, m, rng, lambda st: -st[2]))           # max kappa directly
        if min_q is None:
            print(f"{m:>3} | (no valid)", flush=True)
            continue
        lq, ld, k = min_q
        mk, mkq, mkd = max_k
        print(f"{m:>3} | {lq:10.2f} | {ld:16.2f} | {k:11.3f} | {mk:14.3f} | {mkq:8.2f}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if MAX kappa stays BOUNDED as m grows, the augmented gcd cannot eat more than a", flush=True)
    print("constant fraction of log|detA|, so log q_min >= log|detA|/K -- reducing OP1 to a PURE", flush=True)
    print("determinant lower bound (Vandermonde/Hadamard, no gcd). If MAX kappa GROWS, the gcd is", flush=True)
    print("unboundedly powerful and the direct determinant route FAILS (honest close). q@maxk shows the", flush=True)
    print("q_min at the worst absorption. Bounded search, one orbit (D=425). Evidence. RH stays [OUT].", flush=True)
