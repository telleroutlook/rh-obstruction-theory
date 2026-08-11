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
the S(T) gap (Lemma G.2, REFEREED) gives d_n − γ_n = (S(γ_n)+1/2)/A'(ξ_n) + lower order
(corrected sign/term and denominator A'=θ'/π per OB-04; see G proof.md §3).
A perturbed multiset 𝒵_ε with ordinates d_n + ε̃_n (where ε̃_n ≈ γ_n − d_n) maps to
the same (d_n) sequence under O_theta. **Status: PROOF-DRAFT (Prop. G.3* Items 2–4
proved unconditionally, OB-04 2026-08-11).**

**Separation (Step B).** Same as §2 — Hadamard uniqueness. **Status: REFEREED.**

**Non-vacuity (Step C).** The kappa_toeplitz construction in 𝔐_FC gives a natural
method operating via O_theta. **Status: PROOF-DRAFT (Bochner positivity).**

---

## §4. Incomparability + coarsening (Theorem H', corrected OB-27)

**Claim (corrected).** `O_finite` and `O_theta` are **incomparable** (neither refines the
other); both are strict coarsenings of `O_oracle`. The earlier claim "O_finite ⊊ O_theta,
every finite collision is a theta collision" was **false** and is withdrawn.

*Why the old inclusion fails.* `O_theta` in the sense of Theorem G is the fixed, zero-free
archimedean sequence `d_n = θ_level(n)` (Riemann–Siegel θ, independent of the multiset 𝒵);
as a map on multisets it is constant, so it separates no pair and cannot dominate anything.
Even read charitably as a functional of 𝒵 (the θ-unfolded count of the imaginary parts), it
is blind to real parts.

*Incomparability, direction 1 (`O_theta` does not refine `O_finite`).* Two symmetric
quartets at the same height `T` but different real offset — `𝒵_a` at `σ=3/4`
(atoms `{3/4±iT, 1/4±iT}`) and `𝒵_b` at `σ=9/10` (atoms `{9/10±iT, 1/10±iT}`) — have the
identical imaginary-part multiset `{±T,±T}`, hence identical `O_theta`, but different
`O_finite`: `Li₁(𝒵) = Σ_ρ 1/ρ` gives `0.0199129…` vs `0.0198551…` (script-verified,
`T=10`). So `O_theta(𝒵_a)=O_theta(𝒵_b)` while `O_finite(𝒵_a)≠O_finite(𝒵_b)`.

*Incomparability, direction 2 (`O_finite` does not refine `O_theta`).* An S(T)-type
perturbation `γ_n → γ_n + ε_n` chosen in the kernel of the first K Li functionals (finite
matching, B1/B2 IFT) still moves the unfolded count, so `O_finite` collides while `O_theta`
separates. (Explicit finite matching: the B1 quartet decay + Vandermonde kernel of
§2/§3.)

*Coarsening (`O_finite ≺ O_oracle` and `O_theta ≺ O_oracle`).* The B2 quartet pair has
`O_finite(𝒵₊)=O_finite(𝒵₋)` (exact Li collision, B2 §4.3 — Gate-A PASS OB-20) but distinct
ordinates, so `O_finite ≺ O_oracle`. By Lemma G.2, an S(T) perturbation with
`ε_n` bounded by `S(γ_n)/A'(γ_n)` (`A'(t)=θ'(t)/π`) preserves `O_theta` but changes the
ordinates, so `O_theta ≺ O_oracle`. **Status: part (ii) inherits the exact B2/G collisions
(firm); part (i)'s two witnesses are explicit but not yet independently checked.**

---

## §5. Summary

The key insight is that all three theorems (B2, G, and the abstract H) share:
- **Same analytic tool:** Hadamard uniqueness for order-1 entire functions.
- **Same IFT structure:** finite evidence matched by perturbed multiset via Vandermonde Jacobian.
- **Same growth argument:** |Ξ(Ri)| → ∞ from Hadamard product.
- **Different kernels:** B2 uses the Li/Weil finite kernel; G uses the S(T) archimedean kernel.

Theorem H unifies these by naming the maps and making the **partial-order** structure
explicit: `O_finite` (B2) and `O_theta` (G) are **incomparable** obstruction layers, both
strict coarsenings of `O_oracle` (§4, corrected OB-27). The unification value is the common
template + the precise placement of each obstruction; the earlier "strict linear hierarchy"
was withdrawn.
