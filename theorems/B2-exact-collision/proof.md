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

### §4.3 Li-type test: self-contained Vandermonde reduction (PROOF-DRAFT)

For Li-type tests `φ_j(ρ) = 1 − (1−1/ρ)^j`, `j = 1, …, m`:

```
A_{jk} = φ_j(1/2+it_k) + φ_j(1/2−it_k)
        = 2 Re[1 − (1 − 1/(1/2+it_k))^j]
        = 2 − 2 Re[(1 − 2/(1+2it_k))^j].
```

Let `w_k = (2it_k − 1)/(2it_k + 1)`.  Since `|2it_k±1|² = 1+4t_k²`, we have
`|w_k| = 1`, so `w_k = e^{iθ_k}` with `θ_k = 2 arctan(2t_k) − π ∈ (−π, 0)` for
`t_k > 0`.  Using `cos(jθ) = Re(e^{ijθ})`:

```
J_{jk} = 2 − 2 cos(jθ_k) = 2(1 − cos(jθ_k)).
```

**Lemma (Li Jacobian full rank — self-contained).** If `t₁, …, t_m > 0` are
distinct, then `det J ≠ 0`.

*Proof.*  Let `x_k = cos θ_k ∈ (−1, 1)` (distinct, since `θ ↦ cos θ` is strictly
monotone on `(−π, 0)` and the map `t_k ↦ θ_k` is strictly monotone).  Using the
Chebyshev polynomial identity `cos(jθ) = T_j(cos θ)`:

```
J_{jk} = 2(1 − T_j(x_k)).
```

**Factor out `(1 − x_k)`.** Since `T_j(1) = 1` for all `j`, we have
`1 − T_j(x) = (1 − x) Q_j(x)` for a unique polynomial `Q_j ∈ ℝ[x]`.  Then:

```
J_{jk} = 2(1 − x_k) Q_j(x_k),
```

so `J = 2 · [Q_j(x_k)]_{j,k} · diag(1 − x_k)`.  Since `x_k ∈ (−1,1)`, each
`1 − x_k > 0`, so `diag(1 − x_k)` is invertible.  Thus:

```
rank J = rank [Q_j(x_k)]_{j,k=1,...,m}.
```

**Degree and leading coefficient of `Q_j`.**  The leading coefficient of `T_j` is
`2^{j−1}`, so `1 − T_j(x) = −2^{j−1} x^j + \text{lower terms}`.  Dividing by
`(1−x)` gives `Q_j` with leading term `2^{j−1} x^{j−1}` (degree exactly `j−1`,
leading coefficient `2^{j−1} > 0`).  In particular, `{Q_1, …, Q_m}` is a sequence
of polynomials of degrees `0, 1, …, m−1` with positive leading coefficients.

**Evaluation matrix is nonsingular.**  Since `{Q_1, …, Q_m}` have degrees
`0, 1, …, m−1`, they are a basis for `ℝ_{≤m−1}[x]` (any `m` polynomials with
distinct degrees 0 through `m−1` are linearly independent).  Express each `Q_j`
in the monomial basis: there is an upper-triangular change-of-basis matrix `U`
(with diagonal entries `2^{j−1} > 0`) such that `Q_j(x) = Σ_{i≤j} U_{ji} x^{i−1}`.
Then:

```
[Q_j(x_k)] = U · [x_k^{i−1}]_{i,k=1,...,m} = U · V(x_1,…,x_m),
```

where `V(x_1,…,x_m)` is the standard Vandermonde matrix.  Therefore:

```
det[Q_j(x_k)] = det(U) · det V(x_1,…,x_m)
              = (∏_{j=1}^m 2^{j−1}) · ∏_{1≤k<l≤m}(x_l − x_k).
```

Both factors are nonzero: `∏ 2^{j−1} = 2^{m(m−1)/2} > 0`, and `∏(x_l − x_k) ≠ 0`
since `x_1, …, x_m ∈ (−1,1)` are distinct. Therefore `det[Q_j(x_k)] ≠ 0`, so
`det J ≠ 0`. ☐

