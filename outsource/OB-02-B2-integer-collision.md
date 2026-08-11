# Problem OB-02 — Exact finite-observation collision with integer multiplicities

**Type:** Analytic number theory / combinatorics. Self-contained; requires no
knowledge of RH or the Riemann zeta function beyond the names of the tests.  
**Repo context:** This is an independent verification request for Theorem B2
(`theorems/B2-exact-collision/`) of the RH Obstruction Theory repository. You do NOT
need any other file from that repo to solve this problem.

---

## Self-contained setup

### Admissible zero multisets

An **admissible symmetric zero multiset** is a locally finite multiset
`𝒵 ⊂ {s ∈ ℂ : 0 < Re(s) < 1}` satisfying:
- Conjugate symmetry: `ρ ∈ 𝒵 ⟹ ρ̄ ∈ 𝒵` (with same multiplicity).
- Functional symmetry: `ρ ∈ 𝒵 ⟹ 1−ρ ∈ 𝒵` (with same multiplicity).
- Admissibility: `Σ_{ρ ∈ 𝒵} |ρ|^{-2} < ∞`.

The **critical-line predicate** is `P(𝒵) = 1` if all elements of `𝒵` have real
part exactly `1/2`, and `P(𝒵) = 0` otherwise.

### Li-type test functionals

For `j = 1, …, m`, define the **Li-type test functional**:
```
φ_j(ρ) := 1 − (1 − 1/ρ)^j,
```
and the observation functional on a finite multiset `𝒵 = {ρ_1, …, ρ_K}`:
```
O_j(𝒵) := Σ_{ρ ∈ 𝒵} [φ_j(ρ) + φ_j(ρ̄)].
```
(The sum runs over all elements with multiplicity.)

The **observation map** `O_Φ := (O_1, …, O_m) : 𝔛_sym → ℝ^m`.

### Off-line quartet

For `σ₀ ∈ (1/2, 1)` (take `σ₀ = 3/4`) and `T > 0`, the **off-line quartet** is:
```
Q(σ₀, T) := {σ₀ + iT,  σ₀ − iT,  (1−σ₀) + iT,  (1−σ₀) − iT}.
```
This is admissible and symmetric, with `P(Q) = 0` (off the critical line).

---

## The theorem to be verified

**Theorem B2 (exact collision, integer multiplicities).** For any `m ≥ 1` and any
`m` distinct rational heights `0 < t₁ < … < t_m`, the following holds:

There exist:
- A positive integer `M` (the multiplicity buffer),
- A rational `T > 0` (large, to be specified),
- A positive integer `R` (the scaling factor),
- An integer vector `α = (α₁, …, α_m) ∈ ℤ^m`,

such that, setting:
```
𝒵_+ := { 1/2 ± i t_k : k = 1, …, m,  each with multiplicity M },
𝒵_− := 𝒵_+  ∪  (additions/removals per α)  ∪  R copies of Q(3/4, T),
```
we have:
1. `P(𝒵_+) = 1` (critical-line predicate true).
2. `P(𝒵_−) = 0` (critical-line predicate false, due to the off-line quartet).
3. `O_j(𝒵_+) = O_j(𝒵_−)` **exactly** for `j = 1, …, m` (observation collision).
4. `𝒵_−` is admissible and symmetric (removal of at most `M` copies from each height
   is valid by construction of `M`).

---

## The proof to be verified

The proof proceeds in five steps. **Please verify each step independently.**

### Step 1 — Li Jacobian is nonsingular (Vandermonde reduction)

**Claim.** The `m × m` Jacobian matrix `J` with entries:
```
J_{jk} = 2(1 − cos(j θ_k)),   where θ_k = 2 arctan(2t_k) − π,
```
has nonzero determinant for any distinct `t₁, …, t_m > 0`.

