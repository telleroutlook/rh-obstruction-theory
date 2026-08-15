#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs.
No RH / RH-equivalent input.

OP1 LEG3 (§6r continuation): the min-psi PLATEAU splits BY REGIME.

The min-psi=3 witness (probe_leg3_witness) turned out to be navail = m-2, minPhi = 1 --
a DEGENERATE config where the t -> -t symmetry of x_of(t)=(4t^2-1)/(4t^2+1) collapses two
residue bases into ONE x-class.  Hypothesis:
  * NON-degenerate  (navail = m-1, minPhi = 0):  adversarial max min-psi = 2;
  * DEGENERATE ±    (navail = m-2, minPhi >= 1):  adversarial max min-psi = 3.
Both m-INDEPENDENT (=> lag=O(1)); the +1 is exactly the t->-t class-doubling.  This would
explain AND unify the §6h "lag plateaus at 3" observation.

This probe runs adversarial coordinate-ascent on VALID K=m collisions, BUCKETING each
found config by navail, and reports the max min-psi in each bucket per (p,m).

HONESTY (L5): local search, one orbit, small p,m.  If the buckets separate cleanly
(navail=m-1 -> <=2, navail=m-2 -> <=3) with NO growth in m, that is strong EVIDENCE for a
regime-split O(1) lag with absolute constant 3.  Not a proof.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
from collections import defaultdict
import random

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A
from discovery.probe_leg3_r2joint import build_pool


def navail_of(tl, p):
    c1 = A.xres(Fr(1), p)
    seen = set()
    for t in tl:
        r = A.xres(A.x_of(t), p)
        if r is not None and r != c1:
            seen.add(r)
    return len(seen)


def minpsi(u, tl, m, p):
    xs = [A.x_of(t) for t in tl]
    rows = [(A.Phi([xs[k] for k in S], p), S) for S in combinations(range(len(tl)), m - 1)]
    minPhi = min(ph for ph, _ in rows)
    best = None
    for ph, S in rows:
        if ph != minPhi:
            continue
        v = A.vpf(A.Psi_val(u, [xs[k] for k in S]), p)
        v = v if v is not None else 10**9
        best = v if best is None else min(best, v)
    return best


def search_bucketed(u, sig, tau, p, m, S, rng, restarts, buckets):
    r = m - 1
    if r < 1 or r >= p:
        return
    for _ in range(restarts):
        bases = rng.sample(range(1, p), r)
        svec = [rng.randrange(S) for _ in range(m)]
        improved = True
        guard = 0
        cur = -1
        while improved and guard < 40:
            guard += 1
            improved = False
            for j in range(m):
                bj, bs = cur, svec[j]
                for sj in range(S):
                    svec[j] = sj
                    pool = build_pool(bases, svec, p)
                    if pool is None:
                        continue
                    oc, vo = cleared_columns(pool, sig, tau, m)
                    if not qmin_fast(oc, vo):
                        continue
                    v = minpsi(u, pool, m, p)
                    v = v if (v is not None and v < 10**9) else -1
                    if v > bj:
                        bj, bs = v, sj
                svec[j] = bs
                if bj > cur:
                    cur, improved = bj, True
            # record the current pool's bucket each sweep
            pool = build_pool(bases, svec, p)
            if pool is not None:
                oc, vo = cleared_columns(pool, sig, tau, m)
                if qmin_fast(oc, vo):
                    v = minpsi(u, pool, m, p)
                    if v is not None and v < 10**9:
                        buckets[navail_of(pool, p)] = max(buckets[navail_of(pool, p)], v)


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 (§6r/regime): adversarial max min-psi BUCKETED by navail (K=m)",
          flush=True)
    print("Orbit D=425 (split-only).  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)
    sig, tau = Fr(3, 4), Fr(1)
    u = A.off_atoms_u(sig, tau)[0]
    rng = random.Random(20260816)

    print(f"\n{'p':>3} {'m':>3} {'#xcls':>6}   max min-psi by deficit d=(m-1)-navail",
          flush=True)
    grand = defaultdict(int)
    for p in (11, 19, 23, 31):
        nxcls = (p - 1) // 2            # available nonzero-t x-classes (t and -t collide)
        for m in (3, 4, 5, 6, 7):
            if m - 1 >= p:
                continue
            artifact = (m - 1) > nxcls   # cannot fill m-1 distinct x-classes => forced degen
            buckets = defaultdict(lambda: -1)
            for S in (81, 243):
                search_bucketed(u, sig, tau, p, m, S, rng, 10, buckets)
            # rebucket by deficit d = (m-1) - navail
            byd = defaultdict(lambda: -1)
            for navail, v in buckets.items():
                if v >= 0:
                    byd[(m - 1) - navail] = max(byd[(m - 1) - navail], v)
            summary = "  ".join(f"d={d}:{v}" for d, v in sorted(byd.items()))
            for d, v in byd.items():
                if not artifact:
                    grand[d] = max(grand[d], v)
            tag = "  (ARTIFACT: m-1>#xcls)" if artifact else ""
            print(f"{p:>3} {m:>3} {nxcls:>6}   {summary}{tag}", flush=True)

    print("\n" + "=" * 96, flush=True)
    print(f"GRAND max min-psi by deficit d (NON-artifact cells only): "
          f"{dict(sorted(grand.items()))}", flush=True)
    print("READING (L5): if max min-psi ≈ 2 + d and, for FIXED d, does NOT grow with m", flush=True)
    print("across non-artifact cells (p>=2m-1), then lag=O(1) per degeneracy level and the", flush=True)
    print("§6h plateau=3 is the d<=1 case.  The x_of ±-collision (only (p-1)/2 x-classes)", flush=True)
    print("sets when a config is forced degenerate.  EVIDENCE, not proof.  RH [OUT].",
          flush=True)
