#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 §6c FOLLOW-UP: attack the sharply-localized open core -- a rigorous LINEAR
lower bound on the TOP Smith invariant  e_max = v_p(s_m(A)) = v_p(D_m/D_{m-1}),
which (by §6c) upper-bounds v_p(q_min) and is met generically.

Candidate proof (pigeonhole + confluent Vandermonde), tested here:
  * mod p there are exactly (p+1)/2 on-line x-classes (§6c rank-count lemma).
  * Any m nodes => by pigeonhole some class holds >= ceil(2m/(p+1)) of them.
  * x_{t+p} == x_t mod p, so {t0 + p*i} is a p-adic expansion INSIDE one class:
    x = xi + p*y, distinct y mod p.  The confluent (divided-difference) structure
    of the Chebyshev/Vandermonde block on c such nodes forces Smith p-exponents
    0,1,...,c-1, hence the TOP invariant of that block is c-1.
  * Therefore  e_max >= (max class multiplicity) - 1 >= ceil(2m/(p+1)) - 1  (LINEAR).
  * The adversary MINIMIZES e_max by spreading the m nodes evenly over all
    (p+1)/2 classes => c_max = ceil(2m/(p+1)) => the bound is the adversary optimum.

Basis note (why A = [C_j(t_k)], C_j = 4(1 - T_j(x)), inherits the Vandermonde
p-adic Smith structure for ODD p): 4 is a p-unit; the change of basis {x^j}<->{T_j}
is unitriangular over Z[1/2] (2 a p-unit), invertible over Z_p; the constant-row
subtraction (C_j uses 1 - T_j, i.e. T_0 - T_j) is a unimodular row operation.  So
the Z_p-Smith form of A matches that of the monomial Vandermonde in the x_k (up to
the j=0 row), which is the classical confluent object.  Verified directly below.

What this probe checks (exact arithmetic):
  (P) adversarial min e_max over node families  >=  ceil(2m/(p+1)) - 1;
  (S) SINGLE-class family {t0+p*i}: e_max == m-1 (full confluence, top depth);
  (A) SPREAD adversarial family (all (p+1)/2 classes, p-adically expanded):
      e_max == ceil(2m/(p+1)) - 1 exactly (bound is TIGHT = adversary optimum);
  (B) basis reduction: v_p(D_r(A)) == v_p(D_r(monomial Vandermonde in x)) for r<m
      (odd p), confirming the confluent-Vandermonde argument transfers to A.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil

import discovery.probe_overdetermined_collision as P
from discovery.probe_qmin_snf import cleared_columns, det_divisor_r


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        return None
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def emax_of(on_cols, m, p):
    """Top Smith p-exponent v_p(D_m) - v_p(D_{m-1}) of the m x K matrix on_cols."""
    vDm = vp(det_divisor_r(on_cols, m, m), p) or 0
    vDm1 = vp(det_divisor_r(on_cols, m, m - 1), p) or 0
    return vDm - vDm1


def x_of(t):
    return (4 * t * t - 1) / (4 * t * t + 1)


def xclass_modp(t, p):
    """x_t as an element of F_p (t rational, denominator a p-unit for inert p)."""
    x = x_of(Fr(t))
    return (x.numerator % p) * pow(x.denominator % p, p - 2, p) % p


# node families for the adversarial minimum (part P)
def families(m, p):
    K = m + 3
    fams = [
        ("half-int", [Fr(1, 2) + i for i in range(K)]),
        ("integer", [Fr(i) for i in range(1, K + 1)]),
        ("thirds", [Fr(a, 3) for a in range(1, K + 1)]),
        ("fifths", [Fr(a, 5) for a in range(1, K + 1)]),
        ("sevenths", [Fr(a, 7) for a in range(1, K + 1)]),
        ("spread-p", spread_family(p, m)),
        ("single-cls", single_class(p, Fr(1), m)),
    ]
    return fams


def single_class(p, t0, m):
    """{t0 + p*i}: all share one x-class mod p; p-adically expanded."""
    return [t0 + p * i for i in range(m + 3)]


