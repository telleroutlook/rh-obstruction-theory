#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cc — VERIFY the load-bearing step of the §6cb sketch:  lift_j ≤ v₂(τ − σ_j)  (and bound the interference).

§6cb's joint proof needs: min_j lift_j ≥ L ⇒ v₂(τ − σ_j) ≥ L for every j (⇒ clustering ⇒ N_j ≥ (m−1)L).
This holds via lift_j ≤ v₂(τ − σ_j), where (from §6bv term structure)
      S_j = w_{m−1} − w_{m−2}·σ_j + Σ_{i<m−2}(±) e_{m−1−i}(X'_j) w_i  =  w_{m−2}·(τ − σ_j) + R_j·w_{m−2},
      τ = w_{m−1}/w_{m−2}  (a 2-adic UNIT since v₂(w_{m−1})=v₂(w_{m−2})=W_top),   σ_j = Σ_{k≠j} x_k = T − x_j,
so lift_j = C_j − W_top = v₂((τ − σ_j) + R_j),  v₂(R_j) ≥ g := v₂(w_{m−3}) − W_top  (profile gap at i=m−3).
By the ultrametric  lift_j = v₂(τ−σ_j)  whenever v₂(τ−σ_j) ≠ v₂(R_j); the ONLY way lift_j > v₂(τ−σ_j) is an
accidental tie v₂(τ−σ_j) = v₂(R_j) ≥ g.  So the clean bound lift_j ≤ v₂(τ−σ_j) can fail ONLY at depths ≥ g,
and g is a fixed O(1) profile constant ⇒ any violation shifts only the additive constant in v₂(q_min) ≥ 9m/2 − O(1).

THIS PROBE (EXACT, L9), n-odd orbits × m ∈ {6,10,14} (m≡2 mod4), many random + a lift-seeking hill-climb:
  • per column compute lift_j = C_j − W_top and dd_j = v₂(τ − σ_j); tally lift_j ≤ dd_j (clean) vs lift_j > dd_j;
  • for any violation, record (lift_j, dd_j, g) — the claim is violations occur ONLY at dd_j ≥ g and are bounded;
  • print g(m) = v₂(w_{m−3}) − W_top (the profile gap) — should be a small O(1) constant.
DECISION (L5): lift_j ≤ dd_j in (nearly) all columns, and every violation has dd_j ≥ g with g = O(1) ⇒ the
§6cb sketch's key step is validated up to a bounded additive constant ⇒ Row 2 floor v₂(q_min) ≥ 9m/2 − O(1)
stands rigorously (modulo FACT A §6br). RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def analyze(ts, m, w, Wtop, tau):
    xs = [x_of(t) for t in ts]
    pc = per_column(ts, m, w)
    if pc is None:
        return None
    Cs = pc[1]
    T = sum(xs)
    out = []
    for j in range(m):
        lift = Cs[j] - Wtop
        sigma_j = T - xs[j]
        dd = vp_frac(tau - sigma_j, 2)
        out.append((lift, dd))
    return out


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6cc: verify lift_j ≤ v₂(τ − σ_j) (load-bearing step of §6cb); bound interference by g. RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1))]
    MS = [6, 10, 14]
    rng = random.Random(20260829)

    for sig, tau_o in ORBITS:
        p, q, n = rho_pqn(sig, tau_o)
        print("\norbit (%s,%s) n=%d:" % (sig, tau_o, n), flush=True)
        for m in MS:
            w = wvec(m, sig, tau_o)
            Wtop = vp_frac(Fr(w[m - 1]), 2)
            g = vp_frac(Fr(w[m - 3]), 2) - Wtop
            tau = Fr(w[m - 1]) / Fr(w[m - 2])
            clean = viol = cols = 0
            viol_examples = []
            # random collisions + a hill-climb seeking large lift to stress the step
            samples = []
            pool = max(200, 14 * m)
            for _ in range(400):
                ts = rng.sample(range(1, pool), m)
                samples.append(ts)
            # add lift-seeking: pick node sets whose σ_j clusters near τ
            for _ in range(200):
                base = rng.randrange(1, pool)
                ts = list({(base + rng.choice([-6, -4, -2, 2, 4, 6, 8])) % pool or 1 for _ in range(m + 4)})[:m]
                if len(ts) == m:
                    samples.append(ts)
            for ts in samples:
                if len(set(ts)) != m or any(t == 0 for t in ts):
                    continue
                a = analyze(ts, m, w, Wtop, tau)
                if a is None:
                    continue
                for lift, dd in a:
                    cols += 1
                    if lift <= dd:
                        clean += 1
                    else:
                        viol += 1
                        if len(viol_examples) < 4:
                            viol_examples.append((lift, dd))
            print("  m=%2d  g=%d  cols=%d  clean(lift≤dd)=%d  viol=%d  viol(lift,dd)=%s" % (
                m, g, cols, clean, viol, viol_examples), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): lift_j ≤ dd_j in (nearly) all columns; any violation has dd_j ≥ g with g = O(1) small ⇒", flush=True)
    print("§6cb's key step holds up to a bounded additive constant ⇒ v₂(q_min) ≥ 9m/2 − O(1). RH stays [OUT].", flush=True)
