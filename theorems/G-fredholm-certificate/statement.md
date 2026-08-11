# Statement — Theorem G (G-fredholm-certificate)

**Theorem ID:** G-fredholm-certificate  
**Program ref:** §9.G (information obstruction; method class 𝔐_FC)  
**Status:** PROOF-DRAFT (information-obstruction core; see §3 for open steps)

---

## §1. Method class 𝔐_FC (Fredholm Certificate, theta-level observation)

**Definition (𝔐_FC).** A method `P ∈ 𝔐_FC` is a construction procedure that:

1. Takes input from the observation map `O_θ : ℕ → ℝ`, where `O_θ(n) = θ(n)` is the
   Riemann–Siegel theta function value `θ(t) = Im(log Γ(1/4 + it/2)) − t log(π)/2`
   evaluated at the unfolded ordinate position `t = θ⁻¹(πn)`.  
   More precisely, the observation is the archimedean level sequence `d_n = θ_level(n)`,
   the zero-free approximation to the n-th Riemann zero ordinate.

2. Constructs a finite-rank self-adjoint positive semidefinite operator `K_N` on a
   Hilbert space `H` using only:
   - the archimedean levels `{d_n : n ≤ N}`;
   - arithmetic data (primes, local factors, weights) that are **zero-free** (do not read
     zero ordinates of any L-function);
   - no parameter fitted by minimizing error against known zeros or spectral samples of ζ.

3. Claims that the resulting determinant `det(I − z² K_N)` converges locally uniformly
   to `Ξ̂(z) = ξ(1/2 + iz)/ξ(1/2)` (normalized so `Ξ̂(0) = 1`).

**Normalization note (OB-08 referee §2.2).** The correct normalization target is
`Ξ̂(z) = ξ(1/2+iz)/ξ(1/2)` with `Ξ̂(0) = 1`.  If the program uses the unnormalized
`ξ(1/2+iz)`, det(I−0·K_N) = 1 but `ξ(1/2) ≠ 1`, so convergence to the unnormalized
function is impossible.

**Fredholm determinant formula (OB-08 referee §2.1 — CORRECTED).** For a finite-rank
positive semidefinite operator K_N with nonzero eigenvalues `λ_1,…,λ_{r_N}`:
```
det(I − z² K_N) = ∏_{j=1}^{r_N} (1 − z² λ_j(K_N)).
```
The zeros of this polynomial in z are at `z = ±λ_j^{-1/2}`, NOT at `±λ_j^{1/2}`.

**Factorization condition (2.7) — logical status (OB-08 referee §3).** There are two
distinct readings:
- **(Weak/definitional):** `K_N = Φ_N(O_θ(𝒵), a_N)` — the construction depends only
  on `(d_n)` and zero-free arithmetic data `a_N`.  This is a direct restatement of the
  membership conditions and is definitionally true for any `P ∈ 𝔐_FC`.
- **(Strong/theorem):** `K_N = Ψ_N(O_θ(𝒵))` — the construction factors through `O_θ`
  alone, with no auxiliary arithmetic data.  Since `O_θ` is a constant map, this would
  force K_N to be the same for all 𝒵, for every P ∈ 𝔐_FC.

The weak reading is definitional (trivially true by construction). The strong reading
is a nontrivial additional claim that is NOT implied by the membership conditions.
Moreover, "zero-free input" does NOT imply "zero-blind output": zero-free arithmetic
data can analytically determine zero ordinates (via Euler product continuation).
Theorem G's obstruction requires the weak reading (plus Prop. G.3*); the strong reading
would be needed for a fully unconditional information-obstruction claim.

**Observation map domain.** `O_θ` is computable from arithmetic/archimedean data alone;
it does not encode the arithmetic fluctuation `S(T) = (1/π) arg ζ(1/2 + iT)`.

**Non-vacuity.** The diagonal class `𝔐_d^{tr}` (see §3 below) is a non-empty subclass
of 𝔐_FC with explicit members: `K_N = D_N = diag(κ_1,…,κ_N)` with `κ_n = 1/(1/4+d_n²)`.
The kappa_toeplitz construction of the sibling repository was a claimed example; its
non-vacuity is conditional on unverified properties (see §3).

---

## §2. Target predicate and adversary pair

**Target predicate T:** "the locally uniform limit of `det(I − z² K_N)` is `Ξ`."

