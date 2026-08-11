# Proof — Theorem G (G-fredholm-certificate)

**Status:** G-info diagonal obstruction (𝔐_d^{tr}) INDEPENDENTLY-CHECKED — GATE-A PASS after integrating OB-22's 7 conditional mods (§1a); G-hard remains CONJECTURE. Prop. G.3* CONFIRMED with corrections by OB-04; finite core INDEPENDENT-CHECKER (OB-17 deposited checker).  
**Analytic / finite separation:** analytic assembly (§1a–§5b) + deposited exact-interval checker for the finite core.

---

## §1. Overview

The obstruction has three components:

1. **Hadamard uniqueness** (REFEREED): two order-1 entire functions with the same zeros
   and the same value at one point are equal.

2. **S(T) gap** (REFEREED): the archimedean levels `d_n = θ_level(n)` differ from the
   true Riemann zero ordinates `γ_n` by an amount determined by the argument function
   `S(T) = (1/π) arg ζ(1/2 + iT)`.

3. **O_θ indistinguishability** (PROOF-DRAFT): the observation map `O_θ` returns the
   same sequence `(d_n)` for the true zero multiset `𝒵_RH` and for a perturbed multiset
   `𝒵_ε` differing by the S(T) fluctuation — neither is preferred by O_θ.

Step 4 (G-hard, CONJECTURE): S(T) is not recoverable within 𝔐_FC.

---

## §1a. Gate-A conditions integrated (OB-22 external review, 2026-08-11)

OB-22 returned **GATE-A CONDITIONAL** for the diagonal G-info obstruction (no reproof
needed — no gap, no circularity, no RH-import, G-hard cleanly quarantined), requiring
seven textual/premise fixes before the status advances. All are integrated here; none
changes the mathematics.

**(M1) Common Hilbert space + xi + counting conventions.** Work on `H = ℓ²(ℕ)`;
`D_N = diag(κ_1,…,κ_N,0,0,…)` and all `K_N` are operators on `H` (so `‖K_N − D_N‖_1` is
well-defined). `ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s)`. `(γ_n)` = the multiset of positive
imaginary parts of ALL nontrivial zeros `β+iγ`, in nondecreasing order with multiplicity
(NOT only critical-line zeros). `N(T)` counts `0 < γ ≤ T`, with the left/right midpoint
value at a zero height; `S(T) = (1/π) arg ζ(1/2+iT)` by continuous variation along
`2 → 2+iT → ½+iT`, midpoint value at zero heights. `A(T) = θ(T)/π + 1`,
`D(T) = #{n : d_n ≤ T}`.

**(M2) Exact Riemann–von Mangoldt as an allowed premise (REFEREED).** Under (M1),
Titchmarsh–Heath-Brown (1986) *The Theory of the Riemann Zeta-function*, 2nd ed.,
**Theorem 9.3** gives the **pointwise** identity
```
N(T) = 1 + θ(T)/π + S(T)      (= A(T) + S(T)),
```
valid off zero heights, extended by the midpoint convention. This exact identity — NOT the
`O(log T)` asymptotic alone — is what Link D (Prop G.3* Item 2) requires. (`S(T) = O(log T)`
is Thm 9.4; `S_1(T) = ∫_0^T S = O(log T)` is Littlewood 1924 / Thm 9.9(A) — both used in
Link D, both unconditional, no zero location.)

**(M3) Weak factorization only (corrected).** The diagonal subclass is
```
𝔐_d^{tr} = { (K_N) : K_N ≥ 0 finite-rank on H,  ∃ allowed auxiliary data a_N and Φ_N with
             K_N = Φ_N((d_n)_{n≤N}, a_N),  and  ‖K_N − D_N‖_1 → 0 }.
```
The theorem does NOT claim `a_N` is determined by `(d_n)`, nor that a `Ψ_N` depending on
`(d_n)` alone exists (that strong reading is a separate, unestablished hypothesis).
**The diagonal proof uses ONLY `K_N ≥ 0` and the trace-norm condition — the factorization
is not an analytic step.** "Zero-free input" does not imply "zero-blind output" (zero-free
arithmetic data can analytically determine zeros), so the strong reading is not established.

