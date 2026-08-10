# Proof — Theorem B2 (exact finite-observation collision)

**Status:** PROOF-DRAFT (partial — rank condition open)  
**Analytic / finite separation:** purely analytic; no finite certificate used.

---

## §1. Strategy overview

We insert one off-line quartet `Q(σ₀, T)` and `n` on-line compensating pairs
`{1/2 ± it_k}` (added or removed) to cancel the quartet's observation shift
exactly.  The key steps are:

1. **Parameterize the perturbation** (§2): express `Δ_j = O_j(𝒵_−) − O_j(𝒵_+)`
   as a linear system `J·α = −δ^{off}(T)` in the on-line adjustments `α`.
2. **Quartet tail** (§3): show `δ^{off}(T) → 0` as `T → ∞` (from B1 proof.md §2).
3. **Rank analysis** (§4): analyse when `J` has a solution with `α ∈ ℤ_{≥0}^n`
   (nonneg integer multiplicities). **THIS IS THE OPEN ITEM.**
4. **Construction** (§5): given the rank, choose `T_*` so `δ^{off}(T_*)` is
   in the range of `J`, and solve for `α`.
5. **Verification** (§6): check `𝒵_− ∈ 𝔛_sym`, `P(𝒵_−) = 0`, exact collision.
6. **Counting-law remark** (§7): the construction adds and removes finitely many
   zeros at bounded heights; the von Mangoldt law is perturbed by `O(1)`.

---

## §2. Parameterization

Fix `σ₀ ∈ (1/2, 1)` (take `σ₀ = 3/4` for concreteness) and `n ≥ m`.

Choose heights `0 < t₁ < … < t_n` (to be determined in §4) and let
`α_k ∈ ℤ_{≥0}` be the multiplicity added at on-line pair `(1/2 + it_k, 1/2 − it_k)`.
Then for `j = 1, …, m`:

```
Δ_j = Σ_{k=1}^{n} α_k · A_{jk}  +  δ_j^{off}(T),
```

where `A_{jk} := φ_j(1/2+it_k) + φ_j(1/2−it_k)` and
`δ_j^{off}(T)` is the quartet contribution.

For exact collision we need `Δ_j = 0`, i.e.

```
J α = −δ^{off}(T),          (*)
```

where `J ∈ ℝ^{m×n}` has entries `J_{jk} = A_{jk}`.

---

## §3. Quartet tail decay

By B1 proof.md §2 (off-line quartet lemma), for each `j`:

- **Li-type tests:** `δ_j^{off}(T) → 0` as `T → ∞`.
- **Weil W2-type tests:** `δ_j^{off}(T) = 4 ĥ_j(T) → 0` (Riemann–Lebesgue).
- **Moment tests (`φ_j(ρ) = ρ^{−k}`):** `δ_j^{off}(T) = O(T^{−k}) → 0`.

So the right-hand side `−δ^{off}(T)` of (*) can be made arbitrarily small in
`ℝ^m` by choosing `T` large.

---

## §4. Rank analysis (PROOF-DRAFT for real/Q rank; integer solution open)

**Question:** For which test families `Φ` and which heights `t₁, …, t_n` is
`J ∈ ℝ^{m×n}` such that (*) has a solution `α ∈ ℤ_{≥0}^n`?

### §4.1 The real rank step

If `n > m`, then generically `J` is surjective over `ℝ` (has a right inverse
`J†`), so any target `b = −δ^{off}(T) ∈ ℝ^m` has a real solution
`α^ℝ = J† b`.  For small `|b|`, `α^ℝ` has small norm.

**Issue:** We need `α ∈ ℤ_{≥0}^n`, not just `α ∈ ℝ^n`.  For small target
`b ≈ 0`, the solution `α^ℝ ≈ 0` is not an integer vector unless we allow
the "removed zero" convention (but removing a real zero has multiplicity
constraints related to the zero multiset structure of `𝒵_+`).

### §4.2 The integer programming obstruction

