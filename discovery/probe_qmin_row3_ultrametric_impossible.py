#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cg — IMPOSSIBILITY probe: the moment-side ultrametric (the §6cd/§6bh machinery) provably CANNOT
produce the Row-3 (n≡2 mod4, 3∤n) floor at p=3.  The open core is intrinsically DETERMINANTAL.

ARGUMENT (see §6cg in op1_arithmetic_floor_findings.md).  With u = (Vᵀ)⁻¹w (V=(x_jᵖ) the node
Vandermonde, u_j = S_j/P'(x_j)), the §6bh identity gives v₃(q_min) = −min_j v₃(u_j).  The ONLY lower
bound on v₃(q_min) obtainable from the Lagrange relations Σ_j x_jᵖ u_j = w_p plus the ultrametric is
        v₃(q_min) = −min_j v₃(u_j) ≥ −min_p v₃(w_p).
For Row 3, w is a 3-UNIT vector (v₃(w_p)=0 ∀p), so this PROVABLE floor is exactly 0 — trivial — no
matter how the m relations are combined (every RHS Λ(g) is a Z₃-combination of units, v₃ ≥ 0).

Yet the TRUE floor is strongly positive (empirically ≈ 9m/2): min_j v₃(u_j) is deeply NEGATIVE,
driven by v₃(det V) NOT being absorbed by the gcd of the Cramer numerators D_j.  The gap between the
ultrametric ceiling (0) and the true floor is precisely the Smith/lattice non-absorption content.

THIS PROBE (EXACT, L9) verifies, for Row-3 orbits × m, over random on-line node sets:
  (A) V·u = w  exact (Fraction), u_j = S_j/P'(x_j);
  (B) the ULTRAMETRIC CEILING  min_p v₃(w_p) = 0  (w a 3-unit) ⇒ provable floor = 0;
  (C) the TRUE  min_j v₃(u_j) = −v₃(q_min)  is strongly NEGATIVE (true floor ≫ 0);
so the provable floor (0) ≪ true floor — the ultrametric route is dead for Row 3 by construction.
DECISION (L5): if (A) holds and provable=0 while true>0 everywhere ⇒ §6cg impossibility confirmed;
(4″) must be posed as a determinantal (Smith-normal-form) nugget, not a valuation-transfer one. RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn
from discovery.probe_qmin_p2_nodd_vandermonde_floor import Pprime_at, S_of


def v3_int(q):
    """v₃ of a nonzero integer q."""
    v = 0
    while q % 3 == 0:
        q //= 3
        v += 1
    return v


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6cg: Row-3 ultrametric IMPOSSIBILITY — provable floor = 0 (w a 3-unit) ≪ true floor. RH [OUT].", flush=True)
    print("=" * 104, flush=True)

    # Row 3: n≡2 mod4, 3∤n. tau=1.
    ORBITS = [(Fr(1, 2), Fr(1)), (Fr(3, 10), Fr(1)), (Fr(7, 10), Fr(1))]
    MS = [4, 5, 6, 7, 8]
    rng = random.Random(20260816)
    all_ok = True

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        assert n % 4 == 2 and n % 3 != 0, "orbit is not Row 3"
        print("\norbit (%s,%s) n=%d [Row 3]:" % (sig, tau, n), flush=True)
        print("  %3s | %-14s | %-16s | %-14s | %s" % (
            "m", "id V·u=w", "ultra ceiling", "TRUE min v₃(u)", "provable≪true?"), flush=True)
        print("  " + "-" * 78, flush=True)
        for m in MS:
            w = wvec(m, sig, tau)
            w3 = [vp_frac(Fr(w[i]), 3) for i in range(m)]
            ceiling = -min(w3)                    # provable floor = −min_p v₃(w_p)
            id_ok = True
            worst_true = 10 ** 9                  # min over samples of TRUE min_j v₃(u_j)
            worst_qmin = 10 ** 9
            pool = max(200, 14 * m)
            for _ in range(40):
                ts = rng.sample(range(1, pool), m)
                if len(set(ts)) != m:
                    continue
                xs = [x_of(t) for t in ts]
                u = [S_of(xs, w, j, m) / Pprime_at(xs, j) for j in range(m)]
                for pp in range(m):               # (A) exact Lagrange relations
                    if sum(xs[j] ** pp * u[j] for j in range(m)) != Fr(w[pp]):
                        id_ok = False
                minv3u = min(vp_frac(u[j], 3) for j in range(m))   # (C) TRUE
                worst_true = min(worst_true, minv3u)
                qm = qmin_exact_orbit(ts, m, sig, tau)
                if isinstance(qm, int) and qm != 0:
                    worst_qmin = min(worst_qmin, v3_int(qm))
            # provable floor = ceiling (=0 for a unit w); true floor = −worst_true (≥)
            provable = ceiling
            true_floor = -worst_true
            gap_ok = (provable == 0) and (true_floor > 0)
            all_ok = all_ok and id_ok and gap_ok
            print("  %3d | %-14s | min_p v₃(w)=%2d | %-14d | provable=%d, true≈%d  %s" % (
                m, "OK" if id_ok else "FAIL", min(w3), worst_true, provable, true_floor,
                "YES" if gap_ok else "-- CHECK"), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("READING (L5): V·u=w exact, ultrametric ceiling = 0 (w is a 3-unit), yet true min_j v₃(u_j) is", flush=True)
    print("strongly negative ⇒ the §6cd/§6bh moment-side route CANNOT prove the Row-3 floor. The (4″) core is", flush=True)
    print("intrinsically Smith/lattice non-absorption of v₃(det V). §6cg impossibility: %s. RH [OUT]." % (
        "CONFIRMED" if all_ok else "NEEDS REVIEW"), flush=True)
