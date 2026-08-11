# Proof — Theorem B2 (exact finite-observation collision)

**Status:** PROOF-DRAFT (CONFIRMED by OB-02 external review, 2026-08-11 — four notation corrections applied)  
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

**Quartet tail decay (§3):** For each `j`, the quartet `Q(σ₀, T) = {3/4±iT, 1/4±iT}` contributes:

```
δ_j^{off}(T) := O_j(Q(3/4, T))
             = 2[φ_j(3/4+iT) + φ_j(3/4−iT) + φ_j(1/4+iT) + φ_j(1/4−iT)]
             = 4 Re[φ_j(3/4+iT) + φ_j(1/4+iT)].
```

**[CORRECTION from OB-02 review]** The draft's `δ^{off}` included only the `Re ρ = 3/4`
conjugate pair and omitted the `Re ρ = 1/4` pair.  The full symmetric quartet `Q(3/4, T)`
has four elements; by symmetry `ρ ↦ 1−ρ`, the `1/4±iT` pair is always present.  Using
the corrected formula, `d_1(T) = 4[Re(1/(3/4+iT)) + Re(1/(1/4+iT))] > 0` (Lemma 4.1 of
OB-02 review), confirming `d(T) ≠ 0`.

For large `T`, `|φ_j(3/4+iT)| = O(T^{-1})` and `|φ_j(1/4+iT)| = O(T^{-1})`,
so `δ_j^{off}(T) → 0` as `T → ∞`.  (This decay argument from B1 proof.md §2 is
unaffected by the correction.)

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
J_{jk} = A_{jk} = 2(1 − cos(jθ_k)).
```

**[CORRECTION from OB-02 review]** The observation map sums over *all* elements of
the multiset.  The pair `L(t_k) = {1/2+it_k, 1/2−it_k}` contributes:

```
O_j(L(t_k)) = (φ_j(ρ_t) + φ_j(ρ̄_t)) + (φ_j(ρ̄_t) + φ_j(ρ_t))
             = 4 Re φ_j(ρ_t)
             = 4(1 − cos(jθ_k)).
```

So the corrected contribution matrix entry is:

```
C_{jk} := O_j(L(t_k)) = 4(1 − cos(jθ_k)) = 4(1 − T_j(x_k)),
```

where `x_k = cos θ_k`.  The earlier `J_{jk} = 2(1 − cos(jθ_k))` was off by a factor of 2;
the corrected matrix is `C = 2J` (nonsingularity is unchanged).

**Lemma (Li Jacobian full rank — self-contained, corrected).** If `t₁, …, t_m > 0` are
distinct, then `det C ≠ 0` where `C_{jk} = 4(1 − T_j(x_k))`, `x_k = cos θ_k`.

*Proof.*  Let `x_k = cos θ_k ∈ (−1, 1)` (distinct, since `x(t) = (4t²−1)/(4t²+1)` is
strictly increasing with `x'(t) = 16t/(4t²+1)² > 0`).  Using the Chebyshev identity:

```
C_{jk} = 4(1 − T_j(x_k)).
```

**Factor out `(1 − x_k)`.** Since `T_j(1) = 1` for all `j`, we have
`1 − T_j(x) = (1 − x) q_j(x)` for a unique polynomial `q_j ∈ ℝ[x]`.  Then:

```
C_{jk} = 4(1 − x_k) q_j(x_k),
```

so `C = 4 · [q_j(x_k)]_{j,k} · diag(1 − x_k)`.  Since `x_k ∈ (−1,1)`, each
`1 − x_k > 0`, so `diag(1 − x_k)` is invertible.  Thus:

```
rank C = rank [q_j(x_k)]_{j,k=1,...,m}.
```

**Degree and leading coefficient of `q_j`.**  The leading coefficient of `T_j` is
`2^{j−1}`, so `1 − T_j(x) = −2^{j−1} x^j + lower terms`.  Dividing by
`(1−x)` gives `q_j` with leading term `2^{j−1} x^{j−1}` (degree exactly `j−1`,
leading coefficient `2^{j−1} > 0`).  In particular, `{q_1, …, q_m}` is a sequence
of polynomials of degrees `0, 1, …, m−1` with positive leading coefficients.

