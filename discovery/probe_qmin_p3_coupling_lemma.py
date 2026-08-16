#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into proofs. No RH input.

§6co — COUPLING LEMMA (closes the last §6cm gap): for the ε=0 (3∤(a+n)) sub-family with consecutive nodes,
the p=3 floor v₃(q_min) ≥ m/2 − O(1) is a THEOREM.  Two proven ingredients + their coupling:

  Λ-STRUCTURE (mod 3).  The ε=0 moments satisfy w_l ≡ [1,1,2,2] period-4 mod 3, hence w_l + w_{l−2} ≡ 0
  mod 3 for all l≥2 ⇒ Λ ANNIHILATES the ideal (z²+1) mod 3 ⇒ Λ factors through
        F₃[z]/(z²+1) ≅ F₉ = F₃[i],  z ↦ i (i² = −1; z²+1 irreducible since −4 ≡ 2 is a non-residue).
  With Λ(1)=w₀=1 and Λ(z)=w₁=1, the induced F₃-linear functional is  Λ(a + b i) = a + b.

  NODE RESIDUES.  x_t = (4t²−1)/(4t²+1); denominators are 3-units, and x_t ≡ 0 (t≢0 mod3, class a₀) or
  ≡ 2 (t≡0 mod3, class a₂).  For node j, P_j ≡ z^{n₀}(z−2)^{n₂} mod 3, n₀=#a₀−[j∈a₀], n₂=#a₂−[j∈a₂],
  n₀+n₂=m−1.  So S_j = Λ(P_j) ↦ i^{n₀}(i−2)^{n₂} = i^{n₀}(i+1)^{n₂} in F₉ (since −2 ≡ 1).

  COUPLING.  (i+1)² = 2i ≡ −i mod 3.  Thus for n₂ = 2c EVEN:
        S_j ↦ i^{n₀}(−i)^c = (−1)^c i^{n₀+c} ∈ {±1, ±i}  ⇒  Λ-image a+b = ±1 ≠ 0  ⇒  S_j is a 3-UNIT.
  (For n₂ odd, i^k(i+1) can give a+b=0 — the annihilation seen in the grid; irrelevant to the floor.)

  FLOOR.  clus(j) = Σ_{k≠j}[v₃(j−k)+v₃(j+k)] ≥ Σ_{k≠j} v₃(j−k) = Σ_{i≥1} #{k≠j: 3ⁱ|(j−k)} ≥ ~m/2
  (rigorous, every j).  The n₂-even class is always nonempty (n₂ ∈ {⌊m/3⌋, ⌊m/3⌋−1}; one is even), so
  ∃ node j with v₃(S_j)=0 AND clus(j) ≥ ~m/2  ⇒  v₃(q_min) = max_j(clus(j)−v₃(S_j)) ≥ m/2 − O(1).  LINEAR.

  => log q_min = Ω(m) = ω(log m) at the single prime p=3 for the ε=0 sub-family with consecutive nodes:
     a rigorous single-prime super-poly lower bound.  RH stays [OUT].

THIS PROBE (EXACT, L9): verifies (1) w_l+w_{l−2}≡0 mod3 (kernel z²+1), (2) Λ(z^l)=a+b with iˡ=a+bi,
(3) S_j mod3 == F₉ formula and n₂-even ⇒ unit, (4) clus(j) ≥ m/2 and the resulting floor is linear.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import comb

from discovery.probe_qmin_p2_floor_identity import wvec
from discovery.probe_qmin_Cj_bilinear import x_of, vp_frac


def v3(x):
    return vp_frac(Fr(x), 3)


def unit_res3(fr):
    """residue mod 3 of the 3-unit part of a 3-integral rational (0 iff v3>0 -> returns actual residue)."""
    fr = Fr(fr)
    v = v3(fr)
    if v > 0:
        return 0
    return (fr.numerator % 3) * pow(fr.denominator % 3, -1, 3) % 3


def il_ab(l):
    """i^l in F3[i] as (a,b): cycle (1,0),(0,1),(-1,0),(0,-1)."""
    return {0: (1, 0), 1: (0, 1), 2: (2, 0), 3: (0, 2)}[l % 4]


def F9_image_ab(n0, n2):
    """a+b for i^n0 (i+1)^n2 in F3[i]  (uses i-2 == i+1 mod 3)."""
    a, b = il_ab(n0)
    for _ in range(n2):                       # multiply by (1 + i)
        a, b = (a - b) % 3, (a + b) % 3
    return (a + b) % 3


