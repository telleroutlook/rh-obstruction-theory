# Theorem B1 — Strict Finite-Inequality Non-Discrimination

**Mathematical status:** PROOF-DRAFT (Gate-A CONDITIONAL, OB-23 2026-08-11: qualitative core CONFIRMED after local repairs — Σ′ convention corrected to R-atom, anchors fixed, RH-example removed; advances to INDEPENDENTLY-CHECKED once §7 mods integrated + corrected checker returns)  
**Computational status:** REPRODUCIBLE (OB-18 checker used B2's doubled convention; corrected R-atom checker requested as OB-24 before restoring INDEPENDENT-CHECKER)  
**Theorem ID:** B1-finite-inequality  
**Program ref:** §7, §7.B.2.B1  
**Paper target:** Paper A (conditional on B2; else lemma of Paper C)

---

## Cross-theorem Σ′ convention note (OB-23, 2026-08-11) — MANDATORY

**B1 and B2 use different (each internally-valid) Σ′ conventions; do not paste numerical
anchors between them.**
- **B1 (this theorem) — R-atom:** `O_j(𝒵) = Σ'_{ρ∈𝒵} φ_j(ρ)`, the sum of `φ_j` over the
  atoms; `Σ'` is the convergence regularization (pairing `ρ` with `1−ρ` to make the
  conditionally-convergent sum well-defined), NOT a doubling. On the quartet this is the
  four-term `δ_j`. This is the Weil-correct reading: a multiset already containing the
  FE-partner `1−ρ` counts each atom once.
- **B2 — R-symm:** `O_j(𝒵) = Σ_{ρ∈𝒵} [φ_j(ρ) + φ_j(1−ρ)]`, which double-counts on a
  multiset closed under `ρ↦1−ρ`, hence is a factor of 2 larger.
- **Consequence:** B1 anchors (`δ_1(1)=608/425`, `T*=90`, `δ_j·T²→2j²`) are in R-atom;
  B2 anchors (`C`, `d`, `1216/425`, …) are in R-symm. B2's exact collision `Cn+Rd=0` is
  **scale-invariant** (C→2C, d→2d leaves β,R,n,M and the collision unchanged), so B2's
  Gate-A PASS and checker are unaffected by the convention; only its displayed C,d are
  doubled relative to B1. **Never reuse one theorem's δ/C/d numbers under the other's
  convention** (this is exactly the error OB-23 caught).

---

## Setting

**Ambient class `𝔛_sym`.**  A locally finite multiset `𝒵` in `ℂ` (with
multiplicity) satisfies `𝒵 ∈ 𝔛_sym` if:

1. **Conjugation symmetry:** `ρ ∈ 𝒵  ⟹  ρ̄ ∈ 𝒵` (with equal multiplicity).
2. **Functional-equation symmetry:** `ρ ∈ 𝒵  ⟹  1−ρ ∈ 𝒵` (with equal multiplicity).
3. **Convergence exponent:** every `ρ ∈ 𝒵` has `0 < Re(ρ) < 1`, and
   `Σ_{ρ ∈ 𝒵} |ρ|^{−(1+ε)} < ∞` for some fixed `ε ∈ (0,1)` (admissibility).
4. **Finite-prefix agreement (optional):** the first `K_0` zeros of `𝒵` ordered by
   `|Im(ρ)|` agree with the verified ordinates of `ζ`.  The theorem holds with
   **or** without this constraint; when imposed, `K_0` is a named parameter.

**Target predicate:**
```
P(𝒵) = 1  ⟺  Re(ρ) = 1/2  for every  ρ ∈ 𝒵.
```

**Finite test family.**  Fix `m ≥ 1` and a family
`Φ = (φ₁, …, φ_m)` of test functions.  Each `φ_j` belongs to one of the
following classes:

- **Li-type:** `φ_j(ρ) = 1 − (1−1/ρ)^j` (Li coefficient index `j ∈ {1,…,K}`);
- **Weil-type:** `φ_j = ĥ_j` the Fourier transform of a compactly-supported
  even `h_j ∈ C_c^∞(ℝ)`, with `Q_W(h_j) = Σ'_{ρ ∈ 𝒵} h_j(ρ)` (Weil-sum convention);
- **Hausdorff–Stieltjes:** fixed-order differences of the moment sequence
  `(μ_k)_{k=0}^{K}` with `μ_k = Σ'_{ρ} ρ^{-k}`;

where `Σ'` denotes the symmetric regularization (pair `ρ` with `1−ρ`) as in
Weil's formula.  The summation convention and test-function decay are part of
the theorem statement.

**Observation map:**
```
O_Φ : 𝔛_sym → ℝ^m,   O_Φ(𝒵) = (Σ'_{ρ ∈ 𝒵} φ_j(ρ))_{j=1}^{m}.
```

---

## Theorem B1 (strict finite-inequality non-discrimination)

**Theorem B1.**  Fix any `m ≥ 1`, any admissible test family `Φ` as above, and
any `𝒵_+ ∈ 𝔛_sym` with `P(𝒵_+) = 1` (i.e. a "good" reference multiset — e.g.
the formal zero multiset of `ζ`) such that `O_Φ(𝒵_+) ∈ ℝ^m` is well-defined
and every component satisfies a *strict* inequality `(O_Φ(𝒵_+))_j > c_j` for
constants `c_j ∈ ℝ`.  Then there exists `𝒵_− ∈ 𝔛_sym` with `P(𝒵_−) = 0`
(at least one off-line zero) and

```
|(O_Φ(𝒵_−))_j − (O_Φ(𝒵_+))_j| < ε_j   for j = 1, …, m,
```

for any prescribed tolerances `ε_j > 0`.  In particular, if `c_j > 0` and
`ε_j < (O_Φ(𝒵_+))_j − c_j`, then `𝒵_−` still passes every strict inequality
`(O_Φ(𝒵_−))_j > c_j`.

**Scope / limitation (mandatory).**  This theorem holds for a **fixed** `m` and
**fixed** `Φ`.  It does not exclude a method that uses an unbounded hierarchy
`m → ∞` of tests, an adaptive stopping rule, or a proved uniform tail bound
converting the infinite sum to a finite one.

---

## Corollaries

**Cor B1-Li.**  For every fixed `K`, the first `K` Li inequalities
`λ_j = O_Φ(𝒵)_j ≥ 0` (j = 1, …, K) do not determine critical-line support
in `𝔛_sym`: there exists `𝒵_− ∈ 𝔛_sym` with at least one off-line zero that
also satisfies all `K` strict positivity conditions.

**Cor B1-Weil.**  For any fixed finite family of compactly-supported Weil test
functions, the same non-discrimination holds.

---

## Escape route (program §3.2, §5 Rule 5)

The theorem does not apply to methods that additionally use:

1. **Euler product discipline:** the exact factorisation `Σ Λ(n) n^{-s}` constrains
   which multisets `𝒵` can arise; `𝔛_sym` admits members with no Euler product.
2. **Functional equation + gamma factor (Ξ-symmetry):** order-one entire functions
   realizing `𝒵` subject to `F(1/2+iz) = F(1/2−iz)` and exponential-type control.
3. **Coefficient arithmetic:** Dirichlet coefficient integrality and multiplicativity.
4. **Infinite test hierarchy:** a method with unbounded `m` (all Li / all Weil tests) is
   not limited by a fixed-`K` result.
5. **Effective tail modulus:** a proved bound `|Σ_{j>K} φ_j(ρ)| ≤ T(K)` with
   `T(K) → 0` supplies information not in the finite record.

A "successful approach" (in the sense of the program) must therefore add at
least one of the above.
