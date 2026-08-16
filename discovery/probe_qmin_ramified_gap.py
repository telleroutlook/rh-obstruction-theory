#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bo — CLOSING THE {2,3}-GAP: the 6|n (2||n, 3|n) orbits are carried by a RAMIFIED prime dividing N(M).

§6bn found a clean complementarity over small primes: p=2 gives a linear q_min floor UNLESS v_2(n)=1
(n=2 mod 4), and p=3 gives one UNLESS 3|n.  The SOLE orbit class {2,3} cannot cover is v_2(n)=1 AND 3|n,
i.e. 6|n with 4-not-dividing-n; the smallest is sigma=5/6 (n=6).  There BOTH small primes are killed by
n's own factorization, so the barrier must live at a LARGER prime.  Candidate: the RAMIFIED primes -- the
odd primes dividing N(M), M = (p^2-q^2-np) + q(2p-n) i, rho=(p+qi)/n (the analog of {5,17} for D=425, which
is N(M) for sigma=3/4).  For sigma=5/6: Re(M)=25-36-30=-41, Im(M)=6*(10-6)=24, N(M)=41^2+24^2=2257=37*61.

This probe adversarially MINIMIZES v_p(q_min) for p in the ramified set {factors of N(M)} (plus 3 extended
to larger m) over the problematic 6|n orbits.  If a ramified prime carries a growing (linear) floor, then
the COMPLETE orbit-robustness map is:
    n = 0 mod 4         -> p=2 (S>=3, PROVED §6bm)
    n odd               -> p=2 (S<0, large)
    n = 2 mod 4, 3-not|n -> p=3 (3-unimodular, OB-42 mechanism)
    n = 2 mod 4, 3|n     -> a ramified prime | N(M)
covering EVERY off-line orbit -- the multi-prime resolution of OP1's orbit-robustness (§6bl(M) gap).

Exact integer q_min (SNF-free det/gcd).  Adversary one-sided = UPPER bound on the true min (L5).  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd
import random

from discovery.probe_qmin_p2_floor_identity import qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int


def rho_pqn(sig, tau):
    pn, pd = sig.numerator, sig.denominator
    qn, qd = tau.numerator, tau.denominator
    n = pd * qd // gcd(pd, qd)
    p = pn * (n // pd)
    q = qn * (n // qd)
    g = gcd(gcd(abs(p), abs(q)), n)
    return p // g, q // g, n // g


def factorize(n):
    n = abs(n)
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def ramified_primes(sig, tau):
    p, q, n = rho_pqn(sig, tau)
    ReM = p * p - q * q - n * p
    ImM = q * (2 * p - n)
    NM = ReM * ReM + ImM * ImM
    fac = factorize(NM)
    return NM, sorted(pp for pp in fac if pp % 2 == 1)   # odd ramified primes


def vp_qmin(ts, m, sig, tau, p):
    xs = [x_of(t) for t in ts]
    if len(set(xs)) != len(ts) or any(t == 0 for t in ts):
        return None
    q = qmin_exact_orbit(ts, m, sig, tau)
    if q is None or q <= 0:
        return None
    return vp_int(q, p)


def descent_min_vp(m, sig, tau, p, rng, restarts=16, rounds=6, pool_hi=48):
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
    print("=" * 100, flush=True)
    print("§6bo: for the 6|n orbits (p=2 & p=3 both killed), does a RAMIFIED prime | N(M) carry the floor?", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(5, 6), Fr(1)), (Fr(1, 6), Fr(1)), (Fr(7, 6), Fr(1))]  # all n=6 (2||n, 3|n)
    MS = (4, 5, 6, 7)
    rng = random.Random(20260816)

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        NM, ram = ramified_primes(sig, tau)
        print("\norbit (%s,%s): (p,q,n)=(%d,%d,%d), N(M)=%d, odd ramified primes=%s" % (
            sig, tau, p, q, n, NM, ram), flush=True)
        # test p=3 extended + each ramified prime
        for pp in [3] + ram[:3]:
            row = [descent_min_vp(m, sig, tau, pp, rng) for m in MS]
            row = ["." if v is None else str(v) for v in row]
            tag = "(ramified)" if pp in ram else "(small)"
            print("   p=%-3d %-11s adv-min v_p(q_min) m=4..7: [%s]" % (pp, tag, ",".join(row)), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if some ramified prime | N(M) shows a GROWING adv-min v_p, the 6|n gap closes and", flush=True)
    print("the {p=2, p=3, ramified|N(M)} set covers EVERY off-line orbit. Descent = UPPER bound. RH [OUT].", flush=True)
