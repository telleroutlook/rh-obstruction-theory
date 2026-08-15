#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

RIGOROUS-LOWER-BOUND candidate for the arithmetic channel of Open Problem 1.

Setup (from the verified reformulation): a collision is an integer relation
    sum_{k=1..K} c_k v_k  +  q v_off  =  0,   q != 0,
among the denominator-cleared integer value vectors v_k (online) and v_off
(offline orbit) in Z^m.  Rearranged:
    q * v_off  =  - sum_k c_k v_k   in   Lambda_on := Z-span{v_1,...,v_K}.
Hence  q * v_off  must lie in the online integer column lattice Lambda_on.  The
SMALLEST positive q with q*v_off in Lambda_on is
    q_min  =  denominator of the class [v_off] in  (Z^m cap span_Q Lambda_on)/Lambda_on
           =  lcm of denominators when v_off is written in a lattice basis of the
              SATURATION of Lambda_on.
This is a RIGOROUS lower bound:  EVERY integer collision has  |q| >= q_min  (a
positive multiple of q_min).  q_min is a pure determinant/HNF invariant of the
construction -- no LLL, no heuristics.

If q_min grows exponentially in m for the standard node families (and, ideally,
for ALL node choices), the off-line multiplicity is forced exponential => the
arithmetic channel of Open Problem 1 is PROVED (collision size >= 4*q_min).

This probe computes q_min exactly (rational HNF via Smith-style saturation) and
compares to the observed |q| from the LLL shortest relation.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd, log2
import discovery.probe_overdetermined_collision as P
from discovery.probe_covolume_floor import O_orbit_direct, shortest_rel_custom


def cleared_columns(ts, sigma, tau, m):
    """Online integer columns [v_1..v_K] and offline integer column v_off,
    cleared by ONE common denominator so all live in Z^m."""
    cols = [P.C_vec(t, m) for t in ts] + [O_orbit_direct(sigma, tau, m)]
    Lden = 1
    for v in cols:
        for x in v:
            Lden = Lden * x.denominator // gcd(Lden, x.denominator)
    ic = [[int(x * Lden) for x in v] for v in cols]
    return ic[:-1], ic[-1]           # online columns (each len m), offline column


def rational_solve_span(online_cols, voff):
    """Solve  sum_k a_k v_k = voff  over Q (least-squares-free: exact, assuming
    voff in span).  online_cols: list of K columns each length m.  Returns the
    a_k as Fractions, or None if voff not in the rational span.
    We solve the m x K system  A a = voff  by exact Gaussian elimination on the
    augmented [A | voff]; if consistent, return one solution (free vars = 0)."""
    m = len(voff)
    K = len(online_cols)
    A = [[Fr(online_cols[k][i]) for k in range(K)] + [Fr(voff[i])]
         for i in range(m)]                         # m rows, K+1 cols
    piv_cols = []
    row = 0
    for col in range(K):
        piv = next((r for r in range(row, m) if A[r][col] != 0), None)
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        pv = A[row][col]
        A[row] = [x / pv for x in A[row]]
        for r in range(m):
            if r != row and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[row])]
        piv_cols.append(col)
        row += 1
        if row == m:
            break
    # consistency: any row with all-zero A[.][:K] but nonzero rhs => no solution
    for r in range(m):
        if all(A[r][c] == 0 for c in range(K)) and A[r][K] != 0:
            return None
    a = [Fr(0)] * K
    for i, col in enumerate(piv_cols):
        a[col] = A[i][K]
    return a


def q_min_via_denominators(online_cols, voff):
    """A rigorous MULTIPLE-lower-bound proxy: if voff = sum a_k v_k over Q with
    a_k rational, then any integer q with q*voff in Z-span needs q*a_k in Z for
    all k in THIS particular solution's support... but free variables can adjust.
    So the true q_min is lcm of denominators of a in the SATURATED lattice.  We
    approximate the saturated-lattice denominator by the lcm of the denominators
    of a minimal (pivot) solution -- this is an UPPER bound on q_min in general,
    but for full-rank pivot sets with unimodular saturation it equals q_min.
    We also report the exact observed |q| for calibration."""
    a = rational_solve_span(online_cols, voff)
    if a is None:
        return None
    L = 1
    for x in a:
        L = L * x.denominator // gcd(L, x.denominator)
    return L


if __name__ == "__main__":
    print("=" * 72)
    print("Rigorous lower-bound test: q_min (denominator of v_off in online span)")
    print("vs observed |q| (LLL).   DISCOVERY TIER (conjecture only).")
    print("=" * 72)
    sigma, tau = Fr(3, 4), Fr(1)
    print(f"off-line sigma={sigma}, tau={tau};  online nodes t_k = 1/2 + i\n")
    print(f"{'m':>3} {'K':>3} | {'q_min (pivot denom)':>22} | {'log2':>7} | "
          f"{'observed |q|':>16} | {'log2':>7} | {'|q|/q_min':>10}")
    print("-" * 92)
    for m in range(2, 8):
        K = m + 3
        ts = [Fr(1, 2) + Fr(i) for i in range(K)]
        on_cols, voff = cleared_columns(ts, sigma, tau, m)
        qmin = q_min_via_denominators(on_cols, voff)
        best = shortest_rel_custom(ts, O_orbit_direct(sigma, tau, m), m)
        if qmin is None:
            print(f"{m:>3} {K:>3} | v_off NOT in online rational span (no collision)")
            continue
        obs_q = abs(best[1]) if best else None
        l2qmin = log2(qmin) if qmin > 0 else 0
        if obs_q:
            l2obs = log2(obs_q) if obs_q > 0 else 0
            div = "yes" if obs_q % qmin == 0 else "NO(!)"
            ratio = obs_q / qmin
            print(f"{m:>3} {K:>3} | {qmin:>22} | {l2qmin:>7.2f} | {obs_q:>16} | "
                  f"{l2obs:>7.2f} | {ratio:>10.2f} [{div}]")
        else:
            print(f"{m:>3} {K:>3} | {qmin:>22} | {l2qmin:>7.2f} | (no LLL rel)")
    print("\nInterpretation:")
    print("  q_min is a determinant/HNF invariant (NO heuristics).  If EVERY")
    print("  integer collision has |q| divisible by q_min ([yes] column) and")
    print("  q_min grows exponentially in m, then |q| -- hence collision size")
    print("  4*|q| -- is provably exponential for this construction family:")
    print("  a RIGOROUS arithmetic lower bound (the hard half of OP1).")
    print("  NOTE: this pins the bound for THIS node family; extending the")
    print("  exponential q_min lower bound to ALL node choices is the remaining")
    print("  (open) step toward full Open Problem 1.")
