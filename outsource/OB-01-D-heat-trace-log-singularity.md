# Problem OB-01 — Heat-trace log singularity: no-log Seeley-DeWitt theorem

**Type:** Classical spectral theory / PDE. Tractable by a specialist in heat-kernel
theory or pseudodifferential operators.  
**Repo context:** This is an independent verification request for one step in Theorem D
(`theorems/D-spectral-asymptotic/`) of the RH Obstruction Theory repository. You do NOT
need any other file from that repo to solve this problem.

---

## Self-contained setup

Let `M` be a compact smooth Riemannian manifold of dimension `d ≥ 1` without boundary,
and let `H` be a classical positive-definite elliptic pseudodifferential operator on `M`
of positive order `m > 0` with positive spectrum `{λ_n}_{n≥1}`, `λ_n → +∞`.

Define the **operator heat trace**:
```
Z_H(t) := Tr(e^{−tH}) = Σ_{n≥1} e^{−t λ_n},   t > 0.
```

The claim to be verified:

**Theorem (Seeley-DeWitt, no-log).** As `t → 0⁺`,
```
Z_H(t) ~ Σ_{k=0}^∞ a_k t^{(k−d)/m},
```
where each `a_k` is a local geometric invariant of `(M, H)` and **no term of the form
`t^α log(1/t)` (with any real `α`) appears in this asymptotic expansion.**

More precisely: for every `K ≥ 0` there is a remainder bound
```
Z_H(t) − Σ_{k=0}^{K} a_k t^{(k−d)/m} = O(t^{(K+1−d)/m})   as t → 0⁺,
```
with **no logarithmic correction term**.

---

## Why this matters for Theorem D

The Riemann zeta function zero-counting function satisfies (Riemann-von Mangoldt):
```
N_ζ(T) := #{n : γ_n ≤ T} = T/(2π) log(T/2π) − T/(2π) + O(log T),
```
where `{γ_n}` are the positive imaginary parts of nontrivial zeros (with multiplicity).

By Abel-Plana / partial summation from this counting function:
```
Z_ζ(t) := Σ_{n≥1} e^{−t γ_n} = (1/(2π)) · log(1/t)/t + O(1/t)   as t → 0⁺.   (*)
```
(This computation is self-contained: `t ∫_0^∞ e^{-tu} (u log u)/(2π) du` splits as
`log(1/t)/t · (2π)^{-1} ∫_0^∞ e^{-v}v dv + O(1/t) = log(1/t)/(t·2π) + O(1/t)`.)

The term `log(1/t)/t` in `(*)` is a `t^{-1} log(1/t)` singularity type.  
The Seeley-DeWitt theorem says `Z_H(t)` for any `H ∈ 𝒞_ell` has only `t^{(k-d)/m}`
terms — no logarithms. Therefore no elliptic operator on a compact manifold can have
spectrum `{γ_n}`.

---

## What we need verified

**Verify, with source citation by exact theorem number:**

1. **(Statement A — no-log expansion):** The asymptotic expansion of `Tr(e^{-tH})` as
   `t → 0⁺` for `H` a classical elliptic operator of order `m` on a compact manifold
   of dimension `d` is of the form `Σ_k a_k t^{(k-d)/m}` with no logarithmic terms.

   **Acceptable sources (any of the following):**
   - Berline-Getzler-Vergne, *Heat Kernels and Dirac Operators* (Springer). Cite the
     theorem number that gives the heat kernel expansion with no log terms. The version
     cited in our proof draft is "Thm 2.30" — please verify whether this is the correct
     theorem number in the standard edition, or supply the correct reference.
   - Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem*
     (2nd ed., CRC Press). The draft cites "Thm 1.8.1" — please verify.
   - Seeley, "Complex powers of an elliptic operator," *AMS Symp. Pure Math.* 10 (1967).
   - Any standard reference giving the full asymptotic expansion with explicit no-log
     statement.

2. **(Statement B — extension to manifolds with boundary, if needed):** State whether
   the no-log property extends to the case where `M` has a boundary (with standard
   elliptic boundary conditions). If it does, cite the theorem. If it does not (i.e.
   logarithmic terms can appear for manifolds with boundary), state the exact condition
   that prevents them, and note that Theorem D applies only to the without-boundary case
   (or to the without-boundary subclass).

3. **(Statement C — log-polyhomogeneous exception):** Confirm that for the class of
   **log-polyhomogeneous** operators (symbols of the form
   `σ_{m-j}(x,ξ) + τ_{m-j}(x,ξ) log|ξ|` as `|ξ| → ∞`), the heat-trace expansion
   **does** acquire logarithmic terms. Specifically: does the leading singular term in
   `Tr(e^{-tH_{logpoly})` for `d=1, m=1` take the form `c · t^{-1} log(1/t)` for some
   computable constant `c` depending on the leading log-symbol coefficient? Cite Schrohe
   (1992), Lesch (1995), or Grubb-Seeley (1995).

---

## Acceptance criteria

1. A precise statement of the no-log theorem for `𝒞_ell` with the exact source
   theorem number (fixing or confirming "BGV Thm 2.30" and/or "Gilkey Thm 1.8.1").
2. Confirmation or correction of the without-boundary restriction.
3. Confirmation that `𝒞_logpoly` does acquire `log(1/t)/t` terms (or a precise
   statement of when it does), with citation.
4. If any of Statements A–C is false as stated, an explicit counterexample or
   correction.
5. No reference to Riemann zeta zero locations, RH, or any numerical zero table.

---

## Why this is not an RH-level problem

This is a **pure spectral theory question** about the heat-kernel expansion of elliptic
operators. It has nothing to do with the Riemann Hypothesis. The answers are known in
the literature; what is needed is precise citation verification (which theorem number,
which edition, which conditions). The main risk is that the BGV/Gilkey theorem numbers
cited in the draft are off by one or refer to a different edition.
