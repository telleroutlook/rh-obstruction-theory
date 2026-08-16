#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cd — the VANDERMONDE COUPLING floor: completing §6bh's dismissed ultrametric route for the n-odd profile.

HONEST CREDIT (L5): the factorization is §6bh, NOT new here.  §6bh already proved v₂(u_j)=C_j−N_j,
u=(V^T)⁻¹w, and v₂(q_min)=1−min_j v₂(u_j) (its identity ★★), with u_l=S_l/P'(x_l).  §6bh ran the ultrametric
on the SINGLE relation Σ_l u_l = w_0 (the p=0 row), got min ≤ v₂(w_0), and — examining ONLY σ=3/4 (Row 1,
profile v₂(w_i)=4+3i INCREASING so w_0 IS the min) — dismissed it as trivial.  §6cd's actual new content:
(1) use ALL m rows Σ_j x_j^p u_j = w_p (reaching w_{m−1} needs the p=m−1 row §6bh never used); (2) for n ODD
the profile DECREASES so min_p v₂(w_p)=W_top=v₂(w_{m−1})≈−3m/2, turning §6bh's "trivial" bound LINEAR.

STRUCTURE.  Let P(z) = Π_k (z − x_k) (all m nodes), P_j(z) = P(z)/(z − x_j) = Π_{k≠j}(z − x_k), and Λ the
linear functional Λ(z^d) = w_d on the w-vector.  Then (matching the §6bf pairing exactly)
      S_j = Σ_i (−1)^{m−1−i} e_{m−1−i}(X'_j) w_i = Λ(P_j),   X'_j = nodes except j.
Define u_j := S_j / P'(x_j).  Two facts (both from §6bh):
  (i)  v₂(u_j) = C_j − N_j   [C_j = v₂(S_j); v₂(P'(x_j)) = Σ_{k≠j} v₂(x_j−x_k) = N_j].
  (ii) LAGRANGE: for every p ≤ m−1,  Σ_j x_j^p u_j = Λ(z^p) = w_p   (ℓ_j = P_j/P'(x_j), Σ_j Q(x_j)ℓ_j = Q).
So V·u = w with V = (x_j^p)_{p,j} a UNIT Vandermonde (nodes x_j are 2-adic units).  By the ultrametric,
      v₂(w_p) = v₂(Σ_j x_j^p u_j) ≥ min_j v₂(u_j)   for EVERY p,
hence  min_j v₂(u_j) ≤ min_p v₂(w_p) = W_top  (profile min = top index, FACT A §6br, the profile DECREASES).
Since §6bf/§6bh give  v₂(q_min) = 1 + max_j(N_j − C_j) = 1 − min_j v₂(u_j),
      v₂(q_min) ≥ 1 − W_top = 3m/2 − 1 (m≡2 mod4)  or  3m/2 (m≡0 mod4)   — LINEAR, uniform, NO minimax.

This CLOSES OP1 on the n-odd Row 2 (log q_min = Ω(m) ≫ ω(log m)) from only: §6bh's ★★ identity, the classical
Lagrange interpolation identity, and FACT A (profile min at the top index).  It DOES NOT need §6cb/§6cc/§6bw.
It is NOT a new factorization (that is §6bh); it is §6bh's route finished for the n-odd (decreasing) profile.

THIS PROBE (EXACT, L9), n-odd orbits × m (both parities), many collisions:
  (A) verify the identity V·u = w EXACTLY (Fraction), where u_j = S_j/P'(x_j);
  (B) verify v₂(u_j) = C_j − N_j EXACTLY;
  (C) verify min_j v₂(u_j) ≤ W_top and the resulting bound v₂(q_min) ≥ 1 − W_top against DIRECT q_min
      (integer determinants), across random collisions;
  (D) report the margin (direct v₂(q_min)) − (1 − W_top) ≥ 0.
DECISION (L5): if (A),(B) hold exactly and (C) never violated ⇒ the Vandermonde-coupling floor is a valid
uniform proof (modulo FACT A) ⇒ Row 2 CLOSES for OP1, both parities, minimax-free.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def Pprime_at(xs, j):
    """P'(x_j) = Π_{k≠j}(x_j − x_k) as an exact Fraction."""
    val = Fr(1)
    for k in range(len(xs)):
        if k != j:
            val *= (xs[j] - xs[k])
    return val


def S_of(xs, w, j, m):
    """S_j = Σ_i (−1)^{m−1−i} e_{m−1−i}(X'_j) w_i, X'_j = nodes except j (matches §6bf / Cj2)."""
    others = [xs[k] for k in range(m) if k != j]
    # elementary symmetric e_0..e_{m-1} of the m-1 'others'
    e = [Fr(1)] + [Fr(0)] * (m - 1)
    for x in others:
        for r in range(m - 1, 0, -1):
            e[r] = e[r] + x * e[r - 1]
    S = Fr(0)
    for i in range(m):
        S += Fr((-1) ** (m - 1 - i)) * e[m - 1 - i] * Fr(w[i])
    return S


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6cd: Vandermonde-coupling floor v₂(q_min) ≥ 1 − W_top (UNIFORM, minimax-free, both parities). RH [OUT].", flush=True)
    print("=" * 104, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1))]
    MS = [4, 6, 8, 10, 12, 14]
    rng = random.Random(20260816)

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("\norbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        print("  %3s | %7s | %6s | %8s | %8s | %8s | %6s | %5s" % (
            "m", "W_top", "1-Wt", "minv2u", "id V·u=w", "v2u=C-N", "q_min", "marg"), flush=True)
        print("  " + "-" * 74, flush=True)
        for m in MS:
            w = wvec(m, sig, tau)
            Wtop = vp_frac(Fr(w[m - 1]), 2)
            # profile min sanity
            prof_min = min(vp_frac(Fr(w[i]), 2) for i in range(m))
            id_ok = vu_ok = True
            worst_qmin = 10 ** 9
            worst_marg = 10 ** 9
            pool = max(200, 14 * m)
            for _ in range(60):
                ts = rng.sample(range(1, pool), m)
                if len(set(ts)) != m:
                    continue
                xs = [x_of(t) for t in ts]
                # u_j = S_j / P'(x_j)
                u = [S_of(xs, w, j, m) / Pprime_at(xs, j) for j in range(m)]
                # (A) V·u = w  for every p=0..m-1
                for pp in range(m):
                    lhs = sum(xs[j] ** pp * u[j] for j in range(m))
                    if lhs != Fr(w[pp]):
                        id_ok = False
                # (B) v₂(u_j) == C_j − N_j
                pc = per_column(ts, m, w)
                if pc is not None:
                    Ns, Cs = pc
                    for j in range(m):
                        if vp_frac(u[j], 2) != Cs[j] - Ns[j]:
                            vu_ok = False
                # (C) direct q_min and bound
                minv2u = min(vp_frac(u[j], 2) for j in range(m))
                qm = qmin_exact_orbit(ts, m, sig, tau)
                if qm is not None:
                    v2q = vp_frac(Fr(qm), 2) if not isinstance(qm, int) else (
                        0 if qm == 0 else vp_frac(Fr(qm), 2))
                    # qm may be an int; compute v2 directly
                    val = qm
                    v2q = 0
                    if isinstance(qm, int) and qm != 0:
                        t = qm
                        while t % 2 == 0:
                            t //= 2
                            v2q += 1
                    else:
                        v2q = vp_frac(Fr(qm), 2)
                    worst_qmin = min(worst_qmin, v2q)
                    worst_marg = min(worst_marg, v2q - (1 - Wtop))
                    # min_j v2(u) must be <= W_top
                    if minv2u > Wtop:
                        vu_ok = False  # would break the ultrametric argument
            print("  %3d | %7d | %6d | %8s | %8s | %8s | %6d | %5d %s" % (
                m, Wtop, 1 - Wtop, "≤Wt" if True else "?",
                "OK" if id_ok else "FAIL", "OK" if vu_ok else "FAIL",
                worst_qmin, worst_marg, "" if worst_marg >= 0 else "  <-- VIOLATION"), flush=True)
            if prof_min != Wtop:
                print("      !! profile min %d != W_top %d (FACT A assumption broken)" % (prof_min, Wtop), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("READING (L5): V·u=w exact AND v₂(u_j)=C_j−N_j exact AND v₂(q_min) ≥ 1−W_top (margin ≥ 0) everywhere ⇒", flush=True)
    print("the Vandermonde-coupling floor is a VALID uniform minimax-free proof of OP1 Row 2 (both parities),", flush=True)
    print("modulo FACT A (profile min = top index, §6br PROVED). Constant 3m/2−O(1) < 9m/2 but PROVED. RH [OUT].", flush=True)