**Adversary pair.** The two objects are:
- `𝒵_RH`: the (hypothetical) multiset of all Riemann zero ordinates `{γ_n}`, on the
  critical line.
- `𝒵_ε`: a multiset where `γ_n` is replaced by `γ_n + ε_n` with `ε_n` drawn from the
  arithmetic fluctuation `S(T)`, i.e. the n-th ordinate is perturbed by an amount not
  visible in `O_θ`.

Under RH, `𝒵_RH` is the zero multiset of `Ξ`. The predicate `T` exactly distinguishes
`𝒵_RH` from `𝒵_ε` (different locally uniform limit), since by Hadamard uniqueness an
entire function of order 1 is determined by its zeros up to a multiplier (and the
multiplier is fixed by the normalization `Ξ(0)`).

**Observation collision.** Both `𝒵_RH` and `𝒵_ε` map to the **same** `O_θ` values: the
archimedean levels `d_n = θ_level(n)` differ from both `γ_n` and `γ_n + ε_n` by
approximately the same amount (the S(T) gap), making them indistinguishable under `O_θ`.

---

## §3. Obstruction statement — CORRECTED (OB-08)

**Diagonal stable subclass 𝔐_d^{tr} (OB-08 referee §8).** Let `𝔐_d^{tr}` be the set of
all finite-rank positive semidefinite families `(K_N)` satisfying:
```
K_N = Φ_N(d_1,…,d_N),       ‖K_N − D_N‖_1 → 0,
```
where `D_N = diag(κ_1,…,κ_N)` with `κ_n = 1/(1/4 + d_n²)`.
(If auxiliary arithmetic data is allowed: `K_N = Φ_N(d_≤N, a_N)` with the same trace-norm condition.)

**Corrected Theorem G (diagonal obstruction — PROOF-DRAFT).**  
The class `𝔐_d^{tr}` is non-empty (witness: `K_N = D_N`).  For every `(K_N) ∈ 𝔐_d^{tr}`:
```
det(I − z² K_N) → G_d(z) = ∏_{n≥1} (1 − z²/(1/4 + d_n²))
```
locally uniformly (by OB-08 Theorem 6.1, using `‖K_N − D_N‖_1 → 0` and the Fredholm
determinant stability inequality).  Moreover, `G_d ≠ Ξ̂` unconditionally:
- If RH holds: `Ξ̂ = F_γ = C·∏(1−z²/γ_n²)` has zeros `{±γ_n}`; `G_d` has zeros
  `{±√(1/4+d_n²)}`; these sets differ since `√(1/4+d_n²) > d_n` and `d_n ≠ γ_n`
  for infinitely many n (Prop. G.3* Item 2).
- If RH fails: `Ξ̂` has at least one non-real zero; all zeros of `G_d` are real.
  Either way `G_d ≠ Ξ̂`. ✓ Unconditional.

**Two independent obstructions in `G_d` vs `Ξ̂`:**
1. **Spectral parameter shift:** `d_n ↦ √(1/4+d_n²)` — the zeros of `det(I−z²D_N)` are
   at `±(d_n²+1/4)^{1/2}`, not at `±d_n`.  Using the shifted determinant
   `det(I−(z²+1/4)D_N)/det(I−(1/4)D_N)` instead would give zeros at `±d_n` — but
   then `F_d ≠ Ξ̂` by Prop. G.3* (even if the 1/4 shift is corrected).
2. **S(T) gap:** `{d_n} ≠ {γ_n}` as multisets (Prop. G.3* Item 2); `F_d ≠ F_γ`.

**Part G-info (information obstruction — PROOF-DRAFT):**  
For any `P ∈ 𝔐_d^{tr}`, the locally uniform limit of `det(I − z² K_N)` is `G_d ≠ Ξ̂`.
The arithmetic fluctuation `S(T)` is not in `O_θ`, and the spectral parameter shift
further separates `G_d` from `Ξ̂`.

**Part G-hard (reduction hardness — CONJECTURE):**  
No method in 𝔐_FC can supply the S(T) data without either reading zero ordinates or
implicitly computing an RH-equivalent quantity.
This conjecture is recorded as `[CONJECTURE]`; it is not a proved premise.

**kappa_toeplitz status (OB-08).** The kappa_toeplitz construction (K_N = D_N + α C_Toeplitz)
cannot be confirmed as an unconditional member of `𝔐_FC` because:
- The matrix `C_Toeplitz` and coefficient `α` are not explicitly defined in a form
  that can be independently verified.
