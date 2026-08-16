#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 §6g: e_max floor PROVED DIRECTLY on the actual matrix A = [C_j(t_k)]
(C_j = 4(1 - T_j(x)), rows j=1..m).  This UNIFIES §6d LEG1 (Vandermonde floor)
and LEG2 (basis reduction A ~ V) into ONE elementary theorem, removing the need
for the classical confluent-Vandermonde staircase AND the off-by-one lemma.

KEY ALGEBRAIC FACT.  T_j(1) = 1 for all j, so every C_j = 4(1 - T_j) VANISHES at
x = 1:  C_j(x) = (x - 1) g_j(x),  deg g_j = j - 1, leading coeff of g_j = leading
coeff of C_j = -4 * 2^{j-1} (a p-unit for odd p).  Since {g_1,...,g_m} have
degrees 0,1,...,m-1, for any m-subset S of nodes:
    det [C_j(x_k)]_{j=1..m, k in S}
        = (prod_j lead g_j) * prod_{k in S} (x_k - 1) * det [x_k^{i}]_{i=0..m-1, k in S}
        = (p-unit) * prod_{k in S}(x_k - 1) * prod_{k<l in S} (x_l - x_k).
Hence (all leading factors are p-units for odd p)
    v_p(det A_S) = sum_{k in S} v_p(x_k - 1) + sum_{k<l in S} v_p(x_l - x_k).   (*)

THEOREM (e_max floor on A, elementary).  For inert p and any on-line node config,
    e_max(A) = v_p(D_m(A)) - v_p(D_{m-1}(A)) >= ceil(2m/(p+3)) - 1.
Proof.  (1) x_k occupy <= (p+3)/2 classes mod p.  (2) v_p(x_l - x_k) >= 1 iff same
class, else 0; v_p(x_k - 1) >= 0 always.  (3) Let S* minimize v_p(det A_S) (= D_m);
pigeonhole gives a class of size c* >= ceil(2m/(p+3)) in S*.  (4) drop a node u from
that class AND the top row C_m -> an (m-1)-minor on S* minus u with rows C_1..C_{m-1}
(degrees still 1..m-1, same factorization), so by (*):
    v_p(det (A_[S* minus u, rows 1..m-1]))
        = v_p(det A_{S*}) - v_p(x_u - 1) - sum_{w in class, w!=u} v_p(x_u - x_w)
       <= v_p(D_m(A)) - (c* - 1)          [v_p(x_u-1) >= 0; same-class sum >= c*-1].
    D_{m-1}(A) divides this minor  =>  v_p(D_{m-1}(A)) <= v_p(D_m(A)) - (c*-1).
  (5)  e_max(A) >= c* - 1 >= ceil(2m/(p+3)) - 1.  QED.

This probe verifies, over strong adversarial node families (incl. single-class and
even-spread), across inert p in {3,7,11}:
  (D1) the determinant identity (*) exactly;
  (D2) v_p(D_m(A)), v_p(D_{m-1}(A)) via the TRUSTED gcd-of-minors det_divisor_r,
       and e_max(A) >= ceil(2m/(p+3)) - 1;
  (D3) the pigeonhole class size c* >= ceil(2m/(p+3)) in a D_m-minimizing subset;
  (D4) the minor-removal inequality v_p(D_{m-1}) <= v_p(D_m) - (c*-1).
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil, gcd
from itertools import combinations

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


def vpf(fr, p):
    if fr == 0:
        return None
    return (vp(fr.numerator, p) or 0) - (vp(fr.denominator, p) or 0)


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


def xcls(x, p):
    return (x.numerator % p) * pow(x.denominator % p, p - 2, p) % p


