#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

OFF-LINE ULTRAMETRIC DECOMPOSITION (§6ao) — complete the pure-3-adic formula for v_3(q_min).

§6an proved (empirically, exact) v_p(det A) = sum_{k<l} v_p(x_k - x_l) for odd p.  With the residual
identity (§6am) v_3(q_min) = v_3(det A) - min_j v_3(minor_j), and minor_j = det[A, col j -> d] (d the FIXED
off-line vector O_orbit_direct), define per deleted node j:
    VD_j := sum_{k<l, k,l != j} v_3(x_k - x_l)         (Vandermonde 3-adic distances of the cluster minus j)
    C_j  := v_3(minor_j) - VD_j                          (the OFF-LINE closeness term for cluster minus j)
    N_j  := sum_{k != j} v_3(x_j - x_k)                  (node j's 3-adic closeness to the rest)
Then v_3(det A) = VD_j + N_j, so
    R_j := v_3(det A) - v_3(minor_j) = N_j - C_j,   and   v_3(q_min) = max_j R_j  (when > 0).
THE FLOOR HINGES ON C_j.  If C_j is BOUNDED (O(1)) -- the fixed off-line orbit cannot be 3-adically close
to many nodes -- then max_j R_j >= max_j N_j - O(1) >= (2 v_3(det A)/m) - O(1) ~ LINEAR (since sum_j N_j =
2 v_3(det A) is super-linear).  That would essentially PROVE the p=3 floor.  This probe measures C_j and
N_j (exact, L9) over random and adversarial min-v3 node sets, reports max_j C_j (does it grow?), max_j N_j,
max_j R_j, and cross-checks max_j R_j == v_3(q_min).  Honest (L5): if C_j GROWS ~linearly (the off-line
orbit CAN track the cluster 3-adically), the simple bound fails and the residual needs the finer argument.
One orbit (D=425). Bounded search. RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
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


def minor_v3(oc, vo, m, j):
    cols = [list(oc[k]) for k in range(m)]
    cols[j] = list(vo)
    dj = int_det(cols_to_rows(cols, m))
    return vp_int(dj, P) if dj != 0 else None


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
    print("=" * 100, flush=True)
    print("OFF-LINE ULTRAMETRIC DECOMPOSITION (§6ao): R_j = N_j - C_j, v_3(q_min)=max_j R_j. Floor hinges", flush=True)
    print("on C_j (off-line closeness): if C_j is BOUNDED, max R_j >= 2 v3(detA)/m - O(1) ~ LINEAR floor.", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)
    print(f"{'m':>3} | {'config':>8} | {'v3(detA)':>8} | {'max C_j':>7} | {'sum C_j':>7} | {'max N_j':>7} | "
          f"{'max R_j':>7} | {'v3(qmin)':>8} | {'chk':>4}", flush=True)
    print("-" * 84, flush=True)
    for m in range(4, 9):
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
            xs = [x_of(t) for t in ts]
            Cs, Ns, Rs = [], [], []
            for j in range(m):
                mj = minor_v3(oc, vo, m, j)
                if mj is None:
                    mj = 10**9
                VD_j = 0
                for a in range(m):
                    for c in range(a + 1, m):
                        if a != j and c != j:
                            VD_j += vp_frac(xs[a] - xs[c], P)
                N_j = sum(vp_frac(xs[j] - xs[k], P) for k in range(m) if k != j)
                C_j = mj - VD_j
                Cs.append(C_j); Ns.append(N_j); Rs.append(v3det - mj)
            maxR = max(Rs)
            q = qmin_fast(oc, vo)
            chk = (maxR == vp_int(q, P))
            print(f"{m:>3} | {tag:>8} | {v3det:>8} | {max(Cs):>7} | {sum(Cs):>7} | {max(Ns):>7} | "
                  f"{maxR:>7} | {vp_int(q, P):>8} | {str(chk):>4}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if 'max C_j' stays BOUNDED (does not grow with m) then the off-line orbit cannot", flush=True)
    print("3-adically shadow the node cluster, so v_3(q_min)=max R_j >= max N_j - O(1) is forced LINEAR by", flush=True)
    print("sum_j N_j = 2 v3(detA) -- a near-complete PROOF of the p=3 floor. If max C_j GROWS ~linearly, the", flush=True)
    print("fixed d DOES track the cluster and the residual needs the finer fixed-vector argument. 'chk' must", flush=True)
    print("be True (max R_j == v_3(qmin)). One orbit (D=425). Evidence, not proof. RH stays [OUT].", flush=True)
