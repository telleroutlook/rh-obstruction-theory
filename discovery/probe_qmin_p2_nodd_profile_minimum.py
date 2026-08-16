#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bz — the PROFILE-MINIMUM route: an UNCONDITIONAL exact floor for m ≡ 0 (mod 4), orbit-free.

§6by discovered W_top := v₂(w_{m−1}) is NEGATIVE-LINEAR and orbit-independent:
      W_top(m) = 1 − 3m/2   (m ≡ 0 mod 4),      W_top(m) = 2 − 3m/2   (m ≡ 2 mod 4),
and that at m ≡ 0 mod 4 EVERY column is "leading-dominated" (C_j = W_top for all j), while at m ≡ 2 mod 4
the top two profile entries TIE (matching the §6bv adjacent r=(0,1) tie) and the adversary gains a bounded lift.

STRUCTURAL EXPLANATION (to be PROVED): the pairing splits  S_j = w_{m−1} + Σ_{i<m−1} ±e_{m−1−i}(X'_j) w_i.
Each x_k is a 2-adic UNIT ⇒ v₂(e_r(X'_j)) ≥ 0 ⇒ v₂(term_i) ≥ v₂(w_i).  Hence
      if  v₂(w_{m−1}) < v₂(w_i)  for ALL i < m−1  (STRICT unique profile minimum at the top),
then v₂(rest) > v₂(w_{m−1}), so by the ultrametric  C_j = v₂(S_j) = v₂(w_{m−1}) = W_top  for EVERY column,
UNCONDITIONALLY (no adversary, no minimax).  Then the EXACT §6bf identity gives
      v₂(q_min) = 1 + max_j N_j − W_top  ≥  1 + 3(m−1) − W_top  =  (9m/2) − 3   [LINEAR, m ≡ 0 mod 4].
So the whole minimax difficulty is CONFINED to m ≡ 2 mod 4 (top-two tie); m ≡ 0 mod 4 needs only the PROFILE
LEMMA "w_{m−1} is the strict min of the valuation profile", checkable/derivable from the §6bm closed form.

THIS PROBE (EXACT, L9), n-odd orbits × m ∈ {4,6,8,10,12,14,16}:
  (A) prints the full profile v₂(w_i), i=0..m−1, and the gap g(m) = min_{i<m−1} v₂(w_i) − v₂(w_{m−1});
      LEMMA needs g(m) ≥ 1 (m≡0 mod4).  Confirms the tie g=0 at m≡2 mod4.
  (B) checks the closed form W_top(m) = 1−3m/2 (m≡0), 2−3m/2 (m≡2), orbit-independent.
  (C) UNCONDITIONAL test: over MANY random collisions, is C_j == W_top for EVERY column (m≡0 mod4)?
      and does it FAIL (some C_j > W_top via cancellation) at m≡2 mod4?  This is the theorem's crux.
DECISION (L5): g(m)≥1 at m≡0 mod4 AND (C) all-columns-dominated unconditionally ⇒ EXACT linear floor is a
THEOREM for m≡0 mod4 with NO minimax.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column
from discovery.probe_qmin_Cj_bilinear import vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def profile(w, m):
    return [vp_frac(Fr(w[i]), 2) for i in range(m)]


def closed_form_Wtop(m):
    return (1 - 3 * m // 2) if m % 4 == 0 else (2 - 3 * m // 2)


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bz: profile-minimum route — UNCONDITIONAL exact floor for m≡0 mod4 (no minimax). RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1))]
    MS = [4, 6, 8, 10, 12, 14, 16]
    rng = random.Random(20260826)

    cf_ok = True
    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("\norbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        for m in MS:
            w = wvec(m, sig, tau)
            prof = profile(w, m)
            Wtop = prof[m - 1]
            gap = min(prof[:m - 1]) - Wtop            # LEMMA needs >=1 at m≡0 mod4; =0 (tie) at m≡2 mod4
            cf = closed_form_Wtop(m)
            if cf != Wtop:
                cf_ok = False

            # (C) UNCONDITIONAL leading-domination test over many random collisions
            alldom = 0; some_notdom = 0; trials = 0; att = 0
            pool = max(200, 14 * m)
            while trials < 120 and att < 4000:
                att += 1
                ts = rng.sample(range(1, pool), m)
                pc = per_column(ts, m, w)
                if pc is None:
                    continue
                trials += 1
                if all(c == Wtop for c in pc[1]):
                    alldom += 1
                if any(c > Wtop for c in pc[1]):     # cancellation lifted some column above the leading term
                    some_notdom += 1
            mod = "≡0" if m % 4 == 0 else "≡2"
            print("  m=%2d (%s) W_top=%3d [cf %3d %s]  gap=%2d  top2=(%d,%d)  all-dom %3d/%3d  lifted %3d/%3d" % (
                m, mod, Wtop, cf, "OK" if cf == Wtop else "XX", gap,
                prof[m - 1], prof[m - 2], alldom, trials, some_notdom, trials), flush=True)
        # one full profile print for the smallest m to show the shape
        w = wvec(8, sig, tau)
        print("    profile v₂(w_i) i=0..7 (m=8): %s" % profile(w, 8), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("closed form W_top = 1−3m/2 (m≡0), 2−3m/2 (m≡2) across all orbits: %s" % (
        "CONFIRMED" if cf_ok else "REFUTED"), flush=True)
    print("READING (L5): gap≥1 AND all-dom=trials at m≡0 mod4 ⇒ C_j=W_top UNCONDITIONALLY ⇒ exact linear floor", flush=True)
    print("v₂(q_min)=1+max_j N_j−W_top≥(9m/2)−3 is a THEOREM for m≡0 mod4, NO minimax. m≡2 mod4 (tie, lifted>0)", flush=True)
    print("remains the sole open core. RH stays [OUT].", flush=True)