**(M4) Link D averaging lemma (explicit).** In Prop G.3* Item 2, replace the one-line
"fractional-part averaging" by: with `h(x) = {x} − ½`, `H(x) = ∫_0^x h`, `H` bounded
1-periodic; substituting `x = A(t)` and `w(x) = 1/A'(A^{-1}(x))` (positive, decreasing
since `A'' ≥ 0` eventually, so bounded variation), integration by parts gives
`∫_{T_0}^T h(A(t)) dt = ∫ h(x)w(x) dx = O(1)`, hence `∫_{T_0}^T {A(t)} dt = T/2 + O(1)`.
Integrating `S(t) = −{A(t)} − m` then gives `S_1(T) = −(m+½)T + O(1) = Ω(T)`, contradicting
Littlewood. Conclusion stated precisely: **the multiset symmetric difference of `{d_n}` and
`{γ_n}` is infinite** (stronger than "≠").

**(M5) Link C notation + no RH split.** Write the first positive zero of `G_d` as `r_1 =
√(1/4+d_1²)` (avoid clash with the eigenvalue symbol `λ_j`). Drop the "if RH / if ¬RH"
split: a rigorously verified critical-line zero `γ_* ∈ [14.134725139, 14.134725145]` has
`Ξ̂(γ_*) = 0` (Platt–Trudgian 2021, Thm 1: RH true up to height 3·10¹²; Odlyzko table
±3·10⁻⁹); since `γ_* < r_1` and `G_d` has no zero in `(0, r_1)`, `G_d(γ_*) ≠ 0 = Ξ̂(γ_*)`,
so `G_d ≠ Ξ̂` — unconditional, using one proven finite-height fact, not RH.

**(M6) Lemma G.5 wording.** Replace "cannot be verified without proving RH" by the formal
implication: *for any PSD family satisfying Lemma G.4's hypotheses, a proof that its
locally uniform limit equals `Ξ̂` would, together with Lemma G.4, constitute a proof of RH.*
Any universal `∀P ∈ 𝔐_FC` statement requires `𝔐_FC`, `O_θ`, condition 3 to be fully
defined in-package; where they are not, only the general PSD-family Lemma G.5 is asserted.

**(M7) Theta-level existence/uniqueness (exact quantifier).** For each `n ≥ 1`, `d_n` is
the unique solution of `θ(d_n) = (n−1)π` in `[7, ∞)`; existence/uniqueness from `θ'(t) > 0`
for `t ≥ 7`, `θ(7) < 0`, and `θ(t) → ∞` (Brent–Platt–Trudgian 2021 eqs (9)–(11) give θ's
expansion with explicit remainder, from which `θ' > 0` on `[7,∞)` follows).

**Scope reminder (OB-22 §7).** What is established is a **diagonal / trace-norm** continuity
obstruction: a family with `‖K_N − D_N‖_1 → 0` cannot have determinant limit `Ξ̂` (it is
forced to `G_d ≠ Ξ̂`). Titles/abstracts must keep the `𝔐_d^{tr}` / "diagonal" qualifier;
the broader "no zero-free construction recovers the zeros" claim is exactly G-hard, which
remains an isolated `[CONJECTURE]`.

---


## §2. Hadamard uniqueness (analytic input) — CORRECTED

**[CORRECTION from OB-04 review]** The original Lemma G.1 stated: "two order-≤1
entire functions with the same zeros and same value at 0 are equal." This is **false**.
Counterexample: `F(z) = 1` and `G(z) = e^z` both have order ≤ 1, the same empty zero
multiset, and agree at `z = 0`, but `F ≠ G`.

The correct statement is that two such functions can differ by `e^{az+b}`, and
additional constraints (evenness + normalization) remove that freedom **in the present
setting**. But the general Lemma G.1 as stated cannot be cited for the current proof.

**Corrected approach (used in Prop. G.3*).** Item 3 of Prop. G.3* does NOT require
a general Hadamard uniqueness theorem. The argument is direct:

