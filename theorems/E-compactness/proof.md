# Proof — Theorem E (finite evidence ⇏ compact convergence; sufficient package)

**Status:** PROOF-DRAFT  
**Analytic / finite separation:** purely analytic; no finite certificate used.

---

## Overview

Two separate proofs:
- **E-neg (§1–§3):** construct a sequence `(F_N)` satisfying `ℰ_N` but failing
  locally uniform convergence.  The key is a Hadamard tail perturbation.
- **E-pos (§4):** given the extra package (H-norm, H-bound, H-tail, H-modulus),
  prove locally uniform convergence via Montel/Vitali + Hurwitz.

---

## §1. Notation

`Ξ(z) = ξ(1/2 + iz)` is the Riemann xi function shifted to the real line; its
zeros are `±γ_n` (`γ_n > 0`, `γ_1 ≈ 14.134…`), all real (assuming RH for
motivation; the theorem holds regardless — it constructs a sequence failing
convergence independent of whether RH is true).

Write the Hadamard factorization:
```
Ξ(z) = Ξ(0) · Π_{n≥1} (1 − z²/γ_n²),
```
where `Ξ(0) = ξ(1/2) > 0` (known: `ξ(1/2) = 1/2 · (−1/2) · π^{-1/4} · Γ(1/4) · ζ(1/2)`
up to the standard normalization; the exact value is a positive real number).
The product converges since `Σ_n γ_n^{-2} < ∞` (Hadamard genus 1).

---

## §2. Construction of the counterexample sequence (E-neg)

**Choose parameters.**  Fix `c > 0` (say `c = 1`).  For each `N ≥ 1`:

- `k_N = N` (use first `N` zeta zeros in place; `k_N → ∞`).
- For `n > N`, define the modified zero:
  `μ_{n,N} := γ_n + c / n   ∈ ℝ,  μ_{n,N} > 0`.
- Define
  ```
  G_N(z) := Π_{n=1}^{N} (1 − z²/γ_n²) · Π_{n=N+1}^{∞} (1 − z²/μ_{n,N}²).
  ```
- Set `F_N(z) := Ξ(0) · G_N(z) / G_N(0)`.

**Convergence of the tail product.**  We need `G_N` to be an entire function of
order 1.  The modified zeros satisfy:
```
Σ_{n>N} μ_{n,N}^{-2} ≤ Σ_{n>N} (γ_n − c/n)^{-2}
```
which converges since `γ_n ∼ (n / 2π) log(n / 2π)` (Riemann–von Mangoldt),
so `γ_n → ∞` and `c/n = o(γ_n)`.  For large `n`, `μ_{n,N} > γ_n/2 > 0`.
The modified tail product converges absolutely, and `G_N` is entire of order 1.

**Finite evidence record verification.**

- (1) Entire order 1: Yes (Hadamard product with `Σ μ_{n,N}^{-2} < ∞`).
- (2) Even: Yes (`G_N(−z) = G_N(z)` since all zeros come in pairs `±μ_{n,N}`).
- (3) Real on `ℝ`: Yes (all zeros and `Ξ(0)` are real).
- (4) Real-rootedness: Yes (zeros are `±γ_n` for `n ≤ N` and `±μ_{n,N}` for `n > N`,
  all real by construction).
- (5) First `N` zeros agree with `γ_1, …, γ_N`: Yes by construction.
- (6) Normalization `F_N(0) = Ξ(0)`: Yes by the definition `F_N(0) = Ξ(0) · G_N(0)/G_N(0) = Ξ(0)`.
- (7) Taylor coefficients: The coefficients `F_N^{(2j)}(0)` involve `Σ_n μ_{n,N}^{-2j}`
  for `j ≥ 1`.  For `j = 0` (normalization), (6) holds.  For `j ≥ 1`, the
  coefficients differ from `Ξ^{(2j)}(0)` by the tail sum
  `Σ_{n>N} (μ_{n,N}^{-2j} − γ_n^{-2j})`, which is nonzero for finite `N`.
  
  **Refinement for condition (7):** To enforce agreement of the first `J_N`
  Taylor coefficients, we can add `J_N` additional free on-line parameters
  (e.g., multiply by a degree-`2J_N` polynomial factor near 0 or adjust `B_N`).
  For the purpose of the basic counterexample (E-neg without condition 7), we
  proceed without enforcing (7) — this is a weaker version of the record.
  
  **For the full E-neg with (7):** adjust the normalization constant `B_N` in
  a factor `e^{B_N z²}` to match the first `J_N` even-power Taylor coefficients.
  This introduces `J_N` free parameters, absorbed into `B_N, B_{2,N}, …`.
  The construction still works since condition (7) is finitely many constraints
  and the modification is a finite-order perturbation preserving (1–6).

