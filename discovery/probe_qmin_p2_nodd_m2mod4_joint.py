#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cb — CLOSE m ≡ 2 mod 4: the "lift is paid for by excess clustering" joint inequality (candidate proof).

At m ≡ 2 mod 4 the top two profile entries tie (v₂(w_{m−1}) = v₂(w_{m−2}) = W_top = 2 − 3m/2), so the pairing
S_j = w_{m−1} − w_{m−2}·σ_j + (higher) can 2-adically CANCEL; define per column
      lift_j  := C_j − W_top      (cancellation depth of the top-two tie, ≥ 0; §6bw showed a SINGLE lift can be
                                    large, but the FLOOR needs min_j),
      excess_j := N_j − 3(m−1)     (extra 2-adic clustering of column j beyond the unconditional base; ≥ 0).
The §6bf identity gives  v₂(q_min) = 1 + max_j(N_j − C_j) = 9m/2 − 4 − min_j(lift_j − excess_j),  so the floor
is LINEAR iff  Q := max over collisions of  min_j(lift_j − excess_j)  is BOUNDED.

CANDIDATE PROOF (to be validated here): lift_j is governed by σ_j = Σ_{k≠j} x_k = T − x_j (T = total node sum;
§6bv: depth = v₂(τ − σ_j), τ = w_{m−1}/w_{m−2}).  If min_j lift_j ≥ L then σ_j ≡ τ (mod 2^L) for EVERY j, so
σ_j − σ_{j'} = x_{j'} − x_j ≡ 0 (mod 2^L) ⇒ v₂(x_j − x_{j'}) ≥ L for ALL pairs ⇒ N_j ≥ (m−1)L ⇒ excess_j ≥
(m−1)(L−3).  Hence for the smallest-lift column, min_j(lift − excess) ≤ L − (m−1)(L−3) = 3(m−1) − (m−2)L ≤ 3
for L ≥ 3 (and ≤ L ≤ 2 for L < 3).  So Q ≤ 3 and v₂(q_min) ≥ 9m/2 − 7 — LINEAR, closing Row 2.

THIS PROBE (EXACT, L9), n-odd orbits × m ∈ {6,10,14} (m≡2 mod4):
  (A) adversary MAXIMIZING min_j(lift_j − excess_j) (= minimizing the floor); report the max achieved Q and the
      implied floor 9m/2 − 4 − Q. Prediction: Q ≤ 3 (bounded), floor ≥ 9m/2 − 7.
  (B) MECHANISM check: at the adversary's best collision, print min_j lift_j =: L and min pairwise v₂(x_j−x_k);
      the candidate proof predicts min-pairwise-v₂ ≥ L (deep lift forces clustering).
DECISION (L5): Q bounded (≤ ~3) AND min-pairwise-v₂ ≥ min-lift ⇒ the joint inequality holds ⇒ m≡2 mod4 floor is
LINEAR, Row 2 closes in full. If Q grows with m ⇒ the joint bound fails and the core stands. Hill-climb
one-sided (LOWER bound on the true adversarial Q ⇒ if it already stays ≤3 that is strong; growth would refute).
RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac, vp_int
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def decompose(ts, m, w, Wtop):
    """Return per-column (lift_j, excess_j) and the min pairwise v₂(x_j−x_k), or None."""
    pc = per_column(ts, m, w)
    if pc is None:
        return None
    Ns, Cs = pc
    lifts = [Cs[j] - Wtop for j in range(m)]
    excess = [Ns[j] - 3 * (m - 1) for j in range(m)]
    xs = [x_of(t) for t in ts]
    minpair = min(vp_frac(xs[a] - xs[b], 2) for a in range(m) for b in range(a + 1, m))
    return lifts, excess, minpair


def adv_maximize_minLE(m, w, Wtop, rng, restarts, rounds, pool):
    """Maximize min_j(lift_j − excess_j) (= minimize floor). Return (bestQ, best_ts)."""
    best, bts = -(10 ** 9), None
    for _ in range(restarts):
        ts = rng.sample(range(1, pool), m)
        d = decompose(ts, m, w, Wtop)
        if d is None:
            continue
        cur = min(d[0][j] - d[1][j] for j in range(m))
        for _rnd in range(rounds):
            improved = False
            for i in range(m):
                for _ in range(10):
                    cand = ts[:]
                    cand[i] = rng.randrange(1, pool)
                    if len(set(cand)) != m:
                        continue
                    d2 = decompose(cand, m, w, Wtop)
                    if d2 is None:
                        continue
                    v = min(d2[0][j] - d2[1][j] for j in range(m))
                    if v > cur:
                        ts, cur, improved = cand, v, True
            if not improved:
                break
        if cur > best:
            best, bts = cur, ts[:]
    return best, bts


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6cb: close m≡2 mod4 — is Q = max min_j(lift_j − excess_j) bounded (≤~3)? ⇒ floor ≥ 9m/2 − 7. RH [OUT].", flush=True)
    print("=" * 104, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1))]
    MS = [6, 10, 14]
    rng = random.Random(20260828)

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("\norbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        print("  %3s | %4s | %8s | %10s | %8s | %6s | %10s" % (
            "m", "Q", "floor>=", "9m/2-7", "minlift", "minpr", "mech ok?"), flush=True)
        print("  " + "-" * 66, flush=True)
        for m in MS:
            w = wvec(m, sig, tau)
            Wtop = vp_frac(Fr(w[m - 1]), 2)
            restarts = 60 if m <= 10 else 40
            rounds = 12 if m <= 10 else 9
            pool = max(200, 14 * m)
            Q, bts = adv_maximize_minLE(m, w, Wtop, rng, restarts, rounds, pool)
            lifts, excess, minpair = decompose(bts, m, w, Wtop)
            minlift = min(lifts)
            floor = 9 * m // 2 - 4 - Q
            # mechanism: deep min-lift should force min-pairwise-v₂ >= min-lift
            mech = (minpair >= minlift)
            print("  %3d | %4d | %10d | %10d | %8d | %6d | %10s" % (
                m, Q, floor, 9 * m // 2 - 7, minlift, minpair, "OK" if mech else "CHECK"), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("READING (L5): Q bounded ≤~3 across m ⇒ v₂(q_min) ≥ 9m/2 − 7 LINEAR at m≡2 mod4 ⇒ Row 2 closes in full", flush=True)
    print("(min-lift forces min-pairwise-v₂, i.e. deep cancellation requires clustering that overwhelms the lift", flush=True)
    print("by factor m−2). If Q grows with m the joint bound fails. Hill-climb one-sided. RH stays [OUT].", flush=True)
