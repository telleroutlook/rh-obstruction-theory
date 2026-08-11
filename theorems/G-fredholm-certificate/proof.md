# Proof — Theorem G (G-fredholm-certificate)

**Status:** PROOF-DRAFT (Prop. G.3* CONFIRMED with corrections by OB-04 external review 2026-08-11; original G.3 REFUTED as written)  
**Analytic / finite separation:** purely analytic (no finite certificates).

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

## §5. The CORE-4 barrier in 𝔐_FC

**Theorem G (information obstruction, PROOF-DRAFT — corrected).**  
For any `P ∈ 𝔐_FC` (assuming the factorization condition (2.7) holds) and any `N`:
1. The operator `K_N` constructed by P has eigenvalues `κ_n ≈ 1/(1/4 + d_n²)`.
2. By Prop. G.3* Item 2, `{d_n} ≠ {γ_n}` as multisets (infinitely many differ).
3. By Prop. G.3* Item 3, `F_d ≠ F_γ` as entire functions (canonical product argument).
4. Closing the gap requires the S(T) data, which is not available in `O_θ`.

*Conclusion.* CORE-4 is `[OBL]` for every `P ∈ 𝔐_FC` operating with observation `O_θ`.
The obstruction is not a finite-N artifact: the counting-function integral (Item 4 of
Prop. G.3*) shows the separation `|F_d(iR) − F_γ(iR)| → ∞` as R → ∞.

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
| O_θ indistinguishability (Item 1) | PROOF-DRAFT (formal/conditional on factorization condition (2.7) from program's 𝔐_FC definition) |
| CORE-4 obstruction (Theorem G) | PROOF-DRAFT (conditional on factorization condition; Items 2–4 unconditional) |
| G-hard conjecture | CONJECTURE (not a premise) |
| Non-vacuity | PROOF-DRAFT (kappa_toeplitz; Bochner positivity) |
| No-RH | ✓ (obstruction is independent of truth of RH) |
| Escape route | Explicit (step outside 𝔐_FC via full S(T) data or non-spectral identity) |
