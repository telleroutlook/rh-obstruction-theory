# Proof — Theorem H (H-information-hierarchy)

**Status:** PROOF-DRAFT  
**Analytic / finite separation:** purely analytic.

---

## §1. The common template

All information obstructions in this repo share the same three-step structure:

**Step A (collision construction).** Given observation layer L, construct a perturbed
zero multiset 𝒵' ≠ 𝒵_RH such that L(𝒵') = L(𝒵_RH) — the perturbation is in the
kernel of L.

**Step B (target separation).** Show that the entire functions F_{𝒵'} and F_{𝒵_RH}
are distinct — by Hadamard uniqueness (Lemma G.1 / Lemma E'.1), two distinct zero
multisets give distinct order-1 entire functions.

**Step C (non-vacuity of collision).** Show that 𝒵' is a non-trivial admissible
multiset (not just a formal construction), by verifying it lies in 𝔛_sym and the
perturbation is concrete.

---

## §2. Instantiation for O_finite (inherits from B2)

**Collision (Step A).** The B2 quartet Q(σ₀,T) provides an off-critical-line zero
multiset 𝒵_- such that, for the finite observation vector
`v_K = (Li_1(𝒵), …, Li_K(𝒵))` (first K Li-type values), we have `v_K(𝒵_-) = v_K(𝒵_+)`.
The Jacobian rank theorem (B2 §4.3, self-contained Vandermonde reduction) proves the
collision is exact and not accidental. **Status: PROOF-DRAFT (B2).**

**Separation (Step B).** 𝒵_+ and 𝒵_- differ in the position of at least one zero
(off vs. on critical line). By Hadamard uniqueness, the corresponding entire functions
differ. **Status: PROOF-DRAFT (inherits Lemma G.1).**

**Non-vacuity (Step C).** The B2 quartet is an explicit construction in 𝔛_sym with
real zero ordinates and complex-conjugate symmetry. **Status: PROOF-DRAFT (B2 §4.5).**

---

## §3. Instantiation for O_theta (inherits from G)

**Collision (Step A).** For the theta-level observation O_theta: n → d_n = θ_level(n),
the S(T) gap (Lemma G.2, REFEREED) gives γ_n − d_n = S(γ_n)/N'(γ_n) + lower order.
A perturbed multiset 𝒵_ε with ordinates d_n + ε̃_n (where ε̃_n ≈ γ_n − d_n) maps to
the same (d_n) sequence under O_theta. **Status: PROOF-DRAFT (G Prop. G.3 open step).**

**Separation (Step B).** Same as §2 — Hadamard uniqueness. **Status: REFEREED.**

**Non-vacuity (Step C).** The kappa_toeplitz construction in 𝔐_FC gives a natural
method operating via O_theta. **Status: PROOF-DRAFT (Bochner positivity).**

---

## §4. Proof of strict separation (Theorem H')

**Claim.** O_finite ⊊ O_theta as information classes: every O_theta-collision is an
O_finite-collision, but not vice versa.

*Proof of O_finite ⊆ O_theta (every finite collision is a theta-level collision).*
Any collision pair (𝒵₊, 𝒵₋) with the same finite Li values in particular has the same
first K Li values for every K. Whether they also have the same theta-levels d_n depends
on the construction. The B2 quartet has 𝒵₋ with an off-critical-line zero at σ₀ ≠ 1/2;
its n-th theta level is d_n^{(𝒵₋)} = θ⁻¹(πn) evaluated in the multiset metric, which
differs from d_n^{(𝒵_RH)} because the zero counts disagree.

Specifically: if 𝒵₋ has a zero at ρ₁ = σ₀ + iγ₁ with σ₀ > 1/2, then the counting
function N_{𝒵₋}(T) has a different shape near T = γ₁ than N_{𝒵_RH}(T), so their
theta-level sequences {d_n^{(𝒵₋)}} differ from {d_n^{(𝒵_RH)}} at the n-th level
near n = θ(γ₁)/π + 1. Thus O_theta(𝒵₋) ≠ O_theta(𝒵_RH) even though the B2 finite
Li values coincide. **Status: PROOF-DRAFT** (explicit d_n computation open).

*Proof of O_theta ⊊ O_oracle.* By Lemma G.2, two multisets related by an S(T)
perturbation γ_n → γ_n + ε̃_n (where ε̃_n is in the kernel of O_theta) have the
same theta-level sequence but different oracle outputs {γ_n}. **Status: PROOF-DRAFT
(Prop. G.3 open step).**

---

## §5. Summary

The key insight is that all three theorems (B2, G, and the abstract H) share:
- **Same analytic tool:** Hadamard uniqueness for order-1 entire functions.
- **Same IFT structure:** finite evidence matched by perturbed multiset via Vandermonde Jacobian.
- **Same growth argument:** |Ξ(Ri)| → ∞ from Hadamard product.
- **Different kernels:** B2 uses the Li/Weil finite kernel; G uses the S(T) archimedean kernel.

Theorem H unifies these by naming the layers and making the inclusion structure explicit.
