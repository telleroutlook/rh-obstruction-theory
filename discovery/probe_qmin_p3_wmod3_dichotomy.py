#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6ck — the ROOT CAUSE of the Row-3 OP1 dichotomy: the residue of the moment vector w=B⁻¹d mod 3.

    FACT 3a (n≡1 mod3): every w_i is a 3-UNIT, unit residues = period-4 pattern [1,1,2,2,...].
        ⇒ W(y)=Σ w_i y^i mod 3 is a unit-coefficient (w_0=1) polynomial; via
        F(s)=Σ_t Λ((z−a)^t)s^t = W(s/(1+sa))/(1+sa), the vanishing order of Λ on (z−a)^t = root
        multiplicity of W mod 3 at a's Möbius image = bounded (≤3 obs; at worst O(log₃ m), SUBLINEAR).
        ⇒ v₃(S_j)=o(m) for both node residues ⇒ v₃(q_min)=max_j clus(j)−o(m) ≥ ⌈m/2⌉−1−o(m), LINEAR.
    FACT 3b (n≡2 mod3): w_0 unit but w_i ≡ 0 mod 3 for EVERY i≥1 ⇒ Λ(f) ≡ w_0 f(0) mod 3 exactly ⇒
        Λ((z−a)^t) ≡ w_0(−a)^t: annihilates a₀≡0 class (deep), unit on a₂≡2 ⇒ no p=3 floor (Row 3b).

READING (L5): n mod 3 controls whether w mod 3 is a full-support period-4 unit vector (3a: LINEAR p=3
floor) or a w_0-only vector (3b: Λ=eval₀ mod 3, a₀ annihilated, no p=3 floor). Row 3a p=3 CLOSES modulo
the PROVABLE FACT 3a (period-4 unit pattern of w=B⁻¹d mod 3, echoing the p=2 period-4 of FACT A §6br).
Row 3b lives at distributed primes (§6ch). RH stays [OUT].

THIS PROBE (EXACT, L9): verify FACT 3a and FACT 3b across distinct Row-3 orbits n × m∈{8,12,16}.
"""
from __future__ import annotations
from fractions import Fraction as Fr

from discovery.probe_qmin_p2_floor_identity import wvec
from discovery.probe_qmin_Cj_bilinear import vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def v3f(x):
    return vp_frac(Fr(x), 3)


def unit_residue_mod3(f):
    """unit part of f (a 3-unit or 3-integral) reduced mod 3."""
    v = v3f(f)
    u = f * Fr(3) ** (-v)
    return (u.numerator * pow(u.denominator, -1, 3)) % 3


if __name__ == "__main__":
    print("=" * 92, flush=True)
    print("§6ck: root cause — w=B⁻¹d mod 3 dichotomy (period-4 units vs w_0-only) by n mod 3. RH [OUT].", flush=True)
    print("=" * 92, flush=True)

    ORB = {10: Fr(3, 10), 14: Fr(1, 14), 22: Fr(1, 22), 26: Fr(1, 26), 34: Fr(1, 34),
           38: Fr(1, 38), 46: Fr(1, 46), 58: Fr(1, 58), 50: Fr(1, 50)}
    PERIOD4 = [1, 1, 2, 2]
    ok3a = ok3b = True
    for n, sig in ORB.items():
        _, _, nn = rho_pqn(sig, Fr(1))
        assert nn == n
        tag = None
        for m in (8, 12, 16):
            w = wvec(m, sig, Fr(1))
            vs = [v3f(Fr(w[i])) for i in range(m)]
            if n % 3 == 1:
                good = all(v == 0 for v in vs) and all(
                    unit_residue_mod3(Fr(w[i])) == PERIOD4[i % 4] for i in range(m))
                ok3a = ok3a and good
                tag = "3a: all units & period-4 [1,1,2,2] -> %s" % ("ok" if good else "FAIL")
            else:
                good = vs[0] == 0 and all(vs[i] >= 1 for i in range(1, m))
                ok3b = ok3b and good
                tag = "3b: w_0 unit, w_i≡0 mod3 (i≥1) -> %s   (v₃=%s)" % (
                    "ok" if good else "FAIL", vs)
        print("  n=%-3d (n%%3=%d)  %s" % (n, n % 3, tag), flush=True)

    print("\n" + "=" * 92, flush=True)
    print("FACT 3a (n≡1 mod3: all w_i 3-units, unit-residue period-4 [1,1,2,2]): %s" % (
        "HOLDS" if ok3a else "FALSE"), flush=True)
    print("FACT 3b (n≡2 mod3: w_0 unit, w_i≡0 mod3 ∀i≥1 ⇒ Λ=w_0·eval_0 mod3): %s" % (
        "HOLDS" if ok3b else "FALSE"), flush=True)
    print("⇒ Row-3a p=3 close rests on FACT 3a (provable from w=B⁻¹d mod 3); Row 3b = distributed (§6ch). RH [OUT].", flush=True)
