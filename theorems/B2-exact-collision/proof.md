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

### §4.5 Exact-collision with integer multiplicities (RESOLVED — PROOF-DRAFT)

**Setup.** Fix rational `t₁, …, t_n` distinct positive, rational `σ₀ = 3/4`,
rational `T` large.  By §4.3, `det J ≠ 0` over `ℚ`, so `α^ℚ = J^{-1}b ∈ ℚ^n`
where `b = −δ^{off}(T) ∈ ℚ^n` (rational when `T, σ₀` rational, tests Li/moment).

**Key scaling trick.** Let `R = lcm(denominators of α^ℚ_k)`.  Set:

- Replace `Q(σ₀, T)` by `R` copies: `4R` off-line atoms.
- Multiply adjustments: `α_k := R · α^ℚ_k ∈ ℤ` (possibly negative).

This scales `(*) J α = b` by `R` and gives `J (R α^ℚ) = R b` — the scaled
integer vector satisfies the scaled equation exactly.

**Sign resolution (the key insight).** The theorem asserts existence of an
indistinguishable pair `(𝒵_+, 𝒵_-)` in `𝔛_sym`.  Both adversaries are
**constructed** — we are not fixing `𝒵_+` to be ζ's zeros.  We are free to
choose `𝒵_+` with any configuration in `𝔛_sym`.

**Construction of `𝒵_+`.** Set the multiplicity buffer:
```
M := R · max_{k=1,...,n} |α^ℚ_k|    (well-defined, finite).
```
Let `𝒵_+` be the finite multiset:
```
𝒵_+ := { 1/2 ± it_k  :  k = 1, …, n,  each with multiplicity  M }.
```
Verification that `𝒵_+ ∈ 𝔛_sym`:
- Locally finite: yes (finite multiset).
- Symmetric under `ρ ↦ ρ̄` and `ρ ↦ 1−ρ`: yes (pairs `1/2 ± it_k` are symmetric).
- Admissibility: finite sum, converges trivially.
- `P(𝒵_+) = 1`: all zeros on the critical line.  ✓

**Construction of `𝒵_-`.**
```
𝒵_- := 𝒵_+
       ∪ { 1/2 ± it_k  :  α_k > 0,  each added α_k times }
       ∖ { 1/2 ± it_k  :  α_k < 0,  each removed |α_k| times }
       ∪ R copies of Q(σ₀, T).
```
**Removals are valid** because each height `t_k` in `𝒵_+` has multiplicity `M`:
```
|α_k| = |R · α^ℚ_k| ≤ R · max_k |α^ℚ_k| = M.
```
So `𝒵_-` never removes more copies than `𝒵_+` has.

**Observation equality.** By construction:
```
O_j(𝒵_-) − O_j(𝒵_+) = Σ_k α_k A_{jk} + R δ_j^{off}(T) = J(Rα^ℚ)_j + R b_j = 0.
```
So `O_Φ(𝒵_-) = O_Φ(𝒵_+)` exactly.  ✓

**Predicate difference.** `P(𝒵_-) = 0` because `Q(σ₀, T)` contributes zeros at
`σ₀ = 3/4 ≠ 1/2`.  `P(𝒵_+) = 1`.  ✓

**Admissibility of `𝒵_-`.** The added/removed atoms are at bounded heights and
finite in number; `𝒵_-` is locally finite, symmetric, and admissible.  ✓

**Status: PROOF-DRAFT (integer-sign step RESOLVED).**

The add-only model (requiring `α_k ≥ 0`) is NOT needed.  The add-and-remove
model works because we construct `𝒵_+` with sufficient multiplicity.

**Limitation:** The collision pair `(𝒵_+, 𝒵_-)` consists of **finite** multisets
in `𝔛_sym`, not the specific Riemann zero multiset.  The theorem asserts existence
of an indistinguishable pair in the class; it does NOT claim the Riemann zero
multiset is indistinguishable from an off-line object.

For the full B2 theorem (exact collision, integer multiplicities), the steps are:

1. Choose `n = m`, `t_k` rational, `σ₀ = 3/4`.  ✓
2. `det J ≠ 0` over `ℚ` (Chebyshev, §4.3): PROOF-DRAFT.  ✓
3. Solve `J α^ℚ = −δ^{off}(T) / R` over `ℚ`.  ✓ (conditional on rank)
4. Scale by `R`: integer vector `α ∈ ℤ^n`.  ✓
5. Construct `𝒵_+` with multiplicity buffer `M = R · max_k |α^ℚ_k|`.  ✓
6. Construct `𝒵_-` (add/remove/quartet).  ✓
7. Verify membership, observation equality, predicate difference.  ✓ (above)

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
| Parameterization (§2) | PROOF-DRAFT ✓ |
| Quartet tail decay (§3) | PROOF-DRAFT ✓ (inherits from B1) |
| Li Jacobian full rank (§4.3, Chebyshev) | PROOF-DRAFT — citation needed |
| Moment Jacobian full rank (§4.4) | PROOF-DRAFT — same citation |
| Integer solution via scaling trick (§4.5) | PROOF-DRAFT ✓ (sign resolved) |
| 𝒵_+ construction with multiplicity buffer | PROOF-DRAFT ✓ |
| 𝒵_- construction (add/remove/quartet) | PROOF-DRAFT ✓ (conditional on rank) |
| Admissibility + symmetry (§6) | PROOF-DRAFT ✓ |
| Observation equality exact (§4.5) | PROOF-DRAFT ✓ (conditional on rank) |
| Predicate P(𝒵_-) = 0, P(𝒵_+) = 1 | PROOF-DRAFT ✓ |
| Counting-law refinement (§7) | DEFERRED |
| Gate A: Chebyshev citation by theorem number | PENDING → INDEPENDENTLY-CHECKED |