The system `J α = b` with `α ∈ ℤ_{≥0}^n` is an integer programming problem.
For generic `J` and small `b`, the ILP solution may not exist.

**Alternative (relaxed model):** allow `α ∈ ℤ^n` (positive = add, negative =
remove from `𝒵_+`).  If we assume `𝒵_+` has sufficiently many on-line zeros at
the chosen heights `t₁, …, t_n` (so removal is valid), the integer system
`J α = b` over `ℤ` has a solution iff `b ∈ J(ℤ^n)` (lattice coset condition).

For the `ℤ`-relaxed model, a solution exists when:

- `rank_ℚ J = m` (full row rank over `ℚ`), AND
- `b ∈ J(ℚ^m)` (solvability over `ℚ`), AND
- the denominators of `J^{-1}b` (over `ℚ`) are bounded — which holds if `T` is
  chosen rationally and `φ_j` are rational functions evaluated at `1/2+it_k` for
  rational `t_k`.

### §4.3 Li-type test: Vandermonde proof (PROOF-DRAFT)

For Li-type tests `φ_j(ρ) = 1 − (1−1/ρ)^j`, `j = 1, …, m`:

```
A_{jk} = φ_j(1/2+it_k) + φ_j(1/2−it_k)
        = 2 Re[1 − (1 − 1/(1/2+it_k))^j]
        = 2 − 2 Re[(1 − 2/(1+2it_k))^j].
```

Let `w_k = 1 − 2/(1+2it_k) = (2it_k − 1)/(2it_k + 1)`, a Möbius image of `t_k`.

Then `A_{jk} = 2 − 2 Re(w_k^j)`.

Write `w_k = r_k e^{iθ_k}` (polar form).  Note `|w_k| = |(2it_k−1)/(2it_k+1)| = 1`
for `t_k ∈ ℝ` (both numerator and denominator have modulus `√(1+4t_k²)`), so
`w_k = e^{iθ_k}` with `θ_k = 2 arctan(2t_k) − π`.  Thus

```
A_{jk} = 2 − 2 cos(jθ_k) = 2(1 − cos(jθ_k)).
```

The matrix `J` with `J_{jk} = 2(1 − cos(jθ_k))` has the structure of a cosine
Vandermonde matrix:

```
J_{jk} = 2 − 2T_j(cos θ_k),
```

where `T_j` is the Chebyshev polynomial of degree `j` if we write
`cos(jθ) = T_j(cos θ)` (correct for integer `j`).

**Full rank argument.** The matrix `B_{jk} = cos(jθ_k)` for `j=1,…,m` and
distinct `θ₁, …, θ_m ∈ (0,π)` is a Vandermonde matrix in disguise: the functions
`t ↦ cos(jt)` for `j = 0, 1, …, m−1` are linearly independent on `(0, π)` and
their evaluation matrix at distinct points is nonsingular (by the theory of
Chebyshev systems / T-systems; see Karlin–Studden).  Therefore:

**Lemma (Li Jacobian full rank).** If `θ₁, …, θ_m ∈ (0, π)` are distinct, then
the `m × m` matrix `J` with `J_{jk} = 2(1 − cos(jθ_k))` has `det J ≠ 0`.
*Proof:* Factor out `2` from each column; the result is a modification of the
cosine-Vandermonde, and the rank follows from the theory of Chebyshev systems. ☐

**Rational heights `t_k` → distinct angles `θ_k`.** The map `t ↦ θ(t) = 2 arctan(2t) − π`
is strictly monotone on `ℝ_{>0}`, so distinct rational `t_k > 0` give distinct
`θ_k ∈ (−π, 0)` (using the convention `t_k > 0` and adjusting the sign of `cos`).
Over `ℚ`, at rational `t_k`, `w_k = (2it_k−1)/(2it_k+1)` is a complex number with
rational real and imaginary parts; `Re(w_k^j)` is a rational number, so `J` is a
rational matrix.  Since `det J ≠ 0` over `ℝ` (by the Chebyshev argument), and
`det J` is a rational number (rational `t_k`), `det J ≠ 0` over `ℚ`.