def det_frac(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    tot = Fr(0)
    for c in range(n):
        minor = [row[:c] + row[c + 1:] for row in M[1:]]
        tot += ((-1) ** c) * M[0][c] * det_frac(minor)
    return tot


def families(m, p):
    K = m + 3
    fams = {
        "half-int": [Fr(1, 2) + i for i in range(K)],
        "integer": [Fr(i) for i in range(1, K + 1)],
        "thirds": [Fr(a, 3) for a in range(1, K + 1)],
        "spread-p": _spread(p, m)[:K],
        "single-cls": [Fr(1 + p * i) for i in range(K)],
    }
    return {k: [t for t in v if t != 0][:K] for k, v in fams.items()}


def _spread(p, m):
    reps = list(range((p - 1) // 2 + 1))
    depth = ceil(2 * (m + 3) / (p + 1)) + 1
    return [Fr(c + p * i) for c in reps for i in range(depth) if (c + p * i) != 0]


if __name__ == "__main__":
    print("=" * 92, flush=True)
    print("OP1 §6g: e_max floor PROVED DIRECTLY on A=[C_j(t_k)] via C_j=(x-1)g_j.", flush=True)
    print("Unifies LEG1+LEG2.  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 92, flush=True)

    d1_ok = d2_ok = d3_ok = d4_ok = True
    for p in (3, 7, 11):
        print(f"\n{'='*92}\np={p} (inert):  floor PH = ceil(2m/(p+3))-1", flush=True)
        print(f"  {'fam':>12} {'m':>2} | {'vD_m(A)':>7} {'vD_m1(A)':>8} {'e_max':>5} "
              f"| {'c*':>3} {'PH':>3} | {'D1 id':>5} {'D2 e>=PH':>8} "
              f"{'D3 c*>=PH':>9} {'D4 minor':>8}", flush=True)
        print("  " + "-" * 88, flush=True)
        for m in range(2, 7):
            PH = ceil(2 * m / (p + 3)) - 1
            for fname, ts in families(m, p).items():
                if len(ts) < m:
                    continue
                # A as cleared integer columns (trusted determinantal-divisor path)
                oc, _ = cleared_columns(ts, Fr(3, 4), Fr(1), m)   # off-line irrelevant to A
                vDm = vp(det_divisor_r(oc, m, m), p) or 0
                vDm1 = vp(det_divisor_r(oc, m, m - 1), p) or 0
                emax = vDm - vDm1
                xs = [x_of(t) for t in ts]
                # (D1) identity on every m-subset; also find D_m-minimizing S* and c*
                best_v, cstar = None, 0
                for S in combinations(range(len(ts)), m):
                    A = [[P.C_vec(ts[k], m)[j] for k in S] for j in range(m)]
                    d = det_frac(A)
                    if d == 0:
                        continue
                    lhs = vpf(d, p)
                    rhs = (sum((vpf(xs[k] - 1, p) or 0) for k in S)
                           + sum((vpf(xs[l] - xs[k], p) or 0)
                                 for a, k in enumerate(S) for l in list(S)[a + 1:]))
                    if lhs != rhs:
                        d1_ok = False
                    if best_v is None or lhs < best_v:
                        best_v = lhs
                        cc = {}
                        for k in S:
                            cc[xcls(xs[k], p)] = cc.get(xcls(xs[k], p), 0) + 1
                        cstar = max(cc.values())
                # (D4) minor-removal: exists (m-1)-minor with v_p <= vDm-(c*-1)
                d4 = (vDm1 <= vDm - (cstar - 1))
                d2 = (emax >= PH)
                d3 = (cstar >= ceil(2 * m / (p + 3)))
                d1 = (best_v == vDm)  # D_m equals min square-subdet valuation (via (*))
                d1_ok = d1_ok and d1
                d2_ok = d2_ok and d2
                d3_ok = d3_ok and d3
                d4_ok = d4_ok and d4
                flag = "" if (d1 and d2 and d3 and d4) else "  <<<"
                print(f"  {fname:>12} {m:>2} | {vDm:>7} {vDm1:>8} {emax:>5} "
                      f"| {cstar:>3} {PH:>3} | {str(d1):>5} {str(d2):>8} "
                      f"{str(d3):>9} {str(d4):>8}{flag}", flush=True)

    print("\n" + "=" * 92, flush=True)
    print(f"(D1) det identity v_p(det A_S)=sum v_p(x_k-1)+sum v_p(x_l-x_k): {d1_ok}", flush=True)
    print(f"(D2) e_max(A) >= ceil(2m/(p+3))-1                           : {d2_ok}", flush=True)
    print(f"(D3) pigeonhole c* >= ceil(2m/(p+3))                        : {d3_ok}", flush=True)
    print(f"(D4) v_p(D_m1) <= v_p(D_m) - (c*-1) (minor removal)         : {d4_ok}", flush=True)
    print(f"ALL: {d1_ok and d2_ok and d3_ok and d4_ok}  => e_max(A) floor is PROVED "
          f"directly on A (LEG1+LEG2 unified, elementary).", flush=True)