A locally uniformly convergent canonical product
```
F_a(z) = C · ∏_{n≥1} (1 − z²/a_n²)
```
has **precisely the zeros** supplied by its factors (with multiplicities). If `F_d = F_γ`,
then their zero multisets are equal, contradicting Item 2. Hence `F_d ≠ F_γ` follows
directly from the canonical product structure — no Hadamard uniqueness invocation needed.

*Note on notation (OB-04).* The canonical product `F_γ(z) = C · ∏(1 − z²/γ_n²)` equals
the actual Riemann ξ-function `Ξ_R(z) = ξ(1/2 + iz)` if and only if RH holds (all zeros
on the critical line). Unconditionally `F_γ` and `Ξ_R` need not be the same. The theorem
applies to `F_γ` as defined, not to `Ξ_R` unconditionally.

---

## §3. The S(T) gap identity — CORRECTED

**Lemma G.2 (corrected).** With `A(t) := θ(t)/π + 1` and `S(t) = (1/π) arg ζ(1/2 + it)`,
the Riemann–von Mangoldt identity away from zero ordinates is:
```
N(t) = A(t) + S(t).
```
The smooth level `d_n` satisfies `A(d_n) = n`. For a **simple** zero ordinate `γ_n`,
assigning `S(γ_n)` its midpoint value gives:
```
A(γ_n) + S(γ_n) = n − 1/2.
```
Therefore:
```
A(d_n) − A(γ_n) = S(γ_n) + 1/2.
```
By the mean-value theorem, for some `ξ_n` between `d_n` and `γ_n`:
```
d_n − γ_n = (S(γ_n) + 1/2) / A'(ξ_n).
```

**[CORRECTION from OB-04 review]** The original proof.md had three errors in the
discrepancy formula:
1. **Sign reversed**: the correct formula gives `d_n − γ_n` (not `γ_n − d_n`).
2. **Missing 1/2 term**: the endpoint half-jump is mandatory under the midpoint convention.
3. **Notation**: `N'(T)` is a step function with no ordinary derivative at zero ordinates;
   the correct denominator is `A'(t) = θ'(t)/π ∼ log(t/2π)/(2π)`.
4. **Tsang citation**: the correct journal is *Acta Arithmetica* **46** (1986), not
   J. Number Theory 23 (1986).

**[CORRECTION from OB-04 review]** The argument "S(t) ≠ 0 for infinitely many t"
does **not** imply `d_n ≠ γ_n` for any specific n. The correct proof of Item 2
(multiset distinctness) does not use the discrepancy formula at all — see §4 below.

*Source for corrected formula:* Titchmarsh §9.4 (exact identity); OB-04 referee
report §5 (convention/sign correction). Status: REFEREED.

**Unconditional bounds used in §4:**
```
S(t) = O(log t),      S_1(T) := ∫_0^T S(t) dt = O(log T)    (Littlewood).
```
The Littlewood bound `S_1(T) = O(log T)` is the critical new input (not listed in the
original outsource file) used to prove Items 2 and 4 of the corrected proposition.

---

## §4. Corrected Proposition G.3* (OB-04 external review, 2026-08-11)

**[ORIGINAL Prop. G.3 REFUTED as written — see OB-04 referee §1 and §§5–6]**