**Status:** PROOF-DRAFT.  The Chebyshev-system argument (Karlin–Studden or
equivalent) needs to be cited with precise theorem number before this is
INDEPENDENTLY-CHECKED.

**Discovery-tier confirmation.** Exact rational computation in
`discovery/jacobian_analysis.py` verified `det J ≠ 0` for Li m=3 and m=5 at
multiple rational heights (see `discovery/jacobian_rank_results.md`).  This
is DISCOVERY TIER only; it does not replace the analytic argument.

### §4.4 Moment-type test: Vandermonde (PROOF-DRAFT)

For moment-type tests `φ_k(ρ) = ρ^{−k}`, `k = 1, …, m`:

```
A_{jk} = 2 Re[(1/2 + it_k)^{−j}].
```

Write `ρ_k = 1/2 + it_k = r_k e^{iφ_k}` with `φ_k = arctan(2t_k)`.  Then
`A_{jk} = 2 r_k^{-j} cos(jφ_k)`.  Factor out the positive diagonal
`D_j = \mathrm{diag}(2r_k^{-j})_{k}`: the matrix is `D_j^{-1} B` where
`B_{jk} = cos(j φ_k)` is again a cosine-Vandermonde for distinct `φ_k`.  By the
same Chebyshev-system argument, `det J ≠ 0` for distinct positive `t_k`.

**Status:** PROOF-DRAFT (same caveat: Chebyshev citation needed).

### §4.5 Exact-collision with integer multiplicities

**Key scaling trick.** Suppose `rank_ℚ J = m` (established above for rational `t_k`).
Given `T` large, the target `b = −δ^{off}(T) ∈ ℚ^m` (all entries rational when
`T, σ₀` are rational and tests are Li/moment).  The exact solution is
`α^ℚ = J^{−1} b ∈ ℚ^m`.  Let `R = \mathrm{lcm}` of denominators of `α^ℚ_k`.  Set:

- Multiply the quartet by `R`: replace `Q(σ₀, T)` by `R` copies of `Q(σ₀, T)`
  (add `4R` off-line zeros).
- Multiply each on-line adjustment by `R`: `α_k ← R · α^ℚ_k ∈ ℤ`.

This scales both sides of `J α = b` by `R` and gives integer solutions.

**Issue: signs.** If some `α_k < 0`, the construction requires removing `|α_k|`
zeros from `𝒵_+` at height `t_k`.  This is valid if `𝒵_+` contains zeros at
those heights with sufficient multiplicity.  For `𝒵_+` = formal zero multiset of ζ,
the zeros are simple and the removal convention must be in the definition of
`𝔛_sym`.  The theorem statement allows `𝔛_sym` members with multiplicity; the
reference multiset `𝒵_+` can be any member, not necessarily ζ's zeros.

**Resolution:** We may choose `𝒵_+ ∈ 𝔛_sym` that has zeros at the chosen
heights `t_1, …, t_n` with large multiplicity (e.g., `N` copies each).  Then the
removal of `|α_k|` zeros is valid if `|α_k| ≤ N`.  For large `T`, `|b| → 0`,
so `|α^ℚ_k| → 0`, and for any fixed `N`, there exists `T_*` large enough that
`|R · α^ℚ_k| ≤ N`.

**Remaining open item:** we need `𝒵_+` to be a **specific** multiset (ideally the
Riemann zero multiset), not an abstract member of `𝔛_sym` with artificially
planted zeros.  If `𝒵_+` = Riemann zero multiset (simple zeros on the critical
line), then the removal requires `α_k ≤ 1` (can remove at most 1 copy) or
`α_k ≥ 0` (only add).

**Two sub-cases:**
- **Add-only model:** require `α_k ≥ 0` for all `k`.  Then the construction
  works whenever the solution `J^{-1} b` has all nonneg components.  For
  `b ≈ 0` (large `T`), this requires either that the unique solution `α = 0`
  (trivial, useless) or that `b` can be chosen with a sign that forces
  `α ≥ 0` — this depends on the sign of `δ^{off}(T)`.
