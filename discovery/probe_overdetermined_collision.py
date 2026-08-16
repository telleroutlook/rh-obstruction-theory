#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture only, NEVER imported into proof
steps or theorem witnesses.  No RH / RH-equivalent input; all objects are
finite explicit multisets of complex rationals.

Follow-up to probe_resource_bounded_collision.py, attacking the *positive*
side of Paper A Open Problem 1: can an OVER-DETERMINED (K > m node)
construction achieve a POLYNOMIAL-size Li-collision?

Key structural fact: O_fin^{(m)} is LINEAR in the multiset.  Writing the
on-line building block  b(t) = (C_1(t),...,C_m(t)),  C_j(t)=4(1-T_j(x)),
x=(4t^2-1)/(4t^2+1),  and the off-line quartet vector  d=(d_1,...,d_m),
d_j = O_j(Q),  a collision matching the first m Li-observations is exactly an
INTEGER linear relation

        sum_{k=1}^{K} n_k b(t_k)  +  q d  =  0,     q != 0,

split into  Z_+  (positive-coefficient on-line atoms, P=1)  and  Z_-
(negative-coefficient on-line atoms + the off-line quartet with multiplicity
|q|, P=0), after adding a common constant to make every multiplicity >= 0.
The collision's atom-count cost is governed by  max(|n_k|,|q|).

So the minimal collision size = length of the shortest integer relation among
the K+1 rational vectors {b(t_1),...,b(t_K), d}.  We find it with exact LLL on
the classic integer-relation lattice  [ I_{K+1} | w * V^T ]  (V the K+1 x m
scaled-integer matrix; large weight w forces V^T c = 0, i.e. the relation).

