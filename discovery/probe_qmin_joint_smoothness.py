#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE JOINT (RAM-DRAINED) SMOOTHNESS FLOOR (§6af) — moving S-unit finiteness onto q_min ITSELF.

State of play after §6ad/§6ae: the barrier is IRREDUCIBLY AGGREGATE.  Per-p fails (v_5, v_17 each
drainable to 0).  §6ab: the ramified channel as a whole is drainable too (some node set gives
v_5=v_17=0), but then geometric log2 q_min blows up.  §6ac's S-unit horn was on G=prod(t_k^2-t_l^2),
which suffers CANCELLATION: v_p(q_min) <= v_p(G) only, so a large prime in G need NOT survive into
q_min.  That gap killed the G-route.

NEW ANGLE: forget G.  Apply the smoothness/finiteness argument to q_min DIRECTLY.  Define the
RAM-DRAINED LOCUS = node sets with v_5(q_min)=v_17(q_min)=0 (ramified channel fully drained).  The
JOINT conjecture (the sole surviving OP1 target) becomes:

    (JS)  on the ram-drained locus, q_min cannot be {2,3,5,17}-smooth for large m; moreover the number
          of DISTINCT primes > 17 dividing q_min GROWS with m (=> log q_min super-poly by prime-count).

This probe adversarially searches the ram-drained locus and measures, per m:
  * whether v_5=v_17=0 is even ACHIEVABLE (confirm §6ab);
  * min log2 q_min SUBJECT TO ram=0 (the pure-geometric residual the adversary must pay);
  * on that minimizer, the NUMBER of distinct primes >17 in q_min and the LARGEST such prime;
  * a control: min log2 q_min with NO ram constraint (the true aggregate min, §6z-agg line).
If (min log2 q_min | ram=0) and the large-prime COUNT both grow with m, (JS) is supported and the
S-unit argument transfers to q_min itself — the missing rigorous mechanism.  If the adversary keeps
q_min {2,3,5,17}-smooth on the ram-drained locus, (JS) is REFUTED and reported (L5).
Exact integer arithmetic (L9).  Bounded search (evidence, not proof).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vp
import discovery.probe_leg3_affine as A

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17
S = (2, 3, 5, 17)


def qmin_of(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return qmin_fast(oc, vo) or None


def ram(q):
    return vp(q, 5) * log2(5) + vp(q, 17) * log2(17)


def large_primes(q):
    """(count distinct primes >17, largest such prime, their total log2 mass) dividing q."""
    n = abs(int(q))
    for p in S:
        while n % p == 0:
            n //= p
    cnt, largest, mass, d = 0, 0, 0.0, 3
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d; e += 1
            if d > 17:
                cnt += 1; largest = max(largest, d); mass += e * log2(d)
        d += 2
    if n > 1:
        if n > 17:
            cnt += 1; largest = max(largest, n); mass += log2(n)
    return cnt, largest, mass


def descent(ts, m, rng, key, rounds=18):
    best_ts = ts[:]
    q = qmin_of(best_ts, m)
    best = key(q) if q else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(6):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 350)
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
    print("JOINT RAM-DRAINED SMOOTHNESS FLOOR (§6af): apply finiteness to q_min ITSELF, not G.", flush=True)
    print("On the locus v_5(q_min)=v_17(q_min)=0, measure min log2 q_min and its large-prime (>17) count.", flush=True)
    print("=" * 100, flush=True)
    print(f"{'m':>3} | {'ram=0 reachable':>15} | {'min log2 q|ram=0':>16} | {'#primes>17':>10} | "
          f"{'largest p':>9} | {'aggregate min':>13}", flush=True)
    rng = random.Random(2026081602)
    import os
    LO = int(os.environ.get("MLO", "2"))
    HI = int(os.environ.get("MHI", "9"))
    NR = int(os.environ.get("NRAND", "500"))
    ND = int(os.environ.get("NDESC", "25"))
    for m in range(LO, HI):
        # penalty key: strongly penalize any ramified content, then minimize total log2 among ram-free
        def ram_free_key(q):
            r = vp(q, 5) + vp(q, 17)
            return (r * 10_000.0) + log2(q)          # ram is dominated; among ram=0, minimize log2 q
        cand_pts = []      # (log2 q, count>17, largest, ts) over ram-free node sets found
        agg_min = None     # unconstrained min log2 q (control)
        def consider(ts):
            global agg_min
            if not ts or len(set(ts)) != m or any(t == 0 for t in ts):
                return
            q = qmin_of(ts, m)
            if not q:
                return
            lg = log2(q)
            agg_min = lg if agg_min is None else min(agg_min, lg)
            if vp(q, 5) == 0 and vp(q, 17) == 0:
                cnt, largest, _mass = large_primes(q)
                cand_pts.append((lg, cnt, largest, ts[:]))
        # broad random
        for _ in range(NR):
            consider(rng.sample(range(1, 350), m))
        # descent toward ram-free-then-small, from many starts
        for _ in range(ND):
            s = rng.sample(range(1, 350), m)
            consider(descent(s, m, rng, ram_free_key))
            consider(descent(s, m, rng, lambda q: log2(q)))   # also feed the aggregate control
        if not cand_pts:
            print(f"{m:>3} | {'NO':>15} | {'(ram=0 not found)':>16} | {'-':>10} | {'-':>9} | "
                  f"{(f'{agg_min:.2f}' if agg_min else '-'):>13}", flush=True)
            continue
        best = min(cand_pts, key=lambda z: z[0])
        lg, cnt, largest, ts = best
        print(f"{m:>3} | {'YES':>15} | {lg:16.2f} | {cnt:>10} | {largest:>9} | "
              f"{(f'{agg_min:.2f}' if agg_min else '-'):>13}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if 'min log2 q|ram=0' GROWS and '#primes>17' GROWS with m, the ramified-drained", flush=True)
    print("locus forces q_min to carry a growing large-prime part — moving S-unit finiteness onto q_min", flush=True)
    print("ITSELF (no G-cancellation gap). That is the JOINT mechanism OP1 needs. If the adversary keeps", flush=True)
    print("q_min {2,3,5,17}-smooth with ram=0 (count stays 0, log2 stays small), (JS) is REFUTED here.", flush=True)
    print("Bounded search, one orbit (D=425). Evidence, not proof. RH stays [OUT].", flush=True)
