#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6cj — the MECHANISM behind the §6ch/§6ci Row-3 split: Λ_w has a deeply-3-annihilated node-residue
class IFF n≡2 mod3.  Reduces Row 3a to a clean, m-independent Λ-lemma.

S_j = Λ(P_j), Λ(z^i)=w_i, P_j(z)=Π_{k≠j}(z−x_k).  At the deepest node (larger 3-adic class, size
≥⌈m/2⌉) P_{j*} ≡ (z−a)^{s−1}(z−b)^{m−s} mod 3.  Nodes x_t=(4t²−1)/(4t²+1) split into exactly two classes
mod 3: a₀≡0 (t≡1,2 mod3) and a₂≡2 (t≡0 mod3).  So v₃(S_{j*}) is governed by the VANISHING ORDER of Λ
on (z−a)^t: L_t(a) = Λ((z−a)^t) = Σ_i C(t,i)(−a)^{t−i} w_i.  Measured law:

    n≡1 mod3:  max_t v₃(L_t) = O(1) for BOTH classes (a₀→0, a₂→2–3, m-independent) ⇒ Row 3a p=3 floor.
    n≡2 mod3:  a₀-class deeply annihilated (max_t v₃(L_t) grows ~linearly in m); a₂→0 ⇒ Row 3b, no floor.

READING (L5): OP1 closes at p=3 for Row 3a MODULO the m-independent Λ-LEMMA "n≡1 mod3 ⇒ max_t v₃(Λ((z−a)^t))
=O(1) for both node residues" — a statement about w mod 3 alone (w=B⁻¹d), the clean next-proof nugget.
Row 3b (n≡2 mod3) remains the harder distributed-content problem (§6ch). RH stays [OUT].

THIS PROBE (EXACT, L9): report max_{t≤m−1} v₃(Λ((z−a)^t)) for a₀=x_1 (x≡0) and a₂=x_3 (x≡2) across
distinct Row-3 orbits n and m∈{10,14}; the a₀-column stays O(1) for n≡1 mod3 and grows for n≡2 mod3.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import comb

from discovery.probe_qmin_p2_floor_identity import wvec
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac
from discovery.probe_qmin_p2_nodd_ramified import rho_pqn


def v3f(x):
    return vp_frac(Fr(x), 3)


def max_vanishing(w, m, a):
    """max_{t<=m-1} v3(Lambda((z-a)^t)), Lambda(z^i)=w_i."""
    mx = 0
    for t in range(m):
        val = sum(Fr(comb(t, i)) * (-a) ** (t - i) * Fr(w[i]) for i in range(t + 1))
        if val != 0:
            mx = max(mx, v3f(val))
    return mx


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("§6cj: Λ_w deeply-3-annihilates a node-residue class IFF n≡2 mod3 (a₀=x≡0 class). RH [OUT].", flush=True)
    print("=" * 96, flush=True)

    # distinct-n Row-3 orbits (n≡2 mod4, 3∤n); dedup by n
    ORB = {10: Fr(3, 10), 14: Fr(1, 14), 22: Fr(1, 22), 26: Fr(1, 26),
           34: Fr(1, 34), 38: Fr(1, 38), 46: Fr(1, 46), 58: Fr(1, 58)}
    print("\n%-5s %4s | %-24s %-24s" % ("n", "n%3", "a₀ (x≡0) max_t v₃(L_t)", "a₂ (x≡2) max_t v₃(L_t)"), flush=True)
    print("  " + "-" * 70, flush=True)
    ok = True
    for n, sig in ORB.items():
        _, _, nn = rho_pqn(sig, Fr(1))
        assert nn == n
        cols = []
        for m in (10, 14):
            w = wvec(m, sig, Fr(1))
            cols.append((max_vanishing(w, m, x_of(1)), max_vanishing(w, m, x_of(3))))
        a0 = "m10=%2d m14=%2d" % (cols[0][0], cols[1][0])
        a2 = "m10=%2d m14=%2d" % (cols[0][1], cols[1][1])
        # law check: n%3==1 -> a0 O(1) (bounded, does not grow); n%3==2 -> a0 grows with m
        if n % 3 == 1:
            good = cols[1][0] <= 4          # a0 stays small at m=14
        else:
            good = cols[1][0] > cols[0][0]  # a0 grows from m=10 to m=14
        ok = ok and good
        print("%-5d %4d | %-24s %-24s  %s" % (n, n % 3, a0, a2, "ok" if good else "CHECK"), flush=True)

    print("\n" + "=" * 96, flush=True)
    print("LAW (%s): n≡1 mod3 ⇒ both classes O(1) (no annihilation) ⇒ Row 3a p=3 floor linear;" % (
        "ALL MATCH" if ok else "MISMATCH"), flush=True)
    print("n≡2 mod3 ⇒ a₀ class deeply annihilated ⇒ Row 3b, no p=3 floor. Row 3a reduces to the", flush=True)
    print("m-independent Λ-lemma (about w mod 3). Row 3b = distributed-content (§6ch). RH stays [OUT].", flush=True)