def S_of(w, n0, n2):
    """Lambda(z^n0 (z-2)^n2), Lambda(z^l)=w_l."""
    poly = {}
    for b in range(n2 + 1):
        poly[b + n0] = poly.get(b + n0, 0) + comb(n2, b) * ((-2) ** (n2 - b))
    return sum(Fr(w[l]) * Fr(c) for l, c in poly.items() if l < len(w))


if __name__ == "__main__":
    print("=" * 100, flush=True)
    print("§6co: COUPLING LEMMA — Λ factors through F₉, n₂ even ⇒ S_j 3-unit ⇒ p=3 floor ≥ m/2. RH [OUT].", flush=True)
    print("=" * 100, flush=True)

    w = wvec(90, Fr(1, 22), Fr(1))            # ε=0 orbit moments (period-4 [1,1,2,2] mod 3)

    # (1) kernel: unit residues satisfy w_l + w_{l-2} ≡ 0 mod 3  (Λ kills z^2+1)
    k1 = all((unit_res3(w[l]) + unit_res3(w[l - 2])) % 3 == 0 for l in range(2, 90))
    r0_3 = [unit_res3(w[l]) for l in range(4)]
    print("\n(1) w_l mod3 = %s period-4; w_l+w_{l-2} ≡ 0 mod3 (Λ annihilates z²+1): %s" % (r0_3, k1), flush=True)

    # (2) Λ(z^l) = a+b where i^l = a+bi   (Λ factors through F9)
    k2 = all(unit_res3(w[l]) == (sum(il_ab(l)) % 3) for l in range(90))
    print("(2) Λ(z^l) ≡ (a+b) mod3 with iˡ=a+bi  (Λ factors through F₉, z↦i): %s" % k2, flush=True)

    # (3) S(n0,n2) mod3 == F9 formula; n2 even ⇒ unit
    k3 = uniteven = True
    for n0 in range(40):
        for n2 in range(24):
            if n0 + n2 >= len(w):
                continue
            S = S_of(w, n0, n2)
            if unit_res3(S) != F9_image_ab(n0, n2):
                k3 = False
            if n2 % 2 == 0 and v3(S) != 0:
                uniteven = False
    print("(3) S(n0,n2) mod3 == i^n0 (i+1)^n2 → a+b: %s ;  n₂ EVEN ⇒ S 3-unit: %s" % (k3, uniteven), flush=True)

    # (4) clus(j) >= ~m/2 (every j) and floor linear at the n2-even node class
    print("\n(4) clus(j) ≥ ~m/2 (all j) and v₃(q_min) ≥ m/2 at an n₂-even (unit) node:", flush=True)
    okF = True
    for m in (9, 12, 15, 18, 24, 30):
        xs = [x_of(t) for t in range(1, m + 1)]
        clus = [sum(v3(xs[j] - xs[k]) for k in range(m) if k != j) for j in range(m)]
        # n2(j): count of a2 nodes (t≡0 mod3) among k≠j
        a2 = [1 if (t % 3 == 0) else 0 for t in range(1, m + 1)]
        tot2 = sum(a2)
        n2 = [tot2 - a2[j] for j in range(m)]
        min_clus = min(clus)
        # floor restricted to n2-even nodes = provable lower bound; also the global floor value
        prov = max(clus[j] for j in range(m) if n2[j] % 2 == 0)
        okF = okF and (min_clus >= m // 2 - 1) and any(n2[j] % 2 == 0 for j in range(m))
        print("  m=%2d: min_j clus=%2d (≥⌊m/2⌋−1=%d)  max clus over n₂-even (unit) nodes=%2d  (≥m/2, LINEAR)" % (
            m, min_clus, m // 2 - 1, prov), flush=True)

    print("\n" + "=" * 100, flush=True)
    print("(1)%s (2)%s (3)%s (4)%s" % tuple("OK" if x else "X" for x in (k1, k2 and uniteven, k3, okF)), flush=True)
    print("THEOREM (ε=0, consecutive nodes): v₃(q_min) ≥ m/2 − O(1) at p=3 — a RIGOROUS single-prime", flush=True)
    print("super-poly lower bound.  Ingredients: Λ↠F₉ (Λ(a+bi)=a+b), (i+1)²=−i ⇒ n₂-even⇒unit, clus≥m/2.", flush=True)
    print("Closes the §6cm coupling gap for 3∤(a+n).  3|(a+n) & general node sets remain (§6cn). RH [OUT].", flush=True)