**Non-convergence.**  We claim `F_N ↛ Ξ` locally uniformly.

Consider the logarithmic derivative ratio:
```
log F_N(z) − log Ξ(z)
  = Σ_{n=1}^{N} [log(1−z²/γ_n²) − log(1−z²/γ_n²)]  (first N terms cancel)
  + Σ_{n>N} [log(1−z²/μ_{n,N}²) − log(1−z²/γ_n²)]
  + (normalization constant from G_N(0)).
```
The first `N` terms cancel identically.  The tail contribution is:
```
Δ_N(z) := Σ_{n>N} log[(1−z²/μ_{n,N}²)/(1−z²/γ_n²)].
```
For `|z| ≤ R` with `R < γ_{N+1}`, the factors are close to 1 and we can write:
```
log[(1−z²/μ_{n,N}²)/(1−z²/γ_n²)] ≈ z²(γ_n^{-2} − μ_{n,N}^{-2}) + O(z^4 ···)
```
The leading term:
```
γ_n^{-2} − μ_{n,N}^{-2} = γ_n^{-2} − (γ_n + c/n)^{-2}
  ≈ 2c/(n γ_n^3)   for large n.
```
So
```
Δ_N(z) ≈ z² · Σ_{n>N} 2c/(n γ_n^3).
```
Since `γ_n ∼ (n/2π) log n` (von Mangoldt), the sum
`Σ_{n>N} 1/(n γ_n^3) ∼ Σ_{n>N} 1/(n^4 (log n)^3)` converges, so the tail
contribution `Δ_N(z)` is a **nonzero constant** (for `z ≠ 0`) that **does not
tend to 0 as `N → ∞`** — in fact it tends to 0 as `N → ∞` since the tail of a
convergent series goes to 0.

**Critical issue:** With `δ_n = c/n` and `γ_n ∼ n \log n`, the sum
`Σ_{n>N} 1/(n γ_n^3)` is the tail of a series that converges, so it **does**
go to 0 as `N → ∞`.  This means `Δ_N(z) → 0` for fixed `z` — the sequence
**converges pointwise** to `Ξ` for this perturbation.  We need a **stronger**
perturbation to force non-convergence.

**Corrected construction.**  Use `δ_n = c · γ_n / n` (perturbation proportional
to `γ_n`):
```
μ_{n,N} := γ_n · (1 + c/n).
```
Then:
```
γ_n^{-2} − μ_{n,N}^{-2} = γ_n^{-2}[1 − (1+c/n)^{-2}] ≈ 2c/(n γ_n^2).
```
The tail sum becomes `Σ_{n>N} 2c/(n γ_n^2)`.  With `γ_n ∼ n \log n/2π`,
this is `Σ_{n>N} c'/n^3 \log^2 n` which still tends to 0.

**The root issue:** for a perturbation `δ_n = c · γ_n^α / n^β`, the tail
converges iff `β > 1 + 2α` (rough bound from `Σ n^{-β} γ_n^{-2(1-α)}`).
To get non-convergence of the tail, we need a **non-summable** perturbation.

**Non-summable perturbation (correct construction).**  

Take `δ_n = c · γ_n` (relative perturbation of order 1):
```
μ_{n,N} := γ_n \cdot (1 + c).
```
But then `μ_{n,N}` is a fixed scalar multiple of `γ_n` and the resulting
function `F_N` has zeros at `γ_n(1+c)` for `n > N` — this is a global rescaling
of the upper tail and does NOT depend on `N`; so all `F_N` (for large `N`) have
the same tail and the sequence converges.

**The correct approach: tail freedom via non-uniqueness.**

The key point is NOT the perturbation size for a fixed sequence, but the
**existence of multiple entire functions satisfying `ℰ_N`** that converge to
**different limits**.  

**Theorem E-neg (revised statement).** There exist two sequences `(F_N^{(1)})`,
`(F_N^{(2)})`, each satisfying `ℰ_N`, such that for every subsequence
`(F_{N_j}^{(1)})`, the locally uniform limit (if it exists) is **different from**
the locally uniform limit of `(F_{N_{j'}}^{(2)})` (if it exists).

**Proof sketch of revised version.** 

