#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

TARGETED 3-ADIC LIFT ATTACK on lemma (4) (§6aw) — is C_j = v_3(S) truly BOUNDED, or does random ascent
(§6au, a mere LOWER bound) miss deep solutions?  This probe attacks the upper cap directly (honesty, L5).

SET-UP (from §6au/§6av).  S = <w, coeff vector of prod_{k in X'}(y - x_k)> = sum_i c_i w_i, where the node
polynomial prod(y-x_k) = sum_i c_i y^i and w = B^{-1} d is the FIXED off-line vector (all w_i are 3-units,
§6av).  Split off ONE free node: X' = {x_free} U Y, |Y| = m-2, g(y) = prod_{Y}(y - x_k) (deg m-2).  Then
prod(y-x_k) = (y - x_free) g(y), so
    S = a - x_free * b,   a = sum_j g_j w_{j+1} = L(y g),   b = sum_j g_j w_j = L(g),
i.e. S is AFFINE in the free node x_free with FIXED (Y-determined) 3-adic integers a, b.  If b is a 3-unit,
the adversary wants x_free ≈ a/b =: alpha 3-adically: v_3(S) = v_3(b) + v_3(alpha - x_free).

REACHABILITY / RIGIDITY.  x_free = x_of(t) = (4t^2-1)/(4t^2+1) = 1 - 2/(4t^2+1) lies in Z_3 (denominator is a
3-unit) with residue in {0, 2} mod 3 (t unit -> x≡0; 3|t -> x≡2).  Solving x_of(t) = alpha gives
    t^2 = (1 + alpha) / (4 (1 - alpha)) =: R.
If R is a 3-ADIC SQUARE (and alpha is a reachable residue), an EXACT t* in Z_3 solves x_of(t*) = alpha, so
integer t ≡ t* mod 3^c give x_of(t) ≡ alpha mod 3^c and hence v_3(S) >= c -- UNBOUNDED.  If for the sampled
Y-sets R is (almost) never a square, that non-squareness IS the rigidity that caps C_j.

THIS PROBE, for m = 4,5,6 (X' has m-1 nodes = 1 free + (m-2) fixed):
  (A) over many random fixed-node sets Y, tabulate v_3(b), the residue alpha mod 3, and whether R is a 3-adic
      square (the reachability test);
  (B) whenever a square R with reachable alpha is found, HENSEL-LIFT a 3-adic sqrt t* to precision 3^c and
      take the integer t_free = t* mod 3^c, then compute S EXACTLY (Fractions, L9) and report v_3(S) as c
      grows (c = 3,6,10,15,20,30).  If v_3(S) tracks c upward, lemma (4) (uniform O(1)) is REFUTED for D=425
      and §6au's plateau is an artifact of shallow random search (report honestly, L5).  If the lift JAMS
      (v_3(S) stops climbing) the rigidity is real and bounds C_j.
Cross-check: the affine identity S == a - x_free*b is verified exactly before any lifting.  One orbit
(D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_Cj_bilinear import Bmatrix, solve_lower, vp_frac, x_of
import discovery.probe_overdetermined_collision as PO

TAU = Fr(1)
P = 3


def node_poly_coeffs(xs):
    """Coefficients [c_0..c_n] of monic prod_k (y - x_k), n=len(xs) (c_n=1)."""
    c = [Fr(1)]                       # start with polynomial "1"
    for x in xs:
        # multiply by (y - x): new[i] = old[i-1] - x*old[i]
        nc = [Fr(0)] * (len(c) + 1)
        for i, ci in enumerate(c):
            nc[i] += -x * ci
            nc[i + 1] += ci
        c = nc
    return c


def S_of_nodes(xs, w):
    """S = <w, coeffs of prod(y-x_k)>. len(xs) must be m-1, w has length m."""
    c = node_poly_coeffs(xs)          # length m
    return sum(c[i] * w[i] for i in range(len(c)))


def vp_frac_local(fr, p):
    return vp_frac(fr, p)


def inv_mod(a, mod):
    return pow(a % mod, -1, mod)


def frac_mod(fr, mod):
    """Reduce a Fraction (3-unit denominator) to an integer mod 3^k."""
    return (fr.numerator % mod) * inv_mod(fr.denominator, mod) % mod


def is_3adic_square(R):
    """R a nonzero Fraction: 3-adic square iff v_3(R) even and unit part ≡ 1 mod 3."""
    if R == 0:
        return False
    v = vp_frac(R, P)
    if v % 2 != 0:
        return False
    u = R / (Fr(3) ** v)              # 3-adic unit
    return frac_mod(u, 3) == 1


def hensel_sqrt_unit(Rn_of, c):
    """Newton-lift a sqrt of a 3-adic UNIT R (given R mod 3^c via Rn_of(mod)) to precision 3^c. R≡1 mod 3."""
    r = 1                             # r^2 ≡ 1 ≡ R (mod 3)
    prec = 1
    while prec < c:
        prec = min(2 * prec, c)
        mod = P ** prec
        Rn = Rn_of(mod)
        # Newton: r <- r - (r^2 - R)/(2r)
        r = (r - (r * r - Rn) * inv_mod(2 * r, mod)) % mod
    return r % (P ** c)


if __name__ == "__main__":
    print("=" * 98, flush=True)
    print("§6aw: TARGETED 3-adic LIFT ATTACK on lemma (4). Is C_j=v_3(S) truly bounded, or does random", flush=True)
    print("ascent miss deep solutions? S = a - x_free*b affine in one node; lift x_free -> a/b if R is a square.", flush=True)
    print("=" * 98, flush=True)
    rng = random.Random(20260816)

    for m in (4, 5, 6):
        print(f"\n{'='*30} m = {m}  (X' has {m-1} nodes: 1 free + {m-2} fixed) {'='*30}", flush=True)
        B = Bmatrix(m)
        w = solve_lower(B, PO.d_vec(TAU, m), m)

        # (A) reachability census + affine-identity cross-check
        print("(A) census over random fixed-node sets Y (|Y|=m-2): v_3(b), alpha mod 3, R a 3-adic square?",
              flush=True)
        n_square = n_total = 0
        affine_ok = True
        squares_found = []
        for _ in range(400):
            ts_fixed = rng.sample(range(1, 400), m - 2)
            Y = [x_of(t) for t in ts_fixed]
            if len(set(Y)) != m - 2:
                continue
            g = node_poly_coeffs(Y)                       # length m-1
            b = sum(g[j] * w[j] for j in range(m - 1))
            a = sum(g[j] * w[j + 1] for j in range(m - 1))  # w has index up to m-1
            if b == 0:
                continue
            n_total += 1
            # cross-check the affine identity on a random free node
            tf = rng.randrange(1, 400)
            xf = x_of(tf)
            if xf not in Y:
                S_direct = S_of_nodes(Y + [xf], w)
                if S_direct != a - xf * b:
                    affine_ok = False
            alpha = a / b
            R = (1 + alpha) / (4 * (1 - alpha)) if alpha != 1 else None
            sq = (R is not None) and is_3adic_square(R)
            if sq:
                n_square += 1
                # a USABLE witness needs: unit b, alpha 3-adically REACHABLE (residue in {0,2}), R in Z_3
                reachable = frac_mod(alpha, 3) in (0, 2) and vp_frac(R, P) >= 0
                if len(squares_found) < 3 and vp_frac(b, P) == 0 and reachable:
                    squares_found.append((ts_fixed, a, b, alpha, R))
        print(f"    affine identity S == a - x_free*b exact: {affine_ok}", flush=True)
        print(f"    R is a 3-adic square in {n_square}/{n_total} sampled Y-sets "
              f"({100.0*n_square/max(n_total,1):.1f}%)", flush=True)

        # (B) if squares exist, LIFT and drive v_3(S) up; else report rigidity
        if not squares_found:
            print("(B) NO square-R (with unit b) found -> single-node target a/b is 3-adically UNREACHABLE for", flush=True)
            print("    these Y; this NON-SQUARENESS is the rigidity that caps C_j. (Evidence for lemma (4).)", flush=True)
            continue
        print("(B) square-R FOUND with unit b -> attempt to drive v_3(S) upward by lifting x_free -> a/b:",
              flush=True)
        ts_fixed, a, b, alpha, R = squares_found[0]
        Y = [x_of(t) for t in ts_fixed]
        v = vp_frac(R, P)                                  # even
        u = R / (Fr(3) ** v)                               # unit ≡ 1 mod 3
        halfv = v // 2
        print(f"    Y from t={ts_fixed}; v_3(b)={vp_frac(b,P)}, alpha mod 3 = {frac_mod(alpha,3)}, "
              f"v_3(R)={v}", flush=True)
        print(f"    {'c':>4} | {'t_free (mod 3^c)':>22} | {'v_3(S)':>7} | {'v_3(x_of(t)-alpha)':>18}", flush=True)
        print("    " + "-" * 60, flush=True)
        for c in (3, 6, 10, 15, 20, 30):
            root_u = hensel_sqrt_unit(lambda mod: frac_mod(u, mod), c)   # sqrt of unit part mod 3^c
            t_free = (root_u * (P ** halfv)) % (P ** c)                  # t* = 3^{v/2} * sqrt(unit)
            if t_free == 0:
                t_free = P ** c
            if any(t_free == tf for tf in ts_fixed):
                t_free += P ** c
            xf = x_of(t_free)
            if xf in Y:
                print(f"    {c:>4} | {'(dup node, skipped)':>22} |", flush=True)
                continue
            S = S_of_nodes(Y + [xf], w)
            vS = vp_frac(S, P)
            vx = vp_frac(xf - alpha, P)
            print(f"    {c:>4} | {t_free:>22} | {vS:>7} | {vx:>18}", flush=True)

    print("\n" + "=" * 98, flush=True)
    print("READING (L5): if in (B) v_3(S) CLIMBS with c (tracks the lift precision), then C_j = v_3(S) is", flush=True)
    print("UNBOUNDED for D=425 -- lemma (4) as stated (uniform O(1)) is REFUTED and §6au's <=12 plateau is a", flush=True)
    print("shallow-search artifact (the p=3 floor would then need a different, weaker C-control argument). If", flush=True)
    print("(A) shows R is (almost) never a square, or (B) v_3(S) JAMS at a bounded value despite lifting, then", flush=True)
    print("the reachability rigidity is real and CAPS C_j -- supporting lemma (4). One orbit (D=425). RH [OUT].", flush=True)
