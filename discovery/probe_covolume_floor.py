#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

DECISIVE EXPERIMENT for the arithmetic channel of Open Problem 1.

Established so far (verify_chebyshev_reformulation.py):
  * O_j(orbit) = 8(1 - Re T_j(u)),  u=(w+1/w)/2, w=1-1/rho   [EXACT]
  * archimedean Chebyshev bound sum_online|c| >= |q||T_m(u*)| holds but is LOOSE
    (Gamma ~ 1.21 => |T_m| ~ 1, cannot explain the observed 10^19 floor).
  * => the exponential floor is ARITHMETIC (integrality + denominators).

HYPOTHESIS to test here:  the floor is a LATTICE-COVOLUME effect.  Writing the
denominator-cleared integer value vectors  v_0,...,v_K in Z^m  (v_k for online
node t_k, v_K for the offline orbit), the integer relations form the kernel
lattice
        Lambda = { c in Z^{K+1} : sum_k c_k v_k = 0 }  (rank r = K+1-m).
For a "balanced" lattice the shortest vector satisfies
        lambda_1(Lambda) ~ covol(Lambda)^{1/r}.
covol(Lambda) = sqrt(det(V V^T)) / g,  V the m x (K+1) integer matrix,
g = gcd of the m x m minors of V (m-th determinantal divisor).

If  log2(shortest relation)  ~  (1/r) log2 covol(Lambda),  then the floor IS the
covolume, and proving covol grows exponentially in m (it must: entries of v_k
carry denominators N_k^j cleared to a common (lcm N_k)^m factor) proves an
exponential lower bound -- the provable core of the arithmetic channel.

