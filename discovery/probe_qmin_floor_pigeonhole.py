#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

PIGEONHOLE ROUTE to lemma (4'') (§6ba) — can the adversary explode C on ALL high-N columns at once?

Lemma (4'') [§6az]: EXISTS a column j with N_j >= m/2 - O(1) AND C_j = O(1).  Proof idea: exploding column j
(C_j large) requires the excluded set X' = {x_k}_{k!=j} to admit a 3-adic ALIGNMENT (some node ≈ a/b, the
target set by the OTHERS of X').  A single specially-aligned node satisfies the target of only ONE column's
complement, so it should explode O(1) columns; to explode K columns needs ~K aligned nodes.  If the number of
simultaneously EXPLODABLE columns K_expl is < the number of HIGH-N columns, a high-N column with small C must
survive (pigeonhole), proving (4'').  This probe MEASURES, adversarially (L5 one-sided = LOWER bound on the
achievable count):
  (A) K_expl(thr) := max over node sets of #{ j : C_j >= thr },  for thr = 2, 3, 5 -- how many columns can be
      exploded AT ONCE?  If K_expl stays SMALL (O(1)) or well below m, pigeonhole is viable.
  (B) the CRITICAL overlap: max over node sets of #{ j : N_j >= m/2 - 2 AND C_j >= 2 } vs #{ j : N_j >= m/2-2 }
      -- can EVERY high-N column be simultaneously exploded?  Report whether a high-N, C<=1 column ALWAYS
      remains (survivor := #{j: N_j>=m/2-2 and C_j<=1} >= 1 for every sampled set).
Exact (L9).  Honest (L5): ascent is a LOWER bound on the explodable count; if survivor ever hits 0, (4'')'s
pigeonhole route is in danger (report plainly).  One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_Cj_bilinear import Bmatrix, solve_lower, vp_frac, x_of
from discovery.probe_qmin_Cj_lift_attack import (
    node_poly_coeffs, S_of_nodes, frac_mod, is_3adic_square, hensel_sqrt_unit,
)
import discovery.probe_overdetermined_collision as PO

TAU = Fr(1)
P = 3


def xs_of(ts):
    return [x_of(t) for t in ts]


def N_of(xs, j):
    return sum(vp_frac(xs[j] - xs[k], P) for k in range(len(xs)) if k != j)


def C_of(xs, j, w):
    Xp = [xs[k] for k in range(len(xs)) if k != j]
    return vp_frac(S_of_nodes(Xp, w), P)


def NC(ts, w):
    m = len(ts); xs = xs_of(ts)
    return [N_of(xs, j) for j in range(m)], [C_of(xs, j, w) for j in range(m)]


def liftable_target(nodes, w, m):
    g = node_poly_coeffs(nodes)                    # m-2 nodes
    b = sum(g[j] * w[j] for j in range(m - 1))
    a = sum(g[j] * w[j + 1] for j in range(m - 1))
    if b == 0 or vp_frac(b, P) != 0:
        return None
    alpha = a / b
    if alpha == 1:
        return None
    R = (1 + alpha) / (4 * (1 - alpha))
    if not is_3adic_square(R) or frac_mod(alpha, 3) not in (0, 2) or vp_frac(R, P) < 0:
        return None
    v = vp_frac(R, P)
    return v // 2, R / (Fr(3) ** v)


def lift_t(pack, c):
    halfv, u = pack
    ru = hensel_sqrt_unit(lambda mod: frac_mod(u, mod), c)
    tf = (ru * (P ** halfv)) % (P ** c)
    return tf if tf != 0 else P ** c


def explode_ascent(m, w, rng, objective, restarts=50, rounds=8):
    """Maximize `objective(Ns,Cs,m)` over node sets via lift-aware coordinate ascent. Returns (best, argmax_ts)."""
    best = -1; best_ts = None
    for _ in range(restarts):
        ts = rng.sample(range(1, 500), m)
        if len(set(xs_of(ts))) != m:
            continue
        for _rnd in range(rounds):
            Ns, Cs = NC(ts, w)
            cur = objective(Ns, Cs, m)
            improved = False
            for i in range(m):
                for vv in range(m):
                    if vv == i:
                        continue
                    others = [xs_of(ts)[k] for k in range(m) if k not in (i, vv)]
                    if len(others) != m - 2:
                        continue
                    pk = liftable_target(others, w, m)
                    cand = ts[:]
                    if pk:
                        tf = lift_t(pk, rng.choice([4, 8, 16]))
                        if tf in ts:
                            continue
                        cand[i] = tf
                    else:
                        cand[i] = rng.randrange(1, 500)
                    if len(set(cand)) != m or len(set(xs_of(cand))) != m:
                        continue
                    Ns2, Cs2 = NC(cand, w)
                    if objective(Ns2, Cs2, m) > cur:
                        ts, cur, improved = cand, objective(Ns2, Cs2, m), True
            if not improved:
                break
        Ns, Cs = NC(ts, w)
        if objective(Ns, Cs, m) > best:
            best = objective(Ns, Cs, m); best_ts = ts[:]
    return best, best_ts


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6ba: PIGEONHOLE route to (4''). How many columns can be exploded at once? Does a high-N,", flush=True)
    print("low-C column always survive?", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)

    print("\n(A) K_expl(thr) = max #{j: C_j >= thr} achievable (adversarial LOWER bound):", flush=True)
    print(f"{'m':>3} | {'K_expl(>=2)':>11} | {'K_expl(>=3)':>11} | {'K_expl(>=5)':>11} | {'m':>3}", flush=True)
    print("-" * 56, flush=True)
    for m in (4, 5, 6, 7, 8):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        k2, _ = explode_ascent(m, w, rng, lambda Ns, Cs, mm: sum(1 for c in Cs if c >= 2))
        k3, _ = explode_ascent(m, w, rng, lambda Ns, Cs, mm: sum(1 for c in Cs if c >= 3))
        k5, _ = explode_ascent(m, w, rng, lambda Ns, Cs, mm: sum(1 for c in Cs if c >= 5))
        print(f"{m:>3} | {k2:>11} | {k3:>11} | {k5:>11} | {m:>3}", flush=True)

    print("\n(B) CRITICAL: can EVERY high-N column be exploded? survivor := #{j: N_j>=m/2-2 and C_j<=1}.", flush=True)
    print("    Adversary MAXIMIZES #{high-N and exploded}; report min survivor over the search (want >= 1):", flush=True)
    print(f"{'m':>3} | {'max #(highN & C>=2)':>19} | {'#highN(typ)':>11} | {'MIN survivor (want>=1)':>22}", flush=True)
    print("-" * 62, flush=True)
    for m in (4, 5, 6, 7, 8):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        thrN = m / 2 - 2

        def obj_overlap(Ns, Cs, mm):
            return sum(1 for j in range(mm) if Ns[j] >= thrN and Cs[j] >= 2)

        best_overlap, best_ts = explode_ascent(m, w, rng, obj_overlap)
        # at the adversary's best overlap config, count survivors + typical #highN
        Ns, Cs = NC(best_ts, w)
        highN = sum(1 for j in range(m) if Ns[j] >= thrN)
        # also scan many configs for the MIN survivor (the dangerous case)
        min_surv = 10**9
        for _ in range(400):
            ts = rng.sample(range(1, 500), m)
            if len(set(xs_of(ts))) != m:
                continue
            # push toward exploding high-N columns a few steps
            for _rnd in range(4):
                Ns2, Cs2 = NC(ts, w)
                cur = obj_overlap(Ns2, Cs2, m)
                for i in range(m):
                    others = [xs_of(ts)[k] for k in range(m) if k not in (i, (i + 1) % m)]
                    if len(others) != m - 2:
                        continue
                    pk = liftable_target(others, w, m)
                    if not pk:
                        continue
                    tf = lift_t(pk, 8)
                    if tf in ts:
                        continue
                    cand = ts[:]; cand[i] = tf
                    if len(set(cand)) != m or len(set(xs_of(cand))) != m:
                        continue
                    Ns3, Cs3 = NC(cand, w)
                    if obj_overlap(Ns3, Cs3, m) > cur:
                        ts, cur = cand, obj_overlap(Ns3, Cs3, m)
            Ns2, Cs2 = NC(ts, w)
            surv = sum(1 for j in range(m) if Ns2[j] >= thrN and Cs2[j] <= 1)
            min_surv = min(min_surv, surv)
        print(f"{m:>3} | {best_overlap:>19} | {highN:>11} | {min_surv:>22}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): in (A), if K_expl stays SMALL/well below m, only a few columns can be exploded at", flush=True)
    print("once -> pigeonhole viable. In (B), if MIN survivor >= 1 for every sampled set, a high-N (N>=m/2-2),", flush=True)
    print("low-C (C<=1) column ALWAYS survives -> lemma (4'') holds by pigeonhole. If survivor hits 0, the", flush=True)
    print("adversary exploded all high-N columns and (4'')'s pigeonhole route is in danger. Ascent = LOWER", flush=True)
    print("bound on explodable count. One orbit (D=425). RH stays [OUT].", flush=True)
