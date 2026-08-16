#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

CHANNEL SPLIT of q_min (§6bd) — is the barrier's log q_min the 3-adic floor alone, or is there an INDEPENDENT
archimedean / other-prime channel?  OP1 holds iff inf_A log q_min = omega(log m).  Channel 1 (proved route,
OB-42) is the p=3 floor: v_3(q_min) >= m/2 - O(1) => log q_min >= (m/2)log 3.  This probe asks whether, under
an adversary MINIMIZING the full integer q_min, log q_min is EXHAUSTED by the 3-adic part or carries a large
residual (other primes + 3-free magnitude) that would be a SECOND, independent lower-bound channel.

q_min = D_m(A) / D_m([A | d])  (exact integer).  For K = m online columns: D_m(A) = |det A|;
D_m([A|d]) = gcd of the (m+1) size-m minors of the m x (m+1) matrix [A | d].  Split:
      log2 q_min  =  v_3(q_min)*log2(3)   +   log2( q_min / 3^{v_3(q_min)} )   [3-free residual].
Report, under adversarial MIN of log2 q_min (D=425 orbit): total log2 q_min, the 3-adic part, the residual,
and the residual's dominant prime.  If residual ~ 0, channel 1 is the whole story (channel 2 redundant); if
residual grows with m, there is an independent archimedean/other-prime barrier worth its own analysis.
Exact (L9).  Honest (L5): adversary = one-sided (UPPER bound on inf q_min).  One orbit.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd, log2
import random

from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.probe_qmin_det_ratio import int_det, cols_to_rows
from discovery.probe_qmin_Cj_bilinear import x_of, vp_int
from discovery.probe_qmin_Cj_lift_attack import (
    node_poly_coeffs, frac_mod, is_3adic_square, hensel_sqrt_unit,
)
from discovery.probe_qmin_Cj_bilinear import Bmatrix, solve_lower, vp_frac
import discovery.probe_overdetermined_collision as PO

SIG, TAU = Fr(3, 4), Fr(1)
P = 3


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def qmin_exact(ts, m):
    """q_min = |det A| / gcd(size-m minors of [A|d]). Returns (q_min, detA) or None."""
    b = build(ts, m)
    if not b:
        return None
    oc, vo = b
    detA = int_det(cols_to_rows(oc, m))
    if detA == 0:
        return None
    g = abs(detA)                                   # minor deleting the d-column
    for j in range(m):                              # minor deleting online column j -> replace j by d
        cols = [list(oc[k]) for k in range(m)]
        cols[j] = list(vo)
        g = gcd(g, int_det(cols_to_rows(cols, m)))
    if g == 0:
        return None
    q = abs(detA) // g
    return q, detA


def split(q):
    v3 = vp_int(q, P)
    resid = q // (P ** v3)                            # 3-free part
    # dominant prime of residual
    dom, n = 1, resid
    d = 2
    best_p, best_e = 1, 0
    while d * d <= n:
        e = 0
        while n % d == 0:
            n //= d; e += 1
        if e > best_e:
            best_p, best_e = d, e
        d += 1 if d == 2 else 2
    if n > 1 and 1 > best_e:
        best_p = n
    return v3, resid, best_p


def liftable_target(nodes, w, m):
    g = node_poly_coeffs(nodes)
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


def adversarial_min_q(m, w, rng, restarts=18, rounds=6):
    best = None
    for _ in range(restarts):
        ts = rng.sample(range(1, 300), m)
        r0 = qmin_exact(ts, m)
        if r0 is None:
            continue
        cur_ts, cur_q = ts, r0[0]
        for _rnd in range(rounds):
            improved = False
            xs = [x_of(t) for t in cur_ts]
            for i in range(m):
                for vv in range(m):
                    if vv == i:
                        continue
                    others = [xs[k] for k in range(m) if k not in (i, vv)]
                    if len(others) != m - 2:
                        continue
                    pk = liftable_target(others, w, m)
                    cand = cur_ts[:]
                    if pk:
                        tf = lift_t(pk, rng.choice([4, 8, 16]))
                        if tf in cur_ts:
                            continue
                        cand[i] = tf
                    else:
                        cand[i] = rng.randrange(1, 300)
                    rr = qmin_exact(cand, m)
                    if rr is not None and rr[0] < cur_q:
                        cur_ts, cur_q, improved = cand, rr[0], True
                        xs = [x_of(t) for t in cur_ts]
            if not improved:
                break
        if best is None or cur_q < best:
            best = cur_q
    return best


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bd: CHANNEL SPLIT of q_min under adversarial minimization (D=425). Is log q_min just the 3-adic", flush=True)
    print("floor, or is there an independent archimedean/other-prime residual?", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)
    print(f"\n{'m':>3} | {'min q_min (adv)':>15} | {'log2 q_min':>10} | {'v_3':>4} | {'3-adic log2':>11} | "
          f"{'residual log2':>13} | {'resid dom prime':>15}", flush=True)
    print("-" * 92, flush=True)
    for m in (4, 5, 6, 7):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        q = adversarial_min_q(m, w, rng)
        if q is None:
            print(f"{m:>3} | {'--':>15}", flush=True); continue
        v3, resid, dom = split(q)
        l2 = log2(q) if q > 0 else 0
        l2_3 = v3 * log2(3)
        l2_res = log2(resid) if resid > 0 else 0
        print(f"{m:>3} | {q:>15} | {l2:>10.2f} | {v3:>4} | {l2_3:>11.2f} | {l2_res:>13.2f} | {dom:>15}", flush=True)
    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if 'residual log2' ~ 0 (q_min is essentially a power of 3), channel 1 (the p=3 floor,", flush=True)
    print("OB-42) is the ENTIRE barrier and channel 2 is redundant. If 'residual log2' GROWS with m, there is a", flush=True)
    print("SECOND independent lower-bound channel (other primes / archimedean covolume) worth its own theorem.", flush=True)
    print("Adversary = one-sided UPPER bound on inf q_min. One orbit (D=425). RH stays [OUT].", flush=True)
