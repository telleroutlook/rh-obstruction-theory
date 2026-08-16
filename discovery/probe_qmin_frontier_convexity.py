#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE TRADE-OFF FRONTIER CONVEXITY TEST (§6ag) — reduce OP1's interior to "two endpoints + convexity".

§6af crisped the barrier: log q_min = ram_mass + geo_mass with two PROVEN-mechanism endpoints
(ram=0 => geo grows via large-prime count; fully spread => ram >= §6ad confluence).  The sole open
nucleus is the INTERIOR joint bound  ram_mass + geo_mass >= c*m.  IF the trade-off frontier
    F(R) := min { geo_mass(q_min) : node set with ram_mass(q_min) = R }
is CONVEX and DECREASING with F(0) large and F(R_max) small but R_max large, then
    min_node ( ram + geo ) = min_R ( R + F(R) )
is attained at an interior R and, by convexity, is bounded below by the tangent/endpoint data alone.
That would reduce the whole aggregate floor to (i) the two endpoint bounds (mechanisms already found)
and (ii) a convexity/interpolation lemma — a clean, self-contained provable structure.

This probe MAPS F(R): over a large adversarial sample (random + descent minimizing geo at various
ram-penalty weights lambda, sweeping lambda to trace the frontier), bin by ram_mass and record min
geo_mass per bin, for m=3..6.  It reports the frontier points (R, F(R)), the implied min of R+F(R),
and a DISCRETE CONVEXITY check (second differences >= 0 along the sorted frontier).  If convex with
high endpoints, the interpolation target is well-posed; if the frontier has a deep interior dip
(R+F(R) << endpoints), the aggregate floor would be WEAKER than the endpoints suggest (report, L5).
Exact integer arithmetic (L9).  Bounded search (evidence, not proof).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vp

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17


def qmin_of(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return qmin_fast(oc, vo) or None


def channels(q):
    ram = vp(q, 5) * log2(5) + vp(q, 17) * log2(17)
    return ram, log2(q) - ram


def descent(ts, m, rng, key, rounds=15):
    best_ts = ts[:]
    q = qmin_of(best_ts, m)
    best = key(q) if q else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(6):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 320)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                q = qmin_of(cand, m)
                if not q:
                    continue
                v = key(q)
                if v < best - 1e-9:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("TRADE-OFF FRONTIER CONVEXITY (§6ag): F(R)=min geo_mass at ram_mass=R. Convex+high ends =>", flush=True)
    print("aggregate floor = min_R (R+F(R)) reducible to endpoints + convexity lemma.", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)
    for m in range(3, 7):
        pts = []      # (ram, geo)
        def rec(ts):
            if ts and len(set(ts)) == m and all(t != 0 for t in ts):
                q = qmin_of(ts, m)
                if q:
                    pts.append(channels(q))
        for _ in range(600):
            rec(rng.sample(range(1, 320), m))
        # sweep ram-penalty weight lambda to trace the frontier (min geo + lambda*ram)
        for lam in (0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 100.0):
            for _ in range(8):
                s = rng.sample(range(1, 320), m)
                rec(descent(s, m, rng, lambda q, L=lam: channels(q)[1] + L * channels(q)[0]))
        # bin by ram_mass (bin width ~ log2(5)=2.32), min geo per bin
        binw = log2(5)
        frontier = {}
        for r, g in pts:
            b = round(r / binw)
            if b not in frontier or g < frontier[b][1]:
                frontier[b] = (r, g)
        fr = sorted(frontier.values(), key=lambda z: z[0])
        print(f"\n----- m={m}  ({len(pts)} node sets, {len(fr)} frontier bins) -----", flush=True)
        print("  (ram_mass, min geo_mass):", flush=True)
        for r, g in fr:
            print(f"     R={r:7.2f}  F(R)={g:7.2f}   R+F(R)={r+g:7.2f}", flush=True)
        rf = min(r + g for r, g in fr)
        # discrete convexity: second differences of F over sorted R (unequal spacing -> slope check)
        slopes = []
        for i in range(1, len(fr)):
            dR = fr[i][0] - fr[i - 1][0]
            if dR > 1e-6:
                slopes.append((fr[i][1] - fr[i - 1][1]) / dR)
        convex = all(slopes[i] >= slopes[i - 1] - 1e-6 for i in range(1, len(slopes)))
        print(f"  => min_R (R+F(R)) = {rf:.2f}   |   slopes {[f'{s:.2f}' for s in slopes]}", flush=True)
        print(f"  => frontier convex (non-decreasing slopes)? {convex}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if F(R) is convex+decreasing with F(0) large and endpoint R_max large, then", flush=True)
    print("min_R(R+F(R)) is pinned by the two endpoints => aggregate floor reduces to endpoints (§6af,", flush=True)
    print("§6ad) + a convexity lemma: a clean provable structure. If min_R(R+F(R)) dips far below both", flush=True)
    print("endpoints (deep interior well), the floor is weaker than endpoints suggest — report honestly.", flush=True)
    print("Bounded search, one orbit (D=425). Evidence, not proof. RH stays [OUT].", flush=True)
