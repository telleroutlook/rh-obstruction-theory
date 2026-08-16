#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

p=3 FLOOR MECHANISM (§6am) — verify the two-step route for v_3(q_min) >= c*m proposed in §6al.

§6al reduced OP1 to a single-prime target v_3(q_min) >= c*m (m>=4), which SUFFICES because OP1 only needs
log q_min = omega(log m).  The proposed proof route is:
   (i)  columns of A fall into <= N(3)=2 classes mod 3 (x_k mod 3 determines the cleared column mod 3),
        so the confluent-Vandermonde staircase forces v_3(det A) >= c1*m;
   (ii) v_3(q_min) = v_3(det A) - min_j v_3(minor_j)  (RESIDUAL identity; minor_j = det[A with col j -> d],
        d the FIXED off-line vector), and the fixed d cannot 3-adically align with ALL m column-deletions,
        so min_j v_3(minor_j) <= v_3(det A) - c*m, leaving a LINEAR residue.
This probe MEASURES both steps exactly (L9):
  * class sizes (n_0, n_2) mod 3 of the node set, and v_3(det A) vs a fitted confluence law;
  * min_j v_3(minor_j) and the residual v_3(q_min) = v_3(det A) - min_j, over random AND adversarial
    (maximize min_j = minimize v_3(q_min)) configs;
  * cross-check v_3(q_min) == v_3(qmin_fast).
If v_3(det A) tracks a clean law >= c1*m AND the residual stays >= c*m under the adversary, step (i)+(ii)
are both plausible and the p=3 lemma is a concrete, provable target.  Honest (L5): a descent gives only an
UPPER bound on the adversary's min residual.  Bounded search.  One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows

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


def class_mod3(t):
    return 2 if t % 3 == 0 else 0          # x-class mod 3 (derived analytically; den never 0 mod 3)


def det_and_minors_v3(oc, vo, m):
    """v_3(det A) and min_j v_3(minor_j), minor_j = det with column j replaced by d=vo."""
    rows = cols_to_rows(oc, m)             # A as rows
    dA = int_det(rows)
    if dA == 0:
        return None
    vdet = vp_int(dA, P)
    # minor_j: replace column j of A by vo, take det. Build column form then convert.
    cols = [list(oc[k]) for k in range(m)]  # oc[k] is column k (length m)
    minv = None
    for j in range(m):
        c2 = [col[:] for col in cols]
        c2[j] = list(vo)
        mrows = cols_to_rows(c2, m)
        dj = int_det(mrows)
        vj = vp_int(dj, P) if dj != 0 else 10**9
        minv = vj if minv is None else min(minv, vj)
    return vdet, minv


def descent_minq3(ts, m, rng, rounds=20):
    best_ts = ts[:]
    b = build(best_ts, m)
    best = vp_int(qmin_fast(*b), P) if b and qmin_fast(*b) else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(8):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 360)
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
    print("p=3 FLOOR MECHANISM (§6am): step (i) v_3(det A) vs class sizes; step (ii) residual", flush=True)
    print("v_3(q_min) = v_3(det A) - min_j v_3(minor_j). Both must be >= c*m for the p=3 lemma.", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)
    print(f"{'m':>3} | {'config':>10} | {'(n0,n2)':>9} | {'v3(detA)':>8} | {'min_j v3(minor)':>15} | "
          f"{'v3(qmin)=resid':>14} | {'xchk':>5}", flush=True)
    print("-" * 92, flush=True)
    for m in range(4, 9):
        rows = []
        # adversarial min-v3 config
        s0 = rng.sample(range(1, 360), m)
        ts_adv = descent_minq3(s0, m, rng)
        rows.append(("min-v3", ts_adv))
        # a couple random valid configs
        cnt = 0
        for _ in range(200):
            cand = rng.sample(range(1, 360), m)
            if build(cand, m):
                rows.append((f"rand{cnt}", cand)); cnt += 1
            if cnt >= 2:
                break
        for tag, ts in rows:
            b = build(ts, m)
            if not b:
                print(f"{m:>3} | {tag:>10} | (invalid)", flush=True); continue
            oc, vo = b
            n2 = sum(1 for t in ts if class_mod3(t) == 2)
            n0 = m - n2
            dm = det_and_minors_v3(oc, vo, m)
            if dm is None:
                print(f"{m:>3} | {tag:>10} | detA=0", flush=True); continue
            vdet, minj = dm
            resid = vdet - minj
            q = qmin_fast(oc, vo)
            xchk = (resid == vp_int(q, P))
            print(f"{m:>3} | {tag:>10} | {str((n0, n2)):>9} | {vdet:>8} | {minj:>15} | "
                  f"{resid:>14} | {str(xchk):>5}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): step(i) OK if v_3(det A) grows >= c1*m (and relates cleanly to (n0,n2) confluence);", flush=True)
    print("step(ii) OK if the residual v_3(q_min) stays >= c*m even at the min-v3 adversary (i.e. min_j", flush=True)
    print("v3(minor) cannot reach v3(detA)). xchk must be True (residual identity == qmin_fast). If the", flush=True)
    print("adversary drives residual toward 0 while v3(detA) stays high, step(ii) FAILS (the fixed d DOES", flush=True)
    print("align) -- report honestly. Bounded search, one orbit (D=425). Evidence, not proof. RH [OUT].", flush=True)
