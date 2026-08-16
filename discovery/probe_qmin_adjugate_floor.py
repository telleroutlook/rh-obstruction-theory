#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

THE ADJUGATE NO-CANCELLATION ROUTE to the p=3 floor (§6bc) — a possibly-PROVABLE reduction of Step 4.

Floor identity (proved, §6ao): v_3(q_min) = v_3(det A) - min_j v_3(minor_j), where minor_j = det[A col j -> d].
Expanding minor_j along its d-column: minor_j = sum_k d_k * T_{jk},  T_{jk} = (-1)^{k+j} M_{kj} (the cofactor;
M_{kj} = det of A with row k, col j deleted).  Define the NO-CANCELLATION prediction
      pred_j = min_k [ v_3(d_k) + v_3(T_{jk}) ]           (a min of explicit cofactor valuations),
so ALWAYS v_3(minor_j) >= pred_j (ultrametric), with equality iff the min-achieving term(s) do not 3-adically
cancel.  Set  gap_j = v_3(minor_j) - pred_j >= 0  (the cancellation amount) and
      no_canc_floor = v_3(det A) - min_j pred_j .
KEY LOGIC:  no_canc_floor >= floor ALWAYS; and IF gap = 0 at the pred-argmin column then floor = no_canc_floor.
So IF (H1) no_canc_floor >= m/2 - O(1) AND (H2) the pred-argmin column has gap 0 (no cancellation), the floor is
PROVED by a pure COFACTOR-VALUATION bound (Vandermonde/pigeonhole -- no bilinear-cancellation subtlety), a far
more tractable target than the joint N_j-C_j bound.  This probe MEASURES, for p=3, the D=425 (3-unimodular)
orbit, over random valid configs AND an adversary that MINIMIZES the floor:
  (H1) is no_canc_floor >= m/2 - O(1)?         (the provable-looking piece)
  (H2) at pred-argmin, is gap = 0?             (does the mechanism transfer to the true floor?)
  (H3) can the adversary force floor << no_canc_floor (cancellation at all low-pred columns)?  If yes the route
       is insufficient and we revert to the joint bound (reported plainly).
Exact (L9).  Honest (L5): adversary ascent = one-sided; a single small config is not decisive.  One orbit.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
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
INF = 10**9


def build(ts, m):
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


def submatrix_det(rows, drop_row, drop_col, m):
    sub = [[rows[r][c] for c in range(m) if c != drop_col] for r in range(m) if r != drop_row]
    return int_det(sub)


def analyze(ts, m):
    """Return dict of floor / no_canc_floor / gap-at-pred-argmin, or None if not a valid config."""
    b = build(ts, m)
    if not b:
        return None
    oc, vo = b
    rows = cols_to_rows(oc, m)             # A as rows
    det = int_det(rows)
    if det == 0:
        return None
    vdet = vp_int(det, P)
    preds, vminors = [], []
    for j in range(m):
        # cofactors T_{jk} = (-1)^{k+j} M_{kj}
        pj = INF
        cols = [list(oc[k]) for k in range(m)]
        cols[j] = list(vo)
        minor_j = int_det(cols_to_rows(cols, m))
        if minor_j == 0:
            return None
        vminors.append(vp_int(minor_j, P))
        for k in range(m):
            if vo[k] == 0:
                continue
            Mkj = submatrix_det(rows, k, j, m)
            if Mkj == 0:
                continue
            pj = min(pj, vp_int(vo[k], P) + vp_int(Mkj, P))
        preds.append(pj)
    min_pred = min(preds)
    floor = vdet - min(vminors)
    no_canc_floor = vdet - min_pred
    jstar = min(range(m), key=lambda j: preds[j])       # pred-argmin column
    gap_at_jstar = vminors[jstar] - preds[jstar]         # >= 0
    # also: min gap over the columns that ACHIEVE min_pred
    argmins = [j for j in range(m) if preds[j] == min_pred]
    min_gap_over_argmins = min(vminors[j] - preds[j] for j in argmins)
    return dict(vdet=vdet, floor=floor, no_canc=no_canc_floor, minpred=min_pred,
                gap_star=gap_at_jstar, gap_argmins=min_gap_over_argmins)


