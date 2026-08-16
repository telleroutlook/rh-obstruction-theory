#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

SMITH-INVARIANT ANATOMY of q_min (§6ai) — the §6ah-reframed nucleus made structural.

q_min = order of [d] in the finite group  Z^m / A Z^m  ≅  ⊕_i Z/s_i  (s_i = Smith invariants of the
integer matrix A, s_1 | s_2 | ... | s_m).  Writing A = U·diag(s)·V (U,V unimodular over Z), the class
[d] maps to c = U^{-1} d (mod s), and
    q_min = lcm_i ( s_i / gcd(s_i, c_i) ).                                (ORDER)
So q_min is carried by the invariants s_i on which d is NOT aligned (gcd(s_i,c_i) small).  §6ah showed
log|det A| = sum_i log s_i ~ O(m^2) but log q_min ~ O(m): the adversary aligns d to KILL the bulk of the
s_i and q_min survives only on a thin O(m) residue.  This probe EXPOSES that residue:
  * compute s_i and c_i exactly (self-contained integer SNF with the U^{-1} transform), verify
    lcm_i(s_i/gcd(s_i,c_i)) == qmin_fast (independent);
  * report, per m and per adversary (aggregate-min vs generic), the per-invariant contribution
    o_i := s_i/gcd(s_i,c_i), how MANY invariants contribute (o_i>1), and where the surviving mass sits
    (top invariants? a fixed tail?).
If the survivors are a BOUNDED number of TOP invariants each of size ~exp(O(m)) (log s_i linear in i),
the floor localizes to "d cannot align with the top-O(1) invariants" — a concrete, provable-looking
target.  If the O(m) mass is spread over O(m) invariants each contributing O(1), that is a different
(diffuse) mechanism.  Either way it PINS the structure §6ah reframed.  Exact (L9). Bounded. RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import log2, gcd
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.qmin_snf_fast import qmin_fast

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17