We compute covol exactly (Bareiss integer determinant of V V^T; g via gcd of a
random-ish spanning set of m x m minors -> use Smith/gcd of all-but-too-many;
here K is small so we can gcd all C(K+1,m) minors) and compare to the exact-LLL
shortest relation (q != 0).
"""
from __future__ import annotations
from fractions import Fraction as Fr
from itertools import combinations
from math import gcd, log2
import discovery.probe_overdetermined_collision as P
from discovery.verify_chebyshev_reformulation import cheb_T_complex, w_and_u


def O_orbit_direct(sigma, tau, m):
    """O_j of orbit {sigma±i tau,(1-sigma)±i tau}, j=1..m (checker convention)."""
    sigma, tau = Fr(sigma), Fr(tau)
    atoms = [(sigma, tau), (sigma, -tau), (1 - sigma, tau), (1 - sigma, -tau)]
    out = []
    for j in range(1, m + 1):
        s = Fr(0)
        for (re, im) in atoms:
            for (r2, i2) in ((re, im), (1 - re, im)):
                s += P._phi_re(j, r2, i2)
        out.append(s)
    return out


def shortest_rel_custom(ts, dvec, m, weight_bits=24):
    """Shortest integer relation sum n_k C(t_k) + q dvec = 0 with q!=0 (LLL)."""
    import math as _m
    vecs = [P.C_vec(t, m) for t in ts] + [dvec]
    K1 = len(vecs); Lden = 1
    for v in vecs:
        for x in v:
            Lden = Lden * x.denominator // _m.gcd(Lden, x.denominator)
    Vint = [[int(x * Lden) for x in v] for v in vecs]
    w = 1 << weight_bits; basis = []
    for i in range(K1):
        row = [0] * K1 + [w * c for c in Vint[i]]; row[i] = 1; basis.append(row)
    red = P.lll(basis); best = None
    for row in red:
        c = row[:K1]; tail = row[K1:]
        if any(tail) or c[-1] == 0:
            continue
        mc = max(abs(v) for v in c)
        if best is None or mc < best[2]:
            best = (c[:-1], c[-1], mc)
    return best


def bareiss_det(M):
    """Exact integer determinant via Bareiss (M list of lists of int)."""
    n = len(M)
    A = [row[:] for row in M]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if sw is None:
                return 0
            A[k], A[sw] = A[sw], A[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def cleared_int_matrix(ts, sigma, tau, m):
    """Return V (m x (K+1) integer matrix): columns = online vectors C_vec(t_k)
    then the offline orbit vector, all cleared by one common denominator."""
    cols = [P.C_vec(t, m) for t in ts] + [O_orbit_direct(sigma, tau, m)]
    Lden = 1
    for v in cols:
        for x in v:
            Lden = Lden * x.denominator // gcd(Lden, x.denominator)
    Vint_cols = [[int(x * Lden) for x in v] for v in cols]   # (K+1) columns
    # V as m rows x (K+1) cols
    K1 = len(cols)
    V = [[Vint_cols[c][r] for c in range(K1)] for r in range(m)]
    return V, Lden


def kernel_covolume(V):
    """covol of {c in Z^{K+1}: V c = 0}. V is m x (K+1), assume rank m.
    covol = sqrt(det(V V^T)) / g,  g = gcd of all m x m minors of V."""
    m = len(V)
    K1 = len(V[0])
    # det(V V^T) exact
    VVt = [[sum(V[i][k] * V[j][k] for k in range(K1)) for j in range(m)]
           for i in range(m)]
    detG = bareiss_det(VVt)          # = sum of squares of m x m minors (>=0)
    # g = gcd of all m x m minors
    g = 0
    for cols in combinations(range(K1), m):
        minor = bareiss_det([[V[i][c] for c in cols] for i in range(m)])
        g = gcd(g, minor)
    return detG, g


if __name__ == "__main__":
    print("=" * 72)
    print("Decisive test: is the collision floor = kernel-lattice covolume?")
    print("DISCOVERY TIER (conjecture only).")
    print("=" * 72)
    sigma, tau = Fr(3, 4), Fr(1)
    print(f"off-line orbit sigma={sigma}, tau={tau};  online nodes t_k=1/2+i\n")
    print(f"{'m':>3} {'K':>3} {'r=K+1-m':>7} | {'log2 shortest(q!=0)':>19} | "
          f"{'log2 covol':>11} | {'log2 covol / r':>14} | {'ratio':>6}")
    print("-" * 92)
    for m in range(2, 7):
        K = m + 3
        r = K + 1 - m
        ts = [Fr(1, 2) + Fr(i) for i in range(K)]
        # shortest relation with q != 0
        best = shortest_rel_custom(ts, O_orbit_direct(sigma, tau, m), m)
        if best is None:
            print(f"{m:>3} {K:>3} {r:>7} | (no relation)")
            continue
        nc, q, mc = best
        # use L2 norm of the full coeff vector as lambda_1 proxy
        coeffs = list(nc) + [q]
        l2 = sum(c * c for c in coeffs) ** 0.5
        log2_short = log2(l2) if l2 > 0 else 0
        # covolume
        V, Lden = cleared_int_matrix(ts, sigma, tau, m)
        detG, g = kernel_covolume(V)
        # covol = sqrt(detG)/g
        log2_covol = 0.5 * log2(detG) - log2(g) if detG > 0 and g > 0 else 0
        per_r = log2_covol / r
        ratio = log2_short / per_r if per_r != 0 else float("nan")
        print(f"{m:>3} {K:>3} {r:>7} | {log2_short:>19.3f} | "
              f"{log2_covol:>11.2f} | {per_r:>14.3f} | {ratio:>6.3f}")
    print("\nInterpretation:")
    print("  If 'ratio' (log2 shortest / (log2 covol / r)) ~ 1 and STABLE across")
    print("  m, the floor IS the covolume^(1/r) => a balanced kernel lattice.")
    print("  Then an exponential lower bound reduces to: covol(Lambda) grows")
    print("  exponentially in m -- provable from the denominator (N_k^m) growth")
    print("  of the cleared value vectors.  That is the arithmetic channel's core.")
    print("  If ratio << 1 (short vector far below covol^(1/r)): the lattice has")
    print("  an anomalously short relation -> covolume alone won't prove the floor.")