**Evaluation matrix is nonsingular.**  Express each `q_j` in the monomial basis: there
is a **lower**-triangular change-of-basis matrix `A` (with diagonal entries `2^{j−1} > 0`)
such that `q_j(x) = Σ_{i=1}^{j} a_{ji} x^{i−1}`.  Let `V_{ik} = x_k^{i−1}`.  Then:

```
[q_j(x_k)] = A · V(x_1,…,x_m),
```

where `V(x_1,…,x_m)` is the standard Vandermonde matrix.  Therefore:

```
det C = 4^m · (∏_{k=1}^m (1−x_k)) · det A · det V
      = 4^m · (∏_{k=1}^m (1−x_k)) · 2^{m(m−1)/2} · ∏_{1≤k<l≤m}(x_l − x_k).
```

All factors positive: `1−x_k > 0`, `x_l−x_k > 0` for `k < l` (since `x` is
increasing in `t`).  Therefore `det C ≠ 0`. ☐

**Note on monotonicity (corrected from OB-02).** The draft stated `θ_1 > … > θ_m`
(decreasing) and `x_1 > … > x_m`.  The correct direction: `t_1 < … < t_m` implies
`θ_1 < … < θ_m` (since `θ'(t) = 4/(1+4t²) > 0`) and `x_1 < … < x_m` (since
`x'(t) > 0`).  The *distinctness* of the `x_k` is what matters for the determinant,
and it holds in either direction.

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
rational `T`.  By §4.3 (corrected), `det C ≠ 0` over `ℚ` (where `C_{jk} = 4(1−T_j(x_k))`
and `x_k = (4t_k²−1)/(4t_k²+1) ∈ ℚ`), so `α^ℚ = C^{-1}b ∈ ℚ^m`
where `b = −d(T) ∈ ℚ^m` (rational by Lemma 4.1 of OB-02 review, using corrected quartet formula).

**Key scaling trick.** Let `R = lcm(denominators of α^ℚ_k)`.  Set:

- Replace `Q(σ₀, T)` by `R` copies: `4R` off-line atoms.
- Multiply adjustments: `n_k := R · α^ℚ_k ∈ ℤ` (possibly negative).

This scales `C α^ℚ = b` by `R` and gives `C n + R d(T) = 0` — the scaled
integer vector satisfies the equation exactly.

**Sign resolution (the key insight).** Both adversaries are **constructed** — we are
not fixing `𝒵_+` to be ζ's zeros.

**Construction of `𝒵_+`.** Set the multiplicity buffer:
```
M := max_{k=1,...,m} |n_k|    (well-defined, finite).
```
Let `𝒵_+` be the finite multiset:
```
𝒵_+ := ⊔_{k=1}^{m} M · L(t_k)   (M copies of each critical-line pair).
```
Verification that `𝒵_+ ∈ 𝔛_sym`:
- Locally finite: yes (finite multiset).
- Symmetric under `ρ ↦ ρ̄` and `ρ ↦ 1−ρ`: yes (pairs `1/2 ± it_k` are symmetric).
- Admissibility: finite sum, converges trivially.
- `P(𝒵_+) = 1`: all zeros on the critical line.  ✓

**Construction of `𝒵_-`.**
```
𝒵_- := (⊔_{k=1}^{m} (M + n_k) · L(t_k)) ⊔ R · Q(3/4, T).
```
Every multiplicity `M + n_k ≥ M − |n_k| ≥ 0` is a nonneg integer, so removals are valid.

**Observation equality.** By construction and the corrected quartet formula:
```
O_j(𝒵_-) − O_j(𝒵_+) = Σ_k n_k · C_{jk} + R · d_j(T)
                       = (Cn + R d(T))_j = 0.
```
So `O_Φ(𝒵_-) = O_Φ(𝒵_+)` exactly.  ✓

**Predicate difference.** `P(𝒵_-) = 0` because `Q(3/4, T)` contributes zeros at
`Re ρ = 3/4 ≠ 1/2`.  `P(𝒵_+) = 1`.  ✓

**Admissibility of `𝒵_-`.** The multiset is finite, symmetric, and locally finite.  ✓

