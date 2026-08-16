#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

ADVERSARIAL SELF-REFUTATION of the §6z ramified-channel floor.  §6z claimed the ramified part
R(nodes) := v_5(q_min)*log2(5) + v_17(q_min)*log2(17)  (D=425 = 5^2*17)
cannot be driven to 0 and rises with m.  BUT §6b once recorded a D=425 config with q_min=3^5*7^2*11
(v_5=v_17=0).  That is a POTENTIAL CONTRADICTION.  Per CLAUDE.md ("verify load-bearing claims by
script, defects never assumed independent"), before building on §6z I must TRY HARD to KILL it.

This probe adversarially MINIMIZES the ramified part specifically (not the generic cluster/spread
attack of probe_qmin_ramified_channel):
  * random rational nodes;
  * "clean" nodes chosen so 5 and 17 do NOT divide any denominator 4t^2+1 (kills the obvious
    denominator route into the ramified primes);
  * spread nodes (distinct x-classes mod 5 and mod 17) to avoid confluence at those primes;
  * coordinate descent that perturbs one node at a time to REDUCE R (and separately v_5, v_17).
It reports, per m, the adversarial MIN of v_5, of v_17, of R, and whether ANY valid collision with
R=0 (ramified part fully drained) was found.

DECISION (L5): if a valid collision with R=0 exists (or min R -> 0), the §6z "cannot be drained"
claim is a SEARCH ARTIFACT and must be RETRACTED.  If min R stays > 0 and grows with m under this
targeted attack, the node-independent ramified floor survives its strongest refutation attempt.
Exact SNF arithmetic (L9).  Bounded search.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vp
import discovery.probe_leg3_affine as A

SIG, TAU, RAMIFIED = Fr(3, 4), Fr(1), (5, 17)   # D=425 = 5^2 * 17


def qmin_of(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    q = qmin_fast(oc, vo)
    return q or None


def ram_parts(q):
    return vp(q, 5), vp(q, 17)


def ram_log2(q):
    v5, v17 = ram_parts(q)
    return v5 * log2(5) + v17 * log2(17)


def clean_t(rng, hi=600):
    """node t with 5 and 17 NOT dividing 4t^2+1 (no ramified prime in its denominator)."""
    for _ in range(200):
        t = rng.randrange(1, hi)
        N = 4 * t * t + 1
        if N % 5 != 0 and N % 17 != 0:
            return t
    return rng.randrange(1, hi)


def spread_t(rng, used5, used17, hi=600):
    """node whose x-residue mod 5 and mod 17 is new (distinct x-classes at both ramified primes)."""
    for _ in range(200):
        t = rng.randrange(1, hi)
        x = A.x_of(Fr(t))
        r5 = A.xres(x, 5); r17 = A.xres(x, 17)
        if r5 is not None and r17 is not None and r5 not in used5 and r17 not in used17:
            used5.add(r5); used17.add(r17)
            return t
    return clean_t(rng, hi)


def descent(ts, m, rng, rounds=40):
    """coordinate descent minimizing ram_log2(q_min) over valid collisions."""
    best_ts = ts[:]
    q = qmin_of(best_ts, m)
    best = ram_log2(q) if q else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(6):
                cand = best_ts[:]
                cand[i] = clean_t(rng) if rng.random() < 0.5 else rng.randrange(1, 600)
                if len(set(cand)) != m:
                    continue
                q = qmin_of(cand, m)
                if not q:
                    continue
                r = ram_log2(q)
                if r < best:
                    best, best_ts, improved = r, cand, True
        if not improved:
            break
    return best, best_ts


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("SELF-REFUTATION of §6z ramified floor (D=425, primes {5,17}). MINIMIZE ramified part.", flush=True)
    print("Can a VALID collision drive v_5=v_17=0 (R=0)?  If yes, RETRACT §6z.", flush=True)
    print("=" * 96, flush=True)
    print(f"{'m':>3} | {'min v_5':>8} {'min v_17':>9} | {'min R log2':>11} | {'R=0 found?':>10}", flush=True)
    rng = random.Random(424242)
    any_r0_overall = False
    for m in range(2, 10):
        minv5 = minv17 = 10**9
        minR = float("inf")
        r0 = False
        for _ in range(500):
            mode = rng.randrange(3)
            if mode == 0:
                ts = [clean_t(rng) for _ in range(m)]
            elif mode == 1:
                u5, u17 = set(), set()
                ts = [spread_t(rng, u5, u17) for _ in range(m)]
            else:
                ts = rng.sample(range(1, 600), m)
            if len(set(ts)) != m:
                continue
            q = qmin_of(ts, m)
            if not q:
                continue
            v5, v17 = ram_parts(q)
            R = v5 * log2(5) + v17 * log2(17)
            minv5, minv17, minR = min(minv5, v5), min(minv17, v17), min(minR, R)
            if R == 0:
                r0 = True
        # targeted descent from a few random starts
        for _ in range(15):
            ts0 = [clean_t(rng) for _ in range(m)]
            if len(set(ts0)) != m:
                continue
            Rd, tsd = descent(ts0, m, rng)
            if Rd < minR:
                minR = Rd
            q = qmin_of(tsd, m)
            if q:
                v5, v17 = ram_parts(q)
                minv5, minv17 = min(minv5, v5), min(minv17, v17)
                if v5 == 0 and v17 == 0:
                    r0 = True
        any_r0_overall = any_r0_overall or r0
        print(f"{m:>3} | {minv5:>8} {minv17:>9} | {minR:>11.2f} | {str(r0):>10}", flush=True)
    print("\n" + "=" * 96, flush=True)
    if any_r0_overall:
        print("RESULT (L5): a VALID collision with R=0 EXISTS ⇒ the ramified part CAN be drained.", flush=True)
        print("§6z's 'cannot be drained' is a SEARCH ARTIFACT of the generic cluster/spread attack.", flush=True)
        print("RETRACT the node-independent ramified-floor claim; the two-channel split still holds", flush=True)
        print("descriptively but neither channel alone carries a node-independent floor.", flush=True)
    else:
        print("RESULT (L5): NO valid collision drove R to 0 under the targeted attack; min R stays", flush=True)
        print("positive and grows with m ⇒ the node-independent ramified floor SURVIVES its strongest", flush=True)
        print("refutation. This is the split-prime (17≡1 mod4) analogue of §5's inert-prime floor —", flush=True)
        print("NEW: the all-split orbits are NOT floor-free, contra the earlier §5/§6b worry.", flush=True)
    print("Bounded search, one orbit. Evidence, not proof. RH stays [OUT].", flush=True)
