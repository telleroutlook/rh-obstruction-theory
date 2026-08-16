#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

RESULTANT ANATOMY of q_min (the sole surviving §6y target).  §6z-agg recast the barrier as
    q_min = lcm_k den(c_k),   c = A^{-1} d,   A = 4(J - M),  M_{jk} = T_j(x_k) = Re[w_k^j],
i.e. c is the quadrature that reproduces the OFF-LINE moments Re[w_a^j] (|w_a|!=1) using ON-LINE
unit-circle nodes w_k (|w_k|=1, x_k = Re[w_k] = (4t_k^2-1)/(4t_k^2+1)).  A Vandermonde/Prony solve
=> the denominators of c_k are governed by an explicit RESULTANT/DISCRIMINANT:
    * GEOMETRIC source: node-difference product  DISC = prod_{k<l}(x_k - x_l),
      with x_k - x_l = 8(t_k^2 - t_l^2)/[(4t_k^2+1)(4t_l^2+1)]  (numerator carries prod(t_k^2 - t_l^2));
    * RAMIFIED source: off-line atom norms |rho|^2 = sigma^2 + tau^2 and (1-sigma)^2 + tau^2
      (for sigma=3/4,tau=1: 25/16 and 17/16 -> odd parts 5^2 and 17 -> D = 425 EXACTLY).

GOAL (bridge to a THEOREM): confirm the EXACT identity  odd-part(q_min) == odd-part of an explicit
resultant built from DISC and the off-line norms — NOT a per-prime coincidence but a single algebraic
object.  If odd-part(q_min) divides (or equals up to bounded off-line-power) the numerator content of
DISC^{-1} cleared times the off-line-norm product, then q_min is a genuine resultant and its growth is
forced by the Vandermonde numerator the adversary cannot fully cancel — the lower-bound vehicle.

We print, for small m and several node sets, the prime-by-prime table:
    v_p(q_min)  vs  v_p(num DISC)  v_p(den DISC)  v_p(offline-norm-num)
and the exact quotient q_min / (candidate resultant) to expose the law.  Exact rational arithmetic
(L9).  Bounded (evidence, not proof).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd, lcm
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_overdetermined_collision as P
from discovery.probe_covolume_floor import O_orbit_direct

SIG, TAU = Fr(3, 4), Fr(1)   # D=425 = 5^2 * 17


def solve_c(ts, m):
    """c = A^{-1} d exactly; returns list of Fraction, or None if singular/no collision."""
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    Mrows = [[Fr(oc[j][i]) for j in range(m)] + [Fr(vo[i])] for i in range(m)]
    for i in range(m):
        piv = next((r for r in range(i, m) if Mrows[r][i] != 0), None)
        if piv is None:
            return None
        Mrows[i], Mrows[piv] = Mrows[piv], Mrows[i]
        inv = Mrows[i][i]
        Mrows[i] = [v / inv for v in Mrows[i]]
        for r in range(m):
            if r != i and Mrows[r][i] != 0:
                f = Mrows[r][i]
                Mrows[r] = [Mrows[r][cc] - f * Mrows[i][cc] for cc in range(m + 1)]
    return [Mrows[i][m] for i in range(m)]


def qmin_lcm(c):
    L = 1
    for v in c:
        L = lcm(L, v.denominator)
    return L


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


def disc(ts):
    """prod_{k<l} (x_k - x_l) as a Fraction."""
    xs = [x_of(t) for t in ts]
    D = Fr(1)
    for k in range(len(xs)):
        for l in range(k + 1, len(xs)):
            D *= (xs[k] - xs[l])
    return D


def offline_norm_num():
    """odd part of numerators of |rho|^2 over the atom set {sigma, 1-sigma} x {tau}."""
    vals = []
    for s in (SIG, 1 - SIG):
        n = (s * s + TAU * TAU)  # |rho|^2
        vals.append(n.numerator)
    return vals


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        return 0
    e = 0
    while n % p == 0:
        n //= p; e += 1
    return e


def odd_part(n):
    n = abs(int(n))
    while n % 2 == 0 and n > 0:
        n //= 2
    return n


def odd_primes(n):
    n = odd_part(n)
    ps, d = set(), 3
    while d * d <= n:
        while n % d == 0:
            ps.add(d); n //= d
        d += 2
    if n > 1:
        ps.add(n)
    return sorted(ps)


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("RESULTANT ANATOMY of q_min (D=425).  odd-part(q_min) vs DISC=prod(x_k-x_l) & offline norms.", flush=True)
    print(f"offline |rho|^2 numerators (odd parts): {[odd_part(v) for v in offline_norm_num()]}  (expect 25,17)", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(271828)
    for m in (3, 4, 5):
        print(f"\n===== m = {m} =====", flush=True)
        node_sets = []
        # a few random node sets + one clustered
        for _ in range(4):
            node_sets.append(rng.sample(range(1, 40), m))
        node_sets.append([2, 7, 12, 17, 22][:m])   # arithmetic-progression-ish (spread)
        for ts in node_sets:
            c = solve_c(ts, m)
            if c is None:
                continue
            q = qmin_lcm(c)
            # cross-check vs qmin_fast
            oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
            qf = qmin_fast(oc, vo) or 0
            D = disc(ts)
            numD, denD = D.numerator, D.denominator
            ok = "OK" if q == qf else f"MISMATCH(qf={qf})"
            print(f"\n ts={ts}  q_min={q}  [{ok}]", flush=True)
            print(f"   odd(q_min)={odd_part(q)}   num(DISC) odd-primes={odd_primes(numD)}   "
                  f"den(DISC) odd-primes={odd_primes(denD)}", flush=True)
            # prime table over union of relevant odd primes
            ps = sorted(set(odd_primes(q)) | {5, 17} | set(odd_primes(numD)) | set(odd_primes(denD)))
            hdr = f"   {'p':>5} | {'vp(qmin)':>8} {'vp(numD)':>8} {'vp(denD)':>8}"
            print(hdr, flush=True)
            for p in ps:
                print(f"   {p:>5} | {vp(q,p):>8} {vp(numD,p):>8} {vp(denD,p):>8}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if v_p(q_min) tracks a fixed function of v_p(numD)/v_p(denD) plus the fixed", flush=True)
    print("off-line primes {5,17} across ALL node sets, q_min is an explicit resultant/discriminant —", flush=True)
    print("the bridge from 'aggregate resists draining (empirical)' to a rigorous growth lower bound.", flush=True)
    print("If the relation is erratic, the resultant identity is more subtle (Sherman-Morrison term).", flush=True)
    print("Exact arithmetic; bounded; evidence not proof. RH stays [OUT].", flush=True)
