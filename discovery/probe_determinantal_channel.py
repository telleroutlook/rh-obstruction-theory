#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.  All objects are finite explicit rational
multisets.

OP1 REMAINING CASE: the higher-order DETERMINANTAL-INJECTION channel.

Context.  The uniform inert-prime theorem (§5) and the on-line 2-adic covector
theorem (§6b) both rest on a p-adic ESCAPE of the off-line vector
(-delta_j ~ c*j).  For ALL-SPLIT off-line orbits (e.g. rho = 3/4 + i,
D = 425 = 5^2 * 17, both 5,17 == 1 mod 4) the observed q_min = 3^5 * 7^2 * 11 is
carried by INERT primes 3,7,11 (== 3 mod 4) that are NOT in den(u_0) and have
ZERO escape (delta_j = 0).  The single (j^2)-parabola covector is VALID but
VACUOUS there.  This probe tests a genuinely different, MULTI-ROW / VANDERMONDE
determinantal mechanism.

Mechanism under test.
  On-line node t = a/b (primitive): x_t = (4t^2-1)/(4t^2+1) depends only on t^2.
  Cross-difference identity (proved by hand, sanity-checked below):
      x_k - x_l = 8 (a_k b_l - a_l b_k)(a_k b_l + a_l b_k) / (N_k N_l),
      N_k = 4 a_k^2 + b_k^2.
  For inert p == 3 mod 4:  p never divides N_k (else (2a/b)^2 == -1 mod p,
  impossible), so x_t in Z_p and the on-line x-values mod p lie in the image of
      t |-> (4t^2-1)/(4t^2+1)  on  P^1(F_p),
  which (t enters only through t^2) has size EXACTLY (p+3)/2.

  cleared_columns() scales ALL columns by one uniform denominator Lden, a p-UNIT
  for inert p (p | none of N_k, and p | den(d) is false for split-only orbits).
  Hence L_p = Z_p-span of the RATIONAL Chebyshev columns, and two on-line columns
  whose x-values agree mod p are EQUAL mod p.  Therefore
      rank(A mod p) <= #{x-values mod p} = (p+3)/2,
  and the number of Smith invariants of A divisible by p is >= m - rank(A mod p),
  giving the RIGOROUS LINEAR FLOOR
      v_p(D_m(A)) >= m - (p+3)/2.
  This is the multi-row Vandermonde argument the single covector cannot reach.

