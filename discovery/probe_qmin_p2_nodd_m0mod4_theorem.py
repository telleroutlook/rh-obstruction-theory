#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6ca — CLOSE THE LOOP: direct q_min verification of the m≡0 mod4 exact-floor theorem candidate, and
confirm the period-4 profile / strict-min dichotomy at larger m.

THEOREM CANDIDATE (n-odd Row 2, m ≡ 0 mod 4, orbit-independent), assembled from already-proved facts:
  (i)  FACT A (§6br, PROVED): v₂(w_i) has period-4 increments [0,−3,−1,−2]; hence for m≡0 mod4 the top
       entry i=m−1 (≡3 mod4) is the STRICT unique minimum of the profile, gap ≥ 1  (W_top = 1 − 3m/2).
  (ii) nodes x_t = (4t²−1)/(4t²+1) are 2-adic UNITS ⇒ v₂(e_r(X'_j)) ≥ 0 for every symmetric coeff.
  (iii) pairing split S_j = w_{m−1} + Σ_{i<m−1} ±e_{m−1−i}(X'_j) w_i, with v₂(each lower term) ≥ v₂(w_i)
       > v₂(w_{m−1}) by (i); so by the ultrametric  C_j = v₂(S_j) = W_top  for EVERY column & collision.
  (iv) §6bf EXACT identity v₂(q_min) = max_j(1 + N_j − C_j), and N_j = Σ_{k≠j} v₂(x_j−x_k) ≥ 3(m−1)
       UNCONDITIONAL (v₂(x_j−x_k) = 3 + v₂(t_j²−t_k²) ≥ 3).
  ⇒ v₂(q_min) = 1 − W_top + max_j N_j  EXACTLY, hence min over collisions = 1 − W_top + 3(m−1) = (9m/2) − 3.
NO adversary, NO minimax — the minimax core is confined to m ≡ 2 mod 4 (top-two tie).

THIS PROBE (EXACT, L9):
  (A) for m ∈ {4,8,12} (m≡0 mod4), compute the TRUE q_min the hard way (integer determinants,
      qmin_exact_orbit) over many collisions; verify per-collision v₂(q_min) == 1 − W_top + max_j N_j,
      and that the MINIMUM over collisions equals (9m/2) − 3.  (Guards against an identity-impl error.)
  (B) extend the profile-increment check to m ∈ {20,24}: confirm period-4 [0,−3,−1,−2] and the
      strict-min(m≡0)/tie(m≡2) dichotomy persist.
DECISION (L5): direct q_min minimum == (9m/2)−3 at m≡0 mod4 ⇒ the theorem candidate's arithmetic is
verified end-to-end (the only remaining formal gap is citing FACT A §6br). RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import vp_frac, vp_int
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def profile_increments(w, m):
    prof = [vp_frac(Fr(w[i]), 2) for i in range(m)]
    return prof, [prof[i] - prof[i - 1] for i in range(1, m)]


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6ca: DIRECT q_min check of the m≡0 mod4 exact-floor theorem candidate. RH [OUT].", flush=True)
    print("Claim: min over collisions of v₂(q_min) = (9m/2) − 3 for m≡0 mod4, unconditionally.", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1))]
    rng = random.Random(20260827)

    print("\n(A) direct q_min (integer determinants) vs identity, m≡0 mod4:", flush=True)
    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("  orbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        for m in (4, 8, 12):
            w = wvec(m, sig, tau)
            Wtop = vp_frac(Fr(w[m - 1]), 2)
            predicted_min = 1 - Wtop + 3 * (m - 1)          # = 9m/2 − 3
            observed = []
            id_ok = True
            trials = 0; att = 0
            pool = max(120, 10 * m)
            while trials < 60 and att < 6000:
                att += 1
                ts = rng.sample(range(1, pool), m)
                qm = qmin_exact_orbit(ts, m, sig, tau)
                if qm is None:
                    continue
                pc = per_column(ts, m, w)
                if pc is None:
                    continue
                trials += 1
                vq = vp_int(qm, 2)
                observed.append(vq)
                # exact identity: v₂(q_min) == 1 − W_top + max_j N_j (since C_j == W_top for all j)
                maxN = max(pc[0])
                allC = all(c == Wtop for c in pc[1])
                if not (allC and vq == 1 - Wtop + maxN):
                    id_ok = False
            omin = min(observed) if observed else None
            print("    m=%2d W_top=%3d  predicted min=(9m/2)-3=%3d  OBSERVED min=%3s  identity(all-C=W & v=1-W+maxN): %s" % (
                m, Wtop, predicted_min, omin, "OK" if id_ok else "FAIL"), flush=True)
            if omin is not None and omin != predicted_min:
                print("      NOTE: observed min %d != predicted %d (need larger sample or clustering hit floor)" % (
                    omin, predicted_min), flush=True)

    print("\n(B) period-4 profile increments & strict-min/tie dichotomy at larger m:", flush=True)
    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("  orbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        for m in (20, 24):
            w = wvec(m, sig, tau)
            prof, inc = profile_increments(w, m)
            # inc[k] = transition into index k+1; pattern keyed by (k+1) mod 4: {1:0, 2:-3, 3:-1, 0:-2}
            pat = {1: 0, 2: -3, 3: -1, 0: -2}
            per4 = all(inc[k] == pat[(k + 1) % 4] for k in range(len(inc)))
            top_gap = prof[m - 2] - prof[m - 1]              # >0 strict-min ; ==0 tie
            print("    m=%2d  incs period-4[0,-3,-1,-2]: %s  W_top=%d  top_gap=%d  (%s)" % (
                m, per4, prof[m - 1], top_gap, "strict-min" if top_gap > 0 else "TIE"), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): OBSERVED min == (9m/2)−3 and identity OK at m≡0 mod4 ⇒ theorem-candidate arithmetic", flush=True)
    print("verified end-to-end; the sole formal dependency is FACT A (§6br, period-4 profile, PROVED). The", flush=True)
    print("minimax core is now confined strictly to m≡2 mod4. RH stays [OUT].", flush=True)
