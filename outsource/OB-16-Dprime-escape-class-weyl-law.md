# Problem OB-16 — D': does a |ξ|/log|ξ|-type symbol yield the T·log T counting law, and is it outside 𝒞_ell?

**Type:** analysis / spectral theory (Weyl law, symbol classes, self-adjoint operators)

**Non-circularity:** RH is not assumed and is not used. Zero locations of ζ are never
read. The Riemann object enters only as the *counting-law shape* `N(T) ~ (T/2π)log T` to
be matched; matching a counting-law shape is not assuming RH (it does not place any zero
anywhere). This problem asks whether a specific symbol growth reproduces that shape and
whether the resulting operator lies outside the class `𝒞_ell` already excluded by
Theorem D.

---

## Background (why this class)

Theorem D (corrected, leading-singularity version) excludes every positive classical
elliptic ΨDO `H ∈ 𝒞_ell` from having spectrum `{γ_n}`: such `H` have pure-power leading
heat-trace singularity `t^{-d/m}`, while `Z_ζ(t) ~ (1/2π)log(1/t)/t`. The corrected D'
audit (OB-01) found that the *escape* class — operators whose heat trace has a
`t^{-1}log(1/t)` leading singularity — is NOT `𝒞_logpoly` (log-polyhomogeneous operators
still have pure-power leading terms). The escape requires eigenvalue counting
`N_H(T) ~ C·T·log T`, corresponding to a symbol growing like `|ξ|/log|ξ|`. This problem
audits that candidate escape class.

---

## All definitions (self-contained — everything is here)

### The candidate operator (1-dimensional model)

On `L²(ℝ)` (or `ℓ²(ℤ)` via Fourier series on `S¹`), consider a self-adjoint operator `H`
defined by a real, positive symbol `h(ξ)` that is a Fourier multiplier:
```
(Hf)^(ξ) = h(ξ) f̂(ξ),      h(ξ) = |ξ| / log(|ξ| + e)   for |ξ| large,
```
with `h` smoothed to be positive and smooth near `ξ = 0` (exact behavior near 0 is
irrelevant to the leading Weyl asymptotics). On `S¹` with integer frequencies `n ∈ ℤ`,
the eigenvalues are
```
λ_n = |n| / log(|n| + e),   n ∈ ℤ  (doubly counted for ±n; use n ≥ 1 with multiplicity 2,
or restrict to a half-line model with λ_n = n/log(n+e), n ≥ 1).
```

### The counting function and the target shape

```
N_H(T) := #{ eigenvalues λ ≤ T }   (with multiplicity).
```
Target shape (Riemann–von Mangoldt, unconditional): `N(T) = (T/2π)log(T/2π) − T/2π +
O(log T)`, i.e. `N(T) ~ (1/2π) T log T` to leading order. We test whether `N_H(T)` has the
same leading order `T log T` (up to the constant, which is symbol-dependent and can be
normalized).

### The class 𝒞_ell (for the "outside" check)

`H ∈ 𝒞_ell` iff `H` is a positive self-adjoint classical (polyhomogeneous)
pseudodifferential operator of some order `m > 0` on a closed manifold of dimension `d`,
i.e. its symbol has an asymptotic expansion into terms **positively homogeneous** of
integer-spaced decreasing degrees `m, m-1, m-2, …`. For such `H`, `N_H(T) ~ C_H T^{d/m}`
(a pure power).

---

## The claims to be verified

### Claim A: the symbol |ξ|/log|ξ| gives N_H(T) ~ T·log T

**Claim A.** For `λ_n = n / log(n + e)` (`n ≥ 1`), the counting function satisfies
```
N_H(T) = #{n ≥ 1 : n/log(n+e) ≤ T} ~ T · log T   as T → ∞
```
to leading order (matching the Riemann–von Mangoldt *shape* up to the constant).

**What to close for Claim A:**
Invert `λ = n/log(n+e)`. For large `n`, `n ≈ λ log n ≈ λ log(λ log λ) ≈ λ(log λ +
log log λ)`, so the largest `n` with `λ_n ≤ T` is `n*(T) ~ T log T · (1 + o(1))`. Give
the rigorous leading asymptotic `N_H(T) = T log T (1 + o(1))` (or the sharper
`N_H(T) = T(log T + log log T + …)`), and compare its leading order with
`(1/2π) T log T`. State clearly whether the match is: leading-order-equal (both `~ c·T log T`),
or differs at the `T log log T` level. (The referee-checked OB-07 finding was that the
naive `2πn/log n` inversion has a `T log log T` discrepancy from `T log T − T`; determine
whether that discrepancy also afflicts this symbol, and whether it is a leading-order
obstruction or a lower-order one.)

### Claim B: the resulting heat trace has leading singularity t^{-1}·log(1/t)

**Claim B.** With `N_H(T) ~ c·T log T`, the heat trace `Z_H(t) = Σ e^{-tλ_n}` satisfies
```
Z_H(t) ~ c · t^{-1} log(1/t)   as t → 0⁺,
```
by a Karamata / Abel-summation argument (same computation as `Z_ζ` in OB-15 Step 3).

