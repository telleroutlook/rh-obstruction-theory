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

## §4. Observation indistinguishability (the core obstruction, PROOF-DRAFT)

**Proposition G.3.** Fix any `N`. Construct the perturbed multiset:
```
𝒵_ε := {d_n + ε_n : n ≥ 1}   where ε_n = γ_n − d_n (the S(T) discrepancy)
```
Then `𝒵_ε = {γ_n : n ≥ 1} = 𝒵_RH`, but there also exist perturbations `{ε̃_n}` with:
- `|ε̃_n| ≤ |ε_n|` for all n;
- `∑_n ε̃_n ≠ ∑_n ε_n` (so the resulting zero multiset differs from `𝒵_RH`);
- `O_θ(n) = d_n + ε̃_n` up to O_θ's precision — i.e. both `𝒵_RH` and the perturbed
  multiset produce the same observation record under `O_θ`.

**Consequence.** A method `P ∈ 𝔐_FC` that only reads `O_θ` cannot distinguish `𝒵_RH`
from `𝒵_ε` using the archimedean level data alone, so it cannot guarantee that
`det(I − z² K_N) → Ξ` (which requires converging to the product over `𝒵_RH`, not `𝒵_ε`).

*Proof sketch.* The archimedean level sequence `(d_n)` depends only on the smooth part
`θ(T)`, which is determined by the gamma factor of ζ alone (zero-free). The S(T) term
requires evaluating `arg ζ(1/2 + iT)`, which depends on zero locations. Two distinct
zero multisets that produce the same smooth counting function N(T) − S(T) = θ(T)/π + 1
will produce the same `(d_n)` sequence. The existence of such distinct multisets is
assured by the freedom to shift zeros by amounts controlled by S(T).

*Open step.* A fully rigorous proof needs to exhibit a specific `{ε̃_n}` satisfying all
conditions, with the resulting entire function `Ξ_ε(z) = Ξ(0) · e^{az} · ∏_n(1 − z/(d_n + ε̃_n))···`
being distinct from `Ξ` on a compact set. The structure is the same as Theorem E-neg
(non-uniqueness / information obstruction); the two theorems share the Hadamard
uniqueness + IFT construction template. Status: PROOF-DRAFT (analogue of E-neg §3). ☐

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
| O_θ indistinguishability (Prop. G.3) | PROOF-DRAFT (open step: explicit ε̃_n exhibit) |
| CORE-4 obstruction (Theorem G) | PROOF-DRAFT (follows from G.1 + G.2 + G.3) |
| G-hard conjecture | CONJECTURE (not a premise) |
| Non-vacuity | PROOF-DRAFT (kappa_toeplitz; Bochner positivity) |
| No-RH | ✓ (obstruction is independent of truth of RH) |
| Escape route | Explicit (§4; step outside 𝔐_FC via full S(T) data or non-spectral identity) |
