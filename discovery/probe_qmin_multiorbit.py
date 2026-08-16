#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

MULTI-ORBIT GENERALITY of the p=3 floor (§6bb) — is v_3(q_min) >= m/2 - O(1) a D=425 artifact, or general?

Every §6a* result used ONE orbit (sigma=3/4, tau=1, D=425).  The on-line matrix (Chebyshev nodes x_of(t)) is
orbit-INDEPENDENT; the floor's orbit-dependence is ENTIRELY through the off-line vector d = O_orbit_direct
(sigma,tau) -> w = B^{-1} d -> C_j.  N_j (pairwise 3-adic valuations of on-line nodes) is orbit-free.  So the
floor per orbit = adversarial-min over node sets of max_j (N_j - C_j^{orbit}).  This probe scans a grid of
orbits (sigma, tau) and reports, at p=3, for m=4..7:
  * whether w = B^{-1} d is 3-adically UNIT (min v_3(w_i) >= 0 => 3-good orbit, cf §6av: needs 3 not dividing
    the orbit denominators),
  * the adversarial-MIN floor (random-restart coordinate descent = one-sided UPPER bound on the true min),
    compared to m/2.
Grid: 3-GOOD orbits (denominators of sigma, tau coprime to 3) AND 3-BAD orbits (sigma=2/3 or tau=3, 3 | data)
to see whether p=3 is special to 3-good orbits.  Exact (L9).  Honest (L5): random-min is an UPPER bound on
min-floor; if a 3-good orbit shows floor << m/2 the generality claim weakens (reported plainly).  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_Cj_bilinear import Bmatrix, solve_lower, vp_frac, x_of
from discovery.probe_qmin_Cj_lift_attack import node_poly_coeffs, S_of_nodes
from discovery.probe_covolume_floor import O_orbit_direct

P = 3


def xs_of(ts):
    return [x_of(t) for t in ts]


def floor_NC(ts, w):
    m = len(ts); xs = xs_of(ts)
    best = -10**9
    for j in range(m):
        Nj = sum(vp_frac(xs[j] - xs[k], P) for k in range(m) if k != j)
        Xp = [xs[k] for k in range(m) if k != j]
        Cj = vp_frac(S_of_nodes(Xp, w), P)
        best = max(best, Nj - Cj)
    return best


def min_floor(m, w, rng, restarts=40, rounds=8):
    best = None
    for _ in range(restarts):
        ts = rng.sample(range(1, 500), m)
        if len(set(xs_of(ts))) != m:
            continue
        cur = floor_NC(ts, w)
        for _rnd in range(rounds):
            improved = False
            for i in range(m):
                for _ in range(5):
                    cand = ts[:]; cand[i] = rng.randrange(1, 500)
                    if len(set(cand)) != m or len(set(xs_of(cand))) != m:
                        continue
                    v = floor_NC(cand, w)
                    if v < cur:
                        ts, cur, improved = cand, v, True
            if not improved:
                break
        if best is None or cur < best:
            best = cur
    return best


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("§6bb: is the p=3 floor v_3(q_min) >= m/2 - O(1) a D=425 artifact or GENERAL across orbits?", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(20260816)

    # (sigma, tau, label): 3-good (denominators coprime to 3) and 3-bad (3 divides sigma/tau data)
    orbits = [
        (Fr(3, 4), Fr(1), "3-good D=425 (baseline)"),
        (Fr(3, 4), Fr(2), "3-good tau=2"),
        (Fr(5, 8), Fr(1), "3-good sigma=5/8"),
        (Fr(7, 8), Fr(1), "3-good sigma=7/8"),
        (Fr(4, 5), Fr(1), "3-good sigma=4/5"),
        (Fr(2, 3), Fr(1), "3-BAD  sigma=2/3 (3|den)"),
        (Fr(3, 4), Fr(3), "3-BAD  tau=3 (3|tau)"),
    ]

    for sigma, tau, label in orbits:
        print(f"\n--- orbit sigma={sigma}, tau={tau}  [{label}] ---", flush=True)
        print(f"    {'m':>3} | {'min v_3(w_i)':>12} | {'w all 3-units?':>14} | {'min-floor':>9} | {'m/2':>4} | {'>=m/2-2?':>8}",
              flush=True)
        for m in (4, 5, 6, 7):
            B = Bmatrix(m)
            d = O_orbit_direct(sigma, tau, m)
            w = solve_lower(B, d, m)
            vws = [vp_frac(wi, P) for wi in w]
            allunit = all(v == 0 for v in vws)
            mf = min_floor(m, w, rng)
            print(f"    {m:>3} | {min(vws):>12} | {str(allunit):>14} | {str(mf):>9} | {m/2:>4} | "
                  f"{str(mf is not None and mf >= m/2 - 2):>8}", flush=True)

    print("\n" + "=" * 96, flush=True)
    print("READING (L5): if 3-GOOD orbits (w all 3-units) show min-floor >= m/2 - O(1) like D=425, the p=3", flush=True)
    print("floor is a GENERAL phenomenon (=> OP1's q_min bound is not orbit-special; worth a general proof).", flush=True)
    print("If 3-BAD orbits (w NOT all units) behave differently (floor smaller/larger), that confirms the", flush=True)
    print("mechanism is '3 unramified in the orbit'. Random-min = UPPER bound on min-floor. RH stays [OUT].", flush=True)
