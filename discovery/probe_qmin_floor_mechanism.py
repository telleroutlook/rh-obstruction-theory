#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

MECHANISM of the CORRECTED lemma (4') (§6ay) — WHY does max_j(N_j - C_j) >= m/2 - O(1) survive C-explosion?

§6ax established: the floor v_3(q_min) = max_j(N_j - C_j) is robust though a single column's C_j is unbounded
(§6aw).  Two candidate mechanisms for a PROOF of (4'):
  (M1) CO-INFLATION: the very 3-adic lift that inflates C_{j0} (x_free ≈ a/b, 3-adically SPECIAL) also
       inflates v_3(det A) = sum_{k<l} v_3(x_k - x_l) (x_free clusters with some node), hence Sum_j N_j =
       2 v_3(det A) grows in lockstep -- the floor is carried by whichever column keeps large N.
  (M2) GOOD COLUMN: at j* = argmax_j N_j, C_{j*} is BOUNDED (the max-N column cannot ALSO have exploded C),
       so N_{j*} - C_{j*} >= max_j N_j - O(1) >= m/2 - O(1) directly.  (This is the clean provable route IF
       C at the argmax-N column is genuinely small.)
This probe measures BOTH, EXACTLY (L9):
  (A) under the §6aw single-node lift (C_{j0} -> huge), track (C_{j0}, v_3(det A), Sum_j N_j, Sum_j C_j,
      floor max_j(N_j-C_j), and at j*=argmax N: N_{j*}, C_{j*}) as precision c grows.  Tests M1 and M2.
  (B) DIRECTLY attack M2: adversarially try to make C_{j*} LARGE *at the argmax-N column* (lift the node
      excluded by the current argmax-N column).  Does argmax-N MOVE away (M2 self-protecting), or can the
      adversary hold argmax-N while exploding its C (M2 FALSE)?  Report min over attack of (N_{j*}-C_{j*}).
Honest (L5): if M2 holds (C at argmax-N stays O(1)), lemma (4') has a clean proof route via the argmax-N
column; if the adversary breaks M2, we fall back to M1 / the joint statement.  One orbit (D=425).  RH [OUT].
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


def v3_detA(xs):
    m = len(xs)
    return sum(vp_frac(xs[k] - xs[l], P) for k in range(m) for l in range(k + 1, m))


def profile(ts, w):
    m = len(ts)
    xs = xs_of(ts)
    Ns = [N_of(xs, j) for j in range(m)]
    Cs = [C_of(xs, j, w) for j in range(m)]
    floor = max(Ns[j] - Cs[j] for j in range(m))
    jstar = max(range(m), key=lambda j: Ns[j])       # argmax N
    return {
        "vdet": v3_detA(xs), "sumN": sum(Ns), "sumC": sum(Cs), "floor": floor,
        "jstar": jstar, "Njstar": Ns[jstar], "Cjstar": Cs[jstar], "Ns": Ns, "Cs": Cs,
    }


def liftable_target(Y, w, m):
    """For fixed nodes Y (list of m-2 x-values), return (alpha, halfv, u) if the free-node target a/b is a
    reachable 3-adic square with unit b, else None."""
    g = node_poly_coeffs(Y)
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
    return alpha, v // 2, R / (Fr(3) ** v)


def lift_t(alpha_pack, c):
    _, halfv, u = alpha_pack
    ru = hensel_sqrt_unit(lambda mod: frac_mod(u, mod), c)
    tf = (ru * (P ** halfv)) % (P ** c)
    return tf if tf != 0 else P ** c


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6ay: mechanism of lemma (4'). M1 co-inflation of v_3(detA)? M2 C bounded at the argmax-N column?", flush=True)
    print("=" * 100, flush=True)
    rng = random.Random(20260816)

    # (A) single-node lift: does v_3(detA)/SumN co-inflate with C_{j0}? is C at argmax-N bounded?
    print("\n(A) under the §6aw lift (explode C_{j0}); track co-inflation (M1) and C at argmax-N (M2):", flush=True)
    for m in (5, 6, 7):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        # find liftable Y + an extra excluded-column node
        pack = None
        for _ in range(800):
            tf = rng.sample(range(1, 400), m - 2)
            Y = xs_of(tf)
            if len(set(Y)) != m - 2:
                continue
            p = liftable_target(Y, w, m)
            if p:
                pack = (tf, p); break
        if not pack:
            print(f"    m={m}: no liftable Y", flush=True); continue
        ts_fixed, apack = pack
        extra = next(t for t in range(2, 500) if t not in ts_fixed)
        print(f"    m={m}: Y t={ts_fixed}, extra t={extra}", flush=True)
        print(f"      {'c':>3} | {'C_{j0}':>6} | {'v_3(detA)':>9} | {'SumN':>5} | {'SumC':>5} | "
              f"{'floor':>5} | {'j*':>2} | {'N_j*':>4} | {'C_j*':>4} | {'N_j*-C_j*':>9}", flush=True)
        for c in (2, 5, 10, 20):
            t_free = lift_t(apack, c)
            while t_free in ts_fixed or t_free == extra:
                t_free += P ** c
            ts = ts_fixed + [t_free, extra]
            if len(set(xs_of(ts))) != m:
                print(f"      {c:>3} | dup", flush=True); continue
            pr = profile(ts, w)
            j0 = m - 1                                    # column excluding 'extra' -> X' = Y U {x_free}
            Cj0 = pr["Cs"][j0]
            print(f"      {c:>3} | {Cj0:>6} | {pr['vdet']:>9} | {pr['sumN']:>5} | {pr['sumC']:>5} | "
                  f"{pr['floor']:>5} | {pr['jstar']:>2} | {pr['Njstar']:>4} | {pr['Cjstar']:>4} | "
                  f"{pr['Njstar']-pr['Cjstar']:>9}", flush=True)

    # (B) directly attack M2: try to explode C AT the argmax-N column; does argmax move or M2 break?
    print("\n(B) attack M2: maximize C at the argmax-N column; report min (N_j* - C_j*) & C_j* range:", flush=True)
    print(f"    {'m':>3} | {'min (N_j*-C_j*)':>15} | {'max C_j* seen':>13} | {'m/2':>5} | {'M2 (N_j*-C_j*>=~m/2)?':>21}",
          flush=True)
    for m in (4, 5, 6, 7):
        B = Bmatrix(m); w = solve_lower(B, PO.d_vec(TAU, m), m)
        min_diff = None; max_Cjs = 0
        for _ in range(60):
            ts = rng.sample(range(1, 500), m)
            if len(set(xs_of(ts))) != m:
                continue
            for _rnd in range(8):
                pr = profile(ts, w)
                js = pr["jstar"]
                # try to explode C at column js: lift the node EXCLUDED by js is not it -- C_js excludes x_js,
                # X' = all but js. To raise C_js, lift a node IN X' (say the smallest-index k!=js) toward the
                # single-node target computed from the OTHER nodes of X'.
                k_free = next(k for k in range(m) if k != js)
                others = [xs_of(ts)[k] for k in range(m) if k not in (js, k_free)]  # m-2 nodes
                pk = liftable_target(others, w, m)
                cand = ts[:]
                if pk:
                    tf = lift_t(pk, rng.choice([4, 8, 16]))
                    if tf not in ts:
                        cand[k_free] = tf
                else:
                    cand[k_free] = rng.randrange(1, 500)
                if len(set(cand)) != m or len(set(xs_of(cand))) != m:
                    continue
                pr2 = profile(cand, w)
                # keep the move if it lowers (N_j* - C_j*) at the (possibly new) argmax-N column
                if pr2["Njstar"] - pr2["Cjstar"] < pr["Njstar"] - pr["Cjstar"]:
                    ts = cand
            pr = profile(ts, w)
            diff = pr["Njstar"] - pr["Cjstar"]
            max_Cjs = max(max_Cjs, pr["Cjstar"])
            if min_diff is None or diff < min_diff:
                min_diff = diff
        print(f"    {m:>3} | {str(min_diff):>15} | {max_Cjs:>13} | {m/2:>5} | "
              f"{str(min_diff is not None and min_diff >= m/2 - 2):>21}", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): (A) if v_3(detA)/SumN GROWS with c alongside C_{j0}, mechanism M1 (co-inflation) holds;", flush=True)
    print("if C_j* (at argmax-N) stays SMALL while C_{j0} explodes, mechanism M2 holds (clean proof route via", flush=True)
    print("the argmax-N column). (B) if the adversary CANNOT push (N_j*-C_j*) below ~m/2 even when targeting the", flush=True)
    print("argmax-N column's C, M2 is robust -> lemma (4') provable as 'C at argmax-N is O(1)'. If M2 breaks,", flush=True)
    print("fall back to M1 / the joint form. One-sided attacks. One orbit (D=425). RH stays [OUT].", flush=True)