What this probe verifies (exact arithmetic):
  (V) the cross-difference identity, at sample nodes;
  (C) #{on-line x-values mod p} == (p+3)/2 for inert p;
  (R) rank(A mod p) <= (p+3)/2 over many node sets;
  (F) v_p(D_m(A)) >= m - (p+3)/2 (the theorem's floor);
  (G) the REMAINING GAP: measure v_p(D_m([A|d])) and
      v_p(q_min) = v_p(D_m(A)) - v_p(D_m([A|d])); is the DIFFERENCE still linear
      (adversarially), i.e. does the off-line column fail to fill the p-deficient
      directions?  This is exactly the open sub-problem.

q_min is taken from the TRUSTED gcd-of-minors qmin_index (probe_qmin_snf).
"""
from __future__ import annotations
from fractions import Fraction as Fr

import discovery.probe_overdetermined_collision as P
from discovery.probe_covolume_floor import O_orbit_direct
from discovery.probe_qmin_snf import (cleared_columns, qmin_index,
                                       det_divisor_r)


# ----------------------------------------------------------------------------
def vp(n, p):
    """p-adic valuation of a nonzero integer."""
    n = abs(int(n))
    if n == 0:
        return None
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def is_inert(p):
    """p == 3 mod 4 (inert in Z[i])."""
    return p % 4 == 3


def offline_conductor(sigma, tau):
    sigma, tau = Fr(sigma), Fr(tau)
    Nrho = sigma * sigma + tau * tau
    Nrm1 = (sigma - 1) * (sigma - 1) + tau * tau
    return Nrho.numerator * Nrm1.numerator


def factor(n):
    facs = {}
    d, f = int(n), 2
    while f * f <= d:
        while d % f == 0:
            facs[f] = facs.get(f, 0) + 1
            d //= f
        f += 1
    if d > 1:
        facs[d] = facs.get(d, 0) + 1
    return facs


# ----------------------------------------------------------------------------
# (V) cross-difference identity sanity check (exact)
def check_cross_identity():
    ok = True
    for (a1, b1), (a2, b2) in [((1, 2), (3, 1)), ((2, 3), (5, 4)), ((1, 5), (2, 1))]:
        t1, t2 = Fr(a1, b1), Fr(a2, b2)
        x1 = (4 * t1 * t1 - 1) / (4 * t1 * t1 + 1)
        x2 = (4 * t2 * t2 - 1) / (4 * t2 * t2 + 1)
        lhs = x1 - x2
        N1, N2 = 4 * a1 * a1 + b1 * b1, 4 * a2 * a2 + b2 * b2
        rhs = Fr(8 * (a1 * b2 - a2 * b1) * (a1 * b2 + a2 * b1), N1 * N2)
        ok = ok and (lhs == rhs)
    return ok


# (C) count of on-line x-values mod p
def xvalues_modp(p):
    """Distinct values of x = (4t^2-1)/(4t^2+1) over t in P^1(F_p).
    Returns a set; 'inf' denotes the point at infinity (4t^2+1 == 0)."""
    vals = set()
    # t in F_p
    for t in range(p):
        num = (4 * t * t - 1) % p
        den = (4 * t * t + 1) % p
        if den == 0:
            vals.add("inf")
        else:
            vals.add((num * pow(den, p - 2, p)) % p)
    # t = infinity: x -> 1 (since (4t^2-1)/(4t^2+1) -> 1)
    vals.add(1 % p)
    return vals


# (R) rank of A mod p, A = rational on-line Chebyshev columns reduced mod p
def rank_modp(rational_cols, m, p):
    """rational_cols: list of columns, each a list of m Fractions (p-integral).
    Reduce mod p and return the F_p-rank."""
    M = []
    for i in range(m):
        row = []
        for col in rational_cols:
            fr = col[i]
            den = fr.denominator % p
            assert den != 0, "denominator divisible by p — p not inert here"
            row.append((fr.numerator % p) * pow(den, p - 2, p) % p)
        M.append(row)
    # Gaussian elimination over F_p
    rank = 0
    ncols = len(rational_cols)
    r = 0
    for c in range(ncols):
        piv = None
        for rr in range(r, m):
            if M[rr][c] % p != 0:
                piv = rr
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for rr in range(m):
            if rr != r and M[rr][c] % p != 0:
                f = M[rr][c]
                M[rr] = [(M[rr][j] - f * M[r][j]) % p for j in range(ncols)]
        r += 1
        rank += 1
        if r == m:
            break
    return rank


def node_families(m, Kmax):
    for K in range(m + 1, Kmax + 1):
        yield (f"half-int K={K}", [Fr(1, 2) + Fr(i) for i in range(K)])
        yield (f"integer  K={K}", [Fr(i) for i in range(1, K + 1)])
        yield (f"thirds   K={K}", [Fr(a, 3) for a in range(1, K + 1)])
        yield (f"small-fr K={K}", [Fr(1, 2)] + [Fr(1, d) for d in range(2, K + 1)])


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 78)
    print("OP1 determinantal-injection channel — inert-prime Vandermonde floor.")
    print("DISCOVERY TIER (conjecture only).  No RH input.")
    print("=" * 78)

    print(f"\n(V) cross-difference identity x_k-x_l = "
          f"8(a_kb_l-a_lb_k)(a_kb_l+a_lb_k)/(N_kN_l):  {check_cross_identity()}")

    # split-only / mixed off-line orbits carrying inert primes with zero escape
    orbits = [(Fr(3, 4), Fr(1)), (Fr(2, 3), Fr(1)), (Fr(1), Fr(1, 5))]
    for (sigma, tau) in orbits:
        D = offline_conductor(sigma, tau)
        facs = factor(D)
        inert = sorted(p for p in facs if is_inert(p))
        print(f"\n{'='*78}\noff-line rho = {sigma} + {tau} i :  D = {D} = "
              f"{' * '.join(f'{p}^{e}' for p, e in sorted(facs.items()))}")
        print(f"  inert primes (==3 mod4) in D: {inert or '(none in D)'}")

        # inert primes we track = those in D plus small inert primes that may be
        # injected purely determinantally (3,7,11) even when absent from D
        track = sorted(set(inert) | {3, 7, 11})
        for p in track:
            xv = xvalues_modp(p)
            cnt = len(xv)
            expect = (p + 3) // 2
            in_D = "in D" if p in facs else "NOT in D (pure determinantal)"
            print(f"\n  --- p = {p} (inert), {in_D};  #x-values mod p = {cnt} "
                  f"(expect (p+3)/2 = {expect}) : {cnt == expect} ---")
            print(f"    {'m':>3} | {'rk(A%p)':>7} {'<=(p+3)/2':>9} | "
                  f"{'vp(D_mA)':>8} {'>=m-flr':>7} | {'e_max':>5} {'vq<=em':>6} | "
                  f"{'vp(qmin)':>8} | {'min vq adv':>10} {'min em adv':>10}")
            print("    " + "-" * 92)
            for m in range(2, 9):
                floor = max(0, m - expect)
                Kmax = m + 3
                # a reference family (integer nodes) for the per-m detail
                ts_ref = [Fr(i) for i in range(1, m + 4)]
                rat_cols = [P.C_vec(t, m) for t in ts_ref]
                rk = rank_modp(rat_cols, m, p)
                on_cols, voff = cleared_columns(ts_ref, sigma, tau, m)
                vDA = vp(det_divisor_r(on_cols, m, m), p) or 0
                vDm1 = vp(det_divisor_r(on_cols, m, m - 1), p) or 0
                emax = vDA - vDm1  # top Smith p-exponent v_p(s_m) = v_p(D_m/D_{m-1})
                qmin = qmin_index(on_cols, voff, m)
                vq = (vp(qmin, p) or 0) if qmin else None
                # adversarial min v_p(q_min) and min e_max over node families
                adv, adv_em = None, None
                for (_, ts) in node_families(m, Kmax):
                    if any(t == 0 for t in ts):
                        continue
                    try:
                        oc, vo = cleared_columns(ts, sigma, tau, m)
                        q = qmin_index(oc, vo, m)
                        em = ((vp(det_divisor_r(oc, m, m), p) or 0)
                              - (vp(det_divisor_r(oc, m, m - 1), p) or 0))
                    except Exception:
                        q, em = None, None
                    if q:
                        v = vp(q, p) or 0
                        adv = v if adv is None else min(adv, v)
                        adv_em = em if adv_em is None else min(adv_em, em)
                le = "n/a" if vq is None else str(vq <= emax)
                print(f"    {m:>3} | {rk:>7} {str(rk <= expect):>9} | "
                      f"{vDA:>8} {str(vDA >= floor):>7} | {emax:>5} {le:>6} | "
                      f"{str(vq):>8} | {str(adv):>10} {str(adv_em):>10}")

    print("\n" + "=" * 78)
    print("READING:")
    print(" (C) #x-values mod p == (p+3)/2  => the on-line geometry occupies only")
    print("     (p+3)/2 residue classes for every inert p (RIGOROUS count).")
    print(" (R,F) rank(A%p) <= (p+3)/2 and v_p(D_mA) >= m-(p+3)/2 confirm the")
    print("     RIGOROUS linear Vandermonde floor on the NUMERATOR.")
    print(" (G) OPEN: if min v_p(q_min) (adversarial) also grows ~ m-(p+3)/2, the")
    print("     off-line column does NOT fill the p-deficient directions and the")
    print("     determinantal channel gives a UNIFORM linear floor => OP1 closed")
    print("     for split-only orbits.  If it stays bounded, the gap survives.")
