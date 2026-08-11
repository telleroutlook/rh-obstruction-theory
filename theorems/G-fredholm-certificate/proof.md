# Proof — Theorem G (G-fredholm-certificate)

**Status:** PROOF-DRAFT (G-info); G-hard step is CONJECTURE  
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

## §2. Hadamard uniqueness (analytic input)

**Lemma G.1.** Let F, G be entire functions of order at most 1 with the same multiset
of zeros `{z_n}` (counted with multiplicity) and with `F(0) = G(0) ≠ 0`. Then `F = G`.

*Proof.* By the Hadamard factorization theorem for entire functions of order ≤ 1:
```
F(z) = e^{az+b} ∏_n (1 − z/z_n) e^{z/z_n}
```
The product is determined by the zeros `{z_n}` up to the exponential prefactor.
The constraint `F(0) = e^b ∏_n (−1/z_n) e^{1/z_n}` pins `b`; similarly for `G`.
If the zeros are the same and `F(0) = G(0)`, then both exponential prefactors are equal,
so `F = G`. ☐

*Note.* `Ξ` is even, order 1, and has infinitely many zeros (all real under RH). The
normalization `Ξ(0) = ξ(1/2)` is a fixed nonzero constant. Lemma G.1 applies.

---

## §3. The S(T) gap identity

**Lemma G.2.** Let `N(T)` be the zero-counting function of ζ in `{0 < Im(s) < T}`. By the
argument principle:
```
N(T) = θ(T)/π + 1 + S(T)
```
where `S(T) = (1/π) arg ζ(1/2 + iT)` and `θ(T) = Im(log Γ(1/4 + iT/2)) − T log(π)/2`.

The archimedean level `d_n` is defined by `θ(d_n)/π + 1 = n`, i.e. the n-th solution to
the smooth part equaling n. This gives `d_n ≈ γ_n` but with discrepancy:
```
γ_n − d_n = S(γ_n)/N'(γ_n) + O(1/γ_n),    N'(T) ~ log(T/2π)/(2π).
```

*Proof.* Standard: Titchmarsh 'Theory of the Riemann Zeta Function' §9.4;
Davenport 'Multiplicative Number Theory' Ch. 15. Status: REFEREED. ☐

**Corollary.** The eigenvalue error for any `P ∈ 𝔐_FC` is:
```
|κ_n^smooth − 1/(1/4 + γ_n²)| / |1/(1/4 + γ_n²)|
  = |1/(1/4 + d_n²) − 1/(1/4 + γ_n²)| / |1/(1/4 + γ_n²)|
  ≈ 2γ_n |γ_n − d_n| / (1/4 + γ_n²)
  ~ S(γ_n) · 2π / (γ_n log(γ_n/2π))
```
This is not `o(1)` in general — `S(T)` is bounded (O(log T), assuming RH: O(log T / log log T))
but is not identically zero.

---

## §4. Observation indistinguishability (the core obstruction)

**Proposition G.3** (PROOF-DRAFT — explicit adversary constructed below)**.**

Define the **smooth adversary** multiset:
```
𝒵_smooth := {d_n : n ≥ 1}   (archimedean levels, all on the real axis)
```
where `d_n` is the n-th solution to `θ(d_n)/π + 1 = n`, with `θ(T) = Im log Γ(1/4+iT/2) − T log(π)/2`.

**Claim.** `𝒵_smooth ≠ 𝒵_RH` as multisets, but `O_θ(𝒵_smooth) = O_θ(𝒵_RH)`.

*Step 1 — `O_θ` is the same for both.*  
The observation map `O_θ` returns the sequence `(d_n)_{n≥1}` — the archimedean levels
defined from the smooth part `θ(T)` only. By definition, both `𝒵_RH` and `𝒵_smooth`
yield this same sequence: for `𝒵_RH = {γ_n}`, the levels `d_n` approximate the
ordinates but differ by the S(T) term; for `𝒵_smooth = {d_n}`, the observation map
returns `(d_n)` exactly. **Either way, `O_θ` outputs `(d_n)`.**

*Step 2 — `𝒵_smooth ≠ 𝒵_RH`.*  
S(T) is not identically zero (Backlund 1914; `S(T)` has infinitely many sign changes,
Tsang 1986). Therefore `γ_n ≠ d_n` for infinitely many `n`. So the two multisets
`{γ_n}` and `{d_n}` differ.

