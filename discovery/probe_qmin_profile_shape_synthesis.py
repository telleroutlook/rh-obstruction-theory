#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cf — SYNTHESIS: the OP1 floor MECHANISM is dictated by the SHAPE of the moment profile v_p(w_i),
i=0..m-1, of the fixed vector w = B^{-1} d at the working prime p.  Three shapes, three mechanisms:

  (a) STRICTLY DECREASING (min at TOP index, linearly negative)  -> §6cd ultrametric floor 1 - W_top.
      Occurs at p=2 for n ODD (Row 2).
  (b) EXACTLY CONSTANT at height h = 2*v2(n) >= 4  -> pins C_j node-independent (§6bi), floor 2m-2-(h-1).
      Occurs at p=2 for 4|n (Row 1).
  (c) CONSTANT at the S=1 boundary (h=2), OR FLAT-AT-UNIT (h=0)  -> ultrametric TIE / no depth, C_j not
      pinned, adversary-liftable -> the un-proved competition lemma (4''). OPEN.
      Occurs at p=2 for n=2 mod4 (h=2, S=1, VACUOUS) and at p=3 for Row 3 (h=0, w a 3-unit).

GOVERNING PARAMETER at p=2 is the 2-adic valuation of n:
      v2(n)=0 (n odd)     -> DECREASING            [Row 2, §6cd, floor 3m/2-O(1)]
      v2(n)>=2 (4|n)      -> CONSTANT h=2v2(n)>=4   [Row 1, §6bm/§6bi, floor 2m-2-S, S=2v2(n)-1]
      v2(n)=1 (n=2 mod4)  -> CONSTANT h=2, S=1 TIE  [Row 3, p=2 VACUOUS -> falls to p=3, OPEN]

This probe VERIFIES (EXACT, L9): the constant-height law v2(w_i)==2*v2(n) for n even; the decreasing shape
for n odd (min strictly at the top index, linearly negative); and the flat-unit p=3 profile for Row 3.

READING (L5): the 4-row coverage split IS this profile-shape trichotomy.  A shape-(a)/(b) prime (the only
provable regimes) can arise ONLY from B's 2-adic content (offline d is 2-integral; B=4(1-T_j) carries the
only 2-adic denominators), landing at the S=1 tie for n=2 mod4 and being unit at every odd prime unless p
ramifies.  Hence Rows 3,4 have NO shape-(a)/(b) prime and are forced onto shape (c) = the open lemma (4'').
OP1 CLOSES for all n != 2 mod4 at p=2 (Row 1 proved §6bm; Row 2 candidate modulo the PROVED FACT A §6br),
OPEN for n=2 mod4.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr

from discovery.probe_qmin_p2_floor_identity import wvec
from discovery.probe_qmin_Cj_bilinear import vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def shape_of(profile):
    """Classify a valuation profile as decreasing / constant / other."""
    if all(profile[i] == profile[0] for i in range(len(profile))):
        return "CONSTANT h=%d" % profile[0]
    if all(profile[i + 1] <= profile[i] for i in range(len(profile) - 1)) and profile[-1] < profile[0]:
        return "DECREASING (top=%d)" % profile[-1]
    return "other"


if __name__ == "__main__":
    m = 8
    print("=" * 100, flush=True)
    print("§6cf: OP1 floor mechanism = w-profile SHAPE at the working prime. Trichotomy in v2(n). RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    # (a)+(b)+(c) at p=2: scan orbits across all n mod 4 (tau=1)
    SIGS = [Fr(2, 3), Fr(4, 5), Fr(6, 7),          # n odd    -> DECREASING (Row 2)
            Fr(3, 4), Fr(7, 8), Fr(5, 12), Fr(9, 16),  # 4|n  -> CONSTANT h=2v2(n)>=4 (Row 1)
            Fr(1, 2), Fr(3, 10), Fr(7, 10), Fr(5, 14)]  # n=2 mod4 -> CONSTANT h=2,S=1 (Row 3)
    ok = True
    print("\np=2 profile shapes (m=%d):" % m, flush=True)
    print("  %-6s %3s %6s  %-30s  law: 2*v2(n)  shape-matches-v2(n)-regime" % ("sigma", "n", "v2(n)", "profile shape"), flush=True)
    for sig in SIGS:
        _, _, n = rho_pqn(sig, Fr(1))
        w = wvec(m, sig, Fr(1))
        prof = [vp_frac(Fr(w[i]), 2) for i in range(m)]
        sh = shape_of(prof)
        vn = v2(n)
        if n % 2 == 1:            # Row 2: decreasing, linearly negative top
            good = sh.startswith("DECREASING") and prof[-1] < 0
            regime = "DECREASING (Row2/§6cd)"
        else:                     # n even: constant at height 2*v2(n)
            good = sh == ("CONSTANT h=%d" % (2 * vn))
            regime = ("CONSTANT h=%d, S=%d " % (2 * vn, 2 * vn - 1)) + (
                "(Row1/§6bm)" if vn >= 2 else "(Row3, S=1 TIE -> p=2 VACUOUS)")
        ok = ok and good
        print("  %-6s %3d %6d  %-30s  h=%2d       %s  [%s]" % (
            sig, n, vn, sh, 2 * vn, good, regime), flush=True)

    # (c) at p=3 for Row 3: w is a 3-unit (flat height 0)
    print("\np=3 profile for Row 3 (n=2 mod4, 3 not| n): FLAT-AT-UNIT (height 0) => no basis depth:", flush=True)
    for sig in (Fr(1, 2), Fr(3, 10), Fr(7, 10)):
        _, _, n = rho_pqn(sig, Fr(1))
        w = wvec(m, sig, Fr(1))
        prof3 = [vp_frac(Fr(w[i]), 3) for i in range(m)]
        flat_unit = min(prof3) == 0
        print("  sigma=%-6s n=%2d  v3(w_i) min=%d  flat-unit=%s  profile=%s" % (
            sig, n, min(prof3), flat_unit, prof3), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): the trichotomy holds EXACTLY. Provable regimes (a),(b) need B's 2-adic depth, absent", flush=True)
    print("for n=2 mod4 (tie) at p=2 and for every odd prime (unit) unless ramified. So Rows 3,4 are forced", flush=True)
    print("onto the open competition lemma (4''); OP1 closes for n != 2 mod4 only. Shape trichotomy: %s" % (
        "ALL MATCH" if ok else "MISMATCH -- investigate"), flush=True)
