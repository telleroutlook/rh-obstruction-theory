#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

CORRECTED rigorous lower bound for the arithmetic channel of Open Problem 1.

A collision is an integer relation  sum_k c_k v_k + q v_off = 0 (q != 0), so
    q * v_off  in  L := Z-span{v_1,...,v_K}   (online integer columns in Z^m).
The smallest positive such q is the order of [v_off] in L'/L where
L' := L + Z*v_off, i.e. the finite index
    q_min = [L' : L] = covol(L) / covol(L') = D_r(A) / D_r([A | v_off]),
where r = rank(A), A = m x K online column matrix, and D_r(X) = gcd of all
r x r minors of X (the r-th determinantal divisor = product of SNF invariants =
covolume of the column lattice).  This is EXACT and RIGOROUS: every integer
collision has q_min | q, hence |q| >= q_min and atom-count >= 4*q_min.

We compute D_r by gcd of r x r minors (r = m here, since the m x K online matrix
has full row rank m for K > m generic nodes) and check q_min | observed |q|.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
from math import gcd, log2
from sympy import Matrix
import discovery.probe_overdetermined_collision as P
from discovery.probe_covolume_floor import (O_orbit_direct, shortest_rel_custom,
                                            bareiss_det)


def cleared_columns(ts, sigma, tau, m):
    cols = [P.C_vec(t, m) for t in ts] + [O_orbit_direct(sigma, tau, m)]
    Lden = 1
    for v in cols:
        for x in v:
            Lden = Lden * x.denominator // gcd(Lden, x.denominator)
    ic = [[int(x * Lden) for x in v] for v in cols]
    return ic[:-1], ic[-1]


def matrix_rank_int(cols, m):
    """rank of the m x len(cols) integer matrix with given columns."""
    return Matrix(m, len(cols), lambda i, j: cols[j][i]).rank()


def det_divisor_r(cols, m, r):
    """D_r = gcd of all r x r minors of the m x len(cols) matrix (columns=cols).
    Minors: choose r of the m rows and r of the columns."""
    K = len(cols)
    g = 0
    for rows in combinations(range(m), r):
        for ccols in combinations(range(K), r):
            sub = [[cols[c][ri] for c in ccols] for ri in rows]
            g = gcd(g, abs(bareiss_det(sub)))
            if g == 1:
                return 1
    return g


def qmin_index(online_cols, voff, m):
    """q_min = D_r(online) / D_r([online | voff]),  r = rank(online).
    None if voff not in the rational span of the online columns."""
    r = matrix_rank_int(online_cols, m)
    aug = online_cols + [voff]
    if matrix_rank_int(aug, m) != r:
        return None                          # voff independent => no collision
    D_on = det_divisor_r(online_cols, m, r)
    D_aug = det_divisor_r(aug, m, r)
    assert D_on % D_aug == 0, f"D_aug {D_aug} must divide D_on {D_on}"
    return D_on // D_aug


if __name__ == "__main__":
    print("=" * 72)
    print("q_min = D_r(A)/D_r([A|v_off])  — rigorous lower bound |q| >= q_min.")
    print("DISCOVERY TIER (conjecture only).")
    print("=" * 72)
    for (sigma, tau) in [(Fr(3, 4), Fr(1)), (Fr(5, 6), Fr(1, 2)), (Fr(3, 4), Fr(3))]:
        print(f"\noff-line sigma={sigma}, tau={tau};  online nodes t_k = 1/2 + i")
        print(f"{'m':>3} {'K':>3} | {'q_min (det-divisor)':>24} | {'log2':>7} | "
              f"{'observed |q|':>18} | {'q_min | |q| ?':>13}")
        print("-" * 88)
        prev = None
        for m in range(2, 7):
            K = m + 3
            ts = [Fr(1, 2) + Fr(i) for i in range(K)]
            on_cols, voff = cleared_columns(ts, sigma, tau, m)
            qmin = qmin_index(on_cols, voff, m)
            best = shortest_rel_custom(ts, O_orbit_direct(sigma, tau, m), m)
            obs_q = abs(best[1]) if best else None
            if qmin is None:
                print(f"{m:>3} {K:>3} | v_off NOT in span (no collision)")
                continue
            l2 = log2(qmin) if qmin > 0 else 0
            dl = f"{l2 - prev:+.2f}" if prev is not None else "  -  "
            prev = l2
            divides = (obs_q is not None and qmin > 0 and obs_q % qmin == 0)
            print(f"{m:>3} {K:>3} | {qmin:>24} | {l2:>7.2f} | {str(obs_q):>18} | "
                  f"{str(divides):>13}  dlog2={dl}")
    print("\nIf q_min | |q| holds AND log2 q_min grows ~linearly in m (dlog2")
    print("bounded below by a positive constant), then |q| is provably")
    print("exponential for this node family: a RIGOROUS arithmetic lower bound.")
    print("Extending exponential q_min to ALL node sets => full Open Problem 1.")
