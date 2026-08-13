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

## §4. Incomparability (Theorem H'(i), corrected OB-34 — INDEPENDENTLY-CHECKED)

**Historical note (OB-27/OB-32).** The original claim "O_finite ⊊ O_theta" was withdrawn.
Theorem G's literal `O_theta(𝒵) = d_n = θ_level(n)` is a fixed, 𝒵-independent sequence and
hence a constant map; a constant map refines every map, giving `O_theta ≺ O_finite` (strictly
coarser, not incomparable). Genuine incomparability requires the nonconstant sampled-count
map `O_theta^{samp}`.

**Setup (M1).** Fix integers K≥1 and M≥1, and fix real sampling levels 0<d₁<…<d_M. Let
ℌ_sym be the class of finite multisets contained in {ρ∈ℂ : 0<Re ρ<1}, invariant with
multiplicity under ρ↦ρ̄ and ρ↦1−ρ. (Requiring 0<Re ρ<1 ensures φ_j(ρ) and φ_j(1−ρ) are
well-defined for every element; in particular 0 and 1 are excluded.)

**Normalization (M2).** Because 𝒵 is reflection-symmetric,
`Li_j(𝒵) = 2∑_{ρ∈𝒵} φ_j(ρ)`; in particular `Li₁(𝒵) = 2∑_{ρ∈𝒵} 1/ρ`. Conjugation
symmetry makes these values real.

**B2 citation (M3).** For every m≥1, Theorem B2 in `OB-02-B2-integer-collision.md`,
Lemmas 3.1 and 4.1 and equations (5.1)–(5.8), constructs an exact collision for the specific
Li family φ_j, j=1,…,m, at σ₀=3/4. Its normalization agrees with the present one on ℌ_sym.
The independent exact replay `OB-13-B2-independent-exact-reconstruction.md`, Lemmas 2.1–2.3
and V1–V5, checks the normalization and the explicit m=2,3 instances. No claim is made here
for an arbitrary finite family of unrelated test functions.

**Witness 1 — `O_finite^{(K)} ⋠ O_theta^{samp}`.** Two symmetric quartets at height T=10
but different real offset: 𝒵_a = Q(3/4,10) = {3/4±10i, 1/4±10i} and 𝒵_b = Q(9/10,10) =
{9/10±10i, 1/10±10i}. Both have imaginary-part multiset {±10,±10}, so N_{𝒵_a}(u) =
N_{𝒵_b}(u) at every level u, giving `O_theta^{samp}(𝒵_a) = O_theta^{samp}(𝒵_b)` (equal).

By the double-counting normalization (M2, M4):

  Li₁(Q(3/4,10)) = 102592/2576009 ≈ 0.039825947813…
  Li₁(Q(9/10,10)) = 4003600/100820081 ≈ 0.039710343022…
  (Exact difference = 30024117552/259713436036729 > 0, script-verified with exact rationals.)

(Note: the per-atom sums S(3/4,10)=51296/2576009 and S(9/10,10)=2001800/100820081 are half
these values — the correct Li₁ applies the reflection factor 2 per M2.) Since Li₁ values
differ, `O_finite^{(K)}(𝒵_a) ≠ O_finite^{(K)}(𝒵_b)`, so `O_finite^{(K)} ⋠ O_theta^{samp}`.

**Witness 2 — `O_theta^{samp} ⋠ O_finite^{(K)}` (all K, M5, M6).** Fix K≥1. From Theorem B2
(σ₀=3/4), B2 produces 𝒵₊ (on-line atoms {1/2±it_k}, multiplicity M₀) and 𝒵₋ carrying
additionally the off-line quartet Q(3/4,T)^{(R)}. The B2 exact collision gives:

  `O_finite^{(K)}(𝒵₊) = O_finite^{(K)}(𝒵₋)` exactly for every j=1,…,K

(with a new B2 pair chosen for each fixed K).

For the sampling separation, we invoke the **non-cancellation parameter selection lemma**:

> **Lemma (M6).** Fix K≥1 and d_*>0. One can choose rational numbers 0<t₁<…<t_K<T<d_*
> such that the B2 vector β = −C⁻¹q(T) satisfies
>   G_K(t₁,…,t_K,T) := 2 + ∑_{k=1}^K β_k ≠ 0.
>
> *Proof.* For fixed distinct positive t_k, as T→∞, φ_j(a+iT)→0, hence q(T)→0, β→0,
> G_K→2. So G_K is not identically zero as a rational function of parameters. If it were
> zero on the open set U_{d_*} = {0<t₁<…<t_K<T<d_*}, clearing denominators would give a
> polynomial zero on an open set, hence the zero polynomial — contradicting G_K→2. So G_K≠0
> somewhere in U_{d_*}; non-zero is an open condition and rational points are dense, so
> parameters can be chosen rational. □

Choose parameters by the lemma with d_* = d₁ (placing all atoms below d₁). Then:

  N_{𝒵₋}(d₁) − N_{𝒵₊}(d₁) = 2∑_k n_k + 4R = 2R(∑_k β_k + 2) = 2R·G_K ≠ 0.

So `O_theta^{samp}(𝒵₊) ≠ O_theta^{samp}(𝒵₋)` while `O_finite^{(K)}(𝒵₊) = O_finite^{(K)}(𝒵₋)`:
`O_theta^{samp} ⋠ O_finite^{(K)}`. The key is that **parameters can be chosen** to avoid
cancellation; this is not automatic for every B2 pair — exact rational counter-example at
K=2, t₁=1/24, t₂=9/40, T=3/8 gives G_K=0 (OB-34 verdict §5.2).

**Theorem G / constant observation (M7).** The levels d_n defined from θ in Theorem G are
fixed and 𝒵-independent. If one defines the observation O_const(𝒵) := (d_n), then O_const
is constant and hence strictly coarser than the nonconstant O_finite^{(K)}. This constant
map is not O_theta^{samp}.

**Corrected Theorem H'(i) (M8).** Fix M≥1 and positive levels 0<d₁<…<d_M. On the corrected
class ℌ_sym, for every K≥1, `O_finite^{(K)} ⋈ O_theta^{samp}`. The first non-refinement is
witnessed by the same-height quartets; the reverse non-refinement is witnessed by a B2 pair
selected using the non-cancellation lemma above. This is an RH-free statement about finite
artificial multisets and an information-refinement preorder, not a standalone analytic barrier.

**Coarsening (`O_finite ≺ O_oracle` and `O_theta^{samp} ≺ O_oracle`).** The B2 quartet pair has
`O_finite(𝒵₊)=O_finite(𝒵₋)` (exact Li collision, Theorem B2, Gate-A PASS OB-20) but
`𝒵₊ ≠ 𝒵₋`, so `O_finite ≺ O_oracle`. For `O_theta^{samp}`: by the non-cancellation lemma,
`O_theta^{samp}(𝒵₊) ≠ O_theta^{samp}(𝒵₋)` for the chosen parameters, so the B2 collision is
not an `O_theta^{samp}`-collision; hence `O_theta^{samp} ≺ O_oracle` as well.

**Status: INDEPENDENTLY-CHECKED (OB-34 Gate-A CONDITIONAL → integrated 2026-08-13, M1–M8).**

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
