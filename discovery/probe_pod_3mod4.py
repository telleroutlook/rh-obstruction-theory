#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

DECISIVE test of a UNIFORM (over ALL on-line node sets) rigorous lower bound.

Mechanism.  On-line conductors are always  N_k = 4 a^2 + b^2  (t_k = a/b
primitive).  For a prime p == 3 (mod 4):  4a^2+b^2 == 0 (mod p) would give
(2a/b)^2 == -1 (mod p), impossible since -1 is a non-residue mod p; and p | b
forces p | a (non-primitive).  Hence  p ∤ N_k for EVERY on-line node.

So the on-line value C_j(t_k) = 8(1 - T_j(x_k)),  x_k rational with denominator |
N_k^j, is p-INTEGRAL for every p == 3 (mod 4).  If the OFF-LINE observation
vector d_j carries p in its denominator to order growing like j*v_p(D) (D = the
off-line conductor), then in the collision  sum_k c_k C_j + q d_j = 0  the term
q d_j can only be p-adically balanced by raising v_p(q):  at j = m this forces
        v_p(q) >= m * v_p(D)    =>    |q| >= p^{m v_p(D)}    (EXPONENTIAL),
uniformly over ALL on-line node choices and counts K.

This probe:
 (1) picks off-line orbits whose conductor D has a prime p == 3 (mod 4);
 (2) reports v_p(denominator of d_m) to confirm it ~ m * v_p(D);
 (3) measures v_p(q_min) across many on-line families (incl. large K,
     prime-matched attempts) and checks v_p(q_min) >= m * v_p(D).
If (3) holds uniformly, the uniform exponential bound is empirically confirmed
for this off-line subclass (=> OP1 proved for off-line targets with a 3-mod-4
conductor prime -- a large explicit family; adversary escapes only by using a
pure sum-of-two-squares conductor).
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd
import discovery.probe_overdetermined_collision as P
from discovery.probe_covolume_floor import O_orbit_direct
from discovery.probe_qmin_snf import cleared_columns, qmin_index


def vp(n, p):
    """p-adic valuation of integer n (n!=0)."""
    n = abs(int(n))
    if n == 0:
        return float("inf")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def vp_frac(fr, p):
    """p-adic valuation of a Fraction."""
    return vp(fr.numerator, p) - vp(fr.denominator, p)


def offline_conductor_primes(sigma, tau):
    """Return dict {p: v_p(D)} for the off-line conductor D = num(N(rho)) *
    num(N(rho-1)), N(z)=Re(z)^2+Im(z)^2, and flag which p are == 3 mod 4."""
    sigma, tau = Fr(sigma), Fr(tau)
    Nrho = sigma * sigma + tau * tau
    Nrm1 = (sigma - 1) * (sigma - 1) + tau * tau
    D = Nrho.numerator * Nrm1.numerator
    # factor D
    facs = {}
    d = D
    f = 2
    while f * f <= d:
        while d % f == 0:
            facs[f] = facs.get(f, 0) + 1
            d //= f
        f += 1
    if d > 1:
        facs[d] = facs.get(d, 0) + 1
    return D, facs


def node_families(m, Kmax):
    for K in range(m + 1, Kmax + 1):
        yield (f"half-int K={K}", [Fr(1, 2) + Fr(i) for i in range(K)])
        yield (f"integer  K={K}", [Fr(i) for i in range(1, K + 1)])
        yield (f"small-frac K={K}", [Fr(1, 2)] + [Fr(1, d) for d in range(2, K + 1)])
        yield (f"thirds   K={K}", [Fr(a, 3) for a in range(1, K + 1)])


if __name__ == "__main__":
    print("=" * 72)
    print("UNIFORM p-adic lower bound test (p == 3 mod 4, unreachable by 4a^2+b^2)")
    print("DISCOVERY TIER (conjecture only).")
    print("=" * 72)
    # off-line orbits with a 3-mod-4 prime in the conductor
    candidates = [(Fr(3, 5), Fr(6, 5)), (Fr(1, 5), Fr(2, 5)), (Fr(3, 7), Fr(1))]
    for (sigma, tau) in candidates:
        D, facs = offline_conductor_primes(sigma, tau)
        p3 = [p for p in facs if p % 4 == 3]
        print(f"\noff-line rho = {sigma} + {tau} i :  D = {D} = "
              f"{' * '.join(f'{p}^{e}' for p, e in sorted(facs.items()))}")
        if not p3:
            print("  (no 3-mod-4 prime in conductor — mechanism N/A, skipping)")
            continue
        p = p3[0]
        dp = facs[p]
        print(f"  target prime p = {p} (==3 mod4), v_p(D) = {dp}")
        # CRUX CHECK: every on-line value C_j(t_k) must be p-integral (v_p>=0).
        crux_ok = True
        for (name, ts) in node_families(6, 12):
            for t in ts:
                if t == 0:
                    continue
                for cj in P.C_vec(t, 6):
                    if vp_frac(cj, p) < 0:
                        crux_ok = False
                        break
        print(f"  CRUX: all on-line C_j(t_k) are {p}-integral (p-unreachable): "
              f"{crux_ok}")
        # correct bound:  v_p(q) >= B(m) := max_{j<=m} v_p(den d_j)
        print(f"  {'m':>3} | {'B=max_j vp(den d_j)':>19} | {'min vp(q_min)':>14} | "
              f"{'>= B?':>6} | {'families ok':>11}")
        print("  " + "-" * 70)
        for m in range(2, 7):
            dvec = O_orbit_direct(sigma, tau, m)
            Bm = max(vp(dj.denominator, p) for dj in dvec)   # = max_j v_p(den d_j)
            Kmax = m + 5
            min_vpq = None
            n_ok = 0
            n_tot = 0
            for (name, ts) in node_families(m, Kmax):
                if any(t == 0 for t in ts):
                    continue
                try:
                    q = qmin_index(*cleared_columns(ts, sigma, tau, m), m)
                except Exception:
                    q = None
                if q is None or q <= 0:
                    continue
                n_tot += 1
                vq = vp(q, p)
                if min_vpq is None or vq < min_vpq:
                    min_vpq = vq
                if vq >= Bm:
                    n_ok += 1
            ok = (min_vpq is not None and min_vpq >= Bm)
            print(f"  {m:>3} | {Bm:>19} | {str(min_vpq):>14} | "
                  f"{str(ok):>6} | {n_ok}/{n_tot:<9}")
    print("\nCorrect uniform bound:  |q| >= p^{B(m)},  B(m) = max_{j<=m}")
    print("v_p(den d_j).  On-line p-integrality (CRUX) makes it RIGOROUS for")
    print("every on-line node set.  If B(m) grows ~linearly in m, |q| is")
    print("exponential uniformly => OP1 proved for off-line orbits whose")
    print("conductor has a prime == 3 mod 4 (an explicit infinite family).")
