# Limitations — Theorem D' (D-prime-logpoly)

**Theorem ID:** D-prime-logpoly  
**Finding:** ESCAPE-ROUTE-REFINED (OB-01 + OB-16, 2026-08-11): `𝒞_logpoly` is NOT the
escape class; the escape class is a log-weighted `S^{1,-1}` symbol class, and the naive
exact model is refuted.

---

## What this document does NOT prove

1. **Does not produce any Hilbert–Pólya operator.** Matching the heat-trace singularity
   type (or even the two-term counting law) is necessary but far from sufficient for an
   operator to have spectrum `{γ_n}`. Infinitely many distinct spectra share a counting
   asymptotic.

2. **Does not refute Theorem D.** Theorem D correctly excludes `𝒞_ell`, and — after the
   OB-01/OB-16 correction — the leading-singularity obstruction **also covers**
   `𝒞_logpoly` (finite log-degree): its leading heat-trace term is a pure power
   `t^{-d/m}`, logs appear only subleading. So `𝒞_logpoly` is NOT an escape.

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