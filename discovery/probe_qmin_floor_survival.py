#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

DOES THE FLOOR SURVIVE THE C-EXPLOSION? (§6ax) — §6aw REFUTED lemma (4): C_j = v_3(S) is UNBOUNDED (a single
3-adic node lift drives it arbitrarily high).  That kills the proof ROUTE "v_3(q_min) >= max_j N_j - max_j C_j
>= m/2 - O(1)" (subtracting an unbounded max_j C_j is vacuous).  But the FLOOR itself is the JOINT quantity
    v_3(q_min) = max_j ( N_j - C_j ),   N_j = sum_{k!=j} v_3(x_j - x_k),   C_j = v_3(<w, coeffs prod_{k!=j}(y-x_k)>),
(§6ao, cross-checked exactly in §6aq).  Inflating ONE column's C_j only removes THAT column from the argmax --
the max over the OTHER columns may still be >= m/2.  This probe decides whether the floor SURVIVES or COLLAPSES
under the very lift that refutes lemma (4):

  (X) CROSS-CHECK: v3_qmin_via_NC(ts) := max_j (N_j - C_j) equals the SNF-free integer-det v_3(q_min) (§6aq
      v3_qmin_fast) EXACTLY on random configs (else the cheap N-C form is wrong).
  (Y) SINGLE-LIFT experiment: build an m-node set whose node x_free is 3-adically lifted (precision 3^c, c up
      to 30) so that C_{j0} explodes for one excluded column j0; report the FULL v_3(q_min) = max_j(N_j - C_j)
      and WHICH column attains it.  If v_3(q_min) stays >= ~m/2 while C_{j0} -> huge, the FLOOR SURVIVES (only
      the route dies).  If it collapses toward 0, the floor is refuted.
  (Z) STRUCTURED-MIN attack: adversarially try to DRIVE v_3(q_min) DOWN using lifts (the real floor test,
      stronger than §6aq's random ascent) -- lift several nodes toward per-column targets and take the best
      (lowest) v_3(q_min) found; compare to m/2.

Exact arithmetic (L9).  Honest (L5): (X) mismatch refutes the N-C form; a genuine collapse in (Y)/(Z) would
REFUTE the p=3 floor (and OP1's q_min lower bound for D=425), not just the route -- reported plainly if seen.
One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_Cj_bilinear import Bmatrix, solve_lower, vp_frac, x_of
from discovery.probe_qmin_p3_floor_fast import v3_qmin_fast
from discovery.probe_qmin_snf import cleared_columns, matrix_rank_int
from discovery.probe_qmin_Cj_lift_attack import (
    node_poly_coeffs, S_of_nodes, frac_mod, is_3adic_square, hensel_sqrt_unit,
)
import discovery.probe_overdetermined_collision as PO

SIG, TAU = Fr(3, 4), Fr(1)
P = 3


def N_j(xs, j):
    return sum(vp_frac(xs[j] - xs[k], P) for k in range(len(xs)) if k != j)


def C_j_val(xs, j, w):
    Xp = [xs[k] for k in range(len(xs)) if k != j]
    return vp_frac(S_of_nodes(Xp, w), P)


def v3_qmin_via_NC(ts, m, w):
    """v_3(q_min) = max_j (N_j - C_j), cheap Fraction form (§6ao). Returns (val, argmax j, per-j list)."""
    xs = [x_of(t) for t in ts]
    rows = [(N_j(xs, j) - C_j_val(xs, j, w), N_j(xs, j), C_j_val(xs, j, w)) for j in range(m)]
    best = max(range(m), key=lambda j: rows[j][0])
    return rows[best][0], best, rows


def build_int(ts, m):
    """Cleared integer on-line columns + off-line vector for the SNF-free v_3(q_min)."""
    if any(t == 0 for t in ts) or len(set(ts)) != len(ts):
        return None
    oc, vo = cleared_columns([Fr(t) for t in ts], SIG, TAU, m)
    if len(oc) != m or matrix_rank_int(oc, m) != m:
        return None
    return oc, vo


if __name__ == "__main__":
    print("=" * 98, flush=True)
    print("§6ax: does the p=3 FLOOR v_3(q_min)=max_j(N_j-C_j) survive the C-explosion that refuted lemma (4)?", flush=True)
    print("=" * 98, flush=True)
    rng = random.Random(20260816)

    # (X) cross-check cheap N-C form vs SNF-free integer-det v_3(q_min)
    print("\n(X) cross-check v3_qmin_via_NC == v3_qmin_fast (integer-det) on random configs:", flush=True)
    okX = True
    for m in range(4, 8):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        got = 0
        for _ in range(200):
            ts = rng.sample(range(1, 200), m)
            b = build_int(ts, m)
            if not b:
                continue
            v_nc, _, _ = v3_qmin_via_NC(ts, m, w)
            v_ref = v3_qmin_fast(b[0], b[1], m)
            match = (v_nc == v_ref)
            okX = okX and match
            print(f"    m={m}: v3_qmin_via_NC={v_nc}  v3_qmin_fast={v_ref}  match={match}", flush=True)
            got += 1
            if got >= 2:
                break
    print(f"  ALL MATCH: {okX}", flush=True)

    # helper: find a Y (m-2 fixed nodes) + separate excluded column so that lifting x_free explodes C_{j0}.
    def find_liftable(m, w, tries=600):
        """Return (Y_ts, alpha, R, halfv, u) with reachable square target for the free node against fixed Y."""
        for _ in range(tries):
            ts_fixed = rng.sample(range(1, 400), m - 2)
            Y = [x_of(t) for t in ts_fixed]
            if len(set(Y)) != m - 2:
                continue
            g = node_poly_coeffs(Y)
            b = sum(g[jj] * w[jj] for jj in range(m - 1))
            a = sum(g[jj] * w[jj + 1] for jj in range(m - 1))
            if b == 0 or vp_frac(b, P) != 0:
                continue
            alpha = a / b
            if alpha == 1:
                continue
            R = (1 + alpha) / (4 * (1 - alpha))
            if not is_3adic_square(R):
                continue
            if frac_mod(alpha, 3) not in (0, 2) or vp_frac(R, P) < 0:
                continue
            v = vp_frac(R, P); u = R / (Fr(3) ** v)
            return ts_fixed, alpha, R, v // 2, u
        return None

    # (Y) single-lift: explode C for one excluded column j0, then read the FULL v_3(q_min).
    print("\n(Y) SINGLE-LIFT: drive C_{j0} -> huge via one node; report full v_3(q_min)=max_j(N_j-C_j) & argmax:", flush=True)
    for m in (4, 5, 6):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        found = find_liftable(m, w)
        if not found:
            print(f"    m={m}: no liftable target found (skip)", flush=True)
            continue
        ts_fixed, alpha, R, halfv, u = found
        # the m-node on-line set = Y (m-2 fixed) + x_free (lifted) + one extra 'excluded-column' node x_j0
        # choose x_j0 = a plain small distinct node; the lift makes C explode for the column excluding x_j0
        # (i.e. X' = Y U {x_free}); we then also compute v_3(q_min) over ALL m columns.
        extra_t = next(t for t in range(2, 500) if t not in ts_fixed)
        print(f"    m={m}: Y t={ts_fixed}, extra(excluded-col) t={extra_t}, alpha mod3={frac_mod(alpha,3)}", flush=True)
        print(f"      {'c':>3} | {'C_{j0} (exploded)':>17} | {'v_3(q_min)=max_j(N_j-C_j)':>26} | {'argmax j':>8} | {'>= m/2?':>7}", flush=True)
        for c in (3, 10, 20, 30):
            root_u = hensel_sqrt_unit(lambda mod: frac_mod(u, mod), c)
            t_free = (root_u * (P ** halfv)) % (P ** c)
            if t_free == 0:
                t_free = P ** c
            while t_free in ts_fixed or t_free == extra_t:
                t_free += P ** c
            ts_full = ts_fixed + [t_free, extra_t]        # m nodes
            xs = [x_of(t) for t in ts_full]
            if len(set(xs)) != m:
                print(f"      {c:>3} | dup node, skip", flush=True)
                continue
            # j0 = the column excluding x_free? No: X'=Y U {x_free} means excluded column is extra_t's index.
            j0 = m - 1                                    # extra_t is last -> X' excludes it = Y U {x_free}
            Cj0 = C_j_val(xs, j0, w)
            vq, argj, rows = v3_qmin_via_NC(ts_full, m, w)
            print(f"      {c:>3} | {Cj0:>17} | {vq:>26} | {argj:>8} | {str(vq >= m/2):>7}", flush=True)

    # (Z) structured minimization: try to DRIVE v_3(q_min) DOWN with lifts (real floor test).
    print("\n(Z) STRUCTURED-MIN: adversarially minimize v_3(q_min) using lifts (stronger than random ascent):", flush=True)
    print(f"    {'m':>3} | {'min v_3(q_min) found':>20} | {'m/2':>5} | {'floor holds (>=~m/2)?':>21}", flush=True)
    for m in (4, 5, 6, 7):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        best = None
        for _ in range(40):
            ts = rng.sample(range(1, 500), m)
            if len(set(x_of(t) for t in ts)) != m:
                continue
            # coordinate lift: for each node, try to align it to lower its column's (N-C) contribution
            for _rnd in range(6):
                improved = False
                for i in range(m):
                    for cc in (2, 4, 8):
                        # attempt: replace node i by a lifted value targeting the single-node root for column i
                        others = [x_of(ts[k]) for k in range(m) if k != i]
                        g = node_poly_coeffs(others)
                        bb = sum(g[jj] * w[jj] for jj in range(m - 1))
                        aa = sum(g[jj] * w[jj + 1] for jj in range(m - 1))
                        if bb == 0:
                            continue
                        al = aa / bb
                        if al == 1:
                            continue
                        Rr = (1 + al) / (4 * (1 - al))
                        if not is_3adic_square(Rr) or frac_mod(al, 3) not in (0, 2) or vp_frac(Rr, P) < 0:
                            # can't lift this column; try a random tweak instead
                            cand = ts[:]; cand[i] = rng.randrange(1, 500)
                        else:
                            vv = vp_frac(Rr, P); uu = Rr / (Fr(3) ** vv)
                            ru = hensel_sqrt_unit(lambda mod: frac_mod(uu, mod), cc)
                            tf = (ru * (P ** (vv // 2))) % (P ** cc)
                            if tf == 0:
                                tf = P ** cc
                            cand = ts[:]; cand[i] = tf
                        if any(cand[i] == cand[k] for k in range(m) if k != i):
                            continue
                        if len(set(x_of(t) for t in cand)) != m:
                            continue
                        vq, _, _ = v3_qmin_via_NC(cand, m, w)
                        cur, _, _ = v3_qmin_via_NC(ts, m, w)
                        if vq < cur:
                            ts, improved = cand, True
                if not improved:
                    break
            vq, _, _ = v3_qmin_via_NC(ts, m, w)
            if best is None or vq < best:
                best = vq
        print(f"    {m:>3} | {str(best):>20} | {m/2:>5} | {str(best is not None and best >= m/2 - 2):>21}", flush=True)

    print("\n" + "=" * 98, flush=True)
    print("READING (L5): (X) must be ALL MATCH. In (Y), if v_3(q_min) stays >= ~m/2 while C_{j0} explodes, the", flush=True)
    print("FLOOR SURVIVES the lemma-(4) refutation -- only the 'max N - max C' ROUTE dies; the argmax simply", flush=True)
    print("moves to another column. In (Z), if structured lifts CANNOT push v_3(q_min) below ~m/2, the floor", flush=True)
    print("is robust even against the sharpest 3-adic attack. A genuine collapse in (Y)/(Z) would REFUTE the", flush=True)
    print("p=3 floor for D=425. Ascent/min are one-sided bounds. One orbit (D=425). RH stays [OUT].", flush=True)
