# Problem OB-23 — B1 Gate-A package: independent review of the finite-inequality non-discrimination

**Type:** Gate-A independent mathematical review (whole-theorem inspection).

**What this is.** A request to **independently inspect Theorem B1** — the strict
finite-inequality non-discrimination result — as a coherent whole, and issue a **Gate-A
verdict**: is it correct, self-contained, non-circular, RH-free, and stated with the
honest strength? B1's quantitative core (the off-line quartet contribution `δ_j(T) → 0`)
is already independently certified by an exact-rational checker (prior review OB-18,
re-run in-repo). This review targets the analytic assembly and the precise logical claim.

**Precise-meaning constraint (OB-18, mandatory).** B1 must be judged as proving **"no
positive uniform separation margin"**, NOT "an exact observation collision". For every
finite `T`, the quartet contribution is strictly nonzero (`δ_1(T) > 0`), so B1 does not
produce an exact collision — that is B2's job. B1's claim is: `inf_T` of the observation
gap between the `P=1` class and the `P=0` class is `0`, so no fixed positive coordinate
margin robustly separates them. Confirm the writeup states exactly this and does not
overclaim an exact collision.

**Non-circularity (mandatory).** RH is not assumed. `𝒵_+` may be *any* member of the
ambient class with `P(𝒵_+)=1` (e.g. the formal ζ-zero multiset, but its zeros are not
assumed on-line and no ζ analytic property is used). No Euler product, functional
equation, or zero location enters. Confirm no hidden RH input.

---

## All definitions (self-contained — everything is here)

### Ambient class
A locally finite multiset `𝒵 ⊂ {0 < Re s < 1}` (with multiplicity) is in `𝔛_sym` iff:
(1) `ρ ∈ 𝒵 ⟹ ρ̄ ∈ 𝒵` (equal mult); (2) `ρ ∈ 𝒵 ⟹ 1−ρ ∈ 𝒵` (equal mult); (3)
admissibility `Σ_{ρ∈𝒵} |ρ|^{−(1+ε)} < ∞` for some fixed `ε ∈ (0,1)`. Predicate:
`P(𝒵)=1` iff every `ρ ∈ 𝒵` has `Re ρ = 1/2`, else `P(𝒵)=0`.

### Observation (symmetric Σ')
For a fixed finite test family `Φ = (φ_1,…,φ_m)`,
```
O_j(𝒵) = Σ'_{ρ∈𝒵} φ_j(ρ),   Σ'_{ρ} f(ρ) := lim_{T→∞} Σ_{ρ∈𝒵, |Im ρ|≤T} f(ρ),
```
the limit existing by admissibility (3) for the two admissible test conventions below.

### Two test conventions (both in scope)
- **W1 (Li / arithmetic):** `φ_j(ρ) = 1 − (1−1/ρ)^j` (or moment `ρ^{−k}`); meromorphic in
  ρ, `→ 0` as `|ρ| → ∞` in the strip.
- **W2 (Weil / spectral):** `φ_j(ρ) = ĥ_j(Im ρ)`, `h_j ∈ C_c^∞(ℝ)` even, `ĥ_j` its Fourier
  transform; `O_j` becomes a function of the imaginary parts. Under W2, `ĥ_j → 0` at ∞
  (Riemann–Lebesgue).
(The theorem is stated separately for W1 and W2. A NAIVE Weil evaluation `ĥ_j` at the
*complex* point `σ_0+iT` blows up like `e^{R_j T}`; the W2 convention — evaluate at the
imaginary part — is the correct one and must be the stated convention. Confirm this is not
fudged.)

### The off-line quartet
For `σ_0 ∈ (1/2,1)` (take `σ_0 = 3/4`) and `T > 0`:
`Q(σ_0,T) = {σ_0+iT, 1−σ_0+iT, σ_0−iT, 1−σ_0−iT}` — four non-real, non-on-line points,
symmetric under conjugation and `ρ↦1−ρ`, so `Q ∈ 𝔛_sym`. Its contribution:
`δ_j(T) = φ_j(σ_0+iT)+φ_j(1−σ_0+iT)+φ_j(σ_0−iT)+φ_j(1−σ_0−iT)`.

---

## The claimed theorem (B1)

For any fixed finite admissible `Φ` (W1 or W2), any `𝒵_+ ∈ 𝔛_sym` with `P(𝒵_+)=1` and
strict inequalities `(O_Φ(𝒵_+))_j > c_j`, and any tolerances `ε_j > 0`: there exists
`𝒵_− ∈ 𝔛_sym` with `P(𝒵_−)=0` and `|(O_Φ(𝒵_−))_j − (O_Φ(𝒵_+))_j| < ε_j` for all `j`
(so if `ε_j < (O_Φ(𝒵_+))_j − c_j`, `𝒵_−` still passes every strict inequality). Precise
meaning: the two predicate classes are **not separated by any positive uniform margin**
under `O_Φ`.

---

## Links to inspect

