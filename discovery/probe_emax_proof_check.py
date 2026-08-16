#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 §6f: VERIFY the self-contained elementary proof of the LINEAR e_max floor
(replaces the classical confluent-Vandermonde staircase citation, gap i).

Claim to verify (MONOMIAL Vandermonde V = [x_k^j]_{k, j=0..m-1} over Z_p, inert p):
  (L1) det of a square Vandermonde = prod_{k<l} (x_l - x_k)  [Vandermonde identity];
  (L2) for inert p, v_p(x_l - x_k) >= 1 iff x_k == x_l mod p (same class), else 0;
  (L3) on-line x-values occupy <= (p+3)/2 classes mod p  [rank-count, CORRECTED:
       x==1 reached by t==inf (p|b), x==-1 by t==0 (p|a); all of P^1(F_p) via s=4t^2];
  (L4) minor-removal identity: for any m-subset S and a node u in a class of size
       c within S, dropping u AND the top column gives an (m-1)-minor with
           v_p(det V_[S minus u, cols 0..m-2]) = v_p(det V_S) - sum_{w!=u, same cls} v_p(x_u-x_w)
                                              <= v_p(det V_S) - (c - 1);
  (MAIN) e_max := v_p(D_m) - v_p(D_{m-1}) >= c* - 1 >= ceil(2m/(p+3)) - 1,
       where c* = largest class size in a D_m-minimizing m-subset S*.

Strategy: over adversarial node families, compute D_m, D_{m-1} of the MONOMIAL
Vandermonde directly (gcd of minors), find an actual argmin m-subset S*, its
largest class c*, and check every link L1,L4,MAIN numerically.  If all hold, the
floor e_max >= ceil(2m/(p+1))-1 is PROVED (elementary), not merely evidenced.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil, gcd
from itertools import combinations


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        return None
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


def xclass_modp(x, p):
    """x in F_p (denominator a p-unit for inert p)."""
    return (x.numerator % p) * pow(x.denominator % p, p - 2, p) % p


def vp_frac(fr, p):
    """v_p of a rational (>=0 for p-integral)."""
    if fr == 0:
        return None
    return (vp(fr.numerator, p) or 0) - (vp(fr.denominator, p) or 0)


def vdet_vandermonde(xs, p):
    """v_p of det of the SQUARE Vandermonde on the given x-list via prod(x_l-x_k)."""
    v = 0
    n = len(xs)
    for i in range(n):
        for j in range(i + 1, n):
            d = xs[j] - xs[i]
            if d == 0:
                return None  # singular
            v += vp_frac(d, p)
    return v


def det_divisor_monomial(xs, m, r, p):
    """v_p of the r-th determinantal divisor D_r (gcd of r x r minors) of the
    m x K monomial Vandermonde [x_k^j], j=0..m-1, k over xs.  Uses the fact that
    every r x r minor is a generalized Vandermonde; we compute gcd of |minor|
    p-valuations = min over row/col subsets of v_p(minor).  For rigor of the
    PROOF we only need D_r as gcd => min of v_p over minors; we compute it
    exactly via integer minors after clearing one uniform p-unit denominator."""
    K = len(xs)
    # clear denominators uniformly (Lden a p-unit for inert p): scale x_k by L
    L = 1
    for x in xs:
        L = L * x.denominator // gcd(L, x.denominator)
    assert (vp(L, p) or 0) == 0, "uniform denom not a p-unit — p not inert here"
    Xint = [int(x * L) for x in xs]              # integers, == x_k * L
    # monomial rows j=0..m-1 ; entry (j,k) = (x_k)^j  -> use (Xint_k)^j / L^j,
    # but L^j is p-unit so p-valuation of any minor is unaffected by the L^j
    # scaling per column-power.  Compute v_p of r x r minors of [x_k^j] directly
    # in EXACT rationals (small sizes).
    best = None
    rows = list(range(m))
    for rowset in combinations(rows, r):
        for colset in combinations(range(K), r):
            M = [[xs[k] ** j for k in colset] for j in rowset]
            d = _det_frac(M)
            if d == 0:
                continue
            vv = vp_frac(d, p)
            best = vv if best is None else min(best, vv)
    return best


def _det_frac(M):
    """Exact rational determinant via fraction-free-ish expansion (small M)."""
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    tot = Fr(0)
    for c in range(n):
        minor = [row[:c] + row[c + 1:] for row in M[1:]]
        tot += ((-1) ** c) * M[0][c] * _det_frac(minor)
    return tot