def snf_with_U(Ain):
    """Integer Smith Normal Form via pivot-MINIMIZATION (guaranteed termination).  Returns (s_list,
    Uinv) with s_i the invariant factors and Uinv the ROW transform: applying the same row ops to A
    and to d gives S and c=Uinv@d, so the class [d] in Z^m/AZ^m ~ +Z/s_i has coords c_i mod s_i."""
    A = [row[:] for row in Ain]
    n = len(A)
    ncol = len(A[0])
    U = [[1 if i == j else 0 for j in range(n)] for i in range(n)]   # row-op accumulator

    def swap_rows(i, j):
        A[i], A[j] = A[j], A[i]; U[i], U[j] = U[j], U[i]

    def addrow(i, j, f):            # row_i += f*row_j
        for k in range(ncol):
            A[i][k] += f * A[j][k]
        for k in range(n):
            U[i][k] += f * U[j][k]

    def swap_cols(i, j):
        for r in range(n):
            A[r][i], A[r][j] = A[r][j], A[r][i]

    def addcol(i, j, f):            # col_i += f*col_j  (V side; does not touch U)
        for r in range(n):
            A[r][i] += f * A[r][j]

    t = 0
    while t < n and t < ncol:
        # bring the smallest nonzero |entry| in submatrix [t:,t:] to (t,t)
        while True:
            piv = None
            for i in range(t, n):
                for j in range(t, ncol):
                    if A[i][j] != 0 and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])):
                        piv = (i, j)
            if piv is None:
                break                       # submatrix all zero -> done
            pi, pj = piv
            if pi != t:
                swap_rows(t, pi)
            if pj != t:
                swap_cols(t, pj)
            # reduce column t and row t modulo the pivot
            reduced = False
            for i in range(t + 1, n):
                if A[i][t] != 0:
                    addrow(i, t, -(A[i][t] // A[t][t]))
                    reduced = True
            for j in range(t + 1, ncol):
                if A[t][j] != 0:
                    addcol(j, t, -(A[t][j] // A[t][t]))
                    reduced = True
            # if a remainder remains anywhere in row/col t, loop picks a smaller pivot next round;
            # if the pivot doesn't divide some off-diagonal submatrix entry, fold it into the row
            if not reduced:
                bad = None
                for i in range(t + 1, n):
                    for j in range(t + 1, ncol):
                        if A[i][j] % A[t][t] != 0:
                            bad = (i, j); break
                    if bad:
                        break
                if bad is None:
                    break                   # (t,t) divides all; column/row cleared
                addrow(t, bad[0], 1)        # bring a non-divisible entry into row t, shrink pivot next
        t += 1
    s = [abs(A[i][i]) for i in range(min(n, ncol))]
    changed = True
    while changed:                          # enforce s_1 | s_2 | ...
        changed = False
        for i in range(len(s) - 1):
            if s[i] and s[i + 1] and s[i + 1] % s[i] != 0:
                g = gcd(s[i], s[i + 1])
                s[i], s[i + 1] = g, s[i] * s[i + 1] // g
                changed = True
    return s, U


def analyze(oc, vo, m):
    """Return (qmin_via_order, qmin_fast, s_list, o_list) where o_i = s_i/gcd(s_i, c_i), c=U^{-1} d."""
    A = [[oc[j][i] for j in range(m)] for i in range(m)]   # rows
    s, U = snf_with_U(A)
    c = [sum(U[i][k] * vo[k] for k in range(m)) for i in range(m)]   # c = U^{-1} d
    o = []
    q = 1
    for i in range(m):
        si = s[i] if i < len(s) else 1
        if si == 0:
            continue
        oi = si // gcd(si, c[i] % si if si else 0) if si else 1
        o.append(oi)
        q = q * oi // gcd(q, oi)     # lcm
    return q, qmin_fast(oc, vo), s, o


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def descent_minq(ts, m, rng, rounds=15):
    best_ts = ts[:]
    b = build(best_ts, m)
    best = log2(qmin_fast(*b)) if b and qmin_fast(*b) else float("inf")
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(6):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 300)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                b = build(cand, m)
                if not b:
                    continue
                q = qmin_fast(*b)
                if not q or q < 2:
                    continue
                v = log2(q)
                if v < best - 1e-9:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("SMITH-INVARIANT ANATOMY (§6ai): q_min = lcm_i(s_i/gcd(s_i,c_i)), c=U^-1 d. Where is the O(m)", flush=True)
    print("residue carried after the gcd eats the O(m^2) bulk of log|detA|=sum log s_i?", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)
    print(f"{'m':>3} | {'adversary':>10} | {'log2 qmin':>9} | {'xchk':>5} | {'#o_i>1':>6} | "
          f"{'top-3 o_i (log2)':>18} | {'log2 s_top':>10}", flush=True)
    for m in range(3, 8):
        for label in ("min-q", "generic"):
            if label == "min-q":
                s0 = rng.sample(range(1, 300), m)
                ts = descent_minq(s0, m, rng)
            else:
                ts = None
                for _ in range(200):
                    cand = rng.sample(range(1, 300), m)
                    if build(cand, m):
                        ts = cand; break
            b = build(ts, m) if ts else None
            if not b:
                print(f"{m:>3} | {label:>10} | (no valid)", flush=True)
                continue
            oc, vo = b
            q_ord, q_fast, s, o = analyze(oc, vo, m)
            xchk = (q_ord == q_fast)
            contributing = [x for x in o if x > 1]
            top = sorted(contributing, reverse=True)[:3]
            top_l = [round(log2(x), 2) for x in top]
            s_top = round(log2(max(s)), 2) if s and max(s) > 0 else 0
            print(f"{m:>3} | {label:>10} | {log2(q_fast):9.2f} | {str(xchk):>5} | {len(contributing):>6} | "
                  f"{str(top_l):>18} | {s_top:>10}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): xchk must be True (order formula == qmin_fast; validates the SNF).  If at the", flush=True)
    print("min-q adversary the surviving o_i>1 are FEW (bounded count) and TOP-heavy (q_min ~ a couple of", flush=True)
    print("large invariants), the floor localizes to 'd cannot align with the top-O(1) Smith invariants'", flush=True)
    print("-- a concrete target.  If instead ~m invariants each contribute O(1), the O(m) residue is", flush=True)
    print("DIFFUSE (a different mechanism).  Compare min-q vs generic to see what the adversary changes.", flush=True)
    print("Bounded search, one orbit (D=425).  Evidence, not proof.  RH stays [OUT].", flush=True)
