# Proof — Theorem D' (D-prime-logpoly)

**Status:** ESCAPE-ROUTE-REFINED (OB-01 + OB-16 external reviews, 2026-08-11): the
`𝒞_logpoly` escape computation below was REFUTED; the escape class is a
log-*weighted* symbol class, and the exact model is itself refuted. See statement.md
§3–§7 for the current verdict.  
**Analytic / finite separation:** purely analytic.

---

## §0. Correction notice (supersedes the earlier §1–§2)

The earlier version of this file attempted to show `𝒞_logpoly` is the escape class from
Theorem D by making the heat-trace log-coefficient `c_{0,1}` equal `(2π)^{-1}` at a
**leading** `t^{-1}log(1/t)` order. This is **REFUTED**:

- For `H ∈ 𝒞_logpoly` (finite nonnegative log-degree), the **leading** heat-trace
  singularity is always a **pure power** `t^{-d/m}`; log terms appear only at
  **subleading** orders `t^k log(1/t)`, `k ≥ 1` (OB-01 review; the Lesch 1999 Thm 3.7
  structure `Z_H(t) ~ Σ c_j t^{(j-d)/m} + Σ (b_k log t + d_k)t^k`, with `b_k` controlled
  by `Wres(H^k)`). So `𝒞_logpoly` cannot produce a leading `t^{-1}log(1/t)`.
- The earlier §1 "computation" of `c_{0,1}` contained draft remnants and an incorrect
  identification of the log-coefficient with a leading term; it is withdrawn in full.

The corrected escape analysis lives in statement.md §3–§7 (OB-16). This proof file now
records only the corrected structural facts.

---

## §1. Leading heat-trace singularity in 𝒞_logpoly is a pure power

**Fact (Lesch 1999 Thm 3.7, scope-checked — OB-15/OB-16).** For a positive self-adjoint
classical elliptic ΨDO `P` of order `m>0` on a closed `d`-manifold, and `A ∈ CL^{a,k}`
log-polyhomogeneous of finite log-degree `k`,
```
Tr(A e^{-tP}) ~ Σ_{j≥0} t^{(j-d-a)/m} c̃_j(log t) + Σ_{r≥0} d̃_r t^r,
```
where `deg c̃_j ≤ k` if `(j-d-a)/m ∉ ℤ≥0`, and `≤ k+1` if it is a non-negative integer.
With `A = I` (so `a=0, k=0`) and `j=0`: the exponent is `−d/m < 0`, not a non-negative
integer, so `c̃_0` is a **constant** — the leading term `t^{-d/m}` carries **no log**.

Hence no `H ∈ 𝒞_ell` and no finite-log-degree `H ∈ 𝒞_logpoly` has a leading
`t^{-d/m}log(1/t)` singularity. Subleading logs (`t^k log t`, `k≥1`, from `Wres(H^k)≠0`)
are allowed and irrelevant to the leading-order comparison with `Z_ζ`.

---

## §2. The genuine escape class (from OB-16) and why the exact model fails

**What produces a leading `t^{-1}log(1/t)`.** By the Abelian/Karamata correspondence, a
leading heat singularity `Z_H(t) ~ c·t^{-1}log(1/t)` is equivalent to a counting law
`N_H(T) ~ c·T·log T`. This requires eigenvalues `λ_n ~ n/log n`, i.e. a symbol growing
like `|ξ|/log|ξ|` — a **log-weighted** class `S^{1,-1}` (elliptic w.r.t. the weight
`w(ξ)=⟨ξ⟩/log(e+⟨ξ⟩)`), **outside** `𝒞_ell` and outside finite-log-degree `𝒞_logpoly`,
but **inside** the ordinary Hörmander class `S¹_{1,0}` (OB-16 §2, §6). So `𝒞_logpoly` is
NOT the escape class; the log-weighted class is.

**The exact model `λ_n = 2πn/log(n+e)` is refuted (OB-16 §2.6).** On `S¹`/`ℓ²(ℕ)`
(NOT `L²(ℝ)`, where the multiplier has continuous spectrum and is not trace class), the
count differs from Riemann–von Mangoldt at the next scale:
```
N_{2π}^+(T) − N_ζ(T) = (T/2π)[log log(T/2π) + 1 + o(1)] ≍ T·log log T.
```
Equal discrete spectra (with multiplicity) force equal counting functions; the
`T log log T` discrepancy excludes the exact model as a Hilbert–Pólya candidate.

**What stays open (OB-16 §4).** A Lambert-`W`-corrected symbol `g(r)=2πr/W(r/e)` matches
even the two-term smooth law `(T/2π)(log(T/2π)−1)` exactly at the continuous-inverse
level (it does not reproduce the `O(log T)` remainder, spacings, multiplicities, or zero
locations). Whether an unconditional, zero-independent self-adjoint operator in this
broader log-weighted class has spectrum exactly `{γ_n}` is the open Hilbert–Pólya
frontier — a literature-status statement, not an impossibility theorem.

---

## §3. Status

| Step | Status |
|---|---|
| Earlier §1 c_{0,1}=(2π)^{-1} "escape via 𝒞_logpoly" | **REFUTED / WITHDRAWN** (OB-01, OB-16): 𝒞_logpoly leading term is a pure power; logs are subleading only |
| Leading singularity of 𝒞_ell / 𝒞_logpoly is pure power `t^{-d/m}` | PROOF-DRAFT ✓ (Lesch 1999 Thm 3.7, A=I, j=0 exponent −d/m ∉ ℤ≥0) |
| Escape class = log-weighted `S^{1,-1}` (`|ξ|/log|ξ|`), outside 𝒞_ell/𝒞_logpoly, inside `S¹_{1,0}` | PROOF-DRAFT ✓ (OB-16 §2, §6) |
| Exact model `2πn/log(n+e)` as HP candidate | **REFUTED** — differs from N_ζ by ≍ T log log T (OB-16 §2.6) |
| Broader `W`-corrected `\|ξ\|/log\|ξ\|` class | OPEN / localized — matches two-term law; zero-independent spectral realization unknown (OB-16 §4) |
| Hilbert space for the model | `S¹`/`ℓ²(ℕ)`, NOT `L²(ℝ)` (continuous spectrum, not trace class) — OB-16 §1.1 |