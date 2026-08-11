# Novelty — Theorem E (E-compactness)

**Theorem ID:** E-compactness  
**Program ref:** §10.E, §14.3, LITERATURE_MATRIX.md §Paper C

---

## Position vs. prior art

### 1. Folklore: "finite numerics ≠ infinite theorem"

The observation that finite real-zero matching does not imply global convergence
is folklore.  What is **new** in E-compactness (after the OB-29 reframing) is:

- the **quantified per-`N` witness over an abstract Laguerre–Pólya target `L`** (a
  record-respecting `F` with `sup_{|z|≤R_N}|F−L| ≥ ε_N`, `R_N ≥ 2λ_{k_N+1}`), via the
  explicit scaled-Vandermonde IFT + Cauchy estimate — **RH-free because it never identifies
  `L` with `Ξ`**;
- the **identified degree of freedom** (tail of the Hadamard product beyond `k_N`);
- the **positive sufficient package** (H-bound + H-uorder + H-div) as a referee-grade
  checklist for what would translate finite evidence into convergence — **with (H-div) over
  `Ξ` explicitly flagged as an RH-strong hypothesis** (OB-29).

**NOT new / withdrawn (OB-29 BLOCKED):** the `Ξ`-specific RH-free version. Matching
`P_r(F_c)=P_r(Ξ)` needs `Ξ=Ξ(0)∏(1−z²/γ_n²)` over real `γ_n` = RH-via-divisor (L5); so the
"exact CCM normalization" packaging cannot be claimed RH-free. The genuine content is the
abstract-`L` lemma; the CCM/`Ξ` specialization is RH-conditional.

### 2. Standard complex analysis (Montel/Vitali/Hurwitz)

The positive theorem (E-pos) uses only classical tools.  The novelty is the
translation to the exact CCM normalization and the precise identification of which
conditions are missing in the published CCM paper (arXiv:2511.22755):
specifically, that the `λ^{−iz}` phase preserves zeros but not the locally
uniform limit, and that the "suitably normalized" condition is the load-bearing step.

### 3. Connes–van Suijlekom (CvS, Commun. Math. Phys. 406 (2025))

CvS prove real-zero results for Fourier transforms of extremal eigenfunctions
associated with lower-bounded quadratic forms, including finite truncations.
This is closely related to the CCM construction.  E-compactness adds the
convergence-boundary analysis to this real-zero framework.

**Delta:** CvS proves real zeros for finite objects; E-compactness explains why
that is insufficient for convergence to `Ξ` and what would suffice.

### 4. Suzuki (2606.09096, Cor 6)

Suzuki proves: convergence to `z² ξ/ξ'` ⟹ RH.  E-compactness does NOT
reprove this; it explains the convergence gap.  The Suzuki target is out of scope
for the current theorem (meromorphic; separate pole/residue argument needed).

---

## Delta summary

| Aspect | Prior art | E-compactness delta |
|---|---|---|
| Finite → global convergence impossible without tail | Folklore | Quantified in exact CCM normalization |
| Sufficient conditions for Ξ limit | Classical analysis | Packaged for CCM/CvS normalization |
| CCM "suitably normalized" meaning | Implicit in 2511.22755 | Made explicit: λ^{-iz} phase trap identified |
| Suzuki meromorphic target | Cor 6 as an implication | Out of scope; separate limitation recorded |

## Publication verdict

**GATE-A BLOCKED (OB-29) for the `Ξ`-specific RH-free claim.** After reframing to the
abstract Laguerre–Pólya target `L`, E has genuine but modest content:
- the **abstract-`L` per-`N` non-identifiability** witness (RH-free; the surviving negative
  result) — a supporting lemma, not a standalone barrier;
- the **conditional sufficiency package** (with (H-div) over `Ξ` flagged as RH-strong).

Positioned as a **Paper C supporting section** on real-zero-approximant non-identifiability,
NOT a standalone RH-free `Ξ`-theorem. Specializing to `Ξ`/CCM is RH-conditional and must be
labelled so. (OB-29 Q6: "supporting section, not standalone novelty".)