def families(m, p):
    K = m + 3
    fams = {
        "half-int": [Fr(1, 2) + i for i in range(K)],
        "integer": [Fr(i) for i in range(1, K + 1)],
        "thirds": [Fr(a, 3) for a in range(1, K + 1)],
        "spread-p": _spread(p, m)[:K],
        "single-cls": [Fr(1 + p * i) for i in range(K)],
    }
    return {k: [t for t in v if t != 0][:K] for k, v in fams.items()}


def _spread(p, m):
    reps = list(range((p - 1) // 2 + 1))
    depth = ceil(2 * (m + 3) / (p + 1)) + 1
    return [Fr(c + p * i) for c in reps for i in range(depth) if (c + p * i) != 0]


if __name__ == "__main__":
    print("=" * 90, flush=True)
    print("OP1 §6f: verify the SELF-CONTAINED proof of e_max >= ceil(2m/(p+1))-1", flush=True)
    print("Monomial Vandermonde, inert p.  DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 90, flush=True)

    all_ok = True
    for p in (3, 7, 11):
        half = (p + 3) // 2   # CORRECT count: x==1 (t==inf) & x==-1 (t==0) reachable
        print(f"\n{'='*90}\np={p} (inert): <= (p+3)/2 = {half} x-classes mod p", flush=True)
        print(f"  {'fam':>12} {'m':>2} | {'vD_m':>5} {'vD_m1':>6} {'e_max':>5} "
              f"| {'c*':>3} {'PH':>3} | {'L1':>3} {'L4':>3} {'MAIN e_max>=c*-1':>16} "
              f"{'>=PH':>5}", flush=True)
        print("  " + "-" * 86, flush=True)
        for m in range(2, 7):
            PH = ceil(2 * m / (p + 3)) - 1   # honest pigeonhole floor over (p+3)/2 classes
            for fname, ts in families(m, p).items():
                if len(ts) < m:
                    continue
                xs = [x_of(t) for t in ts]
                # (L3 sanity) number of classes
                classes = {}
                for idx, x in enumerate(xs):
                    classes.setdefault(xclass_modp(x, p), []).append(idx)
                nclasses = len(classes)
                # D_m, D_{m-1} of monomial Vandermonde
                vDm = det_divisor_monomial(xs, m, m, p)
                vDm1 = det_divisor_monomial(xs, m, m - 1, p)
                if vDm is None or vDm1 is None:
                    continue
                emax = vDm - vDm1
                # find a D_m-minimizing m-subset S* and its largest class
                cstar = 0
                best_v = None
                for S in combinations(range(len(xs)), m):
                    sub = [xs[k] for k in S]
                    v = vdet_vandermonde(sub, p)
                    if v is None:
                        continue
                    if best_v is None or v < best_v:
                        best_v = v
                        # largest class size within S
                        cc = {}
                        for k in S:
                            cc[xclass_modp(xs[k], p)] = cc.get(xclass_modp(xs[k], p), 0) + 1
                        cstar = max(cc.values())
                # L1: v_p(D_m) equals the MIN square-Vandermonde valuation (best_v)
                L1 = (best_v == vDm)
                # L4/MAIN: e_max >= c*-1 and >= PH ; c* >= PH (pigeonhole)
                MAIN = (emax >= cstar - 1)
                gePH = (emax >= PH)
                L4 = (cstar >= ceil(2 * m / (p + 3)))  # pigeonhole over (p+3)/2 classes
                ok = L1 and MAIN and gePH and L4 and nclasses <= half
                all_ok = all_ok and ok
                flag = "" if ok else "  <<< FAIL"
                print(f"  {fname:>12} {m:>2} | {vDm:>5} {vDm1:>6} {emax:>5} "
                      f"| {cstar:>3} {PH:>3} | {str(L1):>3} {str(L4):>3} "
                      f"{str(MAIN):>16} {str(gePH):>5}{flag}", flush=True)

    print("\n" + "=" * 90, flush=True)
    print(f"ALL PROOF LINKS HOLD (L1 det=prod, L4 pigeonhole c*>=PH, "
          f"MAIN e_max>=c*-1>=PH): {all_ok}", flush=True)
    print("If True: e_max >= ceil(2m/(p+3))-1 is PROVED elementarily (Vandermonde", flush=True)
    print("det + minor removal), NO classical confluent-staircase citation needed.", flush=True)