**What to close for Claim B:**
Confirm that `N_H(T) ~ c T log T` implies `Z_H(t) ~ c t^{-1} log(1/t)` via
`Z_H(t) = t∫_0^∞ e^{-tu} N_H(u) du`, and that this is the **leading** singularity (a
genuine `t^{-1}log(1/t)`, not a pure power). This is what makes the class an escape from
Theorem D's leading-log obstruction.

### Claim C: this H is OUTSIDE 𝒞_ell (and outside 𝒞_logpoly)

**Claim C.** The symbol `h(ξ) = |ξ|/log|ξ|` is not a classical polyhomogeneous symbol of
any order `m > 0`; hence `H ∉ 𝒞_ell`. It is also not log-polyhomogeneous of finite
log-degree (`𝒞_logpoly`), because `1/log|ξ|` is not a finite sum of homogeneous ×
`(log|ξ|)^k` terms.

**What to close for Claim C:**
1. Show `|ξ|/log|ξ|` is not positively homogeneous of any degree, and is not a finite sum
   `Σ_j σ_{m-j}(ξ)` with `σ` homogeneous — because `h(2ξ)/h(ξ) = 2·log(|ξ|+e)/log(2|ξ|+e)
   → 2` but with a slowly-varying correction incompatible with exact degree-1 homogeneity
   at any finite order.
2. Show it is not in `𝒞_logpoly` (finite log-degree): `1/log|ξ|` has an infinite expansion
   `Σ_k c_k (log|ξ|)^{-k}`... — clarify that `𝒞_logpoly` as usually defined allows
   *positive* powers of `log|ξ|` times homogeneous symbols, not `(log|ξ|)^{-1}`; so `h` is
   outside it. State which symbol class (if any standard one) contains `h` — e.g. the
   "slowly varying" or Grushin/SG classes — or confirm it is outside all standard calculi.
3. Conclude: `H` escapes Theorem D because D's hypothesis (`H ∈ 𝒞_ell`) fails.

### Claim D (the genuinely open part): can such an H realize spectrum {γ_n}?

**Claim D (EXPLORATORY — inconclusive is an acceptable outcome).** Matching the
*counting-law shape* `T log T` is necessary but far from sufficient to have spectrum
*equal to* `{γ_n}`. Determine what is known:
- Does matching `N_H(T) ~ N_ζ(T)` to leading order constrain the actual eigenvalues
  `λ_n` beyond their counting density? (No — infinitely many spectra share a counting
  asymptotic.)
- Is there any known self-adjoint operator, built from a `|ξ|/log|ξ|`-type symbol WITHOUT
  reading zero ordinates, whose spectrum is exactly `{γ_n}`? (Expected answer: NO known
  construction; this is the Hilbert–Pólya problem and is open.)

**What to verify for Claim D:**
State precisely and honestly: (i) counting-law match is a *necessary* condition that this
class *can* meet (unlike 𝒞_ell); (ii) it is *not sufficient* for spectral equality;
(iii) no construction achieving spectral equality is known, and building one from first
principles (no zero input) is open. This is a **localization of the open frontier**, not a
theorem.

---

## Acceptance criteria

1. **CONFIRMED (partial-by-design):** Claims A, B, C are proved (counting law, heat-trace
   leading log, outside 𝒞_ell/𝒞_logpoly); Claim D is honestly localized as open. This is
   the target outcome — it establishes the escape class is real and correctly places the
   Hilbert–Pólya frontier.

2. **PARTIAL:** A–C mostly confirmed with a precise gap (e.g. the exact constant in the
   Weyl law, or the exact symbol-class membership of `h`).

3. **REFUTED:** if `|ξ|/log|ξ|` does NOT give `T log T` counting (e.g. the `log log`
   correction changes the leading order), or if it is secretly in `𝒞_ell`/`𝒞_logpoly`,
   give the corrected asymptotic / classification.

4. **INCONCLUSIVE + localization:** for Claim D especially — "counting-law match is
   achievable in this class but spectral realization is open" is the expected and
   acceptable conclusion. Do NOT force a prove/disprove dichotomy on the Hilbert–Pólya
   question.

This problem does **not** ask to prove or disprove RH, nor to construct a Hilbert–Pólya
operator. It asks to verify that the escape class from Theorem D is real (can match the
counting law), correctly classify it (outside 𝒞_ell), and honestly localize what remains
open.

---

## Numerical anchor (sanity only — not an input)

For `λ_n = n/log(n+e)`, the counting `N_H(T) = #{n : n/log(n+e) ≤ T}` versus the sharp
fixed-point inverse `n* = T·log(n*)` (iterated): at `T = 10³, 10⁴, 10⁵, 10⁶` the ratios
`N_H(T)/(T log n*)` are `0.9999, 1.0000, 1.0000, 1.0000` — so `N_H(T) ~ T log n* ~ T log T`
to leading order, confirming the `T log T` shape. (Naive `T log T` alone is off by a
slowly-varying `log log` factor — ratio `≈ 1.27` at `T=10⁴` — which is exactly the
`log log` correction Claim A must address; the sharp fixed point removes it.)
Script-verified. This anchor sanity-checks Claim A's leading order only; the symbol-class
membership (Claim C) and the open Hilbert–Pólya localization (Claim D) are the analytic
content.