**Exact m=2 sanity check (from OB-02 §7).** Take `t₁=1, t₂=2, T=1`.  Then
`x₁ = 3/5`, `x₂ = 15/17`, giving:

```
C = [[8/5,  8/17],
     [128/25, 512/289]],     det C = 3072/7225 ≠ 0.

d(1) = [1216/425, 1763072/180625].

β = C⁻¹(−d(1)) = [−1426/1275, −854/375].

R = 6375,  n = (−7130, −14518),  M = 14518.

Cn + R·d(1) = 0   (exactly).
```

`𝒵_+` has multiplicity 14518 at each pair; `𝒵_-` has multiplicities 7388 and 0
at those pairs, plus 6375 copies of `Q(3/4, 1)`.

**Status: PROOF-DRAFT (integer-sign step RESOLVED; corrections from OB-02 applied).**

---

## §5. Construction summary

The full construction is contained in §4.5.  No additional choices are needed:
`n = m`, `t_k` rational, `T` rational, `σ₀ = 3/4`.  The five steps are:

1. Compute `C_{jk} = 4(1 − T_j(x_k))` with `x_k = (4t_k²−1)/(4t_k²+1) ∈ ℚ`.  ✓
2. Compute corrected `d(T)_j = 4 Re[φ_j(3/4+iT) + φ_j(1/4+iT)] ∈ ℚ`.  ✓
3. Solve `β = −C^{-1} d(T) ∈ ℚ^m`; scale by `R` to get `n ∈ ℤ^m`.  ✓
4. Construct `𝒵_+` with buffer `M = max_k |n_k|`; construct `𝒵_-` with adjusted
   multiplicities and `R` copies of `Q(3/4, T)`.  ✓
5. Verify `C n + R d(T) = 0` exactly (rational arithmetic).  ✓

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
| Quartet contribution — corrected to include 1/4±iT pair (§3) | PROOF-DRAFT ✓ (OB-02 correction applied) |
| Li pair contribution — corrected factor 4 (§4.3, previously factor 2) | PROOF-DRAFT ✓ (OB-02 correction applied) |
| Li Jacobian full rank: det C ≠ 0 (Chebyshev + lower-triangular + Vandermonde) | PROOF-DRAFT ✓ — self-contained |
| Monotonicity direction: x_k increasing in t_k (corrected from draft) | PROOF-DRAFT ✓ (x'(t) = 16t/(4t²+1)² > 0) |
| Coefficient matrix A: lower-triangular (corrected from "upper") | PROOF-DRAFT ✓ |
| Moment Jacobian full rank (§4.4, cosine-Vandermonde) | PROOF-DRAFT ✓ — self-contained |
| Rationality of C and d(T) for rational t_k, T | PROOF-DRAFT ✓ |
| Integer solution via scaling trick (§4.5) | PROOF-DRAFT ✓ |
| 𝒵_+ construction with multiplicity buffer M = max|n_k| | PROOF-DRAFT ✓ |
| 𝒵_- construction (corrected multiset-copy notation) | PROOF-DRAFT ✓ |
| Admissibility + symmetry | PROOF-DRAFT ✓ |
| Observation equality exact: Cn + R·d(T) = 0 | PROOF-DRAFT ✓ |
| Predicate P(𝒵_-) = 0, P(𝒵_+) = 1 | PROOF-DRAFT ✓ |
| Exact m=2 sanity check (OB-02 §7, t₁=1 t₂=2 T=1) | CONFIRMED ✓ (rational arithmetic) |
| Independent exact reconstruction (OB-13, m=2 + m=3 + mutation) | CONFIRMED ✓ INDEPENDENT-CHECKER (Python stdlib fractions, SHA-256-pinned, two routes agree) |
| det C ≠ 0 closed form (OB-13 Lemma 2.3, scaled Vandermonde) | CONFIRMED ✓ |
| Global O_j definition + predicate P made explicit (OB-13) | DONE (see statement.md) |
| Counting-law refinement (§7) | DEFERRED |
| Overall theorem B2 | **CONFIRMED by OB-02 external review (2026-08-11); finite certificate INDEPENDENT-CHECKER by OB-13 (2026-08-11)** |
