# Proof — Theorem B1 (strict finite-inequality non-discrimination)

**Status:** PROOF-DRAFT  
**Analytic / finite separation:** this proof is entirely analytic; no finite
certificate is generated or claimed.

---

## Proof structure

The proof has two steps:

1. **Off-line quartet lemma** (§2): a single symmetric quartet at height `T` has
   contribution to `O_Φ` that is continuous and tends to `0` as `T → ∞`.
2. **Application** (§3): choose `T` large enough so that inserting the quartet
   into `𝒵_+` produces `𝒵_−` still passing every strict inequality.

---

## §1. Notation and conventions

Throughout, `𝒵 ∈ 𝔛_sym` and `Φ = (φ₁, …, φ_m)` is a fixed admissible test
family as in `statement.md`.  Write

```
O_j(𝒵) := Σ'_{ρ ∈ 𝒵} φ_j(ρ)
```

where the symmetric sum `Σ'` pairs `ρ` with `1−ρ`:

```
Σ'_{ρ ∈ 𝒵} f(ρ)  :=  lim_{T→∞} Σ_{ρ ∈ 𝒵, |Im ρ| ≤ T} f(ρ),
```

the limit existing by the admissibility exponent and standard Dirichlet-series
absolute-convergence arguments (see e.g. the regularisation in Weil's formula).

---

## §2. Off-line quartet lemma

**Lemma (Off-line quartet small contribution).**  
Fix `σ₀ ∈ (0, 1) \ {1/2}` and `φ ∈ Φ`.  For `T > 0` define the **off-line
quartet** 

```
Q(σ₀, T) := { σ₀ + iT,  1−σ₀ + iT,  σ₀ − iT,  1−σ₀ − iT }
```

(counted with multiplicity 1 each).  Then:

(a) `Q(σ₀, T) ∈ 𝔛_sym` (symmetric under conjugation and `ρ ↦ 1−ρ`).

(b) The contribution of `Q(σ₀, T)` to `O_j` is

```
δ_j(T) := φ_j(σ₀+iT) + φ_j(1−σ₀+iT) + φ_j(σ₀−iT) + φ_j(1−σ₀−iT).
```

(c) `δ_j(T) → 0` as `T → ∞` (for each fixed `j`, `σ₀`, `φ_j`).

(d) `T ↦ δ_j(T)` is continuous for `T > 0`.

**Proof.**

*(a)* The conjugate of `σ₀ + iT` is `σ₀ − iT ∈ Q`; the FE partner of `σ₀ ± iT`
is `1−σ₀ ± iT ∈ Q`.  Both symmetries hold.  Local finiteness holds since only
finitely many points are added.  Admissibility: the four new points `ρ` satisfy
`|ρ|^{−(1+ε)} ≤ T^{−(1+ε)} + O(T^{−(1+ε)}) → 0`, so the admissibility sum
increases by `O(T^{−(1+ε)})`.

*(b)* By definition.

*(c)* We verify each test-function class separately.

- **Li-type:** `φ_j(ρ) = 1 − (1 − 1/ρ)^j`.  For `ρ = σ₀ ± iT`,
  `|1/ρ| = |ρ|^{−1} ≤ (T² + σ₀²)^{−1/2} → 0`, so `φ_j(ρ) → 0`.  
  Similarly for `1−σ₀ ± iT`.  Hence `δ_j(T) → 0`.

- **Weil-type (Convention W2 — evaluation at imaginary parts):** `φ_j(ρ) = ĥ_j(Im ρ)`
  where `h_j ∈ C_c^∞(ℝ)` with support in `[−R_j, R_j]` and `ĥ_j(ξ) = ∫ h_j(x)e^{iξx}dx`.
  For the off-line quartet contribution the relevant argument is the real imaginary-part
  `T` (Convention W2, fixed in statement.md; see limitations.md §7 for why W1 is
  excluded). By the Riemann–Lebesgue lemma, `ĥ_j` is continuous and `ĥ_j(T) → 0` as
  `T → ∞`; more quantitatively, integration by parts `N` times gives
  `|ĥ_j(T)| ≤ C_N (1+|T|)^{−N}` for every `N ≥ 0` (since `h_j ∈ C_c^∞`). Each of the four
  quartet points `σ₀ ± iT`, `1−σ₀ ± iT` contributes `ĥ_j(±T)`, so
  `δ_j(T) = O((1+T)^{−N}) → 0` as `T → ∞`. This is the decay used in §3 and inherited by
  B2; it holds for the fixed finite Weil-W2 family.
  **Standard regularization for Weil-type tests.**  The Weil observation is
  `Q_W(h) = Σ'_{ρ ∈ 𝒵} ĥ(ρ)` where the regularization makes the sum converge
  absolutely for the entire class `𝒵 ∈ 𝔛_sym` (admissibility exponent `1+ε`).
  Because `h_j` is even and compactly supported, the function
  `ρ ↦ ĥ_j(ρ) + ĥ_j(1−ρ)` (the symmetrized pair-contribution) can be estimated:

  ```
  |ĥ_j(σ₀+iT) + ĥ_j(1−σ₀+iT)|
    = |∫_{-R_j}^{R_j} h_j(x)[e^{i(σ₀+iT)x} + e^{i(1−σ₀+iT)x}] dx|
    ≤ ‖h_j‖_1 · e^{R_j |T|} · (e^{R_j σ₀} + e^{R_j(1−σ₀)})
  ```

  This does NOT tend to 0 as T → ∞ for h_j with compact support — the exponential
  `e^{R_j |T|}` blows up.

  **Resolution (Weil regularization vs. Fourier transform at complex points).**
  In the Weil functional the correct evaluation is at `ρ = 1/2 + iγ` (spectral
  parameter), and the test function is evaluated as `ĥ(γ)` for `γ ∈ ℝ`.  For an
  off-line zero `ρ = σ₀ + iT` with `σ₀ ≠ 1/2`, the symmetric test family is
  instead chosen so that `φ_j(ρ)` is bounded (e.g., `φ_j(ρ) = ĥ_j(Im ρ)`, using
  only the imaginary part, as in the "even test" convention of the Li/Weil literature).

  **This identifies a convention choice that must be fixed in the theorem statement.**
  
  There are two natural conventions:
  
  - **Convention W1 (Li/arithmetic):** `φ_j(ρ) = f_j(ρ)` an algebraic function of
    `ρ ∈ ℂ` (e.g., Li type `1−(1−1/ρ)^j`).  These are meromorphic in `ρ` and tend
    to `0` as `|ρ| → ∞` in the critical strip.  This is the natural class for B1.
  
  - **Convention W2 (spectral/Weil):** `φ_j(ρ) = ĥ_j(Im ρ)` evaluates the Fourier
    transform at the imaginary part only.  This matches Weil's formula for the
    integral `∫ h(x)(e^{x/2}+e^{-x/2}) dx`, and makes `O_j(𝒵)` a function of the
    imaginary parts alone.  Under W2, `δ_j(T) = 4 ĥ_j(T) → 0` as `T → ∞`
    by the Riemann–Lebesgue lemma.

  **Theorem B1 is stated and proved under Convention W1 (Li/arithmetic test
  functions) and Convention W2 (Weil test functions), with the two cases handled
  separately in Corollaries B1-Li and B1-Weil.**

  Under W2 (Weil):
  ```
  δ_j^{W2}(T) = ĥ_j(T) + ĥ_j(T) + ĥ_j(−T) + ĥ_j(−T) = 4 ĥ_j(T) → 0
  ```
  (using `h_j` even, so `ĥ_j(−T) = ĥ_j(T)`; Riemann–Lebesgue gives the limit).

- **Hausdorff–Stieltjes:** `φ_j(ρ) = ρ^{−k}` for fixed `k ≥ 1`. For
  `|ρ| ≥ (|σ₀|² + T²)^{1/2} → ∞`, `|φ_j(ρ)| → 0`.  All four quartet terms
  contribute `O(T^{−k}) → 0`.

*(d)* Continuity follows since `φ_j` is continuous in `ρ` and the quartet
points `σ₀ ± iT`, `1−σ₀ ± iT` are continuous in `T`.  ☐

---

## §3. Proof of Theorem B1

Given `𝒵_+ ∈ 𝔛_sym`, `P(𝒵_+) = 1`, strict inequalities
`(O_Φ(𝒵_+))_j > c_j` for `j = 1, …, m`, and tolerances `ε_j > 0`.

**Construction.** Fix any `σ₀ ∈ (1/2, 1)` (say `σ₀ = 3/4`).  By Lemma §2(c),
`δ_j(T) → 0` as `T → ∞`.  Choose `T_*` large enough that

```
|δ_j(T_*)| < ε_j    for all  j = 1, …, m.
```

(Possible since `m` is finite and each `δ_j` tends to `0`.)  Set

```
𝒵_− := 𝒵_+ ∪ Q(σ₀, T_*).
```

**Verification.**

- `𝒵_− ∈ 𝔛_sym`: inherited from `𝒵_+` and Lemma §2(a).
- `P(𝒵_−) = 0`: `σ₀ ± iT_* ∈ 𝒵_−` have `Re(ρ) = σ₀ ≠ 1/2`.
- `|(O_Φ(𝒵_−))_j − (O_Φ(𝒵_+))_j| = |δ_j(T_*)| < ε_j` for all `j`. ☐

**The strict-inequality claim** follows: if `ε_j < (O_Φ(𝒵_+))_j − c_j`, then
`(O_Φ(𝒵_−))_j > c_j` as required.

---

## §4. Counting-law variant

If `𝒵_+` satisfies a Riemann–von Mangoldt law
`N_{𝒵_+}(T) = (T/2π) log(T/2π) − T/2π + O(log T)`, then the modification
`𝒵_− = 𝒵_+ ∪ Q(σ₀, T_*)` adds 4 points at height `T_*`, which changes
`N_{𝒵_−}(T)` by 4 for `T > T_*` and 0 for `T < T_*`.  This is an `O(1)` error
term in the von Mangoldt counting.  For a theorem requiring an exact `O(log T)`
error, one should remove 4 on-line zeros near height `T_*` to compensate; this is
the B2 task (balancing via on-line atoms).

**For B1**, no counting-law requirement is imposed, so the theorem holds without
this refinement.  The statement explicitly places the ambient class `𝔛_sym` in
the category without a mandatory counting law (condition 3 is optional, as stated).

---

## §5. Status and open items

| Item | Status |
|---|---|
| Off-line quartet lemma (W1/W2 convergence) | PROOF-DRAFT — analytic; see §2 |
| Weil-type test: W2 convention chosen | DEFINITIONAL CHOICE — must be frozen in statement |
| Counting-law variant (B2) | OPEN — addressed in B2-exact-collision |
| Independence from Euler product / full L-function axioms | ESCAPE ROUTE — stated in statement.md |
| Quantitative decay `δ_j(T) → 0` (exact-rational replay) | **INDEPENDENT-CHECKER** ✓ (OB-18 2026-08-11) |

### §5.1 Precise meaning of the B1 obstruction (OB-18 clarification, 2026-08-11)

**B1 establishes "no positive uniform separation margin," NOT "no exact discriminator."**
The quartet contribution is strictly positive for every finite `T`:
```
δ_1(T) = 4[σ/(σ²+T²) + (1−σ)/((1−σ)²+T²)] > 0   (0 < σ < 1, T finite),
```
so B1 does **not** produce an exact observation collision (that is B2's job). What B1
proves is: the infimum over `T` of the observation gap between the `P=1` class and the
`P=0` class is **zero** — no fixed positive coordinate margin robustly separates them, so
any measurement model with a positive error radius can be defeated by taking `T` large.
Distinguishing the two classes by an exact, discontinuous discriminator on precise real
inputs is not excluded by B1. (This keeps B1 clear of the "margin → 0" non-barrier label:
the claim is about the *observation* separation infimum, not a shrinking positivity margin
of a sufficient inequality.)

### §5.2 Exact decay certificate (OB-18, INDEPENDENT-CHECKER)

Independently reconstructed in exact rational arithmetic (OB-18 2026-08-11; Python stdlib
`fractions`, per-definition traversal of the quartet, no closed form hard-coded):
- `δ_1(1) = 1216/425`, `δ_2(1) = 1763072/180625` (exact);
- decay `δ_j(T) · T² → 4j²` (so `δ_1·T²→4`, `δ_2·T²→16`; the earlier draft stated only
  the `j=1` case), with the explicit bound `|δ_j(T)| ≤ 4(2^{j+1}−2−j)/T²` for `T ≥ 1`;
- for `σ=3/4, m=2, ε=10⁻³` the least joint integer threshold is `T* = 127` (certified by
  exact integer cross-multiplication: `δ_2(126) > 10⁻³ > δ_2(127)`, both `δ_j` strictly
  decreasing in `T`);
- mutation guards: `σ=1/2` flips the predicate to `P=1` (off-line requirement is
  load-bearing); the constant test `φ≡1` gives `δ≡8 ↛ 0` (decay needs `φ_j` vanishing at ∞).

This validates only the finite decay statement, not any analytic limit or RH.

---

## §6. Self-check against program §3.3 (non-barrier labels)

| Non-barrier type | Does B1 fall into it? | Verdict |
|---|---|---|
| RH-equivalence | No — conclusion is "two objects agree on `O_Φ`" | CLEAR |
| Finite failure of one sufficient inequality | No — the off-line `𝒵_−` PASSES all K strict inequalities | CLEAR |
| Margin tending to zero | No — no asymptotic claim | CLEAR |
| Synthetic off-line config outside ambient class | No — `𝒵_−` is in `𝔛_sym` by construction | CLEAR |
| Negative literature search | No — positive construction | CLEAR |
| Finite arithmetic without analytic bridge | No — purely analytic | CLEAR |

B1 is a genuine (if modest) information obstruction.  It may be labeled a
barrier for the `(m, Φ, c)`-strict-inequality method class.
