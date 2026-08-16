#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bx — COLLAPSE the per-prime C_j/N_j apparatus to ONE object: v_p(q_min) via the node-Vandermonde solve y=V⁻¹w.

The Lagrange interpolation identities  Σ_j x_j^r · (S_j / P'(x_j)) = w_r  (r=0..m−1, exact since deg≤m−1),
with S_j = ⟨w, coeffs ∏_{k≠j}(X−x_k)⟩ the off-line pairing and P'(x_j)=∏_{k≠j}(x_j−x_k), say that the vector
      y_j := S_j / P'(x_j)      (= v_p(y_j) = C_j − N_j)
solves  V y = w  where V[r][j] = x_j^r is the NODE VANDERMONDE and w is the FIXED off-line vector.  I.e.
      y = V⁻¹ w  =  the Lagrange QUADRATURE WEIGHTS representing the fixed functional L(Q)=⟨w,coeffs Q⟩:
      ⟨w, coeffs Q⟩ = Σ_j y_j Q(x_j)  for every deg≤m−1 poly Q.
Combined with the floor identity v_p(q_min) = max_j(1 + N_j − C_j) this PREDICTS the prime-/orbit-agnostic
      v_p(q_min) = 1 − min_j v_p(y_j),   y = V⁻¹ w.
So the ENTIRE floor problem = "the most p-adically-negative component of V⁻¹w", V=node Vandermonde, w fixed.

THIS PROBE (EXACT, L9) — for orbits × m × primes p∈{2,3,5}:
  (a) solves y = V⁻¹w exactly (Fraction Gaussian elimination) and cross-checks y_j == S_j/P'(x_j);
  (b) computes true q_min (qmin_exact_orbit) and DISCOVERS the offset off_p := v_p(q_min) + min_j v_p(y_j)
      — the prediction is off_p ≡ 1 for every p, orbit, m.  If off_p is a clean constant the reduction holds;
      any mismatch REFUTES it (report honestly, L5).
Adversary-free (structural identity check).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import qmin_exact_orbit, wvec
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac, elem_sym


def vandermonde_solve(xs, w):
    """Exact solve V y = w, V[r][j] = xs[j]**r (r=row=exponent, j=col=node). Returns y (list of Fraction)."""
    m = len(xs)
    # augmented matrix rows r=0..m-1
    M = [[xs[j] ** r for j in range(m)] + [Fr(w[r])] for r in range(m)]
    for c in range(m):
        piv = next(r for r in range(c, m) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for r in range(m):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [M[r][m] for r in range(m)]


def Sj_over_Pprime(xs, w, j, m):
    """y_j = S_j / P'(x_j), S_j = signed off-line pairing, P'(x_j)=∏_{k≠j}(x_j−x_k)."""
    Xp = [xs[k] for k in range(m) if k != j]
    e = elem_sym(Xp)
    S = sum((-1) ** (m - 1 - i) * e[m - 1 - i] * Fr(w[i]) for i in range(m))
    Pp = Fr(1)
    for k in range(m):
        if k != j:
            Pp *= (xs[j] - xs[k])
    return S / Pp


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6bx: does v_p(q_min) = 1 − min_j v_p(y_j) with y = V⁻¹w (node Vandermonde, fixed w)?", flush=True)
    print("=" * 104, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(3, 4), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1)), (Fr(2, 5), Fr(1))]
    PRIMES = [2, 3, 5]
    rng = random.Random(20260824)

    all_ok = True
    lagrange_ok = True
    for sig, tau in ORBITS:
        print("\norbit (%s,%s):" % (sig, tau), flush=True)
        for m in (4, 5, 6, 7):
            w = wvec(m, sig, tau)
            # a few random valid node sets
            trials = 0
            attempts = 0
            while trials < 3 and attempts < 200:
                attempts += 1
                ts = rng.sample(range(1, 40), m)
                qm = qmin_exact_orbit(ts, m, sig, tau)
                if qm is None:
                    continue
                xs = [x_of(t) for t in ts]
                y = vandermonde_solve(xs, w)
                # cross-check Lagrange identity y_j == S_j/P'(x_j)
                for j in range(m):
                    if y[j] != Sj_over_Pprime(xs, w, j, m):
                        lagrange_ok = False
                offs = []
                for p in PRIMES:
                    minv = min(vp_frac(yj, p) for yj in y)
                    vq = vp_frac(Fr(qm), p)
                    offs.append(vq + minv)          # prediction: == 1
                tag = "OK" if all(o == 1 for o in offs) else "MISMATCH"
                if tag == "MISMATCH":
                    all_ok = False
                if trials == 0:
                    print("  m=%d q_min=%d  off_p(=v_p(q)+min_j v_p(y_j)) for p=2,3,5: %s  [%s]" % (
                        m, qm, offs, tag), flush=True)
                trials += 1

    print("\n" + "=" * 104, flush=True)
    print("Lagrange identity y_j == S_j/P'(x_j): %s" % ("HOLDS" if lagrange_ok else "FAILED"), flush=True)
    print("Reduction v_p(q_min) = 1 − min_j v_p(V⁻¹w)_j across all p,orbit,m: %s" % (
        "CONFIRMED" if all_ok else "REFUTED (see MISMATCH rows)"), flush=True)
    print("If CONFIRMED: floor problem = 'most p-adically-negative component of V⁻¹w', prime-/orbit-agnostic,", flush=True)
    print("unifying all 4 coverage-map rows into ONE Vandermonde-solve object. RH stays [OUT].", flush=True)
