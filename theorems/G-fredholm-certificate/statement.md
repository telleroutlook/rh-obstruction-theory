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
   to the Riemann entire function `Ξ(z) = ξ(1/2 + iz)`.

**Observation map domain.** `O_θ` is computable from arithmetic/archimedean data alone;
it does not encode the arithmetic fluctuation `S(T) = (1/π) arg ζ(1/2 + iT)`.

**Non-vacuity.** The kappa_toeplitz construction of the sibling repository
`absolute-arithmetic-spectral-verification` is an explicit published member of 𝔐_FC:
it constructs `K_N = D_κ + α C_Toeplitz` with `κ_n^smooth = 1/(1/4 + d_n²)`,
uses Bochner's theorem for positivity, and attempts local-uniform determinant convergence
to Ξ.  Bochner positivity: PROOF-DRAFT (see sibling repo `proof/m3/bochner_positivity.py`).

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

## §3. Obstruction statement (two-part)

**Part G-info (information obstruction — PROOF-DRAFT):**  
For any `P ∈ 𝔐_FC`, the observation `O_θ` does not determine whether the resulting
determinant converges to `Ξ` or to a distinct entire function `Ξ_ε` with perturbed zeros.
Specifically, the arithmetic fluctuation `S(T) = (1/π) arg ζ(1/2 + iT)` is not
reconstructible from `O_θ`, and the S(T) gap is exactly the eigenvalue error that
prevents CORE-4 from closing without reading zero ordinates.

**Part G-hard (reduction hardness — CONJECTURE):**  
No method in 𝔐_FC can supply the S(T) data without either (a) reading zero ordinates
(forbidden by the zero-free constraint) or (b) implicitly computing arg ζ along the
critical line (equivalent to knowing the zero locations, hence RH-equivalent).
This conjecture is recorded as `[CONJECTURE]`; it is not a proved premise.

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
| Computational | REPRODUCIBLE (sibling repo spectral error verified) |

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