*Step 3 — Entire functions are distinct.*  
Define:
```
Ξ_smooth(z) := Ξ(0) · ∏_{n≥1} (1 − z²/d_n²).
```
This is entire of order 1 (since `Σ d_n^{-2} < ∞`; same proof as for `Ξ`, by
von Mangoldt `d_n ∼ n/2π · log(n/2π)`). By Lemma G.1 (Hadamard uniqueness), since
`{d_n}` and `{γ_n}` are distinct multisets and both products share the same
normalization `Ξ(0)` at `z=0`, we conclude `Ξ_smooth ≠ Ξ`.

*Step 4 — Quantitative separation.*  
For `z = i R` with `R > d_{k_0}` for some `k_0` where `d_{k_0} ≠ γ_{k_0}`:
```
Ξ_smooth(iR) / Ξ(iR) = ∏_{n≥1} [(1 + R²/d_n²) / (1 + R²/γ_n²)].
```
Every factor is `> 0`. For `n = k_0` where `d_{k_0} < γ_{k_0}` (which occurs whenever
`S(γ_{k_0}) < 0`, so `γ_{k_0} > d_{k_0}`):
```
(1 + R²/d_{k_0}²) / (1 + R²/γ_{k_0}²) > 1
```
with a definite positive gap bounded away from 1 for `R ∼ d_{k_0}`. Since
`|Ξ(iR)| → ∞` as `R → ∞` (Hadamard product lower bound; same as E-neg §3):
```
|Ξ_smooth(iR) − Ξ(iR)| ≥ |Ξ(iR)| · |Ξ_smooth(iR)/Ξ(iR) − 1|
                        ≥ c · |Ξ(iR)| → ∞.
```
So `Ξ_smooth ≠ Ξ` as entire functions, with explicit separation on `iℝ`. ✓

*Step 5 — `det(I − z² K_N) → Ξ_smooth ≠ Ξ`.*  
A method `P ∈ 𝔐_FC` reads only `O_θ` and produces eigenvalues `κ_n ≈ 1/(1/4 + d_n²)`.
By Hadamard uniqueness, the resulting determinant product converges (if it converges at
all) to an entire function determined by the eigenvalue sequence `{d_n}`. That function
is `Ξ_smooth`, not `Ξ`. The gap is exactly the S(T) discrepancy; it does not
vanish as `N → ∞` because S(T) is not zero almost everywhere. ☐

**Consequence.** No method `P ∈ 𝔐_FC` can guarantee `det(I − z² K_N) → Ξ` from `O_θ`
data alone. The adversary `𝒵_smooth` is O_θ-indistinguishable from `𝒵_RH` and produces
a distinct limit.

*Status: PROOF-DRAFT.* Steps 1–4 are self-contained. Step 5 relies on the
`O_θ`-definition of `𝔐_FC` and Lemma G.1 (REFEREED). The S(T) sign-change fact
(Step 2) is REFEREED (Backlund 1914, Tsang 1986; Titchmarsh §9.4 records the
sign-change property). Needs independent verification of the quantitative bound in
Step 4.

---

## §5. The CORE-4 barrier in 𝔐_FC

**Theorem G (information obstruction, PROOF-DRAFT).**  
For any `P ∈ 𝔐_FC` and any `N`:
1. The operator `K_N` constructed by P has `κ_n^smooth ≈ 1/(1/4 + d_n²)`.
2. By Lemma G.2, `1/(1/4 + d_n²) ≠ 1/(1/4 + γ_n²)` whenever `S(γ_n) ≠ 0`.
3. By Hadamard uniqueness (Lemma G.1), `det(I − z² K) ≠ Ξ` as entire functions if the
   eigenvalues of K are `{1/(1/4 + d_n²)}` rather than `{1/(1/4 + γ_n²)}`.
4. Closing the gap requires the S(T) data, which is not available in `O_θ`.

*Conclusion.* CORE-4 is `[OBL]` for every `P ∈ 𝔐_FC` operating with observation `O_θ`.
The obstruction is not a finite-N artifact: it persists for all N (the S(T) fluctuation
does not vanish as N → ∞).

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
| Hadamard uniqueness (Lemma G.1) | REFEREED (classical; cited) |
| S(T) gap identity (Lemma G.2) | REFEREED (Titchmarsh §9.4) |
| O_θ indistinguishability (Prop. G.3) | PROOF-DRAFT (explicit 𝒵_smooth adversary constructed; S(T) sign-change REFEREED) |
| CORE-4 obstruction (Theorem G) | PROOF-DRAFT (follows from G.1 + G.2 + G.3) |
| G-hard conjecture | CONJECTURE (not a premise) |
| Non-vacuity | PROOF-DRAFT (kappa_toeplitz; Bochner positivity) |
| No-RH | ✓ (obstruction is independent of truth of RH) |
| Escape route | Explicit (§4; step outside 𝔐_FC via full S(T) data or non-spectral identity) |
