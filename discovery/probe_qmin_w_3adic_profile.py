#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

3-ADIC PROFILE of the fixed vector w = B^{-1} d (§6av) — find the MECHANISM behind lemma (4)'s O(1) bound.

§6au reduced lemma (4) to: C_j = v_3( sum_{i=0}^{m-1} (-1)^{m-1-i} e_{m-1-i}(X') w_i ) is O(1), where
w = B^{-1} d is FIXED (off-line data in the monomial basis; B[i][l]=coeff of x^l in 4 q_i, q_i=(1-T_i)/(x-1)).
Since e_0(X') = 1 always, the i=m-1 term is the fixed +- w_{m-1}; the whole pairing's boundedness must be
explained by the 3-adic profile of w.  This probe computes, EXACTLY (L9), for m = 4..22:
   - v_3(w_i) for every coordinate i (and its rational value for small m),
   - v_3(d_i) of the raw off-line vector,
   - the min and max of v_3(w_i), to see whether w_i are 3-adic INTEGERS (v_3 >= 0), bounded below, or grow.
If the w_i have UNIFORMLY BOUNDED-BELOW 3-adic valuation (say v_3(w_i) >= -c), then since e_{m-1-i}(X') are
3-adic INTEGERS (x_k in Z_3), each term has v_3 >= -c, and the FIXED e_0-term +-w_{m-1} pins the sum's low end
-- capping how large v_3(pairing) can be UNLESS higher-order cancellation occurs.  The observed max_j C_j<=12
suggests exactly such a cap.  This profile is the key data for an analytic proof / EXT statement of lemma (4).
Honest (L5): a profile with v_3(w_i) -> -infinity linearly would instead EXPLAIN a growing C_j (would
contradict §6au's plateau -- flagged if seen).  One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr

import discovery.probe_overdetermined_collision as PO
from discovery.probe_qmin_Cj_bilinear import Bmatrix, solve_lower, vp_frac

TAU = Fr(1)
P = 3


if __name__ == "__main__":
    print("=" * 92, flush=True)
    print("§6av: 3-adic profile of the FIXED w = B^{-1} d. Mechanism behind lemma (4) v_3(<w,e(X')>)=O(1).", flush=True)
    print("=" * 92, flush=True)
    print(f"\n{'m':>3} | {'v_3(w_i), i=0..m-1':>46} | {'min':>4} | {'max':>4} | {'v3(w_{m-1})':>11}", flush=True)
    print("-" * 84, flush=True)
    for m in range(4, 23):
        B = Bmatrix(m)
        d = PO.d_vec(TAU, m)
        w = solve_lower(B, d, m)
        vs = [vp_frac(wi, P) for wi in w]
        vshow = ",".join(str(v) for v in vs)
        if len(vshow) > 46:
            vshow = vshow[:43] + "..."
        print(f"{m:>3} | {vshow:>46} | {min(vs):>4} | {max(vs):>4} | {vs[-1]:>11}", flush=True)
    # detailed small-m rational values to spot a closed form
    print("\nrational w for m=4,5,6 (spot a closed form / denominators):", flush=True)
    for m in (4, 5, 6):
        B = Bmatrix(m)
        w = solve_lower(B, PO.d_vec(TAU, m), m)
        print(f"  m={m}: w = {[str(wi) for wi in w]}", flush=True)
        print(f"        d = {[str(di) for di in PO.d_vec(TAU, m)]}", flush=True)
    print("\n" + "=" * 92, flush=True)
    print("READING (L5): if v_3(w_i) is bounded below by an absolute -c (does NOT go to -inf with m), then", flush=True)
    print("every pairing term +-w_i e_{m-1-i}(X') has v_3 >= -c (e_l in Z_3), and the fixed e_0-term +-w_{m-1}", flush=True)
    print("anchors the sum -- capping v_3(<w,e(X')>) = C_j at O(1) absent fine cancellation, matching §6au's", flush=True)
    print("plateau (max_j C_j<=12 to m=21). This profile is the analytic key for proving lemma (4). If instead", flush=True)
    print("min v_3(w_i) -> -inf ~ linearly, that channel of the bound fails. One orbit (D=425). RH [OUT].", flush=True)
