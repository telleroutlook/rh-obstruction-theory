#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE DRAIN-CONFLICT EXPERIMENT (decisive test of the §6aa/§6z-agg aggregate floor).  §6aa pinned
q_min into a GEOMETRIC channel (odd primes bounded above by G=prod(t_k^2-t_l^2)) and a RAMIFIED
channel ({5,17} from off-line atom norms).  Each channel ALONE is drainable (§6z-note; §6z-agg).
The aggregate floor — if real — must be the CONFLICT: no single node set drains BOTH at once.

This probe MAPS the (ram_log2, geo_log2) Pareto frontier over structured + random + descent-optimized
node sets, for each m, using THREE targeted attacks:
  (1) minimize GEOMETRIC only  (structured smooth families: consecutive / small / geometric t_k, and
      descent on geo);
  (2) minimize RAMIFIED only   (descent on v_5*log5 + v_17*log17; spread mod {5,17});
  (3) minimize the JOINT total log2 q_min (descent on the full quantity).
It reports, per m:  min ram (with geo there),  min geo (with ram there),  min TOTAL,  and the smallest
achieved max(ram,geo) — the closest any node set gets to draining BOTH.  If min-of-max stays bounded
away from 0 and min-TOTAL grows ~linearly (matching §6z-agg 4,18,39,46,77,96,102,129 for m=2..9), the
conflict — hence the aggregate floor — is CONFIRMED under the strongest joint attack.  If some node
set drives BOTH channels near 0 (min-of-max -> 0), OP1's barrier FAILS for this orbit and is reported
REFUTED (L5).  Exact SNF (L9).  Bounded search.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
from discovery.probe_leg3_pushm import vp
import discovery.probe_leg3_affine as A

SIG, TAU, RAM = Fr(3, 4), Fr(1), (5, 17)   # D=425


def qmin_of(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return qmin_fast(oc, vo) or None


def channels(q):
    """(ram_log2, geo_log2). ram = 5,17 part; geo = everything else."""
    ram = vp(q, 5) * log2(5) + vp(q, 17) * log2(17)
    return ram, log2(q) - ram


def geo_log(q):
    return channels(q)[1]


def ram_log(q):
    return channels(q)[0]


def spread_ok_ts(rng, m, hi=400):
    """nodes with distinct x-residues mod 5 and mod 17 (drains ramified)."""
    u5, u17, ts = set(), set(), []
    tries = 0
    while len(ts) < m and tries < 4000:
        tries += 1
        t = rng.randrange(1, hi)
        if t in ts:
            continue
        x = A.x_of(Fr(t))
        r5, r17 = A.xres(x, 5), A.xres(x, 17)
        if r5 is None or r17 is None or r5 in u5 or r17 in u17:
            continue
        u5.add(r5); u17.add(r17); ts.append(t)
    return ts if len(ts) == m else None


def descent(ts, m, rng, key, rounds=25):
    """coordinate descent minimizing key(q) over valid collisions."""
    best_ts = ts[:]
    q = qmin_of(best_ts, m)
    best = key(q) if q else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(6):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 400)
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


def structured_families(m):
    fams = []
    for c in (1, 2, 3, 5, 10, 20):
        fams.append(list(range(c, c + m)))                 # consecutive (geo-smooth)
    for r in (2, 3):
        g = [r ** k for k in range(1, m + 1)]              # geometric
        if len(set(g)) == m:
            fams.append(g)
    fams.append([2 * k + 1 for k in range(m)])             # odd numbers
    fams.append([2 ** k + 1 for k in range(1, m + 1)])     # 2^k+1
    return [f for f in fams if len(set(f)) == m]


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("DRAIN-CONFLICT (D=425): can any node set drain BOTH channels? map (ram,geo) frontier.", flush=True)
    print("§6z-agg min-TOTAL baseline (m=2..9): 4.00 18.16 39.22 45.78 76.94 95.77 101.59 129.32", flush=True)
    print("=" * 100, flush=True)
    print(f"{'m':>3} | {'min ram (geo@)':>16} | {'min geo (ram@)':>16} | {'min TOTAL':>10} | "
          f"{'min max(r,g)':>12}", flush=True)
    rng = random.Random(1732051)
    for m in range(3, 9):
        pts = []   # (ram, geo)
        def record(ts):
            if ts and len(set(ts)) == m:
                q = qmin_of(ts, m)
                if q:
                    pts.append(channels(q))
        # structured
        for f in structured_families(m):
            record(f)
        # random
        for _ in range(150):
            record(rng.sample(range(1, 400), m))
        # spread (ramified-drain seeds)
        for _ in range(30):
            record(spread_ok_ts(rng, m))
        # descent: minimize geo, ram, total from several starts
        for _ in range(6):
            s = rng.sample(range(1, 400), m)
            record(descent(s, m, rng, geo_log))
            record(descent(s, m, rng, ram_log))
            record(descent(s, m, rng, lambda q: log2(q)))
        # also descent on total from structured smooth starts
        for f in structured_families(m)[:4]:
            record(descent(f, m, rng, lambda q: log2(q)))
        if not pts:
            print(f"{m:>3} | (no valid points)", flush=True)
            continue
        min_ram = min(pts, key=lambda rg: rg[0])
        min_geo = min(pts, key=lambda rg: rg[1])
        min_tot = min(r + g for r, g in pts)
        min_max = min(max(r, g) for r, g in pts)
        print(f"{m:>3} | {min_ram[0]:6.2f} ({min_ram[1]:6.2f}) | "
              f"{min_geo[1]:6.2f} ({min_geo[0]:6.2f}) | {min_tot:10.2f} | {min_max:12.2f}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): 'min ram (geo@)' shows the geo cost paid when ramified is minimized; 'min geo", flush=True)
    print("(ram@)' the ramified cost when geo is minimized. If these are ANTI-correlated (small one =>", flush=True)
    print("large other) and 'min max(r,g)' stays bounded away from 0 while min-TOTAL ~ the §6z-agg line,", flush=True)
    print("the two-channel CONFLICT is confirmed: no node set drains both, so the aggregate floor holds.", flush=True)
    print("If 'min max(r,g)' -> 0, some node set drained BOTH and OP1's barrier FAILS here (report it).", flush=True)
    print("Bounded search, one orbit. Evidence, not proof. RH stays [OUT].", flush=True)
