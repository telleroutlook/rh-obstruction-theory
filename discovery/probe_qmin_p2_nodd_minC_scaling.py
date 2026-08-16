#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6by — SCALE the Row 2 open core (CORE-2) and test the "leading-term-dominated column" proof route.

The §6bf reduction is EXACT:  v₂(q_min) = max_j(1 + N_j − C_j),  N_j ≥ 3(m−1) UNCONDITIONAL, hence
      v₂(q_min) ≥ 1 + 3(m−1) − min_j C_j^(2).
So the floor is LINEAR provided  min_j C_j = o(m)  — and there is HUGE SLACK: any bound min_j C_j ≤ (3−c)m
with c>0 already yields a positive-linear floor.  We do NOT need the tight §6bu ceiling (≤2).

NEW structural lever (from §6bv): the off-line pairing splits as
      S_j = Σ_i (−1)^{m−1−i} e_{m−1−i}(X'_j) w_i  =  w_{m−1}  +  [node-dependent lower terms],
because the i=m−1 term is e_0·w_{m−1}=w_{m−1}, NODE-INDEPENDENT and SHARED by every column j.  Therefore if
at least ONE column is "leading-dominated" (its lower terms do not 2-adically cancel w_{m−1}, so C_j =
v₂(w_{m−1})), then  min_j C_j ≤ v₂(w_{m−1}) =: W_top(m),  and the floor is linear PROVIDED W_top(m)=o(m).

THIS PROBE (EXACT, L9), n-odd orbits × m up to 16:
  (a) W_top(m) = v₂(w_{m−1})  — a pure orbit constant (no adversary). Bounded, or linear-with-small-slope?
  (b) adversarial max of min_j C_j (strong hill-climb, one-sided lower bound on the true adversarial max);
  (c) at the adversary's best collision, #columns that are leading-dominated (C_j == W_top) — is it ≥1 always?
  (d) proven floor 1+3(m−1)−minC  vs the 3(m−1) baseline, and ratio minC/m → does it →0?
DECISION (L5): if (a) W_top=o(m) AND (c) ≥1 leading-dominated column ALWAYS ⇒ CORE-2 reduces to the clean
lemma "some column's lower terms fail to cancel w_{m−1}", a much weaker (slack-rich) statement than §6bu.
If min_j C_j creeps toward 3m or no column is leading-dominated ⇒ the joint minimax core stands. RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column
from discovery.probe_qmin_Cj_bilinear import vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def adv_max_minC_with_ts(m, w, rng, restarts, rounds, pool):
    """Maximize min_j C_j (= minimize the floor). Return (best_minC, best_ts)."""
    best, bts = -(10 ** 9), None
    for _ in range(restarts):
        ts = rng.sample(range(1, pool), m)
        pc = per_column(ts, m, w)
        if pc is None:
            continue
        cur = min(pc[1])
        for _rnd in range(rounds):
            improved = False
            for i in range(m):
                for _ in range(10):
                    cand = ts[:]
                    cand[i] = rng.randrange(1, pool)
                    if len(set(cand)) != m:
                        continue
                    pc2 = per_column(cand, m, w)
                    if pc2 is None:
                        continue
                    v = min(pc2[1])
                    if v > cur:
                        ts, cur, improved = cand, v, True
            if not improved:
                break
        if cur > best:
            best, bts = cur, ts[:]
    return best, bts


if __name__ == "__main__":
    print("=" * 108, flush=True)
    print("§6by: scale CORE-2 (max min_j C_j) and test the leading-term-dominated-column route. RH [OUT].", flush=True)
    print("Floor identity: v₂(q_min) ≥ 1 + 3(m−1) − min_j C_j.  Slack: any min_j C_j ≤ (3−c)m ⇒ linear floor.", flush=True)
    print("=" * 108, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1))]
    MS = [4, 6, 8, 10, 12, 14, 16]
    rng = random.Random(20260825)

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("\norbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        print("  %3s | %7s | %7s | %6s | %10s | %8s | %8s" % (
            "m", "W_top", "maxminC", "#lead", "floor>=", "3(m-1)", "minC/m"), flush=True)
        print("  " + "-" * 74, flush=True)
        for m in MS:
            w = wvec(m, sig, tau)
            W_top = vp_frac(Fr(w[m - 1]), 2)
            restarts = 40 if m <= 10 else (28 if m <= 14 else 20)
            rounds = 10 if m <= 12 else 8
            pool = max(200, 14 * m)
            best, bts = adv_max_minC_with_ts(m, w, rng, restarts, rounds, pool)
            pc = per_column(bts, m, w)
            nlead = sum(1 for c in pc[1] if c == W_top)
            floor = 1 + 3 * (m - 1) - best
            print("  %3d | %7d | %7d | %6d | %10d | %8d | %8.3f" % (
                m, W_top, best, nlead, floor, 3 * (m - 1), best / m), flush=True)

    print("\n" + "=" * 108, flush=True)
    print("READING (L5): W_top=o(m) AND #lead>=1 always ⇒ min_j C_j ≤ W_top ⇒ CORE-2 closes via a slack-rich", flush=True)
    print("'≥1 non-cancelling column' lemma (much weaker than §6bu's tight ≤2). If maxminC ~ 3m or #lead can hit", flush=True)
    print("0, the joint minimax core stands. Hill-climb one-sided (lower bound on the true adversarial max). RH [OUT].", flush=True)
