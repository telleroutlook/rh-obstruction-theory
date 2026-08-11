# Problem OB-03 — Non-uniqueness of entire order-1 functions matching finite evidence

**Type:** Classical complex analysis (Hadamard factorization + implicit function theorem).
No number theory required.  
**Repo context:** This verifies the quantitative step (§3) of Theorem E
(`theorems/E-compactness/`) in the RH Obstruction Theory repository. You do NOT need
any other file from that repo.

---

## Self-contained setup

Let `{γ_n}_{n≥1}` be any sequence of positive reals satisfying:
- `0 < γ₁ < γ₂ < … → +∞`;
- `Σ_{n≥1} γ_n^{-2} < ∞` (the Hadamard genus-1 convergence condition);
- `γ_n ~ (n/2π) log(n/2π)` as `n → ∞` (von Mangoldt asymptotics — used only for
  the quantitative bound, not for the existence result).

Define the **reference entire function**:
```
Ξ(z) := C · ∏_{n≥1} (1 − z²/γ_n²),   C > 0,
```
which is entire of order 1, even, and real on `ℝ`.

Fix integers `k_N ≥ 1` (the "first `N` zeros"), `J_N ≥ 1` (the "first `J_N` Taylor
conditions"), and a constant `c₀ > 0`.

---

## Theorem to be verified (§3 quantitative estimate)

**Theorem (non-uniqueness with finite evidence).** For any `ε > 0`, there exists an
entire function `F ≠ Ξ` satisfying:
1. `F` is entire of order 1.
2. `F` is even: `F(−z) = F(z)`.
3. `F` is real on `ℝ`.
4. The zeros of `F` are all real (equal to `±γ_n` for `n ≤ k_N`, and to `±μ_n` for
   `n > k_N`, where `μ_n ∈ ℝ`, `μ_n > 0`).
5. `F(0) = Ξ(0) = C`.
6. `F^{(2j)}(0) = Ξ^{(2j)}(0)` for `j = 0, 1, …, J_N` (first `J_N + 1` even-power
   Taylor coefficients agree).
7. `sup_{|z| ≤ R₀} |F(z) − Ξ(z)| ≥ ε` for some `R₀ = R₀(N, ε, c₀)`.

That is, the finite evidence record (conditions 1–6) does **not** uniquely determine `Ξ`.

---

## The proof to be verified

### Step A — Perturbed tail product

For `n > k_N`, define:
```
μ_n := γ_n (1 + c₀/(n − k_N)).
```
Then:
- `μ_n > γ_n > 0` for all `n > k_N`.
- `Σ_{n > k_N} μ_n^{-2} ≤ Σ_{n > k_N} γ_n^{-2} < ∞`.
- `μ_n/γ_n = 1 + c₀/(n−k_N) → 1` as `n → ∞`.

Define the preliminary perturbed function:
```
F₀(z) := C · ∏_{n=1}^{k_N} (1 − z²/γ_n²) · ∏_{n > k_N} (1 − z²/μ_n²).
```
`F₀` is entire of order 1 (both products converge), even, real on `ℝ`, real-rooted,
and `F₀(0) = C`. It satisfies conditions 1–5.

**Please verify:** that `F₀` has order exactly 1. (The order is determined by
`Σ μ_n^{-2} < ∞`, which forces genus 1 in the Hadamard factorization.)

### Step B — Taylor coefficient matching via IFT

The even-power Taylor coefficients of `F₀` are:
```
F₀^{(2j)}(0) / (2j)! = −C · e_j({γ_n^{-2}}_{n≤k_N}) · e_{?}({μ_n^{-2}}_{n>k_N})
```
(where `e_j` denotes the `j`-th elementary symmetric polynomial in the reciprocal
squares, from the logarithmic derivative of the Hadamard product).

To enforce condition (6), we adjust `J_N` of the tail zeros. Specifically, treat
`μ_{k_N+1}, …, μ_{k_N+J_N}` as free parameters and freeze `μ_n = γ_n(1+c₀/(n−k_N))`
for `n > k_N + J_N`.

The Jacobian of `(F^{(2j)}(0))_{j=1,…,J_N}` with respect to `(μ_n^{-2})_{n=k_N+1,…,k_N+J_N}` is:
```
∂(F^{(2j)}(0)) / ∂(μ_n^{-2}) = (const) · (−1)^j · (2j)! · (product of other terms)
```
The key matrix (after extracting positive scalars) is of the form `U · V` where `U`
is upper-triangular with positive diagonal and `V` is a Vandermonde matrix in the
values `μ_{k_N+1}^{-2}, …, μ_{k_N+J_N}^{-2}`.

**Please verify:** that this Jacobian is nonsingular when the `μ_n^{-2}` are distinct
(which they are, since `μ_n$ are distinct). The claim is that the Vandermonde structure
ensures nonsingularity.

**Result:** By the implicit function theorem, for small `c₀`, there exist adjusted
tail zeros `μ_{k_N+1}^{(c₀)}, …, μ_{k_N+J_N}^{(c₀)}` (close to the original
`γ_{k_N+1}, …, γ_{k_N+J_N}`) such that the resulting `F` satisfies condition (6).
The order remains 1 (the `e^{az²}` Hadamard factor has `a ∈ ℝ` determined by condition (5);
for even functions, `a` is determined by the normalization).

### Step C — Quantitative separation

**Claim.** `F ≠ Ξ` with quantitative separation:
```
|F(iR) − Ξ(iR)| ≥ c(c₀) · |Ξ(iR)|   for R ≈ γ_{k_N+1}.
```

*Proof.* Evaluate at `z = iR`, `R = γ_{k_N+1}`:
```
F(iR) / Ξ(iR) = ∏_{n=1}^{k_N} 1 · ∏_{n > k_N} [(1 + R²/μ_n²) / (1 + R²/γ_n²)].
```
(The first `k_N` factors cancel exactly.) The `n = k_N+1` factor:
```
(1 + R²/μ_{k_N+1}²) / (1 + R²/γ_{k_N+1}²)
= (1 + γ_{k_N+1}²/μ_{k_N+1}²) / 2   [since R = γ_{k_N+1}]
= (1 + (1+c₀)^{-2}) / 2 =: η(c₀) < 1.
```
So `F(iR)/Ξ(iR) ≤ η(c₀)^{1/2} < 1` (the product of all factors is bounded from 1).

**Lower bound for `|Ξ(iR)|`:**
```
|Ξ(iR)| = C · ∏_n (1 + R²/γ_n²) ≥ C · ∏_{n: γ_n ≤ R} 2 = C · 2^{N(R)},
```
where `N(R) ~ R log R / (2π) → ∞`. So `|Ξ(iR)| → ∞`.

Therefore `|F(iR) − Ξ(iR)| ≥ (1 − η(c₀)) · |Ξ(iR)| → ∞`, so for any `ε > 0`, we
can choose `R` large enough to exceed `ε`. ✓

---

## Acceptance criteria

1. Verify Step A: `F₀` is entire of order 1 (genus-1 Hadamard product).
2. Verify Step B: the Taylor-matching Jacobian has Vandermonde structure and is
   nonsingular when the `μ_n^{-2}` are distinct.
3. Verify Step C: the quantitative separation argument is rigorous (no gaps in the
   product bound).
4. State whether the resulting `F` satisfies **all** of conditions (1)–(7).
5. If any step has a gap, identify it precisely.
6. **No knowledge of Riemann zeta zeros is needed.** The sequence `{γ_n}` is any
   sequence satisfying the stated conditions; take `γ_n = n` for a concrete example.

---

## What this does and does not prove

This theorem says: given any sequence `{γ_n}` satisfying the Hadamard conditions, the
finite evidence record (first `k_N` zeros, first `J_N` Taylor coefficients,
normalization, order 1, real-rooted) does **not** uniquely determine the entire function
`Ξ = C · ∏(1 − z²/γ_n²)`. It is a pure complex analysis result with no connection to
RH or the Riemann zeta function. If `{γ_n}` happen to be the Riemann zeta zero
ordinates, the theorem says: finite spectral data does not uniquely pin down the
CCM/Ξ target.
