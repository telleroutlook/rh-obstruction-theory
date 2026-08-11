# Limitations — Theorem D' (D-prime-logpoly)

**Theorem ID:** D-prime-logpoly  
**Finding:** ESCAPE-ROUTE-REFINED — **Gate-A BLOCKED (OB-31, 2026-08-12) for Claim A's
universal form.** The claim "the obstruction covers the full finite-log-degree `𝒞_logpoly`"
is FALSE (the class omits ellipticity; `H=(I−Δ_x)(I−Δ_y)` on `𝕋⁴` is a non-elliptic classical
counterexample with a leading `t⁻¹log(1/t)`). It survives only for the narrowed class
`𝒞_logpoly^{sub,ell}` (positive elliptic classical principal symbol + strictly-lower-order
finite log). Claims B/C/D-analytic/E confirmed; the escape class is the log-weighted
`S^{1,-1}` class; the naive exact model is refuted. See statement.md §0.

---

## What this document does NOT prove

1. **Does not produce any Hilbert–Pólya operator.** Matching the heat-trace singularity
   type (or even the two-term counting law) is necessary but far from sufficient for an
   operator to have spectrum `{γ_n}`. Infinitely many distinct spectra share a counting
   asymptotic.

2. **Does not refute Theorem D — and does NOT cover the full `𝒞_logpoly` (OB-31 correction).**
   Theorem D correctly excludes `𝒞_ell`. The leading-singularity obstruction extends **only to
   the narrowed `𝒞_logpoly^{sub,ell}`** (positive **elliptic** classical principal symbol,
   log terms strictly below principal order) — there the leading heat-trace term is a pure
   power `t^{-d/m}`, logs only subleading. It does **NOT** cover the full finite-log-degree
   `𝒞_logpoly`: without ellipticity, `H=(I−Δ_x)(I−Δ_y)` on `𝕋⁴` (positive, self-adjoint,
   classical, log-degree 0, non-elliptic) has `N_H~π²Λ log Λ` and a **leading** `t⁻¹log(1/t)`.
   So "`𝒞_logpoly` is NOT an escape" is **withdrawn**; only "`𝒞_logpoly^{sub,ell}` is not an
   escape" is (conditionally) claimed, PENDING re-review.

3. **`𝒞_logpoly` is NOT the escape class (corrected).** The earlier claim that
   `𝒞_logpoly` escapes Theorem D because `c_{0,1}` is "freely tunable to `(2π)^{-1}`" at
   leading order is **REFUTED**: a finite-log-degree operator cannot have a leading
   `t^{-1}log(1/t)` singularity. The genuine escape class is the log-*weighted* class
   `S^{1,-1}` (`|ξ|/log|ξ|`-type), outside `𝒞_ell` and `𝒞_logpoly` but inside `S¹_{1,0}`.

4. **The exact model `2πn/log(n+e)` is refuted, not merely open.** Its normalized
   counting differs from Riemann–von Mangoldt by `≍ T·log log T` (OB-16 §2.6), so it is
   not a Hilbert–Pólya candidate beyond leading order. Only the broader Lambert-`W`-
   corrected `|ξ|/log|ξ|` class remains open.

5. **Does not determine whether the log-weighted class contains a Hilbert–Pólya
   operator.** Whether an unconditional, zero-independent self-adjoint operator in the
   `S^{1,-1}` class has spectrum exactly `{γ_n}` is the open frontier — a literature-
   status statement, not an impossibility theorem, and not a claim about RH.

6. **Does not extend to non-compact manifolds or `L²(ℝ)`.** The discrete-spectrum /
   trace-class analysis requires a compact manifold (`S¹`) or an `ℓ²(ℕ)` diagonal model;
   on `L²(ℝ)` the `|ξ|/log|ξ|` Fourier multiplier has purely continuous spectrum and
   `e^{-tH}` is not trace class (OB-16 §1.1).