**Link A (Σ' well-defined).** For `𝒵 ∈ 𝔛_sym` and admissible `Φ`, `O_j(𝒵)` converges.
For W1, `|φ_j(ρ)| = O(|ρ|^{−1})` (Li) or `O(|ρ|^{−k})` (moment), so the sum is dominated by
`Σ|ρ|^{−(1+ε)} < ∞`. For W2, `φ_j` is bounded and `ĥ_j` has rapid decay in `Im ρ`; combined
with admissibility the sum converges. **Confirm the convergence for both conventions.**

**Link B (quartet membership + decay).** `Q(σ_0,T) ∈ 𝔛_sym` (all four symmetries, local
finiteness, admissibility increment `O(T^{−(1+ε)})`); `δ_j(T)` continuous in `T`; and
`δ_j(T) → 0` as `T → ∞`: W1 via `|1/ρ| → 0`; W2 via `δ_j^{W2}(T) = 4ĥ_j(T) → 0`
(Riemann–Lebesgue, `h_j` even). **Confirm decay for both conventions; confirm the naive
complex-point Weil evaluation is NOT used.**

**Link C (construction + verification).** Given `ε_j > 0`, finiteness of `m` lets one pick
`T_*` with `|δ_j(T_*)| < ε_j` for all `j` simultaneously. Then `𝒵_− = 𝒵_+ ⊔ Q(σ_0,T_*)`
satisfies: `𝒵_− ∈ 𝔛_sym`; `P(𝒵_−)=0` (off-line atoms at `Re = σ_0 ≠ 1/2`);
`|O_j(𝒵_−) − O_j(𝒵_+)| = |δ_j(T_*)| < ε_j`. **Confirm.**

**Link D (precise meaning, OB-18).** `δ_1(T) > 0` for every finite `T` (e.g. W1:
`δ_1(T) = 4Re[φ_1(σ_0+iT)+φ_1(1−σ_0+iT)] > 0`), so B1 gives **no exact collision** but
`inf_T |δ_j(T)| = 0` — no positive uniform margin. **Confirm the theorem is stated at this
strength and not overclaimed as exact collision.**

---

## Gate-A questions (the deliverable)

### Q1 — Hidden gap / circularity / RH-import
Does any step assume RH, an RH-equivalent, or a ζ-zero location? (`𝒵_+` is an arbitrary
`P=1` member; the quartet is explicitly constructed off-line.) Confirm or exhibit the leak.

### Q2 — Convention correctness
Confirm the W1 and W2 cases are each handled correctly, that the naive Weil evaluation at a
complex point (which blows up like `e^{R_j T}`) is explicitly NOT the convention used, and
that the theorem statement fixes W1/W2 as the admissible classes (an unrestricted "any test
function" would be false — e.g. a constant test gives `δ ≡ 4 ↛ 0`). Confirm the class is
correctly restricted.

### Q3 — Σ' convergence and admissibility
Confirm the admissibility exponent `ε ∈ (0,1)` genuinely makes `O_j` converge for both
conventions, and that adjoining the finite quartet keeps `𝒵_−` admissible.

### Q4 — Precise meaning and scope honesty
Confirm B1 is stated as "no positive uniform separation margin" (not exact collision — that
is B2), and that the scope/limitations are correct: (a) fixed finite `Φ`, fixed `m` (the
infinite Li/Weil hierarchy escapes); (b) no Euler product / functional equation / coeff
arithmetic; (c) `O(1)` counting-law perturbation only (no counting law is imposed on
`𝔛_sym`); (d) B1 is about the observation-separation infimum, keeping it clear of the
"margin → 0" non-barrier label (the claim is about the observation gap, not a shrinking
positivity margin of a sufficient inequality).

### Q5 — Gate-A verdict
Given Links A–D and Q1–Q4: does B1 constitute a correct, self-contained, non-circular
finite non-discrimination theorem at the stated (uniform-margin) strength — should its
mathematical status advance from PROOF-DRAFT toward INDEPENDENTLY-CHECKED? Or does a
specific gap block it?

---

## Numerical anchor (sanity only — already certified by OB-18)

W1, `σ_0 = 3/4`, Li `φ_1(ρ)=1/ρ`: `δ_1(1) = 1216/425 ≈ 2.861`; `δ_1(T)·T² → 4` (more
generally `δ_j(T)·T² → 4j²`); for `m=2, ε=10^{-3}` the least joint integer threshold is
`T* = 127`. These are exact-rational-certified in
`theorems/B1-finite-inequality/` (OB-18; see B1 proof.md §5.2). The Gate-A deliverable is
the whole-theorem judgment (Links A–D, Q1–Q5), not a re-run of this arithmetic.

---

## Acceptance criteria

1. **GATE-A PASS:** Links A–D confirmed, Q1–Q5 answered with no blocking gap; verdict
   "advance B1 toward INDEPENDENTLY-CHECKED." State any required textual conditions.

2. **GATE-A CONDITIONAL:** the chain is correct but a specific textual fix is required
   (e.g. tighten the convention statement, or the precise-meaning wording). Give the exact
   edit.

3. **GATE-A BLOCKED:** a genuine gap, circularity, RH-import, or overclaim (e.g. B1 stated
   as an exact collision) exists. Identify it, exhibit it, give the minimal repair.

All outcomes decisive. A verdict of "PASS at the uniform-margin strength, provided the
statement does not claim exact collision" is exactly the intended scope — do not treat
B1's weaker-than-B2 conclusion as a defect; it is the honest strength of this theorem.