**Rationality.** For rational `t_k`, `w_k = (2it_k−1)/(2it_k+1)` has rational real
and imaginary parts; `cos(jθ_k) = Re(w_k^j)` is rational.  Hence `J ∈ ℚ^{m×m}` and
`det J ∈ ℚ \setminus {0}`.

**Status: PROOF-DRAFT (self-contained — no external citation required).**  The
argument uses only: (a) the Chebyshev identity `cos(jθ) = T_j(cos θ)`, (b)
elementary polynomial long division `(1−T_j)/(1−x) = Q_j`, (c) leading-coefficient
computation by induction on `T_j`'s recurrence, and (d) Vandermonde
nonsingularity for distinct points.  All four are standard and can be verified
from first principles.

**Discovery-tier confirmation.** Exact rational computation in
`discovery/jacobian_analysis.py` verified `det J ≠ 0` for Li m=3 and m=5 at
multiple rational heights (see `discovery/jacobian_rank_results.md`).
This is DISCOVERY TIER only; the analytic argument above is the theorem.

### §4.4 Moment-type test: cosine-Vandermonde (PROOF-DRAFT, self-contained)

For moment-type tests `φ_k(ρ) = ρ^{−k}`, `k = 1, …, m`:

```
A_{jk} = 2 Re[(1/2 + it_k)^{−j}].
```

Write `ρ_k = 1/2 + it_k = r_k e^{iφ_k}` with `r_k = (1/4 + t_k²)^{1/2}` and
`φ_k = arctan(2t_k) ∈ (0, π/2)` (for `t_k > 0`).  Then:

```
A_{jk} = 2 r_k^{-j} cos(j φ_k).
```

Let `D = diag(r_k^{-j})_{k=1,...,m}` (positive diagonal), so `J = 2 [cos(jφ_k)] · D`.
Since `D` is invertible, `rank J = rank [cos(jφ_k)]_{j,k=1,...,m}`.

**Lemma (cosine-Vandermonde).** If `φ₁, …, φ_m ∈ (0, π/2)` are distinct, then
`det[cos(jφ_k)]_{j,k=1,...,m} ≠ 0`.

*Proof.*  The same Vandermonde reduction as §4.3 applies: `cos(jφ) = T_j(cosφ)`,
so `[cos(jφ_k)] = [T_j(x_k)]` with `x_k = cos φ_k ∈ (0,1)` distinct.
The matrix `[T_j(x_k)]` differs from `[x_k^{j-1}]` by the upper-triangular
Chebyshev-to-monomial change-of-basis `U` (leading coefficient `2^{j-1}`):
`[T_j(x_k)] = U · V(x_1,…,x_m)`.  So
`det[T_j(x_k)] = det(U) · det V = (∏ 2^{j-1}) · ∏_{k<l}(x_l−x_k) ≠ 0`. ☐

**Status: PROOF-DRAFT (self-contained).**

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
| Li Jacobian full rank (§4.3, Vandermonde reduction) | PROOF-DRAFT ✓ — self-contained, no external citation |
| Moment Jacobian full rank (§4.4, cosine-Vandermonde) | PROOF-DRAFT ✓ — self-contained |
| Integer solution via scaling trick (§4.5) | PROOF-DRAFT ✓ (sign resolved) |
| 𝒵_+ construction with multiplicity buffer | PROOF-DRAFT ✓ |
| 𝒵_- construction (add/remove/quartet) | PROOF-DRAFT ✓ |
| Admissibility + symmetry (§6) | PROOF-DRAFT ✓ |
| Observation equality exact (§4.5) | PROOF-DRAFT ✓ |
| Predicate P(𝒵_-) = 0, P(𝒵_+) = 1 | PROOF-DRAFT ✓ |
| Counting-law refinement (§7) | DEFERRED |
| Gate A status | PROOF-DRAFT complete — ready for independent check |
