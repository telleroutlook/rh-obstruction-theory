#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6bv — STRUCTURE of the two tied terms, to write the FACT B depth-bound PROOF.

§6bu isolated FACT B to: at m≡2 mod4 exactly TWO terms of C_j = v₂(Σ_r (−1)^r w'_{m−1−r} e_r(y_{≠j})) tie for
the ultrametric minimum, and their sum cancels to a fixed small depth (1–2) ≤ A.  To PROVE the bound we need
the two tied term-indices r₁,r₂ and the leading 2-adic units u₁,u₂ of the two terms (term_r / 2^V mod small
2-powers); depth = v₂(u₁ + u₂).  This probe prints, at the adversary's-best tie column (one orbit, m≡2 mod4):
  • the full (r, index i=m−1−r, v₂(w'_i), v₂(e_r), v₂(term_r)) table,
  • the two tied r's and their post-strip odd units u = term_r / 2^V (as integers mod 32),
  • u₁+u₂ mod 32 and its v₂ = depth,
so the cancellation is explicit.  If r₂ = r₁+1 (adjacent) and u₁ ≡ −u₂ mod 2 but ≢ mod 4/8, the depth bound
is a 2-line statement about consecutive Newton sums e_r,e_{r+1} and the FACT-A profile step.  Exact (L9).
Adversary one-sided.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, per_column
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac, elem_sym
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def odd_part_mod(fr, mod):
    """Return (v2, odd-part-as-int mod `mod`) of a nonzero Fraction fr (fr must be a 2-adic integer here)."""
    v = vp_frac(fr, 2)
    u = fr / Fr(2) ** v          # 2-adic unit (Fraction, odd num & odd den)
    num, den = u.numerator, u.denominator
    return v, (num * pow(den, -1, mod)) % mod


def col_table(xs, w, j, m):
    Xp = [xs[k] for k in range(m) if k != j]
    e = elem_sym(Xp)
    rows = []
    for i in range(m):
        r = m - 1 - i
        coeff = Fr(e[m - 1 - i] * w[i])   # term for exponent-index i; e index m-1-i = r
        if coeff == 0:
            continue
        vw = vp_frac(Fr(w[i]), 2)
        ve = vp_frac(Fr(e[m - 1 - i]), 2) if e[m - 1 - i] != 0 else None
        rows.append((vp_frac(coeff, 2), i, m - 1 - i, vw, ve, coeff))
    return rows


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
    print("=" * 100, flush=True)
    print("§6bv: structure of the two tied terms at m≡2 mod4 (to write the depth-bound proof).", flush=True)
    print("=" * 100, flush=True)

    for sig, tau in [(Fr(2, 3), Fr(1)), (Fr(4, 5), Fr(1))]:
        p, q, n = rho_pqn(sig, tau)
        rng = random.Random(20260822)
        print("\norbit (%s,%s) n=%d:" % (sig, tau, n), flush=True)
        for m in (6, 10):
            w = wvec(m, sig, tau)
            hi, bts = adv_best(m, w, rng, 40, 10, pool=max(120, 12 * m))
            pc = per_column(bts, m, w)
            jstar = min(range(m), key=lambda j: pc[1][j])
            rows = col_table([x_of(t) for t in bts], w, jstar, m)
            rows.sort()
            V = rows[0][0]
            tied = [rr for rr in rows if rr[0] == V]
            print("  m=%d  V=%d  #tied=%d" % (m, V, len(tied)), flush=True)
            print("    (v₂term, i, r=m-1-i, v₂w'_i, v₂e_r):", flush=True)
            for vt, i, r, vw, ve, _ in rows[:6]:
                print("      %s   i=%d r=%d  v₂w'=%s v₂e=%s" % (vt, i, r, vw, ve), flush=True)
            if len(tied) == 2:
                (_, i1, r1, _, _, c1), (_, i2, r2, _, _, c2) = tied
                v1, u1 = odd_part_mod(c1, 32)
                v2, u2 = odd_part_mod(c2, 32)
                s = c1 + c2
                dv = vp_frac(s, 2) - V if s != 0 else 10 ** 9
                print("    TIED r=(%d,%d) [adjacent=%s]  u₁≡%d u₂≡%d (mod32)  u₁+u₂≡%d  depth=%s" % (
                    r1, r2, abs(r1 - r2) == 1, u1, u2, (u1 + u2) % 32, dv), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if tied r are ADJACENT and u₁+u₂ has small fixed v₂, the depth bound is a 2-line", flush=True)
    print("statement on consecutive Newton sums e_r,e_{r+1} + the FACT-A profile step. RH stays [OUT].", flush=True)
