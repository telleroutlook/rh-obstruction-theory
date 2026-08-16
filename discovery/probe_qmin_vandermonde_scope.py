#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6ce — SCOPE of the §6cd Vandermonde-coupling floor: is it a coverage-map UNIFICATION, or Row-2-specific?

The §6cd bound  v_p(q_min) ≥ 1 − profile_min(w; p)  is valid at ANY prime p where the nodes x_t are p-adic
UNITS (derivation needs only: §6bf identity, Lagrange V·u = w, unit nodes).  At p=2 all nodes x_t =
(4t²−1)/(4t²+1) are units regardless of orbit, so the bound holds for EVERY orbit.  This probe tests whether
it is non-vacuous (linear) across all n mod 4, i.e. whether §6cd collapses the 4-row map.

RESULT (see §6ce in op1_arithmetic_floor_findings.md): the bound is LINEAR only for n odd (profile_min(p=2)
≈ −3m/2); for n≡0 mod4 profile_min = +const (vacuous, though p=2 still carries via §6bm) and for n≡2 mod4
profile_min = +const AND p=2 does not carry (needs p=3 / ramified).  So §6cd is Row-2-specific; NOT a
unification.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

from discovery.probe_qmin_p2_floor_identity import wvec, qmin_exact_orbit
from discovery.probe_qmin_Cj_bilinear import vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def row_of(n):
    if n % 4 == 0:
        return "n≡0 mod4"
    if n % 2 == 1:
        return "n odd"
    if n % 6 == 0:
        return "6|n"
    return "n≡2 mod4,3∤n"


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6ce: scope of §6cd — floor 1−profile_min(p=2) across all n mod 4. Linear only for n odd? RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    SIGS = [Fr(1, 2), Fr(2, 3), Fr(3, 4), Fr(4, 5), Fr(5, 6), Fr(6, 7), Fr(3, 8), Fr(3, 10)]
    rng = random.Random(11)
    for sig in SIGS:
        tau = Fr(1)
        p, q, n = rho_pqn(sig, tau)
        print("\nσ=%s n=%d [%s]:" % (sig, n, row_of(n)), flush=True)
        for m in (4, 6, 8):
            w = wvec(m, sig, tau)
            pm = min(vp_frac(Fr(w[i]), 2) for i in range(m))
            wq = 10 ** 9
            for _ in range(15):
                ts = rng.sample(range(1, max(200, 14 * m)), m)
                if len(set(ts)) != m:
                    continue
                qm = qmin_exact_orbit(ts, m, sig, tau)
                if qm:
                    t, v = qm, 0
                    while t % 2 == 0:
                        t //= 2
                        v += 1
                    wq = min(wq, v)
            floor = 1 - pm
            tag = "LINEAR (carries)" if floor > 0 else ("VACUOUS bound" + (" & p=2 dead" if wq <= 6 else " but v2q linear via §6bm"))
            print("  m=%2d  profile_min(p=2)=%3d  §6cd_floor=%3d  min v2(q_min)=%3d  holds=%s  [%s]" % (
                m, pm, floor, wq, wq >= floor, tag), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("READING (L5): §6cd floor linear ⟺ profile_min(p=2) linearly negative ⟺ n odd. §6cd is Row-2-specific,", flush=True)
    print("NOT a coverage-map unification. Rows 1,3,4 keep their own mechanisms (§6bm; p=3; ramified). RH [OUT].", flush=True)
