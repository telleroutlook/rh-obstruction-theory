#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

SIMULTANEOUS-PIGEONHOLE / CRT-TENSION cross-table (§6ak) — the §6aj-reframed nucleus, tested directly.

§6aj: the adversarial-min q_min is SMOOTH (primes <= ~53) and its bits are an AGGREGATE over small primes;
the ramified {5,17} do NOT vanish jointly even though §6ae drained each prime INDIVIDUALLY.  The proposed
nucleus is a SIMULTANEOUS small-prime pigeonhole: sum_{p} v_p(q_min) log p >= c*m because the m nodes
cannot be aligned to few x-classes mod ALL small p at once -- draining one prime FORCES spreading mod
another (CRT tension).  This probe tests that mechanism head-on with a CROSS-TABLE:
   rows   = "run a descent that MINIMIZES v_p(q_min) for one target prime p" (should hit ~0, per §6ae),
   cols q = the RESULTING v_q(q_min) at that same config for every small q.
If the diagonal is ~0 (each prime individually drainable) but the OFF-diagonal is LARGE (zeroing p blows
up the other primes), that is the CRT tension made quantitative -- and log q_min stays >= c*m along every
row.  If instead some row zeroes MANY primes at once, the tension is weak and the aggregate floor is soft
(report honestly, L5).  Also reports, per row, total log2 q_min and #primes simultaneously zeroed.
Exact integer arithmetic (L9).  Bounded search.  One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17
SMALL = (3, 5, 7, 11, 13, 17, 19, 23)


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def vp_int(n, p):
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v


def qmin_of(ts, m):
    b = build(ts, m)
    if not b:
        return None
    q = qmin_fast(*b)
    return q if q and q >= 2 else None


def descent(ts, m, rng, key, rounds=20):
    """Coordinate descent minimizing key(q_min_int)."""
    best_ts = ts[:]
    q = qmin_of(best_ts, m)
    best = key(q) if q else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(8):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 320)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                q = qmin_of(cand, m)
                if not q:
                    continue
                v = key(q)
                if v < best - 1e-12:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts


def pigeon_floor(p, m):
    """§6d/§6g pigeonhole floor on v_p(D_m(A)) (numerator): ceil(2m/(p+3)) - 1."""
    return -(-2 * m // (p + 3)) - 1


if __name__ == "__main__":
    print("=" * 108, flush=True)
    print("CRT-TENSION CROSS-TABLE (§6ak): row = descent MINIMIZING v_p(q_min) for target p; entries =", flush=True)
    print("resulting v_q(q_min) for each small q. Diag~0 + large off-diag => zeroing one prime forces", flush=True)
    print("others up (simultaneous-pigeonhole floor). Compares to PH(p,m)=ceil(2m/(p+3))-1 (numerator).", flush=True)
    print("=" * 108, flush=True)
    rng = random.Random(20260816)
    for m in (4, 6, 7):
        print(f"\n----- m = {m} -----  (PH floor per p: " +
              ", ".join(f"{p}:{pigeon_floor(p, m)}" for p in SMALL) + ")", flush=True)
        head = "target\\v_q |" + "".join(f"{p:>5}" for p in SMALL) + " | log2 q | #zeroed"
        print(head, flush=True)
        print("-" * len(head), flush=True)
        # also a plain min-q row (minimize total log2 q_min)
        rows = [("minq", lambda q: log2(q))] + [(p, (lambda pp: (lambda q: vp_int(q, pp)))(p)) for p in SMALL]
        for tag, key in rows:
            # best of a few descents from random starts
            best_ts, best_key = None, float("inf")
            for _ in range(5):
                s0 = rng.sample(range(1, 320), m)
                ts = descent(s0, m, rng, key)
                q = qmin_of(ts, m)
                if q is None:
                    continue
                kv = key(q)
                if kv < best_key:
                    best_key, best_ts = kv, ts
            if best_ts is None:
                print(f"{str(tag):>10} | (no valid)", flush=True)
                continue
            q = qmin_of(best_ts, m)
            vps = [vp_int(q, p) for p in SMALL]
            zeroed = sum(1 for v in vps if v == 0)
            row = "".join(f"{v:>5}" for v in vps)
            label = "min-q" if tag == "minq" else f"min v_{tag}"
            print(f"{label:>10} |{row} | {log2(q):6.2f} | {zeroed:>7}", flush=True)
    print("\n" + "=" * 108, flush=True)
    print("READING (L5): if along EVERY row log2 q stays >= c*m and no row zeroes MANY primes at once (the", flush=True)
    print("off-diagonal stays large when the diagonal target -> 0), the small primes are NOT simultaneously", flush=True)
    print("drainable => a genuine CRT/pigeonhole floor. If some row zeroes most primes AND has small log2 q,", flush=True)
    print("the tension is weak and the aggregate floor is soft -- report honestly. One orbit (D=425).", flush=True)
    print("Bounded search. Evidence, not proof. RH stays [OUT].", flush=True)