If max|coeff| grows only polynomially in m as K = m + O(1) (or K = O(m)),
the barrier SURVIVES a polynomial budget.  We compare against the standard
construction's log2 M from the baseline probe.
"""
from __future__ import annotations
from fractions import Fraction as Fr
import math


# --------------------------------------------------------------------------
# Chebyshev closed form for the exact building-block vectors (rational)
# --------------------------------------------------------------------------
def cheb_T(j, x):
    if j == 0:
        return Fr(1)
    a, b = Fr(1), Fr(x)
    for _ in range(1, j):
        a, b = b, 2 * x * b - a
    return b


def C_vec(t, m):
    """b(t) = (C_1,...,C_m),  C_j = 4(1 - T_j(x)),  x=(4t^2-1)/(4t^2+1)."""
    t = Fr(t)
    x = (4 * t * t - 1) / (4 * t * t + 1)
    return [4 * (1 - cheb_T(j, x)) for j in range(1, m + 1)]


def d_vec(T, m):
    """Off-line quartet vector d_j = O_j(Q), Q={3/4+-iT,1/4+-iT}.
    O_j(rho)+O_j(1-rho) summed over the quartet, via the same Chebyshev-free
    per-definition phi to stay independent of the C_vec closed form."""
    T = Fr(T)
    atoms = [(Fr(3, 4), T), (Fr(3, 4), -T), (Fr(1, 4), T), (Fr(1, 4), -T)]
    out = []
    for j in range(1, m + 1):
        s = Fr(0)
        for (re, im) in atoms:
            for (r2, i2) in ((re, im), (1 - re, im)):     # rho and 1-rho
                s += _phi_re(j, r2, i2)
        out.append(s)
    return out


def _phi_re(j, re, im):
    """Re[ 1 - (1 - 1/rho)^j ],  rho = re + i im, exact rational."""
    # 1/rho
    den = re * re + im * im
    ir, ii = re / den, -im / den
    # base = 1 - 1/rho
    br, bi = 1 - ir, -ii
    # base^j
    pr, pi = Fr(1), Fr(0)
    for _ in range(j):
        pr, pi = pr * br - pi * bi, pr * bi + pi * br
    return 1 - pr    # real part of 1 - base^j


# --------------------------------------------------------------------------
# exact-rational LLL (integer basis, Fraction Gram-Schmidt)
# --------------------------------------------------------------------------
def lll(basis, delta=Fr(3, 4)):
    B = [[Fr(v) for v in row] for row in basis]
    n = len(B)
    Bstar = [row[:] for row in B]
    mu = [[Fr(0)] * n for _ in range(n)]
    Bnorm = [Fr(0)] * n

    def dot(u, v):
        return sum(a * b for a, b in zip(u, v))

    def compute_gso():
        for i in range(n):
            Bstar[i] = B[i][:]
            for j in range(i):
                mu[i][j] = dot(B[i], Bstar[j]) / Bnorm[j]
                Bstar[i] = [a - mu[i][j] * b for a, b in zip(Bstar[i], Bstar[j])]
            Bnorm[i] = dot(Bstar[i], Bstar[i])

    compute_gso()
    k = 1
    while k < n:
        # size-reduce row k against rows k-1..0 with in-place mu updates
        for j in range(k - 1, -1, -1):
            if abs(mu[k][j]) > Fr(1, 2):
                q = _nint(mu[k][j])
                B[k] = [a - q * b for a, b in zip(B[k], B[j])]
                for l in range(j):
                    mu[k][l] -= q * mu[j][l]
                mu[k][j] -= q
        if Bnorm[k] >= (delta - mu[k][k - 1] ** 2) * Bnorm[k - 1]:
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            compute_gso()               # only after a Lovász swap
            k = max(k - 1, 1)
    return [[int(v) for v in row] for row in B]


def _nint(x):
    """nearest integer to Fraction x."""
    fl = x.numerator // x.denominator
    return fl + 1 if 2 * (x - fl) > 1 else fl


# --------------------------------------------------------------------------
# find the shortest integer collision relation among {b(t_k)} ∪ {d}
# --------------------------------------------------------------------------
def shortest_relation(ts, T, m, weight_bits=24):
    """Return (coeffs, q, maxcoeff) for the shortest integer relation
    sum n_k b(t_k) + q d = 0 with q != 0, found via LLL."""
    vecs = [C_vec(t, m) for t in ts] + [d_vec(T, m)]     # K+1 vectors in Q^m
    K1 = len(vecs)
    # clear denominators with ONE COMMON factor L across ALL vectors, so that
    # sum n_i (L v_i) = 0  <=>  sum n_i v_i = 0  (coeffs stay the true n_i).
    Lden = 1
    for v in vecs:
        for x in v:
            Lden = Lden * x.denominator // math.gcd(Lden, x.denominator)
    Vint = [[int(x * Lden) for x in v] for v in vecs]
    # integer-relation lattice:  rows = [ e_i | w * V_i ]  (V_i the i-th vector)
    w = 1 << weight_bits
    basis = []
    for i in range(K1):
        row = [0] * K1 + [w * c for c in Vint[i]]
        row[i] = 1
        basis.append(row)
    red = lll(basis)
    # a row is a genuine relation iff its trailing m coords are all 0
    best = None
    for row in red:
        coeffs = row[:K1]
        tail = row[K1:]
        if any(tail):                      # relation not exact -> skip
            continue
        if coeffs[-1] == 0:                # q == 0 -> no off-line atom, reject
            continue
        mc = max(abs(c) for c in coeffs)
        if best is None or mc < best[2]:
            best = (coeffs[:-1], coeffs[-1], mc)
    return best, K1


def verify_relation(ts, T, m, ncoeffs, q):
    """Exact check that sum n_k b(t_k) + q d = 0 in Q^m."""
    acc = [Fr(0)] * m
    for t, n in zip(ts, ncoeffs):
        for j, cj in enumerate(C_vec(t, m)):
            acc[j] += n * cj
    for j, dj in enumerate(d_vec(T, m)):
        acc[j] += q * dj
    return all(a == 0 for a in acc)


# --------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 72)
    print("Probe: OVER-DETERMINED (K>m) Li-collision — shortest integer relation")
    print("DISCOVERY TIER (conjecture only; not a proof, not a witness).")
    print("=" * 72)
    print("\nStandard (m-node) baseline for comparison: log2 M ~ 6*m (super-poly).")
    print("Here: K = m + extra on-line nodes, T=1; report shortest relation size.\n")

    T = 1
    print(f"{'m':>3} | {'K (=m+extra)':>12} | {'nodes t_k':>28} | "
          f"{'max|coeff|':>16} | {'log2':>7}")
    print("-" * 90)
    for m in range(2, 10):
        extra = 3                       # a few more nodes than equations
        K = m + extra
        # on-line nodes: distinct small half-integers to keep denominators modest
        ts = [Fr(1, 2) + Fr(i) for i in range(K)]   # 1/2, 3/2, 5/2, ...
        best, K1 = shortest_relation(ts, T, m)
        if best is None:
            print(f"{m:>3} | {K:>12} | (no q!=0 relation found)")
            continue
        ncoeffs, q, mc = best
        assert verify_relation(ts, T, m, ncoeffs, q), f"relation invalid m={m}"
        log2mc = math.log2(mc) if mc > 0 else 0
        tstr = ",".join(str(t) for t in ts)
        if len(tstr) > 26:
            tstr = tstr[:23] + "..."
        print(f"{m:>3} | {K:>12} | {tstr:>28} | {mc:>16} | {log2mc:>7.2f}")

    print("\nInterpretation:")
    print("  Compare 'log2 max|coeff|' here against the baseline log2 M (~6m).")
    print("  If it stays SMALL / grows slowly with m => a polynomial-size")
    print("  collision exists => the barrier SURVIVES a polynomial budget")
    print("  (positive answer to Open Problem 1, strengthening Theorem A).")
    print("  If it also blows up => evidence for a resource-bounded SEPARATION.")