- **Add-and-remove model:** allows removing on-line zeros from `𝒵_+`; valid
  if `𝒵_+` is generic enough.  For a theorem in `𝔛_sym` (not specifically ζ),
  this is the easier model.

**Status of integer step: OPEN.**  The scaling trick gives integers; the sign
constraint (nonneg vs. signed) needs resolution.  The theorem can proceed with
the add-and-remove model (relaxed `α ∈ ℤ`) pending this refinement.

For the full B2 theorem (exact collision, integer multiplicities), the program is:

1. Choose `n = m` (square Jacobian), `t_k` rational, `σ₀ = 3/4`. ✓
2. Show `det J ≠ 0` (over `ℚ`): PROOF-DRAFT (Chebyshev argument above). ✓
3. Solve `J α = −δ^{off}(T)` over `ℚ` via `J^{-1}`.  ✓ (conditional on rank)
4. Scale by `R = lcm(denominators)`: integer solution. ✓
5. Verify `α_k ∈ ℤ` (with sign model): OPEN (add-only vs. add-and-remove).
3. Solve `J α = −δ^{off}(T_*)` over `ℚ`.
4. Scale `T_*` so that `α_k = q_k / r` with bounded denominator `r`, then take
   `r` copies of the quartet and `r · α_k` copies of the on-line atoms.
   → Works if the scaling keeps all objects in `𝔛_sym`.
5. Verify `α_k ∈ ℤ_{≥1}` (or `ℤ_{\geq 0}` with removal).

If Step 2 fails for all rational `t_k` and natural test families `Φ`, then B2
does **not** hold for those families and the theorem is downgraded to B1.

---

## §5. Construction (conditional on §4 succeeding)

Assume `det J ≠ 0` at heights `t₁, …, t_n`.  For large `T`:

1. Set `α = −J^{-1} δ^{off}(T)` (over `ℝ`).
2. Since `δ^{off}(T) → 0`, for large enough `T` we have `|α_k|` small.
3. Use the scaling argument of §4.5 to obtain integer multiplicities.
4. Set `𝒵_− = 𝒵_+ ∪ {on-line atoms with mult α_k} ∪ Q(σ₀, T_*)`.
5. `O_Φ(𝒵_−) = O_Φ(𝒵_+)` by construction.  ☐ (conditional)

---

## §6. Admissibility and symmetry check (conditional)

- `𝒵_−` is symmetric under conjugation and `ρ ↦ 1−ρ` because all added/removed
  atoms are symmetric (on-line pairs `1/2 ± it_k`, quartet `Q`).
- Admissibility: finitely many new atoms, `|ρ|^{-(1+ε)}` sum increases by `O(1)`.
- `P(𝒵_−) = 0`: the quartet `Q(σ₀, T_*)` contributes `σ₀ ± iT_*` with
  `Re(σ₀) = 3/4 ≠ 1/2`.

---

## §7. Counting law remark

`𝒵_−` differs from `𝒵_+` by finitely many atoms (bounded height modifications).
`N_{𝒵_−}(T) = N_{𝒵_+}(T) + O(1)`.  This is an `O(1)` perturbation, not
`O(log T)`.  If the ambient class requires exact `O(log T)` counting, an
additional balancing step is needed (moving more on-line atoms to compensate).
This is left for refinement after the rank step.

---

## §8. Status summary

| Step | Status |
|---|---|
| Parameterization (§2) | DONE |
| Quartet tail decay (§3) | DONE (inherits from B1) |
| Real rank generically full (§4.1) | PLAUSIBLE, needs proof |
| Integer/rational solution (§4.5) | OPEN — central task of Days 15–21 |
| Vandermonde analysis for moment tests (§4.4) | CONJECTURE |
| Full construction (§5) | CONDITIONAL on rank |
| Admissibility check (§6) | DONE conditionally |
| Counting-law refinement (§7) | DEFERRED |
