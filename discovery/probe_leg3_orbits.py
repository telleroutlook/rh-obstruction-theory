#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs.
No RH / RH-equivalent input.

OP1 LEG3 (§6r-note3 generalization): does the x-class-SLACK regime split for min-psi hold
across ALL THREE off-line orbits (D=425, D=4, D=26), not just D=425?

Claim to stress: at the hardest pool size K=m, adversarial max min-psi obeys
    min-psi <= 2   when x-class slack  slack_x := (p-1)/2 - (m-1) >= 1,
    min-psi <= 3   at the tight boundary slack_x = 0,
independently of which off-line orbit (u = a+bi) is used; small-p artifacts (p < 2m-1,
forced-degenerate) excluded.

FAST config: S=81 tuning depth, 8 restarts, p in {7,11,13}, only p >= 2m-1 cells, all 3
orbits.  Reports max min-psi per (orbit, slack_x sign).

HONESTY (L5): local search, small p,m.  Agreement across orbits STRENGTHENS the regime-
split evidence; disagreement would localize an orbit-dependent effect (report it).  Not a
proof.  RH stays [OUT].
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


def adv_max(u, sig, tau, p, m, S, rng, restarts):
    r = m - 1
    if r < 1 or r >= p:
        return None
    best_overall = -1
    for _ in range(restarts):
        bases = rng.sample(range(1, p), r)
        svec = [rng.randrange(S) for _ in range(m)]
        cur = -1
        improved, guard = True, 0
        while improved and guard < 30:
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
        best_overall = max(best_overall, cur)
    return best_overall


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 (§6r-note3): x-class-slack regime split ACROSS ALL 3 off-line orbits",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(20260816)

    grand = defaultdict(lambda: defaultdict(int))   # orbit -> slack_sign -> max
    for name, sig, tau in A.ORBITS:
        u = A.off_atoms_u(sig, tau)[0]
        print(f"\norbit {name}:", flush=True)
        for p in (7, 11, 13):
            nx = (p - 1) // 2
            for m in (3, 4, 5, 6):
                if m - 1 >= p or (m - 1) > nx:      # skip trivial + artifact
                    continue
                slack = nx - (m - 1)
                v = adv_max(u, sig, tau, p, m, 81, rng, 8)
                if v is None or v < 0:
                    continue
                sign = ">=1" if slack >= 1 else "=0"
                grand[name][sign] = max(grand[name][sign], v)
                print(f"   p={p:>2} m={m}  slack_x={slack}  -> max min-psi = {v}",
                      flush=True)

    print("\n" + "=" * 96, flush=True)
    print("GRAND max min-psi by (orbit, slack_x):", flush=True)
    ok = True
    for name in grand:
        s1 = grand[name].get(">=1", "-")
        s0 = grand[name].get("=0", "-")
        print(f"   {name}:  slack_x>=1 -> {s1}   slack_x=0 -> {s0}", flush=True)
        if isinstance(s1, int) and s1 > 2:
            ok = False
        if isinstance(s0, int) and s0 > 3:
            ok = False
    print("\nREADING (L5):", flush=True)
    if ok:
        print("across ALL orbits, slack_x>=1 -> min-psi<=2 and slack_x=0 -> min-psi<=3.", flush=True)
        print("The regime split is ORBIT-INDEPENDENT: LEG3's constant is governed by the", flush=True)
        print("x-class slack (p-1)/2-(m-1), not the specific curve.  Strengthens the §6r-", flush=True)
        print("note3 evidence.  Not a proof.  split-only OP1 OPEN.  RH [OUT].", flush=True)
    else:
        print("an orbit BREAKS the slack_x bound -> orbit-dependent effect (see rows above).", flush=True)
        print("HONEST negative; localize before claiming orbit-independence.  RH [OUT].", flush=True)
