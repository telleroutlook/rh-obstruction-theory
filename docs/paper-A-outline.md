# Paper A — Outline
# Finite Observables Do Not Determine Critical-Line Support

**Working title:** Finite Observables Do Not Determine Critical-Line Support  
**Target:** ~15 pages; research note or short paper  
**Theorem files:** `theorems/B1-finite-inequality/`, `theorems/B2-exact-collision/`  
**Status:** **INDEPENDENTLY-CHECKED** — both B1 (Gate-A PASS OB-23, after §7 mods) and B2
(Gate-A PASS OB-20) passed whole-theorem independent Gate-A review; both have deposited
independent checkers (B1 R-atom OB-24; B2 OB-21/OB-13). This is the strongest-standing paper:
two double-axis-established obstruction theorems. (G-info, Paper-A-adjacent, is also
Gate-A PASS OB-22 + checker OB-17 — see docs/STATUS.md.)

---

## Abstract (draft)

We prove two information-theoretic obstruction theorems for methods that observe
only finitely many values of a test family (Li coefficients, Weil sums, or moments)
computed at the zeros of a zeta-like function.

**Theorem B1 (strict finite-inequality non-discrimination):** For any finite family
Φ = (φ₁, …, φ_m) of Li/Weil-W2/Hausdorff test functions and any K, there exist two
admissible zero multisets 𝒵₊ (with predicate P=1) and 𝒵₋ (P=0, containing an off-line
zero) such that the finite observation vector O_Φ(𝒵₊) = O_Φ(𝒵₋) exactly and
all the first K Li inequalities λⱼ ≥ 0 hold for both. (`𝒵₊` ranges over abstract P=1
members — e.g. explicit finite on-line multisets; the instantiation "𝒵₊ = the ζ zero
multiset" is conditional on RH and is *not* used, per OB-23 §7.1.)

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

## §4bis. (Optional) Theorem G-info — the archimedean-level companion

G-info (`theorems/G-fredholm-certificate/`, **Gate-A PASS OB-22 + deposited interval checker
OB-17**) is the same phenomenon one layer up: a method reading only the archimedean
theta-levels `d_n = θ_level(n)` (the `𝔐_FC` class) cannot force the diagonal PSD Fredholm
determinant `G_d` to equal `Ξ̂`, because the limit `G_d = ∏(1−z²/(1/4+d_n²))` differs from
`Ξ̂` unless RH holds (Lemma G.4/G.5 — convergence would *imply* RH, so it cannot be a
zero-independent input). Include as a §4bis if the paper is expanded to ~20pp; otherwise cite
as companion work. **G-hard (the general non-diagonal case) stays a CONJECTURE and is out of
scope** — the paper claims only the diagonal G-info obstruction. Its checker
`diagonal_fredholm_interval_replay.py` certifies the Gram levels `d_n`, the 3-way separation
`γ_n < d_n < √(1/4+d_n²)`, and the tail bound, by outward-rounded interval arithmetic.

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

## §5bis. Convention discipline and deposited certificates (for the methods/appendix)

- **Σ′ convention (must be stated once, prominently).** B1 uses the **R-atom** convention
  `O_j(𝒵)=Σ'_ρ φ_j(ρ)` (each atom once; `Σ'` is convergence regularization, not doubling);
  B2 uses **R-symm** `O_j(𝒵)=Σ_ρ[φ_j(ρ)+φ_j(1−ρ)]` (doubles on FE-closed multisets). They
  differ by a factor 2. Numerical anchors are **not** interchangeable between the two: B1's
  correct R-atom values are `δ_1(1)=608/425`, threshold `T*=90` (for `σ₀=3/4, m=2, ε=10⁻³`),
  decay `δ_j(T)·T² → 2j²`; B2's collision `Cα+Rb=0` is scale-invariant (unaffected). Do not
  paste a δ/C/d anchor across the two theorems.
- **Deposited independent checkers (reproducibility appendix).** All pure-stdlib, exact
  rational / outward-rounded interval, no floats in the certificate path:
  `b1_ratom_certified_checker.py` (SHA `199c7dad…`), `b2_certified_checker.py` (SHA
  `776eeab5…`), `diagonal_fredholm_interval_replay.py` (SHA `e197f2bb…`). Each re-runs to
  `ALL_CERTIFIED_CHECKS_PASSED`. A finite certificate validates only the finite replayed
  statement, never the analytic theorem — state this explicitly.

---

## §6. Novelty statement

The exact collision construction (B2) with integer multiplicities and zero tolerance
appears to be new. B1 (finite-inequality non-discrimination) is related to known
limitations of finite Li evaluations (Bombieri–Lagarias type) but is stated here in
the abstract 𝔛_sym class with an explicit escape route list. The self-contained
Vandermonde rank proof is elementary and requires no T-system theory citation. **Precise
strength of B1 (state carefully):** B1 establishes *no positive uniform separation margin*
between the `P=1` and `P=0` classes (the observation-gap infimum is 0), **not** an exact
discriminator failure at fixed inputs — this keeps B1 clear of the "margin → 0" non-barrier
label. B2 is the exact-collision strengthening on a constructed (not-ζ) member.

---

## §7. Submission target and readiness

- **Venue (provisional):** Acta Arithmetica / Journal of Number Theory (short note), ~15pp
  (or ~20pp if the G-info §4bis is folded in).
- **Readiness:** B1 and B2 have both **passed whole-theorem independent Gate-A review**
  (OB-23 with §7 mods; OB-20) and carry **deposited independent checkers** (OB-24; OB-21/OB-13)
  — the two review dependencies listed in earlier drafts are **closed**. What remains is
  editorial: expand the proof sketches (§3, §4) to full proofs from the theorem files, add the
  convention/reproducibility appendix (§5bis), and finalize the prior-art comparison.
- **Hard boundary (must appear in the intro and conclusion):** the paper proves *no-go
  theorems for a method class*, names all five acceptance-test elements (class, non-vacuity,
  observation, target, escape), and states plainly that it does **not** prove, disprove, or
  approach RH.
