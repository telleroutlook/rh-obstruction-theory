#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bu — ISOLATE the FACT B no-cancellation quantity: the m≡2 mod4 tie's cancellation DEPTH.

Row 2's floor is (9/2)m − O(1); the O(1) tie-correction was confirmed BOUNDED in m (§6bt).  The SOLE remaining
rigorous step is FACT B: at m≡2 mod4 the ultrametric minimum of C_j = v_2(Σ_r (−1)^r w'_{m−1−r} e_r(y_{≠j}))
(y_k=x_k−1, v_2(y_k)=1) TIES between the two smallest-valuation terms term_{r1},term_{r2}.  A tie is dangerous
only if the two terms CANCEL: v_2(term_{r1}+term_{r2}) can exceed the tie value V=v_2(term_{r1})=v_2(term_{r2}).

THE CRUX QUANTITY (what FACT B must bound):
    depth := v_2(term_{r1}+term_{r2}) − V   ( = v_2(1 + term_{r2}/term_{r1}), a 2-adic-unit-ratio quantity ).
C_j exceeds the naive tie value V by exactly `depth` when the two tied terms are the argmin.  FACT B ⟺ depth is
bounded by a per-orbit constant (predicted A = 2·v₂(a²−b²)−1, FACT A's period-4 spike) uniformly in m and node.

THIS PROBE (EXACT, L9): for n-odd orbits, m∈{6,10,14,18,22} (≡2 mod4), at the adversary's best node set AND
random valid sets, (i) find the two smallest-valuation terms, confirm they TIE (V1==V2), (ii) compute the
cancellation depth of their sum, (iii) compute the FULL C_j and check C_j == V + depth at the tie column,
(iv) compare depth to A = 2·v₂(a²−b²)−1.  If depth ≤ A uniformly, FACT B's constant is pinned and the lemma
statement is: "the ratio of the two tied terms is ≢ −1 mod 2^{A+1}".  Adversary one-sided.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_orbit_trichotomy import orbit_beta, v2int
from discovery.probe_qmin_p2_floor_identity import wvec, per_column
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac, elem_sym
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn, beta_gauss_numer


def col_terms(xs, w, j, m):
    """Return the additive terms (as exact Fractions) of the C_j pairing for column j, plus their v_2 list."""
    Xp = [xs[k] for k in range(m) if k != j]
    e = elem_sym(Xp)
    terms = []
    for i in range(m):
        coeff = Fr(e[m - 1 - i] * w[i])
        if coeff != 0:
            terms.append((vp_frac(coeff, 2), coeff, i))
    return terms


def analyze_col(xs, w, j, m):
    """At column j: identify the two lowest-valuation terms, whether they tie, the cancellation depth of the
    tied group's sum, and the full C_j."""
    terms = col_terms(xs, w, j, m)
    if len(terms) < 2:
        return None
    terms.sort(key=lambda t: t[0])
    V = terms[0][0]
    tied = [t for t in terms if t[0] == V]
    total = sum(t[1] for t in terms)
    Cj = vp_frac(total, 2)
    tie_sum = sum(t[1] for t in tied)
    depth = (vp_frac(tie_sum, 2) - V) if tie_sum != 0 else 10 ** 9
    return dict(V=V, ntied=len(tied), Cj=Cj, depth=depth, gap=(terms[1][0] - terms[0][0]))


def adv_best(m, w, rng, restarts, rounds, pool):
    best, bts = None, None
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
            best, bts = cur, ts[:]
    return best, bts


if __name__ == "__main__":
    print("=" * 104, flush=True)
    print("§6bu: the m≡2 mod4 tie CANCELLATION DEPTH — the exact quantity FACT B must bound.", flush=True)
    print("=" * 104, flush=True)

    ORBITS = [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1)), (Fr(6, 7), Fr(1)), (Fr(2, 5), Fr(1)), (Fr(3, 5), Fr(1))]
    MS = [6, 10, 14, 18, 22]
    rng = random.Random(20260821)

    for sig, tau in ORBITS:
        p, q, n = rho_pqn(sig, tau)
        _, _, beta, _, _, _, _ = orbit_beta(sig, tau, M=8)
        gre, gim, _ = beta_gauss_numer(beta)
        A_spike = 2 * v2int(gre * gre - gim * gim) - 1     # FACT A period-4 spike for j≡2 mod4
        print("\norbit (%s,%s) n=%d  γ=%d%+di  A=2v₂(a²−b²)−1=%d:" % (sig, tau, n, gre, gim, A_spike), flush=True)
        for m in MS:
            w = wvec(m, sig, tau)
            restarts = 40 if m <= 10 else (24 if m <= 18 else 16)
            rounds = 10 if m <= 14 else 8
            hi, bts = adv_best(m, w, rng, restarts, rounds, pool=max(120, 12 * m))
            if bts is None:
                print("  m=%2d: no valid set found" % m, flush=True)
                continue
            pc = per_column(bts, m, w)
            jstar = min(range(m), key=lambda j: pc[1][j])
            info = analyze_col([x_of(t) for t in bts], w, jstar, m)
            # also scan a few random valid sets for the max depth seen
            maxdepth = info["depth"]
            for _ in range(200):
                ts = rng.sample(range(1, max(90, 8 * m)), m)
                pc2 = per_column(ts, m, w)
                if pc2 is None:
                    continue
                jj = min(range(m), key=lambda j: pc2[1][j])
                inf2 = analyze_col([x_of(t) for t in ts], w, jj, m)
                if inf2 and inf2["gap"] == 0 and inf2["depth"] < 10 ** 8:
                    maxdepth = max(maxdepth, inf2["depth"])
            tie = "TIE(n=%d)" % info["ntied"] if info["gap"] == 0 else "gap=%d" % info["gap"]
            print("  m=%2d: adv %s V=%d depth=%s C_j=%d ; max depth over random ties=%s  (A=%d)" % (
                m, tie, info["V"], info["depth"], info["Cj"], maxdepth, A_spike), flush=True)

    print("\n" + "=" * 104, flush=True)
    print("READING (L5): depth ≤ A = 2v₂(a²−b²)−1 uniformly ⇒ FACT B lemma = 'the two tied top terms have ratio", flush=True)
    print("≢ −1 mod 2^{A+1}', a single-residue-class no-cancellation bound with the constant PINNED by FACT A.", flush=True)
    print("Adversary one-sided (max depth is a LOWER bound on the worst). RH stays [OUT].", flush=True)