# ---- adversarial floor-minimizer (structured 3-adic lifts, reusing the §6aw lift machinery) ----
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


def adversarial_min(m, w, rng, restarts=20, rounds=6):
    """Minimize the true floor; return the analysis dict at the achieved minimum."""
    best = None
    for _ in range(restarts):
        ts = rng.sample(range(1, 400), m)
        a0 = analyze(ts, m)
        if a0 is None:
            continue
        cur = a0
        for _rnd in range(rounds):
            improved = False
            for i in range(m):
                xs = [x_of(t) for t in ts]
                for vv in range(m):
                    if vv == i:
                        continue
                    others = [xs[k] for k in range(m) if k not in (i, vv)]
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
                        cand[i] = rng.randrange(1, 400)
                    a2 = analyze(cand, m)
                    if a2 is not None and a2["floor"] < cur["floor"]:
                        ts, cur, improved = cand, a2, True
            if not improved:
                break
        if best is None or cur["floor"] < best["floor"]:
            best = cur
    return best


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6bc: adjugate NO-CANCELLATION route. floor = vdet - min_j v(minor_j); minor_j = sum_k d_k T_jk.", flush=True)
    print("pred_j = min_k[v(d_k)+v(T_jk)] (cofactor valuations); no_canc_floor = vdet - min_j pred_j >= floor.", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)

    print("\n(1) RANDOM valid configs: does no_canc_floor >= m/2 (H1) and is gap=0 at pred-argmin (H2)?", flush=True)
    print(f"{'m':>3} | {'#cfg':>5} | {'min floor':>9} | {'min no_canc':>11} | {'m/2':>4} | "
          f"{'H1:no_canc>=m/2-2':>17} | {'H2: gap*==0 frac':>16}", flush=True)
    print("-" * 82, flush=True)
    for m in (4, 5, 6, 7):
        cnt = 0; minfl = INF; minnc = INF; gap0 = 0
        tries = 0
        while cnt < 60 and tries < 4000:
            tries += 1
            ts = rng.sample(range(1, 120), m)
            a = analyze(ts, m)
            if a is None:
                continue
            cnt += 1
            minfl = min(minfl, a["floor"]); minnc = min(minnc, a["no_canc"])
            if a["gap_star"] == 0:
                gap0 += 1
        print(f"{m:>3} | {cnt:>5} | {minfl:>9} | {minnc:>11} | {m/2:>4} | "
              f"{str(minnc >= m/2 - 2):>17} | {f'{gap0}/{cnt}':>16}", flush=True)

    print("\n(2) ADVERSARIAL floor-min: can the adversary force floor << no_canc_floor (H3, cancellation route)?", flush=True)
    print(f"{'m':>3} | {'adv floor':>9} | {'no_canc@min':>11} | {'m/2':>4} | {'gap* @min':>9} | "
          f"{'gap over pred-argmins':>21}", flush=True)
    print("-" * 74, flush=True)
    for m in (4, 5, 6, 7):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        a = adversarial_min(m, w, rng)
        if a is None:
            print(f"{m:>3} | {'--':>9}", flush=True); continue
        print(f"{m:>3} | {a['floor']:>9} | {a['no_canc']:>11} | {m/2:>4} | {a['gap_star']:>9} | "
              f"{a['gap_argmins']:>21}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): if (H1) no_canc_floor >= m/2 - O(1) AND (H2) gap=0 at the pred-argmin (so floor =", flush=True)
    print("no_canc_floor), the p=3 floor reduces to a COFACTOR-VALUATION bound (min_j pred_j <= vdet - m/2),", flush=True)
    print("which is a Vandermonde/pigeonhole statement -- a tractable proof target for Step 4 of OB-42. If (H3)", flush=True)
    print("the adversary drives floor << no_canc_floor (cancellation at every low-pred column), the route is", flush=True)
    print("insufficient and Step 4 stays the full joint bound. One orbit (D=425). RH stays [OUT].", flush=True)
