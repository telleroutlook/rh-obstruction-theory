#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE CORRECTED OP1 TARGET (post §6u/§6w).  Both prime-by-prime routes are dead: lag=O(1)
(§6u) and the per-prime floor v_p(q_min)>=ceil(2m/(p+3))-1 (§6w, broken at p=13).  What OP1
actually needs is the AGGREGATE bound

        inf over valid collisions of  log q_min = sum_p v_p(q_min) log p   is super-poly in m.

§6w showed that at a config MINIMIZING one prime's part (v_13=0), the FULL q_min stayed
enormous (379 bits) — mass migrated to other primes.  But that witness did NOT minimize the
whole q_min.  DECISIVE question now: can the adversary, using the very clustering weapon that
drains individual primes, drive the ENTIRE q_min down toward polynomial size?

This probe adversarially MINIMIZES the full log2(q_min) over VALID collisions (K>=m, rank m,
finite qmin), m=2..13, 3 orbits, comparing three adversaries:
  * CLUSTER  — nodes packed into few x-classes mod a small prime p in {7,11,13} (the §6w weapon,
    which provably drains that prime's part to 0);
  * SPREAD   — nodes in distinct x-classes (max Vandermonde spread);
  * RANDOM   — small-integer rational nodes, no structure.
Per m it reports the MIN log2(q_min) each adversary achieves and the overall min, plus the
increment d(log2) vs the previous m.  If the overall min log2(q_min) keeps growing ~linearly
(q_min exponential => super-polynomial), the corrected aggregate target is strongly supported
and clustering does NOT threaten it; if it flattens or drops toward O(log m), that is a real
threat to OP1 and must be reported.

HONESTY (L5): bounded random search, small m; DETECTS a downward break if one exists in range,
else evidence (not proof) that the aggregate q_min resists the per-prime draining attack.
RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A

ORBITS = [("D=425", Fr(3, 4), Fr(1)), ("D=4", Fr(2, 5), Fr(4, 5)), ("D=26", Fr(1), Fr(1, 5))]


def class_node_bases(p, want):
    seen, bases = set(), []
    c1 = A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r != c1 and r not in seen:
            seen.add(r); bases.append(t0)
            if len(bases) >= want:
                break
    return bases


def qmin_of(ts, sig, tau, m):
    """full integer q_min for a VALID collision (rank m, finite qmin), else None."""
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    pool = [Fr(t) for t in ts]
    oc, vo = cleared_columns(pool, sig, tau, m)
    if matrix_rank_int(oc, m) != m:
        return None
    q = qmin_fast(oc, vo)
    return q if q else None


def adv_cluster(sig, tau, m, p, ncls, S, rng, trials):
    bn = class_node_bases(p, ncls)
    if len(bn) < ncls:
        return None
    best = None
    for _ in range(trials):
        assign = [k % ncls for k in range(m)]; rng.shuffle(assign)
        ts = [bn[assign[k]] + p * rng.randrange(S) for k in range(m)]
        q = qmin_of(ts, sig, tau, m)
        if q and (best is None or q < best):
            best = q
    return best


def adv_spread(sig, tau, m, p, S, rng, trials):
    bn = class_node_bases(p, (p - 1) // 2)
    if len(bn) < min(m, (p - 1) // 2):
        return None
    best = None
    for _ in range(trials):
        # one node per distinct class where possible, small depths
        ts = [bn[k % len(bn)] + p * rng.randrange(S) for k in range(m)]
        q = qmin_of(ts, sig, tau, m)
        if q and (best is None or q < best):
            best = q
    return best


def adv_random(sig, tau, m, hi, rng, trials):
    best = None
    for _ in range(trials):
        ts = rng.sample(range(1, hi), m)
        q = qmin_of(ts, sig, tau, m)
        if q and (best is None or q < best):
            best = q
    return best


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("CORRECTED OP1 TARGET: adversarially MINIMIZE full log2(q_min) over valid collisions.", flush=True)
    print("Does the per-prime-draining CLUSTER attack shrink the WHOLE q_min toward polynomial?", flush=True)
    print("3 orbits; CLUSTER(p in 7,11,13) vs SPREAD vs RANDOM.  DISCOVERY. No RH.", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260817)
    overall_prev = None
    for name, sig, tau in ORBITS:
        print(f"\norbit {name} (sig={sig}, tau={tau}):", flush=True)
        prev = None
        for m in range(2, 14):
            cvals = []
            for p in (7, 11, 13):
                for ncls in (2, 3):
                    if ncls <= min(m, (p - 1) // 2):
                        v = adv_cluster(sig, tau, m, p, ncls, 30, rng, 150)
                        if v:
                            cvals.append(v)
            spreadv = min([x for x in (adv_spread(sig, tau, m, p, 30, rng, 150) for p in (11, 13)) if x], default=None)
            randv = adv_random(sig, tau, m, 400, rng, 300)
            cmin = min(cvals) if cvals else None
            cands = [x for x in (cmin, spreadv, randv) if x]
            if not cands:
                continue
            qmin = min(cands)
            lg = log2(qmin)
            d = f"{lg - prev:+.2f}" if prev is not None else "  -  "
            def lz(x):
                return f"{log2(x):5.1f}" if x else "  -  "
            print(f"   m={m:>2}: min log2 q_min = {lg:6.2f}  (d={d})   "
                  f"[cluster {lz(cmin)} | spread {lz(spreadv)} | random {lz(randv)}]  "
                  f"argmin={'cluster' if qmin==cmin else 'spread' if qmin==spreadv else 'random'}", flush=True)
            prev = lg
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if min log2 q_min keeps rising ~linearly in m and the CLUSTER column is", flush=True)
    print("NOT systematically the smallest, then per-prime draining does NOT shrink the aggregate", flush=True)
    print("q_min => the corrected super-polynomial target survives the attack that killed both", flush=True)
    print("per-prime routes.  Bounded search, evidence not proof.  RH stays [OUT].", flush=True)
