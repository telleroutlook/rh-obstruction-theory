#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bs — FACT B closed form: extract the pinned C_j(m) for Row 2 (n odd) as a function of m, and localize the
tie.  §6bp/§6bq showed C_j = min_j C_j is node-INDEPENDENT (two-sided adversary min==max) with sequence
[-5,-7,-6,-10] at m=4..7.  This probe (i) pushes m to 10 with a strong two-sided adversary to fit the
period-4-in-m closed form of C_j(m), (ii) reports, at the minimizing column, the FULL sorted term-valuation
list and the argmin index r*, so the ultrametric-min structure (unique vs tie) is explicit per m mod 4, and
(iii) reports the resulting floor 1+3(m-1)-C_j(m) vs a measured v_2(q_min) sample.

If C_j(m) = round(S*m) + period4(m) with S=-3/2, the floor is provably ~ (3-S)m = (9/2)m, and the only
proof-gap is the m≡2 mod4 ultrametric tie (two equal top terms -> must show no cancellation).  Exact (L9).
Adversary one-sided per direction (L5).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int, vp_frac, elem_sym
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


def adv_minC(m, sig, tau, w, rng, maximize, restarts=28, rounds=10):
    best = None
    for _ in range(restarts):
        ts = rng.sample(range(1, 300), m)
        pc = per_column(ts, m, w)
        if pc is None:
            continue
        cur = min(pc[1])
        for _rnd in range(rounds):
            improved = False
            for i in range(m):
                for _ in range(12):
                    cand = ts[:]
                    cand[i] = rng.randrange(1, 300)
                    if len(set(cand)) != m:
                        continue
                    pc2 = per_column(cand, m, w)
                    if pc2 is None:
                        continue
                    v = min(pc2[1])
                    if (v > cur) if maximize else (v < cur):
                        ts, cur, improved = cand, v, True
            if not improved:
                break
        if best is None or ((cur > best) if maximize else (cur < best)):
            best = cur
    return best


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bs: Row 2 pinned C_j(m) closed form + tie localization (n odd).", flush=True)
    print("=" * 100, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1))]
    rng = random.Random(20260819)

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        print("\norbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        seq = []
        for m in range(4, 11):
            w = wvec(m, sig, tau)
            lo = adv_minC(m, sig, tau, w, rng, maximize=False)
            hi = adv_minC(m, sig, tau, w, rng, maximize=True)
            seq.append(lo if lo == hi else None)
            # term structure at a random minimizing column
            argmin_r, gap = None, None
            for _ in range(60):
                ts = rng.sample(range(1, 90), m)
                pc = per_column(ts, m, w)
                if pc is None:
                    continue
                jstar = min(range(m), key=lambda j: pc[1][j])
                tv = term_vals([x_of(t) for t in ts], w, jstar, m)
                argmin_r = tv[0][1]
                gap = (tv[1][0] - tv[0][0]) if len(tv) >= 2 else None
                break
            fl = 1 + 3 * (m - 1) - lo if lo is not None else None
            print("  m=%2d (m%%4=%d): C_j in[%s,%s] %s  argmin r*=%s uniq-gap=%s  floor 1+3(m-1)-C=%s" % (
                m, m % 4, lo, hi, "PIN" if lo == hi else "!!", argmin_r, gap, fl), flush=True)
        # fit: C_j(m) - floor(S*m), S=-3/2
        print("  C_j(m) m=4..10: %s" % seq, flush=True)
        corr = [seq[i] - (-3 * (i + 4)) // 2 if seq[i] is not None else None for i in range(len(seq))]
        print("  C_j(m) - floor(-3m/2): %s  (period-4-in-m correction)" % corr, flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if C_j(m)=floor(-3m/2)+period4(m) pinned, floor = 1+3(m-1)-C_j(m) ~ (9/2)m is provable", flush=True)
    print("modulo the m=2 mod4 ultrametric tie. Adversary one-sided per direction. RH stays [OUT].", flush=True)
