#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

STEP (2) RIGOROUS: v_3(det A) >= QUADRATIC pigeonhole floor (§6ar) — nail the crux of the §6ao skeleton.

The §6ao proof skeleton's step (2) claims v_3(det A) >= m^2/4 - O(m), FORCED because the x-map has only
N(3)=2 residue classes mod 3, so any m nodes have >= C(ceil(m/2),2)+C(floor(m/2),2) ~ m^2/4 SAME-mod-3-class
pairs, and (by §6an, v_3(det A)=sum_{k<l} v_3(x_k-x_l), exact) each same-class pair contributes v_3>=1.

Two facts make this RIGOROUS and this probe checks both, exactly (L9), at LARGE m (cheap: ONE int_det per
config, not m+1):
  (F1) den(x_t)=4 t^2+1 is a 3-adic UNIT for all t (t!=0: 4+1=5=2 mod3; t=0 excluded) => x_t is a 3-adic
       integer, mod-3 class well-defined; and t != 0 mod 3 -> x=0, t=0 mod 3 -> x=2 (only 2 classes).
  (F2) same mod-3 x-class => v_3(x_k - x_l) >= 1.
Then v_3(det A) >= (#same-class pairs).  The ADVERSARY minimizing v_3(det A) BALANCES the 2 classes to
minimize same-class pairs, hitting PIG(m) := C(ceil(m/2),2)+C(floor(m/2),2).  So the prediction is:
       adversarial-min v_3(det A)  ==  PIG(m)   (up to the O(m) from higher v_3 and the 4/all-ones/leading
                                                 -coeff correction, which §6an measured = 0 for odd p).
This probe: (a) verifies F1/F2 by direct class computation; (b) adversarially MINIMIZES v_3(det A) at
m=4..20 and compares to PIG(m); (c) reports the class-split at the minimizer (should be balanced).  If the
adversarial min tracks PIG(m) ~ m^2/4, step (2) is an airtight pigeonhole lemma -- a clean, provable,
outsourceable nugget.  Honest (L5): descent = UPPER bound on the true adversarial min; a min BELOW PIG(m)
would refute F2.  One orbit (D=425).  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import comb
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


def x_class_mod3(t):
    """3-adic class of x_t = (4t^2-1)/(4t^2+1). den is a 3-unit; class = num*den^{-1} mod 3."""
    x = x_of(t)
    num, den = x.numerator, x.denominator
    assert den % 3 != 0, f"den divisible by 3 for t={t}"          # F1 check
    inv = pow(den % 3, -1, 3)
    return (num % 3) * inv % 3


def PIG(m):
    return comb((m + 1) // 2, 2) + comb(m // 2, 2)


def v3_detA(ts, m):
    b = build(ts, m)
    if not b:
        return None
    dA = int_det(cols_to_rows(b[0], m))
    return vp_int(dA, P) if dA != 0 else None


def descent_min_v3det(ts, m, rng, rounds, tries):
    best_ts = ts[:]
    best = v3_detA(best_ts, m)
    best = best if best is not None else 10**9
    for _ in range(rounds):
        improved = False
        for i in range(m):
            for _ in range(tries):
                cand = best_ts[:]
                cand[i] = rng.randrange(1, 500)
                if len(set(cand)) != m or any(t == 0 for t in cand):
                    continue
                v = v3_detA(cand, m)
                if v is not None and v < best:
                    best, best_ts, improved = v, cand, True
        if not improved:
            break
    return best_ts, best


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("STEP (2) RIGOROUS (§6ar): adversarial-min v_3(det A) =? PIG(m)=C(ceil(m/2),2)+C(floor(m/2),2).", flush=True)
    print("If the min tracks PIG(m) ~ m^2/4, the 2-class-mod-3 pigeonhole floor on v_3(det A) is airtight.", flush=True)
    print("=" * 96, flush=True)
    rng = random.Random(20260816)
    # (a) F1/F2 direct checks
    print("\n(a) F1 (den is 3-unit) + F2 (same-class pair => v_3(x_k-x_l)>=1) checks over t=1..60:", flush=True)
    ts_chk = [t for t in range(1, 61)]
    cls = {t: x_class_mod3(t) for t in ts_chk}
    n0 = sum(1 for t in ts_chk if cls[t] == 0)
    n2 = sum(1 for t in ts_chk if cls[t] == 2)
    nother = sum(1 for t in ts_chk if cls[t] not in (0, 2))
    f2_ok = True
    f2_bad = None
    for a in range(len(ts_chk)):
        for b in range(a + 1, len(ts_chk)):
            ta, tb = ts_chk[a], ts_chk[b]
            if cls[ta] == cls[tb]:
                if vp_frac(x_of(ta) - x_of(tb), P) < 1:
                    f2_ok = False; f2_bad = (ta, tb); break
        if not f2_ok:
            break
    print(f"    F1: all den 3-units = True (asserted in x_class_mod3, no exception raised)", flush=True)
    print(f"    class counts over t=1..60: class0={n0}, class2={n2}, other={nother}  (expect other=0, 2 classes)",
          flush=True)
    print(f"    F2: same-class => v_3>=1 : {f2_ok}" + (f"  COUNTEREXAMPLE {f2_bad}" if not f2_ok else ""),
          flush=True)
    # (b) adversarial min vs PIG(m)
    print(f"\n{'m':>3} | {'adv-min v_3(detA)':>17} | {'PIG(m)':>7} | {'m^2/4':>6} | {'split@min (c0,c2)':>17}",
          flush=True)
    print("-" * 66, flush=True)
    for m in range(9, 19):
        # lean budget (one int_det per config; UPPER bound on adv-min, L5) to extend the quadratic trend.
        if m <= 12:
            NR, rounds, tries = 5, 6, 5
        else:
            NR, rounds, tries = 3, 4, 4
        best_v, best_ts = None, None
        for _ in range(NR):
            s0 = rng.sample(range(1, 500), m)
            if not build(s0, m):
                continue
            ts, v = descent_min_v3det(s0, m, rng, rounds, tries)
            if v is not None and (best_v is None or v < best_v):
                best_v, best_ts = v, ts
        if best_ts is not None:
            c0 = sum(1 for t in best_ts if x_class_mod3(t) == 0)
            c2 = len(best_ts) - c0
            split = f"({c0},{c2})"
        else:
            split = "-"
        print(f"{m:>3} | {str(best_v):>17} | {PIG(m):>7} | {m * m // 4:>6} | {split:>17}", flush=True)
    print("\n" + "=" * 96, flush=True)
    print("READING (L5): if F1/F2 hold and adv-min v_3(detA) ~ PIG(m) ~ m^2/4 with a BALANCED split at the", flush=True)
    print("minimizer, then step (2) is an airtight pigeonhole lemma: v_3(det A) >= PIG(m) = m^2/4 - O(m),", flush=True)
    print("forced by only 2 residue classes mod 3 -- a clean provable nugget closing the crux of §6ao. If the", flush=True)
    print("min drops BELOW PIG(m), F2 is false and the count needs care. Descent = UPPER bound on adv-min.", flush=True)
    print("One orbit (D=425). Evidence, not proof. RH stays [OUT].", flush=True)
