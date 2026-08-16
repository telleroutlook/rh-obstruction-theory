#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

STRESS-TEST the AGGREGATE OP1 floor (§6y) with the STRONGEST attack.  Per-prime (§6w) and
per-channel (§6z-note) handles are ALL drainable; the only object that resisted is the aggregate
log q_min.  §6x supported linear growth but used only generic cluster/spread/random sampling and
was truncated with a suspicious m=10 dip.  probe_ramified_drain showed COORDINATE DESCENT drains
what generic sampling cannot.  So here we turn coordinate descent (+ all drain weapons as moves)
on the FULL log2(q_min) and push m, asking: can the aggregate be driven SUB-LINEAR?

Also verifies the clean reformulation used to reason about the target:
    (LCM)  q_min = lcm of denominators of x = A^{-1} d   (Ax=d over Q; q d in colspan_Z(A) <=> qx in Z^m).
This equals D_m(A)/D_m([A|d]) and is the exact quantity whose log we want >= c*m.

DECISION (L5): if coordinate descent drives min log2(q_min) sub-linear (increment collapsing toward
0) the aggregate floor — hence OP1 — is THREATENED and reported honestly. If min log2(q_min) keeps
rising ~linearly under this strongest combined attack, the aggregate floor survives every draining
technique that killed the per-prime/per-channel routes. Exact SNF + exact rational solve (L9).
Bounded search. RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2, lcm
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows
import discovery.probe_leg3_affine as A

SIG, TAU = Fr(3, 4), Fr(1)   # D=425


def class_node_bases(p, want):
    seen, bases, c1 = set(), [], A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r != c1 and r not in seen:
            seen.add(r); bases.append(t0)
            if len(bases) >= want:
                break
    return bases


def qmin_of(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    q = qmin_fast(oc, vo)
    return q or None


def solve_lcm_den(ts, m):
    """q_min via (LCM): lcm of denominators of x=A^{-1}d, exact rational Cramer-free solve."""
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    # rows of the m x m system, RHS = vo
    M = [[Fr(oc[j][i]) for j in range(m)] + [Fr(vo[i])] for i in range(m)]
    # Gaussian elimination (exact)
    for i in range(m):
        piv = next((r for r in range(i, m) if M[r][i] != 0), None)
        if piv is None:
            return None
        M[i], M[piv] = M[piv], M[i]
        inv = M[i][i]
        M[i] = [v / inv for v in M[i]]
        for r in range(m):
            if r != i and M[r][i] != 0:
                f = M[r][i]
                M[r] = [M[r][c] - f * M[i][c] for c in range(m + 1)]
    dens = [M[i][m].denominator for i in range(m)]
    L = 1
    for d in dens:
        L = lcm(L, d)
    return L


def descent(ts, m, rng, rounds=30, cluster_bases=None):
    best_ts = ts[:]
    q = qmin_of(best_ts, m)
    best = log2(q) if q else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(8):
                cand = best_ts[:]
                roll = rng.random()
                if cluster_bases and roll < 0.5:
                    cand[i] = rng.choice(cluster_bases) + rng.choice([7, 11, 13]) * rng.randrange(20)
                else:
                    cand[i] = rng.randrange(1, 700)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                q = qmin_of(cand, m)
                if not q:
                    continue
                v = log2(q)
                if v < best - 1e-9:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best, best_ts


if __name__ == "__main__":
    print("=" * 92, flush=True)
    print("AGGREGATE stress test (D=425): coordinate-descent MINIMIZE full log2(q_min). Sub-linear?", flush=True)
    print("Also cross-checks (LCM) q_min = lcm(den(A^{-1} d)) == qmin_fast.", flush=True)
    print("=" * 92, flush=True)
    rng = random.Random(1618033)
    lcm_ok = lcm_tot = 0
    prev = None
    print(f"{'m':>3} | {'min log2 q_min':>15} | {'d/dm':>7} | {'(LCM) check':>12}", flush=True)
    cb = []
    for p in (7, 11, 13):
        cb += class_node_bases(p, (p - 1) // 2)
    for m in range(2, 13):
        best = float("inf")
        # generic + cluster starts
        for _ in range(120):
            kind = rng.randrange(3)
            if kind == 0:
                ts = rng.sample(range(1, 700), m)
            elif kind == 1:
                p = rng.choice([7, 11, 13]); bn = class_node_bases(p, rng.choice([2, 3]))
                if len(bn) < 2:
                    continue
                ts = [bn[k % len(bn)] + p * rng.randrange(20) for k in range(m)]
            else:
                ts = [rng.choice(cb) + rng.choice([7, 11, 13]) * rng.randrange(15) for _ in range(m)]
            if len(set(ts)) != m:
                continue
            q = qmin_of(ts, m)
            if q:
                best = min(best, log2(q))
                # (LCM) cross-check on a sample
                if lcm_tot < 400:
                    L = solve_lcm_den(ts, m)
                    lcm_tot += 1
                    if L == q:
                        lcm_ok += 1
        # descent from several starts
        for _ in range(10):
            ts0 = rng.sample(range(1, 700), m)
            if len(set(ts0)) != m:
                continue
            bd, _ = descent(ts0, m, rng, cluster_bases=cb)
            best = min(best, bd)
        d = f"{best - prev:+.2f}" if prev is not None else "  -  "
        print(f"{m:>3} | {best:15.2f} | {d:>7} | {lcm_ok}/{lcm_tot}", flush=True)
        prev = best
    print("\n" + "=" * 92, flush=True)
    print(f"(LCM) q_min == lcm(den(A^-1 d)) held {lcm_ok}/{lcm_tot}.", flush=True)
    print("READING (L5): if 'd/dm' stays bounded away from 0 (min log2 q_min ~linear in m) under this", flush=True)
    print("descent+cluster attack, the AGGREGATE floor survives the strongest draining technique —", flush=True)
    print("the one that killed the per-prime and per-channel handles. If d/dm collapses toward 0, the", flush=True)
    print("aggregate is drainable and OP1 is threatened (report honestly). Bounded search. RH [OUT].", flush=True)
