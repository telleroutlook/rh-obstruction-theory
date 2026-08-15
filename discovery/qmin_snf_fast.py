#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

Fast q_min via Smith Normal Form.  q_min = [L + Z voff : L], L = colspan_Z(M),
M = integer on-line columns (m x K).  We use the identity

    q_min = D_r(M) / D_r([M | voff]),

where D_r = product of the (nonzero) invariant factors of the matrix = the r-th
determinantal divisor = gcd of all r x r minors = lattice index [Z^r : sublattice].
SNF computes the invariant factors in POLYNOMIAL time (no minor enumeration), so
this handles large node pools that the gcd-of-all-minors route cannot.
"""
from __future__ import annotations
from math import gcd


def _snf_invariant_product(M):
    """Product of the nonzero invariant factors of integer matrix M (list of
    rows).  Equals the top determinantal divisor D_r (r = rank).  Integer SNF by
    repeated pivoting; returns (product, rank)."""
    A = [row[:] for row in M]
    rows = len(A)
    cols = len(A[0]) if rows else 0
    prod = 1
    r = 0
    for t in range(min(rows, cols)):
        # find a pivot (smallest nonzero abs) in submatrix A[t:, t:]
        while True:
            piv = None
            for i in range(t, rows):
                for j in range(t, cols):
                    if A[i][j] != 0 and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])):
                        piv = (i, j)
            if piv is None:
                return prod, r          # no more nonzero -> done
            pi, pj = piv
            A[t], A[pi] = A[pi], A[t]
            for row in A:
                row[t], row[pj] = row[pj], row[t]
            # reduce column t and row t against the pivot
            changed = False
            for i in range(t + 1, rows):
                if A[i][t] != 0:
                    q = A[i][t] // A[t][t]
                    if q:
                        for j in range(cols):
                            A[i][j] -= q * A[t][j]
                    if A[i][t] != 0:
                        changed = True
            for j in range(t + 1, cols):
                if A[t][j] != 0:
                    q = A[t][j] // A[t][t]
                    if q:
                        for i in range(rows):
                            A[i][j] -= q * A[i][t]
                    if A[t][j] != 0:
                        changed = True
            if not changed:
                # ensure divisibility: if pivot doesn't divide some entry, keep going
                bad = False
                for i in range(t + 1, rows):
                    for j in range(t + 1, cols):
                        if A[i][j] % A[t][t] != 0:
                            # add row i into row t to expose a smaller gcd
                            for k in range(cols):
                                A[t][k] += A[i][k]
                            bad = True
                            break
                    if bad:
                        break
                if not bad:
                    break
        prod *= abs(A[t][t])
        r += 1
    return prod, r


def qmin_fast(on_cols, voff):
    """q_min = D_r(M) / D_r([M | voff]) via SNF.  on_cols: list of integer
    columns (each length m); voff: integer column length m.  Returns int or None
    if voff not in the rational span (no finite collision)."""
    m = len(voff)
    M = [[on_cols[k][i] for k in range(len(on_cols))] for i in range(m)]   # m x K
    Maug = [M[i] + [voff[i]] for i in range(m)]
    dM, rM = _snf_invariant_product(M)
    dA, rA = _snf_invariant_product(Maug)
    if rA > rM:                      # voff added rank -> not in span(M)
        return None
    if dA == 0:
        return None
    return dM // dA
