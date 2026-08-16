#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE FLOOR-CARRIER lemma (§6az) — §6ay killed both simple mechanisms (M1 co-inflation of v_3(detA) doesn't
fire; M2 'argmax-N column has bounded C' is FALSE -- the adversary can explode C there and the floor just
MOVES to another column).  So the correct, minimal form of lemma (4') is an EXISTENCE statement:

    (4'')  EXISTS a column j  with  N_j >= m/2 - O(1)  AND  C_j = O(1)  simultaneously.

This implies max_j(N_j - C_j) >= m/2 - O(1) directly.  This probe tests (4'') under the SHARPEST adversary:
  (A) adversarially MINIMIZE the floor v_3(q_min) = max_j(N_j - C_j) (structured 3-adic lifts + random), and
      at the achieved minimum report the FLOOR-CARRIER column j_f = argmax_j(N_j - C_j): its N_{j_f}, C_{j_f}.
      Hypothesis: C_{j_f} stays O(1) (small) while N_{j_f} >= m/2 - O(1) -- the floor is carried by a
      HIGH-N, LOW-C column that always exists.
  (B) census: over the same adversarial configs, the pair (min_j C_j, and the max N_j among LOW-C columns).
      Tests whether a low-C column with high N is always available.  Specifically report
      G := max_{j : C_j <= 1} N_j   (best N among near-zero-C columns) and compare to m/2.
Exact (L9).  Honest (L5): if C_{j_f} GROWS with m (or G < m/2 - O(1)), (4'') fails and the floor -- though
empirically robust (§6ax) -- has no clean existence proof via low-C columns.  One orbit (D=425).  RH [OUT].
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
    Ns = [N_of(xs, j) for j in range(m)]
    Cs = [C_of(xs, j, w) for j in range(m)]
    return Ns, Cs


def liftable_target(nodes, w, m):
    g = node_poly_coeffs(nodes)                       # nodes has m-2 entries
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


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6az: floor-carrier lemma (4''): EXISTS j with N_j >= m/2-O(1) AND C_j = O(1). Sharpest adversary.", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)

    print(f"\n(A)+(B) adversarially MINIMIZE the floor; report the floor-carrier (N_jf, C_jf) and G=max_{{C<=1}}N_j:",
          flush=True)
    print(f"{'m':>3} | {'min floor':>9} | {'m/2':>5} | {'carrier N_jf':>12} | {'carrier C_jf':>12} | "
          f"{'max C_jf seen':>13} | {'min G (C<=1)':>12}", flush=True)
    print("-" * 92, flush=True)
    for m in (4, 5, 6, 7, 8):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        min_floor = None; carrier_at_min = (None, None); max_Cjf = 0; min_G = None
        for _ in range(70):
            ts = rng.sample(range(1, 500), m)
            if len(set(xs_of(ts))) != m:
                continue
            for _rnd in range(10):
                Ns, Cs = NC(ts, w)
                floor_now = max(Ns[j] - Cs[j] for j in range(m))
                improved = False
                for i in range(m):
                    # try to explode C at some column by lifting node i toward the target from the other m-2
                    # nodes excluding i and a chosen victim column vv
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
                        f2 = max(Ns2[j] - Cs2[j] for j in range(m))
                        if f2 < floor_now:
                            ts, floor_now, improved = cand, f2, True
                if not improved:
                    break
            Ns, Cs = NC(ts, w)
            floor_now = max(Ns[j] - Cs[j] for j in range(m))
            jf = max(range(m), key=lambda j: Ns[j] - Cs[j])
            # G: best N among near-zero-C columns
            lowC = [Ns[j] for j in range(m) if Cs[j] <= 1]
            G = max(lowC) if lowC else -1
            max_Cjf = max(max_Cjf, Cs[jf])
            if min_floor is None or floor_now < min_floor:
                min_floor = floor_now; carrier_at_min = (Ns[jf], Cs[jf])
            if min_G is None or G < min_G:
                min_G = G
        print(f"{m:>3} | {str(min_floor):>9} | {m/2:>5} | {str(carrier_at_min[0]):>12} | "
              f"{str(carrier_at_min[1]):>12} | {max_Cjf:>13} | {str(min_G):>12}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if at the adversarial MIN of the floor the CARRIER column has C_jf = O(1) (small) and", flush=True)
    print("N_jf >= m/2 - O(1) -- and G = max_{C<=1} N_j stays >= m/2 - O(1) -- then lemma (4'') holds: a HIGH-N,", flush=True)
    print("LOW-C column always EXISTS, giving max_j(N_j-C_j) >= m/2 - O(1). This is the corrected, provable", flush=True)
    print("nugget. If C_jf grows or min G < m/2 - O(1), (4'') fails too. One orbit (D=425). RH stays [OUT].", flush=True)