This follows from the **non-uniqueness of entire functions of order 1 with a
prescribed finite set of zeros and finitely many Taylor coefficients.**

Specifically: given any `L > 0` and any `ε > 0`, there exist entire functions
`F, G` of order 1 satisfying `ℰ_N` for the same record, with
```
F(z) ≠ G(z)   for  |z| = L.
```
This is a consequence of the infinite freedom in the tail of the Hadamard
product: the constraint `ℰ_N` fixes only `k_N` zeros and `J_N` Taylor
coefficients, leaving infinitely many zeros in the tail unconstrained.

**Quantification (proof.md §3 goal).** For `R > γ_{k_N}`, the space of
entire functions satisfying `ℰ_N` and bounded on `|z| ≤ R` by `M_R` is
**infinite-dimensional**: distinct choices of tail zeros `(μ_{n,N})_{n>k_N}`
satisfying `Σ μ_{n,N}^{-2} < ∞` and `|F_N(z)| ≤ M_R` give distinct `F_N`.
The difference `F_N^{(1)} − F_N^{(2)}` is nonzero and not controlled by `ℰ_N`.

This shows that `ℰ_N` does not identify the limit: **any limit point `G` of a
normal-family accumulation point need not equal `Ξ`.**

---

## §3. Quantitative tail estimate (OPEN — to complete)

The following estimate is needed to close E-neg rigorously:

**Claim (to prove):** For `R > 0` fixed, the set of entire functions satisfying
`ℰ_N` and `sup_{|z|≤R} |F(z)| ≤ M_R` contains elements that are `ε`-far from
`Ξ` in the sup-norm on `|z| ≤ R`, for any `ε > 0` and any `M_R`.

**Approach:** Combine:
1. The Borel–Carathéodory theorem to bound `F_N` on `|z| ≤ R` in terms of its
   real part (growth control).
2. The Hadamard product tail: show that altering the zeros `μ_{n,N}` for
   `n > k_N` while keeping `Σ μ_{n,N}^{-2} < ∞` can produce a function
   with `sup_{|z|≤R} |F_N − Ξ| ≥ ε` for any `ε`.

**Status:** PROOF-DRAFT (strategy clear; quantitative bound not yet written).

---

## §4. Proof of E-pos (sufficient convergence package)

**Given:** `(F_N)` satisfying `ℰ_N` and hypotheses (H-norm), (H-bound), (H-tail),
(H-modulus).

**Step 1 (Normal family).** By (H-bound), the family `{F_N}` is locally uniformly
bounded.  By Montel's theorem, every subsequence has a further subsequence
converging locally uniformly to some entire function `G`.

**Step 2 (Identification).** We claim `G = Ξ`.
- `G(z_0) = \lim F_{N_j}(z_0) = Ξ(z_0) ≠ 0` by (H-norm).  
- By (H-tail), the zero sequence of `F_N` converges to the zero sequence of `Ξ`
  (in the Hadamard-product sense), so `G` has the same zeros as `Ξ`.
- `G` has order 1 (uniform limit of order-1 functions with bounded norm on each
  disk).
- By the Hadamard factorization uniqueness theorem, an entire function of order 1
  is determined by its zeros up to an exponential factor `e^{az+b}`.  The
  conditions `G(z_0) = Ξ(z_0)` and `G$ even pin the factor: `G = Ξ`.

**Step 3 (Hurwitz).** Since `F_N → Ξ` locally uniformly and `Ξ` is not
identically zero, Hurwitz's theorem implies: every zero of `Ξ` is a limit of
zeros of `F_N` (with multiplicity), and every accumulation point of zeros of
`F_N` is a zero of `Ξ`.  Since all zeros of `F_N` are real (condition 4), all
zeros of `Ξ` are real.

**Note on RH:** This shows that if the convergence is proved, real zeros of
`Ξ` follow — but the theorem does not claim this is proved; it identifies the
exact hypotheses (H-bound) + (H-tail) that would complete the argument.  ☐

---

## §5. Summary

| Result | Status |
|---|---|
| E-pos (sufficient package → Ξ convergence + real zeros) | PROOF-DRAFT (standard Montel/Hurwitz; detail clear) |
| E-neg (finite evidence ≠ convergence, non-uniqueness argument) | PROOF-DRAFT (strategy clear; quantitative §3 open) |
| Quantitative tail estimate (§3) | OPEN |
| Normalization convention (CCM frozen) | DONE |
| Suzuki meromorphic target | OUT OF SCOPE for this theorem (see limitations.md) |
