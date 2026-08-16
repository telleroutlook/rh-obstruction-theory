#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bn — MULTI-PRIME COMPLEMENTARITY: does EVERY off-line orbit have SOME small prime with a linear floor?

MOTIVATION.  §6bm PROVED the p=2 floor v_2(q_min) >= 2m-2-S for the 4|n opposite-parity orbit family
(S = 2 v_2(n) - 1 >= 3).  The closed form S = 2 v_2(n) - 1 - v_2(N(M))/2 (rho=(p+qi)/n, M=(p^2-q^2-np)+
q(2p-n)i) splits the p=2 channel cleanly by n mod 4:
    * n = 0 mod 4  ->  S >= 3   -> p=2 floor PROVED LINEAR (§6bm).
    * n odd        ->  S <  0   -> beta has 2 in the DENOMINATOR; p=2 floor empirically LARGE (§6bl), unproved.
    * n = 2 mod 4  ->  S =  1   -> p=2 VACUOUS (§6bl borderline).  <-- the ONLY orbit class p=2 cannot cover.

OP1 (orbit-robust) needs: for EVERY off-line orbit rho, inf over node sets of log q_min = omega(log m).
A single prime p with a UNIFORM (all-nodes) linear floor v_p(q_min) >= c*m suffices for that orbit.  The
open gap is entirely the n=2 mod 4 class.  THIS PROBE tests the COMPLEMENTARITY CONJECTURE:

    (COMP)  For every off-line orbit, THERE EXISTS a small prime p in {2,3,5} with
            adv-min over node sets of v_p(q_min) growing LINEARLY in m.

Method: for each orbit and each p in {2,3,5}, run a coordinate descent that AGGRESSIVELY MINIMIZES
v_p(q_min) (= the OP1 danger direction; descent gives an UPPER bound on the true adversarial min).  If the
descent still cannot drive v_p below a linear trend, that prime carries a uniform floor for the orbit.
The conjecture is that the p=2-vacuous (n=2 mod 4) orbits are exactly where p=3 or p=5 takes over.

Exact integer q_min via qmin_exact_orbit (SNF-free det/gcd).  Adversary one-sided (L5).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd
import random

from discovery.probe_qmin_p2_floor_identity import qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int


def rho_pqn(sig, tau):
    """rho = sig + i tau = (p + q i)/n in lowest terms."""
    pn, pd = sig.numerator, sig.denominator
    qn, qd = tau.numerator, tau.denominator
    n = pd * qd // gcd(pd, qd)
    p = pn * (n // pd)
    q = qn * (n // qd)
    g = gcd(gcd(abs(p), abs(q)), n)
    return p // g, q // g, n // g


def v2_slope_closed_form(sig, tau):
    """S = v_2(beta) = 2 v_2(n) - 1 - v_2(N(M))/2 (Fraction; may be half-integer)."""
    p, q, n = rho_pqn(sig, tau)
    ReM = p * p - q * q - n * p
    ImM = q * (2 * p - n)
    NM = ReM * ReM + ImM * ImM
    return Fr(2 * vp_int(n, 2) - 1) - Fr(vp_int(NM, 2), 2), n


def distinct_x_set(ts):
    xs = [x_of(t) for t in ts]
    return len(set(xs)) == len(ts) and all(t != 0 for t in ts)


def vp_qmin(ts, m, sig, tau, p):
    if not distinct_x_set(ts):
        return None
    q = qmin_exact_orbit(ts, m, sig, tau)
    if q is None or q <= 0:
        return None
    return vp_int(q, p)


def descent_min_vp(m, sig, tau, p, rng, restarts=14, rounds=6, pool_hi=40):
    """Coordinate descent MINIMIZING v_p(q_min).  Returns the min v_p found (UPPER bound on adv-min)."""
    best = None
    pool = list(range(1, pool_hi + 1))
    for _ in range(restarts):
        ts = rng.sample(pool, m)
        cur = vp_qmin(ts, m, sig, tau, p)
        if cur is None:
            continue
        for _ in range(rounds):
            improved = False
            for idx in range(m):
                for cand in pool:
                    if cand in ts:
                        continue
                    trial = ts[:]
                    trial[idx] = cand
                    v = vp_qmin(trial, m, sig, tau, p)
                    if v is not None and v < cur:
                        cur, ts, improved = v, trial, True
            if not improved:
                break
        if best is None or cur < best:
            best = cur
        if best == 0:
            break
    return best


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6bn: multi-prime complementarity — does EVERY orbit have a small prime with a linear q_min floor?", flush=True)
    print("=" * 104, flush=True)

    # Orbits spanning all three n mod 4 classes.  Tag each with its p=2 status from the closed form.
    ORBITS = [
        (Fr(3, 4), Fr(1)),   # n=4  (0 mod4) -> p=2 PROVED
        (Fr(5, 8), Fr(1)),   # n=8  (0 mod4) -> p=2 PROVED
        (Fr(5, 6), Fr(1)),   # n=6  (2 mod4) -> p=2 VACUOUS  <-- test complement
        (Fr(9, 10), Fr(1)),  # n=10 (2 mod4) -> p=2 VACUOUS  <-- test complement
        (Fr(3, 10), Fr(1)),  # n=10 (2 mod4) -> p=2 VACUOUS  <-- test complement
        (Fr(2, 3), Fr(1)),   # n=3  (odd)    -> p=2 S<0 large
        (Fr(4, 5), Fr(1)),   # n=5  (odd)    -> p=2 S<0 large
    ]

    MS = (4, 5, 6, 7)
    PRIMES = (2, 3, 5)
    rng = random.Random(20260816)

    print("\n%-12s %-8s %-7s  %s" % ("(sig,tau)", "nmod4", "S(p2)", "adv-min v_p(q_min) per prime, m=4..7"), flush=True)
    for sig, tau in ORBITS:
        S, n = v2_slope_closed_form(sig, tau)
        cells = []
        for p in PRIMES:
            row = [descent_min_vp(m, sig, tau, p, rng) for m in MS]
            row = ["." if v is None else str(v) for v in row]
            cells.append("p%d:[%s]" % (p, ",".join(row)))
        print("%-12s %-8s %-7s  %s" % ("(%s,%s)" % (sig, tau), "%d" % (n % 4), str(S), "  ".join(cells)), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("READING (L5): for each orbit, is there a prime whose adv-min v_p(q_min) GROWS with m (linear floor)?", flush=True)
    print("If EVERY row has such a prime -> COMPLEMENTARITY holds -> OP1 orbit-robust via {2,3,5}. Descent =", flush=True)
    print("UPPER bound on the true adv-min, so a row that stays >0 and grows is strong floor evidence. RH [OUT].", flush=True)
