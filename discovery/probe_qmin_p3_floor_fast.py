#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

DIRECT p=3 FLOOR via FAST MINOR-DET FORMULA (§6aq) — the decisive, correctly-targeted OP1 test.

§6ap mistake, corrected here: maximizing max_j C_j is the WRONG target. The p=3 residual is
    v_3(q_min) = v_3(det A) - min_j v_3(minor_j)                              (§6am identity, exact)
and BOTH v_3(det A) and each minor_j = det[A, col j -> d] are INTEGER DETERMINANTS.  So v_3(q_min) is
computable with int_det alone -- NO slow SNF (qmin_fast) -- which lets us push the DIRECT adversarial
floor test to LARGE m (m=4..16) cheaply.  The enemy of OP1 is q_min -> 1, i.e. v_3(q_min) -> small.  So we
ADVERSARIALLY MINIMIZE v_3(q_min) over node sets (coordinate descent, many restarts) and ask:

    does the adversarial-minimum v_3(q_min) GROW with m (=> log q_min = omega(log m) => OP1 TRUE for p=3),
    or can the adversary drive it to O(1) / 0 (=> p=3 floor fails; need another prime or finer argument)?

This supersedes §6al (which used the slow qmin_fast and truncated at m=9) with the fast formula, and directly
decides the floor rather than a proxy.  Cross-check on small m: v_3 via minor formula == v_3(qmin_fast).
Exact integer arithmetic (L9).  Honest (L5): descent gives an UPPER bound on the true adversarial min; if it
keeps dropping as search deepens we say so.  One orbit (D=425).  RH stays [OUT].
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


def v3_qmin_fast(oc, vo, m):
    """v_3(q_min) = v_3(det A) - min_j v_3(minor_j), using only integer determinants (no SNF)."""
    dA = int_det(cols_to_rows(oc, m))
    if dA == 0:
        return None
    vdet = vp_int(dA, P)
    vmin = None
    for j in range(m):
        cols = [list(oc[k]) for k in range(m)]
        cols[j] = list(vo)
        dj = int_det(cols_to_rows(cols, m))
        vj = vp_int(dj, P) if dj != 0 else 10**9
        vmin = vj if vmin is None else min(vmin, vj)
    return vdet - vmin


def descent_min_v3(ts, m, rng, rounds=25, tries=10):
    best_ts = ts[:]
    b = build(best_ts, m)
    best = v3_qmin_fast(*b, m) if b else 10**9
    if best is None:
        best = 10**9
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(tries):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 400)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                b = build(cand, m)
                if not b:
                    continue
                v = v3_qmin_fast(*b, m)
                if v is not None and v < best:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts, best


if __name__ == "__main__":
    print("=" * 94, flush=True)
    print("DIRECT p=3 FLOOR (§6aq): adversarially MINIMIZE v_3(q_min)=v3(detA)-min_j v3(minor_j), fast (int", flush=True)
    print("dets only, no SNF), pushed to large m. Does the adversarial min GROW with m => OP1 TRUE for p=3?", flush=True)
    print("=" * 94, flush=True)
    # cross-check the fast minor formula against qmin_fast (SNF) on small m
    print("\ncross-check (fast minor formula vs qmin_fast SNF), a few random configs:", flush=True)
    rng = random.Random(20260816)
    ok = True
    for m in range(3, 8):
        for _ in range(400):
            ts = rng.sample(range(1, 300), m)
            b = build(ts, m)
            if not b:
                continue
            vf = v3_qmin_fast(*b, m)
            q = qmin_fast(*b)
            vs = vp_int(q, P) if q else 0
            match = (vf == vs)
            ok = ok and match
            print(f"    m={m}: fast={vf}  SNF={vs}  match={match}", flush=True)
            break
    print(f"  ALL MATCH: {ok}", flush=True)
    print(f"\n{'m':>3} | {'adversarial-min v_3(q_min) UPPER bound (lean descent, larger m)':>58} | {'m/2':>4}",
          flush=True)
    print("-" * 74, flush=True)
    for m in range(10, 14):
        # ultra-lean budget: solidify the growth trend at larger m (UPPER bound on adversarial min, L5).
        NR, rounds, tries = 3, 4, 4
        overall = None
        for _ in range(NR):
            s0 = rng.sample(range(1, 400), m)
            if not build(s0, m):
                continue
            _, v = descent_min_v3(s0, m, rng, rounds=rounds, tries=tries)
            if v is not None and (overall is None or v < overall):
                overall = v
        print(f"{m:>3} | {str(overall):>58} | {m // 2:>4}", flush=True)
    print("\n" + "=" * 94, flush=True)
    print("READING (L5): if the adversarial-min v_3(q_min) GROWS with m (roughly linear, tracking ~m/2), the", flush=True)
    print("p=3 floor holds: log q_min >= (min v_3)*log 3 = omega(log m) => OP1 TRUE for D=425. If the adversary", flush=True)
    print("drives it to a constant / 0 as m grows, the single-prime p=3 floor FAILS and OP1 needs the multi-", flush=True)
    print("prime CRT-tension argument (§6ak) or a finer bound -- reported honestly. Descent = UPPER bound on", flush=True)
    print("the true adversarial min. One orbit (D=425). Evidence, not proof. RH stays [OUT].", flush=True)
