#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE PIGEONHOLE-FORCED PER-p FLOOR (§6ae) — the potential UNCONDITIONAL nugget.

§6ad proved (empirically, exact) NON-ABSORPTION on clustered nodes: when c nodes share an
on-line x-class mod p, v_p(q_min) grows ~linearly in c (the augmented gcd does NOT absorb the
§6g confluence floor).  The adversary escapes only by SPREADING nodes over distinct x-classes.

BUT the number of finite on-line x-classes mod p is FIXED: N(p) = #{ r : r = x_of(t) mod p exists }.
§6ac found N(5)=2, N(17)=8.  By pigeonhole, ANY m nodes put >= ceil(m / N(p)) into one class =>
forced confluence depth ceil(m/N(p)) => (if §6ad non-absorption holds at that depth) an
UNCONDITIONAL floor  v_p(q_min) >= g( ceil(m/N(p)) ),  linear in m for FIXED p.  Small N(p) (p=5!)
makes this floor bite hard and early — the adversary CANNOT drain that p to 0.

This probe:
  T0  count N(p) exactly for p in {5,17} (and neighbours) — the pigeonhole capacity.
  T1  UNRESTRICTED per-p adversary: minimize v_p(q_min) over MANY node sets (random + spread +
      descent), for p=5 and p=17 separately, m=2..9.  If min v_5(q_min) STAYS >0 and grows while
      min v_17(q_min) -> 0, p=5 gives a per-p unconditional floor (clean rigorous target).
  T2  the pigeonhole-OPTIMAL config (nodes spread as evenly as possible over the N(p) classes,
      p-adically expanded within each) — the adversary's best case — measure v_p(q_min) vs the
      predicted floor from max class multiplicity c_max = ceil(m/N(p)).
Exact integer arithmetic only (L9).  Bounded search (evidence, not proof).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil
from collections import defaultdict
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vp
import discovery.probe_leg3_affine as A

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17


def classes_mod_p(p):
    """map residue r -> list of t0 in 1..p with x_of(t0) == r mod p (finite on-line classes)."""
    cls = defaultdict(list)
    for t0 in range(0, p):
        r = A.xres(A.x_of(Fr(t0)), p)
        if r is not None:
            cls[r].append(t0)
    return cls


def qmin_of(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return qmin_fast(oc, vo) or None


def vq(ts, m, p):
    q = qmin_of(ts, m)
    return vp(q, p) if q else None


def pigeonhole_optimal(cls_keys, p, m, rng):
    """spread m nodes as evenly as possible over the N(p) classes; p-adic expansion within."""
    N = len(cls_keys)
    counts = [m // N + (1 if i < m % N else 0) for i in range(N)]
    ts, used = [], set()
    for ci, r in enumerate(cls_keys):
        # pick counts[ci] nodes with x-residue r: t0 + p*y for the class rep t0
        # find a base t0 with that residue
        base = None
        for t0 in range(0, p):
            if A.xres(A.x_of(Fr(t0)), p) == r:
                base = t0; break
        if base is None:
            return None
        ys = rng.sample(range(0, 60), counts[ci])
        for y in ys:
            t = base + p * y
            if t != 0 and t not in used:
                used.add(t); ts.append(t)
    return ts if len(ts) == m else None


def adversary_min_vp(p, m, rng, cls_keys):
    """minimize v_p(q_min) over random + descent + pigeonhole-optimal node sets."""
    best = None
    def upd(ts):
        nonlocal best
        if ts and len(set(ts)) == m and all(t != 0 for t in ts):
            v = vq(ts, m, p)
            if v is not None and (best is None or v < best):
                best = v
    for _ in range(400):
        upd(rng.sample(range(1, 300), m))
    for _ in range(40):
        upd(pigeonhole_optimal(cls_keys, p, m, rng))
    # coordinate descent minimizing v_p from several starts
    for _ in range(20):
        cur = rng.sample(range(1, 300), m)
        cv = vq(cur, m, p)
        if cv is None:
            continue
        for _r in range(15):
            improved = False
            for i in range(m):
                for _ in range(6):
                    cand = cur[:]
                    cand[i] = rng.randrange(1, 300)
                    if len(set(cand)) != m or any(t == 0 for t in cand):
                        continue
                    v = vq(cand, m, p)
                    if v is not None and v < cv:
                        cv, cur, improved = v, cand, True
            if not improved:
                break
        if best is None or cv < best:
            best = cv
    return best


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("PIGEONHOLE-FORCED PER-p FLOOR (§6ae): N(p) finite on-line x-classes => forced confluence.", flush=True)
    print("=" * 100, flush=True)
    print("\n--- T0: N(p) = number of finite on-line x-classes mod p (pigeonhole capacity) ---", flush=True)
    for p in (3, 5, 7, 13, 17):
        cls = classes_mod_p(p)
        print(f"  p={p:>3}: N(p)={len(cls)}  classes(residues)={sorted(cls.keys())}", flush=True)

    print("\n--- T1: UNRESTRICTED per-p adversary min v_p(q_min) (can it reach 0?) ---", flush=True)
    print(f"{'m':>3} | {'min v_5(q_min)':>14} | {'ceil(m/2)-1':>11} | {'min v_17(q_min)':>15} | {'ceil(m/8)-1':>11}",
          flush=True)
    cls5 = sorted(classes_mod_p(5).keys())
    cls17 = sorted(classes_mod_p(17).keys())
    for m in range(2, 10):
        rng = random.Random(777 + m)
        v5 = adversary_min_vp(5, m, rng, cls5)
        rng = random.Random(9001 + m)
        v17 = adversary_min_vp(17, m, rng, cls17)
        f5 = max(0, ceil(m / max(1, len(cls5))) - 1)
        f17 = max(0, ceil(m / max(1, len(cls17))) - 1)
        print(f"{m:>3} | {str(v5):>14} | {f5:>11} | {str(v17):>15} | {f17:>11}", flush=True)

    print("\n--- T2: pigeonhole-OPTIMAL config (best adversary spread) v_p(q_min) vs forced-confluence ---",
          flush=True)
    print(f"{'m':>3} | {'p=5 v(q) [opt]':>14} | {'p=17 v(q) [opt]':>16}", flush=True)
    for m in range(2, 10):
        rng = random.Random(31337 + m)
        b5 = min([v for v in (vq(pigeonhole_optimal(cls5, 5, m, rng), m, 5) for _ in range(30)) if v is not None],
                 default=None)
        rng = random.Random(51337 + m)
        b17 = min([v for v in (vq(pigeonhole_optimal(cls17, 17, m, rng), m, 17) for _ in range(30)) if v is not None],
                  default=None)
        print(f"{m:>3} | {str(b5):>14} | {str(b17):>16}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): N(5)=2 is the crux. If T1 min v_5(q_min) stays >0 and grows ~m/2 while", flush=True)
    print("min v_17(q_min) -> 0 (N(17)=8, adversary spreads freely), then p=5 alone yields an", flush=True)
    print("UNCONDITIONAL per-p floor v_5(q_min) >= g(ceil(m/2)) — pigeonhole + §6ad non-absorption,", flush=True)
    print("the missing rigorous input for OP1's floor (log q_min >= c*m*log5, super-polynomial).", flush=True)
    print("If min v_5 -> 0 too, the per-p route fails and the floor stays purely aggregate (§6ab).", flush=True)
    print("Bounded search, one orbit (D=425). Evidence, not proof. RH stays [OUT].", flush=True)
