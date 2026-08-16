#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bt — DECIDE the sole remaining Row 2 (n odd) gap: is the m≡2 mod4 tie correction O(1) UNIFORM in m?

§6bs found C_j(m) = ⌊−3m/2⌋ + period4(m), PINNED (node-independent) at every m EXCEPT m≡2 mod4, where the
ultrametric minimum TIES (uniq-min gap=0) and the correction jumped (+3 for (2/3); +4→+5 for (4/5) across
m=6→10; (6/7) even lost pinning C_j∈[−4,0] at m=6).  The floor is 1+3(m−1) − max_node(min_j C_j); it stays
LINEAR ⟺ the tie's max-over-nodes correction is o(m).  FACT A says the profile's m≡2 spike is A=2v₂(a²−b²)−1,
a FIXED per-orbit constant — so the correction SHOULD be O(1).  But §6bs's +4→+5 leaves it empirical.

THIS PROBE isolates the tie: for each n-odd orbit, push m through {6,10,14,18,22} (all ≡2 mod4) and report
  corr(m) = hi − ⌊−3m/2⌋,  hi := max over node sets of (min_j C_j)  [the adversary's best; caps the floor].
If corr(m) is BOUNDED (flat / period settles) as m grows, Row 2's floor slope is uniformly (9/2) and OP1
closes for every n-odd orbit modulo a single O(1) no-cancellation constant.  If corr grows, the slope
degrades (still ω(log m) as long as corr=o(m), but the clean (9/2) claim weakens).

Uses the CHEAP per_column C_j (bilinear pairing, no dets) so the adversary can reach m=22.  Adversary is
one-sided per direction (hi = UPPER bound on true max, so corr reported is a LOWER bound on the true worst
correction → conservative for the "bounded" reading; a genuinely bounded hi is strong evidence).  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac, elem_sym
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def term_vals(xs, w, j, m):
    Xp = [xs[k] for k in range(m) if k != j]
    e = elem_sym(Xp)
    terms = []
    for i in range(m):
        coeff = e[m - 1 - i] * w[i]
        if coeff != 0:
            terms.append((vp_frac(Fr(coeff), 2), i))
    terms.sort()
    return terms


def adv_hi(m, w, rng, restarts, rounds, pool):
    """max over node sets of (min_j C_j) — the adversary's best (caps the floor from below)."""
    best = None
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
        if best is None or cur > best:
            best = cur
    return best, ts


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6bt: m≡2 mod4 tie correction growth — is max_node(min_j C_j) − ⌊−3m/2⌋ bounded in m?", flush=True)
    print("=" * 104, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1)), (Fr(2, 5), Fr(1))]
    MS = [6, 10, 14, 18, 22]
    rng = random.Random(20260820)

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("\norbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        for m in MS:
            w = wvec(m, sig, tau)
            # scale search effort down as m grows to stay in budget
            restarts = 40 if m <= 10 else (24 if m <= 18 else 16)
            rounds = 10 if m <= 14 else 8
            hi, tsbest = adv_hi(m, w, rng, restarts, rounds, pool=max(120, 12 * m))
            floor_lp = (-3 * m) // 2
            corr = hi - floor_lp if hi is not None else None
            # tie structure at the adversary's best node set
            gap = None
            if hi is not None:
                pc = per_column(tsbest, m, w)
                jstar = min(range(m), key=lambda j: pc[1][j])
                tv = term_vals([x_of(t) for t in tsbest], w, jstar, m)
                gap = (tv[1][0] - tv[0][0]) if len(tv) >= 2 else None
            fl = 1 + 3 * (m - 1) - hi if hi is not None else None
            print("  m=%2d: hi(max_node min_j C_j)=%s  ⌊−3m/2⌋=%d  corr=%s  uniq-gap=%s  floor=%s (~9m/2=%.1f)" % (
                m, hi, floor_lp, corr, gap, fl, 4.5 * m), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("READING (L5): corr(m) BOUNDED as m grows ⇒ Row 2 floor slope uniformly (9/2), OP1 closes for every", flush=True)
    print("n-odd orbit modulo one O(1) no-cancellation constant. corr growing ⇒ slope degrades (still ω(log m)", flush=True)
    print("if o(m)). Adversary one-sided (hi is UPPER bound ⇒ corr is a conservative LOWER bound). RH [OUT].", flush=True)
