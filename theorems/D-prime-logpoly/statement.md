# Statement — Theorem D' (D-prime-logpoly)

**Theorem ID:** D-prime-logpoly  
**Program ref:** EXT-1 (extension of Theorem D; audit of log-polyhomogeneous escape route)  
**Status:** ESCAPE-ROUTE-OPEN (confirmed; see §3)

---

## §1. Context and question

Theorem D (D-spectral-asymptotic) proves that no operator in the class 𝒞_ell (positive
elliptic pseudodifferential operators of any order on any compact smooth manifold) can
have spectrum equal to the Riemann zero ordinates `{γ_n}`. The obstruction is that
𝒞_ell operators have polyhomogeneous Seeley–DeWitt heat-trace expansions with no
`log(1/t)` terms, while `Z_ζ(t) ∼ (1/2π)·log(1/t)/t`.

Theorem D explicitly lists **log-polyhomogeneous operators** as an escape route (escape
item 3 of Theorem D, statement.md §Escape routes).

This document audits that escape route by asking: does the log-polyhomogeneous class
𝒞_logpoly (Schrohe 1992, Lesch 1995, Grubb–Seeley 1995) necessarily fail to reproduce
`Z_ζ(t) ∼ (1/2π)·log(1/t)/t`, or is it a live candidate?

---

## §2. The class 𝒞_logpoly

**Definition.** `H ∈ 𝒞_logpoly` if:
- `H` is a pseudodifferential operator of order `m > 0` on a compact smooth manifold `M`
  of dimension `d`;
- the symbol of `H` has a log-polyhomogeneous expansion:
  ```
  σ(H)(x,ξ) ~ Σ_j (σ_{m-j}(x,ξ) + τ_{m-j}(x,ξ)·log|ξ|)   as |ξ| → ∞,
  ```
  where `σ_{m-j}` is positively homogeneous of degree `m-j` and `τ_{m-j}` is
  positively homogeneous of degree `m-j`.

This class strictly contains 𝒞_ell (when all `τ_k = 0`).

**Key examples:**
- Powers `H^z` for complex `z` (Seeley's complex powers), expanded around non-integer `z`.
- The operator `log H` for `H ∈ 𝒞_ell`.
- Parametrix contributions involving log-symbols in the Grubb–Seeley resolvent calculus.

---

## §3. Heat-trace expansion (REFEREED result)

**Theorem (Schrohe 1992; Lesch 1995; Grubb–Seeley 1995).** For `H ∈ 𝒞_logpoly` of
order `m > 0` on a compact `d`-manifold:
```
Z_H(t) ~ Σ_{j≥0} Σ_{k=0}^{K_j} c_{j,k} · t^{(j−d)/m} · (log(1/t))^k   as t → 0+,
```
where `c_{j,0}` are the classical Seeley–DeWitt coefficients and `c_{j,k}` for `k ≥ 1`
are determined by the log-symbol components `τ_{m-j}`. In particular, the leading
log-term is:
```
c_{0,1} = (1/(m·(2π)^d)) · ∫_M ∫_{S^{d−1}} τ_m(x,ω) dω dx,
```
and the leading singularity of the heat trace is:
```
Z_H(t) ~ c_{0,0} · t^{−d/m} + c_{0,1} · t^{−d/m} · log(1/t) + lower order.
```

---

## §4. Escape-route verdict: CONFIRMED OPEN

**Claim.** The log-polyhomogeneous class 𝒞_logpoly is a **genuinely open escape route**
from Theorem D. The obstacle to Theorem D's extension to 𝒞_logpoly is:

1. **Singularity type matches:** For `d = 1, m = 1`, the leading term is
   `c_{0,1} · t^{-1} · log(1/t)`, which is exactly the same type as
   `Z_ζ(t) ∼ (1/2π) · log(1/t)/t`.

2. **Coefficient is freely tunable:** The coefficient `c_{0,1}` is determined by the
   log-symbol `τ_1(x,ω)` via a cosphere integral. In particular, on the circle `S^1`
   (d = 1, m = 1), choosing `τ_1(x,ω) = 1` gives `c_{0,1} = (2π)^{-1}`.

3. **No further constraint from compactness:** The log-polyhomogeneous calculus does not
   impose a sign or rationality constraint on `c_{0,1}` that would prevent it from
   equaling `(2π)^{-1}`.

**Consequence.** The heat-trace singularity method of Theorem D **cannot** be extended to
exclude all of 𝒞_logpoly. The coefficient `c_{0,1} = (2π)^{-1}` is achievable by
choosing `τ_1 ≡ 1` on `S^1`, and Theorem D's argument breaks down at this point.

---

## §5. What this does NOT say

1. **Does not produce a Hilbert–Pólya operator:** Having the right heat-trace singularity
   type is necessary but far from sufficient. The spectrum of any `H ∈ 𝒞_logpoly` is
   not known to equal `{γ_n}` — that would require additionally:
   - the Weyl law matching `N_H(T) ~ T log T / (2π)` (the leading counting function),
   - the individual eigenvalues matching the Riemann zeros,
   - positive self-adjointness in a compatible Hilbert space.

2. **Does not refute Theorem D:** Theorem D correctly excludes 𝒞_ell. The escape route
   is real and was always declared in Theorem D's statement; this document confirms it.

3. **Does not assert any log-polyhomogeneous operator has spectrum {γ_n}:** This is an
   open question. The escape route is open; the question of whether it is traversable
   is a different (and harder) problem.

---

## §6. New research question (opened by this audit)

**Can a log-polyhomogeneous operator be constructed from zero-free arithmetic data
such that its spectrum is {γ_n}?**

Sub-questions:
- Is there any structural obstruction to log-polyhomogeneous operators having
  spectrum with `T log T` counting beyond the singularity-type match?
  (E.g., is the Weyl law for 𝒞_logpoly still polynomial `T^{d/m}`, just with the
  log factor coming from the symbol rather than the counting function?)
- If the Weyl law for 𝒞_logpoly can be `T log T` (not just `T^{d/m}·log T`), then
  this class is a live Hilbert–Pólya candidate and warrants dedicated investigation.

**This is recorded as a CONJECTURE and a future research direction, not a theorem.**

---

## §7. Status summary

| Component | Status |
|---|---|
| Log-polyhomogeneous heat-trace expansion (§3) | REFEREED (Schrohe 1992, Lesch 1995, Grubb–Seeley 1995) |
| Singularity-type match for d=1, m=1 (§4) | PROOF-DRAFT (computation from §3 formula) |
| Coefficient tunability to (2π)^{-1} (§4) | PROOF-DRAFT (immediate from §3 formula) |
| Escape route verdict: OPEN | CONFIRMED (see §4) |
| Weyl law for 𝒞_logpoly (§6 open question) | OPEN — not yet analyzed |
| Spectrum = {γ_n} for some H ∈ 𝒞_logpoly | OPEN CONJECTURE |
