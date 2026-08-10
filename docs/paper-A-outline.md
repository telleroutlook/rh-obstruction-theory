# Paper A — Outline
# Finite Observables Do Not Determine Critical-Line Support

**Working title:** Finite Observables Do Not Determine Critical-Line Support  
**Target:** ~15 pages; research note or short paper  
**Theorem files:** `theorems/B1-finite-inequality/`, `theorems/B2-exact-collision/`  
**Status:** PROOF-DRAFT complete; both theorems self-contained; ready for independent review

---

## Abstract (draft)

We prove two information-theoretic obstruction theorems for methods that observe
only finitely many values of a test family (Li coefficients, Weil sums, or moments)
computed at the zeros of a zeta-like function.

**Theorem B1 (strict finite-inequality non-discrimination):** For any finite family
Φ = (φ₁, …, φ_m) of Li/Weil-W2/Hausdorff test functions and any K, there exist two
admissible zero multisets 𝒵₊ (all zeros on the critical line) and 𝒵₋ (containing an
off-line zero) such that the finite observation vector O_Φ(𝒵₊) = O_Φ(𝒵₋) exactly and
all the first K Li inequalities λⱼ ≥ 0 hold for both.

**Theorem B2 (exact observation collision):** Under the same hypotheses, 𝒵₊ and 𝒵₋
can be chosen so that O_Φ(𝒵₊) = O_Φ(𝒵₋) exactly (not just up to a small error),
with 𝒵₊ consisting of on-line pairs and 𝒵₋ additionally containing an off-line quartet.

These results show that no method relying only on the finite observation O_Φ can
distinguish between the two multisets — the predicate "all zeros on the critical line"
is not a function of the observation. The obstruction is structural (the observation
map has a non-trivial kernel on the relevant class) and applies regardless of the
truth of the Riemann Hypothesis.

---

## §1. Introduction and context

**What the paper does not claim.** This paper does not prove, disprove, or make
progress toward RH. The results are about a *class of methods* — those using only a
finite observation O_Φ — not about RH itself. The obstruction is to the method class,
not to the mathematical question.

**Relation to prior work.** The Li criterion (Li 1997) shows that RH is equivalent
to λⱼ ≥ 0 for all j. Our results show that any *finite* truncation λ₁, …, λ_K ≥ 0
does not distinguish on-line from off-line zero configurations. Bombieri–Lagarias
(1999) noted a related limitation for finite Li evaluations; our result is exact
(zero tolerance, integer multiplicities) rather than approximate.

---

## §2. Setup

- **Ambient class 𝔛_sym:** locally finite zero multisets in the critical strip,
  symmetric under complex conjugation and ρ ↦ 1−ρ, with admissibility exponent bound.
  Membership is checkable; the formal Riemann zero multiset is a member.
- **Test family Φ:** Li-type φⱼ(ρ) = 1 − (1−1/ρ)ʲ; Weil-W2 ĥ(Im ρ); moment ρ⁻ʲ.
- **Observation map O_Φ(𝒵):** the vector of symmetrized sums.
- **Off-line quartet Q(σ₀, T):** four zeros at σ₀ ± iT, 1−σ₀ ± iT with σ₀ = 3/4.
- **On-line compensating pairs:** {1/2 ± itₖ} with rational tₖ, integer multiplicity αₖ.

---

## §3. Theorem B1 (strict finite-inequality non-discrimination)

**Statement.** For any m and any K, there exist 𝒵₊, 𝒵₋ ∈ 𝔛_sym with:
- O_Φ(𝒵₊) = O_Φ(𝒵₋) (exact equality for all m tests).
- All first K Li inequalities hold for both.
- P(𝒵₊) = 1, P(𝒵₋) = 0 (predicate differs).

**Proof sketch.** Off-line quartet Q(σ₀, T) contributes δʲᵒᶠᶠ(T) → 0 as T → ∞
(Riemann-Lebesgue for W2; power decay for moments; direct estimate for Li-W1).
Choose T large so |δʲᵒᶠᶠ(T)| < ε for all j. The inequalities are strict for
𝒵₊; by continuity they remain strict for 𝒵₋ after adding the small quartet.

**Limitations.** Fixed K only; no K → ∞ claim; the theorem does not use or imply
any K → ∞ behavior of the Li coefficients for ζ.

---

## §4. Theorem B2 (exact observation collision)

**Statement (conditional on admissibility of the constructed 𝒵₊).** There exist
𝒵₊, 𝒵₋ ∈ 𝔛_sym with O_Φ(𝒵₊) = O_Φ(𝒵₋) exactly, P(𝒵₊) = 1, P(𝒵₋) = 0,
and all αₖ ∈ ℤ (integer multiplicities).

**Proof sketch.**
1. Choose n = m rational heights t₁, …, tₘ > 0. The Jacobian Jⱼₖ = φⱼ(1/2+itₖ) +
   φⱼ(1/2−itₖ) has det J ≠ 0 by a self-contained Vandermonde reduction:
   Jⱼₖ = 2(1−cos(jθₖ)) = 2(1−Tⱼ(xₖ)) = 2(1−xₖ)Qⱼ(xₖ); the matrix [Qⱼ(xₖ)] =
   U·V(x₁,…,xₘ) with upper-triangular U and Vandermonde V, both nonsingular.
2. The target b = −δᵒᶠᶠ(T) ∈ ℚᵐ for rational T; solve α^ℚ = J⁻¹b ∈ ℚᵐ.
3. Scale by R = lcm(denominators): integer vector Rα^ℚ ∈ ℤᵐ.
4. Construct 𝒵₊ with multiplicity buffer M = R·maxₖ|αₖ^ℚ| at each height; all
   removals in 𝒵₋ are valid by construction.
5. Observation equality: J(Rα^ℚ) + Rb = 0 by construction. ✓

**Explicit limitation.** The collision pair (𝒵₊, 𝒵₋) uses a *constructed* 𝒵₊
(not the Riemann zero multiset). The theorem asserts existence of an indistinguishable
pair in 𝔛_sym, not that ζ's zeros are indistinguishable from an off-line configuration.

---

## §5. Escape routes

The obstruction applies only to the class of methods with fixed finite observation O_Φ.
The following escape routes are identified:

1. **Infinite test hierarchy:** using all Li coefficients (K → ∞).
2. **Euler product:** methods using the multiplicative structure of ζ (Selberg class axioms).
3. **Gamma factor / analytic continuation:** archimedean data not captured by O_Φ.
4. **Coefficient arithmetic:** integrality and positivity of Dirichlet coefficients.
5. **Integer-multiplicity retraction:** if the rank condition fails for some test family,
   B2 retracts to B1 (the inequality theorem is unconditional).

---

## §6. Novelty statement

The exact collision construction (B2) with integer multiplicities and zero tolerance
appears to be new. B1 (finite-inequality non-discrimination) is related to known
limitations of finite Li evaluations (Bombieri–Lagarias type) but is stated here in
the abstract 𝔛_sym class with an explicit escape route list. The self-contained
Vandermonde rank proof is elementary and requires no T-system theory citation.

---

## §7. Submission target

- **Venue (provisional):** Acta Arithmetica / Journal of Number Theory (short note)
- **Length:** ~15 pages
- **Dependencies for submission:** independent review of B2 Vandermonde argument;
  confirmation that the multiplicity-buffer construction does not require 𝒵₊ = ζ zeros.