- If the convergence `det(I − z² K_N) → Ξ̂` were proved for any PSD K_N with finite-rank
  limits, RH would follow (Lemma G.4 + Corollary G.5, proof.md §5b, CONFIRMED by OB-10
  2026-08-11: any locally uniform limit of `det(I − z² K_N)` with K_N ≥ 0 has all-real
  zeros via Hurwitz; if this limit equals Ξ̂, then all zeros of Ξ̂ are real, which is RH).
  Therefore membership condition 3 of 𝔐_FC ("claims det → Ξ̂") cannot be verified
  without proving RH.

The diagonal class `𝔐_d^{tr}` replaces kappa_toeplitz as the explicit non-vacuity witness.

---

## §4. Escape route

A construction **outside** 𝔐_FC can avoid this obstruction if it supplies the S(T) data
by a route other than the archimedean theta-level. Explicit escape routes:
- A construction that uses the full von Mangoldt `Λ`-explicit formula (reads zeros →
  outside 𝔐_FC by design).
- A construction that achieves `det = Ξ` via a non-spectral identity (e.g., an
  infinite-dimensional Borel sum or a Selberg-class factorization) without first
  approximating eigenvectors.
- Any construction whose positivity proof requires RH as a hypothesis (outside 𝔐_FC by
  the forbidden-construction-leaf rule, spec §3.3 of the sibling repo).

---

## §5. Acceptance test compliance (program §14)

| Check | Status |
|---|---|
| **Class** (checkable membership) | O_θ-observation + zero-free + no fitted parameter — syntactically checkable via sibling repo guard.py |
| **Non-vacuity** (serious published construction in 𝔐_FC) | kappa_toeplitz (sibling repo) — PROOF-DRAFT (Bochner positivity) |
| **Target** (adversaries differ on predicate) | Ξ vs Ξ_ε — differ as entire functions by Hadamard uniqueness |
| **Observation** (collision exact) | O_θ maps both to same d_n sequence (S(T) gap) — PROOF-DRAFT |
| **Invariant** (obstruction survives equivalences) | S(T)-gap is basis-independent (a fact about counting functions) |
| **No-RH** (no RH among hypotheses) | Correct: obstruction holds whether or not RH is true |
| **Escape** (explicit route outside class) | See §4 — read zeros or non-spectral identity |
| **Scope** (ambient class + resource bound) | 𝔐_FC + theta-level observation; finite-rank approximation package |

---

## §6. Mathematical and computational status

| Axis | Status |
|---|---|
| Mathematical | PROOF-DRAFT (G-info); CONJECTURE (G-hard) |
| Computational | INDEPENDENT-CHECKER (OB-17 2026-08-11: certified exact-rational interval replay of the diagonal-Fredholm finite core — `checker/diagonal_fredholm_interval_replay.py`, SHA-256 e197f2bb…c8f4058b; d_n enclosed to <6.83e-12, three-way separation γ_n<d_n<√(1/4+d_n²) certified, tail Σ_{n>2048}κ_n<10⁻³, both mutation guards pass) |

**What is proved here (G-info, PROOF-DRAFT):**
1. The Hadamard uniqueness lemma: an order-1 entire function is determined by its zeros
   + normalization (classical, REFEREED).
2. The S(T) gap: `γ_n − d_n = S(γ_n)/density + lower order`, where S(T) is the
   argument function — this is a standard analytic number theory identity (REFEREED;
   Titchmarsh §9.4; Davenport §15).
3. The observation indistinguishability: O_θ returns the same d_n for both 𝒵_RH and 𝒵_ε
   when ε_n is chosen from the S(T) discrepancy.

**What remains CONJECTURE:**
- G-hard: the impossibility of S(T) recovery from zero-free arithmetic data within 𝔐_FC
  — this would require a precise statement about what prime-based constructions can compute,
  which is the open problem.

**Limitation.** Theorem G does NOT:
- prove RH or imply anything about the truth of RH;
- assert the kappa_toeplitz construction is wrong (it may be correctable outside 𝔐_FC);
- assert no Fredholm certificate exists (only that theta-level methods in 𝔐_FC cannot
  close CORE-4 from O_θ alone);
- assert that S(T) is genuinely uncomputable from primes (that is the CONJECTURE part).
