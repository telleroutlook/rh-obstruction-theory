# Novelty — Theorem E (E-compactness)

**Theorem ID:** E-compactness  
**Program ref:** §10.E, §14.3, LITERATURE_MATRIX.md §Paper C

---

## Position vs. prior art

### 1. Folklore: "finite numerics ≠ infinite theorem"

The observation that finite real-zero matching does not imply global convergence
is folklore.  What is **new** in E-compactness is:

- the **quantified per-`N` witness** in the exact CCM normalization (a record-respecting
  `F` with `sup_{|z|≤R_N}|F−Ξ| ≥ ε_N`, `R_N ≥ 2γ_{k_N+1}`);
- the **identified degree of freedom** (tail of the Hadamard product beyond `k_N`);
- the **positive sufficient package** (H-bound + H-tail + H-modulus) as a
  referee-grade checklist translating finite evidence into a rigorous convergence
  theorem.

The value is the CCM/Suzuki-specific packaging, not the abstract observation.

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

E-compactness has genuine new content:
- a precise **checklist** for the CCM convergence step (paper-quality);
- the **per-`N` non-identifiability** witness (Paper C main negative result);
- the **sufficient package** as the positive direction.

The negative theorem needs the quantitative §3 estimate before it is stronger
than a "slogan." Paper C is publishable once proof.md §3 is completed.