**Proof strategy.** Let `x_k = cos θ_k ∈ (−1, 1)`. Using the Chebyshev identity
`cos(jθ) = T_j(cos θ)` and the factorization `1 − T_j(x) = (1−x) Q_j(x)` with
`Q_j` a polynomial of degree `j−1` and leading coefficient `2^{j−1}`:
```
J_{jk} = 2(1−x_k) Q_j(x_k).
```
Since `1−x_k > 0`, factoring gives `rank J = rank [Q_j(x_k)]`. The polynomials
`{Q_j}_{j=1}^m` have degrees `0, 1, …, m−1` with positive leading coefficients,
forming a basis for `ℝ_{≤m-1}[x]`. Writing `Q_j(x) = Σ_{i≤j} U_{ji} x^{i-1}` with
upper-triangular `U` (diagonal entries `2^{j-1} > 0`):
```
[Q_j(x_k)] = U · V(x_1,…,x_m)
```
where `V` is the standard Vandermonde. Since `x_1,…,x_m` are distinct (because
`t ↦ θ(t) ↦ cos θ(t)` is strictly monotone), `det V ≠ 0`, so `det J ≠ 0`. ✓

**Please verify:** (a) The Chebyshev identity; (b) that `deg Q_j = j−1` with leading
coefficient `2^{j-1}` follows from the recurrence `T_{j+1}(x) = 2x T_j(x) − T_{j-1}(x)`;
(c) the Vandermonde factorization.

### Step 2 — Rationality of J and δ^{off}

**Claim.** For rational `t_k, σ₀, T`, the matrix `J ∈ ℚ^{m×m}` and the quartet
contribution `δ_j^{off}(T) ∈ ℚ` for Li-type tests.

*Proof.* `J_{jk} = 2(1 − Re[(1−1/(1/2+it_k))^j])`. The quantity `1/(1/2+it_k) = (1/2−it_k)/(1/4+t_k²)` is rational for rational `t_k`. So `J_{jk} ∈ ℚ`. Similarly
`δ_j^{off}(T) = O_j(Q(3/4,T))` is a sum of `φ_j` at rational points, hence rational. ✓

### Step 3 — Rational solution and integer scaling

**Claim.** Given `det J ≠ 0` over `ℚ`, let `α^ℚ = −J^{-1} δ^{off}(T) ∈ ℚ^m`. Set
`R = lcm(denominators of α^ℚ_k)` and `α = R · α^ℚ ∈ ℤ^m`. Replace `Q` by `R` copies
of the quartet (scaling `δ^{off}` by `R`). Then `J · α = −R · δ^{off}(T)` exactly. ✓

### Step 4 — Multiplicity buffer and valid removal

**Claim.** Set `M = R · max_k |α^ℚ_k|`. The multiset `𝒵_+` with all heights at
multiplicity `M` allows removal of up to `|α_k| = R|α^ℚ_k| ≤ M` copies at each
height. Hence `𝒵_−` is well-defined. ✓

### Step 5 — Observation equality and predicate separation

**Claim.** By construction:
```
O_j(𝒵_−) − O_j(𝒵_+) = Σ_k α_k J_{jk} + R δ_j^{off}(T)
                      = [J α]_j + R δ_j^{off}(T)
                      = −R δ_j^{off}(T) + R δ_j^{off}(T) = 0.
```
And `P(𝒵_−) = 0` because the quartet `Q(3/4, T)` contributes points at `Re = 3/4 ≠ 1/2`. ✓

---

## Acceptance criteria

1. Confirm or correct each of Steps 1–5 above.
2. If the Vandermonde reduction in Step 1 has a gap, identify it precisely.
3. Confirm the scaling trick in Step 3 is logically complete (R copies of the
   quartet really produce a scaled equation, not an approximation).
4. Confirm that `𝒵_−` is admissible (locally finite, symmetric, admissibility sum
   increases by finitely many terms).
5. State clearly whether this constitutes a proof of Theorem B2 as stated, or whether
   additional conditions are needed.
6. **No reference to actual Riemann zeta zeros, RH, or numerics required.** The
   construction is entirely combinatorial / algebraic for fixed `m, t_1, …, t_m`.

---

## What this does and does not prove

This theorem says: there exist two finite admissible symmetric zero multisets in the
critical strip with the same Li-type observation vector but different critical-line
predicates. It does **not** claim anything about the actual Riemann zeta zeros, and
does not claim to prove or disprove RH.