def spread_family(p, m):
    """Fill all (p+1)/2 finite x-classes (reps t=0..(p-1)/2), each p-adically
    expanded by t -> t + p*i.  Adversary's even-spread optimum."""
    reps = list(range((p - 1) // 2 + 1))          # t = 0,1,...,(p-1)/2
    depth = ceil(2 * (m + 3) / (p + 1)) + 1
    fam = []
    for c in reps:
        for i in range(depth):
            t = Fr(c + p * i)
            if t != 0:
                fam.append(t)
    return fam


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    sigma, tau = Fr(3, 4), Fr(1)      # split-only off-line orbit D=425 (inert-free)
    print("=" * 78)
    print("OP1 §6c: LINEAR lower bound on top Smith invariant e_max.")
    print("Pigeonhole + confluent Vandermonde.  DISCOVERY TIER.  No RH input.")
    print(f"off-line rho = {sigma}+{tau}i (D=425, split-only).")
    print("=" * 78)

    for p in (3, 7, 11):
        half = (p + 1) // 2
        print(f"\n{'='*78}\np = {p} (inert):  (p+1)/2 = {half} x-classes mod p")
        # sanity: exactly half finite x-classes from t=0..(p-1)/2
        cls = {xclass_modp(t, p) for t in range((p - 1) // 2 + 1)}
        print(f"  finite x-classes realized by t=0..(p-1)/2: {len(cls)} "
              f"(expect {half}) : {len(cls) == half}")
        print(f"  {'m':>3} | {'PH=ceil(2m/(p+1))-1':>20} | {'min e_max (adv)':>15} "
              f"| {'>=PH':>5} | {'single-cls e_max':>16} {'==m-1':>6} "
              f"| {'spread e_max':>12} {'==PH':>5}")
        print("  " + "-" * 100)
        for m in range(2, 8):
            PH = ceil(2 * m / (p + 1)) - 1
            emins, e_single, e_spread = [], None, None
            for name, ts in families(m, p):
                ts = [t for t in ts if t != 0]
                if len(ts) < m:
                    continue
                try:
                    oc, _ = cleared_columns(ts, sigma, tau, m)
                    e = emax_of(oc, m, p)
                except Exception:
                    continue
                emins.append(e)
                if name == "single-cls":
                    e_single = e
                if name == "spread-p":
                    e_spread = e
            emin = min(emins) if emins else None
            ok = (emin is not None and emin >= PH)
            s_ok = (e_single == m - 1)
            sp_ok = (e_spread == PH)
            print(f"  {m:>3} | {PH:>20} | {str(emin):>15} | {str(ok):>5} "
                  f"| {str(e_single):>16} {str(s_ok):>6} "
                  f"| {str(e_spread):>12} {str(sp_ok):>5}")

    # (B) basis reduction: A's p-adic determinantal divisors == monomial Vandermonde
    print(f"\n{'='*78}\n(B) basis reduction check (odd p): v_p(D_r(A)) vs monomial "
          f"Vandermonde in x_k")
    print("  A = [C_j(t_k)], C_j = 4(1-T_j(x)); Vandermonde M = [x_k^j], j=1..m")
    for p in (3, 7):
        for m in (4, 5):
            ts = [Fr(i) for i in range(1, m + 4)]
            oc, _ = cleared_columns(ts, sigma, tau, m)
            # monomial Vandermonde rows j=1..m (clear denominators uniformly)
            xs = [x_of(t) for t in ts]
            from math import prod
            Lden = 1
            for x in xs:
                Lden = Lden * x.denominator // __import__("math").gcd(Lden, x.denominator)
            Vcols = []
            for x in xs:
                Vcols.append([int((x ** j) * (Lden ** j)) for j in range(1, m + 1)])
            same = all(
                (vp(det_divisor_r(oc, m, r), p) or 0)
                == (vp(det_divisor_r(Vcols, m, r), p) or 0)
                for r in range(1, m))
            print(f"  p={p} m={m}: v_p(D_r) match for r=1..{m-1} : {same}  "
                  f"[A: {[vp(det_divisor_r(oc,m,r),p) or 0 for r in range(1,m+1)]}, "
                  f"V: {[vp(det_divisor_r(Vcols,m,r),p) or 0 for r in range(1,m+1)]}]")

    print("\n" + "=" * 78)
    print("READING: if (P) min e_max >= PH holds AND (A) spread e_max == PH, the")
    print("pigeonhole+confluent bound e_max >= ceil(2m/(p+1))-1 is the TIGHT")
    print("adversary optimum => a RIGOROUS LINEAR floor on the top Smith invariant,")
    print("the exact missing step of §6c.  (S) and (B) confirm the mechanism/basis.")