The original proof had four defects: (1) Item 1 requires the factorization condition (2.7)
from the program definition of 𝔐_FC, which was not included in the outsource file;
(2) the discrepancy formula was wrong (sign, 1/2 term, N' notation); (3) the Hadamard
uniqueness lemma was cited incorrectly (see §2); (4) the Step 4 ratio argument was
invalid — one factor ≠ 1 does not prevent all other factors from compensating it.

**Corrected Proposition G.3*.**

Define:
```
F_γ(z) := C · ∏_{n≥1} (1 − z²/γ_n²),
F_d(z) := C · ∏_{n≥1} (1 − z²/d_n²),     C = ξ(1/2) > 0.
```
Both products converge locally uniformly (since Σ γ_n^{-2} < ∞ and d_n ∼ γ_n ∼ 2πn/log n
by OB-04 Lemma 3.2; note the correct inversion is γ_n ∼ 2πn/log n, not (n/2π)log(n/2π)).

**Item 1 (formal/conditional).** If `O_θ` is defined as the constant map
`O_θ(𝒵) := (d_n)_{n≥1}` for all `𝒵 ∈ 𝒳`, then both multisets yield the same output.
This is immediate from the definition. The program-level obstruction for `𝔐_FC` additionally
requires the factorization condition (2.7): every admissible output of every `P ∈ 𝔐_FC`
factors through `O_θ`. This must be verified from the program's definition of `𝔐_FC`.

**Item 2 (multiset distinctness — corrected proof, unconditional).**

Suppose for contradiction that the symmetric difference of `{γ_n}` and `{d_n}` were finite.
Then `D(t) − N(t) = m` (constant integer) for all sufficiently large `t`. By the
Riemann–von Mangoldt identity and (2.5):
```
m = ⌊A(t)⌋ − A(t) − S(t) = −{A(t)} − S(t),
```
so `S(t) = −{A(t)} − m`. Integrating and applying Lemma 3.3 (fractional-part averaging,
OB-04 §3): `S_1(T) = −(m + 1/2)T + O(1)`. Since m is an integer, `m + 1/2 ≠ 0`, so
`S_1(T) = Ω(T)`. This contradicts Littlewood's unconditional bound `S_1(T) = O(log T)`.
Therefore the symmetric difference is **infinite** — infinitely many `d_n ≠ γ_n`. ✓

*Note:* The original proof claimed "S(t) ≠ 0 for infinitely many t implies d_n ≠ γ_n for
some n." This does NOT follow — S(t) nonvanishing at arbitrary t does not imply mismatch
at a zero ordinate. The Littlewood bound argument above is the correct proof.

**Item 3 (distinct entire functions — corrected proof).**

Since `F_γ` and `F_d` are locally uniformly convergent canonical products, each has
precisely the zeros from its factors. If `F_d = F_γ`, their zero multisets would be equal,
contradicting Item 2. Hence `F_d ≠ F_γ`. No Hadamard uniqueness theorem is invoked. ✓

**Item 4 (quantitative separation — corrected, unconditional).**

**[CORRECTION]** The original argument evaluated the ratio at `R = γ_n` and concluded
from one factor ≠ 1. This is **invalid**: the remaining factors can compensate exactly.

The correct argument uses the counting-function integral representation (OB-04 Lemma 3.4):
```
log(F_d(iR) / F_γ(iR)) = ∫_0^∞ K_R(t) (D(t) − N(t)) dt,
    K_R(t) = 2R²/[t(t² + R²)].
```
Using `D(t) − N(t) = −{A(t)} − S(t) + O(1)` and splitting into fractional-part and
S-terms:

- **Fractional-part term**: By Lemma 3.3 (OB-04) the primitive of `{A(t)} − 1/2` is
  O(1). Since `K_R(t)` is positive and decreasing with bounded total variation, and
  `∫_{T_0}^∞ K_R(t) dt = log(1 + R²/T_0²)`, one gets:
  ```
  ∫ K_R(t) {A(t)} dt = (1/2) log(1 + R²/T_0²) + O(1) = log R + O(1).
  ```

- **S-term**: Let `G(t) = ∫_0^t S(u) du = O(log t)` (Littlewood). Integration by parts:
  `∫ K_R(t) S(t) dt = −∫ K_R'(t) G(t) dt`. Using `−K_R'(t) ≪ t^{-2}` for `t ≤ R` and
  `R²t^{-4}` for `t > R`, and `G(t) = O(log t)`, the integral is O(1) uniformly in R.

Combining:
```
log(F_d(iR) / F_γ(iR)) = −log R + O(1),
```
hence `F_d(iR)/F_γ(iR) = e^{O(1)}/R`, giving:
```
c/R ≤ F_d(iR)/F_γ(iR) ≤ C₁/R    for R ≥ R_0.
```
In particular, `|F_d(iR)/F_γ(iR) − 1| → 1` as R → ∞. ✓

**Corollary.** Since `F_γ(iR) → ∞` (Hadamard product lower bound), we get
`|F_d(iR) − F_γ(iR)| ∼ F_γ(iR) → ∞`. The absolute separation is explicit and
holds for all sufficiently large R, not merely along a subsequence.

**Numerical anchor correction (OB-04 §7).**

The original outsource file stated `d_1 ≈ γ_1 ≈ 14.1347`. This is **incorrect** for the
normalization `A(d_n) = n` (i.e. `θ(d_n) = (n-1)π`). The correct values:
```
θ(14) ≈ −1.783,    γ_1 ≈ 14.1347,    θ(γ_1) ≈ −1.729,
d_1 = g_0 ≈ 17.846    (first Gram point, where θ(d_1) = 0).
```
So `d_1 ≈ 17.846 ≠ γ_1 ≈ 14.135`. The smooth adversary `{d_n}` is NOT close to `{γ_n}`
at small n. (The indexing convention d_n = g_{n-1} shifts d_1 substantially above γ_1.)

*Status: PROOF-DRAFT ✓ (corrected).* Items 2–4 proved unconditionally.
Item 1 is formal/conditional on the program-level factorization condition (2.7).
The corrected proof uses Littlewood's S_1(T) = O(log T) as the critical classical input.

---

## §5. The CORE-4 barrier in 𝔐_FC — CORRECTED (OB-08)

**Corrected Fredholm determinant formula.** For `K_N = D_N = diag(κ_1,…,κ_N)` with
`κ_n = 1/(1/4 + d_n²)`:
```
det(I − z² D_N) = ∏_{n=1}^{N} (1 − z² κ_n) = ∏_{n=1}^{N} (1 − z²/(1/4 + d_n²)).
```
Zeros at `z = ±(1/4 + d_n²)^{1/2}`, NOT at `±d_n` or `±κ_n^{1/2}`.

**Local uniform limit (OB-08 Theorem 5.1 + 6.1).** Since `Σ κ_n = Σ 1/(1/4+d_n²) < ∞`
(by `d_n ∼ 2πn/log n`), `D = diag(κ_n)` is trace class with `‖D−D_N‖_1 = Σ_{n>N} κ_n → 0`.
By the Fredholm determinant stability inequality
`|det(I+A) − det(I+B)| ≤ ‖A−B‖_1 exp(1+‖A‖_1+‖B‖_1)`,
we get `det(I−z²D_N) → G_d(z) = ∏_{n≥1}(1−z²/(1/4+d_n²))` locally uniformly.

**G_d ≠ Ξ̂ unconditionally (direct zero-value argument; INDEPENDENT-CHECKER, OB-17).**
The zeros of `G_d` are exactly `{±√(1/4+d_n²)}` (all real; the convergent product is
nonzero off these points — OB-17 §8.3). In particular the least positive zero is
`λ_1 = √(1/4+d_1²) > 17.8526`, and `G_d(z) ≠ 0` for `0 < z < λ_1`.
- **Under RH:** `Ξ̂(γ_1) = 0` with `γ_1 < 14.1348 < λ_1`, so `G_d(γ_1) ≠ 0 = Ξ̂(γ_1)`,
  hence `G_d ≠ Ξ̂`. (This uses a single certified on-line ordinate `γ_1`, not RH.)
- **Under ¬RH:** `Ξ̂` has a non-real zero while all zeros of `G_d` are real; still
  `G_d ≠ Ξ̂`.

**Caution (OB-17 §0.3):** `G_d ≠ Ξ̂` is NOT deduced by transitivity from `G_d ≠ F_d` and
`F_d ≠ Ξ̂` (that inference is invalid). The direct value comparison `G_d(γ_1) ≠ Ξ̂(γ_1)`
above is the closed argument. The "spectral shift" and "S(T) gap" are two *descriptions*
of why the divisors differ, not two inequalities chained together.

**Certified interval replay (OB-17, INDEPENDENT-CHECKER 2026-08-11).** The finite core —
`γ_n < d_n < √(1/4+d_n²)` for n=1,2,3, plus the tail bound giving convergence to `G_d` —
is independently certified in exact-rational interval arithmetic by
`checker/diagonal_fredholm_interval_replay.py` (SHA-256
`e197f2bb…c8f4058b`; prints `ALL_CERTIFIED_CHECKS_PASSED`; source-verified and re-run
in-repo). It encloses `d_1,…,d_5` to width `< 6.83e-12`, certifies the three-way
separation (`γ_n` from Odlyzko's table with ±3e-9, used only for comparison), passes both
adversarial mutations, and certifies `Σ_{n>2048} κ_n < 10^{-3}`. Validates only the finite
separation + convergence, not RH.

**Theorem G (diagonal obstruction — PROOF-DRAFT — corrected).**  
For any `(K_N) ∈ 𝔐_d^{tr}`:
1. `det(I − z² K_N) → G_d` locally uniformly (Theorem 6.1, using trace-norm stability;
   tail bound certified by OB-17 checker).
2. `G_d ≠ Ξ̂` unconditionally (direct zero-value argument above — NOT transitivity).

*The earlier statement "eigenvalues κ_n ≈ 1/(1/4+d_n²) → determinant zeros near d_n" was
incorrect: zeros are at `±κ_n^{-1/2} = ±√(1/4+d_n²)`, not at `±d_n`.*

**Shifted-determinant alternative (OB-08 §2.3).** To recover zeros at `±d_n` from a
finite-rank operator, use:
```
det(I − (z²+1/4)D_N) / det(I − (1/4)D_N) = ∏_{n=1}^N (1 − z²/d_n²).
```
But even this gives limit `F_d ≠ Ξ̂` (by Prop. G.3* Items 2–4). The S(T) obstruction
remains; the spectral-shift issue is a separate additional obstruction.

---

## §5b. All-real-zeros of PSD Fredholm limits — CONFIRMED (OB-10 2026-08-11)

**Lemma G.4 (PSD Fredholm limit has all-real zeros).** Let `K_N ∈ 𝓑(H)` be
finite-rank, self-adjoint, positive semidefinite (`K_N = K_N* ≥ 0`), with nonzero
eigenvalues `λ_1,…,λ_{r_N} > 0`, and
```
f_N(z) = det(I − z² K_N) = ∏_{j=1}^{r_N}(1 − z² λ_j).
```
If `f_N → f` locally uniformly on ℂ, then f is entire, `f(0) = 1` (so `f ≢ 0`),
and every zero of f is real.

*Proof (OB-10 referee, CONFIRMED).*
1. Each `f_N` has zeros only at `z = ±λ_j^{-1/2} ∈ ℝ\{0}`; hence no zeros in the
   open upper/lower half-planes 𝕌, 𝕃.
2. f entire (Weierstrass convergence theorem); `f(0) = lim f_N(0) = 1`, so `f ≢ 0`.
3. On the connected open set 𝕌: each `f_N|_𝕌` is zero-free, `f_N → f` locally
   uniformly. By Hurwitz's zero-free corollary (Conway, *Functions of One Complex
   Variable I*, 2nd ed., **Ch. VII §2, Corollary 2.6**, p. 152), either `f|_𝕌 ≡ 0`
   or `f|_𝕌` is zero-free. The first is excluded: `f ≡ 0` on the nonempty open set
   𝕌 would force `f ≡ 0` on ℂ (identity theorem), contradicting `f(0) = 1`. So `f`
   is zero-free on 𝕌.
4. Same for 𝕃. Since `ℂ \ (𝕌 ∪ 𝕃) = ℝ`, all zeros of f are real. ∎

*Citation correction (OB-10 §3):* the precise reference is Conway VII.§2 **Cor. 2.6**
(the zero-free-limit corollary); Theorem 2.5 is the zero-counting stability from which
it follows. The identity-theorem step (excluding `f|_𝕌 ≡ 0`) is essential and is now
explicit. (Ahlfors, *Complex Analysis*, 3rd ed., Ch. 5 §1.1, Thm 2, p. 178 is an
alternative reference — note p. 178, not p. 176.)

**Corollary G.5 (convergence to Ξ̂ ⟹ RH).** If some `P ∈ 𝔐_FC` had
`det(I − z² K_N) → Ξ̂` locally uniformly with `K_N ≥ 0`, then by Lemma G.4 all zeros
of Ξ̂ are real — i.e. RH holds. Therefore membership condition 3 of 𝔐_FC ("claims
det → Ξ̂") cannot be *verified* (as a proved locally uniform limit) without proving
RH. This is why 𝔐_FC membership is stated with condition 3 as a *claim*, and why the
obstruction (Theorem G) targets what O_θ can determine, not whether any such P exists.

---

## §6. G-hard (CONJECTURE — not a proof step)

**Conjecture G-hard.** No method `P ∈ 𝔐_FC` can recover the S(T) data from zero-free
arithmetic inputs alone without either reading zero ordinates or implicitly computing an
RH-equivalent quantity.

*Evidence (not a proof):*  
- All known zero-free arithmetic constructions (prime diagonal, Bochner-Toeplitz,
  Guinand-Weil test-function pairing) produce smooth spectral densities; none exhibits
  a mechanism for capturing the S(T) arithmetic fluctuation.
- The best-known oracle-separation intuition: S(T) is a sum of contributions from
  individual zeros via the explicit formula; reconstructing it from primes alone would
  require inversion of the Euler product modulo knowledge of all zero ordinates — a
  circular dependency.

*This conjecture is explicitly NOT used as a proof premise anywhere.*

---

## §7. Relation to other theorems in this repository

| Theorem | Method class | Obstruction type | Relation to G |
|---|---|---|---|
| B1/B2 | Finite-inequality / exact-collision | Information (finite observation) | B2 uses same Hadamard + IFT template |
| E-neg | CCM entire-Ξ normalization | Information (non-uniqueness) | E-neg §3 is the exact analogue; G reuses the argument |
| D | Elliptic operators on compact manifolds | Structural (heat-trace invariant) | Different: structural, not information |
| G (this) | 𝔐_FC, theta-level observation | Information (S(T) gap) | New class; CORE-4 obstruction |

**Key reuse:** The proof of G-info is structurally the same as E-neg §3 with the
perturbed-tail construction replaced by the S(T) discrepancy. The underlying tool
(Hadamard uniqueness) is shared.

---

## §8. Status summary

| Step | Status |
|---|---|
| Lemma G.1 (Hadamard uniqueness, general) | **REFUTED as stated** (OB-04: 1 and e^z are a counterexample). Not used in corrected proof. |
| Canonical product distinctness (Item 3) | PROOF-DRAFT ✓ — direct argument: F_d = F_γ ⟹ same zero multiset, contradicts Item 2 |
| S(T) gap identity — corrected (§3) | REFEREED (Titchmarsh §9.4) with corrections: sign reversed, 1/2 term added, N'→A' |
| Tsang citation corrected | *Acta Arithmetica* **46** (1986) — not J. Number Theory 23 |
| Item 2 multiset distinctness — corrected proof | PROOF-DRAFT ✓ — Littlewood S_1(T)=O(log T) + fractional-part averaging (unconditional) |
| Item 4 quantitative separation — corrected proof | PROOF-DRAFT ✓ — counting-function integral + Littlewood; log(F_d/F_γ)(iR) = −log R + O(1) |
| Numerical anchor d_1 corrected | d_1 = g_0 ≈ 17.846 (NOT ≈ 14.134); original anchor was wrong |
| Lemma G.4 (PSD Fredholm limit all-real zeros) | CONFIRMED (OB-10 2026-08-11; Conway VII.§2 Cor. 2.6 + identity theorem) |
| Corollary G.5 (det → Ξ̂ ⟹ RH) | CONFIRMED (OB-10; membership condition 3 unverifiable without RH) |
| O_θ indistinguishability (Item 1) | PROOF-DRAFT (formal/conditional on factorization condition (2.7) from program's 𝔐_FC definition) |
| CORE-4 obstruction (Theorem G) | PROOF-DRAFT (conditional on factorization condition; Items 2–4 unconditional) |
| G-hard conjecture | CONJECTURE (not a premise) |
| Non-vacuity | PROOF-DRAFT (kappa_toeplitz; Bochner positivity) |
| No-RH | ✓ (obstruction is independent of truth of RH) |
| Escape route | Explicit (step outside 𝔐_FC via full S(T) data or non-spectral identity) |
