#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs.
No RH / RH-equivalent input.

THE OP1-CLOSING PER-PRIME CLAIM.  §6g PROVED e_max(A) >= floor := ceil(2m/(p+3))-1 for
every inert p and every on-line node set.  If the FIXED off-line vector's q_min inherits
this per-prime,

        (CLAIM)   v_p(q_min) >= floor = ceil(2m/(p+3)) - 1   for all valid collisions,

then  log q_min >= sum_{p<=2m-1} floor(p)*log p ~ 2m*sum log p/p ~ 2m*log(2m)  (Mertens)
=> q_min super-polynomial => OP1 CLOSES.  (For p > 2m-1 floor<=0 so the claim is trivial.)

This probe ADVERSARIALLY MINIMIZES v_p(q_min) over valid collisions and flags ANY violation
v_p(q_min) < floor, across ALL 3 off-line orbits, p in {7,11,13}, both regimes, clustered
AND spread node sets (de-biased: NOT build_pool's forced navail=m-1), with a light
coordinate-descent polish on the best random seed.  A single violation REFUTES the claim
(and localizes a real gap); none across the sweep is strong evidence for the OP1-closing
per-prime floor.

HONESTY (L5): bounded search, small m; DETECTS a break if one exists in range, else evidence
of survival, not proof.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import emax_smith
import discovery.probe_leg3_affine as A

ORBITS = [("D=425", Fr(3, 4), Fr(1)), ("D=4", Fr(2, 5), Fr(4, 5)), ("D=26", Fr(1), Fr(1, 5))]


def class_node_bases(p, want):
    seen, bases = set(), []
    c1 = A.xres(Fr(1), p)
    for t0 in range(1, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None and r != c1 and r not in seen:
            seen.add(r)
            bases.append(t0)
            if len(bases) >= want:
                break
    return bases


def pool_of(bn, assign, depths, p):
    ts = [bn[assign[k]] + p * depths[k] for k in range(len(assign))]
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    return [Fr(t) for t in ts]


def vpq(pool, sig, tau, m, p):
    oc, vo = cleared_columns(pool, sig, tau, m)
    q = qmin_fast(oc, vo)
    if not q:
        return None
    v, qq = 0, q
    while qq % p == 0:
        qq //= p
        v += 1
    return v


def emax_of(pool, sig, tau, m, p):
    oc, _ = cleared_columns(pool, sig, tau, m)
    return emax_smith(oc, m, p)[0]


def adv_min(sig, tau, p, m, ncls, S, rng, trials, polish):
    bn = class_node_bases(p, ncls)
    if len(bn) < ncls:
        return None
    best = None
    for _ in range(trials):
        assign = [k % ncls for k in range(m)]
        rng.shuffle(assign)
        depths = [rng.randrange(S) for _ in range(m)]
        pool = pool_of(bn, assign, depths, p)
        if pool is None:
            continue
        v = vpq(pool, sig, tau, m, p)
        if v is None:
            continue
        if best is None or v < best[0]:
            best = (v, list(assign), list(depths))
            if v == 0:
                break
    if best is None:
        return None
    # light coordinate-descent polish minimizing v_p(q_min)
    v, assign, depths = best
    for _ in range(polish):
        improved = False
        for j in range(m):
            bj, bd = v, depths[j]
            for sj in range(S):
                depths[j] = sj
                pool = pool_of(bn, assign, depths, p)
                if pool is None:
                    continue
                vv = vpq(pool, sig, tau, m, p)
                if vv is not None and vv < bj:
                    bj, bd = vv, sj
            depths[j] = bd
            if bj < v:
                v, improved = bj, True
        if not improved:
            break
    pool = pool_of(bn, assign, depths, p)
    em = emax_of(pool, sig, tau, m, p)
    return (v, em)


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("OP1-CLOSING CLAIM: v_p(q_min) >= floor=ceil(2m/(p+3))-1 for ALL valid collisions?", flush=True)
    print("Adversarially MINIMIZE v_p(q_min); flag any violation. 3 orbits, p in {7,11,13}.", flush=True)
    print("A per-prime floor => (Mertens) super-poly q_min => OP1 closes.  DISCOVERY. No RH.", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260817)
    violations = 0
    global_slack = None
    for name, sig, tau in ORBITS:
        print(f"\norbit {name} (sig={sig}, tau={tau}):", flush=True)
        for p in (7, 11, 13):
            navail_max = (p - 1) // 2
            for m in range(max(2, (p + 1) // 2), navail_max + 6):   # span p<=2m-1 (active) upward
                floor = ceil(2 * m / (p + 3)) - 1
                cell_min = None
                for ncls in sorted(set([2, min(3, navail_max), navail_max])):
                    if ncls < 2 or ncls > min(m, navail_max):
                        continue
                    res = adv_min(sig, tau, p, m, ncls, 36, rng, 120, polish=2)
                    if res is None:
                        continue
                    v, em = res
                    if cell_min is None or v < cell_min[0]:
                        cell_min = (v, em, ncls)
                if cell_min is None:
                    continue
                v, em, ncls = cell_min
                slack = v - floor
                flag = "" if slack >= 0 else "  *** VIOLATION ***"
                if slack < 0:
                    violations += 1
                if global_slack is None or slack < global_slack[0]:
                    global_slack = (slack, name, p, m, v, floor)
                print(f"   p={p:>2} m={m:>2} floor={floor:>2}: adv min v_p(q_min)={v:>2} "
                      f"(e_max={em}, best ncls={ncls}) slack={slack:+d}{flag}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print(f"TOTAL violations of v_p(q_min) >= floor: {violations}", flush=True)
    if global_slack:
        s, nm, p, m, v, fl = global_slack
        print(f"TIGHTEST: slack={s:+d} at orbit {nm}, p={p}, m={m} (v_p(q_min)={v}, floor={fl})", flush=True)
    if violations == 0:
        print("READING (L5): no valid collision beat the proved e_max floor at any prime, any", flush=True)
        print("orbit, in range => strong evidence for the per-prime q_min floor that (via", flush=True)
        print("Mertens) makes q_min super-polynomial and CLOSES OP1.  Evidence, not proof.", flush=True)
    else:
        print("READING (L5): a violation was found => the per-prime floor claim is FALSE as", flush=True)
        print("stated; inspect the witness — it localizes exactly where the transfer fails.", flush=True)
    print("RH stays [OUT].", flush=True)
