#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

STRESS-TEST THE C_j = O(1) LEMMA (§6ap) — the SOLE remaining gap in the §6ao p=3 proof skeleton.

§6ao reduced OP1 (via the p=3 floor v_3(q_min) >= m/2 - O(1)) to ONE lemma:
    (LEMMA C)  max_j C_j <= B  for an absolute constant B, where
               C_j = v_3(minor_j) - sum_{k<l, k,l != j} v_3(x_k - x_l)
                   = (3-adic closeness of the FIXED off-line orbit to the node cluster minus node j).
Crucially C_j uses ONLY minor determinants + node x-differences -- NOT qmin_fast's slow SNF -- so it can be
pushed to LARGER m cheaply.  This probe:
  (a) ADVERSARIALLY MAXIMIZES max_j C_j (coordinate ascent) over m=4..14 -- the off-line orbit trying hard
      to 3-adically shadow the cluster -- and reports the largest max_j C_j found.  If it stays bounded by a
      small constant as m grows, LEMMA C is strongly supported (=> OP1 proof essentially closed for D=425).
  (b) computes the off-line atoms' x-values and their 3-adic distances v_3(xi_atom - x_k) to explain WHY C_j
      is bounded (the atoms' x-values should be 3-adically SEPARATED from the rational node classes).
Exact integer/rational arithmetic (L9).  Honest (L5): ascent gives a LOWER bound on the true max C_j; if it
plateaus at a constant across m that is strong evidence, not proof.  One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows

SIG, TAU = Fr(3, 4), Fr(1)          # D=425 = 5^2 * 17
P = 3


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def vp_int(n, p):
    v = 0
    while n and n % p == 0:
        n //= p; v += 1
    return v


def vp_frac(fr, p):
    if fr == 0:
        return 10**9
    return vp_int(fr.numerator, p) - vp_int(fr.denominator, p)


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


def maxCj(ts, m):
    """max_j C_j = max_j [ v_3(minor_j) - sum_{k<l,k,l!=j} v_3(x_k - x_l) ].  Uses only minor dets."""
    b = build(ts, m)
    if not b:
        return None
    oc, vo = b
    xs = [x_of(t) for t in ts]
    # precompute pair valuations
    pv = [[0] * m for _ in range(m)]
    for a in range(m):
        for c in range(a + 1, m):
            pv[a][c] = pv[c][a] = vp_frac(xs[a] - xs[c], P)
    best = None
    for j in range(m):
        cols = [list(oc[k]) for k in range(m)]
        cols[j] = list(vo)
        dj = int_det(cols_to_rows(cols, m))
        if dj == 0:
            continue
        vmin = vp_int(dj, P)
        VD_j = sum(pv[a][c] for a in range(m) for c in range(a + 1, m) if a != j and c != j)
        Cj = vmin - VD_j
        best = Cj if best is None else max(best, Cj)
    return best


def ascent_maxC(ts, m, rng, rounds=15):
    best_ts = ts[:]
    best = maxCj(best_ts, m)
    best = best if best is not None else -10**9
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(8):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 400)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                v = maxCj(cand, m)
                if v is not None and v > best:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts, best


if __name__ == "__main__":
    print("=" * 92, flush=True)
    print("STRESS-TEST LEMMA C (§6ap): adversarially MAXIMIZE max_j C_j. If it stays bounded as m grows,", flush=True)
    print("the off-line orbit cannot 3-adically shadow the cluster => p=3 proof skeleton closes for D=425.", flush=True)
    print("=" * 92, flush=True)
    # (b) off-line atom x-values and their 3-adic separation from a few rational nodes
    print("\n(b) off-line atoms x-value 3-adic behavior (why C_j is bounded):", flush=True)
    atoms = [(SIG, TAU), (SIG, -TAU), (1 - SIG, TAU), (1 - SIG, -TAU)]
    # atom 'x' analog: x=(4 z^2 -1)/(4 z^2 +1) with z^2 = re^2 - im^2 + 2 i re im -> use real proxy re^2-im^2
    for (re, im) in atoms[:2]:
        z2 = re * re - im * im           # real part proxy of z^2 for the atom
        xa = (4 * z2 - 1) / (4 * z2 + 1)
        seps = [vp_frac(xa - x_of(t), P) for t in (1, 2, 3, 6, 9)]
        print(f"    atom(re={re},im={im}): x_re-proxy={xa}, v_3(x_atom - x_t) for t=1,2,3,6,9 -> {seps}",
              flush=True)
    print(f"\n{'m':>3} | {'max_j C_j (adversarial ascent, best of restarts)':>48} | {'m/2 floor target':>16}",
          flush=True)
    print("-" * 74, flush=True)
    rng = random.Random(20260816)
    for m in range(4, 15):
        NR = 12 if m <= 10 else 6
        overall = None
        for _ in range(NR):
            s0 = rng.sample(range(1, 400), m)
            if not build(s0, m):
                continue
            _, v = ascent_maxC(s0, m, rng)
            if v is not None and (overall is None or v > overall):
                overall = v
        print(f"{m:>3} | {str(overall):>48} | {m // 2:>16}", flush=True)
    print("\n" + "=" * 92, flush=True)
    print("READING (L5): if 'max_j C_j' plateaus at a small constant (no growth) across m=4..14 while the", flush=True)
    print("m/2 floor target grows, LEMMA C (max_j C_j = O(1)) holds empirically and the p=3 floor v_3(q_min)", flush=True)
    print(">= m/2 - O(1) is essentially proved for D=425 => OP1 TRUE. If max_j C_j GROWS with m, the off-line", flush=True)
    print("orbit CAN shadow the cluster and the residual bound needs the finer argument -- report honestly.", flush=True)
    print("Ascent gives a LOWER bound on the true max. One orbit (D=425). Evidence, not proof. RH [OUT].", flush=True)
